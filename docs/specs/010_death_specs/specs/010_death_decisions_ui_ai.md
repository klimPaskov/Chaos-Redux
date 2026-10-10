# Event 010 - Death: Decisions, Containment, UI, AI, and Player Responses

## Decision design overview

Death needs player responses, but those responses should not appear before the world has reason to suspect a crisis. The decision systems are phased:

1. **Pre-reveal local reports**: small, local, low-information decisions for island owners, nearby naval powers, and attentive players.
2. **Reveal containment**: public decisions to declare war, fortify coasts, hold borders, investigate wastelands, and coordinate against Death.
3. **Emergency compact**: shared coalition decisions once Death is a major world threat.
4. **Dark methods**: optional necromancy decisions to fight Death at moral and political cost.
5. **Black Oath**: alternate path to pledge to Zol and join Death's side, with heavy risks.
6. **World-end emergency**: last-stage decisions for continental footholds.
7. **Aftermath**: recaptured wasteland survey, outposts, and one permanent custodial policy after Death is defeated.

The category should not show every possible decision at once.
Visibility is controlled by reveal state, country confirmation, proximity, war state, route flags, compact membership, and active stage.

Death uses ordinary decisions, targeted state decisions, cooldowns, state modifiers, and normal war and occupation gameplay.
Its only mission is the narrow `death_hold_quarantine_line_mission`, started by Strengthen Quarantine Line, which tests whether the country actually keeps a fortified line bordering Death rather than clicking a permanent buff.
Do not add broad goal-style mission stacks or auto-completing objective cards unless a later accepted spec asks for them.
Decision gates use native predicates only when their behaviour is documented; Survey and Outpost therefore require an acting-country-owned division physically present in the selected state, and no Death decision claims a current-supply or supply-connection check.

## Decision categories

| Category ID | In-game title | Who sees it |
| --- | --- | --- |
| `death_missing_island_category` | Missing Island Reports | Countries that received the delayed report pair. Planning name: Maritime Errata. |
| `death_country_containment_category` | Coastal Precautions before the country confirms the case; The Black Country after confirmation or public reveal; Custody of the Empty Land after defeat | Countries with direct border danger, war contact, Compact membership, a confirmed coastal warning, or (before confirmation) an exposed report recipient with an eligible port. It never becomes global. Planning name: The Death Country. |
| `death_black_ledger_category` | Death's Muster | Active DTH only. Planning name: Black Ledger. |

Every price below is a `death_decision_cost` constant paid through the sale-aware Event 026 path, with at most four spendable types per action and at most three shown inline; the full bundle is on hover.

## Decision inventory

