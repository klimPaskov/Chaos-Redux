# IW-043 / IW-058 focus closeout audit

Date: 2026-07-18
Scope: Event 006 IW-043 Middle Volga (`CHU`) and IW-058 Assyria (`ASY`) focus packages, their focus helpers, English focus localisation, and the FORM-12/13/18 terminal surfaces.
Mode: bounded source audit plus narrow ordering/localisation correction.
Supersedes the earlier focus audit's MCP and adapter-writer observations where this handoff supplies newer evidence.

## Documentation reconciliation note (2026-07-18, post-audit wiring)

The structural focus findings and layout diagnostics below remain useful
evidence, but the post-audit source now resolves the sovereign ordering noted
here: `independence_wave_iw058_ratify_sovereign_autonomy_compact` writes the
compact and settlement-mode records without firing `chaosx.nr006.5810`, and
the final ratification focus helper is the sole `.5810` caller. The exact
CHU/ASY FORM-12/13/18 transactions are operational under their admitted
carrier contracts. Preserve historical audit findings; do not reintroduce the
old decision call or treat its fail-closed wording as current status.

## Executive result

The package source contains 48 shared focuses: 23 IW-043 and 25 IW-058. All
48 are reachable through the imports in `common/national_focus/006_independence_wave_focus.txt`.
The prerequisite graph has no unknown package IDs or cycles; the intended
same-block OR semantics are retained for the constitutional alternatives and
the IW-058 settlement capstone. The two route mutexes are symmetric.

Two missing focus title/description pairs were added:

- `independence_wave_iw043_repair_cheboksary_workshops`;
- `independence_wave_iw058_fortify_mountain_river_corridor`.

The FORM-18 first-stage member-registration decision no longer fires event
`chaosx.nr006.5810`. It now records only first-stage integration. Event 5810
remains on the final IW-058 ratify-focus helper after the settlement mode and
records are valid. The sovereign-autonomy compact decision writes its mode and
compact records but does not call 5810. This removes the first-stage proof
write that made the federation ratify focus fail its
`NOT = { has_country_flag = independence_wave_assyria_mesopotamian_settlement_complete }`
gate.

At audit time there was one unresolved dynamic ordering issue: the sovereign
autonomy decision still fired 5810 before the
`ratify_mesopotamian_settlement` focus could pass its `can_write_*` trigger.
The post-audit wiring removed that call; the federation and sovereign routes
now use the final ratification focus as the terminal presentation surface.
The residual-risks section is retained as historical audit context.

No Independence Wave advisor icon, portrait, sprite, dossier, or related asset
was created, requested, or referenced. Existing commander small portraits and
BAY/RHI protected leader portraits were not touched.

## Changed files and identifiers

| File | In-scope change | Identifiers |
| --- | --- | --- |
| `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` | FORM terminal focus availability now uses exact carrier, founding-invitation capability, and adapter-attestation gates instead of the broad readiness shorthand. | `independence_wave_iw043_convene_volga_ural_federal_congress`, `independence_wave_iw043_convene_idel_ural_compact`, `independence_wave_iw058_convene_mesopotamian_federal_congress` |
| `common/scripted_effects/006_independence_wave_iw043_iw058_focus_effects.txt` | Matching completion helpers publish the terminal surface only when the same carrier/capability/attestation contract is true; the final IW-058 ratify helper still dispatches 5810 only after `can_write_*` passes. | `independence_wave_complete_focus_iw043_convene_volga_ural_federal_congress`, `independence_wave_complete_focus_iw043_convene_idel_ural_compact`, `independence_wave_complete_focus_iw058_convene_mesopotamian_federal_congress`, `independence_wave_complete_focus_iw058_ratify_mesopotamian_settlement` |
| `common/decisions/006_independence_wave_iw043_iw058_decisions.txt` | Removed the event 5810 call from first-stage FORM-18 member registration; the decision records integration only. Final FORM-18 federation congress uses 5812, while sovereign autonomy retains 5810. | `independence_wave_iw058_register_form18_member_charters`, `independence_wave_iw058_hold_form18_federal_congress`, `independence_wave_iw058_ratify_sovereign_autonomy_compact` |
| `localisation/english/006_independence_wave_iw043_iw058_focus_l_english.yml` | Added the two missing title/description pairs; existing `_tt` keys remain aligned. | `independence_wave_iw043_repair_cheboksary_workshops`, `independence_wave_iw058_fortify_mountain_river_corridor` |

