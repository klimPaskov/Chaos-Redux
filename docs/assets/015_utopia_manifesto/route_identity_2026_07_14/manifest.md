# Event 015 route-identity asset manifest

Package date: `2026-07-14`  
Scope: cosmetic-tag flags, institutional leader portraits, advisor portraits, and league emblems for Event 015, *The Utopia Manifesto*

## Outcome

This package contains a complete route-identity visual set:

- `75` runtime TGA flag files: `25` names at `82x52`, `41x26`, and `10x7`
- `4` runtime institutional leader portrait DDS files at `156x210`
- `16` runtime advisor portrait DDS files at `64x64`
- `5` runtime league-emblem DDS files at `64x64` with real transparency
- frozen image-generation masters, split source masters, processed PNGs, package finals, decoded PNGs, contact sheets, a per-file checksum ledger, and validation evidence

No gameplay, character, localisation, interface, or scripted-GUI file is changed by this package. Exact sprite definitions and character replacements are recorded in `gfx_handoff.md` for the parent implementation pass.

## Source mode and rights

Every visual is original fictional OpenAI `image_gen` output. No internet image, archival photograph, uploaded reference, famous-person likeness, real national flag, real party emblem, or third-party character was used. The source files are therefore recorded as original generated assets without an external attribution requirement.

Prompt evidence is in `prompts/route_identity_prompts.md`. The three pre-existing frozen atlases are copied into `source_png/atlases/`, and every split or independently generated master is preserved in `source_png/`. The twelve ideology-completion masters were generated in twelve separate `image_gen` calls from their route's frozen base master, preserving each route motif while changing composition as well as palette.

## Cosmetic-tag flag inventory

The exact cosmetic-tag tokens were verified from the current Event 015 country/effect/localisation surfaces. The task-mentioned path `common/cosmetic_tags/015_utopia_manifesto_cosmetic_tags.txt` does not exist; the current tag definitions live in `common/countries/cosmetic.txt`.

Arbitrary recipient countries can hold any ideology after a cosmetic tag is applied, so every route has deliberate `democratic`, `communism`, `neutrality`, and `fascism` variants. Each family uses four independent ideology compositions rather than palette-only substitutions. The four original force-ideology routes retain one intentional alias between their unsuffixed file and canonical ideology file; Practical Commonwealth retains its existing unsuffixed fallback and four independent ideology files.

| Runtime flag stem | Visual source | Lookup purpose |
| --- | --- | --- |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH` | voluntary commonwealth atlas master | unsuffixed fallback |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_democratic` | same voluntary master | forced democratic lookup |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_communism` | communal row and shared foundation | communism lookup |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_neutrality` | sheltered civic diamond | neutrality lookup |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_fascism` | stepped hierarchy and guarding braces | fascism lookup without real fascist symbols |
| `UTOPIA_MANIFESTO_COUNCIL_UNION` | council union atlas master | unsuffixed fallback |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_communism` | same council master | forced communism lookup |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_democratic` | open chamber and incomplete civic wreath | democratic lookup |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_neutrality` | balanced register rows | neutrality lookup |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_fascism` | work tools behind a command chevron | fascism lookup without real fascist symbols |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA` | planned utopia atlas master | unsuffixed fallback |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_neutrality` | same planned master | forced neutrality lookup |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_democratic` | survey compass over open civic frames | democratic lookup |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_communism` | survey compass over common table and five nodes | communism lookup |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_fascism` | survey compass locked into a vertical monument | fascism lookup without real fascist symbols |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND` | closed island atlas master | unsuffixed fallback |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_fascism` | same closed-island master | forced fascism lookup |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_democratic` | separated gateway brackets around the island | democratic lookup |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_communism` | equal boundary segments on a shared base | communism lookup |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_neutrality` | balanced arcs and controlled channel | neutrality lookup |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH` | plural commonwealth atlas master | unsuffixed fallback |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_democratic` | open arches, lamp, and bridge | democratic-preserving formation |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_communism` | delegates at a shared table | communism-preserving formation |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_fascism` | broken enclosure and open lamp-door | fascism-preserving formation without real fascist symbols |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_neutrality` | crossing bands, bridge, and lamp | neutrality-preserving formation |

For every stem above, the installed paths are:

- `gfx/flags/<stem>.tga` — `82x52`
- `gfx/flags/medium/<stem>.tga` — `41x26`
- `gfx/flags/small/<stem>.tga` — `10x7`

