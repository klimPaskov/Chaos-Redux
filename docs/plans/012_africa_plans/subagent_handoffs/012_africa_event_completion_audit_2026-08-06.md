# Event 012 Africa completion audit — 2026-08-06

## Verdict

Status: **blocked and incomplete**.

Event 012 has a large, coherent source implementation, but it does not satisfy the repository completion standard. The 809-row acceptance ledger itself records 44 blocked achievements, 64 blocked AI profiles, 16 blocked priority-member packages, 16 blocked polity candidates, 199 queued polity candidates, 3 blocked host playbooks, 6 blocked actions, and only 52 of 239 asset rows as installed runtime. Current MCP evidence adds five malformed external-focus convergence gates, incomplete event-chain analysis, unresolved decision-timer grammar, and no accepted probability evidence. Current documentation and workbook wording also misstate the six blocked actions.

This was a read-only gameplay audit. No gameplay, localisation, workbook, asset, or GFX file was patched by this auditor. The only file created by this audit is this handoff.

## Audit inputs and method

The audit reviewed `AGENTS.md`, all nine Event 012 specifications, the matrices and diagrams under `docs\specs\012_africa_specs`, the current research and prompt material, `docs\events\012_africa`, the dated plans and handoffs under `docs\plans\012_africa_plans`, and the current gameplay, localisation, GFX, model, sound, and spreadsheet consumers.

