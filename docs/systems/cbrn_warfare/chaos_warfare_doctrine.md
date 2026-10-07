# Chaos Warfare doctrine, institutions, and officer corps

> **Authority:** The user-approved [2026-09-20 CBRN amendment](../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md) governs the three-policy, three-HQ design and combined bonus ceilings. This document describes the current doctrine source; the [implementation ledger](../../plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md) tracks wider package validation. Source evidence below does not establish live-game behavior.

## Current source arithmetic and validation limit

The accepted 2026-09-20 ceilings apply to combined legal sources, not to each trait independently. The parent and technology owner retuned doctrine, spirits, High Command, and technology after the first audit. The completion auditor then recomputed strict all-independent upper bounds for separately legal scenarios; the table gives source arithmetic, not the engine's final stat formula. Controlled Retaliation, Theater Contamination, and Terminal Hazard share one `army_spirit` slot; Mask Discipline and Hazard Assault Cadres share one `division_command_spirit` slot. No effective-cap or engine acceptance is claimed here.

| Endpoint and legal posture | Independent-source budget bound | Accepted ceiling |
| --- | ---: | ---: |
| Army attack with Terminal | +4.0375% | +5% |
| Army organisation with Controlled Retaliation and Mask Discipline | +4.5807% | +5% |
| Planning with Theater | +14.7368% | +15% |
| Coordination with Terminal | +7.7496% | +8% |
| Reinforcement | +2 percentage points | +2 percentage points |
| Line/support artillery doctrine soft attack; with legal global attack | +9.5000%; +13.9211% | +10% doctrine; +15% conventional |
| Projector soft/hard/defense/breakthrough/organisation | +32.8602% / +32.8455% / +34.7559% / +34.5832% / +33.6309% | +35% dedicated static each |
| Armored delivery soft/hard/defense/breakthrough/organisation | +26.4582% / +4.0375% / +24.5894% / +24.5894% / +26.3683% | +35% dedicated static each |
| Chaos Battalion soft/defense/breakthrough/organisation | +20.1633% / +12.7500% / +34.8490% / +33.3404% | +35% dedicated static each |
| Protection Company nominal attack/defense | +14.4413% / +12.7500% | +35% dedicated static each |
| CBRN reconnaissance utility from hidden weather technologies | +30% on base 4 | +35% dedicated static |

The [October 7 source audit](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-07_doctrine_reward_budget_source_checks.md) resolves actual category membership and tests all thirteen retained roles under pooled identical-stat and independent-layer models.
Its 137 checks reproduce the overlapping armored organization and conservative breakthrough failures in the captured baseline, then place all sixty-five revised role/stat rows within their source budgets.
Chaos Battalion receives one 15% mastery III breakthrough grant, four percent from its advanced doctrine technology, and eleven flat organization points on base forty.
The conservative breakthrough bound reserves the possible 10% Cadres defense/breakthrough factor and 2.5% CBRN-earned defense skill, reaching +34.849%.
Each of the two projector upgrades grants 2.5% soft attack, 13% hard attack, 4% defense and 6.5% breakthrough.
Only Projector and the three armored delivery variants belong to the retained chemical-support category; Protection Company and HQs are not members.
Projector receives Fire Support's five organization points, while armor receives only its own five, avoiding the ten-point overlap on base twenty-four.
The generic radio/radar and ordinary vanilla progression are equal-baseline sources, not selectively removed from one side.
These source bounds include the possible commander defense-skill layer but do not prove native modifier accumulation, actual division statistics or campaign mastery pacing.
The unchanged conditional hazard endpoint scenarios below retain their separate country and spirit-slot limits.

