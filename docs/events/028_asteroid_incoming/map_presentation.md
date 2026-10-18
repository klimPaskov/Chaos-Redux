# Event 028 graphics-only impact presentation

Disposition: implemented source separation and lifecycle, with native visual and save/restore acceptance open.
Acceptance basis: the user's explicit presentation-only reuse requirement and prohibition on nuclear use, damage, ledgers, condemnation, retaliation and fallout.
The October 4 decision to retain native detonation damage is superseded for this requirement by the graphics-only path, not treated as equivalent compliance.

## Exact consumers and flow

`gfx/entities/nuke_028_asteroid_incoming_visuals.asset` defines two presentation aliases.
`asteroid_incoming_main_visual_entity` clones installed `nuke_big_entity`, and `asteroid_incoming_fragment_visual_entity` clones installed `nuke_entity`.
Each sets `default_state = "attack"` while inheriting the vanilla mesh, animation, scale, particle, light and map-sound package.
No custom mesh, animation, DDS, icon, portrait, GUI, raid or bomb definition is introduced.
All existing 55 DDS consumers, super-event music and settings-aware music playback are unchanged.

The main-centre profile calls `asteroid_incoming_emit_main_visual` after its scripted physical receipts and crater registration.
The existing four-hour `.9` queue calls `asteroid_incoming_emit_fragment_visual` through its original wrapper.
Emission requires a recorded impact, an applied physical-state receipt, the exact matching main/fragment state flag and no previous visual receipt.
A miss reaches neither emitter and cannot seed the visual cache or add an entity, registry entry or cleanup obligation.

The emitters reuse `air_winter_visual_seed_anchor_provinces`, which contains only state-to-land-province coordinate writes.
They do not call Air Winter climate, schema migration, entity creation, suppression or ledger effects.
The shared ledger has 1,081 anchors, matching all 1,081 installed states, with every anchor belonging to its exact state and every anchor classified as land in `map/definition.csv`.
Examples are state 64/province 6521, state 16/province 11506 and state 506/province 12994.
No province is chosen from another state and no new hardcoded copy of the map ledger is introduced.
Any map revision must revalidate the shared ledger before this consumer is accepted.
An absent anchor produces `asteroid_incoming_visual_failed` without redirecting the impact or using detonation as a fallback.

## Private IDs, receipts and retirement

`common/script_constants/028_asteroid_incoming_visual_constants.txt` centralizes the private ID base and retirement grace.
The exact ID is `entity_id_base + air_winter_visual_anchor_province`, using the shared ledger's explicit numeric province literal rather than a typed state reference.
The 1,081 anchors yield 1,081 distinct reserved IDs, currently 15036 through 28408, with no overlap against the 5,406 audited existing/proof IDs.
Examples are state 64/province 6521/entity 21521 and state 506/province 12994/entity 27994.
Only seven sites can be live under the event's existing maximum fragment plan.
The ID is stored before `create_entity` and emitted as a literal through `meta_effect`, so retirement does not depend on an opaque auto-handle being captured or retaining the same identity after a reload.
The reserved band is separate from the current Air Winter five per-state bands, 3001–4081, 5001–6081, 7001–8081, 9001–10081 and 11001–12081, and its proof entity 8600064.
Current gameplay `create_entity` consumers are confined to these two owning modules, and installed vanilla has no scripted consumer beyond its documentation example.
This is a source allocation audit, not proof of native entity persistence or an undocumented ID-size limit.

`asteroid_incoming_visual_emitted` records dispatch once, not a claim that rendering was observed.
Normal state fields retain the reserved ID, emission transaction and cleanup due day.
The registry and `asteroid_incoming_visual_cleanup_active` are created only after a dispatch, so a campaign without an impact does not iterate an uninitialized visual registry.
The existing monthly host calls `asteroid_incoming_cleanup_expired_visuals` before the achievement and impact guards, visiting only registered sites.
Retirement begins after a 30-game-day grace period, and occurs at the next ordinary monthly visit, independently of dust, country existence, ownership, controller or achievement eligibility.
This is deliberately separate from the inherited real-time animation/particle duration, not a claim that game days equal presentation seconds.
Retirement removes the exact private graphical ID and cleanup fields, then clears the registry/active flag when no pending site remains.
The permanent dispatch receipt remains, so duplicate callbacks and retirement cannot replay the visual.

## Script/API contract

File: `common/scripted_effects/028_asteroid_incoming_map_visual_effects.txt`.
The existing `028_asteroid_incoming_presentation_effects.txt` news-delivery module is preserved and is not part of this graphics change.
Entry wrappers are STATE-scoped, require no caller outputs, and initialize `asteroid_incoming_visual_profile` before the shared emitter.
The shared emitter consumes that caller-owned temporary input and publishes only the private regular state fields/flags above.
`asteroid_incoming_clear_site_visual` is STATE-scoped and consumes its private reserved ID.
`asteroid_incoming_cleanup_expired_visuals` is COUNTRY-scoped for the existing global monthly host and uses only the visual-site registry.
Neither entry depends on `ROOT`, the original chooser, original target country or a live current controller.
Example: inside the already committed main-crater state, call `asteroid_incoming_emit_main_visual = yes`.

The complete graphical closure executes `create_entity` and `destroy_entity`, coordinate-cache writes and private visual bookkeeping only.
It contains no `launch_nuke`, stockpile debit, nuclear callback, population/building/unit damage, Deaths registration, Chaos change, fallout or diplomatic effect.
The retired timed-marker emitter is removed, so this path also cannot suppress a genuine subsequent nuclear strike for seven days.
Other owners' legacy nuclear-handler exclusions are not rewritten or treated as native proof.

## Evidence and remaining gates

The validation runs, live tool checks, save inspection and the remaining gates for this presentation are recorded in [map_presentation_evidence.md](../../plans/028_asteroid_incoming_plans/map_presentation_evidence.md). The graphics-only presentation contract above is the current design.
