# Event 35 Bank Lifecycle Decision Audit

Status: bounded read-only source audit delivered for parent review. Two localization and AI cost-contract gaps remain recorded below. The final current-valid actor guard is present in both bank context triggers and the shared bank failure resolver.

Acceptance basis: the parent task authorized the full Event 35 specification package without simplifications. This audit covers only the bank holiday, audit, recapitalization, policy withdrawal, deadline recovery, mission capacity, cleanup, and related localization surfaces named in the task.

## Scope and source identity

This subagent changed only this handoff file. It did not edit gameplay, tests, localization, assets, or Git state. It did not launch Hearts of Iron IV or request logs.

The current source identities read for this handoff are:

| File | SHA-256 |
| --- | --- |
| `common/decisions/035_great_depression_decisions.txt` | `7CFB33FA89DCE450B3692A2C87D01100374B61B20C36448F40FA4BFB2EDF20E5` |
| `common/scripted_effects/035_great_depression_bank_effects.txt` | `633F27EC77552D19B4354C008FEE71B87409F093B6A404B663C36C434CB94155` |
| `common/scripted_triggers/035_great_depression_bank_triggers.txt` | `A133A8A86994A2778D7EB96FAAE9F7C208EA4F9B84B7480BFCF3E9804898292D` |
| `common/scripted_triggers/035_great_depression_triggers.txt` | `0A092F8B2AA71CC87F8682E8551B0FD0788C789A1B6E41C2642706594A195925` |
| `common/scripted_effects/035_great_depression_decision_effects.txt` | `16B87B44668B9A5D5ED2BE3F673F2F9C3A04632126ABB165767BF872EA2DC5A4` |
| `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt` | `A59B1034461ED5ED4272AA614F11B134C2BE55F760222A4F12BA5C12DDFF3E32` |
| `common/scripted_effects/035_great_depression_effects.txt` | `34643D34E5788DD6CFD26155370A583CF949EA8DCE04FADACBF9DDBBAF0FACE2` |
| `common/scripted_effects/035_great_depression_incident_effects.txt` | `27A1B1889B7E44E2FF2FAE17D825A132DB0967FAC6A907C7AAE0DA51519A9E99` |
| `common/script_constants/035_great_depression_constants.txt` | `38565055771CBE1CABB3BA5A639A44FD21C883827B6039951215743AE0D35863` |
| `localisation/english/035_great_depression_l_english.yml` | `DCE24F6FC7F7347E43E882D800F0B3C879162C7B0276E82C294DC7BEB89F0C77` |

The accepted finance route in `docs/specs/035_great_depression_specs/035_great_depression_spec_part_3_decisions_missions.md:219-262` orders bank holiday and audit, reopening viable institutions, recapitalization, then a durable guarantee. The decision map at `docs/specs/035_great_depression_specs/035_great_depression_decision_map.md:62-73,205-241` sets the route sequence, two-support-mission limit, three-active-mission ceiling, four-cost finance family, and visibility limit. The mission implementation prompt at `docs/specs/035_great_depression_specs/035_great_depression_decision_mission_prompt.md:230-238` requires automatic completion, centralized duration, distinct success and failure, no second payment, save-safe state, and cancellation for invalid countries without a failure effect.

## Findings sorted by severity

### High

No confirmed high-severity lifecycle defect remains in the latest source. `great_depression_active_country_is_valid` is now required by both bank contexts and by `great_depression_fail_bank_program`, so an actor that becomes special, nonhuman, or otherwise invalid cannot certify the audit or receive renewed panic from the cancellation or timeout failure helper. The shared predicate checks `exists`, `uses_normal_civilian_systems`, exclusion from special and actual nonhuman countries, and coherent crisis state in `common/scripted_triggers/035_great_depression_triggers.txt:107-113`.

The owner reports all 15 actual-source bank lifecycle tests passing, including the invalid-actor cases. This audit did not rerun that suite.

### Medium

The recapitalization action uses the finance-trade custom cost, which includes political power, but its decision block has no `ai_hint_pp_cost`. The audit action uses the shared fixed hint at `common/decisions/035_great_depression_decisions.txt:1070`, while `great_depression_recapitalize_viable_institutions` omits it at lines 1087-1120. The action still gates affordability and its AI weight checks affordability, but the custom-cost AI reserve hint is missing. The source diff contains no changed legacy AI weight coefficients. The probability owner remains responsible for any AI behavior change and its comparison.

Both missions use `custom_cost_text = great_depression_financial_program_prepaid` at `common/decisions/035_great_depression_decisions.txt:3288-3289,3311-3312`. Localization contains only the base key at `localisation/english/035_great_depression_l_english.yml:598`; no `_blocked` or `_tooltip` variants exist anywhere under `localisation/`. The row is a prepaid status, not another payment. Add exact aliases to the base status for the native suffixed keys so the mission cost contract is complete without duplicating payment prose.

