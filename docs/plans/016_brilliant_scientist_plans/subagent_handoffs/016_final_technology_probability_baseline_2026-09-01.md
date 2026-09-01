# Event 016 final technology probability baseline, 2026-09-01

## Status and audit boundary

This is a read-only weighted-logic baseline for the final-completion tranche and records only evidence available from the current repository snapshot plus successful HOI4 MCP artifacts captured before the MCP transport closed.

No gameplay, AI, technology, special-project, decision, effect, trigger, localisation, asset, specification, spreadsheet, or runtime file was changed, and no commit was created.

The worktree contains concurrent changes, so every MCP revision is reported beside the current local SHA-256 captured at handoff time; where they differ, the current local source is treated as the current-source statement and the older MCP result is not promoted to a current comparison.

## Required references

The audit consulted `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-mtth/SKILL.md`.

The required offline wiki pages consulted were Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Technology modding under `paradox_wiki/`.

The vanilla documentation consulted was `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `script_math_functions.md`, `dynamic_variables_documentation.md`, `loc_formatter_documentation.md`, `loc_objects_documentation.md`, `script_collection_input.md`, and `script_collection_operator.md`.

The relevant documentation confirms that `random_list` is probability-proportional to declared weights, `set_technology` grants a named technology, technology research eligibility is a separate trigger path, and AI research weights are not click probabilities.

## MCP identity and source revisions

The successful MCP artifacts use workspace `mod_chaos_redux_ea3b2d67c2c0`, game `Operation Postern 1.19.2.0 (d245)`, adapter `hoi4-1.19.2.v1`, and workspace identity `d8a1d88374e80d7f570cd2a4ef9ae28716f36afe38d2ba5dfdc0db59eff9b6c3`.

| Source | Current local SHA-256 | MCP source revision and source hash used by the evidence |
| --- | --- | --- |
| `common/technologies/016_brilliant_scientist_project_technologies.txt` | `e87aae3518511b2b558187bc12d140200f86e857d68ecc867fcaf5c6af2f4ffe` | `e08719f6a3c55e0337b9e3ebb9d4308e0bf99e2c667b5b24c647356b0a15894`; probability hash `2dd4ab3fff316868b2757718f1967289fb35ba2eb256819490546bc45d27645f` |
| `common/technologies/016_brilliant_scientist_project_force_technologies.txt` | `f8e714ec71c27d21d4c9e8f92b25134f584aaa314b52f5eafcb5500a84b5b26d` | `d773f00a0527f334ec11614bfa3a7216fecb186ac662fc25b29935d9ee648368`; probability hash `c1829588026142345f311bc5a4d004fc8be18d414341d6bf7c310095b4a88e90` |
| `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt` | `3be72d9d560a3d8c92ed42e886bc5a46f7f53ac70f52c47fea6fd6fd6efca3f6` | explicit-inspect/evaluate revision `59161242e7ee872a7ec5e305d80ed1c2ee08d089cc91d97547e63fc8be333253`; aggregate hash `055e2e4f696d47f023a669a8b9b5e63191a8612731b4e4ac4823148c19525152`; candidate provenance hash `3be72d9d560a3d8c92ed42e886bc5a46f7f53ac70f52c47fea6fd6fd6efca3f6` |
| `common/scripted_effects/016_brilliant_scientist_project_effects.txt` | `a240c3a3311dbe26bbd562b985ad20552e4fe6bb2a629a0d0e55bd1d7bb10d7b` | `b0b7f38abc1ccbb2e5da167371cfabcdaad4875452c4f9f54483ec37ef87b1e8`; probability hash `7935e7655aae3f0ff3cc2e1c44fae3aeb62401a197152a2282518f0f05c263e7` |
| `common/special_projects/projects/016_brilliant_scientist_projects.txt` | `b1148c8516e6743be727ee59abe3beb03c8cd347342db8a2c09d4f2dcfa7cdd8` | `f8ac5ed2209eaa9def670c54c1fc83e49c80092253fa32711f618b8f77efc57d`; probability hash `5910f089e202d681af7b9a412c77406745b5a8e6e19c5971f5a8db275d48fc12` |
| `common/decisions/016_brilliant_scientist_technology_actions.txt` | `0dd929bbd12bfe9752a808fcae15943f629d2b7fc6f19940719d5a4cde0a913d` | MCP revision `61db44d39f2e5c15c9c3be8c0f21523c748ede849cb507ed982dd437b62dbfc4`; aggregate hash `ff5a550324ebdb57ec01fa2586c82d4e0a6c2d80fc4c6465ab1dd40930373c7e` |
| `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt` | `1b8d64e32a5281d360a75d3d2a5759261f5b422e58d92f303ac7a5b3e3d5fd6b` | no current MCP revision; probability transport closed before required inspect |
| `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt` | `bbb8a628865a9a35e49ac335a90bc57411db60982eb3332ff433e9437aee46f5` | no separate MCP source revision |
| `common/script_constants/016_brilliant_scientist_project_constants.txt` | `eeb0cd8962ed20a9eb2242885bb407119d92682b0517bb99d3af0da6926eaf96` | no separate MCP source revision |
| `common/script_constants/016_brilliant_scientist_technology_action_constants.txt` | `d3d90a084efdbbd981184aec75b4fe334fda28317a12af7c174c3786bb8a277f` | no separate MCP source revision |
| `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt` | `cd4d626f56c1251a55104f101d595eff2fbfa3ade6c25f7c266cbbdf199bb06f` | no separate MCP source revision |
| `common/special_projects/projects/016_dhrondan_envoy_project.txt` | `77611ed129ebc20f744af1b15143cf24ea29892ee04fcc46723aa6d801b1841e` | no current probability revision; special-project adapter is unavailable |
| `common/decisions/016_dhrondan_contact_decisions.txt` | `d991406da31ab1402d233167a8c1ea7c05f9fea6809d9e294188760f9add5e82` | prior mission artifact source hash `4a370bea603b8759a82a054d48def6cc59b821ba28929b5e6f3ab605da32ee94`; current inspect was blocked by transport |
| `common/scripted_triggers/016_dhrondan_contact_triggers.txt` | `100ee828d677ea9cf97262b911f5b36b9ae587d4f98aed4f98994b469fe9b53a` | no current probability revision |
| `common/script_constants/016_dhrondan_contact_constants.txt` | `0ef8ce2af2dec82b8acc4ee2a7af379129c6d839b649a82eb62cf55e5628aa6f` | no separate MCP source revision |

The force-technology and D'Rhondan MCP hashes predate concurrent changes visible in the current local SHA table, so their older artifacts are retained only as bounded historical evidence.

## 1. Hidden technology research selection and grant-only availability

The audited technology IDs are the eleven hidden IDs in `016_brilliant_scientist_project_technologies.txt` and the seven hidden IDs in `016_brilliant_scientist_project_force_technologies.txt`.

The operational/base IDs are `brilliant_scientist_portal_warfare_tech`, `brilliant_scientist_clone_formations_tech`, `brilliant_scientist_robot_formations_tech`, `brilliant_scientist_paleogenetic_formations_tech`, `brilliant_scientist_xenobiological_formations_tech`, `brilliant_scientist_xeno_chemical_control_tech`, `brilliant_scientist_xeno_neural_control_tech`, `brilliant_scientist_xeno_machine_control_tech`, `brilliant_scientist_xeno_researched_control_tech`, `brilliant_scientist_alien_infantry_tech`, and `brilliant_scientist_temporal_guard_tech`.

The force IDs are `brilliant_scientist_portal_warfare_weaponization_tech`, `brilliant_scientist_clone_formations_weaponization_tech`, `brilliant_scientist_robot_formations_weaponization_tech`, `brilliant_scientist_paleogenetic_formations_weaponization_tech`, `brilliant_scientist_xenobiological_formations_weaponization_tech`, `brilliant_scientist_alien_predictive_warfare_tech`, and `brilliant_scientist_temporal_guard_weaponization_tech`.

Source review shows every listed technology has `allow = { always = no }` and `ai_will_do` with the file-local disabled factor equal to zero, while grant callers use explicit `set_technology` paths in the custom API and project-output effects.

The explicit `technology_ai_will_do` inspection for the operational source returned `PROBABILITY_SOURCE_INSPECTED` with eleven candidates, zero available candidates, one required adapter input, and zero unresolved inputs.

The operational discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7195d46987e8fb4003455ebdb4dced02eac9d38a269adf8017fc030d80746fb9/892131b348090a01268a628d55b56e4b657e1fd97b34d10c3f57141853093441/probability-inspect-2dd4ab3fff31.json`.

