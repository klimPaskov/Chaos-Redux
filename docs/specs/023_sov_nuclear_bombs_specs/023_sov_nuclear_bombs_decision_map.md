# Event 023 decision and mission map

## Design rules

- Use one primary Event 23 decision category and one linked collapse-custody category only if current engine constraints make the combined surface unreadable.
- Show three to five primary actions in a normal phase. Six is the hard maximum.
- Show one to three active missions.
- Hide obsolete, invalid, and unrelated actions.
- Use no more than four spendable cost types per action.
- Use icon-first cost localisation.
- Use selected-target management for countries and selected-site management for storage or test states.
- Use dynamic costs and durations based on stockpile, distance, war state, site security, readiness, integrity, and current posture.
- Every reserved bomb, reactor entitlement, transferred device, and dismantled device needs one reconciled ledger transaction.
- Working decision names in this file are structural labels, not final localisation.

## Category header

| Display | Source | Purpose |
| --- | --- | --- |
| Operational bombs | Authoritative Soviet operational stockpile less reserved devices | Shows available arsenal |
| Arsenal Readiness | Event 23 visible value | Shows delivery and technical usability |
| Command Integrity | Event 23 visible value | Shows authorization and accounting reliability |
| Posture and knowledge | One compact dynamic status | Shows current strategic identity and foreign awareness |

Contextual tooltips can summarize storage risk, active target, response deadline, custody disputes, or exchange stage. They should not become additional permanent meters.

## Opening event choices

The event opening presents four mutually exclusive custody doctrines.

| Working choice | Immediate direction | Main strength | Main risk | AI preference |
| --- | --- | --- | --- | --- |
| Party custody | Political leadership controls codes, storage appointments, and release | High central Integrity | Slow release and purge vulnerability | Stable political leadership, peace, coup fear |
| Military custody | General Staff and delivery commands hold primary operational authority | High wartime Readiness | Military refusal, coup, or unauthorized preparation risk | Major war, loyal command, strong delivery force |
| Scientific safety veto | Technical certification is required before use | Accident control and high Integrity | Slow emergency response | Recent failure, peace, moratorium tendency |
| Dispersed special commands | Several regional commands receive bounded custody and emergency authority | Survivable retaliation | Lower Integrity and collapse risk | Evolution III or IV, exposed capital, nuclear rival |

A later doctrine reform is possible through one long decision after a command incident, evolution change, or major war-state change. It should cost time, command disruption, and institutional support. It cannot be switched repeatedly for free.

## Phase 1: Establish the arsenal

Normal visible actions: four or five.

### Audit the sealed stockpile

Type: timed decision or mission.

Purpose:

- Establish complete device accounting.
- Improve Command Integrity.
- Resolve a small number of uncertain opening entries.

Requirements:

- Event 23 active.
- No active full exchange.

Possible costs:

- Support equipment.
- Civilian factory burden.
- Command power.
- Time.

Dynamic factors:

- Larger stockpile increases duration.
- More storage sites increase duration.
- Party custody or scientific veto lowers failure risk.
- Soviet Collapse pressure raises duration and risk.

AI:

- High priority when Integrity is below 70 or Missing entries exist.

Cleanup:

- Cannot overlap with another full audit.
- Rebuilds the ledger once.

### Harden the highest-risk storage site

Type: selected-site timed decision.

Purpose:

- Improve one depot's defense, concealment, and local custody.
- Raise Integrity.
- Reduce theft, bombing, and collapse-seizure risk.

Requirements:

- Selected registered storage state.
- Soviet ownership and control.
- No active combat in the state.

Possible costs:

- Support equipment.
- Infantry equipment.
- Civilian factory burden.
- Manpower commitment.

Dynamic factors:

- Front distance, rail access, population, air defense, and current garrison.

AI:

- Prioritize exposed sites holding a large arsenal share.

Cleanup:

- Site has a cooldown and finite hardening stage.

### Disperse a reserve package

Type: timed decision.

Purpose:

- Move a bounded share of bombs from one site to two or more secure sites.
- Raise survivability and Readiness.
- Lower Integrity if communications or guards are weak.

