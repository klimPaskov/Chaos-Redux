# Coding Prompt: Implement Event 6 Independence Wave

Implement the full Event 6 Independence Wave rework from the spec pack.

Read and follow:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-event-assets`
- `chaos-redux-super-events` when super-events are implemented
- `hoi4-focus-trees` for Event 006 focus trees
- `hoi4-decisions-missions` for Event 006 decisions and timed missions
- `docs/events/006_independence_wave.md` after you create it
- the full spec files in this pack

## Required design behavior

- Event 6 remains Minor Repeatable.
- It belongs to the Liberations cluster as the lowest-threat entry and should usually be the first liberation cluster event.
- It is independent from Event 5. Do not use Event 5 variables, missions, focus routes, republic route logic, collapse progress, event logs, formables, startup ideas, or package flags as a requirement for Event 6.
- Mark every release with Event 6 origin. Shared tags can exist in both systems, but mechanics must follow release origin.
- If Event 6 releases a Soviet republic style tag, it does not become part of the Soviet Collapse system. It uses Event 6 focus, decision, package, GUI, formable, achievement, and event-log logic.
- Volga Bulgaria or Old Great Bulgaria from Event 6 uses the Independence Wave tree and Volga overlay, not Event 5 content. Its Event 6 routes and formables must differ from the Soviet Collapse version.
- Countries do not become independent instantly. The event starts a dossier and decision phase.
- The first successful wave releases 3 to 5 inactive countries, mostly ordinary HOI4 or modded releasables.
- Higher chaos tiers release more countries per successful wave. Use baseline 3 to 5, Evo I 4 to 6, Evo II 5 to 7, Evo III 6 to 9, Evo IV 8 to 12, Evo V 10 to 16, capped by valid candidates and performance.
- Event 6 must never delete an existing host country. Before release, reserve at least one host state, preferably the current capital. Shrink or skip candidates until the host keeps at least one state. This has no exceptions inside Event 6.
- Host countries must be selected from weak, unstable, wartime, overstretched, colonial, occupied, or low-legitimacy countries.
- Hosts must be able to negotiate, suppress, delay, accept, invite observers, arm loyalists, ask for guarantees, evacuate archives, trade territory, and protect the capital, with meaningful costs.
- Decisions must use dynamic costs and active missions. Do not turn the system into a political-power shop.
- Evolutions must unlock non-democratic releases, stronger armies, coalition behavior, mutual guarantees, volunteers, faction formation, territorial demands, patron puppet struggles, wars, historical-return packages, local-polity packages, custom tags, necromancy, anti-mankind doctrine, and strange-state cooperation.
- Candidate ladder must start with ordinary releasables, then dormant or game-rule tags, city and protectorate packages, historical-return and local-polity packages at Evo IV, and strange packages at Evo V.
- Released countries receive the route-level Liberation Provisional Tree or a package-specific Event 6 overlay. Do not replace the focus architecture with a small linear tree.
- Do not implement the focus tree as a numbered focus-by-focus copy of the spec. Build the final focus count, layout, prerequisites, bypasses, rewards, and AI weights from the route architecture.
- Focuses must include AI behavior that reacts to route, ideology, war, stability, patron leverage, recognition, faction membership, and chaos tier.
- Every package that uses real symbols, leaders, dynasties, flags, or cultural references needs source review.
- Assets must be processed, placed, documented, and handed off. Do not leave loose generated images or untracked downloads.
- Super-events fire only for major evolved moments, not for the base minor event.
- Achievements must check origin, disqualify debug routes, and test meaningful gameplay.

## Implementation phases

### Phase 1: Foundation

Create shared constants, scripted triggers, scripted effects, and variables for:

- release origin
- candidate scoring
- host scoring
- protected host state
- host survival floor
- release count target
- actual release count
- package type
- pressure
- legitimacy
- radicalization
- militia strength
- foreign attention
- patron leverage
- coalition cohesion
- claim ambition
- old-state memory
- local-polity cohesion
- occult pressure

### Phase 2: Dossier and host crisis

Implement dossier creation before any release.

Required host decision groups:

- open negotiations
- offer local autonomy
- suppress committee offices
- deploy garrisons
- invite observers
- arm loyalists
- request guarantees
- evacuate archives
- trade territory
- reserve capital administration
- delay the crisis
- accept controlled release

Timed missions should include:

- hold capital ministry
- guard depot belt
- secure border posts
- maintain rail access
- prevent capital isolation
- keep legitimacy above threshold

### Phase 3: Candidate resolver

Build a batch resolver that:

1. scores hosts
2. selects candidates by chaos tier and package ladder
3. marks protected host state
4. checks combined state removal across all candidates
5. reduces candidate territory where possible
6. skips candidates that would take the protected state or delete the host
7. recalculates actual release count
8. applies Event 6 origin
9. creates armies, ideas, decisions, and tree access
10. records event log and evolution context

Avoid daily or weekly world polling. Run resolver logic at event start, decision resolution, candidate timeout, and wave completion.

### Phase 4: Country setup

For each released country:

- assign origin flag
- assign package type
- assign government and ideology from tier logic
- create dynamic starting army
- grant equipment and units based on variables
- add provisional ideas
- load Event 6 tree or overlay
- unlock starting decisions
- register host and wave index
- record event details
- apply AI strategy

### Phase 5: Focus tree and decisions

Implement the route-level Liberation Provisional Tree with:

- opening trunk
- civic legitimacy
- military survival
- revolutionary committee
- national directorate
- patron cabinet
- anti-patron struggle
- coalition congress
- border commission
- crisis branch
- historical-return overlay
- local-polity overlay
- railway and free-city overlays
- strange modules
- late-game ambition routes

Focuses should unlock decisions, missions, leaders, ideas, claims, cores, guarantees, faction actions, border commissions, and route-specific events. Flat modifiers are supporting rewards only.

### Phase 6: Packages

Implement a minimum viable package set before adding rare packages.

Minimum ordinary set:

- ordinary releasables from valid cores
- dormant or game-rule tags where safe
- free city or free port
- border protectorate
- railway sovereignty

Minimum high-chaos historical or local set:

- Assyria
- Mesopotamia
- Mapuche Araucania
- Guarani or Charrua
- Aymara
- Palmares
- Buganda
- Asante
- Sokoto
- Kanem-Bornu
- Barotseland
- Volga Bulgaria
- Circassia or Mountain Republic
- Bukhara, Khiva, or Kokand

Add more only when state mapping, assets, and origin gating are safe.

### Phase 7: Assets

Create or source all report images, icons, ideas, flags, portraits, focus icons, achievement icons, and super-event images required by the final implemented package set.

For real symbols or leaders, use sourced material. For fictional or strange assets, generated art is acceptable. Record source mode and uncertainty in the asset manifest.

### Phase 8: Super-events and achievements

Implement super-events only after their trigger moments exist.

Required candidate super-events:

- First League of New States
- Great Partition Week
- First Old Name Returns
- First Impossible State
- League War
- Human Renunciation
- The Rump That Endures

Implement achievements with strict origin checks, route checks, and debug disqualifiers.

### Phase 9: Documentation and validation

Update:

- event docs
- event log entries
- event details
- localisation
- asset manifest
- achievement docs
- super-event docs
- catalog spreadsheet
- focus-tree route docs
- decision docs

Final report must list changed files, implemented routes, implemented packages, assets, super-events, achievements, remaining blockers, and validation performed.

Do not claim completion until all required files, assets, docs, and catalog updates match the implemented state.

## Subagent and audit routing for implementation

Use project subagents where the implementation becomes broad.

| Need | Suggested route | Parent responsibility |
| --- | --- | --- |
| file location and existing pattern search | repo exploration helper | review findings and make final edits |
| reusable scripted effects or triggers | scripted system architect | keep constants centralized and avoid duplicate logic |
| focus tree quality | focus tree auditor | fix route gaps, icon gaps, AI gaps, and count mismatches |
| decision and mission quality | decision mission auditor | fix passive buttons, flat costs, stale missions, and cleanup gaps |
| country packages | country package auditor | fix missing tags, histories, flags, leaders, parties, and state mappings |
| localisation | localisation auditor | fix missing keys, duplicate keys, and text mismatch |
| assets | source researcher, generated event art worker, icon artist | final sprite wiring and docs alignment |
| super-event quote and audio | super-event text and audio researchers | verify source confidence and final trigger alignment |
| completion | event completion auditor | do not claim complete until blockers are resolved |

Subagent output is not completion. The main implementation pass must review, wire, validate, and report the final state.

## Improvement loop

After a first working pass, inspect the feature for shallow areas.

Check:

- whether early waves feel too similar
- whether host choices have real costs
- whether decisions are active missions or passive buttons
- whether released countries have playable problems
- whether high-chaos packages have distinct identity
- whether focus routes interact with decisions and AI
- whether assets communicate route and package differences
- whether super-events have complete quote, audio, image, docs, and trigger packages
- whether achievements require mastery instead of passive waiting
- whether Event 5 separation and host survival rules remain intact after every new feature
- whether Soviet republic style tags released by Event 6 remain outside the Soviet Collapse system
- whether Volga Bulgaria and Old Great Bulgaria use different Event 6 routes from their Event 5 versions

When a gap is found, write a concrete addendum and implement it before final completion. Do not mark the event complete with known shallow route families, missing asset documentation, missing dynamic costs, or missing origin checks.

## Updated spec and plan paths

Read the source specs from:

```text
docs/specs/006_independence_wave_specs/
```

Use working plans, subagent handoffs, improvement addenda, and audit follow-up notes from:

```text
docs/plans/006_independence_wave_plans/
```

If an accepted plan changes the source design, fold it into the matching source spec or report that it remains queued with a reason.

## Subagent deployment requirements

All project custom Codex subagents must be spawned with `fork_context=false`.

The parent prompt must pass every needed path, user correction, accepted plan, queued plan, rejected plan, task scope, and validation requirement explicitly. Do not rely on inherited conversation state.

Use active small-patch subagents during implementation:

- `chaosx_decision_mission_auditor` for decision costs, tooltips, GUI button text, cleanup, AI checks, and existing formable requirements
- `chaosx_focus_tree_auditor` for route locks, prerequisite fixes, focus AI, icon references, small reward variety, and existing formation hooks
- `chaosx_country_package_auditor` for package setup, tag references, party names, focus loading, starting setup, and existing formable checks
- `chaosx_localisation_auditor` for missing keys, dynamic localisation, cost text, scripted localisation, and cross-surface wording
- `chaosx_scripted_system_architect` for narrow helper logic, script constants, formation helpers, GUI button helpers, cleanup helpers, and direct call sites

Every subagent patch must write a handoff under:

```text
docs/plans/006_independence_wave_plans/subagent_handoffs/
```

The main agent must review every handoff before claiming completion.

Use `chaosx_improvement_loop_planner` after meaningful implementation tranches. Do not spawn it again until the previous addendum is implemented, folded into specs, queued with a reason, or rejected. If the planner says new mechanics would bloat the system, treat its closure handoff as the signal to finish validation and completion reporting rather than adding more design.

## Formables, scripted GUI, and animations

Implement the formation layer from the spec:

- focuses prepare or reveal formables
- decisions verify state control and perform formation
- post-formation missions handle integration
- hidden formables have reveal logic, AI rules, disqualifiers, assets, and cleanup
- formation identity reads Event 006 release origin and formation origin
- formation never violates host survival during initial wave resolution

Implement mechanic windows only where useful:

- Independence Dossier Board
- New States Congress
- Patron Ledger
- Formation Ledger

Every button must have costs, missing-requirement tooltip, scripted trigger, scripted effect, AI equivalent, cleanup, localisation, and validation.

Use `chaos-redux-frame-animation` for animated sprites and portraits. Every animation must have source frames, processed frames, sheet PNG, sheet DDS, static fallback, GIF preview for review only, manifest, and gfx handoff. Do not wire GIFs as final assets.
