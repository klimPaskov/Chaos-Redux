# Event 014 - Cannibalism

Event 014 is a Minor Fire-Once crisis rooted at `chaosx.nr14.1`. It is deliberately outside every event cluster. The dispatcher selects one eligible country already at war, then scores its exposure from dynamic war duration, supply stress, casualties, stability, diplomatic isolation, convoy vulnerability, and occupation conditions. The chosen country receives a military predation crisis that can be contained locally, concealed, exploited, allowed to spread into an international network, or transformed into a playable warlord and unification campaign.

The baseline incident and all three evolutions have separate entry paths. An evolution may deepen an active Event 014 crisis or define the opening state before Event 014 fires. Disabled evolutions do not leak their meters, decisions, countries, Event Details rows, or presentation surfaces into the baseline route.

## Core values

Event 014 uses seven central values. Tuning is defined in the Event 014 script-constant files rather than repeated in events or decisions.

- **Field Hunger** measures material desperation inside the affected formations. War, poor supply, isolation, casualties, and predatory policy raise it. Restored logistics and humane relief reduce it.
- **Command Integrity** measures whether officers, military police, medical services, and civilian authorities still control the affected force. Compromised formations, concealment, and terror exploitation weaken it. Rotation, investigation, discipline, and witness protection restore it.
- **Cult Cohesion** exists only when Evolution I is enabled and active. It measures the strength of the ritual ideology, oath groups, marks, spoils, and internal organizers.
- **Network Reach** is a global measure derived from infected countries, warlord countries, foreign seeds, prison nodes, ports, islands, occupation nodes, rail nodes, formation nodes, and population-consumption milestones.
- **Larder Stores** is a finite resource for cannibal countries. It decays with controlled territory and armed forces and is replenished only by eligible, ledgered population consumption or defined captures.
- **Frenzy** measures predatory operational pressure. Starvation and consumption can raise it. It cannot substitute for Larder Stores or create free recruitment.
- **Network Alignment** measures whether a warlord cooperates with, manipulates, or resists the concealed network and later convergence.

Country and state meters are clamped by shared constants. Weekly processing is limited to countries already participating in Event 014. It does not scan every country through a world-wide daily, weekly, or monthly on-action.

## Baseline crisis and responses

The opening reports missing soldiers, disturbed burial details, broken ration ledgers, and a formation whose conduct no longer matches an ordinary supply emergency. The host chooses among three response families:

1. **Open emergency response** acknowledges the crisis, restores supply, rotates units, protects witnesses and burial parties, separates followers from organizers, and allows public legal accountability.
2. **Conceal and isolate** limits immediate exposure but damages trust and lets records, transfers, and compromised officers survive behind sealed files.
3. **Exploit the terror** weaponizes the perpetrators as shock troops. It produces immediate military leverage at the cost of integrity, public legitimacy, escalation pressure, and later foreign hostility.

The containment category combines immediate decisions with timed logistics and unit objectives. Supply-corridor restoration, formation rotation, prison control, island access, network disruption, convergence interdiction, and transformation-anchor assaults have success, partial-success, and failure outcomes where appropriate. Humane actions include ration relief, medical and burial protection, witness safeguards, conditional amnesty for followers, prisoner screening, victim identification, and long reconstruction. Suppression and public court-martial remain available without treating prisoners or affected civilians as expendable resources.

Local victory requires the affected country to remove the active crisis, resolve its local nodes and formations, and finish the applicable legal, logistical, or suppression obligations. Concealment can end the visible emergency without proving clean containment. Terror exploitation leaves a deliberately corrupted outcome and continuing risk. Worldwide victory requires all active countries, nodes, warlords, convergence structures, and reinfection routes to be removed and the global cleanup resolver to finish.

## Evolution I - Ritualization

Evolution I creates an invented military predation ideology. It is not based on a living tradition, religion, Indigenous practice, or borrowed sacred motif. Cult Cohesion becomes active, oath groups and an internal ritual economy appear, and new actions investigate organizers, separate coerced followers, ban marks and spoils, or exploit the ideology for terror.

