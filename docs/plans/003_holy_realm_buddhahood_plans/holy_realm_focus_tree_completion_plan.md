# Holy Realm Buddhahood Focus Tree Completion Plan

## Scope

This plan covers the gap between the current `THR_focus` implementation and the accepted Buddhahood focus-tree spec. It does not authorize a whole-tree rewrite by a focus audit subagent; it is a handoff for the main implementation pass.

## Current State

`common/national_focus/003_holy_realm.txt` contains 111 Holy Realm focus blocks and a complete Holy Realm Buddhahood route built around refuge survival, teaching, Dhyana meditation, mutually exclusive governance choices, Arhat administration, sanctuary logistics, guardian defense, Sangha Compact diplomacy, pilgrimage-protection expansion, anti-chaos Buddhahood powers, Final Silence, Empty Seat aftermath, and the hidden False Buddha Schism outcomes. It hooks into Buddhahood systems through `THR_buddha_mandate`, which is localized as `The Unshaken Seat`, and through decisions in `common/decisions/003_holy_realm_decisions.txt`.

The route-coverage evidence is recorded in `docs/events/003_holy_realm.md` under `Focus Route Coverage`. The required route list remains in `docs/specs/003_holy_realm_buddhahood_specs/specs/holy_realm_buddhahood_focus_tree.md`.

## Implemented Tranche - 2026-06-11

The first route-lock tranche is implemented in `common/national_focus/003_holy_realm.txt`:

- Teaching route: `THR_send_first_envoys`, `THR_translation_houses`, `THR_teach_under_bombardment`, and `THR_many_lamps_one_flame`. `Many Lamps, One Flame` reads `teaching_successes` and `crisis_teaching_successes`.
- Meditation route: `THR_sit_beneath_prayer_flags`, `THR_first_quiet`, `THR_second_quiet`, `THR_third_quiet`, and `THR_fourth_quiet`. The quiet focuses read `dhyana_depth`.
- Governance route family: `THR_council_of_abbots`, `THR_name_protector_regent`, and `THR_seat_pilgrim_assembly` are mutually exclusive route choices and set governance flags.
- `THR_buddha_mandate` requires the completed teaching gate, fourth quiet gate, and one governance choice in addition to the older Arhat/industry/military/diplomacy prerequisites.
- Holy Realm-specific focus filters now cover Bodhi, Teaching, Meditation, Governance, Sanctuary, Compact, Anti-Chaos, Nirvana, and Hidden branches.

The second route-lock tranche is implemented in `common/national_focus/003_holy_realm.txt` and the shared power charge logic:

- Post-Buddhahood sequence: `THR_the_awakened_one` and `THR_show_the_powers` make Buddhahood and the first anti-chaos power display visible in the tree.
- Anti-chaos powers branch: `THR_powers_are_not_toys`, `THR_one_becomes_many_focus`, `THR_path_through_walls`, `THR_lotus_bridge_focus`, and `THR_touch_sun_moon_focus` add focus-gated power pacing and route flags.
- Disciplined power use: `holy_realm_power_restraint_doctrine` lowers ordinary Buddha power Meditation Charge cost from `20` to `15` while keeping the existing `is_special_chaos_country` target gate.
- Final sequence alignment: `THR_doctrine_last_war` is localized as `The Last Wheel` and requires `THR_show_the_powers`; `THR_witnesses_gather` and `THR_extinction_of_defilements_focus` gate `THR_final_silence`; `THR_empty_seat` covers the non-terminal aftermath focus.
- Empty Seat aftermath: `THR_witnesses_keep_the_record` follows `THR_empty_seat` and makes taught countries, Mandala mission hosts, observer hosts, development hosts, and valid compact members react to the non-terminal Final Silence outcome.

The third route-lock tranche is implemented in `common/national_focus/003_holy_realm.txt` and the shared Schism-resolution helpers:

