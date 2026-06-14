# Event 009: White Peace

Event 009 White Peace is a repeatable Peace-cluster de-escalation event. It looks for wars that can be ended without conquest, indemnity, faction disruption, subject-state side effects, or scripted-story damage, then forces a status-quo settlement between the selected pair. The event is intentionally quiet: the popup has one acknowledgement option, and the settlement has already been signed.

## Runtime Flow

1. `chaosx.nr9.1` is selected from the normal repeatable event pool or through the Peace cluster path. Event 9 remains in `global.repeatable_events`.
2. `get_event_weight` calls `calculate_white_peace_dynamic_cap`, then clips the recovered repeatable weight to the current White Peace cap. The stored repeatable recovery value is not overwritten by the dynamic cap.
3. `prepare_white_peace_runtime_context` recalculates war pressure, chooses the current evolution stage, selects a branch, saves `white_peace_primary` and `white_peace_partner`, and exposes `event_cluster_actor` for log attribution.
4. `chaosx.nr9.1` opens the correct one-option report variant: `.2` single minor, `.3` several minor settlements, `.4` major-country settlement, or `.5` broad circular.
5. The report option runs `apply_white_peace_current_context`. Each settled pair receives recent-settlement memory, a modest timed opinion modifier, and delayed sender/recipient survival tracking for the No Winner achievement. Multi-pair branches loop only until their branch cap is reached.

## Safety Gates

Country eligibility is centralized in `can_country_be_white_peace_target`. The target must exist, use normal civilian systems, be at war, control at least one state, keep its capital, be below the near-capitulation threshold, and avoid civil war, subject, faction, special-country, nonhuman, protected-war, and recent-settlement states.

Pair eligibility is centralized in `can_pair_receive_white_peace`. It requires a live war relation, two independently valid countries, no same-tag or faction relation, safe capitals, and either a minor-versus-minor pair or an evolved major-eligible pair. Base and stage I use only `can_minor_pair_receive_white_peace`; stage II and III can use `can_major_pair_receive_white_peace`.

Other event systems can opt out by setting `white_peace_protected_country` or `white_peace_protected_war_actor` on any participant that should never be selected by this event.

## Dynamic Weight

The tuning values live in `common/script_constants/009_white_peace_constants.txt`. The main variables are:

| Variable | Purpose |
| --- | --- |
| `global.white_peace_active_war_count` | Countries currently in normal, non-protected wars. |
| `global.white_peace_safe_minor_pair_count` | Valid minor-versus-minor candidate pairs. |
| `global.white_peace_minor_only_war_count` | Valid minor-only pressure proxy. |
| `global.white_peace_major_candidate_count` | Valid major-involved pairs for stage II and III. |
| `global.white_peace_major_locked_pair_count` | Safe major-involved pairs blocked only because the major branch is not unlocked. |
| `global.white_peace_recent_memory_actor_count` | Warring countries blocked by recent White Peace country memory. |
| `global.white_peace_recent_pair_memory_count` | Candidate pair scans blocked by exact reciprocal pair memory. |
| `global.white_peace_protected_war_actor_count` | Warring actors excluded as protected, special, or nonhuman. |
| `global.white_peace_broad_conflicts_settled` | Broad-branch safe conflict relations settled during the current firing. |
| `global.white_peace_environment_cap` | War-pressure cap before stage and recent-broad penalties. |
| `global.white_peace_repeatable_decay_multiplier` | Current Event 009 repeatable cap ratio applied to the live cap before evolution multipliers. |
| `global.white_peace_effective_dynamic_cap` | Live cap after stage/recent penalties; never above `1500`. |

One small valid war produces a low live cap below ordinary event prominence. Many active wars and safe minor pairs raise the cap, but `constant:white_peace_weight.max_environment_cap` clamps the environment at `1500`. Higher stages apply lower multipliers, so stronger branches become less likely even though they can settle more.

Normal repeatable recovery and repeatable firing decay still apply. `update_repeatable_event_weights` continues to recover the stored event weight. `calculate_white_peace_dynamic_cap` multiplies the environment cap by Event 009's current repeatable cap ratio, then by the evolution-stage multiplier, and `get_event_weight` clips only the live value used by the picker and settings preview.

## Branches and Stages

| Stage | Branch behavior | Limits |
| --- | --- | --- |
| Base | Settles one safe minor-versus-minor pair. | One pair. |
| I: Repeated Minor Settlements | Can settle several safe minor pairs from one firing. | Two pairs, or three under heavier safe-minor pressure. |
| II: Major-Country Settlement | Adds a rare branch that can settle one safe major-involved pair. | Major participant gets longer recent-memory. |
| III: Broad Diplomatic Settlement | Adds a rare broad branch that can quiet several safe pairs while leaving protected wars untouched. | Five pairs and capped Chaos reduction. |

