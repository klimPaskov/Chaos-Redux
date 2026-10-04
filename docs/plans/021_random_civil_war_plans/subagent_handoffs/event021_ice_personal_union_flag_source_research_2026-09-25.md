# Event 021 / Event 006 Icelandic Cosmetic Flag Source Research

Audit date: 2026-09-26. The requested filename retains the parent-provided 2026-09-25 date.

Status: `needs_user_review`.

## Parent verification correction (2026-09-26)

The initial search conclusion below missed the installed Vanilla 1936 country-history assignment. `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/ICE - Iceland.txt:30` sets `set_cosmetic_tag = ICE_personal_union`; the Event 021 `iw_012/ICE` adapter can capture an existing ICE or release ICE through the ordinary package path. A whole-install file-name search found no `ICE_personal_union` TGA or DDS in base game or DLC, and the five standard names are absent from the installed normal/medium/small flag roots. Thus this is a real inherited cosmetic-flag asset gap for the live 1936 Iceland identity, not merely an unused cosmetic definition. The route remains dynamically selected by current anchor ownership/control, host eligibility, dormant-country state, and package preflight; this correction does not add or recommend any fixed country roster.

The historical-art finding still stands: the evidence supports Iceland's 1918 national cross design and a lighter blue, not a Danish overlay or an exact reproducible shade. No flag asset was created because the precise visual treatment requires user direction; engine fallback behavior remains untested. The corrected identity finding is incorporated in the finding and route sections below. The production no-go means no art or wiring before the asset-treatment decision, not that the cosmetic is inactive.

## Finding

Official Alþingi records support a historical Icelandic national flag for the sovereign Kingdom of Iceland during its personal union with Denmark, but they do not establish a separate joint Denmark–Iceland union flag. The supported flag is Iceland’s own blue field with a white Nordic cross and a red cross inset within it. The 1918 version used a lighter blue than the post-1944 version; the precise historical blue is not recoverable from the descriptions reviewed.

The parent correction is confirmed: installed Vanilla `history/countries/ICE - Iceland.txt:30` executes `set_cosmetic_tag = ICE_personal_union` for the 1936 ICE start. The prior statement that this identity had no source assignment was incomplete. The tag is active in the Vanilla 1936 country history, not merely an inactive cosmetic definition. The history's later `drop_cosmetic_tag` lines 132 and 189 are commented out and do not clear it.

**Decision: YES, this is a real conditional Event 021 inherited-package flag-asset coverage gap, not an inactive cosmetic definition.** The dynamic `iw_012` route can reuse the live `ICE` country, whose Vanilla 1936 start carries `ICE_personal_union`; the five corresponding TGAs are absent from the installed Vanilla tree and the mod. This is a source-level missing-asset finding, not a claim about engine fallback or a claim that every ICE route state keeps this tag.

**Production recommendation: NO-GO within this research-only task.** The historical design reference is supportable as Iceland's own flag during the personal union, but the precise pre-1944 blue is not established. Do not copy the Vanilla ICE image, invent a Danish composite, generate art, or wire files without a separately approved asset-production decision.

## Current consumers and dynamic route conditions

