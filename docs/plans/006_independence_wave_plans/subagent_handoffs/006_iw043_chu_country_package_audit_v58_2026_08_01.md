# IW-043 CHU country-package audit v58

Date: 2026-08-01 (Europe/Kyiv).

Scope: Event 006 IW-043 Middle Volga Congress on the vanilla `CHU` carrier only.

Disposition: HOLD / fail-closed; CHU was not admitted and no content-attestation gate was changed.

## Coverage checklist

| Surface | Evidence and disposition |
| --- | --- |
| Carrier and registration | Vanilla `CHU` remains the carrier in `common/country_tags/00_countries.txt` and `common/countries/Chuvashia.txt`; no duplicate custom CHU country was added. `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:19-30` requires original tag `CHU`, package `iw_043`, Event 006 origin, package flag, and Soviet Collapse exclusion. |
| Allocator and admission | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:67-85` omits `iw_043` from `has_independence_wave_runtime_package_content_attestation_for_execution_id`; normal and scenario preflight therefore remain fail-closed even though the exact CHU pair is enumerated at lines 145-150 and 242-245. No admission change is authorized. |
| Map and setup | Vanilla CHU capital is state `256` (Cheboksary) in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/CHU - Chuvashia.txt`. IW-043 full-anchor proof requires states `249` and `256`, with compact proof at `249`, in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:895-912`; the latest map artifact reported `ok` for selected states `249`, `256`, and `676`. |
| Setup loop | `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1263-1368` loads the mapped force profile, applies the dynamic starting force, writes package ledgers, ideas, politics, focus framework, formable adapters, and opening event `chaosx.nr006.4301`. Before this audit, `independence_wave_iw043_cosmetic_identity_ready` had no setter, so `has_independence_wave_iw043_setup_surface` at `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:914-923` could never pass. |
| Forces and technology | The shared force allocator records a current-generation package receipt only after division creation, stockpiles, inherited technologies and slots, and air/navy transfer in `common/scripted_effects/006_independence_wave_force_effects.txt:871-887`; IW-043 composition and binding checks are in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:698-814`. No Technology Tree Viewer is exposed by the installed MCP, so technology-tree inspection remains unresolved. |
| Politics and leaders | `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:109-470` owns route politics, party names, institutional roles, idea lifecycle, and cleanup. `common/characters/006_independence_wave_iw043_iw058_characters.txt:11-49` defines four male civilian-large CHU institutional consumers and no advisors. |
| Portraits and flags | Opening Mirsaid Sultan-Galiev and the promoted Galimzhan Ibrahimov and Luka Semyonovich Spasov consumers are present at the existing large-portrait paths. The Bolgar civic-presidium row remains unresolved: Musa Dzhalil and Karim Tinchurin evidence are not rights/role-cleared and the existing DDS is not an admission-quality replacement. `interface/006_independence_wave_iw043_iw058_portraits.gfx:10-25` registers the four CHU large sprites; no advisor or female portrait is authorized. Cosmetic identities are `CHU_independence_wave_middle_volga_congressX`, `CHU_independence_wave_volga_bulgariaX`, and `CHU_independence_wave_volga_federationX` in `common/countries/006_independence_wave_formable_cosmetics.txt:46-60`. |
| Focus and decisions | `common/scripted_effects/006_independence_wave_iw043_iw058_focus_effects.txt` contains 48 package focus IDs and the shared focus framework; `common/decisions/006_independence_wave_iw043_iw058_decisions.txt:13-1113` contains the IW-043 category and package decision/mission contracts. The latest focus MCP artifact records 184 shared nodes and 14 blocking diagnostics outside the package node set, so shared-tree geometry remains an Event 006 completion risk. |
| AI and playability | `common/ai_strategy/006_independence_wave_iw043_iw058_ai_strategy.txt:10-112` has seven CHU profiles for foundation, reserve recovery, tracked crisis, federal, restoration, emergency, and civilian normalization, all bound to exact package/setup/route triggers with `abort_when_not_enabled = yes`. Static AI source is present; live AI observation remains parent-owned. |
| Formables and cleanup | FORM-12/13 settlement contracts and family `volga_ural_federation` are registered by setup and guarded by exact anchors, consent ledgers, route proof, identity, and cleanup in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:1137-1175` and `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1553-1828`. Vanilla Idel-Ural shortcuts remain guarded by the Event 006 compatibility override. |

## Safe patch applied

Changed file: `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1263-1290`.

The IW-043 setup effect now clears `independence_wave_iw043_cosmetic_identity_ready` at entry and sets it only after `independence_wave_force_mapping_loaded`, `independence_wave_force_mapping_package_id = iw_043`, `independence_wave_force_package_applied`, and `has_independence_wave_force_package_for_current_generation = yes` all pass.

Before: the existing setup-surface trigger required a flag that had no setter, so CHU could not reach the package identity, opening ideas, force receipts, focus framework, route registration, or opening event.

After: the intended setup surface can pass only after the existing mapping and current-generation force proof; absent force proof still fails closed.

The analogous IW-058 setter remains outside this CHU-scoped patch and should be handled by the ASY audit.

## Exact blockers and admission checklist

1. Keep `iw_043` out of central content attestation until the complete country package and every grounded route consumer pass a new independent audit.
2. Resolve Bolgar civic-presidium identity, source rights, route-role acceptance, durable manifest/hash evidence, approved male HOI4 repaint, DDS, and runtime sprite wiring for `CHU_independence_wave_bolgar_civic_presidium`.
3. Reconcile the current portrait source ledger and stale package prose before promotion; the dedicated Musa/Togan visual audit records visual PASS but separate `NEEDS_USER_REVIEW` rights/role gates.
4. Re-run CHU package, tag, allocator, focus, decision, formable, AI, and cleanup audits after the portrait tranche, then add `iw_043` to the central content-attestation authority only if every gate passes.
5. Preserve the CHU/IW-046 mutex, Event 005 behavior, states `249`/`256` ownership and control checks, FORM-12/13 consent and cleanup, and Soviet Collapse exclusions during any promotion.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, and 13 attested packages; the patch did not alter these counts or attestation membership.
- `python -B .tools/audit_chaosx_country_tags.py` passed with zero external country-definition or identity-surface collisions.
- A source-order check confirmed the CHU cosmetic-ready setter precedes `has_independence_wave_iw043_setup_surface = yes` and is guarded by all four force/mapping receipts; a separate check confirmed central content attestation still omits `iw_043`.
- No Hearts of Iron IV process, live execution, save/load, or player-owned runtime validation was run.

## Changed identifiers and remaining risk

Changed identifier: `independence_wave_iw043_cosmetic_identity_ready` only; no country tag, state, leader ID, party ID, focus ID, localisation key, formable ID, advisor, portrait family, or admission flag was added or promoted.

Remaining risks are the unresolved Bolgar portrait/rights/role gate, central content-attestation omission, shared focus geometry diagnostics, and unavailable Technology Tree Viewer evidence.
