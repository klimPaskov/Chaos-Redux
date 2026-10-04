# Event 014 hidden-hoard probability evidence

Date: 2026-10-04.
Owner: implementing agent (Event 014 takeover, round 1).
Disposition: `implemented` for the baseline and same-scenario comparison of the new hidden-hoard AI weights; decision selection among real targets remains for live observation.

## Surfaces

- `chaosx.nr14.82` options `.a` (confront), `.b` (tolerate) and `.c` (bargain): adapter `event_option_ai_chance`, complete local pool.
- `cannibalism_unified_investigate_hidden_hoards` and `cannibalism_unified_seize_hidden_hoard`: adapter `decision_ai_will_do`, score only.

All weights use the existing `cannibalism_unified_decision_ai` levels and factors (high 25, standard 10, preferred x2, cautious x0.5, invalid x0); no new AI constant was added.

## Route notes

`hoi4.probability_inspect` returned `INTERNAL_ERROR` with no artifact for both adapters, including the unchanged `chaosx.nr14.71` pool, for path, identifier and inline sources.
`hoi4.probability_evaluate` and `hoi4.probability_compare` worked with path and snapshot sources.
A compare against the pre-change HEAD source is impossible because the candidates are new (`PROBABILITY_SURFACE_EMPTY`), so the same-scenario comparison uses a neutral baseline: the current file with every new `ai_chance` or `ai_will_do` replaced by `base = standard` and no modifiers.
The neutral snapshots lived in the ignored `.tmp/e014_hoard_probability/` folder: events SHA-256 `4ca0e71e61ce045e9a1ced93c4432f232c608731a491480f86faef2d9b75e719`, decisions SHA-256 `74f8508aad6d8d1836aab142dd509367446add72972aa878b32b5f98f88e8eba`.
All scenarios are declared synthetic inputs, not observed campaign state.

## Event options (`event014_hoard_review_r1`)

Baseline evaluation `probability-3ebabfba947130945e1fd2e3` (`PROBABILITY_ANALYZED`, complete, 0 unresolved, scenario hash `04aa69328427ac0828b1d7007453f128bb927d10cd2b03109670b7a4014f1992`, source revision `cf6e6db5844b9919a11b88571bd80e18a85a7f73789aba555b1a3514ef57e735`).

| Scenario | Confront | Tolerate | Bargain |
| --- | --- | --- | --- |
| `cbl_break_peace_absorbed` (break route, peace, Larder 900) | 50 (58.8%) | 10 (11.8%) | 25 (29.4%) |
| `cbl_keep_war_governor` (keep route, war, live governor) | 12.5 (16.1%) | 40 (51.6%) | 25 (32.3%) |
| `cbl_chain_low_larder_located` (chain route, Larder 40, located cache) | 50 (31.3%) | 10 (6.3%) | 100 (62.5%) |
| `wendigo_host_short_of_command` (no route flags, war, 2 Command Power) | 25 (71.4%) | 10 (28.6%) | ineligible |

Comparison `probability-2ad0e67d44023f655b0f0948` (`PROBABILITY_ANALYZED`, complete) against the neutral baseline reports 11 changed rows over the same four scenarios: the neutral pool splits evenly between the eligible options, while the live weights follow the warlord-settlement route, the cache's location, a governor at war and a short Larder as tabulated above.
The unaffordable bargain stays ineligible in both sources.

## Decisions (`event014_hoard_decisions_r1`)

Baseline evaluation `probability-69af205d445422372cef383a` (`PROBABILITY_ANALYZED_PARTIAL`, scenario hash `82c416d6bb1700948255a4d20bb7b4defae173b132f7d45dd928efb7f3ab114f`, source revision `1b92fc5226f448c425a8c2c45c6bfaa1f093812b132de8d2d4a69ba4c3e8bd77`); eligibility is declared through candidate overrides.

| Scenario | Investigate | Seize |
| --- | --- | --- |
| `cbl_break_low_larder` | 100 | unresolved |
| `cbl_keep_stocked` | 25 | unresolved |

The seizure score is unresolved because its first modifier is the meta-trigger force check (two divisions already in the target state), which the scenario cannot declare; with the force present the score is 25, or 50 under low Larder, and without it the invalid factor makes it 0.
Comparison `probability-71ae07f2d0478605191389cb` (`PROBABILITY_ANALYZED_PARTIAL`) against the neutral baseline reports 4 changed rows with the same unresolved force check.

## Limits

Decision scores are not normalized by the adapter, and the state targets of the seizure decision are not enumerated, so no statement is made about which cache the AI picks.
How often the AI actually stands two divisions in a cache state is campaign behaviour for live observation.
