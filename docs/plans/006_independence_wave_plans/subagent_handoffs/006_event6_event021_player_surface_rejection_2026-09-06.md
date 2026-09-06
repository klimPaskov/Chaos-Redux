# Event 006 / Event 021 player-surface boundary — 2026-09-06

## Disposition

Rejected the observed uncommitted Event 021 widening as incompatible with the accepted Event 006 origin boundary. The working tree was restored to the current Event 006 trigger authority; no Event 021 adapter receipt may publish Event 006 categories, decisions, focus content, history, queues, league systems, or evolutions.

## Authority and evidence

`common/scripted_triggers/006_independence_wave_triggers.txt` keeps `is_independence_wave_package_content_active` available for the bounded internal Event 021 setup window, while the explicit `is_independence_wave_event6_local_content_active` and `is_independence_wave_event6_player_surface_allowed` helpers both require `is_independence_wave_active_country` and exclude adapter receipts. This preserves the explicit invariant that nothing from Event 006 is visible before a real Event 006 origin fires and supplies the missing scripted-trigger definition used by existing categories, decisions, and focus content.

The rejected working-tree proposal introduced `is_independence_wave_event021_package_country` and allowed that predicate through Event 006 local-content/player-surface gates. It had no accepted design basis and conflicted with the source-of-truth map, quality checklist, resume packet, and player-surface origin-gate handoffs. Those widening additions were removed with a narrow patch. A nine-line active-origin-only definition for the already-referenced `is_independence_wave_event6_local_content_active` helper remains as the sole source correction.

## Scope limits

No Event 021 gameplay, achievement, asset, localisation, or adapter implementation was changed. Internal Event 021 compatibility/setup receipts remain available only where the committed Event 006 package-content predicate already permits them. A future change would require an explicit accepted design decision before any Event 006 player-facing surface is widened.

## Validation

- `python .tools/audit_event6_allocator.py --strict` continues to pass with the retired pre-event crisis surface and exact 3/4/5/7/10 ladder.
- `python .tools/audit_event6_gui_matrix.py` continues to pass the source contract for the five mutually exclusive tabs and cleanup.
- Source inspection confirms the Event 006 trigger file has no uncommitted diff after removal of the widening.
