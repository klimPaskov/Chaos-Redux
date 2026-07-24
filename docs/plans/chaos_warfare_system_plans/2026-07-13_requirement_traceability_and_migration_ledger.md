# Chaos Warfare requirement traceability and migration ledger

Date: 2026-07-13

Purpose: preserve the complete accepted scope while implementation proceeds. A row may move from `queued` to `implemented` only when the listed repository evidence exists and has been reviewed. `Verified` is reserved for task-specific validation evidence, not mere file presence.

Status vocabulary: `queued`, `in progress`, `implemented`, `verified`, `verified by explicit user instruction`, `unsupported`.

## Authority decisions

| ID | Decision | Status | Evidence |
| --- | --- | --- | --- |
| AUTH-01 | Numbered specs govern over matrices, then specialist prompts, then legacy behavior. | verified | Package source-of-truth map and Stage 0 note. |
| AUTH-02 | Continuous ordinary-air contamination has no verified 1.19.2 eligible-activity hook; exact selected-state raids remain required. No estimator is retained. | unsupported for continuous route; verified for raid route | `2026-07-13_stage_0_engine_source_verification.md` |
| AUTH-03 | Doctrine may reduce Condemnation impact while evidence, attribution, and confirmed-use records remain intact. | verified by explicit user instruction | User correction, 2026-07-13. |
| AUTH-04 | Numbered spec 08 keeps chemical doctrine separate from camp/genocide infrastructure despite the compact-goal conflict. | queued migration | Spec 08 and completion checklist. |
| AUTH-05 | Medical response uses scripted capacity backed by support equipment, trucks, and field-hospital/treatment technology; no separate medical archetype is presently justified. | verified design decision | Stage 0 vanilla field-hospital review. |
| AUTH-06 | Tabun receives the complete payload/delivery role mapped by the numbered specs and delivery matrix. | in progress; exact strategic lot, class payload, profile, and aircraft rack are implemented, while active release routes remain open | Specs 04-05 and chemical-agent delivery matrix. |

## Numbered-spec traceability

### Spec 01: core system and gameplay loop

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S01-01 | National program loop covers establishment, protection, delivery, HQ preparation, use/exploitation, and aftermath. | Program decisions, equipment, HQ, delivery, response, AI, and docs all connected. | queued |
| S01-02 | Persistent national values cover Chemical Readiness, policy, military/civil protection, filters, decon, medical response, biosecurity, surveillance, containment, weaponization, attribution control, evidence, and Condemnation context. | Central constants, documented variables/flags, scripted localisation. | in progress; Stage 1 national core implemented, equipment/bio/UI values queued |
| S01-03 | State values cover chemical contamination class/intensity/duration, outbreak agent/stage/intensity, medical saturation, evidence, protection, and responsible actor memory. | State helpers and cleanup contracts. | in progress; chemical contamination/evidence ownership implemented, outbreak and persistent actor records queued |
| S01-04 | Army/order values cover selected HQ, preparation, protected posture, forecast, delivery profile, affected force, and cleanup corridor. | HQ companies/abilities and order-scoped helpers. | in progress; Stage 4 implements exact deployed-company gates, affected-force commitment, preparation, active posture, finite upkeep, and cleanup identity, while selected-state/agent/route adapters remain Stages 6 to 8 |
| S01-05 | Readiness bands gate content and are capped by milestones, equipment, and institutions rather than free accumulation. | Readiness constants/triggers, decisions, doctrine integration, UI. | queued |
| S01-06 | Choking, blister, nerve, incapacitating/malodor, and biological profiles remain mechanically distinct. | Profile constants and scenario results. | in progress; chemical profiles implemented, biological profiles and scenario results queued |
| S01-07 | Shared exposure resolves payload, conditions, protection, disruption, deaths, contamination, medical saturation, evidence, attribution, and Condemnation in one sequence. | One public chemical exposure entry point called by every route. | in progress; fail-closed calculator implemented, route migration and single dispatcher queued |
| S01-08 | Counterplay and failure states include friendly blowback, accidents, medical collapse, political rupture, and doctrine lock-in. | Effects/events/AI and tests. | queued |

