# FORM-48 scripted-system architecture audit

Date: 2026-07-18

Status: no P0 correctness defect found. One P1 cross-generation relation-cleanup
gap was demonstrated and fixed. FORM-48 readiness remains deliberately
fail-closed; this audit does not attest IW-173, IW-179, or IW-184 runtime
content and does not promote any shared readiness flag.

## Scope and authority

This was an independent, narrow audit of the FORM-48 transaction and
post-formation scripted-system architecture. It covered the dedicated FORM-48
effects and triggers, their shared registry and FORM-01/02/04 cleanup seams,
decision lifecycle contracts, constants, and system documentation. Pacific
focus, idea, localisation, package, adviser, portrait, and asset content were
read only where needed to understand a call site; none of those surfaces was
edited.

The audit used:

- the Event 006 implementation plan and the prior FORM-48 registry and
  post-formation handoffs;
- the offline wiki pages for data structures, triggers, effects, scopes,
  events, decisions, AI, localisation, interfaces, and scripted GUI;
- official `effects_documentation.md`, `triggers_documentation.md`,
  `script_concept_documentation.md`, and script-constant documentation from
  the installed game;
- vanilla Czechoslovak federation and Greek guarantee teardown precedents;
- installed vanilla state definitions, which resolve state 378 to California,
  state 629 to Hawaii, and state 684 to the Caroline Islands; and
- the existing Chaos Redux dynamic-effect registry and FORM-48 system docs.

Read-only HOI4 MCP inspection was attempted before the patch. Map inspection
of states 378/629/684 returned `MAP_MODEL_BUDGET_BLOCKED`. Event/decision lint,
focus inspection, and GUI inspection returned `ARTIFACT_STORAGE_LIMIT` before
producing reviewable artifacts. No artifact ID was emitted. There is no custom
FORM-48 scripted GUI; its player surface uses standard decision and mission UI.
These tool-side limits are recorded as unsupported analysis and were not used
to justify readiness or completion.

## Finding and correction

### P1: stale member bindings could own unrelated diplomatic teardown

`independence_wave_form48_remove_event6_autonomous_relations` correctly gated
each of the four reciprocal access/guarantee removals behind a directional
ownership flag, but its outer proof required only that the saved carrier still
exist. If a member retained stale FORM-48 markers while its Event 006
generation or the carrier generation changed, those old ownership flags could
remove a relation belonging to another transaction.

The new member-scope trigger
`has_independence_wave_form48_current_autonomous_binding` requires all of the
following before any relation mutation:

- the member is marked as a FORM-48 autonomous member;
- the member has a live Event 006 generation;
- the saved carrier pointer, saved carrier generation, and saved autonomous
  family exist;
- the saved family is FORM-48;
- the member live generation equals the saved carrier generation;
- the carrier exists and has a live Event 006 generation and formable family;
- the carrier family is FORM-48; and
- the carrier live generation equals the member's saved carrier generation.

The relation-cleanup effect now uses this proof as its outer limit. It still
checks the four ownership flags independently. A stale or cross-generation
member therefore loses only its local FORM-48 flags and pointers; it cannot
mutate military access or guarantees on another transaction.

No P0 transaction, eligibility, consent, cleanup-order, value-clamp,
decision-lifecycle, or readiness defect was found.

## Helper map

