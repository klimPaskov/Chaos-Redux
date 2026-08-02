# Event 016: Kruger Directorate

## Scope

The Kruger Directorate is the ordinary host-country management surface for Event 016. It gives Doctor Warren Kruger's current host one decision category for institutional form, facilities, staff, scientific priorities, internal security, foreign liaison, technical authority, and generic project-ledger commands.

This implementation owns the host framework around projects. The fifteen native project families, their stages, rewards, incidents, technologies, equipment, and units remain in the Event 016 project package. The Directorate never substitutes generic progress for a family-native outcome.

## Activation and visible state

`brilliant_scientist_directorate_category` is visible only to the country accepted by `brilliant_scientist_is_current_host`. Its category description exposes the four player-readable variables as integers:

- `brilliant_scientist_mandate`: formal authority granted to Kruger and the Directorate.
- `brilliant_scientist_dependence`: reliance on Kruger's personal methods and command.
- `brilliant_scientist_exposure`: foreign and public visibility of the programme.
- `brilliant_scientist_project_capacity`: institutional bandwidth available for ambitious work.

Independent Capacity and Grievance remain hidden. Decisions alter them through the shared measure helpers, while their consequences are communicated through requirements, incidents, control-state triggers, and player-facing warnings elsewhere in Event 016. The header also resolves a broad Government Control label from the shared stable, strained, compromised, and lost flags. Named appointment, institutional, priority, security, and authority fragments explain the visible causal direction without printing either hidden value. The latest loyalty-review and relocation records remain visible after their transient request context has been cleared.

At appointment and ordinary transfer, the host receives one mutually exclusive archetype flag from its current country facts: refugee network, colonial or overseas empire, strong university system, industrial power, militarized state, small threatened state, or a neutral default. The archetype is presentation state rather than a fifth Directorate meter. It supplies a country-shaped clause in the existing `.4`, `.5`, `.6`, `.7`, `.8`, `.9`, `.10`, and `.11` reports and gives their AI choices a modest preference for universities, factories, security offices, emergency survival, or diplomacy. The same preference now reaches the four initial institutional-form decisions: university and refugee hosts favor the Public Science Council, militarized and threatened hosts favor the Compartmentalized Military Office, industrial and colonial hosts favor the Private Industrial Concession, and refugee or colonial hosts favor the Exile Scholar Network. These are bounded AI weights on existing choices, not new routes or meters. The assignment is repeated for a transfer recipient, so a former host's presentation never leaks into the new country.

Shared tuning introduced here is under `common/script_constants/016_brilliant_scientist_directorate_constants.txt`. Timing, political costs, equipment gates and spends, construction burdens, persistent modifiers, and AI weights are separated by category. The priority and relocation cooldown values are additionally mirrored as file-scoped `@` literals in their decision files because the timed-country-flag `days` field rejects script-constant and variable tokens; both copies must change together. The shared `brilliant_scientist_measure_delta` ladder remains the source for minor, moderate, and major meter changes.

## Institutional forms

The host selects one mutually exclusive institutional form. The choice sets `brilliant_scientist_directorate_institution_established`, a route flag, a self-cleaning dynamic modifier, and immediate visible or hidden measure changes.

| Form | Character | Central trade-off |
| --- | --- | --- |
| Public Science Council | Civilian and university oversight | Less Mandate and Dependence; more public Exposure and conventional research |
| Compartmentalized Military Office | Guarded military chain | Faster special projects and better detection; greater Dependence and civilian burden |
| Private Industrial Concession | Privileged industrial partners | Better factory learning and prototypes; commercial exposure and weaker direct control |
| Exile Scholar Network | Displaced international specialists | Strong research and project breadth; political fragility and foreign attention |

Every Directorate dynamic modifier uses `brilliant_scientist_is_current_host` as its enable condition and removes itself when the country ceases to be Kruger's host. Transfer and terminal cleanup must still clear the associated route and action flags so a former host does not retain stale state.

## Facilities and staff

The facility decisions operate through the shared Event 016 facility targets rather than hardcoded state IDs.

