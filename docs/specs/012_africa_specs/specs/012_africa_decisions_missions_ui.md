# Event 012 — Decisions, Missions, Mechanics, and UI

## Core gameplay loop

The Africa event should play through a living Congress system, not a static decision store. The player is managing a continental claim while trying to turn paper cores into real administration, protect African countries from colonizers, keep a faction together, and decide whether integration is federal, revolutionary, military, traditional, or high-chaos supernatural.

The loop is:

1. Choose a regional priority.
2. Build legitimacy and authority through missions, focuses, victories, and aid.
3. Offer protection or charter membership to African countries.
4. Fight colonial holders or support African states already fighting them.
5. Release or strengthen regional authorities instead of direct-annexing everything.
6. Pressure regional authorities and members toward integration.
7. Manage resistance, cohesion, colonial alarm, and paper-core burden.
8. Complete Africa Is One.
9. Survive the Second Scramble.
10. Become a world-chaos pole and sponsor continent unifiers.

## Visible mechanic values

| Value | Public meaning | Increases from | Decreases from | Unlocks / consequences |
| --- | --- | --- | --- | --- |
| Continental Legitimacy | Belief that the unifier can speak for Africa. | Liberation victories, federal bargains, old-crown ceremonies, diaspora return, successful aid, recognition. | Failed wars, forced annexations, member revolts, low stability, lost capitals. | Peaceful integration, member acceptance, diaspora return, Africa Is One, post-unification recognition. |
| Congress Authority | Ability to make decisions stick. | Statebuilding focuses, military route, capital control, rail and port missions, regional offices. | Overextension, fractured congress, low stability, regional resistance. | Faster integration, stronger ultimatums, forced protectorates, crisis control. |
| Charter Cohesion | Willingness of League members to remain. | Federal route, successful defence, fair aid, shared victories, member votes. | Aggressive pressure, abandoned members, ideological conflict, foreign infiltration. | Faction stability, shared decisions, common war plans, member integration. |
| Liberation Momentum | Practical success against colonial holders. | Winning wars, sending aid, cutting colonial supply, completing liberation missions. | Stalemates, failed ultimatums, lost member wars, low equipment. | New war plans, volunteer routes, anti-colonial uprisings, stronger Africa-wide units. |
| Regional Trust | Per-region acceptance of integration. | Regional authorities, local investment, protected status, low resistance, autonomy deals. | Forced annexation, garrison abuse, unmet promises, route mismatch. | Regional integration, reduced paper-core burden, special regional branches. |
| Colonial Alarm | External panic and counterpressure. | Cores/claims, ultimatums, annexations, high-chaos powers, Second Scramble triggers. | Recognition, slow federalism, diplomacy, colonial-holder defeats. | Sanctions, interventions, Scramble conference, naval blockade, great-power coalition. |
| Paper-Core Burden | Administrative cost of claiming land before governing it. | Uncontrolled or unintegrated African cores, war devastation, resistance. | Integration missions, regional authorities, infrastructure, legitimacy. | Stability, consumer goods, compliance, supply, resistance, faction confidence. |
| Covenant Pressure | High-chaos supernatural/nature pressure. | Green Covenant route, disaster ultimatums, nonhuman pacts, mythic unit use. | Suppression, ritual controls, federal/legal route choices, low chaos. | Weather/disaster tools, nonhuman allies, diplomatic fear, world-threat risk. |

Values should be displayed through scripted localisation in the decision category and custom UI. The player should see at least current value, trend, and top causes for each major value.

## Decision categories

### Category 1 — Continental Congress

The main category appears immediately after the proclamation. It shows the value summary and opens the custom Congress interface.

Core decisions:

| Decision | Availability | Cost model | Result | AI notes |
| --- | --- | --- | --- | --- |
| Call Regional Delegates | Start; repeat with regional cooldown. | Political work plus trains/convoys if region is distant; stability risk if overused. | Raises Legitimacy and Regional Trust in chosen region; may reveal a regional authority option. | AI uses for adjacent or controlled regions first. |
| Survey Paper Cores | Start; once per region. | Civilian factory days, trains, political work. | Reveals integration requirements and lowers Paper-Core Burden slightly. | AI prioritizes controlled regions with high resistance. |
| Establish Congress Office | Controlled or protected regional capital. | Support equipment, manpower, civilian factory burden. | Creates regional administrative progress; unlocks missions. | AI uses if stable and has equipment. |
| Publish Charter Draft | Legitimacy threshold or focus. | Political power plus cohesion risk if route contradicts members. | Sets route tone; improves invitations. | AI uses when it has at least two potential members. |
| Emergency Authority Decree | Low Authority or war. | Command power, stability, legitimacy cost. | Raises Authority quickly; hurts Cohesion/Trust. | Military AI uses; federal AI avoids. |
| Open Congress Interface | Always for human unifier. | None. | Opens scripted GUI. | AI has equivalent scripted effects. |

