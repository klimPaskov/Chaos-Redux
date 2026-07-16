# Event 006 Mediterranean asset and provenance inventory

Date: 2026-07-16
Scope: IW-017 Corsica (`COR`), IW-018 Sardinia (`ARX`), IW-019 Sicily
(`ASX`), and FORM-05 Mediterranean Island League
Mode: read-only asset/provenance audit; no asset, gameplay, localisation, or
sprite file was changed

## Verdict

None of the four audited packages is visually complete in the current working
tree.

| Package | Flag state | Portrait state | Icon state | Asset verdict |
|---|---|---|---|---|
| IW-017 `COR` | Registered vanilla flag family is present and technically valid; no local override | Three live portrait sprite consumers have no source, DDS, or registration | Six ideas do not have final package art; two custom decision sprites are absent; shared Level 1 focus families are available | blocked on portraits and icons |
| IW-018 `ARX` | Valid ImageGen-authored base triplet is installed; no ideology/route variants; provenance ledger has a migrated-reference hash defect | Four live portrait sprite consumers have no source, DDS, or registration | Six ideas do not have final package art; two custom decision sprites are absent; shared Level 1 focus families are available | blocked on portraits, icons, route coverage, and provenance repair |
| IW-019 `ASX` | Valid ImageGen-authored triplet is installed, but the design is constitutional-independence-route-only while occupying the unsuffixed base filenames | Four live portrait sprite consumers have no source, DDS, or registration | Seven ideas do not have final package art; three custom decision sprites are absent; required Level 2 country-specific focus group/assets do not yet exist | blocked; unsuffixed flag must not be treated as a neutral baseline |
| FORM-05 | No final tag, flag, emblem, source package, or sprite exists; source of truth remains fail-closed | No formable-transition portrait asset is defined | Three lifecycle ideas lack final art and one live decision sprite is absent | intentionally blocked pending identity decisions |

The current Mediterranean character, idea, decision, and decision-category
files are in-flight untracked files. This inventory records their exact live
consumers as seen in the shared working tree and should be rerun after parent
integration if those identifiers change.

## Governing requirements used

- The accepted country registry assigns `COR` and `ARX` Level 1 and `ASX`
  Level 2. Level 1 requires dynamic leadership plus complete flag and
  localisation coverage. Level 2 additionally requires a country-specific
  focus group, a bespoke decision family, distinctive assets, and a unique
  leader/institution path.
- The accepted visual specification requires coordinated 94x86 focus families,
  distinct 64x64 idea art for lifecycle and route institutions, distinct 32x32
  decision art, complete 82x52/41x26/10x7 flag ladders, generated fictional
  portraits, sourced real-person portraits, and no Event 6 custom advisor
  portrait icons.
- `chaos-redux-event-assets` is stricter than the older specification wording
  for institutional portraits: a council, assembly, congress, board, or office
  must use a people-free symbolic/institutional image and an institutional
  name. This satisfies the Event 6 male-only direction without inventing a
  collective of human subjects.
- Every **new** final flag, including a historical reconstruction, must retain
  official ImageGen source evidence. A historical design also requires a cited
  design source and a recorded geometry/colour/symbol comparison. Reusing an
  unchanged registered vanilla flag is not production of a new flag.
- No fallback or generic substitute is authorized. A missing consumer remains
  a blocker until final art or an explicitly approved existing-family mapping
  is recorded.

