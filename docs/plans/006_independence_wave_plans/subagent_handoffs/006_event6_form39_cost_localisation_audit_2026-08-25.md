# Event 006 FORM-39 Civil-Service Cost Localisation Audit

Date: 2026-08-25

Scope: The bounded localisation change for `independence_wave_form39_open_regional_civil_service` and its custom-cost trio.

## Verdict

PASS for the requested localisation-only patch. The new tooltip is compact, uses the correct civilian-factory texticon, and reports the same `civilian_factory_standard` amount already enforced by the existing source gate. The patch does not change payment, AI, timer, cancellation, cleanup, category membership, or any event/pre-event UI source.

One pre-existing source risk remains: the decision checks available civilian-factory capacity but does not declare a `civilian_factory_use` modifier while its 210-day project is active. This is outside the bounded localisation patch and is recorded for parent review rather than changed here.

## Issue list, sorted by severity

1. P2 residual design risk, pre-existing and not introduced by this patch: `can_pay_independence_wave_form39_civil_service_cost` reaches `can_pay_independence_wave_strategic_cost`, which checks `num_of_civilian_factories_available_for_projects > constant:independence_wave_decision_cost.civilian_factory_standard` at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:386-390`, but `common/decisions/006_independence_wave_form39_decisions.txt:121-149` has no `modifier = { civilian_factory_use = ... }`. Therefore `£civ_factory` is presently a capacity requirement, not a consumed or reserved payment. The old prose tooltip described the same requirement, so the localisation patch does not worsen or repair this behavior.

2. No patch-introduced issue found in the requested cost localisation trio.

## Exact source and localisation evidence

- `common/decisions/006_independence_wave_form39_decisions.txt:121-149` keeps the decision id, `visible`, `available`, `custom_cost_trigger`, `custom_cost_text`, 210-day `days_remove`, payment call, project flag, completion tooltip, cancellation trigger, cleanup effect, and `ai_will_do` unchanged.
- `common/scripted_triggers/006_independence_wave_form39_triggers.txt:207-221` keeps the post-formation carrier/member gates, 40 command-power gate, strategic stability/factory gate, standard diplomatic gate, major transport gate, and no-active-project gate unchanged.
- `common/scripted_effects/006_independence_wave_form39_effects.txt:167-170` is unchanged and still calls the strategic payment plus the second standard diplomatic payment.
- `common/script_constants/006_independence_wave_constants_registry.txt:1182-1186,1203-1206,1215-1224` defines the transport, command-power, stability, and `civilian_factory_standard = 2` values referenced by this surface.
- `localisation/english/006_independence_wave_formable_registry_l_english.yml:166-168` contains exactly one base, tooltip, and blocked key for the trio. The base remains `10% £stability_texticon`, `40 £command_power`, and the major transport display; the tooltip now appends `2 £civ_factory`; the blocked key retains the red versions and the same factory amount.
- `git diff --name-only --` limited to the four requested source paths reports only `localisation/english/006_independence_wave_formable_registry_l_english.yml`; the decision, trigger, and effect files have no worktree changes.

The custom-cost contract in `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:decision-cost` specifies that the base key is used when `custom_cost_trigger` passes, the `_blocked` key otherwise, and `_tooltip` is used on hover. The localisation page's text-icon section specifies the `£` notation. The installed vanilla precedent at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/decisions_l_english.yml:137-139` uses the same `decision_cost_civ_factory_2`, `_blocked`, and `_tooltip` trio, and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/texticons.gfx:172-173` defines `GFX_civ_factory` for `£civ_factory`.

## Cost and requirement clarity

- Base cost: the visible spendable palette remains stability, command power, and the two-unit standard transport path represented by convoy/train icons. The major transport gate is unchanged.
- Tooltip: the replacement is icon-first and compact: `$independence_wave_form39_civil_service_cost$` followed by the dynamic `civilian_factory_standard` amount and `£civ_factory`. It removes the previous prose sentence without losing the amount or source gate.
- Blocked cost: all affected values remain red, including the factory-capacity requirement, with no literal resource names.
- Cost-count audit: at most four spendable types are represented if convoy and train alternatives are counted separately: stability, command power, convoy, and train. Civilian factories are not consumed by `independence_wave_form39_pay_civil_service_cost`; they are a source requirement, so the patch does not add a hidden fifth spendable cost.
- Texticon audit: stability uses `£stability_texticon`, command power uses `£command_power`, transport uses `£convoy_texticon` and `£GFX_train_texticon`, and the capacity requirement uses the valid `£civ_factory`. No literal `Civilian Factories` fallback remains in the changed tooltip.
- Source/payment alignment: `independence_wave_decision_pay_strategic` removes standard stability and invokes one standard diplomatic payment, while FORM-39 invokes a second standard diplomatic payment. This preserves the existing 40 command-power and two-standard-transport payment shape behind the major transport gate; the patch only changes presentation.

## Decision lifecycle and mission-quality notes

- This is a timed project decision rather than a mission id. It has a 210-day timer, a project-active flag on selection, a completion effect on timer expiry, a cancellation trigger for loss of the carrier or bound members, and a cancellation cleanup effect that clears the active flag.
- The category contains the existing shipping, civil-service, plebiscite, and dissolution actions; the patch adds no action, mission, category, tab, or active-mission surface.
- No duplicate mission was introduced. No mission owner/category/region/requirement/duration/success/failure matrix is applicable beyond the timed decision lifecycle above.
- The completion tooltip remains `independence_wave_form39_open_regional_civil_service_tt`; the cost tooltip change does not alter the project outcome text.

## AI, route locks, cleanup, and exploit notes

- AI: `ai_will_do = { base = constant:independence_wave_decision_ai.high }` at decision line 149 is unchanged. No probability-bearing source changed, so a `chaosx_ai_probability_auditor` pass is not required for this localisation-only patch.
- Route validity: `is_independence_wave_form39_postformation_carrier`, bound-member, controlled-capital, and no-active-project checks remain source-enforced. No retired Independence Wave crisis, category, or pressure surface was inspected or revived.
- Cleanup: the existing cancellation and runtime cleanup hooks remain untouched. The localisation change cannot create stale flags or alter cooldown behavior.
- Exploit risk: the only follow-up concern is the pre-existing lack of `civilian_factory_use` reservation described under the P2 issue. The new tooltip accurately exposes the gate but does not create the underlying capacity behavior.

## Cognitive-load and UI notes

- Visible primary actions remain four in the federal compact category, below the six-action ceiling; this patch changes no action count or category density.
- No active mission count or new target control was added. The three existing timed project decisions remain distinct and source-gated.
- The changed visible value has clear significance: `2 £civ_factory` corresponds to the existing standard factory-capacity gate. The base cost continues to show the actual resource palette, while the hover text supplies the non-consumed capacity requirement.
- The tooltip is shorter than the replaced prose and contains no wall of text, raw trigger block, or literal resource-name fallback.
- No scripted GUI, dedicated mechanic window, event log, or pre-event visual layout is in scope for this YAML-only change.

## Validation and MCP evidence

- Static diff validation: target-scoped `git diff --check` produced no whitespace error; the target diff is one line removed and one line added in the English localisation file.
- Localisation validation: the file retains UTF-8 BOM bytes `EF BB BF`, and the three FORM-39 civil-service cost keys occur exactly once.
- Icon validation: the installed vanilla `texticons.gfx` contains one `GFX_civ_factory` definition backed by `gfx/texticons/civ_factory.dds`.
- Reference validation: the offline Decision modding and Localisation pages, vanilla decision localisation, vanilla texticon definition, vanilla trigger documentation for `num_of_civilian_factories_available_for_projects`, and vanilla `civilian_factory_use` precedent were consulted.
- GUI MCP evidence: not applicable to this bounded cost-localisation audit. No decision-owned scripted GUI or named window is linked to the changed keys, and no `decision_inspect` route is exposed by the installed `hoi4_agent_tools`; therefore `hoi4.gui_inspect`/`hoi4.gui_render` were not invoked for an unrelated layout surface. No live game or GUI proof is claimed.
- Probability MCP evidence: not applicable because the decision AI weight and all weighted source logic are unchanged.

## Recommended follow-up

No change is recommended for the requested localisation patch. If FORM-39 civil-service is intended to reserve two civilian factories throughout its 210-day project, review `common/decisions/006_independence_wave_form39_decisions.txt:131-133` against the vanilla `modifier = { civilian_factory_use = ... }` pattern and then align the base/tooltip/blocked wording with that chosen payment-versus-requirement model in a separate scoped change.

Simplifications or omissions in this audit: none within the requested localisation scope. Live gameplay and GUI validation were intentionally not claimed or performed.
