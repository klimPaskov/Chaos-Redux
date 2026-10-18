# IW-093 / IW-098 scripted package architecture

This document describes the package adapters in
`006_independence_wave_iw093_iw098_package_effects.txt`. Both packages are
admitted (agent decision D19, 2026-10-05): the static content attestation in
`006_independence_wave_package_dispatch_triggers.txt` is the admission proof,
and the package-local attestation trigger only binds the carrier tag.

## Helper contract

| Helper | Scope and inputs | Outputs and side effects |
| --- | --- | --- |
| `independence_wave_dispatch_iw093_iw098_package_setup` | Prepared country scope; `independence_wave_setup_package_id` | Routes only IDs 93/98, prepares the exact date-appropriate leader and all-male command roster, then calls package setup |
| `independence_wave_dispatch_iw093_iw098_package_final_validation` | Country scope; same setup ID | Routes final validation and preserves the shared selected/no-candidates result contract |
| `independence_wave_dispatch_iw093_iw098_package_cleanup` | Country scope; original tag and active package ID | Routes generation cleanup before the shared reset |
| `independence_wave_prepare_iw093_leadership` | Exact prepared IW-093 `DOX` scope | Recruits and promotes the male Prempeh II character only for the Event 006 origin; no living unrelated DOX scope is touched |
| `independence_wave_prepare_iw098_date_appropriate_leadership` | Exact prepared IW-098 `SOK` scope, Event 012 absent | Forms the neutrality government, then before 17 June 1938 promotes `SOK_independence_wave_hasan_dan_muazu` (startup history roster, source placeholder portrait) and from that date the vanilla `SOK_siddiq_abubakar`, writing the matching role proof |
| `independence_wave_iw098_queue_succession_check` / `_run_succession_check` | Admitted `SOK` | A Sokoto released before the cutover runs its own hidden check `chaosx.nr006.9810` every `succession_check_days` (14) days, guarded by a due date converted with `chaosx_convert_days_to_date_offset`; from the cutover it fires `chaosx.nr006.9811` once |
| `independence_wave_iw098_hand_over_sultanate` | `SOK` in `chaosx.nr006.9811` | Promotes Siddiq Abubakar III when Hasan led the government, retires Hasan, and moves the date receipts to the post-cutover branch |
| `independence_wave_prepare_iw093_command_roster` / `_iw098_command_roster` | Exact prepared Event 006 package scope | Recruits two package-specific male corps commanders only after the immutable tag, package, region, depth, archetype, and Event 012 safety proofs agree |
| `independence_wave_ensure_baseline_laws` | Admitted package setup scope | Installs civilian economy, export focus, and volunteer-only laws only when absent |
| `independence_wave_initialize_iw093_politics` / `_iw098_politics` | Admitted package setup scope | Applies centralized opening popularities and researched institutional party names; both packages begin non-electoral and neutral-aligned |
| `independence_wave_lock_iw093_royal_confederacy_route` / `_constitutional_cabinet_route` / `_veterans_emergency_route` | Exact IW-093 scope after a paid conference; matching shared route is undecided or already compatible | Locks the shared government route, installs the package route flag, applies centralized party politics, moves institutional values, and changes all five shared country mechanics |
| `independence_wave_lock_iw098_sultanic_federal_route` / `_northern_constitution_route` / `_frontier_command_route` | Exact IW-098 scope after a paid compact; matching shared route is undecided or already compatible | Locks the shared government route, installs the package route flag, applies centralized sultanic/civic/emergency politics, moves package values, and changes all five shared country mechanics |
| `independence_wave_iw098_select_sultan_by_date` | Event 006 prepared/active `SOK` scope | Chooses the dated selection receipt only when the matching role attestation exists; the separate leadership proof requires the matching ruling character, Hasan before the cutover and Siddiq after it |
| `independence_wave_initialize_iw093_values` / `_iw098_values` | Matching prepared package scope | Initializes the four visible package values from centralized constants and clamps them before setup can succeed |
| `independence_wave_clamp_iw093_values` / `_iw098_values` | Matching package country | Clamps authority/compact, institutional balance, economic network, host settlement, and security values to their documented ranges |
| `independence_wave_configure_iw093_focus_surface` | Prepared IW-093 `DOX` | Assigns the full shared framework, publishes the reviewed constitutional/popular/traditional/emergency/patron and former-host routes, excludes the radical route, and registers league, FORM-24, ambition, power-struggle, and signature hooks |
| `independence_wave_configure_iw098_focus_surface` | Prepared IW-098 `SOK` with a reviewed generic or already-loaded Event 006 tree | Assigns the full shared framework, publishes the reviewed constitutional/traditional/emergency/patron and former-host routes, excludes popular/radical routes, and registers league, FORM-25, ambition, power-struggle, and signature hooks |
| `independence_wave_setup_iw093_asante` | Prepared `DOX`, fixed package 93, state 274 anchor | Records package-local anchor/point values, initializes the paid-decision and focus surfaces, proves the two corps commanders, loads force-registry row 93, and applies the generation-bound river/jungle opening force before writing setup receipts |
| `independence_wave_setup_iw098_sokoto` | Prepared `SOK`, fixed package 98, state 902 anchor | Records package-local anchor, initializes the reviewed content only when Event 012 is absent, proves the two corps commanders, loads force-registry row 98, and applies the generation-bound mounted opening force before writing setup receipts |
| `independence_wave_validate_iw093_package` / `_iw098_package` | Active Event 006 package scope | Sets final validation success only when setup, fixed anchor, capital/succession, host survival, actual command roles, exact mapped force profile and tradition, current-generation one-time force receipt, opening-or-completed staged idea, and runtime attestation still hold |
| `independence_wave_cleanup_iw093_asante` / `_iw098_sokoto` | Matching original tag and package ID | Removes package decisions, focus receipts, shared focus/formable profiles, route exclusions, staged ideas, package-local values and the SOK succession check, then restores the generic tree if the Event 006 tree was loaded. The startup rosters (Prempeh II and the DOX commanders, Hasan and the SOK commanders) stay with their tags, so a later release finds them again. SOK cleanup never retires vanilla Siddiq or clears Event 012 focus or lifecycle flags |