Requirements:

- At least two valid storage states.
- Secure transport route.

Possible costs:

- Trains.
- Fuel.
- Support equipment.
- Command power.

Risks:

- Exposure.
- Convoy loss.
- Missing-device incident.
- Collapse transfer during transit.

AI:

- Use when a site is threatened by war or enemy nuclear targeting.
- Avoid during low Integrity or contested transport.

Cleanup:

- Each device moves once and remains in transit until completion.

### Centralize release authority

Type: doctrine support decision.

Purpose:

- Improve Integrity and prevent unauthorized use.
- Lower rapid response and survivability.

Requirements:

- Not already at the strongest centralization stage.
- No imminent retaliation deadline.

Possible costs:

- Command power.
- Temporary Readiness loss.
- Time.

AI:

- Use after a refusal incident, missing device, or collapse recovery.

### Delegate emergency retaliation

Type: doctrine support decision.

Purpose:

- Improve survivable retaliation.
- Raise Readiness.
- Lower Integrity.

Requirements:

- Evolution III or IV, or confirmed enemy nuclear threat.
- Valid regional command and storage.

Possible costs:

- Command power.
- Support equipment.
- Temporary political or command strain.

AI:

- Use only when central command is exposed and Integrity remains adequate.

## Phase 2: Production and delivery

Normal visible actions: three to five, depending on stockpile and capability.

### Expand fissile production

Type: reactor construction entitlement decision.

Purpose:

- Use one queued reactor entitlement or begin event-owned reactor construction.
- Raise future bomb production.

Requirements:

- Valid selected Soviet state.
- Current vanilla reactor route verified.
- No active combat or transfer risk in the state.

Possible costs:

- Civilian factory burden.
- Fuel or resource commitment if supported.
- Construction time.

AI:

- Build only when below the posture production cap and the site can be defended.

Cleanup:

- One entitlement is consumed after successful placement.
- Invalid placement does not consume the entitlement.

### Assemble a device batch

Type: timed decision.

Purpose:

- Convert current nuclear production into a bounded batch of operational bombs.

Requirements:

- Verified atomic capability.
- Sufficient reactor or production progress.
- Secure assembly access.
- Storage capacity.

Possible costs:

- Civilian factory burden.
- Support equipment.
- Time.

Dynamic batch size:

- Reactor capacity.
- Evolution stage.
- Readiness.
- Integrity.
- Current reserve floor.

AI:

- Build toward posture reserve, then stop.

Cleanup:

- Batch transaction applies once.

### Prepare delivery crews

Type: timed mission.

Purpose:

- Train and certify crews for the current vanilla delivery route.
- Raise Readiness.

Requirements:

- A valid delivery platform exists.
- Fuel and access are available.

Possible costs:

- Air experience or the current route's relevant experience.
- Fuel.
- Command power.
- Temporary aircraft commitment if supported.

AI:

- High priority if bombs exist but no prepared delivery route does.

### Conduct a command exercise

Type: timed mission.

Purpose:

- Test communication, authentication, target transfer, and abort procedures.
- Improve Readiness and Integrity when successful.

Possible costs:

- Command power.
- Fuel.
- Temporary delivery-force availability.

Failure risks:

- False order.
- Lost code material.
- Public exposure.

AI:

- Use before a public test, major ultimatum, or retaliation posture.

### Install stronger authentication

Type: safety decision.

Purpose:

- Improve Integrity and reduce unauthorized-use incidents.
- Add delay to rapid release.

Possible costs:

- Support equipment.
- Civilian factory burden.
- Time.

AI:

- Prioritize after custody disputes or at high stockpile size.

## Phase 3: Test program

Normal visible actions: survey, prepare, conduct, cancel, investigate.

### Survey a remote test state

Type: selected-state decision.

Purpose:

- Lock a valid exact test state.
- Calculate site quality.

Requirements:

- Soviet-owned and controlled state.
- Low population preference.
- No active combat.

Possible costs:

- Civilian factory burden.
- Trains.
- Time.

