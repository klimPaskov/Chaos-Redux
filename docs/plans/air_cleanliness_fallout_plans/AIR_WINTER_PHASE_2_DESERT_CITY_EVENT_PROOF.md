# Air Winter Phase 2 Desert-City Water Convoy Event Proof

## Proof boundary

This document records the static proof for the exact Desert City route in `chaosx.fallout.13` and its delayed result in `chaosx.fallout.49`. Hearts of Iron IV was not launched. The user explicitly excluded a game run, so no runtime observation is claimed.

The chain belongs to the Air Winter pilot. It does not count toward the 660-block Fallout living-world release floor. This tranche does not change the Air Winter survival formula, monthly mortality, Fallout request thresholds, blackout transition, treaty projects, active combat pressure, strategic bombing, the manual scenario, or any living-world scheduler activation gate.

## Implemented files

Gameplay and presentation:

- `common/script_constants/air_cleanliness_winter_event_constants.txt`
- `common/dynamic_modifiers/air_cleanliness_winter_dynamic_modifiers.txt`
- `common/scripted_triggers/air_cleanliness_winter_triggers.txt`
- `common/scripted_effects/air_cleanliness_winter_event_effects.txt`
- `common/scripted_localisation/air_cleanliness_winter_event_scripted_localisation.txt`
- `events/fallout_world_end_events.txt`
- `localisation/english/fallout_world_end_events_l_english.yml`
- `localisation/english/air_cleanliness_winter_l_english.yml`
- `interface/air_cleanliness_winter.gfx`

Dedicated asset package:

- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_desert_water_convoy_source.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_desert_water_convoy.png`
- `gfx/event_pictures/fallout/report_event_air_winter_desert_water_convoy.dds`
- `docs/assets/air_cleanliness_fallout/contact_sheets/air_winter_report_events_final_contact_sheet.png`
- `docs/assets/air_cleanliness_fallout/manifest.md`
- `docs/assets/air_cleanliness_fallout/air_winter_report_event_gfx_handoff.md`

The accepted design contract is `AIR_WINTER_PHASE_2_DESERT_CITY_EVENT_ADDENDUM.md`.

## Exact route and subtype proof

`air_winter_event_is_desert_city_route` requires both the reviewed arid presentation class and the existing Air Winter city response identity. The Phase 2 state-local route order is:

1. mountain capital
2. engine island state
3. exact arid urban state, event 13 with subtype `desert_city`
4. generic city
5. maritime, oceanic, or tropical coast
6. non-city arid or Mediterranean state, event 13 with subtype `none`
7. highland or polar state
8. boreal or equatorial food state

The exact arid urban row therefore cannot be consumed by the generic city row. Mountain capitals and engine islands retain their higher route precedence.

Event 13 already owned the non-city arid and Mediterranean fallback. The numeric event id alone could not distinguish that fallback from the exact urban route. The typed `air_winter_event_route_subtype` table closes that ambiguity with `none` and `desert_city` values.

The subtype is initialized, copied, validated, or cleared through all four storage levels:

1. temporary state route selection
2. durable first-frost origin row
3. country candidate row
4. owner-bound opening receipt on the selected state

The country candidate validator accepts `desert_city` only when the candidate event id is 13. Every other event may carry only `none`. The first-frost validator enforces the same pairing. Ordinary candidate coalescing compares both the event id and subtype, so a generic event 13 observation cannot consume an exact Desert City marker and the exact marker cannot consume a generic row.

The exact route adds 131 to its Phase 2 candidate score. The current pressure interval ends at 130 and the phase weight is 1000. It therefore wins against another ordinary Phase 2 candidate owned by the same country without overtaking a Phase 3 candidate. Ordinary selection and first-frost capture apply the same bonus.

The dispatcher clears any older event 13 opening receipt before writing the current one. It writes the receipt only for subtype `desert_city` and stores the dispatching country as the original owner. Generic subtype `none` keeps no exact receipt.

## Shared event 13 separation

Event 13 has two fail-closed interfaces.

- A valid exact receipt displays the Desert City title, government-aware city description, dedicated picture, and the three delayed choices.
- A completely absent exact receipt displays the arid or Mediterranean fallback text, shared Phase 2 picture, and the two existing immediate choices.

A partial receipt is neither valid nor absent. It cannot open the exact or generic interface. Existing state reconciliation clears a partial receipt or a receipt whose stored owner no longer owns the state.

The generic options remain executable and retain their original immediate effects. Only a valid exact receipt can call the Desert City opening transaction or create an event 49 branch.

## Opening transaction

The exact opening provides three distinct authorities.

| Branch | Display and click gate | Exact payment | Opening state change | Base AI weight |
| --- | --- | --- | --- | ---: |
| municipal water board | valid exact receipt and no pending branch | 1 percent Stability | Water +8, Shelter +2, Adaptation +2, Building Damage Pressure +15, local factories reduced by 10 percent for 31 days | 60 |
| railway tanker service | valid exact receipt, no pending branch, operational railway | 500 Manpower, 3 Trains, 1,000 Fuel | Water +5, Adaptation +2, Exposure +1, Building Damage Pressure +8 | 30 |
| motor water columns | valid exact receipt, no pending branch, operational infrastructure | 200 Manpower, 20 Motorized Equipment, 1,000 Fuel, 7 Command Power | Water +5, Adaptation +4, Exposure +2, Building Damage Pressure -8 | 10 |

The municipal branch has no affordability gate, so every valid exact popup retains one executable choice. Railway and motor affordability are checked when their option is displayed and again inside the click transaction. Payment uses the existing Air Winter payment helpers, which negate the positive temporary quote immediately before applying the country resource effect.

Every valid click clears older Desert City policy, outcome, receipt, branch, waterworks, and result-modifier state. It then pays once, applies the opening ledger change, writes one exclusive state branch, writes matching state and country policy memory, refreshes the state to bind the original owner, refreshes the 46-day country cooldown, and schedules event 49 after exactly 30 days.

An invalid click performs no payment and no ledger mutation. The stale-choice helper clears only a receipt or pending branch owned by the same original event chain, then opens the established recovery notice when Fallout is not active.

## Pending-owner and result authority proof

The opening refresh writes both `air_winter_pending_delayed_result` and `air_winter_pending_event_owner`. Event 49 independently requires:

1. the saved country and state event targets
2. equality between the saved country and the country resolving the event
3. current ownership of the state by that country
4. the pending-result flag
5. the pending-owner variable
6. equality between the pending owner and saved event country
7. live ownership by the pending owner
8. exactly one Desert City branch

The final read-only code audit found that the first draft relied on the generic target helper for item 4 through item 7. That helper intentionally accepts an initial event when no pending row exists. The final Desert City result trigger now proves the full pending-owner row inside its own state block. A surviving branch without its owner receipt cannot resolve event 49.

Regular event targets are used instead of global targets. The offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` states that regular event targets carry into events fired within the same effect chain, including delayed child events. The installed `effects_documentation.md` defines `save_event_target_as`. The implementation follows that documented chain lifetime and avoids shared global target collisions between simultaneous countries.

## Deterministic result partition

Event 49 contains nine result options. Every branch has a success, partial, and failure partition.

| Branch | Success | Partial | Failure |
| --- | --- | --- | --- |
| municipal | Water at least 30, Adaptation at least 25, Building Damage Pressure at most 65 | success is false and any two success conditions pass | success and partial are both false |
| railway | operational railway, Water at least 30, Adaptation at least 25, Exposure at most 60 | success is false, railway remains operational, and any two ledger conditions pass | success and partial are both false |
| motor | operational infrastructure, Water at least 30, Reclamation at least 25, Exposure at most 60 | success is false, infrastructure remains operational, and any two ledger conditions pass | success and partial are both false |

The exclusive branch triggers reject any pair of branch flags. Partial explicitly excludes success. Failure explicitly excludes success and partial. This makes one and only one result available for every valid branch, including railway or infrastructure loss during the 30-day delay.

