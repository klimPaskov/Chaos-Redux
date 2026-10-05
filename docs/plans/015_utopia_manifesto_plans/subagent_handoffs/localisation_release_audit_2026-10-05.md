# Event 015 Localisation Release Audit Handoff, 2026-10-05

## Disposition

Status: the assigned release-copy audit and the follow-up G6 growth-decision cost sync are implemented. The G6 acceptance basis is the parent-approved final payment matrix in the task messages on 2026-10-05; the decision owner confirmed the matching source and consumer-localisation edits.

The accepted basis is the user-authorized release review recorded in `docs/plans/015_utopia_manifesto_plans/agent_decisions_2026-10-05.md`, especially its sections on concise choices and factual reports.

This handoff covers nine English localisation files with 1,590 quoted values. It reviewed all 1,590 values, including 35 GUI-family values in the main localisation file that remained read-only under `resume015_gui` ownership, and made targeted edits only within its assigned scope.

The focus localisation and the decision-completion file remain under their assigned owners, except for the two Auxiliary gift amount references changed under the parent's narrow G6 authorization below. My all-Event-015 literal scan now finds none of the forbidden visible terms `id`, `record`, `segment`, `snapshot`, `transaction`, `receipt`, `ledger`, `pilot`, or `provider`. It also finds no update-history wording or achievement-route advertising.

## Changes

`localisation/english/015_utopia_manifesto_events_l_english.yml` contains 66 edited keys. Sixty-four option labels that exceeded the agreed 41-character rough cap were shortened without changing IDs or scripted effects. The two district reports now describe the unfinished housing, transport, and facilities, and the challenged compulsory charter, without listing mechanic values.

The edited option identifiers are `chaosx.nr15.2.b`, `chaosx.nr15.3.b`, `chaosx.nr15.3.c`, `chaosx.nr15.4.a`, `chaosx.nr15.5.b`, `chaosx.nr15.9.c`, `chaosx.nr15.11.c`, `chaosx.nr15.12.a`, `chaosx.nr15.13.c`, `chaosx.nr15.15.a`, `chaosx.nr15.15.c`, `chaosx.nr15.21.a`, `chaosx.nr15.22.a`, `chaosx.nr15.23.a`, `chaosx.nr15.23.c`, `chaosx.nr15.30.b`, `chaosx.nr15.31.c`, `chaosx.nr15.31.option_d`, `chaosx.nr15.32.a`, `chaosx.nr15.32.b`, `chaosx.nr15.32.option_d`, `chaosx.nr15.40.c`, `chaosx.nr15.40.e`, `chaosx.nr15.42.a`, `chaosx.nr15.43.b`, `chaosx.nr15.44.b`, `chaosx.nr15.51.b`, `chaosx.nr15.51.c`, `chaosx.nr15.53.a`, `chaosx.nr15.53.c`, `chaosx.nr15.53.option_d`, `chaosx.nr15.60.a`, `chaosx.nr15.61.b`, `chaosx.nr15.62.b`, `chaosx.nr15.62.c`, `chaosx.nr15.62.e`, `chaosx.nr15.63.c`, `chaosx.nr15.64.a`, `chaosx.nr15.70.b`, `chaosx.nr15.73.c`, `chaosx.nr15.74.a`, `chaosx.nr15.74.b`, `chaosx.nr15.74.c`, `chaosx.nr15.81.a`, `chaosx.nr15.83.a`, `chaosx.nr15.90.b`, `chaosx.nr15.90.c`, `chaosx.nr15.93.b`, `chaosx.nr15.101.c`, `chaosx.nr15.102.b`, `chaosx.nr15.105.b`, `chaosx.nr15.106.c`, `chaosx.nr15.107.b`, `chaosx.nr15.109.b`, `chaosx.nr15.110.a`, `chaosx.nr15.113.a`, `chaosx.nr15.120.c`, `chaosx.nr15.121.c`, `chaosx.nr15.122.c`, `chaosx.nr15.123.c`, `chaosx.nr15.210.e`, `chaosx.nr15.215.b`, `chaosx.nr15.217.b`, and `chaosx.nr15.219.b`.

The two report keys are `chaosx.nr15.45.obligations.d` and `chaosx.nr15.46.d`. The existing `.47.d` text remains tied to the frozen, actual casualty value and was not changed.

