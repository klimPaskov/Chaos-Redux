# Event 006 completion inventory — 2026-09-03

## Disposition

Event 006 remains **HOLD / PARTIAL**.

This is a bounded read-only completion inventory against the accepted specifications under `docs/specs/006_independence_wave_specs/`, the current source-of-truth map and resume packet, the current Event 006 source, dated package handoffs, the offline Paradox wiki snapshot, and installed vanilla documentation.

No gameplay, localisation, spreadsheet, asset, specification, plan other than this handoff, or runtime file was edited. No live Hearts of Iron IV execution, save/load behavior, or engine completion is claimed.

The current allocator receipt remains:

- 149 publishers;
- 126 automatic/high-chaos selectable packages;
- 138 SCN-008-ranked packages;
- 40 runtime adapters;
- 32 content-attested packages across 29 compatible reservation groups;
- 161 unattested selectable rows out of 193 non-overlay rows;
- eight adapter-only fail-closed rows: IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179;
- the automatic ladder `3 / 4 / 5 / 7 / 10`, with World Collapse also at 10.

The highest-value next implementation target is **IW-015 Galicia (`iw_015`, carrier `GLC`, state 171, `RG-171`)**, not a broad central-admission batch.

The 2026-08-30 no-additive-roster repair resolved the earlier duplicate-Castelao design blocker by preserving vanilla Fuco Gómez and Alfonso Daniel Castelao, applying the Event 006 portrait to the existing liberal leader once per generation, and restoring the vanilla portrait during cleanup. IW-015 is therefore closer to promotion than the older 2026-08-26 admission audit implies. Its remaining gates are bounded: independent portrait/rights terminology and rights acceptance, confirmation that the vanilla flag family is the accepted Event 006 opening identity, named typed probability evidence, and one fresh package audit before a parent-owned central promotion. FORM-07 can remain separately fail-closed just as the admitted CAT package does.

No adapter-only package is safe to promote directly from the present evidence.

## Authority and references consulted

The accepted design authority is:

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md`;
- parts 2 through 7 in the same `specs/` directory;
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`;
- the accepted research, package, AI, balance, formable, scenario, and asset matrices under the same specification package.

The current implementation authority is:

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`;
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`;
- `docs/plans/006_independence_wave_plans/006_event6_iw177_source_of_truth_resume_note_2026-08-31.md`;
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`;
- current Event 006 source and the dated package handoffs named below.

The required offline wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, national focuses, country creation, interfaces, scripted GUIs, achievements, and units. Installed vanilla documentation was consulted for `country_event`, event targets, `is_subject_of`, `original_tag`, script constants, decision visibility/availability, AI-strategy lifecycle, and scripted-GUI context/window contracts. These references support the source interpretation only and do not replace MCP or runtime evidence.

## Fresh Event MCP evidence and limits

Read-only `hoi4.event_inspect` trace and `hoi4.event_render` overview calls were run for each implemented Event 006 event family:

| Family | Root | Rendered selected nodes | Overview manifest |
| --- | --- | ---: | --- |
| Core release/report/cleanup | `chaosx.nr6.1` | 5 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d62e1cbc12bce23c63aea94d1e633ea52671e4a12f8e84842c9cb82db8a71d3/70953854045b94fe0944f139f3f46cc8bc5d241be5be3074c949091cbdc87e3b/event-overview-d56afb96621c-manifest.json` |
| Evolution incidents | `chaosx.nr6.36` | 7 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c09f2cd9bcd30277a50695a4c3870c29180ccb826998c791eb32823905402a9/0d7d054666c932c83b08029d39a4d3011360881169bdf03ffd89f990a198d103/event-overview-d56afb96621c-manifest.json` |
| League/host incident chain | `chaosx.nr6.18` | 5 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/774c197ac799fcb2875cf6532439424a89627fb00cbf88f4adb09d8af3f40873/68de2a10c6a9c40e3b24b79e77b14d31e8602b0879d06fe19096dd0032069d89/event-overview-d56afb96621c-manifest.json` |
| Rhineland/Bavaria chain | `chaosx.nr6.11` | 5 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c643e186c225004f9ba8f8cbc12d7db58cd7fa020b11929b0640d4255b74ff8/31d49f0351d2aca7176534fb6bcfe33f9208e7b988ea6a63f54b71d7c4d8378f/event-overview-d56afb96621c-manifest.json` |
| IW-043 CHU | `chaosx.nr006.4301` | 3 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac0cf82b9b3216bdeccdb7919743a7f84cf20fd85624d586e5d4a9a781be145e/9aefddb14fa2b206c119f9b9c80d3e4f98fbd585d66a0e621f5a2d870dd457f4/event-overview-d56afb96621c-manifest.json` |
| IW-058 ASY | `chaosx.nr006.5801` | 3 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f4f6d5d2a87502ccf145f87d2258c8cd1fd8fb25228f4eb21882062131c3808/d7995f5edaa4a79c4a34715504c493b2aa071b2f17e29b8d899e779e9cc26080/event-overview-d56afb96621c-manifest.json` |
| IW-093 DOX | `chaosx.nr006.9301` | 20 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc4774df57d39faf9377405f47f959d56b8610311c4c8c354f13eceab85fcd56/c7013bbfe079247f91211e04bb29c125c2cb02b04293c012cbb8b5bc17fec8a2/event-overview-d56afb96621c-manifest.json` |
| IW-098 SOK | `chaosx.nr006.9801` | 20 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e69afc77420c46e10b226e5379874f95745467b41ac7e1d77ab5588041a4f499/6d9d15ca0b77ce59a08b8a3d558b4e8625fa3291f3f97679f9ac1cfacfd1fb30/event-overview-d56afb96621c-manifest.json` |

All calls returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` at revision `d56afb96621c5db5d4ea7fdf4f8524e99aeab1b51652ab8d0c60f7750cc8a6b5`, graph hash `ffa45c972dd89ff8e2877e7ea21be5b0583cf4ef3d33041e66ff77a8b71287d5`, workspace `mod_chaos_redux_ea3b2d67c2c0`.

