# Event016 DHR diplomatic reward closure plan

Status: the two paid-advisor contracts are accepted, promoted to the Alien Infantry and D’Rhonda specification, implemented, and reviewed in `subagent_handoffs/016_final_dhr_advisor_reward_implementation_2026-09-02.md`.
The four remaining diplomatic reward contracts are queued for owner implementation review; the Synod no-DLC accord alternative specifically awaits user approval.
The following findings describe the pre-implementation baseline, not a claim that all six rewards remain untouched.
The accepted advisor tranche preserves the 88-focus layout and has a corrected same-fixture MCP probability comparison in `subagent_handoffs/016_final_dhr_advisor_reward_probability_2026-09-02.md`.

## Priority findings

1. The six named DHR diplomacy focuses all call `dhrondan_focus_add_diplomatic_credit` and then set a focus-specific receipt flag. The helper only sets `dhrondan_diplomatic_credit_established` and grants `constant:dhrondan_focus_reward.political_power_small`; a repository-wide scan found no consumer of the credit flag or credit variable, so the repeated reward is an unowned PP/flag ladder rather than a gameplay consequence.

2. `DHR_exchange_maps_for_access` is not dead: `dhrondan_access_map_exchange_ready` is consumed by `dhrondan_focus_has_access_map_exchange`, which gates the existing Covenant compact decision. Older route-consumer notes that call this flag unused are stale and should not drive a second compact gate.

3. `DHR_choose_our_terrestrial_partners` currently leaves `dhrondan_terrestrial_partner_selection_open` as history only. It needs a separate, consented partner operation, because `dhrondan_is_valid_compact_partner` is deliberately Covenant-compact-specific, rejects existing NAP partners, and does not establish willingness to receive unilateral military or market access.

4. The existing `chaosx.nr16.49` event is the correct response/expiry surface for the new partner offer, but it currently means only a Two-World Compact. A positive offer-kind flag and kind-aware validation, text, cleanup, and report handling are required so a partner offer cannot accidentally use compact NAP, compact-concluded, or achievement effects.

5. `DHR_invite_the_enclave_congress` currently records `dhrondan_enclave_congress_invited` without protecting the shared integration decision. The integration decision already has the correct paid target operation (`50` PP and `60` days); it needs an authoritative route-contract gate so the receipt becomes a useful route-specific unlock without adding a new decision or branch.

6. `DHR_seat_the_human_delegates` and `DHR_open_the_translation_bureaus` have existing paid advisor consumers available for reuse, but their current advisor gates do not consume the focus receipts. The advisor gates should be tightened/broadened deliberately rather than adding free ideas, spirits, or modifier ladders.

## Scope and invariants

The implementation must preserve exactly 88 focuses, the existing three mutually exclusive regime roots, all existing focus IDs and coordinates, the existing focus AI weights until the probability owner completes a baseline, and the existing alien infantry/landing/contact APIs. It must not add a focus, branch, country, GUI, superevent, achievement, cohort reward, equipment loop, or new event ID.

The six focus IDs to preserve are:

| Focus ID | Current completion receipt | Current repeated reward | Planned consumer |
| --- | --- | --- | --- |
| `DHR_seat_the_human_delegates` | `dhrondan_human_delegates_seated` | `dhrondan_focus_add_diplomatic_credit` | Paid Covenant envoy advisor gate |
| `DHR_ratify_the_two_world_covenant` | `dhrondan_two_world_covenant_ratified` | `dhrondan_focus_add_diplomatic_credit` | Existing compact root gate |
| `DHR_open_the_translation_bureaus` | `dhrondan_translation_bureaus_open` | `dhrondan_focus_add_diplomatic_credit` | Paid translation/intelligence advisor gate in every regime |
| `DHR_exchange_maps_for_access` | `dhrondan_access_map_exchange_ready` | `dhrondan_focus_add_diplomatic_credit` | Existing compact gate plus partner-offer root gate |
| `DHR_choose_our_terrestrial_partners` | `dhrondan_terrestrial_partner_selection_open` | `dhrondan_focus_add_diplomatic_credit` | New paid, consented partner offer using `chaosx.nr16.49` |
| `DHR_invite_the_enclave_congress` | `dhrondan_enclave_congress_invited` | `dhrondan_focus_add_diplomatic_credit` | Route-specific paid integration contract |

