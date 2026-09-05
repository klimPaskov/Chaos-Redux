# Event 006 IW-095 Dahomey flag identity/source research — 2026-09-05

Status: BLOCKED for a historically sourced 1936 opening flag; route-specific Abomey/Danhomè traditional identity is NEEDS_USER_REVIEW. This is a read-only source and provenance handoff. No runtime, gameplay, central-admission, GFX, image, DDS, manifest, or contact-sheet asset was created or changed.

## Scope and decision summary

This pass covers only the non-portrait flag/cosmetic identity for IW-095 Dahomey. The current package carrier is `DAH` on installed state `776-Dahomey.txt`, with `FRA` as the 1936 owner and `556` retained only as the stale planning baseline. The installed vanilla DAH flag ladder is engine-usable, but no member of it is defensible evidence for a distinct 1936 Dahomey/Abomey opening identity.

There is no located primary, redistributable 1936 Dahomey national flag or state/cosmetic mark that clears the package gate. The strongest historical material is an attested 1856 Danhomè royal/military appliqué banner and a 1938 museum photograph of a Dahomey banner; both support a route-specific traditional institution motif, not a 1936 national flag, and both have unresolved direct-use rights. A route-specific original reconstruction could be considered only after parent acceptance of the route semantics, cosmetic tag, exact runtime basename, and rights/asset-production path. It must be labelled an interpretive alternate-history/traditional route identity, not an authentic 1936 state flag.

## Authority and files reviewed

The accepted Event 006 design and binding surfaces reviewed were:

- [006 Event 006 first-footprint admission improvement addendum](../006_event6_first_footprint_admission_improvement_addendum_2026-08-26.md), including the IW-095 source/identity gate and the prohibition on generic or invented historical symbols.
- [Event 006 candidate country registry](../../../specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv), IW-095 row requiring sourced historical flags and leaders for `DAH`.
- [Event 006 package research resolution](../../../specs/006_independence_wave_specs/research/006_package_research_resolution.csv), IW-095 row requiring a released identity/origin match and source-backed route variants.
- [Event 006 current installed map/package bindings](../package_bindings/006_current_installed_map_package_bindings.csv), which binds IW-095 to state `776` and records stale baseline `556` as Bamako.
- [Event 006 current binding audit](../package_bindings/006_current_installed_map_binding_audit.md), which confirms `776=Dahomey` and `556=Bamako`.
- [Event 006 sensitive identity research rules](../../../specs/006_independence_wave_specs/research/006_sensitive_identity_research_rules.md), including the distinction between community, territory, government, and route-specific symbols.
- [Prior IW-095 asset source handoff](006_event6_iw095_dahomey_asset_source_research_2026-09-02.md), [Abomey banner source handoff](006_iw095_dahomey_abomey_banner_source_research_2026-08-27.md), [symbol source gate](006_iw095_symbol_source_gate_2026-08-26.md), [source research handoff](006_event6_iw095_source_research_2026-09-01.md), and [package re-audit](006_event6_iw095_dahomey_package_reaudit_2026-09-02.md).
- Canonical review references under `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`, including `README.md`, `CATALOG.md`, `REFERENCE_MANIFEST.md`, and `flags/contact_sheet.png`. The canonical flag shelf contains no DAH reference and is review-only, not a runtime or rights grant.

The required offline wiki pages were consulted, including [Country creation - Hearts of Iron 4 Wiki.md](../../../../paradox_wiki/Country%20creation%20-%20Hearts%20of%20Iron%204%20Wiki.md), [Cosmetic tag modding - Hearts of Iron 4 Wiki.md](../../../../paradox_wiki/Cosmetic%20tag%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md), [Graphical asset modding - Hearts of Iron 4 Wiki.md](../../../../paradox_wiki/Graphical%20asset%20modding%20-%20Hearts%20of%20Iron%204%20Wiki.md), and the required core pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding. The installed vanilla documentation reviewed included `documentation/triggers_documentation.md`, `documentation/effects_documentation.md`, and the relevant script-concept documentation for `has_cosmetic_tag`, `set_cosmetic_tag`, and `drop_cosmetic_tag` behavior.

