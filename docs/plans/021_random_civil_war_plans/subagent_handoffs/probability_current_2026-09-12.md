# Event 021 Current Probability Evidence — 2026-09-12

Status: targeted parent-owned evidence, not a complete independent acceptance certificate.

This handoff records the current read-only HOI4 MCP probability receipts obtained for Event 021 after the sponsor resource guards, route-proof repairs, exposure marker repair, and current source review. No gameplay file was edited by the probability calls.

## Archetype pool

The current source exposes six candidate entries at `common/scripted_effects/021_random_civil_war_parent_effects.txt:1120.entry.1` through `:1120.entry.6` through adapter `random_list`. Inspection returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, six candidates, six required inputs, and zero unresolved inputs.

Source revision: `2c799900fb7ae0d0e45f37fe7dfc7ce2927b547294d57eeca3cd298afe4f94c5`.

Source hash: `ac4d84b98a34cfc4b7cde74ac8849cadc6c30e06f06664ab12c4d1744901c70b`.

Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741705cc7f70606b09a879b65477be222924deecc5cd5e323867548d7b46469b/3162987153d14ef316202d27cc925f56ede734241469e880d56d04fb34e59648/probability-inspect-ffe0c7fe9093.json`.

The eight-scenario evaluation `event021_archetype_current_complete_2026_09_12` completed with 48 candidate rows, zero unresolved inputs, validation passed, and 45 warnings. The warnings come from intentional one-route fixtures that produce dominance or required starvation. Analysis: `probability-53cc39be84893b94175e5eed`.

Evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d24e9a7b1b18d4d42e659f175d75d40050cf8a25aa1d88f84286d2f816de5cbe/6e05222b99140abe8f2010f588e4a966a752854a9f474b068ddfacfd1713656a/probability-53cc39be84893b94175e5eed.json`.

The nine-step sweep `event021_archetype_sweep_2026_09_12` completed with 16 sweep points, zero unresolved inputs, and no reported rank reversal. Analysis: `probability-b2ea2bbce037cf44d49864b7`.

Sweep artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e304bc2156238b0e7de9ce81f5c1d1262b29db5192f0148acd8adc52e928c324/2bbd1beea2dfc77074284a8cec63e332dee225e703b851dd8472cd5ec07e23f8/probability-b2ea2bbce037cf44d49864b7.json`.

The seeded pseudo-random simulation `event021_archetype_simulation_2026_09_12` used 2,000 samples, seed `21021`, and a 180-day horizon across eight scenarios. It completed with zero unresolved inputs and validation passed. Analysis: `probability-33fff2831771945b5f7757fc`.

Simulation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50958d46e6bebc3c511a70bbf15c886d0cf448e8bffe4ac3a397121e70ab0bfa/793c0594670402e4efd943840482fa3037682e84961e8b6f843bd8b4068c27ce/probability-33fff2831771945b5f7757fc.json`.

## Sponsor decision comparison

The current sponsor decision inspection found `event021_support_government`, `event021_support_opposition`, and `event021_offer_mediation` as a complete three-candidate score-only pool with seven required inputs and zero unresolved inputs.

Source revision: `a6e750bba8366c9665e9863cec65323e0af02bbd39e46ab742f3823d6278eb87`.

Source hash: `ffe0c7fe9093ea2e125ea0ef6eaac03cf66e91395d057cd5682e694233e6f89a`.

The same five scenarios were compared against the readable pre-repair snapshot `docs/plans/021_random_civil_war_plans/probability_snapshots/sponsor_resource_guard_before_2026-09-02/021_random_civil_war_decisions.txt`. The comparison completed with 15 candidate rows, zero unresolved inputs, zero diagnostics, and five attributed changes.

Analysis: `probability-245b599b71315c1bb338e11a`.

Comparison artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c1d669058245dc4652b7229bc34783aaaa2b7b79127f67226d854b5c8447f56/9354dafbb14c11695a33c4f3fb977d084135ca1b99618db2ae743fc0b8238380/probability-245b599b71315c1bb338e11a.json`.

The source delta raises government support from `1.5` to `1.6875` in SPN-01 and SPN-03, applies exact-zero support rows to the mediator profile in SPN-05, and leaves mediation at `1.5`. These are raw score changes. The installed decision adapter does not provide normalized action probabilities.

## Bounded scheduler admission sequence

The manifest `event021_scheduler_cap_sequence_2026_09_12` models the normal review, Critical queue, and nested crisis admission layer with a fixed 15-day timer, theater cap 5, front cap 10, generation cap 2, explicit per-candidate caps, and source-bound eligibility expressions.

The current MCP certifies the no-transition admission layer with exact state distributions and zero unresolved inputs. GLB-01 has exact next-selection probabilities of 0.50 normal, 0.25 Critical, and 0.25 nested.

GLB-01 artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fb1f31d9c4c9cccf674881c7f6fca96ca907df34e98867b3395a9314cf4df2e/c28316200889992182aedf2b5174c487ffdcf09e4103fa4b3c6044caefe5f4ba/probability-e92c6847cbe87f754b5dbe5a.json`.

GLB-02 excludes the Critical candidate at the front-cap boundary and yields 2/3 normal versus 1/3 nested.

GLB-02 artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b90da3712d8fb7c1642f596def1664afc361425dedd80dad6bc00308ca4bebf/1031da3cf759eaac00ca1563832951e6ac9932abf33a4d400855fcb6c591b99c/probability-6ba0dc4de1d04f0e56e28a73.json`.

GLB-03 excludes every candidate when theater and front capacity are saturated.

GLB-03 artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80fcf04ec3a04dccaa6bc3fd86649beb3372602a0e4b471e0b21794c1dc5563b/a5a46b3956c7bd7a95b12f0e4f28cd398a3bf003de35c80f75caa308b77d7cba/probability-833e70aaf8cedd0b34d2e63a.json`.

The separate full-lifecycle transition manifests returned unresolved `selected.*` transition conditions in the current MCP route. Therefore this handoff claims bounded admission-cap evidence only. It does not claim recurrence, settlement, cleanup, or gameplay-effect execution.

## Disposition

These receipts are useful current parent-owned evidence. They do not close the complete TGT, ARC, SEV, EVO, FRT, SPN, STR, SET, REC, GLB, CLU, and SCN matrix, nor do they replace the independent specialist certificate that did not return. The Event 006 content-gate repair and the initialized Collapse State Authority repair occurred after the inspected source revisions. A fresh current-checkout full certification remains open.