The current generic helper should be removed from these six completion rewards only after a full common and generated-content scan proves that `dhrondan_focus_add_diplomatic_credit` and `dhrondan_diplomatic_credit_established` have no external contract. The six receipt flags remain authoritative state and are not to be deleted.

## Proposed reward contracts by focus

### 1. Human delegates: paid Covenant envoy unlock

Keep `dhrondan_human_delegates_seated` and remove only the unused credit helper from `DHR_seat_the_human_delegates` in `common/national_focus/016_dhrondan_focus_tree.txt`.

In `common/characters/016_dhrondan_characters.txt`, change the existing paid `DHR_harmonic_envoy_rae_syl` advisor availability to require both `dhrondan_covenant_route` and `dhrondan_human_delegates_seated`. Preserve its existing 100 PP cost, AI factor, trait `dhrondan_harmonic_envoy`, portraits, and localisation. The trait's existing improvement-relations upkeep reduction is the tangible effect; the focus does not grant a free hire or a new character.

The focus completion tooltip may use the existing advisor icon/tooltip pattern (`custom_effect_tooltip` plus `show_ideas_tooltip` where supported) with a new dedicated key such as `DHR_human_delegates_effect`, but localisation edits are deferred until parent acceptance. The focus remains Covenant-only, so no non-Covenant bypass is introduced.

### 2. Two-World Covenant ratification: authoritative compact gate

Keep `dhrondan_two_world_covenant_ratified` and remove the unused credit helper from `DHR_ratify_the_two_world_covenant`.

Add `has_country_flag = dhrondan_two_world_covenant_ratified` to the existing `dhrondan_offer_two_world_compact.target_root_trigger` in `common/decisions/016_dhrondan_country_decisions.txt`, after its existing Covenant, world-order, integration-started, and map-exchange requirements. Add one concise root tooltip if needed so direct/scripted calls explain that ratification is required.

This is an authoritative direct-call/save-state guard even though the normal graph already places `DHR_the_chamber_of_two_skies` behind ratification. It must not consume `dhrondan_terrestrial_partner_selection_open`, stack an unrelated partner gate onto the compact, or alter the existing `.49` compact response, NAP, stability, opinion, expiry, or AI semantics.

### 3. Translation bureaus: paid intelligence advisor unlock for all regimes

Keep `dhrondan_translation_bureaus_open` and remove the unused credit helper from `DHR_open_the_translation_bureaus`.

The focus is shared and has no regime prerequisite. In `common/characters/016_dhrondan_characters.txt`, make the existing paid `DHR_shadow_listener_thel_ior` advisor available only after `dhrondan_translation_bureaus_open` and one of `dhrondan_imperial_route`, `dhrondan_synod_route`, or `dhrondan_covenant_route`. Preserve the existing 100 PP cost, AI factor, trait `dhrondan_shadow_listener`, portraits, and localisation. Its current decryption and research-speed effects are the concrete consumer.

This intentionally broadens the current Synod/Covenant-only advisor gate because the existing focus is universal and promises translation capacity, while the advisor is the existing paid intelligence consumer. It does not add a new spirit or generic modifier ladder. If parent rejects broadening Thel on route-identity grounds, the only acceptable fallback is to gate an already all-regime paid advisor with the same receipt and document the changed effect before implementation; do not leave the shared receipt history-only.

### 4. Map exchange: preserve compact consumer and feed the independent partner lane

Keep `dhrondan_access_map_exchange_ready` and remove the unused credit helper from `DHR_exchange_maps_for_access`.

