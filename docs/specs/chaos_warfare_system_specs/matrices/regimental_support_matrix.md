# Regimental Support Matrix

| Company | Group | Manpower | Essential equipment | Direct stat philosophy | Scripted role | Compatibility | AI use gate |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| Gas Mask and Decon Detachment | primary protection | 250 to 400 | 80 to 120 mask crates, 20 to 40 support eq, 5 to 15 decon | minimal direct combat, small org retention | exposure and death reduction | compatible with ordinary support, exclusive with another primary protection unit | enemy capability or doctrine |
| Chemical Recon Detachment | reconnaissance | 150 to 300 | 15 to 30 masks, 20 to 40 instruments, 30 to 50 support eq, 5 to 15 trucks | modest recon only | surprise reduction, agent detection, evidence | can coexist with mask support | enemy capability or CBRN order |
| Hazard Pioneer Detachment | engineer specialist | 300 to 500 | 40 to 70 masks, 30 to 60 decon, 40 to 70 support eq, 10 to 25 trucks | modest fort and urban adjuster | contaminated route movement and cleanup | can coexist with engineers if balance allows | assault template and mastery 2 |
| Chemical Projector Battery | offensive delivery | 250 to 400 | 20 to 40 masks, 10 to 20 decon, projector equipment, 40 to 100 payload lots | support penalties normalized near vanilla artillery support | close chemical delivery | exclusive with other offensive chemical delivery | payload and policy |
| Chemical Ammunition Train | artillery enabler | 300 to 500 | 20 to 40 masks, 15 to 30 decon, 30 to 60 support eq, 30 to 80 trucks, shell lots | no major attack by itself | enables prepared chemical artillery | one per division, useful only with artillery | artillery density, shell reserve |
| Armored Chemical Delivery | offensive delivery | 250 to 400 | 12 to 20 eligible tanks, 15 to 30 masks, 10 to 20 decon, payload | reduced chassis stats like other regimental armor | close armored exposure and infantry breakthrough adjuster | no parachute, exclusive with projector delivery | armor posture, fuel, payload |
| Nerve Agent Suppression | garrison CBRN | 300 to 500 | 30 to 50 masks, 20 to 40 decon, 10 to 20 instruments, 10 to 25 trucks, nerve payload | high suppression, low frontline stats | targeted state suppression operation | garrison role, exclusive with offensive delivery | radical policy, high resistance |
| Field Epidemiology and Quarantine | bio defence | 250 to 450 | 20 to 40 masks, 20 to 40 instruments, 20 to 40 support eq, 10 to 25 trucks | little direct combat | detection and spread reduction | compatible with protection or medical | outbreak or bio threat |
| Medical Countermeasure Detachment | medical defence | 250 to 450 | 20 to 40 masks, 30 to 60 support eq, medical capacity, 10 to 20 trucks | recovery and trickleback only under exposure | lower military death and saturation | can coexist with mask support, exclusive with ordinary duplicate medical role if needed | nerve or repeated exposure |
| Biological Security Assault | special capture | 300 to 500 | 50 to 80 masks, 40 to 80 decon, 20 to 40 instruments, 50 to 80 support eq | modest urban and fort utility | capture facility, preserve evidence, prevent release | doctrine-only, one per division | infected or facility target |

## Suggested direct stat anchors

These are maximum targets for a fully equipped company before doctrine or technology.

| Company | Organization | Max strength | Supply | Terrain or combat effect |
| --- | ---: | ---: | ---: | --- |
| Gas Mask Detachment | 5 to 10 | 0.2 to 0.4 | 0.03 to 0.06 | no attack bonus, exposure protection |
| Chemical Recon | 5 to 10 | 0.2 to 0.3 | 0.04 to 0.07 | recon and information only |
| Hazard Pioneer | 5 to 10 | 0.3 to 0.5 | 0.06 to 0.10 | fort and urban +5 to 10%, contamination movement |
| Projector Battery | 0 to 5 | 0.2 to 0.4 | 0.06 to 0.12 | support-style attack penalties, chemical operation effect |
| Ammunition Train | 0 to 5 | 0.3 to 0.5 | 0.10 to 0.18 | no direct attack, enables fire plan |
| Armored Delivery | 5 to 10 | 0.4 to 0.7 | 0.05 to 0.12 plus fuel | reduced chassis stats, battalion adjuster up to 5% breakthrough |
| Nerve Suppression | 0 to 5 | 0.3 to 0.5 | 0.08 to 0.14 | suppression 2 to 5, targeted operation adds temporary effect |
| Epidemiology | 5 to 10 | 0.2 to 0.4 | 0.05 to 0.10 | outbreak defence |
| Medical Countermeasure | 5 to 10 | 0.3 to 0.5 | 0.05 to 0.10 | exposure mortality and recovery |
| Biosecurity Assault | 5 to 10 | 0.4 to 0.6 | 0.08 to 0.14 | urban +5%, capture safety |

## Essential equipment scaling

| Equipment status | Direct stats | Scripted special effect | Operation eligibility |
| ---: | ---: | ---: | --- |
| 0 to 24% | vanilla shortage scaling | 0% | blocked |
| 25 to 49% | shortage scaling | 25% | defensive emergency only |
| 50 to 74% | shortage scaling | 55% | low-intensity operation |
| 75 to 89% | shortage scaling | 80% | normal operation |
| 90 to 100% | full | 100% | full operation |

## Duplicate and exploit controls

- one offensive chemical delivery company per division
- one primary gas-mask protection company per division
- operation effect weighted by equipped manpower, not simple presence
- no airborne armored delivery
- no chemical effect while payload need is disabled or depleted
- no battalion adjuster from a company with essential equipment below threshold
- template conversion needs an equipment delivery delay before operation eligibility
