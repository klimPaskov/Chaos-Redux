# Event 006 GUI and achievement core-surface closure handoff

Date: 2026-08-02

Mode: improvement-loop closure audit and bounded implementation handoff.

No gameplay, GUI, GFX, localisation, achievement, package, formable, super-event, asset, workbook, or catalog source was edited by the audit that produced this handoff. The parent applied the bounded League-frame selector correction described below in `common/scripted_effects/006_independence_wave_effects.txt`.

## Result

Do not add another broad Event 006 mechanic at this point.

The admitted country, League, `6002`, formable, achievement, and Statehood Ledger sources do not expose a safe broad expansion that is independent of the existing package, rights, identity, and formable blockers.

One bounded core correction was required before the GUI/achievement source surface could close: `independence_wave_refresh_status_frame_state` treated the ordinal League phase as a monotonic visual threshold even though the phase enum contains failure, crisis, split, and dissolution states.

The current code therefore maps `congress_failed` to `league_drafting`, `consultative_league` to `league_vote`, and `dissolved_network` to `league_activated`.

The parent replaced those three `greater_than_or_equals` checks with explicit phase groups and clears `independence_wave_status_gui_show_animation` in `independence_wave_reset_current_generation`. The source-level selector and cleanup contract are now closed; the semantic render matrix below remains a bounded offline-QA receipt rather than a live-game claim.

The older claim that no admitted package can complete the Radical Bloc route is also stale.

IW-184/HBX is admitted, assigns the full shared framework, explicitly allows Radical Sovereignty and the League route, and can reach the radical dangerous-milestone and containment-survival proof under the accepted high-chaos or Open Sovereignty gates.

No achievement or `6002` gameplay rewrite is justified by the current source.

## Highest-impact bounded implementation tranche

### 1. Correct the League status-frame selector

Owner surface: `common/scripted_effects/006_independence_wave_effects.txt`, effect `independence_wave_refresh_status_frame_state`.

Retain the default assignment `independence_wave_gui_league_frame = constant:independence_wave_gui_frame.league_rest`, then use exact equality groups instead of ordinal comparisons:

| GUI frame | Exact League phases |
| --- | --- |
| `league_rest` | `none`, `informal_network`, `congress_failed`, `dissolved_network` |
| `league_drafting` | `regional_conferences`, `congress_preparation` |
| `league_vote` | `charter_vote` |
| `league_activated` | `consultative_league`, `formal_league`, `durable_league`, `league_crisis`, `reformed_league`, `rival_leagues` |

This is a presentation correction only.

It must not change League phase values, phase transitions, charter flags, decisions, AI, achievements, or the ASSET-042 frame order `rest, drafting, vote, activated`.

### 2. Reconcile the Radical Bloc reachability statement

