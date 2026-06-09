# Event 006 Next Missing Country Package Audit

## Current Status Note

Historical read-only package audit. Its Kuban (`KUB`) and Altai (`ALT`) research remains useful only as archived evidence; the 2026-06-05 user correction supersedes KUB/ALT as current Event 006 package-expansion scope. Current country-addition work favors niche generic releases such as `ASN`, `KBN`, `PLM`, and `AYM` sharing `independence_wave_liberation_provisional_tree`.

Read-only country-package audit run on 2026-06-04 with explicit context only. No gameplay, localisation, asset, or flag files were edited.

## References checked

- Required offline wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, and National focus modding.
- Required vanilla docs: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, `documentation/loc_objects_documentation.md`, `documentation/script_concept_documentation.md`, `common/characters/_documentation.md`, `common/decisions/_documentation.md`, `common/ai_strategy/_documentation.md`, and `common/on_actions/_documentation.md`.
- Event 006 source files requested by the parent prompt, plus vanilla country tags, country history, state history, characters, localisation, flags, and vanilla focus precedents for candidate carriers.

## Current-source conclusion

The current Event 006 files already implement the documented package set through Eritrea and Mesopotamia. I found no live Event 006 identifiers for `DON`, `KUB`, `ALT`, `independence_wave_package_don`, `independence_wave_package_kuban`, `independence_wave_package_cossack`, `independence_wave_package_altai`, or `independence_wave_package_idel_ural` in the Event 006 script, constants, decisions, focus tree, ideas, AI, scripted localisation, or localisation.

Mapuche remains blocked by the user correction. PRA remains queued until Event 005 railway baggage is separated.

## Ranked candidates

### 1. Don Host / Don Cossack Host, carrier `DON`

Recommendation: best next bounded tranche.

Tag evidence:

- Vanilla tag exists in `common/country_tags/00_countries.txt`: `DON = "countries/Don Republic.txt"`.
- Vanilla country file exists: `common/countries/Don Republic.txt`.
- Vanilla history exists: `history/countries/DON - Don Republic.txt`, with capital state `218`, two research slots, starting tech, neutral politics, and `recruit_character = DON_vladimir_sidorin`.
- Vanilla country localisation exists for communism, fascism, democratic, neutrality, base name, DEF, and ADJ in `countries_l_english.yml`.
- Vanilla party localisation exists for Don communist, fascist, democratic, and neutrality party names in `parties_l_english.yml`.

State/core evidence:

- Vanilla state `218` is Rostov, a city state owned by SOV, with SOV core, VP 9417, one arms factory, one civilian factory, air base, and naval base.
- Vanilla state `245` is Millerovo, rural, SOV-owned and SOV-cored.
- Vanilla state `238` is Volgodonsk, rural, SOV-owned and SOV-cored.
- Vanilla Germany focus precedent dynamically adds Don cores on `218`, `245`, and `238` if they are missing. This makes Don suitable for the same Event 006 dynamic-core pattern already used for MIS, ITZ, MAY, NAH, and INU.
- Safe Event 006 start: seed only `218` as the anchor, mask `245` and `238` during release, then restore them as later proof/claim territory. Require the host to control `218`, `DON` to be inactive, chaos gate Evo IV/V or Evo III/IV depending on parent design, and normal Event 006 host survival checks.

Leader/portrait/flag evidence:

- Vanilla character `DON_vladimir_sidorin` exists in `common/characters/DON.txt` with country leader roles and field marshal role.
- Character localisation exists in `WUW_characters_l_english.yml`.
- The character references `GFX_portrait_DON_Vladimir_Sidorin` and `GFX_idea_DON_vladimir_sidorin`, but I did not find matching sprite registration or DDS files in vanilla by grep. This is the main caveat.
- Vanilla flag files are complete for base, communism, fascism, and neutrality in large, medium, and small flag folders. No new flag assets should be needed.

