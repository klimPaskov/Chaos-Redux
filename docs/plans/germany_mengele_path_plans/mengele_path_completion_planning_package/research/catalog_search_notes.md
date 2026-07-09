# Catalog search notes

## chaos_redux_events_catalog.csv

Rows: 1014

Headers: `ID, Event Name, Details, Evo I, Evo II, Evo III, Evo IV, Evo V, World-End Scenario, Type, Cluster ID, Member Severity, Status`
Matches:
- Line 4: `The Holy Realm`. Transforms Tibet or a Tibet-centered Himalayan state into the Holy Realm. The route begins as a defensive mountain refuge, develops into a Bodhisattva-led state, creates the Arhat Administration, reaches the Buddha Mandate, and can branch into restraint, peacekeeping, coercive pacification, Divine Sovereignty, or the final doctrine. Evolutions are focus-path gates, while the actual mechanics come from the selected focuses, decisions, and events inside those unlocked paths.
- Line 71: `Gods of Africa`. Africa gods predict total chaos and the world will burn. Decisions to pray to them or suffer disasters. More ignorance causes the disasters to escalate and become more rapid till the culmination, which would be a destruction to player’s campaign. Use existing events for disasters.
- Line 167: `The Custerdome`. If the player manages to keep the chaos meter low for a very long time, then get this easter egg event. The place of wealth and peace. Campaign end. (Can only happen if the user is exremely lucky with the events and doing everything they can to keep the Chaos low until 1944)

## chaos_redux_clusters_catalog.csv

Rows: 14

Headers: `Cluster ID, Cluster Name, Details, Members (ID), Type, Chaos level, Status`
No matches for `mengele`, `auschwitz`, `tibet`, `genocide`, or `camp`.

## chaos_redux_scenarios_catalog.csv

Rows: 7

Headers: `Scenario ID, Scenario Name, Details, Type Options, Intensity Scaling, Status`
No matches for `mengele`, `auschwitz`, `tibet`, `genocide`, or `camp`.


## Conclusion

The event catalog CSV does not expose a standalone Mengele event row. The Holy Realm row is relevant because the current implementation map says the Tibet Expedition can interact with Holy Realm states and assets. The coding agent should not invent a new catalog event row until repository discovery shows how the Germany chain is documented in the full repo.
