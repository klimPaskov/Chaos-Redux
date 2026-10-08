# Public Works native architecture review, 2026-10-08

Disposition: completed narrow read-only architecture and source review.
Historical WIP findings and intermediate failures below remain evidence, with their current dispositions supplied by the closing verification sections.
This disposition closes the assigned review and does not establish full Public Works or Event 35 completion.
Acceptance basis: the current parent assignment authorizes a fresh read-only Public Works audit after prior agent `01a117ae-48c1-7ba2-a2ff-a7c5b7221dbc` returned authoritative NotFound without a handoff.
The parent retains implementation ownership and the full Event 35 goal.
This review makes no gameplay, GUI, asset, Git, spreadsheet, or skill changes.
The sole authored file is this handoff.

## Findings requiring parent action

1. **Replace the unverified connection token.**
The inspected owner trigger and effect use `is_connected_to_capital`, but reference search found no native documentation and source lookup found zero scripted-trigger definitions.
The whole-file MCP check returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, with two unresolved instances in the earlier four-root trigger revision.
Later source reads also show the token in the frozen-partner validator and neighbor selection.
Use an actual `has_railway_connection` from the paying country's capital to the candidate neighbor, including a deliberate capital-state identity case.
The documented `is_in_home_area` means land connection of the first province to its owner capital, so it is not equivalent railway proof and was not adopted as a substitute.

2. **Housing and abandoned works currently certify their own flags.**
The inspected finish helper sets `great_depression_public_works_housing_proven` or `great_depression_public_works_abandoned_conversion_proven`, adds `great_depression_public_works_housing_recovery`, then the physical-target trigger accepts that flag.
The recovery modifier supplies construction speed and local supply.
This chain has no frozen pressure or abandoned-burden baseline and no measured reduction of that baseline.
Require a real positive need at preparation, its exact state/episode source, accepted work, and a material verified change in the existing pressure or burden consumer before success.
A national demand total alone does not attribute relief to this state because other states and policies change that total.
Use the existing mapped state contribution and stage ledger to establish the local change.
Keep housing and abandoned conversion distinct outcomes, retain their mapped durable state legacy, and grant no factory or slot.

3. **Strengthen repair proof against physical building removal.**
The inspected helper correctly records positive `damaged_building_level@<type>` and sets a target of `max(0, initial_damage - repair_amount)`.
The trigger then requires actual getter reduction, which is materially stronger than accepting a repair modifier.
Also freeze total building levels and require preservation at certification.
A fall in damaged levels after demolition or physical loss must not count as repair.
Validate presence, positive initial damage, nonnegative target below the initial baseline, exact repair kind, and continuing authority.
The installed getter is in damaged building levels, not a percentage or construction-points measure.
Do not convert `BASE_FACTORY_REPAIR = 1.0` into one full building level per day.

4. **Complete the owner integration before publishing success.**
At the recorded source revision, `035_great_depression_effects.txt` still completes Public Works after elapsed work and applies its recovery modifier and project count.
The wrapper in `035_great_depression_decision_effects.txt` still pays and authorizes without calls to the new preparation, binding, or finish helpers.
Search over those two files found no direct references to the new helpers.
The parent was actively constructing the owner files while this review ran, so this is a revision-bound integration finding, not a claim about later parent edits.
Keep the successful native result gate before completion receipts, reopening credit, inherited-liability settlement, national relief, and legacy counters.

5. **Bind identity and issuance to the full paid transaction.**
The current plan predicate checks plan episode, authorization, kind range, ownership, and control.
Binding still needs current registration, coherent active crisis, project episode/type, an unspent authorization, and a fresh matching payment witness.
Retain payer identity and exact site identity alongside episode and authorization mirrors.
An existing positive authorization number alone is not proof that this call paid.
The once-only `result_issued` marker is a useful guard, but its authorization must match the current plan before it blocks or proves anything.
Stale flags must not block a later paid project or certify another episode.
The proven marker must likewise match the exact plan and result.
Never mint a proof from an old already-used receipt.

6. **Use the frozen rail neighbor throughout.**
The inspected neighbor loop retains the first valid neighbor by refusing a second assignment once the site has its partner variable.
This follows the requested deterministic selection and avoids random target weights.
In the site -> neighbor -> country traversal, `PREV` is the neighbor and `PREV.PREV` is the site.
On returning neighbor -> site, `PREV` is the neighbor to store.
At resolution, site -> payer-country gives `PREV` as the site and the stored typed state pointer as the partner.
Require current ownership and control of both endpoints, actual partner-capital rail connection, adjacency, exact plan identity, no existing satisfied connection at preparation, and native buildability for the same pair.
Use the identical country path restrictions at buildability, build, and proof.
A negative default controller path cost plus an allowance for only the intended payer is documented path rejection behavior, but its exact dynamic identity predicate and current province control remain native-validation limits.
`build_only_on_allied = yes` alone permits allied ground and does not establish owner-only routing.
No state-pointer arithmetic or broad route reroll is authorized.

7. **Finish bounded construction and repeat protection.**
Infrastructure target is frozen from the initial level plus one bounded gain.
Port and anti-air targets are fixed missing-capacity targets.
At accepted resolution, compute the nonnegative shortfall against that frozen target and emit at most one level once, then read the native getter.
If external work has already met the frozen target, emit no extra level.
If damage or removal has widened the shortfall beyond one level, emit at most the accepted level and withhold success until the exact target is met.
Respect actual building maximums, coastal province placement, and current control.
For naval bases, a state aggregate getter does not prove the selected port location, sea access, blockade status, or an actual convoy route.
The parent must either name the exact intended province and verify its consumer or keep those port-connection claims unresolved.
Keep physical issuance and lifetime state returns across transfers and episode cleanup so later episodes cannot reset a construction grant.
The current `infrastructure_cap` tuning exists, but target clamping and a concrete diminishing-returns policy need owner wiring rather than reliance on the constant's presence.

## Proposed helper map

These names keep the parent's current owner file and existing helper names.
Additional names are proposals for local completion and cleanup, not newly implemented declarations.

