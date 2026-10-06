# Event002 shared super-event window audit

Status: the slot-1 popup has a successful matched production render and source comparison; the corrected multi-slot visual pass is incomplete because the final GUI render timed out after 600 seconds.

Scope was limited to the single shared window `chaosx_super_events` in `interface/chaosx_super_events.gui`. I made no source, GFX, sound, asset, index, spreadsheet, or commit changes.

The live MCP schemas exposed `hoi4_gui_inspect` and `hoi4_gui_render` in workspace `mod_chaos_redux_ea3b2d67c2c0`. The artifact resource template responded, and inspect plus two render calls succeeded. No separate health or version route was exposed.

The current source hashes are recorded in [the evidence manifest](../super_gui_evidence_20261006/mcp_evidence_manifest_20261006.json). The shared window is 899×592 and its source hash is `1954AFCF0E49BDB501BE51E69E2F85089867023C99A018C6CE3FA8E4EA3B4CF3`.

For slot 1, the accepted fixture `zombie_kursk_1936` rendered at 1920×1080, UI scale 1, normal state, with generated scenarios disabled. The window is centered; the image, description, title, Quotation heading/body, and close button fit their regions. I found no visible clipping, text overflow, raw localization key, or button-label alignment defect.

The production full SVG was range-read in 57 exact byte ranges and verified against its resource URI SHA256. It was converted with the installed `hoi4-agent-tools/node_modules/sharp` package into a 1920×1080 PNG for image review. A 920×620 inspection crop is saved beside it and is explicitly a derivative, not a separate production render.

The matched source comparison reports 795,694 changed pixels and a changed ratio of 0.3837258873 against `docs/plans/002_zombie_outbreak_plans/super_gui_evidence_20261005/before/chaosx_super_events.gui.before`, whose SHA256 is `152053B333F6D57283ED355642D035625F4A873764778265526E8FAC1953EF24`. Both sides resolve the current `GFX_super_event_zombies` texture and current DDS SHA256 `748799A096C58A639D2EEF1717142CAAA2A9703807250C8ED74958F2EC83121C`; this is a GUI-source comparison, not an asset comparison against the historical film-scene image.

The first successful related-scenario render covered slot 2, slot 3, and slot 5 at the same resolution and scale. Its validation passed 43 checks. It reported no text-overflow, click-bounds mismatch, conflicting click regions, missing localization, missing sprite/texture/font, unresolved click region, or unresolved visibility findings. The source graph produced 18 background-under-content overlap warnings, which matched the expected layered panel, three non-blocking missing-trigger warnings for `super_event_close`, and 13 missing-state-coverage warnings because only the normal state was requested.

The click-region image shows `super_event_close` covering the visible 352×48 button face at (550.5, 729). The layout report marks it clickable and enabled; its button label is centered and has no overflow. The inspector still reports `GUI_BUTTON_TRIGGER_MISSING`: “Button super_event_close has no matching scripted GUI visibility/enabled trigger.” This is a source warning for the parent to review; the returned evidence does not show a hit-region mismatch.

The first slot-2 fixture displayed the literal `[azl_faction_leader.GetName]` because its direct `GetSuperEventDesc` override retained the token. That preview is not accepted as source-correct description evidence. I verified that `establish_anti_zombie_league` saves `azl_faction_leader` inside the country decision scope at `common/scripted_effects/002_zombie_outbreak_effects.txt:765-793`, called from `common/decisions/002_zombie_outbreak_decisions.txt:2961-2963`. The installed English country localization resolves democratic USA as `USA_democratic: "United States"` and generic USA as `USA: "America"`. The source-correct fixture therefore uses a democratic USA country target and the `GetName` output `United States`.

The getter map assigns the slot images at `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:16,22,28,34`. The title, quote, remark, and description getters select the slot-2/3/5 keys at lines `438,444,450`, `709,715,721`, `980,986,992`, and `1251,1257,1263`, respectively; the corresponding English copy is at `localisation/english/002_zombie_outbreak_l_english.yml:61-74`. For slot 3, `GetWorldEndScenario` selects the zombie terminal label under `world_end_zombies` at `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:294-330`, while `GetWorldEndTooltip` selects `chaos_tier_end` under `world_end` at lines `402-408`; the English tooltip template is `localisation/english/chaosx_chaos_meter_l_english.yml:14`.

The final corrected request used `zombie_azl_usa_democratic_1936`, resolved the slot-2 description text to “Under United States's leadership,” and requested the slot-3 terminal tooltip `§RTerminal world state: Zombie Apocalypse§!`. The single `hoi4_gui_render` call returned no artifacts and the exact error `tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_render; Caused by: timed out awaiting tools/call after 600s`. I stopped GUI retries after that route error.

Slot 3’s tooltip text is source-derived: `GetWorldEndTooltip` returns `chaos_tier_end` while `world_end` is set, and `world_end_zombies` resolves to “Zombie Apocalypse.” The corrected tooltip display and the slot-2 dynamic description therefore remain visually unresolved. The prior slot-3 and slot-5 matrix images show their normal-state image/title/description/quote/button values, but the final accepted render with the source-correct USA fixture and tooltip was not returned.

No source fix was applied. The shared-framework warning and the corrected slot-2/tooltip visual gate remain with the parent.

Skills used: `chaos-redux-scripted-gui`, `chaos-redux-super-events`, `chaos-redux-event-assets`, and `chaos-redux-subagents`. No skill files were created or updated.
