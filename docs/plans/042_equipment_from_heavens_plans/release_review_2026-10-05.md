# Event 042 release review, 5 October 2026

Status: source repair completed; event release approval remains incomplete.

## What changed

The event-owned package and singular-to-plural transition are retained and repaired.
Discovery is `.2` behind hidden entry `.1`; recovery has one final summary or halt report, with three-to-seven physical visits.
All six report cards and nine achievement DDS files resolve to the event-owned GFX registry.
Dates, caller-owned temporary outputs, winner attribution, the exact growth-window boundary, accident losses, duration merging and forced-firing feedback are repaired.
No whole-world periodic hook, focus tree, decision/mission, country, portrait, world-end or super-event is introduced by this repair.

## Evidence

The fresh baseline save is `qa_001_fresh_head.hoi4`, HOI4txt, USA, 1936.1.1.12, Operation Postern v1.19.2.0.a729 (2bce).
The read-only save-inspection `info` command was used; no game was launched.
Every supplied full popup screenshot, the contact sheet and zlog screenshot was opened.
`evt042_pop00.png` is the legacy `.news.47` world-news report for the Dominican Republic; pop01-pop03 are vanilla and pop04 has no event visible.
Those screenshots do not validate the current rework.
The parsed-source recovery interpreter passes 9 tests covering counts 3-7, accident summaries, lost states, fallback states, duplicate dispatches, persistent arrays, cleanup and grant isolation.
Physical modifiers and accident equipment loss are narrow stubs in that interpreter, not engine execution.
All 27 keys from both prior localisation files are retained in the plural file, which has 190 keys.
The report colour audit returns `total keys with colour: 0`.
Fifteen DDS files were decoded and visually reviewed in `evidence/assets_contact.png`; report cards are 210x176 and achievement states 64x64.

## Source balance review

The four magnitude weight sets sum to 100: 60/30/10, 50/35/15, 40/40/20 and 35/40/25.
These are source table normalizations only, not measured campaign frequencies.
Special slot weights 40/40/15/5 imply a raw count expectation of 0.85; the allowlist contains seven distinct safe candidates.
A hazardous cargo has a 12-percent accident roll; it replaces one middle visit and removes at most one percent of the anchor stock still present plus one infrastructure level.
State burden caps at 3.0: -1.5 local supply, -24-percent building speed and -30-percent infrastructure repair before capped logistics relief.
Duration is 30/45/60 days plus a 15-day physical-theme increment; stronger/later existing burdens survive a weaker subsequent landing.
Nuclear rolls rise from 25 to 55 percent across four Chaos bands, with finite 25-250 bomb caches.
Vanilla launch requires strategic bombers, an air base, war, 20 command power and one bomb; no production unlock is granted.
AI receives identical tables, no extra crews, manpower, fuel, supply or economic bonuses.
AI strategies and all delivery weight/band tables are unchanged by the repair.

## MCP limits

The baseline event trace returned `EVENT_INSPECTED_PARTIAL`, revision 3847e34a08e7d75169959ca12d9b601e0b82e964aff636ccd37c531ff000cd41; it excludes helper projections.
The baseline probability discovery returned revision 04e8873f7664f4d19c88af5f49e93c54d47258b2313ee3ce05609d4cc0295bd9.
Multiple reference/probability calls, the probability compare, final event render and a hidden-fielding technology inspect timed out awaiting tools/call after 600s.
Shared-detail GUI inspection/render and final event compare were requested narrowly but have not yielded acceptable before/after artifacts.
No MCP visual approval, weighted balance approval, engine execution or helper coverage is claimed.
Returned citations, revisions and artifact URIs are in `evidence/mcp_parent.json` and `subagent_handoffs/probability_2026-10-05.md`.

## Remaining issues and omissions

Borrowed Nightmare still uses a stockpile-plus-army decline during war as a proxy for combat loss.
Attrition or transfers can satisfy it; native leader callbacks identify a leader and owner, not the exact participating division.
The requested exact combat-loss proof remains blocked, and no weaker requirement has been substituted.
Required final MCP comparison and shared-detail visual evidence remain open; no render artifact or validation.json was available to inspect for those calls.
Catalog wording is queued for the catalog owner under the task prohibition on workbook/CSV edits.
Existing uncommitted shared registration, log, cluster, evolution and Settings integration hunks are preserved for their owners; the isolated commit contains only this owner's one-line caller initialization in Settings.
The original uncommitted rework author could not be identified. Klim Pashkov added the plural localisation file in 794b31a7b; no historical rename commit exists.
Tier-4 airframes/jets and special families outside the verified allowlist are existing documented exclusions, not new substitutes introduced by this repair.
No additional fallback or gameplay simplification is introduced; report consolidation and within-count accident replacement are explicit G6 owner design decisions.

