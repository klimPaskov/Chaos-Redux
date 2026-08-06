# Event 020 Black Plague completion audit handoff

Date: 2026-08-06

Mode: read-only gameplay audit; this handoff is the only file written by the auditor.

## Verdict

Event 020 is **partial and blocked**, not complete.

The current source implements a substantial playable package, including the persistent disease system, the shared disease-response category, five evolutions, exactly `RTA` and `RTX`, the 52-focus RTA tree, the 71-focus RTX tree, the four-intensity `SCN-012` bootstrap, earned Evolution V/world-end logic, aftermath actions, report chains, super-events, achievements, and one shared oversized rat entity for all six rat subunits.

A completion claim is blocked by missing runtime art, incomplete custom-unit audio and counter acceptance, missing model and portrait production evidence, partial Event MCP lifecycle evidence, unresolved scenario rollback, stale source-of-truth documentation, open release/live validation, and accepted presentation or aftermath work that remains queued or simplified.

## Controlling corrections

The following later corrections are correctly reflected in current gameplay source and control this audit:

- `RTA` is the sole reusable Rat Nation carrier and `RTX` is the separate Rat King; broods beyond those two actors are internal state markers rather than additional tags.
- `SCN-012` scales plague coverage, RTA brood basins, RTX royal territory, rat armies, and Chaos through low, medium, high, and maximum intensity; it does not scale country count.
- The scenario bootstrap activates Evolutions I through IV only and explicitly leaves Evolution V and `world_end` to the earned terminal route.
- Human containment remains inside `chaosx_disease_containment_category`; Event 020 does not introduce a separate Black Plague disease category.
- One shared oversized quadruped rat model is the accepted consumer for `rat_swarm`, `rat_brutes`, `rat_burrowers`, `rat_carrion_guard`, `rat_dock_stowaways`, and `rat_tunnelers` across both rat tags.

The rat-owned `black_plague_rat_brood_category` and `black_plague_rat_king_court_category` are internal country gameplay surfaces, not duplicate human disease-response categories, so their presence does not violate the shared-category correction.

## Completion status by surface

