# Event 010 Death Planning Package

## Resume and authority boundary

This package is the retained design and provenance source for Event ID 10, `Death`, which replaced the obsolete `Spirit of War/Peace` event entirely.
Event 010 is implemented in source.
[`docs/events/010_death/overview.md`](../../events/010_death/overview.md) describes the current implementation, and [`agent_decisions_2026-10-05.md`](../../plans/010_death_plans/agent_decisions_2026-10-05.md) records the parent-accepted October design changes (Seal Names, Survey and Outpost field work, No Graves Needed, Wasteland Roads, four-type cost bundles, reporting, launch failure, Six Continents, defeat aftermath, the four-tab Black Atlas).
Where this package and those two records disagree, the implementation records describe what exists and the accepted decision table describes what was approved; the spec text below has been reconciled to both on 2026-10-10.
The [source-processing record](research/010_death_source_processing_notes.md) separates the original user constraints from planner decisions and specialist choices.
`DTH` is Death's existing registered country identity in `common/country_tags/chaosx_countries.txt:5`, mapped to `countries/Death.txt`.
Reuse and inspect that owner package under [the shared identifier registry](../shared_identifier_registry.md); it is not a free tag candidate.
Current workflows belong to [chaos-redux-subagents](../../../.claude/skills/chaos-redux-subagents/SKILL.md) and [chaos-redux-event-assets](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), under the repository `CLAUDE.md`.

## Remaining work

| Item | Disposition | Owner record |
| --- | --- | --- |
| Event catalog workbook parity for the Event 010 row and scenario row 6 | accepted and queued; the in-game wording is implemented and the workbook update waits for an authorized spreadsheet pass | [`catalog_changes_pending.md`](../../plans/010_death_plans/catalog_changes_pending.md) |
| Living Compact obligations, shared missions, leadership disputes, and success or collapse thresholds | accepted and queued as a later tranche of the July improvement loop | [July addendum, Later Tranches](../../plans/010_death_plans/2026_07_11_death_improvement_loop_addendum.md) |
| Black Atlas regional diagnostics after public revelation | accepted and queued as a later tranche; decisions stay the authoritative action surface | same |
| Route-aware aftermath for Compact members, Black Book users, Heralds, and oathbreakers | accepted and queued as a later tranche | same |
| Seal Names backlash replay after a Fallout world rewrite suppresses state-control callbacks | unresolved integration limit | [`release_completion_2026-10-06.md`](../../plans/010_death_plans/release_completion_2026-10-06.md) |
| GUI production render, complete weighted-logic comparison, and inherited art-master provenance | unresolved verification limits; they do not reopen implemented source | same |

