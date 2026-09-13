# Event 039 assassin target startup repair handoff

Disposition: implemented and accepted by parent review within the user's campaign-error repair request.

Scope: prevent new-game decision availability evaluation from dereferencing the absent global `murder_mystery_assassin_state` event target.

## Changed source

The only gameplay file changed is `common/decisions/039_murder_mystery_decisions.txt`.

The six guarded ordinary decision identifiers are `murder_mystery_discipline_unauthorized_cell`, `murder_mystery_request_central_support`, `murder_mystery_integrate_local_cells`, `murder_mystery_manage_captured_officials`, `murder_mystery_negotiate_local_settlement`, and `murder_mystery_order_high_value_operation`.

Each block now uses the documented fail-closed shape below, with the original target body preserved byte-for-byte inside the present-target branch.

```text
if = {
	limit = { has_event_target = murder_mystery_assassin_state }
	event_target:murder_mystery_assassin_state = {
		murder_mystery_action_is_available = yes
		has_political_power > constant:murder_mystery_action_cost.political_power_gate
	}
	else = {
		always = no
	}
}
```

The existing `murder_mystery_selected_cell_is_valid = yes` predicate remains outside this guard in `murder_mystery_discipline_unauthorized_cell`.

Before the repair, the five ordinary decision `available` blocks entered `event_target:murder_mystery_assassin_state` directly, producing the pasted startup error at original lines 2050, 2512, 2548, 2586, and 2624 when the target had not yet been created.

After the repair, an absent target makes the guarded branch false without evaluating the target scope, and a present target evaluates the same action-availability and political-power predicates as before.

No costs, effects, AI weights, localisation, mission timing, or category visibility conditions were changed.

## Baseline and validation evidence

The original bytes are backed up at `docs/testing/live_qa/20260913_campaign_start_repairs/baseline/assassin/common/decisions/039_murder_mystery_decisions.txt`.

The baseline SHA256 is `9330430AD2C6F73F7BBB8A3F4C485A519E7EA8BC81A4DD07752CF643DE1CA84E`.

The worker's five-guard intermediate candidate SHA256 was `1D99F52443BAA435FFC031EA8F56746A1A39C0E6AFED9ED2F63FADC970585391`.
Parent review added the identical guard to the high-value ordinary decision, producing final SHA256 `1AA26206C4BFC7128567D5FDF12A6886309175589D822751014394AAA9594D3D`.
The parent accepted all six guards after proving that unwrapping them restores every original byte, including line endings and all AI, cost, effect, and remaining predicate fields.

A no-index comparison between the backup and candidate contains exactly five six-line guard insertions at the five decision `available` blocks and no other gameplay changes.

The parent probability audit captured the pre-patch source revision `e1eda8a9b2ff3c2a56d0bbc08fa03945ed02f553a1ffc0216b70beaee0f22efb` and is comparing this candidate; the patch has no probability or balance intent.

## Target lifecycle

At a new game, `murder_mystery_assassin_state` is absent, so the new `has_event_target` limit fails closed before any `event_target:` scope is entered.

Event `chaosx.nr39.32` calls `murder_mystery_create_assassin_state_candidate` at `events/039_murder_mystery.txt:351` and creates the temporary AXS candidate with `murder_mystery_assassin_state_candidate` at `common/scripted_effects/039_murder_mystery_integration_effects.txt:1522`.

The final global target is written only after the candidate passes the split and transaction checks: `murder_mystery_commit_assassin_state_transaction` saves it at `common/scripted_effects/039_murder_mystery_runtime_effects.txt:1446` and sets `murder_mystery_assassin_state_exists` at line 1448; the caller also re-saves the candidate at `common/scripted_effects/039_murder_mystery_integration_effects.txt:1661` after commit success.

During the active assassin-state and derivative phases, the target-present branch retains the existing runtime, country-runtime, cooldown, and political-power checks.

Cleanup clears the final target conditionally at `common/scripted_effects/039_murder_mystery_runtime_effects.txt:2062`, clears runtime/category flags immediately around that operation, and then marks the runtime resolved through the existing finalization path.

## Additional consumer review

The decision source contains 33 textual references to `event_target:murder_mystery_assassin_state` in the Event 039 mission and decision surfaces after the requested area.

The unmodified positive references belong to selectable-mission activation or availability checks whose enclosing Brotherhood or cell-administration category is runtime- and actor-gated; the pasted startup output did not report these mission consumers.

The unmodified negative references belong to active-mission cancellation or AI-blocked checks; no AI weights or cancellation semantics were changed.

Parent review resolved the same direct-target risk in `murder_mystery_order_high_value_operation` by adding the identical required-target guard to its ordinary availability block.
Its selected-cell maturity predicate still runs first, and its target-present political-power and action checks remain exact.
Its execution scope remains protected by the existing availability and action transaction contract.

There are no `custom_cost` or target-scoped localisation/tooltip references for this target in the decision source.

## Required audit notes

The five reported eager ordinary availability dereferences and the same-pattern high-value ordinary decision risk are fixed.
The mission activation, mission availability, cancellation, and AI references retain their existing lifecycle gates and were not reported as startup errors.

The existing categories contain no additional visible action, mission, value, or text.
Their `visible_when_empty` settings are unchanged, while category visibility still depends on the active runtime and the expected actor flags.

Cognitive load is unchanged: no additional primary actions or simultaneous missions were introduced, and the existing player-facing values retain their current meaning and thresholds.

Mission owner and route remain Event 039. Brotherhood missions operate on the selected foreign-cell route; cell-administration missions operate on the derivative-cell/local-administration route. Their existing category visibility, selected-cell or derivative requirements, constant-driven durations, success effects, timeout effects, cancellation conditions, and duplicate-mission exclusions are unchanged.

Each repaired ordinary decision still has one spendable political-power gate represented by `constant:murder_mystery_action_cost.political_power_gate`; there is no fifth cost, cost-count change, or localisation cost string to update.

AI validity and route locks are unchanged.
Read-only probability evidence is recorded separately, and no AI factor or weighted condition was redesigned.

Localisation and tooltips are unchanged, including the existing `murder_mystery_action_requirements_tt` custom trigger tooltip used by `murder_mystery_action_is_available`.

The repair adds no flags, targets, loops, effects, or cleanup paths, so it introduces no exploit or target-retention path.

## References and validation limits

The event-target rules were checked against `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` (Event targets), `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` (event-target scope failures), and `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` (conditional `if` triggers and explicit `else`).

The installed documentation checked was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` for `has_event_target` and `if`, `effects_documentation.md` for save/clear target effects, and `script_concept_documentation.md` for control-flow blocks.

Vanilla precedent was checked in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/RAJ_GOE.txt:5030-5055`, which pairs target existence checks with target-scoped decision predicates.

An in-repo guarded event precedent is `events/039_murder_mystery.txt:415-432` in `chaosx.nr39.40`, where `has_event_target` precedes the target-scoped option trigger and effect.

No live game was launched and no logs were searched or requested, per the task constraint; campaign runtime is unverified by this repair handoff.
No gameplay simplification was introduced.

No plan handoff was written because the requested fix is local and implemented.
