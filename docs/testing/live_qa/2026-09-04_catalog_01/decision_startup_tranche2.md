# Decision startup parser repair tranche 2

Status: implemented in the six parent-approved decision files after confirming the same diagnostics in `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_08/logs/error.log`.

## Scope and authority

This tranche covers only parser and reference repairs in Event 028, Event 031, Event 032, Event 035, and Event 039 decision sources. Event 025 category and GUI work, Event 029, Event 026, protected events 006, 012, 016, and 023, scripted effects, and non-decision sources remain outside this tranche.

No AI weights, probability values, thresholds, timers, effect values, mission nesting, or mechanic behavior were redesigned. Existing numeric values are retained; only invalid keys and unsupported constant placements were corrected.

## Immediate archives

Immediate pre-edit bytes are archived under `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_decisions_tranche2/` with the original relative paths.

| Source | Archive SHA-256 | Edited source SHA-256 |
| --- | --- | --- |
| `common/decisions/028_asteroid_incoming_decisions.txt` | `1DDD74DF0F7F3A40A6850E35E93901607514E36B3CEF0F33C73927E9CF63EFC7` | `35CC6F435CB2AE016D93C1BC9966923ACCF2B1D82166CDB147E37030C38B38D6` |
| `common/decisions/031_random_terror_decisions.txt` | `060B99B9AE9B4B6451490A0B1619CCA27F40DC4504A35D9A52DD94973E961920` | `E581C162306F487816AA86E95EA25934EDF3121274F6700E327635051277E0A0` |
| `common/decisions/032_missiles_decisions.txt` | `12A98D672830C1378B97167C4D2C0C518969C3833AACA74F7F5F9DB828F76CB3` | `FAF772392B482EE0309EF317259FF6DD2520D3EFA8A08F7415275841ACA2E99F` |
| `common/decisions/035_great_depression_decisions.txt` | `CD22130CB65E721A1CDF116A21DC5AD7831C4298046D9DA99EADF95075E21630` | `2CB7B2538E5329772320A858CE7E3B06B5065E858FD4506C6F96DC75AF77C185` |
| `common/decisions/categories/035_great_depression_categories.txt` | `4AB57DD4B3BD7C1B8B40F24F8A96A4E17F02DC2B2470B1A5D8E5088B65F65AB8` | `05470BB75EB34E4FA57A3203CD325A1C7C9372CA59CE999BE0F735F522C84274` |
| `common/decisions/039_murder_mystery_decisions.txt` | `7D6B51CA0089D67A28AACA0C7576E37D40FFD0A07DFD5DC8DDEB6323BB435D6E` | `9330430AD2C6F73F7BBB8A3F4C485A519E7EA8BC81A4DD07752CF643DE1CA84E` |

## Issue list by severity

1. Critical startup parser issues: invalid trigger and effect keys in decision-owned files were corrected so the engine can recognize the intended resource checks and experience debits.
2. High startup parser issues: malformed constant tokens in fields that reject `constant:` were replaced with file-local literals retaining values `1`, `25`, and `2`.
3. High decision registration issue: the invalid `desc` field was removed from the Event 035 category definition, leaving the category ID to provide its normal localisation lookup.
4. Medium reference issue: invalid `state_target = any_state` was changed to documented `state_target = any` in the three Event 028 rival-state decisions.
5. Medium reference issue: invalid Event 031 same-country checks were changed to `tag = ROOT` inside the existing `NOT` blocks, preserving the exclusion condition.

## Changed files and identifiers

- `common/decisions/028_asteroid_incoming_decisions.txt`: added `@asteroid_incoming_decision_civilian_factory_use = 1` and used it in all twelve `civilian_factory_use` modifier fields; changed the two `has_command_power` checks to `command_power`; changed `state_target = any_state` to `state_target = any` for `decision_asteroid_incoming_reconnoiter_crater_site`, `decision_asteroid_incoming_disrupt_extraction_routes`, and `decision_asteroid_incoming_prepare_crater_offensive`.
- `common/decisions/031_random_terror_decisions.txt`: changed the three `set_timed_country_flag` calls to `set_country_flag` blocks with the same flag names and `@` day values; changed seven `add_army_experience` effect keys to `army_experience`; changed fifteen `is_same_country = ROOT` checks to `tag = ROOT`; changed three partner-sponsor `political_power` checks to `has_political_power`.
- `common/decisions/032_missiles_decisions.txt`: changed nineteen `has_command_power` checks to `command_power` and changed the `add_air_experience` effect to `air_experience` at `missiles_improve_guidance_and_maintenance`; the concurrent Event 032 icon edits are preserved in full.
- `common/decisions/035_great_depression_decisions.txt`: added `@great_depression_ai_hint_pp_cost = 25` and changed all eleven `ai_hint_pp_cost` fields to that same-value local alias.
- `common/decisions/categories/035_great_depression_categories.txt`: removed only `desc = great_depression_category_desc`, which the launch log identified as an unexpected category token.
- `common/decisions/039_murder_mystery_decisions.txt`: added `@murder_mystery_objective_required_divisions = 2` and used it in the two objective `divisions_in_state` mission requirements.