| Surface | Status | Evidence and disposition |
| --- | --- | --- |
| Event registration, opening, cluster, log, details, and catalog | Finished statically; runtime proof partial | `events/020_black_death.txt` contains the `chaosx.nr20.1` root and a broad report chain through `.95`; the workbook exports contain Event 20, Diseases cluster `8`, and `SCN-012`. Event MCP could render the current graph but did not complete workspace-wide lifecycle/helper projections. |
| Core state disease, population loss, spread, response capacity, Deaths, and Chaos integration | Partial | The scripted effects, triggers, modifiers, decisions, and state-owned scheduler are present. The MCP state-flow report for `black_plague_system_active` is partial, and the required focused live lifecycle matrix remains absent. |
| Shared disease category, response decisions, missions, and Black Plague mapmode | Partial and currently runtime-blocked | Event 020 extends `chaosx_disease_containment_category`, and its dedicated response actions and mapmode hooks are present. The referenced `gfx/interface/ideas/020_black_death/idea_black_death.dds` is deleted in the current worktree while `interface/chaosx_ideas.gfx` and three dynamic modifiers still reference `GFX_idea_black_death`. |
| Event-owned scripted GUI | Not applicable | Event 020 uses the pre-existing shared disease board and shared framework; it does not introduce a dedicated event-owned scripted GUI, so a `chaosx_event_ui_worker` handoff is not required. |
| Shared disease-board visual evidence | Partial | The 2026-08-05 header inspection/render covers multiple states at 1920x1080 and 2560x1440. The full popup inspection/render stopped at `SCAN_BYTE_LIMIT`, so there is no complete hierarchy/click-region/resolution artifact for the whole shared board. |
| Evolution I-V sequencing and earned terminal route | Partial | All five activation surfaces and terminal takeover logic are present. `black_plague_evolution_advanced_this_check` now enforces at most one evolution per due check. Target/scope/timing and earned Evolution V execution still lack a clean full-chain MCP lifecycle pass and focused live sequence evidence. |
| RTA and RTX country packages | Partial | Exactly the two accepted tags are used, internal broods remain RTA state, and the King remains RTX. Country identity, decisions, focus trees, templates, and terminal/aftermath hooks are present, but current flag binaries and several localisations remain modified in the worktree and are not a final reviewed asset state. |
| RTA/RTX focus trees | Partial with strong structural evidence | The current files contain 52 RTA focuses and 71 RTX focuses. The 2026-08-05 MCP focus renders report zero crossings, zero node intersections, and zero long connectors; current source still includes uncommitted RTA prerequisite edits, and the current completion audit has not established final AI probability coverage for every route. |
| `SCN-012` four-intensity scenario | Partial and design-blocked | Source correctly applies the four intensity profiles, uses only RTA/RTX, reconciles existing actors, forces I-IV, and excludes V/world-end. The accepted implementation still lacks a journaled inverse transaction after mutations if a late postcondition fails; retry cleanup is not equivalent to rollback. |
| Scenario validation matrix | Missing | No durable results cover all four fresh-launch intensities, launch during an active crisis, existing RTA/RTX preservation, internal-brood top-up, no-new-anchor repeat reconciliation, save/reload, grace coexistence, post-grace RTA absorption into RTX, mapmode rebuild, or failed-postcondition retry. |
| Rat defeat and aftermath | Partial and simplified | Scoped participant hooks, metrics, `.71`, eligible `.72`, super-event 087, `.73-.75`, Crown restoration, and five shared-category aftermath projects exist. The accepted addendum still records `.73` falling back to the first eligible human response host rather than the saved contributor, compact broader aftermath depth, and reused reconstruction presentation. |
| Super-events and audio | Partial | Art/text/sound wiring exists for coronation, world end, and defeat aftermath, with sound wrapper IDs 101, 102, and 103; the third file is `super_event_087_rat_king_defeat_aftermath.wav`. Release attribution/rights disposition and live playback remain open. |
| Shared rat 3D entity | Runtime installed but package blocked | `black_plague_rat_entity`, the mesh, five actions, textures, scale `1.35`, and shared unit/template consumers exist. The production handoff records 101 loose boundary edges as a QA risk, and the claimed provider/Blender/reimport evidence directory is absent. |
| Custom-unit audio | Blocked | The 3D handoff leaves four CC BY 4.0 vocal candidates at `needs_user_review`, has no accepted impact/contact source, and leaves sound definitions and runtime wiring open. The required source pages, licenses, original/derived checksums, role coverage, and animation synchronization evidence are not currently retained in the repository. |
| Large and map counters | Blocked for acceptance | Bespoke counter DDS files are installed and hash-recorded in the handoff, but the package is explicitly review-gated. The claimed exact vanilla definition/DDS inspection, skill-local reference-family inspection, sampled vanilla-green evidence, original art, round-trip, and contact-sheet evidence is unavailable because the referenced production folder is absent. |
| Portraits | Runtime DDS present; production handoff blocked | Five fictional rat portrait families and the Rat King animation sheet are wired under `gfx/leaders/020_black_plague/`. No `chaosx_portrait_creator` handoff was found, and all six tracked permanent sources under `docs/assets/portraits/020_black_plague/` are deleted in the current worktree. |
| Other 2D visual provenance | Blocked | All 55 tracked records under `docs/assets/020_black_plague/` and all nine tracked `gfx/source/event20/` records are deleted in the current worktree, including manifests, prompts, source frames, processed previews, animation contact sheets, and DDS archives. Runtime DDS survival does not replace durable production evidence. |
| Achievements | Partial | Fourteen public contracts and icon triplets are documented and wired, and the scenario-launch flag disqualifies ordinary shortcuts. No final focused live unlock/non-unlock matrix was supplied. |
| Documentation and catalog | Partial and stale | The CSV exports contain the corrected Event 20, Diseases cluster, and SCN-012 wording. Multiple active spec/review/overview surfaces still say no bespoke 3D model is required or planned, reject model production, retain the accepted infantry entity as the consumer, or record 51 rather than 52 RTA focuses. |

