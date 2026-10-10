# Event 009 Dynamic Weight Model

## Current model reconciliation, 2026-10-05

Disposition: implemented as source-level observations, with numerical design acceptance unresolved and mandatory probability validation blocked.
The parent accepted isolated one-on-one wars under user G6 on 2026-10-05, as recorded in `docs/plans/009_white_peace_plans/agent_decisions_2026-10-05.md`.
The original design model below remains historical proposal evidence, and its tuning suggestions and worked examples are not approved or validated by their location in this spec.

## Current source observations

`calculate_white_peace_dynamic_cap` uses base pressure, capped active-war, safe-minor-pair, and minor-only pressure, plus the applicable clutter bonus.
Source clamps the environment cap to `120..1500`, applies repeatable decay and stage multipliers plus the recent-broad penalty, rounds the effective cap, and clamps it again to `120..1500`.
This differs from the historical formula's unqualified `floor` result, which omitted the final effective floor.
No eligible candidate leaves the dynamic cap at zero.
The active-war variable is a country-at-war proxy, not a verified unique-war inventory.
Candidate pair counts divide symmetric eligible pair observations by two, and every eligible pair is a separate isolated war.
Third-party participation or another active enemy disqualifies a candidate at every stage.
Candidate scanning remains on demand without a periodic all-country poll.
The shared picker and recovery lifecycle remain parent-owned and were not independently re-audited in this curation pass.

The current constants file contains base `125`, floor `120`, ceiling `1500`, active-war pressure `90` capped at `540`, safe-minor pressure `85` capped at `595`, minor-only pressure `60` capped at `240`, clutter bonuses `125/175/225`, and recent-broad penalty `0.80`.
Stage multipliers remain `1.00/0.78/0.55/0.38`, and branch weights remain base `100`, Stage I `70/30`, Stage II `60/25/15`, and Stage III `50/25/15/10`.
These are implementation observations, not evidence of balance acceptance or normalized scenario outcomes.
The parent explicitly accepted current evolution settings as actual branch gates in its 2026-10-05 follow-up task.
`calculate_white_peace_dynamic_cap` resets runtime context and clears all three computed flags before calling `set_white_peace_evolution_gates`.
That helper sets caller-local Event 009 id and type, then the relevant stage and tier before each `is_current_evolution_enabled` check.
The resulting flags are `white_peace_multi_branch_enabled`, `white_peace_major_branch_enabled`, and `white_peace_broad_branch_enabled`.
Existing stage progression and war-pressure thresholds remain additional requirements, and an old unlock flag cannot promote a disabled current evolution.
The displayed constants are ungated tuning values rather than unconditional live branch shares.
`select_white_peace_branch` sets all later-stage multi weights to zero when Stage I is disabled, major weights to zero when Stage II is disabled, and broad weight to zero when Stage III is disabled.
`can_country_be_white_peace_major_target` additionally requires the current major-enabled gate, without the former historical-unlock fallback.
Base isolated minor peace remains eligible when all evolutions are disabled.
Invalid branches receive zero weight, so the eligible pool is normalized rather than explicitly transferring weight to a named substitute.
`load_white_peace_branch_weight_variables` loads temporary variables for random-list labels, replacing the historical helper handoff's described file-local branch mirrors.
Source requires one candidate for single and major, two for multi, and three for broad.
Observed settlement caps are base one, Stage I two with a high-pressure three-pair allowance, Stage II three, and Stage III five.
The Stage III five-settlement cap is distinct from the rejected five-pair achievement alternative.

Source score constants are base `10`, minor bonus `40`, no-major bonus `30`, long-war bonus `20`, safe-capital bonus `20`, independence bonus `15`, outside-faction bonus `15`, major penalty `-35`, and score floor `1`.
Safety vetoes apply before scoped-array weighted selection, and recent pair memory is an exclusion rather than a soft score penalty.
Source memory durations are country `181` (one day past the No Winner check), pair `360`, major `540`, and broad `720` days.
Source Chaos changes are minor `-1`, major `-2`, and multi/broad capped at `-3`.
Source evidence is `common/script_constants/009_white_peace_constants.txt`, `common/scripted_effects/009_white_peace_effects.txt`, and `common/scripted_triggers/009_white_peace_triggers.txt`.

## Legacy proposal dispositions

| Claim in the historical model | Disposition | Acceptance or implementation basis |
| --- | --- | --- |
| Multi-party route or larger segment of one overcrowded war | rejected | Parent acceptance under user G6, because third-country safety cannot be proven. |
| Formula using `floor` without a final effective floor | superseded | Current source rounds and clamps after multipliers. |
| Approximate worked cap examples | unresolved | No validation against proxy counts, final floor, rounding, or MCP scenarios. |
| Optional environment `stale_war_bonus` | unresolved | Absent from current cap constants and effect, with no supplied acceptance. |
| Named branch-weight transfer | superseded | Current source zeros unavailable branch entries. |
| Optional `white_peace_broad_candidate_score` | unresolved | Absent from current runtime reset/count helpers, with no supplied acceptance. |
| Optional major Chaos `-3` or broad `-4` | unresolved | Source uses major `-2` and broad cap `-3`, with no supplied acceptance for alternatives. |
| Five-pair Circular achievement alternative | rejected | Parent accepted only three distinct isolated minor wars. |
| Evolution toggles affecting logging alone, with gameplay enabled by historic unlocks | superseded | Parent explicitly accepted actual current-setting branch gates on 2026-10-05, implemented in gate computation, stage selection, branch weights, and major eligibility. |
| Exact numerical balance and scenario claims | blocked | Assigned probability inspection timed out after 600 seconds. |

No unresolved proposal in the historical model is authorized by this reconciliation.
Stages I and III retain multiple separate isolated-war settlements, and result dispatch follows the actual settled count after immediate settlement.
The Circular achievement requires a broad branch settling three distinct isolated minor wars.

## Mandatory probability evidence

The assigned auditor is `/root/event009/wp009_probability_audit`.
Its named scenario fixture is `docs/plans/009_white_peace_plans/subagent_handoffs/white_peace_probability_scenarios_2026-10-05.json`.
The parent reported that the auditor's first `hoi4.probability_inspect` request timed out after 600 seconds.
No scenario-specific result handoff was available during reconciliation.
Preserve the fixture, immutable baseline source identities, and eventual scenario-specific audit-patch-compare handoff without substituting source matching for probability evidence.
The curator did not tune weights or launch a duplicate auditor.

## Design intent retained from the original model

The original proposal's tuning tables, branch tables, safety scores, memory table, Chaos table and validation list are superseded by the source observations above and by the main spec; the 2026-10-10 spec audit removed them from this file (they remain in git history).
The following design intent stays authoritative:

- One safe minor war should leave the cap well below the default `1000` (the original target was roughly `250-400`); several safe wars can approach `1000`; only severe clutter should approach `1500` before decay and stage multipliers.
- Higher stages are stronger per firing and therefore less likely to be selected.
- Candidate scanning runs on demand (event picker, event list detail, Peace cluster detail, Settings test firing); no daily or weekly loop exists for this event.
- The effective cap clips the live weight and never erases stored repeatable recovery; when war clutter falls the live weight falls immediately, and when it rises the stored weight still recovers normally.
- Unavailable states use the compact skip reasons in `white_peace_skip_reason` (no active war, no safe pair, major stage locked, protected conflicts, recent memory) and never show raw trigger blocks.

The original worked examples were approximations and remain unresolved until a probability audit produces scenario numbers.
