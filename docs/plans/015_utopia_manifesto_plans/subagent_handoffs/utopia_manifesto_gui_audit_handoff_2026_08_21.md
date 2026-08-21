# Event 015 Utopia Manifesto GUI audit handoff

## Scope and verdict

This audit covers only Event 015, `utopia_manifesto`, and its decision-category Commonwealth Ledger.

The exact scripted GUI is `utopia_manifesto_ledger_scripted_gui`, and its exact window is `utopia_manifesto_ledger_container`.

The GUI is event-owned because `utopia_manifesto_ledger_category` in `common/decisions/categories/015_utopia_manifesto_categories.txt` attaches `scripted_gui = utopia_manifesto_ledger_scripted_gui`, whose `context_type = decision_category` block resolves to `window_name = "utopia_manifesto_ledger_container"`.

No other Utopia Manifesto decision category attaches a scripted GUI.

The Utopia super-event GUI, shared event log, event-details framework, settings UI, shared registries, and every unrelated GUI remained outside scope.

The bounded audit found one Event 015 defect: three tooltip localisation keys referenced by the current ledger layout were missing.

Those three localisation keys now exist, and the post-fix scoped checks resolve all 35 ledger localisation references.

No layout, gameplay, cost, AI, probability, decision, mission, event, focus, on-action, shared helper, shared localisation, shared GFX, or asset file was changed by this audit.

## Exact identifiers and owned surfaces

| Surface | Identifier or path | Audit result |
| --- | --- | --- |
| Event | Event 015, `utopia_manifesto` | Event owner confirmed from the accepted spec and source attachment |
| Decision-category entry | `utopia_manifesto_ledger_category` | Sole Utopia category with a `scripted_gui` attachment |
| Scripted GUI | `utopia_manifesto_ledger_scripted_gui` | Resolves with `context_type = decision_category`, human-only visibility, and AI disabled |
| Window | `utopia_manifesto_ledger_container` | Resolved and rendered as the compact `700x500` Ledger |
| Layout | `interface/015_utopia_manifesto_ledger.gui` | Inspected only; pre-existing concurrent edits were preserved and were not attributed to this task |
| Presentation wiring | `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` | Inspected only; no behavior change |
| GFX | `interface/015_utopia_manifesto.gfx` | Exact ledger sprites inspected only |
| Localisation | `localisation/english/015_utopia_manifesto_l_english.yml` | Three missing ledger tooltip keys added |
| Assets | `gfx/interface/015_utopia_manifesto/ledger/` plus exact linked Event 015 Ledger art | Inspected read-only; no art was generated, repainted, moved, or converted |

The three added keys are:

- `utopia_manifesto_ledger_gui_stores_left_tt`
- `utopia_manifesto_ledger_gui_ground_left_tt`
- `utopia_manifesto_ledger_gui_ground_right_tt`

## Required sources consulted

Repository guidance and skills:

- `AGENTS.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`

Accepted Event 015 design and prior implementation evidence:

- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_2_commonwealth_ledger.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/ledger_layout_audit_2026-08-05.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/ledger_scripted_gui_cleanup_2026-08-03.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/ledger_state_architecture_reaudit_2026_07_16.md`

Offline wiki snapshot:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- Interface modding
- Scripted GUI modding

Installed vanilla documentation and precedent:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/categories/AST_decision_categories.txt`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/AST_cabinet_trust_scripted_gui.txt`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/AST_cabinet_trust_scripted_gui.gui`

The vanilla AST cabinet-trust category confirmed the installed decision-category attachment structure: category `scripted_gui`, `context_type = decision_category`, and a named container window.

## MCP pre-change evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Pre-change shared revision: `bca29aaa350cb562d587aab0f106e2561b3d3b945833db14c300720b9f8e4b82`.

