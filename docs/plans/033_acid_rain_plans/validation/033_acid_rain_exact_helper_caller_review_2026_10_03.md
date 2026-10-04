# Exact state civilian population gateway caller compatibility review

Date: 2026-10-03.
Repository: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Disposition: source audit completed, caller repairs unresolved, MCP reference and event coverage incomplete.
Authority: the parent explicitly requested read-only review of all 213 exact call sites and this report only.
The parent owns helper edits, validation, integration, and commit.
No gameplay source, helper documentation, constants, generators, or Git index were edited by this auditor.

## Findings for the parent

The population-first gateway retains the existing seven temporary input fields and its two temporary output fields.
The existing record-only Deaths branch supports `chaos_deaths_apply_state_pop = 0` with `chaos_deaths_record_state_ledger = 1` in state scope.
The change needs no new API parameter, caller logging-policy switch, reason migration, target redesign, or Fallout regeneration.

The census contains exactly 213 executable `= yes` call sites in 17 script files, with 197 in `fallout_consolidated_effects.txt` and one in each other file.
A broader search across `common`, `events`, `history`, and `interface` found 214 literal source occurrences, comprising those 213 calls and the helper definition.
There are no additional literal direct calls in GUI, GFX, or asset source in that search.
Computed names and external or console invocations are outside the literal census.

Twenty-two callers consume `state_civilian_population_loss_applied` after return.
Ten initialize both public output temporaries locally before the exact helper.
Twelve consume the applied output without initializing its storage at this call boundary.
No caller directly consumes the public `state_civilian_population_loss_result` output in its enclosing named block.
The remaining 191 calls ignore the gateway outputs, including three independent readback paths.
Missing output initialization in an output-ignoring call is not a runtime dependency on the return value.
The helper documentation still asks callers to initialize both public outputs.

All calls execute in an explicit state iterator or pointer block, or in a caller whose documented contract is STATE.
For Fallout, the census has 25 `every_owned_state` calls, one state-registry `for_each_scope_loop` call, three STATE-contract calls, and 168 calls under state-pointer blocks.
These are source scope contracts, not observed runtime pointer validity.
The Migration adapter omits the required population-floor input.
The Famine adapter supplies that input only on its positive-floor branch.
The gateway's missing-input guard resets the whole request to zero, so these paths depend on ambient storage or fail closed.
The assertion that every caller supplies its complete population-floor contract is therefore unsupported for these two adapters.

These caller issues exist in the inspected caller source.
A transaction reorder alone does not establish that it introduced them.
They affect confidence in caller receipt accounting under the documented helper contract and should be resolved or explicitly carried as open risks by the parent before a shared-helper compatibility claim.

## Bounded recommendations, with no patches applied

Initialize the following existing outputs immediately before each of the 12 consumer calls below, inside the exact state call block or its enclosing caller frame.
Preserve all existing inputs, logging flags, reasons, and target attribution.

```txt
set_temp_variable = { state_civilian_population_loss_applied = constant:chaos_meter_deaths.zero }
set_temp_variable = { state_civilian_population_loss_result = constant:chaos_meter_deaths.zero }
apply_exact_state_civilian_population_loss = yes
```

| File | Call line | Enclosing named block and reviewed lines | Receipt consequence |
| --- | --- | --- | --- |
| `020_black_plague_scenario_effects.txt` | 312 | `black_plague_scenario_seed_state`, 245–344 | Opening Deaths total and remaining opening budget use the applied receipt. |
| `029_riches_found_harm_effects.txt` | 43 | `riches_found_apply_harm_record`, 18–97 | Harm total, mass-death gates, and condemnation use the applied receipt. |
| `famine_adapter_effects.txt` | 570 | `famine_apply_related_state_deaths_exact`, 546–578 | Forwards `famine_related_deaths_applied`. |
| `famine_core_effects.txt` | 2633 | `famine_apply_mortality`, 2522–2643 | State totals, result, and condemnation use the applied receipt. |
| `migration_adapter_effects.txt` | 62 | `migration_apply_related_state_deaths_exact`, 39–74 | Forwards `migration_related_deaths_applied`. |
| `fallout_consolidated_effects.txt` | 38622 | `fallout_event_230_apply_movement_shares`, 38573–38644 | Splits observed source loss into movement and Deaths. |
| `fallout_consolidated_effects.txt` | 60174 | `fallout_orientation_record_country_deaths`, 60151–60186 | Accumulates actual loss and decrements a remaining request across a state array. |
| `fallout_consolidated_effects.txt` | 60220 | `fallout_orientation_record_state_deaths`, 60208–60228 | Persists requested and applied outcome receipts. |
| `fallout_consolidated_effects.txt` | 60420 | `fallout_orientation_apply_capital_evacuation`, 60390–60446 | Uses observed loss to cap migration and Deaths. |
| `fallout_consolidated_effects.txt` | 70620 | `fallout_event_100_apply_requisition_failure_deaths`, 70604–70625 | Accumulates the country receipt over owned states. |
| `fallout_consolidated_effects.txt` | 80508 | `fallout_event_243_apply_failure_deaths_and_damage`, 80477–80534 | Persists the receipt before separately registering exact country Deaths. |
| `fallout_consolidated_effects.txt` | 107799 | `fallout_event_499_apply_migration`, 107775–107829 | Uses the receipt for destination credit and migration ledgers. |

