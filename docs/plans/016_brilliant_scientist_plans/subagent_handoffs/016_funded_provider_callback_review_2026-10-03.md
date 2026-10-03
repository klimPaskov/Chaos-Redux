# Event 016 funded-provider callback review

Disposition: bounded source review complete for the funded-stage cold-result contract and the seven no-DLC Prototype removal callbacks. No gameplay source was changed by this reviewer. The current source has no concrete duplicate-grant or stale-result defect in the reviewed paths. Native paid-project cancellation/reselection generation remains unresolved and is not waived as engine acceptance.

Scope: review the current absolute shared-root working tree against source commit `9ec6bc483d48ba6fa81c2ef32683594eb4613523`, including the parent-owned stage-core change, its matching helper contract, and the seven named Prototype decisions. The current repository HEAD is `3af464814b8220d104ff20e31603e85138a00842`. The prior `016_funded_provider_cold_lifetime_2026-10-03.md` remains historical and was not overwritten.

## Severity-sorted findings

1. **High, still unresolved outside this callback patch:** native project cancellation followed by reselection, including callback-generation isolation, still lacks proof that an old native callback cannot settle against a later selection. This patch resets funded-provider helper outputs and decision-consumer outputs. It does not add native start/cancel tracking, change native project timers, or prove native callback ownership. Keep this as a full-goal blocker.
2. **No remaining concrete source defect found in the bounded callback path:** the seven callers initialize both returned values before finish, the finish transaction initializes its own nested outputs, exact family/stage receipt matching prevents another active stage from settling, and no-DLC grants require accepted output as well as a finished receipt. Parent-reported source-driver results are recorded below and are not live-game acceptance.
3. **Engine evidence remains limited:** no new MCP queries were made. The prior exact lookup, event, and decision route timeouts remain historical route limits and do not establish engine behavior or acceptance.

## Current source delta from `9ec6bc`

The parent-owned working-tree delta adds temporary-result initializers and matching-receipt schema extension to `common\scripted_effects\016_mengele_project_stage_effects.txt`. The stage-effects patch is owned by architect handle `01a1029c-eda8-7ec2-911f-8adb4042ae0c`. It does not change script constants, project-stage costs, paid durations, AI expressions, visible strings, decision tooltips, models, or native-project source definitions. The seven decision files each add exactly two lines immediately before `brilliant_scientist_mengele_finish_project_stage = yes`: zero `mengele_event016_stage_finished` and zero `mengele_event016_project_output_applied`. No other decision fields changed in these seven path-limited diffs. No persistent country flag, technology, decision, project, or constant ID was added. The matching `016_mengele_project_stage_effects.md` has 43 added lines versus the baseline, documenting the consuming-frame storage contract and seven callback result ownership.

The shared begin frame owns `mengele_event016_project_index` and all quote outputs before `load_project_stage_quote`: loaded marker, duration, duration-loaded marker, quote-source gap, and civilian-factory, political-power, support-equipment, and fuel amounts. Debit requires a loaded quote and a valid request, provider, predecessor, affordability, and empty receipt. The quote and payment values themselves are unchanged.

Cancel and finish initialize their consumed index before nested mapping. On an exact matching receipt, they extend partial receipt arrays before reading stored rows. Both snapshot the three direct costs and clear only the matching family's active row. Finish also initializes its output, gap, availability, and incident-result fields before nested output and incident helpers. Package dispatch resets its own conventional/custom grant results and the stage-package result before use. Native adoption and cleanup likewise initialize the nested sync/component result and loop index consumed after helper return.

## Seven Prototype callback review

Each listed `remove_effect` sets its literal family and Prototype stage, initializes both result fields to zero, and then calls the shared finish helper. Any no-DLC operational grant is gated on all of: no Gotterdammerung, `stage_finished = one`, `project_output_applied = one`, and that family's durable Prototype-completed flag.

| Family | Decision ID | Existing no-DLC output after accepted Prototype |
| --- | --- | --- |
| Cloning | `mengele_event016_cloning_prototype` | Preserves the existing clone-production completion path behind its completion flag guard, then grants the clone operational package. |
| Teleportation | `mengele_event016_teleportation_prototype` | Grants the portal operational entitlement. |
| Robotics | `mengele_event016_robotics_prototype` | Grants the robot operational entitlement. |
| Paleogenetics | `mengele_event016_paleogenetics_prototype` | Grants the paleogenetic operational entitlement. |
| Xenobiological Synthesis | `mengele_event016_xenobiological_synthesis_prototype` | Grants the xenobiological operational entitlement. |
| Alien Arms | `mengele_event016_alien_arms_prototype` | Grants the alien-infantry operational entitlement. |
| Temporal | `mengele_event016_temporal_prototype` | Grants the temporal operational entitlement. |

The result gates reject cold entry with no matching receipt, a receipt for another family or stage, and a repeated removal callback after the receipt was cleared. A matching receipt can finish while output is rejected, for example after provider loss or failed package application. In that case `stage_finished` may report the matching settlement, but `project_output_applied` remains zero, so none of the seven custom grants run. A successful output sets the private completion flag and the output result, allowing exactly the existing family grant path. Cloning additionally checks its established Germany completion flag before invoking its clone-production completion effect, preserving the existing variant handling.

