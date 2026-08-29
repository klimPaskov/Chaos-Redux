# Great Depression 2.0 specification, part 11: Achievements, acceptance scenarios, and completion standard

## Achievement role

Event 35 achievements should reward national recovery, center reopening, prevention of evolved spread, survival of Social Collapse, difficult liquidation, and resolution of the worldwide crisis. They must use stable episode receipts and clear disqualifiers.

Event 34 owns the cross-event Evolution III crash-and-recovery achievement through its accepted `The Long Fall` contract. Event 35 supplies the recovery receipts that contract needs and does not create a duplicate inherited-crash achievement.

The labels below are working labels. Final names and descriptions need implementation writing and icon review.

## Achievement 1: Back to Work

### Mastery goal

Recover from a severe independent Event 35 episode while preserving every original Depression Center and losing no civilian or military factory level through Event 35.

### Required conditions

- Player country enters Event 35 through an independent firing.
- Starting Severity meets the final severe minimum.
- The opening Depression Center registry is frozen for the achievement.
- Every original center reaches Recovered or another approved positive restructured state.
- No original center is abandoned.
- No Event 35 factory-loss receipt is recorded.
- Recovery proof completes for the same player-owned episode.

### Disqualifiers

- Event 34 inherited source.
- Any Event 35 factory-loss receipt.
- Deliberate center abandonment or liquidation.
- State transfer, annexation, puppeting, or tag switching used to remove a failing center from the requirement.
- Debug, force completion, or achievement tracking that begins after the opening snapshot.

### Tracking

Freeze the original center IDs and their civilian and military factory levels at the accepted opening transaction. Ordinary combat damage does not disqualify the achievement unless Event 35 records the loss as its own consequence. The achievement evaluates during recovery completion before active episode data is cleared.

### Icon direction

An open factory gate with workers returning and every industrial building still intact.

## Achievement 2: Every Center Reopened

### Mastery goal

Reach Economic Paralysis and recover every Depression Center without abandoning one.

### Required conditions

- Peak Severity reaches `100`.
- The country survives the maximum-Severity emergency.
- The episode contains at least three centers, or every valid center available to a smaller economy.
- Every registered center reaches Recovered or an approved positive restructured state.
- Final national result is Strong or Uneven Recovery.

### Disqualifiers

- Any center ends Abandoned, Shuttered, unresolved, or invalidly removed from the ledger.
- A center is liquidated as the final solution.
- Recovery closes through debug or forced cleanup.
- State transfer is used to bypass a center requirement.

### Tracking

Use the episode center registry, highest Severity receipt, maximum-emergency completion, and final center-state counts. A later valid center addition becomes part of the requirement once registered.

### Icon direction

Several industrial bays or workshops with their lights restored, shown as one readable district.

## Achievement 3: Containment Line

### Mastery goal

Contain material Financial Contagion without allowing any foreign country materially exposed by the player's source crisis to convert into a full Event 35 crisis.

### Required conditions

- Financial Contagion is active in the player's source episode.
- Source Severity reaches the final deep-contraction threshold.
- At least the required number of valid foreign countries reaches Observed Exposure or a stronger stage, scaled for the valid pool.
- At least one aid, ring-fence, clearing, diversification, or coordinated-rescue action completes.
- No attributable foreign full-crisis conversion occurs.
- All outgoing source links resolve as Contained or through source recovery.
- The source country recovers.

### Disqualifiers

- A foreign conversion materially attributed to the player's source episode.
- Deleting, annexing, or invalidly cleaning an exposed country to remove the link.
- Disabling the evolution after exposure begins.
- Debug or force cleanup.
- Loss of source-country ownership.

### Tracking

Multi-source exposure needs attribution. A conversion disqualifies the achievement when the player source was a material dominant or secondary contributor. An unrelated source does not disqualify it unless the player's exposure record crossed the final contribution threshold.

### Icon direction

A chain of banks, factories, and freight links stopped by a clear economic firebreak. Avoid disease imagery.

## Achievement 4: The Social Peace

### Mastery goal

Recover from Social Collapse after near-maximum Severity without a successful coup, Event 35 civil conflict, or permanent emergency rule.

### Required conditions

