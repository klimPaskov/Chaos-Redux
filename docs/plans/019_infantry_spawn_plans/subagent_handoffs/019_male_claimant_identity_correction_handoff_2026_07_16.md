# Event 019 Male Claimant Identity Correction Handoff

> Visual supersession notice: this handoff remains authoritative for male gameplay names, sex flags, and leader metadata. Any statement below about human portrait appearance, portrait review, or earlier portrait assets is superseded by `019_full_portrait_regeneration_handoff_2026_07_16.md`; the fixed slots now show armies/hosts with no individual focal human/person. The dated direct-scenario `GFX_portrait_communist_rebels` review is also superseded: SCN-013 now reuses the Event 19 formation scenes through `GetInfantrySpawnScenarioActorArmyScene`.

Date: 2026-07-16

## Result

All twenty Event 019 claimant profiles now create and present male leaders. Slot numbers, portrait sprite identifiers, region gates, archetype mapping, commander statistics, stable character UIDs, claimant ledgers, and promotion behavior are unchanged.

Claimant creation has one `create_corps_commander` path. It sets `female = no`. The exact-ID post-create scan requires `is_female = no` before the claimant row can be appended. The former even-slot flag and duplicate female creation branch are removed.

No registry file was edited. No fallback or simplification was used.

## References consulted

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-subagents`
- `chaos-redux-event-assets` for the direct scenario portrait review
- Offline wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Country creation
- Vanilla `common/characters/_documentation.md`
- Vanilla `documentation/effects_documentation.md`
- Vanilla `documentation/triggers_documentation.md`
- Vanilla `common/national_focus/spain.txt` dynamic corps-commander precedent
- Vanilla explicit male operative creation and `is_female = no` trigger precedents

## Final name and region matrix

Every profile has four male localisation variants. The first name in each row is the asset-metadata primary.

| Slot | Male name variants | Preserved runtime region gate |
| ---: | --- | --- |
| 01 | Erik Vinterdal<br>Soren Halberg<br>Lukas Eberhardt<br>Willem Van Aert | Europe |
| 02 | Milan Vargov<br>Tomas Kral<br>Viktor Volny<br>Stefan Dravik | Europe |
| 03 | Faris al-Mazhar<br>Nabil Darzi<br>Idris Qamar<br>Rafiq Ben Yusef | Middle East or Africa |
| 04 | Dev Suryapala<br>Arjun Rathore<br>Ravi Nanduri<br>Sahan Perera | Asia or Australia |
| 05 | Arkady Zorenko<br>Timur Bekhan<br>Viktor Saranov<br>Mikhail Oraz | Europe or Asia |
| 06 | Anil Senaviratne<br>Mihir Kulkarni<br>Ranjit Das<br>Naim Rahman | Asia |
| 07 | Tadashi Morioka<br>Kenjiro Sakai<br>Liang Weizhen<br>Park Min-jun | Asia |
| 08 | Lucio Valcarcel<br>Isidro Montoro<br>Camilo Ferreyra<br>Renato Velasco | North America or South America |
| 09 | Lucien Vautrin<br>Henri Delorme<br>Alain Mercier<br>Willem Declerq | Europe or North America |
| 10 | Nikolai Karsky<br>Ivan Volenko<br>Dmitri Mirov<br>Veselin Radic | Europe |
| 11 | Samir Qazwini<br>Arman Tolegen<br>Jalal Nouri<br>Bekir Sadyk | Middle East or Asia |
| 12 | Minh Tran Vinh<br>Huy Pham Dao<br>Akio Shibata<br>Park Yeon-jun | Asia or Australia |
| 13 | Matteo Vellani<br>Luca Marenzi<br>Nikos Argyros<br>Mateo Salvat | Europe or South America |
| 14 | Klaus Weissen<br>Anselm Hartmann<br>Petr Novak<br>Marek Wozniak | Europe |
| 15 | Jabari N'Doye<br>Kofi Mensah<br>Themba Dlamini<br>Amadou Keita | Africa |
| 16 | Layth al-Hadri<br>Marwan Zahir<br>Samir Khoury<br>Amin Ben Said | Middle East or Africa |
| 17 | Shunpei Arakida<br>Hiroshi Kagawa<br>Chen Rongwei<br>Han Jae-sung | Asia |
| 18 | Ingvar Solhavn<br>Frej Nyholm<br>Elias Rask<br>Sigurd Falk | Europe |
| 19 | Elias Mercer<br>Jonah Whitcomb<br>Rafael Ortega<br>Malcolm Avery | North America or South America |
| 20 | Marcus Voss<br>Elliot Ward<br>Nathan Vale<br>Samuel Arden | Australia only |

Profiles 04 and 12 retain their Asia and Australasia diaspora gate. Profile 20 remains Australia-only.

## Gameplay and derivative audit

- `infantry_spawn_set_current_claimant_profile_metadata` now sets only the archetype. No claimant sex flag or even-slot sex branch remains.
- `infantry_spawn_create_current_claimant_commander` uses one explicit male creation block.
- The post-create unit-leader proof matches both the immutable claimant ID and `is_female = no` before any claimant ledger mutation.
- Claimant takeover and derivative promotion continue to promote the exact existing character. The protected exact-transfer package also contains a male claimant proof.
- The Event 19 derivative package has three one-person direct leader identities and three institutional councils. Its source is owned by the exact-transfer specialist and was audited read-only.
- The scenario actor effect creates `Unbidden Assembly` and `Muster Council` as institutional authorities without personal sex metadata. Both use `GFX_portrait_communist_rebels`. The sprite resolves to `gfx/leaders/001_communism_spread/portrait_communist_rebels.dds`. A decoded original-size review confirmed a trio of faceless, shrouded nonhuman figures, so the portrait is genuinely genderless and no swap is required.

## Files changed

Gameplay and localisation:

- `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt`
- `common/script_constants/019_infantry_spawn_claimant_constants.txt`
- `localisation/english/019_infrantry_spawn_l_english.yml`

Current documentation and specifications:

- `docs/assets/019_infantry_spawn/notes/claimant_identity_metadata.md`
- `docs/events/019_infantry_spawn/overview.md`
- `docs/specs/019_infantry_spawn_specs/matrices/019_possessed_general_matrix.md`
- `docs/specs/019_infantry_spawn_specs/matrices/019_asset_inventory.md`
- `docs/specs/019_infantry_spawn_specs/prompts/019_infantry_spawn_asset_prompt.md`
- `docs/specs/019_infantry_spawn_specs/prompts/019_infantry_spawn_coding_prompt.md`
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_4_evolution_iii.md`
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_6_derivative_countries.md`
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_8_scenario_interactions_acceptance.md`
- `docs/specs/019_infantry_spawn_specs/review/manual_subagent_role_reviews.md`

