# Bugs found in the 2026-10-03 live playtest

Each entry gives where it was seen, the evidence, the cause when known, and its status.
Statuses: `fixed` (fixed and verified in game), `fixed, pending retest`, `routed` (sent to the agent that owns the files, with the evidence), `open`.

## Startup and loading

### B001 Thousands of startup errors from in-progress event work — routed

- Seen: the first launch of the working tree reached the main menu with 547 error lines.
- Sources:
  - `027_doctrine_research_exact_mastery_effects.txt`: `index` inside `add_mastery` is rejected by the installed engine; 214 errors.
  - `006_independence_wave_*` effects: unknown scripted triggers, and `clear_global_flag` used instead of `clr_global_flag`.
  - `026_black_friday_effects.txt`: an undefined effect.
  - `camp_administration_ui_l_english.yml` line 181: raw line breaks inside a quoted value.
  - Duplicate entries in vanilla special-project lists.
- Status: each source was routed to the Codex thread that owns it. The second launch had 21 lines, and the clean-snapshot launch had 9.

### B002 Sicily (ASX) flags are 24-bit — fixed

- Seen: `error.log` warns "slow to read format - Consider using 32bpp" for all fifteen ASX flag files.
- Fix: converted to 32-bit uncompressed TGA with an opaque alpha channel. Same pixels, same bottom-left origin as the other flags.

### B003 Komi (KOM) democratic flag fails to load — fixed

- Seen: "Unsupported format. Expected 32bpp, uncompressed, no color palette" for `gfx/flags/KOM_democratic.tga` in all three sizes, followed by "File not found".
- Cause: the files stored a top-left origin with an attribute descriptor (byte 17 = 40). The engine accepts only the bottom-left layout the other flags use.
- Fix: rewritten bottom-up with descriptor 8. Verified visually; pending a retest in game.

### B004 Two tokens not registered as synchronized dynamic tokens — fixed, pending retest

- Seen: "Token chaosx_cxt_extension_zombie_cure_payload / zombie_cure_bomb_1 is a dynamic token, this can cause OOS".
- Fix: added both to `common/synchronized_dynamic_tokens/` (`chaosx_tokens.txt`, `chaosx_equipment_tokens.txt`).

### B005 Black Friday scripted localisation builds an invalid token — routed

- Seen: three lines of 'Creation of dynamic token "0]" failed' at startup.
- Cause: `026_black_friday_scripted_localisation.txt` uses `localization_key = "[?var|0]"`, which the parser splits as a key token.
- Routed to the Event 026 thread with the fix: real localisation keys holding the expressions.

### B006 Runtime recruit_character warnings for dated CBRN scientists — routed

- Seen: 58 lines of "recruit_character should only happen in game/history files" from `chaosx_startup_history_effects.txt`.
- Evidence: in a November 1936 save the runtime recruitment still attaches the scientists (SOV_yakov_fishman has country SOV), so it is a warning, not a failure.
- A swap to character-scope `set_nationality` was tried and reverted: an unrecruited character belongs to no country, so it cannot be scoped.
- Routed to the CBRN thread with the holder-tag route that removes the warning.

## User interface

### B007 Triggerable Scenarios rows #016 and #018 show "SCN-0NN" on two lines — fixed

- Seen: Global Jihad and The Fracture Cascade showed "SCN-01" wrapped over "6" and "8", while every other row reads "#0NN".
- Fix: `chaosx.scenarios.entry.id.global_jihad` → "#016" and `chaosx.scenarios.entry.id.random_civil_war` → "#018". The owning threads were told to keep it.

### B008 Assassin Network scenario is missing from the list and collides with Fallout's number — routed

- Seen: the scenario catalogue lists SCN-014 Assassin Network as "Needs Testing", and its localisation exists. No triggerable-scenario id registers it, and its entry label "#014" is Fallout's id.
- Routed to the Event 039 thread: register it with a free id and correct the catalogue row.

### B009 Event Logs History opens without its empty-state text — fixed, pending retest

- Seen: the first time Event Logs opens on History in a fresh game, the list is blank. "No events have been fired yet." appears only after switching to another tab and back.

### B010 Air Cleanliness shows "-0.000%" at zero — reopened (retest 2026-10-05 failed)

- Seen: in a fresh game the Air Cleanliness tab shows "Last recovery: -0.000%" and "Recorded falls: -0.000%".

### B011 Tier 4 is named two ways — fixed

- The Chaos Meter window and top bar call tier 4 "Total Chaos". Event-log text and requirement tooltips call it "Totalen Chaos" (`chaosx.events_log.evolution.tier.4`, `chaosx.event_chaos.requires.5`).

## Models

