# Repo Explorer Handoff

QA artifact: bounded missing country-flag source recovery for the archived Event 031 launch log.

## Scope read

- Parent task: Recover the missing flag source/final evidence reported by `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_07/logs/error.log`.
- Explicit constraints: read-only first tranche; no gameplay, localisation, GFX, asset, or country edits; no staging, commit, game launch, desktop automation, generated art, generic fallback, or web research.
- Files or ids requested: the log-unique tags `JHX`, `JIX`, `JKX`, `JLX`, `JMX`, `JNX`, `JOX`, and `JPX`; normal, medium, and small files for democratic and neutrality.
- Skills or docs read: `AGENTS.md`; `chaos-redux-event-assets/SKILL.md`; `chaos-redux-subagents/SKILL.md`; the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, graphical assets, country creation, and cosmetic tags; vanilla `script_concept_documentation.md`, `effects_documentation.md`, and `triggers_documentation.md`; vanilla Germany country and flag references.

## Primary findings

- The launch log has exactly eight unique country tags and six missing combinations per tag: 48 direct runtime flag files in total.
- Every direct tag path is absent for both ideologies at all three tiers. There is no case where a direct full-size flag exists while only medium or small is missing.
- The eight histories start with neutrality as the ruling party and 100 neutrality popularity, while the same launch log reports democratic atlas requests at `no_game_date` and neutrality requests at `1936.01.01.12`.
- Event 031 already has eight complete three-size fictional flag ladders under `event31_dormant_carrier_01` through `_08`. The source and final files are usable only for those existing cosmetic-tag consumers until the parent accepts identity and wiring; they are not direct `JHX` through `JPX` replacements.
- The protected Event 006, Event 012, Event 016, and Event 023 packages have no bounded exact-tag ownership overlap with `JHX` through `JPX`. Their active or pending asset records are listed below.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_07/logs/error.log:7420-7559` | Archived runtime source of the missing-flag report. | Democratic requests occur at `no_game_date`; neutrality requests occur at `1936.01.01.12`; all three folder tiers are reported for all eight tags. |
| `common/country_tags/031_random_terror_countries.txt:8-15` | Canonical current tag-to-country mapping. | Resolves all eight tags to the `common/countries/031_random_terror_J*.txt` definitions. |
| `common/countries/031_random_terror_JHX.txt` through `common/countries/031_random_terror_JPX.txt:2-5` | Current country definitions. | All eight set `eastern_european_gfx`, `eastern_european_2d`, and a country color; no flag token is present. |
| `history/countries/JHX - Local Cell.txt` through `history/countries/JPX - Transnational Network II.txt:8-65` | Startup identity and ideology context. | Each has a fallback capital and `oob = "031_random_terror_dormant"`; each sets ruling party `neutrality`, democratic popularity `0`, and neutrality popularity `100`. |
| `common/scripted_effects/031_random_terror_effects.txt:4522-4529` | Existing Event 031 cosmetic identity map. | `original_tag = JHX` through `JPX` maps in order to `event31_dormant_carrier_01` through `_08`. |
| `docs/assets/031_random_terror/flags/manifest.md:1-20` | Existing source and runtime flag manifest. | Eight dormant-carrier source masters, processed PNGs, and normal/medium/small TGAs are recorded; status is `needs_user_review` for parent identity/runtime review. |
| `docs/plans/031_random_terror_plans/subagent_handoffs/031_flags_categories_visual_audit_handoff.md:27-34` | Existing visual audit of the eight candidate ladders. | All eight rows are `PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY` at `82x52 / 41x26 / 10x7`. |
| `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/manifest.md:1,7-22` and `blockers.md:1-3` | Protected Event 006 ownership evidence. | Event 006 owns the researched `AKX`–`CLX` tranche and explicitly refuses placeholders for unresolved reservations; no J-tag row exists. |
| `docs/plans/012_africa_plans/012_africa_independence_wave_tag_loading_handoff.md:39-61` and `docs/assets/012_africa/high_chaos_country_art/` | Protected Event 012 ownership evidence. | Event 012 uses non-J niche carriers and separate `AFRICA_PROMOTED_*` high-chaos flag ladders; current 2026-09-05 icon/event-art handoffs remain pending live review/promotion. |
| `docs/assets/016_brilliant_scientist/manifest.md:7-33` and `package_records/krg_flag_package.json` | Protected Event 016 ownership evidence. | KRG base/route triplets and DHR flag identities have their own runtime ladders and registrations; no J-tag row exists. |
| `docs/assets/023_sov_nuclear_bombs/manifest.md:5,80` and `gfx_handoff.md:5` | Protected Event 023 ownership evidence. | Event 023 explicitly excludes flags from its original asset scope; its active package is event art/icons/DDS, with no J-tag flag claim. |

## Current tag definitions

| Tag | Current profile | Fallback capital | Country definition | History file | Existing direct flag state |
| --- | --- | ---: | --- | --- | --- |
| `JHX` | Local Cell | `104` | `common/countries/031_random_terror_JHX.txt` | `history/countries/JHX - Local Cell.txt` | No `gfx/flags/JHX*` file; no flag field in the country definition. |
| `JIX` | Regional Insurgent | `47` | `common/countries/031_random_terror_JIX.txt` | `history/countries/JIX - Regional Insurgent.txt` | No `gfx/flags/JIX*` file; no flag field in the country definition. |
| `JKX` | Transnational Network | `112` | `common/countries/031_random_terror_JKX.txt` | `history/countries/JKX - Transnational Network.txt` | No `gfx/flags/JKX*` file; no flag field in the country definition. |
| `JLX` | Jihadist International | `49` | `common/countries/031_random_terror_JLX.txt` | `history/countries/JLX - Jihadist International.txt` | No `gfx/flags/JLX*` file; no flag field in the country definition. |
| `JMX` | Final Revelation / Final Command | `64` | `common/countries/031_random_terror_JMX.txt` | `history/countries/JMX - Final Command.txt` | No `gfx/flags/JMX*` file; no flag field in the country definition. |
| `JNX` | Local Cell II | `107` | `common/countries/031_random_terror_JNX.txt` | `history/countries/JNX - Local Cell II.txt` | No `gfx/flags/JNX*` file; no flag field in the country definition. |
| `JOX` | Regional Insurgent II | `46` | `common/countries/031_random_terror_JOX.txt` | `history/countries/JOX - Regional Insurgent II.txt` | No `gfx/flags/JOX*` file; no flag field in the country definition. |
| `JPX` | Transnational Network II | `141` | `common/countries/031_random_terror_JPX.txt` | `history/countries/JPX - Transnational Network II.txt` | No `gfx/flags/JPX*` file; no flag field in the country definition. |

The country package handoff at `docs/plans/031_random_terror_plans/subagent_handoffs/031_country_package_handoff.md:17-27,50-52` identifies the same eight profiles and says the package has no country flags or portrait sprite registrations. The current country files therefore do not supply an alternate default image.

## Missing direct runtime ladder

The expected filenames below follow the HOI4 country/cosmetic flag naming rule: `TAG_ideology.tga` in the root, `medium`, and `small` folders. The `normal`, `medium`, and `small` dimensions are respectively `82x52`, `41x26`, and `10x7`.

| Tag | Ideology | Size | Expected runtime | Existing source/final or absent proof |
| --- | --- | --- | --- | --- |
| `JHX` | `democratic` | normal (82x52) | `gfx/flags/JHX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JHX` | `democratic` | medium (41x26) | `gfx/flags/medium/JHX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JHX` | `democratic` | small (10x7) | `gfx/flags/small/JHX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JHX` | `neutrality` | normal (82x52) | `gfx/flags/JHX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JHX` | `neutrality` | medium (41x26) | `gfx/flags/medium/JHX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JHX` | `neutrality` | small (10x7) | `gfx/flags/small/JHX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JIX` | `democratic` | normal (82x52) | `gfx/flags/JIX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JIX` | `democratic` | medium (41x26) | `gfx/flags/medium/JIX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JIX` | `democratic` | small (10x7) | `gfx/flags/small/JIX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JIX` | `neutrality` | normal (82x52) | `gfx/flags/JIX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JIX` | `neutrality` | medium (41x26) | `gfx/flags/medium/JIX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JIX` | `neutrality` | small (10x7) | `gfx/flags/small/JIX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JKX` | `democratic` | normal (82x52) | `gfx/flags/JKX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JKX` | `democratic` | medium (41x26) | `gfx/flags/medium/JKX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JKX` | `democratic` | small (10x7) | `gfx/flags/small/JKX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JKX` | `neutrality` | normal (82x52) | `gfx/flags/JKX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JKX` | `neutrality` | medium (41x26) | `gfx/flags/medium/JKX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JKX` | `neutrality` | small (10x7) | `gfx/flags/small/JKX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JLX` | `democratic` | normal (82x52) | `gfx/flags/JLX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JLX` | `democratic` | medium (41x26) | `gfx/flags/medium/JLX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JLX` | `democratic` | small (10x7) | `gfx/flags/small/JLX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JLX` | `neutrality` | normal (82x52) | `gfx/flags/JLX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JLX` | `neutrality` | medium (41x26) | `gfx/flags/medium/JLX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JLX` | `neutrality` | small (10x7) | `gfx/flags/small/JLX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JMX` | `democratic` | normal (82x52) | `gfx/flags/JMX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JMX` | `democratic` | medium (41x26) | `gfx/flags/medium/JMX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JMX` | `democratic` | small (10x7) | `gfx/flags/small/JMX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JMX` | `neutrality` | normal (82x52) | `gfx/flags/JMX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JMX` | `neutrality` | medium (41x26) | `gfx/flags/medium/JMX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JMX` | `neutrality` | small (10x7) | `gfx/flags/small/JMX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JNX` | `democratic` | normal (82x52) | `gfx/flags/JNX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JNX` | `democratic` | medium (41x26) | `gfx/flags/medium/JNX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JNX` | `democratic` | small (10x7) | `gfx/flags/small/JNX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JNX` | `neutrality` | normal (82x52) | `gfx/flags/JNX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JNX` | `neutrality` | medium (41x26) | `gfx/flags/medium/JNX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JNX` | `neutrality` | small (10x7) | `gfx/flags/small/JNX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JOX` | `democratic` | normal (82x52) | `gfx/flags/JOX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JOX` | `democratic` | medium (41x26) | `gfx/flags/medium/JOX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JOX` | `democratic` | small (10x7) | `gfx/flags/small/JOX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JOX` | `neutrality` | normal (82x52) | `gfx/flags/JOX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JOX` | `neutrality` | medium (41x26) | `gfx/flags/medium/JOX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JOX` | `neutrality` | small (10x7) | `gfx/flags/small/JOX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JPX` | `democratic` | normal (82x52) | `gfx/flags/JPX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JPX` | `democratic` | medium (41x26) | `gfx/flags/medium/JPX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JPX` | `democratic` | small (10x7) | `gfx/flags/small/JPX_democratic.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JPX` | `neutrality` | normal (82x52) | `gfx/flags/JPX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JPX` | `neutrality` | medium (41x26) | `gfx/flags/medium/JPX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |
| `JPX` | `neutrality` | small (10x7) | `gfx/flags/small/JPX_neutrality.tga` | **Absent — A1.** `Test-Path -LiteralPath` returned `False` for this exact path; the direct basename scan returned zero matches. |

