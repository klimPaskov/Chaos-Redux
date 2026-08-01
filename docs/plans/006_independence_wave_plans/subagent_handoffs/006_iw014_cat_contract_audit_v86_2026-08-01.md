# IW-014 Catalonia country-package contract audit v86 - 2026-08-01

## Disposition

IW-014 remains HOLD and is not content-attested or admitted. The CAT adapter is wired into the dormant Event 006 dispatch path, but its runtime and scenario preflights remain fail-closed. No release, promotion, or FORM-07 admission is recommended from this audit.

The narrow CAT cleanup defect was patched in `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt`. The cleanup now clears both `independence_wave_cat_compact_crisis_resolved` and `independence_wave_cat_compact_crisis_failed`, and the header now describes eleven concrete-cost projects instead of ten.

## Contract and identity coverage

| Surface | Evidence | Result |
| --- | --- | --- |
| Tag registration | Vanilla `common/country_tags/00_countries.txt:200` maps `CAT` to `countries/Catalonia.txt`; `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:8` requires `original_tag = CAT` and package `iw_014`. | Covered by reuse of the vanilla carrier. No duplicate CAT tag or country file is present in the adapter. |
| Vanilla history and capital | Vanilla `history/countries/CAT - Catalonia.txt:1` sets `capital = 165`; `history/states/165-Catalonia.txt:14-34` keeps `SPR` owner, CAT/SPR cores, Barcelona victory points, industry, airbase, and naval base. | Covered for the accepted compact anchor. Fresh-map ownership and post-release host survival still need runtime evidence. |
| Leader and portrait | Vanilla `common/characters/CAT.txt:4-15` defines `CAT_lluis_companys`, the sourced vanilla portrait, and liberalism leader metadata; CAT history recruits this character at `history/countries/CAT - Catalonia.txt:80`. | Preserved. Route effects promote the same `CAT_lluis_companys` character at `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:172-244`; no replacement portrait or generated leader was added. |
| Flag and country identity | `docs/events/006_independence_wave/catalonia_package.md:5,41` and the implementation handoff state that vanilla CAT history, flag, capital, Companys portrait, and carrier identity remain authoritative. | Covered at source level. No new flag, cosmetic tag, or identity fallback is allowed. |
| Package origin and lifecycle | `is_independence_wave_cat_package` and `can_initialize_independence_wave_iw_014_package` are in `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:8-32`; setup and cleanup are `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:305-420`. | Adapter path exists and is generation-scoped through shared Event 006 setup. Runtime execution is blocked by content attestation and FORM-07 readiness. |

## File-surface checklist

| Surface | Files and identifiers | Audit result |
| --- | --- | --- |
| Constants | `common/script_constants/006_independence_wave_catalonia_constants.txt` (`independence_wave_catalonia_pressure`, route popularity, AI priorities, 420-day founding crisis) | Present and CAT-specific. Values are centralized. |
| Ideas | `common/ideas/006_independence_wave_catalonia_ideas.txt` (`cat_contested_assembly`, `cat_industrial_compact`, `cat_constitutional_charter`, `cat_workers_board`, `cat_municipal_covenant`, `cat_security_command`, `cat_patron_trade_mission`) | Present, CAT-restricted, lifecycle-owned, and localized. Existing Event 006 idea pictures are reused. |
| Triggers | `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt` | Exact tag, anchor, host, route, ledger, force, AI, and array proofs are present. Triggers do not mutate country flags. |
| Effects | `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt` | Setup, politics, route governments, ledgers, focuses, validation, and cleanup are present. Cleanup patch is included in this audit. |
| Decisions and mission | `common/decisions/006_independence_wave_catalonia_decisions.txt:15-225` | One 420-day mission plus eleven concrete-cost project decisions are defined and localized. Cleanup removes all eleven decisions and the mission. |
| Focus ownership | `common/national_focus/006_independence_wave_focus.txt:75-82,3527-3614`; `common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-64` | CAT roots are imported, but setup requests `full_framework`. The shared additive-carrier trigger currently accepts only ICE (`iceland_tree`), so CAT has no source-approved additive carrier contract. |
| Dispatch | `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-60`; `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:33,183-184,280-281` | CAT setup, validation, cleanup, runtime wrapper, and scenario wrapper are registered. The exact content-attestation OR intentionally omits `iw_014`, so these paths stay dormant. |
| Regional allocator | `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt:18-24`; `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt:20-29,128-130,192` | CAT is bound to state 165 and RG-165 in the allocator. This is a dormant reservation surface, not an admission proof. |
| Localisation | `localisation/english/006_independence_wave_catalonia_l_english.yml` | CAT project, focus, idea, party, and tooltip keys are present. The file has a UTF-8 BOM. Vanilla CAT country and leader keys remain authoritative. |
| Assets | Existing Event 006 idea/focus sprites plus vanilla CAT flag and `GFX_portrait_CAT_lluis_companys` | No CAT-specific generated asset or `.gfx` registration was added. Asset provenance is acceptable for the reuse contract, but no independent Event 006 visual attestation exists yet. |
| Documentation | `docs/events/006_independence_wave/catalonia_package.md`; `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw014_cat_package_implementation_2026-08-01.md` | Implementation documentation exists, but its “additive overlay” wording conflicts with the `full_framework` assignment and requires parent design resolution. This audit handoff records the conflict without changing the design. |

