# Event 012 Created Actor Static Country Package Audit Handoff

Date: 2026-06-20
Scope: audit-only pass for Event 012 created, transformed, sponsored, and restored Africa actor country-package surfaces. No gameplay files were edited.

## Summary

No small, clear country-package bug was found that justified a local patch. The audited created actor package is statically covered across tag registration, country definitions, country histories, OOBs, flags, portraits, direct and ideology-specific localisation, shared classification, setup helpers, focus loading, role spirits, reinforcement paths, AI strategy, documentation, and asset manifests.

The remaining blocker wording about deeper route-specific country-package consequences is still valid. It is not a narrow static defect: the live implementation already has selected-unifier origin/profile cases, the regional-authority mandate/package cycle, dossier slot families, and created-actor role packages, but does not yet make every shared-tree country play as a fully bespoke route package.

## Files Changed

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_created_actor_static_country_package_audit_handoff.md`

## Files Inspected

- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`
- `common/country_tags/chaosx_countries.txt`
- `common/countries/*` for Event 012 tags `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`, `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, `GHC`, `BON`, `HYR`, `BIR`, and `SAO`
- `history/countries/<TAG> - *.txt` for the same 25 tags
- `history/units/<TAG>_1936*.txt` for the same 25 tags
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.txt`
- `common/scripted_triggers/chaosx_dynamic_triggers.md`
- `common/national_focus/012_africa_focus.txt`
- `common/national_focus/012_africa_authority_focus.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/ideas/012_africa_ideas.txt`
- `common/ai_strategy/012_africa.txt`
- `interface/012_africa.gfx`
- `localisation/english/012_african_union_l_english.yml`
- `localisation/english/chaosx_countries_l_english.yml`
- `docs/assets/012_africa/implementation_asset_manifest.md`
- Offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, and Country creation.
- Vanilla docs and precedents: `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `common/decisions/_documentation.md`, `common/ai_strategy/_documentation.md`, `common/characters/_documentation.md`, `common/ai_templates/_documentation.md`, and vanilla country/focus/capital/OOB examples.

## Country Package Coverage Checklist

- Tag registration: covered for all 25 Event 012 created actors in `common/country_tags/chaosx_countries.txt`.
- Country files: covered by one `common/countries/*.txt` file for each Event 012 tag, with graphical culture and map color.
- History files: covered by one `history/countries/<TAG> - *.txt` file for each Event 012 tag, with `capital`, OOB loading, technology, politics, popularities, and direct institutional leader setup.
- OOBs: covered by land OOBs for all 25 tags, plus naval and air OOB variants where the package has a matching maritime or air role.
- State handling: seat-state constants in `012_africa_effects.txt` and `012_africa_triggers.txt` match each actor history `capital` value.
- Setup hooks: `africa_setup_regional_authority_subject`, `africa_setup_high_chaos_actor`, and `africa_apply_created_country_setup_package` apply the one-time country package after transfer/binding.
- Focus loading: regional authorities load `africa_regional_authority_focus_tree`; high-chaos actors load `africa_high_chaos_actor_focus_tree`.
- Politics and leaders: all 25 history files define `set_politics`, `set_popularities`, and institutional `create_country_leader` blocks.
- Portraits: all 25 leader portrait references resolve to registered sprites and existing DDS files, with `GHP` intentionally reusing the Independence Wave gorilla chair portrait.
- Flags: normal, medium, and small TGA files exist for all 25 base tags, and direct `file` checks report expected HOI4 dimensions without `- top` origin output.
- Names: direct country names, `_DEF`, `_ADJ`, and democratic/communist/fascist/neutral variants with `_DEF` and `_ADJ` exist in `chaosx_countries_l_english.yml`.
- Ideas: umbrella spirits and role-specific seat spirits exist for the regional authorities and Bestiary actors.
- Forces and reinforcement: static OOBs, dynamic guard-division setup, role stockpiles, production packages, companion focus rewards, and decision-side reinforcement hooks are present.
- AI: `common/ai_strategy/012_africa.txt` contains survival, role-family, and tag/actor strategy entries for regional authorities and high-chaos actors.
- Assets and docs: `docs/assets/012_africa/implementation_asset_manifest.md` records the live portrait/flag/actor package coverage; `docs/events/012_africa_foundation.md` records the country-package scope.

## File Surface Checklist

- `common/country_tags/chaosx_countries.txt`: no missing tag entries for the 10 regional authorities or 15 high-chaos actors.
- `common/countries/`: no missing country definition files for the audited tags.
- `history/countries/`: no missing history files; all audited histories include a capital and leader setup.
- `history/units/`: no missing land OOBs; maritime/air extras are present only where relevant.
- `common/scripted_effects/012_africa_effects.txt`: spawn, bind, setup, role package, production, dynamic guards, focus loading, and reinforcement helpers are present.
- `common/scripted_triggers/012_africa_triggers.txt`: regional authority and high-chaos seat-state groups, transfer gates, mandate gates, and package gates are present.
- `common/scripted_triggers/chaosx_dynamic_triggers.txt`: all 25 tags are registered as special chaos countries; the 15 high-chaos actors are registered as actual nonhuman countries.
- `common/national_focus/012_africa_authority_focus.txt`: shared authority and Bestiary trees have country/role branches and capstones.
- `common/decisions/012_africa_decisions.txt`: Charter lifecycle, mandate, regional package, high-chaos package, and actor-side action surfaces exist.
- `common/ideas/012_africa_ideas.txt`: role spirits and umbrella spirits exist and are localised.
- `common/ai_strategy/012_africa.txt`: regional authority and high-chaos actor strategy blocks exist.
- `localisation/english/chaosx_countries_l_english.yml`: direct and ideology-specific country names are covered.
- `interface/012_africa.gfx`: leader portrait sprites resolve to live DDS files.
- `docs/assets/012_africa/implementation_asset_manifest.md`: asset coverage is current for the actor portrait/flag packages.

## Missing Or Stale Country Package Surfaces

- No stale tag reference, missing country file, missing history file, missing land OOB, missing focus-tree loader, missing portrait sprite, missing flag family, or missing ideology country-name localisation was found.
- No local documentation correction was needed beyond this audit handoff.
- Existing broader completion handoffs remain current where they say Event 012 still lacks full route-specific country-package depth beyond the implemented origin/profile, mandate/package, dossier-slot, and role-package layers.

## Map And State Setup Issues

- No seat-state mismatch found. Every audited `capital = <state>` in `history/countries/<TAG> - *.txt` matches the corresponding `@africa_<tag>_seat_state` constant.
- OOB province locations resolve to the expected actor seat state for the static land and naval OOB locations checked against vanilla plus mod state files.
- Regional authority spawns add a core and transfer the matched seat state before binding subjects.
- High-chaos actor spawns use `africa_can_transfer_seat_state_to_high_chaos` before adding a core and transferring the matched habitat state.
- No supply, railway, port, factory, or controller patch was made. The setup package already adds role-specific capital infrastructure, naval bases, dockyards, civilian factories, military factories, or bunkers where mapped.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

- No opposite-gender portrait/name-pool issue found. These created packages use direct institutional leader names, not one-person random personal-name pools.
- Generated/council/nonhuman portraits are wired through institutional leader names and stable `GFX_portrait_012_africa_*` sprites.
- Party setup is basic but present through ideology popularities and institutional leaders in each history file.
- Role staff and command staff are generated by setup helpers with institutional role naming, costs, and role traits.
- No flag orientation or missing-size issue found in normal/medium/small flag files for the 25 base tags.

## Focus, Decision, Idea, And Asset Issues

- Focus loading is present in the setup helpers and gated by `africa_regional_authority_subject` or `africa_high_chaos_actor`.
- The shared regional authority tree has common setup branches, family branches, and ten tag-specific capstones.
- The shared high-chaos tree has common setup branches, Bestiary role branches, and actor-specific capstones, including the later `BON`, `HYR`, `BIR`, and `SAO` parity work.
- Decision surfaces include Charter aid/exit/resistance, regional authority mandate/package actions, high-chaos package actions, and actor-side role consequences.
- Idea coverage includes umbrella spirits plus one named role seat spirit per created actor.
- Asset coverage is documented and wired for generated/regional portraits, high-chaos portraits, flag families, and related achievement assets.
- No narrow focus, decision, idea, or asset patch was made.

## Starting Military, Technology, Industry, Supply, And Production Issues

- All 25 tags have land OOBs and starting technology blocks.
- Maritime actors have naval OOBs and matching naval tech gates; air-capable actors have air OOBs and air-tech gates.
- Dynamic guard counts are present for regional authorities and high-chaos actors through `africa_calculate_authority_guard_count`, `africa_create_authority_guard_divisions`, `africa_calculate_high_chaos_guard_count`, and `africa_create_high_chaos_guard_divisions`.
- Reinforcement helpers exist and are called from relevant focus/decision paths.
- Created actors receive one-time production package helpers for support equipment, infantry equipment, convoys, motorized, or trains according to role family.
- No force, technology, industry, or production patch was made.

## AI And Playability Issues

- Regional authority survival, family-route, and tag-package AI strategy blocks are present.
- High-chaos actor survival, family-route, and actor-package AI strategy blocks are present.
- AI route validity is materially improved by tag gates, package flags, mandate/capstone checks, former/resistant-member exclusions, and capital-control checks.
- Residual playability risk is design-depth, not static wiring: the shared trees and shared setup packages are adapted by tag, but they are still shared companion trees rather than fully bespoke route-specific country packages.

## Validation

- Compared all 25 country tag entries against `common/countries/` files and `history/countries/` files; no missing files found.
- Checked direct and ideology-specific localisation keys for all 25 tags, including `_DEF` and `_ADJ`; no missing keys found.
- Checked normal/medium/small flag files for all 25 tags with `file`; dimensions are `82x52`, `41x26`, and `10x7`, and no `- top` origin output appeared.
- Compared `capital =` state IDs against the Event 012 seat-state constants; all 25 matched.
- Mapped OOB `location =` province IDs through vanilla plus mod state files; no OOB location outside the actor's seat state was found.
- Resolved all leader portrait sprite references in the 25 history files to registered sprite entries and existing DDS textures.
- Checked shared special-country and nonhuman classifiers; all 25 Event 012 actor tags are documented and registered where expected.

## Skipped Meaningful Validation

- No live in-game scenario launch, map render, focus load, or GUI render validation was run. This handoff is a static country-package audit only, matching the requested narrow subagent scope.
- No balance simulation was run for the created-actor forces, industry, AI, or reinforcement pace.
- No asset visual inspection pass was rerun beyond file presence, dimensions, sprite wiring, and manifest alignment.

## Remaining Setup Or Identity Risks

- The current package still relies on shared regional authority and Bestiary focus trees. That is acceptable for this narrow static audit, but it does not close the broader blocker around deeper route-specific country-package consequences.
- Existing-country variants and selected unifier host identities still need later full-route consequence design if the parent wants bespoke outcomes beyond origin/profile cases and current decision/focus hooks.
- Live scenario validation and live focus loading in game remain outside this handoff.
- No plan handoff was written beyond this audit report because no broad new redesign was scoped or requested here.
