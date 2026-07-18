# Event 006 IW-043 / IW-058 scripted package architecture

This file documents the helper surface in
`006_independence_wave_iw043_iw058_package_effects.txt`. All helpers run in
country scope and are guarded by exact original tag, Event 006 active-origin,
package id, package flag, and (where required) the shared origin-safe runtime
attestation. No helper performs a periodic or world-country scan.

## Helper map

| Helper | Inputs | Outputs / side effects |
| --- | --- | --- |
| `independence_wave_clamp_iw043_package_values` / `_iw058_` | Package normal variables | Clamps package values to the constants table. |
| `independence_wave_recalculate_iw043_rights_compact` | IW-043 clause flags | Deterministically writes `iw043_rights_compact` as the 20-point start plus 15 per ratified clause, clamps it, and derives `iw043_rights_compact_complete`. |
| `independence_wave_recalculate_iw058_guarantee_count` | Four IW-058 guarantee flags | Recomputes `iw058_community_guarantee_count`. |
| `independence_wave_record_iw058_autonomy_external_treaty_terms` | Exact sovereign IW-058 carrier, all four community guarantees, owned/controlled Mosul anchor | Records the boundary, return/protection, transit/property, and security chapters shared by the former-host and regional-partner autonomy paths. The separate church/civil competence settlement exclusively owns the jurisdiction record. |
| `independence_wave_apply_iw043_political_surface` / `_iw058_` | Exact package plus signature/shared route flags | Applies the centralized opening, constitutional, popular, restoration/traditional, emergency, or patron popularity profile; sets election law and package-specific party names without touching vanilla history. |
| `independence_wave_dispatch_iw043_iw058_government_route_politics` | Exact package after the shared route lock | Reapplies the political and institutional surfaces so shared-route outcomes receive a matching institutional leader and final party identity. Non-IW-043/IW-058 countries are inert. |
| `independence_wave_apply_iw043_institutional_surface` / `_iw058_` | Exact package plus route flags | Idempotently recruits the eight package characters, adds the signature and shared-route leader roles, and keeps the three staged idea slots coherent. |
| `independence_wave_restore_iw043_civilian_surface` / `_iw058_` | Temporary emergency/guardianship route cleared | Removes only the temporary role/idea and reapplies the prior permanent route. Guarantees, route flags, and settlement records remain. |
| `independence_wave_apply_iw043_cosmetic_identity` / `_iw058_` | Cosmetic-ready flag and route flags | Applies opening/outcome X-suffixed cosmetics. Emergency IW-043 preserves the prior outcome; IW-058 uses a temporary guardianship cosmetic and restores the prior route. |
| `independence_wave_record_iw043_force_receipts` / `_iw058_` | Generic force mapping, current generation, opening force budget | Records durable one-time country receipts; the shared allocator separately stamps each newly materialised division with immutable package/generation provenance. No second formation is created. |
| `independence_wave_bind_*_force_package` / `independence_wave_release_*_force_package` | Durable receipt flags plus division-scoped provenance | Binds only an owned division carrying the exact package and current-generation receipt, then persists the global target for the timed operation. Release clears the pointer and binding state without disbanding or refunding a unit; the designated-formation marker remains on the materialised division and is cleared only by exact package cleanup, so rebuilding a same-named template cannot spoof completion. |
| `independence_wave_*_begin_paid_transaction` | Decision-provided temporary id and cost variables | Validates all resources, spends once, and stores a normal paid transaction id. |
| `independence_wave_*_commit_paid_transaction` / `_rollback_` | Decision temporary transaction id | Closes the matching ledger. Rollback intentionally does not refund; timeout/cancel effects own the authored penalty. |
| `independence_wave_setup_iw043_middle_volga` / `_iw058_assyria` | Shared setup temporary package values and targets | Loads generic force mapping, applies starting force, writes package identity/values, adds three opening ideas, recruits institutional roles, records receipts, and fires opening incident `chaosx.nr006.4301`/`.5801` once. Setup succeeds only after the exact surfaces validate. |
| `independence_wave_validate_iw043_package` / `_iw058_` | Live package state | Sets shared final-validation result only when setup, anchor, route mutex, values, receipts, cosmetics, and institutional surface remain valid. |
| `independence_wave_cleanup_iw043_middle_volga` / `_iw058_assyria` | Exact live package identity | Removes every package decision and all inventoried receipt/pending/rejected/settlement flags, ideas, roles, cosmetics, variables, adapter flags, and route flags. Recruited characters are left dormant for repeatable Event 006 generations. Package id/identity is cleared last. Event 005/Soviet flags are untouched. |
| `independence_wave_iw_formable_invalidate_signature_receipts` | Carrier scope; no arguments | Clears signature anchor, settlement, identity, integration, stage, and score receipts without touching league membership or Event 006 origin. Called on a new proposal and by transaction cleanup. |
| `independence_wave_iw_formable_write_signature_settlement_records` | Carrier scope after the consent ledger is rebuilt | Writes only the FORM-12, FORM-13, or FORM-18 constitutional records earned by that family's local package contract and consent threshold. Local clauses and external consent remain separate proof surfaces. |
| `independence_wave_iw_formable_capture_generation_receipts` | Carrier scope after the shared member/anchor recount | Deduplicates current owned-and-controlled member anchors, records the current generation/family/proposal sequence, and sets the family settlement receipt only when family minimums, authored settlement clauses, method policy, and league permission pass. No cores or sovereignty changes. |
| `independence_wave_iw_formable_prepare_signature_congress` / `_finalize_signature_congress` | Carrier scope inside the paid package congress | Opens the immutable invitation proposal, then rebuilds member and unique-anchor ledgers at expiry and dispatches the keyed shared commit only when the exact family contract still passes. |
| `independence_wave_iw_formable_reset_signature_congress` | Carrier scope after timeout or cancellation | Closes invitation state, clears signature receipts, restores the discovered transaction stage, and applies the family-specific retry cooldown without a periodic scan. |
| `independence_wave_iw_formable_score_ai_consent` | Candidate scope with `ROOT` as carrier | Scores only exact FORM-12/13/18 candidates from route compatibility, host threat, recognition, bilateral relation, autonomy offer, disputes, and instability. AI accepts or withholds through generic consent effects; human candidates remain pending for the reply event. |
| `independence_wave_iw_formable_stage_member_from_root` / `_stage_consented_members` | Candidate scope / carrier scope; frozen consent and current receipt ledgers | Records generation-safe staged integration markers for consenting sovereign members. Staging never ends an Event 006 origin, transfers states, adds cores, creates subjects, or rewrites league membership. |
| `independence_wave_iw_formable_advance_staged_members` | Carrier scope after formation | Advances only exact staged members through charter registration and initial defense/revenue integration. The member tag, territory, sovereignty, Event 006 origin, focus content, and units remain unchanged. |
| `independence_wave_iw_formable_cleanup_transaction` / `_failure_cleanup` | Carrier scope during cancel, failure, or package reset | Clears carrier and member stage markers, invalidates signature receipts, restores the pre-signature carrier cosmetic on failure, and leaves package origins and league state intact. Cleanup is idempotent. |
| `independence_wave_formable_identity_adapter_12/13/18` | Registry meta-effect; exact family readiness and adapter attestation | Applies only the family-specific `X` cosmetic and writes a generation/family/sequence identity receipt. It never writes an attestation flag or grants cores/claims. |
| `independence_wave_formable_integration_adapter_12/13/18` | Registry meta-effect after an identity receipt | Runs bounded consenting-member staging, then writes integration committed plus its generation/family/sequence receipt only when the family consent minimum is staged. It never absorbs a member or ends an origin. |
| `independence_wave_write_iw043_*_route_proof` / `independence_wave_write_iw058_*` | Exact capstone, settlement, anchor-defense, or host-crisis transaction | Writes mutually exclusive IW-043 route proof and the three independent IW-058 achievement proofs only after their full package, origin, territory, constitutional, civilian-control, and no-client predicates pass. |

