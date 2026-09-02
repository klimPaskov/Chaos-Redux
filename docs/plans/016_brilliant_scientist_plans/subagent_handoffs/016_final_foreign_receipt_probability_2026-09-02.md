# Event 016 foreign-operation receipt probability baseline

Status: prepatch baseline secured on 2026-09-02 and the frozen owner patch was compared on the three baseline-supported pools on 2026-09-02. The comparisons are partial and unresolved in the exact places recorded below, with no normalized probability or complete lifecycle certification claimed. This audit edited only this handoff; no foreign gameplay, AI weight, localisation, or source file was edited by this audit.

## Contract and scope

This audit covers the foreign-operation decision willingness surface and the separate host-response event option pools described by `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_foreign_lifecycle_review_2026-09-02.md`.

The source scope is:

- `common/decisions/016_brilliant_scientist_foreign_decisions.txt`
- `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`
- `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt`
- `common/script_constants/016_brilliant_scientist_foreign_constants.txt`
- `events/016_brilliant_scientist_foreign_events.txt`
- `common/mtth/016_brilliant_scientist_foreign_mtth.txt`

The retained before-source identity is commit `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd`.
The current repository HEAD at capture was `375ff3049ff48f81e04e6d49208f98fe1361598e`.
The six retained source blobs are identical between those commits; `git diff --ignore-space-at-eol` was empty, and the current working-tree marks are line-ending-only rather than semantic foreign-source changes.

Raw SHA-256 and retained/current Git blob identities are:

| Source | Raw SHA-256 | Git blob |
|---|---|---|
| `common/decisions/016_brilliant_scientist_foreign_decisions.txt` | `7d76a5b4a6e33b26c8dd3162530547598b183f54f4e9c2273e0d5a6d286d3408` | `643909a4cb4cc599f82f0ff5100f03935e5f742f` |
| `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt` | `6192259e7d657c77b951e40871ecef2cf691d3fe008beda40832a9c1fcfb66a9` | `0839d988223a2e195413676fcb9a8119a754f74c` |
| `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt` | `eff7c2fbcd5fad75cc1e983ceb3ee988c4cfbb4ed1734fa039221fd868cd90c9` | `009a4d3673946d6a593839720b1ad8e1888bfe52` |
| `common/script_constants/016_brilliant_scientist_foreign_constants.txt` | `94e00eee79916d7baf17c4a18c5bb96a330296c711c8a938d9019ee515816557` | `03614da7a7f565b762d26ef5bb92fa52f7d0f29e` |
| `events/016_brilliant_scientist_foreign_events.txt` | `ae97bf2aec5e2e0e49a7ec933c8857b577484cbbf1af155a4ca18dad632c686c` | `b5a64717acfc48ce7f2d801331b9350a2396833e` |
| `common/mtth/016_brilliant_scientist_foreign_mtth.txt` | `e4e47a20d513097a84f0c8c1a361874825d2cacc3a441759f5b53902cce187a6` | `c3d1387eac557f6a09b9355759e9f3f3ce5f4e18` |

The frozen owner after-source raw SHA-256 values are decision `eb163ae804104d01d68b2e2dfc4e76896fd6069812039e33e1a072f829052d62`, effects `4eedd265aa1760c3ea4852ba5c499f8a06e78283a526a8b452abb9f3fe2b5aaf`, triggers `624d229bdb637cc25188766ac26543a431a5de63282c0ccc7c2f232dbcf09d80`, constants `9fa0e9ca054c4b9c2911a9e9f9910298c652347ee34f6e742809d197e71b8b72`, and events `2b6629fc445f8d495867fba26b85b44d5eb4715665d14690af412e874d763264`.
The owner reports that the constants change is metadata-only (`role` enum `actor1`/`host2`) and that old weights, costs, timers, and event option chances are unchanged.

## Candidate surfaces

The decision category `brilliant_scientist_foreign_operations_category` contains these exact 11 candidates:

1. `brilliant_scientist_foreign_observe_program`
2. `brilliant_scientist_foreign_send_formal_invitation`
3. `brilliant_scientist_foreign_recruit_assistant`
4. `brilliant_scientist_foreign_steal_archive`
5. `brilliant_scientist_foreign_sabotage_project`
6. `brilliant_scientist_foreign_encourage_defection`
7. `brilliant_scientist_foreign_extract_kruger`
8. `brilliant_scientist_foreign_offer_protection`
9. `brilliant_scientist_foreign_attempt_assassination`
10. `brilliant_scientist_foreign_build_counter_program`
11. `brilliant_scientist_foreign_public_challenge`

