# C6 nonhuman human-system boundaries, 13 October 2026

## Current conclusion

C6 is partial and must not be marked complete.
The safe source changes below protect country and state entry boundaries, direct chemical unit damage, civilian population loss and inherited human modifiers.
Native state combat modifiers with `attacker_modifier = yes` still affect nonhuman attackers fighting into eligible human-held states.
Installed documentation exposes that setting as a fixed boolean without a per-unit country filter.
Replacing human suppression with another mechanic would require a design decision and is outside this narrow repair.

The reviewed C6 boundary repairs are committed, while the absolute requirement remains partial.
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

Broader country setup, every national spirit in every event, every occupation-law modifier, and all post-30 legacy event designs were not semantically audited in this bounded pass.
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

## Simplifications, omissions and blockers

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
