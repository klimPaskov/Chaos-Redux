# Event 020 decision cost budget and payment trace handoff

Disposition: implemented for the cost-budget cleanup explicitly approved by the parent on 2026-10-05. The accepted basis is the parent's five terminal/shared-action maps and the later authorization to clean up the ordinary shared-state profile. This is a bounded quote, affordability, debit, commitment, and tooltip correction; it does not change AI weights or create a mechanic.

## Changed files

- `common/scripted_effects/020_black_plague_terminal_response_effects.txt`
- `common/scripted_triggers/020_black_plague_terminal_response_triggers.txt`
- `common/script_constants/020_black_plague_terminal_response_constants.txt`
- `common/scripted_effects/020_black_plague_shared_response_effects.txt`
- `common/scripted_triggers/020_black_plague_shared_response_triggers.txt`
- `common/script_constants/020_black_plague_shared_response_constants.txt`
- `common/decisions/020_black_plague_shared_response_decisions.txt`
- `localisation/english/020_black_plague_response_l_english.yml`

No commit was created. The global Black Friday price registry, unrelated country-level project costs, response outcome effects, action durations, target selectors, mission resolution, and category/UI implementation were not changed.

## Resulting cost profiles

The player-facing inline rows show at most three amount tokens. Each blocked alias mirrors those visible values in red. Full tooltips show every fee or committed resource and label the launch payment, civilian factory commitment, Response Capacity commitment, and duration separately. A capacity or duration value is never presented as a material payment.

| Action | Spendable fees after patch | Actual commitments | Baseline and quote source |
| --- | --- | --- | --- |
| `last_response_hold` | support equipment, infantry equipment, manpower | 3 civilian factories | 180 support, 300 infantry, 4,500 manpower; dynamic Black Friday quotes |
| `last_response_refuge` | motorized equipment, manpower, fuel | 4 civilian factories | 120 motorized, 5,000 manpower, 1,900 fuel; dynamic Black Friday quotes |
| `strike_royal_node` | infantry equipment, fuel | 3 civilian factories, 2 Response Capacity | 250 infantry, 1,200 fuel; dynamic country-price quotes; 120 days |
| `strike_the_crown` | infantry equipment, fuel | 5 civilian factories, 5 Response Capacity | 500 infantry, 2,400 fuel; dynamic action-specific quotes; 180 days |
| `seal_royal_burrows` | support equipment, fuel | 3 civilian factories, 3 Response Capacity | 180 support, 1,600 fuel; dynamic action-specific quotes; 180 days |

The Hold and Refuge project checks still require Stability and War Support at or above their existing 20% floors. Those are eligibility thresholds, not fees. Their civilian factories remain committed by the existing native decision modifiers for the 120-day missions. The last-response launch window remains one day.

The three Royal actions retain their existing active capacity and native factory reservations. Royal Node now also checks its civilian factory availability and 2-point Response Capacity before launch; its custom-cost trigger, `available` trigger, and cost row use the same two direct quotes and two commitments. Crown Strike and Royal Seal already checked their direct quotes, civilian factory use, and Response Capacity thresholds in the shared triggers. Their state-selected launchers remain zero-day launchers, while the 180-day native missions own the work and cleanup.

The action-specific price-table fields for removed Crown Strike and Royal Seal fees remain registered, but their constants now resolve to zero. The registry keys are retained for Black Friday; no shared country motorized, train, or command-power value was reduced. Country-level projects still quote and pay their original motorized, train, and command-power fees.

## Ordinary selected-state action matrix

All 26 ordinary state-targeted actions now spend the selected state's population-band support and fuel quotes only. Before this patch the common bundle also charged motorized equipment; three named actions added trains and two added command power. Those five action-specific fees and gates are removed only from their exact state-action paths. The support/fuel/civilian-factory/Response-Capacity profile has four distinct direct-or-committed resource types. Existing population scaling, factory modifiers, response burdens, effects, targets, mission timers, and cancellation cleanup remain in place.

Outside Black Friday sale modifiers, the population-band fees are 45 support plus 450 fuel below five million people, 90 support plus 900 fuel from five million, and 120 support plus 1,200 fuel from ten million. The selected-state quote functions, the affordability gate, and the debit all read the same registered Black Friday price-table fields for the chosen band.

