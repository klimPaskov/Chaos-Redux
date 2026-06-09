# Chaos Redux Implementation Spec: Union Collapse, Communist Spread, Holy Realm Rework, Final Silence, Zombie Raids, and Super-Event Audio

## Purpose

This spec turns the rough request into an implementation-ready task for the Chaos Redux repo. The work is a multi-system update, not a single event patch. It touches event runtime logic, MTTH pacing, focus trees, decisions, scripted GUI settings, balance constants, civil-war handling, world-end logic, population/deaths tracking, super-event audio, focus filters, localisation, docs, and validation.

The implementation must avoid shallow fixes. Whenever a repeated pattern appears, such as crises becoming harder against non-AI countries or focus branches unlocking decision families, create reusable scripted helpers and constants instead of one-off hardcoding.

---

## 1. Soviet Union Collapse: Max Threat Must Force Total Collapse

### Core behavior

When the Soviet Union collapse threat reaches its maximum value, the collapse must become unavoidable.

At max threat:

1. The Union Collapse system enters a forced collapse state.
2. Every valid releasable country inside the Soviet Union is released.
3. If the current chaos tier unlocks special chaos countries, those valid chaos countries are also released.
4. Every released country declares war on the Soviet Union.
5. War declarations do not all happen instantly. They are queued through MTTH events, so the collapse unfolds over time.

### Valid release pool

The release pool must include:

- all existing vanilla or modded releasable tags with valid cores inside Soviet-controlled territory
- all Chaos Redux releasable Soviet-region tags already supported by the repo
- high-chaos special tags whose unlock conditions are met
- historical, regional, or special chaos tags only when their state targets are valid and not already owned by an existing living country that should remain separate

Do not include:

- tags already alive unless the logic is an uprising or expansion into their core states
- tags with no valid core state in the Soviet-controlled release area
- invalid placeholder tags
- tags whose release would leave broken state ownership or no capital
- special chaos tags gated behind a higher chaos tier than the current campaign has reached

### Soviet Union survival target

The Soviet Union tag must remain alive as the enemy target. If releasing every eligible country would leave the Soviet Union with no valid capital or no controlled state, reserve a small emergency remnant around the current capital or scripted fallback capital. This remnant exists so the released countries can actually declare war against the Soviet Union.

### MTTH release and war pacing

Use a queued collapse chain:

- max threat sets `soviet_collapse_forced_total_release_active`
- the system builds or iterates a release queue
- each valid country release schedules a follow-up event
- each follow-up event releases one country or a small regional batch
- after a delay, that country declares war on the Soviet Union
- the MTTH should be shorter at high chaos and when Soviet stability is low
- the MTTH should still prevent all countries appearing and declaring war on the same day

Recommended pacing:

| Condition | MTTH direction |
| --- | --- |
| chaos below high-chaos special threshold | slower, mostly vanilla or already-supported tags |
| high chaos | faster, adds eligible special chaos countries |
| Soviet capital threatened | faster |
| Soviet Union already fighting many collapse states | slightly slower to prevent instant unreadable spam |
| player is Soviet Union | use readable wave pacing and clear warnings |

### Player-facing feedback

Add clear event/log feedback:

- first warning when max threat is reached
- collapse wave reports naming the latest released countries
- event details entry explaining that the union has crossed the point of no return
- final status entry when all valid releases have been processed

---

## 2. Communist Controlled State Spread Rework

### Baseline aggression increase

The communist controlled state spread is currently too weak. Increase its baseline aggression:

- shorter spread intervals
- lower cooldowns
- stronger weighting toward adjacent vulnerable states
- stronger weighting toward states with low stability, low compliance, unrest, war damage, civil war chaos, or nearby communist-controlled states
- more active pressure during major wars and civil wars

The system should remain readable. Do not create constant popups. Prefer state changes, log entries, decision alerts, and periodic reports.

### New reusable mechanic: Non-AI Crisis Pressure

Create a reusable mechanic that makes crisis systems harder when a non-AI country is directly fighting the crisis.

Working name:

`Non-AI Crisis Pressure`

Purpose:

When a human-controlled country is actively opposing a crisis, that crisis should become more aggressive, because the player can react better than the AI. This should not be limited to the communist spread system. It should become a reusable pattern for future crises.

Core effects when active:

- lower spread cooldowns
- higher spread chance
- more frequent crisis actions
- faster escalation of local pressure
- reduced recovery windows after the player clears crisis states
- stronger targeting of front-line or recently-cleared states
- optional extra crisis missions when the crisis has a decision category

Suggested helper design:

- scripted trigger: `chaosx_is_non_ai_crisis_pressure_active`
- scripted effect or factor block: `chaosx_apply_non_ai_crisis_pressure_factor`
- constants for mild, standard, severe, and extreme pressure
- setting flag: `chaosx_setting_non_ai_crisis_pressure_enabled`

### Miscellaneous settings checkbox

Add a checkbox in the miscellaneous settings view:

Display name: `Harder Crises for Players`

Tooltip meaning:

When enabled, major crisis systems become more aggressive when a player-controlled country is actively fighting them. This affects spread frequency, cooldowns, and pressure recovery. AI-only crisis fronts use normal tuning.

Default: enabled unless existing mod settings convention suggests otherwise.

The setting must:

- appear in the miscellaneous view
- persist through the existing settings system
- be readable by scripted triggers
- have localisation and tooltip text
- be easy to reuse for other crisis systems

### Civil war compatibility

Fix communist spread inside civil wars.

The system must work when:

- the original country has split into loyalist and rebel tags
- a civil-war state has a controller different from the owner
- the communist-controlled state is inside one side's territory but adjacent to the other side
- state ownership is unclear due to occupation
- one side is a player and the other is AI

Do not block spread only because a state is part of a civil war. The spread target should be based on current controller, owner, adjacency, and war validity.

Implementation must avoid invalid spread into:

- impassable states
- states without controller
- states outside valid target continents or regions if the event defines a regional limit
- states controlled by special non-standard countries that should be immune under existing Chaos Redux rules

---

## 3. Holy Realm Spam and Balance Fixes

### Refuge relief spam

Fix Holy Realm refuge relief spam.

Required behavior:

- repeated relief events must have target-specific cooldowns
- a country or state should not receive the same relief event repeatedly in a short period
- relief reports should consolidate when several relief actions happen close together
- AI decisions should not spam relief if the target no longer needs relief
- cleanup flags must be removed when the relief situation ends

### Final warning spam

Fix final warning spam.

Required behavior:

- final warning should be once per target or once per escalation stage
- warning should not repeat every tick when nothing changed
- warnings should have target-level memory flags
- final warning escalation should have a clear final state
- old warning flags should be cleaned up when the target is dead, annexed, integrated, or no longer valid

### Chaos-based peace versus silence balance

The Holy Realm should become less able to choose peace as chaos rises.

Implement a chaos-tier scaling model:

| Chaos state | Peace decisions | Final Silence decisions | BOP direction |
| --- | --- | --- | --- |
| low chaos | many peace actions, few silence actions | rare, expensive | peace side stronger |
| mid chaos | peace actions still available but costlier and slower | more visible | contested |
| high chaos | fewer peace actions, stricter cooldowns | common, cheaper, stronger | silence side stronger |
| extreme chaos | peace route mostly defensive and humanitarian | dominant route unless resisted | final silence pressure rises |

The balance of power must reflect this. Peace and Final Silence should not both remain equally available forever.

---

## 4. Holy Realm Focus Tree Corrections

### Mandala Bureau

The Mandala Bureau focus must:

- unlock or create an intelligence agency if the Holy Realm does not already have one
- grant several free intelligence agency upgrades
- unlock or improve intelligence decisions tied to Mandala diplomacy, peace letters, foreign monitoring, and crisis observation
- add agency-themed localisation and focus tooltip text

Suggested free upgrades:

- Cryptology Department or equivalent vanilla-compatible upgrade
- Radio Interception Group
- Invisible Ink or Diplomatic Training
- Passive Defense if the branch is defensive
- Localized Training Centers if the branch sends envoys abroad

Use actual valid upgrade IDs from the repo or vanilla files.

### Focus filter cleanup

Clean Holy Realm focus filter tags.

Required:

- remove filter tags that point to no valid focus
- remove filters from focuses outside the intended branch
- add missing filters to actual focuses in the branch
- make peace, Final Silence, intelligence, diplomacy, intervention, refuge, and Mandala branches easy to filter
- validate the focus filter UI after changes

### The World Is Asked to Kneel

This focus must become a true world conquest pivot.

