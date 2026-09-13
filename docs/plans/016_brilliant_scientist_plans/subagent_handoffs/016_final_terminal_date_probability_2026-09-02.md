# Event 016 terminal-date qualification score baseline

Date: 2026-09-02

Status: prepatch deterministic-score baseline secured, read-only, source-only and unresolved at MCP engine level. No gameplay, score constant, AI weight, configuration, localisation, or runtime file was edited. No completion or acceptance claim is made.

## Scope

The audited surface is `brilliant_scientist_calculate_defeat_qualification_score` in `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt`.

The parent-proposed mechanical correction is limited to elapsed active-day accounting. It will read actual `global.num_days`, initialize zero when no valid start exists, accumulate completed active intervals without counting inactive gaps, and add the current open interval. The duration thresholds and score constants remain unchanged.

The current effect also evaluates major-power, opponent, project-family, weaponization, singularity, territorial, and industrial components. Every non-duration component is zero or absent in the retained fixture so the date boundary cases remain isolated.

## Source retention and references

The retained prepatch source point is HEAD `957ae81cc6539c2e29beebe92f4c6523eea91532`.

| Surface | Path | HEAD blob | Current raw SHA-256 |
| --- | --- | --- | --- |
| Qualification scorer | `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` | `0d62467db51976f213f5dcc8826e09a1e39ce545` | `8d0e861c8e7afcd9e7032e4ebb207c5e1700cb8570cf2233286c0e103387bcbc` |
| Duration thresholds and score values | `common/script_constants/016_brilliant_scientist_super_event_constants.txt` | `ec4d650b74104132b73c4a342047b208b94dead6` | `b69b37e578dc19bb1842ef8ed46c4eacc1e694e01949a6ce96550f8214392a32` |
| Readiness helper context | `common/scripted_triggers/016_brilliant_scientist_super_event_triggers.txt` | `c8365095a7ce68f3853c0603a0a253cd42af3481` | `a946570099f786b9ba4b606b5de1a94b67e7b33817ad0820d6188d7791b5b4ed` |
| Super-event callers | `events/016_brilliant_scientist_super_events.txt` | `bb8b52742c7322331dc1427aa288e0d33f0246da` | `9d818531b8f3813ecad0c3bfea12ab2ccc9fae38e09898f68f01f255e488ffda` |

The current effect and constants have no semantic diff from retained HEAD in the captured workspace. Their raw hashes differ because of working-tree line-ending representation and concurrent source bookkeeping. The parent separately owns a non-score local/regional defeat guard in the same effect file, so that guard is not attributed to the date-score baseline.

The current scorer is at `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt:400-419`.

The readiness trigger is `brilliant_scientist_qualifying_defeat_is_ready` at `common/scripted_triggers/016_brilliant_scientist_super_event_triggers.txt:128-138`.

The source constants are at `common/script_constants/016_brilliant_scientist_super_event_constants.txt:100-139`:

- `duration_short_days = 180`, `duration_long_days = 365`, and `duration_epic_days = 730`.
- `duration_short = 2`, `duration_long = 2`, and `duration_epic = 2`.
- The scorer uses three independent threshold checks, so the intended duration contribution is 0 below 180, 2 from 180 through 364, 4 from 365 through 729, and 6 at 730 or above.
- `minimum_score = 12` and `regional_minimum_score = 6` are unchanged context thresholds and are not selection probabilities.

