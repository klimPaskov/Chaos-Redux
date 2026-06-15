# Event 010 Death Country Package Audit Handoff

Audit date: 2026-06-15
Scope: DTH Death country package only.

## Changed Files

- `history/countries/DTH - Death.txt`
- `docs/plans/010_death_plans/subagent_handoffs/country_package_audit_handoff.md`

## Changed Identifiers

- Tag: `DTH`
- OOB: `DTH_1936`

## Patch Summary

Before: `history/units/DTH_1936.txt` existed and defined the Death host templates, but `history/countries/DTH - Death.txt` did not register it. A starting or manually selected DTH could load without the template surface, and wiki guidance warns that countries should load an OOB even if no starting divisions are deployed.

After: `history/countries/DTH - Death.txt` registers `set_oob = "DTH_1936"` on line 2. The OOB still contains only `division_template` blocks and no `division = { ... }` placements, so Death keeps the intended no-starting-units setup while its templates are available.

## Country Package Coverage Checklist

- Tag registration: present. `common/country_tags/chaosx_countries.txt` defines `DTH = "countries/Death.txt"`.
- Tag conflict check: no `DTH` entry found in vanilla `common/country_tags`; only the Chaos Redux entry was found.
- Country definition: present. `common/countries/Death.txt` uses `color = rgb { 0 0 0 }`.
- History file: present. `history/countries/DTH - Death.txt` has capital placeholder, zero research slots, no convoys, Zol recruitment before politics, neutrality rule, and starting Death ideas.
- Character file: present. `common/characters/DTH.txt` defines `DTH_zol`, name `Zol`, portrait `GFX_portrait_DTH_zol`, and leader ideology `despotism`.
- OOB file: present. `history/units/DTH_1936.txt` defines templates only; no deployed land/naval/air units.
- Starting ideas: present. `death_country_without_breath` and `death_first_silence` are added in history and defined/localised.
- Focus tree: present. `common/national_focus/010_death_focus_tree.txt`, id `death_focus_tree`.
- Focus loading: DTH-only via `country = { factor = 0 modifier = { add = 30 is_death_country = yes } }`.
- Special classification: present. `common/scripted_triggers/chaosx_dynamic_triggers.txt` includes DTH in both `is_special_chaos_country` and `is_actual_nonhuman_country`.
- Initial world notification: no ordinary popup from `chaosx.nr10.1`; it is hidden and schedules delayed missing-island reports.
- Ordinary surrender shortcut: mitigated. `death_country_without_breath` has `surrender_limit = 1.00`; actual defeat is `death_check_defeat` -> `DTH = { num_of_controlled_states < 1 }`.

## File Surface Checklist

- `common/country_tags/chaosx_countries.txt`: DTH tag present.
- `common/countries/Death.txt`: black map color present.
- `common/characters/DTH.txt`: Zol character present.
- `history/countries/DTH - Death.txt`: patched to register `DTH_1936`.
- `history/units/DTH_1936.txt`: Death templates present, no divisions.
- `common/ideas/chaosx_ideas.txt`: Death country ideas present.
- `interface/chaosx_characters.gfx`: `GFX_portrait_DTH_zol` points to `gfx/leaders/010_death/portrait_DTH_zol.dds`.
- `interface/chaosx_ideas.gfx`: Death idea sprites present.
- `localisation/english/010_death_l_english.yml`: DTH name/adjective and Zol localisation present.
- `localisation/english/chaosx_ideas_l_english.yml`: Death idea localisation present.
- `common/national_focus/010_death_focus_tree.txt`: DTH focus tree present.
- `events/010_death.txt`: hidden entry and delayed report events present.

## Missing Or Stale Country Package Surfaces

- `DTH_neutrality_party` and related party-name localisation are not present in `localisation/english/010_death_l_english.yml`, and history does not set `name`/`long_name` in `set_politics`. The spec suggests `Zol` or `The Last Office`; this needs a parent design choice rather than an audit-only patch.
- `DTH_zol` has no explicit leader trait, `expire`, or `id` in `common/characters/DTH.txt`. The current leader works as a minimal character package, but the spec calls for a unique nonordinary Zol trait direction.
- `gfx/leaders/DTH/portrait_DTH_zol.dds` exists alongside the wired `gfx/leaders/010_death/portrait_DTH_zol.dds`. The wired path is correct; the duplicate is stale or legacy unless another surface intentionally uses it.
- Base `gfx/flags/DTH.tga` has nonzero RGB texture values, while ideology variants checked here are pure black. This is acceptable if the generated near-black default flag is intentional, but it does not strictly match the docs phrase "all-black flag set." The ruling neutrality flag is pure black.

## Map And State Setup Issues

- No starting owned states, cores, buildings, factories, supply, railways, ports, navy, or air are assigned in history. This matches the event design: Death starts from a runtime-selected island through `death_consume_current_state`.
- `capital = 1` is only a dormant placeholder until runtime setup moves the capital with `set_capital = { state = PREV remember_old_capital = no }` inside `death_consume_current_state`. This is not a current defect, but manual pre-event DTH selection may show a placeholder capital before Death consumes its origin.
- `death_consume_current_state` transfers owner/controller to DTH, adds a DTH core, removes population and buildings, applies wasteland flags/modifiers, and moves the capital to the consumed state.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

