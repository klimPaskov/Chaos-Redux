# IW-095 Dahomey asset-source closure — 2026-09-19

## Disposition

**Disposition: `blocked` for an exact opening-1936 DAH identity and flag source.**

The installed DAH ladder is a technically complete vanilla consumer, but its neutral design is the green-hoist/yellow-over-red flag adopted by the Republic of Dahomey on 16 November 1959, so it is not date-fit for the Event 006 opening identity.

The historically defensible materials found here are royal-war-banner evidence or research references rather than an attested 1936 national flag, and the museum image candidates are not redistribution-cleared.

The route-specific historical branch is **`needs_user_review` only if the parent explicitly accepts an Abomey/Danhomè traditional-institution identity**, names the route and exact cosmetic-tag/runtime basename, and obtains either permission for a source image or an approved original reconstruction brief.

An explicitly alternate-history civic flag is also **`needs_user_review`**, not complete, until the parent records the route identity and exact X-suffixed runtime basename and a later asset worker supplies a provider/output-rights receipt.

No `pass` disposition is available for the current package-wide 1936 baseline.

## Scope and ownership boundary

This is source and evidence research for the non-portrait visual gate only.

No gameplay, country, event, localisation, GFX, flag, manifest, processed PNG, TGA, DDS, or runtime wiring file was changed.

The parent retains ownership of route selection, cosmetic tags, basename approval, package admission, FORM-24 wiring, and final asset integration.

## Required references reviewed