| Conditional endpoint | Largest source stack in a separate country- and spirit-slot-legal scenario | Source arithmetic |
| --- | --- | ---: |
| Choking artillery dose | Fire support 1.04 × Integrated Command 1.04 × Terminal Hazard 1.05 × stable-choking MIO 1.03 × one chemical advisor 1.03 | 1.204843 × base |
| Chemical air dose | Fire support 1.04 × Integrated Command 1.04 × air link 1.02 × Terminal Hazard 1.05 × one chemical advisor 1.03 | 1.193145 × base |
| Choking contamination | Choking artillery dose 1.204843 × three 1.03 contamination factors × one advisor factor 1.02 | 1.342896 × base |
| Blister contamination | Base doctrine dose 1.04² × Terminal Hazard dose 1.05 × one advisor dose 1.03 × three 1.03 contamination factors × one advisor contamination 1.02 × persistent MIO 1.02 | 1.329858 × base |
| Air or blister duration | Fire support 1.03 × Integrated Command 1.03 × air link 1.10 × Terminal Hazard 1.10 × persistent MIO 1.15 | 1.476242 × base |
| Soviet toxicological casualty pressure | Choking artillery dose 1.204843 × Terminal Hazard casualty factor 1.10 × toxicological director 1.05 | 1.391594 × base |
| Japanese or American biological seed potency | Terminal Hazard 1.20 × Integrated Command 1.10 × strategic-dissemination MIO 1.02 × two compatible advisors 1.02² | 1.400795 × base |
| Exact-state cleanup output | Theater Contamination 1.10 × low-water MIO 1.15 × rapid-route MIO 1.15 | 1.454750 × base |

The earlier doctrine handoff's 1.03² chemical-advisor and 1.02⁵ biological-advisor products pooled country-locked appointments from different countries and are superseded for legal scenario maxima. `common/characters/cbrn_historical_specialists.txt` permits the chemical theorist only for GER and toxicological director only for SOV; the largest biological actor combinations have two compatible potency appointments, in JAP or USA after their date gates. `common/script_constants/cbrn_historical_advisor_constants.txt` and `common/scripted_effects/cbrn_historical_advisor_effects.txt` define and apply their factors. The choking and blister rows are separate endpoint scenarios: Stable Choking Fill affects choking artillery dose, while Persistent Agent Formulation affects blister contamination and duration. Persistent Agent Formulation is a descendant of Stable Choking Fill in `common/military_industrial_organization/organizations/cbrn_delivery_organizations.txt`; they are not mutually exclusive. The chemical-readiness generation maximum from one eligible advisor is 1.20, not the old 1.20². The core owner removed the orphan `cbrn_doctrine_advisor` planning/organisation constant blocks; their former values are not active bonuses. Conditional scenario and revised static technology source arithmetic are bounded as shown, while probability, MCP, and engine checks remain open.

These source-arithmetic bounds are separate scenario calculations, not a claim that all listed bonuses coexist or that the engine applies their product exactly. The parent retains final balance review and the user retains live-game validation.

The [same-mask hazard correction](../../specs/chaos_warfare_system_specs/corrections/2026-09-27_same_mask_hazard_budget.md) addresses a separate conditional ceiling: with 89% sealed-mask issue, full field kits and medical capacity previously improved choking casualties from the same-mask 0.25 to 0.06. The full chemical path now floors added protection and treatment at half the current actual-mask casualty result, including military deaths, civilian deaths, and medical saturation. Issued masks remain foundational, and missing or worn equipment still weakens that baseline. The 1.495 cleanup source product in the table is unchanged. Native exposure and project-selection evidence remains open.

## Purpose

Chaos Warfare is a conditional CBRN grand doctrine. Adoption establishes the national command immediately; subsequent mastery and technology gates grant formation, headquarters, logistics, and operation eligibility without a second establishment mission. Actual chemical delivery remains equipment-backed and must use the shared exposure pipeline.

Doctrine may reduce the Condemnation impact of an accepted chemical or biological use. That reduction affects Condemnation only. It never discounts payload consumption, evidence, attribution, deaths, contamination, medical saturation, resistance trauma, domestic war-support penalties, use counters, confirmed-use history, or strategic and mass-casualty public-harm floors.

The implementation is split across:

- `common/doctrines/` for the grand doctrine and four mastery tracks
- `common/script_constants/cbrn_doctrine_constants.txt` for shared gameplay tuning, with the existing `chem_integrated_operations.condemnation_mult` table retained as the single migration-safe 0.75/0.55/0.35 Condemnation ladder for chemical and biological callers
- `common/scripted_triggers/cbrn_doctrine_triggers.txt` and `common/scripted_effects/cbrn_doctrine_effects.txt` for reusable gates and state changes
- `common/decisions/cbrn_doctrine_decisions.txt` for the three use-policy choices and exact-state cleanup
- `common/ideas/cbw_spirits.txt`, `common/ideas/cbrn_high_command.txt`, and the leader-trait files for officer-corps content
- `interface/cbrn_doctrine.gfx` and `interface/chaosx_traits.gfx` for final runtime assets.

