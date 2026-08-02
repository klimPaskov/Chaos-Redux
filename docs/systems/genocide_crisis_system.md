# Camp Repression Network, Deaths, Discovery, and the Repression Ledger

## Overview

The camp repression rework connects detention sites, forced labor, gulags, experiment programs, contaminated killing sites, discovery, condemnation, reform, and postwar accountability into one optional network. Ordinary campaigns remain quiet until a government activates or inherits a network, expands it, loses control of it, exposes it publicly, or reaches a crisis threshold.

The system preserves three established contracts:

- population harm is reported through the Chaos Meter Deaths pipeline and removes real state population;
- evidence keeps the authority stored in `genocide_responsible_country`, even after control or ownership changes;
- foreign condemnation requires discovered evidence, deliberate public use, or an explicit crisis or legal-exposure route.

The system never offers a protected-class target selector. State selection is based on occupation, non-core status, colonial administration, borderland or periphery status, prison-labor infrastructure, political-opposition pressure, resistance, and country-specific territorial history.

## Core Lifecycle

1. A decision, event, historical marker, inherited network, or country bridge identifies a valid state pool.
2. Dormant historical markers remain inert until a route activates them. They do not inflict recurring harm or create ordinary popups.
3. Activation stores the responsible country, site type, phase, evidence state, and country-kit pool; the state is added once to `global.genocide_active_camp_states`.
4. The existing host-only Chaos Meter monthly pulse calls the camp dispatcher. No separate daily, weekly, or monthly world-country loop is used.
5. The registered-state processor applies the resolved population loss once, reports it through the shared Deaths helpers, updates labor and resistance pressure, and deepens hidden evidence.
6. The responsible-country processor updates guard, transport, supply, administrative overextension, stability, legitimacy, reform, and country-specific pressure.
7. Enemy capture, inspection, public use, outbreak exposure, crisis exposure, or a country legal route can reveal evidence. Ordinary operation does not create passive foreign condemnation.
8. Discovery reads `genocide_responsible_country`, exposes stored hidden atrocity and cover-up pressure, and records the state as discovered without recurring report spam.
9. Reform and dismantlement freeze expansion, close active sites, remove active registration, preserve the historical record, and convert active burdens into reform, redress, or legacy outcomes.

## Site Types and State Pools

The shared layer distinguishes dormant, detention, labor, radicalized, gulag, experiment, and contaminated sites. Existing buildings remain the physical anchors:

- `concentration_camp`
- `extermination_camp`
- `gulag_labor_camp_network`

Scripted markers extend those buildings where a country program needs a laboratory, famine, relocation, concession, colonial, or evidence-only state without creating a duplicate building type.

Pool ordering is country-specific and deterministic for AI selection. Occupied and non-core pools are preferred over colonial or emergency pools; core fallback is used only by routes that explicitly permit it and carries lower output, higher stability damage, stronger resistance, and greater reform pressure.

## Building Icon Assets

The concentration-camp and extermination-camp buildings use distinct custom artwork on both building-icon surfaces. Both families follow the vanilla HOI4 building language: compact ochre pictograms, chunky painterly highlights, and—on the indexed strip—the standard charcoal beveled tile.

- `GFX_building_concentration_camp` reads `gfx/interface/buildings/building_concentration_camp.dds` as a native `27x23` standalone icon.
- `GFX_building_extermination_camp` reads `gfx/interface/buildings/building_extermination_camp.dds` as a native `27x23` standalone icon.
- `GFX_buildings_strip` reads `gfx/interface/buildings/building_icon_strip.dds` as a `35`-frame strip of `46x46` frames.
- Strip frame `34` belongs to `concentration_camp`; strip frame `35` belongs to `extermination_camp`.