### Category 2 — Charter League Diplomacy

This category manages African countries before conquest.

Decision families:

| Family | Player action | Dynamic costs and risks | Outcomes |
| --- | --- | --- | --- |
| Observer invitations | Invite African countries to observe the congress. | Cost lower with Legitimacy and proximity; higher if ideological mismatch or in another faction. | Observer status, future membership, small trust. |
| Protection offers | Offer protection to African countries threatened by colonial holders. | Convoys, equipment, relations, route access. | Protected member, defensive call rules, colonial alarm. |
| Aid a country fighting a colonizer | Send volunteers, equipment, officers, engineers, medical teams, air support. | Equipment, command power, army XP, convoys, fuel, foreign access. | Raises Momentum and Cohesion; if abandoned, lowers both. |
| Charter membership | Invite full faction membership. | Legitimacy, trust, ideological compatibility, war state. | Member joins; becomes eligible for integration pressure. |
| Member confidence mission | Timed objective to defend, supply, or support a member. | Requires units, aid, port/rail routes, or local victories. | Success raises Cohesion; failure can make member resistant. |
| Anti-puppet clause | Demand a member refuses external puppet pressure. | Political power, legitimacy, relations; high risk if foreign patron strong. | Blocks foreign influence or starts diplomatic crisis. |
| Expel infiltrators | Counter foreign-backed faction in member state. | Intelligence exposure, command power, support equipment. | Lowers foreign influence; can hurt trust if heavy-handed. |

Current implementation note: full members and protected members use separate aid target arrays through `africa_send_league_aid` and `africa_send_protected_league_aid`. Both start `africa_member_confidence_mission` when aid is sent to a Charter-side country that is already at war and no other confidence mission is active. The mission stores that member as the active target; success requires the target to stay in the Charter relationship, avoid capitulation, and finish the war before the deadline. Failure raises Colonial Alarm and lowers League Cohesion. Higher-commitment aid corridors are split into `africa_open_member_aid_corridor` and `africa_open_protected_aid_corridor`; they spend command power, support equipment, convoys, and trains, grant the target manpower and logistics stockpiles, set one active target cap, and resolve through `africa_aid_corridor_mission`. Bestiary-warning defiance now calls `africa_apply_bestiary_warning_defiance_package_pressure`, so unlocked high-chaos systems add route-specific value pressure instead of only the generic defiance penalty. The sponsor layer now uses `africa_continent_sponsor_readiness_mission` before `AFR_africa_is_one`, then requires four route-specific external proof decisions after the dynamic cross-continent union. Those proof decisions require matching external continent world-end readiness flags before World Is One certification can set the shared readiness flag.

Current GUI implementation note: `africa_continental_congress_scripted_gui` is attached to `africa_continental_congress_category` and has click handlers for Congress, Register, Dossier, Sponsor, Seats, and Terms buttons. The panel includes live regional-seat and Bestiary-seat cards, selected dossier/seat/profile status, survey and Archive guard status, regional/liberation/return/Bestiary operation status, and a warning docket. It spends PP/resources, calls existing Event 012 helpers, and sets timed recent-action flags for exploit protection. It also wires the Charter banner, Authority Atlas seal, and Bestiary warning seal as static fallback sprites with route-gated animated overlays. This resolves the display-only state for core actions and adds first visible target-card and animation surfaces, but it does not yet implement full region/member/dossier card lists or per-target GUI selection.

### Category 3 — Liberation War Office

This category handles anti-colonial war and external holders of African states.

Decision families:

| Family | Player action | Dynamic costs and risks | Outcomes |
| --- | --- | --- | --- |
| Colonial ultimatum | Demand a colonial holder release, transfer, or negotiate over African states. | Legitimacy, Authority, army readiness, colonial alarm. | Acceptance transfers/releases states; refusal grants war goal and raises alarm. |
| Border incident | Support local uprising or border clash. | Equipment, command power, intelligence exposure, member trust. | Creates claims, weakens colonial control, can backfire. |
| Open aid corridor | Build land/sea/air route to a protected African country. | Convoys, trains, fuel, ports/rail, civilian factories. | Enables stronger aid and missions. |
| Sabotage colonial logistics | Route-specific sabotage against ports, rail, depots. | Intelligence exposure, local support, equipment. | Weakens holder; raises alarm. |
| Recognize liberated authority | Create regional authority in liberated states. | Legitimacy, support equipment, local support. | Subject/faction authority appears; lowers paper-core burden. |
| Postwar settlement | Decide fate of conquered African states. | Authority, Trust, compliance, resistance, route. | Direct integration, regional authority, protectorate, federation, or occupation. |

Current implementation note: the Liberation War Office has operation prep, border columns, rail-belt preparation, external-holder case refreshes, Scramble treaty settlement, and a state-targeted front-objective decision. `africa_secure_liberation_objective_state` targets controlled African front states through map mode, spends support equipment, manpower, and command power, improves infrastructure, raises Liberation Momentum and Regional Trust, and records the secured state. `africa_liberation_front_deadline_mission` now requires border columns, rail-belt offices, and the configured number of secured front states while the Charter is at war. Mission cancel, success, and timeout all call `africa_clear_liberation_objective_progress`, so retrying the mission cannot reuse old secured-state flags or objective counts.

### Category 4 — Regional Integration

This is the main anti-snowball category. It turns claimed land into usable land.

For each region, the player should see a curated set of actions only when relevant. Do not display every African state at once.

Integration steps:

1. **Survey.** Identify regional capitals, rail hubs, ports, resistance, local authority.
2. **Secure.** Hold key states and keep supply connected.
3. **Administer.** Spend equipment, manpower, civilian factories, and political work to build local offices.
4. **Recognize or federate.** Choose regional authority, protectorate, member state, or direct administration.
5. **Integrate.** Complete missions, lower resistance, and raise Regional Trust.
6. **Finalize.** Remove paper-core penalties in that region and unlock regional branch rewards.

Mission types:

| Mission | Requirement | Duration | Success | Failure |
| --- | --- | --- | --- | --- |
| Hold the Regional Capital | Own/control named regional capital and keep supplied divisions there. | 120–180 days depending on resistance. | Trust + Authority; unlock next step. | Resistance rises; trust falls. |
| Secure the Rail and Port Corridor | Control named rail hubs/ports and maintain supply. | 150–210 days. | Paper-core burden down; construction decisions cheaper. | Supply penalties and colonial infiltration. |
| Staff the Local Offices | Spend support equipment, manpower, civilian factory burden. | 90–150 days. | Administration progress. | Corruption/unrest event. |
| Regional Congress Vote | Requires Legitimacy and low resistance. | 90 days. | Peaceful integration/federation. | Resistant-member flag or autonomy demand. |
| Garrison Without Breaking It | Place divisions but avoid harsh crackdown. | 120 days. | Resistance down without trust collapse. | Military route may succeed but trust falls. |
| Build the First Continental Road | Infrastructure/rail construction in region. | 180–365 days. | Industry and integration boost. | Cost overrun; Paper-Core Burden temporarily up. |

Current implementation note: the Authority Atlas uses `africa_selected_dossier_survey_mission` as the first timed old-seat survey objective. `africa_open_next_historical_dossier` funds the survey and consumes support equipment; the mission opens and surveys the selected dossier only if its representative old-seat state remains secured. Failure raises Restoration Debt and Local Sovereignty pressure and leaves the dossier available for a retry. The active dossier belongs to one of eight visible profiles: Nile/Red Sea, Maghreb/desert, Sahel charter, western crowns, central river, Great Lakes, Indian Ocean, and southern stone seats. Survey success, local office work, old-seat guards, observer settlement, protected-seat settlement, regional-office settlement, and direct Archive settlement apply profile-specific value movement while preserving the selected-dossier flow; settlement requires the selected dossier to have both its own local office and old-seat guard. Settlement also applies one value-only, once-per-dossier outcome through `africa_apply_selected_dossier_specific_settlement_effects`, with all 32 historical dossier IDs mapped to public settlement summaries through `GetAfricaSelectedDossierSettlementSummary`. Direct Archive settlements also start `africa_direct_archive_seal_mission`, which requires Legitimacy, Old-Seat Legitimacy, and Restoration Debt to stay inside the proof thresholds. Success proves the seal and relieves debt; failure exposes a counterfeit-claim crisis, raises Colonial Alarm, and uses the Counterfeit Crowns super-event surface. Settled dossiers can also start a stored-context resistance watch: observer and protected-seat settlements can commit timed Congress mediation with support equipment, manpower, and profile logistics, while regional-office and direct Archive settlements can commit timed enforcement with rifles, support equipment, manpower, command power, and profile logistics. Profile logistics require convoys, trucks and army experience, infantry escorts, or trains according to the stored resistance dossier profile. Those interventions use the stored resistance dossier id and seat state, not the next selected dossier, block further dossier settlement while active, and resolve through settlement-mode and profile-specific value effects plus visible local reports. The category header uses `GetAfricaSelectedDossierSeatName`, `GetAfricaSelectedDossierSettlementSummary`, and all four settlement fork counters so no selected dossier shows a clear fallback rather than an empty state label.