Likely Event 006 files touched:

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
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`

Risks:

- Event 005 already includes DON in Soviet Collapse progressive release logic and core setup. Event 006 must assign only Event 006 origin, package flags, provisional tree, and Event 006 decisions. It must not use Event 005 release variables, focus trees, republic logic, or event logs.
- The vanilla leader portrait reference is present but the portrait asset registration/files were not found. If the parent requires verified leader art, use an existing Event 006 council/non-portrait route or send portrait work through an asset subagent. Do not touch flags.
- Because `218` is strong and may be a host capital in some campaigns, the trigger must reject capital-state release and fall back to skip rather than erasing the host.

### 2. Kuban Host / Kuban People's Republic, carrier `KUB`

Tag evidence:

- Vanilla tag exists in `common/country_tags/00_countries.txt`: `KUB = "countries/Kuban Republic.txt"`.
- Vanilla country file exists: `common/countries/Kuban Republic.txt`.
- Vanilla history exists: `history/countries/KUB - Kuban Republic.txt`, with capital state `234`, two research slots, starting tech, neutral politics, and `recruit_character = KUB_ivanis_vasily_nikolaevich`.
- Vanilla country and party localisation exists for the supported ideologies.

State/core evidence:

- Vanilla state `234` is Krasnodar, a city state owned by SOV, with oil, tungsten, SOV core, VPs, one civilian factory, infrastructure, and a naval base.
- Vanilla states `233` Sochi and `235` Stavropol are SOV-owned, SOV-cored, and are used by the vanilla Kuban core precedent.
- Vanilla Germany focus precedent dynamically adds Kuban cores on `234`, `233`, and `235` if missing.
- Safe Event 006 start: seed only `234`, mask `233` and `235`, then restore them as proof/claim territory.

Leader/portrait/flag evidence:

- Vanilla character `KUB_ivanis_vasily_nikolaevich` exists in `common/characters/KUB.txt` with country leader and field marshal roles.
- Character localisation exists in `WUW_characters_l_english.yml`.
- The character references `GFX_portrait_KUB_ivanis_vasily_nikolaevich` and `GFX_idea_KUB_ivanis_vasily_nikolaevich`, but I did not find matching sprite registration or DDS files in vanilla by grep.
- Vanilla flags are complete for base, communism, fascism, and neutrality in large, medium, and small folders. No new flag assets should be needed.

Likely Event 006 files touched:

- Same surfaces as DON, with a Kuban package constant, seed trigger, reduced-release anchor, startup classification, focus/decision mini-overlay, package label, event-log rows, and docs.

Risks:

- Same Event 005 overlap risk as DON. `KUB` is already part of Event 005 progressive release candidate logic, so Event 006 must be origin-gated everywhere.
- `234` is oil-bearing and coastal, so the package could accidentally collide conceptually with Oil Protectorate or Free Port logic. The package should be explicitly Cossack/frontier historical-return, not a generic port or oil state.
- Portrait asset evidence has the same caveat as DON.

### 3. Idel-Ural / Altai-adjacent steppe federation check, possible carrier `ALT` only if narrowed

Tag evidence:

- Vanilla has no direct `Idel-Ural` country tag in the checked country tags.
- Vanilla has Idel-Ural cosmetic localisation and news text, and vanilla has `ALT = "countries/Altay.txt"`.
- `ALT` has country file, history, characters, portrait sprite registrations for Grigory Gurkin and Samuil Yufit, and complete ideology flag sets.

State/core evidence:

- `ALT` has vanilla cores in state `40` Altai Krai and state `654` Oyrot Region.
- This is clean for an Altai/Oyrot release, but it is not a clean Idel-Ural carrier and should not be used as an Idel-Ural fallback.

Leader/portrait/flag evidence:

- `ALT_grigory_gurkin` and `ALT_samuil_yufit` exist in vanilla characters.
- `GFX_portrait_Grigory_Gurkin` and `GFX_portrait_Samuil_Yufit` are registered in vanilla `_leader_portraits.gfx`.
- Complete ALT flag sets exist.

Likely Event 006 files touched:

- Same broad Event 006 surfaces if implemented as an Altai/Oyrot steppe package, but the current source matrix names Idel-Ural rather than Altai as the candidate. A parent implementation should first add or accept an explicit Altai/Oyrot package spec if this route is chosen.

Risks:

- This is not the next safest source-spec package because it does not directly satisfy the Idel-Ural row.
- Event 005 already uses ALT in Soviet Collapse progressive release logic and core setup.
- Recasting ALT as Idel-Ural would be a fallback, and fallbacks are forbidden without user discussion.

## Non-recommended missing packages

- Asante, Kanem-Bornu, Darfur, Zulu, Herero, Nama, Aymara, Muisca, and Palmares did not show clean vanilla country-tag support in the checked vanilla tag files. They likely require custom tags and asset planning before implementation.
- Kokand has a vanilla victory point name, but no clean country tag/history/flags were found in the checked vanilla support.
- Mapuche remains blocked by user correction unless a real accepted standalone tag/core package is present.
- PRA remains queued until Event 005 railway baggage is separated.

## Exact recommendation

Implement exactly one next package: `DON` as the Event 006 Don Host package.

Use a one-state Rostov `218` release anchor, dynamically seed and later restore broader Don proof cores `245` and `238`, set only Event 006 origin and package state, load only the Event 006 provisional tree, and reuse existing Event 006 old-name/frontier/council art families. Do not create or edit flag assets. If the parent requires a verified leader portrait before completion, route the missing portrait check through an asset subagent or represent leadership through Event 006 council mechanics until portrait support is confirmed.

Closure/final validation should not replace implementation if the parent wants another package tranche. If the parent does not want to accept the Event 005 tag-overlap and portrait caveats, prioritize closure/final validation instead of forcing a weaker custom-tag package.
