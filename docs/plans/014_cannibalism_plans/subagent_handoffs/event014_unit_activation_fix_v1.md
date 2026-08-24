# Event 014 unit activation repair v1

Date: 2026-08-24

## Result

The nine Event 014 irregular line subunits remain inactive at database load and become valid only after an Event 014-owned hidden bridge technology is granted. Each bridge technology uses `allow = { always = no }`, `enable_subunits`, `popup = no` grants, and no folder, path, or visible tree placement. The existing paid formation transactions, locked templates, and `force_allow_recruiting = no` safeguards remain in place, so activating a subunit does not create a free division or free recruitment route.

Ordinary countries cannot research or receive these bridge technologies because the only gameplay callers are Event 014 package, focus, inherited/unified, and Wendigo transition effects. CXT remains the explicit test exception: the existing Event 014 registration still registers all nine tokens and the shared CXT helper calls `unlock_subunit` when it creates its test templates.

## Exact unlock matrix

| Inactive subunit | Hidden technology | Existing Event 014 gate that grants it | Formation contract retained |
| --- | --- | --- | --- |
| `cannibal_scavenger_warband` | `cannibalism_scavenger_warband_tech` | `cannibalism_setup_current_warlord_country` package; `cannibalism_open_inherited_warlord_recruitment` for inherited and unified hosts | Starting Scavenger Warband and the existing basic recruitment transaction remain package/flag/cost controlled. |
| `cannibal_feast_guard` | `cannibalism_feast_guard_tech` | `cannibalism_setup_current_warlord_country` package only | Feast Guard remains a starting package formation; no new paid decision was invented for it. |
| `cannibal_feast_cohort` | `cannibalism_feast_cohort_tech` | `cannibalism_warlord_focus_form_the_feast_cohorts`; `cannibalism_unified_focus_raise_the_cannibal_legions`; Wendigo inherited cannibal transition | Existing Feast Cohort or unified legion transaction still owns the manpower, equipment, cap, and template lock. |
| `cannibal_bone_guard` | `cannibalism_bone_guard_tech` | `cannibalism_warlord_focus_bind_the_guard_to_one_mouth`; `cannibalism_warlord_focus_raise_the_bone_guard`; `cannibalism_unified_focus_bone_guard_command`; Wendigo inherited cannibal transition | Existing Bone Guard transaction remains flag, cap, payment, and locked-template controlled. |
| `cannibal_bone_riders` | `cannibalism_bone_riders_tech` | The same warlord and unified bone-guard gates as Bone Guard, plus Wendigo inherited cannibal transition | Existing Bone Riders transaction remains the only paid rider route; no new elephant or rider unit was added. |
| `cannibal_island_reavers` | `cannibalism_island_reavers_tech` | Warlord package origin, `cannibalism_warlord_focus_train_the_origin_specialists`, unified origin mapping, and Wendigo inherited-origin transition | Existing origin specialist decision and template remain the cost and flag gate. |
| `cannibal_siege_eaters` | `cannibalism_siege_eaters_tech` | Warlord package origin, `cannibalism_warlord_focus_train_the_origin_specialists`, unified origin mapping, and Wendigo inherited-origin transition | Existing origin specialist decision and template remain the cost and flag gate. |
| `cannibal_march_predation_column` | `cannibalism_march_predation_column_tech` | Warlord package origin, `cannibalism_warlord_focus_train_the_origin_specialists`, unified origin mapping, and Wendigo inherited-origin transition | Existing origin specialist decision and template remain the cost and flag gate. |
| `cannibal_network_cadre` | `cannibalism_network_cadre_tech` | `cannibalism_warlord_focus_train_network_cadres`; `cannibalism_warlord_focus_open_the_courier_routes`; inherited warlord transition | Existing network cadre decision remains the flag, cap, payment, and locked-template gate. |

The inherited and unified calls preserve the Event 014 contracts already documented by the package: inherited Scavenger and Network access, unified Feast Cohort legion access, unified origin specialist knowledge, and Bone Guard/Bone Riders access. Wendigo reasserts the complete inherited cannibal set through `cannibalism_unlock_event014_wendigo_cannibal_subunits` without opening Feast Guard as a new paid route.

