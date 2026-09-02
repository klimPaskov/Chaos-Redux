# IW-058 ASY portrait clearance handoff

Handoff date: 2026-09-02 (Europe/Kyiv).

This is an evidence-only clearance pass for the two existing ASY institutional portrait consumers. No gameplay, character identity, localisation, `.gfx`, central admission, runtime DDS, source master, crop, or processed PNG was changed.

## Final disposition

| Consumer | Existing identity/source treatment | Rights/date/role result | Accepted gate |
| --- | --- | --- | --- |
| `ASY_independence_wave_civic_national_assembly` / `GFX_portrait_ASY_independence_wave_civic_national_assembly` | Rev. Joel E. Werda/Warda, [Paris Peace Conference source](https://commons.wikimedia.org/wiki/File:Rev._Joel_E._Werda_at_Paris_Peace_Conference_(cropped).png) | The attributed circa-1920 Commons image is public-domain/PD-US-expired and visually identifies Werda, but the archived master is only 283x378 and no reliable record establishes that he was living and active in the required 1936 civic role. The low-resolution source cannot be safely enlarged or repainted. | **FAIL-CLOSED** |
| `ASY_independence_wave_levies_guardianship` / `GFX_portrait_ASY_independence_wave_levies_guardianship` | Shamoun Hanne Haydo, [Commons source](https://commons.wikimedia.org/wiki/File:Syriac-Aramean_Warrior_and_Leader,_Shamoun_Hanne_Haydo.png) | Identity/likeness, male framing, and village-defense leadership continuity through 1936 remain plausible. The early-20th-century image has an unknown photographer and date; the Commons `PD-Turkey` basis is not independently defensible for this package. Rights/date therefore remain `needs_user_review`, and no runtime promotion is authorized. | **FAIL-CLOSED** |

Both consumers remain source-placeholder/candidate treatments rather than accepted styled-final portraits. The user has not supplied a final HOI4-style replacement, and this worker did not operate RunPod or ImageGen.

## Existing source and runtime receipts

The durable archive currently contains only the two existing source masters at `docs/assets/portraits/006_independence_wave/`; no new source was selected or downloaded in this pass.

| Artifact | Dimensions/format | SHA-256 | Status |
| --- | --- | --- | --- |
| `docs/assets/portraits/006_independence_wave/portrait_ASY_independence_wave_civic_national_assembly_source.png` | 283x378 grayscale PNG | `b2243d791bff5c61e9b6b157c69859885dda35cd17b09415012a83de06d8f0db` | Existing Werda source; blocked on resolution and 1936 continuity |
| `docs/assets/portraits/006_independence_wave/portrait_ASY_independence_wave_levies_guardianship_source.png` | 950x1514 RGBA PNG | `2f34457778a84ae4e54f65dacedb588d97cce0e4fe78b1d52b46c61de992fe7b` | Existing Haydo source; rights/date hold |
| `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_civic_national_assembly.dds` | 156x210, 131168 bytes, one-level uncompressed BGRA | `717e5c11a5ac85d90d34f8aca53cc9611fb8ef0716c85bad885b5afb95829821` | Existing runtime source-placeholder candidate; not accepted final |
| `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_levies_guardianship.dds` | 156x210, 131168 bytes, one-level uncompressed BGRA | `4c75d0c118de632ecd0913525f7258758dbd1458edc1b96d1a7e66a5ede69eb1` | Existing runtime source-placeholder candidate; not accepted final |

There is no archived DDS under `docs/assets/portraits/006_independence_wave`; the two hashes above are the unchanged runtime hashes. Existing controlling handoffs record the Werda full-frame crop `(0,0,283,378)` and Haydo crop `(110,25,840,760)`, with decoded-pixel equality for both source crops; no crop was recreated here.

## Targeted research and rejection evidence

The strongest role-correct Levies lead was [RAB Tremma Yacob Khoshaba Aboona](https://assyrianlevies.info/rab-tremma-y-k-aboona.html): the page identifies him as born in 1900, enlisted in the Iraq Levies on 16 February 1922, and serving through 1955, which would cover 1936. The site identifies its photographs as shared by request and states `All rights reserved` on its home page, so there is no legally usable source license for this package and the images were not archived.

The exact-role alternatives remain inadmissible. [Iraq Levies in Training at Habbaniya E11584](https://commons.wikimedia.org/wiki/File:Iraq_Levies_in_Training_at_Habbaniya_E11584.jpg) is public-domain official photography dated 1939–1945, but it is an unnamed group after the 1936 baseline. [Iraqi Levies recruit, 1918](https://commons.wikimedia.org/wiki/File:Iraqi_Levies_recruit,_1918.jpg) is public-domain and unnamed, and predates the required role receipt. [Royal Air Force Levies Iraq](https://commons.wikimedia.org/wiki/File:Royal_Air_Force_Levies_Iraq.jpg) is a 2022 uploader-supplied CC BY-SA image with no named 1936 subject. None can stand in for a real named leader.

The Malik alternative remains blocked: [Malik Ismail II in Baquba](https://commons.wikimedia.org/wiki/File:Malik_Ismail_II_in_Baquba.jpg) is public-domain period photography from 1918–1919 but does not establish an active Levies or guardianship role in 1936, while [Malik Khoshaba](https://commons.wikimedia.org/wiki/File:Malik_Khoshaba.jpg) is a modern drawing and has a prior Kaiserreich ownership collision. No exact 1936 active-role receipt was found.

Additional Commons Haydo variants were not promoted. [Standing portrait of Shamoun Hanne Haydo](https://commons.wikimedia.org/wiki/File:Standing_portrait_of_Shamoun_Hanne_Haydo.jpg) is only 334x509 with no reliable date or photographer metadata, and [Aramean fighter Shamoun Hanna Haydo](https://commons.wikimedia.org/wiki/File:Aramean_fighter_Shamoun_Hanna_Haydo.jpg) carries conflicting modern upload/date evidence. Neither repairs the existing rights/date hold.

The otherwise plausible Shimun XXI lead was excluded because vanilla already owns `ASY_shimun_eshai` and the approved Kaiserreich reference owns `ASY_shimun_xxi_eshai`; it also would not preserve the existing generic institutional consumer identity. No existing DDS was relabelled or reused for either consumer.

## Wiring and review boundary

The existing sprite IDs, GFX definitions, character portrait references, and runtime paths remain unchanged. The only file added by this pass is this dated handoff. The source masters were visually inspected, and the installed vanilla leader portrait references were consulted for the native 156x210 full-portrait framing; no new image entered the package.

Offline Paradox portrait/data references and the vanilla portrait-related documentation were consulted. No RunPod, ImageGen, game launch, live consumer test, or unrelated asset/system edit was performed.

The ASY civic national assembly and levies guardianship consumers therefore cannot clear the accepted IW-058 gate from this pass. The package remains fail-closed pending a defensible named male 1936 role source for each consumer and, for grounded source-placeholder mode, a user-supplied HOI4-style final with its provider evidence.
