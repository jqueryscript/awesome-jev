#!/usr/bin/env python3
"""Validate Jev research data and render the public resource sections."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent
CANDIDATES_PATH = ROOT / "candidates.json"
VERIFIED_PATH = ROOT / "verified-items.json"
REJECTED_PATH = ROOT / "rejected-items.json"
ARTICLE_PATH = ROOT / "article.md"
README_PATH = ROOT / "README.md"
ARTICLE_START = "<!-- BEGIN GENERATED ARTICLE RESOURCES -->"
ARTICLE_END = "<!-- END GENERATED ARTICLE RESOURCES -->"
README_START = "<!-- BEGIN GENERATED README RESOURCES -->"
README_END = "<!-- END GENERATED README RESOURCES -->"

CATEGORIES = (
    "Official Jev resources",
    "SDKs and API clients",
    "Gateways and integrations",
    "Agent tools and MCP servers",
    "Browser and computer-use agents",
    "Applications and developer tools",
    "Open System One implementations",
    "Benchmarks and evaluations",
    "Examples and learning resources",
    "Community resources",
)
OFFICIALITY = {"official", "community", "independent"}
RELATIONSHIPS = {
    "direct",
    "official_resource",
    "independent_implementation",
    "community_resource",
}
ACTIVITY = {"active", "experimental", "archived", "stale", "broken", "unknown"}
STATUSES = {"include", "reject", "needs_review"}
REJECTION_REASONS = {
    "duplicate",
    "fork_without_material_difference",
    "jev_only_mentioned",
    "no_working_code",
    "insufficient_evidence",
    "unrelated",
    "abandoned",
    "spam",
    "generated_placeholder",
    "broken",
    "misleading_claim",
    "other",
}
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ARTICLE_DATE_PATTERN = re.compile(r"(?m)^\*Last updated: [A-Z][a-z]+ \d{1,2}, \d{4}\.\*$")
README_SUMMARY_PATTERN = re.compile(
    r"\*\*Last verified:\*\* \d{4}-\d{2}-\d{2} · "
    r"\*\*Resources:\*\* \d+ · \*\*Categories:\*\* \d+"
)
REQUIRED_FIELDS = {
    "id",
    "name",
    "canonical_url",
    "github_url",
    "official_or_community",
    "creator_or_org",
    "category",
    "subcategory",
    "short_description",
    "what_jev_does_here",
    "jev_relationship",
    "language_or_stack",
    "license",
    "activity_status",
    "discovered_at",
    "last_verified",
    "evidence_urls",
    "duplicate_of",
    "fork_of",
    "quality_notes",
    "verification_notes",
    "status",
    "rejection_reason",
}


class ValidationError(ValueError):
    """Raised when the research data or rendered output is invalid."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValidationError(f"cannot read {path.name}: {error}") from error
    if not isinstance(value, dict):
        raise ValidationError(f"{path.name} must contain an object")
    return value


def validate_date(value: Any, field: str) -> None:
    if not isinstance(value, str) or not DATE_PATTERN.fullmatch(value):
        raise ValidationError(f"{field} must use YYYY-MM-DD")
    try:
        dt.date.fromisoformat(value)
    except ValueError as error:
        raise ValidationError(f"{field} is not a valid date") from error


def validate_url(value: Any, field: str, *, allow_empty: bool = False) -> None:
    if allow_empty and value == "":
        return
    if not isinstance(value, str):
        raise ValidationError(f"{field} must be a string")
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc or parsed.fragment:
        raise ValidationError(f"{field} must be a fragment-free HTTPS URL")


def validate_sentence(value: Any, field: str) -> None:
    if (
        not isinstance(value, str)
        or len(value) < 20
        or "\n" in value
        or not value.endswith(".")
    ):
        raise ValidationError(f"{field} must be a one-line factual sentence ending in a period")