The operational explicit-inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f886d5489e6b88070818ee51221a175a7d165957e2d9bb6792a6177009741f6f/52c5e02e2ec247d145afc903f341a33359012104fb059e807c7f825753dce65c/probability-inspect-2dd4ab3fff31.json`.

The force-technology discovery artifact reported seven candidates and suggested `technology_ai_will_do`, and the explicit inspection reported seven candidates, zero available candidates, one required input, and zero unresolved inputs.

The force discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/71ec64fbccdf8a299b4e6c4aebb935d52a1af3fc2c924ee5d2cc576d04fd357b/cea98221705bb8cd0fba8c862556593231b1d62e146c8d8d8a22c5e5a5fc800489/probability-inspect-c18295880261.json`.

The force explicit-inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38efdfbd7fa04b76113466868543af1e6bf392f858108665e1cd9593fd536e/5baedceccd768b277dfc909583a2814569ca0abd8069c481dd81a87ec8b2a956/probability-inspect-c18295880261.json`.

Targeted `hoi4.tech_inspect` explain reports provide structural support for the ordinary-research exclusion.

For `brilliant_scientist_portal_warfare_tech`, the report marks `hidden: true`, preserves the raw `allow = { always = no }`, reports `ai.factor = @CR_SC_BRILLIANT_SCIENTIST_PROJECT_TECHNOLOGY_AI_DISABLED`, finds no research weights, and traces grants from `brilliant_scientist_rebuild_project_force_runtime_package`, `chaosx_grant_custom_operational_technology_core`, and `brilliant_scientist_apply_project_stage_output`.

The portal structural artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e604f1b0fbad619d56b703ba57130fab14e07d49c05346a065ad34bf64acc4c9/c4e0a298b63fd68c841c82e8d76ce4353f45cf83fe8980b92b26970d05b214c6/technology-explain-24faa55703e9.json`.

