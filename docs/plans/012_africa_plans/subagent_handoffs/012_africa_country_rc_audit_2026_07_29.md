# Event 12 Africa country-package release-candidate audit

Date: 2026-07-29.

Scope: Event 12 host selection, original-host preservation, Event 6 Independence Wave niche-carrier loading, cosmetic identity surfaces, the sixteen priority-member carriers and sovereign characters, the South Africa branch, and country-linked focus, idea, decision, military, technology, industry, supply, production, AI, and asset surfaces.

The audit was read against the Event 12 country-package specifications and handoffs, the Event 6 registry and package-binding notes, the required offline Paradox wiki pages, and the installed vanilla documentation and country precedents.

## Result

The Event 12 country package is structurally wired for the sixteen priority-member identities, the seven Event 6 niche carriers, and the 51 mapped host playbooks, with no new country tags or priority-member cosmetic tags.

The current release-candidate asset tree contains all sixteen sovereign DDS portraits, all 21 Event 6 niche flag ladder files, and all 103 focus, idea, decision, and report-image DDS references registered by the package.

The host-selection, original-host state model, and generic-tree preservation gates are internally coherent. Normal Event 12 hosts, RSA exile patrons, and world-order package candidates are gated to `generic_focus` unless an explicit replacement approval flag exists; niche Event 6 carriers are the intentional direct-tree exception.

The seven Event 6 niche carriers are registered with country definitions, histories, localisation, focus loading, package effects, and shell gates, while retaining their original Event 6 tags and filename-driven flag ladders.

All sixteen sovereign character definitions, portrait references, history/Event 1240 recruitment consumers, and localisation entries resolve. The Aksum, Nubia, and Merina characters explicitly carry `gender = female` metadata.

One narrow mechanical patch was made: the Aksum, Nubia, and Merina sovereign characters now carry `gender = female` metadata to match their female titles and the country-package gender contract.

No new country tags, priority-member cosmetic tags, country package, focus tree, workbook row, or broad identity redesign was added by this audit. Concurrent asset work installed the approved portrait and niche-flag files; this handoff records and validates that state but does not claim their production.

## Country-package coverage checklist

| Surface | Status | Evidence |
| --- | --- | --- |
| Event 12 entry event and host initialization | Covered | `events/012_african_union.txt` (`chaosx.nr12.1`) and `common/scripted_effects/012_africa_effects.txt` (`africa_initialize_selected_host`) |
| Host-selection weighting and frozen pre-fire contacts | Covered | `common/scripted_effects/012_africa_effects.txt` (`africa_prepare_random_event_fire`, `africa_select_weighted_prefire_host`) |
| Original host persistence | Covered | `africa_origin_host_id`, `africa_original_host_preserved`, global `africa_host`, and `africa_is_current_host` in `common/scripted_effects/012_africa_effects.txt` and `common/scripted_triggers/012_africa_triggers.txt` |
| Mapped host playbook coverage | Covered structurally | `africa_apply_mapped_host_playbook` maps the 51 host rows documented in `docs/plans/012_africa_plans/012_africa_host_first_proof_exactness_handoff.md` |
| Priority-member carrier registry | Covered structurally | `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt` and `common/scripted_triggers/012_africa_priority_member_triggers.txt` |
| Niche Event 6 country definitions and histories | Present | `common/country_tags/006_independence_wave_countries.txt`, `common/countries/006_independence_wave_*.txt`, and `history/countries/006_independence_wave_*.txt` for DOX, DSX, DUX, DYX, DZX, EMX, and EQX |
| Niche Event 6 shell-receipt gate | Covered | `africa_priority_member_has_active_event6_shell_receipt` and the seven niche branches in `common/scripted_effects/012_africa_priority_member_effects.txt` |
| Sixteen sovereign character IDs | Present | `common/characters/012_africa_priority_member_characters.txt` |
| Vanilla-carrier sovereign recruitment | Covered | Hidden event `africa_priority_member.1240` in `events/012_africa_priority_member_events.txt` |
| Niche sovereign recruitment | Covered | Direct `recruit_character` lines in the seven Event 6 country history files |
| Priority-member focus tree and overlay loading | Covered structurally | `common/national_focus/012_africa_priority_member_focus.txt` and `africa_priority_member_ensure_focus_tree_loaded` |
| Priority-member starting and mature ideas | Covered structurally | `common/ideas/012_africa_priority_member_ideas.txt` and package registration effects |
| South Africa allied branch | Covered structurally | `events/012_africa_rsa.txt`, `common/scripted_effects/012_africa_rsa_effects.txt`, `common/scripted_triggers/012_africa_rsa_triggers.txt`, and `common/decisions/012_africa_rsa_decisions.txt` |

