# Biological Weapons exact output identity review

Date: 2026-10-07.
Role: chaosx_scripted_system_architect, source audit and architecture only.
Root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Disposition: reviewed correction recommendation for parent implementation within the accepted exact-marker and fifteen-family closure scope.
Acceptance basis is the explicit task instruction approving exact markers on existing mapped outputs, retaining no Biological selection controls, preserving native payloads, and preserving an active matching paid receipt and timer.
The task explicitly retains D17 fixed-order historical adoption.
Document existence does not establish acceptance, and this review does not amend or waive stronger native lifecycle requirements.
Only this handoff was written, with no gameplay, asset, model, index, or commit changes.

## Finding and precise counterexample

The Biological callback heuristic present at the initial audit does not establish the completing project's identity.
The counterexample line references below bind to the initial source hashes, and the concurrent parent checkpoint later in this handoff distinguishes subsequent edits.
`016_mengele_project_stage_effects.txt:1644-1648` calls `brilliant_scientist_mengele_observe_reused_biological_sources` from the provider branch of `016_brilliant_scientist_project_on_actions.txt:20-22` on every `on_project_completion`.
The helper at `016_mengele_native_prototype_effects.txt:414-486` queries six country completion bits and absent observed flags, chooses the first unobserved completion, then explicitly sets `fresh_output` at 483.
It never reads or authenticates the callback's FROM project.

Concrete reachable source scenario: Biological Theory is complete and Prototype is incomplete, then `brilliant_scientist_project_incident_active` temporarily makes the provider invalid.
Anthrax completes during that interval, so the provider callback branch does not run and `mengele_event016_reused_source_observed_anthrax` stays absent.
After incident recovery, the provider is valid and its Biological receipt is empty.
An unrelated project completes.
Lines 418-422 select the historical Anthrax completion, lines 481-484 submit Biological/Anthrax/fresh_output, and lines 370-386 apply Prototype and persist fresh provenance.
The family-wide authenticity OR at `016_mengele_project_stage_triggers.txt:1529-1540` accepts Anthrax completion without authenticating the callback.
This contradicts D17's claim that unrelated completions observe and settle nothing.
The helper documentation itself acknowledges delayed observation while invalid at `016_mengele_native_prototype_effects.md:321`.

A second case exposes wrong source identity: retain that unobserved historical Anthrax completion, then genuinely complete Plague after recovery.
The scan chooses Anthrax first and marks Plague observed as well, so Plague's callback can persist source Anthrax with fresh mode.
These are source-derived counterexamples, not observed engine runs.

## Recommended helper and caller map

All proposed effects below run in the completing COUNTRY scope.
The country output has FROM as the project according to installed project documentation, but the literal output call site supplies identity without depending on an undocumented project-ID accessor.
Use one hidden additive call at the beginning of each existing `project_output.country_effects`, before its original consumer calls.
Never hook `iteration_output`, a generic completion adapter, or a facility-state output.

| Existing source | Existing metadata constant, code | Recommended literal effect | Exact current output location |
| --- | --- | --- | --- |
| `anthrax_bomb` | `biological_anthrax`, 6 | `brilliant_scientist_mengele_native_completion_anthrax_bomb` | `common\special_projects\projects\biowarfare_main_projects.txt:476-490` |
| `plague_bomb` | `biological_plague`, 7 | `brilliant_scientist_mengele_native_completion_plague_bomb` | Same file, 714-728 |
| `tularemia_bomb` | `biological_tularemia`, 8 | `brilliant_scientist_mengele_native_completion_tularemia_bomb` | Same file, 947-961 |
| `smallpox_bomb` | `biological_smallpox`, 9 | `brilliant_scientist_mengele_native_completion_smallpox_bomb` | Same file, 1185-1199 |
| `weaponize_the_zombies` | `biological_weaponized_zombies`, 10 | `brilliant_scientist_mengele_native_completion_weaponize_the_zombies` | `common\special_projects\projects\zombie_weaponized_projects.txt:73-80` |
| `black_plague_weaponization_program` | `biological_black_plague`, 11 | `brilliant_scientist_mengele_native_completion_black_plague_weaponization_program` | `common\special_projects\projects\020_black_plague_weaponization_projects.txt:56-63` |

The parent owns those output edits and must reread the current shared source before applying them.
Each wrapper takes no caller selector input and overwrites source, family, mode, and output witness with its own literals.
It may set its matching existing `mengele_event016_reused_source_observed_*` informational marker even without a valid provider, attempts private settlement only through the strict provider/predecessor/receipt gates, and clears transient selectors on every exit.
Do not suppress the genuine output attempt merely because an observed marker already exists.
The six wrappers must be called only by those six literal output blocks.
A marker or supplied numeric source alone cannot authenticate a fresh transaction.

| Helper | Inputs and defaults | Outputs and side effects | Caller |
| --- | --- | --- | --- |
| `brilliant_scientist_mengele_reused_native_source_matches_family` | COUNTRY trigger, temporary family/source, defaults none | Pure exact whitelist: Biological accepts only its six enumerated sources, High Energy only reactor source 5 | Reused settlement core |
| `brilliant_scientist_mengele_reused_native_source_is_completed` | COUNTRY trigger, family/source | Pure exact paired completed query, rejects none, unknown, fractional, and mismatched codes | Historical branch of reused settlement |
| `brilliant_scientist_mengele_reused_native_output_witness_matches` | COUNTRY trigger, family/source/output_source, default witness none | Pure exact whitelist plus equal synchronous witness | Fresh branch of reused settlement |
| `brilliant_scientist_mengele_settle_reused_native_prototype` | COUNTRY, exact family/source/mode and fresh witness when applicable | Existing dedicated result, changed private Prototype and exact source/mode at family index only after successful application | Six literal wrappers, reactor wrapper, historical adoption helper |
| `brilliant_scientist_mengele_adopt_reused_native_prototype` | COUNTRY, family and current completed objects, witness explicitly none | Fixed-order historical selection, adopted_settled or blocked/none, no native output replay | Existing after-Theory transaction |

Keep this logic in the Event016 native helper files with matching markdown contracts.
The shared `chaosx_dynamic_effects.txt` registry is for neutral cross-system APIs and has no fitting exact-provenance helper.
Do not extend `brilliant_scientist_mengele_prepare_native_prototype_request` casually, because its current supported-source mapping and fallback are specific to Cloning, Electronics, and Rocketry.

## Settlement, witness and temporary ownership requirements

Replace the reused core's generic `project_native_output_is_authentic` settlement gate with exact source/family validation and explicit mode branches.
For fresh_output, require the matching synchronous `mengele_event016_native_prototype_output_source` witness and do not require `is_special_project_completed` to be visible inside the project output.
For adopted_completed, require the exact selected completed project and no fresh witness.
Reject every other mode rather than treating the current generic else branch as adopted success.
Retain strict provider validity, Theory predecessor, incomplete Prototype, and empty matching paid receipt in both branches.
The Biological family-wide completed OR may remain a read-only historical eligibility probe for the after-Theory driver at 1499-1505, but it must not authorize exact settlement or classify fresh provenance.
Tightening that aggregate predicate without changing its pre-selection caller can accidentally prevent legitimate historical adoption.

The reused core is shared with High Energy, so its reactor literal wrapper must also supply a matching reactor witness if the common fresh gate requires one.
Preserve the reactor output payload and historical adoption behavior, and do not leave it silently blocked by a Biological-only change.

The existing core owns its stage, index, applied result, and package-applied slots before nested helpers at 354-357.
Keep that pattern and retain source/mode/index through application until the provenance arrays are written, before selector cleanup.
Initialize authorization storage in the consuming transaction and clear it on every exit.
Any caller that reads `mengele_event016_native_prototype_result` after return must initialize that slot in its own frame before the call.
Specifically add that initialization before reused adoption at stage effects 1555, because 1557 consumes the returned result and this branch lacks the explicit initializer present at 1535 for the other native families.
If an output caller does not consume the result, no result-dependent operational grant should be invented.