The standalone sprite aliases are registered in `interface/chaosx_buildings.gfx`, while the indexed strip is registered in `interface/countrystateview.gfx`. The corrected HOI4-style source art, direct vanilla comparison, transparency review, frame-order review, final hashes, and prompt provenance are recorded in `docs/plans/system_camp_repression_rework_plans/subagent_handoffs/2026-08-02_camp_building_icon_hoi4_style_correction.md`.

Future visual extensions should preserve the existing frame order and append new building frames at the end of the strip. A later gulag-network art pass should remain a separate building-icon requirement rather than reusing either camp icon.

## Deaths and Population Damage

Every recurring or immediate population-loss action enters the Chaos Meter Deaths system. The state owner receives the population-loss record and real state population reduction; the stored responsible country receives hidden evidence, later condemnation, and tribunal responsibility. This distinction is important in occupied China, Manchuria, the Raj, North Africa, Libya, the Congo, occupied Poland, and Soviet borderlands.

Recurring harm is owned by the registered monthly state processor. Decisions and events can create a distinct immediate burst, but they do not duplicate the recurring monthly tick. Recruitable-population and stability modifiers represent institutional burden; they are not substitutes for population deaths.

The player-facing Deaths summary continues to group camp, forced-labor, gulag, chemical-site, and biological-site losses through the existing reason mappings.

Terminal Hazard Doctrine can increase an existing camp network's resolved death multiplier by 1.25 only while the stored responsible country also maintains Unrestricted Chaos Warfare. The calculation still begins from the camp system's own buildings, escalation, policy, site, and country-program inputs and retains its 3.50 cap. This integration cannot create or unlock a camp, extermination building, experiment site, restricted chemical site, or occupation law, and it does not modify evidence, discovery, resistance, Condemnation, or the responsible-country record.

## Chemical and Biological Killing Methods

Radicalized networks can develop abstract chemical and biological killing capacity. The method layer is a strategic pressure system, not an operational recipe.

Chemical methods cover chlorine, phosgene, mustard gas, lewisite, tabun, sarin, and soman. Biological methods cover anthrax, tularemia, plague, and smallpox. Availability follows existing technology, special-project, equipment, and site gates. Activation and upkeep consume the corresponding stockpile or program capacity.

Biological method potency follows `Tularemia < Anthrax < Plague < Smallpox`, and only Smallpox is severe. This method is abstract camp killing and accountability pressure, not a battlefield or strategic release route, so activating it does not seed an ordinary biological lifecycle episode. Its stock use, deaths, evidence, resistance, discovery, tribunal, and responsible-country records remain owned by the camp system.

Each method changes a site's resolved harm, supply burden, accident pressure, evidence depth, discovery severity, resistance, stability damage, and tribunal exposure. Shortages reduce controlled output while worsening administrative and accident pressure. Chemical accidents may use the existing contamination system when an exact accident route is implemented; biological accident pressure remains a camp safety and discovery record unless an exact state-scoped release supplies the complete ordinary-lifecycle contract. The monthly state processor still owns the single recurring harm tick.

AI use is capped separately for active, radicalized, experiment, contaminated, and concurrent-project sites. Reform, discovery, supply failure, excessive overextension, or loss of route validity stops expansion and can expose shutdown or dismantlement actions.

## Discovery, Condemnation, and Responsibility

Every active state stores `genocide_responsible_country`. Responsibility survives occupation, liberation, and ordinary ownership changes. A secondary responsibility record is used only by the explicit Germany/Vichy collaboration path.

Evidence is layered rather than binary. Site type, accumulated deaths, concealment, records, experiment activity, contaminated methods, famine pressure, and failed destruction attempts deepen the record. Discovery can occur through:

- enemy control of a valid evidence state;
- inspection, court, review, liberation, or post-collapse routes;
- public use or a country-specific crisis exposure;
- Pingfang outbreak or retreat records;
- Auschwitz and Mengele-linked capture;
- Soviet famine, gulag, or successor archives;
- colonial reckoning and concession records.

