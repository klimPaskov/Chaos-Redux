# CBRN Diplomacy Actions

## Purpose

The CBRN international-response layer adds material inspection pressure, exact-state forensic publication, and foreign decontamination relief to the shared Condemnation system. Each action consumes real equipment or factory capacity, uses a recorded country or state target, and preserves the existing death, contamination, evidence, attribution, and weapon-use histories.

The accepted design source is `docs/specs/chaos_warfare_system_specs/specs/09_condemnation_deaths_air_cleanliness_and_diplomacy.md`. This implementation also follows the consequence and evidence mappings under `docs/specs/chaos_warfare_system_specs/matrices/`.

## Demand Inspections

`cbrn_demand_inspections` targets one existing country at Formal Censure or above. The target must not already have active international inspections, an active refused-inspection policy, or another active CBRN inspection demand, and the two countries must not be at war.

The demanding country consumes:

- 10 CBRN instruments;
- 10 support equipment.

The target receives the 30-day `cbrn_answer_inspection_demand_mission`. Accepting the existing international-inspection decision grants inspectors access and clears the demand. Refusing inspections or allowing a still-valid demand to time out clears the demand and records the normal public blocked-inspection Coverup source. If the demanding country no longer exists, the deadline only clears the stale demand. The timeout guard prevents mission removal from recursively resolving the same refusal twice.

## Share Forensic Evidence

`cbrn_share_forensic_evidence` targets one state controlled by the publishing country. The state must hold at least one unpublished chemical action record or detected ordinary-pathogen episode with a live recorded actor, an action or seed date, and enough evidence to support publication.

The publishing country consumes:

- 20 CBRN instruments;
- 15 support equipment;
- one civilian factory for 21 days.

At completion the system selects the eligible record with the greatest evidence value. Equal evidence keeps the earlier candidate in the fixed inspection order. Biological weapon potency never affects selection: Tularemia, Anthrax, Plague, and Smallpox receive no different publication priority, just as their delivery success remains separate from their consequence hierarchy.

For a chemical record, publication:

- adds 15 state evidence;
- recalculates attribution through the shared chemical evidence resolver;
- records the action date as published;
- calculates the published share from that exact action's recorded paid and unpaid Chemical liability;
- exposes only the additional unpaid liability justified by the resulting attribution band;
- uses the actor's aggregate latent Chemical bucket only as a settlement ceiling, never as the source of the amount;
- never adds the original use source a second time.

For a biological record, publication:

- adds 15 evidence to the selected agent episode;
- records that episode's seed date as published;
- re-enters the selected agent's exact attribution and unpaid-Condemnation path;
- never changes the agent, raid outcome, delivery success, deaths, spread, or contamination history.

The 90-day state cooldown limits repeated publication work. A new action or a new biological episode in the same state remains eligible after the cooldown because its action or seed date differs from the published record.

## Sponsor Decontamination Mission

`cbrn_sponsor_decontamination_mission` targets one chemically contaminated foreign-controlled state. Access must be supported by a shared faction, subject relationship, active international inspections, or active foreign observers. The sponsor and recipient must not be at war.

The sponsor consumes:

- 100 gas masks;
- 60 decontamination sets;
- 30 CBRN instruments;
- 40 support equipment;
- 25 trucks;
- 10 convoys;
- two civilian factories for 45 days.

Masks, decontamination sets, and instruments are removed oldest model first through the established equipment-family debit helpers. The state stores the exact provider, initial recipient controller, and start date. A controller change or war with the provider cancels the mission without refund or cleanup.

At completion the mission removes contamination according to the current state band:

| Current contamination | Cleanup points |
| --- | ---: |
| Trace or Local | 12 |
| Serious | 10 |
| Severe | 8 |
| Catastrophic | 5 |

The lower cleanup rate in worse bands represents the larger contaminated area and material load, not weaker effort. An International Medical Mission designer raises cleanup by 25%. The mission also lowers current Medical Saturation by 12. If the state still contains observable chemical evidence, observer access adds 8 evidence and may expose an additional part of that exact action's unpaid Chemical liability. Repeating a mission at the same attribution band cannot expose the same liability again; only a stronger evidence band can justify a further transfer.

Cleanup never erases civilian deaths, military losses, evidence already acquired, attribution, the recorded action, contamination history, medical-saturation history, Condemnation history, or weapon-use history.

## Retaliation Authority

Confirmed chemical or biological use records an exact bilateral first-use ledger between the offender and victim. Retaliation Authority permits release only against that recorded offender, while the countries remain at war, for 365 days after confirmation. The record is keyed by country ID, so simultaneous wars and multiple offenders do not share authorization.

