# Event 006 IW-093 / IW-098 country-package readiness audit

Date: 2026-08-02.

Scope: bounded country-package audit for IW-093 Asante (`DOX`) and IW-098 Sokoto (`SOK`). This audit covers country registration, map binding, runtime setup, politics, leadership, focus, decisions, ideas, forces, technology inheritance, production, AI, formable linkage, central allocator admission, localisation, portraits, and flags. No gameplay, localisation, focus, decision, character, portrait, flag, or asset file was changed.

## Verdict

Both packages are structurally wired but neither is close enough to full static admission. Both remain intentionally fail-closed. The package-local setup and cleanup adapters are present, but the central allocator admission list, external content receipts, grounded identity and flag evidence, and FORM-24/FORM-25 family contracts are incomplete.

There is no safe package-local patch to apply in this audit. Setting either runtime attestation, adding a generic portrait or flag, or pretending that a registry family row is an executable formable adapter would weaken the fail-closed contract. The central allowlist and formable family work belong to their owning admission and formable surfaces.

| Surface | IW-093 Asante (`DOX`) | IW-098 Sokoto (`SOK`) |
| --- | --- | --- |
| Tag and origin | Structurally ready; new X tag is registered and exact `original_tag = DOX` gates are present. | Structurally ready; vanilla `SOK` is reused with exact not-living and `original_tag = SOK` gates. |
| Current-map anchor | State 274 is bound and guarded; Kumasi province semantics remain unresolved. | State 902 is bound and guarded; current-map rebound is documented. |
| Runtime country package | Setup, validation, cleanup, politics, values, ideas, focus, decisions, force, and AI surfaces are present. | Same surfaces are present, with Event 012 state-safety guards. |
| Leadership and portraits | Prempeh II source provenance exists but the treatment is not admitted; both commanders are invented/generated and blocked. | Dikko treatment/rights remain unresolved, Bello is invented/generated and blocked, Siddiq source is blocked, and Hasan is absent. |
| Flags | Base `DOX.tga` triplet exists but its period geometry/provenance is not admitted. | No mod `SOK` flag triplet; vanilla ideology triplets are not Event 006 period evidence. |
| Focus, decisions, ideas, AI | Static surfaces pass bounded review. | Static surfaces pass bounded review. |
| Formable | `west_african_federation` is selected, but FORM-24 has no family readiness, identity, X-tag, flag, territory, integration, or member-policy adapter. | `sahel_confederation` is selected, but FORM-25 has the same missing central adapter surfaces. |
| Central admission | Blocked: IW-093 is absent from the global content-attestation allowlist and has no external receipt. | Blocked: IW-098 is absent from the global content-attestation allowlist and has no external receipt. |

## Country package coverage checklist

- [x] DOX is registered at `common/country_tags/006_independence_wave_countries.txt:55` and points to `common/countries/006_independence_wave_DOX.txt`.
- [x] DOX has a dormant history shell at `history/countries/DOX - Asante.txt:1-10`; runtime Event 006 owns territory, capital, politics, leaders, forces, ideas, focus, and AI.
- [x] SOK remains the vanilla carrier at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:270`; the mod does not define a second SOK country file or history override.
- [x] Vanilla SOK starts with capital state 902, `infantry_weapons = 1`, and `SOK_siddiq_abubakar` in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/SOK - Sokoto.txt:1-10`.
- [x] Region-09 loaders publish IW-093 and IW-098 package IDs, reservation groups, region, depth, archetype, disposition, candidate tags, and anchors at `common/scripted_effects/006_independence_wave_packages_region_09_effects.txt:11-24,56-69`.
- [x] Region-09 planning gates require exact candidate/tag and anchor availability at `common/scripted_triggers/006_independence_wave_packages_region_09_triggers.txt:9-16,36-43`.
- [x] Exact origin and anchor proofs reject living countries, Soviet origins, duplicate Event 006 origins, wrong tags, and wrong states at `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:12-70`.
- [x] Shared dispatch invokes the package setup, final validation, and cleanup adapters at `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:24,42,58`.
- [x] The hidden character handoff recruits the exact package roster from `events/006_independence_wave.txt:283-303`; it is not an on-action or world-scan path.
- [x] English country, party, leader, commander, and adjective localisation is present at `localisation/english/006_independence_wave_countries_l_english.yml:615-630` and `localisation/english/006_independence_wave_iw093_iw098_country_core_l_english.yml:1-27`.
- [x] No advisor, high-command, dossier, or advisor-portrait surface is defined; this is an intentional package boundary, not an untracked missing advisor.

