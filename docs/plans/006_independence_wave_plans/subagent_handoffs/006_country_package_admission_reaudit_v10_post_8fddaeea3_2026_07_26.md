# Event 006 country-package admission re-audit v10

Audit date: 2026-07-26.

Audit mode: read-only country-package and admission re-audit. No gameplay, map, localisation, focus, portrait, flag, or asset files were changed by this audit.

## Verdict

The ten compile-time attested packages have complete static country-package coverage except for the explicitly partial Frisia decision lane. Nine of the ten packages are static PASS. Frisia (`IW-007` / `AGX`) is PARTIAL because its 300-day coastal-conference decision can finish and grant rewards after recognition, membership, authorization, or client-route validity changes, its displayed strategic cost does not match its three-civilian-factory modifier, and its custom trigger tooltips are incomplete. These defects are in `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:575-607` and remain parent-scope work.

All ten package identities are present in the current execution attestation in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:55-68`. Static readiness and capacity branches exist for all ten in `common/scripted_triggers/006_independence_wave_triggers.txt`, including Event 005 origin/state/host clearance, exact tag readiness, anchor checks, host survival, duplicate-country checks, duplicate-anchor checks, and duplicate reservation-group checks. This is compile-time evidence only; no live allocation, save/load, or in-game execution claim is made.

The ten rows expose only nine compatible reservation groups because Rhineland (`RHI`) and Saar (`AJX`) intentionally share `RG-RHINE-SAAR`. The exact ten-country band therefore remains fail-closed until a tenth unique group is admitted or a valid map rebinding is accepted. This is a parent-wide capacity blocker, not a missing static package surface.

## Authority and reviewed evidence

- Current source is the post-reversion tree at `8fddaeea3`, after `904c277d5`, `b19a116cc`, `f8ca54d24`, and `cf2316a9a`.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` supplies the accepted ten-row registry, portrait policy, map binding summary, and runtime boundary. Its historical statement that the `f8ca54d24` reflow was current is superseded by `docs/plans/006_independence_wave_plans/subagent_handoffs/006_shared_focus_geometry_reversion_2026_07_26.md` and the current `8fddaeea3` source.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event_completion_audit_v9_final_2026_07_26.md` remains the parent-wide completion baseline and correctly records the nine-group/tenth-package block, live-validation gap, shared-focus block, and ARX/HAW/FSM exclusions.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md` supplies the package contract for identity, territory, host interaction, leadership, forces, overlays, and cleanup.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md` supplies the sourced-male/institutional portrait rule and the no-custom-advisor-art rule.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_binding_audit.md` supplies the installed anchor, extension/compact set, host-capital, and reservation-group bindings.
- `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_07_26.md` reports zero reserved country-tag collisions, zero custom-cosmetic collisions, and the scanned installed-registry counts.
- The offline allocator check `python -B .tools/audit_event6_allocator.py` passed structurally with publishers 149, automatic/high-chaos selectable packages 126, SCN-008 ranked selectable packages 138, automatic counts 3/4/5/7/10, and World Collapse count 10. It does not replace engine execution validation.

## Ten attested package checklist

