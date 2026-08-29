# Asteroid Incoming, Part 10: Achievements and Acceptance

## Achievement design

Event 028 is a major event and needs a small set of difficult achievements. Achievements should reward distinct play patterns. They should not unlock because the event merely fired.

Every label below is a working label. Final names and descriptions require normal localisation work.

## Achievement 1: Preserve the Near Miss

### Play pattern

Choose the close-passage option while the event has reached its most dangerous evolved form.

### Conditions

- Event 028 fires at 800 Chaos or above.
- Global Fragmentation is enabled and eligible.
- Extraordinary Minerals is enabled and eligible.
- The chooser selects the miss.
- No impact transaction, fragment, dust, or crater is created.

### Disqualifiers

- Force-trigger or debug bypass when the achievement framework excludes them
- Any Event 028 impact already resolved in the campaign
- Evolution disabled before selection

### Difficulty purpose

The player refuses a powerful destructive option and all possible crater material at high Chaos.

### Icon direction

A bright object passing above Earth, a telescope silhouette, and a narrow gap. The completed icon should communicate avoided contact without treating destruction as victory.

## Achievement 2: Government Beyond the Crater

### Play pattern

Remain as the original target country after the capital state is destroyed, relocate government, and complete national recovery.

### Conditions

- The player's country is the locked main target.
- The main impact destroys its capital state.
- The country survives without changing to another tag through annexation or release.
- It completes the national network and outer-ring recovery objectives within a defined deadline.
- It still controls its replacement capital at completion.

### Disqualifiers

- The country was not the original intended target.
- The capital moved before trajectory lock.
- Another country completed the recovery after annexation.

### Difficulty purpose

The achievement tests survival, logistics, and reconstruction after the most disruptive target profile.

### Icon direction

A government building or flagless civic structure standing beyond a crater horizon, with rail and communication lines restored.

## Achievement 3: Collector of Fallen Stars

### Play pattern

Control the main crater and several fragment sites at the same time.

### Conditions

- Extraordinary Minerals is active.
- The player directly controls the main crater.
- The player directly controls at least three fragment crater states.
- Subject control does not count.
- All sites remain controlled for a continuous verification period, such as 180 days.

### Disqualifiers

- Temporary occupation without sustained control
- Counting the same site more than once
- Controller switching that breaks the continuous period

### Difficulty purpose

The player must fight or negotiate across several regions to assemble a large uncapped armour advantage.

### Icon direction

One large meteoric fragment surrounded by three smaller fragments above an armored plate or shield. Avoid fantasy gemstones.

## Achievement 4: Piercing the Impossible

### Play pattern

Defeat a country benefiting from the main crater's plus 100 percent armour modifier and take the crater state.

### Conditions

- Extraordinary Minerals is active.
- An enemy country controls the main crater and has the main-crater armour modifier.
- The player is at war with that controller.
- The player takes control of the main crater.
- The player holds it for a defined period.
- The enemy loses the main-crater modifier through the same control change.

### Disqualifiers

- Peaceful transfer, console transfer, or subject integration when the achievement requires conquest
- Capturing a fragment site instead of the main crater
- The enemy did not have the active modifier

### Difficulty purpose

The player overcomes the strongest mineral advantage and proves that crater control can change hands through war.

### Icon direction

A fractured armored plate struck by a narrow spear or shell, with crater texture behind it.

## Achievement 5: A World Reconnected

### Play pattern

Lead a high-dust recovery without owning the original target.

### Conditions

- The player is not the original main target.
- Opening Dust Load reaches Impact Winter or Severe Impact Winter.
- The player reaches the highest national protection state.
- The player completes the atmospheric observation contribution and transport-protection actions.
- Global dust later reaches zero while the player remains active and has not abandoned the protection program.

### Difficulty purpose

The player responds to a global environmental crisis and does not exploit the impact directly.

### Icon direction

A globe crossed by restored rail, shipping, and observation lines under a clearing sky. Keep the design compact and period appropriate.

## Achievement tracking rules

- Tracking must use stable event, target, crater, controller, and recovery records.
- The achievement system should distinguish intended target from current crater controller.
- Direct control and subject control must use the stated rule for each achievement.
- Continuous-hold achievements need a reset when control is lost.
- Save and reload must preserve progress.
- Debug and force-trigger disqualifiers should follow the current project achievement policy.
- Achievement conditions must not depend on a transient event target that disappears after the chain.
- Every achievement needs completed, grey, and not-eligible icons and matching localisation.

