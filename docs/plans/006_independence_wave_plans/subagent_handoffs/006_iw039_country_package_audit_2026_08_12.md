# IW-039 Cossack Don country-package audit - 2026-08-12

## Disposition

**FAIL-CLOSED / PREFLIGHT ONLY.** IW-039 is not implementable or promotable on the current filesystem. This audit intentionally makes no gameplay, asset, dispatcher, attestation, preflight, or Join changes. The central Event 006 lists remain unchanged.

The existing preflight handoffs remain authoritative and are superseded only by the additional current-worktree checks in this document:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw039_preflight_2026_08_10.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw039_probability_preflight_2026_08_10.md`

IW-040's 2026-08-12 promotion does not establish IW-039 readiness. IW-040 is a different vanilla carrier, anchor, leader/asset contract, and package implementation.

## Country package coverage checklist

| Surface | Current evidence | Disposition |
| --- | --- | --- |
| Candidate identity | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:40` names `IW-039,Cossack Don,...,DON,reuse_registered_tag,...,245|238,...,RG-DON-KUBAN`. | Static registry row only. Preserve vanilla `DON`; do not create a replacement tag. |
| Vanilla country definition | Vanilla `common/countries/Don Republic.txt` provides eastern European graphical cultures and orange `rgb { 255 170 0 }`. | Available as an additive carrier, not an Event 006 package. |
| Vanilla country history | Vanilla `history/countries/DON - Don Republic.txt` uses capital state `218`, two research slots, standard starting technology, neutrality elections, and `recruit_character = DON_vladimir_sidorin`. | Must remain untouched outside an origin-gated adapter. |
| Vanilla character | Vanilla `common/characters/DON.txt` defines `DON_vladimir_sidorin` as despotism/fascism country leader with `cossack_ataman`, plus cavalry/ranger field-marshal traits. | Existing identity can be considered only after package-role and portrait provenance review. No invented replacement. |
| Vanilla OOB | Vanilla `history/units/DON_cossack_host.txt` defines one eight-cavalry-regiment template and fifteen cavalry divisions at provinces including 9417. | No accepted Event 006 conversion, reinforcement, or compact-start policy. |
| Runtime adapter | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` has no `iw_039` or `DON` adapter entry. | Hard blocker. |
| Content attestation | The same dispatch trigger file has no `iw_039` attestation entry. | Hard blocker. |
| Setup/final validation/cleanup | `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` dispatches IW-040 at lines 38, 68, and 112, but no IW-039 setup, final-validation, or cleanup effect. | Hard blocker. |
| Join | `common/scripted_effects/006_independence_wave_join_effects.txt:238` probes IW-040; no IW-039 probe exists in the current Join chain. | Must not widen Join order before package gates pass. |
| Event 006 country content | No IW-039 country-specific Event 006 effects, triggers, decisions, missions, ideas, AI, character consumer, or localisation file exists. | Missing package surfaces. |
| Shared focus assignment | The shared tree has no DON-specific adapter or hook. | Missing package assignment and reward audit. |
| Map binding | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:40` binds `DON` to `245|238` (Millerovo and Volgodonsk), with SOV host-remnant `219`. | Candidate binding, not an accepted runtime contract. |
| Reservation group | `RG-DON-KUBAN` is shared by IW-039 and IW-040 in `006_current_map_reservation_groups.csv:75`. | Requires mutual exclusion and host protection. |
| Scenario rank | `common/scripted_effects/006_independence_wave_scenario_effects.txt:234` ranks `iw_039`. | Static ranking membership does not prove executable content. |
| FORM-11 | Registry metadata references `BMX` as a provisional identity, but no IW-039 runtime carrier, consent, state puzzle, or explicit exclusion handoff exists. | Must be implemented or explicitly excluded before admission. |

## File surface checklist

### Present static shells

