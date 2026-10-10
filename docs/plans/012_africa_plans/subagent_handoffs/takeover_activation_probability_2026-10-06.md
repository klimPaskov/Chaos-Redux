# Event 012 Gods activation eligibility probability audit

Status: Baseline evidence is captured. The parent has applied the planned three-file repair and is reviewing one additional World-form progression edge. The post-change decision-score pass and compare currently available in this report are intermediate only; final after evidence is pending the parent's final helper hash.

This is a read-only handoff for the activation eligibility repair. I made no gameplay, AI, event, focus, decision, mission, doctrine, technology, localisation, or tuning edits. The parent owns the repair and live-game validation.

## Audited weighted surface

The only weighted surface in this narrow scope is the `decision_ai_will_do` adapter over `common/decisions/012_africa_gods_decisions.txt`. The requested candidates were the five previously audited participant response intents `gods_of_africa_comply_demand`, `gods_of_africa_substitute_demand`, `gods_of_africa_negotiate_demand`, `gods_of_africa_refuse_demand`, and `gods_of_africa_permanent_defiance`, plus the host's doctrine decisions `gods_of_africa_choose_reciprocal_covenant`, `gods_of_africa_choose_sovereign_exaction`, and `gods_of_africa_choose_strategic_ambiguity`.

These are decision willingness scores, not click probabilities. The adapter declares `selectionRule=score_only`, `normalizedProbability=false`, and `completePoolRequired=false`; the five participant intents and three doctrine choices do not form one live decision race, and the request did not provide all decision categories or target-array actors.

The activation defect itself is in an unweighted scripted-trigger/effect path. No `ai_will_do`, `ai_chance`, MTTH, research, doctrine-selection, random-list, random-event, or AI-strategy weight was changed by the parent patch.

## Before source and dependency hashes

The exact bytes copied before the owner patch are under `docs/plans/012_africa_plans/subagent_handoffs/takeover_activation_probability_2026-10-06_evidence/`. The three files the parent planned to edit are also the relevant eligibility, first-proof chronology, and milestone caller sources. Hashes below are SHA-256 of exact copied file bytes, not the MCP's normalized source hash.

| Source path | Before SHA-256 | Parent-reported after SHA-256 |
| --- | --- | --- |
| `common/scripted_triggers/012_africa_gods_epoch_binding_triggers.txt` | `5afb48b7e53e2d1aa2f47fde96742add41f85c7203c94842093bdf674effb67e` | `6b0a22c6f03f5ca5bf78b6b00e10014513036fded63a1da97b6aafa66c23d68c` (intermediate owner version; final version pending) |
| `common/scripted_effects/012_africa_triggerable_scenario_effects.txt` | `f6554dece95c091db2e7ed60f0fef647853b46107ca473f62a187d2878258197` | `3c515a4d0b17947e9d89709e49ef2b1260f2223ff1c87ace46fdf190030c0bd2` |
| `common/scripted_effects/012_africa_focus_route_effects.txt` | `8f57e66cb69a5768a25a2d8ca044a628fe45abf7dfd709f9395552bf1e29859f` | `dc220b4c80eb5c9150518a325dc3c810b1f5b80dfaed9e23c2245ce31d36c838` |
| `common/scripted_effects/012_africa_gods_recovery_effects.txt` | `14affd56c1200bd1289b00973ba151158b686065e42b13421b8ecbd2dae562a2` | unchanged at baseline capture |
| `common/scripted_effects/012_africa_gods_effects.txt` | `f9fcb0d37264eb6e10e64ca8b774226c17804170fae194bf616f4155aa00d51` | unchanged at baseline capture |
| `common/scripted_triggers/012_africa_gods_recovery_triggers.txt` | `3664ab41fa1bfc62eca631c5e1618cfa94e3e3dda7568d0c749c816e5e34369c` | unchanged at baseline capture |
| `common/scripted_triggers/012_africa_gods_triggers.txt` | `5f8e6ff91f20ab804d6f6900120defee82a99f85ac04a734b8f5939e260e687b` | unchanged at baseline capture |
| `common/scripted_triggers/012_africa_world_order_triggers.txt` | `51a995d3b83109798862216b475124e328b28e304b6934ee677de3e5facd7a23` | unchanged at baseline capture |
| `common/script_constants/012_africa_world_order_constants.txt` | `c902dd4d8a10f4de871d6b5e4db5fd784d947f34f942d77cd67e199c792ed6ed` | unchanged at baseline capture |
| `common/scripted_effects/012_africa_evolution_effects.txt` | `81a3be56dc3b931588cb11b246777b0971851fc994bffb00a9cc72bf04da7c4e` | unchanged at baseline capture |
| `common/scripted_effects/012_africa_world_order_effects.txt` | `2035e3f7c33f3cfe4b265712cae708d18706d74724dc76ee8cbdf92efac5e41c` | unchanged at baseline capture |
| `events/012_african_union.txt` | `c3e0390e6a5a6193d6fc04defdccb6e0267b36c66734e78d5221de7eceee288d` | unchanged at baseline capture |
| `common/decisions/012_africa_gods_decisions.txt` | `03e124a014d54d59539db8e4bdf4693d3f071df79207d50f05751978fa715fd5` | unchanged at baseline capture |
| `common/script_constants/012_africa_gods_constants.txt` | `be9f4d3cd489b86d6dca14b213d8d02fd48b42020228dd209f0f8098a14d563e` | unchanged at baseline capture |

