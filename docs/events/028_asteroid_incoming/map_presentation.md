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

`python -B .tools/validation/validate_028_presentation.py` exercises eight actual-source emission/receipt cases, all seven unique retirement IDs, pre-due/exact-due/repeated cleanup, duplicate-after-cleanup and a never-fired host.
It models conservative helper-temporary cleanup and treats graphical native effects as opaque primitives, not simulated engine outcomes.
The shared anchor closure is checked as 1,081 coordinate-only rows.
The existing news-delivery module is checked against its immutable source baseline so a map-helper filename collision cannot silently replace the queue, deduplication, annexed-reader or super-event-wait helpers.
The live `script_validate` check of STATE `create_entity` returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, checking syntax, command kind and declared scope only, with native arguments unresolved.
The proposed automatic-handle draft was replaced before commit by the reserved-ID design above, avoiding an unproved saved auto-handle identity assumption.
The first reserved-ID implementation's numeric `THIS.id` assumption was subsequently removed after inspecting the already named `qa_evt028.hoi4` save.
That save stores the original state-506 reference as `-10737.41318`, not plain integer 506, so it does not support arithmetic on that reference to allocate a graphical ID.
The source model now rejects numeric use of `THIS.id` and seeds every simulated state's real distinct anchor from the actual shared source ledger.
This corrects the model and source assumption without claiming that the earlier save executed either graphics-only implementation.

The connected server's live status resource reports stdio version 3.10.0 for this client's PID 27936, with two concurrent and four shared tool slots, captured on 2026-10-07.
The map request returned `MAP_LOOKUP_COMPLETED`, revision `f26a1d44c99dfcab52391b4d756f2dee2b881d72d94e2c5406bf0868b7fa3cea`, for states 16, 64 and 506 and province 6521, with no unknown province or missing geometry IDs.
It was explicitly lookup-only, not complete adjacency/railway/supply or native placement validation.
Map receipt: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c45211402178e169f6e3ec009583df63a3b4d7e2e034e314b293fcf2f38710ae/35be954d95e3892d316b38f231b6daf886885b1fb8f590c05e33879d8937b36d/map-lookup.f26a1d44c99dfcab.b0628a25f31fee55.json`.
The focused `.9` trace returned `EVENT_INSPECTED_PARTIAL`, revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0`, zero indexed helpers and one blocking diagnostic in its whole-workspace counts.
Its linked detailed report was not enumerated by the exposed resource inventory, which listed only server status; no omitted diagnostic or helper lifecycle acceptance is claimed.
That trace and the first helper lookup captured the temporary filename-collision draft, not the final separated module.
The 600-second scope-render observation timeout was retried with a one-node overview, while the matching source-overlay comparison uses current graphics source versus the immutable pre-change runtime in reverse direction.
Those pending results cannot be used as passing final-source evidence.
No native task negotiation, helper-expansion or job capability is inferred from server version or exposed routes alone.

Installed effects documentation: `create_entity` 3046–3068 and `destroy_entity` 3528–3537, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Offline Effects snapshot: corresponding commands at 366–367, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
Installed Script Constants: `documentation/script_concept_documentation.md` 215–244 and `common/script_constants/documentation.md` 12–31.
Vanilla entity/default-state/clone precedents: `gfx/entities/nuke.asset` 1–25, `particle_entities.asset` 162–180, `buildings.asset` 800–803 and ordinary blast presentation in `common/raids/air_raids.txt` 979–982.
The parent read the relevant local sections and the live revision-bound `create_entity` wiki/installed sections, rather than relying on a context bundle alone.

Open native gates include cloned attack-state playback, inherited particles/lights/sounds, province placement and zoom, pause/speed behavior, entity identity after save/restore, duplicate and annexed-host sequencing, actual retirement and zero nuclear native statistics/achievements/diplomatic/fallout effects.
The source separation eliminates the known detonation calls but does not establish these observed results.
No game was launched, no clean live error log is claimed, and the full Event 028 goal remains incomplete.
Future improvement: centralize a shared scripted-entity ID reservation registry if another subsystem adds map-entity allocation, with a fresh cross-owner collision audit before extending this band.
