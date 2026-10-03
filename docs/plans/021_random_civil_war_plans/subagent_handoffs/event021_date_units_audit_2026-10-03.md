# Event 021 date-unit audit, 2026-10-03

## Disposition and authority

Disposition: date-unit source review complete for the parent's working-tree patch and isolated proposed tree `c9b68609121636dc2cb678a2b40f04cda18edf75`, with MCP lifecycle validation and commit publication still unresolved.
The full Event 021 goal remains incomplete.
The report name retains the assigned 2026-10-03 date, with final evidence collection continuing into 2026-10-04 Europe/Kiev.

Authority is the parent's read-only assignment and subsequent explicit confirmation that it applied 41 date-duration writes, an ANY-scope conversion helper, schema-first integer calendar constants, and ceiling to the next engine hour.
Only this Markdown report is written by this auditor.
Gameplay, Git index, commits, launches, external-war repairs, source mechanics, and the unfinished three-helper ledger migration remain parent-owned.
No simplification or fallback implementation was made.

Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Observed HEAD before the parent's date commit: `b60528470e00464641edf2e99f591e1599d33a8a`, an unrelated elephant-model blocker commit.
This is not the requested date commit SHA.
The parent's isolated proposed tree has been verified in the addendum below.
The parent must record the actual date-only commit SHA after its final review and publication.

## Findings

The parent's five-file patch covers all 41 Event 021 raw date-plus-duration writes found by the audit: 13 base effects, 12 parent effects, three decision effects, 12 evidence effects, and one treaty fallback.
Every reviewed write has a contiguous `set_temp_variable = { event021_date_offset = <original day operand> }`, `event021_days_to_date_offset = yes`, and addition of the encoded output.
No additional Event 021 date arithmetic was found in the shared token consumers.
An early manual tally of 42 was corrected to the exact 41-site inventory below.

The helper's required output storage exists in the caller before helper entry.
It remains unscoped throughout the synchronous call, and each call consumes it immediately before another helper can overwrite it.
All eleven evidence types preserve `event021_evidence_duration`, both sponsor paths retain day inputs, and all three evolution stages preserve their MTTH values and existing clamps.
Only the copied offset is converted.
Native duration operands remain in days.

The whole-day conversion is `days * 24 / 100000`.
Fractional-hour durations use `ceil(days * 24) / 100000`.
The parent stores the unrounded hours privately, rounds the already caller-initialized output, increments it by one hour only when the rounded value is less than the original hours, then divides by 100000.
This gives exact offsets for integer days and a nonnegative delay of less than one game hour for positive fractional durations.
There is no whole-day rounding and no conversion of an absolute date.

The recurrence base remains the maximum of the current encoded date, recorded target cooldown, and successor grace.
Earliest and latest dates add independently converted 60- and 180-day offsets.
The copied recurrence review and next-review anchors remain encoded dates.
The post-window `constant:random_civil_war_value.one` is converted as one day, giving 0.00024 rather than one raw date unit.
The copied treaty hold date bypasses conversion, while the multiline fallback adds the converted 180-day duration.
Memory, reconstruction, sponsor, evidence, exposure, scenario-batch, same-tag, cluster reservation, strange incident, and all three evolution due dates are covered.

No Event 021 elapsed-date subtraction feeding a native `days =` field, mixed `num_days` arithmetic, or secondary multiplication/division of stored Event 021 dates was found.
Date comparisons, snapshot dates, log dates, treaty array dates, and plain receipt dates retain their encoded units.
The date-only patch adds no event target, persistent flag, persistent variable, GUI, map change, or periodic hook.

## Helper map and tuning

| Helper | Scope | Inputs | Output | Side effects | Consumers |
| --- | --- | --- | --- | --- | --- |
| `event021_days_to_date_offset` | ANY | Required caller-initialized temporary `event021_date_offset` in days | Same temporary variable containing the encoded hour-ceiled offset | Private temporary `event021_date_unrounded_hours` is overwritten, with no persistent state | All 41 writes listed below |

The helper lives in `common\scripted_effects\021_random_civil_war_date_effects.txt`.
Its matching contract is documented in `common\scripted_effects\021_random_civil_war_date_effects.md`.
The documentation explicitly states required caller-owned in/out storage, scope, output, rounding, private scratch state, original day-input preservation, copy-only absolute anchors, and a usage example.
No named argument or placeholder parameter API is introduced.

| Constant category | Schema | Key | Value | Meaning |
| --- | --- | --- | --- | --- |
| `event021_calendar` | `any_key = yes`, `data = int`, schema first | `hours_per_day` | 24 | Convert day durations to hours |
| `event021_calendar` | Same | `hours_per_date_unit` | 100000 | Convert hours to encoded offsets |
| `event021_calendar` | Same | `hour_step` | 1 | Advance a rounded-down fractional hour |

