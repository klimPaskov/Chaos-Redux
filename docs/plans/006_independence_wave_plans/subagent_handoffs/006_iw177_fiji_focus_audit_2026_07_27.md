# IW-177 Fiji Focus Audit

Date: 2026-07-27.

Scope: source-only audit of the six Fiji full-framework focuses, root registration, localisation, icons, AI hooks, generic-tree protection, and the FORM-39 route-surface guard.

Verdict: PASS for the six focus definitions and their full-framework registration after the explicit open-board import; HOLD for runtime package attestation because the FORM-39 adapter surface is intentionally fail-closed and remains unwired.

## Changed files and identifiers

I added `shared_focus = independence_wave_fij_open_labor_shipping_board_focus` at `common/national_focus/006_independence_wave_focus.txt:45`.

Before this patch the root imported only `independence_wave_fij_convene_constituent_congress_focus` and `independence_wave_fij_ratify_island_compact_focus` at lines 44-45, and the open-board focus was a parallel sibling of the communal-veto focus rather than an ancestor of the ratify capstone.

After this patch the root explicitly imports convene, open labor and shipping, and ratify at lines 44-46, while the other three Fiji focuses are pulled through the prerequisite graph.

No Fiji focus definition, reward helper, localisation string, icon, decision, or adapter was changed by this audit.

The current parent-owned generic-tree protection is reviewed as correct: `can_initialize_independence_wave_iw_177_package` requires `has_focus_tree = generic_focus` at `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:230-235`, so IW-177 cannot overwrite a meaningful non-generic tree.

## Route coverage

| Route surface | Focus and source | Availability and prerequisite semantics | Reward hook | Status |
|---|---|---|---|---|
| Founding congress | `independence_wave_fij_convene_constituent_congress_focus` at `common/national_focus/006_independence_wave_pacific_focus.txt:285-299` | Requires the shared capital-preparation focus, FIJ package, capital control, and no active matching decision. | `independence_wave_fij_focus_convene_constituent_congress` | PASS |
| Communal representation | `independence_wave_fij_register_communal_veto_focus` at lines 301-315 | Requires convene; package-gated and blocked while its decision is active. | `independence_wave_fij_focus_register_communal_veto` | PASS |
| Labor and shipping | `independence_wave_fij_open_labor_shipping_board_focus` at lines 317-331 | Requires convene; package-gated and blocked while its decision is active. It is parallel to communal veto, so it needed the explicit root import. | `independence_wave_fij_focus_open_labor_shipping_board` | PASS after import patch |
| Former-host settlement | `independence_wave_fij_settle_colonial_accounts_focus` at lines 333-347 | Requires communal veto, a living former host, and no active matching decision. | `independence_wave_fij_focus_settle_colonial_accounts` | PASS, conditional on a living host |
| Coastal defense | `independence_wave_fij_charter_coastal_guard_focus` at lines 349-363 | Requires communal veto and no active matching decision; severe-host-threat raises AI priority. | `independence_wave_fij_focus_charter_coastal_guard` | PASS |
| Island compact | `independence_wave_fij_ratify_island_compact_focus` at lines 365-380 | Two separate prerequisite blocks require both settlement and coastal guard; availability also requires stable congress, recognition, and no active matching decision. | `independence_wave_fij_focus_ratify_island_compact` | PASS for focus surface; FORM-39 publication remains HOLD |

The shared-focus closure check after the import patch reaches all six Fiji IDs: convene, register communal veto, open labor and shipping, settle colonial accounts, charter coastal guard, and ratify island compact.

## Missing or simplified content

- FORM-39 Melanesian Federation has no `independence_wave_formable_identity_adapter_39` and no `independence_wave_formable_integration_adapter_39` anywhere in the repository.
- IW-177 setup selects `constant:independence_wave_formable_family.melanesian_federation` and registers the family at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:798-815`, but `has_prepared_independence_wave_iw_177_package_setup` requires `independence_wave_fij_melanesian_route_adapter_complete` at `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:419-462`.
- The adapter flag has no setter; it is only required by the prepared-setup proof and cleared during FIJ cleanup at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:1014`.
- No PNG/WPG member-package transaction or FORM-39 carrier/X-tag identity transaction is present, so the fail-closed HOLD is correct and should not be bypassed from a focus reward.
- The open-board focus is intentionally parallel to communal veto in the focus tree, while the decision surface requires communal veto before opening the board; this is a route-order risk to review if the intended player sequence is strictly linear, but it is not patched here.

## Icon coverage

