# Event 012 Africa niche host-binding handoff

Date: 2026-08-09.

Scope: final host-admission patch for the existing Event 006 shell tags HZX (Basotho/Basutoland), EUX (Eswatini/Swaziland), and ELX (Zanzibar). This handoff owns the narrow Event 012 host triggers and playbook effect guard. It does not create tags, states, releases, priority-member packages, portraits, GUI, ledger rows, or workbook rows.

## Outcome

Event 012 now admits one of these three shells only when all of the following are true: the live country keeps its original HZX/EUX/ELX identity, Event 006 has recorded the active-origin receipt, and the country owns and controls its own African core capital. The admission is deliberately state-ID-free because the installed map has no authoritative unique Basutoland, Swaziland, or Zanzibar state. A borrowed, acquired, occupied, or guessed fallback state cannot satisfy the gate.

Once the gate passes, the existing Event 012 initializer remains the sole content path. It preserves the selected country as `event_target:africa_host`, applies the existing compact playbook, and calls `africa_load_continental_focus_tree`; no cosmetic tag or country identity replacement is applied. The 22 full and 29 compact playbook definitions are unchanged.

## Country-package coverage checklist

| Surface | HZX | EUX | ELX |
| --- | --- | --- | --- |
| Event 006 tag registration | present | present | present |
| Event 006 country definition | shell only; runtime-owned map setup | shell only; runtime-owned map setup | shell only; runtime-owned map setup |
| Event 006 history | politics/popularity only; no start state | politics/popularity only; no start state | politics/popularity only; no start state |
| Event 006 origin receipt required | `is_independence_wave_registry_event6_origin` | same | same |
| Current-state admission | own and controlled African core capital | own and controlled African core capital | own and controlled African core capital |
| Event 012 playbook | `africa_host_playbook.basutoland` | `africa_host_playbook.swaziland` | `africa_host_playbook.zanzibar` |
| Depth/overlay | compact / southern Africa | compact / southern Africa | compact / Swahili and Indian Ocean |
| Existing first proof | preserved guarantee | diplomatic recognition | diplomatic recognition |
| Cosmetic identity change | none | none | none |
| Fallback state/tag | forbidden | forbidden | forbidden |

## Exact file surface

### Changed gameplay files

- `common/scripted_triggers/012_africa_triggers.txt`: added `africa_is_independence_wave_niche_host_tag` and `africa_is_valid_independence_wave_niche_host_binding`; inserted the fail-closed gate into `africa_is_eligible_host`.
- `common/scripted_effects/012_africa_effects.txt`: guarded the HZX, EUX, and ELX branches in `africa_apply_mapped_host_playbook` with the same current-state admission trigger. Direct calls therefore cannot assign niche playbook content to a bare or borrowed shell.

### Documentation file

- `docs/plans/012_africa_plans/012_africa_niche_host_bindings_final_2026-08-09.md`: this source-linked handoff.

### Reviewed but unchanged

- `common/country_tags/006_independence_wave_countries.txt:65,71-72`: HZX/EUX/ELX registration is already present.
- `common/countries/006_independence_wave_HZX.txt`, `006_independence_wave_EUX.txt`, and `006_independence_wave_ELX.txt`: graphical shells remain intentionally map-neutral.
- `history/countries/HZX - Basotho.txt`, `EUX - Eswatini.txt`, and `ELX - Zanzibar.txt`: no synthetic capital, ownership, OOB, industry, or technology was added.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt:1146-1161`: Event 006 blocked arrays remain authoritative; Event 012 does not bypass them.
- `common/scripted_triggers/012_africa_proof_triggers.txt`: homeland proof already requires the host's own capital to be a host core, so acquired-state proof remains impossible.
- `common/scripted_localisation/012_africa_scripted_localisation.txt` and `localisation/english/012_african_union_l_english.yml`: Basutoland, Swaziland, and Zanzibar problem/proof/leverage/rival text already exists and remains aligned with their playbook IDs. No unused localisation key was introduced.
- `common/countries/012_africa_cosmetic.txt`: no niche cosmetic identity exists or is needed; Event 012 preserves the original host tag.

## Event 006 evidence

The three tags are registered in `common/country_tags/006_independence_wave_countries.txt` as IW-124 Basotho (HZX), IW-125 Eswatini (EUX), and IW-116 Zanzibar (ELX). Their definitions and histories intentionally omit runtime state setup. The installed Event 006 scenario initializer places all three in blocked package arrays, and `is_independence_wave_registry_event6_origin` resolves to the active Event 006 origin receipt (`independence_wave_active_origin` plus `liberation_origin = independence_wave`).

The current Event 006 package-binding ledger remains unchanged: HZX and EUX are `disabled_no_unique_current_state`; ELX is `scenario_only_unbound`. Existing Event 006 and Event 012 handoffs explicitly prohibit a generic South Africa, Natal, Tanganyika, Mauritius, Comoro, or other substitute state. The new trigger therefore waits for a future approved runtime to materialise the exact shell rather than inventing map ownership.

## Event 012 host-selection and content evidence

`africa_has_mapped_host_playbook` continues to enumerate all accepted host IDs, and HZX/EUX/ELX remain compact rows. The static definitions remain 22 full rows and 29 compact rows; no row was removed, reclassified, or promoted. The new `africa_is_eligible_host` gate is only an additional condition for the three Event 006 shells; every other mapped host follows the pre-existing eligibility path.

`africa_initialize_selected_host` still saves the selected country as the global `africa_host` target, sets `africa_original_host_preserved`, applies the mapping, and calls `africa_load_continental_focus_tree`. The focus loader uses `africa_continental_focus_tree` for generic hosts and does not alter the country's original tag or apply a cosmetic identity. This is the complete cosmetic/content-loading path for a valid niche shell.

## Map and state setup audit

Vanilla state history and the bounded HOI4 map inspection were checked for the likely substitute IDs. The installed 1936 map has no state-localised or state-history entry named Basutoland, Swaziland, Zanzibar, Lesotho, or Eswatini. South Africa/Natal, Tanganyika/East Africa, Mauritius, Comoro, and Madagascar are existing states but are not authoritative unique bindings for these shells and are not used by this patch.

The read-only MCP map inspection covered state IDs 542, 546, 707, 708, and 719 plus selected African provinces. It returned `MAP_INSPECTED` with valid state membership, network, and geometry checks; the workspace-wide diagnostic stream remains noisy with unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` errors. The state render returned `MAP_RENDERED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24f66076c537b9030cd14c38066bd763d40b1462f65a5872796ceec4222530d9/ec3f0a32aa58f1ecdb14da53b9b0b267228df97d89c34fb002485c294d2275cd/map-state.png`.

