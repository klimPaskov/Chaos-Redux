# Event 026 South Africa purchase baseline

This directory retains the physical pre-adapter source used for the five-action comparison.
The authoritative decision baseline is `012_africa_rsa_decisions.txt`, copied before the purchase adapter with SHA-256 `40283784e0d0ea091bd96c96c46f0155ec01e911091b2b20a0389ac5e1d696cc`.
It has 217 physical lines and remains unchanged in the working tree.

The 2026-10-03 raw-blob review found that Git's text filter had changed the committed decision blob to SHA-256 `0f26091f29c6a8deb681a51c1c4521e0ba03a7921d32c6069b3b55619ff52dbe`.
The original physical file was intact, so source-model comparisons against that file remained valid.
The filtered commit was not byte-identical evidence and must not be used as the archived hash identity.

The repair promotes the intact source using `git hash-object -w --no-filters` and a path-specific isolated-index entry.
A narrow `.gitattributes` rule disables line-ending conversion for this snapshot directory.
The raw committed decision blob must match the recorded source hash without text decoding or checkout filters.
Supporting nested source copies are retained as comparison material and are not individually certified by this decision-baseline record.
This baseline identity repair establishes no probability, engine, or live-game result.
