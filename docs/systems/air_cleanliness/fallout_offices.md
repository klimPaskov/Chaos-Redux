# Fallout Ash-week Offices and Office Arcs

The fifth step of the Ash-week orientation gives every Fallout survivor its first public office. The office becomes a national spirit, and a three-stage arc later decides whether it grows into a lasting institution, survives under strain, or collapses. Agent decision A16 in `docs/plans/air_cleanliness_fallout_plans/agent_decisions_2026-10-04.md` records the design choices; the candidate table is `docs/plans/air_cleanliness_fallout_plans/FALLOUT_OFFICE_CANDIDATES.md`.

## How it works

1. During orientation, `fallout_orientation_advance_country` calls `fallout_office_install_candidate_package`. If the country's memory, region and archetype match one of the twelve pilot memory rows, the pilot's three candidates are used; otherwise the three candidates of the country's region and archetype cell (108 cells, candidate ids 101 to 424). The package also stores the role of each slot for the event text.
2. Step 5 (events `chaosx.fallout.78` to `81`) offers the three candidates. Slot 1 is a relief or administration office paid with Medicine and Food, slot 2 a security or extraction office paid with Fuel and Scrap, and slot 3 an institution paid with Power, Shelter capacity and Scrap. Each option shows the national spirit its office would install. The hidden AI uses the existing orientation score. The step is skipped without a popup only when the country has no region or archetype, or cannot pay for any candidate.
3. The result (event 80, or hidden 81) is graded as before. On success or a limited result `fallout_office_record_selected_candidate` stores the candidate, its role, slot and generation in `fallout_office_*` variables, sets `fallout_office_held` (and `fallout_office_limited` for a limited result), and installs the role's office idea, named after the candidate through the role's `GetFalloutOffice<Role>Title` scripted localisation. A failure stores the candidate with `fallout_office_refused` and installs nothing.
4. Once orientation is complete, the living-world candidate review (`fallout_event_build_country_candidate_registry`) adds one row for the office's role: candidate ids 1060, 1067, 1074, 1081, 1088 or 1095, cooldown family `character`, primary family `character_and_leader`, the office as its institution actor, and the managed resource as its pressure resource. The scheduler issues it like any ordinary event.
5. Introduction (N, hidden AI N+1): three approaches, each with a cost, an optional immediate gain, and changes to public trust and strain in the office (`fallout_office_arc_trust`, `fallout_office_arc_strain`, starting at 50 and 30, or 38 and 38 for a limited office).
6. Pressure (N+2, hidden AI N+3), 40 days later: the event shows trust and strain and offers a civic route or a command route, each with its own cost and ledger change and a preview of the institution it can found.
7. Outcome (N+4, hidden AI N+5), 210 days later: score = trust - strain + Cohesion / 5 + Recognition / 5 + managed resource / 5, plus 10 on the command route. Success (50 or more) replaces the office idea with the route's institution and raises the managed resource, Recognition, Cohesion and stability. A partial result (25 or more) adds `fallout_office_strained` for 180 days. A failure removes the office, adds `fallout_office_collapse` for 365 days, cuts the managed resource, Recognition, Cohesion and stability, and for the doctor and militia arcs kills people in the capital (Fallout aftermath Deaths reason).
8. Cleanup (N+6) releases the delayed rows, refunds the introduction cost if the outcome never resolved, and closes the arc for the Fallout generation. `fallout_office_arc_last_route` and `fallout_office_arc_last_outcome` remain as memory for later content.

## Roles

| Role | Arc | Office idea | Civic institution | Command institution | Managed resource | Events |
| --- | --- | --- | --- | --- | --- | --- |
| Quartermaster | The Ration Rolls | Quartermaster's Office | Public Ration Ministry | Army Commissariat | Food | 1060 to 1066 |
| Doctor or medical board | The Triage Order | Chief Medical Office | Public Health Board | Medical Command | Medicine | 1067 to 1073 |
| Grid engineer | The Repair Schedule | Chief Engineer's Office | Public Works Authority | Works Directorate | Power | 1074 to 1080 |
| Militia commander | The Militia Oath | Militia Command | Civil Defence Service | Militia High Command | Fuel | 1081 to 1087 |
| Local mayor or ward chair | The Ward Petitions | Ward Council | Elected Ward Assembly | District Prefects | Shelter capacity | 1088 to 1094 |
| Judge or tribunal chair | The First Verdict | Emergency Court | Survivors' Courts | Emergency Tribunals | Recognition | 1095 to 1101 |

