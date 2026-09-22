# CBRN doctrine and spirit balance handoff

Disposition: implemented for the doctrine, spirit, HQ active-trait, and scoped constants assigned to the doctrine worker; cross-system completion remains unresolved for biological spread and detection probability surfaces.

The parent accepted the full legal stack budgets during the 2026-09-20 CBRN overhaul: passive army attack 5%, organization 5%, planning 15%, coordination 8%, reinforcement 2 percentage points, conventional combat 15%, dedicated CBRN static combat 35%, and additional CBRN hazard benefit 50% on one metric.
The parent also distinguished authored CBRN specialization multipliers from intrinsic agent identity, route base, target density, weather, terrain, and outcome severity; issued mask coverage is the foundational equipment mechanic, while subsequent treatment and protection factors share the 50% additional-benefit ceiling.
The verified route-condition command receipt can independently reach 1.25 before doctrine multipliers; artillery specialization 1.240988 × that scenario input 1.25 = 1.551235 against an unconditioned base, but the authored specialization component remains below 1.50.
All arithmetic below is source arithmetic, not a live-game result.

## Source changes

- `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt` and the four `common/doctrines/subdoctrines/land/chaos_warfare_*_subdoctrines.txt` files now concentrate the four tracks on protected assault, armored delivery, fire support, and command, respectively.
- `common/ideas/cbw_spirits.txt` reduces global combat and organization benefits, gives theater and terminal spirits supply costs, moves Hazard Assault Cadres to the surviving gas-mask/decontamination detachment, and gives the academy a real 3% Army Experience benefit instead of a stale random-trait promise.
- `common/unit_leader/cbrn_hq_traits.txt` removes active-order planning and limits protective medical modifiers; active postures retain movement, supply, or attack tradeoffs.
- `common/script_constants/chemical_warfare_constants.txt`, `biowarfare_constants.txt`, `biological_lifecycle_constants.txt`, `camp_repression_rework_constants.txt`, `cbrn_historical_advisor_constants.txt`, and `chemical_spirit_constants.txt` contain the assigned cross-metric retunes.
- `localisation/english/cbrn_doctrine_balance_l_english.yml` is a new UTF-8 BOM description file; narrow reward, academy, HQ-order, and Dimercaprol tooltip edits are in `chaosx_doctrines_l_english.yml`, `chaosx_ideas_l_english.yml`, `cbrn_hq_l_english.yml`, and `chaosx_technologies_l_english.yml`.
- The core worker mirrored doctrine and spirit tuning in `common/script_constants/cbrn_doctrine_constants.txt`; the unit, technology, high-command, historical-roster, MIO, exposure, HQ-effect, and biological-lifecycle workers own their separate files and values cited below.

The four doctrine identifiers remain `extermination_columns`, `chemical_suppression`, `contaminant_firebases`, and `integrated_chemical_operations`, with the grand-doctrine identifier `chaos_warfare` retained for save and script compatibility.
The new description keys are `CBRN_BALANCED_CHAOS_WARFARE_DESC`, `CBRN_BALANCED_HAZARD_ASSAULT_DESC`, `CBRN_BALANCED_TOXIC_ARMOR_DESC`, `CBRN_BALANCED_CONTAMINANT_FIRE_DESC`, and `CBRN_BALANCED_INTEGRATED_COMMAND_DESC`.
Existing localisation keys narrowly corrected include `chemical_operations_academy_spirit_desc`, `chemical_operations_academy_spirit_tt`, `chemical_suppression_camp_nerve_methods_unlocked_tt`, `contaminant_firebases_raid_targeting_teams_tt`, `contaminant_firebases_persistent_agent_distribution_tt`, `contaminant_firebases_deep_contamination_fireplans_tt`, the Integrated Command M2/M4/M5 reward descriptions and tooltips, `cbrn_hq_active_combined_overmatch_desc`, affected active HQ-order descriptions, and `dimercaprol_desc`.

## Conventional and dedicated combat stacks

| Metric | Full legal source stack | Ceiling |
| --- | --- | --- |
| Army attack | Protected assault mastery 2% + Terminal Hazard spirit 3% = 5% | 5% |
| Army organization | Assault 1% + Integrated Command 1% + Controlled Retaliation 1% + Mask Discipline 1% + biological security director 1% = 5% | 5% |
| Planning | Grand doctrine 1% + Integrated activation 1% + Theater Contamination spirit 3% + native High Command genius 5% + deployed Operations HQ 5% = 15% | 15% |
| Coordination | Fire support 2% + armor 2% + Integrated Command 3% + Terminal Hazard spirit 1% = 8% | 8% |
| Reinforcement | Protected assault 1 percentage point + Integrated Command 1 percentage point = 2 percentage points | 2 pp |
| Conventional line/support artillery soft attack | Fire-support adoption and mastery 10% + global army attack 5% = 15%; the former artillery-wide spirit attack modifier is gone | 15% |
| Chemical projector soft/hard/defense | Soft: category 20% + global attack 5% + two technology flat gains 1.2 / base 12 = 35%; hard: global attack 5% + 1.2 / base 4 = 35%; defense: category 20% + 0.6 / base 4 = 35% | 35% |
| Chemical projector breakthrough | Category 15% + 1.5 / base 10 = 30%; a conservative additional 5% global-attack allowance reaches 35% even if treated as equivalent | 35% |
| Chaos Battalion breakthrough | Assault category 10% + Battalion-specific 5% + 1942 technology flat 2.7 / base 18 = 30%; a conservative 5% global-attack allowance reaches 35% | 35% |
| Chaos Battalion organization | 1942 technology flat 12 / base 40 = 30% + global organization 5% = 35% | 35% |
| Chemical projector organization | Fire-support flat 5 / base 18 = 27.78% + global organization 5% = 32.78% | 35% |
| Armored delivery organization | Armor flat 5 / base 24 = 20.83% + global organization 5% = 25.83% | 35% |