| Helper | Scope and inputs | Outputs and side effects | Direct call sites |
| --- | --- | --- | --- |
| `great_depression_public_works_has_recorded_need` | STATE, ROOT is payer, current registration and native getters | Pure eligible-need predicate, no persistent writes | Public Works availability and preparation |
| `great_depression_public_works_has_rail_need` | STATE and candidate neighboring STATE, payer capital network | Pure exact missing-link predicate | Need predicate and preparation |
| `great_depression_prepare_public_works_plan` | STATE below payer ROOT, no active project | Freeze kind, payer/site, episode, native level/damage baseline, target, rail partner or real local burden, prepared receipt | `great_depression_launch_regional_works_program`, before debit |
| `great_depression_bind_public_works_plan` | Same STATE, fresh exact paid authorization | Bind immutable plan to authorization, activate only applicable repair treatment | Same wrapper after successful authorization |
| `great_depression_public_works_plan_is_current` | STATE plus exact payer/site/episode/authorization and project type | Pure identity and continuing-authority gate | Process, finish, result predicates |
| `great_depression_public_works_rail_plan_is_valid` | STATE with frozen partner | Pure ownership/control, adjacency, capital-network and pair-buildability gate | Rail issuance and certification |
| `great_depression_public_works_repair_proof_is_met` | Repair kind, initial/target damage and total-level baseline | Pure measured repair proof | Finish after accepted work and final completion |
| `great_depression_public_works_physical_target_is_met` | Frozen kind and target, exact issuance identity | Pure getter/pair proof, with distinct measured housing/burden branch | Finish and final completion |
| `great_depression_finish_public_works_result` | Current paid STATE plan with accepted work | At most one bounded construction or rail mutation, verified outcome receipt, no national success before proof | Public Works branch of project processing |
| `great_depression_public_works_result_is_proven` | Current plan and proven authorization | Final read-only result gate, optionally recheck current output | `great_depression_complete_center_project` Public Works branch |
| Proposed `great_depression_suspend_public_works_plan` | Exact lost/paused STATE transaction and recorded payer | Remove active repair boost, retain partial work and immutable plan, stop payer commitment | Transfer, doctrine pause, project pause |
| Proposed `great_depression_clear_public_works_plan` | Exact state transaction with acknowledged failure, cancellation, or completion | Remove transient treatment and input fields, retain durable issued/proven history and appropriate legacy | Failure, cancellation, recovery cleanup, transfer adoption |

There is no need to turn this owner logic into a new global router or to duplicate the shared dynamic damage helper.
`damage_state_building_dynamic` implements damage and does not supply a documented repair contract.
Its owner API and docs were inspected.
Document these owner helpers in `035_great_depression_public_works_effects.md`, with an owner API link in the shared registry docs if required by the repository convention.
No helper documentation was authored by this subagent outside this handoff.

## Constants and tuning plan

The parent has created integer `great_depression_public_works_kind` values 0 through 9 and a fixed-point `great_depression_public_works` group.
Observed values are repair amount 1 damaged level, repair acceleration 2, infrastructure need floor 3, infrastructure cap 5, map gain 1, port target 1, anti-air target 1, railway level 1, proof grace 28 days, housing population floor 1000 thousand people, housing pressure floor 1, allowed path cost 1, denied path cost -1, and owner addition 2.
These are observed tuning, not balance approval.
Continue using the existing dynamic project-duration quote and its accepted work/certification split.
Use separate accepted tuning for housing/local-burden relief and persistent state return limits only if existing mapped values do not suffice.
Do not infer free building levels from repair acceleration.
Script constants require schema-first categories and are supported only in documented fields.
Native argument validation did not prove constant acceptance in every construction or railway field.
When necessary, pass constants through documented variables or literal meta substitutions under owner control, preserving the frozen target and exact units.
The probability owner retains baseline, patch, and compare evidence for affected eligibility or AI surfaces.
No probability inspection or duplicated audit was performed here.

## Event targets, ROOT, PREV, and cleanup

For targeted decisions, ROOT is the paying country and FROM is the selected state.
The current `FROM = { owner_helper = yes }` entry legitimately retains payer ROOT.
Entering another country from a foreign callback does not rebind ROOT.
The native control-change callback retains new controller ROOT, old controller FROM, and changed state FROM.FROM.
Do not invoke these ROOT-dependent project helpers from such a foreign-root chain without an explicit actor contract or recipient-rooted event.
If a country helper enters its stored project state, PREV at that specific entry is the calling country.
Use that relationship only where the actual nesting proves it.

Persist asynchronous plan identity and partner through state-owned normal scope pointers and mirrored payer receipts.
Regular event targets are useful for one synchronous transaction but can be overwritten by nested work and do not replace durable project storage.
No new global event target is necessary.
If an existing global target is used, clear only the exact matching owner's target, never another living actor's selection.

Suspend removes the active repair acceleration immediately on loss of valid authority.
Failure/cancellation consumes the exact failure receipt once and settles only proven paid/unspent amounts under the existing refund contract.
Completion freezes the result and legacy before clearing transient plan fields.
Adoption validates original payer, old episode, exact site, progress, issued/proven authorization, new holder, and successor episode.
It must not transfer the old country's doctrine or fabricate payment, national credit, a second refund, or another map grant.
Persistent construction history and diminishing-return state survive normal center cleanup and permanent transfer.
Preserve compact completed history, completed work, and the mapped state legacy.

## Migration and validation contract

1. Extend the existing read-only target predicate with real need while preserving current registration, selection, stage, doctrine, cost, and cooldown rules.
The inspected existing Public Works target predicate requires a Reopened center, which excludes a center that is currently Abandoned.
The abandoned conversion branch therefore also needs deliberate accepted target-stage wiring.

2. Prepare need before payment, recompute the coherent cost quote, debit once, authorize once, and bind only the fresh receipt.
If either authorization or binding rejects after debit, follow the existing exact refund/cancellation contract without publishing success.

3. Reuse accepted elapsed-work accounting and pause/resume rules.
Call finish before generic completion.
Keep failed native proof in a bounded certification state or its documented failure path.
The observed proof-grace tuning is not sufficient until that lifecycle is wired.

4. Award national relief, project count, reopening credit, inherited-liability settlement, and final legacy only after native or measured local proof for the same transaction.
Lasting-capacity conversion must consume completed Public Works evidence and create the mapped durable result once.
It must not create a second native building merely for consuming the first project's receipt.

5. Wire suspend and cleanup into failure, project pause, doctrine switch, state loss/regain, permanent transfer/adoption, national recovery, and invalid actor cleanup.
Keep exactly one live owner and preserve the physical work.

Required meaningful source scenarios for the parent are positive repair, unchanged damage despite modifier, fractional damage below one level, demolition masquerading as repair, bombing during work, external completion before resolution, building maximum, one-level issue with a larger post-loss deficit, same-call/repeated-call completion, stale issued flag, stale authorization, missing payer, foreign ROOT, state loss/regain, successor adoption, two valid neighbors, no valid neighbor, hostile intervening controller, partner capital-network loss, zero housing pressure, local housing relief despite unrelated national worsening, real abandoned burden conversion, and repeated episode diminishing returns.
Tests must execute production helper chains and model temporary-variable call-frame cleanup.
Caller-preinitialize any output scratch that survives a helper return.
No actual-source execution tests or live-game scenarios were run in this read-only review.

## MCP evidence and unsupported coverage

