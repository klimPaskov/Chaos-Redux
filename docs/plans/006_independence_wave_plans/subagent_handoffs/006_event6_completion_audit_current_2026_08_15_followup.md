# Event 006 current completion follow-up audit — 2026-08-15

Mode: read-only completion audit against the accepted Event 006 specifications, current source-of-truth map, current handoffs, and the dirty shared worktree.

Whole-event disposition: **HOLD / PARTIAL**.

This audit does not edit gameplay, assets, localisation, the workbook or CSV mirrors, central package admission, or Git state.

## Current supersession notice (2026-08-26)

The release-gate, joint-count, and `.350` recruitment findings below are dated snapshot evidence only. Commit `7858a2b1f` supersedes the `exists = no` release wording with the dormant-country-scope predicate, and commit `d6abc3792` supersedes the unresolved joint expected-count overwrite with actual Event 005 plus Event 006 selected-count recomputation. Current `.350` behavior validates pre-defined package rosters and writes checkpoint flags, while additive NAV/GLC consumers are owned by startup history; do not use the stale passages below to drive new implementation.

## Executive disposition

The post-IW-045 routing boundary remains 149 publishers, 40 runtime adapters, 32 content-attested selectable packages, 29 compatible reservation groups, and 161 unattested selectable rows out of 193 non-overlay rows.

The automatic ladder remains `3/4/5/7/10`, with World Collapse also targeting `10`.

The accepted no-pre-event-surface rule is implemented and must be treated as closed rather than carried as a blocker.

The dormant-carrier execution repair is source-coherent for standalone Event 006 execution: pre-release metadata and package preflight use the dormant-country-scope predicate, which accepts an absent tag or an existing empty startup shell and rejects living carriers, release occurs before capital assignment and package setup, the selected anchor becomes the live capital, and setup/final validation precede durable commit.

The fixed numeric dormant-capital defect is also broadly repaired across the current package triggers, including FER's ordered 408/409 runtime anchors while vanilla history capital 563 remains permitted only before release.

At the 2026-08-15 snapshot, one high-severity central blocker remained after those repairs: the Event 006 pool-exhaustion partial branch overwrote the shared joint-plan expected-country count with the Event 006 selected count only.

In a joint Event 005+006 plan, the wrapper first calculates `Event 005 selected + nominal Event 006 target`, but `006_independence_wave_package_allocator_effects.txt:124-138` later replaces that total with the Event 006 subset when the Event 006 pool exhausts.

The shared lock and contract then require the complete package array, which still includes Event 005 rows, to equal the overwritten Event 006-only value.

The expected outcome at that snapshot was a fail-closed joint-plan rejection before release, not a partial-release exploit; the count was subsequently reconciled by `d6abc3792`, while the accepted joint Liberations path remains unproven at runtime.

No package-local tranche among IW-047, IW-048, IW-050, IW-051, IW-052, IW-053, IW-054, IW-057, and IW-060 is ready for central promotion on the current evidence.

## Corrected current invariants

### No player-visible pre-event surface — finished

`events/006_independence_wave.txt:11-14` keeps `chaosx.nr6.1` hidden and triggered-only.

The retired compatibility endpoint `chaosx.nr6.3` is also hidden and triggered-only and only clears stale crisis flags.

There is no active `independence_wave_crisis_category`, `independence_wave_open_host_crisis`, crisis-cost decision surface, or queue presentation in current gameplay source.

`.tools/audit_event6_allocator.py` checks the absence of the category, mission, cost, and queue surface and passes.

`docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md:37` records the controlling supersession as source-superseded and runtime-closed.

The remaining crisis-named scripted helpers and localisation are hard-disabled parser-compatibility residue, not an accepted visible surface.

The instruction at `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:167` to retain a “crisis queue sentence” is stale and conflicts with the newer no-pre-event authority.

### Dormant/no-country execution — bounded source pass