For `brilliant_scientist_xeno_chemical_control_tech`, the report likewise marks `hidden: true`, preserves `allow = { always = no }`, reports zero AI research weight, and traces explicit grants from the runtime package, custom upgrade API, project-stage output, inheritance output, and grant reapplication helper.

The xeno-control structural artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e49c5760d530895ab662e14ef118f0ad3bae690d4e647cc796a716fb3c7b250a/02c28f0f76aed4d84eb994ff305b6eec426958508da25972c4fca75aa9ce3c4f/technology-explain-24faa55703e9.json`.

The targeted structural result is classified `bounded` rather than exact runtime proof because the technology analyzer explicitly does not execute runtime `allow` triggers or exact research-choice behavior, and the full graph carried 1,427 inherited blocking diagnostics outside this targeted evidence boundary.

The xeno report also emits `TECH_SUSPICIOUS_IDENTICAL_SIGNATURE` for the four xeno control IDs; this is a design warning about identical parsed effects/unlocks/year/categories and should be reviewed independently of probability.

`hoi4.tech_render` was required for the rendered structural view but failed twice with the exact error `tool call error: tool call failed for \`hoi4_agent_tools/hoi4.tech_render\`\n\nCaused by:\n    Transport closed` after the explain reports completed.

Conclusion: the source and targeted structural MCP evidence support grant-only, unavailable-to-ordinary-research behavior for the examined hidden technologies, but no current rendered technology view or runtime research simulation is claimed.

## 2. Public random operational-technology API

The audited helper is `chaosx_grant_random_custom_operational_technology` in `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:216-272`.

The helper zeroes seven temporary weights, assigns `constant:chaosx_custom_technology_tuning.random_candidate_weight` to each unowned base technology, executes one seven-entry `random_list`, sets a temporary applied flag only inside a selected branch, and therefore has a source-level all-held no-op contract.

The tuning constant is `chaosx_custom_technology_tuning.random_candidate_weight = 1` in `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt:56-63`.

The complete candidate pool supplied to MCP was:

- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:234.entry.1` -> portal.
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:234.entry.2` -> clone.
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:234.entry.3` -> robot.
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:234.entry.4` -> paleogenetic.
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:234.entry.5` -> xenobiological.
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:234.entry.6` -> alien infantry.
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:234.entry.7` -> temporal.

The source discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/871b226d2e887be28565cf18e76d036d2a83e86fdbed40be92463e95c43dd660/e4648f89865e7099e7d42167713a821e13a957b9f39f0da5bc34a7f8df9b104d/probability-inspect-055e2e4f696d.json`.

