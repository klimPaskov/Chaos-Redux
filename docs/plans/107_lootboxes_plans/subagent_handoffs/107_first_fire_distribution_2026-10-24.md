# Event 107 Lootboxes first-fire distribution correction

Disposition: The user’s 24 October 2026 correction is accepted design and queued for implementation. This handoff records documentation changes only. No runtime definition, implementation, or gameplay completion is claimed.

## Acceptance basis and current design

The user directed: “the lootboxes event should target every country and every country should get one free lootbox when it first fires, and it should be random rarity, as if it was a normal opening. So player countries would always get the box appear on they screen for them to open.” This is the acceptance basis for the global first-fire pass and welcome box. Every country existing at the first global firing receives lasting access and exactly one zero-payment sealed box, including all MP humans, subjects, minors, and poor AI or human countries. There is no human-exclusion roll or PP affordability gate.

The root first-fire guard admits one global distribution, and a per-country first-grant guard makes individual grants idempotent. The grant uses the ordinary random rarity and reward selection, evolution/recipe rules, and authoritative completion resolver. Human recipients automatically see the local window and complete all five chest clicks; clicks one through four grant nothing, and click five grants once. AI uses the same resolver without GUI. Ordinary completion accounting, hidden influence, and rarity adaptation apply. The welcome receipt records explicit zero-payment provenance and never claims a 50 PP payment. Later purchases remain exactly 50 PP. Save/reload/resume/repeated delivery cannot reroll, duplicate the welcome box, reset history, or overwrite pending state. No recurring worldwide hook or automatic entitlement for later-created countries is accepted.

## Source-of-truth map and dispositions

- `docs/specs/107_lootboxes_specs/README.md` records the direct user decision, acceptance basis, no-runtime claim, and status of the correction.
- `01 - Event Identity and Core Loop.md` is the detailed design authority for global distribution, zero-payment provenance, shared opening flow, persistence, and 50 PP subsequent purchases.
- `05 - Decisions, AI and Integration.md` maps the global grant to the human and AI routes and prohibits an ongoing world scan.
- `06 - Achievements and Validation.md` adds poor-human/AI, MP human, first-fire idempotency, and click completion scenarios.
- Parts 02 and the coding, goal, decision/mission, and achievement prompts now distinguish welcome boxes from paid purchases and reuse ordinary rarity/completion behavior.
- The user directed on 24 October 2026: “Adopt uploaded IDs and migrate the catalog.” Canonical targets include Lootboxes 107, Fuel Crisis 109, Rise of Cossacks 122, and Demilitarization 114. Former Lootboxes 112 and Fuel Crisis 114 identities are historical only for those respective events. Parent-owned workbook and shared-registry migration is authorized and in progress. This subtask made no workbook or registry changes.
- `107_lootboxes_implementation_handoff.md` remains an older workflow record and should be read as superseded for current first-fire design by the README and this handoff. The prior `107_import_review_2026-10-10.md` is historical and remains unchanged.
- All files under `docs/plans/107_lootboxes_plans/imported_review/` are immutable historical evidence and were not edited.

The paid-only statements in the former active design conflicted with the user's correction. The current spec distinguishes welcome provenance from the paid receipt rather than treating the welcome box as a purchase. Achievement-specific conditions that explicitly require a purchase remain as written; ordinary completion accounting is applied to the welcome opening.

## Acceptance scenarios for implementation

| Scenario | Required result |
| --- | --- |
| First fire with poor human and poor AI countries, including several MP humans, subjects, and minors | Every then-existing country gets access and one box; no affordability or human filter excludes anyone. |
| Human first-fire delivery | Its window appears automatically; all five accepted clicks are available; first four grant nothing; fifth delivers once and applies ordinary completion accounting. |
| AI first-fire delivery | Same sealed random rarity/reward and completion resolver, with no human GUI. |
| Save/reload/resume with welcome box pending at any click stage | Same identity, rarity, reward, provenance, and accepted stage resume with no resampling or extra grant. |
| Repeat root callback or per-country delivery after pending or completed welcome box | First-fire guard blocks a second distribution; per-country guard does not reset access, pending contents, history, adaptation, or influence. |
| Later-created country after the first firing | No automatic welcome box or recurring grant. A later purchase, when available, still costs exactly 50 PP. |
| Welcome and ordinary paid openings | Both use ordinary completion accounting, hidden influence, and rarity adaptation; only paid opening records an actual 50 PP debit. |

## Changed files and limits

Changed documentation: `README.md`, Parts 01, 02, 05, and 06, plus `107_lootboxes_coding_prompt.md`, `107_lootboxes_goal_prompt.md`, `107_lootboxes_decision_mission_prompt.md`, and `107_lootboxes_achievement_prompt.md`. Reconciled stale references to Fuel Crisis as catalog identity 114 while its design package uses ID 109 pending migration. Updated catalog references omit unverified status labels. No assets, gameplay, localization, workbook, registry, or historical imported-review files changed.

Meaningful documentation checks are limited to confirming affected links resolve and searching active text for the superseded narrow-recipient, no-free-welcome, and paid-only pending requirements. Runtime behavior and exact event registration remain for implementation and parent integration review.

## Parent integration after catalog migration

The parent completed the authorized catalog and shared-registry migration on 24 October 2026.
The catalog has 155 unique event IDs and uses the canonical package identities 104 through 122, with all migrated events remaining Unavailable.
The final migration evidence supersedes this handoff’s earlier pending-migration observations, while preserving those observations as subtask history.
See the [current task report](../../repo_cleanup/planning_package_import_2026-10-24.md) for the original-row preservation, completed mappings and verification limits.
Runtime implementation remains outside this import task.