def validate_record(item: Any, index: int) -> None:
    if not isinstance(item, dict):
        raise ValidationError(f"item {index} must be an object")
    missing = REQUIRED_FIELDS - item.keys()
    extra = item.keys() - REQUIRED_FIELDS
    if missing:
        raise ValidationError(f"item {index} is missing: {', '.join(sorted(missing))}")
    if extra:
        raise ValidationError(f"item {index} has unknown fields: {', '.join(sorted(extra))}")

    item_id = item["id"]
    if not isinstance(item_id, str) or not ID_PATTERN.fullmatch(item_id):
        raise ValidationError(f"item {index} has an invalid id")
    for field in ("name", "creator_or_org", "license", "quality_notes", "verification_notes"):
        value = item[field]
        if not isinstance(value, str) or not value.strip() or value != value.strip():
            raise ValidationError(f"{item_id}.{field} must be a nonempty trimmed string")
    if not isinstance(item["subcategory"], str) or item["subcategory"] != item["subcategory"].strip():
        raise ValidationError(f"{item_id}.subcategory must be a trimmed string")

    validate_url(item["canonical_url"], f"{item_id}.canonical_url")
    validate_url(item["github_url"], f"{item_id}.github_url", allow_empty=True)
    validate_sentence(item["short_description"], f"{item_id}.short_description")
    validate_sentence(item["what_jev_does_here"], f"{item_id}.what_jev_does_here")
    validate_date(item["discovered_at"], f"{item_id}.discovered_at")
    validate_date(item["last_verified"], f"{item_id}.last_verified")

    if item["official_or_community"] not in OFFICIALITY:
        raise ValidationError(f"{item_id} has invalid official_or_community")
    if item["category"] not in CATEGORIES:
        raise ValidationError(f"{item_id} has invalid category")
    if item["jev_relationship"] not in RELATIONSHIPS:
        raise ValidationError(f"{item_id} has invalid jev_relationship")
    if item["activity_status"] not in ACTIVITY:
        raise ValidationError(f"{item_id} has invalid activity_status")
    if item["status"] not in STATUSES:
        raise ValidationError(f"{item_id} has invalid status")

    stack = item["language_or_stack"]
    if not isinstance(stack, list) or not stack or any(not isinstance(v, str) or not v.strip() for v in stack):
        raise ValidationError(f"{item_id}.language_or_stack must be a nonempty string array")
    if len(stack) != len({value.casefold() for value in stack}):
        raise ValidationError(f"{item_id}.language_or_stack contains duplicates")

    evidence = item["evidence_urls"]
    if not isinstance(evidence, list) or not evidence:
        raise ValidationError(f"{item_id}.evidence_urls must be nonempty")
    for evidence_index, url in enumerate(evidence):
        validate_url(url, f"{item_id}.evidence_urls[{evidence_index}]")
    if len(evidence) != len(set(evidence)):
        raise ValidationError(f"{item_id}.evidence_urls contains duplicates")

    for field in ("duplicate_of", "fork_of"):
        if item[field] is not None and (not isinstance(item[field], str) or not item[field].strip()):
            raise ValidationError(f"{item_id}.{field} must be null or a nonempty string")

    reason = item["rejection_reason"]
    if item["status"] == "reject":
        if reason not in REJECTION_REASONS:
            raise ValidationError(f"{item_id} must have an allowed rejection_reason")
    elif reason is not None:
        raise ValidationError(f"{item_id} must not have a rejection_reason")

    if item["status"] == "include":
        if item["activity_status"] in {"archived", "stale", "broken", "unknown"}:
            raise ValidationError(f"included item {item_id} must be active or experimental")
        if item["duplicate_of"] is not None:
            raise ValidationError(f"included item {item_id} cannot be a duplicate")


def validate_dataset(data: dict[str, Any], label: str) -> list[dict[str, Any]]:
    if data.get("schema_version") != "1.0":
        raise ValidationError(f"{label}.schema_version must be 1.0")
    validate_date(data.get("last_updated"), f"{label}.last_updated")
    if set(data.keys()) != {"schema_version", "last_updated", "items"}:
        raise ValidationError(f"{label} must contain only schema_version, last_updated, and items")
    items = data["items"]
    if not isinstance(items, list):
        raise ValidationError(f"{label}.items must be an array")
    for index, item in enumerate(items, start=1):
        validate_record(item, index)
    return items


def item_signature(item: dict[str, Any]) -> str:
    return json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def derive_partitions() -> tuple[dict[str, Any], dict[str, Any]]:
    candidates_data = load_json(CANDIDATES_PATH)
    candidates = validate_dataset(candidates_data, "candidates")
    verified = sorted(
        (item for item in candidates if item["status"] == "include"),
        key=lambda item: (CATEGORIES.index(item["category"]), item["name"].casefold()),
    )
    rejected = sorted(
        (item for item in candidates if item["status"] == "reject"),
        key=lambda item: item["id"],
    )
    metadata = {
        "schema_version": candidates_data["schema_version"],
        "last_updated": candidates_data["last_updated"],
    }
    return ({**metadata, "items": verified}, {**metadata, "items": rejected})


