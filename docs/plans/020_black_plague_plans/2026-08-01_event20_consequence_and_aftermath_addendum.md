# Event 020 consequence, hierarchy, and defeat aftermath addendum

## Reconciliation status (2026-08-01)

This addendum is now a mixed-disposition record rather than an unimplemented tranche proposal.

| Package | Disposition in the current worktree | Remaining work or decision |
| --- | --- | --- |
| A. RTA hierarchy | Implemented statically: the three mutually exclusive roots, follow-ups, `.45` acknowledgement event, hierarchy state, runtime cap/pulse/absorption/candidacy consumers, and route-aware AI are present. | Six dedicated hierarchy icons, deeper route depth, and live route validation remain open. |
| B. RTX route crises | Implemented statically: `.57`, `.58`, and `.59` are defined and called from the route-capstone crisis paths, with route-specific meter and pulse consumers. | The crisis cards still use generic event art and have no declared live scenario proof. |
| C. Crown Strike | Implemented statically as a shared timed state action: the start gate, costs, dedicated icon, timeout/success effects, and `.64`/`.65` reports are wired. | It is not a native `activate_mission`/`days_mission_timeout` owner and has no live validation. The parent must decide whether the shared state-action API is accepted. |
| D. Defeat aftermath | Partially implemented: the idempotent resolver, `.71`, `.73`, `.74`, `.75`, and Seal Royal Burrows action exist. | Defeating-actor capture, targeted `on_capitulation`/`on_state_control_changed` hooks, contribution and reconstruction coupling, and the qualifying ID 87 gate remain unresolved. |
| Two-tag/no-model boundary | Accepted: `RTA` is the sole Rat Nation carrier, `RTX` is the separate Rat King, internal broods are state markers, and no 3D model production is required for this goal. | Archive-only RTB-RTM assets and bespoke models must not be revived as runtime requirements. |
| Super-event 87 | Reserved and production-blocked. | Keep the explicit global eligibility gate and final art, quote, audio, localisation, and registry blockers. |

The dispositions below are the current documentation source for this addendum; they do not claim whole-spec completion or live-game validation.

## Status and planning boundary

This is a bounded improvement-loop addendum for the next Event 020 content tranche.
It does not reopen the full Black Plague design package.
It converts accepted but shallow route and aftermath promises into implementable content while preserving the live disease, scenario, evolution, decision, achievement, and two-country architecture.

The two-tag correction is a hard acceptance rule.
`RTA` remains the only reusable base Rat Nation carrier and `RTX` remains the only Rat King country.
Additional broods remain state flags, Rat Infestation, Brood Mass, army pulses, and internal route state inside `RTA`.
No new Rat Nation tag, rival country, country pool, or tag-scaled scenario package may be added.

This tranche excludes 3D models, skeletal animation, new equipment, technology-tree work, a new decision category, a new disease mapmode, and a new scripted GUI.
The installed package has no Technology Tree Viewer, so no technology-tree evidence was produced.

## Relationship to prior plans

The accepted source specification remains `docs/specs/020_black_plague_specs/`.
This addendum is an implementation slice of Parts 5 through 8 and their matrices, not a competing design layer.

The earlier `rat_absorption_follow_up.md` is resolved by the live state-marker absorption implementation and is marked superseded in the same planning change.
The core-readiness report and the 2026-08-01 content-tranche handoff are implementation evidence, not unresolved expansion addenda.
No prior improvement addendum remains open for the design gaps owned here.

## Live evidence snapshot

The snapshot includes the current Event 020 worktree tranche, including its uncommitted RTA route modules and report-picture wiring.