## Changed files

- `common/technologies/014_cannibalism_irregular_activation_technologies.txt` defines the nine hidden bridge technologies at lines 12-81.
- `common/scripted_effects/014_cannibalism_activation_effects.txt` defines the package, focus, inherited, unified, and Wendigo grant helpers at lines 10-101.
- `common/scripted_effects/014_cannibalism_effects.txt` contains only the activation-call insertions owned by this tranche at lines 5215, 12172, 12183, 15917, 15929, 15947, 17403, 17552, 17557, 17564, 17713, 17747, and 18613; concurrent Event 014 template and reset edits in this file were preserved and are not owned by this handoff.
- `interface/014_cannibalism_activation_technologies.gfx` maps all nine default technology sprites to the existing vanilla `gfx/interface/technologies/infantry_weapons.dds` texture; no new art was created and no visible technology folder or GUI branch was added.
- `localisation/english/014_cannibalism_l_english.yml` adds diagnostic names and descriptions for the nine bridge technologies at lines 2163-2180 and retains UTF-8 BOM encoding.
- `common/scripted_effects/014_cannibalism_cxt_test_effects.txt` was not changed because it already registers all nine Event 014 tokens through the idempotent CXT extension.

## MCP evidence

The baseline `hoi4.tech_inspect` unlock queries for all nine inactive subunits returned no technology unlock rows and no external grants. The baseline Scavenger artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0dceda9664fe192e5c64ba722860f17da4bb5bbcba453a0b9a178e3d50de08f5/ffa2a7f774397b7db8905a8321c98ce7180976735cfbbc7c82d9a9f1369ceea4/technology-unlocks-6a4015dda798.json`, with graph revision `6a4015dda798ac998dbe056d85ca42e2b507ec7e07674577880f00e559dd950a` and graph hash `80dd1cd52681f94ad8492248bb3b7e10b3db0a9b01ad1b3112a67eaec3ebfe50`.

The final cached post-change pass returned `TECH_INSPECTED_PARTIAL`, status `ok`, no blockers, and graph revision `4eec0bfec23c16a8e7500adebd16486548d0ac014ab5dd2e8f3e4989a0857c45` with graph hash `3d085e2a310f886fc28afa8d573ccea24175bc4e2a3d97fe1674242f93baf03b` for every row below. Every artifact report resolved exactly one technology to its selected subunit, reported `issues = []`, and exposed the expected static external-grant helper stack.

| Subunit | Post-change `hoi4.tech_inspect` artifact |
| --- | --- |
| `cannibal_scavenger_warband` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25eac549428160e0b82f5b6a5f5eb7e012e1006567cc5be4ae88cc73cf655df7/db13f6201ca4f78914ab4540e9a5a1d2243b4571f9e2d1f1fe8d2c3e71c936f0/technology-unlocks-4eec0bfec23c.json` |
| `cannibal_feast_guard` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a374edfd71a225696bc02def6f2256d9bfa7078d2416d7a21306b4ad89bf264/9b214e266a5c05d78c90cbe1a393a4e8cc1da178f1906a079bfc73dce6c6a3ed/technology-unlocks-4eec0bfec23c.json` |
| `cannibal_feast_cohort` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d8cd5eac74ba9dc932fb0f13147c451872d057ae8330835f87e9a96a36c98af/59881713cca50ecde07820514c5334072caffe1407aafd73d45ed3b09adf49dc/technology-unlocks-4eec0bfec23c.json` |
| `cannibal_bone_guard` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9022214524b8dc6fea69eebbec57492bb36159649776a55c22b4e24f89a6d7be/5cb9668650c9f7b40ef0e46563cc769c5cbb2e85447b7276c4d696ae76a3b559/technology-unlocks-4eec0bfec23c.json` |
| `cannibal_bone_riders` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/57a5fac4fb715aab897951701a56a0478bb7fd09273f2916f5d6451a9d8c83bb/4ccd95f6de22852db7e119f5031223e3e46a366851e4def478858b47f41b6f23/technology-unlocks-4eec0bfec23c.json` |
| `cannibal_island_reavers` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/87b1ccd8cf1e118222196e9a6059855edb7d415bba9f2787adb90a4e09227e71/1fc79097fcda5b30e79c9bc17e88f1aa24192a4449cf0f915235b6ecc075da9a/technology-unlocks-4eec0bfec23c.json` |
| `cannibal_siege_eaters` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6235be4183f5cec4a8673c2677d37419fa18291ca6c07631e6a5162dbdc3225e/439f6eaf23fdb7783a1d293f6568fc35ffa59559c8827d9d03b9aa95b65e45a5/technology-unlocks-4eec0bfec23c.json` |
| `cannibal_march_predation_column` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc7ff45dcc0a0111bcaa25f78f7d4fba7c44865898364b93534e3b0aa04b54d6/588584d7400031a94ab2983a9c6008d30035c056379e44b0840e06b9cb5cd1b3/technology-unlocks-4eec0bfec23c.json` |
| `cannibal_network_cadre` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb6d08fbb6e58317e04c225ba77def8eac3c6275c3150811aea8781ebe558695/45a59a1a4707749f270be32b012f3a78fa8a6672537aaa696cf86f6e685baaf1/technology-unlocks-4eec0bfec23c.json` |

