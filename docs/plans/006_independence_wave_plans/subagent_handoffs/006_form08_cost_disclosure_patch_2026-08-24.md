# FORM-08 Danubian project cost disclosure patch

Date: 2026-08-24.

Status: **SOURCE-APPLIED / STATICALLY VERIFIED**.

## Scope

The three FORM-08 Danubian charter projects no longer share one inaccurate cost string. Congress, arbitration, and transport now each select an action-specific `custom_cost_text` and blocked variant.

The old shared wording incorrectly displayed War Support and omitted the distinct security resources used by arbitration. It also hid that congress and transport combine the strategic and administrative command commitments.

## Source changes

- `common/script_constants/006_independence_wave_decision_constants.txt` adds the centralized 40-command-power combined FORM-08 commitment, its payment value, and the strict-resource gate value.
- `common/scripted_triggers/006_independence_wave_form08_triggers.txt` adds the combined administration-plus-strategic affordability helper and routes congress/transport through it.
- `common/scripted_effects/006_independence_wave_decision_effects.txt` adds the matching combined payment effect with the existing convoy/train fallback.
- `common/scripted_effects/006_independence_wave_form08_effects.txt` uses that payment for congress and transport; arbitration uses only the standard security payment contract.
- `common/decisions/006_independence_wave_form08_decisions.txt` selects three dedicated cost keys.
- `localisation/english/006_independence_wave_formable_registry_l_english.yml` discloses the actual resources in compact action-specific groups, removes the obsolete War Support wording, and preserves UTF-8 BOM encoding.

Congress and transport show stability plus the combined command commitment, transport reserve, and manpower. Arbitration uses the four-group standard security package (manpower, army experience, infantry equipment, and support equipment) instead of stacking a second strategic bundle. Civilian-factory availability remains a project-capacity trigger, not a falsely displayed consumed resource.

## Validation boundary

- The existing `can_pay_independence_wave_form08_*` triggers and payment effects remain paired by action; no AI weight or route gate was changed.
- The combined trigger uses a 39-point strict gate so exactly 40 command power remains sufficient for the 40-point payment.
- Static Event 006 allocator, country API, flag-family, and SCN-008 matrix audits pass after the change.
- MCP probability-source discovery passes for all three FORM-08 mission candidates with no source diagnostics or unresolved inputs; no balance comparison is claimed because the adapter exposes no evaluable decision candidates.
- No live Hearts of Iron IV run or live tooltip observation was performed in this source tranche.
