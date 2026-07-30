# Event 012 diaspora owner protocol

The diaspora owner protocol makes the selected target the source of consent for voluntary return, housing, veterans, investment, citizenship, representation, and emergency evacuation actions. The host keeps the quote and resumes the normal action path only after the target accepts or accepts negotiated safeguards. Refusal closes the quote, and withdrawal cancels an active action without moving a population or changing a country's tag, borders, or relationship state.

## Helper map

`africa_diaspora_initialize_host_ledger` and `africa_diaspora_initialize_target_ledger` create explicit host capacity and target evidence ledgers.

`africa_diaspora_validate_target_capacity`, `africa_diaspora_prepare_target_response`, and `africa_diaspora_resume_pending_action` gate the existing action begin path without changing its quote, payment, mission, or generation logic.

`africa_diaspora_accept_target_request`, `africa_diaspora_request_counterterms`, `africa_diaspora_refuse_target_request`, and `africa_diaspora_withdraw_active_action` are target-owned response effects.

`africa_diaspora_apply_current_outcome` dispatches full, partial, and failure proof after the shared matrix semantics. Full branches write citizenship, representation, capacity, skills, safe evacuation, and locally owned project evidence. Failure branches restore capacity, clear consent where a fresh answer is required, and write the exact Event 012 achievement disqualifiers exposed by the existing achievement triggers.

## Constants and tuning

`common/script_constants/012_africa_diaspora_constants.txt` centralizes capacity lanes, trust deltas, protected local ownership, withdrawal timing, and AI response weights. The action matrix remains the source of truth for action costs, durations, risks, and outcome probabilities.

Passage and veterans use the passage lane, housing uses the housing lane, bonds use the investment lane, and emergency evacuation uses the emergency lane. Failed actions return their lane; full and partial results consume it.

## Event targets and cleanup

The host saves `africa_diaspora_request_host` and the selected target as `africa_diaspora_request_target` for the short consent chain. The resume and cancel effects clear both regular targets after the ordinary action path has either restarted or closed.

Active target-owned actions schedule one delayed withdrawal review. Shared action cleanup clears that review state before active generation variables are removed. Cancellation clears standing consent and emergency state, applies the withdrawal trust delta, and reuses the existing action mission and capacity cleanup.

## UI and assets

The protocol reuses `GFX_report_event_generic_conference`; no new icon, portrait, flag, sprite, or `.gfx` registration is required. The event localisation lives in `localisation/english/012_africa_diaspora_protocol_l_english.yml` and is UTF-8 with BOM.

## Future extension

Future work can expose the host capacity and target ledger values in the existing Charter League GUI. Such a surface should read the saved host variables and target flags and must preserve the same target-owned response gate.
