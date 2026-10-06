# Event 002 Cure Progress GUI Fresh Review

**Disposition: implemented and visually accepted for the bounded Event 002 cure panel repair.** Parent acceptance covers the 136px container, 96px body, three concise localisation changes, and the retained activation lines. Live campaign validation remains with the user.

## Ownership and acceptance basis

Event `002_zombie_outbreak` owns this panel through `chaosx_zzz_cure_category` in `common/decisions/categories/002_zombie_outbreak_categories.txt`, which attaches `zzz_cure_progress_scripted_gui` from `common/scripted_guis/002_zombie_outbreak_scripted_guis.txt`.

The scripted GUI uses `context_type = decision_category` and `window_name = "zzz_cure_progress_container"`. Its presentation-only visibility rule is `is_ai = no`, and its only dynamic property selects the cure bottle sprite. The category and all linked assets are Event 002 owned.

The parent task authorized the fresh cure-window audit. The parent then explicitly accepted the measured 96px body and 136px panel, the shorter local and shared research sentences, and the shorter final body sentence. This was the acceptance basis for the repair. The repository has no `docs/specs/002_zombie_outbreak_specs/` directory, so this handoff does not infer broader design approval from an absent specification or from implementation evidence.

The work stayed on `zzz_cure_progress_container`. The shared event log, event details, settings UI, super-event framework, shared registries, and unrelated windows were not audited or changed.

## Exact surface and source identities

| Surface | Identifier or path | Evidence |
| --- | --- | --- |
| Decision category and entry | `chaosx_zzz_cure_category` | `common/decisions/categories/002_zombie_outbreak_categories.txt` |
| Scripted GUI | `zzz_cure_progress_scripted_gui` | `common/scripted_guis/002_zombie_outbreak_scripted_guis.txt` |
| Window | `zzz_cure_progress_container` | `interface/chaosx_decisions.gui:18-50` |
| Bottle element | `zombie_cure_progress_bottle` | Dynamic property `[GetZombieCureCategoryBottleSprite]` |
| Header element | `zombie_cure_progress_header` | `zzz_cure_category_progress_header` |
| Body element | `zombie_cure_progress_body` | `zzz_cure_category_progress_body` |
| Scripted localisation | `GetZombieCureCategoryCurrentProgress`, `GetZombieCureCategoryResearchMode`, `GetZombieCureCategoryActivationEffect`, `GetZombieCureCategoryBottleSprite` | `common/scripted_localisation/chaosx_scripted_localisation.txt:35-243` |
| GFX registration | `GFX_decision_category_zombies_cure` and `GFX_decision_category_zombies_cure_0` through `_100` by tens | `interface/chaosx_decisions.gfx:31-78` |
| GUI localisation | `localisation/english/chaosx_decisions_l_english.yml:7-15` | Header, body, local/shared research, local/shared activation, and progress outputs |
| Runtime sprite family | `gfx/interface/decisions/002_zombie_outbreak/zombie_cure/zombie_cure_<0-100>.dds` | Twelve registered stage DDS files are present, each 53,388 bytes |
| Fonts | `hoi_18b`, `hoi_16mbs` | Resolved by the GUI inspect graph to installed font assets |
| Gameplay controls | None | The window has no buttons, action effects, costs, or AI actions |

The inspected script source maps local progress to `zzz_cure`, shared progress to `global.zzz_cure`, completed cure output to the `cure_activated` idea branch, and shared mode output to `is_in_tech_sharing_group = cure_sharing`. The bottle getter selects the 10-point sprite tier from these same local or shared progress branches.

The GUI GFX definitions and DDS files were read within the cure sprite family. The MCP source graph resolves the stage-zero sprite to `gfx/interface/decisions/002_zombie_outbreak/zombie_cure/zombie_cure_0.dds`, and the 46% fixtures select `GFX_decision_category_zombies_cure_40`. The older GUI handoff records that no separate Event 002 cure asset manifest or art handoff exists. No new asset was requested or produced.

Parent applied the bounded source changes to `interface/chaosx_decisions.gui` and `localisation/english/chaosx_decisions_l_english.yml`. This subagent edited no gameplay, GUI, GFX, localisation, asset, index, workbook, or commit source. The owned GUI block is 792 bytes before and after. Its SHA-256 changed from `0f99e4c183d2c495f76e81caaf572c75bcdd9db6b78ff03e4243e24932aaa733` to `e8addc315af75f0987feab8f5fa9c8958a5c216510fd2def8ba0c63bbf5822a7`.

The parent supplied the enclosing post edit file hashes: `interface/chaosx_decisions.gui` is `4a87919352be1a3748551085a34749b6bdc5f4c849a839846cef97d1a0c564ad`, and `localisation/english/chaosx_decisions_l_english.yml` is `f45dbad8b4760ded7cf0924cf6e737623c32359d9b2837c3b098b184968a93cf`. The exact GUI block and the named cure keys were reread after the edit.

