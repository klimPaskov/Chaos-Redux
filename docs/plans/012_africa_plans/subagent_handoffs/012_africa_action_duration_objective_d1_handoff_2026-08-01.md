# Event 012 Africa action duration/objective D1 handoff

## Scope and disposition

This tranche owns the 102-row action-duration/objective contract, the four shared targeted action missions, the existing offer-response delay, the related English launch tooltip, and the `action_concept` rows in `012_africa_acceptance_ledger.csv`. It does not change event 210, country packages, focus trees, assets, the workbook, or other Event 012 systems. No fallback or broad mechanic redesign was introduced.

All 85 `queued_with_owner` action-concept rows are now `implemented` in the acceptance ledger. The five previously implemented instant rows remain implemented, and the twelve rows marked `blocked_with_gate` (73-76 and 85-92) remain blocked because their existing package gates are outside this tranche. The ledger's other surfaces were not edited.

## Helper map

| Helper or call site | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `africa_prepare_action_contract` | Host/temporary profile; reads `africa_requested_action_id` after `africa_prepare_action_profile` selects family, kernel, phase, target mode, and shared duration band. | Writes row-specific minimum, maximum, nominal, response-window, and objective profile fields from `constant:africa_action_contract`. | End of `africa_prepare_action_profile`; therefore existing player, AI, quote refresh, and revalidation paths all receive the contract. |
| `africa_requote_selected_action_against_action_target` | Host quote rebuild against the exact saved target. | Persists `africa_quote_duration_minimum`, `africa_quote_duration_maximum`, `africa_quote_duration_days`, `africa_quote_response_days`, and `africa_quote_objective` alongside the existing cost/risk snapshot. | Existing refresh/requote path; no new selector or target path. |
| `africa_create_action_record` | Host after payment and target revalidation. | Copies the quote fields to target-scoped active variables and snapshots `africa_active_action_started_at_war`; the pre-existing `africa_action_record_active` target gate prevents same-target concurrent overwrite. | Existing `africa_begin_quoted_action_against_target` launch path. |
| `africa_action_objective_is_complete` | Targeted mission target; requires active current-generation record. | Completes only peace-or-timeout rows after a target that started at war reaches peace, or the intervention preparation row when the target is at war with ROOT. Offer rows use their delayed response event; other rows remain timeout/callback driven. | `available` on all four shared action missions. |
| `africa_action_contract_should_cancel` | Targeted mission target. | Cancels capitulated or lost targets through existing `africa_cancel_action` and idempotent cleanup. | Added to each existing mission `cancel_trigger`, preserving event-active and generation guards. |
| `africa_cleanup_action` additions | Target after resolution or cancellation. | Clears every new active duration/objective/start-war variable, while existing mission flags, arrays, state project flags, reservations, and cooldown cleanup remain unchanged. | Existing resolve/cancel cleanup path. |

## Constants and tuning

`common/script_constants/012_africa_action_constants.txt` adds `africa_action_objective` (`none`, `peace_or_timeout`, `response_window`, `invalid_target`, `war_preparation`, `review_window`, `terminal_gate`) and `africa_action_contract`. The contract declares minimum, maximum, nominal, and objective values for every action key in matrix order. Bounded nominal values are deterministic integer midpoints; qualitative `ongoing with annual review`, `multi-year`, `campaign-ending`, and long-preparation rows use explicit bounded defaults. The existing `africa_action_duration_band` remains the mission routing enum and is not repurposed.

## Mission and response wiring

`mission_africa_action_short`, `mission_africa_action_medium`, `mission_africa_action_long`, and `mission_africa_action_epic` now use the vanilla scoped mission form `days_mission_timeout = FROM.africa_active_action_duration_days`. This preserves one bounded mission ID per band while allowing each target record to retain its own duration. The existing mission arrays and duration flags remain unchanged. Offer-response action 210 is scheduled with `days = africa_active_action_response_days` inside the existing target scope; its options and outcome callbacks remain in `events/012_african_union.txt`, which is intentionally untouched.

Same-target concurrency is safe under the existing launch guard (`event_target:africa_action_target = { NOT = { has_country_flag = africa_action_record_active } }`) and the bounded active-target array. A target cannot receive a second action record until the first record's cleanup clears its timer snapshot and record flag. Different targets retain independent active duration variables even when they share a mission ID.

## Files changed

- `common/script_constants/012_africa_action_constants.txt`
- `common/scripted_effects/012_africa_action_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/decisions/012_africa_decisions.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa/action_duration_objective_contract.md`
- `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv` (action-concept rows only)
- This handoff file.

## Validation evidence

- Static profile dispatch count: 102 action IDs in `africa_prepare_action_contract`.
- Static contract count: 102 `_default_days` entries and matching min/max/objective references; no missing constant references and all objective values are in the declared enum range.
- Balanced braces and no unsupported `<=`/`>=` operators in the touched script files; no accidental `+` patch lines remain.
- Mission syntax audit confirms four `days_mission_timeout = FROM.africa_active_action_duration_days` call sites and no `var:FROM` or `var:africa_active_action_response_days` forms. Vanilla scope precedents were read from `ETH`, `SOV`, `JAP`, and `CHI` decision files plus the official script-constant and effect documentation.
- Acceptance ledger audit: 90 action rows are `implemented`, 12 remain `blocked_with_gate`, zero action rows remain `queued_with_owner`, and no stale fixed-band timer sentence remains in implemented action rows.
- Read-only Event Chain Viewer trace for `chaosx.nr12.210` returned `EVENT_INSPECTED_PARTIAL` with no direct blockers. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/04f1729452f15ed65060507f7b9664587c2179811395443e7c5ee735625b4ccb/564425f3736d636027a8f9d8a7182113b1f7fdb35cf5a29ecbab873f9f87ae94/event-trace-cd94999c0ae5.json`.

## Skipped checks and limitations

- Hearts of Iron IV was not launched. Live mission timer parsing, target-scoped duration evaluation, delayed event persistence, save interruption, and in-game tooltip rendering remain parent/user runtime checks.
- The MCP trace is workspace-partial (`MCP_INLINE_FILES_TRUNCATED`) and reports workspace-wide unresolved diagnostics; it is evidence of the existing event 210 route only, not a complete Event 012 lint pass.
- `response_window` is a contract class for the eight existing offer rows; their response event is delayed, but the event source remains parent-owned and its option probabilities were not changed.
- The matrix's recurring annual-review, multi-stage, terminal, and project-specific completion semantics are represented by explicit duration/objective values but retain the existing timeout/result kernels where no external success setter exists. Adding those predicates would require a separate mechanic design and call sites.
- The four shared host duration variables in `common/scripted_effects/012_africa_effects.txt` remain for unrelated legacy surfaces; this tranche does not rewrite them because target records now own the mission timer.

