# Event 011 Secret Alliance implementation improvement addendum

Status: accepted and resolved design-fidelity pass.

`011_secret_alliance_improvement_resolution.md` records the implementation disposition of tranches A-G. That resolution closes this addendum as a planning item and does not make an Event 011 completion claim. The clean decision and mission freeze at `b7965b7e` and the clean localisation freeze at `087d66ab` record their audited states. Gameplay candidate `c4bb10ce` postdates those freezes with later commitment and operation-dossier causality, and its final completion audit is still running.

Date: 2026-07-10.

This addendum is a planning handoff. It does not edit gameplay, assets, localisation, spreadsheets, or the Event 011 source specification.

## Loop decision

Event 011 does not need another broad expansion. The five-part source specification still has enough routes, decisions, achievements, scenario variants, visual direction, and wartime outcomes. The current implementation needs a bounded causal-depth tranche before completion can be considered.

The tranche should make the implemented parts affect one another. Member motives should shape operations. Operations should create specific clues and attack specific preparedness layers. Counterplay should change later operations and recruitment. Hidden commitments should become public faction goals. Coalition Resolve should react to real war and member facts. These connections are accepted must-fix work because the source specification and the scripted-system architecture already require them.

No new country tags, focus trees, formables, world-end branches, achievement families, major GUI windows, or animation families are accepted by this pass.

## Implemented foundations to preserve

The following implementation work already has the right basic shape and should remain stable while the deeper loop is added.

| Foundation | Current identifiers | Preserve |
| --- | --- | --- |
| Fixed target and one active context | `secret_alliance_target`, `secret_alliance_active`, `secret_alliance_prepare_random_event_fire` | The pact never retargets after firing |
| Three-minor automatic opening | `secret_alliance_select_weighted_minor_member`, `secret_alliance_event.normal_founders` | Exactly three distinct valid AI minor founders before the entry event |
| Real reveal faction | `faction_template_secret_alliance_anti_target_pact`, `secret_alliance_create_public_faction` | A true faction of existing countries, with no replacement tag |
| Hostile-war convergence | `on_war_relation_added`, `secret_alliance_handle_war_relation_added`, `secret_alliance_reveal_pact` | Immediate public reveal and immediate entry of every remaining valid active member into the existing target war |
| Counter-network breadth | `secret_alliance_foreign_interference`, `secret_alliance_coalition_crisis` and the existing decision families | Investigation, protection, diplomacy, deception, border action, emergency action, and revealed-war action all remain represented |
| Limited border conflict boundary | `secret_alliance_start_dynamic_border_conflict` and resolution helpers | A border conflict stays below normal war until an explicit escalation creates normal hostility |
| Reveal conversion | `secret_alliance_convert_hidden_values_to_war_state` | Evidence and Preparedness continue to matter after reveal |
| Triggerable scenario identity | the five scenario types and four intensity settings | The scenario remains an immediate public faction and war path |
| Achievement set | the six `011_secret_alliance_*` achievement IDs | No new achievements and no renaming without a registry conflict |

The improvement tranche should extend these foundations. It should not replace them with a second system.

## Current depth gaps and evidence

