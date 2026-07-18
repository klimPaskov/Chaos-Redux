# Event 015: Utopia Manifesto

## Current status

`utopia_manifesto` is Event 15, a Minor Fire-Once country transformation event. Its entry is `chaosx.nr15.1`. The live package contains 106 Event 15 event definitions, a 124-focus replacement tree, 121 decisions, 44 missions, 9 decision categories, 50 staged ideas, 24 characters, 14 achievements, and five final cosmetic identities.

This document describes the current implemented mechanic. Live script remains the runtime authority. The accepted specifications under `docs/specs/015_utopia_manifesto_specs/` remain the design authority. Dated handoffs under `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/` are evidence snapshots.

Event 15 is complete against its accepted specifications and plans in the frozen 2026-07-18 source snapshot. The fresh read-only whole-event audit passes with zero open P0 through P3 finding, fallback, simplification, omission, blocker, or queued accepted plan. Its SHA-256 is `5a90b637478872d6f960c7e67630e0efd0fda3e17869bad2c094473596a12183`, and its 53-file runtime-text manifest SHA-256 is `395873f4821fdf159cfb2f6edb9eecc0790a724f151cb0df62f89b969649d4b2`.

## Opening and recipient selection

Automatic entry is registered through the fire-once event registry with the Event 15 script constant. Selection prefers an eligible player and otherwise uses a conservative weighted minor-country pool. The target gates reject major powers, strong industrial states, invalid or capitulated countries, nonhuman and special Chaos actors, active country-replacement packages, and countries whose focus package is not safe to replace.

The selected country receives a real choice.

- An AI recipient accepts.
- A human recipient can accept or reject.
- Acceptance records the original ruling ideology group, exact active leader, exact leader ideology subtype, and election permission before Event 15 institutions can change them.
- Acceptance recruits the Event 15 character roster, initializes the Ledger and staged ideas, and loads `utopia_manifesto_tree`.
- Rejection clears the event-owned opening state and leaves the country's existing focus tree, territory, forces, technology, parties, leader, and base flag intact.

The event history name is `Utopia Manifesto`. The Event Details entry is `chaosx.events_log.window.event_details.utopia_manifesto`, with the latest valid actor recorded for the event log. All twelve hidden Event 15 definitions use documented `hidden = yes`. The `.116`, `.150`, `.163`, `.164`, `.165`, `.205`, `.207`, `.212`, `.214`, `.216`, `.218`, and `.220` declarations use `hidden = yes` rather than `hide_window`.

## Commonwealth Ledger

The Commonwealth Ledger is the central state model. The visible axes are:

- Need
- Plenty
- Concord
- Choice versus Assignment

The Common Reserve is a separate durable score with its own bands. It is not a fifth Ledger axis.

Each visible axis is rebuilt as a bounded total:

```text
displayed total = base + durable policy record + current country contributions
```

The result is clamped from 0 to 100. Current contributions are recalculated from the Event 15 actor's industry, infrastructure, war, occupation, capital condition, institutions, subject status, named pressure, and loss of core territory recorded at acceptance. A refresh replaces the previous live contribution rather than adding it again, so repeated refreshes with unchanged inputs are idempotent.

Ledger refreshes occur through actor-scoped entry points such as acceptance, the National Survey, Ledger-changing decisions and events, the Recount button, the self-scheduling Event 15 pulse, and relevant war, peace, capitulation, annexation, peace-conference, and state-control hooks. Event 15 does not use a daily, weekly, or monthly world scan.

The Ledger window is defined by `interface/015_utopia_manifesto_ledger.gui` and `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`. It is attached to `utopia_manifesto_ledger_category` through:

```txt
scripted_gui = utopia_manifesto_ledger_scripted_gui
```

The window presents the four axes, route, political organization, reserve, callings, district project, selected case, external network, and formation state. Forty-six unique GUI sprite references resolve through the current Event 15 sprite package. The 10 mutually exclusive case cards occupy the case presentation, while the 7 district-role cards and 6 district-state overlays appear together in the Stores and Settlements presentation.

## Callings and material pressure

Six calling families translate country conditions into playable shortages:

- Provisioning and Agriculture
- Workshops and Arsenal
- Civic Works and Transport
- Learning and Care
- Maritime and Settlement
- Defense and Watches

Each family separates structural pressure, durable policy adjustment, temporary adjustment, uncovered severity, and present severity. Necessary Ground reads uncovered severity. Temporary Emergency Levy coverage cannot erase the underlying case justification.

Shortage flags use hysteresis. They enter above the shortage threshold and clear below the lower exit threshold, preventing repeated oscillation at the boundary. The principal methods are Open Call, Guaranteed Placement, Assignment Quota, Emergency Levy, and Second Trade. These methods share mission ownership and cooldown rules so one calling lifecycle cannot overwrite another.

## Focus tree and route architecture

`common/national_focus/015_utopia_manifesto_focus_tree.txt` contains 124 focuses. The graph has one root, all 124 focuses are reachable, all 124 have AI weights, and the five political interpretations are mutually exclusive.

| Route | Constitutional identity | Capstone | Final cosmetic identity |
| --- | --- | --- | --- |
| Consent of Households | voluntary household and municipal consent | Commonwealth by Consent | `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH` |
| Common Table | councils, shared stores, and worker government | Union of Tables | `UTOPIA_MANIFESTO_COUNCIL_UNION` |
| Guardians of Measure | surveys, standards, and technical planning | Perfect Measure | `UTOPIA_MANIFESTO_PLANNED_UTOPIA` |
| Closed Island | assignment, autarky, and compulsory service | Perfect Island | `UTOPIA_MANIFESTO_CLOSED_ISLAND` |
| The Joke Understood | public criticism, mixed institutions, and sunset rules | Good Place That Admits Its Limits | `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH` |

Shared branches cover the public edition, survey, common stores, callings, property transition, Garden Settlements, the island project, defense, Necessary Ground, stewardship, the League, formation, succession, and post-formation play. A constitutional-crisis band lets the country restore consent, empower councils, give authority to surveyors, seal the island, or admit that the book was a question. Every correction rejoins the shared tree.

The island branch has five geographic variants:

- an existing island capital
- an archipelago network
- a leased island
- a coastal refuge
- an Inland Island

The leased-island path uses a fixed foreign lease, renewal choices, expiry, return, and paid replanning. It does not grant a free island.

## Decisions and missions

The current operational inventory is:

| Source | Decisions | Missions |
| --- | ---: | ---: |
| Main package | 105 | 40 |
| Evolution consumption | 15 | 1 |
| Prefire evolution obligations | 1 | 3 |
| Total | 121 | 44 |

The nine categories are Ledger, District, Island, Necessary Ground, Stewardship, League, Defense, Governance, and Formation. Every decision has `ai_will_do`. Every mission uses an activation gate, a variable-backed timeout, cancellation handling, and a terminal outcome.

The main families are:

- national survey and published accounts
- common stores, reserve rotation, emergency release, and sustained reserve proof
- calling methods, training, and emergency labor
- property transition and public tenure
- Garden Settlement survey, construction, charter, and maintenance
- island selection, construction, lease, defense, and replanning
- Necessary Ground preparation, offers, responses, escalation, and closure
- stewardship provision, route repair, charter, vote, return, association, revolt, and integration
- League observers, members, sponsors, aid, reserve, defense, cohesion, and succession
- paid defense growth, engineers, auxiliaries, and contract closure
- constitutional correction, total repeal, formation proof, proclamation, and post-formation renewal
- fifteen evolution interpretation actions and their shared obligation mission

All player-facing costs use the same material payment helpers and equality-safe affordability gates as AI actions. The system does not function as a political-power store.

## Garden Settlements and Penal Works

Garden Settlement projects begin with a real selected state. The survey records which of four roles remain materially suitable:

- Market Garden
- Industrial Housing
- Rail Junction Town
- Refugee Municipality

Every project must maintain housing, transport, and role-plan obligations. Terminal checks can produce completion, an incomplete district, or failure. A route-specific charter then applies the constitutional consequence. The Provision Ring remains the fifth district-role proof used by the Perfect Measure achievement. It is not duplicated as an ordinary district button.