The system compares the earliest exact action date in both directions. A country that struck first cannot obtain mitigation by being attacked later. If both countries have a confirmed action on the same engine day, the result is contested and neither side receives retaliation mitigation.

Strategic or civilian-target retaliation may become policy-legal, but it receives no participant-pressure mitigation. Nerve-agent suppression and doomsday releases remain outside Retaliation Authority and require their own extreme-use gates. A verified battlefield or military-target response receives a 0.75 participant-pressure multiplier. That multiplier changes only the international participant pressure attached to the new use; it does not reduce the source Condemnation, deaths, evidence, attribution, contamination, medical saturation, resistance trauma, use history, or domestic consequences.

## AI

AI weights are route-aware and consume the same equipment as player actions.

- Democratic countries favor inspection demands and forensic publication.
- Inspection demands rise sharply against Arms Embargo targets and fall against faction partners.
- Forensic publication rises when chemical or biological evidence has reached confirmed attribution.
- Defensive CBRN profiles favor international decontamination.
- Decontamination rises for serious or worse contamination and for faction partners, while active war lowers priority.
- Retaliation weights require an active bilateral right against the selected target; a generic retaliation policy or another enemy's use does not qualify.

No AI path receives free equipment, free evidence, inferred attribution, or hidden cleanup.

## Source Map

| Surface | File |
| --- | --- |
| Central tuning | `common/script_constants/cbrn_diplomacy_constants.txt` |
| Eligibility and exact-record checks | `common/scripted_triggers/cbrn_diplomacy_triggers.txt` |
| Costs, record selection, publication, and cleanup | `common/scripted_effects/cbrn_diplomacy_effects.txt` |
| Bilateral first-use recording and exact retaliation classification | `common/scripted_effects/cbrn_diplomacy_effects.txt`, `common/scripted_effects/cbrn_exposure_effects.txt`, `common/scripted_effects/biological_lifecycle_effects.txt` |
| Exact chemical action liability | `common/scripted_effects/cbrn_consequence_effects.txt`, `common/scripted_effects/condemnation_sanctions_effects.txt` |
| Inspection response integration | `common/scripted_effects/condemnation_response_effects.txt` |
| Decision category | `common/decisions/categories/cbrn_diplomacy_categories.txt` |
| Decisions and mission | `common/decisions/cbrn_diplomacy_decisions.txt` |
| Opinion memories | `common/opinion_modifiers/cbrn_diplomacy_opinion_modifiers.txt` |
| Sprite registration | `interface/cbrn_diplomacy.gfx` |
| Player-facing text | `localisation/english/cbrn_diplomacy_l_english.yml` |
| Condemnation context registration | `common/script_constants/condemnation_sanctions_constants.txt`, `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt` |

All subsystem helpers remain in the CBRN-specific trigger and effect files. None is added to the generic dynamic trigger or effect API.

## Assets

The three independent 32x32 decision icons are:

- `GFX_decision_cbrn_demand_inspections` at `gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_demand_inspections.dds`;
- `GFX_decision_cbrn_share_forensic_evidence` at `gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_share_forensic_evidence.dds`;
- `GFX_decision_cbrn_sponsor_decontamination_mission` at `gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_sponsor_decontamination_mission.dds`.

The source PNGs, transparent intermediates, processed PNGs, final-DDS contact sheet, prompts, hashes, validation, manifest, and GFX handoff are under `docs/assets/chaos_warfare_system/stage_8_consequence_diplomacy/`. The icons are independent compositions and do not overwrite or resize any existing Chaos Redux raid or decision asset.

## Engine Boundaries

The implementation does not estimate responsibility from country history, substitute a nearby state, infer a missing actor, approximate a bilateral record, or derive one action's liability from an aggregate source bucket. Every chemical action records its own paid, unpaid, and total Chemical liability before publication. The aggregate latent Chemical bucket is used only to settle the exact recorded amount and cannot increase it.

No broad daily, weekly, or monthly all-country mutation pulse was added. Target and state eligibility are evaluated by the decision system, while selected actions mutate only their recorded targets.

## Future Plans

- Add more international-response actions only when the accepted specifications assign them a distinct material cost, exact target, and consequence boundary.
- Add a dedicated treaty or organization interface only if the existing decision and Condemnation interfaces become too dense; do not duplicate the same actions in two player surfaces.
- If future engine versions expose sub-day action timestamps, replace the documented same-day contested result with exact chronological ordering while preserving the current country-ID keyed ledger.
