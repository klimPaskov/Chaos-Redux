# Event 064 Acceptance Criteria

These checks define implementation acceptance for Border Fortifications. A checked item needs source evidence and the relevant static, scenario, probability, asset, or save-load proof. Planning completion does not mark these implementation boxes complete.

## A. Identity and registration

- [ ] A001 All project-facing event labels, event-scoped folders, filenames, prompt names, asset identifiers, achievement identifiers, and probability scenario IDs use `064`.
- [ ] A002 Event name is Border Fortifications everywhere.
- [ ] A003 Event type is Minor Repeatable everywhere.
- [ ] A004 Event Chaos level is `1` everywhere.
- [ ] A005 Event status stays To Be Reworked until implementation begins.
- [ ] A006 Event status changes to Needs Testing only after the implementation is wired and statically valid.
- [ ] A007 Canonical entry event remains `chaosx.nr64.1`.
- [ ] A008 Namespace remains unique.
- [ ] A009 Event 064 is registered in the correct repeatable-event array.
- [ ] A010 Event 064 is absent from major and fire-once arrays.
- [ ] A011 `get_event_type` or the current replacement resolves Event 064 correctly.
- [ ] A012 Debug and settings name mappings resolve Border Fortifications.
- [ ] A013 Event enable and disable settings affect normal automatic selection.
- [ ] A014 Manual event triggering uses the accepted no-cluster route by default.
- [ ] A015 The existing thin Event 064 shell is fully replaced and no duplicate path remains.

## B. Global transaction

- [ ] B001 One unique wave token is created per Event 064 incident.
- [ ] B002 The token records natural, cluster, manual, and debug context before construction.
- [ ] B003 A second root cannot begin while the same incident token is active.
- [ ] B004 The world country scope is snapshotted once.
- [ ] B005 Each valid country is processed at most once.
- [ ] B006 The construction wave finishes before human report choices own any state.
- [ ] B007 Report options cannot rerun automatic construction.
- [ ] B008 AI and human countries receive physical changes at the same game moment.
- [ ] B009 Global result counters equal the sum of saved country results.
- [ ] B010 An invalid country does not abort the world transaction.
- [ ] B011 An invalid province does not abort its country transaction.
- [ ] B012 A no-op wave still cleans up safely.
- [ ] B013 Temporary country arrays are cleared.
- [ ] B014 Temporary province and state candidates are cleared.
- [ ] B015 Temporary score variables are cleared.
- [ ] B016 Cluster context is cleared after the wave.
- [ ] B017 Save and reload cannot repeat a completed global transaction.
- [ ] B018 Multiplayer produces one world transaction and one local report per human country.
- [ ] B019 Leaving a report open does not delay the physical grant.
- [ ] B020 Event history records one wave and country reports add no duplicate rows.

## C. Country eligibility

- [ ] C001 Normal majors are valid.
- [ ] C002 Normal minors are valid.
- [ ] C003 Player-controlled countries are valid.
- [ ] C004 AI countries are valid.
- [ ] C005 Subjects with territory are valid.
- [ ] C006 Overlords with territory are valid.
- [ ] C007 Faction members are valid.
- [ ] C008 Civil-war countries are valid.
- [ ] C009 Released and temporary countries are valid when they control normal territory.
- [ ] C010 Special Chaos countries are not blanket-excluded.
- [ ] C011 Special actors with normal map buildings but no normal economy still receive the physical wave.
- [ ] C012 Special actors skip unsupported response systems cleanly.
- [ ] C013 Dead country scopes are skipped.
- [ ] C014 Off-map carrier scopes are skipped.
- [ ] C015 Countries with no controlled land territory are skipped for construction.
- [ ] C016 Land-borderless human countries receive the correct observation or redoubt report.

## D. Direct frontier definition

- [ ] D001 Candidate province is land.
- [ ] D002 Candidate province is currently controlled by the processed country.
- [ ] D003 Candidate has a direct passable land adjacency to another country's controlled province.
- [ ] D004 Peaceful foreign borders qualify.
- [ ] D005 Hostile fronts qualify.
- [ ] D006 Allied borders qualify.
- [ ] D007 Faction-internal borders qualify.
- [ ] D008 Subject and overlord borders qualify.
- [ ] D009 Civil-war frontiers qualify.
- [ ] D010 Occupation control frontiers qualify.
- [ ] D011 River land edges qualify.
- [ ] D012 Enclaves qualify.
- [ ] D013 Strait-only adjacency does not qualify.
- [ ] D014 Canal-only non-land adjacency does not qualify.
- [ ] D015 Sea adjacency does not qualify.
- [ ] D016 Lake adjacency does not qualify.
- [ ] D017 Impassable adjacency does not qualify.
- [ ] D018 Off-map provinces do not qualify.
- [ ] D019 Invalid land-fort slots do not qualify.
- [ ] D020 Same-controller adjacency does not qualify.
- [ ] D021 A province touching several foreign countries is processed once.
- [ ] D022 A border state is created only from at least one valid direct frontier province.
- [ ] D023 A coastal border state also has a valid coast or port role.
- [ ] D024 Firing-time control determines the snapshot.
- [ ] D025 Later same-day border changes do not reopen the snapshot.

