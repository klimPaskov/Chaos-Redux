# C6 nonhuman human-system boundaries, 13 October 2026

## Current conclusion

C6 source closure is implemented for the audited human-system boundaries, including native country-targeted attacker protection and synchronous inherited sanction cleanup.
The first two repair commits are preserved.
The third-round closure below records the broadened inherited/legacy audit, accepted parser repair, matching helper contracts, meaningful checks and native-engine verification limits.

No push or game launch occurred.

- `b3946629cfdade087cfa4204e1c4efa053489bc1`: human casualty, disease, camp, inherited modifier, pollution, panic and legacy population boundaries, 27 paths.
- `22802baa3b38c963410ab6d6e4686649adba7625`: human condemnation eligibility and inherited owned-pair reconciliation, 6 paths.

The shared shell outage interrupted verification, and execution recovered during the continuation.
The four pending writes were inspected and confirmed before any replay, and source checks completed after recovery.
Both source themes used reviewed isolated indexes, captured real-index entries and compare-and-swap ref publication.
Path-specific real-index reconciliation was verified, preserving unrelated working changes.
HEAD guards prevented publication of stale condemnation trees during intervening commits, and the candidate was rebuilt against the new HEAD before publication.
The parent owns the restore-plan C6 status and any eventual commit annotation.

## Authorization and history evidence

Scope comes from C6 in `docs/plans/chaos_redux_restore_plan_2026-10-12.md` and the parent's explicit assignment to exclude nonhuman actors from human-targeted systems while preserving ordinary warfare, new mechanics and dynamic values.
This is a scripted-system repair, with no historical text, art or balance rewrite.

Inspected classifier history: `a382b251b`, `76d2bc4a4`, `5aad4b796`, `6be345bcb`, `76682d528` and `726103283`.
Commit `76d2bc4a48e06ae24beb7023b5aaac8bd195d6fd` removed the literal `original_tag = ZZZ` from the shared classifier, but `is_zombie_outbreak_country` still contains that exact condition.
Its replacement therefore preserves the original exclusion and does not warrant a restore.
The same commit replaced literal Death conditions with `is_death_country`.
No exact restore was performed because the inspected history did not prove a removed classification behavior.

The existing `is_actual_nonhuman_country` registry covers outbreak actors, Wendigo markers, ZIN, Death, DHO/cave actors, nonhuman derivative families, actual nonhuman Kruger transitions and rat actors.
The existing inverse `uses_normal_civilian_systems` remains the country classifier.
Human special countries remain human, including the Holy Realm.
Famine and migration retain their stricter existing special-country eligibility rules and the existing Holy Realm exception.

## Implemented source changes

| File | Owned change |
| --- | --- |
| `common/scripted_triggers/chaosx_dynamic_triggers.txt` | Add hidden state classifier `state_uses_normal_civilian_systems`, requiring existing human OWNER and CONTROLLER. |
| `common/scripted_triggers/chaosx_dynamic_triggers.md` | Document the state classifier's scope, inputs, output, side effects, example and consumers. |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | Reject an exact human civilian loss request when either holder is nonhuman, returning zero and clearing the existing inputs. Preserve the other owner's positive population helper. |
| `common/scripted_effects/chaosx_dynamic_effects.md` | Document rejected nonhuman civilian transactions. |
| `common/scripted_effects/chaos_meter_effects.txt` | Guard combat civilian deaths and percentage-based state mortality by the state classifier. Reject known nonhuman country targets in the human Deaths ledger, without changing native war damage. |
| `common/scripted_triggers/biological_lifecycle_triggers.txt` | Apply the state classifier to ordinary episode admission, in addition to the original zombie, wasteland and population checks. |
| `common/scripted_effects/biological_lifecycle_effects.txt` | Add `bio_lifecycle_retire_current_agent_for_nonhuman_state` at existing activation/tick boundaries, clearing live flags, deadlines and human burden while retaining history and granting no recovery achievement. |
| `common/scripted_effects/cbrn_consequence_effects.txt` | Filter hostile and friendly direct chemical `damage_units` by unit-owner classification. Guard first exposure shock and state medical burden. Derive the unified military fraction only from eligible human armies. |
| `common/scripted_effects/cbrn_scripted_effects.md` | Document direct damage, normalized human-only fraction and biological retirement contracts, including native combat-area limitations. |
| `common/scripted_triggers/cbrn_scripted_triggers.md` | Document ordinary disease admission through the common state gate. |
| `common/scripted_triggers/camp_repression_rework_triggers.txt` | Add human classification to country eligibility and current state classification to active-site validity. |
| `common/scripted_triggers/camp_administration_triggers.txt` | Require a human-owned and human-controlled operational site. |
| `events/041_disease_in_divisions.txt` | Select human random recipients and allow the fallback only for a human root. Existing disease damage tuning and the legacy `always = no` damage limits are preserved. |
| `events/043_massive_flood.txt` | Guard direct state population debits and human report delivery, preserving physical building damage and original amounts. |
| `common/scripted_effects/condemnation_sanctions_effects.txt` | Add human source and maintenance boundaries, filter candidate/target/participant admission, and snapshot invalid owned sanction pairs for existing exact teardown. |
| `common/scripted_triggers/condemnation_sanctions_triggers.txt` | Require human holders for public/tier/response eligibility and both human parties for diplomatic pair eligibility. Preserve the other owner's unrelated trailing-line change. |
| `common/decisions/categories/condemnation_sanctions_categories.txt` | Hide both human condemnation categories from nonhuman actors. |
| `docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md` | Document source and maintenance contracts, frozen cleanup array, owned relation teardown and existing scheduling latency. |

