# Event 016 CXT native inventory fixture handoff

Status: partial bounded implementation. The parent retains Event 016 integration, MCP scenario work, audits, and final review. No gameplay completion or live behavior is claimed.

## Authority and disposition

The parent assigned the CXT fixture clause in `016_final_mengele_portfolio_closure_plan_2026-09-02.md` and the Event 016 final completion contract within a three-file write boundary. The parent clarified that generic CXT setup already registers the six Singularity components, so this change exercises their existing project objects and does not register them again. The observation probe is **implemented** with source and static-inventory evidence below; the full provider fixture matrix remains **unresolved** because CXT's ordinary setup and the current provider gate do not permit authentic provider transactions in this boundary.

## Files and identifiers

| File | Change |
| --- | --- |
| `common/scripted_effects/016_alien_infantry_cxt_test_effects.txt` | Added explicit `chaosx_cxt_event016_probe_native_inventory` effect. The existing carrier and `_apply` effect are unchanged. |
| `docs/testing/chaosx_test_country.md` | Documented invocation, scope, inputs, outputs, idempotence, and the difference between native inventory and provider receipts. |
| This handoff | Records evidence, unsupported scenarios, and parent integration needs. |

The new effect is country scoped and runs only for initialized `CXT` when the player invokes `e chaosx_cxt_event016_probe_native_inventory`. It has no input parameters, costs, grants, project completion effects, or normal CXT extension call site. Every run clears and rebuilds the private observation arrays `chaosx_cxt_event016_observed_native_families`, `chaosx_cxt_event016_observed_biological_agents`, and `chaosx_cxt_event016_observed_singularity_components`. The first array contains all fifteen family IDs only when the thirteen mapped family projects, all six biological agent projects, and all six Singularity component projects are completed. The probe also refreshes `chaosx_cxt_event016_probe_dlc_available` and `chaosx_cxt_event016_probe_provider_gate_closed`; the latter checks absence of the Kruger current-host flag and Mengele provider receipt initializer and a false Mengele provider gate. These flags and arrays are test observations only and no gameplay trigger reads them.

The probe uses the existing `brilliant_scientist_project_family`, `brilliant_scientist_biological_agent`, and `brilliant_scientist_singularity_component` constant categories. No constants, event targets, global flags, timers, weighted values, or cleanup effect were added. Repeated probes replace their own prior observations; no migration of provider or CXT registration data is required.

## Source and reference evidence

- All eleven required offline wiki core pages were consulted. No separate Special Project page exists in this snapshot; the installed `effects_documentation.md` and `triggers_documentation.md` entries for `complete_special_project` and `is_special_project_completed` define the native boundary, and installed vanilla project definitions supply the four reused vanilla project IDs. The installed script-constant documentation and a vanilla `clear_array` precedent were consulted.
- `common/scripted_effects/chaosx_dynamic_effects.txt` and its matching Markdown registry were inspected; they contain no neutral helper for this CXT-only observation, and the registry directs event-owned adapters to their owning source files.
- The generic CXT completion helper already enumerates every one of the 26 distinct project IDs referenced by the probe. Thirteen direct family rows plus Biological Weapons and Singularity conditional rows make fifteen family observations; there are six agent rows and six component rows. The four vanilla project definitions are in `air_projects.txt`, `radar_projects.txt`, `rocket_projects.txt`, and `nuclear_projects.txt`; the remaining referenced IDs are defined by the mod.
- Read-only `hoi4.event_inspect` traced `chaosx.nr16.901` with revision `8dea088062e0fd592f7fbc57f33971e20e80302ff6f4897b4e8345bef63a050f`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dafc15a0a1c0c49ff9cbf70c26f93865c5155ff755cb2a1e8ca83238b68b16c6/cf97b3e8c061d9b10549eb5682ddb9700a17baa175e98d96a8b5d6b001c82b6a/event-trace-8dea088062e0.json`. This is navigation evidence only. Its validation field reports 3,909 blocking graph diagnostics across the full workspace, not a task-specific runtime verdict.
- Static validation counted fifteen family rows, six agent rows, and six component rows; all 26 referenced IDs occur in the generic CXT project-completion list, and each resolves to a mod or installed vanilla project definition. The scoped diff check found no whitespace error. No HOI4 process, live save, timed decision, native project clock, native raid, or DLC-state transaction was run.

## Scenario coverage and exact blockers

| Accepted scenario | This handoff's evidence | Remaining blocker |
| --- | --- | --- |
| Fifteen provider families | The private array maps the thirteen direct native project families and adds Biological Weapons and Singularity only when their six underlying project objects each exist as completed. | An observed CXT project object is not a Mengele Theory, Prototype, Deployment, or Weaponization receipt. |
| Native Prototype callback versus paid stage, including rocketry alternatives | The probe observes the completed native objects; rocketry is one family row if either installed alternative is completed. | `chaosx_test_country_complete_all_special_projects` completes projects before a valid provider owns callbacks, bypassing normal clock and payment. No native completion is fabricated here. |
| Begin, finish, and cancel in both DLC states | The probe records the current Gotterdammerung state only. | The provider decision callbacks and native decision lifecycle live outside the assigned write scope. `brilliant_scientist_mengele_project_stage_provider_is_valid` requires a real Mengele directorate, registry, and active program state that ordinary CXT intentionally lacks. |
| Six Singularity components | Six existing component project objects are individually observed; generic CXT owns their completion registration. | This does not prove provider component de-duplication, provider six-count, or Fallout settlement. No second component registration was added. |
| Six biological agents | Six project-backed agent IDs are individually observed. | Native biological raid eligibility, payload reservation, results, and cleanup require the separate raid surface and actual provider conditions. |
| DHR five-receipt positive and negative | None claimed. | Ordinary CXT grants broad conventional knowledge and lacks Mengele identity, so toggling DHR receipts here would contaminate the normal registry or prove only an identity failure. Real provider scenarios must vary the five exact learned operational receipts. |
| Provider cleanup | The existing CXT `_apply` still calls `brilliant_scientist_mengele_cleanup_provider_receipts` only for an invalid provider; the probe confirms CXT remains isolated. | CXT has no authentic active provider payment receipt to cancel or refund. Synthetic receipts would falsely imply transaction coverage. |

## Parent integration map

For full scenario evidence, keep the existing private provider helpers and their real call sites: `brilliant_scientist_mengele_begin_project_stage` from timed decision `complete_effect`, `brilliant_scientist_mengele_cancel_project_stage` from exact `cancel_effect` or cleanup, `brilliant_scientist_mengele_finish_project_stage` from exact `remove_effect`, `brilliant_scientist_mengele_record_native_project_prototype` from the authentic project callback, `brilliant_scientist_mengele_record_singularity_component` from the six authentic component callbacks, and `brilliant_scientist_mengele_cleanup_provider_receipts` from provider loss. Their scope is a real provider country, their inputs are existing literal family/stage or component selectors and active receipts, and their side effects are normal paid settlement or cleanup. The CXT probe is a separate read-only observation path and must not be migrated into any of those call sites.

The tuning table remains the existing Event 016 family/stage constants and provider quote helper; the probe introduces no cost or duration. No event target is needed. The parent should validate normal provider transactions under both DLC states using the scenario matrix without copying CXT's completed-project inventory into provider flags. DHR positive and missing-one-receipt cases, native callback de-duplication, same-family re-entry, refunds, six-component de-duplication, raid outcomes, and Fallout remain unsupported by this handoff. No simplification is presented as coverage.