| Surface | Current evidence | Remaining design gap |
| --- | --- | --- |
| Event chain | `events/020_black_death.txt` defines the accepted milestone allocation from `chaosx.nr20.2` through `.75`, plus `.90` and scheduler callbacks; events `.45`, `.57-.59`, `.64-.65`, and `.71-.75` are present | Most implemented milestones remain deliberately compact reports |
| Event pictures | Origin reports use `GFX_report_event_020_black_plague_origin`, overseas infection uses `GFX_news_event_020_black_plague_overseas`, and Rat emergence uses `GFX_report_event_020_rat_emergence` in the current worktree | Severe crisis, royal route crises, Crown Strike, Doctor Wu, ordinary Rat King defeat, and qualifying global defeat still reuse the scenario image or have no dedicated asset |
| RTA tree | Read-only focus inspection reports 35 playable focuses with zero node intersections and two connector crossings; the three-way hierarchy roots, follow-ups, and `.45` acknowledgement are present | Generic vanilla icon inventory diagnostics remain, six dedicated hierarchy icons are not wired, and the accepted full route-tree depth is still larger than this compact playable shell |
| RTA routes | Urban, Field, Dock, and War second lanes plus the three-way hierarchy now affect Brood Mass, division caps, spread routes, King candidacy, and route-aware AI | Additional bespoke route decisions and deeper narrative branches remain optional content work |
| RTX tree | Read-only focus inspection reports 50 playable focuses, including twelve route-policy focuses | The route policy consumers, crises, Crown Strike vulnerabilities, and AI plans are wired; deeper administration and cultural branches remain content work |
| Human counterplay | Emergency Countermeasure Drive, Royal Node strikes, route crises, Crown Strike, and Royal Burrow sealing have costs, time, success, failure, and reports `.54` through `.75` | Crown Strike is a shared timed state action rather than a native mission owner; dedicated crisis/aftermath art and live validation remain open |
| Rat King defeat | The rat pulse detects `RTX` with no controlled states, retires it idempotently, fires `chaosx.nr20.71`, and opens `.73` for the first eligible human response host | The resolver does not yet preserve a scoped defeating actor, the `.72` reconstruction path is not coupled to aftermath sealing, and ID 87 remains unwired |
| Reconstruction | `chaosx.nr20.72` fires immediately with global eradication | It is not tied to the work of securing former Royal Nodes or resolving the crown's archives |
| Super-events | Coronation ID 85 and world-end ID 86 have unique art, text, audio, and runtime wiring | `constant:black_plague_identity.global_defeat_super_event_id = 87` is reserved but has no trigger, image, localisation, quotation research, audio, or GUI registration |
| Documentation | The overview, route-module contract, event-chain map, decision matrix, and Part 7 now record the live two-tag route, Crown Strike, crises, and aftermath operations | This addendum, the readiness report, historical handoffs, prompts, and asset manifests are being reconciled so stale “missing” claims do not revive rejected work |

The focus inspector also reports missing references for many generic vanilla focus sprites.
Those diagnostics reflect its bounded sprite inventory and are not proof that vanilla sprites fail in game.
They do reinforce the accepted art requirement that major Event 020 route focuses should receive event-specific icons instead of remaining visually generic.

## Delivered tranche and remaining scope

The current tranche gives political route choices runtime effects, wires the late Crown Strike counterstroke, and turns Rat King defeat into a static aftermath path while leaving the established milestone chain intact.
Remaining accepted scope is the `.45` hierarchy report, scoped defeat attribution and reconstruction coupling, native-mission API decision review, final narrative and presentation breadth, dedicated severe-crisis/Doctor Wu/Crown Strike/Royal Burrow/global-defeat assets, source-frame UI animation, verified licensed audio and quotations for ID 87, workbook/catalog export reconciliation, and deeper optional route branches.

## Package A: RTA hierarchy becomes a real route choice

### Route graph

Keep `black_plague_rat_brood_signal` as the common root.
Rewire the current serial focuses into three mutually exclusive hierarchy roots:

```text
black_plague_rat_brood_signal
|-- black_plague_rat_four_mouths                    Distributed Instinct
|   `-- black_plague_rat_many_nests_one_signal      new follow-up
|-- black_plague_rat_choose_a_voice                 Dominant Beast
|   `-- black_plague_rat_fang_above_the_warren      new follow-up
`-- black_plague_rat_read_the_marks                 new Emergent Cunning root
    `-- black_plague_rat_stolen_route_memory         new follow-up

Any completed follow-up opens black_plague_rat_capped_pulses.
```

The existing archetype branches remain separate from this hierarchy choice.
Origin answers where `RTA` learned to survive.
Hierarchy answers how the single carrier coordinates its internal broods.

### Route tuning

Add one centralized `black_plague_rat_hierarchy_route` constant table and consume `black_plague_rat_hierarchy` inside the existing cap refresh, brood pulse, state-marker absorption, King candidacy, and AI helpers.
Use positive constants and explicit subtract effects rather than unary negative variable tokens.

| Route | Runtime gain | Runtime weakness | Exact target tuning |
| --- | --- | --- | --- |
| Distributed Instinct | More force capacity from a wide state network and faster internal marker consolidation | Lower raw Brood Mass growth and weaker Rat King candidacy | Add 2 division-cap points per controlled state, subtract 2 Brood Mass from each normal pulse, use a 45-day marker-consolidation cooldown, and subtract 15 from the King candidacy score |
| Dominant Beast | Larger pulses, stronger inherited state-marker units, and a direct candidacy advantage | Consolidation creates a longer internal lock and makes loss of the command center more damaging | Add 4 Brood Mass per normal pulse, add 12 persistent division-cap points, inherit one additional capped brood unit from a valid marker, use a 75-day marker-consolidation cooldown, and add 10 to the King candidacy score |
| Emergent Cunning | Better use of transport and occupation routes and the strongest Rat King candidacy | Smaller force ceiling and slower raw growth | Subtract 2 Brood Mass per normal pulse, subtract 10 from the hierarchy cap bonus before the final cap clamp, add 3 exposure only to valid transport or rat-occupation routes, and add 20 to the King candidacy score |

