# Event 029 sealing cost profile audit

Status: read-only audit complete for `decision_riches_found_gold_seal_depths` and `decision_riches_found_demons_permanent_seal`. No gameplay source was changed. This handoff is the only file written for this task.

The requested cost profiles are present in the current decision blocks, cost triggers, and decision localisation. Cost-profile parity does not close the separate evacuation and casualty gaps below.

## Findings by severity

### High: the demonic permanent seal can bypass evacuation and entombment handling

`decision_riches_found_demons_permanent_seal` uses `riches_found_demons_district_cleared` in its `visible`, `available`, and `target_trigger` blocks. That helper accepts any of `riches_found_demons_district_evacuated`, `riches_found_workforce_evacuated`, or `riches_found_demons_military_purge`.

The separate `riches_found_seal_would_entomb_workforce` predicate treats a mine in severe collapse or supernatural crisis as unsafe to seal when the deposit is not exhausted and neither evacuation flag is set. Military purge does not satisfy either evacuation flag. The demonic decision does not call this predicate, and its AI weight rises during supernatural crisis without the entombment penalty used by the baseline permanent-seal decision.

The baseline permanent-seal decision calls `riches_found_record_entombment_harm` before `riches_found_permanently_seal_mine` and reduces AI willingness when the entombment predicate is true. The in-scope demonic decision calls only the permanent-seal helper. That helper closes the mine, clears active mine work, applies the permanent output loss, and records permanent-seal history, but does not record entombment harm.

Recommended parent fix: require an evacuation receipt or an exhausted deposit before this permanent seal can resolve, and apply the existing entombment consequence if the accepted route permits sealing with people still trapped. Mirror the safety condition in AI. Do not treat military purge as equivalent to evacuation.

### Medium: the gold-seal route has no emergency-phase or integrity threshold gate

The gold-seal decision is gated by a gold layer and `riches_found_gold_route_is_restricted`. That helper is true for quarantine, district quarantine, controlled access, or temporary closure. The in-scope action does not require `riches_found_phase_emergency`, although the separate baseline `decision_riches_found_seal_depths` does, and it does not check sealed-depth integrity or evacuation state.

The outcome starts `riches_found_begin_partial_seal` only when there is no existing `riches_found_mine_partial_seal` and `riches_found_mine_can_begin_temporary_closure` is true. This preserves the existing conflicting-partial-seal rule and prevents a second integrity loss. The decision has no explicit minimum-integrity rule. If the gold-only action is intended to be emergency-only or to require a particular integrity state, that entrance condition is currently absent. The accepted design supplies no new numeric integrity threshold, so one remains unresolved rather than inferred here.

Recommended parent review: decide whether the gold-only action should share the baseline emergency-phase gate, and whether integrity or evacuation must gate it. If either is required, put that condition in the matching target, availability, and tooltip contract without changing the existing one-time partial-seal guard.

### Medium: target entry does not directly require an active mine

`riches_found_state_is_active_selected_or_only_mine` checks registration and controller selection. It does not call `riches_found_mine_is_active`. The gold-specific route can therefore be selected from a registered mine that is closed or otherwise not operational when its other target flags still match. `riches_found_mine_can_begin_temporary_closure` blocks only the partial-seal subeffect. The gold decision still sets both sealed-depth flags and applies its pressure reductions if that helper rejects.

The shared late-payer guard requires the original controller, a registered mine, and a nonterminal mine. It does not require the mine to be active. The permanent-seal action may intentionally resolve on a collapsed mine, so the correct active-state rule needs parent design review. If inactive or terminal mines must not accept these projects, add the appropriate entry gate and preserve the late-payer refund path.

## Cost and requirement audit

| Decision | Native timed commitment | Manual spends | Output opportunity cost | Total distinct cost types |
| --- | --- | --- | --- | ---: |
| `decision_riches_found_gold_seal_depths` | 2 civilian factories for 60 days | 300 manpower and 150 support equipment | Lower workings remain unavailable to ordinary extraction | 4 |
| `decision_riches_found_demons_permanent_seal` | 2 civilian factories for 90 days | 600 manpower and 150 support equipment | Mine output ends permanently | 4 |

