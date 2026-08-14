# Event 006 DM-01 material-cost repair receipt — 2026-08-14

## Disposition

The accepted Part 3 contract is at `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md:411-438`. Vanilla `effects_documentation.md:1252-1265` states that `add_equipment_to_stockpile` removes equipment when `amount` is negative, so a positive amount would be a real add-versus-spend defect.

The current worktree already contains the narrow repair. Every DM-01 payment amount in `independence_wave_decision_pay_provisional_capital` is a negative `constant:independence_wave_decision_cost.*_spend` token, and the corresponding constants are negative. `HEAD` does not contain this helper at all, so the positive pre-repair version cannot be reconstructed from committed history. This subagent therefore made no gameplay edit and did not overwrite the concurrent source changes.

## Severity-sorted findings

1. **P1, resolved in the live worktree:** a positive stockpile amount would grant equipment instead of charging the accepted material commitment. The current helper uses `-250/-500/-1000` infantry spends, `-50/-100/-200` support spends, and `-10/-100` isolated-capital transport spends through named script constants.
2. **P2, evidence limitation:** the probability adapter can inspect the mission AI source but cannot construct a runnable DM-01 mission from empty typed country, capital, force, equipment, and transport fixtures. No quantitative AI or timing claim is made.
3. **P2, evidence limitation:** shared `independence_wave_status_window` GUI inspection and rendering expose global graph truncation and pre-existing overlap or unresolved diagnostics. DM-01 has no dedicated GUI change in this repair, so no rewrite was warranted.
4. **P3, minor clarity gap:** the automatic mission description names the force-tier material categories and transport alternative but does not display exact quantities. It is intentionally not a selectable decision and has no custom cost triplet. Adding a player-click cost widget would exceed this narrow repair.

## Cost and requirement parity

| Branch | Availability gate | Payment token | Runtime payment |
| --- | --- | --- | --- |
| Fragile | Infantry `> 249`, support `> 49` | `infantry_light_spend`, `support_light_spend` | Removes 250 infantry and 50 support equipment |
| Viable | Infantry `> 499`, support `> 99` | `infantry_standard_spend`, `support_standard_spend` | Removes 500 infantry and 100 support equipment |
| Armed or high chaos | Infantry `> 999`, support `> 199` | `infantry_major_spend`, `support_major_spend` | Removes 1000 infantry and 200 support equipment |
| Missing force-level variable | Infantry `> 499`, support `> 99` | Standard spend tokens | Removes the standard tier |
| Capital with no supply node and train available | Train `> 9` | `provisional_capital_train_spend` | Removes 10 trains |
| Capital with no supply node and no qualifying train | Motorized `> 99` | `provisional_capital_motorized_spend` | Removes 100 motorized equipment |

The strict `>` gates sit one unit below the exact spend, so an exact stockpile qualifies and is then charged without using unsupported unary negative variable syntax. A supplied capital bypasses transport entirely. An isolated capital chooses train first and motorized only when the train gate fails. The equipment types are vanilla-supported `infantry_equipment`, `support_equipment`, `train_equipment`, and `motorized_equipment`.

## Decision lifecycle and mission quality

- **Owner:** every released country, as required by the Part 3 spec.
- **Category and region:** `independence_wave_founding_category`, with the capital state as the operational region.
- **Entry:** `independence_wave_refresh_country_state` calls `independence_wave_start_provisional_capital_mission`; the starter requires active package setup, controlled capital, garrison satisfaction, all material gates, no prior success or failure, no reservation, and no active DM-01 mission.
- **Mission mode:** `independence_wave_secure_provisional_capital` remains automatic. `activation = { always = no }`, `available = { always = no }`, and there is no `selectable_mission = yes`.
- **Duration:** the 75-day base remains in the decision. Fragile subtracts 45 days for 30 days, viable subtracts 30 days for 45 days, and armed or high-chaos remains 75 days.
- **Success:** timeout sets `independence_wave_dm01_capital_secured` and `independence_wave_dm01_capital_administration_ready`, applies the capacity, legitimacy, security, and instability deltas, and refreshes idea lifecycles.
- **Failure:** losing the capital or the required garrison, or leaving the active-country state, cancels the mission, marks failure and relocation state, applies the bounded failure deltas, refreshes ideas, and fires `chaosx.nr6.311`.
- **Duplicate risk:** reservation is set before payment, the active-mission check blocks a second starter, `fire_only_once = yes` remains, and cleanup removes the mission and clears reservation, success, failure, administration, and relocation flags.
- **Sunk cost:** payment occurs before `activate_mission` and is not repeated or refunded by cancellation, timeout, relocation, or cleanup.

## AI, route, localisation, and GUI notes