No focus GFX file was changed. The existing icon registrations cover every
focus reference.

## High-priority fixes first

1. **Completed:** keep 5810 out of
   `independence_wave_iw058_register_form18_member_charters`; first-stage
   integration must not write the final settlement proof.
2. **Post-audit wiring recorded:** the sovereign-autonomy decision writes the
   compact and settlement-mode records without firing 5810; the final
   ratification focus is the sole `.5810` caller after its `can_write_*`
   contract passes. Preserve this ordering and review it in the parent-wide
   closeout audit.
3. **Preserve the current FORM gates:** do not replace the exact carrier,
   founding-invitation, and adapter-attestation checks with a broad readiness
   shortcut unless the owning adapter contract is promoted at the same time.
4. **Documentation follow-up:** reconcile stale signature-package handoffs
   that still describe the pre-promotion adapter-attestation and proof-writer
   state; the exact CHU/ASY tranche now has those operational receipts.
5. **Low priority:** consider route-aware AI modifiers for fixed-weight
   constitutional/formable capstones after the settlement decision costs and
   adapter contracts are finalized.

## Missing or simplified content list

- No focus node, prerequisite edge, route mutex, helper dispatch, icon, or
  player-facing localisation triple is missing after the two repaired pairs.
- No branch was replaced with a generic fallback and no new route family was
  invented. Emergency branches remain temporary spurs, as designed.
- FORM-12/13/18 adapter execution remains gated by exact carrier, consent,
  anchor, and staged-integration contracts; those transactions are operational
  for CHU/ASY, and this audit did not invent identity, core, claim,
  member-absorption, or cosmetic fallbacks.
- The former sovereign-autonomy terminal ordering issue is recorded below as
  historical audit context. Current source keeps the compact decision as a
  mode/record writer and the final ratification focus as the sole 5810 caller.

## Route coverage

The table distinguishes structural graph reachability from dynamic terminal
proof ordering. Every focus is in the imported graph; the sovereign note is a
runtime contract issue, not an omitted node.

