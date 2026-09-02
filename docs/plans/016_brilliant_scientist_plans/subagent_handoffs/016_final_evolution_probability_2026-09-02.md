# Event 016 Tranche 5 evolution and host-reaction probability handoff

Date: 2026-09-02

Owner: `chaosx_ai_probability_auditor` (read-only)

Status: bounded partial audit complete; this is not a completion or ready-for-user-acceptance claim.

The binding source is `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`, with F6 scope from `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_lifecycle_preimplementation_review_2026-09-02.md`.

## Outcome

The four evolution option pools and the three host-reaction option pools were compared with source objects containing the retained prepatch bytes from commit `e7307e228e2b4bda3309672e8077ac9889c7bb36` and the current postpatch bytes.

All completed option-level comparisons reported `comparisonChanges=0`, so no AI option score, modifier factor, candidate ranking, or normalized option probability changed under the named fixtures.

The parent changes are nonweighted lifecycle and root-eligibility guards, so this result is expected and does not prove the scripted-effect receipts, event-root predicates, or engine delivery behavior.

The MCP adapter withheld normalized probabilities because complete eligibility was not proven for the helper-heavy pools; the evidence is therefore partial and bounded rather than an exact campaign probability claim.

No balance fix or weight change is recommended from this pass.

## Audited source surfaces

| Surface | Source files | Change state | Classification |
| --- | --- | --- | --- |
| Evolution option AI chance | `events/016_brilliant_scientist_evolutions.txt` (`chaosx.nr16.21/.22/.23/.24`) | unchanged from retained commit; current SHA-256 `742e4855dc4b47074e39f3a310c2c1180c55471a39da646fc2c8ab0b3a56c907` | exact source identity; option comparison partial because caller/helper state is incomplete |
| Evolution timing source | `common/mtth/016_brilliant_scientist_mtth.txt` | current SHA-256 `7d6946684460dc7338dfdcd20eaedfd7b1fa4838462f4882011bc3bcde6723f`; semantic diff from `e7307e2` is empty with `--ignore-space-at-eol` | no weighted surface discovered by MCP |
| Evolution mission scores | `common/decisions/016_brilliant_scientist_evolution_missions.txt` | current SHA-256 `4f19a1ef1f937235f87b869a11a988494f12553a35ff69516a5b1ca84dfd452`; semantic diff from `e7307e2` is empty with `--ignore-space-at-eol` | no weighted surface discovered by MCP |
| Host-reaction option AI chance | `events/016_brilliant_scientist_host_reaction_events.txt` (`chaosx.nr16.7/.8/.9`) | parent added one root-trigger `NOT = { brilliant_scientist_is_kruger_sovereign_country = yes }` to each event; postpatch SHA-256 `304f414dde65f73de59788157fb5902b600d30900bd880795adf8e24f499f550` | option comparison partial; root-trigger eligibility remains unresolved in the probability adapter |
| Host-reaction schedulers | `common/scripted_effects/016_brilliant_scientist_host_reaction_effects.txt` | parent added the same sovereign exclusion to the three schedulers | nonweighted scripted-effect surface; no option-weight change |
| Evolution lifecycle guards | `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt` | parent added shared context and `is_current_evolution_enabled` checks to four base packages, four seeds, and three lower-stage prefire delivery/policy blocks; current SHA-256 `b888ab495bb1846e5289405e4f96d1fd5bc1af5b8f799a9000f3938ecec324b4` | nonweighted scripted-effect surface; not directly analyzable by the probability adapter |

The before and after inputs to every completed `probability_compare` were source objects with `path` and `inlineClausewitz`; no cached analysis ID was used as a source selector.

## Evolution scenarios

Scenario set ID: `E016_EVOLUTION_BASELINE_2026_09_02`.

The exact named scenario IDs were:

`E016_EV_ALL_ENABLED_ACTIVE_HOST_PUBLIC`, `E016_EV_ALL_ENABLED_ACTIVE_HOST_SECRET`, `E016_EV_ALL_ENABLED_PREFIRE_PUBLIC`, `E016_EV_ALL_ENABLED_PREFIRE_SECRET`, `E016_EV_ALL_DISABLED_ACTIVE_HOST_PUBLIC`, `E016_EV_ALL_DISABLED_ACTIVE_HOST_SECRET`, `E016_EV_ALL_DISABLED_PREFIRE_PUBLIC`, `E016_EV_ALL_DISABLED_PREFIRE_SECRET`, `E016_EV_ONLY_IV_ENABLED_ACTIVE_HOST_PUBLIC`, `E016_EV_ONLY_IV_ENABLED_ACTIVE_HOST_SECRET`, `E016_EV_ONLY_IV_ENABLED_PREFIRE_PUBLIC`, `E016_EV_ONLY_IV_ENABLED_PREFIRE_SECRET`, `E016_EV_III_DISABLED_IV_ENABLED_ACTIVE_HOST_PUBLIC`, `E016_EV_III_DISABLED_IV_ENABLED_ACTIVE_HOST_SECRET`, `E016_EV_III_DISABLED_IV_ENABLED_PREFIRE_PUBLIC`, and `E016_EV_III_DISABLED_IV_ENABLED_PREFIRE_SECRET`.

The fixtures covered active-host versus prefire execution, public versus secret context, all enabled, all disabled, only IV enabled, and III disabled with IV enabled.

The four candidate pools were complete at source-inspect level when supplied as per-event inline source objects:

- `.21`: `chaosx.nr16.21.a`, `.21.b`, `.21.c`, `.21.d_option` (4 candidates).
- `.22`: `chaosx.nr16.22.a`, `.22.b`, `.22.c`, `.22.d_option`, `.22.e` (5 candidates).
- `.23`: `chaosx.nr16.23.a`, `.23.b`, `.23.c` (3 candidates).
- `.24`: `chaosx.nr16.24.a`, `.24.b`, `.24.c`, `.24.d_option`, `.24.e`, `.24.f` (6 candidates).

The public fixtures declared KRG, democratic government, no war, the public compact, public-science context, university host archetype, computing-machine technology, and the canonical Kruger character.

The secret fixtures declared KRG, fascist government, war, faction membership, secret-directorate context, strategic-security context, militarized host archetype, the canonical Kruger character, and the same declared project and capacity variables.

The state variables and flags were explicit scenario inputs, but unresolved helper and typed-trigger evaluation means they are not engine proof of `is_current_evolution_enabled`, `brilliant_scientist_is_current_host`, stage history, or prefire caller state.

## Evolution inspect evidence

The broad path inspection of `events/016_brilliant_scientist_evolutions.txt` found 18 candidates across four categorical pools and correctly withheld a complete normalized pool because of `MULTIPLE_CATEGORICAL_POOLS`.

Broad inspect artifact: [probability-inspect-991079c10600](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5520f9ba95aec990f9e392ddd3449cd13a245cb0c069dddecca3507ed091d58/8cac12185baebfcb442d8a91101864bcf3c1b066da61e47c50b09c7735dbffc2/probability-inspect-991079c10600.json).

Broad inspect source hash: `991079c10600fa27cdc9f504c3733bca8131773446da2fdab72eb5b16cd770de`.

Broad inspect source revision: `5401f669628a870a9c533c45553c28c91e5724e5a8b414606cecd9d0f219eeac`.

The successful per-pool inline inspections were:

- `.21`, pool complete, unresolved 0: [probability-inspect-233c8eaa0e97](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/626475aacef9dd8f48da65cb16a2ed792eed034590c269f0914a9324ab7d9fc8/caf7d30c8aa204d78d80f42f878a4f8fe0b95f1d26dff8374f88661ddb13ab49/probability-inspect-233c8eaa0e97.json); source hash `233c8eaa0e9721757f34c9d70946cdd7afe277a30b4df171c5c94944397a5f65`; source revision `4611821da476b26bfe9f2176649ad198831a80841db012317395c72a24d8c1fa`.
- `.22`, pool complete, unresolved 0: [probability-inspect-233c8eaa0e97](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0a55211e974d4e1381856d0b4bde9c2564f00121ae9ded4e1f7aea75284399e/60da9076f784515c75b8059a496e681c71d20b04a91a0fd8f4abcabf25c65235/probability-inspect-233c8eaa0e97.json); source hash `233c8eaa0e9721757f34c9d70946cdd7afe277a30b4df171c5c94944397a5f65`; source revision `f528d05414a323efb9fc22e06ad01c6bd5a5ce41f604aed1536e7f89ff847e59`.
- `.23`, pool complete, unresolved 0: [probability-inspect-991079c10600](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37d4a5eda093a3a5586c72864dc934f2841d1add2e86e2216b7e089e798317d1/a505151816660bb7715327066a812bed25db587ed254312f69e78dca33bcbb01/probability-inspect-991079c10600.json); source hash `991079c10600fa27cdc9f504c3733bca8131773446da2fdab72eb5b16cd770de`; source revision `5401f669628a870a9c533c45553c28c91e5724e5a8b414606cecd9d0f219eeac`.
- `.24`, pool complete, unresolved 0: [probability-inspect-991079c10600](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86d44f7e88eefc7ae74da571af448fc7f12b7fe92a1da3892af172449ad538d8/3557c1ca21c7e5518f8fa43530830ce9c6a57524a46da3dc8535def09f565586/probability-inspect-991079c10600.json); source hash `991079c10600fa27cdc9f504c3733bca8131773446da2fdab72eb5b16cd770de`; source revision `f254a3447118e32b564f7a16df5ac50fdc1d379b30a6a2405d267b5e9c8e0817`.

Path-based `.21`, `.22`, and `.24` inspections also returned `INTERNAL_ERROR`; the inline source route succeeded and is the retained evidence. This is a tooling limitation, not a claim that the pools are invalid.

## Evolution source comparisons

All four comparisons used the same 16-scenario set and source objects for before and after.

