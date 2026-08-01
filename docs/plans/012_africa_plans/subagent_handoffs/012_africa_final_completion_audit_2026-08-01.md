# Event 012 Africa final completion audit

Date: 2026-08-01

Status: **Incomplete. No hard static load blocker was found, but accepted gameplay, presentation, and acceptance work remains open.**

Mode: Read-only completion audit.

Audited revision: current Event 012 source at `e50e59c33`; the Event 012 scoped source is clean against that revision.

The requested commits `70ab0821b`, `79dbdbac7`, `b812329ed`, `08da3e4cc`, `919bb76ec`, `444dadccb`, `d03017bb5`, and `9749bf37c` are ancestors of the audited revision.

The shared worktree also contains unrelated Event 016, Event 020, fallout, workbook, and catalog-export changes; those changes were not treated as Event 012 gameplay evidence.

## 1. Executive verdict

Event 012 is a broad source implementation with a coherent playable core, but it is not a completed release package.

The entry event, core Charter state machine, full action inventory, focus-tree inventory, priority-package scaffolding, RSA and diaspora branches, W0-W4 world-order source, event-log/detail/evolution surfaces, localisation coverage, achievement registry, AI registry, and most registered 2D presentation assets exist.

Completion is blocked by W5 initial certification, thirteen priority-package end-to-end acceptance paths plus three dormant package/host bindings, achievement owner and lifetime-disqualifier closure, two AI acceptance blockers, unresolved action/runtime acceptance, missing model packages, incomplete four-role super-event audio, external-package identities, native-language review, branch-aware focus/UI acceptance, and committed catalog/spec promotion.

The current source itself describes the same boundary: `docs/events/012_africa/overview.md` does not claim gameplay, live behavior, or presentation completion, and `docs/plans/012_africa_plans/012_africa_final_improvement_loop_addendum_2026-08-01.md` marks implementation and acceptance open.

## 2. Hard load-safety result

No hard Event 012 load-safety blocker was found in the bounded static audit.

- All 493 Event 012 custom GFX references resolve against mod or vanilla sprite definitions.
- Every texture path referenced by the Event 012 GFX definitions resolves to an existing mod or vanilla file.
- All 32 distinct referenced `chaosx.nr12.*` event IDs have definitions.
- All eight referenced focus-tree load targets have definitions: `africa_continental_focus_tree`, `africa_priority_member_focus_tree`, and the six external continent trees.
- The current Event 012 localisation audit covers 17 files and 4,140 keys with zero duplicate groups, zero missing keys among 1,390 source references, and complete required localisation for 405 executable focus IDs, 80 ideas, 44 achievements, and 16 characters.
- The two repaired Charter animations have registered static fallbacks and existing final DDS paths.
- Existing narrow HOI4 event inspections returned partial/deferred large-workspace analysis with no blocking Event 012 diagnostic; the focus inspection resolved all 276 continental focus titles and reported layout diagnostics rather than a parser failure.

Limits: this was not an engine launch, live campaign, GUI click, sound playback, model reimport, or branch-aware focus render.

## 3. Completion status by surface

