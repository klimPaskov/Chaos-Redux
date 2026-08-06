# IW-026 Macedonia localisation audit and patch handoff

Date: 2026-08-06

## Outcome

The Macedonia package has complete local coverage for all 60 visible identifiers referenced by its decision category, mission and decisions, custom effect tooltips, ideas, party names, and character definition. No duplicate keys or broken scripted-localisation calls were found. The localisation file retained its required UTF-8 BOM.

The visible character name contradicted the sourced portrait and character definition. `MAC_independence_wave_vardar_presidium` rendered the institutional label `Vardar Presidium` even though the character file defines a male country leader and corps commander whose sourced identity is Metodija Andonov-Cento. The localisation now exposes that identity. The former-host negotiation also now uses the saved former-host scope instead of an abstract ledger label.

## Changed files

- `localisation/english/006_independence_wave_macedonia_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw026_macedonia_localisation_audit_2026_08_06.md`

No central admission file, gameplay script, AI weight, advisor surface, or other country package was changed.

## Changed keys

Content changes:

- `MAC_independence_wave_vardar_presidium`
- `MAC_independence_wave_vardar_presidium_desc`
- `independence_wave_mac_settle_yugoslav_ledgers`
- `independence_wave_mac_settle_yugoslav_ledgers_desc`
- `independence_wave_mac_host_ledgers_effect_tt`

All 60 keys in the file also had their leading indentation removed to match the repository localisation convention. Key names, namespaces, and gameplay references were preserved.

## Dynamic localisation added

- The negotiation title and description now display `[independence_wave_former_host.GetNameDef]`.
- The completion tooltip now displays `[independence_wave_former_host.GetNameDefCap]`.
- These tokens follow the existing Event 006 Iberian former-host precedent and the Macedonia decision is visible only while `has_independence_wave_living_former_host = yes`.

No existing dynamic token, formatting code, cost value, state name, timer, or sourced quotation was removed.

## Before and after

- Before: the male leader appeared as `Vardar Presidium`, obscuring the person shown by the wired Metodija Andonov-Cento portrait.
- After: the leader appears as `Metodija Andonov-Cento`, and his description directly identifies his work in Macedonia's provisional government.
- Before: the former-host decision used the abstract title `Settle the Former-Host Ledgers` and never named the other country.
- After: the title, description, and result name the current former host dynamically and state that war ends the talks.
- Before: all keys had a leading space.
- After: keys begin at column one without changing the `l_english:` header or BOM.

## Coverage audit

### Missing keys

None. The required set contains 60 keys and matches the 60 keys in the Macedonia localisation file exactly.

Shared cost keys are present in `localisation/english/006_independence_wave_decisions_l_english.yml`:

- `independence_wave_cost_administration_light`
- `independence_wave_cost_administration_standard`
- `independence_wave_cost_diplomatic_standard`
- `independence_wave_cost_security_standard`
- `independence_wave_cost_security_major`
- `independence_wave_cost_strategic`

### Duplicate keys

None among the Macedonia file or across English localisation for its 60 keys.

### Scripted localisation issues

None found. The package file does not call a `defined_text` block. The new former-host scope tokens match an existing Event 006 usage pattern.

### Dynamic text opportunities

Implemented: the former-host name in the settlement decision and result tooltip.

Remaining optional improvement: `independence_wave_mac_vardar_council_category_desc` could display the current civic-mandate and mountain-defence variables. This would require a deliberate shared Event 006 display convention and was not added during this bounded coverage audit.

### Cross-surface mismatch notes

- Resolved: the character, portrait sprite, and portrait handoff identify Metodija Andonov-Cento, while the old localisation exposed an institution.
- The male identity is confirmed by `gender = male` in `common/characters/006_independence_wave_macedonia_characters.txt`.
- No advisor, high-command, theorist, chief, dossier, or small-portrait role is defined. Advisor-related text appears only in source comments that explicitly forbid such a surface.
- Macedonia AI strategies contain no player-facing localisation reference and required no localisation key.
- Party-name and idea identifiers referenced by the package effects all resolve to this localisation file.