- Hidden Schism branch: `THR_debate_the_pretender_focus`, `THR_exile_the_echo`, `THR_break_false_mandala`, and `THR_absorb_the_shadow` are hidden through `allow_branch` until `holy_realm_false_buddha_schism_triggered` exists.
- Schism refresh: `holy_realm_trigger_false_buddha_schism` marks the focus tree layout dirty after recording the evolution so the branch can appear in a live session.
- Shared outcomes: the existing debate and suppression decisions now call the same scripted effects used by the focus branch. Exile ends immediate pressure while leaving `holy_realm_false_buddha_echo_abroad`; absorption is Totalen Chaos-gated and records `holy_realm_corrupted_buddhahood_route`.

The fourth route-integration tranche formalizes the existing Mandala of Nations as the Sangha Compact implementation:

- `thr_joining_rule_mandala_peace_only` now uses `holy_realm_sangha_compact_candidate_valid`, blocking special chaos countries, puppet/subject entrants, majors, existing faction members, offensive-war states, and countries without a chaos threat, teaching history, observer/development contact, or Pilgrim Assembly humanitarian opening.
- `holy_realm_mandala_of_nations_member_joined` rejects invalid members, fires compact refusal notices, and applies a Sangha Cohesion loss instead of letting them count toward the achievement/watch state. Members leaving after receiving the Peace Vow fire a compact exit notice and refresh member validity.
- `holy_realm_refresh_sangha_of_nations_status` counts only `holy_realm_sangha_compact_member_valid` members toward the eight-member high-cohesion requirement.
- `THR_mandala_demand_anti_puppet_clauses` adds the requested anti-puppet compact action, removes hard-invalid members, refreshes member validity, and improves Sangha Cohesion.
- `THR_mandala_joint_defense_of_passes` adds a crisis defense compact action and faction goal, available only during true chaos threats to the Realm, its neighbors, or the compact. It spends command capacity and support equipment, improves compact initiative/projection, raises Sangha Cohesion, and sends defensive support to valid compact members.
- `holy_realm_apply_sangha_governance_bonus` makes Council, Protector Regent, and Pilgrim Assembly choices alter compact actions: Council adds political capacity/cohesion, the Assembly adds refugee manpower/cohesion, and the Regent adds command capacity while straining cohesion and raising Defilements.

The fifth anti-chaos power tranche expands the post-Buddhahood power branch:

- `THR_read_pattern_suffering` gives Pattern of Suffering its own route focus, tied to the existing evolution, chaos enemies, or teaching evidence.
- `THR_vanishing_from_sight_focus` and `THR_seated_in_sky_focus` give Vanishing from Sight and Seated in the Sky dedicated focus payoffs.
- `THR_touch_sun_moon_focus` now requires the full named-power lattice: Pattern, One Becomes Many, Path through Walls, Lotus Bridge, Vanishing from Sight, and Seated in the Sky.

The sixth guardian-route tranche reframes and caps the existing military support branch:

- `THR_shelters_under_stone` is now the player-facing `Fortress Without Hatred`, matching the fort and anti-air sanctuary defense role.
- `THR_quiet_mobilization` is now `Mountain Pass Detachments`, matching the defensive reserve and pass-watch role.
- `THR_mountain_artillery_mandalas` is now `The Bell and Rifle`, framing artillery as guardian support rather than conquest.
- `THR_unbroken_pass` is the anti-chaos defensive capstone, gated by chaos pressure, active special-chaos enemies, or a recent capital-sanctuary fall, and applies `holy_realm_last_pass_mobilization`.

The seventh sanctuary-logistics tranche makes the economic support route map-facing:

- `THR_count_mountain_roads` is now player-facing `Pilgrimage Roads`, retaining its infrastructure and listening-post work.
- `THR_monastic_labor_vows` is now `Monastery Workshops`, retaining its civilian workshop and infrastructure role.
- `THR_mountain_granaries` adds high-valley infrastructure and a supply node behind the road route.
- `THR_snowline_clinics` adds support equipment, infrastructure, stability, Compassion, and relief Chaos reduction.
- `THR_storehouses_for_world` adds a supply node, Command Power, and, when the Mandala of Nations exists, compact-member infrastructure aid and Sangha Cohesion.

