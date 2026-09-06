# Event 006 completion-gap reaudit — 2026-09-06

## Audit disposition

Event 006 remains **HOLD / PARTIAL**.

This is a read-only completion audit of the current checkout against the accepted Event 006 specifications, the current source-of-truth map and resume authority, the implementation, dated handoffs, asset manifests, catalog exports, static validators, and the available HOI4 MCP routes.

It is not a completion claim and does not treat source inspection, static validators, or partial MCP output as runtime proof.

No gameplay, asset, localisation, workbook, or generated catalog file was edited by this audit.

The checkout changed concurrently while the audit was running. The MCP graph revision moved between requests, and several Event 006 files contain uncommitted work from other agents. Findings about the current checkout therefore describe the observed 2026-09-06 working-tree state rather than a single immutable commit.

## Controlling authority

The audit used the following as the current authority chain:

- `docs/specs/006_independence_wave_specs/006_independence_wave_part_1.md` through `006_independence_wave_part_7.md`, including the accepted acceptance criteria in Part 7.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`.
- `docs/plans/006_independence_wave_plans/006_event6_iw177_source_of_truth_resume_note_2026-08-31.md`.
- `docs/plans/006_independence_wave_plans/quality/spec_acceptance_checklist.md`.
- The current implementation and the latest dated implementation, audit, asset, and catalog handoffs.

The older whole-event completion audits remain useful evidence, but their counts and blockers were reconciled against the current source-of-truth files and current validators rather than copied forward unchanged.

## Current authoritative boundary

| Boundary | Current count or rule | Status |
|---|---:|---|
| Accepted registry rows | 206 | Accepted design inventory |
| Selectable non-overlay rows | 193 | Allocation universe |
| Overlay-only rows | 13 | Bounded overlays; do not count toward selectable package closure |
| Content-attested selectable packages | 32 | Implemented source boundary |
| Compatible reservation groups represented by attestations | 29 | Implemented source boundary |
| Runtime adapters | 40 | Eight exceed the attested package boundary |
| Unattested selectable rows | 161 | Primary completion blocker |
| Adapter-only, fail-closed IDs | 8 | IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, IW-179 |
| Automatic/high-chaos selectable entries | 126 | Static allocator inventory |
| SCN-ranked entries | 138 | Static scenario inventory |
| Automatic ladder | 3 / 4 / 5 / 7 / 10 | Implemented static contract |
| World Collapse allocation | 10 | Implemented static contract |

The current static allocator reports 149 publishers, 126 automatic/high-chaos selectable entries, 138 SCN-ranked entries, 40 adapters, 32 attestations across 29 groups, and 20 static witnesses. It passes the 3/4/5/7/10 ladder, World Collapse 10, Event 005-before-Event 006 reservation ordering, and retired pre-event crisis checks.

These counts define a bounded implementation, not the accepted 206-row package goal.

## Requirement-by-requirement status

| Surface | Status | Current evidence | Remaining gap or blocker |
|---|---|---|---|
| Entry, allocation, release, report, rollback, cleanup | Partial | Root event source, allocator, dynamic custom-carrier materialisation, array rebind, host-survival rollback, and success-only report publication are present. Static allocator and SCN publication validators pass. | Root MCP inspect/render is partial. No engine/runtime proof of full allocation, release, failure rollback, and cleanup transaction exists. |
| Chaos ladder and allocation ordering | Finished in source/static scope | Exact 3/4/5/7/10 ladder and World Collapse 10 pass. Event 005 reservations precede Event 006 reservations. | Live/runtime consumer proof remains outside this audit. |
| No-pre-event player surface | Conflict in current checkout | The accepted authority retires the pre-event crisis and requires Event 006 player surfaces to depend on the real Event 006 origin. | Current uncommitted Event 021 compatibility predicates widen Event 006 player-surface eligibility. This conflicts with accepted origin separation and requires an explicit disposition before it can be accepted. |
| Event chains and evolutions | Partial | Root and five accepted evolution families are source-wired: integration, Balkan fragmentation, North American infighting, African decolonisation, and restoration. Event log/detail/evolution localisation is present. | Available MCP inspect/render results are partial; several chain calls timed out. No stable-revision compare or complete runtime reachability proof exists. |
| Country/package coverage | Partial / largest gap | 32 attested selectable packages across 29 compatible groups; 40 adapters. Current country API validator reports broad 242, resolved 191, Soviet 34, Africa 45, missing 0, duplicate 0, and IW-031 pass. | 161 selectable rows remain unattested. Eight adapter-only IDs fail closed. Generic registry presence, adapter dispatch, or country API resolution is not package completion. |
| Focus trees | Partial | Main Event 006 tree has 184 direct focuses and the accepted layout evidence reports 195 connectors, 318 direct/shared definitions, and no accepted geometry violations. The deliberately removed visible reclamation connector is an accepted geometry tradeoff with its availability gate retained. | The current working tree contains new focus callbacks and gate changes that lack fresh MCP evidence. The latest accepted MCP pass is from 2026-09-05, not the current dirty revision. The earlier inventory also found 92 of 184 direct focuses using base-only AI weighting. |
| Decisions and missions | Partial | Bounded source inventories, timeout/cooldown handling, category gates, and package decisions exist. Prior audits counted 88 activation blocks, 86 timed-mission timeout rows/effects, and two repeatable cooldowns; another inventory counted 80 accepted source rows by a narrower method. | Counting methods are not yet reconciled into one acceptance matrix. Affordability, category density, timeout consequences, package reachability, and typed AI scenarios remain incomplete. |
| AI, probability, MTTH, random pools | Partial / blocked | The outer 14-region selection pool has synthetic normalisation evidence. AI strategy, focus AI, decisions/missions, event options, and package selection weights exist in source. | The nested 126-package dynamic pool lacks complete scenario evidence. Event options, decisions/missions, focus selection, strategy factors, and named MTTH/AI surfaces lack a complete typed fixture matrix and whole-event balance conclusion. Current DAH AI flag corrections are uncommitted and require same-scenario probability comparison before acceptance. |
| Formables | Partial / blocked | 48 accepted formable families exist in the design inventory; 14 have bounded state-puzzle/runtime contracts. FORM-16 static validator passes. | FORM-06 through FORM-47 are not all proven beyond the admitted bounded families. FORM-42 remains blocked, FORM-48 is unreachable through the current FSM path, FORM-39 retains member/identity gates, and FORM-08 has only two researched states against a three-state threshold. |
| League lifecycle | Partial / blocked | League gameplay source and one associated evolution/super-event path exist. | Lifecycle reachability and probability proof are incomplete. The shared league emblem is absent. Super-event 23 audio and firing remain blocked. |
| Scripted GUI / Statehood Ledger | Needs user review | The event-owned Statehood Ledger has a `chaosx_event_ui_worker` handoff. Static GUI matrix passes five tabs, five recognition frames, three dependency states, four league states, four formable states, cleanup, and four static/animated pairs. Earlier MCP evidence inspected 48 elements and rendered multiple states. | Fresh 2026-09-06 GUI inspect/render calls timed out after 180 seconds. Dynamic tab, click-region, blend-frame, multi-resolution, and live consumer proof remain open. Static matrix results are not visual/runtime proof. |
| Visual assets and flags | Partial / gated review | Current audits found 102 registered tag families and 1,530 technically valid TGA flags, with no incomplete size/ideology families. Report/news art, super-event images, GUI panel, achievement icons, animation sheets, FORM-05/FORM-48 emblems, and state-puzzle assets pass structural/runtime-file inspection. | 228 identical ideology aliases need an ownership/policy decision. Most accepted formable emblem identities and the shared league emblem are absent. State-puzzle unresolved/qualifying variants rely only on colour/opacity and need user review for non-colour recognition. Asset acceptance rows ASSET-005/006/039/044 remain review-gated; ASSET-046 remains blocked. |
| Portraits | Partial / blocked | Current portrait audit found 70 runtime DDS files, 64 GFX pairs, 72 character references across 46 keys plus 18 effect consumers, and no unresolved consumer path. It also found 51 supplied inputs and 38 exact mappings. | Thirteen supplied-input rows remain unresolved, six runtime DDS files are unregistered orphans, and grounded subjects still require attributed source-placeholder/final replacement lifecycle evidence. ASSET-045 remains blocked. |
| Super-events and audio | Partial / blocked | Super-event 23 and 24 text/image/source wiring exists; the alternate `Alte Kameraden` source candidate has an archived 110-second WAV and checksum evidence. | The accepted London Brass Players recording for super-event 23 is blocked for redistribution. The alternate candidate is not approved or wired. There is no accepted runtime audio package or firing proof. Super-event 24 reachability remains dependent on incomplete upstream package/formable paths. |
| Frame animation | Partial / review-gated | Current visual audit reports 16 of 16 animation-sheet ordering checks passed, with static/animated GUI pairs present. | Fresh MCP visual evidence is unavailable; source/frame ordering does not prove in-game animation timing or presentation. |
| Achievements | Partial | Current definitions inventory contains 16 achievements and 48 state icons; the audit found zero missing source files. | Reachability remains dependent on gated packages, league outcomes, and formables. No full scenario/runtime completion proof exists. |
| SCN-008 Sovereign Scatter | Source/static implemented; runtime partial | The dedicated validator passes all 32 cells, eight edge cases, and success-only `.2 -> .80` publication, with no failed report/result dispatch. Catalog and localisation wording are aligned. | Fresh event MCP requests timed out. SCN-008 still inherits the incomplete 126-package probability evidence and 161-package content gap. |
| Documentation and catalog | Aligned to partial boundary | Event details, all five evolution texts, cluster wording, and SCN-008 wording match current localisation. Catalog statuses remain `Needs Testing`, `Partially Available`, and `Needs Testing`. CSV export evidence reports 166 event rows, 20 cluster rows, and 16 scenario rows. The stale super-event visual registry path was corrected in commit `a4659feb7e`. | No 14/20 capacity or playability promotion is justified. A final whole-event completion report cannot be produced while the above blockers remain. |
| Custom 3D units and unit audio/counters | Not applicable to accepted Event 006 scope | No accepted Event 006 custom 3D unit package was found. | If a later package introduces one, the full 3D, sourced-audio, checksum, synchronization, and bespoke vanilla-green counter contract becomes mandatory. |

## Current authority conflict and provisional work

### Event 021 separation conflict

The accepted current authority says Event 021 origin-neutral receipts are internal compatibility receipts only and must not publish Event 006 categories, missions, costs, queues, or history surfaces.

The observed uncommitted current checkout adds `is_independence_wave_event021_package_country`, then allows Event 021 package actors through `is_independence_wave_event6_local_content_active` and `is_independence_wave_event6_player_surface_allowed` in `common/scripted_triggers/006_independence_wave_triggers.txt`.

That widening conflicts with:

- `docs/plans/006_independence_wave_plans/quality/spec_acceptance_checklist.md`.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_player_surface_origin_gate_2026-09-03.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_category_origin_gate_normalization_2026-09-05.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_event021_content_predicate_narrowing_2026-09-01.md`.

