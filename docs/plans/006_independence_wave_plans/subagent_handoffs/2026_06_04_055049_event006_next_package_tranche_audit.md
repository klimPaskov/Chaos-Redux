# Event 006 Next Package Tranche Audit

Date: 2026-06-04 05:50 UTC
Role: `chaosx_country_package_auditor`
Scope: read-only Event 006 sidecar audit. No gameplay, localisation, asset, country, history, or flag files were patched.

## Required Context Read

- `AGENTS.md`
- Skills: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-event-planning`, `chaos-redux-improvement-loop`, `hoi4-focus-trees`, `hoi4-decisions-missions`
- Offline wiki pages: Data structures, Triggers, Effect, Localisation, Scopes, Event modding, Decision modding, AI modding, National focus modding, Country creation, Modifiers, Idea modding
- Vanilla docs/examples: effects/triggers docs, decision docs, AI strategy docs, character docs, vanilla country/history/state/decision examples

## Existing Implementation Boundary

Exclude the already-completed or partial Event 006 packages named by the parent prompt: Old Great Bulgaria, Assyria, Danzig, Buganda, Sokoto, Bukhara, Khiva, Guarani, Charrua, Kurdistan, generic Railway/Timetable Authority, Archive-State, and Necromantic Custodianship.

Non-negotiables carried into the ranking:

- Event 006 releases must stay independent from Event 005.
- Event 006 must never erase a host.
- Do not propose Mapuche unless a real accepted independent tag exists. Current repo evidence still supports the earlier blocker: no standalone accepted Mapuche tag/core package was verified.
- Do not propose `PRA` until Event 005 railway baggage is separated.
- New flag artwork is allowed in principle for Event 006, but this audit does not create flags or assets.

## Ranked Next Tranches

### 1. Barotseland Single-Package Tranche, Recommended

Package direction: `iw_pkg_barotseland`, local-polity or historical-return package around the Lozi floodplain, treaty/autonomy memory, and protected regional state formation.

Why this is safest:

- It is a one-state vanilla releasable with a clean state-history core, a named vanilla leader, ideology flags in all flag sizes, and no Event 005 collision found in the Event 006 repo scan.
- It adds source-spec value because Barotseland is repeatedly named in the Event 006 country-package/spec matrices as an African local-polity or historical-return candidate, but is not already implemented.
- It follows the same low-risk pattern as recent Bukhara/Khiva/Sokoto work: use an existing vanilla carrier tag and add Event 006 package proof, startup spirit, formation decisions, AI bias, focus overlay nodes, event-log labels, and docs without creating country or flag files.

Evidence:

- Tag: vanilla `BAR = "countries/Barotseland.txt"` in `~/projects/Hearts of Iron IV/common/country_tags/00_countries.txt`.
- Country/history: `~/projects/Hearts of Iron IV/history/countries/BAR - Barotseland.txt` sets `capital = 981`, recruits `BAR_yeta_iii`, and defines neutrality-heavy politics.
- State group: vanilla state `981 - Barotseland` has owner `ENG`, `add_core_of = ZAM`, `add_core_of = BAR`, VP `697` Mongu, chromium/tungsten resources, and rural state category.
- Leader/portrait: `~/projects/Hearts of Iron IV/common/characters/BAR.txt` defines `BAR_yeta_iii` as a country leader; `~/projects/Hearts of Iron IV/dlc/dlc043_gotterdammerung/interface/ww_portraits.gfx` registers `GFX_portrait_BAR_yeta_iii`.
- Localisation: vanilla country and party localisation exist for `BAR`; `BAR_yeta_iii` has English character localisation.
- Flags/assets: vanilla has `BAR_communism`, `BAR_democratic`, `BAR_fascism`, and `BAR_neutrality` in large, medium, and small flag folders.
- Missing Event 006 surfaces: no `independence_wave_package_barotseland`, package constants, seed trigger, package label, BAR-specific focus overlay, decisions, startup spirit, AI profile, event-log type, or Event 006 docs entry found.

New flags/assets required:

- New flags: no.
- New mandatory gameplay assets: no, if the parent reuses existing Event 006 generic package icons for the first tranche.
- Future polish assets: Lozi/floodplain decision icon, package spirit icon, focus icon, and optional route seal should be routed later through asset subagents.

### 2. Dahomey Single-Package Tranche

Package direction: `iw_pkg_dahomey`, West African old-state package around Dahomey/Benin, coastal customs, palace council, and restrained old-name legitimacy.

Why it ranks second:

- It has a clean vanilla one-state core and complete vanilla flags, so release safety is strong.
- It has source-spec value as the country-package matrix names Dahomey as an existing or old-state package for the Bight of Benin.
- It is weaker than Barotseland because vanilla `DAH` appears to provide advisors but no clear country-leader role in `common/characters/DAH.txt`; the parent should add an Event 006 council or verify a vanilla leader path before implementation.

Evidence:

- Tag: vanilla `DAH = "countries/Dahomey.txt"` in `~/projects/Hearts of Iron IV/common/country_tags/00_countries.txt`.
- Country/history: `~/projects/Hearts of Iron IV/history/countries/DAH - Dahomey.txt` sets `capital = 776`, starting tech, convoys, politics, and recruits many `DAH_*` characters.
- State group: vanilla state `776-Dahomey.txt` has owner `FRA`, `add_core_of = DAH`, VP `10919`, infrastructure, and a naval base.
- Leaders/portraits: `common/characters/DAH.txt` contains advisor-style `DAH_*` characters; no `country_leader` role was found by audit search. Treat leader setup as missing until parent verifies otherwise.
- Localisation: vanilla country localisation exists for `DAH` ideology names and adjective.
- Flags/assets: vanilla has `DAH_communism`, `DAH_democratic`, `DAH_fascism`, and `DAH_neutrality` in large, medium, and small flag folders.
- Missing Event 006 surfaces: no package constants, seed trigger, package label, focus overlay, formation decisions, startup spirit, AI profile, event-log type, or docs entry for Dahomey found.

New flags/assets required:

- New flags: no.
- New mandatory non-flag asset: likely no if using a generic Event 006 council/old-state icon, but a leader/council definition is required. If the parent wants a bespoke Dahomey council portrait or palace seal, route it through asset subagents instead of improvising.

### 3. Verified Americas Game-Rule Mini-Tranche: Miskito, Maya, or Itza

Package direction: one small local-polity tranche using one or more of `MIS`, `MAY`, and `ITZ`, not Mapuche.

Why it ranks third:

- The tags, country files, council character definitions, localisation, and ideology flags exist in vanilla.
- It has source-spec value as the Event 006 specs name Maya, Itza, and Miskito-style local-polity packages as game-rule or indigenous packages.
- It is not the immediate safest because these tags do not have persistent state-history cores in the scan. Vanilla Chilean decisions add cores dynamically before transfer, so Event 006 would need its own explicit core/anchor helper and validation. This is more invasive than Barotseland or Dahomey.

Evidence:

- Tags: vanilla `MIS`, `MAY`, and `ITZ` are registered in `~/projects/Hearts of Iron IV/common/country_tags/00_countries.txt`.
- Country/history:
  - `MIS - Miskito.txt`: capital `317`, comment says cores `312`, `317`, recruits `MIS_miskito_council` only under Trial of Allegiance.
  - `MAY - Maya.txt`: capital `475`, comment says cores `313`, `475`, `476`, `474`, recruits `MAY_maya_council` only under Trial of Allegiance.
  - `ITZ - Itza.txt`: capital `311`, comment says core `311`, recruits `ITZ_itza_council` only under Trial of Allegiance.
- Vanilla core precedent: `~/projects/Hearts of Iron IV/common/decisions/CHL.txt` dynamically adds cores for `MIS` on states `312` and `317`, `MAY` on `313`, `475`, `476`, `474`, and `ITZ` on `311`.
- Leaders/portraits: vanilla character files define council leaders for all three tags, but the audit did not verify matching portrait sprite registrations beyond the character references. Parent should verify sprites before treating this as asset-complete.
- Localisation: vanilla country and council localisation exists for `MIS`, `MAY`, and `ITZ`.
- Flags/assets: vanilla has ideology flags for all three tags in large, medium, and small folders.
- Missing Event 006 surfaces: no Event 006 package flags, package constants, local-polity labels, dynamic core/anchor helper, focus overlays, decisions, startup spirits, AI profile, event-log types, or docs entries for these tags found.

New flags/assets required:

- New flags: no.
- New mandatory implementation support: yes, an Event 006-owned core/anchor path is needed because state-history cores were not verified.
- New portrait/assets: verify vanilla council portrait sprites first; if missing, route council portrait/icon work through asset subagents.

## Not Recommended for the Next Tranche

- `PRA`: still queued until Event 005 railway baggage is separated. Existing repo evidence shows PRA is Event 005-branded and lacks persistent state-history cores for Event 006.
- Mapuche: do not implement until a real accepted independent tag and core/state package is created or explicitly approved.
- Don/Kuban: vanilla `DON` and `KUB` have strong leaders, flags, and vanilla dynamic core precedent in `NSB_Poland.txt`, but no persistent state-history cores were found, and Event 005 currently has Don/Kuban-adjacent custom successor content plus `DON`/`KUB` progressive-release references. This should wait for an origin-separation design pass, not be the next safest Event 006 package.

## Recommended Parent Tranche

Implement `iw_pkg_barotseland` only.

Keep it deliberately narrow:

- seed `BAR` only from state `981`
- require `BAR` inactive and the host survival/protected-state checks to pass
- set Event 006 origin and `independence_wave_package_barotseland`
- add one startup spirit, one package label, two focus overlay nodes, Formation Ledger decisions, one event-log package type, and restrained AI weights
- do not touch Event 005 files
- do not add country files, history files, or flag files

## Files Likely Touched for Barotseland

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `common/ai_strategy/006_independence_wave.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`

Avoid touching:

- Event 005 files
- `common/country_tags/`
- `common/countries/`
- `history/countries/`
- `history/states/`
- `gfx/flags/`

## Risks and Validation Checks

- Host survival: verify a release from state `981` cannot fire if it would consume the host's protected last state or protected capital. The host must never be erased.
- Origin separation: every package-specific decision, focus, idea, AI strategy, event-log type, and label must require Event 006 origin/package state, not tag alone.
- Existing-tag safety: if `BAR` already exists, Event 006 must not overwrite it with a focus tree. Use only Event 006 additive content if explicitly designed.
- Focus loading: load only the Event 006 provisional tree/overlay, never Event 005 content.
- Localisation: add all package labels, decision names/descs, focus names/descs, idea names/descs, event-log text, and scripted loc. Keep `006_independence_wave_l_english.yml` UTF-8 with BOM.
- Icon coverage: if generic Event 006 icons are reused, verify all `GFX_*` references are registered. Do not request or wire new art names without placeholder-safe definitions.
- AI: add restrained local-polity/historical-return weights; avoid aggressive expansion without state proof and Border Commission checks.
- Validation commands: run helper/localisation/icon reference scans similar to the 2026-06-04 wiring audit after implementation. Include a package audit after the tranche.

## Asset Note

No new flag artwork is required for the recommended Barotseland tranche. Vanilla `BAR` flags exist in all required sizes. New package-specific icons, portraits beyond the vanilla leader portrait, route seals, and animation are optional future polish and should be routed through the asset subagent workflow if requested.