## E. Baseline fortification

- [ ] E001 Every valid direct frontier province below cap receives one land-fort level.
- [ ] E002 Baseline ordinary frontier cap starts at level three.
- [ ] E003 A province at cap receives no baseline level.
- [ ] E004 A province above cap is preserved.
- [ ] E005 Existing historical forts are not lowered.
- [ ] E006 Existing mod-added forts are not lowered.
- [ ] E007 The effect adds one level while preserving the existing building value.
- [ ] E008 One baseline wave does not grant anti-air.
- [ ] E009 One baseline wave does not grant radar.
- [ ] E010 One baseline wave does not grant infrastructure.
- [ ] E011 One baseline wave does not grant railways.
- [ ] E012 One baseline wave does not grant supply hubs.
- [ ] E013 One baseline wave does not grant coastal forts.
- [ ] E014 One baseline wave does not grant internal redoubts.
- [ ] E015 Fort damage behavior is inspected and documented.
- [ ] E016 The baseline does not accidentally repair every existing fort unless the intended effect explicitly does so.
- [ ] E017 Physical forts persist after control transfer.
- [ ] E018 Physical forts persist after ownership transfer.
- [ ] E019 Physical forts persist after peace settlement.
- [ ] E020 Physical forts persist after save and reload.

## F. Repeat lifecycle

- [ ] F001 A later valid firing creates a new unique wave token.
- [ ] F002 A later firing builds a new current-control snapshot.
- [ ] F003 Newly created frontiers can receive forts on a later wave.
- [ ] F004 Old internalized fort belts remain physical.
- [ ] F005 Repeated baseline waves approach caps gradually.
- [ ] F006 Repeated waves do not exceed active caps.
- [ ] F007 Repeated waves can choose different evolved targets.
- [ ] F008 Last-wave target memory does not become permanent unbounded state.
- [ ] F009 A natural cooldown or equivalent guard prevents immediate global repeats.
- [ ] F010 The cooldown is tuned with the shared repeatable weight system.
- [ ] F011 Event 064 remains repeatable after the cooldown.
- [ ] F012 Manual debug firing can bypass natural timing only under explicit debug context.
- [ ] F013 Manual debug firing suppresses achievements.
- [ ] F014 Exact duplicate cluster dispatch is rejected or merged.
- [ ] F015 No recurring world scan fortifies borders between waves.

## G. Evolution framework

- [ ] G001 Defense in Depth requires at least 200 Chaos.
- [ ] G002 Fortress States requires at least 400 Chaos.
- [ ] G003 Fortress World requires at least 600 Chaos.
- [ ] G004 Each stage also follows shared evolution maturation.
- [ ] G005 Each stage respects event settings enablement.
- [ ] G006 Evolution eligibility adds zero direct Chaos.
- [ ] G007 Evolution maturation adds zero direct Chaos.
- [ ] G008 Enabled stages affect future waves.
- [ ] G009 Stages do not retrofit every prior position at maturation time.
- [ ] G010 A first high-Chaos firing uses only stages legitimately enabled and matured.
- [ ] G011 High-tier first firing still respects per-wave caps.
- [ ] G012 Disabled Defense in Depth skips depth positions cleanly.
- [ ] G013 Fortress States works when Defense in Depth is disabled.
- [ ] G014 Fortress World works when Fortress States is disabled.
- [ ] G015 Lower enabled stages still work when higher stages are disabled.
- [ ] G016 Evolution history logs first concrete materialization.
- [ ] G017 Evolution history does not log a stage that changed nothing.
- [ ] G018 Event Details evolution catalog remains separate from evolution history.

## H. Defense in Depth

- [ ] H001 Strategic frontier anchors use bounded scoring.
- [ ] H002 Current hostile front increases anchor priority.
- [ ] H003 Capital approach increases anchor priority.
- [ ] H004 Major victory point increases anchor priority.
- [ ] H005 Supply and railway role increases anchor priority.
- [ ] H006 Mountain or hill terrain increases anchor priority where valid.
- [ ] H007 River crossing approach increases anchor priority where engine support is reliable.
- [ ] H008 Corridor or enclave exposure increases anchor priority.
- [ ] H009 Allied borders remain eligible through geographic value.
- [ ] H010 Anchor quota scales sublinearly with frontier size.
- [ ] H011 Anchor hard cap is enforced.
- [ ] H012 An anchor receives at most one evolved bonus in a wave.
- [ ] H013 Ordinary frontier plus anchor totals at most two Event 064 levels in a wave.
- [ ] H014 Defense in Depth ordinary cap starts at level four.
- [ ] H015 Defense in Depth anchor cap starts at level five.
- [ ] H016 Depth positions are bounded.
- [ ] H017 Depth positions are near a real frontier approach or strategic objective.
- [ ] H018 Depth positions are not uniform random interior provinces.
- [ ] H019 Depth position cap starts at level two.
- [ ] H020 A depth position receives at most one level in a wave.
- [ ] H021 Distinct regions receive priority before repeated targets in one region.
- [ ] H022 Unsupported exact terrain or crossing detection uses a documented safe approximation.
- [ ] H023 A maintained map-role registry, when needed, is validated and documented.
- [ ] H024 No valid depth candidate leaves the quota slot unused and creates no filler position.

