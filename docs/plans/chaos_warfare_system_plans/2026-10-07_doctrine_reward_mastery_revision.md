# Chaos Warfare reward concentration and mastery coverage

Disposition: proposal reviewed; selected allocation is accepted and implemented in source in [2026-10-07_doctrine_reward_mastery_implementation.md](2026-10-07_doctrine_reward_mastery_implementation.md).
The selected version uses the fifteen-percent mastery III/four-percent technology allocation, role lists, the three other reward concentrations, Projector-only organization and the conservative 6.5-percent Projector breakthrough tiers.
Other illustrative allocations and historical source tables below remain proposal/baseline evidence, not current implemented values.
The parent assigned a read-only architecture and budget proposal after the user rejected the weak individual doctrine rewards and narrow mastery rosters.
The accepted specialization purposes and combined ceilings come from `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md:19-55`.
This document implements no gameplay, localisation, graphics, skill, workbook, index, or permission changes.

## Findings that explain the complaint

Infantry adoption grants only 3% breakthrough to `category_cbrn_assault_battalions`, whose retained member is `chaos_battalion`.
That unit is inactive until the existing infantry mastery III technology grant, so the adoption stat cannot benefit the normal initial protected formation.
The current direct breakthrough reward is divided between adoption 3%, mastery IV 3%, mastery V category 4%, and mastery V Battalion-specific 5%.
The separate 1942 technology supplies another 15% breakthrough.
The doctrine therefore has 15 percentage points of authored lifetime breakthrough reward, with little visible payoff at any single step.

`cbrn_mask_discipline_unlocked`, `cbrn_contaminated_terrain_movement_unlocked`, and `cbrn_shock_exploitation_unlocked` each have only their set call in current `common/**/*.txt` literal references.
They must not be advertised as an independent mask, movement, or exploitation capability.
The actual milestone recorders and their technology prerequisites remain the source of concrete unlocks.

Mastery is currently restricted by authored explicit `sub_units` lists of three, three, two, and three entries.
Installed documentation supports `sub_units`, `categories`, and `equipment` filters and describes the multiplier as scaling contributing manpower.
It specifies no three-type cap.
Field Medical Support and Biosecurity Assault are absent from every current list despite having real manpower, equipment, training, and supply requirements.

## Minimal reward recommendation

Concentrate existing lifetime allowances into an immediate protection benefit and larger named specialist payoffs.
Keep every reward identifier, recorder, unlock, threshold, XP cost, mastery multiplier, AI coefficient, and permission check unchanged.
No new administrative layer, weapon authorization, recurring hook, or paid training action is needed.

| Track | Concrete patch proposal | Removed scattered grants | Lifetime change |
| --- | --- | --- | --- |
| Protected assault adoption | Move the existing 10% primary-protection reliability grant from mastery I into adoption | Adoption assault breakthrough 3% moves into mastery III | Same reliability and breakthrough totals |
| Protected assault mastery III | Grant 10% breakthrough to `category_cbrn_assault_battalions` alongside the existing Chaos Battalion unlock | Remove adoption 3%, mastery IV 3%, and mastery V category 4% | Same category total of 10% |
| Protected assault mastery V | Retain Battalion-specific 5% soft attack and 5% breakthrough and the terminal-operation unlock | None | Same late specialist payout |
| Armored delivery adoption | Consolidate armored delivery breakthrough into one 5% grant | Remove mastery IV 3% after combining adoption 2% | Same total of 5% |
| Armored delivery mastery I | Consolidate that track's three armored reliability grants into 15% | Remove mastery IV and V reliability grants of 5% each after combining mastery I 5% | Same track total of 15% |
| Fire-support adoption | Give line and support artillery one 9.5% soft-attack grant each | Remove line artillery mastery II 3% and IV 2.5%, and support artillery mastery I 2%, II 2%, and V 1.5%, combining their adoption 4% | Same 9.5% total per conventional category |
| Integrated command adoption | Consolidate the current national reconnaissance bonuses into 25% | Remove mastery I 10% and V 5% after combining adoption 10% | Same total of 25% |

The minimum first patch can be restricted to the two infantry relocations and mastery coverage.
The other three concentration rows are independent parent-reviewed extensions using existing allowances.
Existing capability milestones still provide the fire-control, delivery, decontamination, HQ, camp-method, persistent-distribution, and terminal-operation behavior owned by the shared pipeline.
The parent must align their descriptions with real current consumers rather than describe any inert compatibility flag as a mechanic.

