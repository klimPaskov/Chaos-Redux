# Historical Chaos Warfare Theorists and CBRN Advisors

## Overview

Selected historical scientists already represented in Chaos Redux can serve both as special-project scientists and as named national advisors or theorists.

Each person remains one static character with one identity and one wired large scientist portrait.
The advisor role uses a separate wired 65x67 dossier card. All fifteen cards have source-resolved DDS files; native card display remains unverified.

## Roster

| Country | Character | Role | Chaos Warfare required |
| --- | --- | --- | --- |
| Australia | Howard Florey | Medical Countermeasure Pioneer | No |
| United Kingdom | Paul Fildes | Biological Warfare Theorist | Yes |
| United Kingdom | Alexander Fleming | Medical Countermeasure Pioneer | No |
| United Kingdom | Norman Heatley | Antibiotic Production Coordinator, from 1940 with Field Antibiotics | No |
| Germany | Gerhard Schrader | Chemical Warfare Theorist | Yes |
| Germany | Kurt Blome | Biological Weaponization Director | Yes |
| Japan | Shiro Ishii | Chaos Weaponization Theorist | Yes |
| Japan | Masaji Kitano | Biological Weaponization Director | Yes |
| Poland | Franciszek Witaszek | Resistance Biological Saboteur | Yes |
| Soviet Union | Grigory Mairanovsky | Toxicological Weaponization Director | Yes |
| Soviet Union | Ivan Velikanov | Biological Warfare Theorist | Yes |
| Soviet Union | Nikolay Zelinsky | Activated-Carbon Protection, with Collective Protection Systems | No |
| United States | Frank Olson | Aerobiology Specialist | Yes |
| United States | Ira Baldwin | Biological Warfare Theorist | Yes |
| United States | Stanhope Bayne-Jones | Epidemiological Survey Director, from 1942 with Mass Vaccine Production | No |

Medical countermeasure appointments for Florey and Fleming, and the project-gated Heatley, Zelinsky, and Bayne-Jones appointments, do not require Chaos Warfare.
Appointments tied to offensive, retaliatory, clandestine, or dual-use weaponization programs require the grand doctrine even though the character remains available as a scientist before adoption.
Blome's biological-program appointment begins in July 1943, Witaszek's resistance leadership in July 1940, and Mairanovsky's secret toxicology director role in 1938 as source-calibrated gameplay floors. Olson's 1943 appointment represents aerobiology research rather than the later Special Operations Division leadership; it improves biological project work and initial delivered potency without a production-director or Condemnation benefit. The [individual correction](../../specs/chaos_warfare_system_specs/corrections/2026-09-27_scientist_lifecycle_and_field.md) records their sources and remaining date limits.

## Gameplay integration

The static trait modifiers are deliberately substantial: the theorists reduce land-doctrine costs by 25-30%, add 20-25% Army experience gain, and provide 25-35% special-project speed or 15% research speed where appropriate.
Political advisors provide strong research, project, production, stability, resistance, or compliance bonuses according to their role.

Operational effects are conditional on the character occupying the relevant advisor slot.
They are applied through `common/scripted_effects/cbrn_historical_advisor_effects.txt` and called only from the shared chemical exposure and biological lifecycle systems.

Operational factors are evaluated within one legally appointable country, not by multiplying every advisor in the roster.
Gerhard Schrader's chemical theorist appointment is GER-only and Grigory Mairanovsky's toxicological director appointment is SOV-only; their dose and contamination factors cannot stack legally.
Neither specialist changes the derived readiness value.
JAP can combine Ishii and Kitano when Kitano's doctrine and project requirements are met: initial potency, spread, and death multipliers are 1.82, growth 1.6875, and medical saturation 1.30 before doctrine and environmental factors.
USA can combine Baldwin and Olson when the doctrine and biological capability requirements are met: potency 1.56, growth 1.20, spread/deaths 1.25, and unchanged medical saturation.
Olson affects initial potency only.
These are source appointment bounds; final intensity/exposed-share and spread-chance clamps remain in the lifecycle consumer.

