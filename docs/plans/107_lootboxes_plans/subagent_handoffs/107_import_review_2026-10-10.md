# Event 107 Lootboxes import review and documentation handoff

Review date: 2026-10-10

Disposition: Documentation reconciliation complete for the imported Event 107 package. This review made no gameplay, localisation, GUI/GFX, asset, audio, workbook, or shared-registry changes and makes no gameplay-completion claim.

## Current authority and acceptance basis

The user selected Event 107 Lootboxes, Event 108 Wrestling Tournament, and Event 112 Rise of Cossacks, and released the former Rule 107 hold. The confirmed mapping is in [`docs/specs/shared_identifier_registry.md`](../../../specs/shared_identifier_registry.md); the parent reports the registry and cross-package 107-hold amendments complete and current identifier checks passing. The workbook state last reported by the parent is row 107 `Rule`/`Unavailable` with Type, Chaos, and cluster empty, and 112 `Lootboxes`/`Unavailable`. Workbook/runtime catalog migration remains queued under parent ownership. This review does not alter either row or infer a status upgrade.

The parent explicitly confirmed the core transaction: exactly 50 PP per purchase; five tactile human interactions; one sealed paid pending box; once-only full delivery; fresh reward evaluation for each new purchase; and no resampling on resume, reload, opening, retry, or replay. The accepted broader design also includes every Part 02 reward family and rarity invariant; the three evolutions at 200/400/600 Chaos; finite hidden burden with peaceful recovery; all four achievement routes; and the complete event-owned window/audio package. AI uses the same completion resolver, and humans keep freedom to delay/resume without a new timeout or balance rule.

The read-only probability review at [`107_108_probability_review_2026-10-10.md`](../../108_wrestling_tournament_plans/subagent_handoffs/107_108_probability_review_2026-10-10.md) cites offline Decision modding lines 383–386 and vanilla `common/decisions/FRA.txt`, line 56, where `FRA_communist_civil_war_decision` uses `fixed_random_seed = no`. This is the verified syntax/placement when the Lootboxes sampler runs through a repeatable native decision. A different sampling route requires its own current-reference check. Do not change weights to solve the RNG issue.

That auditor reports that the illustrative rarity equations normalize and preserve their stated order. It does not certify complete recipe or omen pools, engine weight precision, or the Chaos/cadence functions. Numeric checks remain with `chaosx_ai_probability_auditor`; this documentation review did not repeat them or edit weights.

The earlier import receipt and review disposition are preserved in `docs/plans/107_lootboxes_plans/imported_review/`. Their approvals, GitHub source revision, source-read ledger, and tool-availability statements are historical author-reported evidence, not fresh acceptance or current checkout findings. The archived review reported no open planning addendum and recommended closure; parent review still decides which imported expansions become accepted design. The current gameplay source/root scan remains with the parent.

## Source-of-truth map and document dispositions

`docs/specs/107_lootboxes_specs/README.md` is the current package authority map for the user-selected identity, parent-reported catalog state, accepted core, unresolved proposals, and archive links. Parts 01–06 remain the design source, but only the claims named above have current acceptance. The current `AGENTS.md` and the skills that own each surface control mutable workflow.

| Document | Disposition | Reconciliation and remaining status |
| --- | --- | --- |
| `README.md` | Reconciled as current source-of-truth map | Records the user-selected IDs, parent-reported workbook rows, displaced Rule/107 and Lootboxes/112 identities, accepted core, unresolved expansions, archive paths, and absence of a gameplay claim. |
| `01 - Event Identity and Core Loop.md` | `unresolved` except for the accepted core | Kept the 50 PP, five-interaction, sealed pending box, once-only full delivery, and fresh-sample constraints. Marked the imported event classification, Chaos level, and standalone cluster unresolved. Added the conditional RNG evidence and clarified source/runtime proof limits. |
| `02 - Rewards, Probabilities and Evolutions.md` | `unresolved` for exact tuning and provider behavior | Preserved accepted family coverage, rarity invariants, and three evolution concepts. Labeled exact weights, quantities, provider behavior, and probability examples as tuning/verification work; assigned numeric checks to the read-only auditor. |
| `03 - Hidden Influence and Peace Recovery.md` | `unresolved` except for hidden influence and finite recoverable burden through peace | Kept the proposed burden bands, symptoms, exact recovery conversion, action-source adapter, and owner integrations as design proposals. Marked its commit-pinned source links as historical. |
| `04 - Lootboxes Opening UI and Audio Handoff.md` | `unresolved` for exact production rows and native timing | Preserved accepted full-window, tactile sequence, rarity reveal, receipt, fallback, and physical-audio scope. Detailed dimensions, source assets, and runtime timing remain unverified; optional MCP/live evidence is not a source-completion gate. |
| `05 - Decisions, AI and Integration.md` | `unresolved` except for accepted purchase/RNG, shared-resolver, and timing constraints | Linked the confirmed registry mapping and recorded the still-queued workbook/runtime catalog work. Detailed AI reserves, cadence, contribution adapters, and other integrations remain proposals. |
| `06 - Achievements and Validation.md` | `unresolved` for exact threshold/timing values | Preserved the four accepted routes and multi-condition design. Added `LB-T09` for fresh sampling on each new purchase and `LB-T10` for matched immediate-AI/delayed-human completion through the common resolver, with no timeout or balance change. |
| `107_lootboxes_coding_prompt.md` | `accepted and queued` as a future prompt; embedded expansions remain `unresolved` | The parent asked to preserve necessary production prompts. It now requires acceptance filtering, parent-owned ID migration, auditor-owned numeric work, bounded MCP use, and the fresh-sample/no-resample rule. |
| `107_lootboxes_goal_prompt.md` | `accepted and queued` as a future prompt; embedded expansions remain `unresolved` | Refreshed as a compact parent-accepted-scope entry point. It is 3,927 characters, within the required 3,500–4,000 range. |
| `107_lootboxes_decision_mission_prompt.md` | `accepted and queued` as a future prompt; expanded AI/decision plans remain `unresolved` | Retained the prompt with parent-acceptance and migration conditions, auditor-owned numeric review, current RNG citation, and no optional-tool or live-game gate. |
| `107_lootboxes_achievement_prompt.md` | `accepted and queued` as a future prompt; the four designs remain `unresolved` | Preserved the self-contained candidate achievement handoff and made implementation conditional on parent acceptance. |
| `107_lootboxes_asset_prompt.md` | `accepted and queued` as a future prompt; production rows remain `unresolved` | Preserved the candidate asset rows and production scope, linked current owner skills, changed processor paths to canonical `.claude/skills`, and bounded optional GUI evidence. |
| `107_lootboxes_implementation_handoff.md` | `superseded` for current workflow by this report and current owner skills | Kept the planning-session record, added a superseded-workflow notice, changed its identity step to the user-selected target/parent-owned migration, and reframed MCP routes and behavior questions as optional evidence choices. Historical tables remain available as context. |
| Four files in `docs/plans/107_lootboxes_plans/imported_review/` | Preserved historical records | `107_lootboxes_package_manifest.json`, `107_lootboxes_review_dispositions.md`, `107_lootboxes_source_and_decision_receipt.md`, and `107_lootboxes_source_coverage.json` were not edited. Their original bytes still match the supplied import hashes. |