## Map, states, host survival, and FORM-07

The CAT anchor is coherent in the current installed map binding: `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:15` records CAT state 165, RG-165, `165=SPR`, and `SPR=41`. The CAT allocator and package loader also reserve state 165 in `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt:18-24` and `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt:20-29,192`.

The FORM-07 family adapter is not ready. `common/scripted_triggers/006_independence_wave_form07_triggers.txt:3-5` hard-codes CAT/NAV/GLC anchors 165/172/171 and `:172-183` requires all three exact corridor members. `:190-221` also requires explicit identity, X-tag, and flag-package contract flags. None of those identity flags is set for the current CAT draft, and the NAV/IW-013 and GLC/IW-015 runtime package adapters are not complete.

There is a concrete binding mismatch that must be resolved by the parent package owner before any FORM-07 admission: the installed current-map binding records NAV's current compact anchor as state 792 and RG-172 in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:14`, while FORM-07 still uses `@FORM07_NAV_ANCHOR = 172` in `common/scripted_triggers/006_independence_wave_form07_triggers.txt:4` and `common/scripted_effects/006_independence_wave_form07_effects.txt:14`. The CAT adapter should not silently change either source; the corridor contract needs a coordinated map/spec decision.

The CAT host-survival proof is source-safe for the compact state because `can_initialize_independence_wave_iw_014_package` requires the former host to exist, retain the protected state, and leave CAT with capital state 165 (`common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:14-32`). It is not a substitute for fresh-map release/reload evidence.

## Politics, leader, party, and route coverage

`common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:145-158` initializes CAT politics and party names without replacing the vanilla country identity. The five route effects at `:163-250` use the existing Companys character and assign liberalism, socialism, oligarchism, despotism, or liberalism as route ideologies. The route trigger at `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:53-61` enforces one route-government state at a time.

The package registers the municipal-commission-versus-industrial-security power struggle and four host routes in `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:106-120`. It also preserves the vanilla non-Companys CAT leader records in the carrier history rather than inventing new leaders. No opposite-gender portrait/name pairing or institutional-body random-name pool is introduced.

## Focus, decision, idea, and mechanic coverage

CAT has six connected package focuses: `independence_wave_cat_secure_barcelona_port_focus`, `independence_wave_cat_integrate_factory_workers_focus`, `independence_wave_cat_reconcile_assembly_focus`, `independence_wave_cat_settle_iberian_charter_focus`, `independence_wave_cat_open_mediterranean_corridor_focus`, and `independence_wave_cat_ratify_catalan_sovereignty_focus` in `common/national_focus/006_independence_wave_focus.txt:3532-3614`. Their effects update the two CAT ledgers, host settlement, league/network state, and sovereignty flags.

The decisions file defines `independence_wave_cat_hold_industrial_compact_together` plus eleven project IDs from `independence_wave_cat_reopen_barcelona_depots` through `independence_wave_cat_open_mediterranean_network` (`common/decisions/006_independence_wave_catalonia_decisions.txt:15-225`). The cleanup removes all eleven project IDs at `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:376-387` and now clears both terminal crisis flags at `:396-397`.

The current contract is internally coherent only as a full Event 006 framework assignment. The CAT setup effect writes `independence_wave_focus_assignment_input = full_framework` at `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:316`, and the prepared trigger requires `independence_wave_full_focus_framework` plus the same assignment at `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:98`. That conflicts with the package documentation and focus-architecture requirement to preserve a meaningful vanilla carrier tree while adding an overlay. Because `can_attach_independence_wave_additive_focus_carrier` currently admits only ICE, this audit does not change CAT to a guessed additive mode and does not admit the full-framework path.

## Starting military, technology, industry, supply, and production

Vanilla CAT starts without an OOB (`#oob` is commented in `history/countries/CAT - Catalonia.txt:3`), has 20 convoys (`:31`), baseline infantry/support/mountaineer/truck/artillery/anti-air and generic 1939 technology (`:6-66`), and recruits Companys (`:80`). State 165 provides Barcelona industry, airbase, port, infrastructure, and coal in vanilla `history/states/165-Catalonia.txt:14-34`.

The CAT package maps to p14 regular defectors in `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:123-142`. The shared force constants give p14 profile 3 (`regular_defectors`), military tradition 72, reinforcement mask 589, and inheritance mask 3 (navy plus air) in `common/script_constants/006_independence_wave_force_package_constants.txt:91,305,519,733`. Mask 589 corresponds to the five required CAT pathways: integrate militias, secure depots, convert defectors, factory/rail guards, and professional officers.