Primary accepted sources:

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`
- `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv`
- `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`

## Flag inventory

### IW-017 Corsica / `COR`

`COR` remains a registered vanilla tag at
`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:206`:

```text
COR = "countries/Corsica.txt"
```

There is no local `gfx/flags/COR*.tga` override. The mod therefore inherits the
vanilla family below. All files are 32-bit uncompressed TGA and bottom-origin.
The normal and medium files use descriptor `8`; the vanilla 10x7 files use
descriptor `0`.

| Vanilla path below `gfx/` | Dimensions | SHA-256 |
|---|---:|---|
| `flags/COR.tga` | 82x52 | `c44349f916978ec247da3019dc5c4e5ef44e5d33b996a46beaf88b1f907abc89` |
| `flags/COR_democratic.tga` | 82x52 | `87cc04ee4132f3865800b05c72da9a940286cf72236ae5a370ab20108badd95d` |
| `flags/COR_communism.tga` | 82x52 | `31bf0f27dff9d93e74fd6b030ce1054cef581f9bdeb532da3d4b012bfe3c7951` |
| `flags/COR_fascism.tga` | 82x52 | `6ebe36a2d2abf048cdc22823a51ba20348a6e4c92986cdc99cd718374b6666d2` |
| `flags/medium/COR.tga` | 41x26 | `ebc264e7637fb5f08fb967239d1757316c8a22cc4de1887844f4090adcbc3618` |
| `flags/medium/COR_democratic.tga` | 41x26 | `b81df8251372270058e03e4fa1ea8710697448239df8a21508130a69e4a1c1a5` |
| `flags/medium/COR_communism.tga` | 41x26 | `e067dbf60d80ad2cef5594a235c06d0c45a764ce5a1cde3baf2945edc3e93ebe` |
| `flags/medium/COR_fascism.tga` | 41x26 | `f8ac3c42c0608e74493b712885da75d73301286a51be6903cad6f16fdfedb1d8` |
| `flags/small/COR.tga` | 10x7 | `a650224c0f58f868139c2ec3fa96779afe693571f0ebbf2f094a28e054e1ddbb` |
| `flags/small/COR_democratic.tga` | 10x7 | `a7aac1bffc20ab2943cc2eb3a1dcf177cc327c5c097ca4941f950cbbf1331ea1` |
| `flags/small/COR_communism.tga` | 10x7 | `c66ef6c814291c8cb999f6255b3d44c44bd672d17dd3dccdb48636bdbc0f26e1` |
| `flags/small/COR_fascism.tga` | 10x7 | `682077de48f9458f22ed0c04a6d4fb0b563b9af056a2402720e1662b59ca8d0e` |

This is valid registered-base reuse under the accepted research resolution. It
does not create an ImageGen obligation. It also does not authorize a custom
Corsican route flag: any new route/cosmetic identity still needs its own
historical ownership case, cited reference, ImageGen flat master, and complete
TGA ladder.

The vanilla `history/countries/COR - Corsica.txt` contains no leader or portrait
definition. There is therefore no verified vanilla leader asset to reuse for
the new Mediterranean character package.

### IW-018 Sardinia / `ARX` and IW-019 Sicily / `ASX`

The source/research packet is:

`docs/assets/006_independence_wave/mediterranean_danube_flag_sources_2026_07_15/`

Its retained design evidence is correctly provenance-recorded:

| Package | Retained research image | Dimensions | License / use boundary | SHA-256 |
|---|---|---:|---|---|
| `ARX` | `source_images/sardinia_gelre_armorial_folio_62r.png` | 1496x2190 | CC BY-SA 4.0; KBR/Nitosane; dated motif evidence, not a 1936 state flag | `08bcb6dc4f0735686659db04431f19ab88f131e50fad96a60c4e8c343111566d` |
| `ARX` | `source_images/sardinia_traditional_four_moors_reference.png` | 2560x1716 | CC0; modern geometry aid only | `d2f2008022eda62ea9be23d360c1ddcfcacc95ae976fd81f62b5c311a539f03c` |
| `ASX` | `source_images/sicily_1848_national_flag_reference.svg` | viewBox 3000x2000 | CC BY-SA 4.0; modern layout aid controlled by the Ministry S.015 object record | `f5f7c72dc612749c2028217c897a047f60a07812d7f5088e4737b538991a67a8` |

Research conclusions are correctly bounded:

- `ARX` is an explicitly fictional 1936 Sardinian civic synthesis based on the
  attested Four Moors motif. It is not an attested 1936 sovereign Sardinian
  flag and must never be documented as one. The retained design uses one red St
  George cross, four inward-facing black heads, forehead bands, and visible
  eyes; Savoy/SPM identity is excluded.
- `ASX` is a normalized flat reconstruction of the surviving 1848 S.015
  constitutional-independence colour: vertical green/ecru/red with one all-gold
  Trinacria. Its exact historical ratio and Trinacria rotation were unresolved
  in the accessible object metadata, so the normalization is disclosed. It is
  not evidence for a neutral, Bourbon/Two Sicilies crown, labor, military,
  fascist, or patron-client baseline.

The generated package is:

`docs/assets/006_independence_wave/mediterranean_danube_generated_flags_2026_07_15/`

Both retained final designs satisfy the new-flag ImageGen provenance rule. The
exact prompts, ordered inputs, original official ImageGen output paths, selected
copies, and rejected outputs are recorded in `prompts/imagegen_prompts.md`.

| Package | Retained official ImageGen copy | Dimensions | SHA-256 |
|---|---|---:|---|
| `ARX` | `source_png/ARX_sardinia_four_moors_imagegen_raw.png` | 1536x1024 | `284e9c0d308a62ef1ea19beb80b5a8f8e97b812e1026e9bea237ec4141edcffc` |
| `ARX` | `source_png/ARX_sardinia_four_moors_imagegen_flat_master.png` | 1536x1024 | `73fd77ee69f1b37dafa80309183b2de470b0f3d3398435c255cf9fd45317f2de` |
| `ASX` | `source_png/ASX_sicily_1848_s015_imagegen_raw.png` | 1536x1024 | `e52afc6d064ddd20d8acf5e112e5b6e02e932440ac83c7311214f267f4fbef36` |
| `ASX` | `source_png/ASX_sicily_1848_s015_imagegen_flat_master.png` | 1536x1024 | `617992ae27926f78ff201de965d56cb61a1129bd3812eb47114dd09fc89a03db` |

The final review sheets are also retained:

| Review sheet | Dimensions | SHA-256 |
|---|---:|---|
| `contact_sheets/006_mediterranean_danube_imagegen_raw_vs_flat_contact_sheet.png` | 1560x502 | `0ed839ab90e60e20ac661bc0886647d43815eee5d753322e1fcb12702bcad520` |
| `contact_sheets/006_mediterranean_danube_final_tga_ladders_contact_sheet.png` | 1350x522 | `53b291509d848d4937ada0b262918e2362fc452c471155e821545b82a0510369` |

Direct runtime inspection found correct dimensions, 32-bit uncompressed TGA,
descriptor `8`, bottom origin, and exact agreement with the package ledger for
all six files:

| Runtime path | Dimensions | SHA-256 |
|---|---:|---|
| `gfx/flags/ARX.tga` | 82x52 | `5d5f9b3a06d21d5add2d281e3535fb0caa1f30c75e256f91a4b51f06822a38cd` |
| `gfx/flags/medium/ARX.tga` | 41x26 | `ea71b628d991cf55de36ca7a1f15fb23ec7725472f5bb1df6e3c28f5040f241d` |
| `gfx/flags/small/ARX.tga` | 10x7 | `141711b581113a7ceeddefe688b84414409abeda9df6f34b501e93ad2d0b2bda` |
| `gfx/flags/ASX.tga` | 82x52 | `075949cf85ca8a382922e97a087c09ad0350575a64197763995122789f5151af` |
| `gfx/flags/medium/ASX.tga` | 41x26 | `aebdb7cf57aef5ad88249c2cef1291346bc2a7ea808ca1129846d851218f2613` |
| `gfx/flags/small/ASX.tga` | 10x7 | `a3b970f6a2b27080a3a375c34142b733f64fe11bd4cc444cb6f5e424bd09a99e` |

Country flags are discovered by exact filename and need no `.gfx`
registration. `ARX` and `ASX` are registered at
`common/country_tags/006_independence_wave_countries.txt:20-21`, so the
unsuffixed files are not merely dormant documentation assets.

#### Route and coverage blockers

- Only unsuffixed `ARX` and `ASX` triplets exist. No ideology or cosmetic-route
  filenames exist.
- The `ARX` base art is marked `handed_off`, but the package still needs an
  explicit route-to-flag decision before claiming complete multi-route flag
  coverage. A base flag silently serving every route is not proof that the
  accepted distinct-route design obligation was fulfilled.
- The `ASX` art is marked `needs_user_review`. Because it is currently installed
  under the unsuffixed base filenames on a registered tag, the parent must do
  one of the following before `ASX` can spawn: restrict the tag identity to the
  constitutional-independence route; assign the S.015 art to an approved
  cosmetic identity and commission a researched neutral baseline; or keep the
  package unavailable. No Bourbon, modern red/yellow, generic ideology, or
  recolour substitute is authorized.

#### Generated-package hash-ledger defect

The in-flight migration of prompt/reference paths from the retired
`assets/flags/` directory to the canonical `assets/vanilla_reference/flags/`
directory changed path strings but left three legacy SHA-256 values. As a
result, `hashes.sha256` currently fails against all three migrated technical
reference inputs:

| Canonical reference path | Ledger SHA-256 | Current file SHA-256 |
|---|---|---|
| `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/normal/arm_uk.png` | `69b612800eb642be2004ccf1ae263fc014ce555f6c0204eff6b607962308b38c` | `0852be44f8f75579b9677904673c6ca254158a33da6b680df96d55b28ffbb9e9` |
| `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/normal/arg_gen_nazism_party.png` | `07007cca92ff9f8a6544858a985aed5a6133a4f5e313dbd7169ea4ee491951e9` | `cbb5400e93cb0aacaa82193eb4555ba70619bdaa1f0c0198f0fc556ae7a432ac` |
| `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/normal/anu_fascism.png` | `aec2babab5bced21a7665583118307446cd5f10d3d3895e39ff7a93359d5cc34` | `b0633149ca295792b63561638db340f7bcab4ad22a21179963781350b1a1b243` |

The first two rows are the ARX/ASX technical presentation references. The third
belongs to ICX but shares the same generated package. The final flag source and
runtime hashes still match; this is a provenance-ledger integrity defect, not a
pixel defect. Repair must either retain the exact legacy inputs under an
auditable frozen path or update the migrated reference records to the actual
canonical bytes and explain that the original generation inputs differed. A
path-only rewrite with stale hashes must not be accepted.

### FORM-05 Mediterranean Island League

The accepted formable registry defines the political direction, but not the
asset identity:

- working identity: Mediterranean Island League;
- eligible direction: Corsica, Sardinia, Sicily, and compatible islands;
- method: league transformation through a maritime congress;
- new tag rule: any new tag must end in `X`.

No FORM-05 flag TGA, final tag, source PNG, generated master, contact sheet,
emblem DDS, or sprite registration exists. This matches the current source of
truth, which keeps FORM-05 through FORM-48 fail-closed until each has a final
tag, public identity, researched motif, approved palette, route map, and stable
consumer.

Reserved names after approval are:

- `gfx/flags/<TAG>.tga`, `gfx/flags/medium/<TAG>.tga`, and
  `gfx/flags/small/<TAG>.tga`;
- `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds`;
- `GFX_independence_wave_formable_form_05`.

The presence of three FORM-05 lifecycle ideas and a
`GFX_decision_independence_wave_form05_maritime_congress` consumer in in-flight
gameplay does not unlock art production. The final tag, public identity, motif,
palette, route ownership, and emblem use must be settled first.

## Portrait inventory

`common/characters/006_independence_wave_mediterranean_characters.txt` contains
eleven live custom portrait sprite consumers. Exact searches found no matching
source master, processed PNG, runtime DDS, `.gfx` registration, manifest row,
or review sheet for any of them.

The stable runtime convention should follow the existing Event 6 portrait
package: all large and army-small files under
`gfx/leaders/006_independence_wave/`, with a dedicated Mediterranean portrait
`.gfx` file registering each exact sprite.

| Package / role | Live sprite | Required runtime path | Target | Current state |
|---|---|---|---:|---|
| `COR` people-free municipal congress | `GFX_portrait_COR_independence_wave_municipal_congress` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_municipal_congress.dds` | 156x210 | absent/unregistered |
| `COR` fictional male leader/commander Pasquale Venturi | `GFX_portrait_COR_independence_wave_pasquale_venturi` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_pasquale_venturi.dds` | 156x210 | absent/unregistered |
| `COR` Venturi army-small dossier | `GFX_portrait_COR_independence_wave_pasquale_venturi_small` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_pasquale_venturi_small.dds` | 65x67 | absent/unregistered |
| `ARX` people-free provisional assembly | `GFX_portrait_ARX_independence_wave_provisional_assembly` | `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_provisional_assembly.dds` | 156x210 | absent/unregistered |
| `ARX` people-free crown consultative council | `GFX_portrait_ARX_independence_wave_crown_consultative_council` | `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_crown_consultative_council.dds` | 156x210 | absent/unregistered |
| `ARX` fictional male leader/commander Gavino Piras | `GFX_portrait_ARX_independence_wave_gavino_piras` | `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_gavino_piras.dds` | 156x210 | absent/unregistered |
| `ARX` Piras army-small dossier | `GFX_portrait_ARX_independence_wave_gavino_piras_small` | `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_gavino_piras_small.dds` | 65x67 | absent/unregistered |
| `ASX` people-free provisional assembly | `GFX_portrait_ASX_independence_wave_provisional_assembly` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_provisional_assembly.dds` | 156x210 | absent/unregistered |
| `ASX` people-free crown council | `GFX_portrait_ASX_independence_wave_crown_council` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_crown_council.dds` | 156x210 | absent/unregistered |
| `ASX` fictional male leader/commander Salvatore Licata | `GFX_portrait_ASX_independence_wave_salvatore_licata` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_salvatore_licata.dds` | 156x210 | absent/unregistered |
| `ASX` Licata army-small dossier | `GFX_portrait_ASX_independence_wave_salvatore_licata_small` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_salvatore_licata_small.dds` | 65x67 | absent/unregistered |