## File-surface checklist

The relevant Event 12 files were found in the following surfaces.

- Host event and host effects: `events/012_african_union.txt`, `common/scripted_effects/012_africa_effects.txt`, and `common/scripted_triggers/012_africa_triggers.txt`.
- Priority-member registration and force setup: `common/scripted_effects/012_africa_priority_member_effects.txt`, `common/scripted_effects/012_africa_priority_member_force_effects.txt`, and `common/scripted_triggers/012_africa_priority_member_triggers.txt`.
- Event 6 registry integration: `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`, `common/country_tags/006_independence_wave_countries.txt`, and the corresponding `common/countries/006_independence_wave_*.txt` and `history/countries/006_independence_wave_*.txt` files.
- Characters and portrait definitions: `common/characters/012_africa_priority_member_characters.txt` and `interface/012_africa_priority_member_characters.gfx`.
- Focus, ideas, and registered sprites: `common/national_focus/012_africa_priority_member_focus.txt`, `common/ideas/012_africa_priority_member_ideas.txt`, and `interface/012_africa_priority_member_assets.gfx`.
- Priority-member and South Africa localisation: `localisation/english/012_africa_priority_member_characters_l_english.yml`, `localisation/english/012_africa_priority_member_l_english.yml`, `localisation/english/012_africa_priority_member_focus_l_english.yml`, `localisation/english/006_independence_wave_countries_l_english.yml`, and `localisation/english/012_africa_rsa_l_english.yml`.
- South Africa branch: `events/012_africa_rsa.txt`, `common/scripted_effects/012_africa_rsa_effects.txt`, `common/scripted_triggers/012_africa_rsa_triggers.txt`, `common/decisions/012_africa_rsa_decisions.txt`, `common/decisions/categories/012_africa_rsa_categories.txt`, and `common/on_actions/012_africa_rsa_on_actions.txt`.
- Cosmetic identity files: `common/countries/012_africa_cosmetic.txt` and `common/countries/012_africa_world_order_cosmetic.txt`.
- Asset folders: `gfx/leaders/012_africa/priority_members`, `gfx/event_pictures/012_africa/priority_members`, `gfx/interface/goals/012_africa/priority_members`, `gfx/interface/ideas/012_africa/priority_members`, `gfx/interface/decisions/012_africa/priority_members`, and `gfx/flags`.

## Missing or stale country-package surfaces

The following surfaces were rechecked for the release candidate.

- `interface/012_africa_priority_member_characters.gfx` points all sixteen sovereign portrait names to `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_<package>_sovereign.dds`; all sixteen paths resolve to 131168-byte DDS files.
- The sixteen installed sovereign families are `aksum`, `asante`, `buganda`, `great_zimbabwe`, `harar`, `kanem_bornu`, `kilwa`, `kongo`, `luba`, `lunda`, `manden`, `merina`, `nubia`, `oyo`, `sokoto`, and `zulu`.
- Older institutional-council files are not used by current runtime character or portrait references; no council identifier or council portrait path remains on the audited runtime surfaces.
- `interface/012_africa_priority_member_assets.gfx` registers four report-event textures, eight focus icons, 35 idea icons, and 56 decision icons; the current path check reports 103 unique DDS references and zero missing files.
- The Event 6 niche tags DOX, DSX, DUX, DYX, DZX, EMX, and EQX each have base, medium, and small TGA flags under `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small`. The flag manifest and validation JSON report all seven ladders valid with the approved dimensions, headers, byte lengths, and opaque alpha.
- No Event 12-specific priority-member country tags or priority-member cosmetic tags were invented; the seven niche carriers continue to use the protected Event 6 tags and their installed filename-driven flag ladders.
- `common/countries/012_africa_cosmetic.txt` contains RSA and continental-route cosmetics only. Those identities are applied by RSA or route effects and are not assigned during priority-member registration.
- The seven niche carriers continue to use the protected Event 6 tags and the nine vanilla carriers continue to use their owning tags; no Event 12 identity surface overwrites those tags.
- HZX, EUX, and ELX remain dormant Event 6 shells marked `disabled_no_unique_current_state` or `scenario_only_unbound` in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, while `africa_apply_mapped_host_playbook` contains HZX, EUX, and ELX compact host rows. They are normally excluded by `africa_is_eligible_host` because they lack a valid controlled African capital/core, but a future Event 6 shell-creation path could make this dependency visible and needs an explicit design decision.

