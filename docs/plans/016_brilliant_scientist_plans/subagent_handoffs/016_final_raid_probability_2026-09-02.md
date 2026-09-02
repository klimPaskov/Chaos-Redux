# Event 016 final raid probability audit — 2026-09-02

Status: partial read-only audit. No gameplay files were edited, no weights were changed, and no completion claim is made.

## Scope and source contract

The accepted contract is `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.

The audited source surfaces are `common/decisions/016_brilliant_scientist_biological_operations.txt`, `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt`, `common/script_constants/016_brilliant_scientist_raid_lifecycle_constants.txt`, `common/raids/biological_raids.txt`, `common/raids/biological_battlefield_raids.txt`, `common/raids/zombie_weaponized_raids.txt`, `common/raids/zombie_weaponized_friendly_raids.txt`, `common/scripted_triggers/016_dhrondan_contact_triggers.txt`, `common/scripted_effects/016_dhrondan_contact_effects.txt`, `common/raids/016_brilliant_scientist_portal_raids.txt`, and `common/decisions/016_brilliant_scientist_portal_containment_decisions.txt`.

The probability workspace was `mod_chaos_redux_ea3b2d67c2c0`, targeting Operation Postern 1.19.2.0 with adapter `hoi4-1.19.2.v1`.

The required offline Paradox wiki pages, vanilla `documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and the applicable Chaos Redux events, decisions, MTTH, event-planning, and subagent skills were consulted before the audit.

## Portal-assisted biological target eligibility

The owner patch is frozen in the biological trigger/effect/constants surfaces. Ordinary battlefield and military targets are unchanged. The accepted Portal-assisted variant permits rear-area targets only with the Portal technology and 10 `teleportation_equipment_1`; only that variant uses the extra transport debit/refund receipt, and pending validity reads that receipt rather than remaining unreserved stockpile.

The exact five named scenario rows were preserved:

| Scenario id | Contract expectation | MCP result |
| --- | --- | --- |
| `E016_BIO_TARGET_ORDINARY_MILITARY_CONTROL_NO_PORTAL_2026_09_02` | eligible | unresolved |
| `E016_BIO_TARGET_REAR_NO_PORTAL_TECH_2026_09_02` | ineligible | unresolved |
| `E016_BIO_TARGET_REAR_PORTAL_TECH_NO_EQUIPMENT_2026_09_02` | ineligible | unresolved |
| `E016_BIO_TARGET_REAR_PORTAL_TECH_FUNDED_2026_09_02` | eligible | unresolved |
| `E016_BIO_TARGET_PORTAL_RECEIPT_PENDING_NO_UNRESERVED_TRANSPORT_2026_09_02` | pending receipt remains valid | unresolved |