| Package / route | Focus path and terminal | Route lock / prerequisite semantics | Audit status |
| --- | --- | --- | --- |
| IW-043 opening | `open_middle_volga_congress` -> `confirm_kazan_mandate` -> `seat_the_delegations` | Exact IW-043 country trigger and framework setup gate. | Reachable. |
| IW-043 river economy | `secure_volga_navigation` -> `reopen_kazan_river_customs` -> `survey_rail_and_ferry_network` and `repair_cheboksary_workshops` -> `trade_beyond_the_middle_volga` | Separate prerequisite blocks enforce the required navigation/customs/survey chain; repair accepts the existing controlled-state or workshop-treaty condition. | Reachable; both sibling spurs are imported. |
| IW-043 river guard / emergency | `organize_the_river_guard` -> `authorize_emergency_navigation_council` -> `return_guard_to_civilian_law` | Emergency authorization requires the severe-host-threat/crisis contract; return requires the emergency route, command power, and no immediate severe threat. | Reachable. |
| IW-043 restoration | `recover_bolgar_civic_memory` -> `settle_muftiate_and_civic_jurisdiction` -> `bind_crescent_to_congress` -> `invite_idel_ural_delegations` and `proclaim_modern_volga_bulgaria` -> `convene_idel_ural_compact` | `bind_crescent_to_congress` is mutually exclusive with the federal chamber; the terminal focus opens only on the exact FORM-13 carrier/capability/attestation contract. | Structurally reachable; FORM-13 is operational for the exact CHU carrier under its three-member/anchor/consent and staged-integration contract. |
| IW-043 federal | `charter_chamber_of_peoples` -> `guarantee_language_and_municipal_rights` and `federalize_river_cities` -> `negotiate_volga_ural_accessions` -> `ratify_modern_volga_federation` -> `convene_volga_ural_federal_congress` | Chamber is mutually exclusive with Crescent; terminal focus publishes the FORM-12 decision surface but does not itself commit the congress. | Structurally reachable; FORM-12 is operational for the exact CHU carrier under its three-member/anchor/consent and staged-integration contract. |
| IW-043 shared spurs | Navigation, trade, emergency, power-struggle, ambition, league, host-policy, and signature helpers are attached by the existing package setup/cleanup framework. | The package cleanup returns a reviewed carrier to `generic_focus` only when it is currently using the package tree. | Registered and graph-connected. |
| IW-058 opening | `assemble_provisional_national_council` -> `hold_mosul_council_quarter` and `seat_church_civic_and_village_delegates`; navigation, diaspora, guarantee, jurisdiction, and levies spurs follow. | Exact IW-058 country trigger, Mosul anchor, and framework setup receipts gate the nodes. | Reachable. |
| IW-058 church compact | `write_four_community_guarantees` -> `settle_church_and_civil_jurisdiction` -> `convene_concordat_council` -> `charter_church_civic_compact` and `link_synods_villages_and_diaspora` -> `ratify_concordat_state` | Concordat assembly is mutually exclusive with the civic assembly; guardianship blocks constitutional capstones. | Reachable. |
| IW-058 civic assembly | `write_four_community_guarantees` -> `settle_church_and_civil_jurisdiction` -> `convene_civic_national_assembly` -> `charter_municipal_and_community_chambers` and `bind_diaspora_experts_to_public_service` -> `ratify_civic_national_state` | Same settlement prerequisites as the church route, with the symmetric church/civic mutex. | Reachable. |
| IW-058 levies guardianship | `discipline_the_levies_board` -> `authorize_levies_guardianship` -> `restore_civilian_command` | Authorization is limited to severe threat/crisis and civilian-law receipts; restoration requires command power and no immediate severe threat. | Reachable. |
| IW-058 federation settlement | `fortify_mountain_river_corridor` + `entrench_mosul_recognition` -> `negotiate_former_host_settlement` -> `offer_mesopotamian_autonomy_charter` -> `convene_mesopotamian_federal_congress` -> `ratify_mesopotamian_settlement` | The final ratify prerequisite is one same-block OR (`convene_mesopotamian_federal_congress` or `offer_mesopotamian_autonomy_charter`), so federation and sovereign settlement branches are not accidentally ANDed. The federation `can_write_*` branch requires the five FORM-18 settlement records and no final proof. | Reachable after the first-stage 5810 removal; final focus can write 5810 in federation mode. |
| IW-058 sovereign settlement | `offer_mesopotamian_autonomy_charter` -> `ratify_sovereign_autonomy_compact` decision -> sovereign mode | The decision completes the autonomy records and writes the sovereign mode; the final ratification focus owns the terminal 5810 presentation after the compact records pass. | Operational for the exact ASY carrier; preserve the post-audit focus-owned terminal ordering and include it in parent closeout review. |
| IW-058 shared spurs | Corridor, diaspora, guarantee, host settlement, power-struggle, ambition, league, signature, and the `mesopotamian_federation` profile are setup/cleanup-registered. | Guardianship is a temporary spur and is excluded from autonomy settlement proof. | Registered and graph-connected. |

## Prerequisite, mutex, and terminal-proof audit

- `independence_wave_iw058_ratify_mesopotamian_settlement` uses one
  prerequisite block containing `convene_mesopotamian_federal_congress` and
  `offer_mesopotamian_autonomy_charter`; this is the intended OR. It has no
  second prerequisite block that would accidentally require both.
- `offer_mesopotamian_autonomy_charter` uses one same-block OR for the church
  versus civic ratification and a separate former-host prerequisite; this is
  the intended OR-plus-AND shape.
- IW-043 mutex: `bind_crescent_to_congress` <->
  `charter_chamber_of_peoples` (symmetric).
- IW-058 mutex: `convene_concordat_council` <->
  `convene_civic_national_assembly` (symmetric).
- No package prerequisite references an unknown focus ID, and no prerequisite
  cycle was found.
- Before the correction, first-stage FORM-18 registration fired 5810 and
  wrote `independence_wave_assyria_mesopotamian_settlement_complete` before
  the final focus. After the correction, first-stage registration only calls
  `independence_wave_iw_formable_advance_staged_members` and records
  `iw058_form18_member_charters_registered` after the integration threshold.
