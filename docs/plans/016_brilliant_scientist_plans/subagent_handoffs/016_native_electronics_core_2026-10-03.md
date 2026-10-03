# Event016 exact native Electronics core handoff

Disposition: implemented bounded helper extension; parent integration is present in current source and remains subject to parent review.
Acceptance basis: the parent explicitly accepted Electronics as fixed exact source sp_air_radar within the existing fifteen-family closure on 2026-10-03.
The parent subsequently required the fresh DLC gate after the localisation audit, directed integrated radar/adoption ordering checks, and explicitly broadened the owned core to fix conservative helper-output lifetime for every supported native source.
Native cancellation and same-project generations remain unresolved; this tranche does not waive them.
No implementation simplification was made, no HOI4 process was launched, and no commit or index operation was performed by this worker.

## Files changed and ownership

- `common/script_constants/016_mengele_native_prototype_constants.txt`
- `common/scripted_triggers/016_mengele_native_prototype_triggers.txt`
- `common/scripted_effects/016_mengele_native_prototype_effects.txt`
- `common/scripted_effects/016_mengele_native_prototype_effects.md`
- This handoff, `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_native_electronics_core_2026-10-03.md`

Only those five files were written.
Parent-owned decisions, presentation, localisation, CXT, radar project, and stage dispatcher were read for integration scenarios and were not patched here.
Foreign shared-tree work was preserved.

## Helper map and before/after behavior

Before this extension, the exact native ownership core supported Cloning and two Rocketry source choices.
Electronics reached its Prototype through parent aggregate/family callbacks rather than this source-selective provenance layer.
The additive core now supports exact Electronics code 4, family ID 2, durable index 1, and the original project ID sp_air_radar.