An active baseline crisis enters the ritual stage through its own escalation event and preserves all existing meters and response history. A pre-fire Evolution I opening starts with ritual evidence already present and initializes the stronger stage directly. Clean containment must break the organizers and ritual economy rather than merely restore calories.

## Evolution II - Organized Network

Evolution II creates a transnational logistical network without revealing its hidden coordinator. Formation cells, prison cells, port cells, island communes, occupation cells, rail cells, foreign seeds, and cannibal warlord states contribute to Network Reach. Ordinary countries can register cells, inspect prisoner transfers, search ports and convoys, break courier chains, and conduct joint suppression. Cannibal actors can seed foreign formations, redirect transfers, establish silent ports, raise local warbands, and synchronize attacks.

Remote islands and mainland communes have distinct territorial logic. Island nodes require coherent reachable territory and can be blockaded, landed against, and searched for survivors. Mainland communes emerge from usable controlled states rather than arbitrary map transfers. Foreign spread is ledgered per source and target so a country cannot receive the same seed twice from one action, and external reinfection remains possible until the relevant source route is destroyed.

The concealed coordinator is created internally during Evolution II. Before the public reveal flag, no visible event, decision, focus, GUI text, Event Details entry, evolution row, country name, achievement, scenario, portrait, or audio metadata may expose Hannibal Lecter. Internal identifiers remain behind scripted visibility gates and use neutral player-facing presentation.

## Warlord countries

Event 014 reserves eight reusable warlord slots, `CBA` through `CBH`. A slot is allocated only when it is dormant and the candidate state passes ownership, control, population, supply, recovery, and origin checks. The system never consumes a last-state country merely to create a host.

Three origins define territory, military composition, AI, decisions, and focus overlays:

- **Island Host** forms around a coherent island or coastal base and specializes in convoy ambush, ports, landings, and archipelago hunting.
- **Siege Commune** forms around an encircled urban or industrial state and specializes in tunnels, workshops, fortified feeding districts, and attacks on relief columns.
- **March Host** forms around a mobile land corridor and specializes in depot raids, rail sabotage, captured transport, and moving Larder doctrine.

All eight reusable slots are origin-agnostic. CBA through CBH can each receive any of the three geographic origin packages, so a defeated slot can return later with a different territory, leader, region, and origin without retaining the prior incarnation.

Starting divisions and equipment scale from the originating state and current event pressure. Recruitment and reinforcement consume manpower, equipment, command capacity, and Larder Stores. Event 014 does not grant free units. The 68-focus shared warlord tree includes hierarchy, Larder economy, military, expansion, infiltration, network alignment, local-victory, and three origin-overlay families. Route-aware AI chooses coherent combinations rather than mixing mutually exclusive identities.

Every warlord slot has seven regional name-and-portrait variants: Europe, Asia, Africa, Middle East, North America, South America, and Oceania. All 56 portraits are independent fictional HOI4-style bust compositions. They depict bald, bloodied, visibly feral male warlords in invented rough clothing and scavenged period gear, with distinct expressions, behaviors, props, regional cues, and regional names. None uses a prison or detention setting, and none copies living ceremonial dress or an actor likeness.

## Population consumption and recovery

State consumption uses the shared Deaths system and records the exact Event 014 population removed. The resolver checks usable population, ownership, control, current recovery, prior consumption, and transaction flags before applying loss. It prevents duplicate consumption, concurrent double-spending, Larder yield from unusable states, and recruitment that bypasses manpower or Larder costs. A country receives Larder Stores only from the population loss actually applied after eligibility and route multipliers.

Liberated feeding states pass through long recovery stages: emergency liberation, identification and burial, institutional reconstruction, and long-term trauma. Reconstruction decisions restore administration and infrastructure gradually. The cleanup resolver removes Event 014 operational modifiers and pointers without erasing recorded deaths, memorial obligations, or aftermath history.

## Evolution III - Public convergence

Evolution III opens a warning period before unification. Countries can identify convergence routes, interdict a prospective host, sever command relays, break foreign nodes, and reduce the readiness score. Host selection scores viable cannibal countries by territory, military strength, Larder Stores, network alignment, route history, and player-control safety. The resolver preserves control of a human-controlled cannibal or Wendigo country rather than silently transferring the player to an AI tag.