Production constraints:

- Generate five distinct people-free institutional masters: one COR, two ARX,
  and two ASX. Use one readable local institution-specific symbol, empty
  chamber, desk, seal, records, machinery, or other people-free composition.
  Do not depict faces, human figures, silhouettes, or crowds.
- Generate three distinct fictional male one-person masters: Venturi, Piras,
  and Licata. The names, male presentation, roles, region, period clothing, and
  character metadata must agree.
- Each one-person master serves the civilian/army large slot at 156x210. Its
  army-small consumer is a separately composed 65x67 dossier card, not a resize.
- New army-small work must use the current processor v4.4 contract in
  `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`
  with the manifest-pinned ImageGen frame/paper overlays, explicit crop and
  face box, full metadata, native and 4x comparison sheet, and approval of the
  exact candidate hash by a reviewer other than the producer.
- The accepted earlier Event 6 portrait package is frozen on processor v4.3.
  That historical pin does not authorize v4.3 for new Mediterranean dossiers.

### Protected portrait boundary

The repo-wide documentation search found four explicit file-level protected
portrait contracts that an asset worker must preserve. Their live bytes match
the documented hashes and all four are 156x210 DDS:

| Protected runtime file | Reason | SHA-256 |
|---|---|---|
| `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds` | approved Event 6 historical exemption | `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b` |
| `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` | approved Event 6 historical exemption | `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2` |
| `gfx/leaders/014_cannibalism/hannibal.dds` | canonical user-supplied Event 14 static portrait | `5c48c9a5b503c3185dcb38ee1aabc403d7668094079b78a20010323930d10b88` |
| `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` | canonical user-supplied Event 14 static portrait | `26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717` |