- Social Collapse is active.
- Peak Severity reaches at least `90`.
- At least one major strike, occupation, riot, mutiny, or government crisis occurs.
- The final social settlement or peace objective succeeds.
- No successful coup receipt exists.
- No Event 35 civil-conflict receipt exists.
- Emergency rule is absent at recovery completion.
- Stability meets the final tuned floor.

### Disqualifiers

- A permanent military or emergency government created by the crisis.
- Successful coup, separatist conflict, or Event 35 civil conflict.
- Debug incident clearing.
- Crisis ownership moved to another country.

### Tracking

Track major Social Collapse incident families, response outcomes, coup and civil-conflict receipts, emergency-government lifecycle, final settlement, stability, and recovery ownership. A baseline strike before Evolution II can count as history but cannot satisfy the required Social Collapse incident by itself.

### Icon direction

A reopened factory after a negotiated settlement, with workers and guards withdrawn from confrontation. Do not include readable document text.

## Achievement 5: Lean but Standing

### Mastery goal

Complete a liquidation-led recovery after accepting real Event 35 industrial loss while retaining national viability and avoiding political collapse.

### Required conditions

- Let the Market Clear or an approved liquidation-led route remains the final recovery philosophy.
- At least one center is consolidated, auctioned, or deliberately resolved through that route.
- At least one exact civilian or military factory level is lost through a validated Event 35 liquidation transaction.
- The country retains the protected industrial floor.
- No successful coup, separatist conflict, or Event 35 civil conflict occurs.
- Recovery proof succeeds for the same episode.

### Disqualifiers

- All industrial loss came from war, bombing, disaster, occupation, or another event.
- No real Event 35 industrial loss occurred.
- Doctrine switching or later program history removes liquidation-route ownership.
- Country falls below the protected viability floor.
- Debug completion.

### Tracking

Record the exact state, building type, amount, liquidation receipt, route ownership, national industrial floor, political-collapse receipts, and final recovery result. Final localisation should present survival after a harsh choice and should not praise unemployment or suffering.

### Icon direction

One surviving active plant beside closed capacity, with clear repair and continued production rather than triumphal imagery.

## Achievement 6: Recovery of Nations

### Mastery goal

Lead or materially support international recovery during The Second Great Depression while preserving the player's own national stability.

### Required conditions

- The Second Great Depression is active.
- The player performs a substantial validated set of aid, clearing, reconstruction, coordinated-demand, or supplier actions.
- At least one major recipient improves through the player's support.
- The player either recovers from Event 35 or remains below national conversion throughout the episode.
- The worldwide lifecycle reaches International Reconstruction.
- Final global recovery proof completes.
- No major Event 34 supplier collapse occurs during the final global proof period.
- The player country remains independent and valid.

### Disqualifiers

- Contribution transactions are refunded, duplicated, or registered after global recovery was already secured.
- The player triggers a critical supplier collapse during the final proof.
- The global episode is force-ended.
- The player is deleted, changes tags without valid continuity, or is a special actor outside normal civilian-system coverage.

### Tracking

Use the global episode ID, contribution receipts, major-recipient improvement receipts, player national state, final-stage entry date, supplier-collapse proof period, and recovery completion transaction. Current modifiers alone are not enough.

### Icon direction

Freight, port, rail, and factory activity returning across linked countries without a world-map graphic or handshake.

## Achievement implementation rules

Every achievement requires:

- Stable achievement ID.
- Game-rule and eligibility checks consistent with current Chaos Redux achievements.
- Episode receipts.
- Positive trigger.
- Disqualifiers.
- Save persistence.
- Final name and description.
- Icon triplet.
- Documentation.
- Test cases for positive and negative routes.

Do not implement achievements as a final-event option that fires automatically without verifying the whole episode.

## Acceptance scenario groups

The implementation is complete only after every applicable scenario below is tested through source inspection, HOI4 MCP evidence where supported, and the project's final user-run in-game validation path. This planning package does not claim that live testing has occurred.

## A. Targeting and entry

### `A-01`: Independent major target

- Several valid majors exist.
- Event 35 is selected automatically or through normal manual event firing.
- One exact major is chosen.
- One history row is recorded.
- Opening report, shock, category, Severity, phase, doctrine choice, and centers appear once.

### `A-02`: Player non-major target

- Player country is not a major.
- It remains eligible.
- Costs and center count scale to the smaller economy.
- The crisis remains severe and recoverable.