Absent proof A1 was run against all 48 paths. The per-path table above records `False` for every `Test-Path` check. A second exact-name scan, `rg --files gfx/flags | Select-String -Pattern 'JHX|JIX|JKX|JLX|JMX|JNX|JOX|JPX'`, returned `MatchCount : 0`. A bounded `rg --files docs/assets` scan also found no source/final filenames carrying any of the eight direct tags.

The archived log extraction itself returned the six combinations for each tag. For example, `JHX` democratic is at log lines `7420`, `7428`, and `7436`, while `JHX` neutrality is at `7536`, `7544`, and `7552`; `JPX` appears at `7427`, `7435`, `7443`, `7543`, `7551`, and `7559`. The same six-path pattern repeats for the other six tags.

## Existing Event 031 candidates

These are the only pre-existing source/final flag ladders that map one-to-one to the eight J-tag carriers. They are separate cosmetic-tag basenames and must not be copied to direct J-tag filenames by inference.

| Current tag | Existing cosmetic basename | Existing source master | Existing final runtime ladder | Evidence and status |
| --- | --- | --- | --- | --- |
| `JHX` | `event31_dormant_carrier_01` | `docs/assets/031_random_terror/flags/source_png/event31_dormant_carrier_01_source.png` | `gfx/flags/event31_dormant_carrier_01.tga; gfx/flags/medium/event31_dormant_carrier_01.tga; gfx/flags/small/event31_dormant_carrier_01.tga` | Manifest rows `13-20`; visual audit row for this carrier is `PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY`. Safe only when the runtime consumer is the mapped cosmetic tag. |
| `JIX` | `event31_dormant_carrier_02` | `docs/assets/031_random_terror/flags/source_png/event31_dormant_carrier_02_source.png` | `gfx/flags/event31_dormant_carrier_02.tga; gfx/flags/medium/event31_dormant_carrier_02.tga; gfx/flags/small/event31_dormant_carrier_02.tga` | Manifest rows `13-20`; visual audit row for this carrier is `PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY`. Safe only when the runtime consumer is the mapped cosmetic tag. |
| `JKX` | `event31_dormant_carrier_03` | `docs/assets/031_random_terror/flags/source_png/event31_dormant_carrier_03_source.png` | `gfx/flags/event31_dormant_carrier_03.tga; gfx/flags/medium/event31_dormant_carrier_03.tga; gfx/flags/small/event31_dormant_carrier_03.tga` | Manifest rows `13-20`; visual audit row for this carrier is `PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY`. Safe only when the runtime consumer is the mapped cosmetic tag. |
| `JLX` | `event31_dormant_carrier_04` | `docs/assets/031_random_terror/flags/source_png/event31_dormant_carrier_04_source.png` | `gfx/flags/event31_dormant_carrier_04.tga; gfx/flags/medium/event31_dormant_carrier_04.tga; gfx/flags/small/event31_dormant_carrier_04.tga` | Manifest rows `13-20`; visual audit row for this carrier is `PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY`. Safe only when the runtime consumer is the mapped cosmetic tag. |
| `JMX` | `event31_dormant_carrier_05` | `docs/assets/031_random_terror/flags/source_png/event31_dormant_carrier_05_source.png` | `gfx/flags/event31_dormant_carrier_05.tga; gfx/flags/medium/event31_dormant_carrier_05.tga; gfx/flags/small/event31_dormant_carrier_05.tga` | Manifest rows `13-20`; visual audit row for this carrier is `PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY`. Safe only when the runtime consumer is the mapped cosmetic tag. |
| `JNX` | `event31_dormant_carrier_06` | `docs/assets/031_random_terror/flags/source_png/event31_dormant_carrier_06_source.png` | `gfx/flags/event31_dormant_carrier_06.tga; gfx/flags/medium/event31_dormant_carrier_06.tga; gfx/flags/small/event31_dormant_carrier_06.tga` | Manifest rows `13-20`; visual audit row for this carrier is `PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY`. Safe only when the runtime consumer is the mapped cosmetic tag. |
| `JOX` | `event31_dormant_carrier_07` | `docs/assets/031_random_terror/flags/source_png/event31_dormant_carrier_07_source.png` | `gfx/flags/event31_dormant_carrier_07.tga; gfx/flags/medium/event31_dormant_carrier_07.tga; gfx/flags/small/event31_dormant_carrier_07.tga` | Manifest rows `13-20`; visual audit row for this carrier is `PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY`. Safe only when the runtime consumer is the mapped cosmetic tag. |
| `JPX` | `event31_dormant_carrier_08` | `docs/assets/031_random_terror/flags/source_png/event31_dormant_carrier_08_source.png` | `gfx/flags/event31_dormant_carrier_08.tga; gfx/flags/medium/event31_dormant_carrier_08.tga; gfx/flags/small/event31_dormant_carrier_08.tga` | Manifest rows `13-20`; visual audit row for this carrier is `PASS_VISUAL; NEEDS_USER_REVIEW_IDENTITY`. Safe only when the runtime consumer is the mapped cosmetic tag. |

