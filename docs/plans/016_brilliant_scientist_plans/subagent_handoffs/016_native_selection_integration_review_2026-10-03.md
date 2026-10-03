# Event 016 native Cloning and Rocketry selection integration review

Date: 2026-10-03.

Disposition: source-only integration review delivered for parent review; no gameplay source was changed by this audit.

The bounded source trace found no remaining concrete integration defect in the six native selection and withdrawal controls after the reported worker and parent corrections.

The full Event 016 goal remains incomplete because native research start/cancel synchronization and callback-generation isolation remain unresolved, and the separate AI probability audit currently has no MCP result or balance certification.

## Scope and ownership

I read `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`, then inspected only the named native-control files and their direct Event 016 category, project-output, CXT, localisation, and preservation-record dependencies.

The audit did not edit gameplay files, alter documentation outside this handoff, make a commit, launch the game, request MCP evidence, or perform model work.

Parent owns final source integration, MCP retries, balance review, and commit; the separate `chaosx_ai_probability_auditor` owns scoring evidence.

## Severity-ordered findings

1. **High, unresolved lifecycle contract:** `common/scripted_effects/016_mengele_native_prototype_effects.txt` explicitly treats selection as provider authorization rather than proof of native start or payment, and records that native start/cancel synchronization, automatic matching-cancellation cleanup, and immutable release/reselection callback generations remain unresolved. The synchronous exact-source output witness rejects opposite-source output, but it cannot authenticate a later callback generation or prove that native payment occurred. Keep this unresolved; explicit withdrawal does not close it.
2. **High, balance evidence pending outside this audit:** the selection decisions have nonzero `ai_will_do` weights, but the separate AI handoff returned no MCP results and no balance certification. The parent has requested one narrower retry; no AI score, ranking, scenario result, or balance claim is established here.
3. **Evidence limit, not a source defect:** this was an explicitly source-only pass with no new MCP requests. The controls are ordinary native decision rows and reuse existing categories and icons; no dedicated scripted GUI layout was introduced. Source review does not prove rendered row appearance, engine refresh, special-project callback timing, or live click behavior.

No other concrete source-level blocker was found in the bounded integration surface.

## Decision categories, visibility, and action budget

The six decision IDs are `mengele_event016_native_select_cloning`, `mengele_event016_native_select_flying_bomb`, `mengele_event016_native_select_jet_engine`, `mengele_event016_native_release_cloning`, `mengele_event016_native_release_flying_bomb`, and `mengele_event016_native_release_jet_engine` in `common/decisions/016_mengele_native_prototype_selection_decisions.txt`.

They attach to the existing `mengele_biological_programs_category` and `mengele_conventional_programs_category`; those categories remain visible only while the Mengele project-stage provider is valid.

The native selection rows require the relevant Theory receipt, the matching empty paid-family receipt, an incomplete private Prototype, and the Gotterdammerung DLC; exact native completion is an alternate eligible state for adoption.

Rocketry can show both unselected source choices together, then the opposite choice becomes hidden after one source is selected; if the selected source is complete, its adoption row and its withdrawal row may both appear.

Cloning normally contributes one selection row and can show both its completed-source adoption row and withdrawal row while a selected source awaits settlement.

Each category describes five program families; counting four other families with one current stage action each, the new controls bring the source-level maximum to six rows per category. The no-DLC paid Prototype row is hidden when Gotterdammerung is present, and the old Rocketry row also hides after either native Rocketry project is complete, so it does not add a duplicate seventh row. This is a source-gate count, not a rendered MCP confirmation.

The selectors and receipt arrays are internal state rather than player-facing value dumps. The visible choices identify the project being committed, completed-source adoption, or withdrawal; there are no unexplained numeric meters or extra tabs.

Release rows remain visible while the selected native project is in progress but are unavailable until that exact project stops and the paid family receipt is empty. The shared decision helper reports the blocked reason. Selection rows can likewise remain visible before source-specific research eligibility is met, while their custom requirement tooltip describes the missing technology condition.

