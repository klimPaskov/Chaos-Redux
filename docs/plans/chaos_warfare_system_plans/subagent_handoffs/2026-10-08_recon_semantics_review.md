# Reconnaissance field semantics review

Disposition: implemented bounded read-only research, with native reconnaissance aggregation unresolved.
The parent assigned this report and the evidence directory `docs/testing/2026-10-08_recon_semantics/`.
Only those documentation and evidence files were written.
No gameplay, shared document, index, or commit was changed.

## Answer and practical next action

`recon_factor` is a percentage modifier, while the authored unit `recon` values are reconnaissance stat inputs.
The weather technology recipient blocks use the sub-unit/category bonus channel and contain `recon`, rather than country `recon_factor` or an equipment-bonus block.
Vanilla research provides strong support for interpreting their values as flat reconnaissance points, but the inspected local authoritative sources do not explicitly document a technology-specific reconnaissance exception.
The generic offline technology rule instead calls sub-unit modifiers multiplicative.
This review therefore does not resolve the technology arithmetic to native proof.

Preserve the current 25% adoption reward, HQ 4%/2% factors, and weather .01/.02/.03 values during this research handoff.
Retain the prior source audit's `passed_with_native_semantics_unresolved` status and the failing fractional countermodel.
Do not reduce weather again to satisfy the alternate model or present the flat-point result as a proven engine cap.
The parent can assess the authored utility reward alongside the separately owned force/cost review while carrying this exact semantic gap into its report.
This review supplies no authorization for tiny replacement bonuses, a narrower mastery path, or other gameplay redesign.

## Actual recipients and distinct channels

| Surface | Exact current source | What is established |
| --- | --- | --- |
| Country doctrine | `common/doctrines/subdoctrines/land/chaos_warfare_operations_subdoctrines.txt:19,76-79`, `recon_factor = 0.25` through the file-local constant | A country activation modifier. It is not confined to the weather category. Installed doctrine documentation distinguishes country modifiers from unit-stat and equipment bonuses. |
| Operations HQ | `common/units/cbrn_hq_support.txt:34,77-80`, deployed `recon_factor = 0.04` | A deployed leader modifier using the percentage factor token. It is not a flat four-point unit recon grant. |
| Medical HQ | `common/units/cbrn_hq_support.txt:51,199-203`, deployed `recon_factor = 0.02` | The same deployed leader percentage channel, alongside its separate sickness/wounded factors. It is not the field medical company's base recon stat. |
| Chemical Reconnaissance Detachment | `common/units/cbrn_regimental_support.txt:52,239-257`, base `recon = 4.00` | Unit stat input, with both `category_cbrn_reconnaissance` and ordinary `category_recon` memberships. |
| Field Medical Support | `common/units/cbrn_regimental_support.txt:115,601-621`, base `recon = 2.00` | Unit stat input, with neither reconnaissance category membership. Weather grants do not select this unit. |
| Weather technology | `common/technologies/chaosx_technologies.txt:58-60,1052-1073` | `portable_anemometer`, `meteorological_stations`, and `upper_air_soundings` grant category `recon` bonuses .01/.02/.03. They do not contain country factors or equipment bonuses. |

The visible instrument technologies still grant the three weather nodes at `chaosx_technologies.txt:1198,1239,1280`.
The recipient membership and source channel are definite source facts, independent of the unresolved numeric interpretation.
The factor may influence a command's units, but these sources do not prove fill scaling, field-marshal propagation, multiple HQ-instance behavior, or exact division aggregation.

## Evidence classification

### Documented

Offline `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md:973` labels `recon_factor` percentual.
Installed `documentation/modifiers_documentation.md:4537-4541` recognizes the modifier, with army and defensive categories and one-decimal display precision, but states no accumulation equation.
Installed `localisation/english/modifiers_l_english.yml:796-797` uses percentage formatting for `recon_factor_tt`.
Together these establish the factor channel's intended percentage meaning, without establishing a multiplication layer for each source.

Offline `paradox_wiki/Unit modding - Hearts of Iron 4 Wiki.md:308-318` lists `recon = 1` as reconnaissance among unit stats.
Installed `common/units/equipment/_documentation.md:113-114` separately identifies equipment stat fields as base values before variant upgrades and modules.
Installed `common/doctrines/grand_doctrines/_documentation.md:51-96` separates country modifiers, category/sub-unit stat bonuses, and `equipment_bonus` entries.
Installed `documentation/effects_documentation.md:2391-2413` documents permanent subunit/category bonuses, but does not document reconnaissance arithmetic.
An equipment archetype modifier, a category stat bonus, and a country factor must therefore retain their actual recipient channels rather than being combined solely because their labels say reconnaissance.

Offline `paradox_wiki/Technology modding - Hearts of Iron 4 Wiki.md:94-122` documents category/sub-unit recipients and generically calls their modifiers multiplicative at line 105.
It gives no reconnaissance-specific exception.
That sentence is neither flat-point proof nor a recon-specific native aggregation formula.

### Strong source inference

Installed vanilla `common/technologies/support.txt:536-544` grants `category_recon = { recon = 2 }` and separately `helicopter_recon = { recon = 1 }` in `tech_recon2`.
The subsequent `tech_recon3` and `tech_recon4` retain category grants of 2 at lines 586 and 636.
Installed vanilla `common/units/recon.txt:19-39,202-226` gives ordinary reconnaissance categories to units with reconnaissance bases 1 and 2.
Those intentionally large technology values and differing base units support the established flat-point reading, but do not expose the native reader or evaluated unit values.