No map write was requested or performed. There is no rollback surface because no map source changed.

## MCP event, focus, and map evidence

- Event 012 inspection: `EVENT_INSPECTED_PARTIAL`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfaea4ed09e60c34d810ba6d86ad77393cb42527aa70871ef8693fb316140e2f/196e09aad90cfdea6d46dd594124dc5a0ebe01ecb8d201179ee22a61a0203d9a/event-lint-08357425bddf.json`. The linked report is authoritative; inline inventory was truncated at 64 paths.
- Post-patch Event 012 scan: `EVENT_INSPECTED_PARTIAL`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/629e4ba01e5acace271fd36454e6800122feaf48da9268592cb876bf82ad85fe/0a8151b3611adb107f0b5ef79ad939a3ee6f74214bb044afd43a7bac1d2981c3/event-scan-a7b6a678b2d8.json`. The focused graph returned no MCP blocker; the linked workspace inventory remains authoritative.
- Event 012 render: `EVENT_RENDERED_PARTIAL`, overview artifacts include `event-overview-08357425bddf.svg` and `.png` under workspace artifact `f40169734f73a25fdf583971548de66de6f590753d0a71362868960f7b13260b`.
- Event 006 inspection: `EVENT_INSPECTED_PARTIAL`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0cd50a6bc8525bfb08756bb43927cb3772e8f76c7068dcd38d399a7b9569aadb/b217c36efabe49188d7bd8b104361547bb004834a2ac8bf3b5b92e7f60d0652a/event-scan-08357425bddf.json`.
- Event 006 render: `EVENT_RENDERED_PARTIAL`, overview artifacts include `event-overview-08357425bddf.svg` and `.png` under workspace artifact `8100fa0499e97814c887d5e2a7365913c78c4005e7d4fa7687fa55f23f7bfbb6`.
- Continental focus inspection: `FOCUS_INSPECTED`, 276 nodes, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e39d40639fe7d1c4f16bb8f9194aa2f871cf8fc782c13faa9afa6edda021f4c4/e661d27d995d0756a7ab0e6740c1ab41a87dbb9ad15c119ccfea12e0eb77219c/focus-inspect.3ef2ea9984cb47a0.json`. It reports the pre-existing 14 blocking layout diagnostics; no focus source was edited.
- Continental focus render: `FOCUS_RENDERED`, artifacts are `africa_continental_focus_tree.focus.html/.svg/.json` under workspace artifact `9d2f0664c6fb90d3e61211a8950574fb4bc963486d5a6e6b66b8621eec8bdc8f`.
- Map inspection: `MAP_INSPECTED`, artifacts `map-inspect.c04864e2f13d93d7.json` and `map-province-geometry.c04864e2f13d93d7.4b70a8b21d5558ab.json` under workspace artifact `ce55295aab9dd8270cd0c9c2687bf18852caec63dcfa7caef2f6c6c3640692d7`.

The installed package exposes no Technology Tree Viewer. Technology evidence was not needed for this host-binding-only change; if a future package adds technology prerequisites, that route is an unresolved tooling limitation and must not be substituted with source-only evidence.

## Validation

- `python .tools/audit_chaosx_country_tags.py` completed with zero external country-definition and identity-surface collisions.
- Source review confirms no new tag, state ID, owner transfer, capital assignment, release, cosmetic assignment, priority package, portrait, GUI, ledger, or workbook change.
- The matrix/source comparison still resolves 51 playbook IDs as 22 full and 29 compact; only the three niche branches gain the current-state receipt guard.
- The static full/compact lists and existing playbook branches remain intact; only the three niche branches gain the current-state receipt guard.
- The event, focus, and map MCP evidence above was collected read-only. No HOI4 process was launched, and no live campaign acceptance is claimed.

## Remaining risks and blockers

- HZX, EUX, and ELX remain dormant on the installed map until an approved Event 006 or later scenario runtime supplies a real country with an African owned-and-controlled core capital and the Event 006 origin receipt. This is intentional fail-closed behavior, not a fallback.
- The pre-existing Event 012 focus renderer reports 14 blocking layout diagnostics; this patch does not alter the continental tree.
- The map renderer reports unrelated workspace-wide building/port locator diagnostics; no state or map source changed here.
- Final live campaign, save/reload, and runtime event acceptance remain parent-owned.

No simplification or fallback was introduced.
