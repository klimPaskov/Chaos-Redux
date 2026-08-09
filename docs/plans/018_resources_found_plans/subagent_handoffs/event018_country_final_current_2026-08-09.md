# Event 018 Oth-Kesh Country-Package Final Audit

Date: 2026-08-10 (handoff filename required by the parent task)

Scope: the persistent Event 018 Oth-Kesh Host country package (`DHO`) and its country-owned runtime support. This audit does not edit Event 018 localisation, decisions, focus source, GUI, spreadsheet, shared event framework, or the concurrent Event 019 provider append.

Verdict: **PASS for the country-owned static package; no confirmed narrow source repair was required.** The only file changed by this pass is this handoff. No gameplay source was staged or committed.

## References and audit method

I read `AGENTS.md`, the complete Event 018 specification package under `docs/specs/018_resources_found_specs/`, the current cave-country documentation, and the existing Event 018 country, focus, asset, probability, and completion handoffs. The required repository skills were read: `chaos-redux-subagents`, `chaos-redux-events`, `hoi4-focus-trees`, `hoi4-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-comfyui`, and `chaos-redux-improvement-loop`.

I consulted the required offline wiki pages in `paradox_wiki/`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus modding, Unit modding, Division modding, and Technology modding. I also read the relevant vanilla documentation in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\`, including effects, triggers, script concepts, and script constants, and checked vanilla country, character, locked-template, OOB, unit, AI-strategy, and portrait precedents. No online Paradox wiki page was used.

The required read-only HOI4 MCP routes were used before reporting supported surfaces:

- Focus inspect and render: current `018_resources_found_cave_focus_tree` resolves to 67 unique focuses, 81 connectors, zero crossings/intersections, and zero Event 018 tree-local diagnostics. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba8fb0c5177e9e3a93b5585a5a3a7c8cbbdc70e390b807353b2b599fa958fb85/2fb0fcac6031271c167e323ea02a65e9761d6c53dab7b544e934502e20e52325/focus-inspect.d3a6c88608703ab1.json`; render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1bbe413dc31ffc8000592b4d838f820e76b0f98253601d7bc68473317ef6a7a7/31b1c62b2d89e5fde4831dc4a98f64922afdf407acb41483f560f487d8e29260/018_resources_found_cave_focus_tree.focus.svg`.
- Event namespace inspect and overview render: `chaosx.nr18` returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, with no blocking diagnostics. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b692487034e96ee93d0cb463a8666b4ddef646e79bdd3a0902a38258340a157/cd641342aa88f980610d4c0c67e5b3b9019c630fe61c0bff7b3f64eefaa83fb9/event-scan-7e8e9a563058.json`; overview artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c702e33f7fae5599f7db04616245974d210210624bcf9d4880d112e49d44f4c/5e8b16d3d4adcabc802b10a21e91773ff7e95623dd5aaf53fa3888bf6f8d4b47/event-overview-7e8e9a563058.svg`.
- Map inspect and render: the dormant country has no fixed state because the first origin is selected by Event 018 at runtime. A bounded map inspection of state 1 nevertheless passed the map graph/state-membership/network checks and the state-layer render completed. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca6825b983adb43c3ba5f0ec9b2a61dd5ecd8c755c1041f3158368aa930b49b4/2dc6bb3392e870df1b8a81f147b218522aad11cc13e03ebff9e82dbed4574fe0/map-inspect.d4bae4183ffda7fd.json`; render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b07c0a868ffe20da57df4937484a67a1cef1b5f95dc880aa6b131d12dffdd288/85da32ed98fe673b11a3ea9cec2a3395b90c48cb25921682b3518e4097a500e2/map-state.png`.
- Technology inspect and render: no custom DHO technology tree is declared. The available technology route returned only a partial global scan, not a DHO-specific tree. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0be687549b9db34c79c3c59f89b94004a72d1b09e6e092d54957d70fe1d8d87/f73e4d400b3589638f127024e0e7e6939165e465af8e2823b8da05dfad5402cd/technology-scan-8fef8ad49cbf.json`; render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e852a29a2a166bcc019b85fb7adf90554e18616fd12c0553c15efc73037bd42/f7d749233e4d55fc420f3b43ce7b9ab376c461b6540a996daf06cdbe09fbdeb7/technology-summary-8fef8ad49b.png`.
- Weighted AI/probability evidence is inherited from `event018_probability_final_current_2026-08-09.md`. That required auditor pass is conditional because the installed adapter cannot prove complete campaign pools or typed ownership/control/neighbor/enemy predicates. No weighted source was changed in this pass, so no probability compare delta was claimed.

## Country-package coverage checklist

| Surface | Result | Evidence and exact identifiers |
|---|---|---|
| Tag registration | Pass | `common/country_tags/018_resources_found_cave_country.txt:2` contains the single `DHO = "countries/The Oth-Kesh Host.txt"` registration. A direct scan found one mod registration, zero vanilla registrations, and zero registrations in the available approved reference mods. |
| Country definition | Pass | `common/countries/The Oth-Kesh Host.txt:8-10` supplies graphical culture and the stable Oth-Kesh color `rgb { 44 58 52 }`. |
| Dormant history | Pass | `history/countries/DHO - Oth-Kesh Host.txt:14-40` provides only a valid dormant capital, zero research slots, politics, stability, war support, leader recruitment, and five starting ideas. It deliberately does not preload an OOB. |
| Runtime creation | Pass statically | `common/scripted_effects/018_resources_found_cave_effects.txt:34-80` initializes DHO once, loads `DHO_1936` once, loads the focus tree, disables ordinary rules, and saves the cave-country target. |
| Origin state and capital | Pass statically | `common/scripted_effects/018_resources_found_effects.txt:1132-1184` records the random origin, discoverer, former owner/controller, continent, sequence, six resource ledgers, and emergence date. `common/scripted_effects/018_resources_found_cave_effects.txt:303-342` transfers, cores, controls, supplies, capitals, and spawns the origin package. |
| Origin exclusion | Pass statically | `common/scripted_effects/018_resources_found_effects.txt:1187-1213` computes `floor(total six strategic resources / 10)` with a per-state cap of 10 and forces origin future capacity to zero. |
| Opening strength | Pass statically | `common/scripted_effects/018_resources_found_effects.txt:1262-1357` clamps the retained score and converts each complete five score points into one division with a six-division minimum and 30-division maximum. |
| Captured capacity | Pass statically | `common/scripted_effects/018_resources_found_cave_effects.txt:1062-1081` and the daily anchor helpers maintain active anchor capacity, activation timing, grace, paced replacement, and over-capacity status. |
| Neighbor wars | Pass statically | `common/scripted_effects/018_resources_found_cave_effects.txt:426-470` resolves both legal owner and physical controller, checks cave-country identity and existing wars, and declares annexation wars only when supported. The recurring tag-specific pulse is `on_daily_DHO` at `common/on_actions/018_resources_found_on_actions.txt:49-55`. |
| Defeat and cleanup | Pass statically | `common/scripted_effects/018_resources_found_cave_effects.txt:2374-2550` handles zero-controlled-state defeat, global threat cleanup, state cleanup markers, arrays, targets, ideas, cosmetic identity, cores, modifiers, and reconstruction handoff. |
| World end | Pass statically | `common/scripted_effects/018_resources_found_cave_effects.txt:2224-2254` requires delayed exact verification, sets the shared terminal state, applies `DHO_WORLD_BELOW`, creates footholds, refreshes capacity, and refreshes neighbor wars. |

## File surface checklist

The following country-owned files were inspected and are internally consistent:

- `common/country_tags/018_resources_found_cave_country.txt`
- `common/countries/The Oth-Kesh Host.txt`
- `history/countries/DHO - Oth-Kesh Host.txt`
- `history/units/DHO_1936.txt`
- `common/characters/018_resources_found_cave_characters.txt`
- `common/country_leader/018_resources_found_cave_traits.txt`
- `common/unit_leader/018_resources_found_cave_traits.txt`
- `common/units/018_resources_found_cave_broods.txt`
- `common/ideas/018_resources_found_cave_ideas.txt`
- `common/ai_strategy/018_resources_found_ai_strategy.txt`
- `common/dynamic_modifiers/018_resources_found_state_modifiers.txt`
- `common/scripted_effects/018_resources_found_cave_effects.txt` (read-only audit; concurrent Event 019 provider append preserved)
- `common/scripted_effects/018_resources_found_effects.txt` (shared Event 018 origin/strength/capacity helpers)
- `common/scripted_triggers/018_resources_found_cave_triggers.txt`
- `common/on_actions/018_resources_found_on_actions.txt` (read-only audit; concurrent Event 019 startup hook preserved)
- `interface/018_resources_found.gfx`, `interface/chaosx_characters.gfx`, and `interface/chaosx_subuniticons.gfx`
- `gfx/flags/`, `gfx/leaders/018_resources_found/`, `gfx/interface/ideas/018_resources_found/`, `gfx/interface/counters/`, and `gfx/entities/018_resources_found_cave_monster.*`
- `localisation/english/018_resources_found_system_l_english.yml` and the country-facing Event 018 localisation consumers (read-only verification only)
- `docs/events/018_resources_found/cave_country.md` and `docs/events/018_resources_found/assets.md`

## Identity, politics, leaders, portraits, flags, and advisors

- `DHO` is a single stable tag with the original nonhuman name `The Oth-Kesh Host`, adjective `Oth-Kesh`, custom neutral sub-ideology `resonant_brood_hierarchy`, and the institutional party `The Resonant Maw` (`localisation/english/018_resources_found_system_l_english.yml:2-42`, `common/ideologies/00_ideologies.txt:203-235`).
- `history/countries/DHO - Oth-Kesh Host.txt:21-33` recruits the authored sovereign `DHO_vhorruk`, fixes neutrality, disables elections, and sets all non-neutral popularity to zero. Runtime setup additionally disables factions, puppeting, volunteers, market access, forced government, and cross-ideology guarantees (`common/scripted_effects/018_resources_found_cave_effects.txt:43-55`).
- `common/characters/018_resources_found_cave_characters.txt:25-88` defines literal nonhuman Vhorruk and the three authored commanders `DHO_thessik`, `DHO_orrukesh`, and `DHO_khalvek`; no human random-name pool, gender-pool assignment, or institutional-body misclassification is used.
- Vhorruk uses the static political portrait `GFX_portrait_DHO_vhorruk`. His eight-frame generated-fictional animation is registered as `GFX_portrait_DHO_vhorruk_animated` for the Event Details consumer only. This deliberate static-country-screen/animated-Event-Details split is documented in `docs/events/018_resources_found/assets.md` and `docs/plans/018_resources_found_plans/subagent_handoffs/generated_event_art_handoff.md`.
- Each commander has a full and small portrait wired to an existing DDS, and each trait is defined in `common/unit_leader/018_resources_found_cave_traits.txt`. No advisors or high-command staff are declared; the package deliberately uses commanders and route ideas rather than normal political-advisor slots.
- Six original flag identities (`DHO`, four ideology variants, and `DHO_WORLD_BELOW`) exist at 82x52, 41x26, and 10x7 in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`. A binary scan found all 18 TGA files to be uncompressed 32-bit images with distinct SHA-256 hashes.