The Mediterranean production tranche must not process, rename, rewrite,
re-encode, or include these four files in a broad portrait replacement pass.

## Focus, idea, and decision icon inventory

### Existing shared Event 6 families

`docs/assets/006_independence_wave/manifest.md` is the current shared static-icon
manifest. It records built-in ImageGen source mode, retained source masters,
processed PNGs, exact prompts, runtime DDS, and the hash ledger at
`docs/assets/006_independence_wave/_tooling/icon_build_report.json`.

Direct validation found:

| Family | Count | Runtime dimensions | Runtime root | Registration | Hash result |
|---|---:|---:|---|---|---|
| shared focus families ASSET-007 through ASSET-019 | 13 | 94x86 | `gfx/interface/goals/006_independence_wave/` | all 13 base plus 13 shine sprites in `interface/006_independence_wave.gfx` | 0 mismatches |
| shared idea families ASSET-020 through ASSET-026 plus Post-Release Instability registry gap | 8 | 64x64 | `gfx/interface/ideas/006_independence_wave/` | all 8 sprites in `interface/006_independence_wave.gfx` | 0 mismatches |
| shared decision families ASSET-027 through ASSET-038 | 12 | 32x32 | `gfx/interface/decisions/006_independence_wave/` | all 12 sprites in `interface/006_independence_wave.gfx` | 0 mismatches |

