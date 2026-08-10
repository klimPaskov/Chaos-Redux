# Event005 Probability Completion Handoff

Date: 2026-08-09
Scope: Event005 decision AI, mission AI, event option AI, random lists, national-focus AI, aftermath option lifecycle, reusable MTTH coverage, and AI-strategy adapter coverage.

## Result

Every Event005 weighted surface supported by the installed HOI4 MCP probability adapters has an explicit candidate pool and named scenario contract with zero unresolved inputs.

The former partial inputs and categorical-pool collision are resolved without a fallback. Events `chaosx.nr5.30`, `.31`, `.32`, `.33`, `.34`, `.35`, and `.37` use distinct `.a`, `.b`, and `.c` option identifiers and localisation keys.

## Decision And Mission AI

- Decision AI inspected 211 candidates and 51 required inputs. Analysis `probability-046dcaa0c9857d85cc773f1d` covers 422 scenario-candidates across available-resource and wartime-denial states with zero unresolved inputs and zero diagnostics; authoritative JSON SHA-256 is `6a7b20b9b5055a7836b856bd5682a9ff47b3098da092324cad663432772ad3a8`.
- Mission AI inspected five candidates and 11 required inputs. Analysis `probability-60a3e4d0f1d5531997f1d860` covers ten scenario-candidates across the same two world-state families with zero unresolved inputs and zero diagnostics; authoritative JSON SHA-256 is `dfd045d7ea032ce16bfaf894017b92e99fc7ea46e0e5681b9f30c065df269700`.

## Event Option AI

The current event-option inspection contains 184 candidates in 141 local pools, including 21 multi-option pools. Every multi-option pool was evaluated independently under two complete named scenarios with zero unresolved inputs.

| Pool | Analysis | JSON SHA-256 |
| --- | --- | --- |
| `chaosx.nr5.2` | `probability-4361b07ba45bf90427f32083` | `39cf39e0f9c5b89ad6c51a942d256ad234c57455fb78ce8b7aeb572176b13408` |
| `chaosx.nr5.30` | `probability-9302d2303b238cdd2c4e7109` | `291c8d7665f629af0f20cc0bce124f34b0f4692daabc31e049bb9a83b9a6145d` |
| `chaosx.nr5.31` | `probability-f1b6d15b0661525a316b63f5` | `6eacbf21f771d62b40717422f5e71a688fcbc3509ccfababcb04d916379fe168` |
| `chaosx.nr5.32` | `probability-a20f021882e408ac63c1349e` | `8678b8cf4826b58674123646e6b878635d899615c8cae121433dd0cc5203db81` |
| `chaosx.nr5.33` | `probability-f0f4bc34292ccf15c5eefe77` | `b941dad08e0c329ac4e8a7f33157889e4786c4c2abe150fba7b6dfb9dabb7b10` |
| `chaosx.nr5.34` | `probability-9a73f57c2853aceedabf7c6b` | `236445994f33af81fed594bbf2dfa997797c82627cb04358724afb439bcdc742` |
| `chaosx.nr5.35` | `probability-8a02fb841b817b0465874483` | `df7bec09d14c6c8c353950dded7e0fbdf9f577df48acf56400932a58beb166ef` |
| `chaosx.nr5.37` | `probability-5e3e97eec6b1c11cbe72f27d` | `64591b386d196e31ce17c3fe98cfc45b376bc0d06a13c4b6e8e350087fcbba2b` |
| `chaosx.nr5.60` | `probability-569eb087376837d90cdf6f9a` | `6d676dc5d4562547b29abea7de92940b770ca4195c89b7b95f52a4bc3525b819` |
| `chaosx.nr5.61` | `probability-7337497826e6ddacdd7bf731` | `f050d7920cac29de37da5c64f277b61f7a744fbc18eb71ee098181c5f87516e3` |
| `chaosx.nr5.62` | `probability-335483609ba68dee01d7b8f5` | `d8375bd3a6cf2451497a0615fcd7561468431bd3a6186fe026c83a19c53305c8` |
| `chaosx.nr5.63` | `probability-b79fbd8795683a6587afda26` | `982badfb89cf8cc658084df6d809cd23a612c544cc413c5ba18eb8e77a943cc3` |
| `chaosx.nr5.64` | `probability-50342881c1c0f70e329cea1f` | `dfdd85c5cb79e3c525dbcaf459d52aae45a071d6ece9ea3150c88bec02e9348b` |
| `chaosx.nr5.65` | `probability-dd718a257475b985ef8b86db` | `43c4aa1495c2efa39bfd4c03dc750d2d343163eb7e4d3f8b812ed4227e8cd197` |
| `chaosx.nr5.66` | `probability-db3034e9f1df63d6db95a5d5` | `0729d41d8247c6f8c8f6f623348793ed4d9e9b0bfdd8685616cb25ec6620483d` |
| `chaosx.nr5.67` | `probability-cb9f98ad0a7f06d54ee6860d` | `8d8d25a633fbb162aa7edfa587857fee1e9c66d5525f4eef15b954335d3b0f6a` |
| `chaosx.nr5.68` | `probability-878cb56e2b55f190718f9601` | `9697ab41fb9d5474e5649254e84fcaaf723535033800c9a72f3d3b44f7f6e678` |
| `chaosx.nr5.69` | `probability-6c6e47a02d8a2e5fe590889a` | `59f5c15f3633368f0c094c00be505ac88170f2a2d7df6e8a2e334ba24cafbf37` |
| `chaosx.nr5.70` | `probability-3c1074cabfbb2940261668ab` | `9a3d0356c67ca7d94a8b84cf94c8a3f7cee7af930cbff448739db2f857f9c032` |
| `chaosx.nr5.96` | `probability-448ba3a09bf24ba0fb8e0177` | `21492de7ff87c68c0a786b224b9833e56b0b0bde17c9dba4de8c9eeb40134c64` |
| `chaosx.nr5.97` | `probability-a9ca3ea974935bbc4ccfe2eb` | `79cdb87459df9811979936f5660d9c784fdc22d0d684a43852d2ee4f0e1c0ef5` |

