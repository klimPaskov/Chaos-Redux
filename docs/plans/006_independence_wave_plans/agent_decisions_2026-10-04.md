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

## D3. Foreign reactions step 2: committed-cohort foreign queue and profile events

Disposition: `implemented`.

Basis: the accepted contract `docs/specs/006_independence_wave_specs/specs/006_foreign_reactions_and_remnant_petitions_contract.md` (Candidate and score contract, Delivery and caps) and the lead's round-1 item 3; D2 supplies the shared bilateral receipts.

Decisions:

- Barrier hand-off: `independence_wave_host_response_finish_plan` calls `independence_wave_foreign_reaction_build_queue` before it clears host and opening receipts; it releases the report/reset barrier through the new `independence_wave_host_response_release_report_barrier` only when no foreign receipt was reserved, otherwise the foreign queue releases it after its last receipt.
- Actor sources are only the bounded ones available in the engine: each target's `every_neighbor_country`, its patron and recognition receipt arrays, the former host's `every_allied_country` (faction members, overlord, subjects), and `global.independence_wave_active_countries`. No package carries an authored contact profile yet, so the package-contact source is recorded as a coverage gap, not substituted.
- A government that lost territory in the current wave (it is in `global.independence_wave_host_response_hosts`) answers only through its host response in that wave. This applies the contract's host precedence and keeps the one-popup-per-actor rule; it also excludes optional-state secondary hosts, which the plan arrays cannot pair with a single target cheaply.
- Concrete facts per family (each family counted once; a fact belongs to its strongest family): direct stake = frontier, claim on a target state, existing guarantee; recorded relationship = patron channel, earlier recognition receipt, Independence Network membership, alliance with the target, alliance with its former host; strategic fit = military access either way, border with the former host without a border with the target, a great power on the target's continent, an earlier-wave state in the same Event 006 region; political fit = same ideology group; conflict = actor at war, or recognition and guarantee both already given.
- Profile: active Event 006 country, else major, else regional (strategic fit or no shared frontier), else neighbor. The live score and profile are re-checked when the router runs; a pair that fell below 6 is consumed without effect.
- Stances per profile (first option is noncommittal and is the 13-day timeout default): neighbor recognize / border talks / stand with the host; regional guarantee / mediate / corridor investment; great power recognition with limited aid / arms channel / containment; earlier wave share institutions / send aid / contest. Costs reuse the existing light and standard diplomatic payments, the DM-31 equipment amounts and the DM-13 guarantee award. A guarantee needs more than ten divisions and reach (frontier, continent or access).
- Patron-style offers (corridor, arms) book nothing until the released country answers: `.71` for humans (refusal default after 13 days), the hidden router for AI (accept below the dominance warning, limit below dependency, refuse beyond). The actor's receipt stays open until that answer, so the barrier waits for consent replies as the contract requires. A limit answer is the contract's limitation/counteroffer form.
- Event IDs: `.64` router, `.65`-`.68` profiles as reserved; `.71` consent reply and `.72` queue deadline added. A collision review of `events/` on 2026-10-04 found `.43`-`.59` and `.64`-`.299` unused before this change.
- Deadline: `.72` is scheduled on every target at last dispatch + 13 + 13 + 2 days and closes only the queue that scheduled it; `on_annex` consumes the receipt or open offer of an annexed country.
- Public history (Event 6 rows, released country primary, foreign government counterpart): recognition 30, guarantee 31, mediation 32, containment 33, aid 34. Patron bargaining, refusals and rivalry stay private.
- AI is deterministic (see `docs/events/006_independence_wave/foreign_reactions.md`); stances add `befriend`, `protect`, `contain` or `antagonize` AI strategies through `add_ai_strategy`. No `ai_chance`, MTTH or random pool was introduced, so no probability baseline applies; the 4/3/2/1 score is a deterministic rank, not a probability.

MCP route evidence: `hoi4.event_inspect` (`mode = trace`, selector `{kind = event, eventId = chaosx.nr6.64}`, depth 1, helpers off) returned `EVENT_INSPECTED_PARTIAL` with 0 blocking diagnostics at revision `aa7908432d2dd3a6a99128a55ffcc50718398ab33c42d437ce1f7a0fbd2e2810` (whole-workspace helper projections deferred). A plain-string selector is rejected by the schema.

Needs live game: hidden routing and dispatch spacing, the timeout defaults, `send_equipment` with `target = PREV`, tag-targeted receipts inside the stance chain, and the barrier hand-off with a human host and a human actor.

## D4. Foreign reactions step 3: remnant petitions (`.69`/`.70`)

Disposition: `implemented`.

Basis: the accepted contract (Remnant petition) and the lead's round-1 item 4.

Decisions:

- The remnant host response consumes `independence_wave_host_response_outside_guarantee_opportunity_open` and opens a 30-day window (`independence_wave_remnant_petition.window_days`) only when the host has not petitioned in its current identity and a qualifying recipient exists; otherwise the opportunity ends without a decision.
- Recipient ranking is deterministic and bounded: the host's `every_neighbor_country`, then `every_allied_country`, scored with the accepted families against the host (frontier 4, alliance 3, access or a great power's continental reach 2, shared ideology 1, war or a claim on the host's land -3, cutoff 6); the first highest score wins and is named in the decision, so the counterpart is explicit before the host pays.
- Recipient validity: living, sovereign, not the host, not at war with it, not already guaranteeing it, not a state released from it, more than ten divisions, reach (frontier, continent or access), and no other petition answered in the same wave.
- The host pays the standard diplomatic cost through the decision; the recipient pays the standard cost only when it accepts. The guarantee is the real engine guarantee, and the host grants military access only in that branch, which is the contingent transit concession.
- Identity epoch: there is no durable generation receipt for vanilla host countries, so the explicit flag `independence_wave_remnant_petition_used` is the epoch receipt. It is set on submission and cleared only by the native lifecycle callbacks `on_annex` (FROM) and `on_release_as_free` / `on_release_as_puppet` (ROOT); no wave id stands in for it.
- AI hosts petition only under a real threat (war, or a neighbor holding or justifying a war goal against them). AI recipients accept at peace when allied with the host or sharing its outlook and able to pay, through the hidden router `.64`; human recipients answer `.69`, which declines after 13 days. `.70` reports accepted, declined or lapsed to the host.
- An accepted petition writes Event 6 history payload 35 with the host as the primary actor. Petitions never touch recognition receipts or Statehood values of released countries.
- The petition does not hold the report/reset barrier: it belongs to the host's identity epoch, not to the foreign queue, and its window and answer close on their own timers.

Needs live game: decision visibility and the named recipient, AI threat gating, `give_guarantee` from a `ROOT = { ... PREV }` chain, the access concession, and the `.70` text for each outcome.

## D5. Central admission of IW-039 DON (Millerovo)

Disposition: `implemented`.

Basis: the user's 2026-09-26 DON design (245 anchor and capital, optional 238, 218 excluded, SOV 219 protected, DHC excluded in both orders) and the lead's round-1 item 5; admission standard 3 of the lead's decisions.

Source review findings:

- Setup is Event 006-only: it removes any `Kavaleriyskaya Diviziya` units (the only vanilla DON OOB, loaded by vanilla Polish events) before the single p39 force application, guarded by the current-generation force receipt, and sets the capital to 245 after the execution capital pass.
- Optional 238 is reserved through the ordinary compact path and trimmed when unavailable; Event 005 ownership, control or reservation of 218 or 238 blocks DON exactly as accepted. 218 is never reserved.
- DHC is rejected in both orders: `is_soviet_collapse_dhc_creation_clear` blocks DHC while DON is reserved, prepared or active, and the DON preflight requires that no DHC exists.
- Cleanup is bound to `independence_wave_don_package_generation_id`.

Defects fixed:

- `is_independence_wave_exact_package_iw_039_tag_available` used the pre-reservation check `is_don_dhc_cross_event_collision_clear`, which rejects a DON that carries `liberation_release_reserved_country`. The execution preflight runs on the reserved carrier, so an admitted DON would have failed execution validation and invalidated its whole wave. The identity trigger now uses the reserved-safe `is_iw039_dhc_runtime_preflight_clear`; the planner keeps the strict check, and the scenario preflight (which runs before reservation) adds it explicitly.
- The SCN-008 scenario preflight had no entry for IW-039 or for the already admitted IW-026 Macedonia, so both were always rejected as unready in scenarios. Both entries were added.

Admission:

- IW-039 is added to the content attestation, the Join probe order (after IW-038) and the scenario preflight; it was already in the SCN-008 ranked registry and the central adapter.
- AI strategy profiles `independence_wave_don_mounted_survival`, `_host_restraint`, `_chartered_host` and `_emergency_guard` mirror the Kuban host profiles.
- `.tools/audit_event6_allocator.py`: the stopped thread's uncommitted adapter-set and dispatcher-family updates were coherent and are adopted; the expected attested set gains IW-039, attested anchors are 33 unique, and a new check proves RG-DON-KUBAN keeps capacity one (no pair exception, one group gate in each of the DON and KUB planners). The audit passes with 33 attested packages and 29 compatible groups.
- FORM-11 remains the internal later-gate marker `independence_wave_don_form11_docket_open` with no carrier.

Needs live game: a DON release with and without 238, the DHC interlock in both orders, the p39 force after a cavalry cleanup, and a scenario run that now reaches DON and MAC.

## D6. Discard the stopped thread's Transcaucasus `has_prepared_*` triggers

