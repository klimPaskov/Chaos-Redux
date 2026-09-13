# Missing country history source recovery — launch 08

Bounded read-only QA report for `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_08/logs/error.log`.

## Scope read

- Parent task: extract the exact `history.cpp` missing-history tags from launch 08, map them to current country-tag registries and package files, and locate an approved existing or tracked recovery source.
- Constraints followed: exact-tag tranche only; no country/history/gameplay edits; no registry removal; no invented generic countries or fallback histories; protected Event 006, 012, 016, and 023 packages were left untouched.
- References read: `AGENTS.md`, `chaos-redux-subagents/SKILL.md`, the offline core wiki pages and `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md`, vanilla documentation, vanilla `common/country_tags/zz_dynamic_countries.txt`, current Event 039 country/runtime files, Event 039 specs and handoffs, and the launch 08 QA artifacts.
- The only write from this tranche is this report.

## Primary findings

- Launch 08 contains exactly seven unique missing-history records: `AXS`, `AXT`, `AXU`, `AXV`, `AXW`, `AXY`, and `AXZ`.
- The records are one each at `error.log:826-832`, all `[history.cpp:279]`, with the same `10:31:49` timestamp.
- History has no size field; each tag represents one missing history-file input, so the bounded count is seven missing files rather than a normal/medium/small size matrix.
- All seven tags are declared in the Event 039 registry, and no current or tracked history source was found for any of them.
- The registry comments describe dormant dynamic carriers, while the registry has no `dynamic_tags = yes` declaration before the entries.

## Current tag registry and package mapping

| Tag | Registry evidence | Common country definition | Runtime/package evidence | History result |
| --- | --- | --- | --- | --- |
| `AXS` | `common/country_tags/039_murder_mystery_countries.txt:9` | `common/countries/039_murder_mystery_assassin_state.txt:1-12` | `create_dynamic_country { original_tag = AXS }` at `common/scripted_effects/039_murder_mystery_integration_effects.txt:1520-1522` | No `history/countries` file with `AXS` prefix |
| `AXT` | `common/country_tags/039_murder_mystery_countries.txt:10` | `common/countries/039_murder_mystery_derivative_state.txt:1-12` | `create_dynamic_country { original_tag = AXT }` at `common/scripted_effects/039_murder_mystery_integration_effects.txt:1715-1717` | No `history/countries` file with `AXT` prefix |
| `AXU` | `common/country_tags/039_murder_mystery_countries.txt:11` | shared `039_murder_mystery_derivative_state.txt` | Reserved Event 039 derivative carrier; no direct `original_tag = AXU` call appeared in the bounded source scan | No `history/countries` file with `AXU` prefix |
| `AXV` | `common/country_tags/039_murder_mystery_countries.txt:12` | shared `039_murder_mystery_derivative_state.txt` | Reserved Event 039 derivative carrier; no direct `original_tag = AXV` call appeared in the bounded source scan | No `history/countries` file with `AXV` prefix |
| `AXW` | `common/country_tags/039_murder_mystery_countries.txt:13` | shared `039_murder_mystery_derivative_state.txt` | Reserved Event 039 derivative carrier; no direct `original_tag = AXW` call appeared in the bounded source scan | No `history/countries` file with `AXW` prefix |
| `AXY` | `common/country_tags/039_murder_mystery_countries.txt:14` | shared `039_murder_mystery_derivative_state.txt` | Reserved Event 039 derivative carrier; no direct `original_tag = AXY` call appeared in the bounded source scan | No `history/countries` file with `AXY` prefix |
| `AXZ` | `common/country_tags/039_murder_mystery_countries.txt:15` | shared `039_murder_mystery_derivative_state.txt` | Reserved Event 039 derivative carrier; no direct `original_tag = AXZ` call appeared in the bounded source scan | No `history/countries` file with `AXZ` prefix |

The common country definitions are present, but they only provide graphical culture and colours; they do not provide country history.

The derivative definition explicitly says `No ordinary civil-war history is attached to this tag` at `common/countries/039_murder_mystery_derivative_state.txt:5-6`, which supports the intended carrier design but does not satisfy the loader while these tags are registered as ordinary entries.

## History filename and path checks

