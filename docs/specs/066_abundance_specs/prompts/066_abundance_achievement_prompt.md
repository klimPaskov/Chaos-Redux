# Event 066 Abundance Achievement Prompt

Implement and document the three Event 66 achievements defined in `specs/066_abundance_spec_part_8_achievements_assets.md`.
Use the exact Event 66 provider receipts as the source of truth.
Do not infer achievement progress from option text, event history, or generated cards that were never applied.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, the current achievement registry and localisation, and the full Event 66 spec pack.
Use the single root Chaos Redux achievement registry and the current root-only achievement asset convention.

## 1. Poisoned Plenty

- Working key: `chaosx_066_poisoned_plenty`
- Visibility: Visible
- Difficulty: Hard
- Eligible country: One continuous player country

Start a qualifying attempt when the player selects a card with at least one successfully applied candidate marked harmful and the provider confirms that it reached its critical abundance threshold.
The provider must expose a valid recovery check.
Within 365 days, the same country must reduce the exact candidate below its owner-defined danger threshold, remain independent, and avoid capitulation.

A later qualifying selection can start a new attempt after a failed attempt.
Do not allow an irreversible provider to create an unwinnable attempt.
Do not count partial or rejected applications.

Disqualify the attempt when the qualifying wave used Force Trigger Mode, debug setup, or transferred progress through tag switching.

Title direction should convey wealth that became dangerous and was brought under control.
Description direction should name the risk and recovery without exposing provider metadata.
Icon direction is an overflowing vessel releasing a dark substance while a hand or tool closes it.

## 2. The Full Ledger

- Working key: `chaosx_066_full_ledger`
- Visibility: Visible
- Difficulty: Very Hard
- Eligible country: One continuous player country in one campaign

Track successful applied receipts across Event 66 waves.
Unlock when the country has selected at least eight distinct deduplication families without repeating a selected candidate identity.
The successful set must include:

- one core HOI4 value
- one Chaos Redux value
- one harmful or mixed value
- one value chosen inside a successful pair or triple
- one DLC-specific value when a supported DLC mechanic was active for the country at campaign initialization

When no supported DLC mechanic was active at initialization, replace the DLC condition with one country-specific mechanic value.
Store that branch once and do not let debug changes switch it later.

Do not count generated but unselected values, partial failures, duplicate candidate identities, force-triggered waves, or receipts collected by another tag.

Title direction should convey a national ledger in which every category has overflowed.
Description direction should make the diverse-family requirement readable without naming hidden providers.
Icon direction is a bursting period ledger with a few clear category symbols.

## 3. Threefold Surplus

- Working key: `chaosx_066_threefold_surplus`
- Visibility: Rare
- Difficulty: Hard
- Eligible country: One player country at `600+` Chaos with Evolution II and Evolution III enabled

Start an attempt when the player selects a triple card whose three successfully applied candidates come from three distinct owner systems.
All three providers must expose an abundance persistence check.
After 180 days, every selected value must still meet its provider's persistence threshold.
The country must remain independent and not capitulated.

Fail the current attempt when any value falls below threshold, any application is partial, the country capitulates, or the ledger transfers to another tag.
A later complete triple can begin a new attempt.

Disqualify Force Trigger Mode and debug setup.

Title direction should convey three unrelated systems remaining in excess at once.
Description direction should state the distinct-owner and six-month persistence challenge.
Icon direction is three different overflowing vessels around one central ring.

## Shared tracking requirements

The Event 66 receipt layer must publish stable fields for:

- wave and card identity
- player country
- force and debug state
- cardinality
- complete or partial result
- provider identity
- candidate identity
- owner system
- deduplication family
- source class
- harm class
- critical threshold
- danger threshold
- recovery state
- abundance persistence state

Tracking must survive save and load.
Progress must be scoped to the same country and campaign.
A failed attempt must clean up its timed state without deleting unrelated long-term Full Ledger progress.

## Assets and localisation

Route completed icon production through `prompts/066_abundance_asset_prompt.md`.
Use the exact current achievement triplet pattern for completed, grey, and not-eligible files.
Write final localisation from the directions above.
Do not expose internal family counts beyond what the achievement description needs.

## Validation

Test natural automatic Event 66 waves separately from forced developer setup.
Use bounded developer setup to prove tracking paths, but confirm that the disqualifier blocks achievement completion under force and debug state.
Verify save and load during each timed attempt.
Verify that partial bundle application never counts as complete.
Verify that tag switching cannot merge or move progress.
Verify that provider removal or migration fails a pending attempt safely.
Document all keys, flags, variables, timed states, icon paths, and failure cleanup.