The eighth teaching-depth tranche adds staged mission capacity:

- `THR_four_teaching_seats` branches after `THR_many_lamps_one_flame`, expands active teaching mission capacity from three to four, and opens late foreign teaching tools.
- `holy_realm_has_open_teaching_slot`, `holy_realm_start_teaching_mission_slot`, and `holy_realm_finish_teaching_mission_slot` make teaching missions occupy a timed seat until their decision timer expires.
- Translation House work now stages distant visits and foreign officer teaching. Teach under Bombardment stages collapsing-capital visits. `THR_four_teaching_seats` stages follow-up letters, Mandala missions, foreign pilgrims, and sympathetic-government support.
- Buddhahood, One Becomes Many, or the One Becomes Many focus raises the active teaching cap to five.

The ninth meditation-depth tranche extends Dhyana after Buddhahood:

- `THR_return_to_the_seat` branches from `The Awakened One`, adds a post-Buddhahood meditation payoff, and unlocks the emergency vow loop.
- `THR_renew_vow_under_fire` requires the awakened meditation seat, the fourth Dhyana, capital control, a true chaos threat to the Realm, a neighbor, or a compact ally, Command Power, and support equipment. It restores Meditation Charge faster than the standard concentration sequence, adds Detachment, lowers Defilements, and records Wrathful Protection readiness.

The tenth governance-depth tranche gives each governance choice a later route hook:

- `THR_abbot_examiners` lets Council of Abbots governance open the fourth active teaching seat before `THR_four_teaching_seats`, adding teaching-route Bodhi and Compassion.
- `THR_regent_pass_watch` gives Protector Regent governance a defensive follow-up with Command Power, support equipment, capital-pass fortification, anti-air, and a small Defilements cost.
- `THR_pilgrim_refuge_courts` lets Pilgrim Assembly governance widen the low-stability humanitarian compact path and adds refugee manpower, Mandala Reach, and Sangha Cohesion.

The eleventh expansion-framing tranche separates pilgrimage protection from coercive conquest:

- The lower borderland branch now uses player-facing pilgrimage, petition, corridor, and protection-ledger language instead of broad ordinary annexation or submission language.
- `THR_letters_beyond_passes` records `holy_realm_pilgrimage_protection_route` for audit and future decision/event hooks.
- `THR_world_is_a_border` remains the explicit high-chaos coercive capstone, so hard expansion is still available only as a darker route rather than the default branch identity.

The twelfth guardian-mission tranche ties the guardian route to an active pilgrimage escort objective:

- `THR_vow_keeper_regiments` now unlocks `THR_bodhisattva_guard_pilgrimage_route`.
- The escort mission is a state-targeted timed mission for controlled core, protected, integrated, Himalayan, or low-infrastructure route states. It consumes an active teaching seat, spends Command Power and support equipment, requires at least two divisions in the selected state, and succeeds only if the route remains controlled and guarded through the timer.
- Success marks the route guarded for later pacing, adds route infrastructure, and rewards Bodhi, Compassion, Sangha Cohesion, Mandala Reach, and Army Experience. Failure or cancellation raises Defilements and lowers Sangha Cohesion.

The thirteenth Schism-reactivity tranche gives the exiled echo a foreign return path:

- `THR_answer_false_buddha_echo_abroad` appears after `THR_exile_the_echo` has left `holy_realm_false_buddha_echo_abroad` active.
- The decision targets foreign countries with prior Bodhisattva contact, a Mandala mission, a collapse visit, war pressure, or low stability. It fires `chaosx.nr3.131` in the host country.
- A host that contains the echo clears the abroad echo and rewards Detachment, lower Defilements, and Mandala Reach. A host that shelters it records `holy_realm_false_buddha_foreign_crisis`, raises Defilements and Final Silence Pressure, and leaves the echo unresolved.

