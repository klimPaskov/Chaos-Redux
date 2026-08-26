# Event 014 documentation state

Status date: 2026-08-26 approved vanilla-visual reuse amendment and parent runtime-wiring continuation.

This ledger is the current documentation map for Event 014 and is limited to documentation evidence, read-only MCP evidence, manifests, and parent-owned handoffs.

## Current source-of-truth facts

- Event root: `chaosx.nr14.1`.
- Classification: Minor Fire-Once, outside every cluster, with no cluster assignment.
- Origins: Island Host, Siege Commune, and March Host only.
- Prison Host is rejected as an origin, country package, portrait slot, focus route, decision route, scenario type, GUI surface, or super-event identity.
- Prison, detention, depot, and prisoner ledgers remain ordinary objectives or logistics and do not define a fourth origin.
- Hannibal Lecter is a concealed coordinator until `cannibalism_reveal_complete`.
- Before reveal, player-facing text, portraits, flags, focus and decision labels, GUI, Event Details, achievements, scenario text, reports, news, super-events, and audio metadata use neutral network, Host, cell, island, siege, commune, or military language.
- After `cannibalism_reveal_complete`, ordinary and Wendigo public reveal transactions may name Hannibal Lecter and expose the approved identity assets.
- Nine gameplay formation families are current: `cannibal_scavenger_warband`, `cannibal_feast_guard`, `cannibal_feast_cohort`, `cannibal_bone_guard`, `cannibal_bone_riders`, `cannibal_island_reavers`, `cannibal_siege_eaters`, `cannibal_march_predation_column`, and `cannibal_network_cadre`.
- The eight foot families share `category_cannibal_irregular_infantry`; Bone Riders is the separate horse-mounted mobile family with the same Event 014 irregular category and real infantry-equipment need.
- Seven families now have parent-installed bespoke mesh, eight-action, entity/GFX, material-map, and runtime sound packages: Feast Guard, Feast Cohort, Bone Guard, Siege Eaters, March Predation Column, Island Reavers, and Scavenger Warband. Bone Riders intentionally uses vanilla `sprite = cavalry`, and Network Cadre intentionally uses vanilla `sprite = infantry`; neither requires an Event 014 custom model, action, entity, or provider package.
- Scavenged Elephant Column uses installed vanilla `elephantry` and adds no Event 014 elephant sub-unit, elephant model, elephant counter, or equipment archetype.
- The current GUI contract has no animation toggle or player animation preference.
- Model inputs must begin with actual Internet-sourced or user-supplied modern game, concept, tabletop, miniature, fantasy, horror, or professional character artwork.
- ImageGen may only perform faithful resolution, alpha, background, padding, or edge cleanup and may not redesign, re-costume, invent missing components, or create a from-scratch descendant for Meshy.
- Feast Guard is the current approved source exception at `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/refs/source/untouched.png` with faithful approved input SHA-256 `C67AF852A27E1379590BD84C5175C378D449AE226F895A2D326B45099040D8C9`.
- The previous generated or substantially redesigned Feast Guard input with SHA-256 `6ACD1D8D9CF4AFE408F8D1EAE8F59BA72CA7E0B8B35B9BCE2E84DC7D37EB8092` is superseded evidence only.

## Authority order

1. Current accepted source specs under `docs/specs/014_cannibalism_specs/`.
2. `docs/events/014_cannibalism/overview.md` for the current event overview and implementation boundary.
3. Current unit/model plan and source-direction amendment under `docs/plans/014_cannibalism_plans/`.
4. Current asset manifests and counter, audio, model, animation, and super-event handoffs.
5. Read-only implementation evidence and fresh MCP artifacts, which describe what is present without changing the intended design.
6. Historical audits, old plans, and superseded handoffs, which remain evidence only when their top notices say so.

## Surface map

