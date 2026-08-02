# Spec 65: The New Year Without Fireworks

Status: accepted source design for a dormant Fallout implementation tranche. No live gameplay acceptance is claimed by this specification.

The New Year Without Fireworks is an East Asian country-only chain about a settlement turning the year beneath an ash-darkened winter sky. Covered lamps, a ration table, memorial ribbons, families, and guards create a concrete social choice without naming a real culture or institution.

The chain is Fallout-owned and uses `chaosx.fallout` only. It is not a super-event, decision category, mission, focus route, bilateral partner, country creation, recurring on-action, scripted GUI, achievement, formable, province target, or map rewrite.

## Identity ledger

| Surface | Assigned value |
| --- | --- |
| Candidate and human opening | `649` |
| Hidden-AI opening | `650` |
| Human delayed result | `651` |
| Hidden-AI delayed result | `652` |
| Human callback | `653` |
| Hidden-AI callback | `654` |
| Authenticated cleanup | `655` |
| Transaction key | `710064` |
| Callback transaction key | `710164` |
| Scheduler route | `7164` |
| Required new route upper bound | `7165` |
| Event Log history | `9170` |
| Catalogue identity | `FALLOUT-649` |
| Report asset identity | `fallout_new_year_without_fireworks` |

The identities are dedicated to this chain and do not reuse zombie ids, files, assets, audio, sprites, or paths. The row remains dormant while `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` are unset.

## Scheduling identity

- Runtime region: `fallout_region.east_asia`
- Primary family: `fallout_event_primary_family.regional_and_biome`
- Preferred phase: `fallout_event_phase.first_winter_year`
- Secondary phase: `fallout_event_phase.consolidation`
- Class: `fallout_event_class.routine_incident`
- Cooldown family: `fallout_event_cooldown_family.recovery`
- Primary and required resource index: `fallout_survival_resource.recognition`
- Visible budget cost: `2`
- Result delay: `21` days
- Callback delay: `330` days after result settlement

The candidate mechanic pressure is the inverse Cohesion gap from the reviewed ledger ceiling. The candidate severity is current Air Winter disease pressure. The state value is current durable Cohesion. The row has no state or province target and stores target value `0` with subject type `none`.

## Country admission

The country must have a current Fallout identity row, current generation, durable survival resource row, exact East Asian region, campaign day from `300` through `2599`, and no committed or closed New Year memory. It must also have at least one affordable branch and the following minimum values.

| Surface | Minimum |
| --- | ---: |
| Food | `12` |
| Clean Water | `8` |
| Fuel | `6` |
| Medicine | `5` |
| Shelter Capacity | `12` |
| Recognition | `8` |
| Cohesion | `20` |

The opening rechecks exact branch affordability before scheduling. Human options hide branches that cannot be paid. Hidden AI chooses only from the same affordable set.

## Four authored branches

### Quiet Remembrance

Quiet Remembrance spends Recognition `2`, Shelter Capacity `2`, and Medicine `1`. It keeps covered lamps and memorial ribbons in one shared register. Success strengthens Recognition, Shelter, Medicine, and the remembrance tradition ledger. Failure worsens disease, Recognition, Cohesion, and the country register, with the authored result Deaths request.

### Hold a Ration Feast

Hold a Ration Feast spends Food `5`, Clean Water `2`, and Fuel `1`. It tests whether a measured table can cross the winter queue without emptying the storehouse. Success strengthens Food, Water, Cohesion, and shared-table trust. Failure creates ration strain and a weaker shared-table memory.

### Stage a Military Ceremony

Stage a Military Ceremony spends Food `2`, Fuel `3`, and Command Power `10`. Guards protect the ration road while the covered lamps remain visible. Success strengthens Shelter, Recognition, Cohesion, War Support, and martial pageantry. Failure turns the ceremony into a closed checkpoint and increases the disease burden.

### Leave the Night to Local Festivals

Leave the Night to Local Festivals spends Food `3`, Recognition `2`, and Scrap `2`. Neighborhoods keep their own careful measure while memorial ribbons travel between doors. Success strengthens Recognition, Cohesion, and local festival autonomy. Failure fragments the night and weakens the durable country memory.

Human tooltips disclose the exact cost and both authored delays. No option creates a unit, building, state target, diplomatic partner, tag, government, or recurring pulse.

## Numerical grade contract

Before payment, the chain freezes Food, Clean Water, Fuel, Medicine, Shelter Capacity, Recognition, Scrap, Cohesion, War Support, Command Power, Stability, Exposure, Disease Pressure, the seven New Year ledgers, generation, owner, branch, mode, event token, transaction key, route, and receipt identities.

The result grade is a deterministic clamped viability score from frozen survival resources, Cohesion, Stability, inverse Exposure, and inverse Disease Pressure. Branch thresholds are fixed in the approved numerical contract.

