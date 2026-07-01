# Event 015 Country-Package-Adjacent Audit Handoff

Date: 2026-07-01
Scope: `utopia_manifesto` cosmetic tags, flag coverage, runtime focus-tree loading, dynamic unit families, claim/integration behavior, and achievement registration.
Patch mode: no gameplay patch made. The only confirmed defect is in flag asset coverage, which was outside the requested patch authority.

## Country Package Coverage Checklist

- Cosmetic tag registration: covered in `common/countries/cosmetic.txt` for `utopia_new_utopia`, `utopia_necessary_commonwealth`, `utopia_league_of_need`, and `utopia_marked_bounds_state`.
- Event-created country tags: none needed. Repo search found no `utopia_*` country tag or history package under `common/country_tags/` or `history/countries/`; Event 015 mutates the accepting existing country.
- Runtime focus tree: covered by `utopia_manifesto_accept_manifesto` in `common/scripted_effects/015_utopia_manifesto_effects.txt`, which calls `load_focus_tree = { tree = utopia_manifesto_tree keep_completed = no }` only after setting `utopia_manifesto_accepted`; `utopia_manifesto_can_load_tree` gates repeat loads.
- Rejection cleanup: initial rejection cleanup clears acceptance, route, ledger, arrays, ideas, and targeting state in `utopia_manifesto_reject_manifesto`. No late identity rollback helper exists, but no inspected path calls rejection after late cosmetic identity application.
- Claims and integration: claims are staged through state flags and missions; integration cores are gated behind compliance and ledger conditions. No instant free core path was found.
- Dynamic unit families: unit templates and spawns are capped by per-family variables and constants, and spawn into controlled states only.
- Achievement registration: Event 015 achievements are registered in `common/achievements/chaos_redux_achievements.txt` as `015_utopia_*` achievements gated by `achievement_utopia_*_ready` flags.

## File Surface Checklist

- `common/countries/cosmetic.txt`: registered four cosmetic tags at lines 25-39.
- `localisation/english/015_utopia_manifesto_l_english.yml`: ideology-specific cosmetic localisation is present for all four tags at lines 16-71.
- `gfx/flags/utopia_new_utopia.tga`, `gfx/flags/utopia_necessary_commonwealth.tga`, `gfx/flags/utopia_league_of_need.tga`, `gfx/flags/utopia_marked_bounds_state.tga`: base flags present and header-validated.
- `gfx/flags/medium/*.tga` and `gfx/flags/small/*.tga`: base medium/small copies present and header-validated.
- `common/scripted_effects/015_utopia_manifesto_effects.txt`: accept/reject, cosmetic identity, unit spawn, claim, integration, and achievement flag helpers inspected.
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`: target eligibility, focus load gate, claim safety, and integration safety inspected.
- `events/015_utopia_manifesto.txt`: event calls accept/reject helpers only.
- `common/national_focus/015_utopia_manifesto_focus_tree.txt`: late identity focus completions call the cosmetic identity helpers.
- `docs/assets/015_utopia_manifesto/manifest.md`, `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_cosmetic_flag_asset_handoff.md`, and `docs/events/015_utopia_manifesto.md`: documentation surfaces inspected for asset claims and late-identity notes.

## Missing or Stale Country Package Surfaces

Finding 1 - ideology-specific flag variants are missing for all four runtime cosmetic tags.

Evidence:
- Localisation defines ideology-specific cosmetic names for `utopia_new_utopia_democratic`, `utopia_new_utopia_communism`, `utopia_new_utopia_fascism`, `utopia_new_utopia_neutrality`, and equivalent variants for the other three tags in `localisation/english/015_utopia_manifesto_l_english.yml`.
- The cosmetic effects set base tags only: `set_cosmetic_tag = utopia_new_utopia`, `utopia_necessary_commonwealth`, `utopia_league_of_need`, and `utopia_marked_bounds_state` in `common/scripted_effects/015_utopia_manifesto_effects.txt`.
- The offline cosmetic tag wiki notes that fallback `COSMETICTAG.tga` does not override an ideology-specific base country flag. Event 015 can apply cosmetic tags to arbitrary accepting minors, many of which have ideology-specific base flags.
- Missing runtime files:
  - `gfx/flags/utopia_new_utopia_democratic.tga`, `_communism.tga`, `_fascism.tga`, `_neutrality.tga`
  - `gfx/flags/utopia_necessary_commonwealth_democratic.tga`, `_communism.tga`, `_fascism.tga`, `_neutrality.tga`
  - `gfx/flags/utopia_league_of_need_democratic.tga`, `_communism.tga`, `_fascism.tga`, `_neutrality.tga`
  - `gfx/flags/utopia_marked_bounds_state_democratic.tga`, `_communism.tga`, `_fascism.tga`, `_neutrality.tga`
  - The same 16 filenames are also missing under `gfx/flags/medium/` and `gfx/flags/small/`.

Impact:
- Cosmetic names and map colors can apply while the visible flag may remain the accepting country's ideology-specific original flag. This is a country-package-adjacent asset defect for arbitrary existing-country targets.

Patch status:
- Not patched. The prompt explicitly forbade patching flags/assets. Recommended follow-up is to create real imagegen-derived ideology-specific variants or approved copies from the generated base flag art for all four ideologies in normal, medium, and small sizes, then update the asset manifest and flag handoff.

Parent resolution:
- Implemented after audit. All four cosmetic tags now have `_democratic`, `_communism`, `_fascism`, and `_neutrality` TGA variants in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`, copied from the corresponding generated base flag art. The asset manifest, icon/animation handoff, cosmetic flag handoff, and event docs document the resolved coverage.