AI:

- Select remote secure interior states.

### Prepare an instrumented proof test

Type: timed mission.

Purpose:

- Prepare the safest secret detonation.

Possible costs:

- One reserved bomb.
- Support equipment.
- Trains.
- Civilian factory burden.

Duration:

- 90 to 120 days, dynamically modified.

AI:

- Preferred for first test under secrecy.

### Prepare a concealed field test

Type: timed mission.

Purpose:

- Gain readiness while preserving deniability.

Possible costs:

- One reserved bomb.
- Trains.
- Fuel.
- Support equipment.

Duration:

- 120 to 180 days.

Risk:

- Higher accident and exposure chance.

AI:

- Use when site quality is strong and public reveal is undesirable.

### Prepare a public demonstration

Type: timed mission.

Purpose:

- Prove the arsenal openly.
- Unlock Demonstrative Deterrence.

Possible costs:

- One reserved bomb.
- Civilian factory burden.
- Support equipment.
- Diplomatic preparation as a consequence, not a fifth spendable cost.

Duration:

- 90 to 150 days.

AI:

- Use when a rival exists, secrecy is failing, or deterrence is needed.

### Strengthen evacuation and instrumentation

Type: supporting decision during test preparation.

Purpose:

- Reduce death and accident risk.
- Improve useful data.

Possible costs:

- Support equipment.
- Manpower commitment.
- Civilian factory burden.

AI:

- Use when site population, accident risk, or foreign observation is high.

### Cancel the prepared test

Type: cancel decision.

Purpose:

- Return the bomb after accounting.
- End site preparation.

Consequences:

- Readiness cost.
- Possible exposure if preparation was observed.

### Investigate a failed or compromised test

Type: timed mission.

Purpose:

- Recover evidence, staff, and command reliability.

Possible costs:

- Support equipment.
- Civilian factory burden.
- Command power.

AI:

- High priority after failure.

## Phase 4: Target selection and coercion

Normal visible actions after selecting one target: private signal, public ultimatum, demonstrate, prepare strike, close target.

### Select a target country

Type: target selector.

Purpose:

- Store one current target.
- Activate only the valid target decisions.

Player visibility:

- Human player sees one selector.
- AI sees all valid targets through scoring.

Cleanup:

- Clear on invalidity, settlement, annexation, faction alignment, or category close.

### Send a private signal

Type: clickable decision.

Purpose:

- Issue a limited secret demand.

Possible costs:

- Political power.
- Intelligence exposure or an equivalent consequence.
- Time.

AI:

- Preferred before public escalation when secrecy remains valuable.

### Issue a public ultimatum

Type: clickable decision plus response mission.

Purpose:

- Name a demand and deadline.

Possible costs:

- Political power.
- Command power.
- Credibility risk as a consequence.

Duration:

- 14 to 45 days.

AI:

- Use when arsenal is Demonstrated and the demand is enforceable.

### Stage a wartime demonstration

Type: test-linked decision.

Purpose:

- Detonate one bomb away from a direct combat target to support the demand.

Possible costs:

- One bomb.
- Delivery fuel or route cost.
- Command power.
- Support equipment.

AI:

- Prefer before limited combat use when time and reserve permit.

### Prepare a limited strike

Type: selected-profile and selected-state mission.

Purpose:

- Lock one exact target state and profile.
- Reserve one bomb.
- Start target response and evacuation time.

Possible costs:

- One bomb reservation.
- Fuel.
- Command power.
- Relevant experience or support commitment.

Duration:

- 7 to 30 days, depending on delivery route and urgency.

AI:

- Use only under profile-specific hard gates.

### Accept a partial settlement

Type: response action.

Purpose:

- End or reduce the demand without detonation.

Consequences:

- Settlement record.
- Credibility change.
- Target cooldown.

### Raise or narrow the demand

Type: response action during negotiation.

Purpose:

- Change the requested outcome.

Rules:

- Raising the demand increases resistance and shortens time.
- Narrowing the demand can improve compliance.
- The action cannot reset the whole response mission indefinitely.