Pre-change inspect artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5916462810ffa0a1e37e69f78f8907dfb6f4d1f6dcd97b3f3ee00fafd6345ef8/7f2bb09803df161bdad17bbff7f5f2d8d0aa6341b8dbd37f652739951c71f627/gui-inspect.bca29aaa350cb562.json`

Pre-change render artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29182e68329fd1531a7a026e2b5db937a9a6bc19b2cb30734fb6d8b71447c95e/3502f1adf0dac5bb56bc6680bad0b64ce057cbf9d8a9a46db9b3b2a1b9c1fbd1/utopia_manifesto_ledger_container-full.svg`

The pre-change render request covered `1920x1080` at UI scale `1.0`, `1366x768` at UI scale `1.0`, and `2560x1440` at UI scale `1.25`.

It requested normal, hover, selected, disabled, warning, active, long-text, and missing-localisation states.

A supplementary pre-change render requested completed, empty-list, full-list, minimum-value, and maximum-value generic states in addition to the preceding matrix and produced:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c701f1fc65e69c746e5a77e58bd0417d9b93561e7da226f20d24b827fac48f78/124813086f1a8e0e54cb2b9615cd59bdb9dc515d8edcd4a0c094b4f60002dd94/utopia_manifesto_ledger_container-full.svg`

The scoped diagnosis was corroborated by the GUI validation summary, which reported exactly three `GUI_MISSING_LOCALISATION` findings before the global diagnostic collection was truncated.

The three findings matched the three exact ledger tooltip references found by the source cross-check.

## Layout hierarchy and background coverage map

The Ledger is a clipped `700x500` decision-category surface.

| Background region | Intended content | GUI elements | Interaction or state | Audit result |
| --- | --- | --- | --- | --- |
| Header, `0..700 x 0..96` | Ledger identity, title, subtitle, route emblem, formation proof | background panel, header plate, default seal, five mutually exclusive route emblems, formation-ready seal, title, subtitle, balance-shift cue | identity emblems replace the default seal; formation and balance cues are state-driven | Covered and aligned with the authored header art |
| Public values, `0..700 x 96..154` | Need, Plenty, Concord, Choice/Assignment | four `32x32` value icons and four compact value text boxes | hover tooltips provide contribution detail | Exactly four visible mechanic values, which is the accepted hard ceiling |
| Tab rail, `24..676 x 156..190` | Overview, Callings, Stores and Places, Ground and Associates | four tab buttons plus four non-interactive selected markers | one tab variable selects one panel; markers are click-through | Four real controls with matching effects and enabled triggers |
| Active panel, `24..676 x 202..424` | One of four mutually exclusive content panels | Overview, Callings, Stores, or Ground panel | only one panel is visible for a valid tab state; missing tab defaults to Overview | Panel bounds remain within the functional background region |
| Footer, `0..700 x 430..486` | current warning/status and recount action | warning animation, footer text, Recount button | warning can appear or disappear; Recount is functional and gated | Covered without exceeding the window bounds |

The authored background and card dimensions match their layout coordinates.

No control or text was placed across a newly introduced ornament, illustration, or functional anchor by this audit.

## Visible value, action, cost, and text-density audits

Visible value budget:

- Need
- Plenty
- Concord
- Choice versus Assignment

The surface exposes exactly four public mechanic values.

Each value has a stable label, an icon as a non-colour cue, a current integer value, scripted band context in its tooltip, current delta, and contribution sources.

Action budget:

- Overview tab
- Callings tab
- Stores and Places tab
- Ground and Associates tab
- Recount

There are exactly five actionable GUI controls.

All five have matching scripted effects and `_click_enabled` triggers.

The four selected-tab markers are non-interactive and click-through.

No fake, dead, or orphaned GUI button was found.

Gameplay actions remain in ordinary decisions as required by the accepted design.

Cost-count and texticon audit:

- The four tab controls spend no resource.
- Recount is an idempotent presentation refresh and spends no resource.
- No GUI control displays a spendable cost.
- The maximum GUI spendable-cost count is therefore zero, and texticon coverage is not applicable to these five presentation controls.

Text-density audit:

- The header uses one title and a two-line-capable subtitle region.
- The top values use compact visible summaries and place their detailed accounting in hover tooltips.
- The Overview and Callings panels use short visible summaries with their longer accounting in hover tooltips.
- The three repaired tooltips each contain three concise lines.
- Long-text and missing-localisation diagnostics were requested in the pre-change render matrix.
- The audit did not identify a further bounded geometry change that was proven necessary after the three missing tooltip keys were repaired.

## State matrix

| State family | Script or render evidence | Result |
| --- | --- | --- |
| Overview/default | missing tab variable or Overview constant selects Overview and its marker | Covered |
| Callings | tab constant selects the six-family Callings panel | Covered |
| Stores | tab constant selects reserve fill, seven exclusive district roles, and six district-state overlays | Covered |
| Ground with no target | `utopia_ledger_case_no_target` | Covered |
| Target eligible | `utopia_ledger_case_target_eligible` | Covered |
| Target selected | `utopia_ledger_case_target_selected` | Covered |
| Pending offer | `utopia_ledger_case_offer_pending` | Covered |
| Counteroffer | `utopia_ledger_case_counteroffer` | Covered |
| Refusal | `utopia_ledger_case_refusal` | Covered |
| Ultimatum available | `utopia_ledger_case_ultimatum_available` | Covered |
| Expired | `utopia_ledger_case_expired` | Covered |
| Stewardship active | `utopia_ledger_case_stewardship_active` | Covered |
| Associate established | `utopia_ledger_case_associate_established` | Covered |
| Warning off/on | Need, Plenty, or constitutional-crisis trigger controls the warning | Covered by source and requested warning render |
| Formation-ready | formation proof shows the dedicated seal until formation | Covered |
| Balance shift | mutually exclusive recent Choice and Assignment cues | Covered |
| District roles | market garden, industrial housing, rail junction, port town, research town, refugee municipality, inland island ring | Seven exact role sprites and visibility handlers resolve |
| District states | surveyed, planned, building, blocked, complete, disputed | Six exact overlay sprites and visibility handlers resolve |
| Disabled | all five controls use explicit click-enabled gates tied to Ledger visibility | Covered by source and requested disabled render |
| Hover and selected | buttons use HOI4 button states; selected tab has a persistent non-colour marker | Covered by requested hover/selected renders |
| Long text and missing localisation | explicit generic diagnostic states requested | Missing localisation defect identified and repaired |

The previously documented case-card and district-overlay exclusivity proofs remain consistent with the current scripted GUI.

The MCP render scenario is offline and does not simulate a live Event 015 country with every possible variable and flag combination, so the matrix combines render artifacts with exact source-state inspection.

## Sprite, font, animation, and asset audit

The final scoped cross-check found:

- 49 GUI sprite references resolved
- 48 scoped Utopia sprite definitions unique with every referenced file present
- all referenced fonts resolved through installed GUI data
- six animated Event 015 Ledger families with a registered static counterpart for each family
- background and card dimensions matching authored coordinates

The six animated families are the Ledger seal, Need warning, reserve fill, Choice shift, Assignment shift, and formation-ready seal.

No missing ledger asset, guessed path, placeholder art, repainted art, or newly generated art was introduced by this audit.

## Before and after behavior

Before:

- `utopia_ledger_stores_left` referenced `utopia_manifesto_ledger_gui_stores_left_tt`, which did not exist.
- `utopia_ledger_ground_left` referenced `utopia_manifesto_ledger_gui_ground_left_tt`, which did not exist.
- `utopia_ledger_ground_right` referenced `utopia_manifesto_ledger_gui_ground_right_tt`, which did not exist.
- Hovering those three informational regions could display a missing-localisation token or no intended explanation.

After:

- all three tooltip keys exist in the Event 015 English localisation file
- each tooltip explains the nearby values, their important causes, and why the current state matters in three concise lines
- all 35 ledger localisation references resolve
- layout geometry, click regions, scripted effects, costs, state logic, AI behavior, and assets are unchanged by this audit

## MCP rewrite record and tooling limitations

The mandatory rewrite route was attempted before the normal localisation patch.

Attempt 1 used `localisation/english/015_utopia_manifesto_l_english.yml` as the main rewrite path and returned `GUI_TEXT_PACKAGE_PATH_UNSUPPORTED` because the route requires the main text-package file to be a `.gui` file under an interface root.

It applied no change.

Attempt 2 supplied the unchanged event-owned `.gui` as the main package and the repaired Event 015 localisation as an additional file.

The package parsed but the route timed out after 180 seconds and applied no change.

The three-key localisation patch was then applied through the normal repository edit path, followed by a successful cached post-fix `hoi4.gui_inspect`.

This is a GUI-rewrite tooling limitation.

It is not evidence of a remaining Utopia layout or gameplay defect.

The MCP inspect also indexes a large shared repository graph.

Its inline collections reported global symbol collisions, unresolved references, overlaps, context diagnostics, and collection truncation from unrelated windows and files.

Those global diagnostics were not attributed to Event 015, were not modified, and do not transfer scope to this worker.

## MCP post-change evidence

Post-change shared revision: `28f1ae5094bca1e43d31c3cd7bb229e69a1053211c2a7d4e7dd66acd972c28b7`.

Post-change inspect artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d50225f5bcca59e5c139eedb0afa694ce5140a710e2412d76725b35693729519/f03819061f531acda6aec1607cdb06d7501217e285bdb2de230b9705cec6a213/gui-inspect.28f1ae5094bca1e4.json`