I independently rechecked the parent-reported intermediate hashes for the three changed files and verified the saved before copies match the before-byte hashes. The parent's later typed-World change supersedes the intermediate epoch-trigger hash above; no final hash is claimed yet.

## MCP baseline and scenario set

The required baseline `hoi4.probability_inspect` ran first on the exact decision source with `adapter=decision_ai_will_do` and `refresh=false`. It returned `PROBABILITY_SOURCE_INSPECTED`, workspace `mod_chaos_redux_ea3b2d67c2c0`, 46 indexed candidates, required inputs `has_war`, `scope.FROM`, `scope.any_of_scopes`, and `variable.global.chaos_meter_value`, `poolComplete=false`, source hash `bab09cc57f2110f434894d6e46f1a78aaaaf6ce82746219944d9ff751a0d0ff5`, and source revision `5534074a3d8661c478e5484bb3ff6273a5c825fcce3882e92c186730020c8a2d`. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b00803d589c054c3de18b68aa7e29d4ef9b27cfc1fe92f331ff52dcde5d5c27d/40bdffc70c687a350233daffac657b13facdda2f6e2feabea5badde1059ee0e9/probability-inspect-bab09cc57f21.json`.

The saved scenario set is `012-GODS-ACTIVATION-ELIGIBILITY-2026-10-06`, hash `2ded6efe59930a96a50f2a69aabc8b1b61fdd18706dfdaafc0cc100035d91e96`. It contains the four parent-named scenarios. All use actor fixture `AFR`, `has_war=false`, `variable.global.chaos_meter_value=0`, and the declared Africa Is One/Evolution I flags; the scenario state is a declared fixture rather than observed campaign state.

| Scenario ID | Declared activation state | Completeness limit |
| --- | --- | --- |
| `INITIAL_UNIFICATION_UNSETTLED` | `africa_continental_settlement_complete=true`, Scramble phase `0`, no settled or defeat flag | Participant and host scopes, event target, authority variables, and active-decision context were not bound. |
| `FINAL_SUCCESS` | Scramble phase `5`, settled flag true, defeat flag false, initial settlement flag false | Same decision scopes and authority inputs remain absent. |
| `FINAL_DEFEAT` | Scramble phase `5`, settled flag true, defeat flag true, initial settlement flag false | Same decision scopes and authority inputs remain absent. |
| `LOST_CAPITAL` | Initial-state flags and phase as above, with the intended capital-loss case | Capital state ID, owner, and controller were not supplied; this is not a complete capital-loss fixture. |

The single baseline `hoi4.probability_evaluate` requested the eight named participant/doctrine candidates and `raw_value`, `ranking`, and `unresolved` outputs. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-e8e4c7c626fb350f6c52e89c`, source revision `5534074a3d8661c478e5484bb3ff6273a5c825fcce3882e92c186730020c8a2d`, MCP source hash `bab09cc57f2110f434894d6e46f1a78aaaaf6ce82746219944d9ff751a0d0ff5`, and the saved scenario hash above. The adapter summarized 32 candidates, 12 eligible, 20 excluded, 716 unresolved trace records, and zero unresolved candidates. It returned no normalized probability, complete selection race, rank-reversal, or exact click result. Its authoritative JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5bdba4d9b2ff62622df6f5d36275d89f5799161404cda677ab67367201eaa5e5/5348d064432378c988a0b13fd03ee888a583b2c5f069d100e776e48755544f9d/probability-e8e4c7c626fb350f6c52e89c.json`.

The explicit baseline `hoi4.probability_render` used the same analysis ID and scenario hash and returned a ranking SVG at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a4bd854679cbe273db2999f63b7f6ff4042f955d73f2e314c33dbff8f6537da1/1c83b266d7b1530890e218c8defe86e772875cab08a023c26cc98598b9c14c11/probability-probability-e8e4c7c626fb350f6c52e89c-ranking.svg` and unresolved SVG at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27f7513f6f8fa75d8df80e0f2b9e05c8c8222fee23a61f0f564fe1c419a2fb51/6c513843b325b7ee2a154683a5dcfdd28f5ea207946007c85c30340bca4ce690/probability-probability-e8e4c7c626fb350f6c52e89c-unresolved.svg`.

## Weight traces and limitations

The MCP source inspection identifies the required global and target inputs, while the four fixtures do not bind participant `FROM`, a complete `gods_of_africa_participants` scope pool, a live Africa host event target, capital control, or the authority owner variables. The analyzer reported 716 unresolved records; its compact result did not expose numeric base and modifier traces for all eight requested choices. The JSON artifact preserves the detailed trace evidence, but this report makes no unsupported candidate score claims.

The returned diagnostics included the reciprocal/exaction/ambiguity doctrine candidates and participant response modifiers, with the exaction war factor and high-Chaos ambiguity factor unsatisfied across the declared four scenarios. Those findings describe the fixture values (`has_war=false`, Chaos `0`) and do not establish actual campaign starvation. The previous takeover handoff also records the unresolved `scope.any_of_scopes` and payment-helper limits for these decision families; its previous scenario analyses are supporting context, not replacements for this four-case baseline.

The five participant intents are not the full live participant decision race; related direct compliance, partial compliance, substitute-slot, return, defensive, and reconciliation decisions have different visibility phases and scope requirements. The three doctrine decisions are a separate host-category surface. The adapter is score-only, so neither raw willingness values nor incomplete rankings are click probabilities. No dominance, starvation, rank reversal, repetition, or exploit conclusion is established by this partial scenario pass.

The parent patch makes no AI weight change, so there is no AI tuning recommendation. The source-level repair should preserve the existing successful settled Scramble endpoint, distinguish defeat from success, retain the reviewed typed-World endpoint, and reuse the canonical idempotent initializer at both the normal milestone and AfricaIsOne setup boundaries. Those source changes are parent-owned; this report does not apply them.

## Intermediate post-change MCP pass (superseded)

Before the parent identified the typed-World endpoint, one post-change inspect/evaluate/render and one compare attempt ran against intermediate epoch-trigger SHA `6b0a22c6f03f5ca5bf78b6b00e10014513036fded63a1da97b6aafa66c23d68c`. The intermediate inspect kept the decision source MCP hash unchanged at `bab09cc57f2110f434894d6e46f1a78aaaaf6ce82746219944d9ff751a0d0ff5` and reported source revision `2292bf6aebb1b41dc0afebc6a05536167b0037fec9794e8141c2b651c1f328f6`.

The intermediate evaluate reused the same scenario hash and reported the same aggregate counts as baseline: 32 candidates, 12 eligible, 20 excluded, and 716 unresolved records. This is intermediate tool output only and does not prove a zero change or compare dependency behavior. Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9cd9be4ceb7c05a2d0ec8fec83a8967d4929f3254539a72425d0bffc49f1a072/abdac7019f416db28fdf099f8aacd27fc77b6849b34e7898ee5cd476d041132b/probability-cf4e80b5aa53760d66d0d8ab.json`; the intermediate ranking SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e338a3ff9c22af58580e649e8fa45413474d35f46faa24b64c56c6a6076ee0d/1a6937f0ed78609f40d5b1fcde2298f151ecb820059fa0e55dd5c7ff6b6436ae/probability-probability-cf4e80b5aa53760d66d0d8ab-ranking.svg`; the intermediate unresolved SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27f7513f6f8fa75d8df80e0f2b9e05c8c8222fee23a61f0f564fe1c419a2fb51/74fddf756712bc52271922b6be74c919511b9692fdc523774f5dbb8ce58b05e9/probability-probability-cf4e80b5aa53760d66d0d8ab-unresolved.svg`.