The route modifiers do not bypass Evolution II for overseas spread.
They do not change the global 180-division maximum.
They do not create conventional manpower, factories, equipment, research, diplomacy, or another rat country.

### RTA hierarchy event

Reserve `chaosx.nr20.45` as a country event for `RTA` with the working role **The Brood Finds an Order**.
It fires once when one of the three hierarchy roots completes.
The focus is the choice, so the event has one acknowledgement option and uses triggered description blocks for Distributed, Dominant, and Emergent outcomes.

Narrative direction:

- Distributed describes signals passing between many nests without a single permanent center.
- Dominant describes one body or command pattern becoming the source of every pulse.
- Emergent describes routes, captured marks, and repeated human behaviors becoming a primitive strategic language.
- Do not describe separate Rat Nation governments or rival tagged countries.
- Do not reveal the sentient Rat King before Evolution IV.

The event should set one one-shot history detail and expose the selected hierarchy in Event Details.
It should not register a second evolution.

### RTA AI

The focus AI chooses:

- Distributed when `RTA` controls at least six states, the territory is disconnected, or no single capital basin holds most controlled states.
- Dominant when `RTA` controls three or fewer states, has high Brood Mass, faces an active war, or needs faster local reinforcement.
- Emergent when Evolution II is active and `RTA` controls a port, rail hub, supply hub, or at least two urban states.

The hierarchy choice must also alter template and target preferences after completion.
Distributed favors coverage and burrow units, Dominant favors brutes and concentrated front requests, and Emergent favors dock, rail, capital, and supply-hub pressure.

## Package B: RTX route policies produce crises and vulnerabilities

Do not add another broad RTX focus lane in this tranche.
The current fifty-focus tree is deep enough for the next step to be consequence wiring.
Use the existing capstone flags as the activation points:

- `black_plague_rat_crown_dominion`
- `black_plague_rat_council_transparent_hunger`
- `black_plague_rat_hierophant_final_omen`

### Absolute Crown crisis

Reserve `chaosx.nr20.57` as **The Tithe Fails**.
It fires once after the Crown policy capstone when the first Royal Node is successfully struck or royal Hunger reaches the existing crisis threshold.

Option direction:

1. Replace the failed warden.
   Spend 10 Dominion, gain 15 Cohesion, and block the next royal pulse for 30 days while the command chain is rebuilt.
2. Exact the missing tribute.
   Gain 15 Brood Mass and 5 terminal preparation, add 10 Hunger, and set `black_plague_rat_crown_brittle_command` for the later Crown Strike calculation.

The Crown AI replaces the warden when Hunger is high, Cohesion is below 50, or the Royal Basin is exposed.
It exacts tribute when Dominion is above 60 and the immediate front is secure.

### Council crisis

Reserve `chaosx.nr20.58` as **The Warrens Refuse the Ledger**.
It fires once after the Council policy capstone when Hunger reaches the crisis threshold or a Council Royal Node is lost.

Option direction:

1. Honor the charter.
   Gain 15 Cohesion, add 5 Hunger, and subtract 10 terminal preparation.
2. Appoint an emergency speaker.
   Gain 10 Dominion, lose 10 Cohesion, and set `black_plague_rat_council_emergency_speaker` until the first crisis is resolved.

The Council AI honors the charter when Cohesion is below 60 or controlled territory is disconnected.
It appoints a speaker when the target continent is close to the accepted control threshold.

### Hierophancy crisis

Reserve `chaosx.nr20.59` as **Ash Beneath the Throne**.
It fires once after the Hierophancy policy capstone when Hunger reaches the crisis threshold or a human country reaches 70 countermeasure progress.
The countermeasure branch should fire from the existing country progress writer when a responder crosses 70, then address `RTX` through the saved Rat King target.
It must not search every country from the rat pulse.

Option direction:

1. Consume another prepared city.
   Gain 20 Brood Mass and 10 terminal preparation, add 15 Hunger, and increase Rat Infestation only in one valid `RTX`-controlled urban state selected by the existing registered-state logic.
2. Seal the reliquaries.
   Lose 10 Dominion, reduce Hunger by 15, and suspend the Hierophancy route exposure bonus for 60 days.