The constants live in `common\script_constants\021_random_civil_war_date_constants.txt`.
The original tuning file `common\script_constants\021_random_civil_war_constants.txt` retains SHA-256 `fba1dbb902f05e96c9926ffa5c21961cc671094abc74038c503d8cb516809bea` from the initial audit.
Existing duration bands and AI tuning are preserved, including review 15/30/60/90/120 days, recurrence 60/180 days, successor grace 45 days, target cooldown 365 days, memory and treaty holds 180 days, sponsor and mediation 90 days, scenario/cluster windows seven days, and evolution clamp 60-180 days.

## Event-target and cleanup plan

No new event target or persistent calendar state is required.
Existing country/global due-date ownership, treaty arrays, recurrence anchors, and cleanup hooks remain authoritative.
The output is immediate temporary storage and must be initialized before every call.
The private unrounded-hours scratch value is created and consumed inside the helper and is not a public return value.
No additional cleanup helper or date-repair world scan is introduced.
Existing exposure, sponsor, evidence, scenario, lifecycle, and achievement cleanup retain their named date fields and ownership.

## Migration and commit boundary

Migration replaces each raw duration addition with a seeded copied offset and the ANY helper, leaving the date base, day operand, flags, receipt identity, scope, eligibility, weights, clamps, and native timers unchanged.
The parent owns isolation of these date hunks from HEAD in mixed files and final commit publication.
The additional proposed-tree verification below proves source-level coverage of the same 41 changes in the named tree.
It does not prove the content of a later commit whose tree has not been compared with this tree.
Do not include unfinished ledger migration, external-war work, decision redesign, source rewrites, or unrelated changes merely because they share these files.
The exact dated commit remains pending.
The proposed-tree tests have been reproduced in the addendum below.

## Exact call-site map

