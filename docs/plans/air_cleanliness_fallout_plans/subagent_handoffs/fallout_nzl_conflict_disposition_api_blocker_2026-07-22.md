# Fallout NZL Lifeboat conflict-disposition API blocker

Date: 2026-07-22  
Scope: NZL Lifeboat State pilot conflict receipts for Samoa (`726`) and the Aotearoa overlap (`284`, `723`)  
Owner: country-package audit  
Status: **blocked; documentation-only audit; no gameplay patch**

## Verdict

The dormant NZL package must remain dormant. A safe, generation-authenticated disposition API cannot be proven from the current repository, so this audit intentionally does **not** edit either of the two permitted gameplay files:

- `common/scripted_triggers/fallout_nzl_lifeboat_triggers.txt`
- `common/scripted_effects/fallout_nzl_lifeboat_effects.txt`

The existing activation gate can be satisfied by two country flags plus matching generation variables, but no gameplay producer sets those receipts. The global conflict-ledger validators define an explicit resolution enum and reciprocal provenance checks, but the source currently contains no resolution commit effect that a NZL-local effect could safely call or mirror. Writing the NZL flags or an enum locally would therefore create an unauthenticated receipt and could activate over a player-owned country, an event package, or a live release reservation.

No fallback, silent retirement, overwrite, release, state transfer, substitute package, on-action, activation caller, or global-allocation change was added.

## Country-package coverage checklist

| Surface | Current evidence | Audit result |
| --- | --- | --- |
| Tag and identity | `common/scripted_triggers/fallout_nzl_lifeboat_triggers.txt:7-40`, `fallout_nzl_assignment_identity_is_current` (`NZL`, memory `constant:fallout_country_memory.new_zealand_lifeboat_state`, region `constant:fallout_region.oceania_remote_islands`, archetype `constant:fallout_government_archetype.maritime_remnant`) | Identity contract is present; it does not resolve either conflict. |
| Exact state package | `fallout_nzl_has_exact_state_package` (`284`, `1079`, `723`, `1080`, `1081`) and `NOT = { 726 = { is_owned_by = ROOT } }` | The five-state shape and Samoa exclusion are fail-closed for current ownership; they are not proof of a reservation/disposition outcome. |
| Capital | `common/scripted_effects/fallout_nzl_lifeboat_effects.txt:522+` writes the package capital path (`284` then `1079`) | Existing package behavior is documented; no capital receipt is emitted by this audit. |
| Samoa / `SAM` | IW-175 loads `SAM` with package id `constant:independence_wave_package_id.iw_175` and anchor state `726` in `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt:279-295`; the planner reserves `726` at `:754-760` | Live-plan/player/event ownership and final resolution are not exported to NZL. `726` cannot be inferred safe from owner absence alone. |
| Aotearoa / `GRX` | `GRX` is registered in `common/country_tags/006_independence_wave_countries.txt:97`; scenario setup blocks IW-174/GRX in `common/scripted_effects/006_independence_wave_scenario_effects.txt:1137-1138`; the collision audit marks it `blocked_pending_distinct_identity` / `specific_variant_disabled` | Disabled registration is not a current retirement receipt. The overlap of `284` and `723` still needs an allocator-owned disposition. |
| Politics, leaders, portraits, flags, advisors, parties | Existing NZL package effects and prior handoffs cover runtime parliament, characters, cosmetic tag, and package assets | No issue in this conflict-API audit; these surfaces remain downstream of the dormant activation gate. |
| Focus, decisions, ideas, assets | Existing NZL focus/decision/idea files and localisation audits cover the package; activation is gated by `fallout_nzl_lifeboat_package_can_activate` | No new content is authorized. No icon, GFX, localisation, workbook, or asset file was changed. |
| Military, technology, industry, supply, production | Existing package setup is in `fallout_nzl_lifeboat_effects.txt`; no conflict disposition writes equipment, states, or supply | Not a safe basis for resolving Samoa/Aotearoa ownership; no balance or setup change was made. |
| AI and playability | `fallout_nzl_activate_lifeboat_package` is documented as dormant and has no gameplay caller; prior NZL proof notes the vanilla NZL alternate-AI retirement question | Playability remains intentionally dormant pending allocator receipts. |

## File-surface checklist and findings

### NZL trigger and effect surfaces