Eight candidates are timed decisions with `days_remove` and `remove_effect`; invitation, protection, and public challenge are immediate response-opening decisions. Their AI willingness is sourced through 11 separate MTTH entries in `common/mtth/016_brilliant_scientist_foreign_mtth.txt`, not a probability-proportional event pool.

The host response events remain separate pools and were not flattened:

- `chaosx.nr16.100`: `chaosx_nr16_100_a`, `chaosx_nr16_100_b`, `chaosx_nr16_100_c`.
- `chaosx.nr16.110`: `chaosx_nr16_110_a`, `chaosx_nr16_110_b`, `chaosx_nr16_110_c`.
- `chaosx.nr16.120`: `chaosx_nr16_detected_secure_a`, `chaosx_nr16_detected_protest_b`.
- `chaosx.nr16.130`: `chaosx_nr16_detected_secure_a`, `chaosx_nr16_detected_protest_b`.
- `chaosx.nr16.140`: `chaosx_nr16_detected_secure_a`, `chaosx_nr16_detected_protest_b`.
- `chaosx.nr16.150`: `chaosx_nr16_detected_secure_a`, `chaosx_nr16_detected_protest_b`.
- `chaosx.nr16.160`: `chaosx_nr16_detected_secure_a`, `chaosx_nr16_detected_protest_b`.
- `chaosx.nr16.170`: `chaosx_nr16_detected_secure_a`, `chaosx_nr16_detected_protest_b`.
- `chaosx.nr16.180`: `chaosx_nr16_180_a`, `chaosx_nr16_180_b`.
- `chaosx.nr16.190`: `chaosx_nr16_190_a`, `chaosx_nr16_190_b`, `chaosx_nr16_190_c`, `chaosx_nr16_190_d`, `chaosx_nr16_190_e`, `chaosx_nr16_190_f`.
- `chaosx.nr16.193`: `chaosx_nr16_193_a`, `chaosx_nr16_193_b`.

The `.101`, `.111`, `.121`, `.131`, `.141`, `.151`, `.161`, `.171`, `.181`, `.191`, and `.194` actor-report events are not host-response weighted pools and were not substituted for the required response events.

## Exact fixture

The complete retained fixture is [E016_FOREIGN_RECEIPT_LIFECYCLE_2026_09_02.scenarios.json](E016_FOREIGN_RECEIPT_LIFECYCLE_2026_09_02.scenarios.json).
Its schema is `1.0`, its `surfaceHint` is `decision_ai_will_do`, and its scenario hash from the MCP evaluations is `5d6c32359c2215900683ace57139969c8dd47bd79e67167105cdf483d109c346`.

The named scenarios are:

- `E016_FOREIGN_FRIENDLY`
- `E016_FOREIGN_NEUTRAL`
- `E016_FOREIGN_HOSTILE`
- `E016_FOREIGN_INTELLIGENCE_DOMINANT`
- `E016_FOREIGN_IDEOLOGY_OPPOSED`
- `E016_FOREIGN_REPEATED_TARGET`
- `E016_FOREIGN_VALID_LIVE_RESPONSE`
- `E016_FOREIGN_EXPIRED_RESPONSE`
- `E016_FOREIGN_MISMATCHED_TYPE`
- `E016_FOREIGN_MISMATCHED_HOST`

The fixture declares relation, government, war, intelligence, operative, foreign-interest, incoming-count, live-receipt, operation/type/host identity, start and expiry dates, repeated-target history, project counts, grievance/dependence/independent-capacity/exposure, flags, current-host event target, operation actor/host event targets, and `HOST`, `ABC`, and `OLD` scopes where needed.
These are explicit adapter inputs, not proof that the engine resolves every custom helper, event target, array, or cross-scope relation.
In particular, the decision root is `ABC`, while host response options use event/root scopes; this scope mapping remains an unresolved limitation.

## Mandatory probability inspection

All calls used the read-only `hoi4` probability service with workspace `mod_chaos_redux_ea3b2d67c2c0`, `refresh=true`, and the exact candidate pools above.