## Map and state setup

The host eligibility trigger requires an existing country, an Africa-mapped playbook, a non-capitulated country, a controlled African capital/core, and no active Event 12 commitment; this prevents dormant shells from being selected by ordinary pre-fire host selection.

`africa_initialize_selected_host` records the selected host ID and global target without transferring territory, releasing a tag, changing a capital, or replacing the original country identity.

The South Africa branch requires `tag = SAF`, `original_tag = SAF`, current Event 12 host state, and control/ownership of states 275, 681, and 719, which provides a concrete Pretoria/Cape/Natal witness before the allied branch starts.

The South Africa transfer and cleanup effects copy Event 12 runtime arrays and constitutional variables to the exile patron and clear the old host runtime, so no missing state-transfer cleanup was found.

Release-candidate safety note: installed vanilla South Africa has a meaningful `south_africa` focus tree (`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\national_focus\south_africa.txt:9` and its SAF-gated focuses). Because `africa_is_eligible_host` now requires `has_focus_tree = generic_focus`, SAF is intentionally excluded from ordinary Event 12 host selection so its vanilla tree cannot be overwritten. South Africa remains handled as the external Allied contact, civil-war, and peace-settlement package from another Event 12 host. The mapped host playbook and host-proof documents still contain SAF host-witness rows; reconciling those stale acceptance rows is deferred design work and remains a full-content documentation blocker, not a runtime overwrite defect.

No map rewrite was made, and no state ownership, core, claim, capital, port, railway, supply, resource, or victory-point mutation was found in the narrow country-package surfaces audited.

## Politics, leaders, portraits, flags, advisors, and parties

- The sixteen character IDs are present and referenced by the package effects and recruitment paths.
- The three female-presenting title identities, `africa_priority_aksum_sovereign`, `africa_priority_nubia_sovereign`, and `africa_priority_merina_sovereign`, now have `gender = female` in `common/characters/012_africa_priority_member_characters.txt`.
- The remaining thirteen sovereign character blocks do not set female metadata and therefore retain the default male metadata expected for their masculine titles.
- Current localisation uses public regnal or office titles such as Asantehene, Alaafin of Oyo, Sultan of Sokoto, Queen of Aksum, Kandake of Nubia, Queen of Merina, and King of the Zulu in `localisation/english/012_africa_priority_member_characters_l_english.yml`.
- The titles are direct public-facing identity labels rather than actual-ish personal names. This is coherent for a sovereign office package, but if the referenced portraits are fictional/generated personal portraits, the repository rule requiring gender-correct personal name pools remains an unresolved content decision and should not be silently redesigned in this audit.
- Party names and country names are present for the sixteen package IDs, with direct Event 6 country names for DOX, DSX, DUX, DYX, DZX, EMX, and EQX in `localisation/english/006_independence_wave_countries_l_english.yml`.
- `EMX` is localised as `Kilwa` with `Kilwan` adjective under all ideology variants; no stale “Kilwa Restoration” public name was found.
- No Event 12-specific advisor, high-command, commander, or portrait asset package was found for these sixteen identities. The existing package specs do not require a full advisor roster, so this is a playability enhancement rather than a narrow parser defect.
- No priority-member cosmetic country definitions were found in `common/countries/012_africa_cosmetic.txt`; this is correct for the accepted design because original country tags remain the carrier identity.

## Focus, decision, idea, and asset issues

