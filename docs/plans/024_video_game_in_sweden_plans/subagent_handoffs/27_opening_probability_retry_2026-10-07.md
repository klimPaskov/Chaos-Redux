# Event 24 opening option probability retry

Audit date: 2026-10-07.

Status: bounded opening-surface audit; numeric rankings and option shares remain unresolved. This handoff covers only the AI option weights for `chaosx.nr24.2`. It does not clear Event 24 stage, campaign-balance, pacing, or full probability acceptance.

## Scope and source identity

`chaosx.nr24.1` is the hidden entry/dispatch root. Its current source clears the prefire receipt, initializes the program, and schedules the visible opening event `chaosx.nr24.2` one day later. The three weighted options are `chaosx.nr24.2.a` Controlled Staff Trial, `.2.b` Civilian Commercial Release, and `.2.c` Competitive Officer League. The `.2` event is guarded by `video_game_in_sweden_is_current_host = yes`. This corrects the earlier shorthand that called `.1` the opening option event.

Current physical source hashes match the already committed 2026-10-07 snapshot identities; no new physical source copy was made.

| Source | Relevant identifiers or lines | Physical SHA-256 |
| --- | --- | --- |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\events\024_hearts_of_iron.txt` | `.1` lines 12-36; `.2` lines 39-97; options `.2.a` lines 49-65, `.2.b` lines 66-80, `.2.c` lines 81-96 | `60904703034703c8254f080b0bf63d2cf1829923db29087fe5687385ec09b095` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\script_constants\024_video_game_in_sweden_constants.txt` | opening bases/factors and source thresholds | `11872d5dd1da14b70a3cd231817e7d5c672a10ef46eb05cfc475558c5fefdb78` |
| `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_triggers\024_video_game_in_sweden_triggers.txt` | `video_game_in_sweden_is_severe_campaign_crisis`, lines 452-460 | `e0bfc38415f180643f69e29ba482d43deec996777a74fd760607e419c0262098` |

The crisis helper is true for capitulation, `video_game_in_sweden_supply_crisis`, `video_game_in_sweden_core_loss_crisis`, `video_game_in_sweden_capital_threat`, or stability below `minimum_audit_stability`. The current constants set that threshold to `0.20`, `stable_program_stability` to `0.35`, `public_program_stability` to `0.50`, `low_army_experience_gate` to `25`, high global threat to `0.5`, and the Totalen Chaos floor to `799` with source comparisons using `>`. These are source thresholds, not scenario values supplied to the evaluation.

## Opening inspect

The first successful weighted inspection used the corrected live source shape `source: { path: "events/024_hearts_of_iron.txt" }`, adapter `event_option_ai_chance`, `refresh: false`, workspace `mod_chaos_redux_ea3b2d67c2c0`, and the complete candidate pool:

- `chaosx.nr24.2.a`
- `chaosx.nr24.2.b`
- `chaosx.nr24.2.c`