Inherited state modifiers retain their original numeric values, `attacker_modifier` behavior and stage conditions, with the shared state classifier added to `enable` in these files:

- `common/dynamic_modifiers/famine_state_modifiers.txt`, 4 state definitions and the country-scoped `famine_national_food_crisis`, which uses the country classifier.
- `common/dynamic_modifiers/migration_state_modifiers.txt`, 10 definitions.
- `common/dynamic_modifiers/biowarfare_state_modifiers.txt`, 6 definitions.
- `common/dynamic_modifiers/chemical_state_modifiers.txt`, 2 definitions.
- `common/dynamic_modifiers/camp_administration_dynamic_modifiers.txt`, 2 definitions, with the country classifier on its country modifier.
- `common/dynamic_modifiers/022_concentration_camps_dynamic_modifiers.txt`, 1 definition.
- `common/dynamic_modifiers/air_contamination_dynamic_modifiers.txt`, 1 definition.

Inherited country sanctions use the country classifier in all 7 definitions in `common/dynamic_modifiers/condemnation_sanctions_dynamic_modifiers.txt`.
The same classifier is added through `do_effect` to human pressure ideas in `common/ideas/air_contamination_ideas.txt`, `common/ideas/049_mass_panic_ideas.txt` and `common/ideas/condemnation_sanctions_ideas.txt`.
The A5 worker owns only the `doomsday` picture binding in the shared mass-panic idea file, and that hunk must remain separate from C6 publication.

## Recovered native write confirmation

One shell command was issued to snapshot and guard exactly these direct negative manpower statements, and its successful completion and fresh source inspection were confirmed after execution recovered:

- `events/069_boxer_rebellion.txt`: country loss `-5000000`.
- `events/076_usa_tests_weapons.txt`: country loss `-10000`.
- `common/on_actions/080_airship_on_actions.txt`: crash state loss `-5000`.
- `common/decisions/080_airship_decisions.txt`: crash state loss `-3000`.

Historical interruption: session `84672` originally returned no output, and inspection sessions `62995` and `11278` were also pending.
After recovery, session `84672` returned successful guard messages for all four paths, and fresh inspection session `42991` read each resulting human-only statement with its original amount.
No second mutation was issued, and there is no remaining uncertain write among these four paths.
The intended state gates preserve physical crash damage, costs, random chance and the existing on-action scheduling.

## Helper, tuning and cleanup map