- The priority-member focus file contains one tree ID, `africa_priority_member_focus_tree`, and eight focus IDs with localisation and registered icon names.
- The priority-member idea file contains 35 IDs, covering sixteen starting problems, three settlement ideas, and sixteen mature package ideas.
- Package registration wires starting and mature ideas and uses `africa_priority_member_ensure_focus_tree_loaded` to load the overlay for Event 6 tags or generic-focus vanilla carriers.
- The host replacement path is now guarded by `has_focus_tree = generic_focus` in `common/scripted_triggers/012_africa_triggers.txt:331-355`; a meaningful vanilla host tree is therefore excluded from normal Event 12 host selection before `africa_load_continental_focus_tree` can run.
- The South Africa exile-patron candidate is likewise guarded by `has_focus_tree = generic_focus` in `common/scripted_triggers/012_africa_rsa_triggers.txt:45-59`, and the world-order package candidate uses the generic-or-explicit-approval gate in `common/scripted_triggers/012_africa_world_order_triggers.txt:9-28`.
- `africa_priority_member_ensure_focus_tree_loaded` in `common/scripted_effects/012_africa_priority_member_effects.txt:251-287` intentionally loads the Event 12 tree for the seven Event 6 niche tags and for generic-focus vanilla carriers, while setting `africa_priority_member_focus_tree_overlay_skipped` for other meaningful trees.
- `interface/012_africa_priority_member_assets.gfx` has registered names for eight focus icons, 35 idea icons, 56 decision icons, and four report-event images, and all 103 current references resolve to files in the local asset tree.
- The older package handoff still describes 40 decision sprites and 16 unresolved post-settlement decision sprites, but the current tree now contains all 56 decision DDS files; the handoff is stale on this point and should be reconciled by the documentation owner.
- No broad focus-tree or decision rewrite was made because it would exceed the bounded country-package audit scope.

## Starting military, technology, industry, supply, and production

- `common/scripted_effects/012_africa_priority_member_force_effects.txt` defines five structural force profiles, package-specific template names, primary and reserve formations, local-support readiness factors, bounded equipment/manpower factors, and an understrength floor of two divisions.
- Niche Event 6 shells receive their shell setup through Event 6 runtime logic before Event 12 package effects run; vanilla carriers retain their existing country history technology, industry, production, and starting equipment.
- No package-specific technology grant, research-slot grant, production-line mutation, convoy/train/fuel adjustment, port assignment, or supply-network rewrite was found in the audited Event 12 country-package surfaces.
- This is consistent with the current package design, which supplies bounded force structures and package ideas rather than replacing each carrier’s entire starting economy.
- No unsupported military or technology parser construct was identified in the narrow inspection, but live executable validation remains parent/user-owned.

## AI and playability issues

- The package focus file and package effects provide AI-visible focus and idea surfaces, and the existing Event 12 AI strategy files remain outside this narrow patch.
- The force effects include local-support readiness and bounded retry logic, reducing the risk of zero-unit package starts.
- Host-tree replacement is now blocked for meaningful vanilla trees by the generic-focus checks described above. SAF’s exclusion from ordinary host selection is intentional RC safety; the remaining work is reconciling stale SAF host-witness/playbook acceptance rows with the external Allied-contact route.
- All sixteen sovereign portraits, all seven niche-carrier flag ladders, and all 103 registered focus, idea, decision, and report DDS references resolve in the current tree, so no country-package presentation blocker remains in these audited assets.
- HZX, EUX, and ELX should remain dormant until a current-map binding exists or Event 12 host eligibility explicitly excludes them by design; no fallback was added.

## Narrow patch made by this audit

Changed file:

- `common/characters/012_africa_priority_member_characters.txt`.

Changed identifiers:

- `africa_priority_aksum_sovereign` now has `gender = female`.
- `africa_priority_nubia_sovereign` now has `gender = female`.
- `africa_priority_merina_sovereign` now has `gender = female`.

Before the patch, the three female-titled sovereign character blocks had no explicit gender metadata and could be treated as the default gender.

After the patch, the three blocks explicitly match their Queen/Kandake localisation and the repository’s country-package gender requirement.

The working copy already contained a broader sovereign-versus-institutional-council rename in this same file from another change; that pre-existing rename was preserved and is not claimed as part of this audit patch.

## Validation

The protected country-tag audit completed with 136 protected Event 006/Soviet tags, zero external country-definition collisions, zero external identity-surface collisions, and one skipped random-event root.

The package coverage checks found all sixteen package trigger, idea, focus/AI, decision, and portrait-GFX identifier surfaces, all sixteen character IDs, all eight focus IDs plus the tree ID, and all 35 idea IDs.

