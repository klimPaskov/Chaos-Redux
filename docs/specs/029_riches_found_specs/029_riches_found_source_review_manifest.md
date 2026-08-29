# Event 029 source review manifest

## Review result

Every file supplied with the task was opened and read in full.

The three CSV catalogs were parsed row by row.

The subagent archive was extracted and every TOML definition inside it was read in full.

No supplied source was sampled, shortened, or skipped to finish faster.

## Supplied source inventory

| File | Role | Bytes | SHA-256 | Review status |
| --- | --- | ---: | --- | --- |
| `chaos-redux-comfyui(2).md` | Chaos Redux portrait workflow skill | 2,123 | `128acd133fedc56b14612eed163de11d7261dac887f11eacf4c8b695dae97fa0` | Read in full |
| `CHAOS_REDUX_MECHANICS(7).md` | Top-level implemented mechanics guide | 57,858 | `615d1293862582fc458acf6440e2d2f7dd738793fc0f11aac6c5c471528cdfc4` | Read in full |
| `chaos-redux-events(8).md` | Event implementation skill | 67,981 | `fbbc00b27aeefa915ec6f5a032a08fbbc076146855f68922609cfe7652e57c0f` | Read in full |
| `AGENTS(7).md` | Repository rules | 38,674 | `6a98c2676c0130bc78e843eb7cf485fd86f04696c03a9225034f2008f3915704` | Read in full |
| `chaos-redux-event-assets(7).md` | Event asset production skill | 111,377 | `5c73bdf087be2ca087aab8e856c14c4d60f473c57c8ec3878e155eabf42a2fdd` | Read in full |
| `chaos-redux-debug-playtest(2).md` | Explicit live QA skill | 30,145 | `ec9d66e433e9d964a2561844aa45281342842b973e059a09fab18f2107283a43` | Read in full |
| `chaos-redux-3d-model-pipeline(3).md` | 3D model pipeline skill | 43,678 | `5ac9915cf30fbde15687eb9c30ca8b8be0d24a5801b72019efceb5766b5f6296` | Read in full |
| `chaos-redux-event-planning(20260813-152954).md` | Full event planning skill | 174,584 | `1f8108878ed76d5dc4fd649e69208f0912924acf9351f5dde2cefa7f3c494886` | Read in full |
| `chaos-redux-super-events(7).md` | Super-event skill | 33,028 | `d7afffcf25b70333fd50aaef1f72378c1c270b8057269597f085c96204e01607` | Read in full |
| `chaos-redux-improvement-loop(8).md` | Improvement-loop skill | 27,425 | `fdd2f3526a0fb4d051dd135a403de99dc402f5df82788c01eedabe44156f96f9` | Read in full |
| `chaos-redux-frame-animation(8).md` | Frame animation skill | 25,386 | `71b9b82c067fb6162d52eff233d8e60f49ece8c6fdec043c5e1de8127b7b769d` | Read in full |
| `chaos-redux-subagents(8).md` | Subagent routing skill | 32,913 | `7062f5a36f9dd7f7844b38374a3339308799441380c6d48d3250c8e989204bb7` | Read in full |
| `chaos-redux-focus-trees(3).md` | Focus tree skill | 98,154 | `51f741f8abde30c7772be46072fa4530361dcf4fc348da97b69c86206761789b` | Read in full |
| `chaosx_dynamic_triggers.md` | Reusable trigger registry | 4,690 | `08142b36d735c9994daca01a1fce8296998c530fab8d3e2fd4ffdf4a45a26a37` | Read in full |
| `config.toml` | Agent and MCP configuration | 10,887 | `8579f09a550ad451e56e6bee51fa39eb559f67849a9c6249c66ef37f8c67c139` | Read in full |
| `chaosx_dynamic_effects.md` | Reusable effect registry | 31,440 | `c44d28801253892b9d141097ba31c0705a3f5b07da46ac163be66998b58f11b7` | Read in full |
| `chaos_redux_scenarios_catalog(3).csv` | Scenario catalog export | 10,807 | `66ea4a5802862c1c72f0f3e8ead04cb4f1bfde5e62f88411e3b29f64cb5cf760` | Read in full |
| `chaos_redux_events_catalog(3).csv` | Event catalog export | 55,685 | `c5c29bc03092fe12d0a44381d59c5865f085c0bc3759240b6d2f151cd21fc6db` | Read in full |
| `chaos_redux_clusters_catalog(3).csv` | Cluster catalog export | 2,586 | `0bdd2e73f4c556af5fbdb028a2bbae258ef4d3402450d4bb112a63644047d299` | Read in full |
| `subagents.zip` | Archive containing project subagent definitions | 56,708 | `6e6f029b37107cc9ab5a27e8b2e874980cc3ab3e515ea1022de0a930b4bcd05f` | Read in full |
| `chaos-redux-decisions-missions(3).md` | Decision and mission skill | 72,964 | `8bf185927863c2da3781aabc31f4df6a373d30a8c497bc21121cd4c3c3cbdbc4` | Read in full |