| Attestation / tag | Map binding and host | Static package coverage | Status | Remaining boundary or blocker |
| --- | --- | --- | --- | --- |
| `IW-001` / `SCO` Scotland | Anchor state 121; compact `121\|133`; extension `120\|136\|933`; host ENG capital 126; `RG-121-120-133` | Vanilla-tag carrier, state/history setup, ENG host survival, dynamic p1 territorial-army/coastal-defense force, five bespoke focuses, eleven projects/route actions, lifecycle ideas, AI, formable hooks, localisation, cleanup, and sourced male Cunninghame Graham/Fortune portraits | **PASS (static)** | Ordinary/compact/extended, joint, SCN-008, save/load, and live host-survival execution are not asserted here. |
| `IW-004` / `BRI` Brittany | Anchor/compact state 14; host FRA capital 16; `RG-14` | State and host setup, dynamic p4 coastal force tradition, five focuses, fourteen decision entries plus mission, lifecycle ideas, AI, formable hooks, flags, sourced portraits, localisation, and cleanup | **PASS (static)** | Live allocation and Event 005 collision execution remain untested. |
| `IW-006` / `AFX` Wallonia | Anchor/compact state 34; host BEL capital 6; `RG-34` | State and host setup, current p6 force value 61 from `common/script_constants/006_independence_wave_force_package_constants.txt:297`, eight focuses, ten decision entries plus mission, ideas, AI, `FORM-03`, sourced institutional Jules Destrée and Louis Hubert baron Ruquoy portraits, flags, localisation, and cleanup | **PASS (static)** | Historical handoff wording has older p6 values, but current runtime constant is 61. Live allocation and focus-engine validation remain untested. |
| `IW-007` / `AGX` Frisia | Anchor/compact state 36; host HOL capital 7; `RG-36` | Identity, state/host survival, Event 005 collision guard, dynamic p7 force, politics, eight-focus overlay, formable hooks, cleanup, AI, localisation, flags, and sourced male Douwe Kalma/Pieter Reenalda portraits are present | **PARTIAL** | `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:575-607` has a 300-day conference cancellation trigger that checks only package identity, stable waterline, and capital, so it can pay rewards after recognition/network/member/candidacy/authorization/client-route validity changes. Add cancellation/no-reward guards. The modifier reserves `civilian_factory_major = 3` while `custom_cost_text = independence_wave_cost_strategic` displays the standard two-factory cost. Custom trigger tooltips are incomplete. The shared focus tree is also parent-wide HOLD with fourteen blocking diagnostics after the `f8ca54d24` candidate reversion. Planning text says p7 44 while runtime constant is 45; this is documentation drift, not a static package blocker. |
| `IW-008` / `RHI` Rhineland | Anchor state 51; extension 42; host GER capital 64; `RG-RHINE-SAAR` | State/host setup, Event 005 collision protection, dynamic p8 force, six ideas, eight focuses, fourteen decisions/incidents plus mission, AI, `FORM-04`, sourced Wilhelm Marx/Gustav-Adolf von Zangen/Matthes portrait set, localisation, and cleanup | **PASS (static)** | Shares `RG-RHINE-SAAR` with AJX, so the pair contributes one selectable group for exact-ten capacity. Protected Matthes source remains untouched. Live execution remains untested. |
| `IW-009` / `BAY` Bavaria | Anchor/compact states `52\|53\|54`; host GER capital 64; `RG-52-53-54` | State/host setup, host-reunification safeguards, Event 005 collision guard, dynamic p9 force, eight focuses, ten projects plus mission, lifecycle ideas, AI, `FORM-04`, protected sourced Rupprecht/Heinrich Held/Friedrich Dollmann portraits, flags, localisation, and cleanup | **PASS (static)** | Shared focus geometry remains parent-wide HOLD. No package-specific static blocker was found. Tech Tree Viewer is not installed, so technology-tree claims remain unresolved where applicable. Live execution remains untested. |
| `IW-010` / `AJX` Saar | Anchor/compact state 42; host GER capital 64; `RG-RHINE-SAAR` | State/host setup, Event 005 collision protection, dynamic p10 force, focus/decision/mission/idea package, AI, `FORM-04`, sourced Walter Simons/Friedrich von Rabenau portraits, flags, localisation, and cleanup | **PASS (static)** | Shares `RG-RHINE-SAAR` with RHI and therefore does not create a tenth unique capacity group. Live execution remains untested. |
| `IW-017` / `COR` Corsica | Anchor/compact state 1; host FRA capital 16; `RG-1` | State/host setup, power-struggle package, dynamic p17 force, Landry civic leader, Chiappe emergency/security/corps commander, two portraitless advisors, focus/decision package, `FORM-05`, AI, flags, localisation, and cleanup | **PASS (static)** | No custom advisor art is used. Live allocation, temporary-rule lifecycle, and save/load execution remain untested. |
| `IW-019` / `ASX` Sicily | Anchor/compact state 115; host ITA capital 2; `RG-115` | State/host setup, dynamic p19 force, political and military roles, focus/decision/idea package, `FORM-05`, AI, flags, localisation, cleanup, and approved disclosure for fictional Sicilian Straits Security Directorate civic Rizzo plus sourced Di Benedetto corps commander | **PASS (static)** | No forbidden advisor/dossier/small/female portrait surface was found. Live allocation and role lifecycle remain untested. |
| `IW-184` / `HBX` California | Anchor/compact state 378; host USA capital 361; `RG-378` | State/host setup, dynamic p184 force with regular defectors/profile 3/reinforcement mask 590/inheritance 3, seven focuses, six decisions plus mission, ideas, AI, strict `FORM-48` route and SCN-008 hooks, fifteen-file HBX and PFX flag ladders, sourced William D. Stephens civic portrait, localisation, and cleanup | **PASS (static)** | `FORM-48` still depends on its full route and live prerequisites; no live allocation, formable execution, or save/load evidence is claimed. No custom advisor/dossier/operative/commander/small portrait surface was found. |

