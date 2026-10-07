# Event 035 bank-program implementation

Disposition: implemented source tranche under the user's full-package instruction, part 3's bank-holiday/audit contract and part 11 C-03.
The compatible staged-work design in addendum A5 supplies the 21-day audit and 42-day recapitalization intervals.
Its conflicting fixed center duration and no-refund choices are not adopted by this tranche.
Whole Event 035 acceptance remains incomplete.

## Transactions and behavior

The authorization actions perform a fail-closed check of current doctrine, supporting-objective room, action lock, quote readiness and full four-type finance affordability before charging.
Each accepted action pays the existing dynamic political-power, convoy, fuel and civilian commitment quote once, records the ordinary response receipt and opens its funded mission on the acting country.
Mission completion makes no second material charge.
No separate reserved stockpile or refundable quantity is created by these bank programs; this does not dispose of the unimplemented regional-project refund requirement.
The temporary holiday applies the central output penalty and hidden temporary credit relief while the audit runs.
An observed Financial Contagion bank holiday keeps its observation and partner-aid metadata but cannot certify the country's funded audit.

Audit success requires the current episode, Finance and Trade policy, its full 21-day work interval, positive industry, no capitulation and Stability at least the central viability threshold.
It reopens viable banks, lowers Severity and enables the local-credit project and paid recapitalization.
It does not grant the lasting credit component relief.
Recapitalization uses the same current-episode audit proof and a separate 42-day funded mission.
Its successful certification lowers Severity and enables the durable credit treatment.
The durable guarantee needs audit and recapitalization proof during Stabilization.

Audit and recapitalization have absolute timeout deadlines at authorization plus 28 and 49 days respectively.
The extra seven days permit viability certification without restarting the work interval.
At or after the timeout deadline success is forbidden.
Failure or either existing policy-review action withdrawing unfinished work clears the active marker first and applies one renewed-panic consequence.
The renewed credit pressure uses the existing central shock-memory interval.
The same active/episode guards protect native callbacks and the bounded owner reconciliation from replay.

The existing active-country receiver reconciles bank programs before its phase-specific Severity cadence.
It restores a missing native mission against its original deadline, adjusts the native timer by the signed difference between remaining absolute time and `days_mission_timeout@mission`, and resolves expired work through the same failure guard.
No new whole-world on-action or country scan is introduced.
Funded proof reserves the support slot even while the native mission is missing.
The former support-slot predicate rejected triples rather than pairs; the documented `count_triggers` contract now enforces the central two-support limit across all seven supporting mission types.
The existing single main lane remains unchanged, giving three total objectives.
Cleanup closes bank markers before mission removal, clears deadlines and episode pointers, removes the holiday and transient bank flags, and grants no recovery or panic to a successor episode.

## Identifiers and source surfaces

New missions are `great_depression_audit_viable_banks` and `great_depression_certify_bank_recapitalization` in the existing category.
There are 79 ordinary decisions and 17 missions, 96 category children.
Seven original bank/mission helpers are in `common/scripted_effects/035_great_depression_bank_effects.txt`, with the two timer synchronizers and bounded reconciliation added in that same owner file.
Exact bank proof and objective predicates are in `common/scripted_triggers/035_great_depression_bank_triggers.txt`.
Existing decision effects, surface predicates, hidden components, mission capacity and terminal cleanup call those helpers.
The active-objective localisation includes both missions below main crisis emergencies.
Central constants hold work intervals, timeout deadlines, viability, output, credit and mission priority.
No event ID, evolution, Chaos source, normal pacing owner, country tag or shared adapter is added.

## Presentation and assets

Bank action and mission names, prepaid-cost rows, conditional cancellation, success, failure and proof descriptions are in `localisation/english/035_great_depression_l_english.yml`.
Three added tooltip-cache fields are derived from the same central bank tuning, and the existing foreign-ROOT cache test verifies all forty current fields belong to the actor.
Audit reuses the existing Halt the Panic mission-family sprite, recapitalization the Prevent a Relapse mission-family sprite, and the temporary holiday the existing Finance and Trade legacy spirit sprite.
These consumers use the original mission and spirit canvases; no image is resized across asset families and no art file or GFX definition is changed.
The package's mandatory full per-asset native-consumer review remains open; this source wiring does not recertify those images.

## Validation and evidence limits

Fifteen actual-source bank tests pass in `.tools/test_event035_bank_lifecycle.py`, including every one of the 128 support-pool subsets and normal-civilian actor eligibility.
They execute paid authorizations and both real policy-review effects, then invoke parsed production mission callbacks under declared native primitive state.
They cover exact work boundaries, premature completion, both failure types, final guarantee gates, stale proof, repeated payment and completion, foreign ROOT, observed-incident bypass, lost-timer shortening, reserved slots and owner/callback deduplication.
The source executor records native activation/removal and declared timer state; it is not the engine scheduler, UI, AI chooser or save system.
The existing fifteen center/project and eight inherited-hook tests pass; the finance producer fixture now supplies an exact current audit episode instead of only a flag.
The fourteen report/quote/CXT/cache tests pass after updating the cache inventory to forty and checking all three bank values.
All 79 pre-existing `ai_will_do` bodies compare equal against the frozen baseline; eligibility and proof dependencies change deliberately and require the separate same-scenario probability audit.
The decision auditor found a missing recapitalization `ai_hint_pp_cost`; the owner added the same existing static custom-cost reserve hint used by the audit action, while actual dynamic fees and affordability remain unchanged.
That native AI hint change is included in the probability owner's final-source request and must not be described as unchanged AI behavior.

Installed references read through the MCP include `activate_mission` at effects 661-670, `add_days_mission_timeout` at 1051-1065, and `add_dynamic_modifier` at 1153-1173, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The native timer getter is documented at dynamic variables 238-240, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`.
Native `count_triggers` was read at triggers 2402-2411, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
Offline mission behavior is Decision modding 465-479, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`; offline count behavior is Triggers 342, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`; offline timer adjustment is Effects 1917, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
Vanilla `common/decisions/GER.txt:92` supplies the timed, cancelable mission precedent.
The explicit COUNTRY audit-timer snippet check returned `SCRIPT_CHECK_PARTIAL`, valid null: seven checked commands, one unresolved scripted predicate and four unchecked native argument blocks, no omitted findings.
It checks native command kinds and declared scopes, not argument semantics or native scheduling.
Its installed documentation revision is `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The whole-file draft checks had unknown-scope roots and must not be substituted for that explicit-scope evidence.

The isolated decision/mission audit is reviewed in `bank_lifecycle_decision_audit_2026-10-07.md`.
It found no confirmed high-severity source lifecycle defect; its missing reserve hint, prepaid tooltip aliases and unexplained grace were repaired by the owner.
Its audit-mission inspection returned `DECISION_ANALYZED_PARTIAL`, revision `83de2533ecb8b860a1f1d60f5d74aef8488b85ce9e06e32d10581db327aa7858`, with 100 unresolved definitions and a truncated source inventory.
Two earlier action inspections returned `DECISION_SOURCE_STALE`, and current per-ID native evidence for the recap action and mission remains absent.
The probability audit remains pending final integration; no numerical before/after result is claimed.
Native UI/hover/mission scheduling, complete before/after probability and user-owned live evidence are not claimed by the source tests.
Center duration, real Public Works improvements, reserved/unspent regional accounting and inherited hidden/corridor/salvage consumers remain separate required work.

Skills used for this tranche are events, decisions/missions, subagents and shared Git commit; the existing asset-family contract constrains icon reuse.
