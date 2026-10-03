# Dormant-tag flag skill correction

Disposition: implemented within the parent-authorized narrow skill-maintenance scope.

## Ownership and change

- Updated `.agents/skills/chaos-redux-events/SKILL.md` with three sentences immediately after the country-package and static-character-history audit paragraph.
- Created this handoff only.
- Preserved the static-token recruitment and dormant-holder ownership rules and the separate pre-existing probability-guidance hunk.
- Created no skills and changed no gameplay, assets, routing definitions, or AGENTS.md.
- Left staging and committing to the parent because the skill contains another owner's uncommitted hunk.

The reusable rule requires all registered country tags, including stateless internal history holders, to have valid default and ideology flag lookup coverage across the normal, medium, and small ladders.
It points to the existing asset workflow, limits asset authorization to the native consumer package, allows intentionally shared institutional designs when documented, and requires actual TGA-header and decoded-orientation checks with direct file repair.
The rule contains no event names, country tags, private task history, or added public mechanics.

## Evidence and validation

Read `AGENTS.md`, OpenAI's `C:\Users\klimp\.codex\skills\.system\skill-creator\SKILL.md`, the events skill's country-package/static-history section, and the existing `chaos-redux-event-assets` flag workflow at lines 566–597.
The existing asset workflow already covers the three sizes, vanilla origin matching, documented byte-identical variants, and avoidance of UI orientation workarounds, so no new skill or routing change was needed.
OpenAI's `skill-creator\scripts\quick_validate.py` accepted the updated skill, and review of the resulting diff confirmed that the separate probability-guidance hunk remains intact.

Directly read `paradox_wiki\Country creation - Hearts of Iron 4 Wiki.md`, lines 461–480, SHA-256 `0c0e57915a7d1eef9ddeebe91c7329e18f4f224af98ac33fac5edd35e3aaa35d`.
Those lines document native filename lookup, ideology priority/default fallback, uncompressed 32-bit format, bottom-left origin, and the 82x52, 41x26, and 10x7 ladders.
The parent supplied user live-QA evidence of missing flag loads for a registered stateless history holder, which establishes why lack of territory does not waive the native consumer package.

Searched installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation` for flag format, dimensions, and TGA guidance and found no matching sections.
Inspected installed and repository flag files directly with Python `struct` and Pillow instead.
Every example below is uncompressed true-color type 2, 32 bits per pixel, and bottom-left origin, and its first stored BGRA pixel matches the decoded bottom-left pixel.
The installed small example uses descriptor 0 while the other examples use descriptor 8, so the rule deliberately requires the relevant format/origin properties instead of prescribing one entire descriptor byte.

| Source | Normal 82x52 | Medium 41x26 | Small 10x7 |
| --- | --- | --- | --- |
| Repository `gfx\flags\KRG.tga` and corresponding subfolders | Descriptor 8 | Descriptor 8 | Descriptor 8 |
| Installed `gfx\flags\ZIM_neutrality.tga` and corresponding subfolders | Descriptor 8 | Descriptor 8 | Descriptor 0 |

Reference file SHA-256 values, in normal/medium/small order:

- Repository: `f03f15663ffec2f00e22c8f456a3d8cf2c1ee795256d47c34edeb4ae77dc6101`, `863c53409bd8d971a04dbfe2341e3c9c67866f3e2b4bcaf8dc378d47e51f3b2d`, `ad5b87394cb26401348bfc4deb1a9bafb06e13cabcc45ffb3a08b48fffadaee3`.
- Installed: `0299ad2470cbab05b886c7869e8d60781923809aa4c93ea05b26e7abf7679cfd`, `f11563ce23dda18e2948a79777007bdf213db35be851be4c0f8bfe6afdf34af1`, `9e9a1af2e0e6fd02d94ce33b80a479055ac6de4fabf9358356baffbdaf404bb0`.

## Reference-route gap and completion limits

The parent reported that its connected tool inventory lacked `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup`.
This subagent's tool inventory exposed those names, but no live schema or reference call was negotiated for this bounded documentation correction.
The citations and binary checks above came from direct local reads, and no MCP or live-engine validation is claimed.
The initial installed `GER.tga` example was absent, so inspection used the existing `ZIM_neutrality.tga` ladder.

Skill correction completed with no simplifications.
No asset completion or engine-warning removal claim is made.
Parent review and the mixed-hunk shared commit remain parent-owned.