## Before and after behavior

Before the repair, the engine rejected the named trigger/effect keys or malformed field tokens during startup and skipped or degraded the affected decision definitions. After the repair, each field uses the documented engine key or a parser-safe literal with the original comparison, amount, flag, duration, and threshold preserved.

The Event 031 flag changes retain timed behavior because `set_country_flag = { flag = ... days = ... }` is the documented timed-country-flag form. The Event 031 mission nesting in `common/decisions/031_random_terror_missions.txt` is untouched. The existing Event 028 dust `check_variable` repairs are untouched.

## Decision lifecycle notes

Event 028 keeps its existing recovery category, state targeting, cooldowns, completion effects, removal effects, and mission lifecycle; only parser aliases and the three state-target enum values changed. Event 031 keeps its existing government-response and actor-command categories, route gates, cooldowns, flag cleanup, and decision adapters; only parser aliases changed. Event 032 keeps its existing program phases, target/site gates, cooldowns, costs, scripted helper calls, and AI factors; only parser aliases changed. Event 035 keeps its existing category visibility and decision lifecycle; the category now omits the invalid `desc` key. Event 039 keeps its existing investigation and foreign-cell mission lifecycle; only the objective division threshold token changed.

## Cognitive-load and surface notes

The tranche changes no visible action count, active-mission cap, category density, player-facing meter, tooltip prose, or cost text. Existing category and mission surfaces therefore retain their prior action budgets and state presentation. The repaired fields restore availability and cost evaluation without introducing another visible value or an additional player choice. The values affected are internal gates or AI hints whose significance is already represented by the existing decision cost and requirement localisation.

## Mission quality notes

Event 028 owns five bounded recovery missions in its existing recovery category, with state or recovery-surface requirements, existing durations, success, cancellation, timeout, and cleanup effects; no mission file was changed. Event 031 owns the existing government and actor mission slots, with the parent runtime's three-slot contract and existing route, duration, success, failure, and cleanup behavior; mission nesting was preserved. Event 039 owns the existing objective missions, which retain their objective state requirement, existing duration, success, timeout, and cancellation paths; the required division count remains `2`. No duplicate mission lane or region-routing change was introduced.

## Cost, requirement, and AI notes

No spendable cost was added, removed, or numerically changed, and no decision exceeds the existing four-type cost contract in this parser tranche. Existing localisation and texticon coverage were not changed because no cost string changed. The Event 028 modifier fallback retains civilian factory use `1`; the Event 035 AI hint fallback retains political-power hint `25`; the Event 039 mission requirement retains division count `2`.

The Event 028 and Event 032 command checks now use documented `command_power` comparisons. Event 031 partner-sponsor checks now use documented `has_political_power` comparisons. The `tag = ROOT` substitutions preserve the existing same-country exclusion. AI weights and route factors were not changed, so no probability target or balance decision was introduced and no probability compare was required for this syntax-only tranche.

## Localisation, cleanup, and exploit notes

No player-facing localisation or tooltip key was added or renamed, so no localisation file was changed. Existing Event 035 category localisation is now resolved through the category ID after removal of the invalid `desc` field. Existing completion, timeout, cancellation, flag cleanup, and scripted adapter effects are unchanged, and no new exploit loop, free-resource path, or cooldown path was introduced.

## Validation and limits

The launch08 log confirms the source diagnostics at Event 028 lines 191-209, Event 031 lines 346-400, Event 032 lines 402-468, Event 035 category line 26 and decision lines 552-562, and Event 039 lines 563-564 before this patch.