| Surface | Current authority | Current state | Boundary or unresolved item |
| --- | --- | --- | --- |
| Event classification and root | `README.md`, spec part 1, event overview | Minor Fire-Once and outside clusters | Fresh MCP inspection is partial because the workspace is large. |
| Hidden identity and reveal | `hidden_identity_surface_audit.md`, `anti_spoiler_audit.md`, event overview, package validation | Neutral pre-reveal language and reveal-gated public identity | No new leak claim is made by this documentation audit. |
| Portrait package | `docs/assets/014_cannibalism/portrait_source_recovery_v6/`, `event014_portrait_handoff_audit_2026-08-25.md`, package validation | 56 portrait files are present in the runtime tree | Portrait-worker acceptance, durable source/rights receipt, static Hannibal provenance, and live review remain open. |
| Origins | spec part 4, `014_removed_origin_cleanup_2026-07-15.md`, event overview | Three origins only; Prison Host rejected | Historical fourth-origin plans remain marked as superseded. |
| Nine gameplay consumers | event overview, README, spec part 4, irregular-unit plan, two unit implementation handoffs | Definition-level consumers and CXT registration are current | Parent owns live test-country and in-game consumer validation. |
| Elephantry separation | Bone Riders implementation handoff and spec part 4 | Vanilla `elephantry` only in Scavenged Elephant Column | No custom elephant model or counter is authorized. |
| Counter art | `event014_cannibal_counter_art_handoff.md`, `docs/assets/014_cannibalism/manifest.md`, `gfx_handoff.md` | Nine triplets and 27 DDS textures with registry consumers are present | Live consumer review remains parent or user-owned. |
| Humanoid model jobs | irregular-unit model plan, source-direction amendment, per-job manifests and handoffs, `docs/assets/014_cannibalism/models_3d/family_jobs.json` | Seven packages are parent-installed with Meshy/Blender evidence; Bone Riders and Network Cadre use the approved vanilla-visual simplifications. Scavenger Warband v2 is documented in `event014_scavenger_warband_v2_runtime_handoff.md`, and Island Reavers v11 remains documented in its corresponding handoff | Live in-game validation is not claimed for the seven bespoke packages; there is no remaining custom-model blocker for the two vanilla-reuse consumers. |
| Bone Riders visual consumer | `event014_unit_visual_reuse_2026-08-26.md`, `models_3d/family_jobs.json`, event overview, spec part 4 | Gameplay profile remains distinct and resolves to vanilla `sprite = cavalry` | No Event 014 custom model, action, entity, provider, or reimport output is required. |
| Network Cadre visual consumer | `event014_unit_visual_reuse_2026-08-26.md`, `models_3d/family_jobs.json`, event overview, spec part 4 | Gameplay profile remains distinct and resolves to vanilla `sprite = infantry` | No Event 014 custom model, action, entity, provider, or reimport output is required. |
| Unit audio | per-job manifests, `sound/014_cannibalism_units_sound.asset`, `sound/014_cannibalism_voices.asset`, and `event014_remaining_unit_audio_runtime_wiring_2026-08-25.md` | Seven bespoke model packages contain their converted 44.1 kHz WAV files, and country-level voice definitions cover the gameplay family set | Model-specific action synchronization applies only to the seven bespoke entities; retained audio records for the two vanilla-reuse consumers are lineage or optional country-level evidence, not custom-model gates. |
| Super-event media | `docs/specs/014_cannibalism_specs/matrices/super_event_matrix.md`, `docs/super_events/014_cannibalism/audio_research.md`, and `subagent_handoffs/event014_super_event_audio_wiring_audit_2026-08-25.md` | Four audio/image packages are source-side documented; all four audio tracks are registered and dispatched through the settings-aware helper | Distinct image registration and live presentation review remain parent-owned. |
| Weighted logic | `subagent_handoffs/event014_probability_final_2026-08-25.md`, fresh `hoi4_probability_inspect` discovery | Scenario-specific evidence exists, but the fresh adapter discovery returned no available scenario adapters or candidates | Named scenario sweeps, comparisons, and final probability sign-off remain incomplete. |
| Catalog workbook | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and its spreadsheet audit handoffs | `Events!N15` and `Scenarios!F10` remain `Needs Testing` | The spreadsheet worker owns the workbook and this documentation pass did not edit it. |
| Animation | frame-animation package docs and model action contracts | Existing Event 014 frame packages remain asset-level evidence; seven bespoke model action sets have source-side evidence and Bone Riders/Network Cadre intentionally use vanilla animation families | No Event 014 animation preference or toggle is part of the GUI contract. |
| MCP event evidence | Fresh `hoi4_event_inspect` and `hoi4_event_render` read-only calls | No blocking diagnostics in the partial inspect/render result | Large workspace deferred full validation and omitted most graph nodes. |

