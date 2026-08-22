# Event 016 D’Rhondan Contact Localisation Audit Handoff

Date: 2026-08-21

## Scope and authority

Audited `localisation/english/016_dhrondan_contact_l_english.yml` against the binding `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md`, the contact decisions and missions, events `chaosx.nr16.40` through `.47`, the envoy special project, the contact constants and effects needed to verify displayed values, and `docs/events/016_brilliant_scientist/systems/dhrondan_contact.md`.

No API definitions, Event 019 files, units, equipment, tactics, DHR country or focus files, assets, achievements, or catalog files were edited.

## Files changed

- `localisation/english/016_dhrondan_contact_l_english.yml`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_contact_localisation_audit_handoff_2026-08-21.md`

## Changed keys

- `sp_dhrondan_envoy_craft_desc`
- `dhrondan_send_kruger_to_dhronda_desc`
- `dhrondan_send_mengele_to_dhronda_desc`
- `dhrondan_expedition_fuel_cost_tt`
- `dhrondan_send_mengele_to_dhronda_effect_tt`
- `dhrondan_kruger_expedition_mission_desc`
- `dhrondan_mengele_expedition_mission_desc`
- `dhrondan_honor_accord_desc`
- `dhrondan_rebellion_pulse_mission_desc`
- `chaosx.nr16.40.a.tt`
- `chaosx.nr16.41.kruger.d`
- `chaosx.nr16.41.mengele.d`
- `chaosx.nr16.42.mengele.d`
- `chaosx.nr16.42.a.tt`
- `chaosx.nr16.43.kruger.d`
- `chaosx.nr16.43.mengele.d`
- `chaosx.nr16.43.a.tt`
- `chaosx.nr16.44.d`
- `chaosx.nr16.44.a.tt`
- `chaosx.nr16.45.kruger.d`
- `chaosx.nr16.45.mengele.d`
- `chaosx.nr16.45.a.tt`
- `chaosx.nr16.46.a.tt`
- `chaosx.nr16.47.a.tt`

## Audit lists

### Missing keys

None. The 58 expected project, category, decision, mission, event title, event description, option, and tooltip keys are present.

### Duplicate keys

None in the assigned file and none for its 58 keys elsewhere under `localisation/english/`.

### Scripted localisation issues

None. This surface uses no `defined_text` blocks or scripted-localisation calls. The dynamic status tokens `[?dhrondan_alien_presence|0]` and `[?dhrondan_pact_strain|0]` remain intact.

### Dynamic text opportunities

The two live pact values are already dynamic in `dhrondan_contact_status_header`. Expedition duration remains consumer-driven through `dhrondan_expedition_days`; the rebellion mission reads `constant:dhrondan_contact.rebellion_pulse_days` directly so daily engine activation after a chaos-only threshold change always receives the full 90-day window. No additional dynamic localisation was added because the displayed requirements are fixed script constants and the current consumers already expose mission countdowns.

### Cross-surface mismatch notes

- The displayed expedition values match `constant:dhrondan_contact.expedition_political_power_cost = 50`, `expedition_fuel_cost = 500`, and `expedition_days = 180`.
- The displayed Kruger authorization changes match the runtime effects: Mandate +10, Dependence +10, Exposure +5, Independent Capacity +10, and Grievance -5. The return report now states the separate Mandate +5, Dependence +5, and Independent Capacity +5 reward exactly.
- The displayed accord values match the runtime decision and effect: 75 Political Power, Pact Strain -10 with a zero clamp, and a 180-day cooldown.
- The rebellion mission text matches the country-scoped 90-day runtime variable.
- Valid expedition timeout opens `chaosx.nr16.42`, whose sole option establishes the pact once. The tooltip now describes that guaranteed valid-return outcome without the internal phrase “valid expedition.”
- All eight purpose-built report DDS files and the purpose-built decision, category, and project DDS files exist. No matching sprite definitions were found anywhere under `interface/` for the referenced `GFX_report_event_016_dhrondan_*`, `GFX_decision_*dhrondan*`, or `GFX_sp_dhrondan_envoy_craft` consumers. This is an unresolved asset-wiring blocker outside this localisation patch.

### File encoding concerns

None. The localisation file begins with the UTF-8 BOM bytes `EF BB BF`.

### Prose-quality issues found and repaired

- Vagueness: Replaced “recovered geometry,” “valid return,” and generic authorization language with concrete plans, exact expedition terms, and clear success or failure outcomes.
- Bloat: Shortened explanations of the Mengele route, return, and failure while preserving its independence from Kruger.
- Obvious explanation: Replaced tooltips that narrated source bookkeeping with the actual unlocked production, landings, pact state, and territorial consequences.
- Repetition: Consolidated repeated statements about route receipts and cleanup into concise player outcomes.
- Overcomplication: Removed “contact receipt,” “Kruger ledger,” “country-scoped rebellion pulse,” “public alien-infantry system,” and “country-package revolt effect” from player-facing text.
- Style-rule repair: Standardized Directorate capitalization, used exact numeric durations, removed the staged contrast in the landing description, and confirmed that the assigned file contains no em dash, semicolon, straight apostrophe inside a value, or update-history wording.

### Sourced quotation preservation

No sourced or attributed quotation appears on the inspected project, decision, mission, or event surfaces. No quotation required preservation.

## Display before and after

Before, the decisions exposed fuel as a bare icon and number, omitted the complete 50 Political Power and 180-day terms from their descriptions, and described several outcomes through internal receipts, ledgers, validity checks, bookkeeping, and bridge effects.

After, both expedition descriptions state 50 Political Power, 500 fuel, and 180 days. The Kruger tooltip preserves all authorization deltas, the return report states the three +5 Directorate rewards, the accord states 75 Political Power, -10 Pact Strain, and 180 days, and the rebellion text states the 90-day pulse. Success, failure, landing, and revolt text now describes what the player receives or loses.

## Dynamic localisation added or fixed

None added. Existing dynamic pact-value tokens were preserved unchanged.

## Owner post-audit corrections verified

The owner made three final tooltip corrections after the localisation patch. `chaosx.nr16.44.a.tt` now states Alien Presence +1 and Pact Strain +5 exactly. `chaosx.nr16.45.a.tt` now says only that this expedition grants no D’Rhondan pact or alien-contact access, so an existing receipt from another source is not contradicted. `chaosx.nr16.46.a.tt` now states the exact 90-day timing and the six-cohort, Pact Strain 30, and global chaos 600 eligibility gates.

All three corrections use direct player-facing prose and contain no em dash, semicolon, internal implementation term, update-history wording, or apostrophe defect. The localisation file still begins with the UTF-8 BOM bytes `EF BB BF`.

## Meaningful validation

- Compared all 58 expected localisation keys to the project, category, decision, mission, and event consumers. No key is missing or duplicated.
- Traced the displayed costs, durations, Directorate deltas, pact establishment, accord reduction, and rebellion duration to `016_dhrondan_contact_constants.txt`, `016_dhrondan_contact_effects.txt`, `016_dhrondan_contact_triggers.txt`, and `016_dhrondan_contact_decisions.txt`.
- Checked every referenced contact-chain GFX token against `interface/` and its expected purpose-built DDS family. The DDS files exist, but the sprite definitions are currently absent.
- Ran targeted scans for em dashes, semicolons, internal receipt and ledger wording, update-history terms, and straight apostrophes in values. No assigned localisation value still matches those patterns.

## MCP evidence and skipped validation

Mandatory HOI4 event inspection could not complete. `hoi4.event_inspect` timed out after 180 seconds for both the `chaosx.nr16.40` downstream trace and the file-scoped scan of `events/016_brilliant_scientist_dhrondan_contact_events.txt`. `hoi4.event_render` also timed out after 180 seconds for the same chain. No artifact URI or rendered overflow evidence was produced, so source review is not treated as equivalent engine evidence.

The installed package has no Technology Tree Viewer, which is irrelevant to this bounded non-technology text surface.

## Unresolved wording decisions

None.

## Recommended follow-up

- The parent or asset-wiring owner should define the purpose-built contact-chain sprites in an in-scope `.gfx` file and then rerun an event render once the HOI4 event MCP route responds.
- Recheck event popup overflow after the MCP route is available because the current timeout prevented rendered text-fit evidence.

## Plan handoff

No separate design-gap plan was written. The missing sprite definitions are a bounded wiring defect for the parent or asset owner, not a localisation design expansion.

## Simplifications, omissions, and blockers

No localisation fallback or simplification was used. Rendered MCP evidence and sprite definitions remain blocked as described above.
