# Event26 native composition audit

2026-10-03. Read-only Strategy A audit against original full Part3/4.
Native completion is unresolved in all eleven requested families.
Source evidence establishes additive composition counterexamples.
Native final quantization and several consumer mappings remain unproved.

## Contract and source finding

Acceptance basis is the original user decision supplied by the parent.
Black Friday multiplies the ordinary current cost after ordinary modifiers, rounds positive results upward to at least one registered quantum, and preserves ordinary zero.
Part3:28–40,42–65,71–77 states this contract.
Part4:46–54 requires verified native composition, and 96–112 requires a confirmed quantum per consumer.

Exact Windows roots:

- M = `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`
- V = `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`

| Citation alias | Exact file under M/V |
| --- | --- |
| Part3 | `M\docs\specs\026_black_friday_specs\026_black_friday_spec_part_3_reusable_cost_modifier_architecture.md` |
| Part4 | `M\docs\specs\026_black_friday_specs\026_black_friday_spec_part_4_cost_surface_coverage.md` |
| I | `M\common\ideas\026_black_friday_ideas.txt` |
| D | `M\common\dynamic_modifiers\026_black_friday_dynamic_modifiers.txt` |
| R | `M\docs\plans\026_black_friday_plans\event26_cost_surface_registry.md` |
| W | `M\paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md` |
| IM | `M\paradox_wiki\Idea modding - Hearts of Iron 4 Wiki.md` |
| MD | `V\documentation\modifiers_documentation.md` |
| Def | `V\common\defines\00_defines.lua` |

W:57–59 says contributions add to a modifier's scope total, including contributions from different blocks.
W:1284–1288 identifies multiplicative exceptions such as consumer goods.
The listed percentage cost factors are not documented as separate multiplicative sale sources.
I:8–9 provides fixed `-0.5/-0.75` contributions, and D does the same for design and leader fields.
`M\common\scripted_effects\026_black_friday_effects.txt:1830–1853` installs these country/leader modifiers without ordinary-total compensation or a native final payment quantizer.
Ordinary modifiers entering the same additive percentage total therefore fail the accepted multiplication order.
Different modifier layers, scope delivery, engine clamps, and final debits remain unresolved.

| Source-model case | Required payment, quantum 1 | Additive result before engine quantization |
| --- | ---: | ---: |
| Base 100, ordinary -20%, sale -50% | 40 | 30 |
| Base 100, ordinary +25%, sale -50% | 63 | 75 |
| Base 100, ordinary -20%, sale -75% | 20 | 5 |
| Base 100, ordinary +25%, sale -75% | 32 | 50 |
| Promotion base 40, ordinary -50%, sale -50% | 10 | 0 |

These are documented arithmetic counterexamples, not observed game payments.
Installed ordinary precedents are `all_india_muslim_league_leader` at `V\common\country_leader\goe_traits.txt:194–201` with advisor -20%, `underage_monarch` at `V\common\country_leader\00_traits.txt:81–89` with advisor/laws +25%, and `politically_connected` at `V\common\unit_leader\00_traits.txt:154–161` with promotion -50%.
Promotion base 40 is Def:1146 and the sale contribution is D:687.
A nonnegative clamp alone does not establish the required promotion payment of 10.

Native rounding is unresolved throughout.
Ordinary 1/3/101 with quantum 1 must become 1/2/51 at baseline and 1/1/26 in Evolution I.
Ordinary zero stays zero.
MD's “Number with … decimal places” describes modifier presentation and does not prove final payment precision, ceiling, or minimum.
R's “Engine quantum” supplies no such evidence.

## Native-family matrix

Every row is unresolved for native completion.
“Mismatch” means documented same-token additive composition fails the contract, without claiming an observed debit.

