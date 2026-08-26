# Event 016 D’Rhonda and Alien Infantry completion audit — 2026-08-25

> Historical completion snapshot superseded for Alien Infantry runtime status by the accepted V13 provider package and static runtime promotion recorded in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_runtime_promotion_2026-08-26.md`. Keep the audit evidence and its live/MCP limitations, but do not use its pre-promotion V8/V10/Quaternius action or missing-package statements as current status.

## Audit outcome

**Overall status: incomplete.** The D’Rhondan contact gameplay, Alien Infantry public API, Event 019 provider migration, Event 016 log/detail registration, four-evolution identity, achievements, and existing Event 016 super-event/aftermath source surfaces are substantially implemented. Completion cannot be claimed because the Alien Infantry runtime model package is still missing four accepted semantic actions plus a supported muzzle locator and synchronized effects/audio, current MCP event evidence is partial or unavailable on several required chains, the current weighted rebellion surface did not receive a fresh completed probability pass, and live acceptance remains open.

This was a read-only gameplay audit. No gameplay, localisation, asset, GFX, sound, spreadsheet, or runtime source was edited. This handoff is the only file created.

## Governing requirements and references

The audit applied `AGENTS.md`, `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, and `chaos-redux-3d-model-pipeline`. It consulted the required offline wiki surfaces, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and the relevant technology/special-project material. It also consulted the installed vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`, including the script-concept, effects, triggers, dynamic-variable, and localisation documentation, plus vanilla event/technology precedents.

The binding design sources are:

- `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md`.
- `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md`.
- `docs/specs/016_brilliant_scientist_specs/016_source_of_truth_map.md`.
- `docs/specs/016_brilliant_scientist_specs/016_core_runtime_handoff_map.md`.
- `docs/specs/016_brilliant_scientist_specs/matrices/016_asset_inventory.md`.
- `docs/specs/016_brilliant_scientist_specs/016_event_chain_map.md`.
- `docs/events/016_brilliant_scientist/systems/super_events_and_aftermath.md`.

The complete Event 016 spec directory was inventoried and searched across its current source files. The binding addendum, source maps, acceptance scenarios, package status, and relevant matrices were read directly. This audit did not perform a second literal byte-for-byte reread of every historical source file already reconciled by the current runtime map; older superseded documents are therefore treated as historical evidence, not current authority.

## Requirement-by-requirement status

| Requirement | Status | Evidence | Missing proof or blocker |
| --- | --- | --- | --- |
| `.40` craft completion/contact entry | Partial | `events/016_brilliant_scientist_dhrondan_contact_events.txt:10-23`; project completion routes to it from `common/scripted_effects/016_dhrondan_contact_effects.txt` | Current MCP trace is partial; helper catalog does not resolve `dhrondan_ai_try_authorize_expedition` even though its source definition exists. |
| `.41` expedition departure | Source-complete | `events/016_brilliant_scientist_dhrondan_contact_events.txt:25-47`; 180-day mission/cost logic is in `common/decisions/016_dhrondan_contact_decisions.txt` and the contact effects/constants | No current dynamic engine execution evidence. |
| `.42` audience and pact | Partial | `events/016_brilliant_scientist_dhrondan_contact_events.txt:49-72` | MCP marks `dhrondan_authorize_pact_and_return` unresolved although its source definition exists at `common/scripted_effects/016_dhrondan_contact_effects.txt:228`; source review is not equivalent to engine lifecycle proof. |
| `.43` successful return | Source-complete | `events/016_brilliant_scientist_dhrondan_contact_events.txt:74-101`; report/transaction cleanup is source-wired | Current runtime execution not proven. |
| `.44` landing report | Source-complete | `events/016_brilliant_scientist_dhrondan_contact_events.txt:103-115`; landing decision reserves exactly 2,000 laser weapons for seven days in `common/decisions/016_alien_infantry_landing_decisions.txt` | Landing target selection, refund, spawn, and receipt behavior lack a complete current MCP probability/lifecycle run. |
| `.45` failed expedition | Source-complete | `events/016_brilliant_scientist_dhrondan_contact_events.txt:117-143`; failure cleanup is source-wired | Current runtime execution not proven. |
| `.46` rebellion warning | Source-complete | `events/016_brilliant_scientist_dhrondan_contact_events.txt:145-161` | Current one-time presentation behavior not dynamically exercised. |
| `.47` rebellion bridge | Partial | `events/016_brilliant_scientist_dhrondan_contact_events.txt:163-179`; source bridge is `common/scripted_effects/016_dhrondan_contact_effects.txt:373` | MCP marks `dhrondan_begin_rebellion_bridge` unresolved although the source definition exists; country-package territory/stockpile transfer remains a separate owner surface. |
| Event 016 remains one minor fire-once event | Partial | `events/016_brilliant_scientist.txt:15-29` retains `chaosx.nr16.1` as the hidden entry dispatcher; the shared automatic-event registry and availability effects own fire-once behavior; the catalog row classifies Event 016 as `Minor Fire-Once` | The entry event itself does not use Clausewitz `fire_only_once`; shared-registry enforcement was source-reviewed but not dynamically proven in this audit. |
| Exactly four logged evolutions | Source-complete, validation partial | `events/016_brilliant_scientist_evolutions.txt:13`, `:84`, `:164`, and `:216` define `.21-.24`; `.90` schedules them at `:324`; constants declare stages 1-4 in `common/script_constants/016_brilliant_scientist_constants.txt:16-27`; detail preview rows are registered at `common/scripted_effects/chaosx_events_log_effects.txt:2567-2583` | No current evolution-chain MCP rerender was produced in this bounded audit. No fifth evolution was found. |
| No Event 016 cluster | Complete by design | Event 016 catalog `Cluster ID` and severity are blank; the generated cluster catalog contains no Event 016 row; the binding Alien Infantry addendum explicitly forbids adding a cluster | No missing cluster should be created. |
| Alien Infantry public identifiers | Source-complete | `alien_infantry` is the unit/API id and `alien_laser_weapon_equipment` is the equipment family; `common/units/016_brilliant_scientist_project_forces.txt`, `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`, and the Alien Infantry API sources use the stable names | Runtime model/entity is still absent, so source identifiers do not prove a finished visible unit package. |
| Envoy craft project | Partial | `common/special_projects/projects/016_dhrondan_envoy_project.txt:15-34` defines `sp_dhrondan_envoy_craft`, with project output through the D’Rhondan completion helper; Event 025 Antarctica bypass and Event 036 evidence-only behavior are present in the contact triggers/effects | The installed probability/technology adapters cannot model special-project AI or project completion timing; no complete MCP project proof exists. |
| Expedition tuning | Source-complete | Contact decisions/constants implement 180 days, 50 political power, and 500 fuel for the expedition contract; source localisation reflects these values | AI authorization evaluation previously timed out; no fresh complete mission-AI result. |
| Rebellion tiers | Source-complete, probability acceptance blocked | `common/scripted_effects/016_dhrondan_contact_effects.txt:345-367` orders high, medium, then low and builds the exact complement; constants/triggers define 10/20/40 tiers and the 6/8/10-arrival, 30/50-strain, 600/800-chaos gates | The current source SHA-256 is `09E4A3A12A4E525CADD5060CC266D34D64F96CC0A6C9E8C37E2E2D8DE2E4571E`. The successful 2026-08-22 probability artifact covered source hash `ED0E8CAEAC0D11A0FE4453319A52E65DFE06FA8A99B5EDB569087710F26E1672`, so it is compatible historical evidence, not a current-source proof. A fresh auditor pass was interrupted at the parent’s direction after MCP retries were stopped. |
| More-than-15-enclave precedence | Resolved design issue; live acceptance open | `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_enclave_precedence_resolution_2026-08-22.md` records the approved rule: ordinary placement caps at 15; each otherwise uncovered component receives one exact 2,000-laser supplemental store | Older handoffs that still call this an unresolved design conflict are stale. Live multi-component conservation remains user-owned. |
| DHR country formation/news continuation | Source-complete, validation partial | `events/016_dhrondan_country_events.txt` defines `.48-.52`, including formation news, compact events, and the hidden safety monitor; country package/focus/decision owners hold the transfer and follow-through | This audit was bounded to `.40-.47`; it used existing structural evidence for `.48` but did not obtain a fresh whole-file render for `.48-.52`. |

## Event log, details, catalog, and actor ownership

The shared event log binds the opening actor to the Event 016 prefire/current host at `common/scripted_effects/chaosx_events_log_effects.txt:283-288` and `:771-779`. The details preview registers exactly four evolution stages at `:2567-2583`. Scripted localisation maps the Event 016 name and evolution titles, and the generated event catalog row contains four populated evolution columns with the fifth blank.

The catalog currently says `Needs Testing`. Its cluster fields are blank, its type is `Minor Fire-Once`, and its world-end prose names Laboratory World and Strategic Singularity. Those values agree with the binding design. The status is not stale: runtime/MCP/user acceptance is still open.

No D’Rhondan contact `.40-.47` event is registered as an Event 016 evolution or cluster member. This is correct and must remain so.

## Super-events, world-end hooks, and aftermath

### Source state

Event 016 owns exactly six visible super-event packages in the current design, with registry ids 90-95: recognition, KRG formation, international threat, Laboratory World, Strategic Singularity, and qualifying defeat. Queue dispatch is event-driven through `chaosx.nr16.300` in `events/016_brilliant_scientist_super_events.txt:10-17`, with actor cleanup helpers `.901-.902` at `:22-59`. There is no periodic global scan.

World-end scenario ids 11 and 12 are the Event 016 Laboratory World and Strategic Singularity outcomes. The shared log reads `world_end_brilliant_scientist_laboratory_world` and `world_end_brilliant_scientist_singularity` at `common/scripted_effects/chaosx_events_log_effects.txt:1341-1345`. Event 016 does not directly seize the Strategic Singularity world-end lock; Fallout owns that lock by the accepted source-of-truth contract.

The aftermath event file defines `.301-.303` and remnant resolution events `.310-.318`, including the Alien cache outcome at `.317` (`events/016_brilliant_scientist_aftermath_events.txt:334-363`) and Singularity core resolution at `.318` (`:369-397`). The aftermath documentation and decision/icon package describe these consumers.

### Exact missing or unresolved super-event issues

- **No D’Rhonda-specific super-event is missing.** The Alien Infantry/D’Rhondan addendum explicitly keeps `.40-.47` as contact follow-ups and does not add a seventh Event 016 super-event package.
- The current `hoi4.event_inspect` call on `events/016_brilliant_scientist_super_events.txt` returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7dd7e929af67b49dc5ecb25c053b0dfc3c447a5a0ff4b160cc2508fc58263ff/881dd7ff4cc7571ae7384df806a5b7c00624e83dc9e3be930985c3fde6572872/event-scan-7d541a2019d5.json`.
- A bounded current super-event overview render timed out. Bounded current aftermath inspect and render calls also timed out. These exact MCP limits prevent a completion claim for queue reachability, terminal cleanup, and aftermath event traversal even though the source is present.
- Current live audio visibility, actor cleanup, one-shot queue dispatch, and world-end lock ownership remain user/parent acceptance items. No source-only inference is promoted to live proof.

