# Event 19 exact recorded-formation transfer handoff

Date: 2026-07-16

## Outcome

Natural multi-state claimant revolts use the approved exact recorded-formation
transaction. HOI4 has no documented division-scoped ownership-transfer effect,
so the implementation recreates only the frozen Event 19 formation set in a
locked dynamic actor, proves the entire destination package, and deletes the
matching source cohorts only after that proof. It uses no fixed tag, ordinary
division, random formation, or takeover fallback. The one-state route remains
the existing takeover or failed-coup path.

The consolidated registry remains
`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`. This
subagent did not edit that file and created no second registry. All ordinary and
family template reconstruction consumes the existing registry/provider
contracts.

No asset file was changed. The male checks in this handoff describe gameplay
leader metadata only; they are not evidence for an individual human focal
portrait. The current fixed-sprite visual contract is army/host scene art and is
owned by the separate asset handoff.

## Files changed by this implementation

- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_effects.txt`
- `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt`
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`
- `common/on_actions/chaosx_on_actions_chaos_meter.txt`
- `common/on_actions/019_infantry_spawn_derivative_on_actions.txt`
- `common/on_actions/019_infantry_spawn_achievement_on_actions.txt`
- `docs/events/019_infantry_spawn/overview.md`
- `docs/specs/019_infantry_spawn_specs/matrices/019_evolution_entry_cleanup_matrix.md`
- `docs/specs/019_infantry_spawn_specs/review/blockers_and_uncertainty.md`
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_6_derivative_countries.md`
- this handoff

## Success proof order

1. Prove the selected claimant, generic provider row, coherent connected
   non-capital region, exact selected states, and every selected source unit,
   lot, generation, template, component, auxiliary membership, and obligation.
2. Freeze the claimant UID and identity, source UIDs and globally unique delete
   cohorts, ledger row identities, live division manifests, optional technology
   gates, recorded starting factors, and all Event 19 global allocators and
   lifetime/progression totals.
3. Stage only the frozen source unit rows. No source division or accounting
   aggregate is removed at this point.
4. Create a fresh dynamic actor, transfer exactly the frozen state set, copy a
   private subset ledger, reconstruct the recorded templates from the sole
   registry, recreate the exact UID/cohort set, copy its obligations, and copy
   the selected claimant.
5. Prove the actor owns, controls, and cores exactly the selected states; has the
   recorded anchor as capital; contains exactly one replacement for every frozen
   UID/cohort and no other division; has aligned private ledgers; preserves unit
   identity, origin, manifest, optional gates, auxiliary membership, obligations,
   and claimant identity; and has exactly one male claimant leader.
6. Re-prove unchanged global Event 19 allocators, generation/evolution state,
   formation and lot totals, claimant totals, management totals, and destruction,
   integration, demobilization, incident, and request totals.
7. Delete each source division only after the stored row, UID, cohort, staged
   status, and exact live scope agree. The only source deletion is
   `delete_unit = { id = <frozen cohort> disband = no }`.
8. Prove zero surviving source UID/cohort matches and the exact source division
   count delta. No source ledger accounting is committed by deletion.
9. Prove every staged historical row and aggregate is still commit-ready, freeze
   the expected accounting result, and commit the source ledger once.
10. Prove every changed historical unit, lot, generation, obligation, claimant,
    and aggregate field. Remaining loyal units and lots are released only from
    the exact frozen claimant subset; unrelated rows are not scanned into a
    mutation set.
11. Install public derivative identity, prove the male claimant and former-parent
    war, restore and re-prove the frozen global accounting, repeat the exact
    source post-commit and territorial proofs, record the history payload, and
    only then unlock both countries.

The post-accounting path is intentionally asymmetric. Once source accounting is
committed, any mismatch calls
`infantry_spawn_lock_failed_natural_derivative_post_commit`; it never calls the
pre-commit rollback over partially committed history.

## Pre-commit rollback and partial-deletion recovery

The recovery order is fixed:

1. Count the exact replacement UID/cohort pairs in the provisional actor.
   Delete a pair only when exactly one matching division exists; zero is allowed
   for a partial actor build, more than one fails recovery. Prove the actor has
   zero divisions, so an ordinary or unmarked unit prevents annex and leaves the
   transaction locked.
2. Remove the actor's provisional cores and prove none remain.
3. Set the narrow global
   `infantry_spawn_natural_derivative_recovery_annex_bypass`, annex the actor
   with `transfer_troops = no`, clear the flag immediately, and prove both that
   the flag cleared and the actor ceased to exist.
4. Prove the parent again owns and controls the complete frozen state set.
5. For each frozen source UID, retain an existing exact source division or
   recreate only that missing UID from the frozen recorded template, starting
   factors, manifest, obligation-linked identity, and origin. Rebind its original
   source row and live scope.
6. Prove the complete restored source UID set, its row/live identities, origins,
   optional gates, auxiliary memberships, and strength ceiling before restoring
   and proving the global accounting snapshot.
7. Clear transaction locks only after every proof passes. Any failure marks the
   ledger invariant and leaves the country locked.

Recovery does not increment Event 19 generation, death/destruction, war,
transfer, claimant-revolt, evolution, request, management, or allocator totals.
If recovery actually recreates a missing source division, the parent receives
`infantry_spawn_natural_derivative_recovery_recreation_consumed`; the natural
transfer availability trigger then fails closed for future recreate/delete
revolts in that country.

## Annex-listener isolation

The narrow rollback bypass guards the listeners that otherwise have broad
side-effects for this unpublished actor:

- `common/on_actions/chaosx_on_actions_chaos_meter.txt`
- `common/on_actions/019_infantry_spawn_derivative_on_actions.txt`
- `common/on_actions/019_infantry_spawn_achievement_on_actions.txt`

The remaining `on_annex` listeners were audited. Genocide cleanup is camp-state
specific; condemnation is participant/target specific; resource discovery is
foreign-actor/participant specific; random-faction, communism, air-cleanliness,
utopia, secret-alliance, cannibalism, and Soviet-collapse handlers all require
their own registered state or flags. The provisional actor has only locked
Event 19 provisional identity and is never registered with those systems, so no
broader bypass was added.

## Anti-repair contract and unsupported live attributes

`unit_strength` is the only documented division-scope live strength signal
available to this transaction. For each frozen source division, preflight takes
the larger recorded `start_equipment_factor` and `start_manpower_factor` as a
conservative threshold. The source must be at or above that threshold, and the
recreated destination must be at or below it. The same upper proof applies only
to a source UID actually recreated during rollback. This prevents the transaction
from turning a damaged source set into a stronger replacement set.

The script path cannot read and reproduce these live-only properties exactly:

- current per-equipment-type inventory and variants
- exact current manpower fill
- organization
- veterancy and experience gained after creation
- medals and decorations
- officer history
- army assignment, battle plans, and orders

No guessed compensation is used inside the owner-approved recreate/prove/delete
substitute. Its authoritative contract is the immutable Event 19 issue manifest,
generation/lot/template/unit and claimant identities, starting
equipment/manpower/experience factors, technology and auxiliary markers, and
outstanding equipment/manpower obligations.

## Validation and audit evidence

- The seven touched gameplay script files have balanced delimiters.
- The natural transaction contains exactly two deletion sites: exact destination
  cleanup and exact source cohort deletion. Both use `delete_unit` with
  `disband = no`; there is no executable `destroy_unit` path.
- The final actor territory proof uses the explicit actor event target for both
  controller and core tests. The recovery territory proof uses the original
  parent root.
- All twenty-four frozen lot identity vectors are cleared, captured, length-
  checked against the frozen lot UID set, and consumed by the destination proof.
  The actor proof therefore remains independent of the source lot status,
  claimant, count, and liability mutations made by the later source commit.
- All three one-person derivative leaders explicitly use `female = no`.
  Collective and council leaders remain genderless. The copied claimant is
  proved `is_female = no` before unlock.
- The annex bypass is present only around the synchronous recovery annex and is
  checked as cleared immediately afterward.
- Scoped diff hygiene found no malformed whitespace or unsupported raw
  comparison operators in the touched gameplay files.
- `hoi4.event_inspect` lint could not allocate a report because the shared MCP
  artifact store returned `ARTIFACT_STORAGE_LIMIT`. No result from that tool is
  claimed.

## Simplifications, omissions, and blockers

The user-approved engine-constrained substitute is the exact
recreate/prove/delete transaction documented above. No additional fallback,
fixed tag, ordinary-unit substitution, random formation, unproved deletion, or
post-commit rollback was implemented. The unsupported live attributes listed
above are explicit engine/API limitations of that approved contract, not
silently approximated features. The MCP lint artifact limit is the only
remaining tooling blocker in this handoff.