The reveal publicly identifies Hannibal Lecter and unlocks the reveal super-event, portrait, character, country identity, decisions, focus content, Event Details text, evolution row, achievements, and audio metadata. Warlords can submit with retained command, surrender their warbands, bargain for autonomy, resist, or challenge the unifier. Submission and resistance have distinct territorial, army, character, and political outcomes. Later warlords can also be absorbed through the same disposition rules.

The unified country inherits territory, divisions, surviving characters, technologies, ideas, route choices, cells, and stored Larder value through explicit transfer effects. Its 108-focus tree covers convergence politics, warlord disposition, supreme hierarchy, continental Larder doctrine, army, navy, air, intelligence and cells, expansion, world counterwar, and the ordinary terminal route. Completed cannibal routes are intentionally absurd and overpowered, but they are gated by difficult progression, world hostility, finite Larder pressure, counterplay, territorial requirements, and terminal checks.

Every successful absorption also calls the shared additive technology-union helper before donor cleanup and annexation. CBL and transformed ZZZ keep their existing technologies, research slots, and established mutually exclusive industry branch while gaining every other compatible researched technology token from the absorbed constituent. Autonomous, resistant, or challenging warlords transfer nothing until a later transaction actually absorbs them. Completed special-project state is outside this token-transfer contract, while the in-place ZZZ transformation preserves its own existing special-project state.

## Unified operational contracts

The post-reveal tree uses three focus cadences: short focuses cost 3 focus units and take 21 days, normal focuses cost 5 units and take 35 days, and terminal focuses cost 8 units and take 56 days. This shorter post-reveal cadence is balanced by hard operational gates. Completing a focus changes a concrete decision cost, stockpile requirement, target lock, receipt cap, mission goal, operation duration, modifier strength, hostility result, or terminal proof requirement. Focus flags are not treated as generic capacity rewards.

The command profile shapes absorption, governors, rival purges, continental commands, and their timetable. The Larder profile shapes storage, captured workshops, the feeding capital, all four population-consumption doctrines, exhausted-frontier abandonment, mission pacing, and battlefield receipts. Army, navy, and air profiles shape paid recruitment, operational reserves, rout and convoy receipts, enemy-front collapse, silent anchorages, and temporary combat modifiers. Cells, expansion, and counterwar shape target pools, lockouts, foreign disruption, terror ultimata, border incidents, postwar integration, coalition-command attacks, and hostility conversion.

Population-backed actions continue to use the exact Deaths transaction. Cannibal Legions, Bone Guards, and independently selectable Island Reavers, Siege Eaters, and March Predation Columns are created with zero starting manpower and zero starting equipment. Their exact population loss becomes manpower only after the Deaths resolver confirms the complete transaction, while their Larder and stockpile gates remain real costs. Each learned origin has its own recruitment decision, knowledge gate, raised counter, and cap.

Three harvest ledgers prevent repeatable receipt fabrication:

- Battlefield receipts come only from distinct enemy-country capitulations recorded in the unified host's defeated-country array. Repeated callbacks for the same country do not issue another receipt. Battlefield processing spends a receipt once harvest caps apply, and victory scaling changes the bounded receipts earned per distinct victory.
- Paid Continental Hunts issue at most one rout receipt after rout-harvest missions open. Collapsing an enemy front spends that receipt once the rout cap is active and also places a target cooldown.
- Paid Continental Naval Hunts issue at most one convoy-hunt receipt after the convoy tables open. Processing the receipt spends it, adds the defined Larder yield, and has its own 90-day cooldown.

World Hostility is persistent pressure rather than display-only state. At 25, 50, and 75 it applies progressively stronger consumer-goods, supply, organization, political-power, and command penalties. It adds command, Larder, support-equipment, fuel, equipment, truck, convoy, and airframe surcharges and gives foreign targets increasingly strong temporary defence and organization counterpressure. The system refreshes from focus completion and paid operations and does not use a daily, weekly, or monthly world scan. Paid counterwar operations reduce Hostility, the capstone strengthens that relief, and Counterwar Conversion spends a larger mobile reserve to convert 15 Hostility into 5 Unified Authority.

The four ordinary Last Table packages are hard gates rather than focus-completion rewards:

- Larder: complete 5 successful paid Larder operations.
- Army: raise 5 Cannibal Legions, raise 1 Bone Guard, and complete 5 paid army operations.
- Expansion: prepare 5 campaigns, complete 3 postwar integrations, and complete 5 cell operations.
- Counterwar: complete 5 paid counterwar operations.

Final Global Mobilization and Dismantle the Ordinary World retain the strict global Chaos requirement of greater than 1000 in addition to all four operational packages. The consolidated focus audit records 316 distinct country flags set by focus-prefixed helpers across the three trees, with at least one live consumer for every flag.

### Unified target selection and icon coverage

Two country scorers, `cannibalism_unified_target_scorer` and `cannibalism_wendigo_target_scorer`, share their hard-validity factors with two MTTH decision-weight entries. Six unified targeted decisions consume `cannibalism_unified_target_decision_weight`: foreign army seeding, global campaign preparation, terror ultimata, border incidents, coalition-hub destruction, and enemy-front collapse. The Wendigo profile has distinct pre-lock and post-lock priorities.

The pre-lock scored AI package intentionally uses fixed first assignment. A valid target receives its band once and newly valid targets can be added later, but the engine provides no scripted removal path, so an existing pre-lock target is not dynamically removed or re-banded when its score changes. The terminal lock applies a separate one-time post-lock escalation package. This is resolved intentional design, not an open audit finding.

All 38 unified decisions use their own deterministic `GFX_decision_<decision_id>` sprite and matching `gfx/interface/decisions/014_cannibalism/decision_<decision_id>.dds`. No unified decision reuses a baseline, focus, idea, or unrelated decision icon.

## Wendigo unification

Event 014 discovers and preserves the existing Wendigo country rather than recreating it. Its units, technologies, ideas, recruitment systems, national identity, and active player control are retained. At the merger, ordinary cannibal inheritances, surviving warlords, cells, and Larder Stores are added without deleting Wendigo content. Additional Wendigo training, anchor states, a transformation countdown, and pre-lock counterplay form a separate 28-focus overlay.

The transformed Hannibal Lecter presentation remains reveal-gated. It uses a distinct animated portrait and a visibly inhuman frozen form without borrowing living Indigenous traditions or sacred motifs. Coalition countries can identify, disrupt, assault, and destroy transformation anchors, break recruitment sites, and interfere with frozen supply corridors before the lock. Once the terminal form locks, its military package is intended to be effectively undefeatable.

The transformation mutates the existing original ZZZ country in place. It preserves ZZZ territory, units, technologies, ideas, equipment, and Event 2 profile state, but immediately disables normal queue recruitment for the locked 16-battalion `Wendigo Pack` before the first overlay focus. Pack recruitment is paid-only after the merge. The ordinary two-Pack muster and the receipt-backed one-Pack muster both validate the complete requested batch against the shared capacity before any population or Larder transaction.

The pre-lock route records each distinct enemy capitulation won after the Winter Network activates. These recorded winter victories supply the countdown gate and cannot be earned from repeated state turnover. Enemy-death receipts are bounded permission tokens. They begin from a non-retroactive snapshot, issue from each full 50,000 new casualties while the country remains an active enemy, cap at two per enemy epoch and five held receipts, and reset the sampled epoch on peace, re-war, route break, terminal lock, or receipt shutdown. A receipt muster still pays exactly 100,000 controlled usable-state population through the canonical Deaths transaction, one receipt, 200 Larder, 500 infantry equipment, and 100 support equipment to create one zero-start Pack.

The existing 28-focus overlay also applies three idempotent Pack support stages, three inherited origin-template upgrades, and two inherited commander stages. `cannibalism_activate_inherited_winter_cell` is a paid targeted operation against a current enemy that already contains an inherited Event 014 cell. It creates sixty days of disruption and can add one bounded pressure contribution to the active terminal hunt, but it does not create a cell, population, Larder, equipment, a unit, or a war goal.

The terminal-hunt family has four maintained surfaces: launch, the 120-day mission, paid pressure, and defender break. Success comes from target capitulation or capital control at full hunt pressure. Failure can come from defender counterpressure, timeout, route break, invalidation, or loss of all anchors. A success adds only five transformation progress, a failure removes ten, and neither path can set `world_end`. The final lock remains owned by the transformation pulse.

