# Event 011 Secret Alliance Planning Package

This package is the source design handoff for Chaos Redux Event 011, **Secret Alliance**.

The event remains a Minor Fire-Once event. Its core identity is a hidden anti-player coalition that begins with three countries, recruits additional members, interferes with the target country, and becomes a real faction when secrecy fails or the coalition enters its final escalation.

The package is split so implementation agents can read the design in a useful order without mixing design, research, asset production, and coding instructions.

## Recommended reading order

1. `specs/011_secret_alliance_spec_part_1_core_and_hidden_pact.md`
2. `specs/011_secret_alliance_spec_part_2_progression_and_evolutions.md`
3. `specs/011_secret_alliance_spec_part_3_counterplay_and_decisions.md`
4. `specs/011_secret_alliance_spec_part_4_reveal_war_and_scenario.md`
5. `specs/011_secret_alliance_spec_part_5_ai_presentation_and_acceptance.md`
6. The matrices under `matrices/`
7. The research notes under `research/`
8. The specialist prompts under `prompts/`
9. The review and architecture handoffs under `handoffs/`

## Design boundaries

The event uses existing countries. It does not create a new country tag and it does not replace national focus trees. The coalition is event-owned and is expressed through hidden membership, operations, decisions, ideas, AI strategies, and a reveal faction.

This keeps the event compatible with any player country, any ideology, and countries that already have substantial content. It also prevents a minor event from overwriting unrelated national identities.

The specification gives direction for all player-facing text. It does not provide final localisation that can be pasted into the game. The implementation pass must write final text from the supplied tone and information rules.

The reveal super-event has a researched quote recommendation, but its final title, description, button wording, image, and audio remain gated behind the dedicated super-event research and asset workflows.

## Package status

The source reading, design, historical research, architecture pass, decision and mission review, localisation review, asset routing review, improvement-loop review, and completion review are represented in this package.

The current environment did not expose the Chaos Redux custom subagent spawning interface. The supplied subagent TOML contracts were therefore read in full and applied as separate manual specialist passes. The corresponding handoffs state this limitation directly and do not claim that an external subagent process ran.

## Verification files

- `source_inventory.md` records every supplied source file, byte count, line count, SHA-256 hash, and full-reading status.
- `manifest.md` records the complete package file list and hashes.
- `handoffs/completion_audit.md` compares the package against every requirement in the Event 011 brief.
- `handoffs/improvement_loop_closure.md` records the mandatory depth and anti-bloat conclusion.

The package contains 33 Markdown files and about 41,000 words before ZIP packaging. The goal prompt is 3,756 characters, within the required 3,500 to 4,000 character range.