Keep the Theory driver's existing snapshots and restoration at 1507-1515 and 1570-1578.
Any new scratch value needed after a nested call must be established by that consuming caller first, because helper-created temporaries are not guaranteed to survive return.
Temporaries remain unscoped, with no ROOT or PREV prefixes.
Do not represent a mutable witness as immutable callback-generation isolation.

## Historical ambiguity, cleanup and paid timer preservation

Retain D17's historical priority: Anthrax, Plague, Tularemia, Smallpox, weaponized zombies, Black Plague.
With several completed sources, the first exact source is a policy-selected adopted receipt, not evidence of which project completed most recently or started under provider ownership.
Record that chosen source and adopted_completed only after the private output succeeds.
Do not add controls or import Rocketry's separate two-source selection contract into Biological Weapons.
Do not mark remaining historical completions fresh on a subsequent callback.
Absent historical observation is never a reconstructed output witness.

Existing observed flags are already overloaded by both scanning and historical adoption at native effects 505-533.
Retaining them for compatibility is safe only when they have no authority over fresh identity.
They cannot prove a literal output was observed, and adoption must not fabricate any distinct output-only fact.
Do not guess a correction for surviving source/mode history already written by the heuristic.
Report unsupported historical provenance instead of rewriting it from current completed bits.

Remove `brilliant_scientist_mengele_observe_reused_biological_sources` and the provider-only completion rescan caller, or remove the unused reconcile helper after a direct call-site search.
Preserve the current host's existing Prototype synchronization and biological-history capture, and the separate CBRN `on_project_completion` integration.
No country pulse, queue, event target, persistent project pointer, new project ID, technology ID, category, GUI, or selection control is required.
Use the existing source codes 6-11, mode codes, family/stage constants, and fifteen-slot append-only provenance arrays.
Biological family 12 maps to existing index 11 through `prepare_project_index`.
No price, duration, threshold, AI factor, or tuning table change is proposed.

On an active Biological receipt, the literal output may record observation but settlement must return blocked without writing accepted source/mode, clearing a receipt, refunding/debiting resources, or shortening/replacing its timer.
The existing stage receipt/cost arrays, native research payment/progress, and decision timer remain authoritative.
A later deliberate history path can only be adopted, never a replay of fresh output.
Do not invent automatic cancellation-time adoption or a new retry policy while removing the scan.
Provider-loss and terminal cleanup keep their existing paid cancellation behavior in the original owner scope, preserve learned output and provenance, and clear only transient witness/authorization through the existing selector epilogue.

Preserve every native output payload in order, including delivery technologies, CBRN decision-surface publication, `bioweapon_available`, facility safety effects, `complete_weaponized_zombie_project_from_project_output`, `black_plague_weaponization_complete_program`, and Black Plague facility history.
The hook must run independently of private settlement success so ordinary country outputs remain intact.

## Parent migration and meaningful validation

1. Add the six literal wrappers and exact reused-source predicates, update the shared core and reactor witness, and preserve all original project payloads.
2. Remove only the provider heuristic path and initialize the reused adoption result in its consuming caller.
3. Update native helper documentation, the stage helper contract, `native_prototype_ownership.md:62-68`, and D17 to distinguish witnessed output from fixed-order historical adoption.
Remove the inaccurate heuristic claim and the delayed-observation-as-fresh limit at native helper documentation 321.
4. Review these scenarios against final source: all six literal identities, output before completed-bit visibility, unrelated completion with historical unobserved Anthrax, actual Plague output with stale Anthrax history, multiple historical completions, absent Theory, invalid provider, current-host exclusion, duplicate output, unsupported/mismatched source or mode, active matching paid receipt, nested result lifetime, and selector cleanup between consecutive source calls.
Compare each complete project definition with its pre-edit source after stripping only the owned additive hook, including native rewards and facility outputs.
Verify a blocked active receipt preserves every paid cost slot, active stage, and timer identity, and that repeated output leaves accepted provenance unchanged.

Completed here: exact current source reads, both counterexample paths, adoption/receipt/source mapping review, six output-boundary reads, installed vanilla output precedent, and offline/installed reference reads.
Implementation, payload-preservation comparison after edits, final source scenario harness, and final wiring tests are parent-owned and were not run by this read-only worker.
No weighted helper or AI change is proposed, so no probability balance target or audit is introduced by this handoff.
No simplifications are proposed.
This recommendation completes the bounded source audit, not Event016 implementation or its fifteen-family completion claim.

## Native Start/cancel and evidence limits

Native Start/cancel synchronization, automatic matching cancellation cleanup, same-project release/reselection, and delayed callback generation isolation remain unresolved without waiver.
The amendment at 20-24 and 57-61 and current ownership document at 109-114 explicitly retain those requirements.
Exact output proves the particular output boundary, not native payment or native Start ownership, because scripted `complete_special_project` can also produce country output.
`is_special_project_being_researched` is an observation, not a callback seam.
Bounded project/on-action reference inspection established completion output and completion callback scopes, but no effect-bearing Start/cancel seam.
This is a bounded research gap, not a claim that no engine integration could exist.
No daily polling, explicit withdrawal substitute, or undocumented native callback is recommended.