### Spec 02: doctrine architecture

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S02-01 | Adoption has prerequisites and establishment cost; it does not grant broad combat-stat stacking. | Grand doctrine and balance audit. | queued |
| S02-02 | All four milestones provide functional protective, delivery, exploitation, and terminal-command unlocks. | Grand doctrine, hidden technologies, readiness caps. | queued |
| S02-03 | Four five-step tracks implement Hazard Assault, Toxic Armored Warfare, Contaminant Fire Support, and Integrated CBRN Command. | Four subdoctrine files and localisation/icons. | queued |
| S02-04 | Mastery pacing uses equipped participation and bounded doctrine progress. | On-action/effect evidence and scenario timing. | queued |
| S02-05 | Doctrine-only technologies are hidden, correctly gated, and unlock real content. | Technology and doctrine files. | queued |
| S02-06 | Officer-corps spirits and command roles are bounded, useful, and mutually exclusive where mapped. | Ideas, traits, AI, localisation. | queued |
| S02-07 | Permanent doctrine bonuses remain within the accepted power budget; temporary operations carry the stronger effects and real costs. | Balance ledger and scenarios. | queued |

### Spec 03: HQ command and regimental support

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S03-01 | Six HQ companies exist: Operations Section, Intelligence/Weather Cell, Protective Logistics, Mobile Decon, Medical Directorate, Biological Security. | `cbrn_hq_support` definitions, icons, tech, AI. | implemented and source-audited; all six definitions, unlocks, exact bills, final counters, baseline AI, and localisation are wired, while live designer/shortage scenarios remain Stage 14 |
| S03-02 | HQ companies use current 1.19 Army HQ schema, essential equipment, deployed-leader modifiers, and shortage scaling. | Definitions plus vanilla-pattern review. | implemented and source-audited against installed 1.19 HQ definitions; native essential/need scaling is used and the unsupported exact per-company fill query is disclosed without an estimator, while live designer/shortage scenarios remain Stage 14 |
| S03-03 | At least six mapped HQ abilities exist with cost, duration, cooldown, company gate, affected-force scaling, AI use, and cleanup. | Abilities/effects/triggers/scenarios. | implemented and source-audited; seven abilities use exact company/context gates, stored force-band CP and stock packages, fail-closed issued-filter affordability, bounded preparation/upkeep/cleanup, final icons, baseline AI, and honest downstream adapters, while live Stage 14 scenarios remain open |
| S03-04 | Ten regimental roles exist: masks/decon, recon, pioneer, projector, ammunition, armored delivery, suppression, epidemiology, medical, biosecurity assault. | Regimental unit file, designer visibility, tech, icons, AI. | implemented and source-audited; all ten role families, three armored chassis variants, final art, localisation, and baseline AI are wired |
| S03-05 | Regimental roles occupy the regimental row and do not masquerade as ordinary support. | Unit definitions and designer inspection. | implemented; all definitions use the 1.19 regimental-support group/category contract |
| S03-06 | Essential-equipment shortage removes or scales powerful scripted benefits. | `essential`, `need`, scripted gates, shortage scenario. | in progress; native standing-equipment shortage scaling is implemented, operation-level payload bands remain Stage 6 |

### Spec 04: equipment, technologies, and subunits

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S04-01 | Four producible gas-mask models provide progression from basic mask to sealed set. | Equipment, tech, enum, art, localisation, production AI. | verified; Stage 2 equipment, model progression, art, localisation, and differentiated production AI are committed in `cc72b1239` |
| S04-02 | Producible decontamination equipment and CBRN instruments support HQ and regimental roles. | Equipment, enum, needs, AI. | implemented for standing HQ/regimental bills and model-aware operation consumption; final live supply scenarios remain Stage 14 |
| S04-03 | Strategic payload, shell lots, armored-delivery stores, and air-payload lots are real consumable equipment where mapped. | Equipment and route consumption. | in progress; exact strategic-agent, shell-lot, armored-store, and four air-payload-class equipment plus conversion/debit/reservation helpers are implemented, while all active route consumers remain open |
| S04-04 | Biological payloads remain agent-specific and stockpile safety uses actual stock. | Equipment, projects, accidents, raids/operations. | queued |
| S04-05 | Protective, detection/forecast, decon, delivery, medical, and biosecurity technology branches are complete and AI-aware. | Tech tree, AI, GFX, localisation. | in progress; protective equipment and Stage 3 support unlocks are wired, later delivery/medical/bio lifecycle integration remains |
| S04-06 | Every agent technology unlocks a complete payload plus a delivery or research role; no dead technology remains. | Tech/profile/delivery audit. | in progress; all nine chemical agents have exact profiles, strategic lots, and CAS/tactical racks, including the previously unreachable Tabun rack and project-gated Malodor/Behavioral racks; active route and later biological audits remain open |
| S04-07 | Standing issue, operational expenditure, and filter consumption remove real equipment and cannot duplicate stock. | Shared protection/payload helpers and exploit audit. | in progress; military/civil issue, filter loss, reconditioning, and transfers are equipment-backed, route payload expenditure remains Stage 6 |
| S04-08 | Legacy equipment and units migrate through stable identifiers or explicit compatibility wrappers; active duplicate families disappear. | Migration section below and search audit. | in progress; consolidated supports are active and legacy IDs remain parse-safe, route adapters and final duplicate retirement remain Stage 6 |
| S04-09 | All new equipment is registered in `script_enum_equipment_bonus_type`. | Enum evidence. | implemented; Stage 2 equipment bonus types and Stage 3 production categories are registered |

