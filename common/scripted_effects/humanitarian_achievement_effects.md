# Exact corridor achievement receiver contract

This note documents the exact corridor receiver contract and the tracked famine achievement recorders.
Both helpers run in the actual receiving COUNTRY.
Protection saves that scope as regular `humanitarian_achievement_gate_receiver`; the three nested origin/front/generation reads use that receiver, not ambient ROOT.
Terminal cleanup initializes the country and saves its receiver locally before its two nested origin/generation reads, so it never relies on a target from an earlier chain.
PREV remains the exact calling origin STATE at cleanup, and the current generation must match the receiving country's active gate record before any terminal arrays are archived.

Protection requires actual conserved zero-death full qualifying-cohort transfer and exact destination owner/route identity; consent alone creates no protection.
The protected-cohort set rejects repeated receipts.
Automatic ordinary passage records that real proof before terminal cleanup archives the qualifying/protected/resolved arrays and clears active arrays.
No achievement threshold, reward, source ledger, art, registry or full-term qualification is changed.
The byte-faithful pre-edit file and exact SHA-256 are recorded in the prospective reception validation-baseline manifest.

## Tracked blockade and extraction country

`humanitarian_achievement_record_blockade_relief`, `humanitarian_achievement_record_blockade_wasteland`, `humanitarian_achievement_record_blockade_recovery`, `humanitarian_achievement_record_extraction_suspended`, `humanitarian_achievement_record_extraction_recovery`, and `humanitarian_achievement_record_alternative_logistics` run in the COUNTRY being credited, entered from the exact calling STATE through `OWNER` or `CONTROLLER`.
At entry `PREV` is that state.
Inside the recorders' nested `PREV = { }` state checks, `PREV.<tracked field>` refers back to the credited country, even when ambient `ROOT` is another controller or the runtime host.
The state ID and current generation must both match that country's tracked attempt.
Relief, recovery, suspension, and alternative-logistics conditions remain binding.
These readers grant no food or population and do not change achievement thresholds.

`humanitarian_achievement_record_blockade_concealed_mortality` uses the same COUNTRY-from-STATE contract.
`famine_apply_mortality` calls it only after a positive measured famine population loss in a concealed tracked blockade state, once for OWNER and once for a different CONTROLLER.
The recorder checks concealment, tracked state flag, exact state ID, and generation before setting `humanitarian_achievement_blockade_concealed_mortality` on the matching country.
The actual Break the Blockade trigger reads this disqualifier.
`humanitarian_achievement_record_blockade_start_actor` clears it at the start of the country's next tracked generation.
No disqualifier is created by an attempted zero-loss mortality pulse, an unrelated state, or a stale generation.
The older `famine_achievement_blockade_concealed_mortality` condemnation output is separate and cannot replace this achievement flag.
