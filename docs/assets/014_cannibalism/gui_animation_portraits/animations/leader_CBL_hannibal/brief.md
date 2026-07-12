# leader_CBL_hannibal Animation Brief

- In-game use: reveal-gated ordinary Hannibal Lecter leader and command-window portrait
- Gameplay surface: `cannibalism_revealed_command_window` and revealed CBL character portrait
- Reveal boundary: this package must never be displayed before `cannibalism_reveal_complete`; the registered scripted GUI already gates the window on that global flag
- Target frame size: 156x210
- Frame count: 12
- Horizontal sheet size: 1872x210
- Static fallback sprites: `GFX_portrait_CBL_hannibal` and `GFX_cannibalism_revealed_portrait_static`
- Animated sprite: `GFX_cannibalism_revealed_portrait_animated`
- Animation rate: 6 FPS
- Looping: yes
- Play on show: yes
- Anchor: bottom-center, with the skull kept inside the lower and middle portrait safe area
- Source mode: twelve separate built-in `$imagegen` outputs; every frame is a newly rendered action pose that uses the accepted identity key only as a reference
- Subject classification: original fictional male-presenting human-origin Hannibal Lecter design, with no actor or real-person likeness
- Identity key: gaunt bald skull, pallid grey-beige skin, long asymmetrical face, crooked narrow nose, one higher cheekbone, mismatched scar patterns, bloodshot wide eyes, irregular stained teeth, torn ears, and an ecstatic predatory expression
- Clothing key: invented, symbol-free scavenged 1936-1945 command clothing assembled from a torn greatcoat, frayed field tunic, rough hide repairs, mismatched webbing, and dirty cloth wraps; no modern clothing and no recognizable national uniform
- Action: Hannibal grips a blood-wet human skull, raises and rolls it toward his mouth, extends his tongue, drags the tongue progressively across the skull, pulls away through wet gore strands, swallows, and lowers the skull into the near-start pose
- Required motion: independently redrawn jaw, tongue, lips, fingers, wrists, eyes, skull angle, blood trails, wet highlights, shoulders, and cloth folds in every frame
- Horror direction: visibly crazed, feral, severely blood-smeared and scarred, human-origin but no longer socially composed; asymmetry and predatory ecstasy must remain readable at 156x210
- Prohibitions: no actor likeness; no calm or calculating expression; no tailored black-leather fashion coat; no ancient-general, Carthaginian, Punic, elephant, classical, laurel, toga, legionary, or antique framing; no insignia, national flag, political symbol, text, watermark, active victim, or living injured person
- Final static PNG/DDS stem: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_static`
- Final sheet PNG/DDS stem: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet`
- Review GIF: `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/previews/leader_CBL_hannibal_preview.gif`
- Contact sheet: `docs/assets/014_cannibalism/gui_animation_portraits/animations/leader_CBL_hannibal/previews/leader_CBL_hannibal_contact.png`
- Target GFX file: `interface/014_cannibalism.gfx`
- Target GUI file: `interface/014_cannibalism_frontline_hunger.gui`
- Wiring precedent: offline `Graphical asset modding` wiki `frameAnimatedSpriteType`; vanilla `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, `interface/_leader_portraits.gfx`, and `common/characters/ABK.txt`; one-row horizontal sheet

Local processing may only crop, resize, align, assemble, preview, hash, and convert the accepted generated frames. It must not create the action by transforming one still.
