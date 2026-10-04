# Event 014 agent decisions, 2026-10-04

The user granted the implementing agent full design authority for the Event 014 takeover after the Codex owners stopped.
Each entry below is an agent decision taken under that authority, with its basis and the implementation that carries it.
Disposition labels follow `CLAUDE.md` Specs and Plans.

## D1. Adopt the stopped thread's Larder logistics patch

Disposition: `implemented`.

Basis: the uncommitted patch matches the parent-accepted tuning recorded in `subagent_handoffs/2026-10-04_larder_logistics_implementation.md` (base 1200, 100 per controlled state, 50 per administrative contract point, ceiling 5000, ordinary cap 2000) and its same-scenario probability comparison in `subagent_handoffs/2026-10-04_larder_probability_comparison.md` shows no direct weight change.
It closes audit finding E014-FINAL-04 and spec part 7 "Larder integration" except the hidden-hoard line, which stays a separate accepted requirement.

Decision: adopt the patch after settling the three review points below, and commit it with its owner plan, audit and evidence folders.
The archived before/after source snapshots under the two evidence folders keep their exact bytes through a `-text` attribute, following the Event 021 and 035 precedent.

## D2. A donor with no capturable capital ships at the maximum route loss

Disposition: `implemented`.

Basis: the patch made `cannibalism_prepare_larder_transfer_quote` fail when either capital could not be captured or the distance read stayed unwritten.
Absorption and autonomy then refused the whole transaction, which could leave a warlord in pending absorption forever, and the Wendigo constructor could refuse its reveal when the transformed ZZZ host holds no state.
A free full transfer would reward the missing capital, while a refusal strands the actor.

Decision: an invalid country or generation context still fails the quote.
A missing capital capture or an unwritten or negative distance now quotes at `cannibalism_larder_logistics.distance_loss_maximum` (0.60), so the shipment loses the most it can lose on any route and the transaction proceeds.

## D3. Constructors always finish once the public reveal flag is set

Disposition: `implemented`.

Basis: the patch gated the CBL constructor's integration, annex, host pointer, roster rebuild and result on the runtime migration result, after the reveal flags, the CBL capital and the Hannibal leader had already been installed.
The Wendigo constructor likewise gated its whole reveal tail on the primary donor's absorption, and gated entry to its reveal block on the quote.
Either failure would have left a revealed but unfinished unification, and in the Wendigo case the dispatcher would then also try to build CBL.

Decision:

- CBL: runtime migration still runs, but the opening Larder assignment, commander, war joining, annex, host pointer, generation, finalization, reveal events and roster rebuild no longer depend on its result.
  An unmigrated spread row has a dead source country after the annex and is invalidated by the normal spread resolution when due.
- Wendigo: the reveal block is entered whenever the constructor's existing host checks pass.
  A donor that is not absorbed (both players human, a failed quote or a failed migration) keeps its own stores, is not annexed, and answers the normal response event through the rebuilt roster, while the transformed country receives the zero-snapshot opening assignment.
  The evolution record, super-event, anchors, focus overlay, roster, report, news, pending-flag clear and result always run after the public flag.

## D4. Keep the spread-queue preflight in both constructors

Disposition: `implemented`.

Basis: review point (a) asked whether the constructor-level `cannibalism_validate_spread_queue` gate could block the reveal for good.
The reveal dispatcher `cannibalism_execute_evolution_iii_reveal` in HEAD already runs the same validation before either constructor and refuses the reveal on failure ("A malformed queue remains flagged for diagnosis and cannot be carried into either irreversible unification branch").
Validation does not fail on stale rows: a row whose source or target country has died still loads its scopes and is invalidated when due through `cannibalism_resolve_loaded_spread_entry`.
Only genuine corruption (misaligned arrays, duplicate IDs, illegal status or mismatched state metadata) sets the durable `cannibalism_spread_queue_invariant_failure` flag.