The unit worker confirmed the surviving category memberships and normalized the formerly excessive Livens and Chaos Battalion flat technology grants.
Protected Assault Expert and Theater Containment Organizer no longer contribute generic 5% attack or defense; the commander worker replaced them with supply endurance and command capacity.
The surviving gas-mask/decontamination detachment receives Hazard Assault Cadres 10% unit attack and defense, while conventional units do not.

## Conditional hazard stacks

| Metric | Worst legal authored specialization stack | Result |
| --- | --- | --- |
| Chemical artillery dose/potency | Fire-support 1.04 × Integrated Command 1.04 × Terminal Hazard 1.05 × stable choking-dose designer 1.03 × two chemical advisors 1.03² | 1.240988 × base |
| Chemical air dose/potency | Fire-support 1.04 × Integrated Command 1.04 × air link 1.02 × Terminal Hazard 1.05 × two chemical advisors 1.03² | 1.228940 × base |
| Chemical contamination points | Artillery dose above × fire-support 1.03 × Integrated Command 1.03 × Terminal Hazard 1.03 × two advisor contamination factors 1.02² × persistent designer 1.02 | 1.439063 × base, conservatively including mutually exclusive designer routes |
| Chemical duration | Fire-support 1.03 × Integrated Command 1.03 × air link 1.10 × Terminal Hazard 1.10 × persistent designer 1.15 | 1.476242 × base |
| Chemical casualty pressure | Artillery dose above × Terminal Hazard casualty factor 1.10 × toxicological advisor death factor 1.05 | 1.433341 × base |
| Cleanup output | Theater Contamination 1.10 × low-water designer 1.15 × rapid-route designer 1.15 | 1.454750 × base |
| Nerve camp deaths | Camp mastery 1.30 × Terminal Hazard camp factor 1.15 | 1.495000 × base |
| Nerve camp payload efficiency | Mastery payload cost 0.50 × baseline use | 50% reduction |
| Biological initial seed potency | Terminal Hazard 1.20 × Integrated Command 1.10 × strategic-dissemination designer 1.02 × five eligible advisor factors 1.02⁵ | 1.486534 × base |
| Chemical Readiness generation | Chemical theorist 1.20 × toxicological director 1.20 | 1.44 × base |
| Chemical Readiness expenditure | Theater 0.70 × terminal 0.75 | 0.525 × base, 47.5% reduction |

Chemical treatment examples remain above the 0.50 residual floor without clamping: blister extra deaths 0.85 generic treatment × 0.80 Dimercaprol × 0.85 advisor = 0.578; medical saturation 0.85 Dimercaprol × 0.85 advisor × 0.85 hospital × 0.85 mobile sorting = 0.522006.
The exposure owner added a final 0.50 residual floor after all extra treatment, shelter, precision, vehicle, MIO, forecast, command, and project effects on each appropriate endpoint.
For example, civilian shelter 0.65 × collective shelter project 0.82 × precision delivery 0.55 would leave 0.29315 exposed fraction without the endpoint floor; the final residual is 0.50.
Armored friendly risk 0.85 vehicle technology × 0.90 MIO × 0.85 sealed crew × 0.85 smoke × 0.40 forecast × 0.60 command would leave 0.132651 residual without the endpoint floor; the final residual is 0.50 of the bounded pre-benefit risk.
The HQ-effects owner also added a final 0.50 preparation-cost floor: the largest legal raw discount stack is 0.75 × 0.90 × 0.95 × 0.70 × 0.60 = 0.269325, floored at 0.50.
The biological-lifecycle owner preserved pathogen-specific antibiotic and Smallpox vaccination baselines, then floored additional growth, mortality, and medical-load response factors at 0.50 relative to those foundations.

## Validation limits and remaining work

The offline Paradox wiki core and doctrine pages, installed vanilla doctrine precedents, vanilla documentation, source references, and current localised consumers were reviewed.
The touched doctrine and localisation sources were inspected for retired unit references and encoding; targeted diff checks found no whitespace errors.
The mandatory `hoi4.tech_inspect` doctrine attempts and the targeted probability inspection route timed out after 180 seconds, so source checks do not substitute for MCP doctrine render/compare or engine-side proof.
The available tool inventory exposes `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare`, but no separate standalone Technology Tree Viewer; standalone viewer evidence is a package gap.
No Hearts of Iron IV process was launched and no commit was made.

Biological spread still lacks the extra-benefit 0.50 residual floor because `bio_spread_countermeasure_mult` feeds `bio_spread_chance` as a `random_list` weight.
The lifecycle owner documented a required baseline audit and same-scenario probability compare before changing that probability-bearing path.
Detection also feeds a `random_list`; distributed surveillance adds a 1.30 multiplier after response bonuses, and its same-metric full legal stack has not been probability-audited or capped.
These are unresolved cross-system budget risks, not evidence that the doctrine/source retunes exceeded the accepted ceilings.
Legacy academy documentation still promises a random 50% Commander trait grant in `docs/systems/cbrn_warfare/chemical_warfare/chemical_operations_commander_trait.md`, `chaos_warfare_officer_corps_spirits.md`, and `chemical_operations_academy_spirit_and_shelling_ai.md`; the documentation curator or parent must replace those claims with the service-earned route and the actual 3% Army Experience spirit.