Effects:

- grant the Holy Realm a claim on every state in the world
- grant war goals on every living country in the world
- do not skip majors, minors, neutral countries, or far-away targets
- exclude only the Holy Realm itself and cases that would be invalid in engine terms
- unlock a decision category to core claimed states later

Core rule:

The new coreable states from this focus must not be registered under the existing `possible_holy_realm_cores` pool. Create a separate global or country-scoped tracking model for these conquest claims and cores. This prevents the normal possible-core system from being polluted.

Suggested decision family:

`Mandate the Kneeling Provinces`

- target any owned and controlled claimed state gained through The World Is Asked to Kneel
- costs scale with population, resistance, compliance, distance from capital, and chaos
- creates a timed integration mission instead of instant free cores for large states
- adds a core only after the mission succeeds
- failure raises resistance, hurts stability, and may create a local revolt event

### Ministry of Silence rename and prerequisites

Rename the focus `Ministry of Release` to `Ministry of Silence`.

Update:

- focus name
- localisation
- descriptions
- event references
- decision references
- docs
- spreadsheet entry if present
- any focus ID if safe, or keep internal ID while changing display name if ID migration is too risky

Prerequisites:

`Ministry of Silence` must require all three branch focuses:

- `The Last Human Signature`
- `Compassion of Nonreturn`
- `A Sermon Without Translation`

Use AND prerequisite semantics. Do not accidentally make them OR prerequisites.

### Final Silence branch ending

`The Last Authorization` must become the final focus of the Final Silence branch.

It must require `Ministry of Silence`.

It should unlock the final decision or event chain that can start the Final Silence world-end scenario.

### 14-day branch focuses with real effects

These focuses must last 14 days and must do real gameplay work:

#### The Last Human Signature

Role: bureaucracy and records are prepared for the Final Silence.

Effects:

- unlock target-list auditing decisions
- add encryption, decryption, or intelligence bonuses
- raise Final Silence BOP pressure
- reduce final warning cooldowns but set proper anti-spam flags
- unlock a report entry showing that administrative records are being converted into target ledgers

#### Compassion of Nonreturn

Role: the Holy Realm frames annihilation as mercy.

Effects:

- unlock evacuation or shelter decisions for Holy Realm states only
- reduce temporary internal resistance or war exhaustion
- increase global condemnation or foreign fear
- make peace decisions less available at high chaos
- add a timed modifier to prepare protected Holy Realm states against the coming world-end scenario

#### A Sermon Without Translation

Role: the doctrine becomes impossible to negotiate with.

Effects:

- unlock global final warning actions with once-per-target memory
- add propaganda or war support
- push BOP toward Final Silence
- reduce foreign acceptance of peace letters
- increase AI hostility against the Holy Realm
- add event-log entry or news flavor

### Vow Against Annihilation option

In the event fired by the renamed Ministry of Silence focus, when the `Vow Against Annihilation` option is chosen:

- autocomplete `Lamps Remain Lit`
- unlock the focuses under the Lamps Remain Lit branch
- set clear route flags so the peace/refusal branch is playable
- prevent the Final Silence branch from soft-locking
- cleanly update tooltips so the player understands the branch opened

### Remove “No doctrine is above refusal”

The Holy Realm should never choose `No doctrine is above refusal`.

Remove the option entirely. Do not leave it as an AI-zero option. Remove or rewrite all references to it so it cannot appear, cannot be selected by AI, and cannot leave dead localisation.

---

## 5. Holy Realm Peace Branch Expansion

### White Flags on Foreign Roads

This focus must do more than simple modifiers.

It should unlock a foreign intervention and peacekeeping decision family.

Decision families:

1. `Dispatch White-Flag Envoys`
   - target countries currently at war
   - sends noncombatant negotiators
   - creates a peace letter event for both sides
   - white peace only happens if both sides accept
   - AI usually refuses unless exhausted, losing, democratic, non-aligned, or facing a common crisis

2. `Open the Road of Return`
   - target refugee-heavy or war-torn countries
   - costs convoys, support equipment, trains, and political power
   - adds temporary recovery modifiers to target states
   - may reduce chaos slightly if successful

3. `Mandala Observer Mission`
   - target active wars
   - adds intelligence visibility and a small relation boost
   - enables later peacekeeping support if the defender is eligible