## Army, templates, technology, industry, supply, and production

- `history/units/DHO_1936.txt:13-107` defines exactly five locked templates: Oth-Kesh War-Brood, Oth-Kesh Stone Phalanx, Oth-Kesh Burrow Column, Oth-Kesh Scree Pack, and Oth-Kesh Feeding Guard. All use `is_locked = yes` and `force_allow_recruiting = no`, with vanilla-range priorities 1 or 2.
- `common/units/018_resources_found_cave_broods.txt:108-276` defines five inactive equipment-independent sub-units with `manpower = 0`, no equipment `need` block, long training time, high armor/hardness, low speed, and explicit hard-attack/piercing counterplay. The file documents `maximum_speed` as a multiplier, not an absolute km/h value. The shared `Slow Blood` spirit keeps all base formations slower than ordinary 4 km/h foot units; the strongest route bonuses remain intentionally counterable by hard attack, piercing, supply denial, and recapture.
- The runtime cave helpers create only the five named templates and pass zero-manpower/zero-equipment factors. The static scan found no Event 018 cave path for naval OOBs, aircraft, ships, or ordinary equipment-stockpile transfer. Equipment-bearing stockpile effects in the shared decision file are ordinary-country countermeasure scopes, not DHO brood creation.
- DHO starts with zero research slots (`history/countries/DHO - Oth-Kesh Host.txt:8,17`) and has no custom technology tree. Captured factories are addressed only through the explicit cave conversion focus/decision path; ordinary industrial production is blocked by `cave_untranslatable_command` and the runtime market/production rules.
- The first emergence adds a supply node only when the origin lacks one (`common/scripted_effects/018_resources_found_cave_effects.txt:320-325`), then applies the origin chamber modifier and capital. Later anchors use explicit state modifiers and controlled activation rather than a fixed map empire.
- Counter, on-map, and model consumers resolve: five large counter DDS files and five on-map DDS files are registered in `interface/chaosx_subuniticons.gfx`, and the five cave sub-unit sprites resolve through cloned entities in `gfx/entities/018_resources_found_cave_monster.gfx`.

