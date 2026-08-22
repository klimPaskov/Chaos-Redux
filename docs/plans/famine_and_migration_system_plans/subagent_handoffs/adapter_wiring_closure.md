# Famine and migration adapter wiring closure

This handoff records the owner-local adapter closure for the famine and migration integration matrix. The shared wrappers remain in `common/scripted_effects/chaosx_famine_migration_effects.txt`; owner systems retain direct Deaths, contamination, blast, plague, disaster, camp, and political ownership.

## Matrix disposition

| Matrix row | Status | Evidence or exact blocker |
| --- | --- | --- |
| Chaos Meter Deaths | API-only with exact blocker | Shared famine exposes exact-death aliases, but no separate owner callback may debit the same owner Deaths transaction. Direct deaths remain owner-owned. |
| Air Cleanliness | Wired | `fallout_consolidated_effects.txt:air_winter_apply_state_population_loss` calls `famine_migration_adapt_air_winter_state` after `state_civilian_population_loss_applied`; state and amount are exact. |
| Condemnation | Wired | Existing famine decision paths call the six condemnation wrappers in `famine_migration_adapter_effects.txt`; sanction aggregation remains Condemnation-owned. |
| Camps and genocide | Wired | `camp_rework_record_latest_state_deaths` calls `famine_migration_adapt_camp_state` after exact Deaths and responsible-country credit. |
| Occupation laws | API-only with exact blocker | `on_state_control_changed` proves only a controller transition; no owner-local hook in the current source proves occupation law, repression action, actor, and amount together. |
| Chemical warfare | Wired | Accepted CBRN nerve-suppression state callback exposes exact state, actor, route, and `cbrn_occupation_last_civilian_deaths`; adapter registers chemical aftermath only. |
| Biological/outbreak | Wired | Black Plague mortality callback passes the exact applied loss to outbreak pressure. Zombie/nonhuman paths are excluded by normal-civilian state validation. |
| Nuclear and thermonuclear | Wired | Vanilla-documented `on_nuke_drop` uses ROOT as launching country and FROM as nuked state; adapter registers food pressure with centralized strike fraction. Evacuation ring remains unclaimed without survivor-count proof. |
| Strategic bombing | API-only with exact blocker | Air Winter reads recent bombing but no current owner callback supplies a single resolved state impact plus responsible bomber actor; no recurring pressure call is added. |
| Natural disasters/Event 13 | Wired | Event 013 `natural_disaster_apply_population_loss` passes exact `natural_disaster_last_deaths` after the resolved state impact. Non-lethal crop/evacuation aftermath has no exact population amount and is not guessed. |
| War/fronts | API-only with exact blocker | Existing war hooks are country-scoped reassessment markers; no state-level front/siege/encirclement amount and actor callback is present. |
| Peace/White Peace | API-only with exact blocker | Existing peace hooks are country-scoped reassessment markers; no exact safe corridor, destination, or return cohort is supplied by the hook. |
| Event 5 Soviet Collapse | API-only with exact blocker | Current event/effect paths expose political stages, wars, and country decisions but no single stable resolved state + exact grain/deportation amount + actor adapter callback. |
| Event 6 Independence Wave | API-only with exact blocker | Release paths prove country transition, not a bounded refugee amount, destination capacity, or return transaction. |
| Event 14 Cannibalism | API-only with exact blocker | Event-owned Hunger Lines/state control are present, but the source does not expose an exact ordinary-civilian hunger amount and actor context for a shared request. Cannibalism deaths remain owner-owned. |
| Event 15 Utopia Manifesto | API-only with exact blocker | Route/territory choices do not provide an exact state-level stores/blockade/refugee amount and responsible actor in one callback. |
| Event 20 Black Plague | Wired | `black_plague_apply_current_state_mortality_once` calls the outbreak adapter after exact owner population loss. |
| Event 21 Random Civil War | API-only with exact blocker | Civil-war creation and rebel participants are country-level; no exact affected state pressure amount is exposed at the creation callback. |
| Event 28 Asteroid | API-only with exact blocker | Impact choices touch state damage, but no stable survivor count, exact food-loss amount, and actor/context contract is available before invalidation. |
| Event 33 Acid Rain | API-only with exact blocker | Rain modifiers identify affected states, but the event has no stable responsible actor or exact food/water loss amount; adding a population fraction would fabricate impact. |
| Event 50 Great Embargo | API-only with exact blocker | Diplomacy source proves embargo state but not import dependence, route restriction, or relief amount per state in the current owner callback. |
| Event 95 Occupation Revolt | API-only with exact blocker | Revolt options change control and political state; no exact famine/forced-labor/relief amount is supplied beyond the existing control-change reassessment. |
| Event 118 Locust | Unavailable-source | No Event 118 source exists in the repository; no locust callback or resolved intensity state can be wired. |
| Event 120 Volcano | Unavailable-source | No Event 120 source exists. Volcano effects are currently owned by Event 013, and only its exact positive-death callback is wired. |
| Event 131 Mutiny | Unavailable-source | No Event 131 source exists; no army/civilian ration context callback is available. |
| Event 149 Immigrations | Unavailable-source | No Event 149 source exists. The flat-drain concept is retired/absorbed; no replacement event or pacing hook is added. |
| Disease cluster | API-only with exact blocker | Cluster ownership provides pacing/member grouping, but no stable member callback with exact resolved state, actor, and amount beyond Black Plague’s wired owner source. |
| Natural Disaster cluster | API-only with exact blocker | The cluster has no additional state callback; Event 013 member impacts are wired individually without adding cluster pacing. |
| Liberations cluster | API-only with exact blocker | Liberation members expose political release, not a proven safe-return destination, capacity, and cohort amount in one owner callback. |
| Wars cluster | API-only with exact blocker | Cluster conflict records are not state-level impact callbacks; war hooks remain reassessment-only. |
| Peace cluster | API-only with exact blocker | Cluster settlement records do not supply an exact return corridor or cohort amount; peace hooks remain reassessment-only. |
| Special Chaos classifiers | Wired by fail-closed shared API | `famine_migration_state_is_valid` and country classifiers reject invalid/nonhuman owners/controllers; no special actor receives civilian pressure. |