| Family and exact BF IDs | Sale source | Actual price consumer and exact source evidence | Finding |
| --- | --- | --- | --- |
| Advisor: `BF-NAT-002/019/020` | I:18,27–29,73,82–84: `political_advisor_cost_factor` and `army/navy/air_advisor_cost_factor` | Native character/idea-slot appointment PP from advisor `cost` or slot default. IM:354–360,477–485, W:511–514, MD:1296–1303,1512–1515,1757–1760,4008–4011. `V\common\idea_tags\00_idea.txt:26–38` sets government default 150. | Mismatch. Slot/ledger combination and final PP debit unresolved. A nested `add_advisor_role` price is not proof of payment at that effect. `M\common\scripted_effects\016_brilliant_scientist_effects.txt:2959–2968` even declares zero. BF-NAT-020 needs its later appointment consumer. |
| Laws: `BF-NAT-003` | I:24–26,79–81: `economy_cost_factor`, `mobilization_laws_cost_factor`, `trade_laws_cost_factor` | Native law-change PP, including level transitions. IM:354–360,477–485, MD:1296–1303 and `V\common\idea_tags\00_idea.txt:26–38`. | Mismatch, with installed +25% precedent. Multi-level order, zero transitions, and final PP ceiling unresolved. |
| Doctrine: `BF-NAT-005` | I:31–34,86–89: `land/naval/air_doctrine_cost_factor` and `special_forces_doctrine_cost_factor` | Current grand-doctrine XP activation. `V\common\doctrines\grand_doctrines\_documentation.md:1–20` describes activation/`xp_cost/xp_type`. `V\common\doctrines\grand_doctrines\land_grand_doctrines.txt:1–12` declares `new_mobile_warfare` at 100 army XP. MD:1562–1565,3012–3015,3793–3796,4780–4783. | Mismatch where the factor reaches the consumer. Current grand-doctrine/special-forces mapping and XP quantization unresolved. `V\common\ideas\finland.txt:1096–1101` supplies ordinary -25% doctrine/ability factors. |
| Staff/command: `BF-NAT-004` and command part of `BF-NAT-018` | I:19–23,30,74–78,85: `high_command_cost_factor`, `army/navy/air_chief_cost_factor`, `theorist_cost_factor`, `command_abilities_cost_factor` | Staff PP: `V\common\idea_tags\00_idea.txt:40–65`. Ability CP: `force_attack` and `cost = 0.22` at `V\common\abilities\generic_leader_abilities.txt:1–8,54–55`. MD:1296–1303,2237–2240, W:849. | Mismatch. Ability scaling into CP, country/leader layers, and final CP ceiling/minimum unresolved. |
| Medal: `BF-NAT-013` | I:56,111: `grant_medal_cost_factor` | Medal CP confirmation: `V\common\unit_medals\00_default.txt:28–43` sets base 30. Def:815 supplies additional factor per active medal. MD:2862–2865, W:904. | Same-token mismatch. Escalation's relation to the sale factor and final CP quantization unresolved. No exact escalation debit is claimed. |
| Leader: `BF-NAT-015` and overlapping conversion in `BF-NAT-004` | D:683–689,1359–1365: `army/navy/military_leader_cost_factor`, `promote_cost_factor`, `unit_leader_as_advisor_cp_cost_factor`. I:54,109 also installs the last field on countries. | Recruitment CP: Def:726–729, with count and cap before modifiers. Promotion: Def:1146. Conversion: W:514, MD:5095–5098. Leader metadata: MD:1897–1900,3405–3408,4088–4091,4507–4510. | Concrete promotion mismatch. Recruitment scope unresolved: Event26 attaches fields to existing leaders, while `V\common\ideas\army_spirits.txt:120–124` supplies a country idea factor. Country/leader conversion overlap and clamps unresolved. Current defines specify recruitment CP despite W:889/895/898 saying PP. |
| Design: `BF-DES-001/002/003` | D:15–681,691–1357. Examples: `infantry_equipment_design_cost_factor` 75/751, `module_tank_gasoline_engine_design_cost_factor` 478/1154, `unit_infantry_design_cost_factor` 598/1274. | Variant/module/template XP. W:857–859, MD:1280–1286,3715–3721,5087–5093. Def:880–882,1120–1125 supplies template/upgrade bases. `V\common\units\equipment\modules\00_tank_modules.txt:142,160,171,178` declares module XP. | Same-token mismatch. Equipment/module overlap, multiple components, DLC consumer mapping, and per-component versus final rounding unresolved. A 664-key inventory does not prove payment. `BF-NAT-007/BF-ABS-007` remain distinct legacy upgrade-price claims. |
| MIO: `BF-ABS-002/004` | Absent from I/D: `military_industrial_organization_design_team_assign_cost`, `military_industrial_organization_design_team_change_cost`, `military_industrial_organization_industrial_manufacturer_assign_cost`, `military_industrial_organization_policy_cost`. | Assignment PP/day and design-change XP are separate at Def:4448–4454. Policy `cost`: `V\common\military_industrial_organization\policies\_documentation.md:23–24`. MIO modifier examples: 63–73. MD:3360–3388 lists fields without formulas. | No native sale adapter. Default assignment upkeep is excluded by Part4:23–38 and default design-change fee is zero. Policy/qualifying fees are unimplemented/unresolved. Absolute-field/D claims exceed evidence: country trait reductions exist at `V\common\country_leader\00_traits.txt:13138–13140`. The cited `V\common\dynamic_modifiers\wuw_dynamic_modifiers.txt:462–492` has MIO funds/research, not these four cost fields. |
| License: `BF-NAT-011/BF-ABS-010` | I:60–63,115–118: `license_anti_tank_eq_cost_factor`, `license_artillery_eq_cost_factor`, `license_infantry_eq_cost_factor`, `license_light_tank_eq_cost_factor`. Six `license_*_purchase_cost` fields are absent. | Native license civilian-industry price: Def:659–660. W:622–624 describes percentage purchase costs. MD:3052–3145 lists distinct fields. `V\common\ideas\netherlands.txt:755–758` supplies ordinary -100% infantry/artillery factors. | Same-token mismatch and zero preservation unresolved. Four factors do not prove all purchase categories. R's absolute classification conflicts with W's percentage descriptions, and MD precision does not settle it. Distinguish commitment from excluded production work. Factory rounding unresolved. |
| Trade: trade part of `BF-NAT-010` | I:64–65,119–120: `trade_cost_for_target_factor`, `overlord_trade_cost_factor` | Targeted trade relation and overlord/subject factory price: W:1161,596, MD:5029–5032,4313–4316. `V\common\ideas\australia.txt:610–615` uses `targeted_modifier/tag`. `V\common\autonomous_states\puppet.txt:21–25` supplies ordinary -90% overlord factor. | Same-token mismatch if the sale reaches that relation. Event26 puts the targeted field in an ordinary country block without a target binding, leaving payer/seller delivery unresolved. Integer commitment, minimum one, and commitment/upkeep classification unresolved. |
| Autonomy/peace: autonomy/peace part of `BF-NAT-018` | I:57–59,112–114: `annex_subject_cost_factor`, `annex_cost_factor`, `puppet_cost_factor` | Subject level-change/annex/free PP: Def:223–225. The latter two fields concern peace costs, MD:1742–1750,4517–4520 and W:561–562. | Subject-annex same-token mismatch. General level-change/freeing coverage unproved. Deprecated peace fields prove neither PP consumer. `V\common\peace_conference\cost_modifiers\_documentation.md:18–38` documents multiplicative `cost_multiplier` instead. That route is absent here and final score rounding unresolved. |