### Back down

Type: response action.

Purpose:

- End the crisis without settlement.

Consequences:

- Credibility and Integrity loss.
- Target cooldown.
- No reward.

## Phase 5: Strike authorization

Normal visible actions: certify, authorize, hold, redirect, abort.

### Complete technical certification

Type: mission completion or decision.

Purpose:

- Recheck device, delivery, target, and command.

Possible outcomes:

- Certified.
- Delayed.
- Safety veto.
- Invalid target.

### Overrule a safety veto

Type: high-risk decision.

Purpose:

- Continue preparation despite technical objection.

Requirements:

- Custody doctrine permits political or military override.
- Readiness remains above the minimum.

Costs and risks:

- Major Integrity loss.
- Accident risk.
- Scientist refusal or defection.

AI:

- Rare, and only during severe war or confirmed retaliation.

### Give final authorization

Type: deliberate final decision.

Purpose:

- Call the shared strike adapter once.

Requirements:

- Every target, delivery, stockpile, war, posture, readiness, integrity, and settlement check passes at click time.

AI:

- Freshly reevaluates the complete situation.

### Hold the strike

Type: pause decision.

Purpose:

- Preserve preparation while negotiations continue.

Consequences:

- Readiness cost over time.
- Exposure rises.
- Bomb remains reserved.

### Redirect the target state

Type: selected-state decision.

Purpose:

- Choose another valid state under the same profile.

Consequences:

- New certification delay.
- No free change to a higher-consequence profile.

### Reduce to remote demonstration

Type: de-escalation decision.

Purpose:

- Replace a combat strike with a demonstration.

Consequences:

- Shared test consequences.
- Lower immediate military effect.
- Possible target response.

### Abort and recover the device

Type: cancel decision.

Purpose:

- End preparation before release.

Consequences:

- Return bomb after accounting.
- Credibility or readiness loss if preparation was public.

## Phase 6: Exchange crisis

Normal visible actions: hotline, stand-down, limit response, preserve reserve, authorize retaliation.

### Establish an emergency hotline

Type: timed diplomatic decision.

Purpose:

- Create direct or mediated communication.
- Extend decision time.
- Help resolve false warnings.

Possible costs:

- Political power.
- Intelligence exposure as a consequence.
- Time.

AI:

- High priority before confirmed cross-major detonation.

### Propose reciprocal stand-down

Type: diplomatic decision plus opponent response.

Purpose:

- Pause new authorizations.

Requirements:

- Valid opposing nuclear major.
- No unresolved released strike that makes the proposal meaningless.

AI:

- Use when both sides retain command and the exchange remains limited.

### Limit the retaliation profile

Type: command decision.

Purpose:

- Restrict the next response to military or logistics targets.

Possible costs:

- Command power.
- Readiness adjustment.

AI:

- Preferred after limited enemy use.

### Preserve a reserve

Type: timed command decision.

Purpose:

- Remove part of the arsenal from immediate release and harden it.

Possible costs:

- Trains.
- Fuel.
- Support equipment.
- Readiness reduction.

AI:

- Use when enemy first-strike risk is high.

### Authorize retaliation

Type: final decision.

Purpose:

- Prepare and release a valid response after confirmed enemy use.

Rules:

- Same exact-state and shared-adapter contract as first use.
- Profile is constrained by the enemy action and current evolution.

### Suspend release orders

Type: pause decision.

Purpose:

- Freeze new Event 23 launches during talks.

Consequences:

- Improves Integrity.
- Reduces immediate Readiness.

### Enter Atomic Moratorium

Type: long decision chain.

Purpose:

- End ordinary targeting and begin sealed reserve, transfer, or dismantlement.

Requirements:

- No released strike.
- Active reservations reconciled.
- Custody ledger available.

## Phase 7: Soviet Collapse custody

Normal visible actions after selecting one crisis: recall, secure route, negotiate, raid or disable, restore ledger.

### Select a disputed depot or breakaway

Type: site or country selector.

Purpose:

- Show only actions for one custody crisis.

### Recall devices

