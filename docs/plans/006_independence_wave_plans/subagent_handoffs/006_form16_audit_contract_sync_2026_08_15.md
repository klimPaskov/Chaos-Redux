# FORM-16 audit contract synchronization

The dedicated `.tools/audit_event6_form16.py` audit was failing on a stale
spelling assumption: the current runtime trigger proves the transaction gate
with `has_country_flag = independence_wave_formable_transaction_ready`, while
the audit only accepted a scripted-trigger call of the same conceptual name.
The source already carries that flag together with runtime prevalidation,
formation-ready state, congress vote, identity, territory, member, arbitration,
generation, rollback, and cleanup predicates.

The audit now accepts either documented spelling without weakening the gate.
The current source audit passes for the admitted ARM/GEO/AZR carrier family,
states 230/231/229, consent/refusal event, transaction mutation, and rollback
cleanup. This is an audit-tool synchronization only; no FORM-16 gameplay,
readiness, admission, Join, GUI, or asset behavior changed.