## Disposition and owner actions

Original Part3/4 remains accepted and unchanged.
Native composition is incomplete.
No acceptance basis authorizes additive discounting, fractional substitutes for registered ceiling payments, or weaker replacement actions.

The initial audit read found `covered_native`.
During this audit the parent independently changed the 14 relevant A rows at R:49–67,228–230 to `source_native_modifier_pending_composition_rounding_live` and added its native-proof boundary at R:40–44.
That pending-evidence disposition is appropriate.
I/D remained unchanged.
`M\docs\plans\026_black_friday_plans\event26_design_modifier_inventory.md:684` still overstates composition from field presence.
R:227,232,234,283–294 retains license/MIO classification and stale precedent gaps.

Affected A IDs are `BF-NAT-002/003/004/005/010/011/013/015/018/019/020` and `BF-DES-001/002/003`.
Applicable same-token components fail the documented composition test.
Unresolved mapping/scope components are distinguished in the matrix.
This does not claim every field reaches every consumer.

For a verified `base × (1 + ordinary_total)` consumer, multiplying by the sale ratio would require a contribution mathematically equal to `(ratio - 1) × (1 + ordinary_total)`.
This is a requirement, not an approved implementation recipe.
The owner still needs exact scope, other price layers, refresh, zero handling, and final quantization evidence.
Use verified A, exact B, or complete C only where the actual action, ordinary current modifiers, UI, affordability, and debit remain correct.
Otherwise retain unresolved status until a precise D limitation is supported.
The installed peace `cost_multiplier` is a documented native route to investigate for peace actions only, without proving its rounding or authorizing a design change.

