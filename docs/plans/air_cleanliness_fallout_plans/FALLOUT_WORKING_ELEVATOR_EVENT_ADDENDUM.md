# Fallout Working Elevator event addendum

The Working Elevator adds a country-level food-storage family after First
Streetlight. It treats a surviving grain hopper as a decision about public
rations, military logistics, licensed trade, or refugee intake. Four authored
policies have distinct costs, thresholds, durable ledgers, prose, AI priorities,
modifiers, and Event Log payloads.

The implementation surfaces are:

- candidate `324`, transaction `710020`, route `7120`
- events `chaosx.fallout.324` through `.330`
- history `9125` with fifteen payload values
- Food, Power, Fuel, Scrap, Clean Water, Shelter Capacity, Cohesion,
  Recognition, Reclamation, grain capacity, logistics, market legitimacy,
  refugee integration, and spoilage variables
- dedicated Working Elevator report art and a registered sprite
- human and hidden AI parity, delayed result, callback, authenticated cleanup,
  Deaths-backed failure, and dormant scheduler state

The hopper result is delayed by 28 days. The storehouse maintenance callback is
delayed by 210 days. The result modifier lasts 330 days and the callback
modifier lasts 240 days. Failure rates are 0.05 percent for the result and
0.025 percent for the callback, both routed through Deaths.

This tranche is intentionally dormant until a live activation coordinator is
approved. It does not claim the engine-native all-province thermonuclear sweep,
blackout authority, save recovery, or multiplayer proof.