## Adoption and command establishment

Chaos Warfare is visible to every country but available only when at least one accepted capability route exists:

- Basic Gas Masks plus a supported chemical-agent technology
- a completed mapped chemical special project
- an established CBRN command flag
- a mapped historical CBRN program profile
- an explicit scenario override.

Adoption costs 100 Army Experience. `cbrn_chaos_warfare_adopt` initializes country data, records program, command, adoption, and establishment-complete flags, clears the retired pending/failure/closed-authority flags and obsolete occupation-law unlock, stores a mask-production baseline and peak use policy, unlocks the Operations and Intelligence HQ section plus the Gas Mask and Decontamination Detachment, and reconciles eligible doctrine capabilities. The source neither starts an establishment mission nor buys or sets a readiness amount; `cbrn_doctrine_raise_readiness_to_minimum` currently refreshes the country mask snapshot.

`cbrn_chaos_warfare_establishment_requirements_met` remains a compatibility-named trigger for Event 027 selectors, but it now means doctrine-held research capability. It does not test an equipment reserve or fielded formation. No establishment timeout, paid remediation, or readiness purchase appears in the current doctrine decision file.

## Reward timing and mastery contributors

The [accepted reward correction](../../specs/chaos_warfare_system_specs/corrections/2026-10-07_doctrine_reward_mastery.md) supplies immediate Protection Company reliability and a substantial fifteen-percent assault breakthrough reward alongside the existing conditional battalion unlock.
Armored delivery receives its five-percent breakthrough allowance on adoption and fifteen-percent track reliability at mastery I.
Line/support artillery receive their nine-and-a-half-percent doctrine soft-attack allowance on fire-support adoption, and Integrated Command receives its twenty-five-percent reconnaissance allowance on adoption.
Relocated fragments are removed rather than added a second time.
The existing reward IDs, costs, thresholds, multipliers, effect calls and deployment prerequisites remain intact.

| Track | Contributor roster |
| --- | --- |
| Protected assault | Protection Company, chemical reconnaissance, Field Medical, Biosecurity Assault, Chaos Battalion |
| Sustained fire support | Projector Battery, ammunition train, Field Medical |
| Specialized armored delivery | Light, medium and heavy armored delivery |
| Integrated command | Operations HQ, Protection HQ, Medical HQ, Protection Company, chemical reconnaissance, Field Medical |

The native lists cover all thirteen retained roles; a unit appears once within each track.
The three armored entries are its retained chassis variants, not an engine-wide contributor cap.
Additional eligible manpower can increase mastery gain, with the original multiplier retained so existing formations keep their rate.
Compatibility flags with no runtime consumer do not create an independent movement, mask-use or exploitation reward.

## Institutional milestones

Native grand-doctrine milestone blocks record their corresponding completed tracks. The cross-track country flags are reconciled by `cbrn_reconcile_doctrine_capabilities` when adoption or relevant mastery and technology-grant helpers run; the current doctrine decision file has no milestone claim cards.

| Institution | Exact proof | Result |
| --- | --- | --- |
| Protective Foundation | Chaos Warfare held; Basic Gas Masks researched; flag not yet claimed | Records the flag, raises decontamination capacity to at least the configured foundation minimum, and unlocks Operations and Intelligence HQ plus Chemical Recon Detachment. |
| Delivery Integration | Protective Foundation; any of Hazard Assault, Contaminant Fire, or Toxic Armor at mastery 2; flag not yet claimed | Records the integration flag. |
| Theater Exploitation | Delivery Integration; any two distinct tracks at mastery 3; flag not yet claimed | Records the theater flag, which exposes the exact-state cleanup decision subject to its separate gates. |
| Terminal CBRN Command | Theater Exploitation; all four tracks active; any track at mastery 5; advanced gas masks, sealed assault protection, or the explicit equivalent-project flag; flag not yet claimed | Records the terminal flag, which gates the Theater CBRN Headquarters technology grant and Unrestricted Authorization choice. |

The current milestone predicates do not require post-adoption mask production, a live 500-mask reserve, a fielded HQ, a completed protective order, payload reserve, decontamination capacity 40, or a policy level. Those older proofs survive in some helper names and historical descriptions but are not part of the four current claim triggers. No separate readiness cap or minimum is applied by these four claim effects.

