# Event 006 decision and mission audit round

Date: 2026-08-24.

Owner: `/root/event6_decision_audit_round`.

Parent: `/root`.

Status: bounded audit complete with one safe localisation patch; Event 006 decision and mission completion remains partial because the Form-08 cost contract, Form-03 League Reserve icon contract, category-density proof, automatic DM-01 disclosure, and typed probability evidence remain open.

## Authority and scope

The requested contract path `docs/specs/006_independence_wave_specs/003_decision_mission_gui_contract.md` is absent from the repository.

This audit therefore used the current authoritative substitutes `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`, `docs/specs/006_independence_wave_specs/prompts/independence_wave_decision_mission_prompt.md`, `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv`, and the current Event 006 handoffs.

The offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, and scripted GUI modding were consulted.

Vanilla decision and mission documentation and the vanilla `custom_cost_trigger` plus `custom_cost_text` pairing precedent were consulted under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`.

The audit covered Event 006 decisions, missions, categories, scripted triggers and effects, cost localisation, pre-event compatibility helpers, lifecycle flags, route locks, AI weights, and the two existing Event 006 decision-owned GUI surfaces.

## Safe patch applied

Changed file: `localisation/english/006_independence_wave_montenegro_l_english.yml`.

Changed localisation ids:

- `independence_wave_mnt_cost_administration_light`
- `independence_wave_mnt_cost_administration_light_tooltip`
- `independence_wave_mnt_cost_administration_light_blocked`
- `independence_wave_mnt_cost_administration_standard`
- `independence_wave_mnt_cost_administration_standard_tooltip`
- `independence_wave_mnt_cost_administration_standard_blocked`

Before, the two MNT administration bundles spelled out `Command Power`, `manpower`, and `civilian factory` in duplicated prose, while the blocked variants added `Unavailable: commits` and comma-joined resource names.

After, each spendable value is shown as a compact icon-first amount, the tooltip aliases the compact base key, and the blocked variant keeps only the state prefix plus red icon-first values.

The payment and requirement contract was not changed.

`common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt:37-47` checks the matching command-power, manpower, and civilian-factory thresholds, while `common/decisions/006_independence_wave_montenegro_decisions.txt:61-101` and `:178-194` use the matching administration payment effects and one-factory modifier.

The file retains its UTF-8 BOM.

The current working tree also contains compact rival-bloc localisation edits in `localisation/english/006_independence_wave_rival_bloc_l_english.yml`; that file was already modified before this audit and was not changed here.

## Severity-sorted findings

### P0/P1: Form-08 uses one inaccurate, over-budget cost bundle for three different actions

`independence_wave_form08_project_cost` at `localisation/english/006_independence_wave_formable_registry_l_english.yml:112-114` is shared by `independence_wave_form08_convene_river_congress`, `independence_wave_form08_arbitrate_minorities`, and `independence_wave_form08_standardize_rail_authority` at `common/decisions/006_independence_wave_form08_decisions.txt:9-78`.

The base string still says `Commits Stability, War Support, Command Power, transport reserves, and manpower for a Danube charter project.` and the tooltip remains a long generic paragraph.

The actual trigger and payment composition differs by action:

- Congress and transport combine `can_pay_independence_wave_strategic_cost` with `can_pay_independence_wave_administration_standard_cost` and therefore use stability, command power, convoy/train transport, civilian factory, and manpower.
- Arbitration combines the strategic bundle with `can_pay_independence_wave_security_standard_cost` and therefore uses stability, command power, convoy/train transport, civilian factory, manpower, army experience, infantry equipment, and support equipment.

The current display includes War Support, which the inspected Form-08 payment effects do not consume, and omits the civilian factory, army experience, and equipment values that the triggers and effects do consume.

This is both a disclosure mismatch and a violation of the four distinct spendable-cost limit.

No localisation-only patch was applied because hiding values would conceal real payment requirements.

Recommended fix: choose a maximum four-group palette per action, split the three `custom_cost_text` keys, then update each matching trigger, payment effect, AI weight, tooltip, and blocked key together.

### P1: Form-03 displays the custom League Reserve ledger as a literal resource label

`independence_wave_form03_compact_technical_mission_cost` and its blocked key at `localisation/english/006_independence_wave_form03_l_english.yml:206-208` contain the literal `League Reserve` label without a matching texticon.

The action really changes `global.independence_wave_league_shared_reserve` by `constant:independence_wave_form03_league.technical_mission_reserve_cost`, requires the minimum reserve, sets `independence_wave_form03_compact_reserve_committed`, and refunds part of the commitment on cancellation through `common/scripted_effects/006_independence_wave_form03_effects.txt:848-866`.

No existing League Reserve texticon was found in the Event 006 interface or GFX sources.

No substitute icon was invented because a wrong resource icon would mislead the player and creating a new asset is outside this bounded audit.

Recommended fix: register and wire a dedicated League Reserve texticon through the accepted asset/UI route, or redesign the display as a clearly separated non-consumed ledger requirement with an approved icon and matching dynamic localisation.

### P1: category density exceeds the accepted visible-action review threshold in many packages

A current structural scan of `common/decisions/006_*.txt` found 87 category roots with 785 direct child action blocks, 56 categories above six child actions, 37 above ten, and a maximum of 26.

The largest current roots are `independence_wave_iw058_council_of_communities_category` with 26 actions, `independence_wave_form03_low_countries_category` with 23, `independence_wave_karelia_crimea_category` with 22, `independence_wave_form05_charter_category` with 16, and multiple 11-15-action package categories.

This is structural evidence rather than proof that every child is simultaneously visible because route flags, readiness triggers, active-project locks, and one-shot flags hide or serialize actions.

The current source has no scenario-backed proof that the six-visible-primary-action limit holds for these roots.

No broad category rewrite was applied because it would change package design and shared GUI assumptions.

Recommended fix: phase or filter the existing package actions by route and project state, document the simultaneous-visible cap per route, and avoid adding warehouse categories or extra tabs solely to hide density.

### P1: DM-01 automatic mission cost is not dynamically disclosed before activation

`independence_wave_secure_provisional_capital` at `common/decisions/006_independence_wave_decisions.txt:19-77` is intentionally `activation = { always = no }` and starts only through `independence_wave_start_provisional_capital_mission` after the country-scoped capital, garrison, equipment, and transport checks.

The mission uses `custom_cost_text = independence_wave_cost_provisional_capital` only after `independence_wave_dm01_costs_reserved` is set, so the player does not see the dynamic quantities before the automatic material commitment.

The current description identifies the material categories but does not expose the computed equipment and transport amounts.

Recommended fix: add a dynamic pre-activation status disclosure sourced from the same helper values without duplicating payment logic, and explain the cancellation/failure consequence in the existing status presentation contract.

### P2: raw value dumps remain dense in ordinary categories

The ordinary founding, government, league, and package category descriptions expose multiple stability, war-support, cohesion, reserve, confidence, host, patron, network, and threshold values as raw rows.

The Statehood Ledger status window provides a bounded presentation for five primary country values plus host, patron, network, phase, and mission summaries, but ordinary categories remain text-dense and the current MCP graph is workspace-global rather than an isolated acceptance proof.

No shared GUI redesign was attempted.

### P2: duration bands require scenario review

The source uses central duration constants for founding, diplomatic, strategic, border, formation, and integration actions, but several package actions use emergency-like 45 or 75 day bands for institutional work.

No timer change was made without a named scenario and accepted balance target.

## Pre-event indication audit

No pre-event Event 006 category, decision, mission, cost, queue, or history indication was found.

`common/scripted_triggers/006_independence_wave_crisis_triggers.txt:9-35` keeps all retired pressure and opening helpers at `always = no`.

`common/scripted_effects/006_independence_wave_crisis_effects.txt:9-52` keeps the former payment, cooldown, queue, history, and resolution helpers as empty compatibility stubs.

`common/decisions/categories/006_independence_wave_categories.txt:11-94` gates the founding and government categories on `is_independence_wave_active_country`, recognition and patron categories on provisional-or-later, network and league categories on recognized-or-later plus unlock flags, and border, formable, and high-chaos categories on later phases plus route flags.

`common/scripted_triggers/006_independence_wave_triggers.txt:9-14` defines active origin as an existing country with `independence_wave_active_origin`, the Independence Wave liberation origin, and no ended-origin flag.

The only `chaosx.nr6.3` compatibility event at `events/006_independence_wave.txt:103-123` clears stale crisis flags and variables; it does not launch a wave or expose a surface.

A targeted search found no live caller for `can_independence_wave_open_crisis`, `independence_wave_queue_crisis_release`, or the retired crisis history/effect helpers.

The allocator audit also passed and explicitly reported `pre-event crisis surface: retired; no category, mission, cost, or queue`.

## Decision category lifecycle notes

- The founding category is active-origin gated and owns the shared Statehood Ledger GUI.
- The government category is active-origin gated.
- Recognition and patron categories require provisional-or-later phase.
- Network and league categories require recognized-or-later phase, with the league requiring its unlock flag.
- Borders require regional-power phase and border-ambition unlock.
- Formables require recognized-or-later phase and formable-discovery unlock and use the existing formable state-puzzle GUI.
- High-chaos actions require regional-power phase and high-chaos unlock.
- Form-08 actions require the active post-formation Danubian carrier helper, `independence_wave_form08_confederation_carrier`, `independence_wave_form08_post_formation_active`, and the `HUN_EMPIRE` cosmetic identity.
- Montenegro package actions require the package setup and project-ready gates, capital control, and `NOT = { has_independence_wave_mnt_active_package_project = yes }` for new projects.
- Form-03 technical mission requires post-charter progression, league membership, development-compact route, minimum shared reserve, and a one-shot reserve-commitment guard.

## Cognitive-load notes

Visible primary actions: structural counts exceed six in 56 categories and exceed ten in 37; simultaneous visibility remains unresolved because the source gates were not evaluated in a complete scenario state.

Active missions: the current source has 18 `selectable_mission = yes` blocks and 87 activation blocks across Event 006 decision files.

The shared caps serialize founding missions through `has_independence_wave_active_founding_mission`, security actions through `has_independence_wave_active_security_mission`, diplomatic actions through `has_independence_wave_active_diplomatic_action`, and league crises through `has_independence_wave_active_league_crisis` in `common/scripted_triggers/006_independence_wave_decision_triggers.txt:41-104`.

Package-specific active-project flags add local serialization, but a complete scenario proof of the simultaneous global mission count was not available.

Player-facing values: the Statehood Ledger gives each primary value a named row and separates host, patron, network, phase, and mission summaries, while ordinary category descriptions still expose raw value lists without meter or threshold framing.

Text density: the custom-cost scan found 690 `custom_cost_text` references and 188 unique base keys with zero missing base keys.

Remaining literal cost labels after the current working-tree compact edits are the Form-08 generic project key and the Form-03 League Reserve custom ledger.

Value significance: the phase and ledger names are generally meaningful, but several package values do not state the threshold, consequence, or next player response in the same short surface.

## Mission quality notes

| Mission or action | Owner and category | Region and requirement | Duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `independence_wave_secure_provisional_capital` | Released-country owner, founding category | Capital control, garrison, tied equipment, and transport or supply checks | Short central band | Timeout secures the capital; capital or garrison loss cancels and records relocation or failure | Low because activation is closed, the reservation flag is required, and `fire_only_once = yes`; disclosure remains incomplete |
| `independence_wave_establish_revenue_service` | Released-country owner, founding category | DM-01 capital-secured flag, capital control, administration bundle, and no severe instability | Founding band | Completion establishes the service; timeout records salary crisis | Low under the founding active-mission cap and one-shot flag |
| `independence_wave_convene_founding_congress` | Recognized network member, league category | League unlock, network membership, valid league phase, strategic bundle | Strategic band | Completion registers founder and opens congress; timeout marks contribution failure and applies league losses | Low while league-crisis lock and one-shot flag hold |
| `independence_wave_coordinate_reclamation_fronts` | Radical league member, high-chaos category | Focus authorization, radical route, minimum member count, preflight witness, and shared reserve floor | Long mission band plus finite reclamation cooldown | Resolver freezes distinct legal member/state/owner pairs before payment; failure or timeout rolls back staging, records failure, and opens league crisis | Low from global coordinated flag, one-shot state, staged-array cleanup, and finite target reservations |
| `independence_wave_form03_request_development_compact_technical_mission` | Form-03 carrier, Low Countries category | Post-charter progression, league member, development-compact route, minimum shared reserve, and no active industrial administration | Long project band | Reserve is committed at start, completion applies integration and league gains, cancellation refunds the configured portion, and stale route loss cancels | Low from committed/complete flags and category active-project lock |
| `independence_wave_mnt_hold_mountain_compact_together` | Montenegro package owner, mountain compact category | Package setup, unresolved crisis, stable compact or capital control | `founding_crisis` central band | Stable compact resolves; timeout or unstable cancel applies package failure | Low while package crisis flags remain mutually exclusive |

## Cost and requirement clarity

The MNT administration light and standard bundles now show three spendable groups each: command power, manpower, and one civilian factory.

The current rival-bloc working-tree strings show icon-first values for invitation (four groups), acceptance (two), reserve (four), host (three), patron (three), and leadership (three); the rival-bloc file was not changed by this audit.

The Form-08 actions exceed four groups through their actual helper unions, and their shared cost key is not action-specific.

The Form-03 technical mission adds a custom League Reserve ledger to three ordinary material groups without a matching icon.

The broader Event 006 shared and package cost audit still contains additional over-budget bundles such as border ultimatum, reclamation front, breakaway sponsorship, integration, strategic factory, package Transcaucasus garrison/command/oil, IW-058 fortification, and several package strategic keys.

Those bundles require payment-effect, trigger, AI, and localisation changes together and were not silently shortened here.

Requirements such as capital control, route flags, project-ready state, host validity, target ownership, active-operation locks, and minimum shared ledgers remain in triggers and are not mixed into the compact MNT cost strings.

## AI validity and route-lock notes

Shared target helpers reject missing or self targets, active wars, invalid ownership, dead or non-compliant league members, client-route locks, and route-incompatible targets in `common/scripted_triggers/006_independence_wave_decision_triggers.txt`.

Form-08 and MNT actions are carrier or package gated, capital-controlled, and active-project locked.

Form-03 technical mission and reclamation actions use route, membership, staged-target, and one-shot guards.

No narrow dead-country, impossible-border, or stale-route defect was safe to patch in this round.

The required probability route was attempted directly for the shared Event 006 decision source with `decision_ai_will_do` and `mission_ai_will_do`, but both `hoi4.probability_inspect` calls timed out after 180 seconds before returning an artifact.

The callable tool inventory did not expose a separate `chaosx_ai_probability_auditor` agent route, and no AI weight or probability-bearing source was changed.

Historical direct MCP evidence remains in the current handoff set, including the shared decision artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6aa085cc53ef56d4be8f2bb3084ec9268f576c904b2b1d1c8be2108256bd099d/9466001b873678b3f052ea65934b854bf07c56f8b7eecae106dc3b099ee1e5de/probability-inspect-35b229abc47d.json`, the Komi mission artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95dadfabd3ec21015b5a4716e0d965e2aa3bd5bb2a3bf8b62e9a46f83442eea7/b0436a19d9530441087195c38510ae78c4fd2211a602383c4ed80aacadb7251d/probability-inspect-e5f696ef78fd.json`, and the Pacific discovery artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/377003b4b52b91c205993740f302e64dc29c46d46cc0ebe1e83f560ba71acb57/c25b9911da431881170f282a02b817a7b329b6c7d77f7182317e7d4193d709cb/probability-inspect-53f86f4d0544.json`.