Every filename in this table is under `common\scripted_effects\`.
At nested return boundaries, an outer caller must also initialize any forwarded temporary output it consumes, such as `famine_related_deaths_applied`, `migration_related_deaths_applied`, or `famine_mortality_result`.
This audit establishes the immediate exact-helper boundary, and does not certify every transitive wrapper's temporary-output lifetime.

Additional input and cleanup findings:

- `famine_adapter_effects.txt:566–570` sets `state_civilian_population_loss_minimum_remaining` only when `humanitarian_related_deaths_minimum_remaining > 0`.
  Assign the existing floor input unconditionally from the existing owner-provided floor before the call, allowing the gateway's existing clamp to handle it.
  Its wrapper APIs, observed at lines 486–494 in the initial snapshot and shifted to 580–588 in the handoff snapshot, are described as API-only, and the repository search found no gameplay producer using those wrappers.
- `migration_adapter_effects.txt:56–62` never assigns `state_civilian_population_loss_minimum_remaining`.
  Resolve its approved protected floor from existing owner state or tuning and explicitly supply that existing gateway field.
  No new API parameter or guessed zero-floor fallback is proposed.
  `migration_apply_forced_displacement_deaths_exact` at lines 76–79 only supplies the reason and delegates.
- `fallout_consolidated_effects.txt:60214,60221,60414` reads `ROOT.fallout_orientation_state_death_request` or `ROOT.fallout_orientation_migration_total_request` even though each is created with `set_temp_variable` in the same enclosing named block.
  Use the unscoped temporary name for these reads, retaining `ROOT.` on persistent receipt destinations.
  State entry does not scope or rebind a temporary scalar.
  The destination credits at lines 38632 and 60430 also scope temporary `fallout_event_230_population_moved` and `fallout_orientation_migration_movement` through `ROOT`.
  Their bounded correction is to pass `var:fallout_event_230_population_moved` and `var:fallout_orientation_migration_movement` without the scope prefix.
- `020_black_plague_effects.txt:1451` and `fallout_consolidated_effects.txt:4044` read `state_civilian_population_loss_reason` after the helper clears its input to the unknown reason.
  Their famine proof adapters consequently receive the cleared input rather than the original cause.
  Keep the existing gateway cleanup and use the already-known cause constant at those two proof assignments, or capture it in caller-owned storage before the call.
  This is an existing cleanup-contract issue, and the parent reorder retains that cleanup.
- `031_random_terror_effects.txt:388–393` accounts a major-loss achievement from `random_terror_civilian_death_request`, without checking the observed applied amount.
  `fallout_consolidated_effects.txt:94729–94749` in `fallout_event_579_apply_failure_deaths` also stores a requested amount as an applied receipt before the exact call.
  Their recorded amounts can exceed actual removal when a floor or native transaction limits the loss.
  The parent should review receipt semantics with the feature owners rather than treating either request as validation of applied deaths.
- The mixed-prisoner-feeding civilian recorder at `014_cannibalism_effects.txt:7322–7330` uses `apply_state_pop = 0` without explicitly opting into `record_state_ledger = 1`.
  Its global civilian and military records do not double the physical debit, but this path does not independently opt into the state civilian Deaths map ledger.
  The Fallout exact-country recorder similarly deliberately sets `record_state_ledger = 0`.
  This audit reports their existing coverage and does not broaden their ledger policy.

No ownership of concurrent work is inferred from these findings.
A small output-storage repair touches 12 exact calls across six files.
Do not rewrite all 213 calls or regenerate Fallout to address those 12 dependencies.

## Existing helper map and contract

| Helper | Scope | Inputs | Outputs | Side effects and consumer |
| --- | --- | --- | --- | --- |
| `apply_exact_state_civilian_population_loss` | STATE | Seven one-shot temporary fields: requested people, minimum remaining people, reason, log switch, target country, has-target switch, contract-supplied switch. | Caller-owned temporary applied people and success result. | Clamp and round intended debit against the protected floor, physically remove once, read state population difference, optionally record the observed positive amount, clear public inputs. All 213 calls are inventoried below. |
| `apply_state_population_loss_without_recruitable_manpower_gain` | STATE | `state_population_transaction_loss` and one-shot contract flag. | Observed recruitable-manpower reconciliation, used internally. | State `add_manpower` debit plus owner and distinct-controller manpower correction. Invoked once by the exact gateway before readback. |
| `chaos_meter_register_deaths` | Existing shared registrar, STATE for this path | Change, reason, civilian switch, apply-state-pop switch, record-state-ledger switch, target-country fields. | Persistent global Deaths totals, cause/history bookkeeping, shared Chaos effects. | With apply-state-pop zero and record-state-ledger one, enters the state recorder rather than mutating population again. |
| `chaos_meter_record_state_civilian_deaths_from_deaths_change` | STATE | Positive `chaos_deaths_change`. | State civilian Deaths total and global map maximum. | Records the observed loss and refreshes the existing mapmode. Source lines 2813–2835. |

The parent helper source inspected at lines 629–735 already contains the population-first ordering.
The matching documentation at lines 261–299 states the observed-loss output, caller preinitialization requirement, and record-only registration.
The registrar's decisive mutually exclusive branches are at `chaos_meter_effects.txt:2770–2780`.
A zero measured loss leaves both outputs zero and does not register Deaths.
Deaths logging still requires the caller's positive log switch and the existing enabled-ledger or Fallout-policy condition.
A zero caller log switch prevents gateway registration even during Fallout overrides.

The gateway clears its public input temporaries before returning.
It does not create an event target, persist a new variable, or require a new cleanup hook.
Existing regular actor targets retain their chain-local lifecycle.
No constants or tuning tables are added or changed by this audit.
Existing reason constants, people-per-thousand values, protected floors, and logging-policy flags remain authoritative.
No migration into a new helper, central router, or wrapper skill is proposed.

## Independent readback and zero-log ownership

| Exact caller | Log switch | Post-call accounting and compatibility |
| --- | --- | --- |
| `camp_admin_record_deaths`, `camp_administration_effects.txt:613` | 0 | Reads `camp_admin_death_before_k - state_population_k`, reconciles finite detainee rows, then registers that actual loss with apply-state-pop zero and record-state-ledger one at lines 622–630. It does not consume public exact outputs. |
| `camp_occ_record_deaths`, `camp_administration_occupation_effects.txt:848` | 0 | Reads `camp_occ_before_k - state_population_k`, debits the exact active row, then registers positive observed loss with apply-state-pop zero and record-state-ledger one at lines 865–873. It does not consume public exact outputs. |
| `fallout_manual_apply_state_aggregate_consequence`, Fallout line 15217 | 0 | Its named provenance helper at 15238–15268 measures total prestrike-to-posttransaction loss and writes its existing manual/state ledgers. The baseline includes previous native strike loss, so it is not an assertion that gateway-applied equals the total prestrike delta. |
| `cannibalism_consume_current_state`, line 4105 | 1 ordinarily, 0 for prisoner feeding | Uses the preinitialized observed receipt. Prisoner feeding splits that receipt in `cannibalism_log_mixed_prisoner_feeding_deaths`, lines 7315–7341, and registers civilian/military parts with apply-state-pop zero. Keep the zero switch on that context. |
| `air_winter_island_refugee_transfer_population`, Fallout line 5716 | 0 | Uses the initialized observed debit to credit the destination. It represents living movement and does not register Deaths. |
| `fallout_event_230_apply_movement_shares`, Fallout line 38622 | 0 | Splits source loss into destination movement and capped deaths, then calls the exact-country recorder for the death portion only. Requires output-storage repair. |
| `fallout_orientation_record_country_deaths`, Fallout line 60174 | 0 | Accumulates state debits, then records the total once through the country recorder at 60188–60206. Requires output-storage repair. |
| `fallout_orientation_apply_capital_evacuation`, Fallout line 60420 | 0 | Credits movement and registers only its capped death portion once through the country recorder. Requires storage and unscoped-input repairs. |
| `fallout_event_243_apply_failure_deaths_and_damage`, Fallout line 80508 | 0 | Registers its saved observed receipt once through the country recorder. Requires output-storage repair. |
| `fallout_event_499_apply_migration`, Fallout line 107799 | 0 | Credits living arrivals and migration ledgers, without a second Deaths registration in its enclosing block. Requires output-storage repair. |

The exact-country recorder at Fallout lines 60188–60206 has both apply-state-pop and record-state-ledger set to zero.
Its callers therefore have global/country Deaths bookkeeping without a second physical debit, and this audit does not certify matching state-map coverage for those paths.
Changing their exact-helper log switch to one would count movement or duplicate separately owned Deaths.
There are nine unconditional zero-log exact call sites and one conditional zero-log call site.

Acid Rain, `acid_rain_apply_state_pulse` lines 2508–2650, initializes both outputs, records native population before and after, computes an independently clamped observed delta, and flags a mismatch against the returned applied amount.
Its applied receipt drives event totals, positive-receipt arrays, prevented-loss accounting, controller reports, and severe-impact reporting.
The gateway transaction-first order aligns its receipt with this independent readback.
The independent check is source wiring evidence, not a claim that an engine scenario was executed.

## Review method and validation limits

The census used `rg` and an in-memory, read-only Node scan to locate braces while ignoring comments and quoted text.
Each exact call was assigned its complete enclosing named block and scope stack.
Every non-Fallout named block was read directly.
All 197 Fallout calls were inspected through their complete named blocks, including 44 distinct block bodies after substituting only the `fallout_event_<number>` identifier component for comparison.
The substitution was an inspection aid and did not alter a source file.
Distinct scope wrappers, request computations, floor tokens, logging flags, receipt reads, and post-call accounting were retained and reviewed.
Mechanical census and output-lifetime findings were cross-checked against the direct source excerpts.
Broad adjacency output that was truncated was not used as the final evidence for an affected block.

Meaningful source checks performed: exact caller count reconciliation, named-block scope inventory, seven-field input completeness, caller-owned output storage, downstream receipt consumption, independent state readback, zero-log ownership, and registrar branch selection.
No engine, save, or in-game test was run.
No HOI4 launch or log request was made.
The parent's local helper tests run separately and are not claimed here.

The workspace changed during inspection.
`012_africa_gods_effects.txt` changed from SHA-256 `11d2c09a97b5677e04ce1922be216f89211c0af40988fd744f382cc3ab17df50` to the final inventory hash, moving the call from line 2548 to 2536.
`031_random_terror_effects.txt` changed from `9bea6830c2a39395f35bb50ce0aba8b0098326638ab31319790037e5b9faed70` to the final inventory hash while its reviewed exact-call block stayed at lines 378–395.
Both affected named blocks were reread using refreshed bounds.
The other 15 caller files retained their original audited hashes at that refresh.
At the final handoff recheck, `famine_adapter_effects.txt` changed from `b8cf3fa18cff04c04fb3a69cb2c7a8ac86451b0dd1b13ffa8974cba90277a4d9` to `09bf27c2f784bbdcbd1883dfa7192b796ef8e18cad3d622820c131b18145fea0`.
Its exact caller moved from line 476 to 570, and the complete named block was reread at 546–578.
The missing output initialization and conditional floor assignment remain in that block.
The other 16 caller file hashes matched the preceding refreshed inventory at this final recheck.
A commit reviewer must compare the hashes below with the files being committed and reread any changed caller block.

Probability weights, AI selection, focus trees, GUI layout, and map topology were not audited or changed.
Reading the existing state Deaths map refresh does not constitute a map rewrite or topology audit.
No probability result or probability-auditor evidence is claimed.
Native population precision, manpower correction behavior, runtime state-pointer validity, actual Deaths history execution, and transitive wrapper storage remain unproven by this source audit.
Parent fixtures should cover zero transaction, partial removal, exact floor, owner/controller distinction, enabled and disabled logging, Fallout logging overrides, multiple calls with stale ambient temporaries, and a caller-owned output surviving the scripted-effect return.

## MCP evidence and exact gaps

The connected tool list exposes `hoi4.source_lookup`, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.event_inspect`.
The source-lookup live schema accepts symbol, bounds, expected revision, and reference inclusion, but does not expose `view` or `keyPath`.
No server-version or health route for this HOI4 service was exposed in the connected list.
No helper-expansion mode, native task, job route, rewrite, or external MCP installation was used.

