# Event 093: validation report

Date: 2 October 2026.

## Result and evidence boundary

**The expanded design is written. The full specialist-driven implementation and validation workflow is not complete.** The supplied source set was read fully, the requested gameplay phases were developed in 18 specification parts, and selected proposed rules were checked with a standalone Python reference model. No HOI4 implementation, engine execution, specialist subagent execution, final media production, or independent completion audit took place.

The synthetic suite ran **56 tests with 0 failures, 0 errors, and 0 skips**. Its success applies only to the reference model and assertions in the delivered test file. It does not prove that the game engine can implement the design, that an actual map has been partitioned correctly, that the AI behaves as intended, or that the numerical balance is good.

## Executed synthetic tests

| Group | Tests | What was exercised |
| --- | ---: | --- |
| Geography | 8 | Longitude wrapping, half-open boundaries, equal arc sampling, represented land majority, deterministic ties, and invalid input |
| Frozen weights | 7 | Normalization, proportions, immutable snapshots, duplicate-state protection, zero-industry handling, and rejection of duplicate identifiers |
| World-end readiness | 12 | Both crowns' independent thresholds, strict Chaos above 1000, political eligibility, joint consent, confidence, stage, scenario ownership, and sustained readiness |
| Civil-war aid | 7 | Promised versus delivered aid, earning threshold, minimum component delivery, oversupply limits, and invalid contracts |
| Regional projects | 9 | Population and state-count tiers, region-size rejection, recent-conquest adjustment, composed speed factors, duration rounding, and minimum duration |
| Transactions and ownership | 13 | Actual-paid refunds, no repeated refunds, nonrefundable components, ownership versus occupation, native-core consent, protected homelands, receiving sphere, and claim provenance |

The tests use synthetic values and simplified functions. They do not import HOI4 files, issue game commands, call probability MCP tools, or inspect a save. The gameplay specification remains the design authority. If the model and prose disagree, the disagreement must be resolved explicitly rather than treating the test as engine truth.

Run the suite from this folder with Python 3.10 or newer:

```bash
python 093_treaty_of_tordesillas_restoration_validation_tests.py --json 093_treaty_of_tordesillas_restoration_validation_results.json
```

The standard library is sufficient. The test command does not require a network connection or game installation.

## Executed package checks

The delivered package check results record verification of 18 consecutively numbered parts, six standalone prompts, the goal prompt's 3500-4000 character bound, nonempty package files, local Markdown link targets, and the source manifest against the supplied extracted files. They also check authored Markdown for the planning skill's prohibited em dash and semicolon punctuation. The preserved original user brief is exempt from editorial alteration.

The goal prompt has **3956 characters without its final newline and 3957 including that newline**. The 18 main specification parts contain **25,354 whitespace-delimited words**. These are counts, not quality or completion measures.

The source audit matches all **46 supplied text files**, including **20 role definitions**, and **14,519 lines** to their recorded byte hashes and continuous read ranges. Hashes and range records establish identity and declared coverage, not independent proof of comprehension. The reading report distinguishes the actual reading from these mechanical checks and corrects the earlier mistaken count of 45.

The ZIP is checked for a single intended top-level folder, safe relative paths, expected entries, and a successful CRC test. The package inventory records byte lengths and SHA-256 values for its other files. The inventory excludes its own checksum to avoid a recursive checksum claim.

## Main-agent review

The author's consistency pass is documented separately. It corrected cross-sphere subject credit, prevented duplicate integration credit for already-cored states, clarified frozen world-end weights, preserved other sources' claims, and kept ownership distinct from occupation. It also preserved separate political consent and relationship history instead of replacing those rules with a numerical Confidence test.

This pass was performed by the same author. It is not independent specialist review.

## Required checks not performed

**Actual subagent runs: 0.** All 20 provided role definitions were read and mapped to relevant work or a reasoned non-applicability. No callable launch route was available. The handoffs in the role execution map are instructions for future real execution, not evidence that a specialist ran. The required independent improvement-loop and completion reviews remain open.

**Installed-game and HOI4 MCP checks: not performed.** Missing evidence includes the actual map projection and state geometry, live Spanish Civil War identities and transitions, native focus-tree collisions, the installed Anarchist Spain coring benchmark, exact script support, AI probability tools, technology inspection where applicable, multiplayer, save/reload, GUI and focus rendering, actual cost/debit parity, performance, and world-end framework integration.

**Linked must-read references: not all available or read.** The project-source protocol was not found in the supplied archive or the attempted searches. The required visual-reference library was absent and its attempted repository path returned 404. Several linked production templates, scripts, installed-game sources, the authoritative workbook, and media reuse records were not supplied or fully inspected. The reading report names these gaps. Full reading of the 46 supplied texts does not close these external requirements.

**Media and final writing: not produced or validated.** The package contains asset plans, research leads, achievement requirements, and writing direction. It does not contain finished icons, event pictures, super-event audio, final selected quotations, or a completed localization set. No audio was listened to, trimmed, mixed, or selected for final use. No asset conversion, in-game consumer wiring, visual contact-sheet review, or license/reuse approval was performed.

**Game balance: not established.** Numerical parameters are proposed tuning. In particular, faster and less tedious coring is a design target, not a measured comparison against the installed Anarchist Spain system.

## Release disposition

Keep Event 093 at **To Be Reworked**. Do not mark the design as implemented, the specialist workflow as complete, or the missing validation gates as passed. The complete requested creative progression is present without silently dropping a phase for a shorter response. The uncompleted work is the explicitly identified evidence, production, implementation, and independent review scope.