The seven niche Event 6 tags each have a country definition, history file, and direct country localisation. The base, medium, and small flag checks found all 21 TGA files, and `docs/assets/012_africa_independence_wave_flags/notes/validation.json` reports `all_valid = true` for every ladder.

The character metadata check confirmed exactly the three intentional `gender = female` lines at the Aksum, Nubia, and Merina sovereign blocks.

The portrait and report-image path checks confirmed that all sixteen sovereign DDS references and all four report-event DDS references exist in the expected asset directories. The complete GFX path scan reports 103 unique focus, idea, decision, and report DDS references with zero missing paths.

The preservation-gate review confirmed `has_focus_tree = generic_focus` in `africa_is_eligible_host` (`common/scripted_triggers/012_africa_triggers.txt:331-355`), in `africa_rsa_is_valid_exile_patron` (`common/scripted_triggers/012_africa_rsa_triggers.txt:45-59`), and the generic-or-explicit-approval gate in `africa_world_package_candidate_base_is_valid` (`common/scripted_triggers/012_africa_world_order_triggers.txt:9-28`). The priority-member loader’s direct niche/generic split is present at `common/scripted_effects/012_africa_priority_member_effects.txt:251-287`.

No Hearts of Iron IV executable or live save was launched because repository instructions reserve live gameplay validation for the user.

## Skipped meaningful validation

No in-game focus-tree rendering, event firing, map rewrite, or save-based state-transfer test was run because the parent owns live gameplay validation and the repository instructions prohibit agents from launching Hearts of Iron IV.

No portrait, flag, focus-icon, idea-icon, decision-icon, or report-art production was attempted by this agent; concurrent asset work changed the current tree and its manifests were rechecked for this handoff.

## Remaining risks and handoff

- All sixteen sovereign portrait DDS files and all 21 niche flag ladder files are present and validated in the current tree. Their production manifests remain the source of provenance and are outside this audit’s ownership.
- Host-tree preservation is covered for normal hosts, RSA patrons, world-order candidates, and priority-member carriers by the current generic/approved or niche-specific gates. Vanilla SAF’s meaningful tree is intentionally preserved and SAF is handled as an external Allied-contact/civil-war/peace-settlement package; stale SAF host-witness/playbook acceptance rows remain deferred design reconciliation.
- The report-event, focus, idea, and decision references are file-complete in the current tree; older package handoffs still contain superseded asset counts and need documentation reconciliation.
- HZX, EUX, and ELX remain unbound dormant shells; the current package has no approved fallback or invented tags for them.
- Title-based sovereign names are direct public names and localise correctly, but the generated-personal-portrait name-pool rule remains unresolved until the portrait identity design is accepted.

No gameplay simplification or fallback was introduced by this audit.

## Final release-candidate re-audit (2026-07-29)

The earlier eight-present/eight-missing portrait count and all-seven-absent flag count are superseded by the current filesystem review. All sixteen sovereign portrait families are installed at `gfx/leaders/012_africa/priority_members`, and all seven Event 6 carriers have base, medium, and small TGA ladders at `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small`.

The protected country-tag audit remains clean after the asset and cosmetic changes: 136 protected Event 006/Soviet tags, zero external country-definition collisions, zero external identity-surface collisions, and one skipped random-event root. No Event 012 country tag or priority-member cosmetic tag was added.

All sixteen sovereign consumers resolve across character definitions, history or hidden Event 1240 recruitment, portrait GFX, and localisation. The seven niche carriers resolve through their Event 6 registry predicates, country definitions, histories, direct sovereign recruitment, Event 12 package effects, focus loader, ideas, forces, and flag ladders. Their original tags remain authoritative.

No package path audited can overwrite a meaningful existing vanilla tree during ordinary host selection: the host, RSA patron, and world-order candidate gates require `generic_focus` unless an explicit replacement approval flag is present, and the priority-member loader’s only non-generic branch is the seven-tag Event 6 niche exception. SAF’s meaningful vanilla tree is intentionally preserved; its external Allied-contact/civil-war/peace-settlement route is safe, while stale SAF host-witness/playbook acceptance rows remain deferred design reconciliation.

No country gameplay file was changed in this final re-audit. The only gameplay patch claimed by this handoff is the earlier explicit female metadata for the Aksum, Nubia, and Merina sovereign character IDs. No fallback, tag invention, broad identity redesign, or silent portrait substitution was introduced.