## I. Fortress States

- [ ] I001 Fortress State must contain a valid direct frontier province.
- [ ] I002 About thirty percent of valid border states is the starting selection anchor.
- [ ] I003 Minimum one selected state applies when a meaningful candidate exists.
- [ ] I004 Hard cap six is enforced as a starting design.
- [ ] I005 Current hostile front raises selection priority.
- [ ] I006 Capital, VP, industry, supply, port, airbase, and strategic sites influence selection.
- [ ] I007 Geographic spread is enforced.
- [ ] I008 Selected-state direct frontier can receive one resolved evolved bonus.
- [ ] I009 Anchor and selected-state bonuses do not stack into a third same-wave level.
- [ ] I010 Evolution II ordinary frontier cap starts at level six.
- [ ] I011 Evolution II strategic sector cap starts at level seven.
- [ ] I012 Evolution II depth cap starts at level three.
- [ ] I013 State anti-air is added only to valid role states.
- [ ] I014 State anti-air cap starts at level three.
- [ ] I015 Radar is rarer than land forts.
- [ ] I016 Radar cap starts at level two during Evolution II.
- [ ] I017 Radar selection favors real air, naval, port, or strategic warning roles.
- [ ] I018 Supply work prefers damage repair or existing network improvement.
- [ ] I019 Infrastructure improvement is bounded.
- [ ] I020 Railway improvement uses a verified route.
- [ ] I021 New supply hubs are exceptional.
- [ ] I022 A free supply hub is never added to every selected state.
- [ ] I023 Automatic supply changes are capped per selected state and wave.
- [ ] I024 Coastal defense requires a coastal border state.
- [ ] I025 Strait-only island states do not become Fortress States.
- [ ] I026 Coastal forts prioritize ports and bounded landing approaches.
- [ ] I027 Coastal forts do not cover every coastal province.
- [ ] I028 Coastal-fort cap starts at level three.
- [ ] I029 A normal selected state receives a role-based subset of buildings.
- [ ] I030 A selected state does not automatically receive every package component.

## J. Fortress World

- [ ] J001 Capital or valid capital approach receives first redoubt priority.
- [ ] J002 Major victory points are valid redoubt candidates.
- [ ] J003 Supply hubs and railway junctions are valid redoubt candidates.
- [ ] J004 Major industrial centers are valid redoubt candidates.
- [ ] J005 Major ports and naval bases are valid redoubt candidates.
- [ ] J006 Strategic air, missile, nuclear, radar, or event sites are valid when supported.
- [ ] J007 Internal corridor positions are valid when they protect real routes.
- [ ] J008 Random rural filler is not allowed.
- [ ] J009 Redoubt quota follows country-size bands.
- [ ] J010 Major status adds at most one base quota slot.
- [ ] J011 Hard cap six is enforced.
- [ ] J012 Capital already on frontier resolves to one capital frontier role.
- [ ] J013 Capital frontier does not receive a third same-wave land-fort level.
- [ ] J014 Invalid capital province selects a valid approach.
- [ ] J015 Island countries can receive internal redoubts.
- [ ] J016 Island redoubt behavior does not create a false land frontier.
- [ ] J017 Evolution III ordinary frontier cap starts at level seven.
- [ ] J018 Evolution III strategic sector cap starts at level eight.
- [ ] J019 Evolution III depth cap starts at level four.
- [ ] J020 Internal redoubt cap starts at level three.
- [ ] J021 Radar can rise to level three in valid strategic states.
- [ ] J022 Internal redoubts remain sparse.
- [ ] J023 Old redoubts remain after capital or network changes.
- [ ] J024 Later waves can select new current strategic positions.

## K. Role overlap and deduplication

- [ ] K001 Every province receives one resolved land-fort role.
- [ ] K002 Role priority is documented.
- [ ] K003 Capital redoubt, anchor, and Fortress State overlap is resolved once.
- [ ] K004 Direct frontier baseline and one evolved bonus is the maximum automatic direct grant.
- [ ] K005 Depth and internal overlap produces one interior grant.
- [ ] K006 State anti-air and radar use state-level dedupe.
- [ ] K007 Coastal target dedupe prevents repeated port fort additions in one wave.
- [ ] K008 Player project uses a separate wave-use guard.
- [ ] K009 A player project cannot make the automatic wave reapply.
- [ ] K010 Result counters count actual building changes once.

## L. Reports and postures