- Installed Vanilla `history/countries/ICE - Iceland.txt:30` assigns `ICE_personal_union` in the 1936 historical setup. In the same file, later `#drop_cosmetic_tag = yes` statements at lines 132 and 189 are comments, not active effects.
- `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt:24` registers package `iw_012` in Event 006’s complete-package array. Event 021 scans that live array with a rotating global cursor in `common/scripted_effects/021_random_civil_war_parent_effects.txt:154`, skips scenario-reserved package IDs, loads the package, and validates its current anchor and carrier before accepting it; this is not a fixed country-participant roster.
- The human-country parent trigger in `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:52-62` requires a normal human country and, among other gates, `independence_wave_event021_dormant_package_available = yes`.
- The Iceland branch in `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt:18` requires state 100 to be owned and controlled by the human host, population above `event021_parent_tuning.minimum_state_population_k`, infrastructure above zero, and `ICE` to pass `is_independence_wave_dormant_country_scope`.
- After package admission, `event021_parent_capture_event6_selected_actor` passes the selected package ID to `independence_wave_capture_event021_adapter_actor` (`common/scripted_effects/021_random_civil_war_parent_effects.txt:3872-3874`). The Event 006 crosswalk captures `ICE` as `random_civil_war_event6_selected_actor` only when the package ID is `iw_012` and `ICE` exists (`common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt:56-67`). If the carrier is absent, the same crosswalk can release `ICE` (`:105`). Neither helper explicitly assigns or clears `ICE_personal_union`.
- The source-level country consumer is the selected `ICE` country scope, which retains its current cosmetic identity when reused unless another effect has changed it. The adapter's absent-country branch calls `release = ICE` but contains no explicit cosmetic-tag assignment; this audit did not establish whether the engine applies the country-history setter during that release and does not assume that it does.
- Installed Vanilla's `common/on_actions/09_aat_on_actions.txt:1154-1169` can fire `iceland_events.1` when `FROM` has original tag `DEN`, ICE is a subject of `FROM`, has completed `ICE_declare_absolute_neutrality`, and has not already declared independence; `events/AAT_Iceland.txt:36-38` then calls `drop_cosmetic_tag = yes`. Separately, the “Iceland wants a Danish King” event chain reaches `iceland_events.9`; its option A at `events/AAT_Iceland.txt:480-499` sets `ICE_independent_kingdom`. Thus the current ICE country can have a different or no cosmetic tag on alternate event paths, so the `ICE_personal_union` gap is conditional on the selected ICE still carrying that identity.
- No explicit Event 006/021 tag assignment, tag-clearing rule, flag sprite, or fallback branch for `ICE_personal_union` was found in the route sources. No engine fallback behavior was tested or assumed, and no fixed roster or candidate-selector change is proposed.

## Installed asset checks

Checked the five standard tag/ideology names in all six requested directories on 2026-09-26: `ICE_personal_union.tga`, `ICE_personal_union_communism.tga`, `ICE_personal_union_democratic.tga`, `ICE_personal_union_fascism.tga`, and `ICE_personal_union_neutrality.tga`.

| Root | Normal | Medium | Small |
| --- | --- | --- | --- |
| Installed Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\flags` | 0/5 present | 0/5 present | 0/5 present |
| Mod `gfx/flags/` | 0/5 present | 0/5 present | 0/5 present |

The Vanilla normal root is `gfx/flags/`; medium and small are `gfx/flags/medium/` and `gfx/flags/small/`. The recursive exact-basename scan over the complete installed Vanilla tree returned zero matching `.tga` or `.dds` files for the five tag/ideology names. The 12 on-disk DLC package directories contain no `gfx/flags` directory; the only installed DLC ZIP (`dlc/dlc003_rocket_launcher_unit_pack/dlc003.zip`, 36 entries) contains none of the five names. The only other directory named `flags` found in the installation is `gfx/interface/career_profile/flags`, which also had no matching names. The mod was checked in its normal, medium, and small flag roots and had zero of the five TGAs.

As control evidence, installed Vanilla has `ICE.tga`, `ICE_communism.tga`, `ICE_fascism.tga`, and `ICE_neutrality.tga` in each standard size root; `ICE_democratic.tga` is absent. The mod has no ordinary `ICE` flag files in those roots. The canonical reference contact sheet at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/flags/contact_sheet.png` shows the Vanilla ICE base flag in the normal 82x52, medium 41x26, and small 10x7 ladders; its catalog records those previews as Vanilla HOI4 references. These checks establish file presence only and do not establish engine fallback behavior.

## Historical design identification and sources

