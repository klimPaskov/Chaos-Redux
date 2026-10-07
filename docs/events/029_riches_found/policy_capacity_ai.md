# Riches Found opening policy and construction capacity

The opening policy's concession weight includes a shared construction-capacity adjustment from `riches_found_ai_weight.policy_poor_concession_add`.
It applies only while `num_of_civilian_factories < riches_found_foreign_interest_threshold.weak_factory_count`, currently 20.
The adjustment is 160, preserving viable public development and state extraction rather than making concession selection certain.
The acceptance basis is `RF_POLICY_03_POOR_MINOR` in the human-authorized AI scenario specification: a poor minor with a valid investor should prefer limited concession or infrastructure access over development it cannot build quickly alone.

## Baseline, sweep and owner patch

The required probability inspector found the complete five-option root pool.
The auditor evaluated all four named policy scenarios individually with typed mine/controller inputs after a four-case batch timeout.
The frozen poor-minor baseline weights were `a/b/c/d/e = 250/125/215/90/15`, so Public Development incorrectly led Concession Economy.
The baseline capacity sweep at 19, 20, 21 and 30 factories confirmed that the old adjustment did not establish the intended preference.
The owner changed only the shared adjustment from 80 to 160.
The current poor-minor weights are `250/125/295/90/15`, giving the intended order: Concession Economy, Public Development, State Extraction, Militarized Mine, Predatory Extraction.
At 19 factories the adjustment applies; at 20, 21 and 30 it does not.
The strict threshold is preserved and no unsupported comparison operator is introduced.

The full event text is unchanged, SHA-256 `c7a509e56ed0131c0d4e85fdb759c39d46e58d1ae0320c2ee05a0a65e0daa94b`.
Frozen/current constant-file hashes are `c478961a3f1024859b7bca1752c02e26a50f61874b798d51b85ba04770039c71` and `53d8ddf3bb195ff49fbad9a1ea00cc1351feed80c4e48a66f2dd04da44ed6da7`.
The source delta contains no other constant or gameplay change.

## Same-scenario comparison

The auditor ran `hoi4.probability_compare` for the same four policy IDs and input hashes.
Because the live route lacks a verified frozen multi-file constant overlay, both comparison inputs use the complete hash-matched event text with exactly one static reference expanded to its verified before/current value.
This is an explicit, source-equivalent analysis projection, not a replacement runtime implementation, raw-source snapshot claim or engine test.
All other references remain unchanged and resolve identically.
The retained request contract, original and projection hashes, typed scenarios, actual returned results and comparison attribution are in `docs/plans/029_riches_found_plans/evidence/2026_10_07_policy_poor_concession_compare.json`.

| Named scenario | Comparison result |
| --- | --- |
| `RF_POLICY_01_STABLE_DEMOCRACY` | Complete five-option pool, zero unresolved candidates, zero changes |
| `RF_POLICY_02_AUTHORITARIAN_MAJOR_AT_WAR` | Complete five-option pool, zero unresolved candidates, zero changes |
| `RF_POLICY_03_POOR_MINOR` | Complete five-option pool, zero unresolved candidates, concession raw delta +80 and rank improves from second to first |
| `RF_POLICY_04_COLONIAL_OCCUPIER` | Complete five-option pool, zero unresolved candidates, zero changes |

The poor-minor comparison is `probability-dff5f975cf48efeb2c8c2e5b`, source revision `8b6081c14fc5d3259f292d33dd8edfd031d6fac3c896c27510f3a922e1e5bc25`, scenario hash `9887d51b6ffe164527079672b14afdbca2caffcb96e4e7b738f62b8ca5ce99b2`.
Its returned trace removes `add:80`, adds `add:160`, and ends at concession weight 295 rather than 215.
The other raw scores are unchanged; normalized event-option shares change only as the complete pool total changes.
These are conditional event-option shares, not event-firing or decision-click probabilities.

## Remaining acceptance limits

The wartime strategic-partner ordering and material predatory weight in a non-desperate war remain unresolved.
The colonial fixture still lacks the required occupation-duration-sensitive ordering.
This patch does not resolve either finding or substitute the poor-minor result for them.
The current sweep's point-level ranking reverses at the 19/20 boundary although the analyzer's `rankReversals` summary is empty, and that summary mismatch remains recorded in the probability audit.
Remaining decision, evolution, incident and recipient/state-pool scenarios still require their full workflow.
No live-game execution or Event029 completion is claimed.
