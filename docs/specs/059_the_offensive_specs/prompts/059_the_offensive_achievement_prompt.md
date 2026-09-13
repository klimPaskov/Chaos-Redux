# Event 059 achievement implementation prompt

Implement one event-specific achievement through the current Chaos Redux achievement system. Read `AGENTS.md`, the Event 059 spec pack, `chaos-redux-events`, `chaos-redux-event-assets`, the current achievement registry, and installed vanilla achievement precedents before editing.

## Working identity

- Working key: `chaosx_059_break_the_spearhead`
- Working label direction: a weaker country turns back the strongest form of the worldwide offensive
- Visibility: visible
- Difficulty: very hard and rare
- Eligible player: any ordinary independent player-controlled country that is not a major when qualification begins

The working key can remain stable. The working label is not final localisation.

## Qualification

Start a guarded qualification record when all of these are true:

- Event 059 is active
- Evolution III, Total Offensive, has activated
- the player enters or is already fighting a defensive war
- at least one original attacking enemy is an AI-controlled major
- the player is independent and not a major
- the player controls its capital and is not capitulated
- the player's side has no major ally or major overlord
- the qualifying enemy major is materially stronger by a verified combination of industry and military capacity
- the qualifying enemy is not already close to capitulation

Snapshot the qualifying enemy, qualification date, player status, relevant core-state baseline, major-ally restriction, and any strength comparison required by the final verified implementation.

## Unlock

Unlock only when:

- at least 180 continuous days have passed since qualification
- the player has remained uncapitulated and independent
- no major has joined the player's side during the qualifying period
- the qualifying enemy remained AI-controlled during the decisive period
- the qualifying enemy major is capitulated or otherwise leaves the qualifying war in defeat
- the player still controls its capital
- the player controls at least 75 percent of the core states it controlled at qualification

The achievement should not require the player to remain a non-major after qualification. Success may legitimately make the country stronger.

## Disqualifiers and exploit guards

Disqualify the active record when:

- the player becomes a subject
- a major joins or protects the player's side
- the player capitulates
- the qualifying enemy becomes human-controlled before the decisive outcome
- the player leaves the qualifying war without defeating the target
- the qualifying war is replaced by an unrelated conflict that no longer contains the tracked attacker
- the player joined after the tracked attacker was already near defeat
- a second qualification attempt would overwrite a stronger valid record

Use one stable tracking record per player country. Clear stale targets safely after annexation, tag changes, war end, or invalidation. Save and reload must preserve valid progress.

## Balance verification

Do not treat major status alone as proof of strength. Use current verified script-accessible values that can compare industry and military capacity at qualification. Centralize thresholds. Audit edge cases where a nominal major is nearly defeated, has no army, or is already fighting several stronger powers.

The achievement must not unlock merely because the player survived, waited 180 days, joined a winning coalition, or delivered the final blow after a late entry.

## Player-facing direction

Write final title and description during implementation. The text should clearly communicate:

- the player begins as a non-major
- Total Offensive must be active
- the war is defensive
- the enemy is a stronger AI major
- no major ally may protect the player
- the player must survive and defeat the attacker

Avoid hidden formula detail in the short description. Put precise blocked conditions in the eligibility tooltip.

## Icon direction

Route the achievement icon through `chaos-redux-event-assets` and `chaosx_icon_artist` with `fork_context=false`.

Create original 64 by 64 achievement artwork showing a small fortified shield or defensive line snapping and turning back a large offensive arrow. Keep the silhouette readable at native size. Do not reuse the event report image. Follow the inspected current achievement consumer for completed, grey, and not-eligible states.

## Validation

- inspect the complete achievement registry before adding the key
- verify tracking across save and reload
- test qualification, each disqualifier, and unlock
- test a late-join exploit
- test a nominal but already defeated major
- test player takeover of the qualifying enemy
- verify localisation and icon states in the achievement UI
- document every tracking identifier and cleanup path
