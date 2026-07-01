# Event 015 Utopia Manifesto Final Country-Package-Adjacent Audit

Date: 2026-07-01
Agent: Chaos Redux country package subagent
Scope: final country-package-adjacent audit for `utopia_manifesto`, focused on focus loading, cosmetic identities, flag coverage, rejection cleanup assumptions, claim/core safety, integration gates, and achievement/cosmetic identity readiness.

## Verdict

Country/cosmetic/flag package status: PASS for completion.

Gameplay gate caveat: integration is safe against instant free cores, but `utopia_manifesto_can_integrate_state` treats local storehouses and household councils as support/accelerator state flags rather than hard prerequisites. If the intended design is that every integration must have both local storehouses and household councils before the Common Administration project can start, this remains a mechanics follow-up, not a tiny country-package defect.

No gameplay, localisation, asset, or country file was patched. This handoff is the only file changed by this audit.

## Country Package Coverage Checklist

- PASS: No new country tag package is intended or needed. Searches under `common/country_tags/`, `history/countries/`, and `history/states/` found no Event 015 `utopia_*` country/history/state setup surfaces.
- PASS: `utopia_manifesto_tree` is loaded only through `utopia_manifesto_accept_manifesto` in `common/scripted_effects/015_utopia_manifesto_effects.txt`, after `utopia_manifesto_accepted` is set and only when `utopia_manifesto_can_load_tree = yes`.
- PASS: The focus tree itself is `default = no` and its `country` block gives weight only to countries with `utopia_manifesto_accepted` in `common/national_focus/015_utopia_manifesto_focus_tree.txt`.
- PASS: Cosmetic colors are registered in `common/countries/cosmetic.txt` for `utopia_new_utopia`, `utopia_necessary_commonwealth`, `utopia_league_of_need`, and `utopia_marked_bounds_state`.
- PASS: Cosmetic localisation covers the base keys through the focus/cosmetic shared keys and has ideology-specific `_democratic`, `_communism`, `_fascism`, and `_neutrality` name, DEF, and ADJ keys in `localisation/english/015_utopia_manifesto_l_english.yml`.
- PASS: Runtime flags exist for all four cosmetic tags, including ideology variants in normal, medium, and small flag folders.
- PASS: No leader, portrait, advisor, party, starting OOB, history country, or map setup package is required.

## File Surface Checklist

- `events/015_utopia_manifesto.txt`
  - `chaosx.nr15.1` option A calls `utopia_manifesto_accept_manifesto`; option B is human-only and calls `utopia_manifesto_reject_manifesto`.
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
  - `utopia_manifesto_accept_manifesto`: initializes ledger, adds opening ideas, and loads `utopia_manifesto_tree`.
  - `utopia_manifesto_reject_manifesto`: clears acceptance, ledger state, arrays, target arrays, and active mission flags.
  - `utopia_manifesto_apply_new_utopia_identity`, `utopia_manifesto_apply_necessary_commonwealth_identity`, `utopia_manifesto_apply_league_identity`, `utopia_manifesto_apply_marked_bounds_state_identity`: set late cosmetic tags.
  - `utopia_manifesto_complete_integration_project`: only core-grant path, guarded by compliance plus Consent/Overreach gates.
  - Claim effects use `add_claim_by = ROOT`; no direct claim-to-core shortcut was found.
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
  - `is_valid_utopia_manifesto_target`, `is_valid_utopia_manifesto_automatic_target`, `utopia_manifesto_can_load_tree`, `utopia_manifesto_needful_land_claim_safe`, and `utopia_manifesto_can_integrate_state` inspected.
- `common/national_focus/015_utopia_manifesto_focus_tree.txt`
  - Late outcome focuses call the cosmetic identity helpers.
  - No focus directly grants cores.
- `common/decisions/015_utopia_manifesto_decisions.txt`
  - `decision_utopia_common_administration` starts/completes the integration project through scripted effects.
  - `decision_utopia_local_households` now requires Needful Land claim or Common Administration state lifecycle before councils.
- `common/countries/cosmetic.txt`
  - Four Event 015 cosmetic identities registered.
- `localisation/english/015_utopia_manifesto_l_english.yml`
  - Country/cosmetic identity names covered for all four ideologies.
- `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`
  - Base and ideology-specific TGA flags covered for all four cosmetic tags.
- `common/achievements/chaos_redux_achievements.txt`, `localisation/english/chaosx_achievements_l_english.yml`, `interface/chaosx_achievements.gfx`, `gfx/achievements/`
  - Event 015 achievement identifiers, localisation, sprites, and DDS files covered.

