# Military Madness: Assets and Achievements

## Visual identity

The event combines ordinary military hardware with visibly failed expectations.
Its identity should suggest an instrument or doctrine pushed past the scale it was designed to measure.

The national-spirit icon uses a damaged military chronometer or mechanical gauge with a clear martial silhouette.
It must read at 64 by 64 pixels and must not look like a new technology unlock or a permanent national institution.

Report art is fictional period documentary material.
It depicts extraordinary military performance using 1936–1945 clothing, vehicles, equipment, and surroundings.
It does not fabricate a historical photograph or identify a real person.

Each stage has one report image.
The image sets the atmosphere of that stage without claiming that the receiving country drew a particular statistic.

## Report directions

The baseline image centers on an analog military test instrument driven beyond its normal range while a field exercise continues behind it.
The instrument has no generated readable numbers or labels.
The scene conveys an unexpected measurable military anomaly.

Military Insanity depicts an exercise whose different elements are succeeding at an implausible pace.
Keep one readable main action and a small number of supporting details.
Avoid a collage of unrelated military symbols.

Impossible Warfare depicts a period force advancing through severe terrain or weather with conspicuous ease.
The image represents the widened situational possibilities, not a guaranteed terrain or weather roll.

Gods of War depicts overwhelming military confidence and coordinated movement in a vast period battlefield.
Its impossibility comes from the scale and conduct of the force.
Avoid literal deities, fantasy armor, modern electronics, and implied new unit types.

The report treatment is applied after generating the full photographic scene.
The finished 210 by 176 RGBA texture uses the established tilted, black-and-white sepia card and real transparent edge treatment.

## Runtime asset set

| Consumer | Runtime file | Dimensions |
|---|---|---|
| Baseline report | `gfx/event_pictures/087_military_madness/report_event_military_madness.dds` | 210x176 |
| Evolution I report | `gfx/event_pictures/087_military_madness/report_event_military_insanity.dds` | 210x176 |
| Evolution II report | `gfx/event_pictures/087_military_madness/report_event_impossible_warfare.dds` | 210x176 |
| Evolution III report | `gfx/event_pictures/087_military_madness/report_event_gods_of_war.dds` | 210x176 |
| Combined national spirit | `gfx/interface/ideas/087_military_madness/idea_military_madness.dds` | 64x64 |
| Offensive achievement | `gfx/achievements/087_military_madness_minor_major_offensive.dds` and its two state variants | 64x64 each |
| Recovery achievement | `gfx/achievements/087_military_madness_core_recovery.dds` and its two state variants | 64x64 each |
| Post-expiry achievement | `gfx/achievements/087_military_madness_hold_after_expiry.dds` and its two state variants | 64x64 each |

The planned set contains fourteen runtime textures.
The three achievement subjects each produce completed, grey, and not-eligible states.
All paths are proposed production targets, not claims that assets have been generated or installed.

The package rows reuse the spirit icon and need no further art.

## Achievement design

Achievements reward actions taken during or after the military opportunity.
Receiving a package, drawing a rare category, receiving duplicates, or reaching Evolution III does not itself earn an achievement.

The identifiers below are stable proposed registration identities.
The final visible titles and descriptions remain a localisation task.

All achievements use the existing single Chaos Redux achievement registry.
They do not create another `unique_id`.
Eligibility remains country-agnostic at the campaign level, while the objective can require a particular military situation.

### A1: A minor defeats a major within one package

**Proposed ID:** `087_military_madness_minor_major_offensive`

When a natural package arrives, an independent non-major country can record major enemies with which it is already at war.
An enemy qualifies only while it controls and owns its recorded capital state at that moment.

Before that same package expires, the recipient must directly take one qualifying enemy's recorded capital state, maintain direct control of it for 30 consecutive days, and see that enemy capitulate.
All three conditions must be satisfied before the package deadline.

The objective uses the enemy and capital frozen at the opening.
A later capital move, change of major status, or change of ideology does not create an easier substitute.

Allied capture alone is insufficient.
Peaceful transfer, release, and scripted state gifts do not count as the required hostile seizure.
A capitulation secured in a shared war can count only when the recipient satisfies its own direct-control requirement.
The achievement does not claim to measure the recipient's exclusive contribution to every battle.

