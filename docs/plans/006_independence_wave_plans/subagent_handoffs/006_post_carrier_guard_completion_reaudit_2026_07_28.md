# Event 006 post-carrier-guard completion re-audit

Date: 2026-07-28

Scope: read-only completion re-audit after the additive focus carrier fail-closed patch and the v31 documentation reconciliation. This audit compares current source with `006_event_completion_audit_v31_2026_07_28.md`, `006_focus_carrier_fail_closed_2026_07_28.md`, the current IW-012 implementation and country-package audits, and the allocator evidence. No gameplay, localisation, GFX, binary asset, workbook, or export file was edited.

## Verdict

**HOLD / PARTIAL.**

The additive carrier guard does not create a new admission or setup regression for the current eleven-package attestation set.

IW-012 still passes the new carrier proof in source order, and the allocator audit still passes with eleven exact attestations across ten compatible reservation groups.

The re-audit found a separate pre-existing IW-012 gameplay reachability defect that the current package and decision audits do not disclose. The natural Coastwatch ledger cannot reach the Armed Neutrality or Emergency Military gate, and the harbour stability predicate cannot be satisfied through the published project path.

## Additive carrier guard

### IW-012 setup path

The carrier proof is ordered correctly.

1. `independence_wave_prepare_country_origin` records the Event 006 origin before package setup, so `is_independence_wave_active_country = yes` is available to the new carrier trigger.
2. `independence_wave_setup_iw_012_ice` initializes the ICE ledgers and sets `independence_wave_ice_lifecycle_initialized`.
3. The setup then sets `independence_wave_focus_carrier_registered`.
4. Only after those receipts exist does setup call `independence_wave_assign_focus_framework` with `additive_overlay`.
5. `can_attach_independence_wave_additive_focus_carrier` requires the active Event 006 origin, the registration flag, the ICE lifecycle flag, and `has_focus_tree = iceland_tree`.
6. `has_prepared_independence_wave_iw_012_package_setup` now requires both the registration flag and `independence_wave_additive_focus_overlay`, so a failed carrier proof cannot publish package setup success.
7. Shared cleanup removes both the registration flag and `independence_wave_focus_overlay_carrier_missing`.

The existing IW-012 initialization trigger already required `has_focus_tree = iceland_tree`, so the patch does not introduce a new tree identity prerequisite that was absent from the admitted package contract.

### Other additive consumers

Current source has two package setup calls that request `additive_overlay`: IW-012 ICE and IW-179 FSM.

The new carrier trigger intentionally contains only the reviewed ICE branch. FSM therefore records `independence_wave_focus_overlay_carrier_missing` and fails its existing prepared-package proof if setup is attempted.

This does not reduce the current eleven-package attestation set because IW-179 is already outside content attestation pending sourced leadership and complete package admission. It does add a concrete future re-admission requirement: FSM needs a reviewed owning-tree carrier branch or an accepted decisions-only disposition before its package can be promoted.

No wildcard carrier, unsupported shared-focus insertion effect, meaningful-tree overwrite, or fallback was introduced.

## New IW-012 source finding

### High: the Coastwatch and harbour path is not naturally reachable

`independence_wave_ice_coastwatch_readiness` starts at `20`.

Before Armed Neutrality, the six project definitions provide only one positive Coastwatch change: `Expand the Coastwatch` adds `15`. The other five pre-route project changes add zero to Coastwatch.

The natural pre-route maximum is therefore `35`.

Both `independence_wave_ice_declare_armed_neutrality` and `can_lock_independence_wave_ice_emergency_military_route` require Coastwatch Readiness at or above `armed_neutrality_threshold = 55`.

Armed Neutrality is also unavailable after any government route locks. Constitutional, Traditional, or Patron-Client can therefore close the route slot before the only second `+15` Coastwatch project could run, even if its threshold were otherwise met.

The harbour success trigger is stricter. `has_stable_independence_wave_ice_state` requires Coastwatch Readiness at or above `60` and Shipping Security at or above `60`. The five naturally reachable non-Armed projects produce maximum pre-route values of `35` Coastwatch and `55` Shipping Security. No other source writer raises those ICE-specific variables before the route gates.

Consequences:

- Armed Neutrality cannot become naturally available.
- The Emergency Military focus cannot become naturally available.
- The advertised six-project, 1,230-day harbour stabilization path cannot complete.
- The harbour mission cannot resolve through `has_stable_independence_wave_ice_state`.
- The formal-route AI matrix cannot be treated as fully source-reachable even though all four `ai_will_do` blocks exist.

This defect is not caused by the carrier guard. It is a stale acceptance claim in the current IW-012 package, decision, event documentation, resume packet, and source-map wording.

The design owner must reconcile the Coastwatch and Shipping progression, the `55` and `60` thresholds, the timing of Armed Neutrality, and whether formal route selection may occur before the harbour project sequence is complete. This audit does not choose a balance repair or authorize a fallback.

## Authority comparison