Historical evidence banners:

- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_claimant_identity_specialist_reaudit_2026_07_16.md`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_claimant_identity_closure_2026_07_16.md`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_localisation_specialist_final_reaudit_2026_07_16.md`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_parent_implementation_audit_packet_2026_07_15.md`

Those four audit bodies remain unchanged as historical evidence. Their new banners direct readers to this correction.

## Validation evidence

- Localisation retains its UTF-8 BOM.
- The Event 19 English file has 2,751 parsed keys and no duplicate key.
- Exactly 80 claimant name rows exist, with four variants for every slot from 01 through 20.
- All 20 metadata primaries match localisation variant 1.
- The claimant effect contains exactly one `create_corps_commander` path with `female = no` and one exact-ID `is_female = no` proof.
- No Event 19 `female = yes`, `is_female = yes`, or former claimant-female temporary variable remains.
- Stable internal profile IDs remain 1 through 20.
- Region-gate assertions passed for profiles 04, 12, and 20.
- The direct scenario portrait exists and resolves through its registered sprite.
- A refreshed narrow `hoi4.event_inspect` lint request for `chaosx.nr19.200` reached the installed service but could not emit its artifact because the shared MCP artifact store is at its limit. The local source checks above completed independently.

## Intentionally retained compatibility references

The even-slot internal profile enum tokens still use their former personal-name spellings, such as `milena_vargova = 2` and `mara_voss = 20`. The user requested stable internal profile IDs, and these tokens are referenced by regional gates and transfer logic. They are not localisation keys and cannot appear to the player. Their constants-file comment now identifies them as frozen compatibility identifiers.

Asset manifests, portrait binaries, portrait provenance, the portrait crosswalk, and reproduction specifications are owned by the active portrait specialist. They were not edited in this pass. No active gameplay, localisation, current spec, or current identity-metadata surface retains a female claimant presentation.