At the 2026-08-15 snapshot, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:204-213` defined preflight on the frozen target country and began with `exists = no`, followed by adapter, content-attestation, and origin-safety gates; current routing uses the dormant-country-scope predicate instead.

`common/scripted_effects/006_independence_wave_execution_effects.txt:15-78` validates aligned metadata, the reserved dormant country, exact package ID, force mapping, reserved anchor, and living former host before release.

At that snapshot, the reserved country check at lines 63-69 explicitly required `exists = no` and the same preflight predicate; this wording is superseded by the empty-startup-shell-capable dormant-country-scope check.

`independence_wave_instantiate_frozen_countries` releases the frozen country before the state-transfer and finalizer passes.

`independence_wave_prepare_frozen_country_packages` sets the selected anchor as capital at lines 332-342, prepares the origin, and dispatches package setup only after the country exists.

The activation, package final-validation, and durable origin-commit passes remain separately counted and fail closed.

The sponsorship-country metadata check intentionally remains a living-country check because sponsorship originates from an existing actor.

The current static allocator audit passes this order and the dormant-target requirement.

This is source/static evidence only because the Event MCP lifecycle projection is partial.

### Dormant fixed-capital validation — finished for the identified source defect

The current dirty worktree replaces all 118 fixed numeric `capital_scope = { state = N }` checks across 34 Event 006 package-trigger files with direct state-scope `N = { is_capital = yes }` checks.

Dynamic or controlled `capital_scope` checks were not indiscriminately replaced.

This closes the reported AXX/BAX/BBX invalid-target pattern and the analogous fixed-state checks in the audited package files.

### FER capital policy — finished for the reported mismatch

IW-057 may retain vanilla dormant history capital 563 before Event 006 creates the country.

The release path reanchors an executed FER package to selected state 408, then state 409 as the ordered fallback, before package setup.

Live FER readiness and setup validate 408/409 rather than treating dormant state 563 as a runtime anchor.

Do not carry the old 408/409-versus-563 mismatch as an unresolved capital blocker.

FER remains blocked by identity/rights, institutional roster, neutral-symbol provenance, typed probability evidence, route-leadership disposition, and central admission.

## Historical high-severity central blocker (superseded 2026-08-26)

### Historical finding — superseded: joint Event 005+006 partial allocation corrupted the shared expected count

`common/scripted_effects/005_006_liberations_collision_effects.txt:1266-1270` sets `global.liberation_plan_expected_country_count` to the Event 005 selected count plus the nominal Event 006 target before calling the Event 006 allocator.

`common/scripted_effects/006_independence_wave_package_allocator_effects.txt:124-138` lowers both the Event 006 target and the shared expected-country count to the Event 006 selected subset when the source-complete pool exhausts after selecting at least one package.

`common/scripted_triggers/chaosx_liberation_release_triggers.txt:222-250` and the corresponding release-contract validation require the full shared package array length to equal the shared expected-country count.

Because the full array retains Event 005 rows, a joint plan that reaches the Event 006 partial branch is expected to fail its shared count contract before ownership mutation.

The standalone Event 006 path is internally coherent because its arrays contain only the selected Event 006 rows.

The current `audit_event6_allocator.py` pass does not exercise this cross-event count mutation and therefore does not close the joint defect.

Recommended owner action: make the partial branch preserve the Event 005 contribution in joint mode, then rerun the shared release-contract audit and the same allocator scenarios through the probability auditor without widening package admission.

## Completion status by surface (2026-08-15 snapshot; superseded where noted above)

| Surface | Current status | Evidence and remaining boundary |
| --- | --- | --- |
| Accepted specification package | Finished as design authority | All seven accepted spec parts remain authoritative except the explicit no-pre-event supersession; current implementation facts belong to the source-of-truth map. |
| Canonical entry and public wave report | Bounded source pass | Hidden triggered-only `chaosx.nr6.1` owns allocation/dispatch and public `.2` follows the committed frozen plan; current Event MCP is partial. |
| No-pre-event player surface | Finished | No category, pressure mission, cost, queue, or pre-report indication remains; retired helper is hard-disabled. |
| Standalone allocator and transaction | Partial | Counts, arrays, reservation order, dormant metadata, release, transfer, setup, validation, rollback, and commit are source-wired; current engine evidence is partial. |
| Joint Event 005+006 transaction | Blocked | Partial Event 006 pool exhaustion overwrites the joint expected-country count and is expected to reject before release. |
| Country registry and admission API | Partial | 149 publishers, 40 adapters, 32 attestations, 29 compatible groups, 161 unattested selectable rows; eight adapter-only rows remain fail-closed. |
| Event chains | Partial | All twelve Event 006 event files received current inspect and render calls at the same graph revision; every result deferred workspace-wide helper/lifecycle analysis. |
| Event Log and Event Details | Partial | Shared source wiring and current catalog mirror wording exist, but whole-event GUI/Event Log acceptance remains open and the MCP event graph cannot prove the complete runtime lifecycle. |
| Evolutions | Bounded source pass / whole-event partial | Five incident families and removal-tail cleanup are source-wired; event inspect/render is partial and weighted MTTH has no supported current timing proof. |
| Shared decisions and missions | Bounded source pass / weighted partial | The accepted DM-01 through DM-62 framework and current cost/localisation repairs exist; typed eligibility, timing, and AI evidence remains incomplete. |
| Focus tree | HOLD | 184 focuses and 196 connectors, with zero crossings and zero node intersections, but two long connectors, four authored detour warnings, and aggregate diagnostics remain. |
| Country packages | Partial | Thirty-two packages are centrally attested; the nine requested recent package-local tranches remain deliberately unadmitted. |
| Map/anchors | Partial | Selected package anchors inspect successfully; KUR's 421/1001/800 policy is unresolved and current map rendering failed with an MCP internal error. |
| SCN-008 | Static source pass / runtime unavailable | The 32-cell matrix and eight edge cases pass the static audit, but the catalog correctly remains `Unavailable` and package coverage is incomplete. |
| Formables | Partial | FORM-16 passes its static source contract; other accepted formable families remain conditional, fail-closed, unadmitted, or blocked by member/package evidence. |
| Statehood Ledger GUI | Source matrix pass / visual acceptance partial | The semantic matrix passes and an event-owned GUI worker handoff exists; current MCP inspection/render returns overlap diagnostics and incomplete state/resolution/comparison artifacts. |
| Grouped formable puzzle GUI | Source-wired / visual acceptance partial | The event-owned GUI worker handoffs exist, including the FORM-12/13 update; current MCP still cannot isolate the requested family/resolution/state proof. |
| AI and probability | Blocked for completion | The required probability auditor was routed, but its fresh MCP probability route was unavailable; historical evidence remains score-only, empty-fixture, incomplete-pool, or unsupported. |
| Portraits and identity assets | Partial | Admitted packages retain their accepted evidence, but the recent unadmitted packages still have the identity/rights/portrait blockers listed below. |
| Flags and other 2D assets | Partial | The strict flag-family audit reports 102 complete registered families and 1530 required TGA files in prior strict coverage; that does not clear historical provenance or admission for the recent packages. |
| Animations | Partial source evidence | Statehood static/animated sibling contracts are present, but current visual-state acceptance is incomplete. |
| Achievements | Source-present / reachability partial | Sixteen definitions, 48 localisation keys, 48 icon variants, and proof writers are source-present; several proofs still depend on unadmitted packages, formables, League paths, or high-chaos reachability. |
| Super-event 23 | Blocked | Image/text registration exists, but the accepted recording cannot yet be redistributed under the required rights/jurisdiction conditions; final audio, wrappers, dispatch, and firing remain blocked. |
| Super-event 24 | Source-wired | Final audio, base sound, wrappers, slot dispatch, presentation predicates, and settings-aware queued playback are wired; reachability remains conditional on the dangerous milestone predicates. |
| Documentation and catalog | Partial | Generic Event 006, SCN-008, and Liberations statuses are aligned; several FER, roster-relocation, and no-pre-event references remain stale or contradictory. |
| Custom 3D units, unit audio, and counters | Not in accepted scope | No Event 006 custom 3D unit or unit-sound/counter package was identified, so no missing 3D worker handoff is asserted. |

## Package-local tranche disposition

| Package | Implemented package-local facts | Actual remaining accepted blockers |
| --- | --- | --- |
| IW-047 MEL | State 833 package-local source; FORM-12/13 rebind across specs, helpers, manifests, generated pieces, DDS/GFX, GUI, scripted localisation, and processed evidence; state 256 is historical traceability only. | Zinovy Zhadinov identity/portrait rights; neutral 1936 symbol provenance; quantitative AI/mission evidence; central adapter, attestation, preflight, scenario, and Join review. |
| IW-048 UDM | Vanilla UDM/state 399/Boris Berman/vanilla flag baseline; local mission, ten projects, ideas, AI, cleanup, localisation, and five focus callbacks. | Parent acceptance of vanilla identity/assets; state-399 host/anchor proof; p48 `industrial_security` versus shared `industrial_breakaway` mapping disposition; typed probability and same-scenario compare; current whole-event MCP; central wiring. |
| IW-050 KOM | State 397, p50 force contract, ledgers, four routes, ten projects, local decisions/ideas/AI/localisation/focus/cleanup, and roster checkpoint source. | Pavel Murashev identity/portrait rights; neutral/route flag provenance; typed mission fixtures; central admission. |
| IW-051 YAK | Existing state 574 anchor with optional 644/876/877; package-local mechanics and source-backed Pavel Pevznyak opening candidate behind an unset rights flag. | Released-identity/origin proof; runtime portrait DDS/GFX; flag provenance; host-remnant proof; typed mission/random-list evidence; central wiring. |
| IW-052 BYA | Vanilla BYA/state 564/p52 package-local mechanics and guarded vanilla roster baseline. | Parent identity choice between the conditional Erbanov group source and the non-top-leader Markizov alternative; rights clearance; runtime DDS/GFX/character consumer; neutral flag; typed probability; central wiring. |
| IW-053 ALT | State 654 with optional state 40; package-local mechanics, AI, decisions, localisation, and focus callbacks. | Gurkin/Yufit role/date/rights evidence; neutral flag provenance; accepted p61 tradition 61 versus shared p61 value 57 disposition; typed probability; central wiring. |
| IW-054 KHA | State 569/p55 package-local mechanics, AI, decisions, localisation, cleanup, and focus callbacks. | Identity and institutional-roster receipts; Event 005 collision and host-remnant policy; Sizyh role/rights; neutral or route-specific flag provenance; typed probability; central wiring. |
| IW-057 FER | Package-local mechanics, AI, decisions, localisation, five focus callbacks, and corrected dormant/live capital lifecycle with ordered runtime anchors 408/409. | Opening identity/portrait rights; concrete roster consumer; neutral/provisional symbol provenance; route-leadership disposition; typed probability; central wiring. |
| IW-060 KUR | Package-local state-421 design, p72 mechanics, AI, decisions, localisation, cleanup, and focus callbacks. | Public/source anchor 421 versus installed binding 1001 and vanilla capital/Form-18 state 800; Seyid Riza portrait rights; neutral 1936 pan-Kurdish symbol; identity/roster receipts; typed probability; whole-event MCP; central wiring. |

IW-055 NEN remains research-only and must not be inferred as a package-local or central gameplay tranche.

IW-045 BSK remains the latest centrally admitted package and current deterministic Join boundary.

The deterministic Join order is IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-038, IW-040, IW-044, IW-045, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, and IW-184.

The eight adapter-only fail-closed IDs remain IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM.

## Accepted-plan disposition

The seven accepted specification parts remain the design authority and have not been narrowed by the recent package-local work.

The no-pre-event rule supersedes the former visible crisis design and is implemented.

The shared allocator/transaction, registry API, active ladder, static standalone witness, five evolution incident families, 32-cell SCN-008 source matrix, shared focus source, and Statehood Ledger source matrix are bounded implementation milestones, not whole-event completion.

IW-047, IW-048, IW-050, IW-051, IW-052, IW-053, IW-054, IW-057, and IW-060 are implemented only to their package-local fail-closed boundaries and have no accepted promotion into shared adapter, attestation, normal/scenario preflight, or deterministic Join.

IW-055 NEN remains research-only.

FORM-16 is a bounded static source pass; broader FORM-01 through FORM-48 coverage is not complete merely because the shared registry and grouped GUI exist.

Super-event 23 remains blocked exactly on its accepted recording and rights path; no replacement may be inferred.

Super-event 24 remains source-wired and must not be weakened while other blockers are addressed.

The generic catalog disposition remains Event 006 `Partially Available`, SCN-008 `Unavailable`, and Liberations `Partially Available`.

No safe central admission tranche follows from this audit.

## Dirty-worktree findings

The shared worktree contained approximately 1470 status rows at the end of the audit, most outside this bounded Event 006 review.

Current Event 006 changes include the no-pre-event retirement, dormant metadata fix, 118 fixed-state capital-check replacements, FER package work, package-local decision/localisation work, focus callbacks, IW-093/IW-098 constant-compatibility changes, and allocator partial-pool behavior.

### Historical startup character recruitment relocation snapshot (superseded 2026-08-26)

`events/006_independence_wave.txt` removes fifteen additive `recruit_character` calls from hidden checkpoint event `.350`.

The untracked `history/general/006_independence_wave_additional_character_recruitment.txt` recruits those fifteen characters for MNT, KOS, RUT, MAC, AXX, BAX, BBX, BOS, NAV, and GLC during startup history, while `.350` retains package-conditional roster checkpoint publication.

This relocation does not reintroduce a player-visible pre-event category, mission, cost, queue, or report.

However, `006_event6_roster_checkpoint_dm01_relocation_current_2026_08_15.md` still states that `.350` performs the KOS and RUT additive recruitment and is stale against the current dirty source.

`006_dirty_gameplay_architect_review_2026-08-03.md:25` explicitly rejected recreating a broad static `history/general` recruitment source and required per-country history if recruitment moved out of hidden events.

The proposed `006_iw057_fer_identity_roster_symbol_receipt_addendum_2026_08_15.md` instead treated startup recruitment through this `history/general` file as the current pre-event repair pattern.

That is a real authority conflict rather than a source-only typo.

The owner must accept one recruitment authority, document the dormant-tag lifecycle and retry semantics, and update the stale `.350` handoff.

The current event comparison route could not compare the removal to a cached baseline, so no current before/after event-lifecycle proof exists for this relocation.

### Weighted source deltas require true same-scenario comparison

`events/006_independence_wave_iw093_iw098.txt` replaces four `ai_chance` conditions that used shared `constant:` references with numerically equivalent file-scoped aliases.

The probability auditor identified this as the mandatory current compare target and could not run the fresh route.

The Event 006 allocator partial-pool branch also changes the effective weighted selection terminal behavior and needs the same complete-pool scenarios before and after repair.

No quantitative equivalence or balance claim is made from source similarity.

## MCP evidence and exact limits

### Event Chain Viewer

All twelve Event 006 event files were inspected and rendered at current graph revision `a0d209ec728fe48cc44e3412c64b7c86ab0d1fea28713348d4dac1ba52035c67`, graph hash `fe13a4e6ac4449272ea587b4a0d9f752629b1d69acc4e84bc21d2952fbdde7d8`.

Every inspection returned `EVENT_INSPECTED_PARTIAL`, every render returned `EVENT_RENDERED_PARTIAL`, and the selected results had zero blocking diagnostics.

Every result carried the same validation limit: `Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked`.

| Event file | Inspect artifact ID | Render artifact ID |
| --- | --- | --- |
| `events/006_independence_wave.txt` | `4cd192ae7dedd27c.../62d6e97244849dfc.../event-scan-a0d209ec728f.json` | `cb45e431aea3c280.../74805bd5efa7f62b.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_join.txt` | `e2c86f5836cf3660.../c464b57ed8694bba.../event-scan-a0d209ec728f.json` | `d0171831.../ae344a98.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_scenario.txt` | `45b9ac9f.../61fa72d4.../event-scan-a0d209ec728f.json` | `3bbef539.../8a59f37e.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_rhineland_bavaria.txt` | `6fec2322.../24ed4bcc.../event-scan-a0d209ec728f.json` | `8d53e547.../96fb4c0f.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_wallonia_frisia.txt` | `f3f82122.../29317414.../event-scan-a0d209ec728f.json` | `1c9eb65f.../3da4d167.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_mediterranean.txt` | `50acdd5f.../ffc5a5e7.../event-scan-a0d209ec728f.json` | `b943f89d.../3cdfe0c3.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_form01_02_04.txt` | `2fa8d86ce2329dc4.../52f3c1a7718aee83.../event-scan-a0d209ec728f.json` | `91e6a4a3.../8b67971e.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_form05.txt` | `ef093215a0870c52.../5850a1072dd30de4.../event-scan-a0d209ec728f.json` | `9df83f5b.../9c17344b.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_form16_events.txt` | `70df7620.../15a40754.../event-scan-a0d209ec728f.json` | `b9024056.../c6425464.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_iw043_iw058.txt` | `0dd0b67a.../ad83ac49.../event-scan-a0d209ec728f.json` | `41c5e5e4.../58dd541a.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_iw093_iw098.txt` | `d5ea8c7accffe71f.../3e9166412a87a230.../event-scan-a0d209ec728f.json` | `d7b01cb.../ad8e24e6.../event-overview-a0d209ec728f-manifest.json` |
| `events/006_independence_wave_evolution_incidents.txt` | `cf82054e.../388d0b96.../event-scan-a0d209ec728f.json` | `bd877940.../01ec21b0.../event-overview-a0d209ec728f-manifest.json` |

The core state-flow evidence is also recorded by `006_event6_dormant_release_audit_2026_08_15.md` as inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62395d101a35e8ba9adbd53a6a64e1a92fc904294746fc74fc72d8ae1d48cbe8/f9564375907b9895c1bd912686cc2a82f91196183c23ae32512302edbc1147f9/event-state_flow-a0d209ec728f.json` and render manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e518a4ead46cba32e0cfbd32d5d4dac2b44523d3800d9d4885906493720148c7/858a2e321160c3fe1d4195c946886ed3b3dbe4957474224c79a66544352f278d/event-state-a0d209ec728f-manifest.json`.

The attempted comparison from historical revision `76e767e6fb64...` to current revision `a0d209ec...` failed exactly with `EVENT_REVISION_NOT_CACHED — Requested event graph revision is not cached`.

The attempted proposed-source comparison against HEAD failed exactly with `EVENT_BASELINE_MISSING — Scan the workspace before comparing proposed source`, even after a current scan.

No before/after event comparison is claimed.

### Focus Tree Viewer

Current focus inspection returned `FOCUS_INSPECTED` at revision `6ea0db179401c9e73cec973002cabf4717a1de01b5447142ff57e0f8982c52e1`.

It reported 184 focuses, 196 connectors, zero crossings, zero node intersections, two long connectors, four linear-detour warnings, and 14 aggregate blocking diagnostics.

Thirteen diagnostics are missing installed-vanilla continuous-focus icons rather than Event 006 source defects.

The remaining Event 006 layout warnings are authored geometry that still requires owner acceptance or a separately authorized owner repair and comparison.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2945595a94c09909797e9594e18e99ac7d031333571fe62fbe6522c1764459d/49ada9c198ae79dbc47244a6d00a74332d10863bb290db3f39beab7b36ead3f6/focus-inspect.6ea0db179401c9e7.json`.

Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7c9b549edb4c5de99092cffe5c5f8178ddad2edece401e952702b873cca9510/6fd46f56385c562f8f01ef3cefb1d001447f10e9dc7b6814103a217e5ec6d669/independence_wave_focus_tree.focus.html`.

### Map Viewer

The current map inspection selected states 40, 397, 399, 408, 409, 421, 563, 564, 569, 574, 644, 651, 654, 800, 833, 876, 877, and 1001.

It returned `MAP_INSPECTED` at revision `bc36dc62...` and loaded all 18 requested state records.

Requested state membership, bitmap geometry, region membership, adjacency, supply, and railway checks passed.

Workspace-global locator validation remained false because of 1323 building-position and 1331 port-adjacent-sea diagnostics, with the response truncated; those diagnostics were not attributed to the selected Event 006 states.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/338b9231ffe2d8a9615c211ebe28f9d4ed2ce0abe0ad0f578001badcfb90a697/6db021d511e8cdddc4ff804f7a46a240258f7ace8f8372aacdbf42e66f64b70d/map-inspect.bc36dc62d63f9fc2.json`.

