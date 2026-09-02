# Event 016 current technology MCP review

## Outcome

Current targeted inspection and render coverage exists for all eighteen Event 016 hidden technologies and all three technologies in the explicitly included shared clone file.
There is no newly identified gameplay defect in this bounded review.
There are three concrete analyzer coverage limitations and one blocked comparison, detailed below; this is not a clean global technology validation, engine-execution proof, probability certification, or overall Event 016 completion.

This auditor changed only this handoff and `.tmp/016_technology_current_mcp_evidence_2026-09-02.json`.
No gameplay, assets, configuration, tests/report generator, or commit was created.
No Hearts of Iron IV launch or log request occurred.
Parent implementation and other agents' concurrent helper/model/GUI work were preserved.

## Scope, authority, and accepted-plan disposition

The requested eighteen are eleven definitions in `common/technologies/016_brilliant_scientist_project_technologies.txt` and seven in `common/technologies/016_brilliant_scientist_project_force_technologies.txt`.
The shared `common/technologies/clone_technologies.txt` contains another three, so the explicit reviewed set is twenty-one, not eighteen including clone.
The six-family conventional integration uses existing flags/modifiers and adds no hidden technology here.
Its source integration remains accepted by `016_final_conventional_api_integration_review_2026-09-02.md`; this task does not reopen its lifecycle, cost, or slot audit.

The named September 1 technology probability baseline, generic identifier migration, and technology/API rework handoffs were read in full.
Their prior render/transport failures are superseded only by the successful current inspect/render evidence here.
Their earlier probability conclusions are historical and not renewed by this audit.
The old rework handoff's research-slot revocation wording is superseded by the current conventional integration handoff's durable-learning contract, not accepted as current behavior.
The current event final-completion contract and prior accepted source integration remain authoritative; no new design or fallback is proposed.

## Completion by surface

| Surface | Current evidence and status |
| --- | --- |
| Exact technology selection and source links | All 21 `explain` requests return the exact requested ID, raw source, source line/hash, and a real technology node; accepted current structural coverage. |
| Hidden/grant-only status | All 21 are `hidden=true`, have no folder placement, and raw source includes `allow={always=no}`; explicit grant sites are discovered for every ID. Runtime trigger execution is outside the analyzer. |
| Equipment and battalion unlocks | All selected equipment/subunit unlock targets resolve, including generic paleogenetic, xenobiological, temporal, robot, portal, clone and Aryan-clone IDs. |
| Alien predictive tactics | Both unlock references are captured, but falsely unresolved by the installed target parser; existing source definitions and vanilla structure verified below. |
| Bonuses/control identities | Distinct nested source bonus bodies and source-linked grant consumers are retained. The analyzer does not give a typed nested-stat comparison; its identical-signature warning is insufficient evidence of duplicate effects. |
| Dependencies | Thirteen source `dependencies` blocks are not converted into graph edges; all selected prerequisite lists/render edge lists are empty. This is incomplete tool coverage, not absent source dependencies. |
| Xeno exclusivity | No technology-level XOR is declared; actual control exclusivity and deterministic repair are in the API/native helper predicates. Source-reviewed, not executed or represented as graph-exclusive edges. |
| Icons/localisation | All 21 explain records resolve icon sprite/texture and English name/description. All 21 targeted node renders contain one successfully rendered icon with zero unresolved icon sprites and no omitted selected node. |
| Comparison | One real historical revision attempt fails `TECH_REVISION_NOT_CACHED`; no source-change regression claim is made. |
| AI/probability | Not evaluated or certified here; parent probability auditor retains ownership. |
| Assets/game UI | Existing references and selected generated previews only. No asset production/manifests/model/sound or in-game research-screen acceptance is claimed. |

## Exact source inventory and outputs

B means `common/technologies/016_brilliant_scientist_project_technologies.txt`.
F means `common/technologies/016_brilliant_scientist_project_force_technologies.txt`.
C means `common/technologies/clone_technologies.txt`.
Numbers below are exact source literal values after substituting file-local constants, not a separate engine or balance evaluation.

