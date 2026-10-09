# Research costs and numeric text reconciliation

Disposition: implemented bounded source calibration and numeric bindings; native timing, presentation, reconnaissance aggregation and full CBRN completion remain unresolved.
Acceptance basis: the parent assigned this documentation tranche and reaffirmed the user's original direct 50/75/100 base-day instruction over spec 13's conflicting relative-band sentence.
The accepted design remains [spec 13](../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md); this report records implementation and evidence limits, without creating another design package.

## Source-of-truth map and dispositions

| Document or receipt | Disposition and evidence boundary |
| --- | --- |
| Spec 13 and CBRN-08 requirement ledger | Accepted day targets corrected to the original user instruction; source calibration implemented; native timing/presentation unresolved. |
| [Research owner handoff](subagent_handoffs/2026-10-08_cbrn_research_cost_review.md) and [40-check receipt](../../testing/2026-10-08_cbrn_research_cost_review/source_test_results.json) | Implemented 27 researchable costs in two files; 40 checks, zero failures, all other resolved technology fields and AI blocks preserved. |
| [Numeric binding handoff](subagent_handoffs/2026-10-08_remaining_constant_localisation.md), [validation receipt](../../testing/2026-10-08_remaining_constant_localisation/validation.json) and [before manifest](../../testing/2026-10-08_remaining_constant_localisation/before_manifest.json) | Implemented 15 expression replacements across ten keys through twelve getters; immutable canonical Git before blobs replace the mutable-HEAD test baseline; native display unresolved. |
| [Reconnaissance semantics review](subagent_handoffs/2026-10-08_recon_semantics_review.md) | Read-only research implemented; percentage factor channel documented, flat weather points strongly inferred from vanilla, native category and HQ aggregation unresolved; no further cut authorized. |
| [13-role force audit](subagent_handoffs/2026-10-08_equal_cost_force_audit.md) and [22-source inventory](../../testing/2026-10-08_equal_cost_force_audit/equal_cost_force_inventory.json) | Source-cost audit retained; two captured technology hashes predate this cost patch, while the other twenty source hashes still match; native combat and full design costs unresolved. |
| [Probability owner handoff](subagent_handoffs/2026-10-08_cbrn_research_cost_probability.md) | Fresh exact-fixture partial comparison reported by the reconciliation auditor below; historical scenario-hash discrepancy remains unresolved and old summaries do not establish verbatim-fixture identity. |
| [Probability skill handoff](subagent_handoffs/2026-10-08_probability_snapshot_skill_note.md) | Implemented narrow generic skill guidance under separate parent ownership; this documentation tranche changes no skill. |
| Current unit and doctrine guides | Implemented documentation alignment; historical ratio, hash identity and native limits preserved. |
| Current simplification guide | Left unchanged: no research-cost, reconnaissance or whole-force claim in this guide requires this tranche's correction. |

## Research calibration and preservation

Installed `NTechnology.BASE_TECH_COST = 110` has no mod override in the reviewed define surface.
The frozen `.5/.75/1` costs therefore modeled 55/82.5/110 unmodified base days.
The parent accepted downward five-decimal factors `.45454/.68181/.90909`, modeling 49.9994/74.9991/99.9999 source days, less than .001 day below the respective 50/75/100 targets.
This tolerance preserves the user's duration target and does not establish exact native completion days.
The owner evidence identifies all 27 researchable IDs, seven basic, ten standard and ten advanced, and preserves hidden grant-marker raw costs with file-local aliases.
No global base override, research-speed, chronology, stat reward or AI coefficient change belongs to this calibration.
The two current source hashes are `4f3743d8d911b2b818cc0d3093417f4b8c2ad21330e00a8fdbba9f62e9e7c998` for `common/technologies/chaosx_technologies.txt` and `d1f9f1e0444b899019264d73025bd951f84e5e754ebf7cc8cb30cbc8752d3eb6` for `common/technologies/cbrn_regimental_support_technologies.txt`.
The owner AST receipt covers all fifty bodies, permits only 27 resolved research-cost fields to change, and preserves the other 23 complete bodies.
A bounded curator check of all 22 force-inventory hashes found only those two technology differences, matching the owner after hashes; the other twenty still match their captured source.
The historical force audit's claim that its technology hashes matched is a capture-time fact, rather than final cost-calibrated source identity.

