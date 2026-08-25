# Event 014 documentation state

Status date: 2026-08-25 parent runtime-wiring amendment.

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
- Nine custom formation families are current: `cannibal_scavenger_warband`, `cannibal_feast_guard`, `cannibal_feast_cohort`, `cannibal_bone_guard`, `cannibal_bone_riders`, `cannibal_island_reavers`, `cannibal_siege_eaters`, `cannibal_march_predation_column`, and `cannibal_network_cadre`.
- The eight foot families share `category_cannibal_irregular_infantry`; Bone Riders is the separate horse-mounted mobile family with the same Event 014 irregular category and real infantry-equipment need.
- Five families now have parent-installed mesh, eight-action, entity/GFX, material-map, and seven-role runtime sound packages: Feast Guard, Feast Cohort, Bone Guard, Siege Eaters, and March Predation Column. Bone Riders, Island Reavers, Scavenger Warband, and Network Cadre remain outside the installed runtime model set under their documented provider or review gates.
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
| Origins | spec part 4, `014_removed_origin_cleanup_2026-07-15.md`, event overview | Three origins only; Prison Host rejected | Historical fourth-origin plans remain marked as superseded. |
| Nine gameplay consumers | event overview, README, spec part 4, irregular-unit plan, two unit implementation handoffs | Definition-level consumers and CXT registration are current | Parent owns live test-country and in-game consumer validation. |
| Elephantry separation | Bone Riders implementation handoff and spec part 4 | Vanilla `elephantry` only in Scavenged Elephant Column | No custom elephant model or counter is authorized. |
| Counter art | `event014_cannibal_counter_art_handoff.md`, `docs/assets/014_cannibalism/manifest.md`, `gfx_handoff.md` | Nine triplets and 27 DDS textures with registry consumers are present | Live consumer review remains parent or user-owned. |
| Humanoid model jobs | irregular-unit model plan, source-direction amendment, per-job manifests and handoffs | Five packages are parent-installed with Meshy/Blender evidence; Scavenger Warband and Network Cadre remain review/provider-blocked; Island Reavers has a later succeeded geometry candidate but no accepted v8 rig/action package, with the earlier HTTP 402 attempt retained as superseded evidence | Live in-game validation is not claimed, and four families are not wired as complete runtime models. |
| Bone Riders model job | Bone Riders model handoff and source audit | Compound horse/rider route is blocked because the available adapter accepts standard humanoid action rigs only | A complete accepted quadruped/horse-rider action route remains needed. |
| Unit audio | per-job manifests, `sound/014_cannibalism_units_sound.asset`, `sound/014_cannibalism_voices.asset`, and `event014_remaining_unit_audio_runtime_wiring_2026-08-25.md` | Five model-complete packages contain 35 converted 44.1 kHz WAV files, and the four blocked packages now add 26 source-derived runtime WAVs, sound definitions, and CBA-CBH/CBL country-level infantry idle bindings | Action synchronization, entity binding, Bone Riders playback, and live validation remain open. |
| Super-event media | `docs/specs/014_cannibalism_specs/matrices/super_event_matrix.md`, `docs/super_events/014_cannibalism/audio_research.md`, and `subagent_handoffs/event014_super_event_audio_wiring_audit_2026-08-25.md` | Four audio/image packages are source-side documented; all four audio tracks are registered and dispatched through the settings-aware helper | Distinct image registration and live presentation review remain parent-owned. |
| Animation | frame-animation package docs and model action contracts | Existing Event 014 frame packages remain asset-level evidence; custom model actions are blocked or pending | No Event 014 animation preference or toggle is part of the GUI contract. |
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

## 2026-08-25 continuation MCP evidence