4. `Unarmed Columns Under White Cloth`
   - sends support units or medical/logistics help
   - lowers casualties or damage in a target allied/friendly war
   - risks a scandal event if the convoy is attacked

### Peace negotiations

Add targeted peace negotiation decisions.

Flow:

1. Holy Realm selects a war where it is not the main belligerent.
2. Holy Realm sends negotiation letters to both sides.
3. Side A receives an event and accepts or refuses.
4. Side B receives an event and accepts or refuses.
5. If both accept, white peace fires.
6. If either refuses, no peace happens and the refusal is logged.
7. AI acceptance should be low by default, especially for aggressive majors.
8. AI acceptance rises when exhausted, losing badly, low manpower, high surrender progress, democratic, non-aligned, or suffering from high chaos.

The system should show that the Mandala is active even when the AI refuses.

### Mandala of Nations super-event

The `Mandala of Nations` focus must trigger a super-event.

Super-event role: major faction or world-order announcement.

Required package:

- unique title
- description
- button text
- verified quote
- unique image
- unique audio ID and audio file
- settings-aware playback
- docs and spreadsheet update
- event log entry

The tone should be active and political, not generic peace flavor. It should present the faction as an organized international project.

### Mandala of Nations decisions after formation

After the faction forms, unlock a Mandala decision category or expand the existing one.

Decision families:

#### Mandala Arbitration

- peace letters to active wars
- conference attempts
- ceasefire observation missions
- white peace if both sides accept

#### Mandala Development Missions

Targets African, South American, and Asian countries or states that are poor, underdeveloped, damaged, or war-affected.

Examples:

- `Support Village Wells`: adds infrastructure or supply improvements
- `Fund Rural Clinics`: adds state modifier reducing attrition and increasing monthly population or stability where supported by existing mechanics
- `Build Grain Storehouses`: improves local supply and reduces famine or chaos pressure
- `Repair Market Roads`: adds infrastructure and a small civilian construction boost
- `Send Teacher-Doctor Caravans`: adds stability, compliance support, or education-themed modifier
- `Restore River Pumps`: infrastructure and local resources where valid
- `Port Sanitation Mission`: naval base or supply support in coastal poor states
- `Monsoon Shelter Program`: reduces disaster or refugee penalties
- `Railway Peace Contract`: adds railways or improves supply hubs
- `Cooperative Workshop Grants`: adds civilian factory progress or one civilian factory in eligible states
- `Clean Water Compact`: lowers local unrest and improves infrastructure
- `Clinic Convoy Under Mandala Flag`: costs trucks, support equipment, convoys, and fuel

These decisions must actually change the map or country:

- infrastructure
- railways
- supply hubs
- civilian factories
- building slots
- state modifiers
- local stability or resistance changes
- target-country recovery ideas
- chaos reduction where appropriate

Do not make these only PP-for-opinion buttons.

#### Mandala Peacekeeping Missions

- target minor democratic defending countries at war
- spawn peacekeeping units for the defender
- units should be defensive, limited, and not abusable
- do not spawn endless divisions
- require Mandala reach, equipment, manpower, and cooldowns
- scale with target size and war intensity

Suggested unit types:

- light infantry peacekeeping brigade
- field hospital support detachment
- engineer defense group
- mountain defense unit for Himalayan or rough terrain targets
- logistics column for supply-poor defenders

#### Faction Member Protection

Unlocked by `Shelter the Exiles` once Mandala of Nations exists.

- spawn peacekeeping or relief units in friendly faction members
- build shelters, hospitals, or supply hubs in faction territory
- evacuate exiles from collapsing fronts
- create temporary defensive modifiers for faction members
- reduce chaos or refugee pressure in faction states

### Peace branch focus rewards

Rework peace branch focuses so they unlock mechanics and decisions, not only manpower, stability, or generic infrastructure.

Examples:

- a focus unlocks arbitration missions
- a focus creates the Mandala development office
- a focus expands eligible regions for aid
- a focus unlocks peacekeeping units
- a focus improves acceptance chances for peace letters
- a focus adds decision targets in Africa, South America, and Asia
- a focus creates a refugee logistics network
- a focus adds a Mandala reach source from faction members
- a focus unlocks emergency anti-chaos missions

### Reduce chaos missions

Add missions where the Holy Realm acts through the Bodhisattva or Mandala institutions to reduce chaos.