## Cross-package and admission findings

### Country identity, tags, map, and host safety

- The current ten attestation IDs and their package tags are exactly `SCO`, `BRI`, `AFX`, `AGX`, `RHI`, `BAY`, `AJX`, `COR`, `ASX`, and `HBX` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:55-68`.
- Current capacity branches in `common/scripted_triggers/006_independence_wave_triggers.txt` cover all ten package IDs with their installed anchors, tag availability, host/state clearance, Event 005 origin clearance, and reservation-group duplicate prevention.
- Installed map bindings are bounded and concrete: states 121, 14, 34, 36, 51, 52, 42, 1, 115, and 378 with host capitals 126, 16, 6, 7, 64, 64, 64, 16, 2, and 361 respectively. The extension/compact sets are limited to those in `package_bindings/006_current_installed_map_binding_audit.md`.
- The installed collision audit `006_installed_tag_collision_audit_2026_07_26.md` reports 102 reserved Event 006 tags, 16 custom cosmetic identifiers, 122 Workshop directories, four sibling local mods, zero reserved-tag collisions, zero custom-cosmetic collisions, and zero exact/state-normalized vanilla identity matches. Its sixteen fuzzy matches remain manual leads, not package blockers for these ten rows.
- The only intentional shared carrier among these ten is the RHI/AJX reservation group `RG-RHINE-SAAR`; it is correctly fail-closed by duplicate-group checks rather than treated as two independent groups.

### Portraits, leaders, flags, parties, and advisors

- Grounded packages use sourced real male or institutional archival portrait material. The reviewed ten packages satisfy that rule, with the approved disclosed fictional civic Rizzo exception in ASX and protected source identities retained for RHI Matthes and BAY Rupprecht.
- Generated one-person grounded approvals were not used as a substitute. ARX remains separately blocked on source-rights and Sardinian-role proof; no package in this ten-row audit inherits that unresolved source.
- The Event 006 asset policy intentionally defines no custom advisor, adviser, dossier, or `GFX_portrait_advisor_*` registration. The direct scan found only explicit comments documenting the absence of those surfaces, not forbidden custom advisor sprite definitions. Portraitless advisor records remain mechanics records and are not treated as missing art.
- No tag, party, cosmetic-name, flag, leader-id, or localisation collision was found in the ten static package surfaces reviewed. Runtime political popularity, law, faction, and cleanup behavior still require live execution evidence before full admission claims.

### Focus, decision, idea, and asset surfaces

- All ten packages have their package-specific focus/decision/idea hooks documented in the preceding table. The shared tree remains a separate parent-wide HOLD. The current source `common/national_focus/006_independence_wave_focus.txt` is the restored baseline after the rejected `f8ca54d24` candidate: 184 focuses, 223 connectors, 49 crossings, 18 node intersections, 27 long connectors, and fourteen blocking diagnostics. The authoritative reversion handoff is `006_shared_focus_geometry_reversion_2026_07_26.md`.
- AGX is the only ten-row package with a package-specific decision defect currently identified. Its conference recognition/client-route guard and cost-text mismatch require a local repair and follow-up decision audit.
- No custom Event 006 advisor art or unregistered country package icon was found. Existing country flags, focus icons, idea icons, and portrait references are present in the package handoffs; this audit did not create or reprocess assets.

### Starting military, technology, industry, supply, and production

- The package handoffs record dynamic force profiles, reinforcement paths, starting setup, industrial/host caps, and supply-safe anchor bindings for all ten rows. The source-level capacity branches and allocator audit confirm the intended 3/4/5/7/10 count ladder and anchor-to-compact-to-extension order.
- No country-specific hard blocker was found in the static force, industry, production, supply, or technology references for the ten rows. Technology-tree viewer validation is unavailable because the installed package exposes no Technology Tree Viewer; this remains an unresolved validation limitation, not evidence of a technology defect.
- Live stockpile, division-template, supply, production-line, fuel, convoy, and save/load behavior were not run and must not be described as accepted by this handoff.

### AI and playability

- Each ten-row package has a route-specific AI strategy/weight surface in its package handoff and current scripted package wiring. No missing AI reference or invalid tag was found statically.
- Static AI presence does not prove survival, front behavior, diplomacy, or route selection. These require live scenario execution after the shared focus and AGX decision blockers are resolved.

## Excluded or separately blocked packages

- `IW-018` / `ARX` Sardinia remains HOLD. `006_arx_roster_source_audit_2026_07_26.md` records the Sardinian crown council rights block for Eugenio di Savoia-Genova and a parent-review-only Vittorio Vernè candidate that still needs grounded visual provenance and Sardinian-role proof. No generated/name-only substitute is accepted.
- `IW-173` / `HAW` Hawaii remains runtime withdrawn because the Digital Archives source `ark:70111/47Nx` is all-rights-reserved and not production-safe for the required portrait.
- `IW-179` / `FSM` Federated States of Micronesia remains runtime withdrawn because no production-safe Henry Nanpei source was established: PN01036 is unavailable, HF01005 is unresolved thumbnail/reuse, and UHM “Mok” fails identity/era requirements.
- These exclusions are not missing ten-row package surfaces and do not alter the exact current attestation list.

## Validation and limitations

- Read-only source, registry, binding, tag-collision, portrait-policy, decision, focus-reversion, and handoff evidence was reviewed against the current repository tree.
- `python -B .tools/audit_event6_allocator.py` completed with the structural allocator pass reported above.
- The installed tag audit is evidence-backed and reports zero reserved/custom-cosmetic collisions. It does not prove gameplay execution.
- No Hearts of Iron IV process was launched. No save/load, live allocation, event option, decision timer, focus route, host survival, or SCN-008 execution was claimed.
- No Technology Tree Viewer is installed in the current MCP package, so technology-tree inspection remains unresolved.
- No map write, asset write, gameplay patch, or fallback was performed.

## Actionable parent handoff

1. Keep the ten current execution attestations and their fail-closed Event 005, host, state, tag, anchor, and reservation-group gates.
2. Repair and re-audit the AGX coastal conference cancellation/reward guards, strategic cost tooltip, and trigger tooltips in `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`.
3. Treat `RG-RHINE-SAAR` as one group for capacity until a tenth unique group is admitted or a reviewed map rebinding is applied.
4. Keep the shared focus tree in HOLD until a new coupled reflow passes authoritative focus inspect/render; do not revive the rejected `f8ca54d24` candidate.
5. Preserve ARX, HAW, and FSM fail-closed status until their source and rights blockers are independently resolved.
6. Run live allocation, host-survival, Event 005 collision, decision lifecycle, focus route, save/load, and SCN-008 scenarios before changing any static PASS to full runtime admission.

## Simplifications, omissions, and blockers

No simplification or fallback was introduced by this audit. The remaining blockers are the AGX decision defects, fourteen shared-focus geometry diagnostics, the nine-group exact-ten capacity boundary, unavailable technology-tree viewer, and the separately documented ARX/HAW/FSM source/runtime exclusions.