The [decision inventory](specs/010_death_decisions_ui_ai.md#decision-inventory) lists response concepts from the original plan that were never built; they remain unresolved proposals and are not part of the implemented scope.

## Main spec files

- `specs/010_death_spec_part_1_core_flow.md`: event identity, origin, stages, reveal, world-end, super-event roles, event-log role.
- `specs/010_death_spec_part_2_mechanics.md`: state identifiers, consumption effect, wasteland rules, spread, withering, coastal jumps, defeat, ghosts, evolutions, shared-system links, scenario.
- `specs/010_death_country_package_and_focus_tree.md`: Death country package, Zol, units, the 26-focus progression tree, Herald and Apostolate identity.
- `specs/010_death_decisions_ui_ai.md`: decision inventory, Living Compact, Dark Methods, Black Oath, Black Atlas, Death's Muster, AI behaviour.
- `specs/010_death_assets_super_events_achievements.md`: visual assets, super-events, achievements, catalog row direction, acceptance criteria.

## Supporting files

- `matrices/010_death_state_effects_matrix.md`
- `matrices/010_death_ai_strategy_matrix.md`
- `matrices/010_death_decision_map.md`
- `focus_graphs/010_death_focus_architecture.mmd`
- `research/010_death_source_processing_notes.md`

## Historical build contracts

The files under `prompts/` are the original 2026 build contracts for the now-implemented event.
Do not rerun them; each carries a header saying so.
A resume task should start from the Remaining work table above, the implementation overview, and the owning plan named in the table.

- `prompts/010_death_goal_prompt.md`
- `prompts/010_death_coding_prompt.md`
- `prompts/010_death_decision_mission_prompt.md`
- `prompts/010_death_asset_prompt.md`
- `prompts/010_death_super_event_prompt.md`
- `prompts/010_death_achievement_prompt.md`
- `prompts/010_death_subagent_prompts.md`

## Open questions

Each item below is proposed (spec audit 2026-10-10) and has no acceptance.
Each conflicts with, or extends, parent-accepted implemented design, so it is recorded here rather than written into the accepted spec text.

1. Give Front Readiness and Compact Cohesion a real rule, or remove them from player view.
   Source review found that `global.death_front_readiness` is written by gear, quarantine and Last Shores decisions but read only by the Black Atlas scripted localisation, and `global.death_compact_cohesion` is read only by the `death_the_living_conference_ready` achievement predicate in `common/scripted_effects/010_death_effects.txt`.
   Decision tooltips still promise that these values rise, so they currently read as progress without consequence.
   Proposal: fold both into the queued Living Compact tranche, where readiness bands scale the `death_wither_damage.active_living_*` damage taken by countries at war with Death, and cohesion below `death_decision_tuning.compact_cohesion_threshold` makes members decline `death_compact_war_declaration`, which is the failure state Part 2 of the decisions spec always described.
   If that tranche is rejected, drop both values from the Atlas and from decision tooltips instead.
2. Remove the two duplicated Atlas rows.
   The Jump surcharge row is `global.death_watch_network` multiplied by `death_soul_power.watch_network_cost_step_percent`, and the Compact tab's Line row (`GetDeathAtlasLineStatus`) is a band of the same `global.death_front_readiness` shown as a number on the Fronts tab, so the Atlas shows two quantities twice.
   One row such as "Watch network 6/10, sea jumps cost 60% more" and one readiness row with its band and consequence would carry the same information in two fewer values.
   This changes the parent-accepted eleven-value Atlas, so it needs parent acceptance.
3. Record Herald sacrifices as atrocities in the shared Condemnation system.
   `death_feed_border_to_death` deliberately hands a populated living state to Death and currently records only the shared deaths receipt through `death_register_consumed_population_deaths`.
   Proposal: the Event 010 caller adds one `condemnation_add_source` receipt with `condemnation_source.atrocity`, the Herald as actor and the frozen pre-consumption population as civilian deaths, following the `random_terror_add_condemnation_source` caller pattern; the Condemnation owner keeps scaling, sanctions and history.
   Death's own consumption stays condemnation-free, as Part 2 already requires.
4. Replace the never-built evacuation concepts with a Migration-owned evacuation request.
   `Mark Low Islands for Evacuation` and `Emergency Refugee Shipping` were never implemented, and the shared Famine and Migration spec (Part 7, Other event consequences) already reserves maritime evacuation of surviving civilians for Event 010.
   Proposal: a warned coastal or island state with a lit port can submit a pre-consumption flight request through `migration_apply_flight_request`; the Migration owner decides the accepted amount and destination, and Death later consumes only the people who remained.
   This is blocked on the Migration movement API that `common/scripted_effects/migration_adapter_effects.md` (Movement boundary) says does not yet exist for external hazard owners.
   It would also let the Last Ferry achievement mean evacuation, as its title suggests, instead of port preparation.
5. Give the shared pressure adjustments their own constants.
   `death_decision_patrol_plan_effect` and `death_decision_interrogate_empty_road_effect` reuse `death_decision_tuning.quiet_quarantine_pressure_reduction`, and `death_quarantine_hold_failure` reuses `death_spread.wither_state_progress_gain` as a pressure gain.
   Separate named constants would let each response be tuned without silently retuning the others; no value changes.

## Changelog

- 2026-10-10 spec audit:
  - Reconciled the package with the implemented source and the 5 October accepted decisions.
    Changes are listed per file below; no accepted user or parent decision was overridden.
  - README: repointed live skill links from the ignored `.agents/skills/` mirror to `.claude/skills/`, added the Remaining work table, marked the prompts as historical build contracts, and added the Open questions above.
  - Part 1: aligned origin population caps, report timing, reveal war scope, the defeat-aftermath threshold and the event-detail wording with the constants and localisation, and condensed the four pre-research super-event briefs into a table of the implemented packages (the research directions remain in git history and in `docs/super_events/010_death/`).
  - Part 2: replaced the suggested variable tables with the implemented identifiers, rewrote the spread-pressure sources to match the effects that actually write pressure, corrected the ghost unit types, and added the implemented Migration and Chaos Meter links.
  - Decisions spec: replaced five overlapping decision tables (several decisions appeared twice under different names) with one inventory keyed by implemented decision ID plus a list of never-built concepts, corrected the category names to the in-game ones, removed the contradiction between "no mission layer" and the implemented hold-line mission, and updated the Atlas stage labels.
  - Country and focus spec: updated the focus map and graph to the implemented 26-focus tree, the idea list to the nine implemented ideas, and the unit type to the three implemented sub-units.
  - Assets spec: recorded the implemented super-event packages and achievement IDs, corrected the Last Ferry condition, and marked the acceptance list as satisfied at source level with its open verification limits.
  - Matrices: updated category and decision names to the implemented ones and marked never-built families.
  - Prompts and research notes: added historical headers and fixed live skill links; the historical read lists were left unchanged.
