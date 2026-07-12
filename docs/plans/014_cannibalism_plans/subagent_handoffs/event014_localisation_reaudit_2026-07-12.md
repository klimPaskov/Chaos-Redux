# Event 014 localisation re-audit — 2026-07-12

## Audit result

Event 014 is **not ready for a clean localisation-completion claim**. The audit found **five bounded finding groups: two P1, two P2, and one P3**.

The exact public name `Hannibal Lecter` is correctly gated behind `cannibalism_reveal_complete`; no reachable pre-reveal exact-name exposure was found. Three pre-reveal strings still foreshadow a hidden identity or later public revelation and are reported separately below. No actual ancient-general, Carthaginian, Punic, or classical framing was found in Event 014's player-facing text or inspected reveal/pre-reveal visual sources.

Audit mode was read-only. No gameplay, localisation, asset, interface, documentation source-of-truth, or spreadsheet content was changed. This handoff is the only file written. No commit was created.

## Findings

### P1 — External spread and reinfection text omits the recorded source actor and route type

The state is dynamic, but the source actor and route are not shown:

- `localisation/english/014_cannibalism_l_english.yml:608`, `chaosx.nr14.60.d`, names only `[cannibalism_spread_target_state.GetName]` and calls the cause merely “the route”.
- `localisation/english/014_cannibalism_l_english.yml:614-615`, `chaosx.nr14.61.d` and `chaosx.nr14.61.reinfection.d`, name only the target state and use “documented wartime route” or “external source”.
- `localisation/english/014_cannibalism_l_english.yml:621-623`, `chaosx.nr14.62.d` and `cannibalism_external_spread_arrival_tt`, again name only the target state and a generic inbound route.
- `common/scripted_localisation/014_cannibalism_scripted_localisation.txt:1-207` has no source-country getter or localized selector for retreat, prisoner transfer, convoy, volunteer return, occupation turnover, deliberate seed, conquest, or survivor routes.

The gameplay already preserves the missing facts. `common/scripted_effects/014_cannibalism_spread_effects.txt:380-382` and `427-429` store the warning route, source country, and source generation on the inbound state; lines `562-563` and `593-594` store the external infection source and route on the receiving country. The source design explicitly requires `Reinfected Externally | Source and route shown` at `docs/specs/014_cannibalism_specs/matrices/event_map_and_state_machine.md:29`.

Impact: countries cannot tell which actor sent the infection or distinguish the eight concrete route families in the warning, arrival, or reinfection narrative. This fails the dynamic actor/state/route and route-readability requirement even though the underlying ledger is correct.

Required resolution: add spoiler-safe route labels and source-country rendering for `.60`, `.61`, `.61.reinfection`, and `.62`, using the stored scope/route data. The pre-reveal labels must remain operational and must not infer or name the concealed leader.

### P1 — Thirteen achievements do not implement their specified staged visibility

`common/achievements/chaos_redux_achievements.txt` uses only static `hidden = yes` or no hidden field. That supports always-secret-until-earned or visible-from-start behavior, not the specified campaign-stage transitions:

- `2111-2119`, `014_cannibalism_repentant_weapon`: statically hidden; required hidden only until exploitation is selected (`spec part 11:133-135`).
- `2122-2129`, `014_cannibalism_break_the_island_host`: visible from campaign start; required visible only after the first Island Host (`153-155`).
- `2132-2174`, achievements `08` through `11`: statically hidden; required to become visible after reveal (`174-237`).
- `2176-2184`, `014_cannibalism_stop_the_reveal`: statically hidden; required to become visible when convergence begins (`256-258`).
- `2187-2195`, `014_cannibalism_defeat_hannibal`: statically hidden; required to become visible after reveal (`278-280`).
- `2198-2206`, `014_cannibalism_break_the_winter_hunger`: statically hidden; required to become visible after the alternate merge (`298-300`).
- `2209-2217`, `014_cannibalism_ordinary_world_end`: statically hidden; required to become visible after reveal (`316-318`).
- `2220-2228`, `014_cannibalism_wendigo_world_end`: statically hidden; required to become visible after the alternate merge (`334-336`).
- `2231-2239`, `014_cannibalism_global_burial_detail`: statically hidden; required to become visible once the defeat aftermath is eligible (`354-356`).
- `2242-2249`, `014_cannibalism_no_empty_state`: visible from campaign start; required visible only after Evolution II (`373-375`).

