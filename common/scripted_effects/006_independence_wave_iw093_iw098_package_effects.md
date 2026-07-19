# IW-093 / IW-098 scripted package architecture

This document describes the bounded fail-closed adapters in
`006_independence_wave_iw093_iw098_package_effects.txt`. The adapters are
intentionally fail-closed: neither package can become a planner candidate or
runtime-attested package until its owning country implementation sets the
explicit runtime content-attestation flag after its complete audit.

## Helper contract

| Helper | Scope and inputs | Outputs and side effects |
| --- | --- | --- |
| `independence_wave_dispatch_iw093_iw098_package_setup` | Prepared country scope; `independence_wave_setup_package_id` | Routes only IDs 93/98, prepares the exact date-appropriate leader, then calls package setup |
| `independence_wave_dispatch_iw093_iw098_package_final_validation` | Country scope; same setup ID | Routes final validation and preserves the shared selected/no-candidates result contract |
| `independence_wave_dispatch_iw093_iw098_package_cleanup` | Country scope; original tag and active package ID | Routes generation cleanup before the shared reset |
| `independence_wave_prepare_iw093_leadership` | Exact prepared IW-093 `DOX` scope | Recruits and promotes the male Prempeh II character only for the Event 006 origin; no living unrelated DOX scope is touched |
| `independence_wave_prepare_iw098_date_appropriate_leadership` | Exact prepared IW-098 `SOK` scope, Event 012 absent | On or after 17 June 1938, reuses and promotes vanilla `SOK_siddiq_abubakar` and writes the post-cutover role proof; the unresolved Hasan branch remains fail-closed |
| `independence_wave_ensure_iw093_iw098_baseline_laws` | Admitted package setup scope | Installs civilian economy, export focus, and volunteer-only laws only when absent |
| `independence_wave_initialize_iw093_politics` / `_iw098_politics` | Admitted package setup scope | Applies centralized opening popularities and researched institutional party names; both packages begin non-electoral and neutral-aligned |
| `independence_wave_iw098_select_sultan_by_date` | Event 006 prepared/active `SOK` scope | Chooses the dated selection receipt only when the matching role attestation exists; the separate leadership proof requires an actual ruling character and currently admits only the post-cutover vanilla Siddiq branch |
| `independence_wave_initialize_iw093_values` / `_iw098_values` | Matching prepared package scope | Initializes the four visible package values from centralized constants and clamps them before setup can succeed |
| `independence_wave_clamp_iw093_values` / `_iw098_values` | Matching package country | Clamps authority/compact, institutional balance, economic network, host settlement, and security values to their documented ranges |
| `independence_wave_configure_iw093_focus_surface` | Prepared IW-093 `DOX` | Assigns the full shared framework, publishes the reviewed constitutional/popular/traditional/emergency/patron and former-host routes, excludes the radical route, and registers league, FORM-24, ambition, power-struggle, and signature hooks |
| `independence_wave_configure_iw098_focus_surface` | Prepared IW-098 `SOK` with a reviewed generic or already-loaded Event 006 tree | Assigns the full shared framework, publishes the reviewed constitutional/traditional/emergency/patron and former-host routes, excludes popular/radical routes, and registers league, FORM-25, ambition, power-struggle, and signature hooks |
| `independence_wave_setup_iw093_asante` | Prepared `DOX`, fixed package 93, state 274 anchor | Records package-local anchor/point values, initializes the paid-decision lifecycle and focus surface, and writes setup receipts only after content, ownership, capital, host-survival, and focus proofs |
| `independence_wave_setup_iw098_sokoto` | Prepared `SOK`, fixed package 98, state 902 anchor | Records package-local anchor, initializes the paid-decision lifecycle and reviewed full-tree surface only when Event 012 is absent, and writes setup receipts only after content, succession, ownership, host-survival, and focus proofs |
| `independence_wave_validate_iw093_package` / `_iw098_package` | Active Event 006 package scope | Sets final validation success only when setup, fixed anchor, capital/succession, host survival, opening-or-completed staged idea, and runtime attestation still hold |
| `independence_wave_cleanup_iw093_asante` / `_iw098_sokoto` | Matching original tag and package ID | Removes package decisions, focus receipts, shared focus/formable profiles, route exclusions, staged ideas, and package-local values, then restores the generic tree if the Event 006 tree was loaded. SOK cleanup never clears Event 012 focus or lifecycle flags |

The trigger file supplies the exact tag/origin wrappers, planner candidate
gates, fixed anchor proofs, Kumasi capital proof, host survival proof, date
cutover, and Event 012 safety guard.

## Admission and dispatch

The region-09 candidate predicates now call
`is_independence_wave_iw093_candidate_preflight` and
`is_independence_wave_iw098_candidate_preflight`. Each combines the exact
immutable tag with the existing legacy content-ready gate. This means the
new fixed wrappers cannot make either dormant row selectable by themselves.