Result: `PROBABILITY_SOURCE_INSPECTED`, status `ok`, `candidateCount = 3`, `poolComplete = true`, `requiredInputs = 9`, `unresolved = 0`, `unsupported = []`. The inspect returned no analysis ID. Its source revision is `2be9734ce2e357333ed5a81b7d2d0e5b3d62cccf9329be32befe3b2650329332`; aggregate source hash is `2d2c31c4c1053d4b3006a116a88430f86350d5b247f44b961bbbaca49426224a`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8fa924a12a8fe45f5f6a57f003276e79faeb879720626aeb0f5dbcc4aabaccc/f43f83a4bc2223bb6b8612966c656caf43639d890b269805da833b94bfaa79a4/probability-inspect-2d2c31c4c105.json`.

The inspect artifact identifies adapter `hoi4-1.19.2.v1`, targeting Operation Postern `1.19.2.0 (d245)`, observed as `1.19.2.0.a729 (d245)`. It declares proportional categorical selection, complete-pool normalization, raw-score and normalized-probability support, and the engine d100 limitation. Runtime option shares are conditional on `.2` being selected and are quantized to 1% increments; they do not include Event 24's own firing chance.

The nine inspect-required paths are `compare_autonomy_state`, `has_army_experience`, `has_capitulated`, `has_government`, `has_stability`, `has_war`, `is_subject`, `variable.global.chaos_meter_value`, and `variable.global.threat`. The three candidates have weight blocks and no option-specific eligibility blocks. The `.2` event's current-host trigger is an event-level gate.

## Source score traces

These are raw source bases and conditional modifiers only. No modifiers were multiplied by hand and no normalized share is inferred.

| Candidate | Raw base | Source modifier trace |
| --- | ---: | --- |
| Controlled Staff Trial (`.2.a`) | `video_game_in_sweden_ai.controlled_opening = 4.0` | Peace `1.8`; low stability `< 0.35` `0.5`; severe campaign crisis `8.0`; democratic `1.5`; neutral `2.0`; fascist `0.4`; low-autonomy subject `1.5`; Chaos `> 799` `0.5`; army experience `< 25` `0.7`. |
| Civilian Commercial Release (`.2.b`) | `video_game_in_sweden_ai.commercial_opening = 3.0` | Stability `> 0.50` `1.5`; war `0.4`; severe campaign crisis `0.0`; communist `1.6`; fascist `0.4`; low-autonomy subject `0.6`; global threat `> 0.5` `1.5`. |
| Competitive Officer League (`.2.c`) | `video_game_in_sweden_ai.officer_opening = 2.0` | War `2.0`; army experience `< 25` `1.4`; supply-crisis flag `0.25`; severe campaign crisis `0.25`; fascist `2.5`; democratic `0.6`; neutral `0.6`; Chaos `> 799` `2.0`. |

The source's severe-crisis factor for Commercial is zero. That is a source-level conditional weight, not proof that O4 activates the helper. All three options remain visible when `.2` fires because there are no option-level `trigger` blocks.

## Named scenarios and input completeness

The evaluation used accepted IDs `P24-O1` through `P24-O4` in set `P24_FINAL_OPENING_MATRIX`, with `actor: SWE` for each. Only explicit Boolean facts were bound: O1 `has_war = false`; O2 `has_war = false` and `has_government = democratic`; O3 `has_war = true`; O4 `has_war = true`. No exact stability, experience, Chaos, threat, autonomy, subject, capitulation, current-host, or crisis values/flags were invented.

| Scenario | Accepted facts | Bound facts in this request | Remaining unbound or qualitative facts |
| --- | --- | --- | --- |
| P24-O1, Calm democratic peace | Democratic or neutral; peace; high stability; adequate army experience; no supply shortage; calm world | `SWE`, peace | Government alternative is unresolved; numeric stability, army experience, Chaos, global threat, subject/autonomy, capitulation, host validity, and supply/crisis flag state are not bound. |
| P24-O2, Calm democratic rearmament | Democratic; peace; high world tension; low army experience; good industry and supply | `SWE`, peace, democratic | Numeric stability, army experience, global threat, Chaos, subject/autonomy, capitulation, host validity, and explicit supply state are not bound. Good industry has no direct opening weight modifier. |
| P24-O3, Militarized Sweden at war | Fascist, military, or strongly authoritarian; war; low army experience; good supply/fuel/trains; Gathering Storm or higher | `SWE`, war | The government alternatives do not map to one exact government value; numeric army experience and Chaos, supply flag, stability, subject/autonomy, capitulation, and host validity are not bound. |
| P24-O4, Emergency defense | Any ideology; war; recent core loss; poor supply and low fuel; low stability | `SWE`, war | Core-loss and supply-crisis flags, numeric stability, fuel, government, army experience, Chaos, subject/autonomy, capitulation, and host validity were not bound. |

The pool is source-complete for every scenario, but external-factor coverage is incomplete for all four. The evaluator's exact union of required inputs is listed above. In particular, O4's accepted poor-supply fact did not arrive as the source flag `video_game_in_sweden_supply_crisis` in the submitted scenario state.

## Probability evaluation result

The fresh evaluation used `refresh: true`, the same complete three-option pool, and only the scenario facts listed above. Result: `PROBABILITY_ANALYZED_PARTIAL`, status `ok`, analysis ID `probability-1a818ceb83bebae965d677cf`, scenario hash `19541eb7c17c694a39cfc2390bd1fe23a5195bc943d16f1d9e2c8c3b11ec33e9`, source revision `73722338d405198e8afaa0dc4e21157ed74d11cbab0452952679f39f3761da0c`, aggregate source hash `2d2c31c4c1053d4b3006a116a88430f86350d5b247f44b961bbbaca49426224a`.

Structured summary: `scenarios = 4`, `candidates = 12`, `eligibleCandidates = 12`, `excludedCandidates = 0`, `unresolvedCandidates = 0`, `unresolved = 20`, one informational diagnostic, and uncertainty validation passed. Twelve scenario/candidate rows were analyzed, one for each P24-O1–O4 × `.2.a`/`.2.b`/`.2.c`. The available structured response does not expose the rows' numeric values or enumerate the 20 individual unresolved items. No ranking, score trace, or conditional share is claimed.

The returned diagnostic is `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS`: `chaosx.nr24.2.c`, modifier `factor:constant:video_game_in_sweden_ai_factor.opening_supply`, across all four scenarios. The supply-crisis flag was not set in the submitted inputs. This identifies a scenario-binding omission, not a source defect or proof that supply never affects the candidate.

Authoritative evaluation JSON URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/abb056df979b8585adf24ea86fb6c9a0150e17dd1a982f7604a5df14e6054023/325d6424a512572403b71e2f8efde8d611cb32c6990e1b35c60b6f4322c62f13/probability-1a818ceb83bebae965d677cf.json`.