The Hierophancy AI consumes a city only when Hunger remains below 60 and terminal eligibility is close.
It seals the reliquaries when Hunger is high, countermeasure progress is widespread, or the Royal Basin is threatened.

### Route-policy runtime consumers

The route capstones should also modify the existing Rat King pulse and human Royal Node outcome helpers.
They must not remain flags that are read only by localisation or focus availability.

- Crown policy adds 3 Dominion per successful royal pulse but causes an additional 10 Dominion loss when the Crown Strike succeeds.
- Council policy adds 2 Cohesion per successful royal pulse and requires three struck Royal Nodes before the Crown Strike can start, but a successful Crown Strike causes an additional 15 Cohesion loss.
- Hierophancy policy adds 3 route exposure to valid overseas, port, or rat-occupation paths while not suspended, but a successful Crown Strike subtracts an additional 15 terminal preparation and suspends that route exposure for 90 days.

All values belong in script constants.
The existing meter clamps remain authoritative.

## Package C: one earned human Crown Strike

### Decision and mission identity

Reserve `black_plague_shared_action.strike_the_crown = 33`.
Add `black_plague_shared_strike_the_crown` inside `chaosx_disease_containment_category`.
It is a state-targeted selectable mission aimed at the current `RTX` capital or preserved Royal Basin target.

Implementation note: the current worktree exposes this surface as a shared timed state action using `days_remove`; it does not yet own native `activate_mission` or `days_mission_timeout` fields. The design below remains the accepted behavior contract while the parent decides whether the API simplification is sufficient.

This is not a second Royal Node action.
Royal Node strikes create the opening.
The Crown Strike asks a human country to capture the sovereign basin before the terminal route hardens again.

### Start requirements

The mission is visible only when:

- Evolution IV is active.
- `RTX` exists, owns at least one state, and is not defeated.
- terminal takeover is not active.
- the target state is the current `RTX` capital or the saved Royal Basin.
- the acting human country is at war with `RTX` and has a valid land, neighboring, airborne, or naval military route using the same concrete reach standard as Royal Node strikes.
- at least two Royal Nodes have been successfully struck globally.
- the acting country has personally completed at least one Royal Node strike.
- the Council route requires three struck Royal Nodes instead of two.

### Cost and duration

Create dedicated constants rather than multiplying payment values inside decision text.

- 240 support equipment
- 120 motorized equipment
- 500 infantry equipment
- 7,000 manpower
- 2,400 fuel
- 30 command power
- five civilian factories
- five Response Capacity
- 180 days

The costs are intentionally twice the current country material bundle because this is a sovereign attack rather than another node raid.
The decision must show every cost and the exact target state.

### Success and failure

Success requires the target state to leave `RTX` control before the 180-day deadline while the acting country remains a valid human host.
Success fires `chaosx.nr20.64`, working role **The Crown Is Broken**, and applies:

- subtract 20 Dominion
- subtract 20 terminal preparation
- subtract 15 Cohesion
- block royal pulses for 60 days
- set the disputed-crown crisis state
- apply the route-specific additional loss described in Package B

Success does not defeat `RTX`, cure any state, remove Rat Infestation, or grant Evolution V.

Timeout fires `chaosx.nr20.65`, working role **The Deep Roads Close**, and applies:

- add 10 Dominion
- add 10 terminal preparation
- add 10 Hunger
- block the acting country from starting another Crown Strike for 180 days
- add 5 additional Dominion for Crown, 5 Cohesion for Council, or 5 terminal preparation for Hierophancy

The mission cancels without a second payoff if `RTX` is defeated, terminal takeover begins, the target becomes invalid for a reason other than successful human capture, or the acting country ceases to exist.
All material costs remain spent after activation.

### Crown Strike AI

AI starts the mission only when it has real reach to the Royal Basin, at least 150 percent of every material requirement, at least one viable front against `RTX`, and no domestic Severe Crisis that already consumes its last Response Capacity.
AI gives the mission maximum priority when terminal preparation is at least 75 or `black_plague_rat_king_route_completed` is set.
It avoids the mission when the target is isolated behind an unreachable sea zone or the acting army cannot materially contest the state.

## Package D: Rat King defeat becomes an aftermath

### One-shot resolver

Create `black_plague_rat_king_resolve_defeat` as the only effect that finalizes Rat King defeat.
The current event-owned rat pulse remains a reconciliation check.
Add targeted calls from `on_capitulation` and from `on_state_control_changed` when the changed state is the Royal Basin or a Royal Node and `RTX` has no controlled states.

Implementation note: the idempotent resolver and pulse fallback are present, but the targeted on-action calls and defeating-actor capture described below are not yet wired in the current worktree.