Post-change comparison render artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29182e68329fd1531a7a026e2b5db937a9a6bc19b2cb30734fb6d8b71447c95e/fe61d8cdeb46d0057d3990579009187859210eeecab265af327fd0327a5b4908/utopia_manifesto_ledger_container-full.svg`

The post-change render repeated the pre-change normal, hover, selected, disabled, warning, active, long-text, and missing-localisation matrix at `1920x1080` UI scale `1.0`, `1366x768` UI scale `1.0`, and `2560x1440` UI scale `1.25` with the pre-change scenario supplied as the comparison baseline.

Its SHA-256 is `29182e68329fd1531a7a026e2b5db937a9a6bc19b2cb30734fb6d8b71447c95e`, identical to the pre-change full-window render, proving that the localisation-only repair did not change geometry, hierarchy, state placement, or click layout.

Post-fix scoped results:

- 75 inspected elements
- 5 buttons with matching effects and enabled triggers
- 42 visibility references resolving to real GUI elements
- 49 GUI sprite references resolving
- 35 localisation references resolving
- exactly one Utopia decision-category scripted-GUI attachment

The before-and-after renders establish unchanged layout, hierarchy, state placement, and click geometry, while the post-change inspect establishes repaired localisation resolution.

## Files changed by this audit

- `localisation/english/015_utopia_manifesto_l_english.yml`
  - added `utopia_manifesto_ledger_gui_stores_left_tt`
  - added `utopia_manifesto_ledger_gui_ground_left_tt`
  - added `utopia_manifesto_ledger_gui_ground_right_tt`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/utopia_manifesto_gui_audit_handoff_2026_08_21.md`
  - added this audit and implementation handoff

`interface/015_utopia_manifesto_ledger.gui` contains pre-existing concurrent changes that were present before this task.

They were preserved, not reverted, and are not changes made by this audit.

## Parent-owned follow-up and remaining risks

The parent retains live consumer and in-game validation.

The offline MCP scenario cannot prove animation playback timing or every live campaign combination of tab, warning, identity, formation, Necessary Ground, district, and stewardship state.

The rewrite route could not apply the localisation-only package, as documented above.

No missing asset handoff remains, and no asset generation was routed.

No design simplification, fallback UI, extra tab, extra action, extra value, gameplay change, or unrelated-interface change was made.
