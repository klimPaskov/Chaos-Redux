# Event 011 - Secret Alliance

Event 011 is `Secret Alliance`, a Minor Fire-Once event rooted at `chaosx.nr11.1`. It is not part of an event cluster. At the instant the event is accepted, the current player country is saved as the fixed target and remains the target for the entire lifecycle, including concealed operations, public reveal, coalition war, settlement, achievements, and cleanup.

## Completion status

This file is the current mechanic and registration overview, not completion proof. `docs/plans/011_secret_alliance_plans/subagent_handoffs/decision_mission_audit.md` and `docs/plans/011_secret_alliance_plans/subagent_handoffs/localisation_audit.md` remain the authoritative strict completion snapshots. Both are incomplete until clean re-audits supersede them.

## Opening and founder selection

The automatic event can fire only when the player is a valid country and at least three valid AI minors exist. It cannot restart after the fire-once history flag, while another Event 011 context is active, or after the event has reached a terminal state. Manual Coalition Unmasked launches use their own gate.

The opening builds a weighted ticket pool for each founder selection. Candidates must be valid independent AI-controlled minor countries. The selector excludes the fixed target, subjects, capitulated or invalid countries, special nonhuman chaos countries, target faction partners, countries already fighting the target, and countries already selected. It strongly prefers factionless countries, then considers adjacency, continent, ideological rivalry, target threat, country size, and grievances. Three distinct founders are drawn from the pool and receive persistent motive, role, support-capability, private-commitment, and commitment-strength profiles.

Normal openings begin at baseline. If evolution settings already make later stages available before the event fires, the event records the open stages and starts with their corresponding membership, readiness, counter-network, and warning package. A pre-fire Evolution III opening first creates the Evolution II package and then gives the pact a short real preparation interval before the public-war stage opens.

## Concealed pact

The pact is event-owned and is never represented by a normal faction while hidden. Its durable state is held in member, founder, sponsor, suspect, confirmed-member, turned-member, and public-member arrays plus global cohesion, readiness, alertness, doctrine, war pressure, and operation state. Each member has its own motive, operational role, support capability, private bargain, and commitment band.

Baseline pulses are ordinary progression. They can recruit valid minors, generate internal disputes, leak traces, lose members, or launch one operation. Operations are selected across six families: diplomatic isolation, intelligence penetration, industrial and transport sabotage, political and social pressure, military preparation, and recruitment. The actor, target surface, risk, evidence class, and readiness layer are recorded before resolution. Adaptive recovery blocks immediate repetition after an exposed or failed operation.

- Evolution I widens the pact to four-to-six minor members and makes recruitment and recurring operations more capable.
- Evolution II widens it to six-to-eight members, permits one valid major sponsor, enables serious covert action, and opens Foreign Interference with visible Evidence and Preparedness.
- Evolution III widens it to eight-to-twelve members, permits a possible second major sponsor, builds war pressure, displays the coalition-closure warning, and permits public faction formation, preparation, and preemption.

Human countries are never silently forced into the hidden pact. A normal human invitation is an explicit event with join, refuse, leak, and expose choices. Scenario construction selects AI members only and keeps the launching human as the target.

## Evidence, suspects, and preparedness

Evidence is source-aware. A clue records one of six independent classes—method, communications, financial, diplomatic, military, or human—and the country that produced it. The same suspect cannot repeatedly farm the same class. Each suspect maintains its own independent-class count, while the global dossier separately tracks network-wide classes. A country reaches Confirmed only when its confidence threshold and its own corroboration threshold are both satisfied. The target can see at most three suspect cards at once and selects them directly from the scripted GUI. Hidden membership is not exposed merely because a country is visible as a suspect.

Preparedness is the sum of seven maintained components: staff security, industrial security, transport security, border readiness, continuity, allied coordination, and known plans. Every project, emergency measure, patrol commitment, and consultation keeps a separate source contribution and clears only its own value on expiry. Protection projects are timed and carry real burdens while active. Evidence and Preparedness change outcome bands, operation-family weights, and reveal conversion; they are not passive score decorations.

## Decision and mission matrix

`secret_alliance_foreign_interference` opens at Evolution II or from an earlier exposed incident. Its investigations compare diplomatic traffic, audit funding, inspect missions and access talks, compare sabotage signatures, trace couriers, question intermediaries, and reconstruct meeting circuits. Named missions then track a real map or country objective: Watch a Liaison Route, Seize a Compromised Courier, Turn a Recruited Clerk, Protect a Defecting Envoy, Break a Safehouse Network, conduct a National Manhunt, and Control a Rumor Channel. A delayed verification event checks the named state and supporting field requirements after activation and repeats while the mission remains active, preventing same-tick completion. Full and partial results register the mission's actual suspect and evidence class; expiry can preserve partial progress rather than silently becoming failure.

