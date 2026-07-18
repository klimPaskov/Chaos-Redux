# Coding Prompt for Chaos Redux Event 19 Infantry Spawn

Implement the complete Event ID `19`, Infantry Spawn, from `docs/specs/019_infantry_spawn_specs/`. Preserve the stable event identity. Treat the request prefix `017` as request metadata, not the event ID.

## Required reading

Before editing, read `AGENTS.md`, every relevant repo skill, all Event 19 spec parts, matrices, prompts, review notes, the current local Event 19 implementation, all current references to ID 19, the offline Paradox wiki pages required by AGENTS.md, vanilla documentation, and relevant vanilla or existing Chaos Redux precedents.

The public repository snapshot used during planning is not the implementation source of truth. Use the local current repository.

## Required implementation

Implement the full cross-surface event contract.

### Core and baseline

- Keep Event 19 Minor Repeatable and globally applied.
- Replace flat one-template-per-state behavior with the diminishing state-coverage model.
- Larger countries still receive more total formations.
- Build weighted state selection and formation lots.
- Implement visible Muster Control and Army Congestion.
- Implement audit, integration, territorial roles, standardization, emergency use, and controlled demobilization.
- Account for manpower, equipment, supply, officer, and rail burdens.
- Prevent disband, template-switch, salvage, and reroll exploits.
- Implement real-effect incidents and AI equivalents.

### Evolutions

Implement four true evolution stages with both active-event and pre-fire paths.

1. Organized Muster with stronger templates, better readiness, support companies, staff, and districts.
2. Arsenal Lottery with multiple units per selected state, serious armor and mechanized families, valid strange units, finite technology-locked equipment, and on-demand requests.
3. Command Fracture with no ordinary automatic spawn by default, fully random safe battalion and support composition, quality and coherence axes, claimant generals, demands, influence, takeover, and revolt.
4. Anomalous Muster with a documented opt-in Chaos unit family registry, train-versus-spawn rules, saturation, containment, and derivative revolt states.

Use the shared evolution logger correctly and respect disabled evolutions. Ordinary generation lifecycle stages are not evolutions.

### Random divisions

Build a verified pool from all valid installed vanilla combat battalions and support companies plus explicitly registered mod additions. Preserve at least one combat battalion, valid support slots, and engine-safe limits. The design target is one to 25 combat battalions and zero to five support companies, subject to local verification.

Do not unlock technology merely because equipment appears. Technology-locked formations receive finite initial equipment and restricted reinforcement.

### Claimants

Create a reusable system for up to three active claimants per country and a 20-profile male claimant pool. Use regional male personal-name pools and male-default leader metadata. Each fixed technical portrait slot displays a separate region-compatible army/muster identity scene with no individual focal human/person. Claimant revolts transfer only recorded loyal event formations and coherent territory. Implement one-state takeover logic.

### Chaos unit registry

Create or extend a reusable documented registry with the fields in the specification. Future unit families opt in once through the registry. They remain excluded by default.

Initial requirements:

- base zombie is trainable and spawnable only through Event 19’s bounded rules
- advanced zombie variants are excluded
- ghosts are spawn-only
- golems are spawn-only unless verified source design says otherwise
- derivative states never set or satisfy parent Zombie, Death, golem, super-event, evolution, or world-end progression

Verify actual local unit and parent-system identifiers before writing call sites.

Keep all Event 19-specific registry tables and provider callbacks in the sole
consolidated Event 19 registry code file. Fold registry constants and triggers
into the existing Event 19 constants and trigger files, and keep startup calls
in existing parent on-actions. Do not create family-specific or additional
Event 19 registry files.

### Derivative countries

Implement complete zombie, ghost, and golem derivative packages through a safe dynamic-country model or stop and request approval for a fixed-tag fallback.

Each package needs:

- distinct origin and identity
- direct public names and flags
- leader or council
- starting politics and ideas with lifecycles
- actual revolting units as starting forces
- reinforcement and sustainment
- roughly 25 to 35 focus-scale route content or an equivalent fully adapted shared tree
- decisions and missions
- route-specific AI
- regional expansion and postwar integration
- defeat cleanup
- shared special and nonhuman classification

Ghost population and wasteland effects are slow and use the shared death pipeline. Derivatives are weaker than parent-event countries and have no world-end route.

### Decisions, GUI, and assets

Implement the phased category, selected-lot Muster Board, claimant tab, and Evolution IV registry tab. GUI buttons call shared decision logic and AI has an equivalent path.

Wire every final visible asset from the Event 19 asset package. Wire the three frame-sheet animations with static fallbacks. Do not leave placeholders.

### Triggerable scenario

Register The Unbidden Muster with the final approved identity `SCN-013`.

Implement four type directions and four intensity stops. Launch is direct and independent of normal chaos, evolution, date, or prior event prerequisites. Create immediate revolt or takeover and wars. Clear every launch bypass after setup. Do not set the terminal world-end flag.

### Cross-event safety

Audit and implement bridges or exclusions for Zombie Outbreak, Death, the actual golem system, Generalissimo, Division Lock, Warlords, Widespread Mutiny, civil-war handling, Chaos Meter, Deaths, Event Log, event enable state, and future cluster compatibility.

Avoid duplicate chaos, deaths, war effects, unit transfers, and parent progression.

### AI and balance

Implement national policy profiles, lot evaluation, claimant behavior, derivative behavior, request safety, and route validity. Centralize all tuning. Run the task-specific scenarios in the specification and inspect opening values, scaling, costs, mission outcomes, revolt strength, derivative growth, and exploit paths.

### Text, docs, and spreadsheet

Write final player-facing localisation from the direction in the spec. Working labels are not final copy. Keep Event Details free of mechanical effect lists and hidden spoilers.

Update Event Log names and selectors, evolution catalog, Event Details, scenario text, country and leader text, focus and decision text, achievements, helper docs, classifier docs, one canonical Event 19 doc, asset manifests, and the event catalog workbook through the spreadsheet worker.

## Subagents and review

Use project custom subagents with `fork_context=false` and explicit bounded prompts.

At minimum, use the scripted-system architect, decision auditor, country auditor, focus auditor, localisation auditor, asset workers, spreadsheet worker, mandatory improvement-loop planner, documentation curator when needed, and final event completion auditor.

Resolve each handoff. Do not leave an accepted addendum without implementation, promotion, queued reason, or rejection reason.

## Completion rule

Do not claim completion while any evolution, decision family, derivative package, AI path, asset, achievement, scenario control, Event Log surface, documentation field, or spreadsheet mirror is missing. Report every simplification and fallback. Fallbacks require user approval.