The decision tooltips describe a 21-day audit and 42-day recapitalization, while the native mission deadlines are 28 and 49 days. Success is allowed from day 21 or 42 up to, but not including, the respective deadline. The final seven days are recovery grace, and expiry fails the program. The action and mission descriptions do not explain that grace while the native mission exposes the longer deadline. Clarify the minimum proof interval and the final failure deadline in the player-facing wording.

### Low

The current native decision inspection covers only `great_depression_audit_viable_banks`. It does not provide current scenario evidence for the recapitalization mission or either bank action. This is a coverage limitation, not evidence that those source definitions are invalid.

## Decision category lifecycle and cognitive load

Both bank actions remain in the existing Event 35 decision category and are visible only in the Stabilize Finance and Trade doctrine through the ordinary decision surface. The route has four primary actions in its specification, below the six-action limit. The bank audit and recapitalization each reserve one supporting objective. The centralized support gate permits fewer than two occupied slots and counts both native active missions and current funded receipts, with an `OR` per bank mission so a restored or missing native mission cannot double-count one authorization. The gate is at `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt:2173-2185`; the displayed capacity ledger mirrors that `OR` counting in `common/scripted_effects/035_great_depression_decision_effects.txt:82-116`. The global mission budget remains one main mission plus two support missions, for three total.

The visible bank-facing values have clear gameplay significance: the holiday has an output penalty, the audit and recapitalization have a proof interval, and the support slot limits concurrent work. The hidden episode IDs and due dates are not exposed as raw counters. The only notable text-density issue is the unexplained seven-day grace between the stated proof interval and native timeout.

## Mission quality

| Mission | Owner and category | Region | Requirement and duration | Success | Failure and duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `great_depression_audit_viable_banks` | Country owner, existing Event 35 category | National | Current episode, valid normal-civilian actor, Finance and Trade doctrine, current audit receipt, at least one factory, no capitulation, stability at the bank floor. Proof opens after 21 days and must complete before day 28. | Closes the holiday, records current-episode audit proof, applies light Severity relief, and opens recapitalization. | Timeout or deliberate policy withdrawal by a valid country renews panic for the configured shock-memory interval and increases Severity. Invalid-country cancellation is cleanup without failure. One mission ID and one active receipt prevent duplicate audits. |
| `great_depression_certify_bank_recapitalization` | Country owner, existing Event 35 category | National | Current episode, valid normal-civilian actor, Finance and Trade doctrine, current audit proof, current funded recap receipt, the same viable productive base and stability floor. Proof opens after 42 days and must complete before day 49. | Records recapitalization, applies strong Severity relief, and unlocks the durable guarantee. | Timeout or deliberate policy withdrawal by a valid country renews panic and increases Severity. Invalid-country cancellation is cleanup without failure. Failed recapitalization can be retried after the decision cooldown, while successful proof is one-time per episode. |

These are short emergency finance objectives. Their 21/28-day and 42/49-day timing is centralized in `common/script_constants/035_great_depression_constants.txt:51-54`, not copied as literals into the decision definitions. `selectable_mission = no` and the `available` objective make them auto-completing without a second click. `is_good = no` is consistent with the offline mission tooltip rule because the successful objective completes the mission and `timeout_effect` is the failure effect.

## Lifecycle, reset, and callback audit

The paid action hooks are `great_depression_declare_temporary_bank_holiday_and_audit` and `great_depression_recapitalize_viable_institutions` in `common/scripted_effects/035_great_depression_decision_effects.txt:527-551`. Each rechecks its start predicate and affordability before committing one shared action payment and authorizing its episode-bound mission. The audit also applies the temporary bank-holiday modifier. The recapitalization action cannot start without current audit proof. The durable guarantee requires current audit proof and the recapitalization episode ID to equal the active episode in `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt:1670-1678`.

Mission success checks are repeated in `great_depression_complete_bank_audit` and `great_depression_complete_bank_recapitalization` in `common/scripted_effects/035_great_depression_bank_effects.txt:32-53`. Both objectives require the current episode receipt and current-valid actor. The objective also requires `global.num_days < deadline_day`, so a due check after day 28 or 49 cannot produce a late reward.

The shared failure effect now requires `great_depression_active_country_is_valid` and a current audit or recap receipt before it writes failure flags, renewed panic, or Severity in `common/scripted_effects/035_great_depression_bank_effects.txt:63-88`. It clears each active marker before nested effects, making repeated cancellation or timeout callbacks inert. Both existing policy-review actions call `great_depression_withdraw_bank_program` before changing doctrine in `common/scripted_effects/035_great_depression_decision_effects.txt:455-475`, so deliberate early withdrawal by a valid country retains the specified panic consequence.