## File surface checklist

| Surface | Current evidence |
| --- | --- |
| Country shell/history | `common/countries/006_independence_wave_DOX.txt:1-11`; `history/countries/DOX - Asante.txt:1-10`; vanilla SOK files above. |
| Character roster | `common/characters/006_independence_wave_iw093_iw098_characters.txt:33-145` defines `DOX_prempeh_ii`, `DOX_kwame_frimpong`, `DOX_kwaku_ntim`, `SOK_muhammad_dikko`, and `SOK_bello_rabah`. |
| Portrait/GFX consumers | `interface/006_independence_wave_iw093_iw098_portraits.gfx:9-29` registers five large portrait consumers under `gfx/leaders/006_independence_wave/`. |
| Focus tree | `common/national_focus/006_independence_wave_focus.txt:24-74` defines `independence_wave_focus_tree` and imports the IW-093/IW-098 roots; `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` contains 43 focus IDs, including the two terminal formable preparation roots. |
| Focus assignment | `common/scripted_effects/006_independence_wave_focus_effects.txt:29-53` performs the guarded full-tree load; package-specific assignment is configured at `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:481-587`. |
| Decisions/categories | `common/decisions/006_independence_wave_iw093_iw098_decisions.txt` contains 18 package decisions and two categories; category definitions are at `common/decisions/categories/006_independence_wave_iw093_iw098_categories.txt:9-22`. |
| Decision effects | `common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.txt` owns paid transactions, timed project lifecycle, route receipts, project-to-idea swaps, and cleanup. |
| Ideas/icons | `common/ideas/006_independence_wave_iw093_iw098_ideas.txt:9-70` defines four staged ideas; their icons and localisation are registered in the matching interface/localisation surfaces. |
| AI | `common/ai_strategy/006_independence_wave_iw093_iw098_ai_strategy.txt:9-133` defines five DOX and five SOK strategy profiles using package constants. |
| Package API | `common/scripted_effects/006_independence_wave_packages_region_09_effects.txt`, `common/scripted_triggers/006_independence_wave_packages_region_09_triggers.txt`, `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`, and the paired package effects/triggers provide the package API and dispatch ownership. |
| Tag collections | `common/script_constants/006_independence_wave_country_registry_constants.txt:21-62,95-112,146-148` includes DOX in Event 006 owned/new, and SOK in registered-reuse, selectable-bound, Africa overlap, current-map-bound, and West/Central Africa collections. |

## Missing or stale country-package surfaces

### 1. Global allocator content attestation is missing for both package IDs

The adapter registry includes both package IDs at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-34`, but `has_independence_wave_runtime_package_content_attestation_for_execution_id` only lists the currently admitted IDs at `:72-89`; IW-093 and IW-098 are absent. `is_independence_wave_runtime_package_preflight_ready` requires both adapter and content attestation at `:94-99`, so neither package can enter the normal release preflight. Scenario preflight also requires the same helper at `:189-198`, even though the exact IW-093/IW-098 scenario rows are present at `:271-278`.

The planner repeats this central gate. Anchor reservation requires the helper in `common/scripted_effects/006_independence_wave_package_planner_effects.txt:95-107`, and candidate allocation weight is zero unless the helper passes at `:481-526`. Region-09 `can_plan_*` predicates therefore describe static candidate availability, not actual runtime admission.

### 2. Package-specific runtime receipts are intentionally unset

The package receipts are defined as external flags at `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:391-400`. No gameplay file sets `independence_wave_iw093_runtime_content_attested` or `independence_wave_iw098_runtime_content_attested`; setup and final validation require those flags at `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:593-605,649-661,714-780`. Cleanup only clears a future receipt at `:812,874`. This is the correct fail-closed behavior while source, flag, formable, and final country audits remain incomplete.

### 3. FORM-24 and FORM-25 are registry rows, not executable family adapters

DOX selects `west_african_federation` and SOK selects `sahel_confederation` at `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:506-526,562-582`. The profile loader has numeric registry profiles for both families at `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:357-379`, but the selected-family readiness dispatcher only has branches for existing FORM-01/02/03/04/05/07/39/48 families at `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt:74-108`.

The commit gate requires a family-specific readiness receipt and explicit adapter flags at `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:523-587`; its allowlist ends with FORM-18 and contains no FORM-24 or FORM-25 branch. Consequently, the packages have no admitted WFX/SFX identity adapter, unused X-tag reservation, exact flag package, territory/anchor contract, integration adapter, or member/consent policy. The FORM-24/25 focus and decision preparation surfaces must remain visible only as package goals and must not bypass the central formable gate.

### 4. Grounded leader and commander evidence is blocked

The current character definitions are all male and correctly pair male names with male metadata at `common/characters/006_independence_wave_iw093_iw098_characters.txt:33-145`. The portrait sprite registrations are structurally complete at `interface/006_independence_wave_iw093_iw098_portraits.gfx:9-29`, but the assets are not admission evidence.

The latest source handoff records the exact blockers in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw093_iw098_source_research_v50_2026_08_01.md:11-16,42-52`:

- Prempeh II has TNA/OGL provenance and an immutable crop, but the retained treatment is visually generic/younger and is not a likeness-preserving HOI4 portrait.
- `DOX_kwame_frimpong` and `DOX_kwaku_ntim` are invented identities with generated portraits; no face-visible, redistribution-clear 1935 Asante commander sources were admitted.
- Hasan dan Mu'azu Ahmadu has no cleared face-visible pre-cutover source.
- Siddiq Abubakar III has no cleared source; the vanilla generic portrait is not likeness evidence.
- Muhammadu Dikko has a retained 1921 reproduction and other review leads, but rights or identity-position and HOI4-treatment gates remain unresolved.
- `SOK_bello_rabah` remains fictional/generated with no grounded source.

The package must not substitute a generic, fallback, unnamed, or opposite-gender portrait. The hidden event currently recruits these exact consumers at `events/006_independence_wave.txt:283-303`, so the source gate is runtime-critical rather than documentation-only.

### 5. Exact period flag evidence is blocked

The mod contains only the base-size/medium/small `gfx/flags/DOX.tga` files. Their provenance and period geometry are not admitted by the latest source handoffs. The mod has no `gfx/flags/SOK*` files; vanilla provides SOK ideology triplets under the game installation, but those files do not establish an Event 006 period flag. The source disposition explicitly blocks both packages in `docs/plans/006_independence_wave_plans/asset_research/006_generated_flag_blockers.md:31` and the latest closure audit at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw093_iw098_country_package_closure_v92_2026_08_01.md:51-54`.

### 6. SOK pre-cutover leadership remains intentionally unavailable

The cutover is `date < 1938.06.17` versus post-cutover in `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:442-451`. `has_independence_wave_iw098_date_appropriate_leadership` explicitly requires post-cutover, the post-cutover Sultan flag, recruited `SOK_siddiq_abubakar`, and Siddiq as ruler at `:488-500`; the comment states that the pre-cutover Hasan branch is omitted until sourced and authored. The setup effect applies the same date-appropriate proof before politics, focus, force, and setup completion at `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:649-667`.

This is not a safe local simplification. Adding a generic Hasan or silently using Siddiq before the cutover would violate the accepted date-aware identity contract.

### 7. Kumasi province semantics are not proved by the current capital trigger

Vanilla state 274 contains Kumasi province `12787` and Accra province `10862` at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/274-British Africa.txt:18-24`. Setup stores `independence_wave_iw093_kumasi_victory_point = 12787` at `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:606-608` and clears it at `:814`, but `has_independence_wave_iw093_kumasi_capital_proof` only proves state 274 is owned, controlled, and capital at `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:402-409`. No capital effect or trigger consumes the province ID. This requires a shared map/capital owner review before admission.

SOK's state 902 contains the Sokoto victory point `1891` and core at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/902-Sokoto.txt:7-24`; the SOK proof correctly checks state 902 at `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:433-440`.

### 8. IW-098 registry baseline is stale after the current-map rebound

The authoritative candidate CSV still names provisional tag `DTX` and baseline state `558` for IW-098 at `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:99`. The installed binding and runtime loader use resolved tag `SOK` and current anchor state `902` at `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:99` and `common/scripted_effects/006_independence_wave_packages_region_09_effects.txt:56-68`. The installed binding records `rebound_to_current_split`, so this is a source-of-truth ledger drift that needs reconciliation before a final admission claim. It is not a reason to rebind runtime to state 558.

### 9. Older route wording is stale but gameplay identifiers are consistent