| Gap | Current implementation evidence | Player-facing consequence |
| --- | --- | --- |
| Motives are weak labels | `secret_alliance_assign_current_member_motive` begins with a generic random list. Geography can overwrite fear and a major ideological difference can overwrite ideology. Motives rarely affect selection, operations, recruitment, or reveal behavior | Arbitrary countries feel interchangeable after selection |
| Doctrine does not direct the pact | `secret_alliance_determine_doctrine` counts motive labels. `secret_alliance_launch_weighted_operation` then uses the same fixed random list regardless of doctrine, actor, geography, or target vulnerability | Containment, punitive, regime-pressure, and spoils pacts play almost the same |
| The pulse stacks unrelated developments | `secret_alliance_run_concealed_pulse` can recruit, trigger a dispute, leak, defect, and launch an operation during one fixed 45-day pulse | Events can feel like disconnected random rolls instead of one developing network |
| Operations have no responsible member | The six report events store only `global.secret_alliance_recent_operation_family`. No operation actor, theater, target state, evidence class, or preparation layer is saved | The player cannot connect a method to a suspect or understand why counterplay worked |
| Evidence is farmable and one-dimensional | `secret_alliance_apply_operation_minor_success`, `secret_alliance_apply_operation_major_success`, and `secret_alliance_apply_operation_disrupted` all add global Evidence. `secret_alliance_select_true_member_clue` applies a repeated confidence gain with no class or source memory | Repeating generic incidents can build a complete case without corroboration |
| Suspect presentation is unbounded | `secret_alliance_select_suspect` uses `global.secret_alliance_suspects` directly. The category files provide a picture but no attached compact scripted GUI | The accepted three-card confidence interface is absent and country lists can grow without curation |
| Preparedness is permanent click accumulation | Protection effects add directly to `global.secret_alliance_preparedness`, set permanent project flags, and reuse `secret_alliance_hardened_networks`. There are no maintained component durations or expiry effects | The player can buy a permanent maximum and the protected surface does not matter |
| Decision caps do not govern most families | `secret_alliance_active_protections`, `secret_alliance_active_diplomacy`, `secret_alliance_active_offensive`, and `secret_alliance_active_emergency` are initialised and checked, but the current action effects do not consistently increment or release them | The category has the shape of a capped campaign but behaves like a large action store |
| Evolutions fill rosters and values immediately | `secret_alliance_open_evolution_i`, `_ii`, and `_iii` raise value floors and fill toward minimum member counts inside the transition effect | Recruitment refusal, sponsor courtship, leaks, and player disruption have little room to matter during escalation |
| The public faction is generic | `faction_template_secret_alliance_anti_target_pact` uses generic regional expansion and enemy-defeat goals and generic rules | Reveal changes diplomacy, but it does not expose the pact's private doctrine or member obligations |
| Coalition Resolve has little war context | `secret_alliance_update_revealed_war` mostly checks target capitulation, first-major capitulation, starting-capital control, and a fixed monthly decrease | Front success, losses, role failure, theater access, conflicting promises, and leadership rivalry do not drive cohesion |
| AI posture is broad and static | `common/ai_strategy/011_secret_alliance.txt` mainly changes army building and war avoidance. Decision AI uses simple base factors | Maritime members, distant members, fear members, sponsors, and opportunists lack distinct plans |
| Scenario types are mainly selection weights | Type affects candidate weighting and the unlikely coalition receives a Cohesion reduction. Composition gates, role packages, doctrine, and war behavior remain mostly shared | The five scenario types do not create five distinct challenges |

## The stronger causal loop

Use one loop across the hidden and public phases.

1. The standing conference chooses an agenda from doctrine, member promises, strategic access, and recent outcomes.
2. One member becomes the operation actor because its role and geography fit the agenda.
3. The operation selects one target surface, one preparation layer, one evidence class, and one risk band.
4. The player sees the physical consequence and chooses whether to investigate, protect, deceive, negotiate, or accept the loss.
5. Resolution changes the exact readiness layer, preparedness component, clue class, suspect confidence, member commitment, and next-operation weights involved.
6. Recruitment, sponsor entry, disputes, and leaks arise from those results instead of rolling beside them without context.
7. Reveal converts the saved commitments and preparation layers into public faction goals, member roles, opening strengths, and fracture points.
8. Wartime results update Resolve through the same promises, roles, and known weaknesses.

This loop uses existing values and decision families. It adds missing relationships and state ownership.

## Must-fix tranche A: standing conference, member roles, and private commitments

`Standing conference` is a working system label and is not final localisation.

Each active member needs four durable facts:

- primary motive
- commitment band
- operational role
- one private commitment or promised benefit when its motive needs one

Use internal role values with these meanings:

| Role | Valid profile | Mechanical responsibility | Failure pressure |
| --- | --- | --- | --- |
| Liaison coordinator | founder with reliable access and diplomatic reach | conference timing, recruitment contacts, common procedure | a captured route raises Evidence and delays the next agenda |
| Intelligence node | state with intelligence capacity or useful access | plans, ciphers, technical delegations, human sources | compromised node feeds suspect confidence and false-plan access |
| Logistics host | state with useful ports, railways, air access, or depots | access, stockpiles, equipment routes, distant-member support | exposed depots and closed routes reduce a real Readiness layer |
| Border arm | neighbor or state with a credible land approach | surveys, border pressure, limited conflict, local offensive plan | failed border action raises grievance or invites withdrawal |
| Political arm | ideological or regime-survival member | front groups, propaganda, political pressure, recruitment narrative | exposed finance and false claims damage the public case |
| Major sponsor | strategically valid major | leadership, arms, intelligence coordination, second-theater support | battlefield distraction or exposure can force a leadership dispute |

A country can hold one primary role and one support capability. Distant and maritime countries should gain support roles instead of receiving implausible land-front behavior.

Private commitments should make the motive concrete.

| Motive | Commitment direction | Expected counterplay | Reveal or war weakness |
| --- | --- | --- | --- |
| Fear | verifiable restraint, border security, or protection against the target | credible guarantee, noninterference, defensive consultation | can accept containment terms or refuse an offensive mission |
| Grievance | settlement of an actual claim, border issue, or recent loss | specific arbitration or concession route | rejects unrelated settlements and fractures over unmet terms |
| Ideology | pressure on the target government or support for a political alternative | exposure of political methods and defense of domestic institutions | difficult to buy off, vulnerable to incompatible successor plans |
| Patronage | aid, access, guarantee, or sponsor protection | expose sponsor coercion or break the aid route | commitment falls when sponsor support fails |
| Opportunism | expected territory, access, status, or postwar gain | reveal conflicting promises and raise expected war cost | seeks delay or separate terms when victory stops looking cheap |
| Regime survival | target noninterference and protection against internal opponents | narrow security assurance and source protection | reacts sharply to exposed fabrication or sponsor meddling |

Member disputes must name two incompatible commitments internally and save the participants. `secret_alliance_maybe_run_internal_dispute` should no longer be only a generic Cohesion loss. A dispute should change an agenda, promise, role, recruitment attempt, or later settlement condition.

The historical anchors already accepted in the source pack provide the structure:

- the Anti-Comintern agreement supports a standing committee, intelligence exchange, and invitations to further states
- secret protocols support private commitments and overlapping expectations
- linked theaters under a major sponsor support role-based geography

These are structural inspirations. They do not impose a fixed ideology or copy historical treaty terms.

### Main implementation surfaces

- `common/script_constants/011_secret_alliance_constants.txt`
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- internal dispute and recruitment events in `events/011_secret_alliance.txt`
- final member-motive and revealed-member localisation after gameplay is stable

## Must-fix tranche B: operation dossiers and adaptive pacing

Replace the current six incident tokens with the six accepted design families:

1. diplomatic isolation
2. intelligence penetration
3. industrial and transport sabotage
4. political and social pressure
5. military preparation
6. recruitment

Existing report images and event IDs can be reused where their scene still fits. The family state must use the accepted conceptual families rather than equating a courier, a safehouse, and a political attack with complete operation families.

Every substantial operation should save this compact dossier:

- operation actor as a regular event target
- operation family
- target surface or named state when geography matters
- readiness layer being built
- evidence class that a failure can expose
- current risk band
- recovery and recent-family state

Operation selection should use doctrine, actor role, actor motive, target geography, target vulnerability, prior success, same-family recency, pact Alertness, and current Preparedness components. One substantial operation remains active at a time.

Use a target-owned delayed event with a dynamic MTTH value. Create `common/mtth/011_secret_alliance_mtth.txt` as specified by the architecture pass. The fixed 45-day constant can remain a tuning anchor, but it cannot be the complete cadence.

### Operation outcome contract