The first and last runtime hashes in each audited family are:

- focus: `goal_independence_wave_army_integration.dds`
  `a268b305f2e59168dc820ca0b3469018548ac057eb7ca50e35526758e82019f1`;
  `goal_independence_wave_traditional_restoration.dds`
  `6159e9576af12bd7ccbafe483f4afa4315ce187f03bd4cd58e6bfadae0cd983d`;
- ideas: `idea_independence_wave_founding_identity.dds`
  `a0a02e18247e685f963a8de0933243134c5fef9d6e4d3ae75cd2ec5382e211ee`;
  `idea_independence_wave_unsettled_borders.dds`
  `b0ee365e58714b5623e92812ea744d7a40a6b9469474afb33085b1b9a28dbace`;
- decisions: `decision_independence_wave_army_integration_actions.dds`
  `8e17cdde8bd6040608cce4153fa93dde9297f019408a7f01e336f91779d8891a`;
  `decision_independence_wave_recognition_actions.dds`
  `b61c3324225f0b219ed2f5286507e4493a001624848bb188cdb47dd635993394`.

These shared icons can support the Level 1 framework where their accepted
semantic family is an exact match. They do not by themselves satisfy ASX's
Level 2 country-specific focus-group and unique-asset obligation.

No `COR`, `ARX`, or `ASX` focus definition or package-specific focus sprite is
currently present. That is acceptable as an asset hold for the two Level 1
packages, but ASX's country-specific focus group and its unique icons remain a
missing Level 2 deliverable. Do not commission ASX focus icons until the final
focus IDs, branch ownership, and stable consumer names exist.

