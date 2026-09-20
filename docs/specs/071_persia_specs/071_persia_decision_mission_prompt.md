# Decision and mission implementation prompt: Event 071 Persia

Read parts 3, 9 to 14, 17, and 18 in full, plus `chaos-redux-decisions-missions`, `chaos-redux-scripted-gui`, actual shared cost and project APIs, and the coding prompt. Implement the complete decision map and eight mission families in part 13.

## Action families

Implement homeland target selection and settlement, regional assessment, opening supply, replacement industry, basic and specialized satrapies, emergency levies, charter hearings, guard equipment preparation and training, guard conversion, Persepolis stages, Gulf agreements, coastal readiness, Evolution III submission, guarantee intervention, administrative relocation, and reduced crisis settlements.

Every action needs a real current target, complete conditions, full cost, result, cooldown, invalid-target behavior, AI behavior, localisation, and icon. Use part 13's proposed tuning until tests justify an explicit change.

Guard recruitment is deliberately staged. Equipment is prepared in payments containing at most three named equipment types, with army experience charged only on the first batch. Personnel training then charges command power and manpower. Reserve capacity when the first preparation batch begins and release expired unused reservations under the documented refund policy. Conversion uses its own recorded equipment difference and keeps existing personnel. Do not hide many material debits under a single label.

## Cost integrity

Use at most four spendable cost types per action, at most three compact inline values, and command power costs no greater than 60. All sacrifices and construction commitments must be visible. If the actual project framework treats a construction allocation as a spendable currency, count it in the budget.

Use a single quote for visibility, availability, confirmation, and debit. Refresh it when the target or situation changes. Debit once, never allow negative stockpiles, and credit the receiver only after a valid sender debit. Inspect shared helpers carefully, including helpers that mutate or negate temporary values in place. Do not let a debit alter a saved quote used by a second action.

Record resource reservations and consumed portions. Cancellation returns only unconsumed resources. Save reload, rapid double clicks, changing the selected subject, and target disappearance must not duplicate costs, refunds, equipment, or capacity.

## Mission behavior

The mission families are opening supply, sustaining mobilization, regional settlement, charter hearing, guard training, Persepolis restoration, coastal readiness, and central command recovery. Preserve their 120-day and 180-day principal durations, the 90-day site stability requirement, and the explicitly limited extensions.

Each mission needs a new action or contribution after entry, clear current objectives, automatic success, success-before-expiry ordering, partial success where specified, and a meaningful failure or settlement. Already owning a stockpile is not enough to claim a new project's reward.

Handle lost control, missing access, subject exit, war, capitulation, canceled construction, and changed targets. An impossible objective must pause, cancel, or offer the stated revised settlement. It must not remain as an indefinite red timer with no response.

## Interface and AI

Keep the main visible action list within three to five choices, six only where needed, and normally one to three active missions. Use selected human targets and all valid AI targets. Clear stale selections. The exact-state puzzle, focus gates, decision gates, and achievement checks must use the same regional meaning.

Coordinate with the bounded Event 071 UI worker. Do not edit shared event log, event details, settings, or super-event systems from this workstream. Follow accepted reference images and native GUI evidence requirements.

AI must avoid unaffordable projects, duplicate preparation, impossible naval programs, and punitive reactions to a subject that is merely cut off. It should resolve real crises and supply shortages before optional distant commitments. Route weighted behavior to the probability auditor's named scenarios.

## Acceptance

Return the complete action and mission inventory, transaction and persistence tests, affordability boundaries, invalid-target tests, AI evidence, localisation and asset references, and the actual files changed. Test first and later project stages, repeated clicks, save reload, success on the final day, partial completion, and cancellation.

Do not call the system complete with a hidden fifth cost, duplicate guard capacity, a mission that can only expire, an approximate map, or a fake construction program. Report exact blockers where required source or engine support is unavailable.
