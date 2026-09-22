# Build the native Event 078 information category

Read the complete source specification in `docs/specs/078_border_conflict_specs/`, especially player presentation, frontier behavior, and achievements.
Follow the current decisions and missions, events, assets, debugging, localization, and subagent guidance.
Inspect the actual native category and state-target consumers before choosing the final interface implementation.
This event needs readable information about actual native border battles and hold objectives.
It has no strategic purchase decisions, paid military resolution, or event-specific currency.

Show one useful active-dispute summary and an inspectable entry for every actual stake.
Each entry identifies the opponent, target state, attacking side, wave, and relevant chain stage.
A supported state-targeted interaction should help the player locate the state without changing the battle.
Group long lists where native behavior permits, but do not hide all disputes beyond an arbitrary count.
Keep several waves and same-pair different-state conflicts distinguishable.

Show pending containment and achievement holds with the correct subject and remaining valid duration.
A failed hold cannot be reset for a fee.
Do not keep a wave open for evolution just because a hold remains pending.
The category disappears when it has no live information.
Historical information remains with the shared history system.

Write tooltips from the same dynamic values that gameplay uses and use appropriate whole-number formatting.
Explain attacking capture, defensive retention, and the single declared target consistently.
Keep shared Event Details narrative-only.
No finished localization in the planning package should be mistaken for runtime text, because it supplies direction briefs only.

Use the category icon from the event asset brief after its consumer dimensions are verified.
A dedicated scripted GUI and a large decorative category picture are not approved parts of this design.
If a native consumer limitation changes the required player experience, return the exact finding to the parent instead of adding a new UI system without review.

Run the decision-mission and localization audits and inspect actual native screens at supported resolutions and UI scales.
Because there are no purchasable or outcome-selecting actions, do not invent AI willingness scores merely to fill a decision field.
Return file changes, conditions, state-target behavior, long-list and long-name evidence, hold timing checks, and unresolved presentation limitations.