## Achievements

Exactly 17 Event 016 achievements are registered in `common/achievements/chaos_redux_achievements.txt:3205-3290`:

1. `borrowed_century`
2. `every_door`
3. `public_method`
4. `the_one_who_left`
5. `clean_break`
6. `approve_everything`
7. `the_former_host`
8. `combined_arms_redefined`
9. `clever_girl`
10. `the_machine_continues`
11. `population_one`
12. `yesterday_sent_help`
13. `not_from_here`
14. `no_second_sun`
15. `the_last_calculation`
16. `the_world_is_the_laboratory`
17. `ordinary_people_won`

No additional D’Rhonda-specific achievement is required by the accepted addendum. Therefore **no achievement definition is missing from this scope**.

Alien Infantry participates in `combined_arms_redefined`: `common/scripted_effects/016_brilliant_scientist_achievement_effects.txt:91` increments the project-family count when the alien-arms project is active and a fielded division has an `alien_infantry` battalion; the completion trigger is at `common/scripted_triggers/016_brilliant_scientist_achievement_triggers.txt:235-239`.

The unresolved achievement issue is validation, not a missing key: current live eligibility for all 17 achievements and the Alien Infantry combined-arms contribution has not been exercised in this audit. Achievement art/localisation are installed according to the current asset matrix, but this audit did not independently decode and rerender every achievement icon.