The broad random-list inspection saw both the seven-entry public pool and the eleven-entry external-upgrade pool, for eighteen candidates total, and returned an incomplete pool with eighteen required inputs and one unresolved item because dynamic entry weights were not declared as direct scenario inputs.

The broad artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c53ae24878c7abd7c69784649ce6b712cd03fc9a3c7c41dc64c2dfb15be054ef/be9f0e47e8ac8863bbd4ef0b0087b7e66c5ede856a46592240e64a06d9ebc170/probability-inspect-055e2e4f696d.json`.

The narrowed seven-entry inspection returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = true`, seven candidates, seven required direct weight inputs, and zero unresolved items.

The narrowed artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/021f9e8d36780e347038baf0cce68e2d0da29528d8a3a66291695e8a2ddf5976/f93b978fabab1d049ac93c5257e7137ea6fc63d65897e5ac3ded008c8929f488/probability-inspect-055e2e4f696d.json`.

The adapter reports `selectionRule = proportional_categorical`, supports raw scores, eligibility, and normalized conditional probability, requires a complete pool, and does not provide campaign cadence or timing distributions.

The named scenario set `E16_CUSTOM_OPERATIONAL_RANDOM_BOUNDARIES_2026_09_01` supplied the complete seven-entry pool and these direct weights, with all unspecified external factors held outside the adapter boundary:

| Scenario | Portal | Clone | Robot | Paleogenetic | Xenobiological | Alien infantry | Temporal | Candidate/external completeness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `CUSTOM_POOL_ALL_UNOWNED` | 1 | 1 | 1 | 1 | 1 | 1 | 1 | Complete direct-weight pool; no campaign timing |
| `CUSTOM_POOL_ONLY_ROBOT_UNOWNED` | 0 | 0 | 1 | 0 | 0 | 0 | 0 | Complete direct-weight pool; owned-state exclusion declared |
| `CUSTOM_POOL_ROBOT_ALREADY_OWNED` | 1 | 1 | 0 | 1 | 1 | 1 | 1 | Complete direct-weight pool; owned-state exclusion declared |
| `CUSTOM_POOL_ONLY_PORTAL_UNOWNED` | 1 | 0 | 0 | 0 | 0 | 0 | 0 | Complete direct-weight pool; owned-state exclusion declared |
| `CUSTOM_POOL_ZERO_ELIGIBLE` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Complete pool but zero-total fallback is not specified by adapter |

The combined analysis is `probability-62539e247885816fd50318e9` with scenario hash `4e8abc9140f865affe052be02cf59e923dcbe7d9d966c873054fb6b679f89152`.

Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72fbcc9063a0297139c739b9edc7b165f12a4f419e3b9cd87e0b41677539b781/ca2a970de9d9f65b1d7b009c23e409a8a6af38796f821056c4ffd35410009c51/probability-62539e247885816fd50318e9.json`.

The rendered ranking, matrix, sensitivity, threshold, and unresolved artifacts are respectively `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b7226e9f8d02a41ecc34b3e2a154ca9e1875385f86c50d8b7b1ceb403f579d4/abd715d8cb5d68089c363bdc3ab03bca5c4746992affc4d079dce7025bbfd067/probability-probability-62539e247885816fd50318e9-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9f48d0492213632465d3ace671c87630cfecf91beb38fc2265441f33b7d03c58/078fc6bf25e516f5851b2836acaff81a815a25e00ad47b276d7a839f6222c1e3/probability-probability-62539e247885816fd50318e9-matrix.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b5c9f25c05e945e4802758bf83a6ae6c00e228396e9d6b66826e5e21c99ad27/5011ff0de4f3d7d8ca8f15ee44b4033112e78d4eb3f47c7b0ab6f4341486c75b/probability-probability-62539e247885816fd50318e9-sensitivity.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50d004a8643beccd6266fc5b98ed8958cf40a6f2eb59bfaad471d998a4580b96/549e25330538375cee2230c1697e2e2d89f610c1b6f3b472df931f3dd4a61ee5/probability-probability-62539e247885816fd50318e9-threshold.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/7e21dd30c9d72a195cafa4fd72a9fd7155ea0ff7f810d184e058eb31e44110b/probability-probability-62539e247885816fd50318e9-unresolved.svg`.

