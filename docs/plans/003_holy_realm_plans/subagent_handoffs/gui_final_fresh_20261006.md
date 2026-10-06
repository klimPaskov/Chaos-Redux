# Event003 Mandala GUI Final Fresh Audit — 2026-10-06

Disposition: implemented source is unchanged; the default Refuge view received a successful production render and visual review; the expanded state matrix and matched source comparison remain unresolved because their single authorized render attempts produced no artifacts.

## Ownership and accepted basis

This audit is limited to the Event003-owned `holy_realm_mandala_category_container` inside `interface/chaosx_decisions.gui`.

The entry event `chaosx.nr3.1` is in `events/003_the_holy_realm.txt`; its Holy Realm country setup establishes the `holy_realm_active` identity used by the dedicated `holy_realm_mandala_category` registered in `common/decisions/categories/003_holy_realm_categories.txt`.

That category attaches only the `holy_realm_mandala_category_scripted_gui` from `common/scripted_guis/003_holy_realm_scripted_guis.txt`; the scripted GUI binds the Mandala image and five existing tab actions.

The source and accepted reference handoffs document this as the bounded Event003 Mandala view, rather than a shared event log, details framework, settings view, or generic GUI.

The parent accepted the five-tab value budget Refuge/Arhats/Diplomacy/Doctrine/Warnings = 3/3/3/4/4, two centered rows, the selected `>` cue, and Refuge as the default when none of the other four tab flags is set.

The reference and acceptance record is `docs/plans/003_holy_realm_plans/subagent_handoffs/gui_release_20261005_evidence/reference_acceptance.md`; its image is `reference_mandala_tabs_values_annotated.png` in the same evidence folder.

Parent review explicitly accepted the current default Refuge image: the Mandala edges are clean, text and values fit, the selected marker is centered, and all five separate hit regions align with their painted faces.

## Exact source identifiers

| Surface | Identifier or file |
| --- | --- |
| Event entry point | `chaosx.nr3.1` in `events/003_the_holy_realm.txt` |
| Dedicated category | `holy_realm_mandala_category` in `common/decisions/categories/003_holy_realm_categories.txt` |
| Dedicated scripted GUI | `holy_realm_mandala_category_scripted_gui` in `common/scripted_guis/003_holy_realm_scripted_guis.txt` |
| Dedicated window | `holy_realm_mandala_category_container` in `interface/chaosx_decisions.gui` |
| Sprite registration | `interface/003_holy_realm.gfx` |
| Scripted-localisation getters | `common/scripted_localisation/003_holy_realm_scripted_localisation.txt` |
| English GUI strings | `localisation/english/003_the_holy_realm_l_english.yml` |
| Event decision entry list | `common/decisions/003_holy_realm_decisions.txt` |
| Promoted state sheets | `gfx/interface/decisions/003_holy_realm/mandala_states/holy_realm_mandala_{dormant,teaching,meditation,awakened,wrathful,final_silence,empty}{,_animated}.dds` |

The active sprite getter is `GetHolyRealmMandalaSprite`; displayed panel getters are `GetHolyRealmPanelPrimaryValueLine`, `GetHolyRealmPanelSecondaryValueLine`, `GetHolyRealmPanelRiskValueLine`, `GetHolyRealmPanelStageLine`, `GetHolyRealmPanelDoctrineLine`, and `GetHolyRealmPanelTabContent`.

The five button getters are `GetHolyRealmPanelTabRefugeButtonText`, `GetHolyRealmPanelTabArhatsButtonText`, `GetHolyRealmPanelTabDiplomacyButtonText`, `GetHolyRealmPanelTabDoctrineButtonText`, and `GetHolyRealmPanelTabWarningsButtonText`.

The directly exercised value keys include `holy_realm_mandala_{refuge,arhats,diplomacy,doctrine,warnings}_{primary,secondary}`, `holy_realm_mandala_doctrine_risk`, `holy_realm_mandala_warnings_risk`, `holy_realm_mandala_empty_line`, and the five `holy_realm_panel_tab_*_selected` strings.

## References and precedents reviewed

The accepted design references are the Event003 plans and handoffs listed above, including `gui_release_20261005.md`, `gui_release_mcp_followup_20261006.md`, `mandala_tab_filtering_20261006.md`, `mandala_real_frames_20261006.md`, and the asset `release_animation_20261006/preview_index.md` plus `notes/runtime_promotion_report.json`.