| Pool | Candidates x scenarios | Analysis ID | Scenario hash | Status | Unresolved | Diagnostics | Changes | Key rendered evidence |
| --- | ---: | --- | --- | --- | ---: | ---: | ---: | --- |
| `.21` | 64 | `probability-341b93e7b5cf0ab5cf68c6eb` | `bc6b135a015e516fdc18f7949dc48989b56cae6d66541248652b9c0c2f94862b` | `PROBABILITY_ANALYZED_PARTIAL` | 3 | 5 | 0 | [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea4ace094938ca5ed2ab5a57a98f48cbae69272db2708318f710d42d980f9cc9/bd001fa242b053fc4cf0fbc1a1170c824c59548b573359f81ac15c5065ca5574/probability-341b93e7b5cf0ab5cf68c6eb.json), [comparison](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/567bf24866dd5adcb637d554bd84e38e7c56020096c060504a1850b008acdb6c/probability-probability-341b93e7b5cf0ab5cf68c6eb-comparison.svg), [unresolved](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a80faa0a3d8c215bcd56d7e51db46af7737e533d75f73f67fea177a82ff90779/d38aeb4289c6c80859eac3acbe1650d7a91aa1003fc2df76fe54f6a1354de80b/probability-probability-341b93e7b5cf0ab5cf68c6eb-unresolved.svg) |
| `.22` | 80 | `probability-cbdff2fe9ccd20f36f4545ae` | `bc6b135a015e516fdc18f7949dc48989b56cae6d66541248652b9c0c2f94862b` | `PROBABILITY_ANALYZED_PARTIAL` | 4 | 7 | 0 | [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81c085f476087bba05dbaa8fda7087a5a5fed54ca7dc2fa6ed1c867ec283e83d/ee8ded0de7ef74ed0340d20b49bcb5d8b9da0ff3bfcd5421d35b8a7da3ab84ff/probability-cbdff2fe9ccd20f36f4545ae.json), [comparison](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/8a1d26d6a54eb24c08f3d05f453bf5e77f3a0042c2d1586cf0b0a1f734dc37b6/probability-probability-cbdff2fe9ccd20f36f4545ae-comparison.svg), [unresolved](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4bc2ccc78ca7fe1c223b1340f7f6d50255f052c7359eec5f0ba15d1c162234af/bb8f7b16681d97c29c41ac0e9d83ddf442752f6cf5305521036eb76af15b4ef8/probability-probability-cbdff2fe9ccd20f36f4545ae-unresolved.svg) |
| `.23` | 48 | `probability-71dee9230e5881188cd2800f` | `bc6b135a015e516fdc18f7949dc48989b56cae6d66541248652b9c0c2f94862b` | `PROBABILITY_ANALYZED_PARTIAL` | 7 | 4 | 0 | [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bab217ea536f0a8d848dcaea48cefaa18abf3b10e8911d9e3eb33ba2b8a446be/7fc4b735340bbffa5379e167d3faa2accaecc8b5f58a57c457edb3f87e81dcb5/probability-71dee9230e5881188cd2800f.json), [unresolved](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26443dd09db1433c4ace0e9df8fa5250c39993f0d199b04765b7e52cbd936c0a/881edfdbbf277e39f18ef5ee0fac43f700d115151fad72af1981053fe6b0e370/probability-probability-71dee9230e5881188cd2800f-unresolved.svg) |
| `.24` | 96 | `probability-f20bd49ab352c21647fed422` | `bc6b135a015e516fdc18f7949dc48989b56cae6d66541248652b9c0c2f94862b` | `PROBABILITY_ANALYZED_PARTIAL` | 25 | 11 | 0 | [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae1a9ff017afb7d1c707cdf603bd188378668b0809c6f80987edbee67ce752ed/2665d793cc4a394c77f6793ea3636f919f389a105b0a9d166ac273b32314c83b/probability-f20bd49ab352c21647fed422.json), [comparison](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/fa0e91dc361d2829f68a5d0b16cda495e27dff30a2640fc5882b22bb12474c9a/probability-probability-f20bd49ab352c21647fed422-comparison.svg), [unresolved](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28480a2f46bed1ecb1489eff78e4de7d3d921fb506bfe933cb810d4c5f544d72/042f6b2b535a786f9a2a53dab13de6431bf20d3f4357b0049a7af2c582653625/probability-probability-f20bd49ab352c21647fed422-unresolved.svg) |

The compare responses reported post-source revision `0d559c43941647903cfef210a401cef5b862ea8786ae94314c46e537858886fb` and post-source hash `e57fb4c295e23440dfb2f79fe24692a802eda357a5c0804f10eb51a29a0c6818` for the inline comparison source.

The compare diagnostics are primarily unsatisfied flavour modifiers and unresolved helper or typed-trigger state. The `.24` pool has the largest unresolved count because several gated options require stage-history and route predicates that the adapter cannot prove from the declared fixture.

The source-level base for every evolution candidate is `constant:brilliant_scientist_evolution_ai.base`; modifiers are the existing preferred, strongly-preferred, cautious, strongly-cautious, and host-flavour factors. No numeric factor or option ordering changed.

The adapter produced no safe exact normalized option percentage for these pools because a complete runtime eligibility pool was not proven. `comparisonChanges=0` means before and after evaluated identically within the bounded adapter model, not that all callers and effects were executed.

## Host-reaction scenarios

Scenario set ID: `E016_HOST_REACTION_BASELINE_2026_09_02`.

The exact named scenario IDs were:

`E016_HOST_REACTION_7_NORMAL_PENDING_HOST`, `E016_HOST_REACTION_7_TERMINAL_DEPARTURE`, `E016_HOST_REACTION_7_SPLIT_KRG`, `E016_HOST_REACTION_7_SAME_TAG_TAKEOVER`, `E016_HOST_REACTION_8_NORMAL_PENDING_HOST`, `E016_HOST_REACTION_8_TERMINAL_DEPARTURE`, `E016_HOST_REACTION_8_SPLIT_KRG`, `E016_HOST_REACTION_8_SAME_TAG_TAKEOVER`, `E016_HOST_REACTION_9_NORMAL_PENDING_HOST`, `E016_HOST_REACTION_9_TERMINAL_DEPARTURE`, `E016_HOST_REACTION_9_SPLIT_KRG`, and `E016_HOST_REACTION_9_SAME_TAG_TAKEOVER`.

Normal fixtures declared a non-KRG current host with the corresponding pending flag, public context, university archetype, a primary facility or custody family where required, and foreign operation targets for `.9`.

Terminal fixtures added departure and world-end flags to the pending host caller.

Split-KRG fixtures declared KRG, secret context, militarized archetype, war, and the transformed-into-Kruger-state marker.

Same-tag fixtures declared KRG, secret context, militarized archetype, war, and the same-tag-takeover marker.
This is a fixture limitation: an actual same-tag takeover retains the original non-KRG host tag.
The KRG-tagged fixture cannot cover that distinction and must not be treated as same-tag root-eligibility evidence.
A retained non-KRG host replay remains queued for the full caller/helper validation pass because this bounded option adapter already leaves both host and sovereign predicates unresolved.

The event-target and war-relation fields for `.9` were declared, but `has_war_with` and the `brilliant_scientist_is_current_host` and `brilliant_scientist_is_kruger_sovereign_country` scripted helpers remain unresolved inputs in this adapter.

## Host-reaction inspect evidence

Broad prepatch inspection found all nine option candidates but did not prove a complete candidate pool because of required `check_variable`, `has_government`, `has_war`, `has_war_with`, and `num_of_factories` inputs.

Broad artifact: [probability-inspect-6c4a133b73fe](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61346a8b519beada7ab7088a4a65417f8564e5bbe404d67e92530e3157608674/eb2c8552fa629755822d075a444c78f0d4720e58bb56e92c4a8cfba572114365/probability-inspect-6c4a133b73fe.json).

Broad source hash: `6c4a133b73fe74ef4153173164627e340db2c1e565381a1e98eb6319d37a07a9`.

Broad source revision: `5047bb5ae8bc4a5f4313c8f251fc9f8ebb2735159feeb2e3f6add9f43e262d29`.

The `.7` inline pool inspection succeeded with three candidates and unresolved 0: [probability-inspect-8df0b0f23d59](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21cc6db5078b8ad611902064a795f80acf51d788a4f55b509cf81760680bcd68/5de6228a4a19c13c395cff60d45fbbc9c5996937d01fe44a67db360e88abeb57/probability-inspect-8df0b0f23d59.json).

The `.7` inline source hash was `8df0b0f23d5925985d353c6503a0872c05aafa7b69b9eb62453d84b2d7073851` at source revision `5047bb5ae8bc4a5f4313c8f251fc9f8ebb2735159feeb2e3f6add9f43e262d29`.

Full inline `.8` and `.9` pool inspections returned `INTERNAL_ERROR`; bounded single-option probes completed but were necessarily incomplete pools. No exact `.8` or `.9` normalized probability claim is made.

## Host-reaction source comparison

The first host comparison attempt was rejected by schema validation because `uncertainInputs` was supplied as an object rather than the required array. That invalid request is superseded and is not evidence.

The corrected source-backed comparison used all nine candidates and all twelve named scenarios.

Analysis ID: `probability-aaed827d584a9bc77d6e3921`.

