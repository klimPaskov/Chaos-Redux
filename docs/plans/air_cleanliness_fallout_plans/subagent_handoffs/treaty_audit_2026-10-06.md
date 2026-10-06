# Air Cleanliness Treaty and Fallout Decision Audit

## Final parent disposition, 2026-10-06

Core commit `9ec627597` resolves the earlier P1 cost-row and Recognition presentation findings with three native custom-cost rows, shared affordability selectors, the new glyph, and owned effect tooltips.
It resolves the P2 source presentation gates with staged families and active-project visibility; native panel density and target clones remain unobserved.
The P3 NZL duration concern is not an outstanding source defect: both durations are stored with `set_variable`, then passed as `days = var:<normal variable>`, matching installed `common/scripted_effects/SIA_scripted_effects.txt:780`.
The patrol source uses `fallout_nzl_patrol_window_days`; the weather source uses `fallout_nzl_weather_warning_days`.
The excerpt below preserves the earlier audit snapshot, rather than overriding these current-source dispositions.
Native expiry, decision-panel fit, and blocked MCP probability comparisons remain open checks.

Date: 2026-10-06.

Repository root: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.

Disposition: read-only audit complete. The only file written by this subagent is this handoff. No gameplay files, assets, spreadsheets, or source documentation were edited, and no commit was made.

## Scope and accepted basis

Reviewed the r2 record at C:\Users\klimp\Videos\chaos_redux_trailer\records\cx\phase2_history\fallout.md, the user rules at C:\Users\klimp\Videos\chaos_redux_trailer\records\cx\inbox\fallout.txt, and the named consolidated treaty decisions, category, effect, trigger, constants, and event sources.

The r2 record marks A19 as implemented by static review, while pledges, ballots, betrayal timing, refunds, and AI choice frequencies remain needs_live_game. A19 records its values, event flow, and text as agent decisions under the user's grant of design authority. The record does not establish engine or live-game behavior.

The user inbox requires one player to receive no repeated report from a chain, calls for low category clutter, and requires texticons for every displayed spendable value.

## Findings sorted by severity

### P1: The treaty category exceeds the visible-action budget and does not cap active projects

The pre-Fallout category is visible to every live treaty member at common/decisions/categories/fallout_consolidated_categories.txt:12-21. When their target and campaign gates hold, it can expose nine decision families: Global Cleaning Day, Joint Filter Convoy, Verification Mission, Shared Sampling Grid, Seed Archive Exchange, Evacuation Corridor, Sanction Burners, Pooled Decontamination, and Call Relief Vote at common/decisions/fallout_consolidated_decisions.txt:39-779.

air_cleanliness_treaty_operation_phase_is_open only checks that the treaty is active and Fallout is not transitioning or active at common/scripted_triggers/fallout_consolidated_triggers.txt:478-483. It does not phase those families. Several targeted decisions produce one entry per eligible member or burner, so the number of visible rows can exceed the number of families.

The per-sponsor locks on filter convoy, seed archive, evacuation, and sanction do not prevent those timers from overlapping with one another, Global Cleaning Day, Verification, the global sampling grid, pooled decontamination, and the relief vote. The proposed six-family visibility gates can reduce menu density, but do not cap simultaneous active projects. Preserve running projects when gating new starts, and decide whether the three-active-project limit needs a start gate.

Parent's proposed sequence also makes Seed Archive unavailable for the 180-day period after the 365-day sampling-grid active flag expires and before its full 545-day cooldown ends. If the intent is to unlock seeds after the grid is first completed, use a completed-grid receipt for the current treaty generation instead of the transient active flag. The existing shared sampling grid requires four members, so the proposed four-member threshold itself is not stricter than its current eligibility gate.

### P2: Recognition has no texticon in the reconstruction cost

fallout_treaty_reconvene_secretariat_cost and its blocked and tooltip variants at localisation/english/fallout_consolidated_l_english.yml:10930-10932 display the spendable Recognition amount as the literal word Recognition. Political Power uses its texticon. The decision has two spendable cost types and no hidden fifth cost, but the Recognition icon coverage is missing. The A19 event-button cost tooltips for pooled pledges and relief votes do use support equipment and fuel texticons.

### P2: Existing Treaty cost tooltips spell out resources without texticons

