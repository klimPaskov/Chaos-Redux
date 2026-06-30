# Event 011 Secret Alliance decision and mission map

## Decision families by stage

| Family | Baseline | Evolution I | Evolution II | Evolution III |
| --- | --- | --- | --- | --- |
| Investigation | Hidden until suspicion threshold | Limited if suspicion high | Full family | Converts to evidence and patron isolation |
| Defensive security | Hidden until category opens | Limited if serious incident fires | Full family | Converts to war readiness and emergency defense |
| Diplomacy | Hidden | Limited quiet talks if member partly known | Full split and leak family | Public isolation and disbandment demands |
| Border operations | Hidden | Hidden | Neighboring member operations | Border defense and preemptive war case |
| War preparation | Hidden | Hidden or low readiness | Full preparation family | War option and allied support |

## Specific action map

| Working id | Family | Visibility | Key requirements | Main cost types | Main outputs | Main risks |
| --- | --- | --- | --- | --- | --- | --- |
| `trace_diplomatic_pouches` | Investigation | Category open | Suspicion and unknown member | Command power, agency capacity, civilian burden | Evidence, member exposure | Pact pressure, cipher change |
| `turn_courier` | Investigation | Courier incident or high suspicion | Active courier target | Political capital, operative access, stability risk | Strong evidence, leak chance | Infiltration, agent scandal |
| `break_radio_net` | Investigation | Agency or signal route | Sufficient equipment or XP | Air XP, support equipment, command power | Cohesion falls, timing revealed | Pact upgrades security |
| `audit_foreign_missions` | Investigation | Industrial survey seen | High-value states exist | Civilian burden, stability risk | Sabotage setup blocked | Diplomatic chill |
| `build_public_dossier` | Investigation | Evidence high | Evidence threshold | Political power, credibility, time | Controlled reveal route | Weak dossier hardens pact |
| `guard_rail_port_nodes` | Defense | Category open | Key state group exists | Infantry equipment, trains, tied divisions | Preparedness, sabotage reduction | State fatigue if repeated |
| `vet_military_staff` | Defense | Command threat | Advisor or general target exists | Army XP, command power | Assassination risk falls | Planning penalty |
| `harden_munitions_plants` | Defense | Industrial threat | Military factories exist | Support equipment, trucks, output burden | Factory damage reduction | Production slowdown |
| `secure_capital_ministries` | Defense | High infiltration or low stability | Capital controlled | Political power, stability, local pressure | Infiltration falls | Public fear |
| `quiet_talks_member` | Diplomacy | Partly known member | Member not fanatical | Political power, relations, trade concession | Member confidence falls | Pact pressure rises |
| `face_saving_exit` | Diplomacy | Wavering member | Member confidence low | Civilian burden, concession | Member leaves | Other members harden |
| `pressure_neutrals` | Diplomacy | Evidence medium | Neutral countries exist | Diplomacy, political power | Invitation chance falls | Relations cost |
| `controlled_leak` | Diplomacy | Evidence high | Public dossier path | Stability risk, credibility | Cohesion falls, member exposed | Reveal accelerates |
| `sweep_frontier_safehouses` | Border | Neighbor member partly known | Supplied divisions in border | Command power, infantry equipment | Exposure rises | Pressure rises |
| `seal_courier_pass` | Border | Courier route through border | Border or rail control | Trains, trucks, divisions | Cohesion falls | Infiltration rises |
| `limited_border_reprisal` | Border | Evolution II, high evidence | Neighbor member, army ready | Army XP, command power, equipment | Member opening strength falls | Immediate reveal chance |
| `contingency_plans` | Preparation | Evolution II | Army staff available | Army XP, command power | Preparedness rises | Staff overstretch |
| `fuel_reserve_security` | Preparation | Evolution II or III | Fuel storage or import route | Fuel, civilian burden | War readiness | Consumer goods burden |
| `local_defense_committees` | Preparation | High pressure | Manpower and rifles | Manpower, infantry equipment, stability | Defensive state readiness | Public militarization |
| `rally_friendly_governments` | Preparation | Evidence medium | Friendly countries exist | Political power, relations | Guarantees, volunteers, support | Diplomatic blowback |
| `prepare_public_war_case` | Preparation | Evidence high | War pressure | Political power, time | War option has lower stability cost | Pact rushes public reveal |

## Mission map

| Mission | Owner | Active stage | Requirement direction | Duration direction | Success | Failure |
| --- | --- | --- | --- | --- | --- | --- |
| Guard the capital network | Target | Category open | Supplied divisions around capital and key rail states | Medium | Preparedness rises and one severe incident is blocked | Infiltration rises |
| Secure the industrial belt | Target | Evolution II | Control and guard dynamic high-value industry states | Medium to hard | Sabotage damage reduction | Industrial incident fires |
| Keep the foreign route watched | Target | After courier route | Hold border, port, or rail route depending on geography | Medium | Evidence rises | Cohesion rises |
| Expose the patron hand | Target | Patron suspected | Evidence, investigation success, diplomacy action | Hard | Patron pressure falls and second-major route blocked | Patron confidence rises |
| Hold the border during public crisis | Target | Evolution III | Supplied divisions and fuel along threatened border | Medium | First pact offensive weakened | Pact opening momentum rises |

## Category cleanup matrix

| Cleanup cause | Required cleanup |
| --- | --- |
| Target gone | Remove category, stop missions, clear selected member cards, keep history flags |
| Member gone | Clear member flags and cards, recalculate member count |
| Public reveal | Hide hidden action family, show public crisis action family |
| Pact defeated | Close public crisis actions, keep achievement and history flags |
| Member leaves | Clear member action decisions and active border missions for that member |
| Patron invalid | Remove patron role, select public leader if reveal already happened |
