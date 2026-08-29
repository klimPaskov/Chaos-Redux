# Famine and Migration Current Probability Evidence

Status: post-separation mandatory HOI4 MCP evidence. This is not a numeric balance certification because the available scenario fixtures do not resolve live HOI4 trigger state.

> **Historical density-patch trace (2026-08-26):** The migration visibility correction was inspected against the then-current 18-action pool at source hash `ef14ce12e61338d733440d0fdc85bc1ede5a883b767cc7fe7ef48edf7327d779`. Analysis `probability-320ed8c0ab9e18a15234344a` returned `PROBABILITY_ANALYZED_PARTIAL`, `comparisonChanges=0`, and 94 unresolved items, but both comparison sides resolved the same intermediate source. It is retained only as a partial score trace and is not valid before/current evidence.

> **Typed-scope probe (2026-08-26):** A focused current-source evaluation of `migration_voluntary_return` attempted to bind `FROM` through the scenario event-target map and supplied the relevant flat facts. Analysis `probability-fd3c283552027c3027e6d626` still returned `PROBABILITY_ANALYZED_PARTIAL`; the remaining unique unresolved paths were `FROM` and the compound `hidden_trigger`. The war modifier and other flat factors resolved. This narrows the blocker to the installed scenario adapter's inability to bind the special decision target and compound hidden eligibility trigger, rather than missing fixture effort or absent source AI.

> **Current-evidence boundary (2026-08-26):** The authoritative latest score evidence is the flat-fact recovery in `subagent_handoffs/final_flat_fact_probability_0826.md`, read together with the distinct-source comparison in `subagent_handoffs/distinct_probability_recovery_0826.md`. Final source inspection found complete declared lists of 10 famine and 18 migration candidates. Genuine temporary-before versus frozen-current comparisons completed under fixed named scenario hashes, then the temporary runtime files were deleted. Current flat-fact matrices reduce unresolved rows from 23 to 15 for famine and from 77 to 60 for migration, but exact named-scenario certification remains blocked by special `FROM`, scoped and compound triggers, and incomplete destination, opposition, and relief-donor registries. Older evidence below is retained for provenance and is superseded wherever it conflicts with this boundary.

## Current flat-fact recovery

The current-source famine matrix is analysis `probability-ee3074ce9bf0db80f330bf06` at scenario hash `638129d61ba378c2ecf61a438d17216d7a2dc976dcbd2e3e92b5e552e99fca6e`. It covers the four named famine scenarios and 40 candidate rows, with 15 unresolved rows and two information diagnostics at MCP source hash `729c115b88697b86b2e70988fc1b093361a9220c673a94f2451b68f7613a5e74`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e860826d78756ed13c6c7e608cb2778834fae16206807e319e4892bca3e23f2d/339223bb1fe22ee11a649ed0e6ae3417667561d1ec0eaa172215868d8d1c2cc8/probability-ee3074ce9bf0db80f330bf06.json`.

The current-source migration matrix is analysis `probability-967ff4fb246a0c8c86c5eeb4` at scenario hash `8c8eb15e528b68603c943cfcf1b47708c56bd1e792b95059293dd62c1aa1da23`. It covers the eleven named migration scenarios and 198 candidate rows, with 60 unresolved rows and seven information diagnostics at MCP source hash `84fa372dc07e66a1b07c299486834ce3112db3b03b8ecae2e8ca2022f014665a`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95f14549a35b5e562b9bb71d9ccd9255232396329e62f6080eaabc8d722260e7/049cb1d0bc519eda59b00e99c4af4c59c8f7c93aaa0b3d3afd1bf7a56953d6ec/probability-967ff4fb246a0c8c86c5eeb4.json`.

