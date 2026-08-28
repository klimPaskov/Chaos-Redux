# Repression and Camps System UI Completion, 2026-08-28

## Scope

This pass repairs the compact decision-category attachment and the five-tab `repression_ledger_window`, lowers the category's decision-list priority, and standardizes the player-facing system name as `Repression and Camps System` for every country.

Internal `repression_ledger_*` identifiers remain unchanged because they are established scripted-GUI, sprite, localisation, and save-facing contracts rather than player-facing names.

## Interface changes

- The category attachment is 500 by 112 pixels, uses a fixed title, presents two short status lines, and exposes one `Open System` action whose visible frame and click region match.
- The popup retains its authored 900 by 560 dossier background and uses the background's central paper area instead of covering the frame or lower action space.
- The five 140-pixel tabs use an 18-pixel gap and equal 64-pixel outer margins.
- Summary, Territories, Sites, and Records use centered two-column layouts with equal 94-pixel popup margins and a 24-pixel gap between 344-pixel cards.
- The Records tab replaces the 112 by 112 decorative seals, which crossed 90-pixel card boundaries, with existing 24 by 24 evidence and reform status marks.
- Country-specific institution names appear only in the phase line and Authority tab. They no longer replace the system title.
- The last player-facing use of “ledger,” the Japanese `Occupation Test Ledger` project, is named `Occupation Test Records`; legacy ids remain internal only.
- Player-facing summaries use ordinary sentences and bounded two- or three-line card copy. Costs, blockers, and detailed consequences remain in tooltips.
- The category priority is `1`, matching the low-priority family used by the related occupation and repression categories.

## MCP visual evidence

The installed HOI4 MCP rendered the final popup under five named scenarios: `summary_normal`, `territories_full`, `sites_actions`, `authority_actions`, and `records_reckoning`.

Final popup render:

`hoi4-agent://workspace/repression_ui_narrow2/artifact/a6ca166660ce0401cb955db9aa95f9a1f17c6dbc706cdeb1fff12b3538057990/3832b781425a60d60fb9d9b157d654c6e4d20dc240362651abbbc8a4b5b5ef76/repression_ledger_window-full.png`

Five-tab scenario matrix:

`hoi4-agent://workspace/repression_ui_narrow2/artifact/7481f0662bd6b5daace60f46fbf17fa0c6bba887e929960612bb4bb706732d0b/a8204eca3dee221b1cdb567b98e17cec764a4cf8b8b2df01747afcb78dceb711/repression_ledger_window-scenario-matrix.png`

Summary click-region evidence:

`hoi4-agent://workspace/repression_ui_narrow2/artifact/b461764b42eb10c92aa7d72b9c85953c50caf06092349ef898381b7d0daf5f1b/681b56dcf8a5c8f21689a1054c856ba5acff975ef173339971199415a6ec82b1/repression_ledger_window-click-regions.png`

Sites and action-bar click-region evidence:

`hoi4-agent://workspace/repression_ui_narrow2/artifact/18d825532aad03ef095f8d2cb410412e6fe5e8680509d5783df5af4276451403/93567af5ca1e3c8526359b79fd0bd2f9d7204eef2060921c6490f901fccf6253/repression_ledger_window-click-regions.png`

Resolution matrix for 1920 by 1080, 1600 by 900, and 1280 by 720:

`hoi4-agent://workspace/repression_ui_narrow2/artifact/cf26ab2dd87663f599e8c11358715cc4e6174459ea2d54f7d83bbd52ef24cb35/b76f7044fa4cddf5e52ed2d71601f08e8fc592d5f79b0fe3ce3fbc76b336b21b/repression_ledger_window-resolution-scale.png`

Final category render:

`hoi4-agent://workspace/repression_ui_narrow2/artifact/752e98b9b9ab5c382136d9108da764895a792a49606b0bed2daa4f771dcaf0d7/b47451344349d8d43030df0b8c6afc7b1ce535ad694d76cdcf792ae5b5a61b94/repression_ledger_category_window-full.png`

The focused popup and category source graphs parsed and linked without blocking diagnostics, both render routes returned `GUI_RENDERED`, and the returned blocker lists were empty. The category validation reported no visible overlap. Popup acceptance used the named scenario matrix and click-region images because the aggregate validator also compares mutually exclusive tab children that never share a rendered scenario.

## Assets and wiring

No new visual asset is required.

The popup continues to use the authored assets under `gfx/interface/camp_repression/`, registered by `interface/camp_repression_rework.gfx`. The final layout consumes `GFX_repression_ledger_window_bg`, the tab and action atlases, card backgrounds, the selected-state and warning frames, and the existing 24 by 24 evidence and reform marks.

## Tooling note

`hoi4.gui_rewrite` was invoked against both the full repository and a focused UI workspace and produced before, proposed, visual-diff, fidelity, validation, and source-diff artifacts. Its write gate rejected the source package because it classifies hidden mutually exclusive tab buttons as aggregate click conflicts. The final source was therefore applied through the repository patch workflow and then inspected and rendered through `hoi4.gui_render` under explicit tab scenarios. This did not reduce the implemented layout or omit any tab, state, control, asset, or resolution review.

## Simplifications, omissions, and blockers

No design simplifications or requested omissions remain. All five tabs, both action rows, the category attachment, low-priority registration, fixed player-facing name, long-text state, interaction states, and the three target resolutions were included in the MCP review.