`state_uses_normal_civilian_systems`: state scope, no parameters, hidden boolean, no side effects, no cached state.
`bio_lifecycle_retire_current_agent_for_nonhuman_state`: state scope, input `bio_active_agent`, no return status required, clears only the current agent's live human episode and services through existing helpers, preserves immutable history and creates no recovery reward.
`condemnation_add_human_source_internal`: country scope, existing source temporary inputs, existing human arithmetic and side effects, called only by the public `condemnation_add_source` human boundary.
`condemnation_monthly_human_pulse_internal`: country scope, existing maintenance state and timers, called only by the public human maintenance boundary.
`cbrn_action_human_military_death_fraction`: caller-owned temporary output declared by `cbrn_dispatch_chemical_action_record` before the direct damage helper and consumed by `cbrn_dispatch_record_actor_history`.
It is zero for nonhuman-only armies, the hostile fraction when eligible human enemies are present, or the bounded friendly fraction when that is the applicable stronger human exposure.
It is a normalized damage receipt and cannot be presented as a killed-person count.

No C6-owned constants, tuning values, event IDs, global event targets, assets, GUI geometry or localisation keys were changed.
The only new persistent array is the country-owned `condemnation_nonhuman_cleanup_participants` scratch snapshot, built and cleared within one existing reconciliation call.
The snapshot prevents removing a sanction pair from its source array during enumeration.
`condemnation_clear_sanction_pair` owns teardown of the system embargo claim, both directional opinion modifiers, recorded AI deltas, pair variables and enforcement burden.
Existing likely-participant reconciliation clears old monitoring opinions and restores their recorded watch-tier AI deltas.
Inherited native relationships are cleaned when an existing reconciliation or target pulse runs, rather than by a new global poll.

## Coverage inspected

The native/ledger inventory in `.tmp/c6_nonhuman/population_damage_inventory.json` contains 1,203 call sites across 131 files.
It includes positive recruitment and explicit resource payments, so that inventory count is not a claim that 1,203 human-harm operations were semantically audited.
The reviewed human entry boundaries cover the following families:

| Family | Source evidence and disposition |
| --- | --- |
| Famine pressure, mortality, reserves and relief | Existing `humanitarian_state_is_valid` checks human OWNER and CONTROLLER. `famine_pressure_request_is_valid` uses it. Inherited state modifiers additionally reject nonhuman holders. |
| Migration, forced returns, reception and exact transfers | `migration_pressure_request_is_valid`, `migration_destination_is_valid`, forced-return eligibility and `civilian_transfer_route_request_is_valid` use the same neutral validator. Inherited movement/depopulation modifiers additionally reject nonhuman holders. |
| Ordinary disease seeds and spread | Canonical lifecycle admission is shared by battlefield, raid, sabotage, facility capture, stockpile accident, campaign and doomsday selectors. Scheduled activation/tick retirement prevents continued progression after a nonhuman takeover. |
| Black Plague and rats | `black_plague_country_is_human_host` already uses the country classifier. The rat-controlled phase is an event-owned nonhuman source, and shared human mortality guards reject its human population loss. Its bespoke rat mechanics are preserved. |
| Camps and human custody | Country eligibility, active-site validity and operational-site authority use human guards, alongside the existing exact custody/transfer ownership. Event 22 relief and camp economy modifiers reject nonhuman holders. |
| Chemical direct unit damage and history | Both native owner-country damage limits use the classifier. Unified history stores a normalized eligible-human fraction. Biological unified history already records military deaths as zero. No defender headcount or estimated killed-person total was found in these shared adapters. |
| State civilian deaths and natural disasters | `chaos_meter_register_state_civilian_deaths_percent` and `apply_exact_state_civilian_population_loss` reject nonhuman state holders. Event 013 disaster mortality calls the percentage helper. The legacy flood bypass is guarded separately. |
| Pollution illness and inherited panic | Hidden pollution ideas include negative monthly population and are guarded through `do_effect`. State attrition and panic ideas also receive current holder classification. |
| Direct negative population natives | Flood guards are present. Boxer Rebellion, US tests and airship crash guards were confirmed by the recovered command and fresh source inspection. |
| Slavery and trafficking | Targeted script and localisation token searches found no implemented `slavery`, `slaves`, `slave_trade` or `traffick` owner system. No absent implementation was invented. |
| Physical or bespoke nonhuman damage | Asteroid impact and conventional missile `damage_units` are physical warfare. Death explicitly has separate living/nonhuman damage bands, and cave brood consolidation explicitly targets DHO. These are preserved. |
| Event 41 inherited disease idea | Event 41 grants no idea and only dispatches native damage plus popup/news. No Event 41 idea grant consumer was found. |
| Heat Wave and Half Gone | Heat Wave modifies physical heat attrition/acclimatization. Half Gone halves equipment, with no population debit. Both remain unchanged. |

