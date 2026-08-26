# Event 014 GUI completion evidence, 2026-08-26

## Outcome

The five Event 014 scripted GUI windows were reviewed within the granted scope. No Event 014 source patch was applied because fresh MCP diagnostics and renders did not provide attributable element-level visual evidence. Visual completion remains blocked by MCP truncation and render timeouts.

No cosmetic animation button, animation toggle, animation-labelled control, or player-facing animation wording exists in the five windows. The retained animated and static sprites are automatic presentation pairs selected by scripted visibility. They are not player features.

## Event ownership proof

Event id and slug: `014_cannibalism`.

The accepted design source is `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md`. It explicitly introduces the early attached header, organized-network window, Cannibal command window, revealed command window, and Wendigo transformation window.

The exact Event 014 windows are:

| GUI window | Scripted GUI | Entry point |
| --- | --- | --- |
| `cannibalism_early_header_window` | `cannibalism_early_header_scripted_gui` | `cannibalism_containment_category` and `cannibalism_network_alerts_category` |
| `cannibalism_network_window` | `cannibalism_network_scripted_gui` | `cannibalism_network_open` calls `cannibalism_gui_open_network_view`; player context attached to `top_bar` |
| `cannibalism_warlord_command_window` | `cannibalism_warlord_command_scripted_gui` | `cannibalism_warlord_command_category` |
| `cannibalism_revealed_command_window` | `cannibalism_revealed_command_scripted_gui` | `cannibalism_unified_command_category` |
| `cannibalism_wendigo_command_window` | `cannibalism_wendigo_command_scripted_gui` | `cannibalism_wendigo_command_category` |

The owning sources are `interface/014_cannibalism_frontline_hunger.gui`, `common/scripted_guis/014_cannibalism_scripted_gui.txt`, `interface/014_cannibalism.gfx`, `localisation/english/014_cannibalism_l_english.yml`, and the Event 014 category entry points in `common/decisions/categories/014_cannibalism_categories.txt`.

No shared event log, Event Details surface, settings UI, options UI, super-event framework, shared registry, generic debug window, focus tree, decision gameplay, portrait, model, audio, or spreadsheet was edited.

## Required references inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- Offline wiki pages `Interface modding` and `Scripted GUI modding`, together with the repository-required core wiki pages
- Installed vanilla `common/scripted_guis/_documentation.md`
- Installed vanilla `common/scripted_guis/RAJ_famine_scripted_gui.txt` and `interface/RAJ_famine.gui` as the exact compact decision-category GUI precedent
- Event 014 spec parts 6, 10, and 12
- `docs/plans/014_cannibalism_plans/014_gui_dimension_ledger.md`
- Prior Event 014 GUI/parser/MCP handoffs dated 2026-08-24 and 2026-08-25

## Source state and concurrent edits

No source file was changed by this pass. Source hashes at handoff time are:

| File | SHA-256 |
| --- | --- |
| `interface/014_cannibalism_frontline_hunger.gui` | `64AE03CB2BE62504F796F4538127F1934A32C38232CA8A0702A57D983FF5A505` |
| `common/scripted_guis/014_cannibalism_scripted_gui.txt` | `AE34922799AE47F90293AB412A004CBF6A65C740B9F70A11FCA363299F2706CD` |
| `interface/014_cannibalism.gfx` | `7885097FDE79644519679A39D5AEF23FE9EFA73C966897F1CBD2AFDA849FFCFE` |
| `localisation/english/014_cannibalism_l_english.yml` | `6F882EE84EB8734C68F2D390A1568B70114AD49494599BECE8513A44DCEDD362` |

The GUI file already had concurrent changes that align the Countermeasures tab, Sort button, and Refresh button into the network control band. This pass preserved those edits and did not amend, revert, stage, or claim them.

## Layout hierarchy and background coverage

| Window | Canvas | Main regions and consumers | Coverage |
| --- | ---: | --- | --- |
| Early | 470x304 | title, three-meter stack, state card, warning/cohesion presentation, mission summary, Network Ledger entry | All functional regions mapped |
| Network | 860x620 | title/summary, close and filter controls, central network presentation, twin clipped lists, selected-target evidence card | All functional regions mapped |
| Warlord | 470x340 | three meters, controlled-state/capacity card, route and critical-state presentation | All functional regions mapped |
| Revealed | 470x380 | revealed portrait bay, two meters, loyalty card, seal, conditional terminal field | All functional regions mapped |
| Wendigo | 470x400 | transformed portrait bay, anchor card, countdown, Pack capacity, conditional terminal field | All functional regions mapped |

The source dimensions remain inside 1366x768, 1600x900, 1920x1080, and 2560x1440 at UI scale 1.0 by coordinate arithmetic. This is not a substitute for the missing MCP resolution renders.

## Value, action, cost, and text-density audit

