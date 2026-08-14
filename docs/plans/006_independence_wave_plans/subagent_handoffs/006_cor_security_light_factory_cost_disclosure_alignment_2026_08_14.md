# COR security-light factory cost disclosure alignment

Date: 2026-08-14

Scope: narrow player-facing cost disclosure repair for admitted IW-017/COR.

## Change

`independence_wave_cor_secure_mountain_post_road` pays the existing security-light resource bundle and reserves the light civilian-factory tier, but its previous shared security-light card omitted that factory reservation.

The decision now selects the dedicated `independence_wave_cost_security_light_factory` triplet, which preserves the light security resources and adds the light-factory reservation through the shared decision-cost constant.

The shared `independence_wave_cost_security_light` triplet was not changed because other callers use it without a civilian-factory reservation.

Only the COR selector and the new base, tooltip, and blocked localization keys changed; payment effects, affordability triggers, duration, AI score, lifecycle guards, and cleanup remain unchanged.

## Validation

The new key has one base entry and complete `_tooltip` and `_blocked` siblings in the UTF-8-BOM Event 006 decision localization.

The COR selector has exactly one consumer and its modifier remains `CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT`.

The admitted Event 006 allocator and scenario-matrix audits remain unchanged at 149 publishers, 126 automatic publishers, 138 SCN-008 publishers, 40 adapters, 32 attested packages, 29 compatible groups, and 161 unattested rows.

No central adapter, attestation, Join, portrait, flag, workbook, AI, payment, or cleanup surface was changed.
