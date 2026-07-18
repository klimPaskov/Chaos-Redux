# IW-043 / IW-058 focus-framework audit handoff

Date: 2026-07-18
Mode: bounded source audit plus narrow focus integration patch
Scope: Event 006 IW-043 Middle Volga (`CHU`) and IW-058 Assyria (`ASY`) focus surfaces

## Documentation reconciliation note (2026-07-18)

The focus graph, import, prerequisite, mutex, icon, and localisation findings
below remain useful evidence. The statement that FORM-12/13/18 are fail-closed
because their attestation flags have no writer is superseded by the exact
CHU/ASY signature tranche: the adapters and five sole proof writers are
operational for their admitted carriers. The final ratification focus remains
the sole `.5810` caller after sovereign-autonomy mode records are written;
whole-Event 006 closeout is still pending.

## Executive result

The two package trees now attach to the full Event 006 framework through their
exact setup transactions. Both packages assign the full focus framework only
after package identity, institutional surfaces, cosmetic identity, and force
receipts are present. Setup publishes the common route, host-policy,
power-struggle, ambition, league, formable, and signature-module receipts;
validation requires those receipts again. Package cleanup clears that runtime
and returns the reviewed reused carriers to `generic_focus` before clearing
package identity.

The static source audit covers all 48 package focuses (23 IW-043 and 25 IW-058).
All 48 are reachable from the main tree after the import patch, have known
prerequisites, exact title/description/tooltip localisation, registered icons,
AI weights, custom effect tooltips, and hidden effect dispatch. At the time of
this audit, the FORM-12, FORM-13, and FORM-18 routes were fail-closed because
their adapter-attestation flags had no writer; the later exact-carrier pass now
supplies those attestations and sole proof writers for CHU/ASY.

No full-tree MCP artifact was produced. `hoi4.focus_inspect` first returned
`WORKSPACE_NOT_REGISTERED` for workspace `chaos_redux`, then the path-based
inspection timed out exactly after 180 seconds while parsing
`common/national_focus/006_independence_wave_focus.txt`. Deterministic source
graph and coordinate checks below were used instead; no live game session was
claimed.

## Files changed

| File | Change |
| --- | --- |
| `common/national_focus/006_independence_wave_focus.txt:43-53` | Imported three IW-043/IW-058 capstone roots plus four disconnected sibling roots so every package branch is included by vanilla shared-focus prerequisite closure. |
| `common/national_focus/006_independence_wave_iw043_iw058_focus.txt:111-116` | Moved `independence_wave_iw043_survey_rail_and_ferry_network` to `x = -2` to avoid the guarantee/federalization boxes at the same resolved coordinate. |
| `common/national_focus/006_independence_wave_iw043_iw058_focus.txt:701-707` | Moved `independence_wave_iw058_fortify_mountain_river_corridor` to `x = 1`, removing its collision with `independence_wave_iw058_convene_concordat_council`. |
| `common/scripted_effects/006_independence_wave_iw043_iw058_focus_effects.txt:122-128,171-177,453-468` | Select the exact Volga-Ural, Idel-Ural, or Mesopotamian family before calling the existing formable registration helper from the matching focus. |
| `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:908-1174` | Added full-framework assignment, route/power/ambition/league/formable/signature registration, setup receipts, and final validation gates for IW-043 and IW-058. |
| `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1176-1670` | Added focus-runtime/formable-profile teardown and guarded generic-tree reload before CHU/ASY identity cleanup. |
| `docs/systems/006_independence_wave_iw043_iw058_signature_packages.md:1-24` | Documented the focus-framework contract, route registrations, import behavior, cleanup, and fail-closed formable status. |

No decision, event, character, idea, tag, country-history, BAY, RHI, asset, or
GFX file was changed by this focus patch.

## Route coverage

The following table is the source-graph coverage, not a claim that the
formable terminal can currently commit. Route flags are set by the existing
package events/effects; focus completion effects only consume or update their
existing route contract.