- [ ] L001 Every human country receives the correct local report after construction.
- [ ] L002 Report shows local direct frontier improvement count.
- [ ] L003 Report distinguishes already-capped frontier count where useful.
- [ ] L004 Report summarizes local anchor count.
- [ ] L005 Report summarizes local depth count.
- [ ] L006 Report summarizes Fortress States changed.
- [ ] L007 Report summarizes internal redoubts changed.
- [ ] L008 Report communicates the global nature of the incident.
- [ ] L009 Report does not claim the government ordered normal construction.
- [ ] L010 Report hides internal scores and arrays.
- [ ] L011 Integrate the Line appears only when locally meaningful.
- [ ] L012 Keep the Roads Open appears only when locally meaningful.
- [ ] L013 Study the Breach appears only with a meaningful foreign target.
- [ ] L014 Observation-only report appears when every active posture is invalid.
- [ ] L015 One posture is selected per response window.
- [ ] L016 Old posture is removed before new posture applies.
- [ ] L017 Postures do not stack.
- [ ] L018 Starting posture duration is around 180 days.
- [ ] L019 Posture duration is visible.
- [ ] L020 Posture modifier effects use valid current modifiers.
- [ ] L021 Integrate remains defense focused.
- [ ] L022 Logistics remains supply and transport focused.
- [ ] L023 Breach remains fort or target focused.
- [ ] L024 No posture becomes a broad permanent army bonus.

## M. Decision category

- [ ] M001 Event 064 uses a normal decision category.
- [ ] M002 Category uses a static picture.
- [ ] M003 The response uses an ordinary decision category with its accepted static picture.
- [ ] M004 Public state is limited to posture, deadline, active project, and valid target status.
- [ ] M005 Category displays current posture.
- [ ] M006 Category displays response time remaining.
- [ ] M007 Category displays active project when present.
- [ ] M008 Category hides after posture, project, and challenge display end.
- [ ] M009 One Event 064 sector project can be active per country.
- [ ] M010 Targeted decisions use map targets without duplicating every state as list clutter.
- [ ] M011 Invalid target tooltips state a player-facing reason.
- [ ] M012 Costs, duration, and result are visible before start.
- [ ] M013 Mission failure conditions are visible after start.
- [ ] M014 Category state survives save and reload.
- [ ] M015 Category cleanup removes stale map markers.

## N. Reinforce a Priority Sector

- [ ] N001 Requires Integrate posture.
- [ ] N002 Requires open response window.
- [ ] N003 Requires no active Event 064 project.
- [ ] N004 Target is a controlled affected border state.
- [ ] N005 Target has a valid province below strategic cap.
- [ ] N006 Cost uses no more than four spend types.
- [ ] N007 Cost prefers civilian factories, infantry equipment, support equipment, and manpower.
- [ ] N008 Cost scales with target and country capacity.
- [ ] N009 Cost preserves reserve floors.
- [ ] N010 Duration starts in the 45 to 75 day band.
- [ ] N011 Result is a bounded fort package.
- [ ] N012 Result does not fortify every land province in the state.
- [ ] N013 Result respects caps.
- [ ] N014 State can receive the package once per wave.
- [ ] N015 Target loss fails or cancels safely.
- [ ] N016 Completion applies once.

## O. Connect the New Line

- [ ] O001 Requires Logistics posture.
- [ ] O002 Requires open response window.
- [ ] O003 Target has a real network gap.
- [ ] O004 Cost uses civilian factories, trains, trucks, and support equipment or a smaller valid bundle.
- [ ] O005 Train and truck reserves are preserved.
- [ ] O006 Duration starts in the 60 to 100 day band.
- [ ] O007 Damage repair is preferred when safely supported.
- [ ] O008 Existing infrastructure or railway support is preferred.
- [ ] O009 Physical route improvement is bounded.
- [ ] O010 Ordinary project does not create a free supply hub.
- [ ] O011 Safe local supply alternative is used only when physical route change cannot be represented.
- [ ] O012 Target loss cleans up the mission.
- [ ] O013 Completion applies once.

## P. Conduct Breach Exercises

- [ ] P001 Requires Study the Breach posture.
- [ ] P002 Requires a meaningful fortified foreign target.
- [ ] P003 Harmless unfortified targets are excluded.
- [ ] P004 Allies and invalid tags are excluded.
- [ ] P005 Target country and objective are stored.
- [ ] P006 Cost uses no more than Army Experience, support equipment, fuel, and Command Power.
- [ ] P007 Reserve floors are preserved.
- [ ] P008 Duration starts in the 45 to 75 day band.
- [ ] P009 Reward lasts roughly 90 to 150 days.
- [ ] P010 Reward improves fort attack or target-bound preparation.
- [ ] P011 Reward does not become broad permanent attack.
- [ ] P012 Target invalidation cleans up safely.
- [ ] P013 A new completed Event 064 breach plan replaces the old plan and copies do not stack.
- [ ] P014 Island countries can use the project with a real continental plan.
- [ ] P015 Completion applies once.

## Q. Harden the Air and Coastal Flank