Live MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`.
`reference_context`, `reference_search`, `reference_read`, `source_lookup`, and `script_validate` were exposed with their live schemas.
The initial reference-context question exceeded the live 160-character bound and was corrected.
Context omitted Scopes, so that section was read directly with its SHA-256 below.
The query `on_special_project_completed` returned no matches, and the actual documented callback is `on_project_completion`.
Successful helper lookup revision `e0cdde3d6dafc32996b00cf30e69dbe2aaa60d85158c4cfbd07ef7347cb10fb6` returned native effects 414-486, but referencesComplete was false with 19,767 unresolved references.
Project lookups for `anthrax_bomb` and `sp_nuclear_reactor` at index revision `cb8d66dba54f48f0368336027c46babd6d906ac7f835b17351149fb7966c699d` returned zero definitions and suggestions only, so exact local project reads supply source evidence, not indexed project coverage.
`event_inspect(mode=trace, selector={kind:event,eventId:chaosx.nr16.1}, maxDepth=1, maxNodes=4, maxEdges=4, expandHelpers=false)` returned `JOB_WORKER_EXIT`, with blocker text `The worker stopped without publishing a terminal job outcome` and no artifact.
Event-domain lifecycle coverage remains blocked, and no render/compare artifact exists for this audit.
No helper_expansion, job route, task negotiation, game launch, or live gameplay observation was used.
`script_validate` checked a COUNTRY trigger snippet pairing the Anthrax source comparison with `is_special_project_completed = sp:anthrax_bomb`.
Its final result was `SCRIPT_CHECK_PARTIAL`, `valid = null`, `parametersChecked = false`, with syntax, command-kind, and declared-scope checks performed for two commands.
It returned one unresolved `SCRIPT_ARGUMENT_BLOCK_UNCHECKED` finding for `check_variable`, no omitted findings, and documentation revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The cited installed comparison section at 2110-2135 was then read through `reference_read`, confirming the proposed source-comparison form, but this does not convert the partial tool result into complete engine evidence.
The final path/line lookup returned source-location revision `4b4092c94a3a94b8330429b6c7a1d9f6ada3e6b062f89200d201d24f8930e149`, zero owners/definitions, and a comment at line 352 after a concurrent parent edit shifted the file.
It does not provide an indexed helper-body proof.

## Concurrent parent checkpoint

After the initial source audit, the parent changed the helper files while this handoff was being drafted.
A focused reread observed the six proposed literal wrappers at native effects 407-465, the updated shared core at 354-390, and the reactor witness at 394-402 under hash `7a09c707496bb1be6f62a58076f1e2eb9cf00e355ea361c61f17e5ead6328712`.
The parent's pure predicates at native triggers 313-391, hash `a2f308d7fbefdaf141f665ff17585b3a24a2466310d2da27f19105f2d3b4d402`, provide exact family/source mapping, exact historical completed queries, and explicit fresh/adopted branches through `brilliant_scientist_mengele_reused_native_prototype_evidence_is_valid`.
That consolidated predicate is compatible with the recommended helper map and does not require three separately named predicates for style alone.
The stage effects then had hash `a8130f660b3dafb779b8023a9ca387afe2f3c14c3b3d1506102821993104b705`.

One concrete follow-up remained in that checkpoint: the after-Theory reused branch at 1555 still called adoption without first initializing its consumed native result in the caller frame.
Add `set_temp_variable = { mengele_event016_native_prototype_result = constant:mengele_event016_native_prototype_result.none }` there before the call.
Also explicitly reset the adopted transaction's output witness to none and initialize core authorization to zero for a self-contained entry contract.
These are helper-contract recommendations, not edits by this worker.
The three biological project files still matched their initial hashes at this checkpoint, so parent-owned output wiring and payload-preservation validation remained pending at the time of that read.
This is a bounded observation of work in progress, not a final integration verdict or completion claim.

## Revision-bound reference record

Paths below are relative to the repository or installed HOI4 root `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV` as labelled.
Hashes identify bytes reviewed and do not assert that another agent's subsequent shared-tree edits were audited.

| Reference | Read spans | SHA-256 / returned revision |
| --- | --- | --- |
| Installed `common\special_projects\projects\documentation.md` | 198-220, MCP read | `16879504bc72aa357f1d3c0f1093e94a3946f8c35e7942f65ac9a5d3bcd6c643` |
| Installed `documentation\triggers_documentation.md` | 2110-2135 and 6228-6257, MCP reads | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation\effects_documentation.md` | 2896-2924, MCP read | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 437-443, MCP read, and 263-282 local | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 245-263, local coverage of omitted context source | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Offline `paradox_wiki\On actions - Hearts of Iron 4 Wiki.md` | 618-623, local | `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a` |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 4683-4714, local | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 2359-2390, local | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Installed `documentation\script_concept_documentation.md` | 216-248, local | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md` | 1-62, local | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Installed `common\special_projects\projects\nuclear_projects.txt` | 1-67, vanilla output precedent | `b822068268cf848ba9dc9000d762c7005bdde4f6773dd5509e17ce895165e83f` |
| Installed `common\on_actions\12_wuw_on_actions.txt` | 1782-1796, vanilla callback precedent | `df3ac91124cb5faa91e9806ebc2e632c05a95bdb6d8c8261abb7649d424a8e88` |

## Initial audited source identities

| Repository source | SHA-256 at audit |
| --- | --- |
| `common\scripted_effects\016_mengele_native_prototype_effects.txt` | `67551532bbdbb54561382223a9ee5add9bcf6fdddc4b93d9b7faa60e9c6b7e54` |
| `common\scripted_effects\016_mengele_project_stage_effects.txt` | `8c5b0f3deb9c80076c64df75370dcce268df72be0f4c58ecc68afc47d3508a62` |
| `common\scripted_triggers\016_mengele_project_stage_triggers.txt` | `5ab7041ce22f13fbfecf641f4ca9e6fc7d693ddf366da14e631a3dfa498e537c` |
| `common\script_constants\016_mengele_native_prototype_constants.txt` | `4786d781a7bbd004ef5b3da116e0e2eb93fa781092cf4b2a3d2e3f8933bb341a` |
| `common\on_actions\016_brilliant_scientist_project_on_actions.txt` | `03caec9d32201475694fd9f648a7f98daffa4c4195a51a8ef3d436950a940b37` |
| `common\special_projects\projects\biowarfare_main_projects.txt` | `284761390b351cffa78dfc0df46cb56b9c970ff88f5b5986b6958159d85e4103` |
| `common\special_projects\projects\zombie_weaponized_projects.txt` | `3012d2b3d3f04cdc0caa96a17af0cfcf56eeb2e32162ebaa15de32bf93b5a99c` |
| `common\special_projects\projects\020_black_plague_weaponization_projects.txt` | `29bb94783f1dac6f5945c7d8bf3436bead255243dd1009622be34c931554acf6` |
| `docs\events\016_brilliant_scientist\systems\native_prototype_ownership.md` | `6aabfb80c13dad5ec6ec7be75432740afa1d6a81822d4db091957c1a9478210a` |
| `docs\specs\016_brilliant_scientist_specs\specs\016_native_prototype_ownership_amendment_2026-10-03.md` | `3f21bb821587839a452f50c34ee3795bce4dc6295c298dcd10d19307b6df4747` |
| `docs\plans\016_brilliant_scientist_plans\agent_decisions_2026-10-04.md` | `11b4f4988183f100c95bff5048f5ce95e55f77de2363dba46afbc4c285990444` |

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or updated within this read-only delegation.


## Parent patch source review and conservative-frame driver

Disposition: the reviewed parent patch corrects both stale-source counterexamples and preserves the existing native payloads.
At the initial parent checkpoint, the result-consuming after-Theory caller needed one local storage initializer.
That finding is implemented and closed by the final rereview below.
The seven wrappers, strict exact source/family/mode predicates, fixed-order historical adoption, paid receipt protection, and cleanup match the recommended correction.
No new selection controls or native clock substitution was found.
Only this handoff and an outside-repository scratch driver were written by this worker.
The scratch driver is `C:\Users\klimp\AppData\Local\Temp\chaosx_bio_exact_review_20261007\driver.py`.
The initial checkpoint driver SHA-256 was `b3ba6a768198788adff69e9ac22ed6fa23b3c317c93b7383255efbe94b606a5c`.
The final driver replaces it at the same scratch path and in the embedded block below.
The complete driver is embedded below so its survival does not depend on the scratch directory.

Scaffold source is `016_native_electronics_core_2026-10-03.md`, SHA-256 `9813633165386e3fa2db3ec0428f3f7ebc702bbb244fdee8ea15c9fc6eec291e`.
Its parser and Model were reused, with quote-aware comment tokenization, support for anonymous schema blocks, NOR semantics for multi-entry NOT, COUNTRY ROOT callback handling, and explicit recording stubs for operational package calls.
The driver parses the current helper/trigger corpus and script constants, evaluates actual Event016 source bodies, and overlays the two frozen baseline effect files only for the old scanner regressions.
Baseline directory is `C:\Users\klimp\AppData\Local\Temp\chaosx_bio_exact_687b8f1f6be84e7e95906d84a5cc7458`.
The baseline hashes match the initial source identities above.
No receipt writer, predecessor predicate, matching paid-receipt predicate, exact source predicate, mode classifier, wrapper, historical selector, or Prototype output body was replaced with a hand-authored model of its expected behavior.
Executed unknown commands fail the suite rather than silently succeeding.

The initial parent-checkpoint run executed 1,814 cases with all listed assertions passing.
The lifetime differential intentionally asserts the observed defective caller behavior as regression evidence, so this count does not imply that the remaining source defect is acceptable.

| Suite | Cases | Source behavior exercised |
| --- | --- | --- |
| Fresh receipt write matrix and duplicate output | 560 | All seven sources across valid/invalid provider, Theory present/absent, private Prototype present/absent, completed bit true/false, and active paid stage 0-4, with actual persistent source/mode writes and duplicate suppression |
| Witness, mode, family and exact historical source | 595 | Missing/zero/wrong/matching witness, supported/invalid/fractional source, valid/invalid mode, family mismatch, exact completed query versus only another project completed |
| Historical receipt matrix and fixed-order subsets | 623 | All seven sources under the same lifecycle/paid matrix, plus every one of the 63 nonempty Biological historical completion subsets retaining D17 priority and adopted mode |
| Frozen old scanner counterexamples | 3 | Actual old generic callback falsely settles historical Anthrax on unrelated completion and on Plague completion, plus direct execution of the frozen old observer under conservative frames with caller-owned storage |
| Output before Theory followed by adoption | 7 | Exact output observation without private Theory, then exact completed source adoption after Theory, with adopted provenance |
| Actual Theory consumer lifetime differential | 4 | High Energy and Biological after-Theory source branches with result storage present versus absent in the consuming outer frame |
| Actual country-output hook boundaries | 14 | The exact first hidden country-output call for reactor and six Biological projects, under valid/invalid provider, before the country completed bit is visible |
| Minimal caller storage and sequential family cleanup | 8 | Every literal wrapper with only caller result storage, followed by Biological then reactor calls with exact independent receipts and cleared scratch selectors |

Every applicable case verifies unchanged active-stage and all four direct-cost arrays, with nonzero cost values in every family slot.
A sentinel at provenance index zero remains untouched, and source, witness, mode, family, requested stage, project index, and authorization all read zero after the transaction epilogue.
Fresh settlement authorization makes zero completed-project queries in this model because availability reconciliation is explicitly stubbed.
This proves that source identity is independent of completed-bit timing within the modeled output boundary.
The fixed-order test asserts policy-selected historical adoption, without inventing a latest-project identity.

The current generic provider callback invokes no Mengele scanner, so unobserved historical Anthrax remains unsettled on unrelated completion.
The current literal Plague output with historical Anthrax present persists source 7/fresh mode 1.
Executing the actual old callback on the frozen baseline instead persists source 6/fresh mode 1 in both cases.
The third old regression supplies caller-owned storage and uses conservative return semantics, demonstrating that the stale-source flaw is independent of the temporary-lifetime issue.

### Initial temporary-storage finding, closed by final rereview

Under stage effects hash `a8130f660b3dafb779b8023a9ca387afe2f3c14c3b3d1506102821993104b705`, the reused after-Theory branch at 1555 still lacks its own result initializer.
With no outer result slot, actual private adoption writes the correct source/adopted receipt, but the branch at 1557 sees result zero and skips its success-only call.
Providing result storage before calling the same unchanged source makes High Energy invoke the bridge with family 5/result 3 and Biological invoke it with family 12/result 3.
Both variants retain the original Theory selector/results on return.
The parent should initialize `mengele_event016_native_prototype_result` to `constant:mengele_event016_native_prototype_result.none` immediately before the reused adoption call.
No gameplay file was patched by this worker.

The original `brilliant_scientist_mengele_grant_native_custom_operational_package` source currently has no High Energy or Biological grant branch.
Consequently, the differential proves a broken success-result/call contract, not a missing actual Biological technology or operational reward.
The driver records that bridge call as a stub and does not claim to execute the full grant.
Explicitly clearing the historical witness and initializing core authorization at entry remain useful contract hygiene, but no additional false settlement or paid-receipt mutation was observed from their current entry values in the reviewed source paths.

### Native payload preservation and source identities

Independent byte comparisons removed only the six added literal hook lines from the three current project files.
The remaining complete files equal the frozen originals byte-for-byte, including every original project definition, country/facility payload, reward, cost and timing field.
This is source preservation evidence and does not execute native project payloads in the test model.

| Current source | SHA-256 used in review |
| --- | --- |
| Native effects | `7a09c707496bb1be6f62a58076f1e2eb9cf00e355ea361c61f17e5ead6328712` |
| Stage effects | `a8130f660b3dafb779b8023a9ca387afe2f3c14c3b3d1506102821993104b705` |
| Native triggers | `a2f308d7fbefdaf141f665ff17585b3a24a2466310d2da27f19105f2d3b4d402` |
| Project on-actions | `45ed55fcb068b61d899eeb37bbba438a41a8c1b007909c64abfe0a9c7b56ed56` |
| Biowarfare projects | `ed13cc3b598ec892e3548136c3f3ae1e66c887c287d4ef953c37767eae20d350` |
| Weaponized zombie project | `c3782d09caa4cd1c3f9580a45b6567bb5b65ce9b2d5f947f7df2b8cb7211cda7` |
| Black Plague project | `4c4db2d712c0d79ee7cbd84bf02c2168da79a21ce18d5a74d50ef82ee6c3660c` |

Final parsed corpus count is 809 helper/trigger files plus the script constant files.
The sorted source-inventory digest printed by the final driver run was `2165611f1e9c9b3d74a15c226b0e30faac2438f9b9a67df96e16728f5049ecbb`.
Whole-corpus parsing reports one explicit gap, `common\scripted_triggers\011_secret_alliance_triggers.txt`, with `IndexError('list index out of range')`.
No executed Event016 helper or required source constant comes from that file, and no fallback definition was substituted for it.
The bounded executed closure is covered, while whole-repository parsing is not claimed complete.
This parser result alone is not an engine diagnosis of that unrelated file.

Before the parent took independent MCP ownership, a fresh pure-trigger lookup succeeded at revision `8f72bb1ea2eb7e3dcb8c6cb46a9b1f06cd146d1505d0bc490c70c26beae1db2a`, returning the complete exact evidence predicate at native triggers 379-391.
A two-node root event trace again returned `JOB_WORKER_EXIT`, with no artifact and the same missing terminal worker outcome.
No further MCP calls were made after the parent took that ownership.

Strict provider validity, current-host identity, native completed/research state, and engine callback timing are supplied fixture inputs.
Availability reconciliation and modifier refresh are stubbed, and original native rewards, facility effects, custom grants and conventional packages remain stub boundaries.
The driver executes no decision timer, native research clock, native resource payment, CBRN full payload, or live engine callback.
It does not prove native Start/cancel synchronization, automatic matching cancellation cleanup, payment provenance, resume behavior, or immutable callback generations.
Those stronger requirements remain unresolved without waiver.
The parent owns the initializer fix, final docs, independent rerun, payload review, final domain validation, and all completion claims.
No gameplay simplification was proposed or applied.

### Reproduction

Run the embedded block from the Chaos Redux root, or run the scratch file with `python C:\Users\klimp\AppData\Local\Temp\chaosx_bio_exact_review_20261007\driver.py` from that root.
The driver itself reads source only and writes no files.
The pinned baseline Git commit must remain available locally.
The final reproducibility revision below removes the driver dependency on the Temp snapshot directory.
The embedded final consumer-lifetime suite requires the success-only bridge call with or without preexisting outer storage.
A separate frozen-baseline suite retains reproduction of the earlier missing-initializer failure.


## Final source rereview after parent corrections

Disposition: the bounded exact-output helper correction is source-reviewed with the temporary-storage finding closed.
This supersedes the pending-initializer status of the earlier checkpoints, while retaining their old scanner and lifetime counterexample evidence.
Native Start/cancel synchronization, matching cancellation cleanup and immutable callback-generation requirements remain unresolved without waiver.
The parent owns final documentation, independent rerun, payload-preservation checks and domain completion claims.
The earlier CXT documentation write problem was outside this worker's file ownership.
The parent subsequently reported completing an atomic replacement limited to its two owned observer-documentation lines, with the source no-extra-grant contract preserved.
This worker did not independently edit or audit that document, and no alternate CXT documentation file or foreign hunk was touched here.

The current after-Theory branch initializes its own native result before reused adoption.
The shared reused core owns authorization storage at zero on entry.
Historical adoption explicitly clears the fresh-output witness, and the adopted evidence branch accepts only a none witness plus the exact completed source query.
The final driver changes the direct-core adopted-mode matrix to reject nonzero witnesses, verifies historical entry clears stale witnesses, and requires the actual after-Theory success call in both outer-storage states.
High Energy and Biological private receipts and the original Theory selector/results remain correct in all four consumer cases.
Without outer result storage, the final public return value may disappear under conservative lifetime, but the consuming after-Theory frame has already invoked its correct success callback.
The frozen old stage/observer/core source still reproduces the two original scanner failures and the two caller-storage failures.

Final driver results: 2,264 cases, no assertion failures.
The original eight suite counts remain 560, 595, 623, 3, 7, 4, 14 and 8, with the consumer suite now asserting corrected behavior.
Additional suites are 28 historical-witness reset/authorization-entry cases, 2 frozen old Theory storage regressions, and 420 CXT probe cases.
Driver SHA-256 is `81690376bd052843742ef65b674a34c4a72bec1fa5a5273298d2361e42045284`.
That checkpoint used a 451-line scratch driver.
The immutable-Git reproducibility revision below supersedes it and supplies the exact final embedded bytes.
The final source-inventory digest is `567f18c5fc2cbf413a94e1f36168184b436b540d8d273b85ec107ceafaf864c9`.
The helper/trigger corpus count is 810 successfully parsed files, with the same explicit unrelated Event011 parser gap.
All executed Event016 bodies and required numeric source constants parse, and no missing executed command was substituted.

| Final source | SHA-256 |
| --- | --- |
| `common\scripted_effects\016_mengele_native_prototype_effects.txt` | `436055f09c3a35f9a96a66516c4bc72f96d64194e01b6567158af30fdd67db60` |
| `common\scripted_effects\016_mengele_project_stage_effects.txt` | `de9639a7161c1e12e0e0fa224922460028c2e1907b16f4d3a972d2adf30b428d` |
| `common\scripted_triggers\016_mengele_native_prototype_triggers.txt` | `2cd654f39c08bcd8ca8400cd26b506625f6975a790720547da551d4cc71aa5ac` |
| `common\scripted_effects\016_mengele_native_ownership_cxt_effects.txt` | `cf5c28dc2901c42d909f677283a54d8cfd1e34d6a8381cfb458dc24af2f6a805` |

### Bounded CXT observation audit

The exact current CXT probe body was executed without a grant stub replacing it.
A tag and initialized-country fixture supplies only its entry gate.
All 289 combinations of independent source/mode array lengths 0 through 16 were checked, including both boundaries around High Energy family 5/index 4 and Biological family 12/index 11.
Snapshots reset to none unless both arrays contain the family's slot, so a short mode array cannot leave a stale source snapshot.
An entirely absent array pair remains absent, and the probe performs no append-only receipt initialization.
All 128 subsets of the seven reused observed flags were copied exactly, then a second probe removed every stale copied flag after the source flags disappeared.
Wrong-tag and uninitialized callers made no persistent or temporary change.

Every CXT case retained all provider arrays, paid receipts and original flags.
Persistent writes were confined to `chaosx_cxt_*` debug variables and flags.
The only executed helper call was the probe itself, with no package bridge, modifier, technology grant, native completion, payment, refund, selection, stage output or carrier registration.
The temporary probe index reads zero after return.
The snapshots copy the current source/mode and existing observed-marker semantics without proving fresh output, native payment, Start ownership or callback generations.
Full native payload and operational-grant boundaries remain explicit model stubs in the other suites, and no live-game result is inferred.
No gameplay simplification or stronger lifecycle waiver was introduced.


## Immutable baseline and independent final rerun

The snapshot recorded Git HEAD `63f0799041f303d5d051dbdf22f8cd0bca5f7a48` in `C:\Users\klimp\AppData\Local\Temp\chaosx_bio_exact_687b8f1f6be84e7e95906d84a5cc7458\head.txt`.
That file's raw SHA-256 is `12aacb318b01bebf4c82d36f88144853e4126c9d1d05f4f70b8274f90b8e14d1`.
All six copied source files were compared directly with that commit's raw blobs.
Stage effects and biowarfare projects match byte-for-byte.
Native effects, project on-actions, Zombie projects and Black Plague projects have identical content after replacing CRLF with LF, and the raw byte difference is confined to line endings.
No gameplay or helper-content delta was silently substituted for the snapshot.
The raw before-source hashes and newline distinction remain explicit so normalized content equality is not misreported as raw blob equality.

The final driver pins that full commit ID, uses read-only `git show <commit>:<path>` for the old two effect files and on-action callback, and verifies their raw SHA-256 values before parsing them.
It uses neither a moving HEAD nor a Temp fallback.
Missing Git objects or unexpected blob bytes stop the rerun with an error.
Thus both old scanner failures and the old caller-storage regression are independently reproducible from immutable Git source.
The embedded driver carries the complete source and no longer reads the snapshot directory or head.txt at runtime.

| Before-source path at pinned commit | Git blob SHA-256 | Snapshot relation |
| --- | --- | --- |
| `common\scripted_effects\016_mengele_native_prototype_effects.txt` | `34b9ff4bb2db62597eff8d88f078f73b5906ac86c61d3752a5c04349a7d50da6` | Same content, Git LF versus snapshot CRLF |
| `common\scripted_effects\016_mengele_project_stage_effects.txt` | `8c5b0f3deb9c80076c64df75370dcce268df72be0f4c58ecc68afc47d3508a62` | Raw bytes identical |
| `common\on_actions\016_brilliant_scientist_project_on_actions.txt` | `32623dbcc250a9a04af64a2d0b4eb14c98586a815cc44370666e2654558e995b` | Same content, Git LF versus snapshot CRLF |
| `common\special_projects\projects\biowarfare_main_projects.txt` | `284761390b351cffa78dfc0df46cb56b9c970ff88f5b5986b6958159d85e4103` | Raw bytes identical |
| `common\special_projects\projects\zombie_weaponized_projects.txt` | `0b3dad3bec4f5ef1a2a745706732206f1984bef089d65b9f517e59e8d5e3ae16` | Same content, Git LF versus snapshot CRLF |
| `common\special_projects\projects\020_black_plague_weaponization_projects.txt` | `eae7e9044a2e72078bfacad6e9580856192868d0918162021534c2b9e74d32ab` | Same content, Git LF versus snapshot CRLF |

The final post-initializer independent rerun with Git-backed before sources passed all 2,264 assertions, with all eleven suite counts unchanged and no failures.
Both High Energy and Biological after-Theory success callbacks execute with or without outer result storage, and all 420 CXT observation cases pass.
The four final helper/trigger/CXT hashes in the prior table remain unchanged.
The latest whole-corpus run parsed 812 helper/trigger files and printed source-inventory digest `4c24a173e7336a91d3816f7bfa05715543dc26eb08ee5f0d548f7b0a67561986`.
The same unrelated Event011 parser coverage gap remains explicit.
Final reproducible driver SHA-256 is `28b1cf62c1f2d46ab61d6f056088ecab9f63ccdf0c89127cf959328f2e05b2ac` with 464 lines.
The earlier driver digests identify historical checkpoints and are superseded by this final driver for independent reruns.

### Parent-reported final domain limits

The parent reported partial file validation with unknown command/root-scope classifications and unchecked native argument blocks, and partial scoped-predicate validation where scripted helper definitions were not documented as native commands.
The parent also reported reading the exact installed `check_variable` section.
Those partial results do not establish full argument semantics, helper lifecycle or live engine behavior.
The reported event file inspection returned `JOB_WORKER_EXIT`, followed by a narrowed one-node request timing out after 600 seconds.
These are limitations of the reported requests and do not establish a global service outage.
No artifact URI or additional final-domain revision was supplied in this message, so this worker records the reports separately from its own earlier tool results.
No further MCP calls were made after the parent took independent domain ownership.
The strong native Start/cancel and matching-cancellation requirements remain unresolved without waiver.
No gameplay simplification, new grant, new carrier, or source edit was made by this worker.

```python
from pathlib import Path
import re, itertools, subprocess, copy, hashlib, json
root=Path.cwd()
prefix='brilliant_scientist_mengele_'
base='mengele_event016_'
def parse(text):
    ts=[t for t in re.findall(r'"(?:\\.|[^"\\])*"|#[^\n]*|[{}=<>]|[^\s{}=<>#"]+',text) if not t.startswith('#')]
    pos=0
    def block():
        nonlocal pos
        out=[]
        while pos<len(ts) and ts[pos]!='}':
            k=ts[pos];pos+=1
            if k=='{':
                v=block();assert pos<len(ts) and ts[pos]=='}';pos+=1
                out.append(('__anonymous_block__','=',v));continue
            if pos>=len(ts) or ts[pos] not in ('=','>','<'):
                continue
            op=ts[pos];pos+=1
            if ts[pos]=='{':
                pos+=1;v=block();assert ts[pos]=='}';pos+=1
            else:
                v=ts[pos].strip('"');pos+=1
            out.append((k,op,v))
        return out
    value=block()
    assert pos==len(ts), ('unconsumed tokens',ts[pos:pos+5])
    return value
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
            elif k in ('hidden_effect','custom_override_tooltip','ROOT'):self.effect(v)
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
# Extension of the embedded Electronics scaffold. Parse every current helper,
# trigger and constants file, then execute only the bounded reused-source closure.
BASELINE_COMMIT='63f0799041f303d5d051dbdf22f8cd0bca5f7a48'
before_expected={
 'common/scripted_effects/016_mengele_native_prototype_effects.txt':'34b9ff4bb2db62597eff8d88f078f73b5906ac86c61d3752a5c04349a7d50da6',
 'common/scripted_effects/016_mengele_project_stage_effects.txt':'8c5b0f3deb9c80076c64df75370dcce268df72be0f4c58ecc68afc47d3508a62',
 'common/on_actions/016_brilliant_scientist_project_on_actions.txt':'32623dbcc250a9a04af64a2d0b4eb14c98586a815cc44370666e2654558e995b'}
