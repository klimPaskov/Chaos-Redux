# Event 012 RSA settlement completion guard

Date: 2026-08-02.

Status: implemented source guard, live acceptance still open.

## Scope

The continental focus-route settlement counter previously accepted the RSA country receipt `africa_rsa_allied_settlement_complete` without checking the global one-use settlement lifecycle. The canonical RSA completion trigger already requires both the surviving country's receipt and `africa_rsa_settlement_completed`.

## Change

`africa_country_counts_as_allied_restored_settlement` now calls `africa_rsa_allied_settlement_is_complete` for the RSA branch. Loyalist and coalition settlement writers already set the country and global receipts together. Restored-polity and priority-member branches remain unchanged, and no opinion, alliance, tag, core, or new country state is introduced.

This prevents a stale or prematurely copied RSA country flag from counting toward continental settlement before the Allied civil-war lifecycle has actually completed.

## Files changed

- `common/scripted_triggers/012_africa_focus_route_triggers.txt`
- this handoff

## Validation

Source inspection confirms the canonical helper definition, both RSA settlement writers, and the single focus-route consumer. The expected bounded cases are: both receipts present passes, country receipt alone fails, global receipt alone fails, and unrelated restored or priority packages still use their existing explicit flags.

Hearts of Iron IV was not launched and no live-save validation was performed, per repository instructions.

## Remaining blockers

RSA civil-war, settlement, exile, and no-patron scenarios still need live acceptance. The broader Event 012 package remains incomplete because W5 receipts, priority-package provenance, achievement and AI scenario evidence, model packages, terminal presentation/audio, native-language review, and focus/UI runtime checks remain open.
