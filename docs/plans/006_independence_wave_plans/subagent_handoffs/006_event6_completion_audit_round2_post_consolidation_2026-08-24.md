# Event 006 completion audit, round 2, after registry consolidations

Date: 2026-08-24

Mode: read-only audit. This handoff is the only file created by this auditor. No gameplay, localisation, asset, workbook, generated export, or existing documentation file was edited.

## Result

Event 006 remains **HOLD / PARTIAL**.

The current authority boundary remains 32 content-attested selectable packages across 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows out of 193 non-overlay rows. The eight adapter-only rows remain fail-closed: IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM.

The recent registry consolidations are implemented source-layout changes, not new completion or admission evidence. Current maintained source validators pass after those moves. Current Event MCP acceptance does not exist: the mandatory inspect and render attempts for every identified Event 006 event chain timed out after 180 seconds, and the usable historical event revision was not present in the current compare cache. Source review and passing static validators are therefore not treated as equivalent to current event-chain evidence.

The repository was highly volatile during this audit. At the final status snapshot, `HEAD` was `7ba4ea2bc9bc4c1635279c97f8334430b52c18b2`, `git status --porcelain=v1` contained 6,288 paths, and 898 paths matched the Event 006-oriented status filter. Uncommitted work is recorded as work in progress, never as accepted completion.

## Authority and scope reviewed

The audit read every file in `docs/specs/006_independence_wave_specs/`, including all seven accepted prose parts and all maintained CSV/Markdown requirement matrices. The principal matrix sizes are:

| Accepted surface | Current design rows |
| --- | ---: |
| Candidate-country matrix | 206 |
| Package-research matrix | 206 |
| Decision/mission map | 80 |
| Formable matrix | 48 |
| Asset matrix | 49 |
| AI-strategy matrix | 24 |
| Achievement matrix | 16 |
| Idea matrix | 14 |
| Regional-overlay matrix | 14 |
| Wave-tuning profiles | 6 |
| State-anchor/reservation-group matrix | 111 |
| Source register | 74 |

Current implementation authority was read from:

- `docs/specs/006_independence_wave_specs/README.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- `docs/events/006_independence_wave/overview.md`
- `docs/plans/006_independence_wave_plans/006_event6_improvement_addendum_2026_08_24.md`
- the current Event 006 event, decision, focus, country, compatibility, registry, localisation, GUI, asset, super-event, achievement, and scenario sources
- the maintained Event 006 handoffs, including the registry-consolidation, validator-restoration, manual no-country diagnostic, current decision/focus/country/localisation audits, GUI worker handoffs, portrait/asset handoffs, and super-event evidence

The accepted design remains authoritative over implementation intent. The source-of-truth map and resume packet remain the implementation ledger, subject to the stale catalog statements and concurrent dirty changes recorded below.

## Completion status by surface

| Surface | Status | Current evidence and exact limit |
| --- | --- | --- |
| Event identity, category, log, details, and entry | **Source implemented; current MCP blocked** | `events/006_independence_wave.txt` retains `chaosx.nr6.1`; current source has the expected category/log/details registrations and no visible pre-event crisis surface. Mandatory current inspect/render calls timed out, so no current chain artifact or rendered acceptance exists. |
| Automatic allocator and wave ladder | **Implemented/proven statically for the admitted boundary** | `.tools/audit_event6_allocator.py` freshly passes 149 publishers, 126 automatic/high-chaos selectable rows, 138 SCN-008-ranked rows, 40 adapters, 32 attestations, 29 compatible groups, the 20-package standalone witness, protected remnant states, exact `3/4/5/7/10` ladder, World Collapse `10`, no pre-event crisis, and deterministic Join ordering. It does not prove live transaction execution. |
| Country API and registered tags | **Structurally proven; breadth partial** | `.tools/audit_event6_country_api.py` freshly passes 242 unique broad-surface tags, 191 resolved current tags, 34 Soviet tags, 45 African tags, zero missing and zero duplicates. Only 32 of 193 non-overlay selectable packages are centrally content-attested; 161 remain unadmitted. |
| Flags | **Structurally complete for registered runtime tags; provenance/admission partial** | `.tools/audit_event6_flags.py --strict` freshly passes 102 registered tags with complete normal/medium/small families. This does not prove historical-symbol provenance or admit an unattested package. |
| Decisions and missions | **Partial** | The accepted map contains 80 rows. Numerous accepted and package-local decision surfaces exist, and recent source/localisation cost repairs are present, but there is no current one-to-one 80-row implementation/consumer/AI/cleanup acceptance receipt. Remaining issues include category density, package cost prose, tooltip observation, and weighted AI evidence. The dedicated League Reserve icon is visible as an untracked current-worktree asset and is not promoted evidence. |
| Shared focus tree and overlays | **Partial / HOLD** | Current documented MCP evidence resolves 184 focuses and 195 connectors with zero crossings and zero node intersections. Six authored layout warnings remain after the economy-lane repair. The 14 regional overlay families have source consumers, including the recently consolidated minor-overlay registries, but a clean whole-matrix and typed probability acceptance remains absent. |
| Evolutions | **Source wired; current event evidence blocked** | Five evolution incident families are in source, with events `chaosx.nr6.360` through `chaosx.nr6.364` now in `events/006_independence_wave_support_events.txt`. Current inspect/render timed out. MTTH/weighted timing acceptance remains incomplete. |
| SCN-008 Every Banner Rises | **Static matrix pass; whole scenario partial** | `.tools/audit_event6_scenario_matrix.py` freshly passes all 32 mode/intensity cells and eight edge cases. Package readiness, typed balance, current event MCP, and live transaction evidence remain open. |
| FORM-16 | **Static contract pass; broader formables partial** | `.tools/audit_event6_form16.py` freshly passes ARM/GEO/AZR anchors 230/231/229, consent/refusal, mutation, rollback, cleanup, and fail-closed behavior. This does not close the 48-family formable matrix. |
| Formables overall | **Partial / blocked** | Current grouped consumers cover FORM-01, 02, 03, 04, 05, 07, 08, 09, 12, 13, 16, 18, 39, and 48. The remaining accepted families lack equivalent current completion receipts. FORM-42 remains blocked by design/evidence; FORM-48 remains unreachable while FSM is unadmitted. |
| Statehood Ledger and owned GUI | **Source/static matrix pass; visual acceptance partial** | `.tools/audit_event6_gui_matrix.py` freshly passes five mutually exclusive tabs, recognition/dependency/league/formable row counts, four static/animated sibling pairs, and source-state contracts. Existing `chaosx_event_ui_worker` ownership handoffs are present, so the gap is not missing worker routing. Clean current per-state/per-resolution hierarchy, click-region, rewrite, and comparison artifacts are absent. |
| Starting forces | **Implemented for admitted packages; breadth partial** | Admitted packages have source force mappings and guard logic. Unattested package rows remain outside completion. Event 006 introduces no current custom 3D unit package, so no Event 006-specific 3D audio/counter completion claim or blocker is created by this audit. |
| AI and weighted logic | **Incomplete** | The source contains allocator weights, decision/mission scores, focus/route AI, strategy factors, and timing surfaces. Existing source-linked discovery artifacts are not quantitative completion. The mandatory probability audit was routed separately; current typed evaluation/compare evidence was not available at handoff time. No balance or probability pass is inferred. |
| Portraits and country identity | **Partial / blocked** | Current authority records 38 grounded source-placeholder portrait consumers and 13 intentionally unmapped portrait consumers. Source placeholders are pending, not styled finals. Unadmitted packages continue to lack complete identity/provenance evidence. Portrait work has named `chaosx_portrait_creator` handoffs for mapped tranches, but current dirty asset/doc changes do not promote new finals. |
| Non-portrait assets | **Partial** | Core Event 006 report/news/icon and several animation/GUI families are wired, but ASSET-002/003 incident crosswalk closure, ASSET-048 variants, historical symbol provenance, and blocked-country asset families remain incomplete. Hundreds of Event 006 asset/reference paths were dirty during this audit and were not accepted as final evidence. |
| Animation | **Source/static fallback implemented; runtime proof missing** | Four Statehood Ledger frame-animation families and static DDS fallbacks are present. Runtime playback, threshold fidelity, save/load return-to-state, and clean current comparison evidence remain unproven. |
| Super-event 23 | **Blocked** | The accepted ordinary super-event is still blocked on an approved rights-cleared recording, final derived audio/checksums, wrappers, sound-definition/firing completion, and current consumer evidence. The alternate rights-complete candidate remains unapproved and cannot be substituted. |
| Super-event 24 | **Source implemented; current binary volatile** | Prior handoffs record a completed source package. `sound/006_independence_wave/super_event_24_every_border_a_casus_belli.wav` was modified in the concurrent dirty tree, so the present checksum/playback state is not re-promoted here. |
| Achievements | **Source/icon tranche implemented; reachability partial** | The 16-row accepted achievement surface and its icon family have bounded source evidence. Package/formable/scenario reachability keeps whole-surface completion open. |
| Documentation and catalog | **Stale/inconsistent** | The workbook and generated CSV currently mark Event 006 and SCN-008 `Needs Testing`, and the Liberations cluster `Partially Available`. `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `docs/events/006_independence_wave/overview.md` still state Event 006 `Partially Available` and SCN-008 `Unavailable` in their catalog summaries. The current source-of-truth map also contains historical arithmetic/status paragraphs that are labelled historical but remain easy to misread. |