| Surface | Status | Evidence and disposition |
| --- | --- | --- |
| Registration, fire-once identity, and host ownership | Source-complete; runtime acceptance open | Event 012 retains the `chaosx.nr12.1` entry identity, Minor Fire-Once catalog classification, active-pool registration, one committed global host, and host-preserving shared effects. Original SAF has a narrow accepted entry exception that preserves `south_african_focus`. No duplicate event-ID or missing load-target defect was found. |
| Host playbooks | Partial | The 51-row matrix contains 22 full dossiers and 29 compact signatures. The acceptance ledger marks 48 implemented and three blocked: Basutoland `HZX`, Swaziland `EUX`, and Zanzibar `ELX` have no accepted unique current-state binding. No substitute tag is authorised. |
| Protection-first Charter | Source-complete; acceptance partial | Protected, Associate, Chartered, Federal, Outside, Resistant, Leaving, and Rival states, clauses, confidence, exit/refusal, and rival behavior exist. The scripted GUI exposes the core state and recurring families, while six late or episodic families remain list-only by documented design. Live state transitions and click regions remain unaccepted. |
| 102 actions | Partial | All 102 matrix rows have a source profile, nonzero cost or resource contract, duration contract, AI route, outcome, and cleanup disposition. The ledger marks 90 implemented and 12 `blocked_with_gate`: rows 73-76 and 85-92. Only 12 rows use a meaningful objective class; the remaining timed rows mostly use the shared duration/outcome kernel. Four shared targeted missions rely on `days_mission_timeout = FROM.africa_active_action_duration_days`, for which the audits found no exact vanilla precedent or live parser confirmation. |
| Action-specific mechanics | Simplified and partly blocked | Most rows use generic full/partial/failure semantics with narrow bespoke effects rather than a unique objective system per action. Disease review remains API-gated, strange formations remain model-gated, and world actions remain package/W5/terminal-gated. If war ends during the natural-disaster mission, the weapon safely does not fire, but the paid action falls into the ordinary outcome path; a dedicated refund/failure policy is unresolved. |
| Focus trees and 78 payoffs | Source-complete except one queued payoff; visual/AI acceptance open | The continental tree has 276 focuses, nine six-node regional overlays, seven constitutional routes, 36 support nodes, 26 host/formation nodes, and 16 shared opening nodes. The priority overlay has eight nodes and the six world trees have 121 nodes. Static inspection found no dangling prerequisites or mutual exclusions. The ledger marks 77 payoff rows implemented and one external-world payoff queued. |
| Focus AI and layout | Simplified / unaccepted | There are 107 flat main route-body `ai_will_do` blocks. Route strategy plans mitigate but do not replace row-level feasibility and crisis weighting. The static MCP layout inspection reports 570 blocking diagnostics, 1,028 intersections, 448 crossings, and 37 long connectors because mutually exclusive overlay templates reuse coordinates. The inspector is not branch-aware, so this is neither accepted runtime layout nor proof of a runtime defect. |
| Seven constitutional identities | Asset/source-complete; runtime acceptance open | All seven routes have three flag sizes, stable sprite registrations, and route emblems. No missing file was found. Runtime identity switching and presentation were not accepted in a live consumer. |
| 215-polity pool | Controlled pool, not implementation-complete | The catalog contains 52 Tier A, 98 Tier B, and 65 Tier C candidates, including 207 grounded and eight explicitly fictional candidates. The ledger intentionally leaves 199 queued and 16 blocked. The pool does not promise 215 runtime tags, and no empty or invented fallback tag is authorised. |
| Sixteen priority packages | Source-present; acceptance blocked | Characters, ideas, focus payload, decisions, bounded forces, localisation, and sprites exist for all 16. Thirteen have current carrier paths: four Event 006 mappings and nine vanilla carriers. Luba `DYX`, Lunda `DZX`, and Kilwa `EMX` remain dormant because no accepted unique binding exists. All 16 ledger rows remain blocked pending origin, formation/release, runtime, and provenance acceptance. |
| Event 006 carrier integration | Partial | Asante `DOX`/state 274, Oyo `DSX`/558, Kanem-Bornu `DUX`/901, and Zulu `EQX`/719 have current Event 006 receipt paths. No new tags were added. The carrier loaders preserve meaningful trees and completed focus history where allowed. |
| RSA | Source-complete; runtime acceptance open | Original SAF can enter through the narrow Allied-rupture gate, preserves `south_african_focus`, and calls the public civil-war effect once. Opening, three settlement, exile, and no-patron log payloads exist. Civil-war, settlement, exile, and weighted candidate behavior lack live acceptance; the weighted selector can choose an RSA candidate before the frozen-roster patron test and then reject it without a fallback. |
| Diaspora | Source-complete; UI/runtime acceptance open | Consent, counterterms, refusal, withdrawal, emergency, capacity, skills, citizenship, representation, and local-ownership writers exist. Temporary targets are cleaned up. The route is voluntary and has no forced-relocation fallback. The Charter GUI does not expose the newer capacity lanes, although the action surface remains usable. |
| Baseline and Evolutions I-III | Source and current catalog present; committed catalog stale | Baseline tier 4, Evolution I tier 4, Evolution II tier 5, and Evolution III tier 6 content exists. Evolution IV was deliberately recast as post-unification state rather than an extra event-log row. The current dirty workbook/export row contains the three evolutions, cluster metadata, `Needs Testing`, and the gated World scenario; the committed `HEAD` CSV contains only Evolution I and leaves the later event metadata blank. |
| Scramble | Source-complete; scenario acceptance open | Five interest classes, a bounded coalition, material outcomes, and Africa-only closure exist. The final launch validator prevents an unsafe declaration, but participant ranking does not prove naval/deployable strength, ports, distance, or material readiness and can starve viable candidates. Several classification subhelpers are definition-only, suggesting an inlined implementation or stale scaffolding. |
| W0-W5 and terminal World | W0-W4 source-complete; W5 blocked | W0-W4 include roster, consent/refusal/counterterms/withdrawal/coercion, six continent loops, four sponsorship modes, union, war, succession, exile, breakup, and terminal lifecycle. There is no initial all-six certification trigger/setter for W5. The only writer of `africa_world_package_implementation_ready` serves successor continuity, not initial package certification. `africa_the_world_super_event_package_ready` remains unset. |
| 44 achievements | Registry/art complete; gameplay acceptance blocked | All 44 definitions, localisation triplets, and 132 three-state DDS files exist. The shared ledger still marks all 44 blocked. The latest B3 work gives narrow evidence for row 24 and row 28, and row 24 now has a bounded direct-host capitulation caller; live victory acceptance remains open. Rows 30, 32, 33, 37, and 38 retain exact-owner gaps; row 37 deliberately fails closed because the civilian-damage owner does not exist. Four rows are model-gated and row 44 is terminal-gated. |
| 64 AI profiles | Static registry complete; acceptance blocked | All 64 profiles have exact predicates, loader/registry calls, and action revalidation: nine overlays, 22 hosts, seven routes, eight member/rival, five external, six high-chaos, and seven world profiles. Profile 42 is the intentional terminal exception. The Scramble material-readiness/rank-starvation issue and the strategy-plan probability adapter's `PROBABILITY_SURFACE_EMPTY` result remain blockers. No 64-scenario campaign proof exists. |
| 239 asset rows | Fully dispositioned, not fully delivered | The authoritative matrix records 50 `installed_runtime`, 21 `installed_dormant`, 133 `deferred_controlled_pool`, 12 `deferred_runtime_gated`, 16 `deferred_model_required`, and seven `deferred_unique_package_required`. No matrix row is undispositioned, but 168 rows remain deliberately deferred. |
| Charter animations | File-complete; runtime acceptance open | The seal is an eight-frame 512x64 sheet at 8 fps and the authority ring is a ten-frame 640x64 sheet at 6 fps. Source frames, final DDS files, registrations, static fallbacks, parity/header/alpha/checksum evidence, and a handoff exist. Runtime animation, scaling, and click proof remain user-owned. |
| Four super-event roles | Partial / blocked | The four image/text roles have documented presentation surfaces. Audio 59 and 60 exist as runtime WAVs and sound registrations but remain dormant because the four-role package is atomic. Audio 58 and 61 lack commissioned original lossless masters and rights-chain evidence. No role is accepted as runtime-wired, and the terminal role remains separately blocked by W5 and presentation readiness. |
| Localisation, event log, details, evolutions, cluster UI | Source-complete with wording/native-review gaps | Required keys resolve and the 2026-08-01 collision repair removed the identified world-order duplicate-key conflict. Exact Afaan Oromoo strings remain absent pending native review. Some player-facing world-order strings still expose implementation language such as ledger, array, target-pool, dossier, or fallback concepts, and action objective class is not exposed as a dynamic player-facing label. |
| Documentation, workbook, and exports | Partial / stale committed state | The overview, subsystem documents, handoffs, asset matrix, and acceptance ledger reflect the current blockers. The final improvement addendum remains active and has not been promoted into a fully accepted source spec. The current workbook and three exports share a 2026-08-01 generation timestamp and the current Event 012 CSV row is populated, but those files are dirty in the shared worktree and the committed Event 012 CSV row is stale. |