Targeted post-edit scans report zero remaining `has_command_power`, `add_air_experience`, `set_timed_country_flag`, `add_army_experience`, `is_same_country`, malformed Event 028 civilian-factory constant, malformed Event 035 AI-hint constant, invalid Event 035 category `desc`, or malformed Event 039 division-threshold constant occurrences in the owned files. They report 13 Event 028 local-alias occurrences including its declaration, 15 Event 031 `tag = ROOT` checks, 19 Event 032 `command_power` checks, 12 Event 035 local-alias occurrences including its declaration, and 3 Event 039 local-alias occurrences including its declaration.

Byte-for-byte archive comparisons show only the listed source changes. The read-only Event 032 comparison against its immediate archive contains the parent's icon edits plus the nineteen command-key and one air-experience-key repairs, confirming that the parent edits were preserved.

The narrow pre-edit `hoi4.event_inspect` queries for `chaosx.nr28.1`, `chaosx.nr31.1`, `chaosx.nr32.1`, `chaosx.nr35.1`, and `chaosx.nr39.1` returned `EVENT_INSPECTED_PARTIAL` artifacts, with helper and lifecycle projections deferred under `MCP_INLINE_FILES_TRUNCATED`; these artifacts are event-linkage evidence only and are not a substitute for decision parser validation. No game process, live gameplay validation, staging, reset, or commit was run.

## Remaining issues and routing

The launch08 log still contains unrelated parent-owned errors in scripted effects, triggers, ideas, and other decision families. Event 029 remains deferred for its repeated constant and trigger issues, and Event 026 has no decision source file in `common/decisions`. Event 025 category registration and its existing scripted GUI remain deferred to the parent because the required GUI inspection previously found unresolved references, missing fonts, missing localisation, and a render timeout; this tranche made no GUI or category investigation changes.

No `docs/plans` file was needed. This handoff is the requested QA artifact at `docs/testing/live_qa/2026-09-04_catalog_01/decision_startup_tranche2.md`.

## Event 031 army-experience payment follow-up

The fresh parser review identified seven remaining unary `-constant:` values on repaired `army_experience` effects in `common/decisions/031_random_terror_decisions.txt`; this follow-up is limited to those payments.

Immediate pre-edit bytes are archived at `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event31_experience_payment/common/decisions/031_random_terror_decisions.txt` with SHA-256 `E581C162306F487816AA86E95EA25934EDF3121274F6700E327635051277E0A0`.

The seven edited decision identifiers are `random_terror_targeted_raid`, `random_terror_prepare_retake` at both existing payments, `random_terror_security_reform`, `random_terror_convert_militia` at both existing payments, and `random_terror_prepare_state_offensive`.

Each former unary payment now immediately assigns its existing positive `constant:random_terror_cost.<key>` value to the unscoped temp `random_terror_army_experience_payment`, multiplies that temp by the existing `constant:universal_cost_framework.negative_one`, and passes the temp to `army_experience`.

The installed `effects_documentation.md:2499-2505` identifies `army_experience` as a COUNTRY effect and `effects_documentation.md:5012-5024` documents `multiply_temp_variable` as multiplying a temp variable by a value or expression. Installed vanilla `common/decisions/WTT_politcal_power_struggle_decisions.txt:8036-8037` passes temp `reduce_xp_amount` to `army_experience`, confirming the variable-valued field. The existing `common/script_constants/chaosx_universal_cost_constants.txt:10-20` defines `universal_cost_framework.negative_one = -1`, and the repository precedent in `common/scripted_effects/006_independence_wave_decision_effects.txt:1327-1330` uses the same positive assignment, negative-one multiplication, and resource debit sequence.

The seven original debit magnitudes, comparison values, effect ordering, helper calls, and all other effects are preserved; no file-local fallback alias, weight, threshold, timer, gameplay process, staging, or commit was added.

The edited source SHA-256 is `FEC966EE89D9E468F46FD049EC67B9272EA0BC9CC2364D15F02CBAFF3C8C5933`. A no-index diff against the immediate archive contains exactly seven unary payment replacements and fourteen preparation lines. Targeted scans find seven temp assignments, seven negative-one multiplications, seven variable-valued `army_experience` effects, and zero remaining unary `-constant:random_terror_cost` payments for the named keys.

No broader negative-constant sweep was performed. The parent should review this single-file follow-up before the next launch checkpoint.
