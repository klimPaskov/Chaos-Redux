# Event 006 D34 dynamic-consumer residual audit

Date: 2026-10-08.
Role and ownership: chaosx_scripted_system_architect; gameplay read-only; this assigned handoff is the only written file.
Scope basis: the parent requests residual consumer review against accepted D34/D38/D42 requirements, with the deliberate D43 Event 021 capture/release contract retained.
The parent reports current admission of 109 packages, 78 reservation groups, and 112 adapters, with 84 selectable rows unattested and IW-076/IW-131/IW-179 fail closed.
This audit does not recompute or change admission, reopen those rows, redo the integrated regional/signature/incident tranches, or close the full Event 006 goal.

## Result

Three residual defect families remain: three live targeted decision pools that omit dynamic countries, two FORM-48 scalar membership checks that still name the HBX template, and one FORM-48 category-description key that still reads the HBX template name and six numeric values.
The targeted decision defect has an ordinary admitted IW-043/IW-058 source path when an existing reach relationship qualifies a released dynamic peer.
The FORM-48 defects are definite mismatches with the accepted runtime-country contract, but current normal admission independently blocks IW-179, so this report does not claim a currently attainable full FORM-48 formation or an observed post-formation display failure.
No native execution, popup, scope-resolution, or probability result is inferred from source inspection.

## R1: dynamic peers omitted by three live targeted decisions

File: `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`.

| Decision | Definition / target list | Existing reachable-partner gate |
| --- | --- | --- |
| `independence_wave_iw043_dispatch_volga_trade_delegation` | 766-869; `targets` at 773-776 | `target_trigger` at 777-781 calls `is_independence_wave_iw043_reachable_partner` |
| `independence_wave_iw058_open_diaspora_expert_mission` | 1446-1537; `targets` at 1453-1456 | `target_trigger` at 1457-1461 calls `is_independence_wave_iw058_reachable_partner` |
| `independence_wave_iw058_request_named_external_guarantee` | 1813-1901; `targets` at 1820-1823 | `target_trigger` at 1824-1828 calls `is_independence_wave_iw058_reachable_partner` |

Each declaration contains a literal `targets = { ... }` list with many Event 006 custom templates and intended ordinary vanilla countries.
None has `targets_dynamic` or `target_array`, including later portions of the full decision bodies.
The exact custom-template omissions include the parent's eleven named tags; they are not isolated to the older formable carrier repairs.
The offline decision rule says a literal target list restricts the actual tag country, while `targets_dynamic = yes` is needed to include countries with that original tag.
An absent template does not become the released dynamic actor merely because a later `FROM` predicate would recognize the actor's origin.

Reachable source chain:

1. An admitted IW-043 actor (`original_tag = CHU`) or IW-058 actor passes its exact package gate and the listed focus-completion/unused-receipt `target_root_trigger`.
2. An existing live dynamic peer from the declared template list has a treaty, league/network, patron, or diaspora reach condition that would satisfy the partner predicate.
3. Native target selection restricts the decision to its static `targets` before `target_trigger` can expose that peer as `FROM`.
4. The missing peer never reaches the existing payment/project action or its target-dependent AI score.

The two existing partner predicates are at `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:288-317`.
They require existence, the correct ROOT actor, a different target, peace with ROOT, no subordination to ROOT, and one of the authored reach relations.
They do not repair the decision's earlier static candidate enumeration.
These are current paid diplomatic consumers, not dormant blueprint/preflight paths.
This is a source-supported missing-target diagnosis, not a claim that a particular live campaign contains a qualifying relationship.

Smallest owner-applied correction:

- Enable original-tag dynamic targeting in these three existing decision definitions using the documented `targets_dynamic = yes` route, while retaining their authored target lists and ordinary vanilla foreign targets.
- For dynamic/custom Event 006 peers, pair that enumeration with a bounded `global.independence_wave_active_countries` registration proof in the target gate: same live country, correct `original_tag`, current package/generation/anchor contract, and matching generation row.
- Retain the existing reach, peace, actor, receipt, affordability, payment, result, and cooldown rules.
- Do not use `targets_dynamic = yes` as permission to accept unrelated civil-war countries, stale rows, Event 021-owned origins, or unregistered dynamic peers.
- Do not replace the entire pool with the Event 006 registry alone: that would silently remove intended ordinary foreign partners.
- A retained mixed pool must preserve both the explicit vanilla branch and the bounded live Event 006 branch; do not assume unverified union/intersection semantics from combining `targets` and `target_array`.

