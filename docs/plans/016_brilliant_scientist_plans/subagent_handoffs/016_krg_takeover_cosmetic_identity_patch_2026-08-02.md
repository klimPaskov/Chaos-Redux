# Event 016 KRG takeover cosmetic identity patch

Date: 2026-08-02

Status: bounded source patch complete; parent review and live takeover validation remain outstanding.

## Scope and recommendation

This follow-up resolves the transformed-host cosmetic identity gap without changing the host's regular country tag, territory, government, focus tree, AI plans, map data, or models.

The offline Cosmetic tag modding reference states that a country may have at most one cosmetic tag, `set_cosmetic_tag` replaces the current cosmetic tag, and `drop_cosmetic_tag` removes it in country scope.

The Event 016 takeover helper intentionally retains the carrier's regular tag and map. Applying the registered `KRG_SCIENTIFIC_REPUBLIC` identity immediately after the existing `drop_cosmetic_tag = yes` is engine-safe for that contract because it changes presentation only and does not create, release, annex, or transfer a country.

## Changed file and identifier

- `common/scripted_effects/016_brilliant_scientist_country_effects.txt:1047-1048`
  - `brilliant_scientist_transform_host_into_kruger_state` now calls `set_cosmetic_tag = KRG_SCIENTIFIC_REPUBLIC` immediately after `drop_cosmetic_tag = yes`.

No other gameplay file, country tag, state, focus, decision, event, character, portrait, flag, technology, equipment, or model was changed by this patch.

## Before and after behavior

Before this patch, a transformed host retained its regular tag and map but dropped any existing cosmetic tag without receiving a Kruger presentation identity, so the host could continue to display its former country name, adjective, color, or flag until a later route effect selected a route identity.

After this patch, the transformed host still retains its regular tag, state ownership, map, diplomacy, and carrier history, but receives the registered `KRG_SCIENTIFIC_REPUBLIC` cosmetic identity as the takeover baseline.

The identity is defined in `common/countries/016_brilliant_scientist_cosmetics.txt`, has map colors, has normal/medium/small flag assets at `gfx/flags/`, and has English generic, `_DEF`, and `_ADJ` localisation keys at `localisation/english/016_brilliant_scientist_country_l_english.yml:44-49`.

The existing route effects later replace this baseline with `KRG_SCIENTIFIC_REPUBLIC`, `KRG_REPLICATED_STATE`, `KRG_MACHINE_STATE`, `KRG_TEMPORAL_CONTINUUM`, `KRG_XENOBIOLOGICAL_ASCENDANCY`, or `KRG_PROJECT_SYNTHESIS` through their existing `set_cosmetic_tag` calls.

## Why the host takeover remains intact

Cosmetic tags do not change a country's regular tag, original tag, state ownership, controller, cores, claims, capital, diplomacy, or focus-tree scope.

The takeover helper continues to set `brilliant_scientist_host_transformed_into_kruger_state`, `brilliant_scientist_kruger_state`, `brilliant_scientist_formation_takeover`, the global active flag, the sovereign government, the host-derived military package, the focus tree, and the carrier event target exactly as before.

This patch does not restore the previously removed `set_cosmetic_tag = KRG` call. That earlier form used an unregistered base cosmetic identity and was intentionally replaced with `drop_cosmetic_tag = yes` in the final correction tranche. `KRG_SCIENTIFIC_REPUBLIC` is a registered cosmetic identity with an asset and localisation surface.

Vanilla precedents in `common/decisions/SWE.txt`, `common/decisions/SIA.txt`, and `common/decisions/HUN.txt` use `drop_cosmetic_tag` followed by `set_cosmetic_tag` in the same effect chain, including on countries that retain their regular tag.

## Semantic and presentation risks

The baseline identity is named `KRG_SCIENTIFIC_REPUBLIC`, although the takeover bootstrap government is neutrality and the Human Scientific Republic route later sets democratic politics. This is an intentional bounded use of an existing registered identity to provide a public Kruger name before route selection, but the parent may later prefer a neutral base cosmetic tag if the design requires the takeover label to avoid route semantics.

The cosmetics file comment currently says these identities are selected only by route-completion effects. This patch makes `KRG_SCIENTIFIC_REPUBLIC` an interim takeover identity as well; the comment is therefore stale but was left unchanged because the parent restricted this patch to the takeover effect and handoff.

The offline cosmetic-tag reference warns that a generic cosmetic flag does not override an ideology-specific base-country flag. Event 016 currently supplies generic `KRG_SCIENTIFIC_REPUBLIC` flags only, so a transformed host with an ideology-specific regular flag may continue to display that regular flag until a future asset pass adds the needed ideology-specific cosmetic flag triplets. This does not affect regular-tag takeover safety or map-color/name assignment.

## Validation performed

- Read `paradox_wiki/Cosmetic tag modding - Hearts of Iron 4 Wiki.md` and the vanilla `effects_documentation.md` entries for `set_cosmetic_tag` and `drop_cosmetic_tag` before editing.
- Confirmed `KRG_SCIENTIFIC_REPUBLIC` is defined in `common/countries/016_brilliant_scientist_cosmetics.txt`.
- Confirmed `KRG_SCIENTIFIC_REPUBLIC.tga` exists in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
- Confirmed generic, `_DEF`, `_ADJ`, and democratic localisation keys exist in the UTF-8-BOM Event 016 English localisation file.
- Confirmed the source ordering is `drop_cosmetic_tag = yes` followed immediately by `set_cosmetic_tag = KRG_SCIENTIFIC_REPUBLIC` inside `brilliant_scientist_transform_host_into_kruger_state`.
- Confirmed repository scans contain no Event 016 trigger or decision that uses `KRG_SCIENTIFIC_REPUBLIC` as a route gate, so the interim identity cannot silently unlock a separate route.
- `git diff --check -- common/scripted_effects/016_brilliant_scientist_country_effects.txt` returned no whitespace errors.

## Skipped meaningful validation

- No live transformed-host takeover or route scenario was run because agents must not launch Hearts of Iron IV; the parent/user owns live formation and map presentation checks.
- No map rewrite or apply was attempted because the patch changes no state, province, ownership, controller, rail, port, supply, or capital data.
- No Technology Tree Viewer validation was run because the installed package exposes no Technology Tree Viewer.
- No new asset was generated and no model pipeline was invoked because this is a country cosmetic wiring change.

No fallback asset or substitute country tag was introduced, and no commit was created by this subagent.