The intermediate `hoi4.probability_compare` used the exact before snapshot of `012_africa_gods_epoch_binding_triggers.txt` and that intermediate current source, with the same four scenarios and eight candidate IDs. It returned `PROBABILITY_SURFACE_EMPTY`, no artifacts, and blocker `No weighted blocks matched this request`, because the changed file contains a scripted trigger rather than decision `ai_will_do` blocks. This is the expected adapter boundary, not a numeric zero delta. A final compare and final after evaluation remain pending the parent's final typed-World helper hash.

## Documentation and skipped analyses

The named parent handoff `takeover_probability_2026-10-06.md` was read. It records the relevant offline wiki references: AI modding, lines 26-37, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`; Decision modding, lines 357-374, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`; and installed decision documentation, lines 1-46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`. These references distinguish decision AI willingness scores from normalized probabilities and document the relevant decision surface. They are reused from the named prior MCP handoff rather than newly queried here.

Skills read: `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and the named parent probability handoff. The MTTH skill was read because the task prompt required it; this repair has no MTTH-backed AI surface.

`probability_sweep` was skipped because the patch changes eligibility gates and call chronology without changing a numeric weight or threshold target. `probability_simulate` was skipped because no uncertain-input distribution was declared. `probability_sequence` was skipped because this is not a declared custom weighted pool with cadence and terminal transitions. Event-option, MTTH, focus-selection, technology/doctrine-selection, AI-strategy, and random-list adapters are outside this weighted scope. Event/focus structural inspect and render were skipped because the owner changed scripted caller/gate definitions only; no event option/chain definition or focus tree selection surface was changed in this AI-weight audit.

No Git commit was made; the parent owns integration and the final commit for the shared change.

## Final after evidence

Pending the parent's final helper hash and the final same-scenario MCP inspect/evaluate/compare pass.

