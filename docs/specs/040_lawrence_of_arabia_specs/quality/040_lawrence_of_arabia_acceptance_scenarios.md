# Event 40 Acceptance Scenarios

## Purpose

These scenarios are implementation acceptance contracts. Source inspection, HOI4 MCP evidence, repository checks, and user live testing should use the same scenario names where possible.

A scenario can pass only when its visible outcome, ledger state, cleanup, AI behavior, and persistent memory agree.

## Baseline eligibility

### `L40-ELIG-001 Britain absent`

Setup:

- Britain does not exist.
- One or more ordinary Arabian countries exist.

Expected:

- Event 40 has no valid automatic target.
- Normal manual firing reports the missing sponsor.
- Force-trigger behavior follows the shared force-mode contract without creating a broken sponsor.
- No Lawrence character or active category appears.

### `L40-ELIG-002 No Arabian target`

Setup:

- Britain is valid.
- Every country in the Event 40 registry is annexed, special Chaos, nonhuman, or otherwise invalid.

Expected:

- Event 40 shows `N/A` eligibility through the event system.
- No target pointer is saved.
- The Fire-Once state is not consumed by a failed automatic attempt.

### `L40-ELIG-003 Player target remains valid`

Setup:

- The player controls a valid Arabian minor.
- Several AI targets also exist.

Expected:

- The player country is included in the candidate pool.
- It is not excluded because it is not a major.
- Its score follows the same declared factors as AI targets.

### `L40-ELIG-004 Special Chaos exclusion`

Setup:

- A Malta Crusaders or other special Chaos actor controls territory inside the geographic registry.

Expected:

- The special actor is not selected as an ordinary target.
- Its territory can affect route access and rivalry.
- The exclusion tooltip is concise and does not expose the shared classifier internals.

### `L40-ELIG-005 Independence Wave successor`

Setup:

- Independence Wave creates a stable country with a capital and core territory in the Event 40 registry.

Expected:

- The successor becomes eligible after stabilization.
- No duplicate tag or package is created.
- It inherits applicable regional preparedness and route facts.

## Entry and character identity

### `L40-CHAR-001 Concealed survival opening`

Setup:

- Standard 1936 campaign.
- Lawrence is not already defined as a live character.

Expected:

- The opening acknowledges that he was believed dead.
- One canonical Lawrence character is created.
- The event uses a grounded portrait source package.
- No supernatural resurrection flag or text appears.

### `L40-CHAR-002 Existing character ownership`

Setup:

- Vanilla or another Chaos Redux package already owns a live Lawrence character.

Expected:

- Event 40 reuses or transfers the existing character through a guard.
- No clone appears in another roster.
- The ownership disposition is documented.

### `L40-CHAR-003 Permanent death`

Setup:

- Lawrence dies during a rescue, revolt, or combat incident.

Expected:

- Every Lawrence-dependent action and route closes.
- Britain can continue only through eligible local agents at reduced strength.
- Lawrence's Kingdom becomes impossible.
- Save and reload preserve death.

## Public mechanic clarity

### `L40-UI-001 One public value`

Setup:

- Active baseline intervention.

Expected:

- The target category shows Lawrence's Influence as the only persistent Event 40 value.
- Hidden reach, cells, trust, and readiness do not appear as extra counters.
- The player can identify the current band, trend, next threshold, and a useful action.

### `L40-UI-002 Action budget`

Setup:

- Test opening, middle, dominant, detention, and Evolution I phases.

Expected:

- Each phase shows three to five primary decisions in normal conditions.
- No phase exceeds six.
- No more than two Event 40 missions are normally active.
- Obsolete decisions disappear.

### `L40-UI-003 No custom-window dependency`

Setup:

- Open the intervention and federation systems.

Expected:

- All required gameplay is usable through decisions, missions, events, and ordinary headers.
- Missing scripted GUI code does not block the event.

## Baseline outcomes

### `L40-BASE-001 British client`

Setup:

- Influence remains in the dominant band through the confirmation period.
- Britain has a valid client route and can sustain it.

Expected:

- A real autonomy or diplomatic client relationship forms.
- The target receives the promised material and institutional package.
- Britain receives access and policy leverage.
- The country remains playable.
- The target cannot be selected again as a fresh ordinary intervention.

