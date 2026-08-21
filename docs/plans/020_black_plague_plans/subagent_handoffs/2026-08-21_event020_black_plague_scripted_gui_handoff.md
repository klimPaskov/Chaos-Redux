# Event 020 Black Plague Scripted GUI Handoff

## Outcome

`black_plague_response_category` now attaches the Event 020-owned `black_plague_response_category_scripted_gui`, whose `black_plague_response_category_window` is a compact read-only national response dashboard. Ordinary decisions remain the only action surface and the shared disease category, shared disease board, contamination mapmode, and selected-state containment ownership are unchanged.

The dashboard exposes one primary value and two supporting values:

- Countermeasure Progress, represented by five 20-point segments and its exact 0–100 value and programme stage.
- Medical Reserve, shown as current stock against capacity.
- Response Capacity, shown as remaining capacity against total capacity, with a visible exhausted-capacity warning.

Country deaths, worldwide deaths, and international-response status are supporting ledger lines rather than additional dashboard meters. Tooltips explain each value and explicitly state that countermeasure progress suppresses mortality and spread and permits cleanup without instantly removing an outbreak.

## Files and identifiers

- `interface/020_black_plague_response.gui`: `black_plague_response_category_window` and its presentation-only children.
- `common/scripted_guis/020_black_plague_response_scripted_guis.txt`: `black_plague_response_category_scripted_gui`, decision-category context, progress segment gates, and exhausted-capacity warning gate.
- `common/decisions/categories/020_black_plague_response_categories.txt`: attaches the scripted GUI to `black_plague_response_category`.
- `localisation/english/020_black_plague_response_l_english.yml`: short category description, dashboard labels, live values, warnings, and tooltips.
- `docs/events/020_black_plague/overview.md` and `docs/events/020_black_plague/shared_response.md`: live runtime and ownership contract.
- `docs/specs/020_black_plague_specs/corrections/2026-08-21_dedicated_response_scripted_gui.md`: later accepted presentation correction.
- `docs/specs/020_black_plague_specs/README.md` and `docs/specs/020_black_plague_specs/manifest.md`: correction routing and package inventory.

The existing `GFX_decision_cat_picture_black_plague_response`, `GFX_chaosx_checkbox_unchecked`, and `GFX_chaosx_checkbox_checked` sprites are reused. No new bitmap, placeholder, model, animation, category, gameplay variable, or progress producer was added.

## MCP evidence

The missing-window baseline is recorded at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18fd5cf427e765e0b14310d0b2342d831145dc80b4ce6be66209fe8c16c64b1c/957a3e984d870dc61c26bc44aa10a2861475b3191fc45f704310d7f475aebfb5/gui-inspect.ada293557a6aa019.json`.

The mandatory rewrite pass generated a before image, proposed image, visual diff, fidelity report, validation report, and exact source diffs. The rewrite itself was blocked from writing because the repository-wide GUI graph exceeds the MCP diagnostic ceiling and contains unrelated legacy sprite collisions. Its scoped proposed artifacts are:

- proposed render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d5dee81a05c60f229997b1dd6d48eb0a499b13ed98bab6ae309111b2c0ce030/e680cfeca1b8a2642005fd07fbaa1c937ba637889a93ef2a40b69a04f2ab1f0a/black_plague_response_category_window-proposed.png`
- visual diff: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42dbf228ae06fa2ffa0b8d98c1a85f7d5bdea71956596e9044e1700cbe2fcdc3/b4d048e6ef30fcadb18e0923e3562180c97c901b25453731087b78662cd3b9fd/black_plague_response_category_window-visual-diff.png`
- proposed fidelity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/711527dabf33e17837b476f7d15ee16f5b874cc3b111de319892bb2040f6308a/188f80c4b99fb15c014ca1bd1d8f9e86c015d53b177c9d8369005de884a3a9c7/black_plague_response_category_window-proposed-fidelity.json`
- rewrite validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9dc87304d976f95f19b30302ac9ed765e8605e7278a3d0946aea3479a593043/7334f00b6af3e9419803a721fc629bddcdaeaa4ab2cd3826f5a59aedf511a553/black_plague_response_category_window-rewrite-validation.json`

After the scoped sources were installed and the three referenced local LFS assets were hydrated, `hoi4.gui_inspect` resolved 21 elements in the exact Event 020 window and recognized its decision-category context. Post-change inspection is recorded at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d94db440fc0d6a27e0336f944f3e12423fc917f9fa2de86f8863d4adbbc2d5ac/e6e59be88672c65f60da839c070d64c1dcd0a86c250222623418b72289e8e02f/gui-inspect.235c618fde462b56.json`.

The normal dashboard rendered at the requested 1366×768, 1920×1080, and 2560×1440 resolutions. Its deterministic render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/946d139a966da35bb57b856826c106b257bc23ad20029b20a70ecc5a85ee55b0/822ac26f205b0c7e27d6a305fc015a3a3fb6b7065049ebc5161a50fd4f830cd7/black_plague_response_category_window-full.svg`.

## Tooling deviation and remaining evidence limit

Two required `chaosx_event_ui_worker` attempts failed before file access because the worker runtime returned `code-mode IPC frame length 143204xxx exceeds 67108864 bytes` for every tool call, including minimal text and working-directory calls. No worker-owned edit was made. The parent completed the same bounded workflow and retained the worker failure as an explicit deviation.

The combined MCP state sweep hit an internal error, and subsequent isolated warning-state rendering timed out after the server had serialized the earlier calls. The localisation audit later completed a bounded long-text render at 1920×1080, recorded in its adjacent handoff. Normal resolution evidence and exact-window inspection are available, but independent rendered artifacts for minimum-value, maximum-value, missing-localisation, and exhausted-capacity states are not available from this MCP session. The source gates for 0, 20, 40, 60, 80, and 100 progress and zero remaining capacity are present and use Event 020 script constants. This is a tooling evidence limitation, not a fallback gameplay or UI implementation.

No live in-game validation was run.