Package mirrors are under `final_tga/flags/`, processed PNGs under `processed_png/flags/`, and verified decodes under `decoded_png/flags/`.

## Institutional leader portraits

| Existing GFX handle | Runtime DDS | Existing character consumers |
| --- | --- | --- |
| `GFX_portrait_utopia_manifesto_household_assembly` | `gfx/leaders/015_utopia_manifesto/leader_household_assembly.dds` | `utopia_manifesto_household_assembly`, `utopia_manifesto_commonwealth_council` |
| `GFX_portrait_utopia_manifesto_council_of_callings` | `gfx/leaders/015_utopia_manifesto/leader_council_of_callings.dds` | `utopia_manifesto_council_of_callings`, `utopia_manifesto_rotating_congress` |
| `GFX_portrait_utopia_manifesto_board_of_measure` | `gfx/leaders/015_utopia_manifesto/leader_board_of_measure.dds` | `utopia_manifesto_board_of_measure`, `utopia_manifesto_college_of_measure` |
| `GFX_portrait_utopia_manifesto_stewardship_council` | `gfx/leaders/015_utopia_manifesto/leader_stewardship_council.dds` | `utopia_manifesto_stewardship_council`, `utopia_manifesto_directorate_of_service` |

Founder/successor sharing is intentional and justified. Each image is an institutional group portrait—not a named individual—and the current paired character IDs represent the same durable governing body before and after a procedural succession. The successor changes membership or constitutional form while the visual identity remains the body, so creating eight nominally different portraits would imply person-specific leaders that the script does not model.

## Advisor portrait inventory

| Character ID | New GFX handle | Runtime DDS |
| --- | --- | --- |
| `utopia_manifesto_interpreter` | `GFX_portrait_utopia_manifesto_interpreter_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_interpreter.dds` |
| `utopia_manifesto_general_provisioner` | `GFX_portrait_utopia_manifesto_general_provisioner_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_general_provisioner.dds` |
| `utopia_manifesto_secretary_of_callings` | `GFX_portrait_utopia_manifesto_secretary_of_callings_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_secretary_of_callings.dds` |
| `utopia_manifesto_surveyor_of_shores` | `GFX_portrait_utopia_manifesto_surveyor_of_shores_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_surveyor_of_shores.dds` |
| `utopia_manifesto_civic_engineer` | `GFX_portrait_utopia_manifesto_civic_engineer_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_civic_engineer.dds` |
| `utopia_manifesto_keeper_of_stores` | `GFX_portrait_utopia_manifesto_keeper_of_stores_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_keeper_of_stores.dds` |
| `utopia_manifesto_league_envoy` | `GFX_portrait_utopia_manifesto_league_envoy_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_league_envoy.dds` |
| `utopia_manifesto_advocate_of_limits` | `GFX_portrait_utopia_manifesto_advocate_of_limits_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_advocate_of_limits.dds` |
| `utopia_manifesto_public_auditor` | `GFX_portrait_utopia_manifesto_public_auditor_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_public_auditor.dds` |
| `utopia_manifesto_constitutional_jurist` | `GFX_portrait_utopia_manifesto_constitutional_jurist_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_constitutional_jurist.dds` |
| `utopia_manifesto_council_organizer` | `GFX_portrait_utopia_manifesto_council_organizer_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_council_organizer.dds` |
| `utopia_manifesto_social_workshop_planner` | `GFX_portrait_utopia_manifesto_social_workshop_planner_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_social_workshop_planner.dds` |
| `utopia_manifesto_chief_surveyor` | `GFX_portrait_utopia_manifesto_chief_surveyor_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_chief_surveyor.dds` |
| `utopia_manifesto_standards_engineer` | `GFX_portrait_utopia_manifesto_standards_engineer_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_standards_engineer.dds` |
| `utopia_manifesto_steward_of_service` | `GFX_portrait_utopia_manifesto_steward_of_service_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_steward_of_service.dds` |
| `utopia_manifesto_contract_broker` | `GFX_portrait_utopia_manifesto_contract_broker_small` | `gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_contract_broker.dds` |

These are sixteen distinct role portraits. They replace the current idea-icon stand-ins only after the parent adds the sprite definitions and updates the corresponding `small =` values in `common/characters/015_utopia_manifesto_characters.txt`.

## League emblem inventory

