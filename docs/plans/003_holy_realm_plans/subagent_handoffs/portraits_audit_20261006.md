# Event 003 portrait audit

Date: 2026-10-06  
Disposition: blocked for provenance and the unused Final Silence portrait; visual, consumer, and frame-sheet audit completed.  
Authority: Parent assignment authorized a read-only portrait audit for Events 002 and 003. It did not authorize art generation, runtime changes, GFX edits, GUI work, or portrait acceptance.

## Verdict and source-mode boundary

The scripted consumers are generic alternate-history and supernatural Holy Realm roles, including The Bodhisattva, the Arhat administration, Buddha Mandate, Divine Sovereignty, False Buddha, and the Empty Seat. No specific named historical leader is defined by the portrait consumers. The asset prompt classifies fictional or symbolic portraits as generated, requires sourced material for real people and for real religious symbols used directly, and prohibits generated portraits of real historical leaders. This audit does not establish approval of that proposed classification. The portrait pixels and filenames alone cannot settle whether a particular Buddhist motif in this legacy set is a direct use of a real religious symbol.

All eleven static portrait DDS files and both animated portrait sheets are present and decode at the dimensions their consumers declare. Native-size review found centered, readable stage imagery and an intentionally empty Empty Seat image. The stage faces are variations of a recurring stylized iconographic figure, not pixel-identical duplicates. The two 16-frame animations contain eight distinct poses followed by mirrored return frames, which forms the expected ping-pong loop rather than a blank or frozen animation.

No portrait-specific source contract, original image/source receipt, native ImageGen prompt/output record, or approved user-final evidence was found in the ignored asset archive. Therefore the actual source mode of the current legacy textures remains unknown. The portraits cannot be certified as sourced, generated through the prescribed workflow, or approved user finals. Before any replacement, the parent must review whether each design is wholly fictional/symbolic or directly depicts a real religious symbol; if a grounded source is selected, it must remain a source placeholder pending the user's HOI4-style final.

GFX_portrait_THR_final_silence is registered but has no current consumer outside its own GFX declaration. The current final-stage effect assigns GFX_portrait_THR_empty_seat, and the terminal route hands off to Fallout. Do not wire or remove the orphan solely from its name; parent must decide whether it represents an intentionally retained compatibility asset or should be retired.

## Consumer map

| Sprite and texture | Current consumer |
| --- | --- |
| GFX_portrait_THR_godly_figure / portrait_THR_godly_figure.dds | Initial scripted country leader The Bodhisattva, created in common/scripted_effects/003_holy_realm_effects.txt:1903-1908. |
| GFX_portrait_THR_refuge_bodhisattva / portrait_THR_refuge_bodhisattva.dds | Refuge-stage leader portrait in holy_realm_set_stage_refuge. |
| GFX_portrait_THR_bodhisattva_pramudita / portrait_THR_bodhisattva_pramudita.dds | Bodhisattva-stage leader portrait and protectorate leader portrait; also used by stage/bhumi refresh logic. |
| GFX_portrait_THR_bodhisattva_acala / portrait_THR_bodhisattva_acala.dds | Bodhisattva bhumi stage refresh. |
| GFX_portrait_THR_bodhisattva_dharmamegha / portrait_THR_bodhisattva_dharmamegha.dds | Bodhisattva bhumi stage refresh. |
| GFX_portrait_THR_arhat_administration / portrait_THR_arhat_administration.dds | Arhat administration stage leader portrait. |
| GFX_portrait_THR_buddha_mandate / portrait_THR_buddha_mandate.dds | Static country leader portrait for the Buddha Mandate/Buddhahood stage. |
| GFX_portrait_THR_false_buddha / portrait_THR_false_buddha.dds | False Buddha schism leader portrait. |
| GFX_portrait_THR_divine_sovereignty / portrait_THR_divine_sovereignty.dds | Divine Sovereignty stage leader portrait. |
| GFX_portrait_THR_empty_seat / portrait_THR_empty_seat.dds | Final Silence non-terminal stage leader portrait. |
| GFX_portrait_THR_final_silence / portrait_THR_final_silence.dds | No consumer found outside interface/chaosx_characters.gfx:54-55. |
| GFX_portrait_THR_buddha_mandate_animated / portrait_THR_buddha_mandate_animated.dds | Event-log presentation via scripted localisation at common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:9928; static fallback remains the country leader portrait. |
| GFX_portrait_THR_empty_seat_animated / portrait_THR_empty_seat_animated.dds | Event-log presentation via scripted localisation at common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:9944; static fallback remains the country leader portrait. |