Scenario hash: `8ed1fc0b9391beaa266077c1c05bf5655c5bcaf64c069cfa1fcdf769a66db3fd`.

Status: `PROBABILITY_ANALYZED_PARTIAL`.

Candidates evaluated: 108 (9 candidates x 12 scenarios).

Unresolved: 26.

Diagnostics: 23.

`comparisonChanges=0`.

Post-source revision: `4e3b6705ac7f8c9bc8e71427bc2a20a273d430aa0ca469e26b73ec353dd9ca26`.

Post-source hash: `cbaef5d52618a20a7e89a708e8ca55e07feffcac85ea247fe1e21c3922c9b909`.

Artifacts: [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1eb375da5b5371e51bd4c132ab6cad4791385379afb31e4eb9c55b131b62742/75679a178224bc351d4ecd9075ddadca15c4810a81bb23d5421991b97c4ca707/probability-aaed827d584a9bc77d6e3921.json), [ranking](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b709fe5f73f0feb06ac5a6da58087f9ffce683962db2f6a3c2ac123c18df01b/9d1c868bb096372f47424217dd1d71d4f7788303263c00fdf93e511cd7361162/probability-probability-aaed827d584a9bc77d6e3921-ranking.svg), [matrix](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43055c2cda9dc7ea51ee2aad0840aee4e281785b0a365cf4e2052b27864a177f/6a3c62065cf205908030001124198f16fb74f5c4959af26df310a87a72dd0ab3/probability-probability-aaed827d584a9bc77d6e3921-matrix.svg), [unresolved](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2daca107759a4948a2b9858aa585edfda9d38e42d72e17f4507068990df38b02/3e1c7854b47e14cffaac86ede7012e2fa0e0ba78b6f0b6fa30c339d83f8bb2d7/probability-probability-aaed827d584a9bc77d6e3921-unresolved.svg).

Every host option uses `base = constant:brilliant_scientist_host_reaction_delta.ai_base`; existing preferred, cautious, restricted, dangerous, settlement, and host-flavour factors remain unchanged.

The compare diagnostics show some declared flavour branches are never active in the twelve fixtures, and unresolved helper/target inputs prevent exact root eligibility. The result proves no option-level weight or ranking change, not that `.7/.8/.9` can fire in each caller state.

## Structural event evidence and root-guard limitation

The available prepatch structural scan for the host file was focused and partial at revision `23d07f38466bd55877a4f79f36a99c34bb9b7f0790f582a264bb307cc60e4646`, with graph hash `38c248ff95d2c1efe04ff3c5a340f4af0f65f201989d8a235d0aec2d3c68519f` and `helpers=0`.

Its artifact is [event-scan-23d07f38466b](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab5e9b9186e17f57896f614bc717dab2ac77894d8de1b6609a9f02a4348042f7/f858b365da50a644b92116eb19b20b459893df57ce431117304126616efd9b2c/event-scan-23d07f38466b.json).

The corresponding bounded options render was rerun at the supported `maxNodes=240` after a rejected `maxNodes=400` request: [manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b563cf1e96440431c9b72dc5ce0f5e4c8e53dce8be35b04163ea1852483e371/56d39df71b7ea4de7c402cb96bf2e648940e5160e751f44cbede89e435017bac/event-options-23d07f38466b-manifest.json).

The structural evidence cannot prove the new `brilliant_scientist_is_kruger_sovereign_country` root predicate because the focused scan did not expand helpers.

The parent also reported that the root event compare cache was unavailable and a source-overlay event comparison timed out at 180 seconds; no full event graph before/after claim is made here.

## Findings

### Exact or bounded findings

