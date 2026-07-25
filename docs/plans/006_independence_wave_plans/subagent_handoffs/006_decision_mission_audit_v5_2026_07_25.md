# Event 006 decision and mission audit v5

Date: 2026-07-25.

Scope: Read-only current-HEAD audit of the Event 006 Independence Wave decision, mission, formable, scenario, focus-link, localisation, AI, cleanup, and decision-owned status GUI surfaces.

No gameplay, localisation, GUI, asset, or balance source was changed by this audit.

## Result

The accepted DM-01 through DM-62 surface is materially implemented in `common/decisions/006_independence_wave_decisions.txt`.

The base file contains 64 current decisions, comprising DM-01 through DM-62 plus the two explicitly supporting choices `independence_wave_treasury_backed_public_works` and `independence_wave_refuse_binding_arbitration`.

The FORM-03 Low Countries surface contains 23 bounded consent, post-charter, project, ratification, recovery, sovereign-associate, and withdrawal actions in `common/decisions/006_independence_wave_form03_decisions.txt`.

The shared formable transaction surface contains ten method, consent-rule, and founding-invitation choices in `common/decisions/006_independence_wave_formable_registry_decisions.txt`.

The SCN-008 ledger contains three explicitly zero-reward navigation controls in `common/decisions/006_independence_wave_scenario_decisions.txt`.

The one current gameplay HOLD is DM-58's visible activation preflight, detailed below.

## Issue list, sorted by severity

### Medium — DM-58 availability does not prove the legal, distinct front set that its paid resolver requires

`independence_wave_coordinate_reclamation_fronts` requires `has_independence_wave_reclamation_front_preflight = yes` in `common/decisions/006_independence_wave_decisions.txt:3539`.

The preflight at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:427` only counts three members satisfying `is_independence_wave_reclamation_front_member_candidate` at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:408`.

That candidate accepts an external claimed state but does not mirror the execution predicate's no-active-war check, `can_declare_war_on` check, existing `take_state_focus` war-goal check, claim-or-neighbour condition, or distinct external-owner constraint.

The actual predicate at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:381` correctly checks each selected state and target owner, including `can_declare_war_on = PREV`, target validity, no current war, and both state and owner array uniqueness.

The paid resolver at `common/scripted_effects/006_independence_wave_decision_effects.txt:667` also performs those exact checks before it increments the staged front count, and `independence_wave_rollback_reclamation_front_staging` at `common/scripted_effects/006_independence_wave_decision_effects.txt:718` removes the staged claim, used-state marker, finite war goal, member staging flag, aligned arrays, and count on failure.

This means DM-58 is cost-atomic, but the player can be allowed to start it without a legal injective three-member-to-distinct-owner front set and then receive the defined no-cost failure, major loss, and league-crisis branch.

Recommended fix: Replace the count-only availability gate with a non-mutating, injective matching preflight that mirrors `is_valid_independence_wave_reclamation_front_state` for each frozen member, including a distinct owner and state reservation for every required front.

Recommended files and identifiers: `common/scripted_triggers/006_independence_wave_decision_triggers.txt`, `is_independence_wave_reclamation_front_member_candidate`, `has_independence_wave_reclamation_front_preflight`, and `common/decisions/006_independence_wave_decisions.txt`, `independence_wave_coordinate_reclamation_fronts`.

The amended preflight should retain the execution-time recheck and rollback, because live war and owner state can still change between availability evaluation and completion.

### Low — GUI MCP output cannot certify the Event 006 window in isolation

`hoi4.gui_inspect` produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20cb8cd69694814ec9d0d4db09236a796159dbe82ccf2c4ef13ceb3c459ddabe/3fd9893a4ce91ccad685c3b2a9b6523494a8c4e7832081995873275cbeceb2bf/gui-inspect.ba4323bf16cb4312.json`.

`hoi4.gui_render` produced the focused `independence_wave_status_window` artifact set, including `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fa9f04b815591ede7937431e1115a19f4bb54558a6d1d4136604cd1bed3dd530/1f550a0af03ecdc41ced98e3a560b7250c05d866109873d1274be9f11ed127c8/independence_wave_status_window-full.png`.

