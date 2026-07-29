# Event 019 incremental registry and category lifecycle completion audit

Date: 2026-07-29
Role: `chaosx_event_completion_auditor`
Mode: focused read-only audit of the latest incremental Event 019 changes
Audit-owned file: this handoff only

## Verdict

**FAIL — the incremental request is not complete.**

The ordinary-category lifecycle change closes the category after a claimant takeover, hides it after a derivative transaction reaches its initialization boundary, and permits quiet Evolution III or IV closeout when no live crisis remains.

The shared registry consumer is structurally dynamic, but ordinary Event 019 automatic generation still cannot select any of the three current providers.

| Severity | Open count | Result |
| --- | ---: | --- |
| P0 | 0 | No destructive registry or transaction corruption was established in this focused audit. |
| P1 | 1 | Providers 501, 502, and 503 remain ineligible for ordinary Event 019 automatic generation because their callbacks never set the receipt that the selector consumes. |
| P2 | 3 | Derivative closure is stamped before the later proven-success commit, quiet closeout can leave the Board-open flag stale, and the latest registry change has no matching implementation handoff or current documentation disposition. |

The parent should not promote the latest incremental request as complete until the P1 provider-selection gap is corrected and independently re-audited.

## Snapshot audited

The decisive snapshot hashes were:

- `common/scripted_effects/019_infantry_spawn_core_effects.txt`: `7C0C849A457C61E7D9ABF31A59B9C93268795544290B0ACFAE47B6C0B08F3978`;
- `common/scripted_triggers/chaos_unit_family_registry_triggers.txt`: `2028F1406CF2D50A09EDBDA8D5FA277ED7A319BD64B08844D4DCCBAA1D70AA82`;
- `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`: `A576E45CD52B134CED539F7563ECE722799F1EDA1C43F9726B724EE9D2B0863B`;
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`: `B76B38688272DA5080C91F5AD2E09F3680812FB88FD4C04D4AA9DD7EFE2CD829`;
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`: `162E9E75358C3A126F6E6B5C9F30145EC42A094E9AC9BA2FFF3CBD3A53F22ED0`;
- `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt`: `FB9D8AB76ACE065F687CE46AEDAA2EA015431E3E04BBE5B012A7F8FF0CE86FF3`;
- `common/decisions/categories/019_infantry_spawn_decision_categories.txt`: `9E0EDFC757503E5571F72585D7152E963A4EEEF8E5B937B31A971BB243E29FC2`;
- `019_ordinary_management_category_lifecycle_handoff_2026_07_29.md`: `D8C4EEFFC44E8061122E7C91958F5EE1B1613FC68F290983DFBE22A622DEC46F`.

The worktree contains extensive unrelated changes.

This audit treated only the Event 019 registry and ordinary-category lifecycle files named below as in scope and did not modify gameplay source.

## Completion status by surface

| Surface | Status | Exact result |
| --- | --- | --- |
| Shared aligned-row discovery | Finished | `infantry_spawn_select_native_registered_family` iterates `global.chaos_unit_family_*` rows, reads the recorded provider ID, and meta-dispatches the provider eligibility callback without a family enumeration. |
| Future-provider extension architecture | Finished structurally | A future provider can contribute one aligned row, startup registration call, neutral visual profile 999, and the complete provider-ID callback surface without adding an Event 19 family list or registry-file row. |
| Current-provider ordinary automatic draws | Missing / fail | Providers 501, 502, and 503 all leave `chaos_unit_family_candidate_native = 0` for an ordinary Event 19 country, while the selector requires that value to be positive. |
| Dynamic provider template and spawn dispatch | Finished | Once a row is selected, Event 19 builds and spawns through provider-ID meta dispatch rather than a family branch. |
| Claimant-takeover category closure | Finished | A proved selected claimant takeover sets `infantry_spawn_claimant_takeover_complete`, clears the open Board flag, and the shared category gate rejects the terminal country. |
| Derivative-revolt category closure | Partial | The parent Board and category are closed, but the closure/disqualifier marker is written during common derivative package initialization rather than at the later proved-success transaction branch. |
| Evolution III or IV quiet category closeout | Finished for the decision category | The category no longer treats evolved capability flags as perpetual visibility, automatic generation is suppressed at Evolution III, and the category gate becomes false when the enumerated crisis and operation signals are absent. |
| Quiet Muster Board cleanup | Simplified / stale-state risk | The scripted GUI becomes invisible because Board availability uses the same gate, but no general quiet-closeout path clears `infantry_spawn_muster_board_open`; the refresh helper is called only by Board transactions. |
| Documentation and handoff alignment | Partial / stale | The lifecycle handoff covers its decision changes, but the latest registry changes are absent from it and no separate current registry handoff was found. Current documentation also overstates success-gated derivative closure and retains pre-incremental completion claims. |
| Assets, super-events, focus trees, country packages, achievements, event log, evolutions, and catalog | Not changed in this increment | No new visual or wider content requirement was introduced by the two audited requests. The early derivative revolt disqualifier does affect achievement history semantics, as described below. |