The pre-patch named-set evaluation was `probability-d5182adc518cde3a6feb74ad`, source revision `5df6c38647c90306b1d1ee7d119de2bcb999b6a8c8845186a8277e731a38f379`, source hash `bb6fc750cb7478828e43c258f5165fa0334909cc0200be0dfde0a66dd2059f5a`, scenario hash `f6c367901f29100dfe19655fc917e03c8b2ab87c588ba3aa2324ea050a6af03f`, five rows, 28 unresolved items, and three diagnostics. Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/12afc6e47a5e47659e72d2ab3ea8dac3434c7af7b03febd108dfaf56d39eb5e7/29becde7be6b468fb302fddaa41dc13b0d653831ae94cf4b492743eb9d6dc496/probability-d5182adc518cde3a6feb74ad.json`.

The post-patch same-row evaluation was `probability-768ec67b5a6ef0dba50e8616`, source revision `421bb0fe3411f54825935f8a3047abe83d52135d8d2bc62bf2ea70c40664e5c1`, the same decision source hash `bb6fc750cb7478828e43c258f5165fa0334909cc0200be0dfde0a66dd2059f5a`, scenario hash `351fde87f03bad26383497c332683b991eb79da785483e8e354ae1b0bf4de0af`, five rows, 27 unresolved items, and three diagnostics. Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9867d7db409b72b61053d89efb51a9d8168a8611d8e611cf8b3ffcc0b7a9ff89/77ef1ba4d587060c73bb9696bf0740d809332e8132a6886ab58963b6399b09d5/probability-768ec67b5a6ef0dba50e8616.json`. Rendered post-patch ranking and unresolved views are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fbc1b93e14a27b17a2122a4e47727d6c4a157ac340483e66e8bade2caed4baf/95669a023eae5e03769e258017347a7cd766fffe1417287f9efa4d062fd03359/probability-probability-768ec67b5a6ef0dba50e8616-ranking.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fabad762f9b2d5e99212996a1331ffcea5230f1d817add52a33fc82c886b45f/5b2915d044d8bb8242d0f855b0c6ab2a31013b9c8416215d6e1887b0a36a27da/probability-probability-768ec67b5a6ef0dba50e8616-unresolved.svg`.

All five eligibility predicates remained unresolved in both passes. The adapter does not accept the required country/target scope declarations in a flat `state` fixture, and nested `state.country`/`state.target` attempts were rejected. The unresolved set includes target ownership/control, original-victim matching, Portal technology, transport equipment and receipt state, the ordinary-pathogen eligibility helper, and related actor war/route gates. The one-item unresolved-count difference is not evidence that any target predicate changed.

The earlier calls that passed `probability-...` analysis ids as `before` and `after` were invalid source selectors and are superseded. The final frozen biological source hashes are decisions `a1ed2f6d7b6e1e6296e1e415c0ecce4e925a912c75897d27f4a182ad715b920c`, triggers `02afa9bdb79aafa80d1ae7430d54e5ca576dc7b8053940ac4ae3ae1da2e7268d`, and effects `ded6a1dbf25aa8adb7c8aba20905fb349ed4cac4a7eb45efae4e12f4e511450d`.

The final source-backed Portal/Bio compare cannot be completed because exact pre-patch bytes were not retained. The decision, biological trigger, biological effect, and constants files were untracked before the owner patch and are absent from `HEAD`, so `git show` cannot recover their pre-patch source. The existing artifact is retained as prior post-Portal evidence, but it predates the final active-country/receipt cancellation patch and must not be presented as a final-source evaluation. This is a source-retention blocker, not a `PROBABILITY_SURFACE_EMPTY` adapter limitation, and the helper changes cannot be attributed without the missing before source. The five named rows therefore remain unresolved rather than synthesized.

Recommended evidence follow-up, without changing gameplay or AI weights: rerun the same five ids only through an adapter-supported typed `scopes`/scope-pool fixture that binds actor and target-state variables, or through a declared target manifest if the adapter supports one. Do not infer eligibility from a score row or manufacture a custom pool.

## Biological deployment outcomes

The mandatory `random_list` inspect for the biological deployment outcome source found the complete outcome pool at `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt`, source hash `cb3fd7ac5df4eb054d8c918a5e69862d31dcbf9666635a3bafb42c3795652ea9`. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c926b7c02f2266801666fd80880160f463a0d9afce8612e565155f8f9ba86ee2/ab97abd472bbf711fc4f92d08d75d2b217228916b10e5e01f1d1325aff9747e8/probability-inspect-cb3fd7ac5df4.json`.

The exact evaluation was `probability-9ffbdc27d23dd5a9d3f52466`, source revision `29c7b56efdb754ec0619af728253785505f856eb5e70d911e477d527f099bf8f`, scenario set `E016_BIO_DEPLOYMENT_OUTCOME_MATRIX_2026_09_02`, scenario hash `6aff591b70815cd4bcdc585102c1f05b7758fc1d3d6c77e15d9c8b064b25e507`, and candidate-pool hash `b1995698d7f79318a070aba18900978f70a4f0b6a77b3bc3c927782d341a3d2d`. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ad376b3ca74b0086decfeb33fb716f9c1d8ec07aa3e9f7a09c0faac04acaee9/743578664917af82f4aa393eef3fd9f9264538d7e23cf822f3a05c53fcbf950f/probability-9ffbdc27d23dd5a9d3f52466.json`. Rendered ranking and matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a4af524bcf0a27dba0f47ea58d3def018fb037734917103ace221b55f407a88/7a95e2471b8ab8cc9976ea979a878afc64a9a680c489a38a212fa5dafdc3db4c/probability-probability-9ffbdc27d23dd5a9d3f52466-ranking.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/03e80c49ff56f093cb8690eb6aacbbcf921154cc5d16d12a1cc7b95d1a099e99/a40b448b5600f6b98d41ca08febd52e6882baae7fdde2e7da03de1554c83b841/probability-probability-9ffbdc27d23dd5a9d3f52466-matrix.svg`.

