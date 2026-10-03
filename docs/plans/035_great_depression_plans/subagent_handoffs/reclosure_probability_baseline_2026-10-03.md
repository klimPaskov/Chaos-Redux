# Event 35 Reclosure Probability Baseline

Status: original source baseline and nine named cases remain preserved. The baseline inspect's terminal 600-second timeout has now been observed. The subsequent valid-schema after comparison is separately recorded as an unsupported helper-source adapter outcome, so no native availability or balance completion is claimed.

## Immutable inputs

Copies were made with Windows `Copy-Item`, without text decoding or newline conversion, under `docs/plans/035_great_depression_plans/audit_inputs/reclosure_2026_10_03/`. Each source hash before copying, copied-file hash, and source hash after copying matched. Existing evidence was not overwritten.

| Original source | Frozen filename | SHA-256 | Bytes |
| --- | --- | --- | ---: |
| `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt` | `035_great_depression_decision_surface_triggers_before.txt` | `AC4A7E1E2F2B911BB3231805A52A8B1CA11D5445D1858AC7E8524C68A09458BF` | 86912 |
| `common/scripted_effects/035_great_depression_effects.txt` | `035_great_depression_effects_before.txt` | `B9E01DE3EB2CC97FA31E73188745AF77A1EEF28F07D86AC51AC0346385AA28A9` | 433132 |
| `common/scripted_effects/035_great_depression_decision_effects.txt` | `035_great_depression_decision_effects_before.txt` | `E5FD51BF46AA5304623470BB78B72C8B832BDB92C2C94E9F596284702DFF040C` | 101564 |
| `common/decisions/035_great_depression_decisions.txt` | `035_great_depression_decisions_before.txt` | `42D0520152DB1C15C32B627D309CF7AB91EF33106E40162F96066B52712D0ED3` | 152710 |

The saved `reclosure_source_scenarios.json` is a domain source-contract fixture, not a verified MCP `scenarioSet`. Its SHA-256 is `4277873E9A8A110B8A6C15E13B80294BD669EDF22B78B8BD1A08B55D4F4C34E7`. Its symbolic actor A, state S, and current episode E avoid inventing campaign identities or numeric balance inputs. All profiles, actor gates, costs, affordability, and timers are held equal. Reuse the exact case IDs after the owner patch.

## Audited source surfaces

The frozen decision-surface triggers define `great_depression_center_is_valid_selector_target` at line 711 and `great_depression_selected_center_target_is_valid` at line 725. Both place `exists = yes` directly in state scope. Installed `documentation/triggers_documentation.md`, lines 2708-2714, documents `exists` as COUNTRY-only. The documented state identity trigger is at lines 7561-7567. Source confirms a scope-contract defect, but its actual engine return is unresolved.

`great_depression_center_project_target_is_open`, lines 737-743, excludes authorized, active-work, paused, certification, and historical `great_depression_center_project_completed_receipt`. The historical exclusion independently rejects an otherwise idle reclosed center and a reopened center's lasting-capacity or public-works follow-on.

The lasting-capacity target at lines 764-769 and public-works target at lines 778-783 both call that open-project predicate. The frozen decision-effects wrappers at lines 611-640 recheck those targets before authorization. The affected decision IDs are `great_depression_reopen_idled_plants`, `great_depression_launch_regional_works_program`, and `great_depression_convert_works_into_lasting_capacity`. Other selector consumers exist and are not treated as a complete normalized AI candidate pool.

The frozen main effects define `great_depression_clear_center_state_flags` at lines 619-631. It clears `great_depression_center_episode_id` at line 627. `great_depression_complete_center_project` calls it at line 845 and rebuilds physical center flags without restoring the episode there. Frozen decision effects call it during abandonment at lines 600 and 714. The reopen mission's objective at decision-surface lines 1902-1912 requires the state episode to equal `ROOT.great_depression_mission_reopen_center_episode_id`. This establishes a source proof-loss path after valid physical transitions.

`great_depression_adopt_transferred_center`, main-effects lines 1139-1280, validates the receiving actor, ownership/control, transfer receipt, and registry capacity. It installs registry, stage, project, and adoption facts but does not assign the receiving active episode to `great_depression_center_episode_id` in the preserved definition. Exact adoption proof and one-shot historical rewards must be considered separately by the owner patch.

`great_depression_complete_center_project` rejects the existing historical completed receipt at line 813 and sets it at line 825. Its specific public-works reward also has a completed receipt at lines 865-866. Simply clearing old receipts to reopen eligibility would weaken duplicate-reward protection. The parent intends separate current project identity and historical completion, with one-shot rewards preserved. No reward coefficients were chosen or changed by this auditor.

