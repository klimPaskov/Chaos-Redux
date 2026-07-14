# Event 006 static icon manifest

## Production contract

- Scope: ASSET-007 through ASSET-038, the requested Post-Release Instability
  registry-gap icon, and the unblocked portion of ASSET-047.
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
`.agents/skills/chaos-redux-event-assets/assets/achievements/overlay.png`.
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
| ASSET-047 | `chaosx_006_assyria_survives` | mountain, river, and exact sourced Assyrian symbol | **blocked, unproduced** |

### Assyria blocker and reserved filenames

The following names are reserved and must not be filled with a substitute:

- `docs/assets/006_independence_wave/source_png/achievements/chaosx_006_assyria_survives_source.png`;
- `docs/assets/006_independence_wave/processed_png/achievements/chaosx_006_assyria_survives.png`;
- `docs/assets/006_independence_wave/processed_png/achievements/chaosx_006_assyria_survives_grey.png`;
- `docs/assets/006_independence_wave/processed_png/achievements/chaosx_006_assyria_survives_not_eligible.png`;
- matching DDS filenames under `gfx/achievements/`.

Required input before production: one exact, approved Assyrian motif with
community/faction ownership and date documented, plus a decision on whether it is
community-wide, church-specific, Levies-specific, or political-faction-specific.
The post-1968 modern Assyrian flag is not an acceptable 1936 baseline.

## ASSET-046 formable flag and emblem blocker

ASSET-046 is unproduced. The formable registry defines `FORM-01` through
`FORM-48`, but it does not yet bind each family to a final gameplay tag, final
identity motif, approved palette, or stable UI emblem reference. Creating generic
emblems would be a prohibited substitute.

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

Required input per `FORM-*` row: final tag, final public identity, verified or
explicitly alternate-history motif, source/ownership note for any historical or
community symbol, palette, route variants, and the UI sizes that consume the
emblem. Parent implementation must decide whether the league emblem is universal
or charter/route-specific before art begins.

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
motifs, three route-owned real-person portrait DDS files, vanilla reuse
boundaries, provenance and license notes, contact sheets, hashes, and explicit
blockers. Its five Group B motif previews are not runtime flags and remain
separate from generated fictional/civic route art.

## Related northern and western Europe generated-art package

The five fictional Group B civic baseline flag triplets, five fictional
institutional council portraits, five independently generated fictional officer
portraits, army thumbnails, prompts, decoded runtime review sheets, and exact
hash inventory are documented in
`northern_western_europe_generated_art_manifest.md`. ACX and AEX remain blocked
at the country-content layer by geography/anchor ownership even though their art
files are complete. No ideology or cosmetic flag variants were produced without
an approved route mapping.
