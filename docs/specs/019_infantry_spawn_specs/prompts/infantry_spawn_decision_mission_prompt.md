# Infantry Spawn decision and mission implementation prompt

Use `hoi4-decisions-missions`, `chaos-redux-events`, and the full spec pack. This prompt is for the decision and mission layer of Event 019.

Implement the management category with phased visibility. The category should not exist as a permanent clutter list in baseline unless the country has active strain, backlog, missions, or cooldowns. Evolution II opens the main category. Evolution III turns it into a crisis layer. Evolution IV adds chaos unit containment and authorization.

Decision families to implement or plan in the first pass:

- inspect the wave
- sort depots
- standardize formations
- absorb local officers
- disband the worst units without equipment farming
- request a random unit with dynamic costs and cooldowns
- emergency front muster
- capital defense muster
- depot lottery
- ban further musters
- empower, rotate, arrest, or contain possessed generals
- hunt illegal regiments
- quarantine chaos units
- authorize base zombie training only
- cap zombie recruitment
- bind golem cadres
- exorcise ghost companies
- close the chaos ledger
- contain splinter countries

Use concrete costs. Prefer army XP, infantry equipment, support equipment, artillery, trucks, trains, fuel, manpower, stability, war support, supply strain, local state control, and time. Use political power only when it fits public decree or political concession. Keep command power costs conservative.

Missions should require action. Implement or plan Guard the depots, Register the regiments, Hold the capital rails, Break the rogue drill field, Seal the strange barracks, Prove the new command, and Recover the pale zone. Use named targets through scripted localisation and avoid raw state lists.

Every important decision and mission needs AI behavior, cleanup, custom trigger tooltips, concise cost text, and exploit protection. Do not expose giant raw triggers. Hide obsolete decisions after route changes, tag death, annexation, category closure, or splinter defeat.

Before completion, run a decision audit using `chaosx_decision_mission_auditor` in the implementation environment and resolve its findings.
