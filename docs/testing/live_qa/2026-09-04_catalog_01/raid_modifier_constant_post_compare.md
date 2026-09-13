# Event 016 raid modifier constant post-patch comparison

Audit date: 2026-09-05.

Audit status: **The 22-field alias/header transformation is exact; the mandatory probability comparison remains unresolved because no native raid outcome adapter or genuine baseline scenario contract is available.**

This is a read-only post-patch audit of the four fictional raid files named by launch_08. No gameplay source was edited by this audit, and no game, desktop, staging, or commit operation was performed.

## Patch boundary and exact source transformation

The archived pre-patch bodies are under docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_raid_weights/common/raids/.

The owner repair manifest is docs/testing/live_qa/2026-09-04_catalog_01/raid_modifier_constant_repair.json.

The manifest SHA-256 is 739685820001708CBCD5516C6140130FBFA8EF9F846C33155C5A7DAE22308F43.

The manifest records the following exact source identities and repair counts.

| Source file | Archived SHA-256 | Current SHA-256 | Fields | File-local aliases and values |
| --- | --- | --- | ---: | --- |
| common/raids/biological_battlefield_raids.txt | DDE40E3EAC91AD357DB5CB3C90AF36E0E3391BAA68D5E5D900241340EF3EDDD7 | 6B01892C53CEBE7BC638F6D4C9EFD5E2E1A6041D8B44546CB18402D3B76A1516 | 4 | CR_STAGING_NATIVE_SUCCESS_BONUS = 0.15 |
| common/raids/biological_raids.txt | 8EF5CEBC37F88862BC3F33DD07B0A307182EB792D5CBCC749CB3F858B8668267 | 911F0403B789BB09343C4B9BD89AB2E48137DF35461D89CCBAE34EF964578374 | 12 | CR_STAGING_NATIVE_SUCCESS_BONUS = 0.15; CR_STAGING_NATIVE_CRITICAL_BONUS = 0.10; CR_STAGING_NATIVE_DISASTER_REDUCTION = -0.08 |
| common/raids/zombie_weaponized_friendly_raids.txt | 94FB7B740DAD22D71BD0D6884EA79FA44D510D4F4804E60C6D436827EE463F8C | 8CF18DF301C689CA377BEAB21976E8E1DEB3F8B0965F54FD6E02AD044FD90613 | 3 | CR_STAGING_NATIVE_SUCCESS_BONUS = 0.15 |
| common/raids/zombie_weaponized_raids.txt | 37A26074261A93809117C16BAFA70751323018B0C06EDA6B057959B4C49787A6 | 4023B49FE8077B26B4A77397F7AC232B176181F7776240FCB77916AE2CE34C78 | 3 | CR_STAGING_NATIVE_SUCCESS_BONUS = 0.15 |

The local current and archived hashes match the corresponding after_sha256 and before_sha256 values in the manifest for all four files.

The post-patch headers add the two-line native-weight explanation, the file-local alias definitions, and a separating blank line before the pre-existing file content.

The header contains four lines before the existing body in biological_battlefield_raids.txt and both zombie files, and six lines before the existing body in biological_raids.txt.

After removing only those added header lines and expanding each alias back to its original constant token, the current body is line-for-line identical to its archived pre-patch body in all four files.

The inverse expansion matched 22 current alias occurrences to 22 archived original occurrences one-for-one: 14 native_success_bonus fields, 4 native_critical_bonus fields, and 4 native_disaster_reduction fields.

The current files contain zero remaining constant:brilliant_scientist_biological_staging.native_* tokens in the repaired weight fields.

The current repaired weight lines are 186, 328, 410, and 492 in biological_battlefield_raids.txt; 326, 345, 367, 765, 784, 806, 1204, 1223, 1245, 1643, 1662, and 1684 in biological_raids.txt; 96, 241, and 386 in zombie_weaponized_friendly_raids.txt; and 138, 273, and 407 in zombie_weaponized_raids.txt.

All outcome formulas, staging-flag gates, references, raid identifiers, AI score blocks, target gates, and other file bytes are preserved by the inverse comparison.

The authoritative shared values remain native_success_bonus = 0.15, native_critical_bonus = 0.10, and native_disaster_reduction = -0.08 in common/script_constants/016_brilliant_scientist_raid_lifecycle_constants.txt:90-104.

The shared native_ai_factor = 4.0 references are outside these 22 rejecting weight fields and were not changed.

## Audited identifiers

| Source file | Raid identifiers and repaired outcome fields |
| --- | --- |
| common/raids/biological_battlefield_raids.txt | anthrax_battlefield_dissemination, plague_battlefield_dissemination, tularemia_battlefield_dissemination, and smallpox_battlefield_dissemination, one success modifier each |
| common/raids/biological_raids.txt | anthrax_strike, plague_strike, tularemia_strike, and smallpox_strike, each with success, critical, and disaster modifiers |
| common/raids/zombie_weaponized_friendly_raids.txt | weaponized_zombie_strike_low_friendly, weaponized_zombie_strike_medium_friendly, and weaponized_zombie_strike_high_friendly, one success modifier each |
| common/raids/zombie_weaponized_raids.txt | weaponized_zombie_strike_low, weaponized_zombie_strike_medium, and weaponized_zombie_strike_high, one success modifier each |

