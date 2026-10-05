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

## D8. Round-1 review corrections

Disposition: `implemented`.

Basis: the skeptical review of the round-1 commits (`ada1dbd8a`, `240711ff9`, `608ba49bf`, `78534832b`, `71217beff`, `bba9eda1e`, `854e31bc6`).

- IW-039 DON final validation: `independence_wave_validate_iw_039_don` reads `is_independence_wave_exact_package_iw_039_runtime_ready`, which reads `has_independence_wave_don_anchor_control`. That trigger compared state 245 with `ROOT`, but final validation runs inside `event_target:independence_wave_execution_country` in the wave executor, where ROOT is the country that fired the wave. Every admitted DON release would therefore have failed validation and invalidated its wave, the same defect class D7 fixed for NAV and GLC. The trigger now uses `PREV` (the checked country), which is also correct in the DON decisions and focus gates where the country is in scope.
- Transcaucasus: `has_stable_independence_wave_iw070/071/072_settlement` also compared the capital state with `ROOT`; `independence_wave_transcaucasus_refresh_package_ideas` evaluates them during setup, so they now use `PREV` as well. The FORM-16 anchor checks keep `ROOT` because they run in the carrier's own decision.
- Foreign reaction router `.64`: a router sent to an AI only to answer a patron offer or a remnant petition no longer routes that country's own pending reaction early; the scheduled `.64` routes it on its dispatch day, keeping the contract's one-day spacing.

Known setup defects outside this round (not admitted, left for their admission items): the same `ROOT`-for-carrier pattern is still present in the setup or validation triggers of IW-043, IW-047, IW-050, IW-057, IW-058, IW-060, IW-093, IW-095, IW-098, IW-177 and IW-179; each must use `PREV` before it is admitted. The shared `has_independence_wave_current_capital_controlled_by_root` and provisional-capital cost triggers reached from `independence_wave_refresh_country_state` also read `ROOT` during setup; they only delay the provisional-phase check until the next refresh and are left to the core-framework owner.

Needs live game: a DON release that now passes final validation.

## D9. Round 2: the wave executor rejected every anchor-bound package (SCN-008 live defect)

Disposition: `implemented`.

Basis: the routed live defect (QA saves `qa_scn008`, `qa_scn008b` and `qa_scn008d`, each with `global.independence_wave_execution_last_failure = 10` and `liberation_plan_last_failure = 0`) and the lead's round-2 item 1.

Save evidence (`qa_scn008d.hoi4`, 1936.2.4, v1.19.2, plain text, read with the save-inspection inspector):

- `liberation_plan_phase = 6` (aborted), `liberation_plan_countries^num = 31`, and all 31 `liberation_plan_country_owners` are 6. Decoding the stored scopes (a country is its tag bytes in little-endian order plus 2^30, a state is its id minus 2^30) gives the frozen rows in executor order: SCO 121 ENG, WLS 122 ENG, BRI 14 FRA, BAY 52 GER, CAT 165 SPR, MAC 106 YUG, BOS 104 YUG, KAR 146 FIN, CRI 137 SOV, BSK 651 SOV, ARM 230, GEO 231, AZR 229, HAW 629, GLC 171, COR 1, MNT 105, AFX 34, NAV 792, ASX 115, RUT 73, HBX 378, AGX 36, ARX 114, BAX 184, BBX 185, RHI 51, DON 245, AJX 42, TRA 84 and TAT 249.
- The plan locked (the shared validator passed and `aligned_array_failure` was not written), so the failure came from the per-package `invalid_scope` block and not from the shared planner.

Root cause:

- The executor's carrier check runs `is_independence_wave_runtime_package_preflight_ready` on the reserved carrier. For anchor-bound packages that preflight calls the exact identity trigger `is_independence_wave_exact_package_iw_XXX_tag_available`, whose anchor block used `is_independence_wave_candidate_anchor_available`. That trigger requires `NOT = { is_liberation_release_current_reserved_state = yes }`, but at execution the anchor is reserved for this very package, so the identity proof always failed.
- In the decoded plan the first such row is KAR (row 7, state 146), so every SCN-008 launch stopped there. The same defect hit CRI, BSK, MNT, RUT, BAX, BBX, DON, TAT, TRA, MAC, BOS, KOS, KUB and AXX, and every ordinary wave that selected one of them. The D5 DON fix replaced only the DHC check and left this anchor block in place.
- Every other check in the block holds for a valid frozen plan (walk-through below), so this is the only cause found in source.

Decisions and fixes:

- New state trigger `is_independence_wave_exact_package_anchor_available` in `006_independence_wave_package_triggers.txt`. It passes the ordinary candidate-anchor proof, or a reservation in the current plan owned by Event 006 for the same package id (`independence_wave_execution_package_id`) and the same carrier (`liberation_release_target_country = PREV`), still owned and controlled by a living host outside Event 005 and not protected. Every `is_independence_wave_exact_package_iw_XXX_tag_available` anchor block now uses it (26 blocks in 13 files, including the packages not yet admitted, so their admissions do not repeat the defect). Planner and scenario preflights run before reservation, so their result is unchanged.
- `.tools/audit_event6_allocator.py` now fails if any exact identity trigger uses the pre-reservation anchor proof, and it checks the three ordered carrier proofs of the executor.
- IW-013 NAV and IW-015 GLC could never enter an ordinary wave. Their `can_plan_*` triggers still used the legacy `is_independence_wave_candidate_tag_available` gate, which requires a content flag that no admitted package receives. They now use new `is_independence_wave_runtime_automatic_package_iw_013_ready` and `_015_ready` triggers that mirror IW-014. The joint Event 005/006 capacity witness is conservative by contract and was left without them, since a false negative only skips an optional member.
- Persistent diagnostics: `independence_wave_validate_execution_metadata` now evaluates its checks as an ordered chain and writes `global.independence_wave_execution_last_failure_detail` (new constant category `independence_wave_execution_failure_detail`: codes 1-5 for the plan and row, 10-23 for the package checks, 30-33 for the sponsorship checks) and `global.independence_wave_execution_last_failure_package_id`. The executor also records codes 40-46 for host capital relocation, instantiation, state transfer, package setup, activation, final validation and origin commit, and the setup, activation and validation passes record the first failing package id. All three globals are cleared when the next launch or standalone wave begins.
- Failure result: the routed live defect overrides the earlier success-only publication rule for the failure case. `independence_wave_trigger_scenario` fires `chaosx.triggerable_scenarios.81` "No Banner Rises" to the launching player when a launch releases no country, and the `.8` else-branch fires it with `independence_wave_scenario_launch_called_off` when a queued launch is called off. The text says no country was released and gives one short reason chosen from `global.independence_wave_scenario_last_failure` through `GetIndependenceWaveScenarioFailureReason`. A finalizer failure after state transfers uses a separate unfinished-government text. The event has one acknowledge option, and the public ledger stays success-only.
- Event ID: a collision review of `events/` on 2026-10-04 found `chaosx.triggerable_scenarios` IDs 1-8, 11 and 80 in use, so `.81` is free.
- Ordinary automatic waves have no launching player, so they keep the diagnostics without a popup.

Source walk-through of a valid frozen plan. Both the SCN-008 path and the ordinary path reach the same `independence_wave_validate_execution_metadata`.

- IW-001 SCO, row 0: the plan is locked with `liberation_release_plan_valid`; the allocator set the contribution flag; the metadata arrays are aligned (allocator gate); `selected_count = target_count` (the scenario allocator sets the target to the selected count and the automatic planner enforces the exact count); the row index is in range; the three var-scoped event targets resolve, because the shared lock validator uses the same pattern on the same rows and passed; owner 6 and package id 1 match the save; IW-001 is in the adapter; the force probe is the one the planner already passed for the same id; SCO does not exist, so it is dormant; it is in `liberation_plan_countries`, so it is the current reserved country; the preflight passes its adapter, attestation, origin and `original_tag = SCO`/`exists = no` checks; state 121 carries the current reservation flag and plan id and is owned by ENG; ENG exists and is in `liberation_plan_hosts`.
- IW-033 KAR, row 7: identical to SCO up to the preflight. `is_independence_wave_exact_package_iw_033_tag_available` now passes. The origin is available, because the reservation flag belongs to the current plan and `independence_wave_finish_package_reservation` cleared any rejection marker. The tag does not exist. State 146 passes the reserved branch of the new trigger (current reservation, Event 006 owner, package 33, target KAR, owned and controlled by FIN, not protected), and its owner FIN is not KAR.

MCP route evidence: `hoi4.event_inspect` (`mode = trace`, selector `{kind = event, eventId = chaosx.triggerable_scenarios.81}`, upstream, depth 1, helpers off) returned `EVENT_INSPECTED_PARTIAL` with 0 blocking diagnostics at revision `2d688e7f825942b8e50d4554e687c13988fcd550f5d36e417003cfb764a9d837`.

Allocator audit: passes with 35 attested packages and 31 compatible reservation groups, and the new identity-trigger guard scans 52 exact identity triggers.

Needs live game: a fresh 1936 SCN-008 launch at Low that releases its countries. If a later stage fails, the next QA save names it through the detail and package-id globals. The finalizer is all-or-nothing, so one package with a broken setup still stops the whole wave after the state transfer; detail codes 43-46 and the package id now expose that case.

## D10. Round 2: the shared state refresh reads the refreshed country, not ROOT

Disposition: `implemented`.

Basis: the lead's round-2 item 2 and decision 2. `independence_wave_refresh_country_state` is Event 006 core code owned by this workstream, so the D8 note that left it to a core-framework owner is withdrawn.

Defect: the refresh runs whenever one of the five values changes, including from a foreign-reaction stance, a League decision, the host response or the executor, where ROOT is another country. Four reachable definitions read ROOT as the refreshed country:

- `has_independence_wave_current_capital_controlled_by_root` (`is_controlled_by = ROOT`), reached through `can_independence_wave_enter_provisional_phase`, so the provisional phase was delayed or wrongly blocked.
- `can_pay_independence_wave_provisional_capital_cost` (`capital_scope = { is_controlled_by = ROOT }`) and `independence_wave_secure_provisional_capital_garrison_satisfied` (`ROOT = { divisions_in_state = ... }`), reached through `independence_wave_start_provisional_capital_mission`, so DM-01 could start late, or never, when the refresh came from another country.
- `independence_wave_achievement_refresh_country_state` (`var:independence_wave_former_host = { NOT = { has_war_with = ROOT } }`), so the peaceful host settlement proof read the wrong country.

Decisions:

- The capital trigger is renamed `has_independence_wave_current_capital_control` and uses `is_controlled_by = PREV` inside `any_owned_state`, so it always tests the checked country. All 69 callers (the AXX, BAX and BBX decisions and missions in `006_independence_wave_balkan_decisions.txt`) evaluate it in the country's own decision scope, where THIS and ROOT are the same country, so their meaning is unchanged. Two quality documents that narrate an earlier commit keep the old name as history.
- The DM-01 cost gate uses `capital_scope = { is_controlled_by = PREV }`. The garrison gate uses `capital_scope = { PREV = { divisions_in_state = { state = PREV ... } } }`: entering PREV pushes the country, and PREV inside it is the capital again (the wiki's `start_civil_war` and `PREV.PREV` examples show the same push). DM-01's own decision and mission scopes are the country, so they are unchanged.
- The achievement settlement proof uses `has_war_with = PREV` inside the former-host scope.
- `has_independence_wave_safe_reserve_surplus` also reads ROOT but is reached only from decisions of the country itself, so it stays as it is.

Validation: a call-graph walk from `independence_wave_refresh_country_state` and the five `independence_wave_change_*` entry points (58 or 59 reachable scripted effects and triggers) finds no remaining ROOT reference.

## D11. Round 2: re-release defects in NAV and in the foreign queue deadline

Disposition: `implemented`.

Basis: the lead's round-2 item 3 and decision 3.

NAV Aguirre roster:

- Defect: `has_independence_wave_nav_command_roster`, read by NAV setup and by `has_prepared_independence_wave_iw_013_package_setup`, needs `NAV_independence_wave_jose_antonio_aguirre` as a corps commander. Only startup history recruits him, and `independence_wave_cleanup_iw_013_basque` retired him, so a second NAV release in one campaign always failed setup and stopped its whole wave.
- Decision: cleanup no longer retires Aguirre. He is part of NAV's startup roster, like the vanilla NAV characters, and stays with the tag. The new `independence_wave_nav_ensure_command_roster` runs at the start of NAV setup: it recruits him with `recruit_character` when NAV does not have him, and gives him back his corps command with `add_corps_commander_role` (traits and skills from his character definition, held in file constants) when another effect removed it. The syntax follows `effects_documentation.md` (`recruit_character`, `retire_character`, `add_corps_commander_role`, all country scope).
- Walk-through of a second release: cleanup keeps Aguirre, NAV is annexed and released again, setup passes `can_initialize_independence_wave_iw_013_package`, the ensure step finds Aguirre and his corps command (or restores them), so `has_independence_wave_nav_command_roster`, the roster checkpoint, the force load and `has_prepared_independence_wave_iw_013_package_setup` all pass as in the first release.

Foreign queue deadline (`.72`):

- Defect: every target stored only the plan id of the queue that scheduled its deadline. A `.72` scheduled by an earlier queue could fire after a newer queue raised on the same target, find the newer plan id, close the newer queue early and clear its schedule. This needs a re-release of the same target within about 30 days.
- Decision: each target also stores `independence_wave_foreign_deadline_date`, the date from which its queue may close (last dispatch plus the response and consent timeouts), converted with `chaosx_convert_days_to_date_offset`. The event still fires `deadline_margin_days` later. `independence_wave_foreign_reaction_check_deadline` acts only when `global.date` has reached the stored date, and then closes the queue only if the stored plan id is still the open queue. An older event that arrives early finds the newer date and does nothing, so the newer queue keeps both its receipts and its own deadline. A schedule without a stored date keeps the plan-id check alone.
- The roughly 230-day foreign-queue blocking stays as accepted design.

Needs live game: a second NAV release in one campaign; a target released twice within 30 days with an open foreign queue.


## D12. Round 2: release-path walk-through of the 31 SCN-008 Low packages

Disposition: `implemented`.

Basis: the lead's round-2 priority-1 item and decision 2. The finalizer is all-or-nothing, so one package that fails setup, activation, final validation or origin commit stops the whole wave.

Method (source walk-through, 2026-10-05):

- For each row, the closure of scripted effects and triggers reached from instantiation (`independence_wave_release_one_frozen_country`), the four finalizer passes (`independence_wave_prepare_country_origin`, the breakaway sponsorship step, the package setup, `independence_wave_activate_prepared_country_origin`, the package final validation and its generic focus tail, `independence_wave_commit_prepared_country_origin`) and the generation reset was walked with ROOT set to the launching country and the carrier as THIS.
- Every ROOT, FROM and caller-level PREV read in that closure was listed and classified.
- Every flag, variable, idea, event target, character and template that the package's `can_initialize_*`, `has_prepared_*`, runtime-ready and final-validation triggers require was matched against its writer in setup, in the shared prepare and activation passes, or in startup history (`history/countries`, `history/general/006_independence_wave_character_recruitment_registry.txt`, or the vanilla history file of the tag).
- The planner's region, depth and archetype for each package id, and the force profile and military tradition decoded from `independence_wave_force_package_profile.p<id>` and `independence_wave_force_package_military_tradition.p<id>`, were compared with the values the package checks expect. All 31 match.
- Every character id the checks read is defined in `common/characters` (mod or vanilla) or generated in setup with `generate_character`; every vanilla roster character is recruited at the top level of its vanilla 1936 history file; every corps-commander check names a character with a corps-commander role. The only fixed template id, DON's vanilla `Kavaleriyskaya Diviziya`, matches `history/units/DON_cossack_host.txt`.

Defects found and fixed:

- TRA (IW-023): `independence_wave_form08_register_readiness` read `is_owned_and_controlled_by = ROOT` for anchor 84. TRA's `has_prepared_independence_wave_iw_023_package_setup` requires `independence_wave_form08_readiness_attested`, so every TRA release failed setup and stopped its wave. It now reads PREV, the registering country.
- The nine custom X-tag carriers (AFX, AGX, AJX, ARX, ASX, AXX, BAX, BBX, HBX) are created with `create_dynamic_country`. A dynamic carrier is a new country object, and the executor copied it from the former host (`copy_tag = THIS`). Every X-tag roster check reads characters that only startup history attaches to the tag, AJX's prepared check also reads startup laws, and the instantiation count requires the new country to exist, which a reserved dynamic country that owns no state yet may not. Decision: the template is now the carrier's own tag (no `copy_tag`, as in every vanilla `create_dynamic_country` call); the new `independence_wave_materialize_custom_carrier` moves the frozen anchor to the carrier inside its creation block, as `release` moves cored states for vanilla carriers; and `independence_wave_ensure_custom_carrier_startup_state` recruits any missing startup roster character and adds any missing startup law, mirroring each tag's startup history. Technology still comes from `inherit_technology` in the force package, so nothing the old `copy_tag` supplied is lost.
- ASX (IW-019) cleanup removed the claims on states 117 and 156 from ROOT, which is the launching country during the setup reset and the annexer at origin end, so it stripped the wrong country's claims and left ASX's own claims on the tag. The cleanup and the focus reward that adds the claims now use PREV, the Sicilian carrier.
- Origin cleanup reached from the generation reset and from `on_annex` read ROOT as the cleaned country in six more places, so it skipped its work whenever another country ran it: the Defensive Congress war mandate flag; the FORM-01/02/04, FORM-07, FORM-39 and FORM-48 frozen autonomous-member cleanup; the founding-invitation cleanup in `independence_wave_formable_close_founding_proposal` (new `independence_wave_formable_clear_founding_invitation_from_prev` and `independence_wave_formable_clear_own_founding_invitation`, sharing `independence_wave_formable_clear_matched_founding_invitation`); the rival-bloc pending invitation; and the reclamation-front coordinator check in `independence_wave_end_active_origin`. All now compare with the cleaned country through PREV or PREV.PREV.
- FORM-16: `has_independence_wave_form16_member_connection_proof` compared ARM, GEO and AZR with ROOT and is evaluated during setup. It now uses the new `has_independence_wave_form16_connection_to_prev`, with the carrier as PREV. This only gated the AI connection receipt, not setup.

Remaining ROOT reads in the closure are a temporary-variable write inside `ROOT = { }` in two rival-bloc registry effects (temporary variables have no scope, so the write is unaffected) and the Event Logs and other systems' code that the commit pass reaches through the Event Log history entry, which use ROOT as their own event actor. IW-093, IW-098, IW-177 and IW-179 still read ROOT for the carrier; they stay adapter-only and are fixed in their admission items.

Per package (row order, anchor and host from the decoded `qa_scn008d` plan in D9):

- SCO (IW-001, 121, ENG): passes. Civic convention and commandant generated in setup, advisors from startup history; full Event 006 tree; FORM-01/02 candidate flags unconditional.
- WLS (IW-002, 122, ENG): passes. Same pattern as SCO.
- BRI (IW-004, 14, FRA): passes. Vanilla BRI advisors from the vanilla history file, coastal commandant generated in setup.
- BAY (IW-009, 52, GER): passes. Generated commandant, startup advisors, vanilla Rupprecht.
- CAT (IW-014, 165, SPR): passes. Vanilla Companys roster.
- MAC (IW-026, 106, YUG): passes. Startup Vardar presidium through the roster checkpoint; full tree.
- BOS (IW-029, 104, YUG): passes. Startup Drina council; generic tree or the Austro-Hungarian overlay.
- KAR (IW-033, 146, FIN): passes. Vanilla KAR roster (top-level 1936 history).
- CRI (IW-041, 137, SOV): passes. Vanilla Tarkhan roster.
- BSK (IW-045, 651, SOV): passes. Vanilla Bykin roster.
- ARM (IW-070, 230, SOV): passes. Shared Transcaucasus validator, ARM branch.
- GEO (IW-071, 231, SOV): passes. Vanilla Zhordania, Kvinitadze and Bagration.
- AZR (IW-072, 229, SOV): passes. The traditional route is correctly excluded.
- HAW (IW-173, 629, USA): passes. Startup territorial delegate; HAW branch of the Pacific command structure.
- GLC (IW-015, 171, SPR): passes (the D7 fixes hold).
- COR (IW-017, 1, FRA): passes. Startup COR roster; FORM-05 readiness unconditional.
- MNT (IW-030, 105, YUG): passes. Vanilla Popovic and Jovanovic, startup Martinovic.
- AFX (IW-006, 34, BEL): passes after the X-tag fix. FORM-03 readiness unconditional.
- NAV (IW-013, 792, SPR): passes (the D7 and D11 fixes hold).
- ASX (IW-019, 115, ITA): passes after the X-tag fix; cleanup claims fixed.
- RUT (IW-038, 73, CZE): passes. Vanilla Voloshyn, startup Brodiy, Mondok and Klympush.
- HBX (IW-184, 378, USA): passes after the X-tag fix.
- AGX (IW-007, 36, HOL): passes after the X-tag fix.
- ARX (IW-018, 114, ITA): passes after the X-tag fix.
- BAX (IW-027, 184): passes after the X-tag fix.
- BBX (IW-028, 185): passes after the X-tag fix.
- RHI (IW-008, 51, GER): passes. Generated commandant, startup advisors, vanilla Matthes.
- DON (IW-039, 245, SOV): passes (the D5 and D8 fixes hold); the vanilla template id matches.
- AJX (IW-010, 42, GER): passes after the X-tag fix, which also restores its startup laws.
- TRA (IW-023, 84, ROM): passes after the FORM-08 fix.
- TAT (IW-044, 249, SOV): passes. Vanilla Alemasov roster.

Validation: the allocator, country API, flag and FORM-16 audits pass; brace balance is 0 on every touched file.

Needs live game: a fresh SCN-008 Low launch that releases all 31 countries, including at least one X-tag carrier (its name, flag, roster and anchor on creation) and TRA. If any stage still fails, the D9 failure-detail and package-id globals name it.


## D13. Round 2: admission of the IW-043 CHU and IW-058 ASY signature packages

Disposition: `implemented`.

Basis: the lead's round-2 priority-2 item and decisions 3 and 4, and the D12 walk-through method applied to both packages.

Adopted hunks: the interrupted round-2 implementer's uncommitted ROOT-to-PREV edits in `006_independence_wave_iw043_iw058_package_triggers.txt` and `006_independence_wave_iw043_iw058_package_effects.txt` were reviewed scope by scope (country scope into states and former hosts, and `random_country_division`, `any_country_division` and the bound division target, where PREV is the country) and are adopted as this workstream's own.

Further scope fixes: the setup, anchor, capital and former-host reads that still used ROOT for the carrier now use PREV (`independence_wave_iw043_safe_action_reserve`, `_iw058_`, the FORM-12, FORM-13 and FORM-18 local settlement contracts, `has_independence_wave_iw058_valid_autonomy_treaty_partner` and the two IW-058 achievement writers). The partner-reach, formable-member and `_from_root` formable triggers keep ROOT, because their callers evaluate them with the carrier as ROOT. A call-graph scan of the CHU/ASY setup, final validation and cleanup closure finds no ROOT read.

Setup defects found and fixed:

- Neither setup ever set `independence_wave_command_roster_ready`, which gates the opening force, so `has_independence_wave_iw043_setup_surface` and `_iw058_` could never pass and both packages always failed setup. New `has_independence_wave_iw043_command_roster` and `has_independence_wave_iw058_command_roster` check the startup roster; setup sets the roster flag before the force pass, and setup completion and final validation also require the roster.
- The opening and federal CHU leaders and the opening ASY leader carried `centrism`, a neutrality sub-ideology, while those routes are ruled by the democratic party, so the country would have shown a generated leader. They now carry `liberalism`; cleanup removes the matching role.
- FORM-12, FORM-13 and FORM-18 are in the shared commit allowlist, but `independence_wave_formable_readiness_family` was never written for them, and the shared family dispatcher had no branch for them, so a focus that switched CHU between FORM-12 and FORM-13 cleared the shared receipts for good. The dispatcher now calls `independence_wave_iw_formable_register_signature_readiness`, and setup writes the receipts through `independence_wave_iw_formable_write_signature_readiness_receipts`.

Portraits (round-1 admission standard; the parent acts as rights reviewer; no generated face of a real person):

- Every repainted real-person portrait is replaced by its unchanged source photograph, cropped with the event-assets crop tool in `source_placeholder` mode and converted with its DDS converter: Mirsaid Sultan-Galiev (1923), Gayaz Ishaki (book plate), Karim Tinchurin (1934), Luka Spasov (1938) and Ignatius Afram I Barsoum. Evidence packages and completed provenance contracts are in `docs/assets/portraits/006_independence_wave/round2_source_placeholders/`. The existing Gallo Shabo portrait is already a source crop.
- The federal presidium's displayed name was Galimzhan Ibrahimov while its portrait source is Gayaz Ishaki; the name and description now follow the source. The Bolgar presidium and the concordat council now show Karim Tinchurin and Ignatius Afram I Barsoum, the people their portraits show.
- Werda (civic national assembly) is rejected as decided. Haydo (levies guardianship) is accepted on rights, but the working tree holds only his repaint and not the source photograph, and downloading it again needs the user's approval, which this run cannot request. Both consumers are unwired (character, startup recruitment, sprite and runtime DDS removed). The civic route gives the vanilla Mar Shimun XXI Eshai one added conservatism role, the guardianship route promotes his own vanilla despotism role with the guardianship trait added for the route, and the popular route promotes the vanilla Benjamin Arsanis. Cleanup removes only the added role and trait.
- Route gap: this run has no subagent tool, so `chaosx_portrait_creator` could not be spawned. The work used the same skill tools in source-placeholder mode and no ImageGen, repaint or RunPod.

Admission: IW-043 and IW-058 are in the content attestation and the Join probe order. Their SCN-008 preflight rows, ranked list entries, planner and reservation publishers and AI strategy profiles already existed. CHU shares anchor 249 and RG-MIDDLE-VOLGA-KAZAN with TAT, so a wave holds at most one of them; ASY uses RG-NORTHERN-MESOPOTAMIA. Both stay high-chaos only.

Formables and achievements: FORM-12, FORM-13 and FORM-18 now pass the shared readiness receipts and keep their keyed commit gates. The IW-043 restoration and federal route proofs remain mutually exclusive through the route flags; the three IW-058 proofs are independent achievements, as designed.

Walk-through: region, depth and archetype match the planner loaders; every required flag and variable is written in setup; every character read is defined and recruited (startup history or vanilla 1936 history); the two fixed templates are defined in setup.

Validation: the allocator audit passes with 37 attested packages and 32 reservation groups (updated to allow only the CHU/TAT shared anchor); the country API, flag, FORM-16 and SCN-008 matrix audits pass.

Needs live game: a high-chaos wave or SCN-008 launch that releases CHU or ASY; the leader shown on each route; a FORM-12, FORM-13 or FORM-18 congress.


## D14. Round 2: focus groups for the Level 2 packages RUT, BSK, ARM, GEO and AZR

Disposition: `implemented`.

Basis: the lead's round-2 priority-3 item; Part 5 requires one country-specific focus group per Level 2 package, and Part 4 records the accepted TAT pattern (adopted in this commit together with the stopped thread's TAT paragraph, corrected to the implemented names and the 720-day mission).

