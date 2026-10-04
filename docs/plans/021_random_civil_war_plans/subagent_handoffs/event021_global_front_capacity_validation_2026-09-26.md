# Event 021 global-capacity plan validation tranche

Disposition: implemented in source as a bounded plan-validation improvement. The dynamic front/actor migration remains incomplete.

## Acceptance basis

The user requires front and actor counts to remain campaign-dynamic and allows the existing shared global front ceiling as a safety limit, but forbids a fixed per-crisis planned-front cap. This change replaces the separate plan-count ceiling with the currently available shared front capacity. It does not claim that current row writers produce an arbitrary number of rows.

## Changed files and behavior

- `common/scripted_effects/021_random_civil_war_parent_effects.txt`: `event021_parent_validate_front_plan` now fails closed if the shared maximum-front value is absent, derives remaining capacity from `global.random_civil_war_max_active_fronts - global.random_civil_war_active_front_count`, clamps negative capacity to zero, and rejects a planned row count above that live remainder.
- `common/script_constants/021_random_civil_war_constants.txt`: removed `maximum_planned_fronts`, whose only runtime reader was the replaced plan validator. Also removed `maximum_multifront_states`, `maximum_major_belligerents`, and `maximum_minor_belligerents` after a current runtime source scan found no code readers. Historical snapshots and old handoffs still preserve their pre-edit text as evidence.
- `common/scripted_effects/021_random_civil_war_parent_effects.md` and `docs/events/021_random_civil_war/overview.md`: documented the global-capacity validation and explicitly retained the fixed writer/activation limitation.

The parent-effects file was `6D736B9413913F1C232DDDC8302F6F7D7C53143D52A01FA1A53D15DDCE3E15DF` before this validator edit and is `F2F238BA3C3B698B883F660881FE736CB87719E6A0FC5E543FAF50FC1B2CD1A3` afterward. The current constants file is `1525A8ED1D75CBCFF5983139F709A7511D4EE9418CF4B11B389057101AD348F9`.

No probability-bearing weights, scores, MTTH coefficients, random pools, or AI factors were edited in this tranche. The manual-scenario ticket uniqueness patch remains unchanged.

## Validation and remaining limits

The exact current runtime source scan found no remaining references to the four removed constant names. The existing capacity setup is initialized by `event021_parent_initialize_global_runtime` through `event021_refresh_global_capacity`, and the plan validator now checks the same global maximum and active-front counter used by the registry. This is source inspection only and does not prove execution or state transfer in HOI4.

The builder still emits the host remnant, primary claimant, up to two named ordinary secondary rows, and one named Event 006 secondary row. Activation, review, succession, scenario replay, and cleanup still have singleton consumers. Those paths continue to impose a fixed effective plan shape, so the user's fully dynamic actor requirement remains incomplete. This tranche has no gameplay fallback and is not a completion claim.

The post-change focused `hoi4.event_inspect(mode=trace, selector={kind:event,eventId:chaosx.nr21.1}, refresh=true)` returned `EVENT_INSPECTED_PARTIAL`, revision `f95e58711c7ffdcda2bae4e59e7e030aa20b045e86c1e5e9d35a647536d55fa0`, graph hash `06fc0bb73dcf1f3e4c47694633ac804b9d812ab3372152192f305b3b10a289e3`, zero blocking diagnostics, and zero helper projections. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9fcb68e80bf499883615c0ee8900f35c077caff77c37625377aa6c599aa60721/46e6d941164de537173fdc4d7fc9ec6032482bf4038ec7318e1ff1be011fff8c/event-trace-f95e58711c7f.json`. This focused event projection does not inspect scripted-effect lifecycle semantics. Runtime multi-front, capacity-boundary, rollback, sibling-settlement, Event 006 coexistence, scenario, and performance checks remain open. No game was launched and no commit was made.
