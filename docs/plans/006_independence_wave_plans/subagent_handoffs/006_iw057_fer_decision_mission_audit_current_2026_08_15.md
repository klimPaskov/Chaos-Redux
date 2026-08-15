# IW-057 FER decision and mission audit, current 2026-08-15

## Disposition

The IW-057 Far Eastern Republic decision and founding-mission surface is source-audited and remains fail-closed outside the central Event 006 adapter, attestation, normal/scenario preflight, Join, and vanilla-history contracts.

This audit applied only narrow package-local fixes for cost presentation, cost-count clarity, the founding-mission capital requirement tooltip, and stale-generation category visibility.

No central admission or Join file was changed, no weighted AI value was tuned, no dedicated scripted GUI was added, and no changes were staged or committed.

The hard rule is preserved: no IW-057 category, mission, wave-pressure meter, cost, queue, or history indication is visible before an active Event 006 origin and package setup proof.

## Scope and references

Audited sources were `common/decisions/006_independence_wave_far_eastern_decisions.txt`, `common/decisions/categories/006_independence_wave_far_eastern_categories.txt`, `common/script_constants/006_independence_wave_far_eastern_constants.txt`, `common/script_constants/006_independence_wave_decision_constants.txt`, `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt`, `common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt`, `common/ai_strategy/006_independence_wave_far_eastern.txt`, `common/scripted_effects/006_independence_wave_decision_effects.txt`, `common/scripted_triggers/006_independence_wave_decision_triggers.txt`, and `localisation/english/006_independence_wave_far_eastern_l_english.yml`.

The accepted design references were `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`, `docs/events/006_independence_wave/far_eastern_republic_package.md`, `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`, and the current IW-057 core, identity/roster, capital-preflight, and capital-reaudit handoffs.

The required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding were consulted.

