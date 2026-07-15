# Revealed Hannibal 12-Frame Animation Plan

## Animation brief

- Asset: `leader_CBL_hannibal`
- In-game use: Event 014 ordinary revealed Hannibal country-leader portrait and reveal mechanic portrait.
- Subject: fictional alternate-history Hannibal Lecter; no actor or real-person likeness.
- Frame size: 156x210.
- Frame count: 12 separately generated/edited source frames.
- Sheet size: 1872x210, horizontal, left to right.
- Static sprite: `GFX_portrait_CBL_hannibal` and `GFX_cannibalism_revealed_portrait_static` using `leader_CBL_hannibal_static.dds`.
- Animated sprite: `GFX_cannibalism_revealed_portrait_animated` using `leader_CBL_hannibal_sheet.dds`.
- Playback: 6 fps, looping, `play_on_show = yes`, no pause.
- Anchor: bottom-centre; face, shoulders, coat collar, and backdrop remain registered.
- Source mode: built-in image generation for the static identity master, followed by twelve separate built-in identity-preserving edits of that approved master.
- Final action: he raises a blood-smeared human skull, turns it, extends his tongue, deliberately licks it, then fixes the viewer with an unnerving grin.
- Gore boundary: blood on face, hand, coat, tongue, and skull is allowed; no entrails and no gore mass obscuring the face.
- Absolute setting prohibition: no prison, jail, cell, bars, cage, barred window, lockhouse, prisoner uniform, detention corridor, handcuffs, or confinement imagery in any frame.

## Shared edit invariants for every frame call

Use the approved static portrait as the identity and composition reference. Preserve the exact same fictional man, bald head shape, facial structure, scars, pallor, coat, command webbing, shoulder piece, camera, crop, smoky command-studio backdrop, lighting direction, palette, and HOI4 painted finish. This must be a real image-model edit for the specified pose and expression, not a local transform, filter, overlay, or recolour. Keep the face and torso registration coherent. Add only one blood-smeared human skull and the hands needed to hold it. No extra people, extra skulls, text, insignia, watermark, or modern object. Never introduce prison imagery.

## Frame sequence

| Frame | Motion state | Required visual change | Prompt delta | Anchor / loop note |
| --- | --- | --- | --- | --- |
| `000` | Low rest | Skull barely visible at the lower-right edge; right hand supports it below chest level; lips closed; direct neutral stare. | Place the blood-smeared skull low at the bottom-right portrait edge, only crown and eye socket partly visible; Hannibal holds it below chest height and stares directly ahead with mouth closed. | Bottom-centre; opening state. |
| `001` | Initial raise | Skull rises into the lower chest area; eyes glance down toward it. | Raise the skull to lower chest height, reveal the supporting hand and more of the cranium, and turn Hannibal's eyes downward while keeping his head almost still. | Face and shoulders fixed. |
| `002` | Raise and turn | Skull reaches mid-chest and rotates three-quarters toward him. | Lift the skull to mid-chest, rotate its face three-quarters toward Hannibal, let his chin dip slightly, and begin a small appreciative smile. | Maintain bottom-centre registration. |
| `003` | Appraisal | Skull reaches shoulder/cheek height; he studies it. | Bring the skull beside his right cheek at shoulder height, tilt it back, and have Hannibal study the brow ridge with a cultivated, intent expression. | Torso and camera unchanged. |
| `004` | Tongue begins | Skull turns to expose temple/cheek; lips part; tongue tip appears. | Rotate the skull so its blood-smeared temple faces Hannibal, part his lips, and show only the tip of his tongue beginning to extend toward it. | Keep skull clear of his eyes. |
| `005` | Approach | Tongue extends halfway; skull held steady close to face. | Extend his tongue halfway across the gap toward the skull while the hand steadies it beside his mouth; eyes remain on the contact point. | No contact yet. |
| `006` | First contact | Tongue touches the skull's temple; expression controlled. | Show the first clear tongue contact against the blood-smeared skull temple, with Hannibal's eyes half-lidded and his hand maintaining the same grip. | Face remains readable. |
| `007` | Deliberate lick | Tongue presses and travels across skull surface; blood smear visibly changes. | Depict the peak deliberate lick: tongue pressed along the skull temple toward the cheekbone, a fresh narrow blood smear following the motion, eyes opened with predatory delight. | Peak action; no entrails. |
| `008` | Finish lick | Tongue reaches the end of the stroke; skull rotates slightly toward viewer. | Complete the lick at the skull cheekbone, turn the skull a little toward the viewer, and begin returning Hannibal's gaze outward while keeping tongue contact readable. | Start easing out. |
| `009` | Retract | Tongue retracts; blood remains on lips; direct eye contact begins. | Retract the tongue almost fully, keep the skull at cheek height, leave a small blood smear on his lips, and make direct eye contact with the viewer. | Face and backdrop fixed. |
| `010` | Grin and lower | Skull lowers to upper chest; wide unnerving grin. | Lower the skull to upper-chest height, turn it outward, and give Hannibal a broad asymmetrical grin exposing filed and broken teeth while he stares directly at the viewer. | Strong reveal beat. |
| `011` | Return low | Skull returns to lower-right edge; grin softens but remains menacing. | Return the skull to the same low bottom-right edge position as frame 000, reduce the grin to a restrained crooked smile, and keep direct predatory eye contact. | Visually close to frame 000 for a clean loop. |

## Output contract

- Source frames: `source_frames/leader_CBL_hannibal_000_source.png` through `_011_source.png`.
- Processed frames: `processed_frames/leader_CBL_hannibal_000.png` through `_011.png`.
- Static PNG: `sheets/leader_CBL_hannibal_static.png`.
- Sheet PNG: `sheets/leader_CBL_hannibal_sheet.png`.
- Review GIF: `previews/leader_CBL_hannibal_preview.gif`, 6 fps.
- Contact sheets: `previews/leader_CBL_hannibal_source_contact_sheet.png` and `previews/leader_CBL_hannibal_processed_contact_sheet.png`.
- Live DDS: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_static.dds` and `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds`.
- GIF timing: repeating `170, 170, 160` millisecond frame durations, exactly 2,000 milliseconds per 12-frame loop, averaging 6 fps despite GIF centisecond quantisation.