### `L40-BASE-002 Independent ally`

Setup:

- Influence remains controlled in the middle band.
- The target completes national-custody and treaty work.

Expected:

- The target remains sovereign.
- Britain gains the negotiated access only.
- The target becomes a valid later Evolution II partner without being treated as a subject.

### `L40-BASE-003 Expulsion at low Influence`

Setup:

- Influence is low.
- The target controls routes and has enough state capacity.

Expected:

- Lawrence leaves without an automatic revolt.
- The local network remains only where it has actual surviving strength.
- Neighboring preparedness rises.
- Britain receives no free recovery attempt.

### `L40-BASE-004 Reckless expulsion at high Influence`

Setup:

- Influence is high.
- Evolution I is active.
- The target expels the mission without securing officers or routes.

Expected:

- A revolt-network incident can occur.
- The result depends on actual cells and officer support.
- A civil war occurs only after a viable territorial and military split is proven.

### `L40-BASE-005 Arrest and negotiated exchange`

Setup:

- The target detains Lawrence.
- Britain chooses negotiation.

Expected:

- Ordinary Lawrence actions pause.
- The exchange transfers the exact agreed concessions once.
- Release restores one character to one roster.
- The same detention cannot be farmed for repeated concessions.

### `L40-BASE-006 Double-game success`

Setup:

- The target accepts British aid, turns a contact, feeds controlled intelligence, and prevents dominance.

Expected:

- The target keeps the validated aid.
- Britain loses expected leverage.
- A sovereign settlement becomes available.
- Exposure and retaliation risks are recorded.

### `L40-BASE-007 Lawrence defection`

Setup:

- High personal trust.
- Credible independent charter.
- British overreach or disavowal.
- Sufficient local success.

Expected:

- Defection occurs through a chain, not one cheap option.
- British personal actions close.
- Lawrence moves to one independent role.
- The regional campaign changes immediately.
- Event-owned Chaos applies once.

## Regional progression

### `L40-REG-001 Internal follow-up does not repeat pacing`

Setup:

- First intervention resolves.
- A second target is selected after the regional delay.

Expected:

- No second random Event 40 History entry is created.
- No second Fire-Once transaction occurs.
- No extra minor-event timer pressure is applied.
- The second target receives a new campaign generation.

### `L40-REG-002 Previous success helps later intervention`

Setup:

- Britain has a nearby client with port, rail, or air access.

Expected:

- The later target receives higher British reach from the real node.
- The client can contribute or refuse.
- No whole-world scan is needed.

### `L40-REG-003 Previous failure creates preparedness`

Setup:

- A target publicly exposes and dismantles the network.
- A neighboring country becomes the next target.

Expected:

- The neighbor receives preparation or detection benefits.
- Britain faces lower promise credibility.
- The previous target does not receive a second opening package.

### `L40-REG-004 Britain temporarily unable`

Setup:

- Britain loses route access during the regional delay.

Expected:

- The chain pauses without clearing durable outcomes.
- It resumes only after valid access returns.
- A timeout or permanent-failure condition can close the campaign cleanly.

## Evolution I

### `L40-E1-001 Pre-fire evolved opening`

Setup:

- Chaos is at least 200.
- Evolution I is enabled.
- Event 40 has not fired.

Expected:

- The first target starts with one relevant cell footprint and stronger British access.
- The target receives an immediate response.
- No automatic coup or war occurs.
- One Evolution I log entry is created at the correct time.

### `L40-E1-002 Strong intelligence breaks cells`

Setup:

- A target with strong counterintelligence, stable government, and route control.

Expected:

- Detection and suppression outperform a weak target under the same network conditions.
- Success can prevent armed escalation.
- The AI chooses evidence and route actions before reckless arrest.

### `L40-E1-003 Viable government replacement`

Setup:

- High Influence, divided officers, valid replacement coalition, and British support.

Expected:

- The replacement government has a leader, forces, supply, and playable setup.
- The transfer is bounded and rollback-safe.
- Event-owned Chaos applies once.
- Shared coup, ideology, or subject consequences are not double counted.

## Evolution II

### `L40-E2-001 Existing clients form a system`

Setup:

- At least two valid settled partners.
- Evolution II is enabled and activated.