The required project skills applied were `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, `chaos-redux-3d-model-pipeline`, `chaos-redux-frame-animation`, `hoi4-focus-trees`, `hoi4-decisions-missions`, `chaos-redux-super-events`, and the read-only portion of `xlsx` for catalog inspection.

The required offline Paradox wiki pages and installed vanilla documentation were consulted. The audit used read-only HOI4 MCP event, focus, and GUI routes. Every weighted surface was routed separately to `chaosx_ai_probability_auditor`; its final status is recorded below.

The source snapshot was actively changing because other bounded Event 012 workers were running. Findings below use the files visible at the final audit snapshot and explicitly distinguish committed/static source evidence from open runtime or tool evidence.

## Exact 809-row acceptance coverage

Ledger: `docs\plans\012_africa_plans\012_africa_acceptance_ledger.csv`.

Snapshot SHA-256: `6DD450AB331509F7F8636B0B6A5669A70146ED71505BDB59E31CCEE39972378E`.

The ledger contains exactly 809 data rows, zero duplicate `acceptance_surface + matrix_row` pairs, and zero blank `source_file`, `implementation_evidence`, `validation_evidence`, or `notes` fields. Nineteen acceptance keys repeat across different surfaces by design; they do not duplicate a surface row.

| Surface | Exact disposition | Completion interpretation |
| --- | ---: | --- |
| Achievement | 44 `blocked` | 0/44 accepted complete. |
| Action concept | 96 `implemented`; 6 `blocked_with_gate` | 96/102 source-implemented; the event is not action-complete. |
| AI profile | 64 `blocked` | 0/64 accepted complete. |
| Asset item | 52 `installed_runtime`; 28 `installed_dormant`; 12 `deferred_runtime_gated`; 133 `deferred_controlled_pool`; 14 `deferred_model_required` | 52/239 active runtime; 187/239 are dormant or deferred. |
| Focus payoff | 78 `implemented` | Row-level payoff code exists, but current focus MCP validation prevents surface acceptance. |
| Host playbook | 48 `implemented`; 3 `blocked` | 48/51 source-implemented. Basutoland/HZX, Eswatini/EUX, and Zanzibar/ELX remain without approved distinct current-state admission. |
| Polity candidate | 199 `queued`; 16 `blocked` | 0/215 promoted as a complete catalog surface; queued rows are controlled-pool entries, not missing-tag authorization. |
| Priority-member package | 16 `blocked` | 0/16 accepted end to end. |

The machine-readable row dispositions are complete. They are not evidence that the overall event is complete; the ledger explicitly records the opposite.

## Completion status by surface

| Surface | Status | Evidence and remaining boundary |
| --- | --- | --- |
| Event identity, root, and registration | Partial | `constant:africa_event.id = 12`, the fire-once registry, `chaosx.nr12.1`, tier-4 eligibility, and Formables cluster 6 registration exist. Required complete event-chain MCP proof is unavailable. |
| Event chains | Blocked evidence | Twelve Event 012 event files contain 182 exact event IDs across four effective ID namespaces. The workspace event scan and root trace are partial; namespace/root rendering did not complete. |
| Event Log and Event Details | Partial | Host/RSA actor mapping, world-order payload logging, and three evolution preview rows are present in `common\scripted_effects\chaosx_events_log_effects.txt:290-307`, `:612-633`, and `:2179-2193`. No complete event-chain render proves every terminal and cleanup path. |
| Evolutions | Partial | Hidden clock `.400` and visible `.401-.403` exist with registered report art. Public tiers 4/5/6 map to three logged stages. `events\012_africa_evolutions.txt` declares `add_namespace = chaosx` while using `chaosx.nr12.*`, relying on another earlier-loaded Event 012 file to declare the effective namespace; this should be normalized or explicitly accepted. |
| Cluster | Static pass | Event 12 is the required Severe member of Formables cluster 6; cluster unlock tier is 3 at `common\script_constants\event_cluster_constants.txt:146-152`. The event itself remains tier 4 and fire-once. |
| Decisions and 102 actions | Partial | All 102 IDs have selector/profile/duration/outcome/cleanup structures; 96 are ledger-implemented. Actions 71-76 remain blocked, and the shared mission timer still lacks an accepted vanilla `FROM.<variable>` grammar precedent. |
| Focuses | Blocked | All 78 accepted payoff rows have implementation entries, but five external trees currently contain MCP-confirmed malformed prerequisites and unreachable descendants. The 276-node continental tree also retains heavy layout diagnostics. |
| Host playbooks | Partial | 48/51 implemented; HZX, EUX, and ELX remain blocked without approved unique current-map admission. No fallback state or tag is permitted. |
| Priority-member country packages | Blocked | All 16 have structural mechanics, force payloads, League/refusal paths, decisions, ideas, character IDs, and shared focus coverage, but all 16 ledger rows remain blocked by formation/release, carrier/origin, portrait, AI, and runtime acceptance. DYX/Luba, DZX/Lunda, and EMX/Kilwa have no accepted unique current-state binding. |
| Controlled polity catalog | Queued/blocked | 199/215 are deliberately queued; the 16 priority rows are blocked. Current Event 012 source does not add a new country tag, which matches the no-new-tags boundary. |
| South Africa Allied settlement | Partial | Narrow original-SAF entry, vanilla-tree preservation, civil war, interveners, settlement, exile, no-patron handling, and log writers are present. Civil-war, settlement-order, exile, and no-patron acceptance scenarios remain unproven. |
| Voluntary diaspora | Partial with spec gap | Consent, withdrawal, passage, housing, skills, bonds, citizenship, representation, and emergency evacuation ledgers exist, and diaspora events `.310-.313` are present. The accepted employment/jobs condition is not implemented as a gate or result witness. |
| Natural-disaster API | Partial | Actions 69/70 preserve an exact selected enemy, derive bounded strength, and call the Event 013 public wrapper. Actions 71-73 remain disease/review blocked, and the priority-member hostile-target builder uses an unresolved whole-world scan. |
| Scramble and world order | Blocked | Six-package, settlement, sovereign, terminal-resolution, chaos, incompatible-world-end, and live-war gates exist. W5 source receipts and its review receipt are self-written in the runtime opening block, so the gate can certify despite current focus and AI acceptance failures. |
| Achievements | Blocked | 44 registry entries and 132 DDS states exist, but the ledger keeps all 44 blocked. Current evidence classifies 24 as `REACHABLE/PARTIAL`, 5 as `ACTIVE/BLOCKED`, 3 as `MODEL-GATED`, 3 as `WORLD-GATED`, and 9 with newer owner evidence that still does not close live acceptance. |
| AI and weighted logic | Blocked | All 64 ledger rows remain blocked. No source-only balance claim is acceptable. See the independent probability audit status below. |
| Charter scripted GUI | Partial; adapter-blocked | The dedicated `chaosx_event_ui_worker` handoff proves Event 012 ownership, decision-category entry, layout-contract coverage, and pre/post inspect/render evidence across 14 states and three resolutions. The bounded geometry repair is implemented. `hoi4.gui_rewrite` rejected all safe source/patch forms, and the returned comparison is same-scenario rather than a true pre/post pixel comparison; workspace/global validation also remains false. |
| Localisation | Static pass; review open | Fresh source reconciliation finds 405 unique Event 012 focus IDs and all 810 name/description keys, plus complete action, event, achievement, character, unit, equipment, and technology coverage. Two Afaan Oromoo flavour strings remain pending native-speaker review. |
| Super-events | Source/asset pass; gameplay gated | Four slots, four unique audio IDs, images, text, settings wrappers, and rights records exist. Their actual emission and terminal end-state remain gated by incomplete gameplay and acceptance surfaces. |
| 3D units and counters | Blocked except partial elephant runtime | Fourteen asset rows remain `deferred_model_required`. Elephant runtime binaries and consumers exist, but the durable source/audio/counter evidence paths named by its handoff are absent from the current repository snapshot. The eight other strange-force consumers remain behind unset manifest and global gates. |
| Catalog and documentation | Stale/inconsistent | The workbook/CSV status remains `Partially Available`, but its action wording and `docs\events\012_africa\overview.md` disagree with the ledger and current source. Several accepted plans remain unpromoted or internally stale. |

## Event-chain inventory and mandatory MCP evidence

The current source contains 182 exact Event 012 event IDs:

| Effective ID namespace | Files and count | Total |
| --- | --- | ---: |
| `chaosx.nr12` | Core 19; diaspora 4; evolutions 4; RSA 9 | 36 |
| `africa_priority_member` | Priority-member reports and hidden recruitment 5 | 5 |
| `africa_world_order` | Scramble/world-order events 13 | 13 |
| `africa_world_package` | Base 14; sponsorship 12; three paired-continent files 14 each; union/war 60 | 128 |
| Total | Twelve files | 182 |

The required event evidence is not complete:

- A workspace `hoi4.event_inspect` scan completed as `EVENT_INSPECTED_PARTIAL`: 360 event files scanned, 9,464 events, 14,614 options, 1,050 entries, 8,145 unresolved nodes, 7,629 terminals, 36,847 edges, 28,031 state accesses, and 2,119 issues. The tool explicitly deferred workspace-wide helper projections and lifecycle passes. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8efd4010436a4620199fd59c8b3ddfcfa99b0e719d4fab4a0f8bdf1f8f1b415/44100bd7eea91f635b89c0f04ead01c3fd701e9bddb326d7f1dea93b9870a5be/event-scan-e95cc5f8ce60.json`.
- A later root trace for `chaosx.nr12.1` also returned `EVENT_INSPECTED_PARTIAL`, and its render selected only three nodes rather than the full shared graph. Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/163d7d71115ade5c86cab605afbfb0762f983244fc3a3e77b7dee9c3cef0e9cb/f0b46de0ac638ca059e6e1f57a07c02e2a6ef3046f9cf514155ee98ff1041b31/event-trace-c5c2ec44234b.json`. Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9e7e58dfbe94ad50dd0145c943331db0c9598dae58111fb8786784026956b74/703918d7084595066f32c1cffe3411a258a837861f42aee18ee859a702829e96/event-options-c5c2ec44234b.json`.
- A namespace-bounded inspect for `chaosx.nr12` and a root overview render for `chaosx.nr12.1` each timed out after 180 seconds with `tool call failed for hoi4_agent_tools/hoi4.event_inspect|render; timed out awaiting tools/call after 180s`.
- `hoi4.event_compare` returned `EVENT_COMPARISON_BASELINE_REQUIRED`: no cached baseline revision, before-graph artifact, or proposed source overlay was supplied. No comparison claim is made.