The current mappings are visible in interface/chaosx_characters.gfx:8-64 and stage effects in common/scripted_effects/003_holy_realm_effects.txt:1668-1810, 1903-1908, and 2004-2007. The overview confirms the older static review archive was deleted and that animated portrait sprites are presentation surfaces: docs/events/003_holy_realm/overview.md:243, 333-335.

## Visual, frame, and vanilla-reference review

Installed vanilla references were inspected from interface/_leader_portraits.gfx:65-68 and 2771-2773: Portrait_USA_Generic_land_4.dds and portrait_SOV_supreme_soviet.dds. Both are 156×210 textures, with the former showing a single leader and the latter a group/council composition. The Event003 static portraits use the same 156×210 canvas and full-canvas background; their centered stylized figure or empty-seat motif is readable at native dimensions. Compared with vanilla's portrait painting, this set has a strong symmetrical Buddhist iconographic treatment. That is visually clear and consistent across the stage, but the source route and any direct use of an actual religious symbol cannot be established by visual inspection.

The two animated sheets are 2496×210, matching sixteen contiguous 156×210 frames. interface/chaosx_characters.gfx declares noOfFrames = 16, animation_rate_fps = 4, looping = yes, and play_on_show = yes for both. Decoded frame comparison found eight distinct poses in each sheet followed by mirrored return frames; frame 0 repeats at 14 and 15, frame 1 at 13, through frame 6 at 8, with a unique midpoint frame 7. This is an intentional ping-pong sequence, not an accidental duplicate sheet or frozen placeholder. Both sheets are fully opaque. Their expected source-frame archives and prompt notes are absent, so the frame lineage remains unverified despite correct geometry and visible motion.

Decoded-pixel hashes were unique across all static textures; the two animated sheets are also distinct. The static art and frame sheets all had alpha extrema 255–255. The Empty Seat has no face by design. No cropped face, blank portrait, or exact duplicate was found. FFmpeg-decoded PNG contact sheets were used for native visual review; no in-game render was performed.

| DDS path | Bytes | Dimensions | Alpha extrema | Raw DDS SHA-256 |
| --- | ---: | --- | --- | --- |
| gfx/leaders/003_holy_realm/portrait_THR_arhat_administration.dds | 98408 | 156×210 | 255–255 | 56e976f72fda1868724fee51d58dbbe5920956f41ca46f4467d26b2cc099e5cf |
| gfx/leaders/003_holy_realm/portrait_THR_bodhisattva_acala.dds | 98408 | 156×210 | 255–255 | 5a570c0a02273d6702013970825e6c0aca8f8c3357d760f23c295971fe72fffa |
| gfx/leaders/003_holy_realm/portrait_THR_bodhisattva_dharmamegha.dds | 98408 | 156×210 | 255–255 | 9cbbc46533706384672137e62c6103779d355952d5228fab5c0c3568843c34dc |
| gfx/leaders/003_holy_realm/portrait_THR_bodhisattva_pramudita.dds | 98408 | 156×210 | 255–255 | 95e6b1e2fc1e1829ac606e67a4343e09f1e6ee5ce7f3216ed70dbf7cd599797d |
| gfx/leaders/003_holy_realm/portrait_THR_buddha_mandate.dds | 131168 | 156×210 | 255–255 | 13fd7b9e71715875d6a84194eef63be57e1beda6bd343850ba8635d4b258fef4 |
| gfx/leaders/003_holy_realm/portrait_THR_buddha_mandate_animated.dds | 2096768 | 2496×210 | 255–255 | a5b25c124437802bcef45bcd4367c8fa36f3e54e0ab8991c46c744d3c1211cf2 |
| gfx/leaders/003_holy_realm/portrait_THR_divine_sovereignty.dds | 98408 | 156×210 | 255–255 | efe6c03d743ec5302eefebc576f719672cba177fd920b6379809cf1ab52755b1 |
| gfx/leaders/003_holy_realm/portrait_THR_empty_seat.dds | 131168 | 156×210 | 255–255 | eb544fb9b8a12121c2d0c3797e4aa923a191d4a495ef36ad18225a96fd16a7b3 |
| gfx/leaders/003_holy_realm/portrait_THR_empty_seat_animated.dds | 2096768 | 2496×210 | 255–255 | b71f1321b4eb28e9cf99f9f907f06e7756fb46cb6d9070f9a2a4149b4da275bf |
| gfx/leaders/003_holy_realm/portrait_THR_false_buddha.dds | 98408 | 156×210 | 255–255 | 98cffc004861eff9beb7b1d6fca938467d18ce4feca98d9cfde447181242971b |
| gfx/leaders/003_holy_realm/portrait_THR_final_silence.dds | 98408 | 156×210 | 255–255 | e5989c9d88e41c8a1302525cdf4629f9b57ff62eb76aa961167554bbd1066726 |
| gfx/leaders/003_holy_realm/portrait_THR_godly_figure.dds | 16664 | 156×210 | 255–255 | e16dfacbab55283308867141692238bc214202048b8e95768495873a6bc4549b |
| gfx/leaders/003_holy_realm/portrait_THR_refuge_bodhisattva.dds | 98408 | 156×210 | 255–255 | d151165b15cb161065d05a45544cc3044632947fa6ca87918d944e927066b58e |