| Focus ID | Icon ID | GFX registration and DDS |
|---|---|---|
| `independence_wave_fij_convene_constituent_congress_focus` | `GFX_goal_independence_wave_founding_administration` | Registered in `interface/006_independence_wave.gfx:3-4`; DDS exists. |
| `independence_wave_fij_register_communal_veto_focus` | `GFX_goal_independence_wave_popular_councils` | Registered at `interface/006_independence_wave.gfx:7-8`; DDS exists. |
| `independence_wave_fij_open_labor_shipping_board_focus` | `GFX_goal_independence_wave_infrastructure_authority` | Registered at `interface/006_independence_wave.gfx:19-20`; DDS exists. |
| `independence_wave_fij_settle_colonial_accounts_focus` | `GFX_goal_independence_wave_former_host_settlement` | Registered at `interface/006_independence_wave.gfx:21-22`; DDS exists. |
| `independence_wave_fij_charter_coastal_guard_focus` | `GFX_goal_independence_wave_army_integration` | Registered at `interface/006_independence_wave.gfx:17-18`; DDS exists. |
| `independence_wave_fij_ratify_island_compact_focus` | `GFX_goal_independence_wave_regional_formable` | Registered at `interface/006_independence_wave.gfx:25-26`; DDS exists. |

All six icons are distinct within FIJ and reuse the existing Event 006 icon family rather than introducing bespoke Fiji art.

## Localisation and reward checks

All six focus title, description, and tooltip keys resolve in `localisation/english/006_independence_wave_pacific_l_english.yml:286-303`.

The corresponding decision-facing names, descriptions, and failure tooltips resolve at `localisation/english/006_independence_wave_pacific_l_english.yml:267-284`.

Each focus reward helper is defined and scoped to FIJ in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:542-630`, and each helper is idempotent on its completion flag.

No title, description, tooltip, icon, or reward mismatch was found in the six focus blocks.

## AI behavior gaps

All six focuses define `ai_will_do` values using the shared focus constants at `common/national_focus/006_independence_wave_pacific_focus.txt:298-379`.

Coastal guard receives an urgent base and severe-host-threat preference, while island compact uses a cautious base and a severe-host-threat modifier.

FIJ package strategy hooks exist at `common/ai_strategy/006_independence_wave_pacific.txt:95-120`, with country-specific production and restraint constants at `common/script_constants/006_independence_wave_pacific_constants.txt:121-129`.

There is no FIJ-specific focus-order strategy that prefers communal veto before the parallel labor-and-shipping focus or adapts the ratify choice to FORM-39 readiness; this is a medium-priority AI depth gap, not a missing focus gate.

## Validation and tooling limits

- A source parser verified the root import list and prerequisite graph, and all six Fiji focus IDs were reachable after the explicit open-board import.
- Static icon checks confirmed all six GFX IDs, texture paths, and DDS files exist.
- Static localisation and helper scans confirmed all six focus key families and reward helper definitions resolve.
- `hoi4.focus_inspect` returned revision `96129cffc0f40cd28bf9e3ff500a6fdf6ed93d94c4990b00d1e8086f319559ee` with 14 blocking layout diagnostics in the central Event 006 tree; its inline inventory did not include the standalone Pacific shared-focus source, so no Fiji geometry conclusion is drawn.
- `hoi4.focus_render` completed successfully for the central tree and produced the HTML/SVG/JSON artifacts under workspace `mod_chaos_redux_ea3b2d67c2c0`; those artifacts are central-tree evidence only and are not used to infer closed Fiji geometry.
- In-game launch and live save validation were skipped per repository policy.

## High-priority fixes and remaining risks

1. Retain the explicit open-board root import at `common/national_focus/006_independence_wave_focus.txt:45`; removing it silently drops one of the six FIJ focuses from the full tree.
2. Keep the FORM-39 adapter guard fail-closed until the identity adapter, integration adapter, X-tag, PNG/WPG member packages, consent transaction, and collision tests exist.
3. Decide whether the parallel open-board focus is intended to precede communal veto; if not, add a narrow FIJ prerequisite or availability gate in a later route-design pass.
4. Add FIJ-specific focus-order AI only if the design requires route-aware sequencing beyond the current per-focus weights.
5. The central tree's 14 blocking layout diagnostics remain outside this FIJ-local audit and should not be attributed to the Fiji package.

No separate improvement plan was written because the only broad gap is the intentionally deferred FORM-39 package, which requires a country/formable tranche rather than a focus-local patch.