| Helper or group | Scope and inputs/defaults | Output and side effects | Integrated call sites |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_native_electronics_private_gate` | COUNTRY; no selector input | Read-only strict provider + Electronics Theory + incomplete private Prototype + existing literal empty Electronics paid receipt | Literal selection and auto-adoption predicates |
| `brilliant_scientist_mengele_can_select_native_electronics_radar` | COUNTRY; no selector input | Read-only private gate, either no held radar selection or exact completion, and exact completion OR both Gotterdammerung and electronic_mechanical_engineering | Parent radar selection decision requirement |
| `brilliant_scientist_mengele_can_release_native_electronics_radar` | COUNTRY; no selector input | Read-only selected radar + empty Electronics receipt + NOT exact sp_air_radar being researched; no provider-validity requirement | Parent radar withdrawal requirement |
| Source dispatch predicates | COUNTRY; temporary source defaults none | Code 4 added to support, literal select/release, exact completed query, selection match, fixed-source non-retired auto adoption; Rocketry-only conflict rule unchanged | Existing generic native API transactions |
| Request mapping, consume, retire, selection, cleanup | COUNTRY; supported source or original owning scope for cleanup | Source 4 maps to Electronics/Prototype/index 1; selection writes only its selected flag, consumption clears only it, release/cleanup retires it; history/observation/native research/paid receipts preserved | Existing generic native selection/adoption/release/provider cleanup APIs |
| `brilliant_scientist_mengele_native_output_electronics_radar` | COUNTRY synchronous exact country-output boundary; no source input | Always records exact observation; fresh-settled only after matching witnessed selection and private output; durable source/fresh mode and matching consumption precede radar retry; dedicated result restored to fresh_settled after retry | Existing sp_air_radar.project_output.country_effects, before parent radar marker and original technology grant |

The source/mode arrays retain their existing fifteen-slot append-only schema.
Electronics writes only index 1 after changed private Prototype output, alongside source 4 and fresh_output 1 or adopted_completed 2.
Its three flags are `mengele_event016_native_selected_electronics_radar`, `mengele_event016_native_observed_electronics_radar`, and `mengele_event016_native_retired_electronics_radar`.
Observed output remains a fact even if private settlement is blocked.
Adoption does not invent observation or replay native output.

The new literal wrapper calls `brilliant_scientist_mengele_settle_native_electronics_deployment_from_radar` only after fresh_settled.
The generic fresh/adopted cores never call that retry.
The parent exact adoption driver and explicit completed selection feedback retry only after adopted_settled, after durable provenance and matching consumption.
No source-only completed query authorizes a fresh output.

The wrapper owns nested mapping/output scratch storage.
For every supported source, the generic selection, fresh-output, and explicit-adoption frames own family/stage/index/project_output_applied/stage_package_applied storage before nested mapping/output calls.
Family/stage start at none; index and both output slots start at zero.
This fixes the documented lifetime defect while retaining the public source/witness input contract.
The five direct initializers deliberately stay in each consuming frame; creating those slots first in another helper would recreate their loss on return.
An outer caller consuming a temporary result must initialize its own storage before the helper call.
This contract is explicit in the API markdown, including initial values, defaults, side effects, and examples.

## Constants, tuning, event targets, and cleanup

The sole constant addition is `mengele_event016_native_prototype_source.electronics_radar = 4`.
It is stable source metadata, not a gameplay tuning value.
No cost, duration, ratio, threshold, AI weight, native project ID, technology ID, or existing family/stage ID changes.
No new tuning table is needed.
No event target or persistent numeric project pointer is introduced.
Selected/observed/retired state stays boolean country flags.
Successful fresh/adopted settlement consumes only matching radar selection.
Release requires inactive exact radar research and an empty matching paid receipt; it retires ownership without cancelling/refunding native work.
Existing provider/terminal cleanup retires held radar selection in the original owner scope, preserving observation, accepted provenance, paid receipts, and learned/native history.
No periodic world scan or fallback callback was added.

## Migration and current parent integration

The parent migrated Electronics alongside Cloning/Rocketry out of generic sync, generic record, and reused-completion scan.
The after-Theory exact branch passes fixed source 4 to the existing exact adoption driver and restores the enclosing Theory callback context.
Parent selection/release controls are `mengele_event016_native_select_electronics_radar` and `mengele_event016_native_release_electronics_radar`.
The parent owns visibility, the six localisation strings, costs/AI, and the existing icon `GFX_decision_brilliant_scientist_project_electronics_guidance_prototype`.
The literal helper's fresh Gotterdammerung gate matches the accepted presentation gate; completed adoption bypasses DLC and the fresh technology gate while retaining the private family conditions.
CXT's existing player-triggered ownership probe observes the three radar flags and index 1 provenance without creating work.
The API markdown records these integrated call sites, four sources across three families, source 4/index 1, and all remaining evidence limits.
No new art, model, entity, animation, icon file, or scripted GUI was needed.

The parent reported full installed radar source equality after removing its owned header and two hooks.
This worker separately inspected the actual country-output hook ordering and exercised that country-effect block in its source model.
The parent's source equality result is preservation evidence, not engine acceptance, and is not reclassified as an independent worker run.

## Meaningful source validation

Final driver results: 6,590 passing source-contract cases after the all-source lifetime correction.
The parent independently reran the current embedded driver against the current tree and reported the same eight suite counts.
The parent also reports that its original Cloning project change is exactly one result-preinitialization line, with the prior payload preserved.

| Suite | Passed | Relevant checks |
| --- | --- | --- |
| Electronics source cases | 869 | Fresh output before completed bit, absent/stale selection, provider/Theory/Prototype gates, all paid family stages and stored costs preserved, fresh DLC/technology versus exact no-DLC completed adoption, held completed-source adoption, retired automatic exclusion, explicit retired adoption, exact release research query, repeat output, matching-only cleanup, wrong witness, and private-gate DLC independence |
| Existing source parity | 960 | Actual-source Cloning/Rocketry selection, fresh, adoption, and release compared against immutable a23ea17; opposite Rocketry selection, exact completion, provider state, and every paid family stage |
| Conservative temporary lifetime | 660 | Helper-local temporary fields discarded on return unless caller-preinitialized; Electronics fresh output including nested retry and paid gates, plus generic selection/explicit-adoption forwarding with and without DLC |
| Parent integration | 184 | Actual radar country effects before marker/native grant, radio_detection already held versus absent, later named radio_detection callback, parent exact adoption driver provenance before retry, and enclosing after-Theory context restoration |
| Conservative Cloning/Rocketry | 2,880 | Actual select/fresh/adopt helpers with only source/result caller storage; provider/Theory/Prototype/selection/completion/opposite selection and paid-stage combinations; durable history and paid receipts compared to current flat model |
| Parent Cloning/Rocketry feedback | 240 | Actual selection/release adapters under conservative frames; correct feedback and adopted Cloning bridge call, with paid receipts preserved |
| Cloning history/bridge | 788 | Actual bridge gate over provider/Theory/Prototype/completion and absent/short/full source/mode arrays; original hidden Cloning country-output boundary forwards fresh history before the original consumer |
| Old-core lifetime regression | 9 | Each Cloning/Rocketry source demonstrates a23ea17 conservative selection/fresh/adoption failing, while the corrected core accepts the same input |

For output before the project marker, the literal wrapper first records accepted Prototype provenance, then attempts the already-seen radar pair if eligible.
The actual parent marker then observes the radar output.
If radio_detection was already held, its marker retry can settle Deployment at that boundary.
If it was absent, the original grant adds it, and the separately invoked existing technology completion boundary settles the pair in the source fixture.
No case changes the dedicated Prototype result or source/mode receipt when the nested later-stage helper clears selectors.
A sentinel at provenance index 0 confirms radar retry cannot redirect the Prototype receipt to the cleared/default index.
The adoption driver retry sees source 4/adopted mode 2 and consumed matching selection before running.

The source model executes actual owned helpers, existing receipt initialization, original stage request/predecessor/empty-receipt predicates, private stage output, cleanup, matching consumption, radar retry, parent country effects, and parent adoption functions.
It supplies explicit native completed/research/technology/DLC state and stubs the strict provider lifecycle predicate, availability reconciliation, dynamic modifier engine refresh, and conventional package-grant implementation.
The full custom operational bridge payload is stubbed; the actual Cloning source gate is evaluated, and parent feedback/output calls are recorded without asserting full technology or CBRN payload execution.
The Cloning native availability predicate is a shared true fixture input for both immutable/current parity models; its prerequisite logic is not re-audited.
The technology callback is invoked as a named later source boundary; the driver does not claim the engine notification order of set_technology.
The singularity initializer uses an already-initialized fixture marker, while actual fifteen-slot append behavior is retained.
Cloning/Rocketry flat-model parity compares persistent receipts/flags/modifiers and the dedicated result against a23ea17.
Only for temporary value comparison, absent and explicitly created zero scratch slots both read as zero, consistent with documented defaults; every other temporary value must match.
The conservative Cloning/Rocketry suite supplies no mapping/output scratch from the outer caller and discards helper-created temporary slots at every return.
Nine negative regressions reproduce the old missing-mapping/output failure and confirm the corrected core resolves it.
The actual original Cloning hidden country-output boundary is exercised before its original CBRN consumer; that consumer and the full neutral technology payload remain outside this driver.
No source test proves native payment/clock, live engine callback order, live grants, cancellation, or immutable generations.
The full executable driver is retained below rather than writing outside the five-file ownership boundary.

## MCP routes, artifacts, and unsupported analysis

Connected metadata exposes reference_context, reference_search, reference_read, source_lookup, event_inspect, event_render, and event_compare.
No hoi4.script_validate route was exposed in this worker's tool inventory.
The initial event/context requests produced no final response before their orchestration cell was stopped.
Narrow retries of reference_context (general, Script Constants, limit 2), reference_search (is_special_project_being_researched, installed game docs, limit 1), and source_lookup (sp_air_radar, one definition, 35 lines, no references) produced no response within each 45-second observation budget.
These are worker deadline observations, not proof that the service globally failed or that any server-side operation was cancelled.

The first narrow event request had invalid selector/mapping fields and maxDepth 0; validation returned the accepted discriminator kinds and minimum depth 1.
A second validation response required selector.eventId rather than selector.id.
The corrected request used `{ kind: "event", eventId: "chaosx.nr16.1" }`, maxDepth 1, maxNodes 2, maxEdges 2, and no helper expansion.
It produced no result within 45 seconds.
The event state render used the same event selector, depth 1/nodes 2, no helper expansion or HTML, and produced no result within 45 seconds.
The event compare used that selector, chain/render limit 2, render false, and default baseline/current inputs; it produced no result within 45 seconds.
No baseline graph or compare artifact was returned, so event-chain change coverage is unresolved.
Helper-expansion, job/task, GUI, focus, map, rewrite, and game-launch routes were not used.

The initial reference_read attempt passed the locally known triggers-documentation path/revision and bounded span; it returned no response within 45 seconds and did not establish a valid resource-id read.
After the parent supplied successful exact search evidence, this worker retried reference_read with section id `d94fad5f14dff54451fa80122aeca43fcec9506ff16676bd16ba26d221930162`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, start 6228, maximum 29 lines.
That worker observation also expired after 45 seconds without a result.
A second attempt used explicit workspace `mod_chaos_redux_ea3b2d67c2c0`, the same exact section/revision, and maximum 16 lines; its result is recorded in the final evidence note below.
No successful worker artifact URI or continuation URI was available for those timed observations.

The parent separately reports successful narrow reference_search for the exact trigger section above and a broad context 600-second timeout.
The localisation auditor's `016_native_electronics_localisation_2026-10-03.md` records successful reference_search (wiki id `23b392819270baa9ee7540f4d1fd1ebcdf8c847dadde883ac18647e0bf607213`, Localisation 276-346), reference_context with no missing/omitted sources, and source_lookup for electronic_mechanical_engineering (source revision `feafdd59697315e7900b0153161a6e7d1c84d8c75c1aa0f406ded13b6300417d`, mod 20-27/vanilla 16-23).
Those attributed results establish individual route/source evidence and refute a global-outage claim.
The worker read required local documentation directly and retains spans/hashes below.
Neither a context bundle nor source-only review is represented as equivalent engine evidence.

No weighted helper or AI policy was edited by this worker.
The parent selection decision AI remains outside this ownership boundary and requires its own chaosx_ai_probability_auditor baseline/compare evidence.
No balance or probability claim is made here.

## Remaining risks and parent follow-up

Native start/cancel synchronization, automatic matching-cancellation cleanup, same-project release/reselection generations, and delayed-output isolation remain unresolved under the accepted no-simplifications contract.
Selection is authorization for an exact witnessed output, not a native start/payment receipt.
Scripted complete_special_project can emit the same exact output boundary.
The paid family timer remains untouched in source and model scenarios.

The all-source temporary lifetime correction is implemented within the owned core under the parent's explicit follow-up authorization.
Parent result initializations are present at selection/release feedback, the after-Theory exact driver caller, provider cleanup, and the original Cloning country-output boundary.
Each result-consuming caller initializes native_prototype_result to result.none before its helper call.
Cloning/Rocketry literal wrappers do not consume the nested result locally; they forward into outer caller-owned storage.
Electronics consumes it for retry and owns its own result slot.
The radar project's bare wrapper call has no later dedicated-result consumer; any future consumer would require its own storage.
The core's five internal output slots are owned by each generic transaction, and are not added public caller inputs.
The prior parent caller-storage warning is resolved in the reviewed source and bounded feedback/Cloning output tests.
Full neutral/custom technology payload and its own output lifetime remain parent-owned and outside the driver; no complete consumer claim is made.
This follow-up writes only the owned effects, API markdown, and this handoff.
Constants and trigger definitions remain unchanged from the Electronics tranche.

Live callback timing, native payment/research, engine result lifetime, cancellation, full native grant consumers, decision rendering, and probability comparisons were not completed by this worker.
HOI4 execution is prohibited; domain evidence was limited by the recorded route deadlines, and decision/AI/runtime acceptance belongs to the parent/user boundary.
The full Event016 goal remains incomplete.
No design simplification, substitute source, fallback timer, guessed cancellation callback, or extra project/model/technology was introduced.

Skills applied: chaos-redux-events, chaos-redux-subagents, and chaos-redux-decisions-missions.
No skill was created or changed.

## Local references read

The following are direct local reads, with exact SHA-256 revisions and relevant spans.
Installed documentation is the primary syntax authority; the offline wiki was consulted in parallel.

| Source path | Read span | SHA-256 revision |
| --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 216-247 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | 1-80 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 6228-6256 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\special_projects\projects\documentation.md` | 36-46; 198-213 | `16879504bc72aa357f1d3c0f1093e94a3946f8c35e7942f65ac9a5d3bcd6c643` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 2278-2296; 2792-2803; 6730-6751; 7820-7840; 7888-7908 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263-270; 425-445; 1069-1133 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 4683-4697 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 2301-2318; 2359-2389 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 25-47 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 59-71 | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_localisation\00_scripted_localisation.txt` | 1-42 | `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\special_projects\projects\radar_projects.txt` | 1-77 | `1a7cc30969a3c896887edccae6a75945996e4dc77312dd02a818aa6e66f9a69a` |

## Final evidence note and source snapshot

The final explicit-workspace exact reference_read retry produced no response within the worker 45-second observation budget.
No global service-health conclusion follows from that deadline.
Immutable existing-source comparison baseline: `a23ea17ca6c53002d9737e62f9558fb0b2657012`.
Hashes below bind this handoff to raw source bytes at capture; later shared-tree edits require rechecking the affected scenarios.

| Source file | SHA-256 at final capture |
| --- | --- |
| `common/decisions/016_mengele_native_prototype_selection_decisions.txt` | `bbe8c7969a20691e5f5ba6057386732bc55672b5f1a030ec34aba842776c4757` |
| `common/script_constants/016_brilliant_scientist_constants.txt` | `adfee7fe6093933c394c34c8a6a162795d4bdb4575512c476b417c1173b6e4a6` |
| `common/script_constants/016_mengele_native_prototype_constants.txt` | `72b235e357ee8543b8fc83864dc5c045ad528360432fb6766995ff54b4c75208` |
| `common/script_constants/016_mengele_project_stage_constants.txt` | `527499b80909a5f7f2544940d6db51a6145ff2634c4c3c0792cbeff22cdacd71` |
| `common/scripted_effects/016_mengele_native_ownership_cxt_effects.txt` | `98756cecf68e5ceab990fb842212b0431cfc4e876ed78e411f0cec739342413c` |
| `common/scripted_effects/016_mengele_native_prototype_effects.md` | `da0f3312b1e2e77de14624251e32f2c76ca93601b058b95429189bd56b176b23` |
| `common/scripted_effects/016_mengele_native_prototype_effects.txt` | `ce5379144355f7323f1ecab0c485af2c212922ce5bfadc30f993dd9a59c30a73` |
| `common/scripted_effects/016_mengele_native_selection_decision_effects.txt` | `72d16905079f85e6273c8be6d2a63ac271497d274da96f094ad406d56318736d` |
| `common/scripted_effects/016_mengele_project_stage_effects.txt` | `abed7c339e0f3497a4a85d73f4a812ca74a7e33e35455f9a967b5f3e1f20fc47` |
| `common/scripted_triggers/016_mengele_alien_arms_stage_decision_triggers.txt` | `ef7e5c23940b5ac3768092553e444708202ba9337bdf61876d898bfc4e7e7b52` |
| `common/scripted_triggers/016_mengele_biological_stage_decision_triggers.txt` | `ad49e955a82b5b323382d80dfcb46f58ea5d404edf8dd981ec60f841d7eb7931` |
| `common/scripted_triggers/016_mengele_cloning_stage_decision_triggers.txt` | `7318ff6926bbe23321df66658355e19e88998954c0918861a33b994a45369a8d` |
| `common/scripted_triggers/016_mengele_computation_decision_triggers.txt` | `a36232c35a42e61ffa81cf53f780d371d9b9547d1e4d317c55cb31429d321bb0` |
| `common/scripted_triggers/016_mengele_conventional_stage_decision_triggers.txt` | `1e361c5f85585c4eb51aa0ea7bb2345cc21287a2ea0c7858ce93263f737b2a38` |
| `common/scripted_triggers/016_mengele_native_prototype_triggers.txt` | `d048e4116c05403b353c874c7355395586a2a0381047871f5d66a4b18f4f5f04` |
| `common/scripted_triggers/016_mengele_native_selection_decision_triggers.txt` | `2f1342e5cdf0dc8c1afd89f297dbb3f6bd8d5d4d029cd9f110083f4c9ac71b33` |
| `common/scripted_triggers/016_mengele_paleogenetics_stage_decision_triggers.txt` | `a457bd6f889ea2ef163ea4f0d536aab8213377737dde496a63f2f35a8d8bcf0a` |
| `common/scripted_triggers/016_mengele_project_stage_triggers.txt` | `5ab7041ce22f13fbfecf641f4ca9e6fc7d693ddf366da14e631a3dfa498e537c` |
| `common/scripted_triggers/016_mengele_robotics_stage_decision_triggers.txt` | `064cc387d3e89830c6b5a3926f542226a052ede2881b5cf3460ddd6136149b69` |
| `common/scripted_triggers/016_mengele_singularity_stage_decision_triggers.txt` | `1c5f614c2baa2f79e7c279ba22258cfc6fc1f369efc0034070a0b9ab1c166252` |
| `common/scripted_triggers/016_mengele_teleportation_stage_decision_triggers.txt` | `73703dc378de6f1bf9735caef49e97b6362c6674c2f855addce591266b45ecbd` |
| `common/scripted_triggers/016_mengele_temporal_stage_decision_triggers.txt` | `a46dda28a3d915e280396c372607f66ba06f81bebee8f0cfaa7809d6b73ef980` |
| `common/scripted_triggers/016_mengele_xenobiological_synthesis_stage_decision_triggers.txt` | `5fc76bec30f2a2fcacf80a5643083725fd1ee7322d8f1d5a8affccc84384c1e3` |
| `common/special_projects/projects/radar_projects.txt` | `dc6620d60b4db716e442502af1bb120f86d6bf5f3c491883558d9292d45e2904` |

| `common/scripted_effects/016_mengele_project_bridge_effects.txt` | `f42d53e42f302ef970ab318751c98014247e628435fc30261846834abf6ce87c` |
| `common/special_projects/projects/016_brilliant_scientist_projects.txt` | `d1d5d5d9ed0761bf67f50e3aa006f6711e385f2a0f3fce2e3250babff3d1352d` |


## Parent final reference delivery

Read artifact: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_native_electronics_reference_results_2026-10-03.json`, SHA-256 `af394655e0de824a4560e2d0eb5ad04b3038aa05863cb1f2eee72afb0e94cdfc`.
The parent successful exact-completion MCP read is complete across 6243-6250 and the 6251-6257 continuation, with nextLine null on the final delivery.
Its id is `d94fad5f14dff54451fa80122aeca43fcec9506ff16676bd16ba26d221930162` and revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
It defines COUNTRY-scoped exact completed queries with sp:, variable, and keyword inputs.
The parent successful Decision modding timer read covers 337-356, id `91b27451ff9a5b5e5b74f6b0b8a12b3012a222b3d82681284186751ca59753eb`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, nextLine null.
It distinguishes selection-time complete_effect from timer remove_effect and cancellation via cancel_trigger/cancel_if_not_visible with cancel_effect; visibility alone does not cancel a timer by default.
Neither owned helper edits that timer lifecycle, and the active paid-family gate continues to leave it untouched.
The artifact records 600-second broad context, 75-line and 12-line exact radar source_lookup, and parent root event-lint timeouts.
The parent reports the four-node root lint timed out and a two-node narrower retry remained pending at this worker final handoff; no final retry result was supplied or inferred.
No new MCP queries were made after the parent took final domain ownership.
No live engine claim follows from these offline reference deliveries.

