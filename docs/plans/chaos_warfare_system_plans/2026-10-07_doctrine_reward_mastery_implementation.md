# Chaos Warfare reward and mastery implementation

Disposition: source implemented and reviewed, 137 source checks passed; native doctrine coverage and matched AI comparison remain blocked; the broader CBRN overhaul remains incomplete.
The [accepted correction](../../specs/chaos_warfare_system_specs/corrections/2026-10-07_doctrine_reward_mastery.md) records the user's weak-reward/narrow-contributor objections and parent-reviewed bounded allocation.
The [architect proposal](2026-10-07_doctrine_reward_mastery_revision.md) retains the source/category review and alternatives, and is not a claim that all alternatives were implemented.

## Behavior and roster

The original infantry adoption reward was 3% breakthrough on Chaos Battalions before their normal unlock requirements were met.
Its four doctrine fragments now form one 15% breakthrough grant at mastery III, coupled to the same recorder and conditional battalion unlock.
Protection Companies receive the retained 10% reliability benefit at adoption; mastery I keeps its night attack and army-cohesion effects.
Mastery V retains 5% assault soft attack and the same advanced equipment grant, with four percent breakthrough and eleven organization points on that hidden technology.
Projector technology breakthrough is 6.5% per upgrade, with the same two tiers, research costs, years, unlocks and other stats.

Armor concentrates two/three-percent breakthrough fragments into 5% at adoption, and three reliability fragments into 15% at mastery I.
Fire support concentrates the 9.5% line and support artillery soft-attack allowance at adoption.
Its five-point organization reward applies specifically to Projector Batteries, leaving armored delivery with its own five-point armor reward rather than both grants.
Operations concentrates the existing 25% reconnaissance allowance at adoption.
Every reward ID, threshold, effect/recorder, permission gate, XP cost, AI coefficient, native multiplier and unlock chronology is retained.
The main emblem is independently restored in commit 7b27f8e8899659c38a77d859bbbef6eec88ab06b.

| Track | Actual contributors |
| --- | --- |
| Infantry (5) | Protection Company, chemical reconnaissance, Field Medical Company, Biosecurity Assault, Chaos Battalion |
| Combat support (3) | Projector Battery, ammunition train, Field Medical Company |
| Armor (3) | Light, medium and heavy armored delivery |
| Operations (6) | Operations HQ, Protection HQ, Medical HQ, Protection Company, chemical reconnaissance, Field Medical Company |

All thirteen retained CBRN roles are covered; entries are unique within each list.
Cross-track medical/protection activity represents different training purposes, while an explicit list avoids relying on undocumented overlapping-filter semantics.
The native documentation provides sub-unit/category/equipment filters and manpower multipliers; it imposes no three-type limit.
The broader roster can accrue mastery faster when more real eligible specialist manpower participates, without weakening the rate of previously eligible formations.
This is contribution arithmetic, not a measured campaign mastery speed.

## Balance evidence contract

Identical-stat grant pooling and independent-source products are kept separate from actual native interpretation.
The intended conservative Chaos breakthrough upper bound is 1.15 * 1.04 * 1.10 * 1.025 = 1.34849, including the possible Cadres defense/breakthrough factor and CBRN-earned defense-skill point.
Projector breakthrough includes three five-percent doctrine sources, two 6.5-percent technologies and the possible 2.5-percent earned skill.
The source audit must verify actual category membership; Protection Company is not in the chemical-support category, and only Projector plus the three armored variants are retained members of that category.
The accidental armored organization case is (24 + 10)/24 times the package army-organization factor; the corrected case contains five flat points, and Projector retains five on its own base of eighteen.
The [source checks](../../testing/2026-10-07_doctrine_reward_budget_source_tests.js) and their handoff retain actual parsed before/after results, source hashes, full thirteen-role coverage and independent/pooled assumptions.
No displayed or native effective division statistic is claimed from those arithmetic models.

Conventional artillery's single 9.5% doctrine grant leaves room for the applicable package army-attack layer within 15%.
Global attack, organization, planning, coordination and reinforcement grants are unchanged.
Equipment, manpower, width, training, supply and support-slot requirements are unchanged; specialist forces do not receive free equipment or automatically authorize attacks.

## References, MCP and limitations