The graph differs from the 2026-09-02 authority snapshot, but comparison against revision `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570` returned `EVENT_REVISION_NOT_CACHED`. Therefore no semantic before/after event comparison is available. The projections still report zero helper expansion, workspace-scale unresolved nodes, and one aggregate blocking diagnostic. They are chain-reachability evidence only, not helper semantics, lifecycle, transaction, save/load, or live gameplay proof.

## Completion status by package and system

| Package/system | Status | Highest-impact missing requirement | Recommended owner |
| --- | --- | --- | --- |
| Core allocator and synchronized release transaction | Partial | Current source repairs cover absent-tag materialization, target/array rebinding, sovereignty scope, host ledger, committed-only report, and rollback source contracts. Fresh MCP remains partial and no cached semantic compare exists. | Event 006 parent, then `chaosx_event_completion_auditor` |
| Central country-package admission | Blocked | Only 32 of 193 non-overlay rows are content-attested; 161 remain unattested. Adapter or shell presence is not admission. | Package owners by bounded tranche; parent owns central promotion |
| Eight adapter-only packages | Partial / fail-closed | Exact ranking and gaps are recorded below. | Package owner, portrait/source worker where applicable, probability auditor, package auditor |
| Thirteen living overlays | Source-complete bounded surface | The post-event global unlock and route-active predicates keep overlays invisible before Event 006. They do not reduce the 161-row selectable-package gap. | Preserve; re-audit only after source change |
| Evolution incident families | Source-complete bounded surface | Five incident families and the Armed Birth reserve follow-through are present; full event comparison and whole-event lifecycle proof remain absent. | Preserve; Event completion auditor after graph change |
| Shared focus architecture | Bounded source/MCP pass | Current authority records 184 focuses, 195 connectors, zero crossings, intersections, long connectors, too-close pairs, or Event 006 layout diagnostics. Package-specific route depth remains admission-dependent. | Focus owner; `chaosx_focus_tree_auditor` after graph change |
| Decisions and missions | Partial | Exactly 80 accepted source rows and current cost-palette repairs exist, but remaining package cost prose, uncosted surfaces, category density, and complete typed probability evidence remain open. | `chaosx_decision_mission_auditor`, probability auditor |
| Statehood Ledger GUI | Partial / route-blocked | Event ownership and prior UI-worker handoff exist. Current inspect/render finds 48 elements, but current family-isolated hierarchy, click-region, resolution, state, and comparison artifacts were not exposed; `hoi4.gui_rewrite` remains blocked by `GUI_PATCH_PRECONDITION_FAILED`, `GUI_UNSAFE_PATCH_RANGE`, and `REWRITE_STRUCTURE_LIMIT`. | `chaosx_event_ui_worker` with exact existing Event 006 window scope |
| Formable state puzzle | Partial | Fourteen runtime-authored forms and 17 category attachments have bounded evidence; FORM-06 through FORM-47 remain fail-closed except admitted bounded families, FORM-42 is blocked, FORM-48 is unreachable through unadmitted FSM, and FORM-08 retains its researched-third-state gap. | Formable/decision owner, Event UI worker only for the Event-owned puzzle layout |
| League of New States | Partial | League gameplay source exists, but ordinary super-event 23 is blocked and final named probability/lifecycle scenarios remain open. | League owner, probability auditor, super-event owner |
| SCN-008 | Source/static partial | Eight player-facing modes by four intensities and eight edge cases pass the static matrix. Event compare, complete package availability, and named probability evidence remain incomplete. | Scenario owner, probability auditor |
| Ordinary super-event 23 | Blocked | The accepted London Brass Players recording lacks verified worldwide redistribution rights. Audio ID 23, settings wrappers, final WAV, catalog row, and firing must remain absent unless the accepted rights gate or explicit waiver is satisfied. | `chaosx_super_event_audio_researcher`, then parent; user approval required for replacement/waiver |
| Ordinary super-event 24 | Source-wired / partial reachability | Selected public-domain cue and source package are preserved, but reachability depends on factual host, collision, transaction, package, and formable gates. | Preserve; super-event audit after upstream admission changes |
| Achievements | Source-present / reachability partial | Sixteen definitions and 48 icon states are present, but signature achievements remain unreachable where package/formable admission is closed and no current row-level final receipt closes the whole family. | Achievement owner after package/formable admission |
| Portraits | Partial | The durable archive has 51 supplied inputs, 38 exact runtime mappings, and 13 unmapped candidates. Grounded rows require `chaosx_portrait_creator` handoffs, rights/role/date evidence, clear placeholder/final terminology, and exact consumer acceptance. | `chaosx_portrait_creator`, then package owner |
| Other non-portrait assets and animations | Partial | ASSET-004 is repaired. Open gates include the AEX basename collision, NWE alias set, ASSET-046 emblem coverage, BWX/chunk-3 flag sources, and the `play_on_show` animation mismatch. ASSET-040 through ASSET-043 retain source/frame-sheet/static-fallback evidence but do not close whole-event acceptance. | Asset source researcher / icon artist / frame-animation worker as classified |
| Custom 3D units and unit audio/counters | Not in accepted current Event 006 tranche | The accepted first-footprint plan explicitly authorizes no new 3D model or custom unit, and current force packages use existing dynamic archetypes. No 3D completion claim is made or required for this inventory. | None unless a later accepted plan adds a custom unit |
| Documentation, Event Details, catalog | Aligned to current bounded source | The 2026-08-29 Event Details/catalog premise is current and XLSX/export authority is preserved. Reconcile only after new gameplay admission or wording changes. | Documentation curator and spreadsheet worker after implementation facts exist |

