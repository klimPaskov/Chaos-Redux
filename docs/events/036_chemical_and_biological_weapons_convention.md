# Event 036 - Chemical and Biological Weapons Convention

Event 036 is a Chaos level 1 Minor Fire-Once diplomatic event rooted at `chaosx.nr36.1`.
Governments sign a convention that makes chemical and biological warfare ordinary state policy.
Every eligible country takes a public posture, a conference returns every few months with a new treaty to ratify, three evolutions widen what members may do, and a late research program opens event-gated weapon projects.
The event is registered in `global.fire_once_events`, belongs to the reworked default-enabled set, and is a High member of the Diplomacy cluster (cluster 3, still under the `diplomatic_panic` constant names).
The specification is `docs/specs/036_chemical_and_biological_weapons_convention_specs/`.

## Files

| File | Owns |
| --- | --- |
| `events/036_chemical_and_biological_weapons_convention.txt` | Entry, opening response, agenda, response and resolution reports, evolution report, program reports, consequence reports, news |
| `common/scripted_effects/036_cbrn_convention_effects.txt` | Opening, postures, Standing, scheduler, agendas, treaties, evolutions, covert program, Condemnation adapters, program |
| `common/scripted_triggers/036_cbrn_convention_triggers.txt` | Posture, treaty, capability, program and eligibility predicates |
| `common/script_constants/036_cbrn_convention_constants.txt` | Every tuning value |
| `common/mtth/036_cbrn_convention_mtth.txt` | AI opening and ratification weights, agenda pool weights, evolution timing |
| `common/decisions/036_cbrn_convention_decisions.txt` and `categories/036_cbrn_convention_categories.txt` | Posture, conference, obligation and contribution decisions and missions |
| `common/ideas/036_cbrn_convention_ideas.txt` | Three posture ideas and integrated doctrine |
| `common/scripted_localisation/036_cbrn_convention_scripted_localisation.txt` | Category header, family and project wording, projected Condemnation tiers |
| `localisation/english/036_cbrn_convention_l_english.yml` | All player-facing text |
| `interface/036_cbrn_convention.gfx` | Category icon, decision icons, idea icons, achievement sprites |

## How it works

1. **Opening.** The entry runs `cbrn_convention_open` once. One bounded `every_country` pass sends the response event to every eligible human and resolves every AI through the five opening weights. Standing, the coordinator and the Opposition Leader are calculated, the opening Chaos is added (`+3` for a weak order, `+5` for a strong one), the History row is given the coordinator as its actor, and the first agenda is queued 90 to 180 days out.
2. **Postures.** Full Ratification, Chemical Accession Only, Retaliation Reservation, Public Rejection, with a covert program as a flag on Public Rejection. `cbrn_convention_set_posture` is the one transaction that changes the registry, the posture idea, ratifications, doctrine and Standing. The timeout answer of a human is Retaliation Reservation.
3. **Opening normalization.** The country's public chemical and biological Condemnation buckets fall once after the posture is recorded, and the option tooltips show the tier the country will land in.
4. **Conferences.** The coordinator runs one self-rescheduling pulse (`chaosx.nr36.80`, every 30 days) that reads only the registries. An agenda picks a family from a weighted pool, opens a 60 to 120 day negotiation (Sponsor, Lobby, Organize Opposition), then collects Ratify, Ratify with reservation or Decline from every voting member. The treaty enters force at quorum, otherwise it enters a 180 or 365 day cooldown.
5. **Treaty families.** Ten, each with a distinct effect: Protection and Assistance Compact (guarantee mission, decontamination access), Chemical Production Articles and Biological Laboratory Registry (declaration missions), Inspection and Verification Protocol (inspection demands between ratifiers, suspension for refusal), First-Use Revision (chemical and biological clauses), Missile and Delivery Cooperation Accord, Strategic WMD Doctrine Charter (Doctrine Integration), Nuclear Materials and Targeting Accord, Arsenal Without Limits Articles, and the International Chaos Weapons Program Charter.
6. **Evolutions.** First Use Becomes Acceptable (200+ Chaos), Strategic WMD Doctrine (400+), The Arsenal Without Limits (600+), rolled by MTTH from the pulse, recorded through the shared evolution context, and accelerated in order when the event first fires at high Chaos. They change no Chaos.
7. **Program.** After the Charter is in force, one project at a time is chosen with exactly equal probability among registered providers, filled by member contributions (industry, research, equipment, facility), and paused if the Charter ratifiers fall below the Arsenal quorum. Completion grants only an access flag to contributors.

## Condemnation integration

Relief applies to the weapon base of an eligible new public source and nothing else.
`condemnation_add_source` calls `cbrn_convention_apply_condemnation_relief` after the weapon-use classification and before the death and contamination terms, so civilian deaths, contamination, evidence and cover-up keep their full value.
The relief multiplier comes from the posture and the highest held stage (Baseline, First-Use clause, integrated doctrine or Nuclear Accord, Arsenal Without Limits).
Floors: biological outbreaks never below `0.70`, nuclear strikes against a capital or a state above the 20 million band never below `0.80`, and the product of doctrine mitigation and relief never below `0.10` chemical, `0.20` biological, `0.50` nuclear.
The existing public-harm floors for confirmed strategic and mass-casualty chemical actions are applied again after relief.
No relief for thermonuclear use, Final Silence, doomsday, atrocity, cover-up, camp or inspection contexts.