The 120 single-option pools are deterministic local pools with conditional probability 1 when their option is eligible. They require no normalization against another candidate.

Event `.97` reported only `EVENT_OPTION_FALLBACK_NOT_PROVEN`, not an unresolved input. Focused event state-flow revision `9dbc4fde7ed472c6ca5aad7e98180e911786c35adb499eeae1dc17f2c543d4e9` proves that `.96` has three branches and `.97` reads the three corresponding country flags; the focused state reports contain zero blocking diagnostics, so an unconditional fallback would weaken the exact lifecycle and is not used.

## Random Lists

All four Event005 `random_list` pools were evaluated independently under contained and rupture scenarios with complete numeric weight inputs, zero unresolved inputs, and zero diagnostics.

| Source pool | Analysis | JSON SHA-256 |
| --- | --- | --- |
| line 5,389 | `probability-bc5e2db448d1d2bb281cfbd6` | `236b5e90970b793fde63b8b0555d746a96519b88792c541dde9516a9a5208bc2` |
| line 25,099 | `probability-75419a5458b6acc3399ed71b` | `a1f2ce6c03392c443f260248f7cfbe0ebf74aa505f56bd5b30da8ff1ba0d794e` |
| line 26,029 | `probability-080bc0f16f284358bf8ca13d` | `a56cde09aebe09bf9d17467b891cb53557fd14ba84788e7933fe7bd02753d599` |
| line 26,402 | `probability-5cb84bb608ff6cb95ae78ca3` | `638f6f86ebf4069b72f254d972b3ad7fc35002b7bb7242d2b4c4bda866cb22f1` |

## National-Focus AI

The four focus files were inspected as complete pools containing 515 republic, 1,035 custom-splinter, 134 factory-successor, and 76 ancient-restoration candidates. Peaceful-reconstruction and wartime-pressure scenarios declare every required input, `focus.external_factors_complete`, and an explicit ownership mask for every candidate so only the active country's tree participates in its score race.

| File family | Analysis | Scenarios | Scenario-candidates | Unresolved | JSON SHA-256 |
| --- | --- | ---: | ---: | ---: | --- |
| republic | `probability-1192f15bf998c24d65f5046d` | 2 | 1,030 | 0 | `bbdc544a3bc3ed1fdd870f24cbadc657f54981d6270eb44abb59398249fdfa4e` |
| custom splinter | `probability-8463f04392b0b4ce37fb0420` | 2 | 2,070 | 0 | `97bb64bf71e1e0c1596278d25212535af15ede1bf2cc20aebd71b6b262e77921` |
| factory successor | `probability-640d24171d6b715b9cf6559d` | 2 | 268 | 0 | `6a1fa7a4ca8ee536b3cd8bc2e860a13dd237478f837218b7bd87035f78f3a57c` |
| ancient restoration | `probability-ee244408f83cb173eb4e3be0` | 2 | 152 | 0 | `c0496f5de0f1360cf3c792a213c0c5734ed6e7c57ac171dbf2d0f24910c2fb3b` |

Ownership-excluded focus diagnostics record that another country's focuses are ineligible in the named actor scenario; they are expected proof of the ownership mask and not missing inputs. Generic starvation thresholds were disabled where they are inapplicable to a complete multi-tree source file.

## Empty Adapter Surfaces

- `direct_random` reports `PROBABILITY_SURFACE_EMPTY` for the Event005 scripted-effects source because it contains no independent direct-random block.
- `event_mean_time_to_happen` reports `PROBABILITY_SURFACE_EMPTY` for `common/mtth/005_soviet_collapse_mtth.txt` because the file defines reusable named MTTH entries rather than event `mean_time_to_happen` blocks.
- `ai_strategy_factor` reports `PROBABILITY_SURFACE_EMPTY` for `common/ai_strategy/005_soviet_collapse.txt`. This is an adapter-coverage boundary, not a missing scenario input; the 216 source entries remain source-audited, and their focus and decision consumers are included in the complete analyses above.

## Terminal Rewrite Rule

The compact focus-layout rewrite must be the final source mutation. After it succeeds or rejects individual safe proposals, the parent must rerun read-only focus inspection, rendering, probability evaluation, and semantic hashes without editing this handoff or any source file.

No simplification or fallback was used.
