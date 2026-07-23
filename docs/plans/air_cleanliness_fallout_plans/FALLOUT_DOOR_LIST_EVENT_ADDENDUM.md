# Fallout The Door List event addendum

## Status and design decision

This is the next reviewed dormant global-survival tranche after Filters Fail at Night.
It is an implementation handoff, not scheduler activation approval.
No earlier Door List addendum exists, and the prior Bad Batch and Filters Fail addenda have implementation proof or handoff records, so this pass does not duplicate an unresolved plan.

The family matrix places the subject in Ash week, but the accepted scheduler forbids ordinary incidents before day 8.
The queue therefore forms during Ash week and reaches the sealed shelter as a `first_season` ordinary candidate.
It may use `first_winter_year` as its secondary phase.
It must never bypass the quiet-period lock to create an Ash-week popup.

## Fixed identities

| Surface | Value |
| --- | ---: |
| Human opening | `chaosx.fallout.230` |
| Hidden AI opening | `chaosx.fallout.231` |
| Human family result | `chaosx.fallout.232` |
| Human specialist result | `chaosx.fallout.233` |
| Human lottery result | `chaosx.fallout.234` |
| Human refusal result | `chaosx.fallout.235` |
| Hidden AI family result | `chaosx.fallout.236` |
| Hidden AI specialist result | `chaosx.fallout.237` |
| Hidden AI lottery result | `chaosx.fallout.238` |
| Hidden AI refusal result | `chaosx.fallout.239` |
| Human callback | `chaosx.fallout.240` |
| Hidden AI callback | `chaosx.fallout.241` |
| Cleanup | `chaosx.fallout.242` |
| Candidate identity | `230` |
| Transaction key | `710010` |
| Candidate route | `7110` |
| Candidate route upper bound after registration | `7111` |
| Event Log history | `9115` |
| Primary family | `global_survival_and_society` |
| Cooldown family | `shelter` |
| Event class | `crisis_incident` |
| Result delay | `12` days |
| Callback delay | `180` days after result |
| Visible budget cost | `3` |

The id search found no Fallout event, candidate, transaction, route, or history conflict.
Unrelated province numbers in manual ledgers are a separate identity domain.
All definitions belong in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

## Historical and regional basis

The design treats admission as an administrative and social choice rather than a generic catastrophe scene.
The British 1939 evacuation scheme assigned priority classes and receiving areas before movement, which supports the family and lottery lanes and the importance of an authenticated list.
The National Archives also documents billeting and organized movement from exposed urban areas into receiving communities, which supports a source-to-destination population transaction rather than created population.
Imperial War Museums records that public shelter access could outgrow official policy and force authorities to accommodate people already seeking safety.
Postwar refugee records show that prolonged camp exclusion harmed health, morale, and skills, which supports the callback consequences of refusal and specialist selection.

Research anchors:

