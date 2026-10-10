# Event 087: Military Madness

**Minor Repeatable · Chaos level 1 · Military Preparation / Low · root `chaosx.nr87.1`**

This package is the rework design for Event 087.
The legacy implementation is `events/087_ww1.txt` with `common/ideas/087_ww1_ideas.txt` (a fixed nine-month entrenchment idea granted through a report option), and the catalog row still names it "It’s WW1"; the rework is not implemented.
Implementation working evidence belongs under `docs/plans/087_military_madness_plans/`.

## Authority

| Source | Status |
| --- | --- |
| User brief (recorded in [Research and source notes](087_military_madness_research_and_source_notes.md)) | Explicit user decisions: identity and cluster role, Minor Repeatable at Chaos level 1, every valid country rolls independently, 365-day packages, one/three/six/ten rolls with broad minima of one/one/two/three, thresholds 200/400/600, no stage after Gods of War, duplicates allowed, random statistic and magnitude, no archetypes or balancing, and a pool covering every technically usable vanilla, DLC, country and Chaos Redux military statistic |
| World Claims connection (Part 5) | Accepted by the parent in the 8 October 2026 planning improvement pass |
| Design changes listed in the revision log | Accepted under the 10 October 2026 spec audit, within the user's planning-package brief |
| Magnitude bands, equal-entry sampling, pre-fire stage selection, technical saturation, achievements | Proposed design elaborating the brief; tune during implementation and record acceptance in the plans folder |
| [Open questions](#open-questions) | Unresolved |

## Specification

| Read order | Document | Contents |
|---|---|---|
| 1 | [Core](087_military_madness_spec_part_1_core.md) | Identity, recipients, stages, cluster role |
| 2 | [Pools and evolutions](087_military_madness_spec_part_2_pools_and_evolutions.md) | Broad through full pools, draw rules, the audited registry |
| 3 | [Magnitudes](087_military_madness_spec_part_3_magnitudes.md) | Per-statistic bands, units, technical saturation |
| 4 | [Stacking and lifecycle](087_military_madness_spec_part_4_stacking_and_lifecycle.md) | Independent packages, expiry, country lifetimes, legacy saves |
| 5 | [Campaign and presentation](087_military_madness_spec_part_5_campaign_and_presentation.md) | Strategy, AI, the spirit and package rows, connections, Chaos |
| 6 | [Assets and achievements](087_military_madness_spec_part_6_assets_and_achievements.md) | Four reports, one spirit icon, three achievements |
| — | [Acceptance and probability scenarios](087_military_madness_acceptance_and_probability_scenarios.md) | Future implementation checks |
| — | [Research and source notes](087_military_madness_research_and_source_notes.md) | Source hierarchy, legacy mismatch, technical findings |

## Prompts

| Document | Use |
|---|---|
| [Goal prompt](087_military_madness_goal_prompt.md) | Short task entry point within 4,000 characters |
| [Coding prompt](087_military_madness_coding_prompt.md) | Complete implementation assignment |
| [Asset prompt](087_military_madness_asset_prompt.md) | Four report scenes, one spirit icon and three achievement triplets |
| [Achievement prompt](087_military_madness_achievement_prompt.md) | Registry, tracking and art routing for the three achievements |

There is no super-event, focus tree, portrait, scripted GUI or new unit in this design.

## Implementation gates

- Every admitted statistic needs a real country-scoped binding, value type, beneficial sign and reversible application, proved against the installed game (Part 2).
- Reduction statistics need a proved technical floor that stays valid with external modifiers (Part 3).
- The acceptance scenarios are future checks; none has been executed.

## Open questions

1. **Boolean military capabilities (Part 2).**
The brief asks for every usable military statistic with a random magnitude; on-off capabilities have no meaningful magnitude.
Proposal: exclude them with a recorded technical reason rather than giving them a fake numeric range.

## Revision log

### 2026-10-10 spec audit

Basis: 10 Oct 2026 spec audit under the user's planning-package brief.

- Replaced the dedicated read-only ledger window with native surfaces: the combined dynamic-modifier spirit shows the active totals, and each active package is one row in the event's decision category with its rolls and remaining days (Part 5).
  The ledger duplicated the spirit tooltip, needed a custom GUI for a Minor event and multiplied player-facing values.
- Made the Chaos impulse a flat +5 per natural occurrence, because the planning rules give no extra Chaos for a higher pre-fire stage (Part 5).
- Replaced the versioned catalog build, revision provenance and catalog-migration rules with one audited, append-only registry while keeping the user's full-breadth requirement (Parts 2 and 4).
- Added bounded AI use of sampled results: temporary front aggression for large land-offense results and invasion priority for naval-invasion results, without touching the draws (Part 5).
- Trimmed the acceptance scenarios to the new design (removed ledger interface and catalog-revision cases) and removed process narration from the research notes and prompts; prompts now use `.claude` skill paths and the repository policy for unavailable tools and specialists.
- Deleted `087_military_madness_source_reading_manifest.json`, `087_military_madness_document_checks.md`, `087_military_madness_review_and_agent_assignments.md`, `087_military_madness_asset_manifest.json` and `087_military_madness_package_manifest.json`.
  They held planning-session reading evidence, historical document checks, unexecuted role assignments duplicated by the coding prompt, an asset list duplicated by Part 6, and a hash inventory with no consumer.