Do not replace or duplicate `dhrondan_focus_has_access_map_exchange`. The existing Covenant compact decision must continue to consume that trigger. The new partner operation described below also consumes the same receipt for all eligible regimes, so Imperial and Synod have a useful map/access consequence without changing the compact's Covenant-only meaning.

No new map flag, opinion ladder, stockpile reward, or compact prerequisite is needed. The map receipt means that DHR has exchanged the information required to make a targeted terrestrial offer; the offer still requires the target's explicit `.49` response.

### 5. Terrestrial partners: one paid, consented partner accord

Keep `dhrondan_terrestrial_partner_selection_open` and remove the unused credit helper from `DHR_choose_our_terrestrial_partners`.

Add one country-target decision, `dhrondan_offer_terrestrial_partner_accord`, to the existing `dhrondan_sovereignty_category` in `common/decisions/016_dhrondan_country_decisions.txt`. Reuse `GFX_decision_category_dhrondan_sovereignty`, `GFX_decision_dhrondan_two_world_compact`, and the existing `GFX_report_event_016_dhrondan_diplomatic_compact` picture. Do not create a category, icon, art asset, GUI, or event ID.

The root trigger should require `dhrondan_country_is_active`, no world end, `dhrondan_world_order_decisions_are_unlocked`, `dhrondan_focus_has_access_map_exchange`, `dhrondan_terrestrial_partner_selection_open`, no war, no active diplomatic offer, no concluded partner receipt, and one of the three existing regime flags. The cost should reuse `constant:dhrondan_decision_cost.diplomatic_compact` (75 PP). The operation should follow the existing immediate offer pattern, use the native `.49` response window (`13` days plus `1` day cleanup grace), and reuse the existing `constant:dhrondan_decision_duration.repeat_cooldown` (90 days) for retry protection. The currently declared 30-day compact duration is not used by the existing compact offer and should not be silently introduced here.

Add a distinct target trigger in `common/scripted_triggers/016_dhrondan_country_triggers.txt`, for example `dhrondan_is_valid_terrestrial_partner_candidate`. It should require that the target exists, is not DHR, is independent, is not capitulated, and is at peace with ROOT; it should allow an existing NAP, because the accord is not a compact and an existing NAP does not prove refusal. It must reject a target that already has `dhrondan_terrestrial_partner_accord_partner`, and the root must reject a second active offer. It must not call `dhrondan_is_valid_compact_partner`.

Before firing `chaosx.nr16.49`, set a positive kind flag such as `dhrondan_diplomatic_offer_partner_accord` on the actor. The absence of that flag remains the legacy/default compact kind. Extend `dhrondan_compact_response_is_valid` and `dhrondan_compact_response_can_commit` with explicit kind branches: the default branch must remain Covenant-only, no-war, no-NAP, no-existing-compact-partner behavior; the partner branch must revalidate the actor and recipient pointers, active/delivered/expiry state, no-world-end, actor independence/peace, and the new NAP-tolerant candidate trigger. This avoids inferring consent from the 75 PP payment.

Extend `dhrondan_clear_diplomatic_offer` in `common/scripted_effects/016_dhrondan_country_effects.txt` to clear the partner-kind flag along with the active/delivered/expiry/global-target state. The reconcile/watchdog helpers must preserve the kind while an offer is valid and clear it with a stale or invalid offer. Pointer checks must continue to ensure an old or mismatched popup cannot clear a newer offer.

Make `.49` kind-aware without adding an event ID. In `events/016_dhrondan_country_events.txt`, use conditional title/description blocks so the partner kind receives `chaosx.nr16.49.partner.t` and `chaosx.nr16.49.partner.d`, while the no-kind legacy path keeps `chaosx.nr16.49.t` and `chaosx.nr16.49.d`. Generic option labels such as “Accept the proposal” and “Decline the proposal” are preferable to labels that call every offer a compact; the default effect path remains unchanged. Reuse the existing picture and response timeout.

On partner acceptance, perform route-specific tangible actions only after the kind-aware `dhrondan_compact_response_can_commit` check succeeds:

| Regime | Consented action | Receipt/relation handling |
| --- | --- | --- |
| Imperial | DHR gives the selected target a guarantee and both countries grant reciprocal military access using the vanilla `give_guarantee`/`give_military_access` pattern. | Set root `dhrondan_terrestrial_partner_accord_concluded` and target `dhrondan_terrestrial_partner_accord_partner`; add one bilateral `dhrondan_terrestrial_partner_accord` opinion marker only if parent accepts its wording/value. |
| Synod | If `has_dlc = "Arms Against Tyranny"`, both countries receive reciprocal market access through `give_market_access`. | Set the same idempotent root/target receipts; do not add generic opinion-only reward. |
| Covenant | Both countries grant reciprocal military access and receive the explicit cultural/embassy agreement marker represented by `dhrondan_terrestrial_partner_accord`. | Set the same root/target receipts; preserve any pre-existing NAP rather than creating a compact NAP. |

The Synod no-DLC behavior needs parent choice before implementation. The recommended native fallback is reciprocal military access with a clear no-DLC tooltip, because it remains a meaningful access agreement without claiming a DLC-only market-access effect. If that fallback is not accepted, the decision must be unavailable when the DLC is absent, with the reason shown explicitly; do not silently substitute a market effect or grant unilateral access.

Partner acceptance must not set `dhrondan_diplomatic_compact_concluded`, `dhrondan_two_world_compact_partner`, or compact achievement receipts, and must not call the default compact NAP effect. A target's existing NAP is left intact. Refusal and expiry clear the kind flag and offer pointers without relation effects or partner receipts, then allow retry after the existing cooldown. Existing `.50`/`.51` IDs may be reused with conditional partner report text/effects, but their default compact reports must remain unchanged and no report may claim compact ratification for a partner accord.

Add only the required dedicated localisation keys in `localisation/english/016_dhrondan_country_l_english.yml` during implementation, keeping the file UTF-8 with BOM. The planned keys are `dhrondan_offer_terrestrial_partner_accord`, `dhrondan_offer_terrestrial_partner_accord_desc`, `dhrondan_terrestrial_partner_target_requirements_tt`, `chaosx.nr16.49.partner.t`, `chaosx.nr16.49.partner.d`, `dhrondan_partner_accord_imperial_accept_effect_tt`, `dhrondan_partner_accord_synod_accept_effect_tt`, `dhrondan_partner_accord_covenant_accept_effect_tt`, `dhrondan_partner_accord_refuse_effect_tt`, and `dhrondan_partner_accord_expired_effect_tt`. Reuse the existing event picture and decision icons.

### 6. Enclave congress: route-specific integration contract

Keep `dhrondan_enclave_congress_invited` and remove the unused credit helper from `DHR_invite_the_enclave_congress`.

Add `dhrondan_integration_route_contract_is_ready` to `common/scripted_triggers/016_dhrondan_country_triggers.txt` with this route-aware OR contract:

| Route | Required existing receipt |
| --- | --- |
| Imperial | `dhrondan_is_imperial_regime = yes` and `dhrondan_subject_world_protocol_ready` |
| Synod | `dhrondan_is_synod_regime = yes` and `dhrondan_optimal_order_administration_ready` |
| Covenant | `dhrondan_is_covenant_regime = yes` and `dhrondan_enclave_congress_invited` |

Use the helper in the existing `dhrondan_integrate_reclaimed_landing_site` root trigger, its `available` path through the authoritative `dhrondan_integration_decision_can_complete`, its `cancel_trigger`, and the completion guard. Preserve the existing `dhrondan_state_can_be_integrated` target validation, no-war guard, 50 PP cost, 60-day duration, core reward, and small war-support reward. Add a concise `dhrondan_integration_route_requirements_tt` tooltip. The normal route capstone already supplies the Imperial/Synod receipts, while the Covenant congress focus supplies its receipt, so this gate protects direct/repeated calls without deadlocking the intended graph.

## Route coverage

