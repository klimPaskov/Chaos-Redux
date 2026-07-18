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
| `independence_wave_apply_iw043_institutional_surface` / `_iw058_` | Exact package plus route flags | Idempotently recruits the eight package characters, adds leader roles, and keeps the three staged idea slots coherent. |
| `independence_wave_restore_iw043_civilian_surface` / `_iw058_` | Temporary emergency/guardianship route cleared | Removes only the temporary role/idea and reapplies the prior permanent route. Guarantees, route flags, and settlement records remain. |
| `independence_wave_apply_iw043_cosmetic_identity` / `_iw058_` | Cosmetic-ready flag and route flags | Applies opening/outcome X-suffixed cosmetics. Emergency IW-043 preserves the prior outcome; IW-058 uses a temporary guardianship cosmetic and restores the prior route. |
| `independence_wave_record_iw043_force_receipts` / `_iw058_` | Generic force mapping, current generation, opening force budget | Records durable one-time country receipts; the shared allocator separately stamps each newly materialised division with immutable package/generation provenance. No second formation is created. |
| `independence_wave_bind_*_force_package` / `independence_wave_release_*_force_package` | Durable receipt flags plus division-scoped provenance | Binds only an owned division carrying the exact package and current-generation receipt, then persists the global target for the timed operation. Release clears the pointer and binding state without disbanding or refunding a unit; the designated-formation marker remains on the materialised division and is cleared only by exact package cleanup, so rebuilding a same-named template cannot spoof completion. |
| `independence_wave_*_begin_paid_transaction` | Decision-provided temporary id and cost variables | Validates all resources, spends once, and stores a normal paid transaction id. |
| `independence_wave_*_commit_paid_transaction` / `_rollback_` | Decision temporary transaction id | Closes the matching ledger. Rollback intentionally does not refund; timeout/cancel effects own the authored penalty. |
| `independence_wave_setup_iw043_middle_volga` / `_iw058_assyria` | Shared setup temporary package values and targets | Loads generic force mapping, applies starting force, writes package identity/values, adds three opening ideas, recruits institutional roles, records receipts, and fires opening incident `chaosx.nr006.4301`/`.5801` once. Setup succeeds only after the exact surfaces validate. |
| `independence_wave_validate_iw043_package` / `_iw058_` | Live package state | Sets shared final-validation result only when setup, anchor, route mutex, values, receipts, cosmetics, and institutional surface remain valid. |
| `independence_wave_cleanup_iw043_middle_volga` / `_iw058_assyria` | Exact live package identity | Removes every package decision and all inventoried receipt/pending/rejected/settlement flags, ideas, roles, cosmetics, variables, adapter flags, and route flags. Recruited characters are left dormant for repeatable Event 006 generations. Package id/identity is cleared last. Event 005/Soviet flags are untouched. |

## Constants and tuning

`common/script_constants/006_independence_wave_iw043_iw058_constants.txt`
holds the package starts, thresholds, costs/durations, force shares, idea and
leader modifiers, AI weights, transaction serials, and fail-closed adapter
states. The generic Event 006 decision-cost and force-package tables remain the
source for shared resource costs and starting-force profiles.

## Event targets and cleanup

The setup chain consumes the existing regular
`independence_wave_setup_anchor_state` and `independence_wave_setup_former_host`
targets. No new global target is created. The existing execution reset owns
the shared target lifecycle; package cleanup only removes package-owned
variables and flags.

## FORM-12 / FORM-13 / FORM-18 adapters

Numeric meta-effect entry points (`identity_adapter_12/13/18` and
`integration_adapter_12/13/18`) exist so the formable registry resolves safely.
Every entry point requires the exact IW-043/IW-058 readiness trigger and an
explicit adapter-attestation flag. With attestation unset, identity, cores,
claims, member absorption, and terminal mutation are inert. Vanilla CHU
Idel-Ural and ASY neo-Assyrian/neo-Mesopotamian decisions were inspected, but
no exact keyed Event 006 compatibility contract was proven in this tranche;
there is no fallback adapter.

## Limitations and follow-up

- Base IW-043/IW-058 runtime content and cosmetic surfaces are admitted by the
  shared origin-safe registry. FORM-12/13/18 adapter flags and achievement
  writer hooks remain intentionally inert and fail-closed.
- The package does not add advisor portraits, icons, sprites, GFX, or other
  advisor assets; gameplay advisors remain asset-neutral.