The all-unowned scenario `E16_CUSTOM_OPERATIONAL_RANDOM_ALL_UNOWNED_2026_09_01` returned seven raw weights of one and an exact conditional probability of `1/7 = 0.142857142857142857` for every candidate, with rank order matching source entry order and zero diagnostics.

Its analysis is `probability-dbd018aed4e4700a35645997` with scenario hash `0f236328c12e3dfc575f98ed0c78b109cc8f8c363a51bf667cd083b07f5f92f4`, and its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee3293a155e66d296eb45cd0c8f4fbe0c4ebd8e1e9c82aff72fa551df679b03b/f3152a6c726000c8dcc9300957018608e46ce067081240ed62d0aa26cb9bf0db/probability-dbd018aed4e4700a35645997.json`.

The only-robot scenario `E16_CUSTOM_OPERATIONAL_RANDOM_ONLY_ROBOT_2026_09_01` returned robot raw weight one and conditional probability one, with all six owned candidates at zero probability.

Its analysis is `probability-e61da1da28b5fd5fe0eb0b02`, with scenario hash `7f36f16575338f5da49d2659eca7304398f69ad84f59c106a37d667f4afd4da9`, and its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fec4167740ddad32877de69bff423b8a111a644edcc7072954c6856f59854f47/88eeaba5e0b2ce1f6651c11e4760362525a76b15544d0c296e1333c8e9fff180/probability-e61da1da28b5fd5fe0eb0b02.json`.

The robot-owned scenario `E16_CUSTOM_OPERATIONAL_RANDOM_ROBOT_OWNED_2026_09_01` returned six remaining candidates at raw weight one and exact conditional probability `1/6 = 0.166666666666666666`, with robot at zero probability.

Its analysis is `probability-9af323923de88ed78a7adffe`, with scenario hash `0328c642252f9de0ab5390330f94988485e22e936d84378394323fcb58391361`, and its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b53810c60ef403e89cd8ca43d259e931f786bdc53b4da63879034bff5c64afb/fc3bf0892f388f2e144d02abafa6702cf422ed2fb9f323bbf69dd5406e391863/probability-9af323923de88ed78a7adffe.json`.

The zero-eligible scenario `E16_CUSTOM_OPERATIONAL_RANDOM_ZERO_2026_09_01` returned all raw values zero and null conditional/path probabilities with diagnostic `PROBABILITY_ALL_ELIGIBLE_VALUES_ZERO: All eligible values are zero in CUSTOM_POOL_ZERO_ELIGIBLE; adapter fallback behavior controls the result`.

Its analysis is `probability-93854cc8fceffab28d80ef4e`, with scenario hash `dc89aaa55b984d63c4ea4e1c8e045a8828b6b7c5d929a00548ecddc3f97a675f`, and its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/adc679f89a5f6b2258a7d6cda7417134e23dbfc213c4d658656a1affe691f697/7167592850878be64040ec77d060ee201d949a8b2a776aefda2d66ee7afe5ccf/probability-93854cc8fceffab28d80ef4e.json`.

The one-left cases produce expected dominance and starvation diagnostics for zero-weight entries, while the all-held case leaves the adapter fallback unresolved.

These four nonzero cases are classified `exact` only for conditional selection under the seven directly declared weights; they do not prove campaign frequency, grant cadence, duration, or runtime state transitions.

Source review supports an idempotent no-op when all seven technologies are held, but no MCP runtime effect execution proves the temporary applied flag or no-op behavior.

The eleven-entry external-upgrade random list at `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:380-414` was discovered in the broad inspect but was not normalized because its dynamic weights and overlap/recovery state were not declared as a complete custom scenario.

## 3. New four-way materials synthesis random list

The parent-introduced source `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt:50-62` defines `brilliant_scientist_complete_materials_synthesis_works` and a four-entry `random_list` at lines 54-59.

The four source entries are `:54.entry.1` aluminium, `:54.entry.2` tungsten, `:54.entry.3` chromium, and `:54.entry.4` rubber, each with literal weight one and each applying `constant:brilliant_scientist_technology_action.synthesis_resource_amount` to the selected `FROM` state.

This is a newly introduced source with no pre-source candidate or before snapshot, so `hoi4.probability_compare` has no valid before side.