- Formalizing the primary campus invests support equipment, trucks, fuel, construction time, and political authority in `event_target:brilliant_scientist_primary_facility`, then adds exactly one infrastructure level there.
- Expanding the prototype works requires the persistent shared project ledger to report at least one Deployment-stage project. It adds one shared building slot and one military factory to the primary site; the one-use country flag prevents repeating that grant.
- Establishing a secondary laboratory requires the recruited research cohort and a distinct owned, fully controlled core state with at least two Infrastructure levels, a Civilian Factory or Military Factory, and either a home-area connection or a Supply Hub. It adds exactly one Infrastructure level, then saves that state as `event_target:brilliant_scientist_secondary_facility`.
- Relocating the primary laboratory is a state-targeted transfer plan, not an unconditional success effect. The destination must be a prepared owned and fully controlled core state with at least two Infrastructure levels and a Civilian Factory or Military Factory. A land transfer requires a home-area connection; an overseas transfer requires a Naval Base and consumes convoys in addition to trucks and fuel. Completion records a persistent request context and starts the relocation cooldown.
- Hardening the primary site is a one-time defensive construction programme that adds one anti-air level and one land-fort level, preventing repeated building or meter farming.
- Mobilizing repairs highlights the damaged primary site and gives the host a timed native repair-speed burden. It does not fabricate instant repairs.

The relocation producer never adds infrastructure, factories, shared slots, facilities, or prototypes. A successful resolver may move the primary-facility state flag and global target, but it must not duplicate or recreate the physical investments left in the network. This keeps repeated transfers from becoming a construction exploit.

The first permanent facility investment sets `brilliant_scientist_facility_network_invested`, which is an Event 016 proof flag used by downstream achievements and resolutions. `brilliant_scientist_facility_network` represents the continuing national burden once the network is established.

The staffing path first recruits a permanent research cohort and can then replace it with a university research network. The upgrade removes the cohort modifier before applying the university modifier, preventing additive double-counting.

## Scientific priorities, security, and authority

Fundamental Inquiry, Prototype Delivery, and Distributed Replication are mutually exclusive priorities. Changing priority removes the other priority modifiers, records the selected priority flag, and applies a common cooldown. The institutional meter shift for each priority occurs only on that priority's first adoption; returning to an already tried priority changes the active modifier without repeating its one-time Mandate, Dependence, Exposure, Capacity, or hidden-state effects.

The internal security section establishes a persistent counterintelligence institution. Its repeatable operations are deliberately differentiated:

- clearance rotation is a light, frequent reduction in current Exposure;
- a loyalty review starts a visible 45-day mission and produces an uncertain findings context rather than applying a guaranteed meter reward;
- false procurement trails consume logistics and Project Capacity to obscure the programme.

Only one security action may run at a time. A pending loyalty finding blocks another review but does not incorrectly block clearance rotation. These are host-triggered decisions and missions, not recurring global on-actions.

The authority path offers cabinet safety oversight, delegated technical authority, and final sovereign technical authority. Cabinet review improves stability and political control while slowing projects. Delegation accelerates work but increases Exposure. Final authority replaces delegated authority, sets `brilliant_scientist_sovereign_science_authority`, and creates the strongest project-speed/political-control trade-off.

## Directorate outcome resolvers

The Directorate owns bounded context producers, while `common/scripted_effects/016_brilliant_scientist_directorate_outcome_effects.txt` commits their narrative outcomes. Neither producer polls the world on a recurring on-action.

### Loyalty review

When `brilliant_scientist_loyalty_review_mission` expires, the host receives `brilliant_scientist_directorate_loyalty_review_requested`. The mission snapshots Mandate, Dependence, Exposure, Independent Capacity, Grievance, the Prototype/Deployment/Weaponization counts, and a four-step intelligence score assembled from agency presence, a mature agency, any operative, and a multi-operative team. It also records boolean history flags for cloning, robotics, paleogenetics, xenobiological synthesis, and singularity projects.

The country-scope resolver `brilliant_scientist_resolve_directorate_loyalty_review_request` is called directly at the end of the mission's `timeout_effect`:

```txt
brilliant_scientist_resolve_directorate_loyalty_review_request = yes
```

The resolver requires the request flag and weights rather than guarantees its result. Foreign-agent findings gain weight from Exposure, agency capability, operatives, and existing foreign access. Kruger-loyalist findings gain weight from Dependence, Independent Capacity, Grievance, and sovereign technical authority. Transformed-personnel findings require relevant project history to become likely. Weak intelligence and low Exposure favor an inconclusive review or a wrongful purge. The chosen finding writes mutually exclusive latest-result flags and a persistent history flag, applies its causal meter consequences, clears every request flag and snapshot variable, and then fires dossier event `chaosx.nr16.10`. It never creates a capturable operative, and an inconclusive review grants no Exposure reduction.

### Primary relocation

After the transfer timer, the host receives `brilliant_scientist_directorate_relocation_requested`. `event_target:brilliant_scientist_relocation_requested_origin` and `_destination` persist the two states. Route flags preserve whether land or sea logistics were paid. The host also snapshots Mandate, Exposure, Dependence, Project Capacity, Independent Capacity, Grievance, project-stage counts, and whether the plan was made under fire.