## Numeric text and portable before evidence

The twelve constant-backed getters serve achievement thresholds, limited facility-recovery fractions and Event 020 response requirements/duration.
They replace fifteen raw expressions across ten public keys without changing numbers, numeric formatters, surrounding prose or requirements.
The portable test reads repo-relative sources from its own location and retained immutable before files.
Its before manifest identifies canonical blobs at commit `0819dc70d724badbe30b74128648976245d6b4ad`, explicitly distinct from original checkout newline bytes.
The parent reran all twelve bindings after replacing the mutable-HEAD baseline; the source receipt does not prove engine getter evaluation or visible wrapping.
No event-log, event-detail, evolution-detail or cluster wording changed, so no event catalog write or CSV export is required; the dirty workbook belongs to another owner.

## Balance and reconnaissance limits

The historical 1.449 conventional-template figure is an algebraic price ratio.
At a 756.5 IC available budget, one plain nine-infantry formation spends 522 IC and retains 234.5 IC; this is a whole formation with reserve, rather than equal spent IC or a deployable fractional force.
The 13-role audit uses whole formations plus reserve and same-slot HQ comparisons, finds no source-proven double mask debit, and qualifies projector pricing as chassis-only.
Armored comparisons require the same chosen flame-tank design; actual module/full-projector costs, native division aggregation and battle results remain unknown.
Preserve Operations' 25% reconnaissance reward, HQ 4%/2% factors and weather .01/.02/.03 fields.
The +34.59813% flat-point source reservation and +40.556% fractional countermodel remain conditional calculations, and neither proves the native 35% cap.
No further bonus cut follows from the read-only semantics review.

## MCP evidence and unresolved delivery

The curator called `hoi4.tech_inspect(mode=explain, technologyId=basic_gas_masks)` successfully and read its complete 21,631-byte linked artifact.
It records `researchCost = 0.45454`, graph revision `9788b23ba5ff29a8ec3e3455242d4c8b2a6a0d861da43a15605b166c1bf0415b`, `TECH_INSPECTED_PARTIAL`, `complete=false`, and unsupported runtime research time, dynamic localisation and large-workspace helper projections.
Stable artifact: [technology explanation](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/507584f8c63d5b65c866b1bb9888cd469fa0eb50a9ed7adbe2ed7b6b27f75791/e150b57ceb00e676700f5a9cbe4ac4c7d530bd17c87aaa905543f49d5e2bd842/technology-explain-9788b23ba5ff.json).
The curator's numeric-response `hoi4.decision_inspect` request returned `DECISION_ANALYZED_PARTIAL`, revision `331e2230de71882b14cfd44e242c4681fe5c2a82779fd715dfffebc9b16ae8fa`, `complete=false` and 100 unresolved definitions under an unbound GER fixture.
Stable artifact: [partial decision receipt](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/852aee59af7e32383b9eeb12b8192f013b17704e8cfbae71cdde2ef4d4115c6e/3c14c61edd4a8b8ecddd0bbaed57b2fd7e24d4b41dbce238c6e76a4101fe4576/decision-b44c8f36ce695101e195c66e.json).
Only its returned receipt was reviewed; its full 613,536-byte body was not read, and no individual gate or tooltip conclusion is drawn from it.
Exposed tools and successful partial inspections establish these route responses; they do not establish standalone viewer availability or native consumer acceptance.
The standalone Technology Tree Viewer is absent under the force auditor's explicit PATH/registered-app/repo search, while historical summary renders retain `sourceAccurate=false`.
The parent's original approximately 48 MB technology before-graph cannot be used canonically while its artifact provenance is unavailable.
The [parent technology receipt](../../testing/2026-10-08_cbrn_research_cost_review/parent_technology_comparison.json), SHA-256 `abd794efb45ae6fd72652d6fa9afa76e0f5718d195478888d9fbf5febf2ccdd2`, records a read-only reverse comparison from current implemented costs to virtual original two-file costs.
It returned `TECH_COMPARED_PARTIAL`, before revision `9788b23ba5ff29a8ec3e3455242d4c8b2a6a0d861da43a15605b166c1bf0415b` and after revision `5d62d7d87fd3f9fe49c3404e107533f797f027aeb9a709a6ee3fe433a6070062`, with zero added/removed/renamed/moved/regression counts.
The 1,258,458-byte comparison body could not be read: `MCP -32603: Artifact provenance manifest is unavailable`; its numeric cost metadata/delta is therefore unread, and no native-day or canonical forward-baseline proof follows.
The original before graph also returned `ARTIFACT_NOT_FOUND`, and the earlier client handle was lost after an app reset with server outcome uncollected.
Stable comparison reference, retained with the exact retrieval blocker: [reverse structural artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a0f0588571705560abcc16b7a4387579526e361c3518c09ca2603bd34bf46d8/1976990cb4a67ad3bd77963806e044143d116baca65aa2d78be524bb898c8ed3/technology-compare-9788b23b-5d62d7d8.json).