### Spec 05: chemical delivery and battlefield effects

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S05-01 | General cylinders, projector battery, artillery, armored delivery, air interdiction/raid, strategic raid, and covert operation all call shared exposure. | Call-site audit with no independent consequence calculator. | queued |
| S05-02 | Each route preserves its identity through preparation, affected-force model, cost, reliability, evidence, and contamination profile. | Route adapters and matrix-aligned constants. | queued |
| S05-03 | Chemical artillery consumes shell lots and supports choking, persistent blister, nerve shock, and incapacitating plans. | Decisions/abilities/effects/equipment. | queued |
| S05-04 | Armored delivery consumes payload, requires sealed/protective equipment, and is not parachute-capable. | Unit/effect audit. | queued |
| S05-05 | Chemical air raids consume payload and contaminate the selected state; continuous-air estimator is removed. | Raid and old-estimator search evidence. | in progress; the estimator is removed, native 120-unit class reservation and five outcome bands are implemented, and no-release outcomes have exact evidence/Condemnation accounting; release-bearing raids remain fail-closed pending accepted condition inputs |
| S05-06 | First-use shock is defender adaptation memory, not a permanent attacker buff. | Flags/modifiers/events and repeat-use scenario. | queued |
| S05-07 | Weather, terrain, target posture, masks, filters, decon, medical response, and friendly blowback affect resolution. | Shared exposure inputs and scenarios. | queued |
| S05-08 | Immediate/continuing civilian deaths and military disruption are bounded and protection-sensitive. | Death adapters and balance scenarios. | queued |

### Spec 06: biological warfare and outbreaks

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S06-01 | Anthrax, plague, tularemia, and smallpox have distinct incubation, detection, spread, lethality, treatment, and persistence. | Agent profiles and four lifecycle scenarios. | queued |
| S06-02 | Weaponized zombies remain separate except for deliberately shared safety/evidence/death helpers. | Boundary call-site audit. | queued |
| S06-03 | Development choices, facilities, stockpile production, weaponization quality, safety, and accidents are connected. | Projects/equipment/effects/events/decisions. | queued |
| S06-04 | Strategic raid, operative planting, battlefield dissemination, sabotage, and historically specific campaign actions preserve route identity and agent lifecycle. | Delivery adapters and tests. | in progress; strategic raids, four operative releases, four native exact-state battlefield land raids, four exact-state food/water/medical sabotage decisions, and two Japan–China exact-state campaign decisions preserve route identity and enter the ordinary lifecycle; final cross-route package scenarios remain open |
| S06-05 | Incubation can remain hidden; detection reveals stage without leaking exact hidden values in final text. | Scheduler, flags, scripted localisation. | queued |
| S06-06 | Spread uses targeted self-scheduling/neighbor jobs, not a broad all-country pulse. | On-action and event audit. | queued |
| S06-07 | Surveillance, quarantine, hospitals, antibiotics, vaccination, border closure, and international medical missions have distinct costs/effects. | Decisions/missions/countermeasure matrix/AI. | implemented and source-audited; exact costs, commitments, provider/cycle ownership, agent-specific treatment, bounded border cleanup, international access, route-aware AI, final localisation, and type-correct assets are wired, while final cross-route Stage 7 package scenarios remain open |
| S06-08 | Captured facilities and samples create evidence, attribution, and accident risk. | State/facility effects and events. | implemented and source-audited; exact mixed-producer payload debit, state/controller ledgers, targeted accidents, native recovery raids, assigned-HQ/BSA requirements, evidence, attribution, AI, final icons, localisation, and documentation are wired, while the actor-controlled enemy-owned native target scenario remains Stage 14 |
| S06-09 | Doomsday release consumes stockpile and records deaths, outbreaks, evidence, Air Cleanliness, and Condemnation once. | Shared record and double-count audit. | queued |