before_hashes={}
def git_before(rel):
    raw=subprocess.check_output(['git','show',BASELINE_COMMIT+':'+rel])
    digest=hashlib.sha256(raw).hexdigest()
    assert digest==before_expected[rel], ('baseline blob mismatch',rel,digest)
    before_hashes[rel]=digest
    return raw
all_paths=sorted(Path('common/scripted_effects').glob('*.txt'))+sorted(Path('common/scripted_triggers').glob('*.txt'))
source_hashes={};defs={};parse_gaps=[]
for p in all_paths:
    raw=p.read_bytes();source_hashes[str(p)]=hashlib.sha256(raw).hexdigest()
    try:parsed=parse(raw.decode('utf-8-sig'))
    except Exception as e:
        parse_gaps.append({'path':str(p),'error':repr(e)})
        continue
    defs.update({k:v for k,o,v in parsed if isinstance(v,list)})
const={}
def constants(b,path=''):
    for k,o,v in b:
        name=path+'.'+k if path else k
        if isinstance(v,list):
            if k!='schema':constants(v,name)
        elif re.fullmatch(r'-?\d+(\.\d+)?',v):const[name]=float(v)
for p in sorted(Path('common/script_constants').glob('*.txt')):
    raw=p.read_bytes();source_hashes[str(p)]=hashlib.sha256(raw).hexdigest()
    try:parsed=parse(raw.decode('utf-8-sig'))
    except Exception as e:
        parse_gaps.append({'path':str(p),'error':repr(e)})
        continue
    constants(parsed)
