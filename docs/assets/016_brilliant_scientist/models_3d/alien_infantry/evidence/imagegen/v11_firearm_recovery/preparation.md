# V11 firearm recovery ImageGen preparation

Date: 2026-08-26

## Immutable source

- Source: `refs/source/user_supplied_alien_reference.png`.
- SHA-256: `17FEF636D5ADA350D92B1F432B58459B135F038BEB97CFEDA201CCF314BF984F`.
- Source mode: user-supplied and explicitly authorized for this model-recovery route.
- The source was not modified or used as the final V11 Meshy input.

## Preparation lineage

The first native ImageGen refinement preserved the alien identity and one-handed pistol but kept the pistol arm raised. Its untouched RGBA result is `native_alpha_raised_pistol.png`, SHA-256 `B682297B7D479B52B82A28CFEA9539276AFA322B9534A81D93ADC910828ACD49`. Corner alpha was zero.

Two low-A-pose edits rendered visible checkerboards as opaque RGB pixels and were rejected as provider inputs. The selected one-handed opaque source is `selected_opaque_checker_low_a_pose_v2.png`, SHA-256 `925FF969CDE30D01E8ADF97119DC8D71A8999FE12AE21BB6A17DDF3E9B204D53`. Installed `rembg` 2.0.61 was used only as the documented background-removal fallback. The resulting one-hand candidate was `refs/original/meshy_input_v11_firearm_recovery.png`, SHA-256 `A613D5328FCB7496E6FC24F8D78B5C633E3FE39081FF5E8E5CE5677E451A495B`; it was rejected at parent review because it lacked support-hand contact.

The approved two-hand opaque ImageGen source is `two_hand_low_ready_opaque_source.png`, SHA-256 `360E0496BA9EB3F817A8052DE4D8B3E1C75BB98690BFCEA15A814FF4589B1756`. It also baked the checkerboard, so the same installed `rembg` fallback produced `refs/original/meshy_input_v11_two_hand_firearm.png`, SHA-256 `CFF2E684F0D7D50A01084CEA76F2BA22CC4CF11BEB5D48AD829AD733FA2976D1`.

The final prepared input is 1024x1536 RGBA with alpha range 0-255 and zero-alpha corners. Visual review found no matte, checkerboard, cast shadow, clipped geometry, internal alpha holes, floating weapon mass, or firearm-on-back artifact.

## Exact approved two-hand edit prompt

```text
Use case: precise-object-edit
Asset type: exact-one-image Meshy 7 firearm-bearing humanoid reference
Primary request: Preserve the alien character and the exact retro-futurist ray pistol design, but change the arm pose into a natural two-handed pistol support grip at low ready. The right hand remains the trigger hand wrapped continuously around the pistol grip with the index finger aligned at the trigger guard. Bring the left hand across to cup and support the right grip/weapon frame in a normal two-handed pistol support contact. Both wrists, elbows, and shoulders must remain anatomically readable and separated from the torso. Point the barrel diagonally forward and slightly downward so the complete weapon body, support contact, barrel, and circular muzzle are fully visible and unobstructed.
Rigging pose: feet shoulder-width and flat, knees relaxed, torso upright, head facing forward; elbows modestly bent and away from the torso; no crossed forearms or hidden hands.
Transparency requirement: actual RGBA transparency outside the character. Do not paint or depict a checkerboard, white/black backdrop, studio gradient, floor, shadow, glow, reflection, or halo.
Invariants: preserve elongated gray alien head, large black almond eyes, slim proportions, uniform, belt, boots, materials, exactly one pistol, pistol silhouette/details, trigger-hand relationship, complete barrel, and circular muzzle. Full body centered and uncropped.
Avoid: firearm on back, shoulder, belt, or floating; one-handed grip; support hand missing the weapon; crossed limbs; fused arms; extra fingers; ambiguous muzzle; second weapon; text or watermark.
```

## Source-to-prepared comparison and approval

The prepared image retains the source alien's elongated gray head, black almond eyes, slim humanoid proportions, fitted uniform, belt, cuffed boots, and retro ray-pistol identity. The source's one-hand raised pose was changed to a centered two-hand low-ready pose. The right hand remains the trigger hand; the left hand cups the lower weapon body/barrel assembly as a genuine support point; the complete barrel and circular muzzle remain visible. No stock exists on this pistol, so stock/shoulder contact is not applicable.

Parent approval was received on 2026-08-26 for the exact prepared checksum `CFF2E684F0D7D50A01084CEA76F2BA22CC4CF11BEB5D48AD829AD733FA2976D1`. Pose preparation mode is `two_hand_low_ready`; a neutral T/A pose was not forced because it would break the required firearm contacts. Approval covered provider work only, not runtime promotion.
