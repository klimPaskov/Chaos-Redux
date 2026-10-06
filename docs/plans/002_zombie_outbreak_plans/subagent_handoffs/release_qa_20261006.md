# Event 002 release QA handoff, 2026-10-06

Disposition: bounded source consolidation is implemented; full release QA remains unresolved at the evidence gates below. The parent owns final integration and commit.

## Current implementation

The weaponized profile category has one zero-cost map-only review action and one map-only counterstrain research action, each targeted at eligible profile capitals. The category remains visible for a live weaponized profile even when the standard outbreak flag is absent. The current decision source SHA-256 is `45b49a133a44474770f03c7fbfd6651c4c005f81f31d004d8b59fa5088c2422f`.

Profile research requires exactly one of the eight type flags, excludes a Wendigo profile with its transformation lock, preserves the selected type and capital during the timer, and cancels with the paid Political Power and matching active sale receipt returned when the type or research eligibility changes. Completed local or shared strain progress hides that strain's action. Existing values remain 45 PP, 55 research days, 34 progress and 240 exposure days; no balance value was changed in this tranche.

The source contract uses the eight existing progress outputs in `apply_weaponized_zombie_counterstrain_research`; the capital decision stores the type through `set_weaponized_zombie_counterstrain_type_from_selected_profile`. The test file parses the relevant current Clausewitz bodies and checks receipt handling and all eight type paths. Its previously uninitialized `state_flags` test fixture is now initialized, so the `has_state_flag` interpreter branch is safe if later exercised.

## Source hashes

Hashes below bind the handoff to the current inspected files. The decision file was frozen at the accepted SHA shown here; no changes to shared localisation, shared systems, assets or the decision source were made in this final handoff pass.

| File | SHA-256 |
| --- | --- |
| `events/002_zombie_outbreak.txt` | `9d3fbca3098da51fa0e946d8c98be810e4da5b2f24f869f7fb52915525d6f253` |
| `events/zombie_weaponized_special_projects.txt` | `b723e9cdb2e9b064659e4689783d03ecc49bcee9a33e03d744cc3cd1938fc0c1` |
| `common/decisions/002_zombie_outbreak_decisions.txt` | `45b49a133a44474770f03c7fbfd6651c4c005f81f31d004d8b59fa5088c2422f` |
| `common/decisions/categories/002_zombie_outbreak_categories.txt` | `f5bebd9a71ab5587dc112ec5eeb91ae39d4a4e8439f6106fd65c57a292bd7f7d` |
| `common/scripted_effects/002_zombie_outbreak_effects.txt` | `1adf1b05f532d7a477e7a5ded2bf94ed20b0c0e6543dcc6f583f9ad9626c72ed` |
| `common/scripted_triggers/002_zombie_outbreak_triggers.txt` | `c2ee9c3a6c42e6ea7810571c101890be6907021cd355539f571d47737cf896af` |
| `common/scripted_localisation/002_zombie_outbreak_scripted_localisation.txt` | `70793cc14d94bc362b95d203e0886ac6c1dfe112e0b57783afc25b2e31e66efb` |
| `common/script_constants/002_zombie_constants.txt` | `7754b0bc4e33e2547dfc70cd7c5754caffa3c7bb9d9453a887b60105686ef9b9` |
| `localisation/english/002_zombie_outbreak_l_english.yml` | `740e0d4688c39c82bbe75e333b8d6a302b4a00528b701e06764ac7b0887477b4` |
| `localisation/english/chaosx_decisions_l_english.yml` | `7f8845b2d78ced9cd0a46582dee9aa2ac93ca430c7b504a7a3e46fce9dac1c1c` |
| `docs/plans/002_zombie_outbreak_plans/subagent_handoffs/refund_receipt_scenarios_20261005.py` | `8a4fdc32760518a51f8d89fdeacd956a02838f535e4d067b2c82057a1ba389d5` |

The final-test harness hash includes the fixture initialization described above.

## Verification and open gates

`python docs/plans/002_zombie_outbreak_plans/subagent_handoffs/refund_receipt_scenarios_20261005.py` completed 10 tests successfully. The five counterstrain source scenarios cover all eight type flags, exact-one-type rejection, selected-type routing, local/shared progress and readiness, and the Wendigo lock. Five receipt scenarios cover sale cancellation, sequence preservation, exclusions, completion cleanup, and reset/expiry/investment rejection. These are bounded source-driven simulations with mocked HOI4 primitives; they do not establish native timer, decision, or race behavior.

Native references reviewed for the accepted targeting pattern were the installed decision documentation `_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, and offline wiki `Decision modding:531-537` and `576-595`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`. Vanilla precedent is `common/decisions/AFG.txt:1901-1929`, with map-only state-target actions. The documentation confirms `FROM` is the chosen target and map-only decisions appear on the map; it does not establish how two markers at the same capital stack or offset.

The mandatory probability workflow has no successful final numeric result. The typed baseline source is preserved as `typed_baseline_current_801e2221.txt` (SHA-256 `801e222166733aa43d43a523f6d3b950bcc54ebb36ed9539731ad4d47487cdd3`). The named scenario contract is `EVENT002_TYPED_COUNTERSTRAIN_BASELINE_20261006`, with `USA_AI_STANDALONE_INFECTED_ONLY` and `USA_AI_STANDALONE_ALL_EIGHT_TYPES`, actor USA, date 1936-07-01, and the eight typed actions. Candidate eligibility overrides and exact target-country/human-control state are not supported or verified by the live scenario schema. The baseline evaluator and mission inspection each timed out after 600 seconds; no result or scenario hash was produced. A corrected same-scenario compare was submitted against the 801E baseline and final `45b49a...` source, but the probability worker exited at model capacity before providing a result. The earlier `f842c...` attempt is superseded by the approved Wendigo-lock correction. Therefore no final numeric comparison is claimed.

The bounded Event 002 inspect previously returned `Transport closed`; no more MCP retries were requested. Live acceptance still needs to verify distinct clicking of review and research markers when both share a capital, along with the previously identified game-state cases in `release_qa_completion_20261006.md`. The parent applied generic action labels and descriptions in the shared decision localisation; current hash is listed above. No game or desktop launch was performed. Asset source/provenance and model QA, current matched cure/super GUI evidence, audio IDs 2/3/6, and portrait provenance remain independent release blockers recorded in the parent reconciliation.

## Changes in this final handoff pass

In this final handoff pass, `docs/plans/002_zombie_outbreak_plans/agent_decisions_2026-10-06.md` was corrected from queued to implemented status for the accepted consolidation, and `refund_receipt_scenarios_20261005.py` now initializes `state_flags`. This handoff records those updates. No shared files, assets, spreadsheets, or commits were touched.