## AI

- Step 5 keeps the orientation score (resource strength, archetype and regional matches).
- Introduction: the role's base priority for each affordable approach, plus 15 for the approach the archetype favours (open approaches for continuity, food compact, religious and mutant governments; guarded approaches for warlord, quarantine, bunker and machine governments; pragmatic approaches for scavenger, nomad, technate and maritime governments).
- Pressure: the civic route gains 20 when Cohesion is at least 40 and 15 when trust is not below strain; the command route gains 15 when trust is below strain and 15 for warlord, quarantine, bunker and machine governments. A route the country cannot pay for is not taken; when neither can be paid for, the civic route is taken.

## Interactions

- Survival resources: every cost and reward uses `fallout_survival_current_entries` and Cohesion, clamped by `fallout_orientation_clamp_resources`.
- Scheduler: the arc rows use the ordinary-event receipt, delayed results, delayed callbacks and cleanup of the living-world scheduler, so fatigue, cooldowns and the visible-event budget apply. Country loss and generation change cancel pending rows through the scheduler's delayed-row reconciliation.
- Event Log: history ids 9211 to 9216 (type `fallout_country_memory`) record the approach, the route and the outcome; the name and detail entries live in `chaosx_scripted_localisation_events_log.txt` and `GetFalloutOfficeArc<Role>EventLogDetail`.
- Deaths: doctor and militia failures use `apply_exact_state_civilian_population_loss` with `chaos_meter_deaths_reason.fallout_aftermath`.

## Tuning

All values are script constants in `common/script_constants/fallout_consolidated_constants.txt`: `fallout_office_arc_cost`, `fallout_office_arc_gain`, `fallout_office_arc_ledger`, `fallout_office_arc_ai`, `fallout_office_arc_threshold`, `fallout_office_arc_result`, `fallout_office_arc_modifier`, `fallout_office_arc_timing` and `fallout_office_arc_transaction`. Idea modifier values are in the idea blocks of `common/ideas/fallout_consolidated_ideas.txt`.

## Icons and art

No new art is required. The eighteen office and institution ideas use vanilla generic idea sprites from the base game's interface files, as the other universal survivor ideas do; the two dynamic modifiers use `GFX_idea_generic_disjointed_gov` and `GFX_idea_generic_economic_crisis`. The arc events reuse existing Fallout report art registered in `interface/fallout_consolidated.gfx` (for example `GFX_report_event_fallout_last_inventory`, `GFX_report_event_fallout_triage_wall`, `GFX_report_event_fallout_last_transformer`).

| Idea | Sprite |
| --- | --- |
| `fallout_office_quartermaster` / `_civic` / `_command` | `GFX_idea_generic_supply_depot` / `GFX_idea_generic_central_management` / `GFX_idea_generic_stockpile_preparation` |
| `fallout_office_physician` / `_civic` / `_command` | `GFX_idea_generic_morale_bonus` / `GFX_idea_generic_commission` / `GFX_idea_generic_secret_police` |
| `fallout_office_engineer` / `_civic` / `_command` | `GFX_idea_generic_improved_industries` / `GFX_idea_generic_build_infrastructure` / `GFX_idea_generic_energy_concern` |
| `fallout_office_commander` / `_civic` / `_command` | `GFX_idea_generic_reserve_divisions` / `GFX_idea_generic_fortify_the_borders` / `GFX_idea_generic_war_preparation` |
| `fallout_office_ward_chair` / `_civic` / `_command` | `GFX_idea_generic_local_self_management` / `GFX_idea_generic_conference` / `GFX_idea_generic_disjointed_gov` |
| `fallout_office_magistrate` / `_civic` / `_command` | `GFX_idea_generic_constitutional_guarantees` / `GFX_idea_generic_political_support` / `GFX_idea_generic_oppression` |

## Future plans

- Named advisors for the person offices, with portraits produced through the portrait workflow, so a successful quartermaster or doctor can enter the advisor roster.
- Second-stage callbacks keyed on `fallout_office_arc_last_route` and `fallout_office_arc_last_outcome`: a ration ministry facing its first surplus, a medical command facing a returning fever, a militia high command pushing toward a warlord government.
- Dedicated Fallout idea art for the eighteen offices and institutions.
- Arcs for further roles from the arc matrix (radio operator, refugee organizer, scavenger captain, agronomist) with their own candidate mapping.
