# Event 023 specification, Part 10: Achievements, acceptance scenarios, and closure

## Achievement purpose

Event 23 achievements should reward distinct play identities:

- Building a credible arsenal.
- Avoiding combat use.
- Winning coercion without detonation.
- Recovering a scattered arsenal.
- Stopping an exchange.
- Using one weapon, then ending the program.
- Resisting the final pressure to launch.

Achievement labels below are working labels. Final wording requires a localisation pass and cultural or historical source review where an allusion is used.

## Achievement 1: A Hundred Suns

Working ID: `023_sov_nuclear_bombs_a_hundred_suns`.

### Goal

After Event 23 fires, reach at least 90 Arsenal Readiness while maintaining at least 100 accounted operational Soviet bombs and no Missing custody entries.

### Purpose

Rewards mastery of storage, delivery, maintenance, and accounting. It confirms that the opening grant became a usable arsenal.

### Disqualifiers

- Event 23 never fired.
- The player is not controlling the Soviet host when the goal is completed.
- Debug-only direct variable manipulation if the project achievements system tracks it.

### Asset direction

A dense field of sealed Soviet bomb casings or storage doors under a hard industrial light. The image should communicate scale and control, not detonation.

## Achievement 2: The Bomb Never Fell

Working ID: `023_sov_nuclear_bombs_the_bomb_never_fell`.

### Goal

Publicly demonstrate the Soviet arsenal, reach Evolution II or later, resolve at least one serious nuclear crisis, then enter Atomic Moratorium with zero Soviet combat nuclear detonations and every device accounted, transferred, or dismantled.

### Purpose

Rewards deterrence and restraint after the player has enough capability to use the weapon.

### Serious crisis qualification

At least one of the following:

- A public ultimatum reached its final response window.
- A nuclear major confrontation became active.
- Soviet Collapse created a disputed custody site.
- The Soviet Union suffered a confirmed enemy nuclear threat or launch preparation.

### Disqualifiers

- Any Soviet combat nuclear detonation.
- Any Missing device when the moratorium completes.
- Entering moratorium before a qualifying crisis.

### Asset direction

A locked bomb cradle, sealed keys, or a dismantlement table with a distant test cloud outside the facility.

## Achievement 3: Ultimatum Without Ash

Working ID: `023_sov_nuclear_bombs_ultimatum_without_ash`.

### Goal

Secure full or partial compliance from a valid independent target through an Event 23 nuclear ultimatum without a Soviet combat detonation against that target.

### Additional requirements

- The target was not already a Soviet subject.
- The demand had a real strategic objective.
- The target response was recorded through the normal mission.
- The settlement remained in force for a minimum verification period.

### Disqualifiers

- The demand used a debug force-success route.
- The target was already capitulated or had no meaningful ability to refuse.
- The settlement is broken immediately by the Soviet Union.

### Asset direction

A signed armistice or transfer document beside sealed launch keys and an unused device. Avoid readable generated text.

## Achievement 4: Scattered Arsenal

Working ID: `023_sov_nuclear_bombs_scattered_arsenal`.

### Goal

During Event 5, recover or verifiably dismantle every Soviet device placed under breakaway, joint, foreign, disputed, or Missing custody, then restore Command Integrity to at least 80.

### Additional requirements

- At least two breakaway custody crises occurred.
- At least one crisis was resolved through negotiation, joint custody, or monitored dismantlement.
- No operational breakaway nuclear actor remains.

### Disqualifiers

- A device is duplicated or removed outside the custody ledger.
- The Soviet Union simply annexes every holder without completing accounting.
- A shared terminal world state ends the campaign before reconciliation.

### Asset direction

Guarded rail lines converging on a sealed central depot, with several numbered or symbolically distinct crates. No readable numbers are required.

## Achievement 5: Firebreak

Working ID: `023_sov_nuclear_bombs_firebreak`.

### Goal

After a confirmed nuclear strike between major powers, achieve a reciprocal stand-down before the exchange reaches General Exchange and before shared Fallout begins.

### Additional requirements

- At least two nuclear majors entered the exchange crisis.
- At least one confirmed cross-major detonation occurred.
- The Soviet Union participated in the hotline or stand-down process.
- The stand-down persists through a verification period.

### Disqualifiers

- The exchange reaches the General Exchange stage.
- The shared Fallout terminal route begins before verification.
- One side violates the stand-down during the verification period.

### Asset direction

Two damaged communication lines joined across a burned horizon, or two command telephones connected while distant smoke rises.

## Achievement 6: First and Last

Working ID: `023_sov_nuclear_bombs_first_and_last`.

### Goal

Conduct exactly one Soviet combat nuclear detonation, then complete a verified dismantlement or transfer of every remaining Soviet device and enter Atomic Moratorium without another Soviet combat detonation.