### Category 5 — Diaspora Return Offices

Unlocks through focus. It should include route-specific versions.

Decision families:

| Family | Requirements | Costs | Results |
| --- | --- | --- | --- |
| Afro-American Delegation | Port access, stability, Legitimacy. | Convoys, civilian factory burden, political work. | Advisors, engineers, doctors, pilots, volunteer cadres. |
| Caribbean Volunteer Route | Atlantic port, convoys, recognition. | Convoys, fuel, diplomatic pressure. | Naval/port bonuses, volunteer units, intelligence networks. |
| Exile Professors and Engineers | Stability and industry branch. | Consumer goods burden, political work. | Research bonuses, construction advisors. |
| Returnee Settlement Councils | Controlled integrated region. | Civilian factories, support equipment, stability risk. | Manpower and skill growth; reduces backlash. |
| Diaspora Guard Cadres | War, equipment, training capacity. | Infantry/support equipment, manpower, army XP. | Specialized volunteer divisions; limited by cooldown and ports. |

### Category 6 — Green Covenant and High-Chaos Reports

Hidden until high-chaos branch unlocks.

Decision families:

| Family | Requirements | Costs | Results |
| --- | --- | --- | --- |
| Read the Weather Before the Treaty | Covenant route or event; colonial target. | Legitimacy, ritual/cultural authority, time. | Predicts disaster chance and target reaction. |
| Storm Ultimatum | High Covenant Pressure and Colonial Alarm. | Stability, Legitimacy, global chaos, possible civilian harm risk. | If colonialist refuses, natural disaster may hit a strategic state; backfire possible. |
| Ananse Wire Network | Intelligence route. | Civilian factories, spies/intelligence exposure where supported. | Sabotage, misinformation, member-infiltration detection. |
| Mami Wata Tide Warning | Coastal/river regions. | Port control, legitimacy, time. | Predicts floods/storms, protects ports, can disrupt enemy convoys. |
| The Great Herd Musters | Elephant unit route. | Support equipment, manpower, supply, Covenant Pressure. | Elephant logistics/special units; high supply cost. |
| Parley with the Forest | Congo Basin high-chaos. | High legitimacy or covenant route; no harsh occupation in Congo. | Nonhuman forest guardian pact; otherwise risk forest revolt. |

## Custom UI — Continental Congress Interface

### Purpose

The interface should help the player manage values, regions, members, integration, and the Second Scramble. It should not be decorative only.

### Entry point

- Button in Continental Congress decision category.
- Optional event log detail button if the event details UI can support it.

### Layout

| Panel | Content |
| --- | --- |
| Header | Current Africa identity, selected unifier flag/cosmetic name, route emblem, leader/council portrait. |
| Value bar | Legitimacy, Authority, Cohesion, Momentum, Colonial Alarm, Paper-Core Burden; each with tooltip breakdown. |
| Regional map/list | Ten region cards with status: unclaimed, claimed, occupied, protected, authority, integrated, resistant, high-chaos. |
| Member board | African observers/members/authorities, influence, trust, risk of exit, integration stage. |
| Colonial alarm board | Top external holders, alarm contributions, sanctions/blockade/intervention risks. |
| Action cards | Contextual actions for selected region or member. |
| Post-unification tab | Hidden until Africa Is One; shows Scramble, continent sponsor, dynamic union names. |
| High-chaos tab | Hidden until Covenant route; shows myth/nature pressure and nonhuman pact states. |