The central package dispatch file calls the new setup, final-validation, and
cleanup dispatcher in the same order as the admitted package families.
Execution and scenario preflight know the exact ID/tag pairs, but the generic
runtime content-attestation list intentionally does not include IDs 93/98.
Consequently SCN-008 and frozen execution remain blocked until a future,
complete package audit promotes those IDs.

## Fixed transaction proofs

The shared executor remains the only owner of release, ownership/controller
transfer, core masking, rollback, and capital assignment. It assigns the
frozen anchor as capital before package setup. IW-093 setup then proves that
the event-target anchor is state 274, owned and controlled by DOX, and is the
capital; the former host must still own a capital. No ownership or capital
mutation is performed by this package file.

IW-098 proves the event-target anchor is state 902, is owned and controlled by
SOK, and is the capital, while the former host still owns a capital. The
package requires both a date-appropriate role receipt and an actual ruling
character. The pre-cutover branch before 17 June 1938 remains unavailable
until Hasan is sourced and authored; on/after that date Event 006 reuses the
vanilla male Siddiq character without duplicating his portrait or character.
The date predicate is kept as a single engine date token;
the corresponding day value is documented in
`common/script_constants/006_independence_wave_iw093_iw098_constants.txt`.

## Focus ownership and Event 012 safety

DOX receives the complete Event 006 framework. SOK may receive the complete
framework only through the reviewed dormant-vanilla exception: its current
tree must be `generic_focus` or the already-loaded Event 006 tree, and neither
`africa_priority_member_package_active` nor
`africa_priority_member_focus_tree_loaded` may be present. The shared Event 006
origin-availability trigger also rejects those Event 012 receipts, so a dead
Event 012 carrier cannot be silently reused as an Event 006 country.

Event 006 cleanup removes only Event 006 focus/formable state. It never clears
Event 012 package, focus, role, or lifecycle receipts. If the Event 006 tree
was loaded, cleanup restores `generic_focus`; Event 012 remains responsible
for assigning its own tree in its own origin transaction.

## Visible package values

IW-093 owns `iw093_confederated_authority`,
`iw093_court_cabinet_balance`, `iw093_cocoa_rail_throughput`, and
`iw093_host_settlement`. IW-098 owns `iw098_emirate_compact`,
`iw098_court_civic_balance`, `iw098_caravan_livestock_network`, and
`iw098_frontier_security`. The package setup initializes and validates all
eight; cleanup clears them. Focuses and paid decisions may change them only
through their owning effects and must call the matching clamp helper.

The setup path also installs the opening staged idea through
`independence_wave_iw093_initialize_decision_content` or
`independence_wave_iw098_initialize_decision_content`. Final validation
requires either that opening idea or its completed-project successor. Package
cleanup removes decisions, active transaction receipts, and both lifecycle
idea stages before shared origin metadata is cleared.

The signature focus imports contain 43 package-specific focuses. Their effects
unlock the 16 paid decision transactions without duplicating their costs or
rewards. Every decision therefore remains unavailable until its exact focus
receipt exists.

## Attestation and blockers

The package effects do not set either runtime content-attestation flag. A
future country package must set `independence_wave_iw093_runtime_content_attested`
or `independence_wave_iw098_runtime_content_attested` only after all required
country, route, force, political, role, and presentation surfaces have passed
their audits. Until then, setup returns `no_candidates`, final validation
cannot succeed, and neither package is promoted by normal or scenario paths.

FORM-24 and FORM-25 identity/integration commits are deliberately not
implemented here. Their carrier/member frozen ledgers, family adapters,
identity reservations, and integration receipts remain blocked on the
separate family readiness and member-policy work.

No Independence Wave advisor icon, advisor portrait, advisor sprite, advisor
dossier, or advisor asset manifest is part of either package. Commander
miniatures are a separate 65x67 derivative of an approved commander portrait.

## Validation performed

- Inspected the shared Event 006 executor order and confirmed capital is
  assigned before package setup, while ownership remains in the shared release
  transaction.
- Inspected the existing IW-043/IW-058 dispatch and setup contracts and
  mirrored their one-result setup/final-validation/cleanup boundaries.
- Checked the Region-09 candidate rows and exact package IDs/tags.
- Confirmed the generic content-attestation branches intentionally omit 93/98,
  keeping execution and SCN-008 promotion fail-closed.
- Confirmed SOK's Event 012 focus loader uses
  `africa_priority_member_focus_tree_loaded`; the Event 006 origin and focus
  assignment gates reject that receipt, and no Event 012 source was edited.

The map inspection tool resolved installed states 274 and 902 as valid selected
state records. No ownership, state-history, or map geometry files were changed.
