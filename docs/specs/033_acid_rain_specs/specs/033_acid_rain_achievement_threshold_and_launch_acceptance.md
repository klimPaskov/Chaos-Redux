# Event 033 accepted achievement threshold and launch origin

Disposition: accepted and implemented in source, with engine acceptance evidence still outstanding.
Acceptance basis: on 2026-10-03 the parent explicitly accepted the recommended Three Evacuations threshold within the latest user/orchestrator authorization to choose recommended options and fully implement them without simplification.
The same parent instruction supplied the two launcher markers and authorized their root-event consumption.
This is an explicit design acceptance and does not infer approval from earlier specification wording or implementation evidence.

## Three Evacuations

Each of the three distinct forecast states must complete a valid paid evacuation strictly before its first severe pulse.
At severe-episode closure, that state's cumulative actual helper-applied severe deaths must be strictly below 0.05 percent of its own population frozen when the forecast was issued.
The ceiling is `frozen_forecast_population_people / 10000 * 5`.
Divide before multiplying and preserve the fractional result without floor, ceiling, or integer rounding.
Equality fails the strict casualty condition.
Evaluate each state independently, then count distinct successful state IDs.
Do not pool the three populations or their deaths.
The pooled severe-survival achievement continues to apply the same 5/10000 ratio to its combined forecast population.

The shared tuning fields are `acid_rain_achievement.severe_survival_death_numerator = 5` and `acid_rain_achievement.severe_survival_death_denominator = 10000` in `common/script_constants/033_acid_rain_constants.txt`.
The completion wrapper derives the evacuation input ceiling from the frozen forecast baseline, and the existing completion ledger retains that unrounded ceiling for final episode settlement.
No current population, requested loss, prevented-death estimate, country manpower value, or substitute threshold can replace the frozen baseline or actual applied death evidence.
Malformed historical records remain subject to the existing integrity guards.
New valid forecast/completion records receive a calculated ceiling rather than a zero placeholder.

## Durable launch origin

The parent owns generic dispatcher arming in `common/scripted_effects/chaosx_settings_effects.txt`.
It sets `acid_rain_launch_authorized` on the actual root recipient for a normal accepted independent or cluster dispatch.
It sets `acid_rain_launch_forced` for a manual accepted dispatch.

Root `chaosx.nr33.1` determines origin only when starting a runtime while no Acid Rain runtime is active.
It sets the durable global flag `acid_rain_forced_generation` when the root recipient has the forced marker, lacks the authorized marker, or is CXT.
Forced wins if both markers exist.
A normal authorized recipient clears the global flag for the generation it starts.
An unarmed direct console root is forced.

The root consumes both country markers on every entry before invoking the runtime start helper.
An active duplicate consumes its markers without changing the existing generation's origin.
Formation country initialization reads the durable global flag and force-disqualifies every participant of a forced generation.
Country achievement initialization also reads the flag so later participants inherit the same origin without a world scan.
The existing CXT-specific debug marker remains active.
Permanent campaign disqualifiers continue to follow the existing achievement integrity contract.

## Implementation and evidence boundaries

This clarification changes achievement eligibility and launch provenance only.
It does not change project or decision costs, AI weights, random selection, weather timing, episode duration, mortality rates, population floors, or migration mechanics.
Migration source commit `f26768187` remains preserved.
The integration handoff contains source checks, numeric boundary cases, launcher truth-table checks, proposed validator assertions, and the remaining MCP/live evidence limits.