The decision inspection used adapter `decision_ai_will_do` and source identifier `brilliant_scientist_foreign_operations_category`.
It returned `PROBABILITY_SOURCE_INSPECTED` with no diagnostics.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d9df34221958b50bfa435be31475a75222a17e5263b55f01bb3e0f87ce4c0e3/98f7d0b39e3486e879d99d3cedc23bc6914d2a7d3b5b3910ee0a5d85dd6952dd/probability-inspect-3e50305d3c4bf.json`.
The inspect source revision was `df6e0ff4078ae88bbaf5841ec169688aa46577d2959d882d30f92e20621fbd0d`, normalized source hash was `3e50305d3c4bf4fe2fe754c9ea87b5811c34d8cfe228917d3e333d729cee92e8`, and the candidate pool was incomplete.
Only these three immediate candidates were discovered: `brilliant_scientist_foreign_offer_protection`, `brilliant_scientist_foreign_public_challenge`, and `brilliant_scientist_foreign_send_formal_invitation`.
The other eight exact candidates returned `CANDIDATE_NOT_FOUND`: observe program, recruit assistant, steal archive, sabotage project, encourage defection, extract Kruger, attempt assassination, and build counter-program.
The inspect therefore reported three discovered candidates, zero available candidates, eight unresolved candidates, and seven required inputs.

Corrected event inspection for `chaosx.nr16.100` used underscore candidate IDs and returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete=true`, three candidates, five required inputs, and no diagnostics.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c42c034169f79728370e029af619cd281b7efe42233243bd274c3c13adc3dbb/535bc9695ae6dd1e0f5248925648570a53c42a8f8fefe252214a3431df34a854/probability-inspect-4944ab87aa95.json`.
Its normalized source hash was `4944ab87aa95b3ec5d7409d271f62afaed6ec43fa5632ce1d83bdbe9978eb605` and source revision was `1f416369eb92684a381c94092a902f3b7c6f5f57f76cda47fbec8df5e79a0ec7`.

Event inspection for `chaosx.nr16.160` used its two exact underscore candidate IDs and returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete=true`, two candidates, one required input, and no diagnostics.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e2e1390de4e8f249e24a2f8dc7272648fe2103879e1f559cd248f6dc20ecf2f/5277348a85a91fd30c49e69c9867156135f45f5d9cc33aef1e6f7690beb45d48/probability-inspect-4944ab87aa95.json`.
Its normalized source hash was `4944ab87aa95b3ec5d7409d271f62afaed6ec43fa5632ce1d83bdbe9978eb605` and source revision was `082f7ecae0666ec7cacc6c70169ab48d60f62ffc463c4bc483230ffc930d8958`.

The remaining required response inspections for `.110`, `.120`, `.130`, `.140`, `.150`, `.170`, `.180`, `.190`, and `.193` each returned the exact MCP status `INTERNAL_ERROR`, status `error`, with no diagnostics and no artifact URI.
No retry loop was performed, and those nine pools remain uninspected by the probability adapter.

## Bounded evaluations

The decision evaluation used adapter `decision_ai_will_do`, the exact 11-candidate pool, the complete fixture, metric `raw_value`, outputs `json`, `ranking`, `matrix`, and `unresolved`, and the raw expected source hash `7d76a5b4a6e33b26c8dd3162530547598b183f54f4e9c2273e0d5a6d286d3408`.
It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-96b500cfe4bf024de1d71a86`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/96e3d52a4a0db5107c447f49193a79dedf48ff41d2ad8bc974b0c4e8adbe201f/dccae22df802eb6b19cdd529d52460745373399ba419ec29256d28ce0d5b5696/probability-96b500cfe4bf024de1d71a86.json`.
The evaluation source revision was `4d4a19e35a2eec1ccae1f28d2abd01b8531db63310cf25f3da37e91afa36ce61`, normalized source hash was `3e50305d3c4bf4fe2fe754c9ea87b5811c34d8cfe228917d3e333d729cee92e8`, candidate pool hash was `19164f84230d0ae488f22e04749f6ef1a0549af120cb32f42a555a63b5eb8b6c`, and cache key was `96b500cfe4bf024de1d71a86e88aec165feaeb190769fef0814d01db2dcc4f48`.
It evaluated 10 scenarios against 30 discovered-candidate rows, with 24 unresolved rows at the top level and no diagnostics.
All rows were `score_only`, `poolComplete=false`, and eligibility remained unresolved.
The rendered ranking, matrix, and unresolved views are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/413b4d5a57aa9d511cfb16ea4d5c9479a2b6f08537dcc57e1ec616076586421c/e1e536c0061a5d1384e283b7233ef74b8f182f6f3761d65fea445caac8777be2/probability-probability-96b500cfe4bf024de1d71a86-ranking.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e94485a082ca60a83bab40b4f1cb4a2238c0ff0a0a190ea6ee983ad04c28cdd/fb9f8be8dbc78e8dc6d33f24a7e09ab4dfcced755e7c62d8c4b3598d96e096d4/probability-probability-96b500cfe4bf024de1d71a86-matrix.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebc73450b021a44aeedf09796cd2fd06e2a0531477172e1a9dd804e6aa1959da/b544c9becbf980d120d604b6dfbfde44861a925955746f935d8ee470790c4cfc/probability-probability-96b500cfe4bf024de1d71a86-unresolved.svg`