| Branch | Success threshold | Partial threshold |
| --- | ---: | ---: |
| Quiet Remembrance | `58` | `38` |
| Hold a Ration Feast | `62` | `42` |
| Stage a Military Ceremony | `63` | `43` |
| Leave the Night to Local Festivals | `60` | `40` |

The callback reads current Food, Clean Water, Recognition, Cohesion, Calendar Trust, Civic Participation, and inverse Ration Strain. It succeeds at `64`, is partial from `42`, and fails below `42`.

Result failure requests `0.0015` of current population in every owned state through the existing Deaths contract. Callback failure requests `0.0007`. Both requests use the Fallout aftermath cause, explicit owner-country target, minimum remaining population, and Deaths logging. No direct population assignment is used.

## Durable ledgers

All seven ledgers are country-scoped and clamped from `0` through `100`.

| Ledger | Initial value | Primary consumers |
| --- | ---: | --- |
| Remembrance Tradition | `15` | Quiet Remembrance result and later identity text |
| Shared-Table Trust | `10` | Ration Feast result and callback grade |
| Martial Pageantry | `10` | Military Ceremony result and government-aware AI |
| Local Festival Autonomy | `15` | Local Festivals result and regional memory |
| Calendar Trust | `30` | Callback grade and generation text |
| Ration Strain | `20` | Callback grade and failure pressure |
| Civic Participation | `25` | Callback grade and durable country memory |

The selected branch applies branch-specific result deltas and one of the success, partial, or failure calendar, ration, and civic deltas. Cleanup preserves durable ledgers while clearing tickets, frozen values, payment receipts, and transient ownership flags.

## Hidden-AI behavior

Continuity Government, Technate, and Machine Protocol prefer Quiet Remembrance. Food Compact and Religious Refuge prefer Hold a Ration Feast when the exact costs are affordable and otherwise prefer Quiet Remembrance. Warlord Command prefers Stage a Military Ceremony during war. Nomad Convoy, Scavenger Syndicate, Maritime Remnant, and Mutant Polity prefer Local Festivals. Quarantine State prefers Quiet Remembrance at or above 60 disease pressure and allows Hold a Ration Feast below that threshold when it is affordable. Bunker Authority prefers Quiet Remembrance before choosing a feast.

The deterministic tie order is Quiet Remembrance, Local Festivals, Hold a Ration Feast, then Stage a Military Ceremony. Every unaffordable or invalid choice receives the reviewed invalid priority `-1000`. No random list or recurring MTTH pulse is required.

## Event Log contract

History `9170` records branch-specific success, partial, and failure payloads, callback success, partial, and failure, and the country as the primary actor. The Event Log detail and name routers use the dedicated `fallout.event_log.new_year_without_fireworks` keys.

The authoritative workbook is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. The row uses the final title, branch wording, 21-day result, 330-day callback, and no self-rescheduling. The export is regenerated with `python .tools/export_event_catalog_csv.py` after workbook updates.

## Cleanup proof

Opening, result, callback, and cleanup surfaces reauthenticate candidate `649`, route `7164`, opening transaction `710064`, exact branch, current dispatch token, mode, target type `none`, target `0`, owner receipt, payment receipt, result ticket, callback ticket when present, result commitment, and callback schedule or callback commitment. Cleanup does not require current generation, ownership, or region so a stale chain can release its own rows after a transition.

Refunds occur only when the exact payment flag exists and result effects were not committed. A callback scheduling failure releases the result row without refunding a committed result. Duplicate result, callback, or cleanup delivery cannot pass the issued-ticket and token checks. Final cleanup clears all transient chain flags and frozen receipt fields. No newer transaction is touched.

## Asset contract

The dedicated asset package is `docs/assets/649_new_year_without_fireworks/`.

- Sprite: `GFX_report_event_fallout_new_year_without_fireworks`
- Runtime path: `gfx/event_pictures/fallout/report_event_fallout_new_year_without_fireworks.dds`
- Dimensions: `210` by `176`
- Content: cold ash-darkened East Asian community at the year turning with covered lamps, a ration table, memorial ribbons, civilians, and guards
- Exclusions: readable script, flags, identifiable people, religious markers, branding, fireworks, zombies, animation, and audio

The source, processed PNG, runtime DDS, sprite registration, and hashes are listed in the asset manifest and proof handoff. The image is fictional and follows the approved single-report-art workflow.

## Runtime boundary

The source wiring is dormant and statically reviewable. Live scheduler dispatch, delayed queue delivery, Event Log rendering, save recovery, multiplayer delivery, host authority, and player-visible art remain unobserved until user validation in HOI4.

No HOI4 process is required for this implementation tranche.
