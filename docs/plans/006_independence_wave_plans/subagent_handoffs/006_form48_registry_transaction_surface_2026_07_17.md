# FORM-48 registry and transaction surface handoff

Date: 2026-07-17

Status: bounded registry tranche implemented; the full FORM-48 feature remains
fail-closed under the accepted completion boundary.

## Assignment and ownership

This tranche owns the exact FORM-48 carrier/member contract, hidden reveal
proof, shared invitation and consent hooks, strict commit proof, PFX cosmetic
identity mutation, autonomous-member integration, AI gating, rollback, and
origin cleanup. It does not own country setup or dispatch, focus trees,
characters or advisers, localisation, assets, player-facing decisions,
post-formation gameplay, or super-event work.

The implementation follows the source-backed package mapping requested by the
parent task:

- HBX / IW-184 / state 378 is the only carrier;
- HAW / IW-173 / state 629 is an autonomous consenting member;
- FSM / IW-179 / state 684 is an autonomous consenting member;
- PFX is a cosmetic identity applied to HBX, not a new country tag.

This corrects the package-ID labels in the accepted plan's locked-direction
paragraph, which conflict with the existing Event 006 package registry. The
tags, states, package constants, and parent assignment all agree on the mapping
above.

## Files and identifiers

Created:

- `common/scripted_triggers/006_independence_wave_form48_triggers.txt`
- `common/scripted_effects/006_independence_wave_form48_effects.txt`

Extended:

- `common/script_constants/006_independence_wave_formable_constants.txt`
- `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`
- `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt`
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`
- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`

Principal dedicated identifiers:

- `is_independence_wave_form48_eligible_member`
- `has_independence_wave_form48_exact_carrier_anchor`
- `has_independence_wave_form48_hidden_reveal_gate`
- `has_independence_wave_form48_exact_founding_ledger`
- `has_independence_wave_form48_strict_mutation_preconditions`
- `has_independence_wave_form48_runtime_commit_proof`
- `should_independence_wave_form48_ai_pursue`
- `should_independence_wave_form48_ai_consent_to_root`
- `independence_wave_form48_register_readiness`
- `independence_wave_formable_identity_adapter_48`
- `independence_wave_formable_integration_adapter_48`
- `independence_wave_form48_rollback_identity`
- `independence_wave_form48_origin_cleanup`

The shared files contained concurrent FORM-05 work before this tranche. The
FORM-05 readiness, identity-guard, and discovery edits visible in those files
are preserved but are not owned or claimed here.

## Transaction contract

FORM-48 never infers members from geography, culture, or an all-country scan.
Invitation enumeration is bounded to the existing Event 006 active-country
registry and accepts only the exact current-generation HBX, HAW, and FSM rows.
The frozen founding proof requires exactly three aligned member and invitation
rows, all three exact anchors, explicit accepted replies, HAW and FSM package
delegation attestations, and no carrier-member war.

Hidden reveal is recalculated through
`independence_wave_form48_refresh_hidden_reveal`. Basic package registration
publishes only `independence_wave_form48_registry_surface_registered` and does
not reveal the formable. Negotiated formation is bound to the researched
maritime-congress route; hidden proclamation is bound to the completed
high-chaos signature route. Hidden proclamation uses a unanimous compact, not
the generic controlled-settlement rule, because HAW and FSM remain sovereign
and are not controlled by HBX.

PFX mutation is protected by
`independence_wave_form48_pfx_identity_in_use`. Successful integration keeps
HBX, HAW, and FSM alive, leaves HAW/FSM tags, states, focus ownership, and Event
006 origins intact, records generation-bound carrier pointers, and creates
only directionally-owned bilateral access and guarantees. Cleanup removes only
relations that this transaction created. A partial integration failure clears
member bindings and relations before dropping PFX and its collision guard.

FORM-48 is excluded from the generic later-family identity, readiness, and
strict-commit pass-throughs. AI pursuit and AI member consent require low
willingness, an actual HBX host-collapse outcome, and the completed high-chaos
signature route. Carrier AI additionally waits until both exact AI member
packages have published their delegation attestations; normal AI remains
dormant.

## Fail-closed boundary and reconciliation

`independence_wave_form48_register_readiness` intentionally does not set the
six shared readiness flags or
`independence_wave_form48_readiness_attested`. Therefore discovery, congress,
and mutation cannot become reachable from this partial tranche. A later
completion tranche may promote those attestations only after country packages,
post-formation gameplay, localisation, asset registration and consumers,
decision/mission behavior, AI, audits, and exact super-event reachability pass
together.

The package-owned reconciliation contract is:

- HAW publishes `independence_wave_haw_pacific_delegation_ready` only from its
  completed delegation route;
- FSM publishes `independence_wave_fsm_pacific_delegation_ready` only from its
  completed federation-mandate route;
- HBX publishes `independence_wave_form48_maritime_congress_researched` only
  from its completed maritime-congress route;
- HBX calls `independence_wave_form48_refresh_hidden_reveal` after both the
  researched maritime route and the complete shared high-chaos signature
  route; neither basic setup nor family registration calls it as a reveal
  shortcut;
- package-specific origin cleanup may call
  `independence_wave_form48_origin_cleanup` before clearing family state; the
  shared cleanup already calls it in the safe pre-ledger-clear position.

The registry adapter already applies `set_cosmetic_tag = PFX`. It does not
register or consume `GFX_independence_wave_formable_form_48`; that sprite is an
asset/UI-owner insertion, preferably in a dedicated
`interface/006_independence_wave_form48.gfx`. The current shared DM-53/54/55
decisions use a generic proclamation icon and should not be globally replaced
by a FORM-48 emblem.

## Validation evidence

- All seven touched Clausewitz script/constant files finish at brace depth zero
  without a negative intermediate depth.
- Every dedicated FORM-48 scripted trigger/effect definition is unique across
  `common/`.
- Exact tag/package/anchor pairs were reconciled against the live Event 006
  package constants and package source files.
- The integration and cleanup effects mirror documented vanilla country-scope
  semantics for cosmetic tags, military access, guarantees, and explicit
  diplomatic-relation removal.
- No periodic on-action, all-country iteration, annexation, state transfer,
  country-tag registration, focus replacement, or adviser mutation was added.
- The HOI4 MCP lint attempt could not scan the files because the server returned
  `ARTIFACT_STORAGE_LIMIT`; local structural and cross-reference checks were
  used instead. This lint remains to be rerun by the parent when storage is
  available.

## Simplifications, omissions, and blockers

The full FORM-48 feature is incomplete by design. This tranche omits every
surface outside its assignment: player-facing member reply decisions,
post-formation mechanics and obligations, public localisation, GFX
registration/consumers, country packages, focus-tree content, characters,
assets, super-event reachability work, and completion audits. Readiness remains
unpromoted until those surfaces and audits pass together. No fallback identity,
generic member substitute, annexation shortcut, or silent readiness promotion
was used.

No commit was created.

Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and
`chaos-redux-decisions-missions`.

## Follow-up reconciliation — 2026-07-18

The invitation, localisation, post-formation gameplay, failure/cleanup, AI,
and dangerous-milestone omissions recorded above were implemented by the
bounded FORM-48 post-formation follow-up tranche. The original registry
transaction contract remains intact, including fail-closed readiness. Its
current handoff is
`006_form48_postformation_and_human_invitation_2026_07_18.md` in this folder.
