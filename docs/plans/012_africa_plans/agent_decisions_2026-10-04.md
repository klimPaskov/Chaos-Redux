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

Disposition: `implemented` for the adoption (documentation commit of 2026-10-04); the excluded items keep their own dispositions.

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

## L13. Final settlement: twelve-factor grade, frozen obligation, donor-backed delivery

Disposition: `implemented` (native transfer deltas and the decision row's appearance are `needs_live_game`).

Basis: the accepted grading design (`subagent_handoffs/012_africa_gods_full_grading_rewards_design_2026-10-03.md`, accepted by the parent on 2026-10-03 under the complete-Gods goal) and the takeover remaining-work list.

Decisions:

- The endpoint runs three passes over the retained census: classify (freeze host Strength and doctrine once, neutral-retire, refresh conduct, freeze inputs, classify with the `full_grade` triggers), initialize obligations and standing diplomacy, then one delivery batch, finalization and `.608`.
  The old flag-based `gods_of_africa_final_*_is_valid` triggers, the flat 2500/1000 packages and the political-power fallbacks are removed, together with their constants.
- A broken accounting invariant leaves `gods_of_africa_settlement_grade_unresolved`, keeps the evidence, cleans live authority, and assigns no standing or obligation.
- The end-phase delivery is a separate untargeted row, `gods_of_africa_deliver_settlement_support`, in the host category with the settlement icon.
  The targeted commit row lists live participants, which are gone after the endpoint, and one fair batch cannot be expressed as a per-recipient target without giving the clicked target priority.
  The commit row keeps its pre-endpoint behaviour and disappears at the endpoint, so the player sees the delivery row take its place.
- The delivery row re-enables after 30 days, so each use moves one real batch and an AI host cannot drain its reserves every day.
- A receiver at war with Africa keeps its balance and is skipped until peace; Africa does not arm a current enemy.
- Distrusted standing records Africa's suspicion one way (the participant has no grievance to remember); Enemy standing records hostility both ways.
- The report cause has six values (`gods_of_africa_settlement_cause`): sustained, mixed, inconsistent, unrecovered, no record, and hostility.

## L14. Gods records in World Is One and the Gods AI weights

Disposition: `implemented`; the probability audit is `blocked` (route below).

Decisions:

- World Is One reads the Gods record through the existing `gods_of_africa_world_history_*` flags, which are now set from the frozen settlement standing (or, before it, from permanent defiance and unresolved broken agreements) for every country with Gods history, on top of the Scramble-derived seed.
  New markers: `gods_of_africa_world_history_voluntary_partner` (voluntary aid given) and `gods_of_africa_world_history_holdout` (permanent defiance).
- Consumers are weights on existing World choices, from `africa_world_package_protocol` constants: invitation AI x2 for a Favored constituent, constituent accept x2 when Favored, refuse x2 when Distrusted and x4 for a holdout, counterterms x1.5 for a voluntary partner, coercion AI x2 against a holdout.
  The existing Enemy exclusion from founding invitations and the holdout war-target signal are unchanged.
- Doctrine weights come from the new `gods_of_africa_ai` group: base 10; Reciprocal Covenant x3 at peace and x1.5 when a participant has proven reliable; Sovereign Exaction x3 at war and x2 when a participant holds African core territory of the host; Strategic Ambiguity x4 from Chaos tier 4.
- The two Gods missions are opened only by the owner and closed only by response decisions or timeout, so their AI score is an explicit zero.
- Deliver settlement support: base 10, x0.25 while the host is at war.

MCP route evidence (2026-10-04): `hoi4_probability_inspect` rejected every adapter-bearing call (`decision_ai_will_do` with a candidate pool, with a relative-path source, and alone) with "Invalid tool arguments", and an argument-free call returned `INTERNAL_ERROR` with zero artifacts.
No baseline or same-scenario compare could be produced; per the takeover instruction the route was not retried in a loop.
The weights above therefore carry no probability evidence and are listed for the separately routed AI probability audit.

## L15. Gods focus overlay layout

Disposition: `implemented`.

Narrow `hoi4_focus_inspect` of `africa_continental_focus_tree` (one call before, one verification call after; no raster) and a source position check of the 24 `gods_of_africa_focus_*` nodes found two overlay defects and no overlaps or same-row spacing faults:

- The entry prerequisite from `africa_identify_host_problem` (34, 0) to `gods_of_africa_focus_prepare_proclamation` (70, 16) drew a line across eleven other connectors.
  The overlay now starts its own column: the prerequisite became `has_completed_focus = africa_identify_host_problem` in `available`, which keeps the same requirement.
- The line from `gods_of_africa_focus_continental_arsenals` to `gods_of_africa_focus_continental_reserve` ran through `gods_of_africa_focus_rails_ports_fuel`; the two children now sit side by side at (61, 24) and (63, 24).

No non-Gods node moved. Before: revision `1f577e13`, 320 diagnostics, 70 connector crossings, 59 node intersections. After: revision `efaa6f4c`, 297 diagnostics, 62 crossings, 53 node intersections, no blocking diagnostics. The remaining diagnostics belong to the shared continental tree outside the overlay. No raster was rendered (`focus_raster` timed out in earlier runs), so the visual appearance remains a live check.

## L16. Gods of Africa achievements

Disposition: `implemented` (in-game unlocking is `needs_live_game`).

Basis: full spec "Achievement directions" and agent decision L5.

Decisions:

- Ids follow the established Event 012 prefix: `africa_gods_long_obedience`, `africa_gods_survive_defiance`, `africa_gods_continental_provision`, `africa_gods_careful_gambler`.
- "High Strength" for Survive Defiance is the continental band (Strength 60 or more) at the moment of defiance; capitulating while at war with Africa, or to Africa, disqualifies.
- "Several refusals" for The Careful Gambler is 2: under the grader, three refusals make a country Enemy and Respected allows fewer than two refusals (three under Strategic Ambiguity), so 2 refusals is reachable with Favored standing, or Respected under Strategic Ambiguity.
- Continental Provision counts only fulfilled contracts from countries that were major powers when they paid, by original demand family.
- Icons use native-transparency ImageGen subjects processed by the achievement workflow; no background removal was needed.

## L17. Proclamation news ships; the global-credibility super-event is blocked on audio

Disposition: news event `implemented`; super-event `blocked`.

- The activation owner fires the major news event `chaosx.nr12.617` once per campaign, guarded by `gods_of_africa_proclamation_news_sent`; `major = yes` shows it to every country, matching vanilla `news.1`.
  Its picture `GFX_news_event_012_africa_gods_proclaimed` is a native ImageGen documentary scene converted to a 397x153 black-and-white DDS (source and processed copies under the local `docs/assets/012_africa/news/`).
- The super-event needs a unique, licensed track already archived in the repository (decision L6).
  The only archived Event 012 sources are the Beethoven Eroica II and Brahms Symphony 4 IV recordings already used by roles 2 and 3, and the shared `docs/super_events/source_audio` archive holds no other track; a second excerpt of a used recording is a duplicate cue, not a unique track.
  Downloading a new track needs the user's explicit permission, which no agent message can give.
  Exact missing input: one licensed, archived, unused track (about 110-120 seconds) for the Gods global-credibility role.
  Until it exists, no silent or duplicate super-event is shipped; the trigger contract stays as in the full spec (fires once while the Gods are active and the host is valid, when Strength first enters the global band, or at activation if it already qualifies).

## L18. Round 1 review fixes

Disposition: `implemented` (fuel-room gate and agreed-terms change are `needs_live_game` for appearance and native fuel readings).

Basis: the skeptical round 1 review of the takeover commits, under the same full design authority.

- `gods_of_africa_participant_owns_host_core_state` was defined twice (`012_africa_gods_epoch_binding_triggers.txt` and `012_africa_gods_triggers.txt`), which the engine reports as a duplicate scripted trigger; the second definition and a repeated `NOT` line in `gods_of_africa_participant_can_reconcile` are removed.
- A full payment that arrives short (for example fuel limited by Africa's tank space) no longer turns the contract into agreed terms. Only the participant's own partial-payment decision does, as its tooltip already says; otherwise a click on "Fulfil the Demand" could expose the participant to a broken-agreement penalty it was never warned about.
- "Fulfil the Demand" and the partial payment need room in Africa's fuel tanks for a fuel demand (`gods_of_africa_host_can_receive_demand_payment`, tooltip `gods_of_africa_host_fuel_room_tt`). Before, a full tank made the click do nothing and let the AI retry it every day.
- The delivery row's re-enable interval reads `gods_of_africa_settlement_delivery.reenable_days`, and the achievement tooltips read their thresholds from `gods_of_africa_achievement` instead of repeating the numbers.
- The settlement equipment budget creates `gods_of_africa_floor_output` before calling `gods_of_africa_floor_temporary_value`. The offline wiki warns that a temporary variable first created inside a scripted effect may not survive its return; without this the army reserve could fall back to the 500 floor and a batch could strip Africa's army stock.
- The unused single-participant wrapper `gods_of_africa_commit_participant_settlement` is removed: settling one participant alone would skip the host's owed totals.
- The archive cleanup no longer clears the emergency proof and substitute terms twice.

MCP route evidence (review, 2026-10-04): one narrow `hoi4_probability_inspect` call (`decision_ai_will_do` with the three doctrine decisions as the candidate pool) and one `hoi4_decision_inspect` call (`mode = inspect`, `id = gods_of_africa_deliver_settlement_support`) both returned "Invalid tool arguments". The probability audit stays `blocked`; neither route was retried.

## L19. Tribute credit follows the participant's loss; empty payments lock briefly

Disposition: `implemented` (the native delivery timing of `send_equipment`, fuel and political-power transfers is `needs_live_game`).

Basis: the round 2 remaining-work list (priority 1) and the offline wiki's description of `send_equipment` as removing equipment from the sender; a participant that gave goods up must not lose them uncredited when Africa's same-tick gain reads lower.

Decisions:

- `gods_of_africa_complete_material_transfer` credits min(request, the participant's measured loss).
  Africa's measured gain is no longer a cap on the participant's credit; it is published separately as `gods_of_africa_payment_received` (never more than the credited loss), and Africa's own stock accounts (`africa_common_defence_stockpile` for demanded and voluntary rifles) read only that gain.
  `gods_of_africa_material_transfer_mismatch` and the native delta outputs keep the evidence when the two sides differ.
- A payment, accepted substitute or voluntary shipment that moves nothing (`gods_of_africa_payment_delivered` zero) calls `gods_of_africa_record_undelivered_payment`: a `.604` row (`gods_of_africa_response_undelivered_report`) says the shipment arrived empty, nothing is credited, and `gods_of_africa_payment_retry_day` closes the same answer for `gods_of_africa_timing.undelivered_retry_days` (7) days.
  The lockout is read by `gods_of_africa_payment_retry_is_open` in Fulfil, partial payment, voluntary aid and Africa's substitute acceptance.
- Every payment gate shows a localised reason instead of a hidden trigger: the demand is still on record, earlier shipments are confirmed (`gods_of_africa_material_transaction_unresolved` blocks only measured families, never political ones), and the retry delay has passed.
  Africa's substitute acceptance also requires that the offering country still holds what it offered, because a failed affordability check used to leave the button live with no effect.
- Every one of these decisions has an explicit `factor = 0` AI modifier while its gate is closed.
- A material demand that an unaccounted earlier shipment made unpayable lapses at its deadline as a neutral retirement (`.604` row `gods_of_africa_response_lapsed_report`) instead of a failure with Wrath and punishment, because the participant had no way to pay it.
  The report-only kinds `undelivered` (17) and `lapsed` (18) extend `gods_of_africa_history_kind` and are never written to the history arrays.

## L20. Only the aggressor breaks an agreement, and one war adds one Wrath gain

Disposition: `implemented` (which side the engine reports as attacker for co-belligerents is `needs_live_game`).

Basis: the round 2 remaining-work list (priority 2) and the lead's decision that a treaty breach requires the participant's own aggression; this replaces L4's "war against the host" wording for the breach factor only.

Decisions:

- A war breaks the participant's live agreements, or agreed contract terms, only when the participant is on the attacking side against the host: `has_offensive_war_with = event_target:africa_host` (`triggers_documentation.md` `has_offensive_war_with`), which also covers joining an attacker's war.
- When Africa is the aggressor (`event_target:africa_host = { has_offensive_war_with = PREV }`), the agreements end without a participant breach: protection is withdrawn through `gods_of_africa_withdraw_protection_package`, the reconciliation stops being live, a renewed recognition ends through the new `gods_of_africa_victor_renewal_ended_sequence` (not the breach marker), the history records the new kind `agreement_ended_by_host` (19), and the participant sees `.616` "Africa Breaks Its Word" or a `.613` line naming Africa.
- An open contract cancelled by Africa's own war is retired neutrally (it no longer counts as broken by war in the grade) and adds no Wrath. Wrath measures Africa's grievance against the participant, and a war Africa started is not the participant's offence.
  War and occupation conduct marks, the war Wrath floor (50) and the outstanding-hostility mark stay exactly as before, as the lead required.
- One war produces one Wrath gain: the wartime cancellation applies the breach gain (20) when an agreed contract or any live agreement stands, otherwise the ordinary war gain (10), and sets the per-war flag `gods_of_africa_agreement_war_breach_recorded`, which the owner review's agreement observation reads; the flag clears at peace.
- `gods_of_africa_retire_interrupted_contract` closes a contract as broken by war only when the participant attacked Africa; otherwise it retires it.

## L21. A partly delivered substitute is re-based as the contract's own terms

Disposition: `implemented`.

Basis: the round 2 remaining-work list (priority 2); L3 already made a partly delivered accepted substitute the contract terms, but left the original family's total and partial shipment in place.

Decision: when part of an accepted substitute arrives, `gods_of_africa_resolve_substitute` sets `gods_of_africa_demand_amount` to the substitute amount and calls the new `gods_of_africa_compute_partial_payment_amount`, the same helper contract creation now uses (partial ratio constants, whole units for equipment, never below one, capacity requirement refreshed).
The mission then shows the substitute family with matching remaining and total figures, and a partial payment is half of the substitute rather than an infantry-sized half clamped to the whole tank balance.
The rejected and failed substitute paths are unchanged.

## L22. Gods overlay rewards are visible and later nodes appear at their evolution

Disposition: `implemented` (in-game appearance of the expanding branch and tooltips is `needs_live_game`).

Basis: the accepted focus integration ("The branch should visibly expand at this milestone through new nodes or changed availability. It should not reveal every later focus from the start.") and the round 2 remaining-work list.

Decisions:

- Evolution II nodes (Rails, Ports, and Fuel; the Continental Reserve; the Hand of Judgment) add `africa_evolution_ii_logged`, and Evolution III nodes (Security Oaths; Sanctuary for Reliable Partners; the Last Sentence; Africa Speaks for Itself) add `africa_evolution_iii_logged` to `allow_branch`.
  The Hand of Judgment is the spec's "Evolution II or III" node; it takes the Evolution II gate because its `available` already required Evolution II. Its Evolution III children stay hidden until their own evolution.
  The layout refresh was already in place: `africa_activate_evolution_ii` and `_iii` call `africa_refresh_continental_focus_tree_layout`, which runs `mark_focus_tree_layout_dirty` on the host.
- Every overlay node whose reward only set a country flag now shows a `gods_of_africa_focus_<name>_tt` effect tooltip in plain current wording; the Office of the Voices also shows the public-pardon unlock, Record Every Refusal shows the mark-offender and escalate-offense unlocks, and the Continental Proclamation's duplicate leniency unlock is replaced by the doctrine-choice tooltip.
- The Hand of Judgment no longer shows `gods_of_africa_permanent_defiance`, a participant decision; its host-facing tooltip states what Africa gains.
- The optional Sacred State / Veiled Instrument fork is `rejected`: the spec marks it optional ("Add it only if Event 012's existing political routes can support it without clutter"), and the three doctrine decisions already cover how Africa handles ambiguity. The four dead localisation keys are removed.

MCP route evidence (2026-10-04, round 2): one narrow `hoi4_focus_inspect` call (`mode = national`, `treeId = africa_continental_focus_tree`) returned revision `23b4daad`, 300 focuses, 297 diagnostics, 62 connector crossings and 53 node intersections, the same counts as the L15 after-state, so the edits added no overlap or crossing. Its single blocking diagnostic is an unexpected brace in the vanilla file `game:common/national_focus/TSR_lingguang_incident_joint_branch.txt`, outside this mod. No raster was rendered.

## L23. Tribute and reconciliation pause only for war with Africa; other wars ease the demand

Disposition: `implemented` (native `surrender_progress` readings for co-belligerents are `needs_live_game`).

Basis: spec acceptance rows DEM-14 ("Target at war with Africa: ordinary demand pauses") and DEM-04 ("Target near capitulation with empty reserves: demand is delayed, reduced, or moved to valid nonmaterial family"), the full spec's "War with Africa" and "Rare reconciliation" sections (which require only no active war with Africa), and the round 2 remaining-work list (priority 1).
The any-war gates came from Codex commit `0edbcc217` ("not a wartime tax"); that was an implementation choice with no user decision or spec row behind it, so it is replaced rather than kept.

Decisions:

- Demand dispatch (`gods_of_africa_participant_can_receive_demand`), reconciliation (`gods_of_africa_participant_can_reconcile`, `gods_of_africa_start_reconciliation`) and the reconciliation mission's `cancel_trigger` exclude a participant only while `has_war_with = event_target:africa_host`.
  The held- and owned-host-core requirements for reconciliation are unchanged.
- A participant at war elsewhere gets an easier demand: the demand scale drops by `gods_of_africa_demand_scale.wartime_delta` (20 points) and by `losing_war_delta` (25 more) above `gods_of_africa_hardship.losing_war_surrender` (0.25 surrender progress); the deadline grows by `gods_of_africa_timing.wartime_deadline_extension_days` (30) and `losing_war_deadline_extension_days` (30 more).
- Above `gods_of_africa_hardship.near_capitulation_surrender` (0.5) the family ladder asks only for political tribute (emergency relief while Africa has an emergency, otherwise recognition once that lane is open); with neither, the demand is postponed by `gods_of_africa_timing.hardship_postpone_days` (60).
- Any participant Africa cannot quote is passed over for `gods_of_africa_timing.unquotable_retry_days` (30). Before this, the dispatcher kept choosing the first eligible participant in the registry every seven days even when no contract could be formed for it, so later participants could starve.
- The `.603` demand and the demand mission say when and why the demand was eased (`GetGodsOfAfricaDemandHardshipLine`); the wartime cancellation tooltip and the broken-agreement tooltip name the war with Africa explicitly.
- Emergency relief is paid in political power, but `gods_of_africa_transaction.emergency_amount` was 500, which almost no government holds, so the emergency lane and the near-capitulation path could never form a contract. It is 50, on the scale of the other political families, and the unpayable-candidate fallback to emergency relief applies only while Africa has a real emergency need (`gods_of_africa_need_emergency`), so the family name never describes a demand Africa has no emergency for.
  The grading's emergency package (`gods_of_africa_contribution_units.emergency_pp_per_package`) moves from 500 to 50 with it, so one base emergency demand still counts as one emergency package.

## L24. Gods AI responses follow the campaign state

Disposition: `implemented` (scores only; the normalized probability audit is `blocked`, see below; live AI behaviour is `needs_live_game`).

Basis: the full spec's "AI design" section (participant archetypes "should emerge from campaign state" with no permanent per-tag personality, the participant decision factors, and the Africa AI list), acceptance rows AI-01 to AI-04, AI-09, AI-10, PAY-06 and PAY-07, the named scenarios in `012_gods_of_africa_ai_probability_scenarios.md`, and the round 2 remaining-work list (priority 2).
Before this, Fulfil scored a flat 100 whenever payable, Africa's targeted actions all scored a flat 1 and substitute acceptance ignored Africa's needs, which failed AI-02, AI-03, AI-04, AI-09, AI-10 and PAY-06/07.

Decisions:

- Posture is computed from the current state by scripted triggers (`gods_of_africa_ai_*` in `012_africa_gods_triggers.txt`): Africa's Strength band, the participant's Wrath band, its opinion of Africa (file-scoped macros 25 and -25, because `has_opinion` takes only a literal), held or owned host cores, faction membership with Africa, protection, a common enemy, leadership of a faction hostile to Africa, surrender progress, factories compared with Africa's, and the Chaos tier.
  The four spec archetypes map to `gods_of_africa_ai_is_loyal_ally`, `_is_defiant_rival`, `_is_selective_gambler`, and the default (cooperative pragmatist).
- The demand burden is frozen at contract creation from the frozen capacity requirement (`gods_of_africa_freeze_demand_burden`, flags `gods_of_africa_demand_heavy_burden` and `_light_burden`, thresholds in `gods_of_africa_ai_burden`).
- All bases and factors are constants in `gods_of_africa_ai_response`; every closed gate has an explicit `factor = 0`. Weights stay as direct modifiers on named posture triggers instead of an MTTH entry, so each decision's score remains readable in place.
- Representative source scores (computed by hand from the constants): strong gambler, heavy burden, Regional Africa, low Wrath: refuse 112.5, negotiate 60, defiance 18, comply 7.2 (AI-02). Cheap demand, Continental Africa, pragmatist: comply 150, negotiate 6, refuse 0.75 (AI-01). Occupier with Continental Africa: refuse 15 and defiance 16 against 2.5 and 0 for the same country without African land (AI-03). Loyal ally against a Regional Africa: comply 90, refuse 1.25, defiance 0; voluntary aid 60 in an African emergency against 6 for a pragmatist (AI-04). Protection: proven partner 30 against a neutral reliable one 10 (AI-09). Mark and escalate: 0 while Africa's surrender progress is above `africa_action_threshold.near_capitulation` (AI-10). Substitute acceptance: 10 (20 in an African emergency) for a needed family against rejection 2; 0 for an unneeded family against rejection 10 (PAY-06/07). Leniency for a participant on track for Favored that is fighting another war: 27 against 3.
- The generic "Offer a Substitute" shortcut scores 0 for the AI, which names its offer through the three slot decisions that weigh Africa's needs.

MCP route evidence: none was run this round. The round-2 lead recorded `hoi4_probability_inspect` (adapter `decision_ai_will_do`) returning "Invalid tool arguments"; the `chaosx_ai_probability_auditor` baseline and the `hoi4_probability_compare` pass stay `blocked` on that route and were not retried.

## L25. Diplomatic demand families carry out real diplomacy

Disposition: `implemented` (the native results of `diplomatic_relation`, `give_guarantee`, `give_military_access`, `recall_volunteers_from` and `transfer_state_to` on live countries are `needs_live_game`).

Basis: the full spec's demand-family sections ("Diplomatic recognition" must not be "an empty popup choice"; "Military access and basing"; "Withdrawal from African territory" must "name the exact states"; "End support for an enemy of Africa" may list only support "that can be detected and ended"; "Alliance and faction concessions" need "high Strength, a relevant diplomatic situation, and route support"), scenario DEMAND-TERRITORIAL-OCCUPIER (territory dominates material families) and RESP-OCCUPIER (no trivial material substitute for land), acceptance row DEM-13, and the round 2 remaining-work list (priority 2).
The vanilla diplomacy syntax follows `effects_documentation.md` (`diplomatic_relation`, `give_guarantee`, `give_military_access`, `recall_volunteers_from`), `triggers_documentation.md` (`has_guaranteed`, `gives_military_access_to`, `has_volunteers_amount_from`, `has_non_aggression_pact_with`, `is_in_faction_with`, `is_subject`), and the vanilla precedents in `common/decisions/FIN.txt` (ending access, pact and guarantee) and `common/decisions/BUL.txt` (`has_volunteers_amount_from = { tag = PREV count > 0 }` then `recall_volunteers_from`).

Decisions:

- Family 12 is renamed `end_enemy_support` (the saved id is unchanged) and the text "security access" is gone. Families 15, 16 and 17 are military access, a non-aggression pact and a guarantee of Africa.
- Every diplomatic family is paid in full with a constant-backed amount of political power and carries out its act in the same payment (`gods_of_africa_carry_out_diplomatic_concession`). None takes a partial payment; the partial decision is hidden for them.
- Recognition adds `gods_of_africa_recognition` opinion both ways; each recognising major adds 5 to the Strength continent component, capped at 20; World Is One reads `gods_of_africa_world_history_recognised` in a constituent's acceptance chance and the invitation weight (both 1.5).
- Territory moves ahead of material needs. The contract freezes up to three named African core states (the three name slots are `gods_of_africa_named_slot`), payment returns exactly those through the core-return path, a lost named state blocks payment with a visible reason, and the demand then lapses at its deadline as the report-only kind `territory_lapsed` (20), mirroring L19.
- End support is offered only while the participant demonstrably gives a non-capitulated enemy of Africa a guarantee, military access or volunteers; the contract names the enemy and the support kinds, and compliance ends exactly those. Lend-lease is excluded because no effect can end it. Territory and end-support demands take no material substitute.
- Military access, the pact and the guarantee need Security Oaths, Evolution III and Continental Strength or more, and are offered only to a participant that is not a subject, outside Africa's faction, at peace with Africa, and not already giving the concession; access comes first while Africa is at war.
- The participant AI weighs the family (constants `comply_family_*`).

## L26. Punishments follow the offence, repeat less, bluff when weak, and stage Tier V as a final ultimatum

Disposition: `implemented` (native results of `damage_building`, `add_resistance`, negative `add_equipment_to_stockpile`, `white_peace`, `send_equipment` and the Event 013 gateway on live countries are `needs_live_game`).

Basis: the full spec's "Punishment architecture" (Tier I to Tier V content, "Punishment family selection", "Target condition", "Bluff outcomes", "Natural Disasters integration", "Deaths and population accounting"), acceptance rows PUN-08, PUN-12, PUN-13 and DOC-05, and the round 2 remaining-work list (priority 2). The Last Sentence tooltip promised a final ultimatum that did not exist; the lead decided the mechanic is built rather than the text cut.

Decisions:

- The tier is unchanged: intent, the first-failure cap and the Strength ceiling still decide it in `gods_of_africa_evaluate_punishment`. A new family layer (`012_africa_gods_punishment_effects.txt`) decides what the tier does: pressure, unrest, infrastructure, stockpile, diplomatic isolation, covert sabotage, logistical sabotage, military losses or disaster (`gods_of_africa_punishment_family`). The offence picks the order of preference; validity per tier and focus, the 180-day repeat window, and a near-capitulation target (diplomatic or pressure, one state) are checked before a family is used.
- State-targeting families strike 1, 1, 3 and 5 states at the four ordinary tiers, never Africa's own cores (unrest only in occupied territory); material losses are tier times a unit and never more than the target holds; a rejected disaster falls back to infrastructure damage. The previous single random state per tier is replaced.
- Bluffs: at Limited Strength every second punishment costs 2 political power and nothing else, with its own report text.
- Tier V is staged: the first time the full gate opens, a final ultimatum (`.618`, mission and three answers: return land and make peace, pay 150 political power and 3000 infantry equipment, or refuse) runs for 60 days. Only refusal or the deadline brings the disaster and population waves, now in up to three states with one Deaths entry each. Meeting it lowers Wrath by 25 and records the new history kind `ultimatum_met` (21), which the grading does not read. No other punishment or ordinary demand falls on the participant while the ultimatum is open.
- Event log: `gods_first_heavy_punishment` (12210), `gods_final_ultimatum` (12211) and `gods_catastrophe` (12212), each with Africa as actor and the participant as secondary actor. The shared events-log scripted localisation received only the six matching entries.
- Judgment focuses: Reach Beyond the Coast opens covert and logistical families, Let the World Answer adds the coalition decision `gods_of_africa_arm_offender_enemies` (1000 infantry equipment from Africa's stocks and 25 political power to a country fighting a defiant government, occupier or marked offender; `.619` report), and the Hand of Judgment opens military losses and, from Crisis, disaster. Each focus tooltip states its own result; the Strength ceiling is unchanged.
- The Tier IV report line reads "Africa has struck us across the nation." so it is not confused with the real final ultimatum.
- The ultimatum notice reuses the punishment report image and the coalition report reuses the protection report image, as the user accepted for `.611` to `.614`.

## L27. Gods focus payoffs deliver real play, and occupier coercion gets its own node

Disposition: `implemented` (native results of `send_equipment`, `add_building_construction`, `add_claim_by` and `create_wargoal` on live countries are `needs_live_game`). Promoted into the accepted focus spec: `docs/specs/012_africa_specs/specs/012_africa_spec_part_3_focus_tree_architecture.md`, section "2026-10-05 accepted design".

Basis: the Gods focus integration spec (`012_gods_of_africa_focus_integration.md`), the 2026-09-25 focus audit's "Missing or simplified content" (Expedition only adds war support, Final Council only records standings, Measure Needs only lowers the emergency threshold, Continental Arsenals has no build-out, "No Sanctuary for Occupiers" replaced by the Sanctuary node), the user's 2026-09-25 acceptance of the Sanctuary node's protection role, and the round 2 remaining-work list (priority 3).

Decisions:

- Expedition: a host target decision with constant-backed rifles, support equipment and manpower from Africa's own forces, a political-power cost, Africa's reserves and a 180-day cooldown; the target must be on track for Favored, at peace with Africa, and at war with a country whose capital is outside Africa. The `.620` report goes to the partner.
- Final Council: the Favored and Respected entitlement coefficient and ceilings rise by 1.25; each participant may pledge a final shipment (counted as aid) or speak for Africa before the settlement, and World Is One weighs that voice (1.5) in invitations and acceptances.
- Measure Needs: surplus suppression and the largest measured shortfall among rifles, fuel, manpower and industry; transport, aircraft and support needs keep their fixed order because the game exposes no matching stock measure for them.
- Continental Arsenals: a one-off arms factory and infrastructure level (air base level at full infrastructure) in the capital state, or the first owned and controlled African state with room.
- No Sanctuary for Occupiers: a new Evolution III judgment node at (90, 27) after the Hand of Judgment; its host decision claims the African core states a participant owns, creates a vanilla `take_claimed_state` war goal (the `afghanistan.txt` pattern), and arms the first African government Africa deals with that holds a core on that land. Event 012 has no existing war-goal helper (the old `africa_targeted_colonial_war_plan_ready` flag has no consumer), so the vanilla claimed-state route is used.
- Focus cost: the new node uses the 10-week standard cost of judgment steps.
- Every new decision has constant-backed AI weights and an explicit `factor = 0` on each closed gate.

MCP route evidence (2026-10-05): one narrow `hoi4_focus_inspect` (`mode = national`, `treeId = africa_continental_focus_tree`), revision `de29fe65`, reports 301 focuses, 297 diagnostics, 62 connector crossings and 53 node intersections, the same crossings and intersections as the L22 state, so the new node adds no overlap or crossing. Its single blocking diagnostic is the vanilla `TSR_lingguang_incident_joint_branch.txt` brace, outside this mod.
