# Holy Realm Buddhahood Focus Tree Completion Plan

## Scope

This plan covers the gap between the current `THR_focus` implementation and the accepted Buddhahood focus-tree spec. It does not authorize a whole-tree rewrite by a focus audit subagent; it is a handoff for the main implementation pass.

## Current State

`common/national_focus/003_holy_realm.txt` contains 98 `THR_` focus ids and a working older Holy Realm route built around refuge survival, Bodhisattva/Arhat stages, Mandala expansion, restraint versus Final Silence, regional conquest/registration, anti-chaos Buddhahood powers, and the hidden False Buddha Schism outcomes. It also hooks into Buddhahood systems through `THR_buddha_mandate`, which is localized as `The Unshaken Seat`, and through decisions in `common/decisions/003_holy_realm_decisions.txt`.

The current tree still does not fully implement the accepted Buddhahood-first route family. The required route list is in `docs/specs/003_holy_realm_buddhahood_specs/specs/holy_realm_buddhahood_focus_tree.md`, especially the coverage table at lines 302-320.

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

The third route-lock tranche is implemented in `common/national_focus/003_holy_realm.txt` and the shared Schism-resolution helpers:

- Hidden Schism branch: `THR_debate_the_pretender_focus`, `THR_exile_the_echo`, `THR_break_false_mandala`, and `THR_absorb_the_shadow` are hidden through `allow_branch` until `holy_realm_false_buddha_schism_triggered` exists.
- Schism refresh: `holy_realm_trigger_false_buddha_schism` marks the focus tree layout dirty after recording the evolution so the branch can appear in a live session.
- Shared outcomes: the existing debate and suppression decisions now call the same scripted effects used by the focus branch. Exile ends immediate pressure while leaving `holy_realm_false_buddha_echo_abroad`; absorption is Totalen Chaos-gated and records `holy_realm_corrupted_buddhahood_route`.

## Missing Route Architecture

Implement these as focus-tree work, not only as decisions:

1. Teaching route follow-up: add more downstream teaching payoffs and mission-slot variety beyond the route-lock chain.
2. Meditation route follow-up: add later Dhyana payoffs, stronger interaction with `meditation_charge`, and visible post-Buddhahood meditation use beyond the route-lock chain.
3. Governance route follow-up: let Council of Abbots, Protector Regent, and Pilgrim Assembly affect later teaching, defense, refugee, and compact tools.
4. Sanctuary logistics: reshape existing generic whole-country construction focuses into named sanctuary logistics: granaries, pilgrimage roads, clinics, workshops, storehouses, and supply support for allies/compact members.
5. Guardian military: turn `THR_vow_keeper_regiments` and support nodes into a defensive guardian route with temple guards, pilgrimage escorts, mountain pass detachments, and anti-chaos defensive doctrine.
6. Sangha Compact diplomacy: either rename and formalize the current `Mandala of Nations` as the accepted compact equivalent, or add a separate Sangha Compact lane with membership rules, cohesion, shared decisions, refusal/exit risks, and anti-puppet clauses.
7. Expansion/liberation: replace broad ordinary annexation/registration rhetoric with the spec's pilgrimage and liberation framing where appropriate. Keep hard conquest as a corrupted/high-chaos route if retained.
8. Anti-chaos powers follow-up: add dedicated `Read the Pattern of Suffering`, `Vanishing from Sight`, and `Seated in the Sky` focuses if the route needs one focus per named power rather than grouped power lanes.
9. Final Silence follow-up: add more aftermath mechanics behind `THR_empty_seat` and stronger witness reactions from taught countries or compact members.
10. Hidden Schism follow-up: branch visibility and all four outcome focuses are implemented. Remaining work is only future-depth material, such as making `holy_realm_false_buddha_echo_abroad` return through a foreign crisis if that route needs a later incident.

## Recommended Implementation Order

1. Add route locks and bridge focuses for teaching, meditation, and governance first, because they gate Buddhahood requirements.
2. Rework AI weights around those route locks before adding late branches.
3. Add Sangha Compact and anti-chaos power focus branches next, reusing existing decision categories and flags.
4. Align Final Silence sequence last, preserving existing terminal/non-terminal decision gates.
5. Run focus, localisation, decision, and AI audits after the new route families are implemented.

## Boundaries

Do not remove the existing Holy Realm mechanics wholesale. Reuse the existing Buddhahood decisions, Mandala GUI, Buddha powers, Final Silence gates, and achievement hooks. The missing work is focus-route visibility, branch pacing, route interaction, and AI behavior.