old_defs=dict(defs)
for rel in before_expected:
    if rel.startswith('common/scripted_effects/'):
        old_defs.update({k:v for k,o,v in parse(git_before(rel).decode('utf-8-sig')) if isinstance(v,list)})
def child(b,k):return next(v for key,o,v in b if key==k)
def callback_text(text):return child(child(child(parse(text),'on_actions'),'on_project_completion'),'effect')
def callback(p):return callback_text(p.read_text(encoding='utf-8-sig'))
current_callback=callback(Path('common/on_actions/016_brilliant_scientist_project_on_actions.txt'))
old_callback=callback_text(git_before('common/on_actions/016_brilliant_scientist_project_on_actions.txt').decode('utf-8-sig'))
class ReviewModel(Model):
    def __init__(self,definitions=None):
        super().__init__(defs if definitions is None else definitions);self.conservative=True;self.calls=[];self.tag='CXT'
    def one(self,k,op,v):
        if k=='tag':return self.tag==v
        if k=='NOT':return not any(self.one(*x) for x in v)
        if k==prefix+'project_native_output_is_authentic':return self.cond(self.defs[k])==(v=='yes')
        if k=='brilliant_scientist_is_current_host':return False
        return super().one(k,op,v)
    def rawrun(self,k):
        self.calls.append(k)
        if k==prefix+'grant_native_custom_operational_package':
            self.bridge_calls.append((self.read(base+'native_grant_family'),self.read(base+'native_prototype_result')));return
        return super().rawrun(k)