The new Event 021 adapter registry files document the compatibility registry but do not supply an accepted basis for widening player-visible Event 006 surfaces. This is therefore a design/authority gap, not accepted implementation evidence.

### Other current working-tree items

- `common/decisions/006_independence_wave_balkan_decisions.txt` contains the first-line marker `# temporary_remove_immediately`. It is a source-hygiene blocker and should not survive a reviewed patch.
- Three DAH AI strategy flags were changed to canonical `independence_wave_dah_*` names in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`. The correction appears semantically narrow, but it is uncommitted and probability-bearing, so it needs the required same-scenario probability comparison before acceptance.
- Current focus-tree callbacks, DAH settlement support, and IW-023 framework-gate changes are provisional until their owning patch handoff and current-revision MCP evidence are available.

No audit finding above authorises reverting other agents' work. The parent must resolve or assign ownership of the conflict against the accepted source-of-truth boundary.

## Accepted-plan disposition

| Plan or tranche | Disposition on 2026-09-06 | Basis |
|---|---|---|
| Core ladder, ordering, rollback, cleanup, success-only publication | Implemented in bounded source/static scope | Current validators and source review; MCP/runtime limits retained |
| Five evolution families | Implemented in source, runtime validation partial | Current event/localisation/log/detail source; partial MCP evidence |
| Accepted focus geometry correction | Implemented | Current source-of-truth explicitly accepts the removed visible connector while preserving availability logic |
| Statehood Ledger event-owned GUI | Implemented in source; needs user review | Worker handoff and prior MCP artifacts; fresh MCP timeout and dynamic-state gaps retained |
| First-footprint package programme | Accepted and queued | 32/29 attested boundary leaves 161 selectable rows unattested |
| IW-095 / DAH package-local work | Implemented locally but centrally unadmitted | Identity, portrait, flag, FORM-24, current AI comparison, and central admission remain open |
| GLC promotion candidate | Accepted and queued | Closest bounded package candidate, but portrait terminology/rights, flag identity, typed probability, current package audit, and parent central promotion are still required |
| ASY and CHU follow-ups | Accepted and queued | Portrait/source-rights closure required |
| NAV, FIJ, DOX, SOK follow-ups | Accepted and queued or blocked by recorded gates | Living-carrier policy, multi-gate closure, or broader package blockers remain |
| FSM / FORM-48 path | Blocked | Identity and route reachability remain incomplete |
| Super-event 23 audio | Blocked | Accepted recording lacks redistribution clearance; alternate candidate remains unapproved |
| Remaining selectable registry rows | Unresolved or accepted and queued by their individual evidence | Registry inclusion alone does not prove acceptance, implementation, or completion |

## HOI4 MCP evidence and limits

### Event root

`chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` and a partial render.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b14d55761b49a5ba6706f5872b30371ddfba9821b3467859da1e0166f22ed50/0cc1b804262785dee2051f4d6fe5a1f584f10cfeabbf9146ab0e0c7c086010cc/event-lint-867e063d60ce.json`
- Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/539a4c376dfd1d7a50e1327f274e7a3ff40d89e4288769512ebacf1f1dea7945/994aa876a26653d627de96dcb05cde57f075e48e2fc7ea7e02095c957a3a6a83/event-overview-867e063d60ce-manifest.json`
- Graph revision: `867e063d60ce069c9ffc04d92b142f4f15a87cfb33206eb447768af957ffa0f0`
- Graph hash: `d3948dd5528285ed23bf34f4925e2e48f9bd2d7d3fc5bbc1c6ed6b46e602f509`
- Completeness: false

### Evolution-family roots

The following roots returned partial inspect evidence at the later graph revision prefix `e5dbb20bfdbf`; four also returned partial render manifests:

- `chaosx.nr6.36`: inspect `event-lint-e5dbb20bfdbf.json`; render `event-overview-e5dbb20bfdbf-manifest.json`.
- `chaosx.nr6.320`: inspect and render partial.
- `chaosx.nr6.330`: inspect and render partial.
- `chaosx.nr6.340`: inspect partial; render failed once with `UNKNOWN: unknown error, realpath 'C:\Users\klimp\AppData\Local\hoi4-agent-tools\state\request-capacity\43f52410ceeba65a\2'`, then timed out after 180 seconds.
- `chaosx.nr6.360`: inspect and render partial.

The revision change from `867e...` to `e5db...` is direct evidence that the checkout/index changed while MCP requests were running.

### Calls without usable evidence

- Batched inspect/render requests for `chaosx.nr6.11`, `chaosx.nr6.18`, `chaosx.nr6.21`, `chaosx.nr6.28`, and the SCN-008 path produced no usable output and were terminated after more than 150 seconds.
- The individual SCN-008 inspect/render request timed out after 180 seconds.
- The retry for `chaosx.nr6.340` render timed out after 180 seconds.
- Current focus inspect/render remained queued for more than 240 seconds and was terminated; no current-revision artifact was produced.
- Fresh Statehood Ledger GUI inspect/render requests reported by the 2026-09-06 visual audit each timed out after 180 seconds.

No valid current `event_compare` was produced. A stable same-revision baseline/current pair did not exist because the graph revision changed during the audit, and the earlier 2026-09-04 compare attempt timed out. Source diffs and partial graphs are not a substitute for semantic comparison evidence.

## Meaningful static validation

The following task-specific checks passed against the observed checkout:

- Allocator boundary and ordering: 149 publishers, 126 automatic/high-chaos selectable entries, 138 SCN-ranked entries, 40 adapters, 32 attestations, 29 groups, 20 static witnesses, exact ladder, World Collapse 10, Event 005 ordering, and retired pre-event crisis.
- Country API: broad 242, resolved 191, Soviet 34, Africa 45, missing 0, duplicate 0, IW-031 pass.
- Flag family completeness: 102 registered tags, 102 complete families, zero incomplete families.
- FORM-16 static contract.
- SCN-008: all 32 cells, eight edge cases, success-only publication, and no failed-result dispatch.
- GUI matrix: five tabs, five recognition frames, three dependency states, four league states, four formable states, cleanup, and four static/animated pairs.
- Achievement file inventory: 16 definitions, 48 icons, zero missing source icons.
- Catalog/localisation alignment for Event 006 details, all five evolutions, the Liberations cluster, and SCN-008.

The validators do not detect the current Event 021 authority conflict, prove dynamic nested probability behaviour, or prove runtime GUI/event/focus consumers.

## Ranked next patch candidates

1. **Resolve the Event 021 authority conflict before merging the current gate widening.** This has the highest safe impact because it protects the accepted Event 005/Event 006/no-pre-event boundary. The parent should either reject the widening and retain internal-only receipts or record a new explicit acceptance basis before any implementation is treated as valid.
2. **Remove the temporary Balkan decision marker within its owning patch.** This is mechanically safe after ownership is confirmed and avoids committing an explicit temporary annotation.
3. **Complete typed probability evidence for the DAH flag correction and current weighted surfaces.** Run baseline/current comparison on the same stable revision and scenarios before accepting the three AI flag substitutions.
4. **Promote GLC only after its remaining evidence closes.** Complete portrait terminology/rights, flag identity, typed probability scenarios, a fresh package audit, and parent-owned central attestation/admission. GLC is the nearest credible package-count gain without broad design expansion.
5. **Rerun Event 006 event/focus/GUI MCP evidence on a stable checkout.** Inspect and render every named chain; compare against a frozen accepted baseline; capture Statehood Ledger states, resolutions, hierarchy, and click regions.
6. **Close package evidence systematically.** Work one accepted first-footprint package at a time; ASY and CHU follow GLC, while NAV, FIJ, DOX, SOK, FSM, and DAH retain their recorded gates. Do not bulk-attest registry rows.
7. **Resolve formable, league-emblem, portrait, and super-event audio blockers.** These are completion-critical but require ownership, source/licence evidence, user review, or upstream route reachability rather than a safe audit-only patch.

## Explicit omissions and blockers

- No live HOI4 run or user validation was performed; live consumer validation belongs to the user.
- No complete event, focus, GUI, map, or probability MCP proof exists for the current dirty revision.
- No stable event comparison exists for the current revision.
- The probability matrix remains incomplete unless supplemented by the separately running `chaosx_ai_probability_auditor` handoff; this audit does not infer its result.
- No map rewrite or declarative map proof was performed. IW-003 still lacks a lawful Cornwall state binding; state 123 is too broad. IW-108 Buganda still conflicts with Event 012 ownership.
- The 161 unattested package rows were not inspected as if registry rows were complete country packages.
- Overlay completeness was not used to reduce selectable-package debt.
- No source-placeholder portrait was promoted to final, no asset provenance gap was waived, and no unapproved image/audio substitute was accepted.
- No 3D model package was required by the accepted Event 006 scope.
- No completion report, catalog playability promotion, or overall Event 006 completion claim is justified.

## Handoff conclusion

The current checkout has a substantial, statically validated Event 006 framework and 32 content-attested packages across 29 groups, but the accepted event remains incomplete because 161 selectable rows are unattested, several runtime/reachability/probability surfaces lack complete MCP evidence, and critical formable, league, portrait, emblem, audio, and route gates remain open.

Before expanding package count, the parent should resolve the current Event 021 player-surface authority conflict and stabilize the checkout for the required event/focus/GUI/probability comparisons.