This changes a weighted target pool even if all numerical coefficients remain identical.
The parent must obtain `chaosx_ai_probability_auditor` baseline and identical-scenario compare before/after an owner-applied patch.
Use at least a legal registered dynamic peer, no qualifying peer, a stale-generation row, an unregistered dynamic country of the same original tag, and an ordinary legal vanilla partner; bind the actor, target, reach flags, funds, and transaction state explicitly.
The three `ai_will_do` blocks contain target-dependent FROM reach modifiers, so score/eligibility effects must not be dismissed as an unchanged-weight proof.
No coefficient, target list, or decision source was edited here.

## R2: FORM-48 founding arrays still test the static HBX scope

File: `common/scripted_triggers/006_independence_wave_form48_triggers.txt:78-108`, helper `has_independence_wave_form48_exact_founding_ledger`.
Residual clauses at 83 and 86 are respectively `is_in_array = { array = independence_wave_formable_member_country_entries value = HBX }` and `is_in_array = { array = independence_wave_formable_invited_country_entries value = HBX }`.
The dynamic `any_of_scopes` HBX lookup at 92-95 was repaired, but it does not replace those two independent scalar equality tests.

The arrays are country-scope receipt arrays holding actual selected country pointers, not template identity enums.
`independence_wave_formable_build_member_and_anchor_ledgers` appends `event_target:independence_wave_formable_candidate_country` at `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:2688`.
The invitation writer appends `event_target:independence_wave_formable_invited_candidate` at 2413, with a parallel generation entry at 2414.
For a released HBX-original dynamic carrier, the correct array element is the live carrier ID rather than its absent static HBX template.

Call chain:

`independence_wave_proclaim_military_union` at `common/decisions/006_independence_wave_decisions.txt:3952-3985` -> available/custom-cost `can_independence_wave_commit_selected_formable` -> FORM-48 branch at `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:1663-1666` -> `has_independence_wave_form48_runtime_commit_proof` -> `has_independence_wave_form48_strict_mutation_preconditions` -> `has_independence_wave_form48_exact_founding_ledger`.

The effect path repeats this proof in `independence_wave_formable_commit_selected_family` at registry effects 3043-3049, and `independence_wave_formable_identity_adapter_48` at `common/scripted_effects/006_independence_wave_form48_effects.txt:42-51` repeats it before publishing the PFX identity.
This is a live transaction validation family, not a template planning check.
Normal current admission independently prevents the required FSM/IW-179 member from completing this family, so the residual should be fixed without changing that fail-closed gate or claiming it is today's sole blocker.

Smallest owner-applied correction: in this explicitly carrier-country helper, compare both local arrays to the actual current carrier (`THIS`) instead of `HBX`.
Retain the existing bounded active-registry HBX lookup, original-tag/eligible-package/378-anchor proof, frozen generation/consent checks, exact array counts, and vanilla HAW/FSM checks.
A two-token correction is sufficient here; deleting the membership tests or adding a fallback static entry is not equivalent.
If the parent instead moves the checks into the existing bounded carrier lookup, keep the arrays scoped to the proposer and compare the selected live carrier pointer, with explicit PREV/ROOT ownership.
Do not add a new generic helper merely to wrap these two scalar tests.

The check affects availability of the shared DM-55 decision, which has `ai_will_do`; route its eligibility baseline/compare through the probability auditor before owner application.
The record must retain the current IW-179-blocked scenario separately from an explicitly assumed valid frozen founding ledger; the latter is a source contract scenario, not a claim of current native attainability.

## R3: FORM-48 category text reads the absent template and wrong ledger