| ID | Source | Declared consumer/output |
| --- | --- | --- |
| `brilliant_scientist_portal_warfare_tech` | B:37 | `teleportation_equipment_1`, `portal_raider`; organisation 20, breakthrough .50, supply -.25. |
| `brilliant_scientist_clone_formations_tech` | B:52 | `clone_equipment_1`, `clone_infantry`; organisation 8, defense/soft attack .15. |
| `brilliant_scientist_robot_formations_tech` | B:67 | `autonomous_robot_equipment_1`, `autonomous_robot`; hard attack/breakthrough/defense .50, organisation 20. |
| `brilliant_scientist_paleogenetic_formations_tech` | B:83 | `paleogenetic_creature_equipment_1`, `paleogenetic_creature`; soft attack/breakthrough .50, supply .25. |
| `brilliant_scientist_xenobiological_formations_tech` | B:98 | `xenobiological_assault_organism_equipment_1`, `xenobiological_assault_organism`; soft attack/breakthrough .50, hard attack .25, organisation 8. |
| `brilliant_scientist_xeno_chemical_control_tech` | B:114 | Xeno base dependency; xeno defense .50, supply -.50, casualty trickleback .50. |
| `brilliant_scientist_xeno_neural_control_tech` | B:128 | Xeno base dependency; xeno organisation 30, morale .50, soft attack .50. |
| `brilliant_scientist_xeno_machine_control_tech` | B:142 | Xeno base dependency; xeno hard attack .75, breakthrough .50, reliability .50. |
| `brilliant_scientist_xeno_researched_control_tech` | B:156 | Xeno base dependency; xeno soft/hard attack .35, organisation 8, supply -.25, experience loss -.50. |
| `brilliant_scientist_temporal_guard_tech` | B:172 | `temporal_guard_equipment_1`, `temporal_guard`; organisation 20, defense .50. |
| `brilliant_scientist_alien_infantry_tech` | B:186 | `alien_laser_weapon_equipment_1` only; intentionally no `enable_subunits` or combat-stat bonus. |
| `brilliant_scientist_portal_warfare_weaponization_tech` | F:36 | Portal base dependency; portal organisation 20, breakthrough .50, supply -.25. |
| `brilliant_scientist_clone_formations_weaponization_tech` | F:50 | Clone base dependency; clone organisation 20, soft attack/defense/breakthrough .85, morale .50, experience loss -.50, casualty trickleback .30. |
| `brilliant_scientist_robot_formations_weaponization_tech` | F:68 | Robot base dependency; robot hard attack/breakthrough/reliability .50. |
| `brilliant_scientist_paleogenetic_formations_weaponization_tech` | F:82 | Paleo base dependency; paleo soft attack/breakthrough .50, maximum speed .25. |
| `brilliant_scientist_xenobiological_formations_weaponization_tech` | F:96 | Xeno base dependency; xeno soft attack/breakthrough .50, hard attack .75. |
| `brilliant_scientist_alien_predictive_warfare_tech` | F:110 | Alien base dependency; `tactic_alien_predictive_vector_assault` and `tactic_alien_probability_screen`. |
| `brilliant_scientist_temporal_guard_weaponization_tech` | F:121 | Temporal base dependency; temporal organisation 20, defense .50, experience loss -.75. |
| `clone_infantry_access_tech` | C:25 | Shared `clone_equipment_1` and `clone_infantry` unlocks without combat-stat refinement. |
| `mengele_clone_refinement_tech` | C:34 | Shared access dependency; clone organisation 10, soft attack .20, defense .15, morale/trickleback .20, experience loss -.20. |
| `mengele_aryan_clone_refinement_tech` | C:50 | Mengele refinement dependency; `aryan_clone_infantry` unlock; Aryan organisation 15, soft attack .30, defense .25, morale/trickleback .30, experience loss -.30. |

The alien battalion remains `active=no` at `common/units/016_brilliant_scientist_project_forces.txt:289`–`:295`; absence of an alien subunit unlock in B:186 is intentional, consistent with its locked-template access contract.
The two predictive tactics at `common/combat_tactics.txt:1280` and `:1302` each require `has_unit_type=alien_infantry`, their matching attacker/defender role, and standard phase; each is initially `active=no`.
No tactic score or probability was evaluated.