## Helper, constant, and lifecycle plan

The new owner bridges are `famine_migration_adapt_air_winter_state`, `famine_migration_adapt_camp_state`, `famine_migration_adapt_chemical_state`, `famine_migration_adapt_black_plague_state`, and `famine_migration_adapt_natural_disaster_state`. They are state-scoped, consume owner-applied exact amounts, and return no persistent value. The nuclear on-action uses `famine_migration_adapter_pressure.nuclear_strike_population_fraction` because the documented callback provides no applied civilian-loss field.

No event target or persistent adapter flag is introduced. Existing owner targets/variables remain in their owner files; shared request temporaries are cleared by the shared generic wrapper. No duplicated arithmetic or duplicate death call was added.

## MCP and validation evidence

Read-only Event Chain Viewer state-flow inspections were run for the scoped implemented roots (`chaosx.nr5.1`, `.nr6.1`, `.nr9.1`, `.nr13.1`, `.nr14.1`, `.nr15.1`, `.nr20.1`, `.nr21.1`, `.nr28.1`, `.nr33.1`, `.nr50.1`, and `.nr95.1`) in workspace `mod_chaos_redux_ea3b2d67c2c0`. The focused artifact for Event 033 is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13dd5082ed9c7d2fefae142e4bc569bf9516be61d0653c7cc4e9ef35c5b0434d/d4b831fd715ab0363e4ff49f298510e915dae579b26de4833fff795991d1080f/event-state_flow-b98e7381a4c7.json`; the other focused reports were partial with the same workspace-wide inline-source truncation diagnostic and no blocking diagnostics.

Targeted source validation checked each new helper name against its owner call site, verified the pressure wrappers are called only after positive exact amounts, and reviewed the diff for accidental second population-loss calls. Live HOI4 execution was not run, as required by repository policy. Weighted probability inspection was not applicable because this patch changes no AI weight, MTTH, random-list weight, or probability surface.

## Known limitations

The remaining API-only rows are source-proof blockers, not synthetic fallbacks. In particular, strategic bombing, occupation-law, Event 033 acid-rain intensity, war/peace state outcomes, and cluster member callback contracts still need owner-local data before safe calls can be added. Event 118/120/131/149 roots remain unavailable and were not fabricated.