## Terminal routes and defeat aftermath

Both world-end branches require Chaos greater than 1000, their full route prerequisites, and terminal gates. The ordinary route unifies the cannibal network into a global war machine. The Wendigo route locks the transformed winter network. Each sets the shared world-end state, begins global war, applies its own country identity and terminal package, and fires unique news, image, super-event, and licensed 44.1 kHz audio.

Event Details exposes two independent post-reveal terminal rows. Scenario ID `6`, **The World Is the Larder**, controls only the ordinary terminal branch and maps to super-event ID `50`. Scenario ID `7`, **No Thaw Will Come**, controls only the Wendigo terminal branch and maps to super-event ID `53`. Each row is default enabled, persists its own disabled state, opens its own detail panel, and gates only its matching automatic terminal selection. Neither row is visible before `cannibalism_reveal_complete`.

The four action-scene super-events and their unique audio IDs are Hannibal's reveal `49`, the ordinary world end `50`, eligible global defeat `52`, and the Wendigo world end `53`. Their registered 44.1 kHz OGG and WAV files use separate sourced recordings and separate visual compositions. ID `51` remains assigned elsewhere and is not part of Event 014.

Before terminal lock, the world can defeat the revealed command or break the Wendigo transformation. Eligible victors receive a distinct global-defeat aftermath only after the exact defeat predicates are recorded. Captured warlords and Hannibal Lecter have explicit custody or death outcomes. Recovered states retain their death ledgers and reconstruction obligations. An international inspection compact, memorial work, victim identification, and long recovery prevent victory from erasing the cost of the crisis.

## Scenario, achievements, AI, and integrations

Scenario `SCN-010` supports five launch types: Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence. Each manual launch first builds a mutation-free manifest of every required actor, opening-state capacity, island node, origin state, and reusable CBA-CBH slot. Planned origin states exclude every planned actor country, so canonical actor initialization cannot consume a later warlord state. The commit begins only when the manifest exactly matches the selected type and intensity. A failed preflight records setup failure without initializing the Event 014 runtime, actors, nodes, evolutions, warlords, or launch history. Automatic pre-fire convergence keeps its existing dynamic selection path.

The event catalog row at `Events!A15:M15` records Cannibalism as `Minor Fire-Once` with an empty cluster field. Its Event Details text, three evolution entries, and both terminal descriptions mirror the corresponding in-game localisation. After the public reveal, The World Is the Larder and No Thaw Will Come appear as separate clickable world-end rows with independent automatic-selection checkboxes. `Events!M15` and `Scenarios!F10` both record `Fully Functional` after the final audit and catalog promotion.

Event 014 defines 18 predicate-based achievements covering clean containment, repeated prevention, multi-front response, island recovery, reinfection, humane use of defectors, warlord play, unification, Larder progression, reveal prevention, ordinary and Wendigo defeat, both terminal routes, global burial work, and preventing an empty-state outcome. Five baseline achievements remain visible in the normal achievement registry and thirteen late-route achievements remain statically hidden there. A separate read-only decision tracker mirrors all 18 at their correct public stages and reads the real achievement completion triggers. Tracker entries have no costs, effects, cooldowns, completion hooks, or AI behavior.

Eight maintained mission families are live: supply-corridor restoration, formation rotation, investigation, prison defense, island access, network disruption, convergence interdiction, and transformation interdiction. Seven additional paid action families cover officer replacement, ritual-cell infiltration, ritual-economy disruption, silent-island reconnaissance, feeding-state liberation, submission preparation, and resistance preparation. The maintained missions preserve their targets and generation state, cap progress, and resolve full, partial, failure, timeout, and cancellation paths. Incarnation reset begins with one idempotent cleanup effect covering all 14 timed missions: the two baseline missions, six maintained objectives, compact vigilance, four unified receipt missions, and the Wendigo terminal hunt. Terminal global target cleanup runs only for the country that owns the active hunt, so resetting another country cannot disturb an unrelated actor's hunt.

