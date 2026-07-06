# Improvement loop closure note for 011 Secret Alliance spec package

This is a planning-package closure note, not a substitute for the mandatory implementation-time `chaosx_improvement_loop_planner` pass.

The design has been expanded around a clear playable loop: hidden pact creation, slow evidence gathering, meaningful countermeasures, motive-based AI, dynamic evolutions, public faction reveal, reveal super-event, and post-reveal war memory. The package avoids adding full random-country focus trees because the event's strength is compatibility with existing campaign countries. Depth is carried through values, decisions, missions, AI, evidence, diplomacy, sabotage, and reveal consequences instead.

Broad expansion beyond this point would risk bloat if it added bespoke focus trees for every possible member, permanent country packages for random actors, or unrelated formables. The implementation-time improvement loop should inspect the actual implemented state and either confirm closure or identify missing depth that emerged during coding.

Implementation-time loop pass should check:

- whether Evidence and Preparedness visibly change outcomes
- whether Evolution II decisions are active enough
- whether Evolution III gives a final preparation window
- whether AI members act according to motive
- whether reveal super-event and audio are complete
- whether assets and localisation remain aligned
- whether hidden member cleanup is safe
- whether achievements are meaningful and not trivial