Paths below are relative to `common\scripted_effects\`.
Before lines identify the initial mixed working-tree source read by this auditor.
Reviewed lines identify the parent-patched mixed working tree, not future isolated-commit line numbers.
Each write-block hash is SHA-256 of the UTF-8 bytes of the matched `add_to_variable` or `add_to_temp_variable` block from the command token through its closing brace, preserving internal line endings and excluding leading indentation.
The day operand is verified from the contiguous caller initialization.

### 021_random_civil_war_effects.txt

| Before line | Reviewed write line | Date destination | Preserved day input | Write-block SHA-256 |
| --- | --- | --- | --- | --- |
| 1253 | 1255 | `random_civil_war_exposure_cooldown_until` | `constant:random_civil_war_timing.exposure_cooldown_days` | `26f77b2ec77b81e34097d730f3495d1ef9c1b728e257a032f648e7e5d78cd1e5` |
| 1436 | 1440 | `random_civil_war_next_review_date` | `constant:random_civil_war_timing.critical_review_days` | `a1007ca4af5c1367ee263c4d82e0a4188e8f3ce9302ac10150920d2512927273` |
| 1441 | 1447 | `random_civil_war_next_review_date` | `constant:random_civil_war_timing.fractured_review_days` | `a1007ca4af5c1367ee263c4d82e0a4188e8f3ce9302ac10150920d2512927273` |
| 1446 | 1454 | `random_civil_war_next_review_date` | `constant:random_civil_war_timing.exposed_review_days` | `a1007ca4af5c1367ee263c4d82e0a4188e8f3ce9302ac10150920d2512927273` |
| 1451 | 1461 | `random_civil_war_next_review_date` | `constant:random_civil_war_timing.stable_review_days` | `a1007ca4af5c1367ee263c4d82e0a4188e8f3ce9302ac10150920d2512927273` |
| 1519 | 1531 | `random_civil_war_next_review_date` | `constant:random_civil_war_timing.initial_review_days` | `a1007ca4af5c1367ee263c4d82e0a4188e8f3ce9302ac10150920d2512927273` |
| 1809 | 1823 | `random_civil_war_reconstruction_until` | `constant:random_civil_war_timing.reconstruction_days` | `16b1e162b978a177d933614db1f54fe18140d937138494589695a721591f00f4` |
| 1812 | 1828 | `random_civil_war_successor_grace_until` | `constant:random_civil_war_timing.successor_grace_days` | `d1ea0814f63b1df1eb61e1f476d1447271fd5d274a30b314e9ce79bf9ebbc856` |
| 1894 | 1912 | `random_civil_war_recurrence_earliest_date` | `constant:random_civil_war_timing.recurrence_minimum_days` | `cc0c9e24d4f35461ec29234c185390dc37912370cd1ff6d665e675c48bacda23` |
| 1896 | 1916 | `random_civil_war_recurrence_latest_date` | `constant:random_civil_war_timing.recurrence_maximum_days` | `dc8156db5e66ff9347e7a7262c2190f6e1b74c44c58dd1fc2c818d2d6a66282d` |
| 2000 | 2022 | `random_civil_war_scenario_batch_deadline` | `constant:random_civil_war_timing.scenario_batch_maximum_days` | `974aa87160c18f523e23b45132dac086e00ebf02e4d7d429bf7b8e90cee96a91` |
| 2079 | 2103 | `random_civil_war_recent_target_until` | `constant:random_civil_war_timing.target_cooldown_days` | `030eb000f84b4323454bf4c5412a406035179d75d6ed336ae468889d8075f3a0` |
| 2082 | 2108 | `random_civil_war_memory_until` | `constant:random_civil_war_timing.event_memory_days` | `4081a7854218cba2724016c9951136278fa26d2b5ec1a560c84c8d56ffb77b64` |

### 021_random_civil_war_parent_effects.txt

| Before line | Reviewed write line | Date destination | Preserved day input | Write-block SHA-256 |
| --- | --- | --- | --- | --- |
| 351 | 353 | `event021_cluster_reservation_expiry` | `constant:event021_parent_tuning.cluster_reservation_valid_days` | `fd53a5159862ee5bd69a9c679a11aa7bb01497835e6b12dd499e5d623354164f` |
| 690 | 694 | `global.random_civil_war_evolution_i_due_date` | `event021_evolution_delay_days` | `c5ce9f938b2fc9f6df13b1b008db97dc1e9f6f0a1687f805dcb4ed91121fc480` |
| 701 | 707 | `global.random_civil_war_evolution_ii_due_date` | `event021_evolution_delay_days` | `d6a3990d5804e8ebd9f31f528572c1a436ba010e96beb6d6d45ef9f6049b288f` |
| 712 | 720 | `global.random_civil_war_evolution_iii_due_date` | `event021_evolution_delay_days` | `44b4613a8800996d718f65be843c7f6a75e6d6b4435a4f27a378dd91b11dd6a7` |
| 918 | 928 | `random_civil_war_next_review_date` | `constant:random_civil_war_timing.stable_review_days` | `a1007ca4af5c1367ee263c4d82e0a4188e8f3ce9302ac10150920d2512927273` |
| 928 | 940 | `random_civil_war_next_review_date` | `constant:random_civil_war_value.one` | `a1007ca4af5c1367ee263c4d82e0a4188e8f3ce9302ac10150920d2512927273` |
| 5492 | 5506 | `random_civil_war_same_tag_deadline` | `constant:event021_parent_tuning.same_tag_deadline_days` | `fbdb2a4a17013776e5bf42390ac94f0203523d945f8290243730783402dc65a7` |
| 5820 | 5836 | `random_civil_war_successor_grace_until` | `constant:random_civil_war_timing.successor_grace_days` | `d1ea0814f63b1df1eb61e1f476d1447271fd5d274a30b314e9ce79bf9ebbc856` |
| 6546 | 6564 | `random_civil_war_settlement_terms_hold_until` | `constant:event021_parent_tuning.settlement_terms_hold_days` | `66ed70350a7613987da35a4d31d9840ad438473746c4e7e26bf8926b16cce59f` |
| 6618 | 6638 | `random_civil_war_settlement_terms_hold_until` | `constant:event021_parent_tuning.settlement_terms_hold_days` | `66ed70350a7613987da35a4d31d9840ad438473746c4e7e26bf8926b16cce59f` |
| 8187 | 8209 | `random_civil_war_strange_incident_until` | `constant:random_civil_war_timing.exposure_cooldown_days` | `949e6fffb54d1c3a170ffbbdd1a23ec28256597b1a1868a9c2d959f2bcf58894` |
| 8318 | 8342 | `random_civil_war_next_review_date` | `constant:random_civil_war_timing.stable_review_days` | `a1007ca4af5c1367ee263c4d82e0a4188e8f3ce9302ac10150920d2512927273` |

### 021_random_civil_war_decision_effects.txt

| Before line | Reviewed write line | Date destination | Preserved day input | Write-block SHA-256 |
| --- | --- | --- | --- | --- |
| 121 | 123 | `event021_settlement_deadline` | `constant:event021_action_tuning.settlement_obligation_days` | `4e2cdda02882b759bd21c253679aba55ccac4c22a2b57b30442383794ddc64b7` |
| 281 | 285 | `random_civil_war_sponsor_commitment_until` | `constant:event021_action_tuning.sponsor_commitment_days` | `d7f839e3ce2f34ce7eaf83ace16d3bb0cbe067eef314fa5525a13d22896217ff` |
| 384 | 390 | `event021_mediation_until` | `constant:event021_action_tuning.mediation_days` | `617aba1434a20ae5dbfb006a921b11814d58d8e3cd742b812c0244c65fe98117` |

### 021_random_civil_war_evidence_effects.txt

| Before line | Reviewed write line | Date destination | Preserved day input | Write-block SHA-256 |
| --- | --- | --- | --- | --- |
| 61 | 63 | `random_civil_war_ideological_evidence_until` | `event021_evidence_duration` | `481b8524c9d852a0f8eaba1a4d1b5f904e3fde215d5cafadaef25c4d93d5ef77` |
| 75 | 79 | `random_civil_war_legal_evidence_until` | `event021_evidence_duration` | `44132e7a12b4c906281ba5ed5d51dfb6223ba95f86659658a3df32a3c17ff0ae` |
| 89 | 95 | `random_civil_war_regional_evidence_until` | `event021_evidence_duration` | `23536bbe360329885f5a4d6c10325f80cb2c5f76dbf482a9c025064661eb4583` |
| 103 | 111 | `random_civil_war_command_evidence_until` | `event021_evidence_duration` | `ab5630622b552a8ba049dea4cd1d4e2f528130864ba64673c1b665e57c391e30` |
| 117 | 127 | `random_civil_war_event6_evidence_until` | `event021_evidence_duration` | `5c4d91180bd748ea276f64e0a59c19c155a80004eb022c75a463581475f8f57f` |
| 131 | 143 | `random_civil_war_same_tag_evidence_until` | `event021_evidence_duration` | `3b01febd6d901dad639ee3de90e52ca10002df252e8ab6d8a5747a171417d482` |
| 145 | 159 | `random_civil_war_external_war_evidence_until` | `event021_evidence_duration` | `a5d596db0ef157dd2de6460aa85f2eed3e74944811cd8724fb2534c42fd67760` |
| 159 | 175 | `random_civil_war_fury_evidence_until` | `event021_evidence_duration` | `caa50f8b0e707605e0a5afb7ff7d581e539218fb640f4dcdb1cdaa13ab75a794` |
| 173 | 191 | `random_civil_war_neighbor_evidence_until` | `event021_evidence_duration` | `5d4bf7beab317c8810d2881e4aa8e0f60d7243614b474a72e2bfbc3b03c9ce68` |
| 187 | 207 | `random_civil_war_sponsor_evidence_until` | `event021_evidence_duration` | `084ae131d2ad0b20ba6491aea52d72bb93b2741c1e63d3d30abee4e145b79a67` |
| 201 | 223 | `random_civil_war_settlement_evidence_until` | `event021_evidence_duration` | `978493422227041f6a2072e9f152a2984ec4cd647e813b6c0343750deb651e23` |
| 454 | 481 | `random_civil_war_sponsor_commitment_until` | `event021_sponsor_duration` | `d7f839e3ce2f34ce7eaf83ace16d3bb0cbe067eef314fa5525a13d22896217ff` |

### 021_random_civil_war_treaty_effects.txt

| Before line | Reviewed write line | Date destination | Preserved day input | Write-block SHA-256 |
| --- | --- | --- | --- | --- |
| 468 | 470 | `event021_treaty_capture_hold_until` | `constant:event021_parent_tuning.settlement_terms_hold_days` | `fcc24b3559b0f9774342893c26d00ebb98455d30ff77f00c7a65605e01e35b7c` |

## Source hashes

These are physical-file hashes and can differ from future normalized Git blobs.
The parent must retain commit evidence separately.

| Source | Before physical SHA-256 | Reviewed physical SHA-256 |
| --- | --- | --- |
| `common\scripted_effects\021_random_civil_war_effects.txt` | `6d9077920f2045783ffbcac00dd20f6b3e403a3070e7e7608f13da41bc0052d7` | `a873d692692652eac90e01ef318ad692200f596f3dedda6254ece8ba80384551` |
| `common\scripted_effects\021_random_civil_war_parent_effects.txt` | `0dbd60bf8259f6848413f84db79f988d6d29cabb26fa09c283066a7a03e1df61` | `01b4676c83150de2d452566dddc28335959c8e30e815caefb81a5e183197794e` |
| `common\scripted_effects\021_random_civil_war_decision_effects.txt` | `653d04b02509fd090e5faf395be489539b912e4be0b929c1b694a7f4b6c63065` | `ca75f251e65d75b637210d9c8222bd08c59b61140fa64874aec60bc560619de1` |
| `common\scripted_effects\021_random_civil_war_evidence_effects.txt` | `b475df038a5adc2a12f5c129585042d6fe099f3be3b9faece80bdbbc9bd4e7ef` | `5544d7879311a8dfca576ba3c0b7a86075bb346de4f4b4e0da8e0d4a5de0ead0` |
| `common\scripted_effects\021_random_civil_war_treaty_effects.txt` | `5ce92d287ada7770e59c1763cc63a4fa35a60e5e6b4b09ebf63a35b121f2b027` | `a565bf3cd7c1345b7e06c98b4a4bcd366e14d04ccd3e6e6409e2e07b8dfee8d2` |

| `common\scripted_effects\021_random_civil_war_date_effects.txt` | New parent file | `863e1d0b51de7de141067f8982a6cb156530c42025002dd67495fa8c1fb019f0` |
| `common\script_constants\021_random_civil_war_date_constants.txt` | New parent file | `195dc390ce1cbd5c081743aee6820e6a2e8e56906e8d72cac080b94edb00a80b` |
| `common\scripted_effects\021_random_civil_war_date_effects.md` | New parent file | `72798b46b179340d4fa4441d7d4effb05bde6ea6b65f1d081dc618f8dce8478f` |
| `common\mtth\021_random_civil_war_mtth.txt` | `7982f0768b8ed04ae7154bcff8cbdac33589f8f7b031cfe12353f625891881c1` | Same, also matching the immutable date-audit before snapshot |

## Coverage inventory

The audit searched all Event 021 runtime files and all runtime files matching `event021`, `random_civil_war`, or `chaosx.nr21.` under `common`, `events`, `localisation`, and `interface`.
The final token inventory contains 62 files, including the two new parent-owned script files.
Arithmetic scans used multiline blocks rather than line-only searches and were followed by explicit source reads of writers, copied anchors, input preparation, comparisons, and cleanup.
The seven other raw date writes encountered in shared-token files belonged to Event 031 or Event 035, and were not substituted into the Event 021 count or patched.

```text
common\achievements\chaos_redux_achievements.txt
common\ai_strategy\021_random_civil_war_ai_strategy.txt
common\decisions\021_random_civil_war_decisions.txt
common\decisions\categories\021_random_civil_war_categories.txt
common\ideas\021_random_civil_war_cxt_extension_ideas.txt
common\ideas\021_random_civil_war_ideas.txt
common\mtth\021_random_civil_war_mtth.txt
common\on_actions\021_random_civil_war_cxt_on_actions.txt
common\on_actions\chaosx_on_actions_chaos_meter.txt
common\script_constants\021_random_civil_war_constants.txt
common\script_constants\021_random_civil_war_date_constants.txt
common\script_constants\chaosx_triggerable_scenarios_constants.txt
common\script_constants\event_cluster_constants.txt
common\scripted_effects\006_independence_wave_effects.txt
common\scripted_effects\006_independence_wave_event021_adapter_registry_effects.txt
common\scripted_effects\006_independence_wave_formable_registry_effects.txt
common\scripted_effects\021_random_civil_war_achievement_effects.txt
common\scripted_effects\021_random_civil_war_active_evolution_effects.txt
common\scripted_effects\021_random_civil_war_cxt_test_effects.txt
common\scripted_effects\021_random_civil_war_date_effects.txt
common\scripted_effects\021_random_civil_war_decision_effects.txt
common\scripted_effects\021_random_civil_war_dynamic_front_candidate_effects.txt
common\scripted_effects\021_random_civil_war_effects.txt
common\scripted_effects\021_random_civil_war_evidence_effects.txt
common\scripted_effects\021_random_civil_war_evolution_log_effects.txt
common\scripted_effects\021_random_civil_war_external_war_effects.txt
common\scripted_effects\021_random_civil_war_front_ledger_effects.txt
common\scripted_effects\021_random_civil_war_lifecycle_effects.txt
common\scripted_effects\021_random_civil_war_parent_effects.txt
common\scripted_effects\021_random_civil_war_successor_effects.txt
common\scripted_effects\021_random_civil_war_treaty_effects.txt
common\scripted_effects\031_random_terror_effects.txt
common\scripted_effects\035_great_depression_effects.txt
common\scripted_effects\035_great_depression_external_adapters.txt
common\scripted_effects\chaosx_event_cluster_effects.txt
common\scripted_effects\chaosx_logic_effects.txt
common\scripted_effects\chaosx_settings_effects.txt
common\scripted_effects\chaosx_triggerable_scenarios_effects.txt
common\scripted_localisation\021_random_civil_war_localisation.txt
common\scripted_localisation\chaosx_scripted_localisation_scenarios.txt
common\scripted_triggers\006_independence_wave_event021_adapter_registry_triggers.txt
common\scripted_triggers\006_independence_wave_force_package_mapping_triggers.txt
common\scripted_triggers\006_independence_wave_triggers.txt
common\scripted_triggers\021_random_civil_war_evidence_triggers.txt
common\scripted_triggers\021_random_civil_war_external_war_triggers.txt
common\scripted_triggers\021_random_civil_war_lifecycle_triggers.txt
common\scripted_triggers\021_random_civil_war_parent_triggers.txt
common\scripted_triggers\021_random_civil_war_sponsor_receipt_triggers.txt
common\scripted_triggers\021_random_civil_war_successor_triggers.txt
common\scripted_triggers\021_random_civil_war_treaty_triggers.txt
common\scripted_triggers\021_random_civil_war_triggers.txt
common\scripted_triggers\035_great_depression_decision_surface_triggers.txt
common\scripted_triggers\chaosx_settings_triggers.txt
common\scripted_triggers\chaosx_triggerable_scenarios_triggers.txt
common\scripted_triggers\individual_crisis_targeting_triggers.txt
common\synchronized_dynamic_tokens\chaosx_tokens.txt
events\021_random_civil_war.txt
events\021_random_civil_war_external_war_events.txt
interface\021_random_civil_war.gfx
localisation\english\021_random_civil_war_external_war_l_english.yml
localisation\english\021_random_civil_war_l_english.yml
localisation\english\021_random_civil_war_requirement_flags_l_english.yml
```

## Reference evidence

The four required live routes are exposed: `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`.
Event reference context returned no missing or omitted required source kinds.
The offline wiki was consulted without web access.
Only relevant cited sections were read.

| Source | Read lines | Revision SHA-256 | Rule |
| --- | --- | --- | --- |
| Repository `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 1464-1475, with the date rule at 1469 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | One game hour is 0.00001 date, and `num_days` uses separate day units |
| Same wiki | 425-434 | Same | Variable precision is 0.00001, with finer precision truncated |
| Same wiki | 435-443 | Same | Caller-preinitialized temporary variables survive helper modifications and are unscoped |
| Installed `documentation\dynamic_variables_documentation.md` | 977-979 and 996-998 | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` | Comparable/localizable `date` versus total-day `num_days` |
| Installed `documentation\script_concept_documentation.md` | 216-222 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` | Shared constants and `constant:` variable access |
| Installed `common\script_constants\documentation.md` | 1-34 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` | Mandatory first schema and integer/fixed-point kinds |
| Installed `documentation\effects_documentation.md` | 3587-3594, 5012-5018, 6476-6485 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | ANY-scope divide, multiply, and round temporary-variable effects |
| Installed `documentation\triggers_documentation.md` | 2110-2135 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` | ANY-scope variable-to-variable comparison |

