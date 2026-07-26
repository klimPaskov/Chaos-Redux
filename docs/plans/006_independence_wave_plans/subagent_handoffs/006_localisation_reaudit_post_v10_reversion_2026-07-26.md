# Event 006 English localisation re-audit after v10 and focus reversion

Audit date: 2026-07-26.

Audit scope: read-only review of the current Event 006 English localisation, scripted-localisation consumers, DM-58 tooltip addition, Event Details and evolution mirrors, decisions, focuses, formables, achievements, SCN-008, super-events, and the current source-of-truth and v10/reversion handoffs.

## Verdict

**PARTIAL.** Static localisation coverage, key wiring, dynamic selectors, encoding, and cost triplets pass for the current tree. Player-facing scenario and formable readiness wording still exposes implementation vocabulary, and a few visible counts and DM-58 member counts are hardcoded instead of dynamic. Whole-event completion remains **HOLD** under the v10 authority and current source-of-truth map.

The current tree was inspected at `a605cda0a` with the restored focus baseline after `8fddaeea3`, `c314f8eb8`, and the v10 documentation reconciliation. The working tree also contains an uncommitted `006_independence_wave_form05_l_english.yml` addition of twenty-six cost tooltip and blocked keys; those keys were audited but were not edited by this pass.

## Missing key list

- **None in the current Event 006 source scope.** All 34 scoped English files resolve their parsed keys, including event, event-log, Event Details, evolution, focus, decision, GUI, country, idea, formable, achievement, scenario, report, and super-event surfaces.
- The ten Event 006 scripted-localisation files contain 100 `localization_key` references and 94 unique targets; all resolve when the shared `localisation/english/chaosx_gui_l_english.yml:173-176` intensity keys are included.
- All 321 Event 006 `custom_cost_text` references resolve to a base key plus matching `_tooltip` and `_blocked` keys. The current tree has 101 unique cost bases, including the uncommitted FORM-05 tranche.
- The DM-58 source consumer at `common/decisions/006_independence_wave_decisions.txt:3552` resolves to the single English key `independence_wave_coordinate_reclamation_fronts_preflight_tt` at `localisation/english/006_independence_wave_decisions_l_english.yml:222`.
- No Event 006 interface text, button text, or tooltip reference was missing.

## Duplicate key list

- **None.** The 34-file scan parsed 5,603 unique localisation keys and found zero duplicate IDs.

## Scripted localisation issue list

- **No unresolved scripted-localisation target.** `GetIndependenceWaveLeaguePhase` remains defined in `common/scripted_localisation/006_independence_wave_scripted_localisation.txt:9` and the Statehood Ledger uses the named selector in `localisation/english/006_independence_wave_gui_l_english.yml:17`.
- **No raw trigger fragments are exposed in the audited player-facing values.** The scan found no visible `check_variable`, `has_*`, `NOT =`, flag, or scripted-effect fragments.
- SCN-008 type, intensity, territory, force, failure-reason, ledger-package-ID, and ledger-reason selectors all resolve to English keys. Their fallback branches are source-level selectors, not missing localisation.
- DM-58 source wiring is complete at the tooltip level. The v10 execution gap is gameplay-side random state selection after activation, not a missing or misleading key in the preflight text.

## Dynamic text opportunities

- `localisation/english/006_independence_wave_scenario_l_english.yml:31` hardcodes `138`, `55`, and `13` in the SCN-008 ready message. The first two values already exist as `independence_wave_scenario_registry.bound_package_count` and `disabled_unbound_package_count` at `common/script_constants/006_independence_wave_scenario_constants.txt:29-30`; the overlay count is currently only implied by the `206` total. A scripted getter or explicit overlay constant would prevent the ready text drifting from the binding registry.
- `localisation/english/006_independence_wave_decisions_l_english.yml:221-222` hardcodes “three compliant members” and “three different external powers” while `common/script_constants/006_independence_wave_decision_constants.txt:273` defines `formation_member_minimum = 3`. A constant formatter or scripted selector would keep the DM-58 description and preflight tooltip aligned if the gate changes.
- Existing event presentation values, Statehood Ledger actor and patron getters, SCN-008 post-run counters, named league phase, formable name getter, and cost constant formatters are already dynamic; no additional correctness gap was found there.

## Cross-surface mismatch notes