The project reference image maps its emblem, two value rows, two status columns, five native tab buttons, and explanatory text to the accepted Event003 hierarchy; the existing native controls remain separate from the state artwork.

The installed GUI documentation `_documentation.md` was read at lines 1–146, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`; it covers the decision-category scripted-GUI scope, click effects, triggers, and properties.

The offline Scripted GUI modding wiki sections Effects lines 179–193 and Template lines 549–628 were read at revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`; the offline Interface modding buttonType section lines 227–256 was read at revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`.

The offline Decision modding wiki revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` was read for category and decision integration.

Installed vanilla precedents inspected were `interface/sov_paranoia_system_scripted_gui.gui` with `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`, and `interface/countrydecisionview.gui` around lines 114–120 for native control state.

No web wiki was used.

## Files changed and source identity

No GUI, scripted-GUI, GFX, localization, gameplay, asset, index, commit, or workbook file was modified by this audit.

The only new files are this handoff and the two receipts in `gui_final_fresh_20261006_evidence/`.

Immediately after the current exact-window inspect and throughout rendering, the whole shared `interface/chaosx_decisions.gui` SHA-256 was `4A87919352BE1A3748551085A34749B6BDC5F4C849A839846CEF97D1A0C564AD`.

The whole-file hash includes the parent-owned Event002 cure outside this window; the normalized current Mandala block at `gui_mandala_container_current.gui` has SHA-256 `E89E794DE43039D40D7C2DA63713602DA08BC2E0F69F2576DDDD05754AD82289` and is line-identical to the accepted `gui_mandala_container.after.gui` snapshot (`diffCount = 0`).

Current linked source hashes at the end of this audit are `common/scripted_guis/003_holy_realm_scripted_guis.txt` `7C247E4F79DDA8B9ABCD1CCD7CBB1BB04A6685065529F34F7AC34EF3C636C260`, `common/decisions/categories/003_holy_realm_categories.txt` `88AB02D4E66E00D3CCDB23C0E03525DDF19137BA979CD4BFA0D4B99FF9445150`, `common/scripted_localisation/003_holy_realm_scripted_localisation.txt` `EF690E66ACA2F30088BA1C4F80CF95A6E0C078CA608ECEC5314EB3D18B9C5A1C`, and `localisation/english/003_the_holy_realm_l_english.yml` `CF8FC3E5A675BE0CA159455B83CFD6391B8621DDD0291522F2D39CF7F52720DD`.

The seven static sheets are 420×420 and the seven animated sheets are 6720×420, 16 frames each, as recorded by the existing promotion handoff; the 10 static and two portrait playback loops are separate consumers and do not alter the Mandala sheet dimensions.

## Pre-change and current MCP evidence

The historical pre-change Refuge render is archived under `gui_release_20261005_evidence/`: the full image SHA-256 is `EB77F071C6817BDBA102B16882D1911200EA442CFFD4E6BD9D1F0276A1085B77`, crop `F372219753FA1EBD24F9E5C57EFAC663B829F99E33BDFB502631CECB70B69224`, annotated image `A006BF7C2E42ABDF0DF3F6471F244A355044153C4C0101B8ACED5E7EF7D849BC`, and click-region image `7A86602D638DCBBB2438A2B7F47CBCBC24760A2FC3FEA4FD2EBB1C57DB5AC830`.

That historical scenario is TIB on 1936.1.1 at 1920×1080/UI1, but it predates the current Mandala texture promotion and its explicit Refuge tab flag differs from the current default-no-tab-flags fixture; it is useful as a historical geometry reference, not a matched texture or source revision comparison.

The accepted reference image SHA-256 is `AA4B2290BBD24484947B8D67E39C18556F36F32FEF38194A8A3EAAE2F68D96FF`.

The fresh current-source `hoi4.gui_inspect` used the exact window and workspace and returned complete coverage, 13 inspected elements, `skippedSourceCount = 0`, shared revision `09fd358650db3dd6b8ed913664d93d8a1299fd1bb0915abbcef64adc8cbaf0f1`, and artifact SHA-256 `c7f1e382087e91e347ad50f1e0939811ce921c98f9752858b764d3d06fec6e1c`.