The first two-commit pass did not semantically audit broader country setup, every national spirit, occupation-law modifiers or all post-30 legacy event designs.
The third-round closure below records the additional human-spirit, occupation-law and post-30 hazard inventory and its exact limits.
The source inventory supports future targeted review without presenting that remaining scope as completed.

## References and tool evidence

Live schemas were verified for `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup` and `hoi4.script_validate`.
The successful general context returned known-mistake entries, which were reviewed as reference rules rather than treated as findings against these files.
Its omitted Data structures and Modifiers coverage was not claimed as read, and relevant modifier sections were later read directly.

- Offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, lines 2359-2401, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, read through MCP. Scripted trigger definitions and `yes`/`no` invocation.
- Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, lines 329-350, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`, read through MCP. Missing target behavior and scope guards.
- Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, lines 5103-5123, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, read through MCP. Hidden trigger scopes and targets.
- `hoi4.source_lookup(is_actual_nonhuman_country)` returned its one active definition at `common/scripted_triggers/chaosx_dynamic_triggers.txt`, lines 42-62, source revision `90c42eb5b1299c9e93eba2d812da2a1ee8345cbc8d18eccb1a4bdc848a649f99`. Reference enumeration was unresolved and was not used as caller coverage.
- Installed `documentation/effects_documentation.md`, lines 3417-3437, read locally. `damage_units.limit` is explicitly a country check.
- Installed `documentation/triggers_documentation.md`, lines 1684-1691, read locally. `any_state_division` is state-scoped and supports OWNER.
- Installed `common/decisions/NOR.txt`, lines 2415-2422, read locally. Exact native precedent: `any_state_division = { OWNER = { tag = ROOT is_in_faction_with = ROOT } }`.
- Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, lines 266 and 404, read locally. Division iteration and owner-country routing.
- Installed `common/scripted_effects/ITA_scripted_effects.txt`, lines 3212-3220, read locally. Native `damage_units` uses country `original_tag = ITA` in its limit.
- Installed `common/dynamic_modifiers/0_dynamic_modifiers.txt`, lines 3-27 and its `autonomous_state` definition, read locally. `enable`, `remove_trigger`, state OWNER scope and fixed `attacker_modifier` behavior.
- Offline `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`, lines 108-130, read locally. Daily dynamic-modifier refresh and attacker spillover.

SHA-256 revisions for the seven locally read reference files are retained in `.tmp/c6_nonhuman/reference_sources.json`, alongside the exact path and line citations above.

Dynamic-modifier `hoi4.reference_search` was issued once, yielded no result for several minutes and was terminated.
`hoi4.script_validate` on the shared trigger file timed out at the service after 600 seconds, one attempt.
Neither was reported as passed and no unchanged retry was made.
A future retry requires a responsive route or a useful tool/input correction, rather than another identical request.
Local documentation and source review established the syntax above.
After the shell outage recovered, the source-derived checks described below completed successfully.
The exhausted MCP failures remain historical failures and were not retried.

## Scenario evidence and parent follow-up

Before-source bytes and SHA-256 values are retained under `.tmp/c6_nonhuman/before/<repo-relative-path>` and `.tmp/c6_nonhuman/before_manifest.json`.
These are working-source baselines and may contain earlier unrelated owner edits.
The parent was given a bounded probability-audit fixture for condemnation participant/target gates, ordinary disease spread eligibility and the Event 41 random recipient pool.
The parent relayed and accepted the independent `c6_c10_probability` source-derived audit.
It found unchanged human scores, excluded nonhuman targets/participants, owned-pair cleanup, rejected mixed holders, preserved Holy Realm human classification and a correct Event 41 qualifying pool gate.
The Event 41 direct-random MCP adapter returned an empty or mismatched candidate inventory, which was not used as probability evidence and was not retried.
No campaign firing probability is claimed.
Numeric scores and weights are preserved, but removal of nonhuman candidates changes pool membership and requires that audit.

Source review expects ordinary human holder/target pairs to keep their old values, the Holy Realm to remain human under the classifier, nonhuman owner/controller pairs to return zero civilian loss, nonhuman-only chemical armies to return zero military fraction, and human-to-nonhuman inherited sanction pairs to teardown through the existing owned-pair cleanup path.
These expectations are source-derived scenarios, not observed engine behavior.

Recovered execution of `.tmp/c6_nonhuman/check_c6.py` and a post-publication run against frozen revision `22802baa3b38c963410ab6d6e4686649adba7625` passed 24 scenarios against the parsed shared classifier: 18 country classes and 6 owner/controller combinations, including absent holders.
Owner-package classifier results were explicit fixture facts, so this does not emulate their full event lifecycle.
The same check proved exact structural equivalence of the original human source and maintenance bodies to their renamed internal bodies, preserving all existing human arithmetic.
It also compared all non-enable modifier content in 34 affected dynamic modifier definitions and 3 file-scoped constants and the modifier values in 35 affected ideas against the captured baselines.
The results are saved in `.tmp/c6_nonhuman/check_results.json`.
Full consumer-scope review caught the national famine modifier inside the state-modifier filename and corrected its guard to the country classifier.
The recovered scope check verifies the expected classifier in each actual modifier enable block, and passed after that correction.

Publication used `.claude/skills/chaos-redux-shared-git-commit/SKILL.md`.
The parent reviewed the human and condemnation patches and accepted the independent source-derived weighted review before publication.
The committed diffs exclude the other owner's positive population helper, crisis-pressure documentation, D4 advisor changes, Event 41 report art, A5 picture binding, unrelated trailing-line cleanup and the parent restore-plan edit.
The airship decision retained its original CRLF bytes and was staged as an exact reviewed one-line-change blob.

## Historical first-pass remaining items

No alternate mechanics or design simplifications were introduced, and all existing human tuning, costs and ordinary warfare remain intact in the reviewed patches.
The absolute C6 requirement remains unmet for native combat-area modifiers affecting nonhuman attackers in human-held states.
Immediate inherited native relation cleanup before the next existing reconciliation is also not established.
The independent source-derived weighted review was accepted and both reviewed source themes were published.
Only the parent owns the broader C6 disposition and any future redesign for native combat-area filtering.
The direct-native write outcomes are confirmed.
The source checks above cover classification and unchanged human values, with no live-engine proof.
No assets or player-facing text were required by these hidden classification guards.

Skills used: canonical `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-map-states`, `chaos-redux-decisions-missions`, `chaos-redux-diplomacy-war`, `chaos-redux-ideas-modifiers` and `chaos-redux-shared-git-commit`.
No skill was created or updated.

## Third-round closure and acceptance

The parent assigned closure of every remaining C6 human-system path and explicitly accepted the native country-targeted state pattern after reviewing the installed add/presence/removal contract.
The parent also accepted the exact concurrent load-repair hunks from `.tmp/live_verification_2026-10-13/human_modifier_load_repair.md` into this C6 source theme.
The parent additionally accepted the two C6-only fixes in `.tmp/live_verification_2026-10-13/final_parser_repair.md`, converting the remaining chemical delivery event call and correcting optional FROM presence to the native nested `FROM = { scope_exists = yes }` trigger.
Other migration enum and combat-constant fixes in that batch are excluded from C6 publication.
That external worker corrected the unsupported parameter-call draft to the supported caller-owned token/day temporary inputs and native meta text, initialized the date-converter return before the child call, and retained the existing modifier state/country registries and native duration sources.
This report records the external provenance and does not claim authorship of that repair.
Only its C6 helper/caller/documentation regions and the 23 required synchronized modifier tokens belong to this publication.
Other live-repair, migration, sanctions restoration, duplicate-grant, transport, audio and unrelated staged or unstaged changes remain separate.

| Remaining or inherited path | Current disposition and source evidence |
| --- | --- |
| Nonhuman attackers in human-held states | Implemented through native country-targeted instances for 23 human-system modifier IDs, with exact matching scope on presence/removal. Existing state variables and enable/remove stage checks are rooted to the containing ROOT state. Human values and attacker settings remain unchanged. |
| Country birth, annexed/released tags and conversion | Implemented by the registered-state remaining-lifetime binder and event-style birth/control hooks. Tag-targeted registration and cleanup receipts prevent another tag inheriting a completed receipt. A transition is scanned once, and adjacent classification writes take the cheap idempotent branch. |
| Immediate inherited sanctions and human camp relations | Implemented synchronously in both directed pair roles. Recorded watch/active AI inverses retain their exact values. All owned source claims are removed, while a native relation is broken only when it is system-created and has no external claim. Historical condemnation entries remain. |
| CBRN occupation laws and inherited authority | Both occupier and occupied scope admission are human-only, current state actions require human holders, and both AI score blocks have the matching final zero factor. Only matching CBRN default/country/state overrides are reset through the documented PREV occupier context. Ordinary occupation is preserved. |
| Human health, outbreak controls, chemical shock and physician roles | Human `do_effect` gates and synchronous removal cover the audited surveillance, vaccination, antibiotic, outbreak-control, first-exposure shock and physician ideas. Country health callbacks reject nonhuman actors and live progress flags are retired. |
| Human camp/custody and genocide spirits | All audited active camp idea groups and the inspection burden receive current human gates and exact transition removal. Genocide political/discovery callbacks and delayed events require human recipients, with current responsible/foreign target checks. The historical restored sanctions helper remains separate and retains its original numbers and effect package. |
| Event 31 human terror | Eligible incident sites require human holders. Five state stages, the four human government-emphasis modifiers, famine spirit and sky-shock recipients are guarded. The final entity, conventional offensive, presence/revolt/ruin and military route mechanics remain. |
| Event 33 evacuation and physical acid effects | The explicitly civilian evacuation disruption receives the state gate. Physical corrosion, truck/army/supply degradation and building damage remain as reviewed physical effects. |
| Events 34 and 35 human labour and economic panic | Delayed labour-dispute execution and labour settlement, human depression-country overlays, active district administration and labour scars are guarded. Permanent physical recovered/scarred district outcomes retain the original complete definitions. |
| Event 37 newcomer workforce | All five inherited newcomer/project/unrest/calm/shift modifier definitions are human-only and are removed on transformation. Existing manifestation and humanitarian admission remain. |
| Event 39 office harm and investigation | Incident selection, retained government authority, generic casualty callbacks and fresh selected-owner action predicates require current human classification. Four human office/protection/investigation spirits are guarded and retired. |
| Event 40 retained hostile mission | The live-target predicate repeats human classification after transformation, and the two active hostile institutional-pressure spirits are guarded and retired. Military, licensing and physical settlement outcomes remain. |
| Event 65 clinical-named traits | Only trauma, stammer and the two paranoia rows gain the human eligibility zero factor. The full 949-row human pool is unchanged, the remaining 945 nonhuman outcomes retain weight one, and existing current-leader clinical traits are removed at transition. The classification is clinical human assignment, not a claim that their native PP/AI modifiers implement physiological damage. |
| Native population, ordinary disease, famine, migration, direct chemical casualties and ledger gateways | Earlier b3946629c/22802baa3 boundaries are preserved and remain the common exact rejection paths. No further native civilian-loss bypass was found in the completed numbered-event hazard inventory. |
| Broader country setup and inherited ideas | The independent inherited-spirit review covered the human health, camp/custody, pressure and physician families and all Chaos Redux occupation-law definitions. Their runtime/history grant paths were inspected, and nonhuman DHO/Death/Rat bespoke starting ideas remain. |
| Post-30 legacy event scope | All 72 present numbered event files for IDs 31-69 and 71-100 were scanned for native harm and human modifier/helper/selector paths. A namespace search found no implemented 101-113 event definitions, and no Event 70 filename exists. The 193 companion paths were a relevant-operation inventory, rather than a complete design audit of every line. |
| Physical and bespoke nonhuman paths | Conventional war/unit/equipment damage and costs, flood buildings, heat, acid corrosion, landing logistics, ZIN divine warfare, cave/Death/Rat bespoke systems and anti-zombie military/technology bonuses retain their reviewed behavior. No missing system was invented. |

### Helper, constants, targets and cleanup ownership

`add_human_state_dynamic_modifier`, `remove_human_state_dynamic_modifier`, `human_state_modifier_bind_existing_country` and `refresh_human_state_modifier_country` are documented in `common/scripted_effects/chaosx_dynamic_effects.md` with their real temporary-input contracts.
All direct calls use `= yes`, with a synchronized exact modifier token and original supplied duration for addition.
The global state registry, per-state recorded country array and per-modifier expiry belong to this API and are retained across other active modifier families.
Regular chain-lifetime targets are used for state, cleanup, new-country and relation pointers.
No new global event target is introduced.
`clear_nonhuman_country_human_systems` is the idempotent country transition owner, with exact idea/flag/modifier/trait retirement and calls to the sanctions and CBRN occupation cleanup owners.
The owning sanctions document records the pair helper inputs, exact inverse use, native external claim preservation and containing-target pointer correction.
The owning occupation document records the country/state reset contexts and existing default-law cleanup.

The only added tuning literal is file-scoped `@HUMAN_TRAIT_DISABLED_WEIGHT = 0` in Event 65, used as the four clinical eligibility zero factors.
All other thresholds, weights, original human values and durations retain their existing sources.
The law AI gate uses the existing disabled-score constant, and the state binding uses the existing date-unit constants and converter.
The physical Rat-control alias `black_plague_rat_control_state` contains the original complete Rat-phase values with its phase-specific enable/removal conditions.
It reuses `GFX_idea_black_death` in `interface/chaosx_ideas.gfx` alongside the human disease modifier.
The two localization keys are `black_plague_affected_state` and `black_plague_rat_control_state`.
No new art, GUI geometry, portrait, focus tree, equipment, country package, event log, event-detail premise or spreadsheet row is introduced.

### Meaningful verification and limits

`python .tmp/handoff3/nonhuman/check_source.py` completed 103 original idea-body comparisons, 70 modifier-body comparisons, 13 preserved helper-body comparisons, 142 exact-target native operation checks, six binding/lifetime/physical-preservation source scenarios and all 23 genocide-event human gates.
It confirmed unchanged human fields and stage conditions after the ROOT qualification, preserved the monitoring inverse and native human embargo-registration body, and found the duplicate root-trigger insertion on a preconditioned genocide event.
That defect was corrected by merging the human gate with the existing event condition before the passing run.
The same scope review separated actual Great Depression state definitions from country definitions and corrected their classifier before acceptance.
The scenario model assumes the installed native keyed-scope contract and does not emulate combat.

The accepted external repair's `test_contract.py` was rerun against the actual current helper bodies and passed 16 production-body cases.
It covers permanent/timed/fractional/negative durations, consumed input envelopes, nested cleanup, correct date return, invalid states, eligible recipients, deduplicated registries, exact family removal and missing/current/expired birth bindings with conservative caller-owned temporary frames.
Only native scope/token/modifier/array facts are mocked.
This is source execution of the authored helpers, not native engine observation.

The read-only AI auditor compared all existing condemnation apply/inverse deltas and all 30 file-scoped AI constants with the captured baseline.
Concern watch remains -60/-50/-40 and censure remains -200/-175/-150 for lend-lease/volunteers/access, with exact sign-opposite cleanup.
Arms, strategic, total and pariah authored strategy deltas also retain exact inverses.
Ordinary human and Holy Realm occupation examples keep 1000/1000 raw scores under the declared eligible contaminated/high-resistance/defensive assumptions.
Nonhuman occupiers and nonhuman state holders score 0/0 after the eligibility factors.
The law inspector found no occupation-law adapter, so those results are source-derived scores and do not imply selection probabilities.

The Event 65 pool comparison preserves all 949 ordered rows and weight-one human cases, with each human row at 1/949.
For a nonhuman DHO case, exactly four clinical rows have zero weight and all 945 remaining rows have probability 1/945.
The MCP inventory found the complete pool and confirmed the nonhuman share.
Human/Holy Realm scenarios remained unresolved in that adapter due missing classifier inputs, so their exact conditional shares come from the actual source comparison.
The Event 34 option adapter likewise does not enforce the outer human event trigger and had unresolved affordability/profile inputs, so it was not used as nonhuman admission proof.
No campaign firing probability, cumulative AI timing or native strategy stacking behavior is claimed.

Reference context/search/read succeeded for the modifier contract and offline arguments.
The vanilla MUN Czechoslovakia state application at lines 805-821 provides a native scoped precedent.
Installed add/presence/remove documentation at 1153-1173, 3775-3795 and 5978-5992 provides exact matching country scopes, with ROOT anchored by the installed modifier header at lines 19-26.
Occupation availability and reset scopes were read from installed `common/occupation_laws/occupation_laws.txt` header, effects 7434-7465 and triggers 6918-6935.
The offline token/targeted-flag sections at Data structures 125 and 955-975 support the token and tag-specific receipt API.
The parser repair records exact meta/temporary references and their revisions in its named handoff.
Previous exhausted full-file validator and source-inspector failures were not repeated.
The interrupted narrow occupation/context and scoped-native validation calls produced no completed result and are recorded as unverified attempts, with direct source/reference review used instead.
There is no native gameplay, rendering, multiplayer token-loader, country-transition or combat-area observation in this source closure.
Native coexistence, targeted combat consumption and repeated strategy accumulation remain verification limits, rather than unimplemented alternate mechanics.
No game or push was performed by this C6 owner.

### Publication, dispositions and scope limits

The previously open native attacker and immediate relation items are implemented in the source above.
The broadened inherited-spirit/occupation and post-30 hazard findings are implemented, and their concrete exact gates were rechecked.
The parent owns the central restoration plan and final overall completion claim.
The semantic review is an audit of human harm, health, labour/custody/office pressure and their inherited paths, rather than a redesign or complete revalidation of every political, physical, focus or country package.
No confirmed C6 defect remains at the source boundary and no design fallback, weaker mechanic or requested route omission was introduced.
No simplifications were made.
The preserved physical/bespoke exclusions are the accepted C6 boundary, and all unobserved native results remain explicitly limited above.

The current owned path list, exact baselines, hashes, source check results and commit/index evidence are retained under `.tmp/handoff3/nonhuman/`.
The independent legacy inventory is `.tmp/handoff3/nonhuman/legacy_review/legacy_human_effects.md`.
The first two C6 commits remain unchanged, and this closure is published through the temporary-index/CAS shared Git workflow.
The small generic native-binding skill update is independently committed as `e523ac97e4f505aa0a82a2d399b0701d51446646` in the canonical ideas/modifiers skill.
Skills used for closure are events, subagents, ideas/modifiers, decisions/missions, diplomacy/war, AI strategies, characters/leaders and shared Git commit.
No event-specific context was added to a skill.

### Restored camp mission integration

The later Handoff 3 camp dependency recovery adds synchronous retirement for six restored French and Belgian missions through `camp_rework_retire_nonhuman_country_missions`.
The call follows `chaos_meter_sync_casualty_eligibility_boundary` inside `clear_nonhuman_country_human_systems` and precedes its idempotent cleanup receipt.
It removes the active Gurs review, concession mandate, refugee response, resource quota, transport corridor and strike response missions, including the native consumer-goods modifiers on the first two, without running their normal completion or timeout outcomes.
It explicitly clears private target IDs, pending routes, the settlement commitment and the legacy closure attempt.
The restored actions and delayed helpers retain runtime human eligibility checks, and cancellation retains the original human invalid-target paths.
Source scenarios cover eligible humans, invalid targets, nonhuman conversion, full-administration ownership and repeated cleanup; the decision-file validator passed, while the larger helper files had unresolved coverage rather than a complete validation result.
Installed effects documentation lines 6083–6092 and offline Effects line 1916 establish that country-scoped `remove_mission` skips completion and timeout effects.
No native conversion observation is claimed.
The final source commit and dependency inventory are recorded in [the current restoration audit](systems_restore_audit_2026-10-13.md).