## Reference and native element mapping

The prior scoped baseline is in `docs/plans/002_zombie_outbreak_plans/cure_gui_evidence/`. The fresh shared 46% production crop and the parent accepted correction overlay are in `gui_final_fresh_20261006_evidence/pre_shared46_cropped.png` and `gui_final_fresh_20261006_evidence/intended_reference.svg`. The reference keeps the existing composition and marks only the body and panel bounds relevant to this repair.

| Reference region | Native element and bounds | Content and state | Adaptation |
| --- | --- | --- | --- |
| Bottle | `zombie_cure_progress_bottle`, logical 100×100 sprite at x=8,y=4 | Local or shared progress stage from `GFX_decision_category_zombies_cure_0` through `_100` | Native `iconType`, no flattened controls |
| Header | `zombie_cure_progress_header`, x=104,y=8, width 352, font `hoi_18b` | Current progress and 100% target | Native left aligned `instantTextBoxType` |
| Body | `zombie_cure_progress_body`, x=104,y=34, width 352, font `hoi_16mbs` | Local/shared research mode, activation duration, one explanatory sentence | Native left aligned `instantTextBoxType` |
| Panel | `zzz_cure_progress_container`, x=0,y=0, width 470 | Attached below the Event 002 decision category description | No painted background or click targets |

The accepted geometry is a 96px body ending at y=130 inside a 136px container, leaving 6px below the body. The icon, header, x/y positions, width, fonts, and left alignment remain as they were.

The repair was source-only in the meaning of code ownership, not in validation. The original production render exposed the shared text overflow. The parent accepted a narrow geometry and wording change without adding controls, background art, or new state behavior.

## Documentation and vanilla precedent

The offline wiki `Interface modding` section for `instantTextBoxType` was read at lines 196-226, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`. It covers native text, font, width, height, and alignment fields.

The offline wiki `Scripted GUI modding` `decision_category` context row was read at line 157, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`. The offline wiki `Decision modding` scripted-GUI section was read at lines 225-228, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.

Installed `common/scripted_guis/_documentation.md` was read at lines 1-146, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`. It defines the `decision_category` context, category attachment, window name, dynamic properties, visibility, and UI triggers.

The vanilla precedent was `interface/sov_paranoia_system_scripted_gui.gui` with `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`. `hoi4.source_lookup` located `sov_paranoia_system_ui_window` at `game:interface/sov_paranoia_system_scripted_gui.gui:20-188`, source revision `be7c7d4da8b311bb56413bae6b367b4c0eea5a6b59970e26d916de6258d51f56`. Its decision-category GUI keeps icon and text elements separate, matching this information-only panel.

The live `hoi4.gui_inspect` and `hoi4.gui_render` schemas were discovered and used on workspace `mod_chaos_redux_ea3b2d67c2c0`. No separate health or version tool was exposed in this connected client. The reference routes, GUI inspect, and GUI render all responded on the fresh connection.

## Before and after MCP evidence

The fresh pre edit `hoi4.gui_inspect` completed with all six named scenarios and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/044fe628c088acdecd25148feb2117ee48b4d951e5ec87d5513d76c09310e944/47e21f950c6bf2116a71fdddb904d783a6a83b42518e6beb09ed2016c9aab39e/gui-inspect.a90d935007f45d4b.json`. The 477,955 byte resource was read in verified byte ranges, archived as `fresh_gui_inspect.json`, and hash checked against the URI. Its shared revision was `a90d935007f45d4bfe6f70fd2dc7e1b1d8b4d365520181292ef1b643e6f50437`.

Before the repair, the shared body measured 346×96 inside its 352×92 box for the 0%, 46%, and 100% shared profiles. The six-line shared body visibly reached the bottom boundary. The parent accepted the 4px height correction and shorter source prose.

The pre edit six fixture render completed at 1920×1080, UI scale 1, normal state, source revision `1ec03dacebe646aaa6bcb1320d1e57230edaa016116a8b07defb2fd238e4eae1`. It rendered five scenario variants plus the named comparison scenario for six source-derived cases. The stored pre full, crop, annotated, source map, hierarchy, click-region, scenario matrix, state matrix, resolution-scale, and local/shared comparison views are in the evidence folder. The scenario comparison reports 13,963 changed pixels at ratio 0.006733699845679012. It is a local-versus-shared comparison on one source revision and is not a source before/after delta.

The fresh pre direct 46% shared production image is archived as `pre_shared46_full.png` and `pre_shared46_cropped.png`. It shows the old six-line shared copy and the clipped body boundary. The scenario source and exact old copy are preserved in `pre_fixtures.json` and `text_comparison.md`.