## P1 finding: current providers remain unreachable in ordinary automatic generation

### Dynamic architecture that passes

`common/scripted_effects/019_infantry_spawn_core_effects.txt:181-188` loads the provider ID from the aligned row and dispatches `chaos_unit_family_provider_[PROVIDER]_event19_evaluate_eligibility`.

`common/scripted_effects/019_infantry_spawn_core_effects.txt:191-265` performs two weighted row passes and has no zombie, ghost, golem, family-501, family-502, or family-503 branch.

`common/scripted_effects/019_infantry_spawn_core_effects.txt:422-444` invokes the selector for every ordinary generation and falls back to the ordinary state processor only when no registry row was selected.

`common/scripted_effects/019_infantry_spawn_generation_effects.txt:2375-2383` spawns a selected family through `chaos_unit_family_provider_[PROVIDER]_event19_spawn_unit`.

`common/scripted_effects/chaos_unit_family_registry_effects.txt` owns the aligned registrar, and `common/on_actions/002_zombie_outbreak_on_actions.txt:10`, `common/on_actions/010_death_on_actions.txt:10`, and `common/on_actions/005_soviet_collapse_on_actions.txt:10` register providers 501, 502, and 503 from their existing parent startup surfaces.

These facts satisfy the no-family-list and no-new-registry-file architecture.

The current visual-profile bindings at `common/scripted_triggers/chaos_unit_family_registry_triggers.txt:107-177` enumerate the three reserved initial identities, but they do not force a future provider edit because an external provider can use the neutral profile 999 without adding another branch.

### End-to-end eligibility that fails

`common/scripted_triggers/chaos_unit_family_registry_triggers.txt:65-75` adds `chaos_unit_family_current_row_allows_event19_native_draw`, which accepts either the ordinary-mix or family-lot policy.

The three current rows at `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4112-4127`, `4348-4363`, and `4571-4586` are enabled, spawn-capable, and register `family_only`, so they pass the new row-policy trigger.

The selector then requires `chaos_unit_family_candidate_native > 0` at `common/scripted_effects/019_infantry_spawn_core_effects.txt:206-212` and again at `242-253`.

Provider 501 initializes both receipts to zero and sets `candidate_native` only for a Zombie Outbreak actor or an existing zombie derivative at `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4130-4141`.

Provider 502 does the same only for a Death actor or an existing ghost derivative at `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4366-4377`.

Provider 503 does the same only for KMB or an existing golem derivative at `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4589-4606`.

For an ordinary Evolution IV Event 019 country, providers 501 and 502 set `chaos_unit_family_candidate_eligible = 1` but leave `chaos_unit_family_candidate_native = 0`.

Provider 503 may set `candidate_eligible = 1` when its industrial condition passes, but it also leaves `candidate_native = 0`.

The resulting total native registry weight is zero, `infantry_spawn_selected_registry_index` remains invalid, and generation proceeds through `infantry_spawn_process_selected_ordinary_state`.

Changing the row gate from `allows_event19_family_lot` to `allows_event19_native_draw` therefore does not make any current provider newly selectable.

The old selector already accepted all three current `family_only` rows; the provider receipts remain the decisive rejection.

### Required disposition

The implementation owner should align the provider eligibility receipt consumed by automatic generation with the requested all-current-provider behavior.

This can be done without a family list by changing the shared receipt contract or the current provider callbacks, but the parent must choose one coherent contract and preserve provider-owned eligibility rules.

A future-provider proof should then register one synthetic external row through the public contract and demonstrate that automatic generation discovers, weights, builds, and spawns it without editing Event 19 selection code.

## Ordinary decision-category lifecycle audit

### Quiet closeout passes for the category

`common/scripted_triggers/019_infantry_spawn_triggers.txt:112-150` centralizes the ordinary lifecycle in `infantry_spawn_ordinary_management_crisis_is_active` and `infantry_spawn_ordinary_management_category_is_relevant`.

The crisis trigger covers unresolved generations, positive active-lot count, positive unaccounted count, active claimants, deferred actions, the pending bounded opening, the named running management operations, and the request cooldown.

Evolution III and IV capability flags are deliberately absent.

`common/decisions/categories/019_infantry_spawn_decision_categories.txt:11-18` uses that shared gate and sets `visible_when_empty = no`.