- [ ] Q001 Requires concrete Evolution II access.
- [ ] Q002 Target is a selected valid Fortress State.
- [ ] Q003 Air branch requires a real air-defense role.
- [ ] Q004 Coastal branch requires a real coastal border role.
- [ ] Q005 Air branch uses Air Experience and never Navy Experience in the same bundle.
- [ ] Q006 Coastal branch uses Navy Experience and never Air Experience in the same bundle.
- [ ] Q007 Each bundle uses no more than four spend types.
- [ ] Q008 Duration starts in the 60 to 100 day band.
- [ ] Q009 Result adds no more than two justified physical improvements.
- [ ] Q010 Result respects anti-air, radar, and coastal-fort caps.
- [ ] Q011 Combined icon remains readable or uses the accepted simplified flank symbol.
- [ ] Q012 Target state can receive the same package once per wave.
- [ ] Q013 Completion applies once.

## R. Prepare a National Redoubt

- [ ] R001 Requires concrete Evolution III access.
- [ ] R002 Country has one valid strategic redoubt target.
- [ ] R003 Capital or capital approach receives default target priority.
- [ ] R004 Player can choose another valid strategic target when interface supports it.
- [ ] R005 One National Redoubt project can complete per wave.
- [ ] R006 Cost uses no more than four spend types.
- [ ] R007 Cost prefers civilian factories, trains or equipment, support equipment, and manpower.
- [ ] R008 Duration starts in the 90 to 140 day band.
- [ ] R009 Result adds one bounded redoubt fort level.
- [ ] R010 Optional support improvement has a clear target role.
- [ ] R011 Result does not create a full capital ring.
- [ ] R012 Target loss or invalid capital change cleans up safely.
- [ ] R013 Completion applies once.

## S. Project lifecycle and exploits

- [ ] S001 Active mission timer persists through save and reload.
- [ ] S002 Mission completion cannot fire twice.
- [ ] S003 Player cannot start several Event 064 projects at once.
- [ ] S004 Player cannot switch posture to collect several modifiers.
- [ ] S005 Player cannot select a fully capped target.
- [ ] S006 Player cannot cancel immediately for a full refund.
- [ ] S007 Refund never exceeds committed resources.
- [ ] S008 Target transfer does not transfer the mission.
- [ ] S009 Target transfer does not duplicate the reward.
- [ ] S010 Annexation removes country posture and project state.
- [ ] S011 Capitulation follows a documented project rule.
- [ ] S012 Released successor does not inherit stale posture by default.
- [ ] S013 Negative equipment or transport stockpiles are impossible.
- [ ] S014 New wave cannot bypass one-active-project cap.
- [ ] S015 Expired response window blocks new starts.
- [ ] S016 Active project can finish after window expiry when still valid.
- [ ] S017 Project history names correct target and outcome.

## T. AI posture behavior

- [ ] T001 AI chooses after local result is known.
- [ ] T002 Capital emergency strongly favors Integrate.
- [ ] T003 Severe supply problem strongly favors Logistics.
- [ ] T004 Real fortified offensive plan strongly favors Breach.
- [ ] T005 No local line makes Integrate invalid unless a redoubt exists.
- [ ] T006 No network target makes Logistics invalid.
- [ ] T007 No fortified foreign target makes Breach invalid.
- [ ] T008 Observation is used only when active choices are invalid.
- [ ] T009 Tiny countries can receive a posture without being forced into an unaffordable project.
- [ ] T010 Special actor behavior follows owner contract.
- [ ] T011 Subject AI respects actual strategic freedom.
- [ ] T012 Civil-war AI values capital survival.
- [ ] T013 Island offensive AI can choose Breach.
- [ ] T014 Island defensive AI can use Fortress World redoubt behavior.
- [ ] T015 Random variation cannot regularly override dominant survival conditions.
- [ ] T016 Similar valid choices retain bounded variety.
- [ ] T017 Old posture memory does not freeze repeat-wave choice.

## U. AI project behavior

- [ ] U001 AI starts a project only when one valid target exists.
- [ ] U002 AI confirms the result changes a physical or target-bound state.
- [ ] U003 AI preserves equipment reserve floors.
- [ ] U004 AI preserves train and truck reserve floors.
- [ ] U005 AI preserves convoy reserve floor.
- [ ] U006 AI preserves fuel reserve floor.
- [ ] U007 AI respects civilian industry cap.
- [ ] U008 AI skips likely-to-fail remote construction when a safer target exists.
- [ ] U009 AI reinforces capital and active fronts before quiet allied borders.
- [ ] U010 AI selects a real network gap and rejects an already developed state.
- [ ] U011 AI selects real high-fort target for breach.
- [ ] U012 AI uses air branch under real air threat.
- [ ] U013 AI uses coastal branch under real invasion threat.
- [ ] U014 AI uses National Redoubt under capital or national collapse threat.
- [ ] U015 AI can skip all projects.
- [ ] U016 AI does not start a second project.

## V. Probability evidence