def code(name):return int(const['mengele_event016_native_prototype_source.'+name])
source_names=[('high_energy_nuclear_reactor','sp_nuclear_reactor','high_energy'),('biological_anthrax','anthrax_bomb','biological_weapons'),('biological_plague','plague_bomb','biological_weapons'),('biological_tularemia','tularemia_bomb','biological_weapons'),('biological_smallpox','smallpox_bomb','biological_weapons'),('biological_weaponized_zombies','weaponize_the_zombies','biological_weapons'),('biological_black_plague','black_plague_weaponization_program','biological_weapons')]
sources=[(code(name),project,family,int(const['brilliant_scientist_project_family.'+family])) for name,project,family in source_names]
def setup(s,provider=True,theory=True,proto=False,active=0,done=False,definitions=None):
    c,p,f,fid=s;m=ReviewModel(definitions);m.provider=provider
    m.flags|={base+'provider_receipts_initialized',base+'singularity_component_entries_initialized'}
    if theory:m.flags.add(base+f+'_theory_completed')
    if proto:m.flags.add(base+f+'_prototype_completed')
    if done:m.completed.add('sp:'+p)
    for suffix in ['active_project_stage','active_cost_political_power','active_cost_support_equipment','active_cost_fuel','active_cost_civilian_factory_commitment','native_later_stage_deployment_source','native_later_stage_weaponization','native_prototype_source','native_prototype_mode']:
        m.arr[base+suffix+'_entries']=[0]*15
    m.arr[base+'active_project_stage_entries'][fid-1]=active
    for suffix in ['active_cost_political_power','active_cost_support_equipment','active_cost_fuel','active_cost_civilian_factory_commitment']:
        m.arr[base+suffix+'_entries']=[101+i for i in range(15)]
    m.arr[base+'native_prototype_source_entries'][0]=901;m.arr[base+'native_prototype_mode_entries'][0]=902
    m.temp.update({base+'native_prototype_result':0,base+'native_prototype_source':0,base+'native_prototype_mode':0,base+'native_prototype_output_source':0,base+'project_family':0,base+'requested_stage':0,base+'project_index':0,base+'project_output_authorized':0})
    return m
def state(m,s):
    i=s[3]-1;return (m.arr[base+'native_prototype_source_entries'][i],m.arr[base+'native_prototype_mode_entries'][i])