Decision: keep the constructor preflight, which adds no blocking condition beyond the dispatcher's existing one and protects the irreversible reveal from starting on a queue that changed in between.

## D5. Network dossier records are shared subject records, not per-viewer intelligence

Disposition: `implemented`.

Basis: audit finding E014-FINAL-02 and spec part 6 require seven fields per Network node card.
The data API proposal (`2026-10-04_gui_data_implementation/evidence/owner_api_proposal.md`) stored every record per observer with `_@ROOT` keys, viewer epochs, reciprocal cleanup indexes and human tag-transfer rules, and left its two-human transfer case unresolved.
The Network lists, however, are the shared global actor and node registries, visible to every viewer with the same rows; per-viewer records would leave most fields unknown for everyone except the report recipient and cannot be read by plain localisation.
The lead allowed consolidating helpers where the required semantics hold: real writers only, unknown distinct from zero, reveal secrecy, and no whole-world iteration.

Decision:

- Records live on the subject STATE or COUNTRY and are read by every viewer; the viewer owns only its tab, sort, page and selection.
- Writers are the delivered reports `.2`, `.20`, `.21`, `.30`, `.60`, `.61`, `.62`, the two route screening payments, spread containment and warning closure, and the start, result and clear effects of the six counteraction missions.
- Certainty is derived from the stored dates: observed, stale (an incident later than the last strength measurement), partial (records but no measurement), or no reports.
- Inbound route warnings appear as state rows while their warning is live, so a defender can see the route and its screening before arrival; the bounded spread queue is read only when the player refreshes the window.
- Rows keep the 374x64 card art and show all seven fields on three lines; the selected dossier is a one-row native list on a dark vanilla `GFX_mini_bg` panel that adds dates and the ordering country.
- The window keeps its centred placement through an explicit negative position instead of `origo = center`, which the production render showed clipping three quarters of the window.

Implementation evidence: `docs/events/014_cannibalism/gui_data_contract.md`, the matching Event014 commit, and the MCP evidence in `subagent_handoffs/2026-10-04_network_dossier_mcp_evidence.md`.

## D6. The targeted March raid keeps a Host-wide cooldown

Disposition: `implemented`.

Basis: the parent-accepted raid proposal keeps the existing 30-day `days_re_enable`, but a `state_target` decision re-enables per target state, which would let the March Host strike a different hub every day.
That would change the action's cadence, its AI frequency and its Larder drain without an accepted balance change.

Decision: a successful strike sets the timed country flag `cannibalism_march_raid_cooldown` for `cannibalism_warlord_decision.long_reenable_days`, and the decision's `target_root_trigger` hides the action while it runs.
The per-state `days_re_enable` stays as the native re-enable value.
Every target and cost check runs before the single debit, so no refund branch exists; a target that stopped qualifying since selection charges nothing and keeps the earlier receipt.
The receipt result distinguishes a hub that kept an undamaged level from one put out of action, and its controller generation is stored only when the controller is an Event 014 actor.

Addendum (round 2, R2-1): the receipt no longer reads provincial damage; see R2-1 below.

## D7. Host command window pages

Disposition: `implemented`.

Basis: audit finding E014-FINAL-03 (warlord part) and the parent-approved 2026-10-04 Overview/States composition.

Decision:

- The States page list is rebuilt when the player opens the page; each card rechecks control when drawn and labels a lost state instead of hiding it, so the list never shows a gap or a stale owner.
- The command windows keep refreshing every frame, without a `dirty` variable, so the live Larder, Frenzy and Alignment values never freeze.
- The raid card uses the existing continental target card art instead of a second controlled-state card, so the strike record reads as a different kind of card from the state list.
- The page flag is view state only and clears with the other view state on an incarnation reset.

## D8. Revealed command window pages

Disposition: `implemented`.