The trigger file supplies the exact tag/origin wrappers, planner candidate
gates, fixed anchor proofs, Kumasi capital proof, host survival proof, date
cutover, and Event 012 safety guard.

## Admission and dispatch

The region-09 candidate predicates call
`is_independence_wave_iw093_candidate_preflight` and
`is_independence_wave_iw098_candidate_preflight`, which prove the exact
dormant tag, as for the other admitted signature packages.

The central package dispatch file calls the setup, final-validation, and
cleanup dispatcher in the same order as the admitted package families. IDs 93
and 98 are in the runtime content attestation, the Join probe order, the
execution and SCN-008 preflights and the SCN-008 ranked list.

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
character. Before 17 June 1938 Sultan Hasan dan Mu'azu Ahmadu leads the
country; from that date Event 006 reuses the vanilla Siddiq character without
duplicating his portrait or character. Setup and validation compare the anchor
and the former host with PREV, the released country, because ROOT is the
launching country during the executor passes.
The date predicate is kept as a single engine date token;
the corresponding day value is documented in the `[source: 006_independence_wave_iw093_iw098_constants.txt]` section of
`common/script_constants/006_independence_wave_constants_registry.txt`.

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

Each route conference is a single political transaction. Its package helper
first verifies that no incompatible shared route was locked while the timed
conference ran. The IW-093 conference focus does not read the shared route lock, because
a compatible shared route must still allow the package conference; the IW-093
route-lock flag is written with the package route and cleared with it. It then
writes the shared route and package route together,
sets party popularities from a centralized 100-point distribution, and
changes legitimacy, recognition, administrative capacity, security, and
instability. The emergency routes trade recognition and legitimacy for
security while increasing instability; the constitutional routes improve
recognition and reduce instability; the royal and sultanic routes emphasize
legitimacy and ordered security. Cleanup clears the package politics receipts
alongside the generation's route flags.

The setup path also installs the opening staged idea through
`independence_wave_iw093_initialize_decision_content` or
`independence_wave_iw098_initialize_decision_content`. Final validation
requires either that opening idea or its completed-project successor. Package
cleanup removes decisions, active transaction receipts, and both lifecycle
idea stages before shared origin metadata is cleared.

Each package has two male corps commanders with distinct terrain and staff
profiles. Setup writes `independence_wave_command_roster_ready` only after the
country owns both characters and both are actual corps commanders. It then
loads the canonical row from the 206-entry force registry and calls the shared
dynamic starting-force effect. IW-093 proves the row-93 `river_jungle` profile
and tradition 64; IW-098 proves the row-98 `mounted_mobile` profile and
tradition 70. Setup and final validation both require the applied force receipt
to match the current Event 006 generation, preventing reruns and stale force
inheritance.

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