Losing the capital interrupts the 30-day hold.
Retaking it restarts the hold if time remains.
Other packages can overlap, but they do not extend the chosen package's achievement deadline.

Icon direction: a compact small military standard taking a much larger fortress or marshal's baton, with a clear asymmetry of scale.

### A2: Recover an invaded homeland

**Proposed ID:** `087_military_madness_core_recovery`

A natural package can open this objective for a country already at war, with at least 50% surrender progress and at least five owned core states controlled by enemies.

Freeze the recipient's complete set of owned core states at that moment.
Before the package expires, it must regain direct control of every state in that frozen set and hold the complete set for 30 consecutive days.

The frozen set prevents later de-coring, cession, release, or boundary changes from shrinking the objective.
If a required state leaves the recipient's ownership, the objective still requires its recovery.
Diplomatic gifts do not replace hostile recovery of the originally occupied states.

The 30-day hold resets when any required state leaves direct control.
A defensive victory achieved through actual reconquest can remain valid after peace, provided the original package deadline has not passed.

The achievement does not depend on a relocated capital, a chosen ideology, or a particular random modifier.
It rewards an extreme recovery from an objectively dangerous opening.

Icon direction: a damaged homeland shield restored around a firmly planted standard, with a readable reclaimed territory motif.

### A3: Keep the gains when the power ends

**Proposed ID:** `087_military_madness_hold_after_expiry`

This objective follows one continuous natural Military Madness active period, beginning when the country receives a package with no previous package active and ending when its last overlapping package expires.

At the start of that period, the country must already be at war.
Record the enemy-owned states that it does not directly control.
During the active period, it must directly seize at least five of those states through hostile control changes, with a combined frozen victory-point total of at least 50.

At the end of the active period, freeze the complete set of qualifying states that the country still directly controls.
That set must meet both thresholds.
The country must then keep direct control of the whole frozen set for 90 consecutive days, remain at war throughout those days, and receive no new Military Madness package.

A new package interrupts the unassisted hold.
There is no option to refuse the new reward for achievement purposes.
A later natural active period can open a fresh attempt.

Losing any required state interrupts the hold.
Leaving all wars interrupts it.
A settings change or debug action used to suppress the natural event invalidates that attempt under the shared achievement-integrity rules.

The objective demonstrates that the country turned temporary force into a position it could retain.
It never removes a package early or grants an extra penalty.

Icon direction: a stopped chronometer beside a still-held military standard and intact defensive position.

## Achievement tracking boundaries

Each objective records its own start, frozen actors or states, provenance, and deadline.
A newer package cannot silently rebind an older objective to a more convenient target.

Tracking uses the actual country, war, control, capitulation, and expiry events available in the installed systems.
Exact trigger and attribution support remains a production verification requirement.

Only qualifying active attempts need observations.
This does not authorize a new daily worldwide scan of every country, state, and war.

Forced occurrences, duplicated callbacks, AI-to-player switching exploits, invalid country lifetimes, and unsupported migration records cannot mint achievement progress.
The existing achievement framework owns the common integrity policy.

The objective record can outlive the package only for A3's explicitly defined 90-day unassisted period.

## Achievement art

Each achievement begins with one original generated transparent subject.
Its grey and not-eligible states are deterministic derivatives of that same subject.

Use the supplied immutable completed and grey templates and the unchanged red-cross overlay.
Do not generate three unrelated pictures or redraw the overlay.

The final three-state files remain directly in `gfx/achievements/`, matching the exact registered identifier.
Source art, prompts, processed layers, hashes, contact sheets, and DDS round-trip evidence remain part of the asset handoff.

## Writing requirements

Achievement text must state the actual action, opening condition, deadline, and control requirement without hiding the difficult part in a vague title.

The report and package rows must distinguish an individual package from the country's combined Military Madness effects.
The ten-roll stage must never be described as ten national spirits.

Numeric results are supplied dynamically with correct signs and units.
Wording must not confuse a percentage with percentage points, a reduced penalty with an added bonus, or a next expiry with the end of every package.