The zero-native-cost decisions pay support equipment and convoys in their start effects, while their only cost explanation is a plain-text effect tooltip. The keys air_cleanliness_global_cleaning_day_effect_tt, air_cleanliness_joint_filter_convoy_effect_tt, and air_cleanliness_treaty_verification_mission_effect_tt in localisation/english/chaosx_decisions_l_english.yml:232-238 spell out support equipment, convoys, and assigned civilian factories without icons. Their costs are two spendable types each plus a reserved factory slot, within the four-type limit, but every displayed value needs the correct icon and the paid amount should have a clear cost presentation. Prefer icon-first cost text alongside the existing requirement/effect explanation.

The later A19 cost keys for sampling, seed archive, evacuation, and pooled decontamination use support equipment, convoy, fuel, and factory texticons. Their action counts are one consumed resource plus a factory slot for sampling, two consumed resources plus a factory for seed and evacuation, and two consumed resources plus a factory for pooled decontamination. Sanction uses one native Political Power cost. Relief Vote uses one native Political Power cost plus the optional support equipment pledge on its ballot button. Reconstruction uses Political Power and Recognition. No Treaty action exceeds four distinct spendable types.

### P2: Treaty category phase gates need target and active-project safeguards

The current relief target gate reads the candidate's air_winter_response_priority_state, checks that the state is valid, meets phase 4 or worse, and remains owned and controlled by that country at common/scripted_triggers/fallout_consolidated_triggers.txt:37513-37523. Evacuation additionally verifies the current priority target flag and recorded owner at lines 656-673. If the planned phase gates rely on a stored priority-state pointer, keep it in the targeted FROM scope and retain those ownership/control and current-priority checks.

Target-trigger branches for already active filter-convoy, seed, evacuation, and relief projects must remain visible even when a new-start phase or member-count gate closes. This keeps ongoing decisions visible through their existing completion path.

### P3: Two non-Treaty dynamic flags still pass variables directly to timed flag fields

The full-path scan of the owner's consolidated decision and effect files found direct variable tokens in set_country_flag days fields at common/decisions/fallout_consolidated_decisions.txt:2123-2126 for fallout_nzl_weather_warning_current and common/scripted_effects/fallout_consolidated_effects.txt:18746-18748 for fallout_nzl_sea_road_patrol_window_current.

These fields are documented as taking integer days, and the project guidance treats set_country_flag days and set_global_flag days as rejecting direct constant and variable tokens. They are outside the Treaty blocks and were not edited. Use a verified literal-text meta-effect expansion or the appropriate same-file literal constant when those owners handle them.

## Parent-owned fixes verified from current disk

The reconstruction target trigger now blocks a recipient with an existing proposer variable at common/scripted_triggers/fallout_consolidated_triggers.txt:37608-37618. The starter saves the proposer as a regular event target before firing .22, and .22 no longer reseeds the event target from the mutable country variable.

The answer trigger verifies the carried proposer target matches the recipient's stored proposer and checks the proposal generation. Refusal retains the incoming lock until the proposer resolves its timed project. The clear helper removes that lock only when its owner matches PREV, preventing one proposal from clearing another.

Both proposal validity and answer_is_open now require that the proposer and recipient have not capitulated. The .22 event has an acknowledgement option when the answer is closed. The on_capitulation hook calls exact reconstruction cleanup for ROOT, and the on_annex hook does the same for FROM.

The formerly bare temporary days token for reconstruction refusal is now expanded to integer text inside meta_effect at common/scripted_effects/fallout_consolidated_effects.txt:696-700. The event target documentation confirms that a regular target saved before a nested country_event remains available in that event chain. The wiki defines country and global flag days as integer values. The live script_validate route was unavailable, so the meta-effect engine execution remains unverified.

The annex callback now invokes fallout_treaty_cleanup_annexed_reconstruction from the exact FROM country at common/on_actions/fallout_consolidated_on_actions.txt:17-29. Its helper at common/scripted_effects/fallout_treaty_reconstruction_cleanup_effects.txt:28-47 resolves the victim's exact proposer or partner receipt, returns the saved Recognition deposit once to a surviving proposer, and uses no world iterator. The new lost result has a constant, event branch, option, and localisation.

The relief-vote start saves its fixed native cost quote, and the cancellation path refunds that exact quote once. Current closure counts live members, calculates the strict majority, requires a payable yes pledge, filters donors by peace and equipment, and resolves a zero-donor result as unfunded with no recipient penalty. The unfunded branch skips the 180-day recipient cooldown. Cancellation and unfunded resolution both set a 14-day caller retry window, while funded results and political rejection keep the original pacing. Direct Fallout and annex releases still call the silent release helper rather than the cancel/refund path. Fallout silence is recorded as accepted in A19.