- `common/script_constants/006_independence_wave_package_constants.txt` declares the package ID `iw_039`.
- `common/scripted_triggers/006_independence_wave_packages_region_04_triggers.txt:52-59` declares `can_plan_independence_wave_package_iw_039`.
- `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt:74-84` declares `independence_wave_load_package_iw_039`.
- `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt:125-159` prepares and reserves the Region-04 IW-039 weight and compact.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt:234` inserts the package into the scenario-ranked array.
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:40` records the research-row identity.
- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:40` records `mounted_mobile`, tradition `82`, no navy, and no air.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:40` records anchor `245|238`.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv:75` records shared group `RG-DON-KUBAN`.

### Missing or stale package surfaces

- No `common/scripted_triggers/006_independence_wave_don_package_triggers.txt` exists.
- No `common/scripted_effects/006_independence_wave_don_package_effects.txt` exists.
- No IW-039 constants, ideas, decision category, decisions, missions, or AI strategy file exists.
- No Event 006 character consumer, leader role, advisor/high-command surface, portrait `.gfx`, or portrait manifest exists.
- No IW-039 Event 006 localisation exists for country names, route governments, leaders, ideas, decisions, missions, focus hooks, or tooltips.
- No IW-039 flag package, alternate-route ladder, source review, rights record, or strict asset QA manifest exists.
- No central package adapter, attestation, setup, final-validation, cleanup, normal-preflight, scenario-preflight, or Join entry exists.

## Map and state setup issues

### Vanilla state facts

- Vanilla state `218-Rostov Area.txt` is owned and cored by `SOV`, has victory point province `9417` worth 15, infrastructure 3, one arms factory, one industrial complex, air base 3, naval base 5, and 1,501,076 manpower.
- Vanilla state `238-volgodonsk.txt` is owned and cored by `SOV`, has infrastructure 2, victory point province `775` worth 1, and source manpower `556677`.
- Vanilla state `245-Donetsk.txt` is owned and cored by `SOV`, has infrastructure 3, victory point province `11476` worth 1, and source manpower `761769`.

The installed-map binding deliberately selects `245|238`, not the vanilla DON capital `218`. The planner source currently captures the host from state 245 and treats state 238 as the compact addition. This is not safe to execute until the package contract explicitly resolves whether Event 006 uses a non-capital compact release or changes capital after release.

### DON/DHC collision

The collision is a release blocker, not a cosmetic concern:

- `common/scripted_triggers/005_soviet_collapse_triggers.txt:8194-8210` requires both states `218` and `238` to be owned and controlled by the Soviet-collapse root before DHC can spawn.
- `common/scripted_effects/005_soviet_collapse_effects.txt:22442-22450` sets `soviet_collapse_don_host_successor`, sets DHC's capital to state `218`, and loads the DHC focus tree.
- `common/scripted_effects/005_soviet_collapse_effects.txt:23389-23397` adds DHC cores and transfers states `218` and `238` to DHC.
- `common/scripted_effects/005_soviet_collapse_effects.txt:4121` adds a DON core to state `218` during the Soviet-collapse core pass.
- `common/national_focus/005_soviet_collapse_republics.txt:4700-4742` exposes the DON/KUB host-congress focus to Event 005, so that focus cannot be treated as Event 006 package content.

An IW-039 adapter that checks only generic ownership and reservation state can race with DHC. Before any adapter is admitted, it must reject DHC ownership/control, `soviet_collapse_don_host_successor`, all DHC origin markers, frozen Event 005 state ledgers, and any active Event 005 transfer involving states 218 or 238. The reverse direction must also be tested: Event 005 must not spawn DHC after an IW-039 compact release has consumed or altered its required states.

State 234 is the IW-040 anchor and is also adjacent to Event 005 KHC logic. It remains a separate shared-group exclusion; IW-039 must not silently expand into 234, 235, 237, 218, or other Don/Kuban claims.

## Politics, leader, portrait, flag, advisor, and party issues

### Leader and identity

Vanilla Sidorin is an existing male leader identity, but the current repository has no IW-039-specific role contract, source review, portrait-worker handoff, rights record, or runtime consumer. The installed DLC portrait path is `dlc/dlc034_no_step_back/gfx/leaders/DON/portrait_DON_Vladimir_Sidorin.dds`; its existence does not substitute for an IW-039 package asset/provenance audit. Do not invent a source-placeholder leader, random name pool, or institutional portrait, and do not promote Sidorin as an Event 006 package leader until the role, date, rights, and runtime wiring are explicitly reviewed.

The vanilla DON country file has no Event 006 parties, route governments, advisors, high command, or package-specific political lifecycle. Vanilla neutrality/fascism leader behavior must remain intact when DON is not carrying an IW-039 origin.

### Flags and assets

Vanilla flag ladders exist at `gfx/flags/DON.tga`, `gfx/flags/DON_{communism,fascism,neutrality}.tga`, and matching `medium`/`small` paths. No IW-039 package flag policy has been accepted. Reusing vanilla DON flags may be possible only after the identity/origin contract is approved; generating an alternate flag without source review is not permitted. No flag manifest, rights note, strict dimensions/opacity audit, or runtime DDS handoff exists for IW-039.

## Focus, decision, idea, and localisation issues

- The shared `independence_wave_focus_tree` contains no DON-scoped package adapter or route hooks. Existing Event 005 DON/KUB focus content is not an Event 006 substitute.
- No IW-039 decision or mission category, cost model, trigger/effect contract, timeout cleanup, or localisation exists.
- No IW-039 starting national spirit, lifecycle, icon, or recovery path exists.
- No Event 006 localisation exists for DON country/adjective/party overlays, leader, route governments, decisions, missions, ideas, focus rewards, tooltips, or debug names.
- A future implementation must preserve vanilla strings outside an explicit origin-gated overlay and must encode new localisation as UTF-8 with BOM.

The earlier read-only focus evidence remains structural only: `independence_wave_focus_tree` contained 184 nodes and 193 connectors, with no DON package node; the render/validation reported generic missing continuous-focus sprites. The current MCP route is unavailable for fresh evidence because current Event 006 worktree calls are reported as `ARTIFACT_MANIFEST_INVALID` before source scanning in the IW-040 promotion handoff. A bounded retry was started during this audit but did not complete before the parent-directed stop.

## Starting military, technology, industry, supply, and production issues

Vanilla DON starts with a cavalry-heavy OOB, two research slots, and the source technology set in `history/countries/DON - Don Republic.txt`. The Event 006 mapping requires `mounted_mobile` with tradition 82, defecting regular conversion, depot/remount integration, and no navy or air inheritance. The package has no accepted rule for whether the original fifteen divisions survive intact, convert from a former host, or are replaced by a compact release force. Do not alter the vanilla OOB, equipment, manpower, production, capital, or technologies until the capital and origin transaction are approved.

State 218's major urban, naval, and air infrastructure makes it materially different from the compact rural states 238 and 245. Any choice between a 218 capital, a 245 anchor, or a 245+238 non-capital compact changes supply, production, victory-point, and Event 005 behavior and must be balance-reviewed with the identity decision.

The installed Technology Tree Viewer is unavailable. The earlier technology inspection was partial/source-inaccurate and found no DON-specific Event 006 technology route. No current quantitative technology claim is made.

## AI and playability issues

- No `common/ai_strategy/006_independence_wave_don.txt` or equivalent IW-039 AI profile exists.
- No DON focus selection, decision score, mission score, diplomacy, host-survival, or Join behavior exists.
- The Region-04 random-list wrapper is structurally present, but the candidate is not executable because runtime adapter and content-attestation gates fail.
- Any future AI or weighted selection patch requires the mandatory baseline, owner-applied patch, and same-scenario `hoi4.probability_compare` pass through `chaosx_ai_probability_auditor`.

The previous probability preflight inspected `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt` and found eight structural entries (`IW-033`, `IW-036`, `IW-037`, `IW-038`, `IW-039`, `IW-040`, `IW-041`, `IW-042`), eight required inputs, zero unresolved expressions, and zero available candidates. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc0c34ecad4f8903411ec3674a56735340b03fee925ff54462fd548085a17645/f40579d6ade5219042524ec899c79e375456cd5d93a55d57c878b0ceb748f931a/probability-inspect-e8f1792fa6b1.json`. No evaluate, sweep, simulate, sequence, render, or compare result is claimed because no complete runtime candidate or scenario contract existed.