### `A-03`: Active Event 35 exclusion

- One country has Event 35 active.
- Independent target selection gives it zero eligibility.
- A consequence call deepens the existing crisis instead of creating a duplicate.

### `A-04`: Active Event 34 exclusion

- One country has Industrial Boom active.
- It cannot receive independent Event 35.
- Lighter contagion or global pressure uses Event 34 adapters.

### `A-05`: No valid target

- No major or player country passes normal civilian and industrial gates.
- Event list shows unavailable.
- No random country call or empty actor history is created.

### `A-06`: Negative Economy cluster actor

- Event 35 is selected as cluster anchor.
- Cluster uses one exact actor.
- Event 35 does not reroll another country.
- One global pacing event is counted.

## B. Opening and Severity

### `B-01`: Independent opening range

- Stable target begins in the intended severe but recoverable range.
- Opening shock is stronger than sustained penalties.
- No factory is deleted.

### `B-02`: Vulnerable opening

- Blockaded, unstable target with damaged industry begins higher.
- The cause list names material problems.
- Emergency actions remain payable.

### `B-03`: Dynamic drift cadence

- Panic and Economic Paralysis use a shorter bounded interval than Stabilization.
- Several normalized pulses under worsening conditions increase Severity gradually.
- Several normalized pulses under strong recovery lower it gradually.
- One ordinary pulse cannot resolve the entire crisis.
- Rescheduling never creates two active pulse receipts for one episode.

### `B-04`: Trend

- Rapid improvement, improvement, stable, worsening, and accelerating conditions are reproduced.
- Trend follows recent movement and shock memory.
- Save and load preserve correct trend history.

### `B-05`: Threshold crossings

- Every band changes intended modifiers and action availability.
- Crossing a threshold does not repeat its one-shot incident each pulse.
- Falling thresholds updates the category and phase proof correctly.

### `B-06`: Economic Paralysis

- Severity reaches `100`.
- Deepest modifier and emergency objective appear once.
- Country retains a viable emergency action path.
- Remaining at `100` does not repeat factory loss or aid.

### `B-07`: Relapse

- Country enters Stabilization.
- A new shock returns Severity to the Depression range.
- Stabilization proof resets.
- Opening shock does not reapply without a new source.

### `B-08`: Baseline political pressure

- Evolution II is disabled.
- Sustained Deep Depression creates an ordinary strike, radicalization event, or government crisis through valid conditions.
- No Evolution II movement registry or occupation system appears.

### `B-09`: Baseline National Breakdown

- Evolution II is disabled.
- Full National Breakdown conditions and a failed prevention objective make civil conflict a bounded possibility.
- Missing actor, territory, force, leader, or recent-war proof forces a nonwar political outcome.
- The event does not clone the national crisis onto every participant.

## C. Recovery doctrines

Run separate checkpoints for every doctrine.

### `C-01`: Emergency Public Works

- Major project consumes real resources.
- State and employment conditions improve.
- Interruption preserves valid partial work and prevents refund duplication.
- Final legacy reflects completed projects.

### `C-02`: Rescue Strategic Industry

- Vital center receives protection.
- Nonprotected sectors bear visible cost.
- Military output is preserved without free equipment.
- Rescue dependence can appear.

### `C-03`: Stabilize Finance and Trade

- Bank holiday and audit sequence works.
- Trade action requires valid routes and partners.
- Blockade makes inappropriate actions invalid.
- Durable credit reform requires completed prerequisites.

### `C-04`: Austerity and Retrenchment

- Fiscal pressure falls.
- Demand and social pressure rise.
- Route can succeed under strong conditions.
- Route carries severe Social Collapse risk under weak conditions.

### `C-05`: Direct State Planning

- Planning board opens coordinated actions.
- Nationalization or trusteeship targets exact center.
- Input rationing protects one sector and creates a cost elsewhere.
- Plan completion creates one bounded institution.

### `C-06`: Let the Market Clear

- Support withdrawal produces real short-term risk.
- Asset reorganization can succeed, partially succeed, or liquidate capacity.
- No repeated auction reward.
- Route remains viable only under suitable conditions.

### `C-07`: Doctrine switch