| Helper | Scope | Inputs and proof | Output and side effects | Principal call sites |
| --- | --- | --- | --- | --- |
| `is_independence_wave_form48_eligible_member` | Candidate country | Live Event 006 origin, sovereign status, exact original tag/package/anchor/ownership/control/capital | Boolean only | FORM-48 discovery and exact ledger construction |
| `has_independence_wave_form48_exact_founding_ledger` | Carrier | Frozen HBX/HAW/FSM rows, exact count, packages, anchors, and acceptance state | Boolean only | Strict mutation and runtime commit proofs |
| `has_independence_wave_form48_strict_mutation_preconditions` | Carrier | Exact carrier identity, ledger, route, and transaction state | Boolean only | FORM-48 identity/integration adapters |
| `has_independence_wave_form48_runtime_commit_proof` / `has_independence_wave_form48_successful_integration_proof` | Carrier | Committed transaction plus live generation-bound member bindings | Boolean only | Registry commit and post-formation initialization |
| `independence_wave_form48_install_autonomous_member` | HAW/FSM member, carrier in `ROOT` | Exact accepted row and current carrier transaction | Saves member carrier/family/generation; creates only missing reciprocal access/guarantees and records each direction it owns | FORM-48 integration adapter |
| `has_independence_wave_form48_current_autonomous_binding` | HAW/FSM member | Member live generation = saved transaction generation = carrier live generation; both families FORM-48 | Boolean only; no state mutation | Relation teardown only |
| `independence_wave_form48_remove_event6_autonomous_relations` | HAW/FSM member | Current-binding proof plus four directional ownership flags | Removes only Event 006-owned access/guarantees; clears local ownership pointers and flags | Member departure, rollback, dissolution, origin cleanup |
| `independence_wave_form48_clamp_public_values` | Carrier | Five carrier public ledgers | Clamps each ledger to its configured 0-100 bounds | Initialization and all cycle outcomes |
| `independence_wave_form48_initialize_postformation` | Committed PFX/HBX carrier | Successful integration proof | Initializes five ledgers, ideas, cycle stage, league/reason-4 seams, and project surface; does not set readiness | Shared registry after atomic commit |
| `independence_wave_form48_begin_*_cycle` / `complete_*_cycle` / `fail_*_cycle` | Carrier | Serialized project state and exact member responses | Starts one mission or resolves its single success/timeout path; updates host, league, patron, and public ledgers | Three carrier projects and missions |
| `independence_wave_form48_dissolve_federation` | Carrier | Strain/member-departure dissolution pressure | Applies configured consequences, then delegates to shared runtime cleanup | Automatic threshold and timed dissolution decision |
| `independence_wave_form48_cleanup_frozen_autonomous_members` / `cleanup_runtime` / `origin_cleanup` | Carrier or Event 006 origin | Frozen founding rows and saved generation-bound member pointers | Removes FORM-48 decisions/missions/ideas/variables/owned relations before shared ledger and identity teardown | Dissolution, rollback, and Event 006 origin cleanup |

This helper remains private to the FORM-48 subsystem. It was not added to
`chaosx_dynamic_effects.txt` because it has one subsystem-specific mutation
call site and no cross-system API use.

## Constants and tuning table

FORM-48 tuning remains centralized in
`common/script_constants/006_independence_wave_form48_constants.txt`:

| Category | Purpose |
| --- | --- |
| `independence_wave_form48_stage` | Stable cycle/stage identities |
| `independence_wave_form48_duration` | Project, mission, response, and dissolution timing |
| `independence_wave_form48_value` | Opening values, ledger bounds, and dissolution thresholds |
| `independence_wave_form48_cost` | Carrier/member command, convoy, fuel, equipment, and factory costs |
| `independence_wave_form48_host_delta` | Former-host consequence table |
| `independence_wave_form48_league_delta` | League cohesion, common-cause, reserve, confidence, and patron-capture changes |
| `independence_wave_form48_patron_delta` | Patron influence changes |
| `independence_wave_form48_country_delta` | Carrier/member public-ledger and consequence changes |
| `independence_wave_form48_modifier` | Timed country-modifier values |

No constant was added or changed by this audit. The three projects remain
serialized, materially funded, and paired with one mission apiece. The six
member fulfillment/withholding choices remain mutually exclusive per response
window. No political-power currency, passive checklist, refund path, free
formation, free unit, or readiness shortcut was introduced.

## Event targets and cleanup lifecycle

FORM-48 uses regular, chain-scoped event targets only:

- `independence_wave_form48_autonomous_member_target` temporarily identifies
  the invited/installing member;
- `independence_wave_form48_cleanup_member` temporarily preserves the member
  while relation directions are removed; and
- `independence_wave_form48_cleanup_carrier` temporarily preserves the exact
  generation-bound carrier during teardown.

No FORM-48 global event target was added. Long-lived ownership is instead
recorded on each member with the carrier pointer, carrier generation, family,
and four directional flags. Cleanup validates that persistent binding before
creating its regular targets. The shared cleanup order remains:

1. traverse frozen FORM-48 autonomous members;
2. remove only generation-bound, directionally owned relations;
3. clear FORM-48 member and carrier runtime state;
4. remove FORM-48 missions and decisions;
5. run shared formable runtime cleanup; and
6. clear the frozen founding ledger and identity/collision state.

