# Event 006 decision and mission current audit handoff

Date: 2026-08-22.

Owner: `/root/event6_decision_current`.

Parent: `/root`.

Status: bounded audit complete; Event 006 decision and mission work remains PARTIAL/HOLD pending design and probability authority.

This handoff follows commit `0f398e5a8` and preserves the current compact localisation edits and all unrelated worktree changes.

> Subsequent tranche note (2026-08-22): commit `f7d950fd6` applies the four-group cost palette to the named decision and project surfaces and supersedes this handoff's over-budget findings for those surfaces. Retain the package cost-prose, automatic DM-01 disclosure, category-density, and typed-probability findings as open follow-up; the four-group tranche handoff is `006_event6_four_group_cost_palette_tranche_2026-08-22.md`.

## Scope and authority

The review covered the accepted Event 006 decision and mission prompt, mechanics specification Part 3, AI/balance/acceptance specification Part 7, decision-mission matrix `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv`, wave tuning matrix, shared decision files, package decision files, scripted payment and trigger helpers, decision categories, package and shared English localisation, and the two Event 006 scripted GUI surfaces.

Retired pre-event crisis surfaces were not reopened, the shared event lifecycle was not redesigned, and no pre-event decision surface was added.

Offline Paradox wiki references required by `AGENTS.md` were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, and scripted GUI modding.