| Surface | Public mechanic values | Gameplay-changing GUI actions | View controls | Result |
| --- | --- | ---: | ---: | --- |
| Early | Field Hunger, Command Integrity, conditional Cult Cohesion | 0 | 1 | Three values, within budget |
| Network | actor count, node count, Network Reach, with per-row context | 0 | five filters, sort, refresh, close, row selection | Data-ledger controls only |
| Warlord | Larder, Frenzy, conditional Alignment, formation capacity | 0 | 0 | Four values, hard ceiling |
| Revealed | global Larder, global Network Reach, integrated warlords, conditional terminal progress | 0 | 0 | Four values, hard ceiling |
| Wendigo | anchor state, countdown, Pack capacity, conditional terminal state | 0 | 0 | Four values, hard ceiling |

No GUI control spends resources. Spendable-cost count and GUI texticon cost coverage are therefore zero and not applicable. Gameplay costs remain in Event 014 decisions.

All visible GUI localisation keys referenced by the five-window source resolve in `014_cannibalism_l_english.yml`. A targeted search found no player-facing `animation`, `animated`, `motion`, cosmetic-animation toggle, or equivalent wording. Pre-reveal strings remain anonymous: the network is titled `The Uncertain Network`, and Hannibal is named only in the revealed and Wendigo command surfaces.

The current source uses one-line titles, a two-line network summary, one- or two-line cards, fixed bounds, clipped list wells, and full-row 374x64 transparent selectors. Source review finds no justified edit, but long-text safety and exact hover/click agreement remain visually unresolved because the MCP diagnostics were dropped.

## Fresh pre-change MCP inspect evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

| Window | Scenario | Result | Artifact |
| --- | --- | --- | --- |
| Early | `event014_resume_pre_cannibalism_early_header_window_2026_08_26` and capture retry `event014_resume_pre_early_capture_2026_08_26` | First response did not expose a typed artifact; capture retry timed out after 180 seconds | No fresh attributable artifact |
| Network | `event014_resume_pre_cannibalism_network_window_2026_08_26` | `GUI_INSPECTED`, `status = ok` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2027fb79400aa4c2e2bee84d06a83dc6ad64f1a2fdf4cdda77c60b96426a25b7/3ca28e89eb6d436c06e865465b0bb29dfbb5167e0f7ed68fdc7c581505a77e6e/gui-inspect.a4f84d3e76676744.json` |
| Warlord | `event014_resume_pre_cannibalism_warlord_command_window_2026_08_26` | `GUI_INSPECTED`, `status = ok` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6c1a16a4ab675b12098584f306fe6a1af24110d4148d8f3fc76e88124ff608a/fbf4b04618301314488dc76004e3ed665cb108f0df4daab0d7621f79964b5792/gui-inspect.1a0762446a6e31b6.json` |
| Revealed | `event014_resume_pre_cannibalism_revealed_command_window_2026_08_26` | `GUI_INSPECTED`, `status = ok` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c455f2eeb4ff051e96a85d4fcaa938a432f48d7f26d178ada575648e0c12b771/41269cfa13ff6b9399a8c3a4fb88287c43820a32a94003301e9eda90860ba4ef/gui-inspect.0cbe470a5f3f0ee4.json` |
| Wendigo | `event014_resume_pre_cannibalism_wendigo_command_window_2026_08_26` | `GUI_INSPECTED`, `status = ok` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b17fb49f3109c44c017b221de5052f62636cf46f3c6f082cd86c4a61df6d391/83adb49f5d64e0f78b7b0992ef94e48449f376bb9a7623ef812839937356a4af/gui-inspect.b099513cfc92d08f.json` |

Every successful inspect returned `MCP_INLINE_COLLECTIONS_TRUNCATED`, `GUI_GRAPH_DIAGNOSTICS_TRUNCATED`, and `GUI_VALIDATION_DIAGNOSTICS_TRUNCATED`. Retained inline errors were dominated by unrelated Event 003 and Event 005 symbol collisions. The Event 014 validation details were dropped before element paths.

The network inspect reports dropped totals including one `GUI_CLICK_BOUNDS_MISMATCH`, one `GUI_TEXT_OVERFLOW`, 24 accidental-clipping findings, 21 child-outside-clipped-parent findings, 11 overlaps, eight missing button-trigger findings, and one spacing finding. None has a retained Event 014 element path, bounds pair, localisation key, or source location. The other windows similarly report dropped overlap, overflow, alignment, spacing, dynamic-value, and animation diagnostics without attributable element paths. These totals cannot justify a safe patch.

## Fresh MCP render, state, resolution, hierarchy, click-region, and comparison requests

### Targeted render retry

