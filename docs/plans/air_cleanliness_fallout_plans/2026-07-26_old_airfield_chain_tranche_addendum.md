# Old Airfield chain tranche addendum

## Decision

Implement one manually reviewed Latin America and Caribbean regional chain as the next Fallout-owned tranche. The chain is candidate `586`, events `586` through `592`, transaction key `710056`, scheduler route `7156`, route upper bound `7157`, and Event Log history `9162`. It remains dormant until the Fallout scheduler release audit authorizes ordinary issuance.

## Implementation contract

The candidate registry must use the existing Fallout ordinary receipt helpers and must select the lowest eligible native state id. Admission requires a current Fallout country and generation, campaign day 730 through 5999, no conflicting ordinary transaction, one affordable branch, and a qualifying state in `fallout_region.latin_america_caribbean`. The state must be owned and controlled, have the current Fallout identity and Air Winter snapshot, Supply Access at least 18, Reclamation at least 8, Exposure below 75, Disease Pressure below 70, surviving population above 3000, one operational air base below the vanilla cap, and one non-damaged infrastructure level.

Create a dedicated constants file for the four branch ids, exact costs, timing, thresholds, ledger defaults and clamps, result and callback deltas, AI priorities, transaction offsets, and Event Log payloads. Do not add free-standing tuning numbers to effects. The result must use one deterministic equal-weight grade and the callback must use one authenticated delayed score. Payment must happen once after current target and affordability revalidation. A stale receipt, lost target, invalid generation, or unaffordable branch must cancel the exact row and record cancellation provenance.

The event file owns human and hidden AI openings, result pair, callback pair, and cleanup. The effects file owns ledger initialization, state selection, branch costs, frozen registry, deterministic grading, Deaths, documented building changes, resource deltas, callback memory, and cleanup. The triggers file owns country admission, state eligibility, branch affordability, current registry authentication, and AI branch conditions. A new dynamic-modifier file may contain only modifier fields confirmed by the engine documentation and each applied modifier must have localisation.

Wire the dedicated report card through a Fallout-only interface sprite and the runtime DDS path. Add Event Log name, detail, choice, result, callback, and cancellation routing for history `9162`. Update the source spec index, add a proof file after implementation, and update the event catalogue workbook through the spreadsheet worker before exporting CSV. Do not activate the scheduler, create bilateral relations, spawn units, add recurring decisions, or claim release-floor credit.

## Review gates

Before gameplay edits, scan the repository for collisions on ids `586` through `592`, candidate `586`, transaction `710056`, route `7156`, route upper bound `7157`, and history `9162`. After implementation, review every event block manually, check the branch and callback outcome paths, verify the exact state target remains authenticated through delayed delivery, and confirm cleanup cannot double-release a row. Record the no-HOI4 runtime boundary in the proof.
