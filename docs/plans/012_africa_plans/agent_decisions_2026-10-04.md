# Event 012 agent decisions, 2026-10-04

The user granted the implementing agent full design authority for the Event 012 takeover after the Codex owners stopped.
Each entry below is an agent decision taken under that authority, with its basis and the implementation that carries it.
Disposition labels follow `CLAUDE.md` Specs and Plans.

## L1. Routed defects are closed

Disposition: `implemented`.

Basis: all six items in `inbox/012.txt` are fixed in `c19dbbc0a`, which is an ancestor of the takeover HEAD; the five touched files are clean and the 012 review confirmed the fixes.
No routed priority-1 defect remains.

## L2. Open the strange-formation package gate

Disposition: `implemented`.

Basis:

- The user approved the strange-force unit rebuild on 2026-09-27 and asked for every remaining model to be finished (`2026-09-27_strange_force_unit_rebuild.md`).
- `c5b475da9` installed the six rebuilt models (gorilla heavy infantry, pan sappers, stone cohorts, riverborn, forest giants, oracle recon), their eight actions, held items, entities, and timed sounds; `6162c7e99` re-rigged the plague carriers.
- Installed entities: `chaosx_gorilla_heavy_infantry_entity`, `chaosx_pan_sappers_entity`, `chaosx_stone_cohorts_entity`, `chaosx_forest_giants_entity`, `chaosx_oracle_recon_entity`, `riverborn_entity`, and `plague_carriers_entity`; the Disaster Wardens use the accepted vanilla `infantry_entity` override.
- All eight counters are registered in `interface/012_africa_strange_force_counters.gfx`, and both DDS files exist for each family.
- Every family has its timed sound entries in `sound/012_africa_strange_forces_sound.asset`.

The gate's own contract (model, entity, counter, and audio receipts per family) is therefore satisfied.

Decision:

- `africa_register_strange_force_asset_manifests` sets all 32 per-family receipts and then `africa_strange_formation_package_ready` in one effect.
  It runs on startup (new games and loads) and again inside `africa_initialize_selected_host`.
- Each spawn template names its entity explicitly (`override_model = <entity>_entity`), which is the form the wiki's Division modding page and most vanilla templates use.
- Each spawn's `set_technology` token exists in `common/technologies/012_africa_strange_force_technologies.txt`, and each equipment token exists in `common/units/equipment/012_africa_strange_force_equipment.txt`.
- The elephant formation stays outside this gate; its no-DLC model is commissioned separately.

Live check (`needs_live_game`): divisions spawned by Actions 74-76 and the focus and Tier A callers display their custom models.

## L3. Contribution helper package is adopted, not rewritten

Disposition: `accepted and queued` until the callers are wired.

Basis: the stopped thread's uncommitted contribution package implements the accepted measured-receipt design; a second recorder would duplicate its definition names.

Decision:

- F2: armour is measured per chassis.
- F4: amounts are integral by construction (`gods_of_africa_floor_equipment_amount` and whole-unit partial payments).
- No lifetime caps. Per-type stockpiles above the native getter's range are a live-game check, not a gameplay cap.
- Voluntary aid keeps its 500 shipment, 1000 capacity gate, and cooldown.

## L4. A treaty breach is the breach of an owned agreement

Disposition: `accepted and queued` until implemented.

Basis: WRA-04 ("commit then invalidate promised payment") and the grading design's "Agreements and reconciliation" section.

Decision: an agreement exists when the host accepted a substitute or an extension, a partial payment began on the current contract, the participant holds a live protection compact, or the participant has an accepted reconciliation or victor renewal.
A breach is failure, refusal, or war on an agreed contract, or war against the host while a compact, reconciliation, or renewal is live.
Generic offender marking stops creating treaty breaches.

## L5. Achievements and super-event are required

Disposition: `accepted and queued`.

Basis: the user's complete-Gods, no-simplification instruction tied to the full spec, and acceptance-matrix rows DOC-09 and DOC-10, which the matrix's completion rule makes blocking.

## L6. Super-event audio

Disposition: `accepted and queued`.

Decision: no file downloads, because downloading needs the user's explicit permission and no agent message can grant it.
Reuse a unique licensed track already archived in the repository if one exists; otherwise record the audio as `blocked` rather than ship a silent or duplicate cue.

## L7. Wrath floor ordering is not a defect

Disposition: `accepted and queued`.

Basis: the floor constants rise in assignment order (50, 60, 70, 70, 80).
The floor still moves to the maximum-floor helper during conduct integration.

## L8. `country_event` delays with constants stay unchanged

Disposition: `rejected` (no change).

Basis: `country_event = { days = constant:... }` in the diaspora and focus-route effects produced no load error in the live 012 logs, the lint sweep flagged only timed flags, and other owners use the same form.

## L9. Excluded items and stopped-thread files

Disposition: `accepted and queued` for the adoption; the excluded items keep their own dispositions.

- Excluded: the Buganda portrait (needs the user's own HOI4-style final), the archival `elephant_shared_base` package (kept, no deletion), and the controlled-pool and queued polity backlog (accepted backlog).
- The stopped thread's uncommitted `overview.md`, spec README, manifest, prompts, and Part 1 edits are finished and coherent (Event 070 catalog facts) and are adopted in the documentation commit with its untracked handoffs.
- `docs/testing/2026-10-03_event26_rsa_before/` is not this owner's and stays untouched.

## L10. MCP routes

Use only narrow calls and never `refresh=true`.
Known blockers to record instead of retrying: probability pools empty or incomplete, `event_compare` returning `EVENT_REVISION_NOT_CACHED`, artifact reads failing with `-32603`, and `focus_raster` timing out.

## L11. Order of work

Defects and the gate first, then the treaty-breach fix and contribution wiring, then conduct, the grader, the settlement obligation, delivery and its decision, then Enemy and World Is One consequences, achievements, the super-event, and AI.
Each step is committed through the shared-tree workflow with only this owner's paths or hunks.
