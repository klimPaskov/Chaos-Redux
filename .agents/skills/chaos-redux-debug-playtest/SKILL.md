---
name: chaos-redux-debug-playtest
description: Explicit-invocation-only Chaos Redux live QA workflow. Use only when the user names this skill or explicitly authorizes autonomous desktop control to launch the supplied debug shortcut, repair fresh Chaos Redux errors, relaunch until clean, play bounded test cases, exercise events and project UI, capture screenshots, fix confirmed defects, and verify the fixes in game. Never use as part of the normal Chaos Redux workflow unless explicitly invoked.
---

# Chaos Redux Autonomous Debug Playtest

Use this skill only after the user explicitly invokes it or explicitly asks Codex to control the computer and perform autonomous Chaos Redux live testing.

Do not add this skill to `AGENTS.md`, `chaos-redux-subagents`, completion-audit routing, event implementation routing, or any default workflow unless the user separately requests that integration. Normal coding agents must not use this skill merely because a feature needs validation.

## 1. Capability gate

This skill does not itself grant Windows desktop control.

Before starting, verify that the active Codex environment can:

- see and control the Windows desktop
- capture and save screenshots
- launch the supplied shortcut
- inspect and stop only the launched HOI4 process
- read the active Hearts of Iron IV log directory
- edit the Chaos Redux repository

If any required capability is unavailable, stop with a blocked report. Do not claim that the skill has controlled the user's computer when it has not.

## 2. Default Chaos Redux configuration

Use these defaults:

```text
logs:
C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\logs

launch_target:
C:\Users\klimp\OneDrive\Desktop\hoi4.exe - Shortcut.lnk

artifact_root:
<mod_root>\docs\testing\live_qa\<run_id>
```

The supplied shortcut is declared by the user to launch HOI4 in debug mode. Preserve and launch that shortcut directly. Do not replace it, rewrite it, or route through the Paradox launcher unless the user requests that change.

Confirm the active log directory by freshness after launch. Do not assume the OneDrive candidate is active merely because the mod is stored in OneDrive.

## 3. Invocation scope

Every invocation must resolve one of these modes:

- `changed-surface`: test files and systems touched by the current task or Git diff
- `named-feature`: test one named event, mechanic, country, focus tree, decision system, scripted GUI, super-event, scenario, or cluster
- `issue-reproduction`: reproduce and fix a reported live defect
- `catalog-coverage`: test all currently implemented and testable catalog entries in bounded checkpoints
- `regression-suite`: rerun a named set of previously passing cases

Do not silently expand `changed-surface` into a full-mod pass. Do not interpret `test everything` as permission to redesign unfinished catalog ideas.

For catalog coverage:

- prioritize rows marked `Needs Testing`
- include rows marked `Implemented` as regression targets
- do not claim rows marked `To Be Reworked`, `New`, blank, reserved, unregistered, or unimplemented are tested unless the user explicitly requests prototype testing and the implementation exists
- reconcile catalog status with actual event registration and repository files
- record discrepancies between catalog status and implementation rather than guessing which is authoritative

## 4. Mandatory project reading before a run

At the start of each invocation, read:

- `AGENTS.md`
- `.agents/skills/hoi4-autonomous-debug-playtest/SKILL.md`, or the packaged generic copy
- this skill
- the task brief, accepted spec, plan, handoff, issue report, and implementation files for the test scope
- the relevant system skills for every surface that may be patched

Common required skills by surface:

- event chains, event logs, evolutions, details, clusters, and scenarios: `chaos-redux-events`
- decisions, missions, costs, and decision GUI actions: `chaos-redux-decisions-missions`
- focus trees and route loading: `chaos-redux-focus-trees`
- visual assets, sprites, flags, portraits, and DDS wiring: `chaos-redux-event-assets`
- animated sprites and portrait overlays: `chaos-redux-frame-animation`
- super-event text, image, audio, slot, and playback: `chaos-redux-super-events`
- localisation and dynamic text: use the project localisation rules and, when useful, `chaosx_localisation_auditor`
- reusable scripted logic: use `chaosx_scripted_system_architect` when a narrow helper is genuinely needed

Consult the required offline Paradox wiki pages and vanilla documentation before patching engine-facing syntax. Live observation does not replace required implementation references.