No mission or timed objective was added or changed, so mission owner, region, duration, success, failure, and duplicate-risk checks are not applicable to this tranche.

## Costs, requirements, AI, and localisation

All six decision rows use zero decision cost and call no provider debit, reserve, or timer. The native special-project definitions retain their existing resource costs, research progress, durations, and project outputs; this audit found no fifth hidden decision cost and no spendable cost string that needs a texticon.

The selection and release `available` blocks use custom trigger tooltips, and the completion effects repeat the matching core eligibility or release gate before changing selection state. The three release helpers require the matching empty paid-family receipt and reject withdrawal while the exact selected native project is being researched.

Selection decisions carry AI weights and release decisions use zero AI weight. Route validity is source-gated by Theory completion, provider validity, matching receipt state, exact source completion or technology eligibility, and Rocketry mutual exclusion; score quality remains unresolved pending the separate auditor retry.

The six decision title and description keys, six requirement-tooltip keys, four result-feedback keys, and the DLC-specific Jet Engine requirement text are present in `localisation/english/016_mengele_native_prototype_selection_l_english.yml` and `common/scripted_localisation/016_mengele_native_selection_text.txt`.

Both existing decision icons resolve in `interface/016_brilliant_scientist_project_icons.gfx`, and both texture files exist. The existing category definitions, category localisations, category sprites, and category art remain wired; this tranche creates no category or icon asset.

No localisation or texticon gap was identified in the inspected controls.

## Completion history, cleanup, and exploit risk

Automatic post-Theory adoption now calls `brilliant_scientist_mengele_can_auto_adopt_exact_completed_native_prototype` before the explicit adoption helper when no source is selected. The exact selected-source path calls adoption directly, allowing a player choice to resolve retired or ambiguous Rocketry history.

The automatic path rejects retired sources and only accepts one unambiguous completed Rocketry source; when both Flying Bomb and Jet Engine are complete without a selection, it leaves both unadopted for an explicit choice.

The shared `brilliant_scientist_mengele_sync_native_project_prototypes` and generic `brilliant_scientist_mengele_record_native_project_prototype` paths directly exclude Cloning and Rocketry, and the reused-native completion scan handles the other families while Rocketry dispatches through exact project wrappers. This blocks aggregate Rocketry completion from granting either source through the shared sync entry.

The three exact project outputs call `brilliant_scientist_mengele_native_output_cloning`, `brilliant_scientist_mengele_native_output_rocketry_flying_bomb`, and `brilliant_scientist_mengele_native_output_rocketry_air_jet_engine`. The Cloning bridge accepts matching fresh provenance as well as a visible completed project, preserving synchronous output settlement when the completion bit is not yet visible.

The Cloning project still calls `cbrn_complete_cloning_project` once. The operational bridge invokes `germany_mengele_complete_cloning_project` behind the existing `germany_mengele_cloning_project_completed` latch, so the legacy payload is idempotent across native and adoption paths.

The output/adoption helpers preserve their dedicated result marker while clearing temporary selectors, and the enclosing Theory transaction restores its saved family, stage, index, and output selectors after the exact-source driver returns.

Provider cleanup calls `brilliant_scientist_mengele_cleanup_native_prototype_selections`, retires and clears selected flags, preserves observed-output flags and source/mode provenance, and now propagates a released selection into the existing `mengele_event016_provider_cleanup_applied` result.

Selection, adoption, release, and cleanup do not grant repeatable native project rewards or refund project costs. Private Prototype completion and exact family receipts prevent selection cycling from repeating the stage output; no free unit loop or repeated completion path was found in the inspected source.

## CXT fixture integration

The player-triggered `chaosx_cxt_event016_enable_mengele_provider_fixture` is guarded by `tag = CXT`, `chaosx_test_country_initialized`, and a not-yet-ready fixture flag. After the existing private receipt initializer it calls `brilliant_scientist_mengele_initialize_native_prototype_provenance`, which appends only empty `none` entries to the source and mode arrays up to the existing family count, then reconciles availability.