An optional stronger single infantry payout is 15% breakthrough at mastery III with all four old breakthrough grants removed, including the Battalion-specific mastery V 5%.
It keeps the direct lifetime total unchanged and trades away the final breakthrough increment.
Use the 10% plus late 5% version when preserving the existing final reward identity matters.
Neither version is an authorization to raise the combined static ceiling.

## Combined budget evidence and limits

The older `subagent_handoffs/2026-09-20_doctrine_balance_handoff.md` provides a useful source inventory, but its flat technology grants and spirit figures are stale.
Current `common/technologies/chaosx_technologies.txt:50-66,207-219` gives fractional projector technology bonuses and Chaos Battalion breakthrough +15% with flat organization +11.
Current `common/ideas/cbw_spirits.txt:10-18,178-182` gives Terminal Hazard attack 2.5% and coordination 0.5%, and Hazard Assault Cadres affects Chaos Battalion attack and defense as well as the protection company.
Do not reuse the older handoff's 2.7 breakthrough, +12 organization, or gas-mask-only Cadres assertions as current proof.

| Metric | Current controlled source stack | Ceiling and effect of proposal |
| --- | --- | --- |
| Passive army attack | Infantry IV 1.5% + Terminal Hazard 2.5% = 4%. Protective HQ active postures have negative attack modifiers | 5%. Proposal adds zero |
| Passive army organization | Infantry I 1% + Operations V 1% + Controlled Retaliation 1% + Mask Discipline 1% + Biological Security Director 0.5% = conservative 4.5% allowance | 5%. Proposal adds zero |
| Planning speed | Grand 1% + Operations adoption 1% + Theater spirit 3% + Operations High Command genius 4% + Operations HQ 5% = 14% | 15%. Proposal adds zero |
| Coordination | Fire II/III 1% each + Armor II/V 1% each + Operations adoption/IV/V 1% each + Terminal 0.5% = 7.5% | 8%. Proposal adds zero |
| Reinforcement | Infantry II 1 percentage point + Operations II 1 percentage point = 2 percentage points | 2 percentage points. Proposal adds zero |
| Conventional artillery soft attack | Line doctrine 4+3+2.5 = 9.5%. Support doctrine 4+2+2+1.5 = 9.5%. Army attack supplies 4% | Doctrine cap 10%, full conventional cap 15%. Consolidation gives `1.095 * 1.04 = 1.1388`, below 1.15 even when the country attack layer multiplies the unit layer |
| Chaos Battalion direct breakthrough | Infantry category 3+3+4 = 10%, Battalion-specific 5%, technology 15% = 30 percentage points | Dedicated cap 35%. Both concentration options preserve exactly the same sources and direct total |
| Protection company reliability | Existing infantry mastery I 10% relocates to adoption. Projector, armor, HQ, and artillery reliability categories do not include this company | No increase in any reliability endpoint. Equipment-level spirit/designer modifiers remain separate current layers |
| Armored delivery breakthrough | Grand chemical 5% + fire adoption 5% + fire V 5% + armor adoption 2% + armor IV 3% = 20% unit-stat grants | Dedicated cap 35%. Consolidation preserves 20% before unchanged equipment, designer, and country layers |
| Armored delivery reliability | Armor I/IV/V 5% each + fire I offensive-delivery 5% + Operations II/III 5% each = 30% unit-stat grants | Proposal preserves 30%. Equipment archetype reliability grants remain separate and must not be counted as the same field |
| National reconnaissance | Operations adoption 10% + I 10% + V 5% = 25% | Proposal preserves 25%. Flat reconnaissance technology points and company base recon remain separate |
| Conditional hazard endpoints | No dose, casualty, contamination, duration, mitigation, cleanup, or permission factor changes | Combined 50% extra-benefit ceiling remains owned by existing endpoint clamps and the same-mask baseline correction |

The precise native accumulation of identical sub-unit and category stat grants is not established by the retrieved references.
The existing grants have identical lifetime sum before and after this proposal.
A deliberately pessimistic independent product of the old four infantry grants is `1.03 * 1.03 * 1.04 * 1.05 = 1.1585028`.
The recommended replacement is `1.10 * 1.05 = 1.155`, so concentration decreases even that pessimistic lifetime reward product.
The analogous old line-artillery product with army attack is `1.04 * 1.03 * 1.025 * 1.04 = 1.1418992`, above the replacement's 1.1388 but still below 1.15.