## Current installed identity and runtime surface

Vanilla source files inspected:

| Surface | Finding | SHA-256 |
|---|---|---|
| `common/country_tags/00_countries.txt` | `DAH = "countries/Dahomey.txt"` | `b3777a74b44bfb1b082817b2a1e9676f0c8cda45a0cbea75e55e2b703f3b73b6` |
| `common/countries/Dahomey.txt` | `african_gfx`, `african_2d`, blue country colour; no flag or cosmetic declaration | `1ee95a5921dd5c6c4ecae3b9571b5917309ad20129fb002b47122abbaf7b50ac` |
| `history/countries/DAH - Dahomey.txt` | Capital `776`, generic neutrality setup and advisors; no named 1936 leader | `8266e12dc603d1e654194acb6203638140c9e58fd723d08a7306b93d5c55bba4` |
| `history/states/776-Dahomey.txt` | State 776, `owner=FRA`, `add_core_of=DAH`, `STATE_776` name, three provinces, naval base | `7740cd5a10c8963fb5437eaf885d14407d7344be9a0f8ba7b2352557e64af610` |
| `common/characters/DAH.txt` | Generic advisors/high command/theorist only; no named 1936 opening leader | `047f12bd8c09417a8e1eaceae07ca8e2d8541264bc2ba212af4d5c2854480d7e` |

The mod currently has no `DAH*.tga` in `gfx/flags`, `gfx/flags/medium`, or `gfx/flags/small`, no IW-095 DAH cosmetic-tag declaration, no DAH flag entry in the Event 006 interface files, and no `DAH`, `Dahomey`, `Abomey`, or `Danhomè` asset output under `docs/assets/006_independence_wave`. Therefore the game falls through to the installed vanilla ladder for the existing carrier; no project-owned flag package currently exists to audit or wire.

## Installed vanilla DAH flag census

All twelve installed inputs were read-only decoded as TGA type 2, RGBA. Normal files are 82x52 with descriptor 8; medium files are 41x26; small files are 10x7. The vanilla ladder has no bare `DAH.tga`, only ideology-specific names. The descriptor/origin convention is inconsistent in the installed files: normal files use bottom-left descriptor 8, neutral/democratic/communist medium files use top-left descriptor 32, fascist medium uses bottom-left descriptor 8, and all small files use descriptor 0. This is an observation, not a proposal to copy the ladder into the mod.

| Installed path relative to vanilla `gfx/flags` | SHA-256 | Visual/semantic observation |
|---|---|---|
| `DAH_neutrality.tga` | `bfa74629618da992c30b95c7e775b2e5cb8b5d45577810e5f5b8f33a15362c15` | Green hoist with yellow-over-red fly; the design is associated with the Republic of Dahomey’s 1959 flag, not a documented 1936 colonial flag. |
| `DAH_democratic.tga` | `40bbbbf7ce00d167ab96965850fe00adcf9a11a8d09a08b8a6f9f8807d2c6a10` | Same green/yellow/red base with a white democratic/star-like mark; ideological game variant, not a sourced 1936 state identity. |
| `DAH_communism.tga` | `8f18c34624d85dd4d5b48c7d0bea4d8c83ebf1fb79989f15fcaa76888b91712d` | Green/red-star ideological variant; no package-specific 1936 provenance. |
| `DAH_fascism.tga` | `f3c18ee3f5e04de13ad96086fd39c474361b0499e31c4b4aee810308504c0daa` | Elephant-panel red/white/grey ideological variant; vanilla localisation names it “Benin Unitary Federation,” not a 1936 Dahomey opening government. |
| `medium/DAH_neutrality.tga` | `3355ff209bf8658bc4abcf36a5bebe100e9f21e55983951a8994ded2274b699c` | Medium of the neutral design; descriptor 32/top-left. |
| `medium/DAH_democratic.tga` | `a95290563028b056e3e1aad929c37e0460a4cd07dfbe0ba22653b64d5bd4c724` | Medium of the democratic design; descriptor 32/top-left. |
| `medium/DAH_communism.tga` | `98b3c119e1d4459d2d6cd06bd9d88aa228589a78b4789f029e0e632700c2fa99` | Medium of the communist design; descriptor 32/top-left. |
| `medium/DAH_fascism.tga` | `1708cb6903d5dd7a893a958607b72f644e61916717f551dc5ed73d46f1b23925` | Medium of the fascist design; descriptor 8/bottom-left. |
| `small/DAH_neutrality.tga` | `a0929469ed6678955bc9b8a7664cb3b23e7a962ad82ddb6ad7cdecedad2b855c` | Small of the neutral design; descriptor 0. |
| `small/DAH_democratic.tga` | `18fa1986423834256571793ca26103f09894c8d50e84c7905c22a6bbf4856d8c` | Small of the democratic design; descriptor 0. |
| `small/DAH_communism.tga` | `a7d3d82326b2b41feca0caa49347b5a98d29a961a07874b81ceb136d979ea2ff` | Small of the communist design; descriptor 0. |
| `small/DAH_fascism.tga` | `7de5132da791612edaeab3de9dd947236bd560246fa27805da9d1b0a50698e04` | Small of the fascist design; descriptor 0. |