| Decision ID | In-game name | Gate | Result |
| --- | --- | --- | --- |
| `death_send_survey_boat` | Send a Survey Boat | Report recipient with a port. Command power, convoys, fuel. | Large case-file gain, confirms the local case, lowers spread pressure. |
| `death_check_telegraph_office` | Check the Telegraph Office | Report recipient. Political power, command power. | Case-file gain, lowers spread pressure. |
| `death_quiet_quarantine_notice` | Issue Harbor Sanitation Notices | Report recipient. Command power, convoys, support equipment, fuel. | Small case-file gain, 90-day quiet quarantine, lowers spread pressure. |
| `death_file_under_weather` | File It Under Weather | Report recipient. Free. | Removes case-file evidence and raises spread pressure; a later report can reopen the file. |
| `death_recognize_death_war` | Declare the Death War | Confirmed or revealed, within the response boundary. Command power, war support. | War with Death. |
| `death_call_living_conference` | Call the Living Conference | Threatened or major country after reveal. Political power, command power. | Forms the Living Compact with this country as leader and invites eligible threatened countries. |
| `death_join_living_compact` | Join the Living Compact | Invited country. Political power. | Membership; raises member count and cohesion. |
| `death_compact_war_declaration` | Compact War Declaration | Compact leader. | Every eligible member inside the danger area enters the war; others are skipped. |
| `death_joint_coastal_patrol_plan` | Joint Coastal Patrol Plan | Compact or coastal responder. Command power, fuel, convoys, support equipment. | Watch network +2, raising forced sea-jump costs; a strong network can intercept one low-pressure coastal jump. Lowers spread pressure. |
| `death_keep_port_lit` | Keep the Port Lit | Coastal controlled state, before or after reveal. Command power, convoys, a major fuel stockpile. | 120-day Coastal Watch on the state: ordinary hidden coastal jumps cannot select it, watch network +1, and the state counts toward The Last Ferry if Death later consumes it. |
| `death_strengthen_quarantine_line` | Strengthen Quarantine Line | Controlled state bordering an active wasteland. Command power, infantry equipment, support equipment. | 120-day line that removes the state from wither targets and eases local supply; starts the hold-line mission. |
| `death_hold_quarantine_line_mission` | Hold the Quarantine Line | Started by the decision above. | Holding to timeout lowers spread pressure; losing every line first raises it. |
| `death_authorize_wasteland_entry_gear` | Authorize Wasteland Entry Gear | At war with or bordering Death. Army experience, support equipment, trucks, fuel. | Temporary national wasteland-entry modifier. |
| `death_share_wasteland_entry_gear` | Share Wasteland Entry Gear | Compact member. Command power, support equipment, trucks, fuel. | Gear for Compact members. |
| `death_last_shores_response` | Last Shores Response | World-end. Command power, army experience, fuel, trucks. | 180-day emergency response; marks the country as a responder for Black Tide Reversed. |
| `death_open_black_atlas` | Open the Black Atlas | Human player after public reveal while Death is undefeated. Free. | Opens the four-tab dashboard; zero AI weight. |
| `death_survey_the_wasteland` | Survey the Wasteland | Living-controlled recaptured state with the actor's own division present. Army experience, support equipment, trucks. | Surveyed Dead Zone, 180-day entry gear, custodial capacity once per state. |
| `death_build_dead_zone_outpost` | Build the Dead-Zone Outpost | Surveyed recaptured state with the actor's own division present. Army experience, support equipment, trucks, trains. | Permanent outpost modifier and custodial capacity once per state; restores nothing. |
| `death_select_sealed_exclusion`, `death_select_memorial_stewardship`, `death_select_transit_custodianship`, `death_maintain_transit_custodianship` | Custodial policies | After defeat, on an outposted state. Custodial capacity (Transit also support equipment, trucks, fuel). | One permanent policy per state; see the custodial addendum below. |
| `death_open_black_book`, `death_bind_the_unburied`, `death_interrogate_empty_road`, `death_seal_names_in_iron`, `death_close_black_book`, `death_burn_black_book` | Dark Methods | See the Dark Methods section. | |
| `death_whisper_to_zol`, `death_take_black_oath`, `death_offer_prison_census`, `death_open_dead_port`, `death_feed_border_to_death`, `death_break_black_oath`, `death_form_black_apostolate` | Black Oath | See the Black Oath section. | |
| `death_consume_another_island`, `death_press_to_mainland`, `death_raise_passive_hosts`, `death_raise_hollow_hosts`, `death_raise_last_shore_hosts` | Death's Muster | See the Death's Muster section. | |
| `death_hide_port_lit_decisions`, `death_show_port_lit_decisions` | Port list toggle | Human player. | Hides or shows the per-state Keep the Port Lit list. |

### Planned concepts that were never built

These appeared in the original planning tables under several overlapping names.
They are not part of the implemented scope; each keeps the disposition shown.

| Planned concept (all names used) | Nearest implemented surface | Disposition |
| --- | --- | --- |
| Open Coastal Watch Stations, Seal the Empty Port, Fund the Watch Network | Keep the Port Lit and the Joint Coastal Patrol Plan | superseded by those two decisions |
| Fortify the Quarantine Line, Guard the Dead Road | Strengthen Quarantine Line and its mission | superseded |
| Issue Wasteland Entry Orders, Send Wasteland Entry Gear | Authorize and Share Wasteland Entry Gear | superseded |
| Establish a Dead-Zone Outpost | Build the Dead-Zone Outpost | superseded |
| Flood the Shore Roads, Burn the Approach Roads | none | unresolved; self-sabotage of a country's own logistics duplicates what withering already does and is not recommended |
| Hold the Census Posts | none (the Counted Every Name achievement uses census participation flags) | unresolved |
| Open Military Access Corridors, Authorize Compact Access | none | unresolved; belongs to the queued Living Compact obligations tranche |
| Coordinate Border Relief | Share Wasteland Entry Gear | unresolved; belongs to the queued Living Compact tranche |
| Mark Low Islands for Evacuation, Emergency Refugee Shipping | none | unresolved; replacement through a Migration-owned evacuation request is an open proposal in the package README |

