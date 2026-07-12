# leader_ZZZ_hannibal_wendigo Animation Brief

- In-game use: reveal-gated transformed Hannibal Lecter leader and Wendigo command-window portrait
- Gameplay surface: `cannibalism_wendigo_command_window` and transformed ZZZ character portrait
- Reveal boundary: this package must never be displayed before `cannibalism_reveal_complete`; the registered scripted GUI additionally requires `cannibalism_wendigo_route_active`
- Target frame size: 156x210
- Frame count: 16
- Horizontal sheet size: 2496x210
- Static fallback sprites: `GFX_portrait_ZZZ_hannibal_wendigo` and `GFX_cannibalism_wendigo_portrait_static`
- Animated sprite: `GFX_cannibalism_wendigo_portrait_animated`
- Animation rate: 6 FPS
- Looping: yes
- Play on show: yes
- Anchor: bottom-center, with deliberately asymmetric shoulders and head motion contained inside the portrait canvas
- Source mode: sixteen separate built-in `$imagegen` outputs; every frame is a newly rendered body-horror pose using the accepted identity and transformation keys only as references
- Subject classification: original fictional male-presenting supernatural transformation of the revealed Hannibal Lecter design, with no actor or real-person likeness
- Human continuity key: traces of the gaunt bald skull, long crooked nose, unequal cheekbones, scar map, bloodshot eyes, and irregular teeth remain recognizable beneath the transformation
- Altered anatomy key: elongated crooked neck, uneven jaw hinges, stretched mouth, one larger eye socket, one raised blade-like shoulder, one dropped shoulder, long many-jointed fingers, frost-split skin, exposed dark fictional tissue, and an emaciated torso twisted off-axis; no antlers or horns
- Clothing key: frozen remnants of the same invented symbol-free scavenged 1936-1945 coat and field tunic, shredded by asymmetric anatomy and fused only as ruined cloth, never ceremonial regalia
- Action: an asymmetric predatory crouch develops into eye-tracking, finger flexion, a sideways neck jerk, jaw unhinging, a forward diagonal lunge, claw reach, frenzied apex, ice-shedding recoil, crooked swallowing spasm, and a tense near-start crouch
- Required motion: independently redrawn anatomy, jaw hinges, tongue, teeth, fingers, wrists, eyes, shoulders, neck, torso twist, frost fractures, ice shards, breath, and icy blood in every frame
- Horror direction: dramatically inhuman, distorted, frenzied, and less human than the ordinary package; no symmetrical calm monster portrait and no merely recoloured or ice-skinned human
- Cultural boundary: no antlers, horns, animal skull headdress, totem, runes, dreamcatcher, feathers, beadwork, tribal motif, Indigenous regalia, sacred symbol, ritual circle, ceremonial garment, or claim of cultural authenticity
- Other prohibitions: no actor likeness; no ancient-general, Carthaginian, Punic, elephant, classical, laurel, toga, legionary, or antique framing; no insignia, national flag, political symbol, text, watermark, active victim, or living injured person
- Final static PNG/DDS stem: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_static`
- Final sheet PNG/DDS stem: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet`
- Review GIF: `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/previews/leader_ZZZ_hannibal_wendigo_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_ZZZ_hannibal_wendigo/previews/leader_ZZZ_hannibal_wendigo_contact.png`
- Target GFX file: `interface/014_cannibalism.gfx`
- Target GUI file: `interface/014_cannibalism_frontline_hunger.gui`
- Wiring precedent: offline `Graphical asset modding` wiki `frameAnimatedSpriteType`; vanilla `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, `interface/_leader_portraits.gfx`, and `common/characters/ABK.txt`; one-row horizontal sheet

Local processing may only crop, resize, align, assemble, preview, hash, and convert the accepted generated frames. It must not create the anatomy or action by transforming one still.