## 4. Exact model and unique-package needs

No model package was found or accepted for any of the 16 `deferred_model_required` rows.

The six missing country visual/model packages are:

- `country_package_pan_high_chaos`
- `country_package_gorilla_kingdom`
- `country_package_the_green`
- `country_package_living_rivers`
- `country_package_stoneborn`
- `country_package_ancient_hosts`

The ten missing unit/model identities are:

- `unit_identity_elephant_logistics`
- `unit_identity_elephant_shock`
- `unit_identity_gorilla_heavy_infantry`
- `unit_identity_pan_sappers`
- `unit_identity_stone_cohorts`
- `unit_identity_riverborn`
- `unit_identity_forest_giants`
- `unit_identity_oracle_recon`
- `unit_identity_disaster_wardens`
- `unit_identity_plague_carriers`

The seven separately deferred unique identity packages are `continent_package_middle_east`, `continent_package_europe`, `continent_package_asia`, `continent_package_north_america`, `continent_package_south_america`, `continent_package_oceania`, and `continent_package_the_world`.

These absences are real completion blockers for their specified consumers; they are not hard load failures because the runtime gates remain closed.

## 5. Accepted-plan disposition

The July 30 non-model world-package addendum is implemented through W4 in source, but that disposition has not been fully promoted into the source specification.

