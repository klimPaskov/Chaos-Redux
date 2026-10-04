# Selected-site survivor-release row integrity

Disposition: implemented in source with parsed production-effect scenarios; post-edit GUI render and native action evidence are separately bounded below.
Acceptance basis: the user's finite-population, one-record-per-accepted-loss, truthful native action and Records requirements.

The read-only decision audit found that `camp_admin_can_release_selected_site` accepted an operating selected site with positive aggregate custody even when the aligned living origin rows did not reconcile.
The old `camp_admin_release_detainees` deliberately set `camp_admin_release_actual_k` to zero for invalid arrays or a live-row sum mismatch, but its GUI caller still suspended the site and appended a `release` history entry.
A 10-thousand aggregate custody and 9-thousand live-row parsed-source fixture reproduced the false record before the patch.
The [pre-edit 125% source render](mcp/before/locations_release_bad_rows_3_5_1/repression_ledger_window-click-regions.png) displayed Release Survivors as an active hover region beside a custody-locked physical-closure face for the declared invalid-row state.
That fixture is a declared renderer state, not proof of an actual engine click.

The existing `camp_admin_site_rows_reconciled` state trigger now participates in the selected-release availability predicate under the selected state.
Both the GUI active face and its click-enabled gate use that same predicate, and the effect checks it again before calling the foundation release.
A new neutral `camp_admin_site_release_locked_records` button has the same 120×38 native rectangle as Release Survivors, no click effect and a specific tooltip that explains the row mismatch and absence of payment, population change or release entry.
The existing authority, absent-site and empty-custody locks keep their own mutually exclusive reasons.
The release effect initializes `camp_admin_release_actual_k` to zero and appends a `release` history entry only when the foundation returns a positive actual release receipt.

The new 15th major-country parsed-source scenario executes current production helpers under three cases:

| Case | Native/effect availability | Physical and Records outcome |
| --- | --- | --- |
| 10 thousand aggregate, 9 thousand living row | Blocked by row trigger | No custody change, suspension or history |
| 10 thousand aggregate, reconciled living row | Available | 10 thousand survivors leave custody once; physical population remains unchanged; one Records entry |
| 10 thousand initially reconciled, host population already at its minimum | Pre-click source state is stale until refresh | Foundation reconciles the observed external loss to zero survivors; no release entry; intake and work remain suspended to prevent a renewed order |

The third case does not invent a death or a released survivor: the host population had already fallen and the foundation only retires the stale custody cohort as outside attrition.
The same parsed production test evaluates the scripted-GUI visible triggers directly: valid rows make only the active Release face visible, while mismatched rows make only the records-locked face visible. This catches a fixture that erroneously displays both controls at once.
The bounded test mocks engine primitives and does not prove a native effect receipt or save persistence.
The `camp_admin_site_release_tt` now names row reconciliation alongside reform authority, and the new locked tooltip supplies the blocked reason without a price grid.
`GetCampAdminSelectedConditions` now gives an operating site with positive but unreconciled custody the concise status `Custody records require reconciliation.` ahead of the ordinary supplied/shortage status; the v4 reference and matching render no longer rely on an unsupported painted warning.
The [v4 ImageGen reference](references/camp_admin_locations_records_locked_reference_v4.png) depicts the intended separate Release Locked and Closure Locked faces over a custody-record warning.
The read-only scoped decision audit verified the post-edit source gate and the zero-headroom next-refresh behavior. It also noted that the shared row-reconciliation helper verifies origin-array length but does not establish the semantic validity of each origin value. That is a distinct remaining origin-provenance limit, not a claim that every malformed origin is now blocked.

## Matched GUI evidence

Installed HOI4 MCP 3.5.1 returned `GUI_RENDERED` for the repaired invalid-row state at [1280×720](mcp/after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1280/repression_ledger_window-cropped.png), [1920×1080](mcp/after/locations_release_records_locked_3_5_1/release_invalid_rows_after_1920/repression_ledger_window-cropped.png), and [125% UI scale](mcp/after/locations_release_records_locked_3_5_1/release_invalid_rows_after_125/repression_ledger_window-cropped.png).
Each [click overlay](mcp/after/locations_release_records_locked_3_5_1/release_invalid_rows_after_125/repression_ledger_window-click-regions.png) shows Work and Purpose active, while the native Release Locked and Closure Locked faces occupy separate rectangles without active click regions.
I inspected the images at original resolution: the selected-site warning, both locked labels, six visible rows and values are legible, with no visible overlap, clipped button text or misaligned hit region.
The [after manifest](mcp/after/locations_release_records_locked_3_5_1/manifest.json) records 18 original MCP artifacts with verified sizes and SHA-256 values, exact requested scenarios, element rectangles and raw source identities.
The 1280 and 1920 renders share revision `889a6471550f81e2d3131807d3e82864c71981f90a111e526bdd4ebf91ceb8bf`; the 125% render uses revision `e2b73256c4265af05d00448e90c794bb87fe5410181764307ef11bf1d6187bd7` after unrelated workspace-index changes. Their GUI, scripted-GUI and English UI localisation file hashes are identical, and the 1280/1920 worker additionally verified the scripted-localisation hash unchanged within both calls.

