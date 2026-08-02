# Event 012 compact promotion decision audit

## Scope

Audited only `africa_record_compact_promotion_proof` and `africa_promote_compact_host`, their Event 012 scripted triggers, effects, constants, English localisation, and compact-promotion documentation.

## Changed files

- `common/decisions/012_africa_decisions.txt`

## Changed identifiers

- `africa_record_compact_promotion_proof`
- `africa_promote_compact_host`

## Before and after

Both decisions required political power strictly greater than their stated cost, which rejected a host holding exactly 25 political power for evidence or 40 political power for promotion.

Their availability checks now use `greater_than_or_equals`, matching the displayed and engine-applied decision cost.

## Audit findings

No critical or high-severity syntax, scope, tag-creation, relationship-transition, or opinion-only promotion defect was found.

### Medium: refusal and failure gates have no writers

`africa_compact_host_can_be_promoted` rejects `africa_compact_overlap_dispute_active`, `africa_compact_access_failure`, and `africa_compact_promotion_refused`, while the evidence trigger also rejects the refusal flag.

An Event 012-wide static search found no `set_country_flag` writer for any of those three flags, and the only references are their triggers plus the promotion effect's two clears.

The documented refusal, access-failure, and overlap-dispute scenarios therefore cannot occur through current source, so their gates are inert rather than hard lifecycle controls.

### Low: unreachable cleanup and documentation discrepancy

`africa_promote_compact_host_package` clears `africa_compact_promotion_refused` and `africa_compact_access_failure` only inside a successful promotion branch, while `africa_compact_host_can_be_promoted` rejects either flag before that branch can run.

Even after writers exist, this path cannot clear either active flag, so the documentation claim that it cleans stale refusal or access-failure state after all conditions pass is not literally achievable by this path.

### Low: unavailable-state detail is not locally described

The decisions have name, description, and success-effect tooltip keys, but the long availability contracts are invoked directly without `custom_trigger_tooltip` wrappers or dedicated requirement tooltip keys.

The player-facing descriptions describe the general contract, but they do not identify the currently failed item when the decision is disabled.

## Meaningful validation

Verified that both decision call sites resolve to their matching scripted trigger/effect definitions, that every `africa_compact_promotion.*` reference resolves to the Event 012 constants block, and that the four decision name, description, and tooltip localisation keys exist.

Source review of the exact proof and promotion effects confirmed they alter only host depth, package flags, authority, integration burden, and evidence flags, with no tag creation, ownership, controller, core, faction, relationship, or opinion effect.

The reused ledger sprite is registered in `interface/012_africa.gfx`, and its referenced DDS asset exists.

An Event 012-wide static search of `common`, `events`, and `history` confirmed that the refusal, access-failure, and overlap-dispute flags have no writer.

## Skipped validation

No game launch or live-session validation was run, because live consumer validation belongs to the user and this audit is limited to static source evidence.

## Remaining issue

Parent review needs an accepted source for each refusal, access-failure, and overlap-dispute writer, together with an explicit repair or expiry path where those states should be recoverable.

## Source reconciliation follow-up (2026-08-02)

The original static search was performed against an earlier flag contract and is stale for the active runtime gates. The compact promotion triggers now reject `africa_overlap_dispute_active` and `africa_project_access_damaged`; both have writers in the shared action result path, and congress settlement or successful recovery clears the active dispute/access state. `africa_compact_promotion_refused` also has an explicit decision writer and a paid reopen decision.

`africa_compact_access_failure` and `africa_compact_overlap_dispute_active` remain legacy compatibility names without direct writers. They are not substituted for the active gates, and no artificial writer was added merely to satisfy the old audit wording. The successful-promotion clear for `africa_compact_access_failure` is retained for save compatibility only.

The remaining lifecycle gap is therefore limited to the legacy aliases and the absence of a compact-specific unavailable-state tooltip. The active refusal, overlap, and damaged-access gates are source-wired; scenario acceptance and final player-facing failure detail remain open.

After those writers exist, remove the unreachable clear calls or move cleanup to a recovery effect whose gate can actually see the active state, while preserving the refusal gate.

Add compact-proof and compact-promotion custom requirement tooltips when the parent selects the final failure and recovery lifecycle, so the disabled state exposes concise current requirements instead of a long raw scripted-trigger contract.
