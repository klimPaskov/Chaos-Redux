# Event 006 Containment Review Decision/Mission Audit Patch Handoff

## Scope

Bounded audit of the Event 006 Independence Wave Sealed Dossier containment review tranche:

- `independence_wave_seal_impossible_registry`
- `independence_wave_hold_containment_review`
- `can_independence_wave_fail_containment_review`
- related Sealed Dossier triggers, effects, constants, localisation, and docs

This pass did not edit flag image files, flag graphics, `gfx/flags`, `common/countries`, `history/countries`, Event 005 files, country packages, visual assets, super-events, scripted GUI, new tags, or world-end systems.

## Changed Files

- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_event006_containment_review_audit_patch_handoff.md`

## Changed Identifiers

- Decision: `independence_wave_seal_impossible_registry`
- Mission: `independence_wave_hold_containment_review`
- Localisation: `independence_wave_seal_impossible_registry_review_tt`

## Findings Sorted by Severity

1. Low: `independence_wave_seal_impossible_registry` started the review through a hidden flag and stability effect, but the click effect did not explicitly tell the player that a containment review mission begins. Patched with a custom effect tooltip.
2. Low: `independence_wave_hold_containment_review` relied on default non-selectable mission behavior. That is valid, but explicit `selectable_mission = no` is clearer and safer for future maintainers. Patched.
3. Low: containment failure after a subject/capitulation failure can leave occult pressure below the Unmarked Congress gate if the country failed from very low pressure. The route is still not retryable and `chaosx_iw_strange_revealed` is set, but the player may need the remaining reveal-side surface, such as the quiet census, before the Congress button becomes available. This is acceptable for the current first-pass surface.

## Category Lifecycle Notes

`independence_wave_sealed_dossier_category` opens for independent Event 006 releases that have a strange package signal, an open sealed audit, or enough occult pressure. The seal route requires the archive audit, no active/failed review, no Unmarked Congress, no containment, and occult pressure below `constant:independence_wave_decision.sealed_unmarked_congress_occult_gate`.

The seal click sets `independence_wave_containment_review_active` through `independence_wave_seal_impossible_registry_effect`, applies the stability cost, hides the quiet census and Unmarked Congress while active, and activates `independence_wave_hold_containment_review`. Successful timeout clears the active review, sets containment/closed flags, lowers occult pressure and radicalization, and closes the category through the existing category gate. Failure clears the active review, sets `independence_wave_containment_review_failed`, sets `chaosx_iw_strange_revealed`, and blocks containment retry.

## Mission Quality Notes

- Owner: Event 006 release country.
- Category: `independence_wave_sealed_dossier_category`.
- Region: no map region; this is a country-scope bureaucratic/occult containment review.
- Requirement: keep occult pressure below the reveal gate and remain independent/uncapitulated without Unmarked Congress appearing.
- Duration: `@independence_wave_containment_review_days` (90 days).
- Success: `timeout_effect` runs `independence_wave_complete_containment_review_effect`.
- Failure: `available` runs `complete_effect` early when `can_independence_wave_fail_containment_review = yes`.
- Duplicate risk: low. The seal decision requires no active/failed review and the mission key is unique; the active flag is cleared by both success and failure.

Mission semantics match the offline wiki: `available` is the early auto-completion/failure condition for non-selectable missions, `timeout_effect` is the uninterrupted timer outcome, and `is_good = yes` makes the tooltip frame the early available condition as failure.

## Cost and Requirement Clarity Notes

The seal decision has political power cost through `constant:independence_wave_decision.sealed_registry_cost` and stability cost through `independence_wave_seal_impossible_registry_effect`. Requirement text is behind `independence_wave_seal_impossible_registry_requirements_tt` and does not expose raw trigger blocks. The patch adds `independence_wave_seal_impossible_registry_review_tt` so the player sees that the click starts a review window, not instant containment.

## AI Validity and Route-Lock Notes

AI use remains bounded to the country-scope decision. There are no targeted countries, state targets, route arrays, or dead-target risks in this containment mission. AI weights prefer civic/democratic containment and lower strange-package containment willingness; eligibility still blocks active review, failed review, Unmarked Congress, containment, and high occult pressure.

## Localisation and Tooltip Gaps

Patched localisation key:

- `independence_wave_seal_impossible_registry_review_tt`

No missing localisation was found for the containment mission name/description, failure tooltip, success tooltip, seal requirement tooltip, or the new seal review-start tooltip. Event 006 localisation remains UTF-8 with BOM and uses the repo's no-`:0` style.

## Cleanup and Exploit-Risk Notes

The containment route is not farmable: the seal decision is one-shot, the active review blocks the quiet census and Unmarked Congress, failure blocks retry, and timeout containment closes the category. No free unit, equipment, core, war-goal, or cooldown loop was found in this tranche.

Remaining exploit/design risk is first-pass scope only: the strange reveal package after `chaosx_iw_strange_revealed` is not fully implemented here, so this mission correctly does not claim full strange country package, focus module, super-event, asset, or world-threat completion.

## Before and After Behavior

Before:

- Clicking `independence_wave_seal_impossible_registry` silently started the containment review through `independence_wave_containment_review_active` and applied stability cost.
- The mission was non-selectable by default, but that intent was implicit.

After:

- Clicking `independence_wave_seal_impossible_registry` shows a custom tooltip that a containment review begins and occult pressure must stay below the reveal gate.
- `independence_wave_hold_containment_review` explicitly declares `selectable_mission = no`.
- Mission success/failure effects are unchanged.

## Validation Run

- Read required local references: AGENTS.md, `hoi4-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`.
- Consulted offline wiki pages for Decision modding, Triggers, Effect, Localisation, Scopes, Data structures, Modifiers, On actions, Event modding, Idea modding, and AI modding.
- Consulted vanilla docs for triggers, effects, script concepts, and script constants, plus a vanilla non-selectable `is_good = yes` mission precedent in `NORDIC.txt`.
- Brace balance passed with balance `0` for:
  - `common/decisions/categories/006_independence_wave_categories.txt`
  - `common/decisions/006_independence_wave_decisions.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
- Unsupported operator scan found no `<=` or `>=` in the bounded Event 006 decision/category/trigger/effect/constant/localisation/event-doc files.
- Localisation BOM check returned `efbbbf` for `localisation/english/006_independence_wave_l_english.yml`.
- Localisation `:0` scan found no matches in `localisation/english/006_independence_wave_l_english.yml`.
- Localisation coverage check found the new review-start tooltip and existing containment mission tooltip keys.
- Forbidden-path check: this patch changed only the files listed above. The worktree already contains modified Event 005 paths, but this audit did not edit them.

## Skipped Validation

- No live in-game UI validation was run from this subagent environment.
- No broad Event 006 validation was run outside the bounded Sealed Dossier containment review tranche.

## Remaining Issues

- The Sealed Dossier remains a first-pass strange surface. Full strange country packages, strange focus modules, strange achievements, super-events, art, scripted GUI, and world-threat systems remain out of scope and unclaimed.
- Future strange-package work should decide whether `chaosx_iw_strange_revealed` alone should unlock a larger reveal route even when occult pressure remains below the Unmarked Congress gate after a non-pressure failure.

## Plan Handoff Path

No broad expansion plan was written. This handoff is the required audit/patch handoff.