Basis: audit finding E014-FINAL-03 (revealed part), the spec's plural "continental target cards", and the parent-approved 2026-10-04 Overview/Loyalty composition, whose layout handoff left open whether one last committed target satisfies the plural cards.
Two loyalty lists and a target card do not fit the 282x222 panel beside the portrait without shrinking every row below readable size.

Decision:

- The window has three pages: Overview (the approved value area), Loyalty (the approved integrated and surviving lists) and Targets.
- The Targets page keeps the three newest committed continental targets, newest first, through the `cannibalism_continental_target_record.rolling_count` constant; three cards fill the panel exactly, so the page needs no scrollbar.
- Every committed executor records its target, not only the global campaign, because each of the six orders picks a country and pays for it.
- The integrated history is written when a warlord is integrated, on the revealed host, keyed by actor generation so a repeated record cannot double a row; it clears on an incarnation reset with the targets.
- Surviving warlord rows are stamped with the actor generation seen when the page opened, so a recycled tag reads as no longer a warlord instead of borrowing an older warlord's row.
- The unification seal and terminal line are shown on Overview only, so the list pages never sit under them.
- The page flags are view state only and clear with the other view state on an incarnation reset.

Implementation evidence: `docs/events/014_cannibalism/gui_data_contract.md` and the MCP evidence in `subagent_handoffs/2026-10-04_command_windows_mcp_evidence.md`.

## D9. Wendigo transformation window pages

Disposition: `implemented`.

Basis: spec part 6 lists anchor-state cards for the Wendigo transformation window, the lead treated them like the aggregate-display findings E014-FINAL-02/03, and `global.cannibalism_transformation_anchor_states` already holds the anchors.

Decision:

- The window has two pages: Overview (the existing totals, countdown and pack capacity) and Anchors.
- The Anchors list binds the global anchor array directly, so the cards always match the anchors the transformation counts and no rebuild effect or new record is needed.
- Each card shows the state name, its standing with its strength (unidentified, identified, locked, broken or lost) and who holds it; the holder line names an enemy by adjective so a long country name cannot push the status out of the card, and the tooltip gives the full name.
- The window is shown only to the transformed host, so showing identification there tells the host what the enemy knows without leaking anything to other viewers.
- The title drops "Winter", because the full title did not fit the 410-pixel header box.
- The page flag is view state only and clears with the other view state on an incarnation reset.

## D10. Hidden hoards

Disposition: `implemented`.

Basis: spec part 7 says hidden hoards can create warlord loyalty events, the lead treated that line as an accepted requirement, and the shipped `CBL_audit_the_submitted_hosts` and `CBL_seize_the_hidden_hoards` tooltips promised investigations and seizure missions that did not exist.

Decision:

- Only a hoarder or an autonomy bargain conceals: 0.30 and 0.20 of the dispatch, capped at 0.45 together. The cache comes out of the dispatch before route loss, so the donor's single debit, the host's single receipt and the cache add up; the CBL and Wendigo constructors conceal nothing.
- The cache record lives on the donor's capital state, keyed to the host and its actor generation, and the host keeps only a list of cache states. This survives the donor's annexation and needs no aligned arrays.
- The loyalty event fires when the shortfall is noticed, one review at a time: confront (immediate partial recovery and resistance), tolerate (the cache stays; a governor grows more loyal; authority falls) or bargain (Command Power scaled by the cache for most of it).
- "Loyalty" and "resistance" use real engine levers: a live governor's HOI4 autonomy, and a timed state modifier with resistance target and local supply penalties on host-owned cache states. Dispositions are not changed by a hoard, so a puppet never turns into an enemy through this system.
- The investigation locates every unlocated cache and reopens its review with a better confront share, which gives the audit focus a use on every warlord-settlement route; the seizure mission is Break-the-Warlords only, as the focus tree already gates it.
- The seizure mission requires the host's own divisions in the cache state: two for the whole cache, one for half at the deadline, none loses it. The AI opens a seizure only where two of its divisions already stand, so it never starts a mission it cannot complete; the same target trigger gates player and AI.
- The three new decision and mission icons were generated in the unified decision icon style instead of reusing existing textures, keeping the spec's one-to-one unified decision asset contract.
- The transformed Wendigo host records caches and answers reviews, but has no unified authority and no investigation or seizure.

