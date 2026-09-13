# Event 006 Event 021 player-surface strict-gate repair

Date: 2026-09-12.

Disposition: **implemented source repair**. The Event 006 player-facing origin boundary is strict again. No package admission, allocator weight, cost, queue, pressure, country identity, or Event 021 internal setup behavior was changed.

## Defect

`common/scripted_triggers/006_independence_wave_triggers.txt` still admitted `is_independence_wave_event021_package_country` into both `is_independence_wave_event6_local_content_active` and `is_independence_wave_event6_player_surface_allowed`. A completed Event 021 compatibility receipt could therefore satisfy Event 006 category, decision, mission, cost, formable, or history-surface gates before a real Event 006 origin existed. This contradicted the accepted no-pre-event contract and the earlier origin-gate repair handoffs.

## Repair

- `is_independence_wave_event6_local_content_active` now requires `exists = yes` plus `is_independence_wave_active_country = yes`.
- `is_independence_wave_event6_player_surface_allowed` now requires the same active Event 006 origin and retains the four adapter-receipt exclusions.
- `is_independence_wave_package_content_active` remains unchanged as the internal Event 021 setup/cleanup bridge. Event 021 receipts still support bounded package preparation without publishing Event 006 player surfaces.
- No category, mission, cost, queue, pressure, request, history indication, or fallback was added.

## Validation

Focused validators pass against the repaired checkout:

- `python -B .tools/audit_event6_allocator.py --strict`: 149 publishers, 126 automatic/high-chaos candidates, 138 SCN-ranked candidates, 40 adapters, 32 attestations, 29 compatible groups, exact `3/4/5/7/10`, World Collapse `10`, and no pre-event category, mission, cost, or queue.
- `python -B .tools/audit_event6_country_api.py --strict`: 242 broad tags, 191 resolved carriers, zero missing, zero duplicates, IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py --strict`: 102 registered and 102 complete flag families.
- `python -B .tools/audit_event6_form16.py`: ARM/GEO/AZR contract pass.
- `python -B .tools/audit_event6_gui_matrix.py`: five tabs and all static/animated state contracts pass.
- `python -B .tools/audit_event6_scenario_matrix.py`: all 32 SCN-008 cells and eight edge cases pass.

The post-change read-only Event MCP retry returned the same cached graph revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d` and graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819` as the preceding request. Inspect returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e45434337fdfda54ce04734e77b032767b170040e9bad335c86dbaeb6affb63/236c783a90494a66646e692a21d583ce283a96f49c0c971d11a5e61c375ebbf6/event-lint-4bccb6ec7fe1.json`; render returned `EVENT_RENDERED_PARTIAL` with manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0641f047130fa836101d53185c9aa3a0ecdfffab8996411d48fe0d194ea056d4/c7cd817e70f09a53953ec0333ac68a75e6586fb75c1dd5a5d45483172c0beb56/event-overview-4bccb6ec7fe1-manifest.json`. The service deferred helper/lifecycle projections and did not expose a dirty-revision distinction, so this is partial structural evidence and not proof of the edited predicate. No live-game or save/load claim is made.

## Remaining risks

The 161 unattested selectable rows, eight adapter-only fail-closed IDs, typed probability evidence, rights/source gates, GUI dynamic-state evidence, and live/runtime evidence remain unchanged. This repair does not promote Event 021 packages or widen Event 006 admission.
