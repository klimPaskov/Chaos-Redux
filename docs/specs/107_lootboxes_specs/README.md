# Event 107 Lootboxes source package

This folder preserves the imported Lootboxes design and future production prompts. The acceptance map below identifies approved high-level mechanics and unresolved implementation details.

## Current decisions and status

On 10 October 2026, the user selected the uploaded event identities: Event 107 Lootboxes, Event 108 Wrestling Tournament, and Event 112 Rise of Cossacks.
The user released the prior Rule 107 hold and asked that displaced catalog identities be recorded.
The current mapping is recorded in [`docs/specs/shared_identifier_registry.md`](../shared_identifier_registry.md) and its JSON mirror.
The parent reports that the registry and cross-package 107-hold amendments are complete and current identifier checks pass.
The current authoritative workbook state last reported by the parent is row 107 `Rule`, `Unavailable`, with Type, Chaos, and cluster empty, and row 112 `Lootboxes`, `Unavailable`.
Workbook and runtime catalog migration remain queued under parent ownership; the registry's identity mapping is settled.
This documentation review changes neither the workbook nor event status.
The former `Rule` at 107 and `Lootboxes` at 112 remain recorded as historical displacement context; use the parent-confirmed current registry mapping for implementation.
The parent source scan identifies Fuel Crisis as Event 114, `Unavailable`, with no Event 114 root; Part 02 records the target for a proposed integration, not an implemented event link.

The parent explicitly confirms the event's core loop: exactly 50 PP per purchase; five tactile human interactions; one sealed paid pending box; complete once-only delivery; and fresh reward selection for every new purchase, with no resampling during resume, reload, opening, retry, or replay.
The parent also confirms all five rarity tiers and their invariants, every Part 02 reward family, and the Premium Boxes, Bonus Drops, and Chaos Loot evolutions at 200, 400, and 600 Chaos.
Accepted event scope includes hidden influence with finite burden and peaceful recovery; all four achievement routes; and a complete event-owned window with tactile stage animation, full rarity reveals, static fallbacks, and physical audio.
AI uses the same sealed purchase and completion resolver; human players retain freedom to delay and resume a paid box.

The accepted mechanics do not certify every implementation detail.
Reward quantities and provider paths, probability percentages, burden conversions and symptom magnitudes, contribution adapters, AI reserves and cadence, achievement thresholds, exact UI dimensions and frame timing, and asset/audio sourcing details remain tuning proposals or verification work.
The imported event classification, Chaos level, and standalone-cluster claim also remain unresolved.
The original receipt and review files retain their authors' attributed approval history; they do not establish present source state or native behavior.

The package contains no current gameplay completion claim.
The parent owns the current source scan and registry/workbook evidence.
The historical source inspection and tool availability recorded in imported files describe earlier snapshots only.
Live-game behavior remains a separate evidence class; no agent should launch HOI4, request a run, or wait for user validation.

## Source-of-truth map

| File | Purpose and disposition |
| --- | --- |
| [01 - Event Identity and Core Loop.md](01%20-%20Event%20Identity%20and%20Core%20Loop.md) | Core transaction and presentation design. The explicitly confirmed requirements above are accepted; other details remain unresolved. |
| [02 - Rewards, Probabilities and Evolutions.md](02%20-%20Rewards%2C%20Probabilities%20and%20Evolutions.md) | Accepted reward-family coverage, rarity invariants, and three evolution concepts; exact quantities and numeric tuning remain open. Numeric checks belong to the assigned read-only probability auditor. |
| [03 - Hidden Influence and Peace Recovery.md](03%20-%20Hidden%20Influence%20and%20Peace%20Recovery.md) | Accepted hidden burden, finite symptom, and peaceful-recovery loop; exact tuning and owner adapters remain open. Imported source links are historical. |
| [04 - Lootboxes Opening UI and Audio Handoff.md](04%20-%20Lootboxes%20Opening%20UI%20and%20Audio%20Handoff.md) | Accepted full window, tactile sequence, rarity reveals, receipt, static fallback, and physical-audio scope; exact production assets and native timing remain open. |
| [05 - Decisions, AI and Integration.md](05%20-%20Decisions%2C%20AI%20and%20Integration.md) | Accepted purchase/resume and AI shared-resolver behavior; detailed AI tuning and shared-system adapters remain open. Registry mapping is settled; workbook status remains parent-owned. |
| [06 - Achievements and Validation.md](06%20-%20Achievements%20and%20Validation.md) | Four accepted achievement routes and scenario matrix; exact threshold/timing values remain tuning proposals. Native evidence must be distinguished from source evidence. |
| [107_lootboxes_implementation_handoff.md](107_lootboxes_implementation_handoff.md) | Imported planning-session record, retained with a superseded-workflow notice. Current mutable rules come from `AGENTS.md` and the owner skills. |

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