The mandatory `hoi4.probability_inspect` for this source could not be completed because the MCP transport closed after the technology explain call and returned the exact error `tool call error: tool call failed for \`hoi4_agent_tools/hoi4.probability_inspect\`\n\nCaused by:\n    Transport closed` on retry.

The named baseline scenario reserved for the later retry is `E16_MATERIALS_SYNTHESIS_RESOURCE_DRAW_2026_09_01`, with the complete four-entry pool, a valid `FROM` state, and no declared external weight modifier.

No probability, uniformity, timing, or no-op conclusion is claimed for this random list until MCP inspect and evaluate succeed.

## 4. New technology-action decision AI scores

The parent-introduced source `common/decisions/016_brilliant_scientist_technology_actions.txt` contains eight new decision IDs under `brilliant_scientist_directorate_category`:

- `brilliant_scientist_launch_predictive_campaign`.
- `brilliant_scientist_saturate_sensor_region`.
- `brilliant_scientist_construct_state_synthesis_works`.
- `brilliant_scientist_activate_high_speed_strike_network`.
- `brilliant_scientist_launch_long_range_delivery_strike`.
- `brilliant_scientist_raise_field_projectors`.
- `brilliant_scientist_order_emergency_regeneration`.
- `brilliant_scientist_order_epidemic_control`.

Each decision uses `base = constant:brilliant_scientist_technology_action_ai.base`, currently eight, with source modifiers of wartime factor three, peace factor 0.5 on high-speed strike, resource-shortage factor two on materials synthesis, high-exposure factor 1.5 on epidemic control, and two additional wartime factors for long-range targets containing an arms factory or industrial complex.

The source discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dce1da6220987c733a02f09d862449f3cee1c72d2c5259167b66565a50611118/7bca5702fe56e5b9aff969b2dfc0ec3a767e9158fde9c75a1051db4a62c453a3/probability-inspect-ff5a550324eb.json`.

An explicit request for `decision_ai_will_do` returned source discovery with `requestedAdapter = decision_ai_will_do`, `discoveryReason = requested_adapter_empty`, and suggested `mission_ai_will_do` rather than a decision adapter.

The exact requested-adapter artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68bd3bb54ca82e141afa6691afe3a7657ed0018e8946fa0c8c6cd2f04d5281bf/26e9611653232ed6b609f68608964748db00334065a5530e9812c133a8eafb5d/probability-inspect-ff5a550324eb.json`.

The rerouted `mission_ai_will_do` inspection returned eight candidates, seven required inputs, zero unresolved inspect items, `poolComplete = false`, and score-only capabilities with `normalizedProbability = false`, `rawScore = true`, and `selectionRule = score_only`.

The rerouted artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6481a301ba52fdf2be1d4a6ecfe5ee9d1eba955205f3f0d2bfa75c1202b7156a/3f9ded8cfccaac0572b9b6f03459536c07740eb291671eb97b7e3cf2e24ef20e/probability-inspect-ff5a550324eb.json`.

The source-identified candidate pool is complete as eight decision IDs, but the adapter cannot resolve the decision gates without runtime fixtures for `FROM`, `check_variable`, `custom_trigger_tooltip`, `has_character`, `has_resources_in_country`, `has_war`, and `is_in_array`.

Named scenarios reserved for the post-transport evaluation are `E16_TECH_ACTIONS_PEACE_BASE_2026_09_01`, `E16_TECH_ACTIONS_WARTIME_BASE_2026_09_01`, `E16_TECH_ACTIONS_RESOURCE_SHORTAGE_2026_09_01`, `E16_TECH_ACTIONS_HIGH_EXPOSURE_2026_09_01`, and `E16_TECH_ACTIONS_TARGET_FACTORY_2026_09_01`.

No score trace, ranking, dominance, starvation, rank reversal, or probability result is claimed for these decisions because evaluation was blocked by the same MCP transport failure.

These decisions are newly introduced and have no pre-source candidate, so no before/after probability comparison exists.

This surface is inherently score-only in the installed adapter; even after the helper fixtures are supplied, a score must not be presented as a click probability.

## 5. Project-family selection, stage progression, and project AI

The native project source `common/special_projects/projects/016_brilliant_scientist_projects.txt` contains ten family prototypes (`sp_brilliant_scientist_computational_engine`, `sp_brilliant_scientist_advanced_materials`, `sp_brilliant_scientist_biomedical_acceleration`, `sp_brilliant_scientist_quantum_transit`, `sp_brilliant_scientist_cloning`, `sp_brilliant_scientist_autonomous_cognition`, `sp_brilliant_scientist_paleogenetics`, `sp_brilliant_scientist_xenobiological_synthesis`, `sp_brilliant_scientist_alien_arms`, and `sp_brilliant_scientist_temporal_mechanics`) plus six Strategic Singularity components.

Each project delegates `visible` and `available` to family or Singularity helper triggers, uses `ai_will_do` with base `constant:brilliant_scientist_project_ai.base = 1`, multiplies by `preferred_factor = 2` during war, and multiplies by `cautious_factor = 0.50` when project capacity is low.

The project output records the family selector and requests the prototype stage; later progression is performed by `brilliant_scientist_advance_project_to_requested_stage` and the stage-entry array in `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`, not by a random stage pool.

`hoi4.probability_inspect` on the native project source returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, zero probability candidates, zero required inputs, and zero unresolved items.

The special-project discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/484405b72cc016f71e0b0941818443fe1a544462e96ba0eef2b94b972c14ea2d/2d4d30edeb86d5a46ec181a8311e026c473acba588dc01248fc0a565815fd2d2/probability-inspect-5910f089e202.json`.

