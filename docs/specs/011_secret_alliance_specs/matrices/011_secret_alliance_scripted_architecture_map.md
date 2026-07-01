# Event 011 Secret Alliance Scripted Architecture Map

This is a design handoff for `chaosx_scripted_system_architect`. Names are proposed working identifiers and may be adjusted to match existing repo conventions.

## Helper families

| Helper | Scope | Inputs | Outputs | Side effects | Expected call sites |
| --- | --- | --- | --- | --- | --- |
| `secret_alliance_can_be_target` | country | candidate target | yes or no trigger | none | event availability, manual debug tests |
| `secret_alliance_is_valid_founder` | country with target event target | candidate founder | yes or no trigger | none | founder selection loops |
| `secret_alliance_score_founder_candidate` | country with target saved | candidate founder | temp score variable | none | selection helper |
| `secret_alliance_initialize_pact` | target country | selected founders | member arrays, role flags, core values | saves target and founders, sets hidden flags | Event 011 opening |
| `secret_alliance_assign_founder_roles` | target country | founder array | role flags on members | sets Convener, Financier, Provocateur | opening helper |
| `secret_alliance_try_invite_member` | target country | candidate pool and stage | possible new member | sets member flags and variables | monthly or event-paced invitation pulses |
| `secret_alliance_refresh_member_validity` | target country | member arrays | cleaned member list | removes invalid members, updates count | on reveal, monthly pulse, decision use |
| `secret_alliance_apply_hidden_incident` | target country | incident family | incident result flags | may damage, alter relations, raise values | baseline and evolution incident events |
| `secret_alliance_record_suspicion_gain` | target country | amount and source | suspicion variable | event log note if threshold crossed | incidents, decisions, missions |
| `secret_alliance_record_evidence_gain` | target country | amount, source, suspect | evidence variable, suspect flags | may reveal suspect status | investigations and missions |
| `secret_alliance_check_evolution_unlocks` | target country | chaos and pact state | evolution flags | records evolution entries if enabled | timed pact controller |
| `secret_alliance_reveal_pact_publicly` | target country | reveal cause | public reveal state | exposes members, opens crisis phase | exposure decision and self-reveal |
| `secret_alliance_reveal_pact_by_war` | target country | member enemy | formal faction and war joins | fires super-event, changes ideas | any member-target war check |
| `secret_alliance_form_anti_target_faction` | pact leader | target and members | faction | creates dynamic name and invitations | war reveal and final ultimatum |
| `secret_alliance_member_leave_pact` | member country | reason | exit flag, cleanup | removes ideas, roles, target flags | diplomacy, defeat, cleanup |
| `secret_alliance_collapse_pact_if_invalid` | target country | member count and war state | collapse or continue | cleanup and aftermath | refresh helper and peace events |

## Constants and tuning plan

Place shared tuning in a script constants file owned by the event or diplomacy system.

| Constant group | Example values to centralize |
| --- | --- |
| selection weights | founder base score, faction penalty, neighbor bonus, claim bonus, ideology bonus |
| starting values | baseline secrecy, cohesion, readiness, suspicion, evidence, counter-readiness |
| evolution thresholds | minimum chaos, minimum age, member count, readiness, and cohesion gates |
| member caps | baseline cap, Evolution I cap, Evolution II cap, Evolution III cap, major patron cap |
| incident pacing | minimum days between incidents, weighted incident families by stage |
| decision costs | equipment, trains, trucks, PP, XP, stability, war support, civilian burden |
| AI weights | investigation willingness, invitation willingness, exposure caution, war preparation |
| reveal thresholds | evidence thresholds, self-reveal readiness, ultimatum timer bands |

## Event target and cleanup plan

- Save the original target country as the event target used by all pact logic.
- Save founders as role-based event targets only for immediate opening logic, then persist membership through flags and arrays.
- Use global event targets only where long-lived cross-event access is required.
- Clear global targets and selected GUI targets during pact collapse, target death, member invalidation, or war aftermath.
- Do not rely on hidden event targets to decide whether no-actor evolution log rows exist.

## Migration and reuse plan

The implementation should avoid writing one-off reveal, member cleanup, and value math inside event options. Shared helpers should be called from events, decisions, missions, AI pulses, GUI buttons, and aftermath cleanup. If the repo already has dynamic value or selected-target helpers, reuse them instead of duplicating the pattern.

## Risks for the architect

- Faction creation and dynamic faction naming may need existing Chaos Redux faction helper patterns.
- Timed flags may reject dynamic duration tokens. Use repo duration guidance before setting timed flags.
- Member arrays must stay aligned across member id, role, status, confidence, revealed state, and promise flags.
- GUI selected target state needs cleanup when selected country exits the pact.
- AI should not require human-only GUI selection to use member-target decisions.