Source inspection therefore supports registration and callsite findings only. It is not equivalent to required per-chain inspect/render evidence, and this alone blocks an event-complete verdict.

## Actions, decisions, and mission blockers

The current ledger correctly records 96 implemented actions and six gated actions:

| Row | Action | Exact remaining boundary |
| ---: | --- | --- |
| 71 | `contain_emergent_disease` | Event 013 target receipt, failure, and cleanup owners are absent. |
| 72 | `research_disease_countermeasure` | Event 013 target receipt, failure, and cleanup owners are absent. |
| 73 | `weaponise_fictional_pathogen` | No approved review-authorisation setter or accepted disease API contract. |
| 74 | `awaken_stone_cohort` | Model/entity/audio/counter manifest gate. |
| 75 | `train_gorilla_heavy_infantry` | Model/entity/audio/counter manifest gate. |
| 76 | `organise_pan_sappers` | Model/entity/audio/counter manifest gate. |

All 102 rows have selector, constant, profile, duration/objective, full, partial, failure, and cleanup source coverage. The current decision audit also fixed the RSA dynamic timer to the vanilla-supported `var:` form and wired four existing sponsorship effect tooltips.

Two engine/policy blockers remain:

1. `mission_africa_action_short`, `_medium`, `_long`, and `_epic` read `days_mission_timeout = FROM.africa_active_action_duration_days` in `common\decisions\012_africa_decisions.txt`. The source snapshot stores the correct row-specific duration, but no installed-vanilla precedent or completed engine evidence validates this grammar. The 102-row timer contract is not engine-proven.
2. Event 012 contains fourteen `every_country` blocks. Accepted planning explicitly covers the one-shot host selection and two Scramble census sweeps, but the nested prefire-contact scan, the two visible-roster refreshes, the priority-member natural-disaster refresh, the global human-audio fan-out, and six continent-constituent enrollment scans lack a clear current approval/disposition. The decision audit independently flags the three player/AI target refreshes at `common\scripted_effects\012_africa_effects.txt:741`, `:764`, and `common\scripted_effects\012_africa_action_effects.txt:2763`. The six constituent scans are at `common\scripted_effects\012_africa_world_order_effects.txt:1299-1434` and contradict older W1 wording that claimed no world scan. These must be explicitly approved or replaced with bounded maintained rosters before completion.

No duplicate action store, free-unit loop, blanket core grant, fallback target after quote invalidation, or hidden GUI execution path was found.

## Focus-tree blockers

Current MCP inspect and render completed for all eight Event 012 focus trees. Five external trees have a confirmed malformed convergence prerequisite because they place an `OR` trigger inside a `prerequisite` block:

- Asia: `common\national_focus\012_africa_world_asia_focus.txt:185`, focus `africa_asia_food_river_and_monsoon_board`; the node and downstream route become unreachable.
- Europe: `common\national_focus\012_africa_world_europe_focus.txt:182`, focus `africa_europe_common_army_and_air_defence`.
- North America: `common\national_focus\012_africa_world_north_america_focus.txt:329`, focus `africa_north_america_resources_and_withdrawal_law`; the node is unreachable.
- Oceania: `common\national_focus\012_africa_world_oceania_focus.txt:343`, focus `africa_oceania_ocean_constitution_and_withdrawal_law`; the node is unreachable.
- South America: `common\national_focus\012_africa_world_south_america_focus.txt:373`, focus `africa_south_america_resource_and_debt_sovereignty_law`; it and two downstream nodes are unreachable.

The Middle East external tree has no Event 012 hard prerequisite error, although it retains layout warnings. The shared eight-focus priority overlay has zero tree-local diagnostics.

The 276-focus continental tree retains 61 connector crossings, 50 node intersections, 35 long connectors, one too-close spacing warning, and repeated generic regional reward warnings after the bounded coordinate repair. These are not equivalent to the five hard external-tree errors, but they prevent a clean layout acceptance.

The five current hard errors contradict `docs\plans\012_africa_plans\subagent_handoffs\012_africa_focus_gui_skill_audit_2026-08-05.md`, which reports zero Event 012 diagnostics for the external trees. That dated handoff is stale against the current source and MCP revision.

Fresh source reconciliation finds 405 unique focus IDs across these eight files, not the 394 claimed by the current localisation handoff. All 810 corresponding name and description keys do resolve, so this is a documentation count error rather than a missing-localisation defect.

## Country packages, polities, tags, and portraits

The sixteen priority packages have meaningful structural differentiation: 16/16 mechanic branches, force payloads, League clauses, refusal/counterproposal paths, overlap settlements, post-settlement actions, character IDs, starting/mature ideas, and shared overlay consumers are present. The no-new-tags rule is respected; the packages reuse nine vanilla carriers and seven existing Event 006 niche carriers.

They are not complete:

- All 16 priority-package ledger rows remain blocked.
- DYX/Luba, DZX/Lunda, and EMX/Kilwa cannot pass current viable-state admission because no approved unique current-map binding exists. The other 13 still require formation/release, origin, route, portrait, AI, and runtime acceptance.
- The shared priority focus has eight nodes and no branch nodes. Package depth is carried by decisions/effects/localisation rather than sixteen bespoke trees; this needs explicit design acceptance rather than an implicit simplification.
- No package-specific advisor or high-command entries were found. The current spec may permit sovereign/party/idea identity to carry the package, but the omission needs an explicit accept/reject disposition.
- The 215-row polity catalog remains 199 queued and 16 blocked. Queued entries must not be converted into new tags or broad state substitutes without a separate accepted plan.

Portrait acceptance is also open:

- All sixteen priority runtime sprite keys point to 156x210 `_source_locked.dds` direct-source placeholders. The durable map at `docs\assets\portraits\012_africa\source_locked_runtime_mapping.md` clearly labels artifact/map placeholders and retains source names.
- No completed `chaosx_portrait_creator` handoff was found for Event 012. The only current mention is the country audit instructing the parent to route the unresolved portrait decisions to that worker.
- Grounded final HOI4-style replacements and explicit user-supplied replacement evidence are absent. Aksum, Nubia, Kilwa, and Great Zimbabwe use artifact/map identity placeholders, and several actor/date choices remain disputed.
- Six fictional high-chaos portraits have native ImageGen, processed DDS, and dormant sprite evidence, but their handoff was not produced by or reconciled through `chaosx_portrait_creator`. They remain dormant behind model/package gates.

Under the current repository portrait rule, both the missing portrait-worker handoff and the grounded-placeholder replacement state block package completion.

## South Africa, diaspora, and Event 013 integration

### South Africa Allied route

`events\012_african_union.txt:33-40` preserves the normal South African tree and calls the Allied rupture only after the narrow RSA gate. `common\scripted_triggers\012_africa_rsa_triggers.txt` and `common\scripted_effects\012_africa_rsa_effects.txt` own the civil war, interveners, settlement, exile, no-patron, and cleanup paths.

Static integration is substantial, but acceptance remains open for at least the civil-war start, each settlement order, exile continuation, no-patron terminal, and cleanup after interveners settle in different orders. No fallback host, annexation shortcut, or new South African tag is authorized.

### Voluntary diaspora

Actions 51-57 and the target-owned diaspora protocol implement explicit consent, refusal, withdrawal, passage, housing, skills, veterans, bonds, citizenship, representation, and emergency evacuation. `events\012_africa_diaspora_protocol.txt` contains `.310-.313`, and `common\scripted_effects\012_africa_diaspora_effects.txt` keeps consent and target capacity separate from opinion.

The accepted spec at `docs\specs\012_africa_specs\specs\012_africa_spec_part_2_charter_league_integration.md:670` requires transport, housing, employment, citizenship, local consent, and political settlement. The Action 53 matrix also requires “local consent and jobs or education available.” Current Action 53 validation at `common\scripted_effects\012_africa_action_effects.txt:3558-3567` checks usable target, registry, and target consent only. No Event 012 runtime flag, variable, trigger, or result witness for diaspora employment, jobs, or livelihood was found. This is a direct accepted-spec omission, not merely missing live proof.