Initial narrow requests:

1. `reference_context({surface:"event", question:"scripted effects temporary variable return lifetime and state_population_k add_state_population", limit:2})` returned the exact tool error `timed out awaiting tools/call after 600s`.
2. `source_lookup({symbol:"apply_exact_state_civilian_population_loss", includeReferences:false, maxDefinitions:1, maxLines:25})` returned the exact tool error `timed out awaiting tools/call after 600s`.
3. `reference_search({query:"temporary variables scripted effects", limit:2})` was requested and had not returned evidence when the client wait was ended for handoff.
4. `event_inspect({mode:"state_flow", selector:{eventId:"chaosx.nr33.1"}, stateSubject:"apply_exact_state_civilian_population_loss", maxNodes:2, maxDepth:1})` was requested and had not returned evidence when the client wait was ended for handoff.

Narrow retries were attempted before recording the reference gap:

- `source_lookup({symbol:"chaos_meter_record_state_civilian_deaths_from_deaths_change", includeReferences:false, maxDefinitions:1, maxLines:5})` succeeded for workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `7457b96c48fcb747a68a9859eb2b25f208bb818c36a269c8e71800ec36d9c76e`.
  It returned one unshadowed mod scripted-effect definition at `mod:common/scripted_effects/chaos_meter_effects.txt`, full definition bounds 2813–2835, excerpt 2813–2817, and `nextLine = 2818`.
  `referencesIncluded = false`, `referencesComplete = false`, artifacts empty, and validation checks empty.
  Its `complete = true` is lookup completeness and does not make the five-line excerpt a complete semantic or engine validation.
- The revision-bound continuation for that symbol, `fromLine:2818,maxLines:18`, returned the exact tool error `timed out awaiting tools/call after 600s`.
- `reference_context({surface:"general",question:"set_temp_variable",limit:2})` returned the exact tool error `timed out awaiting tools/call after 600s`.

No reference bundle IDs and revisions were returned for `reference_read` to consume at report preparation.
The remaining reference-search and event-inspection client wait was terminated after the context and source failures and narrow retries.
No server job cancellation or successful completion is claimed for those unanswered requests.
The pertinent local reference sections were therefore read directly and their byte hashes are recorded below.
This is the parent-authorized local-reference fallback for unavailable or unresponsive reference routes.
It does not replace missing event inspection, render, comparison, script-validation, or runtime evidence.
No returned MCP artifact URI, event graph, scenario hash, render, or engine proof was available to archive.

## Caller source revisions and counts

All hashes are SHA-256 over the actual file bytes, rather than normalized text.
The following inventory reflects the refreshed caller snapshot used for the final count and recommendations.

| Ref | Caller source | Exact calls | SHA-256 |
| --- | --- | --- | --- |
| F1 | `common\scripted_effects\012_africa_gods_effects.txt` | 1 | `0f843a91cc6ce294dc2cce699740d9778aa86687b5cd8d6614a4bed09466fa0e` |
| F2 | `common\scripted_effects\014_cannibalism_effects.txt` | 1 | `1751eee6c2a9de6770b6aadae2d6f18010ef84ea85bf17e6003fc4773a2fe302` |
| F3 | `common\scripted_effects\015_utopia_manifesto_decision_effects.txt` | 1 | `53c27e56704dcd44788c94e0a8bc2a13a39fd18fe39a31e8040a4d032731a8b8` |
| F4 | `common\scripted_effects\018_resources_found_incident_effects.txt` | 1 | `47c3c30882d1ca69f95d5c36b1ece91e3b72fe9f792e3df631111e23c036a9e9` |
| F5 | `common\scripted_effects\020_black_plague_effects.txt` | 1 | `6a74a8e8b96abb53957a45af7761e4123696c292e1158ec15516a68326e473d0` |
| F6 | `common\scripted_effects\020_black_plague_evolution_effects.txt` | 1 | `e7e3ac036837616bb0bf38855b3a74f4c9aa2338f917ffcedbd760843cf85c75` |
| F7 | `common\scripted_effects\020_black_plague_scenario_effects.txt` | 1 | `da1af5181b2c7346ef100ba509d8b63531857ac297d4a114968cb1372b64a030` |
| F8 | `common\scripted_effects\028_asteroid_incoming_runtime_effects.txt` | 1 | `0a902614c03d060b159dadba42c706d3c203cb0f448884e7ab10ac4bf2643214` |
| F9 | `common\scripted_effects\029_riches_found_harm_effects.txt` | 1 | `d0046e3a9c0f7d1b5f118e1571fb61ff0697683c647c7ceac492b3215790fc60` |
| F10 | `common\scripted_effects\031_random_terror_effects.txt` | 1 | `8edd15c352b0b4a8143b7a391078b5b6c0a01a41fe64fea73cc86ced7b68b37a` |
| F11 | `common\scripted_effects\033_acid_rain_effects.txt` | 1 | `9bdfb2abfa1a29bea9fdf073026db787e2597295ee7b02aa0fe7f25da1fa8d53` |
| F12 | `common\scripted_effects\camp_administration_effects.txt` | 1 | `0e32bc2e248b96c5f5d58d772fe97ce5134837a439638d567fe46cceae85bad5` |
| F13 | `common\scripted_effects\camp_administration_occupation_effects.txt` | 1 | `bcc7f24795b174d1e53f536f9aa73043760cf65741ee1913da130abbee89fbc5` |
| F14 | `common\scripted_effects\fallout_consolidated_effects.txt` | 197 | `2217d7d893b5d9d476ed7e4645ebb14e3ab7697fd3421b9b8fa85d2e4a0132a6` |
| F15 | `common\scripted_effects\famine_adapter_effects.txt` | 1 | `09bf27c2f784bbdcbd1883dfa7192b796ef8e18cad3d622820c131b18145fea0` |
| F16 | `common\scripted_effects\famine_core_effects.txt` | 1 | `095974659833ac0c8a6d6bc0b40bce34a545754976c83b78cfe1007d97a1025d` |
| F17 | `common\scripted_effects\migration_adapter_effects.txt` | 1 | `37aad37c1b3aa4a31cc24dd6cc0c789b9c0648ff7070acb473c62e890c4d7c7a` |

