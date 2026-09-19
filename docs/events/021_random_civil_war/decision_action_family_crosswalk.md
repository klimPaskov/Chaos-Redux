# Event 021 Decision and Mission Action-Family Crosswalk

This crosswalk resolves the named action and mission families in the Event 021 decision specification against the phase-specific normal decision category and settlement callbacks.
The category intentionally exposes only three to five relevant primary actions and one to three missions at a time, so every family does not receive a simultaneously visible identifier.
The mapping is an implementation disposition, not a claim that every family has independent runtime acceptance.

| Spec family | Current surface | Implementation disposition |
| --- | --- | --- |
| Secure the arsenals | `event021_secure_arsenals` | Direct opening decision with equipment, trains, command power, authority, pressure, and same-tag leverage effects. |
| Establish a capital defense command | `event021_defend_capital` | Direct opening decision with manpower, infantry equipment, command power, capital defense state, and authority effects. |
| Restore the rail spine | `event021_secure_rail_spine_mission`, `event021_reconstruct_administration` | The mission holds a stored opening-front rail state and reconstruction repairs the same bounded state; no second rail action is exposed in the same phase. |
| Conduct a bounded loyalty review | `event021_review_loyalty` | Direct decision with a hardliner failure branch and authority/pressure consequences. |
| Integrate loyal formations | `event021_integrate_formations` | Direct active-front decision that advances integration progress and removes fractured-command pressure. |
| Negotiate a regional guarantee | `event021_offer_emergency_settlement`, `chaosx.nr21.5` | Settlement talks open the regional guarantee and obligation selector; the named guarantee is a settlement term, not a duplicate action. |
| Offer a limited amnesty | `event021_offer_emergency_settlement`, `event021_hold_settlement_terms_mission` | Amnesty is represented by the settlement obligation and its timed terms mission, with failure and postwar memory handled by settlement resolution. |
| Call an emergency coalition | `event021_complete_coalition_governance` | Coalition governance is a settlement-obligation action and is unavailable outside its obligation phase. |
| Emergency requisition | `event021_secure_arsenals`, `event021_decision_seize_depot` | Requisition is deliberately bounded into arsenal/depot actions so it spends real stockpile resources and cannot become a repeatable free-source decision. |
| Seize a local depot | `event021_seize_depot` | Direct opposition/front decision requiring a valid owned and controlled depot target. |
| Organize regional recruitment | opening force package and `event021_integrate_formations` | Recruitment is package-specific opening/reinforcement logic; the visible action is integration because Event 006 actors must retain their own reinforcement content. |
| Integrate defecting officers | `event021_integrate_formations` | Shared integration action consumes the current front’s integration progress and does not create duplicate characters or rosters. |
| Establish field administration | `event021_reconstruct_administration`, `event021_review_regional_administration` | Reconstruction and prevention administration cover the controlled-region authority and supply role. |
| Open a foreign liaison | `event021_support_government`, `event021_support_opposition`, `event021_offer_mediation` | Evolution II neighbor actions provide separate civilian relief, armed support, and mediation channels with sponsor receipts and commitment caps. |
| Request recognition | `event021_offer_emergency_settlement`, settlement outcomes | Recognition is a settlement gate and outcome rather than a free-standing diplomatic action. |
| Coordinate with another opposition front | `event021_set_priority_front`, multi-front front registry | The priority-front action and front registry coordinate the selected front without introducing a second selection GUI. |
| Reject the rival claim | settlement selection and `event021_set_priority_front` | Rival-claim rejection is represented by settlement terms and front-priority commitment; hardliner outcomes preserve separate claimant settlement paths. |
| Hold the capital | `event021_hold_the_capital_mission` | Timed mission with distinct success and timeout effects. |
| Secure the rail junctions | `event021_secure_rail_spine_mission` | Timed mission bound to an opening-front logistics state. |
| Protect the depot belt | `event021_seize_depot`, depot state receipt, and settlement resolution | Depot protection is a state-targeted action with actual control proof; failed control is handled by the front and settlement lifecycle. |
| Keep the corridor open | `event021_open_relief_corridor` | Separate civilian relief decision; armed support decisions do not reuse the civilian action. |
| Complete local mobilization | opening force package, package reinforcement, and `event021_integrate_formations` | Mobilization is derived from actual force, manpower, equipment, and package limits rather than a free visible division-spawn action. |
| Deny recognition | `event021_review_loyalty`, settlement terms, and sponsor decisions | The denial surface is role- and phase-specific, using loyalty, settlement, and sponsor gates without a duplicate recognition button. |
| Preserve the civilian route | `event021_open_relief_corridor`, `event021_offer_mediation` | Civilian relief and mediation are separate effects and use distinct resource profiles. |

The crosswalk therefore resolves the completion-audit finding that the specification names more families than the normal category can show at once.
The remaining open gate is runtime proof that each phase-specific surface appears and resolves correctly in live play.