Every custom paid decision is exact-balance safe. Static decision families pair the displayed and deducted cost with an adjacent strict gate one fixed-point step lower, while unified-country gates are derived from the final route- and hostility-adjusted runtime costs after all modifiers. Larder and stockpile checks use inclusive comparisons. Air-program experience and airframe gates are progression alternatives for establishing the program and are not deducted by the foundation action.

The exact evidence contracts and transfer rules are documented in `docs/achievements/014_cannibalism/achievements.md`.

Ordinary governments, foreign responders, the three warlord origins, unified command, and Wendigo command have route-aware AI. Shared world threat influences sanctions, joint operations, counterwar, and terminal hostility. Event 014 also interacts with Death, zombie/Wendigo systems, Fury and war pressure, famine, locusts, disease, natural disasters, camps and detention sites, chemical and biological warfare, fallout, and recovery relief. Nonhuman and incompatible terminal actors are excluded from ordinary infection and population consumption.

## Event history and player surfaces

The event log records the opening host, evolution changes, node and warlord milestones, local containment, reinfection, reveal, unification, terminal routes, global defeat, and cleanup. Event Details shows the current actor, stage, meters, response posture, network state, and legal aftermath. Pre-reveal entries use neutral language and neutral imagery. Reveal-gated surfaces switch atomically when the public flag is set.

The scripted GUI presents the early crisis meters, network alerts, selected targets, cannibal command values, convergence warning, revealed command, and Wendigo transformation. Twelve non-portrait animated packages have independently authored source frames, sheet DDS files, static fallbacks, preview GIFs, contact sheets, manifests, and `.gfx`/`.gui` handoffs. The live ordinary and transformed character sprites use `gfx/leaders/014_cannibalism/hannibal.dds` and `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` directly. Each leader animation begins with that exact supplied portrait as frame `000`. The ordinary sheet adds 11 image-generated action states and the transformed sheet adds 15. Both play at 12 fps with `gfx/FX/buttonstate_blendframes.lua`. The complete package therefore contains exactly 14 semantic animation packages and 142 genuine source plus 142 processed frames. No package is transform-only motion.

## Visual and audio inventory

The exhaustive filename-level inventory is maintained in `docs/specs/014_cannibalism_specs/matrices/asset_inventory_matrix.md` and the production packages under `docs/assets/014_cannibalism/`. Exactly one dedicated Event 014 registry, `interface/014_cannibalism.gfx`, holds the consolidated event sprites. The two required shared registries are `interface/chaosx_pictures.gfx` for reports and news and `interface/chaosx_super_events.gfx` for super-events, so exactly three GFX files reference Event 014 textures.

The Event 014 runtime surface is consolidated from 93 dedicated script, GUI, and localisation loader files to 23 merge-safe files. The 23-file result is the practical minimum of one dedicated file per incompatible HOI4 loader schema, including separate `.gui` and `.gfx` files. Per-tag country/history files, engine-required flag ladders, binary assets, and shared global registries remain structurally separate and were not counted or falsely described as merged.

| Asset family | Runtime location | Stable code-facing names |
|---|---|---|
| Decision categories, panels, and action icons | `gfx/interface/decisions/014_cannibalism/` | `GFX_decision_category_cannibalism_*`, `GFX_cannibalism_*_category_panel`, `GFX_decision_cannibalism_*` |
| Ideas and dynamic modifiers | `gfx/interface/ideas/014_cannibalism/` | `GFX_idea_cannibalism_*` |
| Unified, warlord, and Wendigo focuses | `gfx/interface/goals/014_cannibalism/` | `GFX_goal_CBL_*`, `GFX_goal_cannibalism_warlord_*`, `GFX_goal_ZZZ_wendigo_*` |
| Achievements | `gfx/achievements/` | the 18 `GFX_achievement_014_cannibalism_*` triplets registered in `interface/014_cannibalism.gfx` |
| Reports and news | `gfx/event_pictures/014_cannibalism/` | `GFX_report_event_cannibalism_*`, `GFX_news_cannibalism_*` |
| Warlord and revealed portraits | `gfx/leaders/014_cannibalism/` | `GFX_portrait_CBA_warlord_europe` through regional `CBH` variants, `GFX_portrait_CBL_hannibal`, `GFX_portrait_ZZZ_hannibal_wendigo` |
| Flags | `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/` | CBA-CBH, CBL, and the registered cosmetic-tag flag set |
| Scripted GUI statics and animations | `gfx/interface/014_cannibalism/` | `GFX_cannibalism_*`, including meter, warning, route, portrait, and terminal sheets plus static fallbacks |
| Super-events | `gfx/super_events/014_cannibalism/` | reveal, ordinary world end, global defeat, and Wendigo world end |
| Super-event music and sound | `music/014_cannibalism/`, `sound/014_cannibalism/` | audio IDs 49, 50, 52, and 53 |