## Registry-consolidation disposition

The following recent consolidations are implemented and preserve their recorded identifier/value sets. They reduce parser-file count; they do not widen the 32/29/40/161 admission boundary or close runtime evidence:

| Consolidation | Current source evidence | Completion disposition |
| --- | --- | --- |
| Ideas, characters, leader traits | 413 ideas, 68 characters, 23 traits in consolidated registries; commit `509126d97` | Implemented structural preservation only. |
| AI strategies and script constants | 637 AI top-level definitions and 377 constants; commit `7bfe...` in maintained handoff history | Implemented structural preservation only; probability remains open. |
| Support events | 13 IDs, including evolutions 360-364, FORM-05 28-34, and FORM-16 6816, in `events/006_independence_wave_support_events.txt`; commit `4d3512d5e` | Implemented structural preservation; current event MCP blocked. |
| On-actions and scripted localisation | 72 callbacks and all 54 Event 006 scripted-localisation definitions/calls preserved; commit `1302aa4c9` | Implemented structural preservation. |
| Compatibility registries | consolidated compatibility surfaces; commit `5605524ba` | Implemented structural preservation. |
| Regional triggers | 149 planner gates plus two mutex triggers in `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt`; commit `d33c98c58` | Implemented; allocator validator currently consumes the registry. |
| Regional publishers | 470 definitions including 149 package publishers in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`; commit `e62f4e6d2` | Implemented; allocator validator passes. |
| Minor overlays | IW-005, IW-022, IW-025, IW-035, IW-059, and IW-085 folded into trigger/effect/decision registries; commit `fc90da49e` | Implemented source-layout change; no admission change. |
| Maintained validators | six repaired validators restored under `.tools/`; commit `3fa88abb8` | Implemented and freshly passing in this audit. |

The later documentation consolidation commit `7ba4ea2bc` was the checked-out head at the final audit snapshot. It aligns shared-registry paths, but it does not cure the catalog-status mismatch or current MCP evidence failures.

## Accepted-plan disposition

| Accepted or current plan | Disposition |
| --- | --- |
| Retire the pre-event crisis surface | **Implemented and statically proven.** |
| Exact `3/4/5/7/10` ladder and World Collapse `10` | **Implemented and statically proven.** |
| Fail-closed transactional allocator/rollback for admitted packages | **Implemented in source and static validators; current live/event MCP receipt missing.** |
| Current 32-package attestation boundary | **Implemented. Preserve exactly; do not widen.** |
| Central breadth for 161 unattested rows | **Missing/queued.** No bulk or generic promotion is acceptable. |
| Registry consolidation program | **Implemented for the committed definition, AI/constants, support-event, on-action, scripted-localisation, compatibility, regional trigger/publisher, and minor-overlay tranches.** It is not gameplay completion. |
| Validator restoration | **Implemented and freshly passing.** |
| Five evolution families | **Source implemented; current event MCP evidence blocked.** |
| SCN-008 32-cell/eight-edge matrix | **Static acceptance implemented; typed balance/runtime completion open.** |
| Statehood Ledger/Event-owned GUI | **Worker ownership and source/static contracts implemented; clean mandatory visual evidence partial.** |
| FORM-16 contract | **Static acceptance implemented; broader formable matrix partial.** |
| Decision/mission map | **Partial.** No current one-to-one 80-row acceptance. |
| Focus layout and AI | **Partial.** Six authored warnings and weighted evidence remain. |
| Ordinary super-event 23 | **Blocked.** Rights-cleared approved audio and consumer completion are missing. |
| Ordinary super-event 24 | **Historically implemented; current dirty binary requires settled-tree re-verification.** |
| IW-050 Komi improvement addendum | **Queued / evidence-blocked / not admission authority.** It explicitly cannot be promoted until the manual transaction symptom, identity/portrait, symbol provenance, map footprint, and typed probability gates close. |

## Mandatory Event MCP evidence

The current Event 006 source has twelve identified event roots or chain entry points:

1. `chaosx.nr6.1` — main entry
2. `chaosx.nr6.36` — Join
3. `chaosx.nr6.18` — Wallonia/Frisia
4. `chaosx.triggerable_scenarios.8` — SCN-008
5. `chaosx.nr6.11` — Rhineland/Bavaria
6. `chaosx.nr6.21` — Mediterranean
7. `chaosx.nr6.360` — evolution support chain
8. `chaosx.nr6.28` — FORM-05 support chain
9. `chaosx.nr6.320` — FORM-01/02/04 support chain
10. `chaosx.nr006.6816` — FORM-16 support chain
11. `chaosx.nr006.4301` — IW-043/IW-058 chain
12. `chaosx.nr006.9301` — IW-093/IW-098 chain

For every root, a narrow read-only `hoi4.event_inspect` trace and `hoi4.event_render` neighborhood call was attempted. All 24 calls failed with the exact blocker `timed out awaiting tools/call after 180s`. An initial standalone inspect of `chaosx.nr6.1` also timed out after 180 seconds.

`hoi4.event_compare` was then attempted using the prior usable partial revision `ca55b24b392ed8604e6404d6e37b8b6d664941fc277077ed0a4b2abc7bed1ac8`. The current server returned `EVENT_REVISION_NOT_CACHED` in workspace `mod_chaos_redux_ea3b2d67c2c0`. There is consequently no current before/after comparison artifact.

The prior partial trace remains historical evidence only:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b7a54be66bf85ae4b1f23bc629195afea447a4e3cd50a5f1af9ebd0c87f0dfc/476d545919fe6b952a37415bddc4795c90521dfc9c807ca3b6f244a2c04fb4d0/event-trace-ca55b24b392e.json`