- [ ] V001 `chaosx_ai_probability_auditor` is spawned with `fork_context=false`.
- [ ] V002 Auditor receives complete option and decision blocks.
- [ ] V003 Auditor receives complete target pools.
- [ ] V004 Auditor receives every scenario from the probability matrix.
- [ ] V005 Base weights and external factors are inspected.
- [ ] V006 Invalid choices prove exact zero probability.
- [ ] V007 Normalized posture probabilities are recorded.
- [ ] V008 Project start probabilities are recorded.
- [ ] V009 Target-selection probabilities or rankings are recorded.
- [ ] V010 Sweeps cover threat, supply, fort level, and reserve changes.
- [ ] V011 Cluster arbitration sequence is simulated or otherwise proven.
- [ ] V012 Additional cluster membership is reachable.
- [ ] V013 No sequence can execute Event 064 twice in one incident.
- [ ] V014 Before and after tuning evidence is saved.
- [ ] V015 Probability completion is withheld when the required toolchain is unavailable.

## W. Chaos impact map

- [ ] W001 First global premium requires actual construction footprint.
- [ ] W002 First global premium is one-time.
- [ ] W003 Starting target is around +8 within the accepted band.
- [ ] W004 Surviving-world percentage fallback handles late unified maps.
- [ ] W005 Repeat premium requires a meaningful new footprint.
- [ ] W006 Repeat premium uses a family cooldown.
- [ ] W007 Repeat premium uses a short-window cap.
- [ ] W008 No-op wave adds zero direct Chaos.
- [ ] W009 Debug wave adds zero direct Chaos.
- [ ] W010 Evolution eligibility adds zero direct Chaos.
- [ ] W011 Evolution maturation adds zero direct Chaos.
- [ ] W012 Defense in Depth pays only on first concrete materialization.
- [ ] W013 Fortress States pays only on first concrete materialization.
- [ ] W014 Fortress World pays only on first concrete materialization.
- [ ] W015 Several stages in one wave pay only when each meets its own footprint.
- [ ] W016 Cluster convergence premium requires another concrete military-abundance result.
- [ ] W017 Cluster convergence premium pays once per cluster incident.
- [ ] W018 Wars and casualties are not counted again by Event 064.
- [ ] W019 Shared military buildup and building sources are inspected.
- [ ] W020 Event-specific premiums document their distinct abnormal cause.
- [ ] W021 Event 064 owns no false demolition reversal.
- [ ] W022 Completion report lists shared-source overlap decisions.

## X. Cluster integration

- [ ] X001 Event 064 is a Medium Sudden Abundance member.
- [ ] X002 Event 064 is a Medium Military Preparation member.
- [ ] X003 Both memberships appear in the authoritative cluster data.
- [ ] X004 Both memberships appear in cluster details.
- [ ] X005 Opening either member row reaches Event 064 details.
- [ ] X006 One automatic Event 064 selection enters at most one cluster context.
- [ ] X007 Eligible-membership arbitration is shared and documented.
- [ ] X008 Additional membership is not permanently shadowed by primary membership.
- [ ] X009 Manual cluster trigger uses exact requested cluster.
- [ ] X010 Standalone Event 064 remains valid.
- [ ] X011 Cluster pacing applies once.
- [ ] X012 Event 064 repeat weight and history still apply once.
- [ ] X013 Queued member context is prepared before execution.
- [ ] X014 Event 064 does not borrow another member's target scope.
- [ ] X015 Sudden Abundance context keeps global physical scope.
- [ ] X016 Military Preparation context keeps global physical scope.
- [ ] X017 Cluster context can change strategic scoring only through relevant conditions.
- [ ] X018 Cluster cost relief affects one relevant cost element.
- [ ] X019 Cluster context does not raise every fort cap.
- [ ] X020 Cluster context does not generate duplicate member rewards.
- [ ] X021 Cluster history records Event 064 member result.
- [ ] X022 Normal event history also records the wave.
- [ ] X023 Missing shared multi-cluster runtime is recorded as a blocker and remains visible.

## Y. Event connections

- [ ] Y001 Event 19 link does not spawn extra divisions through Event 064.
- [ ] Y002 Event 27 link does not grant a second doctrine reward.
- [ ] Y003 Event 32 strategic sites can raise valid protection priority.
- [ ] Y004 Event 42 can reduce one relevant project cost without duplicating stockpiles.
- [ ] Y005 Event 56 can raise coastal priority around real naval assets.
- [ ] Y006 Event 23 can raise anti-air, radar, or redoubt priority around real strategic sites.
- [ ] Y007 Event 22 receives no positive atrocity reward from Event 064.
- [ ] Y008 Event 55 network quality can lower actual logistics work.
- [ ] Y009 Event 58 building levels are read and caps respected.
- [ ] Y010 Event 61 does not delete physical forts.
- [ ] Y011 Event 46 map shuffle does not trigger an unbounded recurring reconstruction.
- [ ] Y012 Event 63 territory transfer preserves physical buildings and clears unsupported temporary country state.
- [ ] Y013 Event 62 can use existing faction-internal fort geography without rebuilding it.
- [ ] Y014 Event 4 and Event 45 AI can account for fortified targets through their own systems.
- [ ] Y015 Connections use lightweight flags and current state with no extra popup chains.

## Z. History, details, and text