Expected:

- Regional institutions use real participants.
- Clients can contribute, refuse, or demand compensation.
- The British Arabian System milestone logs once.
- The system does not invent an empty faction.

### `L40-E2-002 Pre-fire high Chaos without clients`

Setup:

- Chaos is at least 400.
- Event 40 has not fired.
- Britain has no valid regional clients or nodes.

Expected:

- Evolution II changes the objective and first-target pressure only where existing relationships support it.
- No clients, bases, or institutions are conjured.

### `L40-E2-003 Counter-bloc formation`

Setup:

- Three independent governments oppose British encirclement.

Expected:

- Founding rules, membership, shared purpose, and failure logic operate.
- Refusing governments remain outside.
- The bloc can share counterintelligence and congress preparation.

## Evolution III and federation

### `L40-E3-001 British Arabia transaction`

Setup:

- Several clients, dominant British influence, valid core, secure routes.

Expected:

- One federation transaction runs.
- Territory, units, equipment, leaders, wars, and subjects transfer without duplication.
- British Arabia receives its country package and super-event.
- Federal Authority begins and Lawrence's Influence closes.

### `L40-E3-002 Independent federation`

Setup:

- Sovereign charter, at least three valid participants, legitimate core, and defensible settlement.

Expected:

- Only ratifying states join.
- Founding territory receives justified cores.
- Disputed territory begins with claims or integration work.
- Event-owned stabilizing Chaos applies once.

### `L40-E3-003 Lawrence's Kingdom remains rare`

Setup:

- Test one ordinary high-Chaos campaign without the hidden personal conditions.
- Test one campaign with every accepted condition.

Expected:

- Ordinary campaign cannot select the kingdom merely from high Chaos.
- Full-condition campaign can unlock the route.
- AI selection remains far below ordinary federation routes.
- Lawrence occupies one leader role and has a succession package.

### `L40-E3-004 Federation rollback`

Setup:

- Force a validation failure before final state transfer.

Expected:

- No partial federation remains.
- Member countries retain their states, units, stockpiles, and leaders.
- Player control does not become stranded.
- Failure is logged for debugging without creating a player-facing fake settlement.

## Cross-event behavior

### `L40-XEV-001 Malta severs the route`

Setup:

- Malta Crusaders controls key Levantine or eastern Mediterranean access.

Expected:

- British route scores and actions update.
- Malta is treated as a rival external power.
- Malta is never selected as an ordinary target.

### `L40-XEV-002 Intel Leaked exposes contacts`

Setup:

- Intel Leaked fires while an Event 40 network exists.

Expected:

- Existing records create evidence and exposure.
- No nonexistent contact is fabricated.
- The network is not automatically erased.

### `L40-XEV-003 Famine and displacement accounting`

Setup:

- An Evolution I revolt closes a food route and displaces civilians.

Expected:

- Famine and Migration receive proven requests through their owner contracts.
- Population loss is recorded once by the owning transaction.
- Event 40 does not duplicate deaths.

## Cleanup and persistence

### `L40-CLEAN-001 Target annexed mid-intervention`

Setup:

- The active target is annexed.

Expected:

- Active missions close.
- The successor or occupier is evaluated through explicit transition logic.
- Invalid pointers and temporary modifiers are cleared.
- Durable evidence and character state remain coherent.

### `L40-CLEAN-002 Britain capitulates`

Setup:

- Britain capitulates while Lawrence is active abroad.

Expected:

- Sponsor actions pause or close according to permanent capacity.
- Lawrence can seek evacuation, local service, defection, or retirement through valid paths.
- No equipment deliveries continue without a sponsor.

### `L40-CLEAN-003 Save and reload`

Setup:

- Save during opening, active mission, detention, regional delay, Evolution II system, and federation formation.

Expected:

- Active target, generation, Influence, character state, decisions, missions, and settlements persist.
- No duplicate Lawrence character, mission, or aid receipt appears after reload.

### `L40-CLEAN-004 Campaign complete`

Setup:

- End the regional campaign through each major completion route.

Expected:

- Active target and temporary arrays clear.
- Settlements, federation state, character death, achievements, and Event Details history remain.
- No periodic processing continues for a closed campaign.