**Unresolved full-stack concern:** Cadres currently includes `modifier_army_sub_unit_chaos_battalion_defence_factor = 0.10`.
The offline modifier entry calls it a defense bonus but does not establish whether it also multiplies attacking breakthrough.
If it applies to breakthrough, the current direct +30% stack times Cadres 1.10 reaches 1.43, above the 1.35 ceiling even before this proposal.
If a separate conservative 4% attack-equivalent allowance is also reserved, `1.30 * 1.10 * 1.04 = 1.4872`.
The parent must establish this native semantic or explicitly reallocate the existing Cadres/technology/doctrine budget before claiming a full legal-stack pass.
No arbitrary increase to the 3% fragments is defensible while that concern remains unresolved.
Keeping the extra 10% defense layer under the pessimistic model permits at most `1.35 / 1.10 - 1.15 = 0.0772727` total doctrine breakthrough with the 15% technology grant.
That is an uncertainty bound rather than a recommended nerf or proven native formula.

The parent supplied a concrete alternative allocation for review: consolidate all 15 doctrine breakthrough points into mastery III, remove all four old doctrine grants, and reduce the hidden 1942 mastery V breakthrough technology from 15% to 5% while keeping its +11 organization.
It gives a 15% specialist unit-unlock payoff and a direct lifetime +20% breakthrough, with `1.20 * 1.10 = 1.32` under the pessimistic Cadres model.
The residual multiplicative room is `1.35 / 1.32 - 1 = 2.2727%`.
This is a parent-proposed reallocation with unchanged unlock chronology, not an accepted or implemented technology retune.

A fresh bounded source pass found no further direct CBRN native breakthrough modifier in `cbrn_high_command_traits.txt`, `cbrn_historical_advisor_traits.txt`, the four CBRN MIO organization files, `cbrn_historical_advisor_effects.txt`, or `cbrn_hq_effects.txt`.
The CBRN MIO native equipment grants concern reliability and cost rather than breakthrough, defense, or attack stats.
`protected_assault_expert` gives supply endurance and `theatre_containment_organizer` gives army-group capacity in `common/unit_leader/chaosx_traits.txt:69-88`.
However, `biological_operations_veteran` at lines 51-58 gives `defense_skill = 1`.
The offline `Character modding` snapshot at lines 256-262 lists +2.5% army defense per skill point and does not explicitly establish attacking breakthrough behavior.
If that extra CBRN-earned skill affects breakthrough and belongs in the same ceiling, `1.32 * 1.025 = 1.353`, marginally above 1.35.
An illustrative 4% mastery V technology increment instead of 5% gives `1.19 * 1.10 * 1.025 = 1.341725`.
That leaves approximately 0.617% multiplicative room and still needs the parent to verify the remaining native layers.
Neither illustrative technology reduction is an engine-validated full-stack result.
General infantry-equipment designers, conventional commander skill, and country bonuses remain the same baseline in a comparison of the CBRN-authored benefit and must not be silently removed from only one side.

The dedicated organization check also illustrates the scarcity of spare universal reward budget: `(40 + 11) / 40 * 1.045 = 1.332375` for Chaos Battalion.
The projector's existing flat 5 organization on base 18 gives `(18 + 5) / 18 * 1.045 = 1.3352778`.
Adding large organization bonuses to either unit would exhaust the 35% ceiling quickly.
Keeping the current specialist costs and delivering larger individual grants through relocation is the lowest-risk response to weak reward presentation.

## Exact mastery rosters

Use one explicit `sub_units` list per track and no simultaneous `categories` or `equipment` filter.
Every ID appears exactly once within its track.
This construction avoids relying on an undocumented native OR, AND, or duplicate-count rule for overlapping filters.
Cross-track overlap reflects the field company supporting two distinct training purposes and does not duplicate an entry within a track.

| Track | Proposed exact contributor list | Change and purpose |
| --- | --- | --- |
| Infantry | `cbrn_gas_mask_decon_detachment`, `cbrn_chemical_recon_detachment`, `cbrn_medical_countermeasure_detachment`, `cbrn_biosecurity_assault_detachment`, `chaos_battalion` | Add protected medical support and Biosecurity Assault. Five types cover protection, reconnaissance, recovery, biological clearing, and protected line assault |
| Combat support | `cbrn_chemical_projector_battery`, `cbrn_chemical_ammunition_train`, `cbrn_medical_countermeasure_detachment` | Add Field Medical Support to sustained fire-support recovery. Three types are a role choice, not an engine limit |
| Armor | `cbrn_light_armored_delivery_detachment`, `cbrn_medium_armored_delivery_detachment`, `cbrn_heavy_armored_delivery_detachment` | Retain all three actual armored delivery variants. Ordinary tanks do not carry the specialist equipment. Adding unrelated foot companies solely to increase the count would erase this training purpose |
| Operations | `cbrn_hq_operations_section`, `cbrn_hq_protective_logistics_section`, `cbrn_hq_medical_countermeasure_directorate`, `cbrn_gas_mask_decon_detachment`, `cbrn_chemical_recon_detachment`, `cbrn_medical_countermeasure_detachment` | Add the field protection, reconnaissance, and medical companies that carry out coordinated HQ work. Six types include the HQ roster and operational field evidence |