### B012 Rat units: little motion and a rigid tail — routed

- Seen: in live footage (Vienna, low camera) the brute rat holds one raised-claws pose for seconds, and its tail stays a straight rod.
- Routed to the 3D model pipeline worker with frame sheets and the clip.

### B013 Demonic zombies render washed-out white with smeared wings — routed

- Seen: in Paris the model reads as a near-white figure with no detail at map zoom, and its wings streak while moving.
- The diffuse averages a flat grey and the specular map is nearly empty.
- Routed to the 3D model pipeline worker.

## Engine and vanilla (not Chaos Redux)

These are recorded so they are not mistaken for mod bugs:

- `GER_super_heavy_armor_entity` and `ITA_mechanized_vehicle_1_entity` are missing for vanilla equipment graphics. Chaos Redux already supplies aliases in `chaosx_vanilla_entity_aliases.asset`, and the lines come from vanilla's own database order.
- `IRQ_kamil_shabib` and the `Hs 123` icon errors come from vanilla history files.
- `gfx/interface/ideas/great_depression.dds` is referenced by vanilla `interface/ideas.gfx` but is not shipped with the game.

### B014 Disaster Wardens have no model; leftover elephant files — open

- `disaster_wardens` (Event 012) uses `sprite = disaster_wardens`, but no `disaster_wardens_entity` exists.
- Its folder `gfx/models/units/012_africa_disaster_wardens/` holds five `.anim` files and no mesh. The unit model rework plan lists it as pending (row 26, "no shipped mesh; axe-bearing").
- The Africa elephant intentionally uses the vanilla elephantry visual (commit 63e5d3d7a). The six animations and three textures left in `gfx/models/units/chaosx_elephants/` have no consumer.

## Committed-code regressions found on 2026-10-03 (afternoon)

### B015 Event 012 tribute helpers use macro parameters the engine does not support — routed
- Seen: a launch of HEAD d51bba41f reached the menu with 593 error lines; 527 came from four Event 012 files added or changed by commit 46ea61997.
- Cause: scripted effects and triggers are called as `helper = { AMOUNT = ... }` / `{ EQUIPMENT = ... }` with `$AMOUNT$` / `$EQUIPMENT$` in their bodies. HOI4 scripted effects and triggers take no parameters, so the parser loses the rest of each file.
- Status: routed to the Event 012 thread with the temporary-variable and meta-effect route. Live QA pins those files to 487033b34 until the repair lands.

### B016 Event 021 calls an undefined scripted trigger — routed
- `event021_sponsor_repayment_receipt_valid` is used in `021_random_civil_war_parent_effects.txt` line 5439 but is not defined in any committed trigger file.

### B017 Event 012 migration helpers and a dynamic token — routed
- `migration_install_gods_of_africa_reception_service` and `migration_clear_gods_of_africa_reception_service` are called but not defined; `gods_of_africa_demand_mission` is not a synchronized dynamic token.

### B018 CBRN Scientist Holder (CSH) has no flags — routed
- "Error loading flag for country CSH" for democratic and neutrality in all three sizes, at load and on 1 January 1936.

## Models

### B019 Two Event 012 unit models can never appear on the map — routed (documentation)
- `pan_sappers` and `oracle_recon` are support companies. A division only displays a line battalion's entity, so `chaosx_pan_sappers_entity` and `chaosx_oracle_recon_entity` are never rendered in play.
- The model showcase displays them through QA-only line copies that exist only in the QA snapshot.

## Scenario runs on 2026-10-03 (afternoon)

### B020 Event 013 path window: overflowing text and wrong data — routed (UI worker)
- Seen: #007 Disaster Barrage at Maximum, first report option "Open the path map".
- The header subtitle wraps below its band; the detail panel text runs under a decorative bar and overlaps the recovery line; the title plate text sits on the frame.
- The next and scheduled impact read 1958.10.31 on 2 January 1936; the panel shows "Sequence 1 / 0" while the header lists 16 segments, "Hazard: unclassified hazard" for a Massive Eruption, and "State: none confirmed" for Washington.
- The legend overlaps a dark bar, a stray letter "S" sits under the map, and the colour strip has no labels.

### B021 Colour codes in event descriptions are unreadable on the parchment window — fixed in part, routed
- Seen: chaosx.nr13.4 shows the threatened state in §Y yellow on beige; it is nearly invisible at 1080p. Vanilla uses no colour codes in any of its 1,537 event descriptions.
- Fixed: the descriptions of chaosx.nr13.4, chaosx.nr15.46/47 and five Event 019 descriptions.
- Routed: the remaining descriptions owned by Events 006, 014, 028 and 033.