W5 is promoted into the 2026-08-01 final improvement addendum and remains unimplemented because authoritative pre-install receipts are absent.

The final B1-B5 plan remains active:

| Tranche | Disposition |
| --- | --- |
| B1: W5 atomic political-package certification | Blocked; no initial certification trigger or setter and no authoritative six-package receipts. |
| B2: Charter, overlays, constitutions, and thirteen reachable priority packages | Source-present; end-to-end acceptance and provenance remain open. Three additional package/host bindings remain dormant. |
| B3: achievement exact owners and disqualifiers | Partial; row 24 and row 28 were narrowed, row 24 has a bounded capitulation owner, but rows 30, 32, 33, 37, and 38 remain unresolved. |
| B4: AI, focus, Scramble, package, and terminal scenarios | Static checks only; two AI blockers, focus layout ambiguity, package readiness, and terminal scenarios remain open. |
| B5: localisation, log, docs, ledger, specs, workbook, and final audits | Docs and ledger were reconciled; native-language review, player-facing wording, spec promotion, clean committed workbook/export alignment, and final acceptance remain open. |

No accepted blocker is safely disposable as “future polish.”

## 6. Highest-confidence bounded non-model tranche

The strongest bounded next gameplay tranche that does not require new tags, models, or external-package receipts is **B3 achievement owner/reachability closure for existing non-model, non-world systems**.

The exact highest-confidence B3 owner is `africa_priority_member_record_rival_bloc_victory`, which now has a bounded `on_capitulation` caller when a rival priority member directly defeats the current host. The remaining gap is live positive/disqualifier acceptance, not a missing source callsite.

The same patch tranche should either wire or explicitly retire the currently definition-only non-model achievement owners whose gameplay systems already exist, especially `africa_achievement_record_development_project`, `africa_achievement_record_diaspora_owned_project`, `africa_achievement_record_disease_outbreak_contained`, `africa_achievement_record_elephant_protection_victory`, `africa_achievement_record_elephant_supply_proof`, `africa_achievement_record_elephant_terrain_region`, `africa_achievement_record_reserve_war_answered`, `africa_achievement_record_socialised_resource_project`, and `africa_achievement_record_weather_army_defeated`.

Rows 30, 32, 33, and 38 need exact accepted owner outcomes before their recorders can be wired.