The bounded `famine_emergency_imports` probe, analysis `probability-acdb8db6e41121b5801a5d80` at scenario hash `0ab0466d4da6f3950206156def98d561a522717a17db93575af37fe7a2bb195e`, resolves the supplied flat country facts and isolates the special `FROM` target as its one unique unresolved class. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebd1c9608f8ff8b85df55c2527689407f216bf1781a4680c3e88ba0bc9782f92/441ef293c1c795e1194c61fd46486ee9ecfe3fd3cdbc432f56c6720ca9a6bec9/probability-acdb8db6e41121b5801a5d80.json`. Follow-up analysis `probability-ad1c19a77bd881519d917f59` accepted `eventTargets = { FROM = "state:1" }` under scenario hash `4774fe73c9de6d07eb939c91c6ca51eed96fe6490b8471fbc146423da4f4333a`, but still did not bind `FROM`. Schema acceptance therefore is not treated as scope resolution.

These matrices are score-only partial evidence. They do not certify exact eligibility, ordering, normalized probability, timing, rank reversal absence, dominance absence, repetition safety, exploit safety, or complete dynamic target pools. The isolated auditor found no gameplay or source-weight patch warranted by the remaining unresolved rows.

## Weighted surfaces

The current weighted surfaces are:

- famine decision and mission `ai_will_do`;
- migration decision and mission `ai_will_do`;
- migration destination selection;
- famine foreign-relief donor selection;
- humanitarian corridor response scoring;
- catastrophic-famine opposition custom pool.

Deterministic disaster/bombing pressure submission and sparse registry cleanup are not weighted candidate pools.

## Inspect evidence

`hoi4.probability_inspect` discovered both separated decision sources. The installed `decision_ai_will_do` adapter returned no candidates for these files, while `mission_ai_will_do` parsed the actual decision and mission candidates. That adapter mismatch is recorded as a tool limitation rather than treated as absence of AI.

The opposition and relief custom-pool sources were inspected separately. The destination pool and corridor scores were included in the migration source inspection/evaluation.

The earlier parallel inspection snapshot used famine hash `ee8ebb8aab094f6cadab6ca0a64b1736e945c363425285d2f47910a516b091bb` and migration hash `d1f041682e94cb10e8fe0117820eb3c9b1fc96e590ec7192bf68d689c9d23d82`. It remains historical source evidence only and is superseded for current counts by the isolated inspections in the next section.

The removed gates were unweighted visibility conditions, so the candidate scores and constants did not change. They restore simultaneous AI access to both mechanics when famine and migration coexist. The named evaluations and HEAD comparisons below remain partial for the same typed-fixture limitation.

## Superseded incident-layer probability claims

Earlier wording about `famine_incident.1`, `migration_incident.1`, `event_option_ai_chance`, incident option pools, normalized incident percentages, or nested incident event targets is superseded.

The deleted `events/famine_incidents.txt` and `events/migration_incidents.txt` files and their constants are deliberate. `famine_register_initial_incident` and `migration_register_initial_incident` are accounting and presentation seams only; they do not create event objects, event IDs, event-pool entries, event-log rows, random events, or pacing pulses.

No current famine or migration event-option pool exists, so the deleted layer is not a probability blocker and no earlier incident-option result is a current balance claim.

## Current direct source inspection

The final isolated `hoi4.probability_inspect` call for `common/decisions/famine_decisions.txt` used the `mission_ai_will_do` adapter and returned `PROBABILITY_SOURCE_INSPECTED` with source revision `7caa56bc69922e4ac74e494d19a279b8816aa78eee4be8be7a7052187e98f579` and MCP source hash `729c115b88697b86b2e70988fc1b093361a9220c673a94f2451b68f7613a5e74`. It exposed the complete declared pool of 10 candidates and six required inputs; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acd719d701e14b9e6b0c1c7b09f887386c7c4e65674f6052b698e5328fdd8aa0/7b911a370582d4a26ad301091bd644afda08efb62b1b52ef2161bbdf9656fb0e/probability-inspect-729c115b8869.json`. The frozen local file SHA-256 is `966b31a3e49d5a0ad11e3483997e5f0567d0d83837b3c074fa293766ea4cc491`.

