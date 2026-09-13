# Event 57 Achievement Implementation Prompt

Implement the complete Event 57 achievement set from `docs/specs/057_the_black_market_specs/09_assets_and_achievements.md`.

Follow the current repository achievement pattern, `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, and the Event 57 transaction, membership, exposure, route, evolution, embargo, provider, and auction receipts.

## Achievements

### `57_the_black_market_no_questions_asked`

Track settled purchases from all baseline cargo families while the player country remains below Exposure `50` for the whole attempt.

Required families are small arms, support or artillery, transport, fuel or convoys, and intelligence.

Track the highest Exposure reached. Debug grants and Force Trigger testing disqualify the run.

### `57_the_black_market_enemy_quartermaster`

Award after a settled equipment delivery whose proven source country is at war with the player at dispatch and settlement, while the transaction does not publicly expose that source.

Reject civil-war duplication, alliance before settlement, and any package without source proof.

### `57_the_black_market_embargo_has_holes`

While the player remains the target of Event 50 or another shared major strategic embargo, settle one fuel delivery, one military-equipment delivery, and one industrial-procurement delivery.

Every delivery must finish while the embargo is active.

### `57_the_black_market_liquid_assets`

The player must never adopt State Patronage. Track verified Market Credit earned from actual sales. Award after the player wins and receives a Grand Auction lot with sale-earned credit at least equal to the winning bid.

Debug credit, duplicated sale receipts, and an unsettled auction do not qualify.

### `57_the_black_market_invisible_empire`

Founding-member route. Award when Evolution III activates while the player has never reached Exposure `25`, never held a Compromised route, and never left membership.

This achievement is hidden until Event 57 fires.

### `57_the_black_market_customs_seizure`

The player must never accept membership. Track every active Black Market route through owned or controlled territory. Award after the player dismantles all of them and the connected regional cell enters verified dormancy.

### `57_the_black_market_prototype_without_a_project`

Award after an active member receives and validly fields or uses one owner-approved experimental package while the source project remains incomplete at dispatch and settlement.

An unapproved token, debug grant, or package whose owner project already completed does not qualify.

## Implementation rules

Use one-time receipts and stable tracking state. Save and reload must preserve progress without duplicate awards.

Do not infer source, hostility, route, cargo class, embargo, provider approval, project state, or settlement from loose flags when the Event 57 receipt already carries proof.

Player-country tracking must survive cosmetic changes. Civil-war and tag replacement behavior must follow the Event 57 membership-transfer contract and must not copy one achievement attempt to both sides.

Add exact localisation for title, description, hidden state, and completion. Final wording should follow the source spec direction and avoid raw mechanics or debug terms.

Add the achievement entries to the existing single Chaos Redux achievement registry. Do not create a new registry with another unique ID.

Coordinate with the asset package so each exact ID has:

- `<id>.dds`
- `<id>_grey.dds`
- `<id>_not_eligible.dds`

Update permanent Event 57 documentation with eligibility, proof, disqualifiers, and asset paths.

Run task-specific checks for:

- one-time award
- save and reload
- tag and cosmetic changes
- civil-war duplication
- debug disqualification
- source and transaction proof
- embargo timing
- Exposure maximum
- route compromise history
- auction settlement
- provider project isolation

Report any engine limitation that prevents an exact condition. Do not weaken the achievement silently.