## Fresh MCP evidence

- Read-only event lint selector: `chaosx.nr14.1` in workspace `mod_chaos_redux`.
- Fresh revision: `2be037dcc94803edc8cb5041f6189ce00f20ffcb12543926a795f54690c2589f`.
- Fresh graph hash: `13ffe35a55f25cea00da198b46b6bcdb5aed8bdffe8bfbe992755aecf821a7e0`.
- Lint result: `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and an inline-file truncation information diagnostic.
- Partial counts: 9,513 events, 14,705 options, 1,071 entries, 8,289 unresolved references, 7,652 terminals, 37,122 edges, and 2,130 issues in the deferred large-workspace scan.
- Lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/175f05b6d3b92978cc10f967f081cc4afbd9dda00d335f70b4d22cecbb5e1ffb/89ff239609591feb0531d58897fdbe15a9711205cf1cc962b369f7cb44c0abb1/event-lint-2be037dcc948.json`.
- Fresh overview render result: partial, selected nodes 2, omitted nodes 41,228, and no branch renders.
- Overview render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fd5b04db8c36fb6ecc55db18e37d8b0b4d0e5f7496dbd120ed3711cdee903c2/d1dab8bc0624457af4e235650a0d31b8a5e89f92dbe1f5c9110181cb6a6449a0/event-overview-2be037dcc948-manifest.json`.
- Overview render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd9b40fd8ed27037d9b51a4bced874d0715373d1c376b297829fefd313a71aed/7b2718b94d70100494e7194b03897adca61c3ff1ea6c096b54ae674ea02321f/event-overview-2be037dcc948.json`.
- Overview render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3df54e046c4e8789cb9dd3dc7f9f7400d34e746934d9e65d4da6ac80b3dbf289/e743d20dea26d752da843add7ddf3f33d1c88c9753d6c1b5f00d5837aefed392/event-overview-2be037dcc948.svg`.
- Overview render PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c05dea7aaeae3eb267fb51bf26f3d20cd62260ceb04d7270230db476abfc9daf/1139494a36826727270ca9403f2c2c1fedfa1c72e4b1bf90d4a1c1d7d3cec74c/event-overview-2be037dcc948.png`.
- MCP evidence is engine evidence for the inspected partial surface only and does not prove model, audio, counter, live GUI, or in-game completion.

## 2026-08-26 continuation MCP evidence

- Read-only `hoi4_event_inspect` lint selector: `chaosx.nr14.1` in workspace `mod_chaos_redux_ea3b2d67c2c0`.
- Fresh revision: `43388d6b2737a1c8e2409f324449210941414fee69c903a1c69d441ca9d33b97c`.
- Fresh graph hash: `dd30c3585ea090f05881b49253cfb4212d58091d19729649a292f8ed561ed67c`.
- Lint result: `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and no skipped sources, while large-workspace projections remain deferred.
- Partial counts: 9,513 events, 14,705 options, 1,075 entries, 8,314 unresolved nodes, 7,651 terminals, 37,146 edges, 28,243 state accesses, and 2,130 issues.
- Lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2c984c9918d4dfb9ded16dd9f7d7863afeffa7c44ce146cd0c2377d747fe5cc/65cf2282b4c60d9512144056b76e3840c3afadcd244653256439864c4df670c9/event-lint-43388d6b2737.json`.
- This artifact is read-only engine evidence for the selected event boundary and does not prove model, portrait, audio, counter, GUI, probability, or live in-game completion.

## 2026-08-26 continuation surface MCP evidence