The vanilla scope precedent is explicit that `on_capitulation` uses ROOT as the capitulated country and FROM as the winner.
The vanilla `on_state_control_changed` precedent uses ROOT as the new controller, FROM as the old controller, and FROM.FROM as the state.
Use those scopes to save the defeating actor without scanning every country.

The resolver runs once and must:

1. Record the defeat date, route taken, peak metrics, and valid defeating actor.
2. Set the existing global and `RTX` defeated flags.
3. Clear Rat King active, grace-period, pulse, route-completed, target-continent, Crown Strike, disputed-crown, and terminal-readiness state that cannot survive defeat.
4. Remove `RTX` from active Rat King arrays and world-threat contribution while preserving history and Evolution IV records.
5. Cancel Rat King decisions and active human Crown Strike missions without paying failure rewards.
6. Keep every surviving Black Plague state, Rat Infestation value, former Royal Node marker, and `RTA` country intact.
7. Fire the existing global defeat news `chaosx.nr20.71` once.
8. Send `chaosx.nr20.73` to the saved defeating actor.
9. Evaluate the qualifying global defeat super-event gate.

Do not set global eradication merely because `RTX` is defeated.
Do not fire reconstruction `.72` until the aftermath mission or ordinary eradication conditions justify it.

### Defeating actor selection

Use this deterministic order:

1. The human host in the scoped `on_capitulation` winner or the new controller of the last Royal Basin state.
2. The living human country with the highest recorded successful Royal Node and Crown Strike contribution from the event-owned contributor registry.
3. For an AI-only war, the living AI winner from the same scoped hook.

If the first actor ceases to exist before event delivery, advance to the next recorded contributor.
Do not search every country and do not assign the choice to `RTX`.

### Crown ruins event

Reserve `chaosx.nr20.73` as **The Crown's Ruins** for the defeating actor.

Option direction:

1. Seal the Royal Burrows.
   Start `black_plague_shared_seal_royal_burrows`, a 180-day country mission using one country material bundle, 15 command power, three civilian factories, and three Response Capacity.
   Success requires every former Royal Node controlled by the actor to complete warren clearance and no former Royal Basin state to remain Rat-Controlled.
2. Preserve the Royal Archives.
   Gain 15 countermeasure progress and set `black_plague_royal_archive_retained`.
   Add 10 relapse risk and 10 Rat Infestation to each former Royal Node still controlled by the actor.
   If the country has an active weaponization project, add the existing condemnation and accident-pressure consequences rather than granting a free offensive payload.

The archive option is not available when the actor lacks a secure controlled former Royal Node.
The seal option remains the default AI choice for cooperative, democratic, medically focused, or domestically infected countries.
Aggressive weaponization AI may preserve the archive only when it can pay the cleanup burden and has not reached full countermeasure progress.

### Seal mission outcomes

Reserve `chaosx.nr20.74` as **The Royal Burrows Are Sealed**.
On success, clear former Royal Node markers only in states that completed cleanup, reduce Rat Infestation by 20 and disease load by 10 in those states, add monitoring memory, and permit reconstruction `.72` when no active rat country or Severe Crisis remains.

Reserve `chaosx.nr20.75` as **Crownless Warrens**.
On timeout, keep uncleared Royal Node markers, add 10 Rat Infestation and 10 incoming exposure to one valid uncleared basin, and invoke the existing rat-resurgence report path.
Failure never reactivates `RTX`, restores the terminal route, or creates another tag.

### Qualifying global defeat super-event

The reserved ID is `constant:black_plague_identity.global_defeat_super_event_id = 87`.
It is optional campaign presentation with a strict gate, not a replacement for the ordinary `.71` defeat news.

All of these hard requirements must be true:

- the Rat King remained active for at least 365 days
- Event 020 deaths reached at least 50,000,000
- `RTX` controlled at least 20 states at its recorded peak
- established Black Plague or Rat-Controlled states reached at least four continents at the recorded peak
- at least three distinct major human opponents or response contributors were recorded
- Evolution IV occurred naturally or through SCN-012, but terminal world end did not fire
- the qualifying defeat super-event has not fired before

Track peak states, peak affected continents, duration, and major contributors through the existing event-owned pulse and targeted war or response hooks.
Do not add a world-iterating periodic on-action.

When the gate passes, show super-event 87 after `.71` and before `.73`.
The package requires its own 457 by 328 image, researched public-domain or licensed quotation, original description, short researched cultural remark, unique licensed lament or memorial track, settings-aware playback ID, source evidence, attribution, and music-catalog row.
Do not reuse coronation audio 101, world-end audio 102, their images, or their quotation families.
Do not enable `super_event_visible` for ID 87 until every asset and localisation consumer exists.