Update the stale wording in `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `docs/super_events/006_independence_wave/research.md` after the parent accepts this source trace.

The corrected statement should be: the Radical Bloc achievement is source-reachable through admitted IW-184/HBX when its high-chaos or Open Sovereignty reveal condition is met, HBX locks Radical Sovereignty, becomes League leader, establishes or transforms a radical-revisionist League, satisfies the dangerous-milestone thresholds, receives an external containment attack against the qualified bloc, and remains sovereign for the configured year.

Do not imply that the route is automatic or easy.

Do not weaken the route, League, danger, external-war, scenario-exclusion, or survival gates merely to produce a witness.

### 3. Record the remaining static achievement matrix

The source definitions, proof triggers, reset writers, presentation keys, and 48 DDS achievement states are present.

The remaining work is a current row-level receipt that records a positive proof, a near miss, every accepted disqualifier family, reset or persistence behavior, scenario provenance behavior, and admission reachability.

| Achievement | Final trigger | Current source disposition | Required static receipt |
| --- | --- | --- | --- |
| `chaosx_006_one_state_to_statehood` | `independence_wave_achievement_one_state_to_statehood_is_complete` | Source-complete for admitted anchor packages | Positive ten-year proof; subject, reunion, and free-recognition exclusions |
| `chaosx_006_no_master` | `independence_wave_achievement_no_master_is_complete` | Source-complete | Positive mature state; dependency history and client-route exclusions |
| `chaosx_006_peace_with_host` | `independence_wave_achievement_peace_with_host_is_complete` | Source-complete | Negotiated settlement clock; forced settlement, renewed war, and subject near misses |
| `chaosx_006_break_reconquest` | `independence_wave_achievement_break_reconquest_is_complete` | Source-complete | Former-host attack and peace; capital-loss grace success/failure and client exclusion |
| `chaosx_006_found_league` | `independence_wave_achievement_found_league_is_complete` | Source-complete | Natural five-founder proclamation versus scenario-preformed League exclusion |
| `chaosx_006_cross_regional_league` | `independence_wave_achievement_cross_regional_league_is_complete` | Source-complete | Two-year continuous proof; cohesion loss, split, radicalization, exit, and preformed exclusions |
| `chaosx_006_rescue_member` | `independence_wave_achievement_rescue_member_is_complete` | Source-complete | Exact DM-44 rescuer/target survival; reunion, annexation, subject, and capitulation near misses |
| `chaosx_006_regional_formable` | `independence_wave_achievement_regional_formable_is_complete` | Source-complete for admitted FORM-01 through FORM-05 families | Committed transaction plus every required first-stage receipt; incomplete integration rejection |
| `chaosx_006_volga_bulgaria` | `independence_wave_achievement_volga_bulgaria_is_complete` | Intentionally unreachable because IW-043/CHU remains unadmitted | Compile-time admission rejection and route-proof fail-closed receipt; do not admit the package here |
| `chaosx_006_assyria_survives` | `independence_wave_achievement_assyria_survives_is_complete` | Intentionally unreachable because IW-058/ASY remains unadmitted | Compile-time admission rejection and route/community/host proof fail-closed receipt; do not admit the package here |
| `chaosx_006_small_to_major` | `independence_wave_achievement_small_to_major_is_complete` | Source-complete | Institutional-major receipt before formable, professional army, and successful League goal; wrong-order near miss |
| `chaosx_006_radical_bloc` | `independence_wave_achievement_radical_bloc_is_complete` | Source-reachable through admitted IW-184/HBX; older no-route wording is stale | Full HBX route-to-League-to-danger-to-external-war-to-one-year chain; forced-scenario, no-containment, and short-survival near misses |
| `chaosx_006_every_flag_survival` | `independence_wave_achievement_every_flag_survival_is_complete` | Source-complete within the accepted SCN-008 package boundary | Low non-Common-Congress proof; other intensity/type, plan mismatch, subject, annexation, and below-85-percent near misses |
| `chaosx_006_balanced_patrons` | `independence_wave_achievement_balanced_patrons_is_complete` | Source-complete | Three distinct major-aid patrons and buyout; duplicate patron, dependency history, unbought concession, and client near misses |
| `chaosx_006_league_arbitrator` | `independence_wave_achievement_league_arbitrator_is_complete` | Source-complete; the formerly writerless expulsion disqualifier is implemented | Five DM-43 receipts in one term; leadership transfer, member war, DM-51 coercion, successful DM-60 expulsion, and cancelled vote behavior |
| `chaosx_006_host_remnant` | `independence_wave_achievement_host_remnant_is_complete` | Source-complete | Exact settlement count and peaceful ten-year proof; subject, reconquest, renewed war, capital, stability, factory, and infrastructure near misses |

## Statehood Ledger source evidence

| Surface | Source evidence | Result |
| --- | --- | --- |
| Category registration | `common/decisions/categories/006_independence_wave_categories.txt` exposes `independence_wave_status_scripted_gui` on the founding category | PASS |
| Window contract | `interface/006_independence_wave.gui` defines the 700x500 `independence_wave_status_window`, five value rows, host/patron/network/phase/mission panels, five tabs, refresh, and animation toggle | PASS |
| Visibility | `common/scripted_guis/006_independence_wave_scripted_gui.txt` requires `is_independence_wave_active_country = yes`; AI is disabled | PASS |
| Refresh | `independence_wave_status_refresh_click` calls `independence_wave_refresh_country_state`, which recomputes country state and the frame variables | PASS |
| Tab exclusivity | Each tab effect clears the other four tab flags; the government panel is the default when none is selected | PASS at source |
| Recognition frames | Explicit band thresholds select frames 1 through 5 | PASS at source; semantic render receipt remains |
| Dependency frames | Explicit patron-warning and severe-instability conditions select calm, watch, and danger | PASS at source; semantic render receipt remains |
| League frames | Explicit equality groups keep failed and dissolved phases on rest, draft only covers regional/congress preparation, charter vote is isolated, and live league phases share activated | PASS at source; semantic render receipt remains |
| Formable frames | Discovery, complete initial integration, and committed transaction select frames 2 through 4 over the hidden default | PASS at source; semantic render receipt remains |
| Animation toggle | Static state strips are visible without `independence_wave_status_gui_show_animation`; authored animated siblings are visible with it | PASS at source; toggle-off semantic return receipt remains |
| Cleanup | `independence_wave_reset_current_generation` clears the five tab flags, animation flag, and generation-local frame variables | PASS at source |
| Localisation | `localisation/english/006_independence_wave_gui_l_english.yml` covers title, values, host, patron, network, phase, mission, tabs, panels, and click tooltips | PASS |

## Fresh read-only GUI evidence

`hoi4.gui_inspect` and `hoi4.gui_render` were run against workspace `mod_chaos_redux_ea3b2d67c2c0`, window `independence_wave_status_window`, scenario `independence_wave_status_default`, and shared/source revision `082abcc3c772f7261ddce65ba39ad0fb2c78fda213c301816c9cb38c0e5f2d30`.

The inspector returned `GUI_INSPECTED`, inspected 48 elements, skipped no source, and produced:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc86732904d49e5d2c0bb4786e49ad854cda732d76464162328679814a879b51/9bb997528369f30eaebfb02ce674924b8f3f0eef6b19c2dac6c5199c3d318599/gui-inspect.082abcc3c772f726.json`

