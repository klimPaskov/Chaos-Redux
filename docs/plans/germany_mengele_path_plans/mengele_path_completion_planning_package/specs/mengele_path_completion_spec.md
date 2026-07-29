# Mengele path completion spec

## Intended result

Finish the Germany Mengele path as a coherent, tested, documented, and sensitive gameplay chain. Completion means the path works from the first Auschwitz event through the Directorate branch, the Tibet Expedition interactions, the cloning project, the Angel Directorate super-event, and any later clone world-order branch already present in the repository.

The chain must remain tied to the camp and genocide crisis systems. It must model hidden internal damage, evidence, discovery, Deaths integration, foreign response, and consequences.

## Non-negotiables

- Treat the uploaded `germany_mengele.md` as the current implementation map, then verify every named file in the actual repository.
- Treat `genocide_crisis_system.md` as the behavior contract for camps, hidden damage, evidence discovery, state registration, Deaths integration, and delayed foreign condemnation.
- Treat `genocide_mechanics_spec.md` as the older concept source only where it still matches the current implementation note.
- Do not make a standalone random-event implementation unless repository discovery proves one exists.
- Do not call the chain complete while any registered super-event image, audio, localisation, or wiring is a placeholder.
- Do not write player-facing text that glorifies atrocity, frames perpetrators heroically, uses gore for shock, or treats Nazi racial claims as true.
- Do not use generated art for real people or real historical victim scenes.
- Do not add a new broad mechanic if an unresolved improvement addendum already exists. Resolve, queue with reason, reject with reason, or promote it first.

## Completion pass

### 1. Repository verification

Locate and open every current-source file named in `specs/current_implementation_map.md`. Verify the actual repository state before editing. Record missing files, renamed files, stale docs, or moved surfaces in the completion report.

Minimum file families to verify:

- Events and event effects: `events/germany_mengele.txt`, `common/scripted_effects/germany_mengele_effects.txt`, `common/scripted_triggers/germany_mengele_triggers.txt`, and `common/script_constants/germany_mengele_constants.txt`.
- Decisions: `common/decisions/germany_mengele_decisions.txt` and `common/decisions/categories/germany_mengele_categories.txt`.
- Ideas, leader traits, AI, focus tree, special projects, unit names, opinion modifiers, and localisation.
- Super-event GFX, scripted localisation, sound definitions, sound definitions, audio docs, and assets.
- Genocide-crisis integration files and Chaos Meter integration files named by the current map.

### 2. Event chain completeness

Audit every `germany_mengele.*` event for trigger validity, option effects, target validity, immediate effects, delayed event timing, duplicate prevention, fail-safe cleanup, and localisation keys.

The event inventory must include at least:

- `germany_mengele.1` entry event.
- `germany_mengele.10` through `.14` report chain.
- `germany_mengele.17` facility demand.
- `germany_mengele.20` coup monitor.
- `germany_mengele.22` emergency revolt on discovered or captured laboratory territory.
- `germany_mengele.23` cloning proposal.
- `germany_mengele.24` cloning project completion handoff.
- `germany_mengele.37` perfect-Aryan formation overthrow event.
- `germany_mengele.38` delayed loyalist war handoff.
- `germany_mengele.40` Tibet expedition start.
- `germany_mengele.120` and `.121` hidden foreign network offers.
- Any additional events found in the repo under the namespace.

Every event should either be finished, deliberately unreachable with a reason, or removed from the live path. No event may remain as a placeholder node that fires during normal play.

### 3. Genocide crisis integration

The Mengele path must remain a linked layer over the camp system, not a disconnected science route.

Verify these behaviors:

- Auschwitz and all experiment-linked states store or preserve the responsible country.
- Experiment-linked atrocity sites are registered into `global.genocide_active_camp_states` when they should produce monthly effects.
- Hidden experiment deaths use the shared Deaths population-loss pipeline and the correct reason buckets.
- Foreign condemnation does not rise passively only because the original regime still controls a site. It rises through discovery, survivor evidence, exposed records, foreign reaction events, or equivalent concrete evidence.
- Enemy state-control discovery can expose Mengele-linked sites and can trigger the emergency laboratory revolt only when its documented conditions are met.
- Closure, rejection, purge, review, expiration, ideology change, coup loss, or Directorate defeat cleans up obsolete variables, flags, targets, decisions, and missions.

### 4. Decisions and missions

Finish the `germany_final_solution_category` and `germany_tibet_expedition_category` surfaces, plus any clone-network or Directorate decisions found in repo.

Required decision quality:

- Categories appear only when at least one meaningful action exists.
- Reveal and hide decisions do not clutter the UI after they become obsolete.
- Costs use political power only when the action is actually bureaucratic. Military or logistical actions should use fitting costs such as XP, equipment, trains, convoys, stability, war support, supply, facility ownership, or state control.
- AI weights respect ideology, war state, Soviet war, facility count, chaos tier, stability, desperation, target validity, and route locks.
- Tibet Expedition decisions cancel safely when Germany stops being fascist, loses needed access, loses the expedition state, or when the Holy Realm path becomes invalid.
- The hidden clone network decisions should target valid countries only and must not create dead targets, duplicate host markers, or impossible client regimes.

### 5. Focus tree and country package

If `mengele_clone_army_focus_tree` is active in the repo, finish it as a real playable tree for the Directorate.

Required focus-tree quality:

- Opening survival and state consolidation after the civil war.
- Laboratory command and clone program path.
- Conventional expansion path with German-Polish heartland, borderland commands, and continental dominance logic.
- Hidden global replacement network path gated by `MCL_the_numbered_future`, high chaos, network size, network strength, and major-power status.
- Non-linear branch structure, route locks, payoff focuses, varied rewards, focus filters, AI strategy, icons, localisation, and no filler chains.
- Starting units, templates, equipment, manpower, commander assumptions, and reinforcement routes for the Directorate.
- Cosmetic tags, flags, ideas, advisors, and leader portrait references for the Directorate, Angelic Directorate, clone clients, and Aryan variant where relevant.

### 6. Super-event finish

Finish the Angel Directorate super-event first, because the current source says its image exists but contains default art.

The reveal super-event should fire only when the campaign moment deserves major presentation, such as the Directorate coup, emergency laboratory revolt, or consolidation depending on current repository design. It must be one-time, settings-aware, documented, and linked to the right audio ID.

Also verify the later `Angelic World Order` super-event and the `Aryan Supremacy` variant if the world-end path is live. Those must use the same final network machinery and must not conflict with the reveal super-event slot.

### 7. Localisation and docs

Write final in-game prose from the design direction, not from prompt fragments. Avoid staccato drama, generic crisis communications, gore, joke framing, and hidden implementation spoilers.

Update or verify:

- `localisation/english/germany_mengele_l_english.yml`.
- Super-event localisation keys for every live slot.
- Chaos Meter history reason localisation.
- Decision, idea, focus, special project, opinion modifier, achievement, and tooltip keys.
- `docs/events/` or the accepted Germany path doc location.
- Asset and audio manifests.
- Spreadsheet catalog only after final in-game wording is stable.

### 8. Tests before completion

Run meaningful validation rather than broad boilerplate only. At minimum, use the route tests in `matrices/mengele_test_matrix.md` and record evidence in the final report.

A completion claim is valid only after the implementation agent can say which tests passed, which were impossible to run, which repo files were changed, which subagent handoffs were reviewed, and which accepted plans were implemented or resolved.
