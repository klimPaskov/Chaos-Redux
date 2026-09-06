# Event 006 Balkan decision registry marker cleanup — 2026-09-06

## Disposition

Implemented a source-hygiene cleanup. Removed the stray `# temporary_remove_immediately` line from `common/decisions/006_independence_wave_balkan_decisions.txt`; no decision identifiers, triggers, costs, effects, localisation, or package gates changed.

## Validation

- The Balkan registry now matches its committed executable source apart from unrelated working-tree changes having been absent before this cleanup.
- `python .tools/audit_event6_allocator.py --strict` continues to pass with the exact 3/4/5/7/10 ladder and retired pre-event crisis surface.
- `python .tools/audit_event6_country_api.py` continues to pass with no missing or duplicate country rows.

## Scope limits

This cleanup does not promote any Balkan package, alter central attestation, or change the no-pre-event boundary. Runtime/MCP/live validation remains subject to the existing Event 006 evidence limits.