Vanilla country localisation further demonstrates the semantic mismatch: `DAH_neutrality` is “Dahomey,” `DAH_democratic` is “Benin,” `DAH_fascism` is “Benin Unitary Federation,” `DAH_communism` is “Socialist Republic of Dahomey,” and the bare `DAH` name is “Benin.” These strings can be technically valid for vanilla ideology switches, but they do not establish a package-approved 1936 opening identity.

## Historical source findings

### 1936 baseline

No primary, dated, rights-cleared 1936 Dahomey national flag, administrative seal, or state banner was located in the reviewed source set. The secondary [Flag of Benin chronology](https://en.wikipedia.org/wiki/Flag_of_Benin) records the green-hoist/yellow-over-red design as adopted on 16 November 1959 for the Republic of Dahomey and records French colonial Dahomey as using the French tricolour from 1894 to 1959. This is useful chronology for rejecting the vanilla neutral art as a 1936 Dahomey flag, but it is not a primary colonial regulation or a mod redistribution license. A French tricolour would represent the colonial host rather than provide the required distinct Dahomey/Abomey route identity and is not recommended as a substitute.

### Route-specific Danhomè/Abomey material

The strongest candidate is Musée du quai Branly–Jacques Chirac object `71.1930.54.910 D`, `ccObjectID 207636`, described as a cotton appliqué banner offered by King Ghézo to Emperor Napoleon III and recorded as Royaume du Danhomè, 1856. Its red/blue border, armed figures, firearms, récades, yellow animal-like figure, and repeated combat imagery are defensible evidence for a Danhomè royal/customary military route motif. It is not a 1936 national flag, and the museum’s online collection conditions and legal notices require permission for image reuse. The object record also contains a dimensional discrepancy between `230 x 353 x 0.5 cm` fields and an approximately `305 x 192 cm` descriptive measurement; any future interpretive reduction must preserve that uncertainty rather than present a false exact reconstruction.

Musée de l’Homme iconothèque record `PV0080632` is a 1938 monochrome photograph of a Dahomey banner with combat/hunt appliqué. It is useful prewar corroboration that the banner tradition remained visible near the period, but the record is marked “Reproduction interdite,” so it is research-only until written permission is obtained.

The [King Adandozan banner source](https://commons.wikimedia.org/wiki/File:King_Adandozan_banner_of_war.jpg) is a c.1800/1811 historical banner distributed under CC BY-SA 4.0 with VRT ticket `2021020410008441` and source hash `E4AF11CB...E2` as recorded in the prior IW-095 handoff. It is useful as an attributable early Danhomè war-banner reference, but it predates 1936 by more than a century and cannot establish an opening national flag.

The [British Library 1854 Dahomey scan](https://commons.wikimedia.org/wiki/File:FOOT(1854)_p098_DAHOMEY,_SKULL_ORNAMENTS_AND_BANNERS.jpg) is public-domain context for banners and regalia, not a uniquely identified national flag. The modern [Ghézo](https://commons.wikimedia.org/wiki/File:Flag_of_Ghezo_of_Dahomey.svg), [Béhanzin](https://commons.wikimedia.org/wiki/File:Royal_banner_of_B%C3%A9hanzin_of_Dahomey.svg), and `Dahomey_flag_1889.svg` reconstructions are not primary evidence for a 1936 state flag and must not be promoted as authentic opening identity without separate source and rights review. The public-domain [Flag of Benin](https://commons.wikimedia.org/wiki/File:Flag_of_Benin.svg) is also the 1959 design and is rejected for this gate.

## Answers to the package-gate questions

1. A historically defensible 1936 Dahomey opening national flag was not found. The package-wide flag identity remains BLOCKED.
2. A historically defensible route-specific cosmetic identity does exist at the level of an attributable Danhomè royal/customary banner tradition, with the 1856 Ghézo object as the strongest source. It is a traditional institutional motif, not a 1936 national flag, and remains NEEDS_USER_REVIEW.
3. The vanilla DAH ideology flags are technically valid engine fallbacks only. They are not semantically acceptable as accepted IW-095 1936 identity evidence: the neutral art is post-1959, the democratic and fascist localisations describe Benin variants, and the communist/fascist art is ideological abstraction. Installed vanilla files also carry no inferred permission for redistribution into the mod.
4. The mod should not copy, recolour, relabel, or promote the vanilla ladder, and this pass does not recommend adding a French tricolour or an invented “Dahomey” flag.

## Exact evidence and rights receipt still missing

To clear a historical 1936 baseline, the parent needs a primary source with an attributable archive/institution, date or period fit, object/function, design description or image, and explicit permission or a clear public-domain/Creative Commons grant covering redistribution in the mod. A primary source confirming that no separate colonial Dahomey flag existed could support an explicitly documented representation decision, but it would not by itself supply a distinct route flag.

To clear the Abomey/Danhomè route, the parent must accept in writing that the flag is a route-specific traditional/alternate-history institutional identity rather than an authentic 1936 state flag, choose the exact cosmetic tag and runtime basename, and authorize the asset-production path. Direct use of the Musée du quai Branly or Musée de l’Homme imagery additionally requires written permission that explicitly covers mod redistribution and public display; the online preview and “Reproduction interdite” record are not rights receipts. An original flat reconstruction would need its own production record, source-motif attribution, interpretive-reduction note, and final asset manifest after that acceptance; this researcher did not generate or process one.

No basis exists in this pass to set an IW-095 identity-rights-cleared flag or to change central admission. No exact runtime basename was supplied or accepted by the parent, so no `gfx_handoff.md` can be produced for a selected asset.

## Changed files and validation

Changed files: this handoff only, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw095_dahomey_flag_identity_research_2026-09-05.md`. No vanilla file was copied, and no mod gameplay or runtime asset file was edited.

Validation consisted of read-only inspection of the accepted specs/plans and prior IW-095 handoffs, the canonical vanilla-reference catalog/contact sheet, the installed vanilla DAH country/state/character/localisation and flag ladders, a complete 12-file path census, SHA-256 hashing, and TGA decoding/dimension/origin checks. No live game was launched and no rights approval was inferred from file presence, museum preview availability, or the vanilla installation.

## Remaining blockers and owner sequence

- Parent/design owner: decide whether IW-095 is allowed to use a route-specific Danhomè/Abomey traditional institution identity and record the acceptance basis.
- Parent/runtime owner: if accepted, choose and register the exact cosmetic tag and runtime basename before asset production; preserve `DAH` base behavior unless the explicit route design authorizes a cosmetic variant.
- Source/legal owner: obtain a primary 1936/colonial symbol receipt for a true baseline, or written museum permission for direct historical imagery; otherwise document the no-separate-flag representation and route-specific interpretation.
- Asset worker: only after those decisions may it create the normal/medium/small ladder, source/processed/final files, manifest entry, contact sheet, and `gfx_handoff.md`.

No fallback art, invented historical claim, generic symbol, or unapproved simplification was used.