| Named condition | Success | Failure | Accident | Classification |
| --- | ---: | ---: | ---: | --- |
| Battlefield, unstaged | 70% | 25% | 5% | exact conditional random-list result |
| Battlefield, staged | 85% | 15% | 0% | exact conditional result; staged accident is intentionally starved by the authored modifier |
| Covert, unstaged | 55% | 30% | 15% | exact conditional random-list result |
| Covert, staged | 70% | 20% | 10% | exact conditional result |

The sensitivity sweep `probability-b019a11c99c3c5b62bd26464` covered 12 points, reported no rank reversals, and retained the expected staged battlefield accident starvation. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c412be17fa0daa1303496a875dbd8dec4e3b5f0761e6054b7953745bf5897a36/d12dd9daaf61b3d602cd430505a80ddc4ae545e5e6b3b03873407b235bbb1ba6/probability-b019a11c99c3c5b62bd26464.json`.

These are exact conditional shares inside the declared outcome pool. They are not campaign-level raid odds, decision click probabilities, or timing distributions. No outcome-weight change is recommended.

## D'Rhondan rebellion pulse tiers

The current mandatory `random_list` inspect used `common/scripted_effects/016_dhrondan_contact_effects.txt:dhrondan_resolve_rebellion_pulse`; the current entries are `:366.entry.1` (revolt) and `:366.entry.2` (no revolt). Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9eda84d9bc60e25e0aadd924d043542d31d1917f9435e50ac47d5826d60ce1a6/4d410359e46f50a25f3244f69d24cf056f5398dcbe0c51ca9334ffaa8b8f3ff1/probability-inspect-9927b030ceeb.json`. Current inspect source revision is `60aaa05b3d657d5602b3bbc01799567e77b8761b5d6cced1aa35c7d7f50c0bed`, source hash `9927b030ceeb98cc6d76a99c1faa3b3872be1d2294c80cce6318e3a4de6e8a28`.

The current exact evaluation is `probability-70e8470c0b1332a2e3e5e7b4`, source revision `7ff2581eb61309a91385c62d6abde512572af0e5e7e05c5139b6767dc2bd6b74`, source hash `9927b030ceeb98cc6d76a99c1faa3b3872be1d2294c80cce6318e3a4de6e8a28`, scenario hash `0dcdfc20b6ef420234777dc492bf1f23a1827f3b860ebac99d911332e09d4c1b`, nine scenarios, 18 candidate rows, zero unresolved rows, and four diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef9a419f88c1e451989531368aba7effb047e92c863160b42d4ec31b1cbb8f58/3516064d5e9de5bed568a68bfa994b8cfd14f0f29ac2eaf87c58edc691db351c/probability-70e8470c0b1332a2e3e5e7b4.json`. Rendered ranking and matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b8ab23a12b02641b7ee9ab3e344cd0452568c9342d3ba1cac80cadaed20eadd/65e1d52a0a4a788fca256625294a97b440150e1055b03819b679a67b6a3d1ca7/probability-probability-70e8470c0b1332a2e3e5e7b4-ranking.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1f032949c47709113fae1ff45dc357a3798eb4c7fda9004b90fb3440e7c34a6/5c1d2e2bee87a6f8b450df1b6dc45743e8c8e90f841dfc273433d7296e9ab225/probability-probability-70e8470c0b1332a2e3e5e7b4-matrix.svg`.