- Switch unavailable before cooldown.
- Switch pays real cost and creates policy whiplash.
- Completed action receipts persist.
- Repeated switching cannot farm rewards.

### `C-08`: Objective capacity

- No more than one main objective and two supporting missions appear.
- Economic Paralysis replaces ordinary missions.
- Obsolete actions hide.

## D. Depression Centers

### `D-01`: Small economy center count

- One meaningful state is selected.
- Costs and project duration scale correctly.

### `D-02`: Large major center count

- Two or three distinct high-value centers are selected.
- Selection does not default to capital-only or duplicate region.

### `D-03`: Local progression

- Distressed center can become Idled and Shuttered only after sustained pressure.
- Warning or objective appears before serious physical loss.

### `D-04`: Reopening

- Doctrine-specific project and supply requirements work.
- Reopened state lowers national pressure.
- No free building restoration occurs.

### `D-05`: State loss

- Active project pauses.
- National shock scales with industrial importance.
- Previous owner stops paying.
- New controller cannot duplicate reward.

### `D-06`: State regain

- Existing project and damage reconcile.
- Lost combat buildings do not return for free.

### `D-07`: Permanent transfer

- One live state record owner.
- Historical loss remains with original episode.
- New owner can adopt local burden through valid contract.

### `D-08`: Involuntary physical loss

- Requires Shuttered or Abandoned state, sustained exposure, failed recovery opportunity, and unused receipt.
- Per-state and per-episode caps hold.

### `D-09`: Deliberate liquidation

- Player receives short-term relief and permanent scar.
- Liquidated factory cannot be restored and rewarded in the same episode.

## E. Event 34 inheritance

### `E-01`: Baseline boom collapse

- Frozen snapshot accepted.
- Same country enters baseline Event 35.
- Boom bonuses are removed before depression penalties.
- Starting Severity reflects reserves and landing preparation.

### `E-02`: Evolution I collapse

- Financial Contagion activates when enabled.
- Speculative regions convert correctly.
- Disabled Financial Contagion remains off while severity inheritance remains.

### `E-03`: Evolution II collapse

- Enabled Evolutions I and II activate.
- Fragile Miracle Regions convert.
- Social Collapse module is ready without duplicate evolution records.

### `E-04`: Evolution III collapse

- Enabled Evolutions I, II, and III activate.
- Starting Severity is very high.
- Global episode starts or deepens once.
- Super-event receipt fires once on actual worldwide pressure.

### `E-05`: Existing Event 35

- Event 34 collapse deepens the same episode.
- Category, base modifier, and center registry are not duplicated.
- Evolution floor only rises.

### `E-06`: Duplicate transaction

- Second call with same collapse ID rejects safely.
- No duplicate shock, center, or history.

### `E-07`: Interrupted handoff

- Frozen snapshot remains recoverable.
- Boom actions stay closed after terminal collapse.
- Repair or cleanup does not leave mixed active modifiers.

### `E-08`: Deleted target

- Invalid target fails closed.
- Source registry cleans without creating a random replacement.

## F. Financial Contagion

### `F-01`: Exposure registry

- Strong, medium, and light relationships create one merged row per source-target pair.
- Invalid special actors are excluded.

### `F-02`: Secondary condition

- Exposed country receives qualitative pressure and compact actions.
- It does not receive the full Event 35 category immediately.

### `F-03`: Aid

- Provider pays exact resources.
- Origin Severity or exposure changes once.
- Refund and cancellation are symmetric.

### `F-04`: Abandonment

- Relationship closes.
- Origin receives one shock.
- Diplomatic and investment consequences apply.
- No repeated abandonment.

### `F-05`: Full conversion

- Vulnerable target converts after sustained Near Depression.
- Entry source, origin, depth, and episode are recorded.
- No random pacing event is counted.

### `F-06`: Anti-loop

- Origin cannot receive immediate return shock through the same link.
- Depth reduces pressure.
- One target converts once per origin episode.

### `F-07`: Origin recovery

- New exposure stops.
- Lighter conditions decay.
- Already converted countries remain active independently.

### `F-08`: Disabled evolution

- No new exposure or conversion.
- Cleanup does not grant rewards or alter baseline recovery.

## G. Social Collapse

### `G-01`: Organized protest

- Prolonged unemployment creates one valid movement.
- Country-specific political context shapes it.
- Player receives a bounded response set.