Vanilla documentation consulted was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`.

Vanilla decision precedents inspected were the timed mission in `common/decisions/AFG.txt` and custom-cost decision patterns in `common/decisions/CZE.txt`.

## Issue list sorted by severity

### Blocker, remaining

IW-057 is not admitted to the central Event 006 dispatcher, attestation registry, normal preflight, SCN-008 preflight, or deterministic Join, so the source-local decision surface cannot be claimed as live runtime-complete.

The parent-owned identity-rights receipt, institutional command-roster receipt, neutral-flag provenance, typed probability evidence, and central promotion remain required before admission.

The package cleanup helper exists and removes the mission, all ten project decisions, package ideas, flags, and ledgers, but the central lifecycle dispatcher does not invoke it while the package is intentionally fail-closed.

### High, fixed in this audit

`independence_wave_fer_codify_durable_sovereignty` displayed the shared strategic cost while also committing one civilian factory through its decision modifier, resulting in five distinct spendable cost types once the convoy-or-train branch was counted and making the display inconsistent with package-local gating.

The decision now uses `independence_wave_fer_cost_strategic`, `can_pay_independence_wave_fer_strategic_cost` no longer requires a civilian-factory availability gate, and the strategic decision no longer commits a civilian factory.

The remaining strategic payment is stability, war support, command power, and either convoys or trains, which is four distinct spendable types and still uses the existing `independence_wave_decision_pay_strategic` effect.

### Medium, fixed in this audit

`independence_wave_fer_register_fer_communities` used the shared administration-standard cost text showing the shared two-factory burden while its package-local modifier and trigger used one factory.

The decision now uses `independence_wave_fer_cost_administration_standard`, whose icon-first text displays command power, manpower, and one civilian factory from `independence_wave_fer_cost.civilian_factory_use`.

### Low, fixed in this audit

The founding mission tooltip did not tell the player that its selected anchor capital also had to remain owned and controlled for success.

`independence_wave_fer_hold_railway_council_desc` now names the selected FER anchor and its capital as the retained objective.

The category could remain visible after a force-package generation rollover if the old setup flag survived, even though every decision-level action was already generation-gated.

The category now also requires `has_independence_wave_force_package_for_current_generation = yes`.

### Low, remaining review note

`independence_wave_fer_duration.project_short`, `project_standard`, and `project_long` are declared in `common/script_constants/006_independence_wave_far_eastern_constants.txt` but the decisions currently use the shared Event 006 bands `independence_wave_decision_duration.short`, `standard`, `long`, and `strategic`, which resolve to 75, 120, 180, and 300 days rather than the package-local 45, 75, and 105-day values.

This may be an intentional shared palette, but it is an unresolved tuning-source inconsistency and was not changed because replacing the shared durations would alter package balance without an accepted design decision or probability/timing review.

## Decision category lifecycle notes

The owner is the FER country with `original_tag = FER`, the exact IW-057 package id, the Independence Wave origin, and the active-origin country contract.

The category is `independence_wave_fer_railway_compact_category` and uses the existing `GFX_decision_independence_wave_integration_missions` icon.

The category is visible only when `is_independence_wave_fer_package = yes`, `independence_wave_iw_057_setup_complete` exists, and the current force-package generation is valid.

`is_independence_wave_fer_package` includes `is_independence_wave_active_country = yes`, so pre-event FER history, low stability, occupation, host pressure, or any unrelated world condition cannot open the category.

The category has one auto-managed founding mission and ten package-local projects, with no extra tabs and no dedicated scripted GUI.

The founding mission activates only for a prepared package/current generation while the crisis is neither resolved nor failed, and it uses `available = { always = no }` so the player cannot click it as an ordinary decision.

The founding mission lasts `constant:independence_wave_fer_duration.founding_crisis`, currently 420 days.

The mission cancels on package loss, force-generation loss, capital loss, anchor loss, or the success-state compact/route/anchor combination.

Its cancel effect records success only when the compact is stable, a route government exists, an ordered anchor remains owned and controlled, and the capital remains controlled by FER; all other package-local cancellation paths apply the one-shot project-failure effect.

Its timeout records `independence_wave_fer_compact_crisis_failed` and applies the same one-shot failure effect.

Every paid project checks package readiness, its own completion flag, its resource/equipment cost, capital control, and the absence of any active package project before starting.

The shared `has_independence_wave_fer_active_package_project` trigger serializes all ten project ids, preventing parallel project duplication and cost races.

Route projects are mutually exclusive through their route flags and the shared route-government absence gate; once one route installs, the other route projects are no longer available.

The durable sovereignty and Pacific corridor capstones require founding settlement, crisis resolution, route/network state, stable compact values, and capital control, so they cannot bypass the foundation sequence.

## Cognitive-load notes

The category description presents only the two package ledgers, their 0-to-100 range, and the shared stability threshold of 60, which gives each visible value a clear meaning, threshold, consequence, and response action.

At the busiest normal stage the player can see the founding mission, four base projects, and one selected-route project, for a maximum of six primary visible actions.

Only one paid project can be active at a time, and the route branch reduces to one visible route action after a route flag is chosen.

The two final projects are staged behind settlement, stability, route, and network proofs rather than being placed in an extra category or tab.

Decision descriptions are short and identify the institutional action and its outcome without exposing raw trigger blocks, implementation flags, or unrelated counters.

The only player-facing dynamic values are the two ledgers and the 60 stability threshold, and the category text explains how to respond by raising both values to that threshold.

## Founding mission quality

| Field | Audit result |
| --- | --- |
| Owner | FER package country, exact IW-057 origin/package contract |
| Category | `independence_wave_fer_railway_compact_category` |
| Region and anchors | `volga_urals_siberia_far_east`; ordered states 408 or 409; selected anchor must also be the capital anchor at runtime |
| Host target | `independence_wave_former_host` must exist, not be ROOT, retain `liberation_release_protected_state`, and still own that protected state; a living host must be at war or settlement is blocked as appropriate |
| Requirement | Install a route government, raise both ledgers to 60, retain an owned/controlled ordered anchor, and keep its capital controlled |
| Duration | 420 days from `independence_wave_fer_duration.founding_crisis` |
| Success | Cancel-time success branch sets `independence_wave_fer_compact_crisis_resolved` only with stable compact, route government, anchor control, and capital control |
| Failure | Timeout, package/force invalidation, anchor loss, capital loss, or any non-success cancellation sets `independence_wave_fer_compact_crisis_failed` and applies the one-shot failure effect |
| Duplicate risk | One founding mission id, one setup flag, one resolved/failed latch pair, and serialized projects prevent duplicate founding resolution or repeated failure penalties |

The founding mission uses `is_good = no` and an urgent shared AI weight because it is a failure-sensitive objective rather than a player-selected spend action.

## Cost and requirement clarity

The audit counted distinct spendable types after separating conditional alternatives such as convoy-or-train and counting only values actually consumed or committed by the decision.

| Decision | Cost types | Duration in source | Cost text | Result |
| --- | ---: | --- | --- | --- |
| `independence_wave_fer_secure_railway_ports` | 3 | shared short, 75 days | shared administration-light icon string | Pass |
| `independence_wave_fer_integrate_coastal_guards` | 4 | shared standard, 120 days | shared security-standard icon string | Pass |
| `independence_wave_fer_register_fer_communities` | 3 | shared standard, 120 days | `independence_wave_fer_cost_administration_standard` | Fixed mismatch; pass |
| `independence_wave_fer_settle_former_host_ledgers` | 2 | shared long, 180 days | shared diplomatic-standard icon string | Pass |
| `independence_wave_fer_ratify_constitutional_autonomy` | 3 | shared short, 75 days | shared administration-light icon string | Pass |
| `independence_wave_fer_adopt_railway_charter_compact` | 2 | shared long, 180 days | shared diplomatic-standard icon string | Pass |
| `independence_wave_fer_convene_coastal_councils` | 3 | shared short, 75 days | shared administration-light icon string | Pass |
| `independence_wave_fer_establish_coastal_emergency_command` | 4 | shared standard, 120 days | shared security-major icon string | Pass |
| `independence_wave_fer_codify_durable_sovereignty` | 4 | shared strategic, 300 days | `independence_wave_fer_cost_strategic` | Fixed five-type over-budget/mismatch |
| `independence_wave_fer_open_pacific_corridor` | 2 | shared long, 180 days | shared diplomatic-standard icon string | Pass |

Every spendable cost shown by the audited FER surface uses a texticon token rather than a literal resource name.

The new package-local administration-standard text uses `£command_power`, `£manpower_texticon`, and `£civ_factory`.

The new strategic text uses `£stability_texticon`, `£GFX_war_support_icon`, `£command_power`, and the conditional `£convoy_texticon`/`£GFX_train_texticon` pair.

The payment effects remain the shared, already-audited Event 006 helpers, so the text changes do not create a free project, refund, or alternate payment path.

Civilian-factory commitment remains on the four administration-light and administration-standard actions that still declare the package-local one-factory modifier; the strategic action no longer carries that fifth burden.

## AI validity and route-lock notes

The four FER AI strategy blocks are gated by `original_tag = FER`, the parent identity-rights flag, package setup, host/route state, and the package-local AI profile flags, so they do not create an independent pre-event AI path.

Decision AI uses shared `high`, `standard`, and `urgent` constants with existing war and host-threat modifiers; no AI weight or probability value was changed in this audit.

All project availability gates are shared with the human resource, capital, package, generation, route, and failure checks, so AI cannot select a dead country target or a closed route through a divergent gate.

Former-host settlement checks the saved host scope for existence, generation-safe protected-state ownership, and peace/war state before bilateral effects; the no-host or host-at-war path closes local ledgers without writing bilateral deltas.

The capital/anchor preflight repair already present in the shared worktree was preserved and is not claimed as this audit's patch.

### Probability evidence and blocker

Fresh read-only MCP source inspection after this audit used the mission adapter on `common/decisions/006_independence_wave_far_eastern_decisions.txt` with source revision `e2259d68c63f39978057d74e226353f239f802196fc6b57d0d0dc2d6a63e2b0a` and source hash `d5c1417fc7a7483b6e9b3fbe2d62eff37b7eaa3f0a205eaf210590ff769ca51f`.

The mission inspection discovered 11 AI candidates, 15 required inputs, zero unresolved source items, zero available candidates under the empty fixture, and `poolComplete = false`.

The mission inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17e0fc763ab5961a183137cef30d4b6c2f3af715edc9a4e4b1adf3723a0f5929/2d7ae0a1976bbadd7832d75dd4a5117ae274f4669fa63d35f7b6585a91efaf83/probability-inspect-d5c1417fc2c7.json`.