## Exact member admission

`is_independence_wave_iw043_formable_member_candidate` is intentionally not a
generic major/reachability predicate. It requires a live sovereign Event 006
country, a nonzero anchor currently owned and controlled by that country, and
one of the current region-05 package/tag pairs:

- `IW-044/TAT`, `IW-045/BSK`, `IW-047/MEL`, `IW-048/UDM`, or `IW-050/KOM`.

The shared `CHU` rows (`IW-043` and `IW-046`) and the active ASY signature
identity are explicit collision exclusions. A candidate already running a
formable proposal or committed formation is also excluded. This keeps
FORM-12/13 inside the researched Volga-Ural package set and proves unique
anchors rather than relying on a member-count hint.

`is_independence_wave_iw058_formable_member_candidate` uses the same origin,
sovereignty, collision, and unique-anchor checks but admits only the current
region-06 corridor rows `IW-060/KUR` and `IW-062/CJX`. `IW-059` is a vanilla
overlay, not an active member country, and the surrounding Caucasus rows are
not FORM-18 members.

## Constants and tuning

`common/script_constants/006_independence_wave_iw043_iw058_constants.txt`
holds the package starts, thresholds, costs/durations, force shares, political
profiles, idea and leader modifiers, AI weights, transaction serials, and
adapter states. The shared `independence_wave_formable_signature` category in
`common/script_constants/006_independence_wave_formable_constants.txt` owns the
FORM-12/13/18 member, consent, unique-anchor, and AI-score thresholds. The
generic Event 006 decision-cost and force-package tables remain the source for
shared resource costs and starting-force profiles.