## Catalog coverage

- `chaos_redux_events_catalog(3).csv` contains 182 data rows plus one header row.
- `chaos_redux_clusters_catalog(3).csv` contains 13 data rows plus one header row.
- `chaos_redux_scenarios_catalog(3).csv` contains 11 data rows plus one header row.

The event export lists Event 029 as Minor Repeatable, unclustered, without evolutions or a world-end field, and with status `Unavailable`.

The user-provided catalog entry lists the status as `To Be Reworked`.

The package preserves that discrepancy and requires the implementation agent to inspect the authoritative XLSX workbook before changing status.

The event export also confirms that Event 018 Resources Found is already implemented, belongs to positive Economy cluster 7, and owns its separate deeper-deposit and underground-breach content.

## Subagent archive coverage

`subagents.zip` contains 20 files totaling 130,999 uncompressed bytes.

| Definition | Bytes | Review status |
| --- | ---: | --- |
| `chaosx_country_package_auditor.toml` | 7,965 | Read in full |
| `chaosx_decision_mission_auditor.toml` | 5,713 | Read in full |
| `chaosx_event_ui_worker.toml` | 8,145 | Read in full |
| `chaosx_focus_tree_auditor.toml` | 4,499 | Read in full |
| `chaosx_improvement_loop_planner.toml` | 7,069 | Read in full |
| `chaosx_localisation_auditor.toml` | 8,894 | Read in full |
| `chaosx_repo_explorer.toml` | 12,690 | Read in full |
| `chaosx_scripted_system_architect.toml` | 5,387 | Read in full |
| `chaosx_3d_model_pipeline.toml` | 19,388 | Read in full |
| `chaosx_event_completion_auditor.toml` | 4,118 | Read in full |
| `chaosx_asset_source_researcher.toml` | 3,017 | Read in full |
| `chaosx_generated_event_art.toml` | 3,307 | Read in full |
| `chaosx_portrait_creator.toml` | 2,029 | Read in full |
| `chaosx_icon_artist.toml` | 6,610 | Read in full |
| `chaosx_documentation_curator.toml` | 10,140 | Read in full |
| `chaosx_skill_maintainer.toml` | 3,819 | Read in full |
| `chaosx_spreadsheet_doc_worker.toml` | 4,607 | Read in full |
| `chaosx_super_event_audio_researcher.toml` | 3,333 | Read in full |
| `chaosx_super_event_text_researcher.toml` | 3,921 | Read in full |
| `chaosx_ai_probability_auditor.toml` | 6,348 | Read in full |

The available definitions were used as role-specific review lenses for event planning, decision design, probability auditing, scripted systems, assets, localisation, documentation, catalog work, and completion auditing.

The current environment did not expose a subagent spawning interface, so none of these agents was literally spawned.

That limitation is carried into the implementation prompts and is not presented as completed subagent work.

## Project rules that directly changed the specification

### Event classification and logging

- Event 029 remains Minor Repeatable and unclustered.
- The normal mine lifecycle is baseline progression, not a sequence of evolution log entries.
- An actual evolution must use dynamic pacing, shared evolution context, current-controller actor mapping, and the common log pipeline.
- An impossible target pool must display `N/A` instead of a misleading zero weight.

### Evolution count

The event-planning source permits one evolution stage per chaos tier and at most five stages.

The user fixed Evolution I at 600+. The remaining higher tiers are 800+ and 1,000+.

The package therefore registers three evolutions and preserves the two empty placeholders as late outcomes inside existing tracks.

This is why The Gilded Sovereignty and The Bottomless Account are not separate evolution rows.

### Decision presentation