The decision adapter inspection correctly found no decision candidates and suggested the mission adapter; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b7c761405ea28a71cd30bbc414598082707475a96d30a39fde58bf8bc6f5461/50e7e6158b0712e50581ac49c0666e83907280740542f8352aa83678be169441/probability-inspect-d5c1417fc7a.json`.

The required `chaosx_ai_probability_auditor` worker route was not callable in the available tool inventory, so these direct MCP receipts are evidence only and are not a worker sign-off or quantitative balance claim.

No probability compare was run because no weighted AI value was changed and the worker-mediated baseline/compare route was unavailable.

## Localisation and tooltip gaps

The FER decision source's 40 unique `name`, `desc`, `custom_cost_text`, and `custom_effect_tooltip` references resolve against the FER or shared Event 006 English localisation files.

The FER localisation file retains UTF-8 with BOM encoding.

The new cost keys are compact, icon-first, and use dynamic constants for every displayed amount.

The founding mission description now explains the capital-control requirement, while the other decision descriptions remain concise and outcome-oriented.

No raw trigger expression or implementation flag is exposed in the audited player-facing text.

## Cleanup and exploit-risk notes

`independence_wave_fer_apply_project_failure` is guarded by `independence_wave_fer_project_failure_applied`, preventing repeated compact/pressure penalties from timeout and cancellation callbacks.

The package cleanup effect removes the founding mission, all ten project decisions, package ideas, local ledgers, flags, and temporary state, and its project effects are idempotent where an already-set route or settlement flag is encountered.

Paid costs are taken in `complete_effect` before the project timer starts and are not refunded on cancellation, preventing free retry loops and making failed projects consequential.

The one-active-project gate prevents parallel payment, duplicate equipment/factory commitments, and repeated route installation.

The strategic civilian-factory burden and gate removed by this audit eliminate the only identified five-type cost and its associated cost-display mismatch; no free-unit, equipment-farming, war-goal, core, or cooldown loop was found in this package-local decision layer.

Central cleanup invocation remains an admission blocker rather than a package-local defect because IW-057 is deliberately not registered in the central dispatcher yet.

## GUI evidence

FER has no dedicated `.gui`, `scripted_gui`, or event-owned mechanic window; the live surface is the shared vanilla `countrydecisionview` decision category.

The mandatory read-only `hoi4.gui_inspect` call targeted `countrydecisionview` with scenario `iw057_fer_decision_category` and returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/606cea6fe7dc4167cc1a3336055eaef4349a0c014d365974e5035f835f80e6b2/824767f7576e9f53eafa78f06dff753d6ed54be0f5a21aae8c0bff85e9c2e99e/gui-inspect.08190190d4e71890.json`.