The corresponding processed review PNGs are under `docs/assets/031_random_terror/flags/processed_png/{normal,medium,small}/`, and the complete manifest also records the final TGA hashes. A read-only header check found all 24 existing Event 031 candidate TGAs present with type `2`, descriptor `0`, and dimensions `82x52`, `41x26`, and `10x7`.

## Protected active-event ownership

| Event | Protected owner and active/pending evidence | Relationship to this tranche |
| --- | --- | --- |
| 006 | `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/manifest.md:1,7-22` records the Event 006 `AKX`–`CLX` researched flag ladders. `blockers.md:1-3` says unresolved reservations remain fail-closed with no generic or placeholder flags. | No `JHX`–`JPX` rows or direct filenames were found. Preserve the Event 006 package and its blocked reservations. |
| 012 | `docs/plans/012_africa_plans/012_africa_independence_wave_tag_loading_handoff.md:39-61` assigns Event 012 to `DOX`, `DSX`, `DUX`, `DYX`, `DZX`, `EMX`, and `EQX` and says no `AFRICA_PRIORITY_*` flag family is required. Event 012 high-chaos source/processed/runtime folders contain separate `AFRICA_PROMOTED_ANCIENT`, `GORILLA`, `GREEN`, `PAN`, `RIVERS`, and `STONEBORN` ladders. The 2026-09-05 icon and event-art handoffs record live review/promotion pending. | No J-tag ownership overlap. `docs/assets/012_africa/manifest.md` is absent, so the flag evidence remains folder/prompt and handoff evidence. |
| 016 | `docs/assets/016_brilliant_scientist/manifest.md:7,27,33` records seven KRG route triplets and four DHR flag identities at all three sizes, with runtime registrations present. `docs/assets/016_brilliant_scientist/package_records/krg_flag_package.json` records source, processed, package TGA, and runtime paths. | No `JHX`–`JPX` rows or direct filenames were found. Preserve KRG/DHR ladders. |
| 023 | `docs/assets/023_sov_nuclear_bombs/manifest.md:5,80` explicitly excludes flags from the original Event 023 asset scope. Its current package and `gfx_handoff.md:5` cover event art, icons, and DDS registrations; live consumer review remains pending. | No J-tag ownership or protected flag asset was found. No Event 023 flag write is justified by this log. |