The verification supplies event .8 now closes the request through cancellation instead of reopening .6. A subject receives one .6 normally or at most one .8 after an invalidated paid choice. The previously reported unbounded recount popup loop is resolved in current source.

These changes belong to the parent or other shared-tree agents, not to this audit. Before the reconstruction edits, two sponsors could overwrite one recipient's proposer pointer and stale cleanup could clear the wrong proposal. Current source blocks a second incoming proposal, carries the original proposer target into .22, checks that pointer against the stored proposer and generation, and clears only the matching pair. Before the new on_annex/on_capitulation hooks, the reconstruction lock could survive partner loss. Current hooks dispatch exact-pair cleanup and a lost result.

Before the refusal cooldown edit, the timed country flag used a bare temporary variable in days. Current source injects an integer string through meta_effect. This audit could not run script_validate because the route returned Transport closed.

Before the relief-vote edit, auto-yes votes could approve a session with no ballots or deliveries and cancellation spent Political Power. Current source checks live-member majority, candidate donor capacity, donor peace/equipment at payment, an unfunded outcome, one saved-quote refund, and a 14-day retry after cancellation or no payload.

## Category lifecycle and cognitive load

air_cleanliness_treaty_category opens for live treaty members before Fallout and closes on transition, active Fallout, or treaty disable. fallout_treaty_reconstruction_category opens only for a current Fallout registry survivor with membership memory and without the banned flag.

Current Treaty content has nine visible decision families, with several target arrays that can create many individual entries. The category has no per-generation family phasing yet. The planned six-family gates need target-instance and active-project safeguards, and need to preserve a useful Seed Archive route during the 180-day post-grid cooldown.

The main values do explain their cause and consequence. The decision descriptions describe the project, cost/effect tooltips show amounts and duration, and the A19 record documents the donation and result rules. The missing icon-first costs in the three legacy action tooltips and the Recognition cost are the substantive clarity defects. The parent vote change adds a distinct unfunded result instead of showing success without a paid pledge. No scripted GUI surface is owned by this Treaty category.

## Timed-project quality and popup counts

| Family | Owner and target | Duration and requirement | Success and failure | Popup/duplicate note |
| --- | --- | --- | --- | --- |
| Cleaning Day | Live treaty sponsor, treaty-wide result | 45 days, member quorum, contamination floor and ceiling, support equipment, convoys, factory slot | Reduces contamination. Cancellation releases locks and does not refund equipment | One cancellation report to sponsor. Completion is a world news event |
| Filter Convoy | Donor member to another member's current priority state | 21 days, Phase 3 or worse state, peace, support equipment, convoys, factory slot | Creates a relief route with a duration. A broken route loses committed stores | Start .1 to donor, success .2 to recipient, cancellation .4 to donor, one per role |
| Verification | Founder/secretariat to one member | 14 days, peace, unreserved live member, support equipment, convoys, factory slot | Subject answers .6. The secretariat receives delayed .7. An invalid receipt cancels | Subject gets .6 normally or one terminal .8 if stores fail at selection |
| Sampling Grid | Any eligible treaty member, treaty-wide | 45 days, four-member quorum, support equipment and factory slot | Forecast .10 to every live member. Cancellation loses committed equipment | One completion popup per member |
| Seed Archive | Donor to another member | 30 days, valid donor source, eligible recipient, peace, support equipment, convoys, factory slot | Recipient receives food reserve and both get memory. A failed route loses the shipment | One .11 popup to recipient |
| Evacuation Corridor | Donor member to another member's severe priority state | 30 days, Phase 4 or worse source, bordering eligible receiver, peace, support equipment, convoys, factory slot | Moves population and adjusts state ledgers. A failed route loses committed stores | One .12 to sponsor and one .13 to source owner |
| Burner Sanction | Member to listed burner | 14 days, severe recent CBRN target | Bars target and records condemnation. Cancellation clears the pending target | One .15 popup to target on successful sanction |
| Pooled Decontamination | Member sponsor to one member priority state | 60 days, Phase 3 or worse, one factory plus support equipment and fuel shares | Two to four shares produce relief. Ordinary cancellation or too few shares returns contributions. Betrayal and Fallout do not | Each eligible other member gets .16, then sponsor, recipient, and contributors get at most one .17 each |
| Relief Vote | Member caller to one member priority state | 21 days, Phase 4 or worse, peace, and a prospective donor pool | Current close effect counts live members, requires a strict majority and at least one payable yes pledge, and reports an unfunded result without a recipient penalty | Non-caller and non-recipient members get .18, every member gets .19, so voters can get two |
| Clean Day Betrayal | Operations fail into a state owned by a treaty violator | Triggered only when pooled decontamination or a filter convoy is cancelled over a violator-held state | Aid is lost. The violator loses relief access and may gain Condemnation | Each affected sponsor or contributor receives one .20, and the violator receives one .21 |
| Reconstruction | Former member survivor to one partner survivor | 90 days, both accounts live, peace, no pair compact/refusal | Success signs the compact. Refusal or failed proposal returns Recognition but retains the Political Power initiation fee | Partner gets .22 and on success .23. The proposer gets .23. Incoming-recipient races are fixed in current source |

