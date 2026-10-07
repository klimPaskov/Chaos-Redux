# Event 012 Gods of Africa decision and mission surface audit

Date: 2026-10-07.

Disposition: unresolved for parent review. This bounded read-only source audit is complete, but native decision-row visual evidence and a complete scenario projection remain unavailable. This is not a completion verdict for the Gods of Africa feature.

## Scope and acceptance basis

The audit covers common\decisions\012_africa_gods_decisions.txt, common\decisions\012_africa_gods_recovery_decisions.txt, common\decisions\categories\012_africa_gods_categories.txt, current decision localisations, and only helper/trigger call sites needed to establish visibility, cost labels, and mission timing.

Acceptance references are docs\specs\012_africa_is_one_gods_of_africa_specs\specs\012_gods_of_africa_full_spec.md, especially Participant response model, Africa-side gameplay, Final settlement, Presentation, and Failure and cleanup, plus docs\events\012_africa\gods_of_africa.md and the 2026-10-04/05 agent decisions. The full spec caps the ordinary participant demand response surface at five actions and requires confirmation before permanent defiance. The parent’s activation and settlement security repair in b3af259674ee4b5d8c4aa049cfeb765b621f376f is accepted prior evidence and is not re-audited here.

No gameplay, weights, GUI, localisation, other documentation, index, or Git files were changed. This handoff is the only written file.

## Findings, ordered by severity

### High — permanent defiance bypasses the required confirmation step

The accepted full spec says permanent defiance requires a confirmation window because it closes the ordinary relationship route. gods_of_africa_permanent_defiance is immediately available through its current trigger, and its completion effect directly calls the irreversible helper (common\decisions\012_africa_gods_decisions.txt:824-883). The block has a warning effect tooltip but no intermediate confirmation decision, event, or confirmation localisation. The bounded offline decision-documentation search did not establish a native confirmation attribute.

Recommended correction: add an explicit localized confirmation step before the existing helper call, using the accepted Event 012 presentation path. Preserve the current outcome and AI eligibility after confirmation.

### High — host category can show more than six primary actions in one phase

Before a doctrine is selected, gods_of_africa_choose_reciprocal_covenant, gods_of_africa_choose_sovereign_exaction, and gods_of_africa_choose_strategic_ambiguity all show while the doctrine variable is zero (common\decisions\012_africa_gods_decisions.txt:1046-1133). The five core priority decisions—gods_of_africa_prioritize_land, _fuel, _manpower, _industry, and _transport—have independent positive-need visibility gates and no doctrine-selected gate (:1134-1261). The need profile sets these shortages independently during the active-host owner refresh (common\scripted_effects\012_africa_gods_effects.txt:1029-1150, called from the owner refresh at :105-112). A source-valid host with five simultaneous shortages can therefore see eight actions before doctrine selection; a positive emergency lane can add a ninth. The emergency lane is later replaced by support or aircraft under the accepted focus gates, but that does not phase it against doctrine selection.

After a doctrine is selected, five core priorities plus one advanced priority can coexist with gods_of_africa_grant_leniency for a current offender with an active demand. Leniency is enabled by doctrine or the office-voices focus and has no visibility suppression against the priority lane (:1307-1383). This gives a source-valid lower bound of seven semantic actions, before other eligible host target actions are counted.

Recommended correction: phase the existing doctrine and priority families, then phase existing target-action families against the active priority set so the host category stays within six semantic actions. Preserve outcomes and the existing category; no extra category or mechanic is needed.

### High — participant actions exceed six when Final Council overlaps a live demand

gods_of_africa_council_pledge and gods_of_africa_council_speech both show whenever gods_of_africa_council_is_open is true (common\decisions\012_africa_gods_decisions.txt:214-289; common\scripted_triggers\012_africa_gods_focus_payoff_triggers.txt:46-55). That trigger checks the active host, Final Council focus, prior voice, defiance, final outcome, and war with Africa, but does not exclude an active demand or an open negotiation. In an ordinary non-diplomatic, non-continuing demand, five response decisions can coexist: comply, partial shipment, extension, refusal, and permanent defiance (common\decisions\012_africa_gods_decisions.txt:336-429, 484-577, 776-883). The two Council choices can therefore raise the same participant category to seven visible semantic actions during an ordinary demand or negotiation phase.