The timed factory commitment is the native `modifier = { civilian_factory_use = 2 }` paired with `days_remove`, not a native political-power `cost` field. The `riches_found_decision_duration.project` and `.long_project` constants resolve to 60 and 90 days. The civilian-factory affordability predicate is `num_of_available_civilian_factories > civ_standard_gate`, with the gate equal to 1, so it requires at least two available factories. Manpower uses `manpower_k` in thousands with inclusive comparisons at 0.3 and 0.6. Support-equipment affordability checks the same `support_equipment` inventory token debited by the decision and requires at least 150.

Each decision calls the same composite affordability helper from both `available.hidden_trigger` and `custom_cost_trigger`. The per-resource display getters use those same affordability predicates. The completion effect debits the manpower and support equipment once. The native factory modifier commits the two factories during the timer. There is no remaining political-power or truck requirement, debit, refund, or `ai_hint_pp_cost` in either in-scope block or its composite cost trigger.

Each inline row presents three values. They use `£civ_factory`, `£manpower_texticon`, and `£support_equipment_text_icon`, with separate available and blocked colours. The base, `_blocked`, and `_tooltip` localisation keys exist for both actions. The cost tooltips state the 60/90-day factory commitment and the output consequence. No fifth spendable cost appears in the decision tooltip, completion effect, removal effect, or cost trigger.

## Decision lifecycle and preserved behavior

Both decisions remain targeted entries in `riches_found_mine_management`, with `fire_only_once = no`, no native cooldown, and no `cancel_trigger`, `cancel_effect`, or `remove_trigger`. Their mine flags hide a successfully resolved action. The frozen-baseline comparison found the complete `ai_will_do` block and the `remove_effect` validity/success branch byte-for-byte equal inside each decision block. The 60-day and 90-day duration constants are unchanged.

At selection, the custom payment is charged in `complete_effect`. When the timer removes the decision, `riches_found_mine_still_valid_for_payer` checks that the target is still controlled by `ROOT`, registered, and nonterminal. If valid, the gold action sets its sealing flags, conditionally begins a partial seal, and reduces pressure. The demonic action sets its permanent-seal flag and runs the terminal mine cleanup. If invalid, each decision refunds the manpower and support-equipment debits. The spent factory opportunity time is not refunded, because it was committed during the timer rather than held as an escrowed inventory payment.

Gold output preservation remains wired through `riches_found_depths_sealed` and the existing mine-contribution refresh. It applies the sealed-depth output factor when the mine is not already using the partial-seal operating factor or bound-account terms. The partial-seal helper retains its existing integrity reduction and one-time guard. Demonic sealing remains permanent through the terminal mine flag, mine cleanup, development loss, and contribution refresh. The current cost change did not alter those effects.

## Evacuation mission quality relevant to the safety gap

`mission_riches_found_evacuate_workforce` is the route-specific timed objective used by the demonic evacuation preparation decision. The controlling country owns the state-subject mission in `riches_found_mine_management`. It requires the cleared mine subject, a ready and active evacuation route, a rail or port route, a passed preparation date, and a valid mission slot. The preparation decision runs for 30 days, then the mission has a 270-day native timeout. Success marks both district and workforce evacuation, preserves the evacuation-route receipt, and lowers supernatural pressure. If the route remains active at timeout, the mission gives partial success. Otherwise it applies failure. The mission subject and preparation flags prevent a duplicate evacuation for the same mine.

The alternative `decision_riches_found_evacuation` is available during the emergency phase for severe collapse or supernatural crisis and sets `riches_found_workforce_evacuated` after its 90-day timer, subject to the late-payer guard. Either evacuation route satisfies the current `demons_district_cleared` helper. A military purge also satisfies it, which is the unsafe substitute identified above.

## Cognitive load, localisation, and AI

Within the requested two-action scope, each action has three compact cost values and one consequence summary. No raw numeric value dump or new visible meter was introduced. Total simultaneous category actions and missions were not counted because that would expand this audit beyond the two named IDs.

The gold effect tooltip describes the sealed upper-workings outcome but does not state an integrity change. Its cost tooltip explains that the lower workings remain unavailable. The demonic effect and cost tooltips explicitly state that ordinary output is abandoned permanently. The missing route requirement is more important than wording and should be decided before adding requirement copy.

