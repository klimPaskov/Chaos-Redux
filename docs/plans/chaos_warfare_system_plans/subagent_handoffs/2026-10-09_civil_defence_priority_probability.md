# Civil Defence relevance and automatic mask-priority source comparison

Status: source-derived after comparison is complete for the fourteen frozen named cases. The probability adapter discovered no weighted surface; results establish script predicates and AI strategy enable-gates only, not native engine rates or odds.

This read-only audit covers current Civil Defence relevance, automatic stock distribution, and the three named helpers `cbrn_country_below_mask_ai_target`, `cbrn_country_should_produce_masks`, and `cbrn_country_has_urgent_mask_production_need` in `common/scripted_triggers/cbrn_protection_triggers.txt`.

The primary weighted consumer is `common/ai_strategy/cbrn_protection_production.txt`; the source defines fourteen AI strategy entries that gate on `cbrn_country_should_produce_masks`, and the urgent entry also gates on `cbrn_country_has_urgent_mask_production_need`.

The raw strategy values are base 50; profile factors 40, 30, 25, 35, 30, 15, and 5; urgent factor 70; and minimum-factory bands 1, 2, 4, 6, and 8.

The installed AI-strategy documentation cautions that minimum-factory strategies do not account for the number of factories actually available, so those literals are not guaranteed factory allocations.

No other direct consumer of the three named helpers was found in `common/` or `events/`; the broad `cbrn_country_has_public_chemical_emergency` helper has other consumers and is outside this narrow review.

## Frozen before/after source snapshots

Repository HEAD at capture was `d53224f109183301ca74351b9e9f07ba22815833`.

| Source | Before bytes and SHA-256 | After bytes and SHA-256 | Assessment |
| --- | --- | --- | --- |
| `common/scripted_triggers/cbrn_protection_triggers.txt` | 41,461; `ce9e25d8fae7c04da8e449b1b468a4bb65f6b652c6a92eb9cd4ff4266e0c2301` | 42,209; `0bf89033e3a99fb2b628be491fb1d7988b2f4c6039e3f4c507d87b9c2e6b2615` | Adds current need, current production signal, and shared structural priority eligibility; removes the AI-only 95% full-gap branch. |
| `common/scripted_effects/cbrn_protection_decision_effects.txt` | 20,310; `bee3a3f81726bd9093e1244ce1bcc7c61d45081bb522994e3b2c5d56b627f506` | 22,020; `8a827a654952ca878f113b2923802e15f573143da5e6f9ee8cce0aa742704ebc` | Adds threatened filter-service and priority-issue passes ahead of remainder work. |
| `common/scripted_effects/cbrn_protection_effects.txt` | 164,713; `b8a45b830f4a2e10c0ce4e5b4cba35cfe527e22daa63f0a3a734bc758d176a8c` | 165,073; `cacdc5e6bb0fd74af36977a973c1a3e4f6def0090ff24cb7f8132ba4b1eadda7` | Keeps military-first ordering, then runs threatened civilian filter and issue passes before remainder passes. |
| `common/ai_strategy/cbrn_protection_production.txt` | 7,500; `c9b7f64a38aae40d1775220d38a3af36b8aacddd8f02c7fd0b0a71ddf569acae` | 7,500; `c9b7f64a38aae40d1775220d38a3af36b8aacddd8f02c7fd0b0a71ddf569acae` | Byte-identical; all strategy IDs, thresholds, and values are unchanged.

Every before and after source is a raw byte copy in `docs/testing/2026-10-09_civil_defence_priority_probability/`; the manifest records copy hashes and verifies that the primary AI strategy file stayed byte-identical.

The primary weighted entries and their literal values are captured in `ai_strategy_surface_inventory.json`; the matrix in `scenario_matrix_before.json` records fourteen named source cases and their assumptions without presenting them as probability-tool output.

## Before-source behavior and weighted consumers

`cbrn_country_needs_civilian_mask_issue` at `common/scripted_triggers/cbrn_protection_triggers.txt:160-168` currently returns true for `has_enemy_used_chemical_weapons`, an enemy with chemical capability, any controlled-state alert, any controlled-state chemical contamination, or the pending UK historical issue flag.

`has_enemy_used_chemical_weapons` at `common/scripted_triggers/cbw_triggers.txt:194-201` conflates three distinct records: permanent victim history on the actor, a finite retaliation-authorized flag, and confirmed-use history on an existing enemy. The source matrix isolates those cases so the new current-need helper can keep actual hostile confirmed use while excluding old victim history and a permission record by itself, as the parent specified.