| League model | Stable GFX handle | Runtime DDS |
| --- | --- | --- |
| Household Congress | `GFX_utopia_manifesto_household_congress_emblem` | `gfx/interface/015_utopia_manifesto/league_emblems/household_congress_emblem.dds` |
| Congress of Common Tables | `GFX_utopia_manifesto_congress_of_common_tables_emblem` | `gfx/interface/015_utopia_manifesto/league_emblems/congress_of_common_tables_emblem.dds` |
| Network Directorate | `GFX_utopia_manifesto_network_directorate_emblem` | `gfx/interface/015_utopia_manifesto/league_emblems/network_directorate_emblem.dds` |
| Island Hierarchy | `GFX_utopia_manifesto_island_hierarchy_emblem` | `gfx/interface/015_utopia_manifesto/league_emblems/island_hierarchy_emblem.dds` |
| Plural Compact | `GFX_utopia_manifesto_plural_compact_emblem` | `gfx/interface/015_utopia_manifesto/league_emblems/plural_compact_emblem.dds` |

The emblems are visually related to the route flags but are not miniature flag copies: each is a separate enamel-and-metal institutional badge with a transparent background and a route-specific silhouette.

## Package map

- `source_png/atlases/` — frozen original flag, institutional portrait, and league-emblem atlases
- `source_png/flags/` — five split base flag masters and sixteen independent ideology masters
- `source_png/institutional_portraits/` — four split institutional masters
- `source_png/advisors/` — sixteen independent advisor masters
- `source_png/league_emblems/` — five keyed split masters and five transparent high-resolution masters
- `processed_png/` — exact runtime-sized PNG intermediates
- `final_tga/` and `final_dds/` — package copies of every runtime final
- `decoded_png/` — engine-format files decoded back to PNG for inspection
- `contact_sheets/` — decoded review sheets
- `asset_records.json` — source/processed/final paths, dimensions, hashes, provenance, and notes for all `100` runtime outputs
- `validation.json` — format, alpha, decode, pixel-equality, count, and distinctness evidence
- `ideology_flag_variant_validation.json` — focused coverage, header, dimension, byte-match, and uniqueness evidence for all five route families
- `ideology_flag_variant_checksums.sha256` — SHA-256 ledger for the ideology-completion sources and package/runtime derivatives
- `gfx_handoff.md` — ready-to-copy sprite definitions and character replacement map
- `prompts/route_identity_prompts.md` — generation prompt record

## Contact sheets

- `contact_sheets/flags_decoded_contact_sheet.png`
- `contact_sheets/flag_size_ladder_decoded_contact_sheet.png`
- `contact_sheets/ideology_flag_variants_source_contact_sheet.png`
- `contact_sheets/ideology_flag_variants_decoded_contact_sheet.png`
- `contact_sheets/ideology_flag_variants_size_ladder_decoded_contact_sheet.png`
- `contact_sheets/institutional_portraits_decoded_contact_sheet.png`
- `contact_sheets/advisor_portraits_decoded_contact_sheet.png`
- `contact_sheets/league_emblems_decoded_contact_sheet.png`

Every contact sheet is built from decoded runtime-format output, not from source art.

## Validation evidence

`validation.json` records `100` validated runtime files:

- all `75` flags are uncompressed 32-bit TGAs with bottom-left origin, correct dimensions, exact file length, and fully opaque alpha
- all `25` DDS files use a one-level uncompressed BGRA layout with the expected masks, dimensions, texture caps, and exact file length
- every TGA and DDS decodes successfully in Pillow
- every decoded file is pixel-identical to its processed PNG
- the five emblem DDS files span alpha `0..255`; all portraits are fully opaque
- all five route families have four unique ideology-variant processed hashes
- all twelve added main-size ideology designs have unique processed hashes
- all four institutional portraits, all sixteen advisor portraits, and all five league emblems are unique within their families
- the only duplicated flag art is the four documented unsuffixed/canonical-ideology alias pairs

## Simplifications, omissions, and blockers

- Simplifications: none.
- Fallbacks: none.
- Missing requested visual assets: none.
- Asset-quality blockers: none.
- Integration intentionally left to the parent because this subtask forbids interface and gameplay edits: register the `25` portrait/emblem sprite handles, replace the `16` advisor `small` portrait references, and connect the five league handles to their UI consumer. Country flags require no sprite registration.