The finish sequence snapshots political power, support equipment, and fuel, clears the paid row, then attempts authorized output. If output is not accepted it refunds those three stored direct costs once. The civilian-factory commitment is cleared from the receipt and is not refunded as cash. Since the seven caller changes only initialize temporary results, their existing native decision timers and payment fields remain untouched.

## Decision lifecycle, load, missions, costs, AI, and localization

These are the existing timed Prototype decisions in the Biological and Advanced program categories. Their categories, visibility, requirements, timer lengths, click behavior, and follow-on branches are unchanged. No mission or timed-objective definition changed. No new player-facing values or actions were added, and no tooltip or localization keys changed.

The existing funded stage uses four cost types: political power, support equipment, fuel, and civilian-factory commitment. The finish/cancel helpers refund only the three stored direct costs, while the civilian-factory commitment remains the decision's timed commitment. Cost counts, displayed texticons, affordability checks, AI scores, and route gates are unchanged by this delta. No AI weight or probability surface changed, so no new AI/MCP expansion was performed at the parent's direction.

## Validation evidence and limits

- Parent's final focused source driver reports 1,867 passing cases, up from the 1,863 checkpoint by four incident-result forwarding cases. Coverage spans all 15 families and four stages, direct political-power/support-equipment/fuel account changes and stored receipt rows, comparisons against `9ec6bc`, 225 affordability cases, 480 partial-schema cases, 56 actual seven-callback combinations, and the four result-forwarding additions. The associated diff changes no constants.
- Parent also reports the full 6,752-case native-source regression suite still passing. The callback driver includes cold result initialization, no-DLC and DLC states, accepted and rejected receipts, output flags, and repeated callback checks. These are source-contract model results, not live engine or native-project timer tests.
- The retained driver and its declared stubs are in `subagent_handoffs/016_funded_provider_cold_lifetime_2026-10-03.md`. That report describes a conservative temporary-scalar model. Provider lifecycle and technology payloads use named stubs; the output does not establish native project cancellation, callback generation, or live-game acceptance.
- The shared helper documentation records the same output ownership table and seven caller rule in `common\scripted_effects\016_mengele_project_stage_effects.md`. The verified `git -C . diff` from the explicit shared root shows 43 added lines relative to `9ec6bc`; its current absolute-root SHA-256 is `4f123818c21e07a83713248a5fe0dcbc9ca3de122d06808c8a6bdee20e7271ef`.
- No new GUI, AI, decision-inspect, event-inspect, or reference queries were made. The prior route timeouts remain documented in the historical source handoff and are not treated as engine acceptance.
- No game was launched, no gameplay source was edited by this reviewer, and no model, asset, index, or commit operation was made.

No simplification was introduced. No source patch is recommended for the bounded callback tranche. Preserve the separate native cancellation/reselection generation blocker until it is independently resolved.

## Current source hashes from the shared root

Hashes were computed from `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux` after the architect's current stage-core patch.

| File relative to shared root | SHA-256 |
| --- | --- |
| `common\scripted_effects\016_mengele_project_stage_effects.txt` | `4d09b832e73c4a5222617cf686103889881c4547da23c71110f5b1947f75afa0` |
| `common\scripted_effects\016_mengele_project_stage_effects.md` | `4f123818c21e07a83713248a5fe0dcbc9ca3de122d06808c8a6bdee20e7271ef` |
| `common\scripted_triggers\016_mengele_project_stage_triggers.txt` | `5ab7041ce22f13fbfecf641f4ca9e6fc7d693ddf366da14e631a3dfa498e537c` |
| `common\decisions\016_mengele_cloning_stage_decisions.txt` | `460b87d5946db3d5cfe90960e32a7c5d9b19b125d5aa4f71f56b3a3e7f6c5f8e` |
| `common\decisions\016_mengele_teleportation_stage_decisions.txt` | `55c65ca1d2e143c414c0131c149b0f561d97090be1ee48df146ae3fd4ceb0f42` |
| `common\decisions\016_mengele_robotics_stage_decisions.txt` | `a562f71ba27b37ed6f5f9543a0dfc8bdf606863ca219ede5b6ac0dab5b4de844` |
| `common\decisions\016_mengele_paleogenetics_stage_decisions.txt` | `4bf57705a70d201a8e44a2fec8de571d6e556bbe22830a1a2773df7617dcb941` |
| `common\decisions\016_mengele_xenobiological_synthesis_stage_decisions.txt` | `582c7e84db57369302bd27ce376491b1f913e94dfb98338e17cee0ded55ee5eb` |
| `common\decisions\016_mengele_alien_arms_stage_decisions.txt` | `ce55413861d3ea8298974b993f18ced5c9a211388e00c2dab523f583a7334401` |
| `common\decisions\016_mengele_temporal_stage_decisions.txt` | `dd0170f577fd1f01068d14714a5afa32b768b3867d2c8a92a742345782046bb3` |
