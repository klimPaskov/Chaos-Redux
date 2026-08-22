# Event 013 pre-improvement accepted-spec gap inventory

> **Historical snapshot — superseded by the implemented Event 013 source package and the final audit.** This document records the gaps observed before the improvement tranche; its findings are not current claims of missing implementation. Use `docs/plans/013_natural_disasters_plans/013_event_completion_final_audit.md` and the dated re-audit handoffs for current status.

Date: 2026-07-11
Mode: read-only implementation/specification audit
Gameplay, GUI, localisation, asset, workbook, and source-spec edits by this subagent: none
Only repository output: this handoff

## Scope and exclusions

This inventory compares the accepted Event 013 source package and readiness gates against the live gameplay, GUI, localisation, documentation, asset, event-log, cluster, scenario, achievement, and workbook surfaces.

The physical-geography correction, public-call output correction, and decision-category picture selector are already owned by `2026-07-11_event013_dynamic_geography_api_architecture_handoff.md` and the parent implementation tranche. They are dependencies below, not duplicated findings. Super-event audio uniqueness is also excluded because the parent has completed that work.

Severity used here:

- **P0**: the live mechanic reverses or invalidates a core accepted contract.
- **P1**: an accepted player-facing or systemic surface is missing, materially shallow, disconnected, mislabeled, or not sufficiently validated for completion.
- **P2**: bounded integration debt, cleanup debt, documentation debt, or a design/pacing question that should be closed before final completion.

## Executive verdict

The strongest defect is causal: the preparation chosen by the player determines which physical or socioeconomic follow-up hazard is created. A port withdrawal can cause a tsunami; clean-water preparation can cause disease. The accepted design instead makes preparation protect against independently resolved physical risks.

Beyond that P0, the implementation still compresses substantial accepted family identity into shared warning-cost helpers, nine generic follow-up classes, one shared state modifier, static family report prose, and an abnormal urgency ledger presented as a physical path map. Cluster 5 also labels five logical evolution roles but does not preserve those roles through dispatch. Existing static audits demonstrate a broad implementation, but they do not close the accepted runtime matrix.

Priority counts from this pass:

- 1 P0 core causal defect.
- 10 P1 accepted-surface gaps or completion blockers.
- 3 P2 cleanup/integration/pacing findings.

## P0 accepted-contract defect

### P0-01 — preparation choices select the follow-up hazard instead of mitigating one

**Accepted contract**

- Part 2 describes warnings as family-specific preparations that reduce deaths, building loss, and aftermath difficulty, and says the player chooses which loss to reduce: `docs/specs/013_natural_disasters_specs/specs/013_natural_disasters_spec_part_2_reusable_system.md:47-81`.
- Part 2 resolves family-specific chains after impact and makes them visible/preventable in aftermath: `:164-179`.
- Part 8's family mini-specs describe protective actions against physical risks. Examples include ashfall air-traffic grounding at `:987-991`, lahar bridge cordons at `:1046-1050`, storm-surge quay closure at `:1165-1169`, and whole-earth rupture coastal watch at `:1343-1347`.

**Live evidence**

- `natural_disaster_prepare_warning_route_profile` writes `natural_disaster_warning_secondary_chain` and `natural_disaster_warning_tertiary_chain` for every family: `common/scripted_effects/013_natural_disasters_effects.txt:2813-2992`.
- `natural_disaster_resolve_chain_risk` then selects those chains specifically because the player chose the secondary or tertiary preparation: `:3572-3593`.
- Earthquake maps secondary preparation to supply collapse and tertiary preparation to tsunami: `:2820-2823`. Thus choosing the tertiary coast/port preparation creates the tsunami route.
- Flood maps secondary preparation to supply collapse and tertiary clean-water preparation to disease: `:2827-2830`. Thus choosing the clean-water preparation creates the disease route.
- The later severity/coast/default-chain resolution only runs after those choice-driven branches: `:3594-3628`.

**Consequence**

The UI presents preparation as protection while the implementation uses it as hazard generation. This reverses causality, misleads player choice, distorts AI choice value, and prevents honest report/aftermath wording.

**Minimal implementation route**