Some earlier package prose still says “federal route” or uses stale host-settlement wording. The implementation identifiers are the current ones: `constitutional_cabinet`, `iw098_court_civic_balance`, and `iw098_frontier_security`. The drift is recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw093_iw098_country_package_closure_v92_2026_08_01.md:63-64` and should be reconciled by documentation ownership rather than by changing route IDs.

## Map, state, and ownership findings

- DOX uses fixed anchor state 274, high-chaos-only disposition, and reservation group `RG-GHANA-ASANTE-FANTE`; SOK uses fixed anchor state 902, automatic-if-not-living disposition, and reservation group `RG-NIGERIA-COARSE`.
- The shared executor assigns each frozen anchor as the new capital before dispatch at `common/scripted_effects/006_independence_wave_execution_effects.txt:321-340`.
- Both fixed-anchor ownership proofs also require the released country to own and control the anchor; host-capital survival proofs require the former host to retain a capital at `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:56-70,411-440`.
- State 902 is a dedicated current-map Sokoto state and its installed binding is coherent.
- State 274 is a broad Ghana state with both Accra and Kumasi; the province-level capital semantic risk above remains unresolved.
- Read-only `hoi4.map_inspect` returned `SCAN_BYTE_LIMIT` in the prior closure audit, so the static vanilla state files are the available map evidence. No map write is warranted in this country-package scope.

## Politics, leaders, portraits, flags, advisors, and parties

- DOX initializes 20/5/70/5 democratic/communist/neutrality/fascist popularity and baseline civilian economy, export, and volunteer laws at `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:166-184` using constants at `common/script_constants/006_independence_wave_iw093_iw098_constants.txt:121-144`.
- SOK initializes 10/5/80/5 popularity and its four package party names at `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:186-204` using constants at `common/script_constants/006_independence_wave_iw093_iw098_constants.txt:146-159`.
- All six route politics rows are centralized and sum to 100 in `common/script_constants/006_independence_wave_iw093_iw098_constants.txt:162-202`.
- DOX `DOX_prempeh_ii` has male metadata and despotism/centrism country-leader roles at `common/characters/006_independence_wave_iw093_iw098_characters.txt:34-56`; the roster trigger requires him to rule at `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:466-472`.
- DOX commanders `DOX_kwame_frimpong` and `DOX_kwaku_ntim` are male corps commanders at `common/characters/006_independence_wave_iw093_iw098_characters.txt:58-100`; their corps roles are required at `:474-479`.
- SOK commanders `SOK_muhammad_dikko` and `SOK_bello_rabah` are male corps commanders at `common/characters/006_independence_wave_iw093_iw098_characters.txt:102-144`; their roles are required at `:481-486`.
- Post-cutover SOK reuses vanilla `SOK_siddiq_abubakar`, whose vanilla leader and generic portrait are defined at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/SOK.txt:4-19`; this is an engine-compatible reuse, not source admission.
- No opposite-gender portrait/name pairing or female metadata was found in the defined roster. The absence of advisors and institutional portraits is intentional and documented.
- The DOX base flag files are non-admitted; no mod SOK flag files exist. Do not copy vanilla SOK flags as a period-specific fallback.

## Focus, decision, idea, and asset findings

- The root `independence_wave_focus_tree` is explicitly imported and loaded only through the guarded full-framework assignment at `common/national_focus/006_independence_wave_focus.txt:24-39` and `common/scripted_effects/006_independence_wave_focus_effects.txt:29-53`.
- The package focus file has 43 focus IDs and package-specific prerequisites, mutual exclusions, bypasses, rewards, and AI weights. The two terminal formable preparation IDs are `independence_wave_iw093_prepare_form24_west_african_federation` and `independence_wave_iw098_prepare_form25_sahel_confederation`.
- The decision file has 18 package decision IDs and two category IDs. Timed projects include active, success, failure, cancellation, transaction, and cleanup receipts; no separate mission file is required by this package design.
- Four staged ideas have allowed scopes, package constants, lifecycle transitions, localisation, and registered icon consumers.
- The five portrait sprites are registered and the corresponding DDS files are physically present, but source handoffs classify the grounded consumers as non-admitted. Physical DDS presence must not be treated as visual admission.
- Focus, decision, idea, and icon surfaces are not the current blockers; the central formable, source, flag, and attestation gates are.

## Starting military, technology, industry, supply, and production findings

