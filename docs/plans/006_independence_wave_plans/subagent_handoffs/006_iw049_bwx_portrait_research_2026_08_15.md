# IW-049 BWX Erzya-Moksha/Mordovia portrait research handoff

Date: 2026-08-15.

## Disposition

The bounded research is complete. The historical 1936 institution and officeholder are now identified, an authentic period institutional source with public-domain metadata is archived, and the named-person portrait gate remains blocked because no attributed rights-cleared Kozikov photograph was found.

No human likeness was invented, repainted, genericized, or substituted. No DDS, `.gfx`, character, country, gameplay, localisation, `156x210` PNG, ImageGen output, or RunPod operation was performed.

The institution source is a research candidate only. It must not be treated as a portrait of Andrey Yakovlevich Kozikov or wired as a runtime leader portrait without parent review of the institution-based design and insignia restrictions.

## Exact 1936 opening consumer

The strongest period-valid consumer is the Council of People's Commissars of the Mordovian ASSR (`Sovet Narodnykh Komissarov`, SNK MAССР), the autonomous-republic executive institution formed at the republic's first Central Executive Committee session on 28 December 1934.

The period-valid chairman covering the 1936 opening is Andrey Yakovlevich Kozikov (`Андрей Яковлевич Козиков`, source form `А.Я. Козиков`). The biographical reference at `http://www.knowbysight.info/KKK/10106.asp` dates his chairmanship from 28 December 1934 through September 1937, and the peer-reviewed article by Galina A. Kursheva and Pavel S. Uchvatov at `https://doi.org/10.47026/2712-9454-2021-2-1-21-29` identifies A.Ya. Kozikov as chairman and documents the April 1935 SNK composition.

The role/date gate therefore passes for Kozikov as a real male 1936 officeholder. The current BWX package is not yet wired to that historical consumer: `common/country_tags/006_independence_wave_countries.txt:32` reserves `BWX`, `common/countries/006_independence_wave_BWX.txt` is a graphical-culture shell, and `history/countries/BWX - Erzya-Moksha Federal Republic.txt` explicitly defers leaders to Event 006 runtime formation. No `common/characters/BWX.txt`, BWX character ID, BWX portrait key, or BWX recruitment line exists in the reviewed project tree.

The historical SNK/Kozykov finding must not be silently converted into a runtime identity for the synthetic Erzya-Moksha Federal Republic until the parent resolves the Event 006 formation consumer and current-map anchor.

## Vanilla carrier and ownership audit

Vanilla has no Mordovia, Mordovian, Mordvin, Erzya, Moksha, Saransk, or Kozikov character or portrait owner in the reviewed `common/characters`, `history/countries`, `gfx/leaders`, `interface`, and `localisation` roots.

The installed vanilla `history/states/255-Penza.txt` assigns the Penza state to `SOV` and adds an `SOV` core, while `common/country_tags/00_countries.txt` has no Mordovia or Erzya-Moksha tag. The vanilla Soviet country history recruits Soviet-owned characters such as `SOV_iosif_stalin` and `SOV_supreme_soviet`; those IDs and their portrait ownership must not be cloned or transferred to BWX.

The exact and variant search terms were `BWX`, `Mordovia`, `Mordovian`, `Mordvin`, `Mordvinian`, `Mordovskaya ASSR`, `Erzya`, `Erzian`, `Moksha`, `Saransk`, `Козиков`, `Андрей Яковлевич Козиков`, and `А.Я. Козиков`. The project search found only the BWX shell/history/localisation, and the vanilla search found no exact or variant person ownership.

The current Chaos Redux binding remains `disabled_no_unique_current_state` / `unbound` for IW-049, with the explicit requirement `Mordovia or Penza map group, current-map split required`. Vanilla state 255 is evidence of the SOV carrier only and is not an authoritative BWX release anchor or a permission to substitute Penza for the unresolved current-map group.

## Authentic institutional source with rights metadata

The accepted institution-source candidate is `File:Emblem of the Mordovian ASSR (1934-1937).jpg` on Wikimedia Commons: `https://commons.wikimedia.org/wiki/File:Emblem_of_the_Mordovian_ASSR_(1934-1937).jpg`.