The exposed reference, source lookup, decision, event, map, and script-check routes were called successfully, apart from explicitly recorded argument or lookup errors.
The configured launcher is `npx --yes --prefer-online hoi4-agent-tools@latest`.
Configuration names `C:\Users\klimp\AppData\Roaming\hoi4-agent-tools\config.json` and workspace storage `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces`.
The connected server version and native task negotiation were not verified.
No helper-expansion, job-inspect, job-cancel, or native task route was used.

The old parent cells 211 and 214 are reported NotFound in the assignment.
Their request outcomes remain unresolved with no recovered snapshots.
This review does not label those requests failed and does not replay a mutation.
The prior agent's authoritative NotFound supplies no findings to inherit.

- Map lookup: `MAP_LOOKUP_COMPLETED`, revision `846e644a9688dee87d1ad4f3fa7b794f0dea3a32a3baafa0578474f0c82a5f47`, exactly two states 64/65 and province 6521, lookup-only.
State 64 has owner GER, capital province 6521, infrastructure 4, civilian factories 4, military factories 5, anti-air 2, and population 7,265,029.
State 65 has owner GER, capital province 514, infrastructure 4, civilian factories 7, military factories 2, and population 5,592,576.
Controller fields are null in this offline lookup.
Province 6521 belongs to state 64, is urban inland land, and is in strategic region 8.
The selected result contains province/state inventory and geometry, but no selected adjacency, supply-node, or railway-network proof.
Those requested coverage items remain unresolved under lookup-only output.
No second map scan or rewrite was performed because the original request completed without a timeout.

- Decision inspection: `DECISION_ANALYZED_PARTIAL`, source revision `2bbc7c7345d4a1ccc1eb1444198b552f266bdcf8cf8d99fb78f3e41ac12501c2`, scenario `PW-NATIVE-CONTRACT-DECLARED-GER`.
The actor is declared GER with an empty state object intentionally used to discover missing inputs rather than seed a fake native outcome.
The report has `complete = false`, 100 unresolved definitions in the tool summary, and 200 unresolved cost entries.
Missing inputs include active flag, episode, severity, and other live state.
The reported affordability false is not a valid affordability conclusion for an actual country.
Nested helper payment is not surfaced as direct payment effects and therefore does not prove no debit.
The first scenario-free request was rejected by the live schema and was corrected.

- Event trace/render: `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, focused revision `db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5`, ROOT selector `chaosx.nr35.1`.
The actual source declares that ID, but the render returned zero selected nodes.
Artifact inspection confirmed `complete = false` and empty rendered nodes.
Helper count zero is the focused-analysis boundary, not evidence that this system has no helpers.
This run supplies no selected-chain render proof or full helper/lifecycle coverage.
No comparison baseline or before-source snapshots were recovered, and no event comparison was fabricated.

- Script checker: current owner trigger file returned partial native coverage and unresolved connection tokens.
A corrective native `has_railway_connection` scope snippet confirms command kind and COUNTRY scope, but returns `valid = null`, `parametersChecked = false`, and one unchecked argument block.
An initial attempt to bind reserved ROOT explicitly was rejected as `SCRIPT_BINDING_RESERVED` and corrected using a real traversal.
No parameter or engine execution success is claimed.

- Reference gaps: `script_doc` coverage has no indexed files.
The initial decision context omitted Localisation, which was subsequently retrieved and read by targeted revision-bound search/read.
The assumed installed path `documentation\scripted_localisation_documentation.md` does not exist.
The actual installed `common\scripted_localisation\00_scripted_localisation.txt:1-9` documents the scoped trigger/key contract and was read.
The named Africa pattern is mod source `common\scripted_effects\012_africa_action_effects.txt:3470-3485,6438-6475`, not an installed vanilla `Africa_action_effects.txt`.
That mistaken vanilla lookup was corrected.
Native `PHI.txt:2015-2027` and `ETH.txt:4114-4121` provide typed railway state precedents, and native `AST.txt:834-850` shows one-level instant building construction.
These source precedents do not prove a campaign railway, port, repair, or local-demand outcome.

## Artifact references


### Bounded map lookup

- `map-lookup.846e644a9688dee8.62e309c88d8841bb.json`, SHA-256 `8047e2077af15bb245b064795f504f6e9b519ec05fbcf346cd53c15b4d0525d4`, 248306 bytes.
  URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8047e2077af15bb245b064795f504f6e9b519ec05fbcf346cd53c15b4d0525d4/9398e63fdf78e2db1173ab98c5ad4d373af5b27beffebdd6e2e959d73750717e/map-lookup.846e644a9688dee8.62e309c88d8841bb.json`.

### Declared decision inspection

- `decision-49b1643218d391199b32a621.json`, SHA-256 `d38c781dde48da464d9652f00f42325ed3d02d9d75524ce64f47751ce1f9699f`, 1740647 bytes.
  URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d38c781dde48da464d9652f00f42325ed3d02d9d75524ce64f47751ce1f9699f/99c1d4ba90531f5359d76eda4e593f994344b0bfe77559c9085da98010abb550/decision-49b1643218d391199b32a621.json`.

### Focused event trace

- `event-trace-db07bcddfa36.json`, SHA-256 `d0ea253fedf7aaf61d28c05b290a3829dcb2699bd407461e44372cdc6f4e1d98`, 1081537 bytes.
  URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0ea253fedf7aaf61d28c05b290a3829dcb2699bd407461e44372cdc6f4e1d98/2a57f0a94e8378630dfcc4c97c1773d564f05f8de9cb7275254491e9379d7cf1/event-trace-db07bcddfa36.json`.

### Focused scope render

- `event-scope-db07bcddfa36-manifest.json`, SHA-256 `7fda5088ae4a70da21abef0a14396de189e60b546b31906a22d11276a9bbb553`, 46675 bytes.
  URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fda5088ae4a70da21abef0a14396de189e60b546b31906a22d11276a9bbb553/c65c22685012cd01e92ac8240efcb1c8cb4296f80ed0bb94f41fc4e294d54b2a/event-scope-db07bcddfa36-manifest.json`.
- `event-scope-db07bcddfa36.json`, SHA-256 `2dee8fbf75dc607ccd1f79bbaa7cd4671ce7ca694ae47288850ab9be506a2d67`, 44898 bytes.
  URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2dee8fbf75dc607ccd1f79bbaa7cd4671ce7ca694ae47288850ab9be506a2d67/7e02f7c5551b75614e68a6fecfb4c42adf17bc43a49837b9885133dfa5e8049d/event-scope-db07bcddfa36.json`.