`cbrn_civil_defence_category_visible` at `common/scripted_triggers/cbrn_protection_triggers.txt:27-35` currently checks public chemical emergency, enemy capability, biological outbreak, and active occupied distribution; it does not check the four active timed response flags.

`cbrn_country_has_public_chemical_emergency` at `common/scripted_triggers/cbrn_protection_triggers.txt:63-72` includes `has_enemy_used_chemical_weapons`, a local exact alert, or local contamination. It is a broad shared helper and should not be globally narrowed for this repair.

The current priority country gap at `common/scripted_triggers/cbrn_protection_triggers.txt:174-180` accepts any controlled populated core below the routine threshold, but does not reject an active state project or require the receiver’s priority-value predicate.

The automatic receiver at `common/scripted_triggers/cbrn_protection_triggers.txt:404-456` requires ROOT control, the national reserve flag, positive population, no active project, a core of ROOT, priority value, and a priority distribution gap. It excludes contaminated low-value rural cores and busy cores even when the country-level AI gap helper counts them.

The priority gap is strict `less_than 50` at `common/scripted_triggers/cbrn_protection_triggers.txt:411-420`; the separate full-distribution gap is strict `less_than 95` at lines 422-431, using `common/script_constants/cbrn_system_constants.txt:884-887`.

`cbrn_complete_priority_distribution_program` at `common/scripted_effects/cbrn_protection_decision_effects.txt:173-190` tries `capital_scope` before the noncapital `every_controlled_state` loop. No deterministic order is claimed for the latter loop.

`cbrn_complete_civilian_filter_replacement_program` at `common/scripted_effects/cbrn_protection_decision_effects.txt:213-231` also tries `capital_scope` before the noncapital `every_controlled_state` loop. Its receiver at `common/scripted_triggers/cbrn_protection_triggers.txt:501-507` checks valid control/reserve/population/no-busy state, positive civilian mask crates, and worn filters, but it does not require core status, priority value, or current local threat; a clean capital is serviced before other states, and the remaining loop order is not claimed.

`cbrn_run_protection_maintenance_cycle` at `common/scripted_effects/cbrn_protection_effects.txt:2416-2439` retains military filter service and military mask issue first, then civilian filter replacement, then civilian priority-mask issue. The source review does not claim a runtime iteration order for the civilian state loops.

No new periodic or worldwide scan is part of this baseline or the parent’s accepted source direction; the reviewed effects consume stock inside the existing maintenance and controlled-state distribution path.

`cbrn_country_below_mask_ai_target` at `common/scripted_triggers/cbrn_protection_triggers.txt:202-236` ORs military coverage deficit, reserve deficit, replacement backlog, a registered mass/prepared/network profile with a full 95% civilian gap, and public-emergency-plus-priority-gap.

`cbrn_country_should_produce_masks` at lines 238-246 requires `basic_gas_masks`, the below-target helper, and at least one production signal, military shortage, or replacement backlog.

The existing `cbrn_country_has_mask_production_signal` at lines 190-200 includes reserve, allied request, Chaos Warfare doctrine, broad enemy-use history, enemy capability, world-confirmed use, or local alert, but not contamination alone or an active timed response. Parent directed that the new current-chemical-need predicate be added to this OR while retaining every existing signal, enabling first production when contamination or an accepted active response is the only signal.

`cbrn_country_has_urgent_mask_production_need` at lines 248-254 uses broad enemy-use history, military mask shortage, or local alert. Its helper remains history-sensitive under the parent’s current direction; the urgent strategy entry remains additionally gated by `cbrn_country_should_produce_masks`.

The registered-profile 95% full-gap branch can make `cbrn_country_below_mask_ai_target` true after routine 50% priority gaps are closed, but `rg` found no caller for `cbrn_complete_full_distribution_program` outside its own definition. This is AI-only unserved demand, not an executed 95% program.

## Named baseline scenarios

The complete source-review matrix is `scenario_matrix_before.json`; each row explicitly binds control, core status, population, coverage, priority value, busy-project state, threat flags, basic-mask technology, and relevant production signals.

