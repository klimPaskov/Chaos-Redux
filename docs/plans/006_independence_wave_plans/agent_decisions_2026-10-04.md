# Event 006 agent decisions, 2026-10-04

The user granted the implementing agent full design authority for the Event 006 takeover.
Each entry below is an agent decision taken under that authority, with its basis and the implementation that carries it.
Disposition labels follow `CLAUDE.md` Specs and Plans.

## D1. AI weights for the package focus groups (TRA, BOS, MAC, KAR, CRI, KUB, TAT)

Disposition: `implemented`.

Basis: the lead's round-1 list named 35 package focus-group `shared_focus` nodes in `common/national_focus/006_independence_wave_focus.txt` without `ai_will_do`, so they fell back to the engine default of 1 while every other node uses the `independence_wave_focus_ai` scale.

Decision:

- Every package group uses only `independence_wave_focus_ai` constants; no new constant was needed.
- The opening node of each group is `urgent` and gets `strong_preference_factor` while the package founding mission is active (`has_active_mission` on the package's own mission) or Event 006 instability is severe (`has_independence_wave_severe_instability`).
- The second node of each REG-03/REG-04 group is `high` and gets `preferred_factor` under the same founding condition.
- For the mutually exclusive civic and security branches of TRA, BOS, MAC, KAR, CRI and KUB, the branch whose paid project has already been completed gets `strong_preference_factor`, because it then earns the companion bonus and, for KAR, CRI and KUB, is the only branch that unlocks the capstone docket.
- The opposite branch gets `avoid_factor` once the other branch's paid project is complete and its own is not, so the AI does not strand its capstone or forfeit the companion bonus.
- With no paid project done, the civic branch is preferred under the constitutional, popular-council or traditional route, and the security branch is preferred under the emergency-military route and strongly preferred under a severe host threat.
- Each capstone docket is `high`, preferred while the founding mission is active and preferred again once the package's own route government is installed, so the capstone follows the package route.
- TAT opens with `urgent` and strong preference during the 720-day compact mission or severe instability; both founding branches are `high` with strong preference during the mission, so the AI fits the founding path inside the mission window.
- TAT nodes already bypass when their paid alternative completes and are unavailable while that alternative runs, so no extra avoid factor was added there.

Validation: a focus-file scan reports 78 shared focuses and 0 without `ai_will_do`; brace balance is 0.

MCP route evidence: `hoi4.probability_inspect` with `adapter = national_focus_ai_will_do`, `source = { path = common/national_focus/006_independence_wave_focus.txt }` and a two-to-three-id candidate pool returned `INTERNAL_ERROR` (artifactCount 0) both before and after the edit; `source = { relativePath = ... }` is rejected by the schema.
The probability baseline and comparison are therefore recorded as an unavailable route, not as evidence.

## D2. Foreign reactions step 1: frozen diplomatic counterparts and shared bilateral receipts

Disposition: `implemented`.

Basis: the accepted contract `docs/specs/006_independence_wave_specs/specs/006_foreign_reactions_and_remnant_petitions_contract.md` (Shared bilateral transactions) names this as the first implementation step.

Decision:

- Paid targeted diplomacy freezes its counterpart when the decision is taken: DM-11 `independence_wave_send_diplomatic_mission`, DM-12 `independence_wave_request_former_host_recognition`, DM-13 `independence_wave_seek_regional_guarantee` and DM-34 `independence_wave_grant_base_or_transit_rights` store the selected capital's owner, the payer as the released country and the payer's `independence_wave_generation_id`; DM-16 `independence_wave_coordinate_recognition_campaign` stores the endorsed member and that member's generation.
- Settlement reads only the frozen receipt through `has_valid_independence_wave_diplomatic_counterpart` (counterpart alive, not the payer, not at war with the payer, released-country generation unchanged) and never the later owner of the selected state; an invalid receipt ends the mission without effect.
- DM-12 additionally requires the counterpart still to be the living former host and the host outcome still to be unsettled at settlement, so a host-response recognition during the mission cannot be paid twice.
- One recognition receipt and one guarantee receipt per released country and actor are stored as tag-targeted variables (`independence_wave_recognized_by_generation_@TAG`, `independence_wave_guaranteed_by_generation_@TAG`) valued with the released country's generation, with bounded actor arrays for cleanup in `independence_wave_cleanup_decision_layer`.
- Recognition writers that share the receipt: DM-11 success, DM-12 success, DM-16 endorsement and DM-39 `independence_wave_recognize_new_independence_wave_country`; DM-11 and DM-39 show a localised blocked requirement when the receipt already exists, and DM-11 settlement awards nothing when a receipt appeared during the mission.
- Guarantee writers that share the receipt: DM-13, DM-34 and DM-44 `independence_wave_rescue_threatened_member`, all through `independence_wave_apply_bilateral_guarantee`, which creates the engine guarantee only when neither the guarantee nor the receipt exists; DM-13 awards its Statehood values only when that call created the guarantee.
- DM-42 League collective recognition stays a League action and does not write a bilateral receipt, because the League, not one member, endorses the target.
- DM-34 joins `has_independence_wave_active_diplomatic_action`, so it can no longer overlap another paid diplomatic action and the single frozen-counterpart slot cannot collide.
- League decisions DM-42/43/44/60/62 also freeze the target's generation (`independence_wave_active_league_target_generation`) and fail their validity check when the target tag is re-released.
- `has_independence_wave_pending_transaction_with_actor` and `has_independence_wave_pending_endorsement_for_target` expose an already-paid active transaction for a pair so the foreign layer settles or defers instead of charging twice.
- All costs and affordability helpers are unchanged; each settlement shows one localised outcome tooltip and the arithmetic runs hidden.

MCP route evidence: `hoi4.decision_inspect` (inventory, id `independence_wave_seek_regional_guarantee`) returned `DECISION_ANALYZED_PARTIAL` at source revision `d5099b86e10526f57c3eedba7fef566dcf9024e5246c6b8e0d5aea1b7e484315` with 218 unresolved definitions, the same count as the 2026-09-27 baseline, so the new helpers added no unresolved reference; `mode = inspect` without a scenario is rejected by the schema.
Needs live game: tag-targeted variable resolution inside `PREV`/event-target scope chains and the hidden settlement branches.