### Additional requirements

- The first use was authorized through the normal Event 23 chain.
- All reserved, stored, missing, breakaway, and joint-custody devices are reconciled.
- The moratorium remains active through a verification period.

### Disqualifiers

- A second Soviet combat detonation.
- A remaining operational Soviet device after completion.
- A hidden unaccounted device.

### Asset direction

One distant test or combat cloud reflected on dismantlement tools and an empty storage rack.

## Achievement 7: The Last Telephone

Working ID: `023_sov_nuclear_bombs_the_last_telephone`.

### Goal

At Evolution IV, during a valid Soviet AI or player first-use crisis against a nuclear major, complete an emergency hotline and stand-down while the Soviet Union faces the severe strategic-loss conditions that would otherwise permit launch.

### Additional requirements

- Chaos is at least 1000.
- The opponent has operational nuclear capability.
- The Soviet capital, capitulation state, or verified enemy launch preparation satisfies the first-use emergency gate.
- A strike was prepared far enough to reach final authorization.
- The Soviet Union chooses hold or stand-down and the opponent reciprocates.

### Disqualifiers

- A Soviet first-use detonation occurs during the crisis.
- The emergency gate was created through debug manipulation without the normal campaign condition.
- The opponent was not a valid nuclear major.

### Asset direction

A period command telephone held above a launch key or sealed order, with the line intact and the background under blackout conditions.

## Achievement implementation contract

Each achievement needs:

- Stable full ID in the root Chaos Redux achievement registry.
- Tracking flags and variables.
- Exact unlock trigger.
- Disqualifiers.
- Player and actor validation.
- Save and reload persistence.
- Localisation.
- Three achievement DDS states.
- Documentation.
- Any route, Event 5, moratorium, exchange, or custody hooks.
- Audit against exploits and debug-only completion.

Achievements should not unlock automatically from the event opening.

## Acceptance scenario A: Baseline opening

Setup:

- `SOV` exists.
- Chaos is between 200 and 399.
- Event 23 has not fired.
- No terminal world state.

Expected:

- Opening event fires once.
- Exactly 100 bombs are added.
- No free reactor entitlement is granted.
- One custody doctrine is selected.
- Readiness and Integrity initialize.
- Hidden Arsenal posture and Unknown knowledge begin.
- Event history records `SOV`.
- The event cannot fire again.

## Acceptance scenario B: Stronger pre-fire openings

Run separate clean cases at:

- 400 to 599 Chaos.
- 600 to 799 Chaos.
- 800 to 999 Chaos with the Evolution III world-state gate true.
- 1000 or more Chaos with the Evolution IV world-state gate true.

Expected:

- Cumulative bomb grants are 175, 275, 400, and 600.
- Cumulative reactor entitlements are 2, 4, 6, and 8.
- Reached evolutions record once and in order.
- Ineligible higher-stage behavior remains locked.
- No grant overwrites an existing stockpile.

## Acceptance scenario C: Incremental evolutions

Setup:

- Fire baseline at 200 to 399 Chaos.
- Progress through each later gate.

Expected:

- Incremental grants are 75, 100, 125, and 200 bombs.
- Reactor entitlements reconcile to the cumulative ladder.
- Each evolution uses active pacing and records once.
- The final totals match the corresponding pre-fire opening.

## Acceptance scenario D: Testing and secrecy

Cases:

- Clean concealed test.
- Public demonstration.
- Failed detonation.
- Premature accident.
- Foreign observation.
- Test canceled after the state becomes invalid.

Expected:

- One bomb is reserved and reconciled.
- Readiness, Integrity, exposure, public knowledge, deaths, contamination, and reports match the result.
- Shared consequences apply once.
- Public demonstration activates arms-race hooks without forcing another event.

## Acceptance scenario E: Coercion

Cases:

- Isolated losing minor accepts a limited demand.
- Guaranteed minor refuses and seeks support.
- Breakaway returns devices through negotiation.
- Strong target offers a partial settlement.
- Soviet backdown reduces credibility.

Expected:

- Target receives a real response window.
- Compliance follows campaign factors.
- No free annexation or subject creation occurs.
- Cooldowns and credibility memory persist.

## Acceptance scenario F: Limited strike

Setup:

- Evolution II active.
- Soviet Union at war with a nonnuclear target.
- Valid military or logistics state.
- Delivery, bomb, Readiness, and Integrity gates pass.

Expected:

- Bomb reserves at preliminary authorization.
- Target can respond and evacuate.
- Final authorization rechecks conditions.
- Shared strike adapter applies consequences once.
- Event 23 records command, credibility, and follow-up state without duplicate deaths or contamination.

