# IW-133 BAN compatibility adapter handoff

Status: package-local preservation boundary added; central runtime wiring remains intentionally blocked by scope.

## Coverage checklist

- IW-133 resolves to the registered vanilla `BAN` tag, not the proposed `FCX` tag.
- The package remains `formable_or_route_only`; it is not admitted to the automatic Event 006 pool.
- Current binding is reservation group `RG-BENGAL-UNION`, anchors `430|431`, with current BAN capital/core on state `430`.
- Vanilla BAN history/country data, the generic focus fallback, GOE/RAJ focus tree, GOE/RAJ decision route, and UK release route were source-reviewed.
- Package-local guards require a living `BAN`, Event 006 origin, `iw_133` package id, explicit named-route marker, and the current anchor/core surface.

## Changed files

- `common/scripted_triggers/006_independence_wave_iw133_ban_compatibility_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw133_ban_compatibility_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw133_ban_compatibility_adapter_handoff_2026_08_14.md`

No assets, localisation, workbook, central adapter, attestation, preflight, or Join files were changed. No files were staged or committed.

## Findings and route risks

- Vanilla `history/countries/BAN - Bangladesh.txt` uses capital `430`; vanilla `history/states/430-Bangladesh.txt` has `add_core_of = BAN`, owner `RAJ`, and Calcutta state `431` has no BAN core in the installed baseline.
- `common/national_focus/india_goe.txt:15353-15397` (`RAJ_united_bengal`) bypasses when `BAN` exists. A living Event 006 BAN must not be counted as proof that the GOE Bengal route completed; the future caller must distinguish completed focus from bypass and preserve the normal branch when no Event 006 origin is present.
- `common/national_focus/india_goe.txt:15695-15706` (`RAJ_tryst_with_destiny`) is a named prerequisite/icon surface; it does not itself release BAN.
- `common/decisions/RAJ_GOE.txt:2098-2115` (`RAJ_GOE_princely_state_timeout`) transfers states to BAN only when living and non-subject, then can add BAN cores. Its surrounding pressure/cleanup logic also checks BAN existence at `1974-2177`.
- `common/decisions/RAJ_GOE.txt:1089-1148` (`RAJ_akhand_bharat_claim_ban`) adds RAJ cores to BAN-core states and can transfer subject-owned states. It is a separate named RAJ route that must not annex or recore an Event 006 BAN counterpart.
- `common/national_focus/uk.txt:3367-3450` (`ENG_the_three_nation_solution`) directly executes `release = BAN`, sets ENG autonomy, adds `ENG_guided_by_britain_raj_1`, resets BAN politics/popularity, and may add BAN to ENG wars. This is the primary destructive collision when an Event 006 BAN is already living.
- `common/national_focus/uk.txt:3520-3625` (`ENG_towards_indian_independence`) conditionally swaps BAN's guided-by-Britain idea and only raises autonomy when BAN is already a subject; the living-tag guard still prevents a sovereign Event 006 BAN from being treated as a fresh vanilla release.
- `common/national_focus/uk.txt:12409-12460` (`ENG_reclaim_the_jewel_in_the_crown`) can create an annexation wargoal against living BAN; this is a war route, not a release route, and remains parent-owned.

## Package-local boundary

`is_independence_wave_iw_133_ban_compatibility_contract` requires:

1. `exists = yes`, `original_tag = BAN`, and the Event 006 active-origin marker.
2. `liberation_origin = independence_wave` and package id `iw_133`.
3. `independence_wave_iw_133_named_route_selected` plus one of the named GOE/RAJ/UK route witnesses (`RAJ_united_bengal`, `RAJ_GOE_partition_has_happened`, or `ENG_the_three_nation_solution`).
4. BAN capital/core ownership on state `430`, with the paired `430|431` core witness retained for the reservation group.

`independence_wave_iw_133_ban_record_route_preservation` sets only the package-local `independence_wave_iw_133_ban_route_preserved` receipt. The caller must branch on that receipt before the destructive vanilla `release`, transfer, autonomy, politics, core, or annexation effect. `independence_wave_cleanup_iw_133_ban_compatibility` clears only the selector/receipt markers.

## Validation

- Read-only MCP `hoi4.focus_inspect`/`hoi4.focus_render` completed for `indian_focus_goe` (`common/national_focus/india_goe.txt`), `british_focus` (`common/national_focus/uk.txt`), and `generic_focus` (`common/national_focus/generic.txt`). The installed server reported source-linked trees and existing vanilla-wide icon/layout diagnostics; no BAN-specific tree exists.
- Read-only MCP `hoi4.map_inspect` completed for states `430`, `431`, and host mutex state `441`; the artifact reported the installed 1081-state map and existing unrelated map diagnostics. `hoi4.map_render` completed for owner layer with coast, port, victory-point, resource, building, supply, and railway overlays.
- Read-only MCP `hoi4.event_inspect`/`hoi4.event_render` completed for `GOE_RAJ_partition.1`, `GOE_RAJ.29`, `GOE_RAJ.30`, and `GOE_RAJ.33`. The installed Event Chain Viewer returned partial workspace-wide graphs (9,499 events, 8,266 unresolved nodes, 14 blocking global diagnostics) but selected route nodes rendered; this is structural evidence only, not live execution proof.
- No technology-tree viewer is exposed by the installed MCP package; no technology surface was changed or claimed.
- Source-level review of the two new scripted files was completed. Live HOI4 execution, map writes, central route wiring, probability audit, and game-launch validation were intentionally skipped because this tranche is package-local and parent-owned central wiring is out of scope.

## Remaining blocker / parent action

The compatibility boundary is dormant until a parent-owned source patch at the named GOE/RAJ/UK call sites invokes the contract and skips destructive vanilla mutation only for a living Event 006 BAN. Do not add IW-133 to central adapter/attestation/preflight/Join lists in this tranche. Preserve the normal vanilla GOE/RAJ/UK behavior whenever BAN is absent or lacks the Event 006 origin/package marker.