## Required gates before any central widening

1. Approve an identity matrix that explicitly chooses the IW-039 capital and compact transaction, including whether state 218 is ever transferred, whether 245 remains the anchor, and how SOV retains a protected host remnant.
2. Write and test a bidirectional DON/DHC collision matrix covering Event 005 before IW-039, Event 006 before Event 005, simultaneous reservation, DHC ownership/control, DHC origin flags, frozen ledgers, and cleanup after abort.
3. Approve one OOB and equipment policy that reconciles the vanilla fifteen-division cavalry history with the `mounted_mobile` p39 force mapping and supply/remount costs.
4. Complete identity, leader-role, portrait-worker, rights, flag, and asset-manifest evidence. A sourced portrait remains a placeholder until the user supplies the accepted HOI4-style replacement; no unresolved portrait may be promoted.
5. Implement country-local setup, final-validation, cleanup, generation safety, host survival, focus assignment, decisions/missions, ideas, localisation, and AI before requesting central adapter or attestation edits.
6. Resolve whether FORM-11 is a supported carrier/member route or explicitly excluded from IW-039 admission.
7. Rerun current read-only map, focus, event, technology, and probability MCP inspections after the package exists. Current MCP evidence is blocked by `ARTIFACT_MANIFEST_INVALID`; source review is not an engine substitute.
8. Run the probability baseline and same-scenario post-implementation compare for the Region-04 pool and all new DON AI/weighted surfaces.
9. Only after all gates pass, add IW-039 to the central adapter, content-attestation, setup/final-validation/cleanup dispatcher, normal/scenario preflight, and Join surfaces in one reviewed change.

