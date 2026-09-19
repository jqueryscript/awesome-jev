# Contribution guidelines

Awesome Jev is a curated directory. A submission must have a verifiable relationship to TypeSafe Jev or be clearly identified as an independent System One-style implementation.

## Requirements

A submitted resource must:

- use a working canonical HTTPS URL;
- explain the exact decision or integration role Jev performs;
- contain meaningful public code, documentation, data, examples, or tests;
- belong to an existing category or explain why the inventory needs a new one;
- identify official, community, and independent work accurately;
- avoid misleading performance, compatibility, or affiliation claims;
- provide primary evidence that a maintainer can review;
- be distinct from listed resources, mirrors, and unmodified forks.

GitHub Stars do not determine acceptance. New and specialized projects are eligible when their code, purpose, and Jev relationship can be verified.

## Propose a resource

Search `candidates.json` and `verified-items.json` before adding a record. Add the complete candidate to `candidates.json` using the shape in `schema.md`. New submissions begin with `needs_review` until a maintainer finishes verification.

Descriptions must be factual, specific, and written in standard American English. `short_description` explains what the resource is. `what_jev_does_here` identifies the decision, routing, scoring, ranking, screening, selection, or other documented role Jev performs.

Do not edit generated resource sections in `article.md` or `README.md` by hand.

## Update or remove a resource

Submit corrections when a project moves, changes its license, becomes archived, stops working, or changes how it uses Jev. Include primary evidence for changes that are not evident from the canonical repository or documentation.

Rejected records remain in `rejected-items.json` after generation. This prevents the same duplicate, placeholder, or unrelated project from entering the research queue repeatedly.

## Validate changes

Run:

```sh
python scripts/build_directory.py --generate
python -m unittest discover -s tests -v
python scripts/build_directory.py --check
npx awesome-lint
```

The repository workflow also checks published Markdown links.

## Pull requests

Keep a pull request focused on one resource or one related maintenance change. Complete the pull request template and link to the evidence used for classification.
