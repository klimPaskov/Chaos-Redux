# Event 19 final completion audit

> **Superseded live verdict:** This historical audit predates both owner
> approvals, the implemented recreate/prove/delete and controlled-trial
> transactions, the later near-completion improvement addendum, and the final
> neutral technical scene. Its two blockers are closed by explicit owner
> approval and subsequent implementation. Current fixed slots show 20 regional
> claimant armies/musters, 6 derivative massed hosts, and 1 neutral unassigned
> muster with no individual focal human/person. Use the newer implementation,
> asset, specialist, and final-audit handoffs for current closure evidence; the
> body below remains a dated evidence record only.

Date: 2026-07-16  
Event: `019_infantry_spawn` / `chaosx.nr19.1`  
Mode: report-only final audit; no gameplay, localisation, asset, workbook, specification, or shared-system edits by this auditor

## Final disposition

Event 19 is **not eligible for a complete claim**. Every remediable and non-approval implementation surface reviewed in this audit is clean, but two exact requested outcomes remain unavailable without an owner decision about an engine-limited substitute:

| Class | P0 | P1 | P2 |
| --- | ---: | ---: | ---: |
| Open remediable findings | 0 | 0 | 0 |
| Owner-approval / engine-capability blockers | 2 | 0 | 0 |

The blocker count is kept separate from ordinary source severity because neither item can be repaired faithfully with the exposed HOI4 scripting API. Both are completion-blocking and therefore P0-equivalent for the overall goal. No fallback or simplification has been used.

### B-019-001: exact live-division subset ownership transfer is unavailable

- **Required outcome:** transfer the chosen claimant subset of existing live divisions, preserving the exact division identities and their live state.
- **Engine boundary:** the capability gate is deliberately false at `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:172-180`. The natural-revolt preflight records the missing capability at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:677-684`, and the transfer helper at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:923-930` is definition-only and has no caller.
- **Why this blocks completion:** vanilla exposes whole-country or ratio-based transfer surfaces, not an exact division-scoped owner reassignment. Recreating, proving, and deleting the selected divisions would discard live division state and is therefore not equivalent.
- **Disposition:** blocked pending explicit owner approval of a weaker substitute. No substitute is wired.

### B-019-002: four exact same-battle achievements cannot be observed

- **Required outcomes:** `One Battalion, One Victory`, `Combined Arms, Improvised`, `Borrowed Future`, and `Barracks Babel`, defined at `common/achievements/chaos_redux_achievements.txt:3131`, `:3152`, `:3183`, and `:3204`.
- **Engine boundary:** the exact recorder at `common/scripted_effects/019_infantry_spawn_achievement_effects.txt:1142-1190` is definition-only and has no caller. Available combat callbacks do not expose the complete same-battle tuple of participating division identity, composition, battle duration, casualties, and strength needed to prove the four requirements.
- **Why this blocks completion:** a controlled-combat or post-combat proxy can produce false positives and false negatives and is not the requested exact proof.
- **Disposition:** blocked pending explicit owner approval of a weaker proxy. The four definitions remain hidden and unwired; the other seven achievements are active and wired.

## Audit scope and evidence base

The audit covered all 34 Event 19 specifications, the implementation and handoff corpus, the event workbook rows, Event 19 gameplay/localisation/UI/assets, and the shared systems Event 19 calls or modifies. The inspected Event 19 runtime surface contains 53 files and 42,793 non-localisation lines. Static cross-reference analysis found:

- 40 unique `chaosx.nr19.*` event IDs and no duplicate definition;
- 1,207 unique top-level Event 19 helper definitions and no duplicate helper name;
- 3,008 direct `infantry_spawn_* = yes` call sites covering 896 unique helpers, with no unresolved direct helper reference;
- 64 decisions and 13 missions across the ordinary, claimant, derivative, and scenario decision surfaces;
- 45 bespoke derivative focus nodes;
- 11 achievement definitions;
- one Event 19 registry implementation and one Event 19 sprite-definition file.