The before and after 125% cropped PNGs have the same 1158×708 frame. A read-only pixel comparison found 6,822 changed pixels confined to x=774–924 and y=581–629, the Release button region; the rest of the matched declared scene remained visually identical.
The [pre-edit manifest](mcp/before/locations_release_bad_rows_3_5_1/manifest.json) records the active Release hover at revision `955d814bf9ca70e67d25e4a1b8edfaab6cc060bc157832ccb38350d05aa213e8`.
The new after layouts have no `GUI_MISSING_LOCALISATION` finding. They retain two `GUI_SCROLLBAR_CONTAINER_BOUNDARY_MISSING` warnings, and the broader static validation reports intentionally inactive locked buttons without click effects; these are not proof of native wheel, tooltip or click behavior.
The MCP fixtures explicitly declare row amounts, label values and visibility because the renderer does not execute the typed selected-state custody arrays. The parsed production-source scenarios establish the source gate and receipt behavior; neither evidence form replaces an engine interaction.
A separate first-pass valid-row diagnostic omitted the new records-locked visibility override. The renderer displayed both the active Release hit region and the locked label in the same rectangle, so that image was rejected rather than presented as a source-valid normal state. The production scripted-GUI triggers are mutually exclusive under valid and invalid row scenarios in the parsed source test. The corrected [valid-row 125% click overlay](mcp/after/locations_release_valid_rows_125_3_5_1/repression_ledger_window-click-regions.png) now explicitly hides the locked face and visibly restores the active Release Survivors label and hit region, while physical closure stays resource-locked. Its [manifest](mcp/after/locations_release_valid_rows_125_3_5_1/manifest.json) verifies six original MCP artifacts and unchanged GUI, scripted-GUI, UI localisation and scripted-localisation hashes within the call at revision `c0b76d49a160b9ec8278e9d4bc082e0204de16d6f064eff6e5b6906a440556ce`. This remains a declared source-render state, not a native click receipt.

Installed `hoi4.reference_context`, `reference_search`, `reference_read` and `source_lookup` were not callable on this task connection, so local reference sections were read directly.
Offline `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md` lines 194–205, SHA-256 `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`, documents per-element click and visibility triggers; `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md` lines 227–249, SHA-256 `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`, documents native button text and tooltip fields.
Installed `common/scripted_guis/_documentation.md` lines 1–68, SHA-256 `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, is the primary syntax reference for named click effects and triggers; installed vanilla `RAJ_tax_fraud_scripted_gui.txt` lines 8–28, SHA-256 `2f66a9db96e512032e9727e42dc609bb6b76082af1195e4cdf4d8d081b2f477a`, and its `interface/RAJ_eic_tax_fraud.gui` lines 53–81, SHA-256 `b81d7f9cbffe8eaa2d9f47a3ee0ee0c2e482d0535fbd67a513dac4fc01332c6c`, provide a vanilla separate-element visibility precedent.
Offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` lines 73–95 and 656–685, SHA-256 `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, documents BOM encoding, one-line escaped tooltip text and first-matching scripted-localisation branches. The repository's key style omits the optional `:0` version marker.
The closest package precedent is the same Locations panel's existing active/locked Work, Purpose, Release and Dismantle controls.

The full static English localisation audit parsed 338 files without parse errors or duplicate keys and found no missing key on the camp package surface, including the new Release Locked face, status and tooltips.
It reports 262 undefined bindings elsewhere in the repository, one missing BOM in the unrelated `006_independence_wave_host_response_l_english.yml`, and one `camp_admin_rows_initialized` flag under an implementation-only hidden trigger; none establishes that the new locked control displays a raw key. The touched camp UI localisation retains its BOM and all three new keys resolve once.
Its source-only JSON is [archived here](mcp/after/selected_release_localisation_audit.json).

MCP source renders cannot execute a native click, reveal the tooltip popup or prove the engine's custody row reconciliation; those remain acceptance limits.
