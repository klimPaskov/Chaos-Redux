# Natural Disasters Reusable API Examples

This file is an implementation handoff, not final code. It describes caller behavior that the scripted-system architect should support.

## Random Event 013 call

Caller: random-event system selects Event 013.

Expected behavior:

- Record one Event 013 fire in Event Log.
- Start a sequence with intensity from evolution and chaos.
- Select family pool from current evolution.
- Select targets through family logic.
- Schedule delayed pulses.
- Open reports and recovery decisions according to news policy.

## Cluster member call

Caller: Natural Disasters cluster schedules a baseline member.

Expected behavior:

- Member produces one Event 013 fire if it actually starts a sequence.
- Cluster member passes a member profile such as baseline local, baseline regional, Evolution I, Evolution II, or abnormal-gated.
- Internal disasters do not create Event Log entries.
- Delay between cluster members prevents same-day disaster spam.

## Disaster Barrage scenario call

Caller: SCN-007 confirmation button.

Inputs:

- scenario type id
- intensity stop
- selected country context, if applicable
- force scenario bypass flag

Expected behavior:

- Bypass normal chaos and evolution prerequisites only inside scenario launch.
- Use same sequence controller.
- Use scenario type to weight family pool.
- Use intensity to scale sequence size, delay compression, and abnormal access.
- Clear scenario bypass flags after setup.

## Nature or divine power targeted disaster

Caller: another Chaos Redux event wants to strike an enemy.

Inputs:

- caller event id
- caller actor country
- target country or state
- family id, such as flood, drought, earthquake, wildfire, sandstorm, or storm
- intensity override
- news policy, often targeted report or quiet if the caller owns its own news

Expected behavior:

- Do not record a separate Event 013 random-event fire unless the caller explicitly wants Event 013 to count as fired.
- Apply the family using the same damage and deaths helper.
- Open recovery for target if allowed.
- Respect family target validity. If the caller asks for tsunami in an inland state, return a clean invalid result or convert only if the caller permits fallback.
- Save caller source so later reports or tooltips can avoid confusing attribution.

## Direct state test call

Caller: debug or scenario testing.

Inputs:

- specific state id
- family id
- intensity
- follow-up yes or no

Expected behavior:

- Apply exactly one family pulse.
- Optionally suppress news.
- Optionally suppress recovery category for testing.
- Deaths and building damage should still use normal family profile unless explicitly disabled.

## Storm corridor movement step

Caller: active storm corridor scheduled event.

Inputs:

- active corridor id
- current state group
- predicted next state group
- intensity
- response score in predicted states

Expected behavior:

- Apply storm corridor damage to current path.
- Apply reduced warning or edge effects to neighbors.
- Read response score to reduce deaths and damage in prepared states.
- Select next state group and update GUI arrays.
- Schedule next step.
- End corridor when duration, path limit, ocean exit, or dissipation condition is reached.

## Return values and cleanup

Each public helper should leave a usable result state for the caller:

- success or invalid target flag
- final family id
- final target state or country
- damage severity band
- report scheduled yes or no
- recovery opened yes or no
- follow-up queued yes or no

Cleanup must clear temporary selection values and event targets. Persistent aftermath flags remain only on affected states and countries until recovery removes them.