## Mastery tracks

Each track costs 100 Army Experience. Native mastery comes from fielded mapped units and uses the current doctrine system. Track adoption and mastery provide deliberately strong combat, protection, logistics, and command returns, while live-agent outcomes remain operation-, stock-, readiness-, and policy-gated.

| Compatibility ID | Player-facing track | Mastery content |
| --- | --- | --- |
| `extermination_columns` | Hazard Assault Formations | Mask Discipline; contaminated-terrain movement; the retained `hazard_pioneer_formation` protection upgrade at mastery 2; Chaos Assault Battalion qualification; shock exploitation; terminal hazard-operation eligibility. |
| `chemical_suppression` | Toxic Armored Warfare | Sealed Tank Crews; armored agent delivery; nerve-suppression certification after its separate gates; protected breakthrough logistics; synchronized shock eligibility. |
| `contaminant_firebases` | Contaminant Fire Support | Projector fire control; counterbattery coordination; Chemical Artillery Shells; persistent-agent shell filling after its separate gates; deep-contamination operation eligibility. |
| `integrated_chemical_operations` | Integrated CBRN Command | Operations and Intelligence HQ; Protection and Decontamination HQ; Mobile Decontamination Columns; Chemical Air Interdiction and biological security; Medical and Biosecurity HQ; terminal theater command certification. |

Toxic Armored Warfare mastery 3 records the camp nerve-method and mobile suppression operation flags. The `nerve_agent_suppression_formation` technology is a non-researchable certification marker, not a separate fielded company; its helper also requires Armored Agent Delivery, a completed sarin or soman project, advanced protection, and the explicit nerve-suppression policy flag. This track grants no camp or occupation-law infrastructure by itself. The camp route and its consequences are owned by the separate camp system.

### Doctrine-only technologies

The doctrine's grant helper silently gives these non-researchable technologies when each current predicate is met, including later retries from mastery and migration effects:

- `hazard_pioneer_formation`, a retained ID that improves the existing protection support category rather than enabling a separate Hazard Pioneer unit
- Chemical Artillery Shells
- Persistent Agent Shell Filling
- Armored Agent Delivery
- Sealed Tank Crews
- Nerve Agent Suppression Formation
- Chaos Assault Battalion and Improved Chaos Assault Equipment
- Mobile Decontamination Columns
- Chemical Air Interdiction
- Theater CBRN Headquarters
- Biological Security Assault Formation.

The four `cbrn_commission_*` scripted effects are compatibility-named grant helpers invoked by `cbrn_grant_available_doctrine_technologies`; they check their exact grant predicates and apply the technologies immediately. There are no corresponding paid seven-day decision commissions in the current doctrine decision file.

Chemical Air Interdiction is an eligibility marker only in this stage. It creates no passive regional effect, makes no estimate of sortie activity, and cannot contaminate a state. A later selected-state operation must prove execution, consume the selected payload, resolve protection and conditions, and call the shared exposure record. Idle chemical-capable aircraft never contaminate a region.

## Use policy

Policy changes are decisions with a 90-day reassessment lock and a five-Command-Power cost. The current decisions have zero native Political Power cost and call the shared policy effect after their exact availability gates pass. Doctrine progression does not change national policy automatically.

One `cbrn_doctrine_policy_command_power_cost.policy_change` constant supplies the inclusive affordability gate, all three hidden click payments, and the scripted-localisation cost quote. The reassessment text reads the same `cbrn_doctrine_timing.policy_reassessment_days` constant used by the timed flag. The click effect checks affordability again before accepting the requested policy, so a failed payment cannot change authority.

| Policy | Command Power | Reassessment | Source decision |
| --- | ---: | --- | --- |
| Retaliation Only | 5 | 90 days | `cbrn_choose_retaliation_only` |
| Battlefield Authorization | 5 | 90 days | `cbrn_choose_battlefield_authorization` |
| Unrestricted Authorization | 5 | 90 days | `cbrn_choose_unrestricted_authorization` |

Policy permits delivery adapters to pass authorization checks. It never spends a payload or creates exposure by itself. The inactive selected-state coercive-security operation retains its separate authorization gate for compatibility, but it is not the accepted camp implementation. Gas-Chamber Saturation Drills use the camp network directly and require no Chaos Warfare doctrine or occupation-policy prerequisite beyond the researched and stocked nerve agent.

