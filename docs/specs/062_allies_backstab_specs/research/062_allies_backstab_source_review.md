# Event 062 source review

## Review statement

Every file supplied with the planning request was read in full before the Event 62 specification was drafted.

The three CSV catalogs were parsed as complete record sets, not sampled as snippets. The supplied subagent archive was extracted and every TOML definition was read in full.

The mounted environment did not contain the Chaos Redux repository, the offline Paradox wiki snapshot, or the installed Hearts of Iron IV vanilla game directory and documentation. Those required repository and engine references could not be read here. Their absence is carried as an implementation blocker and no repository-specific inspection is claimed.

## Supplied files read

| File | Bytes | Lines | SHA-256 | Status |
| --- | ---: | ---: | --- | --- |
| `chaosx_dynamic_triggers.md` | 3935 | 62 | `7f6733ef08b816c38aba6d5c675f98c054e9167accd5be3bdf536b65bb60291e` | Read in full |
| `chaosx_dynamic_effects.md` | 14618 | 281 | `2ed4e8f3d220d7d09fd32eabe5e2d35226816d417dbbc11a9635758080bccdf7` | Read in full |
| `CHAOS_REDUX_MECHANICS(9).md` | 71678 | 1165 | `f3a4276d534056b5349c17e029df8f0821dd2b7728237af07d377375a3c38291` | Read in full |
| `chaos_redux_clusters_catalog(4).csv` | 2836 | 15 | `ae37b095ccf1e264397284b1c9e2e9184433e75c5bb6957ef50ea14cef1c63f7` | Read in full |
| `chaos_redux_scenarios_catalog(4).csv` | 12239 | 57 | `0704f9c5a77b6c1bb06f5eead93eb9e130986718763ed7cc212225fc84e22ce2` | Read in full |
| `chaos_redux_events_catalog(4).csv` | 52722 | 253 | `a2d1edcd12a2891eb4b9040139447993f0657af93b166fa0ddd4a1b1186a6fbf` | Read in full |
| `chaos-redux-improvement-loop.md` | 27478 | 288 | `dd1cea075f7d76a5a0c1c8a55ce65bc69d677afd3010cf51d42baa39054cfa53` | Read in full |
| `AGENTS(10).md` | 43195 | 418 | `5fd1111fc9acb189987b5d11b371a1d4202f63c91f5d9487f6408515321d7567` | Read in full |
| `chaos-redux-subagents(1).md` | 36164 | 358 | `ff5e08f96238d5cc3a353fd71253252e7f06d638f4261a6715bbb16d7d6ede9d` | Read in full |
| `config(2).toml` | 11385 | 190 | `df72462c8abcafffeb8250bcd5934680928604a4c64181bd401340c57f508adb` | Read in full |
| `chaos-redux-decisions-missions(1).md` | 74499 | 1167 | `8503d548c92d96ffa4419e760045d726201a69fa78a4a55a87087d855b1af5a5` | Read in full |
| `chaos-redux-event-assets.md` | 124623 | 1520 | `7c15faa859cd40540cd1d64a00ff2112d68327aa37ae8dbe762763e5ba405cc8` | Read in full |
| `chaos-redux-3d-model-pipeline.md` | 87136 | 414 | `ced1ca88126e46f860d55abb66d5507c48aa40b9687715855497e8b0cf71a377` | Read in full |
| `chaos-redux-events(1).md` | 72941 | 805 | `91463e91407af1fe88358050729cb247793f004ac96e890e3ff659c455b85714` | Read in full |
| `chaos-redux-comfyui.md` | 2123 | 17 | `128acd133fedc56b14612eed163de11d7261dac887f11eacf4c8b695dae97fa0` | Read in full |
| `chaos-redux-debug-playtest.md` | 30145 | 667 | `ec9d66e433e9d964a2561844aa45281342842b973e059a09fab18f2107283a43` | Read in full |
| `chaos-redux-focus-trees.md` | 98154 | 1504 | `51f741f8abde30c7772be46072fa4530361dcf4fc348da97b69c86206761789b` | Read in full |
| `chaos-redux-frame-animation.md` | 27086 | 496 | `a8dd6bdcec2b849c6f5c85abffb863510a5585418f2e608c713c8ba83154aa48` | Read in full |
| `chaos-redux-super-events.md` | 33028 | 794 | `d7afffcf25b70333fd50aaef1f72378c1c270b8057269597f085c96204e01607` | Read in full |
| `README(20260830-071218).md` | 2351 | 38 | `bb4b9587eddce00479b5792a7897dbe6f41cc48c5a46fe67b2e129dafbaf8978` | Read in full |
| `chaos-redux-event-planning(1).md` | 195156 | 2278 | `09a18e704984a9d08cb20851f6599acc494ff1939016e384fd049c3b3c412464` | Read in full |
| `subagents(4).zip` | 59612 | binary | `799dfd4e95715d0840b90009558e4d719e2f42eba16db4a258644bc990bd796d` | Read in full |

