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

Independent Capacity and Grievance remain hidden. Decisions alter them through the shared measure helpers, while their consequences are communicated through requirements, incidents, control-state triggers, and player-facing warnings elsewhere in Event 016.

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

## Deferred outcome adapter contracts

The Directorate owns bounded context producers, while the shared Event 016 event/effect layer owns narrative outcomes. Neither producer polls the world on a recurring on-action.

### Loyalty review

When `brilliant_scientist_loyalty_review_mission` expires, the host receives `brilliant_scientist_directorate_loyalty_review_requested`. The mission snapshots Mandate, Dependence, Exposure, Independent Capacity, Grievance, the Prototype/Deployment/Weaponization counts, and a four-step intelligence score assembled from agency presence, a mature agency, any operative, and a multi-operative team. It also records boolean history flags for cloning, robotics, paleogenetics, xenobiological synthesis, and singularity projects.

The parent resolver must be a country-scope scripted effect named `brilliant_scientist_resolve_directorate_loyalty_review_request`. Once that effect exists, call it directly at the end of the mission's `timeout_effect`:

```txt
brilliant_scientist_resolve_directorate_loyalty_review_request = yes
```

The resolver must require the request flag, weight rather than guarantee its result, and use the captured intelligence score, Exposure, hidden pressure, and project-history context. Its valid result families are a foreign-agent finding, a Kruger-loyalist finding, a project-gated transformed-personnel finding, an inconclusive review, or a wrongful purge that raises Grievance. It must clear the request flag, intelligence/history flags, and all loyalty snapshot variables after one outcome. It must not grant a capturable operative or a deterministic Exposure reduction on every use.

### Primary relocation

After the transfer timer, the host receives `brilliant_scientist_directorate_relocation_requested`. `event_target:brilliant_scientist_relocation_requested_origin` and `_destination` persist the two states. Route flags preserve whether land or sea logistics were paid. The host also snapshots Mandate, Exposure, Dependence, Project Capacity, Independent Capacity, Grievance, project-stage counts, and whether the plan was made under fire.

The parent resolver must be a country-scope scripted effect named `brilliant_scientist_resolve_directorate_relocation_request`. Once that effect exists, call it directly after the request context is written:

```txt
brilliant_scientist_resolve_directorate_relocation_request = yes
```

The resolver must validate both global state targets again, then weight successful transfer, interception, prototype loss, staff refusal, and escape opportunities from the stored context. Success clears the primary-facility state flag and `brilliant_scientist_facility_type` variable at the origin, sets both at the destination, replaces `event_target:brilliant_scientist_primary_facility`, and grants no buildings, slots, facilities, prototypes, project stages, or equipment. Every terminal outcome clears the request flag, route/under-fire flags, request targets, and snapshot variables. An invalid target must resolve as interruption or failure, never as unconditional success.

These two resolver effects are parent-owned and are not defined or called by this bounded Directorate tranche. Until the parent wires them, requests remain pending by design and a whole-Event-016 completion claim is blocked.

## Foreign liaison lifecycle

Foreign actions use the shared Event 016 actor-selection helpers. `Review Foreign Approaches` is an explicit player or AI decision: its one-time completion effect refreshes valid foreign interest, selects one bounded actor target, and then all follow-up decisions operate only on that actor. There is no daily, weekly, or monthly world scan.

The host may:

- offer one controlled research-access package;
- open a persistent joint laboratory at a viable partner-owned site;
- accept a persistent foreign protection framework;
- restrict the currently selected actor's access;
- terminate standing controlled access, joint-laboratory, and protection frameworks.

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

Player-facing strings are in `localisation/english/016_brilliant_scientist_directorate_l_english.yml`. Every decision, mission, custom result tooltip, persistent dynamic modifier, and the four-value category header is localized there.

This tranche requires no new raster asset. It deliberately uses verified existing vanilla sprite identifiers:

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

Because all required sprites already exist, this tranche adds no DDS files and no `.gfx` registration. It does not edit `interface/016_brilliant_scientist.gfx`. If bespoke Directorate art is later commissioned, stable replacements should use `GFX_decision_brilliant_scientist_directorate_institution`, `_facility`, `_security`, `_foreign_liaison`, and `_project_board`; source/final files should live under `docs/assets/016_brilliant_scientist/` and `gfx/interface/decisions/016_brilliant_scientist/`, with registrations in a distinct `interface/016_brilliant_scientist_directorate.gfx` handoff so existing Event 016 registrations remain untouched.

## Source references

Implementation was checked against the offline wiki snapshot pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, and Scripted GUI Modding. The official vanilla `documentation` folder and `common/decisions/_documentation.md` were treated as the primary engine reference. Vanilla targeted state decisions, Soviet Academy decision-category art, generic decision sprites, and dynamic-modifier examples provided concrete precedents.

## Future plans and suggestions

- Replace generic sprites with a coordinated bespoke Directorate icon family only after the asset manifest and stable sprite IDs are approved.
- Give the richer scripted Directorate window its own bounded implementation tranche; ordinary decisions must remain the gameplay authority and AI entry point.
- Add family-specific warnings to the project cards once all fifteen native families expose stable status contracts.
- Connect foreign-framework invalidation to the shared Event 016 cleanup effect so partner defeat, host transfer, and terminal branches cannot retain stale global targets.
- Implement and directly wire the two parent-owned outcome resolvers documented above; do not replace them with periodic request polling.
- Use Event 016 incidents to surface hidden Independent Capacity and Grievance consequences without exposing exact values.
- Revisit institutional and security weights after the native family burdens and accident frequencies are final, since those systems determine the real value of capacity, secrecy, and replication.
