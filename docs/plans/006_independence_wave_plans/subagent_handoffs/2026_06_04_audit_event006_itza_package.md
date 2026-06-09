# Audit: Event006 Itza Package

Read-only audit of the `iw_pkg_itza` Independence Wave local-polity tranche.

## Findings

No correctness findings identified for the ITZ tranche.

## Evidence

- Vanilla reuse is valid. Vanilla registers `ITZ` in `~/projects/Hearts of Iron IV/common/country_tags/00_countries.txt:316`, uses capital `311 #Belize` and comments core `311` in `~/projects/Hearts of Iron IV/history/countries/ITZ - Itza.txt:1`, `:5`, defines the council leader/portrait in `~/projects/Hearts of Iron IV/common/characters/ITZ.txt:4`, `:8`, and vanilla Chile liberation dynamically adds the ITZ core before transfer at `~/projects/Hearts of Iron IV/common/decisions/CHL.txt:6279`, `:6282`.
- The seed gate prevents capital deletion and requires a weakened host. `common/scripted_triggers/006_independence_wave_triggers.txt:355` gates tier IV/V, `ITZ = { exists = no }`, `311 = { is_capital = no }`, host control of state `311`, host survival floor, and host weakness through war, low stability, low war support, or surrender progress at `:356-371`.
- Event005 contamination is avoided through Event006 origin gating. `is_independence_wave_release` requires `chaosx_release_origin_independence_wave` and excludes Soviet-collapse/Event005 flags in `common/scripted_triggers/006_independence_wave_triggers.txt:8-13`; ITZ package checks use that trigger through `is_independence_wave_itza_package` at `:1529-1533`.
- Temporary ITZ core cleanup is correct. The seed adds only state `311` core plus `independence_wave_itza_package_core_seeded` in `common/scripted_effects/006_independence_wave_effects.txt:777-785`. Cleanup removes the core only while `ITZ` does not exist at `:873-881`; if `ITZ` exists, it only clears the temporary state flag at `:883-888`. The cleanup call runs after the release loop in `events/006_independence_wave.txt:115`.
- Release anchor and later claim logic match the intended design. The package anchor selects state `311` in `common/scripted_effects/006_independence_wave_effects.txt:435-455`; the Yucatan petition effect records state `313` as a claim target, not a free transfer, at `:2698-2703`.
- Startup identity is wired. `common/scripted_effects/006_independence_wave_effects.txt:1379-1398` sets `independence_wave_package_itza`, local-polity package flags/type, `constant:independence_wave_package.itza`, lake-council family, local-polity cohesion, and `independence_wave_itza_lake_council_spirit`.
- Focuses and decisions are coherent with nearby Miskito patterns. The ITZ focus pair is in `common/national_focus/006_independence_wave_focus.txt:1367-1414`, mirroring the Miskito setup just above it. The ITZ decisions and timed mission are in `common/decisions/006_independence_wave_decisions.txt:1872-1969`, matching Miskito costs, visibility cadence, AI weights, custom tooltips, and failure/success mission behavior.
- Event-log routing is complete. Constants are defined at `common/script_constants/006_independence_wave_constants.txt:173-174`; record effects set those types at `common/scripted_effects/006_independence_wave_effects.txt:3692-3707`; scripted localisation maps both types in current list, history detail, event detail, selected-detail title, and selected-detail body routing at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:724`, `:780`, `:1900`, `:1956`, `:2571`, `:2623`, `:3607`, `:3663`, `:3809`, `:3831`. GUI keys exist in `localisation/english/chaosx_gui_l_english.yml:294`, `:309`.
- Localisation is present and player-facing. ITZ package, idea, focus, decision, tooltip, and mission keys are present in `localisation/english/006_independence_wave_l_english.yml:81`, `:413-414`, `:443-446`, `:555-566`. I found no ITZ-facing update-history wording.
- The tranche avoided flag/country/history/tag edits. `git status --short -- common/country_tags common/countries history/countries history/states gfx/flags` reports no changes, and repo searches find no modded `ITZ` flag, country, country-tag, or history files.

## Validation Run

- Opened required offline Paradox wiki references: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.
- Consulted vanilla documentation: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `common/decisions/_documentation.md`, `common/on_actions/_documentation.md`, `common/ai_strategy/_documentation.md`, and `common/script_constants/documentation.md`.
- Compared vanilla ITZ tag/history/character/localisation/flag evidence and vanilla Chile dynamic-core release precedent.
- Ran targeted `rg` checks for ITZ identifiers across Event006 gameplay, scripted localisation, GUI localisation, docs, and parent handoff.
- Checked unsupported inclusive comparison operators across the audited Event006 files; no matches.
- Counted braces in audited script files; all checked files had matching open/close brace counts.
- Checked localisation BOM bytes for `localisation/english/006_independence_wave_l_english.yml` and `localisation/english/chaosx_gui_l_english.yml`; both begin with `efbbbf`.
- Checked `:0` localisation suffixes in the touched Event006 localisation files; no matches.

## Remaining Risks

- This was a read-only tranche audit, not a live-game balance pass. Balance still depends on the wider Event006 package pool, chaos-tier release frequency, and how often state `311` meets the weakened-host gate.
- The broader Event006 implementation remains dirty/uncommitted in the worktree; this report only assesses the ITZ package surfaces named above.