## Acceptance scenario G: AI first-use boundary

Case 1:

- Chaos 800 to 999.
- Evolution III active.
- Soviet Union losing a war against a nuclear major.
- No enemy nuclear use.

Expected: Soviet AI major first use remains impossible.

Case 2:

- Chaos 1000 or more.
- Evolution IV active.
- Nuclear major enemy.
- Severe strategic loss.
- Valid target and delivery.
- No stand-down.

Expected: Soviet AI first use becomes possible but remains rare and profile-restrained.

Case 3:

- Same as Case 2, but a valid stand-down or settlement exists.

Expected: first-use weight is zero.

## Acceptance scenario H: Retaliation and exchange

Cases:

- Confirmed enemy nuclear strike.
- Suspected false warning.
- Limited reciprocal exchange.
- Exchange reaches General Exchange.
- Successful hotline and stand-down.

Expected:

- Retaliation windows are not instant.
- False warnings favor confirmation.
- First multi-major exchange fires the super-event once.
- The super-event remains nonterminal.
- Fallout activates only through the shared route.

## Acceptance scenario I: Soviet Collapse

Cases:

- Storage remains under Soviet control.
- One breakaway gains physical custody.
- Several breakaways gain devices.
- Joint custody settlement.
- Recovery raid.
- Technical denial.
- One breakaway completes operationalization.
- `SOV` ceases to exist.

Expected:

- Snapshot occurs before state transfer.
- Device totals reconcile.
- Physical custody does not grant instant launch.
- Operationalization uses all four stages.
- Soviet-only systems stop when `SOV` no longer exists.
- Local custody systems continue where valid.

## Acceptance scenario J: Disabled evolutions

For each evolution:

- Disable it before the gate.
- Reach the gate.
- Advance beyond normal MTTH.

Expected:

- No log entry.
- No grant.
- No posture or decision unlock.
- Baseline remains playable.
- Later content has a clean skip or remains correctly locked.

## Acceptance scenario K: Actor invalidity

Setup:

- `SOV` does not exist before event selection.

Expected:

- Event 23 shows `N/A` in the event list.
- It is not selected automatically.
- Manual launch reports the impossible host state.
- No substitute successor is selected.

## Acceptance scenario L: DLC and technology routes

Run the event with every supported nuclear delivery and special-project configuration identified in the current installed game.

Expected:

- The opening grants the minimum verified atomic capability needed for the event premise.
- No thermonuclear or missile capability is granted.
- At least one valid current-vanilla delivery route is supported.
- Missing optional DLC content does not create broken decisions or raw keys.
- No unverified fallback is used.

## Acceptance scenario M: Multiplayer

Cases:

- Human Soviet Union targets a human minor.
- Human Soviet Union targets a human nuclear major.
- Save and reload during a response mission.
- Soviet player tag switches and returns.

Expected:

- Target response remains available.
- Final authorization remains deliberate.
- No duplicate grant, response, or launch.
- Global exchange and shared consequences remain synchronized.

## Documentation closure

Before Event 23 can be called complete:

- Every accepted specification part is implemented or explicitly rejected with a reason.
- Every subagent handoff is reviewed.
- The event completion auditor compares the final repository against this package.
- Decision and mission audit is complete.
- Probability audit and post-patch comparison are complete.
- Localisation audit is complete.
- Assets are final and wired.
- Super-event quote, remark, image, audio, and slot are final and documented.
- Achievements are complete.
- Event 5 integration is documented.
- Shared nuclear adapter documentation is current.
- The authoritative workbook is updated and CSVs are regenerated.
- The event is added to the reworked-event default allowlist only after all required surfaces are ready.
- A Git commit contains only the completed Event 23 plan or implementation scope.

## Improvement-loop closure assessment

This specification already provides:

- A clear event promise.
- Two readable command values.
- A posture ladder.
- Testing, secrecy, production, coercion, targeting, limited use, exchange, and restraint.
- Soviet Collapse custody and successor logic.
- AI and probability scenarios.
- Presentation and asset direction.
- Achievements and acceptance cases.
- Cross-event and shared-system boundaries.

A further broad design expansion is not recommended before implementation. Additional mechanics would likely increase clutter and duplicate the shared nuclear, Fallout, event, and decision systems.

The improvement loop should resume only if implementation or audit reveals a concrete missing play loop, an invalid engine assumption, or a major accepted feature that cannot be represented through the current design.

## Simplification rule

Implementation may merge actions, reports, or asset variants only when the merged result preserves every accepted gameplay role, route distinction, AI behavior, consequence, and visible state.

Any omitted decision family, evolution behavior, collapse state, target response, achievement, asset, AI route, or shared-system connection must be reported as a simplification or blocker. It cannot be hidden inside a completion claim.