`common/scripted_triggers/fallout_nzl_lifeboat_triggers.txt:42-56` defines `fallout_nzl_conflict_dispositions_are_current` as:

1. `has_country_flag = fallout_nzl_samoa_disposition_resolved`;
2. `has_country_flag = fallout_nzl_aotearoa_overlap_resolved`;
3. one generation variable for each receipt; and
4. each generation equal to `global.fallout_transition_generation`.

`fallout_nzl_lifeboat_package_can_activate` at `:59-65` consumes that trigger. It does **not** check a typed disposition, source package id, source country, cleanup owner, output tag, player reservation, event ownership, or reciprocal global conflict row.

`common/scripted_effects/fallout_nzl_lifeboat_effects.txt:157+` contains `fallout_nzl_reset_package_runtime`; it intentionally clears NZL runtime state but does not create Samoa/Aotearoa receipts. `fallout_nzl_activate_lifeboat_package` at `:522+` is explicitly commented as a dormant entry point. A gameplay search finds only that definition; there is no event, decision, on-action, startup effect, allocator, or planner caller.

The two NZL receipt flags/variables occur only in the trigger. A source search for setters found no `set_country_flag = fallout_nzl_samoa_disposition_resolved`, no `set_country_flag = fallout_nzl_aotearoa_overlap_resolved`, and no setter for either generation variable. Generation equality alone authenticates freshness, not who resolved the conflict or what was resolved.

### Global conflict-ledger surfaces

`common/scripted_triggers/fallout_world_end_triggers.txt:2517-2629` defines `fallout_live_tag_conflict_resolution_is_current`. It expects `fallout_live_tag_conflict_resolved`, `fallout_live_tag_conflict_resolution_generation`, `fallout_live_tag_conflict_resolution`, and `fallout_live_tag_conflict_cleanup_owner`, validates the explicit enum range, checks player/event-package provenance, and checks reciprocal output/cleanup relationships. `fallout_successor_assignment_country_row_is_current` at `:2670+` consumes the same current row.

`common/scripted_effects/fallout_world_end_effects.txt:3002+` (`fallout_record_live_tag_conflict_row`) records a source row as `allocation_pending`; it does not commit a resolution. `fallout_reset_successor_allocation_ledger` at `:2858-2875` only clears resolution fields. `fallout_finalize_successor_allocation_transaction` at `:2936+` finalizes the transaction after validation but does not expose a NZL-specific disposition receipt. A source search found no gameplay setter for `fallout_live_tag_conflict_resolution`, `fallout_live_tag_conflict_resolution_generation`, `fallout_live_tag_conflict_cleanup_owner`, or `fallout_live_tag_conflict_resolved`.

The enum in `common/script_constants/fallout_world_end_constants.txt` is the correct shared type vocabulary (`continued_in_place`, `converted_existing`, `released_releasable`, `created_dynamic`, `retired_landless`, `preserved_event_package`, `player_reserved`, with `none` and `upper_bound`). Its existence does not prove a producer or a valid result for either NZL overlap.

### Independence Wave surfaces

- `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt:167-175` can plan IW-175 when the release plan is open, a plan slot exists, `SAM` is available, and `726` is an available anchor. This is a planning predicate, not a committed conflict disposition.
- `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt:279-295` loads IW-175 with `SAM`, Pacific reservation group, and anchor `726`; `:754-760` reserves the anchor. The reservation system does not write the NZL receipt fields.
- `common/country_tags/006_independence_wave_countries.txt:97` registers `GRX`, but no IW-174 loader/reserver is present in the searched package effects. `common/scripted_effects/006_independence_wave_scenario_effects.txt:1137-1138` places IW-174/GRX in blocked arrays. Static “blocked” state cannot be treated as an allocator-owned `retired_landless` or other resolution.
- The installed tag audit (`docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_07_22.md:122-129`) requires GRX to remain disabled unless a distinct, researched identity is proven. The manual disposition row (`006_vanilla_identity_manual_dispositions_2026_07_16.csv:14`) recommends additive NZL content if that proof fails. Neither document is a runtime receipt.

## Why no narrow gameplay patch is safe