A bounded exact-tag search over the protected Event 006, 012, 016, and 023 asset roots returned no `JHX`, `JIX`, `JKX`, `JLX`, `JMX`, `JNX`, `JOX`, or `JPX` matches. This is a tranche ownership check, not a full-mod asset audit.

## Vanilla and offline references

The offline Country creation page requires a unique three-character tag, a linked country definition, and large/medium/small flags for each ideology (`paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md:36-42,48,324-342`). The offline Cosmetic tag page specifies the same three TGA folders and dimensions and states that ideology-specific files use `COSMETICTAG_ideology.tga`; a fallback does not override an ideology-specific base-country flag (`paradox_wiki/Cosmetic tag modding - Hearts of Iron 4 Wiki.md:22-29`). The offline Localisation page confirms that `@TAG` displays the default `gfx/flags/TAG.tga` flag (`paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:211-213`).

Vanilla `common/countries/Germany.txt` and `common/country_tags/00_countries.txt` provide the country-definition/tag precedent. The installed vanilla flag set contains `gfx/flags/GER_democratic.tga`, `gfx/flags/medium/GER_democratic.tga`, and `gfx/flags/small/GER_democratic.tga`, decoded as `82x52`, `41x26`, and `10x7`; it also contains ideology-specific neutrality and fascist/communist variants. Vanilla `documentation/effects_documentation.md:6720-6727` documents `set_cosmetic_tag`, while `documentation/triggers_documentation.md:3605-3612,6983-6988` documents `has_cosmetic_tag` and `original_tag`. These references support keeping the existing `event31_dormant_carrier_*` basenames tied to their cosmetic tags.