- Leader: `DTH_zol` is recruited before `set_politics`, matching wiki guidance for intended starting leaders.
- Portrait: `GFX_portrait_DTH_zol` is wired and the final DDS is 156x210.
- Gender/name pool: Zol is a fixed fictional/nonhuman/institutional-style name; no random human name pool is used.
- Ideology: neutrality/despotism pairing is present and all ideology country-name localisation resolves to "Death."
- Party names: missing as noted above.
- Advisors/high command: none found. This matches the fixed-purpose nonhuman package unless a future Herald/Zol office route needs advisors.
- Flags: all standard DTH flag sizes exist for base and ideology variants. Ideology variants are black; base default flag is near-black/generated rather than pure black.

## Focus, Decision, Idea, And Asset Issues

- Focus tree id `death_focus_tree` loads only for `is_death_country = yes`; `is_death_country` includes `tag = DTH`, `original_tag = DTH`, and `death_country`.
- Focus IDs found: `death_shroud_whispers`, `death_hunger_shore`, `death_mourning_host`, `death_wasteland_roads`, `death_black_census_focus`, `death_last_shores_focus`, `death_world_consumed_focus`.
- Focus icon sprites exist in `interface/010_death.gfx`.
- Starting ideas are defined, localised, and have sprite paths. The patched OOB now supports later focus/scripted host spawns by registering the templates at start.
- Decision surfaces are outside this audit's requested file list, but references show Death decisions use `is_death_country` exclusions and `death_country_exists` gates.
- Optional animated Zol/world-end UI assets, Black Atlas UI assets, and Black Oath/Herald art remain queued in `docs/events/010_death.md`; not a country-package blocker for the audited intent.

## Starting Military, Technology, Industry, Supply, And Production Issues

- Starting divisions: none. Validation found no `division = {` placements in `history/units/DTH_1936.txt`.
- Starting templates: present through `DTH_1936` after this patch.
- Starting navy/air: none found.
- Research slots: `set_research_slots = 0`.
- Convoys: `set_convoys = 0`.
- Industry/production: none in history. Runtime consumption strips buildings from Death states.
- Runtime stockpile/manpower: `death_setup_country` adds `20000` manpower and `5000` infantry equipment when the event-country setup first runs. This does not create starting units, but it is a balance/design surface to review if the intent also means no initial stockpile before host spawning.

## AI And Playability Issues

- DTH has focus-level `ai_will_do` weights and scripted spread/host behavior.
- No separate `common/ai_strategy/DTH.txt` was found. Current survival/playability is driven by national spirits, scripted pulses, decisions against Death, and focus AI rather than a dedicated AI strategy plan.
- `death_country_without_breath` suppresses normal diplomacy/economy/army desires and supports the no-normal-surrender behavior.
- Manual DTH play is possible only as a fixed-purpose/debug country. The tree is narrow and stage-gated; it is not a full normal-country tree, which matches the fixed-purpose Death exception but is shallower than the broad spec architecture.

## Meaningful Validation

- Checked offline wiki country-creation/OOB guidance and vanilla examples before patching.
- Checked `DTH` tag uniqueness against Chaos Redux and vanilla country tag files: only Chaos Redux defines it.
- Verified `history/countries/DTH - Death.txt` now registers `set_oob = "DTH_1936"`.
- Verified `history/units/DTH_1936.txt` has no `division = { ... }` placements.
- Verified `death_focus_tree` selector is DTH-only through `is_death_country`.
- Verified DTH is classified by shared `is_special_chaos_country` and `is_actual_nonhuman_country`.
- Verified `010_death_l_english.yml` and `chaosx_ideas_l_english.yml` keep UTF-8 BOM.
- Verified flag and portrait dimensions with `file`; verified flag RGB ranges with ImageMagick `identify`.

## Skipped Meaningful Validation

- Did not run the game or parser. This was a scoped country-package audit in an already-dirty Event 010 workspace with many uncommitted parent changes.
- Did not modify binary flags/portraits or generate new assets.
- Did not patch party names or Zol trait because the exact party/trait text needs a parent design choice.

## Remaining Setup Or Identity Risks

- Decide whether to add `DTH_neutrality_party`/`DTH_neutrality_party_long` as `Zol`, `The Last Office`, or another accepted wording.
- Decide whether Zol should receive a dedicated leader trait in `common/country_leader/chaosx_leader_traits.txt` or remain traitless.
- Decide whether the base non-ideology `DTH.tga` should be replaced with pure black to match the docs phrase "all-black flag set," or whether the generated near-black default flag is intentionally accepted.
- Review whether `death_setup_country` should grant manpower/equipment before first host spawn, or whether host spawn effects should be the only place those reserves appear.