### Natural disasters and disease

Actions 69/70 derive bounded Event 013 strength and call `call_natural_disaster = yes` only after exact selected-enemy, war, cooldown, reserve, and eligibility checks in `common\scripted_effects\012_africa_action_effects.txt:7289-7542`. The wrapper never widens to another country after the selected target fails validation.

The natural-disaster member target refresh still uses `every_country` at `common\scripted_effects\012_africa_action_effects.txt:2763` and needs explicit approval or a maintained hostile roster. Actions 71-73 remain blocked as listed above. The newly wired Disaster Wardens and Plague Carriers consumers remain dormant because the global and per-family model/entity/counter/audio gates are unset.

## Scramble, W5, and terminal-world blockers

The terminal contract is structurally strict. `common\script_constants\012_africa_world_order_constants.txt:149-154` requires six packages, six settled packages, two sovereign completions, sponsorship chaos 450, high-chaos package review 750, and terminal chaos 1000. `africa_terminal_world_identity_can_commit` at `common\scripted_triggers\012_africa_world_order_triggers.txt:917-955` additionally requires the terminal route, every actor terminally resolved, no unresolved war against the host, no incompatible world end, and the ready super-event package. `africa_form_terminal_world_identity` at `common\scripted_effects\012_africa_world_order_effects.txt:3707` writes the final identity only after that trigger.

The completion problem is W5 certification provenance:

1. `africa_world_register_package_surface_receipts` writes route, focus, decision, idea, AI, identity, and localisation receipts.
2. `africa_world_review_runtime_surface_registry` writes the “reviewed” receipt from those source-written flags.
3. `africa_world_certify_all_package_runtime_surfaces` sets `africa_world_package_implementation_ready` on all six candidates.
4. All three effects are called consecutively from the Scramble opening block at `common\scripted_effects\012_africa_world_order_effects.txt:724-733`.

This is self-certification, not evidence-backed promotion. It can record AI and focus readiness even though the acceptance ledger has 64 blocked AI rows and current MCP finds five malformed external focus trees. The review flag therefore does not fail closed against the current audit state. W5 must remain blocked until the review receipt has a real parent-owned promotion boundary or the design explicitly accepts automatic source registration as sufficient and reconciles the ledger and diagnostics.

The terminal super-event source package is materially complete: four distinct slots, images, titles, quotes, audio IDs 58-61, settings wrappers, CC0/public-domain sources, runtime WAVs, and one shared presenter exist. This closes the older roles 1/4 audio blocker, but it does not close W5 political proof, external focus validity, AI balance, terminal state transfer, achievement 44, or live end-state acceptance.

## Achievements

The registry contains 44 Event 012 achievement definitions and the filesystem contains exactly 132 Event 012 achievement DDS files, covering eligible, grey, and not-eligible states.

All 44 acceptance rows remain blocked. The latest ledger distribution is:

- 24 `REACHABLE/PARTIAL` rows with incomplete positive/disqualifier/cleanup ownership.
- 5 `ACTIVE/BLOCKED` restoration/package rows.
- 3 `MODEL-GATED` rows: 18, 35, and 40.
- 3 `WORLD-GATED` rows: 41-43.
- 9 rows with newer owner evidence, including elephant, natural-disaster, reserve, development, diaspora, and terminal paths, but no full acceptance proof.

Row 36 has an elephant unit consumer but remains blocked by exact movement, desert, supply, protection-war, destruction, and disqualifier evidence. Row 44 has terminal helper callsites but remains blocked by the self-certifying W5 path and unaccepted terminal political state. Installed art cannot promote any achievement without its exact runtime conditions.

## AI and probability evidence

The source contains the 64 profile predicates/loaders and 102-action dispatch paths, but the acceptance ledger intentionally records all 64 as blocked. Static source review cannot establish relative frequency, route preference, target fairness, retry behavior, or campaign balance.

The required `chaosx_ai_probability_auditor` completed read-only discovery, named-scenario evaluation, and rendering and returned the following evidence to this completion audit. The evidence does not accept any of the 64 rows:

- Event world-order option discovery found 16 candidates with an incomplete pool. The four-scenario evaluation `probability-d76856c253444186ec118a08` evaluated 64 candidate-scenarios but remained partial with nine unresolved results and nine diagnostics; option `.1.e` was never eligible because the relevant flags and variable state could not be resolved.
- The direct random surface in `common\scripted_effects\012_africa_action_effects.txt` evaluates to an exact 20 percent under its bounded scenario (`probability-ed247ffdcaff586a75d3a642`). This proves one local random value, not campaign balance.
- Action-effect random lists evaluated 14 candidates under `probability-f9d5b7f645bf1da5e2cfef7e` with one unresolved result and an incomplete pool. AI-profile random lists evaluated 118 candidates under `probability-f8eb45019e3be1685b9fdd4e` with 29 unresolved results and an incomplete pool.
- Decision discovery found 206 candidates. The key 16-action pool evaluation remained partial with 51 unresolved results; the three-scenario sweep `probability-c8bd0dd69c7a884580c16e09` returned zero raw scores because required flags, targets, and variables were unresolved. `rankReversals = []` is not acceptance under an incomplete pool.
- The mission adapter returned `PROBABILITY_SURFACE_EMPTY` because the shared missions expose no native `ai_will_do` surface. The AI-strategy-plan adapter likewise returned `PROBABILITY_SURFACE_EMPTY` for nested focus/research factors, and the MTTH adapter returned `PROBABILITY_SURFACE_EMPTY` for the Event 012 event/MTTH paths.
- Focus discovery found 276 continental, 8 priority, and 20-21 candidates per external world tree, all with incomplete pools. The priority evaluation `probability-9ece80ceb18eca88781aebf2` was partial with 57 unresolved results and all eight candidates never eligible in the flat state.
- Strange-force technology evaluation `probability-25fe994a644fd47375e96991` found all eight candidates ineligible because `allow = { always = no }`. Elephant evaluation `probability-76dd9e01448be872a66974b4` returned raw factor zero and unresolved external research factors. Custom-pool discovery found zero declared candidates, so no sequence analysis was possible.

No weighted source was changed by this audit, so there is no legitimate before/after probability comparison. The completed MCP pass is meaningful negative evidence: it proves several local weights and hard gates, but incomplete pools, unresolved scenario state, and unsupported adapter surfaces prevent relative-frequency or route-balance acceptance. The probability auditor did not finish its separate artifact-index handoff after returning these findings and was interrupted after two bounded finalization attempts; the analysis IDs above remain evidence, but the missing standalone handoff is a documentation gap. All 64 AI rows remain blocked.

## Charter GUI evidence and remaining adapter gap

The dedicated `chaosx_event_ui_worker` handoff at `docs\plans\012_africa_plans\subagent_handoffs\012_africa_event012_charter_gui_2026-08-06.md` proves that `africa_charter_window` is owned exclusively by Event 012 and entered through the host-only `africa_charter_council_category`. It documents the member, regional, state, action-family, diaspora, project, rival, and primary/secondary-value layout contracts. The worker changed only `interface\012_africa_charter.gui` to repair scale-induced selector displacement.

Current target-scoped GUI evidence supersedes older timeout/internal-error notes:

- Pre-change `hoi4.gui_inspect` returned `GUI_INSPECTED` for 87 inspected elements. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7a01ec5a0e4805c3097830405a3a5a920f43e1659e87b9661303c6f642c540a/0f3b36f0399ea78d46725bced87e3836d52162f83fb8999deed4196e243e4d8a/gui-inspect.4f664932032b5432.json`.
- Post-change `hoi4.gui_inspect` returned `GUI_INSPECTED` for the same 87 elements at source revision `eab478ecc98355b24b293bbdb7d6d34a7c4d27504487144319ec762400cac68a`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d4ea30f50e5e7bfa2278c154ba44741936b8c2c36e96a8deb54fb1a8142a632/453af0f76d22114ec2778882aaee745f2a659748475d498a787e730c046c0d66/gui-inspect.eab478ecc98355b2.json`.
- Post-change `hoi4.gui_render` returned all 14 requested states and the 1920x1080, 1366x768, and 2560x1440 routes. It produced full, cropped, annotated, click-region, source-map, hierarchy, state-matrix, resolution, and comparison artifacts. Click-region artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f88611c268255e409e7f65907ada2cd79ca4b243a013893d694cf201e9016066/cbe62faf64589e306a1f4741894a4675a2b1570b791b144118db3bfb45064c60/africa_charter_window-click-regions.png`. Hierarchy artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5da8c6da1af5477466f7153c257ea23d8a0a726ec663aff91e4aec9a39f5b901/72e9bfa5b4dac19d54389152446a36be8f2a015f2e010b12262cfd5843527748/africa_charter_window-hierarchy.svg`.

The pre/post layout graphs show that the overlay and diaspora click rectangles moved onto their painted controls, and the repaired selectors remain visible and clickable. Workspace validation remains false because the full source graph reports 1,900 blockers and 170 overlaps, mostly unrelated or intentionally layered. The comparison artifact reports zero changed pixels because it is a same-scenario comparison rather than a changed-revision pre/post comparison; it does not prove the long-text and missing-localisation variants are visually distinct.

The mandatory `hoi4.gui_rewrite` route was attempted. It returned `GUI_SOURCE_STALE`, `GUI_UNSAFE_PATCH_RANGE`, `REWRITE_STRUCTURE_LIMIT`, and conflicting source/patch-mode validation rather than an applicable rewrite. The worker therefore used the parent-authorized direct patch and recorded source hash `A1AB9DB83542EA41DDF7005601A7E57E0A847DA66F03C1F5F6FABDA978B7CB1E`. This is an exact adapter blocker, not missing worker ownership. The surface remains partial until the parent accepts the direct-patch exception or the rewrite adapter can apply the change and produce a genuine pre/post comparison.