The fourteen main-file keys are `utopia_manifesto.district.reason.no_suitable_role`, `utopia_manifesto.district.reason.control_lost`, `utopia_manifesto.district.reason.survey_at_risk`, `utopia_manifesto.district.reason.core_lost`, `utopia_manifesto.district.reason.obligations_at_risk`, `utopia_manifesto.district.reason.obligations_failed`, `utopia_manifesto.district.reason.charter_invalid`, `utopia_manifesto.district.reason.clear`, `decision_utopia_close_the_gates_desc`, `decision_utopia_attach_penal_works_to_district_desc`, `utopia_manifesto_reject_cleanup_tt`, `decision_utopia_repeal_the_founding_charter_desc`, `mission_utopia_repeal_the_founding_charter_desc`, and `decision_utopia_survey_district_site_effect_tt`.

`localisation/english/015_utopia_manifesto_l_english.yml` contains the fourteen prose keys listed here plus the G6 gift-amount display key. Eight district-reason strings gained terminal punctuation. The close-gates description no longer implies manpower or Stability payments that the decision does not charge. The Penal Works description no longer duplicates live price variables as fixed amounts. The repeal description likewise no longer repeats fixed PP, Stability, support-equipment, and train values, while its native cost and dynamic tooltip remain intact. The district survey tooltip and repeal text replace their semicolon joins with complete sentences, and the rejection and cancellation notices retain their wording with plain punctuation. The added `utopia_manifesto_auxiliary_support_gift_amount` value renders the current gift constant through `[?temp_gift|0]` for the scripted getter.

`localisation/english/015_utopia_manifesto_evolution_consumption_l_english.yml` has three corrected Closed Order price keys. Its normal and blocked custom rows display infantry equipment, support equipment, and command power. Its tooltip names those three live prices and the displayed PP price.

The two policy decisions remain distinct. `decision_utopia_enforce_closed_order` charges native PP plus infantry equipment, support equipment, and command power. `decision_utopia_close_the_gates` still charges native PP plus infantry equipment, support equipment, and Army XP. The source decision, custom-cost trigger, and payment helper were checked against the corresponding localisation rows.

`localisation/english/015_utopia_manifesto_evolutions_l_english.yml` changes only `utopia_manifesto.evolution.5.body` to remove the one-path-versus-the-other construction while preserving its world-state premise.

`localisation/english/015_utopia_manifesto_release_feedback_l_english.yml` changes only `chaosx.nr15.98.already.d` to replace its semicolon with plain sentence structure. The `.97` and `.98` IDs and plain report values remain intact.

No gameplay cost, effect, event ID, quote, or attribution changed by this localisation subagent. Under the parent's narrow G6 authorization, this subagent added `GetUtopiaManifestoAuxiliarySupportGift` to `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt` and replaced the two Auxiliary gift amount literals in decision-completion localisation with that getter. The focus file, GUI-owned key families, assets, workbook, and CSV were not changed.

## Coverage and evidence

The event option inventory counted 290 `.a`, `.b`, `.c`, `.e`, and `.option_d` labels. Before patching, 64 exceeded 41 characters and the maximum was 45. After patching, all 290 are at or below 41 characters and the maximum is 41.

`python .tools/report_colour_audit.py --event 015` returned `total keys with colour: 0`, covering report and news descriptions and their reachable scripted-localisation output.

The relevant Event 015 source links support the two revised district descriptions. `events/015_utopia_manifesto.txt` routes `.45.obligations.d` from the district-debt state and `.46.d` from the challenged Closed Island charter. Its `.47` immediate block snapshots the last civilian loss before the report text is shown.

The Closed Order source mapping is `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` around lines 525-533, `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt` around lines 160-164, and `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt` around lines 541-620. Those files show PP large plus infantry large, support medium, and command power medium, with no Stability payment.

The separate Close Gates mapping is `common/decisions/015_utopia_manifesto_decisions.txt` around lines 2338-2355. It shows PP medium plus infantry large, support large, and Army XP medium, matching `utopia_manifesto_cost_close_gates` and its tooltip in the main English localisation file.

## Reference evidence

`hoi4.reference_context(surface=localisation)` succeeded in workspace `mod_chaos_redux_ea3b2d67c2c0`.

The offline wiki source `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, was read at lines 59-72 for the English YAML header, UTF-8 BOM, quoted one-line values, and key syntax, and at lines 656-705 for scripted-localisation selection and scope behavior.

The installed-game reference route identified `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_formatter_documentation.md`, revision `1fbd9a031fd09100d79bac08dec3c16e19468f23516c5e67c67578156282af08`. Its indexed section is only lines 1-2, the title for formatter documentation. The direct local file documents formatter consumers and has no further YAML authoring rules relevant to this prose-only patch.

The repository requires no `:0` suffix in localisation keys, following the applicable `AGENTS.md` rule. No key syntax was changed.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`. No skill files were created or edited.

