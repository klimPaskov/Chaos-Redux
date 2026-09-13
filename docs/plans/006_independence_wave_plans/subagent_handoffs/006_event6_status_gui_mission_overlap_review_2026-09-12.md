# Event 006 mission/detail overlap review

Disposition: **unresolved; no source edit**.
Date: 2026-09-12.

## Scope and acceptance

The parent authorized only a demonstrable mission/detail geometry repair in `interface/006_independence_wave.gui`, window `independence_wave_status_window`.
The existing founding-category attachment `independence_wave_status_scripted_gui`, five tabs, sprites, controller, and warning relocation remain intact.
Gameplay, localisation, assets, controller wiring, shared interfaces, and unrelated changes are excluded.
This review continues the earlier Event 006-owned inspection, not a redesign.

The parent explicitly reaffirmed the accepted five-value exception through `docs/specs/006_independence_wave_specs/prompts/independence_wave_decision_mission_prompt.md` (Required mechanic values) and the Statehood Ledger evidence in `006_event6_current_mcp_evidence_2026-09-12.md`.
The warning-repair receipt `006_event6_status_gui_warning_placement_repair_2026-09-12.md` and historical `006_statehood_ledger_gui_closure_2026-08-30.md` were also read.
All five founding values and the accepted host/patron/network context remain unchanged; the generic four-value rule is not used to remove accepted Event 006 content.
This supersedes the earlier worker's treatment of the five founding values themselves as an unresolved acceptance decision for this bounded task, without claiming that all density or dynamic-text concerns are closed.

The current scripted-GUI skill was reread and its integrated visual-review checklist applied.
The former `references/visual-review.md` path is absent; the current skill contains the review contract inline.
Offline Interface modding and Scripted GUI modding references and the installed scripted-GUI documentation/Soviet paranoia native text-box precedent were revisited.
The exact GUI, GFX, and controller sources were reopened; no change was made to them.

## Source and reference mapping

Source revision: `4df34107e11d2a719f1b76688f7aaf908ff301e0ad2174dcd0b1662efa5e63bc`.
GUI SHA-256: `d8b2a3dde2e33b6643664eb4560243647a9069da3ba58987c33bd284f52e677f`.
The initial GUI diff against the checkout was empty.

| Region | Native source mapping | Finding |
| --- | --- | --- |
| Active-commitments heading | `independence_wave_status_mission_header`, x366/y386, 220 × 22 | Retained. |
| Active-commitments text | `independence_wave_status_mission`, x366/y410, 220 × 40, `hoi_16mbs` | Logical rectangle ends at y450. |
| Five exclusive tab detail texts | `independence_wave_status_{government,recognition,security,league,ambitions}_panel`, x280/y444, 386 × 42 | Logical rectangles begin six pixels before the mission rectangle ends. |
| Existing warning repair | `independence_wave_status_instability_warning`, x318/y384, scale 0.75 | Preserved; not moved back into the instability metric. |
| Background | `GFX_independence_wave_status_panel`, 700 × 500 | Existing composition and bottom inset retained. |

The selected visual reference is the parent's post-warning cropped production render at this exact revision:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e9f30eb962758ee93d79dbcb9aca2e75eacdce13392f2540cfd9f4f8319365c/c5f147265017bd9309b074a83c303200ce1fb5a7a89778c0b7358bb21ea927cb/independence_wave_status_window-cropped.png`.
It was reopened and actually viewed at native dimensions.
The mission placeholder is a single line with visible space before the detail-panel text.
The visible bottom-right corruption is the five detail texts overprinting one another, not demonstrated mission glyphs overprinting detail glyphs in this fixture.
The six-pixel logical intersection is a real geometry risk, but it must not be mislabeled as an observed mission-text collision.

No corrected reference or speculative geometry patch was made: changing the mission height could truncate legitimate two-line text, while lowering 42-pixel detail boxes would consume the small remaining bottom inset.
The requested repair requires actual mission expansion and coherent selected-panel evidence before choosing those adaptations.
The source click handlers still set one tab flag and clear the other four; no visibility redesign is inferred from the empty fixture.
The production overprint remains a visual acceptance blocker rather than being waived as a rendering discrepancy.

## Mandatory MCP evidence

Fresh `hoi4.gui_inspect` used the exact window and this scenario, with generated scenarios disabled:

```json
{"id":"event006_status_repair_baseline_post_warning","resolution":{"width":1920,"height":1080},"uiScale":1}
```

It returned `GUI_INSPECTED`, the revision above, complete selected-window projection, 48 elements, 16 sprites, two fonts, 39 localisation references, and one scripted GUI.
Fidelity counts were 556 modelled, five approximated, 15 ignored, zero missing, four unsupported, and 12 unresolved.
It reported 63 nonfatal overlap findings; a passing validation flag does not close visual defects.
The mission-specific warning is `GUI_UNRESOLVED_DYNAMIC_VALUE` for `[This.GetIndependenceWaveMissionStatus]`.
No mission-to-tab glyph-overlap diagnostic was present in this baseline; background containment and near-alignment messages are not evidence of that collision.

