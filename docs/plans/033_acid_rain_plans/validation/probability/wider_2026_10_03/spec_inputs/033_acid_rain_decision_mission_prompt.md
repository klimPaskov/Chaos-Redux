# Event 033 Acid Rain decision and mission implementation prompt

Implement the complete national Acid Rain decision category described in Part 5 and the decision-cost matrix. Read the decision and mission skill, Event 33 runtime contract, AI matrix, current decision GUI, CBRN civilian-protection hooks, Deaths integration, and save migration rules before editing. Use `chaosx_decision_mission_auditor`, `chaosx_ai_probability_auditor`, `chaosx_event_ui_worker`, and `chaosx_event_completion_auditor`.

## Category contract

Every valid country receives the category as soon as Event 33 forms, even when no front is near it. Keep it visible while the country has an active project, warning, acute exposure, urgent effect, unresolved aftermath, or demobilization work. Close it when none of those conditions remain. AI uses the same effects and pays the same costs. The compact inlay shows phase, World Coverage, national Preparedness, warning or exposure status, and the map button.

## Permanent projects

Implement four component projects with four tiers each:

- Shelter Network, 7.5 Preparedness per tier
- Protected Water and Food, 6.25 per tier
- Medical and Protective Capacity, 6.25 per tier
- Transport and Infrastructure Resilience, 5 per tier

Together they produce 0 to 100 Preparedness. Their protection effects reduce the requested state-population loss before the exact mortality transaction. They must never work only by changing `local_manpower`, a casualty estimate, or a display counter. Use country bands A to D with multipliers 0.65, 0.85, 1.00, and 1.35. Use next-tier cost multipliers 1.00, 1.25, 1.55, and 1.90 and duration multipliers 1.00, 1.15, 1.35, and 1.60. Use the exact representative base costs and rounding rules in the matrix. Civilian factories and manpower are temporary commitments. Return each reservation once. Consume support equipment, trains, convoys, motorized equipment, and fuel as defined. Land and island Water variants are mutually exclusive.

Apply one project slot to fragile countries, two to established countries, and three only to qualifying great powers or the reviewed global-phase emergency case. Do not hide unaffordable projects. Show the missing resource and keep the button blocked. Cancellation must release temporary commitments, preserve consumed equipment, and never duplicate refunds.

## Urgent response

Implement these state-targeted or national actions:

- Activate Shelter Protocols
- Secure Emergency Water and Food
- Emergency Medical Surge
- Reroute Transport and Repair Crews
- Evacuate Forecast Severe Zone

Use the exact duration, country-band cost, target gate, expiry, effect, and action cap in the matrix. Every action uses no more than four resource types. Evacuation requires a live forecast and must complete before the first severe pulse to provide its full effect. Separate warning visit IDs and severe episode IDs prevent stale or duplicate action use. Action availability must remain useful under one, two, or three fronts.

## Recovery

Implement Restore Transport Network, Decontaminate Water and Soil, Repair Exposed Industry, and Demobilize Emergency Apparatus. Target only valid states or country ledgers. Prioritize tier-3 water and transport harm before low-tier industry damage. Recovery changes Event 33 aftermath state and can repair building damage through bounded effects. It must not erase Deaths history or remove Air Contamination already added.

## AI

Use threat states, affordability, reserve floors, country band, warning time, state population, capital status, aftermath tier, war status, convoy access, and current project balance. Implement the A1 through A20 cases in the AI matrix. Blocked options must not retain dominant effective weight. Strong CBRN protection can lower Medical priority but cannot replace national Preparedness. Landlocked countries never pay convoys. Island countries never pay trains and convoys for the same Water action.

Run the repository probability tools and `chaosx_ai_probability_auditor` against final weights. Record raw and effective weights for every case. Do not accept a design where a useful payable case has no reachable action, where the AI spends below reserve floors, or where an AI-only shortcut bypasses a player cost.

## Verification

Test exact-resource affordability, one-unit-short blocking, project cancellation, controller transfer, country capitulation, category visibility, multiple warnings, global phase, event dissipation, save reload, second generation, and AI behavior at each country band. Run UI checks at 1920 by 1080, 1600 by 900, and 1366 by 768. Finish only when every listed cost, effect, refund rule, AI case, and cleanup path has static and in-game evidence.