Reset ordering is safe in source. `great_depression_clear_dynamic_state` calls `great_depression_clear_bank_program_runtime` first in `common/scripted_effects/035_great_depression_effects.txt:2303-2357`. `great_depression_cancel_all_missions` also begins with that helper in `common/scripted_effects/035_great_depression_decision_effects.txt:119-140`. The bank helper clears active receipts before removing either mission, removes the temporary modifier, then clears due dates, deadlines, and episode IDs in `common/scripted_effects/035_great_depression_bank_effects.txt:107-117`. Abort, actor invalidation, episode reset, and recovery paths invoke this cleanup before a successor episode can authorize the same mission ID.

Installed game documentation says `remove_mission` removes the mission without running completion or timeout effects. The offline mission documentation and vanilla precedent also support the auto-completion, timeout, and cancellation shape. No source path was found that lets a completion or timeout from the retired episode pass the current active receipt and episode checks. The parent fixture records native activation and removal but does not emulate an engine scheduler. Any callback already queued by the native engine before removal remains a runtime scheduling uncertainty rather than a demonstrated source defect.

The existing active-country receiver is unchanged. `great_depression_process_active_registry` iterates the registered active-country array and queues `chaosx.nr35.8` for each valid owner in `common/scripted_effects/035_great_depression_effects.txt:5028-5061`. That country event invokes `great_depression_weekly_pulse` in `events/035_great_depression.txt:175-190`, and the pulse runs `great_depression_process_bank_program` before phase cadence in `common/scripted_effects/035_great_depression_effects.txt:4866-4871`. Reconciliation restores a missing native mission and synchronizes its timeout from the saved absolute deadline. The calculation is `deadline_day - global.num_days - days_mission_timeout@mission_id`, followed by `add_days_mission_timeout`, in `common/scripted_effects/035_great_depression_bank_effects.txt:120-159`. A deadline already reached fails instead of restarting the interval.

The separate `bank_holiday` incident records `great_depression_bank_holiday_observed` in `common/scripted_effects/035_great_depression_incident_effects.txt:654-657`. It does not set `great_depression_bank_audit_complete`. Only the guarded audit success effect writes that proof flag.

## Cost, requirements, AI, and localization

The audit and recapitalization decisions use the `finance_trade` cost family. It has four spendable types: political power, convoys, fuel, and committed civilian factory capacity. The inline row shows three icon-bearing values, and the full tooltip shows the civilian-factory commitment as a fourth. The displayed icons are `£pol_power`, `£convoy_texticon`, `£GFX_fuel_texticon`, and `£civ_factory`. The family has available, blocked, and tooltip localization at `localisation/english/035_great_depression_l_english.yml:387-389`. `great_depression_can_pay_finance_trade` checks all four values in `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt:642-653`, and both availability and custom-cost blocks use that same predicate. `great_depression_commit_country_action` pays once through `great_depression_pay_action_cost` in `common/scripted_effects/035_great_depression_decision_effects.txt:145-154`. The mission rows are prepaid and add no fifth payment.

The audit action is AI-weighted toward financial pressure and Finance and Trade profiles, with blockade or trade failure reducing its score. The recapitalization action additionally requires the audit-success AI check and reduces its score when rescue dependence is high. Source diff inspection showed no changed legacy Event 35 AI weight coefficients. No probability analysis was run here because the parent assigned that route to the separate probability owner.

The failure and success tooltips are present, and the bank viability tooltip names industry, capitulation, stability, and the stability floor. Mission titles and descriptions are present. The prepaid mission custom-cost localization is the only missing native key family found, as described above.

## Validation and evidence limits

The parent reports all 15 actual-source bank lifecycle tests passing, including invalid actor types, both policy reviews, missing-timer restoration, duplicate callbacks, recapitalization failure and retry, and the late guarantee. This subagent did not rerun the tests. No live-game or native scheduler test was run.