## Mandatory MCP and validation limits

Live metadata exposes the required routes.
Final calls using `workspaceId = mod_chaos_redux_ea3b2d67c2c0` returned no terminal result within 60,000 ms client deadlines.

| Route | Exact bounded request |
| --- | --- |
| `hoi4.reference_context` | idea, limit 3, native stacking/rounding question |
| `hoi4.reference_search` | `political_advisor_cost_factor`, limit 2 |
| `hoi4.source_lookup` | `black_friday_sale`, maxDefinitions 1, maxLines 25, includeReferences false |
| `hoi4.event_inspect` | trace, selector `{ kind: "event", eventId: "chaosx.nr26.1" }`, maxDepth 1, maxNodes 4 |
| `hoi4.event_render` | overview, same selector/bounds |
| `hoi4.event_compare` | same selector, render false, maxChainNodes 4, before revision `9a7c9c23f5d02569f7457fa868eaecdea03c47f77dc3652d62c24492f5e65755` |

The historical baseline revision comes from `M\docs\plans\026_black_friday_plans\subagent_handoffs\completion_final_audit_current.md:99–103`.
Current cache availability was not established.
No current artifact URI, server revision, source-lookup override result, graph, render, or comparison was delivered.
A valid revision-bound `hoi4.reference_read` is blocked upstream because context/search returned no reference ID/revision.
An unresolved-revision probe is not counted as a valid documentation read.
Early selector validation errors were corrected before final attempts.
Client deadlines establish retrieval limits, not service health or engine behavior.
Local citations/hashes do not substitute for MCP or native payment evidence.

Performed: original contract/source comparison, installation-scope review, installed ordinary-modifier precedents, native price declarations/defines, registry consumer cross-check, and the arithmetic counterexamples above.
Missing: exact price factor order, displayed/affordable/paid parity, quantum/ceiling, positive minimum, ordinary zero, scope delivery, and native before/after evidence per consumer.
AI weights/probabilities are outside this deterministic price assignment and remain with the parent's `chaosx_ai_probability_auditor`.

