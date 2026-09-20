# Event 006 probability-source refresh — 2026-09-20

Disposition: read-only evidence refresh / no balance or gameplay change.

This receipt reruns the required `hoi4.probability_inspect` discovery pass against the current Event 006 weighted sources after the documentation-only focus reconciliation.

## Current discovery results

| Surface | Adapter and source | Current result | Boundary |
| --- | --- | --- | --- |
| Outer automatic allocator | `random_list` on `common/scripted_effects/006_independence_wave_effects.txt` | `PROBABILITY_SOURCE_INSPECTED`; 14 candidates, complete pool, 14 required inputs, zero unresolved inputs, zero candidates available under the empty fixture | Declared outer totals are inspectable, but this is not a campaign distribution. |
| Nested package planner | `random_list` on `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` | `PROBABILITY_SOURCE_INSPECTED`; 126 candidates, 126 required inputs, incomplete pool, one unresolved input, zero candidates available under the empty fixture | No nested package probability, dominance, starvation, repetition, or rank-reversal claim is valid. |
| Decision scores | `decision_ai_will_do` on `common/decisions/006_independence_wave_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED`; 13 candidates, 89 required inputs, incomplete pool, zero unresolved inputs, zero candidates available under the empty fixture | This is a score surface, not a normalized click probability. |
| Mission scores | `mission_ai_will_do` on `common/decisions/006_independence_wave_decisions.txt` | `PROBABILITY_SOURCE_INSPECTED`; 72 candidates, 54 required inputs, incomplete pool, zero unresolved inputs, zero candidates available under the empty fixture | Mission ranking remains incomplete without typed gate state. |
| Focus scores | `national_focus_ai_will_do` on `common/national_focus/006_independence_wave_focus.txt` | `PROBABILITY_SOURCE_INSPECTED`; 184 candidates, 17 required inputs, incomplete pool, zero unresolved inputs, zero candidates available under the empty fixture | No focus-selection probability or balance claim follows. |
| AI strategy factors | `ai_strategy_factor` on `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` | `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces` and zero candidates | Source strategy assignments remain score inputs without adapter-backed factor comparison. |
| Event MTTH | `event_mean_time_to_happen` on `events/006_independence_wave.txt` | `PROBABILITY_SOURCE_DISCOVERED` with `requested_adapter_empty`; the adapter suggested 22 `event_option_ai_chance` candidates instead | No Event 006 MTTH timing distribution is exposed by this adapter. |
| Root event options | `event_option_ai_chance` on `events/006_independence_wave.txt` | 22 candidates, incomplete pool, 13 required inputs, one unresolved input, zero candidates available under the empty fixture | No normalized option probability is claimed. |
| Support event options | `event_option_ai_chance` on `events/006_independence_wave_support_events.txt` | 154 candidates, incomplete pool, 46 required inputs, one unresolved input, zero candidates available under the empty fixture | No normalized support-event option probability is claimed. |

The direct-random discovery pass on `common/scripted_effects/006_independence_wave_effects.txt` correctly redirected to the 14-entry `random_list` surface and found no separate direct-random pool.

## Current artifacts and source hashes

The outer allocator artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9508859f9ad77321585ba529f35b0da4713becb2299baed7b01c0fef8bdd3356/06095c2316da46071553e64d9c0300e5c6167698f56e08d3beb8ec5903138cc0/probability-inspect-81c56ee8edae.json` with source hash `81c56ee8edae354bdfd6e5368439d77c565a86cf631dc4d97e9917c1265a6d13`.

The nested package artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00745eb5211fc957009ddbc73f627cf449916025e2291ca9482fde67346183af/016dba8a32665b777e8c5893fbe703cacbe2bb853a92713fb496bdf5010f4227/probability-inspect-17e35c209602.json` with source hash `17e35c209602f859bd3e5b71bd6b394aa613d7d8686e0d07f1d8ee3b803585e6`.

The decision-score artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a07be83c19f288ddd1613a987e66e0c9899f570d3fb4cd503bfdd49395c32d/3d6cf4b5b8abc60cce14aeca9a012f369791da49806bf9cb95ff62fa5686d4c7/probability-inspect-56ce1f4c9325.json` with source hash `56ce1f4c932577f3413cdd7f71196f3a283ac2f194ce48f8b3d44224c24593d2`.

The mission-score artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c4708873143407fa24152b04a56b040f99ab3e8b85be59e35f2f00dcb7d6c99/ff375c43bbcc22805f6a585ea3f3f32295595aef503720caf99c1646a224eef5/probability-inspect-56ce1f4c9325.json` with the same source hash `56ce1f4c932577f3413cdd7f71196f3a283ac2f194ce48f8b3d44224c24593d2`.

The focus-score artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c69437b1696782847372275316e54c6d03671c7ede41dd4b819f1f476a8e12fa/8a5c79f4ee9643e70af29db7e7730090739fcc7924da31557928b40a73475f6e/probability-inspect-d4970a31fc37.json` with source hash `d4970a31fc37dc20a72a88f0424eb21920d2727318674b01b82eba64f1ee576b`.

The AI-strategy artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67c6693e1f67a010df384d83563628db3dadd024b2df4af26c5bb51c4d2fc454/95d4c1b07b3c3881515255a7ab957466b629ba39b7993d4c585001d547746dc9/probability-inspect-b84ee2ca17f4.json` with source hash `b84ee2ca17f45793196641dd0d383779fb2e36ab29da6a1ee2d90912ec82deb6`.

The event-option artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f70e5305ac367f07f397b3bdfbdcbe26a4313ca5c44ae704925d276b51b7ab8/c9bb1ca26a7016474604f1844bd6109fc7b4a8d44ee9916047c7ec69f48dd1b2/probability-inspect-1257ea0e6330.json` with source hash `1257ea0e633018078f75a4b22931bd46666d1ed8e72d22f6708262b9ffe5d961`.

The support-event artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7782d68dbeb93af3890ba5300036dd46f0fe26f5125a412ad736d40409b6b05/313bb3103f234d6d4952240faf90ce9a8d819435f2cc0e3d74d144f7fa7da55e/probability-inspect-4d7ed5adb1d7.json` with source hash `4d7ed5adb1d7c26803d1771ba98d4a3c9149fb2e2661d3ff0e770edbcf613437`.

The MTTH discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c636c34d9aa59f50dac6efec0399d62d2a98533cbcce7cfc5a85ca770f6e3c8/897665bad552c35f632f142eb8ed17e0663e79d307f5f9dc90c57cf4699e4ee3/probability-inspect-24209960336e.json` with source hash `24209960336e274ec644436436e692c07fd3c9c0f9585d041053209210614200e1d`.

## Balance boundary

The earlier 2026-09-19 outer-allocator and two-entry formable-congress evaluations remain the current exact declared-fixture evidence; this refresh changes no source weight and does not supersede their scenario results.

No `hoi4.probability_compare`, sweep, sequence, or simulation is warranted by this refresh because no owner-applied weighted patch occurred and the nested and score surfaces remain incomplete or empty under the available fixtures.

The current required `chaosx_ai_probability_auditor` route remains responsible for the final bounded audit handoff; this parent receipt does not promote direct MCP inspection into typed campaign balance evidence.

No AI weight, MTTH, random-selection weight, decision score, mission score, focus score, strategy factor, or package admission was changed.