## Asset production and wiring package

The existing origin, overseas, and Rat-emergence assets are complete and wired in the current worktree.
Do not regenerate or rename them.

| Stable working asset | Type and size | Source mode | Consumer |
| --- | --- | --- | --- |
| `report_event_020_black_plague_severe` | report card, 210 by 176 | generated period-documentary | `.6`, `.8`, and emergency failure `.56` |
| `report_event_020_rat_king_crisis` | report card, 210 by 176 | generated fictional documentary | `.53`, `.57`, `.58`, and `.59` |
| `report_event_020_crown_strike` | report card, 210 by 176 | generated fictional documentary | `.54`, `.55`, `.64`, and `.65` |
| `news_event_020_rat_king_defeat` | news strip, 397 by 153, black and white | generated fictional period-news | `.71` |
| `report_event_020_rat_king_aftermath` | report card, 210 by 176 | generated fictional documentary | `.73`, `.74`, and `.75` |
| `report_event_020_doctor_wu` | report card, 210 by 176 | generated period-documentary with the approved fictional Doctor Wu treatment | Event 163 Black Plague bridge reports |
| `super_event_087_rat_king_defeat` | super-event art, 457 by 328 | generated fictional art | qualifying global defeat only |
| `decision_strike_royal_node` | decision icon, 33 by 32 | generated icon | existing Royal Node strike |
| `decision_strike_the_crown` | decision icon, 33 by 32 | generated icon | new Crown Strike mission |
| `decision_seal_royal_burrows` | decision icon, 33 by 32 | generated icon | new aftermath mission |

The RTA hierarchy route needs six 94 by 86 focus icons for `four_mouths`, `choose_a_voice`, `read_the_marks`, and their three follow-ups.
The three roots should share an entwined-tail signal family while remaining compositionally distinct.
Distributed uses multiple equal knots, Dominant uses one commanding head or fang, and Emergent uses a captured route map or signal marks.

Static art is appropriate for this tranche because the new consumers are one-shot event cards, decision icons, and focus-route symbols.
Motion would not communicate a changing gameplay value on those surfaces.
The accepted source-frame crisis seal and animated Rat King portrait remain separate queued asset packages and are not replaced by transform-only animation.
No 3D asset is requested.

Every asset handoff must retain source PNG, processed PNG, final DDS, exact sprite name, target `.gfx`, dimensions, source mode, prompt or provenance, contact sheet, and consumer crosswalk.

## Documentation and source-of-truth promotion

This addendum remains the working disposition record under `docs/plans/020_black_plague_plans/`.
The event-chain map, decision matrix, Part 7 aftermath spec, overview, and route-module contract already carry the statically implemented `.57-.59`, `.64-.65`, and `.73-.75` surfaces.
Do not create duplicate implementation work from the historical package prose.
Promote only the still-accepted design gaps rather than leaving two competing sources:

- merge the three-way RTA hierarchy and its exact consumers into Part 5 and the focus architecture matrix
- merge RTX route crises and Crown Strike vulnerability into Part 6
- merge the Crown Strike mission, defeat resolver, aftermath choice, seal mission, and super-event 87 gate into Part 7
- merge AI, tuning, validation, and asset requirements into Part 8
- keep `.45`, `.57` through `.59`, `.64`, `.65`, and `.73` through `.75` aligned with the current event-chain map
- update `decision_mission_matrix.md`, `ai_strategy_matrix.md`, `asset_inventory.md`, `focus_tree_route_architecture.md`, `implementation_acceptance_checklist.md`, and `tuning_and_balance_targets.md`
- preserve the two-tag correction as the highest-priority country rule

The following documentation updates are already promoted or being reconciled:

- `docs/events/020_black_plague/overview.md`
- `docs/events/020_black_plague/shared_response.md`
- `docs/systems/black_plague_rat_route_modules.md`
- `docs/assets/020_black_plague/event_art/manifest.md`
- `docs/assets/020_black_plague/rat_identity_asset_manifest.md`
- `docs/assets/020_black_plague/audio_manifest.md`
- the Event 020 super-event research and music-catalog records
- the Event 020 workbook row remains parent-owned; this cleanup does not edit the workbook or export-only CSVs

The Rat identity manifest must classify RTB through RTM flag art as archival unused production after the two-tag correction.
It must not present those tags as Event 020 runtime requirements.

## Suggested implementation surfaces

Gameplay and presentation files likely affected by an accepted implementation are:

- `events/020_black_death.txt`
- `common/national_focus/020_black_plague_rat_focus_tree.txt`
- `common/script_constants/020_black_plague_rat_constants.txt`
- `common/script_constants/020_black_plague_shared_response_constants.txt`
- `common/scripted_effects/020_black_plague_rat_effects.txt`
- `common/scripted_effects/020_black_plague_shared_response_effects.txt`
- `common/scripted_triggers/020_black_plague_rat_triggers.txt`
- `common/scripted_triggers/020_black_plague_shared_response_triggers.txt`
- `common/decisions/020_black_plague_rat_decisions.txt`
- `common/decisions/020_black_plague_shared_response_decisions.txt`
- `common/ai_strategy/020_black_plague_rat_ai_strategy.txt`
- the existing Event 020 on-action integration file for targeted capitulation and state-control hooks
- `localisation/english/020_black_plague_reports_l_english.yml`
- `localisation/english/020_black_plague_rat_focus_l_english.yml`
- `localisation/english/020_black_plague_rat_decisions_l_english.yml`
- `localisation/english/020_black_plague_response_l_english.yml`
- `localisation/english/020_black_plague_super_events_l_english.yml`
- `interface/020_black_plague_event_pictures.gfx`
- `interface/020_black_plague_rat_identity.gfx`
- `interface/020_black_plague_response.gfx`
- the shared super-event sprite and scripted-localisation registries for ID 87
- the shared sound registry and settings-aware playback helper for the new defeat audio ID

Do not add a world-periodic daily, weekly, or monthly on-action.
Use event-owned arrays, the existing seven-day Event 020 pulse, focus completion, decision outcomes, `on_capitulation`, and narrowly gated `on_state_control_changed` calls.

## Implementation order and current dispositions

Steps 2 through 5 are statically represented in the current worktree, with the limitations in the reconciliation table above.
Step 1 is only partially promoted because the defeat-actor contract remains unresolved.
Step 6 is intentionally blocked by the ID 87 asset and eligibility gate.
Steps 7 through 9 remain documentation, asset, and validation work and must not be read as completed by the static wiring.

1. Promote the accepted addendum into the source spec and reserve all identifiers.
2. Rewire the RTA hierarchy graph and add its constant-backed runtime consumers and AI.
3. Add RTX policy consumers and route crisis events.
4. Add Crown Strike state targeting, mission lifecycle, route modifiers, reports, and AI.
5. Add the one-shot Rat King defeat resolver, actor registry, aftermath event, seal mission, and cleanup.
6. Add global-defeat qualification tracking and trigger only after the ID 87 art, text, quotation, audio, GUI, and sound package is complete.
7. Wire the static event, decision, and focus assets without renaming the already-wired origin, overseas, or Rat-emergence sprites.
8. Align localisation, Event Details, event log, docs, manifests, workbook, and export-only catalogs.
9. Run focus, decision, localisation, event-completion, asset, and documentation audits before any completion claim.

## Acceptance scenarios

### RTA hierarchy

- Each campaign can complete exactly one of Distributed, Dominant, or Emergent hierarchy roots.
- All three routes can reach `black_plague_rat_capped_pulses` with the correct fixed archetype branch.
- The hierarchy variable is read by pulse, cap, absorption, candidacy, and AI logic.
- Distributed produces a wider but slower brood, Dominant produces a stronger concentrated brood with a longer consolidation lock, and Emergent produces better route pressure with a smaller army ceiling.
- `RTA` remains the only base Rat Nation tag in every route.

### RTX route consequences

- Only the crisis for the completed government policy capstone can fire.
- Every route has one meaningful player choice, one AI decision rule, one pulse consumer, and one Crown Strike vulnerability.
- Crisis events cannot repeat after their route's one-shot resolution.
- Route meters remain clamped and no option grants human industry or manpower.

### Crown Strike

- The mission cannot appear before Evolution IV or before the Royal Node requirement.
- The target is always the live `RTX` capital or saved Royal Basin.
- Material and Response Capacity costs are paid once and remain paid after activation.
- Human capture before 180 days produces `.64` and the exact route-adjusted setback.
- Timeout produces `.65` and the exact route-adjusted royal recovery.
- Defeat or terminal takeover cancels the mission without paying the wrong outcome.
- AI never starts the mission against an unreachable target.

### Rat King defeat and aftermath

- Capitulation, loss of the last Royal Basin state, and the event-owned pulse all converge on one idempotent defeat resolver.
- `.71` fires once, a valid defeating actor receives `.73`, and `RTX` cannot continue pulses, decisions, or terminal preparation afterward.
- `RTA` and established plague states survive until their own cleanup or defeat rules resolve.
- Sealing former Royal Nodes can succeed through real state cleanup and fire `.74`.
- Failure fires `.75`, creates bounded resurgence pressure, and never revives `RTX` or creates another tag.
- `.72` represents earned reconstruction rather than automatically following every Rat King defeat.

