# Event 006 IW-093/IW-098 localisation registry continuation

## Scope

This source-layout continuation consolidates the three disjoint IW-093/IW-098 English localisation parser files into one package registry. It does not widen package admission, change the adapter-only fail-closed boundary, or alter executable identifiers.

## Files

- Receiver: `localisation/english/006_independence_wave_iw093_iw098_l_english.yml`
- Removed: `localisation/english/006_independence_wave_iw093_iw098_country_core_l_english.yml`
- Removed: `localisation/english/006_independence_wave_iw093_iw098_decisions_l_english.yml`
- Removed: `localisation/english/006_independence_wave_iw093_iw098_focus_l_english.yml`
- Active source-of-truth updates: `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

## Preservation proof

The three former files contained 340 unique localisation key/value pairs after excluding their repeated `l_english:` roots. The receiver contains the same 340 unique pairs, with no missing, extra, or duplicate key, and retains source markers for the former country/core, idea, category, decision, and focus sections. The receiver remains UTF-8 with BOM and one `l_english:` root.

## Runtime boundary

Localisation is auto-loaded by the English localisation directory, so no event, decision, focus, package gate, portrait, country-tag, or adapter reference changes. Historical handoffs may continue to mention the former parser paths as evidence; the active source map and resume packet point to the consolidated receiver.

## Validation

- Key/value crosswalk against `HEAD` versions: 340 old entries, 340 new entries, no missing or extra pairs, no duplicate keys.
- BOM check: receiver starts `239,187,191` and has one `l_english:` root.
- Static Event 006 validators remain the required follow-up after commit.

## Simplifications and blockers

None. This is a source-layout consolidation only; no gameplay or wording simplification was made.