1. Resolve the candidate follow-up route from family, severity, geography, sequence origin, and existing recovery state without consulting the warning choice.
2. Persist a separate protected-system or protected-route token from the warning action.
3. Apply matching protection only to candidate probability, lead time, death/damage multipliers, mission difficulty, or partial outcome.
4. Let a mismatched preparation protect its advertised system without replacing the physical hazard.
5. Integrate with the parent's physical chain-target resolver so an impossible tsunami/lahar/wildfire target is skipped rather than substituted.

Completion proof needs at least earthquake/tsunami, flood/disease, volcano/lahar, wildfire spread, drought/famine, and rupture/coastal-chain traces showing that changing preparation does not change the candidate hazard identity.

## P1 accepted-surface gaps

### P1-01 — accepted family follow-up identity is collapsed into nine generic chain enums

**Accepted contract**

Part 8 defines many family/context routes beyond the seven playable prevention mission classes. Representative accepted routes include:

- seismic landslide and urban fire: `013_natural_disasters_spec_part_8_deep_family_minispecs.md:84-86`;
- dam-failure flash: `:146`;
- inland flood: `:204`;
- transport collapse: `:265` and `:1329`;
- airfield accident and thunderstorm return: `:441-442`;
- shelter disease: `:559`;
- smoke illness: `:794`;
- resource shutdown: `:855`;
- flood renewal: `:912`;
- respiratory deaths: `:1031`;
- naval disruption and coastal famine: `:1151-1152`;
- dust veil: `:1269`;
- regional landslides and urban fire under rupture: `:1389-1390`.

**Live evidence**

- `natural_disaster_chain` contains only `none`, `aftershock`, `tsunami`, `famine`, `disease`, `wildfire_spread`, `refugee_pressure`, `supply_collapse`, `lahar`, and `political_shock`: `common/script_constants/013_natural_disasters_constants.txt:296-312`.
- `natural_disaster_execute_chain_followup` branches on only those generic values: `common/scripted_effects/013_natural_disasters_effects.txt:5024-5119`.
- The documentation itself describes only seven playable objectives plus refugee/political consequences: `docs/events/013_natural_disasters/overview.md:122`.

**Consequence**

Twenty-five family names and reports lead into a much smaller set of shared outcomes. Distinct accepted routes cannot drive family-specific cards, reports, AI prevention, damage direction, or history summaries.

**Minimal implementation route**

Add a fine-grained `natural_disaster_followup_route` token distinct from the generic mechanical `natural_disaster_chain` class. Resolve and persist the route by family/context, localize and display it, then dispatch compatible routes into shared chain executors where reuse is appropriate. The route token must survive warning, report, aftermath, GUI/history snapshot, mission, resolution, and cleanup.

### P1-02 — 75 named warning actions use only three generic cost packages

**Accepted contract**

- Part 10 calls for family-fit costs drawn from manpower, equipment, trucks, trains, convoys, fuel, XP, construction/civilian capacity, temporary output loss, stability, and time pressure: `013_natural_disasters_spec_part_10_recovery_decision_mission_map.md:5`.
- Part 8 assigns concrete differences such as air XP plus temporary airbase shutdown (`:989`), command/rail disruption (`:1049`), temporary port throughput loss (`:1167`), and major temporary supply penalty (`:1345`).

**Live evidence**

- The 50 helper-driven secondary/tertiary choices in `common/decisions/013_natural_disasters_decisions.txt` call only:
  - `natural_disaster_pay_warning_field_teams` 20 times;
  - `natural_disaster_pay_warning_transport` 14 times;
  - `natural_disaster_pay_warning_shelter` 16 times.
- Across the warning decision block (`:54-3020`) there are zero uses of `add_air_experience`, `add_navy_experience`, `add_army_experience`, `add_command_power`, `add_political_power`, `add_war_support`, or `add_timed_idea`.
- The three shared helpers are defined at `common/scripted_effects/013_natural_disasters_effects.txt:3632-3692` and reduce costs to support equipment/trucks, trains/convoys/fuel, or support equipment, with manpower/stability.
- The current event doc overclaims war-support costs at `docs/events/013_natural_disasters/overview.md:109`.

**Consequence**

The names and protection categories vary, but the state capacity sacrificed by the country does not reflect aviation, naval, rail-command, industrial-shutdown, port-closure, water, or other accepted family decisions.

**Minimal implementation route**

