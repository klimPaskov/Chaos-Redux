# Event 006 Starter Package Viability Audit

Scope: read-only country-package audit for Event 006 Independence Wave starter package candidates. No gameplay, localisation, asset, or spreadsheet files were edited.

## Viability Table

| Candidate | Tag status | Likely start states / groups | Viability | Required blockers before implementation |
| --- | --- | --- | --- | --- |
| Old Great Bulgaria / Volga Bulgaria | `OGB` exists in repo: `common/country_tags/chaosx_countries.txt`; country/history/loc/flags/portrait exist as Event 005 content. | Current Event 006 partial seed targets `249` Kazan and `256` Chuvashia. Event 005 uses the same states. Plausible later Volga/Kama proof can include `399` Udmurtia, `400` Kirov, `401` Balakovo, `829` Engels-Marxstadt, `652` Orenburg only after explicit state proof. | Conditional. This is the best shared-tag separation test, but not safe as-is. | `common/scripted_effects/006_independence_wave_effects.txt` calls missing trigger `can_independence_wave_seed_volga_bulgaria_package` and missing idea `independence_wave_volga_old_state_memory`. Every OGB focus/decision/idea/AI/cosmetic path must check `chaosx_release_origin_independence_wave`; do not call Event 005 focus trees, decisions, formables, event logs, or helper state. |
| Assyria | `ASY` exists in vanilla; Chaos Redux does not replace `common/country_tags`, so vanilla tag/history/loc/flags remain available. | `676` Mosul: owner `IRQ`, cores `IRQ`, `KUR`, `ASY`, VP Mosul. Iraq keeps Baghdad/core territory, so host survival is straightforward unless campaign state is already reduced. | Safe starter after OGB blockers, using vanilla tag and assets. | Needs Event 006 package data, origin-gated overlay, focus/decision/AI/localisation hooks, and source-aware state proof. Do not fake it through an unrelated tag. |
| Mapuche / Araucania | No standalone release tag found in repo or vanilla. Existing support is cosmetic only: `CHL_mapuche_state` and `kingdom_of_araucania_and_patagonia` in `common/countries/cosmetic.txt` plus vanilla cosmetic loc/flags. | Plausible states: `950` Araucania, `949` Aysen, possibly `512` Rio Negro for later claims. | Blocked under no-fallback-tag rule. | Needs an explicit real tag decision from the parent. Using `CHL` plus a cosmetic tag would not create an independent Mapuche package and would collide with Chile. |
| Buganda | No distinct `BUG` tag found. Vanilla `UGA` exists and has `UGA_neutrality` localisation as "Kingdom of Buganda". | `548` Uganda: owner `ENG`, core `UGA`, rural state, Lake Victoria-adjacent. England host survival is safe in normal starts. | Safe if the package is allowed to use `UGA` as the Buganda route carrier. | Parent must accept `UGA` rather than a separate Buganda tag. Needs Event 006 route/cosmetic handling, leader/source review, and no invented royal portrait or unsourced symbol. |
| Free City package | `DNZ` exists in vanilla; no Event 005 contamination found. | `85` Danzig: owner `POL`, cores `POL`, `DNZ`, `KSH`, city/coastal, VP 10, naval base and dockyards. | Safest structural city package. | Needs Event 006 free-city package data, origin setup, city/free-port route hooks, and host-survival check against Poland. |
| Railway package alternate | `PRA` exists in repo as Event 005 Pale Railway Authority. | Event 005 uses `570` Novosibirsk and `571` Omsk. | Not first. Viable only after stronger Event 005 separation work. | Current `PRA` package is Event 005-branded. Its history uses an institutional board portrait with random single-person male names, which is unsafe for a council/board portrait package unless Event 006 overrides it with an institutional leader. Must not load Event 005 PRA focus/decisions/ideas. |

## Safest Next Implementation Order

