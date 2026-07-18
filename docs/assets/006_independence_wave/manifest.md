# Event 006 static icon manifest

## Production contract

- Scope: ASSET-007 through ASSET-038, the requested Post-Release Instability
  registry-gap icon, the researched FORM-01 through FORM-04 child packages of
  ASSET-046 and ASSET-048, and the unblocked portion of ASSET-047.
- Source mode: built-in `$imagegen`; generated masters are project-controlled and
  contain no third-party image material.
- Source masters: `docs/assets/006_independence_wave/source_png/`.
- Processed masters: `docs/assets/006_independence_wave/processed_png/`.
- Final runtime files: `gfx/interface/goals/006_independence_wave/`,
  `gfx/interface/ideas/006_independence_wave/`,
  `gfx/interface/decisions/006_independence_wave/`, and `gfx/achievements/`.
- Exact SHA-256 hashes for every delivered source, processed PNG, and runtime DDS
  are recorded in `_tooling/icon_build_report.json`.
- Generation prompts and sensitive-source constraints are recorded in
  `prompts/006_icon_prompts.md`.

The focus rows are family-level baseline icons because the accepted specification
defines thirteen focus icon families. They are not a claim that every individual
focus has unique art.

## Focus icon families

All final files are 94x86 uncompressed BGRA DDS with alpha. For each row,
`source_png/focuses/<stem>_source.png` is the source,
`processed_png/focuses/<stem>.png` is the processed master, and
`gfx/interface/goals/006_independence_wave/<stem>.dds` is the final file.

| Asset ID | Stable stem / proposed sprite | Intended use | Status |
|---|---|---|---|
| ASSET-007 | `goal_independence_wave_founding_administration` / `GFX_goal_independence_wave_founding_administration` | survival and founding-administration focuses | final, handed off |
| ASSET-008 | `goal_independence_wave_constitutional_state` / `GFX_goal_independence_wave_constitutional_state` | constitutional route | final, handed off |
| ASSET-009 | `goal_independence_wave_popular_councils` / `GFX_goal_independence_wave_popular_councils` | council route | final, handed off |
| ASSET-010 | `goal_independence_wave_traditional_restoration` / `GFX_goal_independence_wave_traditional_restoration` | traditional route | final, handed off |
| ASSET-011 | `goal_independence_wave_military_emergency` / `GFX_goal_independence_wave_military_emergency` | military route | final, handed off |
| ASSET-012 | `goal_independence_wave_patron_client` / `GFX_goal_independence_wave_patron_client` | client route | final, handed off |
| ASSET-013 | `goal_independence_wave_recognition_diplomacy` / `GFX_goal_independence_wave_recognition_diplomacy` | diplomacy route | final, handed off |
| ASSET-014 | `goal_independence_wave_army_integration` / `GFX_goal_independence_wave_army_integration` | military branch | final, handed off |
| ASSET-015 | `goal_independence_wave_infrastructure_authority` / `GFX_goal_independence_wave_infrastructure_authority` | economy branch | final, handed off |
| ASSET-016 | `goal_independence_wave_former_host_settlement` / `GFX_goal_independence_wave_former_host_settlement` | former-host route | final, handed off |
| ASSET-017 | `goal_independence_wave_league_congress` / `GFX_goal_independence_wave_league_congress` | league branch | final, handed off |
| ASSET-018 | `goal_independence_wave_regional_formable` / `GFX_goal_independence_wave_regional_formable` | formable branch | final, handed off |
| ASSET-019 | `goal_independence_wave_high_chaos_sovereignty` / `GFX_goal_independence_wave_high_chaos_sovereignty` | radical branch | final, handed off |

## Idea icon families

All final files are 64x64 uncompressed BGRA DDS with alpha. For each row,
`source_png/ideas/<stem>_source.png` is the source,
`processed_png/ideas/<stem>.png` is the processed master, and
`gfx/interface/ideas/006_independence_wave/<stem>.dds` is the final file.