Additional parent-owned sources:

| Source | SHA-256 |
| --- | --- |
| `common\scripted_effects\chaosx_dynamic_effects.txt` | `8b4db4f595a607d041d0f072de65dd906cdb10c40246690f78d3e4305dab4d49` |
| `common\scripted_effects\chaosx_dynamic_effects.md` | `aaf32beb1adac49dfbb1aefa4afa274571e35b6dbacd4c302da661ea1db0de39` |
| `common\scripted_effects\chaos_meter_effects.txt` | `c00446add013dbac77f73be962328730f4a493c6af61ad3e50ac1ff1f7d96293` |

## Offline and installed reference evidence

The offline wiki was used locally, without a web wiki request.
Installed game root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
The following spans were read for the rules applied here, and their source revisions are represented by the file hashes in the subsequent table.

| Reference | Read spans and design implication |
| --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263–290 and 309–328, event target persistence. 431–470, especially 440–442, temporary-output lifetime and unscoped temporaries. 1682–1693, state population in thousands. |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 3359–3365, state `add_manpower` and recruitable-manpower side effect. 4682–4701, scripted-effect invocation. |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 256–268, ROOT, THIS, PREV, OWNER and CONTROLLER. 528–542, state iterators. |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 570, `has_variable` existence semantics. |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 656–678, scripted localisation inherits its calling scope. No localisation change is proposed. |
| Installed `documentation\effects_documentation.md` | 1468–1476, STATE/COUNTRY `add_manpower`. 7820–7841, temporary assignment accepts values and variables. 6496–6511, regular and global target saves. |
| Installed `documentation\triggers_documentation.md` | 2110–2151, variable comparisons and clamps. 5006–5021, `has_variable`. |
| Installed `documentation\dynamic_variables_documentation.md` | 465–480, manpower in thousands and deprecated plain manpower. 1163–1178, native state population in thousands. |
| Installed `documentation\script_concept_documentation.md` | 216–249, global script constants and explicit support restrictions. |
| Installed `common\script_constants\documentation.md` | 1–84, schema and fixed-point example. |
| Installed `common\scripted_localisation\00_scripted_localisation.txt` | 1–10, documented native text-trigger scope contract. |
| Installed `common\scripted_effects\SAF_german_coup_effects.txt` | 51–80, existing negative manpower debit and country credit pattern. This country-scope precedent does not prove the custom state ledger mechanism. |
| Installed `common\scripted_effects\00_scripted_effects.txt` | 1–35, native helper invocation and state iterator precedent. |

