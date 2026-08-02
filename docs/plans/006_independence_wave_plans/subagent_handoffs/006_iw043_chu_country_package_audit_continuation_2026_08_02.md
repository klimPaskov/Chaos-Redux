# IW-043 CHU country-package audit continuation

Date: 2026-08-02 (Europe/Kyiv).

Scope: Event 006 IW-043 Middle Volga Congress on the vanilla `CHU` carrier only.

Disposition: HOLD and fail-closed. CHU remains outside the central content-attestation set and no admission flag was changed.

## Coverage checklist

| Surface | Current result |
| --- | --- |
| Carrier and tag | Vanilla `CHU` remains the shared carrier for IW-043 and IW-046. Exact package and origin gates are present in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:19-30`. |
| Map and state setup | IW-043 still requires the researched states `249` and `256`, with compact anchor `249`, and does not alter the vanilla CHU history shell. |
| Setup and force proof | The setup gate requires the current IW-043 mapping, applied force package, and current-generation force receipt. The missing CHU cosmetic-ready setter was patched below. |
| Politics, leaders, and parties | Four male institutional CHU characters, route roles, staged ideas, and party localisation remain source-wired. No advisor role or advisor portrait is present or authorized. |
| Portraits and flags | Existing CHU large portrait consumers and cosmetic flags remain wired. The Spasov river-security consumer is promoted and hash-verified in `006_iw043_chu_spasov_postwire_portrait_receipt_2026_08_02.md`; Mirsaid Sultan-Galiev, Galimzhan Ibrahimov, and Karim Tinchurin remain rights, provenance, date, or role-gated as documented in the current portrait handoffs. No new portrait or flag was added in this setup patch. |
| Focus and decisions | IW-043 package focus effects, the shared full-framework assignment, decisions, missions, and focus and decision icons remain present. Shared focus geometry and MCP `SCAN_BYTE_LIMIT` remain whole-event blockers. |
| Ideas and assets | The three IW-043 idea slots and registered icons are present. No fallback icon, portrait, flag, advisor, or dossier derivative was created. |
| Forces, technology, industry, supply | Dynamic force mapping, inherited technology and slots, starting stockpiles, air and navy transfer, formation template, and supply receipts remain owned by the shared force layer. The installed package exposes no Technology Tree Viewer, so technology-tree inspection remains unresolved. |
| AI and playability | CHU foundation, recovery, crisis, federal, restoration, emergency, and normalization profiles remain origin and route gated with `abort_when_not_enabled = yes`. Live AI behavior remains parent-owned future QA. |
| Formables and cleanup | FORM-12 and FORM-13 adapters, consent and anchor ledgers, vanilla shortcut guards, and generation cleanup remain fail-closed and unchanged. |

## Safe patch

Changed file: `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1263-1289`.

Changed identifier: `independence_wave_iw043_cosmetic_identity_ready` only.

Before: `has_independence_wave_iw043_setup_surface` required `independence_wave_iw043_cosmetic_identity_ready` at `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:916-922`, but the IW-043 setup effect had no setter, so a valid CHU force package could never pass setup-surface validation.

After: `independence_wave_setup_iw043_middle_volga` clears the receipt at entry and sets it only after `independence_wave_force_mapping_loaded`, the IW-043 mapping package id, `independence_wave_force_package_applied`, and `has_independence_wave_force_package_for_current_generation = yes` all pass.

The patch does not set package identity, assign a leader, promote a portrait, register a formable, or change central attestation. It only makes the existing setup gate reflect the already-required current-generation force proof.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic or high-chaos selectable packages, 138 SCN-008 ranked packages, 14 attested packages, and 13 compatible reservation groups.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
- `python -B .tools/audit_chaosx_country_tags.py` passed with zero external country-definition or identity-surface collisions.
- Targeted source-order inspection confirms the clear occurs at setup entry, the receipt setter follows the force pass, and the setup-surface trigger consumes the same receipt.
- No Hearts of Iron IV process, live execution, save/load, or player-owned runtime validation was run.

## Remaining blockers and admission status

CHU remains unadmitted because the grounded roster still lacks a rights and role-cleared replacement for the Bolgar civic-presidium consumer, the current portrait shelf remains provenance-only for unresolved rows, shared focus diagnostics remain unresolved, and the installed package has no Technology Tree Viewer.

The patch is limited to CHU-owned setup logic and does not resolve portrait, asset, formable, focus, AI, balance, runtime, or whole-event admission blockers.