- `AGENTS.md`.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`, including the flag ladder, provenance, rights, source-package, and handoff rules.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md` and its `flags/contact_sheet.png` reference family.
- `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md` for the `gfx/flags` ladder, TGA format, and normal/medium/small dimensions.
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md` for graphical asset paths and `.gfx` context.
- `paradox_wiki/Cosmetic tag modding - Hearts of Iron 4 Wiki.md` and the relevant `Flags` section in `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`.
- Vanilla documentation `effects_documentation.md` (`set_cosmetic_tag`) and `triggers_documentation.md` (`has_cosmetic_tag`).
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md`.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`.
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`.
- `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv`.
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw095_package_completion_2026-09-19.md`.
- Earlier evidence handoffs `006_iw095_symbol_source_gate_2026-08-26.md`, `006_iw095_dahomey_abomey_banner_source_research_2026-08-27.md`, `006_event6_iw095_dahomey_asset_source_research_2026-09-02.md`, and `006_event6_iw095_current_evidence_refresh_2026-09-13.md`.

## Installed DAH identity and runtime ladder

The installed country definition is `common/countries/Dahomey.txt` under `DAH = "countries/Dahomey.txt"` in `common/country_tags/00_countries.txt`.

The installed country history uses state `776-Dahomey.txt`, with France as owner and DAH as core at the 1936 start, and the package handoff records state 776 as the current map anchor.

The vanilla runtime consumer is the standard tag/ideology basename in `gfx/flags`: `DAH_neutrality.tga`, `DAH_democratic.tga`, `DAH_fascism.tga`, and `DAH_communism.tga`, with the same basenames under `gfx/flags/medium` and `gfx/flags/small`.

The installed localisation identifies the neutral tag as `Dahomey`, the democratic and bare tag as `Benin`, the fascist tag as `Benin Unitary Federation`, and the communist tag as `Socialist Republic of Dahomey`.

### Technical inspection

All normal files are 82×52 pixels, 32-bit TGA, full-frame alpha, and use descriptor 8.

All medium files are 41×26 pixels and full-frame except the fascist file's anti-aliased alpha range; neutral, democratic, and communist medium files use descriptor 32 while fascist uses descriptor 8.

All small files are 10×7 pixels; neutral, democratic, and communist use descriptor 0 while fascist retains anti-aliased alpha and uses descriptor 0.

The neutral normal geometry is a green hoist of approximately one third width with yellow and red horizontal fly bands, with major colors green `RGB(0,153,0)`, yellow `RGB(255,255,0)`, and red `RGB(255,0,0)`.

The democratic variant adds a white star to the same base geometry, the communist variant is a green field with a red star, and the fascist variant is a red-bordered white panel with a grey elephant motif.

These are visual and technical observations only and do not establish a 1936 identity or a redistribution licence for the vanilla files.

| Runtime file | Dimensions | Alpha | SHA-256 | Source/date/identity disposition |
|---|---:|---|---|---|
| `vanilla/gfx/flags/DAH_neutrality.tga` | 82×52 | 255–255 | `bfa74629618da992c30b95c7e775b2e5cb8b5d45577810e5f5b8f33a15362c15` | Republic of Dahomey design adopted 1959; reject as opening-1936 baseline. |
| `vanilla/gfx/flags/DAH_democratic.tga` | 82×52 | 255–255 | `40bbbbf7ce00d167ab96965850fe00adcf9a11a8d09a08b8a6f9f8807d2c6a10` | Later/generic ideological derivative; no 1936 evidence. |
| `vanilla/gfx/flags/DAH_fascism.tga` | 82×52 | 255–255 | `f3c18ee3f5e04de13ad96086fd39c474361b0499e31c4b4aee810308504c0daa` | Generic elephant-panel derivative; no 1936 evidence. |
| `vanilla/gfx/flags/DAH_communism.tga` | 82×52 | 255–255 | `8f18c34624d85dd4d5b48c7d0bea4d8c83ebf1fb79989f15fcaa76888b91712d` | Generic communist derivative; no 1936 evidence. |
| `vanilla/gfx/flags/medium/DAH_neutrality.tga` | 41×26 | 255–255 | `3355ff209bf8658bc4abcf36a5bebe100e9f21e55983951a8994ded2274b699c` | Same anachronistic neutral identity. |
| `vanilla/gfx/flags/medium/DAH_democratic.tga` | 41×26 | 255–255 | `a95290563028b056e3e1aad929c37e0460a4cd07dfbe0ba22653b64d5bd4c724` | Ideological derivative; no 1936 evidence. |
| `vanilla/gfx/flags/medium/DAH_fascism.tga` | 41×26 | 225–255 | `1708cb6903d5dd7a893a958607b72f644e61916717f551dc5ed73d46f1b23925` | Ideological derivative; no 1936 evidence. |
| `vanilla/gfx/flags/medium/DAH_communism.tga` | 41×26 | 255–255 | `98b3c119e1d4459d2d6cd06bd9d88aa228589a78b4789f029e0e632700c2fa99` | Ideological derivative; no 1936 evidence. |
| `vanilla/gfx/flags/small/DAH_neutrality.tga` | 10×7 | 255–255 | `a0929469ed6678955bc9b8a7664cb3b23e7a962ad82ddb6ad7cdecedad2b855c` | Same anachronistic neutral identity. |
| `vanilla/gfx/flags/small/DAH_democratic.tga` | 10×7 | 255–255 | `18fa1986423834256571793ca26103f09894c8d50e84c7905c22a6bbf4856d8c` | Ideological derivative; no 1936 evidence. |
| `vanilla/gfx/flags/small/DAH_fascism.tga` | 10×7 | 221–255 | `7de5132da791612edaeab3de9dd947236bd560246fa27805da9d1b0a50698e04` | Ideological derivative; no 1936 evidence. |
| `vanilla/gfx/flags/small/DAH_communism.tga` | 10×7 | 255–255 | `a7d3d82326b2b41feca0caa49347b5a98d29a961a07874b81ceb136d979ea2ff` | Ideological derivative; no 1936 evidence. |

The mod has no `DAH*.tga` files in `gfx/flags`, `gfx/flags/medium`, or `gfx/flags/small`, and the canonical review library has no DAH ladder.

The vanilla files are not copied into the mod because the skill requires preserving the existing vanilla base and does not infer a redistribution licence from installed game data.

## Historical source review

### Primary museum record: Ghézo/Danhomè royal-war banner

The Musée du quai Branly — Jacques Chirac record for object `71.1930.54.910 D` (`ccObjectID 207636`) records a cotton appliqué textile credited as “Tenture offerte par le roi Ghézo à l’Empereur Napoléon III.”

The [official object lookup](https://collections.quaibranly.fr/?action=search&field=/Record/ObjectNumber,/Record/ObjectNumber2&label=N°%20de%20gestion&value=%5b71.1930.54.910%20D%5d) and [machine-readable record](https://collections.quaibranly.fr/ccProxy.ashx/?action=get&command=search&query=and(not(isnull(CCObjectID));71.1930.54.910%20D)&fields=*&range=1-20&responseFormat=json) describe a red-and-blue border, pole-side attachment strips, armed warriors with firearms and récades, a possibly leonine yellow animal, and a repeated combat scene.

The record gives conflicting dimensions, `230 × 353 × 0.5 cm` in the object fields and approximately `305 × 192 cm` in the descriptive text, so this uncertainty must be retained if the source is ever used in a manifest.

This is strong evidence for a Danhomè royal/military banner associated with the Abomey court in 1856, but it is not evidence that the same appliqué design was a national or regional state flag in French Dahomey in 1936.

The associated museum preview images were inspected only in temporary storage and were not copied, processed, or proposed as runtime assets.

The museum [online-collection conditions](https://m.quaibranly.fr/fr/recherche-scientifique/catalogues-et-publications/bibliotheque-et-fonds-documentaires/catalogues/conditions-de-mise-en-ligne-des-collections/) and [legal notices](https://www.quaibranly.fr/en/legal-notices/legal-notices/) require rights review or prior written authorization for protected image reuse, and the related Musée de l’Homme record `PV0080632` carries “Reproduction interdite.”

**Disposition:** route motif only, `needs_user_review`; do not ship the museum photograph or imply a cleared runtime image.

### Other inspected historical references

| Candidate | Source, date, and rights | Visual/identity fit | Disposition |
|---|---|---|---|
| King Adandozan banner of war | [Commons record](https://commons.wikimedia.org/wiki/File:King_Adandozan_banner_of_war.jpg); authentic royal war banner sent as a gift in 1811 or circa 1800; image marked CC BY-SA 4.0 with VRT ticket `2021020410008441`; inspected JPEG SHA-256 `e4af11cb1d9621b67041d3ce4d3d74cf41460d77387fbe9872dfead55be610e2`. | Tan appliqué field with rows of black profile heads/figures and red/black weapons; visually a banner, not a flat country flag; too early and tied to Adandozan. | Research corroboration only; not a 1936 baseline. |
| 1854 banner plate | [Commons record](https://commons.wikimedia.org/wiki/File:FOOT(1854)_p098_DAHOMEY,_SKULL_ORNAMENTS_AND_BANNERS.jpg); 1854 period book plate, British Library/Mechanical Curator, Commons categories mark the scan public domain. | White banner with central dark figure/animal and skull/regalia motifs; useful period context, not one attributable state flag. | Research context only; do not promote to runtime. |
| `Dahomey_flag_1889.svg` | [Commons record](https://commons.wikimedia.org/wiki/File:Dahomey_flag_1889.svg); modern vector by Jaume Ollé/SVG ArnoldPlaton, page and file metadata indicate public-domain treatment. | Flat green/yellow/red design associated with Ghezo, but the page itself says “perhaps” 1889 and notes evidence may instead point to 1818–1859; no 1936 continuity proof. | Research only; date and attribution uncertainty block package baseline. |
| `Flag_of_Ghezo_of_Dahomey.svg` | [Commons record](https://commons.wikimedia.org/wiki/File:Flag_of_Ghezo_of_Dahomey.svg); CC BY-SA 4.0 modern reconstruction by Di (2020) based on Hubert-Herald and an attributed badge. | Route-specific Ghezo reconstruction, not a 1936 national flag and not a primary period scan. | Research only; any later route use needs explicit attribution/share-alike handling and parent acceptance. |
| `Royal_banner_of_Béhanzin_of_Dahomey.svg` | [Commons record](https://commons.wikimedia.org/wiki/File:Royal_banner_of_B%C3%A9hanzin_of_Dahomey.svg); modern reconstruction by Samhanin (2019), Commons marks public-domain treatment. | Royal banner reconstruction for Béhanzin circa 1889–1892; ownership, colours, and function do not establish a universal 1936 identity. | Research only; primary confirmation and route acceptance required. |
| `Flag_of_Benin.svg` | [Commons record](https://commons.wikimedia.org/wiki/File:Flag_of_Benin.svg); public-domain vector treatment. | The design is the 1959 Republic of Dahomey/Benin flag and is anachronistic for IW-095's 1936 opening. | Reject for the opening baseline. |

The temporary inspection copies of the Commons JPEGs/SVGs remain outside the repository under the local temporary directory and are not asset deliverables.

The historical sources above cannot safely be collapsed into a claim that an exact 1936 DAH national flag is known.

The French tricolour is also rejected as an independent DAH identity because it represents the colonial sovereign rather than a distinct Dahomey/Abomey route.

## FORM-24 relationship

The accepted family registry identifies FORM-24 as the West African Federation and lists Asante, Fante, Dahomey, Benin, Oyo, and compatible republics as possible participants.

The accepted formable specification requires an accepted route, eligible territories, local names, leader identity, flag/cosmetic identity, member or territory proof, and integration or consent handling before a formable is promoted.

The current IW-095 package handoff records only generic FORM-24 preparation and no accepted DAH member consent ledger, symbol contract, member-capital/territory adapter, family carrier identity, or cleanup route.

No regional or formable emblem was invented here, and no FORM-24 symbol should be used to satisfy the DAH opening-flag gate.

## Evidence and output status

| Deliverable | Status | Reason |
|---|---|---|
| Exact 1936-capable DAH opening source | **Blocked** | No attested identity with date and role fit was found. |
| Reuse of installed vanilla DAH ladder | **Rejected** | Neutral design is post-1936 and installed-game rights are not inferred. |
| Rights-cleared historical image | **Blocked** | Museum images require permission; open references are banners/reconstructions or date-uncertain. |
| Parent-approved route-specific identity | **Needs user review** | Possible only after explicit route, tag, basename, and source/reconstruction decision. |
| Explicit alternate-history civic flag | **Needs user review** | Requires parent acceptance plus later ImageGen provider/output-rights receipt. |
| Source PNG | **Not created** | No accepted source/basename. |
| Processed PNG | **Not created** | No accepted source/basename. |
| Final normal/medium/small TGA or DDS | **Not created** | No accepted identity; no runtime promotion. |
| Manifest entry | **Not created** | No selected deliverable or runtime basename. |
| `gfx_handoff.md` | **Not created** | No exact runtime basename or final hashes to hand off. |
| Contact sheet | **Not created in repository** | Candidate inspection was research-only and did not form a deliverable package. |

There is no provider/output-rights receipt for an IW-095 generated flag in the current asset evidence tree.

## Exact remaining gates

1. The parent must choose whether IW-095 opens as a historically grounded Dahomey/Abomey identity, a parent-approved traditional-institution route, or an explicitly alternate-history civic identity.
2. The parent must record the exact cosmetic tag and runtime basename, including the required X-suffixed route tag when a new route identity is selected.
3. For a historical route, the parent must accept an original reconstruction brief constrained by the primary banner evidence or obtain written permission for any museum image; direct museum-image reuse is not cleared.
4. For an alternate-history route, a later asset worker must create the source and full 82×52, 41×26, and 10×7 ladder under the event-asset skill and preserve a provider/output-rights receipt; this handoff does not invent that receipt or art.
5. After acceptance, the asset worker must produce and hash the source PNG, processed PNG, final ladder, manifest, contact sheet, and `gfx_handoff.md` before the parent wires anything.
6. FORM-24 needs a separate accepted DAH member/consent/territory/symbol contract and a distinct family identity asset; it cannot be treated as evidence for the opening DAH flag.
7. Central package admission remains fail-closed until identity, rights, and runtime basename evidence are accepted by the parent.

## File changes

Only this dated handoff was added.

No gameplay or GFX files were edited, and no asset was staged, promoted, wired, or committed.

## Simplifications and blockers

No unapproved fallback or invented historical flag was used.

The package remains incomplete for the requested source closure because the exact 1936 identity, redistribution rights, parent-approved route basename, and FORM-24 identity contract are unresolved.