Membership registration checks the global members array before inserting, so the .19 loop does not duplicate reports from duplicate membership entries. Pooled result reporting has an explicit per-country report-sent flag and clears it after dispatch.

Clean Day betrayal is connected for both pooled decontamination and Joint Filter Convoy. Each cancellation checks the reserved state's current owner against the banned flag and violator array before selecting the refund or betrayal branch. The betrayal effect revokes the violator's treaty relief routes, limits public Condemnation through its 90-day flag, sends .21 to the violator, and sends .20 to the affected sponsor/contributors. The violation path records the banned flag before membership removal, matching the accepted A19 rationale.

For N live treaty members and a caller distinct from the recipient, a relief vote sends N - 2 ballot popups and N result popups, for 2N - 2 total across the treaty and at most two to one country. If the caller targets itself, it sends N - 1 ballots plus N results, for 2N - 1 total and at most two to one other country. Pooled decontamination sends at most N - 1 pledge requests and one deduplicated result to each participant, with at most two popups per country. Reconstruction normally gives the partner one proposal popup and, if signed, one result popup. Verification gives its subject .6 normally or at most one terminal .8 after a paid option becomes unaffordable.

Correction: verification's retry path is now terminal after one .8 notice, as described above. The .19 event has no explicit timeout_days. The offline Event modding page says an event without timeout_days uses the default 13-day choice window at line 186. A later relief vote cannot resolve before its 21-day duration, so an ordinary prior .19 popup should close before a later vote overwrites the shared result variable. Do not treat that normal-cadence result overwrite as a confirmed defect.

## AI and target validity

The named target families use member arrays or the condemnation target array and check country existence, membership, peace, source state, current priority state, and project receipts. Reconstruction's answer and proposal triggers now require both sides to be uncapitulated.

The required probability audit was routed to chaosx_ai_probability_auditor. Its pre-patch mission_ai_will_do inspection recognized eight timed Treaty decision candidates plus reconvene, with poolComplete true, zero required inputs, and zero unresolved candidates, but generated no scenario scores. Follow-up probability inspection/evaluation/sweep/compare and the .16/.18/.22 event-option inspections failed with Transport closed. Do not claim a score or post-patch comparison.

Probability artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84b3888f7d315d73b1d7a4b69faaa638ec7ae034e6a4824066032b08eb52de73/85fdcc5f4d0b382324010cffece3c248d1300389a3c5f6bfd9308d924ff5ee68/probability-inspect-41b693faf86e.json.

Source revision: 62b442ec8907e457e673f7f8655dee4ea150d3113a2aa14046b99cc41ffba3af.

Source hash: 41b693faf86e7bee0e73c40347c74c9dad6f2b4deb3a643f706a170ed84ef691.

The two base decision weights Global Cleaning Day and Joint Filter Convoy still need their decision_ai_will_do inspection. Event option pools .16, .18, and .22 also need probability evidence after transport recovers. Any weight or scenario edit requires the matching comparison pass.

## MCP and reference evidence

Workspace ID: mod_chaos_redux_ea3b2d67c2c0.

hoi4.decision_inspect was called in inspect mode for air_cleanliness_treaty_call_relief_vote with one declared USA 1936 scenario and no refresh. It returned DECISION_ANALYZED_PARTIAL, complete false, 100 unresolved definitions, and MCP_INLINE_FILES_TRUNCATED for 64 of 6,829 source paths. The report candidate had unresolved FROM and state inputs, so it is not a decision-gate proof.

Decision artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b0679799f35d761edf15bd492aab01b44877e6faa0f03ab54e615ca15768e8c/0f0523ebda688446bfaf9525a6f7be2bd6865c1d1d81d0fd634ec06585a809b2/decision-5253c3551fe47b6e22ef66be.json.

Decision inspect source revision: 6a5f905214dc72f32ccc7ab9faa4c7c348527ec21995bfa657674878532f213c.