Recommended correction: keep the Council open until settlement, but phase its two participant actions until the current demand and any negotiation are resolved. This preserves both choices without adding a category.

### High — defiance preparation, reconciliation, and a final ultimatum can overlap

The four defensive preparation decisions are visible for a defiant participant with a current host: gods_of_africa_prepare_defensive_defiance, gods_of_africa_harden_stockpiles, gods_of_africa_secure_transport, and gods_of_africa_prepare_countermeasures (common\decisions\012_africa_gods_decisions.txt:884-1003). gods_of_africa_seek_reconciliation is also visible while reconciliation is pending (:1004-1043). The final ultimatum’s return-land, pay-settlement, and refuse choices are independently visible while its deadline is open (:114-212); they do not exclude preparation or reconciliation. The punishment dispatcher issues the ultimatum at its Tier V gate (common\scripted_effects\012_africa_gods_effects.txt:3380-3405), while the reconciliation starter requires peace and no active demand but does not reject a pending ultimatum (:4110-4143). A defiant participant with reconciliation pending can therefore face four preparation actions, one reconciliation action, and two ultimatum answers; if it holds African land or is at war with Africa, return-land raises the total to eight. The reconciliation and ultimatum missions can both be active as separate 60-day clocks.

Recommended correction: phase preparation and reconciliation controls against the open ultimatum response state, or defer one of the two timers until the other resolves. Preserve each outcome and failure path.

### Medium — expedition cost localization shows four values inline

gods_of_africa_send_expedition has four distinct spendable types per use: infantry equipment, support equipment, manpower, and political power (common\decisions\012_africa_gods_decisions.txt:1972-2029). The normal and blocked strings show all four values inline (localisation\english\012_africa_gods_l_english.yml:198-200), exceeding the decision skill’s three-value inline display limit. All four icons are correct. The cost tooltip says only that equipment and men leave Africa’s forces; the separate availability tooltip carries the PP payment and stock/reserve conditions.

Recommended correction: show no more than three values inline and put the fourth amount/icon plus reserve requirement in the full cost tooltip. Keep all four spendable types and the accepted price.

### Medium — fixed custom political-power costs lack AI saving hints

Offline Decision modding says custom costs do not automatically teach the AI to reserve political power and documents ai_hint_pp_cost for fixed PP costs (paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:284-336, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162). In the Gods decision file, the only ai_hint_pp_cost is the protection decision’s literal at :1492. Other fixed-PP custom-cost actions with AI weights have no hint: gods_of_africa_ultimatum_pay_settlement, gods_of_africa_council_speech, the four defensive preparation decisions, gods_of_africa_seek_reconciliation, gods_of_africa_arm_offender_enemies, gods_of_africa_send_expedition, and gods_of_africa_coerce_occupier (common\decisions\012_africa_gods_decisions.txt:147-181, 251-280, 884-1043, 1913-2085). The dynamic current-demand cost is excluded from this fixed-cost list because its resource and amount vary by contract.

Recommended correction: add a matching fixed PP saving hint to each applicable fixed-cost decision or record why that AI should not reserve PP. This is a source-level budgeting concern, not a measured AI probability finding.

### Low — generic substitute shortcut duplicates the first valid alternative

During negotiation, gods_of_africa_substitute_demand and up to three named slot decisions are visible together (common\decisions\012_africa_gods_decisions.txt:578-744). The player-only shortcut chooses the first valid slot in order and submits that same frozen offer (common\scripted_effects\012_africa_gods_effects.txt:4856-4880). It duplicates Alternative I when slot 1 is valid, or the first later valid slot otherwise. It is not a fourth substitute outcome, but it is an extra row repeating a visible choice.

Recommended correction: hide the generic shortcut whenever a named valid alternative is shown, or make its behavior visibly distinct. Retain all three accepted alternatives.

### Low — public values have partial significance guidance near the category display