The `.100` evaluation used its exact three-candidate pool, the same fixture, metric `raw_value`, the same output set, and raw expected source hash `ae97bf2aec5e2e0e49a7ec933c8857b577484cbbf1af155a4ca18dad632c686c`.
It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-8339daf6f06bacb3463fd100`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd951883ae546826939ee3cf55e63efd0b7ced1a6f7cb9ad9e5d1ced30b5c9bb/1290dca615c86a713eb75ed47fa3578b8bc28275bd2059d628e9ba400b3fed0e/probability-8339daf6f06bacb3463fd100.json`.
The normalized source hash was `4944ab87aa95b3ec5d7409d271f62afaed6ec43fa5632ce1d83bdbe9978eb605`, source revision was `f9020ee6dee600a4682334bd9840d6c01f3b966d4d072d0a9f69a4d3e030ebe3`, candidate pool hash was `e358d63cd88c29e7d58cc3e08f6ee319d4c1bf7c066f3393a9dea174b98830e9`, and cache key was `8339daf6f06bacb3463fd1009d18603ed42bdcb26157a3eb7b4b5bdf3387216e`.
It evaluated 10 scenarios and 30 candidate rows, with 10 unresolved rows and one warning diagnostic.
The pool was complete as a candidate list, but support was `unsupported` because factor and helper traces were unresolved.
The warning was `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for `chaosx_nr16_100_c` across all 10 scenarios because `brilliant_scientist_is_transfer_ready` resolved false in the supplied fixture/root context.
The rendered ranking, matrix, and unresolved views are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c32c780cc1e4b809ac55dbd38bd07207f9d89e41dccb1e983e2cfd35c1f52713/08fa88c6c3e1e49304daa142a00f31a89a664f2cea7bca314092b0f9c55166d6/probability-probability-8339daf6f06bacb3463fd100-ranking.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a686178f799d6a923388ab867ce28a84a498ef8e3b651053c1e0e07265247449/ad42f7b91f3f8445ae0788a8c5a48af6471a1f96cbcedf5b834894c26ece45ff/probability-probability-8339daf6f06bacb3463fd100-matrix.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/319255acae312b7d5f01be613112e339bc1dbd3945cfa50eaa0cbd1514f96db0/04eaaea6ff8b2685a91b01bc43218ecadae3894b0cb74bf649e5ac9d4c1fa9a4/probability-probability-8339daf6f06bacb3463fd100-unresolved.svg`