| Regime | Focus rewards that become live | Tangible route action |
| --- | --- | --- |
| Imperial | Shared translation receipt unlocks Thel; map receipt and partner-selection receipt unlock the partner offer; route contract keeps subject-world integration paid and gated. | A consented `.49` accord gives guarantee plus reciprocal military access; integration remains paid core conversion. |
| Synod | Shared translation receipt unlocks Thel; map receipt and partner-selection receipt unlock the partner offer; route contract keeps optimal-order integration paid and gated. | A consented `.49` accord gives reciprocal market access when the DLC exists, or the parent-approved native equivalent when it does not. |
| Covenant | Delegates receipt unlocks Rae; translation receipt unlocks Thel; map receipt continues to gate compact and also enables the partner offer; ratification receipt gates compact; congress receipt gates integration. | Compact remains the existing Covenant-only NAP/acceptance path; independent partner acceptance gives reciprocal military access and cultural/embassy agreement. |

No route gains a new focus, country, spirit, GUI, super-event, or achievement. No route receives free cohorts, free laser guns, or a recurring stockpile reward.

## Existing history versus unwired promises

The six focus-specific flags are legitimate historical receipts because each has either an existing consumer or a proposed narrow consumer that matches the focus title. `dhrondan_access_map_exchange_ready` is already consumed by `dhrondan_focus_has_access_map_exchange`; its older “unused” documentation row should be marked stale rather than patched around. `dhrondan_human_delegates_seated`, `dhrondan_translation_bureaus_open`, `dhrondan_terrestrial_partner_selection_open`, and `dhrondan_enclave_congress_invited` currently record history without a meaningful downstream effect, and the plan gives each one existing advisor, decision, event, or integration consumer.

`dhrondan_diplomatic_credit_established` is different: it is produced only by the six repeated helper calls, has no reader in the scanned source, and grants only the same small PP reward each time. It should be retired after a full common/generated scan, not converted into another generic store. Do not remove route flags that are consumed by route helpers, decisions, events, or achievement checks.

## `.49` transaction risks and safeguards

The native popup has one active actor offer, actor/recipient event-target pointers, an actor delivered bit, an expiry date, and a global recipient pointer. The kind flag must be set before firing `.49`, included in every response validity/commit branch, and cleared with the offer. A stale or mismatched popup must not clear a newer offer. The partner target can enter a war, become a subject, capitulate, disappear, or receive a partner accord while the popup is open; the response trigger must revalidate all of these states and the expiry path must only close the owned offer.

The current event framework documents a native same-pair annexation/release caveat: a popup already delivered to a target may be invalidated by target destruction or scope changes. The new branch should rely on the existing pointer/expiry cleanup and safe invalid response, not add a periodic world scan. A legacy save with no kind flag must continue to be treated as the default compact offer; the partner branch must never infer kind from a generic active flag.

Partner acceptance is idempotent through the root/target receipt pair. Once either receipt exists, the target query and root decision must reject another partner offer. The route actions must be applied only inside the validated acceptance branch, so paying PP or refusing/expiring cannot grant access. Existing NAP partners remain legal candidates for the accord, but the accord does not manufacture or overwrite that NAP.

## AI and balance ownership

No focus AI weights should change in this plan. The new partner decision should initially reuse an existing conservative DHR decision base, with route factors only if already present in the category, and must not be treated as balanced until the parent routes the weighted surface through `chaosx_ai_probability_auditor`.

The probability owner must establish named baseline scenarios for Imperial, Synod, and Covenant worlds, including no eligible targets, an existing NAP target, an eligible peaceful target, an active offer, a target entering war, DLC present/absent for Synod, and a route receipt missing. The owner must compare the same scenarios after any AI or weighted-target change. Source weights are not probability proof, and this plan does not authorize changing weights.

## Implementation order and dependencies