## Subagent definitions read

| Definition | Bytes | Lines | SHA-256 | Status |
| --- | ---: | ---: | --- | --- |
| `chaosx_3d_model_pipeline.toml` | 24375 | 188 | `235cb326978966a6b284c64dd0dfe8acf9d2be668393b8122c5e37b88875cb92` | Read in full |
| `chaosx_ai_probability_auditor.toml` | 6348 | 67 | `20336a1ec04210d7f468e364fa48ca59427a5fa1292e8765af9eb746a73e6856` | Read in full |
| `chaosx_asset_source_researcher.toml` | 3017 | 59 | `4db7e102822821201eb80055d45ad89272de7cdc4c6c695953d45854bd0e8df6` | Read in full |
| `chaosx_country_package_auditor.toml` | 7965 | 88 | `b140694067beb96d77ab31f6bf1eaa595eff02cf6ae83ce33e50e7ef2bedece4` | Read in full |
| `chaosx_decision_mission_auditor.toml` | 8443 | 100 | `b8d579a9aec9fae7f9a6c5a291976660460ee8a3f1b69e8ef77af70535315433` | Read in full |
| `chaosx_documentation_curator.toml` | 10140 | 132 | `8aea5aad0f4c5350013377041e57029d3cd296774a6713977f2e34cccf533885` | Read in full |
| `chaosx_event_completion_auditor.toml` | 4117 | 67 | `59cbca30c23cd810ac31618eb0ece7a1280455b641096dd2c701e680b261aaee` | Read in full |
| `chaosx_event_ui_worker.toml` | 10720 | 85 | `4afc059508881379bc272bbfac519ddbbe0c448c1fa5f46626cd78fd459f736d` | Read in full |
| `chaosx_focus_tree_auditor.toml` | 4499 | 81 | `83149977d6749cfe743d8ec4c2afa769a019dbfbbc8fd62390460b3629f444e3` | Read in full |
| `chaosx_generated_event_art.toml` | 3909 | 73 | `f7c85c45acf334f76b93ed95409b0165affdc801fea6dd1094651533d89ae3ea` | Read in full |
| `chaosx_icon_artist.toml` | 7611 | 105 | `1afbd89167f2dab6bba6271d2da7523c923a5faba495dbeedde43950af70c0f7` | Read in full |
| `chaosx_improvement_loop_planner.toml` | 7069 | 62 | `a90323b1cbbd664fa61e245186fe7dd912498018e07f3e2393e2641555fbd2bf` | Read in full |
| `chaosx_localisation_auditor.toml` | 9109 | 109 | `f754134bb8df4ec8c99a50c3de69eda2c2b6a211a026aae396af600f224bf30e` | Read in full |
| `chaosx_portrait_creator.toml` | 2029 | 21 | `87b001c6fb5afc33267eb77a3187ff654dbf6b03ae5d669cb2d5182bf7ac2174` | Read in full |
| `chaosx_repo_explorer.toml` | 12690 | 235 | `3b7380b83e0dd6bba741b5c5cd5419e3e5bf22c284459d28d60706b246d964a1` | Read in full |
| `chaosx_scripted_system_architect.toml` | 5387 | 75 | `b2e012aaec78bc875ae27275eb03f86d425aa19ece182716d2570117ff56cacf` | Read in full |
| `chaosx_skill_maintainer.toml` | 3819 | 48 | `1c5efb578a007fc1e3e7f0561d7353876d73918be830f754870041f9d2f66ac2` | Read in full |
| `chaosx_spreadsheet_doc_worker.toml` | 4605 | 60 | `896cb63222484317280d31c340edfc282847774f8edab31a68d7fc2b8b0be33b` | Read in full |
| `chaosx_super_event_audio_researcher.toml` | 3339 | 66 | `248c26c573151ac503886da9bc8cf1942d2af41608528fb2e92161a7808f7d9b` | Read in full |
| `chaosx_super_event_text_researcher.toml` | 3921 | 63 | `c918dae02f2b1127f71134065558f313faec82fba49f3e43022bfeaf3bfb66cb` | Read in full |