The latest completed `hoi4.decision_inspect` request targeted `great_depression_audit_viable_banks` under scenario `event35-bank-audit-lifecycle-refresh`. It returned `DECISION_ANALYZED_PARTIAL`, not a timeout or pending request, with `complete = false`, 100 unresolved definitions, and an inline source list truncated to 64 of 6,903 paths. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d4fe29877ce466d6f7e32025cc0552d028950b8ed1670a08b29e310496d0673b/430f19ef80bd8f50f0a83483fb40b55f2d656d4917858198821ab023493342ff/decision-52f04af03e39275e3011a76f.json`, source revision `83de2533ecb8b860a1f1d60f5d74aef8488b85ce9e06e32d10581db327aa7858`. Its decision-file source hash matched the local decision file, but the later actor-valid bank-trigger hash `A133A8A86994A2778D7EB96FAAE9F7C208EA4F9B84B7480BFCF3E9804898292D` postdates that artifact. The scenario did not declare the campaign flags and variables needed to resolve the gate, so its unresolved entries are not campaign eligibility evidence. Two earlier action-inspect attempts returned terminal `DECISION_SOURCE_STALE` errors as the source index changed. No native MCP request remains pending. Recapitalization and action IDs therefore retain source review but lack current per-ID decision-inspect evidence.

The reference routes resolved the relevant syntax coverage. Offline `paradox_wiki/Decision modding` lines 465-479, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, covers timed missions, auto-completion, activation, cancellation, and timeout. Installed `documentation/effects_documentation.md` lines 661-670, 1051-1065, and 6083-6092, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, covers mission activation, timeout adjustment, and removal semantics. Offline `paradox_wiki/Effects` line 1917, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, documents the variable form of `add_days_mission_timeout`. Installed `documentation/triggers_documentation.md` lines 2402-2411, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, documents `count_triggers`. Offline `paradox_wiki/Decision modding` lines 300-336, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, documents the base, blocked, and tooltip localization keys for custom costs. Vanilla `game:common/decisions/GER.txt`, `GER_mefo_bills_mission`, lines 92-161, source lookup revision `20afbef6b43300094deb0c3aeed9caf10d8fb5b55a9f7fb9b9929dc3c7114b7a`, provides a timed mission precedent with cancellation and timeout effects.

## Handoff to parent

Recommended source follow-ups are limited to adding `ai_hint_pp_cost = @great_depression_ai_hint_pp_cost` to `great_depression_recapitalize_viable_institutions` after the separate probability owner completes any required comparison, adding aliases for `great_depression_financial_program_prepaid_blocked` and `great_depression_financial_program_prepaid_tooltip`, and clarifying the 21/28 and 42/49 day windows in player-facing text. No gameplay patch or broad design expansion was made in this audit.

Remaining limitation: current mission lifecycle source is reviewed and the latest actor guard is included in the source identity above, but `decision_inspect` did not provide complete scenario coverage for every action and mission ID. Treat the route coverage as unresolved rather than source-equivalent engine evidence.

## Read-only addendum, 2026-10-07

This addendum records the parent's post-review source updates. It changes only this audit handoff and does not alter gameplay source. The earlier findings section remains the review-time snapshot. The three medium follow-ups below are now dispositioned implemented in the current source.

The recapitalization decision now includes `ai_hint_pp_cost = @great_depression_ai_hint_pp_cost` at `common/decisions/035_great_depression_decisions.txt:1106`. The parent reports that the probability owner was notified for the required post-change review. This addendum did not run a probability inspection or comparison, and it does not claim that comparison is complete.

The prepaid mission cost now has `great_depression_financial_program_prepaid_blocked` and `great_depression_financial_program_prepaid_tooltip` at `localisation/english/035_great_depression_l_english.yml:599-600`. The audit and recapitalization mission descriptions now state both the proof interval and final deadline at lines 595 and 597.

The mission table now distinguishes failure by a valid country from invalid-country retirement. The latest `great_depression_fail_bank_program` still requires `great_depression_active_country_is_valid` before it can set failure flags, renewed panic, or Severity at `common/scripted_effects/035_great_depression_bank_effects.txt:63-88`. Both bank context triggers use the same actor guard at `common/scripted_triggers/035_great_depression_bank_triggers.txt:33-43`. The parent reports all 15 actual-source bank tests passing, including the invalid actor cases. This audit did not rerun them.

The current post-review file identities are `common/decisions/035_great_depression_decisions.txt` SHA-256 `9F8B1D5C025EDD432070DBAE91A2CB0A4666812F123B712136181442DC99E42F`, `localisation/english/035_great_depression_l_english.yml` SHA-256 `94C7A24DC93CE400AE3A94EA3847358D0706CED99BC31BD02BA35276C7476BA0`, `common/scripted_effects/035_great_depression_bank_effects.txt` SHA-256 `633F27EC77552D19B4354C008FEE71B87409F093B6A404B663C36C434CB94155`, and `common/scripted_triggers/035_great_depression_bank_triggers.txt` SHA-256 `A133A8A86994A2778D7EB96FAAE9F7C208EA4F9B84B7480BFCF3E9804898292D`.

The original native artifact boundary is unchanged. Its `decision_inspect` request completed as `DECISION_ANALYZED_PARTIAL`, not as a timeout or pending request. It remains bound to source revision `83de2533ecb8b860a1f1d60f5d74aef8488b85ce9e06e32d10581db327aa7858`, covers only `great_depression_audit_viable_banks`, has unresolved scenario inputs, and does not include the post-review decision and localization hashes above. No broader MCP request was made for this addendum, and no native request remains pending.
