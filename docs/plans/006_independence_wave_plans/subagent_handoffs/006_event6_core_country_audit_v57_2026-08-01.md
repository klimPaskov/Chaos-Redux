# Event 006 core country-package audit v57

Date: 2026-08-01.

Scope: static country-package coverage and runtime-admission consistency for IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-017, IW-019, IW-173, IW-184, and the fail-closed IW-014 CAT carrier.

This audit is read-only for gameplay files. The only file added by this audit is this handoff.

## Decision

The Event 006 core package has a static content-admission PASS for exactly thirteen package IDs: IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-017, IW-019, IW-173, and IW-184.

The overall Event 006 runtime-readiness decision remains HOLD / PARTIAL because live allocation, release, state transfer, force materialization, focus visibility, AI timing, formable execution, cleanup, save/load, and SCN-008 transaction evidence are not present in this static audit.

IW-014 Catalonia remains HOLD and fail-closed. Its adapter, exact CAT/state-165 preflight branch, and setup/final-validation/cleanup dispatch wrappers are registered, but IW-014 is intentionally absent from the compile-time content-attestation trigger. CAT setup also requires `has_independence_wave_formable_commit_readiness = yes`; the Iberian/Mediterranean formable identity, territory, flag, and consenting-member adapter has not been independently accepted.

## Exact admission and map crosswalk

| Package | Carrier tag | Anchor / compact states | Former host | Reservation group | Static result |
| --- | --- | --- | --- | --- | --- |
| IW-001 | `SCO` | 121 / 121\|133 | ENG | `RG-121-120-133` | content-attested; runtime open |
| IW-002 | `WLS` | 122 / 122 | ENG | `RG-122` | content-attested; runtime open |
| IW-004 | `BRI` | 14 / 14 | FRA | `RG-14` | content-attested; runtime open |
| IW-006 | `AFX` | 34 / 34 | BEL | `RG-34` | content-attested; custom X history/flag present |
| IW-007 | `AGX` | 36 / 36 | HOL | `RG-36` | content-attested; custom X history/flag present |
| IW-008 | `RHI` | 51 / 51, optional 42 | GER | `RG-RHINE-SAAR` | content-attested; mutex with IW-010 required |
| IW-009 | `BAY` | 52 / 52\|53\|54 | GER | `RG-52-53-54` | content-attested; runtime open |
| IW-010 | `AJX` | 42 / 42 | GER | `RG-RHINE-SAAR` | content-attested; mutex with IW-008 required |
| IW-012 | `ICE` | 100 / 100 | ICE | `RG-100` | content-attested; self-host protection remains runtime-critical |
| IW-017 | `COR` | 1 / 1 | FRA | `RG-1` | content-attested; runtime open |
| IW-019 | `ASX` | 115 / 115 | ITA | `RG-115` | content-attested; custom X history/flag present |
| IW-173 | `HAW` | 629 / 629, optional 630\|631\|642\|727 | USA | `RG-629` | content-attested; runtime open |
| IW-184 | `HBX` | 378 / 378 | USA | `RG-378` | content-attested; custom X history/flag present |
| IW-014 | `CAT` | 165 / 165 | SPR | `RG-165` | HOLD; deliberately not content-attested |

The authoritative current binding rows are in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`. The CAT row is a static map reservation only and does not override the formable-readiness gate.

## Dispatcher and attestation consistency

The adapter OR block in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-34` includes IW-014 in addition to the broader registered package pool.

The content-attestation block in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:67-84` contains exactly the thirteen admitted IDs listed above and contains no `iw_014` branch.

`is_independence_wave_runtime_package_preflight_ready` requires both the adapter and content-attestation triggers before any exact package/tag branch can pass. Its CAT branch (`iw_014` -> `original_tag = CAT`) is therefore fail-closed while CAT remains unattested.

`is_independence_wave_scenario_package_preflight_ready` also requires the same content-attestation trigger before its exact package branch. CAT cannot enter scenario admission merely because its exact tag is available.

The central setup, final-validation, and cleanup effects call twelve regional wrappers, including `independence_wave_dispatch_catalonia_package_setup`, `independence_wave_dispatch_catalonia_package_final_validation`, and `independence_wave_dispatch_catalonia_package_cleanup` in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-61`. Wrapper registration is not admission evidence.