Achievements `01` through `05` are correctly visible. The static hiding of the name-bearing achievements prevents an exact pre-reveal `Hannibal Lecter` leak, but those entries do not become discoverable at their specified public stages. No alternate staged-visibility surface was found.

Required resolution: implement a real state-dependent visibility surface for these thirteen achievements or reconcile the source specification through an explicitly approved design decision. A static secret-achievement substitute is a fallback and was not assumed in this audit.

### P2 — Three reachable pre-reveal strings foreshadow the concealed identity/reveal

These strings do not expose `Hannibal Lecter`, but they tell the player that a hidden leader or later identity/revelation exists:

- `localisation/english/014_cannibalism_l_english.yml:148`, `cannibalism.evolution.summary`: “a unified command that appears only after public revelation.” It is returned for every Event 014 evolution without a reveal guard at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:6308-6309`.
- `localisation/english/014_cannibalism_l_english.yml:879`, `cannibalism_warlord_read_the_common_signs_tt`: “without exposing any later identity.” It is used by the pre-reveal warlord focus at `common/national_focus/014_cannibalism_warlord_focus.txt:1317`.
- `localisation/english/014_cannibalism_l_english.yml:1821`, `cannibalism.gui.open_network.tt`: “without naming a hidden leader.” The button is on the pre-reveal header at `interface/014_cannibalism_frontline_hunger.gui:49`, and the network GUI is explicitly pre-reveal at `common/scripted_guis/014_cannibalism_scripted_gui.txt:73-80`.

Required resolution: replace these with in-world descriptions of the evidence currently visible, without discussing later content, a hidden identity, or implementation-stage secrecy.

### P2 — Tunable costs, durations, and thresholds are not consistently dynamic in localisation

The displayed values currently agree with their script constants, so this is not a present-value mismatch. They are nevertheless duplicated literals and will silently drift when tuning changes. Event 014 already demonstrates the correct patterns through `[?constant:category.key|0]` and prepared cost variables elsewhere in the same file.

Exact affected families:

- International response and reconstruction: `localisation/english/014_cannibalism_l_english.yml:1407`, `1411`, `1415-1416`, `1419-1420`, `1423`, `1427`, `1431`, `1435`, and `1440-1441` (`cannibalism_joint_suppression_cost_text`, `cannibalism_convergence_interdiction_cost_text`, the three Island Host cost/effect families, the three reconstruction costs, and compact cost/duration). Their sources are `common/script_constants/014_cannibalism_achievement_constants.txt:63-123`.
- Warlord synchronized attack: `localisation/english/014_cannibalism_l_english.yml:574`, `cannibalism_synchronize_warlord_attack_desc`, hardcodes “thirty-day” while the effect text correctly reads `constant:cannibalism_warlord_decision.synchronized_operation_days` at line `576`.
- Unified decision fixed-value outliers: `localisation/english/014_cannibalism_l_english.yml:1491`, `1551-1568`, `1581`, `1584`, `1593`, `1595`, `1600`, `1604`, `1608`, `1612`, `1631-1632`, `1683`, `1685`, `1694-1702`, `1737`, `1739`, and `1741`. These duplicate hostility tiers, population floors and losses, receipt counts/yields, cooldowns, air gates, counterwar results, and terminal costs owned by `common/script_constants/014_cannibalism_unified_decision_constants.txt`.
- Achievement thresholds: `localisation/english/chaosx_achievements_l_english.yml:502`, `505`, `517`, `520`, `523`, `526`, `529`, `538`, `541`, and `544`. These duplicate the country, island, duration, retained-warlord, Larder, route, continent, consumed-population, Network Reach, Chaos, and compact thresholds in `common/script_constants/014_cannibalism_achievement_constants.txt:13-25` and `common/script_constants/014_cannibalism_core_constants.txt:699-708`.

Required resolution: render the owning constants or initialized runtime variables directly, keeping integral values on `|0`. Where achievement localisation cannot safely evaluate a runtime token, the implementation needs a documented staged/dynamic presentation mechanism rather than a silently duplicated literal.

### P3 — Player-facing implementation terminology and prohibited punctuation remain

Implementation-stage terminology:

- `localisation/english/014_cannibalism_l_english.yml:91`, `cannibalism_amnesty_requirements_tt`: “Evolution I evidence”.
- `localisation/english/014_cannibalism_l_english.yml:596`, `cannibalism_prison_infiltrate_transfers_effect_tt`: “generation-checked route enters the ledger”.
- `localisation/english/014_cannibalism_l_english.yml:1386`, `cannibalism_captured_warlord_anti_decapitation_escape_tt`: “character-outcome ledger”.

Semicolons or em dashes prohibited by the Event 014 writing guidance remain in these keys:

- `localisation/english/014_cannibalism_l_english.yml:362`, `cannibalism_unified_command_burden_desc`.
- Lines `514`, `519`, `524`, `529`, and `556`: `cannibalism_raise_scavenger_warband_effect_tt`, `cannibalism_raise_feast_cohort_effect_tt`, `cannibalism_raise_origin_specialist_effect_tt`, `cannibalism_raise_bone_guard_effect_tt`, and `cannibalism_seed_foreign_formation_effect_tt`.
- Line `1386`, `cannibalism_captured_warlord_anti_decapitation_escape_tt`.
- Lines `1566`, `1617`, and `1627`: `cannibalism_unified_battlefield_consumption_requirements_tt`, `cannibalism_unified_army_operation_effect_tt`, and `cannibalism_unified_naval_operation_effect_tt`.

Required resolution: rewrite these as direct player-facing world-state/effect language and split clauses with periods or commas.

## Reveal-secrecy proof

The exact public name gate is correctly ordered and enforced across the audited surfaces:

- Ordinary unification sets `cannibalism_reveal_complete` before CBL ownership, leader, portrait, name, or tree setup at `common/scripted_effects/014_cannibalism_unification_effects.txt:491-529`.
- Wendigo merge sets the same flag before identity preparation, portrait, focus, report, news, or audio-facing work at `common/scripted_effects/014_cannibalism_wendigo_effects.txt:439-455`.
- Reveal events require the flag: `events/014_cannibalism.txt:435-439` for `.70` and `537-542` for `.72`. Captured-Hannibal aftermath requires it at `events/014_cannibalism_aftermath.txt:125-137`.
- News requires it at `events/_chaosx_news.txt:1342` and `1353-1356`.
- Pre-reveal GUI surfaces explicitly require the flag to be absent at `common/scripted_guis/014_cannibalism_scripted_gui.txt:15-22`, `73-80`, and `172-176`; named portrait surfaces require it at `213-219` and `242-247`.
- Event Details selects the pre-reveal premise while the flag is absent and the revealed text afterward at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:4407-4415`.
- Evolution III title mappings are flag-gated at lines `1851`, `2861`, `4567`, and `5242`; the Evolution III body is gated at `5896`.
- All four Event 014 super-event emitters require the reveal flag at `common/scripted_effects/014_cannibalism_super_event_effects.txt:51`, `72`, `96`, and `118`.