File: `localisation/english/006_independence_wave_pacific_l_english.yml:178`, key `independence_wave_form48_federal_compact_category_desc`.
It uses `[HBX.GetName]` twice and six HBX-scoped variables: shipping coordination, industrial specialization, defense readiness, member autonomy, compact strain, and completed program cycles.
The category is defined at `common/decisions/categories/006_independence_wave_categories.txt:666-676` and is visible for either a post-formation carrier or an active autonomous member.
`common/decisions/006_independence_wave_form48_decisions.txt:61-402` supplies its live carrier/member work-cycle decisions.
The ordinary `_desc` binding makes this key the category's description; no explicit alternate description selector repairs it.

Producer/consumer chain:

Successful shared commit -> `independence_wave_form48_initialize_postformation` -> six ledger variables initialized on the live carrier at `common/scripted_effects/006_independence_wave_form48_effects.txt:322-328` -> post-formation carrier/member category visibility -> the HBX-static description key.

For an autonomous HAW/FSM viewer, using ROOT alone would also be wrong: ROOT is the member, while the common ledger belongs to the actual bound carrier.
This is a definite display-addressing mismatch in the accepted post-formation surface, with the same current IW-179 admission caveat as R2.
It is not an observed zero/wrong-name display and no native localisation rendering was performed.

Smallest owner-applied correction: apply the existing D38 display approach to this one description key.
Resolve the valid current HBX-original carrier through the bounded active registry and its package/generation/378-anchor proof, respecting the member's validated carrier binding when the viewer is a member.
Capture the name pointer and six numbers in caller-initialized temporary outputs before formatting the unchanged narrative/labels.
The existing FORM-05 implementation at `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt:352-415` demonstrates this caller-owned display pattern.
Avoid a static tag alias, unbound pointer, ROOT-only substitution, persistent presentation variable, stale temporary result, or invented fallback identity.
Update the existing localisation key and its narrow scripted-localisation consumer together; no layout, picture, asset, new mechanic, or spreadsheet change is implied.
This presentation-only correction does not alter a weight or probability-bearing gate and does not require a probability comparison on its own.

## Literal references that are not definite residual defects

| Surface | Classification and evidence |
| --- | --- |
| Eleven named literal scope blocks in `006_independence_wave_triggers.txt` | Capacity/preflight blueprint checks at AFX 2240, AGX 2268, AJX 2358, ARX 2420, ASX 2448, GZX 4067, CJX 4375, HBX 4599, AXX 4627, BAX 4655, BBX 4683; they select planned packages/countries/anchors/groups before materialization and are not live government mutation scopes |
| All other custom scope blocks in that main trigger file | The full scan finds 34 custom-template blocks, all in `independence_wave_liberations_capacity_try_iw_*`; the same preflight classification applies |
| `tag = X` in automatic readiness, region dispatch, and execution | Template selection against possible-country/blueprint scopes, followed by `create_dynamic_country` and live event-target rebinding; not an original-tag replacement opportunity |
| `original_tag`, `copy_tag`, `original_tag_to_check` | Identity/template/explicit original-tag enumeration tokens, not literal live country scalar targets |
| Event 021 adapter registry and footprint | Deliberate static blueprint/capture/release API; D43 adds the bounded aligned active-registry fallback only when a static actor was not captured, with owner capture validity retained; do not widen or rewrite this accepted cross-origin contract |
| D42 FORM-05 ARX/ASX threat and Pacific HBX collapse modifiers | Already use bounded `global.independence_wave_active_countries` lookups and original-tag/package predicates; no remaining literal ARX/ASX/HBX live scope was found there; not re-audited or rebalanced |
| FORM-04 `strength_ratio.tag = GER`, vanilla HAW/FSM/ICE/SCO/RHI scopes | Ordinary vanilla country consumers, not custom dynamic-template defects; unchanged |
| Country-name registration keys in `006_independence_wave_countries_l_english.yml` | Country identity/localisation definitions, not live `[TAG...]` lookups |
| Scenario blocked-country and planned-country arrays | Static candidate/blueprint pools used before release; their literal entries are deliberate |

