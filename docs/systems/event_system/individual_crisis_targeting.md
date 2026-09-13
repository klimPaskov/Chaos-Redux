# Individual crisis targeting

## Purpose

The individual crisis targeting layer prevents a country from receiving more than three independently assigned crisis or special-mechanic packages at the same time.

The rule applies to automatic and scenario selectors that choose one country or a bounded group of countries.

World-scale packages that apply to every eligible country remain outside this system, do not consume a slot, and keep their existing selection and application behavior.

## Selection curve

The shared tuning lives in `common/script_constants/individual_crisis_targeting_constants.txt`.

| Active individual packages | Normalized event factor | Candidate ticket multiplier | Result |
| ---: | ---: | ---: | --- |
| 0 | 1.00 | 4 | Full selection pressure |
| 1 | 0.50 | 2 | Half selection pressure |
| 2 | 0.25 | 1 | Quarter selection pressure |
| 3 or more | 0.00 | 0 | Ineligible until a package resolves |

Candidate selectors multiply their existing package-owned score by the shared ticket multiplier, so geography, ideology, strength, and other owner scoring retain their relative meaning.

Fixed-target packages are reserved for a separate event-pool adapter because their target is chosen by the owning package rather than by a country candidate pool.

The current source has the candidate-ticket contract wired, but the fixed-target adapter is not yet declared or consumed. Until that adapter is restored and compared through the probability workflow, fixed-target package weights must not be described as load-adjusted runtime behavior.

The hard cap is also present in the package eligibility trigger so direct, manual, or delayed selector routes cannot bypass it.

## Derived active load

`individual_crisis_load_is_below_cap` rebuilds the current load from the lifecycle markers already owned by each event package.

The shared layer does not maintain a second persistent counter, so winning, losing, expiry, cleanup, ownership loss, and other package-specific endings immediately affect the next selection without a reconciliation job.

| Package | Active provider |
| --- | --- |
| Holy Realm | `holy_realm_active` |
| Soviet Collapse | `soviet_collapse_active_origin` |
| Fury | `fury_actor` |
| Secret Alliance | `secret_alliance_target_country` or `secret_alliance_active_member` |
| Natural Disasters | The queue, chain mission, warning state, or aftermath state remains active |
| Utopia Manifesto | `utopia_manifesto_accepted` |
| Brilliant Scientist | `brilliant_scientist_current_host` |
| Resources Found | `resources_found_field_system_participant` or an active controlled resource field |
| Random Civil War | `random_civil_war_active` |
| Video Game in Sweden | `video_game_in_sweden_program_active` |
| Riches Found | A controlled state has an active mine |
| Time Traveler | The short prefire reservation or timed `time_traveler` idea is present |
| Random Terror | `random_terror_affected_country` or an active controlled terror state exists |
| Murder Mystery | The global runtime is active and the country is the original host |

Secret Alliance founder, recruit, and sponsor selection uses the same capacity gate and pressure curve because membership applies the bounded system to those countries as well as to the headline target.

Natural Disaster remains one slot throughout warning, impact sequencing, chain missions, and aftermath cleanup, rather than ceasing to count as soon as the initial impact lands.

Random Terror follow-up waves and scenario phases may continue an already active Random Terror package without requesting another slot.
Their weighting removes that current provider once and still applies pressure from every other active individual package.

## Integrated target routes

Weighted country pools use `adjust_individual_crisis_candidate_ticket_weight` after their existing owner score in Holy Realm, Fury, Secret Alliance recruitment, Utopia Manifesto, Brilliant Scientist initial and send-away recipient selection, Random Civil War, Video Game in Sweden fallback host selection, Riches Found, Time Traveler, Random Terror, and Murder Mystery.

Bounded triggerable scenarios use the same curve: Fury retains its continent and country-size passes for both triggerable and world-end continental seeds, Random Civil War retains its intensity-derived unique-country budget, and Random Terror retains its scenario target count while drawing each new country from load-sensitive tickets.

The central event picker does not currently consume `apply_individual_crisis_fixed_target_event_pressure`.
That companion remains a separately scoped follow-up whose first consumer must declare its explicit country scope and event-pressure input and output.
The previously listed packages require current owner-side target classification before migration.
Holy Realm prefers eligible Tibet, then selects a Bhutan or Nepal refuge host when Tibet does not exist, while Video Game in Sweden resolves its host through owner-side prefire selection.
Neither selection path proves that the central event picker already has a fixed target available.
The weighted picker evaluates each candidate in both the total-weight and running-weight passes, so a target resolver used there must remain consistent across both passes without selecting randomly or changing package state.
The blocked architecture contract, smallest next integration change, and validation limits are recorded in [the fixed-target companion handoff](../../plans/021_random_civil_war_plans/subagent_handoffs/individual_crisis_fixed_target_contract_2026-09-13.md).

Natural Disaster automatic and Disaster Barrage routes, Resources Found and Riches Found direct-entry routes, Video Game in Sweden, and the other package-owned preflight routes recheck capacity before accepting their final target.

Time Traveler resolves an eligible weighted host before the fire-once history record is accepted, and its short prefire flag reserves the slot until the timed idea is applied, so an empty eligible pool does not consume the event and the one-day report delay cannot admit a fourth package.

## Global exemptions

Zombie Uprising, Independence Wave, Tensions Rising, Sudden Death, Africa, Cannibalism, Black Plague, Black Friday, Doctrine Research, Asteroid Incoming, and Acid Rain remain exempt because their core application is global or all-eligible rather than an independently assigned bounded country package.

A country at the individual cap can still receive effects from these global systems.

## Runtime sequence

1. A bounded event candidate enters the normal event-pool or package preflight path.
2. The proposed country derives its active load from owner lifecycle markers.
3. Load zero, one, or two scales the existing selection weight by the shared curve.
4. Load three produces zero tickets and fails the capacity trigger.
5. When an owning package clears its marker, timed idea, active state, or runtime flag, the derived load falls automatically and the country can become eligible again.

## UI, localisation, and assets

This is an invisible event-selection rule and adds no player-facing name, tooltip, decision, or scripted GUI surface.

No localisation keys, icons, sprites, DDS files, or interface registrations are required.

## Future extensions

New bounded country packages should expose one authoritative active-provider trigger or marker, add that provider to the shared load derivation, gate every first-application route, and apply the shared pressure after their owner-specific candidate score.

If a future package can be active in several internal phases, its provider should combine those phases into one slot instead of counting each phase separately.

If a package changes from bounded assignment to an all-eligible global application, its provider and selector integration should be removed together so it becomes a documented global exemption.