## Matching HOI4 MCP evidence

Because this audit traces an Event 031-owned cosmetic mapping, the required read-only event inspection and rendering routes were run for `chaosx.nr31.1`.

- `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` with trace artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b04cad3a44030ead1fd49e1ebb54ed417f3a41e67e9f968fd2df4e2f193af66/8e5af16acfc8609bd1ec44549500004fa093c55df95c49580e96cf44fb295bfc/event-trace-1102e50fad94.json`.
- `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` with overview manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77d37e79572780fbe77dedee65bcfce688910194b446e39738f52f308a369ed1/8dc5e3ebe215daff7201fd487025949821568251dece53ce265fa04b0a9d7041/event-overview-1102e50fad94-manifest.json` and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5b388f9107f2d95da48d1c71b788d8c90eb45a4a782f2436559b26af27ab0ed/520ffa6acd40d2237bcd4deae90840662bd225c99dd81088be58e8bd9a79bc07/event-overview-1102e50fad94.png`.
- Both MCP results report a focused partial analysis because the workspace graph is large and inline source inventory is truncated. They report no MCP blocker for the bounded event trace; they do not prove that direct J-tag flag files exist.
- No weighted-logic surface is in this flag tranche, so `hoi4.probability_inspect` and `chaosx_ai_probability_auditor` are not applicable here. The enabled tool inventory exposes technology inspect/render routes but no standalone Technology Tree Viewer; that viewer remains an unverified package gap and is unrelated to this flag audit.

## Likely edit order for the parent

1. Review the 48 direct-path absences and decide whether the launch errors should be resolved with new direct `TAG_ideology.tga` ladders or by ensuring the runtime reaches the existing Event 031 cosmetic tags before flag lookup.
2. If the parent selects the existing Event 031 package, accept the eight identity mappings in `common/scripted_effects/031_random_terror_effects.txt:4522-4529` and clear the manifest's `NEEDS_USER_REVIEW_IDENTITY` status through the owning asset workflow. Do not rename or duplicate those files into J-tag basenames without an accepted identity decision.
3. Keep Event 006, Event 012, Event 016, and Event 023 paths protected during any asset-owner dry-run. The current bounded scan found no overlap, but Event 012's root manifest is absent and its active handoffs are still pending live review/promotion.
4. After an owner applies an accepted asset or wiring change, re-run the exact path and log checks below. The user owns live HOI4 consumer validation.

## Parent-owned write protocol

No gameplay, GFX, source, processed, or final flag files were written by this scout. Any proposed write requires the parent/asset owner to retain the current mappings and provide:

- Dry-run: enumerate the 48 expected direct paths, confirm no pre-existing direct files will be overwritten, and show the approved source-to-runtime mapping.
- Review: verify Event 006/012/016/023 protected roots are untouched and that direct-tag versus cosmetic-tag ownership is explicit.
- Apply: add only approved asset files or parent-owned cosmetic wiring through the normal workflow.
- Post-validation: inspect TGA type/descriptor/dimensions, compare source/processed/final hashes, rerun the exact `flagtextureatlas` extraction, and perform the user-owned live consumer check.
- Rollback/recovery: remove only newly added direct J-tag files or restore their pre-apply checksums; preserve all existing `event31_*` ladders and protected event packages.

## Validation checks

- `rg -o 'Error loading flag for country [A-Z0-9]{3}[^\r\n]*Path gfx/flags(?:/medium|/small)?/' docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_07/logs/error.log | Sort-Object -Unique` should continue to identify only the eight first-tranche tags until the parent intentionally expands scope.
- Run the 48 exact `Test-Path -LiteralPath` checks represented in the missing-ladder table; after any approved write, each intended path should exist and no unintended path should appear.
- `rg --files gfx/flags | Select-String -Pattern 'JHX|JIX|JKX|JLX|JMX|JNX|JOX|JPX'` should match exactly the direct files the parent intentionally installs.
- For every accepted TGA, verify type `2`, bottom-left descriptor `0`, and dimensions `82x52`, `41x26`, or `10x7`; keep source and final hashes in the owning manifest.
- Recheck `common/scripted_effects/031_random_terror_effects.txt:4522-4529` against any cosmetic mapping change and preserve the Event 031 manifest/audit status.

## Risks and blockers

### Confirmed blockers

- All 48 direct runtime paths requested by the launch log are absent.
- The existing Event 031 candidate ladders are cosmetic-tag assets with identity review still pending; they do not prove that direct J-tag basenames are valid.
- The parent must choose direct-tag identity/source ownership or an accepted cosmetic-tag activation/wiring path before an asset owner can apply anything.
- Event 012 has no root `docs/assets/012_africa/manifest.md`; its high-chaos flag evidence is distributed across per-identity source/processed folders and current handoffs.

### Ordinary risks

- HOI4 prefers ideology-specific flag names when they exist, so adding only a default `TAG.tga` would not address the six ideology-specific requests shown in the log.
- Event 031's visual audit passes the ladders, but `NEEDS_USER_REVIEW_IDENTITY` remains a real source-of-truth gate.
- The MCP event trace/render is partial workspace evidence and is not a flag-file existence check.

## Recommended next action

Parent should review this report and choose the direct-tag versus cosmetic-tag route. The only pre-existing exact one-to-one candidates are the eight Event 031 dormant-carrier ladders listed above; install or wire them only after the parent accepts their identity ownership and records the resulting dry-run.