### `G-02`: Negotiated settlement

- Costs and concessions apply.
- Strike or occupation ends.
- Social condition improves.
- Durable settlement is recorded.

### `G-03`: Force response

- Command power remains within project limit.
- Equipment and manpower costs apply.
- Exact deaths use shared API.
- Repression can worsen later strain.

### `G-04`: Emergency government

- Correct government form is selected from valid institutions.
- Mandate mission opens.
- It returns power, becomes permanent through visible route, or fails.

### `G-05`: Coup without regional base

- Valid elite or military actor exists.
- Coup can occur.
- Civil war remains ineligible without territory.

### `G-06`: Separatist route

- Valid regional identity and package exist.
- Territory and force setup are coherent.
- If package is absent, autonomy or regional crisis replaces country creation.

### `G-07`: Civil war gate

- All extreme conditions are satisfied.
- Territory follows support and centers.
- Full national crisis is not cloned onto every participant.
- Shared war and death Chaos is not duplicated.

### `G-08`: Recent civil war block

- New Event 35 civil conflict has zero eligibility.
- Recovery and settlement remain available.

### `G-09`: Disabled evolution

- No Evolution II movement ladder, factory-occupation system, coup route, separatist conflict, or movement-specific civil war appears.
- Baseline strikes, radicalization, government crises, and the guarded National Breakdown chain remain functional.
- A baseline civil conflict still requires the full baseline gate and failed prevention objective.

## H. The Second Great Depression

### `H-01`: First global activation

- One global episode ID.
- One bounded world registration.
- One actual pressure package.
- One super-event receipt.
- One guarded Chaos source.

### `H-02`: Lighter pressure

- Stable country receives Global Contraction.
- Full Event 35 category does not open.
- Condition scales with exposure.

### `H-03`: Local conversion

- Highly exposed country converts.
- Stable self-sufficient country remains lighter.
- Entry source and global episode are recorded.

### `H-04`: Supplier boom

- Active Event 34 country receives world orders.
- Benefits and Overheating both change.
- AI and player can refuse further exposure.

### `H-05`: Supplier collapse

- Supplier enters or deepens Event 35.
- Dependent countries receive exact shocks.
- World stage deepens once.

### `H-06`: Global recovery

- Industrially weighted recovery advances stage.
- Final proof lasts required period.
- New major crisis pauses or resets proof.

### `H-07`: Global resolution

- Lighter pressure decays.
- Active national depressions remain.
- International agreements with a post-crisis role persist.
- Matching Chaos reversal is capped by recorded source.

### `H-08`: Existing global episode

- New Evolution III origin joins or deepens it.
- No second world registry or super-event.

### `H-09`: Disabled evolution

- No global pressure, super-event, or worldwide conversion.
- Inherited national severity remains valid.

## I. Repeatability and country changes

### `I-01`: Strong reform repeat

- Country recovers strongly.
- Safeguard blocks early independent refiring.
- Later episode starts with bounded reform benefit.

### `I-02`: Hollow recovery repeat

- Country retains scars.
- Later vulnerability rises within cap.
- Recovery remains possible.

### `I-03`: Civil war during active crisis

- One national episode owner remains.
- Center burdens divide by control.
- No duplicate categories across every small side.

### `I-04`: Annexation

- Active country cleanup removes arrays, decisions, exposure, and missions.
- No replacement target inherits the whole crisis at random.

### `I-05`: Release or successor

- A valid successor adopts local burden only through explicit state and country contract.
- History remains with original episode.

### `I-06`: Save and reload

- Severity, phase, trend, doctrine, centers, evolutions, exposure, world stage, missions, and receipts persist.
- Opening shock and threshold events do not repeat.

## J. Cluster, logs, and presentation

### `J-01`: Event list

- Event ID, name, type, Chaos level, and availability display correctly.
- No valid target shows `N/A`.

### `J-02`: Event history

- Independent firing has one pacing history row.
- Event 34, contagion, and global consequence entries do not create extra pacing events.
- Source remains visible in Event 35 details.

### `J-03`: Evolution history

- Each enabled evolution logs once with actor, date, tier, and stage.
- Disabled evolution does not set recorded flags.
- Event Details preview has no fake history date.

