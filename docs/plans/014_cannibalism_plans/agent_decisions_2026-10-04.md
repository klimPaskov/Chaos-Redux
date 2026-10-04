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