Protection projects compartmentalize staff plans, rotate ciphers, secure industrial choke points, disperse stockpiles, guard the cabinet, harden border communications, protect ports and airfields, and establish continuity sites. Diplomacy can approach a suspect, offer a security guarantee, address a grievance, expose sponsor pressure privately, request allied consultation, convene a neutral inquiry, or demand an explanation. Offensive actions feed false plans, run controlled shipments, plant a false dispute, turn a member, sabotage a forward depot, disrupt a conference, raid the border, or seize a courier aircraft or vessel. Border actions prepare and use an actual controlled border pair, require the appropriate trains and deployed units, and may open a limited conflict with escalation, withdrawal, or negotiated stand-down outcomes.

Public actions require evidence thresholds and independent corroboration before the target can release a partial dossier, name a first member, present the coalition case, expose a major sponsor, or demand inspections. Naming an innocent country records a durable false-accusation consequence, strengthens the hidden pact, damages stability and relations, and disqualifies the applicable achievements. The coalition-crisis category adds emergency mobilization, fortification, overseas recall, a final warning, preemption, defensive alliance seeking, leadership evacuation, a visible countdown, and post-reveal war actions.

Costs scale with target size, repeat use, and action family. They can consume command power, service experience, political power, stability, war support, support equipment, trains, trucks, convoys, fuel, and manpower. Availability uses the same computed values as the displayed custom costs. AI countries use the same effects, caps, commitments, objectives, and outcome model.

## Reveal contract

Every reveal route calls `secret_alliance_reveal_pact`. The reusable effect refreshes member validity, snapshots the reveal state, scores every eligible member for public leadership, creates `secret_alliance_public_coalition`, and adds every valid active member. When a target war already exists, the effect performs the complete member call before it commits the revealed state or fires the super-event; it retries the call transaction and rolls back an incomplete public faction instead of recording a partial reveal. The faction name is dynamically rendered as Anti-[target] Pact.

If any active member enters a normal hostile war with the fixed target, `secret_alliance_handle_war_relation_added` immediately saves that war as the anchor, reveals the pact, creates the faction, adds every valid active member, and calls every valid active member into the same target war. This route deliberately ignores delayed-call and turned-member hesitation because the external war has already activated the pact.

Public conference, public dossier, captured conference, preemption, and fracture reveal routes converge on the same effect. Planned war preserves turned-member exits, planted false-plan consequences, delayed calls, and fractured-member withdrawals. Hidden cohesion becomes Coalition Resolve; readiness becomes opening coordination; Evidence becomes known weaknesses; Preparedness becomes target defenses. The converted bands apply staged coalition and target ideas rather than flattening the hidden game into one modifier.

The reveal fires super-event 73, starts the public offensive countdown when no war already exists, and replaces concealed AI with target-specific coalition-war AI.

## Coalition war and settlement

Members receive role-aware AI priorities for the target front, production, logistics, naval support, intelligence, and distant support. Major sponsors receive stronger build and target pressure. Turned and fractured members are de-prioritized or removed. Maximum-intensity scenario members receive the most aggressive mapped posture.

During war, capital loss, objective progress, failed offensives, sponsor distraction, conflicting promises, two-major rivalry, separate terms, concessions, target countermeasures, and member fractures update Coalition Resolve and opening coordination. The target can exploit liaison maps, strike known depots, offer separate terms, publicize conflicting aims, support member opposition, demand sponsor accountability, or coordinate a counteroffensive. War pulses test collapse, delayed calls, fracture exits, capital survival, and settlement eligibility.

The final outcomes are target victory, coalition victory, negotiated settlement, internal rupture, or a continuing regional bloc. Settlement records starting-capital control, preserves achievement snapshots, applies the appropriate country flags and ideas, and then removes Event 011's runtime arrays, event targets, missions, timed burdens, border conflict, hidden variables, and AI strategies.

## Triggerable scenario

SCN-009 `Coalition Unmasked` launches the complete Evolution III package against the current player through one of five compositions:

- Regional Ring
- Ideological Front
- Great-Power Sponsor
- Unlikely Coalition
- Random Coalition

