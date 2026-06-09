# Event 006 Border Commission Protected Transfer Safety Audit Handoff

Date: 2026-05-30 08:53:28 UTC

Scope: Event 006 Independence Wave, Border Commission protected-transfer safety patch only.

## Files changed

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_085328_border_commission_safety_audit_handoff.md`

No gameplay, localisation, GUI, flag, or asset files were edited by this audit.

## Parent patch audited

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`

Audited ids and helpers:

- `independence_wave_decision.border_transfer_legitimacy_cost`
- `independence_wave_decision.border_transfer_legitimacy_spend`
- `independence_wave_decision.border_transfer_patron_leverage_spend`
- `can_independence_wave_offer_protected_transfer`
- `independence_wave_offer_protected_transfer`
- `independence_wave_clamp_patron_leverage`

## Issues by severity

High:

- No high-severity issue found. The protected-transfer trigger/effect/constants are internally matched and do not introduce a patron-leverage underflow.

Medium:

- No medium-severity issue found. Startup legitimacy is `35`, while the new trigger-side affordability gate is `5`, so normal Event 006 releases are not deadlocked by this patch.

Low:

- Existing decision description does not spell out the hidden legitimacy spend or patron-leverage relief. I did not patch localisation because this task was constrained to decision/effect logic and the parent patch did not add a new visible key.

## Decision category lifecycle notes

- Owner: Event 006 released country.
- Category: `independence_wave_border_commission_category`.
- Decision: `independence_wave_offer_protected_transfer`.
- Region/target: state-targeted through `state_target = any`; targets must be a ROOT core not owned or claimed by ROOT, not a capital, not host-survival reserved, not already claimed by the commission, and owned by an eligible existing owner.
- Reveal/opening: `can_independence_wave_open_border_commission` requires an Independence Wave release plus a border-office/directorate/officer/civic/arbitration route gate.
- Reuse/cooldown: completion sets `independence_wave_border_commission_cooldown` using a temp-variable-backed duration, and the decision also has `days_re_enable = @independence_wave_border_commission_days`.

## Mission quality notes

No mission was added or changed by this patch.

- Owner: Event 006 released country.
- Category: `independence_wave_border_commission_category`.
- Requirement: targeted decision trigger `can_independence_wave_offer_protected_transfer`.
- Duration: clickable decision only; no active mission duration.
- Success: immediate effect sets cooldown, records peaceful border resolution, spends legitimacy, reduces/clamps patron leverage, raises claim ambition, and flags the target state as petitioned.
- Failure: no mission failure branch applies.
- Duplicate risk: low for protected transfer because target states get `independence_wave_protected_transfer_petitioned` and the general target filter blocks states already claimed by the commission; the cooldown also throttles repeat use.

## Cost and requirement clarity notes

- `border_transfer_legitimacy_cost = 5` is the positive affordability constant.
- `border_transfer_legitimacy_spend = -5` is the matching effect-side spend.
- `can_independence_wave_offer_protected_transfer` uses `check_variable = { var = independence_wave_legitimacy value = constant:independence_wave_decision.border_transfer_legitimacy_cost compare = greater_than_or_equals }`, which is supported by vanilla trigger documentation.
- `independence_wave_setup_released_country` initializes `independence_wave_legitimacy` from `constant:independence_wave_startup.initial_legitimacy`, currently `35`; the new cost gate is therefore affordable for normal startup releases before other legitimacy spends.
- `border_transfer_patron_leverage_spend = -5` is followed immediately by `independence_wave_clamp_patron_leverage = yes`, which clamps below-floor leverage back to `constant:independence_wave_decision.patron_leverage_floor` (`0`).

## AI validity and route-lock notes

- AI uses the existing protected-transfer decision entry and complete effect; no AI-only path bypasses the new scripted trigger or clamp.
- Route gate remains intact: protected transfer requires `independence_wave_route_patron_cabinet` or `independence_wave_compact_anti_puppet_clause`.
- Target owner gate remains intact and does not select dead owners: `owner = { exists = yes ... }`.
- No closed-route or disabled-evolution dependency was introduced by this patch.

## Localisation and tooltip gaps

- No localisation file was changed.
- No new on-screen id or renamed decision was introduced.
- Low residual UX gap: the decision description still describes the negotiated transfer generally rather than listing the new `5` legitimacy gate or the patron-leverage floor safety. I left this unchanged because the audit was logic-only and the existing decision is already localised.

## Cleanup and exploit-risk notes

- The patron-leverage floor safety issue from the Patron Ledger audit is addressed for this Border Commission effect by the direct clamp call after the leverage spend.
- No equipment, unit, war-goal, core, or flag-asset loop was introduced.
- The cooldown duration uses the established safe pattern: constant assigned into a temp variable, then passed to `days =`.
- No flag assets or flag files were touched.

## Before and after behavior

Before parent patch:

- `independence_wave_offer_protected_transfer` could subtract patron leverage without a clamp in the protected-transfer effect.
- The effect had no trigger-side legitimacy affordability gate for its legitimacy spend.

After parent patch:

- Protected transfer is target-eligible only when the released country has at least `5` legitimacy.
- Completing protected transfer spends `5` legitimacy, subtracts `5` patron leverage, then clamps patron leverage to the configured floor.
- Normal Event 006 releases start with `35` legitimacy and therefore are not blocked by the new affordability gate.

## Validation run

- `rg -n '<=|>=' common/script_constants/006_independence_wave_constants.txt common/scripted_triggers/006_independence_wave_triggers.txt common/scripted_effects/006_independence_wave_effects.txt common/decisions/006_independence_wave_decisions.txt`
  - Result: no unsupported `<=` or `>=` operators found.
- `rg -n '^\s*days\s*=\s*constant:' common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt common/script_constants/006_independence_wave_constants.txt common/decisions/006_independence_wave_decisions.txt`
  - Result: no direct `days = constant:` duration usage found.
- `rg -n '^\s*(days_re_enable|days_remove)\s*=\s*constant:' common/decisions/006_independence_wave_decisions.txt`
  - Result: no decision duration fields using `constant:` directly found.
- Brace-depth check over the three parent-touched files plus `common/decisions/006_independence_wave_decisions.txt`.
  - Result: all four files ended with `balance=0 min=0`.
- Targeted rg check for `border_transfer_legitimacy_cost`, `border_transfer_legitimacy_spend`, `border_transfer_patron_leverage_spend`, and `independence_wave_clamp_patron_leverage`.
  - Result: constants, trigger, spend, and post-spend clamp are present at the expected call sites.

## Skipped validation

- No live-game scenario validation was run.
- No full-repo `git diff --check` was run because the worktree intentionally contains unrelated dirty Event 005/Event 006 changes outside this bounded audit.
- No flag or asset validation was run because the user explicitly said not to touch flags anymore, and this audit did not inspect or edit flag assets.

## Remaining risks and recommended fixes

- No blocking issue remains for the bounded protected-transfer floor-safety patch.
- Optional future polish: if the parent opens a localisation pass, add concise requirement/effect text for the `5` legitimacy gate and patron-leverage relief so the visible decision text fully reflects the hidden variable movement.