Artifact discovery returned only `hoi4-agent://server/status` from `list_mcp_resources` and the template `hoi4-agent://workspace/{workspaceId}/artifact/{sha256}/{provenanceHash}/{name}` from `list_mcp_resource_templates`.
The template supports byte `offset`/`length` reads up to 1,048,576 bytes and an optional `metadata=manifest` selector.
The connected tool list exposed no standalone artifact-reader tool.
Parent-reported server status was version 3.10.0 over stdio, and task negotiation was not verified.
The advertised artifact template does not establish successful artifact delivery.

Two bounded reads of the evaluation JSON at offset `0`, lengths `1048576` and `8192`, both returned exactly: `Mcp error: -32603: Artifact provenance manifest is unavailable`. Neither read returned artifact bytes, so byte-count or SHA-256 verification could not be performed. No workspace registration or server configuration artifactRoot value was present in the evidence available for this follow-up, so local artifact access was not attempted and no `.hoi4-agent` path was assumed. The 20 individual unresolved category/input entries and per-row traces therefore remain unavailable and are not guessed here.

The evaluation itself returned these render resources:

- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/637be51d44f782e459435746c4ca2fc31305357eaec04566f2c307d5dde54b7e/6384a2770b610683e795e478fe9e5092f37751a10f2e3fa1e11680b493ad065e/probability-probability-1a818ceb83bebae965d677cf-ranking.svg`
- Ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0cebc2c5cb261889c1a91fcc955f749fc2ce6d2d8ce170d0eca50757469b471c/cc03332e94c0e696a37401785615482fb8d78ff84f131f11d1804cd7d0190d47/probability-probability-1a818ceb83bebae965d677cf-ranking.png`
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed3765ab899b6d4f77d0417f546bb28be5ca5ddac053f774d318e5fe738e0237/465471118be70373d03f2b383add64fcc11cb72c6ffc6f6eb2f31b11d415aace/probability-probability-1a818ceb83bebae965d677cf-matrix.svg`
- Matrix PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13bc0d20b1ed9072d391958076c21dd6a25099bc3ae8ac3cc82e3af14628f456/5d0d33562f221be66452e50970528ec6efe9ef0999bfc4193c3f48c316994c49/probability-probability-1a818ceb83bebae965d677cf-matrix.png`
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9390ab16c85ec3b55551bcaf05a4451a4a3806211cc534c865cd907f37f78b56/f4383d81189afbbf75544fad332c60ccf1969b43b86f598c689d3aec1d553e4d/probability-probability-1a818ceb83bebae965d677cf-unresolved.svg`
- Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0688eb3dac4c61e64b11b944deec61573f88fce080972181c1bc66e782f6379/9933ddea20e4e67b3eb7f69f106c2573cab430553d117a3bd05b84f2bc3ed216/probability-probability-1a818ceb83bebae965d677cf-unresolved.png`

