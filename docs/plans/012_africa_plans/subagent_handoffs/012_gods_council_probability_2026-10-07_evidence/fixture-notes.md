# Fixture notes

The nine-case file is a prepared prepatch scenario matrix, not an observed campaign state and not an MCP evaluation result.

It uses the scenario fields seen in prior successful HOI4 MCP request evidence: schemaVersion/id/scenarios at the set level and actor/date/state/flags/controls/scopes/scopePools at the case level. It does not inject helper results or candidate overrides.

Every case models GER as the participant and ETH as current host, with host generation 27, participant generation 27, authority epoch 4, ETH origin/host identity, the host participant array containing GER, a synthetic owned and controlled capital state 271, a 500-equipment donor reserve, a 400-unit host reserve variable, and 50 political power. These facts are model inputs only.

COUNCIL_PART_PAID sets GER infantry equipment to 1,400, which leaves 900 above the 500 donor reserve. The frozen prepatch source has no live pledge-progress token, so this case is only a stock analogue for the partial-payment threshold. No future flag or helper name was guessed.

COUNCIL_EMPTY_RETRY sets the participant inventory to the 500 reserve. COUNCIL_STALE_AUTHORITY changes only the participant generation to 26 while ETH remains at generation 27. COUNCIL_COMPLETE records the existing council voice and pledge flags.

The decision candidate pool supplied to MCP contains exactly gods_of_africa_council_pledge and gods_of_africa_council_speech. The successful probability_inspect call says these are the complete discovered candidates for this bounded surface. This pair is complete for willingness-score comparison only and is not a complete country decision-selection denominator.

The synthetic participant scope pool contains only GER and is complete inside the model fixture so the current-host membership check can be traced. It does not claim that an actual campaign has only one participant.

The fixture does not fully bind AI strategy factors outside the two decision blocks, the diplomatic opinion used by the speech-friendly modifier, the complete African-core ownership map, or live runtime scopes. The inspector reported no required input paths, but the valid probability evaluation and sweep did not return, so this is not proof that all source helpers resolved.

The nine named cases are stored for the parent’s later same-scenario comparison. Only COUNCIL_READY was sent in the bounded evaluation and sweep probes, and neither probe returned an analysis id, a trace, a canonical MCP scenario hash, or rendered output. The fixture SHA-256 is recorded separately in fixture-metadata.json.
