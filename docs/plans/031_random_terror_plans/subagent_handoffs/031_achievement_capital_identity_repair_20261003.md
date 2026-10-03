# Event 31 achievement capital identity repair

## Disposition and acceptance basis

Disposition: implemented in the working tree, with engine and specialist evidence still incomplete.

The active user goal requires exact states, multiplayer-safe achievement handling, and exploit controls.

The accepted achievement prompt requires The City Still Stands to retain its capital, War Without a Capital to recover its original capital within one year, and Maximum Survivor to preserve or restore the capital captured at scenario confirmation.

## Changed source and behavior

Changed file: `common/scripted_effects/031_random_terror_achievement_effects.txt`.

The old generic state flag `random_terror_achievement_original_capital` identified a capital without identifying the country that recorded it.

The ledger stores `random_terror_achievement_original_capital_state` on the government when its achievement ledger is initialized.

The variable contains the persistent state reference returned by the documented `capital` game variable.

The loss callback compares its exact lost-state target with that government's stored state reference.

Retaking and restoration callbacks credit the current owner only when the restored state equals that owner's recorded original capital.

The City Still Stands requires the current capital to equal the recorded state and requires that state to remain owned and controlled by the tracked government.

War Without a Capital requires the recorded original state to be currently owned and controlled by that government when the completion predicate is reached.

Maximum Survivor stores a separate `random_terror_achievement_maximum_original_capital_state` at valid Maximum scenario confirmation and checks current ownership and control of that state.

Scenario confirmation does not overwrite the government's earlier ordinary-crisis capital identity.

The capital recovery deadline is created only on the first recorded loss.

Repeated loss does not extend the deadline and clears retaking and restoration proof, so a previous recovery cannot satisfy a later loss without another recovery.

No tuning value, AI weight, target weight, cost, threshold, asset, or player-facing requirement was changed.

## Helper contract

| Helper | Scope | Inputs | Output and side effects |
| --- | --- | --- | --- |
| `random_terror_achievement_initialize_country` | Country | Documented `capital` scope variable | Captures the government's original state once with the existing ledger initialization. |
| `random_terror_achievement_record_state_loss` | Former government | Exact `event_target:random_terror_achievement_lost_state` | Matches the recorded capital, records loss, starts the first-loss deadline, and invalidates recovery proof on another loss. |
| `random_terror_achievement_record_original_capital_retake` | State | Current OWNER and its recorded state reference | Credits only that owner's matching capital. |
| `random_terror_achievement_record_civil_authority_restore` | State | Current OWNER and its recorded state reference | Records restoration only for that owner's matching capital. |
| `random_terror_achievement_record_scenario_launch` | Confirming player country | Existing valid UI launch, type, and Maximum intensity proof | Captures a separate scenario-start capital reference. |
| `random_terror_achievement_finalize_country` | Country | Existing achievement proof plus recorded state references | Requires current ownership/control for the three capital-dependent achievements. |
| `random_terror_achievement_daily_tick` | Country | Ordinary capital reference and current `capital` | Identifies a different controlled backup capital and disqualifies the city run if its identity is missing or no longer matches. |

Missing stored identities fail closed rather than reconstructing an original capital from shared state flags.

The state reference persists with the country ledger and is not a temporary event target.

## References read

The connected MCP tool list did not expose the four reference lookup routes named by AGENTS.md, so these pertinent local sections were read directly.

| Reference | Section | SHA-256 revision |
| --- | --- | --- |
| `documentation/dynamic_variables_documentation.md` in the installed game | Lines 174–190, `capital` | `538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA` |
| `documentation/effects_documentation.md` in the installed game | Lines 7888–7913, `set_variable` | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| `documentation/triggers_documentation.md` in the installed game | Lines 2110–2145, `check_variable`, and 6079–6094, `is_owned_and_controlled_by` | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | Lines 439–456, persistent variable scoping and scope references | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | Line 1847, state ownership and control predicate | Offline snapshot |

The installed vanilla RAJ scripted-trigger precedent uses a scope-valued `THIS` entry, and the installed AST, SWI, and shared scripted-effects precedents use scope-valued `PREV` entries.

The existing Chaos Redux Fallout and Random Civil War effects also persist state pointers and use them through `var:` scopes.

## Parent review and validation limits

The parent reviewed every original-capital reference in the achievement effect file and the retaking/restoration call sites in `031_random_terror_effects.txt`.

The original state flag has no remaining runtime reads or writes in the achievement file.

The ordinary government reference and the Maximum scenario reference have separate capture points.

The source checks enforce these cases:

- A restored state recorded by another government cannot credit the current owner's capital achievement.
- A recaptured matching capital can credit its original government.
- Another loss clears recovery proof and leaves the first-loss deadline unchanged.
- Maximum scenario confirmation retains its own capital independently from earlier ordinary-crisis tracking.
- A country lacking the recorded state cannot satisfy a capital-dependent completion predicate.

These are source-contract findings, not observed live-game outcomes.

The fresh MCP event lint route failed during the preceding pass with `timed out awaiting tools/call after 600s`.

The full achievement architect failed before execution with `workspace routing discovery timed out`.

No live save/reload or multiplayer result is claimed.

## Remaining work

The global tag-switch disqualification and player-specific origin-to-destination transaction remain unresolved.

The complete twelve-achievement audit, valid/invalid outcome scenarios, and final engine evidence remain open.

The previous count-repair commit's real-index reconciliation succeeded after the shared lock cleared.

The capital-identity repair has a separate, reviewed commit scope containing only its source file and this handoff.