## Archive and provenance findings

The direct ignored-path check found docs/assets/portraits/003_holy_realm/ absent. docs/assets/003_holy_realm/ contains source_audio material but no portrait package. The expected docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/ directory and both expected animation portrait source folders under docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/ and portrait_THR_empty_seat/ are absent. No portrait source PNGs, crop records, original image receipts, prompt/output notes, rights attribution, or approved user-final evidence were found.

The overview says the former static source and processed review files/contact sheet were deleted by Git commit 87d441ac75 and no replacement archive is recorded at docs/events/003_holy_realm/overview.md:243. The named commit is not available in the local Git object database, so this audit cannot inspect the deleted files or independently verify their former contents. A separate ignored archive, docs/assets/003_holy_realm_buddhahood/release_animation_20261006/, contains a reviewed Mandala-symbol animation package, not portrait artwork; its manifest identifies a 420×420 holy_realm_mandala_core consumer and fourteen Mandala DDS outputs. It does not close the portrait or portrait-animation provenance gap. Git reports docs/assets/ ignored by .gitignore:80; the archives above were checked directly on disk.

## Bounded follow-up

1. Parent decision required for portrait_THR_final_silence.dds: map it to an accepted current consumer or retire the unused sprite and texture in a separately reviewed patch. The existing Final Silence stage uses the Empty Seat portrait, so no source-only change is justified.
2. Provenance is blocked for the ten active static portraits and the two animated presentation sheets. Parent should review whether a direct real Buddhist symbol is depicted in any asset and set the source mode accordingly before replacement; do not infer generated or sourced provenance from the current pixels.
3. If an asset is grounded in a real person or real religious symbol, archive the attributed source and keep the wired portrait explicitly pending the user's HOI4-style final. If the parent confirms a fictional/symbolic portrayal, use the generated route only after production is authorized and retain prompt, source, crop, preview, and DDS evidence.
4. The animated portraits need recoverable source-frame lineage or a reviewed replacement frame package before their animation provenance can be claimed. The visible ping-pong sequence and geometry are intact, but this audit did not repair or regenerate frames.
5. No runtime, GFX, character, or scripted-effect files were changed; no HOI4 session, RunPod, or live-game visual validation was used.

Review contact sheets: C:\Users\klimp\AppData\Local\Temp\portrait_audit_002_003_20261006\003_holy_realm_portraits_contact.png, portrait_THR_buddha_mandate_animated_frames_contact.png, and portrait_THR_empty_seat_animated_frames_contact.png.