- DOX resolves force row `p93` to profile `river_jungle` and military tradition `64`; SOK resolves force row `p98` to profile `mounted_mobile` and military tradition `70` at `common/script_constants/006_independence_wave_force_package_constants.txt:384-389` and package setup `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:620-637,681-698`.
- Dynamic materialization requires active origin, profile, tradition, at least three reinforcement pathways, commander roster readiness, generation metadata, former-host and anchor targets, and current-generation protection at `common/scripted_triggers/006_independence_wave_force_triggers.txt:73-91`.
- The public force entry point inherits host technology and research slots, defines the profile template, creates opening divisions and stockpiles, transfers approved air/navy material, and records a generation receipt at `common/scripted_effects/006_independence_wave_force_effects.txt:869-889`.
- No package-specific free divisions or free equipment are added by the DOX/SOK focus or decision surfaces. Paid project costs and force tuning are centralized in package and force constants.
- DOX has no history production line and vanilla SOK begins with only `infantry_weapons = 1`. This is intentional host-inheritance design, but live playability remains dependent on a valid shared release host and the three-pathway force contract.

## AI and playability findings

- AI profiles cover foundation, severe-host-crisis restraint, and all three government routes for each country in `common/ai_strategy/006_independence_wave_iw093_iw098_ai_strategy.txt:9-133`.
- Package decisions own route-choice odds and transaction costs; AI strategy constants shape construction, infantry/support production, infrastructure, trains, bunkers, and war restraint without adding an unconditional world scan.
- The packages cannot currently be selected by the normal allocator because the global content-attestation helper is missing both IDs. This is an admission blocker, not an AI bug.
- Once admitted, playability still depends on the shared host-transfer and reinforcement-pathway contract; this cannot be validated by launching the game in this audit.

## Recommended one bounded next tranche

After the independent source/portrait/flag review is complete, run one parent-owned “IW-093/IW-098 admission-contract reconciliation” tranche with no fallback assets and no early attestation. The tranche should:

1. Reconcile IW-098's candidate-registry baseline field to the current SOK state-902 rebound while retaining the resolved `SOK` tag and runtime anchor 902.
2. Resolve the shared Kumasi province-versus-state capital proof with the map/capital owner, or explicitly record an accepted state-only interpretation in the source-of-truth documentation.
3. Implement and independently review the FORM-24/FORM-25 family adapters, including WFX/SFX identity and unused X-tag reservation, exact territory/anchor/member/consent policy, flag package, integration ownership, and cleanup receipts.
4. Only when the complete package and visual gates pass, add IW-093 and IW-098 to the central content-attestation allowlist and write their external runtime receipts in the same reviewed admission change, then rerun allocator, country-surface, formable, and map/static checks.

Do not set `independence_wave_iw093_runtime_content_attested` or `independence_wave_iw098_runtime_content_attested` before all four steps pass. Do not add a package-local duplicate of the central formable or allocator adapters.

## Validation evidence

- `python .tools/audit_event6_allocator.py` passed on 2026-08-02 with 149 publishers, 126 automatic/high-chaos selectable packages, 14 attested packages, and 13 compatible reservation groups. IW-093 and IW-098 remain outside the attested count as expected.
- Current static counts re-confirmed 43 package focus IDs, 18 package decision IDs, two decision categories, four staged ideas, and ten AI strategy profiles. The prior closure audit records zero missing focus localisation/sprite references, zero missing decision localisation/icon references, zero missing idea localisation/icon references, and zero unresolved package constant references.
- `python .tools/audit_hoi4_country_tags.py` was attempted read-only but exceeded the long workspace scan window without producing a report. The prior closure audit records the same limitation for the full country-surface scan.
- Read-only `hoi4.map_inspect` and `hoi4.focus_inspect` previously returned `SCAN_BYTE_LIMIT`; no MCP write tool was used.
- Hearts of Iron IV was not launched, and no live-save or in-game validation is claimed.

## Remaining setup or identity risks

- Neither package is runtime-admitted.
- Grounded leader/commander source and HOI4 treatment evidence remains blocked as listed above.
- Exact Asante and Sokoto flag evidence remains blocked.
- Pre-cutover SOK remains unavailable until a sourced Hasan character and portrait are authored and reviewed.
- FORM-24/FORM-25 central adapters remain absent.
- The Kumasi province semantic proof and IW-098 stale baseline ledger field remain unresolved.
- No simplification or fallback was introduced by this audit.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw093_iw098_package_readiness_audit_2026_08_02.md`.
