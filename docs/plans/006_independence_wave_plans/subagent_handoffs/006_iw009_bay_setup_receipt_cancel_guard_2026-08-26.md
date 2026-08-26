# IW-009 Bavaria founding-mission setup-receipt guard — 2026-08-26

## Scope and result

This handoff covers the admitted IW-009 Bavaria founding-mission lifecycle in the Rhineland/Bavaria/Saar decision package.

The narrow receipt-loss guard is patched and left unstaged and uncommitted.

## Source evidence

`independence_wave_setup_iw_009_bavaria` in `common/scripted_effects/006_independence_wave_rhineland_bavaria_saar_package_effects.txt` clears `independence_wave_iw_009_setup_complete` at setup entry and only restores it after `has_prepared_independence_wave_iw_009_package_setup = yes` succeeds.

The existing mission activation for `independence_wave_bay_hold_the_state_together` already required that same receipt, but its pre-patch cancellation path did not.

The shared `has_stable_independence_wave_bay_state` trigger checks only the two settlement values, so the pre-patch successful cancellation branch could mark the crisis resolved without rechecking capital control.

The existing `independence_wave_cleanup_iw_009_bavaria` removes the mission, clears both value variables and crisis flags, and clears the IW-009 receipt, so no cleanup effect needed alteration.

## Changed files and identifiers

- `common/decisions/006_independence_wave_rhineland_bavaria_saar_decisions.txt`: `independence_wave_bay_hold_the_state_together` now cancels when `independence_wave_iw_009_setup_complete` is absent, and only resolves successfully when the Bavaria package, current receipt, stable state, and capital control all remain true.
- `common/decisions/categories/006_independence_wave_categories.txt`: `independence_wave_bay_state_category` now requires the current IW-009 setup receipt, hiding stale actions after a failed or retried setup.
- `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml`: `independence_wave_bay_hold_the_state_together_desc` tells the player that capital control is part of the founding mission.
- `docs/events/006_independence_wave/northern_western_europe_packages.md`: the Bavaria founding-crisis contract records receipt loss, capital loss, timeout, and category hiding.

## Before and after behavior

Before this patch, a stale receipt could coexist with an active mission whose activation had required that receipt, while the category remained visible.

Before this patch, a capital-loss cancellation could also take the successful-resolution branch if both value thresholds had been reached.

After this patch, receipt loss cancels into the existing failure branch, the stale category is hidden, and only the current receipt plus capital control and both value thresholds resolve the mission.

## Decision and mission audit notes

The category has one active founding mission and at most four founding projects before route content becomes available, so its initial phase remains within the visible-action and active-mission budget.

The two displayed values are named, show their current values out of 100, state the shared threshold of 60, and are connected to distinct civic and security project outcomes.

The mission is owned by IW-009 Bavaria, requires its package and current setup receipt, lasts 480 days, resolves on both value thresholds plus capital control, fails on receipt loss, package loss, capital loss, or timeout, and has no duplicate mission in the category.

The project mutex `has_independence_wave_bay_active_package_project` limits the category to one active project at a time.

The in-scope spendable-cost strings remain icon-first and stay at four or fewer distinct cost types: administration light has command power, manpower, and civilian factories; security light has command power, infantry equipment, and support equipment; diplomatic standard has command power plus one dynamic transport type; security standard and security major each have manpower, army experience, infantry equipment, and support equipment; strategic has stability, command power, one dynamic transport type, and civilian factories.

No AI weight, target-selection, random, or route unlock was changed; the mission retains its existing constant-backed urgent AI score, so no probability comparison was applicable to this patch.

No dedicated scripted GUI is owned by IW-009, so `hoi4.gui_inspect` and `hoi4.gui_render` have no in-scope GUI surface to inspect or render.

`hoi4.event_inspect` was run against `chaosx.nr6.10` and returned partial structural evidence at revision `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e5931721c7013aa64bcf6023148061be71d938a5870abce0ca6ff7516d539de/e6ae974941dd26851b7c930a8b01e01c9c9ee31a63861435a36678b58d580ab8/event-trace-744cd12bca3e.json`.

The installed MCP exposes no decision or mission inspection route, so the lifecycle proof remains source- and validator-backed rather than an equivalent direct MCP decision projection.

## Focused validation

The static lifecycle assertion passed for setup clear and prepared-branch restore, activation receipt, receipt-loss cancellation, receipt and capital guarded resolution, receipt-gated category visibility, existing cleanup, player-facing capital text, and technical lifecycle documentation.

`python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 32 attested packages, and the existing `RG-RHINE-SAAR` capacity of two distinct packages.

`git diff --check` passed for the four touched gameplay, localisation, and documentation files.

No live game run was performed, because live validation belongs to the user.

## Remaining issues and boundaries

No further package analogue was assessed in this tranche.

No shared GUI, super-event, focus, broad pool, cost balance, scripted trigger helper, or cleanup architecture was changed.

The working tree remains intentionally unstaged and uncommitted.