The participant category displays Strength and Wrath with their current bands. Strength’s tooltip says the global value limits Africa’s practical punishment ceiling; Wrath’s tooltip says visible conduct can move it and war, occupation, and defiance impose floors (localisation\english\012_africa_gods_l_english.yml:334-346, 672-673). The host category displays Strength and doctrine (:689). These values are named and consequential, and the category does not expose a raw multi-variable dump. The descriptions do not show band thresholds or summarize the immediate player actions that move each value near the display.

Recommended correction: clarify causes and player response in the existing concise value/localisation text if the accepted spec expects those facts at the category surface. Do not add another public value or a new GUI.

## Source-derived concurrent scenario matrix

These counts describe simultaneous source-visible semantic actions, not an engine row limit and not proof of clipping. Targeted country rows are counted once per action family. A row may be greyed by its available trigger; that does not remove it from the visible action surface.

| Scenario | Participant category | Host category and missions |
| --- | --- | --- |
| Idle enrolled participant, active host | The ordinary category is visible. Voluntary aid appears only when its need, reserve, and cooldown gates pass. Final Council pledge and speech can appear together if the Council is open. | Doctrine choices and priority lanes depend on current host variables; the owner-built need profile is not gated by doctrine selection. |
| Ordinary active non-diplomatic demand | Five response actions can coexist: comply, partial shipment, extension, refusal, and permanent defiance. One demand mission belongs to this participant. | Current host priorities and any eligible targeted action remain independent of this participant’s response rows. |
| Continuing-support demand, before sign | Sign agreement replaces partial payment; comply, extension, refusal, and defiance remain visible, for up to five. | The host’s active demand and priority actions remain independently visible. |
| Continuing-support demand, signed | Sign disappears after the signed flag; partial payment remains hidden for this family. The other four response actions can remain visible while the owner handles later instalments. | The demand mission and frozen instalment terms remain owner-managed. |
| Negotiation open, slots not yet submitted | The generic shortcut, up to three named alternatives, and return-to-demand can show together: five rows, with one duplicated substitute outcome. Ordinary comply, partial, refusal, and defiance rows are hidden by the negotiation flag. | The host can accept or reject only after a valid offer is pending. |
| Substitute submitted, awaiting host answer | The generic shortcut and all slot rows hide after the offer flag; return-to-demand remains. | Accept and reject are simultaneous answer choices on the same pending target; the demand mission continues until resolution or timeout. |
| Final Council open during an active demand or negotiation | The two Council choices are not gated off by demand or negotiation. They can add two rows to the five-row response surface, reaching seven. | The host’s active phase remains open before settlement. |
| Defiant, reconciliation pending, final ultimatum open | Four preparation actions plus seek-reconciliation and two ultimatum answers are visible; return-land is a third ultimatum answer when the participant holds African land or is at war with Africa. This is seven or eight actions. Reconciliation and ultimatum missions can both be active. | The host still has its active category until final settlement; the parent-owned punishment and cleanup effects determine the current target state. |
| Final settlement before commit | The untargeted commit decision is visible only for the active secured host with the Final Council/settlement unlock. Other active-host actions are not suppressed by this row. | Priority and eligible target actions can still coexist; exact total varies by current needs, unlocked focuses, and target states. |
| Final settlement after commit, delivery pending | Ordinary participant demand actions are closed; category visibility remains only for victor/recovery exceptions. | Active-host actions are closed. The pending delivery decision is the host’s continuing row and re-enables on its configured 30-day interval. |
| Lost host without an active recovery/victor request | The ordinary participant category is hidden unless an explicit recovery/victor condition keeps it open. Ordinary response decisions still require current host and participant generation. | Ordinary host decisions require an active valid host. Recovery shows only its current congress/member choices; delivery remains only if frozen support is still owed. |

## Decision category lifecycle and cognitive load

gods_of_africa_participant_category is visible for current enrolled participants under an active host, plus explicit victor and recovery routes (common\decisions\categories\012_africa_gods_categories.txt:14-31). gods_of_africa_host_category is visible for a valid active host, pending settlement delivery, or a current recovery phase (:34-47). This is a deliberate lifecycle; lost-host visibility is not a stale ordinary contract surface.

The participant display has two public values, Strength and Wrath, with bands and concise consequence text. Their significance is partly clear: Strength is tied to punishment limits, and Wrath to conduct/floors. Thresholds and direct response levers are spread across decisions and other tooltips rather than summarized at the display. Host doctrine is a named route choice; priority rows are named need lanes rather than unexplained numeric values. No source row exposes a wall of internal counters.

