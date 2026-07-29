# Event 016 Kruger State focus runtime audit handoff

Date: 2026-07-29

Owner: `/root/event16_focus_runtime_audit`

Status: runtime audit complete; no gameplay patch was required inside the narrowed focus-tree scope.

## Files and surfaces reviewed

- `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_focus_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`
- `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt`
- `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt`
- `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`
- `interface/016_brilliant_scientist_kruger_state_focus.gfx`
- `localisation/english/016_brilliant_scientist_focus_l_english.yml`
- `common/decisions/016_*` and `common/decisions/categories/016_*` consumers

## Route coverage

| Route surface | Focus IDs | Runtime result |
| --- | --- | --- |
| Formation and origin gates | `KRG_audit_inherited_portfolio` through `KRG_complete_the_founding_audit` (001-010) | Implemented; audit is the sole root and the four origin openers are branch-gated. |
| State purpose and sovereign identity | `KRG_define_the_states_purpose` through `KRG_the_project_synthesis` (011-030) | Implemented; human, directorate, clone, machine, temporal, xenobiological, and synthesis routes use identity-open gates and route locks. |
| Economy, facilities, and supply | `KRG_stabilize_the_laboratory_economy` through `KRG_sustainable_project_capacity` (031-040) | Implemented; one of the four supply choices is accepted by the single OR prerequisite block, with maintenance and facility validity checks in `available`. |
| Conventional security | `KRG_restore_the_ordinary_chain_of_command` through `KRG_a_council_of_project_commanders` (041-047) | Implemented; command and counterintelligence rewards are represented by consumed focus unlock flags. |
| Cloning project lane | `KRG_audit_the_growth_halls` through `KRG_the_replicated_host` (048-053) | Implemented; stage/history triggers gate the lane and capstone. |
| Robotics project lane | `KRG_wake_the_assembly_lines` through `KRG_an_army_of_machines` (054-059) | Implemented; stage/history triggers gate the lane and capstone. |
| Paleogenetics project lane | `KRG_open_the_restoration_ledger` through `KRG_the_dinosaur_host` (060-065) | Implemented; stage/history triggers gate the lane and capstone. |
| Xenobiological project lane | `KRG_open_the_designed_organism_dossier` through `KRG_the_engineered_legion` (066-071) | Implemented; exact control mode and stage/history triggers gate the lane and capstone. |
| Portal and temporal lanes | `KRG_recover_the_transit_logs` through `KRG_the_continuity_guard` (072-082) | Implemented; deployment, anchor, evidence, stabilization, and debt checks are present. |
| Exotic and biological lanes | `KRG_build_an_independent_reactor_grid` through `KRG_authorize_agents_of_last_resort` (083-088) | Implemented; delivery, containment, and rare-material checks are present. |
| Diplomacy and foreign policy | `KRG_a_state_without_friends` through `KRG_settle_accounts_with_the_former_host` (089-093) | Implemented; recognition, intelligence, patron, and former-host consumers are wired. |
| Expansion and integration | `KRG_open_the_scientific_commonwealth` through `KRG_the_continental_laboratory_network` (094-097) | Implemented; integration requires a foreign route, one project capstone, and capacity/overextension checks. |
| Evolution and terminal choices | `KRG_evolution_four_sovereign_science`, `KRG_commit_to_the_laboratory_world`, `KRG_commit_to_the_strategic_singularity` (098-100) | Implemented; evolution availability, scenario switches, and terminal mutual exclusion are explicit. |

No undefined prerequisite or mutual-exclusion target was found (81 references checked; zero bad/self references). The separate prerequisite blocks used for AND semantics and single blocks used for OR semantics match the offline national-focus reference.

## Load and engine evidence

`hoi4.focus_inspect` inspected one tree from `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`:

- 100 focuses, 100 resolved titles, 100 unique IDs.
- KRG tree diagnostic count: 0.
- Layout: 108 connectors, 0 crossings, 0 node intersections, 0 long connectors, 0 same-row spacing violations.
- Bounds: x 0..52, y 0..20; layout hash `2051c203ebb08be69fbdf861193ea1b0d14345c6f393f7f331809834c78e2633`.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b11d8ff941a6a790dc8ca3050060dbd59bcfa0dfaa27b69edcde4d297b90d36e/bca4d804fbffe43ca726e0fbfa792f3c08c2f6c925979b29b1067a7469b1d34e/focus-inspect.fc6bdcfe86acb6ab.json`.

`hoi4.focus_render` also completed. Render artifacts:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8f95a3995f66ac4b309b09efc8de002c31fe456c2a7966f323a22514084dfe8c/69ec53bccaf5b4c0042cc5e0764432f823d3899ada2032c6f453d8032ae1be11/brilliant_scientist_kruger_state_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3940e09ebb5223b75ebc586a321aa5edc7bc8d4955d8f99332da13ca426dd532/c12230e85e368a4d589d798f6ef2185d8ff423ced141e0a206b30ba1d6936331/brilliant_scientist_kruger_state_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54a8228139e70350ab634cc22f8748f74a85dc321319154bfe1b53220c0aa221/31385096af9358c60e89fca11e70674c432a21103e6cb1fcddf5e6c0ffb359dd/brilliant_scientist_kruger_state_focus_tree.focus.json`