The mission retains its urgent AI weight, but its automatic activation path means that weight is not a player-selectable purchase score. No invalid target, dead-country target, route-lock, or DM-02-plus change was introduced.

`independence_wave_secure_provisional_capital` and its description are present in `localisation/english/006_independence_wave_decisions_l_english.yml`. The description communicates the duration band, force-tier garrison, equipment commitment, isolated-capital transport burden, and emergency relocation consequence.

The decision category uses the shared `independence_wave_status_scripted_gui`; this is not a named event-owned dedicated GUI. Read-only inspection and rendering were completed, and no GUI rewrite was applied.

## MCP evidence

- `hoi4.probability_inspect`, adapter `mission_ai_will_do`, current source hash `efc4d478e6f23c5c4b07f6b079d8296b138a0a17d774f5b7c2bc53c53e904035`, revision `7442bcad7bce47b835e38f12e1806232c1d8e65e7aa93103b269dfe8251decdb`, found 54 candidates and 42 required inputs with zero inspect-unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77b27b4d255ba80045e36501063d0abe9cde6801d314f9b48909133517487b11/56274611fcb203bf590a30bd94098a2b713881b5351563fed6ce635ef3057090/probability-inspect-efc4d478e6f2.json`.
- `hoi4.gui_inspect` for `independence_wave_status_window`, scenario `independence_wave_status_default`, completed with 48 inspected elements. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/954534e7a8b94d69bd7237aa9e2f090653a43d8644f528541426177177f52633/b469a521dea730c750786d7608704203d0b16e0660d0d4dcd9fe3749ecb0860b/gui-inspect.057fc56363e52f92.json`.
- `hoi4.gui_render` covered normal, active, warning, disabled, and long-text states at 1280x720 and 1920x1080. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7151f87950fd10f39ae7cf64c5dc04fee0744ed2835a3358531571452bcdae64/e5fce1901a1794d53c872a5e5aa50b0418c3742d6d39c4d66c78939fb7420f55/independence_wave_status_window-full.svg`.
- `hoi4.event_inspect` lint for `chaosx.nr6.311` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics. The large workspace pass deferred helper projections and lifecycle passes. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/876fd23310ccb8886ea172eabcd1a9701142ea234942d04ca6273bd6e024b066/01c262dbcf6c2101e5d3862e5f095c2232980623e1d09d743be0639a24a5f0a5/event-lint-d21fdfa2723e.json`.

## Static validation

- Extracted the DM-01 payment block and found ten amount statements, all matching `constant:independence_wave_decision_cost.*_spend`; every expected force-tier and transport token is present.
- Parsed all eight spend constants and confirmed they are negative. Parsed all eight gate constants and confirmed they are one below the matching displayed commitment.
- Confirmed trigger references cover fragile, viable, armed, high-chaos, missing-force-level standard fallback, supply-node bypass, train, and motorized branches.
- Confirmed brace balance in the scoped trigger, effect, and decision files and confirmed definition and call/reference coverage for the DM-01 helpers.
- Confirmed decision lifecycle keys and the starter's reservation plus `activate_mission` call.
- Vanilla documentation and precedents were checked for negative equipment removal, `activate_mission`, mission timeout adjustment, and the train or motorized equipment archetypes.

## Source hashes and ownership

These are current worktree hashes for the concurrent gameplay edits, not changes made by this subagent:

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`: `2a94a7012293d2ee2d30301d71133402880968ca`.
- `common/scripted_effects/006_independence_wave_decision_effects.txt`: `730e0404cf26ade65b22c1ca78f7d383aa6a991d`.
- `common/decisions/006_independence_wave_decisions.txt`: `925e37acff23c36878b466082c4e4bf29e52e7b0`.
- `common/script_constants/006_independence_wave_decision_constants.txt`: `31b961f2766ccaae48384509ced136c907635286`.
- `localisation/english/006_independence_wave_decisions_l_english.yml`: `804a44290ec8671cfe2d05af01cfaf6f15cca1b4`.

`HEAD` has no `independence_wave_decision_pay_provisional_capital` definition, so no committed positive-amount baseline exists for a before/after hash comparison. No DM-02-plus source was edited by this subagent. The only file added by this subagent is this handoff.

## Remaining risks and skipped validation

The current gameplay edits are uncommitted concurrent work and require the parent’s final integrated review. The probability adapter still needs non-empty typed fixtures for meaningful live-state balance evidence. GUI evidence is read-only and carries shared-window graph truncation and unresolved diagnostics. No live HOI4 launch was performed, as required by repository instructions. No `hoi4.gui_rewrite` or post-change GUI comparison was performed because this repair does not change GUI source. No commit was created.
