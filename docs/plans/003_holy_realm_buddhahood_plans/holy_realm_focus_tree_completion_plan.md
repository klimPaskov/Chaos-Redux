# Holy Realm Buddhahood Focus Tree Completion Plan

## Scope

This plan covers the gap between the current `THR_focus` implementation and the accepted Buddhahood focus-tree spec. It does not authorize a whole-tree rewrite by a focus audit subagent; it is a handoff for the main implementation pass.

## Current State

`common/national_focus/003_holy_realm.txt` contains 85 `THR_` focus ids and a working older Holy Realm route built around refuge survival, Bodhisattva/Arhat stages, Mandala expansion, restraint versus Final Silence, and regional conquest/registration. It also hooks into Buddhahood systems through `THR_buddha_mandate`, which is localized as `The Unshaken Seat`, and through decisions in `common/decisions/003_holy_realm_decisions.txt`.

The current tree still does not fully implement the accepted Buddhahood-first route family. The required route list is in `docs/specs/003_holy_realm_buddhahood_specs/specs/holy_realm_buddhahood_focus_tree.md`, especially the coverage table at lines 302-320.

## Implemented Tranche - 2026-06-11

The first route-lock tranche is implemented in `common/national_focus/003_holy_realm.txt`:

- Teaching route: `THR_send_first_envoys`, `THR_translation_houses`, `THR_teach_under_bombardment`, and `THR_many_lamps_one_flame`. `Many Lamps, One Flame` reads `teaching_successes` and `crisis_teaching_successes`.
- Meditation route: `THR_sit_beneath_prayer_flags`, `THR_first_quiet`, `THR_second_quiet`, `THR_third_quiet`, and `THR_fourth_quiet`. The quiet focuses read `dhyana_depth`.
- Governance route family: `THR_council_of_abbots`, `THR_name_protector_regent`, and `THR_seat_pilgrim_assembly` are mutually exclusive route choices and set governance flags.
- `THR_buddha_mandate` requires the completed teaching gate, fourth quiet gate, and one governance choice in addition to the older Arhat/industry/military/diplomacy prerequisites.
- Holy Realm-specific focus filters now cover Bodhi, Teaching, Meditation, Governance, Sanctuary, Compact, Anti-Chaos, Nirvana, and Hidden branches.

## Missing Route Architecture

Implement these as focus-tree work, not only as decisions:

1. Teaching route follow-up: add more downstream teaching payoffs and mission-slot variety beyond the route-lock chain.
2. Meditation route follow-up: add later Dhyana payoffs, stronger interaction with `meditation_charge`, and visible post-Buddhahood meditation use beyond the route-lock chain.
3. Governance route follow-up: let Council of Abbots, Protector Regent, and Pilgrim Assembly affect later teaching, defense, refugee, and compact tools.
4. Sanctuary logistics: reshape existing generic whole-country construction focuses into named sanctuary logistics: granaries, pilgrimage roads, clinics, workshops, storehouses, and supply support for allies/compact members.
5. Guardian military: turn `THR_vow_keeper_regiments` and support nodes into a defensive guardian route with temple guards, pilgrimage escorts, mountain pass detachments, and anti-chaos defensive doctrine.
6. Sangha Compact diplomacy: either rename and formalize the current `Mandala of Nations` as the accepted compact equivalent, or add a separate Sangha Compact lane with membership rules, cohesion, shared decisions, refusal/exit risks, and anti-puppet clauses.
7. Expansion/liberation: replace broad ordinary annexation/registration rhetoric with the spec's pilgrimage and liberation framing where appropriate. Keep hard conquest as a corrupted/high-chaos route if retained.
8. Anti-chaos powers: add a focus lane that upgrades or gates the implemented Buddha powers after Buddhahood. The current powers exist as decisions but not as a focus branch.
9. Final Silence: keep the existing late branch but add visible spec sequence alignment: Awakened One, Show the Powers, Last Wheel, Witnesses Gather, Extinction of Defilements, Final Silence, Empty Seat.
10. Hidden Schism: expose a hidden focus branch only when False Buddha Schism flags are active. Current debate/suppression decisions exist, but the focus route is absent.

## Recommended Implementation Order

1. Add route locks and bridge focuses for teaching, meditation, and governance first, because they gate Buddhahood requirements.
2. Rework AI weights around those route locks before adding late branches.
3. Add Sangha Compact and anti-chaos power focus branches next, reusing existing decision categories and flags.
4. Align Final Silence sequence last, preserving existing terminal/non-terminal decision gates.
5. Run focus, localisation, decision, and AI audits after the new route families are implemented.

## Boundaries

Do not remove the existing Holy Realm mechanics wholesale. Reuse the existing Buddhahood decisions, Mandala GUI, Buddha powers, Final Silence gates, and achievement hooks. The missing work is focus-route visibility, branch pacing, route interaction, and AI behavior.
