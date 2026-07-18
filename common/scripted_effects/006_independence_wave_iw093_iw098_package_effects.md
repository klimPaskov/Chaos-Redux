# IW-093 / IW-098 scripted package architecture

This document describes the bounded foundational adapters in
`006_independence_wave_iw093_iw098_package_effects.txt`. The adapters are
intentionally fail-closed: neither package can become a planner candidate or
runtime-attested package until its owning country implementation sets the
explicit runtime content-attestation flag after its complete audit.

## Helper contract

| Helper | Scope and inputs | Outputs and side effects |
| --- | --- | --- |
| `independence_wave_dispatch_iw093_iw098_package_setup` | Country scope; `independence_wave_setup_package_id` | Routes only IDs 93/98 to package setup; no mutation itself |
| `independence_wave_dispatch_iw093_iw098_package_final_validation` | Country scope; same setup ID | Routes final validation and preserves the shared selected/no-candidates result contract |
| `independence_wave_dispatch_iw093_iw098_package_cleanup` | Country scope; original tag and active package ID | Routes generation cleanup before the shared reset |
| `independence_wave_iw098_select_sultan_by_date` | Event 006 prepared/active `SOK` scope | Chooses a pre/post 17 June 1938 role receipt only when the matching role attestation exists; it does not author a role surface |
| `independence_wave_setup_iw093_asante` | Prepared `DOX`, fixed package 93, state 274 anchor | Records package-local anchor/point values and setup receipts only after content, ownership, capital, and host-survival proofs |
| `independence_wave_setup_iw098_sokoto` | Prepared `SOK`, fixed package 98, state 902 anchor | Records package-local anchor and Event 012-preservation receipt only after content, succession, ownership, and host-survival proofs |
| `independence_wave_validate_iw093_package` / `_iw098_package` | Active Event 006 package scope | Sets final validation success only when setup, fixed anchor, capital/succession, host survival, and runtime attestation still hold |
| `independence_wave_cleanup_iw093_asante` / `_iw098_sokoto` | Matching original tag and package ID | Clears only package-local flags/variables. SOK cleanup never clears Event 012 focus or lifecycle flags |

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

IW-098 proves the event-target anchor is state 902 and that the former host
still owns a capital. The package requires a date-appropriate role receipt:
the pre-cutover branch is before 17 June 1938 and the post-cutover branch is
on/after that date. The date predicate is kept as a single engine date token;
the corresponding day value is documented in
`common/script_constants/006_independence_wave_iw093_iw098_constants.txt`.

## Event 012 safety

Sokoto setup records whether `africa_priority_member_focus_tree_loaded` was
present but never clears or replaces that focus tree. No Event 006 focus-tree
assignment is made here. Cleanup clears only the generation-local receipt and
leaves Event 012’s own flags and lifecycle state to its owning system.

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

## Validation performed

- Inspected the shared Event 006 executor order and confirmed capital is
  assigned before package setup, while ownership remains in the shared release
  transaction.
- Inspected the existing IW-043/IW-058 dispatch and setup contracts and
  mirrored their one-result setup/final-validation/cleanup boundaries.
- Checked the Region-09 candidate rows and exact package IDs/tags.
- Confirmed the generic content-attestation branches intentionally omit 93/98,
  keeping execution and SCN-008 promotion fail-closed.
- Confirmed SOK’s Event 012 focus loader uses
  `africa_priority_member_focus_tree_loaded`; no Event 012 source was edited.

No live-game or MCP render validation was available in this implementation
context. No country, focus, decision, idea, character, localisation, or
visual/asset source was touched.