## Assets, animation, models, audio, and counters

The 239-row asset matrix is fully classified but far from fully active: 52 installed runtime, 28 installed dormant, 12 runtime-gated, 133 controlled-pool deferred, and 14 model-required deferred.

The fourteen model-required rows are high-chaos country packages 197-202 plus unit rows 205-212: Gorilla Heavy Infantry, Pan Sappers, Stone Cohorts, Riverborn, Forest Giants, Oracle Recon, Disaster Wardens, and Plague Carriers. The guarded gameplay data and spawn consumers now exist, but the shared `africa_strange_formation_package_ready` flag and four model/entity/counter/audio receipts per family remain unset. This is the correct fail-closed behavior.

Current package status is mixed and none of these eight can be promoted:

- Gorilla and Pan are blocked at the Blender-adapter dependency route; no final model, animation, sound, counter, or runtime export exists.
- Stone has a Meshy source download and partial production evidence but no complete locked-adapter export, final audio/counter package, or runtime acceptance.
- Forest Giants and Oracle Recon are blocked before complete production and lack final source-to-runtime handoffs.
- Riverborn and Disaster Wardens have active working/evidence files, but no accepted final model/audio/counter/runtime manifest closes their ledger row.
- Plague Carriers has intake/provider evidence but no accepted final package.

For every blocked custom unit, required Internet-sourced audio provenance, original and derived checksums, complete role coverage, animation synchronization, final sound-definition wiring, exact installed-vanilla large/on-map counter inspection, skill-local reference-family inspection, sampled vanilla-green evidence, original counter art, final DDS comparison, and live runtime consumer proof remain absent or incomplete. No generated, synthesized, placeholder, copied, renamed, or unlicensed substitute is acceptable.

The shared elephant is a partial exception. Runtime mesh, six animations, textures, six WAVs, entity/asset registrations, subunit/equipment/technology, large/on-map two-frame counters, and host/Action 102 consumers exist. The runtime mesh and counter hashes match the handoff:

- Mesh `6C3B53731646C3F57F56D26AFE5E4F7215C3E034469AD04179A3F0A70F4D5988`.
- Large counter `5D455DC3268BE89451D967E187FD5AAA8D6966C9A82FF8AE933208DF2201A21E`.
- On-map counter `6E2AC8B322F4FE1D6D126E1B02727BE721B83FD4EEC5788D6B9D0AB083188BDD`.

However, `docs\assets\012_africa\models_3d\elephant_shared_base` is absent from the current filesystem. The handoff names `evidence\audio\source_urls.json`, `audio_manifest.json`, `sound_design_handoff.md`, original source downloads, Blender checkpoints, reimport proofs, counter reference/palette evidence, and comparison assets under that root, but none of those durable files is present. The tracked handoff preserves summary authors/licences/checksums but not the exact original source pages for all unit-audio roles or the required vanilla counter-definition/DDS/reference inspection. The elephant may remain ledger `installed_runtime`, but its complete source-evidence package and achievement acceptance are blocked until those artifacts are restored or explicitly relocated and reconciled.

The four super-event audio roles do have durable source-page, licence, source-hash, runtime-hash, duration, and wrapper evidence. Their asset completion should not be conflated with terminal gameplay completion.

## Localisation, catalog, and documentation gaps

The current localisation audit reports no missing runtime key after its strange-force patch, and this audit independently confirms 405/405 unique focus IDs have names and descriptions. Event references, action fields, achievement triplets, character names, portrait sprite names, subunits, equipment, and technologies are covered.

Open wording/presentation items:

- The two required Afaan Oromoo fictional flavour strings occur exactly once each and only in localisation, but native-speaker idiom/dialect/offensiveness review remains open.
- The GUI long-text and missing-localisation renders produced no visible difference, so visual overflow/fallback acceptance is unresolved.
- The localisation handoff's “394 focus IDs” count is stale; current source has 405 unique focus IDs.

The catalog remains materially stale despite the 2026-08-06 spreadsheet re-audit:

- `Events!C13` and `docs\spreadsheets\chaos_redux_events_catalog.csv` say Actions 71-72 are review-gated and Actions 73-76 are model-gated. The ledger says 71-72 lack Event 013 receipt/failure/cleanup owners, 73 is the review/API gate, and only 74-76 are model-gated.
- The same cell says late Scramble, world-order, constitutional, host-opening, and restoration actions remain list-only behind their political gates. “List-only in the Charter GUI” is accurate presentation wording, but the ledger classifies Actions 77-102 as implemented gameplay rows; the catalog must not imply they are unimplemented.
- `docs\events\012_africa\overview.md` is older still: it says only 90 actions are implemented and rows 73-76 plus 85-92 are blocked. Current ledger truth is 96 implemented and 71-76 blocked.
- The overview claims direct activation for DYX, DZX, and EMX, while the current country-package audit says those three lack an approved unique current-state binding and cannot pass viable-state admission.
- The overview says W5 is source-accepted, but current focus and AI evidence does not support the self-written W5 review receipt.

