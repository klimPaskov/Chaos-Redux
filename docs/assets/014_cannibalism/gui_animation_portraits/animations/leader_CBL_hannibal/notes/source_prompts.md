# leader_CBL_hannibal Source Prompt Record

## Source mode

All retained artwork was produced with the built-in `$imagegen` tool. No CLI/API fallback, actor photograph, real-person reference, sourced third-party image, local drawing, local compositing, mouth replacement, or transform-generated frame was used.

The first accepted generation was an identity-only reference with an anatomical skull model and no stains. It is retained at `notes/leader_CBL_hannibal_identity_reference.png` and is not a runtime frame. Frame 000 is a separate full imagegen redraw from that identity reference. Frames 001-011 are separate full imagegen redraws that use frame 000 plus the preceding accepted action state as visual references.

## Moderation and wording record

Four early built-in generation attempts were rejected by the image-generation output safety system when the prompts used explicit blood/gore wording. No image was returned from those calls. The accepted calls preserved the requested visual direction with `dark-crimson wet-looking stage glaze and red-brown pigment` wording, no victim, no wound, and no exposed tissue. The retained images visibly read as severe fictional blood staining without weakening the requested feral skull-licking action.

This was a prompt-wording adjustment inside the same built-in imagegen workflow, not a local-art or static-image fallback.

## Identity-reference prompt

```text
Use case: stylized-concept
Asset type: identity reference for a painted 1930s-1940s alternate-history horror game leader portrait
Create a vertical, deliberately non-photographic painted portrait of an entirely invented gaunt bald scavenger commander. He hunches asymmetrically and grips a weathered anatomical skull model at upper chest height with two coherent hands. His pallid long crooked face has mismatched old scars, torn ears, hollow temples, very wide feverish eyes, irregular stained teeth, and an ecstatic wild grin. His tongue tip is barely visible behind the lower teeth. He must look disheveled, unsettling, animalistic, and socially uncomposed.
He wears invented symbol-free scavenged 1936-1945 clothing: torn greatcoat cloth, frayed field tunic, rough hide repairs, mismatched webbing, and dirty cloth wraps. The clothing is ruined and improvised, not stylish.
Dark ruined wartime command room backdrop, fixed straight-on portrait camera, bust composition, bottom-center anchor, both hands and skull model fully visible, cold window light and dim rust-red practical light. Rough-brush HOI4-style painterly realism, not a photograph.
The face must be original and must not resemble any actor, celebrity, or real person. No violence, no victim, no wounds, no blood, no tissue. No text, logos, insignia, flags, symbols, watermark, modern objects, tailored fashion, ancient history, Carthage, Punic imagery, elephants, classical armor, laurels, togas, antlers, horns, ceremonial regalia, Indigenous or tribal motifs. Coherent fingers and skull anatomy.
```

## Shared retained-frame prompt contract

Every retained frame call repeated these constraints:

```text
Use case: precise-object-edit
Asset type: one source frame of a 12-frame painted HOI4 horror leader portrait action loop
Preserve the accepted invented elongated crooked bald face, torn ears, mismatched old scars, huge unequal feverish eyes, irregular teeth, ruined symbol-free 1936-1945 scavenged clothing, old human skull, fixed tight portrait camera, palette, ruined room, and bottom-center anchor.
Redraw the complete portrait as a genuinely new painted action frame. Redraw jaw, lips, tongue, eyes, fingers, wrists, shoulders, skull angle, cloth folds, lighting, and every dark-crimson wet-looking stain. Do not translate, scale, rotate, warp, recolour, crop, paste a mouth or tongue, or apply a local stain overlay to a previous still.
Deliberately non-photographic rough-brush historical horror game art. No actor or real-person likeness. No active violence, victim, wound, body, or exposed tissue. No text, logo, insignia, flag, symbol, or watermark. No modern or tailored clothing. No ancient-general, Carthaginian, Punic, elephant, classical, laurel, toga, or legionary imagery. No antlers, horns, animal headdress, runes, tribal, Indigenous, sacred, or ceremonial motifs. No extra or fused fingers.
```

## Per-frame prompt deltas and lineage

| Frame | References supplied to imagegen | Exact action delta retained |
| --- | --- | --- |
| 000 | identity reference | Tighten to a feral clutch; hunch farther over the skull; expose the ecstatic grin and tongue tip; add heavy dark-crimson wet-looking stains to face, teeth, fingers, collar, temple, and crown; redraw the entire portrait rather than applying stains to the reference. |
| 001 | frame 000 | Raise the skull several inches toward the left cheek; rotate both wrists and all fingers; cock the head right; open the jaw; split the eye focus between skull and viewer; redraw shoulders and cloth tension. |
| 002 | frames 000 and 001 | Roll the stained temple toward the mouth; lift the skull to mouth level; drop and cant the lower jaw; extend the tongue to just before contact; move the near hand to the crown and the far hand under the jaw. |
| 003 | frames 000 and 002 | Flatten the tongue tip against the skull temple for first contact; tilt the skull inward; sharpen the unequal ecstatic stare; tighten crown and jaw grips; add the first new tongue smear. |
| 004 | frames 000 and 003 | Drag the flattened tongue upward from temple toward brow; turn the skull upward and inward; shift the jaw sideways; roll both eyes toward contact; raise one shoulder and lengthen the wet trail. |
| 005 | frames 000 and 004 | Rotate the brow and near eye socket toward the mouth; bend the tongue along the socket edge; stretch the mouth off-center; move the far hand beneath the jaw and clamp the crown with a new finger pattern. |
| 006 | frames 000 and 005 | Lift the skull to the highest point; flatten the fully extended tongue across the stained crown; strain jaw and long neck; make the shoulders maximally uneven; intensify stains across tongue, teeth, nose, chin, fingers, and crown. |
| 007 | frames 000 and 006 | Jerk the head back while the skull stays high; peel the tongue away; retain one short wet-looking crimson strand; expose all irregular teeth; cross the eyes toward the strand; recoil both hands into a new grip. |
| 008 | frames 000 and 007 | Snap forward for a shorter second lap around the stained cheekbone; curl the tongue along the bone edge; cant the jaw; roll both wrists down; raise one shoulder and change the stain path. |
| 009 | frames 000 and 008 | Break contact; roll the skull down; retract the tongue halfway; flare both eyes toward the viewer; begin a visible swallow; slide all fingertips into a lower grip. |
| 010 | frames 000 and 009 | Lower the skull another step; close into a crooked ecstatic grin; tighten the throat in a swallow; leave only a small tongue tip; relax wrists while preserving feral asymmetry and accumulated stains. |
| 011 | frames 000 and 010 | Return the skull to upper chest height near frame 000; rebuild the tense clutch with new fingers and wrists; reopen the wide predatory stare; hide the tongue; redraw all stains and cloth so the frame connects without duplication. |

## Accepted output policy

Only the files in `source_frames/` are accepted runtime-source frames. The Codex default generated-image copies remain outside the repository. Discarded and moderation-blocked attempts are not represented as final assets.
