# Event 016 Directorate GUI overlap repair handoff

## Scope and ownership

This handoff covers Event 016, `brilliant_scientist`, and only its dedicated Kruger Directorate decision-category surface.

Ownership is explicit in source: `brilliant_scientist_directorate_category` in `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt` attaches `scripted_gui = brilliant_scientist_directorate_scripted_gui`; that definition in `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt` declares `window_name = "kruger_directorate_container"`; the window is defined in `interface/016_brilliant_scientist_directorate.gui`.

No event outcomes, decisions, costs, AI, project effects, balance, shared GUI framework, portrait identity, or unrelated UI were changed.

## Exact identifiers and files

- Decision entry: `brilliant_scientist_directorate_category`.
- Scripted GUI: `brilliant_scientist_directorate_scripted_gui`.
- Window: `kruger_directorate_container`.
- Layout: `interface/016_brilliant_scientist_directorate.gui`.
- Presentation wiring: `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.
- GFX registry inspected: `interface/016_brilliant_scientist_directorate.gfx`.
- Localisation: `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml`.
- Final-art files supplied concurrently by the asset owner and not edited by this GUI worker: `gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds` and `gfx/interface/016_brilliant_scientist/directorate/directorate_compact_header.dds`.
- Primary background sprites: `GFX_kruger_directorate_background` and `GFX_kruger_directorate_compact_header`.
- Other event-owned sprite families inspected: `GFX_kruger_directorate_profile_*`, `GFX_kruger_directorate_mandate_*`, `GFX_kruger_directorate_dependence_*`, `GFX_kruger_directorate_exposure_*`, `GFX_kruger_directorate_capacity_*`, `GFX_kruger_directorate_control_*`, `GFX_kruger_directorate_project_*`, `GFX_kruger_directorate_facility_*`, `GFX_kruger_directorate_contact_*`, `GFX_kruger_directorate_sovereignty_*`, `GFX_kruger_directorate_singularity_*`, tab/open/close/animation controls, and their animated/static marker pairs.

Files changed by this GUI worker:

- `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.
- `interface/016_brilliant_scientist_directorate.gui`.
- `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml`.
- This handoff.

## References inspected

- Repository `AGENTS.md`.
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, including scripted-GUI layout, action integrity, value/action budgets, background-first layout, and interactive state rules.
- `.agents/skills/chaos-redux-events/SKILL.md` for event ownership and player-facing writing.
- Offline `paradox_wiki/Interface Modding - Hearts of Iron 4 Wiki.md` and `paradox_wiki/Scripted GUI Modding - Hearts of Iron 4 Wiki.md`, plus the repository-required core wiki pages.
- Installed vanilla `common/scripted_guis/_documentation.md` and related interface documentation.
- Vanilla scripted-GUI precedent including `RAJ_tax_fraud_scripted_gui.txt`, which uses individual `<element>_visible` triggers in a `decision_category` consumer.
- The user-supplied live screenshot `C:/Users/klimp/AppData/Local/Temp/codex-clipboard-8e14b4ee-c1f9-414f-9f30-1304bfb8569c.png`.

## Root cause and repair

The live decision-category consumer rendered all five nested lower content containers simultaneously at `x = 40, y = 344`. Container-level visibility was therefore not a reliable exclusivity boundary in this consumer. The Authority label also lacked its own availability visibility trigger, allowing it to detach from the hidden Authority control.

The repair keeps the nested containers only as coordinate anchors and gates every painted child directly through supported scripted-GUI element visibility triggers. Overview, Projects, Facilities, Foreign, and Authority are mutually exclusive at the actual elements that paint text, cards, meters, indicators, and animations. No-tab state resolves to Overview only. Authority button, label, panel children, singularity indicator, and armed animation hide when the sovereignty surface is unavailable. Compact/full visibility is likewise applied to individual painted children, so a collapsed record cannot leak the full window.

Project-only animated/static markers require the Projects state. Authority-only singularity markers require the available Authority state. Warning animations require the full state. Projects replaces Exposure with Capacity rather than showing a fifth mechanic value.

Concise localisation removes the redundant project-stage count dump and repeated raw foreign/facility operation counts. The profile label is `Dr. Warren Kruger`, and its verified installed font is `hoi_16mbs`; no speculative font token is used.

