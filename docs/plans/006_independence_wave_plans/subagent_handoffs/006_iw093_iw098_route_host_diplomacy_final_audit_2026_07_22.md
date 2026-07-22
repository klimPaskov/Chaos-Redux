# IW-093 / IW-098 route-politics and former-host diplomacy final audit

**Date:** 2026-07-22  
**Scope:** Uncommitted IW-093 Asante (`DOX`) and IW-098 Sokoto (`SOK`) route-politics, paid former-host diplomacy, post-crisis recovery, FORM-24/25 preparation gates, supporting localisation and documentation.  
**Result:** **PASS — no gameplay-blocking finding in the audited surface.**

## Severity-ranked findings

### Low — FORM-24 documentation calls the required Asante route “federal”

`can_prepare_independence_wave_form24_from_iw093` correctly requires
`independence_wave_iw093_route_constitutional_cabinet`; there is no IW-093
`federal` route flag. The player-facing/formable behaviour is correct, but the
implementation references call it federal in two places:

- `docs/systems/006_independence_wave_iw093_iw098_signature_packages.md:187`
- `docs/plans/006_independence_wave_plans/006_iw093_iw098_signature_packages_improvement_addendum_2026_07_18.md:86`

**Recommended fix:** replace “federal route” with “constitutional-cabinet
route” in both passages. Do not alter the working trigger at
`common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:370`.

### Low — Sokoto constitutional-route AI description names the wrong value

The addendum says northern constitutional AI prefers high “host settlement,”
but Sokoto has no matching package value. The implemented decision correctly
uses `iw098_court_civic_balance` and `iw098_frontier_security`:

- documentation: `docs/plans/006_independence_wave_plans/006_iw093_iw098_signature_packages_improvement_addendum_2026_07_18.md:146`
- implementation: `common/decisions/006_independence_wave_iw093_iw098_decisions.txt:767`

**Recommended fix:** describe the actual `frontier security` threshold in the
addendum. This is documentation drift only; it does not invalidate AI targets
or route locking.

## Lifecycle and decision-quality notes

- Each package category exposes a bounded progression: route conference/compact,
  state project work, former-host negotiation, conditional post-crisis recovery,
  and a one-time FORM preparation decision. Receipts, cancelled/failed flags,
  package-local active flags, and the shared diplomacy-active predicate prevent
  duplicate transactions and simultaneous negotiations.
- Route locks are mutually exclusive locally and are checked against the shared
  government route before the writer runs. The six route writers install the
  intended political distributions; all eight distributions total exactly 100:
  IW-093 `20/5/70/5`, `12/3/82/3`, `55/3/40/2`, `8/2/65/25`; IW-098
  `10/5/80/5`, `10/2/85/3`, `45/3/50/2`, `8/2/65/25`.
- FORM-24 is reachable from the specified path: initial host settlement 15,
  `independence_wave_iw093_screen_colonial_veterans` contributes 5, and either
  accepted host outcome contributes 30, reaching the trigger threshold 50.
  The constitutional-cabinet route, authority 70, and cocoa/rail 65 remain
  deliberate independent requirements. FORM-25 retains its own eligible-route,
  emirate-compact, caravan-network, and frontier-security gates.
- The 90-day host dispatches are paid when started, retain an active transaction
  lock, and have explicit completion failure, cancellation, and cleanup paths.
  The 75-day post-crisis decisions are visible only for an unresolved crisis and
  write the same receipt only after a recoverable shared host outcome.
- There is no separate timed mission in this tranche. The timed surfaces are
  decisions (`days_remove`), so mission owner/category/region/duration/duplicate
  risk is not applicable. Their decision equivalents are package-owned,
  country-scoped, and receipt-protected.

## Former-host diplomacy, AI, and scope notes

- Both negotiation-host triggers require the exact frozen former host, a living,
  independent, non-capitulated counterparty with a capital and no current war
  against the negotiating country. They reject stale targets, subjects, dead
  hosts, and self-targeting.
- The host event is sent only after the initiating country saves the regular
  `independence_wave_iw093_negotiating_country` or
  `independence_wave_iw098_negotiating_country` event target. The responding
  host is saved in event immediate scope. This is a valid regular-event-target
  chain under the offline Event Modding reference; no global target is created
  or left to clean up.
- Recognition applies a non-aggression pact; association adds guarantee and
  military access; rejection applies embargo and at most one annexation wargoal.
  Decision cleanup clears package state only, deliberately preserving those
  bilateral diplomatic outcomes. Rejection cannot write the settlement receipt.