The country-scope resolver `brilliant_scientist_resolve_directorate_relocation_request` is called directly after the request context is written:

```txt
brilliant_scientist_resolve_directorate_relocation_request = yes
```

The resolver validates both global state targets again, including ownership, control, core status, infrastructure, industry, route suitability, and the absence of another facility-type record at the destination. Land routes, low Exposure, Mandate, and Capacity favor success. Sea movement, war, and Exposure favor interception. Advanced project counts and an actual undamaged Prototype-or-higher family enable prototype loss. Grievance, weak Mandate, Independent Capacity, Dependence, and sovereign authority favor refusal or escape. A zero-weight success cannot be selected after invalidation.

Success clears the primary-facility state flag and `brilliant_scientist_facility_type` variable at the origin, sets both at the destination, replaces `event_target:brilliant_scientist_primary_facility`, and grants no buildings, slots, facilities, prototypes, project stages, or equipment. Prototype loss calls `brilliant_scientist_damage_project` for the highest consequential eligible family found in the real ledger. Escape marks the requested destination with the hidden `brilliant_scientist_hidden_escape_cell` state flag without moving the fixed character or primary-laboratory target. Every outcome clears the request flag, route and under-fire flags, request targets, snapshots, selection scratch state, and outcome weights before firing dossier event `chaosx.nr16.11`.

## Foreign liaison lifecycle

Foreign actions use the shared Event 016 actor-selection helpers. `Review Foreign Approaches` is an explicit player or AI decision: its one-time completion effect refreshes valid foreign interest, selects one bounded actor target, and then all follow-up decisions operate only on that actor. There is no daily, weekly, or monthly world scan.

The host may:

- offer one controlled research-access package;
- open a persistent joint laboratory at a viable partner-owned site;
- accept a persistent foreign protection framework;
- restrict the currently selected actor's access;
- terminate standing controlled access, joint-laboratory, and protection frameworks.

The first Prototype and facility records also produce three finite host-context reports. `chaosx.nr16.7` settles the primary facility as a civic compact, restricted district, or industrial charter and applies a small causal shift to the existing meters. `chaosx.nr16.8` settles custody of the second resolved Prototype as public trust, executive reserve, or patent pool and adds the family to a persistent receipt array without changing its project stage. `chaosx.nr16.9` is owned by the foreign-resolution transaction and gives the host a named-actor response. These reports use the registered Directorate dossier picture, have dynamic family and operation text, and write matching host and Kruger-character history flags. They are ordinary incidents rather than evolutions, decisions, or additional rewards.

The existing loyalty and relocation dossiers, `chaosx.nr16.10` and `chaosx.nr16.11`, append the same host-archetype clause after their finding or convoy outcome. This keeps the selected institutional profile visible when security review or laboratory movement resolves without creating another reward, evolution, or event-log entry.

Controlled access, the joint laboratory, and the protection framework each have one successful lifetime establishment per host. Termination removes an active framework but retains its historical establishment flag, so a terminate/reopen loop cannot manufacture infrastructure or repeatedly harvest institutional meter changes.

The joint laboratory persists its country and state through:

- `event_target:brilliant_scientist_joint_laboratory_partner`;
- `event_target:brilliant_scientist_joint_laboratory_site`.

The protection framework persists its country through `event_target:brilliant_scientist_foreign_protection_partner`. Controlled research access persists its partner through `event_target:brilliant_scientist_controlled_research_access_partner`. The termination decision clears the controlled-access, joint-laboratory, and protection host flags; clears all partner/site flags; and clears all four global event targets. Event 016 transfer, host-removal, and terminal cleanup must perform the same cleanup in case the host loses the programme before choosing termination.

Opening foreign research access or a joint laboratory sets `brilliant_scientist_research_advantage_exposed`. Foreign liaison effects use Mandate, Dependence, Exposure, Project Capacity, Independent Capacity, and Grievance as causal state rather than flat diplomatic flavour.

## Generic project-board contract

The family-native project package publishes the current Directorate selection through:

- `brilliant_scientist_directorate_project_selection_ready`;
- `brilliant_scientist_directorate_selected_project_family`;
- `brilliant_scientist_directorate_selected_project_stage`;
- the selected-status flags for active, suspended, damaged, replicable, replicated, publishable, and published state.

The Directorate then provides six generic commands:

1. Approval locks the selected family/stage for the decision duration and writes `brilliant_scientist_directorate_project_approval_requested` plus approved family/stage variables. It never advances a project stage.
2. Suspension invokes `brilliant_scientist_suspend_project` and writes a family-native suspension request.
3. Resumption invokes `brilliant_scientist_resume_project` and writes a family-native resumption request.
4. Cancellation invokes `brilliant_scientist_dismantle_project` and writes a family-native cancellation request.
5. Independent replication invokes `brilliant_scientist_replicate_project_to_requested_stage` for an eligible locked family/stage, then records the completed replication and updates Dependence, Exposure, Project Capacity, and Independent Capacity.
6. Publication invokes `brilliant_scientist_publish_project` only for an independently replicated, publishable result, records completion, and sets `brilliant_scientist_public_reputation_established`, `brilliant_scientist_research_advantage_exposed`, and `brilliant_scientist_sovereign_science_authority`.

Long-running approval, replication, and publication decisions lock family/stage values at start. If the visible selection changes or the host is lost, their cancel triggers prevent completion against a different project.

The native project package must consume and clear the approval/suspend/resume/cancel request flags and their command variables after applying the matching family-specific effect. It must also rebuild the selected-status flags whenever the board selection or native project state changes.

## AI and balance

AI weights favour institutional choices consistent with government, war, control, Exposure, and capacity. Expensive decisions require resources above the exact spend, then remove the matching equipment, fuel, manpower, or experience at start. Timed construction and institutional actions impose consumer-goods and efficiency burdens while active, so political power is not a generic progress purchase.

The most powerful permanent bonuses have explicit costs:

- facility and university networks require construction and civilian allocations;
- Prototype Delivery and sovereign authority trade ordinary research or political control for special-project speed;
- foreign cooperation raises Exposure or Dependence;
- independent replication consumes a long project interval and logistics;
- publication creates the largest Exposure increase in the Directorate package.

The AI cannot bypass family prerequisites through the generic board. The native family package remains responsible for eligibility, capacity occupation, accident risk, stage advancement, and rewards.

## Localisation and UI assets

Player-facing decision strings are in `localisation/english/016_brilliant_scientist_directorate_l_english.yml`. Outcome reports and causal header fragments are in `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`. Broad control, cause, and latest-result selection is defined in `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt`.

Ordinary decisions deliberately use verified existing vanilla sprite identifiers:

| Use | Sprite identifier |
| --- | --- |
| Directorate category | `GFX_decision_category_SOV_soviet_academy_of_sciences` |
| Civil governance and foreign frameworks | `GFX_decision_generic_political_discourse` |
| Military institutional form | `GFX_decision_generic_army_support` |
| Industrial commitments | `GFX_decision_generic_industry` |
| Research, staffing, and project board | `GFX_decision_generic_research` |
| Security and access restriction | `GFX_decision_infiltrate_state` |
| Loyalty review | `GFX_decision_oppression` |
| Replication and covert logistics | `GFX_decision_generic_operation` |
| Facilities and joint laboratory | `GFX_decision_generic_construction` |
| Directorate dynamic modifiers | `GFX_idea_generic_research_bonus` |

Both result events use the dedicated `GFX_report_event_016_brilliant_scientist_directorate_dossier` sprite registered in `interface/016_brilliant_scientist.gfx`. Its final asset lives at `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_directorate_dossier.dds`; source, decoded, contact-sheet, and manifest records belong under `docs/assets/016_brilliant_scientist/`. The image contract is a sealed counterintelligence dossier, laboratory floor plan, and convoy route rather than another Kruger portrait.

## Source references

Implementation was checked against the offline wiki snapshot pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI Modding. The official vanilla `documentation` folder and `common/decisions/_documentation.md` were treated as the primary engine reference. Vanilla targeted state decisions, Soviet Academy decision-category art, generic decision sprites, and dynamic-modifier examples provided concrete precedents.

## Future plans and suggestions

- Replace generic sprites with a coordinated bespoke Directorate icon family only after the asset manifest and stable sprite IDs are approved.
- Give the richer scripted Directorate window its own bounded implementation tranche; ordinary decisions must remain the gameplay authority and AI entry point.
- Add family-specific warnings to the project cards once all fifteen native families expose stable status contracts.
- Connect foreign-framework invalidation to the shared Event 016 cleanup effect so partner defeat, host transfer, and terminal branches cannot retain stale global targets.
- Use Event 016 incidents to surface hidden Independent Capacity and Grievance consequences without exposing exact values.
- Revisit institutional and security weights after the native family burdens and accident frequencies are final, since those systems determine the real value of capacity, secrecy, and replication.
