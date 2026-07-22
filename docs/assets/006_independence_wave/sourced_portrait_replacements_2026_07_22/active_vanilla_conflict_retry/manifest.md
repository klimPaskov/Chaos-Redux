# Event 006 active-vanilla conflict portrait retry

Source-only manifest for the 2026-07-22 retry of three grounded Event 006
leader/commander portraits whose former identities are active vanilla
characters. The parent prompt classifies every requested role as
`grounded_source_only`: real male people only, alive and role-plausible in
1936, with a defensible regional or command connection. The former identities
are not renamed or reused here:

- `IW-008 RHI` civic/constitutional/patron leader: Konrad Adenauer is an
  active vanilla GER character.
- `IW-009 BAY` military/emergency mountain-command leader: Franz Ritter von
  Epp is an active vanilla GER character.
- `IW-001 SCO` territorial/military commander: Edmund Ironside is an active
  vanilla ENG character.

The active ownership findings above are recorded in the existing parent-owned
audits [`006_rhi_bay_postportrait_admission_audit_2026_07_22.md`](../../../../plans/006_independence_wave_plans/subagent_handoffs/006_rhi_bay_postportrait_admission_audit_2026_07_22.md)
and [`006_sco_agx_postportrait_admission_audit_2026_07_22.md`](../../../../plans/006_independence_wave_plans/subagent_handoffs/006_sco_agx_postportrait_admission_audit_2026_07_22.md). This package does
not duplicate that tag audit or alter any existing source, portrait, GFX,
localisation, gameplay, or runtime file.

## Processing boundary and status vocabulary

All files under `source_masters/` are unchanged downloaded source bitstreams.
No crop, resize, retouch, recolour, PNG preview, DDS conversion, contact
sheet, or `.gfx` edit was made. The parent must independently choose and
review a source before running the approved portrait pipeline.

- `source_ready`: subject/role fit and an explicit archive/licence basis are
  documented; the unchanged local source is available for independent review.
- `needs_review`: a face-visible candidate is useful, but rights, provenance,
  branch, date, or regional-fit uncertainty remains. It must not be processed
  without a separate reviewer decision.
- `blocked`: no acceptable sourced candidate was acquired. None of the three
  requested roles is blocked in this retry.

## Candidate ledger