The fresh current state-layer render failed exactly with `INTERNAL_ERROR — Unexpected internal error` and returned no artifact.

Earlier package-specific render artifacts remain historical bounded evidence, but they are not a current map-render substitute.

### Scripted GUI Viewer

Both event-owned scripted GUIs have the required `chaosx_event_ui_worker` handoffs.

The Statehood Ledger handoff is `006_iw006_statehood_ledger_gui_worker_2026_08_06.md`.

The grouped formable-state-puzzle handoffs are `006_event_ui_worker_formable_state_puzzle_gui_handoff_2026-08-14.md` and its 2026-08-15 update.

No GUI-worker handoff is required for the shared Event Log, Event Details framework, settings UI, super-event framework, or shared scenario UI.

Current Statehood Ledger inspection returned `GUI_INSPECTED` at revision `a05c59b2...`, with 48 selected elements, 75 selected `GUI_VISIBLE_OVERLAP` diagnostics, and a workspace-global diagnostic set truncated at 2000 blockers.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67d39c3ca55864d1bdf5fe68820df1b5ab1ba8465e91c8f013a67c7594650dc5/359cb1be833f4249dfd2315ce982dd76dbac8941f8ad3a39a75840778aafe238/gui-inspect.a05c59b2ccdc32b5.json`.

The render request covered all fourteen states, 1920x1080 and 1366x768, and a comparison scenario, but returned only one full SVG and `MCP_RESPONSE_TRUNCATED` because the response was 40194 bytes.

Returned SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d245b460614d138be4d724b8fbbe4c0c3ae510648ae12c90abf3733e231c13/d56cf75c51fe753cf739698867f9bddfc664ae9fc3523f471314e8661110ec2f/independence_wave_status_window-full.svg`.

