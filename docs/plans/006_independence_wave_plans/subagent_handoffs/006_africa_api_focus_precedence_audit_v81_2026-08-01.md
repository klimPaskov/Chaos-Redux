# Event 006 Africa API and focus precedence audit handoff

Date: 2026-08-01.

Scope: Event 006 country-registry API integration with the Event 012 Africa priority-member package, focusing on carrier provenance, focus-tree ownership, cleanup sequencing, and the existing Event 006 origin-preservation contract. No tags, country definitions, states, advisor icons, portraits, or generic content were added.

## Outcome

Event 012 package registration remains available on approved Event 006 carriers after the live receipt and Action 102 gates succeed.

The Africa focus loader now fails closed while Event 006 owns either the active `independence_wave_active_origin` receipt or `independence_wave_focus_tree`. It clears the loaded receipt, sets the existing `africa_priority_member_focus_tree_overlay_skipped` flag, and leaves the Event 006 tree untouched.

The same loader also fails closed for a Soviet-collapse origin so a stale or concurrently transitioned Event 012 package cannot replace a Soviet focus tree.

Event 012 ideas, decisions, forces, League behavior, and AI state continue to load additively while the focus overlay is skipped.

`independence_wave_end_active_origin` and `independence_wave_reset_current_generation` retry the existing loader after clearing the Event 006 origin receipt. If the Event 012 package remains active and the tree has been restored to `generic_focus`, the Africa tree loads with `keep_completed = yes`.

Generic vanilla carriers remain eligible for the Africa tree, and meaningful non-generic trees continue to receive additive package content with the overlay skipped.

## Files changed

- `common/scripted_effects/012_africa_priority_member_effects.txt`.
- `common/scripted_effects/006_independence_wave_effects.txt`.
- `docs/events/006_independence_wave/systems/country_registry.md`.
- `docs/plans/012_africa_plans/012_africa_independence_wave_tag_loading_handoff.md`.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_priority_member_country_package_audit_2026-08-01.md`.
- This handoff.

The concurrent Africa nature-power assignments in `012_africa_priority_member_effects.txt` were preserved unchanged.

## Helper map

| Helper | Scope | Inputs | Outputs | Side effects and call sites |
| --- | --- | --- | --- | --- |
| `africa_priority_member_ensure_focus_tree_loaded` | COUNTRY effect | Active Event 012 package, current origin flags, and current focus tree | `africa_priority_member_focus_tree_loaded` or `africa_priority_member_focus_tree_overlay_skipped` | Loads the static Africa tree only when the protected Event 006/Soviet surfaces are absent; called by package registration and Event 006 IW-093/IW-098 cleanup. |
| `africa_priority_member_can_register_package` | COUNTRY trigger | Africa host target, Action 102 approval, origin predicate, carrier identity, and lifecycle flags | Registration eligibility | Intentionally retains active Event 006 carrier eligibility so the package payload can coexist additively; it still rejects Soviet origin and stale requalification. |
| `is_independence_wave_registry_event6_origin` | COUNTRY trigger | Event 006 active-origin lifecycle | Event 006 provenance result | Canonical Event 006 origin view used by the registry and related package gates. |
| `is_independence_wave_registry_soviet_origin` | COUNTRY trigger | Soviet-collapse active-origin lifecycle | Soviet provenance result | Canonical Soviet provenance guard used by Africa origin predicates, registration, and the loader. |
| `independence_wave_registry_clear_event6_origin` | COUNTRY effect | Valid Event 006 origin cleanup | Cleared active receipt and ended marker | Clears the origin before the post-clear Africa loader retry. |
| `independence_wave_end_active_origin` | COUNTRY effect | Event 006 cleanup reason and active origin | Ended Event 006 generation | Runs the existing cleanup, clears the origin, and then retries the Africa focus loader. |
| `independence_wave_reset_current_generation` | COUNTRY effect | Generation reset request | Cleared Event 006 generation state | Performs generation cleanup, clears the active origin, and then retries the Africa focus loader. |

## Constants and tuning

No constants were added or changed.

The focus tree ID, `keep_completed = yes`, package flags, and overlay receipt flags already belong to the existing Event 012 package contract.

The precedence check uses existing boolean flags and focus-tree predicates rather than introducing a numeric tuning value.

No unsupported dynamic focus-tree field was introduced; the `load_focus_tree` tree ID remains static and no variable or constant token is passed to that field.

## Event targets and cleanup

No event target was added, renamed, or cleared by this patch.

The existing `africa_host` target remains the Action 102 registration input, and existing Event 006 setup targets retain their prior ownership and cleanup.

The post-clear retry is deliberately placed after `independence_wave_registry_clear_event6_origin` and after the reset path clears `independence_wave_active_origin`, so the helper cannot replace an Event 006-owned focus surface during cleanup.

The existing DOX and SOK cleanup calls remain in place and become guarded no-ops while Event 006 still owns the origin/tree.

## Migration from the previous duplicated precedence

1. The old Event 012 loader treated the seven Event 006 carrier tags as an unconditional replacement-tree exception and could load `africa_priority_member_focus_tree` over an active `independence_wave_focus_tree`.
2. The loader now checks active Event 006 origin/tree and Soviet provenance before any `load_focus_tree` effect.
3. The package registration gate remains unchanged for active Event 006 carriers, preserving the accepted live-receipt and Action 102 route while keeping the package payload additive.
4. Event 006 cleanup now retries the loader only after its origin receipt is cleared, restoring the Africa tree when the package remains active and the current tree is generic.
5. The canonical Event 006 registry document and current Event 012 loading/audit handoffs now describe this same precedence and sequencing.

## Read-only architecture evidence

The offline focus inspection found `africa_priority_member_focus_tree` as a separate eight-focus tree and found that Event 006 owns a separate `independence_wave_focus_tree` surface. The current Africa inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08ccb9b60178a3ce4818a2d91766eed476c563a1d1064ed2ccac4487b7577af9/8d62d703954722e7bcb028838430d4af317d2b95d3caad6224e64d5234b8f4df/focus-inspect.ccc5219f5c550211.json`.