def paid(m):return copy.deepcopy({k:v for k,v in m.arr.items() if 'active_' in k})
def protected(m,s,before):
    assert paid(m)==before,'paid receipt or direct cost mutated'
    assert (m.arr[base+'native_prototype_source_entries'][0],m.arr[base+'native_prototype_mode_entries'][0])==(901,902),'other family zero slot overwritten'
    for n in ['native_prototype_source','native_prototype_mode','native_prototype_output_source','project_family','requested_stage','project_index','project_output_authorized']:
        assert m.read(base+n)==0,('selector leaked',n,m.read(base+n))
def literal(m,s):m.run(prefix+'native_completion_'+s[1])
def request(m,s,mode,witness=None,source=None,family=None):
    m.temp[base+'project_family']=s[3] if family is None else family
    m.temp[base+'native_prototype_source']=s[0] if source is None else source
    m.temp[base+'native_prototype_mode']=mode
    if witness is not None:m.temp[base+'native_prototype_output_source']=witness
    else:m.temp.pop(base+'native_prototype_output_source',None)
    m.run(prefix+'settle_reused_native_prototype')
counts={};failures=[]
def suite(name,fn):
    try:counts[name]=fn()
    except Exception as e:failures.append({'suite':name,'error':repr(e)})
def fresh_suite():
    n=0
    for s in sources:
        for provider,theory,proto,done in itertools.product([False,True],repeat=4):
            for active in range(5):
                m=setup(s,provider,theory,proto,active,done);before=paid(m);literal(m,s)
                ok=provider and theory and not proto and active==0
                assert state(m,s)==((s[0],1) if ok else (0,0)),(s,provider,theory,proto,active,done,state(m,s))
                assert m.read(base+'native_prototype_result')==(2 if ok else 5)
                assert m.query_count==0,'fresh source authorization queried completed bit'
                protected(m,s,before)
                if ok:
                    old=copy.deepcopy((m.arr,m.flags,m.modifiers));literal(m,s)
                    assert (m.arr,m.flags,m.modifiers)==old and m.read(base+'native_prototype_result')==5
                n+=1
    return n
suite('fresh_receipt_write_matrix_and_repeat',fresh_suite)
def malformed_suite():
    n=0
    for s in sources:
        for witness,mode,family,done in itertools.product([None,0,s[0],99],[0,1,2,3,1.5],[s[3],1],[False,True]):
            m=setup(s,done=done);before=paid(m);request(m,s,mode,witness,family=family)
            ok=family==s[3] and ((mode==1 and witness==s[0]) or (mode==2 and done and witness in [None,0]))
            assert state(m,s)==((s[0],mode) if ok else (0,0)),(s,witness,mode,family,done,state(m,s))
            protected(m,s,before);n+=1
        for invalid in [0,1,12,s[0]+.5]:
            m=setup(s,done=True);before=paid(m);request(m,s,1,invalid,source=invalid)
            assert state(m,s)==(0,0);protected(m,s,before);n+=1
        m=setup(s,done=False);m.completed.add('sp:'+sources[1 if s[0]==5 else 0][1]);before=paid(m)
        request(m,s,2,None);assert state(m,s)==(0,0);protected(m,s,before);n+=1
    return n
suite('wrong_witness_mode_family_and_exact_history',malformed_suite)
def adoption_suite():
    n=0
    for s in sources:
        for provider,theory,proto,done in itertools.product([False,True],repeat=4):
            for active in range(5):
                m=setup(s,provider,theory,proto,active,done);before=paid(m);request(m,s,2,0)
                ok=provider and theory and not proto and active==0 and done
                assert state(m,s)==((s[0],2) if ok else (0,0));protected(m,s,before);n+=1
    # Every subset of historical Biological projects retains D17 fixed priority.
    for mask in range(1,64):
        m=setup(sources[1]);completed=[s for i,s in enumerate(sources[1:]) if mask&(1<<i)]
        m.completed={ 'sp:'+s[1] for s in completed };m.temp[base+'project_family']=sources[1][3];before=paid(m)
        m.run(prefix+'adopt_reused_native_prototype')
        assert state(m,sources[1])==(completed[0][0],2);protected(m,sources[1],before);n+=1
    return n
suite('historical_receipts_and_fixed_order_subsets',adoption_suite)
def regressions():
    anthrax,plague=sources[1:3];n=0
    for cb in ['unrelated','plague']:
        old=setup(anthrax,done=True,definitions=old_defs);old.conservative=False
        if cb=='plague':old.completed.add('sp:'+plague[1])
        old.effect(old_callback)
        assert state(old,anthrax)==(anthrax[0],1),'old false fresh not reproduced'
        assert prefix+'observe_reused_biological_sources' in old.calls
        new=setup(anthrax,done=True);before=paid(new)
        if cb=='plague':literal(new,plague)
        new.effect(current_callback)
        assert state(new,anthrax)==((plague[0],1) if cb=='plague' else (0,0))
        assert prefix+'observe_reused_biological_sources' not in new.calls
        protected(new,anthrax,before);n+=1
    # Frozen old observer can settle when its consuming caller establishes slots.
    old=setup(anthrax,done=True,definitions=old_defs);old.temp[base+'native_prototype_source']=0;old.temp[base+'native_prototype_mode']=0
    old.run(prefix+'observe_reused_biological_sources');assert state(old,anthrax)==(anthrax[0],1);n+=1
    return n
suite('actual_old_scanner_counterexamples',regressions)
def before_theory():
    n=0
    for s in sources:
        m=setup(s,theory=False);before=paid(m);literal(m,s);assert state(m,s)==(0,0)
        m.completed.add('sp:'+s[1]);m.flags.add(base+s[2]+'_theory_completed');m.temp[base+'project_family']=s[3]
        m.run(prefix+'adopt_reused_native_prototype');assert state(m,s)==(s[0],2);protected(m,s,before);n+=1
    return n
suite('before_theory_output_then_historical_adoption',before_theory)
def consuming_driver():
    outcomes=[]
    for s in [sources[0],sources[1]]:
        for storage in [False,True]:
            m=setup(s,done=True)
            if not storage:m.temp.pop(base+'native_prototype_result')
            m.temp.update({base+'project_family':s[3],base+'requested_stage':1,base+'project_index':s[3]-1,base+'project_output_applied':1,base+'computation_output_applied':0,base+'stage_output_gap':0,base+'project_output_authorized':0,base+'project_availability_reconciled':0,'brilliant_scientist_singularity_component':0})
            outer={k:m.temp[k] for k in [base+'project_family',base+'requested_stage',base+'project_index',base+'project_output_applied',base+'computation_output_applied',base+'stage_output_gap',base+'project_output_authorized',base+'project_availability_reconciled','brilliant_scientist_singularity_component']}
            m.run(prefix+'adopt_completed_native_after_theory')
            assert state(m,s)==(s[0],2);assert all(m.temp[k]==v for k,v in outer.items())
            outcomes.append({'source':s[0],'caller_result_initialized':storage,'bridge_calls':m.bridge_calls,'result_after_return':m.read(base+'native_prototype_result')})
            assert m.bridge_calls==[(s[3],3)], 'after-Theory success callback lost its result'
            assert m.read(base+'native_prototype_result')==(3 if storage else 0)
    print('CONSUMER_STORAGE',json.dumps(outcomes));return len(outcomes)
suite('actual_theory_consumer_lifetime_differential',consuming_driver)

