# Event 015 route-identity asset manifest

Package date: `2026-07-14`  
Scope: cosmetic-tag flags, institutional leader portraits, advisor portraits, and league emblems for Event 015, *The Utopia Manifesto*

Flag, institutional portrait, and advisor pipeline correction: `2026-07-15`

Current runtime status: all route-identity sprites and character handles are wired. The five League emblems have Ledger consumers, and the Ledger category attaches `utopia_manifesto_ledger_scripted_gui`. Earlier package text that assigns those steps to the parent records the production-time handoff, not an open task.

## Outcome

This package contains a complete route-identity visual set:

- `75` runtime TGA flag files: `25` names at `82x52`, `41x26`, and `10x7`
- `4` runtime institutional leader portrait DDS files at `156x210`
- `16` runtime advisor portrait DDS files at `65x67`, each built from an independent fictional ImageGen portrait master and separate ImageGen dossier-frame and paper/seal overlays
- `5` runtime league-emblem DDS files at `64x64` with real transparency
- individual built-in ImageGen source masters, processed PNGs, package finals, decoded PNGs, comparison/contact sheets, per-file checksum ledgers, and validation evidence

No gameplay, character, localisation, interface, or scripted-GUI file is changed by this package. Exact sprite definitions and character replacements are recorded in `gfx_handoff.md` for the parent implementation pass.

## Source mode and rights

Every active visual is original fictional OpenAI built-in ImageGen output. Flags were generated from text-only heraldic briefs. Institutional leaders are people-free symbolic establishments; bundled vanilla leader portraits were used only to compare tonal hierarchy, painted finish, and small-size readability. Advisor faces are independently generated fictional specialists, while their visible dossier frame and paper/seal are separate generated overlays. No internet image, archival photograph, famous-person likeness, real national flag, real party emblem, or third-party character is present. The source files are recorded as original generated assets without an external attribution requirement.

Prompt evidence is in `prompts/route_identity_prompts.md`, with authoritative handles and the rejection log in `prompts/corrected_flag_and_institutional_prompts_2026_07_15.md`. The active flag package uses `21` separate built-in calls for `21` distinct compositions; only the four documented unsuffixed/canonical pairs are aliases. All four institutional portraits likewise have independent built-in source masters. The three old atlases remain under `source_png/atlases/` only as superseded package history and are not active flag or institutional sources.

## Cosmetic-tag flag inventory

The exact cosmetic-tag tokens were verified from the current Event 015 country/effect/localisation surfaces. The task-mentioned path `common/cosmetic_tags/015_utopia_manifesto_cosmetic_tags.txt` does not exist; the current tag definitions live in `common/countries/cosmetic.txt`.

Arbitrary recipient countries can hold any ideology after a cosmetic tag is applied, so every route has deliberate `democratic`, `communism`, `neutrality`, and `fascism` variants. Each family uses four independent ideology compositions rather than palette-only substitutions. The four original force-ideology routes retain one intentional alias between their unsuffixed file and canonical ideology file; Practical Commonwealth retains its independent unsuffixed lookup and four independent ideology files.

| Runtime flag stem | Visual source | Lookup purpose |
| --- | --- | --- |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH` | byte alias of the democratic composition | unsuffixed engine lookup |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_democratic` | household wreath, lamp, ledger, bridge, wheat, and olive | forced democratic lookup |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_communism` | three-house covenant, provisions, ledger, bridge, keys, and vines | communism lookup |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_neutrality` | household shelter, lamp, sprout, common table, knot, and bridge | neutrality lookup |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_fascism` | storehouse, households, command lamp, clasps, chain, keys, and grain | fascism lookup without real fascist symbols |
| `UTOPIA_MANIFESTO_COUNCIL_UNION` | byte alias of the communism composition | unsuffixed engine lookup |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_communism` | six callings, shared ledger table, and broken cooperative tool-wheel | forced communism lookup |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_democratic` | six vocational chambers, empty table, open doorway, and branches | democratic lookup |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_neutrality` | six registry cabinets, empty table, balance, seal, cord, and keys | neutrality lookup |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_fascism` | fortified vocational register, chained table, lock, keys, and beacon | fascism lookup without real fascist symbols |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA` | byte alias of the neutrality composition | unsuffixed engine lookup |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_neutrality` | standards apparatus around a reservoir settlement, ledger, weights, and bridge | forced neutrality lookup |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_democratic` | compass, three bridged garden neighborhoods, balance, ledger, and open gate | democratic lookup |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_communism` | compass, five settlement nodes, rail, water, plan table, gear, and bridge | communism lookup |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_fascism` | compass and plumb bob locking city, dam, granary, rail, ledger, keys, and weights | fascism lookup without real fascist symbols |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND` | byte alias of the fascism composition | unsuffixed engine lookup |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_fascism` | fortress island, reserve store, beacon, cistern, locks, chain, keys, and emergency causeway | forced fascism lookup |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_democratic` | lighthouse island, granary, civic hall, broken seawalls, open gates, bridge, and harbor | democratic lookup |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_communism` | beacon, granary, cistern, cooperative store, provision ledger, chain, and segmented seawall | communism lookup |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_neutrality` | settled island, balanced seawalls, controlled causeway, ledger, keys, and sea oats | neutrality lookup |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH` | ledger, bridge, lamp, pump, store, garden, road, compass, service nodes, keys, and charter cord | unsuffixed engine lookup |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_democratic` | five borough gates, empty ledger table, lamp, bridge, garden, water, rail, and open gate | democratic-preserving formation |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_communism` | workshop, store, field, rail-water transport, shared ledger table, bridge, and grain | communism-preserving formation |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_fascism` | fortified store, command lamp, sealed ledger, controlled bridge, conduits, keys, and chains | fascism-preserving formation without real fascist symbols |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_neutrality` | lamp, bridge, standards ledger, pump, garden, crate, rail, compass, balance, conduits, and seal | neutrality-preserving formation |

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