Stage pressure is derived from active-war and candidate-pair counts, plus persistent stage flags once higher stages have been reached. Evolution rows are recorded through `record_white_peace_evolution_if_needed` with `constant:white_peace_event_log.evolution_type`.

## Chaos and Memory

White Peace suppresses the normal per-country `on_peace` Chaos Meter adjustment while its own settlement branch runs, then applies one capped branch-level reduction. Single minor settlements reduce Chaos by `-1`; major settlements reduce by `-2`; multi and broad branches accumulate pair reductions but clamp them through `constant:white_peace_chaos_delta.multi_minor_cap` and `constant:white_peace_chaos_delta.broad_cap`.

Settlement memory uses:

- `recent_white_peace_country` for affected countries;
- `recent_white_peace_pair_<tag>` for exact pair-repeat prevention on each participant;
- `recent_major_white_peace_country` for major participants;
- `recent_broad_white_peace` for broad-settlement pacing.

The timed flag durations are mirrored as file-scoped constants in `009_white_peace_effects.txt` because HOI4 timed-flag `days =` fields do not reliably accept script constants.

## Event Log and Cluster

White Peace is registered as Peace cluster ID `4` through `event_cluster_id.peace` and `event_cluster_peace`. `event_belongs_to_cluster` maps `constant:white_peace_event_log.event_id` to the Peace cluster, and cluster runtime preparation calls the White Peace context helper before firing.

The shared repeatable-event history recorder logs Event 009 after dispatch through `on_repeatable_event_fired`. Its default actor hook points the history row at `white_peace_primary`. The event details window, evolution detail previews, selected-evolution panes, history labels, settings cluster names, and Peace-cluster availability status have White Peace and Peace-cluster scripted-localisation branches.

## Achievements

Event 009 adds five achievements:

- `achievement_white_peace_status_quo_ante`: a player minor has a prolonged Event 009 war settled while independent and outside factions.
- `achievement_white_peace_no_winner`: a directly affected player country and its settlement partner both remain alive, independent, and uncapitulated after 180 days through the delayed Event 009 sender/recipient check.
- `achievement_white_peace_chain_of_tables`: six minor-country pairs are settled before any major-country settlement branch fires.
- `achievement_white_peace_silence_of_giants`: a player major is part of a long-war major-country settlement.
- `achievement_white_peace_the_circular`: one broad branch settles at least three separate safe conflicts or five safe pairs.

All unlock tracking is set only inside Event 009 settlement helpers or the delayed Event 009 survival check, so ordinary peace conferences cannot satisfy these achievements.

## Assets

- Report image: `GFX_report_event_009_white_peace`, backed by `gfx/event_pictures/report_event_009_white_peace.dds`, registered in `interface/009_white_peace_event_images.gfx`.
- Achievement icons: completed, grey, and not-eligible triplets for all five Event 009 achievements under `gfx/achievements/`, registered in `interface/chaosx_achievements.gfx`.
- Asset source, processed PNGs, prompts, contact sheets, and handoff notes: `docs/assets/009_white_peace/`.

No news image or animation is used. The broad branch uses the same restrained report presentation because the event remains administrative rather than spectacular.

## Helper Index

- `calculate_white_peace_dynamic_cap`: computes availability, war pressure, candidate counts, and live cap.
- `prepare_white_peace_runtime_context`: recalculates context and selects targets.
- `select_white_peace_branch`: chooses the current branch from stage and candidate availability.
- `select_weighted_white_peace_primary_candidate`: builds a scored country pool from valid pair candidates and randomly chooses a primary by score.
- `select_weighted_white_peace_partner_for_current_primary`: builds a scored enemy-country pool for the chosen primary and randomly chooses a partner by score.
- `score_white_peace_pair`: records the current selected pair score for diagnostics and log context.
- `apply_white_peace_pair`: applies pair settlement, memory, opinion, achievements, and delayed survival tracking.
- `apply_white_peace_current_context`: executes the selected branch and fires the correct report variant.
- `record_white_peace_evolution_if_needed`: records newly reached White Peace evolution rows through the shared evolution log.

## Future Plans

- Add a Stage III news popup only if repeatable event news presentation gains a stable pattern for quiet diplomatic circulars.
- Consider a reusable peace-candidate helper only after another Peace-cluster event needs the same safety gates.
