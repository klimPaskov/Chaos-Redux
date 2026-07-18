# Event 006 IW-093 / IW-098 country-package readiness audit

Date: 2026-07-18
Mode: read-only source audit; this handoff is the only file created.
Packages: IW-093 / Asante and IW-098 / Sokoto
Scope: tag identity, installed-map binding, Event 005/006 compatibility,
runtime admission, country setup, leaders and portraits, flags, politics,
focus/decision/idea surfaces, military/technology/industry, AI,
localisation, assets, and FORM-24/FORM-25 linkage.

## Executive verdict

Both packages must remain fail-closed. Neither is a complete Event 006
country package in the checked-in source.

| Package | Resolved identity and map proof | Static pool disposition | Current runtime verdict |
| --- | --- | --- | --- |
| IW-093 Asante | `DOX` (new Event 006 `X` tag), state `274`, Kumasi VP `12787`, host `ENG` | `high_chaos_only`; reservation group `RG-GHANA-ASANTE-FANTE` | **NOT READY**. Region-09 load/weight/reserve publishers exist, but no exact tag wrapper, runtime attestation, setup, final-validation, cleanup, focus, AI, leader, force, idea, or politics adapter exists. |
| IW-098 Sokoto | `SOK` (reused vanilla identity), state `902`, Sokoto VP `1891`, host `ENG` | `automatic_pool_ready_if_not_living`; reservation group `RG-NIGERIA-COARSE` | **NOT READY**. Vanilla identity/history must remain additive; no Event 006 adapter or exact preflight exists, and the shared legacy content-ready gate has zero grants. |

The static rows do not authorize release. `common/scripted_effects/006_independence_wave_effects.txt` initializes setup/final-validation success to `no_candidates`, dispatches the central package adapters, and resets the generation when no adapter succeeds. The central dispatch file has no IW-093/IW-098 branches. A package selected by a static region registry therefore cannot commit ownership or country state.

No gameplay, localisation, focus, decision, map, asset, or spreadsheet files
were edited by this audit. No fallback or substitute package was introduced.

## Source and precedent basis

The audit followed `AGENTS.md` and the repository skills
`chaos-redux-subagents`, `chaos-redux-events`, `hoi4-focus-trees`,
`hoi4-decisions-missions`, `chaos-redux-event-assets`, and
`chaos-redux-improvement-loop`. The required offline Paradox wiki pages were
consulted (data structures, triggers, effects, modifiers, localisation,
scopes, on actions, event, decision, idea, AI, country, focus, state, and
portrait references). Vanilla documentation consulted included
`documentation/effects_documentation.md`, `triggers_documentation.md`,
`modifiers_documentation.md`, `script_concept_documentation.md`,
`loc_objects_documentation.md`, and `dynamic_variables_documentation.md`.
Vanilla country/state/history/character/focus/localisation files were checked
directly. HOI4 MCP domain tools were not exposed in this session, so this is a
source-level audit rather than an MCP render or runtime result.