The installed Vanilla 1936 history assignment identifies the runtime cosmetic tag as active for that start, while the tag name and Alþingi sources identify its historical referent as Iceland during the 1918–1944 constitutional union with Denmark. Alþingi’s contemporaneous 9 September 1918 debate described Iceland as a free and sovereign state in personal union with Denmark. Alþingi’s historical overview dates the union’s entry into force to 1 December 1918 and the Republic’s establishment and termination of the union to 17 June 1944; its English parliamentary booklet also notes that the union was effectively severed after Denmark’s occupation in 1940.

Alþingi’s 1997–98 flag bill history says a 19 June 1915 royal decree selected the blue, white, and red cross design and that this became Iceland’s national flag when sovereignty took effect on 1 December 1918. A 7 November 2018 parliamentary record says the flag raised on 1 December 1918 had the same cross design used today, but its blue was lighter and did not darken until 1944. The 1915/1918 decree color terms are reported as ultramarine blue and high red; Alþingi’s 1997–98 account explicitly says the historical blue term has no unambiguous modern color equivalent. Act No. 34/1944 supplies the later statutory geometry and proportions, but its post-1944 color wording must not be treated as an exact pre-1944 color specification.

These sources support an Icelandic national flag design for the personal-union state. They do not identify a Danish overlay, a dual-flag combination, or a distinct “personal union” emblem. A period variant could be justified only as Iceland’s own flag with a documented pre-1944 color treatment; the exact blue remains uncertain. The official 2018 centenary page captions a photograph of the 1 December 1918 ceremony and credits Þorleifur K. Þorleifsson / Ljósmyndasafn Íslands, but the page does not provide a reuse license and the photograph was not retrieved or used as a flat design source.

Sources reviewed (official Alþingi records and publications; accessed 2026-09-26):

- [Jóhannes Jóhannesson, debate on the Danish–Icelandic Act of Union, 9 September 1918](https://www.althingi.is/altext/raeda/30/70.html).
- [Alþingi, 927/122 bill on Iceland’s national flag, 122nd legislative session 1997–98](https://www.althingi.is/altext/122/s/0927.html).
- [Alþingi, parliamentary record on the 1918 flag, 7 November 2018](https://www.althingi.is/skodalid.php?lidur=lid20181107T182730&lthing=149).
- [Alþingi, “100 years of sovereignty 2018,” dated 1 December 2018](https://www.althingi.is/um-althingi/fraedslu--og-kynningarefni/100-ara-fullveldi-2018/).
- [Alþingi, Act No. 34/1944 on Iceland’s national flag, enacted 17 June 1944](https://www.althingi.is/lagas/nuna/1944034.html).
- [Alþingi, English parliamentary booklet, 2000 edition](https://www.althingi.is/pdf/enska_2000.pdf), historical overview of the 1918 personal union, its effective severance in 1940, and the Republic in 1944.

## Rights, provenance, and remaining decision

The cited Alþingi material is authoritative historical/legal documentation, not an explicit license grant for any embedded photograph or graphic. No public-domain or Creative Commons status is asserted, no image was downloaded, and no external asset was copied. Rights for any future archival image reference and legal/reuse status for a flag rendering remain unverified.

The identity-to-1936-start link is confirmed by installed Vanilla history, so no further choice is needed to classify this as an inherited package gap. Remaining decisions are narrower: whether to authorize a separate original reconstruction of Iceland’s documented 1918 national-flag design for the missing ladder, and what color treatment to use when the historical blue is described only as lighter/ultramarine without a reproducible exact value. A separate Denmark–Iceland composite is unsupported. For a newly released ICE where no existing tag state is available, whether the engine applies this history setter remains unverified and must not be used as an assumption in the asset handoff.

No asset, contact sheet, manifest, DDS, source image, or GFX handoff was created because this update was source research only. The missing ladder is classified as a real conditional inherited-package coverage gap, but asset production remains unapproved and the pre-1944 color remains unresolved.
