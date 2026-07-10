# Army HQ Company and Ability Matrix

## Headquarters support companies

| HQ company | Manpower target | Essential equipment target | Passive target | Ability unlocked | Shortage behavior | AI role |
| --- | ---: | --- | --- | --- | --- | --- |
| CBRN Operations Section | 250 to 400 | 60 support eq, 30 masks, 20 instruments, radios | +3 to 5% planning speed, -10% preparation time | Prepare Chemical Offensive | ability blocked below 50% instruments or masks | required for offensive CBRN HQ |
| Chemical Intelligence and Weather Cell | 200 to 350 | 50 support eq, 30 instruments, 10 trucks, radios | +10% recon or intel factor, +15% forecast confidence | Seal Operational Area or Forecast Preparation | no forecast improvement below essential floor | artillery and air HQ |
| Protective Logistics Section | 300 to 500 | 80 support eq, 80 mask crates, 30 trucks | +15% effective order coverage, -15% filter consumption | Issue Theater Protective Posture | coverage scales directly with masks | defensive and retaliatory HQ |
| Mobile Decontamination Column | 400 to 700 | 100 decon, 60 trucks, 40 masks, 50 support eq | -20% contaminated attrition, +25% route cleanup | Establish Decontamination Corridor | no cleanup below 40% trucks or decon | contaminated theater HQ |
| Medical Countermeasure Directorate | 300 to 500 | 70 support eq, medical capacity, 25 trucks, 30 masks | -20% exposure death multiplier, +10% trickleback under exposure | Mass Antidote and Casualty Response | mortality reduction scales with supplies | nerve and high-casualty defense |
| Biological Security Section | 300 to 550 | 60 support eq, 40 instruments, 40 decon, 25 trucks, medical | +20% detection, -20% spread from captured state | Seal Infection Corridor | loses outbreak control when instruments or decon are absent | bio-threat and occupation HQ |

Numbers are planning anchors. Exact vanilla HQ manpower and equipment scale must be checked in 1.19 files.

## Ability matrix

| Ability | Required HQ company | Preparation | Active duration | Cooldown | Command power target | Recurring equipment | Main friendly penalty | Main effect |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| Prepare Chemical Offensive | CBRN Operations | 7 to 21 days | 3 to 14 days | 45 to 120 days | 20 to 60 scaled by battalions | payload, masks, filters, shell or air lots | supply +10%, blowback risk | enables selected delivery and protected exploitation |
| Theater Protective Posture | Protective Logistics | 1 to 3 days | 14 to 60 days | 14 days | 10 to 35 | masks and filters weekly | movement -3 to -7%, attack -2 to -5% | strong protection and lower surprise |
| Decontamination Corridor | Mobile Decon | 3 to 7 days | 14 to 45 days | 30 days | 10 to 45 | decon, trucks, fuel | local route bottleneck during setup | reduced movement and supply penalty, state cleanup |
| Seal Operational Area | Weather or Biosecurity | 2 to 7 days | 14 to 60 days | 30 days | 10 to 35 | support eq and manpower | local output and resistance pressure | lower spread, better evidence control or preservation |
| Mass Antidote Response | Medical Directorate | 1 day | 7 to 21 days | 30 days | 10 to 40 | medical capacity, support eq | supply +5 to 10% | lower nerve deaths and org loss |
| Seal Infection Corridor | Biosecurity | 2 to 5 days | 30 to 90 days | 45 days | 15 to 45 | decon, medical, instruments | movement and output penalty | lower biological spread and faster detection |
| Combined CBRN Overmatch | Theater CBRN HQ tech plus two companies | 14 to 30 days | 7 to 14 days | 120 to 240 days | 50 to 60 | large masks, payload, decon, medical, fuel | high supply and political burden | simultaneous protected operation and cleanup |

## Ability outcome modifiers

| Factor | Effect on preparation | Effect on dose or protection | Effect on blowback | Effect on evidence |
| --- | ---: | ---: | ---: | ---: |
| Readiness below 40 | +50% time | -35% | +50% | +25% |
| Readiness 40 to 59 | baseline | 80% | +15% | baseline |
| Readiness 60 to 79 | -15% | 100% | -15% | -10% accidental evidence |
| Readiness 80 to 100 | -25% | 110% cap | -30% | -20% accidental evidence |
| Payload ratio 25 to 49% | no change | 35% | +25% | high wreckage and waste |
| Payload ratio 50 to 74% | no change | 65% | +10% | baseline |
| Payload ratio 75 to 99% | no change | 90% | baseline | baseline |
| Payload ratio 100%+ | no change | 100% | -5% reserve effect | baseline |
| Protection below 50% | no change | attacker bonus unchanged | +75% | +25% |
| Protection 90%+ | -5% | attacker benefit from safe exploitation | -40% | -10% handling evidence |

## HQ company combinations

| HQ role | Recommended companies | Purpose |
| --- | --- | --- |
| Defensive protection | Protective Logistics + Medical Countermeasure | survive enemy chemical use |
| Chemical artillery | CBRN Operations + Weather Cell | prepared barrage and forecast |
| Armored breakthrough | CBRN Operations + Mobile Decon | release and exploit corridor |
| Strategic air | Weather Cell + CBRN Operations | target, forecast, and coordinate raid |
| Biological containment | Biosecurity + Medical Countermeasure | detect and contain outbreak |
| Occupation CBRN | Biosecurity + Mobile Decon | capture facilities and manage contaminated state |
| Full capstone | Theater tech with CBRN Operations plus one protection and one cleanup company | combined operation without all six slots |

## Validation gates

- Verify how many HQ support slots current vanilla permits.
- Verify whether company-gated abilities can require more than one HQ company.
- Verify order scopes and unit-modifier syntax.
- Verify command-power scaling by battalions and maximum cost.
- Verify equipment status can gate or scale scripted ability effects.
- Verify AI can assign HQ support and use abilities.
