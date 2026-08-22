# Battlefield Biological Dissemination

## Purpose

Battlefield biological dissemination is an Army-led native raid route for Anthrax, Plague, Tularemia, and Smallpox. It attacks an exact enemy-controlled state on the active front and then hands any successful release to the ordinary biological lifecycle. It is not a decision deployment, covert operation, continuous air mission, background pulse, or weaponized-zombie route.

The route is deliberately conditional. A country needs full Chemical Readiness, a policy that allows battlefield use, the matching completed biological-agent project, a current war, Theater CBRN Headquarters technology, and a valid active Combined CBRN Overmatch headquarters command. The selected state must be passable, eligible for an ordinary pathogen episode, controlled by the enemy, and contain either a supply node or at least three enemy divisions. It must border an actor-controlled eligible state containing one of the actor's divisions.

## Native raid and headquarters contract

Combined CBRN Overmatch is the theater authorization and preparation layer. Its headquarters command performs the existing 14–30-day preparation and must remain active and valid. The native raid then performs one day of final release assembly, selects the exact target state, reserves the biological payload, and assigns the delivery formation.

Each raid accepts one assigned formation with at least three infantry, motorized, or mechanized battalions. Its origin is a supply node and its map path is a land arrow. The same target cannot be struck again by this raid type for 180 days.

Current-version raid scripting exposes the exact `var:target_state`, actor, victim, assigned formation, result callback, and native `essential_equipment` reservation. It does not expose a native launch callback or a link between a particular headquarters command and the raid's selected state. Consequently, the supported contract is layered:

- the valid active Combined CBRN Overmatch trait and operation code prove current theater authorization;
- the native raid's selected state, assigned formation, supply-node origin, and essential equipment prove delivery context;
- resolution fails closed if either layer is no longer valid.

No state is inferred from the headquarters, no estimator or proxy launch hook is retained, and no alternate state is searched if the exact native context fails. Native payload already reserved by the raid remains lost when context is rejected; no release, evidence substitute, or biological-use record is fabricated.

## Agent and cost tuning

The values below are gameplay tuning for route identity and balance. They are not claims that historical battlefield biological doctrine used standardized HOI4-sized packages. The equipment quantities represent complete route packages within the mod's production scale.

| Agent | Agent potency tier | Native payload reservation | Command Power | Route potency | Canonical lifecycle strength | Base AI weight | Base success factor |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Tularemia | low | 25 | 10 | 1.00 | 0.85 | 1.50 | 0.50 |
| Anthrax | moderate | 50 | 10 | 1.00 | 1.00 | 1.00 | 0.50 |
| Plague | serious | 25 | 12 | 1.00 | 1.15 | 0.60 | 0.50 |
| Smallpox | severe | 10 | 15 | 1.00 | 1.30 | 0.40 | 0.50 |

Overall weapon strength is strictly `Tularemia < Anthrax < Plague < Smallpox`, and only Smallpox belongs to the severe tier.

All four agents have the same native battlefield-delivery reliability. The different AI weights describe route preference and strategic willingness, not success probability.

Tularemia emphasizes incapacitation and frontline medical disruption at the lowest overall severity. Anthrax creates a moderate persistent local burden. Plague is a serious regional-spread threat. Smallpox is the severe agent, with the greatest canonical lifecycle strength and long-incubation strategic danger.

The raid parser requires file-local `@` values for native preparation, cooldown, Command Power, success, damage, and essential-equipment fields. Shared lifecycle, history, AI, blowback, and consequence tuning lives in `common/script_constants/biological_battlefield_constants.txt`. Reservation and Command Power values are mirrored deliberately and must remain equal across the two parser surfaces.

## Resolution and shared lifecycle

The native result callbacks map to the ordinary lifecycle as follows:

| Native result | Release behavior | Lifecycle result |
| --- | --- | --- |
| Failure | No release; full payload lost; attempt evidence and eligible Condemnation recorded | none |
| Limited success | Weak exact-state release | partial |
| Success | Effective exact-state release | success |
| Critical success | High-intensity exact-state release | catastrophic operational result |

The internal `catastrophic` result token represents a critical operational delivery multiplier shared by every agent. It does not classify Tularemia, Anthrax, or Plague as severe weapons.

Every releasing outcome calls `bio_resolve_battlefield_dissemination`, which validates the immutable raid agent, exact actor, victim, selected state, active authorization, native debit authority, and result. It then prepares the private `battlefield_dissemination` seed record and calls `bio_lifecycle_dispatch_seed` in the selected state.

The lifecycle owns incubation, detection, progression, disruption, deaths, contamination, medical saturation, evidence, attribution, Condemnation, Air Cleanliness contribution, spread, treatment, and cleanup. The raid adapter does not calculate a second consequence path. A successful delivery creates an incubation seed; it does not guarantee a detected or sustained outbreak.