## Route Architecture Completion

These route families are implemented as focus-tree work, with decisions used only for active mission and action surfaces:

1. Teaching route follow-up: downstream mission-slot variety is implemented through `THR_four_teaching_seats` and the active teaching-seat cap. Remaining future-depth work is only additional mission-family outcomes if later balance wants more target-specific success/failure events.
2. Meditation route follow-up: `THR_return_to_the_seat` and `THR_renew_vow_under_fire` now add a post-Buddhahood Dhyana payoff, stronger `meditation_charge` interaction, and visible emergency meditation use. Remaining future-depth work is only additional failure events or ordinary-war abuse consequences if later balance wants more risk.
3. Governance route follow-up: `THR_abbot_examiners`, `THR_regent_pass_watch`, and `THR_pilgrim_refuge_courts` now let Council of Abbots, Protector Regent, and Pilgrim Assembly affect later teaching, defense, refugee, and compact tools. Remaining future-depth work is only route-specific failure events or AI balance tuning if later audits show one governance route dominates.
4. Sanctuary logistics: implemented as Pilgrimage Roads, Monastery Workshops, Mountain Granaries, Snowline Clinics, and Storehouses for the World. Remaining future-depth work is only state-group specificity if a later map pass wants named Himalayan subregions instead of all controlled states.
5. Guardian military: `THR_vow_keeper_regiments` and its support nodes now form a defensive guardian route with Fortress Without Hatred, Mountain Pass Detachments, The Bell and Rifle, The Unbroken Pass, and the active `Guard the Pilgrimage Route` timed escort mission. Remaining future-depth work is only optional Temple Guard naming if the unit template needs a second non-mountaineer identity.
6. Sangha Compact diplomacy: the current `Mandala of Nations` is now formalized as the accepted compact equivalent with membership rules, cohesion checks, shared decisions, invalid-member rejection notices, member exit notices, anti-puppet clauses, and a crisis-only joint defense act. Remaining future-depth work is only deeper member-specific diplomatic aftermath if later audits need more reactivity.
7. Expansion/liberation: lower borderland and regional integration focuses now use pilgrimage, petition, corridor, and protection-ledger framing, while `THR_world_is_a_border` remains the explicit high-chaos coercive capstone. Remaining future-depth work is route-specific liberation events or refusal outcomes if later audits need more reactivity.
8. Anti-chaos powers follow-up: dedicated `Read the Pattern of Suffering`, `Vanishing from Sight`, and `Seated in the Sky` focuses are implemented. Remaining future-depth work is only power-specific decision upgrades if balance requires more than route flags and charge/virtue rewards.
9. Final Silence follow-up: `THR_witnesses_keep_the_record` now adds aftermath mechanics behind `THR_empty_seat` and turns taught countries, Mandala-contact states, and valid compact members into Empty Seat witnesses. Remaining future-depth work is only event-text variants or longer reconstruction chains if later audits need more reactivity.
10. Hidden Schism follow-up: branch visibility, all four outcome focuses, and the exiled echo foreign incident are implemented. Remaining future-depth work is only additional country-specific crisis variants if later audits need more reactivity.

## Implemented Order

1. Added route locks and bridge focuses for teaching, meditation, and governance first, because they gate Buddhahood requirements.
2. Reworked focus AI weights around those route locks before adding late branches.
3. Added Sangha Compact and anti-chaos power focus branches next, reusing existing decision categories and flags.
4. Aligned the Final Silence sequence last, preserving existing terminal/non-terminal decision gates.
5. Recorded route coverage in the canonical event doc after the route families were implemented.

## Boundaries

Do not remove the existing Holy Realm mechanics wholesale. Reuse the existing Buddhahood decisions, Mandala GUI, Buddha powers, Final Silence gates, and achievement hooks. The missing work is focus-route visibility, branch pacing, route interaction, and AI behavior.