## Validation and file changes

### Checks performed

- Read the required offline Paradox wiki pages and vanilla documentation before auditing.
- Read the required Chaos Redux event, focus-tree, decision/mission, event-asset, ComfyUI portrait, and subagent skills.
- Inspected current IW-039 preflight/probability handoffs, current IW-040 source/promotion handoffs, registry rows, planner shell, map bindings, central dispatch/Join files, vanilla DON country/history/character/OOB/state/flag files, and Event 005 collision effects/triggers/focuses.
- Ran targeted current-worktree searches confirming no IW-039/DON runtime adapter, attestation, dispatcher, or Join references; the current files contain IW-040 entries instead.
- Attempted the required read-only map, focus, event, technology, and Region-04 probability MCP routes. The bounded batch did not complete before the parent-directed stop; current workspace MCP calls are separately documented as `ARTIFACT_MANIFEST_INVALID` in `006_iw040_kuban_package_promotion_2026_08_12.md`.

### Changed files

- Added only this audit handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw039_country_package_audit_2026_08_12.md`.
- No gameplay, map, asset, localisation, central adapter, attestation, preflight, dispatcher, or Join file was changed.
- No files were staged or committed.

## Simplifications, omissions, and blockers

The package is incomplete by design because its identity, capital/compact transaction, DON/DHC collision policy, OOB policy, portrait/flag provenance, country-specific gameplay, AI, localisation, and current engine evidence are unresolved. No fallback leader, synthetic flag, copied IW-040 package, or central registry shortcut was used. The package remains in preflight and must not be described as admitted, playable, or promoted.
