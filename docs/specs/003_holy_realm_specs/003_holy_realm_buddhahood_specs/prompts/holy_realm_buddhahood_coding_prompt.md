# Resume Prompt: Holy Realm Buddhahood

This is the single task brief for further Holy Realm Buddhahood work.
It replaces the former goal, decision, achievement, super-event and asset prompts, whose requirements live in the spec files.

The Holy Realm is implemented.
Do not rebuild the event chain, focus tree, decisions, Mandala GUI, portraits, Mandala animation, super-events or achievements.
Start from `docs/events/003_holy_realm/overview.md` and `docs/plans/003_holy_realm_plans/release_qa_completion_20261006.md`, then read only the spec sections that govern the item you take.

Pick work only from these sources:

- An Open questions item in the [package README](../README.md) after its proposal is accepted by the user or parent; record that acceptance in the README before editing source.
- An open gate in the [route coverage matrix](../matrices/holy_realm_buddhahood_route_coverage_matrix.md).
- A defect found in current source.

Follow `CLAUDE.md` and the skills it routes: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-super-events`, `chaos-redux-event-assets` and `chaos-redux-frame-animation`.
Use `chaos-redux-scripted-gui` and `chaosx_event_ui_worker` for the Mandala window, with a recorded reference, exact window and source identifiers, states and resolutions.
Shared event details, event logs, settings and the super-event framework remain parent-owned.
Route every character portrait to `chaosx_portrait_creator` and every changed weight to the read-only `chaosx_ai_probability_auditor` with a same-scenario before and after comparison.

Keep these rules intact:

1. Final Silence can start only after Buddhahood, and its terminal branch requires Chaos above 1000 and hands the world-end to Fallout.
2. Buddha powers require Meditation Charge and act only against valid chaos actors with a current hostile front.
3. Portrait, Mandala state, country identity and super-event presentation change when the Bodhisattva becomes the Buddha.
4. No refuge or relief action creates manpower, food or equipment without a real source.
5. Calendar dates may scale AI weights but never decide availability.
6. The concentration sequence stays a timed, paid commitment, never an instant purchase; its acceptance as the three-minute hold replacement stays unresolved until recorded.
7. Hidden achievements stay hidden in player-facing text.

Report changed files, identifiers, meaningful validation, every simplification and the remaining gates, and update the release reconciliation instead of creating a new report.