The `.160` evaluation used its exact two-candidate pool, the same fixture, metric `raw_value`, the same output set, and the same raw expected event-source hash.
It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-8605bd2caaf5ce1554ed42af`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ecb5f54fab3b9696abf33e733471c4512408cab09f601af16a07a8d8c7e6ac5b/9c0c781b0c513c41903561ccd89d4a650486139e39f5f963f22c491110aa6f81/probability-8605bd2caaf5ce1554ed42af.json`.
The normalized source hash was `4944ab87aa95b3ec5d7409d271f62afaed6ec43fa5632ce1d83bdbe9978eb605`, source revision was `f9020ee6dee600a4682334bd9840d6c01f3b966d4d072d0a9f69a4d3e030ebe3`, candidate pool hash was `b21b60b2a85939d7ee7d1b0ca169f2eac72a791aa4c23bf0cdd50c5d1221ca9c`, and cache key was `8605bd2caaf5ce1554ed42afa8b352677bb8e822f75edfa92ba2ed0d122b3635`.
It evaluated 10 scenarios and 20 candidate rows, with four unresolved rows and no diagnostics.
Both options were eligible in the adapter, but support was `unsupported` because the `dependence` and `mandate` modifier traces remained unresolved.
The rendered ranking, matrix, and unresolved view are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/345fc76857352db4689d2225886cbf1a2dfc1197eaa1522a8b8ba6281b865082/4aaa4efe3e366a7b70399a71308c9265b0823e0dd8a23659acba89292667c489/probability-probability-8605bd2caaf5ce1554ed42af-ranking.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/652b76a6511c2e6ed6113237658cd9c2ae1bdeb1533ce431520b3dad945c2d38/a9059fcd475d4c650a6002cc67a70308dd404f2a57b66cdd9d25812bbff4e094/probability-probability-8605bd2caaf5ce1554ed42af-matrix.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3dc1bde48d71d8d46a53c2cfbed4fd0b492015989e32ab6300d243e87daf46e/1074eac400e32273cc0f11dab2a9c33738c9a65bd3d148a723b58126524c5bf1/probability-probability-8605bd2caaf5ce1554ed42af-unresolved.svg`

No evaluation was attempted for `.110`, `.120`, `.130`, `.140`, `.150`, `.170`, `.180`, `.190`, or `.193` because their mandatory inspect calls returned `INTERNAL_ERROR` without a source artifact.

## Frozen owner postcompare

Each valid comparison reused the exact fixture and the exact separate candidate pool from the baseline.
The before side used retained source bytes from commit `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd` as `inlineClausewitz`, and the after side used the frozen current source path with its lowercase expected hash required by the MCP schema.
One initial decision submission was rejected before analysis because the after hash was uppercase; the corrected lowercase submission is the valid result below.

The decision category comparison used adapter `decision_ai_will_do`, all exact 11 decision IDs, and scenario hash `5d6c32359c2215900683ace57139969c8dd47bd79e67167105cdf483d109c346`.
It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-bd3b07b29b6e62856ae9f657`, before analysis `probability-b52845dad1e4ab5a1e417666`, after analysis `probability-6ca4f991fd975014c16dca00`, `comparisonChanges=0`, no scenario changes, no regressions, 27 unresolved items, and no diagnostics.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b7f209451e362747907e6a3ad215d0b9ea7847d225d8dc7b69dff8c7297cbf3/279743e966401e847ad6c705658fb76e37e66e4865d5e04d144c1ae54b576d3e/probability-bd3b07b29b6e62856ae9f657.json`.
Candidate pool hash was `19164f84230d0ae488f22e04749f6ef1a0549af120cb32f42a555a63b5eb8b6c`, aggregate after source hash was `538c761ce7ccf1c00b68e1c2ffd6a716548b8afb04b4b5211c816e054cae7682`, source revision was `a003fc5e9c644d69f3c2454fbf771d8dddceacd5f6b25fb224c0e5b05d0a1307`, and cache key was `bd3b07b29b6e62856ae9f65775c75019b9b3e5669144cb98daf4c4c8d2cb6c98`.
All 30 represented rows remained `eligibility=unresolved` and `supportLevel=score_only`, with zero eligibility prevalence for each of the three discovered immediate decisions.
The comparison ranking, matrix, comparison, and unresolved views are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c80b48c088fa56657a4c9f31462356051a8fa43ddc1a88ead1fe6dfc6102e10/2a19da5c2b6376b4cd52c70f4495ddd74f43d36cd4d8e6f0aeed7c54531d6451/probability-probability-bd3b07b29b6e62856ae9f657-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e94485a082ca60a83bab40b4f1cb4a2238c0ff0a0a190ea6ee983ad04c28cdd/001d5bce7d1378aab7abe4c4a3aeb9258d090069e77bc554a2d1f618b39b1e96/probability-probability-bd3b07b29b6e62856ae9f657-matrix.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/8a8c2f33c03732595920dd7f0f13dea9e632669e2b9687cb9bc36d0a1f3f239d/probability-probability-bd3b07b29b6e62856ae9f657-comparison.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/953afa7b4408c3840483a57ff596a244878a3fc7207f4a846a6d7bbffc6504bd/6bbbe09a239c4ac8401d8ec313d7c938746fe71b29786de7cad0c407419bfcd0/probability-probability-bd3b07b29b6e62856ae9f657-unresolved.svg`.

