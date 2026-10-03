# Migration custody receipt cleanup

Date: 2026-10-03.
Disposition: implemented source correction pending independent parent audit and mixed-hunk commit.
Acceptance basis: the user's exact cohort ownership, no duplicate population/deaths, valid actor/site proofs, and complete cleanup requirements.

## Proven contract defects

The Camp dispatcher supplies action-local temporary custody inputs.
The strict migration receipt previously used `clear_variable` on those fields, which clears normal variables rather than consuming the temporary envelope used by the caller.
The current-state wrapper also left the previous strict result, duplicate-result marker, and resolved amount untouched when its preflight rejected a later call.
The Camp consumer accepts either a valid wrapper result or `migration_cohort_custody_already_recorded = 1`, so a previous duplicate marker could incorrectly acknowledge a later rejected attempt in the same effect chain.

The wrapper already accepted a positive current-host/route proof, while the strict receipt's final guard required a value greater than one.
The Camp owner supplies the re-resolved whole living amount as that proof, so a valid one-person remainder was inconsistent between the two layers.
The strict receipt also lacked the wrapper's explicit live actor-target check and neither entry point bound the site proof to the current state.

## Correction and public contract

`migration_clear_cohort_custody_request` resets all twelve temporary request/proof fields to their existing zero/none constants.
Both current-state and strict receipt exits call it after accepted or rejected attempts.
The current-state wrapper initializes its own result, strict result, duplicate and achievement markers, and resolved amount before preflight.
Successful public results, duplicate marker, and resolved living amount remain readable after cleanup.
The site proof must equal `THIS.id`; the strict receipt requires the live valid actor target; a positive route/current-host proof is accepted consistently at both layers.

The actor-approval token remains distinct from actor identity.
`camp_repression_action_dispatcher_effects.txt:84-98` sets that token to its approved `camp_rework_action_id`, and the Camp wrapper copies it to the temporary actor proof.
It is not a country database ID.
An initially drafted country-ID equality check was rejected and removed before commit after this caller trace proved the token's actual meaning.
The actual actor country is the explicitly saved and validated `migration_cohort_custody_actor` target.

Aligned arrays, explicit cohort ID, unique row, current host, live status, exact whole-row amount, supported internment/labor action, transaction, generation, revision, and request identity remain mandatory.
No persisted generic dedupe was introduced because dated source action identities remain nonuniform.
Existing achievement receipt idempotence remains the owner of duplicate evidence.
No population, Deaths, route, reception-load, service-capacity, decision cost, or AI weight changes occur here.

## Changed surface and mixed ownership

The owned hunks are the custody helpers in `common/scripted_effects/migration_adapter_effects.txt` and their existing table/contract in `migration_adapter_effects.md`, plus this handoff.
The helper-map row now documents the already-wired Camp callback instead of claiming that no owner supplies the required fields.
The concurrent Event 012 reception helpers and their new documentation are other-owner work and remain outside this commit.
The parent uses isolated index and reviewed owned patches to preserve those unstaged additions.

## Source cases and validation limits

- A valid whole living row with route proof one can pass the same positive-proof requirement in both receipt layers.
- Missing actor target, invalid actor country, mismatched site ID, missing proof, invalid row/status/host, or partial amount remains rejected.
- A duplicate success followed by a rejected wrapper call cannot retain a positive duplicate marker or resolved amount.
- A later call must provide fresh temporary request fields; the cleared envelope cannot validate an omitted field from the prior call.
- Accepted and duplicate results remain available to the Camp consumer, while only request/proof inputs are consumed.

These are source-contract traces, not game or MCP execution results.
Relevant installed references are `effects_documentation.md:2773` (`clear_variable`) and `:7820` (`set_temp_variable`), alongside offline Data structures temporary-variable scope and lifetime sections.
The current Camp dispatcher, staged-row resolver/commit, and migration achievement consumers were read directly.
The already recorded mechanic-test timeouts do not establish execution of this new custody correction.
No game was launched and no logs were read.
No mechanical fallback or simplification was introduced.