### File encoding concerns

None. The file begins with bytes `EF BB BF`, confirming UTF-8 with BOM before and after the patch.

## Prose-quality audit

### Vagueness

Resolved the two clearest cases: the institutional leader placeholder and the unnamed former host. `independence_wave_mac_route_effect_tt` remains intentionally shared across five government routes and therefore describes the route effect generically. A route-specific rewrite would require separate gameplay tooltip keys and is outside this localisation-only patch.

### Bloat

No material bloat remains. Decision descriptions generally lead with the action and keep their requirement or consequence in one or two sentences.

### Obvious explanation

No tooltip merely repeats its title. The custom effect tooltips add consequences beyond the visible decision label.

### Repetition

`Vardar`, `compact`, and `council` recur throughout the package, but they distinguish its municipal and mountain-defence identity rather than repeating whole claims. No deletion was warranted.

### Overcomplication

The abstract `former-host ledger` wording was replaced with direct country naming, concrete negotiation subjects, and the war cancellation condition. Other sentences remain readable on first pass.

### Style-rule repair

The new prose uses direct subjects and active verbs. The file contains no em dash, semicolon in prose, dialectical hedge, staccato chain, prompt fragment, implementation-history wording, or hidden-route disclosure.

### Sourced-quotation preservation

No sourced or attributed quotation appears on any inspected Macedonia localisation surface, so no quotation text was altered.

## Meaningful validation

- Cross-referenced the exact decision, tooltip, idea, party-name, and character identifiers from `common/decisions/006_independence_wave_macedonia_decisions.txt`, `common/scripted_effects/006_independence_wave_macedonia_package_effects.txt`, `common/ideas/006_independence_wave_macedonia_ideas.txt`, and `common/characters/006_independence_wave_macedonia_characters.txt`. Required keys: 60. Present keys: 60. Missing: 0. Extra: 0.
- Scanned all English localisation for duplicate occurrences of the 60 Macedonia keys. Duplicates: 0.
- Confirmed the six shared custom-cost keys and their dynamic constant tokens in the shared Event 006 decision localisation.
- Confirmed that the former-host dynamic syntax matches `006_independence_wave_iberian_l_english.yml` and that the decision requires a living former host.
- Confirmed the source character has only country-leader and corps-commander roles and is explicitly male.

## MCP evidence and limitations

The read-only Event Chain Viewer inspected the Macedonia decision source selector and returned revision `ac30ffb41cd030372cc34c0d4229d1d6c58242e02002e28c6a2c291bdd397238`, graph hash `e1ecab98dcea0cc6a837c50c386f108efec055aff103ad775c71aa0dd3dc90a2`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74f9140bee7c84b4bef8264c4415891b29f5449f9585419bb2c3a768d4f2c34c/00bcf1702a289be99a5d5aa215718c71f60ddede005247eaced9319ea2cb49d1/event-scan-ac30ffb41cd0.json`.

The result was `EVENT_INSPECTED_PARTIAL`: the installed event route produced a workspace event graph and does not provide a dedicated decision localisation or decision-card overflow renderer. It therefore cannot verify decision text overflow. Source review and length inspection were completed, but they are not treated as equivalent visual engine evidence.

## Skipped meaningful validation

- No decision-card render or resolution-based overflow comparison was available through the installed HOI4 MCP routes.
- No in-game validation was performed because live consumer testing belongs to the user.
- AI probability evaluation was not run because this task changed no AI weight or probability-bearing surface.

## Unresolved wording decisions

- The durable portrait handoff and runtime identifiers use the Latin transliteration `Metodija Andonov-Cento`, while cited source filenames also show `Čento`. This patch follows the accepted handoff spelling for cross-surface consistency. A project-wide decision to display the diacritic would need the portrait documentation and any mirrored catalog wording updated together.
- Route-specific effect text could name each installed government and its exact ledger deltas, but doing so requires additional per-route tooltip keys or scripted localisation and is left to the parent as optional follow-up.

No simplification or fallback was introduced.