That inspected setup path does not set native selected, retired, observed, source-history, mode-history, or project-completion state and does not grant a completed-project package. The parent reports that no carrier or on-action was added for this fixture.

The existing player-triggered `chaosx_cxt_event016_probe_native_inventory` calls `chaosx_cxt_event016_probe_native_ownership` only as an observation snapshot. Both probe layers reject execution unless the country is CXT and initialized; the ownership helper copies selected, observed, retired, and existing source/mode values into CXT-only observation state without extending provider receipts or creating stages, selections, or grants.

The CXT fixture initializes empty provenance slots, while its inventory probe observes completed native objects. That permits source adoption and ambiguity checks in the fixture but does not demonstrate a fresh native research clock, native payment, callback ordering, or runtime persistence.

## Source evidence and artifacts

- Native decisions and decision requirements: `common/decisions/016_mengele_native_prototype_selection_decisions.txt`; presentation gates: `common/scripted_triggers/016_mengele_native_selection_decision_triggers.txt`.
- Decision feedback and CXT observation: `common/scripted_effects/016_mengele_native_selection_decision_effects.txt` and `common/scripted_effects/016_mengele_native_ownership_cxt_effects.txt`.
- Exact-source core and codes: `common/scripted_effects/016_mengele_native_prototype_effects.txt`, `common/scripted_triggers/016_mengele_native_prototype_triggers.txt`, and `common/script_constants/016_mengele_native_prototype_constants.txt`.
- Parent stage and bridge integration: `common/scripted_effects/016_mengele_project_stage_effects.txt`, `common/scripted_effects/016_mengele_project_bridge_effects.txt`, and their matching Event 016 stage/bridge trigger files.
- Native project outputs: `common/special_projects/projects/016_brilliant_scientist_projects.txt`, `common/special_projects/projects/rocket_projects.txt`, and `common/special_projects/projects/air_projects.txt`.
- CXT setup and inventory probe: `common/scripted_effects/016_alien_infantry_cxt_test_effects.txt`.
- Existing category and sprite wiring: `common/decisions/categories/germany_mengele_categories.txt`, `localisation/english/016_mengele_provider_program_categories_l_english.yml`, `interface/016_brilliant_scientist_project_icons.gfx`, `interface/016_brilliant_scientist_directorate.gfx`, and `interface/016_brilliant_scientist_kruger_state_decisions.gfx`.
- No-DLC paid Prototype route locks: `common/scripted_triggers/016_mengele_cloning_stage_decision_triggers.txt` and `common/scripted_triggers/016_mengele_remaining_conventional_prototype_decision_triggers.txt`.
- Whole-block preservation evidence: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_native_prototype_project_preservation_2026-10-03.json` records `removedSingleOwnedHookEqualsBaseline = true` for all three changed native project files.
- Ownership and lifecycle limits: `docs/events/016_brilliant_scientist/systems/native_prototype_ownership.md`.

## Validation limits and parent follow-up

Meaningful source review covered exact decision visibility versus availability, atomic selection and release predicates, source-specific output dispatch, after-Theory adoption, fallback route locks, CXT fixture/probe guards, Cloning payout idempotence, result restoration, and the three-file project-payload preservation record.

No game, MCP, probability scenario, or live decision-row render was run in this bounded review. No tests were requested or run, and this report is not gameplay or balance certification.

Parent follow-up is to retain the lifecycle items above as unresolved, attach the separate probability auditor's narrower retry result when available, and keep runtime/MCP evidence limits visible in the final Event 016 review.

## Files and identifiers changed by this audit

Only this report was created: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_native_selection_integration_review_2026-10-03.md`.

This audit changed no decision, mission, scripted GUI, scripted helper, localisation, asset, or gameplay identifier; the six decision IDs listed above are audited current-source IDs.

No new plan handoff was written.