1. Adding only typed NZL variables would still let a local caller assert an enum without the global source row, output relation, cleanup owner, and player/event provenance required by the global validator.
2. Adding setters to `fallout_nzl_lifeboat_effects.txt` would make the dormant country package its own allocator and could bless `726` while IW-175 is reserved or live, or bless `284`/`723` while a future Aotearoa package is active.
3. Treating blocked `GRX` as retired would silently resolve a curated-disabled package without a distinct-identity decision. Treating absent IW-175 runtime flags as safe would similarly conflate “not currently selected” with “resolved for this transition.”
4. Strengthening the NZL trigger to call the global current-row trigger is not sufficient by itself: the current global row is scoped to a live conflict country and does not identify a completed, state-specific Samoa or Aotearoa disposition receipt. A dedicated allocator-owned bridge is required.
5. There is no activation caller to test, and no map/state transfer is authorized by this scope. Any local patch would therefore be unexercised and could not prove post-resolution map safety.

## Required future disposition contract (handoff only; not implemented)

The allocator/planner should own a dedicated bridge and write it only after the global conflict transaction is committed for the same transition generation. The bridge should include, for each receipt, an explicit type using `constant:fallout_tag_conflict_resolution.*`, the transition generation, the affected state set (`726` for Samoa; `284` and `723` for Aotearoa), source package/tag identity, output tag when applicable, and cleanup owner. A commit marker may retain the existing NZL flags, but flags must never be the only proof.

The future NZL trigger should fail closed unless all of the following are true:

- `NZL` has a current successor assignment row and the exact five-state package; `726` remains excluded from NZL ownership;
- both typed receipts exist, have a non-`none`/less-than-`upper_bound` enum, and match `global.fallout_transition_generation`;
- the Samoa receipt names the actual IW-175/SAM source or an explicit allocator result, rather than assuming the planner is inactive;
- the Aotearoa receipt names the actual GRX/IW-174 source only if that package is genuinely live and resolved; a blocked registration is not a retirement result;
- player-reserved and event-package ownership are represented by the global provenance contract and are not overwritten; and
- reciprocal source/output/cleanup-owner validation passes before NZL activation is callable.

The bridge must be written by the future allocator/planner, not by `fallout_nzl_activate_lifeboat_package`, an on-action, a decision, an event, or a startup fallback. No disposition type is selected in this handoff because the current repo does not prove which result is semantically correct for either conflict.

## Validation and skipped validation

Meaningful checks run:

- Read the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, events, decisions, ideas, and AI, plus the relevant vanilla official documentation for variables, effects, triggers, event targets, and script constants.
- Inspected the NZL trigger/effect files, global allocation trigger/effect files, IW-175 planner/reservation files, IW-174 registration/blocking files, NZL spec/proof documents, and the installed IW collision audit.
- Searched gameplay sources for NZL receipt setters, global conflict-resolution setters, and activation callers. The only activation definition is `fallout_nzl_activate_lifeboat_package`; no gameplay caller was found.
- Confirmed the exact state identifiers, package ids (`iw_174 = 174`, `iw_175 = 175`), shared resolution enum, and current source paths cited above.

Skipped meaningful validation:

- No HOI4 launch, save test, focus render, event render, or map rewrite was run. The package is dormant, no caller exists, and this audit is explicitly documentation-only.
- No Technology Tree Viewer inspection was possible; the installed HOI4 MCP package exposes no Technology Tree Viewer. Technology is not a dependency of this conflict receipt.
- No global allocation, Independence Wave, GFX, localisation, workbook, asset, or map files were changed.

## Changed files and remaining blockers

Changed files:

- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_nzl_conflict_disposition_api_blocker_2026-07-22.md` (this handoff only).

No tags, states, leaders, parties, focus ids, localisation keys, formable ids, constants, or gameplay identifiers were changed.

Remaining blockers before any NZL disposition patch can be considered:

1. The live successor allocator must commit typed, generation-authenticated, state-specific Samoa and Aotearoa receipts with reciprocal source/output/cleanup provenance.
2. The allocator must expose a supported bridge to the NZL package; the country effect must not invent or copy global conflict rows.
3. IW-175/SAM must have an explicit current-plan/event/player resolution for `726`.
4. IW-174/GRX must remain blocked until a distinct identity is proven, or the allocator must emit an explicit non-overlap result; no static blocked flag may be interpreted as retirement.
5. A future allocator/planner caller must be identified and validated before activation is enabled. Until then, the NZL Lifeboat State pilot remains dormant by design.

No simplifications were made; the requested gameplay patch is incomplete by design because the required engine/repo semantics are not yet proven.
