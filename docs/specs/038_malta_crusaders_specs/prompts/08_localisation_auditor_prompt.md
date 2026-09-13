# Prompt for `chaosx_localisation_auditor`

Work with no inherited conversation context. Audit and make bounded patches to Event 38 localisation and scripted localisation only.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-super-events`, `chaos-redux-subagents`, and the full Event 38 spec pack, especially `20_event_logs_details_catalog_localisation.md` and the player-facing writing rules.

Audit every Event 38 visible surface:

- entry and follow-up events
- news and report events
- event options
- decisions, missions, costs, requirements, tooltips, and categories
- Crusade Council labels, buttons, values, thresholds, states, and tooltips
- focuses, focus requirements, navigation, and inlay text
- ideas, technologies, equipment, units, traits, laws, opinion modifiers, factions, country names, adjectives, parties, leaders, principalities, and formables
- evolution names and descriptions
- event log, Event Details, cluster, public Holy World row, and manual scenario
- super-event title, description, button, quote, and audio-facing documentation
- achievements
- scripted target, state, country, order, relic, and principality text

Check missing keys, duplicates, encoding, key syntax, raw tokens, decimal formatting, stale IDs, country or route leakage, cost texticons, long raw trigger output, hidden-route spoilers, implementation-history wording, debug text, update-history wording, and cross-surface mismatches.

Write in-world text. Never use em dashes or semicolons. Avoid staccato, empty drama, generic crisis communications, dialectical contrast formulas, and reusable AI-sounding templates. Do not present Nazi racial or Atlantean claims as fact. Keep atrocity text concrete and serious without cheap humour. Hidden Teutonic and Atlantis routes must remain absent from public catalog text.

Event Details describes premise and public state, not reward lists or secret gates. Tooltips still explain visible consequences and exact blocked requirements. Cost strings use amount plus matching texticon and no filler labels.

Patch clear local defects. List every key changed in the handoff at `docs/plans/038_malta_crusaders_plans/subagent_handoffs/localisation_auditor.md`. Flag wording that requires sourced quote or cultural-reference research rather than inventing it.