Vanilla decision examples and the relevant files under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation` were also consulted, including the vanilla `custom_cost_trigger` and `custom_cost_text` pairing precedent.

## Safe patch applied

Changed file: `localisation/english/006_independence_wave_pacific_l_english.yml`.

Changed localisation id: `independence_wave_cost_pacific_island_strategic`.

Before, the key exposed literal resource names and padded prose: `Requires more than ... Stability, ... War Support, ... Command Power, ... manpower, and ... convoys. Completion commits exactly those amounts.`

After, the key uses compact icon-first values for stability, war support, command power, manpower, and convoys while retaining the five dynamic constants used by the existing Pacific payment trigger and effect.

This key is used by `custom_cost_text` in `common/decisions/006_independence_wave_pacific_decisions.txt` for the Pacific strategic decisions, so the source key needed to match the existing compact shared tooltip and blocked strings.

Gameplay payment, eligibility, AI, duration, mission cleanup, and the five-resource Pacific mechanic were not changed.

The existing compact edits in `localisation/english/006_independence_wave_decisions_l_english.yml` and `localisation/english/006_independence_wave_formable_registry_l_english.yml` were not reverted or reformatted.

## Severity-sorted findings

### P0/P1: several actions exceed the accepted four-type spendable-cost budget

The audit normalized convoy/train alternatives as one transport cost group and found these shared or package-local keys above the four-type limit.

| Localisation id | Distinct cost groups | Evidence and consequence |
| --- | ---: | --- |
| `independence_wave_cost_border_ultimatum_major` | 9 | Stability, war support, command power, transport, manpower, army XP, infantry equipment, support equipment, and a civilian factory are exposed together. |
| `independence_wave_cost_reclamation_front` | 8 | Stability, war support, command power, transport, manpower, army XP, infantry equipment, and support equipment are exposed together. |
| `independence_wave_cost_breakaway_sponsorship_standard_factory` | 7 | Command power, transport, manpower, army XP, infantry equipment, support equipment, and a civilian factory are exposed together. |
| `independence_wave_cost_integration_major` | 6 | Command power, manpower, army XP, infantry equipment, support equipment, and a civilian factory are exposed together. |
| `independence_wave_cost_agx_coastal_conference` | 5 | Stability, war support, command power, transport, and a civilian factory are exposed together. |
| `independence_wave_cost_security_standard_factory` | 5 | Manpower, army XP, civilian factory, infantry equipment, and support equipment are exposed together. |
| `independence_wave_cost_strategic` and `independence_wave_cost_strategic_major` | 5 | Strategic lines expose stability, war support, command power, transport, and a civilian factory. |
| `independence_wave_cost_pacific_island_strategic` | 5 | The Pacific trigger and payment effect actually consume stability, war support, command power, manpower, and convoy or train. The applied patch only makes the disclosure icon-first. |
| `independence_wave_cost_iw070_garrison`, `independence_wave_cost_iw071_command`, and `independence_wave_cost_iw072_oil` | 5 | Package lines expose command power, manpower, army XP, infantry equipment, and support equipment. |
| `independence_wave_form03_reopen_charter_talks_cost` | 5 | Form 03 cost line exposes five spendable groups. |
| `independence_wave_iw058_cost_fortification` | 5 | IW-058 cost line exposes command power, infantry equipment, support equipment, transport, and a civilian factory. |
| `independence_wave_komi_cost_strategic`, `independence_wave_kos_cost_strategic`, `independence_wave_kub_cost_strategic`, `independence_wave_rut_cost_strategic`, `independence_wave_tat_cost_strategic`, and `independence_wave_udm_cost_strategic` | 5 | Package strategic lines expose the same five-way strategic bundle. |

These are design-level payment defects, not safe localisation-only defects, because removing a displayed value without changing its trigger and payment would hide a real requirement.

Recommended owner fix: select a maximum four-group cost palette per action and update the matching payment effect, trigger, AI weight, tooltip, and blocked key together in `common/scripted_effects/006_independence_wave_decision_effects.txt`, `common/scripted_triggers/006_independence_wave_decision_triggers.txt`, package helpers, and the corresponding localisation files.

### P1: package cost strings still contain literal resource labels and prose

The package keys in `localisation/english/006_independence_wave_form01_02_04_l_english.yml`, `006_independence_wave_form05_l_english.yml`, `006_independence_wave_form08_l_english.yml`, `006_independence_wave_form39_l_english.yml`, `006_independence_wave_form48_l_english.yml`, and `006_independence_wave_rival_bloc_l_english.yml` retain variants of `Requires`, `Commits`, `and`, literal `Command Power`, `manpower`, `Convoys`, `Trains`, or `civilian factory` wording.

The affected strings should be rewritten icon-first after the payment palette is accepted, with dynamic values and a separate requirement tooltip where a civilian factory or route condition is not consumed.

The audit found 689 `custom_cost_text` references covering 188 unique base keys, and all 188 base keys were present after the Pacific patch; this is a localisation quality and clarity gap rather than a missing-key gap.

### P1: category density is not proven to stay within the accepted visible-action limit

The structural scan found 87 Event 006 decision categories and 782 action blocks; 56 categories contain more than six action blocks, 37 contain more than ten, and the largest contains 23.

Shared categories above the six-action review threshold are `independence_wave_security_category`, `independence_wave_host_relations_category`, `independence_wave_patron_category`, and `independence_wave_network_category`.

Package examples include `independence_wave_form03_low_countries_category` with 23 action blocks, `independence_wave_iw058_council_of_communities_category` with 23, `independence_wave_karelia_crimea_category` with 22, `independence_wave_form05_charter_category` with 16, and several categories with 11–15 action blocks.

This count is structural rather than a claim that every block is simultaneously visible; route flags, `project_ready` triggers, and active-project locks hide or serialize some actions. The current source does not provide a scenario-backed proof that every package stays at six or fewer visible primary actions, so no broad category rewrite was applied.

Recommended owner fix: phase or filter package actions in their existing category files and document the active-action cap per route, without adding extra warehouse categories or changing the shared lifecycle.

### P1: raw state values are too dense without a state presentation contract

Founding and government category descriptions expose several raw stability, war support, cohesion, reserve, confidence, and threshold values without a meter or stage marker.

The league description exposes eight or more simultaneous values, including cohesion, common cause, patron capture, reserve, confidence, opening confidence, revisionist pressure, and completed-action thresholds.

The existing founding status scripted GUI provides a bounded presentation surface, but the other shared categories do not attach that GUI, and the GUI inspection has workspace-global diagnostics. A new shared GUI or lifecycle redesign was out of scope, so this remains a design handoff.

### P1: DM-01 automatic mission cost is not dynamically disclosed

`DM-01` in `common/decisions/006_independence_wave_decisions.txt` is an automatically started provisional-capital mission with no `custom_cost_text`.

`independence_wave_start_provisional_capital_mission` in `common/scripted_effects/006_independence_wave_decision_effects.txt` can commit tied infantry equipment, support equipment, and train or motorized transport when the capital lacks supply, while `independence_wave_can_start_provisional_capital_mission` checks the related material and garrison conditions.

The mission description names the material categories but does not show dynamic quantities before activation, so the player cannot clearly evaluate the automatic commitment.

Recommended owner fix: add a dynamic status or mission disclosure using the accepted status presentation contract, with quantities sourced from the same helper values and a clear cancellation or failure explanation; do not duplicate payment logic in localisation.

### P2: duration bands need scenario review, not blind normalization

The shared constants and package constants use 30–75 day emergency bands, 90–150 day early founding bands, 150–270 day institutional bands, 120–365 day diplomatic or border bands, and 180–540 day formation or integration bands in most places.

Some package projects use 45 or 75 days for actions that may be institutional rather than emergency actions, so the accepted matrix should be checked against the intended phase before changing constants.

No timer was changed in this bounded audit.

## Decision and mission lifecycle notes

The founding category attaches `independence_wave_status_scripted_gui`; the formables category attaches `independence_wave_formable_state_puzzle_scripted_gui`; other shared categories remain ordinary decision categories and were not moved into a new GUI.

DM-01 activates only through the existing refresh and start helper after capital, garrison, equipment, and route checks, uses the short dynamic duration band, succeeds on mission timeout, and fails or relocates on capital or garrison loss.

DM-02 is gated behind the active founding mission and capital or economic requirements, has an explicit completion success effect and timeout failure path, and is not duplicated while the active founding mission lock is present.

Komi package founding projects use `is_independence_wave_komi_project_ready`, package route flags, and an active-project lock to serialize projects; timeout and cancel paths resolve success or failure and clear package state through existing helpers.

The broader mission scan found automatic founding-crisis missions that intentionally use timeout as success and cancellation as failure, so a missing `complete_effect` in those blocks is not by itself a defect.

## Mission quality notes

| Surface | Owner and category | Region and requirement | Duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| DM-01 provisional capital | Released country, founding category | Capital state, control, garrison, equipment, and supply or transport availability | Short band, normally 30–75 days after modifiers | Timeout establishes the provisional capital; capital or garrison loss cancels and invokes relocation or failure cleanup | Low while the active founding mission and start flags are present; automatic material commitment still needs clearer disclosure |
| DM-02 provisional administration | Released country, founding category | Capital and economic or administration requirements with the active founding mission gate | Matrix-defined early founding band | Completion applies success; timeout applies salary or administration crisis failure | Low while active founding mission and route flags are held |
| Komi founding crisis | KOM owner, northern compact category | Package project-ready trigger, capital, force, and state requirements | `founding_mission_days = 420` | Completion or stable cancel resolves the project; timeout and unstable cancel fail and clean package state | Active-package-project trigger serializes the project set |
| Pacific island strategic decisions | Pacific package owner, package strategic surface | Island route checks, diplomatic target and material thresholds | Package strategic project duration, commonly 90 days | Existing complete, timeout, and cancel paths remain unchanged | Route flags and active project gating are present; the at-audit five-type payment finding is superseded for the named Pacific surface by `f7d950fd6`; package cost-prose and typed-probability follow-up remain open |

## Cost and requirement clarity audit

Shared light administration and diplomatic payments are within the four-group budget.

Shared security standard factory, strategic, border, integration, breakaway, reclamation, and Pacific strategic bundles exceeded the accepted four-group budget in this audit snapshot; the named surfaces are superseded by the `f7d950fd6` four-group tranche, while package cost-prose, automatic DM-01 disclosure, category-density, and typed-probability gaps remain open.

The Pacific trigger `can_pay_independence_wave_pacific_island_strategic_cost` and effect `independence_wave_pacific_pay_island_strategic_cost` agree on the five actual spendable values, so the applied patch does not hide a payment mismatch.

Factory reservation, route availability, target validity, and non-consumed requirements should be separated from spendable cost text where the action has both kinds of conditions.

The icon-first shared compact edits were preserved, and the patched Pacific key uses `£stability_texticon`, `£GFX_war_support_icon`, `£command_power`, `£manpower_texticon`, and `£convoy_texticon` rather than literal resource names.

## AI validity and route-lock notes

The source audit found existing target, route, country-alive, control, active-project, and one-time flag checks in the shared and Komi package paths inspected; no narrow invalid-target or dead-country defect was safe to patch without a scenario.

The mandatory custom `chaosx_ai_probability_auditor` route was not available in the callable tool inventory, so direct MCP probability results below are evidence only and are not treated as an auditor handoff.

Direct shared decision probability inspection used `hoi4_probability_inspect` with adapter `decision_ai_will_do` and returned 10 candidates, 0 available candidates, 88 required inputs, and no unresolved inputs.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6aa085cc53ef56d4be8f2bb3084ec9268f576c904b2b1d1c8be2108256bd099d/9466001b873678b3f052ea65934b854bf07c56f8b7eecae106dc3b099ee1e5de/probability-inspect-35b229abc47d.json`.