`common/scripted_triggers/019_infantry_spawn_triggers.txt:184-187` disables ordinary automatic generation whenever global Evolution III is active or the country suppression flag is present.

`common/scripted_effects/019_infantry_spawn_evolution_effects.txt:953-960` also stamps `infantry_spawn_automatic_generation_suppressed` when Evolution III is applied to a country.

Therefore an evolved ordinary country with no enumerated crisis, live lot, claimant, deferred action, operation, or cooldown has a false category gate while new ordinary automatic spawning is suppressed.

`common/scripted_triggers/019_infantry_spawn_triggers.txt:695-703`, `common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt:10-14`, and `common/decisions/019_infantry_spawn_decisions.txt:10-24` reuse the same lifecycle contract for gameplay actions and the Board doorway.

This satisfies the requested ordinary decision-category closeout behavior.

### Claimant takeover passes

`common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt:204-235` performs the selected-character proof and takeover effects.

The success branch sets `infantry_spawn_claimant_takeover_complete` at line 219 and calls `infantry_spawn_muster_board_close` at line 220.

The category gate rejects the completed-takeover flag at `common/scripted_triggers/019_infantry_spawn_triggers.txt:147`.

The claimant close effect therefore occurs on the successful takeover branch and is aligned with the documented lifecycle.

### Derivative closure occurs too early to be called success-gated

`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:475-597` owns common derivative package initialization.

After the common initializer sets `infantry_spawn_derivative_package_initialized`, it scopes to the former parent and immediately calls `infantry_spawn_achievement_mark_claimant_or_derivative_revolt` and `infantry_spawn_muster_board_close` at lines 542-545.

The achievement helper sets the parent flag `infantry_spawn_achievement_revolt_history` at `common/scripted_effects/019_infantry_spawn_achievement_effects.txt:556-558`, and the category gate rejects that flag at `common/scripted_triggers/019_infantry_spawn_triggers.txt:148`.

The exact multi-state transaction does not set `infantry_spawn_natural_derivative_revolt_succeeded = 1` until the later final ownership, control, core, source, and accounting proof at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:5310-5331`.

The one-state same-tag transaction likewise does not set success until its later validation at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:5491-5522`.

`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:5105-5124` explicitly handles a post-commit finalization failure after common package work by leaving both countries locked and marking invariant failure.

No transaction-local failure path clears the already-written parent revolt-history flag; the only located clear is the broad achievement-history cleanup at `common/scripted_effects/019_infantry_spawn_achievement_effects.txt:1125`.

Successful derivatives do close the category, so the visible terminal result is present.

The implementation does not match the stronger documentation claim that the completed or successful derivative outcome owns the closure, because a later failed and quarantined finalization already stamped the same persistent revolt-history disqualifier.

This also changes achievement eligibility semantics, because `infantry_spawn_achievement_revolt_history` is a persistent disqualifier used by the closeout achievements.

The implementation owner should move or positively confirm the parent terminal marker at the existing proved-success commit points.

If post-commit quarantine is intentionally terminal for the ordinary UI, it should use an explicitly documented failure-state gate rather than record a successful revolt history that did not pass the final success proof.

### Quiet Board flag can remain stale

`common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:531-540` clears an invalid open Board only when `infantry_spawn_muster_board_refresh_if_open` is called.

The located callers of that helper are Board action transactions in the same file.

No general mission completion, deferred replay, lot teardown, or category-transition path calls it.

`common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:16-20` prevents the stale Board from remaining visible because `infantry_spawn_muster_board_is_available` becomes false.

The country flag `infantry_spawn_muster_board_open` can nevertheless remain set after passive quiet closeout.

This is not a failure of the requested decision-category visibility, but it contradicts the lifecycle handoff's stronger statement that quiet closeout closes the Board and can cause a later renewed crisis to reopen the Board implicitly instead of through the doorway decision.

## Accepted-plan and handoff disposition

| Authority | Disposition |
| --- | --- |
| `019_ordinary_management_category_lifecycle_handoff_2026_07_29.md` | Accepted for the shared category gate, `visible_when_empty = no`, claimant close, evolved quiet category closeout, and player/AI gate parity. Not accepted as completion proof for success-gated derivative closure or passive Board-flag cleanup. |
| `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_7_decisions_ui_ai_balance.md` | The category lifecycle requirements are promoted into the source specification, but the successful-derivative wording is only partially implemented. |
| `docs/systems/chaos_unit_family_registry.md` | The external one-row/provider-callback architecture remains valid. Its completion-status paragraph predates the latest selection change and cannot establish that current providers participate in ordinary automatic generation. |
| Latest `core_effects` and shared registry-trigger diffs | No current implementation handoff or accepted-plan disposition was located. The lifecycle handoff's changed-file list does not mention either registry file. |
| `019_final_completion_audit_2026_07_18.md` and derived “no closure gate remains” statements | Historical for this incremental scope. They predate the 2026-07-29 registry and category changes and do not supersede the open findings in this audit. |