## MCP event evidence and limits

The required read-only Event MCP route was used on the current working revision.

- Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
- Revision: `c5c2ec44234bf0204343bfb037b9c21d042007efccafb416e12764447dc735ca`.
- Graph hash: `1bf1ef10b558fb1edc5b936589bd3d940ca3e8bd2dacef7757e7af1cd1727655`.
- The initial broad roots/refresh call timed out after 180 seconds.
- A narrow scan of `events/020_black_death.txt` returned `EVENT_INSPECTED_PARTIAL`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73a88264bdbcc050672eff7c8495945f446a69edef3b1be01c430d53c51e4049/303ecbb1ec22b7dead51351d3f5f5acc0a4fdc969ae7f860be93720bdded063f/event-scan-c5c2ec44234b.json`.
- The bidirectional trace from `chaosx.nr20.1`, depth 10, returned `EVENT_INSPECTED_PARTIAL`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/735187053e5ac9507e188b264fd3a7818ccc40ebf8683b3918ef1a54b85825fb/b1e10ad67ee172c34c7474c3f1319a88b590480277279b855c45c277155df4e7/event-trace-c5c2ec44234b.json`.
- The overview render returned `EVENT_RENDERED_PARTIAL` with 88 selected nodes and 40,814 omitted workspace nodes; authoritative JSON SHA-256 `27af4b07d31b76b3c259e235ad22fb955c1fe5422cfc35d3d6fdee4f4c50eb55`, SVG SHA-256 `d5cd90c12367d87b176689b0c38d7cf5629713be7f37203a164a63a42b5bc97b`, PNG SHA-256 `4013c15076a3115ec32629843d18b36742594ecd8cca03a3b188cf4cd22b77ff`, and layout SHA-256 `f4032e89ef1295beef34bfbaedf61931f4724aaf223ee700ed58f1c29d9c1b8e`.
- State-flow inspection for global flag `black_plague_system_active` returned `EVENT_INSPECTED_PARTIAL`; authoritative artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa14234d112eb685b6782035dbc03ce7951e5102c946aa2b78913e2419eadc73/93dc4e116cf7c116019176b0c95a3edc981c0d8a7cd063a40a3d6adbb090a745/event-state_flow-c5c2ec44234b.json`.
- Each successful route reports zero blocking diagnostics but `validation.passed = false` because the large workspace deferred workspace-wide helper projections and lifecycle passes.

This evidence proves that the current source can be parsed into a large linked event graph and rendered, but it is not equivalent to a clean event-chain lifecycle, scope, target, timing, terminal, or unresolved-reference pass.

`hoi4.event_compare` was not invoked because this audit received no proposed event source or event-graph baseline, and `events/020_black_death.txt` is unchanged relative to `HEAD`. The recent model commit did not change the event graph. The comparison requirement should be applied when a gameplay revision is proposed against this recorded current revision.

## Accepted-plan disposition

| Accepted item | Disposition |
| --- | --- |
| Exactly `RTA` plus `RTX` | Implemented statically and retained. |
| Internal RTA broods instead of additional tags | Implemented statically and retained. |
| Shared disease category with Black Plague decisions | Implemented statically and retained. |
| Four scenario intensities | Implemented statically; full launch/repeat validation missing. |
| SCN-012 must not grant Evolution V or world end | Implemented statically; earned terminal route remains separate. |
| One shared oversized rat model for all six subunits | Runtime entity and actions installed; package completion blocked by geometry QA, missing evidence, audio, counter review, and live consumers. |
| Consequence and aftermath addendum | Core mechanics promoted; `.73` audience ownership, broader narrative/presentation depth, release rights, and live proof remain queued or simplified. |
| State-clipped black fog enhancement | Unresolved optional design gap; no verified safe clipping mechanism or reproducible prototype/blocker artifact was found. The mandatory black mapmode base exists. |
| Historical no-model boundary | Superseded by the accepted 2026-08-05 shared-model brief and runtime commit, but not reconciled across active docs. |

## Missing, simplified, blocked, or stale requirements

### Runtime and gameplay blockers

1. `gfx/interface/ideas/020_black_death/idea_black_death.dds` is deleted while still referenced by `GFX_idea_black_death`; this is a concrete missing runtime asset, not a provenance-only issue.
2. `SCN-012` has retry cleanup but no complete inverse rollback for disease ledger changes, state transfers, country activation, evolution state, and Chaos already applied before a late failure.
3. `.73` still uses the documented first-eligible-human fallback rather than the accepted saved contributor/actor contract.
4. Focus, mission, mapmode, scenario, achievement, super-event playback, model, counter, and aftermath live validation remains absent; this repository workflow does not launch Hearts of Iron IV, so those results remain parent/user-owned evidence.

### Custom 3D, sound, and counter blockers

1. `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-05_event020_rat_shared_3d_model_handoff.md` claims the provider outputs, requests/responses, hashes, Blender checkpoints, previews, DDS packs, exports, and reimport proof are retained under `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/`, but that directory does not exist and no files at that path are tracked by Git.
2. The model handoff records 101 loose boundary edges as a QA risk without naming them as intentional open surfaces or recording a repaired/rejected disposition.
3. The unit sound package is incomplete: there is no accepted impact/contact source, no final source/license/checksum/synchronization package, and no parent-owned sound-definition/runtime wiring.
4. The counter package is installed but explicitly `needs_user_review`; the absent production evidence prevents independent verification of the exact installed-vanilla family, green sampling, original art, DDS round-trip, and comparison contact sheet.

### Portrait and visual-asset blockers

1. No Event 020 `chaosx_portrait_creator` handoff was found for the fictional brood or Rat King portrait families.
2. The six tracked source PNGs under `docs/assets/portraits/020_black_plague/` are deleted; portrait source archives are permanent evidence and cannot be treated as disposable temporary workspace.
3. All 55 tracked Event 020 asset records under `docs/assets/020_black_plague/` and all nine tracked records under `gfx/source/event20/` are deleted, contradicting handoffs that say ImageGen masters, prompts, manifests, contact sheets, and processed previews are retained.
4. Current RTA/RTX flag binaries are modified while their durable review/provenance package is absent from the current asset tree.
5. Broader dedicated crisis, Doctor Wu, route, reconstruction, and aftermath presentation remains queued where the accepted addendum still identifies reused art or compact presentation.

### Stale documentation

The following current-facing files conflict with the accepted and installed shared rat model:

- `docs/specs/020_black_plague_specs/README.md`.
- `docs/specs/020_black_plague_specs/review/source_of_truth_and_plan_disposition.md`.
- `docs/specs/020_black_plague_specs/review/limitations_and_blockers.md`.
- `docs/specs/020_black_plague_specs/matrices/asset_inventory.md`.
- `docs/specs/020_black_plague_specs/manifest.md`.
- `docs/events/020_black_plague/rat_route_depth.md`.
- `docs/events/020_black_plague/rat_king_depth.md`.
- `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`.
- `docs/plans/020_black_plague_plans/2026-08-05_focus_gui_mcp_layout_audit.md`.

Several of those same files record 51 RTA focuses, while the current tree and 2026-08-05 MCP audit record 52. Historical handoffs may preserve old facts, but active source-of-truth and current overview surfaces require explicit supersession or reconciliation.

## Probability and AI audit

The required weighted-surface pass was routed to `chaosx_ai_probability_auditor` for natural origin weighting, evolution timing, direct random/random-list blocks, event options, decision/mission AI, RTA/RTX focus AI, strategy factors, and declared scenario pools. The result is **partial and unresolved**, so no exact probability, exact timing, or balance claim is supported.

| Weighted surface | MCP result | Evidence and limit |
| --- | --- | --- |
| Event option `ai_chance` discovery | Partial | Inspecting `events/020_black_death.txt` found 91 candidates but reported `poolComplete = false`, four required inputs, and one unresolved input. Artifact SHA-256 `7134aa439710394f85546d9085d05a6e89dac8721635013cde5680a4e4b533bd`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7134aa439710394f85546d9085d05a6e89dac8721635013cde5680a4e4b533bd/d04ee0c28b12fb2b2e9d43cfe5d07cdc574da30b5f9f53fe0ddfeb50056d36fe/probability-inspect-7923851ea457.json`. |
| `.46` coherence-crisis option probe | Partial | The bounded candidate pool `chaosx.nr20.46.a/.b` was evaluated under four named low/medium/high/maximum SCN-012 scenarios with empty declared state. Analysis `probability-2106d3253ed7a74c2562f649` returned `PROBABILITY_ANALYZED_PARTIAL`, two candidates, three unresolved inputs, and no diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8019ddf98163d3f43dcaa68f3f997c22af8dae726b05e0e5b4a1c1888043d1f/d5f43728d516c98e69e67c85f03e5def3bb25d88054f28b987624dc47184cf76/probability-2106d3253ed7a74c2562f649.json`; scenario hash `61483c05ba211a30970835d22456aaeda65aaeadb005e3ad0e6857df22e250e9`. Source review finds base weights 75/25 with conditional doubling, but unresolved inputs prevent an exact conditional probability claim. |
| RTA/RTX rat decision `ai_will_do` | Partial | Inspecting the 39-ID local decision pool in `common/decisions/020_black_plague_rat_decisions.txt` returned only two candidates, `poolComplete = false`, one required input, and 37 unresolved candidates. Artifact SHA-256 `7aa0ca982fd569e2c7143c3251a0627d8105fcab03a054ad3e60398779178655`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7aa0ca982fd569e2c7143c3251a0627d8105fcab03a054ad3e60398779178655/428244a7b67143f52809bd39f77f2fcfa8c506dc60fc374348d6c9423a221572/probability-inspect-ef74839ba803.json`. |
| Human response, shared response, and weaponization decision AI | Blocked | The adapter returned `PROBABILITY_SURFACE_EMPTY` for the exact inspected decision sources. Source review is not equivalent MCP probability evidence. |
| Evolution MTTH | Blocked | `event_mean_time_to_happen` returned `PROBABILITY_SURFACE_EMPTY` for `common/mtth/020_black_plague_rat_mtth.txt`, the event source, and related effects. Source review identifies I-IV base constants and conditional multipliers, but exact effective timing is not established. |
| Natural-origin weighted ticket pool | Missing MCP evaluation | The pool is implemented inside scripted effects rather than a directly completed adapter surface. Its documented population, crowding, occupation, resistance, troop, refugee, war, port, rail, and protection factors were not converted into exact scenario evidence. |
| Direct random and `random_list` | Blocked/empty | Inspecting `events/020_black_death.txt` returned `PROBABILITY_SURFACE_EMPTY`. |
| National-focus AI | Tool error | Inspecting `common/national_focus/020_black_plague_rat_focus_tree.txt` returned `INTERNAL_ERROR`; the earlier bounded focus note is not whole-tree weighted evidence and does not cover RTX independently in this pass. |
| AI strategy factors | Blocked/empty | Inspecting `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` returned `PROBABILITY_SURFACE_EMPTY`. |