Penal Works is one Closed Island method attached to the existing district lifecycle. It pays manpower, infantry equipment, support equipment, and reserve for faster construction while increasing supply strain, garrison burden, resistance, Assignment, and durable coercive conduct.

Civilian loss uses the shared state-scope helper `apply_exact_state_civilian_population_loss`. The helper records deaths through `chaos_meter_register_deaths` with `constant:chaos_meter_deaths_reason.gulag_repression`, localised as deaths from camps and forced labor. Event 15 does not substitute manpower payment for Deaths accounting and does not define a separate Deaths system.

## Necessary Ground

Necessary Ground permits one active case. The domestic shortage family and the external case type are separate records.

The six general case types are:

- port access
- defensive corridor
- essential resource
- settlement and housing
- island or capital refuge
- reconstruction zone

The leased-island project adds a dedicated `island_project_lease` type. The selected target and state are stored in exact one-item founder arrays with matching IDs. The target country records every exact founder in `utopia_manifesto_case_founders`. The selected state independently records every exact founder in `utopia_manifesto_case_state_founders`. A country or state keeps its shared marker until its final founder record is removed. The case proceeds through domestic review, claim, state assessment, response, settlement or escalation, enforcement where lawful, and stewardship where territory changes hands.

Peaceful methods include purchase, long supply contract, lease, settlement agreement, joint administration, association, and conversion. The ladder records attempted trade, lease, settlement, and joint methods. An ultimatum requires the lawful route exception or the required prior peaceful attempts and refusal. Enforcement uses the private `utopia_manifesto_necessary_ground_take_state` wargoal so cleanup cannot remove an unrelated generic wargoal. Wargoal creation injects the exact saved state ID into the generator. `take_states` also requires ROOT membership in the state's founder array and ownership by the exact target in PREV, isolating simultaneous founders from one another.

Finite foreign terms are explicit:

- settlement agreements run through a dynamically prepared 365 to 540 day mission
- long supply contracts run through a dynamically prepared 540 to 720 day mission
- association duties run through a dynamically prepared 365 to 540 day mission
- the island lease begins at 2,190 days, with 1,095 day renewal and 730 day counteroffer extensions

An island-lease renewal reserves the exact founder and lessor on both countries before `.213` opens. Cancellation or replanning invalidates that pair without releasing its delayed slot, so an already open human response cannot answer a later lease. Every `.213` option still returns through hidden bridge `.214`; the bridge applies only a live exact-pair response and then clears the answer and reservation even when the popup became stale. Founder teardown, lessor teardown, and annexation follow the same reverse links. A different pair can proceed independently, while the same pair receives a fresh full-duration request only after the earlier slot resolves.

Temporary market access is not part of the active contract. Long supply records an exact founder, partner, and state relationship, checks whether the founder already holds resource rights before granting them, and removes only the exact rights Event 15 created. A pre-existing resource-rights agreement therefore survives contract expiry or teardown. Integrated-state benefits are removed when the Event 15 actor no longer owns the state. Ownership and controller restoration are method-specific, and the code records a reconciliation condition instead of transferring a third-party-owned state to an arbitrary country.

The target lifecycle uses exact reverse founder relationships on both the selected country and selected state. Case-created access and guarantees, settlement agreements, long-supply contracts, association duties, island leases, autonomy pacts, League defense guarantees, and their compact sources have separate founder-attribution records. Access and founder guarantees use a shared exact-pair creator gate: a later Event 15 source co-claims a relation only when another live Event 15 source already owns it, while an unattributed pre-existing relation is never claimed. Cleanup removes its source first and revokes the relation only after the final Event 15 creator disappears. Shared state packages likewise clear only when no founder remains. The narrow `on_annex` hook snapshots the annexed target's founders before the target record is cleared, then notifies each exact founder once. During active stewardship, a surviving third-party annexer becomes the successor target with integrity, local-support, and Ledger costs. Annexation by the founder becomes an explicit coercive-conduct, achievement, and stewardship-failure disposition. Target loss before stewardship invalidates and clears the case, enforcement peace has an invalid-target cleanup branch, and state-transfer methods require the selected target to survive the transfer. A one-shot state-control hook snapshots the changed state's exact case, association-charter, settlement, supply, and island-lease founders, then dispatches hidden bridge `.165` after one hour to validate each founder independently. The delay lets a full annexation's founder-rooted `.163` disposition settle first. The bounded self-scheduling Event 15 actor pulse also reconciles owner-only changes that do not fire a controller-change hook, while the peace-conference callback performs an immediate actor-scoped reconciliation. These paths use no recurring world or all-country scan, arbitrary successor search, or silent integration.