The representative final `hoi4.tech_render` artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99bf32c90fc8024bfab8a52c3b53622507b73efcad7ed3c5081817fa5dba965b/4ff7606421acc562cc6746c69c11a0e20e9c9277c7c0c9781775725074c091c6/technology-technology-f75821d45709-manifest.json`. It returned `TECH_RENDERED_PARTIAL`, `renderedIconCount = 1`, and `unresolvedIconSprites = []`; `sourceAccurate = false` remains expected because the hidden node intentionally has no visible folder or path. The rendered node label is `Scavenger Warband Activation` and its source path is `mod:common/technologies/014_cannibalism_irregular_activation_technologies.txt`.

The final structural comparison artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11b89a9968e935c504c1f265359a904663918c1e75934f5b15b76593af7524d3/7ad554b7a8e44172051afacfc59621884657a514b21ce1342878987e107d7be2/technology-compare-6a4015dd-4eec0bfe.json`. It reports `added = 9`, `removed = 0`, `renamed = 0`, `moved = 0`, and `regressions = 9`; the regression count corresponds to the nine intentionally unplaced hidden bridge nodes rather than a missing unlock edge. The MCP validation note is partial because large-workspace helper projections were deferred, but the direct unlock reports contain no issues or blockers.

The installed package exposes no separate Technology Tree Viewer. The available read-only `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` routes supplied the technology evidence above, and no GUI tree branch was created because the offline wiki confirms that an unplaced hidden technology does not need a visible folder branch.

## Source and package validation

- A direct 9/9 contract check confirmed every inactive unit remains `active = no`, every bridge technology has exactly one matching `enable_subunits` entry and `allow = { always = no }`, every bridge is granted by at least one Event 014 helper, and every bridge has exactly one registered icon sprite.
- Balanced-brace checks passed for the new technology, helper, and interface files and for the touched `014_cannibalism_effects.txt` file, which currently contains concurrent edits from another Event 014 tranche.
- The existing `common/scripted_effects/014_cannibalism_cxt_test_effects.txt` registration was re-read and confirmed to list all nine tokens; no CXT file or `common/script_enums.txt` change was required.
- No focus, decision, event GUI, map, state, AI-weight, probability, equipment, or art surface was changed, so their MCP routes and the probability auditor were not in scope for this tranche.
- No Hearts of Iron IV process was launched; live recruitment and save-state validation remain parent/user-owned.

## Remaining risks and limitations

The MCP adapter does not execute the runtime `set_technology` and division-recruitment transaction, so a live user-owned check is still required to confirm each locked template becomes recruitable exactly after its matching route grant. The comparison and inspect tools defer large-workspace helper projections, so direct artifact evidence is structural rather than a full dynamic save simulation. The hidden technologies intentionally have no visible tree placement and therefore should not be made researchable or placed in a folder without a future design request.

No gameplay simplification was made. No route, paid transaction, CXT registration, equipment dependency, or Event 014 identity path was replaced with a fallback.
