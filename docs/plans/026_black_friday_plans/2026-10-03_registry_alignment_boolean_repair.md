# Event 026 registry alignment Boolean repair

Disposition: EC-A01 verified and closed for its bounded source defect, with EC-A02 achievement proof still unresolved.
Acceptance basis: the original full cost-source goal and the completion auditor's concrete EC-A01 finding in `subagent_handoffs/2026-10-03_exact_cost_source_completion_audit.md`.

The quote producer wraps the three source-array equality predicates in an explicit `AND` inside `NOT`.
HOI4 `NOT` is NOR over sibling triggers, so an unwrapped sibling list did not reject one or two mismatches.
The shared actual-source interpreter and both RSA source models now implement NOR.
This corrects the test model as well as the production rejection gate.

The shared suite adds eight truth-table checks for NOR and explicit negated conjunctions.
It also checks all 26 nontrivial short/long/equal combinations for the three data arrays, plus short and long source-ID arrays.
Each mismatch runs through the producer, effect frontend, and Black Friday bridge, then the shared affordability gate, for 84 rejection checks.
Malformed quotes remain invalid and cannot be paid.
The 434 rational-oracle quotation cases and 56 standalone quantizer cases still pass.
Both RSA suites pass their existing 295 and 30 cases with corrected NOT semantics.
The independent completion auditor reran those suites and the nine caller scenarios, verified all eight Boolean cases and 84 rejection cases, and checked 256 guard combinations separately.
Its source fingerprint matches `9f5831663708c2b25d2a25ec27b2c047cbeb4fbb52ecb15c772d6fcc62110101`.

The existing nine outer-caller scenarios initially failed after the source integration commit because their preservation comparison used moving `HEAD`.
They now use immutable before revision `f32aaa4b7acc3621fcb5375743b63bfc7a81f739`, and all nine pass again.
This is a test-evidence correction, not a reset or gameplay patch.
The original exact-result JSON remains evidence for its recorded pre-repair source hashes and is not represented as current NOR validation.

Reference: offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, flow-control table at lines 337-345, specifically NOT/NOR at line 341.
The installed Boolean dispatch is not exposed as an independent trigger-documentation section, and the current reference MCP route has returned no usable cited section.
No new domain limit, quantum change, native operation, periodic scan, or event enablement is introduced.
Native, full all-owner registry, UI/debit, save/reload, multiplayer, and failed MCP gates remain unresolved.
This repair does not close the separate achievement proof finding.