The focused inspect reported five inspected elements, modelled fidelity 36, approximated fidelity 2, ignored fidelity 13, missing fidelity 1, unsupported fidelity 11, unresolved fidelity 0, and no `GUI_VISIBLE_OVERLAP`; aggregate workspace validation remained false because of unrelated global GUI diagnostics.

The mandatory read-only `hoi4.gui_render` call covered normal, active, disabled, warning, long-text, and missing-localisation states at 1920x1080 and 1366x768 UI scale 1 and returned artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cef49a14298f4520d7b743980f3f3bef7a7abed5eec93cd9893160d245b792f6/a35824122671acd3b88e46180a668e4339e7ac27c6af151d21d459978df1a6fa/countrydecisionview-full.svg`.

The render response was truncated by the MCP response-size limit, with no source blockers or checks reported, so it is route-resolution and visual-surface evidence rather than a complete fidelity proof.

No `hoi4.gui_rewrite` call was made because no in-scope FER GUI patch exists and the shared vanilla window is not owned by this package.

No `chaosx_event_ui_worker` route applies because IW-057 does not introduce a dedicated scripted GUI.

No callable `hoi4.decision_inspect` or `decision_render` route was present, so source review and the shared decision-window GUI evidence are not treated as an engine parser replacement.

## Changed files and identifiers

The audit patch changed `common/decisions/006_independence_wave_far_eastern_decisions.txt` for `independence_wave_fer_register_fer_communities` and `independence_wave_fer_codify_durable_sovereignty` cost localisation, plus removal of the strategic decision's civilian-factory commitment.

The audit patch changed `common/decisions/categories/006_independence_wave_far_eastern_categories.txt` to add the current-generation visibility guard.

The audit patch changed `localisation/english/006_independence_wave_far_eastern_l_english.yml` for `independence_wave_fer_hold_railway_council_desc`, `independence_wave_fer_cost_administration_standard`, and `independence_wave_fer_cost_strategic`.

The audit patch changed `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt` to remove the strategic civilian-factory payment gate.

A concurrent parent/other-agent worktree change in the same decision file adds host-loss versus living-host tooltip branching for `independence_wave_fer_settle_former_host_ledgers`; it was preserved and is not claimed as this audit's patch.

A concurrent parent capital-preflight repair in the same trigger file changes the dormant 563 handling and fixed 408/409 capital-anchor availability; it was preserved and is not claimed as this audit's patch.

The required handoff is this file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw057_fer_decision_mission_audit_current_2026_08_15.md`.