The Formables cluster row and evolution titles remain aligned. The Event row correctly stays `Partially Available`; it must not be promoted while the above blockers remain.

## Accepted-plan disposition

Row-level plan disposition is complete: every one of the 809 accepted matrix rows has a current status and evidence field.

Document-level promotion is not complete:

- `012_africa_final_improvement_loop_addendum_2026-08-01.md` remains the active bounded addendum and says no further broad addendum should be written until B1-B5 are implemented, queued with an exact owner, or rejected. Its header notes later W5 work, but body counts and several open/closed claims are stale.
- `012_africa_non_model_world_package_implementation_addendum_2026-07-30.md` has not been cleanly marked “implemented through W4; W5 promoted” as the final addendum instructed.
- `docs\events\012_africa\overview.md` has not absorbed the current 96/6 action disposition, the current 13/3 package reachability, the five focus MCP errors, the portrait-worker rule, or the self-certifying W5 gap.
- The August 5 focus/GUI audit is superseded by current focus diagnostics.
- The August 6 spreadsheet re-audit is not reconciled with the ledger's exact blocked-action meanings.
- Portrait production and disposition handoffs are not routed through the required `chaosx_portrait_creator` owner.
- The August 6 Charter GUI re-audit supplies explicit `chaosx_event_ui_worker` ownership, event-entry proof, layout-contract coverage, and pre/post inspect/render evidence. It remains adapter-blocked because `hoi4.gui_rewrite` rejected every safe form and the comparison route did not compare changed revisions.

No separate undocumented Event 012 gameplay patch was identified among the current bounded audit/implementation handoffs: the decision, focus-layout, country, localisation, spreadsheet, strange-force, and model tranches each have a named handoff. Some handoffs are untracked in the shared worktree, so the parent must review and preserve them before any commit or completion claim.

## Required next actions

1. Fix and rerender the five malformed external focus convergence prerequisites, then rerun all eight focus inspect/render routes and update the stale August 5 handoff.
2. Resolve the probability adapter/state gaps for decision missions, nested strategy plans, MTTH, focus eligibility, and incomplete event/random pools, then rerun the same named scenarios; keep all 64 AI rows blocked until the results are scenario-complete.
3. Redesign W5 so the review receipt is parent-owned evidence rather than three consecutive self-certifying runtime calls; retest six-candidate, five-candidate, duplicate-continent, invalid-capital, and stale-roster scenarios.
4. Close the six action gates honestly: implement Event 013 disease receipt/failure/cleanup owners for 71-72, obtain explicit approval/API for 73, and leave 74-76 closed until complete model/entity/audio/counter packages exist.
5. Add the accepted diaspora employment/jobs/education gate and result evidence without weakening consent, housing, citizenship, or local political settlement.
6. Resolve the shared mission `FROM` timer grammar with authoritative engine evidence or a spec-preserving supported architecture.
7. Obtain explicit approval/disposition for the undocumented `every_country` calls or replace them with maintained bounded rosters.
8. Complete all 16 priority packages: approve unique bindings for DYX/DZX/EMX or retain them blocked; resolve formation/release, portraits, AI, runtime, and advisor/shared-focus design decisions for all sixteen.
9. Route all grounded and fictional character portraits through `chaosx_portrait_creator`; retain grounded placeholders as pending until final replacement evidence exists.
10. Restore or relocate the elephant source/audio/counter evidence root, and finish the eight other model packages with licensed sourced audio and bespoke vanilla-green counter proof before any gate setter is added.
11. Close achievement owners and disqualifiers one row at a time and retain all 44 as blocked until their named acceptance scenarios are proven.
12. Review and preserve the completed Event 012 UI-worker handoff and direct geometry repair; obtain parent acceptance of the documented rewrite-adapter exception or rerun `hoi4.gui_rewrite` when supported, then produce a genuine changed-revision comparison and review visually distinct long-text and missing-localisation states.
13. Reconcile the workbook, overview, source map, final addendum, focus audit, country audit, asset manifests, and catalog exports to one current 96/6 and 809-row status vocabulary.
14. Rerun complete per-chain event inspect/render and event comparison when the MCP route can return bounded Event 012 graphs. Do not treat source-only review as equivalent evidence.

## Simplifications, omissions, and blockers disclosure

No fallback, gameplay fix, balance target, tag, country package, unit model, audio candidate, counter, portrait, GUI rewrite, or spreadsheet edit was introduced by this audit.

The event remains incomplete because required accepted content is blocked, deferred, or missing as documented above. The most important hidden simplifications are the W5 self-review receipt, the missing diaspora employment condition, the shared zero-branch priority focus without explicit design disposition, the grounded portrait placeholders admitted as runtime art, and the assumption that source-written registration receipts equal AI/focus acceptance.

The audit does not claim live Hearts of Iron IV acceptance. Live consumer validation remains user-owned, but absent tool, source, asset, and handoff evidence remains an agent-side completion blocker and may not be deferred silently as future polish.
