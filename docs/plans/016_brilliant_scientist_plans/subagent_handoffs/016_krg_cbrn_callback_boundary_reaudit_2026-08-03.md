# Event 016 native CBRN callback boundary re-audit

> Scope correction, 2026-08-09: this audit remains valid for the optional KRG biological stockpile and delivery ledger, but its callback absence does not block native Event 016 biological or Portal Facility Raids. Native raids remain engine-owned for preparation, reservation, cancellation, expiry, outcome, and history; no parallel ledger is authorized. See `docs/plans/016_brilliant_scientist_plans/016_portal_plague_documentation_reconciliation_2026-08-09.md`.

## Finding

The current HOI4 raid API still exposes only outcome-time scripted hooks. Native `essential_equipment` is collected when a raid is created, while strategic and battlefield biological raids invoke their existing resolvers from `success_levels.*.actor_effects`. The available RAID_INSTANCE documentation exposes actor, victim, target, and outcome context, but no stable raid identity, pre-reservation callback, cancellation callback, expiry callback, or native `on_raid_*` on-action.

## Evidence reviewed

- `common/raids/biological_raids.txt` and `common/raids/biological_battlefield_raids.txt` collect fixed native payloads before outcome effects and call the existing biological resolvers at every outcome site.
- `common/scripted_effects/biological_raid_effects.txt` and `common/scripted_effects/biological_battlefield_effects.txt` resolve post-native actor/victim/state contexts and have no reservation or cancellation lifecycle.
- Vanilla `common/raids/_documentation.md`, `documentation/effects_documentation.md`, and `documentation/triggers_documentation.md` document only outcome-time RAID_INSTANCE surfaces; repository on-action files contain no supported raid launch/cancel/expiry callbacks.
- `docs/plans/016_brilliant_scientist_plans/016_krg_biological_stockpile_delivery_addendum.md` requires a stable idempotent receipt spanning pre-reservation, native reservation, outcome settlement, cancellation, expiry, transfer, and defeat.

## Disposition

Do not add an Event 016 stockpile ledger, production decision, delayed flag, parallel payload, or outcome-only debit. Those approaches can double-charge native payloads, create free payloads, or mis-handle concurrent/cancelled raids. The queued KRG biological stockpile remains blocked until a shared CBRN owner supplies a stable native callback/receipt contract.

When that contract exists, the intended Event 016 boundary is four keyed helpers: pre-reservation gate, reservation commit, outcome settlement, and cancellation/expiry return. The existing confirmed-use helper must remain attached to canonical confirmed lifecycle attribution rather than every native consumption outcome.

No gameplay files were changed by this audit. No HOI4 runtime was launched. The absence of a callback is an engine/API blocker, not an approved fallback.