## Validation and skipped validation

A localisation reference scan checked 40 unique FER decision and mission references and found no missing keys.

Brace counts matched in the touched decision source, FER trigger source, FER effect source, and FER category source.

The FER localisation BOM was present, and touched script sources contained no unsupported `>=` or `<=` operators.

The GUI inspect and render artifacts above were generated after the source patch.

The probability inspect artifacts above were generated after the source patch.

A live Hearts of Iron IV launch or gameplay session was not run because repository instructions reserve live consumer validation for the user.

A probability baseline/compare through `chaosx_ai_probability_auditor` was not run because that worker route was unavailable and no weighted AI value was changed.

A GUI rewrite was not run because there is no package-owned GUI to rewrite.

## Remaining issues and recommended next steps

The parent should retain IW-057 fail-closed until identity/roster/flag receipts, typed scenario probability evidence, and central adapter/attestation/preflight/Join wiring are accepted.

After a callable `chaosx_ai_probability_auditor` route exists, rerun the same named IW-057 mission scenarios with typed FER fixtures and record baseline and compare evidence before any AI-weight change.

The parent should decide whether the package-local 45/75/105 project-duration constants are intentional dead tuning data or whether the decisions should adopt them in a separate balance-approved change.

The parent should reconcile the concurrent host-ledger tooltip branch with the package documentation and preserve its host-loss no-bilateral-delta behavior.

The ordinary shared country-decision window is adequate for this package's current action count and text density; no dedicated GUI redesign is recommended from this audit.

## Simplifications, omissions, and blockers

No requested decision or mission was omitted from the source audit.

No central admission, Join, or unrelated balance change was made.

The only material evidence limitations are the unavailable worker probability route, empty-fixture MCP probability results, truncated shared-window render response, deferred central cleanup invocation, and the unresolved package-duration tuning-source question.

No commit or staging was performed.