| State action | Civilian factories | Response Capacity | Existing duration |
| --- | ---: | ---: | ---: |
| `sentinel_surveillance` | 1 | 2 | 60 days |
| `inspect_transport_hubs` | 1 | 2 | 35 days |
| `stronger_prevention_law` | 1 | 2 | 120 days |
| `close_threatened_corridor` | 1 | 2 | 30 days |
| `port_inspections` | 1 | 2 | 45 days |
| `restrict_troop_routes` | 1 | 2 | 30 days |
| `preposition_field_hospitals` | 1 | 2 | 45 days |
| `suspend_civilian_travel` | 1 | 2 | 30 days |
| `relief_corridor` | 1 | 2 | 45 days |
| `burial_sanitation` | 1 | 2 | 35 days |
| `seal_all_transport` | 2 | 3 | 14 days |
| `evacuate_threatened_perimeter` | 1 | 2 | 30 days |
| `foreign_medical_mission` | 2 | 2 | 90 days |
| `maintain_containment` | 1 | 2 | 90 days |
| `controlled_reopening` | 1 | 2 | 60 days |
| `trace_residual_clusters` | 1 | 2 | 56 days |
| `rotate_exhausted_personnel` | 1 | 2 | 30 days |
| `restore_local_administration` | 2 | 2 | 90 days |
| `rebuild_hospitals_transport` | 2 | 3 | 120 days |
| `support_surviving_households` | 2 | 2 | 120 days |
| `preserve_sentinel_surveillance` | 1 | 2 | 180 days |
| `remove_emergency_restrictions` | 1 | 2 | 30 days |
| `fortify_cordon_line` | 2 | 2 | 60 days |
| `armored_clearance` | 1 | 2 | 45 days |
| `air_reconnaissance_sweep` | 1 | 2 | 21 days |
| `liberate_and_quarantine` | 2 | 3 | 90 days |

The heavy burden of 3 is retained only for `seal_all_transport`, `rebuild_hospitals_transport`, and `liberate_and_quarantine`; all other listed actions retain the medium burden of 2. Existing non-spendable requirements also remain separate: Armored Clearance requires the existing infantry equipment stock floor, and Liberate and Quarantine requires a containment force in the selected state.

## Payment and cleanup trace

For an ordinary selected-state action, the decision's `custom_cost_trigger` calls `black_plague_shared_country_can_pay_scaled_selected_state`. Human players price the selected board state; AI evaluation checks through the state-specific target logic. `black_plague_shared_state_can_pay_scaled_materials` selects the same three population bands as the start effect and checks only support equipment and fuel against the same live Black Friday quote variables. Each affordability check is `NOT = { native getter < quote }`, so the source condition accepts exact equality. No manpower getter is used in this profile.

`black_plague_begin_shared_state_action` sets the selected state, owner, action scale, burden, and active marker. The ordinary payment branch reads the selected band's support and fuel quote, debits those same values, credits the Black Friday purchase, registers the state response, and recomputes remaining Response Capacity. It no longer reads or debits motorized equipment, trains, or command power. The three former train gates and the two former command-power gates were also removed from the corresponding action selectors. Completion and cancellation continue through the existing shared finish/cancel effects; these clear the active state receipt and recompute capacity. No material refund existed, and no refund behavior was added.

The Royal Node/Crown Strike/Royal Seal payment branches use the exact same registered direct quote keys as their affordability helpers. Their tooltips display the actual direct quote plus their existing factory and response commitments. The corresponding mission completion, timeout, and cancellation outcomes remain unchanged.

Hold removes the current support, infantry, and manpower quotes, then records its purchase. Refuge removes the current motorized and fuel quotes and spends the current manpower quote, then records its purchase. Both decisions and payment helpers use the same inclusive stockpile or manpower boundary. Factory availability uses a negated `<` check, and the stability and war-support floors remain inclusive. Success, timeout, terminal checks, one-day launch window, and the existing mission lifecycle are unchanged.

## Localisation and selectors