Current grouped-formable inspection returned `GUI_INSPECTED` at revision `504bdf865...`, with 93 selected elements and 1042 overlap diagnostics dominated by co-located mutually exclusive family definitions, plus the same global truncation class.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b5d948a3f286e97c479f362d9dbc939157d9f23300d67b426ab17ca122f70bb8/11a699a6b96a17acd54eb16bac33c2fa6108ef410a68101df2ed96177b7e92ba/gui-inspect.504bdf865a70c22f.json`.

The render request covered FORM-12 with related FORM-13, all states, two resolutions, and a comparison scenario, but returned only one full aggregate SVG and `MCP_RESPONSE_TRUNCATED` because the response was 41874 bytes.

Returned SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0d6628e50f989b4c7b7264b970286e228543cf35b7af4a53813387d4ae62f51/562636c90ba4bbd326f0f4b2abfb66d5f36495c15e24b224f993632d17d7140d/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The current GUI route did not return separate crop, annotation, hierarchy, click-region, state, resolution, or comparison artifacts for either window.

The older worker handoffs retain pre/no-op evidence, but the current family-specific and multi-resolution acceptance proof remains incomplete.

No GUI rewrite is justified by this read-only audit.

### Probability workflow

The complete weighted inventory was routed to `chaosx_ai_probability_auditor` as required.

The auditor's mandatory fresh call to `hoi4.probability_inspect` for the dirty IW-093/IW-098 event-option surface failed exactly with `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`.

The auditor could not perform fresh evaluate, sweep, simulate, sequence, render, or true same-scenario compare calls in its runtime.

This route-specific blocker is not replaced by direct source review.

The weighted inventory includes event-option `ai_chance`, shared and package mission/decision `ai_will_do`, the shared and package focus score race, the outer fourteen-region and inner regional package `random_list` pools, formable success/failure random lists, package AI strategies, and evolution MTTH.

Historical bounded evidence remains usable only at its recorded limits:

- Core event-option inspection found 20 candidates, zero available, 13 required inputs, an incomplete pool, and one unresolved value under an empty scenario; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebf6bff0e3403d6f2f586014cf2126a1ed52e88573098538c6a78b6391a1a989/a99789fe32cde798d4b4a63ccadc6a3ab12bb43017f6af6d223142d01f936d6b/probability-inspect-b97c0de3de07.json`.
- Shared focus inspection found 184 candidates, 15 required inputs, and an incomplete pool; it proves no named route-state ranking or normalized click probability; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6278d1595ecf6ddd5234cf5cb7351b348f670b0cae26bc7c1bfe0f4e2b0adff/47175fae71b2e74c7203fc8abe3cebcb089c4673c4f5b5b4e3be0fc03471da8a/probability-inspect-c46802f6db53.json`.
- The outer allocator inspection found fourteen source-level region entries and a complete outer pool, but zero available entries and unresolved inner-package availability; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67f51637c58748a683f37bcb6a7246318c44d909bda907fe2a914215ecdc39e2/5d0f8ae36933aafc0a421e2f23431f94187d5c7eaca5dccbcf1d4eaa69db2b55/probability-inspect-bc6f7ff8598d.json`.
- UDM historical inspection found eleven source mission candidates, zero available, fifteen required inputs, and no numeric balance conclusion; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/05794e499c9f97759789ba9c25e95a3601772a72960aa671b74192e568f87bfa/a1b53ec3bf1a41ecc313d6cc418ecdd66befd529e7d325e0cbaa5eee75610a62/probability-inspect-cae802712e77.json`.
- YAK historical inspection found eleven missions under an empty unadmitted-state scenario and no valid ranking or probability; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d40cbba6d58aa615e4e841d1394bfe358f08d245542ecee4988c71feafe84bc4/12ce5ef6061e8b425236242108a25d1fb178d5cb84396ac77d511925b11839c6/probability-inspect-5c508a1eaf9f.json`.
- FER historical inspection found eleven missions across twelve explicitly empty typed scenarios, zero available candidates, fifteen required inputs, an incomplete pool, and 135 unresolved evaluation rows; inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17e0fc763ab5961a183137cef30d4b6c2f3af715edc9a4e4b1adf3723a0f5929/2d7ae0a1976bbadd7832d75dd4a5117ae274f4669fa63d35f7b6585a91efaf83/probability-inspect-d5c1417fc7a7.json`, evaluate artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6a8887ebe1d850fede912c1d57489c7db580099ccbde23155b75b03cf501107/d32820d5f7dbff95aa895811383a20ae673e0109ad4d52bf80e9fe8a199efc60/probability-430cca0af78c796f8bae6d73.json`.