## End-to-end acceptance criteria

### Event identity and selection

- Event 028 is registered as a major fire-once event.
- Baseline availability begins at Calm World.
- The event remains unavailable and shows `N/A` when three valid target pairs cannot be built.
- The chooser sees exactly three distinct country and state targets plus miss.
- Canceling confirmation does not reroll.
- Impact and miss both consume the major event and reset shared major pacing.

### Target and trajectory

- Each target option shows the locked country, state, and region.
- The selected state remains fixed through ownership and control changes.
- Impact resolves after two game days.
- A capital hit relocates the capital to a valid backup.
- The target receives one preparedness choice.
- Multiplayer produces one chooser and no duplicate global transactions.

### Damage and Deaths

- Main center loses all population and all buildings.
- Main Ring 1, Ring 2, and Ring 3 apply the required population percentages.
- Damage follows shortest land adjacency across borders.
- Each state receives one strongest profile.
- Civilian losses equal the actual state population removed.
- Deaths reasons identify main, ring, fragment, and rescue sources.
- Country reports are consolidated.
- Main crater remains permanent and nonradioactive.

### Dust

- Every main impact creates Dust Load.
- Miss creates no dust.
- Opening load uses actual destruction and fragment outcomes.
- Dust produces visible stages and global production, supply, weather, and Air Cleanliness effects.
- Dust decays and closes cleanly.
- National mitigation works without instantly clearing the global state.
- Event 013 links are bounded, supported, and do not duplicate the main event.

### Evolutions

- Global Fragmentation applies at 600 Chaos when enabled.
- Actual fragment count follows valid geography and reports the real count.
- Fragment damage uses 50, 25, and 5 percent population profiles.
- Extraordinary Minerals applies at 800 Chaos when both evolutions are active.
- Main crater grants plus 100 percent existing land armour to its controller.
- Each fragment site grants plus 20 percent existing land armour.
- Bonuses transfer and stack without stale duplicates.
- Miss records no evolution.

### Nuclear separation

- Visual effects play correctly.
- No nuclear or thermonuclear history is recorded.
- No nuclear condemnation, retaliation, radioactive fallout, or nuclear-use Chaos entry occurs.
- Dust appears as an asteroid environmental source.

### Decisions and AI

- Decision phases expose no more than the planned visible action cap.
- Costs use no more than four spendable types and use correct icons.
- Decisions target exact states and show blocked reasons.
- AI can use every important response path.
- Probability scenarios preserve protected relationships and strong miss preference for ordinary peaceful AI.
- Crater AI values sites without abandoning normal survival logic.

### Presentation

- Entry, target emergency, reports, news, Event Details, evolution views, and super-event use finished localisation.
- Dynamic names and flags survive target annexation or cosmetic changes.
- Main super-event image, unique licensed music, quote, and button remark are aligned.
- All required DDS files and sprite wiring are complete.
- No placeholder art, default audio, raw localisation key, or temporary working label appears in game.

### Documentation and catalog

- Event docs describe the final implementation.
- The authoritative workbook row replaces the stale Event 28 entry.
- Evolution detail fields match Event Details wording.
- CSV exports are regenerated from the workbook.
- Event status remains disabled by default until implementation, assets, AI, docs, and audits are complete.

## Required validation scenarios

1. Baseline main impact at low Chaos.
2. Miss at low Chaos.
3. Fragmentation at 600 to 699 Chaos.
4. Fragmentation plus minerals at 800 to 899 Chaos.
5. Six-fragment plan at 900 to 999 Chaos with reduced valid pool.
6. Capital impact and backup relocation.
7. Cross-border ring affecting at least three countries.
8. Target annexed during the two-day delay.
9. Main and fragment outer-ring overlap.
10. Main crater changes controller through war.
11. Fragment state changes controller through peace.
12. Save and reload during target lock.
13. Save and reload during severe dust.
14. Event shows `N/A` in an invalid late-game world.
15. Nuclear systems remain unchanged after every impact visual.
16. Achievement tracking survives reload and resets continuous control correctly.

## Completion standard

The event is incomplete when any required target path, damage ring, report, dust stage, evolution, decision phase, AI behavior, asset, super-event component, achievement, log surface, document, or catalog field is missing. A smaller fallback must be reported and approved before it can replace the accepted design.