Primary Chaos Redux evidence:

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:94,99`
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:94,99`
- `docs/specs/006_independence_wave_specs/research/006_signature_country_research_dossiers.md`
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:94,99`
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_state_collisions.csv:12`
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv:80,98`
- `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_07_18.json`
- `common/scripted_triggers/006_independence_wave_packages_region_09_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_09_effects.txt`
- `common/scripted_triggers/006_independence_wave_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`
- `common/scripted_effects/006_independence_wave_scenario_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`

## Identity, registration, and collision checklist

### IW-093 / Asante / DOX

- Registry row 94 resolves `DOX`, `reserve_new_event6_X_tag`, high-chaos only,
  state 274, Kumasi-required capital, and reservation group
  `RG-GHANA-ASANTE-FANTE`.
- `common/country_tags/006_independence_wave_countries.txt:55` registers
  `DOX = "countries/006_independence_wave_DOX.txt"` for IW-093. The shell
  uses African graphical cultures and a map colour only.
- `history/countries/DOX - Event 006 Country Shell.txt` is intentionally
  dormant and has no fixed country setup. No vanilla Asante country identity
  was found, so a new Event 006 `X` tag is the correct identity policy.
- The installed tag audit reports `collisions: []`; `DOX` is in the Event 006
  owned identifier set and no external country definition collides with it.

### IW-098 / Sokoto / SOK

- Registry row 99 initially has a provisional `DTX`, but the accepted research
  resolution overrides it to `SOK`, `reuse_registered_tag`, automatic only when
  the tag is not living, state 558 host direction with current anchor state
  902, and reservation group `RG-NIGERIA-COARSE`.
- Vanilla `common/country_tags/00_countries.txt` registers
  `SOK = "countries/Sokoto.txt"`; Chaos Redux correctly does not register a
  second SOK country shell.
- The installed audit manually reviews IW-100 `DVX` as a broader Hausa federal
  route, distinct from the Sokoto identity. Do not collapse IW-100 into SOK or
  overwrite a living SOK country.

## Map, state, host, and Event 005 compatibility

- Current installed binding row 94 binds IW-093 to state 274 (`274=ENG`,
  `ENG=126`), with Kumasi VP `12787` in that state. The binding explicitly
  requires Kumasi as the capital location and says the host retains at least
  one 1936 state after compact transfer.
- Current installed binding row 99 binds IW-098 to dedicated state 902
  (`902=ENG`, `ENG=126`), with Sokoto VP `1891`; the installed SOK core includes
  state 902. The binding explicitly requires Sokoto as the capital location
  and the host protected-state test.
- `RG-GHANA-ASANTE-FANTE` permits at most one automatic package on coarse
  state 274. IW-093 is the high-chaos automatic claimant; IW-094 Fante is
  unbound, so no second Ghana release may be inferred.
- `RG-NIGERIA-COARSE` permits at most one automatic package from its coarse
  group. The state-collision row for state 902 lists `IW-098|IW-100`; IW-098
  has reservation priority and IW-100 is route/formable-only. Optional claims
  must be trimmed before anchor transfer.
- The shared planner in
  `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
  enforces N-1 host capacity and a protected remnant. Event 005/006 shared
  transaction and reservation gates remain the required collision barrier;
  no direct IW-093/IW-098 Event 005 collision was found. Static binding is not
  a runtime proof until a package adapter invokes the shared reservation and
  final-validation APIs.

## Admission and runtime surface findings

1. `common/scripted_triggers/006_independence_wave_packages_region_09_triggers.txt:9-15`
   and `:36-42` expose planning predicates for DOX/state 274 and SOK/state
   902. Both call the generic `is_independence_wave_candidate_tag_available`.
2. `common/scripted_triggers/006_independence_wave_package_triggers.txt:23-45`
   requires `exists = no`, reservation/origin exclusions, and
   `has_country_flag = independence_wave_package_content_ready`. No source
   sets that flag for IW-093 or IW-098; the installed audit records
   `legacy_content_ready_grant_count: 0`. Thus the region-09 candidates do not
   become content-ready merely because their rows have map bindings.
3. There is no
   `is_independence_wave_exact_package_iw_093_tag_available`,
   `is_independence_wave_exact_package_iw_098_tag_available`, or corresponding
   ready wrapper in `006_independence_wave_package_triggers.txt`.
4. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`
   attests only IW-001, 002, 004, 006, 007, 008, 009, 010, 017, 018, 019,
   043, 058, 173, 179, and 184. IW-093 and IW-098 are absent from the runtime
   adapter, content-attestation, normal preflight, and SCN-008 exact-preflight
   ORs.
5. `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`
   dispatches setup, final validation, and cleanup only for the already
   attested package families. It has no region-09/IW-093/IW-098 calls.
6. `common/scripted_effects/006_independence_wave_scenario_effects.txt:163,295`
   places both IDs in the ranked SCN-008 registry, and its dynamic loader can
   call the region-09 load/reserve publishers. However,
   `independence_wave_scenario_attempt_ranked_packages` calls the shared exact
   preflight first; absent attestation branches record
   `liberation_plan_reject_reason.package_unready` and do not reserve them.

**Result:** static rank/load/reserve rows are present, but normal and scenario
execution are fail-closed before country setup. No ownership, capital, party,
leader, army, idea, focus, AI, or cleanup behavior can be claimed as live.

## Country-package coverage checklist

| Surface | IW-093 / DOX | IW-098 / SOK |
| --- | --- | --- |
| Tag/country definition | DOX shell exists; registration and X-suffix policy pass. | Vanilla SOK definition exists; no duplicate Chaos Redux shell, as required. |
| Country history/start setup | Dormant shell only; runtime setup is missing. | Vanilla history only; no Event 006 additive setup adapter. |
| State ownership/cores/capital | Binding proves state 274/Kumasi direction; runtime transfer/capital assignment missing. | Vanilla state 902 is ENG-owned with NGA/SOK cores and Sokoto VP; runtime transfer/capital assignment missing. |
| Leader/character | No Event 006 character or leader. Prempeh II is the researched period anchor, but not wired. | Vanilla `SOK_siddiq_abubakar` exists. Research requires Hasan dan Mu'azu Ahmadu before 17 June 1938 and Siddiq after; no Event 006 date-aware selector exists. |
| Portrait | No DOX portrait or `.gfx` registration. Prempeh II source is cleared as a candidate, not yet copied/wired. | Vanilla male `GFX_portrait_SOK_siddiq_abubakar` is available. Hasan source is cleared as a candidate; external Siddiq source remains blocked, but no custom Event 006 portrait is needed if the installed vanilla portrait is reused. |
| Flag | No Event 006 DOX flag triplet or route registration. Asante symbol/flag research remains blocked pending identity ownership and provenance. | No Event 006 SOK flag triplet. Modern Sokoto State art, generic jihad banners, and unverified sacred text are explicitly prohibited. |
| Politics/parties/laws | No DOX party names, ruling party, stability/war-support setup, laws, or diplomatic opening. | Vanilla neutrality 75%, no election, and vanilla party names exist; no additive Event 006 politics, route flags, or date-aware replacement. |
| Ideas/national spirits | Only shared generic Event 006 lifecycle ideas exist; no Asante-specific starting idea lifecycle. | Same: no Event 006 Sokoto lifecycle; Event 012 `africa_priority_*` ideas are a separate promotion system and cannot substitute. |
| Focus loading | No package assignment or DOX-specific route. Shared tree requires an explicit assignment and full-framework flag. | Vanilla SOK has a meaningful vanilla/generic tree surface; never blind-load `independence_wave_focus_tree`. Event 012 overlay loading is separate and gated by `africa_priority_member_focus_tree_loaded`. |
| Decisions/missions | No IW-093 Event 006 decisions/missions/categories. | No IW-098 Event 006 decisions/missions/categories. Event 012 decisions are separate. |
| Army/units/technology/industry/supply | No starting divisions, templates, stockpile, manpower, technology, production, convoy, fuel, or supply setup. | Vanilla only has infantry weapons level 1 and no package-specific force/industry setup; no Event 006 additive military adapter. |
| AI | No IW-093/DOX Event 006 AI strategy file or package-specific weights. | No IW-098/SOK Event 006 AI strategy file or package-specific weights. |
| Localisation | Country and ideology keys `DOX`, `DOX_DEF`, `DOX_ADJ`, and ideology variants exist in `006_independence_wave_countries_l_english.yml:615-630`. No leader, focus, decision, idea, or route strings are wired. | Vanilla SOK names/ideology keys exist in `countries_l_english.yml:4596-4610`; no Event 006 package-specific leader/focus/decision/idea strings. |
| Cleanup | No IW-093 cleanup adapter in central dispatch. | No IW-098 cleanup adapter in central dispatch. |

The Event 012 files (`common/national_focus/012_africa_priority_member_focus.txt`,
`common/scripted_effects/012_africa_priority_member_effects.txt`,
`common/ideas/012_africa_priority_member_ideas.txt`, and
`common/decisions/012_africa_priority_member_decisions.txt`) contain Asante and
Sokoto promotion content, but that system uses its own package variables,
flags, institutional councils, and focus tree. It is not an Event 006 release
adapter and must not be used to imply IW-093/IW-098 readiness.

## Focus, decisions, formables, and route compatibility

- `common/scripted_effects/006_independence_wave_focus_effects.txt:28-56`
  deliberately loads the full Event 006 tree only for an explicit full-framework
  assignment; additive modes do not call `load_focus_tree`. No IW-093/IW-098
  assignment publisher exists.
- `common/national_focus/006_independence_wave_focus.txt` is a shared framework,
  not a country-specific Asante or Sokoto tree. A future DOX package may use the
  full framework only after a reviewed assignment; a future SOK package must
  use an additive overlay unless a deliberate tree review proves its vanilla
  tree is generic and safe to replace.
- FORM-24 West African Federation and FORM-25 Sahel Confederation are present
  in `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv:25-26`,
  `common/script_constants/006_independence_wave_formable_constants.txt:41-42,326-327`,
  generic profile loading (`common/scripted_effects/006_independence_wave_formable_registry_effects.txt`),
  and localisation. However, `is_valid_independence_wave_formable_founding_carrier`
  in `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`
  has carrier branches only for FORM-01 through FORM-05, FORM-48, FORM-12,
  FORM-13, and FORM-18. No FORM-24/25 carrier/member/commit branch and no direct
  DOX/SOK package reference was found. FORM-24/25 linkage is design registry
  coverage, not executable package readiness.
- Any future new formable or route tag for FORM-24/25 must end in `X`; SOK
  reuse remains the identity carrier and DVX remains a distinct Hausa route.

## Asset and identity provenance blockers

- `docs/plans/006_independence_wave_plans/asset_research/006_real_portrait_and_symbol_sources.md:35`
  clears a Prempeh II 1935 National Archives/OGL candidate for IW-093; this is
  a source handoff, not an installed portrait or `.gfx` registration.
- The same source file at `:37` clears Hasan dan Mu'azu Ahmadu for IW-098
  before the 17 June 1938 succession boundary. At `:51`, the Smithsonian/
  Commons rights conflict blocks copying Siddiq Abubakar III from that external
  source. Existing vanilla SOK portrait reuse remains the only currently
  available visible male portrait path.
- `docs/plans/006_independence_wave_plans/asset_research/006_package_asset_coverage.md:152-155`
  and `006_generated_flag_blockers.md:31-33,82` keep Asante and Sokoto flag
  work blocked pending exact institutional ownership and provenance.
- No Event 006 DOX/SOK leader, country flag, idea, focus, or decision sprite
  registration was found. There are no custom Event 006 advisor icons/assets;
  this constraint must remain unchanged. Institutional/council portraits from
  Event 012 are not Event 006 advisor substitutes.

## Recommended implementation order

1. Complete the country-specific package design and asset attestations first;
   do not grant `independence_wave_package_content_ready` as a shortcut.
2. Add exact immutable DOX/SOK availability wrappers, runtime content
   attestation, and SCN-008 preflight branches only after the full package
   audit passes.
3. Add region-09 setup/final-validation/cleanup adapters that call the shared
   release transaction, map anchor/host checks, and rollback/reset contracts.
4. Build DOX runtime setup around the researched Prempeh II/Asante authority
   package. Build SOK as a guarded additive route preserving vanilla identity,
   with the Hasan/Siddiq date boundary and no blind history/tree overwrite.
5. Add country-specific politics, ideas, leader/portrait wiring, military and
   technology/industry setup, focus assignment, decisions, AI weights,
   localisation, flags, and cleanup. Keep advisors asset-neutral.
6. Implement FORM-24/FORM-25 carrier/member/commit eligibility and route flags
   as a separate audited tranche; then rerun tag collision, map binding,
   Event 005/006 transaction, asset, scenario, focus, localisation, and
   country-package audits.

## Validation and skipped meaningful checks

Completed source checks:

- Exact registry/research/map rows inspected for both packages.
- Installed tag collision JSON reviewed: 102 Event 006 country tags, 108 owned
  identifiers, 122 Workshop roots plus three sibling local mods, and
  `collisions: []`.
- Vanilla SOK tag, shell, history, state 902, character, portrait reference,
  generic-focus usage, and localisation inspected. Vanilla state 274 and
  Kumasi VP/state localisation inspected.
- Region-09 planner, scenario rank/loader, shared candidate gate, central
  dispatch, focus assignment, formable registry, Event 005/006 transaction,
  asset research, and Event 012 separation surfaces inspected.
- Repository searches confirmed no IW-093/IW-098 setup/final-validation/
  cleanup adapter, exact dispatch wrapper, Event 006 AI file, package-specific
  idea/decision/focus/leader/flag asset, or FORM-24/25 carrier branch.

Skipped: no game session/save, no HOI4 MCP render/rewrite, no map mutation, no
Technology Tree Viewer (the installed package exposes none), and no live
portrait/flag visual review. These omissions prevent a runtime or visual
pass claim; they do not change the fail-closed verdict.

## Simplifications, omissions, and blockers

No simplification was introduced by this audit. The packages themselves remain
incomplete: runtime adapters, country setup, politics, leaders, military,
focus/decision/idea/AI surfaces, flags, exact localisation, cleanup, and
FORM-24/25 route linkage are still missing. The parent should not promote
either package until those surfaces are implemented and independently audited.
