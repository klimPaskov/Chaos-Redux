# Event 016 host-archetype flavour tranche handoff

## Scope

This tranche adds country-shaped presentation to the existing Event 016 host-context reports without adding a root fire, a cluster, a fifth evolution, a project reward, a new Directorate meter, or a 3D asset reference. It remains compatible with the minor fire-once incident contract.

## Runtime changes

- `common/script_constants/016_brilliant_scientist_host_flavor_constants.txt` centralizes the classification gates and small AI preference factors.
- `common/scripted_effects/016_brilliant_scientist_host_flavor_effects.txt` defines `brilliant_scientist_assign_host_flavor`. It clears all seven archetype flags and assigns exactly one using current country facts in priority order: exile host, subject empire, university system, industrial power, militarized state, threatened small state, then default.
- `common/scripted_effects/016_brilliant_scientist_effects.txt` calls the assignment from `brilliant_scientist_initialize_host_state`, which covers both first appointment and ordinary transfer recipients.
- `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt` defines `GetBrilliantScientistHostFlavorClause` with a safe default branch.
- `events/016_brilliant_scientist_directorate_outcomes.txt`, `events/016_brilliant_scientist_context_events.txt`, and `events/016_brilliant_scientist_host_reaction_events.txt` add modest archetype-aware AI weights to the already available options while preserving all existing ideology, security, exposure, war, and causal modifiers.
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` appends the dynamic clause to `.4`, `.5`, `.6`, `.7`, `.8`, and `.9` descriptions and provides seven player-facing clauses.

## Validation evidence

The new constants, effect, scripted localisation, and modified event files have balanced Clausewitz blocks. The localisation file remains UTF-8 with BOM, and all new scripted-localisation and localisation keys are unique within the Event 016 surfaces. Focused event inspection should cover `chaosx.nr16.4`, `.5`, `.7`, `.8`, and `.9`; live host classification and AI choice behavior remain user-owned because the agent must not launch the game.

## Remaining risks

The thresholds are intentionally conservative and static until quantitative balance evidence is collected. A country can only display one archetype, so a large subject empire is presented as colonial before its industrial or university capacity is shown. Broader bespoke country chains, project/news/remnant art, live transfer scenarios, and the seven Event 016 3D unit packages remain deferred by the parent acceptance boundary.