## Living Containment Compact

This is a coalition/compact layer.
It can coexist with existing factions; the system should not break major alliance structures just to force a new faction.

Compact goals:

- coordinate war entry.
- reduce coastal jump risk through patrol networks.
- fund wasteland-entry gear.
- mark threatened states.
- prevent AI countries from ignoring a revealed Death neighbor.

Compact values:

| Value | Meaning | Rules that read it |
| --- | --- | --- |
| `global.death_compact_members` | Number of members. | The Living Conference achievement. |
| `global.death_compact_cohesion` | Willingness of members to cooperate. | Only the Living Conference achievement predicate and the Atlas Compact row. |
| `global.death_watch_network` | Coastal detection and patrol coverage, capped at `death_decision_tuning.watch_network_max_strength`. | Each point raises Death's forced island and mainland sea-jump soul costs; a strong network can intercept one ordinary low-pressure coastal jump by spending strength; at maximum, ordinary sea jumps are blocked unless Death has No Ferry Returns, pressure is high, or world end has begun. |
| `global.death_front_readiness` | Planned as the ability to occupy Death without withering away. | Only the Black Atlas display; no gameplay rule reads it. |

The planning text also described a `public_panic` value and failure states (low cohesion refusing war entry, panic raising stability costs, poor readiness bleeding offensives, ideological rivals trading accusations).
None of these is implemented.
They remain the substance of the queued Living Compact obligations tranche, and the package README records the proposal to give readiness and cohesion real consumers or remove them from view.

### Dark Methods: Necromancy Against Death

This branch should be useful, frightening, and optional. It should never be the clean best answer.

Implementation status: implemented as living-country containment decisions using `death_black_method_exposure`, `death_bound_names`, and `death_mourning_debt`. The route creates weak capped bound-shade hosts, exposes Black Book offices to scandal pressure, and can be closed for free if the country has only opened the book. After a forbidden method has been used, the route is closed through `Burn the Black Book`.

Unlock conditions:

- Death revealed.
- country at war with Death or controls a recaptured wasteland.
- high casualties, high chaos, or completed black-book investigation.
- not already Herald of Zol.

Values:

| Value | Meaning |
| --- | --- |
| `death_black_method_exposure` | How visible the country's forbidden work has become. |
| `death_bound_names` | Resource used to raise or reinforce anti-Death spectral units. |
| `death_mourning_debt` | Political/spiritual cost that can trigger backlash. |

Decisions:

| Decision | Cost/requirement | Result | Risk |
| --- | --- | --- | --- |
| `Open the Black Book` | Political power, stability; at war with Death or controlling a recaptured wasteland. | Unlocks the forbidden decisions and the Black Book offices spirit. | Raises exposure. |
| `Bind the Unburied` | Army experience, support equipment, manpower. | Creates one weak, capped Bound Shade division that resists wasteland attrition better. | Raises exposure and mourning debt. |
| `Interrogate the Empty Road` | Black Book open, enough exposure, and no prior inquiry; political power and command power. | Reports currently available coastal or land-withering routes and the pressure band; it does not predict a next state. It also raises the watch network and lowers spread pressure. | Raises exposure. |
| `Seal Names in Iron` | Living-controlled recaptured wasteland bordering active Death land, with a separate 180-day state cooldown; 35 political power, 150 support equipment, 3 trains. | Blocks Death's border wither in the selected state for 120 days, reduces Black Book exposure by 2 and mourning debt by 1. | Raises spread pressure by 2 if Death retakes the state while the seal holds. |
| `Close the Black Book` | Book opened but no forbidden method used. Free. | Closes the route. | None. |
| `Burn the Black Book` | Only after using dark methods; political power. | Removes the branch and the Black Book spirits. | Burning before high exposure is part of the Book Burner achievement. |

AI should use dark methods only when desperate, authoritarian, high chaos, or on the edge of collapse. Democracies should generally avoid it unless Death is at world-end and no normal route remains.

### Black Oath: Joining Death

The alternate join-Death path should be playable but dangerous. It is not a normal alliance with Death.