### Mediterranean idea consumers

`common/ideas/006_independence_wave_mediterranean_ideas.txt` defines 22 ideas:
six COR, six ARX, seven ASX, and three FORM-05. None uses the existing Event 6
idea-family sprites. All currently point to six generic `picture` tokens.

HOI4 resolves `picture = <token>` through `GFX_idea_<token>`. Exact searches of
the installed vanilla interface and the mod interface found only one valid
sprite token:

| Current picture token | Consumers | Exact sprite state |
|---|---:|---|
| `generic_volunteer_expedition_bonus` | 5 | resolves to vanilla `GFX_idea_generic_volunteer_expedition_bonus` |
| `generic_political_reform` | 5 | **missing**; no exact vanilla or mod `GFX_idea_generic_political_reform` |
| `generic_communist_revolution` | 3 | **missing**; only longer `GFX_idea_generic_communist_revolutionary_*` names exist |
| `generic_military_sphere` | 3 | **missing**; vanilla has `GFX_goal_generic_military_sphere`, not an idea sprite |
| `generic_trade_connections` | 4 | **missing**; no exact vanilla or mod idea sprite |
| `generic_neutrality_home_defense` | 2 | **missing**; no exact vanilla or mod idea sprite |

Seventeen of the 22 current idea consumers therefore resolve to nonexistent
sprites. The remaining five all reuse one generic vanilla image and do not
establish distinct package/route-institution art.

Exact current mapping:

| Idea ID | Current picture |
|---|---|
| `cor_exposed_island_supply` | `generic_volunteer_expedition_bonus` |
| `cor_civic_coastal_compact` | `generic_volunteer_expedition_bonus` |
| `cor_constitutional_communes` | `generic_political_reform` |
| `cor_mountain_communes` | `generic_communist_revolution` |
| `cor_island_guard_mandate` | `generic_military_sphere` |
| `cor_protected_customs_mandate` | `generic_trade_connections` |
| `arx_fragmented_island_authority` | `generic_volunteer_expedition_bonus` |
| `arx_sardinian_reconstruction_council` | `generic_political_reform` |
| `arx_island_constitution` | `generic_political_reform` |
| `arx_sardinian_labor_compact` | `generic_communist_revolution` |
| `arx_crown_consultative_state` | `generic_neutrality_home_defense` |
| `arx_mountain_guard_directorate` | `generic_military_sphere` |
| `asx_contested_port_authority` | `generic_volunteer_expedition_bonus` |
| `asx_trinacrian_state_compact` | `generic_political_reform` |
| `asx_palermo_constitution` | `generic_political_reform` |
| `asx_chambers_of_labor_compact` | `generic_communist_revolution` |
| `asx_two_sicilies_crown_council` | `generic_neutrality_home_defense` |
| `asx_straits_security_directorate` | `generic_military_sphere` |
| `asx_protected_mediterranean_mandate` | `generic_trade_connections` |
| `independence_wave_form05_provisional_maritime_charter` | `generic_trade_connections` |
| `independence_wave_form05_ratified_island_union` | `generic_trade_connections` |
| `independence_wave_form05_charter_breakdown` | `generic_volunteer_expedition_bonus` |

Before production, the parent must freeze an explicit art map: either assign an
existing accepted Event 6 idea family where it is semantically exact, or reserve
and commission a distinct 64x64 ImageGen source/runtime sprite for the idea.
Silent generic reuse is not an approved fallback. FORM-05 rows remain blocked
until the formable identity is approved.

### Mediterranean decision consumers

The in-flight decision and decision-category files reference eight custom
32x32 sprite names. None has a source PNG, processed PNG, runtime DDS,
registration, manifest row, or asset-registry row.