Only this handoff was written.
Gameplay, registry, design, enablement, and other agents' files were not edited.
No game was launched and no logs were sought.
Skills used: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`.
No asset, GUI, 3D, or skill surface was changed.
No entire-goal audit was performed.

## Source revision identities

HEAD read during audit: `a34261fe4cb4575c27b54dad6eb103941364409f`.
The shared tree is not frozen.
These locally computed SHA-256 values bind audited bytes and are not MCP-issued revisions.
Executable FileVersion/ProductVersion both read `1.0`, which does not verify R's advertised game build.
The binary hash identifies the installation without claiming executed engine evidence.

| Exact file under M/V | SHA-256 |
| --- | --- |
| `M\AGENTS.md` | `38e479cb75828ba888860be8bc3739f9286c0d925cc7d8de5ecd3b8dadec46cf` |
| `M\docs\specs\026_black_friday_specs\026_black_friday_spec_part_3_reusable_cost_modifier_architecture.md` | `a852ddae45a49c835b98d0a34998e098f816089bf87fdf64cd5c2f53e94eeb58` |
| `M\docs\specs\026_black_friday_specs\026_black_friday_spec_part_4_cost_surface_coverage.md` | `4df7cca604040bfb5da9c3373de95960b72dc54b5c89b23f25938bfce79589a3` |
| `M\common\ideas\026_black_friday_ideas.txt` | `dd2adb0a5956b3bc747a0527cae21f22448dbd81e7bb30fb6598a468dc459fb3` |
| `M\common\dynamic_modifiers\026_black_friday_dynamic_modifiers.txt` | `a5aa4b5599370d9754ca84988efe443f80b1658221b1c5fc0f6f8b9bd94b7104` |
| `M\common\scripted_effects\026_black_friday_effects.txt` | `a7e0201e52f19d573746158fb7d691d8046cf208caac625bfc6335ffde73112a` |
| `M\docs\plans\026_black_friday_plans\event26_cost_surface_registry.md` | `a239f625a0f83266be3acb3cb4b219d882e05d9e939833e3873015b37b9ec23e` |
| `M\docs\plans\026_black_friday_plans\event26_design_modifier_inventory.md` | `467ccd5171e622f4514f78c86bd8d52ad8efa906b06905e18795c7ed8bca071b` |
| `M\paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md` | `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f` |
| `M\paradox_wiki\Idea modding - Hearts of Iron 4 Wiki.md` | `a6405eb98a02a9de4689b7c0ef80b5a887b6c6c747d3907f68c109ed3fd099ac` |
| `M\common\scripted_effects\016_brilliant_scientist_effects.txt` | `7dc6686137643177045b8fc278078e3be349ce113d2520b9add8d21b11c4f447` |
| `M\docs\plans\026_black_friday_plans\subagent_handoffs\completion_final_audit_current.md` | `65964f52ab3de0877233615ded62e6c03d531dbe1e29ce4870b40d0a3119e080` |
| `V\hoi4.exe` | `870ebf1f615262facca48a3b947775c41f0a5338f3068c40958209f5c41c65ad` |
| `V\documentation\modifiers_documentation.md` | `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e` |
| `V\common\defines\00_defines.lua` | `405a24ce579815443cafe052cff1361e20c712ca8182e3f10ccbf45330dd4be4` |
| `V\common\country_leader\00_traits.txt` | `b629d44fde5fa93d176a1db04bdac83c53e51f55dd789359dca7a96ab4d25dc5` |
| `V\common\country_leader\goe_traits.txt` | `842f16bdc1153ebd5278afa039643490149d2bc763f865e67b60034059b9d4b3` |
| `V\common\unit_leader\00_traits.txt` | `249ce6ee645cbd0270a8834ddc251c1f53ac981c979ac2a7c1852f929d850035` |
| `V\common\idea_tags\00_idea.txt` | `59de89c2407405d7ed6854332c92ac0961948d1d2246f60c0b81e7d0e82e1863` |
| `V\common\abilities\generic_leader_abilities.txt` | `7da51338083808ee1a84d4b1e57c1929470bdbf583003bd085e99a0a2b0e9028` |
| `V\common\unit_medals\00_default.txt` | `ac8f6fd131ade8fbb3752541119d154c0b770be71b1877f672b3f206e5275325` |
| `V\common\autonomous_states\puppet.txt` | `79d3b1c2986a1c6b8d8a1a9bc65f7b46b121412c1ece0da82e5f2955d5f0eb81` |
| `V\common\doctrines\grand_doctrines\_documentation.md` | `5ff029facf7fa8e8139d3ee33209329483f241e0241b0b568f687ca4ac2b43f0` |
| `V\common\doctrines\grand_doctrines\land_grand_doctrines.txt` | `cd81a877366c582f096422320cd7fcf9fb259afcc8d45d3dbb887b37792b329d` |
| `V\common\military_industrial_organization\policies\_documentation.md` | `5c8853bd9568e3d77d7f2e8dffce529602b0a18c2e6a3e65583f72cf611cc440` |
| `V\common\peace_conference\cost_modifiers\_documentation.md` | `feeda5d05fc51bf7c58653cd0a3440826960abeddd74148134072530ffb4814d` |
| `V\common\ideas\finland.txt` | `9e9cc6599d73c77aefb80417c84137397cc7577fc37758c5c64679eba367d184` |
| `V\common\ideas\netherlands.txt` | `98ce4a03b53fe6dd37f8469bdd2bf5d4528fca912f035fb7de7f57eb3aa2de51` |
| `V\common\ideas\australia.txt` | `aedd76ab9adac1816441a4d7d00f49793a425dc258ef177a98522d8170d5a3b2` |
| `V\common\ideas\army_spirits.txt` | `932c983b6ff7cf3a221bb4b7399ff1f1ff9fdf3f4ca52e83e13ed47fd64fb512` |
| `V\common\units\equipment\modules\00_tank_modules.txt` | `f9cfc13af9ffd13133d9ad6afdcc1714ba159dc5f94119fff23068efb43e9591` |
| `V\common\dynamic_modifiers\wuw_dynamic_modifiers.txt` | `2a03bfa939115db4c2b0720466f287927925e9e36b939c574bfb6ce3ad832db3` |