## Condemnation-only doctrine mitigation

`cbrn_prepare_chemical_action_record` owns the doctrine lookup so every accepted chemical delivery route receives one consistent multiplier:

- Operations mastery 1: 0.75
- Operations mastery 4: 0.55
- Operations mastery 5: 0.35
- otherwise: 1.00.

The shared exposure calculation applies this value only to the Condemnation base before attribution and public-harm floors. Evidence and attribution are calculated independently. The old Theater Contamination and Terminal Hazard numerical catalogue in this guide was superseded by the 2026-09-20 combined-cap retune; the current compatible endpoint maxima are in the source-arithmetic table above. Physical payload debit, evidence, attribution, deaths and death history, contamination and contamination history, medical saturation and medical history, confirmed-use history, domestic war-support penalties, biological-use counters, accident records, resistance trauma, and public-harm floors remain fully recorded.

## Exact-state decontamination assignment

An active Army HQ Decontamination Corridor plus Theater Exploitation exposes a state-targeted assignment decision. It requires a controlled state with actual chemical contamination and permits one national assignment every 28 days.

Each assignment spends 4 Command Power, 40 Decontamination Equipment, and 300 Fuel at deployment. The column also needs at least 100 Gas Masks, 20 Support Equipment, and 2 Motorized Equipment in the stockpile, but it does not consume those support stores for the assignment. Decontamination stock is debited from the oldest available model. The decision requires both the payment and support stores before dispatch; a failed payment applies neither cleanup nor the 28-day national lock.

The cost row's three texticons use scripted-localisation trigger quotes from the same `cbrn_doctrine_cleanup_assignment_cost` constants as its affordability checks and payment. Each amount remains visible in a ready or shortage colour without raw constant interpolation; native decision-list rendering of that row remains unverified.

The assignment requirement and result descriptions and the Theater Contamination, Terminal Hazard, Mask Discipline, and Hazard Assault Cadres spirit tooltips use `common/scripted_localisation/cbrn_doctrine_value_localisation.txt`. Each tooltip prepares its numeric values from the same doctrine, biological, raid, and cleanup constants consumed by gameplay before formatting the player text. `localisation/english/cbrn_doctrine_l_english.yml` contains no raw constant interpolation; native spirit-tooltip rendering remains unverified.

The same binding file also supplies the Chemical Operations Commander trait and the Controlled Retaliation, Contaminant Fire Coordination, and Chemical Operations Academy tooltips in `chaosx_abilities_l_english.yml` and `chaosx_ideas_l_english.yml`. Their visible text focuses on the applicable modifiers and earned-service rule; AI tuning and release-accounting notes remain in script and documentation rather than the spirit hover. Native trait and officer-corps hover rendering remains unverified.

Cleanup output depends on the current contamination class:

- Trace or Local: 10 points
- Serious: 8 points
- Severe: 5 points
- Catastrophic: 3 points.

The current Theater Contamination source multiplier for this output is 1.10 before the compatible MIO cleanup factors shown above. The effect calls the state contamination record and records only the amount actually removed. It does not erase evidence, attribution, deaths, Condemnation, or confirmed-use history. The national and selected-state assignment locks use the same 28-day tuning constant; their in-game expiration remains a live validation item.

## Officer corps and high command

The three mutually exclusive Army Command postures are Controlled Retaliation, Theater Contamination, and Terminal Hazard. Controlled Retaliation contributes 1% army organisation in its legal organisation scenario. Theater Contamination contributes 3% planning in its legal planning scenario and supports exact-state cleanup. Terminal Hazard contributes 2.5% army attack and 0.5% coordination in its separate offensive scenario. Current `common/ideas/cbw_spirits.txt`, doctrine constants, and the source-arithmetic tables above govern the remaining effects; the older high-magnitude spirit and paid offensive HQ preparation examples are superseded. Evidence and attribution remain recorded independently of the posture.