Implementation status: implemented as the Herald route. `Whisper to Zol` prepares the route, `Take the Black Oath` applies the Herald of Zol cosmetic identity and Black Oath idea, Herald service decisions manipulate name debt/black favor/living disgust, and Black Apostolate is a hidden player-only culmination after world-end thresholds.

Unlock conditions:

- Death publicly revealed.
- country borders Death, is losing a war against Death, or controls a recaptured wasteland.
- high chaos or severe instability.
- player choice, or extreme AI desperation.
- country is not a special nonhuman country.

Core rule: a Herald is not safe. It is merely not first.

Black Oath values:

| Value | Meaning |
| --- | --- |
| `death_name_debt` | What the country owes Zol. If it rises too high or goes unpaid, Death can consume Herald states. |
| `death_living_disgust` | Diplomatic hostility from non-Herald countries. |
| `death_black_favor` | Temporary power gained from serving Death. |

Decisions:

| Decision | Cost/requirement | Result | Risk |
| --- | --- | --- | --- |
| `Whisper to Zol` | Political power, stability; high chaos or near the Death border. | Opens the oath route and adds black favor. | Living disgust rises. |
| `Take the Black Oath` | Political power, stability, war support; leaves the Compact. | Country becomes Herald of Zol; super-event `66`. | War with containment members, name debt begins. |
| `Offer a Prison Census` | Political power, stability, manpower. | Raises one Herald Census Host and adds black favor. | Raises name debt and living disgust. |
| `Open a Dead Port` | Coastal state; command power, convoys, fuel. | Marks a temporary Dead Port, adds black favor, and may trigger a Death coastal jump. | Raises name debt; Death may consume the port later. |
| `Feed the Border` | Non-capital controlled state bordering an active wasteland (any coastal state after world-end); command power, political power, stability, manpower. | The state is consumed through the shared consumption effect; large black favor and name-debt relief. | The state becomes a wasteland and its people are erased. |
| `Break the Oath` | Political power, command power, stability. | Rejoins the living side and removes Herald status. | Death targets the traitor aggressively. |
| `Proclaim the Black Apostolate` | Hidden thresholds after world-end; player only. | Black Apostolate cosmetic identity and route culmination. | Permanent isolation; no living-state cores. |

AI should almost never take the Black Oath. It may do so if:

- chaos is very high.
- country is authoritarian or extremist.
- capital is near Death.
- stability is collapsing.
- no allies are helping.
- Death already controls a large part of the continent.

The path should be disabled for AI countries whose survival is essential to another active event unless a valid alternate exists.

## Custom UI: The Black Atlas

Death uses a compact scripted GUI window after reveal. The Black Atlas summarizes the current stage, consumed population, coastal risk, wither-line pressure, compact posture, and forbidden-route exposure without replacing normal map play. It is a transient decision-category dashboard with a native Close button and no standalone decorative status icons; consumed population is displayed in `K`, `M`, or `B` bands.
The parent accepted the four-tab summary under the user's G5/G6 repair authority on 6 October 2026, preserving all existing summary fields while reducing visible values to at most four.

### Entry point

A decision category button: `Open the Black Atlas`.

### Accepted summary tabs

| Tab | Player sees |
| --- | --- |
| Seas | Stage, consumed-state count, consumed-population band and coastal risk. |
| Fronts | Watch current/maximum, jump surcharge and front readiness, counting the two Watch numbers separately. |
| Compact | Quarantine-line status, compact status/cohesion and current footholds. |
| Book | The existing forbidden-office status, only while that context matters. |

Labels and values use aligned native text controls.
Four tab actions and Close keep the view within five navigation choices; the human-only opener hides while open and immediately reopens to Seas after closing.
The larger six-panel map, census, coast, line, compact-members and forbidden-method concept remains an unresolved proposal, not implemented or accepted through this repair.
The current scoped reference, source wiring and blocked production-render proof are recorded in `docs/plans/010_death_plans/subagent_handoffs/final_black_atlas_gui_audit_2026-10-06.md`.

### Information discipline

The UI does not reveal exact hidden next targets.
It shows bands instead: the stage (`No public name`, `Death Country`, `Last Shores`), the coast risk (`watch network holding`, `watch network thin`, `recent jump, lower immediate risk`, `sea jumps blocked by watch network`, `all remaining coasts exposed`), and the line and compact bands.
The planning risk labels `quiet`, `watched`, `thin`, `open`, `critical` and the stage label `Black Continent` were replaced by these implemented bands.

