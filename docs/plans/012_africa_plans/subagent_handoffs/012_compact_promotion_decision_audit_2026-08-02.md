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

A medium-severity documentation-to-code cleanup discrepancy remains: `africa_promote_compact_host_package` clears `africa_compact_promotion_refused` and `africa_compact_access_failure` only inside a successful promotion branch, while `africa_compact_host_can_be_promoted` rejects either flag before that branch can run.

The refusal gate is therefore correctly hard in gameplay, but the documentation claim that the package clears stale refusal or access-failure state after all conditions pass is not literally achievable by this path.

## Meaningful validation

Verified that both decision call sites resolve to their matching scripted trigger/effect definitions, that every `africa_compact_promotion.*` reference resolves to the Event 012 constants block, and that the four decision name, description, and tooltip localisation keys exist.

Source review of the exact proof and promotion effects confirmed they alter only host depth, package flags, authority, integration burden, and evidence flags, with no tag creation, ownership, controller, core, faction, relationship, or opinion effect.

## Skipped validation

No game launch or live-session validation was run, because live consumer validation belongs to the user and this audit is limited to static source evidence.

## Remaining issue

Parent review should decide whether to remove the unreachable flag-clearing lines or revise `docs/events/012_africa/compact_promotion.md` to describe them as defensive no-ops, without weakening the refusal gate.