Create centrally tuned cost-profile enums/helpers for at least air operations, coast/naval, command/rail, civilian-output shutdown, shelter/medical, transport/evacuation, fuel/convoy, and field/research observation. Map all 75 actions deliberately, retain the visible physical cost rule, and update AI affordability/war-state priorities and cost localisation in the same change.

### P1-03 — persistent impact modifiers are shared and severity-led rather than family-specific

**Accepted contract**

- Family playbooks require unique damage pattern and persistent disruption: `013_acceptance_gate_matrix.md:12-25` and `013_implementation_readiness_ledger.md:25-32`.
- Part 8 calls for port throughput/dockyard output, airbase efficiency, factory/machinery output, water/shelter/fuel strain, food/crop pressure, and other family-specific directions.

**Live evidence**

- The modifier file explicitly states that one variable-backed disruption profile is shared by every family: `common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt:4-6`.
- `natural_disaster_state_disruption` contains only supplies, supply impact, speed, attrition/truck attrition, repair, and resources: `:9-20`.
- Severity establishes the common modifier values in `natural_disaster_prepare_severity_profile`: `common/scripted_effects/013_natural_disasters_effects.txt:3240-3294`.
- Broad damage booleans scale that same variable set in `natural_disaster_apply_state_modifier_profile`: `:3462-3544`; they do not produce the accepted port, air, factory, water/shelter, or family-specific persistent identities.

**Consequence**

Immediate building damage can vary, but the part the player works against over weeks or months converges on the same supply/repair/resource profile.

**Minimal implementation route**

Either expand the supported variable-backed fields or add a small set of genuine family-profile modifiers. A 25-modifier explosion is unnecessary, but coast/port, aviation/ash, winter/fuel, heat/water, flood/disease, fire/smoke, seismic/transport, volcanic/food, and abnormal/exclusion profiles should be mechanically distinguishable and centrally tuned.

### P1-04 — family reports are unique by name/art but not honest about the resolved outcome

**Accepted contract**

- Reports must be sent after damage is known so they are honest: `013_natural_disasters_spec_part_2_reusable_system.md:35-45`.
- Every report should name visible damage, human consequence, active recovery/aftermath, and the chain risk the country can influence: `013_natural_disasters_spec_part_6_presentation_assets_super_events.md:11-22`.

**Live evidence**

- There are 25 distinct report event definitions and family images at `events/013_natural_disasters.txt:132-830`.
- `natural_disaster_fire_family_report` has access to impact-state family/severity, but it dispatches only a family event id (`chaosx.nr13.101` through `.125`): `common/scripted_effects/013_natural_disasters_effects.txt:1088-1154`.
- The report descriptions are static per family. For example, earthquake always says aftershocks threaten routes at `localisation/english/013_natural_disasters_l_english.yml:2-4`, even if the live route is tsunami, supply collapse, or none. Flood always states contaminated stores at `:8-10`, regardless of resolved damage and route.
- The events do not append a dynamic severity, damage, phase, or actual-route block; their sole option only clears unread state: `events/013_natural_disasters.txt:133-144` and the repeated family pattern thereafter.

**Consequence**

The reports are family-specific prose, but they can assert a chain that did not resolve and omit the actual recovery/chain state.

**Minimal implementation route**

Retain the 25 events and art. Add scripted-localisation report clauses driven by the report-state snapshot: severity, dominant damage, deaths/human consequence band, active phase/recovery need, and actual fine-grained follow-up route. Suppress a chain sentence when no route exists. This should follow P1-01 so the report does not merely repeat the generic chain class.

### P1-05 — evolution unlocks do not upgrade already-open aftermath cards

**Accepted contract**

- Evolution I can alter active-event pools and future season rolls: `013_natural_disasters_spec_part_5_evolutions_clusters_scenarios.md:29`.
- Evolution II explicitly upgrades open aftermath cards and can add new chain risks to unresolved serious disasters: `:48`.

**Live evidence**

- `natural_disaster_refresh_evolution_state` only calculates temporary current evolution when a call is processed: `common/scripted_effects/013_natural_disasters_effects.txt:520-555`.
- `natural_disaster_record_reached_evolutions` records flags/log rows/super-event eligibility but never walks or syncs open cards: `:557-619`.
- `natural_disaster_evolution` is assigned only when a state/card is created or refreshed by a repeat impact: `:2333`, `:5420`, and `:5501`.
- No idempotent evolution-sync effect exists for unresolved active cards.