### UI states

| State | Visual cue | Gameplay meaning |
| --- | --- | --- |
| Inactive/locked region | Dim regional card. | No action yet. |
| Claimed paper core | Thin outline, warning paper seal. | Core exists but unintegrated. |
| Active mission | Progress bar and small rail/port/capital icon. | Timed objective underway. |
| Integration ready | Soft glow around regional seal. | Player can integrate/federate/authority. |
| Resistant member | Red warning border or broken charter seal. | Member may leave or revolt. |
| Colonial alarm high | Flashing telegraph/warship warning frame. | External crisis near threshold. |
| Africa Is One ready | Animated continent seal with static fallback. | Final unification focus/decision available. |
| High-chaos active | Subtle particle/weather/covenant animation. | Supernatural route active. |

### Animated asset plan

Animated UI should clarify state and not overwhelm. Candidate animated assets:

| Asset | Size direction | State | Static fallback | Animation note |
| --- | --- | --- | --- | --- |
| `africa_congress_seal_animated` | UI emblem, ~96x96 or existing category size | Interface open and stable. | `africa_congress_seal_static` | Slow paper/gold seal shimmer from real frames. |
| `africa_integration_ready_glow` | Region card overlay | Integration action available. | `africa_integration_ready_static` | Gentle pulse, not transform-only. |
| `africa_colonial_alarm_warning` | Warning frame | Alarm near Scramble threshold. | `africa_colonial_alarm_static` | Telegraph/warship light flicker. |
| `africa_covenant_pressure_animated` | High-chaos tab emblem | Covenant route active. | `africa_covenant_pressure_static` | Storm/leaf/river particles from real frames. |
| `africa_is_one_seal_animated` | Final formable seal | Africa Is One available/completed. | `africa_is_one_seal_static` | Dramatic but readable frame loop. |
| `africa_leader_frame_high_chaos` | Leader portrait frame overlay | High-chaos ruler/council. | `africa_leader_frame_static` | Subtle aura/weather/leaf/drum-shadow frame. |

All final animations require `chaos-redux-frame-animation`: real source frames, sheet DDS, static fallback DDS, GIF preview for review only, frame plan, manifest, and `.gfx`/`.gui` handoff.

### Button actions

GUI buttons must call the same scripted effect families as decisions and AI. They need costs, requirements, tooltips, AI equivalents, and cleanup. Examples:

- Select Region.
- Start Regional Survey.
- Invite Observer.
- Send Aid Package.
- Pressure Member.
- Create Regional Authority.
- Begin Integration Mission.
- Issue Colonial Ultimatum.
- Prepare Scramble Defence.
- Sponsor Continent Unifier.

The UI must close or hide when the unifier dies, tag switches, world-end scenario fires, or event 012 fails.

## Decision pacing and clutter control

The decision system should use phases:

| Phase | Visible decisions |
| --- | --- |
| Opening | Congress office, survey home/adjacent region, first invitations, first war prep. |
| League building | Member invitations, aid, protection, early integration. |
| Regional campaigns | Only active selected region plus emergency member actions; no wall of state decisions. |
| Continental consolidation | Integration missions, resistant member crises, postwar settlements. |
| Africa Is One | Final integration, Scramble preparation, route identity. |
| Post-unification | Scramble crisis, continental sponsor actions, dynamic union names. |
| World-end | World Congress, last borders, terminal path. |

Use an active region selector pattern so the player is not shown hundreds of decisions. AI can evaluate hidden scripted effects separately.

## AI decision behavior

AI Africa unifier should not blindly press every action. It should evaluate:

- Current war and front pressure.
- Equipment, manpower, convoys, trains, and fuel.
- Legitimacy versus Authority route.
- Regional proximity and supply routes.
- Member strength and resistance risk.
- Colonial holder strength.
- Chaos tier and high-chaos route flags.
- Whether the selected route prefers federal, revolutionary, military, crown, or covenant actions.

AI should prioritize:

1. Home-region integration.
2. Aid to African members at war with colonial holders.
3. One colonial war at a time unless very strong.
4. Regional authority creation when overextended.
5. Cohesion repair if members are likely to leave.
6. Scramble defense once Africa Is One is close.

AI should avoid:

- Pressuring strong members with low trust.
- Starting multiple major colonial wars while under-equipped.
- Using high-chaos disaster actions outside high chaos.
- Sponsoring other continent unifiers before Africa is secure.
- Annexing subjects faster than paper-core burden can be managed.

