# Event 006 additive focus carrier fail-closed re-audit - 2026-07-28

## Scope and verdict

This bounded audit covers the current fail-closed carrier patch in four scripted files. Source-level carrier gating, setup ordering, and generation cleanup are sound. IW-012 has a reviewed source carrier. Generic meaningful-tree insertion remains an explicit HOLD; this patch does not claim that a shared-focus block can be injected into an arbitrary existing vanilla tree. No gameplay file was edited by this audit.

## Route and carrier coverage

| Surface | Evidence | Result |
| --- | --- | --- |
| IW-012 Iceland carrier | `common/national_focus/iceland.txt:28-42` imports the Event 006 shared root, seven generic overlay focuses, and four ICE route focuses. `common/scripted_effects/006_independence_wave_ice_package_effects.txt:348-355` registers the carrier before additive assignment. `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt:149-152` requires the carrier, `iceland_tree`, and additive receipt. | Source contract PASS; live shared-focus visibility and save/load persistence remain HOLD. |
| Event 006 overlay route | `common/national_focus/006_independence_wave_focus.txt:3151-3276` contains eight generic overlay focuses with `available`, rewards, tooltips, and `ai_will_do`. | Source content present; carrier admission is package-owned. |
| IW-012 formal route branch | `common/national_focus/006_independence_wave_focus.txt:3286-3423` contains four mutually exclusive route focuses: `independence_wave_ice_choose_constitutional_route`, `independence_wave_ice_restore_traditional_authority`, `independence_wave_ice_establish_emergency_command`, and `independence_wave_ice_accept_patron_mandate`. | Route blocks present and mutually exclusive; existing route-AI audit remains unchanged. |
| Generic meaningful-tree adapters | Example IW-179 requests additive assignment at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:734-746`, while its admission trigger requires the additive flag at `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:384-386`. No reviewed carrier registration exists for this adapter. | Correctly fail closed: no additive flag, no prepared receipt, and no package setup-complete claim. |
| Full Event 006 framework | `common/scripted_effects/006_independence_wave_focus_effects.txt:48-53` still uses explicit `load_focus_tree = independence_wave_focus_tree` for full-framework ownership. | Separate full-tree path; no dynamic insertion or overwrite introduced. |

## Fail-closed behavior and ordering

- `can_attach_independence_wave_additive_focus_carrier` at `common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-64` requires an active Event 006 country, `independence_wave_focus_carrier_registered`, the ICE lifecycle flag, and `has_focus_tree = iceland_tree`.
- `independence_wave_assign_focus_framework` at `common/scripted_effects/006_independence_wave_focus_effects.txt:43-73` clears stale overlay/missing-carrier flags, records assignment intent, sets `independence_wave_additive_focus_overlay` only when the carrier trigger passes, and otherwise sets `independence_wave_focus_overlay_carrier_missing`.
- IW-012 initialization proves the tree before assignment: `can_initialize_independence_wave_iw_012_package` already requires `has_focus_tree = iceland_tree`; setup then refreshes lifecycle state, registers the carrier, and assigns the additive mode at `common/scripted_effects/006_independence_wave_ice_package_effects.txt:340-355`.
- Generation reset dispatches package cleanup before centralized focus cleanup at `common/scripted_effects/006_independence_wave_effects.txt:383-389` and `:2820-2824`. `independence_wave_clear_focus_runtime` clears both carrier and missing-carrier receipts at `common/scripted_effects/006_independence_wave_focus_effects.txt:80-90`. The ICE package cleanup clears lifecycle state at `common/scripted_effects/006_independence_wave_ice_package_effects.txt:410-441`.
- The assignment variable still records `additive_overlay` on a failed carrier admission. It is diagnostic intent only; all current prepared/package gates additionally require the additive flag, so it does not by itself publish a successful package.

## Icons, localisation, and reward alignment

| Route surface | Icon evidence | Localisation/reward result |
| --- | --- | --- |
| Eight generic overlay focuses | Existing `GFX_goal_independence_wave_*` references at `006_independence_wave_focus.txt:3151-3276`; no icon ids changed. | Focus ids and `_tt` keys are present in `localisation/english/006_independence_wave_focus_l_english.yml`; rewards match the existing focus bodies. |
| Four ICE route focuses | Existing constitutional, traditional, emergency, and patron icon ids at `006_independence_wave_focus.txt:3286-3410`; no icon ids changed. | Focus and custom tooltip keys are present; route rewards remain the existing route-lock effects. |
| Unadmitted generic adapters | No package-specific icon or localisation surface is exposed by this patch. | Intentional HOLD pending a reviewed owning-tree carrier; no missing key or reward mismatch was introduced. |

## AI behavior gaps

- All inspected Event 006 overlay and ICE route focus blocks retain `ai_will_do`; no AI weights were changed in this carrier patch.
- Generic adapters without a carrier cannot expose their overlay focuses to AI, by design. Each future adapter needs a source-reviewed carrier and route-aware AI admission before promotion.
- The assignment variable caveat above should remain visible to admission audits; consumers must not treat that variable alone as runtime readiness.

## Validation and artifacts

- Required offline Paradox wiki pages and installed vanilla documentation for national focuses, `has_focus_tree`, `shared_focus`, and `load_focus_tree` were consulted.
- PowerShell static check on exactly the four touched scripted files: focus triggers `91/91` braces, focus effects `408/408`, ICE effects `198/198`, and ICE triggers `66/66`; no negative nesting or unsupported `<=`/`>=` comparisons.
- MCP inspection of the unchanged central tree returned layout hash `a7bd7fe6afd3db003f656ef344cedcc280edb3c30cb5e0c5f12cab316890acb1`, `validation=false`, and 14 existing blocking geometry diagnostics. Artifact: [central focus inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4563c13d9fbf1d1146bcccfc2af585afb29287e44a77ce953ad144660559d0d2/fbb52e5765f60472315f9a6699ea0648062dca0b229cac2e1085d0454d7cda03/focus-inspect.1b173f631a883d1a.json).
- MCP inspection of `iceland_tree` found 89 vanilla focuses and does not expand imported `shared_focus` nodes. It reported `validation=false` with 193 blockers dominated by inline truncation and vanilla missing-sprite diagnostics, so it is not runtime proof of the 12 imported Event 006 blocks. Artifact: [ICE focus inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ef9ff01681630135078619a667b599456bce600e316bcf91ab229581b7a75c6/bcbf55b68e7a1b0973add189976a08ef28516f792919283f87aafa17dbcc6334/focus-inspect.c8e40164d5165814.json).
- The existing exact-vanilla `iceland.txt` body/import comparison remains the source proof for the reviewed carrier; live game launch, save/load, and consumer validation were intentionally skipped per repository instructions.

## High-priority fixes and remaining risks

1. Keep generic meaningful-tree overlays on HOLD until each adapter registers a reviewed owning-tree carrier and its prepared trigger proves that carrier.
2. Obtain parent-owned runtime evidence that the ICE imports are visible and persist through save/load; MCP inspection cannot expand `shared_focus` imports.
3. Keep the central focus-tree geometry reflow separate: the 14 MCP blockers are pre-existing and unrelated to carrier gating.
4. Do not add an unsupported dynamic shared-focus insertion effect or overwrite an existing vanilla tree as a "fix."

## Handoff

- Gameplay files reviewed (existing patch, not edited here): `common/scripted_triggers/006_independence_wave_focus_triggers.txt`, `common/scripted_effects/006_independence_wave_focus_effects.txt`, `common/scripted_effects/006_independence_wave_ice_package_effects.txt`, and `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt`.
- Focus ids reviewed: the eight Event 006 overlay ids and four ICE route ids listed above. No focus ids, localisation keys, or icon ids changed in this audit.
- Route behavior is fail-open before the patch (an additive request could expose the overlay flag without a carrier) and fail-closed after it (only the reviewed ICE carrier exposes the flag; unreviewed adapters remain unadmitted).
- No simplification was hidden: generic meaningful-tree insertion, live visibility, save/load persistence, and central geometry validation remain explicit HOLD items.