MEL and KOM strategy inspection historically discovered no probability-weighted surface; static AI strategy directives are not normalized probabilities.

BYA, ALT, KHA, and KUR have no current typed package probability receipt.

The evolution MTTH adapter historically exposed no supported weighted surface, so no timing distribution is proven.

No dominance, starvation, rank reversal, repetition, timing drift, snowball safety, or normalized campaign probability conclusion is supported for whole Event 006.

## Task-specific static validation

`python .tools/audit_event6_allocator.py` passes with 149 publishers, 126 automatic/high-chaos selectable rows, 138 SCN-008 ranked rows, 40 runtime adapters, the exact eight adapter-only rows, 32 content attestations, 29 compatible groups, a 20-package static standalone witness, and the `3/4/5/7/10` ladder.

That audit also verifies no active pre-event crisis category, mission, cost, or queue and checks anchor/compact/extended/lock order.

`python .tools/audit_event6_country_api.py` passes with 242 broad unique tags, 191 resolved unique carriers, 34 Soviet rows, 45 African rows, zero missing tags, and zero duplicates.

`python .tools/audit_event6_scenario_matrix.py` passes all 32 SCN-008 cells and eight edge-case receipts.

`python .tools/audit_event6_flags.py --strict` reports 102 registered Event 006 tags, 102 complete flag families, and zero incomplete registered families.