## Reproducible source driver

Run the following Python block from the Chaos Redux root.
It reads source and Git baseline only, performs no filesystem writes or gameplay operations, and reports its separate suites and stubs.
Driver UTF-8 SHA-256: `474201a273bf5427d8cc35905179891cf640f0952ed68256158ab3a3239417b0`.

```python
from pathlib import Path
import re, itertools, subprocess, copy, hashlib, json
root=Path.cwd()
prefix='brilliant_scientist_mengele_'
base='mengele_event016_'
def parse(text):
    ts=re.findall(r'"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>]+',re.sub(r'#[^\n]*','',text))
    pos=0
    def block():
        nonlocal pos
        out=[]
        while pos<len(ts) and ts[pos]!='}':
            k=ts[pos];pos+=1
            if pos>=len(ts) or ts[pos] not in ('=','>','<'):
                continue
            op=ts[pos];pos+=1
            if ts[pos]=='{':
                pos+=1;v=block();assert ts[pos]=='}';pos+=1
            else:
                v=ts[pos].strip('"');pos+=1
            out.append((k,op,v))
        return out
    return block()
paths=[
'common/scripted_effects/016_mengele_native_prototype_effects.txt',
'common/scripted_triggers/016_mengele_native_prototype_triggers.txt',
'common/scripted_effects/016_mengele_project_stage_effects.txt',
'common/scripted_effects/016_mengele_native_selection_decision_effects.txt',
'common/scripted_effects/016_mengele_project_bridge_effects.txt',
'common/scripted_triggers/016_mengele_project_stage_triggers.txt',
'common/scripted_triggers/016_mengele_conventional_stage_decision_triggers.txt',
'common/scripted_triggers/016_mengele_native_stage_decision_triggers.txt']
# Add all literal receipt trigger owners without assuming a filename.
paths=[p for p in paths if Path(p).exists()]
for p in Path('common/scripted_triggers').glob('016*.txt'):
    if '_decision_receipt_is_empty = {' in p.read_text(encoding='utf-8-sig') and str(p).replace('\\','/') not in paths:
        paths.append(str(p).replace('\\','/'))
defs={}
for p in paths:defs.update({k:v for k,op,v in parse(Path(p).read_text(encoding='utf-8-sig')) if isinstance(v,list)})
const={}
constant_paths=['common/script_constants/016_brilliant_scientist_constants.txt','common/script_constants/016_mengele_project_stage_constants.txt','common/script_constants/016_mengele_native_prototype_constants.txt']
for filename in constant_paths:
    p=Path(filename)
    for cat,op,b in parse(p.read_text(encoding='utf-8-sig')):
        if isinstance(b,list):
            for k,_,v in b:
                if isinstance(v,str) and re.fullmatch(r'-?\d+(\.\d+)?',v):const[cat+'.'+k]=float(v)
class Model:
    def __init__(self,definitions=defs):
        self.defs=definitions;self.temp={};self.vars={};self.arr={};self.flags=set();self.completed=set();self.research=set();self.tech=set();self.provider=True;self.modifiers=[];self.retry=0;self.retry_checks=False;self.query_count=0;self.dll=False;self.conservative=False;self.retry_mode=1;self.gtd=True;self.bridge_calls=[];self.tooltips=[]
    def read(self,s):
        if s.startswith('constant:'):return const[s[9:]]
        try:return float(s)
        except ValueError:pass
        if '^' in s:
            a,i=s.split('^',1)
            if i=='num':return len(self.arr.get(a,[]))
            i=int(self.read(i));return self.arr.get(a,[])[i] if i<len(self.arr.get(a,[])) else 0
        return self.temp.get(s,self.vars.get(s,0))
    def cond(self,b):return all(self.one(k,op,v) for k,op,v in b)
    def one(self,k,op,v):
        if k in ('AND','hidden_trigger'):return self.cond(v)
        if k=='OR':return any(self.one(*x) for x in v)
        if k=='NOT':return not self.cond(v)
        if k=='check_variable':
            d={k:v for k,o,v in v}
            if 'var' in d:a=self.read(d['var']);b=self.read(d['value']);op=d.get('compare','greater_than_or_equals')
            else:k,op,x=v[0];a=self.read(k);b=self.read(x)
            return {'=':lambda:a==b,'equals':lambda:a==b,'>':lambda:a>b,'<':lambda:a<b,'greater_than_or_equals':lambda:a>=b,'less_than_or_equals':lambda:a<=b,'not_equals':lambda:a!=b,'greater_than':lambda:a>b,'less_than':lambda:a<b}[op]()
        if k=='has_country_flag':return v in self.flags
        if k=='is_special_project_completed':self.query_count+=1;return v in self.completed
        if k=='is_special_project_being_researched':return v in self.research
        if k=='has_tech':return v in self.tech
        if k=='has_dlc':return self.gtd if v=='Gotterdammerung' else self.dll
        if k==prefix+'project_native_output_is_authentic':return True
        if k==prefix+'project_stage_provider_is_valid':return self.provider
        if k=='brilliant_scientist_can_research_mengele_cloning_prototype':return True
        if k in self.defs:return self.cond(self.defs[k])==(v=='yes')
        raise AssertionError(('unsupported trigger',k,v))
    def write(self,k,v,temp):
        if '^' in k:
            a,i=k.split('^',1);i=int(self.read(i));assert i<len(self.arr[a]);self.arr[a][i]=v
        else:(self.temp if temp else self.vars)[k]=v
    def run(self,k):
        before=set(self.temp)
        try:self.rawrun(k)
        finally:
            if self.conservative:
                for new in set(self.temp)-before:self.temp.pop(new)
    def rawrun(self,k):
        if k==prefix+'grant_native_custom_operational_package':
            body=self.defs[k];provider_if=next(v for name,op,v in body if name=='if')
            candidates=[v for name,op,v in provider_if if name=='if']
            clone_if=next(v for v in candidates if 'mengele_event016_cloning_theory_completed' in str(v))
            gate=next(v for name,op,v in clone_if if name=='limit')
            self.bridge_calls.append(self.provider and self.cond(gate))
            return
        if k==prefix+'reconcile_project_availability':return
        if k==prefix+'grant_conventional_stage_package':
            self.temp[base+'stage_package_applied']=1;return
        if k==prefix+'settle_native_electronics_deployment_from_radar':
            self.retry+=1
            if self.retry_checks:
                assert self.arr[base+'native_prototype_source_entries'][1]==4
                assert self.arr[base+'native_prototype_mode_entries'][1]==self.retry_mode
                assert base+'native_selected_electronics_radar' not in self.flags
            self.effect(self.defs[k])
            return
        self.effect(self.defs[k])
    def effect(self,b):
        taken=False
        for k,op,v in b:
            if k=='if':
                lim=next((v for k,o,v in v if k=='limit'),[])
                taken=self.cond(lim)
                if taken:self.effect([x for x in v if x[0]!='limit'])
            elif k=='else_if':
                if not taken:
                    lim=next((v for k,o,v in v if k=='limit'),[])
                    taken=self.cond(lim)
                    if taken:self.effect([x for x in v if x[0]!='limit'])
            elif k=='else':
                if not taken:self.effect(v)
                taken=True
            elif k in ('hidden_effect','custom_override_tooltip'):self.effect(v)
            elif k=='tooltip':pass
            elif k=='custom_effect_tooltip':self.tooltips.append(v)
            elif k=='set_technology':
                for tech,_,level in v:
                    if tech!='popup' and self.read(level)>0:self.tech.add(tech)
            elif k=='while_loop_effect':
                lim=next(v for k,o,v in v if k=='limit');i=0
                while self.cond(lim):
                    self.effect([x for x in v if x[0]!='limit']);i+=1;assert i<=1000
            elif k in ('set_temp_variable','set_variable'):
                if v[0][0]=='var':d={k:v for k,o,v in v};key=d['var'];val=d['value']
                else:key,_,val=v[0]
                self.write(key,self.read(val),k=='set_temp_variable')
            elif k=='subtract_from_temp_variable':
                key,_,val=v[0];self.write(key,self.read(key)-self.read(val),True)
            elif k=='add_to_array':
                d={k:v for k,o,v in v};self.arr.setdefault(d['array'],[]).append(self.read(d['value']))
            elif k=='clear_array':self.arr[v]=[]
            elif k=='set_country_flag':self.flags.add(v)
            elif k=='clr_country_flag':self.flags.discard(v)
            elif k=='add_dynamic_modifier':self.modifiers.append(v[0][2])
            elif k=='force_update_dynamic_modifier':pass
            elif k in self.defs:self.run(k)
            else:raise AssertionError(('unsupported effect',k,v))
def fixture(code=4):
    m=Model();m.temp[base+'native_prototype_source']=code
    m.flags|={base+'provider_receipts_initialized',base+'singularity_component_entries_initialized'}
    for suffix in ['active_project_stage','active_cost_political_power','active_cost_support_equipment','active_cost_fuel','active_cost_civilian_factory_commitment','native_later_stage_deployment_source','native_later_stage_weaponization']:
        m.arr[base+suffix+'_entries']=[0]*15
    for suffix in ['native_prototype_source','native_prototype_mode']:m.arr[base+suffix+'_entries']=[0]*15
    return m
def receipt(m):return (m.arr[base+'native_prototype_source_entries'][1],m.arr[base+'native_prototype_mode_entries'][1])
def result(m):return m.temp[base+'native_prototype_result']
def run(m,s):m.run(prefix+s)
count=0
# Exhaustive fresh eligibility, completed-bit timing, and paid stages.
for provider,theory,proto,selected,done in itertools.product([False,True],repeat=5):
    for active in range(5):
        m=fixture();m.provider=provider
        for enabled,suffix in [(theory,'electronics_theory_completed'),(proto,'electronics_prototype_completed'),(selected,'native_selected_electronics_radar')]:
            if enabled:m.flags.add(base+suffix)
        if done:m.completed.add('sp:sp_air_radar')
        m.arr[base+'active_project_stage_entries'][1]=active
        for suffix in ['active_cost_political_power','active_cost_support_equipment','active_cost_fuel','active_cost_civilian_factory_commitment']:
            m.arr[base+suffix+'_entries'][1]=77
        paid=copy.deepcopy({k:v for k,v in m.arr.items() if 'active_' in k})
        run(m,'native_output_electronics_radar')
        eligible=provider and theory and not proto and selected and active==0
        assert result(m)==(2 if eligible else 5),(provider,theory,proto,selected,done,active,result(m))
        assert receipt(m)==((4,1) if eligible else (0,0))
        assert (base+'native_selected_electronics_radar' in m.flags)==(selected and not eligible)
        assert base+'native_observed_electronics_radar' in m.flags
        assert paid=={k:v for k,v in m.arr.items() if 'active_' in k}
        assert m.query_count==0 # Stubbed reconciliation is the only excluded completion-query seam.
        assert m.retry==int(eligible)
        count+=1
# Literal selection and explicit adoption gates, including held completed source.
for theory,proto,selected,done,tech,provider,gtd in itertools.product([False,True],repeat=7):
    for active in range(5):
        m=fixture();m.provider=provider;m.gtd=gtd
        for enabled,s in [(theory,'electronics_theory_completed'),(proto,'electronics_prototype_completed'),(selected,'native_selected_electronics_radar')]:
            if enabled:m.flags.add(base+s)
        if done:m.completed.add('sp:sp_air_radar')
        if tech:m.tech.add('electronic_mechanical_engineering')
        m.arr[base+'active_project_stage_entries'][1]=active
        expected=provider and theory and not proto and active==0 and (not selected or done) and (done or (gtd and tech))
        assert m.cond(m.defs[prefix+'can_select_native_electronics_radar'])==expected
        assert m.cond(m.defs[prefix+'native_electronics_private_gate'])==(provider and theory and not proto and active==0)
        run(m,'select_native_prototype')
        assert result(m)==((3 if done else 1) if expected else 5)
        assert receipt(m)==((4,2) if expected and done else (0,0))
        count+=1
# Auto adoption requires exact history and non-retired disposition.
for retired,done,other_done,selected in itertools.product([False,True],repeat=4):
    m=fixture();m.flags.add(base+'electronics_theory_completed')
    if retired:m.flags.add(base+'native_retired_electronics_radar')
    if selected:m.flags.add(base+'native_selected_electronics_radar')
    if done:m.completed.add('sp:sp_air_radar')
    if other_done:m.completed.add('sp:sp_air_jet_engine')
    expected=done and not retired
    assert m.cond(m.defs[prefix+'can_auto_adopt_exact_completed_native_prototype'])==expected
    if expected:
        run(m,'adopt_exact_completed_native_prototype');assert result(m)==3 and receipt(m)==(4,2)
        assert base+'native_observed_electronics_radar' not in m.flags
    count+=1
# Explicit adoption permits retired completed history, retaining its disposition.
m=fixture();m.flags|={base+'electronics_theory_completed',base+'native_retired_electronics_radar'}
m.completed.add('sp:sp_air_radar');run(m,'adopt_exact_completed_native_prototype')
assert result(m)==3 and receipt(m)==(4,2) and base+'native_retired_electronics_radar' in m.flags
assert m.retry==0
count+=1
# Release gates use exact research and paid-family receipt, independent of provider.
for selected,research,provider in itertools.product([False,True],repeat=3):
    for active in range(5):
        m=fixture();m.provider=provider
        if selected:m.flags.add(base+'native_selected_electronics_radar')
        if research:m.research.add('sp:sp_air_radar')
        m.research.add('sp:sp_air_jet_engine')
        m.arr[base+'active_project_stage_entries'][1]=active
        run(m,'release_native_prototype_selection')
        expected=selected and not research and active==0
        assert result(m)==(4 if expected else 5)
        assert (base+'native_selected_electronics_radar' in m.flags)==(selected and not expected)
        assert m.arr[base+'active_project_stage_entries'][1]==active
        assert m.research==({'sp:sp_air_radar','sp:sp_air_jet_engine'} if research else {'sp:sp_air_jet_engine'})
        count+=1
# Actual nested retry: provenance visible first, index 0 stays intact, result survives,
# and later-stage Deployment history has its separate exact source.
for radar_seen,radio in itertools.product([False,True],repeat=2):
    m=fixture();m.flags|={base+'electronics_theory_completed',base+'native_selected_electronics_radar'}
    if radar_seen:m.flags.add(base+'native_electronics_radar_project_output_seen')
    if radio:m.tech.add('radio_detection')
    m.arr[base+'native_prototype_source_entries'][0]=91;m.arr[base+'native_prototype_mode_entries'][0]=92
    m.retry_checks=True;run(m,'native_output_electronics_radar')
    assert receipt(m)==(4,1) and result(m)==2
    assert m.arr[base+'native_prototype_source_entries'][0]==91 and m.arr[base+'native_prototype_mode_entries'][0]==92
    assert (base+'electronics_deployment_completed' in m.flags)==(radar_seen and radio)
    assert m.temp[base+'project_family']==0 and m.temp[base+'requested_stage']==0 and m.temp[base+'project_index']==0
    saved=copy.deepcopy(m.arr);mods=m.modifiers[:];run(m,'native_output_electronics_radar')
    assert result(m)==5 and m.arr==saved and m.modifiers==mods and m.retry==1
    count+=1
# Witness mismatch rejects stale selectors; retirement clears only on fresh reselection.
for witness in [0,1,2,3,5]:
    m=fixture();m.flags|={base+'electronics_theory_completed',base+'native_selected_electronics_radar'}
    m.temp[base+'native_prototype_output_source']=witness;run(m,'settle_fresh_native_prototype')
    assert result(m)==5 and receipt(m)==(0,0) and base+'native_selected_electronics_radar' in m.flags
    count+=1
m=fixture();m.flags|={base+'electronics_theory_completed',base+'native_retired_electronics_radar'}
m.tech.add('electronic_mechanical_engineering');run(m,'select_native_prototype')
assert result(m)==1 and base+'native_retired_electronics_radar' not in m.flags
count+=1
# Cleanup preserves durable observations/provenance/research and paid receipt.
for selected in [False,True]:
    m=fixture();m.flags|={base+'native_observed_electronics_radar'}
    if selected:m.flags.add(base+'native_selected_electronics_radar')
    m.arr[base+'native_prototype_source_entries'][1]=4;m.arr[base+'native_prototype_mode_entries'][1]=2
    m.arr[base+'active_project_stage_entries'][1]=3;m.research.add('sp:sp_air_radar')
    before=copy.deepcopy(m.arr);run(m,'cleanup_native_prototype_selections')
    assert result(m)==(4 if selected else 0) and m.arr==before and receipt(m)==(4,2)
    assert base+'native_observed_electronics_radar' in m.flags and base+'native_selected_electronics_radar' not in m.flags
    assert (base+'native_retired_electronics_radar' in m.flags)==selected and 'sp:sp_air_radar' in m.research
    run(m,'cleanup_native_prototype_selections');assert result(m)==0 and m.arr==before
    count+=1
# Immutable a23ea17 parity for all existing source identities across selection/fresh/adopt/release.
old=defs.copy()
for path in paths[:2]:
    old.update({k:v for k,o,v in parse(subprocess.check_output(['git','show','a23ea17:'+path]).decode('utf-8-sig')) if isinstance(v,list)})
names={1:('cloning','cloning','sp_brilliant_scientist_cloning','native_output_cloning'),
       2:('flying_bomb','rocketry','sp_rockets_flying_bomb','native_output_rocketry_flying_bomb'),
       3:('jet_engine','rocketry','sp_air_jet_engine','native_output_rocketry_air_jet_engine')}
parity=0
for code,(suffix,family,project,wrapper) in names.items():
    for selected,opposite,done,provider,active in itertools.product([False,True],[False,True],[False,True],[False,True],range(5)):
        m=fixture(code);m.flags.add(base+family+'_theory_completed');m.provider=provider
        if selected:m.flags.add(base+'native_selected_'+suffix)
        if opposite and code in (2,3):m.flags.add(base+'native_selected_'+('jet_engine' if code==2 else 'flying_bomb'))
        if done:m.completed.add('sp:'+project)
        m.tech|={'experimental_rockets','fighter2'}
        index=7 if code==1 else 3;m.arr[base+'active_project_stage_entries'][index]=active
        for action in ['select_native_prototype',wrapper,'adopt_exact_completed_native_prototype','release_native_prototype_selection']:
            a=copy.copy(m);b=copy.copy(m)
            for obj in [a,b]:
                for attr in ['temp','vars','arr','flags','modifiers','completed','research','tech']:setattr(obj,attr,copy.deepcopy(getattr(m,attr)))
            b.defs=old
            run(a,action);run(b,action)
            for attr in ['vars','arr','flags','modifiers','retry']:assert getattr(a,attr)==getattr(b,attr),(code,action,attr)
            for key in set(a.temp)|set(b.temp):assert a.temp.get(key,0)==b.temp.get(key,0),(code,action,'temporary value',key)
            parity+=1
# Conservative call-frame deletion of outputs first created in returning helpers.
# Outer callback owns only the result; literal wrapper owns its forwarded scratch.
conservative=0
for provider,theory,proto,selected,done,seen,radio in itertools.product([False,True],repeat=7):
    for active in range(5):
        m=fixture();m.conservative=True;m.provider=provider
        m.temp[base+'native_prototype_result']=0
        for enabled,suffix in [(theory,'electronics_theory_completed'),(proto,'electronics_prototype_completed'),(selected,'native_selected_electronics_radar'),(seen,'native_electronics_radar_project_output_seen')]:
            if enabled:m.flags.add(base+suffix)
        if done:m.completed.add('sp:sp_air_radar')
        if radio:m.tech.add('radio_detection')
        m.arr[base+'active_project_stage_entries'][1]=active
        m.retry_checks=True;run(m,'native_output_electronics_radar')
        eligible=provider and theory and not proto and selected and active==0
        assert result(m)==(2 if eligible else 5)
        assert receipt(m)==((4,1) if eligible else (0,0))
        assert (base+'electronics_deployment_completed' in m.flags)==(eligible and seen and radio)
        assert m.arr[base+'active_project_stage_entries'][1]==active
        assert set(m.temp)=={base+'native_prototype_source',base+'native_prototype_result'}
        conservative+=1
# The parent project's actual COUNTRY source: wrapper runs before marker/grant.
def child(b,k):return next(v for key,_,v in b if key==k)
radar=dict((k,v) for k,o,v in parse(Path('common/special_projects/projects/radar_projects.txt').read_text(encoding='utf-8-sig')))['sp_air_radar']
country=child(child(radar,'project_output'),'country_effects')
ordered=[k for k,o,v in child(country,'hidden_effect')]
assert ordered[:2]==[prefix+'native_output_electronics_radar',prefix+'mark_native_electronics_radar_project_output']
integrated=0
for radio,selected,active in itertools.product([False,True],[False,True],range(5)):
    m=fixture();m.flags.add(base+'electronics_theory_completed');m.temp[base+'native_prototype_result']=0
    if selected:m.flags.add(base+'native_selected_electronics_radar')
    if radio:m.tech.add('radio_detection')
    m.arr[base+'active_project_stage_entries'][1]=active
    paid=copy.deepcopy({k:v for k,v in m.arr.items() if 'active_' in k})
    m.retry_checks=selected and active==0;m.effect(country)
    eligible=selected and active==0
    assert result(m)==(2 if eligible else 5)
    assert receipt(m)==((4,1) if eligible else (0,0))
    assert base+'native_electronics_radar_project_output_seen' in m.flags and 'radio_detection' in m.tech
    assert (base+'electronics_deployment_completed' in m.flags)==(eligible and radio)
    # Invoke the existing technology callback as a named later boundary, without
    # claiming engine set_technology notification order.
    run(m,'native_completion_radio_detection')
    assert (base+'electronics_deployment_completed' in m.flags)==eligible
    assert result(m)==(2 if eligible else 5) and paid=={k:v for k,v in m.arr.items() if 'active_' in k}
    integrated+=1
# Parent adoption driver: matching selection or non-retired exact history,
# retry only after index 1 adopted provenance and matching consumption.
for retired,selected,done,seen,radio,active in itertools.product([False,True],[False,True],[False,True],[False,True],[False,True],range(5)):
    m=fixture();m.flags.add(base+'electronics_theory_completed')
    m.temp.update({base+'native_prototype_result':0,base+'adoption_outer_family':2,base+'project_family':2,base+'requested_stage':1,base+'project_index':1,base+'project_output_applied':1,base+'stage_package_applied':0})
    if retired:m.flags.add(base+'native_retired_electronics_radar')
    if selected:m.flags.add(base+'native_selected_electronics_radar')
    if done:m.completed.add('sp:sp_air_radar')
    if seen:m.flags.add(base+'native_electronics_radar_project_output_seen')
    if radio:m.tech.add('radio_detection')
    m.arr[base+'active_project_stage_entries'][1]=active
    eligible=done and active==0 and (selected or not retired)
    m.retry_checks=eligible;m.retry_mode=2
    run(m,'try_adopt_exact_native_prototype')
    assert receipt(m)==((4,2) if eligible else (0,0)) and m.retry==int(eligible)
    assert (base+'electronics_deployment_completed' in m.flags)==(eligible and seen and radio)
    assert result(m)==(3 if eligible else (5 if selected or (done and not retired and active==0) else 0))
    assert base+'native_observed_electronics_radar' not in m.flags
    integrated+=1
# Whole after-Theory wrapper restores its paid outer transaction's output fields.
for seen,radio in itertools.product([False,True],repeat=2):
    m=fixture();m.flags.add(base+'electronics_theory_completed');m.completed.add('sp:sp_air_radar')
    if seen:m.flags.add(base+'native_electronics_radar_project_output_seen')
    if radio:m.tech.add('radio_detection')
    expected={base+'project_family':2,base+'requested_stage':1,base+'project_index':1,base+'project_output_applied':1,base+'computation_output_applied':7,base+'stage_output_gap':8,base+'project_output_authorized':0,base+'project_availability_reconciled':9}
    m.temp.update(expected);m.temp[base+'native_prototype_result']=0;m.retry_checks=True;m.retry_mode=2
    run(m,'adopt_completed_native_after_theory')
    assert receipt(m)==(4,2) and all(m.temp[k]==v for k,v in expected.items())
    integrated+=1
# Generic Electronics APIs own mapping scratch but the caller owns the result.
for done,active,gtd in itertools.product([False,True],range(5),[False,True]):
    m=fixture();m.conservative=True;m.gtd=gtd;m.flags.add(base+'electronics_theory_completed');m.tech.add('electronic_mechanical_engineering')
    m.temp[base+'native_prototype_result']=0
    if done:m.completed.add('sp:sp_air_radar')
    m.arr[base+'active_project_stage_entries'][1]=active
    run(m,'select_native_prototype')
    assert result(m)==((3 if done else 1) if active==0 and (done or gtd) else 5)
    assert receipt(m)==((4,2) if done and active==0 else (0,0))
    conservative+=1
# All supported old sources: actual core fresh/select/adopt with conservative
# helper frames and only source/result caller storage. No caller mapping scratch.
native_lifetime=0
for code,(suffix,family,project,wrapper) in names.items():
    for provider,theory,proto,selected,done,opposite in itertools.product([False,True],repeat=6):
        for active in range(5):
            seed=fixture(code);seed.provider=provider
            seed.temp[base+'native_prototype_result']=0
            for enabled,name in [(theory,family+'_theory_completed'),(proto,family+'_prototype_completed'),(selected,'native_selected_'+suffix)]:
                if enabled:seed.flags.add(base+name)
            if opposite and code in (2,3):seed.flags.add(base+'native_selected_'+('jet_engine' if code==2 else 'flying_bomb'))
            if done:seed.completed.add('sp:'+project)
            seed.tech|={'experimental_rockets','fighter2'}
            index=7 if code==1 else 3;seed.arr[base+'active_project_stage_entries'][index]=active
            for costs in ['active_cost_political_power','active_cost_support_equipment','active_cost_fuel','active_cost_civilian_factory_commitment']:
                seed.arr[base+costs+'_entries'][index]=113
            for action in ['select_native_prototype',wrapper,'adopt_exact_completed_native_prototype']:
                a=copy.copy(seed);b=copy.copy(seed)
                for obj in [a,b]:
                    for attr in ['temp','vars','arr','flags','modifiers','completed','research','tech','bridge_calls','tooltips']:setattr(obj,attr,copy.deepcopy(getattr(seed,attr)))
                b.conservative=True
                run(a,action);run(b,action)
                private=provider and theory and not proto and active==0
                conflicting=opposite and code in (2,3)
                if action==wrapper:
                    success=private and selected and not conflicting
                    expected_result=2 if success else 5;mode=1
                    assert base+'native_observed_'+suffix in b.flags
                elif action=='adopt_exact_completed_native_prototype':
                    success=private and done and not conflicting
                    expected_result=3 if success else 5;mode=2
                else:
                    allowed=private and not conflicting and (not selected or done)
                    success=allowed and done
                    expected_result=(3 if done else 1) if allowed else 5;mode=2
                assert result(b)==expected_result,(code,action,provider,theory,proto,selected,done,opposite,active,result(b))
                assert b.arr[base+'native_prototype_source_entries'][index]==(code if success else 0)
                assert b.arr[base+'native_prototype_mode_entries'][index]==(mode if success else 0)
                assert (base+'native_selected_'+suffix in b.flags)==(True if action=='select_native_prototype' and expected_result==1 else selected and not success)
                for field in ['vars','arr','flags','modifiers']:assert getattr(a,field)==getattr(b,field),(code,action,field)
                assert result(a)==result(b)
                assert {k:v for k,v in b.arr.items() if 'active_' in k}=={k:v for k,v in seed.arr.items() if 'active_' in k}
                if code==1:
                    proof=b.cond(b.defs[prefix+'native_cloning_fresh_receipt_is_present'])
                    assert proof==(success and mode==1)
                native_lifetime+=1
# Actual parent selection/release feedback adapters under conservative frames.
native_ui=0
for code,(suffix,family,project,wrapper) in names.items():
    for selected,done,opposite,active in itertools.product([False,True],[False,True],[False,True],range(5)):
        for action in ['native_selection_decision_complete','native_release_decision_complete']:
            m=fixture(code);m.conservative=True;m.temp[base+'native_prototype_result']=0
            m.flags.add(base+family+'_theory_completed')
            if selected:m.flags.add(base+'native_selected_'+suffix)
            if opposite and code in (2,3):m.flags.add(base+'native_selected_'+('jet_engine' if code==2 else 'flying_bomb'))
            if done:m.completed.add('sp:'+project)
            m.tech|={'experimental_rockets','fighter2'}
            index=7 if code==1 else 3;m.arr[base+'active_project_stage_entries'][index]=active
            run(m,action)
            if action=='native_selection_decision_complete':
                allowed=active==0 and not(opposite and code in (2,3)) and (not selected or done)
                expect=(3 if done else 1) if allowed else 5
                assert result(m)==expect
                expected_tt='mengele_event016_native_selection_'+('adopted' if expect==3 else 'committed' if expect==1 else 'blocked')+'_tt'
                assert expected_tt in m.tooltips
                if code==1:assert m.bridge_calls==([True] if expect==3 else [])
            else:
                expect=4 if selected and active==0 else 5
                assert result(m)==expect
                expected_tt='mengele_event016_native_selection_'+('released' if expect==4 else 'blocked')+'_tt'
                assert expected_tt in m.tooltips
            assert m.arr[base+'active_project_stage_entries'][index]==active
            native_ui+=1
# Actual Clone bridge gate, with source/mode proof independent of completed bit.
body=defs[prefix+'grant_native_custom_operational_package']
provider_if=next(v for name,op,v in body if name=='if')
clone_if=next(v for name,op,v in provider_if if name=='if' and 'mengele_event016_cloning_theory_completed' in str(v))
clone_gate=next(v for name,op,v in clone_if if name=='limit')
clone_bridge=0
for provider,theory,proto,done,length,source,mode in itertools.product([False,True],[False,True],[False,True],[False,True],[0,7,8,15],[0,1,2,4],[0,1,2]):
    m=fixture(1);m.provider=provider;m.temp[base+'native_grant_family']=8
    if theory:m.flags.add(base+'cloning_theory_completed')
    if proto:m.flags.add(base+'cloning_prototype_completed')
    if done:m.completed.add('sp:sp_brilliant_scientist_cloning')
    m.arr[base+'native_prototype_source_entries']=[0]*length
    m.arr[base+'native_prototype_mode_entries']=[0]*length
    if length>=8:
        m.arr[base+'native_prototype_source_entries'][7]=source
        m.arr[base+'native_prototype_mode_entries'][7]=mode
    expected=provider and theory and proto and (done or (length>=8 and source==1 and mode==1))
    assert (m.provider and m.cond(clone_gate))==expected
    clone_bridge+=1
# The actual original Clone COUNTRY hidden boundary includes the parent's result
# storage, fresh literal wrapper and history bridge call before original consumer.
native_projects={k:v for k,o,v in parse(Path('common/special_projects/projects/016_brilliant_scientist_projects.txt').read_text(encoding='utf-8-sig'))}
clone_hidden=child(child(child(native_projects['sp_brilliant_scientist_cloning'],'project_output'),'country_effects'),'hidden_effect')
for selected,done,active in itertools.product([False,True],[False,True],range(5)):
    m=fixture(1);m.conservative=True;m.flags.add(base+'cloning_theory_completed')
    if selected:m.flags.add(base+'native_selected_cloning')
    if done:m.completed.add('sp:sp_brilliant_scientist_cloning')
    m.arr[base+'active_project_stage_entries'][7]=active
    m.effect(clone_hidden)
    expected=selected and active==0
    assert result(m)==(2 if expected else 5)
    assert m.bridge_calls==([True] if expected else [])
    assert m.arr[base+'native_prototype_source_entries'][7]==(1 if expected else 0)
    clone_bridge+=1
# Negative regression: immutable a23ea17 drops helper-created mapping slots
# under conservative return, while the corrected source settles the same input.
old_lifetime_regression=0
for code,(suffix,family,project,wrapper) in names.items():
    for action,expected in [('select_native_prototype',1),(wrapper,2),('adopt_exact_completed_native_prototype',3)]:
        old_case=fixture(code);old_case.defs=old;old_case.conservative=True
        new_case=fixture(code);new_case.conservative=True
        for m in [old_case,new_case]:
            m.temp[base+'native_prototype_result']=0;m.flags.add(base+family+'_theory_completed')
            m.tech|={'experimental_rockets','fighter2'}
            if action==wrapper:m.flags.add(base+'native_selected_'+suffix)
            if action=='adopt_exact_completed_native_prototype':m.completed.add('sp:'+project)
            run(m,action)
        assert result(old_case)==5 and result(new_case)==expected
        index=7 if code==1 else 3
        if expected!=1:
            assert old_case.arr[base+'native_prototype_source_entries'][index]==0
            assert new_case.arr[base+'native_prototype_source_entries'][index]==code
        old_lifetime_regression+=1
# No radar branch in either generic settlement core: retry stays wrapper-only.
for name in ['settle_fresh_native_prototype','adopt_exact_completed_native_prototype']:
    assert prefix+'settle_native_electronics_deployment_from_radar' not in str(defs[prefix+name])
print(json.dumps({'electronics_scenarios_passed':count,'cloning_rocketry_parity_cases_passed':parity,'conservative_output_lifetime_cases_passed':conservative,'parent_integration_cases_passed':integrated,'cloning_rocketry_conservative_cases_passed':native_lifetime,'cloning_rocketry_parent_ui_cases_passed':native_ui,'clone_bridge_cases_passed':clone_bridge,'old_lifetime_regression_cases_passed':old_lifetime_regression,'limits':['Engine queries supplied as fixture state','Provider lifecycle predicate stubbed','Availability reconciliation and dynamic modifier engine refresh stubbed','Full custom operational bridge payload stubbed; actual Clone bridge gate evaluated from source',
'Conventional technology package grants stubbed; actual stage-output, receipt initialization, mapping, provenance, consumption, release, cleanup and radar retry source executed']},indent=2))

```
