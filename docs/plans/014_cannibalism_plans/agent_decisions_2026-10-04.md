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