## Missing Or Stale Country Package Surfaces

No missing country package surfaces found.

The previous stale original-ideology-flag risk is resolved. Current files include all of these variants in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`:

- `utopia_new_utopia`, plus `_democratic`, `_communism`, `_fascism`, `_neutrality`
- `utopia_necessary_commonwealth`, plus `_democratic`, `_communism`, `_fascism`, `_neutrality`
- `utopia_league_of_need`, plus `_democratic`, `_communism`, `_fascism`, `_neutrality`
- `utopia_marked_bounds_state`, plus `_democratic`, `_communism`, `_fascism`, `_neutrality`

Supporting docs now also describe this in:

- `docs/assets/015_utopia_manifesto/manifest.md`
- `docs/assets/015_utopia_manifesto/icon_animation_handoff.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_cosmetic_flag_asset_handoff.md`
- `docs/events/015_utopia_manifesto.md`

## Map And State Setup Issues

No country-history or map setup issue found.

- Event 015 does not create a country tag, change starting ownership, change starting controllers, or assign a capital.
- No starting cores, claims, supply, railway, port, resource, building, or victory-point edits are intended.
- Claims are runtime-only and use state flags:
  - `utopia_manifesto_needful_land_claim_safe` requires controlled state, non-core state, not already claimed by Event 015, and ROOT eligibility.
  - `utopia_manifesto_apply_boundary_arbitration_state_outcome` adds claims after arbitration outcome checks.
  - `utopia_manifesto_resolve_marked_district_survey_mission` adds hardline claims only to validated marked survey states and records forced-settlement risk.
- Cores are not granted by claims. The only core path found is `add_core_of = ROOT` inside `utopia_manifesto_complete_integration_project`.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

No politics package defect found.

- No new country leader, character, portrait, advisor, commander, party, election, law, or diplomacy setup is intended.
- No generated personal leader portrait/name pairing exists, so the gender/name-pool audit is not applicable.
- Cosmetic tags are fictional institutional identities, not character packages.
- Cosmetic flag coverage is clean: all four base tags and all ideology variants exist in every HOI4 flag folder and header-validate to the expected sizes.
- No `drop_cosmetic_tag` cleanup is present in rejection, but rejection is only exposed on the initial event option before any inspected cosmetic identity path can run. If another system later calls `utopia_manifesto_reject_manifesto` after late-route identity application, it would need a cosmetic rollback helper.

## Focus, Decision, Idea, And Asset Issues

Focus and cosmetic identity readiness: PASS.

- `utopia_manifesto_tree` is not a default tree and is loaded only by the accept helper.
- `utopia_new_utopia` calls `utopia_manifesto_apply_new_utopia_identity`.
- `utopia_necessary_commonwealth` calls `utopia_manifesto_apply_necessary_commonwealth_identity`.
- `utopia_marked_bounds_state` calls `utopia_manifesto_apply_marked_bounds_state_identity`.
- `utopia_manifesto_maybe_apply_league_identity` can apply `utopia_league_of_need` when League focus/member/confidence gates are met and no later identity has already superseded it.
- Achievement readiness is aligned with these paths:
  - `utopia_manifesto_maybe_check_achievements` calls `utopia_manifesto_maybe_apply_league_identity` before setting ready flags.
  - `015_utopia_new_utopia` and `015_utopia_league_of_need` are registered and gated by `achievement_utopia_new_utopia_ready` and `achievement_utopia_league_of_need_ready`.
  - All 12 Event 015 achievement DDS sets exist: normal, `_grey`, and `_not_eligible`.

Asset issue status: PASS for country/cosmetic/flag package.

- The flag TGA validation checked 60 files: 20 normal-size, 20 medium, 20 small.
- Expected headers:
  - normal: 82x52, image type 2, 32 bpp, descriptor 8, bottom-origin
  - medium: 41x26, image type 2, 32 bpp, descriptor 8, bottom-origin
  - small: 10x7, image type 2, 32 bpp, descriptor 8, bottom-origin

## Claim, Core, And Integration Gate Findings

PASS: No instant free core path was found.

- `common/national_focus/015_utopia_manifesto_focus_tree.txt` has no `add_core_of`, `add_state_core`, or direct core reward.
- `common/decisions/015_utopia_manifesto_decisions.txt` starts integration through `decision_utopia_common_administration`, not direct coring.
- `common/scripted_effects/015_utopia_manifesto_effects.txt` has one core-grant path:
  - `utopia_manifesto_complete_integration_project`
  - requires `compliance > constant:utopia_manifesto_integration.compliance_core_gate`
  - requires ROOT `utopia_manifesto_consent_stable = yes`
  - requires ROOT `utopia_manifesto_overreach_safe = yes`

PARTIAL/RISK: Local storehouses and household councils are not hard start prerequisites for every integration project.

- `utopia_manifesto_can_integrate_state` requires control, non-core status, owned or claimed/common-admin state status, no previous integration, and compliance plus ledger stability or Marked Bounds route.
- `utopia_manifesto_start_integration_project` sets `utopia_manifesto_common_administration`.
- `utopia_manifesto_complete_integration_project` gives bonuses if `utopia_manifesto_local_storehouse` or `utopia_manifesto_household_councils` are present, but it does not require both flags before the core check.
- This is not an instant-core bug, because the compliance/core gate remains. It is a design-gate caveat if the parent intended local stores and councils to be mandatory, not optional accelerators.

No patch made: adding mandatory storehouse/council flags would materially change the integration mechanic and route pacing. That belongs to a decision/mechanics follow-up, not this final country/cosmetic package audit.

## Starting Military, Technology, Industry, Supply, And Production Issues

No starting setup issue found.

- Event 015 does not create a country with starting army, navy, air force, research slots, technologies, production lines, convoys, trains, manpower, fuel, or stockpiles.
- Runtime unit families are focus/decision rewards, not a starting OOB package.
- No new supply, port, railway, resource, building, or capital setup is intended.

## AI And Playability Issues

No country-package AI blocker found.

- Automatic targets are AI-only, non-major, normal civilian countries, not special chaos or nonhuman countries, not capitulated, and not fighting a player.
- Focus replacement remains a deliberate Event 015 design. It is gated by `utopia_manifesto_accepted`, but it does not detect every possible bespoke minor focus tree. This is an existing identity/playability risk for arbitrary eligible minors, not a country-package registration defect.
- Decision AI weights exist for integration and supporting decisions, though deeper route-aware AI behavior is outside this country-package audit.
- Remaining multi-Utopia mission risks from prior decision audit, such as generic relationship flags and concurrent target storage, are broader decision-system risks and not blockers for cosmetic/country package completion.

## Validation

- Consulted required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, national focuses, country creation, cosmetic tags, graphical assets, and achievements.
- Consulted vanilla documentation for effects, triggers, modifiers, localisation/object references, decision/focus/cosmetic behavior where applicable, plus vanilla `common/countries/cosmetic.txt` precedent.
- Searched country tag/history/state surfaces for Event 015 country package leakage: no `utopia_*` tag/history/state setup found.
- Searched Event 015 runtime script for `load_focus_tree`, `set_cosmetic_tag`, `drop_cosmetic_tag`, `add_core_of`, `add_state_core`, `add_claim_by`, ownership transfer, annexation, release, and dynamic country effects.
- Header-validated all 60 cosmetic flag TGAs across normal, medium, and small folders: no missing files, no bad dimensions, no top-origin TGAs.
- Checked all 36 Event 015 achievement DDS files for presence.

Skipped validation:

- No live game/runtime validation was performed from this subagent audit.
- No spreadsheet checks were performed; the user explicitly said not to touch spreadsheets.
- No visual art critique beyond header/size/origin and documented source/manifest consistency was performed.

## Patches

Changed files:

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_final_country_package_audit.md`

Changed gameplay identifiers: none.

Changed tags, state IDs, leaders, parties, focus tree IDs, localisation keys, or formable IDs: none.

Before behavior: Event 015 country/cosmetic/flag package had to be re-audited after ideology flag variants were added.

After behavior: No runtime behavior changed. The final handoff records that the country/cosmetic/flag package is clean for completion, with a mechanics caveat around whether local storehouses and household councils should be hard integration prerequisites.

## Remaining Risks

- If the design requirement is mandatory local storehouse plus household council before every integration project, `utopia_manifesto_can_integrate_state` needs a follow-up mechanics patch.
- If any future path calls `utopia_manifesto_reject_manifesto` after late cosmetic identity application, add a cosmetic rollback helper using `drop_cosmetic_tag` and clear late identity flags.
- Arbitrary eligible minor focus replacement remains a known design risk because acceptance loads `utopia_manifesto_tree` onto existing countries.

## Completion Readiness

Country/cosmetic/flag package is clean for completion.

The only remaining caveat is a decision/mechanics gate question, not a country package, cosmetic tag, localisation, or flag coverage defect.
