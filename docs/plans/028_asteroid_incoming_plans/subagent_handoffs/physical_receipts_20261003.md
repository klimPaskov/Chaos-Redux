# Event 028 physical receipt correction, 2026-10-03

Disposition: implemented bounded source correction, parent integration and native validation unresolved.
Acceptance basis: the explicit bounded physical transaction assignment in this session, accepted Part 3, Part 4, the tuning matrix, and completion-audit findings F01, F05, F12 and F13.
No commit or game launch was performed.

## Write ownership and immutable baseline

Only `common\scripted_effects\028_asteroid_incoming_effects.txt` and this new handoff are written.
The source changes are confined to physical profile consumption, building removal/capture, physical receipt idempotence, and footprint registration.
Runtime processing, country aggregation/accounting, mineral control, controller hooks, cleanup, decisions, localisation, constants and shared helpers remain parent or other-worker owned.
No new gameplay helper, constant file, event target, branch, periodic hook or balancing change is introduced.
No probability-bearing candidate, weight, tuning value or eligibility check is changed.

The pre-edit bytes are the committed blob `222dbeaca37dc6118665359f8b3908389c7b8440` at commit `9d7862dcb78ae097f61eb95e07e3ff2e911f75db`, path `common/scripted_effects/028_asteroid_incoming_effects.txt`.
Raw blob SHA-256 is `44a5519e86a8e6fcaaf0c681f84ecc77d365383a7cd4092d3d9cb450fad08a44`, equal to the pre-edit working-file raw SHA-256.
The test reads that exact commit blob through byte-preserving subprocess output, verifies its hash, and compares its parsed AST with the actual working source.
HEAD moved during the shared-tree work, so the immutable commit above is used instead of a future HEAD.
The final source identity and test result are recorded below after execution.

## Helper contracts and call order

| Helper | Scope and inputs | Outputs/defaults | Side effects and call sites |
| --- | --- | --- | --- |
| `asteroid_incoming_record_footprint_profile` | State, temporary profile and nonnegative ring, positive global transaction ID, aligned GLOBAL footprint columns | Temporary `asteroid_incoming_profile_recorded`, zero on refusal and one on success, caller must own zero-initialized storage if consumed | Appends one aligned row or updates the exact cached row, retains strongest profile and the minimum ring only within that profile, mirrors state profile/ring and existing planned/transaction flags only on success. Main/fragment planners remain callers. Invalid proof sets existing `asteroid_incoming_transaction_failed_closed`. |
| `asteroid_incoming_load_profile_fractions` | State, saved profile | Four fractions, all zero for unknown profile | Existing getter body and tuning stay identical. `asteroid_incoming_apply_state_transaction` initializes population, industry, logistics and strategic fraction storage before calling it. |
| `asteroid_incoming_prepare_selected_building_loss` | State, selected before level and selected fraction | Rounded, clamped temporary `asteroid_incoming_remove_levels` | Every direct caller initializes this output to zero before calling. No physical mutation. |
| `asteroid_incoming_remove_selected_building_levels` | State, building token and positive prepared removal count | No consumed temporary output | One meta-generated native removal request with explicit state ID and count, replacing the per-level loop. Zero count performs no native request. Exact province targeting remains unresolved. |
| `asteroid_incoming_capture_selected_building_receipt` | State, selected before and after levels | Temporary `asteroid_incoming_selected_actual`, clamped nonnegative observed difference | Every direct caller initializes this output to zero. Adds observed loss once to existing state physical building total. |
| `asteroid_incoming_apply_selected_strategic_building_receipt` | State, selected building token and strategic fraction | Persistent state total changes, no forwarded temporary API | Owns before/after meta readback storage before entering generated text and owns both nested helper outputs. Reads before, prepares count, removes, reads after, captures, adds one strategic receipt. |
| `asteroid_incoming_apply_building_receipt` | State, caller-owned industry/logistics/strategic fractions | Existing physical before snapshot and industry/logistics/strategic/total loss variables | Dispatches every original token exactly once. No nuclear ledger call or package demolition hook is added. |
| `asteroid_incoming_apply_state_transaction` | Valid state selected by the parent, existing resolvable predicate | Existing actual population and physical building receipts | Initializes fractions in its own frame, mutates population once through the existing shared loss helper, registers measured Deaths with no second debit, applies buildings once, and retains existing accounting/mineral flags and calls. Rejected/repeated calls preserve prior receipt values by placing physical zero initialization inside the existing success guard. |

The shared population helper and matching markdown contract were inspected before changing the owner.
No duplicate population helper is created.
The shared helper's recruitable-manpower reconciliation and the asteroid Deaths reason/target inputs stay unchanged.
The building snapshot follows the population transaction, so its population snapshot reads the captured pre-debit population receipt when present.
An isolated building-only caller without that receipt retains the current-population snapshot behavior.

Temporary outputs first created by a child are discarded in the conservative test model.
Inherited caller-owned scalars retain child modifications, including through meta text.
Persistent regular state/global variables and regular event targets have separate storage from temporary scalars.

## Deduplication and category plan

The original sixteen duplicated physical tokens are `biowarfare_facility`, `concentration_camp_site`, `cw_facility`, `extermination_camp_site`, `dam`, `dam_mountain`, `cataract_dam_mountain`, `canal_kiel`, `canal_panama`, `naval_base`, `nuclear_reactor`, `rocket_site`, `nuclear_facility`, `air_facility`, `land_facility` and `naval_facility`.
Each retains its explicit first dispatch and loses the duplicate strategic-extra dispatch.
Ports and canals use logistics once.
The naval research facility uses the strategic fraction and receipt, matching the other three native special-project facilities and Part 3's exposed installation family.
This is a category correction under the supplied single-category assignment, with no constant or percentage change.
All other existing explicit categories are preserved.
Industry includes the existing production/refinery/industrial-infrastructure dispatches.
Logistics includes the existing infrastructure/rail/supply/port/naval-support/canal/energy dispatches.
Strategic includes the existing air/fortification/radar/anti-air/fuel/rocket/reactor/facility/dam/camp/landmark dispatches.

A token's observed loss enters exactly one of industry, logistics or strategic and the physical total once.
It does not enter a second category to feed Dust.
Parent F12 integration must sum actual logistics plus actual strategic destruction before applying the existing one-per-six-level, fifteen-point bounded contributor.
The Dust formula itself is outside this worker's write scope.

## Footprint cache, event targets, cleanup and migration

Two state-owned persistent fields are added inside the existing registration helper: `asteroid_incoming_state_footprint_index` and `asteroid_incoming_state_footprint_transaction_id`.
On append the index is the pre-append GLOBAL state-column length and the transaction mirror is the current positive transaction ID.
All three columns are appended together.
On an existing row, the helper requires both fields, matching transaction, integral nonnegative index, individual bounds for all three columns, and exact state identity after entering the array row.
A stronger candidate replaces profile and its associated ring.
An equal candidate retains the shorter ring.
A weaker candidate changes neither row profile nor row ring.
Actual registration flags are written only after a valid row transaction.

The arrays are append-stable during planning.
Concurrent row removal or reordering is prohibited by this contract.
Identity, bounds, alignment or stale-cache failure rejects without repairing, inventing a state or partially writing registration, and signals the existing failed-closed flag.
Parent must check that signal before any physical mutation.
A pre-existing row lacking the cache is deliberately unresolved rather than source-scanned.
Replanning after clearing arrays obtains fresh indices through the append path.
The next issued transaction supersedes old state cache fields through its transaction identity.
No cleanup hook or global-array layout is changed here.

The existing regular `asteroid_incoming_profile_state_current` target is reused for the exact state identity check.
It remains chain-local and clears with the originating effect chain.
No global target or manual regular-target cleanup is introduced.

Parent has applied caller-owned `asteroid_incoming_lock_result` in runtime target acceptance and caller-owned `asteroid_incoming_prefire_ready` in the shared Event28 prefire dispatcher.
The current reads confirm them at runtime lines 558 to 559 and shared settings lines 4055 to 4058, respectively.
These changes are outside this worker's write set.
The parent reports the runtime history tranche committed as `611c93f8731484aa4a08b195ad3c54d3f47529ea`.

Parent-owned migration:

1. Retain those caller initializations and audit any additional forwarded outputs under the same conservative lifetime contract.
2. Gate resolution on successful complete planning, aligned columns and absence of the failed-closed flag.
3. Replace the runtime array-index while-loop with the documented `every_state` scope iterator once per impact, filtered to the current transaction and existing planned flag, with receipt/application guard and array identity checks as appropriate.
The user expressly permits this transaction-time scan.
Do not introduce periodic world hooks.
4. Preserve one physical processing and one accounting pass for each state, even when several planned profiles overlap.
5. Fold strategic destruction into the existing bounded Dust contributor once.
6. Retain parent-owned report/count/history and mineral/current-controller integration.
No claim is made that `for_each_scope_loop` bypasses the installed 1000-iteration ceiling.

One additional parent-owned output proposal is the opening history payload envelope.
`asteroid_incoming_prepare_random_event_fire` creates `events_log_history_payload_override` and `events_log_history_payload_override_active` at runtime lines 282 to 283, and the shared logger consumes them at `chaosx_events_log_effects.txt` lines 690 to 691.
The Event28 dispatcher branch inspected here preinitializes readiness but does not itself preinitialize those two forwarded payload outputs.
The parent should establish whether they already have caller-owned storage in the actual outer dispatch frame, and otherwise initialize both to zero in the owning Event28 caller before invoking the prefire helper.
This is a scoped lifetime proposal with downstream history consequences, not a patch or proof of an observed incorrect history row.
The current runtime/settings read identities are `4F657B6E2E68CFF3324A1DB6F6580059BAF41BF3F0DFF0D5B06D77F081D8FB12` and `577119DA0C1F1A512FB79C597959BDDFCFC21D3653EE6770DF173CA1EC07ECEA`.
Physical getters do not forward temporary outputs beyond the state transaction wrapper, so the wrapper's fraction storage covers both child consumers.
The shared population helper's reconciled-gain temporary output is not consumed by this physical owner, which measures population again instead.

## Native installation and queued-project gaps

Installed native `remove_building` documentation says it removes levels in a specified state or province, and explicitly warns that omitting a province does not recursively find province buildings.
The current adapter passes an explicit state but no province.
A state aggregate reader is therefore insufficient proof that naval bases, forts, supply nodes, rail segments, special facilities, dams, canals, camp visual anchors or landmarks are removed.
The source model uses an explicit aggregate removal callback for arithmetic and call-order testing only.
It cannot close province targeting or rail-segment semantics.

