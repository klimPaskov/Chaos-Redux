# Event 018 cave-monster 3D integration addendum

## Disposition

Status: `bounded_integration_required`.

Broad Event 018 expansion remains closed.

The earlier RF-018-01 through RF-018-08 addendum is fully resolved, and this review does not reopen any of those mechanics or propose another route, country, doctrine, focus family, unit family, model variant, or visual layer.

The new 3D tranche is materially complete at the package level, but it is not ready for a closure handoff because the shared map entity does not currently resolve from any of the five brood `sprite` tokens and the installed audio hooks do not yet demonstrate the synchronization contract recorded by the audio handoff.

The parent should implement or explicitly reject the two bounded integration items below, refresh the affected crosswalk rows, obtain the user-owned live-consumer evidence, and then close this tranche without another broad improvement-loop pass.

## Evidence baseline

The selected mesh, idle, move, attack, revised death, diffuse, normal, and specular source files all match their runtime copies byte-for-byte by SHA-256.

All five large counter DDS files and all five on-map counter DDS files also match their selected evidence copies byte-for-byte.

The four runtime WAV hashes match `evidence/audio/sound_design_handoff.md`, and their measured durations are 24.240 seconds for idle, 6.384 seconds for move, 9.020 seconds for attack, and 6.000 seconds for death.

The model registration defines `resources_found_cave_monster_mesh`, the four animation types, and one entity named `resources_found_cave_monster_entity`.

The five sub-units instead declare `sprite = cave_monster_brood`, `sprite = cave_stone_phalanx_brood`, `sprite = cave_burrow_war_brood`, `sprite = cave_scree_tide_brood`, and `sprite = cave_anchor_guard_brood` at `common/units/018_resources_found_cave_broods.txt:110`, `:143`, `:176`, `:211`, and `:244`.

The offline Unit Modding reference states at lines 44 and 119 that `sprite = SPRITE` resolves the map model through `SPRITE_entity` by default.

No entity named for any of the five declared sprite tokens exists in the current `gfx/entities` source, and none of the five locked templates in `history/units/DHO_1936.txt` declares `override_model`.

The nearest installed-vanilla precedent is `common/units/infantry.txt` with `sprite = infantry` and `gfx/entities/units_infantry.asset:141` defining `infantry_entity` as a clone of the fully authored infantry base entity.

## RF-018-3D-01 — Resolve every brood sprite token to the shared entity

The preferred repair is to retain `resources_found_cave_monster_entity` as the canonical authored entity and add five lightweight entity aliases in `gfx/entities/018_resources_found_cave_monster.asset`:

| Sub-unit consumer | Declared sprite | Required resolving entity | Canonical clone target |
| --- | --- | --- | --- |
| `cave_monster_brood` | `cave_monster_brood` | `cave_monster_brood_entity` | `resources_found_cave_monster_entity` |
| `cave_stone_phalanx_brood` | `cave_stone_phalanx_brood` | `cave_stone_phalanx_brood_entity` | `resources_found_cave_monster_entity` |
| `cave_burrow_war_brood` | `cave_burrow_war_brood` | `cave_burrow_war_brood_entity` | `resources_found_cave_monster_entity` |
| `cave_scree_tide_brood` | `cave_scree_tide_brood` | `cave_scree_tide_brood_entity` | `resources_found_cave_monster_entity` |
| `cave_anchor_guard_brood` | `cave_anchor_guard_brood` | `cave_anchor_guard_brood_entity` | `resources_found_cave_monster_entity` |

This keeps the five bespoke counter identities stable while making every plurality-selected map model resolve to the same mesh, actions, scale, and sound states.

It must not create five duplicate meshes, five texture sets, or five animation packages.

Changing all five gameplay `sprite` tokens or adding template-only `override_model` values is not the preferred repair because it broadens the touched surface and can leave future or dynamically copied templates dependent on a separate exception.

If the parent chooses either alternative, it should first prove that all five counter token pairs still resolve and record why the alias pattern was rejected.

Static acceptance requires an exact entity resolution for each of the five declared sprite tokens, preservation of the canonical entity and source-to-runtime hashes, preservation of the ten counter registrations and hashes, and a corrected `runtime/crosswalk.md` table that records the full chain from sub-unit to sprite token to resolving entity to canonical entity.

User-owned live acceptance requires at least one division of each locked DHO template to display the cave-monster model at normal campaign zoom, remain grounded at the recorded 0.8 scale, enter idle and move without a T-pose or invisible fallback, enter attack, defend, and support-attack through the authored attack action, and use the authored death action when destroyed.

The same review must confirm that each of the five templates retains its distinct large and on-map counter art even though the 3D entity is shared.

## RF-018-3D-02 — Reconcile the sound handoff with the action timeline

The audio provenance and runtime hashes are complete, but the synchronization evidence is not yet aligned.