## Stewardship and status

Acquired or controlled Necessary Ground enters an obligation system rather than receiving an immediate core. Stewardship covers emergency provision, transport restoration, local charter, a charter period, status choice, long integration, return, association, Assigned Colony, revolt, and mediation.

Terminal helpers remove active missions before flags and scopes are cleared. Temporary modifiers and system-created diplomatic relations are removed through the method that created them. Revolt target and state arrays survive until the response event resolves them. Integrated-state markers reconcile on later ownership change.

A completed association charter has durable reverse indexes on its founder, host, and state. Its recurring public review uses one target-wide, non-reusable reservation: hidden bridge `.207` always releases its delayed slot, while visible `.221` opens only for a still-live association and becomes inert if that generation is invalidated before a human answers. A later association waits for a fresh full-duration reservation instead of inheriting an old callback. Active-duty target annexation fails the duty cleanly. Later host annexation, founder withdrawal, founder teardown, or ownership transfer away from the recorded host removes only that founder's charter and diplomacy sources. The state-control bridge, peace-conference callback, and bounded Event 15 actor pulse cover both control and owner-only changes. Another founder's valid charter or another Event 15 diplomatic source on the same pair is preserved. Loss records Need and Concord consequences, refreshes external-network and formation proof, and never preserves a charter modifier on a successor-owned state.

## League and external network

The League begins as a lightweight foreign commonwealth, not a free annexation framework. It tracks candidate, observer, member, sponsor, aid, reserve, defense, cohesion, and failure state. A partner's role package may layer compatible duties for the same founder, such as member plus defense, sponsor plus observer, or member plus aid, but only one Event 15 founder may own that active or pending package. Paid actions and role recorders compare every reverse-linked founder's exact role arrays before resources or diplomacy change, so a second founder cannot spend on a package the recorder would reject. Sponsorship is a targeted request with the ordinary variable League response term. The selected major may consent to technical aid, consent to a sponsor-created guarantee, or refuse, and no sponsor is recorded before that exact response returns. Founder-to-member guarantees share the exact-pair creator gate with case, island, association, and autonomy guarantees; member-to-founder and sponsor-to-founder guarantees retain their separate directional provenance. Exit, expulsion, collapse, annexation, and terminal cleanup therefore revoke only the final relation Event 15 created. Technical sponsorship creates no guarantee.

Recognized associates and compacts can support formation proof. Favorable foreign reaction contacts do not count as League members or recognized external partners. Every recognition-bearing League role records a deduplicated package source even when another system already made the partner visible. That source survives while another exact League role remains and is removed after the final role ends; visible recognition then survives only while a live compact or association independently supports it. Full-invitation and reserve-compact answers return through an exact founder-target bridge that requires the League and matching request to remain live, accepts only one valid response flag, and clears the exact request before applying a role. A delayed answer after collapse or terminal teardown therefore clears stale response state without rebuilding the League. Founder-side and partner-side reverse indexes reconcile candidate, invitation, sponsorship, observer, member, sponsor, aid, reserve, defense, compact, association-duty, charter, and wartime-response relationships. Formal defense uses the unique `faction_template_utopia_manifesto_commonwealth_league`; a partner records the exact founder only after it actually joins that template. Exit removes only an attributed template membership, while collapse and terminal teardown require the same template identity before dismantling a founder-led faction. An exact member attack on its founder records an obligation breach. An exact founder attack on its member opens a one-shot leave-or-remain response and records founder consequences. Annexation or exit removes the exact relationship and refreshes cohesion and formation proof without annexing a member or erasing another founder's network.