The historical Gas-Chamber Saturation Drills numerical example is superseded by the accepted combined-cap retune; the current legal authored nerve-camp mortality specialization reaches 1.495 times base according to the doctrine owner's source arithmetic. The hook runs only inside the camp system's state death calculation and uses its stored responsible-country pointer. It does not create, reveal, authorize, or unlock a camp, extermination building, experiment site, restricted chemical site, or occupation law, and it does not alter camp evidence, discovery, resistance, trauma, Condemnation, or responsibility records. Unrestricted Authorization remains the governing national use policy.

The earlier flat-stat explanation for Chemical Projector Batteries and the Chaos Battalion is superseded because technology subunit bonus fields are multiplicative toward the unit. Current `common/technologies/chaosx_technologies.txt` gives each projector tier 2.5% soft attack, 13% hard attack, 4% defense, and 7.5% breakthrough; the 1942 Battalion technology grants 15% breakthrough and 11 flat organisation. The strict legal all-independent upper bounds are in the current source table above, while exact engine aggregation remains unresolved.

The auditor found that the earlier reconnaissance technology values added flat `recon` values of 2, 3, and 5 to a base of 4, or +250%. The parent resolved the accepted +35% dedicated-static ceiling to include this reconnaissance utility. The technology owner verified fractional `recon` syntax against installed vanilla `common/technologies/infantry.txt` and changed the three grants in `common/technologies/chaosx_technologies.txt` to 0.2, 0.4, and 0.6. Their +1.2 sum on base 4 is +30% in source arithmetic; the engine result remains unverified.

Chemical Operations Commander is earned from completed qualifying Headquarters service. Chemical Operations Academy grants +3 percent army experience gain and does not award the trait. The two paid offensive HQ preparation orders are retired; five protective orders remain. A country's first confirmed chemical exposure applies a defender-side command shock without an attacker buff.

The Division Command slot contains mutually exclusive Mask Discipline, Hazard Assault Cadres, and Contaminant Fire Coordination postures. Mask Discipline contributes 1% army organisation in the Controlled Retaliation organisation scenario. Hazard Assault Cadres instead contributes 10% role-specific attack and defense to the Chaos Battalion and Protection Company route and cannot coexist with Mask Discipline. Current spirit source controls the remaining effects; the older +35% artillery attack example is superseded.

Chemical Operations Commander supplies native CBRN High Command specialist, expert, and genius ranks. The current `common/country_leader/cbrn_high_command_traits.txt` source grants +1/+3/+4 percent planning speed and +5/+10/+15 maximum Command Power across those ranks. Civil Defence Coordinator, Chemical Logistics Inspector, and Biological Security Director retain their distinct institutional offices; Biological Security Director contributes 0.5% army organisation and -15% resistance growth.

The `chemical_operations_commander` leader trait is awarded through completed service and grants no free release ability. Its remaining protective order effects require the active HQ source and engine review.

## AI behavior

The source weights for adoption and track preference use program profiles, industry, war, enemy chemical use, and explicit route flags. Battlefield Authorization and Unrestricted Authorization start at zero and gain source weight from route and spirit modifiers; availability and final choice remain separate questions. The current decision file gives only the three policy choices and exact-state cleanup an AI score. The August probability audit predates this narrowed roster, while the [September cleanup comparison](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-25_theater_three_cost_probability_compare.md) resolves a base cleanup score but leaves eligibility, modifiers, and final choice partial. No current scenario-specific probability proof is claimed for doctrine adoption, all three policy choices, or the full cleanup decision pool.

Officer-corps and high-command choices use the same defensive, battlefield, logistics, and outbreak profiles. Nonhuman AI receives zero selection weight for these institutional appointments and spirits. Every HQ ability retains the full player-equivalent composition, readiness, policy, stock, and Command Power gate. AI receives no hidden payload, readiness, or contamination shortcut.

## Compatibility and migration

The grand doctrine and four track IDs remain stable for save and script compatibility. Legacy atrocity-facing names and broad permanent bonuses are replaced. The Chemical Operations Academy remains an active officer-corps route that grants +3 percent army experience gain, while the old chemical-air spirit ID remains hidden and unavailable for save compatibility. Chemical Operations Commander is earned from completed qualifying Headquarters service; no academy trait roll, periodic country scan, or passive chemical activity grants it. Legacy Integrated Operations biological bonuses are neutralized. The dedicated Theater Contamination and Terminal Hazard spirits provide the accepted biological escalation, deployment refund, and Condemnation behavior.