The first severe exposure can use a bounded report, news card, or super event. Repeated discoveries update evidence and condemnation silently. There is no recurring leak, refugee, sabotage, or minor camp report roll in ordinary monthly processing.

## Country Packages

### Germany and Auschwitz

Germany prioritizes strict occupied-Poland prisoner-source states before wider occupied and non-core pools. Auschwitz is the shared destination node in state `88`; source-state transfers do not relabel the source as Auschwitz. The occupied-Poland expansion, eastern fortification labor, SS laboratory annex, and military-review branches use timed missions and resource costs.

Auschwitz experiment pressure reads both `mengele_autonomy` and `mengele_permission_level`. Rejected authority blocks transfer; restricted, limited, full, and bypass authority produce distinct autonomy, evidence, project, and coup pressure. Facility registration marks the actual selected state. The cloning unlock remains gated and retried through the Mengele event pulse rather than completing a project directly. Capture of a qualifying laboratory state can feed the existing emergency Directorate revolt.

The associated Germany focus rewards use a consolidated lifecycle. The future-state, territorial-command, and foreign-science lanes never require more than three stable national spirits before convergence; world-order launch removes the lane ideas and grants exactly one final spirit. The core variant preserves the exact science-and-force totals. Stage-specific final variants preserve the exact highest completed optional territorial stage through reclamation, continental dominance, the command spine, or full world dominance. The consolidation adds no new command prerequisite and never grants a higher stage early.

### Japan, Ishii, and Pingfang

Japan uses Shiro Ishii influence, Kwantung autonomy, experiment-site count, evidence depth in China, outbreak risk, and tribunal severity. State `328` is the Pingfang anchor. States `716` and `611` remain separate labor precedents.

Manual and AI pool order is Chinese or Manchurian occupied states, then other colonial occupation states, then a desperate home-island fallback only when the foreign pools are empty. Subject-controlled states are valid and retain owner-linked Deaths attribution. Japan has a five-project dossier chain, Pingfang authority and records events, outbreak containment, army review, retreat evacuation, destruction, surrender, and tribunal outcomes. Obsolete Ishii and outbreak aliases migrate once into canonical values.

### Soviet Union, Gulags, Paranoia, and Famine

The Soviet package uses the accepted northern, Siberian, Far Eastern, steppe, Central Asian, borderland, industrial, and political-opposition pools. `paranoia_pressure` is a projection of vanilla `SOV_paranoia`; the camp system never starts or maintains a second paranoia system.

Gulag expansion, prisoner transfers, NKVD authority, quota pressure, grain confiscation, famine relief, party review, military prisoner release, dismantlement, concealment, and admission of administrative collapse share one lifecycle. Famine pressure persists at country and state level and inflicts its monthly Deaths tick once.

The Union Crisis bridge always records repression memory and grievance. Beneficial Moscow-authority or obedience relief is capped at `8`, grants only the remaining amount, and stops at total-collapse threat `86`, terminal collapse, or inactive crisis. Post-collapse and invasion records preserve famine, deportation, old-movement, and foreign-evidence consequences for successor politics.

### United Kingdom and the Raj

The British package prioritizes Raj detention states and Indian Ocean security states before a colonial emergency fallback. It includes survey, activation, military labor works, manpower levy, dominion coordination, guard allocation, prisoner release, reform, and dismantlement. India or the Raj receives local labor burden and autonomy pressure while Britain receives the administrative benefit and imperial legitimacy cost.

### United States

The United States route requires war, a valid homeland or Pacific threat, sabotage fear, or severe chaos. Military-security-zone and interior pools are geographic and strategic. The route includes relocation authority, labor administration, court review, termination, redress, compensation, record access, and civil-liberties recovery. AI activation is rare and post-threat termination is favored.

### France, Vichy, and North Africa

