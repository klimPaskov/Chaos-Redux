# IW-043 / IW-058 country-package final audit

Date: 2026-07-18
Scope: IW-043 Volga Bulgaria (carrier `CHU`) and IW-058 Assyria (carrier `ASY`), including FORM-12/13/18 adapters, vanilla identity compatibility, country assets, setup/cleanup, AI, and the exact achievement predicates.

## Documentation reconciliation note (2026-07-18)

This final audit remains the authority for zero collisions, additive carrier
identity, no advisor assets, and reviewed visual evidence. Its earlier caveat
that party keys were not yet wired to centralized political effects is
superseded by the current package effects: setup and signature/shared-
government routes now apply the centralized politics, popularity, election,
final-party-name, and institutional-leader surface with matching cleanup
receipts. The exact CHU/ASY FORM-12/13/18 attestation and sole proof-writer
status is also current in the source-of-truth specs; retain this audit's
static limitations and do not infer whole-Event 006 completion.

## Result

**Final verdict: pass after one narrow leader-precedence fix.** The parent resolution closes the prior political-identity blocker. IW-043 and IW-058 now receive exact-package political surfaces at setup, after a shared government route locks, and after a signature route is selected. The re-audit found that a prior shared `marxism`/`oligarchism` role could make the broad `has_country_leader` guard suppress a later signature-role addition on the same character. The three affected signature leaders now idempotently receive and explicitly promote their exact ideology role: the IW-043 Bolgar Civic Presidium (`conservatism`), the IW-058 Concordat Council (`conservatism`), and the IW-058 Civic National Assembly (`centrism`). The packages remain additive overlays on vanilla `CHU` and `ASY`; they do not define a replacement country file, history file, focus tree, or vanilla character. The static package and installed-tag audit found no exact tag collision, member absorption, subject/core shortcut, or prohibited IW advisor asset.

No fallback, placeholder, route omission, or other simplification was introduced by the politics resolution or this narrow fix.

## Coverage checklist

- **Identity/history:** Vanilla `CHU` and `ASY` are reused. The mod has no `common/countries/CHU.txt`, `common/countries/ASY.txt`, or corresponding country-history overwrite. Vanilla references inspected: `CHU` capital state 256 (Cheboksary), `ASY` capital state 676 (Mosul), their vanilla graphical cultures/colors, starting technologies, and vanilla characters. `common/countries/006_independence_wave_formable_cosmetics.txt` contains only cosmetic color/UI entries for long `X` identities.
- **Tag registry:** `common/country_tags/006_independence_wave_countries.txt` reserves the event's `X` tags; it has no `CHU =` or `ASY =` definition. Installed audit (`.tools/audit_hoi4_country_tags.py`, game + workshop + local-mod roots) reported 206 package definitions, 102 Event-006 reserved tags, and zero collisions. The audit now inventories all split Event 006 package-trigger files, recognizes the exact IW-043 wrapper, and reports IW-043 as attested while IW-046 remains fail-closed.
- **Setup/map:** `can_initialize_independence_wave_iw043_package` and `can_initialize_independence_wave_iw058_package` require exact original tag, Event-006 liberation origin, package/setup mapping, current generation/force/cosmetic/institutional surfaces, host linkage, and controlled anchors state 249 (`CHU`) / state 676 (`ASY`). No unbounded world-state scan is used.
- **Forces/technology/industry:** Dynamic starting force is inherited/derived from current carrier and bounded by the force constants; no host land-unit transfer. Opening templates are `Middle Volga River Guard` (IW-043) and `Assyrian Levies Detachment` (IW-058). Technology/research-slot inheritance and factory/supply/stockpile floors are handled by the shared dynamic force effects. Division package and generation provenance is written on every created division, and binding rechecks the exact package/generation/template signature before committing.
- **Ideas/leaders:** Three opening ideas per package are installed, with route and normalization lifecycle ideas. Eight institutional characters are recruited dynamically and assigned route-specific leader roles; they are all explicitly male and use large portraits only. No advisor, high-command, field-marshal, corps-commander, theorist, dossier-card, or small portrait is defined in this package.
- **Political surface:** `independence_wave_apply_iw043_political_surface` and `independence_wave_apply_iw058_political_surface` are gated by the exact package triggers. Precedence is emergency, package-signature route, shared popular/traditional/patron/constitutional route, then opening state. The shared dispatch runs only after `independence_wave_select_government_route` writes the shared route flag. All seven popularity rows contain exactly the four supported ideology groups and sum to 100: opening `55/10/30/5`, constitutional `70/10/15/5`, popular `20/65/10/5`, restoration `60/5/30/5`, traditional `30/5/60/5`, emergency `15/5/75/5`, and patron `20/5/70/5` (democratic/communism/neutrality/fascism). Setup and final validation both require the exact package political-surface receipt.
- **AI/playability:** Sixteen exact package/route/crisis/normalization AI strategy profiles cover CHU and ASY foundation, reserve recovery, tracked crisis, route choices, emergency/guardianship, and civilian normalization. The strategies are origin/package-gated, abort when disabled, and avoid arbitrary target creation/world scans.
- **Diplomacy/host relations/regional ambition:** Setup registers the four bounded former-host lanes (negotiation, guarded frontier, association, and reclamation), the package ambition family, and the Event-006 league route. Triggers require a live former host, reject self-host and invalid Soviet-collapse states, and gate host-conflict/reclamation receipts through Event-006 linkage. No package adapter creates subjects, ends a member's Event-006 origin, transfers state, adds cores/claims, or rewrites league membership.
- **Formables:** FORM-12/13 candidates are the exact `TAT`/IW-044, `BSK`/IW-045, `MEL`/IW-047, `UDM`/IW-048, and `KOM`/IW-050 member set; FORM-18 candidates are exact `KUR`/IW-060 and `CJX`/IW-062. Candidate triggers reject subjects, wars, capitulation, incompatible package/formable flags, stale generation, Soviet/Event-005 origins, and duplicate anchors. Required member/consent/anchor counts are 3/3/3 for FORM-12/13 and 2/2/2 for FORM-18. The adapters stage current-generation consent receipts and identity/integration receipts only; they do not absorb members or mutate member sovereignty.
- **FORM-18 defensive settlement:** `independence_wave_achievement_resolve_country_peace` writes the defensive-war, sovereign-anchor, and corridor-control receipts only after tracked host-reclamation conflict linkage, defensive war recording, state 676 ownership/control, corridor fortification, and stable corridor security. Offensive pretext is explicitly excluded by the FORM-18 method policy.
- **Achievements:** Volga Bulgaria proof requires exact IW-043/CHU package state, state 249 and 256 control, and mutually exclusive federal/restoration proof/cosmetic routes. Assyria survival proof requires exact IW-058/ASY package state, state 676 protection, settlement/host-conflict survival, civilian-law levies, no guardianship, and exactly one church/civic route. All proof writers and resets are generation/package/sovereignty gated.
- **Cosmetics/flags/localisation:** Runtime flags exist for the ten IW-043/IW-058 country/formable cosmetic identities, each with normal/medium/small ladder. Character, trait, idea, route, cosmetic, focus, and political-party labels are covered in `localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml`. The political effects reference 32 party-name tokens; all 32 resolve exactly once and the localisation file remains UTF-8 with BOM.
- **Cleanup:** CHU and ASY cleanup removes package decisions/ideas/leader roles/cosmetic tags, clears formable ledgers and receipt flags, clears exact package/generation division provenance, clears focus runtime, and restores `generic_focus` only when the current tree is the Event-006 tree. The shared popular/traditional/patron additions have matching `marxism`/`oligarchism` role removals, and all six one-time role receipts plus both political-surface receipts are cleared. It intentionally does not disband/refund units or alter member state/core/subject surfaces.