| Live sprite | Consumer occurrences | Required runtime path after approval | State |
|---|---:|---|---|
| `GFX_decision_independence_wave_cor_customs` | 6 | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_cor_customs.dds` | absent/unregistered |
| `GFX_decision_independence_wave_cor_mountain_communes` | 3 | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_cor_mountain_communes.dds` | absent/unregistered |
| `GFX_decision_independence_wave_arx_shipping` | 7 | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_arx_shipping.dds` | absent/unregistered |
| `GFX_decision_independence_wave_arx_mountain_guards` | 2 | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_arx_mountain_guards.dds` | absent/unregistered |
| `GFX_decision_independence_wave_asx_port` | 7 | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_asx_port.dds` | absent/unregistered |
| `GFX_decision_independence_wave_asx_grain_straits` | 3 | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_asx_grain_straits.dds` | absent/unregistered |
| `GFX_decision_independence_wave_asx_two_sicilies` | 1 | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_asx_two_sicilies.dds` | absent/unregistered |
| `GFX_decision_independence_wave_form05_maritime_congress` | 3 | `gfx/interface/decisions/006_independence_wave/decision_independence_wave_form05_maritime_congress.dds` | absent/unregistered and FORM-05-blocked |

The first seven names are sufficiently concrete to enter an asset registry once
the parent confirms they are final. The FORM-05 name may be reserved, but art
must wait for the formable identity/motif decision. All final decision art must
be authored at the 32x32 decision surface; do not resize focus or idea art.

## Sprite registration and engine-discovery summary

| Asset type | Discovery contract | Current Mediterranean result |
|---|---|---|
| country flags | exact filenames under the three `gfx/flags` ladders; no `.gfx` | COR vanilla and ARX/ASX base triplets resolve; FORM-05 absent |
| large portraits | exact `spriteType` name to 156x210 DDS | 8 consumers, 0 registrations, 0 DDS |
| army-small portraits | exact `spriteType` name to independently composed 65x67 DDS | 3 consumers, 0 registrations, 0 DDS |
| package ideas | `picture` token resolves to exact `GFX_idea_<token>` | 17 broken consumers; 5 generic resolving consumers; 0 final package mappings |
| custom decisions/categories | exact `GFX_decision_*` registration to 32x32 DDS | 8 sprite names, 0 registrations, 0 DDS |
| shared Event 6 icons | registered in `interface/006_independence_wave.gfx` | 13 focus families plus shine, 8 ideas, and 12 decisions present and hash-valid |
| FORM-05 emblem | reserved `GFX_independence_wave_formable_form_05` | no DDS or registration; correctly blocked |

## Canonical reference packs

The canonical skill-local library is
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`. Its
`README.md` and `CATALOG.md` identify vanilla build Operation Postern
v1.19.2.0.a729, extraction date 2026-07-16, exact vanilla source paths, native
dimensions, and owning definitions. Reference PNGs are review inputs only and
must not be wired, copied, traced, or shipped.

Relevant inventory:

| Reference family | Examples | Native dimensions | Contact sheet SHA-256 |
|---|---:|---|---|
| flags normal/medium/small | 7 per size | 82x52 / 41x26 / 10x7 | shared 1500x1158 sheet `cbf35c6f96347537a5d8e781b198e5949a6515f959f1bc12b55d35847cb36b3e` |
| leader portraits | 8 | 156x210 | `8966ae351d1fe8fc13d47ca1c59ec3d8a34da9101ce5fd65f7acff3421bd0401` |
| commander portraits | 5 | 156x210 | `d62a4b80265533c93669a5eef267dff8db2021a01c1f31dcb73102bf1cc20ca9` |
| advisor/army-small dossiers | 9 | 65x67 | `444d4c1ea83d63aaed1e4db126f697ce64818348b5eac2cec5a1c7ace6a1c8ae` |
| national focus icons | 16 | 100x88 vanilla source canvas | `c539ed22416e39a079573220ab25f8fa51b2cf0a26cb3e535e96af2660fd86a1` |
| idea icons | 15 | 60x67 or 60x68 vanilla source canvas | `e6354fa85658e9a05eae31d2abb9bc714b27444c1c1f0f0ea75b03f57178d060` |
| decision/category icons | 15 | 33x30, 33x32, or 114x101 by owning surface | `82c4b6e8da8843377075fa5252b0dc37b26b8c4311863344aa7dc3faa07cb930` |

The `portraits/advisors/` folder contains three explicitly catalogued vanilla
army-small dossier references and six advisor dossier references. It is the
correct visual reference family for the three Mediterranean army-small
consumers. It is **not** authorization to restore Event 6 gameplay advisor art.

## Event 6 advisor-icon withdrawal check