## R2-1. The March raid hub check reads hub count and a recent-strike flag, not damage

Disposition: `implemented`.

Basis: lead round 2 decision R2-1 and the QA live load, which reported "Not a valid state building" at the raid target trigger and the raid receipt.
`non_damaged_building_level` accepts state buildings only (`documentation/triggers_documentation.md` 6554-6567; vanilla uses it for factories and dockyards), while `supply_node` is a province building (vanilla `common/buildings/00_buildings.txt`, `level_cap province_max = 1`).
No documented trigger reads damage on a province building from a state.

Decision:

- The target trigger follows vanilla `common/decisions/SWE.txt` 2232-2256: a passable enemy-held state beside the Host with `supply_node > 0` and `supply_node < 2`, so exactly one single-level hub, and without the timed state flag `cannibalism_march_raid_recent_strike`.
- A strike sets that flag on the struck state for `cannibalism_warlord_decision.march_raid_hub_repair_days` (30), passed through a temporary variable because timed flags do not accept `constant:` days. The flag keeps a hub under repair off every March Host's list, including other March Hosts that the per-state re-enable does not cover.
- The receipt result is decided from tuning: put out of action when `march_raid_supply_node_damage` (0.50) is not below `march_raid_hub_level` (1), otherwise damaged. At current tuning every strike records a damaged hub, which is what the strike does.
- The 0.50 damage, the per-state `days_re_enable`, the Host-wide cooldown and `ai_will_do` are unchanged. The target pool only loses states struck in the last 30 days, which the same Host could not strike again within its own 30-day cooldown anyway, so no probability comparison was run; a matching `hoi4.probability_compare` remains advisable if the target pool changes further.
- The tooltip names the repair window instead of an undamaged hub, and the raid card text already reads "damaged" or "put out of action".

## R2-2. Land forts and naval bases are placed through a province filter

Disposition: `implemented`.

Basis: lead round 2 decision R2-2, the wiki `Effects` entry for `add_building_construction` (province buildings are placed through `province`), every vanilla bunker and naval base construction (for example `common/national_focus/afghanistan.txt` 4666-4671 and 2175-2196), and the Event 31 precedent in d334dc062.
Six Event 014 rewards called `add_building_construction` for a bunker or naval base with no `province` block and probably built nothing.

Decision:

- `cannibalism_add_state_fort_levels` (STATE scope, caller input `cannibalism_fort_levels`) fortifies every victory-point province with `province = { all_provinces = yes limit_to_victory_point = yes }`. A state without a victory point (a warlord capital or a Wendigo anchor can be one) fortifies its border provinces, and a state with neither fortifies every province, so the reward is never empty.
- `cannibalism_add_state_port_levels` (STATE scope, caller input `cannibalism_port_levels`) builds at coastal victory points, else at the existing naval bases, else at every coastal province, and builds nothing in a landlocked state.
- The Island Host port focus moves its whole port package (naval base, shared slot and dockyard, which vanilla also limits to coastal states) to a held coastal state when the capital is landlocked or lost, preferring a state that already has a naval base.
- The resistance contract capital forts, the unified and warlord capital defenses and the Wendigo anchor defenses all call the fort helper; the levels and the callers are unchanged.
- The province checks read `any_province_building_level` with the same meta-trigger pattern as the siege victory-point check, because a province filter has no state variable.
- Tooltips say the forts go to the capital's or anchor's victory points and that the port work moves to a held coastal state when the capital has no coast.
- Placement on the map is `needs_live_game`; the source now matches every vanilla provincial construction.