- `event-scope-db07bcddfa36.svg`, SHA-256 `9face78761cb01baa688cdda6bb78157e2be60ebb26db28f874a3b2b250e4424`, 18775 bytes.
  URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9face78761cb01baa688cdda6bb78157e2be60ebb26db28f874a3b2b250e4424/ef285bf816f53ed0508e7b84dca0c7382406e918cd17099ba4858f2785fe9566/event-scope-db07bcddfa36.svg`.
- `event-scope-db07bcddfa36.png`, SHA-256 `202ea640104a6bef0ff4b518b21bd490d81f1ef347b82a323599a34cd87fc9ff`, 5119 bytes.
  URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/202ea640104a6bef0ff4b518b21bd490d81f1ef347b82a323599a34cd87fc9ff/fb212c4dcefb572ad8e05798138455cf062c1dfe1120dc7f360ab0cecf75a587/event-scope-db07bcddfa36.png`.

Map, decision, event-trace, and event-render JSON bytes were read from the configuration-derived artifact storage and verified against their declared SHA-256.
The event diagram PNG was not visually reviewed because the verified render data contained no selected nodes.

## Revision-bound reference ledger

- damage_building: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:3374-3416`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, section ID `6db20aa22013e093967eae30ec8f4fa33d9c1f43fbca091315b034443c978b48`.
- building_level: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md:1101-1103`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, section ID `01110bbd97da5ffd6b7bcc26612a1fb5e4171d22fbfcc88882058f5347bc7806`.
- damaged_building_level: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md:1118-1120`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, section ID `4ecfa4e7bcc36c7e298ee1f2308016575f6c23f7223abaaec180d430609b1b3b`.
- damaged_building_level: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:1676-1676`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, section ID `ba08074c66a3d36d91dd09d8487ab499712ca096db393e607996fef1a9d5fe9e`.
- can_build_railway: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:1884-1919`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, section ID `593767fb49f2a7ed9f71dfafbfaf4c3e12abe4eb54efd8503299eab16f140204`.
- has_railway_connection: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:4609-4627`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, section ID `257d687ea16038f7e20eb8846bd1a31054386789cc38552298840e99b9f24008`.
- build_railway: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:2535-2571`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, section ID `f4f3bfb9fe187d3769272ee5783393def3bd6eba9165e7037a7c111805bc5952`.
- build_railway: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:373-373`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, section ID `a5dd780d2d20cee4c05d97de2f412abbb8ff0cf320c71a3cb654124cfeca86e1`.
- <span id="state_repair_speed__factor"></span>state_repair_speed_<Building>_factor: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\modifiers_documentation.md:4879-4886`, revision `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e`, section ID `dc1005c4b89c5b75b4fa5ececd077f9672cbe76998b6093596a2dd9dd91211ef`.
- State scope: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md:1219-1226`, revision `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f`, section ID `f3989916e670d444c8c5e3f096ed5a3c7b022ea239fa6cae349f45a3a79e2ba1`.
- add_building_construction: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:839-847`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, section ID `a4c185544d8b359d172254e5d2dbdc4aa7acaa201bce1a9bd563d3a59d08bbab`.
- add_building_construction: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:3614-3614`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, section ID `0f817f631ed352b778d103b6ff8f00fabc89044d8c8dabb5746c943a3465ecea`.
- Event targets: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:263-269`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, section ID `35458d3ddf0b1a88c189b06b2950edf3407e2a3f5e6980657ee9665a997fce9d`.
- Targeted decisions: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:513-518`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, section ID `09d5949e5fe45735721cecc1a56ee07a277873591c4a5289b66d184e7658ce96`.
- Script Constants: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md:216-222`, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, section ID `c859ab9d6a857bfc830f89b36b004514b78ee454e001a80238a9d1f7b355ccd0`.
- Constants: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md:2-34`, revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`, section ID `48deec564822a81f6806514736148c344258acac56db7e9989998ed30dd26b68`.
- Scripted localisation: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md:656-705`, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, section ID `8466af7164ce523520ef7e725d7711b333cc284bf7a70f0eeb7834993db17bb8`.

Additional directly read local sections: offline Scopes 811-839, Data structures 270-325 and 425-444, Effects 1759-1761, Triggers 1961-1986, installed dynamic variables 1096-1179, installed decision documentation 1-46, and installed Script Constants documentation.
Native defines 751 explicitly describes base repair as 1 percent before factories.
The file hash for directly read definitions and source precedents is retained below.

## Source identities at review closure

Parent owner files changed during this audit.
These hashes identify the reviewed state and must be compared with the parent's eventual final bytes before applying the findings as final validation.

