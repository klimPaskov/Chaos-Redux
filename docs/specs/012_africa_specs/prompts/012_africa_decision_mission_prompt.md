# Decision and Mission Prompt — Event 012 Africa

Use `hoi4-decisions-missions`, `chaos-redux-events`, `hoi4-focus-trees`, and `chaos-redux-improvement-loop`. After implementation, run or spawn `chaosx_decision_mission_auditor` for a targeted audit and small patch pass. Any subagent must be spawned with `fork_context=false` and explicit paths.

## Source files

Read:

- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`
- `docs/specs/012_africa_specs/matrices/012_africa_decision_map.md`
- `docs/specs/012_africa_specs/specs/012_africa_focus_tree_plan.md`
- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`
- `docs/specs/012_africa_specs/specs/012_africa_evolutions_world_end_and_scenarios.md`

## Implementation objective

Implement Event 012’s decision, mission, and mechanic-presentation layer as a staged continental unification system. It must not become a political-power store and must not instantly annex/core the continent.

## Required decision categories

Create or extend decision categories for:

1. Continental Congress
2. Charter League Diplomacy
3. Liberation War Office
4. Regional Integration
5. Diaspora Return Offices
6. Green Covenant / High-Chaos Reports
7. Post-Unification Continental Sponsorship
8. RSA Civil-War Emergency branch, when applicable

The categories should be phased and route-aware. Hide obsolete or invalid actions after route changes, integration completion, member exit, war end, annexation, civil war resolution, or terminal world-end.

## Required mechanic values

Expose these values in category headers, scripted localisation, national spirits, or a custom GUI:

- Legitimacy
- Authority
- League Cohesion
- Liberation Momentum
- Regional Trust
- Colonial Alarm
- Paper-Core Burden
- Covenant Pressure

Values must change through focuses, decisions, missions, wars, state control, foreign aid, League membership, integration outcomes, evolution state, and AI actions. They must unlock or block content.

## Cost rules

Avoid decisions that cost only political power or command power. Use varied costs and requirements:

- army/navy/air XP;
- infantry/support equipment, artillery, trucks, trains, convoys, aircraft, ships, tanks;
- fuel and supply capacity;
- manpower and local support;
- stability, war support, legitimacy, regional trust, League cohesion;
- civilian/military factory burden;
- rail/port/depot control;
- placed supplied divisions;
- active deadlines and missions;
- relations, access, foreign influence debt, intelligence exposure.

Every blocked nonstandard requirement needs clear tooltip/localisation.

## Mission requirements

Timed missions should ask the player to do real work:

- hold named capitals;
- defend ports;
- keep convoy/rail corridors open;
- place supplied divisions in named regions;
- secure rail hubs and depots;
- win a liberation campaign by a deadline;
- keep League cohesion above a threshold;
- integrate a region without rebellion;
- calm or negotiate Green Covenant pressure;
- win RSA civil-war objectives.

Do not require a second click after the objective is already completed if a goal-style mission is better.

## Custom GUI

If feasible, implement the Continental Congress Interface or a lighter scripted GUI equivalent:

- entry point from Continental Congress decision category;
- meters for the core values;
- regional authority cards;
- selected target card;
- action buttons for aid, integration, protection, referendum, administration, emergency council;
- warning states for low cohesion, rebellion, scramble pressure, and Green Covenant crisis;
- static and animated sprites from the asset package;
- AI equivalents for every gameplay button;
- cleanup after invalid targets or route changes.

If full scripted GUI implementation is not feasible in the current pass, report it as a simplification and implement a decision-header/scripted-localisation fallback only with explicit approval.

## Required decision families

At minimum implement families matching the decision map:

- Convene the Proclamation Congress
- Seat Regional Delegates
- Draft the Charter Articles
- Emergency War Council
- Recognise a Provisional African Authority
- Send Officer Cadres
- Open Relief/Aid Corridors
- Demand Anti-Puppet Clauses
- Prepare Liberation Fronts
- Raise Border Liberation Columns
- Secure Rail Belts
- Protect African Allies
- Begin Regional Integration Talks
- Establish Charter Administrations
- Hold Integration Referendums
- Convert Paper Cores to Living Cores
- Invite Return Cadres
- Build Return Settlements
- Form Diaspora Officer Schools
- Read River and Sky Reports
- Bargain with Forest Courts
- Call the Tides
- Threaten the Scramble
- Sponsor Other Continental Unifiers
- Proclaim Cross-Continental Unions
- Pursue The World Is One

## AI

AI must have route-aware decisions. It should:

- help African countries at war with colonisers before pressuring them;
- avoid integration pressure while cohesion is near collapse unless military/high-chaos route permits it;
- avoid invalid missing-target decisions;
- stage regional integration;
- avoid suicidal war against all major colonisers at once;
- run RSA civil-war decisions according to side;
- use high-chaos decisions only when unlocked.

## Leader/court display-name hooks

When a decision, mission, GUI action, or formation route creates or publicly recasts an Event 012 ruler/council identity, call the same localisation path used by the country-package layer. Keep source-language joke names in localisation only; do not expose direct English translations or raw phrase strings in ids.

## Cleanup and exploit checks

Implement cleanup for:

- selected target flags/variables/event targets;
- obsolete active missions;
- dead/annexed members;
- completed integrations;
- members leaving or declaring war;
- RSA civil-war conclusion;
- super-event and world-end transition;
- high-chaos nonhuman actors.

Exploit checks must cover:

- free unit loops;
- repeated equipment/factory/influence farming;
- cheap core/claim conversion;
- war-goal spam;
- repeated integration referendums;
- AI repeated aid target loops;
- puppet/annex shortcuts.

## Audit handoff requirement

After implementation, `chaosx_decision_mission_auditor` should audit or patch small local issues. Its handoff should list changed decision ids, mission ids, category ids, localisation keys, AI changes, before/after behaviour, and remaining risks under:

```text
docs/plans/012_africa_plans/subagent_handoffs/
```


## Revision 2 expansion requirements

Also implement the expanded source files:

- `specs/012_africa_niche_polities_and_subjects.md`
- `specs/012_africa_high_chaos_absurd_paths.md`
- `matrices/012_africa_expanded_subject_matrix.md`
- `matrices/012_africa_absurd_high_chaos_routes_matrix.md`

The implementation must add the Legacy Authority Lane, Authority Register decisions, Integration Temperature/trust/resistance model, Priority A historical authorities, as many Priority B authorities as needed for regional depth, and high-chaos Covenant actors with explicit nonhuman/supernatural classification. Do not collapse this into generic modifiers, placeholder tags, or one broad “native authority” subject.


## Revision 2 decision/mission requirements

Implement an Authority Register with selected-target or phased presentation. It must support observer offices, Charter Subjects, regional governorate merging, old-capital guard missions, charter road repair, council holding, integration missions, rivalry arbitration, and high-chaos disaster warnings. Use dynamic non-PP costs: equipment, trains, convoys, local support, legitimacy, stability, army XP, supply, units in named states, port/rail control, and faction cohesion.

High-chaos disaster warnings must have target counterplay, Omen Reliability, false-warning risk, AI equivalents, cooldowns, and legitimacy costs.

## Add Restoration Dossiers and Bestiary Clause system

Implement the decision and mission layer from `specs/012_africa_niche_country_expansion.md` and the updated decision maps.

Required decision families:

- Open Regional Archive.
- Survey Old Seat.
- Charter Local Office.
- Raise Local Guard.
- Protect Monument / Regalia.
- Negotiate Settlement.
- Manage Forgery Crisis.
- Bestiary Clause.
- Supernatural Sanction.

The category must use regional filters, active caps, readable dynamic value summaries, custom trigger tooltips, and cleanup for obsolete or invalid dossiers. Costs must use concrete resources and objectives: equipment, manpower, construction burden, trains, convoys, divisions in named states, ports/rail/monuments controlled, local trust, legitimacy, League cohesion, restoration debt, mythic pressure, and cooldowns. Do not turn this into a political-power store.