The `.100` host-response comparison used adapter `event_option_ai_chance`, the exact pool `chaosx_nr16_100_a`, `chaosx_nr16_100_b`, `chaosx_nr16_100_c`, and the same scenario hash.
It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-c6507938f5a5e0215ecfdc91`, before analysis `probability-a80ac2b186e1a48b0f79c734`, after analysis `probability-223a66c593d50f90e6f77dc9`, `comparisonChanges=0`, no scenario changes, no regressions, 11 unresolved items, and one warning diagnostic.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7018876f7bb6ac2a8d100268479685c80398f7a1eaf35be7d435d7e61417c949/af768d4fd3ad8b96a8f31950d5dcab512710c3dc60511bac51355a2efdabebf4/probability-c6507938f5a5e0215ecfdc91.json`.
Candidate pool hash was `e358d63cd88c29e7d58cc3e08f6ee319d4c1bf7c066f3393a9dea174b98830e9`, aggregate after source hash was `198e1a41b7d62ee240b38d00964646dc20b3245d2731567eba7b8d27ddbdfde6`, source revision was `ae68cf4cf4e284afd2aaf4b5187cebd4c2b786eb6c95506cee4fb8cbac406ccc`, and cache key was `c6507938f5a5e0215ecfdc9148cf162f2ae493ac4b7f3a11b748a91c11f4cee0`.
All ten scenarios retained A and B eligible and C ineligible, so the adapter saw 20 true and 10 false rows, all `supportLevel=unsupported`.
The warning remained `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for C across all ten scenarios because the transfer-ready/current-host helper path remained false in this fixture/root context.
The comparison ranking, matrix, comparison, and unresolved views are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d47b9f830ac85267fd21d99af44606541c338fa04c80a559e87d8414b5dba8f6/620aa453e1a1bfb2e53357cefb4f129f588a14e74cc6bffcdc760902ea94c3c3/probability-probability-c6507938f5a5e0215ecfdc91-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a686178f799d6a923388ab867ce28a84a498ef8e3b651053c1e0e07265247449/b8beef001b644403bc14cdfc188859a99ed6560c59fa55b82fed362c86971e0d/probability-probability-c6507938f5a5e0215ecfdc91-matrix.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/2895fab1707a36f34ea9177be318267f60b3596ac10883986b8b73777ecee67b/probability-probability-c6507938f5a5e0215ecfdc91-comparison.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f54d76f733dc7c1192dd151259575c3d8abcbdc29423a9e61c62701efe94dad3/2b9e08f9af33a2a94b891a92b7ba84411cd2aa4cb5a9d28f4dd83bedbd09a448/probability-probability-c6507938f5a5e0215ecfdc91-unresolved.svg`.

The `.160` host-response comparison used adapter `event_option_ai_chance`, the exact pool `chaosx_nr16_detected_secure_a`, `chaosx_nr16_detected_protest_b`, and the same scenario hash.
It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis ID `probability-6acd0a064ee13e9a2bab8748`, before analysis `probability-888a2ffe4a22489cb4e5c902`, after analysis `probability-4de980c09149ce876990f23c`, `comparisonChanges=0`, no scenario changes, no regressions, four unresolved items, and no diagnostics.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/609ba18cdc82d4d896bcb741a960d2c476213472cef79d84bb08b05bbc4595ed/73e8e29c8b1bbaeb0c7b7036732ad762bbd8dae5023b57839e305cb4a18d8af8/probability-6acd0a064ee13e9a2bab8748.json`.
Candidate pool hash was `b21b60b2a85939d7ee7d1b0ca169f2eac72a791aa4c23bf0cdd50c5d1221ca9c`, aggregate after source hash was `198e1a41b7d62ee240b38d00964646dc20b3245d2731567eba7b8d27ddbdfde6`, source revision was `ae68cf4cf4e284afd2aaf4b5187cebd4c2b786eb6c95506cee4fb8cbac406ccc`, and cache key was `6acd0a064ee13e9a2bab8748ff5699ff9e050e61775a01cbdb08555097d71c0e`.
Both options remained eligible in all ten scenarios, all 20 rows were `supportLevel=unsupported`, and the high-dependence/high-mandate factor traces remained unresolved.
The comparison ranking, matrix, comparison, and unresolved views are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c40710bd2e19bbdb854cd9fe61c7cf84721b9381227aa2b1468f3f7a05f407cf/7718460dd56fe1271d880a3c785981c4d5fa6c29b7bfd25824a59e7aab4c59c2/probability-probability-6acd0a064ee13e9a2bab8748-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/652b76a6511c2e6ed6113237658cd9c2ae1bdeb1533ce431520b3dad945c2d38/623f01bd1a2775b424d758aa13d71943b59c68782451c7e20c51da087e29794e/probability-probability-6acd0a064ee13e9a2bab8748-matrix.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/6e13dcc47115e243fdbc18b6c55d58d1c902173dbd59f44da73dfd075e67ffc8/probability-probability-6acd0a064ee13e9a2bab8748-comparison.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3dc1bde48d71d8d46a53c2cfbed4fd0b492015989e32ab6300d243e87daf46e/761ea2031aed8dabcde673cdc3a056a50b0edfebd68876f5f9449fa796a906b7/probability-probability-6acd0a064ee13e9a2bab8748-unresolved.svg`.