Row 37 must remain fail-closed until a real civilian-damage owner exists; creating a proxy from action use or war start would be a forbidden simplification.

This auditor did not implement that patch because gameplay edits are outside the read-only event-completion-auditor role and the exact owner outcome for each remaining row must be approved rather than inferred.

## 7. Meaningful validation evidence and missing validation

Performed or reused against the current Event 012 source:

- Commit ancestry and Event 012 scoped-worktree checks.
- Event-ID definition/reference closure and focus-tree load-target closure.
- Mod-plus-vanilla GFX definition closure and texture-path existence checks.
- Current Event 012 localisation duplicate, source-reference, scripted-localisation, focus, idea, achievement, and character coverage audit.
- Matrix and acceptance-ledger counts for all eight required surfaces: 102 actions, 44 achievements, 64 AI profiles, 78 focus payoffs, 51 host playbooks, 215 polity candidates, 16 priority packages, and 239 asset rows.
- Static reachability scan of 1,285 Event 012 top-level scripted effects, triggers, and MTTH definitions.
- Existing narrow MCP event, focus, decision/probability, and GUI evidence where it was task-specific.
- Current-versus-committed catalog comparison for Event 012.

Still missing and materially relevant:

- Engine parser confirmation for the dynamic `FROM` mission timer path.
- One-pass registration/fire-once/host transfer runtime proof.
- Branch-aware focus layout acceptance and route-by-route focus AI behavior.
- Charter GUI runtime scaling, animation, click, and late-family accessibility proof.
- All 64 AI scenario bands with rank, starvation, target retry, and terminal isolation evidence.
- Scramble participant material-readiness and coalition outcome scenarios.
- Thirteen reachable priority-package formation/release/player/AI acceptance scenarios.
- RSA civil-war, settlement, exile, and no-patron scenarios.
- Diaspora consent/counterterm/refusal/withdrawal and capacity-lane scenarios.
- Achievement positive, disqualifier, loss, host-transfer, and cleanup scenarios.
- W5 six-package initial certification and terminal World lifecycle proof.
- Model creation, Blender/PDX export, reimport, entity consumer, and runtime scale evidence for all 16 model rows.
- Four-role super-event audio dispatch, playback, licensing, and terminal gating evidence.
- Native-language review and clean committed workbook/export synchronization.

## 8. Simplifications, omissions, and blockers

- Three of 51 host playbooks are blocked rather than substituted.
- Thirteen priority packages are reachable but unaccepted; three are dormant.
- The 215-polity catalog remains a controlled candidate pool, not 215 implemented countries.
- Ninety action rows rely primarily on shared timing/outcome behavior; only 12 use an explicit objective class.
- Twelve action rows remain gated.
- One of 78 focus payoff rows remains queued.
- One hundred seven route-body focuses retain flat AI factors.
- Six Charter late/episodic families are list-only.
- W5 and the terminal World presentation are not implemented or certified.
- All 44 achievement rows remain blocked in the acceptance ledger despite complete registry/localisation/art.
- All 64 AI rows remain blocked pending scenario evidence.
- One hundred sixty-eight of 239 visual rows remain deferred, including all 16 model rows and seven unique package rows.
- Two of four required super-event audio masters are absent, and the completed two remain dormant under the atomic gate.
- Exact Afaan Oromoo localisation is absent pending native review.
- Current workbook/export content is not cleanly committed, while the committed Event 012 catalog row is stale.

No fallback tag, proxy achievement owner, substitute model, generic continent identity, unlicensed audio, or silent readiness setter was accepted.

## 9. Definition-only helper appendix

The static scan found 52 top-level Event 012 helpers with no literal source reference outside their definition.

This is a reachability warning, not a blanket load failure: some names can be compatibility hooks, planned dynamic entry points, or remnants of inlined logic.

The achievement recorders, first-proof orchestration, RSA proof helpers, package cleanup, and terminal cleanup need explicit owner disposition before completion. The priority rival-victory wrapper has an explicit source owner but remains live-acceptance gated.