The 26 ordinary cost families in `localisation/english/020_black_plague_response_l_english.yml` now have a three-value inline row and blocked alias plus a full tooltip showing all four direct/committed resource types and the duration. Their previous train and command amounts are removed from every quote row and tooltip. The three Royal action families show their two direct fees and civilian factory amount inline, with Response Capacity and duration in the full tooltip. Hold and Refuge retain three direct inline fees, with factory commitment and mission duration in the full tooltip. The seven bounded prose edits in this file replace generic bookkeeping terms with the existing medical, logistics, and charter activities; they do not change effects, costs, timers, or benefits.

A repository-wide search found the legacy `black_plague_shared_action_cost`, `_blocked`, and `_tooltip` strings only at their three localisation definitions and in historical audit artifacts; no current source consumer references them. They still describe the country-level support/motorized/fuel bundle, so they were left unchanged and are not counted as an active selected-state quote.

The 26 ordinary state actions all live in the shared `chaosx_disease_containment_category` and share `black_plague_response_decisions_are_visible`, gated by direct-response eligibility plus AI status or the shared disease board being selected. Their state-specific `target_trigger` functions restrict the map states, but there is no phase or family pagination gate in source. MCP scenario counts could not be confirmed because decision inspection timed out; the dedicated GUI worker owns visual inspection/render evidence. This remains a source-level cognitive-load risk for parent review, and no category redesign was included in this bounded cost patch.

## Evidence and validation

A source-contract audit parsed all 26 ordinary selected-state decision definitions and matched each `custom_cost_text`, factory modifier, duration constant, active capacity burden, affordability helper, and payment branch. It checked the 26 base/blocked/full-tooltip families, the three Royal action families, and both terminal response families for exact fee/icon coverage and four-or-fewer direct-or-committed types. The audit confirmed the three population-band gates and payment selectors match and accept equality using negated native `<` checks. It confirmed generic country-level motorized costs remain in the country-materials path and Black Friday registration remains intact.

The offline wiki `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:308-321` describes the custom-cost base, `_blocked`, and `_tooltip` key forms. The installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md:1-24` was read for native decision trigger/modifier context; it has no custom-cost-specific section. Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/ITA.txt:2553-2555` pairs a custom cost trigger with a localized two-resource cost key. The installed effect documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:1252-1266` supports country-scope `add_equipment_to_stockpile`, a variable `amount`, and negative amount removal. The repository's existing generic support debit/grant precedent is `common/scripted_effects/chaosx_dynamic_effects.txt:750-752`; the exact-archetype anti-tank transfer precedent is `common/scripted_effects/019_infantry_spawn_management_effects.txt:2802`. A focused `hoi4.script_validate` call confirmed command kind and country scope for the 018 stockpile grants, but left both native argument blocks unchecked (`SCRIPT_CHECK_PARTIAL`, `parametersChecked=false`). This is source/documentation evidence, not proof of an in-game equipment-level result.

`hoi4.reference_context` and `hoi4.decision_inspect` for the in-scope surface timed out after 600 seconds. The Event 018 `hoi4.gui_inspect` call also timed out; the parent reports dedicated Event 018 and Event 020 GUI workers own the required inspection/render attempts. No GUI route was retried. AI probability work and any comparison are owned by the separate probability auditor; no AI weight changed here.

No `.tools` or `.tools/validation` test covers Event 020 decision cost profiles, response reservations, or quote/payment parity. The existing Event 018 field-value-slot and Event 020 outbreak-entry tests cover different GUI and trigger surfaces and were not run. The task-specific source-contract audit is not an engine-runtime test. All user-live gameplay evidence remains outstanding.

## Remaining issues and limits

The shared response category still exposes 26 state-target action selectors behind one common visible gate; source does not prove how many matches a concrete scenario presents at once. The native effect's argument parameters for the exact anti-tank/support stockpile transfers were not checked by the MCP validator, although their command kind, scope, installed documentation syntax, and existing archetype precedents align. Decision inspection and matching production GUI evidence are blocked by the inspector timeout and remain with the parent and dedicated GUI worker. No AI probability comparison was run by this cost-only owner.
