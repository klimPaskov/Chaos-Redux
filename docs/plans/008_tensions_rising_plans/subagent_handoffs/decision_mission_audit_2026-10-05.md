# Event 008 Decision and Mission Audit

Audit date: 2026-10-05  
Disposition: Read-only scoped audit. No decision or mission definitions owned by or directly dispatched from Event 008 were found. The Event 008 AI posture ideas affect shared diplomatic AI behavior and are being covered by the parent’s separate probability baseline audit.

## Scope and evidence

Searched recursively under `common/decisions` for the case-insensitive terms `chaosx.nr8.` and `tensions_rising`; there were no matches. This covers Event 008 decision IDs, category and mission identifiers, and source-level Event 008 flag or helper references in the decision tree.

Searched the Event 008-owned event, effect, trigger, and idea files for `decision`, `mission`, and `ai_will_do`; there were no source matches. The event chain defines popup events in [008_tensions_rising.txt](../../../../events/008_tensions_rising.txt:35), including root event `chaosx.nr8.1`, follow-up reports `.2` through `.10` and `.12`, border-war outcomes `.13` through `.15`, and hidden achievement events `.20` and `.21`. Border-war outcome dispatch points at `chaosx.nr8.13`, `.14`, and `.15` in [008_tensions_rising_effects.txt](../../../../common/scripted_effects/008_tensions_rising_effects.txt:1228). These are event links, not decisions or missions.

The current implementation-facing [Event 008 overview](../../../events/008_tensions_rising/overview.md) describes temporary AI posture ideas and says the system creates no focus trees, formables, or new countries. The historical source spec and AI matrix mention increasing AI willingness for existing war-adjacent or hostile decisions, including direct weights as one possible implementation. Those references describe shared existing actions and do not name or define an Event 008 decision. The overview identifies itself as the current implementation-facing record, so this audit does not expand into a repo-wide shared-decision review.

## Issues sorted by severity

1. Evidence limitation: the exposed `hoi4_decision_inspect` route did not produce a usable result. A scoped inspect call with `id = tensions_rising` first returned `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.decision_inspect: Decision inspection requires declared scenarios at scenarios`, despite the live schema marking `scenarios` optional. Two retries supplied one named CXT scenario and remained pending for more than three minutes each; both were terminated. No MCP decision artifact or scenario coverage was returned. A global decision inventory was not run because it would exceed this Event 008 scope.
2. Gameplay issues: none identified in the Event 008-owned decision and mission surface because the scoped source paths contain no such definitions.

## Category lifecycle and cognitive load

Event 008 owns no decision category, so there is no category unlock, visibility, phase, cooldown, or cleanup lifecycle to audit. It exposes zero decision actions and zero active missions in the scoped source. Decision values, requirements, costs, and tooltips are therefore not applicable, and there is no decision category text-density or unclear player-facing value issue.

## Mission quality

No Event 008 mission definitions were found. Owner, category, region, requirement, duration, success, failure, and duplicate-mission cleanup are not applicable.

## Costs, requirements, and localisation

There are zero spendable decision or mission costs in scope, so the cost-count audit is zero distinct cost types and texticon coverage is not applicable. No Event 008 decision requirement, trigger tooltip, decision description, mission localization, or cost localization keys were found to audit. Event popup text and its mechanical tooltips remain outside this decision/mission audit.

## AI validity, route locks, cleanup, and exploit risk

No Event 008 decision `ai_will_do` score, decision target, route lock, or mission AI score exists in the scanned decision sources. The event does apply timed national spirits to selected AI countries. Four ideas are defined in [008_tensions_rising_ideas.txt](../../../../common/ideas/008_tensions_rising_ideas.txt:11), and [apply_tensions_rising_ai_posture_to_country](../../../../common/scripted_effects/008_tensions_rising_effects.txt:731) selects the stage-specific timed idea at lines 750-770. Their `ai_join_ally_desire_factor` and `enemy_justify_war_goal_time` modifiers can affect shared diplomatic and war-preparation behavior indirectly, but they are not decision-owned `ai_will_do` blocks. The parent’s `008_probability_baseline` audit owns probability-surface analysis of these exact idea modifiers; its MCP artifacts were still pending when this handoff was written.

Event-level border-war targeting and event cleanup do not create a decision or mission surface. No decision cleanup hook, hidden-decision reveal, cooldown abuse, free-action loop, or cost exploit was found because there are no scoped decision or mission actions.

## Recommended fixes

No small decision or mission patch is justified. Keep the Event 008 decision and mission scope empty unless accepted design later names a specific decision or objective. The shared diplomatic actions affected indirectly by the timed ideas require their own source-specific review before anyone attributes a defect to Event 008.

## Validation and remaining uncertainty

Completed narrow source searches over `common/decisions` and the Event 008-owned event, effect, trigger, and idea files; reviewed the Event 008 source spec, AI matrix, and current overview. No gameplay files were changed.

Skipped decision scenario analysis because the bounded `hoi4_decision_inspect` attempts did not return a result and no in-scope decision exists. No GUI inspect/render was required because Event 008 owns no decision GUI. Offline syntax references and vanilla decision precedents were not required because this audit made no engine-facing changes.

Remaining uncertainty is limited to the unavailable decision-inspection artifact and the parent probability auditor’s pending evidence for the timed AI posture modifiers. This handoff does not claim a repo-wide audit of the unrelated shared decisions those modifiers may influence.

## Changed files and handoff

Changed file: `docs/plans/008_tensions_rising_plans/subagent_handoffs/decision_mission_audit_2026-10-05.md`.

Changed gameplay, mission, scripted GUI, or localisation IDs: none.

Before and after behavior: no gameplay behavior changed. This handoff documents that Event 008 has no directly owned decision or mission surface and records the indirect AI posture hooks for the parent’s separate probability review.

Meaningful validation: scoped source evidence and MCP decision-inspection attempts are recorded above. No syntax or runtime validation was applicable to a read-only audit.