1. `africa_achievement_record_development_project`
2. `africa_achievement_record_diaspora_owned_project`
3. `africa_achievement_record_disaster_weaponised_against_civilians`
4. `africa_achievement_record_disease_outbreak_contained`
5. `africa_achievement_record_elephant_formation`
6. `africa_achievement_record_elephant_protection_victory`
7. `africa_achievement_record_elephant_supply_proof`
8. `africa_achievement_record_elephant_terrain_region`
9. `africa_achievement_record_forced_relocation`
10. `africa_achievement_record_forced_scenario`
11. `africa_achievement_record_other_world_end`
12. `africa_achievement_record_reserve_war_answered`
13. `africa_achievement_record_socialised_resource_project`
14. `africa_achievement_record_weather_army_defeated`
15. `africa_achievement_record_world_terminal_super_event`
16. `africa_ai_policy_is_protection_first`
17. `africa_breach_first_proof_corridor`
18. `africa_breach_first_proof_no_coercion`
19. `africa_breach_first_proof_sovereignty`
20. `africa_confirm_all_required_first_proof_regions`
21. `africa_confirm_first_proof_domestic_settlement`
22. `africa_confirm_first_proof_reform`
23. `africa_focus_can_continue_grounded_route`
24. `africa_focus_route_ensure_continental_tree_loaded`
25. `africa_has_current_host`
26. `africa_has_living_core_project_capacity`
27. `africa_has_opening_contact`
28. `africa_is_compact_host_playbook_country`
29. `africa_is_full_host_playbook_country`
30. `africa_prepare_first_contact_targets`
31. `africa_priority_member_cleanup_runtime`
32. ~~`africa_priority_member_record_rival_bloc_victory`~~ (now caller-backed by the bounded direct-host capitulation owner)
33. `africa_promote_compact_host_package`
34. `africa_register_first_contact_regional_power`
35. `africa_register_first_contact_subject`
36. `africa_register_first_contact_threatened`
37. `africa_reset_compound_first_proof_ledger`
38. `africa_rsa_allied_settlement_is_complete`
39. `africa_rsa_civil_war_first_proof_satisfied`
40. `africa_scramble_participant_fears_other_continent_unifier`
41. `africa_scramble_participant_has_former_colonial_relationship`
42. `africa_scramble_participant_has_resource_nationalisation_exposure`
43. `africa_scramble_participant_has_south_africa_allied_relationship`
44. `africa_scramble_participant_is_coalition_member`
45. `africa_scramble_participant_is_ideological_rival`
46. `africa_select_mapped_first_proof_action`
47. `africa_world_constituent_can_accept_counterterms`
48. `africa_world_constituent_can_refuse_counterterms`
49. `africa_world_order_route_is_diplomatic`
50. `africa_world_package_is_resolved`
51. `africa_world_package_is_sovereign_complete`
52. `africa_world_terminal_protocol_cleanup_after_identity`

## 10. Recommended next actions

1. Continue the bounded B3 tranche by validating the direct-host rival-victory owner and then resolve rows 30, 32, 33, 37, and 38 without proxy milestones.
2. Run focused decision/event inspection after that patch and reconcile the 44-row achievement ledger rather than bulk-promoting it.
3. Obtain the authoritative six-package receipts before implementing B1 W5 certification; do not infer readiness from source existence.
4. Run the thirteen reachable priority-package and 64-profile acceptance scenarios, including Scramble material-readiness/rank-starvation and terminal isolation.
5. Produce the 16 required model packages through the approved 3D pipeline and obtain the seven unique external identity packages.
6. Complete audio 58 and 61 with rights evidence, then validate all four super-event roles atomically.
7. Finish native-language and player-facing wording review, promote accepted W0-W5 rules into the source specs, and commit the authoritative workbook plus regenerated exports together.
8. Rerun the focus, decision, country-package, localisation, and final event-completion audits before any completion claim.

Final disposition: **Event 012 Africa is incomplete. The current runtime-gated source is statically load-safe within the audited scope, but the accepted design is not fully implemented, promoted, or validated.**