## Layout and background coverage map

The fixed window is `500 x 620`.

| Painted region | Accepted bounds | GUI use |
| --- | --- | --- |
| Header | `x 38-462, y 8-65` | title, subtitle, close control; compact art supplies the collapsed header |
| Profile | `x 38-163, y 72-289` | portrait frame, portrait, concise name |
| Telemetry | `x 169-464, y 72-225` | Mandate, Dependence, Exposure or Capacity, profile condition |
| Government control | `x 169-464, y 228-292` | primary control value, state frame, warning marker |
| Navigation/content | `x 38-462, y 301-542` | five mutually exclusive view selectors and one content state |
| Footer | `x 38-449, y 552-604` | animation toggle and decision-action direction |

The hierarchy remains `kruger_directorate_container` -> compact/full coordinate anchors -> individually state-gated elements. The five lower content anchors share the same content bay intentionally; direct child gating makes that shared geometry safe.

## Information, action, and text-density audit

- Primary visible mechanic value: Government Control.
- Supporting values: Mandate and Dependence, plus Exposure in Overview/Facilities/Foreign/Authority or Capacity in Projects. Maximum simultaneous visible mechanic values: four.
- Projects retains current family/stage/status and the project ledger, but removes four redundant raw stage totals.
- Facilities and Foreign use concise status summaries instead of repeated counters already represented by the top telemetry and state text.
- Primary view controls: Overview, Projects, Facilities, Foreign, and Authority when available. Authority is absent, not disabled or detached, when unavailable.
- Supporting controls: collapse/open and animation toggle. All are wired controls; there are no fake buttons.
- Gameplay-changing controls inside the GUI: zero. Gameplay orders remain in the real decisions below the category, as the footer states.
- Spendable cost types inside this GUI: zero. Cost texticons are therefore not applicable.

## State matrix reviewed

| State | Expected visible lower content | Special behavior |
| --- | --- | --- |
| No tab/default | Overview only | deterministic fallback |
| Overview selected | Overview only | selected tab treatment |
| Projects selected | Projects only | Capacity replaces Exposure; marker animation/static fallback scoped here |
| Facilities selected | Facilities only | facility card and two concise columns |
| Foreign selected | Foreign only | contact card and concise pressure/operations text |
| Authority selected and available | Authority only | sovereignty card and singularity state visible |
| Authority unavailable | no Authority button or label | default fallback remains clean even if a stale sovereignty tab flag exists |
| Collapsed | compact header only | all full-window children suppressed |
| Animations on/off | animated/static counterpart only | warning/project/singularity elements retain the same bounds |
| Warning/active/completed/empty/crowded/long text | state-specific visuals within the same bays | no additional controls or value dumps introduced |

The resolution matrix covers `1366 x 768`, `1920 x 1080`, and `2560 x 1440` at UI scale 1, including the screenshot-sized decision-category consumer geometry.

## MCP evidence

### Before

- Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
- Inspect revision: `94db0db38bc6838d1c02a8f84163ddd19be09d46c696c1711106c235cb0868c2`.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5705f590e202f9d9004aa041e1d89e00191c0a443b75c0eacccf3977aa6af4b7/f5b9a388123374aa720e82696b6f55a9206a5794811e127ebccad26c86913e5b/gui-inspect.94db0db38bc6838d.json`.
- Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/106022a3f02aced985b24f90b579d22661b5859b8ee03d7407bcea2c624d1aa7/eae4f64134e7f1f4518606c599b96cfdfaeb4cfeeab57feaa26c028a0ed46d73/kruger_directorate_container-full.svg`.
- The pre-change matrix included full/cropped/annotated/hierarchy/click-region/comparison views; normal, hover, selected, disabled, warning, active, completed, empty/full-list, long-text, default, all five tabs, collapsed, animations off, and sovereignty available/unavailable scenarios; and all three required resolutions.

### After logic and localisation repair

