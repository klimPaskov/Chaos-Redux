# Event 010 Death country package audit and small patch handoff

Date: 2026-06-15
Agent role: Chaos Redux country package subagent

Supersession note: this handoff predates the parent final asset pass and final route-disposition cleanup. Its missing route-achievement DDS and stale-manifest findings are resolved; current source-of-truth status lives in `docs/assets/010_death/generated_art_manifest.md`, `docs/events/010_death.md`, and the Event 010 specs.

## Scope audited

- `DTH` tag registration and conflict safety.
- Death country file, history file, Zol character, leader portrait reference, black map color, no starting units, no starting state ownership.
- Dynamic origin and spread setup in `common/scripted_effects/010_death_effects.txt` and `common/scripted_triggers/010_death_triggers.txt`.
- Shared special-chaos and actual-nonhuman classification.
- Herald of Zol and Black Apostolate cosmetic identities, flags, ideas, and cleanup.
- Death identity achievements and active stale Spirit of War/Peace references in the scoped files.
- Event 010 generated art manifest.

## Files changed

- `common/countries/cosmetic.txt`
- `common/scripted_effects/010_death_effects.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.md`
- `docs/plans/010_death_plans/subagent_handoffs/country_package_audit_death_routes_handoff.md`

`common/scripted_effects/010_death_effects.txt` was already dirty before this pass. The only local change made there by this audit is the defeat cleanup adjustment listed below.

## Changed identifiers

- Cosmetic tags added:
  - `death_herald_of_zol`
  - `death_black_apostolate`
- Defeat cleanup changed:
  - `death_finish_defeat`
  - `death_first_silence`
  - `death_public_death`
  - `death_world_end_death`
  - `death_black_census`
- Classification documentation updated:
  - `is_special_chaos_country`
  - `is_actual_nonhuman_country`

## Before and after behavior

- Before: `death_make_herald_of_zol` and `death_form_black_apostolate_effect` called `set_cosmetic_tag = death_herald_of_zol` / `death_black_apostolate`, and flags/localisation existed, but the cosmetic tags were not defined in `common/countries/cosmetic.txt`.
- After: both cosmetic tags are defined with dark map/UI colors matching their route identity and existing flag files.

- Before: shared trigger script already treated `DTH` as special chaos and actual nonhuman, but `chaosx_dynamic_triggers.md` did not document that coverage.
- After: the documentation lists `DTH`, original `DTH`, and the Death country marker under both shared classifications.

- Before: `death_finish_defeat` removed `death_public_death` and `death_world_end_death` but added `death_black_census`, leaving stale active Death lifecycle identity after defeat.
- After: defeat cleanup removes `death_first_silence`, `death_public_death`, `death_world_end_death`, and `death_black_census` from `DTH`.

## Country package coverage checklist

- Tag registration: `DTH = "countries/Death.txt"` exists in `common/country_tags/chaosx_countries.txt`.
- Tag conflict safety: `DTH` was found only in Chaos Redux tag files, not in vanilla `common/country_tags`.
- Country definition: `common/countries/Death.txt` uses `color = rgb { 0 0 0 }`.
- History setup: `history/countries/DTH - Death.txt` recruits `DTH_zol`, sets neutrality/no elections, 100 neutrality popularity, no convoys, zero research slots, and starts with `death_country_without_breath` plus `death_first_silence`.
- Starting units: `history/units/DTH_1936.txt` defines templates only; no starting `units = { ... }` blocks were found.
- State ownership: no `DTH` owner/controller/core entries were found in `history/states`; Death origin is dynamic.
- Leader: `common/characters/DTH.txt` defines `DTH_zol` with `GFX_portrait_DTH_zol` and `death_god_of_death`.
- Portrait: manifest and `interface/chaosx_characters.gfx` point to `gfx/leaders/010_death/portrait_DTH_zol.dds`, verified as 156x210 DDS.
- Flags: base `DTH` and route cosmetic flags exist in normal/medium/small sizes.
- Shared classification: script covers `DTH` as special chaos and actual nonhuman; markdown now matches.

## File surface checklist

- Country tags: covered.
- Common country file: covered.
- Country history: covered.
- State history: no static DTH state assignment found; dynamic origin applies state transfer/core/controller.
- Ideas: covered for Death lifecycle, Black Oath, and Black Apostolate route ideas.
- Scripted effects/triggers: covered for origin, setup, reveal, route cosmetics, and defeat cleanup.
- Achievements: covered for Death identity achievements and icon reference state.
- Localisation: covered for DTH names, parties, Zol, trait, route cosmetic names, and Death ideas.
- Assets/manifest: current manifest inspected.