All exact-name occurrences in Event 014 localisation resolve through one of those post-reveal country, character, focus, GUI, event, news, aftermath, achievement, or super-event surfaces. The three indirect spoiler strings in the P2 finding are the only pre-reveal secrecy defects found.

## Clean-surface evidence

- Encoding and key integrity: Event 014 main and super-event files plus related achievement, chaos-meter, event-name, and shared-GUI English files all retain UTF-8 BOM. No leading-space keys, `:0` suffixes, malformed key declarations, or duplicate Event 014 keys were found.
- Reference coverage: 975 explicit Event 014 localisation references across events, aftermath, news, GUI, scripted localisation, characters, decisions, and focus tooltips produced zero missing keys. Implicit decision/category, focus, idea, trait, dynamic-modifier, and achievement key checks also produced zero missing keys. All 281 Event 014 variable interpolation tokens resolve to variables or constants present in gameplay, and integral Event 014 values use `|0`.
- Scripted localisation: `common/scripted_localisation/014_cannibalism_scripted_localisation.txt` contains no literal `§` or `£`; country names, adjectives, party names, warlord names, stages, node types, target selection, and sort labels all have terminal/default branches. The only missing dynamic family is the source/route presentation described in P1.
- Country package: CBA-CBH have base and four-ideology name/DEF/ADJ triplets plus neutrality party short/long names. CBL has the same base coverage, three complete cosmetic triplets, party keys, and both Hannibal character-name keys.
- Focus trees: all 72 warlord, 108 unified, and 28 Wendigo focus nodes have their implicit name/description keys and referenced custom tooltips. The hierarchy, Larder, military, network, four origin, unified command, and Wendigo routes remain textually distinct; no copied-route localisation block was found.
- Decisions, missions, and GUI: all implicit names/descriptions and explicit tooltips exist. Dynamic base-event, warlord, and Wendigo costs/timers are correctly rendered except for the bounded literal families in P2. GUI labels and referenced tooltip keys are complete.
- Reports, news, super-events, and assets: all report/news picture tokens and all 224 relevant Event 014 explicit focus/report asset references resolve. Six audited Event 014 `.gfx` sources have zero missing texture files. All four super-event image selectors and title/quote/button/body mappings resolve. All 54 achievement DDS variants for the 18 achievements exist. Visual inspection of the six pre-reveal report sources and the ordinary/Wendigo reveal portrait/report/super-event sources found no pre-reveal Hannibal portrait and no ancient-general, Carthaginian, Punic, or classical motif.
- Achievements: all 18 name, description, and tooltip key triplets exist and agree with their completion triggers. The remaining achievement defect is staged visibility, plus the duplicated threshold literals reported above.
- Scenario 010: all five types and four difficulty/impact texts exist. `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Events!A15:M15` and `Scenarios!A10:F10`, exactly match the live pre-reveal premise, three evolution descriptions, two terminal super-event descriptions, five scenario-type descriptions, and four difficulty texts. Both catalog rows remain marked `Needs Testing`.
- Cleanup and aftermath: local/global victory wording, external reinfection, captured warlord/Hannibal outcomes, liberated-state recovery, identification, institutions, memorials, inspection compact, global defeat, and both terminal routes have complete keys and cross-surface wording. The remaining aftermath defects are the hardcoded costs/duration and the staged visibility of the burial-detail achievement.

## Simplifications, omissions, fallbacks, and blockers

- No audit surface requested by the parent task was omitted.
- No fallback or simplification was used or approved.
- No gameplay/localisation/assets/spreadsheet patch was made; this is an audit handoff only.
- Completion is blocked by the two P1 findings. In particular, static `hidden = yes` is not equivalent to the specified staged achievement visibility, and this audit did not silently accept that substitution.

## Skills used

- `chaos-redux-events`
- `hoi4-decisions-missions`
- `hoi4-focus-trees`
- `chaos-redux-super-events`
- `chaos-redux-subagents`
- `xlsx` for the read-only Event Catalog cell comparison