The focus inspector reported pre-existing generic-tree missing-icon diagnostics and three Africa layout warnings; no focus source or asset changes were made.

The read-only Event scan completed as a bounded workspace scan with deferred helper/lifecycle projections. Its current artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/184c5100ed01cdc9604cbf8459b20704caf22d41cc79922ccc80d5817124e604/c87fb439f579d7be94a5237c750daff948dfa5a04f1e525a6707d6e8a49b318a/event-scan-fcce0bc1eab2.json`.

Offline wiki and vanilla documentation confirm that `load_focus_tree` replaces the active national tree and that `keep_completed` preserves completed focus receipts; this is why the Event 006 ownership guard is required before the effect.

## Validation

- Re-read the changed loader and lifecycle blocks with line-numbered source inspection.
- Confirmed the loader contains the Event 006 active-origin, Event 006 focus-tree, and Soviet-origin fail-closed branch before its load branch.
- Confirmed both Event 006 cleanup paths call the loader after clearing the active origin.
- Confirmed generic carriers still use the existing generic-tree branch and meaningful-tree skip branch.
- No Hearts of Iron IV process or live-save validation was run; the parent owns live campaign acceptance.

## Risks and limitations

Active Event 006 carriers can still register the Event 012 package by design, but they do not receive the Africa focus tree until Event 006 cleanup clears the protected origin/tree and executes the post-clear retry.

If a future Event 006 cleanup path restores neither `generic_focus` nor a reviewed no-tree state, the loader remains fail-closed and records the skipped overlay rather than guessing or overwriting the current tree.

The Soviet guard protects against stale package flags and origin transitions, but it does not attempt to migrate or remove an Africa tree that was loaded before a later Soviet-origin transition.

No fallback tags, substitute states, generic focus content, advisor assets, or unrelated systems were introduced.

## Follow-up

Any future change that wants Africa focus content to coexist concurrently with the full Event 006 tree must introduce an explicitly reviewed additive focus-surface contract instead of weakening this guard or reusing `load_focus_tree` as an overlay mechanism.
