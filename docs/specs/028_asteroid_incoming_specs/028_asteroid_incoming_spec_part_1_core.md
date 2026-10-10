# Asteroid Incoming, Part 1: Core

## Catalog entry

- Event ID: `28`
- Event name: Asteroid Incoming
- Event type: Major, global, fire-once
- Baseline Chaos level: Calm World
- Catalog status: Needs Testing, enabled in the default event queue
- Cluster and world-end scenario: none

The explicit user requirements are listed once in the [package README](028_asteroid_incoming_spec_index.md#explicit-user-requirements).
This part explains how they fit together and how the event connects to shared systems.

## Event promise

For a brief period, observatories can steer a very large Earth-bound asteroid.
The danger cannot be cancelled; the only choice is where the object goes.
Three dynamically selected countries appear as targets, each tied to one visible state, and a fourth option keeps the natural near-miss course.

A strike is a global map event.
The course locks for two days, the centre state is destroyed, three land-adjacency rings suffer falling damage, civilian deaths enter the shared Deaths ledger, each affected country receives one report, a permanent crater remains, and atmospheric dust weighs on the whole world.
The map explosion is presentation only, and every ledger, report and modifier names the asteroid as the source.

The near miss is a complete outcome.
It causes no impact, dust, fragment or crater, and no later punishment for restraint.
The world receives one close-passage bulletin and the Major event is consumed.

## Campaign role

Event 028 creates one hard strategic decision followed by a long consequence chain.

1. The chooser directs a rare global disaster at a rival, a stranger or nobody.
2. The map changes permanently around the crater and temporarily across the rings.
3. Dust turns one regional disaster into a shared economic and supply problem.
4. At high Chaos, crater sites become military objectives worth fighting over.

The player-facing surface stays small.
The chooser makes one targeting choice, the target makes one preparedness choice, affected countries work through one recovery category, and the world watches one dust stage.
Internal calculations can be detailed; the visible surface shows only what drives the next decision.

## Fixed design rules

These rules turn the user requirements into acceptance rules.

- The board offers exactly three distinct valid country and state pairs plus the near miss, or it is unavailable; it never offers fewer targets or substitutes invalid ones.
- Each target option names the country, state and continent and says whether the state is the capital.
- Pairs are built before the board opens and never reroll, including after cancelling the confirmation or reloading a save.
- The locked state is a fixed coordinate; ownership, control, tag or government changes during the lock never move it.
- Each state is processed once at its strongest applicable damage profile.
- Every civilian loss is a real state population transaction registered once through the shared Deaths ledger.
- Each affected country receives one consolidated report, never one popup per state or fragment.
- No nuclear history, condemnation, retaliation, fallout, Chaos ladder entry or Deaths reason is created.
- Crater armour bonuses follow current control and are rebuilt from registered sites, never stacked as stale copies.

## Full event flow

Implemented event identifiers are given for orientation; the overview documents their exact behaviour.

1. **Selection.**
   The shared Major dispatcher builds the target board before dispatch and history accounting, and rejects a failed board without consuming the event.
   An invalid world shows `N/A` with the reason and stays out of automatic selection.
2. **Board (`chaosx.nr28.1`).**
   The chooser sees three strike options and the near miss.
   When Global Fragmentation or Extraordinary Minerals is active, the description warns that extra fragments will strike elsewhere and that crater control will matter, without revealing locations.
3. **Confirmation (`chaosx.nr28.2`).**
   A strike opens a confirmation that repeats the target and its consequences.
   Cancelling returns to the same board (`chaosx.nr28.8`) without rerolling.
4. **Lock.**
   Confirmation locks the pair, records the chooser publicly, sets the expected impact date and queues the hidden resolver on both the chooser and the target.
   The world receives the locked-course bulletin naming the target state, country, continent and date.
5. **Preparedness (`chaosx.nr28.3`).**
   The target chooses one of three stances during the two days (Part 2).
6. **Resolution (`chaosx.nr28.4`).**
   One hidden transaction plans every footprint, applies damage once per state, records deaths, registers craters, damages units, computes dust and aggregates per-country receipts.
7. **Reports and super-event.**
   Each affected country receives one report (`chaosx.nr28.5` for main-footprint countries, `chaosx.nr28.7` for fragment-only countries), the world receives the impact bulletin, and the super-event names the target and region.
   Fragment visuals follow one by one (`chaosx.nr28.9`).
8. **Recovery.**
   Affected countries work through emergency and reconstruction actions, every country can protect itself from dust, and crater controllers and rivals gain crater actions under Extraordinary Minerals.
9. **Aftermath.**
   The main crater is permanent, fragment sites keep their persistent crater identity, dust fades through stages with milestone bulletins, and each country receives one closeout report (`chaosx.nr28.6`) when its local recovery ends.

## Choice quality

The three targets should create tension without one option looking fake.
The board favours populated, connected states whose rings cross meaningful borders, places the second target on a different continent when possible, and still allows unusual combinations across campaigns.

The near miss must stay mechanically credible.
Choosing it gives up the chance to cripple a rival and, at high Chaos, all crater material, while avoiding dust and fragment risk (and, under the proposed condemnation below, the diplomatic cost of a strike).
No hidden reward makes it strictly better, and no hidden penalty punishes it.

## Connections to shared systems

Each connection exists because it drives a real consequence; decorative links are excluded.

### Major-event pacing

Strike and near miss both consume Event 028, reset Major weights under the shared rules and reset timer acceleration.
A failed board does not consume the event.

### Chaos Meter and Deaths

Civilian deaths raise Chaos through the shared Deaths rule, and dust raises it through the shared Air Cleanliness synchronization.
Event 028 adds no separate Chaos reward on top of those measured sources.
The Deaths ledger uses eight asteroid reasons (main impact, three main rings, fragment centre, two fragment rings, rescue failure), defined in `chaos_meter_deaths_reason`.

### Air Cleanliness

Dust writes its own source slot (`asteroid`, id 4) in the shared contamination ledger: one opening injection and a monthly reservoir that follows the stage.
It never borrows chemical, biological, fallout, aerosol or Acid Rain slots, and threshold behaviour stays owned by the shared system.

### Natural Disasters (Event 013)

Event 028 owns the impact geometry, damage, crater, reports and dust.
Inside the impact transaction it may request up to four supported Event 013 secondary disasters in catastrophic-ring states and fragment centres; Event 013 validates the family and terrain, skips unsupported families without substitution, and owns its own effects, deaths and food consequences.

### Famine and migration (proposed)

Status: proposed by the 2026-10-10 audit, not implemented, needs parent acceptance and the famine owner.

A strike that kills half a region and darkens the sky should threaten food, and the Famine system already owns food security, relief and survivor flight.
The design therefore routes the impact into famine instead of inventing an asteroid food value.

- Catastrophic-ring states, major-ring states and fragment centres submit one famine request each through a famine-owned asteroid adapter, modelled on `famine_adapt_acid_rain_state` in `common/scripted_effects/famine_adapter_effects.txt`.
- The proven amount is the state's measured impact deaths, and an accepted request opens the famine disaster food context (crop loss, damaged transport, unmet need).
- Event 028 makes no direct migration request; people flee through the famine-owned survivor flight when a famine stage is actually reached, so the two mechanics stay separate and nothing is counted twice.
- The global dust stage does not call famine directly; its effect on food reaches famine through Air Cleanliness and the existing Air Winter adapter, which avoids double counting.
- The near miss and a fail-closed course submit nothing.

The player-facing result is the existing Famine category appearing in badly hit states, with relief, reserves and evacuation as real choices.

### Camps (proposed)

Status: proposed by the 2026-10-10 audit, not implemented, needs the camp owner.
The impact already removes camp buildings in its footprint; Part 3 defines how registered camp sites must be reconciled so the camp ledger does not keep detainees who died or a site that no longer exists.

### Condemnation (proposed)

Status: proposed by the 2026-10-10 audit, not implemented, needs parent acceptance and the condemnation owner.

The chooser is publicly recorded, so a strike should cost something diplomatically; otherwise the near miss is only credible through dust and fragment risk.

- After a strike resolves, the chooser receives one public condemnation source through `condemnation_add_source` with a new non-weapon context (working name `directed_impact`), the original target as victim and the measured main-footprint deaths as the casualty input.
- The context is a non-weapon context like camp discovery: it writes no `used_unconventional_weapon`, repeat-use or pledge-breach history and is not a nuclear, chemical or biological source.
- A chooser who strikes its own territory through fragments gains nothing extra; fragment deaths are not attributed to the chooser, because fragment sites were not chosen.
- The near miss creates no condemnation.

This keeps the user's prohibition on nuclear condemnation intact while giving the choice a visible diplomatic consequence.

### World threat

Event 028 registers no world-threat source.
The dust is a shared economic burden, not an external enemy, and the world-threat flag would suppress ordinary geopolitics for the whole recovery.

### Riches Found (Event 029)

A registered Event 029 mine inside the footprint follows the reconciliation in Part 3, owned by the Event 029 package.

## Replay value

Replay value comes from the target mix, the geography and borders the rings cross, the target's preparedness stance, fragment locations, the dust severity those produce, and later fights over crater control.
The event does not need a large option tree; the changing map makes the same four choices produce different campaigns.