## Severity-sorted evidence gaps and disposition

### T1 — Required structural comparison is blocked

The earlier real scan artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/55a4f393ec3fc36b143084e3dcf800146e047a1ec6c68015aea884e0c99153ec/0eeda93f94ec8056fa1288f8dd1f1ecdcb724cd0ae49671543e793591c237977/technology-scan-2a862ecb7112.json`.

Its actual JSON is `technology-analysis.v1`, `report.authoritativeGraphIncluded=false`, with `artifactProjection.mode=large-scan-summary` and no `graph`.
It is not a durable comparison graph.
It was read locally, not repeatedly submitted as an invalid artifact.

The single comparison used this supported schema and the historical revision actually recorded inside that artifact:

```json
{"workspaceId":"mod_chaos_redux_ea3b2d67c2c0","before":{"revision":"2a862ecb7112e9a7bd4aa209c9ac0ca0647258e073cd5609e3cb1bb96157855d"},"after":{"revision":"f45db9ce92bee7b706e34c93e5ea88803a4bc79199995d4e5753ddd2aeb5bf15"},"refresh":false,"render":false}
```

Result: `status=error`, `TECH_REVISION_NOT_CACHED`, message `Requested technology revision is not cached`, zero artifacts/changed files, and `validation.passed=false`.
The old revision was not invented and the current revision was not substituted as a fake before side.

Installed `schemas/technology.js` accepts exactly one `revision` or `artifactUri` per graph reference.
`technology/service.js:371` accepts a validated graph as the top-level JSON, `graph`, or `report.graph`; summary projections are insufficient.
`technology/queries.js:36` conditionally emits the full graph only below its record threshold.
Current explain/render outputs contain reports/selections, not an authoritative whole-graph snapshot.
The inspected baseline handoffs supplied no usable full graph resource.
`core/idle-cache-lifetime.js:2` releases idle analysis caches after 30 seconds, and `technology/service.js:437` clears history as well as current graphs.
Thus no current before/after regression claim is possible from this evidence.
Minimal follow-up is an actual retained compatible graph baseline and immediate cached comparison across a future owner change; do not relabel reports or fabricate reconstructed baseline data.

### T2 — Dependency and exclusive-control coverage is incomplete

Installed `technology/source-analysis.js:224` parses classic `path`, then XOR/subtechnology edges, but never parses `dependencies`.
The structural-field set at `:4` also omits `dependencies`, which appears incorrectly among the effect keys instead.
Every one of the thirteen declared dependency blocks above remains in the raw source but all selected `directPrerequisites` arrays and corresponding individual render edge sets are empty.
The one-node renders therefore prove ID/icon/source selection, not correct dependency topology.

No Xeno technology declares a static XOR, so `exclusiveChoices=[]` is accurate for the technology database.
The actual exclusivity policy is source-backed:
`common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt:216`–`:240` forbids each selected control when another control is current.
Current-state queries at `:59`–`:95` account for native/external flags and learned tech.
`common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:175` chooses native control first, otherwise repairs external/learned state in deterministic chemical/neural/machine/researched order, and `:308`–`:335` clears competing control packages.
The grant blocks at `:458`–`:505` use the matching eligibility predicate and operational-base core.
These conditions are not modeled as technology graph-exclusive edges, and their runtime execution is not certified.

Minimal disposition: retain source acceptance and explicit analyzer gap; do not change gameplay to add redundant XOR/path structure merely to silence the tool.

### T3 — Predictive tactic target warnings are parser false negatives

Only `brilliant_scientist_alien_predictive_warfare_tech` has targeted `TECH_UNLOCK_TARGET_MISSING` issues, one for each tactic.
Both unlock declarations are captured, and the focused unlock render shows three correct IDs and two edges, but marks both targets missing.

The source definitions exist at `common/combat_tactics.txt:1280` and `:1302`.
Installed `technology/source-analysis.js:455`–`:459` only discovers tactic definitions beneath a `combat_tactics={...}` wrapper.
The mod and installed vanilla `common/combat_tactics.txt:14` instead use root-level `tactic_...` definitions, which is the actual vanilla precedent.
This establishes an exact tooling resolution defect, not missing game content.
No duplicate tactic or wrapper change is recommended.

### T4 — Xeno identical-signature warning does not compare control bonuses

All four controls return one shared `TECH_SUSPICIOUS_IDENTICAL_SIGNATURE` design warning.
Their equal parsed signature is `c74ec12de9ab52b3ea503a30a8ddb8bb007b2b2d2556bf004c5106f03b3ec57b`.
The effect keys are `dependencies`, `special_project_specialization`, and `xenobiological_assault_organism`.
Installed `technology/source-analysis.js:348`–`:396` builds that signature from top-level key names and unlock tokens, and `technology/graph.js:1051`–`:1080` groups those signatures without nested effect values.

The differentiated bonuses are retained in each report's `technology.rawSource` and are listed in the exact inventory above.
Each control also has five actual source-linked grant sites: project stage output, project inheritance, native force rebuilding, public upgrade, and grant reapplication.
For chemical these are `016_brilliant_scientist_project_effects.txt:573` and `:1142`, `016_brilliant_scientist_project_force_effects.txt:490`, and `016_brilliant_scientist_custom_technology_api_effects.txt:466` and `:613`.
The five-source/six-node focused chemical grant render genuinely captures those consumers.
It does not execute native health gates, country scopes, control policy, or nested bonus arithmetic.
`matchingBonuses=[]` refers specifically to external research bonus references in `technology/queries.js:242`, not absence of the nested combat bonuses.

Minimal disposition: no gameplay differentiation patch is warranted by this warning.
Treat the current source as four differentiated controls and retain missing typed-stat analysis as a limitation.

## Current MCP invocation and actual coverage

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Workspace identity: `d8a1d88374e80d7f570cd2a4ef9ae28716f36afe38d2ba5dfdc0db59eff9b6c3`.
All successful calls returned revision `f45db9ce92bee7b706e34c93e5ea88803a4bc79199995d4e5753ddd2aeb5bf15`, graph hash `6bf3afb7279f4d6fa193b77d224c0efab644c3df8888c8dd43df9c2a5c379fba`, and `complete=true`.

Each exact ID was passed to `tech_inspect` with `mode=explain`, `refresh=false`, then `tech_render` with `view=technology`, `maxNodes=8`, `includeHtml=false`, `refresh=false`.
All 21 inspect calls returned `TECH_INSPECTED`.
All 21 individual renders returned `TECH_RENDERED`, exact selected ID, one node, zero omitted nodes, and one requested/rendered icon with no unresolved sprites.
Two additional `maxNodes=20` renders used chemical `view=grants` and predictive `view=unlocks`; their actual node/edge counts are respectively 6/5 and 3/2, both with zero omissions.

The first targeted request rebuilt the technology inventory internally; the auditor did not request a broad scan or audit unrelated vanilla issues.
The cache-adjacent sequence retained one current revision for all successful calls.
Global `validation.passed=false` reports 1,427 blocking technology diagnostics; those are not represented as Event 016 findings or a pass.
The selected reports have only the shared Xeno design warning and the two predictive tactic resolution errors discussed above.
All other selected issue arrays are empty.

The analyzer's stated limits include runtime allow/visibility execution, meta-generated/variable IDs, exact AI research choice/time, and dynamic localisation without runtime values.
Individual graph previews are `sourceAccurate=false`, explicitly generated analysis layouts, not research-screen placement previews.
Their narrow canvas clips long diagram headings and abbreviates labels/year-constant text; this is a visible limitation of these diagnostic artifacts, not an in-game UI acceptance claim.
Raw JSON retains exact IDs and source locations.
No `view=assets`/metadata/exclusive broad render was requested because installed `technology/render.js:315`–`:342` ignores `technologyId` for those views and would return unrelated global selections.
Exact ID `technology` renders supplied real icon evidence instead.

## Icon and source-reference evidence

`interface/016_brilliant_scientist_hidden_technologies.gfx:4`–`:21` registers all eighteen `GFX_<technology_id>_medium` sprites under `gfx/interface/technologies/016_brilliant_scientist/`.
`interface/clone_system.gfx:9`–`:11` registers the three shared clone technology sprites.
All twenty-one texture files were found locally, and MCP reports every sprite and English name/description resolved.
The four Xeno PNGs, chemical grant PNG, predictive unlock PNG, shared clone access PNG, and alien base PNG were opened and visually reviewed.
This establishes real icon rendering and source-linked diagram content, not a complete production-art provenance/style audit.

- grants for `brilliant_scientist_xeno_chemical_control_tech`: [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f14db0b8a4617557df4804f497aa200bb99cd9e0ce1cd134858442b182cbc4f0/1714e945f0cc4696842dde279b9ae8c4aa83fe67fa05d6bf45e7ac8adbe35ed0/technology-grants-f45db9ce92be.json), [PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6cd3bc8035b257b1009133ae920af74620a0744c82ab1e3d42f480a5db463a58/eec2f43dfcf1c4b86db6a71638771002c37773a5472352653713cde5a82802af/technology-grants-f45db9ce92be.png).
  Local PNG: `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/6c/6cd3bc8035b257b1009133ae920af74620a0744c82ab1e3d42f480a5db463a58/technology-grants-f45db9ce92be.png`.
- unlocks for `brilliant_scientist_alien_predictive_warfare_tech`: [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94c594b56d54249ddaded29df41e3a5fd50f466b098546fa5c52736b8bf1fc5e/bf0dd456839db4ed8f3683fad367da7dbeee0e5de91a84edd14db584eb0d6f2f/technology-unlocks-f45db9ce92be.json), [PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41cad7767040e8524e4af5d90d880401662155f8982e507fd411cff35c3b5c2f/034e978bc4f9f3045b9a1e4b63d96be959cfa903a5b992bd4a9300436443e528/technology-unlocks-f45db9ce92be.png).
  Local PNG: `C:/Users/klimp/AppData/Local/hoi4-agent-tools/workspaces/mod_chaos_redux_ea3b2d67c2c0/artifacts/41/41cad7767040e8524e4af5d90d880401662155f8982e507fd411cff35c3b5c2f/technology-unlocks-f45db9ce92be.png`.

All individual render manifests below retain JSON/SVG/PNG resource URIs, content hashes, icon coverage, and exact selection.
The bounded local evidence JSON retains every request shape/result/validation/artifact, including the failed comparison.

| Exact selected ID | Current inspect | Current individual render |
| --- | --- | --- |
| `brilliant_scientist_xeno_chemical_control_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6a11947aa2b9532a703d137d8e34dd06a968c8b7f2f934d58bbaa85d424d904/58efad853830eb17e0d1bebd121ae5ae0cefa0abcf83d1e50c457ed7cb6046e2/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c16f4d3820a2bb871daba32752fae05837a3585a0cd7cda313ee3c110f2f8b2/21b6abc4b562a7ad8ec40d256d8971fc4120287e0ce9e82a2b4654f06b599bfa/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_portal_warfare_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30b2a50302338e9cd1d7456368902ee8486817292e6c1a60aad73d398d1bb4ef/830df9cb27e41de47437b065d90b28b0a5e12b1b6722d5afd24bf3af6f7c95a5/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6e44555baf5e2849ce6e0f4a48cf5d09b3d76a67b1a07e47ee5300059003eaa/793ef8b0feb2360e3dd6a85c442729944665aec47438c203bc24872fcf752800/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_clone_formations_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/520ec5a7d89db6022eff2181c41082894a549662fe267b8bce1a95966333277c/75a030eec60cc626e35b381dcbbf1ed2020b118ced33eab42313b5cf71029bf0/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ec0ed1e4a1fe99ea4db9effdfaa20494a0d37cc24e7a9f8f4a04fcd935e2244/1bbf48018cd98908fa4ea730a8fef75fc19b5f4483fedf07ad9e88407915bbc0/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_robot_formations_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1327031ff3a7480de54790d727b82b2a0f0dc073b14bc119e96d311ffc1cbb1f/e812bc1b46df41e97156cdbfc15c6b9c8cd8e1f326458cc72ef5e5b86d9238ba/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6fe9d0244f7065b8239481a7ed606cbc4fcf2460ee17fa081dbc71acd79202a/68abc915aeb16d0db25bd5749e27276a7dcdfd8a8a7d4957af722bc4c39e0246/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_paleogenetic_formations_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f2ae39a5534c70a0e2f2cb8411b2423d68f2cbbb93392f74e6b19a018f0c0fe/5153c7db0011d34e68e9b74dc507c734bb475b23bcb4fde425d2269da84a240a/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d36958c5f14724c36e5af3a2495973b7de90ab01801c97d32ccbae75215160b5/54b955b245227e8b74270ac2d423dee21d1f3022ffd64a07abb97c2fce158826/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_xenobiological_formations_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a174248ecd6b5e47ed2ba1e8e8368cf850a79f1c71004e1a8e7cccf93d69eb63/f05591a496750a9a94faf7f1da491038c7d3d20d44d7bd24c8e6995f055e3300/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d8a212b6c6268cdeffa1c867b107fcb5f78ed0f9a23d17a8331f6f023ec35a4a/09e2ef5d26d2d9acbd89b70780bc14fbd2774e9cda4f7aa9316d3f94fd8ceaff/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_xeno_neural_control_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36372d8c1791eddf0c6020996b248ab2e95c8adb305ded205bf0b77cf0508dc0/04f6911be321be8ddcae54ae3d8607eff8327317f17e054aca0e48d347bcff76/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0913003162f0a7e3f04408fc949b5c04e58b7da1eb8b55d823c56cf4458ea823/79ca0f46f68a43913e575ac509c60cd3616b2c163a7685358edec379a7749e6c/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_xeno_machine_control_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9825219ef21c887edf376e49a5cf822699b320a75809004e8d78eb0c6c3df81a/1ab12cfadb244d189fc4495f23ef1c6249c4fae7c1677298e1488c1db2098ba2/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/248c6844a9adccd85b8b6dfac319dd44b12fe2eda34dc22d919710b15bb5a18b/0d912ba2c665f7982e48a538d4aedb20db700e3d841f0429f98a44af60c0a4de/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_xeno_researched_control_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b09641bcd7f297dd947ebb5d4ec7adce37bf9b6c7c598ad4554c8394b73b86b1/99f87ce11e62a7d082e7343d16b8790c991a826d3230eeaff83b77c70f4f04fb/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6f7b7cf5c87a9da0a442d6af68f44dd8ee9b538cd87a628671f8d69bc8901ef/dba8eb3f8b914d8123f044d4a5b7292447ed4324313509bef561b06df506a866/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_temporal_guard_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a85e41f211d5b55bd1f1b678e2d10748c29408129316f7a3f9be7915ed9ddd73/5791fd784cd1c542e74b05cbbc244abf6c837bcfc453b53cdf18a337a75c577a/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0f6dd00231be551d91751823e8cb8be9fc7d3b77be43645130cc1340999420b/b942abbb68b5df0f7d07efa65fb5c14eed960fdb89c0de3d686051c43bf28c37/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_alien_infantry_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/442fd478ef00dc287902a4e8af9b9fc2cde5616e31f5d106a4a6310d2bd73f2d/76ff5c322e01b47562283db8f7675a96f4b1c9607eb133f6c7a16f4eb156eed0/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4fec8f4ec0e5a69d63d8fe83e4b72ed7dee74f548244e7e125b8e6bf836a546/959a1ef7c959f5a787c0fa81bc5c065b0e9be8380b0156f59154021c6ff451e9/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_portal_warfare_weaponization_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5993503227b2a064396362c0a4ec24849a1d01f67e671e047fe2c82c935a719/b008ee25a33e4f8e6c24cb8c3210900811989187cd1ce4bc8fbd3550b7380bf0/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/803d439242a1b66591673b947d6f6875037bae2a8735091b74fb144c38721d56/40ed9cd8a334a6b799160988347f3c12f5635c7ed55276eb55cd9e144b21951a/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_clone_formations_weaponization_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc19daa50910b190421162aaf12980cb622182729f0b3032ee75787582a5a10b/7e32edcbd8d0ac0dd7e0549344354d72a201a30c6e531eb1c60c1c2fd6a58ea8/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b40d4b357d2ff1453abead7f9b816d4f6a9199cc28908280b4e620fdd0b18aee/0f30591ecd28dea189f5d97e35b0bd3c4eee57982dc40b4d25438bb0af084d13/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_robot_formations_weaponization_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/239cda87ab2cb828dfb2bbb12b1ffdf91fb8daec580f82ea51ff8d43df1815df/72ed52fc420391ef43b8d2634e5a7602800de5fb1749b09121699eb5b04d083f/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/274671ad7ed9a473357db6c04a0af0724997f8969cf640a3961365e632d38dfe/98a643436857e76e2db40abd5df3ca9f1fdca55e7a865ebaec83842fed35f20c/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_paleogenetic_formations_weaponization_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81772f7c57aef17ad3b07ffeb417eece2c9b314966f12798076cb758deff9373/6baf33e1cf37e381faf8aac61c91e631493b87eb6b332aab17791c0ec5655622/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e500d2adc024841a207e5ade983eb77a92ba5bf4fa5d7bbe7b4a506ac2f5724/0b20cb6c70fe097a82c8de705929d33583a7f43461c2332c4efd81bcaf2038a0/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_xenobiological_formations_weaponization_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/372203ddd68d347d14dbb05ec6a46a293d5118c28823b294a5118be1a376c97d/54353dc6b4a93fe6d70df11a79500f78f57ca80f2c755a8767f149544d1001aa/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0520097d55babf3a47336af895664fea924f7d83fd3570787609ab51fcf654b/7b5c97ecf2f32023a4fa3430d2e8763b6aceda5fce4df6229aa3d4eb37041447/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_alien_predictive_warfare_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63d21ba8e6afd86c56d9046d51675c0b363bedf2ce2782fa8af5f0341584fc54/89fad3420f3272d23894481a7242207844b259080b48e03d476843c0ba4afc21/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e3b42e8b010eb2ed3a5a57fc43d6011043a37031782395e293d29da21c1645f/ba334e7169e9f1bf4c28459bae3ecd866d90cfc7544a56522705ca04f20de3a7/technology-technology-f45db9ce92be-manifest.json) |
| `brilliant_scientist_temporal_guard_weaponization_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad23f609d64946db008e81eb7f1c132076b2215dce27e25ba5d926c65139c682/5cac345f93953eef31b43ec4267b936f5cdb7a551f2f06630efb6db802cf7013/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f246d7bbc2e9e33a292cac653323bdb7f625e9c44a33290be1e6982295de2e6/db6a95da3ca713e427f8a218a8f77a99fdaef2693651667f1daac190e83a620a/technology-technology-f45db9ce92be-manifest.json) |
| `clone_infantry_access_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1cdc09b19130f157b239501183c3fbaa1203859a30f452c88f51da594bcde965/d2bed2100490636678339d6f92b41103578fe97fe1df040282a06d347a48e3d2/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cdd641bdfc276c327e3db8278c821f3bd334e7051c46018e3fb92c7aa8ae1a59/8da0378cd554981e8b2d6ba9f162af713af9b53379da4fdbe08fc3da5f2b1b60/technology-technology-f45db9ce92be-manifest.json) |
| `mengele_clone_refinement_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea74021ce56c43a25b71808f8f2489476df12e3ca10fc599002c084e067bfd7e/50889820d4f3edbb1a2a827222da9886908db2ac62065a59de139f9ba248665e/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/70987749720a975a5f6dbf5e8fc51bfc9ac22dee98fcb4d4991bbc95fc1f4c2f/a38ae5de95c38d2bca5afe639ecfc894f059a4b1033f7ebb5b1cc2e2e6cb9746/technology-technology-f45db9ce92be-manifest.json) |
| `mengele_aryan_clone_refinement_tech` | [Explain](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b3a36990c4625dfa2465c1d0ae6f7f37c4bb3e1902f000067c9ea702a747eab/dbbe028e4c6282f825a7ccd8ebf23d7685f2f6984de847f87e17428299aadb9f/technology-explain-f45db9ce92be.json) | [Render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9724b0edc3ad51ee31fafdabb13baa79270fc3b4d559b432b47c1d0ee543ed04/6d9bc344676aff0b273abcc2c450b1f66b7d38cae55f91e00dd3b4aefc036e56/technology-technology-f45db9ce92be-manifest.json) |

## Capture clock and hashes

Initial local capture: 2026-09-02 16:36:05 +03:00.
Source-consumer capture: 16:39:41 +03:00, HEAD `227b1432a70464b307d666f560c5675afdffe75f`.
All tool evidence had been returned by 16:45:14 +03:00.
The three technology source hashes were reread at 16:45:41 +03:00 and remained unchanged; they exactly match each respective MCP technology record.

| Path | SHA-256 |
| --- | --- |
| `common/technologies/016_brilliant_scientist_project_technologies.txt` | `60bf2225fa86b235ee30898a9b1d19383d6d89af72613764fd1a72d75ae7548e` |
| `common/technologies/016_brilliant_scientist_project_force_technologies.txt` | `8b0129a6b71ffcb5ad5d4ef354329d3ed10b18919d0849922a52763049f3f1d0` |
| `common/technologies/clone_technologies.txt` | `a78527473911e0de61275be813b632ba91a4fc002adc3d967159b0b23d6a9e55` |
| `interface/016_brilliant_scientist_hidden_technologies.gfx` | `71a07ec57c50fcff84fd19347baea6f3c65ba4e91515661663dc3e3636e56cb1` |
| `interface/clone_system.gfx` | `44edf27ebdf68d3e0fa5530a49023cb4e3778ab42f8e3e8c98ce3395a0568d2b` |
| `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt` | `4aa4cb9bae94a76b8f33a5ea37f76e3c1ab040168fb688c7b9cd4a3c9eb6d3e1` |
| `common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt` | `ede44be51d047929e45de9edbf59d5064c98983e5a914c46f0d7fc31b58aa19b` |
| `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt` | `da6bb0f953985df30e13952f1891739c68e8904628a900a3387b1a5b93d5c974` |
| `common/scripted_effects/016_brilliant_scientist_project_effects.txt` | `d058ff42828df16e43083be79076577121d663c6031ff0b27cba6576a1ccd37f` |
| `common/combat_tactics.txt` | `68fd04bdc00a562135b761f700584a04ee62881dc934d9e6088090c32031c0b9` |

Helper source hashes describe the local consumer read at that clock, not a promise that concurrent helper owners made no later change.

## Required references and final disposition

Read guidance: AGENTS.md; `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, and `chaos-redux-event-planning`.
The skills' requirements caused exact selected-resource review, source/engine separation, icon-reference checks, and preservation of comparison blockers; no skill was changed.
The offline core wiki references were consulted, with Technology modding's allow/effects/unlock/dependencies/icon sections and Doctrine modding opened for this task.
Offline Effects and Modifiers remained the parallel syntax references.
Installed vanilla `documentation/effects_documentation.md:7805` confirms COUNTRY `set_technology`, `documentation/modifiers_documentation.md:2157` and `:2692` documents trickleback/experience-loss modifiers, and `common/doctrines/_documentation.md` distinguishes current doctrine systems.
Vanilla `common/technologies/infantry.txt:1206`–`:1244` supplies grant-only `allow={always=no}` precedent; vanilla root-level `common/combat_tactics.txt` supplies the tactic-definition precedent.
These selected records are technologies, not legacy or modern doctrine branches.

No simplification or fallback was introduced by this audit.
Source content and current selected inspect/render coverage are accepted within this bounded task.
Comparison, dependency/control-policy semantic graph proof, nested-stat analysis, and tactic target resolution remain explicitly incomplete.
Parent owns final evidence disposition, probability certification, broader asset/runtime acceptance, documentation integration, and completion/commit claims.