An initial post edit inspect and render omitted the supported `is_ai` scenario fact. The inspect reported one unresolved GUI visibility condition. Those results are preserved as `post_gui_inspect_unresolved_visibility.json` and the first post route output. They are superseded.

The corrected post edit `hoi4.gui_inspect` supplied `scenario.values.is_ai = false` to each human USA fixture. It completed with `complete = true`, `fidelityCounts.unresolved = 0`, no layout diagnostics, and shared revision `726122c540c023d128dfb7369d4666068444efe6d387674b836b2042748c8a8a`. Its 477,351 byte inspect artifact was archived as `post_gui_inspect.json` and verified against SHA-256 `81f0d7c2071d731e784c596774b696745604cc2b44a0a65fe8a1ab466ec45d69`.

The corrected six fixture `hoi4.gui_render` completed on that same source revision. It returned five scenario variants plus the sixth `comparisonScenario`, one normal state, and one 1920×1080 UI scale 1 resolution. It reports no layout overflow and `fidelityCounts.unresolved = 0`. Its cross-branch comparison changed 9,288 pixels at ratio 0.004479166666666667. It is a comparison of local and shared display on the updated source.

The direct post edit shared 46% render also completed with `scenario.values.is_ai = false`, normal state, 1920×1080 at UI scale 1, and zero unresolved fidelity. The actual production image is archived as `post_46_shared_full.png` and `post_46_shared_cropped.png`. The local 46% after image is archived as `post_46_local_full.png` and `post_46_local_cropped.png`. The direct shared render source revision is `5936b0ef82f334e37375ed577d038def3b9615410edb6d50e12a443f84a6b042`. The current source file hashes and exact 792 byte window block were reread after these renders.

The route emits generic state coverage warnings for hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation. These states have no matching native controls or list in the source. The applicable mechanic states are the six explicit progress/profile fixtures. The rendered window has zero clickable elements and no list.

The exact URI and SHA records for archived source, layout, full, crop, annotated, hierarchy, click-region, and direct shared images are in `files_manifest.json`. The corrected fixture payloads are in `pre_fixtures.json` and `post_fixtures.json`.

## Visual checklist and action budget

The local 46% crop shows the shortened national research copy on one line, the unchanged 360-day activation, the final explanatory sentence, the 46% header, and the 40% bottle stage. The shared 46% crop shows the shortened shared research copy, the unchanged 120-day activation over two lines, the final explanatory sentence, the 46% header, and the 40% bottle stage. Both production crops are readable with no overlap, clipping, raw keys, or dynamic tokens.

The old shared text occupied six wrapped rows and exceeded the body height by 4px. The new shared text occupies four rows and leaves clear space below it within the expanded panel. The icon does not overlap either text column. There is no background asset or background region in this window.

This display exposes one progress measure with a 100% target, the research mode, an activation duration, and one explanatory sentence. It remains below the four-value ceiling. There are zero gameplay actions, zero costs, zero spendable cost types, and zero texticons required. Left aligned labels are the accepted source design, so button centering does not apply.

The visual checklist is complete for geometry, margins, text wrapping, clip bounds, contrast, native fonts, sprite stage selection, parent-relative placement, z-order, and click regions. The only click-region view is visually identical to the full image because this window has no click targets.

## Event behavior and integration boundary

Before the repair, local and shared profile text contained longer descriptions that produced a four pixel body overflow in the shared profile. The bottle selection and progress values were unchanged.

After the parent edit, the container height is 136px and the body max height is 96px. Local mode reads `National research. Only our findings count.`, shared mode reads `Shared research. Members combine their findings.`, and the final sentence reads `Advanced strains take longer to research.`. The 360-day local activation and 120-day shared activation strings remain unchanged. The exact source wording comparison is in `text_comparison.md`.

No gameplay effect, decision cost, AI behavior, or cleanup path is attached to this information-only GUI. The event owner retains the category gate and actual cure-sharing membership logic. The GUI scenario adapter receives the getter outputs under their source accessor names and does not establish live group membership or the `cure_activated` idea state. The parent and user retain campaign runtime validation.

No asset handoff was required. Every referenced cure stage sprite resolves. No animation is present. No fallback art, controls, or static replacements were introduced.

## Remaining limits and handoff

The MCP inspection and renderer are offline representations. They do not prove live campaign category availability, real technology-sharing membership, or possession of the completed cure idea. The corrected `is_ai=false` fact resolves the source visibility condition for the declared player fixture, but it does not replace user live-game validation.

The parent owns final integration, commit, and user evidence review. The user owns live campaign validation. No source edit or commit was made by this subagent.

Skills read for this task: `chaos-redux-scripted-gui`, `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`. No skill was created or changed.