The shared dynamic force entry point is called by CAT setup at `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:337-340` and implemented in `common/scripted_effects/006_independence_wave_force_effects.txt:871-889`. It inherits technology and research slots, creates dynamic divisions and stockpiles, and conditionally transfers approved former-host naval and air fractions. The transfer helper requires an armed-or-higher force level and a port-level check for navy (`common/scripted_effects/006_independence_wave_force_effects.txt:805-865`), so the p14 inheritance flags are capability declarations rather than proof that every calm or automatic scenario transfers ships and aircraft. Fresh-map force output, equipment, supply, and inheritance behavior remain unverified.

## AI, diplomacy, and playability

`common/ai_strategy/006_independence_wave_catalonia.txt` defines four CAT-specific layers: industrial survival, living-former-host restraint, settled industry, and emergency command. The decision blocks carry CAT-specific AI weights and cancellation checks. These are source-complete but cannot activate until `independence_wave_iw_014_setup_complete` is reached.

CAT's host, league, network, and formable fields are registered in the setup effect, but FORM-07 identity, member, and integration contracts are not attested. No diplomatic admission, autonomous-member relation, or Iberian federation transaction can execute through the current dispatcher. The bounded FORM-07 cleanup logic in `common/scripted_effects/006_independence_wave_form07_effects.txt:141-224` is generation-safe, but it is not evidence that CAT is ready to commit.

## Missing or stale surfaces and blockers

1. The implementation describes CAT as an additive vanilla-carrier overlay but requests `full_framework` and requires `independence_wave_full_focus_framework` (`common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:316`; `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:98`). The additive-carrier trigger only recognizes ICE (`common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-64`). Parent design must choose and fully wire a reviewed CAT carrier contract before admission.
2. `independence_wave_formable_family = iberian_federation` is selected, but `has_independence_wave_formable_commit_readiness = yes` is required at `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:121` and FORM-07 identity flags are not present (`common/scripted_triggers/006_independence_wave_form07_triggers.txt:190-221`). No X tag, flag triplet, or identity fallback may be invented in this audit.
3. FORM-07 requires the CAT/NAV/GLC all-three corridor, while NAV and GLC runtime package adapters are not complete (`common/scripted_triggers/006_independence_wave_form07_triggers.txt:169-183`; `docs/events/006_independence_wave/catalonia_package.md:7`).
4. FORM-07's NAV anchor 172 conflicts with the current installed NAV compact anchor 792 (`common/scripted_triggers/006_independence_wave_form07_triggers.txt:4`; `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:14`). Parent coordination is required before any corridor or map claim.
5. IW-014 is present in the dormant adapter and exact CAT wrapper but absent from the compile-time content-attestation OR (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:33,72-88,183-184,280-281`). This is the correct fail-closed behavior while blockers 1-4 remain.
6. Runtime/fresh-map evidence is still missing for Companys recruitment, dynamic force creation, conditional navy/air inheritance, host-target persistence, mission cancellation, all five route governments, and generation-safe cleanup. Source inspection cannot promote the package.

## Patch record

Changed file:

- `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt`

Before the patch, CAT cleanup removed the mission, eleven project decisions, ideas, ledgers, and most package flags but left `independence_wave_cat_compact_crisis_resolved` and `independence_wave_cat_compact_crisis_failed` set. After the patch, both terminal crisis flags are cleared alongside `independence_wave_cat_compact_stabilized` at lines 396-397. The adapter header now says eleven concrete-cost projects.

No tags, states, leaders, parties, focus IDs, localisation keys, formable IDs, or map bindings were changed.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 14 attested packages, and 13 compatible reservation groups.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan --workshop-root C:\__chaosx_missing_workshop_root__` passed with zero external country-definition collisions and zero external identity-surface collisions. The default workshop-root surface scan exceeded its 120-second timeout, so the narrowed scan intentionally excluded Workshop roots.
- `rg -n "set_country_flag =" common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt` returned no matches.
- A source check found twelve CAT decision blocks including the 420-day mission and eleven project decisions, and eleven cleanup removals. `localisation/english/006_independence_wave_catalonia_l_english.yml` begins with UTF-8 BOM.
- `git diff --check -- common/scripted_effects/006_independence_wave_catalonia_package_effects.txt` completed with only Git's normal LF/CRLF conversion warning.

Skipped meaningful validation: no HOI4 process was launched, no in-game release/reload was performed, and no runtime force or focus-render proof was claimed. The broad Workshop scan timed out and was replaced by the narrowed source/installed-game scan described above. No new plan handoff was written because the unresolved blockers require a parent-level contract decision rather than a safe local CAT patch.

## Parent action

Keep IW-014 outside exact content attestation. Resolve the additive-versus-full-focus ownership contract, complete or formally replace the FORM-07 Iberian family with an audited Mediterranean route, and reconcile NAV state 172 versus current anchor 792 before requesting a fresh CAT audit and runtime admission review.