| Package / route | Focus path and terminal | Route lock / safety behavior | Status |
| --- | --- | --- | --- |
| IW-043 opening | `open_middle_volga_congress` -> `confirm_kazan_mandate` -> `seat_the_delegations` | `allow_branch` and `available` require `is_independence_wave_iw043_country`. | Reachable. |
| IW-043 river economy | `secure_volga_navigation` -> `reopen_kazan_river_customs` -> `survey_rail_and_ferry_network` / `repair_cheboksary_workshops` -> `trade_beyond_the_middle_volga` | Repair accepts owned state or the existing workshop treaty; trade requires both customs and survey. | Reachable after explicit sibling imports; no dead descendant. |
| IW-043 emergency guard | `organize_the_river_guard` -> `authorize_emergency_navigation_council` -> `return_guard_to_civilian_law` | Crisis focus requires severe host threat and active security crisis; return requires emergency route, command power, and no severe threat. | Reachable after explicit `return_guard_to_civilian_law` import. |
| IW-043 federal | `charter_chamber_of_peoples` -> `guarantee_language_and_municipal_rights` + `federalize_river_cities` -> `negotiate_volga_ural_accessions` -> `ratify_modern_volga_federation` -> `convene_volga_ural_federal_congress` | Chamber is mutually exclusive with Crescent; final proof requires federal route, thresholds, and FORM-12 attestation. | Reachable; FORM-12 operational for the exact CHU carrier. |
| IW-043 restoration | `recover_bolgar_civic_memory` -> `settle_muftiate_and_civic_jurisdiction` -> `bind_crescent_to_congress` -> `invite_idel_ural_delegations` + `proclaim_modern_volga_bulgaria` -> `convene_idel_ural_compact` | Crescent is mutually exclusive with Chamber; final proof requires restoration route, thresholds, and FORM-13 attestation. The consent focus switches selected family to `idel_ural`. | Reachable; FORM-13 operational for the exact CHU carrier. |
| IW-043 shared framework | Constitutional, popular-council, traditional, emergency-military, and patron-client lanes; four former-host lanes; internal power struggle `traditional_authority_vs_assembly`; ambition, league, and signature registration. | Radical sovereignty is explicitly excluded for this package; route flags are cleared in cleanup. | Registered and validation-gated. |
| IW-058 opening | `assemble_provisional_national_council` -> `hold_mosul_council_quarter` / `seat_church_civic_and_village_delegates`; navigation and diaspora/guarantee spurs connect from those roots. | Mosul ownership is checked where the focus requires it; all nodes require the exact ASY package trigger. | Reachable. |
| IW-058 church compact | `write_four_community_guarantees` -> `settle_church_and_civil_jurisdiction` -> `convene_concordat_council` -> `charter_church_civic_compact` + `link_synods_villages_and_diaspora` -> `ratify_concordat_state`. | Concordat and Civic Assembly are mutually exclusive; guardianship blocks constitutional choice. | Reachable. |
| IW-058 civic assembly | `convene_civic_national_assembly` -> `charter_municipal_and_community_chambers` + `bind_diaspora_experts_to_public_service` -> `ratify_civic_national_state`. | Civic route is mutually exclusive with Concordat and consumes the existing community-guarantee gate. | Reachable through the OR prerequisite closure of the settlement capstone. |
| IW-058 levies guardianship | `discipline_the_levies_board` -> `authorize_levies_guardianship` -> `restore_civilian_command`. | Authorization requires severe host threat, active crisis, and civilian-law receipt; restore requires command power and no severe threat. | Reachable after explicit `restore_civilian_command` import. |
| IW-058 autonomy / settlement | `fortify_mountain_river_corridor` + `entrench_mosul_recognition` -> `negotiate_former_host_settlement` -> `offer_mesopotamian_autonomy_charter` -> `convene_mesopotamian_federal_congress` -> `ratify_mesopotamian_settlement`. | Offer requires either constitutional route and excludes guardianship; FORM-18 readiness also requires exact family/profile and attestation. | Reachable; FORM-18 operational for the exact ASY carrier, with sovereign autonomy mutually exclusive. |
| IW-058 shared framework | Constitutional, popular-council, traditional, emergency-military, and patron-client lanes; four former-host lanes; internal power struggle `traditional_authority_vs_assembly`; ambition, league, signature, and default `mesopotamian_federation` profile. | Radical sovereignty is explicitly excluded; guardianship is a temporary spur and cannot coexist with autonomy. | Registered and validation-gated. |

## Reachability and prerequisite audit

The deterministic parser follows every `prerequisite = { focus = ... }` token
from each imported shared focus, including both tokens in a same-block OR
prerequisite. Results:

| Check | Before patch | After patch |
| --- | ---: | ---: |
| Package focus IDs | 48 | 48 |
| Reachable from `006_independence_wave_focus.txt` imports | 40 (the earlier audit counted only the first token in OR blocks) | 48 |
| Unreachable after correct OR-token traversal | 8 reported by the earlier narrow parser | none |
| Package-prefixed unknown prerequisites | none | none |
| Resolved package coordinates | 48 | 48 |
| Exact coordinate collisions | two (`109,5` and `121,5`) | none |

The two actual pre-patch coordinate collisions were:

- `independence_wave_iw043_federalize_river_cities` with
  `independence_wave_iw043_survey_rail_and_ferry_network`; the survey node is
  now at resolved `(107,5)`.
- `independence_wave_iw058_convene_concordat_council` with
  `independence_wave_iw058_fortify_mountain_river_corridor`; the fortification
  node is now at resolved `(122,5)` after its `x = 1` adjustment.

The prerequisite review found no OR/AND inversion. Separate prerequisite
blocks are used for required civic/economic/host gates; the two constitutional
choices in IW-058 autonomy are one same-block OR, and the final settlement
capstone uses the intended same-block OR for church versus civic ratification
plus a separate former-host prerequisite.

Mutual exclusions are symmetric and correct:

- `independence_wave_iw043_bind_crescent_to_congress` ↔
  `independence_wave_iw043_charter_chamber_of_peoples`.
- `independence_wave_iw058_convene_concordat_council` ↔
  `independence_wave_iw058_convene_civic_national_assembly`.

## Icon, localisation, and reward coverage