## Adapter-only package priority inventory

### Priority 1 — IW-015 GLC: closest safe promotion candidate

Current identifiers and files:

- package `iw_015`, carrier `GLC`, anchor state 171, reservation group `RG-171`;
- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`;
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`;
- `common/scripted_effects/006_independence_wave_effects.txt` for the existing-leader portrait override;
- `history/general/006_independence_wave_character_recruitment_registry.txt` and `common/characters/006_independence_wave_characters_registry.txt` after removal of the duplicate character;
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` for adapter/attestation/preflight;
- `common/scripted_effects/006_independence_wave_join_effects.txt` for deterministic Join.

Current evidence:

- the 2026-08-30 handoff `006_event6_glc_no_additive_roster_repair_2026-08-30.md` resolves the duplicate Castelao design by using the vanilla country-leader roster and an institutional p15 territorial-defense command;
- state 171 and dormant registered `GLC` are accepted current bindings;
- package-local setup, cleanup, shared focus, decisions, AI, force mapping, parties, localisation, and portrait application/restoration exist;
- `iw_015` remains absent from central content attestation and Join by design.

Missing before promotion:

1. `chaosx_portrait_creator` must reconcile the supplied Castelao consumer's rights and the conflicting `source_placeholder` versus older `styled_final` terminology without changing bytes or relabelling evidence by assumption.
2. The asset/source owner must issue an explicit opening-identity receipt for vanilla GLC flags, or provide a rights-cleared alternative if the accepted identity requires one.
3. `chaosx_ai_probability_auditor` must evaluate named GLC package, route, decision, focus, and strategy scenarios; no source-only weight reading is sufficient.
4. `chaosx_country_package_auditor` must perform a fresh post-roster whole-package audit and explicitly permit standalone GLC admission while FORM-07 remains separately fail-closed.
5. Only then may the parent add the exact central content-attestation, runtime/SCN-008 preflight parity, capacity, and deterministic Join entries, followed by same-scenario probability comparison and Event MCP comparison if a usable baseline is cached.

### Priority 2 — IW-058 ASY, then IW-043 CHU: source-deep but portrait-blocked

IW-058 identifiers are `iw_058`, carrier `ASY`, state 676, `RG-NORTHERN-MESOPOTAMIA`, events `chaosx.nr006.5801` through `.5812`, and FORM-18. Its package-local setup, cleanup, 25-focus extension, 20 decision/category IDs, nine AI strategies, ideas, force mapping, events, cosmetics, and formable adapter are present.

The smallest missing ASY tranche is an evidence-only `chaosx_portrait_creator` pass for:

- `ASY_independence_wave_civic_national_assembly`, whose Werda evidence fails the low-resolution/later-life/1936-continuity gate; and
- `ASY_independence_wave_levies_guardianship`, whose Haydo evidence remains rights/date `needs_user_review` and whose Malik alternative lacks an exact 1936 active-role receipt.

After those two consumers pass, rerun package, asset, event, focus, decision, formable, and probability audits before adding `iw_058` to attestation and Join.

IW-043 identifiers are `iw_043`, carrier `CHU`, states `249|256`, `RG-MIDDLE-VOLGA-KAZAN`, events `chaosx.nr006.4301` through `.4314`, and FORM-12/FORM-13. Its substantial gameplay package is present, but the complete four-consumer grounded roster is not admitted: Mirsaid Sultan-Galiev remains source/rights gated and Karim Tinchurin remains rights/date `needs_user_review` because the available source is outside the accepted 1936 baseline. Preserve the CHU/IW-046 mutex and group capacity one. Complete the two portrait/role receipts and named probability audit before any central change.

### Priority 3 — IW-013 NAV: deep source, but carrier policy and rights remain unsafe

Identifiers are `iw_013`, carrier `NAV`, anchor 792 with optional 172/806, `RG-172`, and FORM-07.

The package is substantially wired, but vanilla NAV is currently living and owns state 792, while normal preflight expects a dormant candidate. This is not a local trigger typo and must not be bypassed with a fallback carrier. Generated route flags remain `needs_user_review`, the Aguirre portrait has rights/hash/terminology conflicts, central attestation and Join omit `iw_013`, and FORM-07 remains fail-closed. Resolve the living-carrier policy, portrait/flag rights, and named probability evidence before a promotion audit.

### Priority 4 — IW-177 FIJ: internally wired but multi-gate

Identifiers are `iw_177`, carrier `FIJ`, state 636, `RG-PACIFIC-ISLANDS`, and FORM-39.

The package-local adapter, setup, force, focus, decisions, AI, flags, and planner wrapper are present, and the 2026-09-01 parity repair preserves the attestation gate. The founding-chair portrait remains provisional pending a valid 1936 source/date/role/rights receipt. FORM-39 also needs FIJ/PNG/WPG member evidence, MFX reservation/identity/flag approval, and current probability/engine receipts. Keep `iw_177` outside attestation and Join.

### Priority 5 — IW-093 DOX and IW-098 SOK: broad source, not near promotion

Identifiers are `iw_093`/`DOX`/state 274/FORM-24 and `iw_098`/`SOK`/state 902/FORM-25. Events are `chaosx.nr006.9301` through `.9304` and `chaosx.nr006.9801` through `.9804`.

Both have package-local gameplay, but they still need multiple grounded leader/commander receipts, complete period/route flag families, and actual FORM-24/FORM-25 member/territory/consent/tag/flag/integration packages. DOX local medium/small flag variants are absent; SOK relies on incomplete vanilla ideology variants for the Event 006 identity. SOK also fails closed before 1938-06-17 because its accepted Event 006 leadership path is unresolved and Event 012 owns the current Siddiq identity. These are not safe near-term central promotions.

### Priority 6 — IW-179 FSM, IW-057 FER, and IW-055 NEN: research or package-boundary blockers

- IW-179 FSM (`FSM`, state 684, `RG-PACIFIC-ISLANDS`) is high leverage because it unlocks FORM-48, but it is not a safe next promotion. No candidate clears the combined named-identity, adult male, 1936 governing-role, stable image, and derivative/reuse-rights gates for `FSM_independence_wave_inter_island_congress_chair`. Keep `independence_wave_fsm_sourced_identity_ready` unset and do not restore Elias Kihleng or use a generic regional portrait.
- IW-057 FER (`FER`, ordered anchors 408/409, `RG-408-409`) has package-local source but lacks an accepted Event 006 identity, neutral flag, roster/portrait receipt, and central adapter, attestation, normal/SCN-008 preflight, dispatch, and Join branches. It is farther from promotion than the adapter-only set.
- IW-055 NEN (`NEN`, installed state 825, public group `RG-579`) remains research-only. It lacks an accepted named community/institution, portrait, symbol, gameplay package, AI, focus, decisions, lifecycle, central adapter, preflight, and Join.

## Other highest-impact blockers

### Package-scale objective

The accepted objective covers all 206 research rows: 193 non-overlay selectable packages and 13 living overlays. Current central admission covers 32 selectable packages only. The remaining 161 rows must be implemented and promoted in bounded regional or reservation-safe tranches. Do not bulk-add attestation entries and do not treat the seven shared country shells or 149 publisher wrappers as gameplay packages.

The queued first-footprint sequence remains research/ownership preparation for IW-108 Buganda, IW-136 Sindh, IW-130 Madagascar, IW-086 Tripolitania, and IW-073 Hejaz. Each has explicit cross-event ownership, identity, symbol, portrait, and package blockers in the current source-of-truth map.

### Formables and League

The 14 reviewed state-puzzle families are only a subset of the accepted 48-form family. FORM-06 through FORM-47 remain fail-closed except explicitly admitted bounded families; FORM-42 is blocked; FORM-48 is source-implemented but unreachable until FSM admission; FORM-39 depends on unclosed Pacific members and MFX; FORM-24/25 are profiles rather than complete formable packages. The next formable work should follow package admission rather than substitute for it.

The League source should be preserved while its named probability/lifecycle scenarios are completed. Super-event 23's rights blocker is independent and must not be hidden as future polish.

### GUI

The Statehood Ledger has proven Event 006 ownership, `independence_wave_status_scripted_gui`, `independence_wave_status_window`, the founding-category entry point, and prior `chaosx_event_ui_worker` evidence. Current full acceptance is still partial because the current MCP response does not expose separate hierarchy, click-region, state, resolution, or comparison bundles, and the mandatory rewrite route rejects the bounded gutter patch. The formable puzzle likewise retains aggregate/global diagnostics and needs family-isolated evidence after an owning source change. Do not route the shared scenario framework, event log, event-details framework, settings, or super-event framework to the Event 006 UI worker.

### Assets

Every grounded portrait consumer requires its own `chaosx_portrait_creator` handoff. Physical DDS/GFX presence is not admission. The current 38 exact source/runtime pairs remain grounded source placeholders unless the parent accepts a different lifecycle classification; the 13 unmapped files remain outside runtime consumers.

No custom Event 006 3D model, skeletal action, unit-audio package, or bespoke custom-unit counter is accepted in the current plan. The 3D audio/counter completion rules therefore do not create a present Event 006 blocker, but they become mandatory if a later accepted package introduces a custom unit.

## Accepted-plan disposition

| Plan/addendum | Current disposition |
| --- | --- |
| Core dynamic/release repair tranches | Implemented at source; partial MCP and no live claim |
| IW-043/IW-058 signature improvement addendum | Gameplay/source tranche implemented; package admission still blocked by complete portrait/role/rights and probability acceptance |
| IW-093/IW-098 package plans | Broad package-local source implemented; identity, flags, formables, probability, and central promotion unresolved |
| IW-177 Fiji package tranche | Package-local source implemented; portrait/date/rights, FORM-39, probability, and central promotion unresolved |
| FORM-03 phase-docket/cost addenda | Source/static implementation receipts present; probability/UI acceptance remains bounded |
| First-footprint admission addendum | Accepted and queued; no bulk promotion. Current target sequence remains research/ownership gated |
| Event 006 next-safe-tranche addendum | FSM remains the nearest high-leverage dependency but is explicitly not patchable until the source identity gate clears; do not treat it as the next safe promotion |
| Statehood Ledger GUI tranche | Source and prior worker evidence present; current rewrite/isolated-render evidence blocked |
| Super-event 23 package | Selected cue retained but runtime implementation blocked on exact rights or explicit waiver |
| Super-event 24 package | Source-wired and preserved; upstream reachability partial |

No accepted plan should be promoted into the specifications as complete while its admission, identity, formable, probability, GUI, or rights gates remain unresolved.

## Recommended implementation order

1. Complete the **IW-015 GLC promotion-readiness tranche**: portrait/rights terminology decision, flag identity receipt, named probability audit, and fresh country-package audit.
2. If and only if that audit permits promotion, apply one parent-owned GLC central patch covering content attestation, normal and SCN-008 preflight parity, capacity, and deterministic Join; keep FORM-07 fail-closed; rerun identical-scenario probability comparison and current event inspect/render/compare.
3. Complete the two missing ASY grounded portrait/role receipts, then repeat the package and probability audits before considering `iw_058` promotion.
4. Complete the two remaining CHU grounded portrait/role receipts, then repeat the package and probability audits before considering `iw_043` promotion; preserve the CHU/IW-046 mutex.
5. Resolve NAV's living-carrier policy and asset rights before any `iw_013` promotion review.
6. Treat FIJ, DOX/SOK, FSM, FER, and NEN as later tranches in the order justified by their independent source gates; do not use a formable dependency to bypass an incomplete country package.
7. After each promotion, reconcile the source-of-truth map, resume packet, package manifest, Event Details, authoritative XLSX/export snapshots, and accepted-plan disposition, then run the appropriate country, localisation, decision, focus, GUI, asset, event, and probability audits.
8. Only after the package program, formables, League, super-events, achievements, assets, GUI, documentation, and named probability scenarios close should the parent request a final whole-event completion audit.

## Validation performed and missing

Performed:

- current allocator validator: passed at `149 / 126 / 138 / 40 / 32 / 29 / 161` with the expected eight adapter-only IDs;
- exact registry and installed-map binding crosswalk for IW-013, IW-015, IW-043, IW-055, IW-057, IW-058, IW-093, IW-098, IW-177, and IW-179;
- current package audit reconciliation, including the 2026-08-30 GLC roster repair that supersedes the older duplicate-identity blocker;
- fresh `hoi4.event_inspect` and `hoi4.event_render` calls for every implemented Event 006 event family named above;
- attempted old/current event comparison, blocked by `EVENT_REVISION_NOT_CACHED`;
- required offline wiki and vanilla documentation review.

Missing or still partial:

- semantic helper/lifecycle event comparison and a cached before/after pair;
- named, typed, same-scenario probability evaluation/comparison across allocator, event, decision, mission, focus, host, League, patron, and AI-strategy surfaces;
- clean family-isolated GUI hierarchy, click-region, state, resolution, overflow, rewrite, and comparison evidence for the Event-owned windows;
- complete package admission receipts for the 161 unattested rows;
- complete 48-form family, League, super-event 23, signature achievement reachability, and asset-rights closure;
- any live/runtime, save/load, or in-game consumer proof, which is not claimed here.

## Final inventory conclusion

Event 006 is not near whole-event completion, but one package is close enough for a disciplined next promotion tranche: **IW-015 GLC** after its 2026-08-30 roster repair. The next safe work is evidence closure and a fresh package audit, not immediate central attestation. IW-058 ASY and IW-043 CHU are the next source-deep packages once their two remaining grounded portrait/role consumers are cleared. All other adapter-only packages have broader identity, carrier, formable, or research blockers.

No simplification or fallback is approved by this inventory.