- Post-crisis recovery is reachable: the shared former-host lifecycle converts a
  missing former host to `host_collapse`, while existing shared settlement
  decisions can replace reclamation conflict with recognised separation or
  guarded coexistence. The package ratification gates accept only those
  recoverable outcomes and a non-warring/dead host condition.
- AI weights are bounded by the same route, resource, threat, and target gates
  as the player surface. No dead-country, closed-route, impossible-border, or
  unsafe-formable target path was found in the audited decision/event chain.

## Cost, tooltip, localisation, cleanup, and exploit notes

- Costs use varied political power, command power, infantry/support equipment,
  trains, convoys, civilian-factory use, and host/territory requirements rather
  than a passive political-power store. Displayed custom-cost text and the
  deducting helpers use the same constants.
- The standard project/dispatch resource predicates use strict `>` comparisons,
  consistent with the shared Independence Wave decision-cost convention. Thus a
  player must retain one whole unit above a displayed integer resource cost. This
  is an established package-wide reserve convention, not a route-specific
  mismatch; if the project later wants exact-at-zero affordability, change the
  shared convention and the cost wording together rather than patching this
  tranche alone.
- All eight event IDs are unique (`chaosx.nr006.9301`–`.9304`,
  `.9801`–`.9804`) and each has localisation. The decision localisation is UTF-8
  with BOM. Outcome text states the bilateral result and the receipt timing.
- Transaction close helpers clear temporary cost/active state. Decision/package
  cleanup clears stale flags and targets without erasing deliberate NAP,
  guarantee, access, embargo, or wargoal effects. No free-unit, equipment-farm,
  core-spam, war-goal-spam, or cooldown-bypass loop was found.
- The audited decision/event/doc surfaces contain no advisor asset registration
  or female-portrait reference. No changed BAY or RHI portrait path was found.
  No decision-owned scripted GUI is present, so GUI inspection/rendering was not
  applicable.

## Validation evidence

- Manual cross-file trace of constants, route triggers/writers, paid decision
  helpers, categories, shared diplomacy locks, events `9301`–`9304`/`9801`–
  `9804`, localisation, effect documentation, package system documentation,
  improvement addendum, resume packet, source-of-truth map, and simplifications
  ledger.
- Event-ID uniqueness check returned one definition for each of the eight IDs;
  localisation presence check found all eight event keys; the package decision
  file contains 18 decision blocks; BOM check returned true.
- Read-only `hoi4.event_inspect` lint and `hoi4.event_render` targets evidence:
  `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e34b059c8b9212ff258b9b23a89f1df6bb936907ffdb567cb502461c84cdb288/5b13459df4a931bc517d97c09dd5f3bb91073e2e0fc2967326e22114c7c14d2f/event-lint-a9eb6bf9cf78.json` and
  `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61cb1088aa7489f06a991fa42da92ab84d5c821c0f2227175dc1d2ce54732fcf/da3177b3162241d22aad38d896508b987f68adfbd8702d9d4af926082efbfa4b/event-targets-a9eb6bf9cf78.json`.
  The MCP report remains partial for this purpose: it inventories the whole
  workspace and carries unrelated global diagnostics, although its bounded
  target render selected the four-event IW-093 branch. It is retained as
  structural evidence, not treated as a clean whole-mod lint.
- Skipped meaningful validation: no live game scenario was run and no GUI
  artifact was rendered; the first is outside this read-only static audit and
  the second has no in-scope scripted-GUI surface.

## Changed files and handoff

- Changed only this audit handoff:
  `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw093_iw098_route_host_diplomacy_final_audit_2026_07_22.md`.
- No decision, mission, scripted GUI, localisation, gameplay, asset, or
  protected-portrait ID was changed.
- Before/after behaviour: unchanged; this was a read-only audit.
- Remaining issues: the two low-severity documentation corrections above. No
  plan addendum was written because no broad mechanic gap was found.

## References consulted

- Repository `AGENTS.md`; `chaos-redux-events`, `hoi4-decisions-missions`, and
  `chaos-redux-subagents` skills.
- Required offline Paradox wiki pages and the relevant vanilla documentation
  (`script_concept_documentation.md`, `triggers_documentation.md`, and
  `effects_documentation.md`), plus vanilla timed-decision/event-target
  precedent.