Finding 2 - asset docs are stale about the flag fallback risk.

Evidence:
- `docs/assets/015_utopia_manifesto/manifest.md` records only base normal/medium/small flag coverage for the four cosmetic tags.
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_cosmetic_flag_asset_handoff.md` records base normal/medium/small output only.
- `docs/events/015_utopia_manifesto.md` says the tags use the standard cosmetic-tag path but does not warn that ideology-specific flag variants are required for consistent replacement on arbitrary target countries.

Patch status:
- Not patched. Docs were outside the requested patch authority.

Parent resolution:
- Implemented after audit. The Event 015 asset manifest, icon/animation handoff, cosmetic flag handoff, and event documentation now record ideology-specific flag coverage and the reason it is needed for arbitrary accepting minors.

## Map and State Setup Issues

- No new state ownership, controller, core, supply, railway, port, resource, or building setup is required because Event 015 targets an existing country and does not create a tag.
- Claim safety is present in `utopia_manifesto_needful_land_claim_safe`: controlled by ROOT, not already core of ROOT, not previously claimed by the Event 015 state flag, and ROOT must be eligible to open Needful Land.
- Boundary and marked-district missions add claims through `add_claim_by = ROOT` only after objective-ready checks, then mark the state as `utopia_manifesto_needful_land_claimed`.
- Integration safety is present in `utopia_manifesto_can_integrate_state`: controlled by ROOT, not already core, owned/claimed/common-admin state, no active or completed integration flag, plus compliance and ledger gates or Marked Bounds route.
- Core creation is delayed to `utopia_manifesto_complete_integration_project` and requires compliance above the core gate, stable Consent, and safe Overreach.

## Politics, Leader, Portrait, Flag, Advisor, and Party Issues

- No leaders, portraits, advisors, parties, or character files are touched by Event 015. No event-created country registration is needed.
- Cosmetic map colors are registered for the four late-route tags in `common/countries/cosmetic.txt`.
- Flag issue remains: base generated flags exist, but ideology-specific variants are missing for arbitrary countries with ideology-specific base flags.

## Focus, Decision, Idea, and Asset Issues

- Focus tree load scope is narrow: `events/015_utopia_manifesto.txt` calls `utopia_manifesto_accept_manifesto`; that helper sets `utopia_manifesto_accepted`, checks `utopia_manifesto_can_load_tree`, loads `utopia_manifesto_tree`, and sets `utopia_manifesto_focus_tree_loaded`.
- The focus tree itself is `default = no` and has a country factor only for `has_country_flag = utopia_manifesto_accepted`.
- Late focus completions call `utopia_manifesto_apply_new_utopia_identity`, `utopia_manifesto_apply_necessary_commonwealth_identity`, and `utopia_manifesto_apply_marked_bounds_state_identity`; League identity is applied through `utopia_manifesto_maybe_apply_league_identity`.
- Decision files were not part of the requested inspect list. Effects/triggers expose claim and integration gates that appear country-safe, but this audit does not certify decision visibility/target filtering.
- Asset issue remains limited to ideology-specific cosmetic flag variants.

## Starting Military, Technology, Industry, Supply, and Production Issues

- No starting military, technology, industry, supply, or production package exists or is required because Event 015 modifies an existing accepting country.
- Dynamic unit families are not starting OOB. They are runtime rewards using capped spawn helpers and route/focus/decision calls.
- Unit families found: `Household Guard`, `Storehouse Engineers`, `Craft Militia`, `Harbor Watch`, `Surveyor Columns`, and `League Cadres`. Each template has a creation flag and spawn counts are clamped through `constant:utopia_manifesto_unit.*` values.
- No uncapped mass spawn or instant tag-level army setup issue was found in the inspected effects.

## AI and Playability Issues

- Accepting AI countries are eligible only through `is_valid_utopia_manifesto_automatic_target`, which blocks majors, strong factory/division states, nonhuman/special chaos countries, capitulated countries, and AI countries fighting a player.
- Runtime focus replacement is deliberate. The target gate excludes several known special focus-tree actors through country flags, but it does not detect every bespoke minor tree in the mod. This is an identity/playability risk rather than a script defect in the inspected scope: an eligible small country with a bespoke tree and no exclusion flag can still be converted to `utopia_manifesto_tree`.
- No patch was made because adding a broader focus-tree exclusion policy could alter Event 015 target design and was outside narrow country-package safety authority.

## Validation Performed

- Checked required offline wiki references, including cosmetic tag behavior, country creation, focus trees, effects, triggers, localisation, and graphical assets.
- Checked vanilla precedent for `set_cosmetic_tag` and `load_focus_tree`.
- Verified base TGA headers for all four cosmetic flags in normal, medium, and small folders:
  - normal: 82x52, image type 2, 32 bpp
  - medium: 41x26, image type 2, 32 bpp
  - small: 10x7, image type 2, 32 bpp
  - all inspected files report bottom-origin descriptor matching the repo flag handoff claim.
- Searched country tag/history registration surfaces and found no Event 015 country tag package requirement.
- Searched achievement registration and found Event 015 achievements registered under `common/achievements/chaos_redux_achievements.txt`.

## Changed Files

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_country_package_adjacent_audit.md`

No gameplay, localisation, asset, focus, decision, achievement, or country file was patched.
