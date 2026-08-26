# Alien Infantry and the Empire of D’Rhonda

## Authority

This addendum is the binding design source for the reusable alien-infantry system, Doctor Warren Kruger’s D’Rhondan contact chain, the Event 019 provider-508 migration, and the Empire of D’Rhonda. It extends Event 016 without changing its minor fire-once opening, its exactly four logged evolutions, or its no-cluster status.

## Reusable alien infantry

The public unit identifier is `alien_infantry`, and its sole equipment family is `alien_laser_weapon_equipment`. Neither identifier is owned by Kruger or D’Rhonda, so future events may consume the same API, unit, equipment, counters, entity, actions, and sounds.

Each battalion has two combat width, zero human manpower, 40 HP, 90 organisation, 0.75 recovery, 10 reconnaissance, 0.50 initiative, five suppression, and 0.04 supply consumption. It requires exactly 200 laser weapons and no ordinary equipment. The only template created by the public API is the locked ten-battalion, twenty-width `D’Rhondan Landing Cohort`, which consumes exactly 2,000 laser weapons. The subunit remains inactive in the division designer, and the template cannot be recruited, duplicated, edited, or manually deployed.

Laser equipment has 0.98 reliability, 6.5 km/h speed, 60 defense, 40 breakthrough, 40 percent hardness, 30 armor, 30 soft attack, 20 hard attack, 80 piercing, 10 air attack, and 0.75 IC cost. It cannot be licensed or lend-leased.

The alien-only tactics are `tactic_alien_predictive_vector_assault` and `tactic_alien_probability_screen`. Both require `has_unit_type = alien_infantry`, the predictive-warfare technology, and the standard combat phase; ordinary formations cannot use them. Predictive Vector Assault uses selection factor four, grants the attacker 35 percent damage and 25 percent movement, reduces defender damage by 15 percent, and raises attacker-inflicted organisation damage by 30 percent. Probability Screen uses selection factor four, reduces attacker damage and attacker-inflicted organisation damage by 35 and 30 percent respectively, and raises defender damage by 30 percent.

The source-counted public API consists of `alien_infantry_grant_contact`, `alien_infantry_revoke_contact`, `alien_infantry_can_call_landing`, `alien_infantry_spawn_landing_cohort`, and `alien_infantry_reconcile_country`. Independent numeric receipts exist for the Kruger pact, Mengele expedition, Event 019 provider 508, D’Rhondan sovereignty, and future-event consumers. Revoking one receipt cannot revoke another source.

Successful landing history is owned by the country that completed the landing transaction. The API stores each selected state in that caller country's regular `alien_infantry_landing_state_registry` array after ordinary commit or Event 019 deferred-commit proof, and it never uses a shared global landing registry. D’Rhondan revolt capture and transfer iterate only the pact host's scoped registry, while receipt revocation removes future access without erasing committed landing history. Re-registering the same state for the same caller is idempotent, and separate callers or providers cannot contaminate one another's state history.

Event 019 retains provider and family ID 508. Its former training and manpower callbacks are replaced by shared contact and UFO-landing calls. Event 019 cleanup revokes only its own receipt.

## D’Rhondan contact

`sp_dhrondan_envoy_craft` is an air-specialization UFO project with breakthrough cost five, very-long prototype time, insane complexity, and five units each of aluminium, tungsten, chromium, and rubber. It requires operational Alien Arms, Rocketry, Advanced Materials, High-Energy, and Computation work. Access is limited to an active Kruger or KRG route, an eligible Mengele program, or an explicit future-event receipt.

An Event 025 Antarctic winner with `antarctica_success` may count the recovered craft as project completion for an active or later-appointed Kruger host. Event 036 remains evidence only. The project must be registered in every shared random Chaosx special-project selector; every future Chaosx special project must be added to those registries in the same change.

The 180-day Kruger expedition costs 50 political power and 500 fuel. It suspends and restores the canonical Kruger identity through the existing character-obligation system. Authorization grants Mandate 10, Dependence 10, Exposure 5, Independent Capacity 10, and Grievance minus 5. A successful return grants another five Mandate, Dependence, and Independent Capacity, establishes the pact once, and unlocks laser production and landing calls. All cleanup paths are exact and idempotent. Mengele receives a parallel program route without modifying Kruger’s Directorate variables.

