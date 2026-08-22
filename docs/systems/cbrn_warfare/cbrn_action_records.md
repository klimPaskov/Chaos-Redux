# CBRN Unified Action Records

## Purpose

The package-wide action ledger gives every accepted deliberate chemical delivery and deliberate biological seed one durable row with the fields required by Spec 09. It is separate from the native event-log view, but each row also creates one system-owned Event Log history entry whose payload is the aligned ledger row index.

## Record contract

The aligned `global.cbrn_action_record_*_entries` arrays store attacker, affected country, exact target state, date, weapon class, agent, delivery method, operation severity, civilian deaths, the native military-death receipt, chemical contamination change, biological outbreak change, evidence quality, attribution state, retaliation status, first-use status, and repeat-use pressure. A caller-supplied victim remains authoritative; when a route has no explicit victim target, the writer records the target state's owner and falls back to the actor only for an unowned state. The Event Log therefore never dereferences a numeric placeholder as a country.

Chemical action adapters write the resolved civilian-death count, contamination change, and the native military casualty fraction. The installed `damage_units` effect does not expose a killed-person count, so the military field is explicitly a normalized fraction receipt rather than an invented headcount.

Biological deliberate-use adapters append immutable identity rows before the incubation/outbreak lifecycle continues. Civilian deaths are updated from the shared civilian-death receipt as the current merged outbreak episode advances. A repeated seed gets a new row and cannot overwrite the prior row's attacker, victim, target state, route, or first-use status. Because the native biological lifecycle merges repeated seeds into one state episode, the current row owns the merged episode's later civilian-death total; the ledger does not invent per-seed attribution where the engine exposes only a merged episode total.

## Event Log consumer

Each deliberate row calls `record_events_log_system_history_entry` with event id 991, event type `event_system_event_type.cbrn_action`, and the ledger row index as payload. The dedicated type keeps these rows out of the Fallout-memory classification. The existing Chaos Redux Event Log shows the attacker and affected country and uses the CBRN detail localisation to expose the record's weapon class, agent, route, outcome, tracked deaths, contamination/outbreak change, evidence, attribution, retaliation, first-use status, and bounded repeat-use classification. The log is an observation surface. It does not replace the authoritative Deaths, Air Cleanliness, outbreak, Condemnation, or diplomacy ledgers.

## Engine boundary

This system performs no recurring country or world scan. It records only a validated action or the later biological lifecycle receipt. It does not estimate unsupported unit headcounts, continuous-air activity, live state weather, or live terrain conditions.