No probability-bearing source changed and no proposed balance revision was supplied, so `hoi4.probability_compare` was not run. A sweep was not completed because the parent auditor stopped further long-running MCP calls after the partial/error batch; the exact unresolved adapters above remain completion blockers rather than being replaced by source-only estimates.

## Meaningful validation present and missing

Present evidence:

- Current Event MCP scan, root trace, overview render, and `black_plague_system_active` state-flow artifacts, all with explicit partial-validation limits.
- 2026-08-05 RTA/RTX focus inspection/render/raster evidence showing 52/71 nodes and clean authored geometry.
- 2026-08-05 shared disease-board header states at two resolutions, with an explicit full-popup `SCAN_BYTE_LIMIT` blocker.
- Static source confirmation of the shared disease category, exactly two tags, four intensity profiles, I-IV-only scenario launch, one shared model consumer, and separate earned Evolution V/world-end logic.
- Current catalog exports for Event 20, Diseases cluster `8`, and `SCN-012` use the corrected player-facing wording.

Missing or insufficient evidence:

- A clean Event MCP lifecycle/helper pass for the bounded Event 020 graph, including scope, targets, timing, terminals, and unresolved references.
- A comparable before/after event revision when the next gameplay patch is proposed.
- Full shared-board hierarchy/click-region/resolution rendering beyond the header.
- Final probability evidence for all Event 020 weighted surfaces; the completed pass found incomplete pools, unresolved inputs, empty adapters, and one focus-adapter internal error.
- Final 3D production, counter, portrait, flag, report/news, and animation source/provenance packages in their claimed durable locations.
- User-owned focused runtime results for natural launch, all scenario intensities, repeat/retry/save behavior, evolution sequencing, missions, mapmode, focus AI, achievements, super-event playback, model actions, counters, and aftermath.

