# IW-043 and IW-058 country-core implementation handoff

Date: 2026-07-18

Owner lane: `/root/iw043_iw058_country_core`

Status: bounded country-core implementation complete; package runtime attestation remains false

## Implemented surfaces

### Institutional characters and exact-package recruitment

- Added eight accepted institutional character records in `common/characters/006_independence_wave_iw043_iw058_characters.txt`.
- Parent integration review rejected standalone CHU and ASY history roster files because they would override the vanilla carrier histories rather than load additively.
- The architecture lane owns guarded `recruit_character` calls inside the exact IW-043 and IW-058 institutional-surface effects, immediately before the matching country-leader role is added.
- Every character has `gender = male`, one stable future large civilian portrait consumer, and no role or recruitment at load.
- No character defines an advisor, advisor idea token, advisor icon, advisor portrait, small portrait, army portrait, commander, or officer role.
- No female portrait candidate or character is present. The portrait handoff is limited to eight separately authored all-male institutional group images.
- Excluded real-person tokens `CHU_gerasim_ivanov`, `ASY_shimun_eshai`, and `ASY_benjamin_arsanis` are not referenced.

The architecture lane owns exact-package setup and route effects. Its agreed role payload is:

| Character | Ideology | Trait |
|---|---|---|
| `CHU_independence_wave_middle_volga_congress` | `centrism` | `iw043_middle_volga_congress_trait` |
| `CHU_independence_wave_federal_presidium` | `centrism` | `iw043_federal_presidium_trait` |
| `CHU_independence_wave_bolgar_civic_presidium` | `conservatism` | `iw043_bolgar_civic_presidium_trait` |
| `CHU_independence_wave_river_security_directorate` | `despotism` | `iw043_river_security_directorate_trait` |
| `ASY_independence_wave_provisional_national_council` | `centrism` | `iw058_provisional_national_council_trait` |
| `ASY_independence_wave_concordat_council` | `conservatism` | `iw058_concordat_council_trait` |
| `ASY_independence_wave_civic_national_assembly` | `centrism` | `iw058_civic_national_assembly_trait` |
| `ASY_independence_wave_levies_guardianship` | `despotism` | `iw058_levies_guardianship_trait` |

Architecture must use `add_country_leader_role` with `promote_leader = yes` only inside the exact package and route hooks. It must not add a static role to the character definitions or select a vanilla carrier leader.

### Traits, ideas, and AI

- Added eight substantial institutional leader traits in `common/country_leader/006_independence_wave_iw043_iw058_traits.txt`.
- Added the complete IW-043 and IW-058 three-slot idea vocabulary in `common/ideas/006_independence_wave_iw043_iw058_ideas.txt`.
- Froze `independence_wave_iw043_emergency_river_guard_idea` with the decision lane as the IW-043 emergency defense-slot replacement.
- Froze `independence_wave_iw058_mesopotamian_federal_settlement_idea` and `independence_wave_iw058_sovereign_autonomy_compact_idea` as the two late IW-058 institutional-slot replacements.
- Added sixteen exact-package-gated AI profiles in `common/ai_strategy/006_independence_wave_iw043_iw058_ai_strategy.txt` for founding policy, reserve recovery, tracked crisis defense, all six main routes, civilian normalization, and both IW-058 settlement modes.
- AI profiles use no country target, world scan, war generator, subject instruction, periodic on-action, or formable bypass. All profiles abort when their exact enable gate stops being true.
- All country-core modifier and AI values use the architecture-owned `independence_wave_iw043` and `independence_wave_iw058` script-constant categories. This lane did not edit or overwrite the shared constants file.

Route odds, action reserves, command ceilings, identity guarantees, consent, guarantor scoring, and formable choice remain the responsibility of the package decisions and their `ai_will_do` blocks. The strategy file supplies persistent production, construction, restraint, crisis, and normalization behavior only.

### Localisation and documentation

- Added UTF-8 BOM English localisation in `localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml`.
- Covered all eight character names and biographies, eight traits, nineteen ideas, route parties and long names, accepted cosmetic names/definitions/adjectives, and sixteen AI profile labels.
- IW-058 text preserves distinct Assyrian, Chaldean, Syriac, and Aramean self-identification and does not present one church as the identity of every community.
- Added the bounded system document `docs/systems/006_independence_wave_iw043_iw058_signature_packages.md` with character, idea, AI, identity, and asset-consumer handoff sections.

## Stable future asset consumers

The character file references eight large civilian portrait sprite IDs:

- `GFX_portrait_CHU_independence_wave_middle_volga_congress`
- `GFX_portrait_CHU_independence_wave_federal_presidium`
- `GFX_portrait_CHU_independence_wave_bolgar_civic_presidium`
- `GFX_portrait_CHU_independence_wave_river_security_directorate`
- `GFX_portrait_ASY_independence_wave_provisional_national_council`
- `GFX_portrait_ASY_independence_wave_concordat_council`
- `GFX_portrait_ASY_independence_wave_civic_national_assembly`
- `GFX_portrait_ASY_independence_wave_levies_guardianship`

The idea file references six stage-icon families:

- `GFX_idea_independence_wave_iw043_congress`
- `GFX_idea_independence_wave_iw043_river_economy`
- `GFX_idea_independence_wave_iw043_river_guard`
- `GFX_idea_independence_wave_iw058_council`
- `GFX_idea_independence_wave_iw058_corridor`
- `GFX_idea_independence_wave_iw058_diaspora`

These are handoff consumers only. This lane created no DDS, PNG, GFX, GUI, advisor asset, advisor sprite, or fallback asset reference, and did not touch BAY/RHI files.

## Coordination contracts

- Architecture confirmed exact triggers for package identity, safe action reserve, tracked severe crisis, anchor security, and civilian normalization.
- Architecture owns `common/script_constants/006_independence_wave_iw043_iw058_constants.txt` and agreed the flat idea, leader, and AI key set consumed here.
- Architecture owns guarded dynamic role hooks `independence_wave_apply_iw043_institutional_surface` and `independence_wave_apply_iw058_institutional_surface`.
- The decision/event lane confirmed the emergency guard and two Mesopotamian settlement idea IDs above and owns their swap call sites.
- Party localisation keys and dynamic leader role payloads were sent directly to architecture.

## Meaningful validation evidence

- Eight character records were counted, with eight male declarations, eight large civilian portraits, and zero country-leader, advisor, commander, or officer roles in their definitions.
- Nineteen ideas were counted and all nineteen carry the correct exact-package `allowed` trigger.
- Sixteen AI profiles were counted, all sixteen carry the exact package trigger in `enable`, and all sixteen use `abort_when_not_enabled = yes`.
- The AI file contains no targeted-country strategy type.
- Every `constant:independence_wave_iw043.*` and `constant:independence_wave_iw058.*` reference resolves to the current architecture-owned constants file.
- Localisation retains its UTF-8 BOM and has no duplicate key in the dedicated file.
- No excluded real-person token appears in the implementation.

## Simplifications, omissions, and blockers

- No design simplification was introduced inside the assigned country-core scope.
- Final portraits, idea icons, and GFX registration are intentionally absent because they belong to the asset lane. The package must remain runtime unattested until those exact consumers resolve.
- Dynamic role assignment, party swaps, idea lifecycle swaps and cleanup, and route-choice `ai_will_do` logic are integration dependencies owned by architecture and decisions/events. This handoff records their exact contracts but does not patch those files.
- The runtime package cannot be declared complete from this lane alone. Full country-package, decision, AI, localisation, asset, and Event 006 completion audits remain required before admission.

No commit was created.