These historical artifacts are partial source/discovery evidence and do not prove current campaign balance or justify an AI rebalance.

## Localisation and tooltip gaps

All 188 current `custom_cost_text` base keys were found for the 690 references.

The targeted remaining literal-cost scan found only `independence_wave_form08_project_cost` and `independence_wave_form03_compact_technical_mission_cost` after the current compact edits.

The MNT keys patched in this round now use the correct `£command_power`, `£manpower_texticon`, and `£civ_factory` tokens for every displayed spendable value.

The Form-08 generic tooltip is still too long and inaccurate because it attempts to explain three different payment bundles in one paragraph.

The Form-03 League Reserve value needs an approved dedicated icon or a redesigned ledger requirement presentation.

## Cleanup and exploit-risk notes

DM-01 has one-time activation, reservation, timeout, cancellation, relocation, and failure flags.

Shared decisions use one-shot flags, cooldowns, route locks, active-operation locks, finite target arrays, and explicit cleanup in the inspected paths.

Form-03 clears its reserve-commitment flag on completion or cancellation and removes its decisions during package cleanup.

Form-08 removes its three project decisions during runtime cleanup and gates all projects on the live post-formation carrier.

No new free-unit loop, equipment farm, war-goal spam path, core spam path, or cooldown bypass was introduced by the MNT localisation-only patch.