## Named baseline cases

| Case ID | Source-contract baseline | Owner's expected after relationship | Classification |
| --- | --- | --- | --- |
| `INH-RECLOSE-COMPLETED` | Historical completed receipt rejects an idle shuttered center | Permit the new valid project, preserve old reward history | Bounded source contract, native unresolved |
| `reopened->lasting_capacity` | Historical completed receipt rejects the mapped follow-on | Permit the distinct eligible follow-on | Bounded source contract, native unresolved |
| `reopened->public_works` | Historical completed receipt rejects the mapped follow-on despite no public-works receipt | Permit the eligible public-works project | Bounded source contract, native unresolved |
| `active-project blocked` | Active-work flag independently rejects opening | Remain blocked | Bounded source contract, native unresolved |
| `invalid episode blocked` | State selector predicates lack exact episode proof and contain unsupported country existence | Reject missing/mismatched state episode before payment | Source validity gap, native unresolved |
| `duplicate old reward blocked` | Completion guard rejects the old completed receipt | Keep old completion replay from paying again | Bounded source guard, native unresolved |
| `EPISODE-COMPLETE-PROOF` | Completion clears episode consumed by exact mission proof | Retain legitimate same-episode proof | Bounded source lifecycle, native unresolved |
| `EPISODE-ABANDON-PROOF` | Abandonment calls the same episode-clearing helper | Preserve identity across continuing physical transition | Bounded source lifecycle, native unresolved |
| `EPISODE-TRANSFER-ADOPT-PROOF` | Adoption does not replace state episode with receiving current episode | Bind accepted adoption to proven receiving episode | Bounded source lifecycle, native unresolved |

Each case declares one symbolic target S for an isolated predicate/transaction contract. This is complete only for that bounded target test. It is not the complete eligible-state, alternate-action, mission, or country pool. Numeric profile inputs, live campaign state, and native scope encoding are absent. No normalized probability, numerical willingness score, rank, dominance, starvation, timing, or full-pool balance result is claimed.

## MCP route state

The mandatory first probability request was `hoi4.probability_inspect`, adapter `decision_ai_will_do`, source `docs/plans/035_great_depression_plans/audit_inputs/reclosure_2026_10_03/035_great_depression_decisions_before.txt`, workspace `mod_chaos_redux_ea3b2d67c2c0`. It ran on cell 6 and was initially unobserved across interruptions. Its terminal result has now been observed: `timed out awaiting tools/call after 600s`. It is no longer a pending request. No analyzer revision, analysis ID, artifact URI, scenario hash, or render came from that call.

Evaluate/sweep were not run from that timed-out baseline inspect. The later documented state/scopes mapping, immutable after captures and final valid-schema comparison disposition are recorded in `reclosure_probability_compare_2026-10-03.md`. Decision `ai_will_do` is willingness evidence when evaluable, not a click probability. Simulation and sequence analysis are not applicable to these declared source contracts.

The decisions/missions skill was read fully for this baseline, alongside the already-read events, subagents, and scenario-planning guidance. Installed decision documentation `_documentation.md`, lines 18-44, establishes acting-country and target-state scope and availability/target gate roles. Source review does not establish native consumer execution.

Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 527-536, corroborates acting-country ROOT and potential state-target FROM for target triggers and availability. Its AI section, lines 358-363, describes modifier structure. This audit retains the required willingness-score interpretation and does not normalize competing decisions into click probabilities.

The reopen decision's unchanged AI body uses `constant:great_depression_target_weight.base`, urgency, high-value and recoverability additions, and a doomed-target factor. Public works retains its relief-coalition, state-coordinator, affordability, recoverability and high-value additions plus the doomed factor. Lasting capacity retains the stabilization, relief-coalition, state-coordinator and recoverability additions plus its not-ready factor. These are identified source trace components, not evaluated numeric scores. The shared constants file hash at capture is `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7`.

## Parent handoff

The parent can apply the bounded state/episode, current-project identity, completion-proof, and transfer-adoption changes against the preserved sources. Keep profile coefficients, costs, actor gates, state candidates, and reward amounts identical. Preserve historical one-shot rewards and block duplicate old completion callbacks. Use the exact saved cases in the mandatory after comparison.

This auditor wrote only frozen evidence, the scenario fixture, and this report. No gameplay, index, or commit changes were made. The probability conclusions remain incomplete until accepted MCP analysis exists.