### Super-event 87

- A short regional Rat King war never shows super-event 87.
- A 364-day crisis never shows it.
- A crisis below any hard global, death, territory, continent, or major-participant requirement never shows it.
- A qualifying 365-day global catastrophe shows it once after `.71` and before `.73`.
- The super-event uses unique art, unique researched text, unique licensed audio, settings-aware playback, and a complete provenance record.
- World end and defeat super-events are mutually exclusive.

### Two-tag and scenario integrity

- Natural play and every SCN-012 intensity create or preserve only `RTA` and `RTX`.
- Scenario intensity scales states, armies, meters, and Chaos without scaling tag count.
- No event or localisation describes independent tagged Rat Nations after the correction.
- `.41` and `.43` describe internal broods and state-marker consolidation rather than multiple Rat Nation countries.

## What should not be added

- no third rat tag
- no restoration of RTB through RTM runtime use
- no diplomatic rat faction or human alliance route
- no fourth RTX government route
- no second Rat King defeat decision category
- no standalone Black Plague reconstruction GUI
- no super-event for each hierarchy choice or route crisis
- no random Crown Strike success detached from the target state's military outcome
- no instant cure, automatic eradication, or deletion of Rat Infestation after victory
- no reusable coronation or world-end art or audio for defeat
- no transform-only animation package
- no 3D unit or building model

## Research basis and historical connections

The existing source-attributed Event 020 research pack is sufficient for this bounded design pass.

- Wu Lien-teh's Manchurian plague response supports the need for masks, isolation, movement control, and management of infected bodies after military victory.
- Dubrovnik and Venice quarantine institutions support a costly, sustained Royal Basin cleanup instead of an instant postwar cure.
- Plague transmission through trade routes, ports, troop movement, and refugees supports the RTA archetype and Emergent route consumers.
- Haffkine's plague-vaccine history supports countermeasure and archive knowledge that still requires production and delivery.
- Regional mortality variation supports leaving former Royal states infected and locally differentiated after `RTX` falls.
- Rat king folklore uses entwined tails as an omen and collective symbol, which supports the Distributed, Dominant, and Hierophant visual language without claiming a historical sentient monarchy.
- The real rat king phenomenon remains distinct from the supernatural Event 020 sovereign.

The implementation pattern should mirror Event 016's event-driven qualifying-defeat score, peak-state tracking, saved victor handoff, and nonterminal aftermath ownership where compatible.
For engine scopes, use the vanilla `on_capitulation` and `on_state_control_changed` precedents inspected in `common/on_actions/00_on_actions.txt` and `events/CapitulationEvents.txt`.

## Open questions and blockers

The current shared timed state-action implementation leaves one parent design choice: whether Crown Strike and Seal Royal Burrows satisfy the accepted mission contract or must be converted to native mission fields.
The remaining `.45`, scoped actor, reconstruction, asset, and ID 87 gaps are implementation or production blockers rather than reasons to redesign the two-tag/no-model boundary.

The qualifying defeat super-event remains production-blocked until a unique quotation, cultural remark, audio track, and image receive research and asset handoffs.
Do not substitute another Event 020 super-event package.

The live Event 020 worktree was changing during this review.
The parent should refresh identifier and diff checks before implementation, preserve the route and event-picture tranche already in progress, and avoid reverting unrelated Event 020 edits.

## Parent implementation handoff

Current state: the RTA hierarchy graph and most runtime consumers, RTX route crises `.57-.59`, Crown Strike `.64-.65`, and static defeat/aftermath `.71-.75` are present in the worktree.

Still required before this addendum can be closed: decide whether the shared timed state-action API is sufficient for Crown Strike or a native mission owner is required, capture the scoped defeating actor through the accepted on-action hooks, couple reconstruction `.72` to the earned aftermath path, add the qualifying ID 87 gate and unique presentation package, replace generic crisis/aftermath art and missing hierarchy icons, and run the task-specific runtime validations.

The two-tag/no-model boundary is accepted and must remain unchanged: `RTA` plus `RTX` only, internal broods as state markers, and no 3D model production in this goal.

Research basis remains the accepted plague science, quarantine, Wu Lien-teh, Haffkine, transport-route, regional mortality, and Rat King folklore notes, plus the Event 016 qualifying-defeat architecture and vanilla capitulation scopes.

`rat_absorption_follow_up.md` is resolved and superseded by the live state-marker absorption path.
No additional improvement addendum should be spawned for this surface until the parent either implements, promotes, queues with a reason, or rejects the remaining gaps above.