The renderer returned `GUI_RENDERED` for 1280x720 and 1920x1080 across `normal`, `warning`, `minimum-value`, `maximum-value`, `long-text`, and `missing-localisation` states.

Key artifacts are:

- Full PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4cb77f76216bc0fbb09931da2f0e3b0001502f3f1778ba3c88dc6fc2ea68223/f2f02fc7e44772276a4fad853a8fd0ed0379bc93e9cd14ded283897378415f98/independence_wave_status_window-full.png`
- Click regions PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a3dc6c07d5466c833a45c8728c46c37519e85939704f39bf5855dc95ba27a56/1a6ac4c3ebab6b822221efb37486c50cf48151e0bc7bd19fc0b4b990b7e25caa/independence_wave_status_window-click-regions.png`
- State matrix JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cbb1933f83f39fae5ba2a981f4febc94926ff6615541a01258cd8bfe38a7b6e3/285b4c300ce95467861a51a29021d41f184aadf5d9007163bef8189c0ee5daa2/independence_wave_status_window-state-matrix.json`
- State matrix PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec5eeb2eb930ef44ad092dff21fb6bfb9823c47a2a7f677e51711ab2619f1300/baf058e2acedf07bafcf34760079a293db9120293c44830e016e6d911d57ac6d/independence_wave_status_window-state-matrix.png`
- Resolution-scale JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/886535f38a570ff0fc908a156d93f2e5647891d8049d02fa2bc6305a599f5de5/536614a9bc7b2c239a84dfe45ccb63c16f3a712e4b6c201174551dc1dbe78ad4/independence_wave_status_window-resolution-scale.json`
- Resolution-scale PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/688eb99d5f9ae866a1245a7cdc151f95cba6221f9784f03a706f13be3c82c358/8b2f6c4f7e03f0ca3ad142ed41d388f9c7d861557e469fcd9e48c8a53bb59e23/independence_wave_status_window-resolution-scale.png`
- Validation JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be12ba311eaa0b8f355bd0adf17f423c9dbdc00362fc786d9f4f2a72f9d54416/ea247a804b8c096e179a3b6fdc28ceb857b8b3328cf7b0acca52ead8cdab749c/independence_wave_status_window-validation.json`

This is bounded offline evidence, not a global GUI PASS.

The default scenario does not populate the Event 006 flags and values needed to prove the semantic frame and toggle matrix.

The workspace-wide validator reports 1,955 blocking diagnostics and 79 visible-overlap diagnostics across the complete mod; no Event 006-specific diagnostic appeared in the filtered inline result, but the global ceiling prevents converting this run into a clean validation claim.

## Required post-patch GUI scenario matrix

After the League-frame selector is corrected, run the same two resolutions with explicit Event 006 scenarios and record the selected frame plus visible panel or sprite in each case:

| Scenario family | Required states | Expected evidence |
| --- | --- | --- |
| Tabs | no tab flag, then each of the five tab flags | Government is the default; exactly one panel is visible after every click |
| Recognition | below Observed, Observed, De Facto, Treaty-backed, Internationally Entrenched | Frames 1, 2, 3, 4, 5 |
| Dependency | no warning, patron warning, severe instability | Frames 1, 2, 3 |
| League | none, informal, regional conferences, congress preparation, congress failed, charter vote, consultative, formal, durable, crisis, reformed, rival leagues, dissolved network | Exact four-frame grouping defined in this handoff; failed and dissolved never show activated, and consultative never shows vote |
| Formable | hidden, discovered, all required initial integration complete, transaction committed | Frames 1, 2, 3, 4 |
| Animation toggle | semantic static frame, animation on, animation off | One static or animated sibling is visible at a time; toggling off returns to the current semantic frame |
| Refresh | mutate a founding value or phase, then invoke refresh | Text band and selected frame agree after the refresh effect |
| Cleanup | active non-default tab and animation flag, then country reset | Flags and frame variables clear; default government/static presentation returns on the next valid setup |

## Radical Bloc source trace

The admitted route is concrete:

1. `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` marks IW-184 California/HBX `automatic_pool_ready` with a government pool that includes a high-chaos republic.
2. `has_independence_wave_package_content_attestation` includes `iw_184`, and `independence_wave_liberations_capacity_try_iw_184` is present.
3. `independence_wave_setup_iw_184_california` calls `independence_wave_focus_allow_radical_sovereignty_route` and `independence_wave_focus_allow_league_route` while assigning the full framework.
4. `can_reveal_independence_wave_radical_sovereignty`, `independence_wave_reject_inherited_borders`, and `independence_wave_focus_lock_radical_sovereignty_route` write the route proof under high-chaos, Open Sovereignty, or the accepted sponsorship gate.
5. The shared League branch can propose or transform to `independence_wave_league_route.radical_revisionist` and records revisionist actions.
6. `has_independence_wave_danger_radical_offensive_league` requires a durable radical-revisionist League, the member/common-cause/reserve/action thresholds, and a live current leader.
7. `independence_wave_publish_danger_milestone` qualifies that leader only for the radical-offensive reason and calls `independence_wave_achievement_begin_radical_containment`.
8. `on_war_relation_added` starts the containment clock only when a non-member attacks the qualified League, and `independence_wave_achievement_radical_bloc_is_complete` requires the radical route, external containment engagement, non-forced provenance, and the configured one-year survival period.

This static trace proves source reachability, not occurrence frequency, AI likelihood, or live completion.

## Research and precedent basis

The relevant offline Interface Modding, Scripted GUI Modding, Decision Modding, Achievement Modding, Localisation, Data Structures, Triggers, Effects, Scopes, On Actions, and AI Modding pages were reviewed together with vanilla decision-category/scripted-GUI and achievement definitions.

The Event 006 candidate matrix, seven-part specification, current source-of-truth map, v98/v99 audits, asset animation manifests, `6002` research, and current source files remain the design authority.

No new historical assertion is needed for this correction.

The IW-184 evidence uses only the already accepted California/HBX alternate-history package direction; it does not broaden the historical or territorial claim.

The installed MCP package has no Technology Tree Viewer.

That limitation is recorded but does not block this GUI/achievement tranche because no technology tree is affected.

## Scope exclusions

Do not use this tranche to:

- admit IW-030, IW-043, IW-058, IW-093, or any other unadmitted package;
- alter super-event `6001`, substitute audio, or create a fallback;
- weaken any `6002` qualification predicate;
- implement another formable family or bypass FORM-39, FORM-42, or FORM-48 member and identity gates;
- add a second Statehood Ledger, another animation family, or another achievement;
- change League gameplay merely to simplify the four-frame display.

## Prior addendum and promotion disposition

The v67 core dynamic-system addendum is implemented and closed.

The IW-043/IW-058 and IW-093/IW-098 package addenda remain implemented in part and explicitly queued at their admission or research boundaries; this handoff does not restack them.

The generic focus closure is separate and already resolved under the one-tree contract.

Keep this handoff in `docs/plans/006_independence_wave_plans/subagent_handoffs/` as implementation and validation evidence.

No design promotion into `docs/specs/006_independence_wave_specs/` is required because the four semantic animation states and the Radical Bloc achievement already exist in the accepted specification.

After the parent applies and validates the exact League-frame correction, reconcile only the stale reachability and GUI-evidence statements in the current source-of-truth and super-event research documents.

## Completion boundary

This tranche is complete only when the explicit League phase groups are implemented, the post-patch GUI scenario matrix is recorded, the sixteen-row achievement receipt is current, and the stale Radical Bloc reachability statements are corrected.

It does not close whole Event 006 completion.

Package capacity/admission, incomplete formable families, broader asset provenance/cleanup, catalog status, and rights-blocked `6001` remain separate blockers.

No fallback or simplification is authorized.
