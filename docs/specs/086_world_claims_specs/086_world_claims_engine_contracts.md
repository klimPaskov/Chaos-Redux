# World Claims: engine contracts and implementation gates

This file describes required behavior and proposed architecture. Identifiers below are planned except where marked “verified existing.” It is not a runnable HOI4 script, and it does not establish support for dynamic containers, scope pointers, string composition, or control-change hooks. Resolve the gates against the installed game before claiming implementation.

## Existing implementation to replace

At repository commit `33b6946dd923b9fc90fbf29bc5798dce3c76a76f`, the fully read `events/086_world_claims.txt` uses verified namespace `chaosx.nr86`. Its hidden `chaosx.nr86.1` selects Germany, then `chaosx.nr86.2` offers every-state claims or a refusal penalty. Its report sprite is `GFX_report_event_world_claims` and its news call is `chaosx.news.72`.

Keep the established namespace where compatible, but replace the Germany-only and all-state behavior. Do not create a parallel `nr086` route while leaving the old one reachable. Audit every main-event, news, localisation, scheduler, and test call site before migration. Existing distant claims created by the legacy version are not retrospectively labeled World Claims integration targets.

## Country and state validity

The proposed participant predicate is: a living country entity with at least one owned valid terrestrial state and an active territorial government. It includes human and AI countries, minors, majors, subjects, civil-war countries, and released countries. Disabled-event settings must follow the shared global-effect contract rather than turning the receiving set into a Germany-only list.

Exclude dormant tags, bookkeeping-only entities with no territorial government, invalid engine scopes, and unowned state slots. A special playable actor is not excluded merely for being nonstandard. Inspect its project classifier. Native claim support can remain valid while its nonstandard integration system requires a provider adapter. Such an adapter must be explicit and tested; a blanket “special country” filter is not an acceptable shortcut around the user's universal rule. Ship ordinary-civilian integration first only as a disclosed staged implementation, not as full universal completion.

A valid foreign state has a real current owner different from the claimant. Native cores and existing claims do not exempt a state from frontier discovery. A core target records provenance but does not receive an occupation grant or a duplicate core award. Owner, controller, claim holder, and core holder are distinct concepts.

## Sparse claimant-state ledger

Key each relationship by campaign identity, claimant epoch, and installed state identity. Required fields are: first wave, provenance source, highest consumed starting ceiling, last verified controller, physical-control start, continuous threshold starts for 80/90/95, project receipts, preparation credit, core-award receipt, and active-job generation. Store only fields needed for an existing relationship.

Keep country-level selected ambition, frozen envelope, anchor set, scale and thresholds, original-major classification, completed territorial signatures, current cosmetic ownership, active projects, assurance references, and confidence state. Keep a separate bounded holding-observation record for adopted ambition states, including original cores and ordinary noncore possessions that have no WC target provenance. That record proves Q/I holding time without turning the state into a WC reward target. Start at the first verified observation unless a native or shared history source proves an earlier uninterrupted run. Do not invent prior time for starting possessions. A wave has one global receipt and one recipient receipt per country. Chaos contributions have separate immutable issuance and bounded reversal records.

These are logical data fields. HOI4 may require arrays, generated dispatch, country-owned variables, or another verified representation rather than associative maps. The implementation must prove that two claimants, a reused tag, and a save/reload remain distinct. Do not present pseudocode maps as native supported syntax.

If the chosen engine representation uses generated state dispatch, bound it to the installed registry, avoid whole-world daily iteration, and test its scaling. Do not invent runtime variable names by concatenating tags or state IDs unless the installed engine explicitly supports that expression.

## Starting-Compliance transaction

Contract inputs: verified current claimant, target state, current active entitlement ceiling, provenance record, current native occupation context. Preconditions: target relationship belongs to that claimant, state is currently controlled by that claimant, state is not already its core, higher numerical ceiling is available, and the native occupation context is ready.

Commit `new_value = max(current_value, ceiling)` and record the ceiling as consumed in the same logical transaction. Rechecking a consumed ceiling does nothing. A higher existing value is preserved while the entitlement still becomes consumed. A higher pending profile is not consumed while the target is uncontrolled or its occupation context is unavailable.

On another country taking control, the World Claims benefit must not be inherited as its integration grant. A state-level `set_compliance` example is insufficient proof that the native engine isolates occupying countries. Probe actual transfer behavior. If a preservation adapter is required, it must save and restore each native occupier's own legitimate baseline without erasing unrelated integration changes. Attribution after normal growth cannot be guessed by subtracting the original grant.

**G1 blocks universal integration release until claimant isolation is proven.** Neither a generic compliance-growth modifier nor an undisclosed global setter is an equivalent implementation. If the engine cannot support the exact requested semantics with a safe adapter, report the limitation and obtain a scoped design revision rather than advertising the behavior as complete.

## Continuous control and core award

Use verified control-change and Compliance-change ownership hooks, or a bounded active-relationship deadline mechanism where native hooks cannot provide threshold transitions. The latter may inspect only scheduled active records and must prove that interruptions between observations cannot be falsely counted as continuous. A coarse sample is not evidence that control or Compliance never dipped.

Keep threshold clocks independently. Native Compliance can change outside World Claims. Probe whether exact transition tracking is available; otherwise use a conservative continuous-test mission/engine facility whose semantics are verified. If only sampled evidence exists, show that exact continuity remains unproven. Do not silently reinterpret continuous days as a sum of sampled days.

