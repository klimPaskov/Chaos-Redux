# Biological incubation timing probability audit

Date: 2026-10-07.
Disposition: exact source identity and random-getter location confirmed, while analyzer support and numeric timing remain unresolved.
Mode: read-only baseline audit before the parent caller repair.
The parent-provided patch intent is to capture the computed delay after the existing draw and keep that single draw inside the incubating and not-scheduled guard; this audit does not claim that edit has been applied or validated.

## Baseline capture

The exact pre-edit working source copy exists at docs\testing\2026-10-07_biological_incubation_timing\before\common\scripted_effects\biological_lifecycle_effects.txt.
Its SHA-256 is 3d611e3424da6f221446810f6f4ad49e4065b1a8c066bcf7bec3989038a5d3cc, and it matches the current file byte-for-byte at 169,226 bytes.
The audited helper is bio_lifecycle_prepare_incubation_delay at lines 635-658.
The inspected random getter is line 653: set_temp_variable_to_random = { var = bio_incubation_random_roll }.

## HOI4 MCP evidence

The live probability tool schema lists direct_random as an adapter and accepts a source selector object, while the source property itself is exposed as unknown.
The exact request used adapter direct_random, source path common/scripted_effects/biological_lifecycle_effects.txt, line 653, and refresh true.
The request was accepted and returned PROBABILITY_SOURCE_DISCOVERED with discoveryReason no_weighted_surfaces, candidates 0, availableCandidates 0, requiredInputs 0, and unresolved 0.
Only the named biological_lifecycle_effects.txt source was listed in filesScanned.
Inspect source revision: 913df62cfa9a7dab36b94795379dca78c0d7dacd39c2e6dd2500ef17f0cac210.
Inspect source hash: e94255d09dd00715c28c876d4b69b243fc7a75673c54483878862b19997d345e.
Inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13fc801800fd171c1527dc3d1ca5cf811cf3f226725573c427605c89c53ce6e5/7d3b2e1a91c897be33a509a97387278f5660df754d55e8514dc53bdc27463fc4/probability-inspect-e94255d09dd0.json.
The tool returned a 384-byte resource link, and its body was not retrieved.

The current source_lookup request at path common/scripted_effects/biological_lifecycle_effects.txt and line 653 confirms the exact owning helper and key path.
It returned source revision cf619439fd438a3c71084bed2b947ff7ab6f6cc1f010d8cc4d681513338f3fcd.
The owner is bio_lifecycle_prepare_incubation_delay, lines 635-658.
The returned keyPath is set_temp_variable_to_random occurrence 0, and the source line assigns bio_incubation_random_roll.
The request and result are retained in source_lookup.json.

The direct_random adapter did not expose a candidate for this random getter.
That is a narrowed analyzer coverage result, not evidence that the random value is constant or that its variance is zero.
The current tool result does not establish whether direct_random intentionally excludes set_temp_variable_to_random or whether this effect needs another supported source representation.

## Source timing trace

The helper selects agent-specific base and random-span constant identifiers for anthrax, plague, tularemia, or smallpox.
The random getter has no explicit min or max arguments in this source.
Installed documentation says the default random value is in the half-open range [0,1), and the offline wiki row describes the same default.
The helper multiplies that draw by the agent-specific random-span value, adds it to the agent-specific base delay, rounds the result, and applies the minimum-event-delay clamp.
The literal values of those constants were not read or hand-calculated in this bounded audit.
No expected delay, outcome distribution, bound after rounding, or exact activation timing is claimed.

The source lookup identifies the owner chain without expanding the whole lifecycle file.
The adapter returned no random candidate, so there are no candidate IDs, a complete weighted candidate pool is not applicable, and no valid probability scenario was submitted.
The four agent names are recorded only as source branches, not as evaluated scenarios.
No helper-output override, native-delay distribution, simulation, sweep, sequence, render, or before/current probability comparison was invented.

## Findings and remaining work

The only exact numeric-random fact established here is the source operation and documented default draw range.
The downstream delay depends on agent-specific constant pairs plus rounding and a clamp, but the probability MCP produced no candidate or analysis ID.
The returned inspect result therefore cannot support a numeric delay distribution or compare before and after the planned caller repair.
An after-edit probability comparison remains blocked unless a later direct_random inspection supplies a real candidate or the connected adapter documents a supported getter-random input shape.
The parent should preserve the single existing random draw under the incubation guard while storing its computed delay after the draw.
That after-edit source behavior is pending parent implementation and review.

No lifecycle logic, constants, test files, or gameplay files were changed by this worker.
No MCP evaluate, compare, sweep, simulation, sequence, or render call was made because the inspect produced no eligible random candidate.
The exact baseline snapshot and both source identity results are retained under docs\testing\2026-10-07_biological_incubation_probability\.
Skills carried from the prior audit context: chaos-redux-subagents, chaos-redux-native-raids, and chaos-redux-events.