Founder/successor sharing is intentional and justified. Each image depicts the durable governing establishment rather than a named person: an empty chamber, route seal, apparatus, ledger, stores, and vacant council furniture. The paired character IDs represent the same institution before and after procedural succession. The successor changes membership or constitutional form while the establishment's visual identity remains continuous, so eight person-specific portraits would misrepresent the script.

Each active portrait is a separate vertical built-in ImageGen symbolic master with its exact dimensions and handle recorded in `asset_records.json`. The official processor uses the full generated canvas, `--source-kind symbolic`, and bundled vanilla references for style comparison only. Per-asset approval metadata is under `metadata/institutional_portraits/`, and each portrait has an individual source/candidate/vanilla comparison sheet under `contact_sheets/institutional_reviews/`. The approved review explicitly excludes people, faces, heads, bodies, hands, crowds, silhouettes, statues, busts, mannequins, framed portraits, photographs, and human shadows.

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

These are sixteen distinct role portraits. The Event 015 sprite registry and character file use the listed handles; the v5 correction preserves every handle and runtime path and replaces only the underlying advisor PNG/DDS presentation.

Each advisor starts from its own vertical fictional OpenAI built-in ImageGen specialist master in `source_png/advisors/`. The final advisor composition is independent of the `156x210` institutional-leader pipeline: every source was reviewed for a viable head-and-shoulders crop and processed through the frozen v5 `retired_advisor_card_processor_REMOVED advisor --source-kind fictional` workflow. The processor composites the generated dark frame and generated paper/paperclip/illegible-note/wax-seal overlays from `.agents/skills/chaos-redux-event-assets/assets/retired_advisor_overlay_kit_REMOVED/`; it only crops, grades, angles, derives alpha shadows, composites, resizes, validates, and exports. It does not draw visible dossier-card artwork. Processor metadata remains immutable pre-approval evidence under `metadata/advisors/`; the independent review decision lives separately in `approvals/advisor_v5_independent_visual_approval_2026_07_16.json`. Per-asset vanilla comparison sheets live under `contact_sheets/advisor_reviews/`.

Fifteen exact portrait masters were retained. The Public Auditor received one built-in ImageGen edit to preserve the full head, face, neck, and upper shoulders in the canonical card crop; its superseded exact master is archived under `rejected_superseded_history/advisor_v5_source_revisions_2026_07_16/`, and the edit handle, prompt, inputs, crop, and hashes are pinned in `advisor_portrait_source_manifest.json`. All sixteen final masters depict visually distinct fictional people, all sixteen processed hashes are unique, and none of the advisor finals was produced by shrinking or padding a leader portrait.

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

- `source_png/atlases/` — superseded historical atlases retained for rejection/history evidence only
- `source_png/flags/` — twenty-one independent built-in ImageGen compositions plus four byte-identical alias source paths
- `source_png/institutional_portraits/` — four independent built-in ImageGen people-free symbolic masters
- `source_png/advisors/` — sixteen independent advisor masters
- `source_png/league_emblems/` — five keyed split masters and five transparent high-resolution masters
- `processed_png/` — exact runtime-sized PNG intermediates
- `final_tga/` and `final_dds/` — package copies of every runtime final
- `decoded_png/` — engine-format files decoded back to PNG for inspection
- `metadata/institutional_portraits/` — symbolic source mode, full generated crop, built-in handle, checksums, vanilla-style comparison, people-free review, and approval for all four institutions
- `metadata/advisors/` — immutable candidate-stage processor inputs, source mode, generated-overlay hashes, reference path, deterministic reconstruction, and nine-band validation for all sixteen advisors
- `approvals/` — producer-independent native-size and 4x visual approval for the exact sixteen-card v5 set
- `contact_sheets/` — decoded, source, native-size, nearest-neighbour, and comparison review sheets
- `asset_records.json` — source/processed/final paths, dimensions, hashes, provenance, and notes for all `100` runtime outputs
- `validation.json` — format, alpha, decode, pixel-equality, count, and distinctness evidence
- `flag_identity_validation_2026_07_15.json` — focused 21-call/4-alias coverage, header, dimension, byte-match, and uniqueness evidence
- `institutional_portrait_validation_2026_07_15.json` — focused source-mode, crop, comparison, DDS, mirror, and decoded-pixel evidence
- `advisor_validation_2026_07_16.json` — immutable full-set candidate reconstruction, source/crop, metadata, comparison, alpha/paper derivation, RGB-support, and nine-band evidence
- `advisor_installed_validation_2026_07_16.json` — post-approval package/runtime DDS hashes and exact decoded-pixel equality for all sixteen installed cards
- `approvals/advisor_v5_independent_visual_approval_2026_07_16.json` — independent per-card approval against the retired_advisor_reference_set_REMOVED vanilla set
- `imagegen_source_evidence_2026_07_15.json` — exact byte-equality proof for all twenty-one flag and four institutional built-in outputs
- `gfx_handoff.md` — ready-to-copy sprite definitions and character replacement map
- `prompts/route_identity_prompts.md` — generation prompt record
- `prompts/corrected_flag_and_institutional_prompts_2026_07_15.md` — active built-in handles, corrected prompt briefs, aliases, and rejection log