Installed `localisation/english/stats_l_english.yml:48-52` uses raw-number formatting for `STAT_ARMY_RECON_VALUE` and `STAT_ARMY_RECON_DIFF`, and percentage formatting for `STAT_ARMY_RECON_MOD_VALUE`.
This demonstrates both presentation channels exist.
It does not prove which one the engine selects for a particular technology recipient.
Installed `common/modifier_definitions/modifier_definitions.txt:1-17` explicitly describes custom definitions as extra modifiers the game does not itself use and describes their value type as tooltip formatting.
No `recon` or `recon_factor` definition is present there, so that file cannot supply the missing native arithmetic.

Vanilla `common/units/hq_support.txt:112-139,161-165` uses both deployed `recon_factor = 0.1` and a separate unit `recon = 1` in `hq_recon`.
This is a direct precedent for keeping the deployed commander factor and unit stat separate.
Offline `Modifiers:58` describes modifier values adding within their applied scope, and offline `Data structures:1700` describes a leader's unit-modifier total.
They support considering a pooled leader factor, but neither document the `deployed_leader_modifiers` loader or how that total interacts with the country total.
The prior independent-factor model is a conservative source reservation, not proof that the engine multiplies each HQ separately.

### Unknown

The exact native arithmetic for technology `category_cbrn_reconnaissance.recon` remains unproven.
Country versus leader aggregation, equipment-fill scaling, field-marshal inheritance, duplicate HQ sections, and conversion of several company inputs into final division/battle reconnaissance remain unproven.
No tactic-selection probability is inferred from these stat values.

Under the current flat-point model, weather alone changes the base-4 detachment by `.06 / 4 = 1.5%`.
Under a pooled fractional technology countermodel, it changes the stat by 6%.
The prior independent-factor reservations consequently remain +34.589% with pooled flat points, +34.59812868125% with separately normalized flat-point guards, and +40.556% in the pooled fractional countermodel.
These are conditional source calculations, not three competing measurements of native behavior.
No arithmetic guard was rerun or rewritten because this review has not supplied a justified replacement formula.

## MCP evidence and revisions

The connected reference_context/search/read and source_lookup routes were called successfully.
The technology context included both installed and offline sources, with no omitted required source kind.
`script_doc` coverage was unavailable, and there is no claimed native-engine source coverage.
The exact successful reference reads are retained in `game_factor_read.json`, `wiki_factor_read.json`, `technology_rule_read.json`, and `additional_reference_reads.json` in the evidence directory.
The `deployed_leader_modifiers` reference search returned zero sections across configured installed, wiki, and script documentation, retained in `hq_search.json`.
This is the exact documentation blocker for the HQ loader, rather than an unavailable reference route.

The current bounded `hoi4.tech_inspect(mode=explain, technologyId=portable_anemometer)` returned `TECH_INSPECTED_PARTIAL`.
Its linked artifact was read in full and saved as `portable_anemometer_explain.json`.
Artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85c17b5374051b40370e64dfe30252f0f88c4beb5592a8a713d8efe6c3e9e0c9/02137e255de36c5114884d0d21c43eab6cb1af72c5a1570e88492645d192fb5f/technology-explain-386c54f7d092.json`.
Artifact SHA-256 is `85c17b5374051b40370e64dfe30252f0f88c4beb5592a8a713d8efe6c3e9e0c9` and graph revision is `386c54f7d09227d36182211b5e6d5c8943ce4e68aeea96c4ae74fd207c71af52`.
It reports `staticAnalysis = true`, `complete = false`, `matchingBonuses = []`, and deferred large-workspace helper projections.
It resolves the exact current source and external grants, but gives no numeric reconnaissance semantics.
No repeated inspection, render, helper_expansion, native task, or job route was launched to try to turn that limitation into proof.

Live source_lookup resolved `portable_anemometer` and vanilla `tech_recon2` without shadowing or override findings under workspace-index revision `ed915a0880f765a2f48dcd59dcbf9a90b648f2baddebbb8d1c336743e0304c35`.
The exact lookup responses are saved as `weather_source.json` and `vanilla_tech_recon2.json`.
`source_excerpts.json` retains Windows absolute paths, line spans, exact read text, and SHA-256 revisions for the actual mod units, HQ, doctrine, technologies, installed vanilla precedents, format files, and unit wiki section.
The four current gameplay-file revisions match the prior final source audit where applicable.

| Reference | Revision |
| --- | --- |
| Installed modifier documentation | `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e` |
| Offline Modifiers | `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f` |
| Offline Technology modding | `c5428838db20c4c812c66aff82cbafc58db3b73453c30436bce0d97436170bee` |
| Offline Unit modding | `996fc17096970b294292a69d35afa0c13ebf78feb76c84d1979372fde7864714` |
| Installed grand-doctrine documentation | `5ff029facf7fa8e8139d3ee33209329483f241e0241b0b568f687ca4ac2b43f0` |
| Installed effects documentation | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Offline Data structures | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |

## Completion limits

Completed: actual recipient and channel review, current source fingerprints, exact vanilla precedents, format review, successful revision-bound MCP documentation reads, and one current partial technology inspection with artifact review.
Unresolved: native technology reconnaissance arithmetic and country/HQ/division aggregation.
No fallback or gameplay simplification was implemented.
No helper, call site, constant, event target, cleanup logic, probability weight, or AI patch was required or added.
No gameplay validation, force/cost comparison, game launch, log search, or commit is claimed.
Skills applied: `chaos-redux-events` and `chaos-redux-subagents`, with no skill changes.
