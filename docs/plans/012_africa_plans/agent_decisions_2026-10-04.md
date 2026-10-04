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

Disposition: `implemented` (callers wired; native transfer semantics remain `needs_live_game`).

Basis: the stopped thread's uncommitted contribution package implements the accepted measured-receipt design; a second recorder would duplicate its definition names.

Decision:

- F2: armour is measured per chassis.
- F4: amounts are integral by construction (`gods_of_africa_floor_equipment_amount` and whole-unit partial payments).
- No lifetime caps. Per-type stockpiles above the native getter's range are a live-game check, not a gameplay cap.
- Voluntary aid keeps its 500 shipment, 1000 capacity gate, and cooldown.

Implementation choices taken under this decision:

- A measured short or unequal delivery is an accounted outcome, not an unresolved transaction: the delivered amount is credited once, the undelivered remainder stays owed on the contract, and the mismatch flag is kept as evidence.
  The adopted package had marked such a delivery unresolved, which would have blocked every later payment of that participant.
- A fuel payment is limited to Africa's free tank space before it is sent, so no participant loses fuel that Africa cannot store; the smaller shipment is a partial payment.
- A partly delivered accepted substitute becomes the contract terms instead of being rolled back, so delivered substitute goods are never lost.
- Family 13 records emergency political power only under the frozen, still-current emergency proof; every other political family fulfils its contract without material credit.
- Temporary helper inputs are read by value; `has_variable` is not used on temporary variables, because the offline wiki warns that temporary-variable presence across scripted-effect boundaries is unreliable.

## L4. A treaty breach is the breach of an owned agreement

Disposition: `implemented`.

Basis: WRA-04 ("commit then invalidate promised payment") and the grading design's "Agreements and reconciliation" section.

Decision: an agreement exists when the host accepted a substitute or an extension, a partial payment began on the current contract, the participant holds a live protection compact, or the participant has an accepted reconciliation or victor renewal.
A breach is failure, refusal, or war on an agreed contract, or war against the host while a compact, reconciliation, or renewal is live.
Generic offender marking stops creating treaty breaches.

Implementation choices taken under this decision:

- The agreement kinds are the schema-bearing `gods_of_africa_agreement` group (`tribute_terms`, `protection_compact`, `reconciliation`, `victor_renewal`); the agreed-terms receipt is bound to the open contract ledger ID, so it can never leak into the next contract.
- `gods_of_africa_record_treaty_breach` is the only writer of `gods_of_africa_treaty_break_count`, `gods_of_africa_unresolved_treaty_break`, `gods_of_africa_prior_treaty_break`, and the `gods_of_africa_broken_treaty` floor cause.
  Its Wrath gain is `gods_of_africa_wrath.treaty_breach_magnitude` (20), which replaces the ordinary refusal (8), failure (12), or war (10) gain.
- Defiance of agreed terms records the breach and keeps the separate defiance gain, because the participant both broke an agreement and left the system.
- One war breaks every live agreement at once and counts as one breach; the per-war dedupe flag clears at peace.
- An unresolved breach opens the same paid reconciliation window as permanent defiance, and the window only opens while the participant is at peace; a window cancelled by war is closed as missed once its due day passes, so a fresh window can open later.
- A war with Africa that cancels a contract without agreed terms records a separate `war_cancellation` history kind and the ordinary war Wrath gain, not a treaty break.
- Player-facing reports `.604` and `.613` name agreed terms, the new `.616` names the agreement a war broke, and the refusal and defiance rows warn when the open contract carries agreed terms.

## L5. Achievements and super-event are required

Disposition: `accepted and queued`.

Basis: the user's complete-Gods, no-simplification instruction tied to the full spec, and acceptance-matrix rows DOC-09 and DOC-10, which the matrix's completion rule makes blocking.

## L6. Super-event audio

Disposition: `accepted and queued`.

Decision: no file downloads, because downloading needs the user's explicit permission and no agent message can grant it.
Reuse a unique licensed track already archived in the repository if one exists; otherwise record the audio as `blocked` rather than ship a silent or duplicate cue.

## L7. Wrath floor ordering is not a defect

Disposition: `implemented`; `gods_of_africa_enforce_wrath_floor` now takes the maximum of the current causes.

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

## L12. Outstanding hostility is reconciled, not forgotten

Disposition: `implemented`.

Basis: the grading design's factor 6 and its Enemy rule ("an actual unresolved major-offense mark"), and its "Agreements and reconciliation" rule that only paid, host-accepted reconciliation resolves outstanding offences.

Decision:

- `gods_of_africa_unresolved_major_offense` is set by the conduct observation for war with the host, controlled or owned host-core territory, and defiance, and it stays until Africa accepts a paid reconciliation; prior war, occupation, defiance, and breach records are permanent.
- Because that mark makes a participant Enemy at the settlement, a participant that fought or occupied Africa without defying it must also be able to reconcile: `gods_of_africa_participant_needs_reconciliation` includes the mark, so the existing reconciliation window opens once it is at peace.
- Reconciliation requires that the participant neither controls nor owns any African core state of the host, matching the conduct resolver's two cached counts.