| Authority | Current disposition |
| --- | --- |
| v31 whole-event audit | Remains the whole-event authority for **HOLD / PARTIAL**, eleven attestations, ten compatible groups, and the carried completion matrix. Its narrow static IW-012 admission remains valid, but its package-completeness wording must now carry the ledger reachability defect above. |
| Additive carrier fail-closed handoff | Static PASS for the reviewed ICE carrier and cleanup contract. Its explicit HOLD for generic meaningful-tree carriers remains correct. |
| IW-012 implementation and country-package audits | The exact adapter, dispatch, carrier, setup, final validation, cleanup, and attestation links remain present. Their claim that the project and route package has no remaining static threshold blocker is stale. |
| IW-012 focus carrier handoff | The twelve ICE imports and four formal route nodes remain present. Live shared-focus visibility remains open, and Emergency Military now also has the source-level ledger gate blocker described above. |
| Allocator evidence | Current static counts remain unchanged and pass. The older eight-package probability handoff is historical first-draw evidence, while v31 and the current audit script are authoritative for the eleven-package set. |
| v31 documentation reconciliation | Current counts and the **HOLD / PARTIAL** authority are aligned. The new carrier receipt contract is documented only in the fail-closed handoff, and the current source map and resume packet overstate IW-012 route-arbitration closure until the ledger defect is resolved or disclosed. |

## Completion status by surface

| Surface | Status | Remaining boundary |
| --- | --- | --- |
| Additive carrier guard | **Static PASS for ICE** | Live shared-focus visibility and save/load persistence remain unproved. |
| Generic additive overlays | **HOLD / fail-closed** | Only ICE has a reviewed carrier branch. FSM and the remaining meaningful-tree overlay packages require explicit carrier or accepted decisions-only dispositions. |
| Allocator and synchronized release | **Static PASS / runtime HOLD** | The audit passes with 149 publishers, 126 automatic or high-chaos selectable packages, 138 SCN-ranked packages, eleven attestations, ten compatible groups, and the exact 3/4/5/7/10 ladder. Ordinary waves, exact-ten execution, host survival, rollback, repeat memory, Event 005 collision, and save/load remain unproved. |
| IW-012 package | **Static admission PASS / gameplay PARTIAL** | Carrier and setup admission are intact. Coastwatch, Armed Neutrality, Emergency route, harbour resolution, live release, force materialization, AI timing, and save/load remain blocked or unproved. |
| Shared focus framework | **Route coverage / validator HOLD** | The central tree remains unchanged and retains fourteen coupled geometry blockers. No coordinated reflow or live carrier render evidence was added. |
| Country packages | **PARTIAL / HOLD** | Eleven of 193 selectable registry rows are exactly attested. The remaining packages cannot be promoted from tags, loaders, portraits, shells, or generic content. |
| SCN-008 | **Static PARTIAL / runtime HOLD** | All 32 mode and intensity cells still lack live selector, collision, reservation, rollback, persistence, host-war, patron, and balance evidence. Only eleven of 138 ranked packages are attested. |
| Assets and portraits | **PARTIAL / HOLD** | The flat shelf has 54 original-size masters, but many grounded rosters, symbols, flags, formable identities, and report variants remain blocked. `docs/assets/006_independence_wave/manifest.md` still says 49 masters while the shelf manifests say 54. |
| Super-events | **PARTIAL / BLOCKED** | `6002` is source-wired but lacks predicate reachability, queue, settings, playback, and hidden-formable proof. `6001` remains blocked by the absence of an accepted rights-cleared recording. |
| Achievements | **Static definitions / reachability HOLD** | The sixteen accepted definitions still lack complete qualification, near-miss, disqualification, persistence, save/load, scenario, and route-reachability evidence. Several formable and package paths remain unadmitted. |
| Documentation and catalog | **PARTIAL** | v31 counts and overall status are reconciled, but the carrier guard is not yet promoted into the source map or resume packet, the IW-012 route-closure wording is now too strong, and the root asset manifest retains the stale 49-master count. |

## Validation performed

- Traced the exact ICE setup order from origin preparation through package setup, active registration, final validation, commit, and cleanup.
- Enumerated every current `additive_overlay` setup request and every carrier-registration writer.
- Compared the new guard with the exact content-attestation, normal preflight, scenario preflight, setup, final-validation, cleanup, region weight, and reservation paths for IW-012.
- Ran `python -B .tools/audit_event6_allocator.py`. It passed with the v31 counts and ordering.
- Traced every writer of `independence_wave_ice_coastwatch_readiness` and `independence_wave_ice_shipping_security` through setup, projects, route rewards, failure, and cleanup.
- Did not rerun the focus MCP inspector because the patch does not modify either focus source and the existing tool does not expand imported `shared_focus` nodes into useful carrier metrics.
- Did not launch Hearts of Iron IV or claim live execution evidence.

## Recommended next actions

1. Keep the carrier guard and its narrow ICE branch. Do not add a generic meaningful-tree wildcard.
2. Resolve the IW-012 Coastwatch, Shipping, Armed Neutrality, route-order, and harbour-stability design as one bounded balance change, then re-audit all four route gates and the 1,440-day mission path.
3. Promote the carrier receipt contract and the new IW-012 blocker into the source map, resume packet, package documentation, and current audit disposition.
4. Give FSM and each future additive package its own preservation-safe carrier proof or an accepted decisions-only disposition before re-admission.
5. Repair the fourteen central focus geometry diagnostics through a coordinated reflow.
6. Run the outstanding live allocator, exact-ten, host-survival, rollback, save/load, force, focus-visibility, route-AI, SCN-008, achievement, GUI, and super-event acceptance matrices.

## Changed files

- Added this read-only audit handoff.
- No gameplay, localisation, GFX, asset, workbook, or export file was changed.

## Simplifications, omissions, and blockers

No fallback or simplification was used by this audit. The guard patch is statically safe for current ICE admission, but Event 006 remains incomplete and the IW-012 ledger reachability defect prevents a clean package-completion claim.