Type: timed transport decision.

Possible costs:

- Trains.
- Fuel.
- Support equipment.
- Manpower commitment.

Mission objective:

- Maintain a valid controlled route until transfer completes.

### Secure the rail corridor

Type: goal mission.

Objective:

- Hold named states and rail hubs with supplied divisions.

Duration:

- 90 to 180 days based on distance and front state.

Success:

- Transfer continues and Integrity improves.

Failure:

- Custody can pass to the breakaway or become Missing.

### Negotiate return or joint custody

Type: diplomatic decision.

Possible costs:

- Political power.
- Economic aid or fuel.
- Security assurance as a consequence.

Outcome:

- Return, joint custody, monitored dismantlement, or refusal.

### Conduct a recovery raid

Type: timed operation.

Possible costs:

- Command power.
- Infantry equipment.
- Support equipment.
- Fuel.

Risks:

- Device destruction.
- Material loss.
- Staff death.
- Foreign intervention.

### Disable the devices

Type: technical action.

Possible costs:

- Intelligence access.
- Support equipment.
- Technical time.

Outcome:

- Technical Denial status.

### Destroy the site

Type: last-resort decision.

Requirements:

- Recovery impossible.
- Operationalization imminent.
- Exact site validated.

Outcome:

- Shared demolition or accident profile.
- No automatic nuclear yield.

### Restore the ledger

Type: timed audit.

Purpose:

- Reconcile recovered, transferred, dismantled, and missing devices.

Success:

- Integrity recovery.
- Obsolete crisis actions close.

## Phase 8: Dismantlement and restraint

### Seal a reserve batch

Type: timed decision.

Purpose:

- Remove a batch from operational use while retaining it under strict custody.

### Dismantle a batch

Type: timed decision.

Possible costs:

- Civilian factory burden.
- Support equipment.
- Technical time.

Outcome:

- Bomb count falls permanently.
- Material compensation only if a verified shared or settlement route provides it.

### Invite observers

Type: diplomatic decision.

Purpose:

- Improve verification and foreign confidence.
- Reveal sites and reduce future secrecy.

### Negotiate reciprocal restraint

Type: diplomatic mission.

Purpose:

- Link Soviet moratorium to another nuclear actor's stand-down.

### Reactivate the arsenal

Type: long emergency decision.

Requirements:

- Atomic Moratorium active.
- Severe crisis.
- Valid operational reserve.
- Long preparation.

Consequences:

- Major Integrity and diplomatic cost.
- Public knowledge remains.

## Mission duration summary

| Mission family | Normal duration |
| --- | --- |
| Stockpile audit | 90 to 150 days |
| Site hardening | 120 to 240 days |
| Device transfer | 30 to 180 days based on route |
| Reactor construction | Current verified construction route |
| Device batch assembly | 60 to 180 days |
| Delivery crew preparation | 60 to 120 days |
| Command exercise | 45 to 90 days |
| Test preparation | 90 to 180 days |
| Ultimatum response | 14 to 45 days |
| Strike preparation | 7 to 30 days |
| Retaliation window | 3 to 30 days based on certainty and command |
| Rail corridor security | 90 to 180 days |
| Breakaway technical access | 180 to 360 days |
| Breakaway command formation | 180 to 360 days |
| Delivery integration | 120 to 360 days |
| Dismantlement batch | 90 to 240 days |
| Moratorium verification | 180 to 365 days |

## Decision audit questions

- Does every action represent a concrete state action, mission, transport, test, demand, launch, negotiation, or dismantlement?
- Are no more than six primary actions visible in one phase?
- Are active missions capped at three?
- Does every cost fit the action and stay within four spendable types?
- Are selected targets and states named clearly?
- Does every bomb transaction reconcile?
- Can AI use every human gameplay system through an equivalent route?
- Do invalid targets hide or clean up?
- Do success, partial success, failure, and cancellation differ?
- Do focus hooks, if any, modify existing decisions without creating a new Soviet tree?
- Are rewards and penalties large enough to change play?
- Are no decisions repeated only to give tiny modifiers?
