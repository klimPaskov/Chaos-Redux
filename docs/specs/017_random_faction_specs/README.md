# Event 17 Random faction planning package

> Documentation reconciliation, 2026-07-29: the accepted implementation is recorded in [`docs/events/017_random_faction/overview.md`](../../events/017_random_faction/overview.md) and the [2026-07-11 completion audit](../../plans/017_random_faction_plans/subagent_handoffs/017_random_faction_event_completion_audit_handoff.md).
> Its `PASS` is dated checkpoint evidence, not fresh engine or asset validation. The catalog's `Needs Testing` status is a live user-validation boundary, not evidence that the static implementation is absent. The planning-only environment note below is retained as historical intake context.

This package contains the full planning handoff for Chaos Redux Event 17 `Random faction`.

## Contents

- `specs/`: four-part source specification
- `matrices/`: AI matrix, decision map, scripted architecture, and catalog handoff
- `prompts/`: historical build contracts for the original implementation (asset, achievement, decision, coding, goal, and subagent tasks).
  Choose continuation from the dated implementation overview and audit cited above before scheduling work.
  These contracts do not authorize repeating completed tranches.
- `research/`: historical inspiration notes and source directions
- `source_review/`: manifest of uploaded project files read before writing the package

## Historical planning environment

The original planning environment lacked the custom subagent runtime.
That limitation does not establish current service health or outstanding implementation work.
Use [the routing owner skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md) for any new bounded pass, with explicit, self-contained inputs.

Historical planning-intake note: no gameplay files were edited while this package was authored. The current gameplay and audit state is documented by the implementation overview and completion handoff cited above.

## Open questions

Each item is proposed (spec audit 2026-10-10); the implemented system is the parent-accepted baseline recorded in the overview and the 2026-07-11 completion audit, so none of these changes is authorized until accepted.

1. One neutrality value instead of two meters.
   Pressure and resilience move in opposite directions in almost every decision (Council, Publish, Observers, Staff Mission, Border Posts), and the neutral status line shows both.
   Proposal: show one Neutrality value per pressured neutral that falls under pressure and rises with resistance, collapsing into a forced choice where pressure now reaches `random_faction_pressure_value.collapse_threshold` (80).
2. Remove fairy dust from aligned members.
   Source review found `random_faction_pressure_score` read only by Demand Commitment's collapse check and one decision AI factor, so an aligned member's pressure drives nothing.
   Proposal: drop the pressure figure from the aligned status line and the pressure changes from Stabilize the New Alignment, Quiet the Opposition and its backlash; keep the shock, stability and relation effects that matter.
3. Fewer overlapping decisions (11 decisions and 2 missions today).
   Publish a Neutrality Declaration is a smaller Neutrality Council without the border objective; merge it into the Council.
   The faction-leader Radio Networks decision duplicates the radio response of the leader reaction report `chaosx.nr17.40`, and three routes grant the same liaison effect to a new member (Request Liaison, Offer Staff Mission, the `.40` staff response).
   Proposal: keep one radio route (the `.40` response) and one leader-side liaison route, and limit Offer Staff Mission to pressured neutrals.
4. Condemnation should cost a bloc its recruits.
   A minor choosing under pressure should shy away from a faction leader under international censure.
   Proposal: in the AI option weights and the pressured-neighbor response, halve a leader that passes `condemnation_is_formally_censured` and quarter one that passes `condemnation_is_pariah_state` (both in `common/scripted_triggers/condemnation_sanctions_triggers.txt`), and show one option tooltip line naming the censure for a human chooser.
   This is a diplomacy link, so it does not conflict with Part 3's rule against direct chemical or biological hooks.

## Changelog

- 2026-10-10 spec audit, pass 1:
  - Repointed skill links to `.claude/skills/` and removed the Codex-only `fork_turns` instruction from the README.
  - Marked the coding and goal prompts and the prompts folder as historical build contracts so they are not rerun against the implemented event.
  - Confirmed the 8 October refinements are present (Part 1 civil agreements versus formal factions, no Evolution IV/V aside in Part 3).
- 2026-10-10 spec audit, pass 2:
  - Added the open questions above: one neutrality value, removal of inert aligned-member pressure, decision consolidation, and a condemnation link for faction choice.