Inspection artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1cdc77bcfe3b4e724caaba79731c40ddf1f3c770ad77cc4e4a4ed95e0deabb12/7309923e6f3026e14799d4c11a98c098363397b749043fd73eac8457d9e73052/gui-inspect.4df34107e11d2a71.json`.

The parent's normalized scenario resource was read directly:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a26c8d41d2604785d6ff1616780420899ccb9c0e7015eb5a76854fd504824279/abcb4c845e107cd60062a18f65acc15851a372f42fcac12816cb84d7a165baf6/independence_wave_status_window-scenario.json`.
Its values, variables, flags, localisation substitutions, visibility overrides, scripted-GUI mocks, and element-state maps are empty.
The normal/long-text/warning rerender used this same baseline, UI scale 1, 1920 × 1080, and `generatedScenarios.enabled = false`.
It returned `GUI_RENDERED`, 27 artifacts, three states, one scenario, one resolution, five variants, and the unchanged source revision above.
The full and cropped PNG identities exactly match the parent's post-warning artifacts, confirming that the normal baseline is unchanged.
The state-matrix PNG was also opened and viewed; it shows normal, synthetic expanded long-text, and warning views.
The matrix is an overview, not a native-size long-text crop, so no detailed stress-state clearance pass is claimed.
The emitted state JSON was read completely and confirms empty explicit localisation/value/visibility maps in all three states, with IDs ending `-normal`, `-long-text`, and `-warning`.
The normal and warning views retain the mission placeholder, while the synthetic long-text state expands text throughout the window; neither establishes the exact real mission substitution and selected-panel combination needed for this bounded repair.

Fresh render receipt artifacts:

- State matrix PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a2b9fbf7f5a5c1d633161f62d8eedc769a670eb25264da60c2b4888cf9d73da/0da60c92f8fe9963e796281d728d6992050115fb70d19e5c1ee99f432f6b9229/independence_wave_status_window-state-matrix.png`.
- State matrix JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/817f24c38e253b52351db197c2851c16202839e771d6f2a7d53ab2077ad9fb2a/aec18c845de3457ec8b264695a0c0bd321ce3f3d80b8fe96f66f0d31c94e0568/independence_wave_status_window-state-matrix.json`.
- Click regions: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95a5006fc0d8cd3942baa6321b87f2c95d01ed7a7d2d477678eaaf399d59b096/0760c2c7e79dc26517b85198ff1bb3f4d867a9602e648f15efd573f85e54c401/independence_wave_status_window-click-regions.png`.
- Hierarchy: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6ab51bd1a02d1bcc37371410041db872f48ec537d4ffcbc31799ba71b7e9c69/dd33f309de99e59fb3029d397d3377391e717aaac4bc32571d6feb64863edb75/independence_wave_status_window-hierarchy.svg`.
- Validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/04780aa04ba53e627a17d8deafd1302faca007b19b570b4b4089969e42e10ee4/b4a174e523e706a38da35e5eee9157026f62a173e81b850d697fde52bf649e19/independence_wave_status_window-validation.json`.
- Fidelity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66131b998cb3d3233a08512d9f863964cae3cf3bd93f77264005557f4e56be5b/5425ae3c56846166ef024f3fe05407da444eb113fcf64c46c5ed95a4cb71981c/independence_wave_status_window-fidelity.json`.

Generated hierarchy and click-region artifacts are retained but are not claimed as fully reviewed state-matched acceptance.
The renderer's zero-pixel self-comparison is not a repair comparison.

Parent full render:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53aefdbe7e4a7e0980126db1cc6ff63b986ad146c1463fa752e8d0935c76e404/09ba0984e0fea53a66f1f18a36d0acd204e4e64afec7f2230c6254134cd9e0d6/independence_wave_status_window-full.png`.

## Limits and disposition

The required real long mission substitutions include the existing formable message, “A formable congress or charter is in progress.”, and no-active-commitment message, “No timed commitment is currently active.”
Both are in `localisation/english/006_independence_wave_gui_l_english.yml`; no localisation was changed.
Merely requesting the `long-text` state is not proof that either real dynamic expansion was substituted.
Until that is established alongside one visible tab panel, the collision remains a source-risk finding rather than a supported specific geometry repair.

No metric, action, texticon, spendable cost, controller, click region, font, sprite, animation, gameplay result, or utility behavior changed.
No art or gameplay fallback and no simplification was introduced.
The earlier four unsupported blendframe cases, static-sibling linkage warnings, unresolved dynamic fixtures, and broader state/resolution/click-region acceptance limits remain open.
No 1366 × 768 visual acceptance or complete GUI acceptance is claimed by this bounded review.
There is no before/after source delta or repair comparison to report because source remains unchanged.
No Hearts of Iron IV process was launched and no live validation is claimed.
Only this dated handoff is worker-authored in the resumed pass; no Git staging or commit was attempted.