The relevant offline and vanilla references were consulted. Vanilla `documentation/dynamic_variables_documentation.md:977-997` defines `global.date` as a comparable date value and `global.num_days` as current total days. Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:959-960` documents encoded date values and the day-count variable. Vanilla `documentation/effects_documentation.md:7888-7907` and `:8203-8215` document `set_variable` and `subtract_from_variable` arithmetic. The terminal review identifies the same defect at `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_terminal_current_review_2026-09-02.md:86-107`.

## Mandatory MCP inspection

The mandatory first weighted-surface call was `hoi4.probability_inspect` on `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` with source refresh. It returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, zero candidates, zero unresolved items, and no available adapters.

Inspection artifact: [probability-inspect-c76118a037e4.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1dce01876f2fae8d3a5b27595b514f28a9c35a6d63e43c3dcec8720a9d191410/89f8a604c940389565784367721cb17c152ef7a01d58386a2dfa982d72aeba1c/probability-inspect-c76118a037e4.json).

The inspect reports normalized source hash `c76118a037e45ce9b0b32a761c9a6c21a6c5420f522b8be07f33cbf260f1c30c` and source revision `05ceab21359d08b9daebe041f7d48c873190059743dd45090a759dae1e1e1e7e` for the current source projection. No custom-score, direct-random, random-list, MTTH, or AI-selection adapter can execute this scripted effect through the installed probability service.

Because the surface is deterministic scripted arithmetic rather than a weighted candidate pool, `probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_render`, `probability_simulate`, and `probability_sequence` were not called. Calling a made-up adapter would mislabel deterministic source behavior as probability evidence.

## Exact fixture

The retained fixture is [E016_TERMINAL_DATE_SCORE_BASELINE_2026_09_02.scenarios.json](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_TERMINAL_DATE_SCORE_BASELINE_2026_09_02.scenarios.json>).

Fixture SHA-256: `d792ff260cf73c78d757d4d1a9a431fe6e1d51b66e9ed4d141d1064a1557da5b`.

The fixture contains 11 named rows with `actor=KRG`, an existing non-subject country, peace, `world_end=false`, the relevant current date and `global.num_days`, explicit threat-start date/day inputs where applicable, and all non-duration score inputs set to zero or absent. It includes the following exact scenario IDs:

- `E016_TERMINAL_DATE_NO_START`
- `E016_TERMINAL_DATE_179_ACTIVE_DAYS`
- `E016_TERMINAL_DATE_180_ACTIVE_DAYS`
- `E016_TERMINAL_DATE_364_ACTIVE_DAYS`
- `E016_TERMINAL_DATE_365_ACTIVE_DAYS`
- `E016_TERMINAL_DATE_729_ACTIVE_DAYS`
- `E016_TERMINAL_DATE_730_ACTIVE_DAYS`
- `E016_TERMINAL_DATE_CLOSED_180_PLUS_100_INACTIVE`
- `E016_TERMINAL_DATE_RESUMED_180_PLUS_10_ACTIVE`
- `E016_TERMINAL_DATE_NEGATIVE_ELAPSED_CLAMP_ZERO`
- `E016_TERMINAL_DATE_DUPLICATED_CLOSE_ONCE`

Each row has a `sourceExpectation` object that records intended active days and duration points. These fields preserve the test contract and are not claims that the current game engine or MCP service evaluated the effect.

The source-only expected duration contribution is:

| Scenario | Intended active days | Intended duration points | Boundary purpose |
| --- | ---: | ---: | --- |
| `E016_TERMINAL_DATE_NO_START` | 0 | 0 | no valid start must not use absolute encoded date |
| `E016_TERMINAL_DATE_179_ACTIVE_DAYS` | 179 | 0 | just below short threshold |
| `E016_TERMINAL_DATE_180_ACTIVE_DAYS` | 180 | 2 | inclusive short threshold |
| `E016_TERMINAL_DATE_364_ACTIVE_DAYS` | 364 | 2 | just below long threshold |
| `E016_TERMINAL_DATE_365_ACTIVE_DAYS` | 365 | 4 | inclusive long threshold |
| `E016_TERMINAL_DATE_729_ACTIVE_DAYS` | 729 | 4 | just below epic threshold |
| `E016_TERMINAL_DATE_730_ACTIVE_DAYS` | 730 | 6 | inclusive epic threshold |
| `E016_TERMINAL_DATE_CLOSED_180_PLUS_100_INACTIVE` | 180 | 2 | inactive gap must not count |
| `E016_TERMINAL_DATE_RESUMED_180_PLUS_10_ACTIVE` | 190 | 2 | completed interval plus current open interval |
| `E016_TERMINAL_DATE_NEGATIVE_ELAPSED_CLAMP_ZERO` | 0 | 0 | negative elapsed input clamps to zero |
| `E016_TERMINAL_DATE_DUPLICATED_CLOSE_ONCE` | 180 | 2 | duplicate close callback contributes once |

The no-start row intentionally documents the current defect. The current scorer initializes duration from `global.date`, then subtracts the start only when the start variable exists. It therefore has no source-level zero initialization for a missing start. The closed-gap and resumed rows intentionally declare interval-ledger inputs that the current scorer does not read, so they remain future source-contract cases rather than current engine results.

## Audit classification and blockers

This is a deterministic source audit, not a probability audit with a normalized candidate pool. There is no rank, selection race, timing distribution, AI score race, or probability-proportional sampling result to report.

The source arithmetic supports the threshold table above as a bounded source expectation. It does not prove that the live game writes the proposed active-interval fields, invokes the scorer at every required close/resume boundary, or clamps invalid dates at runtime.

No MCP adapter can currently evaluate the scripted effect's scope, date values, global day count, interval receipts, duplicate-close guard, or the downstream `brilliant_scientist_qualifying_defeat_is_ready` caller. No engine proof is claimed for the terminal qualification or for achievement evidence that consumes `brilliant_scientist_world_threat_duration_days`.

The parent may use this frozen fixture for the later same-scenario source comparison after the duration patch. The comparison must preserve the exact 11 scenario bodies and distinguish the unrelated local/regional defeat guard from the date-accounting change.

## Simplifications, omissions, and remaining work

No gameplay simplification was applied. The only omission is MCP execution of the deterministic effect because the installed service exposes no suitable adapter. A later compare remains required after the parent freezes the `global.num_days` active-interval implementation. No overall Event 016 terminal acceptance claim is made.

Skills used: `chaos-redux-events` for the scripted event/super-event source contract and `chaos-redux-subagents` for bounded read-only handoff ownership. The required offline wiki and vanilla documentation references are listed above. No skill was changed.

## Postpatch deterministic-score inspect and source-only comparison

After the active-day implementation was frozen, a fresh mandatory `hoi4.probability_inspect` was run against the current `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt`. It returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`, zero candidates, zero unresolved items, and no available adapters. The current inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95620d1f6a47368e32f9ee69f813075430d9f3b7bdb1cd5ebbb57bf95135775b/5ae79a515c5e24c464d9568b3d08f43f42a48787e41b5d7066281dfe1e740ebd/probability-inspect-94efeab5ec51.json`; it reports source revision `db7d65fa8401296cc2ce14169b121b6978be18a68c3a93e068a8ebc49b366d83` and normalized source hash `94efeab5ec5126e8eaa60321abadf8bc5e5b8ee56eaee879a714d1f2359216d4`.

The current scorer source raw SHA is `b2c58fc0ce3600eadab37f2b3cf7f7f0f91f17bcaa170b85e1a6647edaac4cfb` and current Git blob is `c36068dcdd128b737503bdbbc89a90f9c4c6cefe`. The constants, readiness helper, and super-event caller sources remain raw SHA `b69b37e578dc19bb1842ef8ed46c4eacc1e694e01949a6ce96550f8214392a32`, `a946570099f786b9ba4b606b5de1a94b67e7b33817ad0820d6188d7791b5b4ed`, and `9d818531b8f3813ecad0c3bfea12ab2ccc9fae38e09898f68f01f255e488ffda`, respectively. The retained 11-row fixture and SHA `d792ff260cf73c78d757d4d1a9a431fe6e1d51b66e9ed4d141d1064a1557da5b` are unchanged.

The source-only comparison against retained HEAD `957ae81cc6539c2e29beebe92f4c6523eea91532` confirms the intended deterministic change: the scorer now calls `brilliant_scientist_refresh_world_threat_duration`, the refresh helper zero-initializes duration, reuses accumulated active days, and adds only the current open interval from `global.num_days`; start/close callers write and clear the numeric day receipt. The three duration thresholds and score constants are unchanged. The working-tree diff also contains parent-owned close-hook wiring and a separate `NOT = { has_country_flag = brilliant_scientist_local_or_regional_defeat_recorded }` guard; those are not attributed to the date-accounting comparison.

Because the fresh inspect found no weighted surface, no probability evaluate, sweep, simulation, sequence, render, or MCP probability comparison was run. The retained 11-row fixture remains a source-contract expectation only: no normalized chance, timing distribution, or engine-level deterministic score result is claimed. The after state is therefore classified as `source-compared / MCP-unresolved`, not as a probability certification.