**Consequence**

An unresolved severe card can remain a lower-evolution recovery object after the world reaches Evolution II, contrary to the accepted active-event behavior.

**Minimal implementation route**

Add an idempotent card-evolution sync invoked by existing event-driven surfaces: due-job worker, reassessment, card interaction, and evolution record. It should upgrade unresolved card evolution once, recalculate eligible route pressure without replacing physical history, refresh category/GUI snapshots, and avoid a prohibited periodic world scan. A global active-state ledger can be used if the existing country arrays cannot enumerate every affected owner safely.

### P1-06 — the abnormal scripted GUI is an urgency/history ledger, not the accepted physical path map

**Accepted contract**

Part 9 requires:

- physical path/current danger rather than a generic announcer: `013_natural_disasters_spec_part_9_abnormal_scripted_gui_map.md:5`;
- an abstract map with path lines, affected-state, next-hit, and chain-origin markers with hover detail: `:24-25`;
- detail buttons that open normal decisions or focus camera: `:26`;
- a timeline containing impact, report, chain, super-event, and reassessment pulses: `:27`;
- selectable state markers and normal decision routing: `:99-103`.

**Live evidence**

- Five cards are fixed left-column buttons: `interface/013_natural_disasters.gui:56-104`.
- All animated family layers occupy the same fixed 470x340 rectangle: `:106-117`; static fallbacks repeat the same arrangement at `:118-129`.
- Next-hit, impact, chain, and relief markers are fixed pixel icons, not state/route positions: `:131-135`.
- The path queue and timeline are text boxes: `:137-145` and `:185-193`.
- The only bottom actions are Refresh, Motion/Static, and Return: `:204-230`.
- Scripted GUI effects support close/return/refresh/animation toggle and five card indices only: `common/scripted_guis/013_natural_disasters_scripted_gui.txt:23-47`. There is no state-marker click, hover record, camera focus, decision/mission route, or timeline-marker action.
- Localisation exposes the queue as `Hazard priority`, not physical path order: `localisation/english/013_natural_disasters_l_english.yml:397-403`.
- Other text nevertheless promises threatened states and expected order of impact: `:343`, `:370`, and the event doc at `docs/events/013_natural_disasters/overview.md:130`.

**Consequence**

The ledger is useful for overlapping urgency and immutable history, but it does not communicate physical segment continuity, origins, or route interaction as accepted. The fixed art is decorative state illustration rather than a map of the live path.

**Minimal implementation route**

Preserve the working urgency/history ledger and eight animation/static packages. Add a real route/segment view with region lanes or dynamically selected marker slots, origin/next-hit/impact/chain markers, marker selection and hover data, focus-camera and decision-routing buttons, and an event-marker timeline. Static mode must retain the same information. Integrate with the parent's physical path/geography and category-presentation work; the missing part is semantic GUI state, not missing art.

### P1-07 — Cluster 5 labels five evolution roles but dispatches all of them as the current global evolution

**Accepted contract**

- Cluster behavior is meant to progress from baseline low entries through varied, regional, and one abnormal logical season as access rises: `013_natural_disasters_spec_part_5_evolutions_clusters_scenarios.md:81-96`.
- The alignment contract says Event 013 appears as multiple logical entries by tier/evolution: `docs/specs/013_natural_disasters_specs/docs_alignment/013_catalog_and_docs_alignment.md:66-67`.

**Live evidence**

- The cluster registers five duplicate Event 013 ids with only role, chance, minimum tier, and danger arrays: `common/scripted_effects/chaosx_event_cluster_effects.txt:438-467`.
- `fire_event_cluster_member_by_temp_id` passes identical Event 013 parameters for every slot: random family, local severity, local-season mode, meaningful news, affected-country report, normal aftermath, and family chain: `:1098-1126`.
- No member-variant/evolution identity is carried through the randomized member queue or Event 013 call.
- Event 013 then derives severity/sequence/family pool from the current global evolution, so at tier 4 the required opening slot can become an Evolution III/abnormal-capable season instead of a low baseline season.
- Cluster details show five rows with the same Event 13 name and only status/danger; the live member text cannot identify opening/early/varied/regional/abnormal roles: `localisation/english/chaosx_gui_l_english.yml:376-377`.
- The event doc overclaims the preserved logical role behavior at `docs/events/013_natural_disasters/overview.md:175`.

