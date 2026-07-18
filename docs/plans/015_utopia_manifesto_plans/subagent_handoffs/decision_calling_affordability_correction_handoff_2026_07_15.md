# Event 015 Calling Mutex and Affordability Correction Handoff

Date: 2026-07-15  
Worker: `chaosx_decision_corrections`  
Mode: bounded patch; no commit created

## Outcome

The two decision findings are corrected in the live Event 015 source.

- Calling sustainment and second-trade training now claim the same `utopia_manifesto_calling_mission_active` mutex used by the four ordinary calling starts.
- Every success, cancellation, failure, timeout, and terminal teardown path for those missions releases the shared mutex together with its mission-specific flag.
- All payment-coupled strict-greater-than predicates found across the main decision surface and its penal-district target trigger now accept a stockpile or reserve exactly equal to the required threshold.
- No price, payment amount, mission duration, AI weight, localisation key, or nonpayment threshold was changed.

No simplification, fallback, or omission was used.

## Files changed

1. `common/decisions/015_utopia_manifesto_decisions.txt`
   - claims the shared calling mutex when starting sustainment or second-trade training;
   - releases the mutex on second-trade cancellation and timeout success;
   - converts 199 payment-coupled affordability predicates to equality-safe forms.
2. `common/scripted_effects/015_utopia_manifesto_decision_effects.txt`
   - releases the shared mutex from sustainment success and failure helpers.