## Asset constraints

The generated visual manifest (`docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/manifest.md`) documents eight all-male institutional portraits, ten flag ladders, and two reports. The static icon manifest documents zero advisor/adviser, dossier, commander, high-command, theorist, or small assets. No IW Independence Wave advisor icons, portraits, sprites, dossiers, or advisor assets were found. Separate 65x67 commander smalls from other packages remain outside this package. Protected `BAY` and `RHI` portrait hashes were not changed:

- `portrait_BAY_rupprecht_of_bavaria.dds`: `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`
- `portrait_RHI_josef_friedrich_matthes.dds`: `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`

## Remaining risks / stale documentation

1. Some gameplay-adjacent markdown and historical handoffs still frame
   FORM-12/13/18 adapter attestation as optional or purely fail-closed. The
   current setup effects do set `independence_wave_form12_adapter_attested`,
   `independence_wave_form13_adapter_attested`, and
   `independence_wave_form18_adapter_attested` after the full setup gates; the
   keyed adapters themselves still retain strict family/route/consent/anchor
   commit gates. The documentation handoff records the exact-doc promotion;
   the common scripted-effects overview remains outside this audit's owner
   boundary.
2. No live game/MCP render was available for this audit (the installed MCP workspace was not registered/usable); confidence comes from source inspection, vanilla/documentation comparison, asset manifests, and the installed-tag audit.

## Parent resolution files verified

- `common/script_constants/006_independence_wave_iw043_iw058_constants.txt`
- `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml`

## Files changed by this re-audit

- `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw043_iw058_country_package_final_audit_2026_07_18.md`

No localisation, history, character, portrait, or advisor-asset file was changed by this re-audit.

## Files inspected

- `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/script_constants/006_independence_wave_iw043_iw058_constants.txt`
- `common/scripted_effects/006_independence_wave_force_effects.txt`
- `common/scripted_effects/006_independence_wave_achievement_effects.txt`
- `common/scripted_triggers/006_independence_wave_achievement_triggers.txt`
- `common/characters/006_independence_wave_iw043_iw058_characters.txt`
- `common/country_leader/006_independence_wave_iw043_iw058_traits.txt`
- `interface/006_independence_wave_iw043_iw058_portraits.gfx`
- `common/country_tags/006_independence_wave_countries.txt`
- `common/countries/006_independence_wave_formable_cosmetics.txt`
- `common/decisions/zz_006_independence_wave_vanilla_formable_compatibility_decisions.txt`
- `common/scripted_triggers/006_independence_wave_vanilla_formable_compatibility_triggers.txt`
- `common/ai_strategy/006_independence_wave_iw043_iw058_ai_strategy.txt`
- `localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml`
- `docs/assets/006_independence_wave/iw043_iw058_generated_visuals_2026_07_18/manifest.md`
- `docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/manifest.md`