The audit used the offline Paradox wiki snapshot and vanilla documentation in parallel. The required core wiki pages were read, together with Interface Modding, Scripted GUI Modding, Country Creation, National Focus, Division Modding, Equipment Modding, Technology Modding, Graphical Asset Modding, and Portrait Modding. Vanilla documentation reviewed included script concepts and constants, effects, triggers, on-actions, decisions, scripted GUI, characters, equipment, and AI, plus relevant vanilla implementations. In particular, the vanilla effect and trigger documentation was checked before classifying B-019-001 and B-019-002 as engine-capability blockers.

## Requirement-by-requirement result

| Surface | Result | Evidence and disposition |
| --- | --- | --- |
| Entry event and catalogue identity | Pass | `events/019_infantry_spawn.txt:13` defines hidden, triggered-only `chaosx.nr19.1`; `common/scripted_effects/chaosx_logic_effects.txt:220` registers repeatable ID 19. The workbook classifies it as `Minor Repeatable` and `In progress`, consistent with the two blockers. |
| Manifestation and location selection | Pass | Diminishing but uncapped coverage and weighted eligible-state selection are implemented at `common/scripted_effects/019_infantry_spawn_core_effects.txt:14-158`; congestion/pressure calculation is dynamic at `:269-297`. |
| Scheduling and pulse isolation | Pass | Active-country scheduling uses `common/mtth/019_infantry_spawn_mtth.txt:10-44` with base/min/max constants at `common/script_constants/019_infantry_spawn_constants.txt:173-183`. The country pulse at `common/scripted_effects/019_infantry_spawn_pulse_effects.txt:9-70` only reschedules while relevant and owns validation, reconciliation, management, claimant, anomalous AI, evolution, and compaction work. There is no Event 19 all-country daily/weekly/monthly on-action. |
| Generation ledgers and obligations | Pass | Generation validation and append paths are present at `common/scripted_effects/019_infantry_spawn_ledger_effects.txt:108`, `:329`, `:375`, `:426`, `:493`, and `:685`; ordinary and provider obligations are recorded at `common/scripted_effects/019_infantry_spawn_generation_effects.txt:2092-2110`. |
| Lifetime compaction | Pass | Bounded compaction begins at `common/scripted_effects/019_infantry_spawn_ledger_effects.txt:747`; start, finish, and failure states are closed at `:826-855`, followed by proof scans and commits. The performance handoff found no uncontrolled whole-world cadence. |
| Muster Board and ordinary management | Pass | Player actions and effects are in `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:125-525`; GUI action routing, gates, and lists are in `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:23-228`. The ordinary liaison is exposed by `common/decisions/019_infantry_spawn_decisions.txt:686-696`, routed through `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:98` and `:199`, and dispatched for AI at `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1546-1577`. |
| Paid-family transaction safety | Pass | The transaction at `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1146-1246` snapshots resources before debit, pays provider and overhead costs, takes a structural snapshot, materialises and verifies the unit, and applies cooldown/history only after success. Failure routes restore structure and refund through `common/scripted_effects/019_infantry_spawn_management_effects.txt:4474-4865`; irreversible training authorisation is post-commit. The final transaction re-audit reports no open finding. |
| Standardisation, integration, and demobilisation | Pass | Management entry points are at `common/scripted_effects/019_infantry_spawn_management_effects.txt:649`, `:699`, and `:798`; exact standardisation preflight/rollback/commit at `:2038`, `:2187`, and `:2230`; settlement at `:2458`, `:2545`, and `:2606`; teardown at `:2617-2920`; demobilisation at `:3103-3150`; integration staff at `:3393-3404`. |
| Evolution I and II | Pass | The first two application helpers begin at `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:286` and `:304` and expand management, control, congestion, and Arsenal behaviour. Ordinary Arsenal candidates, quality, coherence, and supply logic are implemented at `common/scripted_effects/019_infantry_spawn_generation_effects.txt:243-553`; finite prototype markings and packages are at `:1575-2102`. |
| Evolution III | Pass except B-019-001 | Application begins at `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:323`; it activates claimants and the Muster Board and suppresses ordinary auto-generation through `common/scripted_triggers/019_infantry_spawn_triggers.txt:110-113`. The bounded opening registry draw is at `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:361-439`. Claimant identity, demand, takeover, failed-coup, report, and Generalissimo surfaces pass. Exact natural-revolt division transfer remains B-019-001. |
| Evolution IV | Pass | Application and anomalous-registry activation are at `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:455-474`. Claimant, zombie, ghost, and golem provider packages have isolated setup, eligibility, build, spawn, sustainment, management payment/refund, and derivative setup paths. |
| Evolution selection and event log | Pass | Four activation/log paths are at `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:515-597`; sequential selection is at `:599-616`. The event-details evolution preview is at `common/scripted_effects/chaosx_events_log_effects.txt:1897-1921`. |
| Claimant identity and takeover | Pass except B-019-001 | Twenty region-compatible identities, 20 portraits, 80 names, and 20 titles/descriptions are bound in `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:207-372`; regional compatibility is explicit at `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:27-109`. The fresh closure audit reports 60/60 claimant crosswalk hashes and P0/P1/P2 = 0. One-state/microstate routing, failed-coup closure, report rows, invalid-portrait fallback, and the visible Evolution III report image are all closed. |
| Generalissimo integration | Pass | Exact Generalissimo validation is at `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:127-158`; rival takeover resolves the failed coup at `common/scripted_effects/019_infantry_spawn_claimant_effects.txt:278-286`. Demands, costs, outcomes, and AI are implemented at `common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt:9-80` and `:426-551`. |
| Evolution IV derivatives | Pass | Private package setup and parent-state clearing begin at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:15-81`; identity and claimant/zombie/ghost/golem setup are at `:435-631`; cleanup and defeat handling are at `:2370-2776` and `common/on_actions/019_infantry_spawn_derivative_on_actions.txt:9-48`. Provider 502 is isolated from Death parent progression and provider 503 from KMB progression in `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4183-4187` and `:4334-4339`. |
| Derivative focus, decisions, and AI | Pass | The bespoke derivative tree begins at `common/national_focus/019_infantry_spawn_derivative_focus.txt:15`; all 45 nodes have icon, availability, reward, and AI surfaces. The decision audit counted 64 decisions and 13 missions, with every object carrying the required player and AI surfaces. Dedicated ordinary and scenario derivative AI strategies are present. Final focus and decision specialist audits report P0/P1/P2 = 0. |
| Ghost decline and chaos-meter bridge | Pass | Decline constants define the 180-day cadence, 0.1%-0.5% scale, and 5,000 cap at `common/script_constants/019_infantry_spawn_derivative_package_constants.txt:150-163`; application selects one controlled state and uses its dedicated death reason at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:2262-2292`. Reason ID 20 is declared at `common/script_constants/chaos_meter_constants.txt:405` and consumed at `common/scripted_effects/chaos_meter_effects.txt:1066-1073`. |
| Assets and scripted GUI | Pass | Post-remediation asset closure reports 3/3 atlases, 26/26 source frames, and 12/12 final PNG/DDS hashes matching their documentation, with all predecessor byte hashes absent. Consumer coverage is 11/11 report sprites, 7/7 Muster Board sprites, six animated/static visibility bindings, and 20/20 claimant portrait routes. Runtime frame counts/speeds are registered at `interface/019_infantry_spawn.gfx:158-198`; scripted static fallbacks are at `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:137-153`. |
| Achievement package | Blocked in part | Eleven achievements are defined. Seven are wired: `Rifle Ready`, `No Room at the Barracks`, `Quiet Demobilisation`, `The Army Voted`, `Order from Noise`, `Three False Apocalypses`, and `Every Barracks at Once`; their trackers are in `common/scripted_effects/019_infantry_spawn_achievement_effects.txt:360-823`. The remaining four exact same-battle achievements are B-019-002. |
| SCN-013 | Pass | Scenario ID 13 is declared at `common/script_constants/chaosx_triggerable_scenarios_constants.txt:26`; launch guards are at `common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt:142` and `:195`. Dynamic split actors and same-tag island/microstate routing are at `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2613-2723`; the launch and one-time host selection/cleanup begin at `:2822-2907`. All 16 type/intensity combinations use shared data tables. No `start_civil_war` or world-end setter is used. |
| History, details, and actor mapping | Pass | The core history payload records claimant appearance/takeover/failed coup and claimant/zombie/ghost/golem/anomalous revolts and defeats at `common/scripted_effects/019_infantry_spawn_core_effects.txt:514-594`; details/history scripted localisation is at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:4500-4598`. The visible claimant report uses the registered Evolution III image at `events/019_infantry_spawn.txt:679-685` and `interface/019_infantry_spawn.gfx:19`. |
| Cluster and world-end isolation | Pass | Event 19 has no registration in `common/script_constants/event_cluster_constants.txt`, `common/scripted_effects/chaosx_event_cluster_effects.txt`, or `events/chaosx_event_clusters.txt`, and does not set a world-end state. SCN-013 is a triggerable scenario, not a cluster/world-end branch. |
| Documentation and workbook | Pass | The current specifications, implementation handoffs, asset manifest, frame plans, and Event 19 workbook rows agree with the implementation. The workbook contains no formula error and preserves Event 19 as `Minor Repeatable / In progress`; `Scenarios!C11` exactly concatenates the four live SCN-013 type titles/tooltips. |

## Registry invariant

The registry isolation requirement is exact and passes:

- sole Event 19 registry implementation: `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`;
- SHA-256: `f5582496605395431ef38af798d6c56d05dd2cf91b7cf8c89d57a42f87c3d90a`;
- providers 501, 502, and 503 each expose exactly eight Event 19 callbacks: eligibility evaluation, template construction, unit spawn, sustainment reconciliation, management evaluation, payment, refund, and derivative setup, for 24 callbacks total at `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4046-4520`;
- no cleanup callback is added; cleanup remains provider registration metadata;
- parent providers register exactly once through `common/on_actions/002_zombie_outbreak_on_actions.txt:10`, `common/on_actions/010_death_on_actions.txt:10`, and `common/on_actions/005_soviet_collapse_on_actions.txt:10`;
- sole Event 19 sprite-definition file: `interface/019_infantry_spawn.gfx`.

## Asset-integrity closure

A final independent asset pass initially found one grouped P2 provenance discrepancy: nine PNG byte hashes recorded under `docs/assets/019_infantry_spawn/` reflected Pillow 11.1 encodings while the retained files reflected Pillow 12.2 encodings. Pixel decoding proved the two encodings identical, and all runtime DDS hashes and PNG-to-DDS pixels were unchanged. The parent then updated the six affected frame-plan rows and three manifest rows and documented the cross-encoder cause at `docs/assets/019_infantry_spawn/manifest.md:81-89`.

The independent focused recheck confirmed that all nine current hashes match the updated documentation, all nine predecessor hashes are absent, all runtime consumers remain complete, and final asset severity is P0/P1/P2 = 0. This P2 is closed and is not included in the open totals.

The final inventory is:

- 11 unique report DDS files at 210x176;
- 20 unique claimant portraits and six unique derivative portraits at 156x210;
- 45 unique focus icons at 100x88;
- 47 unique decision icons at 33x32;
- nine unique idea icons at 64x64;
- 33 unique achievement DDS files, forming 11 triplets, at 64x64;
- 91 unique regional flag identities at each of 82x52, 41x26, and 10x7;
- three genuine frame-authored animation packages: 8-frame 64x64 Muster seal, 8-frame 156x210 critical-command border, and 10-frame 64x64 anomalous-registry emblem, each with a static fallback, sheet, preview, contact sheet, source frames, processed frames, and runtime DDS.

## Balance, performance, isolation, and exploit disposition

- **Dynamic tuning:** manifestation pressure, quality, coherence, supply, combat/support bounds, AI timing, cooldowns, decline, and package behaviour are driven through Event 19 script constants and variables. Evolution III combat/support bounds are 1-25 and 0-5 at `common/script_constants/019_infantry_spawn_constants.txt:1635-1650`.
- **Performance:** repeated work is country-scoped and self-cancelling; world iteration is limited to bounded activation/scenario setup and one-time cleanup. Achievement continuity alone uses its dedicated daily surface, and derivative maintenance uses a 30-day cadence.
- **State isolation:** ordinary, claimant, zombie, ghost, and golem paths use explicit classification and private derivative state. Non-normal unit classification is bridged through `common/scripted_triggers/019_infantry_spawn_triggers.txt:738-799` and `common/scripted_triggers/chaosx_dynamic_triggers.txt:127` without advancing parent Death/KMB systems.
- **Transactions:** selected-family purchases, standardisation, demobilisation, and SCN-013 same-tag routing have preflight, snapshot, proof, commit, and rollback/refund surfaces. The final transaction, performance/isolation, and balance/exploit handoffs report no open finding.
- **AI:** ordinary management, claimant demands, derivatives, scenario packages, focus selection, decisions, and missions carry explicit AI logic; no player-only progression path was found outside the two deliberately hidden achievement definitions.

## Specialist handoff disposition

The following latest specialist results were accepted as evidence and cross-checked against the live source:

- `019_focus_tree_specialist_reaudit_2026_07_16.md`: P0/P1/P2 = 0;
- `019_country_package_specialist_reaudit_2026_07_16.md`: no open package finding;
- `019_registry_isolation_specialist_reaudit_2026_07_16.md`: exact registry invariant passes;
- `019_decision_mission_final_closure_2026_07_16.md`: P0/P1/P2 = 0;
- `019_localisation_specialist_final_reaudit_2026_07_16.md`: P0/P1/P2 = 0;
- `019_final_claimant_identity_closure_2026_07_16.md`: P0/P1/P2 = 0 and 60/60 claimant crosswalk hashes;
- `019_selected_family_transaction_reaudit_2026_07_16.md`: paid-family transaction passes;
- `019_performance_isolation_ai_audit_handoff.md` and `019_balance_exploit_audit_handoff.md`: no completion-blocking performance, isolation, AI, balance, or exploit finding;
- final message-only asset-integrity closure: P0/P1/P2 = 0 after focused remediation verification.

The older claimant specialist re-audit that reported four P2 items is superseded by the fresh claimant closure after those items were repaired. No superseded finding has been carried into the final totals.

## Tooling limitations

The installed HOI4 MCP was attempted as an additional, non-authoritative inspection layer:

- narrow `hoi4.event_inspect` for `chaosx.nr19.1` returned `ARTIFACT_STORAGE_LIMIT`;
- exact derivative-tree `hoi4.focus_inspect` returned `ARTIFACT_STORAGE_LIMIT`;
- exact Muster Board `hoi4.gui_inspect` returned `SCAN_BYTE_LIMIT`.

These are tool-capacity failures, not source findings. No conclusion in this audit depends on those failed renders; source, localisation, asset, workbook, vanilla-reference, and specialist evidence was inspected directly.

## Simplifications, omissions, and blockers

No fallback, placeholder, simplification, or silent omission was accepted. The implementation intentionally leaves two exact requirements unavailable rather than substituting weaker behaviour without approval:

1. B-019-001: exact live-division subset ownership transfer for the natural claimant revolt;
2. B-019-002: exact same-battle proof for four achievements.

All other requested surfaces audited here are implemented and have no open P0, P1, or P2 finding. Event 19 must remain marked **in progress / incomplete** until the owner either supplies a newly available exact engine surface or explicitly approves a documented substitute for each blocker.

## Skills used

- `chaos-redux-subagents` for ownership boundaries, specialist evidence, supersession, and completion-audit reporting;
- `chaos-redux-events` for event integration, log/detail, evolution, documentation, and workbook alignment;
- `chaos-redux-event-assets` and `chaos-redux-frame-animation` for final asset, sprite, animation, fallback, manifest, and provenance checks;
- `chaos-redux-focus-trees` for the derivative focus-tree completion standard;
- `chaos-redux-decisions-missions` for decision/mission surfaces and AI review;
- `chaos-redux-improvement-loop` for accepted improvement-plan disposition;
- `chaos-redux-mtth` for the active-country timing review;
- `xlsx` for direct workbook inspection.

## Auditor changes

This dated report is the auditor's only file change. No gameplay, localisation, asset, workbook, specification, or shared-system file was edited, and no commit was created.
