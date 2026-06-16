# Event 012 Africa — Acceptance Criteria

This file defines pass/fail expectations for implementing the planning package.

## Event baseline

- Event ID 12 remains a Minor Fire-Once event in the Formables cluster.
- The event selects one valid country whose capital is in Africa.
- The selected country receives a clear public proclamation and a staged Africa package.
- The selected country receives all-African paper cores/claims as the fantasy premise, but those do not become fully stable cores without staged integration.
- The chosen country changes visible cosmetic identity immediately or through the opening focus/decision flow.
- If RSA is selected while in the Allies, the event starts the RSA civil-war branch instead of the normal unifier package.
- If the RSA continental side wins, the Allies make peace with Africa through a dedicated aftermath/treaty branch.

## Focus tree

- The unifier gets a large focus tree or overlay route, not a short generic tree.
- The tree contains opening survival/state-building, political routes, industry, military, diplomacy, expansion/integration, diaspora, League management, regional authority, post-unification, high-chaos, and world-end/continent-sponsor paths where unlocked.
- Political, industry, military, diplomacy, and expansion branches interact with the mechanic values and each other.
- The tree has route locks, optional branches, convergence nodes, hidden/high-chaos branches, and late-game ambitions.
- Focus rewards are varied: buildings, railways, ports, resources, units, decisions, missions, advisors, leaders, identities, claims/cores, war goals, faction mechanics, events, and mechanic values.
- The tree is not mostly new ideas, stability, war support, political power, or flat modifiers.
- Every important focus has icon direction and final implementation has icons/localisation/AI.
- A route coverage table is produced after implementation.

## Decisions, missions, and GUI

- Decision systems represent real actions, not a political-power store.
- Costs use equipment, manpower, XP, convoys, trains, fuel, local support, legitimacy, supply/rail/port control, deadlines, stability, war support, and faction cohesion where appropriate.
- Timed missions require real map objectives such as holding capitals, rail hubs, ports, corridors, or supplied divisions.
- The player can see and understand Legitimacy, Authority, League Cohesion, Liberation Momentum, Regional Trust, Colonial Alarm, Paper-Core Burden, and Covenant Pressure through a decision header or custom GUI.
- The Continental Congress scripted GUI or equivalent presentation includes regional cards, meters, selected targets, warnings, and clickable actions with matching AI equivalents.
- Decision categories are phased and avoid showing every possible action at once.
- Obsolete decisions and missions clean up after integration, war, route change, annexation, subject transfer, civil war, or event completion.

## Charter League and regional authorities

- African states are not immediately annexed by default.
- African states can join a faction/League, receive aid, be defended, become regional authorities, resist integration, leave the faction, or declare war if pressured too hard.
- Strong African countries resist more often and can demand equal-seat federation, autonomy, or leadership contests.
- Regional authority subjects exist as meaningful state intermediaries and can be integrated later.
- Integration is staged and uses local trust, authority, legitimacy, resistance/compliance, and map objectives.

## Country packages

- The selected unifier has dynamic identity changes, party names, route names, leader/council handling, starting ideas, AI strategy, and a real military package.
- New regional authorities have names, tags or tag placeholders, flags, leaders/councils, starting forces, focus/decision relationships, and AI behaviour.
- High-chaos nonhuman/supernatural actors are explicitly nonhuman or supernatural, not human caricatures.
- Any fighting country has dynamically scaled starting forces and reinforcement pathways.
- Real leaders use sourced portraits; fictional leaders use generated portraits with gender presentation/name-pool notes; councils use institutional names.

## Evolutions

- Baseline stages are not logged as evolutions.
- Each evolution has active-event and/or pre-fire evolved opening rules.
- Evolution I adds clear early proclamation/news and nearby consolidation.
- Evolution II adds stronger integration tools, temporary buffs, dramatic cosmetics, and weird units including elephant formations where appropriate.
- Evolution III adds global-chaos/continent-sponsor tools.
- Evolution IV adds major world-chaos pole behaviour, dynamic cross-continent unions, and final confrontation hooks.
- Disabled evolutions do not set flags that required baseline content later depends on.

## Super-events and world-end

- Super-event roles are defined but final titles, quotes, cultural remarks, and audio are research-gated.
- Required super-event moments include at least: Africa is One, Scramble for Africa reaction, possible continent-sponsor reveal, dynamic cross-continent union reveal, and World Is One terminal branch.
- World-end branch only triggers if Africa fully unified, extreme chaos/world-end conditions exist, “Africa is one” has fired, all other continental unifiers exist, they have pursued post-unification paths, and their world-end path is unlocked.
- The World Is One path is terminal and gates incompatible future systems.