The League can continue after the founder's institutional collapse through a viable recorded successor. If the founder led a matching faction and the successor is a member, faction leadership transfers before the founder leaves. Terminal Event 15 cleanup then relinquishes founder attribution and runtime flags without making the successor or other members leave the preserved template faction. Members retain their tags, territory, and autonomy.

## Military and auxiliaries

Military growth is paid and bounded. The shared capacity is consumed whether a formation comes from a focus or a decision. The eight formation presentations are Citizen Watch, Workers' Defense Column, Commonwealth Engineer Corps, Household Service Formation, Small Professional Guard, League Defense Group, Auxiliary Service Column, and Commonwealth Field Guard. Both the template definition and every matching deployed unit receive their name through `GetUtopiaManifestoMilitaryFormationName`, so language packs can localise the eight presentations without changing the paid-formation helper.

Thirty-four focuses use the dynamic paid-growth contract: 26 institutional and 8 military. Every caller explicitly cancels if its live gate becomes invalid, refreshes and rechecks the current tier price at completion, pays before creating proof or a formation, and keeps every downstream reward behind the matching payment-success guard. A final-tick affordability change therefore fails closed rather than granting a free milestone. State-control changes refresh ROOT and FROM dynamic costs outside the Fallout-only callback guard, while Ledger, island, and history-sensitive work remains guarded.

Auxiliaries use paid sourcing, capped formation, dependency, incidents, betrayal, demobilization, and cleanup. They are not a free manpower or equipment loop. The No Foreign Hands achievement records their use as a disqualifier.

## Evolutions and event families

The 106 Event 15 definitions cover the opening chain, founding incidents, calling incidents, provision incidents, settlement and island incidents, Necessary Ground, stewardship, the League, consentful sponsorship and wartime League responses, military and auxiliaries, constitutional contradictions, bilateral responses, five evolutions, five evolved openings, foreign reactions, aftermath, the actor pulse, three public news milestones, two hidden founder-rooted annexation bridges, one hidden founder-rooted state-control bridge, and the hidden association-review reservation bridge. Twelve definitions use `hidden = yes`; visible `.221` carries the association review after `.207` releases the reserved slot.

The five evolutions are:

1. Glosses in the Margin
2. Necessary Shores
3. Cities of One Measure
4. Nowhere Made Law
5. The Perfect Island

Each evolution has three interpretation choices, giving 15 choice flags. Active delivery and an explicit prepared prefire choice call the same idempotent setup dispatcher. Each choice unlocks one paid policy action and one shared timed obligation that alters a second existing system. No sixth evolution, second reserve system, free territory, free core, free division, or free equipment grant is used.

The actor-scoped `chaosx.nr15.150` pulse schedules conditional incidents and evolution delivery. Foreign reactions and news milestones use bounded one-shot recipient selection from real route, network, war, or revolt edges.

## Ideas, characters, identities, and achievements

The 50 idea definitions form staged families rather than permanent spirit accumulation. Acceptance starts with three Event 15 ideas. Route, store, property, district, stewardship, and auxiliary helpers replace the relevant family stage, keeping the active Event 15 country-idea count within the accepted three-slot lifecycle.

The 24-character package contains:

- eight founder and successor institutional leader entries sharing four people-free built-in ImageGen institutional tableaux
- sixteen advisors with distinct roles, traits, costs, AI weights, and lifecycle flags

Institutional leaders use people-free built-in ImageGen, vanilla-HOI4-style `156x210` tableaux: empty chambers, council tables, ledgers, standards apparatus, stores, seals, and route emblems represent the governing body without depicting a person, face, crowd, silhouette, statue, or portrait. The sixteen advisors use distinct vanilla-HOI4-style `65x67` dossier cards. Each begins with an independent fictional ImageGen portrait master and separate ImageGen frame and paper/seal overlays. Processor v5.0 only crops, grades, angles, derives alpha shadows, composites the generated layers, validates, and exports. It does not draw the advisor card. Advisor cards are not square portraits and are not resized institutional leader portraits. Focused provenance validation requires every one of the sixteen portrait masters and both overlay masters to exactly match its recorded built-in ImageGen object before processing is accepted.

