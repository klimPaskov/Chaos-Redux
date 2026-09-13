# Event 031 focus army experience alias repair

Status: implemented in the scoped focus source; parent integration and launch validation remain pending.

This bounded repair addresses the six `Invalid effect add_army_experience` entries reported for `common/national_focus/031_random_terror_focus.txt` in `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_08/logs/error.log` at lines 130, 722, 814, 932, 1099, and 2073.

The offline Effects reference documents `army_experience = <float> / <variable>` as the country effect that adds army experience, and the installed vanilla effects documentation lists `army_experience` as a country-scoped effect.

## Changed files

| File | Change |
| --- | --- |
| `common/national_focus/031_random_terror_focus.txt` | Replaced six exact `add_army_experience` keywords with `army_experience` and preserved every argument and surrounding block. |
| `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_focus_aliases/common/national_focus/031_random_terror_focus.txt` | Byte-preserving backup of the immediate pre-patch source. |
| `docs/testing/live_qa/2026-09-04_catalog_01/event31_focus_alias_repair.md` | This implementation and validation handoff. |

The backup is 104,236 bytes with SHA-256 `258C2DEAF721E9047E9A812EC37E823CC5D0A88E3851826CBCC2CA18FB5EE18C`.

## Changed focus ids

| Focus id | Source line | Argument preserved |
| --- | ---: | --- |
| `random_terror_founding_crisis` | 130 | `constant:random_terror_cost.actor_offensive_experience` |
| `random_terror_command_the_front` | 722 | `constant:random_terror_cost.actor_offensive_experience` |
| `random_terror_standardize_captured_formations` | 814 | `constant:random_terror_cost.actor_convert_experience` |
| `random_terror_command_the_armed_movement` | 932 | `constant:random_terror_cost.actor_offensive_experience` |
| `random_terror_disciplined_ranks` | 1099 | `constant:random_terror_cost.actor_convert_experience` |
| `random_terror_prepare_the_state_offensive` | 2073 | `constant:random_terror_cost.actor_offensive_experience` |

## Route behavior before and after

| Surface | Before | After |
| --- | --- | --- |
| Six listed completion rewards | The parser rejected `add_army_experience`, producing six blocking focus diagnostics and preventing the intended army experience reward from resolving. | The native `army_experience` effect is parsed with the original constant argument, so each focus retains its intended army experience reward. |
| Focus routes and prerequisites | Existing route graph, focus ids, prerequisites, mutual exclusions, coordinates, and AI weights. | Unchanged. |
| Localisation and icons | Existing keys and icon references. | Unchanged. |

No focus route was added, removed, merged, simplified, or redesigned by this repair.

## MCP evidence

The required pre-change read-only focus inspection used `hoi4.focus_inspect` for `random_terror_actor_focus_tree` and returned `FOCUS_INSPECTED` with six blocking `FOCUS_GAMEPLAY_REFERENCE_MISSING` diagnostics at the six source lines.

Pre-change inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f812c9df96a19fe72269984c4ff57dd199ad361af1d8e4507d160101d700f7a1/5a439e27d6cb3ada374e1cb6c7029d67442b867449bcc73e6300c32dde1ed860/focus-inspect.7119d6f90d50fd93.json`.

The required pre-change read-only focus render returned `FOCUS_RENDERED` and produced HTML, SVG, JSON, source-map, and plan artifacts.

Pre-change render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0bb62a68c0a644a2aca40f12aaf2c9c613147e6bffa8c62244d0aeb446d99fa2/8e8d10da75ab86e4d48846c0eb0ee338825953fb4eb7c0155d09f7129470f338/random_terror_actor_focus_tree.focus.html`.

The pre-change layout had 114 focuses, 104 connectors, zero connector crossings, zero node intersections, zero long connectors, and layout hash `69ec88315409c5c578ffca2852052037f7ee6a48510a92189c11ac79a1a6d2a9`.

The required post-change read-only focus inspection returned `FOCUS_INSPECTED` with validation passed and zero blocking focus diagnostics.

Post-change inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17a9f2e436f962110e0d5361bf0ffff11fcc55e8ee8819871abe9106d72bee7a/98296d5878c2985334ba87c41d3c6e2df108a80b145db73506405ba9c9b30bd4/focus-inspect.43177f1e896b44e4.json`.

The required post-change read-only focus render returned `FOCUS_RENDERED` and retained the same 114-focus graph, 104 connectors, zero connector crossings, zero node intersections, zero long connectors, and layout hash `69ec88315409c5c578ffca2852052037f7ee6a48510a92189c11ac79a1a6d2a9`.

Post-change render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/366da6eef3cfd897c35f268f3b01ac3d8e7c9afff1bf74ffd6c96216690011cf/5cd161a03fa756f572ed18bc1d4943d3d18a89c0d328843fe5667c5cca29dad7/random_terror_actor_focus_tree.focus.html`.

The exposed MCP tool inventory has no separate `hoi4.focus_lint` route, so `hoi4.focus_inspect` validation and its blocking diagnostics serve as the available narrow focus lint evidence.

## Source validation

The post-patch source audit finds zero `add_army_experience` tokens and six `army_experience` completion-reward calls at the expected lines.

The working source hash is `D3082BA4F338E9CF399E8B0EF37FE89BE48F7A402DA3F66F0E516A738254954E`, and the 24-byte size reduction is exactly the six removed `add_` prefixes.

## Skipped meaningful validation

No `hoi4.focus_rewrite` call was used because the user authorized the direct six-token repair, the existing layout is unchanged, and no focus redesign is in scope.

No `chaosx_ai_probability_auditor` pass was routed because no focus weight, AI block, probability-bearing modifier, or route choice changed.

No live game launch was performed because the parent owns launch and integration validation.

## Remaining risks and parent handoff

The post-change MCP render still reports the unrelated vanilla warning that `continuous_restrict_freedom_desc` is missing from `l_english` in `game:common/continuous_focus/generic.txt`.

The launch log contains other out-of-scope invalid effects and triggers in `common/decisions/031_random_terror_decisions.txt`; this repair intentionally leaves those files untouched.

The parent should review the three listed changed files, preserve the backup, and run the authorized integration launch check.
