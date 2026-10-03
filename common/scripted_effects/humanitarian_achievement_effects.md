# Exact corridor achievement receiver contract

This note documents only `humanitarian_achievement_record_gate_protection` and `humanitarian_achievement_record_gate_terminal_cleanup`; other helpers in the file retain their existing contracts.
Both helpers run in the actual receiving COUNTRY.
Protection saves that scope as regular `humanitarian_achievement_gate_receiver`; the three nested origin/front/generation reads use that receiver, not ambient ROOT.
Terminal cleanup initializes the country and saves its receiver locally before its two nested origin/generation reads, so it never relies on a target from an earlier chain.
PREV remains the exact calling origin STATE at cleanup, and the current generation must match the receiving country's active gate record before any terminal arrays are archived.

Protection requires actual conserved zero-death full qualifying-cohort transfer and exact destination owner/route identity; consent alone creates no protection.
The protected-cohort set rejects repeated receipts.
Automatic ordinary passage records that real proof before terminal cleanup archives the qualifying/protected/resolved arrays and clears active arrays.
No achievement threshold, reward, source ledger, art, registry or full-term qualification is changed.
The byte-faithful pre-edit file and exact SHA-256 are recorded in the prospective reception validation-baseline manifest.