### Spec 07: gas masks and civil defence

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S07-01 | Military coverage uses issued mask crates, protective clothing/model, filters, training, warning, and medical support. | Coverage helper and division/HQ issue model. | in progress; real military issue/model/filter inputs, division needs, HQ protective posture costs, filter wear, and medical commitments are wired, while final exposure-specific HQ protection is integrated with route migration |
| S07-02 | Civilian state coverage is population-scaled and consumes crate-equivalent stock plus administration/time. | Formula constants, state decisions, stock changes. | verified; population-scaled state issue and exact stock removal are committed in `cc72b1239` |
| S07-03 | National reserve, registration/fitting, priority-city issue, full distribution, alert distribution, replacement, reconditioning, occupation supply, and exports exist. | Decision family and AI. | implemented; Stage 2 decision families and AI cover the mapped reserve/distribution lifecycle |
| S07-04 | Emergency issue wastes stock; collection/reconditioning cannot create infinite masks. | Constants and exploit scenario. | verified; waste/recovery bounds and raw-versus-effective distribution accounting were audited in Stage 2 |
| S07-05 | Filter storage loss, alert use, exposure use, and civilian consumption require replacement. | Targeted scheduler/exposure calls and stock ledger. | implemented; loss and replacement are targeted/self-scheduled with exposure consumption routed through shared protection helpers |
| S07-06 | Starting stock follows the accepted matrix, Britain is strongest, and all totals are documented as gameplay tuning with honest confidence. | Startup constants/effects and docs. | verified; thirty differentiated profiles are committed, with Britain strongest at 45,000 crates and confidence disclosed as gameplay tuning |
| S07-07 | Mask protection reduces every chemical death path, including suppression and continuing contamination. | Shared protection dependency audit. | in progress; shared exposure consumes applied protection, remaining legacy/suppression/continuing route migration belongs to Stages 6, 8, and 9 |
| S07-08 | Protective posture has a real tempo/opportunity cost. | HQ ability/unit modifiers and scenario. | implemented in source through force-band CP, masks, filter wear, support upkeep, supply burden, -5% movement, and -3% attack; Stage 14 live scenario remains open |

### Spec 08: suppression, occupation, and nerve agents

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S08-01 | Nerve Suppression is a targeted, temporary occupation decision requiring advanced agent, protection, and equipment. | Decision/trigger/effect. | queued |
| S08-02 | It consumes payload and creates suppression, deaths, contamination, medical saturation, evidence, resistance trauma, and severe Condemnation. | Shared exposure/action record and delayed effects. | queued |
| S08-03 | Radicalisation memory, neighboring spillover, liberation discovery, and coverup/inspection choices persist after immediate suppression. | State/country flags, jobs, events. | queued |
| S08-04 | CBRN Coercive Security and Protected Occupation Administration remain bounded policies with counterplay. | Occupation law/decisions and AI. | queued |
| S08-05 | Doctrine does not unlock genocide infrastructure; camp/genocide systems remain independent. | Removal/migration audit. | queued |