- `AGENTS.md`: SHA-256 `e6375b0aa386e510abd4a35677dccf2871e47f75c9f169e593d52f8c77feff28`, 48552 bytes, last write 2026-10-07T18:39:14.9621977+03:00.
- `.agents/skills/chaos-redux-events/SKILL.md`: SHA-256 `88037fc7f66e0d02c766ece6f381f12fc82cbdb4314caa4ce0bf909952c78f4a`, 102647 bytes, last write 2026-10-07T21:26:51.8404676+03:00.
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`: SHA-256 `2cce9d17fa69e19da18e400b7ea156c8328619928f60c020aa0b38c7c96ef83f`, 79564 bytes, last write 2026-10-07T21:36:09.9887022+03:00.
- `.agents/skills/chaos-redux-subagents/SKILL.md`: SHA-256 `0447c92781ff53befe897284dca64ee4b3edfebf8e4879bdd92a1e00f5eb5976`, 57560 bytes, last write 2026-10-07T21:40:23.6937421+03:00.
- `docs/specs/035_great_depression_specs/035_great_depression_spec_part_3_decisions_missions.md`: SHA-256 `cd2249d9e026fb4da98398f3cc475764b57000a18dc4ec0cbd4d3d8b0594df14`, 25430 bytes, last write 2026-08-28T15:14:10.8141453+03:00.
- `docs/specs/035_great_depression_specs/035_great_depression_spec_part_4_centers_recovery_repeatability.md`: SHA-256 `1be2f0437945b3479ebbc52ceed25284b5592771037c904ce21042fa69d2dc3e`, 17466 bytes, last write 2026-08-28T15:14:10.8191392+03:00.
- `docs/specs/035_great_depression_specs/035_great_depression_spec_part_11_achievements_acceptance.md`: SHA-256 `d1303136850f83926c6dab5f32a941967f6101f43cc669913fc9df18459a6def`, 29238 bytes, last write 2026-08-28T15:14:10.7966488+03:00.
- `common/scripted_effects/035_great_depression_public_works_effects.txt`: SHA-256 `ba1a040975639dd823f9912a90f15d09f108690f6821cc1359188b508895f3f0`, 14127 bytes, last write 2026-10-08T09:56:06.5248669+03:00.
- `common/scripted_triggers/035_great_depression_public_works_triggers.txt`: SHA-256 `96fb59774defed3db42fa01cb9a0b18c53163d24ba104c8d715cabed708ccabb`, 7923 bytes, last write 2026-10-08T09:58:15.5014871+03:00.
- `common/scripted_effects/035_great_depression_effects.txt`: SHA-256 `e0c992b2041df8638385119c337040a380d9ce01e7dbaf351ecec2944d047750`, 531617 bytes, last write 2026-10-07T20:39:05.8012543+03:00.
- `common/scripted_effects/035_great_depression_decision_effects.txt`: SHA-256 `f51d0f777c93f4a2ee22a1796a322bfa2dd7cf5d4e99044d1cbd4b313993af9a`, 154947 bytes, last write 2026-10-07T20:38:21.8857700+03:00.
- `common/script_constants/035_great_depression_constants.txt`: SHA-256 `9ffc391b87dea6ce1369ea98e6587ac47837bdf581366a130dbd23759ddf1a2a`, 34498 bytes, last write 2026-10-08T09:50:56.1814367+03:00.
- `common/dynamic_modifiers/035_great_depression_dynamic_modifiers.txt`: SHA-256 `be7196c998a7a69353ea367fe4610484c653fbeb9c699bb27223c267a2eb8742`, 9655 bytes, last write 2026-10-08T09:58:15.5040735+03:00.
- `common/scripted_effects/012_africa_action_effects.txt`: SHA-256 `646e6dbdcc5337b279ccc520ed2557a0fc368ae89d7474cf9cc002dc72c3c28d`, 539661 bytes, last write 2026-10-04T11:13:08.4873984+03:00.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/defines/00_defines.lua`: SHA-256 `405a24ce579815443cafe052cff1361e20c712ca8182e3f10ccbf45330dd4be4`, 405669 bytes, last write 2026-06-12T10:21:57.0968692+03:00.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/PHI.txt`: SHA-256 `468ae9a96eacd0e6339a810931a69c0228ad08eb652f8a0a0d58bcf48044a914`, 53918 bytes, last write 2026-07-07T14:43:13.5650659+03:00.

## Completed work, blocked work, and limitations

Completed: full required skill/AGENTS reading, Parts 3/4/11 review, existing shared damage API inspection, owner-source inspection, exact native/wiki rules, native and mod railway precedents, bounded map inspection, declared decision inspection, focused event inspect/render, partial native command/scope checks, artifact byte verification, and this helper/cleanup/migration contract.
Blocked or unresolved: selected-chain event render, full helper/lifecycle MCP coverage, adjacency/supply/rail network coverage in lookup-only output, native argument acceptance, actual repair/construction/rail execution, measured housing/abandoned relief, payer-bound cleanup and repeat protection, complete parent integration, matching final-source validation, and probability-owner evidence.
Skipped: actual-source execution tests because this is a read-only architecture assignment with owner implementation still in progress, probability analysis because another owner handles it, comparison because no recoverable before snapshot exists, and live game testing because agents are prohibited from launching HOI4.
No fallback, gameplay simplification, negative-damage repair, invented numeric state-ID conversion, free factory, broad map repeat, central router, or wrapper skill was applied.
The review is complete as an evidence-backed handoff, while Public Works and the full Event 35 goal remain unclaimed and require parent integration and review.
Skills used: chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents.
Skills created or updated: none.

## Parent follow-up and bounded repair-family confirmation

The parent explicitly reviewed all seven findings and is addressing them before runtime publication.
The earlier no-call-sites finding describes the initial WIP runtime files only.
Staged `common/scripted_effects/035_great_depression_effects.e35-works-review.tmp` now calls binding at line 814, native result finishing at line 868, and the Public Works result gate at line 882.
Staged `035_great_depression_decision_effects.e35-works-review.tmp` prepares the plan at line 790 before affordability/payment and authorization.
These are observed staged changes, not published-source or native execution proof.
The staged hashes at this follow-up were `d0b3189ef29b2d57730eb219f9d4c12575de31a325a8f8477fed6788a7468d28` and `18935491d13d638e3729c026660dec16c0ae6c1f1c11c1db0fab38e831a99d9b` respectively.
The inspected owner trigger now uses `great_depression_public_works_has_capital_railway` with native `has_railway_connection` and an explicit capital case.
Its follow-up hash was `aa12fc799a602417f6bdd1891694ae95919107390f1cc2e1b762ce47175f91cf`.

Exactly one bounded MCP reference read reconfirmed installed `documentation\modifiers_documentation.md:4879-4886`, section ID `dc1005c4b89c5b75b4fa5ececd077f9672cbe76998b6093596a2dd9dd91211ef`, revision `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e`.
It returned OK, identifies the `state_repair_speed_<Building>_factor` family as category STATE, and explicitly lists both `rail_way` and `naval_base` among modified types.
Therefore `state_repair_speed_rail_way_factor` and `state_repair_speed_naval_base_factor` are supported STATE modifier-family keys, alongside `state_repair_speed_infrastructure_factor`.
Offline `Modifiers - Hearts of Iron 4 Wiki.md:1219`, revision `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f`, independently documents the family as percentage repair speed in the state.
This proves the family/type/scope contract and does not prove actual repair, repair queue behavior, modifier constant acceptance, or getter reduction.
No map route was called again.

Remaining fine-grained implementation recommendations preserve the parent's stated design:

- Match every fresh paid witness and mirrored receipt to the same actor, site, project type, episode, and authorization before binding or credit.
- Require both total-level preservation and real damaged-level reduction, retaining baseline values through legitimate pauses and transfers.
- A repair administration term must remain absent until legitimate resume/adoption revalidates the current receipt, including when the project processing pass otherwise skips an inactive or invalid actor.
- Keep issued amount, authorization, kind, and frozen target after suspension, cleanup, and adoption so a repeated call cannot issue another level.
- Revalidate the frozen neighboring partner, its current capital network, and the same route restrictions at issuance and final proof.
- Measure housing/abandoned relief through the exact existing local contribution, independently from unrelated national demand movement, and freeze that measurement before generic completion clears or changes center stages.
- Keep the transient result gate before every completion counter and downstream settlement, and retain the proved state legacy before transient plan cleanup.

The parent's described payer, demolition, issuance, adjacency, local-burden, and pause/resume corrections remain acknowledged implementation work in progress until their final bytes and production-chain checks are reviewed.
No new mechanic design, negative repair effect, fallback, gameplay edit, or other file change was made in this follow-up.

## Published-contract final source review

Scope: the published Public Works owner helpers, predicates, direct launch/completion, local-demand consumer, adoption, pause/resume, and exact mission retirement.
The AGENTS and three skill hashes remain identical to the previously read versions.
Earlier WIP findings are historical and are superseded where the checks below show published corrections.

### Confirmed corrections

- The unverified capital-connection token is replaced by a native restricted railway predicate with an explicit capital case, and the frozen pair is checked against actual neighboring states.
- Preparation precedes the actual `great_depression_commit_country_action` cost path, which calls `great_depression_pay_action_cost` before relief and its action receipt.
Binding requires exact payer/site, current registration and episode, unspent project authorization, an authorization newer than the preparation snapshot, expected action count, and the current paid-action day.
- Repair proof reads both preserved total levels and reduced damaged levels for the selected building kind.
The reviewed owner code contains no deletion or negative-damage repair effect.
This rules out plain demolition as the source proof, without asserting observed native repair or historical demolition-plus-reconstruction exclusion.
- Housing and abandoned recovery now change the physical stage to Reopened and update its ledger before calling `great_depression_measure_center_local_demand` again.
The national rebuild at `035_great_depression_effects.txt:4623-4624` consumes that same derived local contribution.
The measured result requires positive initial contribution and strict reduction, Reopened status, and no Liquidated status, in addition to the outcome marker.
The measured helper does not read housing/abandoned proven flags, so the former flag-only circular proof is resolved at source level.
No factory or slot is granted by that local recovery branch.
- Published completion calls the native result helper and gates completion on `great_depression_project_has_public_works_result` before completion receipts and project credit.
Issued authorization, payer, site, kind, amount, and target survive transient clearing.
Matching issued authorization blocks another emission from the same paid transaction, including after adoption.
- Native mission timeout and the center resolver use the same Public Works failure path.
The exact mission retirement helper cancels/removes the matching mission, and its cancellation helper does not invoke the pressure-bearing generic mission timeout.
No second Public Works failure-pressure call was found in those reviewed paths.

### Remaining actual issues

1. **Proof grace diverges after a legitimate pause.**
`035_great_depression_public_works_effects.txt:363-365` initializes the proof deadline once as the project due date plus 28.
`035_great_depression_effects.txt:1121` later extends the project due date by accepted pause elapsed time without extending an already-created proof deadline.
The native mission synchronization recomputes its deadline from the extended due date plus 28.
Example: work is due at D, proof is pending until D+28, and a valid ten-day pause runs from D+20 to D+30.
Resume moves the project/native mission deadline to D+38, but the center proof resolver still sees D+28 and can fail immediately.
That pause is below the existing 28-day pause-failure threshold.
Synchronize an existing proof deadline with the accepted due-date extension once, or derive both deadlines from the same preserved due-date contract.
Do not reset grace on every pulse.

2. **Repair acceleration resumes one processing invocation late.**
`035_great_depression_effects.txt:1078,1092` updates the repair term while the state is still marked Paused.
The successful resume branch clears Paused through the stage setter at lines 1123-1124, but neither that setter nor the remainder of the invocation restores the repair term.
The adoption hook also sees Paused and therefore does not restore it prematurely.
After legitimate resume, invoke the same receipt-validated repair-term helper after the stage transition so the accepted work interval does not run without its intended acceleration until the next processing pass.

3. **Adoption overwrites original issuance episode provenance.**
`035_great_depression_effects.txt:1399` assigns the successor episode to `great_depression_public_works_issued_episode_id`.
Original payer remains, and this strengthens the successor episode's spent marker, so this finding is not a demonstrated duplicate grant.
However, the durable issuance receipt loses its original episode while retaining that original payer.
Preserve the immutable issuance episode separately from any live successor episode used for the repeat cap.
The state transfer episode is not immutable across multiple transfers.

Documentation remains unfinished: `common/scripted_effects/035_great_depression_public_works_effects.md` was absent at this review, and the main effects markdown has no Public Works helper API section.
The assigned architecture handoff documents the proposal, but should not substitute for the published owner's required API documentation.

### Review identities and limits

- Public Works effects SHA-256: `b821df56f7c30ecc49befb55a2204e5234142805beb19c3ae0bfa17d6a43356d`.
- Public Works triggers SHA-256: `b364c9845c66a7d7e9ba2e12ed1b9d1be4472d01242b8357044dc55c2c5063f9`.
- Main effects SHA-256: `8a43f78845a4414a6c3f65f65c50c91d18880336e7534c4491c10c1ba02c5ec2`.
- Decision effects SHA-256: `f29884873961b254d8357bbcf016fc0fcc111232642e41b2c95becbdbc082953`.
- Project duration effects SHA-256: `f19841558cf2e4472f515025c937ab9eeffa75dda8708f9c2fb303f260791cf5`.

Task-specific validation was read-only production-chain and dependency review, including measured local recovery, actual debit ordering, preserved-level repair proof, spent issuance guards, and shared failure/cancellation accounting.
No actual-source execution fixture or native game execution is claimed.
Fresh bounded source lookup and whole-owner-trigger native command validation were requested in execution cell 47 and remained pending when this section was first written.
Their outcomes must be recorded when observable, and pending observation does not establish tool failure.
No new map scan, probability audit, gameplay edit, fallback, or simplification was performed.

## Additional issuance, housing, and transfer review

The latest source replaces the raw-authorization finish guard with the current episode guard, recomputes local contribution immediately before recovery, accepts measured external local recovery, excludes Distressed+Protected alone from housing need, and permits native mission activation for an exact current selected paid unspent Public Works plan.
Those changes were inspected in the published owner source and decision-surface predicate.
The payer remains distinct from the successor live owner.
The earlier issuance-episode provenance concern is clarified by the parent's explicit choice that this field is a mutable spent-episode guard.
This clarification does not remove the stale-receipt adoption issue below.

### Remaining guard flaw reproduced through production helpers

The adoption rewrite at `035_great_depression_effects.txt:1398-1399` still checks only `issued_authorization_id == center_project_authorization_id` before assigning the successor spent episode.
It does not check that the durable issuance belonged to the transferred project's pre-adoption episode.
A retained episode-34 issuance with authorization 1 can collide with an episode-35 fresh paid project whose authorization restarts at 1.
Transfer that project before it issues anything, then adopt it into episode 72.
Adoption rewrites the old issuance to spent episode 72, and the corrected finish guard suppresses the fresh project's required construction.
Using the existing `PublicWorksTests.prepared/launch` fixtures and the actual reconciliation, selection/adoption, and project processing effects reproduced `stale_transfer_spent_episode 72`, infrastructure remaining 2 instead of reaching the frozen target 3, and no Public Works completion receipt.
This is a false spent latch, not a duplicate grant.
Before rewriting live plan identity, require the existing issuance to match the pre-transfer episode plus the exact transferred receipt identity, including authorization and site/payer where relevant.
A transfer test for an actually issued current project must continue to prove no second grant.

### Pause issues remain in the inspected bytes

The transfer test now present in `.tools/test_event035_public_works.py` manually invokes `great_depression_update_public_works_repair_term` after calling the production process helper.
That explicit extra invocation hides the missing production resume call.
Running the actual process helper alone after adoption reproduced `resume_paused False repair_term False`.
Restore the repair term after the legitimate resume stage transition, inside the production path.

The proof-deadline extension gap also remains: project due date is extended at line 1121, while an existing proof deadline is initialized only once in the owner timeout helper.
The ten-day pause during an already-running 28-day proof grace still has mismatched center and native deadlines.
A third source replay reached an unbound numeric operand in the fixture's downstream failure path and raised TypeError, so that replay does not establish complete failure/cleanup execution.
The deadline mismatch remains directly evidenced by the production assignments and the earlier explicit D+20 to D+30 scenario.
No production helper was stubbed to work around that fixture limitation.

### Evidence status

Owner-reported source-test results were not presented as this subagent's rerun results.
The inspected file now contains later-episode and transfer tests in addition to the reported 14-case pass.
The two targeted additional source replays above used the existing actual-source interpreter with declared native fixtures, in memory through `python -B`, and wrote no test or gameplay file.
These are source execution results, not native building, repair queue, railway, or campaign execution.

The previously pending execution cell 47 completed and was recovered.
Source lookup returned one owner definition, helper revision `ba5bcc198b797e36b2a0b1d9049a9b35e9f58276a44e3641c694eec75615a5bd`.
Native trigger validation returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, zero unresolved commands among 144 checks, 44 unchecked argument blocks, and `parametersChecked = false`.
Those results belong to that earlier requested source state and do not constitute final-byte parameter validation for later edits.

Latest reviewed source hashes: owner effects `a0477e08198514c3fd1ff256a2c81f7c81a389d3814f41fea7ca6f0f535e5f6f`, owner triggers `90eed3bd1ba7d118bf0cde6140c10b8c05699ff9f683460f9ec4c0abd62448cb`, and main effects `8a43f78845a4414a6c3f65f65c50c91d18880336e7534c4491c10c1ba02c5ec2`.
No global completion claim, map repeat, probability duplication, gameplay edit, new mechanic design, or simplification is made.

## Final verification of the three owner corrections

Disposition: all three reported runtime-source flaws are resolved in the reviewed published bytes.
This closes those narrow findings only and does not claim native execution or full Event 35 completion.

- Adoption relabels the spent episode only when both issued authorization and issued episode match the transferred project's pre-adoption identity.
An old episode's reused authorization therefore remains historical rather than marking the successor's unissued work spent.
- The unconditional processor entry updater still removes invalid repair administration, and the controlled processing branch restores or removes it after the actual stage transition/completion.
The production transfer test no longer needs a manual repair updater.
- The center proof deadline is derived from the current legitimately extended project due date plus 28 on each relevant check.
Native mission synchronization follows the same updated due date before the proof-timeout check.
Recomputation does not grant fresh grace from the current day.

### Narrow source execution results and test fixture gaps

The three new regression methods were run unchanged through `python -B .tools/test_event035_public_works.py` with explicit method selectors.
The original-payer/repair-resume method passed.
The other two methods failed at the reviewed test-file hash, for fixture sequencing assumptions rather than reproducing the corrected runtime flaws:

1. `test_adoption_cannot_relabel_an_old_same_serial_as_current_issuance` correctly observes that old issuance stays at episode 34, but advances the whole work interval before the first processing invocation resumes the paused project.
That invocation correctly treats elapsed time as suspension rather than accepted work, so infrastructure remains 2.
Process the legitimate resume immediately after adoption, then advance the accepted work interval and resolve.

2. `test_post_work_pause_resume_keeps_proof_and_native_deadline_equal` assumes seven days at Severity 100 sets the project Paused flag.
The current processor suspends on ownership/control or civilian-system invalidity, while Severity 100 contributes to the separate paralysis accounting and failure path.
Use a real existing suspension condition to test these exact pause/resume corrections.
A new Severity-driven suspension rule would be a separate gameplay decision and was not added or inferred by this review.

Two in-memory narrow probes using the same actual-source interpreter then verified the corrected scenarios without editing any test:

- Stale episode-34 auth1, fresh episode-35 paid auth1, transfer to episode 72 before issuance, process resume, advance accepted work, and resolve: old receipt remains historical until fresh issuance, infrastructure reaches target 3, and a completion receipt is present.
- Accepted repair work with proof pending, seven elapsed days, actual control-loss suspension, five-day pause, control restoration and one processor invocation: Paused clears, repair acceleration is present immediately, the proof deadline increases only by legitimate suspension, and stored center/native mission deadlines all equal current due date plus 28.

Both probes passed.
The probe used existing production effects without a manual repair updater or production-helper stub.
No full-suite result is claimed here, and the owner's 82-method run remains owner evidence pending its final result.

### Exact reviewed identities and limits

- Main effects SHA-256: `235c9a3775913c41dea22940a0ab4fcec7bb23d887d524256231e8bbf9c563a3`.
- Public Works effects SHA-256: `d3acdad33e4ccbf2df7076d549c6f0fa5841f68acdb18dc3b1c2147eac37e767`.
- Regression file SHA-256: `3f1b71d8d13c35448b45772807e94097042836730e34150c477f6f79aace630b`.

No remaining runtime guard flaw was found in these three exact deltas.
The two regression fixture corrections above remain needed at the recorded test revision.
Native parameter acceptance and actual game behavior retain the previously documented coverage limits.
Only this assigned handoff was edited, with no map repeat, probability work, gameplay edits, fallback, or simplification.

## Final actor-validity boundary verification

The parent reports that the corrected 18-method Public Works suite passed at the prior actor boundary.
That result is recorded as owner evidence rather than this subagent's full-suite rerun.

The three published gates were inspected: preparation, paid binding, and `great_depression_public_works_plan_is_current` now call `great_depression_active_country_is_valid` in ROOT country scope.
The underlying predicate requires country existence, normal civilian-system eligibility, exclusion from special and actual-nonhuman classes, and coherent active crisis state.
The stronger predicate therefore preserves coherence while rejecting the four specified invalid actor classes.
The surrounding payer/site, receipt, authorization, episode, current registration, and payment ordering checks remain present.
The main effects hash remains `235c9a3775913c41dea22940a0ab4fcec7bb23d887d524256231e8bbf9c563a3`.

The new `test_invalid_actor_cannot_pay_or_directly_finish_accepted_work` method was run independently with `python -B` and passed all eight combinations of missing/noncivilian/special/nonhuman actors and prepayment/direct completion.
The actual-source fixtures assert unchanged infrastructure, no additional resource debit, and no Public Works completion receipt.
No production helper was substituted, and no test file was edited by this subagent.
No remaining flaw was found in these three exact guard changes.

Reviewed owner effects hash: `980091b7c3a517a163f3a1c47057b0ea82f705b32e19d69eca97fcc6502f8d57`.
Reviewed owner triggers hash: `c204327cf9add639b31dd26997c8573eef738e278e96125b9215e3472f2deba0`.
Reviewed test file hash: `9dc45c5b5cb39b92a9153402f52015ca966d0715a636d412eaab59704efe9195`.

The parent's new 19-method run remains pending its reported result.
Native execution and full-event completion are unclaimed.
Only this handoff changed, with no gameplay, map, probability, Git, asset, or spreadsheet work and no simplification or fallback.

## Assigned handoff closure: actor and foreign authority

The enclosing repair-updater guard now permits mutation only when the state is owned by ROOT or its recorded live plan owner equals ROOT.
Inside that authority boundary, valid paid current plans restore repair administration and invalid, paused, or uncontrolled plans remove it.
A recorded original/live owner can therefore remove its invalidated term after control loss, while an unrelated ROOT or former owner after adoption cannot remove the successor's term.
The stronger active-country predicate remains in preparation, binding, and current-plan validation.
No concrete remaining guard defect was found in these exact actor/authority deltas.

Five current regression methods were independently run and passed: original-payer transfer/resume, stale same-serial adoption, corrected control-loss proof/native deadline synchronization, the eight invalid-actor combinations, and foreign-ROOT processor isolation.
The corrected adoption fixture processes resume before accruing work, and the corrected deadline fixture uses OCCUPIER control then restores the rightful actor.
Neither requires a manual repair updater.
A separate in-memory production-processor probe also passed after successor adoption: invoking the old payer as stale ROOT preserved the successor's repair term and live owner while retaining the original payer.
These tests execute actual source against declared native fixtures and do not establish native game execution.

The matching published owner documentation, `common/scripted_effects/035_great_depression_public_works_effects.md`, now exists and was read.
It documents the helper scope, immutable need and payment inputs, bounded native result proof, measured local recovery, transfer/cleanup, tuning and direct consumers, and explicitly retains native transport, refund, lasting-capacity, asset and full-event limits.
The earlier missing-owner-documentation finding is closed.

Final reviewed source identities: owner effects `d65f47b935cc472dedfbc01f6437b2051856cf5b3ab4ad8ad0dcb2edda677250`, owner triggers `c204327cf9add639b31dd26997c8573eef738e278e96125b9215e3472f2deba0`, main effects `235c9a3775913c41dea22940a0ab4fcec7bb23d887d524256231e8bbf9c563a3`, and regression file `7ccc0169c05ae76c14d5eb67f67644d54e1c0eaf84e5143206ea525b48b10df1`.

The parent's corrected prior 18-method pass is retained as owner-reported evidence.
The parent reports that the final whole-current-source suite passed all 86 methods in 102.797 seconds, including all 20 Public Works methods, 512 additive stage/treatment combinations, eight invalid-actor prepayment/direct-completion cases, and foreign-ROOT repair retention.
This is recorded as the parent's actual completed source-suite result, distinct from this subagent's independently executed targeted tests and probes.
The owner code is frozen, and a final SHA-256 check confirmed that all four source/test identities immediately above remain unchanged.
The actor/authority note and assigned narrow review are finalized with no remaining concrete guard defect found in the reviewed scope.
The parent's commit remains pending the probability owner's comparison, which this subagent neither duplicated nor marked complete.
Required native argument acceptance, repair queue behavior, railway/province placement, consumer rendering, save/reload and live campaign outcomes remain unproven under the earlier MCP/source coverage limits.
No HOI4 launch, log request, additional map scan, probability duplication, gameplay change, fallback or simplification occurred.
Only this assigned handoff was edited, and the narrow review is closed with the above limitations.

## Final paid-project-type isolation review

The parent identified and repaired a concrete generic-completion bypass after the earlier review closure.
The published `great_depression_project_has_public_works_result` now permits its non-Public-Works branch only when project type is non-Public-Works and both the active Public Works plan and paid Public Works receipt are absent.
Otherwise it requires exact Public Works result proof, whose current-plan predicate also requires Public Works project type.
Relabeling a paid Public Works project as finance restoration therefore rejects both branches instead of reaching generic completion.
The trigger is pure and does not alter payment, authority, or completed-project state.

Independent narrow source validation passed:

- The new actual-source paid-type-mismatch regression and terminal cleanup regression both passed.
- The existing ordinary finance-restoration producer/completion regression passed.
- Additional production-helper probes rejected the finance-type mismatch when either the active plan marker alone, the paid receipt marker alone, or both markers survived.
Each rejected invocation preserved buildings, reopened/project counters, and resource-debit count and created neither finance restoration nor a generic completion receipt.
- A completed Public Works project cleared both transient markers, after which the actual paid lasting-capacity action and processing completed successfully without another infrastructure grant.
This proves the unaffected ordinary non-Public-Works gate and legitimate post-Public-Works handoff at source level, without establishing the complete lasting-capacity design or native execution.

No remaining defect was found in this exact type-isolation change.
Current owner trigger hash: `6aecf24598d19608bf64c00479e674ccff2b7ce5f9eca25e058a60f52056ca80`.
Current regression file hash: `36214c332c7f07c737d314d9fbc420b225127ac9ed304acc0d9fa834dd974f57`.
Owner effects and main effects remain `d65f47b935cc472dedfbc01f6437b2051856cf5b3ab4ad8ad0dcb2edda677250` and `235c9a3775913c41dea22940a0ab4fcec7bb23d887d524256231e8bbf9c563a3` respectively.

The prior 86-method pass belongs to its earlier source revision.
The parent reports the final whole-current-source suite passed all 87 methods in 82.667 seconds, including the 21 Public Works methods and the new type-mismatch regression.
This is recorded as completed parent-run source evidence, separately from this subagent's independently passed mismatch, ordinary finance, cleanup, and post-Public-Works lasting-capacity probes.
Final filesystem SHA-256 verification matches trigger `6aecf24598d19608bf64c00479e674ccff2b7ce5f9eca25e058a60f52056ca80` and regression file `36214c332c7f07c737d314d9fbc420b225127ac9ed304acc0d9fa834dd974f57`, with the main/owner effects hashes unchanged as recorded above.
The narrow paid-type-mismatch review is finalized and this handoff is frozen for the parent's private-index rebuild.
The private Git index rebuild and probability comparison remain parent-owned and were not touched or claimed complete.
Only this handoff changed, with no broad native calls, gameplay edit, map scan, fallback or simplification.
The narrow review is closed while all previously stated native execution and full-event acceptance limits remain.