def native_boundary_suite():
    n=0
    files={'sp_nuclear_reactor':'common/special_projects/projects/nuclear_projects.txt',
           'anthrax_bomb':'common/special_projects/projects/biowarfare_main_projects.txt',
           'plague_bomb':'common/special_projects/projects/biowarfare_main_projects.txt',
           'tularemia_bomb':'common/special_projects/projects/biowarfare_main_projects.txt',
           'smallpox_bomb':'common/special_projects/projects/biowarfare_main_projects.txt',
           'weaponize_the_zombies':'common/special_projects/projects/zombie_weaponized_projects.txt',
           'black_plague_weaponization_program':'common/special_projects/projects/020_black_plague_weaponization_projects.txt'}
    for source in sources:
        text=Path(files[source[1]]).read_text(encoding='utf-8-sig')
        body=child(child(child(parse(text),source[1]),'project_output'),'country_effects')
        assert body[0][0]=='hidden_effect'
        assert body[0][2]==[(prefix+'native_completion_'+source[1],'=','yes')]
        for provider in [False,True]:
            m=setup(source,provider=provider,done=False);before=paid(m)
            # Execute the actual hidden output boundary. Remaining native payload
            # stays a recorded boundary, not an invented engine/grant emulation.
            m.effect([body[0]])
            assert state(m,source)==((source[0],1) if provider else (0,0))
            assert m.read(base+'native_prototype_result')==(2 if provider else 5)
            protected(m,source,before);n+=1
    return n
suite('seven_actual_country_output_hook_boundaries',native_boundary_suite)
def sequential_and_minimal_callers():
    n=0
    for source in sources:
        m=setup(source);m.temp={base+'native_prototype_result':0};before=paid(m)
        literal(m,source)
        assert state(m,source)==(source[0],1) and m.read(base+'native_prototype_result')==2
        protected(m,source,before);n+=1
    m=setup(sources[1]);literal(m,sources[1]);m.flags.add(base+'high_energy_theory_completed');literal(m,sources[0])
    assert state(m,sources[1])==(6,1) and state(m,sources[0])==(5,1)
    assert (m.arr[base+'native_prototype_source_entries'][0],m.arr[base+'native_prototype_mode_entries'][0])==(901,902)
    assert all(m.read(base+x)==0 for x in ['native_prototype_source','native_prototype_mode','native_prototype_output_source','project_family','requested_stage','project_index','project_output_authorized'])
    return n+1
suite('minimal_result_callers_and_sequential_family_cleanup',sequential_and_minimal_callers)


def final_entry_contracts():
    n=0
    for source in sources:
        for stale in [1,99]:
            m=setup(source,done=True);m.temp[base+'project_family']=source[3]
            m.temp[base+'native_prototype_output_source']=stale
            m.temp[base+'project_output_authorized']=99;before=paid(m)
            m.run(prefix+'adopt_reused_native_prototype')
            assert state(m,source)==(source[0],2);protected(m,source,before);n+=1
        for mode in [0,3]:
            m=setup(source);m.temp[base+'project_output_authorized']=99;before=paid(m)
            request(m,source,mode,source[0]);assert state(m,source)==(0,0);protected(m,source,before);n+=1
    return n
suite('final_historical_witness_reset_and_authorization_entry',final_entry_contracts)
def old_consumer_regression():
    n=0
    for source in [sources[0],sources[1]]:
        m=setup(source,done=True,definitions=old_defs);m.temp.pop(base+'native_prototype_result')
        m.temp.update({base+'project_family':source[3],base+'requested_stage':1,base+'project_index':source[3]-1,base+'project_output_applied':1})
        m.run(prefix+'adopt_completed_native_after_theory')
        assert state(m,source)==(source[0],2) and not m.bridge_calls
        n+=1
    return n
suite('frozen_old_theory_result_storage_failure',old_consumer_regression)
def cxt_observations():
    n=0;probe='chaosx_cxt_event016_probe_native_ownership'
    observed=['nuclear_reactor','anthrax','plague','tularemia','smallpox','weaponized_zombies','black_plague']
    # Source and mode array length vary independently. Stale snapshots must be
    # replaced by none unless BOTH arrays have the selected family's slot.
    for source_len,mode_len in itertools.product(range(17),repeat=2):
        m=setup(sources[1]);m.flags.add('chaosx_test_country_initialized')
        m.arr[base+'native_prototype_source_entries']=[700+i for i in range(source_len)]
        m.arr[base+'native_prototype_mode_entries']=[800+i for i in range(mode_len)]
        for family in ['high_energy','biological_weapons']:
            m.vars['chaosx_cxt_event016_'+family+'_native_source']=999
            m.vars['chaosx_cxt_event016_'+family+'_native_mode']=999
        arrays=copy.deepcopy(m.arr);flags=set(m.flags);m.run(probe)
        for family,fid in [('high_energy',5),('biological_weapons',12)]:
            full=source_len>=fid and mode_len>=fid
            assert m.vars['chaosx_cxt_event016_'+family+'_native_source']==(700+fid-1 if full else 0)
            assert m.vars['chaosx_cxt_event016_'+family+'_native_mode']==(800+fid-1 if full else 0)
        assert m.arr==arrays,'probe altered provider array schema or receipts'
        assert {f for f in m.flags if not f.startswith('chaosx_cxt_')}==flags
        assert all(k.startswith('chaosx_cxt_') for k in m.vars)
        assert m.calls==[probe] and not m.bridge_calls and not m.modifiers and not m.tech
        assert m.read('chaosx_cxt_event016_native_probe_index')==0;n+=1
    # Every observed-source subset is copied, then removed on a subsequent probe
    # once the original observation disappears. No stale debug flag survives.
    for mask in range(128):
        m=setup(sources[1]);m.flags.add('chaosx_test_country_initialized');arrays=copy.deepcopy(m.arr)
        for i,name in enumerate(observed):
            m.flags.add('chaosx_cxt_event016_observed_reused_'+name)
            if mask&(1<<i):m.flags.add(base+'reused_source_observed_'+name)
        m.run(probe)
        for i,name in enumerate(observed):
            assert ('chaosx_cxt_event016_observed_reused_'+name in m.flags)==bool(mask&(1<<i))
            m.flags.discard(base+'reused_source_observed_'+name)
        m.run(probe)
        assert all('chaosx_cxt_event016_observed_reused_'+name not in m.flags for name in observed)
        assert m.arr==arrays and not m.bridge_calls and not m.tech and not m.modifiers;n+=1
    # Entirely absent arrays and the wrong tag/uninitialized caller are harmless.
    m=setup(sources[1]);m.arr={};m.flags.add('chaosx_test_country_initialized');m.run(probe)
    assert m.arr=={} and m.vars['chaosx_cxt_event016_high_energy_native_source']==0 and m.vars['chaosx_cxt_event016_biological_weapons_native_mode']==0;n+=1
    for tag,initialized in [('GER',True),('CXT',False)]:
        m=setup(sources[1]);m.tag=tag
        if initialized:m.flags.add('chaosx_test_country_initialized')
        before=copy.deepcopy((m.arr,m.vars,m.flags,m.temp));m.run(probe)
        assert (m.arr,m.vars,m.flags,m.temp)==before;n+=1
    return n
suite('cxt_short_arrays_defaults_and_observation_only',cxt_observations)

print(json.dumps({'before_commit':BASELINE_COMMIT,'before_hashes':before_hashes,'suite_counts':counts,'total_executed_cases':sum(counts.values()),'failures':failures,'parsed_helper_trigger_files':len(all_paths)-sum(x['path'].startswith('common\\scripted_') for x in parse_gaps),'parse_gaps':parse_gaps,'source_inventory_sha256':hashlib.sha256(json.dumps(source_hashes,sort_keys=True).encode()).hexdigest(),'boundaries':['strict provider validity and current-host fixture','availability reconciliation stubbed','dynamic modifier refresh stubbed','native payload and custom/conventional package grants stubbed','no live native payment timer or callback-generation claim'],'reviewed_hashes':{k:v for k,v in source_hashes.items() if k.replace('\\','/') in ['common/scripted_effects/016_mengele_native_prototype_effects.txt','common/scripted_effects/016_mengele_project_stage_effects.txt','common/scripted_triggers/016_mengele_native_prototype_triggers.txt','common/scripted_effects/016_mengele_native_ownership_cxt_effects.txt']}},indent=2))
if failures:raise SystemExit(1)
```