## Ideas, focus, decisions, and asset coverage

- The five starting ideas are `cave_mineral_carapaces`, `cave_slow_blood`, `cave_resource_born_broods`, `cave_surface_starvation`, and `cave_untranslatable_command` (`history/countries/DHO - Oth-Kesh Host.txt:35-41`, runtime setup at `common/scripted_effects/018_resources_found_cave_effects.txt:64-70`). Their modifiers enforce armor, slowness, zero normal recruitment, anchor dependence, and diplomacy/production isolation.
- The remaining cave route ideas and state/dynamic modifiers have localisation, registered `GFX_idea_*` sprites, and physical DDS files. A direct scan matched all 20 unique `picture` tokens in `common/ideas/018_resources_found_cave_ideas.txt` to registered sprites and existing textures; all 17 dynamic-modifier icons also resolve.
- The current focus source contains 67 unique DHO focus IDs. A direct scan matched every focus name, description, tooltip, normal icon, and shine icon to localisation and registration. The focus MCP route found no Event 018-local diagnostic. Older focus handoffs that report 65 are historical snapshots; `docs/events/018_resources_found/cave_country.md` and the current MCP result use 67. This documentation discrepancy is recorded for the parent/documentation curator and is outside this country-only handoff's patch scope.
- Decisions and missions are owned by the decision worker and were not edited. Country-owned helpers expose commander recruitment, anchor activation, spawn preferences, industry conversion, origin fortification, and doctrine-specific brood behavior to those decisions and focus rewards.
- The generated-fictional portrait, flag, counter, idea/state, focus, report/news, super-event, and cave-monster model runtime files are covered by `docs/events/018_resources_found/assets.md`, `docs/plans/018_resources_found_plans/subagent_handoffs/generated_event_art_handoff.md`, and the existing icon/model handoffs. The temporary `docs/assets/018_resources_found/` production workspace is intentionally absent; no runtime file points into that archive.

