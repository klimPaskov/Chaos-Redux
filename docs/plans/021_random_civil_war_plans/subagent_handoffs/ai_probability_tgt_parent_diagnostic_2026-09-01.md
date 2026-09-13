# Event 021 target-weight parent diagnostic

Date: 2026-09-01

Status: Current manifest-backed parent evidence; not an independent `chaosx_ai_probability_auditor` certificate and not live-game proof.

The parent recovered the installed HOI4 MCP `customWeightedPoolManifest` schema and declared the current `event021_random_civil_war_prepare_target` arithmetic from `common/scripted_effects/021_random_civil_war_effects.txt` and `common/script_constants/021_random_civil_war_constants.txt`. Boolean source branches were represented as explicit zero-or-one scenario inputs. The invalid or reserved gate multiplies the score to zero and the candidate eligibility gate excludes it, matching the source helper's fail-closed minimum behavior.

`hoi4.probability_inspect` completed with `PROBABILITY_SOURCE_INSPECTED`, one complete declared candidate, zero unresolved inputs, source hash `8132d1cc046b40c885799b1dcd5d05a6980925bac4202fe1256b131a8f43dab2`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/83d072d8ae2a74aea75637659ef3f0ebaf5cf6853a8f482f26333b82964a8952/52ea2288aa8db6656afe73731d8ffcd96ae4172cead12ca968731e15856730ed/probability-inspect-8132d1cc046b.json`.

`hoi4.probability_evaluate` completed with analysis `probability-75458d26511189833fd24427`, scenario hash `29240122aa242e26156dda7b172370506bbb5823b14d53054c5fd0566feeb8f9`, zero unresolved evidence, and authoritative JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c55b09805cb98885e7b2881831e92bd9dd49b233af6d30b80bc117acbe64b72/44399017e8619eae29d8136e70ddc77f3d389e32b2fb1ccd8c4a9d7fd986f820/probability-75458d26511189833fd24427.json`.

| Scenario | Raw weight | Eligibility | Conditional probability | Result |
| --- | ---: | --- | ---: | --- |
| `TGT-STABLE-ELIGIBLE` | 122 | true | 1 | Pass: stable eligible target retains live weight. |
| `TGT-WEAK-ELIGIBLE` | 916 | true | 1 | Pass: weak target has substantially greater raw weight than the stable fixture. |
| `TGT-INELIGIBLE-ZERO` | 0 | false | 0 | Pass: no valid target contributes no live weight. |

The dominance warnings for the two eligible fixtures are expected because each scenario intentionally contains one abstract candidate and tests its raw score and eligibility rather than a multi-country normalized distribution.

Three specialist attempts on 2026-09-01 did not produce a replacement certificate. The first rejected an invalid source-less adapter request before the manifest schema was recovered. Two later auditors received the validated manifest and exact two-call workflow but remained running through bounded waits; one also remained running after an explicit stop-and-report instruction. Their handles were closed. The successful parent calls prove that the manifest and probability service are operational, but repository policy still requires the independent probability-auditor certificate for final completion.
