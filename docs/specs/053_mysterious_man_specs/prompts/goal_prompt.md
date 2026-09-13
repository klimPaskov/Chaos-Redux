Implement Chaos Redux Event 53, Mysterious Man, from every file under `docs/specs/053_mysterious_man_specs/`.

Follow `AGENTS.md`, the relevant repo skills, the offline wiki, vanilla documentation, and mandatory HOI4 MCP workflows. Preserve unrelated changes.

Keep Event 53 as a Chaos level 1 Minor Fire-Once event with no cluster. The parent event selects exactly one valid human-controlled ordinary country through a uniform draw. The chain stays attached to that country. Country-scoped visits never count as new firings. Pause them while the target is not human-controlled. End the chain when the target ceases to exist or stops using normal civilian systems, unless an owner supplies explicit legal-successor proof. Never retarget another player by guess.
An unrelated world-end flag does not cancel the chain while the selected target remains valid.

Each visit locks one valid demand and exact amount before the popup. Baseline demands Political Power. Evolution I at 400+ broadens demand types. Evolution II at 800+ raises their scale and enables major and compound consequences. Evolution III at 1000+ enables absurd demands and catastrophe packages. Payment removes the displayed cost once and protects only that visit. Refusal, including inability to pay, calls one Event 53-owned selector.

Implement the 57-entry registry in `quality/consequence_registry_manifest.md`. Build a fresh pool on every refusal. Add each currently valid live package exactly once and choose one uniform random entry. Do not weight, duplicate, prefer, suppress, or protect against repeats. Target, severity, and flavour variants stay inside their package. Compound consequences receive one ballot and prevalidate every component before mutation.

Event 53 owns lifecycle, demand selection, equal package selection, attribution, receipts, cleanup, and legal-successor transfer. Connected systems own crisis effects and cleanup through bounded adapters. Borrowed packages must not alter source-event firing, weight, timer, History, cluster, evolution, opening super-event, or world-end state. Require isolation, idempotence, receipts, and cleanup evidence.

Use documented neutral helpers, including `call_natural_disaster`, stockpile debits, building damage, exact population loss, and owner APIs. Keep the Event 53 selector out of `chaosx_dynamic_effects`.

Implement nationwide nuclear annihilation without an attacker country. Process every unique valid owned or controlled target state once through real nuclear-scale destruction, exact Deaths, fallout, and Air Cleanliness paths. Create no false Condemnation and do not directly set a world-end flag. Ordinary contamination may later make the Fallout owner eligible.

Use normal event popups and produce the five generated report-event scenes in the asset brief. Do not add a decision category, custom GUI, focus branch, country package, character portrait, animation, 3D model, achievement, manual scenario, super-event, investigation path, or Event 53-owned world-end branch.

Wire event registration, default enabled state after rework, Event History, Event Details, actor mapping, evolution logs, docs, assets, and final localisation. Update only the authoritative event catalog workbook after final in-game wording exists, then run the exporter. Never edit catalog CSV files directly.

Run every named validation and probability scenario with the MCP event and probability tools. Use relevant subagents with `fork_context=false` and complete prompts. Finish with localisation and completion audits.

Do not use placeholders, silent fallbacks, simplified packages, hidden weighting, scattered hardcoded tuning, duplicate population losses, fabricated attacker attribution, or source-event bookkeeping. Report every blocker or omission. Mark completion only when every accepted package is implemented or explicitly blocked, all active adapters have evidence, and every required log, asset, document, and catalog surface is aligned.