## Country-package coverage checklist

| Surface | Result | Evidence and remaining boundary |
| --- | --- | --- |
| Tag registry and origin separation | Covered statically | `common/country_tags/006_independence_wave_countries.txt`, `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`, `common/scripted_effects/006_independence_wave_country_registry_effects.txt`, and Event 006 preflight origin exclusions. No external definition or identity-surface collision was found. |
| History, capital, state ownership, cores, and host survival | Covered statically | Current map bindings provide anchors, compact/extension states, initial owners, capitals, and former-host implications for all thirteen admitted rows. Vanilla carriers retain vanilla history; custom X carriers have `AFX`, `AGX`, `AJX`, `ASX`, and `HBX` history/flag surfaces. Live release and host-remnant survival remain unproven. |
| Politics, laws, parties, leaders, portraits, flags, and advisors | Covered statically | Package effects, character files, sourced-portrait handoffs, vanilla-carrier preservation, party/localisation files, and lifecycle ideas are present for the admitted set. Portrait source, role, date, and gender reviews are recorded in package handoffs. No custom Event 006 advisor icon is currently required. |
| Focus trees and route loading | Covered statically | `common/national_focus/006_independence_wave_focus.txt` plus regional overlays and the package focus-assignment triggers provide the shared framework and route gates. MCP focus evidence records 184 nodes with icon, localisation, reward, and AI coverage; the 45 crossing/28 long-connector/7 through-node/5 spacing diagnostics are a parent-wide geometry risk, not a missing country-package surface. Live focus visibility remains open. |
| Decisions, missions, ideas, and lifecycle cleanup | Covered statically | Shared and regional decision/idea files, route locks, mission timers, project ledgers, and cleanup effects exist for the admitted packages. Live availability, costs, expiry, and cleanup/save-load behavior remain open. |
| Forces, technology, industry, supply, and production | Static mapping only | `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt` and `common/scripted_effects/006_independence_wave_force_package_effects.txt` provide package profiles, traditions, and reinforcement counts. No live army/navy/air materialization, stockpile, manpower, production, train, fuel, rail, port, or supply proof was available. The installed MCP has no Technology Tree Viewer, so technology placement and runtime unlock evidence remain unresolved. |
| AI, diplomacy, host ledgers, formables, and cleanup | Covered statically; runtime open | Regional AI strategy files and host/network/formable/cleanup hooks are present, including shared-carrier mutex logic for RHI/AJX and self-host protection for ICE. No live AI timing, diplomacy, formable transaction, annexation/puppet/return, or rollback proof was available. |
| Assets and localisation | Covered statically | Group `.gfx`/DDS/flag surfaces, source manifests, character consumers, focus/idea/decision icon references, and UTF-8-BOM English localisation are present for the admitted package groups. CAT deliberately reuses vanilla CAT flag and Companys portrait and adds no custom portrait or advisor asset. |

## Package file surface