3. `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
   - makes the penal-district target trigger's reserve start floor equality-safe.
4. `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/decision_calling_affordability_correction_handoff_2026_07_15.md`
   - records this correction and its audit evidence.

The existing teardown in `common/scripted_effects/015_utopia_manifesto_effects.txt` was audited but did not need an edit.

## Calling mission mutex correction

### Start paths

The following decision starts both check that `utopia_manifesto_calling_mission_active` is absent and set it before mission activation:

- `decision_utopia_prove_every_calling_chosen` -> `mission_utopia_sustain_every_calling_chosen`
- `decision_utopia_learn_second_trade` -> `mission_utopia_learn_second_trade`

Together with the existing four ordinary calling-method starts, the live source has six mutex claims before calling-mission activation. Because all six starts gate on the same country flag, their click order no longer changes whether overlap is possible.

### Exit paths

The shared mutex is released on all mission-owned exits:

- sustainment success: `utopia_manifesto_complete_calling_sustainment`;
- sustainment cancellation/failure: `utopia_manifesto_fail_calling_sustainment`;
- second-trade cancellation: `mission_utopia_learn_second_trade.cancel_effect`;
- second-trade timeout success: `mission_utopia_learn_second_trade.timeout_effect`;
- ordinary calling success/failure: the existing `utopia_manifesto_resolve_unpopular_calling` and `utopia_manifesto_fail_unpopular_calling` helpers.

Terminal teardown remains complete and correctly ordered:

- `utopia_manifesto_remove_all_active_missions` explicitly removes `mission_utopia_fill_unpopular_calling`, `mission_utopia_sustain_every_calling_chosen`, and `mission_utopia_learn_second_trade`;
- `utopia_manifesto_clear_decision_runtime` then clears `utopia_manifesto_calling_mission_active`, `utopia_manifesto_calling_sustainment_active`, and `utopia_manifesto_second_trade_active`;
- `utopia_manifesto_clear_all_runtime_state` calls that decision cleanup before the narrower calling-state cleanup.

This matters because official `remove_mission` behavior does not execute a mission's timeout or cancel effect; teardown therefore must and does clear the flags itself.

## Exact affordability correction

### Corrected predicate count

The correction changed **200 payment-coupled predicates**:

| Predicate family | Count | Equality-safe form |
| --- | ---: | --- |
| Equipment stockpiles | 169 | `NOT = { has_equipment = { type < cost } }` |
| Manpower, army experience, command power, and stability | 27 | `NOT = { resource < cost }` |
| Reserve-score variable thresholds | 4 | explicit `check_variable` with `compare = greater_than_or_equals` |
| **Total** | **200** | |

The 169 equipment predicates cover 69 support-equipment, 46 train, 22 motorized, 18 convoy, and 14 infantry-equipment checks. The 27 direct-resource predicates cover 19 manpower, 3 command-power, 2 army-experience, 2 `stability`, and 1 `has_stability` checks.

The previously reported **181** generic `constant:utopia_manifesto_decision_cost.*` defects are all included: 156 equipment and 25 direct-resource predicates. The full live review also found and corrected **19** payment-coupled gates outside that original count:

- 9 district equipment start thresholds;
- 4 duplicated Penal Works equipment gates (`available` and `custom_cost_trigger`);
- 2 duplicated Penal Works manpower gates;
- 3 reserve gates in the main decision file; and
- 1 reserve gate inside `utopia_manifesto_state_is_valid_active_penal_district`, which otherwise continued to block the exact Penal Works reserve floor through `target_trigger`.

### Payment alignment review

The main file contains 199 corrected gates across 85 decision blocks. Every corrected generic `decision_cost` predicate was matched to the same constant assigned to a `utopia_manifesto_cost_*` input in its own decision block before `utopia_manifesto_pay_prepared_decision_cost` executes.

The special thresholds were reviewed individually:

- Garden Market starts retain 50 support and 10 trains after reserving the existing 20 support and 5 train maintenance floors (`70` and `15` start thresholds).
- Industrial Housing retains 20 support and 25 motorized after its 100 support and 50 motorized payment (`120` and `75`).
- Rail Junction retains 20 support and 5 trains after its 50 support and 20 train payment (`70` and `25`).
- Refugee Municipality retains 20 support, 5 trains, and 25 motorized after its 100/10/50 equipment payment (`120`, `15`, and `75`), and an exact reserve start score of 30 remains above its 20 floor after the existing 5-point reserve nudge.
- Penal Works accepts the exact 3000 manpower, 500 infantry equipment, 100 support equipment, and 30 reserve start floor; its existing 10-point reserve subtraction leaves the documented 20-point post-cost floor.

No tuning constants or subtraction effects were altered.

### Preserved nonpayment comparisons

The strict `>` comparisons still present in the main decision file are intentional nonpayment thresholds: Penal Works AI resistance, positive diplomatic opinion, minimum guard divisions, auxiliary source-army manpower, and severe surrender pressure. Event 015 trigger/effect files likewise retain strict suitability, maintenance-obligation, candidate, AI-capacity, opinion, and route-state thresholds that do not authorize an immediate subtraction. These were deliberately not rewritten.

## Validation evidence

- Re-parsed the main file into decision blocks: 85 blocks contain 199 corrected affordability gates, and zero corrected generic gate lacks its same-block prepared payment constant.
- Re-scanned the live main decision file after editing: no strict equipment, manpower, experience, command-power, stability, or reserve payment predicate remains.
- Re-scanned the penal target trigger after editing: all three decision-side reserve checks plus its target-side reserve check use `greater_than_or_equals`.
- Re-scanned all calling flag producers, consumers, mission activations, mission exits, mission removal, and teardown: six starts claim the mutex; ordinary success/failure, sustainment success/failure, second-trade cancellation/timeout, and terminal cleanup release it.
- Confirmed the existing evolution-consumption cost triggers use the same equality-safe inverted-less-than structure adopted here.
- Structural checks on the three edited gameplay files leave brace depth balanced and do not introduce unsupported `<=` or `>=` operators.

## Risks and remaining scope

- This bounded correction does not address other Event 015 audit findings such as localisation coverage, prefire evolution producers, or foreign/news event reachability.
- The repository was already under concurrent modification. Counts and lifecycle conclusions above come from a final re-scan of the live files, not from assumptions about the earlier audit snapshot.
- No gameplay fallback was introduced. No runtime diagnostic code was needed.

## References consulted

- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- offline wiki snapshots for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Equipment
- vanilla `common/decisions/_documentation.md`
- vanilla `documentation/triggers_documentation.md`
- vanilla `documentation/effects_documentation.md`
- vanilla Bulgarian internal-affairs mission mutex precedents
- Event 015 evolution-consumption affordability triggers