**Consequence**

The five display rows are tier gates, not five mechanically distinct logical season variants. The cluster cannot guarantee its accepted escalation shape or explain which role fired.

**Minimal implementation route**

Carry a member-variant enum alongside member id through preparation, participation, random firing order, pending queue, history, and detail arrays. Map it to a validated cluster-only Event 013 family-pool/evolution/severity/sequence override: first two baseline/low, third Evolution I/varied, fourth Evolution II/regional, fifth Evolution III/abnormal. Keep each accepted Event 013 call as one history row. Update member localisation and workbook status only after live validation.

### P1-08 — Skyfall Crisis promises skyfire hail and ocean-impact chains that are not modeled

**Accepted contract**

- Skyfall Crisis includes meteor, meteor shower, skyfire hail, ocean impact, and abnormal ash if chained: `013_natural_disasters_spec_part_5_evolutions_clusters_scenarios.md:109`.
- Player-facing scenario text repeats that contract: `localisation/english/chaosx_gui_l_english.yml:134`.

**Live evidence**

- The Skyfall weighted pool contains meteor impact, meteor shower, direct tsunami, direct ashfall, whole-earth rupture, and massive eruption: `common/scripted_effects/013_natural_disasters_effects.txt:1428-1440`.
- It contains no hailstorm/skyfire entry.
- Tsunami and ashfall are selected as independent primary families; there is no persisted meteor-origin/ocean-impact relationship that creates the promised tsunami or ash chain.
- Below Maximum, an abnormal Skyfall draw resolves to meteor impact: `:1596-1599`; that restriction is sound but still does not supply the missing hail/ocean chain identity.

**Consequence**

The scenario type and workbook/localisation sell a linked skyfall crisis that the controller represents as unrelated family draws.

**Minimal implementation route**

Introduce meteor-origin context. Allow fire-bearing hail as a linked ordinary segment and an ocean meteor origin as the causal precursor to a coastal tsunami route. Use the same sequence/history row and existing throttled news. This depends on P1-01 and the parent's physical chain-target validation. Removing the accepted/localised concepts instead would be a design simplification and requires user approval.

### P1-09 — documentation, localisation, and workbook statuses overclaim the live mechanics

**Exact misalignment**

- `docs/events/013_natural_disasters/overview.md:109` says warning costs include war support as appropriate; the 75-warning block has no war-support cost.
- `docs/events/013_natural_disasters/overview.md:130` says the selected GUI card shows sequence id; the selected-card localisation does not display it, and the GUI has no sequence-id text field.
- `docs/events/013_natural_disasters/overview.md:175` and `docs/systems/event_system/event_clusters.md:80-84` describe five distinct logical cluster season roles that are not carried through dispatch.
- `localisation/english/013_natural_disasters_l_english.yml:343`, `:370`, and workbook Evolution III prose call the urgency list a path/expected next-hit order, while `:397-403` accurately identifies it as hazard priority.
- Read-only workbook inspection found `Events!G14 = Needs Testing` and `Scenarios!G8 = Needs Testing`, but `Clusters!G6 = Implemented`. The improvement handoff explicitly says Cluster 5 must remain incomplete until the scenario matrix passes: `docs/plans/013_natural_disasters_plans/013_improvement_loop_handoff.md:115-119`.
- `docs/plans/013_natural_disasters_plans/013_implementation_validation_notes.md:60` and `013_event_completion_final_audit.md:13` correctly acknowledge that no live-engine scenarios were executed, but both documents also claim no accepted-surface simplification remains. The P0/P1 findings above contradict that closure wording.

**Minimal implementation route**

After gameplay/UI remediation, align the event doc, system docs, GUI/event/scenario localisation, cluster detail text, and all three workbook rows to the verified behavior. Until Cluster 5 is mechanically variant-aware and executed, set `Clusters!G6` to `Needs Testing`. Workbook text must continue to match final in-game wording exactly.

### P1-10 — the accepted runtime validation matrix remains unexecuted

**Accepted contract**