Suggested missions:

1. `The Bodhisattva Walks the Burning Road`
   - target a region with active war or high chaos pressure
   - costs trains, trucks, support equipment, and political power
   - success slightly lowers chaos and adds local recovery
   - failure creates a news report and raises Final Silence BOP pressure

2. `Seven Nights of Open Kitchens`
   - target famine/refugee pressure areas
   - costs convoys and infantry/support equipment
   - improves state supply and lowers unrest

3. `Letters Carried Past the Guns`
   - targets both sides of a war
   - starts peace letter chain
   - both sides must accept for white peace

4. `The Quiet Bell Mission`
   - target a faction member or friendly minor
   - reduces local chaos, panic, or instability
   - cooldown scales with Mandala reach

5. `Witnesses at the River Crossing`
   - sends observers to a major front
   - gives intel and unlocks later peacekeeping aid
   - refusal or attack increases condemnation against the attacker

### Infrastructure focus spam cleanup

Audit the Holy Realm focus tree and remove repeated infrastructure rewards.

The Holy Realm already gets very high infrastructure from early focuses. Later focuses should use varied rewards:

- decision unlocks
- timed missions
- intelligence upgrades
- agency unlocks
- peacekeeping units
- faction mechanics
- Mandala reach changes
- BOP movement
- claims, war goals, or coring decisions
- advisors
- factories only where geographically justified
- railways, supply hubs, airbases, forts, or AA only when the focus narrative supports it

---

## 6. Mandala Reach Balance

Mandala reach is too high when the Holy Realm controls only Nepal and Bhutan.

Rebalance it so early reach is limited.

Suggested model:

Base reach:

- Nepal only: very low
- Nepal and Bhutan: still low
- nearby Himalayan consolidation: modest
- major conquest or large faction membership: meaningful
- large population, ports, industry, or multiple Mandala members: high
- world-scale conquest or major global influence: very high

Mandala reach sources:

- owned core population
- controlled strategic regions
- number and strength of Mandala faction members
- number of successful peace missions
- number of active development offices
- intelligence network maturity
- major conquest milestones
- global legitimacy from accepted peace talks

Mandala reach should not be inflated by:

- one or two small countries
- repeated decisions with no cap
- passive focus rewards that ignore actual map position
- inactive faction members

Add debug tooltip or scripted localisation showing why reach has its current value.

---

## 7. Final Silence World-End Scenario

### Trigger reliability

Fix the chain so the Final Silence actually happens when the decision or event that starts it is selected.

Required flow:

1. final decision or event selected
2. set Final Silence preparation flag
3. show the correct warning or last authorization event
4. set `world_end`
5. set Final Silence scenario flag
6. trigger Final Silence super-event
7. begin visible nuclear deployment sequence
8. remove population from non-Holy-Realm states
9. feed deaths system
10. disable or gate incompatible ongoing systems

### Visual nuclear deployment

The world-end scenario should visibly deploy nukes to every province or state outside Holy Realm territory.

Implementation target:

- every valid non-Holy-Realm state receives visible nuclear strikes
- strikes should be staggered by region or timed waves so the player can see the world ending
- Holy Realm states are excluded
- if the engine requires state-level rather than province-level strikes, use every valid state
- use visual effects where available
- add reports/log entries between waves if the sequence lasts more than a few days

Regional wave example:

1. Central Asia and Soviet remnants
2. East Asia and Southeast Asia
3. Europe
4. Middle East and Africa
5. Americas
6. Oceania and remaining islands

### Population and deaths system

After or during strikes:

- remove population from affected states
- add deaths to the Chaos Redux deaths tracking system
- classify deaths under a Final Silence or nuclear annihilation cause
- avoid double counting states hit by multiple visual waves
- update event log and event details
- apply long-term state devastation modifiers if world-end state remains playable

### Safety checks

- exclude Holy Realm owned and controlled states
- exclude states already processed
- handle wasteland, impassable, and invalid states safely
- do not fire repeatedly after `world_end`
- prevent duplicate super-event playback

---

## 8. Weaponized Zombie Disease Raid Cooldown

Remove the cooldown from weaponized zombie disease raids.

Required:

- no global cooldown
- no hidden cooldown blocking rapid use
- no UI tooltip still claiming a cooldown exists
- no stale scripted flag that re-adds cooldown through cleanup logic