## Event 019 migration

Provider 508 is the current Alien Infantry Event 019 contract. `common/script_constants/016_brilliant_scientist_project_force_constants.txt:507-515` declares the Alien Infantry family with `provider_id = 508` and `source_event_id = 16`. Registration and callbacks are in `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:55-65`, `:169-184`, `:628-719`, `:744`, `:999-1094`, `:1610-1651`, and `:1918-1955`. The legacy refund body is deliberately a no-op at `:1478` because provider 508 does not pay through it.

The current design grants and cleans only the provider-508 receipt, limits a transaction to one family lot/one exact 2,000-laser debit, and uses explicit commit/rollback and parent isolation. Older provider-522 or generic provider handoffs are historical and must not override the provider-508 API handoff.

Current MCP evidence is incomplete. A fresh inspect of `chaosx.nr19.1` returned `EVENT_INSPECTED_PARTIAL`; a fresh options render returned `INTERNAL_ERROR` with no artifact. Earlier 2026-08-22 structural evidence remains useful but is not a fresh render of the current graph. Required live conservation, absent/present receipt isolation, cleanup, and rollback scenarios remain open.

## Technology and project links

- `brilliant_scientist_alien_infantry_tech` enables `alien_laser_weapon_equipment_1` at `common/technologies/016_brilliant_scientist_project_technologies.txt:170-177`.
- `brilliant_scientist_alien_predictive_warfare_tech` depends on Alien Infantry technology at `common/technologies/016_brilliant_scientist_project_force_technologies.txt:106-115` and enables its two tactics.
- The sub-unit remains `active = no` and is made operational through the public API; this is intentional and prevents an early direct unlock from bypassing the receipt/project contract.
- `sp_dhrondan_envoy_craft` is defined in `common/special_projects/projects/016_dhrondan_envoy_project.txt:15-34`.