- A later narrow read-only `hoi4_gui_render` retry succeeded for `cannibalism_network_window` in scenario `event014_targeted_network_normal_2026_08_26`, normal state, and one `1920x1080` render coordinate (the adapter normalized the requested 1280x720 input to its 1920x1080 canvas). Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/14ca74fc2d4120165140404d28c9511d4875641c4e0c9d3e2bf34e517a22ca68/cannibalism_network_window-full.svg`.
- The response returned `GUI_RENDERED`, `status = ok`, no blockers, and no source changes. The wire response was truncated and reported no retained validation checks, so this single normal-state artifact improves evidence availability but does not close hover, disabled, long-text, click-region, multi-resolution, or comparison review.
- A second narrow normal-state retry succeeded for `cannibalism_warlord_command_window` under scenario `event014_targeted_warlord_normal_2026_08_26`; its attributable artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/356eda9a5565ef7475fbeca05d9002dcef5a8fbdc5f659787da7ef3a485f6ca7/9af633c47ddaca4dc7f034cafcffeff6e6ac8b249ed03730ab46099ba57fb1b7/cannibalism_warlord_command_window-full.svg`.
- This retry also returned `GUI_RENDERED`, `status = ok`, no blockers, and no source changes; the response was wire-truncated with no retained validation checks, so it improves normal-state evidence only and does not close the remaining visual matrix.
- A third narrow normal-state retry succeeded for `cannibalism_revealed_command_window` under scenario `event014_targeted_revealed_normal_2026_08_26`; its attributable artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f441cea9faf5d200fedd25fd95fadad86bb775973942db14d40b7501c6effc9/df0ccf706f92d513b64730a561c85c76bcd9282746356fddd9c46d6d47798f04/cannibalism_revealed_command_window-full.svg`.
- This retry returned `GUI_RENDERED`, `status = ok`, no blockers, and no source changes; its wire response was truncated with no retained validation checks, so it improves attributable normal-state coverage only.

- Read-only `hoi4_focus_inspect` calls covered the unified, warlord, and Wendigo Event 014 trees in `common/national_focus/014_cannibalism_focus.txt`.
- The unified tree returned `FOCUS_INSPECTED` at revision `7cdbef4cb9bc637558f7e082f80c3ca2ef529acef0e6af4d054dd2f639b99a02` with 108 focuses, 103 connectors, and zero crossings, intersections, long connectors, or blocking diagnostics; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bed446f8b88a1a95fc49121678f96d9fd0f209af10dbb74fa20885b136a017fe/eb1a39d75fd722e4b2820b58bfc1c49478219a3deea8deded2b33bd27b3333bc/focus-inspect.7cdbef4cb9bc6375.json`.
- The warlord tree returned `FOCUS_INSPECTED` at revision `72527e8e7a3af1b49503516a2a972de95e1b753f5d23def28b3c8ac2138c991a` with 68 focuses, 79 connectors, and zero crossings, intersections, long connectors, or blocking diagnostics; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0e834a8a1ca715bdc64aab0445fb3602f492a4c96d66fa472f88a32d9285270/67c9566b4600d013bdc830dc575779f7ee8fad5cbdc51a18f1548f72b2cd7268/focus-inspect.72527e8e7a3af1b4.json`.
- The Wendigo tree returned `FOCUS_INSPECTED` at revision `8409a1089534af92df876da74652411a99a84866c9f3c143725322b43ab55940` with 28 focuses, 28 connectors, and zero crossings, intersections, long connectors, or blocking diagnostics; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b18876d56c05ee1e9705cd3a24bfeb7cbd2d2284ad238f93d50cbcd9458690f8/31b22a8d4f143a7b99136d187895c2e73844beae295d97604dd8bdfaa6a6542b/focus-inspect.8409a1089534af92.json`.
- The focus adapter still reported non-blocking spacing information and one unrelated vanilla continuous-focus localisation warning; these calls do not prove gameplay, localisation, model, portrait, audio, probability, or live in-game completion.
- Read-only `hoi4_tech_inspect` unlocks calls covered `cannibalism_bone_riders_tech` and `cannibalism_network_cadre_tech` for their sub-unit targets and returned `TECH_INSPECTED_PARTIAL` at revision `80e9982c0e5ffadc246f8822e9310fbc4716330a93dd070bb3607d6003952ec3` with graph hash `50efcab3dae58bd7c0fd595f45632eb12f8371e5c5780fac109cc7f074aceb1e`; the reports contain 672 technologies, 850 unlocks, 4 unresolved items, and deferred helper projections.
- The Bone Riders technology artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35eed4850ffee8c5b7ecbeed921b05c22248b4dd83a29b1ad598327b49fd822f/145c610a1d3499d28d0806787eec6d66f6b33325c3c8bea9dea351d485db3c43/technology-unlocks-80e9982c0e5f.json`, and the Network Cadre technology artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7dd9b66f918a877fd26362921969d10505d5359eb17f89853e83be47e5f37a6d/0cf3e09335068f903d1913f82a512b81d5a9ec342e8dc4c226b9d4648d0e1794/technology-unlocks-80e9982c0e5f.json`.
- Read-only `hoi4_probability_inspect` listed 11 adapters but returned no available adapters, candidates, required inputs, or scenario artifact; no weighted-logic completion claim is made from this discovery response, and `event014_probability_final_2026-08-25.md` remains the scenario-specific evidence boundary.
- A fresh GUI-inspect retry was not accepted because the first request supplied `relatedScenarios` as strings where objects were required and the second omitted the required scenario paired with `windowName`; no new GUI artifact is claimed, and the bounded prior GUI artifacts remain the current evidence.

