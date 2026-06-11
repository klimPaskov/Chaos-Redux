# Holy Realm Buddhahood Focus Tree Completion Plan

## Scope

This plan covers the gap between the current `THR_focus` implementation and the accepted Buddhahood focus-tree spec. It does not authorize a whole-tree rewrite by a focus audit subagent; it is a handoff for the main implementation pass.

## Current State

`common/national_focus/003_holy_realm.txt` contains 73 `THR_` focus ids and a working older Holy Realm route built around refuge survival, Bodhisattva/Arhat stages, Mandala expansion, restraint versus Final Silence, and regional conquest/registration. It also hooks into Buddhahood systems through `THR_buddha_mandate`, which is localized as `The Unshaken Seat`, and through decisions in `common/decisions/003_holy_realm_decisions.txt`.

The current tree does not yet implement the spec as a Buddhahood-first 72-focus route family. The required route list is in `docs/specs/tbd_holy_realm_buddhahood_specs/specs/holy_realm_buddhahood_focus_tree.md`, especially the coverage table at lines 302-320.

## Missing Route Architecture

Implement these as focus-tree work, not only as decisions:

1. Teaching route: add a visible path from the Bodhisattva vow through mission-slot, foreign teaching, crisis teaching, and `Many Lamps, One Flame` gates. It should read `teaching_successes` and `crisis_teaching_successes`, not only unlock `THR_hold_dharma_teaching`.
2. Meditation route: add a visible Dhyana path from Mandala/seat preparation through four Dhyana milestones. It should interact with `THR_begin_concentration_sequence`, `THR_hold_*`, `dhyana_depth`, and `meditation_charge`.
3. Governance route family: add the three promised governance choices: Council of Abbots, Protector Regent, and Pilgrim Assembly. They should change party/leader/advisor or route flags and affect later teaching, defense, and refugee/compact tools.
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
