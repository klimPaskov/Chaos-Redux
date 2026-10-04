# Germany Mengele report `.10` current-source probability qualification

Status: complete MCP evaluation of the four-option local pool under two explicit source-consistent scenarios; no claim about actual event fire cadence, live engine option selection or later deaths.
Installed HOI4 MCP 3.6.0 was version-checked and its inspect/evaluate tools were listed before use in an isolated workspace.
`input.json` supplies the exact current `events/germany_mengele.txt` path and `.10` identifier, all four option IDs, top-level dates, the state-88 controller map, German and Polish scope bindings, the stored German responsible-country pointer, relevant flags and source-trigger inputs.
It supplies **no candidate eligibility overrides**.
The synthetic `has_cosmetic_tag = GER` and zero infantry-derivative family values resolve unrelated special-country classifier branches; they are declared evaluator inputs rather than observations of a save.
`manifest.json` verifies that the full source file remained SHA-256 `ecdec59f0ec0069cd6c81b6504434745723318cf8981136386b6f0368171d4d0` during the run and records hashes for all nine saved inputs, wrappers and MCP artifacts.

The identifier-qualified inspector found the exact four candidates with `poolComplete=true` and no unresolved inputs.
The evaluator returned `PROBABILITY_ANALYZED`, `analysisStatus=complete`, zero unresolved candidates, source hash `ed1c70133d90e49dcbda857ba71982caaef8724fec902a76b15b6187f772eefc`, source revision `ad96087f1f8670eec9d403467cc7c918f407f2bdc44ee59d05e6b281f232415e`, and scenario hash `26dc4381026c2618fcd203c7e4b940d5c1ede4eeaf8fd17f20e24b2b60035e02`.
The [matrix PNG](probability-probability-9936a9ed103663831c7b1f97-matrix.png) was visually inspected against the saved JSON.

| Declared scenario | `.10.a` | `.10.b` | `.10.c` | `.10.closed` |
| --- | ---: | ---: | ---: | ---: |
| GER controls POL-owned state 88 on 1943-06-01 with eligible experiment authority | 15% | 65% | 20% | 0% |
| POL controls state 88 on 1943-06-01 while GER retains the other declared inputs | 0% | 0% | 0% | 100% |

These are exact **conditional option shares** for the declared complete local event pool, not the probability that the triggered-only event appears.
The event calls its older loss helper in `immediate` before these options are chosen; option effects may alter the timing of later reports, which this single-event evaluation does not model.
The sole remaining diagnostic relevant to interpreting the pool is `EVENT_OPTION_FALLBACK_NOT_PROVEN`: every option has a trigger, so no unconditional fallback is established for an undeclared intermediate state.
The earlier connected full-file evaluation exited when it lacked an identifier and complete state bindings; the exact-block inline [qualification](../ger_mengele_10_inline_2026-09-27/review.md) remains a narrower diagnostic, while this current-source run supersedes its conditional shares for the two bound cases.

A separate connected `random_list` inspection/evaluation of the same unchanged event file returned a complete two-candidate pool and `PROBABILITY_ANALYZED` with zero unresolved items at revision `5c0116f092a5eaf00cb5742aee1dbbcde1cc1542c2c1ac2f13fb5d974afffb5d`, scenario hash `7873423cd45b677a1160661e4d3b550f266dbe70549b9de983f60f85f4598913`, and [authoritative JSON artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb39da991fbd94647690b121f294a1d2a45f3adbcf31873d17de80162c49aa12/2779faebc24700a5faf4852df8bcabbccf063627822afb8fdb60d212fe295e40/probability-2e6cbfae7035234a7c82c73e.json).
The source `.12.a` list gives 70 weight to queue `.20` and 30 to queue `.13`; that conditional split applies only if `.12.a` is selected and its list executes. It does not include `.12` event firing, `.12.a` option eligibility/selection, later event availability or cumulative deaths.