1. Fix and complete `OGB` only as an origin-gated Event 006 package, because the worktree already contains partial OGB seeding and this validates the Event 005 separation rule.
2. Add `ASY` Assyria using vanilla tag `ASY` and state `676` Mosul; it has a real tag, state core, history, loc, parties, and flags.
3. Add `DNZ` as the first city/free-port structural package; it is cleaner than `PRA` because it has no Event 005 baggage.
4. Add `UGA` as Buganda only if the parent accepts the vanilla Uganda tag as the package carrier.
5. Keep Mapuche blocked until a real tag is created or explicitly chosen. Do not use a fallback tag.
6. Keep `PRA` queued until the parent wants a railway package and is ready to override the Event 005 leader/history/focus/decision surfaces under Event 006 origin.

## Country Package Coverage Checklist

| Surface | OGB | ASY | Mapuche | Buganda / UGA | DNZ | PRA |
| --- | --- | --- | --- | --- | --- | --- |
| Real tag | Yes, repo | Yes, vanilla | No | Yes, vanilla `UGA` | Yes, vanilla | Yes, repo |
| Country/history file | Yes | Yes | No | Yes | Yes | Yes |
| Valid start state | Yes, partial | Yes | State exists, no tag | Yes | Yes | Yes |
| Base localisation | Yes | Yes | Cosmetic only | Yes | Yes | Yes |
| Flags | Yes, repo | Yes, vanilla | Cosmetic only | Yes, vanilla | Yes, vanilla | Yes, repo |
| Leader/portrait safe | Council portrait acceptable | Vanilla | Blocked | Needs source review | Vanilla | Blocked for Event 006 unless institutionalized |
| Event 006 origin-gated package | Partial and broken | Missing | Missing | Missing | Missing | Missing |
| Event 005 separation risk | High | Low | Low | Low | Low | High |

## File Surface Checklist

- Event 006 specs/plans: `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`, `006_independence_wave_spec.md`, `006_independence_wave_decisions_ai.md`, `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`.
- Current Event 006 implementation: `events/006_independence_wave.txt`, `common/scripted_effects/006_independence_wave_effects.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, `common/script_constants/006_independence_wave_constants.txt`, `common/national_focus/006_independence_wave_focus.txt`, `common/decisions/006_independence_wave_decisions.txt`.
- Shared Event 005 surfaces: `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/scripted_triggers/005_soviet_collapse_triggers.txt`, `common/decisions/005_soviet_collapse_decisions.txt`, `common/national_focus/005_soviet_collapse_factory_successors.txt`, `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`.
- Tag/state evidence: `common/country_tags/chaosx_countries.txt`, `history/countries/OGB - Old Great Bulgaria.txt`, `history/countries/PRA - Pale Railway Authority.txt`, vanilla `common/country_tags/00_countries.txt`, vanilla `history/states/676-Mosul.txt`, `548-Uganda.txt`, `85-Danzig.txt`, `950 - Araucania.txt`, `570-TS 12.txt`, `571-TS 13.txt`.

## Missing Or Stale Surfaces

- `OGB`: Event 006 has partial seed/package logic, but the seed trigger and Volga idea are missing.
- `ASY`, `UGA`, `DNZ`: usable vanilla tags/states exist, but no Event 006 package registry entries, route overlays, decisions, AI, or package docs are implemented.
- `Mapuche`: only cosmetic Chile surfaces exist; no independent tag.
- `PRA`: all strong railway surfaces are Event 005-branded and cannot be reused directly.

## Validation Evidence

Commands run:

```bash
rg -n "\b(OGB|Assyria|Assyrian|Mapuche|Buganda|PRA|DNZ|UGA|ASY)\b" common history localisation docs events
rg -n "\b(ASY|UGA|DNZ)\b" ~/projects/'Hearts of Iron IV'/common/country_tags ~/projects/'Hearts of Iron IV'/history/states ~/projects/'Hearts of Iron IV'/localisation/english
rg -n "can_independence_wave_seed_volga_bulgaria_package|independence_wave_volga_old_state_memory" common docs localisation events
find gfx/flags -maxdepth 3 -type f \( -name 'OGB*' -o -name 'PRA*' -o -name 'SOG*' \)
find ~/projects/'Hearts of Iron IV'/gfx/flags -maxdepth 3 -type f \( -name 'ASY*' -o -name 'UGA*' -o -name 'DNZ*' -o -name 'CHL*' \)
```

Skipped validation: no live HOI4 load or parser validation was run. No gameplay files were changed, and no commit was made.