The nine outcomes have distinct physical consequences and effects:

- success restores water or transport capacity, lowers exposure, and applies 10 percent local supply relief for 60 days
- partial preserves a reduced route while adding pressure and a small Deaths request
- failure loses water, adds exposure and other route-specific pressure, applies a larger Deaths request, damages at most one operational repairable target, and reduces local supply by 10 percent for 60 days

Municipal failure prefers operational infrastructure and then a supply node. Railway failure prefers an operational railway and then infrastructure. Motor failure prefers operational infrastructure and then a supply node. Every ladder checks `non_damaged_building_level@<type>` before `damage_building`. No building is deleted and no permanent level removal is used.

The installed `dynamic_variables_documentation.md` defines the named non-damaged building variable. The installed `effects_documentation.md` defines state-scoped `damage_building` and accepts fractional repairable damage. This tranche applies 0.50 damage without a repair penalty.

Every casualty result calls `air_winter_event_apply_deaths`. The helper calculates a bounded percentage of the remaining state population, applies the loss once, and registers the observed loss through the existing Deaths system with the Air Winter reason. Manpower spent on crews is a country resource payment and is not logged as a civilian death.

## AI proof

Each exact opening branch has a pre-choice plausibility trigger derived by reversing its own opening ledger changes against the delayed success gate.

| Branch | Pre-choice projection |
| --- | --- |
| municipal | Water at least 22, Adaptation at least 23, Building Damage Pressure at most 50 |
| railway | operational railway, Water at least 25, Adaptation at least 23, Exposure at most 59 |
| motor | operational infrastructure, Water at least 25, Reclamation at least 25, Exposure at most 58 |

Every plausible predicate has a factor 2 modifier and a literal `NOT` inverse with factor 0.5. Government, war, Stability, and War Support preferences remain separate multiplicative factors. Unavailable paid options are absent from the AI choice set because they use the same display gate as a human player.

The result event does not need random AI weights. Its trigger exposes exactly one option for the stored branch and live outcome.

## Memory and cleanup proof

State and country memory records one of three policies, one of three outcomes, and whether the result requested casualties. State cleanup owns the opening receipt, all three branches, all policy and outcome flags, the temporary waterworks modifier, and both supply-result modifiers. Country cleanup owns the corresponding policy, outcome, and casualty flags.

The shared pending trigger includes all three Desert City branches. Pairwise invalid branches cancel through reconciliation. A sole exact branch without the generic pending flag also cancels during the existing monthly reconciliation pass. Ownership loss invalidates the pending-owner contract. Fallout snapshot capture preserves the established order by freezing the Air Winter state row before the same pass cancels pending chains and removes the waterworks modifier.

Every completed result clears the opening receipt, removes the municipal waterworks modifier, clears all three branches, clears the generic pending flag and owner through state refresh reconciliation, and leaves only its intended timed supply result and durable memory. Full Air Winter state reset removes the timed supply result as well.

## Dynamic event-picture proof

Event 13 uses `picture = [GetAirWinterEvent13Picture]`. `GetAirWinterEvent13Picture` returns the dedicated Desert City sprite only when the exact owner-bound receipt is valid. Its default returns `GFX_report_event_air_winter_phase_2`. Event 49 uses the dedicated sprite directly.

This syntax has a current vanilla precedent. Installed `events/Britain.txt` uses `picture = [GetHitlerCroatianHandshakeEventPicture]` for event `britain.14`. Installed `common/scripted_localisation/00_scripted_localisation.txt` defines that token with conditional `localization_key = GFX_*` rows and a default picture. The offline Localisation page explicitly requires the American spelling `localization_key` for a scripted-localisation option. The Air Winter implementation mirrors that spelling and structure for both the picture selector and its government-aware nouns.

The dedicated sprite is registered once as `GFX_report_event_air_winter_desert_water_convoy` in `interface/air_cleanliness_winter.gfx`. The source, processed, DDS, sprite, event, manifest, and handoff paths all use Fallout-owned Air Winter directories. No zombie id, file, asset, audio, sprite, or path is used.