The corresponding final migration inspection exposed the complete declared pool of 18 candidates and eleven required inputs at MCP source hash `84fa372dc07e66a1b07c299486834ce3112db3b03b8ecae2e8ca2022f014665a`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/606987e49cdca6e1b873ad1475cf70184f31259343d40fd89b243358a5c5056b/6a152f721c5f863384eb887b619ea2e9a6ec25a77209e582a74c74e02801f12f/probability-inspect-84fa372dc07e.json`. The frozen local file SHA-256 is `bd748779a4eb8a0037215a58be3f92597973f22be9e668a35efdc3cef9a3a6a6`.

The current destination custom-pool inspection found four live declared entries but could not discover the dynamic neighbor candidates. It returned an incomplete registry at source hash `8169d9fb45fde0b399097d3f252c64fe6be7ba7e21a1e5952531ea8b34ddc65d`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a96188c86331f555ef4b3f706f85901555ec6e1f49b823694cc61e6599a7a368/2767d7dd3053467a2d425326ee7de011247498bd0dd14e7415ab86e4d41a82f2/probability-inspect-8169d9fb45fd.json`.

The current famine opposition custom-pool inspection found seven declared channels but remained an incomplete custom pool at source hash `4040a2f554f24521026236dad3316f209169a510b184103f4b81b1b437f1f22e`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69af1b8f8a18e350c14441c83bf37f47fa586d71efd6d103480ecf042b7d81bf/de9d458d8f21ab38d486f7b0e6837dbfd4acb99d7e1add93d4f08a39bce2f219/probability-inspect-4040a2f554f2.json`.

The current famine relief-donor inspection remained an incomplete dynamic registry with zero discovered candidates at source hash `7ea4b17392347739c4cb1630752666624bb8f489d2c8aeba915c80d29f060a8`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38cc7f020663eaaa50b9d75603e6087e82cb7af6951d11a5829cd01e93ec4cd6/9fca70e4816ea62de5ca83d6646863f5696601db546f7f6644b48a13b6e88b5a/probability-inspect-7ea4b1739234.json`.

The final owner refund-only patch changed the decision source files after these direct inspections. The current famine decision file hash is `bb8d664fb7aac3dff93321b2abc25999f8441d5760979d851b041931df4d12a2`, and the current migration decision file hash is `6cfad3a2ba346576e012313f0ac0efcb9f120b8250c40f489ad0f627faedf1a6`; the inspection artifacts above predate that patch and are bounded structural evidence. The later density-patch inspection, same-scenario comparison, and typed-scope probe are current for the migration source. They establish no modeled willingness-score change from the visibility patch and isolate the `FROM`/compound-trigger adapter limit, but they do not provide complete named-scenario or dynamic-pool certification.

## Historical named-scenario evaluation snapshot

The earlier famine evaluation ran these four scenarios and returned `PROBABILITY_ANALYZED_PARTIAL` with seven artifacts:

- `prob_famine_relief_dense`
- `prob_famine_relief_blocked_island`
- `prob_soviet_extraction`
- `prob_requisition_donor`

The earlier migration evaluation ran these eleven scenarios and returned `PROBABILITY_ANALYZED_PARTIAL` with seven artifacts:

- `prob_humanitarian_border`
- `prob_capacity_exhausted_border`
- `prob_outbreak_reception`
- `prob_nuclear_evacuation`
- `prob_genocide_escape`
- `prob_authoritarian_pushback`
- `prob_destination_selection_internal`
- `prob_destination_selection_persecution`
- `prob_corridor_acceptance`
- `prob_forced_return`
- `prob_integration`

The earlier seven-candidate opposition inspection ran under `prob_opposition_channel` and returned `PROBABILITY_ANALYZED_PARTIAL` with nine artifacts.

All scenario fixtures used an empty state object because no save-state fixture was available to the tool. Eligibility and modifier inputs that depend on live flags, scopes, variables, war relations, routes, or state ownership therefore remain unresolved. The artifacts prove source parsing and trace construction, not the intended quantitative ordering.

## Historical baseline and owner-patch comparison snapshot

The repository HEAD version of the former combined decision source was loaded as the real pre-separation baseline. Its old candidate IDs were mechanically normalized in-memory only so that the comparison route could match candidate identity; no baseline file was written or changed.

An earlier `hoi4.probability_compare` run used the same four famine scenarios for HEAD versus the then-current famine source and returned `PROBABILITY_ANALYZED_PARTIAL` with nine artifacts.

