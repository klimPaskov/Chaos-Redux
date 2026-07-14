# Event 015 route-identity asset handoff

Handoff date: `2026-07-14`  
Role: `chaosx_icon_artist`  
Scope: Event 015 cosmetic-tag flags, institutional leader portraits, advisor portraits, league emblems, source/processed/final packages, validation, and exact GFX handoff only

## Outcome

The requested route-identity visual package is complete:

- five cosmetic-tag flag families are installed at normal, medium, and small HOI4 sizes
- four fixed-ideology lookup files are also installed for the four routes that force ideology
- four compositionally distinct Practical Commonwealth ideology variants are installed because that route preserves the forming country's ideology
- four institutional group portraits are installed for the exact existing leader GFX handles
- sixteen distinct advisor portraits are installed to replace all current idea-icon stand-ins
- five distinct league emblems are installed under the stable sprite IDs supplied by the country-package handoff
- source masters, processed PNGs, package DDS/TGA finals, runtime files, decoded PNGs, contact sheets, prompt evidence, checksum records, and format validation are preserved

No interface, character, gameplay, scripted GUI, or localisation file was edited. The exact parent-owned wiring is ready in `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/gfx_handoff.md`.

## Installed flag families

Exact cosmetic-tag stems:

1. `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH`
2. `UTOPIA_MANIFESTO_COUNCIL_UNION`
3. `UTOPIA_MANIFESTO_PLANNED_UTOPIA`
4. `UTOPIA_MANIFESTO_CLOSED_ISLAND`
5. `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH`

Every runtime stem has an `82x52` file in `gfx/flags/`, a `41x26` file in `gfx/flags/medium/`, and a `10x7` file in `gfx/flags/small/`.

Lookup coverage:

- Voluntary Commonwealth: base plus `_democratic`
- Council Union: base plus `_communism`
- Planned Utopia: base plus `_neutrality`
- Closed Island: base plus `_fascism`
- Practical Commonwealth: base plus `_democratic`, `_communism`, `_fascism`, and `_neutrality`

The first four base/suffix pairs intentionally share their route visual because their formation effects force that ideology. The four Practical Commonwealth ideology files use different symbols and layouts—not recolors—because that route preserves current ideology. The base Practical flag is a fifth separate design.

The task-referenced `common/cosmetic_tags/015_utopia_manifesto_cosmetic_tags.txt` does not exist in the workspace. Exact tags were verified from `common/countries/cosmetic.txt`, the Event 015 identity effects, and localisation.

## Institutional leaders

| Existing handle | Runtime DDS | Sharing decision |
| --- | --- | --- |
| `GFX_portrait_utopia_manifesto_household_assembly` | `gfx/leaders/015_utopia_manifesto/leader_household_assembly.dds` | Household Assembly and Commonwealth Council |
| `GFX_portrait_utopia_manifesto_council_of_callings` | `gfx/leaders/015_utopia_manifesto/leader_council_of_callings.dds` | Council of Callings and Rotating Congress |
| `GFX_portrait_utopia_manifesto_board_of_measure` | `gfx/leaders/015_utopia_manifesto/leader_board_of_measure.dds` | Board of Measure and College of Measure |
| `GFX_portrait_utopia_manifesto_stewardship_council` | `gfx/leaders/015_utopia_manifesto/leader_stewardship_council.dds` | Stewardship Council and Directorate of Service |

Four portraits are the correct design rather than a simplification. Each is a multi-person institutional body portrait, and the existing founder/successor pairs model the same durable governing institution through a procedural succession. Eight portraits would falsely turn those bodies into person-specific leaders and weaken the intended institutional identity.

## Advisor portraits

Installed under `gfx/leaders/015_utopia_manifesto/advisors/`:

- `advisor_utopia_manifesto_interpreter.dds`
- `advisor_utopia_manifesto_general_provisioner.dds`
- `advisor_utopia_manifesto_secretary_of_callings.dds`
- `advisor_utopia_manifesto_surveyor_of_shores.dds`
- `advisor_utopia_manifesto_civic_engineer.dds`
- `advisor_utopia_manifesto_keeper_of_stores.dds`
- `advisor_utopia_manifesto_league_envoy.dds`
- `advisor_utopia_manifesto_advocate_of_limits.dds`
- `advisor_utopia_manifesto_public_auditor.dds`
- `advisor_utopia_manifesto_constitutional_jurist.dds`
- `advisor_utopia_manifesto_council_organizer.dds`
- `advisor_utopia_manifesto_social_workshop_planner.dds`
- `advisor_utopia_manifesto_chief_surveyor.dds`
- `advisor_utopia_manifesto_standards_engineer.dds`
- `advisor_utopia_manifesto_steward_of_service.dds`
- `advisor_utopia_manifesto_contract_broker.dds`

All sixteen are distinct, role-specific civilian portraits. `gfx_handoff.md` supplies the sixteen new `GFX_portrait_utopia_manifesto_<token>_small` definitions and the exact character-entry replacement table.

## League emblems

| Stable sprite ID | Runtime DDS |
| --- | --- |
| `GFX_utopia_manifesto_household_congress_emblem` | `gfx/interface/015_utopia_manifesto/league_emblems/household_congress_emblem.dds` |
| `GFX_utopia_manifesto_congress_of_common_tables_emblem` | `gfx/interface/015_utopia_manifesto/league_emblems/congress_of_common_tables_emblem.dds` |
| `GFX_utopia_manifesto_network_directorate_emblem` | `gfx/interface/015_utopia_manifesto/league_emblems/network_directorate_emblem.dds` |
| `GFX_utopia_manifesto_island_hierarchy_emblem` | `gfx/interface/015_utopia_manifesto/league_emblems/island_hierarchy_emblem.dds` |
| `GFX_utopia_manifesto_plural_compact_emblem` | `gfx/interface/015_utopia_manifesto/league_emblems/plural_compact_emblem.dds` |

