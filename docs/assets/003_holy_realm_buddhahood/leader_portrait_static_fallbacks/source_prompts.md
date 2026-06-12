# Holy Realm Static Leader Portrait Source Prompts

Generation mode: `$imagegen`, one generated 4x2 static portrait source sheet split into eight distinct source PNGs.

Input image: `source_png/portrait_THR_godly_figure_reference.png`, converted from `gfx/leaders/THR/portrait_THR_godly_figure.dds` and used as the identity/edit anchor.

Source sheet prompt:

> Use the provided reference image as the edit target and identity anchor: a compact orange masked Holy Realm godly figure with large eyes, jeweled crown, ornate side ornaments, and two small sun/moon discs. Create a production-ready 4 columns x 2 rows source sheet for eight modified versions of that same portrait. Each panel must remain recognizably derived from the reference image: same central mask-like face, crown silhouette, front-facing bust portrait, sacred Himalayan icon-painting feel, and leader-portrait crop. Do not make unrelated new people. Do not use a simple filter, vignette, hue shift, or glow overlay; each panel should be an actual imagegen transformation of costume, expression, ornaments, halo, and ritual state while preserving the original identity. No text, no labels, no UI, no watermark. Order panels left-to-right, top row then bottom row: 1 Refuge Bodhisattva: humbler softened version of the same orange mask, worn saffron cloth, refuge halo; 2 Pramudita Bodhisattva: joyful awakened version of the same face, lotus-gold crown additions; 3 Acala Bodhisattva: wrathful protector transformation of the same mask, darker blue-black armor and flame crown accents, no gore; 4 Dharmamegha Bodhisattva: cloud-of-dharma elder transformation, same face under pale silver rain-cloud mandala; 5 Arhat Administration: austere administrative transformation, same mask and crown restrained, beads and seal-like ornaments; 6 False Buddha: corrupted pretender transformation of the same face, cracked gold mask, red-black halo, unsettling but not a new person; 7 Divine Sovereignty: imperial transformation of the same masked figure, heavier crown, black-gold mandala and regalia; 8 Final Silence: ashen terminal transformation of the same face, muted sealed-mouth mask, fading halo. High contrast, readable at 156x210.

Generated source sheet archived at `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/source_png/holy_realm_static_portraits_generated_source_sheet.png`.

| Panel | Sprite alias | Source PNG |
| --- | --- | --- |
| 1 | `GFX_portrait_THR_refuge_bodhisattva` | `source_png/portrait_THR_refuge_bodhisattva_source.png` |
| 2 | `GFX_portrait_THR_bodhisattva_pramudita` | `source_png/portrait_THR_bodhisattva_pramudita_source.png` |
| 3 | `GFX_portrait_THR_bodhisattva_acala` | `source_png/portrait_THR_bodhisattva_acala_source.png` |
| 4 | `GFX_portrait_THR_bodhisattva_dharmamegha` | `source_png/portrait_THR_bodhisattva_dharmamegha_source.png` |
| 5 | `GFX_portrait_THR_arhat_administration` | `source_png/portrait_THR_arhat_administration_source.png` |
| 6 | `GFX_portrait_THR_false_buddha` | `source_png/portrait_THR_false_buddha_source.png` |
| 7 | `GFX_portrait_THR_divine_sovereignty` | `source_png/portrait_THR_divine_sovereignty_source.png` |
| 8 | `GFX_portrait_THR_final_silence` | `source_png/portrait_THR_final_silence_source.png` |

Buddha Mandate and Empty Seat static DDS files are sourced from frame 000 of their dedicated animation packages.