The same earlier route used the eleven migration scenarios for HEAD versus the then-current migration source and returned `PROBABILITY_ANALYZED_PARTIAL` with nine artifacts.

Those comparisons were genuine HEAD-to-current source comparisons for their historical source hashes, but they are not current post-refresh comparisons and cannot prove target dominance, starvation absence, or exact selection percentages.

## Scenarios without a valid weighted model

`prob_relief_donor` cannot be evaluated as a static complete candidate pool because valid donor states are drawn from a live sparse registry and depend on endpoint, stock, relation, capacity, and route receipts. The source was inspected, but no fixed candidate list was fabricated.

`prob_disaster_flight` and `prob_bombing_exodus` are deterministic pressure contracts. They have source-discovery evidence but no normalized probability to evaluate.

`prob_cleanup` is a deterministic registry/transaction sequence, not a categorical or independent-chance selection. An earlier `hoi4.probability_sequence` attempt was rejected because its schema requires transition targets to belong to a declared weighted-pool state and does not accept the system's registry invariants as a pool state. No random weights were added merely to satisfy the analyzer. Cleanup remains a source/transaction audit scenario, not probability evidence.

## AI design evidence that remains source-level

- AI uses the same availability, target, route, capacity, policy, and cost gates as the player.
- Ideology contributes only after safety eligibility and is bounded by the destination constants.
- Persecution, famine, bombing, camps, occupation conduct, contamination, route danger, capacity exhaustion, and forced-return policy can exclude a destination before affinity contributes.
- Zero-total destination or donor pools fail closed; they do not select a fabricated fallback.

These are source facts, not numerical MCP conclusions.

## Independent-auditor route status

The fresh isolated `chaosx_ai_probability_auditor` recovery route completed and its handoff is authoritative. Within that subagent runtime, the only callable analysis surface was the direct HOI4 MCP probability family; it did not expose a nested auditor tool. The completed audit still cannot certify exact eligibility, normalized balance, timing, dominance, rank reversal, starvation, repetition, or exploit safety because the adapter is score-only, typed scopes remain unresolved, and all three dynamic custom pools are incomplete.

Owner-applied weighted changes exist in the final separated sources: famine decisions use famine-owned reception demand and famine-stage factors, migration corridor responses use the migration-owned humanitarian-open policy trigger, and famine relief selection uses narrow migration-owned persecution and reception-policy seams. Source review found no impossible positive choice, raw cross-mechanic read, dominance, starvation, rank reversal, repetition, or exploit defect, but that is not numeric certification.

The source-hash form of `hoi4.probability_compare` remains unsupported, but the accepted path-based recovery supplied materially distinct temporary before files and frozen current files. Famine analysis `probability-4afd69e0e79bd79eefce0d1a` used four named scenarios at scenario hash `90ebda36ce4ae460b3dd64cbefdb6ae5d5ae4f8deadf0da15828cfec35a13739`; it returned `comparisonChanges=0` with 46 unresolved items. Migration analysis `probability-35fd3b50d64d8a2cbbed5af4` used three named scenarios at scenario hash `d0e5281c91db132e22ea8cfa0c4d9373bbe197d251859451641995bc87b43b26`; it returned `comparisonChanges=6` with 134 unresolved items and four informational diagnostics. The six rows are the two corridor modifier changes repeated across three scenarios, not six candidate or balance changes. Provenance ambiguity is closed; exact named-scenario and dynamic-pool certification remain blocked.

Famine comparison artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ee35ac8f350bc2e820ac4e71ba492777a718644d576f6d84ad48eec3e1a1746/d989f58eebde25a1a880569a5c8bb072ad9a291ec76bef52f6f6f25b107a856c/probability-4afd69e0e79bd79eefce0d1a.json`.

Migration comparison artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e18aeed48d51f13834da02e62224082ea671580383a588d501179eb5c3f7b1a/7a2916fce9cb62258856d61c7e7ff5517c423a9ea95ef08259521beb05219349/probability-35fd3b50d64d8a2cbbed5af4.json`.
