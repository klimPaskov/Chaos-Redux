# Repression site-cost parameter startup repair plan

Disposition: `implemented` for the accepted source migration, with runtime validation and unresolved GUI presentation evidence retained as limits.
Acceptance basis: the parent explicitly accepted the eight-TXT-file and owner API Markdown migration after reviewing this plan and delegated guarded implementation within the user's safe parser-repair authorization.
Scope: launch_08 first-cause diagnosis and behavior-preserving migration of the directly linked site-cost API.
Implementation evidence: `repression_parameter_evidence/migration_manifest.json`, `application.json`, and `source_validation_live.json` record the 114 exact call mappings, guarded nine-file application, and source-level boundary validation.
The parent owns live validation and final acceptance.
The implementation handoff is `repression_parameter_implementation_handoff.md` in this directory.
No files were staged or committed.

## First cause and cascades

Authoritative evidence: `logs/launch_08/logs/error.log` relative to this directory.
Log line numbers below refer to that archived launch, while source locations can move under concurrent work.

| Evidence | Diagnosis |
| --- | --- |
| Log 565–566, decision source line 306 | First reported failure in the requested decision file is `camp_rework_can_pay_site_labor = { STATE = FROM }`, with invalid scope type `STATE` and invalid value `{`. |
| Log 567–576, decision source 364 onward | The second labor gate breaks parsing inside `available`. Later `OR`, `NOT`, `FROM`, effects, and category errors are consistent with lost parser context after the unsupported argument block. Preserve their existing nesting rather than deleting valid triggers or categories. |
| Log 1090–1092, trigger source 7 and 110 | The quote helper contains literal `$STATE$`, reported as an invalid trigger. Its nested quote call also supplies `{ STATE = $STATE$ }`, reported as an invalid value. These are direct defects in the helper contract. |
| Log 1093 onward | The purported scripted-trigger declaration named `check_variable` is a cascade after the nested quote call. The source has a normal native `check_variable` inside the affordability helper. Do not rename the native trigger. |
| Log 876 onward, site-cost scripted localisation source 9 | The first direct quote call breaks parsing before later localisation branch errors. Treat subsequent `NOT`, `localization_key`, and `defined_text` diagnostics as likely cascades, subject to a fresh parser pass. |
| Log 2560 onward, dispatcher source 114 | The labor affordability argument block is rejected first. `NOT`, `OR`, state-validity triggers, and infrastructure are then read as effects. |
| Log 2573–2575, dispatcher source 135 | The payment call independently exposes `STATE` as an invalid effect. Both the trigger and payment interfaces need migration. |

The supported repair is boolean helper invocation plus explicit temporary inputs.
This conclusion is specific to the current `$STATE$`/`STATE` API and the installed parser evidence.
It does not justify rewriting unrelated block syntax or assuming every diagnostic elsewhere has the same cause.
Installed `documentation/triggers_documentation.md:7482` explicitly supports `set_temp_variable` in triggers, and `:5166` supports conditional `if` triggers.
Neither temporary arithmetic nor the quote's conditional rounding should be removed as supposedly effect-only syntax.

## Pre-migration call inventory

An exact helper-ID search across runtime `common` and `events` found 11 definitions and 114 parameter calls in eight TXT files.
There are 104 external calls and 10 calls between helpers.
Argument forms are 39 `FROM`, 51 `var:camp_selected_state_id`, 14 `var:camp_rework_action_state_id`, and 10 forwarded `$STATE$`.
No callers of these IDs were found in event files.
The decision file received concurrent `ai_hint_pp_cost` additions during this inspection, so its current positions below differ from archived launch positions.
Re-enumerate exact IDs before applying a patch and preserve those concurrent edits.

Paths in this table are relative to `common/`.

| File | Calls | Current call lines |
| --- | ---: | --- |
| `decisions/camp_repression_generic_decisions.txt` | 12 | 307, 365, 425, 483, 681, 731, 775, 787, 812, 832, 854, 871 |
| `scripted_effects/camp_repression_action_dispatcher_effects.txt` | 14 | 114, 135, 143, 163, 179, 184, 208, 209, 219, 220, 229, 236, 243, 248 |
| `scripted_effects/camp_repression_rework_effects.txt` | 12 | 3907, 3920, 3980, 3984, 4018, 4021, 4069, 4076, 4089, 4093, 4106, 4111 |
| `scripted_effects/camp_repression_site_cost_effects.txt` | 5 | 14, 36, 48, 67, 86 |
| `scripted_triggers/camp_repression_site_cost_triggers.txt` | 5 | 110, 119, 127, 138, 147 |
| `scripted_guis/camp_repression_ledger_scripted_gui.txt` | 6 | 494, 530, 539, 547, 557, 567 |
| `scripted_localisation/camp_repression_ledger_scripted_localisation.txt` | 6 | 774, 805, 815, 824, 834, 844 |
| `scripted_localisation/camp_repression_site_cost_scripted_localisation.txt` | 54 | 9, 17, 28, 36, 48, 57, 69, 78, 90, 99, 111, 120, 132, 141, 153, 162, 173, 181, 192, 200, 211, 219, 230, 238, 250, 259, 271, 280, 291, 299, 310, 318, 329, 337, 348, 356, 368, 377, 389, 398, 409, 417, 428, 436, 447, 455, 466, 474, 485, 493, 504, 512, 525, 538 |