| Appointment | Operational bonus |
| --- | --- |
| Chemical Warfare Theorist | +30% delivered dose, +25% contamination, 18% less resulting Condemnation |
| Toxicological Weaponization Director | +30% dose, +25% deaths, +30% contamination, 22% less resulting Condemnation |
| Biological Warfare Theorist | +30% initial potency, +20% growth, +25% spread/deaths, 18% less resulting Condemnation |
| Chaos Weaponization Theorist | +40% initial potency/spread/deaths, +35% growth, +30% medical saturation, 30% less resulting Condemnation |
| Aerobiology Specialist | +20% initial potency only |
| Biological Weaponization Director | +30% initial potency/spread/deaths, +25% growth, 22% less resulting Condemnation |
| Resistance Biological Saboteur | +25% initial potency/spread, 15% less resulting Condemnation |
| Medical Countermeasure Pioneer | 30% fewer chemical/biological deaths and chemical medical saturation; 35% less biological medical saturation; +15 detection |
| Activated-Carbon Protection | 25% fewer military chemical casualties with issued respirators |
| Antibiotic Production Coordinator | 25% less medical saturation with an active qualifying antibiotic course |
| Epidemiological Survey Director | 25% less outbreak growth with an active Surveillance Network |

The historical multipliers still used by the current helpers match `33b6946dd^`; retired readiness and biological-program-director entries are absent.
The aerobiology and three later defensive appointments keep their distinct current consumers and use the table above.
Active CBRN Operations High Command ranks additionally protect the controller's affected states by 20%, 30%, or 40% against chemical/biological deaths and medical saturation, selecting the highest rank once.
The existing combined hazard-response floor retains at least half the relevant baseline after protection.
Chemical contamination and medical-saturation temporaries are initialized in `cbrn_calculate_chemical_action_outputs` before their nested advisor helpers, so the returned factors remain available to the later output calculation.

Chemical specialists increase delivered dose, deaths, or contamination according to their appointment, while reducing resulting Condemnation without erasing evidence.
Biological specialists can increase seed potency, growth, spread, deaths, or medical saturation according to their role. Olson's aerobiology appointment affects only initial potency and does not reduce Condemnation.
Defensive specialists reduce deaths and medical saturation or increase outbreak detection.
Some offensive specialists reduce the Condemnation generated by their operations; none reduce payload expenditure, evidence, attribution, or recorded deaths. Olson changes no Condemnation outcome.

## Scientist and advisor roster

The fifteen dual-role scientists and advisors are static characters in `common/characters/cbrn_historical_specialists.txt`; the other 52 scientist-only profiles are in `common/characters/cbrn_historical_scientists.txt`. All 67 are recruited directly into their home countries at scenario start with the skills and traits recorded in [the scientist roster](cbrn_historical_scientists.md). Advisor appointment requirements remain separate.

## Assets and wiring

The large portraits remain under `gfx/leaders/scientists/` and remain registered by the existing scientist portrait file.
Advisor DDS files live under `gfx/interface/advisors/cbrn/` and are registered by `interface/cbrn_historical_advisors.gfx`.
Political-advisor cards are assigned through `portraits.civilian.small`; theorist cards are assigned through `portraits.army.small`; the full scientist portrait remains `portraits.army.large`.
All fifteen card sprites and 65x67 DDS files resolve. The [original runtime inventory](../../assets/portraits/cbrn_scientist_runtime_inventory_2026-09-25.md) records twelve cards; the [defensive-card manifest](cbrn_defensive_advisor_cards_manifest_2026-09-27.md) records the three additional cards. The earlier [portrait audit](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-25_cbrn_scientist_portrait_provenance_audit.md) records the absent historical archive; the user confirmed that the scientist portraits already in the mod are approved and recovering that archive is not a blocker.

## Future extensions

Country routes may add event-driven retirement, defection, arrest, or program-control changes for these characters when historically appropriate.
Those changes should manipulate the existing static character roles rather than create replacement identities.