Direct Komi mission probability inspection used `mission_ai_will_do` and returned 11 candidates, 0 available candidates, 15 required inputs, and no unresolved inputs.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95dadfabd3ec21015b5a4716e0d965e2aa3bd5bb2a3bf8b62e9a46f83442eea7/b0436a19d9530441087195c38510ae78c4fd2211a602383c4ed80aacadb7251d/probability-inspect-e5f696ef78fd.json`.

Direct Pacific inspection discovered that the requested decision adapter had no candidates and suggested `mission_ai_will_do`; the mission adapter exposed 28 candidates or examples and no required inputs in discovery mode.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/377003b4b52b91c205993740f302e64dc29c46d46cc0ebe1e83f560ba71acb57/c25b9911da431881170f282a02b817a7b329b6c7d77f7182317e7d4193d709cb/probability-inspect-53f86f4d0544.json`.

No AI weight or balance patch was made, and no probability compare was run because the custom auditor route and a complete scenario candidate set were unavailable.

## GUI evidence

The required read-only inspect and render routes were run for every Event 006 decision-owned scripted GUI surface in scope.

Status window inspect: `independence_wave_status_window`, scenario `independence_wave_status_default`, revision `4810e6db3b628432ae5eba5fd4ad571eb08362778978ed39d69b8bf72841bb2f`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ff50e75abd1c602d184d5715f78167147c922e2d605a2f28a2558cdcc9a88b3/aafdeaf4bb1e7d4e40833d5f4a12e58841b7958d90bd45ed6770f3747bf056e7/gui-inspect.4810e6db3b628432.json`.

Formable window inspect: `chaosx_independence_wave_formable_state_puzzle_window`, scenario `event006_formable_activated_normal`, revision `29dc700b4e152a05327b24fa3fe027896ed53ad63d613bc9b2990977c9976bd2`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ceafdfe54ac57cf49c962864588a9be5d62be188d0f3d2d063791d49a9938a6/2f9080649970dab4b93f36cd4f3462ca13835d48fd625f6c223d8a44b265e112/gui-inspect.29dc700b4e152a05.json`.

