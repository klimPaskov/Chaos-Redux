# Event 016 cross-domain review transition gate handoff

## Scope

The one-time cross-domain review keeps a two-civilian-factory burden active for 120 days. Transfer, Kruger State formation, and new sovereignty containment transitions are now blocked while the review is pending or in progress, so an ownership change cannot replace the timed decision with a one-day report.

## Changed files

- `common/scripted_triggers/016_brilliant_scientist_triggers.txt`
- `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt`
- `localisation/english/016_brilliant_scientist_foreign_l_english.yml`
- `localisation/english/016_brilliant_scientist_directorate_l_english.yml`
- `docs/events/016_brilliant_scientist/overview.md`
- `docs/events/016_brilliant_scientist/systems/projects.md`

## Runtime contract

`brilliant_scientist_sovereignty_transition_is_allowed` is the shared country trigger for transfer, fixed-tag formation, host transformation, and containment-board opening. It rejects only `brilliant_scientist_cross_domain_review_pending` and `brilliant_scientist_cross_domain_review_in_progress`; completed reviews remain transferable and terminal/world-end guards are unchanged. The timed decision retains its original completion, cancellation, and one-day resolution event.

## Validation and remaining risk

Focused static checks should cover the trigger/effect references, the timed decision, and Event 016 localisation. No live HOI4 session was launched. The remaining risk is user-owned runtime confirmation that the decision UI and transfer/containment decision visibility update immediately when the review starts.