- The least complex adequate presentation is required.
- One ordinary category and one static category picture are adequate for Event 029.
- A dedicated scripted GUI was rejected because the player can manage the system through phased decisions, missions, dynamic values, and tooltips.
- The visible action budget is three to five main decisions per phase and one to three active missions.
- Extraction Pressure is primary. Mine Development, Local Order, and Revenue Legitimacy are supporting values.

### Costs and balance

- Important actions use concrete costs and requirements instead of default political-power purchases.
- No action may expose more than four spendable cost types.
- Dynamic values, thresholds, durations, chances, and AI weights require central tuning.
- Repeatability requires explicit protection against farming, stacking, controller cycling, occupation abuse, and duplicate contracts.

### Asset authorization

- Only assets required by accepted event surfaces are planned.
- Report art, a static category picture, gameplay icons, state-modifier icons, idea icons, evolution icons, and achievement triplets are authorized.
- Portraits, flags, focus icons, animations, audio, custom units, and 3D models were rejected as unsupported by the accepted event surfaces.

### Anti-bloat review

- Event 029 receives no focus tree because any ordinary country can own it and the mine system already provides lasting play.
- Event 029 receives no country tag because local corporate or supernatural capture can be represented through state and controller systems.
- Event 029 receives no super-event because its repeated crises do not create one universal global threshold or terminal state.
- Event 029 receives no manual scenario because the design does not need a separate sandbox setup.
- Event 029 receives no cluster because the supplied catalog and concept do not support one.

## External research reviewed

The package also used external research for facts that were not established by the project sources.

| Source | Design use |
| --- | --- |
| International Monetary Fund, Dutch Disease: Wealth Managed Unwisely | Resource dependence, sector crowding, and the need for diversification |
| World Bank, Natural resource booms are a mixed blessing for local communities, too | Employment, migration, prices, service pressure, public capacity, and patronage |
| World Bank, Mining Community Development Agreements Source Book | Community agreements, local benefits, obligations, participation, and development projects |
| World Bank, Raising and Sharing Revenues from Natural Resources | Revenue allocation, institutional checks, local sharing, and corruption risks |
| Library of Congress, The Diary of a Forty-Niner | Claim jumping, improvised courts, water rights, road agents, and violent disputes |
| Library of Congress, The Shirley Letters from California Mines in 1851-52 | Shafts, drainage, flooding, collapse, speculation, gambling, and costly failed development |
| Extractive Industries Transparency Initiative, Contracts and Licenses | Contract disclosure, compliance monitoring, revenue collection, and local obligations |
| Extractive Industries Transparency Initiative and Open Ownership, beneficial ownership material | Hidden owners, conflicts of interest, bribery risk, and licensing checks |
| Voluntary Principles on Security and Human Rights | Public and private security risks, community relations, and rules of engagement |
| University of Exeter Institute of Cornish Studies, Knockers and Tommyknockers research | Warning knocks, hidden labor, guidance, punishment, and the need to preserve cultural context |
| National Coal Mining Museum for England, Tommyknockers | Tool hiding, extinguished lights, seam guidance, and underground-warning motifs |
| UNESCO material on Potosi and Cerro Rico | Boundary against turning a living or historic mining tradition into a generic evil cult |

Research-derived content is identified in `029_riches_found_research_notes.md`.

Gold Disease, The Gilded Sovereignty, Demons Beneath the Mine, and The Bottomless Account are fictional design constructions.

They are not presented as historical, medical, religious, or ethnographic facts.

## Environment limitations

The following required implementation sources and tools were not available in this environment:

- the active Chaos Redux repository
- the offline Paradox wiki snapshot under the repository
- installed vanilla Hearts of Iron IV documentation and game files
- approved local reference mods
- the authoritative event catalog XLSX workbook
- the HOI4 MCP event, probability, GUI, technology, and map tools
- the custom Codex subagent spawning interface
- live game control and validation

The specification does not claim any repository inspection, vanilla precedent check, MCP result, asset production, code implementation, catalog edit, or live test.

Every missing implementation gate is carried into the coding prompt, specialist prompts, probability scenarios, and acceptance criteria.

## Completeness statement

The planning package is complete for the event design described here.

No design section was simplified or truncated for speed.

The package deliberately excludes surfaces that the source rules and anti-bloat review found unjustified.

Those exclusions are recorded design decisions, not hidden omissions or fallbacks.