## Contact sheets

- `contact_sheets/flags_decoded_contact_sheet.png`
- `contact_sheets/flag_size_ladder_decoded_contact_sheet.png`
- `contact_sheets/flags_corrected_imagegen_source_contact_sheet.png`
- `contact_sheets/flags_corrected_decoded_contact_sheet.png`
- `contact_sheets/flags_corrected_small_10x7_readability_contact_sheet.png`
- `contact_sheets/flag_imagegen_source_normal_medium_small_comparison.png`
- `contact_sheets/ideology_flag_variants_source_contact_sheet.png`
- `contact_sheets/ideology_flag_variants_decoded_contact_sheet.png`
- `contact_sheets/ideology_flag_variants_size_ladder_decoded_contact_sheet.png`
- `contact_sheets/institutional_portraits_decoded_contact_sheet.png`
- `contact_sheets/institutional_portraits_corrected_source_contact_sheet.png`
- `contact_sheets/institutional_portraits_corrected_processed_contact_sheet.png`
- `contact_sheets/institutional_reviews/*_comparison.png`
- `contact_sheets/advisor_portraits_decoded_contact_sheet.png`
- `contact_sheets/advisor_sources_contact_sheet.png`
- `contact_sheets/advisor_portraits_native_contact_sheet.png`
- `contact_sheets/advisor_portraits_enlarged_nearest_contact_sheet.png`
- `contact_sheets/advisor_reviews/*_comparison.png`
- `contact_sheets/league_emblems_decoded_contact_sheet.png`

The decoded contact sheets are built from runtime-format output. The advisor source, native-size, enlarged nearest-neighbour, and per-asset comparison sheets are explicit pipeline-review evidence and are not runtime assets.

## Validation evidence

`validation.json` records `100` validated runtime files:

- all `75` flags are uncompressed 32-bit TGAs with bottom-left origin, correct dimensions, exact file length, and fully opaque alpha
- all `25` DDS files use a one-level uncompressed BGRA layout with the expected masks, dimensions, texture caps, and exact file length
- every TGA and DDS decodes successfully in Pillow
- every decoded file is pixel-identical to its processed PNG
- the five emblem DDS files and sixteen advisor dossier DDS files span alpha `0..255`; the four institutional portraits remain fully opaque
- every advisor DDS is exactly `65x67` and `17,548` bytes with the required legacy one-level BGRA header, transparent outer-corner treatment, and a byte-identical package/runtime mirror
- every advisor DDS decode is pixel-identical to its processed PNG; every source master and processed advisor hash is unique within the sixteen-file family
- all five route families have four unique ideology-variant processed hashes
- all `21` independently generated main-size flag compositions have unique processed hashes and recorded built-in handles
- flag processing retains ImageGen-authored geometry without quantization, tracing, primitive redraw, motif substitution, or a palette ceiling; each output stays inside the source-preservation finishing threshold
- all four people-free symbolic institutional portraits, all sixteen generated-overlay advisor portraits, and all five league emblems are unique within their families
- every institutional metadata record uses `source_kind = symbolic`, the full generated master, a people-free visual review, and a distinct built-in handle
- every advisor metadata record names the generated frame and paper/seal hashes and records that no visible card artwork was drawn programmatically
- the only duplicated flag designs are the four documented unsuffixed/canonical-ideology alias pairs

## Simplifications, omissions, and blockers

- Simplifications: none.
- Fallbacks: none.
- Missing requested visual assets: none.
- Asset-quality blockers: none.
- Integration intentionally remains outside this asset subtask. The advisor correction preserves all sixteen existing handles and runtime paths and therefore requires no `.gfx`, character, gameplay, or localisation edit. The separate league-emblem UI-consumer handoff remains unchanged. Country flags require no sprite registration.