Democratic and Free France use inspection, legacy review, liberation, reform, and reckoning. Vichy or authoritarian France uses internment, collaboration transfers, North African labor, rail projects, and refugee-pressure management. German secondary responsibility is stored only by the explicit collaboration transfer. North African and colonial pools are exhausted before a penalized metropolitan fallback.

The live France pool API is `is_france_camp_legacy_pool_state`, `is_france_north_africa_labor_pool_state`, `is_france_vichy_internment_pool_state`, `is_france_other_colonial_labor_pool_state`, and `is_france_core_fallback_pool_state`. Selection uses `camp_rework_select_france_legacy_state`, `camp_rework_select_france_new_repression_state`, `camp_rework_select_france_active_state`, and `camp_rework_select_france_north_africa_active_state`.

### Italy, Libya, and East Africa

Italy uses Libyan and East African colonial pools for desert administration, roads, forts, ports, supply links, security battalions, transport guards, closure, local release, compensation, and records. `ita_authorize_homeland_emergency_detention` is a distinct emergency route into the penalized Italian core fallback; it does not make Italian cores valid colonial-project targets. `ita_expand_desert_transport_guard` is the dedicated colonial transport-guard action. Regime change and discovery expose closure and reform behavior.

The live Italy pool API is `is_italy_libya_repression_pool_state`, `is_italy_east_africa_repression_pool_state`, `is_italy_balkan_occupation_pool_state`, `is_italy_colonial_project_pool_state`, and `is_italy_core_fallback_pool_state`. The colonial-project pool is the Libya-or-East-Africa union. Selection uses `camp_rework_select_italy_new_colonial_state`, `camp_rework_select_italy_core_emergency_state`, `camp_rework_select_italy_active_colonial_state`, and `camp_rework_select_italy_project_state`.

### Belgium and the Congo

Belgium prioritizes Congo concession states, including valid subject-controlled territory. Concession quotas, resource routing, transport corridors, strike response, inspection, reform, compensation, and local administration change both Belgian output and Congolese burden or autonomy pressure. A non-Congo colonial emergency pool is secondary and does not start the Congo quota mission.

### Generic Users

Generic authoritarian users require a real occupation, resistance, wartime, doctrine, or severe-crisis gate. Their pool order is occupied non-core, colonial or subject, prison-labor or political-opposition states, and finally the explicitly penalized core fallback. The kit includes activation, quotas, labor projects, guards, evidence destruction, radicalized escalation, contaminated escalation, reform, and dismantlement. AI use is conservative and capped.

## Player Actions and Dispatcher

The final 2026-07-11 inventory contains 84 player actions: 29 Germany/Japan/Soviet actions, 43 U.K./U.S./France/Italy/Belgium actions, and 12 generic actions. The closing actions are `fr_support_refugee_and_rescue_networks`, `bel_negotiate_colonial_strike_settlement`, and `generic_inspect_active_site`. The same files contain 41 missions; Ledger show, hide, open, and close are four separate controls. The final decision/mission re-audit passed, and all 32 Ledger country action slots use the same native cooldown gates as their corresponding normal decisions.

All country actions use `camp_rework_route_country_specific_action`. State actions persist their target through the normal country variable `camp_rework_action_state_id`; `camp_rework_prepare_selected_action_state` resolves the pointer, while `camp_rework_dispatch_prepare_colonial_selection` and `camp_rework_dispatch_restore_colonial_selection` adapt subject-controlled states to the existing country payloads without overwriting the player's Ledger selection.

Restricted chemical, biological, radicalized, and extermination routes use the strict helper family in `common/scripted_triggers/camp_repression_rework_triggers.txt`: `camp_rework_country_can_use_radicalized_route`, `camp_rework_germany_can_use_restricted_method_route`, `camp_rework_japan_can_use_restricted_method_route`, `camp_rework_country_can_use_restricted_method_route`, `camp_rework_country_has_explicit_extreme_doctrine_route`, and `camp_rework_fixed_country_can_use_extermination_route`. Fixed country packages require their own program or explicit doctrine route; the generic ideology shortcut cannot unlock them. Chemical and biological actions also require their actual technology, facility, and stockpile capacity.