| Asset ID | Stable stem / proposed sprite | Intended use | Status |
|---|---|---|---|
| ASSET-020 | `idea_independence_wave_improvised_government` / `GFX_idea_independence_wave_improvised_government` | Improvised Government lifecycle | final, handed off |
| ASSET-021 | `idea_independence_wave_unrecognized_state` / `GFX_idea_independence_wave_unrecognized_state` | Unrecognized State lifecycle | final, handed off |
| ASSET-022 | `idea_independence_wave_fragmented_command` / `GFX_idea_independence_wave_fragmented_command` | Fragmented Command lifecycle | final, handed off |
| ASSET-023 | `idea_independence_wave_unsettled_borders` / `GFX_idea_independence_wave_unsettled_borders` | Unsettled Borders lifecycle | final, handed off |
| ASSET-024 | `idea_independence_wave_patron_pressure` / `GFX_idea_independence_wave_patron_pressure` | Patron Pressure lifecycle | final, handed off |
| ASSET-025 | `idea_independence_wave_league_membership` / `GFX_idea_independence_wave_league_membership` | league membership lifecycle | final, handed off |
| ASSET-026 | `idea_independence_wave_founding_identity` / `GFX_idea_independence_wave_founding_identity` | founding identity lifecycle | final, handed off |
| Registry gap | `idea_independence_wave_post_release_instability` / `GFX_idea_independence_wave_post_release_instability` | Post-Release Instability | final, handed off; add an ASSET ID before registry closure |

The Post-Release Instability row was requested under a stable implementation name
after the accepted asset-family registry was written. It does not currently have
an ASSET ID; the parent must reconcile the registry rather than silently folding it
into a different family.

## Decision and mission icon families

All final files are 32x32 uncompressed BGRA DDS with alpha. For each row,
`source_png/decisions/<stem>_source.png` is the source,
`processed_png/decisions/<stem>.png` is the processed master, and
`gfx/interface/decisions/006_independence_wave/<stem>.dds` is the final file.

| Asset ID | Stable stem / proposed sprite | Intended use | Status |
|---|---|---|---|
| ASSET-027 | `decision_independence_wave_recognition_actions` / `GFX_decision_independence_wave_recognition_actions` | recognition actions | final, handed off |
| ASSET-028 | `decision_independence_wave_government_actions` / `GFX_decision_independence_wave_government_actions` | government actions | final, handed off |
| ASSET-029 | `decision_independence_wave_army_integration_actions` / `GFX_decision_independence_wave_army_integration_actions` | army integration actions | final, handed off |
| ASSET-030 | `decision_independence_wave_depot_border_actions` / `GFX_decision_independence_wave_depot_border_actions` | depot and border actions | final, handed off |
| ASSET-031 | `decision_independence_wave_former_host_negotiations` / `GFX_decision_independence_wave_former_host_negotiations` | former-host negotiations | final, handed off |
| ASSET-032 | `decision_independence_wave_patron_aid` / `GFX_decision_independence_wave_patron_aid` | patron aid | final, handed off |
| ASSET-033 | `decision_independence_wave_patron_balancing` / `GFX_decision_independence_wave_patron_balancing` | patron balancing | final, handed off |
| ASSET-034 | `decision_independence_wave_network_aid` / `GFX_decision_independence_wave_network_aid` | network aid | final, handed off |
| ASSET-035 | `decision_independence_wave_league_votes` / `GFX_decision_independence_wave_league_votes` | league votes | final, handed off |
| ASSET-036 | `decision_independence_wave_border_arbitration` / `GFX_decision_independence_wave_border_arbitration` | border arbitration | final, handed off |
| ASSET-037 | `decision_independence_wave_formable_proclamation` / `GFX_decision_independence_wave_formable_proclamation` | formable proclamation | final, handed off |
| ASSET-038 | `decision_independence_wave_integration_missions` / `GFX_decision_independence_wave_integration_missions` | integration missions | final, handed off |

## Achievement icon triplets

Every delivered achievement has:

- `source_png/achievements/<id>_source.png`;
- `processed_png/achievements/<id>.png`, `<id>_grey.png`, and
  `<id>_not_eligible.png`;
- `gfx/achievements/<id>.dds`, `<id>_grey.dds`, and
  `<id>_not_eligible.dds`.