The state-targeted landing decision reserves 2,000 laser weapons for seven days, permits one pending landing, and has a thirty-day base cooldown. DHR focus progression reduces only that post-landing recovery to 24 days with the restored landing network, 18 days with guarded descent windows, and 12 days after securing near space; every tier retains the same seven-day reservation and exact 2,000-gun cost. Losing the state cancels and refunds the reservation. Completion spawns one fully equipped cohort, marks the state, increases Alien Presence, adds five Pact Strain, and records persistent history. `Honor the D’Rhondan Accord` costs 75 political power, removes ten Pact Strain, and has a 180-day cooldown.

A country-scoped ninety-day rebellion pulse becomes available only after six arrivals, Pact Strain 30, and shared chaos 600. No world-iterating daily, weekly, or monthly on-action is permitted. Its revolt probabilities are ten percent for six or seven arrivals at chaos 600–799, twenty percent for eight or nine arrivals, Pact Strain 50, or chaos 800, and forty percent for at least ten arrivals while chaos is at least 800.

Events `chaosx.nr16.40` through `.47` own craft, expedition, pact, landing, failure, and rebellion follow-ups. They are not evolutions.

## Empire of D’Rhonda

`DHR` is a fixed dormant tag initialized idempotently. A revolt transfers every marked state still owned by the pact host, including disconnected enclaves. Host-controlled states switch controller; third-party occupations remain. Lost marked states become DHR claims. DHR cores are added without removing host cores, and the first viable marked state becomes the capital.

Surviving host alien formations are deleted without refund. The host laser stockpile transfers to DHR. The ordinary one-time expedition force is `max(5, min(15, marked_states + floor(arrivals / 2)))` locked cohorts. If more than fifteen disconnected viable landing components exist, the formation transaction grants and immediately consumes one additional 2,000-weapon reserve for each component beyond the fifteenth, solely so every enclave receives one cohort before any remainder concentrates at the capital. The exceptional cohort count and its equipment remain recorded separately from the ordinary capped grant. Later uprisings join an existing DHR, and reinitialization after annexation cannot duplicate the country, its characters, or the opening force.

The three mutually exclusive regimes are Emperor Vael IX’s non-aligned Imperial Continuity, First Calculant Sera Qel’s neutrality-mapped technocratic Synod with its own cosmetic identity, and Speaker Ilyr Ren’s democratic Two-World Covenant. The country has six distinct advisors or high-command figures and three alien commanders.

The DHR focus tree contains exactly 88 focuses: eight survival and landing-network focuses; 24 political focuses, eight per regime; ten laboratory-economy focuses; 12 alien-army and predictive-warfare focuses; eight orbital-logistics, air, and naval-support focuses; eight diplomacy and intelligence focuses; 12 expansion and world-order focuses; and six crisis and late-game focuses. DHR remains unable to train aliens normally. Every arrival still costs 2,000 laser weapons. At most three focus-created spirits may coexist: staged political, military, and off-world-corridor lifecycles.

## Assets and acceptance

The reusable model consumer is `alien_infantry_entity`. Its one Meshy input depicts a generic bald green alien with large black eyes, a charcoal retro uniform, grounded boots, and one readable retro-futurist laser pistol held upright in the right hand while the left arm hangs free, without Kruger or DHR markings. The production route uses Meshy 7 exclusively, vanilla infantry scale calibration, packed PDX materials, Blender PDX export and reimport, and genuine idle, move, laser-attack, defend, support-attack, retreat, and death actions. There is no separate UFO map model.

The package requires sourced laser-fire, movement, idle, and death audio; bespoke vanilla-green large and map counters; original equipment, hidden-technology, tactic, project, decision, event, achievement, focus, flag, and country-interface assets; and complete fictional DHR portrait packages. All references must be wired before acceptance.

Completion requires MCP comparisons for the technology, event, probability, focus, decision, and state-transfer surfaces; named scenario audits; an isolated improvement-loop pass; all mapped final auditors; Event 016 and Event 019 documentation; persistent-history and asset manifests; catalog workbook alignment; exported CSVs; model reimport evidence; and user-owned live acceptance.