Do not reread the entire repository for a narrow known-feature run. Read the complete source-of-truth files for the scoped feature and use targeted search for dependencies.

## 5. Repository boundary

The only default editable repository is:

```text
C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux
```

Never edit:

- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`
- Workshop reference mods
- another local mod
- Paradox launcher files
- the user's normal saves
- unrelated personal OneDrive files

Vanilla, documentation, offline wiki, and approved reference mods are read-only references.

Preserve unrelated uncommitted changes. Do not reset or clean the repository. Before editing a file with pre-existing changes, inspect the exact diff and retain the user's work.

## 6. Launch and clean-start gate

Use this startup sequence:

1. Record the current repository commit, branch, changed files, and test scope.
2. Record hashes and timestamps for `error.log`, `game.log`, `setup.log`, `text.og` and `exceptions.log` when present.
3. Launch:

```powershell
Start-Process -FilePath 'C:\Users\klimp\OneDrive\Desktop\hoi4.exe - Shortcut.lnk'
```

4. Identify the new HOI4 process and retain its PID.
5. Wait for the main menu to become visually stable.
6. Capture a main-menu screenshot showing the visible game version and evidence that Chaos Redux loaded.
7. Copy the fresh logs into the run artifact folder.
8. Triage only the current-run delta.
9. If a target-mod blocking error exists, close HOI4 and enter the repair loop before starting a campaign.
10. If no target-mod blocking error exists, start or load the dedicated test game.
11. Use save files as well for debugging, they can sometimes be useful.

The clean-start gate passes when the current launch reaches the main menu and a country map without a new attributable blocking error. It does not require every harmless engine warning to disappear.

## 7. Chaos Redux error triage

Treat an error as attributable when the fresh line identifies or strongly implies a Chaos Redux path or identifier, including:

- `chaosx` namespaces, keys, effects, triggers, variables, flags, sprites, GUI entries, events, decisions, ideas, focuses, or localisation
- event-owned files and folders using an event ID and slug
- Chaos Redux interface, GFX, music, sound, scripted GUI, on-action, achievement, country, history, or asset paths
- a file changed by the current task

Classify findings as:

- startup blocker
- crash or exception
- script parse or malformed token
- invalid effect, trigger, scope, variable, event target, or constant use
- duplicate ID or duplicate key
- missing localisation or scripted localisation
- missing texture, sprite, sound, music, portrait, flag, or GUI entry
- invalid event, decision, focus, idea, country, state, or character reference
- runtime spam or repeated cleanup failure
- warning with demonstrated gameplay impact
- warning without demonstrated impact
- uncertain attribution

Do not make broad speculative fixes from a generic warning. Find a reproducible connection to Chaos Redux first.

When an error appears after the agent's patch, treat it as caused by the current change set until the agent proves otherwise from the pre-patch log evidence.

## 8. Repair loop

For each attributable error:

1. Save the full fresh line, repeated count, file path, line number when present, and screenshot state.
2. Close HOI4 through the in-game exit flow.
3. If the game is frozen, capture the screen and relevant logs, then stop only the recorded HOI4 PID.
4. Read the owning skill and the relevant source-of-truth spec or documentation.
5. Search the repository for the exact identifier and its call sites.
6. Inspect a Chaos Redux precedent and a vanilla precedent when engine behavior is involved.
7. Patch the smallest complete surface.
8. Keep localisation, GUI, GFX, docs, and catalog wording aligned when the behavioral fix changes those surfaces.
9. Do not add a placeholder asset, default audio, fake localisation, generic focus branch, or other fallback.
10. Run targeted checks for the exact failure.
11. Relaunch through the same shortcut.
12. Verify the original fresh error no longer appears.
13. Verify no new attributable error was introduced.
14. Repeat until clean or a hard stop is reached.

Default maximum repair cycles are `6`. The user may set a different limit. The loop should normally continue without requesting confirmation between cycles. Stop only for a hard blocker, ambiguous design decision, unsafe scope expansion, or exhausted cycle budget.

## 9. Test-country rule

Use one primary player country for a run unless the user explicitly authorizes multi-country coverage.

Selection order:

1. user-specified country
2. country that owns the named feature or event route
3. a stable major country that can access Chaos Redux settings and survive long enough for testing

For a broad single-country pass, the default harness country is the United States in a fresh 1936 non-Ironman game. Record that choice. This is a test harness choice, not a claim that every country-specific branch is covered.

Stay on the primary country. Prefer Chaos Redux settings, force-trigger controls, triggerable scenarios, decisions, and normal gameplay setup over tag switching.

When a country-specific route cannot be reached from the primary country, mark it `not covered in single-country mode`. Do not silently switch countries and still claim one-country testing.

When the user explicitly requests multi-country coverage, use separate dedicated saves by country or feature. Do not perform uncontrolled tag switching inside one polluted save.

## 10. Deterministic setup policy

Use the least invasive setup that preserves the behavior being tested:

1. normal gameplay path
2. Chaos Redux settings and manual trigger UI
3. triggerable scenario UI
4. event or feature-specific debug control already provided by the mod
5. recorded console setup only when the preceding methods cannot create the state efficiently

The settings UI's Force Trigger Mode may bypass ordinary event selection restrictions for a manual test. Do not use it when the test is specifically about normal eligibility, chaos thresholds, timing, enable and disable state, weight, or random selection.

Record every forced trigger, slider value, scenario type, console command, focus autocomplete use, instant construction use, AI toggle, date change, variable change, and tag switch.

Never use a setup shortcut to prove the shortcut's bypassed condition works.

## 11. Dedicated test artifacts

Create:

```text
<mod_root>\docs\testing\live_qa\<run_id>\
  run_manifest.md
  test_report.md
  repair_ledger.md
  coverage.csv
  setup_commands.md
  logs\
  screenshots\