The probability reconciliation auditor reports a fresh replay of the exact saved `scenario_fixture.json` fixture with hash `9014abc855784fcdc7f9cba67f0c7d33afff123b1402db73949c381209e7c004` in both frozen-before evaluates and both before/after comparisons.
Main analysis `probability-0a6b9348d79ac6a20805a416` has 150 rows, 144 eligible, zero exposed changes, 181 unresolved items and six unresolved candidates; regimental analysis `probability-e3ae87cec00775b6c50bd12e` has twelve rows, twelve eligible, zero exposed changes, 29 unresolved items and no unresolved candidates.
The frozen [reconciliation receipt](../../testing/2026-10-08_cbrn_research_cost_probability/reconciliation.json), SHA-256 `b8f7bd088bf72b352eb9b01c2edae6bccbf8694e0850e4df1bed3d0415662070`, preserves sixteen raw request/result packets and the exact limits.
The curator read the four replay packets in [raw_calls](../../testing/2026-10-08_cbrn_research_cost_probability/raw_calls/), verified each request's `scenarioSet` equals the saved fixture verbatim, and checked their matching returned hash and partial counts.
The auditor also ran explicitly synthetic bindings and a 49/50/51 coverage sweep, but native AI base/factor `@` tokens remained unresolved, the sweep render was stale and standalone comparison render was not cached.
Its partial score outputs do not establish exact numeric ordering, threshold effects, rank reversal or native probability; shared helpers/constants remain current rather than a historical whole-workspace snapshot.
The six scenarios bind only year; doctrine and stage names are labels, while prerequisite, country, CBRN-variable, complete gamewide pool and `technology.external_factors_complete` inputs remain unknown.
Zero exposed `ai_will_do` score change does not establish unchanged total native research preference because research cost is a native selection input.
The historical `6af9...5633fd467` versus `6af9...f08a3e6c19cf61` discrepancy remains unresolved without the original request and fully assembled verified artifacts; edited summaries do not repair that provenance.

Parent review reran all forty research-cost checks and all twelve numeric-binding checks in both the shared checkout and an extracted isolated candidate tree.
The extracted tree also retained exact equality of all four replay request fixtures, their returned scenario hash and referenced snapshot byte hashes.
Only the five owned probability-guidance lines enter the shared skill commit; unrelated skill edits retain their existing staged or unstaged state.
These checks cover authored source and evidence integrity, without adding native engine proof.

The wider CBRN goal remains incomplete.
Native technology field precision/calendar rounding, source-accurate card/scroll layout, numeric wrapping, reconnaissance aggregation and whole-force outcomes remain unproved.
No fallback or gameplay simplification was introduced by this documentation tranche.