Decisions:

- Each package gets five `shared_focus` nodes in `common/national_focus/006_independence_wave_focus.txt`, imported into `independence_wave_focus_tree` and gated by a new `can_use_independence_wave_<tag>_focus_group`: an opening node, two complementary branches, a former-host settlement node that needs both branches and the generic founding settlement, and a capstone that also needs Recognize Fellow New States. The full map is in Part 4.
- Rewards reuse each package's existing clamped helpers, so a focus and its paid project reach the same milestone: RUT and BSK reuse their `_focus_` helpers; ARM, GEO and AZR reuse the project completion helpers and `independence_wave_transcaucasus_complete_arbitration`. The Transcaucasus settlement node uses the new `independence_wave_transcaucasus_focus_settle_former_host` (both local measures, plus the shared host-negotiation settlement when the former host lives and is at peace), whose flag is cleared by package cleanup.
- Exclusivity: a focus is unavailable while its paid project runs and is bypassed once the project's result exists; the project is unavailable once the focus has progress (`focus_progress`, with file-scoped minimums beside each decision file's other `@` values) and hidden once the focus result exists.
- The RUT and BSK reward hooks on the generic opening focuses (Prepare the Capital Administration, Inventory the State, Bind the First Oath) were removed, so each reward has one focus owner.
- AI follows D1 with `independence_wave_focus_ai` only: the opening node is `urgent` with strong preference during the founding mission or severe instability; branches are `high`, strongly preferred during the mission, with the civic branch preferred on civic routes and the security branch preferred under a severe host threat or the emergency route; the settlement node is preferred while a living former host is not a severe threat; the capstone is preferred once the route government or the stable settlement exists.
- Timing: the opening and both branches take 105 days after the generic opening focus, inside every founding window (RUT 600, BSK 420, Transcaucasus 210 days).
- Icons reuse registered Event 006 goal sprites; all 130 referenced localisation keys exist once, in `006_independence_wave_focus_l_english.yml`.

Defect fixed in the existing groups: the DON, KAR, CRI, KUB and TAT group gates required `has_complete_independence_wave_iw_0XX_package_setup`, whose `independence_wave_origin_prepared` and `independence_wave_origin_activation_ready` flags are cleared by the origin commit. Every one of those groups was therefore unavailable to the released country. Gates now read the package setup receipt (`independence_wave_iw_0XX_setup_complete`), which persists until package cleanup. The same transaction-only proof is still read after commit by the FORM-09 member readiness checks in `006_independence_wave_formable_registry_triggers.txt`; that belongs to the formable item and is recorded there.

MCP: `hoi4.focus_inspect` (national, `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`) returned `FOCUS_INSPECTED` with no mod diagnostics at revision `7f79b2979891c18ac712f0eeefe3b614cf4134e0be0c154b21b254a3b59b8998`; it counts 184 direct focuses and omits the 103 imported `shared_focus` nodes, so layout and attachment of these groups remain a recorded MCP gap.

Needs live game: each group visible and progressing for a released RUT, BSK, ARM, GEO or AZR; the DON, KAR, CRI, KUB and TAT groups visible after release.


## D15. Round 2: two incidents for every Level 2 package that had none

Disposition: `implemented`.

Basis: the lead's round-2 priority-4 item; Part 5 Level 2 requires several unique incidents per package. Before this change only RHI, BAY, AFX, COR, ARX and ASX had package incidents. A collision review of `events/` and `common/` on 2026-10-05 found no reference to `chaosx.nr6.73` to `.299`, so `.101` to `.142` are used.

Decisions:

- SCO, WLS, BRI, CAT, TRA, MAC, BOS, KAR, CRI, RUT, KUB, TAT, BSK, ARM, GEO, AZR, HAW, HBX, NAV, GLC and DON (21 packages) each get two incidents grounded in their own history: for example the Clyde Admiralty contracts and the Highland land raids for Scotland, the Cluj university and the Saxon town charters for Transylvania, the Ishimbay wells and the Kurultai elections for Bashkiria, the Batumi port dues and the autonomy statutes for Georgia. The full list is in `docs/events/006_independence_wave/package_incidents.md`.
- Scheduling: the first incident is scheduled when the country resolves its founding posture (the existing `chaosx.nr6.41`/`.42` resolution effects, which every released country passes through), and either answer to it schedules the second. Delays are `independence_wave_package_incident.first_delay_days` (45) and `second_delay_days` (150). No world hook is used.
- Generation safety: scheduling stores `independence_wave_package_incident_generation`; `can_fire_independence_wave_package_incident` requires an active origin of the same generation, and `independence_wave_clear_package_incident_runtime` runs in the generation reset and at origin end.
- Options: two per incident, each trading Statehood values (through `independence_wave_decision_apply_country_deltas`) against the package's own ledgers (through its existing clamped helper) and, where stated, former-host hostility. Every incident offers one free answer; costly answers require and spend 35 political power (new `independence_wave_package_incident` constants) or the existing light manpower cost. DON has no package ledger, so its options trade Statehood values and the host relation only.
- AI: `ai_chance` uses `independence_wave_decision_ai` bases, doubled for the answer that fits a civic route, an emergency route or a severe host threat.
- Pictures reuse existing vanilla report pictures; no new art is needed.

Validation: every effect, trigger and constant the events and localisation reference is defined; the 252 new localisation keys are unique.

Not attempted: probability inspection of the new `ai_chance` weights (the lead folds the narrow probability attempt into the baseline-incident item).

Needs live game: a released package receiving both incidents; a re-released tag not receiving an earlier generation's incident.


## D16. Round 2: recurring statehood incidents and deeper evolution incidents

Disposition: `implemented`.

Basis: the lead's round-2 priority-5 item. Part 2 (Baseline incidents) requires a recurring layer of founding, recognition, security, government, League and formable incidents for every active Event 006 country, and lists five to seven new incidents per evolution, where each evolution had one shared incident family.

Decisions:

- One pulse per country. `independence_wave_start_statehood_incidents` runs from the founding posture resolution (the same two effects that schedule the package incidents), and the hidden `chaosx.nr6.150` reschedules itself after a random 90 to 139 days. No daily, weekly, monthly or world hook is used.
- Pool: 20 baseline incidents (`.151`-`.170`: four founding, three recognition, three security, four government, three League, three formable) and 11 evolution incidents (`.171`-`.181`: two Replicable Independence, two Dormant Nations, two Armed Birth, three Sovereign Congress, two Open Sovereignty). The new evolution incidents take spec-listed items that the existing `.360`-`.364` families do not already cover (volunteer civil servants, host anti-secession coordination, a returning claimant, the school language dispute, the Armed Birth coup and equipment crisis named in its failure section, the common defence clause, the patron scandal, the collective response to reconquest, the radical constitutional experiment and anti-host coalition planning).
- Eligibility reads live country state only: founding phase, the five values, the former-host relation and outcome, patron influence, League membership, the League route and patron capture, formable progress flags, and the active and enabled evolutions. Disabling an evolution in the Event Logs removes its incidents.
- Weights: each category has a base weight that doubles in the matching situation (emergency founding, recognition below de facto, war or a severe host threat, an undecided route, League leadership or crisis, an open founding proposal); a quiet-season weight grows for settled countries and shrinks in severe instability, so stable states see fewer incidents.
- Cooldowns: each incident fires once per generation; opening one puts its category on a 240-day cooldown (150 for evolution incidents), stored as a date through `chaosx_convert_days_to_date_offset`.
- Generation safety: the pulse stores the generation and a due date; the delay window (60-day first delay, 90 to 139-day interval) guarantees that a pulse left over from an earlier release of the tag arrives before the current due date and does nothing. Incident events also require the matching open-incident id. `independence_wave_clear_statehood_incident_runtime` runs in the generation reset and at origin end.
- Options: every incident has a free answer. Costs reuse the shared light diplomatic and light security payments and a 35 political power cost; three answers add manpower or army experience; two League answers deliver equipment to the member that asked. ai_chance follows the `independence_wave_decision_ai` palette with route, war and host-threat modifiers.
- Pictures reuse registered vanilla and Event 006 report pictures; no new art.

Validation: brace balance 0 on the four new script files; every scripted effect, trigger and constant referenced by the events and effects is defined; all 194 localisation keys exist once.

MCP: `hoi4.probability_inspect` (`event_option_ai_chance`, source `events/006_independence_wave_statehood_incident_events.txt`, candidate `chaosx.nr6.163`) returned `INTERNAL_ERROR`; not retried. `hoi4.event_inspect` (trace, `chaosx.nr6.165`, downstream, depth 1, helpers off) returned `EVENT_INSPECTED_PARTIAL` with 0 blocking diagnostics at revision `b64cae37af8b30b3de242281669ac26c9677f1190578cdbdd91f7831c9967795`.

Needs live game: a released country receiving its first incident about 60 days after its founding posture and later incidents every few months; a re-released tag not receiving a pulse from its earlier generation.


## D17. Round 2: rare world milestone news

Disposition: `implemented`.

Basis: the lead's round-2 priority-6 item and Part 2 (Rare milestone events).

Decisions:

- Ten milestones, each a permanent global flag, an Event 006 history row through `record_events_log_system_history_entry` (payloads 40 to 49, after the existing 1-4, 23, 24 and 30-35) and a `major = yes` news event `chaosx.nr6.190` to `.199`. The first League congress news (`.35`) and the danger milestone (super-event 24) stay as they are, so "first league congress convened" is not duplicated.
- Each fires from the transaction that proves it, never from a scan: broad recognition and the one-state major from the state refresh (through the achievement refresh, which the refresh already calls); the peaceful treaty from `independence_wave_set_host_outcome` (recognized separation, living host, not at war); the host annexation from the existing `on_annex` achievement handler (annexer is the country's own former host); the regional formable from the shared formable commit and the FORM-05 proclamation; the collective rescue from the DM-44 rescue proof; the cross-regional League from the League value refresh; the radical bloc from DM-58 and DM-59; the survivor counts from the wave commit.
- Thresholds: "broad recognition" is treaty-backed recognition (60), the band at which several governments maintain relations; "cross-regional" is a formal, durable or reformed League with members from three regions, a lower bar than the four-region, ten-member achievement, because the milestone marks the first such League rather than a two-year proof; the survivor count counts registry entries that are still active origins. When one wave crosses both survivor thresholds, only the twenty-five news is sent.
- Milestones feed AI: the statehood incident `ai_chance` blocks read six of the flags (security after the first host annexation, arms after the first rescue, paid recognition after the first broad recognition, conciliation after the first peaceful treaty, collective war after the first radical bloc, union answers after the first union). Achievement proofs are unchanged; the milestone calls sit in the same transactions as the matching achievement writers.
- History detail: ten payload branches were added to the Event 006 block of the shared `chaosx_scripted_localisation_events_log.txt` with one minimal insertion before the Event 006 fallback.
- Pictures: registered vanilla news pictures and the Event 006 league congress picture; no new art.

Validation: brace balance 0 on all touched files; every milestone effect, constant and localisation key referenced is defined once.

Needs live game: each news firing once, the history rows and their detail text in the Event Logs.


## D18. Round 2: package contacts as a foreign-reaction source, and no score from major status

Disposition: `implemented`.

Basis: the lead's round-2 priority-7 item and the accepted foreign reactions contract (candidate and score sections: verified package contacts and registered regional stakeholders are an actor source, and major status alone supplies neither a contact nor score).

Decisions:

- Registry: `common/scripted_effects/006_independence_wave_package_contact_effects.txt` gives each of the 37 attested packages two or three researched contacts (92 rows), each with a one-line basis in the source comment and in `docs/events/006_independence_wave/package_contacts.md`. Bases are recorded 1918-1939 relationships: cross-border kin, emigrant and exile communities, the Promethean movement sponsored from Warsaw, interwar occupation or sponsorship, and long-standing trade. Examples: RUT with HUN, POL and ROM (its host CZE is excluded as an actor); CAT with FRA, SOV and MEX; NAV with FRA and ENG; GLC with POR, ARG and CUB; the Caucasus packages with TUR, FRA, POL or PER.
- Registration: `independence_wave_register_package_contacts` runs in `independence_wave_commit_prepared_country_origin`, so only a fully validated origin registers; it clears and rebuilds the bounded country array `independence_wave_package_contact_entries`. The generation reset and origin end clear it.
- Builder: each cohort target's contacts are the first actor source, before neighbors, patrons, recognizers, host allies and earlier-wave countries, so the actor cap never drops a researched contact. Candidate validity (living, sovereign, not the target or its host, not in the cohort) is unchanged.
- Score: a registered contact is a recorded-relationship fact (three points), shown in the event reason as "Our ties with its people are older than its new government, through kin, exiles or trade." The strategic-fit fact "a great power on the target's continent" is removed from both the foreign builder and the remnant petition ranking, and its reason line is retired. Military access, the host-border balance and a shared Event 006 region remain.
- Profiles: the great-power profile now needs `is_major` and a recorded relationship (which includes a package contact); a registered contact also qualifies an actor for the regional-stakeholder profile. A great power without a contact takes the profile its other facts give it.

CAT walk-through (one wave with IW-014): origin commit registers FRA, SOV and MEX on CAT. The builder's contact loop adds FRA first (living, sovereign, not SPR, not in the cohort). FRA scores direct stake 4 (shared Pyrenean frontier) plus recorded relationship 3 (contact) plus political fit 1 when both are democratic, 7 or 8, above the cutoff of 6, and as a major with a contact it receives the great-power profile `.67`. Without the contact FRA would score 5 and stay in the public report only; before this change it reached 7 through the continental-reach fact, which is the major-status score the contract forbids. SOV and MEX enter the pool through the same source but stay below the cutoff (3, or 4 with shared ideology).

Remnant petition: without the continental fact, a recipient needs a frontier or alliance plus access, or a frontier and an alliance together, to reach 6. The petition remains reachable for a neighbouring ally, which is its usual recipient.

Not attempted: the contract's probability baseline and comparison for the changed deterministic score (scores are deterministic ranks, not action probabilities; the probability route returned INTERNAL_ERROR earlier this round).

Needs live game: a CAT or RUT wave in which the contact governments appear among the foreign reactions with the contact reason line.


## D19. Round 2: admission of IW-093 Asante (DOX) and IW-098 Sokoto (SOK)

Disposition: `implemented`.

Basis: the lead's round-2 priority-8 item, decision 5 (every admission includes the ROOT-to-PREV fix) and the round-1 admission standard (a photo of the correct 1936-role person within about ten years, the parent as rights reviewer, no generated face of a real person).

Setup defects found and fixed (each one failed every release):

- ROOT read for the carrier: the fixed anchor ownership proofs, the Kumasi capital proof, the Sokoto anchor proof and both host capital survival proofs compared the anchor or host with ROOT, the launching country during the executor passes. They now read PREV. The host-negotiation, counterparty and settlement triggers also read PREV (or PREV.PREV inside the host's own event), which keeps their meaning in the events and decisions that use them.
- `has_independence_wave_iw093_runtime_content_attestation` and `_iw098_` required package flags that no file ever set. They now bind only the carrier tag; the static content attestation is the admission proof, as for every other admitted package.
- The planner gate also required the legacy `independence_wave_package_content_ready` flag, which is never set; it now proves the exact dormant tag, like CHU and ASY.
- The DOX history sets no government, so Prempeh II could not be the ruling leader when the leadership proof ran. Both packages now form their neutrality government before promoting the leader.
- Cleanup retired Prempeh II, the DOX commanders and the SOK commanders, all recruited only by startup history, so a second release of either tag failed setup (the D11 NAV defect). Cleanup keeps them.

Sokoto leadership: before 17 June 1938 the new `SOK_independence_wave_hasan_dan_muazu` (startup history roster, despotism) is promoted and attested; from that date the vanilla `SOK_siddiq_abubakar` is. A Sokoto released before the cutover runs its own hidden check (`chaosx.nr006.9810`, every 14 days, guarded by a due date through `chaosx_convert_days_to_date_offset`) and on the cutover fires `chaosx.nr006.9811` "A New Sultan in Sokoto": Hasan dies, Siddiq succeeds and takes the government if Hasan led it, and the receipts move to the post-cutover branch.

Portraits:

- Hasan dan Mu'azu: source placeholder from the archived June 1934 London Zoological Gardens group photograph (Commons, Public Domain Mark), cropped to his head and shoulders with the event-assets crop tool (manual crop 624,300,1007,815 around the Commons face annotation) and converted with its DDS converter. As rights reviewer the parent accepts the 1934 date, because Abdullahi Bayero, named in the same caption as Emir of Kano, became Emir only in 1926 and Hasan became Sultan in 1931, which rules out the 1924 date of a later press caption; a UK photograph of unknown authorship from 1934 left copyright at the end of 2004. Evidence and the completed provenance contract are in the local, git-ignored `docs/assets/portraits/006_independence_wave/round2_source_placeholders/`. No ImageGen, repaint or RunPod was used. Route gap: `chaosx_portrait_creator` could not be spawned in this run.
- Prempeh II and Muhammadu Dikko keep the user-supplied HOI4-style finals installed on 2026-08-21, which is the intended final state for grounded subjects.
- Kwame Frimpong, Kwaku Ntim and Bello Rabah are fictional officers; their portraits depict no real person, so the no-real-person rule does not apply. They remain for the new armies of the two packages.

Flags: DOX keeps the Asante tricolour with the Golden Stool shared with Event 012's DOX carrier (commit `da5fd37da`), with identical ideology and route variants and medium and small sizes; no route-specific flag is added. SOK keeps the vanilla Sokoto ideology flags of its vanilla carrier. The Event 006 flag audit passes (102 complete families).

Formables: FORM-24 (West African Federation) and FORM-25 (Sahel Confederation) are recorded as fail-closed. Setup registers each family profile for discovery and the package readiness triggers track progress, but neither family has a carrier tag, member roster, territory proof, consent rule or flag, and neither is in the shared commit allowlist. Opening them belongs to the formable item.

Admission: IDs 93 and 98 are in the content attestation and the Join probe order; their execution and SCN-008 preflights, ranked-list entries, planner and reservation publishers and AI strategy profiles already existed. Both are signature-depth packages and stay high-chaos only. Foreign contacts: DOX registers FRA and USA, SOK registers FRA and SAU.

Walk-through (DOX, then SOK): the loaders publish region `west_central_africa`, depth `signature` and archetype `agrarian_regional`, matching the prepared-scope proofs; the executor sets the anchor (274 or 902) as capital before setup; the leader is promoted after the government is formed; the anchor, capital and host proofs read the released country; both commanders exist with corps-commander roles from startup history; values, the opening idea, the focus framework with signature and formable flags and the mapped force (p93 `river_jungle` 64, p98 `mounted_mobile` 70) are written before the setup receipt; final validation reads the same receipts.

Validation: the allocator audit passes with 39 attested packages, 34 reservation groups, 41 adapters and IW-177 and IW-179 as the only adapter-only rows (its expected sets were updated); the country API, flag and SCN-008 matrix audits pass; brace balance is 0 on all touched files.

Needs live game: a high-chaos wave or SCN-008 launch that releases DOX or SOK; Hasan leading a pre-1938 Sokoto and the June 1938 succession event.


## D20. Round 2: admission of the Volga and Siberian packages; FER stays blocked

Disposition: `implemented` for IW-047 MEL, IW-048 UDM, IW-050 KOM, IW-051 YAK, IW-052 BYA, IW-053 ALT and IW-054 KHA; `blocked` for IW-057 FER.

Basis: the lead's round-2 priority-9 item and decision 5.

Identity decision: each of the seven is a vanilla carrier, and its vanilla roster is the accepted package identity: `MEL_zinovy_zhadinov`, `UDM_boris`, `KOM_pavel_murashev`, `YAK_pavel_pevznyak` (with the user-supplied final already wired as a character-scoped override) and `YAK_anatoly_pepelyayev`, `BYA_seymon_ignatyev` and `BYA_bidia_dandaron`, `ALT_grigory_gurkin` and `ALT_samuil_yufit`. Event 006 adds no character, portrait or flag; the faces are the game's own assets. KHA has no vanilla characters, so it keeps its vanilla roster and the leader the game appoints, which is the accepted institutional leadership. The parent-owned `independence_wave_iw_0XX_identity_rights_cleared` flags, and KHA's `independence_wave_kha_institutional_roster_ready`, are now published at the start of each package setup, with this decision as their basis. UDM therefore uses its vanilla leadership with no Event 006 face, as the item allows.

Setup defects found and fixed:

- ROOT read for the carrier in every package: the anchor ownership, capital and host proofs in `can_initialize_*`, `has_prepared_*` and the runtime-ready triggers compared with ROOT, the launching country during setup. All now read PREV (state and host scopes entered from the carrier); the unsettled-host and host-settlement checks also read PREV.
- YAK: the p51 force mapping (mask 647) raises integrate-militias, regional guards, secure depots, terrain units and professional officers, but setup and the prepared proof expected convert-defectors and forbade integrate-militias, so YAK always failed setup. Both now follow the mask.
- KHA: the p54 mapping (mask 1159) raises capital-border defense, not professional officers, and the loader and candidate registry give KHA standard depth while its proofs required regional depth. Both are fixed, so KHA can pass setup.
- ALT: the prepared proof read `independence_wave_force_reinforcement_pathway_count`, which nothing writes; it now reads `independence_wave_reinforcement_pathway_count`. ALT's mapped tradition (p53 = 61) already equals its accepted tradition, so the stale "blocked" branch never fires.
- The planner gates used the retired `independence_wave_package_content_ready` flag; they now use new `is_independence_wave_runtime_automatic_package_iw_0XX_ready` triggers, as BSK does.

Walk-through (all seven): the loaders publish region `volga_urals_siberia_far_east` and the depth and archetype each package checks (MEL standard river-or-corridor, UDM standard industrial breakaway, KOM and ALT standard mountain-or-frontier, YAK and BYA regional mountain-or-frontier, KHA standard mountain-or-frontier); the decoded force profiles (p47 river_jungle, p48 industrial_security, p50 and p51 mountain_frontier, p52, p53 and p54 mounted_mobile), traditions and reinforcement masks now match every prepared proof; every roster character is recruited at the top level of its vanilla 1936 history; the identity flags are set before `can_initialize_*`, which ALT, BYA and KHA read through their command-roster triggers; the cosmetic route tags used by MEL and YAK have flags in all three sizes and localisation.

Admission: the seven IDs are in the adapter list, the content attestation, the execution and SCN-008 preflights, the Join probe order, the Liberations capacity probe and the three central package dispatchers. They were already in the SCN-008 ranked list, and their AI strategy profiles already existed. MEL shares RG-MIDDLE-VOLGA-KAZAN with TAT and CHU, so a wave holds at most one of the three. Foreign contacts: MEL FIN and EST, UDM FIN and HUN, KOM FIN and EST, YAK MAN and JAP, BYA MON, MAN and JAP, ALT MON and TAN, KHA TAN and MON.

Formables: FORM-12 and FORM-13 invite exactly TAT, BSK, MEL, UDM and KOM, so three more of their member rows can now exist; their three-member, three-anchor rule is unchanged. FORM-14 (Siberian Federation) has a discovery profile only: no carrier, member contract, consent or flag, and it is not in the commit allowlist, so it stays closed.

FER blocked: the vanilla FER tag has no characters and Event 006 has no sourced FER roster; its setup requires `independence_wave_iw_057_command_roster_ready`, and its vanilla flags are not the neutral flag with recorded provenance that the item requires. A sourced roster needs new photographs, which this run cannot download without the user's approval. FER stays out of the adapter list and unattested; its ROOT reads are left for its own admission.

Validation: the allocator audit passes with 46 attested packages, 40 reservation groups and 48 adapters (its expected sets, group and anchor counts and the dispatcher-family count of 34 were updated); the country API, flag and SCN-008 matrix audits pass; brace balance is 0 on every touched file.

Needs live game: a wave that releases one of the seven, especially YAK, KHA and ALT, whose force proofs changed.


## D21. Round 2: Fiji admitted, Micronesia stays blocked, FORM-48 reviewed

Disposition: `implemented` for IW-177 FIJ and for the startup-roster cleanup fix; `blocked` for IW-179 FSM; FORM-48 stays closed.

Basis: the lead's round-2 priority-10 item and its photo-date decision, which accepts a sourced photograph taken within about ten years of the 1936 baseline.

Identity decision: Ratu Sir Lala Sukuna is the accepted Fiji country leader. His source photograph dates from about the 1940s, which the lead's rule accepts. The HOI4-style final in the stable consumer `portrait_FIJ_independence_wave_founding_congress_chair.dds` is now the user-supplied file `portrait_FIJ_ratu_sir_lala_sukuna_source_00002.dds` (156x210) from the user's portrait output folder. It replaces an earlier agent-made repaint of a real person, which the project rules do not allow as a final. The GFX name, character id and localisation are unchanged, and no advisor, commander or small portrait was added.

Political fix: vanilla FIJ and the package both rule with the democratic party, but Sukuna's leader role and both `promote_character` calls used `centrism`, a neutrality ideology. He would have led the non-ruling party, so `has_independence_wave_fij_origin_leadership` (ruling leader) could never pass. The character and both promotions now use `liberalism`, as D13 did for CHU and ASY.

Setup defects found and fixed:

- ROOT read for the carrier: the anchor and former-host checks in `can_initialize_*` and `has_prepared_*` for IW-177 and IW-179 compared with ROOT, which is the launching country during setup. Both now read PREV, as HAW and HBX already did. The FSM settlement-cancel check also reads PREV inside its capital scope, which is the same country there.
- Planner gate: `can_plan_independence_wave_package_iw_177` checked the generic candidate wrapper. It now uses the new `is_independence_wave_runtime_automatic_package_iw_177_ready` trigger, as HAW and HBX do.
- Second release: the HAW and FIJ cleanups retired their startup-roster characters, so a later release of either tag could never restore its leader (the D11 defect class). The same defect was in the COR, KOS, MNT and RUT cleanups. Each cleanup now keeps those characters, and each setup already restores the roles through `promote_character`.

Walk-through: the loader publishes region 13 (`southeast_east_asia_oceania`), regional depth and the `port_or_island` archetype, which the proofs check. The p177 force profile decodes to `coastal_maritime` and its tradition constant matches the prepared proof. FIJ's proofs check no reinforcement pathway, so the mask (659) needs no match. Sukuna is recruited by the shared history roster, and the vanilla tree is `generic_focus`, which the setup requires.

Admission: IW-177 is in the content attestation, the Liberations capacity probe (new `independence_wave_liberations_capacity_try_iw_177`) and the Join probe order after IW-054. It was already in the adapter list, the execution and SCN-008 preflights, the SCN-008 ranked list and the Pacific dispatchers. It reserves `RG-PACIFIC-ISLANDS`, which it shares with the unadmitted IW-175 SAM and IW-179 FSM. Foreign contacts: AST and NZL.

FSM blocked: Micronesia has no sourced 1936 leader, `independence_wave_fsm_sourced_identity_ready` stays unset, and the user's portrait folder has no FSM final. A sourced leader needs new photographs, which this run cannot download without the user's approval. FSM stays out of the attestation, and its setup keeps failing closed.

FORM-48: its contract binds HBX as carrier and HAW and FSM as sovereign members. HBX and HAW are admitted, but FSM is not, and no substitute member is invented, so the family stays unreachable. IW-183 Cascadia (HAX) has no package and is not a FORM-48 member. FORM-39 (FIJ, PNG and WPG) also stays closed, since PNG and WPG are unadmitted and the MFX flag still awaits user review.

Validation: the allocator audit passes with 47 attested packages, 41 reservation groups, 48 adapters and IW-179 as the only adapter-only ID (its expected attested set and its group and anchor counts were updated); brace balance is 0 on every touched file.

Needs live game: a wave that releases FIJ, and a second release of HAW, COR, KOS, MNT or RUT after an earlier one ended.


## D22. Round 2: admission of IW-060 Kurdistan (KUR) and IW-095 Dahomey (DAH)

Disposition: `implemented` for IW-060 KUR and IW-095 DAH.

Basis: the lead's round-2 priority-10b item, decision 5 (every admission includes the ROOT-to-PREV fix), and the D20 rule that a vanilla carrier's vanilla roster is its accepted package identity.

Anchor decision for KUR: the package-local proofs required state 421 (Ilam), but the loader, the planner gate and the reservation all bind state 1001, and the executor moves the capital to the reserved anchor. The proofs could therefore never pass. State 1001 is the accepted anchor. It is the vanilla state named Kurdistan, around Sanandaj, it is a KUR core with victory points, and it lies in the Iranian Kurdish heartland where Qazi Muhammad later led the Mahabad republic. State 421 (Ilam) is a southern border state with no victory point. The KUR triggers, the founding mission and its description now read state 1001. FORM-18 reads each member's stored anchor rather than a fixed state, so it needs no change. Vanilla KUR history keeps state 800 (Van) as its capital, and no history or map file changes.

Identity decision: both are vanilla carriers. KUR keeps its vanilla roster: Seyid Riza leads the opening democratic government, with Qazi Muhammad, Mahmud Barzanji and Ihsan Nuri leading the other parties, all with the game's own portraits, and the vanilla KUR flags. Vanilla DAH defines advisors but no country leader, so it keeps its vanilla roster and the leader the game appoints, which is the accepted institutional leadership, as D20 accepted for KHA. Event 006 adds no character, portrait or flag for either. The parent-owned `independence_wave_iw_060_identity_rights_cleared` and `independence_wave_iw_095_identity_rights_cleared` flags, and DAH's `independence_wave_dah_roster_checkpoint`, are now published at the start of each package setup with this decision as their basis.

Setup defects found and fixed:

- KUR anchor mismatch, described above.
- KUR read ROOT, the launching country during setup, in the anchor and former-host checks of `can_initialize_*`, `has_prepared_*` and the runtime-ready trigger. DAH read ROOT in its runtime-ready trigger. All now read PREV, and so do the unsettled-host and host-settlement checks of both packages.
- DAH setup required a roster receipt that nothing published, so it always failed. Setup now publishes the identity flag and runs `independence_wave_dahomey_checkpoint_roster`.
- DAH cleanup restored a democratic government with 60/10/10/20 popularities, but vanilla DAH is ruled by its neutral party without elections at 25/5/50/20. The cleanup and its constants now match vanilla. KUR cleanup restored its vanilla popularities as bare numbers. They are now `restore_*` constants in `independence_wave_kurdistan_politics`.

Walk-through: the KUR loader publishes region `caucasus_anatolia_mesopotamia`, regional depth and `mountain_or_frontier`, and DAH's publishes `west_central_africa`, regional depth and `agrarian_regional`, which the proofs check. p60 decodes to `mountain_frontier`, tradition 72 and mask 653, which raises integrate-militias, secure depots, convert-defectors, terrain units and professional officers, exactly the five pathways the KUR proof expects. p95 decodes to `territorial_defense`, tradition 57 and mask 535, which raises integrate-militias, regional guards, secure depots, volunteer corridors and professional officers, exactly the DAH proof. Neither inherits a navy or air force. The KUR roster characters are recruited by vanilla KUR history.

Admission: both IDs are in the adapter list, the content attestation, the execution and SCN-008 preflights, the Join probe order after IW-177, the Liberations capacity probe (new tries) and the central dispatchers (the `kurdistan` and `first_footprint` families). The planner gates use new runtime-ready triggers. Both were already in the SCN-008 ranked list, and their AI strategy profiles, shared-focus callbacks, decisions and ideas already existed. KUR shares `RG-NORTHERN-MESOPOTAMIA` with the admitted IW-058 ASY, and DAH shares `RG-NIGERIA-COARSE` with the admitted IW-098 SOK, so a wave holds at most one of each pair. Foreign contacts: KUR IRQ, TUR and SOV. DAH POR, BRA and ENG.

Validation: the allocator audit passes with 49 attested packages, 41 reservation groups, 50 adapters and 48 anchors (its expected sets, anchor count and the dispatcher-family count of 36 were updated); brace balance is 0 on every touched file.

Remaining gap: a DAH cleanup keeps the Event 006 party names, since vanilla DAH has no party name keys to restore.

Needs live game: a wave that releases KUR from Iran with state 1001 as its capital, and a wave that releases DAH.


## D23. Round 2: FORM-08 Danubian Confederation made operational

Disposition: `implemented`.

Basis: the lead's round-2 priority-11 item (formables). The FORM-08 matrix row names Transylvania, Banat, Vojvodina, Slavonia and compatible members, sets no numeric minimum, and requires any new formable or route tag to end in X.

Defects that kept FORM-08 from ever forming:

- Member count: the registry required three members, consents and anchors, but the geography guard admits only TRA (state 84) and AXX (state 82). Vojvodina is a HUN-origin overlay and Slavonia has no unique map anchor, so a third member could never exist. FORM-08 is now a two-member family (`minimum_members`, `minimum_consents` and `minimum_anchors` are 2), the same shape as FORM-11 and FORM-18. The integration adapter already integrates `minimum_members - 1` partners, so it now integrates AXX.
- Carrier self-exclusion: `is_independence_wave_form08_eligible_member` rejected any country with an open founding proposal. The carrier check, the member ledger and the commit proof all run through it while the carrier's own proposal is open, and `has_valid_independence_wave_formable_founding_proposal` requires that proposal, so the strict mutation preconditions could never hold. The registered carrier (`independence_wave_form08_readiness_attested`) now stays eligible while its proposal is open. Other countries with their own open proposal are still excluded.
- Territory: `independence_wave_formable_state_puzzle_form08_territory` was `always = no`. It now requires states 84 and 82 to qualify. The state-puzzle summary reads "/ 2", and the consumer spec and manifest carry `summary_required_count` 2 so a regeneration keeps it.
- AI: the three FORM-08 AI strategies had `allowed = { has_cosmetic_tag = HUN_EMPIRE }`. `allowed` is checked only before the game starts (offline wiki, AI modding, Arguments), when no country holds that cosmetic tag, so they never applied. They now use `allowed = { original_tag = TRA }`, and their `enable` blocks still require a formed confederation.
- Identity lock: the cleanup cleared the global identity lock for every country that ran it. Only the carrier that holds the identity or the carrier flag releases it now, as D7 did for IFX.

Identity decision: FORM-08 no longer reuses the vanilla `HUN_EMPIRE` cosmetic. That identity named a Transylvania and Banat federation "Austria-Hungary" or "Austro-Hungarian Empire" under neutral or fascist governments, broke the X-ending tag rule, and was blocked whenever Hungary formed Austria-Hungary. The carrier now takes the X-ending cosmetic tag `DCX` ("Danubian Confederation"; communist "Danubian Union of Councils", fascist "Danubian Federal State"). Its flag is an alternate-history civic synthesis of the member colours: navy over crimson split by a gold-edged white wave for the Danube, with two gold stars for the founders. It was generated with ChatGPT Images through the `gptimage` MCP. All three attempts drew the design but added vignette shading to the large fields, so the accepted master was flattened to its four design colours before the Lanczos exports. That processing step is recorded in `docs/assets/006_independence_wave/form08_danubian_confederation_flag_2026_10_05/manifest.md`. The collision scan for `DCX` over the mod, vanilla, the Workshop folder and sibling local mods found no use. The renamed flags `independence_wave_form08_identity_attested` and `independence_wave_form08_identity_in_use` keep their requirement localisation.

MCP: a narrow `hoi4.gui_render` call on `chaosx_independence_wave_formable_state_puzzle_window` was rejected as invalid arguments by the tool schema, as in D7, and was not retried. The only GUI-facing change is the summary count in an existing string; no layout, sprite or click region changed.

Validation: the allocator, flag, country API and SCN-008 matrix audits pass; brace balance is 0 on every touched file.

Related D22 gap: the FORM-18 state puzzle still draws its KUR piece from state 421 (Ilam), while KUR is now anchored at state 1001. The piece qualifies from KUR's membership, not from ownership of 421, so gameplay is unaffected, but the picture shows the wrong state. Moving the piece needs new geometry from the state-puzzle generator and a shared GUI regeneration, which is queued for the next FORM-18 tranche. FORM-18 also still lacks its admitted CJX member (IW-062).

Needs live game: a TRA carrier inviting AXX, the congress vote and commit, the DCX names and flag, AXX's integration, and the FORM-08 post-formation decisions and AI.


## D24. Round 2: FORM-11 Cossack Host Federation, member invitation scope and FORM-09 member proofs

Disposition: `implemented`.

Basis: the lead's round-2 priority-11 item (formables). The FORM-11 matrix row names Don, Kuban and compatible Cossack packages, the host-capital and steppe-corridor proof, a host assembly route, and civilian control, cavalry integration and Russian settlement as the integration policy, and requires an X-ending tag. Part 5 keeps state 218 (Rostov) outside the Don package and leaves the FORM-11 carrier unresolved; this decision resolves it.

FORM-11 decisions:

- Members and carriers: DON (IW-039, anchor 245) and KUB (IW-040, anchor 234). RG-DON-KUBAN releases at most one of them per wave, so the family forms across two waves. The profile row was already a two-member family (two members, consents and anchors; negotiated federation or military settlement). Either host can carry it, as AFX or AGX can carry FORM-03; the shared global identity lock allows one carrier at a time, and the proposal dispatch never invites a country with its own open proposal.
- Gates: each package selects FORM-11 at its own later gate, never at release. DON selects it when the Millerovo host charter succeeds (the existing `independence_wave_don_form11_docket_open` marker now has its consumer); KUB selects it when it codifies durable sovereignty. Registration attests readiness only while the host owns and controls its anchor as capital.
- Identity: X-ending cosmetic tag `CHX` ("Cossack Host Federation"; communist "Federation of Cossack Soviets", fascist "Cossack Federal Directorate"). The collision scan over the mod, vanilla, the Workshop folder and sibling local mods found no use of `CHX`. Flag: an alternate-history synthesis of the Don blue-gold-red and Kuban blue-raspberry-green tricolours with a green hoist triangle and two crossed white lances for the two hosts, generated with ChatGPT Images through the `gptimage` MCP. Both attempts added vignette shading, so the accepted master was flattened by hue class (RGB nearest-colour flattening would have turned the darkest blue into green); the step is recorded in the local `docs/assets/006_independence_wave/form11_cossack_host_federation_flag_2026_10_05/manifest.md`.
- Territory: the state puzzle requires states 245 and 234 to qualify. State 218 is not a candidate, and no transfer, claim or core touches it.
- Consent and connection: the shared invitation decisions apply. The member needs a faction, non-aggression pact, access, guarantee, land border or a shared Event 006 region with the carrier. Both hosts are in `eastern_europe_western_russia`, which stands in for a land border that Rostov usually blocks.
- Integration policy: a member that authorizes full integration ends its origin and transfers only its own host states (245 and 238 for DON, 234 for KUB). Any other consenting member becomes a sovereign autonomous host member (reciprocal access and guarantees through the shared helper, plus the Autonomous Host Membership idea). The full-compact-control trigger now lists DON 245, KUB 234 and also AXX 82, so FORM-08 members can authorize the full integration its adapter already supported.
- Post-formation: the Host Federation Charter category tracks civilian control (35 at formation), cavalry integration (40) and resident settlement (30), clamped 0 to 100, with provisional, coordinated (all 50) and integrated (all 75) charter ideas. Three one-time projects run one at a time: Seat the Federal Host Council (administration cost, 120 days), Raise the Federal Mounted Corps (security cost, 150 days) and Open the Stanitsa Lands (strategic cost, 180 days, after the council; lowers cavalry integration as host privileges shrink). After all three, the ledgers reach 60/55/55 and the charter is coordinated. The repeatable Convene the Grand Host Circle (50 political power, 75 days, 180-day cooldown) adds 5 to each ledger and reaches the integrated charter after four sessions.
- AI: decision weights follow `independence_wave_decision_ai` (council doubled on the constitutional route, corps raised under a severe host threat or on the emergency route, lands preferred on civic routes and halved under a severe host threat). Three AI strategies (`allowed` on `original_tag` DON or KUB) build the army and avoid wars until the charter projects are complete.
- State puzzle: a FORM-11 consumer spec and its two exact-geometry pieces were compiled with the archived consumer compiler (its module root redirected to the repository, no code change). The runtime generator is not byte-stable on two shared files (the localisation file carries hand-added category aliases, and the scripted localisation still carried D23's unreachable FORM-08 count-3 branch), so the generated GFX, grouped GUI and scripted GUI were installed after confirming that their diff contains only FORM-11 and FORM-18 lines, the scripted localisation was installed after confirming its block diff contains only FORM-08, FORM-11, FORM-18 and state 234/245/1001 blocks, and the five new localisation keys were inserted into the shared localisation file by hand.

Shared defects found and fixed:

- Invitation scope: `has_valid_independence_wave_formable_founding_invitation` is evaluated in the invited member's own scope (its decisions, its consent events and the consent effects), where ROOT is the member. The FORM-08, FORM-09, FORM-12, FORM-13 and FORM-18 branches used member-candidate triggers that require `NOT = { tag = ROOT }` and, for the signature families, `ROOT` to be the carrier, so every human member reply and every FORM-08 AI reply (which goes through the shared membership decisions) was rejected; FORM-08 could never collect its second consent. The branches now read the carrier from the stored invitation: FORM-08 and FORM-11 use the member trigger plus no war with the inviting carrier, FORM-09 uses its eligibility trigger, and new `is_independence_wave_iw043_formable_invited_member` and `is_independence_wave_iw058_formable_invited_member` share a ROOT-free identity trigger with the unchanged candidate triggers that the dispatch and ledger use with the carrier as ROOT.
- FORM-09 members and carriers read `has_complete_independence_wave_iw_02X_package_setup`, whose origin activation flag the origin commit clears, so no released Balkan package could ever be a FORM-09 member or carrier (the D14 defect class). They now read each package's persistent setup receipt. The FORM-09 state-puzzle pieces also used the member eligibility that excludes a country with an open proposal, so the carrier's own anchor never qualified while it was proposing; they now use `is_independence_wave_form09_member`, which includes the exact carrier.
- FORM-18's Kurdistan piece showed state 421; it now shows state 1001, the accepted KUR anchor (D22 gap). FORM-18 still requires the unadmitted CJX member.

MCP: `hoi4.gui_inspect` (window `chaosx_independence_wave_formable_state_puzzle_window`, with and without a scenario) and `hoi4.gui_render` (same window, scenario with controls, 1920x1080) were rejected as invalid tool arguments, as in D7 and D23; not retried. Source evidence instead: the FORM-11 pieces are 123x83 at (140,89) and 92x66 at (208,8), and the FORM-18 pieces end at y 172 at most, all inside the 440x180 map container.

Validation: the allocator, country API, flag, FORM-16, SCN-008 matrix and GUI matrix audits pass; brace balance is 0 on every touched script file; every scripted trigger, effect and script constant referenced by the added lines is defined.

Needs live game: a DON wave and a later KUB wave, the charter and durable-sovereignty gates, the invitation, a member reply, the congress, the CHX names and flag, both integration choices, the charter projects, and a human member replying to a FORM-08 or FORM-09 invitation.


## D25. Round 2: regional framework engine and the Levant and Arabia tranche

Disposition: `implemented` for the framework engine and for IW-073 Hejaz (CUX), IW-076 Hadhramaut (CXX), IW-078 Imamate of Oman (IMO), IW-081 Lebanon (LEB) and IW-082 Palestine (PAL); `blocked` for IW-074, IW-075, IW-077, IW-079 and IW-080.

Basis: the lead's round-2 priority-12 item (regional coverage, Levant and Arabia) and decision 5. Every bound row needs at least a Level 1 package, and Level 2 rows also need a decision family, a starting problem and incidents.

Engine decision: most remaining rows already have a planner gate, loader, reservation, SCN-008 rank and force mapping, but no package engine, so the finalizer rejects them. Rather than copying a bespoke engine per row, one shared Level 1 engine (`common/scripted_effects/006_independence_wave_regional_framework_effects.txt` and its triggers) sets up any listed row: it checks the released country's anchor capital and former host, assigns the full Event 006 tree, allows the four host routes, registers the ambition family and League route, reloads the force mapping (whose loader already raises the mask's reinforcement pathways) and applies the dynamic starting force. The only per-row code is one identity block (identity basis, leadership, government routes, power centres) and one exact id-to-tag line. The engine reads the released country and its stored anchor and host, never ROOT; prepared, complete and runtime-ready checks mirror the bespoke packages; cleanup acts only for the generation that set the package up and restores a ruling party the row changed. The regional identity overlay, archetype and ambition family come from the shared systems, which is what Part 5 lists for Level 1. Level 2 content stays bespoke per row and is not generated from a template.

Leadership decisions (D20 and D22 rule: a vanilla roster is an accepted identity, and the leader the game appoints is accepted institutional leadership; no face is generated for a real person):

- IMO keeps the vanilla Imam Muhammad bin Abdullah al-Khalili, Imam of Oman from 1920 to 1954.
- LEB keeps its vanilla roster led by Abdallah Bayhum.
- If a vanilla leader is no longer present, the game appoints one; the framework records a roster checkpoint only when the vanilla leader exists, so a missing character never stops the all-or-nothing wave.
- PAL's vanilla government is the mandate administration under the British High Commissioner. A released Palestine opens under its democratic party, led by the vanilla Ahmed Hilmi Pasha, and suspends the High Commissioner's leader role for its own generation (`remove_country_leader_role`); cleanup re-adds the role with its exact vanilla ideology, trait and expiry and restores the recorded ruling party.
- CUX and CXX are institutional councils led by the leader the game appoints. Sourced leaders need new photographs, which this run cannot download without the user's approval. Their registered flags and names already exist (the flag audit counts them among the 102 complete families).
- CUX and CXX are custom X-tags, so each gets a `create_dynamic_country` branch in the release step and the baseline-law entry of the custom-carrier startup helper.

Government routes follow each row's researched route pool; radical sovereignty is excluded for all five. Power centres: traditional authority and assembly (CUX, IMO), central government and provinces (CXX, PAL), domestic cabinet and foreign patron (LEB).

Level 2 layers (`common/scripted_effects/006_independence_wave_levant_arabia_package_effects.txt`, decisions in `common/decisions/006_independence_wave_levant_arabia_decisions.txt`): each row starts with a problem idea and has three or four paid projects through the shared cost helpers, with mutually exclusive settlements where the history offers a real choice (Lebanon's confessional apportionment or a civic charter; Oman's renewed Treaty of Seeb or a closed coast road). Incidents `chaosx.nr6.200` to `.207` (two per row) use the package incident scheduler. The full description is in `docs/events/006_independence_wave/levant_arabia_packages.md`.

Admission: the five ids are in the adapter list, the content attestation, the execution and SCN-008 preflights, the Join probe order, the Liberations capacity probe and the three central dispatchers (one new `regional_framework` family); the planner gates read the new runtime-ready triggers. They were already in the SCN-008 ranked list. Foreign contacts: CUX IRQ, JOR and EGY; CXX ENG, YEM and HOL; IMO ENG and SAU; LEB FRA, SYR and BRA; PAL ENG, EGY and JOR. LEB and PAL share RG-LEVANT-MESOPOTAMIA-COARSE, so a wave holds at most one of them.

Walk-through (all five): the loaders publish region `levant_arabia`; the force mapping exists for p73, p76, p78, p81 and p82 with no navy or air inheritance; the executor moves the capital to the anchor before setup; `can_initialize` reads the setup targets; the identity block writes the roster and route receipts that `has_prepared` requires; the force loader writes the mapping, pathway and application receipts; the setup receipt persists after commit for the decisions; IMO and LEB recruit their roster at the top level of their vanilla 1936 history files.

Blocked rows:

- IW-074 Najd: disposition formable or route only, and its anchor 292 holds the Saudi capital, which the planner protects; no route consumer exists.
- IW-075 Jabal Shammar, IW-077 Mahra, IW-079 Jabal al-Druze and IW-080 Syrian Coast: no planner gate, loader or reservation exists. IW-075 could be bound to state 857 (Ha'il) in a later tranche; the other three need a map state the current map does not have.

Validation: the allocator audit passes with 54 attested packages, 45 reservation groups and 55 adapters (its expected sets, dispatcher-family count of 37, group and anchor counts were updated); the country API, flag, FORM-16 and SCN-008 matrix audits pass; brace balance is 0 on every touched file; every referenced trigger, effect, constant and localisation key exists once.

Needs live game: a wave or SCN-008 launch that releases IMO from Oman and CUX from Saudi Arabia (the dynamic-country path), the Palestine leader swap and its restoration after an origin ends, and the decision and incident flow of each Level 2 row.


## D26. Round 2: North Africa and Sahara tranche

Disposition: `implemented` for IW-083 Rif (RIF) and IW-086 Tripolitania (DHX); `blocked` for IW-084, IW-087, IW-088, IW-089, IW-090, IW-091 and IW-092; IW-085 Cyrenaica stays an implemented vanilla-overlay package.

Basis: the lead's round-2 priority-13 item, using the D25 regional framework engine.

Decisions:

- RIF (Level 2) keeps its vanilla roster: Muhammad ibn Abd el-Krim al-Khattabi, President of the Rif Republic from 1921 to 1926. State 290 carries a RIF core, so the ordinary `release` path creates it. Routes: constitutional, traditional, emergency, patron client; power centres: the republic and the tribes. Its layer starts with The Tribal Levies and offers four projects (the National Assembly of Ajdir, unified levies, mountain redoubts and the Ajdir road and telephone network) and two incidents, Veterans of Anual (`chaosx.nr6.208`) and The Mines of Uixan (`chaosx.nr6.209`).
- DHX (Level 1) is an institutional council in the tradition of the 1918 Tripolitanian Republic, led by the leader the game appoints; it is created as a dynamic country with its registered flags and names. Routes: constitutional, popular council, traditional, emergency, patron client.
- Contacts: RIF FRA, MOR and SOV; DHX TUR, EGY and TUN.

Blocked rows:

- IW-089 Darfur and IW-091 Toubou: their anchors (767 and 775) have `force_link_ownership_to` in the installed map history, so they cannot be owned apart from the state they are linked to; IW-091 is also an unresearched reservation with no history or names.
- IW-088 Tuareg Confederation: no planner gate, an unresearched reservation, and forced ownership links on states 514 and 515.
- IW-084 Kabylia, IW-087 Fezzan, IW-090 Wadai and IW-092 Amazigh Atlas: no planner gate, loader or reservation, because each needs a distinct map state the current map does not have.

Validation: the allocator audit passes with 56 attested packages, 47 reservation groups and 57 adapters (expected sets and counts updated); the country API, flag and SCN-008 matrix audits pass; brace balance is 0 on every touched file; every referenced trigger, effect, constant and localisation key exists.

Needs live game: a wave that releases RIF from Spain and DHX from Italy, and the Rif decision and incident flow.


## D27. Round 2: West and Central Africa tranche

Disposition: `implemented` for IW-097 Oyo (DSX), IW-099 Kanem-Bornu (DUX), IW-106 Aro Confederacy (EBX) and IW-107 Biafran regional state (BIA); `blocked` for IW-094, IW-096, IW-100, IW-103 and IW-104. IW-097's registry Level 3 signature module is `accepted and queued`.

Basis: the lead's round-2 priority-14 item, using the D25 regional framework engine.

Decisions:

- Oyo is a registry Level 3 row. It is admitted now with a Level 2 layer (the Oyo Mesi deadlock as its starting problem, four projects and two incidents), because a release with a real layer is better than no coverage; the signature module (the Alaafin Siyanbola Ladigbolu I with a sourced portrait, the Oyo Mesi balance and city-state relations) stays queued. Leadership is the institutional government of the Oyo Mesi and the city interests, led by the leader the game appoints. Event 012's dormant Oyo sovereign, recruited by the DSX history, belongs to Event 012 and is not used.
- Kanem-Bornu (Level 2): the Shehu's council at Maiduguri, led by the leader the game appoints; a starting problem (the declining Lake Chad trade), three projects and two incidents.
- The Aro Confederacy (Level 1): a confederated council led by the appointed leader.
- The Biafran regional state (Level 1) keeps the vanilla BIA roster; its democratic government opens under the leader the game appoints, and the vanilla Akenzua II leads only on the neutrality routes.
- Institutional leadership through the leader the game appoints follows the D20 and D22 precedent. The research resolution asks for a sourced officeholder or institution and otherwise a block; the appointed leader is not presented as a real person, and a sourced leader or institutional character for each council is queued in the package doc.
- EBX and BIA share the Benue anchor 900. Both are in RG-NIGERIA-COARSE with every other Nigerian row, so a wave holds at most one of them, and once one owns state 900 the other's anchor is unavailable. The allocator audit records this as its second shared-anchor exception beside CHU and TAT.
- DSX, DUX and EBX get the dynamic-country release branch and the baseline-law entry; BIA is released from its vanilla core.
- Contacts: DSX FRA and BRA; DUX FRA and SAU; EBX ENG and FRA; BIA ENG and SPR.

Blocked rows:

- IW-094 Fante, IW-103 Luba and IW-104 Lunda: no planner gate, loader or reservation; each needs a distinct map state.
- IW-096 Benin Kingdom: no planner gate, and its registered tag BIA is the carrier of the admitted IW-107.
- IW-100 Hausa Federation: formable or route only, and its anchor 902 is IW-098 Sokoto's.

Formables: FORM-24 West African Federation and FORM-25 Sahel Confederation stay closed (no carrier tag, member contract, consent rule, territory proof or flag, and not in the commit allowlist). FORM-26 Kongo Basin Federation has no admitted member.

Validation: the allocator audit passes with 60 attested packages, 47 reservation groups and 61 adapters (expected sets, the closure text and the shared-anchor exception updated); brace balance is 0 on every touched file; every referenced trigger, effect, constant and localisation key exists.

Needs live game: a wave that releases one Nigerian framework row from Britain through the dynamic-country path, and the Oyo and Bornu decision and incident flow.


## D28. Round 2: East Africa, Horn and Great Lakes tranche

Disposition: `implemented` for IW-108 Buganda (UGA), IW-110 Rwanda (RWA), IW-111 Burundi (BRD), IW-113 Harar (HAR), IW-114 Afar state (AFA), IW-115 Somaliland sultanate federation (SOM) and IW-119 Tigray (TIG); `blocked` for IW-109, IW-112, IW-116, IW-117, IW-118 and IW-120.

Basis: the lead's round-2 priority-15 item, using the D25 regional framework engine.

Decisions:

- All seven are vanilla tags released from their vanilla cores, so no release branch is needed. Rwanda keeps Mwami Mutara III Rudahigwa, Burundi Mwami Mwambutsa IV and the Afar state Sultan Mohamed Yayyo of Aussa. Vanilla UGA, HAR, SOM and TIG have no country-leader characters, so the game appoints the leader of their opening government (the D20 and D22 rule).
- Six Level 2 layers, each with a starting problem, three paid projects and two incidents (`chaosx.nr6.214` to `.225`), grounded in the row's history: the Lukiiko and the 1900 mailo land titles in Buganda; the redrawn chiefdoms, the ubuhake cattle contracts and Lake Kivu in Rwanda; the Bezi and Batare princely houses and Lake Tanganyika in Burundi; the walled city, its merchants and the Zeila road in Harar; rival sultans, Berbera and the grazing wells in Somaliland; the princely houses, the church lands of Aksum and the highland passes in Tigray. The Afar state is Level 1. The full description is in `docs/events/006_independence_wave/east_africa_packages.md`.
- Texts that touch community questions (the Rwandan court and chiefdoms, the shrines of Harar, the Dervish veterans) describe institutions and choices, never a community as the problem.
- Contacts: UGA ENG and RAJ; RWA BEL and ENG; BRD BEL and ENG; HAR ENG, ITA and EGY; AFA ITA and FRA; SOM ITA, YEM and ENG; TIG ITA and EGY.

Blocked rows: IW-109 Bunyoro, IW-112 Ankole, IW-116 Zanzibar, IW-117 Kilwa restoration and IW-120 Oromo regional federation have no planner gate, loader or reservation (each needs a distinct map state or a named community package); IW-118 Maasai is an unresearched reservation with no history or names.

Formables: FORM-27 Great Lakes Federation, FORM-28 East African Federation and FORM-29 Horn League State stay closed (no carrier tag, member contract, consent rule, territory proof or flag, and not in the commit allowlist). FORM-27 now has three admitted candidate members (UGA, RWA, BRD) and FORM-29 four (HAR, AFA, SOM, TIG), so their carrier contracts are the natural next formable work.

Validation: the allocator audit passes with 67 attested packages, 49 reservation groups and 68 adapters (expected sets and counts updated); brace balance is 0 on every touched file; every referenced trigger, effect, constant and localisation key exists.

Needs live game: a wave that releases one Great Lakes and one Horn row, and the decision and incident flow of a Level 2 row.


## D29. Round 2: Southern Africa and Indian Ocean tranche, and named institutions for custom carriers

Disposition: `implemented` for IW-126 Barotseland (BAR), IW-130 Madagascar restoration (MAD), IW-131 Comoros (FAX) and IW-132 Mauritius (FBX), and for the named-institution governments of every custom framework carrier; `blocked` for IW-121, IW-122, IW-123, IW-124, IW-125, IW-127, IW-128 and IW-129.

Basis: the lead's round-2 priority-16 item, using the D25 regional framework engine, and the lead's per-tranche rule that a row needs a sourced leader or institution or a vanilla roster, or stays blocked.

Named institutions (correction to D25, D26 and D27): the research resolution asks custom X-tag carriers to govern through a provisional institution with a regionally sourced name. The custom carriers previously opened under an unnamed neutrality government. Each now sets its neutrality party to its institution and makes it the ruling party at setup: the Consultative Council of the Hejaz (CUX, after the 1926 Majlis al-Shura of Mecca), the Council of the Hadhrami Sultanates (CXX), the Central Reform Board of Tripolitania (DHX, the 1919 governing board of the Tripolitanian Republic), the Oyo Mesi and Council of Ministers (DSX), the Council of the Shehu of Bornu (DUX), the Confederated Council of the Aro Towns (EBX), the Council of the Comoro Sultanates (FAX) and the Mauritian Council of Government (FBX, the colony's council from 1886). The chair is still the leader the game appoints, because no rights-cleared portrait of a real officeholder is in the working tree and downloads need the user's approval. The research resolution's preferred standard, sourced officeholders or archival institution material, remains queued for these eight rows.

Decisions:

- Barotseland (Level 2) keeps Litunga Yeta III; its layer covers the divided Kuta, Lewanika's floodplain canals and the mine labour contracts, with incidents The Kuomboka (`chaosx.nr6.226`) and Cattle Sickness on the Plain (`.227`).
- Madagascar (Level 2): vanilla MAD has no characters, so the game appoints the leader of its opening government (D20 rule). Its layer covers the highland and coastal divide, the Tamatave railway and the recall of the Vy Vato Sakelika exiles, with incidents The Vanilla Planters (`.228`) and The Rova Question (`.229`).
- The Comoros and Mauritius (Level 1) are custom carriers with the named institutions above.
- Contacts: BAR ENG, POR and SAF; MAD FRA and ENG; FAX FRA and OMA; FBX ENG, FRA and RAJ.

Blocked rows:

- IW-121 Zulu: its research resolution forbids a generated dynasty member or institution and requires a sourced incumbent, claimant or regency material; the regent Mshiyeni kaDinuzulu has no rights-cleared portrait in the working tree.
- IW-122 Ndebele, IW-123 Xhosa, IW-124 Basotho, IW-125 Eswatini and IW-127 Herero state: no planner gate, loader or reservation.
- IW-128 Nama and IW-129 Ovambo: unresearched reservations with no history or names.

Formables: FORM-30 Southern African Confederation and FORM-31 Indian Ocean League State stay closed (no carrier tag, member contract, consent rule, territory proof or flag, and not in the commit allowlist).

Validation: the allocator audit passes with 71 attested packages, 53 reservation groups and 72 adapters (expected sets and counts updated); brace balance is 0 on every touched file; every referenced trigger, effect, constant and localisation key exists.

Needs live game: a wave that releases a custom carrier and shows its named institution as the ruling party, and the Barotseland and Madagascar decision and incident flow.

## D30. Round 2: South Asia and Himalaya tranche, FORM-32 to FORM-35 readiness, and idea pictures

Disposition: `implemented` for IW-134 Punjab (FDX), IW-136 Sindh (SIN), IW-137 Balochistan (BLC), IW-138 Pashtunistan (PSH), IW-139 Kashmir (KAS), IW-140 Hyderabad (HYD), IW-141 Mysore (MYS), IW-143 Madras States (RAS), IW-145 Assam (FOX), IW-147 Manipur (MPU) and IW-148 Sikkim (SKK); `blocked` for IW-133, IW-135, IW-142, IW-144, IW-146 and IW-149; `accepted and queued` for a FORM-32 carrier contract.

Basis: the lead's round-2 priority-17 item, using the D25 regional framework engine, the D20/D22 leadership rule (a vanilla roster is accepted identity; a vanilla tag with no characters opens under the leader the game appoints) and the D29 named-institution rule for custom carriers.

Decisions:

- Ten Level 2 rows and one Level 1 row (Sikkim). Kashmir, Hyderabad, Mysore, the Madras States and Manipur keep their vanilla rulers through the roster checkpoint. SIN, BLC, PSH and SKK have no vanilla characters. FDX and FOX open under the Punjab and Assam Legislative Assemblies.
- Each Level 2 layer is grounded in the province's 1930s politics: Punjab's canal colonies, regiments and debt bills; the Sukkur Barrage lands and Karachi in Sindh; the sardars, Bolan Pass and Makran coast in Balochistan; the tribal agencies, the Khudai Khidmatgar and the Khyber in Pashtunistan; the Praja Sabha, Banihal road and Srinagar weavers in Kashmir; the jagirs, Legislative Council and Osmania University in Hyderabad; the Representative Assembly, Bhadravati works and Irwin Canal in Mysore; the 1936 Temple Entry Proclamation, the Sree Mulam Assembly and Cochin harbour in the Madras States; tea garden contracts, Digboi and the Brahmaputra steamers in Assam; and the valley and hills, the Imphal road and hill schools in Manipur. Incidents are `chaosx.nr6.230` to `.249`. The texts present communities, castes and religions as parties to a settlement, never as the problem.
- Pashtunistan has no vanilla core on its anchor 442; the release step's existing planned-anchor core makes `release` valid, so no special case is needed.
- IW-134 Punjab has loader anchors 440 and 986. Runtime readiness binds 440, so every automatic and SCN-008 release uses 440 and the loader's fallback never diverges from the checked anchor.
- Contacts: FDX ENG, USA and CAN; SIN ENG and OMA; BLC PER, AFG and OMA; PSH AFG and ENG; KAS ENG and TIB; HYD ENG, TUR and SAU; MYS ENG and USA; RAS ENG, FRA and SRL; FOX ENG and BRM; MPU BRM and ENG; SKK TIB and NEP.

Blocked rows:

- IW-133 Bengal, IW-144 Dravidian Federation and IW-149 Himalayan Confederation: formable or route only, with no route consumer.
- IW-135 Khalistan (KHL): the vanilla tag's name belongs to a later era, and it shares RG-PUNJAB-SIKH and anchor 986 with Punjab.
- IW-142 Travancore (FLX): it shares anchor 982 with the Madras States, whose vanilla ruler is the Maharaja of Travancore.
- IW-146 (FPX): an unresearched reservation that needs a named Naga package.

FORM-32 to FORM-35 readiness: FORM-32 Indus Federation has all four named members admitted (FDX, SIN, BLC, PSH); FORM-33 Dravidian Federation has RAS and MYS (Travancore blocked); FORM-34 Northeast Federation has FOX and MPU but requires the unresearched Naga package; FORM-35 Himalayan Confederation has KAS and SKK. All four stay closed (no carrier tag, member contract, consent rule, territory proof or flag, and not in the commit allowlist). FORM-32 is queued first because its member prerequisite is met; its contract needs a new X-ending carrier and flag, which this tranche does not create.

Idea pictures (correction to D25 to D29 and the earlier consolidated registry): `generic_government`, `generic_political_discourse`, `generic_diplomatic_treaty` and `generic_army_motorization` have no `GFX_idea_` sprite in vanilla or the mod, so sixty Event 006 ideas showed no picture. They now use the vanilla `generic_constitutional_guarantees`, `generic_political_support`, `generic_flexible_foreign_policy` and `generic_infantry_bonus` sprites.

Validation: the allocator audit passes with 82 attested packages, 58 reservation groups and 83 adapters (expected sets and counts updated); brace balance is 0 on every touched file; every referenced trigger, effect, constant and localisation key exists; every Event 006 idea picture now resolves to a defined sprite.

Needs live game: a wave that releases a South Asian row from the Raj (in particular Pashtunistan through its planned-anchor core, and Punjab and Assam as custom carriers under their assemblies), and the decision and incident flow of the Level 2 rows.

## D31. Round 2: Southeast Asia, East Asia and Oceania tranche

Disposition: `implemented` for IW-150 Aceh (ATJ), IW-151 Minangkabau (FUX), IW-154 Bugis state (FXX), IW-155 Bali (BLI), IW-159 Shan federation (GCX), IW-161 Mon State (IAX), IW-162 Kachin state (IBX), IW-166 Laos (LAO), IW-167 Champa (CHM), IW-169 East Turkestan (GMX), IW-170 Inner Mongolia (MEN), IW-171 Ryukyu (OKN) and IW-175 Samoa (SAM); `blocked` for IW-152, IW-153, IW-156, IW-157, IW-158, IW-160, IW-163, IW-164, IW-165, IW-168, IW-172, IW-174, IW-176 and IW-178; `unresolved` for the D29 Comoros admission noted below.

Basis: the lead's round-2 priority-18 item, using the D25 regional framework engine, the D20/D22 leadership rule and the D29 named-institution rule.

Decisions:

- Eleven Level 2 rows and two Level 1 rows (the Bugis state and Champa). Aceh and Mon State are registry Level 3 rows admitted with a Level 2 layer, as Oyo was in D27; their signature modules stay queued.
- Vanilla rosters: ATJ Sultan Alauddin Muhammad Da'ud Syah II (the last sultan, in exile), BLI the Dewa Agung of Klungkung, LAO King Sisavang Vong, MEN Prince Demchugdongrub and OKN Hiroshi Sho, each checked through the roster checkpoint. CHM and SAM have no vanilla characters, so the game appoints their opening leaders.
- Named councils for the custom carriers: the Minangkabau Council of the Nagari, the Hadat Council of South Celebes, the Federal Council of Shan Chiefs (the real federal council of 1922), the Provisional Mon Federal Council (the provisional federal council the Mon research names), the Council of the Kachin Duwas and the Provisional Council of East Turkestan. The sourced-officeholder standard stays queued as in D29.
- Each Level 2 layer is grounded in 1930s conditions: the uleebalang and ulama, the reform madrasahs and the Penang pepper trade in Aceh; adat and the reformers, the Thawalib schools and the Ombilin mines in Minangkabau; the eight kingdoms, the Paruman Agung and the subak in Bali; the sawbwas, the Lashio railway and Bawdwin in the Shan States; Mon schooling and the Moulmein trade; the duwas, the Kachin levies and the jade road; the Luang Prabang court and the south, the Mekong and the Buddhist Institute in Laos; the oasis governors and caravan roads of East Turkestan; banner pastures, the Autonomy Council and the banner cavalry in Inner Mongolia; the cycad years, the Shuri assembly and the emigrant remittances in Ryukyu; and the Mau, the Fono of Faipule and the reparation estates in Samoa. Incidents are `chaosx.nr6.250` to `.271`.
- East Turkestan keeps its accepted binding to anchor 617, which is Sinkiang's protected capital, so it is chosen only after Urumqi passes to a country with its capital elsewhere.
- Contacts: ATJ TUR, ENG and SAU; FUX SAU, EGY and ENG; FXX ENG and AST; BLI HOL and GER; GCX SIA, YUN and ENG; IAX SIA and ENG; IBX YUN, ENG and USA; LAO SIA and FRA; CHM CAM and MAL; GMX SOV, TUR and AFG; MEN MON and MAN; OKN USA, BRA and PRU; SAM USA and GER.

Blocked rows:

- IW-152 Riau and IW-158 Pattani: their leadership resolution requires a sourced incumbent or claimant, or authentic material for an actual royal council, and forbids a generated dynasty member or institution. Both sultanates had been abolished (1911 and 1902), and no sourced 1936 claimant or council material is in the working tree.
- IW-153, IW-157, IW-160, IW-163, IW-168, IW-174 and IW-178: specific community variants without a planner gate.
- IW-164 Arakan or Rakhine: name and leadership must follow a named community settlement, and its reservation is unresearched.
- IW-165 Wa and IW-176 Tonga: no planner gate, loader or reservation.
- IW-156 Moluccan federation: a vanilla route overlay by design.
- IW-172 Ainu state: restricted to a named Ainu institution with sourced leadership, which the working tree does not have.

Review note (`unresolved`): D29 admitted the Comoros (FAX) under a named council although its leadership resolution is the same sourced-claimant rule that blocks Riau and Pattani here, and its sultanates had also been abolished (1912). The Hadhramaut (CXX) rule is the same, but its sultanates were still reigning in 1936. The lead should decide whether FAX stays admitted under its council or is blocked like Riau and Pattani; the runtime is unchanged until then.

Formables: FORM-36 Maritime Federation has Aceh, the Bugis state and Bali; FORM-37 Mainland Southeast Asian Federation has Mon State, the Shan federation and the Kachin state; FORM-38 Polynesian League State has Hawaii and Samoa. All three stay closed (no carrier tag, member contract, consent rule, territory proof or flag, and not in the commit allowlist); FORM-36 and FORM-37 now meet their member minimum and are queued.

Validation: the allocator audit passes with 95 attested packages, 64 reservation groups and 96 adapters (expected sets and counts updated); brace balance is 0 on every touched file; every referenced trigger, effect, constant, localisation key and picture exists.

Needs live game: a wave that releases a custom carrier in Southeast Asia under its council, a vanilla release such as Ryukyu from Japan or Laos from France, and the decision and incident flow of the Level 2 rows.

## D32. Round 2: Americas tranche and the IW-196/IW-204 overlay scope fix

Disposition: `implemented` for IW-180 Quebec (QUE), IW-182 Newfoundland (GZX), IW-185 Texas (HCX), IW-192 Yucatan (YUC), IW-200 Guarani state (GAR) and IW-203 Patagonian state (HUX), and for the IW-196/IW-204 overlay trigger fix; `blocked` for IW-181, IW-183, IW-186 to IW-191, IW-193 to IW-195, IW-198, IW-199, IW-201, IW-202, IW-205 and IW-206; IW-196, IW-197 and IW-204 stay vanilla route overlays.

Basis: the lead's round-2 priority-19 item, using the D25 regional framework engine, the D20/D22 leadership rule and the D29 named-institution rule.

Decisions:

- Four Level 2 rows (Quebec, Newfoundland, Texas, Yucatan) and two Level 1 rows (Guarani, Patagonia). Vanilla QUE and YUC have no characters, so the game appoints their opening leaders; GAR keeps its vanilla Guarani Council. GZX opens under the Newfoundland House of Assembly (the assembly suspended in 1934), HCX under the Texas Legislature and HUX under the Congress of the Patagonian Territories (the five national territories).
- Level 2 layers: Quebec's power trusts, Legislative Assembly and caisses populaires, with incidents on the Abitibi settlers and the Thetford asbestos strike; Newfoundland's dominion debt, restored responsible government and fisheries board, with the Labrador boundary and the Water Street merchants; Texas's oil glut, legislature, Railroad Commission proration and Ranger companies, with the hot oil runners and the border bridges; Yucatan's henequen haciendas, congress, ejidos and the port of Progreso, with the leagues of resistance and the price of twine. Incidents are `chaosx.nr6.272` to `.279`.
- Anchors: HUX binds its first loader anchor, 512. GAR's first loader anchor, 301, is Paraguay's protected capital; GAR binds 688 Chaco Boreal, and its runtime readiness also requires 301 to be unavailable so the loader's choice and the readiness check agree. The guard lives only in the runtime-ready trigger, because the allocator audit forbids the pre-reservation anchor proof inside exact tag-availability triggers.
- Contacts: QUE FRA and USA; GZX ENG, CAN and POR; HCX MEX, ENG and GER; YUC CUB and USA; GAR ARG and BRA; HUX ENG and CHL.
- IW-196/IW-204 fix: `has_independence_wave_iw196_antilles_anchor_control`, `has_independence_wave_iw196_antilles_guard_objective`, `has_independence_wave_iw204_restoration_anchor_control`, `has_independence_wave_iw204_restoration_guard_objective` and the two `choose_anchor` effects read ownership, control and divisions in the calling carrier's scope (`owns_state`, `controls_state`, `divisions_in_state`) instead of ROOT, matching the IW-156 and IW-197 overlays. Their callers (the carrier's own decisions and `on_daily_TAG` hooks) are unchanged.

Blocked rows:

- IW-181 Acadia, IW-186 Cherokee, IW-188 Lakota, IW-189 Dine and IW-194 Miskito: no planner gate, loader or reservation.
- IW-183 Cascadia: formable or route only.
- IW-187, IW-190, IW-191, IW-195, IW-199, IW-202, IW-205 and IW-206: specific community variants without a planner gate.
- IW-193 Oaxaca and IW-198 Aymara: their research requires a sourced leader of the exact named community or authentic institutional material and forbids a generated council.
- IW-201 Muisca restoration: no period Muisca institution existed to restore, and a made-up council would be a generated institution.

Formables: FORM-44 Rio de la Plata Confederation has GAR and HUX, and FORM-45 Mesoamerican Federation has YUC; FORM-40 to FORM-43, FORM-46 and FORM-47 have no admitted member. All stay closed.

Validation: the allocator audit passes with 101 attested packages, 70 reservation groups and 102 adapters (expected sets and counts updated); brace balance is 0 on every touched file; every referenced trigger, effect, constant, localisation key and picture exists.

Needs live game: a wave that releases Newfoundland from the United Kingdom or Texas from the United States as a custom carrier under its institution, Guarani released on the Chaco Boreal, and the IW-196 and IW-204 guard missions counting divisions in the carrier's own anchor.
