# Event 012 B3 Capital Without Capture owner closure

Status: implemented as a narrow engine-callback owner patch; the achievement remains blocked for live campaign acceptance and any other matrix proof not represented by the source trigger.

## Scope

This tranche closes the two remaining government-capture reader-only flags for `africa_capital_without_capture` without adding a country tag, a faction, a recurring world scan, or a proxy based on opinion or project count.

## Exact owner

The existing `on_puppet` callback in `common/on_actions/012_africa_world_order_on_actions.txt` is the authoritative peace-conference subject-creation witness. It requires that ROOT retain an African core, be the current Event 012 host or a current-generation member, and be placed under a non-African capital. Government-capture classification is additionally host-only because the achievement protects the Charter government, not an ordinary member government.

When the external overlord (`FROM`) has the target-owned `africa_diaspora_bond_issue_completed` receipt, the callback calls `africa_achievement_record_diaspora_government_capture`; this is the narrow diaspora-capital actor definition used by the investment route.

All other qualifying external overlords call `africa_achievement_record_foreign_government_capture`. The callback then preserves the pre-existing `africa_achievement_record_external_puppet_status` owner for the military achievement, so no existing disqualifier is replaced or duplicated.

The bounded `on_release_as_puppet` callback covers the occupied-territories release path with the same host-only classification. The engine documentation exposes no single callback that identifies every direct autonomy effect as a new government capture, so unmarked autonomy-level changes remain an explicit acceptance blocker rather than being inferred from a generic subject state.

## Source changes

- `common/scripted_effects/012_africa_achievement_effects.txt` defines the two sticky achievement owner helpers.
- `common/on_actions/012_africa_world_order_on_actions.txt` classifies the overlord inside the bounded `on_puppet` and `on_release_as_puppet` witnesses.
- `docs/plans/012_africa_plans/012_africa_b3_achievement_owner_closure_2026-08-01.md` records the row-28 follow-up.
- `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` records the measured ownership, loss, capture, and corruption owner evidence while retaining the blocked live status.

## Validation and remaining risk

Static source review confirms one definition and two bounded callback owners for each new helper, one shared external-puppet receipt, no new tags or models, and no reader-only government-capture flag in the Event 012 source tree.

The callbacks use the documented subject-creation scopes (`ROOT` as puppet and `FROM` as overlord); ordinary opinion changes, faction membership, annexation, and unrelated diaspora contact do not set either flag. Direct autonomy transitions that do not pass through one of these subject-creation callbacks remain unclassified.

The achievement remains blocked until a live campaign demonstrates ten distinct locally controlled projects, the measured ownership threshold, no later ownership loss, no unresolved corruption, and no capture outcome. No in-game session was launched.

No fallback was used. The remaining unclassified direct-autonomy paths are a documented engine-scope limitation and keep the achievement blocked until an exact owner is exposed.