| Scenario id | Revolt | No revolt | Classification |
| --- | ---: | ---: | --- |
| `NO_CONTACT_BELOW_6` | 0% | 100% | exact conditional pool probe; activation gate not typed |
| `ARRIVALS_6_CHAOS_600_STRAIN_30` | 10% | 90% | exact conditional tier result |
| `ARRIVALS_7_CHAOS_799_STRAIN_49` | 10% | 90% | exact conditional tier result |
| `ARRIVALS_8_CHAOS_600_STRAIN_30` | 20% | 80% | exact conditional tier result |
| `ARRIVALS_9_CHAOS_799_STRAIN_49` | 20% | 80% | exact conditional tier result |
| `ARRIVALS_7_STRAIN_50` | 20% | 80% | exact medium-tier boundary |
| `ARRIVALS_7_CHAOS_800` | 20% | 80% | exact medium-tier boundary when high arrival threshold is absent |
| `ARRIVALS_10_CHAOS_800` | 40% | 60% | exact high-tier boundary |
| `ARRIVALS_12_CHAOS_900` | 40% | 60% | exact high-tier result |

The source trigger currently requires high tier as arrivals at least 10 and Chaos at least 800. Medium tier is an OR of arrivals at least 8, strain at least 50, or Chaos at least 800, and the resolver checks high before medium before the low fallback. This source ordering is consistent with the accepted boundary behavior, including arrivals 10 at Chaos below 800 taking the medium branch when the resolver is eligible. The exact MCP rows above prove only the supplied temporary-weight pool, not activation or trigger evaluation.

The corrected source-backed `hoi4.probability_compare` used the exact named tier rows with `before.inlineClausewitz` from `git show HEAD:common/scripted_effects/016_dhrondan_contact_effects.txt` and `after.inlineClausewitz` from the current file. It returned analysis `probability-d491f178da340465bfd521d0`, scenario hash `94075e1cecd98fc7c4850396fe680b32938962596cd1cdd7a145a31df2344dcf`, 9 scenarios, 18 rows, zero unresolved items, and `comparisonChanges=0`. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/abea0b374213785fc6c91197cbe1c185508e2e5b3c84a96e6b15cef355ef3873/adb43a9aae87e2a9789285c48d5305b9c9d302c31ff5a6931852ea0a4da294b6/probability-d491f178da340465bfd521d0.json`. Comparison and rendered ranking/matrix/unresolved views are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/6e40f6764bb2dbb0dbbf247f86da51d210daed0ce4ac4a107bbeff7be3acbfef/probability-probability-d491f178da340465bfd521d0-comparison.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94fe98147351f3fe397ad394284b69326f809b050400e9880fe9a278236473cc/1990da9b30981ba100cae8a3d90af254f70faa42da349370be8fbd940fe2dfd4/probability-probability-d491f178da340465bfd521d0-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a14295ac2ff578073030bfeb50d2990ee70921ccd4686ecdbe0f253aef7848a6/5833204c308f55dc6e8adc8cb8e42870c8f9fba9d72074da7f282474833e598c/probability-probability-d491f178da340465bfd521d0-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/57f3cc0ccd045276bb1a54948bd737bcb4e5a68e60ef6e31d260c3c410f73eaf/probability-probability-d491f178da340465bfd521d0-unresolved.svg`.

This compare proves the DHR effects random-list pool is unchanged under the declared temporary-weight scenarios only. It does not prove or compare the DHR eligibility/tier helper predicates.

No rank reversal was observed in either exact tier analysis. The dominance/starvation diagnostics at 0/100 and 10/90 are direct consequences of the authored pool values and below-gate probe, not a recommendation to alter the tier weights. No cumulative pulse timing or repeated-campaign probability is claimed because the random-list adapter does not model the 90-day mission cadence.

## Native raid AI, staging, and Portal AI adapter boundary

The biological native raids and zombie raid variants retain their own native raid reservations. Their source `ai_will_do` blocks include `constant:brilliant_scientist_biological_staging.native_ai_factor` under `brilliant_scientist_biological_staging_ready`, and their outcome factors include the staging success, critical, and disaster entries. The contract value is a fourfold staging multiplier plus outcome-factor changes. This is source evidence and a score factor, not a normalized raid selection probability.