Installed paths are rooted at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`.
Vanilla `events\BFTB_Bulgaria.txt`, event `bftb_bulgaria_tsar_boris.2` at lines 2182-2203, records `BUL_date_of_tsars_death = global.date` at line 2199.
Its physical SHA-256 is `d2740d3716de01b81aef29c95527d974dedebfac3a1571695955815115387d88`.
This is a native absolute-date storage precedent, not a native day-conversion example.
The existing Event 013 conversion at `common\scripted_effects\013_natural_disasters_effects.txt`, lines 1720-1749, supplies the exact 24/100000 repository precedent.
The user-provided Event 013 live QA at 2026-10-03 20:00 establishes the hour-unit observation in the parent prompt, not a new live test by this auditor.

Live source lookup found `event021_parent_schedule_evolution_due_date` at baseline parent lines 679-714 with indexed revision `6dbb25e09bfb18bf0d58d3c7e1f0a55c5bd85052fa8d04af7ba65d92e754447f`.
Its bounded inline text stopped at line 704 with a continuation, and the local underlying definition was read through line 714.
Its reference projection was incomplete, with `referencesComplete = false` and 18450 unresolved references.
No consumer coverage is inferred from its empty reference list.
The exposed source-lookup schema lacks `view` and `keyPath`, so the newer child-structure route was not invented.

## Meaningful validation and limitations

All 41 call sites were matched as contiguous initialize/call/add sequences, preserving the original day operand separately.
The multiline treaty fallback and the one-day recurrence boundary were independently read.
The shared-token arithmetic pass found no additional Event 021 writer.
All eight native `days =` occurrences in the five effect files, plus three native day-duration occurrences in the decision file, match HEAD's operands.
The MTTH file is byte-identical to the immutable parent snapshot under `docs\plans\021_random_civil_war_plans\probability_snapshots\event021_date_units_before_2026-10-03\`.
The original tuning-file hash also matches the initial read.
These source checks establish operand preservation, not native execution.

The arithmetic model gives one day = 0.00024, seven days = 0.00168, 30 days = 0.00720, 45 days = 0.01080, 90 days = 0.02160, 180 days = 0.04320, and 365 days = 0.08760.
A 90.01-day input becomes 2161 hours and 0.02161, avoiding the early 2160-hour expiry.
A positive 0.00001-day input becomes one engine hour.
Zero remains zero.
This is mathematical inspection of the production helper structure, not a mocked engine or live-game test.

MCP `event_inspect(mode = state_flow, selector = { kind = event, eventId = chaosx.nr21.1 })` timed out after 600 seconds.
The narrower trace completed with `EVENT_INSPECTED_PARTIAL`, `analysisMode = focused`, helpers = 0, and revision `828ca59a9a1fa1a44d0bf5a12bce75e5cb65e717d2d055388d5ac1994d71fe92`.
Its source inventory was truncated inline to 64 of 388 paths, and whole-workspace helper/lifecycle analysis was deferred.
Artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b98b7e4b397d5801165c0174c4c86a36f67653a079bb3f181bfe2350a369297/6c86e69a58f6e4b7fb8d15b1c9f2c2f1b0b45fa3f115984e37c91aa84ccb5faf/event-trace-828ca59a9a1f.json`.