## AI and playability

- `common/ai_strategy/018_resources_found_ai_strategy.txt:34-439` provides under-capacity anchor defense, resource-corridor offense, origin recovery, world-end fronts, hierarchy/doctrine targeting, garrison reinforcement, and objective concentration. `@CAVE_FRONT_RATIO = 0` is a supported vanilla-style `front_control` value used alongside explicit `front_unit_request` priorities; it is not treated as a confirmed defect.
- `common/ai_strategy/018_resources_found_ai_strategy.txt:441-520` gives ordinary countries defeat/containment weights, anti-tank and CAS production/role priorities, and explicit alliance/military-access rejection toward DHO.
- The required probability audit is conditional rather than a numeric balance sign-off because the installed adapter cannot prove complete campaign pools or typed runtime predicates. No AI or probability-bearing source was changed here, so no new baseline/compare pair is claimed. The parent should continue to carry the conditional findings from `event018_probability_final_current_2026-08-09.md`.
- Static playability is coherent: DHO begins only at the emergent origin, grows only through captured resource capacity, wars every adjacent land actor, has a slow armored roster with hard-attack counters, and can lose capacity into `cave_unfed_broods` instead of receiving free human recruitment. Actual AI front allocation and campaign pacing remain unobserved without a live game run.

## Missing, stale, or blocked surfaces

