# Event 009 White Peace Source Package

This package records source design for Event ID `9`, White Peace.
A spec location, date, status label, or old handoff does not establish approval.
Accepted audit decisions are recorded in [agent_decisions_2026-10-05.md](../../plans/009_white_peace_plans/agent_decisions_2026-10-05.md).

## Source-of-truth map

| Surface | Document | Authority and disposition |
| --- | --- | --- |
| Accepted audit changes | [2026-10-05 decisions](../../plans/009_white_peace_plans/agent_decisions_2026-10-05.md) | Parent acceptance within the user-authorized audit, including G6 and G7. |
| Main source design | [Main spec](specs/009_white_peace_spec.md) | Source design with acceptance recorded per claim. |
| Weight model | [Dynamic model](specs/009_white_peace_dynamic_weight_model.md) | Current source observations and historical proposals, with numeric validation unresolved. |
| Presentation | [Text, log, and cluster](specs/009_white_peace_event_text_log_cluster.md) | Accepted result delivery and implemented key map, with parent-owned wording follow-up. |
| Safety criteria | [Safety matrix](matrices/009_white_peace_safety_ai_acceptance_matrix.md) | Parent-owned acceptance criteria with their stated evidence limits. |
| Current behavior | [Overview](../../events/009_white_peace/overview.md) | Parent-owned implementation documentation. |
| Validation | [Validation matrix](../../plans/009_white_peace_plans/009_white_peace_validation_matrix.md) | Parent-owned scenarios and unresolved checks. |
| Catalog follow-up | [Catalog pending](../../plans/009_white_peace_plans/catalog_changes_pending.md) | Accepted and queued because workbook and CSV edits were excluded. |
| Legacy reconciliation | [Curator handoff](../../plans/009_white_peace_plans/subagent_handoffs/009_documentation_curator_2026_10_05.md) | Exact document dispositions and evidence limits. |

## Accepted boundary

The parent accepted isolated one-on-one candidate wars on 2026-10-05 under user G6 because Event 009 cannot prove third-country participants safe.
The base settles one minor-country pair, and Stages I and III can settle several separate isolated wars.
Current evolution settings gate actual branch behavior through `is_current_evolution_enabled` after caller-local Event 009 id, type, stage, and tier are set.
Disabled Stage I multi, Stage II major, and Stage III broad paths have zero branch weight or eligibility, and historical unlock flags cannot restore disabled major settlements.
Existing stage progression and war-pressure requirements remain additional gates, while base isolated minor peace remains eligible when all evolutions are disabled.
The parent explicitly accepted this evolution-setting fix in its 2026-10-05 follow-up task.
The earlier one-overcrowded-war multi-party route is rejected.
Settlement runs immediately in hidden `chaosx.nr9.1` before notification.
A successful chain sends one aggregate acknowledgment report to each human-controlled participant. If all settled participants are AI, it sends one global observer-news event.
The result variant follows actual successful settlement count, and the broad variant requires a broad branch that settles at least three separate wars.
User G7 requires a forced invalid entry to find a valid candidate or explain rejection, represented by plain `chaosx.nr9.6` feedback for a human root.
The Circular achievement uses three distinct isolated wars without a five-pair alternative.
No Winner keeps continuous survival, with narrow capitulation, annexation, and subject-transition hooks invalidating its watch and `.20` checking a carried partner target.

Source uses an on-demand dynamic cap with a `1500` environment ceiling, stage multipliers, and repeatable decay.
This is implementation evidence rather than numerical balance approval.
The assigned probability inspection timed out after 600 seconds, so numerical scenario validation remains blocked.

## Supporting material

Research and prompts remain supporting briefs subordinate to the accepted decisions above.
Their workflow/navigation instructions were reconciled in the October 7 package audit; this does not approve every historical design claim or certify implementation.
Use [chaos-redux-subagents](../../../.claude/skills/chaos-redux-subagents/SKILL.md) for current routing and evidence requirements.
The three legacy handoffs retain their original bodies beneath superseded notices.

The source package excludes broad focus trees, country packages, formables, dedicated scripted GUI windows, and high-spectacle presentation.
The installed observer image is `gfx/event_pictures/009_white_peace/news_event_009_white_peace.dds`, using `GFX_news_event_009_white_peace` in `interface/009_white_peace_event_images.gfx`.
Production evidence is linked by [the news-art handoff](../../plans/009_white_peace_plans/subagent_handoffs/white_peace_news_art_handoff.md).
Parent review, required MCP evidence, and completion claims remain parent-owned.

## Open questions

Each item is proposed (spec audit 2026-10-10) and needs parent or user acceptance before implementation.

1. Random War re-ignition: Event 004 Random War does not read White Peace memory, so it can declare a fresh war between a pair White Peace has just settled.
   Proposal: Event 004 skips a pair while either side carries `recent_white_peace_pair_<TAG>` for the other (owner: Event 004).
   This keeps a settlement meaningful without adding any White Peace value.
2. Return after a settlement: a completed settlement ends the only war behind its front states, yet displaced civilians wait on the migration system's general return path.
   Proposal: the settlement calls the migration owner's existing return helper for front-flight cohorts displaced by that war, so Help Families Return is immediately useful for the two countries (owner: famine and migration system).
   White Peace adds no migration values or tooltip lines of its own.
3. Close the dangling legacy tuning ideas as rejected: the optional stale-war weight bonus, the broad candidate score, the major `-3` and broad `-4` Chaos alternatives, and extra weight after repeated Peace-cluster checks without a firing.
   Each adds a tuning knob without a difference the player can see, and the implemented drivers already scale with war clutter.
4. Event 012 opt-out: the Scramble, liberation and forced-withdrawal chains should set and clear `white_peace_protected_war_actor` through an owner marker, following Event 039's working pattern.
   This stays an unresolved integration requirement for the Event 012 owner.

## Changelog

- 2026-10-10 spec audit, pass 1:
  - Aligned the main spec with source: Chaos `-1` per minor pair, `-2` per major war, chain cap `-3`, 181-day country memory, the Stage II multi branch, and an isolated major war.
  - Removed the stale "narrow enemy side" major wording, optional debug metadata, the optional `-4`, and the conditional-news wording, and replaced the duplicated weight formula with a pointer to the weight model.
  - Condensed the weight model's retained historical proposal, whose tables duplicated source or the main spec, into its still-valid design intent.
  - Repointed skill links to `.claude/skills/` and prompt instructions to `CLAUDE.md`.
  - Named the two protection flags and Event 039 as the working opt-out precedent, and marked installed assets as implemented.
- 2026-10-10 spec audit, pass 2:
  - Added the open questions above and two validation cases (recent pair memory, enemy-occupied capital).