## 2026-08-26 model-folder cleanup evidence

- The current model documentation tree contains seven dedicated model-package folders and no `cannibal_bone_riders` or `cannibal_network_cadre` model-package folder after the approved vanilla-visual reuse cleanup.
- A runtime-source scan outside `docs/assets/` found no `docs/assets/.../provider`, `provider/downloads`, or `provider\\downloads` references.
- Historical handoffs, reports, and manifests may still name removed provider or download paths; those references are preserved as lineage-only evidence and are not runtime dependencies.
- `docs/assets/014_cannibalism/models_3d/family_jobs.json` and `vanilla_visual_reuse_2026-08-26.md` are the current asset-ledger authority for the seven bespoke packages and two vanilla-reuse consumers.

## 2026-08-25 continuation MCP evidence

- `hoi4_event_inspect` with selector `{kind: event, eventId: chaosx.nr14.1}` returned `EVENT_INSPECTED_PARTIAL` at revision `f588a2607444400ec9fa9d102943fc0e10dc4482ebca9935232a4df2966f59d5` with zero blocking diagnostics in the selected Event 014 boundary. The adapter deferred workspace-wide helper projections because the repository is large; the partial result reported 9,513 events, 14,705 options, 1,075 entries, 8,314 unresolved nodes, 7,651 terminals, 37,146 edges, and 2,130 issues in the deferred workspace scan. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/639f87ef1443400f555beedeace6f403bbcaeb6dd0744780524a9e97262dab2d/66d0e673d7ffa777cb0871473697fd7623db6a75e627dd1ce0598908225f17ec/event-lint-f588a2607444.json`.
- `hoi4_focus_inspect` returned `FOCUS_INSPECTED` with zero crossing, intersection, long-connector, and blocking diagnostics for all three Event 014 trees: unified 108 focuses and 103 connectors (layout hash `29064367ddef9fc917547f65c9cfe4dcf48cda240902f03eb18e51086e8cd364`), warlord 68 focuses and 79 connectors (layout hash `f704cbaaf49c7b954a5e3cb44a3b416fcace774f60d249c4ec9557a609438ef1`), and Wendigo 28 focuses and 28 connectors (layout hash `5685038128dbcfa8f7eadf68f3d359e8d1206578b3b06cae2239ed940aff0e89`). The adapter reported only non-blocking spacing warnings and one unrelated vanilla continuous-focus localisation warning.
- `hoi4_focus_render` for `cannibalism_unified_focus_tree` returned `FOCUS_RENDERED` with HTML, SVG, JSON, source-map, and plan artifacts. A matching `hoi4_focus_raster` request returned `INTERNAL_ERROR` after validation accepted the national-tree spacing parameters; no raster pass is claimed for this continuation.
- `hoi4_gui_inspect` for `cannibalism_network_window` resolved 27 owned elements. Its global source graph was dominated by unrelated Event 003/Event 005 symbol collisions, visible-overlap diagnostics, and truncated diagnostics; those workspace-wide adapter errors were not patched as Event 014 work. The bounded inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0aa68b2da6c3dd81d9f465b5356cb40176eee0986b6ef88bddc4e552cac67a98/9de8e5ff366f4e49b85877f64bd9c243b4d48df85e871e9dcc0acb81a80ca116/gui-inspect.4644732d483a21d3.json`; the post-change render artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/e8dd9e6e12ff30d3fbdb15db1d21ec54eb3ea7cca8f6977c6d5a7175aa305638/cannibalism_network_window-full.svg`. Existing Event 014 parser-repair and post-change artifacts remain the authoritative bounded GUI evidence.

## Contradictions reconciled

| Contradiction | Evidence | Resolution |
| --- | --- | --- |
| Old package status said no downstream blockers while model and audio handoffs are blocked | `quality/package_status.md`, per-job model and audio handoffs | Added the 2026-08-25 downstream amendment and limited the 2026-07-15 closure to its frozen scope. |
| Asset matrix said counter output was still pending | `matrices/asset_inventory_matrix.md`, counter handoff, current registries | Changed the row to nine counter triplets and 27 present DDS/registry consumers, with live review still open. |
| Event overview said future counter workers owned all counter files | `docs/events/014_cannibalism/overview.md` | Recorded counter package presence and retained parent ownership only for model/entity/action/audio runtime work and live review. |
| Counter manifest and GFX handoff said the ninth registration was pending | `docs/assets/014_cannibalism/manifest.md`, `gfx_handoff.md`, counter handoff | Reconciled all nine registry families as integrated and retained only live consumer review as open. |
| GUI audit and dimension ledger mentioned animation toggles or preferences | `014_gui_dimension_ledger.md`, `2026-07-22_event014_gui_focus_improvement_loop_audit.md`, decision/mission audit | Removed current toggle claims and marked historical animation-toggle wording superseded. |
| Historical plans described Prison Host and Lockhouse as a fourth origin | old focus remediation, portrait, and closure handoffs | Added superseded notices and changed one active weighting sentence to ordinary prison/detention objectives. |
| Model docs allowed substantially original or generated-from-scratch ImageGen inputs | old model-source direction, adaptation briefs, per-job manifests and handoffs | Established actual sourced/user-supplied artwork plus faithful enhancement only; generated or redesigned descendants are rejected. |
| Feast Guard model input hash and provenance described the old generated line | Feast Guard handoff, manifests, source gate override | Recorded user-supplied `refs/source/untouched.png` and faithful input SHA-256 `C67AF852A27E1379590BD84C5175C378D449AE226F895A2D326B45099040D8C9`; marked the old `6ACD...` line superseded. |
| Older model-family handoff treated generated geometry and old source checks as current | `event014_cannibal_3d_model_family_handoff.md`, per-job model handoffs | Marked old provider evidence historical and rejected while retaining failure evidence. |
| Bone Riders and Network Cadre handoffs described unresolved custom model work | `event014_unit_visual_reuse_2026-08-26.md`, `models_3d/family_jobs.json`, removed model workspaces | Reclassified both as approved vanilla-visual simplifications with exact `cavalry` and `infantry` sprites; retained old records are historical lineage only and no custom-model blocker remains. |
| Current family-job ledger omitted Bone Riders and retained a stale Network Cadre model root | `docs/assets/014_cannibalism/models_3d/family_jobs.json`, current folder listing | Added nine gameplay-consumer accounting, seven custom-package accounting, two explicit vanilla-reuse entries, and a `lineage_only` provider-cache policy. |

## Superseded or duplicate document list

- `event014_cannibal_3d_model_family_handoff.md` is historical eight-family provider evidence and is superseded by the source-direction amendment, `event014_cannibal_model_family_handoff.md`, and per-family handoffs.
- `014_modern_model_source_adaptation_brief_2026-08-22.md` is a historical three-job redesign brief and is superseded by the faithful-enhancement source gate.
- `sourced_reference_manifest_group_a_redo_2026-08-22.md`, `sourced_reference_manifest.md`, modern group-B/group-C GFX handoffs, and per-job modern adaptation briefs remain research evidence only and do not authorize provider input.
- Archival model-source handoffs and the old Bone Riders, March, and Network archival GFX handoffs remain rejected evidence with explicit superseded notices.
- `event014_cannibal_bone_riders_model_handoff.md`, `event014_bone_riders_final_v8.md`, `event014_bone_riders_paid_v9.md`, `event014_network_cadre_final_v8.md`, and `event014_cannibal_network_cadre_3d_handoff.md` are historical custom-model attempts superseded by the 2026-08-26 vanilla-visual reuse decision.
- The 2026-07-15 consolidation audits remain historical closure evidence for the frozen mechanics and presentation scope and do not close the 2026-08-22 model, counter, audio, or parent-review amendment.
- Old focus, portrait, and unified-decision handoffs that retain fourth-origin examples remain historical evidence with superseded notices; they are not current route specifications.
- Counter art manifest, GFX handoff, and plan handoff are intentionally cross-linked rather than merged because they hold separate source, registry, and validation evidence.

## Markdown hard-wrap issue list

- `docs/plans/014_cannibalism_plans/014_gui_dimension_ledger.md` had a current GUI contract sentence that was patched without flattening surrounding deliberate structure.
- `docs/plans/014_cannibalism_plans/improvement_loop/2026-07-22_event014_gui_focus_improvement_loop_audit.md` contained historical prose wrapped across physical lines; the affected GUI paragraphs were corrected, but the old audit was not wholesale reflowed because it is historical and contains deliberate list and section structure.
- New ledger, resume, and handoff prose uses one physical line per sentence, with headings, list items, tables, and code or artifact lines preserved as deliberate Markdown structure.
- No binary, spreadsheet, generated image, DDS, or gameplay file was inspected or rewritten as part of the Markdown hard-wrap pass.

## Recommended parent decisions

- The live `chaos-redux-3d-model-pipeline` skill already carries the modern-designed-artwork source-first and faithful-cleanup gate. Keep the 2026-08-22 maintenance handoff as historical evidence, but do not treat its older adaptation wording as the current rule.
- Keep Bone Riders on vanilla `sprite = cavalry` and Network Cadre on vanilla `sprite = infantry` as the approved current scope; do not reopen their removed provider/model workspaces without a new design decision.
- Keep the seven dedicated model packages and their source/provenance records under parent live-consumer and binary-provenance review, with provider paths treated as lineage-only.
- Keep the installed runtime sound definitions and CBA-CBH/CBL country-level voice mappings as the current locations, while treating model-specific action/entity synchronization as applicable only to the seven bespoke model packages.
- Complete parent-owned entity, model, action, and live consumer validation before any final package-completion claim. The four super-event audio registrations are closed in `subagent_handoffs/event014_super_event_audio_wiring_audit_2026-08-25.md`.

## Current parent handoff state

The gameplay/documentation design is current at nine consumers, three origins, no cluster, no Prison Host, reveal-gated Hannibal identity, separate vanilla elephantry, no animation toggle, and a 27-texture counter package. Seven model/action/entity/audio packages are parent-installed with source-checked evidence, while Bone Riders and Network Cadre use approved vanilla `cavalry` and `infantry` sprites with no custom model blocker. Parent live consumer validation, portrait-worker acceptance, partial MCP/GUI evidence, unresolved probability scenarios, two bespoke-model provenance mismatches, and super-event image/live review remain open as documented evidence gates. The four Event 014 super-event audio registrations are source- and runtime-wired; their distinct image and live presentation review remain parent-owned.
