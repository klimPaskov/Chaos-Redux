# Event006 Localisation Audit: Evolution Wording Patch

## Scope

Bounded localisation/scripted-localisation audit for stale Event006 wording that could present package, dossier, formation, compact, local-polity, strange-package, or route records as evolution entries.

The accepted Event006 evolution log policy remains: only the four true release-scale tier milestones are evolution entries:

- Gathering Storm
- Rising Cascade
- Old Names Return
- Impossible Statehood

## Files changed

- `localisation/english/chaosx_gui_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_173018_event006_localisation_evolution_wording_patch.md`

## Files inspected but not changed

- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/systems/events_log_evolutions_and_clusters.md`
- `docs/plans/006_independence_wave_plans/source_of_truth_map.md`

## Keys changed

- `chaosx.events_log.evolution.type.independence_wave_tier`
- `chaosx.events_log.window.event_details.independence_wave`
- `chaosx.events_log.window.evolution_details.independence_wave.title.stage_1`
- `chaosx.events_log.window.evolution_details.independence_wave.title.stage_2`
- `chaosx.events_log.window.evolution_details.independence_wave.title.stage_3`
- `chaosx.events_log.window.evolution_details.independence_wave.title.stage_4`
- `chaosx.events_log.window.evolution_details.independence_wave.body.stage_1`
- `chaosx.events_log.window.evolution_details.independence_wave.body.stage_2`
- `chaosx.events_log.window.evolution_details.independence_wave.body.stage_3`
- `chaosx.events_log.window.evolution_details.independence_wave.body.stage_4`
- `chaosx.events_log.window.evolution_details.independence_wave_tier.body`
- `chaosx.events_log.window.evolution_details.independence_wave_dossier.body`
- `chaosx.events_log.window.evolution_details.independence_wave_formation.body`
- `chaosx.events_log.window.evolution_details.independence_wave_package.body`
- `chaosx.events_log.window.evolution_details.summary.independence_wave_record`

## Scripted-localisation changed

`GetEventsLogSelectedEvolutionSummary` now routes selected Event006 rows whose `events_log_selected_evolution_event_id` is Event006 but whose type is not `constant:independence_wave_event_log.evolution_type` to `chaosx.events_log.window.evolution_details.summary.independence_wave_record`.

Before: Event006 dossier/package/formation rows inherited the generic `Evolution Stage` summary label.

After: Event006 non-tier rows show `History Row`, while the true tier milestones still use the generic evolution-stage summary.

## Validation

- Confirmed `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_gui_l_english.yml` still report UTF-8 BOM via `file`.
- Confirmed no `:0` localisation keys in the two touched/related English localisation files with `rg -n "^[A-Za-z0-9_.-]+:0\\s"`.
- Confirmed Event006 active evolution recorder calls remain four and only in `common/scripted_effects/006_independence_wave_effects.txt`.
- Confirmed no gameplay event, decision, focus, trigger, or effect files were edited.
- Confirmed no `record_events_log_evolution_entry` call sites were changed.

## Remaining risks

- The shared key `chaosx.events_log.window.event_details.evolution_entry_meta` still says `Evolution Stage` because it is a generic event-log template used outside Event006. I did not change it in this bounded patch. If Event006 non-tier dossier/package/formation rows are later shown through that exact generic event-preview template, a small shared-UI branch may still be needed.
- The worktree was already heavily dirty before this audit, including Event006 files and shared event-log files. This handoff only claims the narrow localisation/scripted-localisation wording patch above, not Event006 completion.

## Skills used

- `chaos-redux-events`
- `chaos-redux-subagents`