The pre-existing PFX global collision guard and league/danger targets are
owned and cleared by their established shared systems. This audit did not
create a parallel owner or fallback cleanup path.

## Migration

Only one mutation seam changed: the relation-removal effect now calls the new
current-binding trigger instead of accepting mere carrier existence. No broad
helper migration was needed. Exact ledger construction, commit, post-formation
initialization, project/mission effects, and shared cleanup ordering already
use reusable helpers and were left intact.

## Architecture matrix

The targeted static architecture matrix passed 25 of 25 contracts. Its
meaningful scenarios included:

1. exact HBX/HAW/FSM packages and anchors on the success path;
2. rejection of a wrong package, anchor, original tag, or non-live Event 006
   origin without requiring scenario-launch provenance;
3. dedicated human HAW/FSM accept and withhold paths with AI kept out of those
   choices and the generic FORM-01/02/04 choices;
4. stale member-generation and stale carrier-generation teardown attempts;
5. preservation of pre-existing access/guarantees through directional
   ownership flags;
6. exact ledger count and acceptance freezing before mutation;
7. sovereign post-formation HAW/FSM with no annexation, transfer, subject,
   origin-end, free-unit, or global-scan shortcut;
8. five bounded public values and automatic/timed dissolution pressure;
9. cleanup before shared member-ledger erasure;
10. direct one-shot reason-4 publication before later generic danger
    evaluation can replace it; and
11. fail-closed readiness with no IW-173/IW-179/IW-184 attestation set site.

A separate decision-lifecycle matrix passed 10 of 10 contracts:

- each of the three carrier projects has one upfront material payment, one
  delayed cycle start, one active-project lock, and a cancellation path;
- each of the three fulfillment choices has one upfront payment, a
  response-in-progress lock, and cycle-bound cancellation cleanup;
- each mission has one success path, one timeout path, reusable cleanup, and
  explicit cancellation cleanup; and
- the human invitation pair charges acceptance once, gives withholding no
  refund/payment seam, and remains unavailable to AI.

Official decision documentation was used for cancellation semantics:
`remove_decision` does not execute a decision's remove effect or cooldown, and
`remove_mission` does not execute its completion or timeout effect. The current
cleanup therefore cannot accidentally pay, refund, succeed, or fail a removed
FORM-48 decision.

## Risks, unsupported fields, and follow-up

- FORM-48 runtime reachability remains intentionally blocked. The dedicated
  readiness helper clears attestation, and no shared readiness flag has a
  FORM-48 promotion site. Independent country-package, focus, decision,
  localisation, and event-completion audits remain prerequisites to any
  parent-owned promotion.
- Material affordability triggers use strict `>` comparisons, so a country
  holding exactly the displayed cost cannot start the action. This is
  conservative and non-exploitable, not a P0/P1 transaction defect, and was
  left unchanged to avoid broad balance/UI churn.
- MCP map, focus, event, and GUI artifacts could not be retained because of
  the tool limits listed above. Static source and vanilla-definition evidence
  was used instead; no inference from the failed calls was treated as proof.
- Static analysis cannot prove live engine execution. This audit therefore
  does not claim runtime attestation or final FORM-48 release readiness.

## Files changed by this audit

- `common/scripted_triggers/006_independence_wave_form48_triggers.txt`
  - added the generation- and family-bound autonomous-binding proof;
- `common/scripted_effects/006_independence_wave_form48_effects.txt`
  - gated reciprocal relation mutation behind that proof;
- `docs/systems/006_independence_wave_formable_registry.md`
  - documented the helper contract, call site, and stale-binding behavior; and
- this handoff.

The two dedicated FORM-48 script files were already untracked shared work when
this audit began. They were patched in place; unrelated concurrent changes were
not reverted or claimed. No constant, event target, focus, idea, decision,
localisation, adviser, portrait, or asset file was changed by this audit. No
commit was created.

## Simplifications, omissions, and blockers

No gameplay fallback or intentional simplification was used. No P0 work is
blocked. Final release/readiness promotion remains incomplete by design until
the parent reconciles the independent audits. The HOI4 MCP storage/budget
limits are validation-tool blockers only and do not justify a readiness claim.

Skills used: `chaos-redux-events`, `hoi4-decisions-missions`, and
`chaos-redux-subagents`.