Installed definitions show `province_max` on naval bases, supply nodes, railways, bunkers, coastal bunkers, all four special-project facilities, all three dams and both canals.
The mod's biological/chemical facilities, camp visual anchors and anomaly pilot also have provincial caps.
Camp networks themselves are state buildings.
Dams have flood-related province damage modifiers, canals have named state damage modifiers, and facilities carry specialization and supply/detection data.
Removal is not documented to invoke those raid/damage side effects.
No flood, contamination, radiation, captured-payload disposal, custody closure or package reward is invented.

A bounded native completion proposal is to supply exact currently occupied province identities through a verified installation registry, target removal at those provinces, and capture before/after levels at the same physical surfaces.
Use the existing profile fraction for each original physical token and reconcile the observed per-province sum into the single existing state category receipt.
For the main center, the offline wiki documents all-provinces selection for `set_building_level`, while vanilla SOV source demonstrates that selection syntax on construction.
A zero-level clear using that syntax is a proposal, with no executed vanilla precedent claimed for queue, rail or receipt behavior.
This proposal remains unresolved until the native consumer and per-province observation route are verified.
Do not substitute a static territory list or a damage/flood effect for exact physical removal.

Searches of the current installed effect registry, installed documentation, vanilla scripted effects/projects, offline wiki and relevant repo source found no `cancel_building_construction` or `cancel_special_project` definition or supported script invocation.
Neither token has a documented native effect scope/context in this installed build.
The native special-project project-definition docs describe phases, cancellation progress and country/project scopes, but provide no script cancellation effect.
`facility_province_id` can identify a project's facility province, which is a useful bounded association, not a cancellation operation.
The requested commands must not be emitted on assumed contexts.

Parent-owned bounded project proposal: at the current validated crater-state transaction, invalidate exact package-local projects by their existing state/actor/receipt identity, release package reservations through their owner API, and suppress future project completion if the source site is the permanent crater.
Native construction and special-project queue cancellation remain blocked until a documented supported API or direct engine evidence exists.
A zero aggregate building count cannot prove no queued project remains.

Existing `bio_facility_capture_resolve_destroyed_facility` was inspected.
It clears captured-facility package records, and its owning wrappers require exact actor/site payload context and combine demolition with payload/evidence/reward outcomes, so it cannot be called as a generic asteroid demolition hook.
Camp closure similarly has exact custody, owner and receipt obligations.
No existing package hook is integrated without an accepted non-rewarding catastrophe contract.
Bio/chemical/camp packages are preserved.

## MCP exposure and evidence limits

This client exposes event inspect/render/compare, map inspect, reference context/search/read and source lookup, with no script_validate.
Connected source_lookup has the older bounded schema without view/keyPath.
No verified health/version or negotiated native-task contract was obtained, so helper_expansion/jobs/tasks are not used.

A first narrow event request used an invalid selector and returned `MCP error -32602`, requiring selector.kind.
The corrected retry uses `mode=trace`, selector `{kind:event,eventId:chaosx.nr28.4}`, depth/nodes/edges one, helpers false.
Reference context uses event surface, bounded physical-receipt question and limit four.
Map retry uses lookupOnly, stateIds [1], overview false.
Final returned statuses are recorded below.
The corrected event retry, reference-context retry and map retry each returned `isError=true` with `timed out awaiting tools/call after 600s`.
No source revision, graph, render, comparison, continuation URI or artifact was returned.
Event render/compare are blocked downstream of the failed current inspection, and no current read-only reference citation was returned for a revision-bound reference_read.
Reference_search, reference_read and source_lookup exposure/schema were verified, but no new successful retrieval from them is claimed.
The parent's prior timeouts remain attributed evidence in the completion audit, separate from these client retries.
No unknown sourceMcpValidate finding is promoted to passed.
No engine, GUI, probability or rendered acceptance is claimed from these local tests.
No AI weight or candidate surface is changed, so a new probability baseline is outside this bounded patch.
Parent's existing probability specialist retains the full Event028 audit.

## Meaningful source validation and limits

The runnable appendix executes actual parsed before/after source, including the selected-building helpers, meta readbacks, population helper, profile wrapper and footprint registration.
Unknown executed effect/trigger tokens raise a test error.
Native callbacks are declared in the model: aggregate building removal clamps to existing levels, fractional callback variants model partial/no application, negative state add_manpower removes current population and grants modeled owner/controller credit, country add_manpower reconciles that credit, Deaths callback records without another population mutation, and mineral-control refresh is an explicit no-op outside this scope.
The callback models are assumptions for source reasoning, not native acceptance.
The test models the installed 1000-iteration ceiling in explicit while/for loops.
It proves that unowned helper ASTs are unchanged relative to the immutable source and that all original building token identities remain.

The user performs live consumer validation.
No game launch, save inspection, player test request, nuclear ledger or probability evaluation is performed here.
No simplification is accepted or introduced as a substitute for the remaining native requirements.
Event028 remains incomplete where province removal, queued native projects, runtime full-footprint processing, Dust integration and current MCP evidence remain unresolved.

## Final validation receipt

The appendix passed all 58 source-model scenarios after the final source edit.
It checks seven fixed population profiles at zero, one, nineteen, one hundred thousand and one hundred million people, actual Deaths without a second debit, owner/controller credit reconciliation under the declared callback, pre-impact population snapshots, and receipt preservation on repeated calls.
It reproduces the baseline missing-fraction storage defect and the four-level naval-base duplicate regression, with modeled removal changing from three levels to two.
It checks partial, zero and full native removal callbacks and one requested native removal of 1501 levels.
It appends and upgrades actual-source footprint rows at sizes 999, 1000, 1001 and 1501, including index 1500 beyond the old ceiling.
It rejects absent cache, stale transaction, negative/fractional/out-of-bounds index, changed row identity, misaligned columns and zero transaction without partial row or registration writes.
All 63 original building tokens are retained once, all sixteen duplicate dispatches are removed, and a current installed/mod definition inventory found no unresolved building token.
Only five gameplay helper ASTs differ from the immutable before source, exactly the five listed in the test's ownership assertion.
All other helper ASTs, including owner aggregation, Dust, mineral control, lifecycle and cleanup, match that before source.

Final raw source SHA-256: `d3c5a26e55edfa2439a833ada0d6cc9f13c5794fcba8857baf3e6d0f73b97438`.
Declared fixture SHA-256: `fae51ae721aedd93da441fc88cb5a860cc0548ff036850ff4ea42dc842686f1d`.
Test callbacks remain declared source-model assumptions, and source-only validation does not establish native province destruction, project cancellation, serialization, full parent runtime processing or rendered acceptance.
The shared-tree source may change after handoff, so rerun the appendix and retain its reported raw after hash when integrating.

Skills used: chaos-redux-events, chaos-redux-subagents and chaos-redux-state-ledgers.
No skill was created or updated.

## Local source citations and revisions

`mod` resolves to `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
`game` resolves to `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
These are direct local reads after the unavailable MCP reference route, and the path suffixes below resolve under those exact Windows roots.
Line spans are one-based and source hashes identify the inspected bytes.

