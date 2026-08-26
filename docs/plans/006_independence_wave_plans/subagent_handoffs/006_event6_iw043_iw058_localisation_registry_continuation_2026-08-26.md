# Event 006 IW-043/IW-058 localisation registry continuation

## Scope

This source-layout continuation consolidates the four disjoint IW-043/IW-058 English localisation parser files into one package registry. It does not widen the adapter-only fail-closed boundary, promote either package, or alter executable identifiers.

## Files

- Receiver: `localisation/english/006_independence_wave_iw043_iw058_l_english.yml`
- Removed: `localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml`
- Removed: `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml`
- Removed: `localisation/english/006_independence_wave_iw043_iw058_events_l_english.yml`
- Removed: `localisation/english/006_independence_wave_iw043_iw058_focus_l_english.yml`
- Active source-of-truth updates: `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

## Preservation proof

The four former files contained 886 unique localisation key/value pairs after excluding their repeated `l_english:` roots. The receiver contains the same 886 unique pairs, with no missing, extra, or duplicate key, and keeps concise source markers for country/core, category, decision, incident-event, and focus sections. The receiver remains UTF-8 with BOM and one `l_english:` root.

## Runtime boundary

Localisation is auto-loaded by the English localisation directory, so no event, decision, focus, package gate, country-tag, portrait, or adapter reference changes. Historical handoffs may continue to mention the former parser paths as evidence; the active source map and resume packet point to the consolidated receiver.

## Validation

- Key/value crosswalk against `HEAD` versions: 886 old entries, 886 new entries, no missing or extra pairs, no duplicate keys.
- BOM check: receiver starts `239,187,191` and has one `l_english:` root.
- Source-size check: 164 bytes saved after removing repeated roots and redundant file banners.
- Static Event 006 validators remain the required follow-up after commit.

## Simplifications and blockers

None. This is a source-layout consolidation only; no gameplay, admission, or wording simplification was made.