- `hoi4_event_inspect` with selector `{kind: event, eventId: chaosx.nr14.1}` returned `EVENT_INSPECTED_PARTIAL` at revision `346feba59f5e70d0f3484698b2408e6b3e9f4bf4f2a66251c73f515c8ae97cae` with zero blocking diagnostics in the selected Event 014 boundary. The adapter deferred workspace-wide helper projections because the repository is large.
- `hoi4_focus_inspect` for `cannibalism_unified_focus_tree` returned `FOCUS_INSPECTED` with 108 focuses, 103 connectors, zero connector crossings, zero node intersections, and no blocking diagnostics. The adapter reported non-blocking same-row spacing warnings from the explicit authored layout and one unrelated vanilla continuous-focus localisation warning.
- `hoi4_focus_raster` produced the CBL PNG/SVG/HTML/JSON review bundle at 3312 by 2488 pixels. The result had no blocking focus diagnostics.
- `hoi4_gui_inspect` for `cannibalism_network_window` resolved 27 owned elements. Its global source graph was dominated by unrelated Event 003/Event 005 symbol collisions and truncated diagnostics; those workspace-wide adapter errors were not patched as Event 014 work. Existing Event 014 parser-repair and post-change network render artifacts remain the authoritative bounded GUI evidence.

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

## Superseded or duplicate document list

- `event014_cannibal_3d_model_family_handoff.md` is historical eight-family provider evidence and is superseded by the source-direction amendment, `event014_cannibal_model_family_handoff.md`, and per-family handoffs.
- `014_modern_model_source_adaptation_brief_2026-08-22.md` is a historical three-job redesign brief and is superseded by the faithful-enhancement source gate.
- `sourced_reference_manifest_group_a_redo_2026-08-22.md`, `sourced_reference_manifest.md`, modern group-B/group-C GFX handoffs, and per-job modern adaptation briefs remain research evidence only and do not authorize provider input.
- Archival model-source handoffs and the old Bone Riders, March, and Network archival GFX handoffs remain rejected evidence with explicit superseded notices.
- The 2026-07-15 consolidation audits remain historical closure evidence for the frozen mechanics and presentation scope and do not close the 2026-08-22 model, counter, audio, or parent-review amendment.
- Old focus, portrait, and unified-decision handoffs that retain fourth-origin examples remain historical evidence with superseded notices; they are not current route specifications.
- Counter art manifest, GFX handoff, and plan handoff are intentionally cross-linked rather than merged because they hold separate source, registry, and validation evidence.

## Markdown hard-wrap issue list

- `docs/plans/014_cannibalism_plans/014_gui_dimension_ledger.md` had a current GUI contract sentence that was patched without flattening surrounding deliberate structure.
- `docs/plans/014_cannibalism_plans/improvement_loop/2026-07-22_event014_gui_focus_improvement_loop_audit.md` contained historical prose wrapped across physical lines; the affected GUI paragraphs were corrected, but the old audit was not wholesale reflowed because it is historical and contains deliberate list and section structure.
- New ledger, resume, and handoff prose uses one physical line per sentence, with headings, list items, tables, and code or artifact lines preserved as deliberate Markdown structure.
- No binary, spreadsheet, generated image, DDS, or gameplay file was inspected or rewritten as part of the Markdown hard-wrap pass.

## Recommended parent decisions

- Decide whether to apply the faithful-enhancement source gate to the shared `chaos-redux-3d-model-pipeline` skill text, because its 2026-08-22 maintenance handoff still describes the older from-scratch fallback even though Event 014 documentation now rejects that route.
- Approve or reject actual sourced/user-supplied inputs for the four remaining model families, keeping the no-redesign rule and exact weapon/anatomy requirements explicit.
- Provide or approve a supported Bone Riders compound action route, or keep that family queued and blocked.
- Decide the runtime sound-definition and country-level voice mapping location for the remaining family packages and whether Bone Riders receives a separate playback package.
- Complete parent-owned entity, model, action, and live consumer validation before any final package-completion claim. The four super-event audio registrations are closed in `subagent_handoffs/event014_super_event_audio_wiring_audit_2026-08-25.md`.

## Current parent handoff state

The gameplay/documentation design is current at nine consumers, three origins, no cluster, no Prison Host, reveal-gated Hannibal identity, separate vanilla elephantry, no animation toggle, and a 27-texture counter package. Five model/action/entity/audio packages are parent-installed with source-checked evidence, and the four blocked packages have source-derived WAVs and sound definitions without action or live-consumer promotion. Bone Riders, Island Reavers, Scavenger Warband, Network Cadre, and live consumer validation remain open or blocked. The four Event 014 super-event audio registrations are source- and runtime-wired; their distinct image and live presentation review remain parent-owned.