| Reference source | SHA-256 |
| --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md` | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_localisation\00_scripted_localisation.txt` | `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\SAF_german_coup_effects.txt` | `a075a33130685a1987336491da37fd6d9e595e13de2576ecab51aff3a6727959` |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\00_scripted_effects.txt` | `93ddd0d2e9f7a1a5640cfdafbae6b9ff0e1b4ee57e829c81d13b0cac23ad90bf` |

## Non-Fallout named-block census

The enclosing block range and complete scope path were inspected, rather than assuming the scope from adjacent lines.
The table uses the latest line bounds from the refreshed inventory.

| Named caller | Exact source and line | Named block span | Nested scope path | Output contract |
| --- | --- | --- | --- | --- |
| `gods_of_africa_apply_population_wave` | `common\scripted_effects\012_africa_gods_effects.txt`:2536 | 2517–2544 | `if / random_owned_controlled_state` | both outputs initialized, applied consumed |
| `cannibalism_consume_current_state` | `common\scripted_effects\014_cannibalism_effects.txt`:4105 | 4002–4225 | `if / else` | both outputs initialized, applied consumed |
| `utopia_manifesto_apply_penal_works_loss_to_active_district` | `common\scripted_effects\015_utopia_manifesto_decision_effects.txt`:915 | 895–924 | `if / var:utopia_manifesto_penal_works_project_state` | both outputs initialized, applied consumed |
| `resources_found_apply_incident_civilian_loss` | `common\scripted_effects\018_resources_found_incident_effects.txt`:48 | 13–56 | `caller STATE` | both outputs initialized, applied consumed |
| `black_plague_apply_current_state_mortality_once` | `common\scripted_effects\020_black_plague_effects.txt`:1428 | 1333–1468 | `if` | both outputs initialized, applied consumed |
| `black_plague_apply_terminal_takeover_loss_once` | `common\scripted_effects\020_black_plague_evolution_effects.txt`:850 | 829–858 | `if` | both outputs initialized, applied consumed |
| `black_plague_scenario_seed_state` | `common\scripted_effects\020_black_plague_scenario_effects.txt`:312 | 245–344 | `if` | applied consumed, storage missing |
| `asteroid_incoming_apply_monthly_rescue_deaths` | `common\scripted_effects\028_asteroid_incoming_runtime_effects.txt`:1115 | 1084–1134 | `if` | outputs ignored |
| `riches_found_apply_harm_record` | `common\scripted_effects\029_riches_found_harm_effects.txt`:43 | 18–97 | `if` | applied consumed, storage missing |
| `random_terror_apply_exact_state_loss` | `common\scripted_effects\031_random_terror_effects.txt`:386 | 378–395 | `caller STATE` | outputs ignored |
| `acid_rain_apply_state_pulse` | `common\scripted_effects\033_acid_rain_effects.txt`:2538 | 2508–2650 | `if` | both outputs initialized, applied consumed |
| `camp_admin_record_deaths` | `common\scripted_effects\camp_administration_effects.txt`:613 | 574–655 | `if / if` | outputs ignored |
| `camp_occ_record_deaths` | `common\scripted_effects\camp_administration_occupation_effects.txt`:848 | 810–897 | `if` | outputs ignored |
| `famine_apply_related_state_deaths_exact` | `common\scripted_effects\famine_adapter_effects.txt`:570 | 546–578 | `if` | applied consumed, storage missing |
| `famine_apply_mortality` | `common\scripted_effects\famine_core_effects.txt`:2633 | 2522–2643 | `if / if / if` | applied consumed, storage missing |
| `migration_apply_related_state_deaths_exact` | `common\scripted_effects\migration_adapter_effects.txt`:62 | 39–74 | `if` | applied consumed, storage missing |

The floor assignments in these blocks preserve subsystem-owned constants and computed floors.
Camp floors are converted from thousands into people.
The occupation floor additionally protects existing camp detainees.
Black Plague scenario seeding computes a proportional floor in people.
Core Famine computes a proportional floor with its existing minimum before handing it to the exact helper.
Migration's missing floor and the conditional Famine-adapter floor are the exceptions described above.

## All 197 Fallout call sites

Every row refers to `common\scripted_effects\fallout_consolidated_effects.txt` at the inventory hash above.
P means both public outputs are locally initialized and applied is consumed.
D means applied is consumed without local preinitialization.
I means the exact outputs are ignored.
Log is the exact gateway's caller switch, not whether later independent accounting exists.

| Call line | Named caller | Complete named block span | State entry path, excluding control-flow wrappers | Output class | Log |
| --- | --- | --- | --- | --- | --- |
| 4030 | `air_winter_apply_state_population_loss` | 3948–4062 | `caller STATE` | P | 1 |
| 5146 | `air_winter_event_apply_deaths` | 5127–5154 | `caller STATE` | P | 1 |
| 5716 | `air_winter_island_refugee_transfer_population` | 5692–5751 | `var:air_winter_island_refugee_offer_source_state` | P | 0 |
| 15217 | `fallout_manual_apply_state_aggregate_consequence` | 15167–15231 | `caller STATE` | I | 0 |
| 20693 | `fallout_event_908_apply_failure_deaths` | 20678–20697 | `var:fallout_event_908_target_state_id` | I | 1 |
| 20714 | `fallout_event_908_apply_callback_failure_deaths` | 20699–20718 | `var:fallout_event_908_target_state_id` | I | 1 |
| 21487 | `fallout_event_534_apply_failure_deaths` | 21472–21491 | `var:fallout_event_534_target_state_id` | I | 1 |
| 21508 | `fallout_event_534_apply_callback_failure_deaths` | 21493–21512 | `var:fallout_event_534_target_state_id` | I | 1 |
| 22081 | `fallout_event_164_apply_failure_deaths` | 22063–22084 | `var:fallout_event_164_result_state_id` | I | 1 |
| 22623 | `fallout_event_450_apply_failure_deaths` | 22608–22627 | `var:fallout_event_450_target_state_id` | I | 1 |
| 22644 | `fallout_event_450_apply_callback_failure_deaths` | 22629–22648 | `var:fallout_event_450_target_state_id` | I | 1 |
| 23176 | `fallout_event_554_apply_failure_deaths` | 23161–23180 | `var:fallout_event_554_target_state_id` | I | 1 |
| 23197 | `fallout_event_554_apply_callback_failure_deaths` | 23182–23201 | `var:fallout_event_554_target_state_id` | I | 1 |
| 23850 | `fallout_event_204_apply_failure_deaths` | 23832–23853 | `var:fallout_event_204_result_state_id` | I | 1 |
| 24610 | `fallout_event_310_apply_failure_deaths` | 24595–24614 | `every_owned_state` | I | 1 |
| 24631 | `fallout_event_310_apply_callback_failure_deaths` | 24616–24635 | `every_owned_state` | I | 1 |
| 25494 | `fallout_event_726_apply_failure_deaths` | 25479–25498 | `var:fallout_event_726_target_state_id` | I | 1 |
| 25515 | `fallout_event_726_apply_callback_failure_deaths` | 25500–25519 | `var:fallout_event_726_target_state_id` | I | 1 |
| 26281 | `fallout_event_464_apply_failure_deaths` | 26266–26285 | `var:fallout_event_464_target_state_id` | I | 1 |
| 26303 | `fallout_event_464_apply_callback_failure_deaths` | 26287–26307 | `var:fallout_event_464_target_state_id` | I | 1 |
| 27111 | `fallout_event_628_apply_failure_deaths` | 27096–27115 | `var:fallout_event_628_target_state_id` | I | 1 |
| 27132 | `fallout_event_628_apply_callback_failure_deaths` | 27117–27136 | `var:fallout_event_628_target_state_id` | I | 1 |
| 27871 | `fallout_event_520_apply_failure_deaths` | 27856–27875 | `var:fallout_event_520_target_state_id` | I | 1 |
| 27892 | `fallout_event_520_apply_callback_failure_deaths` | 27877–27896 | `var:fallout_event_520_target_state_id` | I | 1 |
| 28682 | `fallout_event_768_apply_failure_deaths` | 28667–28686 | `var:fallout_event_768_target_state_id` | I | 1 |
| 28703 | `fallout_event_768_apply_callback_failure_deaths` | 28688–28707 | `var:fallout_event_768_target_state_id` | I | 1 |
| 29467 | `fallout_event_436_apply_failure_deaths` | 29452–29471 | `var:fallout_event_436_target_state_id` | I | 1 |
| 29488 | `fallout_event_436_apply_callback_failure_deaths` | 29473–29492 | `var:fallout_event_436_target_state_id` | I | 1 |
| 29909 | `fallout_event_733_apply_failure_deaths` | 29894–29913 | `every_owned_state` | I | 1 |
| 29930 | `fallout_event_733_apply_callback_failure_deaths` | 29915–29934 | `every_owned_state` | I | 1 |
| 30965 | `fallout_event_915_apply_failure_deaths` | 30950–30969 | `var:fallout_event_915_target_state_id` | I | 1 |
| 30986 | `fallout_event_915_apply_callback_failure_deaths` | 30971–30990 | `var:fallout_event_915_target_state_id` | I | 1 |
| 31955 | `fallout_event_719_apply_failure_deaths` | 31940–31959 | `var:fallout_event_719_target_state_id` | I | 1 |
| 31976 | `fallout_event_719_apply_callback_failure_deaths` | 31961–31980 | `var:fallout_event_719_target_state_id` | I | 1 |
| 32947 | `fallout_event_880_apply_failure_deaths` | 32932–32951 | `var:fallout_event_880_target_state_id` | I | 1 |
| 32968 | `fallout_event_880_apply_callback_failure_deaths` | 32953–32972 | `var:fallout_event_880_target_state_id` | I | 1 |
| 33982 | `fallout_event_922_apply_failure_deaths` | 33967–33986 | `var:fallout_event_922_target_state_id` | I | 1 |
| 34003 | `fallout_event_922_apply_callback_failure_deaths` | 33988–34007 | `var:fallout_event_922_target_state_id` | I | 1 |
| 34776 | `fallout_event_387_apply_failure_deaths` | 34761–34780 | `var:fallout_event_387_target_state_id` | I | 1 |
| 34797 | `fallout_event_387_apply_callback_failure_deaths` | 34782–34801 | `var:fallout_event_387_target_state_id` | I | 1 |
| 35771 | `fallout_event_572_apply_failure_deaths` | 35756–35775 | `var:fallout_event_572_target_state_id` | I | 1 |
| 35792 | `fallout_event_572_apply_callback_failure_deaths` | 35777–35796 | `var:fallout_event_572_target_state_id` | I | 1 |
| 36262 | `fallout_event_338_apply_failure_deaths` | 36247–36266 | `var:fallout_event_338_target_state_id` | I | 1 |
| 36283 | `fallout_event_338_apply_callback_failure_deaths` | 36268–36287 | `var:fallout_event_338_target_state_id` | I | 1 |
| 36747 | `fallout_event_485_apply_failure_deaths` | 36732–36751 | `var:fallout_event_485_target_state_id` | I | 1 |
| 36768 | `fallout_event_485_apply_callback_failure_deaths` | 36753–36772 | `var:fallout_event_485_target_state_id` | I | 1 |
| 37475 | `fallout_event_705_apply_failure_deaths` | 37460–37479 | `var:fallout_event_705_target_state_id` | I | 1 |
| 37496 | `fallout_event_705_apply_callback_failure_deaths` | 37481–37500 | `var:fallout_event_705_target_state_id` | I | 1 |
| 38622 | `fallout_event_230_apply_movement_shares` | 38573–38644 | `var:fallout_event_230_source_state_id` | D | 0 |
| 44919 | `fallout_event_443_apply_failure_deaths` | 44904–44923 | `var:fallout_event_443_target_state_id` | I | 1 |
| 44940 | `fallout_event_443_apply_callback_failure_deaths` | 44925–44944 | `var:fallout_event_443_target_state_id` | I | 1 |
| 45404 | `fallout_event_296_apply_failure_deaths` | 45389–45408 | `every_owned_state` | I | 1 |
| 45425 | `fallout_event_296_apply_callback_failure_deaths` | 45410–45429 | `every_owned_state` | I | 1 |
| 46493 | `fallout_event_796_apply_failure_deaths` | 46478–46497 | `var:fallout_event_796_target_state_id` | I | 1 |
| 46514 | `fallout_event_796_apply_callback_failure_deaths` | 46499–46518 | `var:fallout_event_796_target_state_id` | I | 1 |
| 60174 | `fallout_orientation_record_country_deaths` | 60151–60186 | `for_each_scope_loop` | D | 0 |
| 60220 | `fallout_orientation_record_state_deaths` | 60208–60228 | `var:fallout_orientation_state_target` | D | 1 |
| 60420 | `fallout_orientation_apply_capital_evacuation` | 60390–60446 | `var:fallout_orientation_state_target` | D | 0 |
| 61290 | `fallout_event_831_apply_failure_deaths` | 61275–61294 | `var:fallout_event_831_target_state_id` | I | 1 |
| 61311 | `fallout_event_831_apply_callback_failure_deaths` | 61296–61315 | `var:fallout_event_831_target_state_id` | I | 1 |
| 62290 | `fallout_event_691_apply_failure_deaths` | 62275–62294 | `var:fallout_event_691_target_state_id` | I | 1 |
| 62311 | `fallout_event_691_apply_callback_failure_deaths` | 62296–62315 | `var:fallout_event_691_target_state_id` | I | 1 |
| 63009 | `fallout_event_478_apply_failure_deaths` | 62994–63013 | `var:fallout_event_478_target_state_id` | I | 1 |
| 63030 | `fallout_event_478_apply_callback_failure_deaths` | 63015–63034 | `var:fallout_event_478_target_state_id` | I | 1 |
| 63943 | `fallout_event_894_apply_failure_deaths` | 63928–63947 | `var:fallout_event_894_target_state_id` | I | 1 |
| 63964 | `fallout_event_894_apply_callback_failure_deaths` | 63949–63968 | `var:fallout_event_894_target_state_id` | I | 1 |
| 64742 | `fallout_event_256_apply_failure_deaths` | 64724–64745 | `var:fallout_event_256_result_state_id` | I | 1 |
| 65523 | `fallout_event_217_apply_failure_deaths` | 65505–65526 | `var:fallout_event_217_result_state_id` | I | 1 |
| 66745 | `fallout_event_684_apply_failure_deaths` | 66728–66750 | `var:fallout_event_684_target_state_id` | I | 1 |
| 67722 | `fallout_event_852_apply_failure_deaths` | 67707–67726 | `var:fallout_event_852_target_state_id` | I | 1 |
| 67743 | `fallout_event_852_apply_callback_failure_deaths` | 67728–67747 | `var:fallout_event_852_target_state_id` | I | 1 |
| 68533 | `fallout_event_282_apply_failure_deaths` | 68518–68537 | `every_owned_state` | I | 1 |
| 68554 | `fallout_event_282_apply_callback_failure_deaths` | 68539–68558 | `every_owned_state` | I | 1 |
| 69308 | `fallout_event_317_apply_failure_deaths` | 69293–69312 | `every_owned_state` | I | 1 |
| 69329 | `fallout_event_317_apply_callback_failure_deaths` | 69314–69333 | `every_owned_state` | I | 1 |
| 69966 | `fallout_event_471_apply_failure_deaths` | 69951–69970 | `var:fallout_event_471_target_state_id` | I | 1 |
| 69988 | `fallout_event_471_apply_callback_failure_deaths` | 69972–69992 | `var:fallout_event_471_target_state_id` | I | 1 |
| 70620 | `fallout_event_100_apply_requisition_failure_deaths` | 70604–70625 | `every_owned_state` | D | 1 |
| 72175 | `fallout_event_775_apply_failure_deaths` | 72160–72179 | `var:fallout_event_775_target_state_id` | I | 1 |
| 72196 | `fallout_event_775_apply_callback_failure_deaths` | 72181–72200 | `var:fallout_event_775_target_state_id` | I | 1 |
| 73095 | `fallout_event_663_apply_failure_deaths` | 73080–73099 | `var:fallout_event_663_target_state_id` | I | 1 |
| 73116 | `fallout_event_663_apply_callback_failure_deaths` | 73101–73120 | `var:fallout_event_663_target_state_id` | I | 1 |
| 74396 | `fallout_event_824_apply_failure_deaths` | 74381–74400 | `var:fallout_event_824_target_state_id` | I | 1 |
| 74417 | `fallout_event_824_apply_callback_failure_deaths` | 74402–74421 | `var:fallout_event_824_target_state_id` | I | 1 |
| 75444 | `fallout_event_782_apply_failure_deaths` | 75429–75448 | `var:fallout_event_782_target_state_id` | I | 1 |
| 75465 | `fallout_event_782_apply_callback_failure_deaths` | 75450–75469 | `var:fallout_event_782_target_state_id` | I | 1 |
| 76542 | `fallout_event_747_apply_failure_deaths` | 76527–76546 | `var:fallout_event_747_target_state_id` | I | 1 |
| 76563 | `fallout_event_747_apply_callback_failure_deaths` | 76548–76567 | `var:fallout_event_747_target_state_id` | I | 1 |
| 77152 | `fallout_event_677_apply_failure_deaths` | 77121–77156 | `var:fallout_event_677_result_state_id` | I | 1 |
| 77176 | `fallout_event_677_apply_callback_failure_deaths` | 77158–77179 | `var:fallout_event_677_result_state_id` | I | 1 |
| 78485 | `fallout_event_492_apply_failure_deaths` | 78470–78489 | `var:fallout_event_492_target_state_id` | I | 1 |
| 78505 | `fallout_event_492_apply_callback_failure_deaths` | 78490–78509 | `var:fallout_event_492_target_state_id` | I | 1 |
| 79279 | `fallout_event_838_apply_failure_deaths` | 79264–79283 | `var:fallout_event_838_target_state_id` | I | 1 |
| 79300 | `fallout_event_838_apply_callback_failure_deaths` | 79285–79304 | `var:fallout_event_838_target_state_id` | I | 1 |
| 80508 | `fallout_event_243_apply_failure_deaths_and_damage` | 80477–80534 | `var:fallout_event_243_transformer_state_id` | D | 0 |
| 81290 | `fallout_event_803_apply_failure_deaths` | 81275–81294 | `var:fallout_event_803_target_state_id` | I | 1 |
| 81311 | `fallout_event_803_apply_callback_failure_deaths` | 81296–81315 | `var:fallout_event_803_target_state_id` | I | 1 |
| 82310 | `fallout_event_845_apply_failure_deaths` | 82295–82314 | `var:fallout_event_845_target_state_id` | I | 1 |
| 82331 | `fallout_event_845_apply_callback_failure_deaths` | 82316–82335 | `var:fallout_event_845_target_state_id` | I | 1 |
| 83119 | `fallout_event_345_apply_failure_deaths` | 83104–83123 | `var:fallout_event_345_target_state_id` | I | 1 |
| 83140 | `fallout_event_345_apply_callback_failure_deaths` | 83125–83144 | `var:fallout_event_345_target_state_id` | I | 1 |
| 83575 | `fallout_event_380_apply_failure_deaths` | 83560–83579 | `var:fallout_event_380_target_state_id` | I | 1 |
| 83596 | `fallout_event_380_apply_callback_failure_deaths` | 83581–83600 | `var:fallout_event_380_target_state_id` | I | 1 |
| 84122 | `fallout_event_506_apply_failure_deaths` | 84107–84126 | `var:fallout_event_506_target_state_id` | I | 1 |
| 84143 | `fallout_event_506_apply_callback_failure_deaths` | 84128–84147 | `var:fallout_event_506_target_state_id` | I | 1 |
| 84943 | `fallout_event_614_apply_failure_deaths` | 84928–84947 | `var:fallout_event_614_target_state_id` | I | 1 |
| 84964 | `fallout_event_614_apply_callback_failure_deaths` | 84949–84968 | `var:fallout_event_614_target_state_id` | I | 1 |
| 85922 | `fallout_event_642_apply_failure_deaths` | 85907–85926 | `var:fallout_event_642_target_state_id` | I | 1 |
| 85943 | `fallout_event_642_apply_callback_failure_deaths` | 85928–85947 | `var:fallout_event_642_target_state_id` | I | 1 |
| 86757 | `fallout_event_527_apply_failure_deaths` | 86742–86761 | `var:fallout_event_527_target_state_id` | I | 1 |
| 86778 | `fallout_event_527_apply_callback_failure_deaths` | 86763–86782 | `var:fallout_event_527_target_state_id` | I | 1 |
| 87587 | `fallout_event_887_apply_failure_deaths` | 87572–87591 | `var:fallout_event_887_target_state_id` | I | 1 |
| 87608 | `fallout_event_887_apply_callback_failure_deaths` | 87593–87612 | `var:fallout_event_887_target_state_id` | I | 1 |
| 88658 | `fallout_event_635_apply_failure_deaths` | 88643–88662 | `var:fallout_event_635_target_state_id` | I | 1 |
| 88679 | `fallout_event_635_apply_callback_failure_deaths` | 88664–88683 | `var:fallout_event_635_target_state_id` | I | 1 |
| 89777 | `fallout_event_761_apply_failure_deaths` | 89762–89781 | `var:fallout_event_761_target_state_id` | I | 1 |
| 89798 | `fallout_event_761_apply_callback_failure_deaths` | 89783–89802 | `var:fallout_event_761_target_state_id` | I | 1 |
| 90801 | `fallout_event_873_apply_failure_deaths` | 90786–90805 | `var:fallout_event_873_target_state_id` | I | 1 |
| 90822 | `fallout_event_873_apply_callback_failure_deaths` | 90807–90826 | `var:fallout_event_873_target_state_id` | I | 1 |
| 91589 | `fallout_event_269_apply_failure_deaths` | 91574–91593 | `every_owned_state` | I | 1 |
| 91610 | `fallout_event_269_apply_callback_failure_deaths` | 91595–91614 | `every_owned_state` | I | 1 |
| 92396 | `fallout_event_541_apply_failure_deaths` | 92381–92400 | `every_owned_state` | I | 1 |
| 92417 | `fallout_event_541_apply_callback_failure_deaths` | 92402–92421 | `every_owned_state` | I | 1 |
| 93370 | `fallout_event_649_apply_failure_deaths` | 93355–93374 | `every_owned_state` | I | 1 |
| 93391 | `fallout_event_649_apply_callback_failure_deaths` | 93376–93395 | `every_owned_state` | I | 1 |
| 94745 | `fallout_event_579_apply_failure_deaths` | 94729–94749 | `var:fallout_event_579_target_state_id` | I | 1 |
| 94766 | `fallout_event_579_apply_callback_failure_deaths` | 94751–94770 | `var:fallout_event_579_target_state_id` | I | 1 |
| 95764 | `fallout_event_586_apply_failure_deaths` | 95749–95768 | `var:fallout_event_586_target_state_id` | I | 1 |
| 95785 | `fallout_event_586_apply_callback_failure_deaths` | 95770–95789 | `var:fallout_event_586_target_state_id` | I | 1 |
| 96575 | `fallout_event_901_apply_failure_deaths` | 96560–96579 | `var:fallout_event_901_target_state_id` | I | 1 |
| 96596 | `fallout_event_901_apply_callback_failure_deaths` | 96581–96600 | `var:fallout_event_901_target_state_id` | I | 1 |
| 97369 | `fallout_event_373_apply_failure_deaths` | 97354–97373 | `var:fallout_event_373_target_state_id` | I | 1 |
| 97390 | `fallout_event_373_apply_callback_failure_deaths` | 97375–97394 | `var:fallout_event_373_target_state_id` | I | 1 |
| 98228 | `fallout_event_740_apply_failure_deaths` | 98213–98232 | `var:fallout_event_740_target_state_id` | I | 1 |
| 98249 | `fallout_event_740_apply_callback_failure_deaths` | 98234–98253 | `var:fallout_event_740_target_state_id` | I | 1 |
| 98821 | `fallout_event_408_apply_failure_deaths` | 98806–98825 | `var:fallout_event_408_target_state_id` | I | 1 |
| 98842 | `fallout_event_408_apply_callback_failure_deaths` | 98827–98846 | `var:fallout_event_408_target_state_id` | I | 1 |
| 99810 | `fallout_event_817_apply_failure_deaths` | 99795–99814 | `var:fallout_event_817_target_state_id` | I | 1 |
| 99831 | `fallout_event_817_apply_callback_failure_deaths` | 99816–99835 | `var:fallout_event_817_target_state_id` | I | 1 |
| 100811 | `fallout_event_698_apply_failure_deaths` | 100796–100815 | `var:fallout_event_698_target_state_id` | I | 1 |
| 100832 | `fallout_event_698_apply_callback_failure_deaths` | 100817–100836 | `var:fallout_event_698_target_state_id` | I | 1 |
| 101765 | `fallout_event_789_apply_failure_deaths` | 101750–101769 | `var:fallout_event_789_target_state_id` | I | 1 |
| 101786 | `fallout_event_789_apply_callback_failure_deaths` | 101771–101790 | `var:fallout_event_789_target_state_id` | I | 1 |
| 102785 | `fallout_event_866_apply_failure_deaths` | 102770–102789 | `var:fallout_event_866_target_state_id` | I | 1 |
| 102806 | `fallout_event_866_apply_callback_failure_deaths` | 102791–102810 | `var:fallout_event_866_target_state_id` | I | 1 |
| 103835 | `fallout_event_929_apply_failure_deaths` | 103820–103839 | `var:fallout_event_929_target_state_id` | I | 1 |
| 103856 | `fallout_event_929_apply_callback_failure_deaths` | 103841–103860 | `var:fallout_event_929_target_state_id` | I | 1 |
| 104629 | `fallout_event_600_apply_failure_deaths` | 104614–104633 | `var:fallout_event_600_target_state_id` | I | 1 |
| 104650 | `fallout_event_600_apply_callback_failure_deaths` | 104635–104654 | `var:fallout_event_600_target_state_id` | I | 1 |
| 105390 | `fallout_event_114_apply_deaths` | 105355–105395 | `var:fallout_event_114_result_state_id` | I | 1 |
| 106377 | `fallout_event_621_apply_failure_deaths` | 106362–106381 | `var:fallout_event_621_target_state_id` | I | 1 |
| 106398 | `fallout_event_621_apply_callback_failure_deaths` | 106383–106402 | `var:fallout_event_621_target_state_id` | I | 1 |
| 107081 | `fallout_event_394_apply_failure_deaths` | 107066–107085 | `var:fallout_event_394_target_state_id` | I | 1 |
| 107579 | `fallout_event_499_apply_failure_deaths` | 107564–107583 | `var:fallout_event_499_target_state_id` | I | 1 |
| 107600 | `fallout_event_499_apply_callback_failure_deaths` | 107585–107604 | `var:fallout_event_499_target_state_id` | I | 1 |
| 107799 | `fallout_event_499_apply_migration` | 107775–107829 | `var:fallout_event_499_origin_state_id` | D | 0 |
| 108520 | `fallout_event_810_apply_failure_deaths` | 108505–108524 | `var:fallout_event_810_target_state_id` | I | 1 |
| 108541 | `fallout_event_810_apply_callback_failure_deaths` | 108526–108545 | `var:fallout_event_810_target_state_id` | I | 1 |
| 109304 | `fallout_event_366_apply_failure_deaths` | 109289–109308 | `var:fallout_event_366_target_state_id` | I | 1 |
| 109325 | `fallout_event_366_apply_callback_failure_deaths` | 109310–109329 | `var:fallout_event_366_target_state_id` | I | 1 |
| 109805 | `fallout_event_415_apply_failure_deaths` | 109790–109809 | `var:fallout_event_415_target_state_id` | I | 1 |
| 110989 | `fallout_event_754_apply_failure_deaths` | 110974–110993 | `var:fallout_event_754_target_state_id` | I | 1 |
| 111010 | `fallout_event_754_apply_callback_failure_deaths` | 110995–111014 | `var:fallout_event_754_target_state_id` | I | 1 |
| 112009 | `fallout_event_859_apply_failure_deaths` | 111994–112013 | `var:fallout_event_859_target_state_id` | I | 1 |
| 112030 | `fallout_event_859_apply_callback_failure_deaths` | 112015–112034 | `var:fallout_event_859_target_state_id` | I | 1 |
| 113009 | `fallout_event_712_apply_failure_deaths` | 112994–113013 | `var:fallout_event_712_target_state_id` | I | 1 |
| 113030 | `fallout_event_712_apply_callback_failure_deaths` | 113015–113034 | `var:fallout_event_712_target_state_id` | I | 1 |
| 114825 | `fallout_event_289_apply_failure_deaths` | 114810–114829 | `every_owned_state` | I | 1 |
| 114846 | `fallout_event_289_apply_callback_failure_deaths` | 114831–114850 | `every_owned_state` | I | 1 |
| 115628 | `fallout_event_331_apply_failure_deaths` | 115613–115632 | `every_owned_state` | I | 1 |
| 115649 | `fallout_event_331_apply_callback_failure_deaths` | 115634–115653 | `every_owned_state` | I | 1 |
| 116558 | `fallout_event_656_apply_failure_deaths` | 116543–116562 | `var:fallout_event_656_target_state_id` | I | 1 |
| 116579 | `fallout_event_656_apply_callback_failure_deaths` | 116564–116583 | `var:fallout_event_656_target_state_id` | I | 1 |
| 117612 | `fallout_event_188_apply_failure_deaths` | 117594–117615 | `var:fallout_event_188_result_state_id` | I | 1 |
| 118081 | `fallout_event_303_apply_failure_deaths` | 118066–118085 | `every_owned_state` | I | 1 |
| 118102 | `fallout_event_303_apply_callback_failure_deaths` | 118087–118106 | `every_owned_state` | I | 1 |
| 118877 | `fallout_event_422_apply_failure_deaths` | 118862–118881 | `var:fallout_event_422_target_state_id` | I | 1 |
| 119432 | `fallout_event_429_apply_failure_deaths` | 119417–119436 | `var:fallout_event_429_target_state_id` | I | 1 |
| 119453 | `fallout_event_429_apply_callback_failure_deaths` | 119438–119457 | `var:fallout_event_429_target_state_id` | I | 1 |
| 120549 | `fallout_event_457_apply_failure_deaths` | 120534–120553 | `var:fallout_event_457_target_state_id` | I | 1 |
| 120571 | `fallout_event_457_apply_callback_failure_deaths` | 120555–120575 | `var:fallout_event_457_target_state_id` | I | 1 |
| 121128 | `fallout_event_175_apply_failure_deaths` | 121110–121131 | `var:fallout_event_175_result_state_id` | I | 1 |
| 122209 | `fallout_event_607_apply_failure_deaths` | 122194–122213 | `var:fallout_event_607_target_state_id` | I | 1 |
| 122230 | `fallout_event_607_apply_callback_failure_deaths` | 122215–122234 | `var:fallout_event_607_target_state_id` | I | 1 |
| 122674 | `fallout_event_359_apply_failure_deaths` | 122659–122678 | `var:fallout_event_359_target_state_id` | I | 1 |
| 122695 | `fallout_event_359_apply_callback_failure_deaths` | 122680–122699 | `var:fallout_event_359_target_state_id` | I | 1 |
| 123183 | `fallout_event_107_apply_failure_deaths` | 123165–123186 | `var:fallout_event_107_result_state_id` | I | 1 |
| 123797 | `fallout_event_513_apply_failure_deaths` | 123782–123801 | `var:fallout_event_513_target_state_id` | I | 1 |
| 123818 | `fallout_event_513_apply_callback_failure_deaths` | 123803–123822 | `var:fallout_event_513_target_state_id` | I | 1 |
| 124308 | `fallout_event_153_apply_failure_deaths` | 124290–124311 | `var:fallout_event_153_result_state_id` | I | 1 |
| 124861 | `fallout_event_670_apply_failure_deaths` | 124843–124864 | `var:fallout_event_670_result_state_id` | I | 1 |
| 124884 | `fallout_event_670_apply_callback_failure_deaths` | 124866–124887 | `var:fallout_event_670_result_state_id` | I | 1 |
| 125975 | `fallout_event_324_apply_failure_deaths` | 125960–125979 | `every_owned_state` | I | 1 |
| 125996 | `fallout_event_324_apply_callback_failure_deaths` | 125981–126000 | `every_owned_state` | I | 1 |
| 126601 | `fallout_event_352_apply_failure_deaths` | 126586–126605 | `var:fallout_event_352_target_state_id` | I | 1 |
| 126622 | `fallout_event_352_apply_callback_failure_deaths` | 126607–126626 | `var:fallout_event_352_target_state_id` | I | 1 |
| 127102 | `fallout_event_401_apply_failure_deaths` | 127087–127106 | `var:fallout_event_401_target_state_id` | I | 1 |

## Handoff status

Completed: 213-call source census, containing-block and state-scope review, immediate input/output compatibility review, independent readback review, zero-log Deaths ownership review, local wiki and installed-documentation evidence, source hashes, and bounded recommendations.
Changed file: this report only.
Helper documentation, direct gameplay call sites, constants, and cleanup logic changed by this auditor: none.
Skipped meaningful validation: executed engine population transactions, event MCP coverage, matched event render/compare, and runtime temporary lifetime, because this assignment is read-only and the required MCP requests did not supply that evidence.
Blocked or unresolved: MCP reference/event coverage, 12 immediate output-storage gaps, the two floor-input paths, scoped temporary input reads, cleared-cause proof reads, and owner review of request-based receipts and existing ledger coverage.
No gameplay simplification, Fallout regeneration, source patch, or commit was performed.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