The source package requires meaningful post-implementation scenarios at `013_natural_disasters_spec_part_7_ai_balance_acceptance.md:114-127`, including delayed baseline, a specific external call, Low/Maximum Barrage, Evolution II regional chains, Evolution III path updates, Event 099 disposition, and news throttling.

**Live evidence**

- `docs/plans/013_natural_disasters_plans/013_implementation_validation_notes.md:5-28` records static scenario review, not engine execution.
- The same file states live-engine scenarios were not executed at `:60`.
- `013_event_completion_final_audit.md:90-95` leaves baseline/evolutions/cluster/Barrage, two-call API, abnormal overlap/archive/observer behavior, control transfer/relief, partial/failure/caps, and all ten achievement routes outstanding.

**Consequence**

Static structure does not prove delayed worker wakeups, same-chain regular-event-target isolation, mission timing, multi-observer GUI arrays, control-transfer queue ownership, achievement reachability/disqualification, animation visibility, or scenario evolution/cooldown behavior.

**Minimal validation route after fixes**

1. Baseline and each evolution, including open-card Evolution II upgrade.
2. All five Cluster 5 logical roles at their relevant tiers; confirm each dispatch variant and history/detail identity.
3. Every Disaster Barrage type at Low and Maximum, then the remaining intensity boundaries.
4. Two public calls in one effect chain: accepted→rejected, rejected→accepted, selected-state→selected-country, and partial multi-hit success.
5. Warning-choice causal tests for the P0 routes.
6. Overlapping abnormal paths, same-state repeated abnormal records, later ordinary hit, dormant archive, two simultaneous observers, marker routing, and static mode.
7. Occupied-state transfer with warning, impact, report, chain mission, recovery mission, and in-transit relief.
8. Full/partial/failure/cancel/expiry/cleanup at every phase cap and AI capacity band.
9. All ten achievement unlocks and disqualifiers.
10. Event 051 overlap, Event 046 inactivity, and the accepted Event 099 disposition.

Do not promote Event, Cluster 5, SCN-007, achievements, super events, or abnormal GUI to runtime-complete until the matching scenarios have evidence.

## P2 cleanup, integration, and pacing findings

### P2-01 — evolution stages can be logged together with no Event 013 pacing state

- `natural_disaster_can_open_evolution_i/ii/iii` uses current tier/manual access, and `natural_disaster_refresh_evolution_state` can select the highest stage immediately: `common/scripted_effects/013_natural_disasters_effects.txt:520-555`.
- `natural_disaster_record_reached_evolutions` has three independent `if` blocks: `:557-617`. If Event 013 first fires at a sufficiently high tier, I, II, and III can be written by the same accepted call.
- No Event 013 pending-stage, due-date, or MTTH state exists.

Part 5 permits a pre-fire evolved opening, so this is not automatically a source-spec violation. It is nevertheless inconsistent with the normal evolution pacing guidance unless global chaos tier is explicitly documented as this event's pacing exception. Minimal route: either document and validate the exception, or add one-stage-at-a-time pending/MTTH pacing without blocking pre-fire family availability.

### P2-02 — Event 099 is an accepted placeholder, but three live Event 070 branches call it and silently do nothing

- Event 099 is intentionally inert: `events/099_desert_storm.txt:3-27`.
- Event 070 calls `chaosx.nr99.1` in three sandstorm branches: `events/070_africa_gods.txt:286`, `:313`, and `:343`.
- Part 5 allows Event 099 to remain a placeholder or become a one-line bridge: `013_natural_disasters_spec_part_5_evolutions_clusters_scenarios.md:128-129`.

The placeholder itself is accepted; the live Event 070 probability branches are the integration debt. Minimal route requires a user-owned design choice: either reroute those branches through the Event 013 dust API with deity cost/cooldown/legitimacy and history ownership, or remove/rebalance them explicitly. Do not silently add a fallback.

### P2-03 — the super-event global event target has no end-of-display cleanup

- `natural_disaster_emit_super_event` clears the previous target and saves `natural_disaster_super_event_scope` globally: `common/scripted_effects/013_natural_disasters_effects.txt:634-647`.
- No later `clear_global_event_target = natural_disaster_super_event_scope` exists outside that next-display replacement.
- The visible flag is timed, but global event targets do not auto-clear.