After the matrix requests below, a single normal-state render was retried with the exact selector `cannibalism_network_window` and scenario `event014_targeted_network_normal_2026_08_26`. The adapter returned `GUI_RENDERED` with no blockers and exposed `cannibalism_network_window-full.svg` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40cfb5508bb2c3917099dda1c792b23e57108c299e4e0861d0e778b0ad8a2970/14ca74fc2d4120165140404d28c9511d4875641c4e0c9d3e2bf34e517a22ca68/cannibalism_network_window-full.svg`. The requested 1280x720 input was normalized by the adapter to a 1920x1080 canvas. The response was wire-truncated and retained no validation checks, so this is an attributable single-state artifact only; it does not prove the unresolved hover, disabled, long-text, click-region, multi-resolution, hierarchy, or comparison cases.

For every exact selector, `hoi4.gui_render` was requested with:

- states: normal, hover, selected, active, disabled, warning, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation
- resolutions: 1366x768, 1600x900, 1920x1080, and 2560x1440 at UI scale 1.0
- a named comparison scenario

| Window | Render scenario | Comparison scenario | Result |
| --- | --- | --- | --- |
| Early | `event014_resume_render_cannibalism_early_header_window_2026_08_26` | `event014_resume_compare_cannibalism_early_header_window_2026_08_26` | 180-second route timeout; no attributable artifact |
| Network | `event014_resume_render_cannibalism_network_window_2026_08_26` | `event014_resume_compare_cannibalism_network_window_2026_08_26` | 180-second route timeout; no attributable artifact |
| Warlord | `event014_resume_render_cannibalism_warlord_command_window_2026_08_26` | `event014_resume_compare_cannibalism_warlord_command_window_2026_08_26` | 180-second route timeout; no attributable artifact |
| Revealed | `event014_resume_render_cannibalism_revealed_command_window_2026_08_26` | `event014_resume_compare_cannibalism_revealed_command_window_2026_08_26` | 180-second route timeout; no attributable artifact |
| Wendigo | `event014_resume_render_cannibalism_wendigo_command_window_2026_08_26` | `event014_resume_compare_cannibalism_wendigo_command_window_2026_08_26` | 180-second route timeout; no attributable artifact |

No fresh full-window, cropped, annotated, hierarchy, click-region, hover, disabled, selected, active, warning, completed, empty, crowded, long-text, missing-localisation, resolution, or comparison image was exposed by the route.

## Rewrite and before/after disposition

`hoi4.gui_rewrite` was not called. The required rule makes rewrite mandatory for an in-scope layout change after attributable inspect and render evidence. No source change was justified, and the render route did not provide the evidence required to review a rewrite safely.

There is no behavioral or visual source delta from this pass. Before and after source hashes are identical because no source was edited. Post-change inspect/render/comparison is therefore not applicable. This handoff does not relabel the failed pre-change render matrix as post-change evidence.

## Click regions, hover, disabled, overlap, and resolution matrix

| Review item | Source finding | MCP result | Status |
| --- | --- | --- | --- |
| Network row click regions | 374x64 transparent selectors exactly match 374x64 entry containers and card sprites | One click-bounds mismatch was dropped without an element path | Unresolved |
| Open, close, tabs, sort, refresh | Every button has a matching scripted effect; Network Ledger has an Evolution II enablement gate | Hover and disabled variants timed out | Unresolved visually |
| Decorative/state sprites | Icons, not buttons; automatic animated/static visibility pairs | Overlap totals were dropped without element paths | Intentional pairs cannot be distinguished from defects by MCP |
| Long text and missing localisation | All referenced GUI keys resolve; source uses fixed bounds and concise text | Requested variants timed out; overflow findings lack paths | Unresolved visually |
| 1366x768 | Window bounds fit by arithmetic | Render timed out | Unresolved visually |
| 1600x900 | Window bounds fit by arithmetic | Render timed out | Unresolved visually |
| 1920x1080 | Window bounds fit by arithmetic | Render timed out | Unresolved visually |
| 2560x1440 | Window bounds fit by arithmetic | Render timed out | Unresolved visually |

## Assets and handoffs

No missing Event 014 GUI asset was proven. No asset was created, moved, regenerated, substituted, or rewired. No animation asset request was opened because the task required removing player-facing animation controls and wording, not removing automatic state presentation, and no such player-facing control or wording exists.

## Parent-owned work and blockers

- Fresh early-header inspect evidence is unavailable because the capture retry timed out.
- Successful inspect artifacts are approximately 56 MB and report globally truncated diagnostics, with Event 014 element paths dropped.
- All five exact-selector render matrices timed out after 180 seconds without attributable artifacts.
- Exact hover, pressed, selected, active, disabled, warning, completed, empty, crowded, hierarchy, click-region, clipping, overlap, long-text, localisation-expansion, resolution, and comparison behavior remains unproven.
- Live consumer and in-game validation remain parent-owned.

## Simplifications, omissions, and completion claim

No fallback UI, placeholder, guessed click region, speculative coordinate edit, gameplay change, asset substitution, or source simplification was introduced.

The required visual-evidence pass is incomplete. This handoff does not claim GUI visual completion.