Current tech MCP evidence is partial. Alien Infantry technology inspect and render returned `TECH_INSPECTED_PARTIAL`/`TECH_RENDERED_PARTIAL`; the predictive technology inspect returned partial evidence, while its current render timed out. The special-project adapter cannot represent `sp_dhrondan_envoy_craft` or prove its output. No preserved pre-change graph exists, so the required compare route returns the equivalent of `TECH_COMPARISON_BASELINE_REQUIRED`; there is no before/after technology proof to claim.

## Visual, portrait, counter, sound, and 3D state

### Completed or source-wired asset surfaces

- The Alien Infantry large and on-map counters are original and registered in `interface/alien_infantry_system.gfx`: `unit_alien_infantry_icon.dds` is 152x42/two frames with SHA-256 `5F982AF84059CB980828E5CBE63489AABB13F04A2AABFBC81B9B01038193FC6A`; `onmap_unit_alien_infantry_icon.dds` is 60x12/two frames with SHA-256 `775980A00D618DCC675BFD12192F53C11ACAD7380D36B008A69FAA432CBDC07B`. The handoff records exact installed `subuniticons.gfx` and matching skill-local counter-family inspection.
- Alien Infantry equipment, technology, tactic, decision, event, focus, flag, portrait, and country-interface 2D art is installed and registered according to `docs/specs/016_brilliant_scientist_specs/matrices/016_asset_inventory.md`.
- The fictional DHR roster has the required `chaosx_portrait_creator` handoff: `016_dhrondan_portrait_package_handoff_2026-08-21.md`. It records 12 native-ImageGen full portraits, nine role cards, final DDS/GFX wiring, hashes, and parent visual approval. No grounded placeholder or replacement portrait remains.
- The sourced Alien Infantry audio package records source pages, licences, original and derived hashes for laser fire, movement, idle, and death in `alien_infantry_3d_model_handoff.md` and `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/runtime/sound_handoff.md`. These assets are installed support, not synchronized runtime proof.

### Hard 3D/runtime blocker

The latest authoritative tranche is `016_alien_firearm_meshy_rig_and_free_animation_2026-08-25.md`. It supersedes older statements that recovery awaits approval or credits.

The approved Quaternius CC0 source has produced three accepted, exported, and actual-byte-reimported actions on the Meshy V8 R2 rig:

- Idle: `alien_infantry_quaternius_idle.anim`.
- Move: `alien_infantry_quaternius_move.anim`.
- Laser attack: `alien_infantry_quaternius_laser_attack.anim`, with verified discharge phase at frame 6 / 0.1667 seconds.

The package is still a completion blocker because:

- Defend was rejected for an implausible raised-knee balance.
- Death was rejected because the integrated pistol separates from the hand during collapse and settling.
- Support attack has no independent substantive firing action; semantic reuse of the laser-attack clip is forbidden.
- Retreat has no valid independent action.
- The locked adapter exposes no supported operation to create or validate a stable muzzle locator/socket. The Meshy rig has no weapon or muzzle bone.
- `alien_laser_muzzle_particle`, `alien_laser_muzzle_flash`, and `alien_infantry_laser_fire` remain intentionally unbound despite the verified discharge frame.
- There is no complete seven-action set, final parent-owned entity/action-state wiring, synchronized particle/light/audio crosswalk, or live model consumer proof.