| Requested role / intended runtime sprite | Disposition and identity | Source page and direct source | Archive, date, author, rights basis | Unchanged local source evidence | Role and era fit | Vanilla/mod ownership check | Deferred runtime outputs |
|---|---|---|---|---|---|---|---|
| `IW-008 RHI` civic/constitutional/patron; `GFX_portrait_RHI_independence_wave_provisional_directorate` | **`source_ready` primary — Karl Jarres (1874–1951)** | [Bundesarchiv Commons page](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-01175,_Karl_Jarres.jpg); [direct unchanged Commons upload](https://upload.wikimedia.org/wikipedia/commons/c/c7/Bundesarchiv_Bild_102-01175%2C_Karl_Jarres.jpg) | German Federal Archives, Bild 102-01175; archive caption dates the image to 1925; photographer recorded as unknown/o. Ang.; current archive credit is Bundesarchiv. Commons records **CC BY-SA 3.0 Germany**, attribution `Bundesarchiv, Bild 102-01175 / CC-BY-SA 3.0`. The Commons file history notes a small uploader crop before this download; no crop was made locally. | `source_masters/RHI/RHI_karl_jarres_bundesarchiv_1925.jpg`; 562×800, 38,735 bytes, SHA-256 `72c952b0f1a1e3c08a16b20c123466b4bfc737d7c03ae63594cf7e6332c2c8d6`; grayscale. | Born in Remscheid, Rhine Province; mayor of Remscheid/Duisburg and Reich Interior Minister. A living Rhineland civic, constitutional, and patron/municipal identity in 1936; the 1925 archive portrait is period-close and face-visible. | Exact/variant scan (`Karl Jarres`, `Carl Jarres`, `karl_jarres`, `carl_jarres`) returned **no textual hits** in the specified vanilla and current Chaos Redux roots. | Processed PNG: none. Final DDS: none. Parent target remains `156×210` large leader portrait at `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds`; no path is created here. |
| `IW-008 RHI` civic/constitutional/patron; same sprite | **`source_ready` alternate — Wilhelm Marx (1863–1946)** | [Commons file page](https://commons.wikimedia.org/wiki/File:Reichskanzler_Wilhelm_Marx.jpg); [LOC catalog](https://www.loc.gov/pictures/item/2014716800/); [LOC digital ID](https://hdl.loc.gov/loc.pnp/ggbain.36651); [direct Commons upload](https://upload.wikimedia.org/wikipedia/commons/9/94/Reichskanzler_Wilhelm_Marx.jpg) | Library of Congress George Grantham Bain collection, digital ID `ggbain.36651`; Bain News Service; Commons date field 1920 but LOC caption card says no date recorded, so retain **undated/early-20th-century (Commons c.1920)** uncertainty. Commons states no known copyright restrictions / public domain. | `source_masters/RHI/RHI_wilhelm_marx_loc_1920.jpg`; 749×1024, 132,275 bytes, SHA-256 `df60e8b2f335d1fe6b399d258a4b4fd52d3186ae6b0fcd323baaf504e5079661`; grayscale. | Born in Cologne; judge/lawyer, Centre Party chairman, and two-time Weimar Chancellor. Strong constitutional/civic Rhenish identity and alive in 1936; image is an unmistakable face-visible Bain portrait but its exact capture date is uncertain. | Exact/variant scan (`Wilhelm Marx`, `wilhelm_marx`) returned **no textual hits** in the specified vanilla and current Chaos Redux roots. | Processed PNG: none. Final DDS: none. Same deferred RHI runtime target as above. |
| `IW-009 BAY` military/emergency mountain command; `GFX_portrait_BAY_independence_wave_mountain_commandant` | **`source_ready` primary — Eugen Ritter von Schobert (1883–1941)** | [Commons file page](https://commons.wikimedia.org/wiki/File:Eugen_von_Schobert.jpg); [NAC record family](https://www.audiovis.nac.gov.pl/obraz/2-12702/); [NAC image endpoint](https://audiovis.nac.gov.pl/obraz/30585/7c907d5fd06cac7ac892ec5f9d66fdae/); [direct unchanged Commons upload](https://upload.wikimedia.org/wikipedia/commons/d/d3/Eugen_von_Schobert.jpg) | National Digital Archive of Poland (NAC), catalogue/info `2-12702`; July 1940; author unknown. NAC/Commons says the material is public domain or State Treasury-owned with free use; Commons applies the Poland/US public-domain rationale. | `source_masters/BAY/BAY_eugen_von_schobert_nac_1940.jpg`; 2315×3520, 1,016,112 bytes, SHA-256 `0512bb979b5bac234eac4c0c61f397664ba97e64cf1626ec95aa05d6d99e7f83`; grayscale portrait. | Born in Würzburg, Kingdom of Bavaria; entered the Royal Bavarian Army and commanded Bavarian infantry, VII Army Corps, and 11th Army. Alive in 1936 and defensible as a Bavarian emergency/army commander. Caveat: he is an infantry/army commander rather than a specialist Gebirgstruppe officer; the role label is an emergency mountain-region command abstraction, not a claim about branch. | Exact/variant scan (`Eugen von Schobert`, `Eugen Ritter von Schobert`, `Eugen Schobert`, `eugen_von_schobert`, `eugen_ritter_von_schobert`, `eugen_schobert`) returned **no textual hits** in the specified vanilla and current Chaos Redux roots. | Processed PNG: none. Final DDS: none. Parent target remains `156×210` large leader portrait at `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`; no path is created here. |
| `IW-009 BAY` military/emergency mountain command; same sprite | **`needs_review` alternate — Ludwig Kübler (1889–1947)** | [Commons file page](https://commons.wikimedia.org/wiki/File:Ludwig_K%C3%BCbler.jpg); [direct unchanged Commons upload](https://upload.wikimedia.org/wikipedia/commons/a/a3/Ludwig_K%C3%BCbler.jpg) | Portrait dated circa 1941; source credited to Władysław Langner, *Ostatnie dni obrony Lwowa 1939* (Warsaw, 1979); author not stated. Commons applies a Poland/US public-domain rationale for an anonymous Polish publication but asks for the first-publication evidence. Rights/provenance therefore remain **needs_review** despite the strong public-domain assertion. | `source_masters/BAY/BAY_ludwig_kuebler_circa_1941.jpg`; 583×782, 96,757 bytes, SHA-256 `0f53222ae6be6dc03f31b594a87f797e44b832f880a9981a4e4fae497efbd096`; grayscale portrait. | Born in Munich; Bavarian Army officer and General der Gebirgstruppe, later commander of 1st Mountain Division and XXXXIX Mountain Corps. Exact mountain-branch and Bavarian regional fit; alive in 1936. Do not process until a reviewer resolves the 1979-book/anonymous-source rights chain. | Exact/variant scan (`Ludwig Kübler`, `Ludwig Kuebler`, `Ludwig Kubler`, `ludwig_kuebler`, `ludwig_kubler`) returned **no textual hits** in the specified vanilla and current Chaos Redux roots. | Processed PNG: none. Final DDS: none. Same deferred BAY runtime target as above. |
| `IW-001 SCO` territorial/military commander; `GFX_portrait_SCO_independence_wave_territorial_commandant` | **`source_ready` primary — Major-General Sir Victor Morven Fortune (1883–1949)** | [Commons source page](https://commons.wikimedia.org/wiki/File:Fortune_Victor_Morven.jpg); [51st Highland Division archive page](https://51hd.co.uk/photos/img110); [direct unchanged Commons upload](https://upload.wikimedia.org/wikipedia/commons/b/bc/Fortune_Victor_Morven.jpg) | Imperial War Museum London, War Office Second World War Official Collection, RML 342; 1940; author not stated on the close portrait. Commons marks the scan/publication as UK-government public domain (`PD-scan`/`PD-UKGov`); the 51HD archive page identifies the original context as Major General Fortune, 12 June 1940, IWM RML 342. | `source_masters/SCO/SCO_victor_fortune_iwm_1940_portrait.jpg`; 200×250, 14,854 bytes, SHA-256 `830f175712988c825a604e48464584dc0b71cd61b51ab423e2badc0c1a46d049`; grayscale close portrait. Context-only unchanged companions from the same archive family are retained at `SCO_victor_fortune_iwm_1940.jpg` (800×525, SHA-256 `3833223d2634eb7f993c1bc152d43c8fad04cb98774c263af3d3e33edb8c8c6d`) and `SCO_victor_fortune_51hd_mid_1940.jpg` (580×609, SHA-256 `6f2a686283bb796b6cd81003efd12a4c40135709eafee3c0e4e50e438f5f3392`). | Scottish-born Black Watch officer; commanded the 52nd (Lowland) Division in 1935–36 and the 51st (Highland) Division from 1937/1938. Alive and an immediately defensible Scottish territorial commander in 1936. The close source is low resolution; the unchanged contextual companions are not substitutes and must not be processed without independent review. | Exact/variant scan (`Victor Fortune`, `Victor Morven Fortune`, `victor_fortune`, `victor_morven_fortune`, `fortune_victor`) returned **no textual hits** in the specified vanilla and current Chaos Redux roots. | Processed PNG: none. Final DDS: none. Parent target remains `156×210` large leader portrait at `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds`; no path is created here. |
| `IW-001 SCO` territorial/military commander; same sprite | **`needs_review` alternate — General Sir Archibald Rice Cameron (1870–1944)** | [NPG portrait record](https://www.npg.org.uk/collections/search/portrait/mw114004/Sir-Archibald-Rice-Cameron); [Commons source page](https://commons.wikimedia.org/wiki/File:Archibald_Cameron_in_1929.jpg); [direct unchanged Commons upload](https://upload.wikimedia.org/wikipedia/commons/a/a3/Archibald_Cameron_in_1929.jpg) | Bassano Ltd whole-plate glass negative, 25 July 1929, given to the National Portrait Gallery in 1974 (NPG x124702). Commons labels the scan public domain/PD-US expired, but the NPG record displays `© National Portrait Gallery, London` and Commons records an explicit third-party copyright-claim warning. Rights are therefore **needs_review**, not cleared. | `source_masters/SCO/SCO_archibald_rice_cameron_1929_commons.jpg`; 1182×1536, 209,961 bytes, SHA-256 `c4d5303969717f660dbd74748216878bad28831d3299e857621bfe650697c691`; grayscale portrait. | Served as GOC-in-C Scottish Command 1933–37 and governor of Edinburgh Castle in 1936; a direct Scottish territorial-command fit, although this is a command-region connection rather than a claim that he was Scottish-born. Do not process until NPG/Commons rights conflict is resolved. | Exact/variant scan (`Archibald Cameron`, `Archibald Rice Cameron`, `archibald_cameron`, `archibald_rice_cameron`) returned **no textual hits** in the specified vanilla and current Chaos Redux roots. | Processed PNG: none. Final DDS: none. Same deferred SCO runtime target as above. |

## Supplementary unchanged source master

The LOC Bain image for Jarres is retained as a provenance/face-reference
alternate, not a second identity: `source_masters/RHI/RHI_karl_jarres_loc_undated.jpg`
(1024×734, 104,205 bytes, SHA-256
`d07eb103f4c5fdf13ca06c9d58fdea2f626c14f82060d2b2d92b740df633b36e`). Its LOC
record is [Dr. Jarres, LCCN 2014716741](https://www.loc.gov/pictures/item/2014716741/)
([ggbain.36592](https://hdl.loc.gov/loc.pnp/ggbain.36592)); the caption card
has no recorded date, the Bain metadata is early-20th-century/possibly c.1900,
and Commons identifies Bain News Service and public-domain/no-known-
restrictions status. It is not the 1925 Bundesarchiv primary and must not be
silently substituted for it.

## Ownership scan evidence

On 2026-07-22, exact and variant name patterns for all six identities were
searched case-insensitively in both the installed vanilla and current Chaos
Redux roots, limited to:

`common/characters`, `history/countries`, `common/country_leader`, `interface`,
`gfx/leaders`, and `localisation/english`.

Patterns covered the accented, unaccented, spacing, hyphen, and common token
forms listed in each candidate row (including `karl_jarres`, `carl_jarres`,
`wilhelm_marx`, `ludwig_kuebler`/`ludwig_kubler`,
`eugen_ritter_von_schobert`, `victor_morven_fortune`, and
`archibald_rice_cameron`). Every candidate returned **no textual hits** in
those requested roots. This is a bounded ownership scan, not a replacement
for the parent’s final character/recruitment audit.

## No fallback / no generated substitution

No generated, generic, fictional, female, advisor, ImageGen, or unrelated
face was used. The old Adenauer, von Epp, and Ironside identities remain
rejected for active vanilla ownership and are not present as replacement
masters in this package. If a reviewer rejects a `needs_review` alternate,
the parent must keep the role unresolved or acquire another defensible real
source; no fallback is authorized.