## Recommended next actions

1. Restore the deleted Event 020 asset evidence and permanent portrait source archive, and place the model provider/Blender/reimport, audio, and counter evidence in the durable paths claimed by their handoffs.
2. Restore or replace `idea_black_death.dds` before any runtime-ready claim.
3. Resolve the model's 101 loose boundary edges with named intentional-open-surface evidence or a repaired export/reimport pass.
4. Complete the Internet-sourced unit audio package, including an accepted impact/contact source, durable source pages and licenses, original/derived checksums, role coverage, action synchronization points, and parent-owned sound definitions/runtime wiring.
5. Complete counter visual review against exact installed vanilla definitions/DDS files and the skill-local reference family, preserve vanilla-green sampling and original-art evidence, and record DDS round-trip/contact-sheet comparison plus runtime acceptance.
6. Route all five fictional portrait families through `chaosx_portrait_creator`, restore their permanent source archive, and produce the required processing/wiring manifest and handoff evidence.
7. Decide and document an atomic inverse-rollback design for `SCN-012`, or explicitly accept the current retry-only simplification; it cannot remain hidden beneath a completion claim.
8. Resolve `.73` actor ownership and the queued broader aftermath/presentation work, or explicitly reject those accepted-plan items with reasons.
9. Reconcile active documentation with the shared 3D model, the current 52/71 focus counts, current asset state, and explicit incomplete validation status; leave historical snapshots marked as such.
10. Rerun the Event MCP route after narrowing or raising the helper/lifecycle scan budget, rerun GUI evidence for the full shared board if the scanner permits it, and apply `hoi4.event_compare` to the next proposed gameplay revision against the current revision recorded above.
11. Rerun probability discovery/evaluation with explicit scenario inputs for natural origin, evolution MTTH, every decision/mission family, both focus trees, strategy factors, and any random pools; resolve the empty/internal-error adapters before making balance claims, then use identical scenarios with `hoi4.probability_compare` for any subsequent weight patch.
12. Run final focus, decision/mission, localisation, country-package, probability, and documentation audits on one stable final worktree after the current RTA focus, flag, and localisation changes are settled.

## Auditor boundaries

No gameplay, localisation, GUI, GFX, model, sound, spreadsheet, or asset file was edited by this audit.

The audit applied the `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, and `chaos-redux-3d-model-pipeline` workflows, together with the required offline wiki and installed vanilla documentation references.

## Parent remediation after this snapshot

The missing `gfx/interface/ideas/020_black_death/idea_black_death.dds` was restored from the repository and the deleted Event 020 source/provenance records under `docs/assets/020_black_plague/`, `docs/assets/portraits/020_black_plague/`, and `gfx/source/event20/` were restored. Active documentation was reconciled to the shared model package and current 52/71 focus counts. The remaining model evidence, sound/counter acceptance, MCP adapter limits, retry-only scenario boundary, and live-validation items in this handoff remain open evidence limits rather than hidden runtime references.
