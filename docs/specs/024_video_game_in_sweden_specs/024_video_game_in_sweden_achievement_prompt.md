# Achievement Prompt: Event 24 Video Game in Sweden

Implement the Event 24 achievements defined in the source specification package at:

`docs/specs/024_video_game_in_sweden_specs/`

Read and follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-subagents`, the current achievement registry, and installed vanilla achievement precedents. Use the single root Chaos Redux achievement registry. Do not create another root `unique_id` file.

Final achievement titles and descriptions must be written from the direction below. The working labels are not mandatory final localisation.

## Achievement A: Reality Check

Stable id:

`024_video_game_in_sweden_reality_check`

Working title direction:

- A concise phrase about testing the game against reality.
- Dry and practical.
- No direct reference to players, save files, or game mechanics.

Description direction:

- As Sweden, allow the war game crisis to reach its highest evolution.
- Complete a full Reality Audit.
- Keep the program below Doctrine-level reliance for the proof period.
- Preserve Stockholm.

Eligible country:

- Player-controlled principal Swedish host.
- Use the same host identity contract as Event 24.

Unlock requirements:

1. Event 24 fired normally.
2. Evolution III was reached and recorded.
3. The player selected Reality Audit.
4. The Reality Audit achieved full success.
5. Simulation Reliance remained below the Doctrine threshold for 365 consecutive days after success.
6. Stockholm remained under the eligible Swedish host's control throughout the proof period.
7. The achievement may require Sweden to be at war during part of the audit or to win a war after the audit if implementation needs a stronger difficulty gate. Use the accepted final specification and do not weaken the route into a wait-only unlock.

Disqualifiers:

- Force-trigger, debug, scenario bypass, or other normal achievement-disabling conditions.
- Restriction or Dual-Track selected in place of the Reality Audit.
- Partial or failed audit.
- Reliance returns to Doctrine or Worldview during the 365-day proof period.
- The eligible Swedish actor ceases to exist or loses Stockholm during the proof period.
- Duplicate actor migration or civil-war copies must not preserve false progress.

Tracking requirements:

- Record the eligible Swedish actor.
- Record full audit success date.
- Start one continuous proof timer.
- Reset the proof timer when Reliance crosses the disqualifying threshold or Stockholm is lost.
- Preserve progress through save and reload.
- Prevent a second Event 24 instance from completing the same proof.

Difficulty:

- Hard.

Visibility:

- Visible, with wording that does not reveal hidden incident families or exact internal thresholds beyond the public route goal.

Why it is not trivial:

The player must permit a risky evolution, pay and complete a field-based mission, accept temporary loss of strong benefits, then maintain disciplined use for a full year.

Icon direction:

- Use the asset id `024_video_game_in_sweden_reality_check`.
- A projected strategy map is corrected by a muddy boot print, field compass, terrain profile, or survey notebook.
- Create completed, grey, and not-eligible variants through the asset prompt.

## Achievement B: According to Plan

Stable id:

`024_video_game_in_sweden_according_to_plan`

Working title direction:

- A restrained phrase about a plan surviving contact with reality.
- It may carry mild irony.
- No modern gamer language.

Description direction:

- As Sweden, choose the maximum-reliance route during Evolution III.
- Defeat a materially stronger opponent before mandatory reassessment.
- Keep Stockholm under Swedish control.
- Complete the reassessment after victory.

Eligible country:

- Player-controlled principal Swedish host.

Unlock requirements:

1. Event 24 reached Evolution III normally.
2. The player selected Trust the Model.
3. The maximum-reliance surge began.
4. Sweden was already fighting or entered a meaningful war against a major power or a country that was materially stronger when the surge began.
5. The opponent was not already close to capitulation at surge start.
6. Sweden won, forced a favorable peace, or caused the qualifying opponent's capitulation before the surge's mandatory reassessment deadline.
7. Stockholm remained under Swedish control throughout the surge.
8. Sweden completed the mandatory reassessment after the qualifying victory.

Materially stronger opponent test:

Use a robust comparison available to script. Prefer a combined or clearly documented test based on factories, fielded manpower, division strength, or major-power status. Do not let a tiny puppet, nearly defeated minor, or already capitulating country qualify.

Disqualifiers:

- Debug or force-trigger route.
- Opponent invalid at surge start.
- Stockholm lost at any point.
- Surge restarted, duplicated, or created after the qualifying war was already effectively won.
- War ends through a non-qualifying unrelated peace that does not represent Swedish success.
- The eligible Swedish actor ceases to exist.

Tracking requirements:

- Snapshot the qualifying opponent and strength proof when the surge begins.
- Record surge start and mandatory reassessment deadline.
- Record Stockholm control throughout the proof window.
- Record the qualifying war outcome.
- Require completion of the reassessment after victory before final unlock.
- Preserve all proof through save and reload.
- Clean invalid targets after annexation, faction changes, civil wars, or war merging without granting a false unlock.

Difficulty:

- Very hard.

Visibility:

- Visible. The description may identify the public Trust the Model route, but it must not reveal hidden incident selection or AI logic.

Why it is not trivial:

The route gives a short military window while worsening supply, adaptability, recovery, or political pressure. The player must use that window against a stronger opponent and then survive the mandatory review.

Icon direction:

- Use the asset id `024_video_game_in_sweden_according_to_plan`.
- A brass plotting table shows a Swedish-colored marker reaching an objective despite broken rail, bad weather, or terrain friction.
- Create completed, grey, and not-eligible variants through the asset prompt.

## Implementation requirements

- Inspect existing Chaos Redux and vanilla achievement patterns.
- Add tracking flags or variables with clear lifecycle and cleanup.
- Keep achievement ids stable.
- Add final localisation and icons.
- Update Event 24 documentation and achievement coverage notes.
- Add task-specific validation for actor identity, continuous timers, opponent qualification, save and reload, civil war, annexation, and debug disqualification.
- Do not convert either achievement into an automatic evolution or decision-click unlock.
- Do not add a third easy achievement to inflate the set.
- Route icon creation through the Event 24 asset prompt and `chaosx_icon_artist` with `fork_context=false`.
- Before completion, use `chaosx_event_completion_auditor` to compare the achievement requirements against the final implementation.

## Completion handoff

Report:

- Achievement ids and localisation keys.
- Tracking flags, variables, and target scopes.
- Exact unlock and disqualifier logic.
- Icon files and registry references.
- Save and reload proof.
- Opponent-strength scenarios checked.
- Any blocker or deviation.

No simplification is authorized without explicit user approval.