- Current event call sites relevant to this ordering are the final focus
  helper (`common/scripted_effects/006_independence_wave_iw043_iw058_focus_effects.txt:495`)
  and sovereign autonomy decision
  (`common/decisions/006_independence_wave_iw043_iw058_decisions.txt:2318`).
  There is no 5810 call in first-stage registration.

## Icon coverage

The package uses 20 unique focus icon IDs, each with a base and matching
`_shine` sprite in `interface/006_independence_wave_iw043_iw058_focus_icons.gfx`.
All 48 references resolve to an existing sprite and texture; no focus uses a
missing or placeholder icon.

| Icon family | Use count | Package |
| --- | ---: | --- |
| `GFX_goal_independence_wave_iw043_navigation` | 5 | IW-043 |
| `GFX_goal_independence_wave_iw043_congress` | 3 | IW-043 |
| `GFX_goal_independence_wave_iw043_river_guard` | 3 | IW-043 |
| `GFX_goal_independence_wave_iw043_bolgar_constitution` | 3 | IW-043 |
| `GFX_goal_independence_wave_iw043_federal_chamber` | 3 | IW-043 |
| `GFX_goal_independence_wave_iw043_form12_congress` | 2 | IW-043 |
| `GFX_goal_independence_wave_iw043_form13_compact` | 2 | IW-043 |
| `GFX_goal_independence_wave_iw043_muftiate_civic_courts` | 1 | IW-043 |
| `GFX_goal_independence_wave_iw043_rights_charter` | 1 | IW-043 |
| `GFX_goal_independence_wave_iw058_mosul_corridor` | 3 | IW-058 |
| `GFX_goal_independence_wave_iw058_diaspora_liaison` | 3 | IW-058 |
| `GFX_goal_independence_wave_iw058_levies_civilian_control` | 3 | IW-058 |
| `GFX_goal_independence_wave_iw058_external_guarantee` | 3 | IW-058 |
| `GFX_goal_independence_wave_iw058_church_civic_charter` | 3 | IW-058 |
| `GFX_goal_independence_wave_iw058_civic_assembly_charter` | 3 | IW-058 |
| `GFX_goal_independence_wave_iw058_provisional_council` | 2 | IW-058 |
| `GFX_goal_independence_wave_iw058_mesopotamian_autonomy` | 2 | IW-058 |
| `GFX_goal_independence_wave_iw058_four_guarantees` | 1 | IW-058 |
| `GFX_goal_independence_wave_iw058_church_civil_jurisdiction` | 1 | IW-058 |
| `GFX_goal_independence_wave_iw058_form18_congress` | 1 | IW-058 |

## Localisation and reward mismatch list

- Missing localisation found and repaired: the two title/description pairs
  listed above. All 48 title keys, 48 `_desc` keys, and 48 `_tt` keys now
  exist in the UTF-8 BOM English file.
- No remaining title/description/tooltip key mismatch was found.
- Every focus has a custom player-facing effect tooltip and a hidden helper
  dispatch. Reward helpers are route-specific (founding, administration,
  public settlement, security reform, diplomacy, ambition, or stabilization)
  rather than a repeated generic reward.
- The event-backed route choices intentionally place their immediate route
  reward in the event/decision surface; this is not a missing focus reward.
- No advisor, portrait, sprite, dossier, or other IW advisor asset reference
  was introduced.

## AI behavior gaps

- All 48 focuses have an `ai_will_do` block.
- Base-weight coverage is 12 urgent, 26 high, and 10 cautious focuses.
- Eight focus nodes have explicit route/context modifiers for severe host
  threat, war avoidance, religious settlement, or crisis recovery: IW-043
  navigation, river guard, trade, Crescent, emergency authorization; and
  IW-058 diaspora liaison, guardianship authorization, and corridor
  fortification.
- Remaining constitutional/formable capstones use fixed high/cautious base
  values and rely on their availability, mutex, and route flags. This is a
  low-priority tuning gap, not a missing AI surface; no broad rebalance was
  attempted inside this narrow audit.

## Validation evidence

Static checks performed against the current working tree:

1. Parsed the main tree and package file: 176 regular main-tree focuses and 48
   package shared focuses; package closure from the main imports is complete.