1. Parent reviews and accepts this plan, including the Synod no-DLC behavior and the choice to broaden Thel to all three existing regimes.
2. Run a full common/generated scan for `dhrondan_focus_add_diplomatic_credit`, `dhrondan_diplomatic_credit_established`, and all six receipt flags before retiring the helper.
3. Add the route-contract trigger and target-candidate trigger, then wire the existing compact root ratification gate and existing integration decision route gate.
4. Add the paid partner decision in the existing sovereignty category, reusing its icon, cost, response window, cooldown, and `.49` offer launch pattern.
5. Add kind-aware offer cleanup/validation and `.49`/`.50`/`.51` conditional handling, preserving the no-kind compact path byte-for-byte in behavior.
6. Add the route-specific partner acceptance actions, idempotent receipts, one bilateral opinion marker if accepted, advisor availability gates, and dedicated localisation.
7. Remove the six generic helper calls and retire the helper only after the scan confirms no external consumer. Optional focus custom effect tooltips may then be added without changing IDs, coordinates, or AI weights.
8. Run bounded syntax/reference scans and the required focus MCP inspect/render/raster/compare after any actual focus-source edit. The parent owns final implementation review, probability baseline/compare, and live gameplay validation.

## Evidence and validation limits

The current read-only focus evidence was collected before this plan-only task in workspace `mod_chaos_redux_ea3b2d67c2c0` for `common/national_focus/016_dhrondan_focus_tree.txt`, tree `dhrondan_focus_tree`:

| MCP pass | Result | Artifact/evidence |
| --- | --- | --- |
| `hoi4.focus_inspect` | `FOCUS_INSPECTED`, status ok | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/254bbae755bb4701121616a6ea444924984bb397fb1e729f296d4a0588482704/87e230197491b9d5ce0a85d37826664daf92bf67a43f388fc07b3497f4e62a8d/focus-inspect.b81ca02ef8c5ae6a.json`; 88 focuses, 102 connectors, zero crossings/intersections, no long connectors, layout hash `cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87`. |
| `hoi4.focus_render` | `FOCUS_RENDERED`, status ok | HTML hash `748ffeb2a79bd6f5051fc503e32b4c2d57c50564f5937cf19f3317af5f5c33b0`; SVG hash `58b73b820a4727005cbfede8b8ec426e300d884cbfbe48eb54beee1452dd5289`; JSON hash `7a4528325a978d55a59d56cce288fd622747f3b7816f34c62538e5a3f6c41123`. |
| `hoi4.focus_raster` | `FOCUS_RASTERIZED`, status ok | PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43f131badb3467ae47ed8f116c25a210825d040473908c0749d696908df61dc5/8648d9c59e6c2bd9627782d42723c494d553f9430c63dab61a0209c3e60c41a1/dhrondan_focus_tree.focus.png`; 6992×2788, same layout hash. |

The MCP report contained one unrelated vanilla diagnostic, `FOCUS_LOCALISATION_REFERENCE_MISSING` for `continuous_restrict_freedom_desc`; it is outside DHR scope and is not a reason to change this plan. No focus rewrite was run because no focus source was edited. No HOI4 launch, log search, or live test was performed.

## Simplifications, omissions, and blockers

This is intentionally a bounded reward-closure plan, not a diplomacy-system redesign. It adds no new event ID, GUI, category, branch, country, spirit, achievement, or asset. The existing foreign-operation category is not repurposed because its `brilliant_scientist_is_valid_foreign_actor` trigger rejects DHR's nonhuman/special package.

The Synod market-access action is DLC-gated by the vanilla precedent in the Austria focus tree. The parent must choose and review the reciprocal-military-access fallback or an explicit no-DLC unavailability rule before implementation. No unilateral access is acceptable, and no consent can be inferred from PP payment.

The existing native `.49` same-pair target-destruction caveat remains; kind-aware pointer/expiry cleanup is the bounded mitigation, not a new polling system. The current focus layout, route structure, and AI weights are unchanged, and no probability claim is made until the named auditor runs the baseline/compare workflow.

The original planning subtask did not change gameplay or create a commit.
The subsequent two-advisor implementation is separately documented above; the other four proposals must not be treated as implemented.