| Outcome | Pact result | Target result | Follow-up |
| --- | --- | --- | --- |
| Pact full success | increases the named Readiness layer and actor commitment | damages or tests the matching Preparedness component | repeat family is penalized and severe recovery applies where relevant |
| Partial or ambiguous result | smaller Readiness gain with a physical trace | registers a specific clue class or creates a plausible suspect | player can investigate the trace or protect the attacked surface |
| Target disruption | reduces the named Readiness layer and raises pact Alertness | registers a strong clue and may expose the actor's role | pact adapts toward cleanup, false traffic, or a different family |
| Target deception | preserves a channel and stores false-plan quality | delays the next plan or misdirects one family | concrete wartime consequence only if the channel survives |

A pact success should not automatically grant global Evidence. Evidence appears when the operation leaves a usable trace. A player disruption should not always produce the same global value package.

Early sabotage should follow the accepted OSS-inspired low-visibility structure. Repeated methods become recognizable through evidence classes. Severe destruction and political violence remain rare Evolution II content with longer recovery and protected-target checks.

### Main implementation surfaces

- `secret_alliance_run_concealed_pulse`
- `secret_alliance_launch_weighted_operation`
- `secret_alliance_apply_operation_minor_success`
- `secret_alliance_apply_operation_major_success`
- `secret_alliance_apply_operation_disrupted`
- `chaosx.nr11.6` through `chaosx.nr11.16`
- the new Event 011 MTTH file

## Must-fix tranche C: evidence classes, corroboration, and suspect curation

Implement the six evidence classes from the tuning model and architecture pass:

- method
- communications
- financial
- diplomatic
- military
- human

Each clue needs a class and a source identity. The exact same class and source pair awards no repeat Evidence. A new source inside a known class provides a reduced amount. The first independent class on a suspect provides a normal amount. Corroboration across classes provides the strongest gain.

Global Evidence represents the strength of the overall case. Suspect confidence represents the strength of the case against one country. A high global value must not confirm a country by itself.

Public coalition actions require both overall case strength and corroboration. Store minimum independent-class counts for partial dossier, member naming, coalition case, and complete-network achievement in script constants. The player should be unable to reach the complete-network state by repeating courier or sabotage actions.

False leads need source memory. The player can disprove a false lead through a relevant investigation, clear the suspect, and recover some credibility. Repeated public accusations without new independent evidence escalate diplomatic and recruitment consequences.

Maintain an internal suspect array for AI and history. Rebuild a separate `global.secret_alliance_visible_suspects` array with at most three countries, ordered by confidence and recency. The human selector and compact panel use the visible array. AI evaluates the full array directly.

Wire the accepted compact scripted GUI to the decision category. It should display Evidence and Preparedness bands, three suspect cards, recent operation state, active objectives, and War Pressure when Evolution III makes it public. It must not display hidden member count, exact Cohesion, exact Readiness, motives, or unconfirmed names.

### Achievement protection

- `011_secret_alliance_every_thread` must use the reveal membership snapshot, independent evidence coverage, and no innocent public naming
- `011_secret_alliance_the_empty_chair` must still require a true founder and restraint
- public-case actions must not create a cheap path to either achievement

### Main implementation surfaces

- evidence and suspect helpers in `common/scripted_effects/011_secret_alliance_effects.txt`
- confidence and public-case triggers in `common/scripted_triggers/011_secret_alliance_triggers.txt`
- selector decisions in `common/decisions/011_secret_alliance_decisions.txt`
- `common/decisions/categories/011_secret_alliance_categories.txt`
- the Event 011 scripted GUI, interface, GFX, and scripted localisation surfaces already mapped by the source pack

## Must-fix tranche D: maintained Preparedness and real objectives

Preparedness should be recalculated from the seven accepted components:

- staff security
- industrial security
- transport security
- border readiness
- continuity
- allied coordination
- known plans

Protection decisions activate maintained projects. Each project needs duration, continuing burden, expiry behavior, component cap, and an attacked surface it can actually protect. Repeating one project cannot permanently fill the global meter.

The protection families should differ in play:

| Project family | Required commitment | Maintained benefit | Opportunity cost |
| --- | --- | --- | --- |
| Staff compartmentalisation | command capacity and army experience | protects plans and reduces penetration | temporary planning or coordination burden |
| Cipher and courier rotation | support equipment plus trains or convoys | protects communications evidence and false-plan channels | transport and command disruption |
| Industrial choke-point security | equipment, factory burden, and a selected industrial region | reduces sabotage on that region | production and local unit burden |
| Stockpile dispersal | trucks, trains, fuel, and selected logistics region | protects equipment and depot layers | continuing supply inefficiency |
| Cabinet protection | manpower and stability tolerance | reduces political attack risk | visible security and legitimacy burden |
| Border communications | supplied units in selected border states plus equipment | resists surveys and improves limited conflict | divisions are tied to the named front |
| Port and airfield protection | fuel, convoys, service experience, and coastal or airbase state | blocks maritime or air access operations | weakens other missions |
| Continuity sites | construction capacity, trains, and command capacity | reduces opening command shock | one-time expensive project with current economic burden |

The category caps must become real. Increment the matching family when a maintained project or mission begins. Decrement it exactly once on success, timeout, cancellation, invalid target, reveal conversion, or cleanup. The architecture pass already defines the idempotent mission pattern.

`secret_alliance_hardened_networks` should represent the current maintained network state or a staged conversion. It should not act as a permanent reward attached to every protection click.

## Must-fix tranche E: evolution escalation with player interruption

Evolution transitions should unlock capability and create a pressured development. They should not instantly fill every minimum roster and value band.

### Evolution I

- Preserve exactly three founders.
- Open the expanded minor recruitment pool and schedule an accelerated invitation.
- A successful invitation, refusal, leak, or conditional acceptance becomes part of the event history.
- The pact can remain below the typical member band when recruitment repeatedly fails.

### Evolution II

- Evaluate one strategically valid major through a sponsor approach.
- Sponsor acceptance requires reach, a useful theater, resources, and a reason to oppose the target.
- Sponsor refusal can create a leak, minor-led continuation, or Cohesion dispute.
- The response category opens through a serious coordinated incident after the sponsor or network reaches the accepted threshold.
- Do not fill the pact to six members inside the evolution effect.

### Evolution III

- Evaluate a second major only after the first sponsor, member roles, and theater access support it.
- Expose War Pressure and begin a dynamic public crisis window.
- Player Evidence, Preparedness, sponsor exposure, low Cohesion, and a preserved turned channel must be able to delay, fracture, or weaken the reveal.
- A pre-fire Evolution III opening starts through the Evolution II package and provides at least one meaningful counter-network response before public reveal.

Use the same enable checks and evolution log contract already documented by the architecture pass. Disabled evolutions cannot set applied flags or consume later progression.

## Must-fix tranche F: public faction goals, roles, and Resolve

The reveal should make the pact's private purpose visible through event-specific faction behavior.

Create Event 011-owned faction goals and, where needed, Event 011-owned rules or rule groups. The current generic regional expansion and enemy-defeat goals do not express doctrine, member obligations, or the target-specific campaign.

Working goal roles, not final localisation:

| Doctrine | Public goal role | Member task | Main fracture condition |
| --- | --- | --- | --- |
| Containment | enforce a limited security settlement and stop further target expansion | defend approaches, maintain guarantees, hold access routes | offensive escalation or a credible target settlement |
| Punitive | execute a bounded coalition offensive and impose military terms | open reachable fronts and maintain depots | casualties, failed offensive, and incompatible territorial demands |
| Regime pressure | coordinate political and military pressure against the target government | political operations, intelligence support, selective military pressure | disagreement over the acceptable successor or settlement |
| Spoils | pursue promised gains under sponsor leadership | capture or hold the member's credible promised objective | conflicting promises, sponsor favoritism, and high war burden |

Do not add a bespoke peace-conference replacement. Doctrine goals influence Resolve, separate terms, faction continuation, and event outcomes through the existing war.

Member roles should change wartime contribution:

- border arms receive local-front priorities
- logistics hosts maintain supply and equipment routes
- maritime members emphasize naval, air, convoy, and expeditionary support
- distant members avoid useless land deployment
- intelligence nodes preserve known-plan or deception effects
- the sponsor coordinates theaters and becomes the center of leadership risk

Coalition Resolve should update from named components:

- objective progress and failed offensives
- member casualties and war burden
- member or sponsor capital loss
- sponsor aid and sponsor distraction
- accessible front and route survival
- public proof of conflicting promises
- separate terms and event-owned defections
- two-major leadership rivalry
- target concessions that answer a real motive

The current automatic monthly decrease for target control of its starting capital should be replaced by event facts that represent failure or stalemate. Capital control remains an achievement and survival fact, not the sole recurring measure of coalition morale.

### Two-major leadership crisis

When two majors are present, save their preferred theater and doctrine pressure. A leadership dispute should occur after a failed objective, sponsor exposure, or an unequal war burden. The target can exploit the dispute through the existing public-evidence and separate-terms families. The dispute can reduce coordination, change leader, split responsibilities, or create a partial fracture. It does not automatically dissolve the faction.

### Postwar continuation

The continued regional bloc outcome requires a positive reason. It is valid only when the surviving membership, leader, doctrine, relations, and completed security goal support it. The faction then receives a postwar security manifest and loses Event 011 anti-target war priorities. Other outcomes dismantle the Event 011 faction after recording the settlement.

The current default route that leaves a regional bloc through an otherwise unqualified target victory is not sufficient.

### Main implementation surfaces

- `common/factions/templates/011_secret_alliance.txt`
- new Event 011 files under `common/factions/goals/`, `common/factions/rules/`, and `common/factions/rules/groups/` as mapped by the architecture pass
- reveal, war update, fracture, settlement, and cleanup effects
- target and member decision categories after reveal
- event-specific AI strategies

## Must-fix tranche G: AI, scenario identity, and achievement fidelity

### AI

Implement the accepted AI matrix as behavior, not only broad army-building posture.

- Founder and recruit AI must use motive, target behavior, access, current wars, faction obligations, stability, equipment, and sponsor support.
- Operation AI must prefer the family which matches actor role and target vulnerability.
- Pact AI must react to Evidence by cleaning routes, planting false traffic, protecting exposed members, or accelerating reveal.
- Pact AI must react to Preparedness by changing theater or method.
- Target AI must evaluate the full suspect array, call the same costs and outcomes as the player, and avoid human-only selector dependence.
- Wartime AI must allocate border, maritime, distant, logistics, and sponsor roles separately.
- Opportunists and fear members should become earlier fracture candidates. Ideological members and healthy sponsors should resist generic buyout logic.

Static AI strategy blocks can retain general posture. Dynamic target-specific and role-specific strategy effects should own the arbitrary target and current role.

### Scenario differentiation

The five scenario types need distinct validity, composition, roles, and doctrine:

| Type | Required identity beyond weighting |
| --- | --- |
| Regional ring | reachable neighboring or regional members, multiple credible approaches, border and logistics roles |
| Ideological front | real ideological opposition and compatible political-arm roles, with regime-pressure doctrine unless composition strongly contradicts it |
| Great-power sponsor | one strategically valid major first, then minor partners which provide reach, access, or another theater |
| Unlikely coalition | deliberate motive and ideology diversity, lower starting Cohesion, stronger promise conflicts, and higher fracture reserve |
| Random coalition | safe weighted composition followed by doctrine and role assignment from the selected members |

Intensity controls composition bands, opening Readiness, Resolve, material support, and risk tolerance. Type-specific minimums must be checked before launch. Insufficient composition blocks launch with a clear reason. Invalid or involuntary human countries cannot be substituted.

Human candidates require explicit join, refuse, leak, or expose outcomes during normal recruitment. Scenario composition which includes humans waits for consent before faction or war creation. No timeout counts as acceptance.

### Achievement fidelity

Keep the six registered achievements. Strengthen their underlying proof:

- complete-network proof uses independent evidence classes and the active reveal snapshot
- turned-source proof requires a preserved channel and a concrete wartime result
- fracture-exit proof counts only Event 011 withdrawal, refusal, or separate-terms outcomes
- Maximum scenario proof uses immutable type, intensity, achieved composition, consent, capital, and independence facts
- two-major proof freezes major status and starting-capital state at the accepted checkpoints