The matching timing render completed with `EVENT_RENDERED_PARTIAL` at the same revision, `analysisMode = focused`, helpers = 0, selectedNodes = 0, and omittedNodes = 42987.
It does not establish Event 021 coverage despite tool-level status `ok`.
Timing data artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/029c53bb4181cab2db33d9fde1c6653491911f01950f39b201e12eba98326dcc/0464d2413bf7daf1f22925d91bd1dbc55eb6a0b1ced7d5a305f6f080ec1dbd45/event-timing-828ca59a9a1f.json`.
Manifest artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/093c97fc26f53ca6167d8652399aec68ab6ea80decb9228200ed5ca1266d34b3/e6242775348d722ce4d01b9f88ebcf283e19421834d5a7c1dc4d635e0964b8b7/event-timing-828ca59a9a1f-manifest.json`.
The large linked trace and render inventories were not read in full, and are retained as unresolved evidence rather than claimed coverage.

Decision inventory completed with `DECISION_ANALYZED_PARTIAL`, `complete = false`, zero scenarios, 218 unresolved definitions, and source revision `51a33aa6f3b9de50e482914dd25c25f06466c45b93e9ac269be2abb7fe8d79f1`.
It is not a timing scenario validation.
Artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4745eb99cab88a8ff1f601e5fdc72bec10df4086526871c3629bf9879daadf2/4ab56ecace7eb54ecf1bd26abcb3f0cec530f2e82f32df24fadee25ac440e28c/decision-9c86a6448001aa18f38f572b.json`.

The connected tool list does not expose `hoi4.script_validate`.
No helper-expansion job or native task route was used without the required health/version/client-negotiation evidence.
Event comparison was not fabricated from partial reports or by comparing the current source with itself.
A graph-bearing before/after comparison and task-specific native scenario evidence remain unresolved.

The read-only `chaosx_ai_probability_auditor` sidecar was routed with no inherited context, no file-write authority, exact immutable snapshot paths, and the calendar correction.
Its agent ID is `01a10386-c934-7491-89ca-5b9eff64c87c`.
Its final inline audit was received and is recorded below.
The specialized comparison remains unresolved and is not replaced by byte-preservation checks.
No AI balance target was selected.

### Received specialized probability evidence

The auditor independently confirmed the 3123-byte MTTH source equals the immutable before snapshot at SHA-256 `7982f0768b8ed04ae7154bcff8cbdac33589f8f7b031cfe12353f625891881c1`.
It confirmed all three current scheduling branches preserve their MTTH day inputs and 60-180 day clamps before conversion, with base days 90, 135, and 120.
It also confirmed the strange-incident two-entry boundary and its existing 0.08 and 0.92 weight constants at original constants lines 676-677.
These are source-preservation observations, not calculated campaign probabilities or timing outputs.

`hoi4.probability_inspect` for the scripted MTTH file under `event_mean_time_to_happen` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, zero candidates, and no available adapters.
Reported MCP revision: `b6e311732ed990bb5c2708b59e129c0c5cc9e6dbd054c1a2d52c43e6bae266ab`.
Reported MCP source hash: `090fc4c0e32cde8b8b04c1f4e7b92e74179b4e17ded2ad7f10450cc05fd6e102`.
Artifact URI, preserved verbatim from the auditor:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d796973b8e36e999ff91c401305164b15dd3c6ee51ea74f0b6a235a7cbcd3bbe/e1e39c3f7640dc8f4b085fe8f4c8001d38f2bc58397173f2c72b9b6c5bfdc443/probability-inspect-090cf4c0e32c.json`.
The installed adapter did not classify these scripted MTTH entries.