The six route gates and asset/audio identities are otherwise structurally present. Minimal route: schedule cleanup after the display window with a generation/sequence guard so an old cleanup cannot erase a newer super-event scope.

## Surface-by-surface coverage snapshot

| Surface | Current status | Evidence and required route |
| --- | --- | --- |
| Baseline controller | Broad static implementation present | Explicit baseline family pool, severity, scheduled warning/impact jobs, Deaths integration, damage, reports, cards, and cleanup exist. Physical eligibility is owned by the active geography correction; live baseline remains unvalidated. |
| Delayed jobs | Static pass | `chaosx.nr13.2` calls `natural_disaster_process_due_job` at `events/013_natural_disasters.txt:59-65`; aligned queues and exact due-date reservation are at effects `:930-1246`. Runtime wakeup/order/transfer still needs the P1-10 matrix. |
| One-row history | Static pass | `natural_disaster_record_call_history` is called once only after at least one scheduled hit: effects `:2624-2657`; delayed worker/report/news/chain paths do not write an Event 013 history row. |
| External API | Active parent dependency | Wrapper, validation, reset, reject/output tokens, report/aftermath policies, and docs exist. Physical geography, resolved-output proof, repeat/spread/chain/execution validation, and category selector are owned by the 2026-07-11 architecture handoff. Same-chain and report-delivery behavior remain runtime gates. |
| Warning differences | Fail | 75 unique names/protection results exist, but P0-01 reverses causality and P1-02 collapses costs. |
| Impact differences | Partial | Per-family priority damage booleans and report/news ids exist; persistent disruption collapses under P1-03. Physical target identity is the parent dependency. |
| Report differences | Partial/fail | 25 distinct events/art/text exist; resolved outcome honesty fails P1-04. |
| News differences and throttle | Static pass, runtime pending | 25 family news events/text/assets exist and policy/cooldown gates are present. P1-10 must prove late small hits do not spam. |
| Follow-up differences | Fail | Seven playable objectives and two untyped consequences exist; accepted route catalogue collapses under P1-01. |
| Recovery decisions/missions | Broad static pass, runtime pending | Rescue, stabilization, reconstruction, foreign relief, typed chain missions, AI factors, active caps, partial/failure/reassessment/cleanup, and transfer hooks are present across decisions `:3034-6638` and effects `:3418-5191`. P1-01/P1-03 limit family identity; P1-10 is still mandatory. |
| Staged visibility/cleanup | Static pass, runtime pending | Warning, impact, card phases, unread flags, category/relief visibility, closure, invalid owner, and transfer paths exist. Concurrent cap/cleanup/relief scenarios are unexecuted. |
| Evolution I | Static pool/sequence pass | Explicit 16-family pool and wider sequence behavior exist; no separate active-card issue identified for I beyond the general sync architecture. Runtime pending. |
| Evolution II | Partial | Explicit 20-family pool, regional spread, higher severity, and chains exist. Open-card upgrade is missing (P1-05); modifier/route identity is shallow (P1-01/P1-03). |
| Evolution III | Partial | Abnormal family pool, sequence locks, history ledger, super-event eligibility, and real frame packages exist. Physical path presentation fails P1-06; Skyfall linkage fails P1-08. |
| Abnormal GUI | Fail accepted interaction/map contract | Active/history urgency sorting and immutable snapshots are useful and should be retained; physical marker/path/timeline/decision routing is absent. Static fallbacks exist. |
| Frame animation/static fallback | Asset pass | Eight accepted pairs are wired: warning rim, impact rim, next-hit marker, rupture, meteor, eruption, tsunami, and storm corridor. Source frames, processed frames, sheets, GIF previews, static DDS, manifests, and handoffs exist. No missing texture reference was found; the gap is semantic GUI wiring. |
| Integrations 046/051/099 | 046 pass; 051 static pass; 099 bounded debt | Event 046 remains inert; Event 051 has mutual exclusion/cleanup but needs runtime overlap proof; Event 099 placeholder is accepted, while Event 070's three inert branches require a design decision. |
| Disaster Barrage | Partial | One public API launch, five types, four intensities, manual abnormal bypass, non-terminal guard, and scenario history are present. Skyfall lacks accepted linkage (P1-08); all type/intensity runs remain unexecuted. |
| Cluster 5 | Fail logical-role contract | Five registered rows exist, but variant identity is lost (P1-07). Workbook `Implemented` status is premature. |
| Event log/evolution/details | Partial | One-row history, three evolution mappings, Event Details, abnormal archive, and cluster/event/scenario name mappings exist. Cluster member roles and path claims are inaccurate; evolution pacing is P2-01. |
| Achievements | Static route coverage, runtime pending | All 10 accepted achievements are registered at `common/achievements/chaos_redux_achievements.txt:1841-2048`, with sequence/state lifecycle hooks in effects. No high-confidence missing static hook was found in this pass; all unlock/disqualifier scenarios remain outstanding. |
| Super events | Static route coverage, cleanup/runtime pending | Six accepted route gates/assets are present; audio uniqueness is parent-complete and excluded. Global target cleanup is P2-03; route eligibility/display still needs runtime proof. |
| Assets | Static pass | 161 unique Event 013 texture references resolve; report, news, decision, modifier, achievement, abnormal GUI, animation, and six super-event packages are represented in manifests/handoffs. No fallback substitution was found. |
| Localisation/docs/workbook | Fail final alignment | P1-09 lists exact overclaims/status mismatch. Report localisation also fails outcome honesty under P1-04. |