The six decisions are `generic_redirect_labor_to_construction`, `generic_redirect_labor_to_resource_extraction`, `generic_restricted_contaminated_site_escalation`, `generic_destroy_evidence_before_retreat`, `generic_inspect_active_site`, and `generic_dismantle_detention_network`.
Each owns an affordability check in `custom_cost_trigger` and another in `available`.
The six GUI effect consumers are `camp_rework_gui_start_labor_project`, `camp_rework_gui_inspect_selected_site`, `camp_rework_gui_begin_selected_dismantlement`, `camp_rework_gui_destroy_selected_evidence`, `camp_rework_gui_apply_selected_chemical_method`, and `camp_rework_gui_apply_selected_biological_method`.
The labor effect declaration was confirmed directly at source line 3899.

## Accepted helper contract

Retain all helper IDs and country scope.
Replace the `STATE` argument with required unscoped temporary `camp_site_cost_state_id`.
Only the quote calculator enters `var:camp_site_cost_state_id` to read the three building levels.
Affordability reads the original country's political power, equipment, manpower, and command power, and payment debits that same country.
Do not invoke the whole affordability or payment helper from state scope or substitute owner/controller as payer.

| Existing helper ID | Calls | Outputs and side effects preserved |
| --- | ---: | --- |
| `camp_rework_prepare_site_cost_quote` | 64 | Deterministic `camp_site_quote_*` temporary outputs, existing minimum level and rounding. No country/state mutation. |
| `camp_rework_can_pay_site_labor` | 9 | Boolean affordability using PP and payment-plus-reserve equipment balances. |
| `camp_rework_can_pay_site_inspect` | 6 | Boolean PP affordability. |
| `camp_rework_can_pay_site_dismantle` | 6 | Boolean PP, manpower_k, and support-equipment affordability. |
| `camp_rework_can_pay_site_evidence` | 6 | Boolean PP, manpower_k, CP, and support-equipment affordability. |
| `camp_rework_can_pay_site_restricted` | 10 | Boolean administrative PP affordability. Existing route and stock predicates remain separate. |
| `camp_rework_pay_site_labor` | 3 | PP and equipment debit once, preserving three country reserve snapshots. |
| `camp_rework_pay_site_inspect` | 2 | PP debit once. |
| `camp_rework_pay_site_dismantle` | 2 | PP, manpower, and support-equipment debit once. |
| `camp_rework_pay_site_evidence` | 2 | PP, manpower, CP, and support-equipment debit once. |
| `camp_rework_pay_site_restricted` | 4 | PP debit once. |

Initialize the required input at every external call site within the same enclosing effect or trigger evaluation.
For targeted decisions and their localisation use `set_temp_variable = { camp_site_cost_state_id = FROM.id }`, matching the existing decision completion contract that stores `camp_rework_action_state_id = FROM.id`.
For selected ledger calls copy `camp_selected_state_id` as the value without the `var:` scope prefix.
For dispatcher calls copy `camp_rework_action_state_id` the same way.
Then invoke the helper as `helper_id = yes`.
The ten nested helper calls use `= yes` and consume the already initialized input.
The sole `$STATE$` scope in the quote becomes `var:camp_site_cost_state_id`.

Example positive gate:

```txt
set_temp_variable = { camp_site_cost_state_id = FROM.id }
camp_rework_can_pay_site_labor = yes
```

Example negative localisation gate:

```txt
set_temp_variable = { camp_site_cost_state_id = camp_selected_state_id }
NOT = { camp_rework_can_pay_site_labor = yes }
```

Place input initialization outside the `NOT` in all six ledger status branches.
Do not insert an always-successful variable setter as a peer alternative inside `OR`.
Preserve conjunction and negation through an enclosing `AND`/existing trigger block if needed.
Initialize again for the payment call rather than relying on a temporary created in its preceding `limit` surviving into the effect body.
Preserve every existing caller initialization of retained quote outputs, including red/normal localisation branches and reserve values.

The API has no default target.
Preserve existing target-validity and action guards and test missing/invalid targets explicitly.
Do not turn an absent state into a capital quote or a persistent selected-state update.
The current calculator's `always = yes` does not establish a reliable invalid-target contract, so startup repair alone cannot claim that boundary validated.

## Migration, tuning, and lifecycle