## Resolved Country Package Surfaces

- The route-achievement manifest entries are current: `death_friend_of_zol`, `death_book_burner`, and `death_black_apostolate` are active and wired.
- The route achievement DDS triplets exist for all three route achievements.

## Map and state setup issues

- No static map ownership issues were found for DTH.
- Origin target triggers enforce island, population cap, not capital, not already consumed, not controlled by DTH, and no divisions.
- Resolved parent-side: origin triggers use preferred and outer remote filters against major/player capitals, safe owner/controller checks, low-pop island caps, no-capital checks, no-division checks, and no-Death-control checks.

## Politics, leader, portrait, flag, advisor, and party issues

- Zol is defined as a nonhuman fictional institutional leader with fixed name and no random name pool, matching the manifest note.
- No gender/name-pool mismatch found.
- DTH party localisation resolves all ideologies to `The Last Office`.
- DTH ideology-name localisation resolves all variants to `Death`.
- Cosmetic route localisation for Herald of Zol and Black Apostolate exists.
- Patched issue: missing `common/countries/cosmetic.txt` entries for both route cosmetic tags.

## Focus, decision, idea, and asset issues

- DTH focus loading is gated through `is_death_country = yes` and `death_setup_country` loads `death_focus_tree`.
- Death ideas are present and localized.
- Patched issue: defeat cleanup no longer leaves or adds active Death lifecycle ideas after defeat.
- Resolved parent-side: `death_friend_of_zol`, `death_book_burner`, and `death_black_apostolate` achievement `.gfx` entries point to present DDS files:
  - `gfx/achievements/death_friend_of_zol.dds`
  - `gfx/achievements/death_friend_of_zol_grey.dds`
  - `gfx/achievements/death_friend_of_zol_not_eligible.dds`
  - `gfx/achievements/death_book_burner.dds`
  - `gfx/achievements/death_book_burner_grey.dds`
  - `gfx/achievements/death_book_burner_not_eligible.dds`
  - `gfx/achievements/death_black_apostolate.dds`
  - `gfx/achievements/death_black_apostolate_grey.dds`
  - `gfx/achievements/death_black_apostolate_not_eligible.dds`

## Starting military, technology, industry, supply, and production issues

- DTH starts with no placed units.
- DTH starts with no convoys and zero research slots.
- History OOB only supplies ghost-host templates for later scripted spawning.
- Consumed states are stripped of industry, infrastructure, supply nodes, railways, ports, airbases, and other strategic buildings by `death_strip_current_state_buildings`.
- Remaining risk: DTH may still keep `death_country_without_breath` after defeat because the tag continues to exist as an empty country; I left that permanent rule idea intact because it is the core nonhuman country rule while the tag exists.

## AI and playability issues

- DTH has a fixed-purpose focus tree and no normal diplomacy/production economy.
- Early DTH has no starting divisions and relies on scripted spread.
- Remaining risk: origin remote-selection precision and richer DTH AI behavior beyond the inspected country package are broader event-system concerns, not patched here.

## Validation run

- `rg -n '^DTH\\s*=|\\bDTH\\b' '/home/klim/projects/Hearts of Iron IV/common/country_tags' common/country_tags` found `DTH` only in Chaos Redux.
- `file` verified DTH and route flags at `82x52`, `41x26`, and `10x7`, and verified Zol portrait as `156x210` DDS.
- A targeted check over `set_cosmetic_tag` usages in `010_death_effects.txt` confirmed `death_herald_of_zol` and `death_black_apostolate` are now defined in `common/countries/cosmetic.txt`.
- `rg` over scoped active files found no active `Spirit of War/Peace` or `spirit_of_war` / `spirit_of_peace` references.
- Follow-up achievement asset check found the route achievement DDS triplets present.

## Skipped validation

- No in-game launch validation was run.
- I did not run broad syntax validation over the whole event because the worktree already contains many unrelated Event 010 edits and the requested scope was a country-package audit with small local patches.

## Remaining risks

- The previously absent DDS triplets for the three active route achievements are resolved.
- The Event 010 asset manifest is current for active Herald/Black Book route achievement wiring.
- Origin state selection is low-pop island safe and uses remote major/player-capital distance tiers.
- No commit was created because the worktree was already broadly dirty with parent/user Event 010 changes; committing only this subagent patch would risk mixing ownership without parent review.