## G6 growth-decision cost sync

Disposition: implemented. The parent explicitly accepted the final four-decision payment matrix on 2026-10-05. The decision owner confirmed that source and completion-localisation changes match it, and this subagent verified the non-owned Auxiliary gift display references against the source constant.

The parent-directed G6 contract covers `decision_utopia_raise_a_citizen_watch`, `decision_utopia_form_engineer_companies`, `decision_utopia_hire_auxiliary_contracts`, and `decision_utopia_reinforce_post_formation_defense`.

The decision owner confirmed the final G6 source and completion-localisation contract.

- Citizen Watch has no native PP charge or upfront payment. It requires the live four-resource formation stock and capacity to start training, checks affordability again at timeout, and charges manpower, infantry equipment, support equipment, and Army XP only if the formation is successfully created.
- Engineer Companies follows the same start gate and timeout recheck, with no native PP or Motorized fee. Successful formation consumes the same four dynamic resources; the infantry formation uses Infantry Equipment plus Engineer support.
- Auxiliary Contracts has no native PP, Motorized, or Convoy fee and no Motorized gift. It pays the four dynamic formation debits immediately and transfers Support Equipment to the selected neighbor. The current gift amount is the shared `support_medium` constant (50 units); its display is dynamic so future retuning does not leave a stale literal.
- Post-formation Reinforce has no native PP charge and pays the four dynamic formation debits immediately.

The Auxiliary support affordability total is `utopia_manifesto_auxiliary_total_support_equipment_cost`. The shared source computes it from the live formation Support Equipment cost plus `constant:utopia_manifesto_decision_cost.support_medium`, the 50-unit recipient gift (`common/scripted_effects/015_utopia_manifesto_effects.txt:7258-7259`). The source trigger gates the combined stock requirement before charging either payment (`common/scripted_triggers/015_utopia_manifesto_triggers.txt:3276-3284`). The decision owner's inline row displays Manpower, Infantry Equipment, and combined Support; its full tooltip also lists Army XP and distinguishes the formation debit from the gift to `[FROM.GetNameDef]`.

The parent's authorized dynamic display uses `GetUtopiaManifestoAuxiliarySupportGift` at `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt:843-852`. Its trigger sets `temp_gift` from the same `support_medium` constant and selects the real English localisation key `utopia_manifesto_auxiliary_support_gift_amount` at `localisation/english/015_utopia_manifesto_l_english.yml:413`. The two gift references in `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml` are the decision description at line 453 and the full cost tooltip at line 478. This keeps the amount dynamic without adding formatter characters to scripted localisation.

The affected completion-localisation keys are `decision_utopia_raise_a_citizen_watch_effect_tt`, `decision_utopia_form_engineer_companies_effect_tt`, `decision_utopia_hire_auxiliary_contracts_effect_tt`, and `decision_utopia_reinforce_post_formation_defense_effect_tt`, plus their four custom cost row families. The decision owner aligned the four rows and full tooltips to the contracts above. The two Watch/Engineer requirement strings now state that the live stock is needed to start and is checked again at the deadline, while their effect text makes clear that no fee is paid at training start.

This subagent changed only the two Auxiliary gift-value references in the decision-completion file under the parent's explicit narrow authorization. All other completion copy and custom cost rows remain under the decision owner's ownership.

The four formation fees, trained unit templates, duration rules, and capacity limits remain unchanged under the accepted source matrix. Source and localization parity was checked against `common/decisions/015_utopia_manifesto_decisions.txt:4910-5044,5770-5787`, the combined-stock source at `common/scripted_effects/015_utopia_manifesto_effects.txt:7258-7259` and `common/scripted_triggers/015_utopia_manifesto_triggers.txt:3276-3284`, the decision-completion strings listed above, and the dynamic gift getter. The Watch and Engineer start gate plus deadline recheck are now disclosed in their requirement copy.

## Remaining scope notes

The GUI-owned key `utopia_manifesto_ledger_gui_stores_left_tt` has also had its semicolon replaced. The GUI owner recorded the copy-only change in `gui_release_audit_2026-10-05.md` and reports that visual review remains unresolved. I did not edit any `_ledger_gui_`, `_ledger_tab_`, or `_ledger_button_` value.

The focus localisation was not edited. The decision owner remains responsible for the decision-completion file, its player-facing copy, and its cost mapping; this subagent made only the two authorized Auxiliary gift amount substitutions documented above. My cross-file prohibited-word scan is currently clean across all Event 015 English values.

No live-game or GUI rendering claim is made by this localisation audit. The shared GUI owner retains the visual review and its own evidence.
