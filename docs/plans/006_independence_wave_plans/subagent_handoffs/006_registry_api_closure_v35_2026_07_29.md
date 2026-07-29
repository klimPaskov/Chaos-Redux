# Event 006 country-registration and reusable API closure v35

Date: 2026-07-29

Scope: Event 006 country registration and reusable carrier API only, with the narrowed Event 006/Soviet Collapse tag-collision universe requested by the parent. CBB, CBD, Fallout, Random Events, and unrelated country systems were not remapped or modified, and `REV`, `ZIN`, and `ZZZ` were left untouched.

## Coverage result

| Registry surface | Result | Evidence |
| --- | --- | --- |
| Canonical package rows | 206/206 | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` |
| Event 006-owned registrations | 102 rows, all custom three-character tags end in `X` | `common/country_tags/006_independence_wave_countries.txt` and the canonical registry |
| Reused registered carriers | 91 rows, 89 unique tags | Canonical registry and `registered_reuse_tags` |
| Overlay-only identities | 13 rows, no standalone Event 006 tag | Registry `tag_resolution` plus route adapters and overlay carrier groups |
| Unique nonblank resolved carriers | 191 | Registry; only `CHU` and `BIA` are shared across package rows |
| Researched custom country definitions | 85 | 102 tag declarations minus 17 inert reservations |
| Inert unresolved reservations | 17, all explicit and fail-closed | `common/country_tags/006_independence_wave_countries.txt` points to `006_independence_wave_unresearched_reservations.txt` |
| Current-map-bound selectable rows | 138 | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` with `anchor_binding_mode != unbound` and excluding overlays |
| Current-map-unbound selectable rows | 55 | Same binding CSV with `anchor_binding_mode = unbound`; no substitute state was invented |
| SCN-008 ranked selectable rows | 138 | Existing `common/scripted_effects/006_independence_wave_scenario_effects.txt` ranked registry and allocator audit |
| Reservation groups | 111 | `common/script_constants/006_independence_wave_package_constants.txt` and binding ledgers |
| Regions | 14 | Canonical registry and existing Event 006 country-group arrays |

Country-group projections de-duplicate scopes, so the 138 bound rows expose 137 unique bound carrier tags and the 55 unbound rows expose 55 unique unbound tags. `BIA` intentionally appears in both status projections because IW-107 is bound while IW-096 is unbound; exact package identity remains package-ID/ledger data, not a carrier-tag inference.

## Changed files

- `common/script_constants/006_independence_wave_country_registry_constants.txt` adds `selectable_bound_tags`, `selectable_unbound_tags`, custom-owned bound/unbound splits, registered-reuse bound/unbound splits, six exact overlay carrier groups, and numeric registry counts.
- `common/collections/006_independence_wave_country_collections.txt` adds Event 006 status and overlay active views over the static country groups.
- `common/collections/chaosx_country_collections.txt` mirrors those status and overlay views as the public reusable `chaosx_country_independence_wave_*` API.
- `common/scripted_effects/006_independence_wave_country_registry_effects.md` documents the status API, dormant/fail-closed semantics, overlay route boundary, and the intentional `BIA` row-sharing caveat.
- No country tag, country definition, country history, allocator, package gameplay, localisation, focus, decision, idea, asset, AI, map, or Soviet Collapse file required a patch after the audit.

## File-surface checklist