## Event targets and cleanup

The setup chain consumes the existing regular
`independence_wave_setup_anchor_state` and `independence_wave_setup_former_host`
targets. A named guarantor accepted with explicit sovereignty safeguards may
be persisted as the package-owned global target
`independence_wave_iw058_regional_settlement_partner` only when the target is
a sovereign same-region Event 006 actor or one of the explicit bounded
regional vanilla tags. The target must still exist, remain at peace, and
guarantee IW-058 when the autonomy mission starts, expires, and writes its
final settlement proof. IW-058 setup and cleanup both clear the global target
and every counterpart receipt, so a later repeatable generation cannot
inherit the treaty.

The signature receipt pass uses one short-lived regular target for the current
member and one for its current anchor while deduplicating the anchor array.
Those targets are not saved globally and are invalidated with the proposal
receipt ledger. No periodic or all-country action owns this work; the only
country pass is the existing bounded `global.independence_wave_active_countries`
array pass during an explicit invitation/ledger action.

## FORM-12 / FORM-13 / FORM-18 adapters

Numeric meta-effect entry points (`identity_adapter_12/13/18` and
`integration_adapter_12/13/18`) exist so the formable registry resolves safely.
Every entry point requires the exact IW-043/IW-058 readiness trigger and an
explicit adapter-attestation flag written only by successful exact package
setup. With attestation unset, identity and integration remain inert. The
identity compatibility gate keeps ordinary families on
`has_independence_wave_selected_formable_identity_available` while signature
families use their keyed adapter readiness. Human invitation events
`chaosx.nr006.4311`, `.4312`, and `.5811` are dispatched only after a matching
signature invitation snapshot is stored; AI candidates use the scored helper
instead. Formation presentations use `.4313`, `.4314`, and `.5812`; the
Mesopotamian settlement presentation remains `.5810` and is called only by the
final ratification focus after either the first federal integration stage or
the complete sovereign-autonomy compact. The full
vanilla CHU Idel-Ural and ASY neo-Assyrian/neo-Mesopotamian decisions are
preserved by exact compatibility redeclarations that add only a negative
active-IW-043/IW-058 visibility guard. There is no fallback adapter.

FORM-18 and the sovereign-autonomy compact share one permanent terminal-choice
lock. Both start gates reject the other transaction's receipt, completion,
mode, and final proof; both finalization gates recheck the opposite branch
before commit. The first successful transaction writes
`iw058_mesopotamian_terminal_settlement_locked`. Exact package cleanup clears
the lock, while ordinary route changes cannot. The final settlement proof also
requires the lock, preventing a stale proof from surviving a cross-mode switch.

## Asset boundary and audit status

- The package does not add advisor portraits, icons, sprites, GFX, or other
  advisor assets; gameplay advisors remain asset-neutral.
- FORM-12/13/18 use only cosmetic `X` identities, explicit sovereign consent,
  unique owned-and-controlled anchors, and staged constitutional integration.
  They do not annex members, create subjects, add blanket cores, duplicate
  units, or replace another Event 6 country package.
- The two achievement definitions remain hidden until the focus, decision,
  country-package, localisation, and completion audits attest the exact proof
  writers and cleanup matrix. The runtime writers themselves fail closed.