## Cleanup requirements

Cleanup must clear:

- Selected region variables and target flags.
- Stale member targets if country dies, leaves Africa, joins incompatible faction, or becomes nonhuman.
- Active regional missions if region is integrated, lost, or transferred.
- Colonial ultimatum targets if target loses African holdings.
- Diaspora return route targets if port access is lost.
- High-chaos nonhuman pact targets if actor dies or route is abandoned.
- Actor-side Bestiary action flags when the package layer is reset or reseeded.
- Scramble crisis decisions after Scramble victory/defeat.
- World-end path decisions when world_end flag is set.

## Balance expectations

The event is chaos tier 4 and can become absurdly powerful, but it must still ask the player to play. Strong effects are allowed; free unchecked snowballing is not.

- Cores are granted, but paper-core burden makes integration necessary.
- Faction invitations are strong, but cohesion and member resistance matter.
- Liberation wars can be powerful, but colonial alarm rises.
- Regional authorities help administer, but slow direct annexation.
- Elephant and supernatural units are strong, but high-cost and route-limited.
- Diaspora return is useful, but requires ports, stability, convoys, and settlement support.
- Post-unification continent sponsorship is huge, but locked behind Africa Is One and Scramble survival.



## Revision 2 decision expansion: Authority register and disaster-warning loop

The decision/UI layer must support the expanded subject system.

### Authority register category

Add a target-managed authority register rather than showing every authority decision at once. The human player should select a region or authority card, then see current actions for that selected target.

Core actions:

- **Open an Observer** — create a non-map authority office in a controlled/liberated region.
- **Release a Charter Subject** — create or transfer a limited subject/faction member.
- **Merge into Regional Governorate** — fold an authority into a broader regional subject while preserving a local autonomy modifier.
- **Dismiss the Claim** — centralist option that reduces clutter but raises future resistance and high-chaos distortion risk.
- **Guard the Old Capital** — timed mission requiring supplied divisions in named states.
- **Repair the Charter Road** — infrastructure/rail/port/supply mission.
- **Hold the Council** — stability/legitimacy/local-support mission.
- **Integrate the Office** — staged integration mission that turns paper cores/claims into real cores only after trust, supply, and control conditions.

Costs must use equipment, trains, convoys, army XP, legitimacy, local support, stability, administrators, supply, and unit placement. Political power may be one component but not the main cost palette.

### Rival authority category

Some authority pairs create rivalry missions and arbitration events. Buganda/Bunyoro, Kongo/Ndongo/Loango, Oyo/Dahomey/Benin, Aksum/Adal/Ajuran, Swahili/Merina/Sakalava, and Songhai/Bornu/Baguirmi-Wadai should have at least one rivalry or arbitration chain.

### High-chaos disaster-warning category

At Evolution III/IV, Green Covenant actors unlock a warning loop:

1. Select a colonial/extractive target or threatened state.
2. Issue a warning through Orisha, Mami Wata, Barotse, Crocodile, Gorilla, Baobab, Locust, Termite, Bird, Ananse, or Giraffe route.
3. Target can comply, pay cost, retreat, or ignore.
4. If Omen Reliability is high, ignored warnings can trigger floods, lightning, forest ambushes, locust supply collapse, termite subsidence, or port storms.
5. False or overused warnings reduce Omen Reliability and Human Legitimacy.

Current implementation note: `africa_verify_omen_reliability` now commissions `africa_omen_reliability_review_mission` instead of immediately setting verified warnings. The mission checks live Habitat Trust, Bestiary Alarm, and Mythic Volatility thresholds; success sets `africa_omen_reliability_verified`, while failure raises Bestiary Alarm, Mythic Volatility, and Covenant Pressure and keeps Bestiary warnings locked until another review succeeds. The high-chaos decision header shows the current omen review status. All 11 Bestiary packages now map to explicit actor tags for spawn/setup/classification: the original six plus `CTL`, `OKP`, `TRM`, `HGD`, and `GHC`. The expanded actors have generated flags and portraits, their one-time package-operation decisions, and actor-target decisions for Chimpanzee Telegraph relays, Okapi shadow dossiers, Termite Citadel engineers, Honeyguide aid routes, and Great Herds relief columns. Those five actor-target decisions also fire local consequence events `chaosx.nr12.40` through `chaosx.nr12.44` using the targeted actor as a carried event target.