### Animated presentation pass

The Black Atlas receives an animation pass because it represents a living supernatural map threat.

Animated assets (implemented; the earlier GUI inspection reported an unresolved static-fallback link for the animated Atlas header, which remains an open verification item):

| Asset | State logic | Direction |
| --- | --- | --- |
| `death_black_atlas_header_animated` | Visible after reveal. | Slow dark fog drift, generated frame-by-frame, static fallback. |
| `death_zol_portrait_world_end_animated` | World-end or Herald oath. | Void-lit Zol portrait frames, static fallback, and registration in `interface/chaosx_characters.gfx`. |

Animation should clarify state. If a surface becomes too busy, keep only the header and critical warning animation.

## DTH Category: Death's Muster

Death's Muster (`death_black_ledger_category`, planning name Black Ledger) is visible only to active Death.
It is not a living-country intelligence tool.
Its header shows four values (consumed states, consumed population, spread pressure, available soul power); each decision shows its own availability and current cost.
Its decisions are `death_consume_another_island`, `death_press_to_mainland`, `death_raise_passive_hosts`, `death_raise_hollow_hosts` and `death_raise_last_shore_hosts`.

Death's Muster decisions do not spend political power.
They spend soul power, which is generated from consumed states, consumed population, and last-shore footholds after world end begins.
Soul power has no storage cap.
The category can offer island consumption after Second Shore and an island-spread focus, mainland pressure after Mainland Smell when normal pressure or the living-war bypass allows it, and one host-raising decision for the current ghost stage.
Host and spread decisions use the same soul-power budget so manual expansion competes with army growth.
Forced island consumption starts at the base island-spread cost, then each successful Death's Muster island consumption raises the next forced island cost by one soul power.
Successful Death's Muster mainland consumption raises the next forced mainland cost by two soul power.
Each ghost host raised increases later host costs by 0.25 soul power.

The same category must be navigable by AI because Death is usually AI-controlled. AI Death should use island spread while it is still cheap, while it is still building the island pattern and pressure, and while valid empty islands remain. It should prioritize the mainland decision once the route is valid and cheap islands are no longer the better pre-reveal spend, then raise the available host tier when it has a valid spawnable wasteland. It should avoid spending pre-reveal souls on hosts only when those souls are needed for a pending mainland press.

## AI strategy matrix

### Death AI

| Situation | Behavior |
| --- | --- |
| Hidden origin | Do nothing visible. No wars or units. |
| Hidden island spread | Consume low-pop empty islands by scripted pulses and cheap Death's Muster island decisions. Living AI does not choose war decisions while Death has consumed only one island. |
| Reports ignored | Slightly increase spread pressure. |
| Mainland route ready | Spend soul power on the Death's Muster mainland decision before raising hosts unless cheap empty islands are still the better pre-reveal spend. |
| Revealed mainland | Declare war on the revealed state's owner and on neighbours that border a wasteland or recognized a warning, wither unguarded states, use Death's Muster mainland or island actions when valid, and remain passive militarily until ghosts. Wider neighbor wars wait for late-stage strength or world-end. |
| 600 ghost tier | Raise weak ghosts through Death's Muster when a valid wasteland can spawn them and Death is not saving for the mainland route or cheap island spread. Hold lines and avoid offensives. |
| 800 ghost tier | Raise stronger ghosts through Death's Muster, use pressure-driven coastal jumps after setbacks, and keep normal attacks restrained before world-end. |
| World-end | Aggressive attacks, foothold expansion, intensified withering, and repeated Last-Shore host spending from Death's Muster. |
| Near defeat | Attempt coastal jump if cooldown and stage allow. No fake capitulation. |

### Neighbor AI

| Country type | Behavior |
| --- | --- |
| Direct neighbor | Join or request compact, guard border states, declare war if not already at war, and prioritize quarantine decisions after Death has more than one consumed island or has reached the mainland. |
| Island owner | Investigate early reports and keep exposed ports lit after repeated reports or revealed Death. |
| Coastal nearby country | Build watch network, fortify vulnerable ports, join compact if Death on same continent. |
| Major power | Coordinate compact, send equipment, declare if Death reaches mainland or world-end. |
| Minor far away | React only after reveal, world-end, or compact call. |
| Existing faction leader | Prefer compact overlay before dissolving/abandoning existing faction. |
| Democratic AI | High containment participation, low necromancy, almost never Herald. |
| Fascist/communist authoritarian AI | Strong containment if threatened. Dark methods possible under high chaos. |
| Desperate unstable AI | May consider Black Oath only if close to collapse. |

