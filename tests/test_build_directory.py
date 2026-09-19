from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_directory.py"
SPEC = importlib.util.spec_from_file_location("build_directory", SCRIPT)
assert SPEC and SPEC.loader
build_directory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_directory)


def sample_item() -> dict:
    return {
        "id": "sample-project",
        "name": "Sample Project",
        "canonical_url": "https://example.com/sample",
        "github_url": "https://github.com/example/sample",
        "official_or_community": "community",
        "creator_or_org": "Example",
        "category": "Applications and developer tools",
        "subcategory": "Classification",
        "short_description": "Classifies support requests with TypeSafe Jev.",
        "what_jev_does_here": "Jev selects a support category from a defined label set.",
        "jev_relationship": "direct",
        "language_or_stack": ["Python"],
        "license": "MIT",
        "activity_status": "active",
        "discovered_at": "2026-09-20",
        "last_verified": "2026-09-20",
        "evidence_urls": ["https://github.com/example/sample"],
        "duplicate_of": None,
        "fork_of": None,
        "quality_notes": "The repository contains code and documentation.",
        "verification_notes": "The README documents the Jev request and response path.",
        "status": "include",
        "rejection_reason": None,
    }


class ValidationTests(unittest.TestCase):
    def test_valid_record(self) -> None:
        build_directory.validate_record(sample_item(), 1)

    def test_reject_requires_reason(self) -> None:
        item = sample_item()
        item["status"] = "reject"
        with self.assertRaises(build_directory.ValidationError):
            build_directory.validate_record(item, 1)

    def test_duplicate_evidence_is_rejected(self) -> None:
        item = sample_item()
        item["evidence_urls"] *= 2
        with self.assertRaises(build_directory.ValidationError):
            build_directory.validate_record(item, 1)

    def test_article_uses_jev_role(self) -> None:
        output = build_directory.render_article([sample_item()])
        self.assertIn(sample_item()["what_jev_does_here"], output)
        self.assertNotIn(sample_item()["short_description"], output)

    def test_readme_uses_short_description(self) -> None:
        output = build_directory.render_readme([sample_item()])
        self.assertIn(sample_item()["short_description"], output)
        self.assertNotIn(sample_item()["what_jev_does_here"], output)

    def test_included_broken_item_is_rejected(self) -> None:
        item = copy.deepcopy(sample_item())
        item["activity_status"] = "broken"
        with self.assertRaises(build_directory.ValidationError):
            build_directory.validate_record(item, 1)

    def test_group_order_is_stable(self) -> None:
        official = sample_item()
        official["id"] = "official-docs"
        official["name"] = "Official Docs"
        official["canonical_url"] = "https://example.com/docs"
        official["category"] = "Official Jev resources"
        output = build_directory.render_readme([sample_item(), official])
        self.assertLess(output.index("## Official Jev resources"), output.index("## Applications and developer tools"))

    def test_readme_omits_editorial_maintenance_sections(self) -> None:
        output = build_directory.render_readme([sample_item()])
        self.assertNotIn("How projects qualify", output)
        self.assertNotIn("Data and maintenance", output)


if __name__ == "__main__":
    unittest.main()