The comparison's inline before objects contained only the decision or event source bytes.
The helper and MTTH provenance was expanded from the current workspace on both sides where the adapter resolved it, so the comparison does not isolate historical versus frozen helper definitions.
This shared-helper context is a limitation, not evidence that old and new helper semantics were identical.

## Evidence interpretation

The decision result is `score_only` and incomplete, not a normalized selection probability.
The three discovered immediate decisions had unresolved eligibility, and the eight timed candidates were not found by the adapter.
The MTTH base expression was recognized for the discovered choices, but the returned `before=1` traces did not provide a resolved post-modifier score; no score race or probability ranking is certified.

For `chaosx.nr16.100`, the adapter exposed source score bases of 30 for option A (`option_medium=30`) and 60 for option B (`option_high=60`), with the democratic factor recognized in the applicable fixture row and raising B to 90.
Option C had source base `option_low=10`, but it was never eligible in the ten supplied scenarios because the transfer-ready/current-host path resolved false in the adapter context.
Dependence, grievance, independent-capacity, custom tooltip, event-target ideology, and other helper branches remained unresolved.
These are bounded source-score traces only and do not imply 30/60/90 probability weights.

For `chaosx.nr16.160`, option A (`chaosx_nr16_detected_secure_a`) exposed base `option_high=60` and option B (`chaosx_nr16_detected_protest_b`) exposed base `option_medium=30`.
Both were eligible in the adapter, while high-dependence and high-mandate modifiers remained unresolved because the fixture's numeric values were not recognized by the compact `check_variable` form.
No normalized event-option chance is certified.

The current evidence does not establish dominance, starvation, rank reversal, repetition rate, or exploit risk for the complete foreign decision category or the complete set of host response events.
The incomplete candidate pool, nine failed event inspections, unresolved custom helpers, unresolved event-target and cross-scope semantics, and absent full external-factor resolution are material blockers.

## Lifecycle review handoff

The probability service cannot prove the planned receipt invariants from this source-only fixture.
The frozen owner patch should be reviewed against these contract points without changing costs, timers, route rewards, detection formulas, or AI weights:

- Guard stale timed callbacks and response/report effects by fixed operation type plus the original actor and host identity.
- Enforce the existing one-live, two-incoming, and once-per-type-per-host constraints at shared operation start.
- Keep a distinct pending-host-response receipt after covert resolution is recorded; do not use `NOT resolution_recorded` as the host-response predicate.
- Record operation dates and lifecycle stages so expiry and duplicate callbacks cannot settle a newer operation.

The relevant implementation touchpoints are `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`, `common/decisions/016_brilliant_scientist_foreign_decisions.txt`, and `events/016_brilliant_scientist_foreign_events.txt`.
These are owner recommendations from the accepted lifecycle contract and source audit, not probability-tuning findings, and were not applied by this audit.

## Blockers and next step

The prepatch baseline and valid partial postcompare are retained, but they do not constitute complete probability certification.

- Eight of the exact 11 decision candidates were `CANDIDATE_NOT_FOUND` in mandatory inspect.
- Nine required host pools returned MCP `INTERNAL_ERROR` with no diagnostics or artifact.
- The three bounded evaluations were partial, with score-only or unsupported helper traces and no normalized probabilities.
- Event-root versus decision-root scope, event targets, custom scripted helpers, arrays, relation predicates, dates, and receipt identity remain unresolved adapter inputs.
- The nine unsupported response pools have no compare artifact because their mandatory inspections failed; any later retry must reuse the exact fixture, source identities, and separate candidate pools rather than infer coverage from the three successful comparisons.

No gameplay, AI weights, localisation, specs, or unrelated documentation were changed, and no commit was created by this audit.