The active demand, reconciliation, and final ultimatum descriptions carry their family, deadline, response/failure stakes, and next player action. The final ultimatum answers are concise and the refusal tooltip says disaster is bounded by current Strength. Exact wrapping, clipping, and visual row height remain unknown because the ordinary category renderer did not find a native decision-category window.

## Mission quality

| Mission | Owner and category | Region and requirement | Duration and timer ownership | Success, failure, and duplicate risk |
| --- | --- | --- | --- | --- |
| gods_of_africa_demand_mission | Participant country; participant category. | No map region; one current, generation-bound demand contract. | Dynamic contract deadline with a 180-day maximum native mission timeout. The owner activates it at common\scripted_effects\012_africa_gods_effects.txt:2310 and synchronizes remaining days; extensions resynchronize via :3136-3172. | Compliance or accepted substitute resolves it; partial shipments retain the same contract and mission; timeout fails the demand. Cancellation closes on stale generation, inactive demand, defiance, or final settlement. One active demand per participant; no same-type duplicate found. |
| gods_of_africa_reconciliation_mission | Participant country; participant category. | No map region; the participant needs reconciliation, is at peace with Africa, has no active demand, and enters a pending review. | 60 days (gods_of_africa_timing.defiance_review_days); owner activates it at common\scripted_effects\012_africa_gods_effects.txt:4120-4142. | Africa accepts the paid offer for success; timeout records failure and retry pressure. The pending flag prevents a duplicate reconciliation mission. It can overlap the final-ultimatum mission. |
| gods_of_africa_final_ultimatum_mission | Participant country; participant category. | No map region; Tier V/final-ultimatum gate for a current participant. | 60 days (gods_of_africa_ultimatum.deadline_days); the issuer sets the due day and activates at common\scripted_effects\012_africa_gods_punishment_effects.txt:503-510. | Return land/make peace or pay the settlement resolves it; refusal or timeout brings the advertised catastrophe. One pending flag prevents duplicate ultimata for a participant. Its overlap with reconciliation is the concern above. |

The three missions are owner-started, non-selectable response surfaces. Their available trigger is deliberately false, leaving success in explicit response decisions and failure in the mission timeout. No decision-level modifier needing its own removal timer appears in these three mission definitions. Settlement delivery is a repeatable decision, not a mission; it uses the configured 30-day days_re_enable and checks pending obligations and spare stock.

## Cost and requirement clarity

No in-scope action exceeds four distinct spendable types per execution. The optional protection shipment is one of convoy or train, never both, so protection is three fixed types plus one alternative at most. The Event 012 four-type cap is respected. The separate Event 013 price was not audited or changed.

| Action family | Distinct spendable types per use | Texticon coverage and clarity |
| --- | --- | --- |
| Demand, partial shipment, installment, and substitute slot actions | One dynamic family/material per contract. | GetGodsOfAfricaPaymentIcon, GetGodsOfAfricaDemandIcon, GetGodsOfAfricaInstalmentIcon, and substitute-slot helpers map the frozen family to its texticon; the inline value contains one amount. |
| Voluntary aid | One: infantry equipment or fuel, selected equipment-first by the helper. | Dynamic normal/blocked strings use infantry-equipment or fuel texticons; the tooltip states ordering, reserve, and cooldown. |
| Ultimatum settlement | Two: political power and infantry equipment. | £pol_power and £infantry_equipment_text_icon appear in normal and blocked strings. The availability tooltip shows PP amount, equipment amount, and reserve; the effect tooltip promises the same two payments and Wrath relief. |
| Final Council pledge/speech and reconciliation/preparation actions | One per action: infantry equipment or political power. | Matching equipment or £pol_power icons are present in each custom cost localization. |
| Partner protection | Three fixed: infantry equipment, fuel, and political power; optionally one convoy or one train. | Three base texticons fit inline; the full tooltip names both optional transport alternatives and reserve requirements. Four types maximum per actual use. |
| Arm a target / African expedition / occupier coercion | Coalition: infantry equipment + PP (2). Expedition: infantry equipment + support equipment + manpower + PP (4). Coercion: PP plus Africa’s conditional rifle support transfer (2 resource types total). | All displayed types use matching icons. Expedition is the only four-value inline string and is the cost-presentation defect above. |
| Settlement delivery | Two outgoing types: infantry equipment and fuel from the host’s frozen obligations. | This fulfills a prior obligation rather than charging the participant. Its row explains available stocks and reserves. |

