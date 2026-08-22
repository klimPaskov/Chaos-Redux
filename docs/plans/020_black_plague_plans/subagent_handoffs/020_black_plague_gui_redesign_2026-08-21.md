# Event 020 Black Plague GUI Redesign Handoff

## Outcome

The bounded redesign is blocked and no runtime source was changed. The mandatory `hoi4.gui_rewrite` route rejected the scoped Event 020 source proposal because the repository-wide GUI graph exceeded the MCP diagnostic ceiling and contained unrelated duplicate texture registrations. The tool returned `status = blocked`, `code = GUI_CHANGES_BLOCKED`, `execution = blocked`, and an empty `changedFiles` list. In accordance with the Event 020 UI-worker contract, the proposed layout was not installed with a source-only fallback.

## Event ownership proof

The surface belongs exclusively to Event 020 Black Plague:

- `docs/events/020_black_plague/shared_response.md` identifies `black_plague_response_category_scripted_gui` as the dedicated Event 020 national-response dashboard.
- `docs/events/020_black_plague/overview.md` identifies the same scripted GUI and window as Event 020 runtime surfaces.
- `docs/specs/020_black_plague_specs/corrections/2026-08-21_dedicated_response_scripted_gui.md` assigns one read-only attachment to `black_plague_response_category` and explicitly excludes the shared disease board and selected-state action surface.
- `common/decisions/categories/020_black_plague_response_categories.txt` attaches `scripted_gui = black_plague_response_category_scripted_gui` to `black_plague_response_category`.

The parent brief named `common/decisions/categories/020_black_plague_response_category.txt`, but that singular file does not exist. The live, read-only entry-point file uses the plural `020_black_plague_response_categories.txt` name. Neither form was edited.

## Exact scoped identifiers

- Event id and slug: `020_black_plague`
- Scripted GUI: `black_plague_response_category_scripted_gui`
- Window: `black_plague_response_category_window`
- Decision category: `black_plague_response_category`
- Category picture sprite: `GFX_decision_cat_picture_black_plague_response`
- Category picture texture: `gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds`
- GUI layout: `interface/020_black_plague_response.gui`
- Presentation binding: `common/scripted_guis/020_black_plague_response_scripted_guis.txt`
- GUI localisation: `localisation/english/020_black_plague_response_l_english.yml`
- Sprite registry: `interface/020_black_plague_response.gfx`
- Live category entry point, read only: `common/decisions/categories/020_black_plague_response_categories.txt`

## References inspected

- Offline wiki: Interface Modding, Scripted GUI Modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.
- Installed vanilla documentation: `documentation/triggers_documentation.md`, `documentation/effects_documentation.md`, and `documentation/modifiers_documentation.md`.
- Exact vanilla precedent: `interface/RAJ_famine.gui` and `common/scripted_guis/RAJ_famine_scripted_gui.txt`.
- Additional vanilla meter precedent: `interface/countrydecisionview.gui`, `interface/countrydecisionview.gfx`, and `interface/countryofficercorpview.gfx`.
- Event 020 accepted correction, prior GUI handoff, localisation audit, category-picture handoff, ownership docs, exact GUI source, scripted-GUI source, localisation, GFX registration, and category attachment.

## Pre-change MCP evidence

### Inspect

`hoi4.gui_inspect` resolved the exact Event 020 window with 21 elements and recognized its decision-category context under scenario `representative_plague_response`.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1377bb8d3c884b4f0dd24af544033e7240f59dc8aaa2991ada8f61e59cc02d0a/0c3b62497eea7647e1904afb3098694fa9465cbc52c422495c5339b3b80d318c/gui-inspect.aeaec78336ea0594.json`
- Scenario values: Countermeasure Progress 60, Medical Reserve 72/100, Response Capacity 5/12, national deaths 125,000, representative world deaths, an active countermeasure programme, and alliance exchange.
- Scoped findings returned within the combined validation set included visible overlap, accidental clipping, inconsistent alignment and spacing, and unresolved dynamic values. The global result was also truncated by unrelated repository diagnostics.

### Render

`hoi4.gui_render` covered normal, hover, warning, minimum-value, maximum-value, and long-text states at 1920x1080 scale 1, 1280x720 scale 1, and 1920x1080 scale 1.25. The tool response itself was wire-truncated, while the linked artifact retained the render evidence.

- Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e72739979198fddc8b3f6aaf1934c1ac16ef88390e6ec716cb351fa6dbc93f7e/04587e3042114e76567b951f8092445067e5e7d05c9430de2365307dfcc2a8b5/black_plague_response_category_window-full.svg`