Formation preserves the original country tag while applying one of five cosmetic identities. Native party names are not overwritten. Four institutional routes install a governing body and later successor body. Practical Commonwealth preserves the saved constitutional group and exact surviving leader. Teardown restores the saved political group, exact surviving leader with the saved ideology subtype, and original election permission before dropping the cosmetic identity.

The 14 achievements are the exact IDs recorded in `docs/specs/015_utopia_manifesto_specs/matrices/achievement_matrix.md`. Each has active base, grey, and not-eligible variants, for 42 current achievement images.

## Repeal, collapse, and aftermath

Total repeal is a paid constitutional course. Formed identities can also enter the aftermath through genuine non-annexed capitulation or constitutional abandonment. Ordinary war does not trigger the aftermath.

The aftermath snapshots the live package, resolves administered territory, chooses a practical legacy, records the public fate of the book, transfers a viable League where possible, and performs complete identity and runtime teardown. Annexation uses a safe terminal state. Cleanup is idempotent and does not create a replacement country, free territory, or substitute leader.

## Super-event

The regional proclamation fires only after route formation, the regional objective, a meaningful external network, and the nontrivial-subject gate.

| Display slot | Route image |
| ---: | --- |
| 96 | Consent of Households |
| 97 | Common Table |
| 98 | Guardians of Measure |
| 99 | Closed Island |
| 100 | The Joke Understood |

All five slots use the title `UTOPIA HAS NEIGHBORS`, the remark `Nowhere has a timetable.`, and Thomas More's closing wish-over-hope judgment from *Utopia* in Gilbert Burnet's translation. Each slot has a route-specific description.

Playback audio ID 57 uses Johannes Brahms, *Symphony No. 3 in F major, Op. 90*, third movement, *Poco allegretto*, performed by the Musopen Symphony Orchestra. The recording is the Event 15-exclusive CC0 source documented in `docs/super_events/015_utopia_manifesto_super_event_audio_research.md`.

All five `457x328` route images exist and are registered in `interface/015_utopia_manifesto_super_event.gfx`. The text, audio, and visual package is wired. The two older two-image presentation files are retained only as historical assets. Their obsolete sprite registrations were removed and they are not selected as fallbacks.

## Asset package

The current asset authority index is `docs/assets/015_utopia_manifesto/manifest.md`. The definitive final asset audit is `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/advisor_asset_final_audit_2026_07_18.md`. It passes the advisor dossiers, active flag and institutional portrait packages, and the separately authored Choice and Assignment animation packages. The July 16 requirement-first report remains supporting evidence for unchanged visual families, not the current audit authority.

Current proof includes:

- 14 registered report images and 3 registered news images
- 5 registered route super-event images
- 124 focus usages across 74 unique focus sprites
- 174 current decision mapping rows covering 9 categories, 121 decisions, and 44 missions, recorded in `docs/assets/015_utopia_manifesto/decision_icon_mapping.csv`
- 165 gameplay decision and mission icon assignments in that current mapping
- 50 ideas using 12 unique pictures
- 14 achievements with 42 active variants
- five required authored-frame packages: 8 Ledger-seal frames, 8 Need frames, 8 Choice frames, 8 Assignment frames, and 10 formation frames
- one additional 8-frame reserve animation retained outside the required-family count
- 46 scripted-GUI sprite references
- 33 static Ledger assets: 4 value icons, 6 Calling icons, 10 case cards, 7 district-role cards, and 6 district-state overlays
- 459 base Event 15 sprite definitions plus 5 route-super-event definitions, with no duplicate names across all 464 registered sprites
- 75 active flag files for five cosmetic families, each with five lookup stems rendered at three sizes
- 4 institutional leader portraits, 16 advisor dossier cards, and 5 League emblems

Every active flag has a genuine built-in ImageGen source. The 21 independent designs and four intentional engine-lookup aliases form flat heraldic flag assets rather than fabric photographs or painterly scenes. Restrained colour finishing, sharpening, and resizing preserve ImageGen-authored geometry and tonal detail. The workflow does not quantize, trace, redraw, substitute motifs, impose a palette ceiling, or replace the generated design with simple shapes.