No category declarations or unit memberships need changing for this minimal roster patch.
Existing semantic categories remain the reward recipients.
The consolidated field roster has 13 retained unit types: ten regimental types including the three armored variants, plus three HQ types.
All 13 occur in at least one proposed track list, so coverage is complete for the retained roster without resurrecting the retired fifteen-role split.
Medical and Biosecurity Assault overlap in `category_cbrn_biosecurity_support`, so using that category alongside `category_cbrn_medical_support` would require native duplicate-match evidence that is presently absent.
An equipment filter on masks would additionally include delivery companies and every other equipment-bearing attachment across purposes.
The explicit rosters give a reviewable limit and avoid silently treating all ordinary infantry as protected training contributors.

## Pacing normalized against field formations

Keep existing multipliers infantry 12, combat support 16, armor 14, and operations 14, with reward threshold 100.
The examples below use authorized manpower at full strength and equal eligible training or combat activity.
They show only the contribution numerator, not calendar days, doctrine XP, combat frequency, engine caps, or an observed mastery rate.

| Formation's specialist components | Before weighted manpower | After weighted manpower | Meaning |
| --- | --- | --- | --- |
| Protection 320 + reconnaissance 220 + field medical 360 | `540 * 12 = 6480` | `900 * 12 = 10800` | Infantry contribution grows 66.7% because recovery staff count |
| Same plus Biosecurity Assault 420 | `540 * 12 = 6480` | `1320 * 12 = 15840` | Infantry contribution grows 144.4% while consuming a fourth support position and more equipment |
| Projector 320 + ammunition train 400 + field medical 360 | `720 * 16 = 11520` | `1080 * 16 = 17280` | Fire-support contribution grows 50% for sustained support |
| One armored delivery company 320 | `320 * 14 = 4480` | `320 * 14 = 4480` | Armored pacing stays unchanged |
| Protection HQ 600 + protection company 320 + reconnaissance 220 + field medical 360 | `600 * 14 = 8400` | `1500 * 14 = 21000` | Operations contribution grows 150% from a concrete HQ plus field-company package |
| One Chaos Battalion 1050 plus protection 320 and reconnaissance 220 | `1590 * 12 = 19080` | `1590 * 12 = 19080` | A previously counted assault formation keeps its existing rate |

Existing battalion and support-slot cost creates a natural pacing tradeoff.
The example with four regimental attachments does not exceed the ordinary five-slot budget, although any fifth support company has its own opportunity cost.
Adding a line Chaos Battalion uses its real width, manpower, training, equipment, and supply budget.
Do not reduce the shared multiplier to force the widened roster back to the old maximum, because that would slow previously eligible formations and penalize the new specialist roles.
Exact engine mastery pacing remains unresolved until the parent can obtain supported doctrine/scenario evidence.

## Constants, helper map, and lifecycle

| Source | Constants to update if the row is accepted |
| --- | --- |
| Infantry file-local values and `cbrn_doctrine_modifier` | Retire `infantry_adoption_breakthrough`, `infantry_m4_assault_breakthrough`, `infantry_m5_assault_breakthrough`. Add `infantry_adoption_protection_reliability = 0.10`, `infantry_m3_assault_breakthrough = 0.10`. Retire the old M1 reliability mirror after relocation. Battalion-specific M5 values remain 0.05 |
| Armor file-local values and matching shared mirror | `armor_adoption_breakthrough = 0.05`, `armor_m1_sealed_reliability = 0.15`. Remove the relocated IV breakthrough and IV/V reliability grant constants |
| Combat-support file-local values and shared mirrors | Both adoption conventional soft-attack constants become 0.095. Remove the five relocated reward soft-attack constants. Add complete shared mirrors for these surviving values rather than claiming the partial existing table is complete |
| Operations file-local values and shared mirror | Add `operations_adoption_recon = 0.25`. Remove the relocated M1 and M5 recon constants |