The separate pre-Event002 inspect snapshot `gui_final_fresh_20261006_evidence/gui_inspect.json` is 561,551 bytes with SHA-256 `8be9fcde1f81148ff4215e194a441c95269205bd081e9db01393f08786929165`; it is explicitly not the current revision.

The successful current Refuge production render receipt is `gui_final_fresh_20261006_evidence/gui_render_minimal_receipt_20261006.md`; it records the TIB default fixture, 1920×1080/UI1, one `normal` state, `values.is_ai = false`, no tab flags, and no baseline, comparison scenario, or related scenarios.

Its full PNG SHA-256 is `4bc1f13b3590260f91a127e5aa12e60bb2a44b3f345ed850d92a1c457411a678`, crop `092dbdb8f6dee606029f93711c7b33046db87619777ddb2aa4a6faa1e9bf28cc`, annotated image `94be39328bffd823ace0158c5a9d167c2ca118915b1ca65185a8df98aa77fd14`, click-region image `c71c42e2dff62f9cbfa571594e5f0f1c2dc2fafef83357ec1c0e01f6b9dceed9`, and source map `6c493c5c1bed9d9390b200862bf4a1e73beb98b0d1c12f85dea492dd347b107e`.

The parent reviewed the annotated and click-region views from the content-addressed cache; I reviewed the full and crop views and found no visible clipping or overflow in the default Refuge view.

The successful request returned a `comparison.json` with zero changed pixels, but supplied neither an old source nor `comparisonScenario`; that result is not a before/after comparison.

The first current-source request that included the archived `.gui` as `sourceBaseline` timed out after 600 seconds with no artifact, so no matched current-source versus historic-source visual comparison exists.

## Layout, action, and text budgets

The owned root is a fixed 470×560 decision-category child; the Mandala element is 218.4×218.4, the body text area is 454×110, and the five tab hit areas are 123×34 each.

The rendered hierarchy is Mandala image, two value rows, stage and doctrine columns, two centered tab rows, and the selected tab's short explanation.

The accepted visible mechanic-value budget is 3/3/3/4/4 across Refuge, Arhats, Diplomacy, Doctrine, and Warnings; the current Refuge image shows its three values, while the four other tab budgets were not visually rendered in this pass.

The GUI exposes five tab-navigation controls and no gameplay-changing button; its GUI cost count is zero, so no cost string or cost texticon is displayed here.

The successful Refuge view has two lines of explanatory body text; the long Diplomacy and warning bodies were supplied in the blocked matrix and remain unreviewed.

The panel's displayed numeric lines use native localized values and color formatting; the empty Refuge risk row comes from `GetHolyRealmPanelRiskValueLine`'s intentional empty-line fallback and is not omitted copy.

## Visual review and diagnostics

In the current 1920×1080/UI1 Refuge render, the transparent Mandala edges are clean, the image and both value rows fit the 470×560 container, the stage/doctrine columns stay separate, the five tab buttons are centered in two rows, and `> Refuge` is centered on its face.

The annotated/source map places all content within the container; the click-region view shows five separate 123×34 regions aligned to their painted button faces without overlap.

The empty Refuge risk row is intentional source output; parent visual review accepted it.

The current inspect and rendered validation report `GUI_ACCIDENTAL_CLIPPING` for the Mandala's 218.4-pixel extent resolving to 218.39999999999998 pixels; the reviewed Refuge screenshot shows no visible edge cut, but the diagnostic remains recorded.

The render reports `GUI_MISSING_FONT` for the empty `holy_realm_mandala_chaos` value row using `hoi_16mbs`; the one-space Refuge risk fallback explains why that row carries no visible text in this fixture, but font metrics remain unresolved for a nonempty warning state.

The renderer reports informational `GUI_INCONSISTENT_SPACING` because sibling vertical gaps range from 2 to 12 pixels; the parent reviewed the current image without identifying a visible spacing defect.

Other current default-state checks report no visible overlap, text overflow, alignment mismatch, off-center tab label, click-bound mismatch, conflicting click regions, missing sprite/texture/localization, z-order risk, tab conflict, or resolution drift.

Fidelity marks six `pdx_tooltip` elements as ignored; the tooltip keys exist in localization, but this pass contains no rendered tooltip view.

The validator's `GUI_STATE_COVERAGE_MISSING` list contains hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation; the Refuge button is visually selected in the explicit scenario, but the expanded matrix that would resolve selected-tab and content cases did not produce images.

