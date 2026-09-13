# Achievements and Visual Assets

## Achievement set

Event 66 supports three achievements.
They reward recovery from harmful excess, long-term use of the provider space, and mastery of the highest bundle evolution.
Working labels guide implementation and asset production.
Final player-facing wording is written during implementation.

## Achievement 1: Poisoned Plenty

- Working key: `chaosx_066_poisoned_plenty`
- Visibility: Visible
- Difficulty: Hard
- Eligible country: The same continuously player-controlled country that receives the Abundance choice

### Campaign requirement

The player selects a card containing at least one candidate whose owner classifies high values as harmful.
The harmful item must apply successfully and reach the provider's critical abundance threshold.
Within 365 days, the same country must reduce that exact value below the provider's danger threshold while remaining independent and not capitulated.

The provider must declare that recovery is possible and supply the danger and recovery checks.
A permanently irreversible harmful provider is excluded from this achievement path even though it remains eligible for the event.

### Disqualifiers

- Force Trigger Mode or a debug launch applied to the qualifying Event 66 wave
- tag switching used to move the achievement ledger
- the harmful item applied only partially or failed
- the country ceased to exist before recovery
- a provider missing a verified recovery condition

### Why it is difficult

The player chooses a dangerous result, absorbs its full effect, then uses the owning mechanic to reverse it within a fixed period.
The achievement tests interaction with the owner system instead of rewarding one event click.

### Icon direction

A period-styled cornucopia or supply vessel overflowing with a dark harmful substance while one clean hand or tool closes the source.
The subject must remain readable at 64x64.
Avoid text, gore, modern warning signs, and a generic red cross.

## Achievement 2: The Full Ledger

- Working key: `chaosx_066_full_ledger`
- Visibility: Visible
- Difficulty: Very Hard
- Eligible country: One continuous player country in one campaign

### Campaign requirement

Across several successful Event 66 choices, the country accumulates applied receipts from at least eight distinct deduplication families without selecting the same candidate identity twice.
The ledger must include:

- at least one core HOI4 value
- at least one Chaos Redux value
- at least one harmful or mixed value
- at least one value selected as part of a pair or triple
- at least one DLC-specific value when a supported DLC mechanic is active for the country

When no supported DLC mechanic is active, the DLC condition is replaced by a country-specific mechanic value.
The substitution must be decided by initial campaign capability, not by a late debug change.

### Disqualifiers

- repeated selected candidate identity
- receipts collected across several tags
- any qualifying wave launched through force or debug controls
- generated cards that were never applied
- invalid or partial items counted as successful families

### Why it is difficult

The repeatable event becomes less likely after repeated firings, and the player must keep choosing new families while accepting at least one dangerous or mixed result.
The achievement rewards long-term engagement with the dynamic registry.

### Icon direction

A thick period ledger bursting with several distinct symbols, such as a fuel drop, gear, star, grain, radio spark, and abstract gauge.
The symbols should read as diverse categories without becoming tiny unreadable detail.

## Achievement 3: Threefold Surplus

- Working key: `chaosx_066_threefold_surplus`
- Visibility: Rare
- Difficulty: Hard
- Eligible country: One player country at `600+` Chaos with Evolution II and Evolution III enabled

### Campaign requirement

The player selects a triple card whose three candidates come from three distinct owner systems.
All three atomic applications must succeed.
After 180 days, every provider must report that its selected value still meets the owner-defined abundance persistence threshold.
The country must remain independent and not capitulated for the full period.

A provider without a persistence check cannot contribute to this achievement.
Spending or losing an abundant resource below its threshold causes failure for that attempt.
A later qualifying triple can start a new attempt.

### Disqualifiers

- pair or single card
- two candidates from the same owner system
- partial application
- one value falls below persistence threshold before the check date
- force or debug launch
- tag switching

### Why it is difficult