`python .tools/audit_event6_form16.py` passes exact ARM/GEO/AZR membership, states 230/231/229, consent/refusal, mutation, rollback, cleanup, and fail-closed readiness.

`python .tools/audit_event6_gui_matrix.py` passes the Statehood Ledger semantic source matrix for five tabs, recognition/dependency/League/formable frames, cleanup variables, and four static/animated sibling pairs while explicitly making no runtime-render or save/load claim.

These static passes do not detect the cross-event expected-count overwrite, establish complete probability behavior, clear identity/rights evidence, or replace the partial MCP routes.

## Documentation, asset, and handoff gaps

The current source-of-truth map correctly records FER's package-local source and closed dormant-capital policy.

The following current-looking documents remain stale about FER and should be superseded or reconciled rather than used as authority:

- `006_iw057_far_eastern_republic_admission_audit_current_2026_08_15.md` still frames the capital policy as unresolved.
- `006_iw057_far_eastern_authority_docs_reconciliation_2026_08_15.md` still says the capital policy is pending.
- `006_current_registry_gap_map_2026_08_15.md` still states that no package-local FER source exists.
- `006_next_safe_registered_package_audit_current_2026_08_15.md` still says FER has no local mechanics.
- `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md:13` still says FER is outside gameplay; central admission remains false, but “outside gameplay” is no longer accurate.
- `006_event6_completion_reaudit_current_2026_08_15.md` predates the FER capital repair and carries the superseded capital blocker.