`evidence/audio/sound_design_handoff.md:10-12` assigns movement one-shots to four planted-foot phases in frames 0-24, attack onset shortly before the action midpoint, and the strongest death slide across frames 18-36.

`gfx/entities/018_resources_found_cave_monster.asset` currently attaches one untimed sound event at state entry for move, attack, defend, support attack, and death.

The action lengths are approximately 1.000 second for move, 1.333 seconds for attack, and 1.500 seconds for death at 24 FPS, while the installed clips are 6.384, 9.020, and 6.000 seconds respectively.

Closure therefore requires one of two explicit outcomes for each action.

The preferred outcome is mechanically trimmed derivatives from the same licensed originals plus timed entity events derived from the reviewed action frames, with no new generated, synthesized, recorded, placeholder, or unlicensed audio.

For movement, this means a short stone-contact derivative used at the four reviewed planted-foot phases rather than replaying a six-second bed as if it were four one-shots.

For attack and death, this means aligning the audible onset to the reviewed attack midpoint and collapse interval instead of relying on an undocumented state-entry offset.

The alternative outcome is an explicit user-approved revision of the sound-design handoff that defines the current files as state-entry ambient beds and records their intended overlap, interruption, and repetition behavior.

That alternative is a design change and must not be silently treated as though the existing four-phase and midpoint contract were implemented.

Idle may remain a long state-entry ambience if the live review confirms that it does not restart excessively, overlap distractingly, or continue implausibly after a state change, and the handoff records that accepted behavior.

Static acceptance requires exact runtime derivative durations, hashes, transformation steps, audible-onset notes, entity event timing, and action-frame mapping in `evidence/audio/sound_design_handoff.md` and `runtime/crosswalk.md`.

User-owned live acceptance requires move contacts to read as movement rather than continuous noise, attack onset to coincide with the visible strike, death collapse to coincide with the falling body, and repeated state changes to stay within the intended audible-density limits.

## Closure boundary and non-goals

No new gameplay mechanic, event, focus, decision, AI weight, probability pool, technology, doctrine, model variant, counter family, sound source, or historical claim is justified by this tranche.

The coherent shared creature model with five role-specific counters is the correct scope for the Oth-Kesh military identity.

Historical or regional research does not add useful value here because the issue is an engine consumer contract, not an unsourced cultural or historical design claim.

After RF-018-3D-01 and RF-018-3D-02 are implemented or explicitly rejected with reasons, the only remaining tasks should be the user-owned live consumer review, documentation reconciliation, a focused asset/runtime re-audit, and parent final review.

Additional models, route-specific skins, particles, new combat states, extra creature families, or more cave-unit types would add maintenance cost without closing either identified defect and should not be added in this pass.

## MCP evidence and limitations

The read-only Event Chain Viewer inspected and rendered `chaosx.nr18.1` before this conclusion.

The event graph revision is `04e76dcf50aebd2f59c678621af2f35f23cb37c45cce1ae2247f61362df19b6f`, with graph hash `637ae6c06bfdf10049ea537534e1e41a7565391041e0a3b4c62d7934331953ed`.

The neighborhood render selected 42 nodes, including `chaosx.nr18.1`, `.41`, `.50`, and `.60`, and produced JSON, SVG, PNG, and HTML artifacts with layout hash `1fce9faae5d7e75d2e666f7c563368fd4ed3d020172d025d32d9696956f5d5d1`.

The tool returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, and the render manifest is `complete: false` because fourteen Event 018 helper calls were unresolved by the viewer's active helper catalog.

Those diagnostics leave any whole-event chain-closure conclusion unresolved and must remain with the parent implementation review; they do not supply or negate the independent unit-to-entity resolution evidence above.

No focus, scripted GUI, or map surface is introduced by this addendum, so no focus, GUI, or map MCP conclusion is claimed.

No weighted AI, MTTH, random-selection, or custom-pool surface is changed or assessed by this addendum, so no probability balance conclusion is claimed.

The installed-package limitation specified for this planner remains recorded: no Technology Tree Viewer evidence is available for this review, and this addendum makes no technology or doctrine conclusion.

## Promotion and parent handoff

This file should remain under `docs/plans/018_resources_found_plans/` while either bounded item is unresolved.

It should not be promoted into the source specification because it does not change the accepted Event 018 design.

After implementation and live review, durable consumer, synchronization, hash, provenance, and validation facts should be reconciled into `docs/assets/018_resources_found/models_3d/cave_monster/manifest.md`, `runtime/crosswalk.md`, `runtime/handoff.md`, `evidence/audio/sound_design_handoff.md`, and the current model handoff.

The parent should then mark this addendum implemented, rejected, or superseded with a reason and issue a narrow 3D-tranche closure note rather than running another broad Event 018 improvement pass.