The renderer modelled 380 elements, approximated 48, and left 12 unresolved, but its combined repository validation is truncated and includes unrelated GUI diagnostics.

No Event 006-specific GUI defect is asserted from that global result.

Source review of `common/scripted_guis/006_independence_wave_scripted_gui.txt` and `interface/006_independence_wave.gui` confirms the window is presentation-only apart from an explicit state refresh and local tab flags, so it does not create an unpriced alternative decision action.

## Decision category lifecycle notes

The eleven base categories at `common/decisions/categories/006_independence_wave_categories.txt:8` through `:81` are staged by active-country, provisional, recognized, regional-power, living-former-host, and focus-unlock predicates.

The high-chaos, league, border, and formable categories require both the appropriate phase and their route or focus unlock, preventing a hidden action family with no reveal route.

The focus tree supplies the gated release points, including the regional-ambition helper at `common/scripted_effects/006_independence_wave_focus_effects.txt:603`, the formable discovery focus at `common/national_focus/006_independence_wave_focus.txt:1723`, the high-chaos focus at `:1921`, the reclamation authorization at `:1934`, and the league-congress entries at `:1599` and `:1634`.

The event cleanup effect clears the route unlock flags including the border, formable, league, patron, and high-chaos gates at `common/scripted_effects/006_independence_wave_decision_effects.txt:852` through `:856`.

The FORM-03 category is carrier, invitation, post-charter, or sovereign-associate gated in `common/decisions/categories/006_independence_wave_form03_categories.txt`.

The scenario ledger category is visible only while the owner has elected to inspect a nonempty rejection ledger in `common/decisions/categories/006_independence_wave_scenario_categories.txt`.

## Mission quality notes

The base surface has 17 timed missions: founding DM-01 through DM-05 and DM-10, foreign-service DM-15, security DM-17, DM-20, and DM-23, host defence DM-30, patron balance DM-35, league DM-45 and DM-47, formable congress DM-54, high-chaos DM-58, and charter transformation DM-59.

All 17 use named duration constants rather than raw day values, provide a completion and timeout or cancellation path, and are protected by completion, failure, cancellation, cooldown, or removal state as appropriate.

DM-58 owner: the initiating charter-compliant league member and its frozen active league-member ledger.

DM-58 category and region: high-chaos league action resolving claim-connected external state targets across the current league membership rather than a fixed geographic region.

DM-58 requirements: radical-revisionist league route, focus authorization, no active league crisis, required material and shared reserve threshold, and the preflight discussed in the Medium HOLD.

DM-58 duration: `constant:independence_wave_decision_duration.long` at `common/decisions/006_independence_wave_decisions.txt:3539`.

DM-58 success: one finite, generation-stamped `take_state_focus` war goal per resolved member after the staged count reaches the configured minimum, followed only then by the strategic and major-security payments.

DM-58 failure: a failed flag, major loss, and league crisis without those material payments, with rollback of the staging ledger.

DM-58 duplicate risk: execution is protected by aligned member, state, and owner arrays plus exact target and state checks, but availability does not currently prove the same injective matching.

FORM-03's `independence_wave_form03_ratify_confederal_charter` is the additional timed mission at `common/decisions/006_independence_wave_form03_decisions.txt:582`.

Its owner is the active Low Countries carrier, its requirement is the full ratification gate, its duration is a named constant, its success resolves full ratification, and its timeout and cancellation paths call the bounded FORM-03 cleanup logic.

No passive mission store or free-unit loop was found in these mission surfaces.

## Cost and requirement clarity notes

The base 64 decisions have an AI block, success path, and lifecycle guard, and every non-mission action has a concrete cost path.

The 15 materially paid base missions use their declared custom costs in completion, while the two founding statehood missions use milestone completion conditions instead of an action charge.

The two apparent custom-cost exceptions are valid specialised helpers rather than missing payments.

DM-41 calls `independence_wave_decision_contribute_safe_reserve` at `common/scripted_effects/006_independence_wave_decision_effects.txt:378`, which consumes exactly one safe infantry, train, convoy, or fuel channel before crediting the shared reserve.

DM-55 calls `independence_wave_formable_pay_selected_commit_cost` at `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:1374`, which charges strategic resources plus the selected method's administration or security commitment before the registry commit request.