The narrow current Portal inspect used `ai_strategy_factor` on `common/raids/016_brilliant_scientist_portal_raids.txt`. It returned `PROBABILITY_SOURCE_DISCOVERED`, source revision `eb96235eae38586c821f6afa2c0292441951098d590aacf5181206994f5e15e2`, source hash `6aae0856c5fc24ad2b7bc8a1523126cd37b7694787d35444972c4f2c766f4d0d`, zero candidates, and `discoveryReason=identifier_not_found` with no available weighted adapter. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9fe4acc4e7c1055025fff1196ae83392402c49d0a421606b8d5975c72ca802b/f8eb6bff1a1beef4866da130661d5d8a1ee34d9b423d9606fc3b2af7fa0659c4/probability-inspect-6aae0856c5fc.json`.

The installed probability adapter set has no native raid `ai_will_do` adapter, so no Portal raid target ranking, staging multiplier trace, raid repetition, or normalized selection probability is proven by MCP. No AI-related tuning recommendation is issued. The separate native selected-unit destruction/full-readiness reconstruction limitation remains an open closure blocker under the parent review.

## Biological decision score evidence

The decision inspect on `common/decisions/016_brilliant_scientist_biological_operations.txt` returned source hash prefix `ed6e3bbcdff4`, six exposed selector candidates, and an incomplete decision pool. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c46f6da3e42b2ae25fbc1e17c8ad90e43e08ede8bde62b6c47a5654708100e9d/0b7e7ea0f2112cb286bf42760fe86dd5233fc31d8a6762c336ee5a22b54d373e/probability-inspect-ed6e3bbcdff4.json`.

The mission adapter inspect with the five declared action ids (`brilliant_scientist_produce_single_biological_payload`, `brilliant_scientist_produce_triple_biological_payload`, `brilliant_scientist_stage_biological_operations`, `brilliant_scientist_battlefield_biological_release`, and `brilliant_scientist_strategic_covert_biological_release`) returned a complete score-only pool with 11 required inputs and zero unresolved inspect items. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0800c37c152dfd52833c407bee20fd021763d3b94bbdf684471d5caa7181b061/172f0c4859b8561f1b89c8d7930ea4cae6541cbbed031b3c1d48b68afb53ce9b/probability-inspect-bb6fc750cb74.json`.

The available mission score model reports raw AI willingness and ranking only, with `normalizedProbability=false`, `rawScore=true`, and `selectionRule=score_only`. The empty-fixture evaluation `probability-2656400d8492ca4532758e08` returned partial unresolved score traces rather than exact decision scores; JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88751e942e309f4fb898e4a104cd58808694e275a6dfb1379992d88f6ea0ddfd/ff07ee67682fb72a06496da7906a136bb4ef050ce2c16cf0ae9da30f4e2c5435/probability-2656400d8492ca4532758e08.json`.

Therefore no decision click probability, route dominance, starvation, or cadence claim is made. Score races must remain separate from the exact outcome-pool shares above.

## Findings, recommendations, and blockers

No weighted-surface rank reversal was proven for the exact biological outcome pool or the current DHR conditional tier pool. The staged battlefield accident zero is an intentional authored outcome modifier and was not treated as a weight defect. No AI weight recommendation is issued pending a complete target-scoped MCP fixture and native raid adapter support.

Open blockers are the unresolved Portal target scopes, missing pre-patch biological source bytes for a valid Portal/Bio compare, the absence of a native raid AI adapter, the unmodeled pulse/raid cadence and terminal transitions, and the parent-reported native selected-unit destruction/full-readiness reconstruction limitation.

Skipped analyses are seeded simulation and sequence analysis because no uncertain input distribution or complete custom lifecycle manifest was declared. No gameplay or AI changes were applied. Remaining conclusions are exact only where explicitly labelled conditional; target eligibility, native raid AI, campaign timing, and decision selection probabilities remain unresolved.
