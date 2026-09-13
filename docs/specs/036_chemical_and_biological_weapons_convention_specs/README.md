# Event 036 specification package

## Event identity

| Field | Accepted value |
| --- | --- |
| Event ID | `036` |
| Event name | Chemical and Biological Weapons Convention |
| Replaces | Alien Spacecraft |
| Event type | Minor Fire-Once |
| Status | To Be Reworked |
| Minimum Chaos level | 1, Calm World |
| Cluster | Diplomacy |
| Member severity | High |

## Purpose of this package

This package is the source design for a complete rework of Event 036.

The event creates a persistent diplomatic order that legitimizes chemical and biological warfare among participating states, lowers the diplomatic cost of ordinary unconventional warfare, weakens nuclear restraint, creates recurring treaty rounds, and can culminate in an international program that opens registered event-gated Chaos weapon research routes without firing their source events.

The convention changes incentives, permissions, research priorities, cooperation, inspections, AI behavior, and Condemnation handling.

It does not grant free weapons on entry.

## Source-of-truth order

Use the files in this order when implementing the event:

1. `00_master_spec.md`
2. The numbered mechanic files from `01` through `15`
3. The matrices under `matrices/`
4. The research note under `research/`
5. The implementation prompts under `prompts/`
6. The quality and catalog handoffs under `quality/`

When a summary and a detailed mechanic file differ, the detailed mechanic file controls.

When a matrix and prose differ, the prose controls unless the prose explicitly identifies the matrix as the tuning source.

## Package map

| Path | Role |
| --- | --- |
| `00_master_spec.md` | Complete event architecture and non-negotiable design rules |
| `01_event_identity_and_playable_promise.md` | Opening, player experience, scope, and global setup |
| `02_national_postures_and_membership.md` | National response choices, membership, reservations, withdrawal, and opposition |
| `03_condemnation_normalization_and_cbrn_integration.md` | Exact relationship with CBRN action records, evidence, Condemnation, deaths, contamination, and protection |
| `04_recurring_conventions_and_treaty_families.md` | Conference cadence, agenda selection, voting, ratification, compliance, and treaty families |
| `05_evolution_i_first_use_becomes_acceptable.md` | Evolution I at 200+ Chaos |
| `06_evolution_ii_strategic_wmd_doctrine.md` | Evolution II at 400+ Chaos |
| `07_evolution_iii_arsenal_without_limits.md` | Evolution III at 600+ Chaos |
| `08_international_chaos_weapons_program.md` | Registered project pool, equal selection, contributions, completion, cancellation, and source isolation |
| `09_decisions_missions_costs_and_visibility.md` | Decision phases, missions, costs, visibility budgets, and cleanup |
| `10_ai_behavior_and_probability_contract.md` | AI posture, treaty, doctrine, use, contribution, and probability audit rules |
| `11_event_chain_reactions_and_localisation_direction.md` | Event namespace, follow-ups, news, event logs, Event Details, and writing direction |
| `12_chaos_impact_and_cross_event_connections.md` | Event-owned Chaos changes and cross-system connections |
| `13_achievements.md` | Seven complete achievement designs |
| `14_asset_requirements.md` | Required report art, category presentation, icons, and achievement triplets |
| `15_acceptance_and_completion_contract.md` | Implementation gates and proof requirements |
| `matrices/` | Exact comparison and validation tables |
| `prompts/` | Reusable implementation prompts |
| `quality/` | Source audit, improvement closure, and catalog handoff |

## Core design boundaries

The player must be able to understand the convention through three compact public states:

- the country’s national posture
- the convention’s global standing
- the current agenda or active Chaos weapon project

Hidden voting scores, diplomatic weights, candidate pools, contribution formulas, source snapshots, evidence state, and AI calculations remain internal.

The convention must use the existing CBRN action record, Condemnation, protection, Deaths, Air Cleanliness, nuclear, chemical, biological, missile, special-project, event-log, and evolution systems.

Event-owned orchestration belongs in Event 036 files.

Shared registries may expose neutral provider contracts, but they must not own Event 036 lifecycle state.

## Catalog alignment warning

The supplied event catalog still describes Event 036 as Alien Spacecraft and classifies it as Minor Repeatable.

The supplied cluster export contains no current cluster row named Diplomacy.

Implementation must update the authoritative workbook and create or reconcile the approved Diplomacy cluster registration before exporting the three CSV snapshots.

Do not silently remap Event 036 to the existing Diplomatic Panic cluster.
