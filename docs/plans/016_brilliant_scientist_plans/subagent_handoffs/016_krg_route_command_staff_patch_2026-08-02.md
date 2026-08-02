# Event 016 KRG route command staff patch

Date: 2026-08-02

Status: patch complete; parent review and live formation validation remain outstanding.

## Scope and outcome

This patch closes the Event 016 Kruger State country-package gap for route-specific staff, commanders, and institutional leader candidates without creating a second Kruger identity or a new asset package.

Doctor Warren Kruger remains the central advisor and sovereign character, and `KRG_continuity_network` remains the machine succession character. The new characters are institutional offices with fixed names, male metadata, existing generic scientist portraits, one route-gated high-command role, one corps-commander role, and an unpromoted despotism country-leader role.

## Changed files

- `common/characters/016_brilliant_scientist_characters.txt` adds `KRG_general_staff_office`, `KRG_machine_command_node`, `KRG_clone_officer_corps`, and `KRG_project_command_council`.
- `common/country_leader/016_brilliant_scientist_traits.txt` adds four small, route-specific advisor/leader traits.
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt` adds `brilliant_scientist_krg_reset_command_staff` and makes each `brilliant_scientist_establish_*_command` helper publish one active route flag and call event `chaosx.brilliant_scientist_krg.90`.
- `events/016_brilliant_scientist_kruger_state_events.txt` adds hidden event `chaosx.brilliant_scientist_krg.90` for guarded synchronous recruitment and advisor activation.
- `localisation/english/016_brilliant_scientist_country_l_english.yml` adds names, leader descriptions, trait names, and trait descriptions for the fixed offices.
- No interface file is changed: the four reused generic scientist sprite names are already registered by the vanilla `interface/_scientists_portraits.gfx` shelf, so adding duplicate local sprite definitions would be redundant.
- `docs/events/016_brilliant_scientist/systems/kruger_state_decisions.md` documents the route staff contract and cleanup behavior.

## Country package coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Tag and country definition | Covered and unchanged | `common/country_tags/016_brilliant_scientist_country.txt`; `common/countries/Kruger State KRG.txt` |
| Dormant history and map setup | Covered and unchanged | `history/countries/KRG - Kruger State.txt`; route transfer effects remain parent-owned |
| Route staff, commanders, and leader candidates | Patched | Four fixed characters in `common/characters/016_brilliant_scientist_characters.txt` |
| Route ideas and command lifecycle | Patched at existing helper boundary | `brilliant_scientist_establish_general_staff_command`, `...machine_command`, `...clone_officer_corps`, `...project_council_command` |
| Character recruitment and activation | Patched | `chaosx.brilliant_scientist_krg.90`; one permanent `..._recruited` flag per office |
| Kruger and machine succession | Preserved | No changes to `KRG_warren_kruger`, `KRG_continuity_network`, or `brilliant_scientist_krg_install_machine_continuity_network` |
| Localisation | Patched | Name, leader description, and trait key pairs in `016_brilliant_scientist_country_l_english.yml` |
| Portrait and model assets | Covered by reuse | Existing vanilla scientist sprites `GFX_portrait_generic_europe_male_02`, `...asia_male_01`, `...africa_male_01`, and `...europe_male_03`; no interface or 3D files changed |
| AI behavior | Minimal role preference | Each fixed advisor uses the normal high-command `ai_will_do = { factor = 1.000 }`; route activation remains focus/decision owned |

## Route and identifier matrix

| Route | Command trigger | Active flag | Character | Advisor token | Trait |
| --- | --- | --- | --- | --- | --- |
| Human general staff | `KRG_a_general_staff_for_the_state` through `brilliant_scientist_focus_set_general_staff_command` | `brilliant_scientist_krg_staff_general_active` | `KRG_general_staff_office` | `KRG_general_staff_office` | `brilliant_scientist_krg_general_staff_advisor` |
| Machine command | `KRG_write_the_machine_command_protocol` or event `chaosx.brilliant_scientist_krg.20.a` | `brilliant_scientist_krg_staff_machine_active` | `KRG_machine_command_node` | `KRG_machine_command_node` | `brilliant_scientist_krg_machine_command_advisor` |
| Clone officer corps | Clone route command focus through `brilliant_scientist_focus_set_clone_officer_command` | `brilliant_scientist_krg_staff_clone_active` | `KRG_clone_officer_corps` | `KRG_clone_officer_corps` | `brilliant_scientist_krg_clone_officer_advisor` |
| Project command council | `KRG_a_council_of_project_commanders` through `brilliant_scientist_focus_set_project_council_command` | `brilliant_scientist_krg_staff_council_active` | `KRG_project_command_council` | `KRG_project_command_council` | `brilliant_scientist_krg_project_council_advisor` |

## Before and after behavior

Before the patch, the command helpers only replaced lifecycle ideas, while the foundation roster decision generated unnamed scientists and project coordination rebuilt forces without adding a route-specific command office.

After the patch, each helper first deactivates any previously hired route office and clears all four route-active flags, then applies the existing lifecycle idea, sets exactly one route-active flag, and invokes event `chaosx.brilliant_scientist_krg.90`.

The hidden event recruits the matching fixed character once, marks its permanent `..._recruited` flag, and activates its high-command role. A repeated helper call reactivates an existing office rather than recruiting a duplicate. The corps-commander role is present on the same character immediately after recruitment, and the country-leader role remains unpromoted so Kruger/network succession is unchanged.

## Politics, portraits, parties, and leaders

All four new characters use institutional names rather than personal random-name pools. All are explicitly male because the reused portraits are male-presenting. No country leader is created dynamically and no existing party or ruling leader is replaced. The candidate leader roles use `ideology = despotism` and are inert unless a later route explicitly promotes one.

The new traits are intentionally modest: general staff adds planning and organization, machine command adds planning and supply efficiency, clone officers add organization/training/army experience, and project council adds command-power generation, decryption, and organization. None duplicates Kruger's +100% research-speed identity trait.

## Map, military, technology, industry, supply, and AI

No state ownership, controller, core, capital, victory point, railway, port, resource, building, starting OOB, equipment, technology, production, or supply file was changed. Commander skills are bounded at 3–4 and use existing vanilla unit-leader traits. The high-command roles cost 0 because the route focus/decision already owns the command-lifecycle commitment; the permanent recruitment guard prevents free duplicate offices.

The AI receives no new world iteration or country scan. Existing route focus and decision AI selects the command lifecycle; the activated advisor remains available at normal high-command priority. Parent-owned scenario checks are still needed to confirm that each route receives the office after formation and that succession still leaves Kruger/network in charge.

## Asset and localisation contract

No new DDS, portrait source, model, entity, interface, or animation was created. The four character entries reuse generic scientist DDS files already present in the vanilla `gfx/leaders/scientists/generic_scientists/` shelf through its stable `GFX_portrait_generic_*` sprite names.

All new character, leader-description, trait, and trait-description keys are in the UTF-8-BOM file `localisation/english/016_brilliant_scientist_country_l_english.yml`.

## Validation performed

- Read the required offline Paradox wiki pages and relevant vanilla documentation before editing.
- Confirmed all four character IDs, advisor tokens, traits, active flags, recruited flags, and event `chaosx.brilliant_scientist_krg.90` are unique with repository-wide `rg` scans.
- Confirmed all four generic portrait GFX names resolve in vanilla `interface/_scientists_portraits.gfx`; no new interface or asset path is referenced.
- Confirmed the four existing command helper call sites in focus and event sources still resolve to the patched helpers.
- Confirmed the localisation file retains its UTF-8 BOM after editing.
- Read-only `hoi4.event_inspect` lint for selector `{ kind: event, eventId: chaosx.brilliant_scientist_krg.90 }` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, no blocking diagnostics, and the rerun artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06ba289ae164a8cddace18a243f605732cb074456cbab63d56324ceacb5916d6/eeb931e92bdee8b826079495c8662ab0582a64cc45ad8617fce9e2b1cb96aad1/event-lint-139c181b58b5.json`.
- No Hearts of Iron IV process was launched, and no live formation, focus, advisor, commander, or succession claim is made here.

## Remaining risks and parent checks

- Parent should run a focused Event 016 formation scenario for each command route and confirm the hidden event fires after route selection, the correct high-command role is active, and only one route office is hired.
- Parent should confirm that `activate_advisor` succeeds immediately after `recruit_character` in the live build; the structure follows the vanilla documentation and Event 006 hidden roster precedent.
- Parent should review whether the unpromoted despotism candidate leader roles should remain in a later political-route pass; they are inert in this patch and do not alter current succession.
- The installed package exposes no Technology Tree Viewer, so technology-tree validation remains unresolved and outside this country patch.

No gameplay fallback, placeholder identity, opposite-gender portrait/name pairing, duplicate Kruger role, new 3D asset, or map rewrite was introduced.