Offline wiki references retrieved through reference_search before the service disconnected: Decision modding targeted decisions, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162, lines 511-536. Decision modding timer and cancel behavior, same revision, lines 337-356. Decision modding mission attributes, same revision, lines 465-479. Effects set_global_flag and set_country_flag integer days, revision 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c, lines 349 and 897.

Installed documentation references retrieved through reference_search: Country Decisions, revision 5e7e686b5582f32c898d805e17171e88f3bfeee4a030deb1884f9726de019, lines 1-46. Script constants schema, revision e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c, lines 1-34. Script Constants, revision 884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7, lines 216-245.

Local offline files also read directly: Data structures regular event targets, lines 303-325. Scopes ROOT, PREV, and FROM definitions, lines 260-263. On actions on_annex scope, lines 257-258 and 363-369. Decision modding targeted decisions, lines 511-536 and cancel behavior, lines 337-356. Effects timed flag parameter rows, lines 349 and 897.

The successful reference_context call reported that Triggers, Scopes, and Localisation were omitted, and that a script_doc source was unavailable. Targeted follow-up search/read calls then returned Transport closed, so the pertinent local pages were read directly. After the initial successful reference context/search calls, hoi4.event_inspect, hoi4.reference_read, hoi4.script_validate, hoi4.source_lookup, and later reference_search calls returned Transport closed. Event inspect/render/compare evidence and script validation are therefore absent. Source review is not a replacement for those routes.

## Fresh QA checks still needed

No game or window was opened in this audit. Use the fresh qa_001_fresh_head for the following bounded checks after parent source work is complete.

First, compare a treaty with three members against one with four members, and count actual decision rows as well as decision families. Check the sampling grid before, during, after its 365-day active period, and during its 180-day remaining cooldown. Confirm Seed Archive remains intentionally available or has a current-generation unlock.

Second, test a Phase 4 recipient and a Phase 5 recipient with the active priority state owned and controlled, then repeat after the priority state is changed or loses control. Confirm target gates follow the current priority-state receipt and running projects remain visible until completion.

Third, test a relief vote with caller and beneficiary auto-yes, an abstaining/no third member, and a payable donor. Confirm the intended live-member majority, the explicit no-payload result, no success memory or success popup without at least one paid share, donor peace filtering, and one-time exact PP refund when invalidated.

Fourth, leave a .19 result unselected while a second vote starts. Confirm the first event closes within the default 13-day choice window before the second 21-day vote can resolve. Also try to start a second relief vote while the first is open and after release.

Fifth, in multiplayer, open a verification response while the paid option is affordable, drain the required equipment/convoys before selecting it, and confirm at most one recount and a terminal close.

Sixth, test reconstruction A to B, then try C to B while A's request is pending. Reject or cancel A's request and confirm only A's paired lock clears. Repeat with B capitulated, A capitulated, B annexed, and A annexed. Confirm .22 closes as unavailable after either side falls, the surviving proposer receives its Recognition deposit once, and no stale incoming pointer blocks later valid partners.

Seventh, after a refusal, confirm the same pair is blocked for 365 days and becomes available after expiry. Check the Recognition cost icon and confirm the refusal cooldown is actually set.

Eighth, test all three legacy cost displays and the reconstruction cost row. Every displayed support equipment, convoy, fuel, civilian-factory, Political Power, and Recognition amount should use its actual texticon. Count visible cost types and ensure none exceeds four.

## Changed files, changed IDs, and remaining work

This audit changed only docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/treaty_audit_2026-10-06.md. No gameplay files were changed by this subagent.

Parent-owned source edits observed on disk include the reconstruction incoming-recipient lock, carried proposer event target checks, matching cleanup, timed refusal flag meta-effect, exact annex hook, lost-result event/localisation, and fixed-quote relief cancellation refund. These are source changes by the parent or other shared-tree agents, not changes made by this audit. The relevant IDs are fallout_treaty_reconvene_secretariat, fallout_treaty_reconstruction_partner_is_valid, fallout_treaty_reconstruction_answer_is_open, fallout_treaty_cleanup_annexed_reconstruction, chaosx_air_treaty.22, and chaosx_air_treaty.23.

Meaningful live validation skipped because this subagent was explicitly read-only and prohibited from opening the game or windows. Event inspection, reference_read, source_lookup, and script_validate also became unavailable with Transport closed. The parent owns gameplay changes and final review.

Skills used: chaos-redux-subagents, chaos-redux-events, and chaos-redux-decisions-missions. No skills were created or updated.