| Surface | Status | Finding |
| --- | --- | --- |
| Tag file registration | PASS | All 102 custom Event 006 tags from the registry are declared exactly once and all end in `X`; 91 reuse rows retain registered tags; 13 overlays reserve no standalone tag. |
| Country definition registration | PASS / fail-closed | 85 researched tags point to individual `common/countries/006_independence_wave_*.txt` definitions; 17 unresolved tags point to the inert reservation file. |
| Formable/cosmetic/route identifiers | PASS | All 17 Event 006 formable/cosmetic identifiers in `common/countries/006_independence_wave_formable_cosmetics.txt` end in `X`; vanilla overlay cosmetics remain carrier identities and are not remapped. |
| Collections | PASS | Static arrays and active collections now distinguish bound, unbound, custom-owned, reuse, and overlay carriers. |
| Package IDs | PASS | `common/script_constants/006_independence_wave_package_constants.txt` covers IW-001 through IW-206; exact row metadata remains in the canonical registry and binding CSVs. |
| Region package dispatch | PASS for admitted publishers / intentional fail-closed rows | Existing region loaders and reserve/plan dispatchers cover the 149 publisher rows; the 55 unbound selectable rows and the two overlay rows without a standalone publisher remain intentional. |
| Registry lifecycle effects | PASS | Existing origin record/clear wrappers remain narrow and do not cross-contaminate Event 012. |
| Country history and identity | PASS for registered surfaces | No stale Event 006-owned tag reference was found; no identity remap was required. Full package history/content admission remains outside this closure. |

## Map and state setup

The current-map binding authority covers every package row with explicit binding mode, readiness, reservation-group, host-survival, rebind, and missing-state semantics. Anchor, compact/extended, owner, and capital fields are populated for bound rows and intentionally blank for unbound or route-overlay rows. `missing_current_state_ids` is empty for all 206 rows. The accepted selectable split is 138 bound and 55 unbound after removing all 13 overlays. The 55 unbound rows remain explicit `unbound`/fail-closed registrations because no unique current-map binding was accepted; no nearby-state fallback was added. Overlay rows retain route-specific carrier/anchor contracts and do not enter the release selector.

## Politics, leaders, portraits, flags, advisors, and parties

No country-package politics, leader, portrait, flag, advisor, or party content was changed. Existing country-definition and history identity surfaces are registration-safe for the 102 custom tags, while package-level leader/portrait/flag/party admission remains a separate content audit and must not be inferred from tag registration.

## Focus, decision, idea, and asset surfaces

No focus tree, decision, mission, idea, icon, flag, portrait, or other asset was changed. The new overlay carrier groups point to the existing route-specific triggers, whose cosmetic/formable/autonomy/ideology gates remain authoritative. Overlay registration does not claim complete route gameplay or asset completion.

## Starting military, technology, industry, supply, and production

No starting setup or technology surface was changed. These systems are package-content responsibilities and remain outside this registration/API closure.

## AI and playability

No AI strategy or playability balance was changed. Active collections are intentionally empty for dormant tags, and callers must still apply origin, content-attestation, living-tag, host-survival, anchor, and reservation gates before loading a package.

## Validation

- `python .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked rows, 12 attested packages across 11 compatible groups, and the expected 6/8/10/14/20 automatic ladder.
- `python .tools/audit_chaosx_country_tags.py --surface-scan` passed with 136 protected Event 006/Soviet tags, zero external country-definition collisions, zero external identity-surface collisions, and one intentionally skipped Random Events root.
- A static registry/API cross-check passed: 206 registry/binding rows, 193 selectable rows, 138 bound rows, 55 unbound rows, 13 overlays, exact status-array projections, 102 custom tags, 85 researched definitions, 17 inert reservations, and 17 X-ending formable/cosmetic identifiers.
- Live/in-game validation was intentionally skipped because the parent decision states that source/static proof is sufficient and live evidence is not required for this closure.

## Remaining registration blockers

- The 55 selectable unbound rows need a future accepted current-map binding before they can enter a release publisher; the API preserves them as fail-closed and does not invent geography.
- Seventeen custom tags remain inert reservations until their named identity research is accepted; registration is present, but package admission must stay blocked.
- Thirteen overlay rows remain route-only and require their existing carrier-specific cosmetic/formable/autonomy/ideology hooks; they must never be promoted to standalone Event 006 countries.
- Reused-tag compatibility adapters and full package-content admission remain parent-owned content work, not registration defects.

No fallback country, nearby-state substitution, tag remap, or unrelated-scope edit was made. No commit was created, per the parent instruction.