`hoi4.probability_inspect` for the parent-effects file under `random_list` found eight file-wide candidates, `poolComplete = false`, eight required dynamic weight inputs, and one unresolved finding.
Reported MCP revision: `36ff793e3dd6e687f72b5f97424274614a7bdc10b2ff88ef1d659ceccfa4010b`.
Reported MCP source hash: `cb249fcbbc39d58c38f7416c3c39cee3f2f921758ebe9ef8966e33ed52ced810`.
Artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd218750b03a676a2e339e2fa67262288e241f63d3715351a98f1e1d9bc0b672/9e498659f9e895c5c01a22eade0f603daad79ea3d17ea11ec1c4ee5e0bff0cf9/probability-inspect-cb249fcbbc39.json`.
An attempted parent-effects inspection under the MTTH adapter returned no candidates for that adapter and suggested `random_list`, exposing the incident entries among the file-wide candidates.
Its artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80bfe3c8cc39bfdd3495823c903895c828dfd49620f1bcf7ed759be7cc06d4b3/bcfa5f11fce351287b5d2e815d4d573ab0f110664a093b19b09b354117417b5e/probability-inspect-cb249fcbbc39.json`.
The narrower two-incident-candidate inspection was terminated after about 87 seconds without a result or artifact.
Reading an inspect artifact body returned `Artifact provenance manifest is unavailable`.
The reported MCP source hashes are retained separately from the physical-file SHA-256 values, and their byte identity is not asserted.