Native doctrine fields do not document general `constant:` support.
Preserve the installed-safe file-local `@` values as explicit mirrors of the shared tuning table.
Do not introduce a wrapper, generator, or runtime variable assignment solely to pass constants into database fields.
For the parent's alternative allocation, use `infantry_m3_assault_breakthrough = 0.15`, remove the Battalion-specific mastery V breakthrough row, and change `@CHAOS_ASSAULT_IMPROVED_BREAKTHROUGH` plus its authoritative shared mirror to the reviewed 0.05 or 0.04 value.
Its +11 organization row stays intact.
This extra technology call site must be included in the parent's meaningful budget and native bonus-coverage review.

| Existing helper family | Scope, inputs, outputs, side effects, and consumers |
| --- | --- |
| `cbrn_record_hazard_assault_adoption`, `cbrn_record_toxic_armored_adoption`, `cbrn_record_contaminant_fire_support_adoption`, `cbrn_record_integrated_command_adoption` | Country scope. No arguments. Existing active-track flags, bounded unit unlocks, and technology reconciliation. Called by the same four adoption effect blocks |
| `cbrn_record_infantry_mastery_*`, `cbrn_record_armor_mastery_*`, `cbrn_record_combat_support_mastery_*`, `cbrn_record_operations_mastery_*` | Country scope. No arguments. Existing mastery flags and capability grants. Called by the same named native rewards |
| `cbrn_grant_available_doctrine_technologies` | Country scope. Existing mastery, prerequisite technology, and permission state inputs. Idempotent mapped technology output. Existing milestone consumers remain unchanged |

No new reusable helper is justified because native stat reward blocks and mastery filters already express the required behavior directly.
`common/scripted_effects/chaosx_dynamic_effects.txt` and `.md` were inspected and contain no suitable native-mastery filter helper.
No new event target, temporary variable, persistent variable, flag, or cleanup hook is needed.
Preserve all existing milestone and policy lifecycle behavior.
Leave the three inert compatibility flags in place for this narrow patch, but correct descriptions that promise unsupported behavior.

## Migration, wording, and validation handoff

1. Parent chooses the minimal infantry patch or the additional concentration rows and records acceptance here or in the accepted spec.
2. Edit the owned doctrine reward blocks and `cbrn_doctrine_constants.txt` mirrors together, removing every relocated grant to prevent doubling.
3. Replace the exact mastery rosters above in the four current doctrine files.
4. Preserve all reward IDs, threshold/cost/AI values, recorders, hidden technology grants, payload requirements, first-use policy checks, and ordinary research availability.
5. Align `localisation/english/cbrn_doctrine_balance_l_english.yml`, affected descriptions in `chaosx_doctrines_l_english.yml`, and the owning doctrine documentation with the selected payout and actual contributors.
6. Preserve icon identities and reward-frame order. Parent owns the separately authorized main-icon restoration.

Suggested infantry adoption wording: "Protection companies keep their respirators, decontamination equipment, and transport serviceable during sustained field use."
Suggested mastery III wording: "Chaos Battalions advance under specialist protection and trained assault coordination. Their equipment and supply needs remain part of every formation."
Suggested mastery summary: "Protected assault, reconnaissance, field medical support, biosecurity assault, and Chaos Battalions contribute to this training."
Do not label a compatibility flag as terrain movement, mask consumption, or a national casualty reduction unless a real engine or pipeline consumer implements that effect.
Use native stat rows for exact numbers rather than putting an obsolete reward list into descriptive prose.

Task-specific source arithmetic above was evaluated directly from the controlled constants and compared with the accepted ceilings.
The retained manpower roster was checked against the current `cbrn_regimental_support.txt` and `cbrn_hq_support.txt` definitions.
Literal reference searches confirmed the three inert flags and the existing recorders.
No engine files or weighted AI logic were patched, so no post-patch probability result is claimed.
Any parent change to weights requires the normal read-only probability auditor baseline and same-scenario compare.

Meaningful pending checks are the Cadres breakthrough semantic and legal full stack, native mastery eligibility and progression, exact before/after lifetime grant totals, selected reward localisation, and preserved permission/unlock behavior.
Native `script_validate` checks country effects or triggers and cannot by itself establish native database mastery filter semantics.
No game was launched and no runtime behavior is claimed.
No simplification or fallback was implemented.
The proposal is incomplete as an engine-validated balance change because the inspection limitations below and Cadres concern remain unresolved.

## Reference and MCP evidence