AKX is a separate conditional case, not counted as a definite residual requiring an immediate patch.
`has_independence_wave_form02_strict_mutation_preconditions` retains literal AKX scopes at `006_independence_wave_form01_02_04_triggers.txt:333,340,345`, and the state-337 puzzle trigger retains one at `006_independence_wave_formable_state_puzzle_triggers.txt:251`.
The current eligibility helper requires scenario origin, package IW-011, and state 337, while D34/current admission leaves IW-011 scenario-only/unattested for ordinary release.
The inspected execution switch contains no AKX `create_dynamic_country` branch and retains a static `release = PREV` fallback after its explicit dynamic branches.
Therefore a live dynamic AKX call chain was not established here; a literal reference to a genuinely static scenario-created AKX would not be this defect.
If the parent later materializes the accepted scenario member dynamically, all four runtime/puzzle AKX sites need the same bounded live lookup before claiming that path complete.
This note does not authorize a new scenario, admission, country, release implementation, or current design change.

## Scan coverage and source identities

The lexical audit used the requested `006*.txt` / `006*.yml` scope and the 102 custom templates declared by `common/country_tags/006_independence_wave_countries.txt`.
Coverage: 71 scripted-effect files, 60 scripted-trigger files, 40 decision/category files, 3 scripted-localisation files, 9 Event 006 event files, and 58 English localisation files.
There were 1,019 non-comment custom-tag lines across the script scope.
The final pass also checked bare target-list tokens, which is how the three R1 decisions were found after scalar/scope inspection.
No non-comment custom-country target residual was found in the nine event files; the incident-file template mentions are comments.
All literal `has_war_with`, `is_neighbor_of`, scalar country values, custom scope blocks, static `tag` fields, bare target-list entries, and English custom-tag namespaces were classified within this bounded file set.
The only English live custom-tag namespaces found were the FORM-48 HBX description reads above.

| Source | SHA-256 at audit |
| --- | --- |
| `common/country_tags/006_independence_wave_countries.txt` | `a924da87bb4a89c72a0d14c38b5c7ff268e5f9f098fedabc147e2331c8069215` |
| `common/decisions/006_independence_wave_iw043_iw058_decisions.txt` | `c6c1df3711f44269543fcc2d093a6f7f968bc2932aca113aa887663d371e13f6` |
| `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt` | `f372d94173d76a4b3a9d4eedb6e7b2df80fae6eebddfd1c92e3fe70a05580127` |
| `common/scripted_triggers/006_independence_wave_form48_triggers.txt` | `342a0fb96aed1def1ba0b766e000a46092ba3d6a0a814f1f2e79644645f17c44` |
| `localisation/english/006_independence_wave_pacific_l_english.yml` | `865e292d3ddec4a21f7b38f35c8ff9bf3ab6829f01a3236d2d8ac4af6232a126` |
| `common/decisions/categories/006_independence_wave_categories.txt` | `36a1f6a753cfb0dc33522e8c977878de0a43ea05198b6968f93378ee71078f80` |
| `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` | `781c75b80725e184af4420aefebbd4bc510374f78c9b38f45cb752fa3d628454` |
| `common/scripted_triggers/006_independence_wave_triggers.txt` | `70d27c4716e15d439a0819b868a1a747ba6dc29cc9cbd9fa7261d97ab5acae15` |
| `common/scripted_effects/006_independence_wave_execution_effects.txt` | `b5cca5c867f01f9610205bb1aa200d996a4ae060e74e5cf058c3d01eeacf2f85` |

## References and connected MCP evidence

Skills used: current events and subagents skills, plus decisions/missions guidance for targeted decision semantics.
Accepted basis read: `agent_decisions_2026-10-04.md` D34, `agent_decisions_2026-10-05.md` D38/D42/D43, and `subagent_handoffs/country_dynamic_carriers_20261006.md`.
Old handoff queued threat/adapter findings were compared to the current accepted repairs, not promoted as still-open defects.

The connected schemas exposed reference_context/search/read, source_lookup with symbol/path/keyPath/fromLine/fromColumn/expectedRevision, and probability_inspect with typed source object, adapter, and candidatePool.
Successful calls returned workspace `mod_chaos_redux_ea3b2d67c2c0`.
No timeout occurred requiring a narrower timeout retry during this audit.
One vanilla continuation returned `SOURCE_REVISION_STALE` after shared workspace indexing changed; the same bounded symbol/fromLine lookup was refreshed successfully rather than treating that as an unavailable route.

