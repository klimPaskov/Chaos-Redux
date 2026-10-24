# Event 107 Lootboxes source package

This folder preserves the imported Lootboxes design and future production prompts. The acceptance map below identifies approved high-level mechanics and unresolved implementation details.

## Current decisions and status

On 24 October 2026, the user directed: “Adopt uploaded IDs and migrate the catalog.” The accepted uploaded identities are Event 107 Lootboxes, Event 108 Wrestling Tournament, Event 122 Rise of Cossacks, Event 109 Fuel Crisis, and Event 114 Demilitarization. This package records only the Lootboxes and Fuel Crisis corrections; the parent owns shared registry and workbook migration.
The former catalog identities Lootboxes 112 and Fuel Crisis 114 are historical only under the accepted migration. Former Rule 107, Custom Laws 109, and other displaced identities are resolved in the parent-owned migration work.
The canonical mapping is 107 Lootboxes, 109 Fuel Crisis, 112 Rise of Cossacks, 114 Demilitarization and 122 Gandhi.
The authorized workbook and shared-registry migration is complete, with original rows preserved in the [migration record](../../plans/repo_cleanup/planning_package_import_2026-10-24.md).
This documentation review changes neither the workbook nor event status.
The former `Rule` at 107 and `Lootboxes` at 112 are historical displacement context. Use the accepted target identities above and confirm the parent migration before runtime registration.
Fuel Crisis uses accepted design ID 109; former catalog identity 114 is historical only. Catalog and registry migration is accepted and parent-owned. No runtime implementation is claimed. Part 02 records a proposed fuel-reward integration only.

On 24 October 2026, the user explicitly corrected the distribution: “the lootboxes event should target every country and every country should get one free lootbox when it first fires, and it should be random rarity, as if it was a normal opening. So player countries would always get the box appear on they screen for them to open.” This accepts one global first-fire pass over every then-existing country, including all human countries, subjects, and minors, with no human-selection exclusion or PP affordability gate. Each country receives one idempotent zero-payment welcome box using ordinary rarity/reward selection and the ordinary opening completion flow. Humans receive the window automatically and perform all five chest clicks; AI uses the same authoritative resolver without GUI. The first four clicks grant nothing, the fifth grants once, and normal completion accounting, hidden influence, and rarity adaptation apply. A root first-fire guard plus per-country first-grant guard must preserve pending contents and history through save/reload/resume/repeated delivery. No recurring world hook or later-country entitlement is authorized. This correction supersedes conflicting active recipient and no-free-box text; imported historical receipts remain unchanged.
The parent also confirms all five rarity tiers and their invariants, every Part 02 reward family, and the Premium Boxes, Bonus Drops, and Chaos Loot evolutions at 200, 400, and 600 Chaos.
Accepted event scope includes hidden influence with finite burden and peaceful recovery; all four achievement routes; and a complete event-owned window with tactile stage animation, full rarity reveals, static fallbacks, and physical audio.
AI uses the same sealed reward and completion resolver for both welcome and paid boxes, without human GUI. Human recipients automatically see their welcome box and retain freedom to delay and resume a pending box.

The accepted mechanics do not certify every implementation detail.
Reward quantities and provider paths, probability percentages, burden conversions and symptom magnitudes, contribution adapters, AI reserves and cadence, achievement thresholds, exact UI dimensions and frame timing, and asset/audio sourcing details remain tuning proposals or verification work.
Event classification and Chaos level remain unresolved. Cluster placement is not decided by the imported standalone claim.
The original receipt and review files retain their authors' attributed approval history; they do not establish present source state or native behavior. Their paid-only and narrow-recipient text is historical and superseded by the 24 October correction recorded above, and those files remain unchanged.

The package contains no current gameplay completion claim.
The parent owns current source evidence and completion of the accepted registry/workbook migration.
The historical source inspection and tool availability recorded in imported files describe earlier snapshots only.
Live-game behavior remains a separate evidence class; no agent should launch HOI4, request a run, or wait for user validation.

## Source-of-truth map

| File | Purpose and disposition |
| --- | --- |
| [01 - Event Identity and Core Loop.md](01%20-%20Event%20Identity%20and%20Core%20Loop.md) | Accepted global first-fire distribution and welcome-box contract, later 50 PP purchase loop, and presentation design; other tuning and implementation details remain unresolved. |
| [02 - Rewards, Probabilities and Evolutions.md](02%20-%20Rewards%2C%20Probabilities%20and%20Evolutions.md) | Accepted reward-family coverage, rarity invariants, and three evolution concepts; exact quantities and numeric tuning remain open. Numeric checks belong to the assigned read-only probability auditor. |
| [03 - Hidden Influence and Peace Recovery.md](03%20-%20Hidden%20Influence%20and%20Peace%20Recovery.md) | Accepted hidden burden, finite symptom, and peaceful-recovery loop; exact tuning and owner adapters remain open. Imported source links are historical. |
| [04 - Lootboxes Opening UI and Audio Handoff.md](04%20-%20Lootboxes%20Opening%20UI%20and%20Audio%20Handoff.md) | Accepted full window, tactile sequence, rarity reveals, receipt, static fallback, and physical-audio scope; exact production assets and native timing remain open. |
| [05 - Decisions, AI and Integration.md](05%20-%20Decisions%2C%20AI%20and%20Integration.md) | Accepted purchase/resume and AI shared-resolver behavior; detailed AI tuning and shared-system adapters remain open. Registry mapping is settled; workbook status remains parent-owned. |
| [06 - Achievements and Validation.md](06%20-%20Achievements%20and%20Validation.md) | Four accepted achievement routes and scenario matrix; exact threshold/timing values remain tuning proposals. Native evidence must be distinguished from source evidence. |
| [107_lootboxes_implementation_handoff.md](107_lootboxes_implementation_handoff.md) | Older planning-session record, superseded for current first-fire design by the current handoff below. |
| [Current first-fire correction handoff](../../plans/107_lootboxes_plans/subagent_handoffs/107_first_fire_distribution_2026-10-24.md) | Current accepted correction, implementation scenarios, dispositions, and limits. |

## Future production prompts

These prompts remain as future handoffs. Each must use this README's acceptance map, current parent direction, and current owner skills before production.

- [107_lootboxes_goal_prompt.md](107_lootboxes_goal_prompt.md) is the compact future implementation goal.
- [107_lootboxes_coding_prompt.md](107_lootboxes_coding_prompt.md) covers the full gameplay implementation.
- [107_lootboxes_asset_prompt.md](107_lootboxes_asset_prompt.md) covers candidate visual and physical-audio work.
- [107_lootboxes_achievement_prompt.md](107_lootboxes_achievement_prompt.md) carries the candidate achievement and icon handoff.
- [107_lootboxes_decision_mission_prompt.md](107_lootboxes_decision_mission_prompt.md) covers the purchase/resumption decisions and AI policy.

## Preserved historical records

The original imported receipts and manifests remain byte-identical under [`docs/plans/107_lootboxes_plans/imported_review/`](../../plans/107_lootboxes_plans/imported_review/).
They record the earlier package's claimed source coverage, dispositions, and hashes.
Their current interpretation and this review's findings are in [the 10 October import-review handoff](../../plans/107_lootboxes_plans/subagent_handoffs/107_import_review_2026-10-10.md).
Do not edit those historical records to make them resemble current findings.

The archived review disposition reports that its planning-stage improvement review found no open addendum and recommended closing design expansion.
That historical closure does not approve the expanded mechanics listed above and does not establish current source state.
Parent review determines which proposals become accepted design or remain queued.
