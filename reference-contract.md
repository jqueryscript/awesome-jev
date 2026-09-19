# Jev resource list reference contract

## Reference identity

**Reference type:** Resource List / ecosystem directory

**Primary entity:** TypeSafe Jev

**Primary user task:** Find useful, current, and verifiable Jev resources, integrations, projects, examples, SDKs, agents, and independent System One-style implementations.

**Primary search intent:** Discover and compare resources in the Jev ecosystem.

**Owning query cluster:** Jev resources, Jev resource list, Awesome Jev, Jev projects, and Jev GitHub.

**Secondary query clusters:** Jev SDKs, Jev API clients, Jev integrations, Jev MCP servers, Jev agents, Jev applications, Jev examples, Jev benchmarks, and OpenJev projects.

## Excluded query ownership

The resource list does not own these focused tasks:

- a full explanation of Jev or System One Models;
- complete Jev API documentation or an API cheatsheet;
- a Jev setup tutorial for one language or framework;
- Jev pricing, rate limits, or model-version tracking;
- Jev Ultrafast documentation or review;
- Jev comparisons with LLMs, classifiers, or named alternatives;
- a ranked list of open-source Jev alternatives;
- detailed Jev integrations for Claude Code, Codex, Cursor, MCP, or browser agents.

The resource list may link to those pages when a verified page exists, but it must not reproduce their full intent.

## Scope

The directory starts with official TypeSafe material and continues through public software, evaluations, and learning resources with a concrete relationship to Jev. It includes independent System One-style implementations only in a separately labeled category.

The directory ends at discovery. It does not reproduce full API references, installation guides, benchmark reports, project reviews, or comparison articles.

## Inclusion rules

An item is eligible when all applicable rules are satisfied:

1. Its canonical URL works and identifies the project or resource clearly.
2. Primary evidence documents how it uses Jev or implements a comparable typed-decision interface.
3. A repository contains meaningful code, documentation, data, examples, or tests beyond a generated landing page or empty starter.
4. An application identifies the decision Jev performs, such as classification, scoring, routing, ranking, selection, screening, guardrails, or agent action selection.
5. A client or integration implements a usable API surface, transport, tool interface, or framework connection.
6. An evaluation provides reproducible methods, data, code, or results with enough context to interpret them.
7. A community resource adds maintained discovery, practical learning material, or first-party community access.
8. An independent implementation states that it is not TypeSafe Jev and provides working public code or weights.

## Exclusion rules

Reject an item when one or more of these conditions applies:

- Jev appears only in keywords, a dependency list, a link collection, or a passing README mention.
- The repository is empty, broken, a generated placeholder, or documentation without a distinct resource.
- The item makes compatibility claims without public evidence.
- It is a mirror, duplicate URL, or fork without material differences.
- It copies another directory without adding independent verification or maintenance value.
- It has no working code where working code is the claimed resource.
- It is unrelated, misleading, spam, or cannot be evaluated from public evidence.
- Its only evidence is a social post that does not link to a verifiable resource.

Use `needs_review` when the idea appears relevant but the public evidence is incomplete, the canonical identity is unclear, or a claim cannot be resolved safely.

## Required fields

Every candidate uses the record shape documented in `schema.md`. The public outputs rely on `name`, `canonical_url`, `category`, `short_description`, and `what_jev_does_here`. Maintenance decisions also require evidence URLs, activity state, official/community labeling, duplicate and fork fields, status, and rejection reason.

## Source hierarchy

1. TypeSafe documentation, repositories, blog, console, and official product pages.
2. The project's canonical repository and documentation.
3. Official package registry or deployment listing.
4. The project's maintained product page.
5. Reproducible evaluation material.
6. Reliable secondary evidence when primary evidence cannot answer a noncritical question.

Search snippets and directory summaries may identify candidates, but they do not verify them.

## Freshness model

- Verification snapshot: September 20, 2026.
- Recheck official access, endpoints, packages, model aliases, prices, and limits before every material update.
- Recheck repository availability, archive state, fork state, license, and stated Jev role at least monthly during the early-access period.
- Recheck all public links during every update.
- Do not publish volatile pricing or rate limits in the resource entries unless the page gains a dedicated maintained reference block.

## Update strategy

New submissions enter `candidates.json` first. They move to the verified or rejected partition only after evidence review. Run the renderer and validation suite after every accepted change. Record material additions, removals, recategorization, and scope changes in `change-log.md`.

## Related ScriptByAI pages

- `Jev Ultrafast`: planned; no URL is assigned until a live ScriptByAI page is verified.
- Other Claude Code, Codex, Cursor, MCP, Agent Skills, browser-agent, coding-agent, and AI-agent pages: link only after the current live URL and visible title are verified.

## Cannibalization boundaries

This page owns ecosystem discovery. A focused page owns a narrower instructional, comparison, reference, review, or troubleshooting task. The resource list may give a one-sentence description and link to that resource without duplicating the focused page's depth.
