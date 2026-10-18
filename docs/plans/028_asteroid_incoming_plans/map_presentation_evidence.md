# Event 028 map presentation evidence and remaining gates

Archived verbatim from [map_presentation.md](../../events/028_asteroid_incoming/map_presentation.md). Headings and references are as they stood in that file.

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

