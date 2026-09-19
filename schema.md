# Jev resource dataset schema

`candidates.json` is the complete research ledger. `verified-items.json` and `rejected-items.json` are exact status partitions derived from it.

## File shape

Each JSON file contains an object with metadata and an `items` array:

```json
{
  "schema_version": "1.0",
  "last_updated": "2026-09-20",
  "items": []
}
```

## Candidate record

```json
{
  "id": "lowercase-stable-id",
  "name": "",
  "canonical_url": "",
  "github_url": "",
  "official_or_community": "official",
  "creator_or_org": "",
  "category": "",
  "subcategory": "",
  "short_description": "",
  "what_jev_does_here": "",
  "jev_relationship": "direct",
  "language_or_stack": [],
  "license": "",
  "activity_status": "active",
  "discovered_at": "2026-09-20",
  "last_verified": "2026-09-20",
  "evidence_urls": [],
  "duplicate_of": null,
  "fork_of": null,
  "quality_notes": "",
  "verification_notes": "",
  "status": "candidate",
  "rejection_reason": null
}
```

## Field rules

| Field | Rule |
| --- | --- |
| `id` | Unique lowercase letters, numbers, and hyphens. It remains stable if the display name changes. |
| `name` | Public project or resource name. |
| `canonical_url` | Unique HTTPS destination used in public outputs. |
| `github_url` | Canonical GitHub repository URL or an empty string for non-GitHub resources. |
| `official_or_community` | `official`, `community`, or `independent`. |
| `creator_or_org` | Public maintainer, company, or organization name. |
| `category` | One final public category listed below. |
| `subcategory` | Optional maintenance label. |
| `short_description` | One factual sentence for the README. It must end with a period. |
| `what_jev_does_here` | One factual sentence that identifies Jev's role or explains the independent implementation. |
| `jev_relationship` | `direct`, `official_resource`, `independent_implementation`, or `community_resource`. |
| `language_or_stack` | Array of documented languages, frameworks, protocols, or platforms. |
| `license` | SPDX identifier, `Proprietary`, `No license detected`, or `Not applicable`. |
| `activity_status` | `active`, `experimental`, `archived`, `stale`, `broken`, or `unknown`. |
| `discovered_at` | ISO date on which the candidate entered the ledger. |
| `last_verified` | ISO date of the latest evidence review. |
| `evidence_urls` | One or more primary evidence URLs for included and rejected records. |
| `duplicate_of` | Stable ID of the canonical record, or `null`. |
| `fork_of` | Stable ID or canonical repository URL, or `null`. |
| `quality_notes` | Concise maintenance assessment. |
| `verification_notes` | What was confirmed or what remains unresolved. |
| `status` | `include`, `reject`, or `needs_review` in the final ledger. |
| `rejection_reason` | `null` unless rejected; otherwise one allowed reason. |

## Public categories

- Official Jev resources
- SDKs and API clients
- Gateways and integrations
- Agent tools and MCP servers
- Browser and computer-use agents
- Applications and developer tools
- Open System One implementations
- Benchmarks and evaluations
- Examples and learning resources
- Community resources

Empty categories are omitted from public outputs.

## Rejection reasons

- `duplicate`
- `fork_without_material_difference`
- `jev_only_mentioned`
- `no_working_code`
- `insufficient_evidence`
- `unrelated`
- `abandoned`
- `spam`
- `generated_placeholder`
- `broken`
- `misleading_claim`
- `other`

## Partition invariants

- Every candidate ID and canonical URL is unique in `candidates.json`.
- Every `include` record appears unchanged in `verified-items.json`.
- Every `reject` record appears unchanged in `rejected-items.json`.
- No `needs_review` record appears in either partition.
- `candidate count = included count + rejected count + needs-review count`.
- Public generated blocks contain only verified items.