- [UK Government Evacuation Scheme, 1939](https://www.nationalarchives.gov.uk/education/resources/home-front-1939-1945-part-one/government-evacuation-scheme/)
- [National Archives evacuation and billeting overview](https://www.nationalarchives.gov.uk/education/resources/evacuation-to-shropshire/)
- [Imperial War Museums on civilian air-raid preparation](https://www.iwm.org.uk/history/how-britain-prepared-for-air-raids-in-the-second-world-war)
- [UNHCR report on prolonged camp exclusion and lost skills](https://www.unhcr.org/publications/report-united-nations-high-commissioner-refugees-5)

These are design anchors, not a claim that every Fallout region copies British civil defence or postwar European camps.
Regional writing should translate the material facts into local institutions, such as communal cellars, mine galleries, metro platforms, hill forts, temple compounds, civic basements, or sealed industrial works.

## Candidate eligibility and deterministic state pair

The producer runs only through the accepted country-owned Fallout scheduler behind both dormant activation gates.
It adds no daily world iterator and does not receive a special on-action.
The candidate is nonrepeatable for the current country generation.

The current country must pass all of the following:

1. It has the current Fallout runtime generation, current country identity, current resource row, and a produced Air Winter snapshot.
2. It is in `first_season` or `first_winter_year`.
3. It has no current Door List candidate, pending transaction, result, callback, cleanup, issued tombstone, or completed memory.
4. It has one destination state and one different source state that pass the exact pair contract below.
5. It can afford at least one branch cost.
6. Its current country Shelter Capacity is at least `20`.

The destination state must be owned and controlled by the current country, carry the current Fallout state identity, carry the current produced Air Winter state snapshot, have state Shelter of at least `35`, and have current civilian population above the shared minimum-remaining floor.
The source state must be owned and controlled by the same country, carry the same current-generation identities, have at least `25,000` current civilian population, and have state Exposure at least `15` points above the destination state.
Source and destination can never be the same state.

The producer scans valid destination and source pairs in ascending destination state id and then ascending source state id.
It accepts the first valid pair and freezes both ids.
It never retargets if a later pair scores better.
This stable pair order is part of determinism.

The candidate scoring receipt uses:

- `severity = frozen source Exposure`
- `state_value = frozen destination Shelter`
- `resource_crisis = current country Shelter Capacity`
- `authored_adjustment = 0`
- preferred phase `first_season`
- secondary phase `first_winter_year`

Region, government, cause-memory, war, character, and relationship match inputs remain neutral unless a later accepted specification gives them an exact current-generation receipt.
The scheduler applies its normal family fatigue, state repetition, cadence, visible-envelope, and crisis-break rules.
There is no minimum-score rescue or fallback selection.

## Frozen opening receipt

Before the opening becomes pending, freeze the runtime generation, control mode, candidate id, transaction key, route, primary family, cooldown family, event class, visible budget cost, issue day, result due day, callback due day, source state id, destination state id, both current owners and controllers, both state identity generations, both Air Winter snapshot generations, source current civilian population, destination current civilian population, source Exposure, destination Exposure, destination Shelter, destination Supply Access, Food, Filters, Medicine, Scrap, Shelter Capacity, Recognition, Cohesion, Adaptation, and Reclamation.

Freeze the cohort and receiving capacity at issue:

`base cohort = min(round(source civilian population * 0.004), 20000)`

`receiving capacity = round(destination civilian population * destination Shelter / 1000)`

`arrival pressure = clamp(round(base cohort * 1000 / max(destination civilian population, 1)), 0, 100)`

All coefficients, bounds, thresholds, branch shares, costs, and deltas belong in `common/script_constants/fallout_world_end_event_constants.txt`.
The result may clamp actual removal to the source state's current safe removable population, but it may not recalculate the cohort, capacity, viability, or projected outcome from later world state.

## Four player choices

| Branch token | Choice | Opening payment | Population policy | Durable question |
| ---: | --- | --- | --- | --- |
| `1` | Admit family units | Food `6`, Filters `4` | Largest admission share | Whether household membership becomes the basis of shelter citizenship |
| `2` | Admit essential specialists | Medicine `4`, Shelter Capacity `3` | Smallest admission share | Whether technical service becomes a privileged class |
| `3` | Publish a public lottery | Recognition `4`, Filters `3` | Medium admission share | Whether a witnessed draw can become a legitimate civic institution |
| `4` | Refuse entry and reinforce the door | Scrap `5` | No admission | Whether exclusion becomes an inherited claim against the shelter |

Payments occur once, after ordinary-slot authentication and delayed-row reservation succeed.
If the selected branch is no longer affordable at commit, the opening closes through cleanup without charging another branch or changing the choice.
The implementation must not silently substitute an affordable branch.

## Deterministic outcome bands

The common admission viability is:

`30% destination Shelter + 15% country Shelter Capacity + 15% Filters + 15% Food + 10% Medicine + 10% destination Supply Access + 5% Cohesion - 20% source Exposure - 20% arrival pressure`

Round once and clamp from `0` through `100`.

| Branch | Success | Partial | Failure |
| --- | --- | --- | --- |
| Family units | viability at least `60`, Food at least `35`, Filters at least `30` | viability at least `40`, Food at least `20`, Filters at least `18` | all lower receipts |
| Essential specialists | viability at least `55`, Medicine at least `30`, Supply Access at least `35` | viability at least `38`, Medicine at least `18`, Supply Access at least `20` | all lower receipts |
| Public lottery | viability at least `58`, Recognition at least `35`, Cohesion at least `40` | viability at least `40`, Recognition at least `20`, Cohesion at least `25` | all lower receipts |

The refusal branch uses a separate door-control score:

`40% Scrap + 25% Cohesion + 20% Recognition + 15% destination Supply Access - 25% source Exposure`

Round once and clamp from `0` through `100`.
Refusal is orderly at `55` or more, fractured from `35` through `54`, and violent below `35`.
The labels success, partial, and failure remain mechanical outcome tokens and must not describe refusal as a moral success.

## Exact population movement and Deaths contract

The branch and outcome determine the intended movement share and intended death share of the frozen base cohort:

| Branch | Success moved, deaths | Partial moved, deaths | Failure moved, deaths |
| --- | --- | --- | --- |
| Family units | `100%`, `0%` | `75%`, `2%` | `50%`, `8%` |
| Essential specialists | `35%`, `0%` | `25%`, `1%` | `15%`, `6%` |
| Public lottery | `70%`, `0%` | `50%`, `1.5%` | `30%`, `7%` |
| Refuse and reinforce | `0%`, `0%` | `0%`, `3%` | `0%`, `10%` |

For an admission branch, calculate intended moved and intended deaths separately, add them into one source-removal request, and cap the moved share against the frozen receiving capacity.
Submit that combined request to `apply_exact_state_civilian_population_loss` in the authenticated source state with the shared minimum remaining population and `fallout_aftermath` reason.
Set Deaths logging off inside the removal helper.
Read back the applied amount, clamp intended deaths to that applied amount, subtract applied deaths from the applied total, add only the remainder to the authenticated destination state with `add_manpower`, and record the exact death remainder once through the shared Deaths API.

For refusal, submit only the intended death amount to the same exact source-state loss helper and add no population to the destination.
People who are not admitted or killed remain in the source state.
The transaction stores requested, applied, moved, killed, capacity-clamped, and source-population-clamped values for Event Log and audit use.
No direct negative manpower effect, duplicate Deaths call, population creation, or migration from a stale state target is allowed.

This follows the accepted Fallout orientation migration sequence.
The implementation should extract or mirror that exact authenticated sequence through a reviewed shared migration effect rather than create a second population-accounting convention.

## Branch consequences

Opening costs are separate from the following result deltas.
All deltas use the sole Survival resource helper, sole Cohesion helper, and authenticated Air Winter state helper.

| Branch and outcome | Result deltas and memory |
| --- | --- |
| Families success | Shelter Capacity `-4`, Recognition `+5`, Cohesion `+6`, destination Shelter `-3`, memory `family_rolls_opened` |
| Families partial | Shelter Capacity `-6`, Recognition `+2`, Cohesion `+1`, destination Shelter `-5`, memory `families_in_the_service_corridor` |
| Families failure | Shelter Capacity `-8`, Medicine `-2`, Recognition `-4`, Cohesion `-6`, destination Shelter `-7`, memory `family_admission_crush` |
| Specialists success | Reclamation `+5`, Adaptation `+3`, Recognition `+1`, Cohesion `-2`, destination Shelter `-2`, memory `service_charter` |
| Specialists partial | Reclamation `+2`, Adaptation `+1`, Recognition `-2`, Cohesion `-4`, destination Shelter `-3`, memory `ranked_bunks` |
| Specialists failure | Medicine `-2`, Recognition `-5`, Cohesion `-7`, destination Shelter `-5`, memory `failed_specialist_sort` |
| Lottery success | Shelter Capacity `-4`, Recognition `+5`, Cohesion `+7`, destination Shelter `-3`, memory `witnessed_draw` |
| Lottery partial | Shelter Capacity `-6`, Cohesion `+1`, destination Shelter `-5`, memory `contested_draw` |
| Lottery failure | Shelter Capacity `-8`, Recognition `-6`, Cohesion `-8`, destination Shelter `-7`, memory `rigged_list` |
| Refusal orderly | Recognition `-6`, Cohesion `-5`, memory `sealed_register` |
| Refusal fractured | Recognition `-9`, Cohesion `-8`, memory `names_left_outside` |
| Refusal violent | Shelter Capacity `-3`, Recognition `-12`, Cohesion `-12`, destination Shelter `-3`, memory `blood_at_the_door` |

The callback converts the result memory into one durable institutional memory:

- family branches produce a survivor-family registry that can support later reunification, household representation, and inheritance disputes
- specialist branches produce a service class that can support technical councils, credential disputes, and labor resistance
- lottery branches produce a civic roll that can support electoral legitimacy, fraud accusations, and appeals
- refusal produces an exclusion register that can support return columns, kin claims, and retaliatory politics

The callback applies only small branch-aware Recognition, Cohesion, Adaptation, or Reclamation deltas.
It causes no second population movement or casualty application.

## Country and state memory

The country stores selected branch, result token, requested cohort, applied source loss, moved population, deaths, callback institution, source state id, destination state id, and completion generation.
The source state stores the current-generation departure or exclusion memory.
The destination stores the current-generation admission memory and admitted amount.
Durable narrative memories that must survive a later generation change need an explicit survival binding in the accepted reset policy.
Operational pending, score, target, due-day, and helper variables must never survive cleanup.

## Hidden AI scoring

The hidden opening uses the same pair, costs, frozen values, viability formulas, outcome bands, population shares, result effects, callback, Event Log, and cleanup as the human opening.
Unaffordable branches are invalid and are not scored.
Each affordable branch starts at `10`, adds `8` for projected success or `3` for projected partial, and then applies:

- Food Compact adds `7` families, `5` lottery, and subtracts `5` refusal
- Continuity Council adds `4` families, `5` specialists, and `4` lottery
- Bunker Directorate adds `6` specialists, `5` refusal, and subtracts `3` families
- Warlord Seat adds `5` specialists, `8` refusal, and subtracts `5` lottery
- Maritime Authority adds `5` families, `5` specialists, and `3` lottery
- Quarantine Board adds `6` specialists, `7` refusal, and subtracts `4` families
- Scavenger Freehold adds `7` specialists and `3` refusal
- Nomad Compact adds `6` families, `4` lottery, and subtracts `3` refusal
- Machine Directorate adds `8` specialists, `5` refusal, and subtracts `4` families and lottery
- Technate adds `9` specialists, `1` lottery, and `2` refusal
- Mutant Communion adds `5` families, `6` lottery, and subtracts `8` refusal
- Religious Refuge adds `8` families, `2` lottery, and subtracts `4` refusal
- Food below `28` subtracts `5` families and `2` lottery, and adds `6` refusal
- Shelter Capacity below `28` subtracts `6` families, `3` specialists, and `5` lottery, and adds `8` refusal
- Recognition at least `35` adds `4` lottery and `2` families
- Source Exposure at least `70` adds `4` families, `3` specialists, and `4` lottery, and subtracts `4` refusal
- Being at war adds `4` specialists and `5` refusal, and subtracts `2` families and `1` lottery

The evaluator selects the highest score and replaces the current winner only on a strictly higher score.
Exact ties resolve families, specialists, lottery, then refusal.
It performs no random list or `ai_chance` roll.

## Transaction timing and cleanup

The human opening is visible and the AI opening is hidden.
The selected branch reserves one result row due exactly `12` days after the opening.
The result reserves one callback row due exactly `180` days after result commit.
Opening, visible result, and visible callback consume a human envelope cost of `3`.
The hidden AI result and callback are not visible, but the AI opening reserves the same narrative envelope so cadence cannot be evaded.

Result authentication requires exact generation, owner, controller, state ids, state identity rows, Air Winter snapshot rows, transaction key, branch token, due day, and unconsumed result tombstone.
Callback authentication requires the committed result token and exact callback due day.
World changes may reduce the applied source removal, but they never reroll the outcome.
Stale ownership, stale generation, deleted current-generation rows, missing source or destination, or duplicate tombstones close through cleanup with no retarget and no alternate branch.

Cleanup order is callback release, result release, pending receipt release, callback tombstone, result tombstone, candidate tombstone, then operational variable clearing.
Cleanup is idempotent and callable after every rejected commit.
Issued and completed memories remain long enough to prevent reissue in the same generation.

## Event Log, localisation, and presentation

History `9115` receives result payloads `11` through `43` for four branches across success, partial, and failure, plus callback payloads `51` through `53`.
The Event Log actor is the choosing country.
The detail receipt includes source state, destination state, selected list, frozen cohort, moved population, recorded deaths, result, and callback institution.
The event detail router and scripted localisation must map `9115` without changing another event family.

Human opening text must name the destination state, source state, available bunks, food and filter strain, and the physical act of reading or closing a list at the shelter door.
It must distinguish intact households, named skills, a witnessed draw, and refusal without revealing threshold arithmetic.
Results must report the exact moved and dead payloads in player-facing form.
Callbacks must describe a concrete institution, dispute, or remembered register.
Regional text may change the shelter material and admission authority, but it may not change mechanics or make unsupported claims about a real culture.
Hidden AI events need no player-facing prose.

## Dedicated asset handoff

Create one fictional documentary report image centered on a numbered metal shelter door, a paper list under a hooded lamp, chalked household marks, and a compressed queue seen through a controlled viewing slit.
Do not show monsters, gore, contemporary insignia, or a generic ruined skyline.
The human opening, result, and callback may share this dedicated family image.

Register `GFX_report_event_fallout_door_list` in `interface/fallout_world_end.gfx`.
Place the DDS under `gfx/event_pictures/fallout_door_list/`.
The handoff requires source PNG, processed `210 x 176` PNG, final DDS, prompt and provenance note, manifest, preview, and exact sprite path.
A static report image is sufficient because animation would not improve the admission decision.

## Engine-sensitive unresolved surfaces

1. Literal multiplayer lobby-host identity remains unproven in the accepted scheduler. This chain relies on the current deterministic country coordinator and does not claim that it has solved lobby-host authority.
2. The exact cross-effect persistence of two regular state targets through the opening, delayed result, callback, and cleanup must be proven with the scheduler's current state-id rebinding pattern before activation.
3. The orientation migration sequence is proven for one source and one destination, but a reusable generic helper is not yet documented. Implementation must review extraction or reproduce the authenticated sequence without altering Deaths semantics.
4. The visible cost `3` follows the accepted scheduler rule that opening, result, and callback each count. Existing older proof wording that calls a multi-popup chain cost `1` must not be copied.
5. The Technology Tree Viewer is not installed, and no technology or doctrine surface belongs to this event.

These are activation blockers where noted, not permission to add a substitute path.

## Acceptance checks

1. IDs `230` through `242`, candidate `230`, transaction `710010`, route `7110`, upper bound `7111`, and history `9115` are unique in their own domains.
2. Ash-week quiet time remains intact and the earliest ordinary opening is day `8`.
3. Source and destination are different, same-country, owned, controlled, current-generation states.
4. Pair selection is stable by destination id and then source id.
5. The opening freezes both identities and every outcome input before pending.
6. Exactly four human choices and four hidden AI choices map to four matching delayed result effects.
7. Branch payments are distinct, affordable at commit, and charged once.
8. Outcome classification rounds once, clamps once, and uses no random fallback.
9. Admission subtracts exact applied population from the source before adding the surviving moved amount to the destination.
10. Deaths records only the applied killed amount and never records moved population.
11. Refusal moves no population and applies any loss only to the source.
12. Current population changes can clamp application but cannot reroll branch or outcome.
13. Human result is due in `12` days and callback is due `180` days after result.
14. Visible budget cost is `3` and both human and AI openings reserve the envelope.
15. AI picks the highest valid score with the documented strict tie order.
16. Country, source-state, destination-state, and durable callback memories are written once.
17. Event Log history `9115` records branch, outcome, callback, states, movement, and deaths.
18. Human localisation is branch-aware, state-aware, and arithmetic-free.
19. The dedicated Door List asset is registered, wired, and documented.
20. Every stale, duplicate, unaffordable, or invalid transaction reaches idempotent cleanup with no retarget.

## Scope limits and promotion

This tranche needs no decision category, scripted GUI, focus route, formable, achievement, super-event, bilateral country consequence, or animated sprite.
Those surfaces would add bloat before the core shelter-citizenship memory has proven value in callbacks.

The file remains in `docs/plans/air_cleanliness_fallout_plans/` until the population helper, scheduler receipt, localisation family, Event Log route, asset manifest, and manual transaction proof are accepted.
After implementation review, merge fixed identities, state-pair eligibility, branch tables, population accounting, timing, AI scoring, memory, and presentation requirements into the global survival and society event bible and the family matrix.
The matrix should then describe the event as Ash-week-origin with first-season delivery.