PASS. The withdrawn custom advisor-art surface has not reappeared.

- `gfx/interface/ideas/006_independence_wave/advisors/` does not exist.
- `interface/006_independence_wave_nwe_advisors.gfx` does not exist.
- No file or directory under live `gfx/` or `interface/` contains both
  `006_independence_wave` and `advisor`.
- No live Event 6 character/interface source registers or consumes a
  `GFX_portrait_advisor_*` sprite.
- The six Mediterranean advisor records—Paolo Pietri, Antone Rocchi, Michele
  Corda, Efisio Satta, Giuseppe Lo Giudice, and Leone Messina—have no custom
  `portraits` blocks and remain asset-neutral.

This matches both current withdrawal handoffs:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_advisor_icon_withdrawal_2026_07_16.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_advisor_icon_withdrawal_audit_2026_07_16.md`

Army-small commander dossier art is a different consumer type and does not
violate this boundary.

## Minimal ordered production and wiring queue

1. **Resolve non-art gates before commissioning.**
   - Decide ASX route ownership: constitutional-only base, cosmetic-route
     identity plus a separately researched baseline, or continued package hold.
   - Freeze the intended route-to-flag coverage for ARX; do not infer ideology
     variants from the base triplet.
   - Keep FORM-05 asset production blocked until final tag, identity, motif,
     palette, route ownership, emblem role, and stable consumers are accepted.
   - Freeze the 22-idea art map and add the seven non-FORM-05 decision sprites
     to the asset registry before generation.

2. **Repair provenance without touching final pixels.**
   - Reconcile the three migrated canonical flag-reference paths/hashes in the
     generated package. Preserve the distinction between original generation
     inputs and current canonical review references.

3. **Produce the minimum live portrait set.**
   - Five people-free institutional 156x210 portraits.
   - Three fictional male one-person 156x210 leader/commander portraits.
   - Three separately composed 65x67 army-small dossiers using processor v4.4
     and independent approval.
   - Retain raw outputs, exact prompts, processed masters, DDS decodes,
     metadata, hashes, contact/review sheets, and a sprite handoff.

4. **Produce/wire the currently concrete icon set.**
   - Seven package decision icons at 32x32 after their registry IDs/stems are
     frozen: COR customs and mountain communes; ARX shipping and mountain
     guards; ASX port, grain/straits, and Two Sicilies.
   - Do not produce the eighth FORM-05 maritime-congress icon until FORM-05 is
     unlocked.
   - For the 22 ideas, commission only the rows whose final art map calls for a
     new asset. Every row must end on a valid registered `GFX_idea_*` sprite;
     the current 17 broken consumers cannot remain. Any proposed reuse of an
     existing shared family requires explicit semantic approval and is not an
     assumed fallback.
   - Do not produce package-specific focus art until stable focus consumers
     exist. ASX's eventual Level 2 focus group must receive its required unique
     icons when those IDs are frozen.

5. **Register and validate.**
   - Register all 11 portrait sprites and every approved custom idea/decision
     sprite in a dedicated Mediterranean `.gfx` surface or another parent-owned
     stable Event 6 registration file.
   - Verify exact consumer-to-sprite-to-file paths, native dimensions, decoded
     DDS pixels, alpha, small-size readability, and manifest hashes.
   - Recheck that no custom Event 6 advisor directory or
     `GFX_portrait_advisor_*` registration entered the tranche.

6. **Do not regenerate unaffected flag art.**
   - COR registered vanilla reuse needs no asset work.
   - ARX final base pixels need no regeneration; only provenance and route
     coverage decisions remain.
   - ASX final S.015 pixels need no regeneration if retained for the approved
     constitutional route. A different neutral baseline or route variant would
     be a separate research plus ImageGen task.
   - FORM-05 remains blocked; no generic maritime emblem or flag substitute is
     permitted.

## Simplifications, omissions, and blockers

No fallback, placeholder asset, locally drawn substitute, or silent sprite
mapping was used in this audit. No asset was generated or changed because the
assigned mode was inventory-only. The unresolved items are reported explicitly
above: 11 missing portrait assets/registrations, 8 missing decision
assets/registrations, 17 immediately broken idea sprite consumers plus five
generic non-final mappings, missing ASX Level 2 focus assets, incomplete
ARX/ASX route flag coverage, ASX route ownership, the generated-package
reference hash defect, and the fully blocked FORM-05 identity/flag/emblem.

Skills used: `chaos-redux-event-assets` and `chaos-redux-subagents`.