The four super-event images are action scenes rather than posed tableaux. The reveal shows a violent convergence breaking barricades and chasing civilians under Lecter's command. The ordinary world end shows a capital overrun in motion. Global defeat shows a kinetic coalition breakthrough, opened cages, and escaping civilians. The Wendigo world end shows the transformed command leading a distorted frozen pack through a collapsing defense. Generated victims are fictional adults, and no image uses real atrocity photography or identifiable people.

The final closure asset pass adds 21 distinct preregistered surfaces: 13 maintained objective/action icons, two achievement-tracker textures, four terminal-hunt icons, the receipt-backed Pack icon, and the inherited winter-cell icon. The full runtime asset tree contains 56 unique regional warlord portraits, 204 focus icons, 18 achievement triplets, four super-event images, two real-frame leader portrait sheets, and 195 unique runtime flags derived from 65 separate built-in ImageGen masters. The current portrait and flag refresh preserves the registered runtime paths while replacing their image content and provenance packages.

Event 014 adds no custom subunit or equipment identifiers. Its scripted formations retain existing battalion and equipment surfaces, so no bespoke unit counter, subunit icon, or equipment art is required. This is a verified scope disposition, not a fallback.

## Principal implementation files

- Entry events, escalation, aftermath, news, and super-event dispatch: `events/014_cannibalism.txt`.
- Selection, meters, staging, population, spread, unification, Wendigo, aftermath, GUI, achievements, and integrations: `common/scripted_effects/014_cannibalism_effects.txt` and `common/scripted_triggers/014_cannibalism_triggers.txt`.
- Player actions: `common/decisions/014_cannibalism_decisions.txt` and `common/decisions/categories/014_cannibalism_categories.txt`.
- Country packages: `common/country_tags/014_cannibalism_countries.txt`, `common/characters/014_cannibalism_characters.txt`, Event 014 ideas, leader traits, dynamic modifiers, dormant history, flags, and name lists.
- Focus trees: all three tree roots live in `common/national_focus/014_cannibalism_focus.txt`.
- UI and localisation: `common/scripted_guis/014_cannibalism_scripted_gui.txt`, `interface/014_cannibalism_frontline_hunger.gui`, `interface/014_cannibalism.gfx`, and `localisation/english/014_cannibalism_l_english.yml`.
- Central tuning: `common/script_constants/014_cannibalism_constants.txt` and `common/mtth/014_cannibalism_mtth.txt`.

## Validation boundary

The current country-package, decision/mission, focus-tree, localisation/asset, spreadsheet, improvement-loop, and documentation consolidation re-audits dated 2026-07-15 report P0/P1/P2/P3 all at zero. They cover the three-origin package, player-safe unification, exact-balance paid actions, exact 14-mission reset, atomic manual-scenario preflight, 68/108/28 focus surfaces, accepted addenda, and the current asset inventory. Older same-day audits and `event014_final_completion_audit_2026-07-13.md` are preserved only as superseded checkpoints. Documentation and filesystem validation confirm the identifiers, file sets, trigger/effect paths, asset registration, catalog promotion, and audit dispositions described above. No in-game runtime session is claimed by this documentation reconciliation.

## Future plans and extension ideas

Future expansion should preserve the completed route boundaries and reveal secrecy. Suitable extensions include more origin-specific postwar reconstruction events, additional diplomatic negotiations around inspection access, regional variants for coalition operations, and more warlord-character consequences after capture or submission. New content should deepen existing ledgers and route consequences rather than add untracked population loss, free recruitment, generic cloned focuses, or another global polling loop.