Disposition: `rejected` (the stopped-thread hunk); `implemented` (the validation wiring below).

Basis: the lead's round-1 item 22.

Decision: the uncommitted 192-line hunk in `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt` defined `has_prepared_independence_wave_iw_070/071/072_package_setup`. Nothing referenced them, and each required `independence_wave_iw07x_setup_complete` and `independence_wave_package_setup_complete`, the very flags it would have to gate, so it could not be wired as written. The admitted ARM, GEO and AZR setups already gate `setup_complete` on their force and focus contracts, and final validation uses the committed `is_independence_wave_exact_package_iw_07x_runtime_ready` triggers. Reworking them to the IW-027 pattern would change the setup flow of three admitted packages without new gameplay value, so the hunk was discarded.

The committed file still had four unreferenced triggers. The three `is_independence_wave_exact_package_iw_07x_runtime_ready` triggers now back `independence_wave_validate_transcaucasus_package`, so final validation also proves anchor ownership and control, the anchor capital, the current-generation force receipt and a live origin, matching the other admitted packages. `has_independence_wave_form16_commit_proof` duplicated checks that `independence_wave_form16_register_readiness` and the shared formable commit already perform and had no consumer, so it was removed. The file now has no unreferenced trigger.

## D7. Admit IW-013 NAV and IW-015 GLC and make FORM-07 Iberian Federation operational

Disposition: `implemented`.

Basis: the lead's round-1 item 6 and decisions 3 and 4.

Rights and identity decisions:

- The archived José Antonio Aguirre source (1933 Pascual Marín photograph, GureGipuzkoa 1112433, CC BY-SA 3.0, attribution and ShareAlike recorded in `docs/assets/006_independence_wave/iberian_portrait_source_research_2026_08_03/manifest.md`) and the Alfonso Daniel Castelao source (Vida Gallega no. 442, 10 March 1930, public-domain claim) are accepted by the parent as rights reviewer. The runtime portraits are the user-supplied HOI4-style outputs already installed, so no generated face of a real person is introduced.
- NAV keeps the vanilla Navarre base outside Event 006 and uses its Basque route cosmetic flags (`NAV_INDEPENDENCE_WAVE_*X`, provenance in `docs/assets/006_independence_wave/iw013_nav_flags_2026_08_13/`) inside it. GLC keeps its vanilla roster and base flag.

Defects fixed during the source review (each made the setup fail every time):

- `can_initialize_independence_wave_iw_013/015_package` and `has_prepared_independence_wave_iw_013/015_package_setup` compared the anchor owner and the former host with `ROOT`; during wave execution ROOT is the country that fired the wave, not NAV or GLC. They now use `PREV`, as every admitted package does.
- NAV required `has_country_leader = { name = "Ramón Ormazábal Tife" }` with the default `ruling_only = yes`, but Ormazábal is NAV's non-ruling Marxist leader; both checks now pass `ruling_only = no`.
- Both prepared checks read `independence_wave_force_military_tradition`, which nothing writes; the force system writes `independence_wave_military_tradition`.

Admission: IW-013 and IW-015 join the content attestation and the Join probe order (around IW-014). They were already in the adapter, runtime and scenario preflights, and the SCN-008 ranked registry. The allocator audit passes with 35 attested packages and 31 compatible reservation groups.

FORM-07 Iberian Federation:

- Identity: X-ending cosmetic tag `IFX` ("Iberian Federation"; ideology names in `006_independence_wave_formable_registry_l_english.yml`), flat flag triplet generated with ChatGPT Images and processed to 82x52, 41x26 and 10x7 TGA (`docs/assets/006_independence_wave/form07_iberian_federation_flag_2026_10_04/manifest.md`). It is an explicitly labelled alternate-history synthesis of the three member flags.
- `can_independence_wave_form07_register_readiness` now needs only the identity clearance (no other carrier holds IFX); readiness sets the identity, X-tag and flag-package receipts that the runtime contract and the shared identity check already require. The identity adapter sets `IFX`, the global identity lock and the carrier flags once the FORM-07 commit proof holds; rollback and cleanup drop `IFX`.
- The pre-existing cleanup released the global IFX lock for every Event 006 country that ran formable cleanup; the lock is now released only by the country that holds IFX or the carrier flag.
- NAV government routes no longer replace IFX with a NAV route flag on the federal carrier.
- The FORM-07 member ledger, consent, corridor proof, integration adapter and state-puzzle overlay already existed; no GUI file changed, so no before/after GUI evidence applies. A narrow `hoi4.gui_inspect` call on `chaosx_independence_wave_formable_state_puzzle_window` was rejected as invalid arguments by the tool schema.

Needs live game: NAV and GLC releases (setup now passes), FORM-07 congress with CAT, NAV and GLC, the IFX flag and names, and the NAV route change after federation.