The installed probability adapter set has no `special_project_ai_will_do` option; the recorded exact validation blocker is `Invalid option: expected one of event_mean_time_to_happen|event_option_ai_chance|decision_ai_will_do|mission_ai_will_do|national_focus_ai_will_do|technology_ai_will_do|doctrine_ai_will_do|direct_random|random_list|ai_strategy_factor|custom_weighted_pool at adapter`.

The native source candidate set is therefore structurally identified but not a probability-normalizable pool, and runtime family eligibility remains dependent on the helper triggers and project state.

Conclusion: project AI evidence is `score-only/source-backed`, with no exact family-selection probability, no exact stage-selection probability, no project timing distribution, and no MCP-proven dominance or starvation result.

## 6. Kruger/Mengele D'Rhondan expedition competition and owner eligibility

The current route gates are in `common/scripted_triggers/016_dhrondan_contact_triggers.txt:85-139`.

`dhrondan_kruger_expedition_is_available` requires the current host, completed `sp_dhrondan_envoy_craft`, `KRG_warren_kruger`, an active and neither injured nor confined Kruger character, no expedition obligation or completed pact, no country/global transaction lock, no active expedition, and no world end.

`dhrondan_mengele_expedition_is_available` requires a Mengele clone Directorate country, the completed envoy craft, no pact, no active expedition, and no world end.

The AI helper `dhrondan_ai_try_authorize_expedition` in `common/scripted_effects/016_dhrondan_contact_effects.txt:182-210` checks the two route gates and then uses `if = { limit = { dhrondan_kruger_expedition_is_available = yes } }` before `else_if = { limit = { dhrondan_mengele_expedition_is_available = yes } }`, so simultaneous validity is deterministic Kruger-first priority rather than a weighted competition.

The two visible authorization decisions in `common/decisions/016_dhrondan_contact_decisions.txt:17-81` both use `constant:dhrondan_contact_ai.dominant = 10000`; the Honor Accord uses base 25 and a factor four at strain at least 50 from `common/script_constants/016_dhrondan_contact_constants.txt:41-52`.

