# Achievement implementation prompt: Event 42 Equipment from Heavens

Implement the three Event 42 achievement routes from the accepted specification. Final names and descriptions require a dedicated localisation pass. Working labels must not be copied automatically into final text.

## Shared achievement rules

- Use the single Chaos Redux achievement registry under `common/achievements/chaos_redux_achievements.txt`.
- Keep runtime IDs stable and event-scoped.
- Add full tracking flags, variables, eligibility snapshots, disqualifiers, unlock triggers, localisation, icons, docs, and Event 42 hooks.
- Use the completed, grey, and not-eligible DDS triplets created by the asset package.
- Preserve save and reload.
- Prevent tag-switch, force-trigger, duplicate-grant, annexation, puppet-release, and repeated-delivery exploits according to the repository achievement rules.
- Do not attempt exact equipment-origin tracing when the engine does not preserve origin inside deployed divisions. Use documented receipt snapshots and bounded proxy conditions.

## `042_equipment_from_heavens_tiny_arsenal_state`

At the qualifying Event 42 receipt, snapshot:

- recipient identity
- total factory count below ten
- fielded division count
- capital state
- delivery date
- player-control and achievement-validity state

Complete when the same country, within one year, has at least fifty more fielded divisions than at receipt, still controls its capital, and then defeats or forces peace against a country that was a major during the challenge window within three years of receipt.

The implementation must decide the cleanest exact war-victory proof supported by current Chaos Redux achievement patterns. A mere temporary battle win is insufficient.

## `042_equipment_from_heavens_nuclear_lottery`

At receipt, require and snapshot:

- zero nuclear weapons before the delivery
- no ordinary nuclear production access before the delivery
- a positive Event 42 nuclear cache
- recipient identity and delivery sequence

Complete when the recipient conducts a normal nuclear strike before it gains ordinary nuclear production access. The strike must use the shared nuclear consequence pipeline and consume a real weapon from the delivered stockpile.

A launch performed only through debug or force-trigger paths must not qualify.

## `042_equipment_from_heavens_borrowed_nightmare`

At receipt, require and snapshot:

- Evolution III active
- one exact allowlisted special-equipment family
- owner event not fired
- recipient identity
- owner event ID and pre-delivery fired state
- compatibility receipt ID

Complete when the recipient materially fields or uses that exact family in a valid combat, raid, payload, or unit action while the owner event remains unfired.

Passive stockpile ownership, reserve modifiers, opening a template, or moving a division without combat is insufficient. Each special family needs an owner-approved completion callback that proves real use without firing the owner event.

If a special family has no safe completion callback, it cannot qualify for this achievement and should not enter the achievement-capable allowlist.

## Multiple challenges

A later Event 42 receipt must not overwrite an active stronger challenge. Use separate eligibility and completion state for the three routes. A failed or expired route cleans its temporary targets and can be reopened by a later valid receipt when repository achievement policy permits it.

## Documentation and validation

Document exact IDs, triggers, snapshots, disqualifiers, callback owners, and icon paths in the Event 42 achievement section. Add acceptance scenarios for fresh campaigns, save and reload, repeated receipts, tag switching, annexation, source-event firing, debug modes, and multiplayer ownership.