`on_startup` calls `cbrn_migrate_legacy_chaos_warfare` for doctrine holders in new campaigns, and CXT setup has a separate call. The migration reconstructs adoption and mastery flags from native doctrine state, clears obsolete occupation-law authority, reconciles current institutional predicates, and retries eligible technology grants. The earlier one-time `cbrn_convene_institutional_review` decision is absent from the current doctrine decision file, so this document cannot claim a user-facing migration action for an existing loaded save. It does not fabricate stock, fielded formations, payload use, or consequences.

Static doctrine definitions use file-local `@` macros because current installed doctrine documentation does not declare global `constant:` support for those parser fields. The local values mirror the centralized `cbrn_doctrine_cost`, `cbrn_doctrine_mastery`, `cbrn_doctrine_modifier`, and `cbrn_doctrine_ai` tables. Scoped effects, triggers, decisions, ideas, and variables continue to use global script constants.

## Verified engine limits

- Native grand-doctrine milestones map one-for-one to tracks; cross-track institutional flags are reconciled by scripted effects after current predicates pass.
- Native mastery measures eligible fielded units but exposes no exact per-unit equipment-fill check in this source review. The former paid Hazard Assault Training decision is absent, so no manual mastery-purchase path is documented here.
- Cumulative gas-mask production and the adoption baseline are recorded, but the current Protective Foundation trigger uses Basic Gas Masks rather than a production increment or reserve proof.
- Combat tactics expose no verified activation effect that can reserve payload and dispatch the shared exposure record. Prepared Chemical Barrage remains weight zero and fail-closed until a payload-consuming adapter exists.
- Chemical Air Interdiction has no continuous ordinary-air hook. No estimator or passive contamination fallback is retained.
- Commander abilities do not expose a selected state. Exact decontamination uses a separate player-selected state decision tied to a currently active corridor.
- The Army Headquarters surface is DLC-owned. No ordinary-division substitute is provided.

## Assets and runtime wiring

The asset package is under `docs/assets/chaos_warfare_system/stage_5_doctrine_officer_corps/`. `interface/cbrn_doctrine.gfx` registers doctrine, spirit, technology, category, and decision sprites, while `interface/chaosx_traits.gfx` registers the leader-trait sprite. Registration alone does not prove a current visible consumer or a live rendered image.

### Current doctrine and technology sprites