Conditions such as owning/holding land, target eligibility, focus unlocks, relationship state, war status, spare stock above reserve, host collapse limits, and cooldowns are requirements or consequences, not additional spendable types. No literal resource-name fallback was found in valid audited cost strings. The dynamic mobile-artillery icon helpers have a “shipment unavailable” fallback; the valid-contract trigger is expected to bind a truck/artillery subtype, so this malformed/stale-state presentation remains an edge case rather than a proven valid cost path.

## AI validity, route locks, and balance evidence

Targeted host decisions use bounded participant/candidate arrays and current-target predicates for accept/reject substitute, reconciliation, offender marking/escalation, coalition support, expedition, and occupier coercion. Participant response rows require the current host/generation and current contract; lost-host rows are closed except for explicit recovery/victor surfaces. No dead-country target or invalid-route decision was established in this source pass.

The exact live decision schema was used, but the scenario evaluator did not establish action visibility. Four declared scenarios were accepted in the broad inspect, which returned DECISION_ANALYZED_PARTIAL, sourceRevision 42dda9cb037cb3721cca63618cc62bd797e248553b1556eaa15ac2be9d711607, reportHash c672e8db6951764354a61aa4d4657d7090627561dbe942141a31eac65cf0018a, and 100 unresolved definitions. The linked artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58bf39f1996feaceb947e494bb7ccd5b8734b9a0877d720f5e20904dbc673aed/81006f91435f1909ae801dbaf4b5c06f7a397473983a71d69339ef7809870056/decision-c672e8db6951764354a61aa4.json.

A one-scenario retry for 012_GODS_OPEN_DEMAND_NARROW inspected gods_of_africa_negotiate_demand. Its linked artifact was read through verified byte ranges, with size 1,475,851 and SHA-256 8ed11780435e1f1d400507e02f48c5ceffd1efcbaa285c343488bbd2b9c1aa51; the source revision is 615f5d7f74a9d9c46dd503fe7b7596c6e89787ca77c4eece7e6257ba05335768. The tool returned 145 unresolved scenario inputs, including exists, has_capitulated, capital_scope, authority epoch/host identifiers, participant-array bindings, war state, and dynamic helper operands. Its reported false visible/available states are unresolved and are not treated as hidden or blocked decisions. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ed11780435e1f1d400507e02f48c5ceffd1efcbaa285c343488bbd2b9c1aa51/56c810e032e435eb830a9589eb091c807241c02f656ee5a4afb75c2856e99d00/decision-ef0c1e55504a241065d9cc52.json.

The current server-status resource reports version 3.10.0 at hoi4-agent://server/status; the artifact template supports bounded byte ranges. The narrow decision artifact embeds a separate score-only AI baseline with unresolved entries; it is not used as probability evidence. Per parent instruction, this audit does not run a new broad probability pass or claim normalized choices. The existing 012_gods_activation_probability_final_2026-10-07.md remains the source for the exact eight-candidate audit and its incomplete scenario/comparison limits. No AI weights were changed.

## Localisation, cleanup, and exploit risk

Recovery decisions have localized names and descriptions in localisation\english\012_africa_gods_recovery_l_english.yml. Demand, reconciliation, ultimatum, and settlement descriptions state the current obligation, cost, deadline, or consequence. The remaining localisation gaps are the expedition cost tooltip and the confirmation/value-clarity findings above.

The parent has committed cleanup 4eb9fdeaf97c1ebf1154829bf1175edf93abec54 for gods_of_africa_cancel_participant. That cleanup addresses the transient agreement/instalment/diplomatic terms and quote/capacity/ease/burden fields identified by the parent. This audit does not duplicate the helper internals or claim to have reviewed that patch. Decision rows themselves require current host/generation/active-demand conditions, so the cleanup is a parent-owned integration dependency rather than evidence that a stale response button remains visible.

