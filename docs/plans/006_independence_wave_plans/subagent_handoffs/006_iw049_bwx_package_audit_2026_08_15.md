# IW-049 BWX package gate audit — 2026-08-15

## Disposition

IW-049 BWX remains HOLD / fail-closed. This audit records the bounded current-source, map, identity, asset, and probability evidence; it does not promote the package, add a runtime adapter, widen attestation or preflight lists, change Join order, or assign a replacement state.

## Current contract

The authoritative candidate row is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:50`. It identifies BWX as the Erzya-Moksha Federal Republic, uses `RG-MORDOVIA`, and explicitly requires a Mordovia-or-Penza current-map split before selection. The installed-map binding remains `disabled_no_unique_current_state` / `unbound_current_map` in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:50`.

The package has only a country shell and neutral history shell (`common/countries/006_independence_wave_BWX.txt`, `history/countries/BWX - Erzya-Moksha Federal Republic.txt`). No complete Event 006 BWX constants, scripted setup/final/cleanup, ideas, decisions, focus callbacks, AI, roster, or package-local localisation family is present. The existing shell comments intentionally defer those runtime assignments.

## Map evidence

The mandatory bounded map inspection of installed state 255 (Penza reference only, never a BWX binding) returned `MAP_INSPECTED` with artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/433ebece4fb3a673b7452f284243766ba5e53274634d1beb37e7e214965bfc73/7aa0a204cf25a03ad514d5057247de05814279e1a70b0eb39f32a7aa6a031a7c/map-inspect.1144978a8f1bafcd.json`

Selected state membership, geometry, and network checks passed. Aggregate map validation remains false because the workspace contains unrelated building-position and floating-harbor diagnostics (`MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`). State 255 is not an accepted BWX anchor; the registry requires a fresh Mordovia/Penza split and host-survival witness.

## Identity and portrait evidence

The portrait research handoff is `006_iw049_bwx_portrait_research_2026_08_15.md`. The 1936 institutional consumer is the Mordovian ASSR Council of People’s Commissars, chaired by Andrey Yakovlevich Kozikov. No defensible Kozikov portrait with attributable source, date, and reusable rights was found. The only archived identity-adjacent source is the authentic 1934–37 Mordovian ASSR emblem (900×910 JPEG, SHA-256 `AA053C843CF27109B4752CFC02C701559BA8C815C7F0A7E977A627DE63229349`) under the flat portrait archive’s `processed/` evidence area; it is not a leader portrait and is not runtime wiring.

No 156×210 portrait, DDS, GFX, character definition, generated face, ImageGen result, or RunPod result was created for BWX.

## Flag and symbol evidence

The symbol handoff is `006_iw049_bwx_symbol_research_2026_08_15.md`. The existing BWX normal/medium/small ladder is technically complete, but its ImageGen provenance cites generic Erzya/Moksha references without accepted provider rights/date or exact historical geometry. The strongest period lead, the 1934 Mordovian ASSR flag, is explicitly Soviet and is not a neutral 1936 Erzya–Moksha federal flag. Textile/embroidery references support only a future clearly labelled fictional civic synthesis. No new ImageGen, TGA, DDS, GFX, or vanilla flag edit was made.

## Probability evidence

The mandatory `hoi4.probability_inspect` request for `common/ai_strategy/006_independence_wave_BWX.txt` returned `PROBABILITY_SOURCE_NOT_FOUND` with no artifact or files scanned. The AI source does not exist, so no BWX weighted-logic, mission-score, AI-strategy, balance, or comparison claim is permitted.

## Authority boundary and next gate

Event 006 remains at 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, and 161 unattested selectable rows. BWX remains outside central adapter, attestation, normal/scenario preflight, and deterministic Join surfaces. Safe next work is a source-backed map split/host witness, named institutional identity decision, and independently reviewed portrait/flag provenance packet. Until those gates pass, do not substitute state 255 or any other existing state, copy a generic portrait, or promote the current generated flag ladder as historically attested.

No gameplay, map, central registry, attestation, preflight, scenario, Join, localisation, workbook, or runtime asset files were changed by this audit.