The prior mission inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b6bad52efe5c36c2f44f9c0a6c8f3b313f09a9d34cf89916457a815c94b95ce/6328d96f90d99757cc84d523c1e72e7c35d1391cfd7e8640310bee42445a6585/probability-inspect-4a370bea603b.json`.

That mission inspection found the three candidate decisions, an incomplete pool, zero available candidates, seven required inputs, and a score-only mission adapter.

The prior named scenario set was `DHR_CONTACT_MISSION_BOUNDARIES_2026_08_25` with complete source candidate IDs `dhrondan_honor_accord`, `dhrondan_send_kruger_to_dhronda`, and `dhrondan_send_mengele_to_dhronda`, and scenarios `NO_CONTACT`, `KRUGER_VALID`, and `MENGELE_VALID`.

The prior partial evaluation analysis is `probability-b8cebaa477512d4b075e6a36` with scenario hash `f2a98db3da2f984cb5e3b50312f34f7d96c28a6bb3d1973febfffb8936629326`.

Its JSON, ranking, matrix, and unresolved artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9fdf89bef67a4c75ee9babac612d6cf66ce2bd688005202e5b2d6e2248cab1d/5a9702299c2b9ca07aea344ea734044492c28383f0f1db454ea7a5989f515b1d/probability-b8cebaa477512d4b075e6a36.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67ba7f7d024b2c562b3c908443b8faccd14c646b9fa358f34ff7464352edb38f/5c2806d7236d50724ba5f1fb3cb6de726c15fcd0789b3296206834627135a741/probability-probability-b8cebaa477512d4b075e6a36-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c1060abfad4b9be2f38f2cefdc928a3075d88c7a8349e74b3028e1dd9d7c06d/e981bfce2588fb59d6a6f70859ee30faf1cf7a9a2c91de54ba2b0e7ebc7b0bc4/probability-probability-b8cebaa477512d4b075e6a36-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82d1506a90f1e34eecbd71aa9448006c988556b0a0b5ba55f9f3529a4c62ee69/1c34a1750006aa5ae8d90de1e391a708ec51454ab316cabc5367a19cf32d1c54/probability-probability-b8cebaa477512d4b075e6a36-unresolved.svg`.

The partial result had eleven unresolved inputs and eight diagnostics, including unresolved `has_character`, `KRG_warren_kruger`, `exists`, `has_cosmetic_tag`, `is_special_project_completed`, `custom_trigger_tooltip`, and numeric pact-strain state.

The prior evaluation did not prove an exact expedition-selection probability or timing distribution, and the current D'Rhondan inspect/evaluate retry was blocked by the MCP transport closure.

Conclusion: the current source still contains a real Kruger-first deterministic route-order risk if both owner gates can be simultaneously true, while exact current score/ranking validity remains `partial/score-only` until runtime fixtures and a fresh MCP revision are available.

## 7. MCP failures, skipped analyses, and comparison boundary

The initial adapter-shaped inspect without a source returned the exact validation error `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: An adapter requires a source; provide a source alone to discover compatible adapters`; subsequent source-first inspection succeeded for the operational, force, API, project-effects, native-project, and new decision sources.

After the targeted technology explains, `hoi4.tech_render` returned `Transport closed` twice, and subsequent probability-inspect attempts for the materials source returned `Transport closed` twice.

The materials inspect/evaluate, new decision score evaluate, current D'Rhondan probability inspect/evaluate, dedicated `probability_sweep`, and fresh probability renders are unresolved because of that transport failure.

No `probability_simulate` or `probability_sequence` run was performed because no complete uncertain-input fixture or cadence/state-transition contract was supplied, and the server became unavailable before such a call could be made.

No `hoi4.probability_compare` result is claimed because the parent-introduced materials and decision surfaces have no pre-source candidate, and the public API and current project/route surfaces had no owner-applied before/after source in this tranche.

## Risks and recommended follow-up without applying fixes

- Reconnect the HOI4 MCP server and run `probability_inspect` then `probability_evaluate` for `E16_MATERIALS_SYNTHESIS_RESOURCE_DRAW_2026_09_01` with the four exact entries at line 54, preserving `FROM` state scope and resource amount as external factors.
- Reconnect the MCP server and evaluate the eight new decision IDs under the named peace, war, shortage, exposure, and target-factory fixtures, retaining score-only classification and never normalizing scores into click probabilities.
- Re-run targeted `hoi4.tech_render` for representative hidden operational, force, and xeno-control IDs and investigate the `TECH_SUSPICIOUS_IDENTICAL_SIGNATURE` design warning before relying on the full hidden-tech family as a clean graph baseline.
- Re-run the public API zero-total scenario to determine whether the engine no-op matches the source contract; until then, treat no-op behavior as source-only and the adapter fallback as unresolved.
- Inspect the eleven-entry external-upgrade pool separately with a complete declared state because the broad source inspection found it adjacent to the public seven-entry pool but did not prove its eligibility or repetition behavior.
- Preserve explicit current-owner semantics for Kruger and Mengele and fresh-test the simultaneous-validity state; if the design requires competition rather than priority, the route-order helper at `common/scripted_effects/016_dhrondan_contact_effects.txt:193-200` is the concrete owner review point.

No balance target was selected and no recommended fix was applied.