The future prompts are preserved because the parent explicitly requested them. Their `accepted and queued` disposition applies to keeping them as handoff artifacts, not to all design requirements repeated inside them. Those requirements remain unresolved unless parent acceptance is recorded.

## Contradictions and exact corrections

- The package used 107 for Lootboxes while the parent-reported workbook still lists Rule at 107 and Lootboxes at 112. The user decision and current shared registry resolve the identity mapping; the parent reports registry/hold amendments complete and identifier checks passing. Workbook/runtime catalog migration remains queued, with no workbook change here.
- Part 01 imported `Minor Fire-Once`, Chaos level 1, `Standalone`, and `To Be Reworked` as if they were current facts. The README now records that only the explicitly accepted core is accepted; those metadata claims remain unresolved against the current workbook's reported `Unavailable` status.
- Part 02 originally named Fuel Crisis as Event 109. The parent's current catalog/source scan identifies it as Event 114, `Unavailable`, with no Event 114 root. Part 02 now targets 114 as a proposed integration and distinguishes it from implemented behavior.
- The README previously pointed at source/decision receipts and manifests in the spec folder, but the import placed them in `docs/plans/107_lootboxes_plans/imported_review/`. Those references now point to the archive and distinguish historical evidence from current findings.
- The old implementation handoff described its MCP availability and routing map as current and included broad native evidence gates. It now carries a superseded-workflow notice; current owner skills and the one-initial-call/one-useful-corrected-retry rule govern. The optional routes are not completion gates, and live-game execution/request/wait is outside agent work.
- The package lacked an explicit per-purchase RNG condition. Parts 01, 02, and 05, the coding/decision/goal prompts, and Part 06 now state that each new paid purchase evaluates and seals its reward selection once. The verified `fixed_random_seed = no` syntax is conditional on the sampler being inside the repeated native decision. `LB-T10` also covers immediate AI and delayed human completion without changing player timing freedom.
- The old review's rarity arithmetic must not be read as certification of actual gameplay odds. The current handoff limits that result to the illustrative equations and records the incomplete recipe/omen pools and Chaos/cadence functions.

## Duplicates, historical records, and prompt status

Part 06 and the achievement prompt repeat the full four candidate definitions. That duplication is retained because the prompt is a self-contained future handoff; Part 06 remains the design source. Part 04 and the asset prompt also overlap on visual families, while Part 04 remains the design contract and the asset prompt remains the production handoff. No design content or historical file was deleted.

The older implementation handoff remains readable as historical planning material, but its mutable tool and approval guidance is superseded by the current skills, README, and this handoff. The four imported receipts/manifests remain byte-identical and retain their original claims. The single current report is this file.

## Hard wraps and meaningful checks

The prose was kept sentence-complete across physical lines; tables, lists, code, and blockquote structure were preserved. A targeted wrap check found no likely mid-sentence prose breaks in the active package.

All local Markdown links in the 13 active package files resolve after this handoff is added. The four archived records were hashed against both the import baseline and the original extracted files; all matched. The goal prompt length was checked at 3,927 characters. No gameplay tests, MCP calls, workbook inspection, live-game run, asset inspection, or numeric audit were performed by this documentation review. The parent owns the current source/root scan and workbook evidence.

## Parent-owned open decisions and next handoff

The accepted Event 107 identity and high-level mechanics are settled. Before implementation, disposition the remaining event classification and Chaos level; permanent-access and recipient details; exact reward recipes, quantities, weights, and provider support; burden/symptom/recovery tuning and source adapters; AI reserve/cadence values; achievement thresholds; and GUI dimensions/timing and exact asset sources. The accepted Fuel Crisis integration target is Event 114, but the catalog marks it `Unavailable` and the parent reports no root. Workbook/runtime catalog changes remain queued, with no status upgrade authorized here. Do not infer additional design approval from the old ZIP or its receipts.

Skills used: `chaos-redux-event-planning` and its specification-delivery reference, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-scripted-gui`, `hoi4-ai-strategies`, and `hoi4-diplomacy-war` (for the relevant AI-score and peace-source distinctions).