The pre-change layout is a 470x272 panel. It uses ten checkbox sprites as a five-segment progress display, a 0.58-scale identity picture, two unframed support-value lines, and three tightly stacked lower status lines. This structure explains the weak hierarchy and collision risk reported by the user and MCP diagnostics.

## Proposed bounded redesign

The rejected rewrite proposal remained read-only and introduced no buttons, click effects, gameplay outcomes, costs, AI behavior, or new art.

### Layout hierarchy

1. A 502x304 category-width panel.
2. A larger 0.80-scale plague-doctor picture as the left identity anchor.
3. A right-aligned title and programme-state block with room for two status lines.
4. One primary Countermeasure Progress section with exact value, five visual stages, and a concise stage legend.
5. Two separated support cards for Medical Reserve and Response Capacity.
6. One subordinate deaths ledger row and one subordinate international-response row.
7. The capacity-exhausted warning stays inside the Response Capacity card rather than competing with the main ledger.

### Background coverage map

| Region | Intended content | Proposed elements | Interaction/state | Status |
| --- | --- | --- | --- | --- |
| Left header anchor | Event identity | Existing plague-doctor picture | Informational tooltip, click-through | Proposed, not applied |
| Right header field | Dashboard title and programme state | Title and programme-status text | Informational tooltips | Proposed, not applied |
| Full-width middle band | Primary 0-100 progress | Label, exact value, five-stage meter, stage legend | Stage fills driven by existing visibility triggers | Proposed, not applied |
| Lower-left card | Medical Reserve | Framed value card | Informational tooltip | Proposed, not applied |
| Lower-right card | Response Capacity | Framed value card plus exhausted warning | Warning visibility from existing trigger | Proposed, not applied |
| Footer row 1 | Mortality ledger | National and world deaths | Informational tooltip | Proposed, not applied |
| Footer row 2 | International coordination | Current response status | Informational tooltip | Proposed, not applied |

### Value and action budgets

- Primary mechanic values: 1, Countermeasure Progress.
- Supporting mechanic values: 2, Medical Reserve and Response Capacity.
- Subordinate status: programme stage, national/world deaths, and international coordination. These remain status text, not competing meters.
- Gameplay-changing GUI controls: 0.
- Primary actions: 0. Ordinary decisions remain the sole action surface.
- Spendable cost types displayed by this GUI: 0.
- Texticon coverage: not applicable because the surface displays no costs.
- Button-like or dead controls: 0 in the proposal.

### Text-density audit

The proposal reserves a two-line header status area, a dedicated progress label/value line, one short stage legend, one line per support value, a capacity warning confined to its owning card, and two separate footer rows. It removes the current lower-row competition and does not add explanatory prose to the panel. Existing concise tooltips remain the explanation surface.

### State matrix

| State | Intended visual behavior | Evidence status |
| --- | --- | --- |
| Normal representative | First three of five stage tiles filled at progress 60, reserve 72/100, capacity 5/12 | Proposed PNG only, rewrite blocked |
| Hover | Tooltips on identity, progress, cards, ledger, and coordination status | Pre-render requested, no applied post-state |
| Warning/capacity exhausted | Warning contained within the Response Capacity card | Proposed source and PNG only |
| Minimum value | Empty stage fill, exact zero value | Pre-render requested, no applied post-state |
| Maximum value | All five stages filled, exact maximum value | Pre-render requested, no applied post-state |
| Long text | Header and footer use dedicated fixed bounds | Pre-render requested, no applied post-state |
| Disabled/selected/active/completed | No controls exist. Programme and stage text remain informational state | No applied post-state |

## Mandatory rewrite evidence and exact blocker

`hoi4.gui_rewrite` was called in `source` mode for `interface/020_black_plague_response.gui`, exact window `black_plague_response_category_window`, workspace `mod_chaos_redux_ea3b2d67c2c0`, and scenario `representative_plague_response`.

Result:

- `status = blocked`
- `code = GUI_CHANGES_BLOCKED`
- `execution = blocked`
- `changedFiles = []`
- Primary blocker: `GUI_GRAPH_DIAGNOSTICS_TRUNCATED`, with 1,999 retained and 1,519 dropped GUI graph diagnostics.
- Additional unrelated blockers: duplicate texture registrations led by `interface/003_holy_realm.gfx` and `interface/005_soviet_collapse.gfx`.
- Scoped proposal validation also reported three visible-overlap and eleven accidental-clipping diagnostics. Because the rewrite never applied, these proposed-layout findings could not be iterated through a compliant post-change loop.

Rewrite artifacts:

- Before PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/347be2cd3b09625aebd943b4db21942d35639719b3f1083f8fb6db9925d83d61/890904dfba6ba83f0737102dc227bd99b2c1d94ca4cc0e8f3bb671ec4919a81c/black_plague_response_category_window-before.png`
- Proposed PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6df311b9cef3db440cf167791cbe257a4a64cf001d732d9cf92c094115573ad8/5c69a5ea3ceb0fa59b982972f610a51838cd47e4400fdd0c1dec11e87b347c86/black_plague_response_category_window-proposed.png`
- Visual diff PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eda6661a23de17b5646acddbcd2cbab2b2a9ab5a6ed7aa6520a2cae7b723dc45/2382fe25bb78913db699174f3c8b0ba7fa78ec08d57b31666731896de9f94fa5/black_plague_response_category_window-visual-diff.png`
- Proposed fidelity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/beee8d6a8275052cd0762d13f3c6042259bb4ef09c23fcd79f012fbf17fd8fee/c83c17c5451ac53501543067d501e2bb279ae798f373f3bcbb7607fbf68416cb/black_plague_response_category_window-proposed-fidelity.json`
- Rewrite validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/791f234aa1d0e296f8ec8428295681b8b2aad2fe7caf75501eee8c3fadc45263/45f6b151f0ba385ebe3c2a6e393be3dcac65fd66130ce3c372e391b8c8a0286e/black_plague_response_category_window-rewrite-validation.json`
- Exact source diff: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/937a7a78c5e61e75cb7693bd8f2875abcbdc18608d8e3f39669b14f54248fbef/9b4782d16d644139cba6434bc43fbd4f8ca7453091831110c4b6c1b318d77b19/020_black_plague_response.gui.diff`

## Files changed

- `docs/plans/020_black_plague_plans/subagent_handoffs/020_black_plague_gui_redesign_2026-08-21.md`

No GUI, scripted-GUI, GFX, sprite, localisation, decision, or gameplay file changed.

## Skipped meaningful validation

- Post-change `hoi4.gui_inspect`, render, resolution, hierarchy, click-region, state, and comparison evidence could not be produced because no source change was applied.
- The proposed PNG could not be accepted as final visual evidence because the rewrite validation still reported scoped overlap and clipping findings and the mandatory iteration loop could not continue after the blocked write.
- No live in-game validation was run or claimed.

## Missing assets and asset routing

No asset is missing. The proposal deliberately reuses `GFX_decision_cat_picture_black_plague_response`, `GFX_tiled_progress_bar`, `GFX_tiled_progress_bar_coloured`, `GFX_tiled_window`, and `GFX_tiled_window_transparent`. It does not request or generate new art.

## Remaining parent-owned work and risks

- Resolve or scope around the repository-wide MCP GUI diagnostic ceiling and the unrelated Event 003/Event 005 duplicate texture registrations, then rerun the exact rewrite.
- Review the proposed PNG and fidelity report before accepting coordinates. The proposal still has scoped overlap/clipping diagnostics and must be iterated rather than installed as-is.
- After a successful rewrite, rerun the same representative, warning, minimum, maximum, and long-text states at all three requested resolution/UI-scale combinations, including hierarchy and click-region views.
- Replace or otherwise resolve synthetic-preview raw localisation/constant strings only through an MCP-reviewed revision. The current source remains unchanged and therefore retains this known issue.
- Runtime and in-game consumer validation remain parent/user owned.

## Simplifications, omissions, and blockers

- Blocker: mandatory MCP rewrite was rejected by global GUI graph truncation and unrelated duplicate texture registrations.
- Omission caused by the blocker: no runtime redesign, localisation correction, or scripted-GUI presentation update was installed.
- Omission caused by the blocker: no compliant post-change visual comparison exists.
- No fallback, placeholder, gameplay change, fake control, asset substitution, or unreviewed source edit was used.
