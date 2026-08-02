# Air Winter Phase 5 Dead-City Salvage Event Proof

## Proof boundary

This document records the static proof for `chaosx.fallout.47` and `chaosx.fallout.48`. Hearts of Iron IV was not launched. The user explicitly excluded a game run, so no runtime observation is claimed.

The route is an Air Winter ruined major-city salvage chain. It does not claim that the later Fallout state grade `dead_city` already exists. Fallout grading is unavailable while the Air Winter event scheduler is active. The candidate therefore uses live urban provenance and physical damage evidence that exist before the Fallout rewrite.

This tranche does not change the Air Winter survival formula, monthly phase coefficients, Fallout grading formula, treaty behavior, world iteration, manual scenario, or Fallout living-world release-floor count.

## Implemented files

Gameplay and presentation:

- `common/script_constants/air_cleanliness_winter_event_constants.txt`
- `common/on_actions/air_cleanliness_winter_on_actions.txt`
- `common/scripted_triggers/air_cleanliness_winter_triggers.txt`
- `common/scripted_effects/air_cleanliness_winter_event_effects.txt`
- `events/fallout_world_end_events.txt`
- `localisation/english/fallout_world_end_events_l_english.yml`
- `interface/air_cleanliness_winter.gfx`

Dedicated asset package:

- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_dead_city_salvage_source.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_dead_city_salvage.png`
- `gfx/event_pictures/fallout/report_event_air_winter_dead_city_salvage.dds`
- `docs/assets/air_cleanliness_fallout/contact_sheets/air_winter_report_events_final_contact_sheet.png`
- `docs/assets/air_cleanliness_fallout/manifest.md`
- `docs/assets/air_cleanliness_fallout/air_winter_report_event_gfx_handoff.md`

The accepted design contract is `AIR_WINTER_PHASE_5_DEAD_CITY_SALVAGE_EVENT_ADDENDUM.md`.

## Identity proof

`air_winter_event_is_dead_city_salvage_candidate` requires all of the following:

1. a valid active Air Winter state in Phase 5
2. no active Fallout transition or completed Fallout world
3. current ownership and control by the same country
4. a recorded original category of `large_city`, `metropolis`, or `megalopolis`
5. the persistent `air_winter_last_building_loss_date` receipt
6. current damage in infrastructure, civilian industry, military industry, airbase, dockyard, supply node, or railway
7. no exhausted-site memory
8. no existing delayed Air Winter branch

The original category prevents a later degraded state category from erasing major-city identity. The loss receipt proves that Air Winter previously applied physical building loss. The current damaged-building check prevents a historical receipt by itself from making a fully repaired state eligible. The exhausted-site flag prevents repeat extraction from the same site.

The installed `documentation/dynamic_variables_documentation.md` defines `damaged_building_level@arms_factory` as the damaged level of a named building type and `non_damaged_building_level@arms_factory` as its non-damaged level. The implementation applies that documented target form to the seven named building types.

The installed `documentation/triggers_documentation.md` records `is_controlled_by` for state scope with `ROOT` and `OWNER` among its supported targets. The candidate uses `OWNER`. The delayed result uses `ROOT`, which is the country resolving the inherited event chain. The control-loss clause uses `OWNER`. The same reconciliation effect separately validates whether ownership still matches the stored pending country.

## Route ordering proof

The Phase 5 state-local selector order is:

1. ruined major-city salvage, typed id 47
2. generic Phase 5 city, typed id 40
3. low-shelter abandonment, typed id 41
4. archive continuity, typed id 42

The dedicated route adds `constant:air_winter_event_runtime.dead_city_salvage_same_phase_bonus`, which is 131, to the normal phase and pressure score. The current pressure range ends at 130. The route therefore wins against another ordinary Phase 5 candidate owned by the same country without overtaking a Phase 6 candidate. The normal lexicographic candidate comparison still resolves family priority, origin cycle, score, and lower state id deterministically.

The route uses the shared Phase 5 seen flag. It broadens deterministic cross-playthrough identity without creating a second Phase 5 popup for the same country.

## Opening transaction

`chaosx.fallout.47` presents three competing authorities.

| Branch | Payable gate | Opening pressure | Base AI weight |
| --- | --- | --- | ---: |
| survey engineers | 500 Manpower, 30 Support Equipment, 10 Motorized Equipment | Adaptation +4, Reclamation +2, Exposure +1, Building Damage Pressure +8 | 60 |
| military quartermasters | 1,000 Manpower, 120 Infantry Equipment, 20 Motorized Equipment, 1,000 Fuel | Adaptation +2, Exposure +3, Building Damage Pressure +15 | 10 |
| licensed district crews | no payable resource gate | Reclamation +4, Exposure +2, Building Damage Pressure +8, Stability loss | 30 |

Survey and military affordability are checked when the option is displayed and again inside the click transaction. Payment uses the existing exact payment helpers. Each helper negates the temporary quote before applying the documented manpower, fuel, or stockpile effect. The licensed branch always leaves one executable option on a valid popup.

Every valid choice clears older dead-city policy and branch memory, applies its cost and ledger effects once, writes exactly one branch, records state and country policy memory, refreshes the state, refreshes the 46-day country cooldown, and schedules event 48 after exactly 30 days.

The AI modifiers are independent multiplicative factors and match the accepted addendum:

- survey starts at 60, multiplies by 2 for a plausible state or by 0.5 for its exact inverse, then multiplies by 2 only when at peace and democratic or neutral
- military starts at 10, multiplies by 2 for a plausible state or by 0.5 for its exact inverse, then independently multiplies by 2 for fascism, war, and war support of at least 65 percent
- licensed salvage starts at 30, multiplies by 2 for a plausible state or by 0.5 for its exact inverse, then independently multiplies by 2 for democratic or communist government, by 2 for stability no higher than 45 percent, and by 0.5 during war

## Deterministic result partition

`chaosx.fallout.48` contains ten mutually exclusive result options.

| Stored branch | Ordinary partitions | Altered replacement |
| --- | --- | --- |
| survey | success, partial, disaster | replaces survey disaster when the mixed-cause gate passes |
| military | success, partial, disaster | replaces military disaster when the mixed-cause gate passes |
| licensed | success, partial, disaster | replaces licensed disaster when the mixed-cause gate passes |

For each branch, partial explicitly excludes success. Disaster explicitly excludes success and partial. Every ordinary disaster description and option excludes the altered gate. The altered option requires the selected branch to be in its disaster partition. This produces one available result for every exact valid branch and no overlapping ordinary result.

Success and partial outcomes grant fixed equipment types through `add_equipment_to_stockpile`. Every caller initializes infantry, support, motorized, and train grant variables, including explicit zeroes. The helper clears all four temporary values after the grant.

The installed `documentation/effects_documentation.md` states that `add_equipment_to_stockpile` supports a variable amount and that a negative amount removes equipment. The salvage helper uses positive values only. Fixed types are `infantry_equipment_1`, `support_equipment_1`, `motorized_equipment_1`, and `train_equipment_1`.

All casualty outcomes call `air_winter_event_apply_deaths`. That helper calculates a bounded percentage of remaining state population, applies the state loss once, and registers the observed loss through the existing Deaths system with Air Winter reason 17.

Disaster damage checks `non_damaged_building_level@<type>` before calling `damage_building`. Survey damage targets infrastructure. Military damage targets an operational military factory, otherwise infrastructure. Licensed damage targets an operational civilian factory, otherwise a military factory, otherwise infrastructure. No damage is issued when every target is exhausted.

The installed `documentation/effects_documentation.md` defines `damage_building` for state scope and shows fractional damage with a repair speed modifier. This tranche applies 0.50 damage without a repair penalty, so it is ordinary repairable damage rather than permanent removal.

## Altered-result boundary

The altered return is fictional high-Chaos content. It does not represent ordinary radiation science and it does not request Fallout.

Its gate requires all of the following:

1. the selected salvage branch is already in its disaster partition
2. `global.chaos_meter_value` is in the final Chaos tier
3. `nuclear_fallout_intensity` is positive
4. the state has the active `nuclear_fallout_state` modifier
5. the state also has active chemical contamination or one of the active biological contamination flags

The nuclear intensity variable alone is insufficient. The active nuclear modifier is also required. Chemical or biological contamination alone is insufficient. Final-tier Chaos alone is insufficient. The result remains a narrow mixed-cause branch and does not change the 100 percent Air Contamination Fallout request rule.

## Event-target and authority proof

The Air Winter dispatcher saves `air_winter_event_country` and `air_winter_event_state` with `save_event_target_as`. The offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` states that regular event targets carry into delayed events fired from the same effect chain. Its documented example saves a state target and fires a country event ten days later.

The opening validates the generic owner-bound target contract and the exact ruined-city candidate. Each click repeats both checks. The state refresh binds `air_winter_pending_event_owner` to the country that made the choice.

The result requires the generic target contract, exact branch, and `is_controlled_by = ROOT`. If ownership changes, the generic pending-owner validation fails. If ownership remains but an enemy controls the state, the dead-city invalid-branch trigger sees that the state is not controlled by `OWNER`.