| Read reference | Lines | Revision |
| --- | --- | --- |
| Installed `documentation/effects_documentation.md`, create_dynamic_country | 3033-3045 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation/triggers_documentation.md`, original_tag / any_of_scopes / is_in_array | 6983-6991 / 1531-1545 / 5672-5685 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, original_tag | 640 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, array equality / bounded scope loop | 1147 / 1149 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, category desc / target selection | 68-78 / 519-530 | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| Offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, scope namespaces | 531-555 | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| Installed `documentation/script_concept_documentation.md`, localisation/event scope relation | 150-155 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common/decisions/_documentation.md`, local direct read | 1-46 | Raw SHA-256 `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` |

The installed decision documentation identifies actor/target scopes and availability timing; the offline target rule supplies explicit `targets_dynamic` semantics.
Vanilla `YUG_ustasa_uprising`, `game:common/decisions/YUG.txt:811-831`, demonstrates dynamic-country creation and storage of the actual new country pointer (`croatia_var = this` at 831, also read locally).
Its resumed source lookup used revision `9a8a04e72d78ed657643910aa7380802e3d815f3112626aca204291e474bbc0b`; the earlier stale expected revision was `2e92f40c9cde866c8cbcbf95e3916cbed6ea4e0982f2b41fe348f9dd693de751`.
Vanilla `ENG_speech_against_germany` at `game:common/decisions/ENG.txt:1669-1699` supplies a direct installed precedent: `targets = { GER }`, `targets_dynamic = yes` at 1685, and `FROM = { original_tag = GER }` in its target gate.
The bounded local excerpt was read and the vanilla file's raw SHA-256 is `83351419122bbc4f4a7fa693dbe7658396c1781b5aea28b5d100a0dd3b8d1fef`.

Source lookup confirmed the non-shadowed FORM-48 ledger at 78-108, the category's decision content at 61-402 and metadata at 666-676, and the FORM-02 AKX conditional sites at 322-347 under indexed revision `2e92f40c9cde866c8cbcbf95e3916cbed6ea4e0982f2b41fe348f9dd693de751`.
The ledger continuation at 104/column 55 reached 108 with no continuation left.
The category's full decision body was not paged because the narrow metadata and relevant decision source were read directly; no complete MCP category-body coverage is claimed.
Lookup references were incomplete (`referencesComplete = false`, 20,205 unresolved references at that revision), so reachable chains above are direct source traces, not claimed complete indexed reference graphs.
The preflight lookup at `independence_wave_liberations_capacity_try_iw_006:2231-2257` and Event 005 classifier at 1858-1860 used revision `9a8a04e72d78ed657643910aa7380802e3d815f3112626aca204291e474bbc0b`.
The three R1 decisions were each found as non-shadowed decision definitions at revision `2b7e25b56df76abb08f208cf98e8570004eb14734da0ed6be7afec85bed98327`, with the first 16 lines retaining their target declarations; their complete bodies were read locally for dynamic/array fields and AI modifiers.
These are offline source and reference results, not native execution.

## Validation, audit routing, and completion limits

Meaningful source checks: all-template scalar/scope/namespace scan, bare-target-list scan, complete three-decision bodies checked for missing dynamic/array fields, actual live pointer producers traced to the FORM-48 receipt consumers, post-formation variable producers traced to the description key, and current D42/D43 implementations checked against the accepted decisions.
A two-clause symbolic array-equality check confirms the source mismatch when an array contains a distinct live HBX-original country pointer; it does not implement the native token/variable resolver or simulate a formation.
No broad generator, durable tooling, scenario simulator, source patch, or helper scaffolding was created.

Probability inspection was started for affected weighted eligibility/target surfaces, solely to identify the owning adapter and route the required later specialist pass.
The first shared-decision identifier request used a nonexistent name and returned identifier_not_found; it was corrected to the actual `independence_wave_proclaim_military_union`.
That decision inspection found one candidate with `poolComplete = false`; empty required-input discovery is not a complete scenario or balance result.
For R1, the connected service classifies these timed `days_remove` actions under `mission_ai_will_do`, despite their player-facing decision presentation; the initial decision-adapter candidate-pool request matched zero and suggested the mission adapter, which was then requested for the exact three candidates.
This metadata classification is not a redesign of their native action type.
Final probability discovery identities and limits are retained below.
No probability_evaluate, sweep, seeded simulation, numeric before/after comparison, or balance target was authored here.
The parent must route R1 and the R2 DM-55 eligibility patch through `chaosx_ai_probability_auditor`; this architecture audit is not that baseline/compare evidence pass.