### Spec 09: shared consequences and diplomacy

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S09-01 | One unified action record owns actor, victim, target state, route, agent, payload, exposure, deaths, contamination, evidence, attribution, and consequence context. | Documented helper contract and call-site audit. | in progress; action contract implemented, live call-site audit queued |
| S09-02 | Deaths use shared tracker, valid population caps, source labels, and continuing-death aggregation without duplicate registration. | Chaos Meter adapter and tests. | queued |
| S09-03 | Air Cleanliness receives contamination-class contributions once, including biological contribution where mapped. | Adapter and dirty-file-safe integration. | queued |
| S09-04 | Chemical, biological, atrocity, and coverup Condemnation buckets remain distinct. | Source adapters/constants/UI. | queued |
| S09-05 | Attribution progresses from latent through suspected/probable/confirmed; delayed confirmation does not double-charge. | Evidence ledger and events. | queued |
| S09-06 | Confirmed use retains a floor; retaliation and doctrine mitigation modify impact according to accepted rules. | Condemnation calculation and scenarios. | in progress; calculator and floors implemented, live consequence scenarios queued |
| S09-07 | Inspection demand, protective aid, retaliation policy, arms embargo, humanitarian carve-out, evidence sharing, decon mission, and ally shielding exist. | Decisions/events/AI/localisation. | queued |
| S09-08 | Sanctions affect practical CBRN production/import/support while humanitarian aid can exempt defensive goods. | Condemnation/sanctions integration. | queued |
| S09-09 | Cleanup removes stale scopes, targets, flags, arrays, and temporary operation state. | Cleanup helper and long-chain scenarios. | queued |

### Spec 10: AI, country programs, and designers

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S10-01 | Five AI postures exist: Civil Defence, Retaliatory Arsenal, Battlefield Chemical Army, Strategic CBRN Power, Desperate Release. | Profile flags/triggers/strategy. | queued |
| S10-02 | AI protects before attacking and has research, production, template, HQ, operation, containment, and sanction behavior. | AI files and scenario records. | queued |
| S10-03 | AI target scoring accounts for war state, strategic value, protection, weather, retaliation, evidence, stock, safety, and self-harm. | Scoring helpers and route tests. | queued |
| S10-04 | Britain, France, Germany, USSR, USA, Italy, Japan, and the four defensive European profiles start differently. | Startup profiles, reserves, tech, AI. | queued |
| S10-05 | Minor countries can access viable defensive CBRN content without offensive overinvestment. | Minor profiles and three scenarios. | queued |
| S10-06 | Six designer families exist and use current MIO schema; country assignments are differentiated. | MIO definitions, AI selection, icons/loc. | in progress; Chemical Munitions Combine and Aerosol and Air Delivery Bureau use the verified 1.19 MIO schema, exact custom payload archetypes, completed-trait queries, bounded scripted effects, differentiated baseline AI weights, final localisation, and independent wired icons. Four families, country-specific assignments, live AI selection, and the two disclosed unsupported/proxy airframe directions remain unresolved. |
| S10-07 | Seven major and at least three minor AI validation profiles are recorded. | Stage 14 report. | queued |

### Spec 11: balance, consistency, and validation

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S11-01 | Remove empty milestones, broad stat stacks, active duplicate unit families, universal Chaos Battalion arsenal, free air effects, tech-only masks, identical stockpiles, AI-disabled mechanics, placeholders, airborne chemical tanks, and mixed Tabun support. | Search/diff audit. | queued |
| S11-02 | Permanent, temporary, friendly-penalty, command-power, equipment, and reserve budgets remain inside the specified bands. | Central constants and balance report. | queued |
| S11-03 | Death, contamination, and Condemnation safeguards cap pathological outcomes without hiding real consequences. | Scenario outcomes and shared helpers. | queued |
| S11-04 | Exploit audit covers token support, disabled equipment, template switching, mask recycling, payload duplication, repeated deaths, concealment, garrison abuse, and air estimation. | Stage 13-14 report. | queued |
| S11-05 | No new broad all-country periodic pulse is introduced. | On-action audit. | queued |
| S11-06 | Ten required scenarios run at weak, normal, and high-chaos settings with costs, deaths, contamination, cleanup, Condemnation, sanctions, and AI decisions recorded. | Stage 14 report. | queued |

### Spec 12: UI, localisation, assets, and achievements