The player must receive a high-chaos triple, choose three unrelated systems together, and preserve all three abundance states for six months while continuing the campaign.

### Icon direction

Three visibly different overflowing vessels arranged around one central ring or cornucopia.
Each vessel should carry a different material cue, such as liquid, papers, and mechanical parts.
The design must stay clear at 64x64.

## Achievement tracking contract

The Event 66 receipt layer must publish:

- player-country identity
- wave identity
- force or debug state
- card cardinality
- complete or partial card result
- provider identity
- candidate identity
- deduplication family
- owner system
- source class, including core, DLC, country-specific, or Chaos Redux
- harm class
- critical, danger, recovery, abundance, and persistence checks when supplied

Achievement tracking reads receipts.
It does not infer success from event-option history or displayed text.

## Event report image

Event 66 needs one report event image.

- Suggested runtime path: `gfx/event_pictures/066_abundance/abundance_report.dds`
- Target size: `210x176`
- Source mode: Generated
- In-game role: Main Event 66 popup image
- Suggested sprite: `GFX_report_event_066_abundance`

### Visual direction

Create a period-authentic documentary scene from the late 1930s or early 1940s.
The image should show an administrative warehouse or rail depot overwhelmed by several kinds of surplus at once.
Crates, fuel drums, sacks, files, coins, military supplies, and industrial parts can spill beyond their normal storage while workers and clerks try to measure them.

The composition should communicate excess without defining one canonical resource.
A clear human scale matters.
The scene can contain a slight impossible quality, but it should still resemble a period press photograph.

Avoid readable generated text, modern containers, modern uniforms, digital devices, maps as the main subject, conference tables, glossy cinematic lighting, fantasy creatures, and one giant cornucopia.

## Achievement icon assets

Each achievement needs a completed 64x64 icon designed for the achievement surface.
The achievement pipeline later derives or creates grey and not-eligible variants according to the inspected current achievement pattern.

Suggested root filenames follow the exact achievement IDs:

- `gfx/achievements/chaosx_066_poisoned_plenty.dds`
- `gfx/achievements/chaosx_066_poisoned_plenty_grey.dds`
- `gfx/achievements/chaosx_066_poisoned_plenty_not_eligible.dds`
- `gfx/achievements/chaosx_066_full_ledger.dds`
- `gfx/achievements/chaosx_066_full_ledger_grey.dds`
- `gfx/achievements/chaosx_066_full_ledger_not_eligible.dds`
- `gfx/achievements/chaosx_066_threefold_surplus.dds`
- `gfx/achievements/chaosx_066_threefold_surplus_grey.dds`
- `gfx/achievements/chaosx_066_threefold_surplus_not_eligible.dds`

Achievement files remain in the achievement root because that surface follows engine-facing root naming.

## Asset consistency

The report image and achievements form one visual family through the idea of overflowing systems.
They should not be resized versions of one source image.
Every achievement icon needs its own composition built for 64x64.

The asset package must retain generated source art, processed PNGs, final DDS files, prompt notes, reference inspection, contact sheets, alignment review, and manifest coverage.
The final runtime paths must not point into the temporary `docs/assets/066_abundance/` workspace.

## Reference inspection

Before production, inspect the matching canonical reference families:

- report event art: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/`
- achievements: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/`

The event image should follow the actual report-event crop, contrast, border, and consumer pattern found in the installed game or established Chaos Redux files.
The achievement icons should follow the current triplet naming, canvas, state, and overlay pattern.

## Asset acceptance

The asset package passes only when:

- the report source is genuine generated scene art, not a primitive local composition
- the report image remains readable at 210x176
- the scene has no readable fake text or modern objects
- all three completed achievement icons are distinct and readable at 64x64
- no icon is a resized report image or resized version of another icon type
- required grey and not-eligible states match the inspected achievement consumer
- source, processed, and final files are documented
- final DDS paths and proposed sprite identities are stable
- no temporary asset path is used at runtime
