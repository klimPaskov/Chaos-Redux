# Event006 Country Package Audit After Generic Playability

Date: 2026-06-05
Agent: `chaosx_country_package_auditor`
Scope: Event006 Independence Wave country-package setup, localisation, tag, history, flag, release setup, KUB/ALT exclusion, and Event005 separation audit.

## Summary

No gameplay, localisation, asset, tag, country, history, focus, or decision files were patched.

The current Event006 country-package state matches the 2026-06-05 correction at the audited surfaces:

- `KUB` and `ALT` are not active Event006 package carriers. The only active Event006 script references found for them are the explicit candidate exclusions in `can_independence_wave_use_candidate_tag`.
- `ASN`, `KBN`, `PLM`, and `AYM` are set up as generic niche Event006 releases with unique flags and shared `independence_wave_liberation_provisional_tree` access.
- `DFR` and `ZUL` remain implemented local-polity packages with custom tag/country/history/localisation/flag support.
- Event006 releases receive startup army and state-building support through `independence_wave_setup_released_country`.
- The inspected Event005 focus/setup surfaces do not attach Event005 content to current Event006-origin custom tags. Overlap tags remain a separation risk only if future Event005 code bypasses the existing spawn/origin gates.

## Files Changed

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_event006_country_package_audit_after_generic_playability.md`

## Audited Inputs

- `docs/plans/006_independence_wave_plans/source_of_truth_map.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/events/006_independence_wave.md`
- `common/country_tags/chaosx_countries.txt`
- `common/countries/Asante Council.txt`
- `common/countries/Kanem-Bornu Authority.txt`
- `common/countries/Palmares Council.txt`
- `common/countries/Aymara Highland Congress.txt`
- `common/countries/Darfur Council.txt`
- `common/countries/Zulu Council.txt`
- `history/countries/ASN - Asante Council.txt`
- `history/countries/KBN - Kanem-Bornu Authority.txt`
- `history/countries/PLM - Palmares Council.txt`
- `history/countries/AYM - Aymara Highland Congress.txt`
- `history/countries/DFR - Darfur Council.txt`
- `history/countries/ZUL - Zulu Council.txt`
- `docs/assets/006_independence_wave/flags/manifest.md`
- `docs/assets/006_independence_wave/flags/darfur/manifest.md`
- `docs/assets/006_independence_wave/flags/zulu/manifest.md`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `events/006_independence_wave.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_countries_l_english.yml`
- Event005 files were read only for separation evidence: `common/scripted_effects/005_soviet_collapse_effects.txt`, `common/scripted_triggers/005_soviet_collapse_triggers.txt`, `common/decisions/005_soviet_collapse_decisions.txt`, Event005 focus files, Event005 events, and Event005 localisation.

## Country Setup Findings

| Tag | Status | Evidence |
| --- | --- | --- |
| `ASN` | Pass | Tag definition, country file, history file, country localisation, 30 flag files across base/ideology variants and large/medium/small, seeded generic cores on state `274`, ordinary package identity restore, shared tree load. |
| `KBN` | Pass | Tag definition, country file, history file, country localisation, 30 flag files, seeded generic cores on states `774` and `901`, ordinary package identity restore, shared tree load. |
| `PLM` | Pass | Tag definition, country file, history file, country localisation, 30 flag files, seeded generic cores on states `936` and `498`, ordinary package identity restore, shared tree load. |
| `AYM` | Pass | Tag definition, country file, history file, country localisation, 30 flag files, seeded generic cores on states `947`, `951`, and `506`, ordinary package identity restore, shared tree load. |
| `DFR` | Pass | Tag definition, country file, history file, country localisation, 15 flag files, seeded package cores on states `887` and `767`, reduced anchor state `887`, package flag/effect path, Darfur decisions and localisation. |
| `ZUL` | Pass | Tag definition, country file, history file, country localisation, 15 flag files, seeded package core on state `719`, reduced anchor state `719`, package flag/effect path, Zulu decisions and localisation. |

Each custom history file defines capital, research slots, basic technologies, politics, popularities, and a council leader using vanilla generic portrait sprite references. Custom party-name localisation is not present for these tags; I treated that as polish, not a functional package blocker.

## Generic Niche Lane

`ASN`, `KBN`, `PLM`, and `AYM` are correctly kept generic:

- `independence_wave_seed_niche_generic_candidates` adds their temporary cores at high chaos.
- `independence_wave_restore_niche_generic_release_identity` sets `independence_wave_niche_generic_release` and clears package/formable/strange identity flags for those tags.
- `independence_wave_setup_released_country` calls `independence_wave_load_provisional_focus_tree`, which loads `independence_wave_liberation_provisional_tree` only for `is_independence_wave_release = yes`.
- No bespoke package overlay, formable family, Event005 focus tree, KUB/ALT-style package route, or tag-specific decision package was found for these four tags.

## Startup Playability

`independence_wave_setup_released_country` provides current release playability support:

- sets `chaosx_release_origin_independence_wave`
- sets Event006 package variables and ordinary release state
- adds `independence_wave_provisional_committee`
- adds `12000` manpower through `constant:independence_wave_startup.startup_manpower`
- adds `900` infantry equipment and `80` support equipment through script constants
- creates an unlocked `Independence Wave Provisional Guard` template
- spawns `2` Provisional Guard divisions at the capital
- adds one instant arms factory in a controlled core state
- loads the shared provisional focus tree

Generic expansion beyond the starting state is present through package proof, claim, and Border Commission systems rather than direct multi-state release. The current generic niche lane keeps extra state cores/claims available for later proof where implemented.

## KUB/ALT Scope Check

Active Event006 gameplay/localisation surfaces were searched for `KUB`, `ALT`, `Kuban`, `Altai`, and `Oyrot`.

Current result:

- `common/scripted_triggers/006_independence_wave_triggers.txt` contains only the expected candidate exclusions:
  - `NOT = { tag = KUB }`
  - `NOT = { tag = ALT }`
- No active KUB/ALT references were found in Event006 AI, ideas, decisions, scripted localisation, localisation, focus tree, icons, or event script.
- Documentation still preserves superseded KUB/ALT notes as historical candidate disclaimers, which matches the source-of-truth map.

## Event005 Separation

Current custom Event006 tags `ASN`, `KBN`, `PLM`, `AYM`, `DFR`, and `ZUL` have no references in inspected Event005 effects, triggers, decisions, AI, focus, events, or Event005 localisation.

For overlap tags such as `OGB` and `PRA`:

- Event006 setup sets `chaosx_release_origin_independence_wave` and loads only `independence_wave_liberation_provisional_tree`.
- Event005 shared setup and event-created focus loader both guard against `chaosx_release_origin_independence_wave`.
- Event005 direct high-chaos setup helpers still contain direct Event005 focus-tree loads, but the inspected call paths require SOV-scoped Event005 readiness and target tags to not exist before spawning. An already existing Event006-origin overlap tag is therefore not a valid target through those normal paths.

Remaining risk: future Event005 edits could call direct `soviet_collapse_setup_*_successor` helpers without the existing spawn/existence gates. That is a future-guard risk, not a current observed Event006 attachment path.

## Validation

Ran static validation/searches:

- Verified the required offline Paradox wiki pages and vanilla documentation before inspecting repo files.
- Confirmed custom tag definitions: one `common/country_tags/chaosx_countries.txt` entry each for `ASN`, `KBN`, `PLM`, `AYM`, `DFR`, and `ZUL`.
- Confirmed one `common/countries` file and one `history/countries` file for each audited custom tag.
- Confirmed flag file counts:
  - `ASN`, `KBN`, `PLM`, `AYM`: 30 files each across `.dds`/`.tga`, base/ideology variants, and large/medium/small.
  - `DFR`, `ZUL`: 15 `.tga` files each across base/ideology variants and large/medium/small.
- Checked flag manifests for missing referenced final/source/processed files; no missing paths were reported.
- Confirmed `006_independence_wave_l_english.yml` and `chaosx_countries_l_english.yml` have UTF-8 BOM bytes `efbbbf`.
- Brace-balance check returned `0` for:
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/decisions/006_independence_wave_decisions.txt`
  - `common/national_focus/006_independence_wave_focus.txt`
  - `events/006_independence_wave.txt`
  - `common/ai_strategy/006_independence_wave.txt`
  - `common/ideas/006_independence_wave_ideas.txt`
- Searched the audited Event006 files for unsupported `<=` and `>=`; none found.
- Searched Event006 files for `ROOT.`/`PREV.` variable tokens. Only normal variables in `independence_wave_build_capital_railway_to_this_state` appeared, not scoped temporary variables.

Skipped validation:

- No in-game run was performed.
- No binary asset visual inspection was performed beyond file existence and manifest path checks.
- No spreadsheet patch was made.

## Remaining Blockers And Follow-Up

1. Full Event006 completion is still not proven. This audit only covers country-package setup and separation surfaces.
2. Custom party-name localisation for `ASN`, `KBN`, `PLM`, `AYM`, `DFR`, and `ZUL` is absent. This does not block release functionality, but a localisation pass could add party names if those governments need more on-screen identity.
3. Event005 direct setup helpers remain unsafe if future code calls them outside their current spawn/existence gates. Keep Event006-origin guards on any new Event005 overlap-tag call path.
4. Some docs intentionally preserve KUB/ALT historical notes. Those should remain framed as superseded candidate records unless a later user request reopens them.
5. Final package completion still requires a broader event-completion audit after any further package, decision, spreadsheet, or localisation changes.

## Skills Used

- `chaos-redux-events`
- `chaos-redux-subagents`
