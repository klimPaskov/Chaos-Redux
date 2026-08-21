# Event 018 decision-category scripted GUI final audit

Date: 2026-08-21

Status: complete for the bounded Event 018 GUI audit and repair.

## Scope

This audit was limited to `resources_found_field_management_category`, `resources_found_field_scripted_gui`, `resources_found_field_window`, and the directly linked Event 018 selection helpers, sprites, scripted localisation, and localisation. No shared or unrelated scripted GUI was changed. There were no unrelated GUI edits from this audit to revert.

The reviewed files and identifiers were:

- `common/decisions/categories/018_resources_found_categories.txt`: `resources_found_field_management_category`.
- `common/scripted_guis/018_resources_found_scripted_gui.txt`: `resources_found_field_scripted_gui` and its five element effects and enabled guards.
- `interface/018_resources_found.gui`: `resources_found_field_window` and its 34 inspected elements.
- `interface/018_resources_found.gfx`: the panel, state overlays, animation strips, navigation arrows, and action-button sprites.
- `common/scripted_effects/018_resources_found_ui_effects.txt`, `common/scripted_effects/018_resources_found_effects.txt`, and `common/scripted_triggers/018_resources_found_triggers.txt`: selection rebuilding, validation, cycling, history, and active-field guards.
- `common/scripted_localisation/018_resources_found_scripted_localisation.txt` and `localisation/english/018_resources_found_system_l_english.yml`: active, evolution-gated, suspended, sealing, and exact-seal history text.

## Repairs

The original shared 16-by-16 black navigation arrows were nearly invisible against the engraved control well. The Event 018 GFX definitions now use exact-pixel installed-vanilla 24-by-24 arrows repacked as standards-compliant Event 018-local DDS files, and the controls are centered at `(31,261)` and `(79,261)`. The final runtime files are `gfx/interface/018_resources_found/resources_found_arrow_left.dds` and `gfx/interface/018_resources_found/resources_found_arrow_right.dds`; their technical validation and hashes are recorded in `event018_arrow_repack_2026-08-21.md`.

The `Show State` recovery guard now enables when any owned state is an active Event 018 field, even if the persistent selected-field pointer is temporarily invalid. Its existing click effect validates or repairs the pointer before `goto_state`, so a one-field invalid-selection state no longer leaves the player without an enabled recovery control.

## Source and interaction audit

The category attaches the correct scripted GUI in `decision_category` context and remains suppressed during the cave world-end terminal state. All five controls have matching click effects and enabled guards, all referenced GUI elements and sprites resolve, and all text and tooltip keys resolve to Event 018 localisation or scripted localisation.

The previous and next controls are disabled in exact-seal history, the history view is read-only, and active, suspended, disturbance, breach, sealing, and closed-state visual guards are mutually staged. Animated and static variants use the same footprints and split on the animation-disable flag, so switching animation mode does not shift the layout or click regions.

The panel retains four always-present field metrics because the requested design explicitly requires Developed Yield, Excavation Depth, Workforce Safety, and Foreign Pressure. Subsurface Disturbance remains hidden until Evolution II and Breach Pressure remains hidden until Evolution III. This explicit staged requirement governs the surface despite the decisions skill's usual lower value-count preference.

The six-resource ledger summary and its detailed tooltip were retained because Event 018 must store additions separately for all six resources. The actual rendered summary and lifecycle strings are compact; deliberately overlong mock strings were rejected as non-representative after comparison with the source localisation.

The independent audit noted that arrow enabled guards use the owned-field registry while cycling rebuilds a current owned-state list. No failing transfer, annexation, closure, or conversion path was demonstrated, and the directly called lifecycle helpers rebuild the registry and validate the selection, so no speculative gameplay rewrite was made.

## MCP workflow and evidence

The event-owned GUI worker completed the required inspect-render-rewrite-comparison workflow. Compound rewrite patches were rejected with `GUI_UNSAFE_PATCH_RANGE`, a scalar rewrite retry timed out after 180 seconds, and source-mode rewrite produced valid before/proposed/diff evidence but refused to apply because repository-wide diagnostics outside Event 018 exceeded the server's global validation threshold. The accepted bounded changes were therefore applied through the normal source workflow and re-inspected and re-rendered with the MCP.

The rewrite workflow's durable before artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/249178837ba1b13a02d48e2a85218977cb7a4396f8c9ab0615fef984d2e237f3/e2c9a0d4b7a4ef33a1738721f11d7c09bb52f8c94c01714207753210107203eb/resources_found_field_window-before.png`. The worker also returned proposed, visual-diff, validation, and source-diff artifacts, but their linked bodies were pruned from the local MCP artifact store before the parent handoff was written. The complete final inspect and render evidence below governs the acceptance disposition.