## Orchestrator live cases

1. From `qa_001_fresh_head`, fire 042 from Settings; note its actual Event Log recipient. Switch to that recipient for presentation checks. Expect one discovery and one final summary, one stockpile grant and one history/pacing entry. USA receives no world-news popup when another country receives the cargo.
2. On a separate fresh-USA branch, run `event chaosx.nr42.1 USA`. Hover the discovery option, confirm actual stock matches its quantities, acknowledge it, and run 45 days. Expect exactly two Event 042 popups, no duplicate grant, readable text and matching art, and final cleanup. Direct/manual delivery must not qualify for achievements.
3. In a disposable branch mark every existing country `efh_chain_active` through console evaluation, then force 042 from Settings. Expect one No Clear Landing Ground report, no equipment and no claimed successful firing. This is an artificial empty-pool fixture.
4. Start a USA delivery, acknowledge it, save between recovery visits and reload that test save. Continue 45 days. Expect the same saved manifest, one final summary, preserved state burdens and no duplicate grant.
5. In a disposable war fixture, after acknowledging discovery transfer every recipient-owned state's control to the enemy while keeping the recipient country in the war. Continue recovery. Expect Recovery Halted, no false success count, and closed chain.
6. Enable/record stages I-III in a disposable fixture and make further deliveries after each prior chain closes. When nuclear/special cargo appears, expect matching discovery art, finite equipment, fieldable recovered templates and no owner-event/production unlock. A recovery accident belongs in the single final summary and states its actual capped loss.
7. With a received nuclear cache, no nukes technology/completed bomb project, ten valid strategic bombers, a usable base, 20 CP and a wartime target, prepare and launch the vanilla nuclear strike. Expect stock reduced by one and ordinary shared fallout/Chaos consequences once, with no nuclear production unlock.
8. For Tiny Arsenal State use a player-controlled country with fewer than ten factories and an ordinary (non-manual) delivery. Reach the extra fifty divisions by day365 while holding its capital, then defeat a major by day1095. Only the actual capitulation winner or accepted-surrender receiver receives credit; a qualifying ally does not.
9. Open Event Details and each evolution toggle at 1920x1080 scale1. Verify recipient/history, three stage rows, no raw keys or exposed flag names, scrollability, fitting text, correct icons and no overlap. These are acceptance checks, not previously observed passes.

## References read locally after route gaps

- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`, 59-117,180-197: conditional descriptions, native dynamic pictures, immediate/after and hidden events; SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, 435-446,1615-1617,1729: temp call frames and equipment getter scopes; SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`, 254-255,276,498-499: winner/receiver and combat callback bindings; SHA-256 `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, 1153-1174,2943-2967: dynamic modifier and country-event delay; SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`, 184-226: arithmetic and script constants; SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`, 1-34: schema must be first; SHA-256 `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/nuclear_raids.txt`, 1-104: stockpile visibility, bomber/base/war/CP and bomb consumption; SHA-256 `966408c81eba9f5928ed352d5f95f6648977b23a8e12ce9aa2cd2cdbca76256f`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_localisation/00_scripted_localisation.txt`, 1714-1733: vanilla dynamic GFX localisation output; SHA-256 `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/00_on_actions.txt`, 5574-5610: native combat callback scopes; no participating-division proof; SHA-256 `52a751456f1774ad5001c86d41d4e46494f751d79b6c224b6cd4c0eebb615eb9`.

## Skills used

`chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-shared-git-commit`, `chaos-redux-scripted-gui`, `chaos-redux-event-assets`, `chaos-redux-save-inspection`, and `chaos-redux-native-raids`.
No skills were created or modified.

The bounded accident snippet returned MCP `SCRIPT_CHECK_PARTIAL`: syntax, command kinds and declared country scope were checked; native argument blocks were not. Installed documentation sections for set_temp_variable (7820-7827), meta_effect (4833-4852), clamp_temp_variable (2681-2694) and check_variable (2110-2135) were read directly to review those arguments. This is not an engine execution pass.
The final narrow event comparison and source lookup also timed out awaiting tools/call after 600s.

The Windows user-mapped-file write problem was resolved by a verified atomic sibling replacement. A generic skill-maintenance note is accepted and queued in `subagent_handoffs/skill_note_2026-10-05.md`; skill files were not edited because they are outside this task's file ownership. Final MCP responses are retained in `evidence/mcp_final.json`.