Retaliation is read from the Retaliation Authority ledger (`cbrn_retaliation_<id>_expiry_day`) while the countries are at war.
A Retaliation Reservation member that uses a weapon without that right, or selects a broader use policy, breaks its reservation once: source relief is skipped, `condemnation_apply_pledge_breach_consequence` (the shared pledge-breach helper, now also used by the non-use pledge) records the 365-day memory with its cover-up and repeat-use gain, and the country is suspended.
`condemnation_calculate_pair_score` calls `cbrn_convention_add_participant_score_term`: members scoring a member's policy-compatible use are less willing to sanction it, reservation members scoring a first use and public opponents scoring any member use are more willing.

## Shared-system hooks

| Shared owner | Hook |
| --- | --- |
| `condemnation_add_source` | Relief adapter and the shared pledge-breach helper |
| `condemnation_calculate_pair_score` | Participant-score term |
| `cbrn_diplomacy_grant_retaliation_right_against_offender` | `cbrn_convention_on_member_attacked` (emergency agenda, Compact guarantees) |
| `cbrn_target_can_receive_inspection_demand_from_root` | Protocol ratifiers can inspect each other without Formal Censure |
| `cbrn_state_can_receive_international_decontamination_from_root` and the retain trigger | Compact partners count as valid decontamination access |
| `condemnation_accept_inspections`, `condemnation_refuse_inspections` | Covert exposure on acceptance, suspension for a Protocol ratifier that refuses |
| `cbrn_change_chaos_warfare_use_policy` | Reservation breach when the policy becomes broader than Retaliation Only |
| `cbrn_diplomacy_complete_international_decon_mission` | Fulfils an Assistance Guarantee |
| `chaos_meter_register_nuclear_condemnation` | Marks capital and top-band targets for the nuclear floor |
| `black_plague_weaponization_directorate_has_access`, `weaponize_the_zombies` `visible` | Program access flags `cbrn_convention_access_black_plague` and `cbrn_convention_access_weaponized_zombies` |
| `black_plague_initialize_runtime`, the zombie outbreak entry and `trigger_zombie_apocalypse_scenario` | Cancellation calls `cbrn_convention_on_black_plague_route_opened` and `cbrn_convention_on_zombie_route_opened` |

The Mengele directorate pattern is the precedent for the access flags: a grant never fires, advances or records the source event, and a country that already has access through another route is skipped.

## Decisions

One ordinary category, `cbrn_convention_category`, shown to countries with a posture. The description carries three lines: posture with its permission line, Standing, and the agenda (ratifications against quorum and days left) or the active project (stage, percent, whether the country contributed).
Posture: Seek Accession (and the Accession Review mission), Revise Posture, Begin Withdrawal (and the Withdrawal Notice mission), Begin, Expand and End Covert Program.
Conference: Sponsor the Agenda, Lobby for Ratification, Organize Opposition.
Obligations: File Declarations (Declaration Deadline mission), Send Protective Equipment (Assistance Guarantee mission), Begin Doctrine Integration (Doctrine Integration mission).
Program: Dedicate Industrial Capacity, Assign Research Teams, Provide Specialist Equipment, Host a Testing Facility.
Evidence, inspections, decontamination aid and use policy stay in the existing CBRN decisions.

## AI

Opening posture, treaty response and every decision use `common/mtth/036_cbrn_convention_mtth.txt` or `ai_will_do` with constants from `cbrn_convention_ai`.
A capable, industrial or warring country leans to Full Ratification, a chemical-only power to Chemical Accession, a threatened minor or democracy to Retaliation Reservation, a peaceful unarmed country to Public Rejection, and a few strong non-democracies to a covert program.
Ratification starts at `45` percent and moves with war, capability, a recent attack and negotiation pressure from lobbying and opposition.

## Achievements

`036_the_reservation_holds`, `036_a_convention_against_the_convention` and `036_small_state_large_ledger`, each with the three image states under `gfx/achievements/` and sprite aliases in `interface/036_cbrn_convention.gfx`.
Tracking flags: `cbrn_convention_achv_reservation_track/lost/proven`, `cbrn_convention_achv_opposition_track/lost/proven`, `cbrn_convention_small_state_proof`.

## Alien Spacecraft

Slot 36 used to hold the Alien Spacecraft stub.
Its jet recovery now lives in Event 025 as the Forerunner Craft (`chaosx.nr25.260` and `.261`), fired once the race has its entrants, and keeps the `chaosx_alien_recovery_event036_*` receipts, `global.chaosx_alien_recovery_event036_recoverers` and `brilliant_scientist_alien_spacecraft_recovered` that Event 016 and the Event 025 ledger read.
Its report art and news picture moved to `gfx/event_pictures/025_alien_technology_in_antarctica/`.

## Icons and assets

Sprites are defined in `interface/036_cbrn_convention.gfx`.

| Sprite | File |
| --- | --- |
| `GFX_decision_category_cbrn_convention` | `gfx/interface/decisions/036_chemical_biological_weapons_convention/categories/cbrn_convention_category.dds` |
| `GFX_decision_cbrn_convention_<name>` (12) | `gfx/interface/decisions/036_chemical_biological_weapons_convention/decision_<name>.dds` |
| `GFX_idea_cbrn_convention_<name>` (4) | `gfx/interface/ideas/036_chemical_biological_weapons_convention/idea_<name>.dds` |
| `GFX_achievement_036_<id>` with `_grey` and `_not_eligible` | `gfx/achievements/036_<id>.dds` |

## Future plans

- Event 076 USA Tests Weapons could read the United States' posture so a Full Ratification test is a declared trial and a Reservation or Rejection test counts as hidden program evidence.
- More providers can join the program by supplying an access flag, a global normal-route proof and a cancellation call.
- The remaining spec achievements (The Secret Article, Masks Before Missiles, All Articles Invoked, Without the Incident) can be added on the existing flags.
