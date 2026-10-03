# Gods requirement text

Disposition: implemented and reviewed in source; native tooltip presentation remains unobserved.
Acceptance basis: the user requires complete Gods localisation, and AGENTS.md requires meaningful text for player-visible flag checks.

The parent checked both Gods localisation and the dedicated Event 012 requirement-flag file before editing.
Commit `d0a58e779` already provided most relevant flag keys, so they were retained rather than duplicated in the Gods file.
Fifteen missing keys were added: twelve focus capability receipts, consolidation, loss of African authority, and recent extreme punishment.
Ten existing descriptions were corrected or tied to their exact focus titles.
The same keys continue to represent the same predicates; no gameplay gate, cooldown, cost, or AI weight changed.

The focus receipts refer to their existing focus-title localisation using `$key$` substitution.
The titles and reward flags were checked against the Gods overlay in `common/national_focus/012_africa_continental_focus_tree.txt:7307-8110`.
The Office of the Voices, arsenals, expedition, logistics, reserve, sanctuary, security, shelter, relief, judgment, reach, offense memory, final council, Last Sentence, and final settlement labels name the corresponding focus.
Substitute conditions describe tribute offers, since their stored data are material family/amount slots rather than country targets.
The escalation receipt describes Africa's response to an offense, and the reliable-partner receipt describes the memory established by compliance rather than claiming a previous protection pledge.

The bounded coverage pass found all 52 literal Africa/Gods flag tokens used in `012_africa_gods_decisions.txt` and `012_africa_gods_triggers.txt` in the English requirement or Gods files.
The overlay's six literal flag tokens are also covered.
This does not claim every dynamically assembled flag or every unrelated Event 012 file has been audited.

Changed files:

- `localisation/english/012_africa_requirement_flags_l_english.yml`: only Gods requirement text.
- `docs/events/012_africa/gods_of_africa.md`: current coverage and remaining scope.
- `012_africa_gods_localisation_audit_2026-10-03.md`: reconcile the historical single-file audit with the dedicated flag registry.
- This handoff: scope, references, and validation limits.

Relevant offline reference is `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:543-550`, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, which confirms flag names appear as requirement localisation keys.
Installed `documentation/triggers_documentation.md`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, supplies the country-flag predicate's scope and date/value behavior.
Vanilla `localisation/english/aat_tooltips_l_english.yml:208` uses another localisation key in the `DEN_had_volunteer_only_flag` flag text, and `aat_focus_l_english.yml:418` supplies concrete `FIN_finno_soviet_pact_flag` text.
The parent requested a bounded localisation reference context; its response is pending at this handoff's preparation, so these pertinent local sections were read directly.
Earlier revision-bound localisation evidence remains in the original audit.

No catalog Event Details, evolution text, assets, focus source, or decision source changed.
No workbook update, art generation, dedicated GUI, or live launch is needed for this source-text tranche.
The current supplied menu-load log does not exercise the changed requirements.
No native tooltip layout or visual completion is claimed.
No design simplification was introduced.
Skills used: events, decisions/missions, focus trees, subagents, and shared Git commit.