## Recommended implementation order and ownership boundaries

1. **Fix P0-01 first.** Do not build new routes/reports on the current choice-driven hazard selection.
2. **Finish the parent's geography/API/category tranche.** Its chain-target and output work should expose the route/state facts needed below.
3. **Add the fine-grained follow-up route token (P1-01).** This becomes the shared input for warning mitigation, report clauses, cards, GUI, AI, Skyfall linkage, and history.
4. **Differentiate warning costs and persistent modifier profiles (P1-02/P1-03).** Update AI and player cost text together.
5. **Make reports outcome-honest and sync active cards on evolution (P1-04/P1-05).**
6. **Preserve Cluster 5 member variants end to end (P1-07), then correct its workbook/detail status.**
7. **Implement the physical abnormal-map interaction layer and Skyfall causal routes (P1-06/P1-08).** Reuse the completed assets; do not replace them with a new fallback.
8. **Align all docs/localisation/workbook fields (P1-09).**
9. **Run the full engine matrix (P1-10), then close P2 cleanup/integration/pacing decisions.**
10. **Use the Event 013 completion, localisation, decision/mission, and asset audits again before any completion claim.**

## Completion gates for the improvement tranche

Do not claim the accepted Event 013 package complete while any of these statements is true:

- a warning choice changes which follow-up hazard exists;
- the accepted family route is not preserved beyond a generic chain class;
- family warning costs and long-lived modifiers remain mechanically interchangeable;
- a report can state a chain/recovery fact that did not resolve;
- an Evolution II unlock leaves unresolved lower-stage cards untouched;
- the abnormal map cannot select a physical marker, communicate route continuity, focus the state, or route to the normal decision/mission surface;
- Cluster 5's five labelled roles still dispatch identical current-evolution calls;
- Skyfall still lacks fire-bearing hail and meteor-origin ocean/tsunami causality while player text promises both;
- Cluster 5 remains marked `Implemented` without its logical-role and runtime proof;
- the required baseline/evolution/API/cluster/scenario/transfer/partial/failure/achievement/GUI cases remain static-only;
- the super-event global target remains indefinitely live;
- any fallback or simplification is used without explicit user approval.

## Sources and skills used

Repo skills:

- `chaos-redux-events`
- `chaos-redux-subagents`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `xlsx` for read-only workbook inspection

Required offline Paradox wiki pages consulted:

- Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding
- Interface Modding, Scripted GUI Modding, Achievement Modding, Sound/Music, and Graphical asset modding for the touched audit surfaces

Vanilla authority consulted:

- official script concept/script constants/effects/triggers/decisions/scripted GUI/on-actions documentation
- vanilla `frameAnimatedSpriteType` and scripted-GUI precedents, including `interface/alerts.gfx`

All ten Event 013 source specs, the acceptance/validation/readiness matrices, blocklist, source/disposition maps, implementation docs, prior handoffs/audits, live gameplay/UI/localisation/assets, and the workbook were read in audit mode. No gameplay or data fallback was introduced. No commit was created; the parent owns implementation and plan-scoped commits.