It is not current clean acceptance and does not replace the failed mandatory route.

## Fresh task-specific validation

All six maintained validators were rerun against the current, dirty working tree and exited successfully:

```text
python -B .tools/audit_event6_allocator.py
python -B .tools/audit_event6_country_api.py
python -B .tools/audit_event6_flags.py --strict
python -B .tools/audit_event6_scenario_matrix.py
python -B .tools/audit_event6_form16.py
python -B .tools/audit_event6_gui_matrix.py
```

The meaningful results are the allocator/country/flag/scenario/FORM-16/GUI counts recorded in the surface table. These validators do not cover current event rendering, weighted probabilities, live transaction behavior, localisation display, portrait provenance/finality, audio acceptance, all dirty assets, or the uncommitted recruitment registry replacement.

## Dirty-worktree limits

The current workspace cannot support an atomic completion claim. Relevant visible work in progress included:

- modified Event 006 decision, Komi, Kosovo, Kuban, Ruthenia, Tatarstan, and Udmurt trigger files;
- deleted `history/general/006_independence_wave_additional_character_recruitment.txt` and `history/general/006_independence_wave_character_recruitment.txt`, with untracked `history/general/006_independence_wave_character_recruitment_registry.txt` as an apparent replacement;
- modified Event 006 cost/technology/evolution localisation and current package documentation;
- an untracked League Reserve icon;
- a modified super-event 24 WAV;
- hundreds of modified Event 006 source/reference/processed asset files;
- multiple modified or untracked current Event 006 audits and authority documents.