| ID | Accepted requirement | Required evidence | Status |
| --- | --- | --- | --- |
| S12-01 | CBRN interface has Arsenal, Protection, Operations, Contamination, and International Response views and all specified interface states. | GUI/GFX/scripted GUI/render review. | queued |
| S12-02 | Dynamic values and requirements are readable, with no hidden incubation or attribution data leaked. | Scripted localisation and localisation audit. | queued |
| S12-03 | Five decision-category families remain discoverable and hide irrelevant content. | Categories/decisions/UI audit. | queued |
| S12-04 | Final player text follows doctrine, chemical, biological, civil-defence, and Condemnation direction and contains no implementation-history wording. | Localisation audit. | queued |
| S12-05 | Every doctrine, technology, unit, equipment, decision, category/UI, state modifier, designer, report/news, and achievement asset in the asset plan has a type-correct final workflow. | Source PNG, processed PNG, DDS, manifest, GFX, wiring. | queued |
| S12-06 | Animated readiness seal, contamination border, and operation preparation indicator use real source frames, static fallback, contact sheet, preview, and handoff. | Frame-animation package. | queued |
| S12-07 | All fifteen named achievements, tracking, localisation, icons, and anti-exploit conditions exist. | Achievement file/GFX/loc/scenarios. | queued |
| S12-08 | Mechanics guide and system docs reflect final behavior; old plans/docs are dispositioned. | Documentation audit. | queued |

## Matrix obligations

| Matrix | Non-negotiable implementation use | Status |
| --- | --- | --- |
| `doctrine_and_tech_matrix.md` | Gates, burden, unlocks, permanent/operational targets, risks, dates, and consistency gates drive doctrine/tech definitions. | queued |
| `hq_and_ability_matrix.md` | Exact six HQ companies and ability gates/cost/duration/cooldown/equipment/AI mapping. | implemented and source-audited; definitions, seven abilities, strict capstone composition, costs, durations, cooldowns, equipment, exact filter/manpower commitments, final assets, and baseline AI are wired, while live Stage 14 scenarios remain open |
| `regimental_support_matrix.md` | Exact ten division-layer roles, grouping, incompatibilities, and role identity. | implemented and source-audited; consolidated and retained compatibility definitions share the required exclusions |
| `subunit_equipment_matrix.md` | Essential/secondary equipment and shortage behavior for every HQ/regimental/line role. | implemented in source for HQ, regimental, and Chaos Assault standing bills with native essential/need shortage scaling; live designer/shortage scenarios remain Stage 14 |
| `chemical_agent_delivery_matrix.md` | Agent-by-route eligibility, payload class, persistence, evidence, and target effects; no invented delivery support. | in progress; exact chemical profiles, payload classes, aircraft-rack eligibility, reservation bands, and failed-attempt evidence are implemented, while matrix-mapped active ground/air routes and scenario proof remain open |
| `biological_agent_countermeasure_matrix.md` | Agent properties and countermeasure effectiveness/tradeoffs. | queued |
| `gas_mask_starting_stockpile_matrix.md` | Country bands, Britain strongest, population conversion, confidence notes, no identical major bundles. | verified; Stage 2 uses all thirty profiles and records the tuning/confidence rationale |
| `contamination_deaths_condemnation_balance_matrix.md` | Route/agent base bands and multipliers feed central constants and scenario expectations. | in progress; Stage 1 chemical profiles centralized, scenario validation queued |
| `country_program_and_designer_matrix.md` | Country posture, start package, research, production, use policy, and designer assignment. | in progress; the two Stage 6 offensive designer families and baseline country/profile preferences are present. Protective, decontamination, biological, and medical families, country-specific assignments, full posture integration, and exact resolution of module-specific weight/agility/range directions remain open. |
| `ai_behavior_matrix.md` | Trigger/action/stop conditions for production, HQ, operations, response, sanctions, and safety. | queued |

## Specialist-prompt gates

| Prompt | Required disposition | Status |
| --- | --- | --- |
| `chaos_warfare_coding_prompt.md` | Governs implementation order, centralization, migration, shared pipeline, unsupported behavior reporting, validation, and completion claim. | in progress |
| `chaos_warfare_decision_mission_prompt.md` | Every decision/mission has exact target, real costs, cancellation/cleanup, AI, tooltips, and exploit controls. | queued |
| `chaos_warfare_asset_prompt.md` | Register stable identifiers before production; no placeholder or cross-type substitute; manifest and wiring required. | in progress overall; Stage 2 and Stage 3 packages are complete, type-correct, manifested, visually reviewed, and wired; later-stage assets remain |
| `chaos_warfare_achievement_prompt.md` | Implement and verify all named achievements, tracking, icons, localisation, and anti-cheese gates. | queued |
| `chaos_warfare_goal_prompt.md` | Final audit checks the full objective, unsupported behavior, changed files, validation, engine limits, and every omission. | in progress |

