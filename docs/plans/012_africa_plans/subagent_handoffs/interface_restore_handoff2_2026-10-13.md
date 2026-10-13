# Event 012 animation preference restoration

Disposition: implemented within the delegated Event 012 interface restore. The parent acceptance basis is the explicit instruction to restore the removed animation toggle from `2fbdf2f4cdd7af607b56987a91b64912e76723a4` while retaining the newer League-completion and Authority qualification. This follows the owner's standing restore direction recorded in `docs/plans/handoffs_2026-10-13/00_common_rules.md` and the Event 012 row for `2367ef0877a3` in `docs/plans/interface_restore_audit_2026-10-13.md`.

Event ownership is explicit in `common/scripted_guis/012_africa_charter_scripted_gui.txt`: `africa_charter_window` has `context_type = decision_category` and binds to `window_name = "africa_charter_window"`. `interface/012_africa_charter.gui` defines that sole root container. `common/decisions/categories/012_africa_categories.txt:13` attaches this scripted GUI to the Event 012 category. No shared framework or unrelated interface was edited.

Changed files:

- `interface/012_africa_charter.gui` restores `africa_charter_toggle_animation` at its historical position `(846, 68)`, using `GFX_chaosx_button_123x34`, `hoi_14mbs`, scale `0.72`, the existing click sound, and its tooltip.
- `common/scripted_guis/012_africa_charter_scripted_gui.txt` restores `africa_charter_toggle_animation_click` and its always-enabled click trigger. The effect sets or clears the player-country flag `africa_charter_gui_show_animation`, matching the effect at lines 22–29 and trigger at line 217 of the accepted parent revision. The four seal/ring visibility predicates combine that preference with the current League/Authority qualifications.
- `localisation/english/012_africa_charter_gui_l_english.yml` restores the two historical GUI strings, `africa_charter_gui_toggle_animation` and `africa_charter_gui_toggle_animation_tt`, with their exact text from the parent revision. No other localisation wording changed.

The accepted source reference is the historical Event 012 window and scripted-GUI source at `2fbdf2f4cdd7af607b56987a91b64912e76723a4`. Commit `2367ef0877a31c2e2a11708da06c92447f6a4098` removed the button, its effect and click trigger, and replaced the two preference gates with League/Authority state-only gates. This patch restores the removed behavior and keeps those newer live-state conditions. The working-tree files and their prior bytes/diffs were snapshotted before editing in ignored `.tmp/interface_restore_handoff2/event012/`.

The current native mapping keeps the toggle as a real `buttonType`; it is not painted into art. It controls the two existing top-right paired sprite consumers: `africa_charter_seal_activation_animated` / `_static` and `africa_charter_authority_ring_animated` / `_static`. Their registrations and textures already exist in `interface/012_africa_charter.gfx`; the button sprite is registered in `interface/chaosx.gfx` and its `gfx/interface/chaosx_button_123x34.dds` texture is present (123×36 pixels). No raster asset, GFX registration, new art, or sprite name was added.

The source state matrix is exhaustive for these paired consumers:

| Preference flag | League completion / Authority | Animated consumer | Static consumer |
| --- | --- | --- | --- |
| Absent or cleared | Any League state / any Authority | Hidden | Visible |
| Set | League incomplete | Hidden | Visible |
| Set | League complete | Visible | Hidden |
| Set | Authority below `constant:africa_measure.medium` | Hidden | Visible |
| Set | Authority at or above `constant:africa_measure.medium` | Visible | Hidden |

The toggle changes only the presentation preference. It has no gameplay cost, requirement, AI equivalent, or gameplay effect. Its historical tooltip states the behavior clearly. It adds one non-gameplay settings control and no mechanic value or spendable cost; the existing dynamic Authority/League values and actions are unchanged. No cost texticons apply.

The source canvas is 1000×680 at `(0, 0)`. At both requested viewport fixtures—1920×1080, UI scale 1, and 1366×768, UI scale 1—the historical button origin is `(846, 68)` and remains inside the source canvas. Its registered texture is 123×36, yielding a nominal source extent of `(846..969, 68..104)` before scale and approximately 89×26 at its declared 0.72 scale. The engine's effective hit region after scaling is not established by source geometry alone.

A direct DDS alpha inspection resolved the ring/button paint overlap. `charter_authority_ring_sheet.dds` is 640×64, giving ten 64×64 frames; `charter_authority_ring_static.dds` is 64×64. At the recent ring position `(820, 12)`, the button's scaled painted face intersects ring source columns 26–63 and rows 56–63. Across the static image and all ten animation frames, 135 of 304 ring pixels in that crop have nonzero alpha and 91 have alpha above 128. The corresponding button-source crop has nonzero alpha at 593 of 594 pixels and alpha above 128 at 508 of 594. This is a real painted overlap, with the later button control drawn over ring pixels. The ring has therefore been returned to the exact historical `(792, 12)` position from the accepted parent revision. In that position the button intersects only ring columns 54–63 and rows 56–63, whose alpha is zero across the static texture and every animation frame; the restored button face no longer covers painted ring pixels.

The historical ring position's 64×64 frame does intersect the current secondary-values text-box rectangle at `(690, 48)`, `maxWidth = 120`, `maxHeight = 48`, by 18×28 pixels. The values are drawn after the ring in the native GUI definition, as they were after the ring in the historical source. This retained source ordering places text above the ring art. Rendered glyph interaction and contrast remain for the parent-owned matched render; no text geometry or content was altered.

Guidance and precedent read for this repair: offline `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`, lines 194–205, revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`, describes `<element>_<modifiers>_click_enabled` and `<element>_visible`; offline `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, lines 369–386, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`, documents element-relative coordinates and container anchors. Installed `common/scripted_guis/_documentation.md`, lines 52–64, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, documents button effects and per-element triggers. Vanilla `interface/sov_paranoia_system_scripted_gui.gui`, lines 20–55, provides a native scripted-GUI example with separate icon and text consumers.

Visual acceptance uses the exact historical native button and ring position from the cited parent revision; no new reference artwork or redesign was requested. Source review covered the default/animation-off and animation-on branches, both League states, both sides of the Authority threshold, the effect/trigger binding, available texture registrations, button/ring alpha geometry, and the button's logical bounds at both requested viewport sizes. The live `reference_context` and targeted `reference_search` MCP calls succeeded. A narrowed `reference_read` and a vanilla `source_lookup` call did not return before cancellation; equivalent local offline wiki, installed documentation, and vanilla source excerpts were read directly. Per the parent instruction, no GUI inspect/render call was made. There are no baseline/intermediate/final render artifacts, rendered hit regions, or observed-game checks in this handoff; the parent owns the final matched renders and their review.

No parent/decision-owner gameplay action-integrity evidence is needed because this is a presentation preference only. Remaining check: parent render review should confirm the button face and its hit region, and check text-over-ring glyph contrast at the restored historical position, at 1920×1080 and 1366×768, scale 1. The button/ring painted-alpha conflict is removed in source. No simplifications or gameplay changes were made.

## Parent integration follow-up

The restored animation button retains the existing installed-font repair: `hoi_16mbs` replaces its unregistered historical `hoi_14mbs` token without changing its coordinates, sprite, scale, label or action.
The parent’s post-restore MCP render timed out after 600 seconds; final visual checks are assigned to Handoff 1 rather than being claimed here.
