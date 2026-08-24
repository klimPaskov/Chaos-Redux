# Event 020 Danimal rat free-route blocker handoff

## Outcome

The zero-cost Danimal rat route did not pass the mandatory semantic or geometry-binding gates. Runtime geometry, animations, GFX, sound definitions, and consumers remain unchanged.

## Files changed

- `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/evidence/free_animation_sources/danimal_action_audit.md`
- `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/rat_ground_unit_shared_model_job.yaml`
- `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/manifest.md`
- this handoff

The adapter also created only bounded evidence outputs: 24 `blender/previews/danimal_*_left.png` phase renders and their `logs/adapter/` request/result receipts. Failed request `96b5e03282b746aa931e9b3f72f58331` produced no checkpoint.

## Evidence and validation

- Environment verifier: `findings=[]`.
- Health request `44c85ce631684325869a762b21ff4c98`: adapter 1.9.2, Blender 5.1.2, `io_pdx_mesh` loaded.
- First successful exact-armature render request: `aa508e6936724e7784c7d7b10b8ab6e6`.
- All eight selected clips rendered at three phases from `Skeleton.001` with direct `Head.000` and `Body.000` consumers.
- Exact PNG hashes and visual review show cross-action equality, including all frame-0 poses, all attack variants at frames 0/10, `Run`=`Hit` at frames 5/10, and `Walk`=`Die` at frame 14. Eight distinct roles are not proven.
- Four-nearest binding request `96b5e03282b746aa931e9b3f72f58331` failed before mutation because `prepare_candidate` rejects `.blend` sources. Native Walk on the approved Meshy geometry was therefore not available to test.
- Credits estimated/consumed: `0/0`. No Meshy or marketplace call and no transaction.
- Ten accepted 44.1 kHz signed PCM16 mono audio candidates and their provenance are preserved unchanged; synchronization remains provisional because final actions do not exist.

## Required parent/tooling follow-up

1. Promote a narrow locked adapter revision that permits job-contained `.blend` input for `prepare_candidate`, or a job-contained Blender-to-FBX/GLB conversion operation, without unrestricted Blender Python.
2. Make source action inspection mute or resolve NLA/master-timeline overrides and emit action-curve or evaluated-pose hashes so each named clip can be proven independently.
3. Rerun the Danimal four-nearest binding and inspect Walk at start/mid/end before any batch.
4. Only if that binding passes, retain defensible Danimal-native roles and retarget Quaternius solely for genuinely missing roles. Do not relabel duplicates.
5. Parent retains all runtime wiring and in-game validation ownership.

## Blockers and simplifications

The requested eight-action package remains incomplete. No fallback, alias, procedural action, local keying, static replacement, purchase, trial, demo, marketplace spend, Meshy spend, or runtime mutation was used.