## Stage 1 ownership and adapter boundaries

The CBRN core owns action-record preparation, payload debit, exposure calculation, protection calculation, route-independent consequence values, and cleanup. It must reuse the existing cross-system public adapters rather than clone their internal ledgers:

| Existing adapter | CBRN responsibility | Boundary rule |
| --- | --- | --- |
| `chem_warfare_register_attack_use` | Submit one chemical-use record after exposure resolution. | Keep legacy confirmed-use and first-use history intact; do not create a second country-level use ledger. |
| `bio_register_condemnation_source` | Submit one biological consequence source when attribution rules permit it. | Biological lifecycle code owns incubation and spread; the adapter receives the final source value only once. |
| `chaos_meter_register_state_civilian_deaths_percent` | Register immediate or continuing civilian deaths with the shared tracker. | State contamination mutation must not register the same death interval independently. |
| `air_contamination_apply_delta_bp` | Apply the resolved chemical or biological Air Cleanliness contribution once. | CBRN supplies class/source context and a bounded delta; it does not fork the Air Cleanliness ledger. |
| `condemnation_add_source` | Add the resolved chemical, biological, atrocity, or coverup source. | Doctrine may mitigate impact under AUTH-03, but evidence, attribution, and confirmed-use memory are not erased. |

New Stage 1 code ownership is intentionally UI-independent:

| File | Owned contract | Status |
| --- | --- | --- |
| `common/script_constants/cbrn_system_constants.txt` | Shared fixed-point profile, protection, evidence, attribution, cleanup, and scheduler tuning. | implemented |
| `common/scripted_effects/cbrn_exposure_effects.txt` | Public chemical action-record/exposure calculator and validation, with later route adapters and consequence dispatch. | implemented for Stage 1 calculator/validator; adapters and dispatch queued |
| `common/scripted_effects/cbrn_protection_effects.txt` | National initialization/readiness/policy and bounded layered protection outputs; later equipment helpers provide real coverage inputs. | implemented for Stage 1 core; equipment integration queued |
| `common/scripted_effects/cbrn_hq_effects.txt` | Army/order preparation state contracts; initially helper-only until HQ content is added. | implemented for Stage 4 activation, committed force band, real stock/filter/capacity/manpower debit, finite upkeep, and cleanup; payload/state consequence dispatch remains later-stage-owned |
| `common/scripted_triggers/cbrn_triggers.txt` | Readiness, policy, protection, payload, attribution, and valid-target gates. | implemented |
| `common/scripted_effects/chaosx_dynamic_effects.md` | Public helper documentation: scope, inputs, outputs, defaults, side effects, cleanup, and examples. | implemented for Stage 1 helpers |

Legacy public identifiers remain available until every internal and external caller is migrated. Compatibility wrappers may translate old arguments into the shared record, but they may not retain an independent exposure, death, contamination, evidence, or Condemnation calculator.

## Legacy migration ledger