No country-owned source omission or confirmed defect was found. The following limitations remain explicit:

1. Hearts of Iron IV was not launched, as required. Equipmentless `create_unit`, zero-manpower reinforcement, locked-template recruitment blocking, single OOB loading, origin supply propagation, random-origin transfer, 6–30 opening strength, 30-day anchor activation, 21-day grace, paced spawn, Unfed Broods, AI allocation, world-end footholds, and defeat cleanup are statically evidenced but not engine-exercised.
2. The Event 018 `.83` first-battle response remains the documented bounded response proxy rather than combat telemetry; this is owned by the event/decision surfaces and was not changed here.
3. The Vhorruk animated sheet is intentionally limited to Event Details; the country-leader screen uses the static portrait because no vanilla-safe animated character-portrait precedent is available.
4. The map MCP report is global/partial and contains unrelated workspace diagnostics for 1,323 invalid building positions and 1,331 invalid port-adjacency records. The bounded state render passed and no DHO fixed-state defect exists because DHO's origin is selected dynamically.
5. The available technology MCP scan is global/partial (663 technologies, 18 folders, 1,690 issues, three unresolved) and found no custom DHO technology tree. The installed package still lacks the dedicated Technology Tree Viewer route required by the project instructions, so no technology-tree completion claim is made.
6. The broad `.tools/audit_hoi4_country_tags.py` run is blocked by an unrelated Event 006 registry mismatch (`extra=['BLX']`). A direct DHO scan against mod, vanilla, and available approved reference tags completed successfully.
7. Historical focus and country handoffs retain older 65-focus counts. The current source and MCP evidence are 67; no focus source or unrelated documentation file was edited under this country-only assignment.

## Changed files and validation

Changed file: `docs/plans/018_resources_found_plans/subagent_handoffs/event018_country_final_current_2026-08-09.md` only. No country source, Event 018 gameplay file, localisation, decision, focus, GUI, spreadsheet, or Event 019 provider file was modified by this pass.

Meaningful checks completed: direct DHO tag collision scan; `python -B .tools/audit_chaosx_country_tags.py` (passes its protected registry checks); binary DDS dimension checks for all DHO portraits and counters; TGA dimension/bit-depth checks for all 18 flags; SHA-256 uniqueness scan for the flag set; GFX texture-path existence scan for DHO portraits, focus/idea/state/decision consumers, and cave counters; focus ID/localisation/icon completeness scan; direct zero-manpower/no-equipment and no-navy/air/equipment-transfer source scans; required focus, event, map, and technology MCP inspect/render routes.

Skipped meaningful validation: live game execution, save/campaign simulation, generic peace-conference behavior, actual AI front allocation, and typed probability compare after a source patch, because no source patch was made and the user/AGENTS.md prohibit launching Hearts of Iron IV. The global map/technology MCP limitations above also prevent claiming complete engine evidence.

## Simplifications, omissions, fallbacks, and parent actions

No country route, brood type, commander, flag variant, capacity rule, origin exclusion, neighbor-war rule, world-end gate, defeat outcome, or country-owned asset was omitted or replaced by a fallback. The deliberate static Vhorruk country portrait, Event Details animation split, `.83` adaptation proxy, temporary asset-workspace removal, and absent custom DHO technology tree are documented design/engine boundaries rather than unapproved substitutes. Parent review should carry the stale 65-versus-67 documentation note and the global MCP blockers into the final Event 018 completion report.