```

Recommended screenshot names:

```text
001_main_menu_pass.png
010_settings_open_pass.png
020_event_006_popup_pass.png
021_event_006_issue_before.png
022_event_006_issue_after.png
030_events_log_history_pass.png
```

Do not put ordinary save files in Git by default. Record the dedicated save name and save path in `run_manifest.md`.

## 12. Chaos Redux smoke test

Every live run that enters a campaign should perform this smoke pass unless the named issue crashes earlier:

- open Chaos Redux settings
- confirm the settings window can be closed and reopened
- open the Event Logs window
- visit Status, History, Evolutions, Events, and Clusters tabs
- click at least one event row and close its detail window
- open the Chaos Meter window
- verify its visible tabs and current values render without raw keys or overlap
- open Triggerable Scenarios when present
- confirm list selection, type control, intensity slider, detail text, confirmation flow, and cancel flow are usable
- save the dedicated game
- reload the dedicated game
- reopen one Chaos Redux window after reload
- advance a bounded period of game time while watching for popup or log spam
- inspect the fresh `error.log` delta

If the scope is narrower and one of these actions would materially alter the feature under test, record the skipped smoke step and reason.

## 13. Event-catalog coverage

Build the live event queue from the current repository catalog and actual implementation, not from memory.

Use the current event catalog workbook or its CSV export. Prefer a CSV export for read-only coverage planning when one exists. Do not edit the workbook during a testing-only run.

For every candidate row record:

- event ID
- event name
- catalog status
- event type
- cluster ID and severity when present
- implemented entry event or namespace
- normal eligibility test required or not
- manual trigger path
- primary actor and whether it can be tested from the primary country
- baseline event test
- evolution tests
- world-end test when implemented and in scope
- event-log and event-detail checks
- decisions, focuses, countries, GUI, assets, super-events, and AI surfaces
- dedicated save or checkpoint
- result
- screenshot paths
- fresh log result
- fixes and retest result
- blocker or not-covered reason

### Status handling

- `Needs Testing`: highest priority for live coverage
- `Implemented`: regression coverage after `Needs Testing`
- `To Be Reworked`: do not treat as a completed feature or completion target
- `New`, blank, or no ID: planning backlog, not a live completion target unless a real implementation is explicitly named
- `Reserved`: not a live implementation target

If a catalog row says `Implemented` but no runnable implementation can be found, record a catalog or documentation defect. Do not invent an event ID or mark it passed.

If implementation exists but the catalog is stale, test the implementation and report the mismatch. Update the catalog only when the parent task includes documentation alignment and implementation facts are verified.

## 14. Event test protocol

For each event in scope:

1. Start from a clean checkpoint.
2. Confirm the event's enable or disable state in the Events tab when applicable.
3. Test normal eligibility separately when eligibility is in scope.
4. Trigger the entry event through the intended manual test surface or natural path.
5. Capture the popup or first visible state.
6. Check title, description, options, image, actor, flag, sound, and localisation.
7. Select each important option in separate checkpoints.
8. Verify immediate effects occur once.
9. Verify follow-up events, decisions, ideas, variables, targets, countries, units, and map changes.
10. Check History and Event Details.
11. Advance time to observe scheduled behavior, MTTH behavior, cleanup, and AI response.
12. Save and reload when the feature persists.
13. Inspect the fresh log delta.
14. Capture a pass screenshot or issue screenshot.

Do not log normal baseline stages as evolution passes. Test actual evolution tracks against their own unlock and log contract.

## 15. Evolution test protocol

For each implemented evolution in scope:

- verify the evolution is enabled when expected and safely skipped when disabled
- set up the true prerequisite state without bypassing the behavior under test
- verify pacing or MTTH rather than assuming an instantaneous transition
- verify shared evolution context and actor display through visible Event Logs behavior
- verify the evolution row in the main Evolutions tab
- verify the selected event's History details related-evolution view
- verify Event Details evolution catalog text does not show fake history metadata
- verify stage, tier, actor, event name, date, and ordering render correctly where applicable
- verify gated decisions, focuses, countries, AI, assets, and follow-ups become available
- verify disabled evolutions do not set recorded flags or unlock content
- verify save and reload persistence

Use separate checkpoints for parallel or mutually exclusive evolution tracks.

## 16. Cluster test protocol

Use the current cluster catalog and actual registry.

For each implemented cluster in scope:

- verify the cluster appears in the Clusters tab
- verify members, roles, minimum tiers, participation chance, and danger labels display
- test automatic firing when a member event is selected and cluster conditions are met
- test manual force fire separately
- verify optional members show fired or skipped reasons
- verify the cluster counts as one global pacing event
- verify member events still apply their own effects, history, and repeatable or fire-once state
- verify cluster history records actor, tier, fired count, skipped count, and member reasons
- verify disabled and cooldown state
- verify a cluster detail row can open member event details without breaking the cluster window
- inspect logs for repeated array, index, or invalid-member errors

Do not treat unimplemented catalog-only cluster ideas as live coverage.

## 17. Triggerable scenario test protocol

Use the current scenario catalog and registry.

For each implemented scenario in scope:

- verify stable ID and sort order in the dynamic list
- select the row and verify details update
- test the type control when the scenario has types
- test Low, Medium, High, and Maximum intensity when they produce distinct setup
- confirm the slider knob, stored value, impact text, and launch effect agree
- verify cancel leaves the game unchanged
- verify confirmation reads the values selected at launch time
- verify launch eligibility matches button state
- verify normal chaos, date, evolution, route, and history prerequisites do not incorrectly block the manual scenario
- verify tightly scoped bypass flags are cleared after setup
- verify the resulting countries, units, wars, flags, ideas, and super-events match the scenario
- verify the same setup does not duplicate when launched once
- inspect History, Evolutions, Events, Clusters, and Chaos Meter where the scenario should update them
- save and reload the scenario state

A scenario marked `Needs Testing` remains unverified until its full launch flow and at least one intensity path pass live testing. Test all intensity paths when the user requests complete scenario coverage.

## 18. Event Logs and Event Details visual audit

Check every scoped surface at the active resolution:

- Status tab counters and values
- History rows and detail windows
- Evolutions rows and related-evolution details
- Events list filters, sorting, live weight, fired count, type, and enable toggle
- Clusters list, details, member rows, and member-event navigation
- Event Details premise text
- actor flags and names
- row indexes and dates on history surfaces
- scroll limits and selection state
- multiple detail windows when supported

Confirm:

- no raw keys
- no unwanted decimal places on integer values
- no clipped, overlapping, or misaligned rows
- no stale selected row after a list rebuild
- no fake history date or sequence in catalog-only views
- impossible events show `N/A` rather than a misleading zero weight
- unreworked events remain disabled by default when that is the current project contract

## 19. Chaos Meter visual and gameplay audit

When the scoped feature touches global systems, inspect:

- Status
- History
- Air Cleanliness
- Condemnation
- Deaths

Verify visible values, filters, logs, enable controls, threshold text, actor lists, and updates after the tested action.

When the feature changes chaos, contamination, condemnation, or deaths:

- capture the value before the action
- perform the action once
- capture the value after the action
- verify the corresponding history or death log entry
- verify no duplicate application
- save and reload
- verify the value persists

Do not use a display-only change as proof that the underlying mechanic changed correctly.

## 20. Decisions, missions, and scripted GUI

For every scoped decision or scripted GUI surface:

- open and close the category or window repeatedly
- verify normal, hover, selected, active, locked, disabled, warning, and completed states when present
- verify every button's cost, requirement, result, blocked text, and tooltip
- click each meaningful action from a clean checkpoint
- verify the button cannot be exploited through repeated clicks or stale targets
- verify AI-equivalent behavior for AI-usable systems
- verify cleanup after target death, annexation, war end, route change, and system completion
- verify dynamic text updates when variables change
- verify decorative overlays do not block input
- verify leader portrait overlays appear only in the intended context and country
- inspect error logs immediately after opening and clicking scripted GUI elements

If a scripted GUI is visually broken but its accepted layout is unclear, capture it and mark `needs_user_review`. Do not redesign the interface from taste alone.

## 21. Focus-tree live audit

For every scoped tree:

- confirm it loads only for the intended country and origin
- inspect the full layout for crossing lines, duplicate coordinates, disconnected branches, accidental dead ends, missing icons, and hidden branches leaking into ordinary play
- test prerequisite OR and AND behavior
- test mutual exclusions, bypasses, route locks, and focus filters
- complete representative early, middle, and capstone focuses
- verify decisions, missions, ideas, units, leaders, advisors, flags, cosmetic names, claims, cores, war goals, and events they unlock
- verify national-spirit lifecycle and that routes do not exceed the accepted simultaneous-spirit limit
- observe AI route selection when AI behavior is in scope
- check that completed branches produce playable follow-up content rather than passive dead ends

A tree that renders without errors can still fail live QA. Record shallow or disconnected design as a design gap. Do not autonomously add a new route family under this testing skill.

## 22. Country-package live audit

For event-created, restored, released, or transformed countries in scope, verify:

- tag registration and map color
- normal, medium, and small flags
- ideology or cosmetic variants
- public name, adjective, parties, and leader names
- leader portrait, gender metadata, and name-pool coherence
- capital, ownership, controller, cores, claims, and fallback territory
- starting ideas and their visible effects
- starting divisions, templates, manpower, equipment, commanders, technology, production, convoys, trains, fuel, and supply
- focus-tree assignment and origin gating
- decisions and AI
- annexation, defeat, release, civil-war, and cleanup behavior

A fighting country that appears without a usable force package is a blocking gameplay defect unless the accepted spec explicitly makes it nonmilitary.

## 23. Super-event live audit

For every scoped super-event:

- verify the trigger threshold and role
- verify the intended slot is used
- verify image, title, description, button, quote, and audio match the same super-event
- verify no unrelated slot content is reused accidentally
- verify settings-aware playback
- verify the audio is audible at an appropriate level and stops or transitions correctly
- verify the image is not missing, stretched, or replaced by another slot
- verify the quote and button text fit the UI and do not clip
- verify world-end and defeat aftermath gates when applicable
- inspect fresh logs for missing sprite, sound, music, or localisation references

Do not substitute default audio, placeholder art, invented quotes, or an unrelated track to make the test pass.

## 24. Asset and animation live audit

Inspect visible scoped assets at their actual in-game size:

- event, report, and news images
- focus, idea, national spirit, decision, category, achievement, tech, and officer-corps icons
- flags
- real and fictional leader portraits
- super-event images
- scripted GUI panels and states
- animated sprites, portrait overlays, and static fallbacks

Check for:

- pink or missing textures
- wrong path or wrong sprite
- wrong dimensions or aspect ratio
- opaque square backgrounds where transparency is required
- white halos or checkerboard remnants
- unreadable small icons
- upside-down flags
- identical ideology variants when distinct designs are required
- animation frame drift, popping, wrong loop rate, wrong context, or click interception
- static fallback missing when animation is hidden or unsupported

A missing final asset is a blocker. Do not create a primitive placeholder or recolor another asset to close the issue.

## 25. AI and time-progression pass

After deterministic interaction tests, run a bounded time-progression pass from a clean save.

Observe:

- event timer behavior
- repeatable and fire-once state
- major-event weight behavior when in scope
- evolution pacing
- decision and mission AI
- focus AI
- country survival and reinforcement
- invalid target cleanup
- event, decision, mission, or log spam
- excessive whole-world iteration symptoms
- unexpected performance degradation

Do not implement a new `on_daily`, `on_weekly`, `on_monthly`, or other all-country iteration as a live-fix shortcut unless the user has explicitly authorized that design under `AGENTS.md`.

## 26. Defect ownership and routing

Fix a defect directly when it is narrow, reproducible, and inside the current feature.

Use relevant project subagents only when they save time or provide a required specialty. They remain optional and must be spawned with `fork_context=false` and a complete explicit prompt.

Examples:

- narrow localisation defect: `chaosx_localisation_auditor`
- narrow decision or mission defect: `chaosx_decision_mission_auditor`
- narrow focus defect: `chaosx_focus_tree_auditor`
- narrow country-package defect: `chaosx_country_package_auditor`
- repeated helper defect: `chaosx_scripted_system_architect`
- missing sourced or generated asset: the correct asset subagent and asset skill
- broad shallow design exposed by testing: report it and route to `chaosx_improvement_loop_planner`, do not redesign it during QA
- spec-versus-implementation uncertainty near completion: `chaosx_event_completion_auditor`

Do not use `chaosx_repo_explorer` for an error that already identifies exact files and IDs.

The parent agent remains responsible for the live loop, integration, relaunch, retest, and completion claim.

## 27. Fix acceptance

A Chaos Redux fix passes only when:

- the original issue reproduces before the fix or has direct fresh-log proof
- the owning source-of-truth and relevant implementation rules were read
- the patch is bounded and does not use an unapproved fallback
- the game relaunches through the debug shortcut
- the original fresh error is absent
- the original visible sequence now passes
- one nearby regression check passes
- Event Logs, Chaos Meter, docs, catalog, or other dependent surfaces remain aligned when applicable
- screenshots show the corrected state when the issue was visual
- save and reload passes when persistent state changed

Do not accept a fix solely because the parser error disappeared.

## 28. Full-catalog coverage ledger

For `catalog-coverage`, create `coverage.csv` with at least:

```text
test_id,catalog_id,name,catalog_status,implementation_status,primary_country,setup_method,baseline_result,evolution_result,cluster_result,scenario_result,ui_result,save_reload_result,log_result,screenshot_refs,fix_refs,final_status,blocked_reason
```

Allowed final statuses:

- `pass`
- `fixed_and_passed`
- `failed`
- `blocked`
- `needs_user_review`
- `not_implemented`
- `not_covered_single_country`
- `not_applicable`

Never convert `not_implemented` or `not_covered_single_country` into `pass` to improve the coverage percentage.

## 29. Completion standard

A scoped Chaos Redux autonomous run is complete only when:

- the exact supplied shortcut was used or an explicitly approved replacement was recorded
- the active log directory was verified by freshness
- Chaos Redux was visibly loaded
- startup and country-map entry produced no new attributable blocking error
- the primary country and test mode were recorded
- every scoped catalog row or named test has a result
- Event Logs and relevant project UI were visually checked
- every confirmed defect was fixed and retested, or clearly blocked
- every fix has fresh-log and live-game evidence
- persistent changes survived save and reload when applicable
- no required asset, AI, localisation, documentation, or catalog alignment was silently omitted
- no fallback or simplification was used without explicit user approval
- unrelated files and ordinary saves were not altered

For catalog coverage, completion means the ledger is honest. It does not mean every unfinished idea in the catalog has become testable.

## 30. Final report

Use:

```markdown
# Chaos Redux Autonomous Debug Playtest Report

## Run configuration
## Source specs and skills used
## Launch and fresh-log evidence
## Startup repair cycles
## Primary-country test session
## Event, evolution, cluster, and scenario coverage
## UI, scripted GUI, asset, and super-event findings
## Confirmed defects and fixes
## Save and reload results
## Screenshots
## Files changed
## Catalog or documentation mismatches
## Simplifications, fallbacks, and blockers
## Final status
```

State separately:

- what is verified in game
- what is fixed and verified
- what remains blocked
- what was not covered because of single-country mode
- what is not implemented
- what needs a design decision

Do not claim the whole mod is complete because the scoped test run passed.