All achievement files are 64x64 uncompressed BGRA DDS with alpha. The grey state
is derived from the accepted completed icon. The not-eligible state uses the exact
approved overlay from
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png`.
Achievement files are engine-discovered by exact filename and do not need
`spriteType` registration.

| Asset ID | Achievement ID | Source direction | Status |
|---|---|---|---|
| ASSET-047 | `chaosx_006_one_state_to_statehood` | small state becoming sovereign statehood | final triplet, handed off |
| ASSET-047 | `chaosx_006_no_master` | severed puppet control | final triplet, handed off |
| ASSET-047 | `chaosx_006_peace_with_host` | signed former-host border | final triplet, handed off |
| ASSET-047 | `chaosx_006_break_reconquest` | capital surviving encirclement | final triplet, handed off |
| ASSET-047 | `chaosx_006_found_league` | founding congress and charter | final triplet, handed off |
| ASSET-047 | `chaosx_006_cross_regional_league` | globe and varied blank pennants | final triplet, handed off |
| ASSET-047 | `chaosx_006_rescue_member` | shields protecting a member state | final triplet, handed off |
| ASSET-047 | `chaosx_006_regional_formable` | fused civic seals over river and rail | final triplet, handed off |
| ASSET-047 | `chaosx_006_volga_bulgaria` | river and documented Bolgar-inspired architecture; no ancient-flag claim | final triplet, handed off |
| ASSET-047 | `chaosx_006_small_to_major` | small state casting major-power shadow | final triplet, handed off |
| ASSET-047 | `chaosx_006_radical_bloc` | opened borders and activated radical bloc | final triplet, handed off |
| ASSET-047 | `chaosx_006_every_flag_survival` | clock ringed by solid blank pennants | final triplet, handed off |
| ASSET-047 | `chaosx_006_balanced_patrons` | three patrons held in balance | final triplet, handed off |
| ASSET-047 | `chaosx_006_league_arbitrator` | peaceful multi-border arbitration council | final triplet, handed off |
| ASSET-047 | `chaosx_006_host_remnant` | protected surviving former-host remnant | final triplet, handed off |
| ASSET-047 | `chaosx_006_assyria_survives` | mountain, river, and exact sourced Assyrian symbol | **final triplet, reviewed, runtime-installed in the IW-043/IW-058 static icon package** |

### Assyria package record and preserved exclusion

The Assyria triplet is final and must not be replaced with a substitute. The
authoritative package record is
`docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/manifest.md`;
its visual and DDS audits are in that package's `validation/validation_report.md`
and `validation/dds_audit.json`.

The delivered source and processed/runtime paths are:

- `docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/source_png/achievements/achievement_chaosx_006_assyria_survives_source.png`;
- `docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/processed_png/achievements/chaosx_006_assyria_survives.png`;
- `docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/processed_png/achievements/chaosx_006_assyria_survives_grey.png`;
- `docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/processed_png/achievements/chaosx_006_assyria_survives_not_eligible.png`;
- matching runtime DDS files under `gfx/achievements/` in the package handoff.

The package preserves the approved motif and ownership/date record. The
post-1968/1973 modern Assyrian flag remains excluded from the 1936 baseline.
Final art does not by itself expose the signature achievement; its proof writer
and adapter-attestation gates remain fail-closed in gameplay.

## ASSET-046 formable flags and remaining emblem coverage

ASSET-046 is partially produced for the four researched formable families that
currently have operational implementations:

- `FORM-01` Celtic Congress: `KCX`;
- `FORM-02` North Atlantic Union: `NUX`;
- `FORM-03` Confederation of the Low Countries: cosmetic identity `LCX`;
- `FORM-04` Rhenish League: `RLX`.

The generated source masters, processed ladders, final runtime TGAs, prompts,
provenance, review sheets, validation, and checksums are recorded in:

- `docs/assets/006_independence_wave/form01_02_04_flags_2026_07_15/`;
- `docs/assets/006_independence_wave/low_countries_form03_2026_07_15/`.

`KCX`, `NUX`, and `RLX` use one accepted ImageGen-authored design per tag and
have explicit, byte-identical ideology filename aliases at normal, medium, and
small sizes. `LCX` is a cosmetic identity whose accepted shared base ladder is
resolved through its carrier. No route recolour or locally redrawn flag art was
introduced.

The remaining `FORM-05` through `FORM-48` flag identities and the per-family UI
emblem set remain blocked until each family has a final gameplay tag, public
identity, researched motif, approved palette, and stable UI consumer. Creating
generic emblems would be a prohibited substitute.

Reserved stable naming contract after those inputs are approved:

- standard flag triplets: `gfx/flags/<TAG>.tga`,
  `gfx/flags/medium/<TAG>.tga`, and `gfx/flags/small/<TAG>.tga`, where every new
  formable tag ends in `X`;
- UI emblem texture per immutable registry ID:
  `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_01.dds`
  through `independence_wave_formable_form_48.dds`;
- matching sprites:
  `GFX_independence_wave_formable_form_01` through
  `GFX_independence_wave_formable_form_48`;
- league emblem texture:
  `gfx/interface/006_independence_wave/emblems/independence_wave_league_emblem.dds`;
- league sprite: `GFX_independence_wave_league_emblem`.

Required input for every unresolved `FORM-*` row remains: final tag, final public
identity, verified or explicitly alternate-history motif, source/ownership note
for any historical or community symbol, palette, route variants, and the UI
sizes that consume the emblem. Parent implementation must decide whether the
league emblem is universal or charter/route-specific before that art begins.

## ASSET-048 regional report variants

The researched FORM-03 child deliverable is produced and wired:

- source and review package:
  `docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/`;
- detailed requirement-to-runtime row:
  `docs/assets/006_independence_wave/low_countries_form03_progression/report_scene/submanifest.md`;
- runtime texture:
  `gfx/event_pictures/006_independence_wave/report_event_006_form03_charter_convention.dds`;
- sprite: `GFX_report_event_006_form03_charter_convention` in
  `interface/006_independence_wave_event_pictures.gfx`;
- consumers: `chaosx.nr6.300` through `chaosx.nr6.308`.

The report scene is a built-in ImageGen alternate-history constitutional and
engineering congress, processed as a 210x176 report card. Its runtime DDS has
real alpha and a pixel-identical decoded review. The remaining regional report
variants stay readiness-controlled and require their package-specific scene,
consumer list, and provenance before production; the FORM-03 scene is not a
substitute for those rows.

## ASSET-040 through ASSET-043: outside the static tranche

These assets require real frame sequences plus static fallbacks and are routed to
`chaos-redux-frame-animation`. They were deliberately not represented by a moved,
scaled, rotated, blurred, recolored, or filtered still image.

| Asset | Reserved static sprite | Reserved animated sprite | Missing production inputs |
|---|---|---|---|
| ASSET-040 recognition seal | `GFX_independence_wave_recognition_seal_static` | `GFX_independence_wave_recognition_seal_animated` | locked GUI size, frame count/rate, state sequence for recognition feedback, authored source frames |
| ASSET-041 dependency warning | `GFX_independence_wave_dependency_warning_static` | `GFX_independence_wave_dependency_warning_animated` | locked GUI size, warning states, frame count/rate, authored source frames |
| ASSET-042 league charter activation | `GFX_independence_wave_league_charter_activation_static` | `GFX_independence_wave_league_charter_activation_animated` | locked GUI size, charter activation beats, frame count/rate, authored source frames |
| ASSET-043 formable eligibility seal | `GFX_independence_wave_formable_eligibility_seal_static` | `GFX_independence_wave_formable_eligibility_seal_animated` | locked GUI size, discovery/eligibility states, frame count/rate, authored source frames |

Each animation handoff must include separate generated, sourced, or provided
source frames; processed frames or sheet; static fallback; manifest; contact
sheet; preview; and `.gfx`/`.gui` wiring notes. Implementation-defined target
sizes in the accepted registry must be resolved before production.

## Review artifacts

- `contact_sheets/006_icon_focuses_contact_sheet.png`
- `contact_sheets/006_icon_ideas_contact_sheet.png`
- `contact_sheets/006_icon_decisions_contact_sheet.png`
- `contact_sheets/006_icon_achievements_contact_sheet.png`
- `contact_sheets/006_icon_dds_decoded_contact_sheet.png`

The final DDS decode sheet was built by reopening the actual runtime DDS files,
not by reusing the processed PNGs.

## Related country-package source manifest

The bounded IW-001 through IW-010 plus IW-012 northern/western Europe source
package is documented separately in
`northern_western_europe_source_manifest.md`. It contains sourced historical
motifs, two approved route-owned real-person portrait DDS files, vanilla reuse
boundaries, provenance and license notes, contact sheets, hashes, and explicit
blockers. Its historical symbol references are retained as provenance inputs or
overlay evidence according to the package-specific handoff.

## Related northern and western Europe generated-art package

`northern_western_europe_generated_art_manifest.md` is the current authority
only for the ACX, AFX, AGX, and AJX generated historical-design flag triplets
and their flag comparisons. Its former portrait, commander-small, and portrait
completion claims are superseded and are not portrait evidence. AEX remains a
vanilla `BEL_flanders` overlay and has no standalone Event 006 flag family.

## 2026-07-16 male HOI4 portrait authority

The current portrait source of truth is
`portrait_regeneration_male_hoi4_2026_07_16/manifest.md`, together with the
production handoff
`../../plans/006_independence_wave_plans/subagent_handoffs/006_event6_male_hoi4_portrait_regeneration_2026_07_16.md`
and the independent final audit
`../../plans/006_independence_wave_plans/subagent_handoffs/006_event6_male_hoi4_portrait_final_independent_audit_2026_07_16.md`.
The audited package contains twenty distinct male `156x210` fictional portraits
and ten matching `65x67` commander-small dossiers under the existing runtime
filenames. The twenty-four textures for AFX, AGX, AJX, BAY, BRI, RHI, SCO, and
WLS retain their existing registrations and consumers. The six ACX and AEX
textures are installed readiness-pool art only and deliberately have no live
sprite or character consumer.

The two user-approved historical portraits remain unchanged and hash-locked:

- `portrait_BAY_rupprecht_of_bavaria.dds`;
- `portrait_RHI_josef_friedrich_matthes.dds`.

The authoritative runtime checksum ledger is
`portrait_regeneration_male_hoi4_2026_07_16/hashes/runtime_sha256_inventory.sha256`;
the package's merged visual review and final independent audit govern visual
acceptance. Every 2026-07-15 fictional portrait, BRI portrait, mixed NWE
portrait, and army-small package is historical and superseded for portrait
files, hashes, and approval. `generated_nwe_hashes.sha256` is not portrait
authority. Custom Event 006 advisor icons remain withdrawn: gameplay advisor
offices have no custom Event 006 portrait cards, sprite registrations, or
runtime DDS files.

## 2026-07-15 AJX neutral-commission focus handoff

The current IW-010 Saar focus source of truth is
`ajx_asset_completion_2026_07_15/manifest.md`. It contains one original
`94x86` Municipal Neutral Commission focus icon without changing Friedrich
Hoffmann, Karl Becker, or either approved RHI/BAY historical leader portrait.

The installed runtime file is
`gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds`.
Its exact prompt, source, processing, contact-sheet, decoded-DDS, metadata, and
SHA-256 contracts remain in the focus-only package. Custom Event 006 advisor
icons and their sprite registrations were removed by explicit user direction;
the gameplay offices remain asset-neutral.

## 2026-07-16 BRI portrait disposition

IW-004 Brittany's current fictional civic, commander-large, and
commander-small evidence is part of
`portrait_regeneration_male_hoi4_2026_07_16/manifest.md` and the independent
final audit named above. Existing BRI filenames, sprite registrations, and
gameplay consumers remain stable; the 2026-07-15 BRI portrait package and its
small-card evidence are superseded.

The package reuses the installed vanilla BRI Gwenn-ha-du flag and historical
political portraits. François Debeauvais remains explicitly blocked because
the available portrait candidates lack both adequate identity detail and a
defensible United States public-domain basis. No Debeauvais asset or generated
likeness is wired. The accepted fictional BRI civic portrait does not clear or
replace that historical-person rights blocker, and portrait presence does not
grant runtime content attestation or SCN008 scenario-preflight readiness.

## 2026-07-18 FORM-48 Pacific visual-asset handoff

This section is the later authority for `FORM-48` and supersedes the older
“remaining FORM-05 through FORM-48” blocked statement only for this one family.
The accepted Pacific plan now supplies the stable `HBX` California carrier,
`PFX` federal identity, researched motifs, palette, and FORM-48 UI-emblem
contract.

The bounded production package is
`form48_pacific_assets_2026_07_17/`. It contains official ImageGen sources,
the public-domain California reference, direct research links and rights notes,
exact prompts, no-dither flat masters, processed PNG ladders, two review sheets,
full validation, checksums, and a parent wiring handoff. The `HBX` source and
runtime ladder were corrected to retain the historically attested
`CALIFORNIA REPUBLIC` legend; the prior textless adaptation is superseded.

Delivered runtime finals:

- complete `HBX` and `PFX` base plus democratic, communism, fascism, and
  neutrality ladders at 82x52, 41x26, and 10x7 under `gfx/flags/`;
- `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_48.dds`;
- proposed stable sprite `GFX_independence_wave_formable_form_48`.

All 30 TGAs are flat, opaque, uncompressed 32-bit bottom-left-origin files and
decode exactly to their processed PNGs. Within each tag and size, the five
ideology filenames are intentionally byte-identical constitutional/civic
identity aliases. `HBX` and `PFX` remain visually and bytewise distinct.

The emblem texture is installed and validated but is not registered or consumed
by this asset-only tranche. Parent implementation owns the `PFX` cosmetic/formable
wiring, the sprite registration, and the live FORM-48 UI consumer. No portrait,
advisor icon, BAY/RHI protected portrait, gameplay, localisation, registry,
`.gfx`, or `.gui` file was changed by the HBX correction.