| Surface | Audit result | References |
| --- | --- | --- |
| Focus IDs | 48 shared focuses, exactly 23 IW-043 + 25 IW-058 | `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` |
| Title / description / tooltip | 48/48 title keys, 48/48 `_desc`, 48/48 `_tt`; English file has UTF-8 BOM | `localisation/english/006_independence_wave_iw043_iw058_focus_l_english.yml` |
| Focus icons | 20 unique icon IDs used; 20/20 are defined in the package GFX | `interface/006_independence_wave_iw043_iw058_focus_icons.gfx` |
| Shine sprites | Matching `_shine` registrations exist for every package icon family | same GFX file |
| AI | 48/48 have `ai_will_do` blocks | focus source; package AI strategy in `common/ai_strategy/006_independence_wave_iw043_iw058_ai_strategy.txt` |
| Reward dispatch | 48/48 have `custom_effect_tooltip` plus `hidden_effect` calling an existing `independence_wave_complete_focus_iw043_*` or `*_iw058_*` helper | focus source and `common/scripted_effects/006_independence_wave_iw043_iw058_focus_effects.txt` |
| Reward mismatch | none found; tooltip names match the focus IDs and helper effects | focus source / localisation / effect file |

No focus icon or localisation fallback was introduced. The reward helpers
retain existing decision, event, idea, force, variable, and formable hooks;
this patch only corrected the selected family input where the helper was
previously called without a family value.

## AI behavior review

There are no missing `ai_will_do` blocks. Focus AI uses urgent/high/cautious
weights and threat modifiers on navigation, river guard, emergency, recovery,
and settlement nodes. The separate package strategy file is origin-bounded to
CHU/ASY and gates federal/restoration/emergency or church/civic/guardianship
profiles on exact route flags, setup receipts, safe reserves, and crisis state.
Decision AI owns action costs, guarantee selection, and formable consent.

Low-priority tuning risk: several constitutional branch focuses use a stable
`high` or `cautious` weight rather than an additional route-specific factor.
That is not a missing AI surface—the route is still hidden/blocked by its
`available` and package flags—but it can be revisited after live decision
weights and settlement costs are finalized. No patch was made because a broad
AI rebalance is outside this narrow focus integration scope.

## Setup and cleanup behavior before / after

| Package | Before | After |
| --- | --- | --- |
| IW-043 | Exact package setup initialized country mechanics but omitted focus assignment and most shared framework receipts. | `independence_wave_setup_iw043_middle_volga` assigns `full_framework`, loads `independence_wave_focus_tree`, exposes five common lanes, all four host lanes, power struggle, ambition, league, `volga_ural_federation`, signature module, and final receipt validation. |
| IW-058 | Exact package setup initialized country mechanics but omitted focus assignment and most shared framework receipts. | `independence_wave_setup_iw058_assyria` publishes the same shared framework with `mesopotamian_federation`, plus exact ASY validation. |
| CHU/ASY cleanup | Package cleanup cleared package-owned flags but could leave the shared focus tree/runtime on a reused vanilla carrier. | Cleanup calls `independence_wave_clear_focus_runtime`, clears the selected formable profile and route exclusions, reloads `generic_focus` only when the carrier currently uses `independence_wave_focus_tree`, then clears package identity last. |

The setup receipt list is intentionally explicit rather than relying on a
single broad success flag. It includes full-framework assignment, focus
assignment value, internal power struggle, ambition, league, selected and
loaded formable family, signature module, five common route availability flags,
and four host-policy route flags.

## Simplifications, omissions, and blockers

- FORM-12, FORM-13, and FORM-18 are not operational. Their readiness gates
  still require `independence_wave_form12_adapter_attested`,
  `independence_wave_form13_adapter_attested`, or
  `independence_wave_form18_adapter_attested`; `rg` found no writer for any
  of those flags. No fallback identity, core, claim, member absorption, or
  cosmetic mutation was added.
- The focus inspector and renderer could not provide an artifact: one call
  reported `WORKSPACE_NOT_REGISTERED`, and the path-based call timed out after
  180 seconds. Engine-side layout rendering, connector crossings, and live
  focus completion were therefore not validated here.
- CHU and ASY use the full Event 006 framework after the accepted review that
  their carrier trees are generic/minimal. Cleanup deliberately returns them
  to `generic_focus`; no new country identity or route family was designed.
- Branch AI uses existing package strategy and static focus weights. No broad
  route-weight rebalance was attempted.

These are documented limits, not hidden substitutes. The narrow patch contains
no gameplay fallback.

## Parent review checklist

1. Review the seven `shared_focus` imports at
   `common/national_focus/006_independence_wave_focus.txt:43-53`.
2. Review the two coordinate changes and all 48 focus blocks in
   `common/national_focus/006_independence_wave_iw043_iw058_focus.txt`.
3. Verify setup receipt gates at
   `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:908-1174`
   and cleanup order at `:1176-1670`.
4. Keep formable adapter attestation fail-closed until the owning compatibility
   evidence is promoted.
5. If live validation becomes available, render both carriers after setup,
   complete one federal/restoration or church/civic route each, attempt the
   emergency spur, and confirm cleanup returns to `generic_focus` without
   leaking package route flags.