Failure records 50 attempt evidence in the exact target state and a base 12 biological Condemnation source according to the supported visibility threshold. It does not create completed-use history. Releasing outcomes use the shared battlefield profile: base seed intensity 20, exposed share 0.04, evidence 50, friendly-spread risk 0.45, and base Condemnation 35 before agent, result, protection, readiness, doctrine, and lifecycle modifiers.

Enemy-held territory owned by the actor, its faction ally, or a subject relation remains a legal player target. Its exposed-population share is multiplied by 1.25. AI never selects actor-, faction-, or subject-related owned territory.

## Friendly blowback

After a successful primary lifecycle dispatch, the route may seed one exact adjacent actor-controlled state that contains an actor division. The base chance is 45 percent. Full readiness multiplies it by 0.70 and very high military respiratory protection by 0.60. Theater Contamination multiplies the remaining chance by 1.10 and Terminal Hazard by 1.20, reflecting doctrine's more aggressive handling. The final chance is clamped to 0–80 percent.

Blowback uses the private connected-spread lifecycle route with 35 evidence, 35 percent of battlefield seed intensity, and 50 percent of battlefield exposed share. It consumes no second payload and does not add a second deliberate-use record or Condemnation source. If no eligible adjacent friendly state exists, no state is substituted and no search or periodic retry occurs.

## Doctrine and AI

Chaos Warfare doctrine is escalation. Existing lifecycle doctrine modifiers can raise potency, growth, spread, deaths, duration, and medical saturation. Battlefield dissemination also makes friendly blowback more likely. Theater Contamination refunds up to 5 Command Power and Terminal Hazard up to 10 after a valid resolution, capped at that agent's native Command Power cost. Neither doctrine refunds payload or reduces evidence, attribution, physical harm, history, accident records, or public-harm floors. Only Condemnation may be reduced through the shared consequence rules.

AI must pass the same readiness, policy, project, payload, headquarters, front, and target checks as the player. It avoids battlefield dissemination without the required domestic safety technologies unless it is on an unrestricted desperate route. Retaliation, permitted first use, unrestricted posture, program preparation, supply hubs, forts, and concentrated enemy formations raise willingness. Defensive profiles, active outbreaks in the target, treaty membership, and high Condemnation combined with import vulnerability suppress willingness. An unrestricted actor under formal censure receives a continuation preference only when a current enemy has crossed the exact near-victory surrender threshold. An actor at its own near-capitulation threshold stops selecting ordinary battlefield dissemination; an explicitly authorized doomsday route leaves the separate doomsday decision as the only biological release choice during collapse. AI never targets friendly-owned ground.

## Assets and wiring

No new raid art was required. The native battlefield raids reuse the existing Chaos Redux biological military-raid assets without modifying or replacing them:

| Sprite | DDS | SHA-256 |
| --- | --- | --- |
| `GFX_raid_type_icon_anthrax_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_anthrax_strike.dds` | `0B3782F0E035EE9A54F64719A666C47E88F9363E9875AB4F43056303B20A3C4E` |
| `GFX_raid_type_icon_plague_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_plague_strike.dds` | `345640F3E2BF329D4EBBC4DBBF21177224558CBC78EC8617EB5066386AE998C8` |
| `GFX_raid_type_icon_tularemia_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_tularemia_strike.dds` | `2B8F1A6B945A6DBC643D251958C6803F647520E9195094DD3B47A8D3A2D8F6FB` |
| `GFX_raid_type_icon_smallpox_strike` | `gfx/interface/military_raids/map_icons/raid_type_icon_smallpox_strike.dds` | `66D665A8301FA0D37CFBE59CFBF02D19BE3A0FE96D693148209534BC9C84FBDA` |
| Battlefield category and unit aliases | `gfx/interface/military_raids/map_icons/raid_unit_icon_biological_raids.dds` | `C700EE7DF963B54061FBD59B54DCF1292777597011797E467C89D3B6747D344F` |

`interface/chaosx_raids.gfx` owns the stable sprite registrations. `common/raids/categories/chaosx_raid_categories.txt` owns the Army-intelligence raid category. `common/raids/biological_battlefield_raids.txt` owns the four native raid types. Generated decision-icon drafts are not part of this route and are not referenced by gameplay, localisation, or GFX.

## Current closure boundary

The food, water, and medical-chain sabotage, laboratory and stockpile accidents, captured-facility recovery, doomsday, countermeasure, asset, and localization surfaces are implemented in their subsystem files.

This document does not claim Stage 13 or Stage 14 completion.

Remaining package validation is to compare all four battlefield agents and weak, normal, and high-chaos profiles in the package scenarios; exercise the native actor-controlled enemy-owned target contract for captured-facility raids where current-version engine behavior remains unobserved; consume the mapped decision, localization, and completion audits and improvement-loop findings; and reconcile any remaining safe legacy callers against the final checklist.