No generated, synthesized, manually authored, placeholder, unlicensed, semantic-alias, transform-only, Blender-repaired, or guessed substitute was accepted. The audio and bespoke counter gates are documented, but they do not waive the missing action/muzzle/entity gates.

## MCP event evidence and exact limits

Current contact-chain inspect/render evidence uses workspace `mod_chaos_redux_ea3b2d67c2c0`, graph revision `7d541a2019d5a129c40fd9666b825bf87b88628b0a3ff4f2ba44df4ea382d8e1`.

- `.40` helper-expanded trace: `EVENT_INSPECTED_PARTIAL`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b080c763158bd82c9af3b5e66f44ced4f2360b986522142e3c28031be323b524/f3cfcd709422560f37804e91721c18a9400b89fb8e6ff8cfb7aa969779e7cb9f/event-trace-7d541a2019d5.json`.
- `.40-.47` file scan: `EVENT_INSPECTED_PARTIAL`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d390a4b74d96fc8889607c383962d440544623f191356a9e2964362b08156a9c/7730e9c668999fca4c1ab0d91669121992e42680949a28d60a6acb1b73fe92b/event-scan-7d541a2019d5.json`.
- `.40-.47` overview render: `EVENT_RENDERED_PARTIAL`; manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84ade298c44ad14cf10dc6334f55563b82c64f4598e2755d09d6a0ce29d77354/0aa9bc1f22378ae44184bbc2e0e66ee4323d31eff6722821a3d7993787e81695/event-overview-7d541a2019d5-manifest.json`.
- The current artifact selected all eight contact events and their options/terminals, but `complete = false`. Its three helper-resolution diagnostics are the source-defined helpers named above; these look like catalog false negatives, but they remain adapter blockers.
- No compatible preserved before graph exists. `hoi4.event_compare` therefore reports `EVENT_COMPARISON_BASELINE_REQUIRED`; current overview/trace artifacts are not a legal baseline substitute.
- Event 019 current inspect is partial and its current render failed `INTERNAL_ERROR`.
- Super-event current inspect is partial; super-event render and aftermath inspect/render timed out under the bounded stop rule.

These artifacts are structural evidence only. They do not simulate the engine or replace user-owned live validation.

## Accepted-plan disposition

| Accepted plan or finding | Disposition |
| --- | --- |
| Alien Infantry/D’Rhonda binding addendum | Promoted into source for `.40-.47`, project/contact/landing/rebellion, provider 508, technology, 2D assets, and documentation. Still incomplete at 3D runtime and full acceptance gates. |
| Event 016 identity: one fire-once event, four evolutions, no cluster | Source and catalog aligned. Dynamic shared-registry proof remains partial. |
| DHR more-than-15 enclave rule | Accepted and implemented according to the 2026-08-22 precedence-resolution handoff. Older conflict reports are superseded. |
| Event 019 provider 508 migration | Accepted and source-implemented. Current MCP render and live conservation/isolation acceptance remain blocked. |
| Meshy V8 plus approved professional-source recovery | Active and partial. Three actions accepted; four roles, muzzle synchronization, entity wiring, and live acceptance remain open. |
| DHR fictional portrait package | Completed by the portrait worker, wired, hashed, and parent-approved. |
| DHR-specific cluster, fifth evolution, or seventh super-event | Rejected by design; none should be added. |

No accepted plan in this scope was silently dropped. The 3D plan remains explicitly active/incomplete rather than being hidden as future polish.

## Stale or contradictory documentation

- `016_core_runtime_handoff_map.md` predates the current Alien Infantry runtime push and includes historical language that Event 016 model packages were deferred outside a no-model scope. That statement is stale for Alien Infantry because the binding addendum and acceptance scenarios make the custom unit model package a hard completion requirement.
- Older model handoffs that say new user approval, approximately 30 credits, or another Meshy recovery authorization is required are superseded by the 2026-08-24 reconciliation and 2026-08-25 approved Quaternius continuation. The current blocker is action/muzzle/runtime capability, not authorization or funding.
- Older completion audits that call the more-than-15 DHR enclave rule an unresolved design conflict are superseded by `016_dhrondan_enclave_precedence_resolution_2026-08-22.md`.
- Older provider-522 or generic Event 019 Alien Infantry notes are superseded by the provider-508 API handoff and current constants/effects.
- The event catalog `Needs Testing` status is current, not stale. The catalog’s no-cluster/four-evolution/world-end wording aligns with source.

## Meaningful validation performed and missing

Performed:

- Source-path verification of all `.40-.47` events, their helper calls, project completion, expedition/pact/return/failure/landing/warning/rebellion effects, and exact rebellion tier construction.
- Cross-check of Event 016 entry identity, four evolution event ids, event-log actor binding, four detail-preview stages, blank cluster row, and catalog wording.
- Cross-check of all 17 achievement registry entries and the Alien Infantry contribution to `combined_arms_redefined`.
- Cross-check of provider 508 family constants, registration, materialization, commit/rollback, cleanup, and legacy-refund isolation.
- Current event inspect/render attempts on `.40-.47`, Event 019, super-events, and aftermath, with exact partial/error/timeout results retained above.
- Current Alien Infantry technology inspect/render attempts and predictive-technology inspect/render attempts, with partial/timeout results retained above.
- Review of the latest 3D action, source/licence, reimport, muzzle, audio, counter, and portrait handoffs.

Missing or blocked:

- A fresh completed probability audit of the current rebellion file hash; the prior 10/20/40 artifact is historical evidence only.
- Complete MCP mission/decision AI evidence for Kruger/Mengele authorization, Honor Accord, landing target selection, and Event 019 provider selection/cleanup.
- A special-project AI/timing adapter for `sp_dhrondan_envoy_craft`.
- Complete helper-expanded MCP resolution for three `.40-.47` helpers.
- Current successful Event 019 render, super-event render, and aftermath inspect/render.
- Baseline-backed event/technology comparisons.
- A complete seven-action Alien Infantry package, supported muzzle locator, synchronized particle/light/audio, parent entity wiring, and user live acceptance.
- Live fire-once registry, four-evolution scheduling, event-log actor/detail, achievement eligibility, super-event queue/world-end lock, aftermath, landing conservation, provider-508 isolation, rebellion transfer, and multi-component enclave acceptance.

## Remaining blockers and recommended next actions

1. Keep Event 016 marked incomplete until the 3D owner supplies four distinct accepted actions, a supported verified muzzle locator, actual-byte reimports for the full set, synchronized particle/light/audio evidence, and a parent-wired `alien_infantry_entity` package.
2. Re-run `chaosx_ai_probability_auditor` only after MCP availability is stable, using the current rebellion file hash and the named low/medium/high boundary scenarios. Do not reuse the 2026-08-22 source hash as current proof.
3. Re-run contact `event_inspect`/`event_render` after the helper catalog can index the three source-defined helpers. Add a baseline only if a real preserved revision exists; do not fabricate one.
4. Re-run Event 019 provider-508 present/absent/cleanup/rollback scenarios and obtain a successful current render of `chaosx.nr19.1`.
5. Re-run Event 016 super-event and aftermath inspect/render, then verify queue one-shot behavior, actor cleanup, world-end lock ownership, and `.301-.318` reachability.
6. Retain exactly four Event 016 evolutions, no cluster, exactly six existing visible super-event packages, and the current 17 achievements. Do not add a DHR evolution, cluster, super-event, or achievement without a new accepted design change.
7. Reconcile or annotate the stale core runtime/model/provider documents so future agents do not revive superseded approval, credit, provider-522, no-model, or enclave-conflict blockers.

## Final classification

- **Finished:** accepted DHR portrait package; Alien Infantry 2D counter/icon family; no-cluster classification; four-evolution and 17-achievement source inventory; source-level provider-508 migration; source-level technology/project ids; accepted 10/20/40 rebellion design; accepted more-than-15 enclave rule.
- **Partial:** `.40-.47` engine evidence; fire-once registry proof; event log/details; DHR continuation `.48-.52`; Event 019 lifecycle; technology/project MCP proof; super-events/world-end/aftermath; achievement eligibility; current weighted-probability acceptance.
- **Blocked:** full Alien Infantry runtime model/entity, four semantic actions, muzzle locator, synchronized fire effects/audio, current successful provider/super/aftermath renders, fresh current probability proof, and all live consumer acceptance.
- **Design gap:** none identified for a DHR cluster, fifth evolution, DHR-specific super-event, or DHR-specific achievement; those additions are outside the accepted design.