### B022 Scenario panel text clipped or written in implementation terms — fixed (e9264c9fe)
- Fallout, Assassin Network, The Unbidden Muster and Black Plague Unbound texts ran past their boxes or behind the Launch button, and several used words such as "verified batch", "tag" and "carrier capacity". Seventy keys were rewritten to fit.

### B023 A zombie horde spawned in an impassable state and capitulated — fixed (5a78436a3)
- Seen: "Rabid Horde has capitulated" right after #001 launched; 22 create_unit failures ("Province is Impassible").
- Cause: the horde received Deep Amazonas (state 968, impassable wasteland). Outbreak state filters now exclude impassable states.

### B024 Hourly "Constant value is not a country tag" error — fixed (26ac17214)
- Cause: Event 079's targeted decisions used a variable inside `targets`. They now use a target array and a root trigger; a 15-hour run logged no new lines.

### B025 Zombie scenario declared war on a country it was already fighting — fixed (26ac17214)

### B026 Assassin Network uses `exists` on a character scope — routed
- 039_murder_mystery_runtime_effects.txt:442, logged at the #019 launch.

### B027 Event 006 decisions declare a modifier without days_remove — routed
- Four decisions, logged at the #013 launch.

### B028 Missile Age uses `exists` on state scopes — routed
- 032_missiles_operations_effects.txt lines 692, 741 and 766; about 400 lines during the #015 launch.

## Snapshot at a6065612d (2026-10-04, after the takeover lint fixes)

### B029 Event 014 siege trigger writes an @constant into a literal-only field — fixed (e08c1815f)
- Seen at startup: "Malformed token: @CANNIBALISM_SIEGE_VICTORY_POINTS" in 014_cannibalism_triggers.txt.
- Cause: `limit_to_victory_point` inside `any_province_building_level` takes only a literal number (vanilla AST.txt uses `limit_to_victory_point > 0`). The thresholds now reach the filter through temporary variables and `meta_trigger`. The next launch logged no load error.

### B030 Biological sabotage reads country triggers in state scope — routed
- 48 runtime lines per session: `has_war_with`, `is_subject_of` and `is_in_faction_with` in `bio_sabotage_state_relationship_is_valid` (biological_sabotage_triggers.txt lines 69–78) run from a state.
- The stopped CBRN thread left an uncommitted country-preflight version of the check in the working tree; the CBRN takeover adopts or replaces it.

### B031 Three unit models render as polished chrome — fixed for two models (51f2eed3f), Feast Cohort open
- Seen while filming the model showcase: Island Reavers and March Predation Column (Event 014) look like mirror chrome; the Feast Cohort looks dark chrome.
- Cause found: their normal maps are plain tangent-space RGB (mean B about 210–220) and their specular maps are flat grey, while the game expects the Paradox packing (normal X in R/A and Y in G; specular R=0, G=strength, B=metal, A=gloss). The alien infantry normal map has the same layout problem.
- Fixed for Island Reavers and March Predation Column in 51f2eed3f (Blender previews show natural skin, cloth and wood; in-game refilm pending).
- Feast Cohort: its three maps belong to an earlier recovery mesh with a different UV layout (the shipped mesh is the 24 August v6 cut), so the texture lands scrambled on the model. A real fix needs the v6 maps re-downloaded from the provider or a retexture; both are provider downloads that wait for the user's go-ahead. Evidence and a staged stopgap: docs/plans/system_unit_model_rework_plans/2026-10-04_texture_repack/handoff.md.

### B032 Every Banner Rises (#008) launches but releases no country — routed (Event 006 takeover)
- Launched from a fresh 1936 save: the hidden launch event took its failure branch a day later (`independence_wave_scenario_failed`, last failure 10 = invalid_scope, released count 0). Nothing changes on the map a month later and the player gets no message.

### B033 Load and runtime errors introduced by the takeover commits — routed
- At fa833647e: a malformed localisation line (031 line 622), `building` used as a literal building type (014 triggers 5163 and effects 18114), `var:PREV.` tokens in 029 triggers (689, 693), `recruit_character` evaluated at load (039 character effects 242), and `is_controlled_by` in country scope in migration decisions (597, 653; about 44 lines per few game hours).

### B034 Chaos Redux hotkeys collide with AMD Radeon Software defaults — open (design decision)
- On an AMD system, Ctrl+Shift+S (Triggerable Scenarios) also toggles Radeon Instant Replay and shows an "Instant Replay: Off/On" toast over the game, and one of the Ctrl+Shift chords opened the Radeon overlay panel, which then captured the mouse until Alt+R. Ctrl+Shift+E (Event Logs) is the Radeon default for starting a recording on many installs.
- Suggestion: offer alternative bindings (for example Shift+F-keys) or document the conflict in the Help window.