The AI weight blocks are exactly equal to the frozen source in the two named decision blocks. The demonic AI currently increases willingness during supernatural crisis and lacks the entombment safety modifier present on the baseline permanent-seal action. As requested, no additional `chaosx_ai_probability_auditor` or probability comparison was run because the parent already owns the Event 029 I/J decision scenarios and the weights were not edited here. AI willingness remains a score, not a click probability.

## Evidence, validation limits, and scope

- Frozen decision source: `docs/plans/029_riches_found_plans/evidence/2026_10_07_seal_cost_before/common__decisions__029_riches_found_decisions.txt`, SHA-256 `0660E6B60D884D2C50333165BE1D112564AD176A2444C1BB96FF5F9F6705163E`.
- Current decision source at handoff: SHA-256 `AE8C42A480A71CCD41AB2553DC324815DAADF6496A406F8B530123B5E2ADE7B9`.
- Current cost triggers: SHA-256 `C53B2A587EA192B7247E3A70F6D878681AAA94D77C44A6286F6FAC8E41B80C96`. Frozen trigger source: SHA-256 `5B93479FCC2E3367847CD5D97B4A0AE4D4275227A2D55F3F9BABA157D465A0D2`.
- Current decision localisation: SHA-256 `0B5E5495AB2D7878EA5FCEAA674DC2B7CFBDB3682DC454225D8B7A5BF97D6CAD`. Frozen localisation source: SHA-256 `D13A3128A2E034A8233448654D76582148E68978C0CCB4FA8DB95628A786B7BB`.
- Removing the two named decision blocks from the current and frozen full files does not yield byte-identical outside text. The current tree also contains `open_railhead` mission hunks outside the requested decision IDs. Those are out of scope and were left untouched, so this audit does not claim the 0660 snapshot is an exact full-file outside-block match.
- `hoi4.decision_inspect` produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a912b21b3b0f7330680df25ea34395195303c77b298ccf7b31f0d3bfe0594893/53755dcff464bb219205e6141022bcf869fdf20b4f2d42aa986588513419181d/decision-c440fc8a7b77f8d816653c15.json`. Its six byte-range reads were contiguous, totaled 47,606 bytes, parsed as JSON, and matched the artifact SHA-256. The one declared scenario, `gold_minimal_source_scenario`, returned `DECISION_ANALYZED_PARTIAL`; gate evaluation was unresolved because it lacked a `FROM` target binding and declared civilian-factory, manpower, and support-equipment inputs. The report also had incomplete workspace coverage. No scenario result is treated as proof of actual game eligibility or payment.
- Offline wiki evidence: `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, lines 284-336 for custom costs and lines 337-356 for timer, `complete_effect`, `remove_effect`, and timed modifiers.
- Installed documentation: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, lines 1-46. Dynamic-variable entries for `manpower_k`, `num_equipment`, and `num_of_available_civilian_factories` are in `documentation/dynamic_variables_documentation.md`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, lines 469-471, 557-559, and 592-595.
- Vanilla precedent: `game:common/decisions/AST.txt`, `AST_union_strike`, lines 2-42, source-index revision `bae6f98dce88e3c73ef5f0f4e2744c337cf3242843b951961b3c293f027ea8de`. It uses `days_remove`, a native decision modifier `civilian_factory_use`, and a `remove_effect`; it also demonstrates that a native PP `cost` and a temporary factory modifier are distinct.
- Event context: `docs/events/029_riches_found/overview.md` lines 102, 183, and 233 describes the emergency seal phase, entombment harm on the baseline permanent seal, and the Demons route's evacuation and sealed-depth integrity context.

No game was launched and no gameplay tests were run. No GUI surface was in scope. No probability scenario was duplicated. Parent review is still needed for the evacuation/entombment and integrity/phase gates.

## Files changed

Only `docs/plans/029_riches_found_plans/subagent_handoffs/seal_cost_audit_2026_10_07.md`.

Decision IDs audited: `decision_riches_found_gold_seal_depths` and `decision_riches_found_demons_permanent_seal`. No decision, mission, scripted-GUI, or localisation source was edited. No broader plan was created because the unresolved fixes are narrow entrance and safety requirements for existing actions.