The over-budget Form-08 and other shared bundles can still create opaque reserve starvation until the payment palettes are corrected at the gameplay layer.

## Mandatory GUI evidence and fidelity limits

The inspected decision-owned surfaces are the existing shared Statehood Ledger `independence_wave_status_window` and the existing formable puzzle `chaosx_independence_wave_formable_state_puzzle_window`; no new GUI was introduced.

Fresh `hoi4.gui_inspect` calls used scenarios `independence_wave_status_default` and `E6_FORMABLE_STATE_PUZZLE_GUI_SETTLED_2026_08_09` and both timed out awaiting `tools/call` after 180 seconds.

Fresh `hoi4.gui_render` calls used the same scenarios with the `normal` state at 1280x720 and both timed out awaiting `tools/call` after 180 seconds.

No `hoi4.gui_rewrite` call was made because no safe GUI source patch was identified and the required read-only route did not complete.

Historical Event 006 GUI artifacts retained in the handoff set include the Statehood Ledger inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ff50e75abd1c602d184d5715f78167147c922e2d605a2f28a2558cdcc9a88b3/aafdeaf4bb1e7d4e40833d5f4a12e58841b7958d90bd45ed6770f3747bf056e7/gui-inspect.4810e6db3b628432.json`, its render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d245b460614d138be4d724b8fbbe4c0c3ae510648ae12c90abf3733e231c13/d338d48ff29e92e22f3f8fa051291bb47280836c5a57b0656e32e5c8ba167b57/independence_wave_status_window-full.svg`, the formable inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ceafdfe54ac57cf49c962864588a9be5d62be188d0f3d2d063791d49a9938a6/2f9080649970dab4b93f36cd4f3462ca13835d48fd625f6c223d8a44b265e112/gui-inspect.29dc700b4e152a05.json`, and its render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0d6628e50f989b4c7b7264b970286e228543cf35b7af4a53813387d4ae62f51/abf65cf55a81b66e84031c62641df89489aedf0eca5985865128a2f8ce792e09/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

Those historical artifacts reported workspace-global diagnostics and visible-overlap counts, so they are fidelity evidence only and do not constitute clean visual or live acceptance.

## Validation

`python -B .tools/audit_event6_allocator.py` passed after the patch and still reported 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, 32 content attestations, 29 compatible groups, the 3/4/5/7/10 automatic ladder, and the retired pre-event crisis surface.

A targeted read-only scan found 690 custom-cost references, 188 unique base keys, zero missing base keys, and the two remaining literal-cost base keys listed above.

The patched MNT localisation still begins with the UTF-8 BOM bytes `EF-BB-BF`.

Live Hearts of Iron IV launch, save/load, and gameplay validation were skipped because live consumer validation belongs to the user.

Current GUI inspect and render were skipped from acceptance because both required calls timed out after 180 seconds.

Current typed probability evaluation and compare were skipped because both direct inspect calls timed out and the separate custom auditor route was not callable.

## Changed files and remaining work

Changed by this audit:

- `localisation/english/006_independence_wave_montenegro_l_english.yml`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_audit_round_2026_08_24.md`.

No decision, mission, scripted effect, scripted trigger, AI, category, GUI, or asset source was changed.

Remaining issues are the inaccurate and over-budget Form-08 payment palette, the uniconized Form-03 League Reserve ledger, package and shared category density, DM-01 dynamic pre-activation disclosure, raw ordinary-category value presentation, and unavailable typed probability/GUI acceptance evidence.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_audit_round_2026_08_24.md`.