The Commons raw wikitext identifies the source as the official Republic of Mordovia archive exhibition and credits the Central State Archive of the Republic of Mordovia, fond R-175, inventory 1, document 4. The official archive page at `http://www.e-mordovia.ru/gosudarstvennaya-vlast-rm/ministerstva-i-vedomstva/archive/virtualnye-vystavki/iz-istorii-mordovskogo-kraya/?sphrase_id=365441&PAGEN_2=2` describes the emblem and flag as approved by the First Congress of Soviets of the Mordovian ASSR on 27 December 1934, directly covering the 1934-1937 period that includes the 1936 opening.

The untouched archived original is `docs/assets/portraits/006_independence_wave/iw049_bwx_mordovian_assr_emblem_1934_1937_source.jpg`. It is a `900x910` RGB JPEG, `347156` bytes, file SHA-256 `AA053C843CF27109B4752CFC02C701559BA8C815C7F0A7E977A627DE63229349`, and Commons SHA-1 `ca4f622f1aea09598b61d206a66fb17d7e675973`.

Commons records the file as `PD-RU-exempt` / Public domain with `attribution_required=false` and an `insignia` restriction. The public-domain metadata is recorded for the emblem source; the insignia restriction and any jurisdiction-specific emblem rules remain a parent-review item. This source is authentic institutional heraldry, not an image of Kozikov.

Visual review passed the institution-source check: the image is a circular archival emblem with Mordovian/Moksha-Erzya lettering, period Soviet heraldic elements, and no human subject. Framing/crop processing was intentionally skipped because this is a source-research handoff and the emblem must not be repackaged as a human leader portrait.

The machine-readable source record is `docs/assets/portraits/006_independence_wave/processed/iw049_bwx_mordovian_assr_emblem_source_evidence_2026_08_15.json`.

## Named-person portrait source gate

No attributed, rights-cleared portrait of Andrey Yakovlevich Kozikov was accepted. The Russian Wikipedia identity page `https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B7%D0%B8%D0%BA%D0%BE%D0%B2,_%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9_%D0%AF%D0%BA%D0%BE%D0%B2%D0%BB%D0%B5%D0%B2%D0%B8%D1%87` exposes no person photograph, and the bounded Commons/person-name search produced no qualifying Kozikov portrait. The Wikipedia page is only secondary corroboration and contains a birth-year typo in its prose; it is not being used as the sole role authority or as image-rights evidence.

The machine-readable identity record is `docs/assets/portraits/006_independence_wave/processed/iw049_bwx_andrey_kozikov_identity_evidence_2026_08_15.json`.

The named-person result is `role_date_gate=PASS`, `identity_gate=PASS`, `portrait_source_gate=BLOCKED`, and `runtime_state=blocked_pending_attributed_portrait_or_explicit_institution_route`. Do not use a generic Soviet portrait, an existing SOV portrait, another Mordovian official, the emblem as a face, or a generated likeness as a substitute.

## Archive, processing, and wiring state

The source archive remains flat under `docs/assets/portraits/006_independence_wave/`: the single original is directly in the parent and no new subfolder was created. The two JSON evidence records are flat under the existing `processed/` directory.

No lossless crop, crop-equality evidence, processed portrait PNG, `156x210` file, DDS, `.gfx` entry, character definition, or runtime placeholder was created. DDS conversion was skipped because this task stops at bounded research and the named-person portrait gate is blocked. No RunPod or ImageGen action was taken.

## Parent decision boundary

Keep IW-049 outside runtime admission until the current-map anchor and Event 006 formation consumer are resolved. If the design chooses the historical named leader route, obtain an attributable Kozikov image with independently verified reuse rights before any placeholder or final is made. If the design chooses the institution route, the archived Mordovian ASSR emblem is a defensible period source for an institution-based asset, but the parent must explicitly accept the non-human subject and insignia restriction before the user creates any HOI4-style final.

No fallback or simplification was used. The only accepted source is the authentic institutional emblem, and it remains research-only pending parent review.
