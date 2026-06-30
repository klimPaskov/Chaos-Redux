# Event 011 Runtime Flow

## Start flow

1. Event 011 is selected by the random event system for the target country.
2. The system verifies that enough valid members exist for the opening strength.
3. The event creates hidden pact state and saves the target, founder, and core members.
4. The first player-facing popup describes repeated diplomatic friction without naming the pact.
5. The pact schedules its first operation pulse.
6. Baseline operations accumulate suspicion and hidden evidence seeds.
7. Evolutions unlock through event pacing, not instant baseline stage movement.

## Operation pulse

1. Refresh member validity.
2. If any core member is now at war with the target, run reveal from war.
3. Score operation families from stage, values, target state, and member roles.
4. Pick a valid operation and acting member.
5. Apply operation effect, suspicion change, and evidence chance.
6. Schedule next pulse using dynamic duration.

## Reveal from war

1. Detect that a core member is at war with the target.
2. Refresh members and remove invalid countries.
3. Save revealed leader.
4. Form public faction or coalition using valid core members.
5. Add all valid core members to war against the target.
6. Apply reveal event, war preparation outcomes, member hesitation checks, and cleanup.
7. Close obsolete hidden decisions and convert needed tools to wartime forms.

## Evidence reveal

1. Target reaches evidence threshold.
2. Player chooses public exposure, quiet pressure, or confrontation.
3. If exposure succeeds, member list becomes public according to evidence strength.
4. Pact may dissolve, split, form public faction, or start war countdown.
5. Follow-up state records outcome for achievements and docs.
