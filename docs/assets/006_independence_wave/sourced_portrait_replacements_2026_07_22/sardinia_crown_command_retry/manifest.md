# Event 006 Sardinia portrait source retry

Research date: 2026-07-22. This is a source-only package for the two remaining
IW-018 ARX identity rows. The files under `source_masters/` are unchanged
downloaded source binaries. No crop, resize, color correction, face synthesis,
advisor treatment, processed PNG, DDS conversion, `.gfx` edit, or runtime wiring
was performed. `source_ready` is not claimed for this package: the commander
candidate is `needs_review`, and the crown/council role is `blocked`.

## Role ledger

| Consumer role / intended sprite | Real candidate | Status | Source page and identity record | Direct original URL | Date / author / archive | Rights statement | Local source master / dimensions / bytes / SHA-256 | Role, era, and uncertainty | Processed PNG | Final DDS |
|---|---|---|---|---|---|---|---|---|---|---|
| `ARX_gavino_piras` / `GFX_portrait_ARX_independence_wave_gavino_piras` | Gioacchino Solinas | `rejected_visual_style_pending_refinish` | [Commons file](https://commons.wikimedia.org/wiki/File:Gioacchino_Solinas.png); [Roma 8 Settembre 1943 biography](https://www.roma8settembre1943.it/i-personaggi/i-personaggi-di-parte-italiana/gen-brig-gioacchino-solinas/) | [Commons original](https://upload.wikimedia.org/wikipedia/commons/4/49/Gioacchino_Solinas.png) | Image dated 1943; photographer/source not named on Commons; source page credits `digilander.libero.it/historiabis/baroma1.jpg` | Commons records Public domain Italy; no explicit PD-1996/US statement was found. Rights remain review-gated. | [`source_masters/sardinia/arx_gioacchino_solinas_1943_original.png`](source_masters/sardinia/arx_gioacchino_solinas_1943_original.png); 181x278; 54,141 bytes; `AF9D453444A7C8EE3F4F75089EEC9104748E19D4C8ADBB0F2F2BF150E1A0EA15` | Solinas was born in Bonorva, Sassari province, on 1 September 1892 and was a decorated Bersaglieri commander. He was alive and militarily active in 1936, giving this a strong Sardinian-born mountain/territorial-command fit. The binary is small and seven years after the opening. Parent found no vanilla ownership hit. The explicit crop is identity-safe, but the v5.0 candidate remains photographic rather than HOI4-painted and is rejected in `visual_review.md`. | `processed_png/ARX_gioacchino_solinas.png` (rejected candidate only) | Not created |
| `ARX_sardinian_crown_consultative_council` / `GFX_portrait_ARX_independence_wave_vittorio_pala` | **No admissible crown candidate** | `blocked` | Role contract is a dynastic/crown consultative state; no sourced non-vanilla officeholder with a defensible reusable portrait was found. | — | — | — | — | Do not fill this grounded role with a generated face, a generic Sardinian, a name-only `Vittorio Pala`, or a cultural historian. The crown row remains blocked pending a documented living-in-1936 dynastic/crown officeholder and reusable image evidence. | Not created | Not created |

## Crown-route collision and rejection evidence

These exact source binaries are preserved as research evidence only. The parent
audited vanilla and installed-country ownership and found active-person conflicts;
none may be wired to ARX under the no-living-country/no-active-person rule.

| Candidate / intended ARX role | Source provenance and exact local binary | Why it is blocked or rejected |
|---|---|---|
| Aimone di Savoia-Aosta, Duca di Spoleto / crown route | [Commons file](https://commons.wikimedia.org/wiki/File:Duca_di_Spoleto.png); [Treccani 1936 biography](https://www.treccani.it/enciclopedia/savoia-aimone-di-duca-di-spoleto_%28Enciclopedia-Italiana%29/); [direct original](https://upload.wikimedia.org/wikipedia/commons/4/4d/Duca_di_Spoleto.png); [`source_masters/sardinia/arx_aimone_savoy_aosta_duca_di_spoleto_original.png`](source_masters/sardinia/arx_aimone_savoy_aosta_duca_di_spoleto_original.png); 389x456; 231,898 bytes; `EAE7D502784F0876B808CC5C0B33D854E6CB627157169B989A7D0C540E027B6D` | Commons describes a pre-1936 scan from *Grande enciclopedia aeronautica* (1936), author AAVV, Public domain Italy with PD-1996. Aimone (1900-1948) is a strong historical Savoy-Aosta fit, but vanilla starts `ITA_prince_aimone` in `history/countries/ITA - Italy.txt:795`; the parent rejected duplication. |
| Amedeo di Savoia-Aosta, Duca d'Aosta / crown route | [Commons file](https://commons.wikimedia.org/wiki/File:Amedeo_di_Savoia-Aosta_(1898-1942).jpg); [Treccani biography](https://www.treccani.it/enciclopedia/savoia-aosta-amedeo-di-duca-d-aosta_%28Dizionario-Biografico%29/); [direct original](https://upload.wikimedia.org/wikipedia/commons/d/da/Amedeo_di_Savoia-Aosta_%281898-1942%29.jpg); [`source_masters/sardinia/arx_amedeo_savoy_aosta_1931_original.jpg`](source_masters/sardinia/arx_amedeo_savoy_aosta_1931_original.jpg); 2784x4296; 732,079 bytes; `73B558F19F1786CF8C558FF794C93B0A07449406610F500446CF5FE3EDA7DC11` | Commons dates the source postcard to 1931 and marks it Public domain Italy/PD-1996, but the colorized postcard includes embedded `AMEDEO AOSTA` lettering and is not a clean source master. More importantly, vanilla starts `AOI_prince_amedeo` in `history/countries/AOI - Italian East Africa.txt:124`; parent rejected duplication. |
| Filiberto di Savoia-Genova, 4th Duke of Genoa / crown route | 1928 [Commons file](https://commons.wikimedia.org/wiki/File:S.A.R._Filiberto_di_Savoia-Genova.png), [direct original](https://upload.wikimedia.org/wikipedia/commons/7/73/S.A.R._Filiberto_di_Savoia-Genova.png), [`source_masters/sardinia/arx_filiberto_savoy_genoa_1928_original.png`](source_masters/sardinia/arx_filiberto_savoy_genoa_1928_original.png), 389x600, 497,691 bytes, `49E95017244F688933E941F9724B5C8C3FDCECB1143D70FE429664818B87200C`; 1938 [Commons file](https://commons.wikimedia.org/wiki/File:Filiberto_di_Savoia-Genova_(1).png), [direct original](https://upload.wikimedia.org/wikipedia/commons/a/a8/Filiberto_di_Savoia-Genova_%281%29.png), [`source_masters/sardinia/arx_filiberto_savoy_genoa_1938_original.png`](source_masters/sardinia/arx_filiberto_savoy_genoa_1938_original.png), 610x888, 1,117,820 bytes, `CA4FC17FCDB90C118D0D39D2078CFBB2AB9F78F33BB6E75B4B7D5EFD51D1D95A`; 1915-25 ICCD [file](https://commons.wikimedia.org/wiki/File:Filiberto_di_Savoia-Genova.jpg), [direct original](https://upload.wikimedia.org/wikipedia/commons/1/10/Filiberto_di_Savoia-Genova.jpg), [`source_masters/sardinia/arx_filiberto_savoy_genoa_1915_1925_iccd_original.jpg`](source_masters/sardinia/arx_filiberto_savoy_genoa_1915_1925_iccd_original.jpg), 299x390, 59,509 bytes, `0DE7E5A8E59F2A2FE78E16295519ACBD70A026B9BBCD3FE1018055458D3CA8BD` | Filiberto (1895-1990) was alive in 1936 and the Duke of Genoa title is a Savoy subsidiary title associated with the Sardinian crown. The 1928 Ravagnani source is a clean candidate and the ICCD image is explicitly archival/public domain; however vanilla defines `ITA_prince_filiberto` in `common/characters/ITA.txt:694` and recruits him in `history/countries/ITA - Italy.txt:776`. Parent rejected all three binaries. |
| Ferdinando Umberto di Savoia-Genova, 3rd Duke of Genoa / crown route | No local binary copied; Commons circa-1920 lead was only a research probe. | Parent found `ITA_ferdinando_umberto_filippo` in `common/characters/TUR.txt:2681`, recruited by `history/countries/TUR - Turkey.txt:533`, and referenced by the Turkey focus at line 6247. Reject; do not source or duplicate. |
| Raimondo Carta Raspi / crown route | [Commons file](https://commons.wikimedia.org/wiki/File:Raimondo_Carta_Raspi.jpg); [Casteddu Online source](https://www.castedduonline.it/cid-ricorda-raimondo-carta-raspi/); [Sardinia Foundation biography](https://www.fondazionesardinia.eu/lorigine-dei-giudicati-sardi-di-raimondo-carta-raspi/); [direct original](https://upload.wikimedia.org/wikipedia/commons/e/e1/Raimondo_Carta_Raspi.jpg); [`source_masters/sardinia/arx_raimondo_carta_raspi_original.jpg`](source_masters/sardinia/arx_raimondo_carta_raspi_original.jpg); 450x587; 116,221 bytes; `D576627CE7ED54C318AFE93E9F86327BC9DE87579DF603AEA62A6174009A9444` | Carta Raspi (Oristano 1893-Cagliari 1965) was a Sardinian historian/editor who returned to Sardinia in 1922 and wrote on medieval Sardinian politics. Commons gives Public domain Italy plus explicit PD-1996, but the portrait carries a large visible signature and the person is a cultural/traditional historian, not a documented dynastic/crown officeholder. Retain only as a cultural lead; it cannot satisfy the current crown role without a design change. |

## Other Sardinian research leads rejected fail-closed

- Luigi Efisio Marras (Cagliari, 1888-1981) is Sardinian-born and alive in 1936, but the only attributable binary located was an explicitly 1950s, 255x346 portrait. The prior retry package records it as blocked; no duplicate copy is made here.
- Pietro Mastino (Sassari, 1883-1960) has a pre-1936, rights-marked Commons portrait, but he was an autonomist/Action Party politician rather than a dynastic/crown officeholder. The prior retry package records it as blocked.
- Gavino Pizzolato (Sorso, 1884-1963) and Ettore Manca, Marchese di Mores (1877-1966), are plausible Sardinian-linked military leads, but the located generals.dk portraits are copyrighted and have no accepted reusable binary. They remain blocked.
- The Araldica Sardegna photographic archive contains living-in-1936 Sardinian noblemen (including Amat Sanjust, Manca di Villahermosa, Sanjust, Cocco Manca Aymerich, and Scano Sisini families), but its family-photo pages state no explicit reuse license. No file was copied or handed off as accepted evidence.
- No dead-before-1936 historical officeholder, later postwar politician, generated face, generic portrait, watermarked archive image, or advisor/dossier icon is an allowed substitute.

## Source and collision notes

The parent audit found no vanilla ownership hit for `Gioacchino Solinas`; that
candidate remains `needs_review` only. The parent found active vanilla ownership
for Aimone, Amedeo, Filiberto, and Ferdinando Umberto; those collisions are the
reason the crown role is blocked. The old generated ARX names `Gavino Piras` and
`Vittorio Pala` are not identity evidence and are not re-used as people.

## Processing boundary

There is one retained processed PNG/review-sheet/metadata trial for Solinas. It
is explicitly rejected because it remains photographic rather than HOI4-painted;
there is no final DDS, advisor asset, or `.gfx` snippet. The parent may advance
only after a stronger identity-preserving painted finish and independent review
close the Solinas style, rights, era, and low-resolution questions. The ARX crown/council role must remain blocked until a new
non-vanilla-owned, defensible dynastic/crown source is found or the design is
explicitly changed by the parent.