This loop should have AI equivalents and strict safeguards so it cannot become a free damage button.

## Restoration Dossiers and Bestiary Clause decisions

The decisions/UI layer now includes a new **Restoration Dossiers** tab. It sits beside the Charter League and integration controls and is unlocked by the Archive of Old Seats focus lane.

### UI presentation

The player sees a compact dossier board with:

- `Archive Mandate`
- `Old-Seat Legitimacy`
- `Local Sovereignty`
- `Restoration Debt`
- `Mythic Pressure`
- `Nonhuman Sovereignty` when unlocked
- `Bestiary Alarm` when nonhuman or supernatural actors are visible
- selected region filter
- active dossier cap and active mission cap
- warning frame when forgery exposure or nonhuman revolt is close

The board should not show every possible dossier at once. It should use regional pools and a selected-target pattern: choose a macro-region, then show the currently relevant dossiers and missions.

### Decision families

| Family | Unlock | Examples | Requirements/costs |
| --- | --- | --- | --- |
| Open Regional Archive | Archive opener focus. | `Open West African Archive`, `Open Nile Archive`, `Open Swahili Coast Archive`. | Controlled/protected regional states, civilian factory burden, trains/convoys/support equipment as relevant. |
| Survey Old Seat | Regional archive open. | `Survey the Meroitic Court`, `Survey the Kilwa Coral Office`, `Survey the Luba`. | Held target state or protected ally, local support, equipment for escorts. |
| Charter Local Office | Successful survey. | `Charter the Songhai River Authority`, `Charter the Ndongo-Matamba Road`. | Legitimacy, support equipment, local trust, no active refusal. |
| Raise Local Guard | Chartered office. | `Raise River Patrols`, `Call Hill Levies`, `Convert Caravan Guards`. | Manpower, rifles, army XP, supply, local trust. |
| Protect Regalia / Monument | Dossier with monument or symbol. | `Guard the Royal Cemeteries`, `Repair Coral Stone Offices`, `Protect the Great Enclosure`. | Divisions in named states, construction capacity, trains, time. |
| Settlement | Mature dossier. | `Offer Protectorate Charter`, `Grant Observer Seat`, `Begin Integration Settlement`, `Demand Direct Rule`. | League cohesion, local sovereignty, restoration debt, stability/war support tradeoffs. |
| Forgery Crisis | Counterfeit route. | `Silence a Counterfeit Claimant`, `Double Down on the Seal`, `Admit the Archive Lied`. | Intelligence exposure, legitimacy, stability, event risk. |
| Bestiary Clause | High-chaos focus. | `Grant Nonhuman Observer Seat`, `Hear the Baobab Senate`, `Negotiate Forest Autonomy`. | Mythic pressure, habitat/state control, local trust, cooldowns, no predatory extraction. |
| Supernatural Sanction | Evolution IV. | `Ask the Masks to Test the Treaty`, `Let the River Judge the Port`, `Request a Rain Omen`. | Covenant pressure, disaster risk, stability, regional autonomy, long cooldown. |

### Active caps

- Early: 2 active dossiers and 1 active old-seat mission.
- Mid: 4 active dossiers and 2 missions after regional archive focuses.
- Late: 7 active dossiers and 3 missions after continental archive offices.
- High-chaos: nonhuman/supernatural missions count against a separate small cap so the board does not become unreadable.

The implementation should use dynamic caps from constants or documented tuning, not scattered magic numbers.

## Court-name display decisions

A small optional decision family can let the player rotate or publicise source-language court/ruler display names for event-created or recast offices. This should stay a flavour and diplomacy layer, not a large parallel mechanic.

| Decision direction | Purpose | Cost/risk | Result |
| --- | --- | --- | --- |
| Register a court display name | Assign a source-language court/ruler display name from the country-package pool. | Legitimacy, Archive Integrity, translator cooldown, possible stability hit. | Changes public display localisation only. |
| Send the court roll to foreign legations | Turn the untranslated name into a diplomatic incident or propaganda confusion. | Convoys, relations, intelligence exposure, Colonial Alarm. | Foreign report event or temporary diplomatic modifier. |
| Retire a court mask | Return a serious institutional display after backlash. | Legitimacy and local trust checks. | Closes the joke-route display without altering historical source notes. |

The category should not appear in baseline play and should not explain the meaning of the source-language strings.
