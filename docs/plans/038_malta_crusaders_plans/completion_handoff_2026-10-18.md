# Event 38 completion handoff, 18 Oct 2026

Disposition: implemented (phase 2), design acceptance unchanged from `docs/events/038_malta_crusaders.md`. The package was written on 2026-10-11 by a session that never committed it. The user approved finishing and committing it on 2026-10-18. Nothing here was observed in game beyond the launch check below.

## What was committed

Phase 2 of Event 38: the two focus trees, the five government identities with their cosmetic tags, the seven principality carriers with their history files, the principality decisions, effects and triggers, the governance effects, and the updates to the phase 1 files that those parts need (characters, ideas, decisions, categories, mtth, constants, cost and core effects, scripted localisation, triggers, events, localisation).

| Area | Files |
| --- | --- |
| Focus trees | `common/national_focus/038_malta_crusaders_focus.txt` (`malta_crusaders_focus_tree`, 108 focuses), `038_malta_crusaders_principality_focus.txt` (`malta_principality_focus_tree`, 39 focuses), two focus localisation files |
| Countries | `common/countries/038_malta_crusaders_cosmetic.txt` (`CRU_ORDER`, `CRU_CONFED`, `CRU_KINGDOM`, `CRU_HOLYSEE`, `CRU_GOD`), seven `038_malta_crusaders_principality_*.txt` carriers, `common/country_tags/038_malta_crusaders_principality_countries.txt`, seven `history/countries/MQ* - Malta Principality *.txt` |
| Scripts | governance and principality effects, principality decisions, principality constants, plus edits to the phase 1 files listed in the commit |
| Flags | `gfx/flags/CRU_ORDER.tga`, `CRU_CONFED.tga`, `CRU_GOD.tga` with `medium/` and `small/` variants |
| Shared | `localisation/english/chaosx_countries_l_english.yml` (names and adjectives of the new tags, Malta hunks only), `common/synchronized_dynamic_tokens/chaosx_runtime_tokens.txt` (29 runtime-built tokens) |
| Docs | `docs/events/038_malta_crusaders.md` (phase status, phase 2 section, assets), this file |

## Defects fixed

- `mpf_council_of_admirals` referenced a sprite that does not exist (`GFX_goal_generic_build_nay`); it now uses `GFX_goal_generic_build_navy`. This was found after the first commit and fixed in a second commit.
- The three flags `CRU_ORDER`, `CRU_CONFED` and `CRU_GOD` had their medium and small variants stored in `gfx/flags/` as `<TAG>_medium.tga` and `<TAG>_small.tga`, where the engine does not look. They are now `gfx/flags/medium/<TAG>.tga` and `gfx/flags/small/<TAG>.tga`.
- `chaosx.nr38.40.d` used a colour code in a report event text (`SCRIPT_NEWS_TEXT_COLOUR_CODE`); the code was removed.
- The runtime-built names (`malta_pr_leader_*`, `malta_pr_officer_*`, `malta_pr_pressure_*`, `malta_seat_*`, with `_senior`) are now listed in the synchronized token file so multiplayer clients allocate them identically.
- Header comments of the cosmetic and principality tag files said the flags were still needed; they now describe the existing files.

## Left out of the commit on purpose

These files have no registration or consumer. They were made for the deferred parts and stay untracked on disk:
`gfx/event_pictures/038_malta_crusaders/super_event_038_eleventh_return.dds`, `gfx/event_pictures/news_event_038_crusade_begins.dds`, `gfx/interface/decisions/038_malta_crusaders/mission_*.dds` (six; the only mission sprite in use is `038_mission_protect_corridor_v5.dds`), `gfx/interface/factions/038_malta_crusaders/holy_world_faction_emblem_terminal.dds`, `gfx/interface/technologies/038_equipment_*.dds` (seven). Wire them when the super event, the Holy World faction and the custom equipment ship.

`common/achievements/chaos_redux_achievements.txt` has uncommitted hunks, but none concern Event 38; the three Event 38 achievements are already in HEAD.

## Checks that answered a question

- `hoi4.script_validate` (file mode) on both focus trees, the principality and governance effects, cost effects, both decision files, the principality triggers and the events file: no findings except the colour-code warning above. Argument blocks are not checked by that tool, and effect and trigger files report unresolved scope roots, so this is syntax, command-kind and declared-scope coverage only.
- `hoi4.focus_inspect` on both trees: both parse, 108 and 39 focuses, no node intersections; the principality tree has 3 connector crossings. The one blocking diagnostic is in a vanilla file.
- Static audits on the working tree: asset wiring (0 unresolved references, 0 implicit lookups missing) and localisation (0 parse errors, 0 missing BOM, 0 undefined key bindings).
- HEAD consistency. Before committing, the commit set was overlaid on an export of the previous HEAD and the committed files were scanned for tokens defined only in other uncommitted working-tree files, and for undefined effect or trigger calls, focus, idea, character and event ids, constants, mtth entries and scripted-localisation getters: clean. After committing, the asset wiring and localisation audits were run on a fresh export of HEAD. They found one Event 38 defect: the focus `mpf_council_of_admirals` used the sprite name `GFX_goal_generic_build_nay` (the vanilla texture file is misspelled, the sprite is `GFX_goal_generic_build_navy`); it now uses the vanilla sprite. The working tree had masked this through an alias that another session added to `interface/chaos_focus_icons.gfx` and has not committed. The remaining HEAD findings do not concern Event 38 (a flag in `chaosx_liberation_release_triggers.txt`, owned by another session).
- Hands-off minimized launch of the working tree (`-quickstart -start_tag=GER`): menu reached after 176 s, `error.log` and `text.log` both empty, no crash directory. The launch ran before the sprite-name fix above.

## Not verified, not done

- Weighted logic (`common/mtth/038_malta_crusaders_mtth.txt`, focus and decision `ai_will_do`) was reviewed by hand by the original session; no `chaosx_ai_probability_auditor` run was made.
- Engine behaviour of principality creation (`create_dynamic_country` on the MQ* carriers, the cosmetic tag switch on the revived `MLT`, `load_focus_tree` at charter) is source-reviewed only.
- Still deferred by decision (unchanged): custom unit families and counters, hidden Teutonic and Atlantis routes, Holy World terminal and scenario, super-event quotes and audio, the Crusade Council window, officer portraits.
- The spreadsheet row of Event 38 and the Formables cluster row are not edited; run the spreadsheet worker and `python .tools/export_event_catalog_csv.py`.
