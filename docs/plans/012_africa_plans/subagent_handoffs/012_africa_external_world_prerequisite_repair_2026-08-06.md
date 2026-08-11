# Event 012 External World Focus Prerequisite Repair Handoff

Status: complete for the five parent-requested Event 012 world-tree prerequisite blocks.

Scope: only the malformed prerequisite declarations at the requested source locations were changed. No unrelated tree, focus reward, AI weight, icon, localisation, layout, decision, or event content was edited.

## Grammar basis

The offline national-focus reference states that one `prerequisite` block containing multiple `focus =` entries is an OR, while multiple `prerequisite` blocks are AND (`paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:234-240`). Vanilla uses the same form, for example `game:common/national_focus/abdacom_shared_branch.txt:591` and `game:common/national_focus/baltic_shared.txt:3124`.

The previous `prerequisite = { OR = { focus = ... } }` form was therefore replaced with one direct prerequisite block containing the same focus entries. The authored OR route meaning is preserved while the MCP focus parser can resolve the parent block.

## Changed files and focus identifiers

| File and line | Focus id | Before | After |
| --- | --- | --- | --- |
| `common/national_focus/012_africa_world_asia_focus.txt:185` | `africa_asia_food_river_and_monsoon_board` | `prerequisite = { OR = { focus = africa_asia_federal_centres_chamber focus = africa_asia_congress_of_revolutionary_republics focus = africa_asia_regional_imperial_chambers focus = africa_asia_liberation_council focus = africa_asia_publish_celestial_covenant_law } }` | `prerequisite = { focus = africa_asia_federal_centres_chamber focus = africa_asia_congress_of_revolutionary_republics focus = africa_asia_regional_imperial_chambers focus = africa_asia_liberation_council focus = africa_asia_publish_celestial_covenant_law }` |
| `common/national_focus/012_africa_world_europe_focus.txt:182` | `africa_europe_common_army_and_air_defence` | Nested `OR` wrapper around six route-institution focuses. | One direct prerequisite block with the same six focus entries. |
| `common/national_focus/012_africa_world_north_america_focus.txt:329` | `africa_north_america_resources_and_withdrawal_law` | Nested `OR` wrapper around five route-institution focuses. | One direct prerequisite block with the same five focus entries. |
| `common/national_focus/012_africa_world_oceania_focus.txt:343` | `africa_oceania_ocean_constitution_and_withdrawal_law` | Nested `OR` wrapper around five route-institution focuses. | One direct prerequisite block with the same five focus entries. |
| `common/national_focus/012_africa_world_south_america_focus.txt:373` | `africa_south_america_resource_and_debt_sovereignty_law` | Nested `OR` wrapper around six route-institution focuses. | One direct prerequisite block with the same six focus entries. |

No focus entry was added, removed, reordered, or renamed.

## Route behavior before and after

Before the patch, the five convergence focuses were intended to unlock after any of their route-institution focuses, but MCP classified the nested wrapper as malformed or unreachable. After the patch, each focus has one valid OR prerequisite block, so completion of any listed route-institution focus satisfies the prerequisite while the existing `available` gates, completion rewards, and `ai_will_do` blocks remain unchanged.

The five route sets remain:

- Asia: federal centres, revolutionary republics, regional imperial chambers, liberation council, or Celestial Covenant law.
- Europe: federal chamber, republics congress, council of crowns, emergency command statute, sovereignties council, or nonhuman compact law.
- North America: bicameral congress, council of governments, civilian command statute, workers and republics congress, or Storm Containment law.
- Oceania: federal island chamber, dominion island council, peoples ocean congress, workers and ports congress, or Deep Sea Containment law.
- South America: republican chamber, council of three regions, workers and communes congress, civilian command statute, council of realms, or Sun Covenant law.

## MCP inspect and render evidence

The installed MCP exposes `hoi4.focus_inspect` and `hoi4.focus_render`, but no standalone `hoi4.focus_lint` route was available in the tool inventory. Focus inspection returns the structural diagnostics used as the lint-equivalent check; the exact unavailable lint route is recorded rather than substituted with source-only claims.