| Sprite | Runtime DDS |
| --- | --- |
| `GFX_doctrine_chaos_warfare_medium` | `gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds` |
| `GFX_doctrine_extermination_columns_medium` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_hazard_assault_formations.dds` |
| `GFX_doctrine_chemical_suppression_medium` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_toxic_armored_warfare.dds` |
| `GFX_doctrine_contaminant_firebases_medium` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_contaminant_fire_support.dds` |
| `GFX_doctrine_integrated_chemical_operations_medium` | `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_integrated_cbrn_command.dds` |
| `GFX_cbrn_doctrine_hazard_assault_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/hazard_assault_reward_strip.dds` |
| `GFX_cbrn_doctrine_toxic_armor_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/toxic_armor_reward_strip.dds` |
| `GFX_cbrn_doctrine_contaminant_fire_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/contaminant_fire_reward_strip.dds` |
| `GFX_cbrn_doctrine_integrated_command_reward_strip` | `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/integrated_command_reward_strip.dds` |
| `GFX_mobile_decontamination_columns_medium` | `gfx/interface/technologies/stage_5_chaos_warfare/cbrn_mobile_decontamination_columns.dds` |
| `GFX_chemical_air_interdiction_medium` | `gfx/interface/technologies/stage_5_chaos_warfare/cbrn_chemical_air_interdiction.dds` |

The five doctrine icons and four mastery strips are explicitly referenced by the active grand-doctrine and subdoctrine definitions. The two technology icons follow the active technology IDs `mobile_decontamination_columns` and `chemical_air_interdiction`, but their visibility in the technology interface is not proven by a focused MCP render.

### Current officer corps, high command, and leader trait sprites

| Sprite | Runtime DDS |
| --- | --- |
| `GFX_idea_chemical_command_reagent_optimization_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/controlled_retaliation_doctrine.dds` |
| `GFX_idea_cbrn_theater_contamination_doctrine_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/theater_contamination_doctrine.dds` |
| `GFX_idea_cbrn_terminal_hazard_doctrine_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/terminal_hazard_doctrine.dds` |
| `GFX_idea_cbrn_mask_discipline_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/mask_discipline.dds` |
| `GFX_idea_cbrn_hazard_assault_cadres_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/hazard_assault_cadres.dds` |
| `GFX_idea_chemical_division_contamination_command_spirit` | `gfx/interface/officer_corp/spirits/stage_5_chaos_warfare/contaminant_fire_coordination.dds` |
| `GFX_idea_cbrn_civil_defence_coordinator` | `gfx/interface/ideas/stage_5_chaos_warfare/civil_defence_coordinator.dds` |
| `GFX_idea_cbrn_chemical_logistics_inspector` | `gfx/interface/ideas/stage_5_chaos_warfare/chemical_logistics_inspector.dds` |
| `GFX_idea_cbrn_biological_security_director` | `gfx/interface/ideas/stage_5_chaos_warfare/biological_security_director.dds` |
| `GFX_trait_chemical_operations_commander` | `gfx/interface/traits/stage_5_chaos_warfare/trait_cbrn_operations_commander.dds` |

The nine idea sprites map to active `picture` values in `common/ideas/cbw_spirits.txt` and `common/ideas/cbrn_high_command.txt`. The leader-trait sprite matches the active `chemical_operations_commander` ID in `common/unit_leader/chaosx_traits.txt`. Source mapping is not a live visual check.

### Current decision and category sprites

Every decision icon below is an independent 32-by-32 concept in `gfx/interface/decisions/stage_5_chaos_warfare/`. The category is an independent 52-by-40 composition.

| Sprite | Runtime DDS |
| --- | --- |
| `GFX_decision_category_cbrn_chemical_operations` | `cbrn_chemical_operations_category.dds` |
| `GFX_decision_cbrn_set_retaliation_authority_policy` | `cbrn_set_retaliation_authority_policy.dds` |
| `GFX_decision_cbrn_set_limited_battlefield_policy` | `cbrn_set_limited_battlefield_policy.dds` |
| `GFX_decision_cbrn_set_unrestricted_policy` | `cbrn_set_unrestricted_policy.dds` |
| `GFX_decision_cbrn_assign_decontamination_corridor` | `cbrn_assign_decontamination_corridor.dds` |

The category icon is referenced by `common/decisions/categories/cbrn_doctrine_categories.txt`; the three policy icons and cleanup icon are referenced by the four active decisions in `common/decisions/cbrn_doctrine_decisions.txt`.

### Registered legacy sprites without a current doctrine consumer

`interface/cbrn_doctrine.gfx` still registers the four milestone sprites `GFX_cbrn_doctrine_milestone_protective_foundation`, `GFX_cbrn_doctrine_milestone_delivery_integration`, `GFX_cbrn_doctrine_milestone_theater_exploitation`, and `GFX_cbrn_doctrine_milestone_terminal_command`. Current doctrine blocks do not reference them, and no dedicated command UI consumer was established by this source review.

The same GFX file retains unreferenced decision sprites for `cbrn_convene_institutional_review`, `cbrn_chaos_warfare_establishment_mission`, `cbrn_complete_delayed_establishment`, the four `cbrn_claim_*` cards, `cbrn_hazard_assault_training`, `cbrn_set_defensive_preparation_policy`, `cbrn_set_strategic_release_policy`, and the four `cbrn_commission_*` cards. Their registered DDS files are legacy assets, not evidence that those decisions remain in the current menu. The old five-policy icon roster is therefore superseded by the three active policy icons above.

## Remaining validation and possible depth

Native raid reservation, cancellation, target-loss, and war-end outcomes still lack an engine-level refund and exactly-once proof. Doctrine and policy AI evaluations remain partial, and the focused doctrine renderer has not produced a source-accurate Chaos Warfare view. Combined unit, commander, and MIO bonuses still need engine-effective evidence alongside the source balance calculation above. These limits are tracked in the [CBRN overhaul completion report](../../plans/chaos_warfare_system_plans/2026-09-25_cbrn_overhaul_completion_report.md).

The registered milestone sprites have no current doctrine consumer. A command summary could use them if a later accepted design calls for one. Other possible depth includes after-action doctrine history and theater-specific staff reports. Any future operation must preserve exact payload, state, protection, evidence, and consequence accounting.