The shared registry and execution contract is in `common/country_tags/006_independence_wave_countries.txt`, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`, `common/scripted_triggers/006_independence_wave_package_triggers.txt`, `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt`, `common/scripted_effects/006_independence_wave_force_package_effects.txt`, and `common/scripted_effects/006_independence_wave_execution_effects.txt`.

Regional package triggers/effects are present for IW-001/IW-002 (`006_independence_wave_scotland_wales_package_*`), IW-004 (`006_independence_wave_brittany_package_*`), IW-006/IW-007 (`006_independence_wave_wallonia_frisia_package_*`), IW-008/IW-009 (`006_independence_wave_rhineland_bavaria_package_*`), IW-010 (`006_independence_wave_saar_package_*`), IW-012 (`006_independence_wave_ice_package_*`), IW-017/IW-019 (`006_independence_wave_mediterranean_package_*`), and IW-173/IW-184 (`006_independence_wave_pacific_package_*`).

Shared and regional content is present in `common/national_focus/006_independence_wave_focus.txt`, `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`, `common/national_focus/006_independence_wave_pacific_focus.txt`, the `common/decisions/006_independence_wave_*` and `common/ideas/006_independence_wave_*` families, regional `common/ai_strategy/006_independence_wave_*.txt` files, package character files under `common/characters/`, interface `.gfx` files under `interface/`, and English localisation under `localisation/english/`.

The CAT draft surfaces are `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt`, `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt`, `common/decisions/006_independence_wave_catalonia_decisions.txt`, `common/ideas/006_independence_wave_catalonia_ideas.txt`, `common/ai_strategy/006_independence_wave_catalonia.txt`, `common/national_focus/006_independence_wave_focus.txt`, `localisation/english/006_independence_wave_catalonia_l_english.yml`, and `docs/events/006_independence_wave/catalonia_package.md`. These surfaces are implementation evidence only and do not authorize attestation.

## CAT fail-closed audit

`common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:14-30` requires the CAT carrier, IW-014 package identity, Mediterranean/Iberia regional profile, state 165 ownership/control, former-host target, capital state 165, and vanilla `CAT_lluis_companys`.

`has_prepared_independence_wave_iw_014_package_setup` at `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:76-145` requires the command roster, laws, full focus framework, five route flags, host routes, power-struggle and ambition registrations, league route, p14 force mapping and reinforcements, navy/air inheritance, AI profile, lifecycle ideas, and `has_independence_wave_formable_commit_readiness = yes`.

The formable readiness requirement is the intended hard blocker until the Iberian federation identity/flag/territory/consenting-member integration or an accepted Mediterranean-league carrier adapter is independently audited. No CAT attestation change is justified by this audit.

CAT cleanup is generation- and identity-gated in `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:373-417` and is designed to clear CAT package state without deleting vanilla history, flag, or Companys. That cleanup remains static-only until a live transaction is tested.

## Missing, stale, or unresolved surfaces

No new static country-package defect was found in the thirteen admitted packages. The current documentation authority records the exact 13-package / 12-group / 13-anchor count and keeps CAT as a separate draft/HOLD; use `docs/plans/006_independence_wave_plans/subagent_handoffs/006_documentation_curator_iw014_admission_boundary_2026-08-01.md` and `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` instead of dated pre-implementation CAT wording.

The preserved pre-implementation CAT audit necessarily says that the adapter was missing at its audit date. That historical document is not current implementation coverage authority, and it must not be read as an attestation.

Some older Pacific and package resume documents contain dated admitted/withdrawn wording. The documentation-curator handoff reconciles the current source-of-truth surfaces; these are documentation risks, not gameplay admission evidence.

## Validation

Meaningful static checks completed:

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable packages, 13 attested packages, 12 compatible reservation groups, and automatic ladder counts 6/8/10/14/20.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` passed with 136 protected Event 006/Soviet tags, zero external country-definition collisions, zero external identity-surface collisions, and one intentionally skipped Random Events root.
- Direct source comparison found 13 exact admitted package IDs and 13 exact admitted ID/tag branches, with CAT adapter registration present and CAT content attestation absent.
- The shared setup/final-validation/cleanup dispatch contains all twelve regional wrappers, including CAT, and a 31-path core-surface inventory resolved without missing files.
- The installed map-binding CSV contains all thirteen admitted rows plus the reserved CAT row for state 165.

Skipped meaningful validation: no Hearts of Iron IV process, fresh-map release, save, or live scenario was launched; no live allocator, release, force, focus, AI, formable, cleanup, or rollback test was run; and no Technology Tree Viewer is installed. These are parent-owned runtime gates, not static PASS evidence.

## Changed files and handoff

Changed file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_core_country_audit_v57_2026-08-01.md` only.

No country tag, country definition, history, state, leader, portrait, flag, idea, focus, decision, AI, formable, or gameplay script was patched by this audit. No fallback or simplification was introduced.

Parent action: retain the thirteen-ID attestation exactly, retain CAT adapter and dispatcher registration without adding CAT to attestation, and independently implement/audit the Iberian/Mediterranean formable adapter before revisiting IW-014 admission.