Status render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d245b460614d138be4d724b8fbbe4c0c3ae510648ae12c90abf3733e231c13/d338d48ff29e92e22f3f8fa051291bb47280836c5a57b0656e32e5c8ba167b57/independence_wave_status_window-full.svg`.

Formable render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0d6628e50f989b4c7b7264b970286e228543cf35b7af4a53813387d4ae62f51/abf65cf55a81b66e84031c62641df89489aedf0eca5985865128a2f8ce792e09/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The GUI results are fidelity evidence, not clean runtime proof: the workspace reported validation false, 2,000 global diagnostics, visible overlap counts of 75 for the status surface and 521 for the formable surface, and unresolved or missing nodes due to workspace-global diagnostics and output truncation.

No `hoi4.gui_rewrite` was run because no dedicated GUI patch was justified in this bounded audit.

## Localisation, tooltip, cleanup, and exploit notes

No missing base `custom_cost_text` key remained across the audited 689 references and 188 unique keys after the Pacific patch.

The principal remaining localisation defect is icon and prose quality in package cost strings, not key presence.

Existing cooldowns, one-shot flags, active-project locks, route flags, and target cleanup were observed in the inspected shared and package surfaces.

No new exploit loop was introduced, and no safe local exploit patch was identified; the over-budget bundles can still create opaque reserve starvation and should be addressed as a balance and payment-palette change.

## Recommended follow-up patches

1. Accept a four-group cost palette per gameplay-changing action, then update payment effects, triggers, AI weights, custom cost text, blocked text, and tooltips together.

2. Add DM-01 dynamic pre-activation cost disclosure through the existing status or mission presentation contract in `common/decisions/006_independence_wave_decisions.txt`, `common/scripted_effects/006_independence_wave_decision_effects.txt`, and the Event 006 decision localisation, without duplicating the payment helper.

3. Audit package categories for scenario-visible action counts and phase or route filtering, starting with Form 03, IW-058, Karelia/Crimea, Form 05, Brittany, IW-043, Transcaucasus, and the Rhineland/Bavaria categories.

4. After the payment palette is approved, convert the package cost keys in the Form 01/02/04, Form 05, Form 08, Form 39, Form 48, rival-bloc, and package strategic localisation files to icon-first dynamic values with non-consumed requirements separated from spendable costs.

5. Re-run the custom `chaosx_ai_probability_auditor` and its required probability compare on named Event 006 scenarios before changing any AI or weighted target logic.

## Validation and skipped validation

The bounded source audit counted category action blocks, normalized all 188 unique custom cost keys, verified that all referenced base keys exist, compared Pacific payment triggers with the payment effect, and inspected mission lifecycle patterns for DM-01, DM-02, Komi, and package crisis missions.

Both Event 006 scripted GUI windows received mandatory read-only inspect and render calls, with the fidelity and diagnostic limitations recorded above.

The edited Pacific localisation file still begins with the UTF-8 BOM bytes `239,187,191`.

Live Hearts of Iron IV launch and gameplay validation were skipped because `AGENTS.md` assigns live consumer validation to the user.

The custom probability auditor and probability compare were skipped because the route was unavailable in the callable tool inventory and direct MCP discovery did not provide complete scenario candidates.

GUI rewrite was skipped because this audit found no safe, local GUI source defect and the workspace evidence is already diagnostic-heavy.

## Remaining blockers

The parent should use `006_event6_four_group_cost_palette_tranche_2026-08-22.md` for the accepted four-group payment surfaces and retain this audit's remaining package cost-prose, automatic DM-01 disclosure, category-density, and typed-probability follow-up; localisation-only shortening of payment logic remains unsafe.

The parent must obtain a callable `chaosx_ai_probability_auditor` route or document an approved equivalent before making AI or weighted-logic changes.

The GUI inspect and render artifacts remain partially unresolved because diagnostics are workspace-global rather than isolated to Event 006.

The current completion audit still reports 161 unattested matrix rows and eight adapter-only rows, so this handoff does not claim full Event 006 package completion.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_mission_current_audit_2026-08-22.md`.