2. Checked package prerequisite IDs, cycles, and the OR/AND block shape:
   unknown IDs = none; cycles = none; final IW-058 ratify prerequisite is a
   single OR block.
3. Checked focus presentation surfaces: 48 helper definitions, 48 helper
   dispatches, 48 title/description/tooltip triples, 48 icon references, 20
   base icon families plus 20 shine sprites, and no missing textures.
4. Confirmed the FORM-18 first-stage decision has no 5810 call and that the
   only relevant current calls are the final focus helper and sovereign
   autonomy decision.
5. Ran `hoi4.focus_inspect` and `hoi4.focus_render` on the assigned main
   `independence_wave_focus_tree` workspace. The tools scanned the main tree
   (176 focuses), not the imported shared package file. They returned a render
   and inspect artifact but reported 14 blocking diagnostics/148 total
   diagnostics for pre-existing main-tree connector crossings, long links,
   and node intersections. No package-specific diagnostic was emitted.

Artifacts:

- Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3b55861139dce56e35245e5328b2ef2f7235cc3b989c7d1001188fc19467e76/c93c86c2782b401fb4e56e572b2c4f4bed6807eae9681f07d42f30ccfd66a542/focus-inspect.20518884dc7ce5fc.json`
- HTML render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e5d353603f609e1a252a396d26b25816c45088ac05208d86d148431373bec78/9a01009603d7589b0754699cad2b3a9d3d722b8d9b05473b7ae9869392ec47d0/independence_wave_focus_tree.focus.html`
- SVG render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43639e97c751583ed85f81908e60040ca831a2eb6ab3537c99b92fa6b2fa52d8/0034d5982bd044016a9fd35454a813b64bea614f6abcf431d2fd2cb9ceeca18e/independence_wave_focus_tree.focus.svg`
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a77d58e67b3d82362bd28ea5200f7eed69c4ca7f31b74aafdc74de08fd8d8701/05121797d2b9579a85d8716e3498b1bea9815a1c02373b26a8841c8ca44dfdba/independence_wave_focus_tree.focus.json`

Skipped meaningful validation:

- No live game/session completion was claimed. The available inspector does
  not parse the imported shared-focus file independently, and the main-tree
  diagnostics are unrelated connector/layout issues outside this package
  scope.
- No new focus asset production was requested or run, per the explicit
  no-IW-advisor-assets constraint.

## Simplifications, omissions, and blockers

- FORM-12, FORM-13, and FORM-18 are operational for their exact CHU/ASY
  carriers under the admitted consent, anchor, paid-congress, and staged
  integration contracts. No fallback identity, core, claim, member
  absorption, or cosmetic mutation was added.
- The sovereign-autonomy ordering paragraph above is retained as historical
  audit evidence. Current source removes the decision's 5810 call and leaves
  the final ratification focus as the sole terminal presentation caller; the
  parent-wide closeout should verify that ordering and its proof records.
- Existing documentation in
  `docs/systems/006_independence_wave_iw043_iw058_signature_packages.md` and
  earlier handoffs still describe all FORM adapters as having no attestation
  writer. Current setup writes explicit attestation receipts, so those docs
  need a documentation-curator reconciliation; gameplay files were not
  broadened to resolve that stale-doc surface here.
- MCP reported main-tree layout diagnostics; this audit did not redesign the
  unrelated 176-focus main layout.

No broader route family, country identity, advisor package, or formable chain
was added. No improvement-loop plan was necessary because the package routes
are deep and connected; the remaining work is a narrow terminal-proof ordering
decision.

## Parent review checklist

1. Review the post-audit 5810 call-site ordering in
   `common/decisions/006_independence_wave_iw043_iw058_decisions.txt:2228-2245,2318`
   and
   `common/scripted_effects/006_independence_wave_iw043_iw058_focus_effects.txt:492-498`.
2. Confirm that federation FORM-18 now reaches the ratify focus after
   first-stage registration and final member integration, without an early
   final-proof flag.
3. Confirm the accepted sovereign path: the compact decision records mode and
   treaty facts, while the final ratify focus writes the terminal presentation
   and proof only after its `can_write_*` contract passes.
4. Reconcile stale signature-package documentation before making a broad
   completion claim for FORM-12/13/18.