The achievement conditions should remain difficult because the mechanics require mastery. They should not depend on repeatable Evidence or permanent Preparedness farming.

## Mandatory architecture compliance carried into this pass

The scripted-system architecture pass remains authoritative for engine-safe ownership. These are accepted implementation corrections rather than new design proposals:

- add `has_civil_war = no` and safe faction-withdrawal conditions to founder, recruit, and sponsor validity
- replace continuously evaluated `any_country` checks in decision and AI gates with member arrays and maintained counts
- use stored dynamic costs in availability and payment instead of hardcoded thresholds which can disagree
- rebuild member arrays from survivors instead of only clearing flags inside the live array
- use the separate founder, visible-suspect, confirmed-member, and turned-member registries defined by the architecture pass
- add narrow faction join or leave, target invalidation, and relevant postwar hooks where current on-actions do not cover state changes
- preserve the reveal recursion guard across every `add_to_war` call and validate that each member joined the anchor's existing target war
- use explicit dynamic faction-name fallback logic
- keep history and achievement facts separate from runtime cleanup

## Optional future ideas

These ideas are useful only after every must-fix tranche is implemented, audited, and folded into the source specification where accepted.

1. Add country-specific incident variants for famous rivalries when a stable target and member pair merits bespoke historical flavor.
2. Add narrow Event 052, Event 147, and Event 150 hooks after those events expose stable public helper contracts.
3. Expand a surviving postwar security bloc into longer diplomatic content if future faction work gives that outcome enough campaign value.

None of these optional ideas blocks Event 011 completion. They must not be used to delay the accepted causal-depth work.

## Explicit anti-bloat boundary

- Keep the existing six achievements.
- Keep one compact category-attached mechanic GUI.
- Keep the single Evolution III warning animation family.
- Keep existing countries and their focus trees.
- Keep the event outside a cluster.
- Keep one reveal super-event.
- Do not add a world-end outcome.
- Do not add real-world sabotage instructions.
- Do not add a separate visible loyalty meter for every member. Internal commitment bands are sufficient.
- Do not add more decisions until the current accepted decisions have distinct clues, surfaces, costs, risks, and outcomes.

## Completion acceptance scenarios for this addendum

The main implementation agent should treat these as task-specific proof for the accepted improvement tranche.

1. Two pacts with different founder motives and geography produce different roles, agendas, and operation weights.
2. The same clue class and source cannot be farmed. Independent classes create visible corroboration and unlock stronger actions.
3. An innocent false lead can be cleared, while repeated unsupported public accusations worsen recruitment and credibility.
4. Only three suspects appear in the human panel, while AI can still evaluate the full internal suspect set.
5. A maintained protection project expires or is cancelled and its Preparedness component falls without corrupting unrelated components.
6. An industrial operation attacks industrial security, a courier operation attacks staff or communications security, and a border survey attacks border readiness.
7. One substantial operation runs at a time. Recent-family and severe-recovery state prevents repetition.
8. Evolution I opens recruitment without guaranteeing an immediate fourth member.
9. Evolution II sponsor refusal, leak, and acceptance each produce a distinct continuation.
10. Evolution III provides a meaningful response window whose duration reacts to event values.
11. A containment faction, a punitive faction, a regime-pressure faction, and a spoils faction select different goals and fracture conditions.
12. Maritime and distant members contribute through appropriate roles instead of receiving the same land-war posture.
13. A two-major coalition can suffer a leadership dispute without automatically collapsing.
14. Coalition Resolve reacts to actual objective, loss, access, sponsor, promise, and withdrawal facts.
15. Every scenario type passes a distinct composition and behavior check at each intensity.
16. A human candidate is never registered, added to the faction, or called to war without explicit consent.
17. The six achievement positive paths remain possible after anti-farming and maintained-project changes.

## Promotion and disposition

The accepted must-fix sections should be implemented in the current Event 011 tranche. After implementation, fold any source-design clarification into `docs/specs/011_secret_alliance_specs/` or record a precise rejection reason before completion. Do not leave this accepted addendum unresolved.

Optional future ideas remain queued in this file and are not part of the completion gate.