The offline on-action documentation defines `on_state_control_changed` with ROOT as the new controller, FROM as the old controller, and FROM.FROM as the state. `common/on_actions/air_cleanliness_winter_on_actions.txt` checks that exact state for any dead-city branch and calls the shared reconciliation effect immediately. This closes the transient loss and recapture window before the delayed result can be discarded. Monthly reconciliation remains the backstop for ownership changes, malformed branch rows, and other invalid pending ledgers. Reconciliation clears all three dead-city branches, the generic pending flag, and the stored owner. Fallout snapshot capture freezes the Air Winter row before the same state pass cancels pending branches.

Every completed result marks `air_winter_memory_dead_city_salvage_exhausted`, clears all three branches, refreshes the state, and writes matching state and country result memory. Ordinary Air Winter reset clears the exhausted receipt. Ownership changes during an interrupted chain do not clear it because no completed extraction occurred.

## Localisation proof

The two events use 39 dedicated localisation keys. Every reference from events 47 and 48 resolves to one key. No key uses `:0`. The localisation file retains its UTF-8 byte order mark.

The opening names municipal engineers, military quartermasters, fire crews, rail crews, utility crews, and the current government authority. Results identify concrete stores, damaged works, casualty records, licensing disputes, and official seals. No working label, generic apocalypse wording, zombie reference, em dash, or semicolon appears in the new text.

## Dedicated asset proof

The source image is a fictional early-1940s documentary scene generated through the approved built-in image workflow. It shows lamp-lit salvage crews, braces, hand tools, a guarded truck, collapsed facades, ice, and ash. The preserved prompt is in the central asset manifest.

Static asset checks recorded:

| File | Dimensions | Mode or payload | SHA-256 |
| --- | ---: | --- | --- |
| source PNG | 1536x1024 | RGB | `64ede9c5dd46c3dd454c89f268a28204250aa6fe32632f0bfacc60f8b227c4ac` |
| processed PNG | 210x176 | RGBA | `39f43d86b62b9574092fd1a9ab75cae33468368f1926c7fe037bccdd4f7163e6` |
| final DDS | 210x176 | uncompressed 32-bit BGRA, 840-byte pitch, one image level | `591d488efb0af4a0ef8f6cddb3a039181ec874b2ec2aef8157c913d11216d536` |
| nine-asset contact sheet | 1840x1302 | RGB | `e1003d74a9b2732760ef9264dfe104ace258b7ebe412fad5e2ef5f80258947a4` |

The final DDS decode is pixel-identical to the processed PNG. Alpha ranges from 0 through 255, with 2,932 fully transparent pixels and 6,484 partially transparent pixels. The source, final image, and nine-image decoded contact sheet were visually reviewed.

`GFX_report_event_air_winter_dead_city_salvage` is registered once in `interface/air_cleanliness_winter.gfx` and consumed by both event blocks. Its source, processed, runtime, sprite, and manifest paths are Fallout-owned. No zombie file, asset, sprite, audio, filename, directory, or visual motif is used.

## Static audit results

The Air Winter pilot snapshot at the end of this dead-city tranche contained:

- 50 unique event blocks before the separate Fallout transition event range
- 159 options
- 158 effect-bearing options
- 54 delayed-result schedules
- one effect-free stale-order acknowledgement

Event ids 47 and 48 each occur once. Event id 49 was free at this snapshot and is now allocated to the later Desert City result recorded in `AIR_WINTER_PHASE_2_DESERT_CITY_EVENT_PROOF.md`. The current pilot totals are 52 blocks, 191 options, 190 effect-bearing options, and 67 delayed-result schedules. All 39 dead-city localisation references resolve. Script braces balance in the event, trigger, effect, constants, and sprite files. The dedicated source and runtime assets have distinct hashes from the other Air Winter report assets.

A narrow refreshed `hoi4.event_inspect` lint request for `chaosx.fallout.47` reached the installed read-only service. It returned `ARTIFACT_STORAGE_LIMIT` before scanning or producing a diagnostic. No source conclusion relies on that failed optional artifact.

Two independent read-only audits reviewed the engine transaction and the event, localisation, and asset contract. Their findings were reconciled before this proof was finalized.

## Unobserved engine boundary

The following remain unobserved because Hearts of Iron IV was not launched:

- live selection from dynamic damaged-building values
- regular event-target retention through the 30-day delay
- owner and controller changes while the result is pending
- the exact control-change on-action firing order against a due delayed event
- exact stockpile readback after fixed-type grants
- repair behavior after 0.50 building damage
- Deaths and population readback for every casualty percentage
- human popup availability and localisation rendering
- AI branch frequency
- save and resume behavior
- multiplayer scheduling and authority behavior

These are runtime observation limits, not passing claims. No fallback or weaker substitute was introduced inside this tranche.