The five related country flags already exist in `common/scripted_effects/015_utopia_manifesto_identity_effects.txt`. No current Event 015 UI consumer maps those flags to art. The parent must add the five sprite definitions and connect the correct handle to the intended league/ledger/country-details UI. No fallback consumer was invented.

## Asset package and evidence

Canonical package: `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/`

Important files:

- `manifest.md` — complete asset inventory, sharing rationale, runtime paths, provenance, and validation summary
- `gfx_handoff.md` — twenty-five ready-to-copy sprite definitions and sixteen character replacements
- `prompts/route_identity_prompts.md` — generation prompt record
- `asset_records.json` — per-output source/processed/final dimensions and SHA-256 values
- `validation.json` — full runtime-format and distinctness results
- `contact_sheets/flags_decoded_contact_sheet.png`
- `contact_sheets/flag_size_ladder_decoded_contact_sheet.png`
- `contact_sheets/institutional_portraits_decoded_contact_sheet.png`
- `contact_sheets/advisor_portraits_decoded_contact_sheet.png`
- `contact_sheets/league_emblems_decoded_contact_sheet.png`

The package retains `3` frozen source atlases, `9` flag masters, `4` split institutional portrait masters, `16` advisor masters, and keyed plus transparent high-resolution masters for all `5` league emblems. Processed and decoded PNGs exist for every runtime output.

The shared root file `docs/assets/015_utopia_manifesto/manifest.md` was deliberately left untouched because the concurrent final event-art producer owns that surface. This route-identity package is self-contained and can be linked or merged into the root manifest by the parent after both handoffs land.

## Meaningful validation

`64` runtime files were validated:

- `39` uncompressed bottom-left-origin 32-bit TGA flags at exact normal/medium/small dimensions
- `4` uncompressed one-level BGRA institutional portrait DDS files at `156x210`
- `16` uncompressed one-level BGRA advisor portrait DDS files at `64x64`
- `5` uncompressed one-level BGRA league emblem DDS files at `64x64`, with alpha spanning `0..255`

Every runtime file decoded successfully and was pixel-identical to its processed PNG. File lengths, DDS masks/caps, TGA origin and bit depth, dimensions, and alpha ranges match the required contracts. Hash-based family checks confirmed four distinct Practical Commonwealth ideology variants, four distinct institutional portraits, sixteen distinct advisor portraits, and five distinct league emblems. The four documented fixed-ideology flag aliases are the only intended duplicates.

The contact sheets were assembled from decoded runtime files and visually inspected at full resolution. Faces remain legible at advisor size, institutional scenes remain distinct, emblem alpha edges are clean, and all flag designs survive the `10x7` reduction.

## Parent integration checklist

1. Add the four existing leader, sixteen new advisor, and five stable league `spriteType` entries from `gfx_handoff.md` to `interface/015_utopia_manifesto.gfx`.
2. Replace the sixteen `GFX_idea_...` advisor `small` handles in `common/characters/015_utopia_manifesto_characters.txt` with the supplied portrait handles.
3. Connect each stable league-emblem sprite to the intended current UI surface using the five existing route-state flags.
4. Link or merge this dedicated package into the shared Event 015 asset manifest after concurrent asset work is reconciled.
5. Include the runtime assets and package evidence in the parent Event 015 audit/commit.

## Files changed by this subagent

- `gfx/flags/UTOPIA_MANIFESTO_*.tga` — thirteen base-level runtime names
- `gfx/flags/medium/UTOPIA_MANIFESTO_*.tga` — thirteen medium runtime names
- `gfx/flags/small/UTOPIA_MANIFESTO_*.tga` — thirteen small runtime names
- `gfx/leaders/015_utopia_manifesto/*.dds` — four institutional portraits
- `gfx/leaders/015_utopia_manifesto/advisors/*.dds` — sixteen advisor portraits
- `gfx/interface/015_utopia_manifesto/league_emblems/*.dds` — five league emblems
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/**` — source, processed, package-final, decoded, contact-sheet, prompt, manifest, GFX-handoff, checksum, and validation evidence
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/route_identity_asset_handoff.md` — this handoff

## Skills and references used

- `chaos-redux-event-assets` — source mode, prompt/provenance, runtime format, alpha, manifest, contact-sheet, and handoff requirements
- `chaos-redux-subagents` — bounded ownership and parent-integration handoff rules
- `imagegen` — original fictional advisor and ideology-variant flag generation plus chroma-key workflow

The required offline Paradox wiki core pages were consulted along with Country Creation, Cosmetic Tag Modding, Portrait Modding, Graphical Asset Modding, Interface Modding, and Scripted GUI Modding. Vanilla character documentation and installed flag/portrait precedents were also inspected. No skill was created or updated; no reusable workflow gap beyond the existing asset skill was found.

## Simplifications, omissions, and blockers

- Simplifications: none.
- Fallbacks: none.
- Missing requested assets: none.
- Unresolved asset blocker: none.
- Parent-owned integration still required: GFX registration, advisor reference replacement, and league UI consumption, as listed above.
- Commit: not created; the parent owns the integrated Event 015 commit and concurrent untracked Event 015 work is present in the shared tree.