The archived launch_08 parser evidence and original locations are recorded in docs/testing/live_qa/2026-09-04_catalog_01/raid_modifier_constant_baseline.md.

The syntax basis remains the installed raid documentation at C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/raids/_documentation.md:209-325 and :411-429, the installed script-constant references at C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md:1-32 and C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md:216-244, and the offline wiki pages paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:42-53 and paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md:176-178.

## Post-patch MCP inspection

Workspace: mod_chaos_redux_ea3b2d67c2c0.

The required post-patch read-only hoi4.probability_inspect call used the current full inline source for anthrax_strike in common/raids/biological_raids.txt with no forced adapter.

The inspect returned status ok and code PROBABILITY_SOURCE_DISCOVERED.

The MCP source revision was 2b3fd67016520a057a67c146811f8575bc4f90eded47e7a78b5b2c5435c68cb5.

The MCP inline source hash was 0112ef1b5b8967066c0dd8e5debb1020b01d52e628094b6df045329004fbbf8c.

The inspect artifact was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1db3fdd9232579bd565603c5d8e296e6078e495b69156ca16cc510362f216b7b/278bc5231f4aedc85a7e1bba709eb06b016aa46459941ee2ca66fe97f0b4341f/probability-inspect-0112ef1b5b89.json with artifact SHA-256 1db3fdd9232579bd565603c5d8e296e6078e495b69156ca16cc510362f216b7b.

The source inventory exposed 11 generic adapters and suggested decision_ai_will_do with four candidates named anthrax_strike, plague_strike, smallpox_strike, and tularemia_strike.

The inventory did not expose a native raid success_factors, raid outcome, or raid AI route.

A second read-only inspect forced direct_random on the same current inline source.

It returned status ok and code PROBABILITY_SOURCE_DISCOVERED with discoveryReason identifier_not_found, requestedAdapter direct_random, candidates 0, and availableCandidates 4 only through the generic decision_ai_will_do inventory.

The direct_random inspect used the same MCP revision 2b3fd67016520a057a67c146811f8575bc4f90eded47e7a78b5b2c5435c68cb5, source hash 0112ef1b5b8967066c0dd8e5debb1020b01d52e628094b6df045329004fbbf8c, and no native raid candidate.

The direct_random inspect artifact was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f6fb57af740caffb66a1901f4abb1fa01b6fa7006a65c71988584d5c7d86bb0/2f7b5d075c6128dc349e700f61912da10d34cb290abbe61d43b187d7f8dfb47a/probability-inspect-0112ef1b5b89.json with artifact SHA-256 5f6fb57af740caffb66a1901f4abb1fa01b6fa7006a65c71988584d5c7d86bb0.

This confirms that the generic inventory can see raid ai_will_do names in the inline source, while the installed probability service still has no native raid modifier or outcome adapter.

## Mandatory before/after comparison attempt

The read-only hoi4.probability_compare call used adapter direct_random and supplied genuine full inline before and after bodies for the same source identifier anthrax_strike and path common/raids/biological_raids.txt.

The before body was read from docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_raid_weights/common/raids/biological_raids.txt.

The after body was read from common/raids/biological_raids.txt.

The only scenario payload that could be passed without fabricating an ID was schemaVersion 1.0 with an empty scenarios array.

The exact MCP response was:

~~~text
MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_compare: Invalid input: expected string, received undefined at scenarioSet.id
Too small: expected array to have >=1 items at scenarioSet.scenarios
~~~

The comparison therefore did not reach a native raid evaluator because the service requires a scenarioSet.id and at least one scenario, while the baseline produced no genuine scenario IDs and the parent explicitly prohibited inventing them.

No comparison ID, before or after analysis ID, comparison artifact, scenario hash, source revision, ranking, matrix, timing result, or modifier trace was emitted.

The earlier baseline inspect evidence remains the exact route blocker: all four raid source scans reported no weighted raid surface, and the generic direct_random probe returned identifier_not_found with zero candidates and no available native raid adapter.

The current inline inspect additionally shows that the generic decision_ai_will_do route can enumerate four raid names, but that route is not a native raid outcome or success_factors analysis and was not substituted for the requested raid comparison.

## Scenario, pool, and conclusion status

No named before/after scenario family exists for this repair, so no scenario ID, scenario hash, or analysis ID is claimed.

The native outcome set would be success, critical, disaster, and failure for each raid type, but the installed MCP does not expose that pool or the actor, target, preparation, unit, interception, equipment, readiness, and target-validity inputs needed to evaluate it.

The raid ai_will_do choices are a separate score race over valid raid and target choices and require a complete competing pool; the generic four-name inventory is not sufficient evidence for that race.

Native raid success probability, critical/disaster probability, AI rank, target selection, dominance, starvation, repetition, cadence, cooldown, sequence, and exploit-risk conclusions are unresolved.

The only exact conclusions are that all 22 repaired fields now expand back to the archived source tokens with the same values and that the installed probability route cannot produce a native raid before/after result for this surface.

No probability evaluate, sweep, render, simulate, or sequence call was made after the compare blocker because no native raid candidate surface, genuine scenario set, or analysis ID existed.

No simplification or unapproved fallback was used.

## Parent handoff

The parent can use this report together with the repair manifest and archived bodies for native launch parser verification.

The parent should treat the source transformation as exact and the probability result as unresolved until a native raid adapter and a genuine scenario contract are available.