## Assets

- Asset package includes flags, route flags, leader/council portraits, focus icons, ideas, decision icons, category icons, report/news/super-event images, achievements, UI panels, animated sprites, and static fallbacks where planned.
- Generated assets follow source-mode rules; real assets are sourced.
- Animated assets are frame-sheet packages with real source frames, not transform-only mockups.
- Assets are documented in a manifest and handoff.

## Achievements

- Achievements are implemented for difficult routes, RSA branch, League cohesion, staged integration, Green Covenant, Scramble response, continent sponsorship, and world-end branch.
- Achievements are not automatic for simply firing the event.
- Achievements have disqualifiers and tracking notes.
- Achievement icons exist.

## AI and balance

- AI route selection respects country archetype, war state, strength, legitimacy, cohesion, chaos, and valid targets.
- AI does not choose invalid missing-target paths.
- AI can use all major decision families through AI-equivalent decisions/effects.
- No free unit loops, core spam, war-goal spam, repeated equipment farming, influence farming, or puppet abuse remain.
- Balance report includes targeted scenario tests: ordinary unifier, weak unifier, RSA in Allies, African ally under attack, high-chaos Green Covenant, full Africa unification, cross-continent union, and World Is One gate.

## Documentation and catalog

- Event docs, event details, event log wording, evolution text, super-event docs, asset manifests, and spreadsheet rows match the implemented state.
- Spreadsheet update happens after implementation facts exist and mirrors in-game wording.
- Completion report explicitly lists any simplifications, omissions, blockers, or fallback content. If none exist, it says so with evidence.


## Revision 2 acceptance additions

- Historical/legacy authorities must be implemented as a real subject/observer system, not just names in localisation.
- Priority A authorities from `012_africa_expanded_subject_matrix.md` must have decisions, at least one focus or focus-family hook, AI behavior, localisation, and asset direction.
- The Authority Register must use phased/selected target presentation or another clutter-control method; it must not dump every authority decision at once.
- Integration Temperature, or an equivalent dynamic trust/resistance model, must govern peaceful integration, subject autonomy, resistance, faction exit, and forced annexation consequences.
- High-chaos nonhuman/supernatural actors must be locked behind Evolution III/IV or explicit Green Covenant gates and classified separately from human authorities.
- No human African authority may be portrayed as a monster, animal state, or supernatural caricature.
- Disaster-warning powers must use Omen Reliability, target response, counterplay, false-warning risk, AI limits, and legitimacy tradeoffs.

## Archive of Old Seats and absurd package acceptance

| Requirement | Pass condition |
| --- | --- |
| Dossier layer exists | Player can unlock and manage historical restoration dossiers through decisions/UI, not only flavour events. |
| Regional coverage | At least one implemented dossier family exists for every macro-region listed in `012_africa_niche_country_expansion.md`. |
| Depth count | At least 24 historical dossier entries have gameplay representation; at least 6 high-chaos absurd/nonhuman packages have gameplay representation. |
| High-chaos gating | Nonhuman/supernatural countries or observer subjects do not appear before the Bestiary Clause/Evolution III gate unless a triggerable scenario explicitly forces it. |
| No caricature | Human African polities are never described with animalizing/nonhuman language. Nonhuman actors are explicit supernatural/animal/legal-fiction entities. |
| Costs and objectives | Dossier decisions use equipment, manpower, construction, trains, convoys, unit placement, regional control, legitimacy, local trust, and time pressure where appropriate. |
| Core discipline | Dossiers grant claims/paper cores first; full cores require staged local settlement/integration. |
| AI validity | AI uses nearby valid dossiers, avoids remote impossible targets, respects route locks, and does not pick hidden absurd branches under normal conditions. |
| Asset source discipline | Historical assets are source-reviewed; fictional/nonhuman assets are generated and documented; animated assets have static fallbacks. |
| Prompt alignment | Coding, asset, achievement, and decision prompts all reference the niche expansion so implementation cannot skip it. |



## Leader display-name flavour

- The source-language joke names listed in `specs/012_africa_country_packages_and_subjects.md` appear only in allowed Event 012 player-facing localisation or scripted localisation.
- English localisation does not translate or gloss the meanings.
- Raw phrase strings are not used as script ids, filenames, tags, variables, sprite names, achievement ids, or asset text.
- Historical country, institution, old-seat polity, symbol, and source names remain researched and separate from court/ruler display masks.