### Herald AI

Herald AI should be rare and unstable. It should:

- feed Death only if black favor is low and name debt manageable.
- avoid sacrificing its capital unless in maximum desperation.
- fight containment countries if already committed.
- consider breaking the oath if Death weakens and living coalition support is nearby.
- never be a reliable normal ally to Death.

### Compact AI

Compact AI should:

- join when Death is revealed and nearby.
- weigh war entry by proximity, strength, ideology, existing war burden, and coastal risk after Death has consumed more than one island.
- prioritize border decisions over generic economy decisions.
- send aid to countries with active Death borders.
- avoid impossible decisions that require absent ports, missing convoys, dead targets, or no route to Death.
- keep some countries from overcommitting if they are already losing a major war.

## Localisation tone

Pre-reveal text: bureaucratic, uncertain, maritime, quiet.

Reveal text: blunt, cold, public recognition.

Containment text: practical and frightened. Governments try to make new categories for something that is not a war.

Necromancy text: grim, euphemistic, self-condemning. Avoid cheap jokes about mass death.

Herald text: cultic but restrained. A government pretends surrender is policy.

World-end text: terminal, spare, no melodramatic filler.

## Exploit and cleanup rules

- No decision should allow infinite free units.
- Bound Shade and Herald Census Host units need real costs and caps.
- Coastal watch should reduce risk, not permanently block Death everywhere. Strong watch-network coverage can intercept an ordinary low-pressure coastal jump once by spending network strength, while high pressure, No Ferry Returns, and world-end pressure bypass that interception.
- Any future evacuation (see the package README open questions) must save only people who actually leave and must route flight through the Migration owner.
- Survey, outpost and custodial projects never restore population.
- Heralds should not become immune to Death forever.
- Black Oath should not allow a player to farm Death bonuses without eventual name-debt consequences.
- Compact membership should clean up when Death is defeated, the country capitulates, or the country becomes Herald.
- Temporary wasteland, outpost, watch, and quarantine modifiers should expire or be removed if the state changes controller, is reconsumed, or Death is defeated.
- All temporary variables used for popup outcomes should be cleared by event options, not by an early generic cleanup if options still need them.

## Implemented case-file and custodial decision addendum (2026-07-11)

The Missing Island Reports category displays the current evidence band and contextual advice.
Existing report, telegraph, quarantine, survey, and weather actions write to the same country ledger.
AI investigations strengthen as evidence moves from fragmentary through pattern and probable; confirmed countries stop treating weather dismissal as a viable response.
Before confirmation, an exposed report recipient sees the containment category as Coastal Precautions and receives only unknown-route port-watch wording; the Black Country title and named exceptions remain behind country confirmation or public revelation, and the Black Atlas opens only after public revelation.

After Death's custom defeat, state-targeted survey and outpost decisions establish the required progression. Three mutually exclusive state-targeted policy decisions then spend custodial capacity inside their shared state effects: Sealed Exclusion for exposed coasts and borders, Memorial Stewardship for secure interior dead zones, and Transit Custodianship for surviving supply-node corridors. Memorial remains selectable per eligible state, but its +3% stability and up-to-2 mourning-debt national reconciliation can fire only once per country. Transit maintenance appears only when its timed maintained-corridor modifier has expired. Selection effects revalidate target and cost so map-target scope cannot grant a free policy.

The Event 010 custodial-capacity cost uses `GFX_death_custodial_capacity_texticon`, registered in `interface/010_death.gfx` and displayed as `£GFX_death_custodial_capacity_texticon`. The asset lives under `gfx/interface/texticons/` and is an 18×18 transparent DDS matching the installed vanilla texticon family. Other decisions reuse the registered survey boat, quarantine line, Living Compact, dead-zone outpost, and wasteland-gear sprites; future art may split them only through the Event 010 asset workflow without renaming gameplay decisions first.
