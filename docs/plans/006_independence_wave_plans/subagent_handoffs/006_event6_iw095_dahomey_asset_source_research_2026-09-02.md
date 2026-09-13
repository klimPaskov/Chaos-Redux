# IW-095 Dahomey asset-source research handoff — 2026-09-02

## Disposition

Scope is limited to non-portrait flag and historical-symbol research for Event 006 IW-095 Dahomey (`DAH`).

The opening-1936 package-wide flag remains **BLOCKED**.

The 1856 Ghézo/Danhomè royal-war-banner record is defensible as a route-specific traditional-institution motif, but not as a package-wide 1936 national flag.

No source image, processed PNG, final TGA/DDS, contact sheet, asset manifest, `gfx_handoff.md`, gameplay file, `.gfx` file, or runtime flag was created or changed.

## Safe evidence outcome

| Candidate | Evidence and provenance | Date/function fit | Rights and disposition |
|---|---|---|---|
| Installed neutral `DAH` flag | Vanilla `DAH_neutrality.tga` is a clean green-hoist/yellow-over-red design. | Secondary chronology records adoption by the Republic of Dahomey on 16 November 1959, so it is not a documented 1936 colonial-Dahomey flag. | Vanilla game asset; no redistribution licence is inferred. **Reject for the 1936 baseline.** |
| Installed democratic/communist/fascist `DAH` variants | Technical ideology variants of the same carrier, including a white-star version, green/red-star version, and elephant-panel version. | They do not establish an opening-1936 Dahomey identity and are later/generic ideological art. | Vanilla game assets; no redistribution licence is inferred. **Do not promote as historical evidence.** |
| `MQB-207636-DAH-1856-BANNER` | Musée du quai Branly — Jacques Chirac object `71.1930.54.910 D`, `ccObjectID 207636`, culture `Royaume du Danhomè`, credit “Tenture offerte par le roi Ghézo à l’Empereur Napoléon III.” The record describes a cotton appliqué banner with a red/blue border, pole-side attachment strips, armed warriors with firearms and récades, a possibly leonine yellow animal, and repeated combat imagery. [Official object record](https://collections.quaibranly.fr/?action=search&field=/Record/ObjectNumber,/Record/ObjectNumber2&label=N°%20de%20gestion&value=%5b71.1930.54.910%20D%5d). | Recorded 1856 and explicitly royal/military; strong evidence for Danhomè court-banner practice, not a state flag in French Dahomey in 1936. | Museum preview-image rights are unresolved; the museum conditions and legal notices require permission for reuse. **Needs user review as a route motif only; never ship the museum photograph or call it a 1936 flag.** |
| `PV0080632` | Musée de l’Homme iconothèque record for a 1938 monochrome Dahomey banner photograph describing a white cotton flag with silk appliqué and combat/hunt scenes. | Corroborates pre-war museum documentation of the banner tradition, but does not establish official 1936 state use. | Record carries “Reproduction interdite.” **Research corroboration only.** |
| King Adandozan banner of war | Commons record for an authentic c.1800/1811 banner, marked CC BY-SA 4.0 with VRT ticket `2021020410008441`; prior inspection copy SHA-256 `E4AF11CB1D9621B67041D3CE4D3D74CF41460D77387FBE9872DFEAD55BE610E2`. [Commons record](https://commons.wikimedia.org/wiki/File:King_Adandozan_banner_of_war.jpg). | Useful evidence of royal-war-banner practice, but far too early and not a national flag. | CC BY-SA 4.0 attribution/share-alike obligations apply. **Do not use as the IW-095 baseline.** |

The museum source has a dimensional discrepancy (`230 x 353 x 0.5 cm` in object fields versus approximately `305 x 192 cm` in descriptive text); this must remain uncertainty in any later manifest.

## Current installed and Chaos Redux flag audit

Vanilla binds `DAH = "countries/Dahomey.txt"` at `common/country_tags/00_countries.txt:160`. The installed country definition `common/countries/Dahomey.txt` is only African graphical culture and colour data. The installed history `history/countries/DAH - Dahomey.txt` sets capital `776`, generic 1936 neutrality, ten convoys, and generic advisors, but no named leader or package identity. State `history/states/776-Dahomey.txt` is `STATE_776` (`Benin/Dahomey`), owned by `FRA`, core `DAH`, with provinces `10919 12874 12762` and capital-compatible naval base `1`.

The 12 installed vanilla flag inputs were inspected at:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/DAH_{neutrality,democratic,communism,fascism}.tga`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/medium/DAH_{neutrality,democratic,communism,fascism}.tga`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/small/DAH_{neutrality,democratic,communism,fascism}.tga`

All are type-2, 32-bit TGA ladders at `82x52`, `41x26`, and `10x7`. The normal files use descriptor `8` (bottom-left). The medium neutrality, democratic, and communist files use descriptor `32` (top-left), while medium fascism uses descriptor `8`; all small files use descriptor `0`. This vanilla inconsistency is another reason not to copy the family into a final Event 006 ladder; new Chaos Redux route ladders should use the project’s validated bottom-left convention.

Current normal-file SHA-256 values are:

```text
DAH_neutrality.tga  bfa74629618da992c30b95c7e775b2e5cb8b5d45577810e5f5b8f33a15362c15
DAH_democratic.tga 40bbbbf7ce00d167ab96965850fe00adcf9a11a8d09a08b8a6f9f8807d2c6a10
DAH_communism.tga  8f18c34624d85dd4d5b48c7d0bea4d8c83ebf1fb79989f15fcaa76888b91712d
DAH_fascism.tga    f3c18ee3f5e04de13ad96086fd39c474361b0499e31c4b4aee810308504c0daa
```

The mod has zero `DAH*.tga` files in each of `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`, so the current carrier falls through to vanilla tag-named flags. There are no DAH/IW-095 matches in `common/country_tags/006_independence_wave_countries.txt`, `common/countries/006_independence_wave_shared_african.txt`, `interface/006_independence_wave.gfx`, or `interface/006_independence_wave_small_assets.gfx`. Standard HOI4 flag lookup needs no `.gfx` sprite definition; a future route must use a stable cosmetic-tag/basename ladder instead.

The canonical review root `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/` and `flags/contact_sheet.png` were inspected. The sheet contains 21 review-only flag references and no DAH reference. The current Chaos Redux Event 006 route precedent `ASY_independence_wave_civic_federationX.tga` was also checked at all three sizes (`82x52`, `41x26`, `10x7`, type-2 32-bit, descriptor `8`); it demonstrates a separate route-specific ladder, not a base-tag replacement.

There are no `IW-095`, `DAH`, Dahomey, Abomey, or Danhomè outputs under `docs/assets/006_independence_wave/`; no source/processed/runtime asset package or handoff basename exists.

## Recommendation to parent

Keep the bare `DAH` vanilla family untouched and keep ASSET-044 blocked for the opening baseline.

If the parent accepts an Abomey/Danhomè traditional-institution route, approve a route-specific cosmetic identity and exact runtime basename first. The asset owner can then make an original flat orthographic reconstruction constrained by the 1856 record’s red/blue border and attributed royal-war-banner motifs, using the required ImageGen flag workflow, and label it as an interpretive route design rather than a documented 1936 flag. Do not directly redistribute the museum photograph. Any Event 006 cosmetic/route tag should follow the project’s explicit `X`-suffix convention once the parent names it.

If a historically grounded 1936 baseline is required, obtain a primary administrative/state-symbol source with usable rights. If that cannot be obtained, the only safe alternative is an explicitly alternate-history civic flag generated from researched regional motifs; it must not be described as an authentic historical Dahomey flag.

## Blockers and next handoff

1. No independently documented, rights-cleared 1936 Dahomey national flag has been established.
2. The Ghézo banner is route-specific and its museum image rights are unresolved.
3. Parent has not selected the opening identity route, cosmetic tag, or exact runtime basename.
4. No source PNG, processed preview, final TGA/DDS, manifest row, or `gfx_handoff.md` can be created without that decision and source mode.
5. DAH identity/rights and central admission remain fail-closed; no flag evidence should set `independence_wave_iw_095_identity_rights_cleared`.

No simplification or fallback was used. This handoff is source evidence only and does not admit IW-095 to the Event 006 pool.