## Dedicated asset proof

The source is a fictional period-documentary scene generated through the approved built-in image workflow. It shows a frost-split main, stone cistern, railway water tanker, period truck, engineers, and civilian water carriers in a culturally neutral arid city. Dry ground, stone, cold dust, and localized frost remain visible. The scene does not apply universal snow and contains no text, flags, logos, modern containers, zombies, or reused Fallout transition art.

| File | Dimensions | Mode or payload | SHA-256 |
| --- | ---: | --- | --- |
| source PNG | 1369x1149 | RGB | `e86a30ae3955a919e91a3aabc7c3615e7182daa4f78b04bea6f78b0d557f7fad` |
| processed PNG | 210x176 | RGBA | `cedeca688fa3053a564aa4311f0bd1c78443857e4cbcda29702536b0770782b7` |
| final DDS | 210x176 | uncompressed 32-bit BGRA, 840-byte pitch, one image level | `39d1d3077dcc040c4985dde76dd6791c02c60743aee0e5b490d278427fec0c84` |
| ten-asset contact sheet | 1840x1302 | RGB | `a46a3ec2acf91e4d6eca9e3c2ed5f75c570f34203a91835835e27a7675a8cc51` |

The final DDS decode is pixel-identical to the processed PNG. Alpha spans 0 through 255, with 2,932 transparent pixels, 6,484 partially transparent pixels, and 27,544 opaque pixels. The source image, processed card, and rebuilt ten-image contact sheet were visually reviewed.

## Static audit results

The Air Winter pilot now contains:

- 52 unique event blocks before the separate Fallout transition and manual event ranges
- 191 options
- 190 effect-bearing options
- 67 delayed-result schedules
- one effect-free stale-order acknowledgement

Event 49 is declared once and scheduled by exactly three event 13 choices. All 51 event references added or used by the Desert City opening and result resolve to exactly one localisation key. All six dynamic-modifier name and description keys exist. The localisation files retain their UTF-8 byte order marks.

The final source audit found balanced script blocks, no unsupported comparison operators, no unary negative variable tokens, exact sprite and path agreement, and no em dash or semicolon in the added gameplay or player-facing text. These mechanical checks support the review but do not substitute for runtime observation.

Two independent read-only audits reviewed the engine transaction and the event, localisation, and asset contract. The engine review identified the missing explicit pending-owner proof in the first result validator. Its follow-up pass also identified that a malformed exact receipt without the generic pending flag could survive monthly reconciliation. Both findings were corrected before this proof was finalized. The final engine-sensitive syntax pass corrected all ten Air Winter scripted-localisation rows from the unsupported British `localisation_key` spelling to the documented `localization_key` spelling. Those rows cover the government-aware nouns and the dynamic event-picture selector. The final localisation review then found no missing key, effect mismatch, generic prose, government mismatch, or prohibited punctuation.

## Unobserved engine boundary

The following remain unobserved because Hearts of Iron IV was not launched:

- exact Desert City route selection in a live candidate cycle
- subtype retention through a save and first-frost delay
- scripted event-picture rendering for exact and generic event 13 routes
- regular event-target retention through the 30-day result delay
- ownership change and malformed receipt reconciliation in engine order
- stockpile, fuel, manpower, Stability, and Command Power readback after payment
- local factory and supply modifier arithmetic and expiry
- repair behavior after 0.50 building damage
- exact province-building selection when more than one matching level exists in the state
- Deaths and population readback for every casualty percentage
- human popup availability and localisation rendering
- AI branch frequency
- save and resume behavior
- multiplayer scheduling and host authority behavior

These are runtime observation limits, not passing claims. No fallback or weaker substitute was introduced inside this tranche.

The wider Fallout implementation remains incomplete. The living-world release-floor count remains 0 of 660. The accepted numerical survival transaction is implemented. SCN-014 remains absent because the exact engine-native every-province thermonuclear sweep cannot be runtime proven without launching Hearts of Iron IV.