| Source path | Lines / rule read | SHA-256 |
| --- | --- | --- |
| `mod\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263 to 328 event targets, 433 to 446 temporary lifetime/scoping, 955 to 965 token variables, 1071 to 1085 array identity, 1216 to 1220 loops | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `mod\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 3611 to 3680 building effects and province selectors | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| `mod\paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 570 to 586 variable predicates and 1837 state flag | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| `mod\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 259 to 267 project, ROOT, THIS, PREV, owner and controller | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| `mod\paradox_wiki\Building modding - Hearts of Iron 4 Wiki.md` | 53 to 72 provincial/state slots, 121 to 132 facility/damage consumers | `1E5FB5410A26AF12B5B791B193F8F602C4EF8A3614ED897AE4C67084477F7BFC` |
| `mod\paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 644 to 652 token-localisation functions | `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064` |
| `game\documentation\script_concept_documentation.md` | 216 to 236 shared constants and load-time injection | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| `game\common\script_constants\documentation.md` | Complete schema and examples | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| `game\documentation\effects_documentation.md` | 1468 to 1476 add_manpower, 2733 to 2753 global target cleanup, 4155 to 4171 every_state, 4297 to 4334 array/for loops, 4833 to 4853 meta text, 5838 to 5875 removal/province warning, 6496 to 6516 target saves, 6621 to 6628 set_building_level, 8573 to 8586 while loop, cancellation-token absence search | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| `game\documentation\triggers_documentation.md` | 2110 to 2138 comparisons, 7561 to 7569 state identity | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| `game\documentation\dynamic_variables_documentation.md` | 1085 to 1103 facility province/state and building reader | `538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA` |
| `game\common\defines\00_defines.lua` | 25 MAX_EFFECT_ITERATION | `405A24CE579815443CAFE052CFF1361E20C712CA8182E3F10CCBF45330DD4BE4` |
| `game\common\special_projects\projects\documentation.md` | 1 to 46 phases, cancellation behavior and project/country scopes | `16879504BC72AA357F1D3C0F1093E94A3946F8C35E7942F65AC9A5D3BCD6C643` |
| `game\common\buildings\00_buildings.txt` | 98 to 225 rail/supply/naval/forts, 500 to 746 facilities/dams/canals/energy | `9FA27D266F726DE04C71311551698C6466257636DCC34D2573A3568D397BD539` |
| `game\common\scripted_effects\00_scripted_effects.txt` | 1 to 106 exact factory-removal precedent | `93DDD0D2E9F7A1A5640CFDAFBAE6B9FF0E1B4EE57E829C81D13B0CAC23AD90BF` |
| `game\common\scripted_effects\SOV_scripted_effects.txt` | 8274 to 8299 all-provinces construction selector precedent | `CC9E16837AFA1428D11E053DC982446B35587980DAA011A1DF12114C3ACE2BF4` |
| `game\common\scripted_effects\RAJ_GOE_scripted_effects.txt` | 677 to 701 bounded owned-state factory removal precedent | `70173CFD8DD97A9F52852FF9DB310487C14B14A503E6A79C3828431B34CFEAAA` |
| `game\common\special_projects\special_projects_documentation.md` | 1 to 110 older project definition/reference, cancellation-token search | `E5D1766E95FE9C71D676046720BB699918E2565C8A43FE5A9183359C98BFCBFE` |
| `game\documentation\console_commands_documentation.md` | Requested cancellation-token absence search | `B65548C92B318F84F2185BE790A3E0F2BCE331EA646E233BF2EA85114BF8215D` |
| `game\common\scripted_localisation\00_scripted_localisation.txt` | 1 to 96 native dynamic-text contract/precedents | `6F490E33736F4DC31568ADD5753A1AFDEF916F3993804FEBFBBE6D1583827587` |
| `mod\common\buildings\chaosx_buildings.txt` | Complete biological/chemical/camp definition file | `AF9FD98C11F71A791C75D3FFBE1AAD5F64A0F15DDB4CF67474FFA42A780FB468` |
| `mod\common\buildings\chaosx_3d_model_pilots.txt` | Complete anomaly building definition | `448F3E1CF9EDCA39A748A4306C55C84A513E0458E0F651409341A992B3783ED1` |
| `mod\common\scripted_effects\chaosx_dynamic_effects.txt` | 46 to 62 existing dynamic building damage, 540 to 628 exact population owner | `8B4DB4F595A607D041D0F072DE65DD906CDB10C40246690F78D3E4305DAB4D49` |
| `mod\common\scripted_effects\chaosx_dynamic_effects.md` | Population transaction and exact-loss API sections | `1ED956C15ADE9879B79249F6D0D974C1D324F7043E9CCD2C2CC9B4235A451EA1` |
| `mod\common\scripted_effects\biological_facility_capture_effects.txt` | 75 to 112 captured ledger cleanup, 642 to 673 native capture demolition, wrapper source search | `AF68FB98172452B324DB17B2A273110E1D9C08E6A3D7F30AECABCCE4E9D1F00C` |
| `mod\common\scripted_effects\camp_administration_effects.txt` | 923 to 1001 exact site closure and project cancellation | `0E32BC2E248B96C5F5D58D772FE97CE5134837A439638D567FE46CCEAE85BAD5` |
| `mod\common\script_constants\028_asteroid_incoming_constants.txt` | 274 to 383 profiles, fixed population, building fractions and Dust tuning | `E81036C0CFFA3D9830B220AA4BA7E311F14165D40599B990D316F77E470FE157` |
| `mod\common\scripted_triggers\028_asteroid_incoming_triggers.txt` | 813 to 844 aligned arrays and resolvable physical transaction | `D591180EDE589C319D6077028736EDAFC184DECB86F62E2D48BFEC3F8AF81A4B` |

The full Part 3, Part 4, tuning matrix and completion audit were read.
Their inspected SHA-256 identities are respectively `F81C3B5C3FDBAF72879DE8AF5C34A1DF1D93926D2EA5DF5D9640C4F6878973E0`, `503C1B916D28D05776947C64DDB044FE1EFB10CFA2FFA072FE8237721691AB92`, `9BDD2CB2B7748F505EB620AAB922FFED3FE78B728BAB76E526A241F636DCF8A7` and `692A8254508C782B696D0BCDB3A6E3661AD1C7ABF4CA305DBE7D45FB89B216D7`.

## Runnable actual-source appendix

Parent iterator addendum: this appendix also reads and executes the actual current runtime `asteroid_incoming_process_footprint` and `asteroid_incoming_apply_state_profile` ASTs.
Installed `effects_documentation.md:4155` to `4171` was read directly again, with unchanged SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
The declared scope-iterator model visits each supplied world-state object once, evaluates the source limit in that state scope and executes its children in that same scope, independently of duplicate array entries.
This scope-iterator model has no numeric-loop ceiling, which is a declared modeling assumption rather than executed native proof.
The actual numeric while/for model retains its 1000-iteration bound.
Capital relocation, target preparedness, medical duration adjustment, rescue setup and secondary-disaster dispatch are explicit no-op callback boundaries in this iterator test.
Country aggregation is a declared callback that appends the fixture's distinct owner/controller recipients once, so the actual post-iterator persistent country-count assignment is tested against a declared recipient registry rather than full country-accounting execution.
Dynamic modifiers and nuclear visuals are recorded no-op native callback boundaries, and establish no native effect or nuclear-isolation acceptance.
The outer failed-closed/alignment gate in the event resolver remains a parent-owned open dependency, and no queue or province-native acceptance is asserted.
The parent's capital caller-order assertion migration and unchanged 23 capital scenarios remain parent-owned and are not edited or independently revalidated here.
This addendum's executed result is 66 source scenarios passed, comprising the earlier 58 physical/helper cases and eight runtime iterator/reentry cases.
It supersedes the earlier 58-case receipt for current iterator coverage while preserving that historical physical-only fixture identity.
The runtime bytes read for this pass have SHA-256 `377003cd7fa7337bd60b95bea4f22886d133595c842369b314aad015bc1dcc8b`.
The combined actual processor/profile AST SHA-256 is `a657c0b46d820680e2c2ad1dd9639e1aee7322f48bded376d20bbfe646d4380a`, and the extended declared fixture SHA-256 is `b4114409bee0ed9a055a7b41d351941ce745d5c8319280ced667db3ce0a788bc`.
The physical-effects source remains byte-identical to the previous handoff at SHA-256 `d3c5a26e55edfa2439a833ada0d6cc9f13c5794fcba8857baf3e6d0f73b97438`.

| Eligible states | Declared world states | Duplicate registry rows | Foreign/stale/unplanned states excluded | Repeat physical calls |
| ---: | ---: | ---: | ---: | ---: |
| 999 | 1002 | 3 | 3 | 0 |
| 1000 | 1003 | 3 | 3 | 0 |
| 1001 | 1004 | 3 | 3 | 0 |
| 1501 | 1504 | 3 | 3 | 0 |

Each fixture also includes one registry-only state ID absent from the declared world, which is never manufactured or visited by the iterator.
The last eligible state's profile is upgraded from 40 to 60 through actual registration before processing, and duplicate rows retain weaker profile values to verify consumption of the stored strongest state mirror.
Every eligible state receives exactly one measured population transaction and Deaths callback in the first pass, and repeated processor entry leaves physical population, buildings, Deaths and state receipts unchanged.
The actual source assigns the persistent affected-country count after the iterator, and the declared two-recipient callback produces a count of two that remains after the working recipient array is cleared in the fixture.
The full cleanup helper and full country-accounting implementation are not executed by this added model.
Processor reentry resets its global batch summary fields to zero even though no state is physically applied again, so these results establish no double physical application and do not establish full processor idempotence.
The parent must retain the event-resolution/idempotence guards and complete the outer failed-closed/alignment gate before physical processing.
No runtime, physical gameplay, shared settings, mineral source, decision source, capital handoff or other document was edited for this addendum.

Run from the repository root with:
`python -B -c "from pathlib import Path; import re; s=Path('docs/plans/028_asteroid_incoming_plans/subagent_handoffs/physical_receipts_20261003.md').read_text(encoding='utf-8'); exec(re.search(r'~~~python\n(.*?)\n~~~', s, re.S).group(1))"`

~~~python
import copy, hashlib, json, math, re, subprocess, sys
from collections import Counter
from pathlib import Path
ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / ".tools/validation"))
from validate_028_availability import parse_source
P = "common/scripted_effects/028_asteroid_incoming_effects.txt"
COMMIT = "9d7862dcb78ae097f61eb95e07e3ff2e911f75db"
before_bytes = subprocess.check_output(["git", "show", COMMIT + ":" + P])
assert hashlib.sha256(before_bytes).hexdigest() == "44a5519e86a8e6fcaaf0c681f84ecc77d365383a7cd4092d3d9cb450fad08a44"
class Text:
    def __init__(self, text): self.text = text
    def read_text(self, encoding): return self.text
before = parse_source(Text(before_bytes.decode("utf-8-sig")))
after = parse_source(ROOT / P)
constants = parse_source(ROOT / "common/script_constants/028_asteroid_incoming_constants.txt")
def definition(path, name):
    text = re.sub(r"#[^\n]*", "", path.read_text(encoding="utf-8-sig"))
    match = re.search(r"(?m)^" + re.escape(name) + r"\s*=\s*\{", text)
    assert match, name
    depth = 1
    for i in range(match.end(), len(text)):
        depth += (text[i] == "{") - (text[i] == "}")
        if depth == 0: return Text(text[match.start():i+1])
    raise AssertionError("Unclosed selected definition " + name)
for category in ("chaos_meter_deaths", "chaos_meter_deaths_reason"):
    constants.update(parse_source(definition(ROOT / "common/script_constants/chaos_meter_constants.txt", category)))
triggers = parse_source(ROOT / "common/scripted_triggers/028_asteroid_incoming_triggers.txt")
shared = parse_source(definition(ROOT / "common/scripted_effects/chaosx_dynamic_effects.txt", "apply_state_population_loss_without_recruitable_manpower_gain"))
RUNTIME_PATH = "common/scripted_effects/028_asteroid_incoming_runtime_effects.txt"
runtime_bytes = (ROOT / RUNTIME_PATH).read_bytes()
runtime = parse_source(Text(runtime_bytes.decode("utf-8-sig")))
runtime_names = ("asteroid_incoming_process_footprint", "asteroid_incoming_apply_state_profile")
runtime_ast_hash = hashlib.sha256(json.dumps({k:runtime[k] for k in runtime_names}, sort_keys=True).encode()).hexdigest()
CHANGED = {
    "asteroid_incoming_record_footprint_profile",
    "asteroid_incoming_remove_selected_building_levels",
    "asteroid_incoming_apply_selected_strategic_building_receipt",
    "asteroid_incoming_apply_building_receipt",
    "asteroid_incoming_apply_state_transaction",
}
assert set(before) == set(after)
assert {k for k in before if before[k] != after[k]} == CHANGED
def walk(rows):
    for row in rows:
        yield row
        if isinstance(row[2], list): yield from walk(row[2])
def inventory(defs):
    return Counter(v[0][2][6:] for k, _, v in defs["asteroid_incoming_apply_building_receipt"]
                   if k == "set_temp_variable" and v[0][0] == "asteroid_incoming_selected_building")
bc, ac = inventory(before), inventory(after)
dups = sorted(k for k, v in bc.items() if v == 2)
assert len(dups) == 16 and set(bc) == set(ac) and set(ac.values()) == {1}
# Each direct call must own the consumed child output immediately before calling.
for name in ("asteroid_incoming_apply_building_receipt", "asteroid_incoming_apply_selected_strategic_building_receipt"):
    rows = after[name]
    for i, (k, _, v) in enumerate(rows):
        out = {"asteroid_incoming_prepare_selected_building_loss": "asteroid_incoming_remove_levels",
               "asteroid_incoming_capture_selected_building_receipt": "asteroid_incoming_selected_actual"}.get(k)
        if out:
            assert rows[i-1][0] == "set_temp_variable" and rows[i-1][2][0][0] == out
class Model:
    def __init__(self, defs):
        self.defs = dict(shared, **defs)
        self.temp, self.reg, self.arrays, self.targets = {}, {}, {}, {}
        self.state_flags, self.global_flags = {}, set()
        self.population, self.buildings, self.removals, self.deaths = {}, {}, [], []
        self.owner, self.controller = "owner", "controller"
        self.reg[self.owner] = {"manpower": 12000.0}
        self.reg[self.controller] = {"manpower": 23000.0}
        self.reg["global"] = {"asteroid_incoming_transaction_id": 7, "asteroid_incoming_planner_mode": 1}
        self.native_removal_ratio = 1.0
        self.missing_temp_reads = []
        self.world_states, self.calls, self.native_boundaries = [], [], []
        self.callbacks, self.country_flags = {}, {}
    def array_ref(self, token, scope):
        name, index = token.split("^")
        return name, len(self.arrays.get(name, [])) if index == "num" else int(self.val(index, scope))
    def val(self, token, scope):
        if token.startswith("constant:"):
            x = constants
            for key in token[9:].split("."):
                x = dict((k, v) for k, _, v in x)[key] if isinstance(x, list) else x[key]
            return float(x)
        if token.startswith("token:"): return token[6:]
        if token.startswith("var:"): return self.val(token[4:], scope)
        if token.startswith("event_target:"): return self.targets[token[13:]]
        if token == "THIS": return scope
        if token == "THIS.id": return scope
        if token == "OWNER": return self.owner
        if token == "CONTROLLER": return self.controller
        if token == "state_population_k": return self.population[scope] / 1000
        if token == "manpower_k": return self.reg[scope]["manpower"] / 1000
        if token.startswith("building_level@"): return self.buildings[scope].get(token.split("@")[1], 0)
        if "^" in token:
            name, i = self.array_ref(token, scope)
            if token.endswith("^num"): return i
            assert 0 <= i < len(self.arrays[name]), ("invalid array read", token, i)
            return self.arrays[name][i]
        try: return float(token)
        except ValueError: pass
        if token in self.temp: return self.temp[token]
        if token.startswith("global."): return self.reg["global"].get(token[7:], 0)
        return self.reg.setdefault(scope, {}).get(token, 0)
    def write(self, name, value, scope, temporary=False):
        if temporary: self.temp[name] = value
        elif "^" in name:
            a, i = self.array_ref(name, scope)
            assert 0 <= i < len(self.arrays[a]), ("invalid array write", name, i)
            self.arrays[a][i] = value
        elif name.startswith("global."): self.reg["global"][name[7:]] = value
        else: self.reg.setdefault(scope, {})[name] = value
    def compare(self, a, op, b):
        return {"=": lambda: a == b, "equals": lambda: a == b, "not_equals": lambda: a != b,
                ">": lambda: a > b, "greater_than": lambda: a > b,
                "<": lambda: a < b, "less_than": lambda: a < b,
                "greater_than_or_equals": lambda: a >= b,
                "less_than_or_equals": lambda: a <= b}[op]()
    def condition(self, rows, scope):
        def node(k, op, v):
            if k in ("AND", "hidden_trigger"): return self.condition(v, scope)
            if k == "OR": return any(node(*r) for r in v)
            if k == "NOT": return not any(node(*r) for r in v)
            if k in triggers: return self.condition(triggers[k], scope) == (v == "yes")
            if k == "check_variable":
                d = dict((a, b) for a, _, b in v)
                if "var" in d: a, comparison, b = d["var"], d.get("compare", "equals"), d["value"]
                else: a, comparison, b = v[0]
                return self.compare(self.val(a, scope), comparison, self.val(b, scope))
            if k == "has_variable":
                return v in self.temp or (v[7:] in self.reg["global"] if v.startswith("global.") else v in self.reg.get(scope, {}))
            if k == "is_in_array":
                d = dict((a, b) for a, _, b in v)
                return self.val(d["value"], scope) in self.arrays.get(d["array"], [])
            if k == "state": return scope == self.val(v, scope)
            if k == "has_state_flag": return v in self.state_flags.get(scope, set())
            if k == "has_global_flag": return v in self.global_flags
            if k == "has_country_flag": return v in self.country_flags.get(scope, set())
            if k == "scope_exists": return True
            if k == "impassable": return v == "no"
            if k in ("OWNER", "CONTROLLER"): return self.condition(v, self.val(k, scope))
            if k == "exists": return scope in self.reg and v == "yes"
            if k == "is_owned_and_controlled_by": return self.owner == self.controller
            raise AssertionError(("unsupported trigger", k, op, v))
        return all(node(*r) for r in rows)
    def frame(self, rows, scope):
        keys = set(self.temp)
        try: self.run(rows, scope)
        finally:
            for k in set(self.temp) - keys: del self.temp[k]
    def call(self, name, scope):
        self.calls.append((name, scope))
        if name in self.callbacks:
            self.callbacks[name](scope)
            return
        self.frame(self.defs[name], scope)
    def run(self, rows, scope):
        matched = False
        for k, op, v in rows:
            if k in ("if", "else_if", "else"):
                d = dict((a,b) for a,_,b in v)
                take = (k == "if" or not matched) and (k == "else" or self.condition(d.get("limit", []), scope))
                if k == "if": matched = False
                if take:
                    self.run([r for r in v if r[0] != "limit"], scope)
                    matched = True
                continue
            if k in ("set_temp_variable", "set_variable", "add_to_temp_variable", "add_to_variable",
                     "subtract_from_temp_variable", "subtract_from_variable", "multiply_temp_variable", "multiply_variable"):
                name, _, value = v[0]
                x = self.val(value, scope)
                if not k.startswith("set_"):
                    old = self.val(name, scope)
                    x = old + x if k.startswith("add_") else old - x if k.startswith("subtract_") else old * x
                self.write(name, x, scope, "temp" in k)
            elif k in ("round_temp_variable", "round_variable"):
                self.write(v, math.floor(self.val(v, scope) + .5), scope, "temp" in k)
            elif k in ("clamp_temp_variable", "clamp_variable"):
                d = dict((a,b) for a,_,b in v)
                x = self.val(d["var"], scope)
                if "min" in d: x = max(x, self.val(d["min"], scope))
                if "max" in d: x = min(x, self.val(d["max"], scope))
                self.write(d["var"], x, scope, "temp" in k)
            elif k == "meta_effect":
                d = dict((a,b) for a,_,b in v)
                token = self.temp["asteroid_incoming_selected_building"]
                def sub(block):
                    return [(a.replace("[BUILDING_TYPE]", token), o,
                             sub(b) if isinstance(b,list) else b.replace("[BUILDING_TYPE]", token)) for a,o,b in block]
                self.frame(sub(d["text"]), scope)
            elif k in ("for_loop_effect", "while_loop_effect"):
                d = dict((a,b) for a,_,b in v)
                n = self.val(d.get("start", "0"), scope)
                for iteration in range(1000):
                    if k == "while_loop_effect":
                        if not self.condition(d["limit"], scope): break
                    else:
                        if n >= self.val(d["end"], scope): break
                        self.temp[d.get("value","v")] = n
                    self.run([r for r in v if r[0] not in ("start","end","value","limit")], scope)
                    n += 1
            elif k == "remove_building":
                d = dict((a,b) for a,_,b in v)
                assert self.val(d["state"], scope) == scope
                count = int(self.val(d["level"], scope) * self.native_removal_ratio)
                actual = min(self.buildings[scope].get(d["type"], 0), count)
                self.buildings[scope][d["type"]] = self.buildings[scope].get(d["type"], 0) - actual
                self.removals.append((scope, d["type"], actual))
            elif k == "add_manpower":
                amount = self.val(v, scope)
                if isinstance(scope, int):
                    actual = min(self.population[scope], -amount)
                    self.population[scope] -= actual
                    for country in {self.owner, self.controller}: self.reg[country]["manpower"] += actual
                else: self.reg[scope]["manpower"] += amount
            elif k == "chaos_meter_register_deaths":
                assert self.temp["chaos_deaths_apply_state_pop"] == 0
                assert self.temp["chaos_deaths_record_state_ledger"] == 1
                self.deaths.append((scope, self.temp["chaos_deaths_change"], self.temp["chaos_deaths_reason"], self.temp["chaos_deaths_target_country"]))
            elif k == "asteroid_incoming_refresh_site_mineral_control": pass
            elif k in self.defs: self.call(k, scope)
            elif k.startswith("var:"): self.run(v, self.val(k, scope))
            elif k in ("OWNER", "CONTROLLER"): self.run(v, self.val(k, scope))
            elif k in ("every_state", "every_country"):
                d = dict((a,b) for a,_,b in v)
                assert "random_select_amount" not in d
                # Declared native scope-iterator semantics, not a numeric while/for loop.
                objects = tuple(self.world_states) if k == "every_state" else tuple(x for x in self.reg if isinstance(x,str) and x != "global")
                assert len(objects) == len(set(objects))
                for obj in objects:
                    if self.condition(d.get("limit", []), obj):
                        self.run([r for r in v if r[0] != "limit"], obj)
            elif k == "add_to_array":
                d = dict((a,b) for a,_,b in v)
                self.arrays.setdefault(d["array"], []).append(self.val(d["value"], scope))
            elif k in ("save_event_target_as", "save_global_event_target_as"): self.targets[v] = scope
            elif k == "set_state_flag": self.state_flags.setdefault(scope,set()).add(v)
            elif k == "set_global_flag": self.global_flags.add(v)
            elif k == "clr_global_flag": self.global_flags.discard(v)
            elif k == "clr_country_flag": self.country_flags.setdefault(scope,set()).discard(v)
            elif k == "clear_variable": self.reg.setdefault(scope,{}).pop(v, None)
            elif k in ("set_state_category", "add_dynamic_modifier", "remove_dynamic_modifier", "launch_nuke"):
                self.native_boundaries.append((k,scope,copy.deepcopy(v)))
            else: raise AssertionError(("unsupported effect", k, op, v))
def state_fixture(defs, profile="main_ring_two", people=100000):
    m = Model(defs)
    m.population[1] = people
    m.buildings[1] = {k: 4 for k in ac}
    m.reg[1] = {"asteroid_incoming_state_profile": m.val("constant:asteroid_incoming_profile."+profile,1)}
    return m
checks = []
def ok(name): checks.append(name)
# Callee-created values expire. Caller-preinitialized values retain child modifications.
for defs in (before,after):
    m = state_fixture(defs)
    m.call("asteroid_incoming_load_profile_fractions",1)
    assert "asteroid_incoming_population_fraction" not in m.temp
    m.temp["asteroid_incoming_population_fraction"] = 0
    m.call("asteroid_incoming_load_profile_fractions",1)
    assert m.temp["asteroid_incoming_population_fraction"] == .25
ok("getter conservative lifetime control")
for profile, fraction in (("main_center",1),("main_ring_one",.5),("main_ring_two",.25),("main_ring_three",.05),
                          ("fragment_center",.5),("fragment_ring_one",.25),("fragment_ring_two",.05)):
    for people in (0,1,19,100000,100000000):
        m = state_fixture(after,profile,people)
        m.call("asteroid_incoming_apply_state_transaction",1)
        actual = math.floor(people*fraction+.5)
        assert m.population[1] == people-actual and m.reg[1]["asteroid_incoming_state_actual_deaths"] == actual
        assert m.reg[1]["asteroid_incoming_preimpact_population_k"] == people/1000
        assert len(m.deaths) == (actual > 0)
        if actual: assert m.deaths[0][1] == actual
        assert m.reg[m.owner]["manpower"] == 12000 and m.reg[m.controller]["manpower"] == 23000
        receipts = {k:v for k,v in m.reg[1].items() if k.endswith("_lost") or k.endswith("_deaths")}
        removals, deaths = len(m.removals), len(m.deaths)
        m.call("asteroid_incoming_apply_state_transaction",1)
        assert m.population[1] == people-actual and len(m.removals) == removals and len(m.deaths) == deaths
        assert receipts == {k:v for k,v in m.reg[1].items() if k.endswith("_lost") or k.endswith("_deaths")}
        assert sum(m.reg[1]["asteroid_incoming_state_"+cat+"_levels_lost"] for cat in ("industry","logistics","strategic")) == m.reg[1]["asteroid_incoming_state_building_levels_lost"]
        assert len({t for _,t,_ in m.removals}) == len(m.removals)
        ok("physical "+profile+" "+str(people))
m = state_fixture(before); m.call("asteroid_incoming_apply_state_transaction",1)
assert m.population[1] == 100000 and not m.deaths
ok("before missing fraction storage reproduces zero modeled loss")
# Preinitialize outputs to isolate duplicate dispatch from the baseline lifetime defect.
results = []
for defs in (before,after):
    m = state_fixture(defs)
    m.temp.update(asteroid_incoming_industry_fraction=.45,asteroid_incoming_logistics_fraction=.55,
                  asteroid_incoming_strategic_fraction=.5,asteroid_incoming_remove_levels=0,
                  asteroid_incoming_selected_actual=0,asteroid_incoming_selected_before=0,
                  asteroid_incoming_selected_after=0)
    m.call("asteroid_incoming_apply_building_receipt",1)
    results.append(4-m.buildings[1]["naval_base"])
assert results == [3,2]
ok("actual AST naval base before 3 after 2")
# Direct requested count above 1000 has no per-level loop in the patched adapter.
m = state_fixture(after); m.buildings[1]["industrial_complex"] = 1501
m.temp.update(asteroid_incoming_selected_building="industrial_complex",asteroid_incoming_remove_levels=1501)
m.call("asteroid_incoming_remove_selected_building_levels",1)
assert m.buildings[1]["industrial_complex"] == 0 and len(m.removals) == 1
ok("one native removal request for 1501 levels")
# Receipt consumes observed difference, including partial or rejected modeled native removal.
for ratio in (0,.5,1):
    m = state_fixture(after); m.native_removal_ratio = ratio
    m.temp.update(asteroid_incoming_industry_fraction=.45,asteroid_incoming_logistics_fraction=.55,asteroid_incoming_strategic_fraction=.5)
    m.call("asteroid_incoming_apply_building_receipt",1)
    assert m.reg[1]["asteroid_incoming_state_building_levels_lost"] == sum(v for _,_,v in m.removals)
    ok("observed removal ratio "+str(ratio))
for size in (999,1000,1001,1501):
    for defs,label in ((before,"before"),(after,"after")):
        m = Model(defs)
        for s in range(1,size+1):
            m.reg[s] = {}
            m.temp.update(asteroid_incoming_profile_candidate=10,asteroid_incoming_ring_candidate=2,asteroid_incoming_profile_recorded=0)
            m.call("asteroid_incoming_record_footprint_profile",s)
        assert len(m.arrays["global.asteroid_incoming_footprint_states"]) == size
        m.temp.update(asteroid_incoming_profile_candidate=60,asteroid_incoming_ring_candidate=1)
        m.call("asteroid_incoming_record_footprint_profile",size)
        expected = 10 if label == "before" and size > 1000 else 60
        assert m.arrays["global.asteroid_incoming_footprint_profiles"][-1] == expected
        if label == "after":
            m.temp.update(asteroid_incoming_profile_candidate=60,asteroid_incoming_ring_candidate=0)
            m.call("asteroid_incoming_record_footprint_profile",size)
            m.temp.update(asteroid_incoming_profile_candidate=20,asteroid_incoming_ring_candidate=0)
            m.call("asteroid_incoming_record_footprint_profile",size)
            assert m.arrays["global.asteroid_incoming_footprint_profiles"][-1] == 60
            assert m.arrays["global.asteroid_incoming_footprint_rings"][-1] == 0
            assert len(m.arrays["global.asteroid_incoming_footprint_states"]) == size
        ok(label+" footprint "+str(size))
# Reordered arrays, absent cache, stale transaction, negative/out-of-range cache and misalignment reject without writes.
for corrupt in ("identity","missing","stale","negative","fractional","bounds","misaligned","zero_transaction"):
    m = Model(after)
    for s in (1,2):
        m.reg[s] = {}
        m.temp.update(asteroid_incoming_profile_candidate=10,asteroid_incoming_ring_candidate=2,asteroid_incoming_profile_recorded=0)
        m.call("asteroid_incoming_record_footprint_profile",s)
    if corrupt == "identity": m.arrays["global.asteroid_incoming_footprint_states"].reverse()
    elif corrupt == "missing": del m.reg[2]["asteroid_incoming_state_footprint_index"]
    elif corrupt == "stale": m.reg[2]["asteroid_incoming_state_footprint_transaction_id"] = 6
    elif corrupt == "negative": m.reg[2]["asteroid_incoming_state_footprint_index"] = -1
    elif corrupt == "fractional": m.reg[2]["asteroid_incoming_state_footprint_index"] = 1.5
    elif corrupt == "bounds": m.reg[2]["asteroid_incoming_state_footprint_index"] = 2
    elif corrupt == "misaligned": m.arrays["global.asteroid_incoming_footprint_profiles"].pop()
    else: m.reg["global"]["asteroid_incoming_transaction_id"] = 0
    snapshot = copy.deepcopy((m.arrays,m.reg,m.state_flags))
    m.temp.update(asteroid_incoming_profile_candidate=60,asteroid_incoming_ring_candidate=1)
    m.call("asteroid_incoming_record_footprint_profile",2)
    assert m.temp["asteroid_incoming_profile_recorded"] == 0
    assert (m.arrays,m.reg,m.state_flags) == snapshot
    assert "asteroid_incoming_transaction_failed_closed" in m.global_flags
    ok("reject "+corrupt)
# Execute the actual runtime processor and profile wrapper, with named external callbacks.
processor = runtime["asteroid_incoming_process_footprint"]
iterators = [v for k,_,v in processor if k == "every_state"]
assert len(iterators) == 1
assert not any(k in ("while_loop_effect", "for_loop_effect") for k,_,v in walk(processor))
assert [k for k,_,v in iterators[0] if k != "limit"] == ["asteroid_incoming_apply_state_profile"]
assert not any(k == "set_variable" and any(a == "asteroid_incoming_state_profile" for a,_,b in v)
               for k,_,v in walk(processor))
receipt_positions = [i for i,(k,_,v) in enumerate(processor)
                     if k == "set_variable" and v[0] == ("global.asteroid_incoming_affected_country_count", "=", "global.asteroid_incoming_affected_country_entries^num")]
assert len(receipt_positions) == 1 and receipt_positions[0] > next(i for i,r in enumerate(processor) if r[0] == "every_state")
iterator_reports = []
for size in (999,1000,1001,1501):
    m = Model(after)
    m.defs.update(runtime)
    for name in ("asteroid_incoming_relocate_destroyed_capital", "asteroid_incoming_apply_target_preparedness_aftermath",
                 "asteroid_incoming_adjust_local_burden_for_medical_preparation", "asteroid_incoming_initialize_state_rescue_burden",
                 "asteroid_incoming_maybe_call_secondary_disaster"):
        m.callbacks[name] = lambda scope: None
    def aggregate_fixture(scope):
        # Explicit country-accounting boundary, not an implementation substitute or native proof.
        entries = m.arrays.setdefault("global.asteroid_incoming_affected_country_entries", [])
        for country in (m.owner,m.controller):
            if country not in entries: entries.append(country)
    m.callbacks["asteroid_incoming_aggregate_current_state"] = aggregate_fixture
    for s in range(1,size+1):
        m.reg[s], m.population[s], m.buildings[s] = {}, 100000, {"industrial_complex":4}
        m.temp.update(asteroid_incoming_profile_candidate=40,asteroid_incoming_ring_candidate=2,asteroid_incoming_profile_recorded=0)
        m.call("asteroid_incoming_record_footprint_profile",s)
    m.temp.update(asteroid_incoming_profile_candidate=60,asteroid_incoming_ring_candidate=1)
    m.call("asteroid_incoming_record_footprint_profile",size)
    # Different fake profiles on duplicate rows cannot override the state's stored strongest mirror.
    for s in (1,size,1):
        for column,value in (("states",s),("profiles",10),("rings",2)):
            m.arrays["global.asteroid_incoming_footprint_"+column].append(value)
    foreign,stale,unplanned = size+1,size+2,size+3
    for s in (foreign,stale,unplanned):
        m.reg[s] = {"asteroid_incoming_state_profile":60,"asteroid_incoming_state_transaction_id":7}
        m.population[s],m.buildings[s] = 100000,{"industrial_complex":4}
    m.state_flags[foreign] = {"asteroid_incoming_state_planned"}
    m.state_flags[stale] = {"asteroid_incoming_state_planned"}
    m.reg[stale]["asteroid_incoming_state_transaction_id"] = 6
    for s in (stale,unplanned):
        for column,value in (("states",s),("profiles",60),("rings",1)):
            m.arrays["global.asteroid_incoming_footprint_"+column].append(value)
    # A registry member absent from the declared world cannot invent a state iterator object.
    for column,value in (("states",size+10000),("profiles",60),("rings",1)):
        m.arrays["global.asteroid_incoming_footprint_"+column].append(value)
    m.world_states = list(range(1,size+4))
    m.calls.clear()
    m.call("asteroid_incoming_process_footprint",m.owner)
    dispatch = [s for name,s in m.calls if name == "asteroid_incoming_apply_state_profile"]
    physical = [s for name,s in m.calls if name == "asteroid_incoming_apply_state_transaction"]
    assert Counter(dispatch) == Counter(range(1,size+1))
    assert Counter(physical) == Counter(range(1,size+1))
    assert m.population[size] == 50000 and all(m.population[s] == 75000 for s in range(1,size))
    assert all(m.population[s] == 100000 and m.buildings[s]["industrial_complex"] == 4 for s in (foreign,stale,unplanned))
    assert m.reg["global"]["asteroid_incoming_affected_state_count"] == size
    assert m.reg["global"]["asteroid_incoming_total_deaths"] == (size-1)*25000+50000
    assert len(m.deaths) == size
    assert Counter(s for s,_,_,_ in m.deaths) == Counter(range(1,size+1))
    assert m.reg["global"]["asteroid_incoming_affected_country_count"] == 2
    # Persistent count is independent of later working-array cleanup.
    m.arrays["global.asteroid_incoming_affected_country_entries"].clear()
    assert m.reg["global"]["asteroid_incoming_affected_country_count"] == 2
    # Restore the declared recipient callback output before a deliberate processor reentry.
    m.arrays["global.asteroid_incoming_affected_country_entries"] = [m.owner,m.controller]
    physical_before = copy.deepcopy((m.population,m.buildings,m.deaths,m.removals))
    receipts_before = {s:copy.deepcopy(m.reg[s]) for s in range(1,size+4)}
    m.calls.clear()
    m.call("asteroid_incoming_process_footprint",m.owner)
    assert Counter(s for name,s in m.calls if name == "asteroid_incoming_apply_state_profile") == Counter(range(1,size+1))
    assert not any(name == "asteroid_incoming_apply_state_transaction" for name,s in m.calls)
    assert (m.population,m.buildings,m.deaths,m.removals) == physical_before
    assert receipts_before == {s:m.reg[s] for s in range(1,size+4)}
    # Source reentry resets batch summary fields. This is not full processor idempotence.
    assert m.reg["global"]["asteroid_incoming_total_deaths"] == 0
    iterator_reports.append({"world_states":size+3,"unique_processed":size,"duplicate_rows":3,
                             "rejected_foreign_stale_unplanned":3,"repeat_physical_calls":0,
                             "persistent_country_count_before_cleanup":2,"reentry_resets_batch_summary":True})
    ok("runtime iterator actual AST "+str(size))
    ok("runtime repeat physical receipts "+str(size))
fixture = {"profiles":[1,.5,.25,.05,.5,.25,.05],"people":[0,1,19,100000,100000000],
           "footprints":[999,1000,1001,1501],"corrupt":["identity","missing","stale","negative","fractional","bounds","misaligned","zero_transaction"],
           "native_removal_ratios":[0,.5,1],"native_large_level_request":1501,
           "runtime_iterator":{"sizes":[999,1000,1001,1501],"duplicate_rows":[1,"last",1],
                               "rejections":["foreign_not_in_registry","stale_transaction","not_planned","registry_only_missing_world_object"],
                               "repeat":True,"stored_profile_upgrade":[40,60],"declared_distinct_recipients":2}}
print(json.dumps({"status":"source-model passed","cases":len(checks),"building_tokens":len(ac),"deduplicated_tokens":dups,
                  "naval_base_before_after":results,"before_sha256":hashlib.sha256(before_bytes).hexdigest(),
                  "after_sha256":hashlib.sha256((ROOT/P).read_bytes()).hexdigest(),
                  "fixture_sha256":hashlib.sha256(json.dumps(fixture,sort_keys=True).encode()).hexdigest(),
                  "runtime_source_sha256":hashlib.sha256(runtime_bytes).hexdigest(),
                  "runtime_processor_profile_AST_sha256":runtime_ast_hash,"iterator_reports":iterator_reports,
                  "changed_ASTs":sorted(CHANGED),"checks":checks},indent=2))

~~~

## Read-only outer failure gate proposal, 2026-10-04

Disposition: proposed parent integration, not applied and not a completion claim.
Acceptance basis is the explicit parent request for current-transaction pre-physical proof and artifact-free planning failure.
Only this documentation section is added.
The five physical helper ASTs and all gameplay source remain unchanged.
The parent's successful rerun of the 66 actual-source scenarios is attributed evidence, and does not close this outer-ordering defect.

### Current source facts and the rollback hole

At the inspected source identities, events\028_asteroid_impact.txt:318 to 330 sets impact_resolution_started, impact_recorded, dust_history_recorded, impact outcome/date/day, dust hold/deadline and opening stage before main/fragment planning.
Its mineral-activation branch follows planning at :331 to :341, and physical processing begins at :342.
The impact/evolution history, presentation, reports and cleanup follow later in the same branch.
A successful outer condition therefore does not currently establish successful planning.

Runtime effects:858 to :881 sets fragments_applied, fragment_site, mineral_site and the transaction mirror, appends to the persistent mineral registry, and refreshes the controller pointer during planning.
Physical effects:303 to :336 requires fragment_site to enter the existing fragment-footprint helper.
Physical effects:167 to :261 records state_planned only after valid aligned registration, and signals transaction_failed_closed on refusal.
A failed first center registration can therefore leave a permanent fragment/mineral flag without state_planned.
Such an orphan cannot safely qualify for the requested planned/current-transaction/unprocessed rollback.
Current flags alone also do not establish whether a mineral-registry entry or controller pointer existed before this attempt.
Adding only a .4 failure gate and clearing all footprint mineral flags would leave this hole or erase legitimate sites.

The existing transaction cleanup is not an abort contract.
Effects:1620 to :1660 clears planned flags through the entire footprint array without transaction/applied qualification, refreshes the entire persistent mineral registry, writes last_transaction_id, clears the transaction ID and clears the failure signal.
It does not clear temporary fragment-site publication or the six fragment-state aliases.
Runtime:2007 to :2017 clears lock/chooser/backup aliases and sets transaction_resolved.
Neither helper should be treated as provenance-aware rollback before the parent changes or wraps its abort use.

### Exact parent ordering

Use the existing locked state as the immutable main center throughout.
Do not rebuild the target pool, reroll fragments after an integrity refusal, choose a replacement center, convert failure to a miss, or alter the original target-state ID/receipt.

1. At .4 entry distinguish a genuinely active unresolved locked transaction from a duplicate/resolved callback.
A duplicate must exit without entering the current generic else branch, since that branch can publish a fail-closed follow-up after a successful impact.
Freeze the positive transaction nonce T and exact locked-state identity in caller-owned storage, and keep only the reentry latch impact_resolution_started before planning.
If helpers return temporary proof values, .4 owns their initial storage before each consumed call.

2. Capture transaction-owned staging provenance before any fragment flag, registry append or alias replacement.
The receipt needs the exact T, state identity, whether the fragment flag was absent, prior mineral flag/registry membership/controller-pointer presence and value, and prior values/presence for every replaced fragment slot alias.
A private receipt or bounded before-image journal is proposed state, not an existing implemented contract.
Do not infer these before images from current flags after the chooser has written them.
The journal concerns only the selected current batch, with the existing maximum-fragment bound, and must be independent of any array it will remove from.

3. Run main planning, then preserve the current fragment selector and its count/geographic behavior.
In the chooser's accepted-batch state loop, pre-register each exact selected center by setting the existing candidate profile to fragment_center and ring to zero, initializing profile_recorded to zero, and calling the existing record_footprint_profile.
Require its success plus matching T, planned flag, cache identity and expected center profile before minting a temporary current-attempt fragment_site flag.
Only then call the existing plan_fragment_footprint, whose center registration is a harmless deduplicated second registration.
This narrow caller change preserves the five physical helper ASTs and the existing fragment helper's flag guard.
It guarantees that every fragment flag this attempt creates already has the planned/current-T receipt needed for rollback.
The fragment flag is an ordinary untimed native flag, so staged ownership and explicit rollback supply its temporary lifecycle rather than automatic expiry.
Stop further staging after the failed-closed signal.
Defer mineral_site, the persistent mineral-registry append, mineral-controller refresh and fragments_applied=1 until successful physical processing.
The existing fragmentation_active flag is a planning input and must be restored to its entry value on abort rather than blindly erasing an older active context.

4. Run the complete proof below before process_footprint, capital relocation, preparedness grants, secondary-disaster dispatch or any impact/Dust/history publication.
A malformed row is a refused whole transaction, not a skipped state.
If global T or a staging receipt changed, refuse the operation and do not clean another transaction's workspace.
Keep the fixed target identity available for diagnosis or the explicitly accepted failure disposition.

5. Settle current-capital continuity before any state loss.
The existing processor calls relocate_destroyed_capital and preparedness aftermath before its iterator.
Parent must place a tested capital readback/failure gate between relocation and preparedness/physical processing, or hoist those two calls with that gate and remove their duplicate execution from the processor.
A read-only viable-backup check may precede the native relocation.
A late no-backup or relocation failure remains an unresolved accepted-contingency dependency.
Do not automatically reuse the ordinary no-impact history/news path for it, invent territory, redirect coordinates, reverse a valid unrelated capital change, or silently ship a permanently waiting branch as the solution.

6. With planning proof and accepted capital proof satisfied, execute the physical iterator once using the stored strongest state profiles.
Recheck T and the planned/member/cache proof at the iterator boundary.
Retain the applied and country-aggregation flags as the owners' idempotence receipts.
After the pass, require exactly the precomputed physical-state count and applied current-T receipts, including the pinned main center and every counted fragment center.
A post-physical fault cannot be rolled back by restoring population or buildings.
Retain actual receipts and block repeat processing rather than relabeling partial destruction as a no-impact failure.

7. Only after that physical closeout publish fragment_site/mineral_site permanence for proven applied centers, commit the actual fragment count, evaluate the existing mineral-activation condition, and refresh current mineral control.
The staged fragment_site flag already exists only on a proven current center and becomes permanent by committing its receipt.
The existing country aggregation derives fragment-center counts from state_profile, so it does not require pre-planning mineral publication.
Then write impact_recorded, impact outcome/date/day, achievement deadline, Dust hold and dust_history_recorded, calculate Dust from the actual receipts, record evolutions/impact history and dispatch presentation/news/country reports.
Finalize the persistent affected-country receipt before cleanup.
The current rescue initialization reads the stored profile and monthly fractions, not the moved impact day/date, as verified at runtime:1015 to :1083.
Its initialization and current country aggregation therefore have no demonstrated need for the early impact/Dust publication.
Any newly integrated consumer that needs a start timestamp must receive a private staged timestamp or a proved commit-time value, rather than forcing public impact history before planning.
Keep the exact current evolution/settings policy with the parent and its existing probability specialist.
No tuning, weights, thresholds or candidate targets are selected by this proposal.

8. An integrity refusal before physical processing performs only qualified staging rollback.
Under the requested no-artifact contract it emits no impact/Dust/evolution history, impact news, super-event/audio, Air Cleanliness injection, recovery state, or secondary disaster.
Keep the already accepted opening history intact.
Whether to publish the existing fail_closed outcome/history/news.97 for a planner-integrity refusal is a separate explicit disposition, since it is itself a history/news artifact.
The current generic .4 else branch must not be reused silently for that policy.

### Complete proof before the iterator

Initialize caller-owned validation counts and invalid-result storage before the validation pass.
Use every_state over real state objects with exact array membership to count validated unique members.
Use the installed scope iterator as a declared model, and do not substitute a >1000 numeric array scan.

- T is positive, unchanged from entry, active and unresolved, and there is no failed-closed planning signal.
All three footprint columns have the same nonzero length.
The locked-state pointer and saved ID still identify the same real state.

- For every represented state, require state_planned, state_transaction_id=T, state_footprint_transaction_id=T, an integral nonnegative cached index, separate bounds in all three columns, exact state identity in states[index], and exact agreement of state_profile/state_ring with profiles[index]/rings[index].
Do not enter an untrusted array scope before its bounds and real-object identity are established.
Do not use scope_exists on a variable as object validation.

- Require the validated unique real-state count to equal the row count.
This catches duplicate rows, a row with no world object, a country token in the state column, an unplanned or foreign member, an omitted current member and stale cache rows.
The earlier consumer test tolerates duplicate rows without double physical application, but that is not approval for malformed planner output.
The outer gate should refuse such output.

- Require one pinned main-center row and no other main-center profile.
Use the source constants for the canonical profile/ring pairs: main_center/0, main_ring_one/1, main_ring_two/2, main_ring_three/3, fragment_center/0, fragment_ring_one/1 and fragment_ring_two/2.
Reject unknown profiles or wrong pairs.
Do not normalize a bad value to the getter's zero default and continue to the fixed Dust base.

- Validate fragment centers against the current selected-center registry, its exact count and slot identities, the accepted minimum/maximum, current-T creation provenance, exclusion from the main footprint and prior centers' forbidden first rings, and center profile/ring 50/0 through the corresponding constants.
Do not use the original selection trigger unchanged after registration, because it rejects a state already in the selected registry.
Validate registered proof instead of rerolling.

- Keep graph integrity separate from physical eligibility.
The current ring-candidate trigger deliberately admits empty and impassable graph carriers.
They can be valid rows with no physical application under the existing resolvable predicate.
Count those rows for complete graph proof and count eligible physical states separately using the actual resolvable predicate.
The pinned main center and counted fragment centers must be physically resolvable.
An already-applied or country-aggregated current member is an idempotence conflict, not an ordinary graph carrier.
This preserves shortest-land-ring traversal while preventing a malformed no-op transaction from generating Dust.

### Qualified rollback and preservation contract

For a fragment-site rollback candidate, require all of the following together: the bounded current-batch creation receipt with T and exact state ID, current fragment-registry membership, state_planned, state_transaction_id=T, unprocessed state_transaction_applied absence, exact retained center receipt, fragment_site, absence of main_crater, and state identity distinct from the fixed main center.
Never run permanent site cleanup over all global footprint states.
Never clear an older site just because it has a current controller or appears in a mineral array.

| Surface | Abort action permitted only with the receipt above |
| --- | --- |
| fragment_site | Clear only when this attempt minted it from an absent before image. Existing/legacy, stale-T, processed or main-center flags stay intact. |
| mineral_site | Preferred ordering never writes it before success, so abort leaves it untouched. Compatibility rollback may restore only a proven current-attempt write from its before image. |
| global.asteroid_incoming_mineral_site_states | Preferred ordering leaves it untouched. Compatibility removal is by the exact newly appended state value only when it was absent before and remains one proven new entry. Preserve old entries and relative order. |
| asteroid_incoming_mineral_controller | Preferred ordering never refreshes it during planning. Compatibility rollback restores the recorded old pointer or clears only a pointer first created by this attempt. |
| fragment_1_state through fragment_6_state | Restore the recorded prior alias or clear only the slot this T replaced, and only while the alias still points to that receipt's exact selected state. Keep original/locked/main-center aliases distinct. |
| fragment controller aliases | Restore only aliases actually written by this attempt. The current chooser's site refresh writes a normal controller variable, not these aliases, so do not clear controller aliases speculatively. |
| fragment_site_states, reserved_first_ring_states, site_countries and count | Restore their entry images or clear only a proven current-T staging workspace after qualified state/alias rollback. Do not clear a legacy registry based solely on its name. |
| planning flags and caches | Clear only current-T unprocessed planned markers through qualified real state scopes, with permanent-site rollback restricted to selected fragment centers. Retain or restore cache/profile metadata by provenance. Do not clear applied, aggregated, mineral, crater or legacy receipt fields. |
| impact/Dust/history flags and variables | Preferred ordering has not written them, so abort performs no compensating clear/reset. Never zero another live Dust or Air Cleanliness source. |
| failure/latch/transaction context | Consume the failure signal and journal before clearing nonce/aliases. Close or release the latch only through the parent-accepted failure disposition. A changed nonce or ambiguous provenance is blocked cleanup, not permission to erase another context. |

Use a different bounded current-batch journal when removing from the mineral registry, not an iterator over the array being modified.
The installed remove_from_array contract removes an element by value or index.
It does not document deleting every duplicate, so malformed multiplicity needs refusal rather than silent sweeping.
Global targets need exact targeted clear/restore, and regular targets expire with the originating chain.
Do not use clear_global_event_targets as a blanket rollback.

Without the pre-registration write order and before-image ownership receipt, the present chooser cannot meet this rollback contract.
The orphan-before-state_planned counterexample is an unresolved implementation defect, not a successful no-op or a verified fail-closed branch.

### Fresh MCP and source evidence for this proposal

All new inspections were read-only, and no native behavior is claimed.
The context bundle initially omitted six source topics, so targeted search/read was used for the relevant detailed rules rather than treating headings as coverage.

- Fresh source lookup initially returned indexed revision 29457947718ecf7cde09117a61525bc4b49cdbe645bd12aef2d09bb383f4d96f.
The bounded continuation correctly returned SOURCE_REVISION_STALE with current revision 36ca4c3be2fd6008caa6dbe1968e47a8cf185fc6e2353e026acd042f07495462.
A new lookup without the stale expectedRevision then read choose_fragment_sites:852 to 896 at fresh revision ee16f1dacebf49d427b40f03c2885f015fed64a3675ce97783734888823d1b08.
Cleanup source was read at revision 36ca4c3be2fd6008caa6dbe1968e47a8cf185fc6e2353e026acd042f07495462 and supplemented by the direct complete block.
These are separate indexed snapshots, not one invented revision.

- Installed effects documentation was read through revision-bound reference_read at lines 4155 to 4172, 2713 to 2722, 6016 to 6030 and 2733 to 2741.
The exact path is C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md, revision/SHA-256 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.

- Offline Data structures Arguments was read at lines 1078 to 1107, path C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md, revision/SHA-256 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4.

- Refreshed .4 event trace returned EVENT_INSPECTED_PARTIAL, focused revision f0e16475c8407b53ed214cb41838952142f1cd8c62e083191f7d8916d82ac506, helpers=0, with whole-workspace helper/lifecycle passes deferred.
Its report is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce7654b29edfefbae63bbfa1e72d32d6d32c6d8b5fbf3aeedb2636a481a8b31c/4d90a27443ff09cdadfa0812daeacc1792891b26c22b8611981b471b9c7a5264/event-trace-f0e16475c840.json.
This focused report does not prove the helper transaction or clear unresolved analysis.

- Bounded state-64 map lookup returned MAP_LOOKUP_COMPLETED at revision db506e6eafcd7513a9aa63f77def167ab18ed365ec83ae6fb56052b1063d1e30.
Its report is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14c2ca7717c5697b74e62c9bc568408b17f9eee31ae905cae729b03a2ea083d4/1efb85836272c72dd96a1084493414359cb050aeae8ab602fe58ab84b45ad967/map-lookup.db506e6eafcd7513.8d030eb3664782be.json.
This verifies route availability and a bounded lookup, not impact geography or native transactions.

The directly read event, runtime, physical effects and trigger raw SHA-256 identities are respectively E9C436B8D1393F354BF5BE6235CCC2FB4205E0413309EAAD7DAF60267F9BA943, 377003CD7FA7337BD60B95BEA4F22886D133595C842369B314AAD015BC1DCC8B, D3C5A26E55EDFA2439A833ADA0D6CC9F13C5794FCBA8857BAF3E6D0F73B97438 and D591180EDE589C319D6077028736EDAFC184DECB86F62E2D48BFEC3F8AF81A4B.
The runnable projection below reads the actual files again and prints their fresh identities.
Its prospective phases and guard fixtures are architecture evidence only, and must not be labeled an implemented after-source comparison.
The fresh projection run passed 23 read-only architecture cases against runtime SHA-256 276cbaf89ffcb4071a077daa6948e787d6ba723fd08d2342332e023f14eb2564, event SHA-256 e9c436b8d1393f354bf5be6235ccc2fb4205e0413309eaad7daf60267f9ba943 and unchanged physical SHA-256 d3c5a26e55edfa2439a833ada0d6cc9f13c5794fcba8857baf3e6d0f73b97438.
The runtime changed concurrently after the earlier direct snapshot, so those source identities are retained as separate reads.
The proposed guard fixtures cover member/cache/profile/canonical-ring proof and current-center rollback predicates, while geometric separation/slot binding, the accepted capital contingency, full journal restoration, native callbacks and post-physical closeout remain parent implementation and validation requirements.

### Runnable actual-source AST projection and proposed guard cases

Run the final Python block in this document, rather than the first 66-case block, to inspect this proposal.
No file writes, patch application or native calls occur.
The proposed guard uses declared world objects and before-image receipts.
It is deliberately distinct from the executed current-runtime tests above.

~~~python
import copy, hashlib, json, re, sys
from pathlib import Path
ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / ".tools/validation"))
from validate_028_availability import parse_source
paths = {
    "event": "events/028_asteroid_impact.txt",
    "runtime": "common/scripted_effects/028_asteroid_incoming_runtime_effects.txt",
    "physical": "common/scripted_effects/028_asteroid_incoming_effects.txt",
    "triggers": "common/scripted_triggers/028_asteroid_incoming_triggers.txt",
}
raw = {k:(ROOT/p).read_bytes() for k,p in paths.items()}
class Text:
    def __init__(self, value): self.value=value
    def read_text(self, encoding): return self.value.decode("utf-8-sig")
runtime = parse_source(Text(raw["runtime"]))
physical = parse_source(Text(raw["physical"]))
event_rows = parse_source(Text(raw["event"]), rows=True)
constants = parse_source(ROOT / "common/script_constants/028_asteroid_incoming_constants.txt")
def fields(rows): return dict((k,v) for k,_,v in rows)
def walk(rows):
    for row in rows:
        yield row
        if isinstance(row[2],list): yield from walk(row[2])
def c(category,key): return float(fields(constants[category])[key])
events = [v for k,_,v in event_rows if k=="country_event" and fields(v).get("id")=="chaosx.nr28.4"]
assert len(events)==1
immediate = fields(events[0])["immediate"]
resolver = next(v for k,_,v in immediate if k=="if")
rows = [r for r in resolver if r[0]!="limit"]
plan_at = next(i for i,r in enumerate(rows) if r[0]=="asteroid_incoming_plan_main_footprint")
process_at = next(i for i,r in enumerate(rows) if r[0]=="asteroid_incoming_process_footprint")
assert any(k=="set_global_flag" and v=="asteroid_incoming_impact_recorded" for k,_,v in rows[:plan_at])
assert any(k=="set_global_flag" and v=="asteroid_incoming_dust_history_recorded" for k,_,v in rows[:plan_at])
chooser = runtime["asteroid_incoming_choose_fragment_sites"]
site_loop = next(v for k,_,v in walk(chooser)
                 if k=="for_each_scope_loop" and fields(v).get("array")=="global.asteroid_incoming_fragment_site_states")
site_body = [r for r in site_loop if r[0]!="array"]
assert next(i for i,r in enumerate(site_body) if r[:2]==("set_state_flag","=") and r[2]=="asteroid_incoming_fragment_site") < next(i for i,r in enumerate(site_body) if r[0]=="asteroid_incoming_plan_fragment_footprint")
assert fields(physical["asteroid_incoming_plan_fragment_footprint"])["if"][0][0]=="limit"
# Preserve exact source nodes, but return phase data only. There is no engine-source output.
latch = [copy.deepcopy(r) for r in rows[:plan_at] if r[:2]==("set_global_flag","=") and r[2]=="asteroid_incoming_impact_resolution_started"]
commit_metadata = [copy.deepcopy(r) for r in rows[:plan_at] if r not in latch]
plan_calls = [copy.deepcopy(r) for r in rows[plan_at:process_at] if r[0] in ("asteroid_incoming_plan_main_footprint","asteroid_incoming_choose_fragment_sites")]
mineral_activation = [copy.deepcopy(r) for r in rows[plan_at:process_at] if r[0]=="if"]
publication = [copy.deepcopy(r) for r in site_body if r[0] in ("set_state_flag","if","asteroid_incoming_refresh_site_mineral_control")]
assert len(latch)==1 and len(plan_calls)==2
assert not any(k in ("set_variable","set_global_flag") and "dust" in str(v) for k,_,v in latch+plan_calls)
projection = {
    "entry": latch,
    "planning_calls_with_qualified_center_preregistration_proposal": plan_calls,
    "gate": "prospective complete world/member/cache/profile proof plus explicit accepted capital gate",
    "physical": copy.deepcopy(rows[process_at]),
    "after_physical_fragment_publication": publication,
    "after_physical_mineral_activation": mineral_activation,
    "after_physical_impact_metadata": commit_metadata,
    "existing_success_tail": copy.deepcopy(rows[process_at+1:]),
}
canonical = {c("asteroid_incoming_profile",k):ring for k,ring in
             (("main_center",0),("main_ring_one",1),("main_ring_two",2),("main_ring_three",3),
              ("fragment_center",0),("fragment_ring_one",1),("fragment_ring_two",2))}
main_profile = c("asteroid_incoming_profile","main_center")
fragment_profile = c("asteroid_incoming_profile","fragment_center")
def prospective_gate(world, columns, tx, locked, centers, journal, failed=False):
    ids,profiles,rings = columns
    if failed or tx<=0 or not (len(ids)==len(profiles)==len(rings)>0): return None
    valid=physical_count=main_count=fragment_count=0
    for sid,state in world.items(): # declared each-real-world-state-once scope iterator
        if sid not in ids: continue
        index=state.get("index",-1)
        if index<0 or index!=int(index) or not all(index<len(a) for a in columns): return None
        index=int(index)
        if not state.get("planned") or state.get("tx")!=tx or state.get("cache_tx")!=tx: return None
        if ids[index]!=sid or profiles[index]!=state["profile"] or rings[index]!=state["ring"]: return None
        if state["profile"] not in canonical or canonical[state["profile"]]!=state["ring"]: return None
        if state.get("applied") or state.get("aggregated"): return None
        valid+=1
        resolvable=not state.get("impassable") and state.get("owner_alive",True) and state.get("controller_alive",True)
        physical_count+=int(resolvable)
        if state["profile"]==main_profile:
            if sid!=locked or not resolvable: return None
            main_count+=1
        if sid in centers:
            receipt=journal.get(sid,{})
            if sid==locked or state["profile"]!=fragment_profile or not resolvable: return None
            if receipt.get("tx")!=tx or receipt.get("id")!=sid or receipt.get("before_fragment") is not False: return None
            fragment_count+=1
        elif state["profile"]==fragment_profile: return None
    if valid!=len(ids) or main_count!=1 or fragment_count!=len(centers): return None
    minimum=c("asteroid_incoming_runtime","minimum_fragment_centers_to_apply")
    maximum=c("asteroid_incoming_runtime","maximum_fragment_sites")
    if centers and not minimum<=len(centers)<=maximum: return None
    return {"rows":valid,"expected_physical":physical_count,"expected_fragments":fragment_count}
def rollback_candidate(sid,state,tx,locked,centers,journal):
    receipt=journal.get(sid,{})
    return (sid in centers and sid!=locked and not state.get("main_crater")
            and state.get("planned") and state.get("tx")==tx and state.get("cache_tx")==tx
            and state.get("profile")==fragment_profile and state.get("ring")==0
            and not state.get("applied") and not state.get("aggregated")
            and state.get("fragment") and receipt.get("tx")==tx and receipt.get("id")==sid
            and receipt.get("before_fragment") is False)
ids=[1,2,3,4]
profiles=[main_profile,fragment_profile,fragment_profile,c("asteroid_incoming_profile","main_ring_three")]
rings=[0,0,0,3]
world={sid:{"index":i,"profile":profiles[i],"ring":rings[i],"tx":7,"cache_tx":7,"planned":True,
            "fragment":sid in (2,3),"main_crater":False,"applied":False,"impassable":sid==4}
       for i,sid in enumerate(ids)}
journal={sid:{"tx":7,"id":sid,"before_fragment":False} for sid in (2,3)}
good=prospective_gate(world,(ids,profiles,rings),7,1,[2,3],journal)
assert good=={"rows":4,"expected_physical":3,"expected_fragments":2}
cases=["valid graph carrier retained, expected physical count distinct"]
for fault in ("misaligned","duplicate","missing_world","stale_tx","stale_cache","fractional_index",
              "wrong_identity","wrong_profile_mirror","unknown_profile","wrong_ring","unplanned",
              "applied","aggregated","redirected_main","unresolvable_main","unowned_fragment"):
    w=copy.deepcopy(world); a=copy.deepcopy([ids,profiles,rings]); j=copy.deepcopy(journal); lock=1
    if fault=="misaligned": a[1].pop()
    elif fault=="duplicate":
        for column,value in zip(a,(1,main_profile,0)): column.append(value)
    elif fault=="missing_world": del w[3]
    elif fault=="stale_tx": w[2]["tx"]=6
    elif fault=="stale_cache": w[2]["cache_tx"]=6
    elif fault=="fractional_index": w[2]["index"]=1.5
    elif fault=="wrong_identity": w[2]["index"]=0
    elif fault=="wrong_profile_mirror": w[2]["profile"]=main_profile
    elif fault=="unknown_profile": w[2]["profile"]=a[1][1]=999
    elif fault=="wrong_ring": w[2]["ring"]=a[2][1]=2
    elif fault=="unplanned": w[2]["planned"]=False
    elif fault=="applied": w[2]["applied"]=True
    elif fault=="aggregated": w[2]["aggregated"]=True
    elif fault=="redirected_main": lock=2
    elif fault=="unresolvable_main": w[1]["impassable"]=True
    else: j[2]["before_fragment"]=True
    assert prospective_gate(w,a,7,lock,[2,3],j) is None,fault
    cases.append("reject "+fault)
assert prospective_gate(world,(ids,profiles,rings),7,1,[2,3],journal,failed=True) is None
cases.append("planning failure refuses success publication")
assert rollback_candidate(2,world[2],7,1,[2,3],journal)
for condition in ("main","legacy","stale","processed","unplanned_orphan"):
    s=copy.deepcopy(world[2]); j=copy.deepcopy(journal); sid=2; lock=1
    if condition=="main": lock=2
    elif condition=="legacy": j[2]["before_fragment"]=True
    elif condition=="stale": s["tx"]=6
    elif condition=="processed": s["applied"]=True
    else: s["planned"]=False
    assert not rollback_candidate(sid,s,7,lock,[2,3],j)
    cases.append("rollback preserves "+condition)
print(json.dumps({"status":"read-only prospective architecture cases passed","cases":len(cases),
                  "current_source_sha256":{k:hashlib.sha256(v).hexdigest() for k,v in raw.items()},
                  "projection_phase_names":list(projection),"valid_proof":good,
                  "orphan_before_planned_is_not_safe_rollback":True,
                  "native_acceptance":False,"source_applied":False,"checks":cases},indent=2))
~~~
