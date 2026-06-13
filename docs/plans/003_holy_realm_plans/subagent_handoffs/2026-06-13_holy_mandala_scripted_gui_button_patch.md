# Holy Mandala Scripted GUI Button Patch Handoff

Date: 2026-06-13

## Scope

Audited and patched the Holy Realm Mandala decision-category scripted GUI buttons only.

## Files Changed

- `common/scripted_guis/chaosx_scripted_guis.txt`

No focus, asset, localisation, decision, or unrelated files were edited.

## Changed Surface

- Decision category: `holy_realm_mandala_category`
- Scripted GUI id: `holy_realm_mandala_category_scripted_gui`
- Scripted GUI window id: `holy_realm_mandala_category_container`
- Interface button ids:
  - `holy_realm_panel_tab_refuge_button`
  - `holy_realm_panel_tab_arhats_button`
  - `holy_realm_panel_tab_diplomacy_button`
  - `holy_realm_panel_tab_doctrine_button`
  - `holy_realm_panel_tab_warnings_button`

## Issue List

1. Critical: the five tab buttons were visually clickable but inert because their scripted GUI effects were named after the element id without the required `_click` suffix. HOI4 scripted GUI effects bind clicks through `<element>_click`, while the existing entries were `holy_realm_panel_tab_*_button = { ... }`.
2. Low: the block used spaces instead of tabs in the touched section. The patch converted the touched Holy Mandala scripted GUI block to tab indentation while leaving unrelated blocks alone.

## Before Behavior

Clicking the Holy Mandala tab buttons did not invoke the intended flag changes. The `GetHolyRealmPanelTabContent` scripted localisation therefore stayed on its default Refuge text unless flags were set by some other path.

## After Behavior

Each button now has a matching scripted GUI click effect:

- `holy_realm_panel_tab_refuge_button_click`
- `holy_realm_panel_tab_arhats_button_click`
- `holy_realm_panel_tab_diplomacy_button_click`
- `holy_realm_panel_tab_doctrine_button_click`
- `holy_realm_panel_tab_warnings_button_click`

Clicking a tab clears the other Holy Mandala tab flags and sets the selected tab flag, allowing `GetHolyRealmPanelTabContent` to show the intended tab text.

## Decision Category Lifecycle Notes

`holy_realm_mandala_category` is still wired to `scripted_gui = holy_realm_mandala_category_scripted_gui`, and the scripted GUI retains `context_type = decision_category` with `window_name = "holy_realm_mandala_category_container"`. I did not change category visibility, priority, icon, or decision lifecycle.

## Mission Quality Notes

No missions were changed. The scoped issue was a scripted GUI click binding defect, not mission owner/category/region/requirement/duration/success/failure behavior. Duplicate mission risk was not relevant to this patch.

## Cost And Requirement Clarity Notes

No decision costs or requirements were changed. The affected buttons are in-panel tab selectors, not decision purchases.

## AI Validity And Route-Lock Notes

The scripted GUI remains `ai_enabled = { always = no }`, matching the existing player-only panel behavior. No AI route behavior or decision AI weights were changed.

## Localisation And Tooltip Gaps

No localisation keys were changed. Existing button text and tooltip keys remain in use:

- `holy_realm_panel_tab_refuge`
- `holy_realm_panel_tab_arhats`
- `holy_realm_panel_tab_diplomacy`
- `holy_realm_panel_tab_doctrine`
- `holy_realm_panel_tab_warnings_short`
- `holy_realm_panel_tab_refuge_tt`
- `holy_realm_panel_tab_arhats_tt`
- `holy_realm_panel_tab_diplomacy_tt`
- `holy_realm_panel_tab_doctrine_tt`
- `holy_realm_panel_tab_warnings_tt`

## Cleanup And Exploit-Risk Notes

The tab effects only set and clear display-selection country flags. They do not grant resources, trigger events, unlock decisions, or bypass requirements. No exploit loop was introduced.

## Task-Specific Validation

- Compared the five `interface/chaosx_decisions.gui` Holy Mandala button names against scripted GUI effect ids derived as `<button>_click`; the corrected comparison returned no mismatches.
- Compared the same five button names against `<button>_click_enabled` trigger ids; the comparison returned no mismatches.
- Checked for remaining unsuffixed Holy Mandala tab effect ids matching `holy_realm_panel_tab_*_button = {`; none remain.

One first-pass `rg` comparison used unsupported lookaround syntax and failed without changing files; it was rerun with plain patterns.

## Remaining Risks

- This was not live-tested in HOI4. Confidence is based on vanilla scripted GUI binding documentation and local id matching.
- The buttons are still plain text buttons, not dynamic active-state sprites. That is existing presentation behavior and was outside this narrow inert-click fix.