## Catalog findings used

- The event catalog contains Event 62 as `Allies Backstab`, Minor Repeatable, Chaos level 1, and To Be Reworked.
- The current event catalog detail is a short baseline statement that one faction expels a member and attacks it. The user-provided Event 62 brief is the accepted expanded direction for this pack.
- The current cluster export does not yet include Event 62 in the Wars member list. The supplied cluster update material explicitly requires Event 62 in Wars as a High member.
- The scenario catalog contains no Event 62 manual scenario. This specification does not invent one.
- The catalogs are export snapshots. Implementation must update the authoritative workbook and run the repository exporter.

## Project rules applied

- Minor Repeatable weight and cap behavior remains owned by the shared event system.
- Evolution eligibility and activation add zero Chaos.
- Cluster firing counts once for pacing while member events keep their own event history and repeatable state.
- Event-owned validation, selection, transaction, lifecycle, and UI rules stay in Event 62 owner files.
- No recurring whole-world daily, weekly, or monthly scan is planned.
- The decision category uses one public value, phase-based visibility, no more than six primary actions, and one to three missions.
- No action has more than four spendable cost types.
- The design uses a static category picture instead of a full scripted GUI.
- No focus tree, new country, custom unit, 3D model, portrait, flag, or frame animation is authorized by this event spec.

## Missing required references

| Missing source | Why it matters | Required later action |
| --- | --- | --- |
| Chaos Redux repository | Existing helpers, exact event log architecture, local names, live file paths, current Event 62 remnants, and uncommitted work could not be inspected | Read the repository before implementation and reconcile every provisional path |
| Offline Paradox wiki snapshot | Required syntax and scope references could not be checked | Read the mandated event, decision, trigger, effect, scope, data, AI, localisation, on-action, modifier, and idea pages |
| Installed vanilla game and documentation | Exact effects, war and faction precedents, decision UI consumers, and asset sizes could not be verified | Inspect current vanilla documentation and at least one matching implementation precedent per surface |
| HOI4 MCP event and probability routes | No event graph, probability baseline, or comparison evidence could be produced | Run event inspect, render, compare, and the full probability audit during implementation |
| Live project subagent invocation | The current tool set exposed no working spawn route. A registry probe returned HTTP 429 | Run the context-complete handoffs in this pack when the project runtime is available |

## Claims deliberately not made

- This pack does not claim that exact Clausewitz effects named conceptually in the design exist under those names.
- This pack does not claim that the repository has no existing Event 62 code.
- This pack does not claim that the cluster workbook or runtime has already been updated.
- This pack does not claim that a project subagent reviewed the design.
- This pack does not claim implementation, asset production, localisation, balance validation, or in-game testing.

## Simplification statement

The design was not shortened for a quicker output. The missing repository, wiki, vanilla, MCP, and subagent evidence is recorded as unavailable verification work. No weaker substitute was presented as equivalent evidence.