## Documentation gaps

`docs/events/019_infantry_spawn.md:597-599` correctly describes quiet category closeout and claimant closure, but “a successful derivative revolt closes” is stronger than the current initialization-time marker.

`docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_7_decisions_ui_ai_balance.md:29-35` correctly states the evolved quiet-closeout contract.

The lifecycle handoff calls `infantry_spawn_achievement_revolt_history` a completed parent-side revolt marker even though source stamps it before final success proof.

`docs/systems/chaos_unit_family_registry.md:13-33` still presents the pre-incremental registry audits as current completion proof and says no closure gate remains.

The shared registry document does not explain the new distinction between row policy, `chaos_unit_family_candidate_eligible`, and the `chaos_unit_family_candidate_native` receipt now required by ordinary automatic generation.

No asset manifest, GFX handoff, localisation, event-log, evolution-detail, or workbook change is required merely to correct these two gameplay contracts.

If player-facing descriptions change during remediation, localisation and the Event 19 catalog must be rechecked at that time.

## Meaningful validation performed

The audit read the mandatory offline wiki references for events, decisions, effects, triggers, scopes, on-actions, ideas, AI, localisation, data structures, units, divisions, and equipment.

It also read the official vanilla decision, effect, trigger, and script-concept documentation and compared the transient category pattern with vanilla categories that combine a dynamic `visible` gate and `visible_when_empty = no`.

The audit traced both weighted registry passes, the provider-ID callback dispatch, all three current registration rows and eligibility callbacks, the selected-row spawn dispatch, the category and Board gates, the claimant takeover branch, the common derivative initializer, both final derivative success branches, and the post-commit failure quarantine.

A static eligibility truth table was evaluated:

| Country context | Provider 501 | Provider 502 | Provider 503 | Automatic selector result |
| --- | --- | --- | --- | --- |
| Ordinary Event 019 country at Evolution IV | `eligible = 1`, `native = 0` | `eligible = 1`, `native = 0` | `eligible` may be 1 after its industrial gate, `native = 0` | No current provider row selected |
| Matching parent actor or matching derivative | `native = 1` only for zombie context | `native = 1` only for Death/ghost context | `native = 1` only for KMB/golem context | Matching provider can be selected |
| Future external provider with a valid neutral row and callback that sets `native = 1` | Provider-owned result | Provider-owned result | Provider-owned result | Structurally selectable without an Event 19 family-list edit |

The existing lifecycle handoff records a read-only `hoi4.event_inspect` state-flow artifact for `infantry_spawn_claimant_takeover_complete`.

This audit did not repeat that inspection because direct source establishes the claimant branch, while the open findings depend on provider callback receipts and derivative effect ordering outside that artifact's stated scope.

No live in-game validation was run because live consumer validation belongs to the user under repository rules.

## Required validation after remediation

1. Prove that an ordinary non-zombie, non-Death, non-KMB Event 019 country can select each current registered provider through the same aligned-row loop, without an Event 19 family enumeration.
2. Register one external neutral-profile test provider through its own registration effect and startup surface, then prove discovery, positive weighting, template build, spawn, ledger ownership, and cleanup without modifying Event 19 selection code.
3. Re-run a claimant takeover trace and confirm the category gate is false and `infantry_spawn_muster_board_open` is clear only after the successful takeover branch.
4. Re-run both multi-state and one-state derivative transactions and confirm the former-parent terminal marker and Board close occur after the final success proofs, while pre-commit recovery and post-commit quarantine preserve truthful failure history.
5. Exercise an Evolution III or IV quiet closeout reached through a passive mission completion or deferred replay and verify both category invisibility and explicit Board-open flag cleanup.
6. Update the registry and lifecycle handoffs with changed files, identifiers, the eligibility truth table, final-success ordering evidence, and any remaining limitations before requesting another completion audit.

## Simplifications, omissions, and blockers

No fallback or substitute was approved or introduced by this audit.

The current implementation contains two undisclosed simplifications:

- current-provider “eligibility” is only documentary or structural for ordinary automatic generation because the consumed native receipt remains false;
- derivative closure uses package initialization as a proxy for final revolt success.

The quiet category itself is implemented, but explicit passive Board-flag cleanup is omitted.

There is no external blocker to correcting these issues.

The remaining blocker is implementation and subsequent independent re-audit.