- Live `hoi4.reference_context(surface=technology, limit=8)` returned both required source kinds, no missing required files, and no omitted source kind. It identifies sources rather than proving their detailed rules were read.
- `hoi4.reference_read` read installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\doctrines\subdoctrines\_documentation.md:8-58`, revision `81dcc8e9565e16050c269220c7a706ec894bb5b22712ecabfcb598e1fb671df0`. Lines 47-56 provide multiplier and the three supported filter forms.
- Offline `paradox_wiki\Doctrine modding - Hearts of Iron 4 Wiki.md:19-56` was read locally after the live search/read identification, revision `125456f6380fac4ebe0b04cfa8c9fab9bbd26d8db54ec08fe697e31a9641c3ee`. The snapshot provides file structure and doctrine trigger/effect names, but its subdoctrine section is empty and does not settle mastery union semantics.
- `hoi4.reference_read` read offline `paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md:945-954`, revision `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f`. The sub-unit defense modifier description does not specify attacking breakthrough.
- Installed `common\doctrines\grand_doctrines\_documentation.md:48-84` was read locally for native country modifiers and unit-stat reward structure. Installed vanilla `common\doctrines\subdoctrines\land\infantry_subdoctrines.txt:384-402` provides `mounted_infantry` with a category-filter mastery override.
- Installed `documentation\script_concept_documentation.md:216-232` and `common\script_constants\documentation.md:1-31` were read locally. Both limit shared tokens to documented supported fields and establish the fixed-point schema.
- `hoi4.tech_inspect(mode=explain, technologyId=chaos_warfare_grand_doctrine)` returned `TECHNOLOGY_NOT_FOUND`. Retrying the actual native doctrine ID `chaos_warfare` returned the same exact blocker in workspace `mod_chaos_redux_ea3b2d67c2c0`. Thus neither successful reference tooling nor a native doctrine source definition proves the technology adapter inspects the current `common/doctrines` surface.
- `hoi4.tech_render(view=doctrine, technologyId=chaos_warfare, maxNodes=25)` returned `TECH_RENDERED_PARTIAL`, zero focused renders, `sourceAccurate=false`, 25 selected nodes, and 538 omitted nodes. Its validation failed, so it does not resolve the native-doctrine inspection blocker. Source revision `cdd436f07c14239970e0b4e1e7baa898e38405d053ebb2742cb063e29131c48a` and graph hash `8ce2e6df4b596e9301b7213cbf38df072f160761adfc69e124048d2a3b509ad5` were retained. Artifact references: [render data](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c752b34daa409b0bb9845217b99051baed0251d009037ce342b224befd9f914/77cf2f83a66b5adad4e02494630ede290c17cae1a04ddf2988807f4dadeb2765/technology-doctrine-cdd436f07c14.json) and [render image](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a28792a9cb0cc897ac53167022963f47f6940375c75ccc976f996e527b8fc3a/2145c4e58522113d0c0c536a6d5b714d582e3b246edc31079587c357348822e4/technology-doctrine-cdd436f07c14.png). No supported proposed-source compare was claimed after this failed focus.
- The attempted vanilla `hoi4.source_lookup(symbol=bicycle_battalions)` returned no exact definition and suggested `bicycle_battalion`. It was not treated as a match. The actual installed `mounted_infantry` source was read directly instead.

Source snapshots at review time, SHA-256:

| File | Revision |
| --- | --- |
| Infantry doctrine | `b6b6a7567ab8b662652d7e1cd8d64a767d34c76436b10a06011d8f68228ce4c1` |
| Armor doctrine | `e49e4dd90e873b30f6bef106f860fd727e58a9f89ea557ca25dbef6d29558603` |
| Fire-support doctrine | `04780475bf9aa5f9e55b08b06690aefb513eacdaab659d2737800ca2bfa35847` |
| Operations doctrine | `a43fde59df37cd0322b9f46f394696ade7216687e01c0aaa18d34f18b507e481` |
| `chaosx_technologies.txt` | `e043995be95771a39f15beaadf8d994c9f4020de51d147270cc51cbe2ce26785` |
| `cbw_spirits.txt` | `c295fface0c6eef93327bebe5f799085f733c9d97cfe168a4ecb6196c7c277fb` |

Skills used: `chaos-redux-events` for reward/wording and no-shallow-substitute rules, and `chaos-redux-subagents` for read-only proposal ownership and parent review.
No decisions, focus call sites, GUI helpers, map surfaces, or event-chain changes are proposed.
Those domain skills and inspectors were therefore not invoked.
No commit was created because the parent explicitly retained index ownership.

## Additional bounded category and stack audit

The parent requested this follow-up before finalizing implementation.
Doctrine and technology before values were read from the immutable `docs/testing/2026-10-07_doctrine_reward_revision/before/` copies.
Unit memberships and bases were read from `common/units/cbrn_regimental_support.txt` and `common/units/cbrn_hq_support.txt`, which the parent identified as unchanged.
The analysis did not assume that a public label or shared protective equipment implies chemical-support category membership.

**Three main findings:**

1. All three armored delivery types receive two flat +5 organization grants on base 24, giving `(24 + 10) / 24 * 1.045 = 1.4804167`, above the dedicated 1.35 ceiling.
2. Old Chaos Battalion breakthrough has +30% direct stat grants plus the separate Cadres defense layer. Reserving that layer and Biological Operations Veteran's defense skill gives `1.30 * 1.10 * 1.025 = 1.46575`. The parent's 15% mastery III plus 4% hidden technology allocation gives `1.19 * 1.10 * 1.025 = 1.341725` under that same conservative pooled-stat model.
3. Projector breakthrough fits the pooled-stat model at `1.30 * 1.025 = 1.3325`, but an intentionally pessimistic product of every independent grant gives `1.05^3 * 1.075^2 * 1.025 = 1.3712249`. The latter is an unsupported native-aggregation bound rather than a proven engine failure. No native additive semantics were confirmed by source inspection alone.

The narrow organization correction is to change the Fire Support mastery I organization recipient from `category_chemical_support_companies` to `cbrn_chemical_projector_battery`.
It keeps the projector's existing +5 payoff and preserves the armored track's own +5 payoff while removing the extra unintended armored +5.
After that correction, armored organization is `(24 + 5) / 24 * 1.045 = 1.2627083`.
It changes neither milestone order nor unlock/equipment requirements.
This is a proposal for the parent, and no source patch was applied by this agent.

### All thirteen role memberships and organization grants

| Exact unit | Chemical-support category | Armored category | Primary-protection category | Base organization | Before flat doctrine or technology gain | Organization including conservative 4.5% national layer |
| --- | --- | --- | --- | --- | --- | --- |
| `cbrn_gas_mask_decon_detachment` | No | No | Yes | 24 | 0 | +4.5% |
| `cbrn_chemical_recon_detachment` | No | No | No | 22 | 0 | +4.5% |
| `cbrn_chemical_projector_battery` | Yes | No | No | 18 | Fire Support I +5 | +33.5278% |
| `cbrn_chemical_ammunition_train` | No | No | No | 18 | 0 | +4.5% |
| `cbrn_light_armored_delivery_detachment` | Yes | Yes | No | 24 | Fire Support I +5 and Armor II +5 | +48.0417% |
| `cbrn_medium_armored_delivery_detachment` | Yes | Yes | No | 24 | Fire Support I +5 and Armor II +5 | +48.0417% |
| `cbrn_heavy_armored_delivery_detachment` | Yes | Yes | No | 24 | Fire Support I +5 and Armor II +5 | +48.0417% |
| `cbrn_medical_countermeasure_detachment` | No | No | No | 22 | 0 | +4.5% |
| `cbrn_biosecurity_assault_detachment` | No | No | No | 26 | 0 | +4.5% |
| `chaos_battalion` | No | No | No | 40 | Improved Battalion technology +11 | +33.2375% |
| `cbrn_hq_operations_section` | No | No | No | 45 | 0 | +4.5% |
| `cbrn_hq_protective_logistics_section` | No | No | No | 45 | 0 | +4.5% |
| `cbrn_hq_medical_countermeasure_directorate` | No | No | No | 45 | 0 | +4.5% |

Only Projector and the three Armored Delivery types belong to `category_chemical_support_companies`.
Protection Company, Reconnaissance, Ammunition Train, Field Medical, Biosecurity Assault, Chaos Battalion, and all three HQ sections do not.
The HQ base is 45, and its `category_cbrn_hq` membership grants supply changes rather than the Fire Support flat organization bonus.
No new chemical-support membership is needed for wider mastery coverage.
If the parent adds such membership later, that would be a distinct reward and balance change requiring this matrix to be recomputed.

### Exact two-tier projector and support combat counts

The technology snapshot has exactly two grants, from `improved_livens_projector` and `advanced_livens_projector`.
Each gives soft attack 2.5%, hard attack 13%, defense 4%, and breakthrough 7.5%.
The base Livens technology does not add a third copy of those grants.
The two doctrine country-attack sources are 1.5% and 2.5%, summed 4%, with their independent product reserved as `1.015 * 1.025 = 1.040375` below.

| Unit or stat | Exact before controlled grants | Pooled-stat model with separate layers | Every-grant independent bound |
| --- | --- | --- | --- |
| Projector soft attack | Grand 5% + Fire adoption 5% + Fire V 5% + Operations IV 5% + two technology 2.5% | `1.25 * 1.040375 = 1.30046875` | `1.05^4 * 1.025^2 * 1.040375 = 1.32860179` |
| Projector hard attack | Two technology 13% + country attack | `1.26 * 1.040375 = 1.3108725` | `1.13^2 * 1.040375 = 1.32845484` |
| Projector defense | Grand 5% + Fire adoption 5% + Fire II 5% + Operations adoption 5% + two technology 4% + reserved earned defense skill 2.5% | `1.28 * 1.025 = 1.312` | `1.05^4 * 1.04^2 * 1.025 = 1.34755885` |
| Projector breakthrough | Grand 5% + Fire adoption 5% + Fire V 5% + two technology 7.5% + reserved earned defense skill 2.5% | `1.30 * 1.025 = 1.3325` | `1.05^3 * 1.075^2 * 1.025 = 1.37122490` |
| Each armored delivery soft attack | Four chemical-support 5% grants + country attack | `1.20 * 1.040375 = 1.24845` | `1.05^4 * 1.040375 = 1.26458231` |
| Each armored delivery defense | Four chemical-support 5% grants + reserved earned defense skill 2.5% | `1.20 * 1.025 = 1.23` | `1.05^4 * 1.025 = 1.24589391` |
| Each armored delivery breakthrough | Three chemical-support 5% grants + armor 2% and 3% + reserved earned defense skill 2.5% | `1.20 * 1.025 = 1.23` | `1.05^3 * 1.02 * 1.03 * 1.025 = 1.24660585` |
| Protection Company attack | Cadres 10% + country attack. No chemical-support grant | `1.10 * 1.040375 = 1.1444125` | Same separate-layer reservation |
| Protection Company defense | Cadres 10% + reserved earned defense skill 2.5%. No chemical-support grant | `1.10 * 1.025 = 1.1275` | Same separate-layer reservation |
| Chaos Battalion soft attack | Battalion-specific Fire-independent infantry V 5% + Cadres attack 10% + country attack | `1.05 * 1.10 * 1.040375 = 1.201633125` | Same separate-layer reservation |
| Remaining seven nonchemical roles excluding Protection and Chaos | No reviewed direct chemical-support attack, defense, breakthrough, or flat organization reward | Unchanged generic country/commander layer only | No chemical-support fragments to multiply |

Protection Company has no authored base soft-attack or hard-attack stat in its unit definition.
Its nominal Cadres attack modifier must not be advertised as a meaningful attack payoff merely because that modifier exists.
Its authored defense, breakthrough, equipment, and reliability behavior remain separate real fields.
Medical and Biosecurity Assault have their own categories and specialist base stats, while their mastery eligibility can expand without inheriting chemical-delivery rewards.
Unchanged intrinsic terrain bonuses and equipment identities are the same baseline on both sides of a CBRN-authored bonus comparison.

The parent suggested reducing chemical-support lifetime soft attack from 20% to 15%, concentrating Fire adoption at 10% with Grand 5%, and removing Fire V and Operations IV soft attack.
The parent also suggested replacing the four defense 5% fragments with Operations adoption 17%.
Those cuts are not needed to fix a Protection Company stack because that company has no chemical-support membership.
They are also not required by the two-tier Projector soft-attack or defense bounds shown above, which remain under 35% even in the every-grant independent model.
The 17% defense option would remove shared lifetime reward rather than merely redistribute it.
It remains a possible parent balance choice, but its basis should be concentration or deliberate headroom rather than the disproved Protection Company overlap.

The before projector breakthrough independent bound could be reduced without changing unlock chronology by concentrating all chemical-support breakthrough at one 15% grant and reducing both projector technology breakthrough grants to 7% each.
Its independent bound would be `1.15 * 1.07^2 * 1.025 = 1.349550875`.
That illustrative allocation is only needed if the parent elects to enforce an every-grant multiplication guard despite unresolved native aggregation.
It is not an approved technology retune and has narrow remaining headroom.
Source-only arithmetic cannot prove whether this extra conservatism is necessary.

The category overlap and flat organization sum are definite source findings.
Native country/stat multiplication, the contribution of unit-defense and defense-skill modifiers to attacking breakthrough, equipment aggregation, and actual division-weighted stats remain explicitly unresolved engine semantics.
No additional MCP call, source patch, index write, commit, or runtime claim was made in this bounded follow-up.