The installed subdoctrine documentation at lines 42-58, revision 81dcc8e9565e16050c269220c7a706ec894bb5b22712ecabfcb598e1fb671df0, documents the native mastery override.
The offline Doctrine/Modifiers/Character sections and vanilla mounted_infantry precedent are recorded in the architect proposal.
Country-only modifiers and native unit-stat blocks remain distinct; database fields retain file-local constants mirrored to the shared tuning table.

Native common/doctrines identifiers are not resolved by the current technology inspector: chaos_warfare explain returned TECHNOLOGY_NOT_FOUND after the narrowed actual-ID retry.
The doctrine render returned partial unrelated selection, zero focused renders, sourceAccurate=false and failed validation; it is not a successful doctrine preview.
The [probability audit](subagent_handoffs/2026-10-07_doctrine_revision_probability.md) owns immutable before sources, same named actor scenarios and exact matched compare results or timeouts.
All five normalized AI bodies match their immutable baseline, and the grand-doctrine source is byte-identical.
The matching armor and infantry nine-scenario comparisons each timed out after 600 seconds without comparison IDs or score traces; Fire Support and Operations comparisons were not submitted after those repeated route failures.
Incomplete helper/external-state coverage cannot become invented click probabilities.
Current native mastery accrual, precise modifier accumulation, actual division stats and in-game presentation remain unproved.
No new GUI, event, decision, on_action, periodic world iterator, equipment, asset alias or CXT content package is introduced.

The two English doctrine files keep current public prose aligned with actual role lists and payouts, including removal of movement/fortification promises from an inert compatibility flag.
The public event/detail/evolution fields are unchanged, so no catalog workbook/export update is warranted by this doctrine correction; the separate catalog owner retains its queued wording review.
Skills used: event assets for the separately committed emblem, events/subagent/native-reference guidance and isolated shared-tree commits.
No stronger unapproved weapon route, policy escalation or substitute milestone is added; unresolved native/MCP coverage remains part of the broader goal's blockers.

The parent reran the actual-source suite: 137 checks pass, with five captured baseline failures reproduced and all sixty-five revised retained-role/stat rows passing both budget models.
The [audit handoff](subagent_handoffs/2026-10-07_doctrine_reward_budget_source_checks.md) distinguishes source AST/constant/recipient proof from native execution and preserves the assumptions.
The highest bound is +34.849% Chaos breakthrough; Projector breakthrough is +34.5832%, Projector defense +34.7559% and armored organization +26.3683% under the independent model.

These sixty-five rows cover soft attack, hard attack, breakthrough, defense and organization.
The neighboring system-guide review found that its reconnaissance technology-only figure omitted the doctrine country factor and two HQ deployed-leader factors.
The [reconnaissance review](subagent_handoffs/2026-10-07_reconnaissance_budget_review.md) owns that separate combination; the passing five-stat audit does not close reconnaissance or whole-package balance acceptance.

The parent applied the [accepted secondary allocation](../../specs/chaos_warfare_system_specs/corrections/2026-10-07_reconnaissance_combined_budget.md) while preserving 25% Operations adoption.
Operations and Medical HQ reconnaissance are 4% and 2%; weather technology fields are 0.01, 0.02 and 0.03.
The parent reran the extended actual-source suite: 221 checks pass, retaining the original 137-check coverage and testing sixty-four reconnaissance subsets for both real company bases.
The [secondary source audit](subagent_handoffs/2026-10-07_reconnaissance_budget_source_checks.md) reproduces forty-one baseline failing subsets and gives a +34.59813% maximum under the flat-point model.
It explicitly retains the alternate fractional-field model's +40.556% result as unresolved native semantics, not a passing cap.
HQ planning, medical reductions, abilities, bills and unlocks remain equal to the captured baseline except the two reconnaissance constants.

The narrow `portable_anemometer` MCP explain and matching 1940 researched-state renders returned partial results, whose complete artifacts were read.
The before and after renders are generated dependency views with `sourceAccurate=false`, zero focused native-folder views and identical PNG bytes; their heading is clipped and they expose no numeric stat delta.
They are not native layout or bonus proof.
The valid comparison request returned `TECH_REVISION_NOT_CACHED`; an earlier request containing unsupported `after.current` was rejected before analysis and was corrected by omitting that field.
Exact revisions, resource URIs, source snapshots and scenario data are retained in [mcp_receipt.json](../../testing/2026-10-07_reconnaissance_budget_review/mcp_receipt.json).
The secondary reductions affect reconnaissance used by combat and native raid success factors; this source audit does not establish their resulting battle or raid outcomes.