| Scenario | Current source result | Parent-directed after check |
| --- | --- | --- |
| `CD_CLEAN_HISTORY_ONLY_PEACE` | Victim history alone currently makes public emergency, category visibility, civilian issue need, production signal, and urgent need true; a 49% core gap also makes the AI target true. | History alone must not retain current category or issue demand; retain the durable history record and broad helper elsewhere. |
| `CD_RETALIATION_PERMISSION_ONLY` | The finite permission flag also satisfies the shared enemy-use helper and currently activates the same gates. | Permission alone must not create current Civil Defence demand; preserve the separate retaliation authorization. |
| `CD_RURAL_CONTAMINATION_VS_CLEAN_CAPITAL` | The clean undercovered capital is a receiver and is attempted before the contaminated low-value rural core, which fails priority-value eligibility; if both states have worn filters and existing mask crates, both pass filter service, with the capital attempted first. | Prioritize threatened states for both filter service and issue before clean fallback work while keeping routine target 50%. |
| `CD_ENEMY_CAPABILITY_ONLY` | Category visibility, issue need, and production signal are true; public chemical emergency and the current below-target AI branch are false when other quotas are met. | Current enemy capability must remain a recognized current need and align the civilian production gap. |
| `CD_ENEMY_CONFIRMED_USE_WITHOUT_TECH` | An existing enemy’s confirmed-use flag triggers current issue and AI production even without enemy chemical technology. | Preserve actual confirmed hostile use independently of technology. |
| `CD_ACTIVE_RESPONSE_AFTER_ALERT_EXPIRY` | With no alert, contamination, history, or enemy capability, an active hospital-response flag does not keep category, issue, or production need visible; the no-reserve under-50 case also lacks a production signal. | Keep accepted active response relevant and let its current-need signal start first production when a serviceable gap exists. |
| `CD_CONTAMINATION_ONLY_NO_RESERVE_FIRST_PRODUCTION` | Local contamination makes issue need, priority gap, and below-target true, but no-reserve contamination alone leaves the production signal and `should_produce_masks` false. | The new current-need predicate must join the production-signal OR without removing existing signals. |
| `CD_NONCORE_CONTAMINATED_ONLY` | Any controlled-state contamination activates issue need, but core-only automatic priority eligibility yields no recipient for a noncore-only case; the separate filter-service path can still service that state if its existing crates have worn filters. | Preserve noncore paid distribution as a separate new-mask issue contract; do not confuse it with service of already-issued noncore filters. |
| `CD_BUSY_CORE_CONTAMINATED` | Country AI gap and production demand are true for a busy core even though both the priority-mask and filter-service receivers reject its active project. | Shared AI-gap and receiver eligibility must reject busy targets. |
| `CD_PRIORITY_GAP_BELOW_50` | A serviceable 49% target has a priority gap and passes the existing receiver. | Preserve the current 50% routine target. |
| `CD_PRIORITY_GAP_EXACT_50` | Exactly 50% fails the strict below-target gap while the alert remains active. | Preserve strict below-50 behavior and do not retune coefficients. |
| `CD_UK_HISTORICAL_RECEIPT_ONLY` | The historical receipt still creates issue need; by itself it does not reveal the category or serve as a production signal. | Preserve the one-time UK issue receipt and its cleanup. |
| `CD_BIOLOGICAL_OUTBREAK_ONLY` | The category is visible, while chemical mask issue, production signal, and urgent production are false. | Keep outbreak visibility without chemical-mask debit or production need. |
| `CD_REGISTERED_PROFILE_FULL_GAP_ONLY` | At 80% coverage, the 95% full-gap profile branch can keep AI production demand true although the 50% priority gap is closed and the full-distribution effect has no executable caller. | Remove this AI-only full-coverage demand unless a real full-distribution consumer exists. |

## After-source comparison

The direct source comparison is saved as `docs/testing/2026-10-09_civil_defence_priority_probability/after_source_comparison.json`, which carries all fourteen same-ID cases, before and after trigger results, receiving targets, stock/maintenance phase gates, and enabled AI strategy factor IDs and literal values.

In the after trigger snapshot, `cbrn_state_has_active_chemical_response` checks the four accepted timed response flags, `cbrn_state_has_current_chemical_need` ORs them with local alert/contamination, and `cbrn_country_has_current_chemical_need` adds current enemy capability and an existing enemy’s confirmed-use flag without victim-history or retaliation-permission tokens.

`cbrn_country_needs_civilian_mask_issue` now uses current need plus the UK receipt; `cbrn_country_has_mask_production_signal` adds current need while preserving its older reserve/request/doctrine/history/capability/world-use/alert signals.

`cbrn_state_has_automatic_priority_mask_gap` is shared by the AI country gap and the actual priority receiver; it requires control, core, population, no active project, the strict below-50 gap, and local need or priority value, while the actual receiver additionally requires the reserve flag.

The after effects add `cbrn_complete_threatened_filter_replacement_program` and `cbrn_complete_threatened_priority_distribution_program`; maintenance calls both after military issue and before the existing civilian filter and priority issue remainder passes.