No evaluation, sweep, comparison, or probability render produced scenario evidence.
There are no named scenario IDs or scenario hashes from the sidecar.
The exact blocker is unclassified scripted MTTH plus an incomplete random-list pool, an unanswered narrow inspection, and unavailable artifact provenance.
The mandatory before/after probability comparison remains unresolved pending the parent's isolated date-only proposed tree and a supported complete scenario/pool route.
The auditor selected no balance targets, normalized no incomplete pool, and wrote no files.

## Completed, pending, and blocked work

Completed by this auditor: required guidance reads, offline and installed reference reads, initial date defect inventory, parent-patch inspection of all 41 writes, caller-storage review, ceiling review, native-day and MTTH preservation checks, shared-consumer scan, exact source/site hash map, and this one report.
Parent implementation reviewed: five changed effect files, one new helper, one new calendar-constant file, and one matching helper-documentation file.
Auditor gameplay files changed: none.
Auditor commits and Git-index writes: none.

Pending with parent: final commit-content review and publication, actual date-fix commit SHA, and review of this handoff.
Blocked/unresolved evidence: full event state-flow timeout, zero-selected-node focused render, incomplete decision/scenario evidence, unexposed script validator, unclassified scripted MTTH, incomplete probability pool, and unavailable probability-artifact provenance.
The specialized auditor has returned, and its required before/after probability comparison remains unresolved for the reasons recorded above.
The existing ledger, external-war, source, and broader Event 021 work is outside this bounded audit and remains incomplete.