- [ ] Z001 Global History row is actorless or uses another verified non-misleading global presentation.
- [ ] Z002 History row records date and world footprint.
- [ ] Z003 History row does not multiply by human count.
- [ ] Z004 Local report uses the correct country counts.
- [ ] Z005 Event Details explains the premise.
- [ ] Z006 Event Details explains physical persistence after border changes.
- [ ] Z007 Event Details avoids exact hidden caps and scores.
- [ ] Z008 Evolution catalog contains all three accepted evolutions.
- [ ] Z009 Evolution history uses concrete dates only after materialization.
- [ ] Z010 Cluster text uses correct member severity.
- [ ] Z011 Final event description no longer says the government ordered normal construction.
- [ ] Z012 Every report option has final localisation.
- [ ] Z013 Every decision and mission has final localisation.
- [ ] Z014 Every invalidation reason has final localisation.
- [ ] Z015 Every posture modifier has final localisation.
- [ ] Z016 Dynamic singular and plural grammar is correct.
- [ ] Z017 No developer-facing variable names reach the player.
- [ ] Z018 No working-label warning reaches the player.
- [ ] Z019 Localisation duplicate and missing-key audit passes.
- [ ] Z020 Localisation encoding and BOM follow repository convention.

## AA. Assets

- [ ] AA001 Current report event art is inspected.
- [ ] AA002 Existing report sprite identity is preserved or migration is documented.
- [ ] AA003 Final report image uses correct `210x176` treatment.
- [ ] AA004 Report image has valid transparent corners.
- [ ] AA005 Report image contains no readable text.
- [ ] AA006 Report image contains no modern objects.
- [ ] AA007 Report image contains no country flag that implies one origin.
- [ ] AA008 Decision category picture uses the verified active consumer dimensions.
- [ ] AA009 Category picture has no fake buttons or meters.
- [ ] AA010 Category icon is `32x32` and readable.
- [ ] AA011 Three posture icons are `64x64` and distinct.
- [ ] AA012 Five decision icons are `32x32` and distinct.
- [ ] AA013 Four completed achievement icons are `64x64` and distinct.
- [ ] AA014 Grey and not-eligible achievement variants are processed through standard tooling.
- [ ] AA015 Icon transparency is valid.
- [ ] AA016 DDS format matches each consumer.
- [ ] AA017 Every asset has a PNG preview.
- [ ] AA018 Every asset has source-mode and provenance notes.
- [ ] AA019 Every asset has a final path and sprite proposal.
- [ ] AA020 Every asset has a SHA-256 hash in the manifest.
- [ ] AA021 `gfx_handoff.md` is complete.
- [ ] AA022 Runtime files point only to final asset paths.
- [ ] AA023 Native-size review passes for every icon.
- [ ] AA024 Event-window and decision-window visual review passes.
- [ ] AA025 The asset inventory contains only the accepted report, category, posture, decision, and achievement families.

## AB. Achievements

- [ ] AB001 Continent of Concrete is registered.
- [ ] AB002 Continent of Concrete uses a natural Event 064 challenge wave.
- [ ] AB003 Its neighbor, state, and frontier minimums are enforced.
- [ ] AB004 Its fort-coverage requirement is bounded and scriptable.
- [ ] AB005 Its multi-neighbor war hold is tracked for 180 days.
- [ ] AB006 Its marked border states cannot be reduced by transfer exploit.
- [ ] AB007 The Line Held is registered.
- [ ] AB008 The Line Held uses a documented attacker strength metric.
- [ ] AB009 Its player begins as a non-major and factionless.
- [ ] AB010 Its capital and marked core border states remain held.
- [ ] AB011 Its independence and faction restrictions are enforced.
- [ ] AB012 Breach the Unbreachable is registered.
- [ ] AB013 It requires Study the Breach and a stored high-fort target.
- [ ] AB014 It uses a continuous land-objective sequence.
- [ ] AB015 It prevents peace-transfer and third-party capital shortcuts.
- [ ] AB016 It completes within the 180-day offensive window.
- [ ] AB017 Last Redoubt is registered.
- [ ] AB018 Last Redoubt requires at least 600 Chaos and concrete Fortress World access.
- [ ] AB019 It requires a sufficiently large core-state base.
- [ ] AB020 It arms below the accepted core VP control threshold.
- [ ] AB021 It tracks capital and linked supply redoubt for 180 days.
- [ ] AB022 It requires recovery to the accepted core VP share.
- [ ] AB023 Every achievement suppresses debug, console, and manual-event shortcuts.
- [ ] AB024 Every challenge state survives save and reload.
- [ ] AB025 Every failed challenge cleans up.
- [ ] AB026 Every completed achievement cleans temporary tracking state.
- [ ] AB027 Every achievement has final title, description, icon triplet, and documentation.
- [ ] AB028 No achievement unlocks merely because Event 064 fired.

## AC. Catalog and documentation