The current event script files themselves were clean in the final scoped status review. That fact does not make the whole Event 006 snapshot clean. The six validators passed while the workspace was dirty; they prove only the source invariants they explicitly inspect. None of the concurrent dirty changes is attributed, reverted, promoted, or accepted by this audit.

## Concrete missing, simplified, blocked, or stale requirements

1. **Central breadth is incomplete:** 161 of 193 non-overlay selectable country rows remain unattested. This is an explicit omission, not a fallback.
2. **Current event-chain evidence is blocked:** every required inspect/render call timed out and comparison could not load the historical revision.
3. **Weighted evidence is incomplete:** there is no current scenario-complete quantitative evaluation and before/after comparison for the allocator, decision/mission AI, focus/route AI, strategy factors, or timing surfaces.
4. **Manual no-country diagnosis remains unresolved:** source inspection distinguishes empty-pool pre-mutation cancellation from later transaction failure/rollback, but no terminal receipt identifies the observed live class. This blocks safe admission work.
5. **Decision/mission matrix completion is not proven:** the accepted 80-row matrix lacks a current one-to-one implementation/AI/localisation/cleanup acceptance receipt.
6. **Focus acceptance remains partial:** six authored layout warnings and typed AI evidence remain.
7. **GUI acceptance remains partial:** worker ownership exists, but clean current per-state/per-resolution/hierarchy/click-region/rewrite/comparison evidence does not.
8. **Formable breadth is incomplete:** only a bounded subset of 48 families has current grouped consumer evidence; FORM-42 and FORM-48 retain hard blockers.
9. **Portrait and identity completion is partial:** 38 source-placeholder consumers remain placeholders, 13 consumers are intentionally unmapped, and unadmitted identities remain unresolved.
10. **Non-portrait asset completion is partial:** incident crosswalk, variants, symbol provenance, blocked-country assets, and current dirty-binary acceptance remain open.
11. **Super-event 23 is blocked:** no approved rights-cleared final recording and completed firing package exist.
12. **Catalog authority is stale:** workbook/export statuses and the current narrative authority documents disagree for Event 006 and SCN-008.
13. **IW-050 cannot be used as a shortcut:** the current improvement addendum is queued/evidence-blocked and explicitly not admission authority.

No unapproved new fallback or simplification was introduced by this auditor.

## Single highest-impact bounded next tranche

After the concurrent worktree settles, implement a **catalog/status authority reconciliation only**.

Use `docs/spreadsheets/chaos_redux_events_catalog.xlsx` as the catalog source of truth and reconcile the current-facing Event 006 authority prose to the workbook/export statuses now present: Event 006 `Needs Testing`, SCN-008 `Needs Testing`, and Liberations `Partially Available`. Update only the contradictory catalog-status statements in:

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`
- `docs/events/006_independence_wave/overview.md`

Preserve the distinct whole-event implementation judgment **HOLD / PARTIAL**, the exact 32/29/40/161 boundary, the eight fail-closed adapter-only rows, and every blocker above. Do not alter the workbook unless a catalog authority owner first finds the workbook status itself incorrect; if the workbook changes, regenerate all three CSV exports through `.tools/export_event_catalog_csv.py`.

This is the highest-impact tranche currently safe without design invention or admission widening because it removes a live source-of-truth contradiction while gameplay admission, IW-050, probability, event MCP, portrait, audio, GUI, and package-breadth work remain evidence-blocked. It is bounded, reversible, and does not imply runtime completion.

## Final completion boundary

Finished: registry-preservation consolidations, restored maintained validators, static admitted-boundary allocator/country/flag checks, SCN-008 static matrix, FORM-16 static contract, and Statehood Ledger static matrix.

Partial: event/log/details current evidence, decisions/missions, focuses, overlays, evolutions, formables, AI, GUI, starting forces beyond admitted packages, assets, portraits, animations, achievements, super-event 24 current binary acceptance, and documentation/catalog alignment.

Blocked: current Event MCP inspect/render/compare, quantitative weighted evidence, manual no-country symptom classification, super-event 23 audio/firing, user-styled grounded portrait finals, FORM-42, FORM-48 reachability, and broad country admission.

The Event 006 completion claim must remain **HOLD / PARTIAL**.