- Exact source comparison result for all four evolution option pools: no before/after change in candidate AI chance, modifier trace, or ranking under the shared named scenario set.
- Exact source comparison result for the host option pool as far as the adapter could evaluate it: no before/after change in candidate AI chance, modifier trace, or ranking under the shared named host fixtures.
- Bounded source observation: every evolution and host candidate retains the same symbolic base and modifier factors; no flat, duplicated, or changed numeric weights were introduced by the parent patch.
- Bounded eligibility observation: the added guards exist in the three host event triggers and three host schedulers, and the added evolution enablement guards are present in the four base, four seed, and three prefire blocks according to the source diff.
- Unresolved engine behavior: the probability adapter does not execute the full caller chain, so it cannot prove stage-specific delivery/policy suppression, seed suppression, active-country cancellation, or root host sovereignty exclusion.

### Balance and exploit-risk disposition

No dominance, starvation, rank reversal, repetition, or timing drift was observed in the before/after option comparisons because all reported comparison changes were zero.

No exact normalized selection probability is claimed for any pool whose helper eligibility or complete candidate pool was withheld.

The added gates reduce invalid lifecycle application and invalid host reaction firing; they do not alter the AI weights themselves.

No positive weight on an impossible candidate was proven or disproven for unresolved helper states.

## Recommendations without applying changes

Retain the parent’s `is_current_evolution_enabled` checks and per-stage context assignment; they match the contract requirement that disabled stages cannot create seed, delivery, or policy rewards while existing history remains intact.

Retain the host sovereign exclusion in both event roots and schedulers so same-tag takeover and split-KRG states cannot schedule or fire host-only reactions.

For later engine validation, replay the exact evolution scenario IDs with typed stage-history and active-prefire caller state bound by the adapter or a full event state-flow artifact.

For later engine validation, replay the exact host scenario IDs with current-host, sovereign-country, event-target, and `has_war_with` helpers expanded; the split-KRG and same-tag cases are the highest-priority root-gate checks.

Do not tune `ai_chance` factors from this pass. Any future weight change must retain these scenario IDs and run a new `probability_inspect` followed by source-object `probability_compare`.

## Skipped analyses and blockers

- `probability_sweep` was not run because no weight, MTTH, or timing target changed and the helper-heavy eligibility inputs remain incomplete.
- `probability_simulate` and `probability_sequence` were not run because no uncertain numeric distribution or complete custom weighted pool was declared.
- Separate MTTH and mission comparisons were not run after inspection because both before and after source objects returned `no_weighted_surfaces`, their semantic source diff is empty at `--ignore-space-at-eol`, and the parent directed no additional server-heavy calls.
- Full event `state_flow` and root event compare were not run from this subagent because the parent reported a long-running full call, an event-compare cache failure, and a 180-second source-overlay timeout.
- Full `.8` and `.9` host pool inspections returned `INTERNAL_ERROR`; their single-option probes are not complete pools.
- The first host compare request was rejected for an input-shape error (`scenarioSet.scenarios[0].uncertainInputs` expected an array); the corrected source-object request above is the valid comparison.

These limitations are explicit and do not authorize synthesizing engine proof or replacing MCP evidence with source-only arithmetic.

## References and skills

The required offline Paradox wiki core pages and relevant Event, AI, MTTH, decision, scope, trigger, effect, and event-target documentation were consulted before the audit.

Vanilla documentation consulted included `documentation/triggers_documentation.md`, `documentation/effects_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, and the relevant decision/event documentation.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, `chaos-redux-decisions-missions`, `chaos-redux-event-planning`, and `chaos-redux-improvement-loop`.

No gameplay, localisation, specification, asset, workbook, runtime, or weight file was edited by this audit.

No skill was created or updated.

No completion claim is made; the remaining full-caller and helper-state evidence is a parent/user acceptance blocker, not a waived requirement.

## Artifact-link correction

The malformed comparison-SVG links for `.23` and the host-reaction comparison were removed during the containment checkpoint.
Their exact original URIs could not be recovered from the bounded retained tool records; no replacement URI is inferred.
The valid JSON and other rendered evidence links above remain the available evidence, with their original partial-result limitations.