## AI and Performance

Country initialization resolves active-site, radicalized-site, experiment-site, contaminated-site, and concurrent-project caps into variables and a Boolean expansion flag. Decision `available`, target, and `ai_will_do` blocks share the same cap contracts. Country-specific selectors preserve each package's pool order instead of copying the generic route.

The registered country and state arrays are bounded and clean stale entries. New and released countries initialize through release, puppet, and state-control hooks. Ordinary monthly work uses the existing Chaos Meter host pulse; the only broad state passes are bounded initialization or explicit one-shot presentation operations.

## Repression Ledger

The Repression Ledger is a scripted GUI with five tabs:

1. Overview: network phase, active sites, population loss, labor output, evidence, resistance, overextension, guard, rail, supply, legitimacy, and reform pressure.
2. State Pools: ordered eligible states, pool type, ownership and control, responsible country, burden, block reason, and available actions.
3. Active Sites: registered sites, site type and phase, population-loss band, output, resistance, evidence, and registration state.
4. Country System: Germany, Japan, Soviet, British, American, French or Vichy, Italian, Belgian, generic, and restricted-method program readiness.
5. Discovery & Reform: discovery state, cover-up pressure, tribunal exposure, reform work, and dismantlement controls.

The selected-state card displays a state name plus named site, phase, population-loss, output, resistance, evidence, registration, and enemy-proximity bands. It does not expose raw internal numeric fields. GUI arrays are rebuilt from bounded registered arrays and invalidate stale selected states.

The header displays `[ROOT.GetName]: [GetCampCountryPanelName]` together with the current phase and discovery state. All 24 generated Ledger sprites have live consumers, including scripted visibility for the evidence and reform seals. The 32 country-action slots mirror the native cooldown gates of their normal decision counterparts.

## Events, Super Events, and Achievements

Country report events cover Auschwitz discovery, Pingfang authority and discovery, Kwantung bypass, outbreak, retreat, tribunal, Soviet famine warning and crisis, relief, administrative breakdown, and records discovery. Colonial and generic report or news cards cover the Raj, U.S. relocation review, France and Vichy, Libya, Congo, and global evidence.

Accepted super-event slots are:

- `12`: Angel of Death Directorate revolt;
- `74`: severe global discovery;
- `75`: Soviet famine catastrophe;
- `76`: Pingfang exposure;
- `77`: colonial reckoning.

Each slot has dedicated art, an audio package, localisation, scripted-localisation routing, bounded playback, and cleanup.

Achievements `60` through `69` cover inherited-site closure, liberated records, defeat of the Directorate, Pingfang shutdown, famine relief over fear, Raj reform, U.S. redress, Congo reform, Italian colonial closure, and French or Vichy legacy closure. Each uses a dedicated normal, grey, and not-eligible icon.

## Gameplay Files

Shared implementation:

- `common/script_constants/camp_repression_rework_constants.txt`
- `common/decisions/categories/genocide_crisis_categories.txt`
- `common/decisions/genocide_crisis_decisions.txt`
- `common/decisions/camp_repression_generic_decisions.txt`
- `common/scripted_triggers/camp_repression_rework_triggers.txt`
- `common/scripted_effects/camp_repression_rework_effects.txt`
- `common/scripted_effects/genocide_crisis_effects.txt`
- `common/on_actions/genocide_crisis_on_actions.txt`
- `common/ai_strategy/genocide_crisis_ai_strategy.txt`
- `events/genocide_crisis_events.txt`

Country packages:

- `common/decisions/camp_repression_major_country_decisions.txt`
- `common/decisions/camp_repression_colonial_country_decisions.txt`
- `common/scripted_effects/camp_repression_major_country_effects.txt`
- `common/scripted_effects/camp_repression_colonial_country_effects.txt`
- `common/ideas/camp_repression_major_country_ideas.txt`
- `common/ideas/camp_repression_colonial_country_ideas.txt`
- `common/dynamic_modifiers/camp_repression_major_country_dynamic_modifiers.txt`
- `events/germany_mengele.txt`
- `events/japan_ishii.txt`
- `events/soviet_gulag.txt`

Ledger and presentation:

- `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`
- `common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt`
- `interface/camp_repression_ledger.gui`
- `interface/camp_repression_rework.gfx`
- `localisation/english/camp_repression_rework_l_english.yml`
- `localisation/english/camp_repression_country_kits_l_english.yml`

## Assets

Runtime decision, idea, project, Ledger, report, news, super-event, and achievement textures live under:

- `gfx/interface/camp_repression/`
- `gfx/event_pictures/system_camp_repression_rework/`
- `gfx/super_events/system_camp_repression_rework/`
- `gfx/achievements/`

Registrations live in `interface/camp_repression_rework.gfx`, `interface/special_projects/biowarfare.gfx`, `interface/chaosx_super_events.gfx`, and `interface/chaosx_achievements.gfx`. Source, manifests, contact sheets, generation prompts, and validation records live in `docs/assets/system_camp_repression_rework/`.

The final static package contains 24 Ledger UI assets; 102 processed package icons covering decisions, ideas, projects, and achievement variants; 27 report, news, and super-event identities; and five unique super-event audio tracks. Achievement ids `60` through `69` each have normal, grey, and not-eligible variants.

The Ledger sprites derive from frozen ImageGen sources in `docs/assets/system_camp_repression_rework/source/ui_imagegen/`. The prompts are recorded in `docs/assets/system_camp_repression_rework/prompts/repression_ledger_imagegen_prompts.md`, and `docs/assets/system_camp_repression_rework/tools/build_ledger_ui_assets.py` is the deterministic processor. Optional authored frame animation remains queued. The maintained static UI is the accepted current presentation, not a simple-shape or header-only fallback.

## Documentation and Workbook Alignment

This system is a cross-event rework rather than a standalone `chaosx.nr<ID>` event. The event workbook remains aligned through the existing Soviet Collapse Event Log row, whose event-details cell matches `chaosx.events_log.window.event_details.soviet_collapse`. Super-event research and final presentation disposition live in `docs/super_events/system_camp_repression_rework_super_event_research.md`; implementation status lives in `docs/plans/system_camp_repression_rework_plans/source_of_truth_and_completion_tracker.md` and `completion_report.md`.

The final decision/mission audit passed. All 15 Part 7 and cross-cutting scenario contracts passed static trace with `ScenarioContracts=15 Failed=0`; `docs/plans/system_camp_repression_rework_plans/scenario_contract_validation_report.md` records the evidence. No engine-runtime scenario execution occurred in this environment, so rendered GUI behavior, AI choices, timed outcomes, and numeric runtime deltas remain an explicit validation gap for the parent final gate.

## Maintenance Rules

- Add a new site only through the shared registration helpers and store responsibility first.
- Add recurring population harm only through the shared monthly Deaths processor.
- Extend AI selection through a country-specific ordered selector and the resolved cap variables.
- Keep discovery evidence after control changes unless an explicit reform or tribunal effect changes it.
- Add a visible decision, idea, mission, event, project, or GUI value together with localisation and its stable sprite registration.
- Keep ordinary operation silent; reserve report, news, and super-event presentation for discovery, crisis, reform, tribunal, or terminal country outcomes.

## Further Extensions

Future additions can deepen postwar tribunal negotiations, successor-state archive diplomacy, prisoner rehabilitation, reparations, resistance rescue networks, and multilateral inspection regimes. They should reuse the responsibility, evidence, Deaths, Ledger, and dismantlement contracts rather than create parallel systems.
