# Jev resource list research plan

Research began on September 19, 2026, and final verification uses September 20, 2026, the date on which the publication dataset was completed.

## Objective

Build a maintained directory of resources that have a documented, useful relationship to TypeSafe Jev or to independently implemented System One-style decision models. The directory must help a developer find official material, clients, integrations, working applications, evaluations, and learning resources without treating every repository that mentions Jev as a resource.

## Research sequence

1. Define page ownership, inclusion rules, evidence requirements, and freshness rules in `reference-contract.md`.
2. Search current web results, GitHub, package registries, TypeSafe properties, project documentation, and community discussions.
3. Record every investigated item in `candidates.json`, including duplicates and rejected projects.
4. Prefer a project's repository, documentation, registry page, or product page when checking its purpose and relationship to Jev.
5. Normalize URLs and identify mirrors, forks, renamed repositories, copied lists, and multiple pages for one project.
6. Assign `include`, `reject`, or `needs_review`. The main editor makes every final classification.
7. Copy included items to `verified-items.json` and rejected items to `rejected-items.json`.
8. Generate the public resource sections in `article.md` and `README.md` from `verified-items.json`.
9. Validate data partitions, descriptions, generated sections, links, and article requirements before delivery.

## Research lanes

- Official TypeSafe resources, official SDKs, API clients, gateways, integrations, MCP servers, and Agent Skills.
- Coding agents, browser and computer-use agents, applications, developer tools, and open System One implementations.
- Benchmarks, evaluations, examples, demonstrations, learning material, and community resources.

Discovery workers return evidence-backed records. They do not make final editorial decisions or edit shared files.

## Evidence standard

An included item must have:

- a working canonical URL;
- public evidence of its purpose;
- a documented direct Jev integration or a clearly labeled independent System One-style implementation;
- meaningful code, documentation, data, or a maintained service;
- a distinct use that is not already represented by the same project under another URL;
- a concise description that can be stated without relying on promotional claims.

Repository activity during launch week is not sufficient by itself. GitHub Stars do not determine inclusion or ordering.

## Counts

The researched count includes every unique candidate record, including duplicates and forks. The final totals must satisfy:

`researched = included + rejected + needs_review`

Needs-review records remain in `candidates.json`. They are not published until the missing evidence is resolved.

## Public ordering

Official resources appear first. Other categories follow the final lookup architecture, with entries sorted alphabetically by name inside each category. Independent implementations are kept separate from software that calls TypeSafe Jev.