The startup roster relocation has no current implementation handoff that reconciles the new history-general source with the older architect prohibition and the stale `.350` handoff.

The current source-of-truth map's “crisis queue sentence” instruction must be retired to match the accepted no-pre-event rule.

The generic workbook mirrors are not stale: Event 006 is `Partially Available`, SCN-008 is `Unavailable`, and the Liberations cluster is `Partially Available`.

Grounded portrait blockers for MEL, KOM, YAK, BYA, ALT, KHA, FER, and KUR still require `chaosx_portrait_creator` handoffs and the repository's explicit pending/final evidence chain.

No archive presence, wired source placeholder, vanilla portrait token, or strict flag-family count by itself clears identity rights, historical role, neutral-symbol provenance, or central package admission.

No undocumented copied counter, placeholder counter, custom 3D unit, generated unit audio, or synthesized unit-sound fallback was found in this accepted Event 006 scope.

## Remaining blockers in recommended order

1. Repair the joint Event 005+006 partial-pool expected-count mutation while preserving standalone partial Event 006 behavior, then validate the complete shared package-array count before release.
2. Resolve the startup character recruitment authority conflict, write a current implementation handoff, and obtain an Event MCP before/after comparison once the baseline route works.
3. Restore the probability auditor's callable MCP route and run true same-scenario comparisons for the IW-093/IW-098 `ai_chance` compatibility delta and allocator terminal-behavior delta.
4. Choose one package-local candidate for the next admission only after its identity/rights, flag, map/host, force/archetype, typed probability, cleanup, and current MCP packet is independently complete.
5. Resolve KUR's 421-versus-1001-versus-800/Form-18 map authority before any KUR promotion.
6. Reconcile the stale FER, roster, and no-pre-event documentation listed above.
7. Obtain family-isolated, multi-resolution, state, hierarchy, click-region, and comparison evidence for the two event-owned GUIs or record an explicit accepted route limitation.
8. Accept the authored focus warnings or authorize a bounded owner repair followed by focus comparison; do not treat missing vanilla continuous-focus icons as an Event 006 source defect.
9. Keep super-event 23 blocked until the accepted recording passes the required redistribution, jurisdiction, human-listening, and production gates.
10. Preserve the current catalog status until package coverage, scenario availability, and whole-event static acceptance actually change.

## Simplifications, omissions, and blockers disclosure

No gameplay, assets, localisation, spreadsheet, or central-admission file was changed by this audit.

No live-game, save/load, player-visible runtime, or campaign-probability claim is made.

Event comparison, current map render, complete current GUI evidence, and fresh probability evaluation were unavailable for the exact reasons recorded above.

The audit therefore supports a precise **HOLD / PARTIAL** disposition and does not support an Event 006 completion claim.

Skills used: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, `chaos-redux-focus-trees`, and `chaos-redux-decisions-missions`.