Low, Medium, High, and Maximum intensity scale member count, major count, resolve, readiness, equipment, trains, trucks, and fuel. Manual launch bypasses normal Chaos, evolution, date, history, prior Event 011 completion, and automatic-fire requirements. It retains the active-context guard, the active `world_end` terminal-conflict gate, valid-target and viable-composition checks, and the normal human-consent rule. Scenario members are AI-only. Maximum intensity snapshots requested membership, the safe valid pool, achieved membership, and achieved majors; its dedicated achievement qualifies only when the requested roster is reached or every safe valid candidate is used.

## Achievements

The six achievements are implemented in `common/achievements/chaos_redux_achievements.txt` and documented in `docs/achievements/011_secret_alliance_achievements.md`: The Empty Chair, Every Thread, Their Man in the Room, Divide the Table, Surrounded, Not Buried, and Two Giants, One Grave. Each uses durable origin, reveal, membership, evidence, capital, fracture, and outcome snapshots. Forced/debug origin, innocent targeting, scenario origin, and human-consent disqualifiers are applied only where specified.

## Registration and files

- Event script: `events/011_secret_alliance.txt`
- Constants and MTTH: `common/script_constants/011_secret_alliance_constants.txt`, `common/mtth/011_secret_alliance_mtth.txt`
- Effects and triggers: `common/scripted_effects/011_secret_alliance_effects.txt`, `common/scripted_triggers/011_secret_alliance_triggers.txt`
- Decisions: `common/decisions/categories/011_secret_alliance_categories.txt`, `common/decisions/011_secret_alliance_decisions.txt`
- On-actions and AI: `common/on_actions/011_secret_alliance_on_actions.txt`, `common/ai_strategy/011_secret_alliance.txt`
- Faction package: `common/factions/templates/011_secret_alliance.txt`, `common/factions/rules/011_secret_alliance_rules.txt`, `common/factions/rules/groups/011_secret_alliance_rule_groups.txt`, `common/factions/goals/011_secret_alliance_goals.txt`
- Ideas and UI: `common/ideas/011_secret_alliance_ideas.txt`, `common/scripted_guis/011_secret_alliance_scripted_gui.txt`, `interface/011_secret_alliance.gui`, `interface/011_secret_alliance.gfx`
- Localisation: `localisation/english/011_secret_alliance_l_english.yml` plus shared event-name, achievement, scenario, music, and super-event files
- Event log and details: shared event-log registration, actor mapping, detail page, and Evolution I-III entries under the Event 011 ID
- Scenario registry: shared triggerable-scenario constants, effects, triggers, scripted localisation, and GUI localisation as SCN-009
- Super-event: slot 73, audio ID 43, image `GFX_super_event_011_secret_alliance_public_reveal`
- Catalog workbook: Event 011 row and SCN-009 row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Asset register

All final paths and sprite identifiers are recorded in `docs/assets/011_secret_alliance/asset_register.md`.

- Event and news art live under `gfx/event_pictures/011_secret_alliance/` and are registered in `interface/011_secret_alliance.gfx`.
- Mechanic UI, meters, suspect states, status icons, faction emblem, decision icons, and idea icons live under `gfx/interface/011_secret_alliance/` and its decision/idea subfolders and are registered in `interface/011_secret_alliance.gfx`.
- Achievement triplets live under `gfx/achievements/` and are registered in `interface/chaosx_achievements.gfx`.
- The reveal image lives at `gfx/super_events/011_secret_alliance/super_event_public_reveal.dds` and is registered in `interface/chaosx_super_events.gfx`.
- The Evolution III warning uses eight independent 128x96 frames assembled into `coalition_closure_warning_sheet.dds`; `coalition_closure_warning_static.dds` is its registered static fallback.

## Balance notes

Founder selection, membership caps, stage openings, operation cadence, clue values, component gains, decision gates, cost scaling, outcome bands, reveal conversion, war facts, scenario packages, and AI weights are centralized in `common/script_constants/011_secret_alliance_constants.txt`. MTTH cadence is centralized in `common/mtth/011_secret_alliance_mtth.txt`. The decision matrix enforces simultaneous-family caps so the target must choose between investigation, protection, diplomacy, offensive preparation, border escalation, and emergency response rather than buy every defense at once.

## Future plans

- Add country-specific motive localisation for named historical rivalries without exposing unconfirmed members.
- Add more postwar memorial and intelligence-reform flavour after the runtime pact state has been cleaned up.
- Extend the compact counter-network panel with optional accessible keyboard navigation if the shared scripted-GUI framework gains a standard pattern.