- [ ] AC001 Authoritative event workbook row 064 is corrected.
- [ ] AC002 Unrelated leader-trait detail is removed from row 064.
- [ ] AC003 Details field describes global frontier fortification.
- [ ] AC004 Evolution I field describes Defense in Depth.
- [ ] AC005 Evolution II field describes Fortress States.
- [ ] AC006 Evolution III field describes Fortress World.
- [ ] AC007 Type is Minor Repeatable.
- [ ] AC008 Chaos level is 1.
- [ ] AC009 Primary cluster is Sudden Abundance.
- [ ] AC010 Additional cluster is Military Preparation.
- [ ] AC011 Member severity is Medium in each cluster.
- [ ] AC012 Workbook uses its accepted multi-cluster structure.
- [ ] AC013 CSV exports are regenerated through `.tools/export_event_catalog_csv.py`.
- [ ] AC014 Event export reflects corrected row 064.
- [ ] AC015 Cluster export reflects both memberships.
- [ ] AC016 All catalog exports come from the same authoritative workbook revision and pass schema comparison.
- [ ] AC017 Permanent Event 064 overview is created or updated.
- [ ] AC018 Overview documents baseline, evolutions, decisions, AI, Chaos, clusters, achievements, assets, and tests.
- [ ] AC019 Event-system registry docs are aligned.
- [ ] AC020 Cluster-system docs are aligned.

## AD. Static and task-specific validation

- [ ] AD001 Event syntax passes.
- [ ] AD002 Decision syntax passes.
- [ ] AD003 Mission syntax passes.
- [ ] AD004 Trigger and effect references resolve.
- [ ] AD005 Building types resolve.
- [ ] AD006 Modifier types resolve.
- [ ] AD007 Localisation keys resolve.
- [ ] AD008 Sprite names resolve.
- [ ] AD009 Achievement ids resolve.
- [ ] AD010 No duplicate event ids exist.
- [ ] AD011 No duplicate scripted names exist.
- [ ] AD012 Normal two-country border scenario passes.
- [ ] AD013 Multi-neighbor province dedupe scenario passes.
- [ ] AD014 Allied border scenario passes.
- [ ] AD015 Subject and overlord scenario passes.
- [ ] AD016 Active war-front scenario passes.
- [ ] AD017 Civil-war scenario passes.
- [ ] AD018 Occupation scenario passes.
- [ ] AD019 Enclave scenario passes.
- [ ] AD020 Strait-only exclusion scenario passes.
- [ ] AD021 Island baseline scenario passes.
- [ ] AD022 Island Fortress World scenario passes.
- [ ] AD023 Tiny-country scenario passes.
- [ ] AD024 Large-continental-country scenario passes.
- [ ] AD025 High-existing-fort scenario passes.
- [ ] AD026 Each evolution alone passes.
- [ ] AD027 All evolutions together pass.
- [ ] AD028 Higher evolution with lower disabled passes.
- [ ] AD029 Repeated wave after border change passes.
- [ ] AD030 Cluster selected-root route passes.
- [ ] AD031 Cluster queued-member route passes.
- [ ] AD032 Multi-cluster arbitration passes.
- [ ] AD033 No duplicate cluster execution is proven.
- [ ] AD034 Save-load during each project passes.
- [ ] AD035 Target loss during each project passes.
- [ ] AD036 Annexation cleanup passes.
- [ ] AD037 Every achievement start and fail route passes.
- [ ] AD038 Every achievement completion route passes.

## AE. Performance and final review

- [ ] AE001 Representative late-game world test is run.
- [ ] AE002 Many-country world pass processes each country once.
- [ ] AE003 Province dedupe holds on complex borders.
- [ ] AE004 Evolved candidate sets remain bounded.
- [ ] AE005 No recurring background world scan exists.
- [ ] AE006 Temporary arrays and variables return to clean state.
- [ ] AE007 Save size impact is reviewed.
- [ ] AE008 Event execution cost is reviewed.
- [ ] AE009 Response category does not create excessive decision clutter.
- [ ] AE010 AI project evaluation remains country-local and bounded.
- [ ] AE011 Achievement checks remain player-local and bounded.
- [ ] AE012 Early-war stalemate risk is tested.
- [ ] AE013 Breach counterplay is tested against levels three, five, seven, and eight.
- [ ] AE014 Project affordability is tested for small, medium, and large countries.
- [ ] AE015 Direct Chaos gain is tested against repeated and no-op waves.
- [ ] AE016 `chaosx_improvement_loop_planner` is spawned near completion with `fork_context=false`.
- [ ] AE017 Any accepted improvement addendum is resolved.
- [ ] AE018 A closure handoff is recorded when no further depth change is needed.
- [ ] AE019 `chaosx_event_completion_auditor` receives all evidence.
- [ ] AE020 Final completion report lists every blocker, omission, fallback, and skipped validation.
- [ ] AE021 Completion is withheld while mandatory probability evidence is unavailable.
- [ ] AE022 Completion is withheld while either accepted cluster membership is missing.
- [ ] AE023 Completion is withheld while assets or localisation use placeholders.
- [ ] AE024 Completion is withheld while the authoritative catalog remains stale.