### B035 Abnormal Disaster Path: the route panel shows art only for some stages — open (Event 013)
- Disaster Barrage, Full Catalogue, Maximum (trailer_210_barrage_launched): the meteor stage (Maryland) draws its scene in the central route panel, while the drought and wildfire stages (Arkansas, Montana, New York) leave the panel an empty dark field with only the numbered pins.

### B036 Event Logs History is empty while events have fired — open (shared Event Logs)
- trailer_240_crisis (20 June 1936, non-debug): the Events tab shows Fired 1 for The Holy Realm, Soviet Union Collapse, Fury and Death (Death "Fired on 1936.1.1, Log #10"), and Disaster Barrage, Black Plague Unbound and Missile Age were launched, but the History tab draws no rows and no empty-state text.
- The Event Details window also shows an empty dark box beside the event name (top right of the window).

### B037 Civilian Deaths, Contamination and Terror Activity map modes draw no colour in a late Fallout world — open
- qa_fo_apr (12 April 1936 after the Fallout strikes, Chaos Meter full): over Europe at continental zoom, Air Winter (blue tint), Famine (brown halos) and Migration (red) recolour the map, while Civilian Deaths, Contamination and Terror Activity leave it unchanged. In trailer_240_crisis (16.1M deaths, 11.1M of them in the United States) Civilian Deaths also shows no colour over North America.

### B010 retest (2026-10-05)
- Still present at fa833647e: the Smoke, Ash, and Aerosols source details read "Directly cleared: -0.000%" with nothing cleared (trailer_240_crisis, non-debug).

### B038 Cluster Details: the activation line is drawn under a dark bar — open (shared Event Logs GUI)
- Event Logs > Clusters > Natural Disasters: in the Cluster Details window the line "Activation: Varies by member  Members: 7  Eligible: 4" sits on a dark rounded bar, its first letter is cut off, and "Members" overlaps the bar's end.

### B039 Riches Found resource field record: overlapping labels — open (Event 029 GUI)
- qa_fo_apr, Events and Decisions > Selected Resource Field: in the Resource Field Record box "Rebuild Outlook" is drawn over another label and a status line under the image overlaps "Operating"; the field reads "Wake Island, Active field 0/0" with every value 0.

### B040 The Hunger Lines (#010) never starts a famine — fixed in source, live recheck pending
- Launched from a fresh 1936 save and run to 25 April 1936: 57 states carry the famine variables but all stay at their zero initial values (no reserve initialisation, no score, no stage), the Famine map mode shows no colour and no famine decisions appear. Save: qa_scn010c.
- Cause: all three QA launches failed inside Event 014's setup (`cannibalism_manual_scenario_setup_failed`, no node states) because of the helper temp-output defect fixed in `abacbd845`, so the famine hook never ran. `839850b0d` makes a successful launch seize the node states' stores and commit acute shortage (Low) or famine (Medium and above) on launch day. Recheck: launch #010 Broken Ranks at Low and Maximum from a fresh 1936 save.

### B041 Network Cadre listed as "NCD" in the division designer — routed (Event 014)
- Division Designer > Infantry Battalions shows the Network Cadre battalion by its abbreviation "NCD" instead of its name, although the name key exists.

### B042 New load errors on the 5 October snapshot (`539b55887`) — partly fixed, rest routed
- Event 016: three localisation values in `016_brilliant_scientist_projects_l_english.yml` broke across lines ("Expected colon"), so the keys after them did not load. Fixed in `874fdc0bd` and `ce195cbe3`.
- Fallout: `fallout_orientation_cell_lock_condition_is_met` used `num_owned_states` as a trigger ("Unknown trigger-type"). Fixed in `874fdc0bd` (read through `check_variable` against a named threshold).
- Event 006: 62 load warnings "recruit_character should only happen in game/history files" from the per-tag blocks in `006_independence_wave_execution_effects.txt` (lines 464–606). Routed to 006.
- Event 027: about 120 "dynamic token ... add it as a synchronized dynamic token" warnings for every `modifier@<doctrine>_mastery_gain_factor` read. Routed to 027.
- Event 012: the same warning for `num_equipment@fighter_equipment_1`. Routed to 012.
- Event 032: one runtime "exists: Invalid Scope, provided: State" at `032_missiles_operations_effects.txt:6388` after a missile programme started. Routed to 032.

### B043 Forcing an event restarts the random event timer
- Not a defect, recorded for testers: firing any event through Settings sets a new random timer window, so a parked timer (`event_timer_days`) does not hold after a forced event. During a three-month run after forcing Event 001, Missiles (032) fired from the restarted timer. The batch harness re-parks the timer before each run of days.