## Source map

Primary runtime surfaces:

- `events/015_utopia_manifesto.txt`
- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt`
- `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt`
- `common/decisions/categories/015_utopia_manifesto_categories.txt`
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
- `common/mtth/015_utopia_manifesto_mtth.txt`
- `common/wargoals/015_utopia_manifesto_wargoals.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_achievement_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_aftermath_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_country_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_decision_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_identity_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_reachability_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_super_event_effects.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_evolution_delivery_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_prefire_evolution_triggers.txt`
- `common/scripted_triggers/015_utopia_manifesto_reachability_triggers.txt`
- `common/ideas/015_utopia_manifesto_ideas.txt`
- `common/characters/015_utopia_manifesto_characters.txt`
- `common/country_leader/015_utopia_manifesto_traits.txt`
- `common/dynamic_modifiers/015_utopia_manifesto_state_modifiers.txt`
- `common/opinion_modifiers/015_utopia_manifesto_opinion_modifiers.txt`
- `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt`
- `common/countries/cosmetic.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/script_constants/015_utopia_manifesto_country_constants.txt`
- `common/script_constants/015_utopia_manifesto_decision_constants.txt`
- `common/script_constants/015_utopia_manifesto_evolution_consumption_constants.txt`
- `common/script_constants/015_utopia_manifesto_narrative_constants.txt`
- `common/script_constants/015_utopia_manifesto_prefire_evolution_constants.txt`
- `common/script_constants/015_utopia_manifesto_settlement_constants.txt`
- `common/script_constants/015_utopia_manifesto_super_event_constants.txt`
- `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`
- `interface/015_utopia_manifesto_ledger.gui`
- `interface/015_utopia_manifesto.gfx`
- `interface/015_utopia_manifesto_super_event.gfx`
- `localisation/english/015_utopia_manifesto_l_english.yml`
- `localisation/english/015_utopia_manifesto_events_l_english.yml`
- `localisation/english/015_utopia_manifesto_focus_l_english.yml`
- `localisation/english/015_utopia_manifesto_ideas_l_english.yml`
- `localisation/english/015_utopia_manifesto_country_package_l_english.yml`
- `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml`
- `localisation/english/015_utopia_manifesto_evolution_consumption_l_english.yml`
- `localisation/english/015_utopia_manifesto_evolutions_l_english.yml`
- `localisation/english/015_utopia_manifesto_super_event_l_english.yml`

Shared integration surfaces:

- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_triggers/chaosx_settings_triggers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `music/chaosx_super_event_music.asset`
- `sound/chaosx_sound.asset`

Current finalization evidence:

- `docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_source_of_truth_and_resume_2026_07_15.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/completion_coverage_matrix.md`
- `docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_final_improvement_loop_closure_2026-07-18.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/focus_final_audit_2026_07_18.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/decision_final_audit_2026_07_18.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/country_final_audit_2026_07_18.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/localisation_final_audit_2026_07_18.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/advisor_asset_final_audit_2026_07_18.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/spreadsheet_final_audit_2026_07_18.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/spreadsheet_current_hash_followup_2026_07_18.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/documentation_final_audit_2026_07_18.md`
- `docs/plans/015_utopia_manifesto_plans/completion_audit.md`

The earlier dated audits and implementation handoffs remain preserved as historical evidence. They do not override the finalization records above.

## Historical labels

`World Tension Subsides`, `Event 015 Placeholder`, and the older lowercase cosmetic identities survive only in dated planning, catalog-recovery, or asset-history records. They are not current Event 15 names, live cosmetic identities, or runtime visual fallbacks.

## Future plans

- Preserve the final whole-event audit and 53-file runtime-text manifest as the regression anchor when shared systems or catalog artifacts change.
- Preserve the passing Necessary Ground scenario matrix as the regression baseline for later case-system changes.
- Use rendered Ledger and super-event inspections for layout evidence when the optional artifact store is available.
- Extend route-specific AI tuning only after observed balance across small coastal, landlocked, island, subject, and war-pressured recipients.