## Isolated proposed-tree verification, 2026-10-04

Verified proposed object: `c9b68609121636dc2cb678a2b40f04cda18edf75`.
`git cat-file -t` identifies it as a tree, not a commit.
Verified base: `b60528470e00464641edf2e99f591e1599d33a8a`.
The base-to-tree diff contains exactly nine paths: the five date effect files already listed, `.tools/test_event021_date_units.py`, and the three helper/constants/documentation files.
No ledger helper, external-war source, original tuning file, MTTH file, or eligibility trigger is included in that diff.
The existing metadata-test dependency `.tools/test_event021_evolution_log.py`, original MTTH, and original tuning file have identical Git blobs in the base and proposed tree.

Using the existing project parser, each proposed initialize/helper/add triple was semantically reversed to its original add-with-day-operand operation.
For all five complete effect files, that reversed AST equals the base AST exactly, preserving node order, repeated keys, nested blocks, eligibility, clamps, native timers, and every unrelated operation.
This establishes that the five source changes contain only the 41 intended date transformations at the parser's scope.
The project parser is a source tokenizer and nested-block model, not the Clausewitz engine.
Comments and whitespace are excluded from AST equality.

The operation kind, date destination, original day input, and nearest same-block date anchor of all 41 proposed transformations match the reviewed working-tree transformations as multisets.
The treaty fallback and cluster reservation inherit some date initialization from surrounding blocks, and exact inverse-AST equality independently proves those surrounding blocks remain unchanged from the base.
The changed working-tree helper ownership from unfinished work is not required by the isolated transformation.

The helper has exactly one definition under proposed `common/scripted_effects`.
Its three referenced `event021_calendar` keys resolve in the same proposed tree, with schema first and integer values 24, 100000, and 1.
The proposed helper, calendar constants, and matching documentation are byte-identical to the earlier reviewed parent files.
No unfinished ledger file is needed for the date helper's dependency closure.

The six calendar tests and twelve metadata tests were reproduced from the proposed tree's test-module blobs in memory, with `CHAOSX_EVENT021_TEST_REVISION` set to the exact proposed tree and `CHAOSX_EVENT021_DATE_BASELINE` set to the exact base.
All 18 passed.
Their production-source loads used `git show` for that tree, rather than the mixed working tree.
Python bytecode writing was disabled, and no checkout, temporary source file, index operation, or gameplay write was performed.
The calendar tests cover fractional-hour ceilings, exact integer-day offsets, caller-storage lifetime, all 41 AST write sites, and native-day/MTTH preservation.
The metadata tests exercise the existing bounded selector and sponsor-receipt source models.
They do not establish native execution or resolve the earlier MCP probability and lifecycle gaps.

### Proposed-tree date write lines and blob identities

These line offsets supersede working-tree offsets only for the named proposed tree.
The original 41-row map above still records the independently reviewed working-tree evidence.
All effect filenames below have prefix `common/scripted_effects/021_random_civil_war_`.

| File suffix | Date sites | Proposed write lines | SHA-256 of raw proposed Git blob |
| --- | --- | --- | --- |
| `effects.txt` | 13 | 1242, 1427, 1434, 1441, 1448, 1506, 1798, 1803, 1887, 1891, 1997, 2077, 2082 | `25f4f988b434384a8e4ecea33033fd7dd65e0c87122bc73be38c295d12976810` |
| `parent_effects.txt` | 12 | 308, 601, 614, 627, 835, 847, 4578, 4908, 5485, 5559, 7039, 7172 | `078bcd1fcafd0caf3fa12a5f152de003909a5ab2527f8ed6032aa4915ece8048` |
| `decision_effects.txt` | 3 | 123, 285, 390 | `77fb6b14691aafb58e78b7ba6d93ee4761e3c474d638cb2b6001b8d9546288a8` |
| `evidence_effects.txt` | 12 | 63, 79, 95, 111, 127, 143, 159, 175, 191, 207, 223, 476 | `1b56eb6095a3e6a76258c6f1b312d5fd84746d278dd59183330d03f9bb099bb2` |
| `treaty_effects.txt` | 1 | 470 | `817f007d4c4fcdcc2ab14ac47fe3a3d1e873328fd30799358aeaaabba025538f` |

The three helper/constants/documentation blob hashes are unchanged from their physical-file hashes recorded above.
The new test blob has SHA-256 `7083fb7c101af0d8abb08c1ffde7ddff2ae81ecce44d098377131213d4b988ef`.
This proposed-tree addendum is the only additional file edit by this auditor.
There are no simplifications, additional gameplay changes, or new completion claims.
The source-level isolated-tree dependency and date-field review is complete, with final parent review and commit publication pending.