Across the fourteen cases, `cbrn_country_should_produce_masks` is true in seven before cases and six after cases; the three newly enabled cases are enemy capability only, active response after alert expiry, and contamination-only first production with no reserve, while history-only peace, retaliation-permission-only, busy-core work, and the orphan 95% full-gap profile lose production demand.

The unchanged production factor file activates base 50 plus the matched limited-profile factor 5 in newly enabled cases; active confirmed hostile use without technology and active alert below 50% also retain urgent factor 70; all other profile factor values and five minimum-factory values remain unchanged.

The rural-contamination case remains production-enabled, but after the patch the contaminated rural core enters the threatened filter and issue passes before a clean capital is serviced by remainder passes; the exact 50% case remains outside the strict below-50 routine gap.

The country-level enemy-capability and confirmed-use cases establish current need without a local state flag; their high-value capital can enter the remainder receiver after stock exists, while local contamination and timed response make their own controlled core a threatened target.

The noncore-only case still does not create an automatic priority-mask receiver, though existing noncore masks with worn filters can use the separate service path; the busy-core case no longer counts as an AI gap or a receiver.

The UK historical receipt remains an issue exception, and biological-only outbreak still reveals the Civil Defence category without entering chemical issue or production demand.

The unchanged broad urgent helper still returns true for victim history or retaliation permission; in those two named cases, the new production target gate is false, so the urgent strategy entry is disabled; a separate military shortage could still satisfy the shared production gate and leave that broad urgent factor applicable.

The full-gap predicate and receiver remain defined, but the production-target branch no longer uses the 95% profile gap and there is still no executable caller of `cbrn_complete_full_distribution_program`.

The five minimum-factory entries share the production gate but the fixtures omit `num_of_military_factories`; exact per-scenario factory-band activation is unresolved, so no factory allocation is inferred.

## HOI4 probability adapter evidence and limits

One bounded `hoi4.probability_inspect` call requested adapter `ai_strategy_factor`, the fourteen actual candidate IDs, and the frozen primary weighted-source snapshot; it returned `status=ok`, code `PROBABILITY_SOURCE_DISCOVERED`, but `discoveryReason=no_weighted_surfaces`, `availableCandidates=0`, and zero required inputs.

The single corrected inspect attempt removed `snapshotPath` and scanned the canonical source path; it again returned `no_weighted_surfaces` with zero candidates. Both exact requests, responses, artifact URIs, hashes, and revisions are preserved in `source_hash_manifest.json` and the adjacent inspect receipts.

The parent’s existing `docs/testing/2026-10-09_continuing_protection/parent_service_status.json` records service version 3.10.0; no separate status or negotiation call was repeated for this unchanged connection.

No `probability_evaluate`, `probability_sweep`, MCP `probability_compare`, simulation, sequence, or render call was made because the bounded inspector discovered no analyzable weighted surface and the corrected retry was exhausted. The completed after comparison is source-derived and must not be represented as an MCP result.

The AI-strategy file contains eight base/profile production-factor entries, one urgent factor, and five minimum-factory bands; their literal values are source strategy values, not normalized probabilities. The adapter result does not establish production shares, selection odds, effective factory counts, or a full game AI ranking.

Because the adapter discovered no weighted surface, this review proves no rank reversals, dominance, starvation, repetition, or full-pool choice outcomes.

The current AI strategy file is the sole weighted consumer source captured for this task. Snapshotting its bytes does not freeze every scripted helper dependency; the four named before snapshots are preserved, and no old whole-workspace helper closure was reconstructed.

Offline semantics were read from `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md:77-110, 768-771` and installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/_documentation.md:85-90, 473-514`; their raw SHA-256 values and the local-reference route limitation are in `reference_evidence.json`.

The first reference-context request exceeded the tool’s 160-character question limit; a retry for the same reference-context overlength failure had already been used in the shared earlier audit, so this audit read the identified local wiki and installed documentation files directly instead of retrying that route.

## Evidence files and ownership

`docs/testing/2026-10-09_civil_defence_priority_probability/` contains four verified `.before` and four `.after` raw snapshots, both probability-inspect request/response pairs, `ai_strategy_surface_inventory.json`, `scenario_matrix_before.json`, `after_source_comparison.json`, `reference_evidence.json`, and the source hash manifest.

A temporary Base64 transfer staging file is retained beside `after_source_comparison.json` and listed in the source hash manifest; the parsed JSON file is authoritative.

This subagent made no gameplay, localisation, index, or commit changes. No game process was launched and no game logs were searched or requested.

This bounded read-only after-source comparison is complete; parent owns final integration, scheduler/stock source tests, and any remaining validation.