### `J-04`: Negative Economy cluster

- Low danger appears after cluster registry completion.
- Optional participation and selected-anchor behavior match part 8.
- Cluster counts one pacing event.

### `J-05`: Category clarity

- Player can identify Severity, trend, phase, doctrine, next threshold, center, and action without reading a long paragraph.
- Visible action and mission caps hold.

### `J-06`: Assets

- Every required asset has source, processed PNG, final DDS, sprite, consumer, manifest, and handoff.
- No placeholder, white halo, opaque icon square, modern prop, or wrong-era scene remains.

### `J-07`: Super-event

- Slot, title, description, reaction, quote, image, audio, settings-aware playback, docs, and workbook agree.
- Quote and audio rights are verified.
- No default or reused unapproved track.

### `J-08`: Writing

- No raw keys or implementation text.
- No hidden formulas or future spoilers.
- Dynamic countries and states resolve.
- Visible costs and requirements are clear.
- Project writing rules are followed.

## K. AI and probability

### `K-01`: Target scenarios

Run `TGT-01` through `TGT-10` with complete pools.

### `K-02`: Doctrine scenarios

Run `DOC-01` through `DOC-07` and confirm expected ordering.

### `K-03`: Action scenarios

Run `ACT-01` through `ACT-05`.

### `K-04`: Contagion scenarios

Run `CTG-01` through `CTG-10`.

### `K-05`: Baseline breakdown scenarios

Run `BDP-01` through `BDP-04` and confirm the baseline route remains compact, guarded, and distinct from Evolution II.

### `K-06`: Social scenarios

Run `SOC-01` through `SOC-05`.

### `K-07`: Global scenarios

Run `GLB-01` through `GLB-10`.

### `K-08`: Evolution timing

Run `EVO-01` through `EVO-08` with scheduled state changes.

### `K-09`: Incident pools

Inspect complete candidate pools in every Severity band and evolution state. Confirm no invalid incident receives weight and no generic incident dominates every context.

## L. Achievement tests

Every achievement needs:

- One positive scenario.
- One near-miss.
- One exploit attempt.
- One save and reload case.
- One disqualifier case.

No achievement should unlock from debug or manual force paths unless the project's existing achievement framework explicitly permits it.

## Completion evidence

Before Event 35 is called implemented, the final report must include:

- Files changed.
- Event IDs and new subevents.
- Scripted effects, triggers, constants, variables, flags, arrays, and event targets.
- Crisis API contract and rejection reasons.
- Event 34 snapshot version and field coverage.
- Decision and mission coverage.
- Doctrine route coverage.
- Depression Center lifecycle coverage.
- Evolution coverage.
- AI and probability comparison evidence.
- Cluster registry and workbook alignment.
- Chaos source and reversal receipts.
- Asset inventory and final runtime paths.
- Super-event research and wiring.
- Achievement coverage.
- Event log and Event Details coverage.
- Documentation and authoritative workbook updates.
- Accepted improvement addendum disposition.
- Task-specific validation findings.
- Every blocker, simplification, omission, fallback, substitution, or unimplemented requirement.

## Improvement-loop conclusion

The project custom-subagent runtime was unavailable, so `chaosx_improvement_loop_planner` could not be executed. Its supplied role definition was applied manually to the assembled package as a final depth and anti-bloat review.

The manual result is closure. The six recovery philosophies, Depression Centers, guarded baseline National Breakdown, Financial Contagion, Social Collapse, The Second Great Depression, the Event 34 handoff, AI scenarios, assets, achievements, and acceptance cases form a complete implementation target. Another broad planning expansion before implementation would add bloat.

The next executable improvement-loop pass belongs after a meaningful implementation tranche, when actual decisions, state logic, and evolutions can be compared with the design. That pass should either produce a bounded addendum for a concrete implemented weakness or recommend closure when the event is connected, readable, replayable, and complete.

It should not add another public meter, a full focus tree, automatic custom countries, 3D models, a permanent scripted GUI, or extra global systems without a new accepted gameplay need.

## Planning completion statement

The planning package is complete when all files in the manifest exist, cross-references resolve, the consolidated specification includes every part, and the package passes the content audits. Planning completion does not claim gameplay implementation, final assets, subagent execution, HOI4 MCP evidence, workbook changes, or live game validation.