- Inspect revision: `9c018e5a68cbcf5eb83f7399466c88917f51178a305504cdffbe95b80fd66887`.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0948ff907b113264dd309303ea90bc2cfb7b2df8efb55552cad776e945bd731d/b7190e823c3bb434f771110ac262463e9d19b84490f14c05c412adffe1af64cf/gui-inspect.9c018e5a68cbcf5e.json`.
- Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/104ed1080bceebdf7f985af4f4d1be654bd33eb3abd096f4153c46de2b93f716/c33c262f3def03b3622d44cb0825957eb1fe53835fccca114ad784ef15e35058/kruger_directorate_container-full.svg`.
- The post-change matrix repeated the pre-change states, hierarchy, click regions, comparison modes, resolutions, and screenshot-sized geometry.

Repository-wide aggregate diagnostics reported by MCP are truncated and include unrelated GUI surfaces; they are not treated as a bounded Event 016 overlap verdict. Event 016 acceptance uses the exact selector, state matrix, generated images, and source ownership above.

### Rewrite route limitation

The mandatory rewrite route was invoked and reviewed, but the server did not accept this existing structure:

- Using the scripted-GUI text file as the main package returned `GUI_TEXT_PACKAGE_PATH_UNSUPPORTED` because the route requires a `.gui` main path.
- Using `interface/016_brilliant_scientist_directorate.gui` with the scripted-GUI file as an additional source returned `REWRITE_STRUCTURE_LIMIT`.
- An exact-patch request limited to verified font changes also returned `REWRITE_STRUCTURE_LIMIT`.

The repair was therefore applied with a bounded source patch after the mandatory rewrite attempts. This is an MCP route limitation, not a substituted claim that the rewrite succeeded.

## Final-art review

The first generated background candidate was rejected during integration review because its edge machinery crossed the accepted profile and content bounds and its center did not preserve the six layout bays. The accepted revision keeps generated machinery outside the live rectangles and clears the exact header, profile, telemetry, control, content, and footer bays with a subdued texture sampled from the same generated source.

The installed runtime DDS files were decoded directly after the final replacement. `directorate_background.dds` is `500x620`, SHA-256 `67F61250E94FB09C21BB247C84007F2962ADD93D933817EFA710C71AE5A469CD`; `directorate_compact_header.dds` is `500x58`, SHA-256 `F9ADEB2EE628DBBC5FD3F343E3D831930B133259E100932D2B92C43565791624`. The accepted safe-bay contact sheet is `docs/assets/016_brilliant_scientist/directorate_ui/background_refresh/contact_sheets/directorate_background_refresh_contact_sheet.png`, SHA-256 `B2EBFE40F1D9D1203FB1D6808EEA5333A918B73CEB6E3CBC4A1C07D32A4570E2`.

A fresh post-art `hoi4.gui_inspect` call was attempted against scenario `E16_DIRECTORATE_FINAL_2026_08_15`, but the server timed out after 180 seconds. A narrower final render for scenario `E16_DIRECTORATE_FINAL_ART_2026_08_15` then completed with `GUI_RENDERED` at `1366x768` and `1920x1080` for normal and long-text states. Its full artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d172c37eeb36f115cf21417531f61bd5752661212eea675d9b98cddae4d1dedf/e2ef4dd3556624d2fc02f97069f31a6ec5350919b998d7516472402bdc0e5a07/kruger_directorate_container-full.svg`, SHA-256 `D172C37EEB36F115CF21417531F61BD5752661212EEA675D9B98CDDAE4D1DEDF`. The completed post-logic MCP state/resolution matrix remains the full state evidence; the direct final-DDS decode and safe-bay contact sheet remain the final-art evidence.

## Remaining parent-owned validation and risks

- Parent/user-owned live consumer acceptance remains outstanding for click-region alignment and the five mutually exclusive tab states.
- The final post-art inspect timed out after 180 seconds, but the narrower post-art render completed. Direct runtime DDS decoding is retained alongside it as the truthful texture evidence.
- No gameplay or balance validation is required from this presentation-only repair because no gameplay logic, costs, AI, effects, or outcomes changed.

## Simplifications, omissions, and blockers

No design simplification or fallback was introduced. Tooling exceptions are the documented `hoi4.gui_rewrite` structure limitation and the final post-art inspect timeout; the narrower final render completed successfully. The final art itself passed direct runtime decode and safe-bay review.