The 23 FORM-03 actions all have AI and lifecycle guards, and all except the timed ratification mission have a custom material cost paired to a payment helper.

The ten formable registry choices are deliberately unpriced route, method, consent, and invitation declarations, with the actual paid congressional transaction kept at DM-54 and DM-55.

The three SCN-008 controls have `cost = 0`, `days_re_enable = 0`, and `ai_will_do = { base = 0 }` because they only paginate or close a player-owned inspection ledger and apply no gameplay effect.

Raw numeric cost and cooldown values occur only on those navigation controls, while the gameplay decisions use script constants and named duration families.

## AI validity and route-lock notes

Every base, FORM-03, and formable-registry decision has an `ai_will_do` block.

The three player-only scenario ledger buttons explicitly disable AI.

Targeted host, patron, network, league, border, and formable decisions are target-root and target-trigger gated, and their visible route locks align with the category lifecycle and focus unlocks above.

DM-58's resolver independently rejects dead, member, war, already-targeted, and war-goal-duplicate owners before creating a finite war goal.

The remaining AI caveat is the same DM-58 availability mismatch: a valid AI or player activation gate should prove the legal matching before the mission can begin.

## Localisation and tooltip notes

The four relevant English localisation files contain all 221 `name`, `desc`, and `custom_cost_text` keys referenced by the base, FORM-03, registry, and scenario decision files.

The DM-58 title, description, custom cost text, and effect tooltip describe the requirement for multiple compliant external objectives and the finite war-goal outcome.

The preflight HOLD makes that wording slightly stronger than the actual availability guarantee, because the current availability count can include a member whose claim candidate cannot later pass the legal-war or uniqueness checks.

No missing localisation key or raw player-facing trigger dump was found in the reviewed decision surfaces.

## Cleanup and exploit-risk notes

DM-58's execution path is strong against free war-goal, duplicate-target, and stale-staging exploits because it pays only after the exact staged count and rolls back generated claims, finite goals, flags, arrays, and counters otherwise.

The remaining risk is a no-cost but disruptive activation that can create a league crisis from a stale or non-injective preflight, which is why the availability HOLD is Medium rather than a cost-atomicity failure.

FORM-03 project, ratification, associate, and withdrawal actions use cancellation and removal effects to clear active-action and project state, while the registry transaction closeout clears selection, invitation, consent, and transaction markers.

No equipment farming, free-unit loop, unrestricted core spam, permanent free war-goal, or cooldown bypass was found in the audited current sources.

## Meaningful validation

I structurally enumerated all decision blocks in the four current decision surfaces.

The check found 64 base decisions, 23 FORM-03 decisions, ten shared registry decisions, and three scenario ledger controls.

It found an AI block, completion path, and lifecycle guard in every base decision, and a timeout or cancellation branch for every base mission.

I verified that the relevant 221 localisation references resolve across `006_independence_wave_decisions_l_english.yml`, `006_independence_wave_form03_l_english.yml`, `006_independence_wave_formable_registry_l_english.yml`, and `006_independence_wave_scenario_l_english.yml`.

I traced DM-58 from availability through its valid-state predicate, staged execution, post-count cost gate, timeout, cancellation, and rollback helpers.

I also reviewed the focused status GUI with `hoi4.gui_inspect` and `hoi4.gui_render`; the global MCP diagnostic collection is not a scoped validation of this window, so it is recorded as fidelity evidence only.

Skipped meaningful validation: no live HOI4 execution was run, because parent scope is a current-source read-only audit and live consumer validation belongs to the user.

Skipped meaningful validation: no numeric AI scenario sweep was run, because the relevant decisions depend on live country values, state ownership, legal-war status, and per-route flags that are not declared by this audit as a concrete scenario set.

## Handoff

Changed files: this audit handoff only.

Changed decision, mission, scripted GUI, and localisation identifiers: none.

Before and after behaviour: no gameplay behaviour changed.

Remaining issue: implement the DM-58 exact injective availability preflight before treating its activation gate as player-safe.

Plan handoff path: no separate implementation plan was written, because the required change is a narrow helper and decision-gate repair rather than a new system.