Final inspect completed with `status=ok`, `code=GUI_INSPECTED`, 34 elements, zero Event 018-local diagnostics, and fully resolved Event 018-local arrow bindings. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec7d933d9106d79a0ee71f428222527844fede7d3bc058e03803935d574226eb/30612caf9b18c61e75fbd42d0ad66202edf890c15b68ddc73f889930753b8fad/gui-inspect.fd88755d3d4feae7.json`.

Final resolution and interaction-state rendering completed at `1366x768` UI scale 1, `1600x900` UI scale 1, `1920x1080` UI scale 1, and `2560x1440` UI scale 1.25 for normal, hover, and disabled states. The panel, labels, state art, arrows, action buttons, and click regions remained within bounds; the three action labels were centered; hover and disabled states were distinct; and no overlap, clipping, or scaling defect was visible. Main artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54962c95840ba3ecc241ffcd508578f05f85f901416076798cd7619b290f4876/6f620454b0b78b0bf4bd3b052edd18ae6d0d6917c8ad33373a879c1fca4b1165/resources_found_field_window-full.svg`. Resolution matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6522e56d80e8ed486aa14792c74ed9aa622742751cee0b3be63fe8fdfbbc9ecf/0d51c080ccdfa3befec65b373581b87ed1c805b0ec45c05562dda720991eb806/resources_found_field_window-resolution-scale.png`. State matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/413d5f09e9e2464f06e2dffc81bed788f4c243fde57c7057a5cebe7d72311552/388918ec6b52b52ec7bbc48605bd3205a6512535e13a1f1044b4c1b0f20e2a17/resources_found_field_window-state-matrix.png`. Click regions: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/552a4fc26afa3efc42795de1bc6d21fb4437e247f602534eb22b961c45d07d04/e1674f06186c6bcfb615812a4d4debefbe8b8a0fbf82cafceb58ed97f11c46cf/resources_found_field_window-click-regions.png`.

Realistic source-length rendering completed for the baseline with evolutions disabled, Evolution I foreign competition and commission, Evolution II disturbance, Evolution III breach, full sealing, suspension, and exact-seal history. The densest Evolution III close-up rendered `Added 999,999 / Total 999,999`, all four core values, Subsurface Disturbance, Breach Pressure, and the three-line lifecycle block without overlap or clipping. Scenario matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8bc89734e3ec67334c96076b64ca4cc3d2f699040ca41d2690557ce49ab2539/fc7594affe11eb5d6eaa05554e493cb29eb21ae3c10580320c572f6735bed8f1/resources_found_field_window-scenario-matrix.png`. Evolution III close-up: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9829b4fe7dd4c4b0f6d1d150f2a987a0451d155d1a6ac9088417dc98016df59/ad21caf0aaa802e1941952ae575be29496f1bf0949bada03fbce0dc933d08eaa/resources_found_field_window-cropped.png`.

The offline renderer does not propagate a hidden parent to its descendants, so every inactive descendant was explicitly hidden in the named scenarios. It also reports unsupported or truncated legacy vanilla button-texture data and unresolved dynamic tokens when a scenario mock is absent; the final named scenarios supplied the Event 018 values explicitly. These are renderer-fidelity limitations, not confirmed Event 018 defects.

The server's repository-wide validation headline remains false because global diagnostics hit the 2,000-entry ceiling in unrelated Event 003, Event 005, and other files. The final Event 018-local diagnostic count is zero. MCP response payloads also emitted `MCP_RESPONSE_TRUNCATED` for artifact lists larger than 32 KiB, while the linked artifacts remained readable.

## Validation disposition

Alignment, spacing, symmetry, scaling, clipping, element bounds, click boxes, hover states, disabled states, state-art swaps, active/history exclusivity, and all requested evolution presentations were reviewed. The navigation arrows are visible and centered, action labels are centered, controls do not overlap, and the invalid-selection recovery path is available.

HOI4 was not launched. Live consumer validation belongs to the user under repository policy and was not substituted by a source-only claim.

No approved or unapproved visual fallback, simplification, unrelated GUI change, or skipped Event 018 MCP surface remains in this bounded audit. The only validation limitation is the MCP server's unrelated repository-wide diagnostic ceiling and its documented offline-renderer fidelity limits.

Temporary evidence under `.tmp/event018_gui_audit` is not durable event documentation and must be deleted after the parent completes the scoped review. No `docs/assets/018_resources_found` directory was created or retained.