| Tree | Inspect artifact and result | Tree-local diagnostics after patch | Render evidence |
| --- | --- | ---: | --- |
| Asia (`africa_asia_world_focus_tree`) | [focus-inspect.63f07b69e25093d6.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54b356f1e723a88e384db639530f4f5c1094ac27b557be8600f06da2f9f4f65f/93e97f04afde0052b75e642a8c0a4e99d91e2460a3b5b1ee91242b276a0f5235/focus-inspect.63f07b69e25093d6.json); 20 focuses, no malformed/unreachable prerequisite diagnostic | 3 repeated-reward warnings | [render JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ada8efce654671352630b9d9e0c43902de5e3bc953183c5998917252d91af516/db7a839a71bd586d3089db61d2d3417edd1798a81bfd235aa908ff5b17ce823f/africa_asia_world_focus_tree.focus.json) |
| Europe (`africa_europe_world_focus_tree`) | [focus-inspect.63f07b69e25093d6.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/75a9ac61086f80af77424590d2ad40f78a2dc2cacc9ce046425740d741747e10/9a271eaafd0b2415758c668994ec2ef91485bca687f7d06323702f92d41384bf/focus-inspect.63f07b69e25093d6.json); 20 focuses, no malformed/unreachable prerequisite diagnostic | 5 layout detour/zigzag warnings | [render JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ba5d617ce5daa1ca7f196144355741837e1851a4eec609d2f8cd82677e5ac26/707c741156b4dccd64e50333fb64c64b0c06558a623e25ea95c45be9b8a5c2f5/africa_europe_world_focus_tree.focus.json) |
| North America (`africa_north_america_world_focus_tree`) | [focus-inspect.63f07b69e25093d6.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d43fce08b2fc0172d3203ce358cc2b2f030b251950e84b939e173b8d1c380f76/b118cbeeb0f27c65ae2f6d0049ddd579ca5fc6d02acccb0762262fc1a02be47f/focus-inspect.63f07b69e25093d6.json); 20 focuses, no malformed/unreachable prerequisite diagnostic | 3 layout detour warnings | [render JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e46842b5cfeb35660ea58677ef343801328a0dbd6e522629ee4c001b5cf52983/c963265d46636cbac1bde4af667eea0973deef14ae828df76faaf56f7dba27c6/africa_north_america_world_focus_tree.focus.json) |
| Oceania (`africa_oceania_world_focus_tree`) | [focus-inspect.63f07b69e25093d6.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d587701d1dce31aec907539497b5e49fbed1814e299e75ec0a828846fcc76f0c/7f82112395d904c97850409472f09452a30a9d31ad43cefd2add430e2aa7ca77/focus-inspect.63f07b69e25093d6.json); 20 focuses, no malformed/unreachable prerequisite diagnostic | 4 layout detour warnings | [render JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07d1241a5d46a4c86552ae50d1510f2df0b7f8b89e2d69ae2caec9162f693c2c/771589feaee5a6535be03b6fc8a58229afc85a5c57d2ee963e57de8470e94f1a/africa_oceania_world_focus_tree.focus.json) |
| South America (`africa_south_america_world_focus_tree`) | [focus-inspect.63f07b69e25093d6.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9cf676b1b01da29b87362491304cedcb071674b3a8a2801eff4cfc1981d3950/224eb30394ca2372a3e3418145c26dd1a3a1c8919ced6f0ac3b5924da4e8c736/focus-inspect.63f07b69e25093d6.json); 21 focuses, no malformed/unreachable prerequisite diagnostic | 1 layout detour warning | [render JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10a6a3cbe451074a545a5f99851d19c3f76e475aeda595a53a85894615113226/0bed4c3767f10e51072fd8bc016ee8b4f8acbb3843e618662c699484c85bc8dd/africa_south_america_world_focus_tree.focus.json) |

All five inspections returned `FOCUS_INSPECTED` and all five renders returned `FOCUS_RENDERED`. The global validation check remains false with 14 blocking diagnostics because the tool scans unrelated vanilla continuous-focus icon/localisation references; no remaining malformed or unreachable prerequisite diagnostic points to the five patched blocks.

## Validation and skipped checks

- Source check: no `prerequisite = { OR = {` block remains in the five requested Event 012 world files.
- MCP focus inspection: completed for all five trees after the patch, with route-local diagnostics recorded above.
- MCP focus rendering: completed for all five trees at `reviewScale = 0.5`; render JSON artifacts are linked above.
- Standalone MCP focus lint: unavailable; `hoi4.focus_inspect` diagnostics were used as the available lint-equivalent route and the exact capability gap is recorded above.
- Probability audit: skipped because no AI weight or probability-bearing modifier changed.
- Live HOI4 runtime/save validation: skipped because gameplay validation belongs to the parent/user and agents must not launch HOI4.

## Remaining risks

- Existing layout detour and repeated-generic-reward warnings remain in the five trees but are unrelated to the repaired prerequisite grammar.
- Global MCP validation still reports the tool's pre-existing continuous-focus reference diagnostics; these are outside the requested five Event 012 files.
- Parent review is still required before commit because the working tree contains concurrent Event 012 work.