The explicit `hoi4.probability_render` call returned `PROBABILITY_ANALYSIS_NOT_CACHED` for this analysis ID, with the blocker “Render requires a retained analysis ID from this authorized workspace.”
No further evaluation or render request was made.
No probability sweep was run because exact benchmark fixture bindings had not been chosen and the twenty unresolved item details were unavailable.
The owner may declare explicit benchmark fixtures within the accepted scenarios' qualitative conditions, including the applicable government variants, without representing those chosen inputs as observed campaign facts.
Simulation was not run because no distributions or seeds were declared.
Sequence analysis does not apply to this event-option pool.
Compare was not run because no weighted source changed and the parent requested comparison only after its patch.

## Structural and reference evidence

`hoi4.event_inspect` was run on the `.2` opening selector. It returned `EVENT_INSPECTED_PARTIAL`, workspace revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0`, graph hash `d494c41cf68a6eb896650d0f95ea38572ce93b8c83273a07a92d60c74eb41ceb`, one blocking diagnostic, 2,285 diagnostics, 10,444 unresolved nodes, and `helpers = 0`. The workspace-wide inline source list was limited to 64 of 403 paths. This is partial structural context and not lifecycle or helper-absence proof. Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26a7d073963540785246c2868e19f9304b995f55312dea7d0dde878fbda28ef4/aa12cdb5620a5846d0c782071c1155dfa666e970a89f4f8113ca46fc248eaece/event-trace-8f4a82aa5d84.json`.

`hoi4.event_render` for selector `.2`, view `options`, returned `EVENT_RENDERED_PARTIAL` with 7 selected nodes, the same graph revision/hash, and the same workspace-scale diagnostic boundary. Render resources:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2f4c38a60ec3442e9f8d513eb80739bde6bdd07fa3af4e677a140165efa9d2f/f0278d84768c8e5611325eb076953a3fefe424711f923efc85258a04243982bb/event-options-8f4a82aa5d84-manifest.json`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16475de2f7e3e2fc1c38851e819e4a86ef5a5c16368b17d18b3f800e303948d4/c972baf69aeca129fa0da624abf7a2dc79e17e59bcb6402f23bd7625d16a00a9/event-options-8f4a82aa5d84.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4028b2f6c07324e246675d7ee5c7a7a31f5a70320d398e2e9daaceac771d78a/ba9989f57fc1c8a8ebb1f7af99d94b7f5e1f76ae31480141d1bfd55a5cb1965d/event-options-8f4a82aa5d84.svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c9bb993c90b995f23972f7d63ac2c9d6275854bfcf4540fac14a2103dc603e2/984440ad1a53040d97681c27b86a16c0bcbc77a722e7251742646c44b051c43f/event-options-8f4a82aa5d84.png`

Offline references read through the configured route:

- Offline wiki `Event modding`, Options, lines 151-179, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
- Offline wiki `AI modding`, MTTH blocks, lines 26-37, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`.
- The wiki distinguishes event-option proportional sampling from `ai_will_do` score races and documents d100 quantization. The installed-documentation search for event-option `ai_chance` returned only the unrelated `special projects documentation` (`e5d1766e95fe9c71d676046720bb699918e2565c8a43fe5a9183359c98bfcbfe`, match line 323), not an event-option rule section. Vanilla `game:events/AAT_Sweden.txt` source lookup located `Sweden_rearmament.1` option `ai_chance` at lines 29-31, source-index revision `8a069c1e5049b5f1356f651580963c6afa9dba88b3a039db153d06d61194b243`; the source-lookup result identified the block location but did not return its body.

## Findings, recommendations, and limits

- Candidate-pool completeness is confirmed at source-definition level. External-factor completeness is not confirmed for any P24-O scenario.
- No scenario rank, normalized share, sensitivity breakpoint, rank reversal, dominance, or starvation conclusion is supported by the accessible evaluation summary. The exact 20 unresolved entries and per-row traces remain unavailable because of the artifact-read failure above.
- The source's zero Commercial crisis factor is consistent with the accepted O4 direction only when the crisis helper is true. The O4 scenario did not bind the crisis flags or numeric stability, so no O4 probability claim follows.
- The accepted orderings remain unresolved: O1 Controlled dominant; O2 Controlled and Commercial close; O3 Officer dominant with Controlled credible; O4 Controlled first with Commercial near-zero or invalid.
- To complete the numerical pass later, bind the accepted IDs to exact government variants, stability and army-experience values relative to the source thresholds, numeric Chaos and threat, subject/autonomy, capitulation, current-host identity, and crisis/supply flags. Preserve the complete three-option pool. Do not tune weights from this partial result.
- D16's organization/rail/control/reserve proxy is not treated as approval or supplied-division proof; the original exact supplied-division requirement remains binding. Field-Validated Planner remains retired. This audit makes no MTTH pacing claim and does not rewrite the current pace accumulators.
- Parent-owned Event 24 `.50` state-flow work is outside this handoff and was not duplicated. No full Event 24 goal or stage acceptance is claimed.

## Reading and validation boundary

The 16 files in `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\specs\024_video_game_in_sweden_specs\`, `takeover_status_2026-10-06.md`, `acceptance_status_2026-10-07.md`, and handoff 26 were read in bounded outputs during the earlier audit. The events, MTTH, and decisions/missions skills were reread in bounded chunks. The user supplied the complete `AGENTS.md` instructions in the prompt.

This follow-up read the physical `AGENTS.md` and `.agents/skills/chaos-redux-subagents/SKILL.md` to EOF using nonoverlapping raw string slices of at most 10,000 characters, with each slice separately returned below the output limit. `AGENTS.md` had 48,378 characters and 48,402 bytes; the covered offsets were `[0,10000)`, `[10000,20000)`, `[20000,30000)`, `[30000,40000)`, and `[40000,48378)`. The subagents skill had 54,643 characters and 54,647 bytes; the covered offsets were `[0,10000)`, `[10000,20000)`, `[20000,30000)`, `[30000,40000)`, `[40000,50000)`, and `[50000,54643)`. These two EOF gaps are resolved. Earlier combined outputs had been truncated; no claim here relies on those truncated displays for these files.

No live game, desktop, save, or logs were used. No gameplay, AI, event, weight, workbook, or CSV file was edited. No Git index operation or commit was performed. Before this handoff was written, the shared worktree was already dirty with 718 status entries; it is not reported as clean. Parent-reported catalogue closure commit `96a4d04f01711d211309af56228bac2ad8c82d39` was noted; the last pre-write local HEAD observed here was `269215ef29d8f5b5e4d09865b0b475c7c8869bda`. This new handoff is the only owned file.
