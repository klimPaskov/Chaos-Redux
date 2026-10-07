# External evidence and source conflicts

## Connected code and documentation

Repository revision inspected: `33b6946dd923b9fc90fbf29bc5798dce3c76a76f`.

**R1. Current Event 088 implementation.** Full file read. The country event is `chaosx.nr88.1`, its option chooses `get_random_sea_region`, and a country loop invokes `add_mines` through an inline meta-effect. This supports the old-behavior diagnosis and the need to separate acknowledgment from global mutation. It does not verify the active engine's cap or mine aggregation.

`https://github.com/klimPaskov/Chaos-Redux/blob/33b6946dd923b9fc90fbf29bc5798dce3c76a76f/events/088_mines.txt`

**R2. Legacy localisation.** Search excerpt read. It describes one random sea region and has a generic acknowledgment. Replace it through the direction-only handoff after implementing the new world change.

`https://github.com/klimPaskov/Chaos-Redux/blob/33b6946dd923b9fc90fbf29bc5798dce3c76a76f/localisation/english/088_mines_l_english.yml`

**R3. Random-region helper.** The supplied Markdown helper registry was read fully and connected source search confirms a curated literal random list. The helper is not a current-map enumeration API. Its full connected TXT implementation was not fetched.

`https://github.com/klimPaskov/Chaos-Redux/blob/33b6946dd923b9fc90fbf29bc5798dce3c76a76f/common/scripted_effects/chaosx_dynamic_effects.txt`

**R4. Cluster documentation.** Connected excerpt read. It lists Sudden Abundance with Event 032 included, while the supplied cluster export omits 032. Neither observed list includes 088. The user's explicit 088 Medium assignment controls the requested change, but unrelated membership and status differences remain untouched until the workbook/runtime comparison.

`https://github.com/klimPaskov/Chaos-Redux/blob/33b6946dd923b9fc90fbf29bc5798dce3c76a76f/docs/systems/event_system/event_clusters.md`

**R5. Offline wiki references.** An Effects search excerpt states that `add_mines` adds mines to a region for the current country. A Scopes fetch was truncated after its initial portion. Map and AI searches supplied only bounded excerpts. These references help locate the native questions but do not close installed-game verification.

`paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`

`paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`

`paradox_wiki/Map modding - Hearts of Iron 4 Wiki.md`

`paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`

## Current primary public source

**W1. Official Steam store, Hearts of Iron IV.** Inspected 2026-09-22. The current listing includes Man the Guns among the expansion packs bundled with the base purchase. This is packaging evidence only. The plan does not infer exact engine version, integration date, entitlement trigger semantics or native mine behavior from it.

`https://store.steampowered.com/app/394360/Hearts_of_Iron_IV/`

**W2. Official Steam announcements from September 2025.** Read at excerpt level. They announced a future integration of Man the Guns with a November release. Those announcements are not used as proof that a particular later patch shipped or that an old installation exposes the same interfaces.

`https://store.steampowered.com/news/posts/?appids=394360&enddate=1759237531&feed=steam_community_announcements`

**W3. Official historical developer diary endpoint, Mines and Minesweeping.** Search identified the source, but the opened page did not provide a readable full body. The forum counterpart returned a challenge page. Not counted as read and not used to validate the cap, combat modifiers or sweep mechanics.

`https://store.steampowered.com/news/app/394360/view/5315892737483187030`

`https://forum.paradoxplaza.com/forum/threads/hoi4-dev-diary-mines-and-minesweeping.1115861/`

## Conflict dispositions

| Conflict | Disposition |
| --- | --- |
| User's global incident versus old random-region code | User's latest explicit requirement wins |
| User's mine event versus technology-sharing catalog description | Correct runtime wording first, then mirror it through XLSX |
| User's Medium membership versus blank event cluster cell and missing cluster member | Add/align 088 Medium through the actual authoritative registry and workbook |
| Supplied cluster export versus connected cluster document membership/status | Record discrepancy and leave unrelated entries unchanged until live comparison |
| Intended 1,000 cap versus no installed define verification | Keep 1,000 as user design target, verify actual native cap and preserve additive behavior |
| Owner fields coexist versus unverified combat aggregation | Preserve ownership contract and do not promise linear combat scaling |
| Current bundled expansion versus historical paid-DLC assumptions | Inspect the supported build's actual feature gate rather than imposing an old packaging rule |
| Old asset prose versus newer explicit achievement template/overlay path | Inspect real files and current processor, do not invent or redraw a missing template |
| Configured subagent/MCP names versus missing callable routes | Configuration read, execution not performed |
| Large skill corpus versus relevance of conditional systems | All supplied text read. Conditional instructions do not create unrelated gameplay requirements |