| Legacy surface | Current issue | Required migration | Status |
| --- | --- | --- | --- |
| `chemical_chlorine_attack`, `chemical_phosgene_attack`, `chemical_mustard_attack`, `chemical_lewisite_attack` | General-wide abilities with route-specific duplicated resolution. | Compatibility-visible wrappers or replacement HQ abilities feeding shared exposure; no independent consequence path. | queued |
| `livens_projector_support_*` agent variants | Agent-by-agent support duplication and inferred payload use. | One profile-driven Chemical Projector Battery; hide legacy variants and migrate templates safely. | in progress; consolidated battery is active and legacy tech unlocks are removed, old route callers remain for Stage 6 migration |
| light/medium/heavy `chemical_tank_support_*` variants | Eighteen active variants, inferred consumption, parachute eligibility. | One Armored Chemical Delivery role/profile family with essential equipment and no parachute use; compatibility migration. | in progress; three chassis variants share one role/profile family and cannot parachute, old route callers remain for Stage 6 migration |
| `chaos_battalion` | Universal arsenal gate, abusive stats, random outbreak behavior without proper payload accounting. | Coherent Chaos Assault Battalion with doctrine-only tech, bounded role, essential equipment, and shared delivery calls. | in progress; bounded equipment-backed battalion is implemented and passive release callers are disconnected, final doctrine/route migration remains |
| `chem_apply_state_contamination` and per-route death calls | Contamination application can register deaths repeatedly. | Split state contamination mutation from one-time and continuing death records. | queued |
| `chem_air_bomb_weekly_tick`, `chemical_air_bomb.1`, `chem_air_ground_ops_heat` | Unsupported mission estimator can contaminate from idle aircraft. | Remove estimator hooks/flags/event; exact-state raids only. | verified; combat hooks and estimator effects/constants are removed, while the stable event ID only clears legacy state and cannot reschedule or expose a target |
| `apply_*_contamination` immediate bio paths | No incubation/detection and immediate death registration. | Migrate valid exact routes to the shared lifecycle; remove random, passive, or abstract callers that cannot prove the full release record; retain no permissive wrapper. | verified; valid exact routes use lifecycle adapters, invalid UWR focus, passive Chaos Assault Battalion, abstract camp, obsolete event, and legacy maintenance callers are removed, and no `apply_*_contamination` identifier remains |
| `on_weekly` biological maintenance | Broad all-country pulse forbidden. | Outbreak-owned self-scheduling and explicit cleanup. | queued |
| `concentration_occupation_law_unlocked` | Doctrine-linked genocide infrastructure conflict. | Remove doctrine grant and migrate law/content ownership to independent camp/genocide systems. | queued |
| `basic_gas_masks`/`improved_gas_masks`/`advanced_gas_masks` | Technology-only protection. | Technologies unlock model progression; actual coverage uses produced/issued equipment. | verified; technology unlocks producible models and shared protection reads real issued stock/model snapshots |
| startup identical cylinder bundles | Weak country differentiation and no real mask reserves. | Matrix-driven country profiles and gas-mask crate reserves through startup helper/constants. | verified for mask reserves; differentiated chemical payload starts remain Stage 10 |
| placeholder/under-development asset and text entries | Invalid final deliverables. | Stable identifiers, type-correct production, final text, manifest, GFX wiring. | in progress; Stage 2 is complete and Stage 3 runtime art/final text are wired, later-system assets remain |

## Stage and commit gates

| Stage | Exit evidence | Status |
| --- | --- | --- |
| 0 | Engine/source note, exact-air result, no gameplay edit. | verified; commit `938738e6` |
| 1 | Constants, persistent-state ownership, documented helper contracts, migration plan, no UI dependency. | implemented; static contract audit passed, live integration belongs to later stages |
| 2 | Producible protection equipment, technology, issue/coverage/filter/distribution/start-reserve system; all existing chemical routes honor it. | implemented and audited; commit `cc72b1239` |
| 3 | Consolidated regimental roles and Chaos Assault Battalion; legacy compatibility and template AI. | implemented and source-audited; final rendered/live package scenarios remain Stage 14 and are not yet claimed |
| 4 | Six HQ companies and mapped abilities with costs, duration, cooldown, shortage, AI, cleanup. | implemented and source-audited; gameplay, AI, final assets, localisation, docs, exact operating lifecycle, and the follow-up filter-affordability audit are complete, while live scenarios remain Stage 14 |
| 5 | Doctrine, milestones, four tracks, hidden tech, officer corps, traits, icons, localisation, balance audit. | queued |
| 6 | All chemical delivery routes migrated to shared exposure; exact-state raids; no continuous estimator. | queued |
| 7 | Distinct biological lifecycle, operations, accidents, facilities, countermeasures, evidence; zombie boundary. | queued |
| 8 | Unified deaths/Air Cleanliness/Condemnation/diplomacy record and double-count audit. | queued |
| 9 | Nerve suppression and occupation policies with delayed trauma/discovery and camp separation. | queued |
| 10 | Route-aware AI, differentiated programs/reserves/designers, major/minor scenarios. | queued |
| 11 | Final UI/localisation/assets with no placeholders. | queued |
| 12 | Fifteen achievements and complete documentation. | queued |
| 13 | Script architecture, decision, localisation, country, completion, and improvement-loop audits resolved. | queued |
| 14 | Thirty balance runs plus AI profile runs recorded; no undisclosed simplification. | queued |

## Completion rule

This ledger is not proof by itself. Completion requires each row's repository/runtime/audit evidence, every package checklist item, every accepted specialist finding, and a final omission report. Unsupported continuous ordinary-air contamination remains disclosed; no estimator or weaker substitute may be introduced without explicit approval.