- Direct prefix check over `history/countries` returned `AXS: ABSENT`, `AXT: ABSENT`, `AXU: ABSENT`, `AXV: ABSENT`, `AXW: ABSENT`, `AXY: ABSENT`, and `AXZ: ABSENT`.
- A recursive exact-name and Event 039 history-name check under `history/` returned no result for any of the seven tags, `039_murder`, `murder_mystery`, `assassin`, or `derivative`.
- The check covered uppercase, lowercase, underscore, dash, space, and arbitrary suffix variants because the filter compared the first three filename characters case-insensitively.
- No nested or alternate history path was found; the offline country-creation reference requires country history under `history/countries` and uses the first three filename characters as the tag.

## Recoverable source evidence

- `git ls-files -- history/countries` produced `TRACKED_EXACT_HISTORY_COUNT=0` for the seven prefixes.
- `git log --all --full-history --name-only -- history/countries` produced `GIT_HISTORY_EXACT_NAME_COUNT=0` for the seven prefixes.
- The current Event 039 registry, both common country definitions, and the integration effect are all `??` untracked worktree files in the scoped `git status` check, so the current carrier implementation has no tracked history counterpart to recover.
- Exact-tag searches in the scoped Event 039 specs, plans, assets, and QA docs found no history-source or approved recovery file; the only non-visual exact-tag documentation hit was the pre-patch localisation name list.
- Event 039 asset evidence exists for flags only: `docs/assets/039_murder_mystery/visual_asset_audit.md:296-316` records normal, medium, and small `AXS`–`AXZ` ladders as passing, and the corresponding `gfx/flags/AX*.tga`, `gfx/flags/medium/AX*.tga`, and `gfx/flags/small/AX*.tga` files exist. These flag assets cannot serve as country history.
- No approved existing history source was found, so there is no safe file to install for any of the seven tags.

## First cause

The direct cause of the seven log records is a country-tag registry entry without a matching `history/countries` file.

The source-side mismatch is that `common/country_tags/039_murder_mystery_countries.txt:4-6` describes the entries as dormant carriers used only by `create_dynamic_country`, but the file has no `dynamic_tags = yes` line before `AXS`–`AXZ` at lines 9-15.

Vanilla provides the relevant precedent at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/zz_dynamic_countries.txt:1-2`: it declares `dynamic_tags = yes` before its `D01` entries, and the installed vanilla `history/countries` folder has zero `D##` history files. The offline country-creation wiki likewise explains both the dynamic-tag declaration and the ordinary per-tag history filename rule.

This establishes a parent-owned registration decision: either the carriers must be made part of an approved dynamic-tag pool using the validated package design, or seven approved per-tag history inputs must be supplied for ordinary registration. This scout did neither.

## Source-of-truth and protected-package check

- `docs/specs/039_murder_mystery_specs/039_murder_mystery_spec_part_6_assassin_state.md:15-21` says no country tag was selected in the spec and requires the carrier audit before asset or country production.
- `docs/plans/039_murder_mystery_plans/subagent_handoffs/chaosx_portrait_creator.md:62-63` also records the dynamic Assassin State carrier tag as unresolved.
- The bounded source search found the seven tags only in the Event 039 registry, Event 039 integration effect, and Event 039 localisation; no protected Event 006, 012, 016, or 023 source file claims these tags.
- No protected package was edited.

## Likely parent action and validation

1. Resolve the accepted Event 039 carrier model before creating any history file: confirm a validated dynamic-tag pool and its capacity, or obtain approved static history content for every ordinary tag.
2. If the dynamic model is accepted, apply the registry change through the parent-owned workflow and verify that all seven entries remain unique and available to the intended `create_dynamic_country` calls.
3. If ordinary registration is accepted, obtain seven tag-specific history files whose names begin with `AXS`, `AXT`, `AXU`, `AXV`, `AXW`, `AXY`, and `AXZ`; do not use a generic shell or repurpose the flag sources.
4. Re-run the narrow launch08 error scan and require zero `history.cpp:279` records for these seven tags, then check that no protected package changed.

## Risks and blockers

- Confirmed blocker: seven history files are absent and no approved current, tracked, malformed-path, case-variant, or recovery-doc source exists.
- Confirmed blocker: the accepted Event 039 spec and the current untracked tag registry disagree on whether the carrier tags have been selected and how they are registered.
- Ordinary risk: adding ordinary histories to dormant carriers could create unintended start-date country state, politics, or OOB behaviour.
- Ordinary risk: declaring a dynamic pool without the parent’s capacity and ownership review could create carrier exhaustion or tag-collision problems.

## Recommended next action

Parent should resolve the Event 039 carrier registration decision and source-of-truth approval before any history-file write; the recovery scout found no existing file that can be safely installed.
