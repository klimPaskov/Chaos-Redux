# Event 006 flag atlas and current diagnostics re-audit

Date: 2026-08-03.

Mode: read-only audit after commit `0810aac90` and the current v103 evidence handoff. No gameplay, focus, flag, asset, localisation, or specification file was changed.

## Verdict

The supplied Event 006 `flagtextureatlas.cpp:510` error family is fully resolved for the registered Event 006 country-tag surface. Every one of the 102 tags registered in `common/country_tags/006_independence_wave_countries.txt` has the unsuffixed flag and all four standard ideology filenames in all three engine atlas sizes. That is 1,530 required TGA files with zero missing files, zero invalid size or depth headers, and zero base-to-ideology byte mismatches.

No Event 006 focus blocker is present in the fresh MCP inspection. The tree retains one design warning for the intentionally isolated `independence_wave_preserve_independent_command` focus. A separate dirty-worktree regression remains blocking in the rival-bloc leadership decision cost gate because it reads engine-backed army experience through `check_variable`.

## Flag atlas evidence

Command:

```powershell
python -B .tools\audit_event6_flags.py --strict
```

Result:

```text
registered Event 006 tags: 102
complete flag families: 102
incomplete flag families: 0
```

A read-only Python header and SHA-256 cross-check enumerated `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small` for each registered tag and the `communism`, `democratic`, `fascism`, and `neutrality` suffixes. It required 82x52 normal, 41x26 medium, and 10x7 small images with 24-bit or 32-bit TGA depth, then compared every suffixed file with its size-matched unsuffixed base.

Result:

```text
tags=102 expected_files=1530 inspected_files=1530
missing=0 bad_headers=0 base_variant_byte_mismatches=0
```

The ideology files therefore exist at the exact names that caused the supplied democratic atlas errors, are valid for the corresponding atlas size, and preserve the reviewed base design byte-for-byte. This closes the reported missing-path error without implying package admission or distinct ideology art.

Command:

```powershell
python -B .tools\audit_chaosx_country_tags.py --surface-scan
```

Result:

```text
Protected Event 006/Soviet tags: 136; external country-definition collisions: 0; external identity-surface collisions: 0; random-event roots skipped: 1
```

The two currently modified `RTA` and `RTX` base-flag triplets are not registered by the Event 006 country-tag file and do not alter this result.

## Focus diagnostics

Read-only MCP call:

```text
hoi4.focus_inspect(mode=national, relativePath=common/national_focus/006_independence_wave_focus.txt, treeId=independence_wave_focus_tree)
```

Result: `FOCUS_INSPECTED`, status `ok`, blockers `[]`, 184 direct focuses, 192 connectors, zero crossings, zero node intersections, zero long connectors, and zero too-close same-row pairs. The current artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cb20af8dfc23427689ac6b8bdec6a78efc418271d8ab248ee8422f16dc22a66/d88cdfbc49ae344432995583c454a4ee4a013f6e1aab4855556959a76869cf0a/focus-inspect.308d914c1e5c7a4d.json`.

The sole Event 006 diagnostic is `FOCUS_ISOLATED` for `independence_wave_preserve_independent_command` at `common/national_focus/006_independence_wave_focus.txt:734`. It is a design warning rather than a blocker. The fourteen missing-sprite errors and the missing `continuous_restrict_freedom_desc` warning belong to vanilla `game:common/continuous_focus/generic.txt`, not to an Event 006 focus or asset. The earlier 186-connector receipt is stale after the six restored visible prerequisite lines; 192 is the current inspected connector count.

## Current blocking source diagnostic

Command:

```powershell
rg -n -g '006_independence_wave*.txt' "check_variable\s*=\s*\{\s*var\s*=\s*(stability|war_support|army_experience)\b" common
```

Current result:

```text
common\scripted_triggers\006_independence_wave_rival_bloc_triggers.txt:162: check_variable = { var = army_experience value = constant:independence_wave_rival_bloc_cost.leadership_army_experience compare = greater_than }
```

`git diff --unified=0 -- common\scripted_triggers\006_independence_wave_rival_bloc_triggers.txt` proves this is an uncommitted regression from the engine-backed `army_experience > constant:...` trigger. `common/decisions/006_independence_wave_rival_bloc_decisions.txt:210` and `:211` use the helper for both `available` and `custom_cost_trigger`, so the leadership decision can fail closed despite sufficient army experience. The committed remaining-engine-value repair closed the FORM-03, FORM-05, and Pacific stability or war-support cases, but it did not cover this rival-bloc army-experience conversion.

## Remaining completion blockers

- Flag atlas coverage is no longer a blocker.
- The rival-bloc army-experience gate above is a current source blocker and should be restored to the documented engine-value trigger before the dirty tranche is committed.
- Focus geometry has no current Event 006 blocker. Removing the isolated warning remains coordinated parent-owned presentation work, not a safe one-line local patch.
- Whole-event completion remains **HOLD / PARTIAL** for the v103 boundaries: fourteen of 193 non-overlay packages are attested, the upper allocation bands remain fail-closed, wider formable and sensitive-package readiness is incomplete, `6001` remains rights and runtime blocked, and package AI, balance, GUI, event-log, allocation, and save/load evidence remains bounded.

No fallback or simplification was introduced by this audit.