The MCP validation result is globally false only because the vanilla `common/continuous_focus/generic.txt` scan reports 13 missing generic/foreign focus sprites and one unrelated localisation key (`DEN_*`, `ETH_*`, `SWI_*`, and `continuous_*`). None references the KRG tree or its assets; no unrelated files were changed.

## Icon coverage

| Surface | Coverage | Evidence |
| --- | --- | --- |
| Focus `icon =` references | 100/100 unique `GFX_goal_KRG_*` IDs | Static cross-check against the focus file. |
| Regular and shine sprites | 100/100 regular and 100/100 `_shine` definitions | `interface/016_brilliant_scientist_kruger_state_focus.gfx`. |
| DDS textures | 100/100 base textures present | `gfx/interface/goals/016_brilliant_scientist/goal_KRG_*.dds`. |
| Texture paths | 0 missing path targets | Static filesystem check. |

## Localisation and reward mismatch audit

- 100/100 focus title keys and 100/100 `_desc` keys exist in `localisation/english/016_brilliant_scientist_focus_l_english.yml`.
- Every `custom_effect_tooltip = KRG_*_effect_tt` used by the tree resolves in that file; the one custom trigger tooltip (`KRG_sovereign_identity_open_tt`) also resolves.
- No title/description mismatch was found against the corresponding focus IDs.
- Every `set_country_flag = brilliant_scientist_focus_unlock_*` emitted by the tree has at least one consumer in `common/` (zero consumerless flags).
- Focus completion blocks do not directly add equipment, manpower, factories, or units. Project capstones call the idempotent `brilliant_scientist_rebuild_project_force_runtime_package` helper only.

## AI behavior

All 17 Event 016 AI plans are defined and have an `allowed`, `enable`, `abort`, and `ai_national_focuses` block. Their focus references resolve to the 100 KRG IDs. Route plans cover charter, rebellion, enclave, takeover, clone, machine, paleogenetic, xenobiological, portal, temporal, alien-arms, biological containment, biological last resort, commonwealth, submission, laboratory-world, and singularity outcomes (`common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt:15-455`). Route capstones are aborted or assigned factor 0 after completion, and terminal plans are mutually disabled.

The remaining AI risk is coverage depth rather than an unresolved ID: `ai_national_focuses` lists intentional route priorities, while ordinary focus `ai_will_do` values handle support nodes. A separate balance pass should verify route selection under every formation origin and disabled-evolution scenario; no load blocker was found.

## Materialization and repeatability check

Formation entry points call `brilliant_scientist_apply_project_force_package_from_history` before loading the tree (`common/scripted_effects/016_brilliant_scientist_country_effects.txt:589-610,850-890`). The dispatcher is guarded by `brilliant_scientist_can_apply_project_force_package_from_history`, which requires a valid KRG/host carrier, Kruger, an owned carrier-controlled state, and `NOT = { has_country_flag = brilliant_scientist_project_force_package_from_history_applied }` (`common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt:612-622`). Family helpers also require the transaction flag and their own persistent `*_materialized` receipt (`:627-685`). Re-entry therefore rebuilds caps/technology without re-spawning formations; no repeatable focus path bypasses these guards.

## Missing, simplified, or deferred content

No missing runtime route, focus ID, icon, localisation key, unlock consumer, or AI plan was identified in this narrowed audit. No gameplay simplification was introduced by this audit. Broader flavour/depth expansion and scenario balance remain outside the requested runtime-readiness scope and should not be inferred as completed from this handoff.

## High-priority fixes and remaining risks

1. Treat the 14 MCP global diagnostics as a separate generic-focus asset/localisation task; do not patch them as Event 016 focus defects.
2. Run the parent-owned route/decision balance pass over all 17 AI plans, especially terminal plan selection and disabled-evolution scenarios.
3. Re-run the focus inspector after any shared generic continuous-focus asset fix so the global validation state is distinguishable from the KRG tree result.

No rollback or recovery action was needed because no gameplay files were changed.