Apply the eight-file migration atomically with `common/scripted_effects/camp_repression_site_cost_effects.md` updated for the boolean API, required temporary input, nested forwarding, retained outputs, and examples.
No new generic registry helper is needed.
The existing `chaosx_dynamic_effects.txt` and matching Markdown were inspected and already use country-scoped boolean helpers with caller-supplied temporaries.
The owner-local API remains the right location.

Keep `common/script_constants/camp_repression_site_cost_constants.txt` and all `camp_site_cost` tuning unchanged.
Keep all formulas, inclusive comparisons, reserve ceilings, resource types, action payloads, and existing AI hints/weights unchanged by this migration.
No event target, flag, on-action, or persistent input cache is added.
The new temporary input expires with its evaluation context and requires no save cleanup.
Preserve `camp_rework_clear_site_labor_reserve` and its existing success/failure/cancellation consumers unchanged.
Do not alter the legacy fixed-cost labor entry point or duplicate debit behavior while repairing the selected-location entry point.

## Evidence and validation conditions

Required references consulted include AGENTS.md, the core offline wiki pages, Interface modding, Scripted GUI modding, the events/decisions/subagents skills, and the scripted-GUI skill for linked consumer inspection.
Relevant detailed references are offline Data structures temporary-variable lifetime/scoping, Effects scripted-effect boolean invocation, installed trigger/effect `set_temp_variable`, installed script constants documentation, and installed `common/scripted_guis/_documentation.md`.
Installed vanilla `common/scripted_triggers/GER_scripted_triggers.txt:151` (`GER_should_split_SOV_front_with_ITA`) demonstrates temporary arithmetic in a scripted trigger.
The Event16 repair identified by the parent is corroborating project precedent, not proof that repression target semantics were already validated.

`hoi4.event_inspect` was called with selector `{kind: "file", sourcePath: "common/decisions/camp_repression_generic_decisions.txt"}`, downstream depth 2, 45 nodes, 90 edges, and `expandHelpers: true`.
It returned `EVENT_INSPECTED_PARTIAL`, revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`, `helpers: 0`, and `validation.passed: false`.
Its explicit limitation is that large-workspace analysis deferred helper projections and lifecycle passes.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f775749d6ba0dc959c6fccf68384d9c5f622ab4b19fd5af03b8d646dd3ee029/e73bdf70ad0f8dadac38256757aa0682deaa281656d8eed2c54bdd1eda5212e0/event-trace-1102e50fad94.json`.
This trace cannot validate quote, payment, scope, or temporary-lifetime behavior, despite the requested helper expansion.

`hoi4.gui_inspect` was called for `repression_ledger_window`, scenario `repression_parameter_startup_selected`, 1920×1080, UI scale 1, and generated scenarios disabled.
It returned `GUI_INSPECTED`, revision `b5770253120dcdd2b8baf6fa6d999b60365ae3125616b96f4ab93a68bb23ade2`, 107 inspected elements, and a passing source-link graph check, while overall `validation.passed` was false.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a33b90356ebb00c6c0f90c8540e3c997f1dc1ea5869b2708b8780c74309ef7ca/02f140ca503b10fd6cdba91fca738be5744e0763c31d379a4b524f763edb22e7/gui-inspect.b5770253120dcdd2.json`.
This bounded dependency inspection supplied no runtime visibility or dynamic values, so it reported conflicting click regions among controls from multiple tabs and unresolved localisation values.
Those diagnostics remain unresolved and parent-owned.
A visual or action-state acceptance claim requires the existing explicit per-control fixtures, since this minimal fixture cannot establish which controls coexist at runtime.
No GUI rendering, source rewrite, or visual acceptance was performed in this parser-only assignment.

Before accepting the owner-applied repair:

1. Re-enumerate the 11 definitions and 114 calls against current source, with a behavior diff covering every changed invocation and retained output initializer.
2. Confirm the first-cause signatures and their cascades disappear in the next parent-owned parser validation, then investigate any remaining errors independently.
3. Exercise quote/gate/payment identity for decision FROM, selected ledger state, and dispatcher state while the ledger selection differs from the action target.
4. Check marker-only, Gulag-only, and combined-building sites, exact balances, each one-resource shortage, single debits, reserve retention, and labor cleanup.
5. Check successive quotes for two different states and repeated red/normal localisation evaluations to detect temporary input/output leakage.
6. Check both positive and negated affordability contexts, missing selected state, and invalid action state without introducing fallback targets.
7. Require matching MCP inspection/render evidence for the existing ledger controls if their scripted calls are migrated, preserving the layout and source identity.
8. If changes extend into AI scoring or weighted target logic, the parent must route the required baseline and comparison through the probability auditor before claiming AI validation.

The diagnostic evidence above describes the state before implementation.
The accepted source migration is applied and source-validated, with final MCP comparison and remaining limits recorded in the implementation handoff.
No probability values, GUI layout, or action design were changed.
No runtime scope proof, live payment execution, or live-game acceptance is claimed.
No simplification was made.