- Event Details and all five evolution fields match the current exported catalog wording after `a605cda0a`; the shared Event Details key is `localisation/english/chaosx_gui_l_english.yml:956`. The generic Event Details remains premise-only and does not expose package IDs or hidden formables.
- The SCN-008 exported scenario row now exactly mirrors `chaosx.scenarios.independence_wave.desc.sovereign_scatter` and its eight type names. The wording is synchronized, but both the localisation and CSV expose implementation terms that conflict with the accepted player-facing direction in `006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md:624,647`.
- Evolution 2 at `localisation/english/006_independence_wave_evolutions_l_english.yml:6` says “regional and signature independence packages can surface sooner.” “Packages” reads as an internal registry term in an evolution body. Evolution 5 at line 12 says projects “enter the independence pool,” which exposes a pool mechanic rather than the public change.
- DM-58 lines 221-225 correctly describe the three-member, distinct-owner preflight and safe rollback outcome, but “synchronized transaction” and “staged operation is rolled back” are implementation-flavored terms that deserve a player-facing wording review. The source/runtime distinction remains documented in `006_event_completion_audit_v10_post_cf2316a9a_f8ca54d24_2026_07_26.md` and does not justify changing the preflight claim without a gameplay decision.
- SCN-008 scenario descriptions at `localisation/english/006_independence_wave_scenario_l_english.yml:14-21` use “release planner,” “map-bound package,” “anchor collisions,” “unique-anchor covenant,” “frozen plan,” “host-remnant validation,” “territory package,” and similar internal terms. The ready line at 31 adds “current-map bindings,” “route overlays,” and “non-selectable.”
- `chaosx.triggerable_scenarios.80.d` at scenario localisation line 34 exposes “Transaction proof,” “Released packages,” “Blocked bound packages,” “Disabled without a unique current-map binding,” “Territory package,” “Force package,” and “registry package disabled.” The SCN-008 ledger keys at lines 48-55 expose “Blocked-Candidate Ledger,” “registry row,” “frozen scenario plan,” and “Navigation changes no gameplay value.” These are useful diagnostics for developers but are not player-facing state descriptions.
- Scenario rejection keys at lines 67-75 expose “final live validation barrier,” “safe country creation could not be proven,” “former-host scope,” “package metadata,” “frozen country and state rows,” “unclassified transaction proof,” and “generic substitute.” The rejection reasons should remain factually specific while describing the player-visible reason, such as an already claimed anchor, invalid host remnant, or unavailable identity.
- Formable registry readiness keys at `localisation/english/006_independence_wave_formable_registry_l_english.yml:45-47` expose “family-matched surveys,” “reserved national identity,” “territorial-anchor thresholds,” and “one exact carrier.” These are internal contract terms and need a wording pass if the shared formation decision surface is visible to players.
- `independence_wave_formable_name_unknown` at formable registry line 43 is an explicit fallback, “the Unsettled Regional Project.” The scripted getter falls through to it at `common/scripted_localisation/006_independence_wave_formable_registry_scripted_localisation.txt:202`; confirm the invalid-family branch is hidden or fail-closed before treating this placeholder-like name as player-facing.
- Super-event 6002 remains correctly titled `Every Border a Casus Belli` with matching description, button, quote, and history milestone. Super-event 6001 remains absent and rights-blocked as required; no localisation gap was found.
- The focus coordinate reversion changed no focus IDs, prerequisites, rewards, icons, AI, or focus localisation. The stale focus geometry statements are documentation-only and do not create a player-facing localisation mismatch.
- `006_documentation_reconciliation_post_cf2316a9a_f8ca54d24_2026_07_26.md:16,18,47,62,69` still describes v9 as current authority and the f8 MCP result as `Transport closed`; those claims are superseded by v10, `8fddaeea3`, and the restored-baseline handoff. The previous `006_localisation_audit_current_2026-07-26.md` also reports the earlier 5,575-key count; the current working tree has 5,603 keys because of the uncommitted FORM-05 additions. These are docs-only stale statements, not missing game strings.

## File encoding concerns

- All 34 scoped Event 006 English YML files begin with UTF-8 BOM bytes `EF BB BF` and decode as UTF-8.
- No scoped key uses the forbidden `:0` suffix, and no semicolon or em dash sentence punctuation remains in the current Event 006 English values.
- No encoding blocker was found. Any mojibake visible in a PowerShell console is a console-code-page display issue, not an observed localisation-file byte failure.

