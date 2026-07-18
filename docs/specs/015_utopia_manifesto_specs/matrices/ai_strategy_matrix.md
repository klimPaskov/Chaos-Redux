# AI Strategy Matrix

| Actor or state | Preferred behavior | Avoid | Escalation condition | Cleanup behavior |
| --- | --- | --- | --- | --- |
| Eligible AI recipient | accept manifesto | rejection | none, acceptance is fixed | initialize route evaluation |
| Democratic founder | Consent or hidden humanist | Closed Island without desperation | invasion, collapse, extreme chaos | restore voluntary institutions after emergency |
| Communist founder | Common Table | private elite restoration | council support, class conflict, blockade | resolve council versus central-plan state |
| Neutral founder | Guardians of Measure | ideological expansion without need | severe shortage, infrastructure weakness | revise plan when data becomes invalid |
| Fascist founder | Closed Island | open plural route | encirclement, war, low Concord | maintain or abandon coercive systems through crisis |
| Voluntary route AI | Open Call, charters, leases, league | low-integrity ultimata | severe Need and repeated refusal | renounce obsolete cases |
| Council route AI | council staffing, common stores, commune partners | mercenary dependency | blockade or member emergency | convene congress, clear deadlocked missions |
| Planner route AI | guaranteed placement, districts, forecasts | too many simultaneous projects | high Need, infrastructure collapse | cancel invalid project and recount |
| Closed Island AI | quotas, fortification, autarky, coercive cases | aid that empties stores | severe threat or high chaos | suppress or reopen after reserve crisis |
| Hidden humanist AI | mixed economy, public audit, peaceful cases | penal labor and forced integration | literal-route failure | sunset obsolete policies |
| League founder | invite small credible partners, deliver aid | annexing members | common external threat | expel invalid members and clear obligations |
| League candidate | join when autonomy and aid are credible | founder with coercive claim history | threat or shortage | leave after betrayal |
| Major sponsor | guarantee, aid, influence | ordinary membership | regional relevance | withdraw or compete with rival sponsor |
| Need target AI | counteroffer when possible | free concession without motive | severe threat from founder or shared crisis | close negotiation after case ends |
| Associate AI | demand provision and charter | instant integration | high local support or severe threat | choose autonomy, integration, or exit |
| Auxiliary source AI | negotiate payment and leverage | unpaid contract | founder desperation | withdraw, defect, or settle contract |
| AI at low Plenty | stores, repair, one project | aid and distant integration | existential Need | reduce commitments |
| AI at low Concord | route-specific reform or repression | ambitious voluntary formation | revolt or constitutional crisis | resolve temporary emergency flags |
| AI at high Need | domestic alternatives, emergency provision, one case | multiple opportunistic cases | blockade, migration, loss of port | close cases after remedy |
| AI at high chaos | reserve, defense, stronger route choices | ordinary peacetime assumptions | evolution conditions | preserve baseline path when evolution disabled |

## Current implementation proof

The current AI package defines 12 plans in `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt`:

- `utopia_manifesto_foundation_restraint`
- `utopia_manifesto_consent_route_strategy`
- `utopia_manifesto_common_table_route_strategy`
- `utopia_manifesto_guardians_route_strategy`
- `utopia_manifesto_closed_island_route_strategy`
- `utopia_manifesto_closed_island_valid_case_escalation`
- `utopia_manifesto_joke_understood_route_strategy`
- `utopia_manifesto_low_plenty_recovery_strategy`
- `utopia_manifesto_high_need_recovery_strategy`
- `utopia_manifesto_low_concord_restraint_strategy`
- `utopia_manifesto_constitutional_crisis_strategy`
- `utopia_manifesto_mature_commonwealth_strategy`

All 124 focuses contain AI logic. All 121 decisions contain AI weights or an intentional zero-use behavior. The same live Ledger, calling, reserve, district, case, target-survival, stewardship, and obligation gates apply to player and AI action. No Event 15 maintenance plan uses recurring global iteration.