def json_text(value: dict[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def validate_repository() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    candidates_data = load_json(CANDIDATES_PATH)
    verified_data = load_json(VERIFIED_PATH)
    rejected_data = load_json(REJECTED_PATH)
    candidates = validate_dataset(candidates_data, "candidates")
    verified = validate_dataset(verified_data, "verified")
    rejected = validate_dataset(rejected_data, "rejected")

    dates = {candidates_data["last_updated"], verified_data["last_updated"], rejected_data["last_updated"]}
    if len(dates) != 1:
        raise ValidationError("all dataset files must have the same last_updated date")

    ids: set[str] = set()
    urls: set[str] = set()
    for item in candidates:
        folded_id = item["id"].casefold()
        folded_url = item["canonical_url"].rstrip("/").casefold()
        if folded_id in ids:
            raise ValidationError(f"duplicate candidate id: {item['id']}")
        if folded_url in urls:
            raise ValidationError(f"duplicate candidate canonical URL: {item['canonical_url']}")
        ids.add(folded_id)
        urls.add(folded_url)

    expected_verified = {item_signature(i) for i in candidates if i["status"] == "include"}
    expected_rejected = {item_signature(i) for i in candidates if i["status"] == "reject"}
    actual_verified = {item_signature(i) for i in verified}
    actual_rejected = {item_signature(i) for i in rejected}
    if expected_verified != actual_verified:
        raise ValidationError("verified-items.json is not the exact include partition")
    if expected_rejected != actual_rejected:
        raise ValidationError("rejected-items.json is not the exact reject partition")
    if any(item["status"] != "include" for item in verified):
        raise ValidationError("verified-items.json contains a non-include record")
    if any(item["status"] != "reject" for item in rejected):
        raise ValidationError("rejected-items.json contains a non-reject record")

    needs_review = sum(item["status"] == "needs_review" for item in candidates)
    if len(candidates) != len(verified) + len(rejected) + needs_review:
        raise ValidationError("candidate partition count is inconsistent")
    return candidates, verified, rejected


def grouped_items(items: list[dict[str, Any]]) -> list[tuple[str, list[dict[str, Any]]]]:
    result: list[tuple[str, list[dict[str, Any]]]] = []
    for category in CATEGORIES:
        category_items = sorted(
            (item for item in items if item["category"] == category),
            key=lambda item: item["name"].casefold(),
        )
        if category_items:
            result.append((category, category_items))
    return result


def render_article(items: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for category, category_items in grouped_items(items):
        lines.extend((f"## {category}", ""))
        for item in category_items:
            lines.append(
                f"- **[{item['name']}]({item['canonical_url']})**: {item['what_jev_does_here']}"
            )
        lines.append("")
    return "\n".join(lines).rstrip()


def render_readme(items: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    groups = grouped_items(items)
    lines.extend(("## Contents", ""))
    for category, _ in groups:
        anchor = re.sub(r"[^a-z0-9 -]", "", category.casefold()).replace(" ", "-")
        lines.append(f"- [{category}](#{anchor})")
    lines.append("")
    for category, category_items in groups:
        lines.extend((f"## {category}", ""))
        for item in category_items:
            lines.append(f"- [{item['name']}]({item['canonical_url']}) - {item['short_description']}")
        lines.append("")
    return "\n".join(lines).rstrip()


def replace_block(text: str, start: str, end: str, body: str, label: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValidationError(f"{label} must contain exactly one generated block")
    before, remainder = text.split(start, 1)
    _, after = remainder.split(end, 1)
    return f"{before}{start}\n{body}\n{end}{after}".rstrip() + "\n"


def expected_outputs(verified: list[dict[str, Any]]) -> tuple[str, str]:
    try:
        article_template = ARTICLE_PATH.read_text(encoding="utf-8")
        readme_template = README_PATH.read_text(encoding="utf-8")
    except OSError as error:
        raise ValidationError(str(error)) from error
    article = replace_block(article_template, ARTICLE_START, ARTICLE_END, render_article(verified), "article.md")
    readme = replace_block(readme_template, README_START, README_END, render_readme(verified), "README.md")
    latest = max(dt.date.fromisoformat(item["last_verified"]) for item in verified)
    article_date = f"*Last updated: {latest.strftime('%B')} {latest.day}, {latest.year}.*"
    article, article_replacements = ARTICLE_DATE_PATTERN.subn(article_date, article, count=1)
    if article_replacements != 1:
        raise ValidationError("article.md is missing its Last updated field")
    summary = (
        f"**Last verified:** {latest.isoformat()} · **Resources:** {len(verified)} · "
        f"**Categories:** {len(grouped_items(verified))}"
    )
    readme, summary_replacements = README_SUMMARY_PATTERN.subn(summary, readme, count=1)
    if summary_replacements != 1:
        raise ValidationError("README.md is missing its verification summary")
    return article, readme


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="validate data and rendered files")
    mode.add_argument("--generate", action="store_true", help="write rendered resource sections")
    args = parser.parse_args(argv)
    try:
        if args.generate:
            verified_data, rejected_data = derive_partitions()
            VERIFIED_PATH.write_text(json_text(verified_data), encoding="utf-8", newline="\n")
            REJECTED_PATH.write_text(json_text(rejected_data), encoding="utf-8", newline="\n")
        candidates, verified, rejected = validate_repository()
        article, readme = expected_outputs(verified)
        if args.generate:
            ARTICLE_PATH.write_text(article, encoding="utf-8", newline="\n")
            README_PATH.write_text(readme, encoding="utf-8", newline="\n")
        else:
            current_article = ARTICLE_PATH.read_text(encoding="utf-8")
            current_readme = README_PATH.read_text(encoding="utf-8")
            if current_article != article or current_readme != readme:
                raise ValidationError("generated sections are stale; run scripts/build_directory.py --generate")
        needs_review = sum(item["status"] == "needs_review" for item in candidates)
        print(
            f"Validated {len(candidates)} candidates: {len(verified)} included, "
            f"{len(rejected)} rejected, {needs_review} needs review."
        )
        return 0
    except (OSError, ValidationError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