## Recommended fixes

1. Rewrite the SCN-008 scenario descriptions, ready status, summary, ledger labels, and rejection reasons in `localisation/english/006_independence_wave_scenario_l_english.yml` into player-readable political, territorial, and diplomatic language while preserving the existing dynamic counts, selected rule, intensity, type, and exact rejection outcomes.
2. Replace “packages” and “independence pool” in `localisation/english/006_independence_wave_evolutions_l_english.yml:6,12` with public-facing wording that describes the evolution without exposing registry mechanics or hidden-route internals.
3. Review `localisation/english/006_independence_wave_formable_registry_l_english.yml:43,45-47` for visibility and rewrite readiness requirements around the player-visible settlement, consent, territory, and identity conditions. Keep hidden families hidden until their reveal logic is true.
4. If the current registry counts are intended to remain visible in the SCN-008 ready state, add a dynamic count selector or registry constants and replace the hardcoded `138/55/13` text at scenario line 31.
5. If the three-slot DM-58 contract is tunable, add dynamic member/owner count formatting for lines 221-222 and consider replacing implementation-flavored “transaction” language without weakening the documented rollback result.
6. Add a supersession note to the historical v9 documentation reconciliation and refresh the older localisation-audit count when the current FORM-05 localisation additions are committed. No gameplay or localisation edit was made by this audit.

## Changed files and display behavior

- Changed by this audit: only this handoff file.
- Gameplay and localisation files changed by this audit: none.
- Changed keys: none by this audit. The twenty-six FORM-05 cost tooltip and blocked keys observed in the working tree are parent/working-tree changes, not authored here; they now complete the cost triplets for the current 321 references.
- Dynamic localisation added or fixed by this audit: none. Existing phase, scenario, formable, actor, patron, and cost selectors were verified.
- Before and after display behavior: unchanged by this audit because this was read-only. Static coverage is now documented against the current 5,603-key tree, while the wording and hardcoded-count gaps above remain unresolved.

## Meaningful validation

- Parsed all 34 scoped English YML files for BOM, UTF-8 decoding, key shape, duplicate IDs, `:0` suffixes, semicolon/em-dash punctuation, and current key count.
- Compared all ten Event 006 scripted-localisation files, 100 localisation-key references, 321 custom-cost references and triplets, DM-58 source/definition cardinality, and Event 006 interface references with the English key set.
- Recomputed the current SCN-008 catalogue type/options and evolution mirrors; the exported Event 006 evolution fields and SCN-008 text match their current in-game localisation values.
- Read the accepted seven-part specification, current source-of-truth map, v10 completion audit, focus reversion handoff, prior localisation audit and closeout, super-event research, formable registry documentation, and relevant offline localisation and vanilla localisation documentation.

## Skipped meaningful validation

- No Hearts of Iron IV process, live GUI, Event Details window, Event Log, or save/load playback was run. This was a source-level read-only audit and live consumer validation remains with the parent/user.
- No MCP focus or GUI rewrite was run because the focus reversion changed no localisation semantics and the current audit was scoped to text coverage and wording.
- No workbook edit or export was run because the parent had already aligned the Event 006 catalog in `a605cda0a` and this pass made no player-facing text change.

## Unresolved wording decisions

- Whether SCN-008 should expose a diagnostic ledger at all, or only show player-readable causes without package IDs, frozen-plan language, and transaction terminology.
- Whether “package” and “pool” in Evolution 2 and Evolution 5 are accepted in-world shorthand or must be replaced to satisfy the specification's ban on implementation language.
- Whether the formable registry's unknown-family fallback can ever be visible; no runtime reachability claim was made here.
- Whether DM-58 should present the three-member gate as a dynamic number and whether its rollback language should remain explicit for resource clarity.

## Simplifications, omissions, and blockers

- No localisation or gameplay simplification was introduced by this audit.
- The audit does not claim whole-event completion. DM-58 runtime witness commitment, restored shared-focus zero-blocker validation, unadmitted country packages, blocked formables, super-event 6001, AI, balance, and live execution remain governed by the v10/source-of-truth HOLD state.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_localisation_reaudit_post_v10_reversion_2026-07-26.md`.