The parent separately owns the transaction-internals review of gods_of_africa_ultimatum_pay_settlement (common\scripted_effects\012_africa_gods_punishment_effects.txt:568+). Its player-facing decision costs are exactly PP plus infantry equipment; normal and blocked strings carry both matching icons, and the requirement text preserves the rifle reserve. The effect tooltip promises the full PP/equipment payment, lifts the ultimatum, and reduces Wrath. The decision offers no partial-delivery response; whether the effect verifies a measured transfer or resolves after zero/partial delivery remains the parent’s open internal question.

The parent also identified gods_of_africa_council_pledge in common\scripted_effects\012_africa_gods_focus_payoff_effects.txt:55-74: it sends equipment directly, adds the nominal pledge amount to host reserve, and records coarse aid history without a measured contribution-ledger receipt. This is accepted L27 final-shipment aid that should feed full grading. The parent owns that measured-receipt integration; no internals audit or patch is made here.

No repeat exploit was established in the decision declarations. Voluntary aid is need/reserve/cooldown gated, defensive preparation is once-only, target interventions carry cooldowns, the substitute flow closes after one offer, and settlement delivery re-enables at its 30-day interval. The ultimatum settlement is a single two-type payment, not a recurrent store.

## Visual evidence, skipped validation, and remaining limits

The category source explicitly says these are ordinary decision categories with no attached scripted GUI. I called hoi4.gui_inspect and hoi4.gui_render on gods_of_africa_participant_category. Inspection returned inspectedElementCount = 0, one missing fidelity reference, and a missing-window diagnostic; render returned a 706-byte offline SVG whose metadata says GUI window gods_of_africa_participant_category was not found. The render reports offlineRepresentation = true; it contains no decision rows or click regions. Inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9cb4bc7c1041b72d9dc70196a16bff8bada706165e81d58a347ff326b8227f13/fe717adc77b2cd2ae6f828e9fc4a0225565b30667b491210be5a77de485d9857/gui-inspect.780a430e07670f2c.json. Render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb078e8331dda35a7934dafe88556926b369bdb98e80e9209c7b978e6ea11291/8c8bfb2974cdb5a4841fa7048e6ff02ca270285d9b328962261d9540e63e4249/gods_of_africa_participant_category-full.svg. No source or MCP projection is native decision-list proof, and no clipping/alignment claim is made.

References read:

- Offline Decision modding, cost and custom-cost behavior: paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:284-336, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.
- Offline Decision modding, missions: the same file at :465-510, same revision.
- Installed decision-category and trigger-cadence documentation: C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md:1-46, revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019.
- Installed mission-timeout dynamic-variable documentation: ...\documentation\dynamic_variables_documentation.md:238-240, revision 538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda.
- Vanilla mission precedent GER_mefo_bills_mission: game:common/decisions/GER.txt:92-161, source-lookup revision ce04fbc609b5651e24a686bb19b6d69216d664d1cb94c8f782b40728157497f1.

No game was launched; no logs, saves, or live-game validation were requested. No tests were run for this read-only assignment. No implementation file or AI probability surface was changed.

## Handoff

Changed file: docs\plans\012_africa_plans\subagent_handoffs\012_gods_decision_surface_review_2026-10-07.md only.

Changed decision, mission, GUI, or localisation ids: none.

Before/after behavior: not applicable; this is a read-only audit.

Meaningful validation performed: targeted decision source, current localisation/helper, mission lifecycle, source lookup, offline reference, and bounded decision-inspector review described above.

Skipped meaningful validation: native decision-row visual inspection could not be produced because the ordinary category window is not a scripted GUI source. The decision inspector’s category/action gates remain unresolved for the declared scenario inputs. Parent-owned transaction and measured-receipt internals were intentionally not duplicated.

Remaining parent work: decide and implement category/action phasing, permanent-defiance confirmation, expedition cost presentation, fixed PP AI saving hints, substitute shortcut disposition, and any accepted value-copy clarification; finish parent-owned ultimatum transaction, Council contribution-ledger, and committed cleanup review; carry forward the existing probability report’s incomplete limits.

Separate plan handoff: none written.