Keep normal validity checks:

- must have required stockpile or unlock
- target must be valid
- target must not be immune through special country rules
- effect must not stack broken modifiers if the raid applies state effects

If spam becomes too strong, balance through costs, stockpile production, target validity, or consequences, not cooldown.

---

## 9. Every Super-Event Must Have Unique Audio

Audit every super-event in the repo.

Required:

- no two super-events may share the same audio ID unless they intentionally call the same super-event slot as the same event, which should be documented
- each super-event needs a unique audio file
- each unique audio file must have documented source, creator/composer, license, source URL, final path, and conversion notes
- unclear-license audio must be replaced
- each super-event must use settings-aware playback
- docs and spreadsheet must reflect the final audio

For new or changed super-events in this task:

- Mandala of Nations must get unique audio
- Final Silence must get unique audio
- any collapse or major escalation super-event touched by this work must keep unique audio

Use the super-event text researcher and audio researcher subagents if available.

---

## 10. Cross-System Documentation and Validation

### Docs to update

Update all relevant surfaces:

- event documentation in `docs/events/`
- focus tree docs
- decision category docs
- super-event docs
- audio manifest or equivalent
- asset manifest where images/icons are added
- spreadsheet row or catalog entry if this repo uses one for the affected events
- settings documentation for the new checkbox
- completion audit report

### Validation checklist

Before calling the goal complete:

- forced Soviet collapse works at max threat
- all valid releasable Soviet countries are released over MTTH waves
- high-chaos special countries appear only when chaos allows them
- released countries declare war on the Soviet Union after delay
- communist spread is more aggressive
- player-facing harder crisis setting exists and works
- communist spread works in civil wars
- refuge relief spam fixed
- final warning spam fixed
- peace versus Final Silence scales with chaos
- Mandala Bureau unlocks intelligence agency and free upgrades
- focus filters point to real focus branches
- The World Is Asked to Kneel grants global claims and war goals
- conquest coring decisions work without polluting `possible_holy_realm_cores`
- Ministry of Release is renamed to Ministry of Silence
- Ministry of Silence requires all three prerequisite focuses using AND logic
- The Last Authorization is final branch focus and requires Ministry of Silence
- three listed branch focuses last 14 days and have effects
- Vow Against Annihilation autocompletes Lamps Remain Lit and unlocks branch
- No doctrine is above refusal option is removed
- White Flags on Foreign Roads unlocks real intervention mechanics
- Mandala of Nations focus triggers a super-event
- Mandala post-formation decisions exist and do real map/country work
- peace negotiations require both sides to accept
- Mandala peacekeeping units spawn only for eligible minor democratic defenders
- Shelter the Exiles unlocks faction-member peacekeeping after Mandala formation
- peace branch focuses unlock actual mechanics
- repeated infrastructure focus rewards are removed or replaced
- Mandala reach starts low with Nepal and Bhutan only
- Final Silence visually nukes the world outside Holy Realm states
- Final Silence removes population and feeds deaths system
- weaponized zombie disease raids have no cooldown
- every super-event has unique audio
- localisation has no missing keys
- focus tree has no invalid prerequisites
- decisions have readable costs and no passive duplicate mission spam
- AI weights do not pick invalid branches
- logs, docs, and spreadsheet match implemented behavior

### Suggested subagent routing

Use subagents where available, but the parent agent remains responsible for final integration.

- `chaosx_repo_explorer`: map existing files, IDs, focus names, settings GUI, super-event audio usage
- `chaosx_scripted_system_architect`: implement reusable Non-AI Crisis Pressure and Soviet collapse queue helpers
- `chaosx_focus_tree_auditor`: audit Holy Realm focus tree after changes
- `chaosx_decision_mission_auditor`: audit Mandala, intervention, development, coring, and zombie raid decisions
- `chaosx_super_event_text_researcher`: Mandala of Nations and Final Silence quote/button text
- `chaosx_super_event_audio_researcher`: unique audio research, licensing, `.ogg` conversion
- `chaosx_asset_source_researcher` or `chaosx_generated_event_art`: super-event images if required
- `chaosx_localisation_auditor`: broad localisation pass
- `chaosx_country_package_auditor`: Soviet collapse releases and special chaos country handling
- `chaosx_event_completion_auditor`: final spec-versus-implementation audit