## State matrix and resolution evidence

| Coverage | Result |
| --- | --- |
| Default Refuge, no tab flags, dormant animated sheet, selected Refuge cue | Visually reviewed at 1920×1080/UI1; accepted by parent |
| Arhats, Diplomacy, Doctrine-at-maximum, and Warnings selected cues | Included in one adjusted matrix request; blocked before render; unresolved |
| Doctrine nonempty risk line and Warnings empty/nonempty risk cases | Included in the blocked matrix with Chaos 0, 999, 1000, and 1001 fixtures; no matrix images; unresolved |
| Hover over Arhats while Refuge remains selected | Included in the blocked matrix; unresolved |
| Dormant / teaching / meditation / awakened / wrathful / final-silence / empty Mandala sheets | Dormant is visible in the accepted default image; the six remaining sheets were included in the blocked matrix and remain visually unreviewed |
| Expanded matrix resolution | Requested once at 1280×720/UI1 after the 1920 matrix exceeded its aggregate pixel budget; blocked by a native animated DDS texture-plane reservation; no 1280 matrix image exists |

The 1280×720 viewport change does not establish a lower-scale view of the fixed native 470×560 panel because the 6720×420 animation-sheet reservation still consumed the request budget before rendering.

The complete request and both exact aggregate-budget results are recorded in `gui_final_fresh_20261006_evidence/gui_render_matrix_budget_block_20261006.md`.

The root 1920×1080 default render is the only current-source production image in this audit; no state-matrix or cross-resolution visual completion is claimed.

## Action coherence and remaining integration

The `holy_realm_mandala_category_scripted_gui` maps each native tab button to its matching existing click action and country flag; the successful Refuge fixture shows the default selected cue and matching Refuge body.

The parent-owned tab-filter handoff maps the 47 existing decisions into 12/9/16/5/5 late-route counts and projects the TIB starting counts as Refuge 3, Arhats 2, Diplomacy 1, Doctrine 3, Warnings 0; this GUI audit does not claim a live decision-list render or audit decision costs/effects.

The matrix's tab fixtures preserved matching flags, selected labels, body getters, and per-control button states, but those action/body combinations are scenario inputs, not observed campaign behavior.

Runtime asset promotion is documented under commit `4dfdc7c7` by the existing animation handoff; this audit did not install, edit, or alter any asset.

The parent retains review of the unrendered tab and sprite states, any decision-owner integration, and source/runtime integration; the user retains live-game validation.

## Simplifications, omissions, and blockers

No layout or source simplification was made by this audit.

The 1920×1080 sourceBaseline comparison timed out without artifacts; the first 1920×1080 matrix was rejected at 68,452,789 aggregate pixels; and the one parent-authorized 1280×720 matrix retry was rejected at 68,276,183 aggregate pixels because the native final-silence 6720×420 texture plane added 2,822,400 pixels to a 65,453,783-pixel reservation.

The exact blocker and no-retry decision are in `gui_final_fresh_20261006_evidence/gui_render_matrix_budget_block_20261006.md`; all matrix states other than the default Refuge image remain unresolved, and the comparison, tooltip, alternate-resolution, and live-game evidence remain pending.

### Follow-up: four selected-tab layouts

The parent authorized one additional narrow `hoi4.gui_render` request for Arhats, Diplomacy, Doctrine, and Warnings at 1920×1080/UI1, all on the natural dormant sprite; the source hashes remained `interface/chaosx_decisions.gui` `4A87919352BE1A3748551085A34749B6BDC5F4C849A839846CEF97D1A0C564AD` and Mandala block snapshot `E89E794DE43039D40D7C2DA63713602DA08BC2E0F69F2576DDDD05754AD82289`.

Its four-fixture preflight was 11,116,800 pixels, below 67,108,864; the single call returned `Transport closed` before structured content or artifacts, so no images, diagnostics, click regions, or validation fields were returned and no retry was made.

The exact fixture IDs, source getter values, preflight math, error, and resulting coverage gap are recorded in `gui_final_fresh_20261006_evidence/tab_subset_20261006/render_attempt_receipt.md`.

Arhats, Diplomacy, Doctrine, and Warnings visual/click coverage remains unresolved; the separate successful Refuge image is unchanged and does not prove these tab states.

The only skill workflows used were `chaos-redux-scripted-gui`, `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-frame-animation`; no skill or source file was modified.
