# Law Upgrade
## Part 10. Achievements and acceptance

## Achievement design

The event has three proposed achievements. Their identities and conditions below are planning records, not final localized titles or claims that they are already registered.

They must be integrated into the project's single canonical achievement owner. No separate Event 82 achievement system, popup framework, or alternate award file is created.

Each achievement must be available without requiring a DLC-specific country mechanic. The conditions concern real campaign outcomes rather than opening a report, receiving the global event, or merely purchasing a law.

## Achievement A: Endure the extreme mobilization

**Proposed identity: `law_upgrade_endure_extremes`.**

The player-controlled country holds both extreme laws for 90 consecutive game days while fighting a defensive war against at least one major country. It then wins that qualifying war without having capitulated during the qualifying interval or before the victory.

The country must genuinely be a defending participant. A declaration initiated by the player followed by joining another defensive conflict does not transform the original war into a qualifying one.

The two laws must be held continuously throughout the 90-day period. A valid law exit breaks that period. A temporary lack of a qualifying defensive enemy also breaks it.

After the 90-day qualification is complete, the country may demobilize and still pursue victory. The achievement should reward enduring and surviving the emergency, not force the player to keep destructive laws indefinitely after the qualifying feat.

Victory means the qualifying major opponent or opponents are defeated in the war's resolved outcome. A white peace is not victory. The implementation must bind this meaning to the existing verified war-result evidence rather than guessing from the mere absence of war.

Visual subject direction: an exhausted but intact industrial and military command surviving an overwhelming mobilization order.

## Achievement B: Recover the workforce without abandoning the war economy

**Proposed identity: `law_upgrade_restore_workforce`.**

The player-controlled country holds both extreme laws during a real war and has a weighted deployed-army equipment deficit of at least 20%. It pays to reverse Totalen Menschen!!! while retaining Totalen Krieg!!!.

After that reversal, while remaining at war and keeping the economy extreme, it reaches at least 95% weighted equipment fulfillment across its deployed land forces and maintains that condition for 30 consecutive game days.

Throughout the qualifying recovery, it retains at least 75% of the deployed land-force manpower recorded at the reversal. This prevents completing the achievement simply by deleting most of the army.

Weight equipment fulfillment by documented production-cost or equivalent owning-system weights rather than treating a rifle and a tank as interchangeable units. The exact data provider must be verified before implementation. Zero requirements cannot qualify.

A return to the conscription extreme, departure from the economy extreme, peace, insufficient retained deployed manpower, or a fall below the fulfillment threshold interrupts the recovery period.

Visual subject direction: civilian tools returning to a still-operating war factory while the recruitment apparatus is dismantled.

## Achievement C: Return the country to civilian life

**Proposed identity: `law_upgrade_restore_civilian_life`.**

The player-controlled country has genuinely held both extreme laws and has paid for the manual reversal of each one. The two payments need not occur together or in a particular order.

It then reaches peace, an economy law at or below Partial Mobilization, a conscription law at or below Limited Conscription, Stability of at least 60%, and control of its own capital. It maintains all those conditions for 90 consecutive game days.

A forced removal by another event does not replace the required history of a paid manual reversal. A zero-price ordinary transaction remains a valid manual reversal if the nation's legitimate current ordinary law cost was zero.

The qualifying history persists across legitimate later law changes. The 90-day civilian-life interval restarts whenever its current conditions fail.

Visual subject direction: a restored civilian workshop and ordinary administrative life after an extreme mobilization notice has been withdrawn.

## Common achievement integrity

The three achievements track the player's actual country and the relevant real historical outcomes. A tag change does not grant another country's history, and a save reload does not reset a completed qualification into a new award.

Testing, console-forced awards, synthetic fixtures, and development bypasses must not produce normal campaign achievements.

An achievement is awarded once through the canonical owner. Its visible progress and awarded state must agree.

The full asset prompt defines the common three-state production route. The achievement prompt defines the registry, persistent-state, and evidence requirements.

## Core acceptance

A passing implementation must preserve the following invariant: one global firing applies one profile, grants its War Support once, and advances each participating category by at most one real adjacent step.

The baseline, three evolution thresholds, names, 99% settings, and doubled manual reversals are fixed user requirements. They are not optional balance proposals.

The detailed penalty tables, nominal MTTH inputs, AI priorities, voluntary-entry gates, achievements, and bounded Chaos milestones are proposed expansions. They require implementation evidence and live balance review, with any deliberate revision documented rather than silently substituted.

## Required evidence families

The acceptance matrix contains named cases for:

1. Baseline and evolved progression, caps, structural gates, and simultaneous recipient treatment.
2. Exact extreme-law entry, legal economic and population settings, current-support scaling, and combined penalties.
3. Manual reversal, all relevant discounts and rounding, failed transactions, re-entry, and save integrity.
4. Compatibility, new and destroyed countries, civil wars, country transformations, and old-save migration.
5. Evolution timing, enabled dependencies, AI candidate-pool behavior, achievements, assets, and readable presentation.

The fixture set must cover different starting law positions rather than testing only a country already at both normal maximums.

## Release blockers

An implementation is not complete while it lacks a proven engine mapping for the intended economic allocation, 99% recruitment and ceiling behavior, real current adjacent law prices, current-support updates, or supported law-owner compatibility.

The package's arithmetic reference checks are not HOI4 playtests. No parser success, source search, or matching tooltip alone proves a country's actual output, population pool, paid price, or save behavior.

The mandatory isolated improvement review and specialist probability review remain required. They were not executed during this planning session.

## Completion statement

This is a complete authored planning package with explicit engine-verification and independent-review gates. It does not claim that Event 82 has been implemented, that all installed DLC systems have been verified, that final assets exist, or that the proposed balance has passed live campaign testing.