No definite additional live custom-template scalar/war/strength/scope/display defect was established in the remaining requested files.
AKX remains explicitly conditional, and current IW-179 admission constrains the FORM-48 consequences as described.
Native reachability, exact formatted output, combined target-source semantics, and probability effects remain unobserved or unmeasured.
No simplification or fallback was applied.
Only this handoff was written; no other document, gameplay file, index, Git state, asset, spreadsheet, hook, or admission list was changed, and no game/log request or launch occurred.

### Final weighted discovery evidence

R2/DM-55: `hoi4.probability_inspect`, adapter `decision_ai_will_do`, source object `{ path: common/decisions/006_independence_wave_decisions.txt, identifier: independence_wave_proclaim_military_union }`, returned `PROBABILITY_SOURCE_INSPECTED`, one candidate, and `poolComplete = false`.
Its source revision is `377a3db3c95196035543c0e6dd750380c13191f9607b01b11b340cf4b30f3c57`, analyzer source hash `e5d185430da68ade61d6e01e16b429f109825526a533ad62b03021f7bec02391`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fe7db1c830bf342450a9183fe73227d903bec8946691ea4f9a0fbd61595ee57/78641ab6b1861db0855e21af8fe3fa53dc248a788eb28048ea824e390d21ec64/probability-inspect-e5d185430da6.json` (declared 9,812,451 bytes).

R1: the corrected `mission_ai_will_do` discovery used the exact three decision identifiers as `candidatePool` and the mod-relative source object for `006_independence_wave_iw043_iw058_decisions.txt`.
It returned `PROBABILITY_SOURCE_INSPECTED`, three candidates, and `poolComplete = true` for that requested three-action source pool.
That does not establish a complete dynamic-country target pool, complete helper inputs, availability, or a numerical scenario.
Reported required paths are `command_power`, `num_of_civilian_factories_available_for_projects`, and `scope.has_equipment`.
Its source revision is `84442b86b626e114ecc55dc36826cf4345280c1ab080dd33df0e4bb535673d7c`, analyzer source hash `2146272f1123b19c6400484febe16c00241a3e488aeb48ae35e52c38d16990ef`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6c15a836f627374cd54882cb5a6107648c67feea4c90a21d4fcaae81ab57051/568128eeb65984b7c43c6a8ba058aabaed7eb74a6e625464c041941627a61341/probability-inspect-2146272f1123.json` (declared 15,571 bytes).
The preceding wrong-adapter discovery is retained as `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fae0b84b083a87a30f392bdde266ade305ad4cfd942759cd29f661738a76a8f/cc9d792aa908c48042e1a2c61af3eef892ffc7a4fc8b2e82fcc6cd4db0d49bbd/probability-inspect-2146272f1123.json`; it found zero requested decision-adapter candidates and suggested the mission adapter, rather than proving a route gap.
The earlier wrong DM-55 identifier discovery is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/533869e95559cfc6be225fd6e55298974828d646169421ff28196b3ae9f37ad5/156ae5fa99a3e68f263ec9bdb81cb977cb18ef731076c3addfe2c57bfd2f8d88/probability-inspect-e5d185430da6.json`; it is not a baseline.
These artifact identities and inline discovery summaries are retained for the specialist handoff; their complete bodies were not consumed for score/parameter analysis, and no such analysis is claimed.
Analyzer source hashes and local raw-file hashes are separate reported identities; this reviewer did not infer they were byte-equivalent.

The final lexical check confirms 55 custom templates in each of the three static target declarations, with no dynamic-targeting option or target-array declaration in any full body.
The main-trigger parent-definition check independently confirms that all 34 custom scope blocks belong to capacity_try helpers.
The three residual source files were rehashed at the end of this audit and still matched the recorded raw hashes.
