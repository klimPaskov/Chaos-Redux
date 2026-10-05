# 017 A Faction Comes Calling release review, 2026-10-05

Status: source repairs implemented; release sign-off remains incomplete because required current-source MCP and live evidence is unavailable.

## Accepted decisions and implementation

- Accepted under the user's 2026-10-05 G2, G3, G6 and G7 authority: article-independent faction news, one regional cascade summary, and explicit failed-offer feedback.
- Implemented: ordinary accession news says that a country has aligned with the current faction name and uses a short country-only headline.
- Implemented: cascade participants suppress individual world accession news, and one regional summary reaches eligible human countries.
- Implemented: faction offers are collected before the pending-choice lock is set, and rebuilding a stale offer releases and reacquires that lock.
- Implemented: .90 explains failed manual preparation, unavailable offers, and a stale choice with no replacement.
- Implemented: decision stability and war-support charges have correct texticons and full cost tooltips.
- Existing faction discovery, strategic reach, costs, pressure outcomes, ideas, achievements and Event Log actor binding were retained.
- No gameplay route or runtime asset was replaced.

## Owned files and surfaces

- `events/017_join_faction.txt`
- `common/scripted_effects/017_random_faction_effects.txt`
- `localisation/english/017_join_faction_l_english.yml`
- `docs/events/017_random_faction/overview.md`

## Evidence and limits

- Live baseline: evt017_pop00.png and evt017_sheet.jpg show one accession world-news popup and the confirmed Siam/Allies grammar defect.
- Parent reviewed the full-resolution popup and all four event contact sheets.
- Offline Event modding lines 117-150, revision 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d, were read for triggered events and major broadcasts.
- Installed effects_documentation.md lines 5053-5074 and vanilla NewsEvents.txt news.1 were read for the country-scope news precedent.
- Current report_colour_audit.py reports zero coloured parchment keys, including shared news aliases.
- Event inspection/render and probability requests timed out after 600 seconds, so branch delivery and normalized AI probabilities remain unverified.

## Exact orchestrator checks

- Load qa_001_fresh_head as USA and force Event 017 from Settings: expect one accession world news sentence that reads correctly for Allies, Axis, Comintern or a custom faction name.
- As an eligible human minor, fire chaosx.nr17.1: expect one faction choice with one to four short Join options.
- Invalidate its offered faction leaders and choose fresh terms: expect replacement offers for the same minor, or one No Faction Agreement report with obsolete pressure cleared.
- Run one Evolution III cascade with several reachable neutral governments: expect one regional summary rather than one world-news popup for every accession.
- Open Event Log and Event Details: confirm the original event name, actor flag, faction result and evolution rows.

## Catalog and assets

The catalog workbook and exports were not edited.
Catalog alignment notes are in catalog_changes_pending.md.
Existing runtime art, sound, flags, portraits and models were reused.
No live HOI4 session or desktop window was opened by this task.

## Required reference evidence

- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:117-150`, local source SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:303-328`, local source SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:2943-2967`, local source SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:5053-5074`, local source SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:3624-3640`, local source SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.

Reference context/search/read routes returned some citations; failed and omitted sections were read locally.
Context inventories do not establish rule or engine coverage.
The connected service version and standalone viewer availability were not independently confirmed.
No repository-wide state-flow or helper-expansion query was used.