At the due core attempt, recheck the current claimant epoch, provenance, controller, active profile, physical minimum, current Compliance, high-threshold duration, and existing core. Award a core once without transferring ownership or removing other cores. Stop ordinary occupation jobs for this pair after its own core is established.

**G2 covers clocks, native core effects, occupation-core interaction, and safe save persistence.** An already earned core surviving a political transfer is expected. Native provider cores are recorded as native facts without fabricating a World Claims core receipt.

## Frontier transaction and batching

The main firing creates one logical snapshot of participant ownership, state validity, traversable land adjacency, old connected World Claims networks, and the active profile. Compute all immediate targets and optional layers from that snapshot. Commit country results idempotently.

A verified snapshot container or generated dispatch must prevent mid-wave transfers from changing later countries' starting data. If the engine cannot hold the needed snapshot across frames, use a bounded synchronous transaction with measured performance or an explicitly staged transaction that freezes the required data before mutating claims. A client-local snapshot is invalid for multiplayer.

A world graph pass during a global event is legitimate. An every-state claim effect is not the algorithm. Do not introduce a new perpetual whole-world monitor. Repeated callbacks reuse the wave receipt and cannot issue a second claim wave or Chaos charge.

**G3 covers valid land adjacency, straits and impassables, frozen breadth-first behavior, and multiplayer order independence.** Existing claim networks must be connected to actual owned seeds before V expansion.

## Ambition and formable providers

A geographic resolver computes candidates from the active map registry and live holdings. A native-provider registry owns each provider's actual triggers, completion effect, cost, identity, territory semantics, and asset references. A World Claims bridge invokes the real route once or reports the missing conditions.

The selected dynamic ambition stores an immutable envelope, anchors, scale, thresholds, and territorial signature. Live qualification is shared by the state piece, count, tooltip, decision, and AI. World/global dormant-state handling is the explicit rule in tuning, not arbitrary denominator pruning.

**G4 covers provider integration and dynamic identity dispatch.** Prove actual map labels, diplomacy labels, war screens, tooltips, ideology changes, and load behavior. A cosmetic tag is a prepared runtime resource, not a command to synthesize a flag or create a new country.

## Puzzle architecture

The canonical geometry input is `docs/formables/state_registry/generated/state_geometry_registry.json`. Consumers declare finite state candidate sets, exact projection and wrap handling, live visibility, shared qualification, and outputs. Prepared regional pages cover the active installed state universe needed for arbitrary World Claims envelopes.

The repository guidance says the former registry builder and consumer compiler are archived. Restore and review that chain deliberately, or approve a replacement. Do not invoke archived producers as normal maintenance. The current reviewed runtime generator is `.tools/generate_formable_state_puzzle_runtime.mjs` and discovers complete manifests. A draft or `assets_pending` manifest is not runtime-ready.

Each category in this family needs its own proven attachment. Informational state icons have tight hover regions and no state-changing click action. Page selection does not mutate the ambition. Scripted GUI must not consume event targets. Scope-sensitive dynamic entries require an installed-engine proof or generated explicit-state wrappers.

**G5 covers active-map provenance, generated page coverage, valid scope, exact live counts, category attachment, resolutions, and DDS integrity.** Required evidence: map inspect/render, GUI inspect/render, and PNG-DDS native-size equality. None was performed in this planning task.

## Transfers, releases, and persistence

Instrument event-owned mutation paths and the shared project adapters that already own transfer, annexation, release, and formation. Do not invent a nonexistent universal hook. Inventory each native hook and every relevant scripted route. An uncovered transfer path is a real compatibility gap.

A new claimant epoch starts for new institutions. Same-country cosmetic changes retain the epoch. A route that transfers continuity uses an explicit one-to-one adapter. Retired records remain historical and cannot schedule work. Save/load restores generations and receipts without replaying pending grants.

**G6 covers lifecycle coverage, tag reuse, civil wars, annexation, country recreation, changed owners/controllers, and multiplayer persistence.** Map-revision migrations must validate installed geometry before remapping state identity. A political map change alone does not require geometry regeneration.

## Timers and scope ownership

Use event-owned active jobs, ordinary mission completion, and the shared Evolution timing surface. GUI updates must not schedule daily or weekly scans. Pure live triggers are preferred. Presentation-only dirty values are permitted only where the verified GUI contract requires them and every applicable owner updates them.

**G7 covers timing, active-job scheduling, save size, and large-campaign performance.** The proposed 90/60/30 timing inputs are not proven MTTH medians. The mandatory probability auditor must begin with inspection and classify exact, bounded, sampled, and unresolved results.

## Source and asset promotion

Every final file belongs to its event or shared-system owner. New constants, helpers, variables, sprites, localisation, achievements, and callback IDs need collision checks and ownership documentation. Shared registries and UI frameworks are parent-owned integration points, not an invitation for a bounded UI worker to rewrite them.

**G8 covers source validation, complete English localisation with required BOM, native assets, registry updates, and gameplay validation.** A parser-clean file is necessary but insufficient. Preserve catalog status until its appropriate implementation review. The full planning-procedure claim also remains blocked while mandatory external reads and independent specialist reviews are missing.
