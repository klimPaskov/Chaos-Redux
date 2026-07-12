# leader_ZZZ_hannibal_wendigo Source Prompt Record

## Source mode

All sixteen retained source frames were produced with the built-in `$imagegen` tool as separate full renders. The ordinary accepted frame 000 was used only as residual identity guidance for the transformation seed. No CLI/API fallback, sourced third-party art, actor image, local drawing, local compositing, skeletal puppeting, or transform-generated frame was used.

The accepted transformation removes the ordinary package's skull prop and action. Its loop is a separate predator-crouch, jaw/claw unfurl, diagonal spring, frenzied apex, ice-shedding recoil, reverse head whip, swallow spasm, shoulder collapse, and re-crouch.

## Shared retained-frame prompt contract

Every retained frame call repeated these constraints:

```text
Use case: precise-object-edit
Asset type: one source frame of a separate 16-frame supernatural winter-horror HOI4 leader portrait action loop
Preserve residual identity from the ordinary invented man through the long crooked nose, scar map, torn ears, mismatched feverish eyes, and irregular teeth. Preserve transformed anatomy through the elongated kinked neck, visibly unequal jaw hinges, one larger eye socket, one blade-like high shoulder, one collapsed shoulder, long many-jointed claw, frost-split corpse-grey skin, blue-white ice plates, shredded frozen symbol-free 1936-1945 scavenged clothing, ruined winter command room, fixed tight portrait camera, and bottom-center anchor.
Redraw the complete portrait as a genuinely new body-horror action frame. Redraw anatomy, jaw, tongue, teeth, eyes, fingers, wrist, shoulders, neck, torso, frost fractures, ice shards, breath, dark-crimson frozen stains, cloth, lighting, and background. Do not translate, scale, rotate, warp, recolour, puppet, paste anatomy, or add local particles or overlays to a previous still.
The figure must remain dramatically inhuman, distorted, asymmetric, and frenzied; never a calm ice-skinned human.
No skull prop. No actor or real-person likeness. No active violence, victim, wound, body, or exposed tissue. No text, logo, insignia, flag, political symbol, watermark, modern clothing, tailored clothing, ancient-general, Carthaginian, Punic, elephant, classical, laurel, toga, or legionary imagery. Absolutely no antlers, horns, deer traits, animal skull headdress, totem, runes, dreamcatcher, feathers, beadwork, tribal motif, Indigenous motif or regalia, sacred symbol, ritual circle, or ceremonial garment.
```

## Per-frame prompt deltas and lineage

| Frame | References supplied to imagegen | Exact action delta retained |
| --- | --- | --- |
| 000 | ordinary frame 000 | Replace human anatomy and skull action with a crooked predator crouch, left-bent elongated neck, high/low shoulders, unequal jaw and eye sockets, crossing many-jointed claw, frost-split skin, frozen ruined clothing, dark-crimson frozen stains, and thin sideways breath. |
| 001 | ordinary frame 000 and Wendigo frame 000 | Split eye tracking between viewer and claw; flex every finger independently; bulge one jaw hinge; part the mouth; leak thin frost breath and subtly alter both shoulder heights. |
| 002 | Wendigo frames 000 and 001 | Jerk the elongated neck sharply right while torso remains left; open jaw partly; press tongue to teeth; drive high shoulder upward; recoil claw and move eye focus. |
| 003 | Wendigo frames 000 and 002 | Unfurl the near claw diagonally toward the viewer with foreshortening; torque the torso away; widen the mouth on one side; diverge the eyes; open new cheek and wrist frost fractures. |
| 004 | Wendigo frames 000 and 003 | Unhinge the jaw much farther on unequal sides; reveal frost-coated tongue; kink and lengthen the neck; advance the claw; pull the high shoulder forward and low shoulder back. |
| 005 | Wendigo frames 000 and 004 | Spring the torso forward and frame-left; lead with the high shoulder; rake the claw diagonally; turn the unequal jaw toward the arm; lash the tongue aside; shed jaw and shoulder ice. |
| 006 | Wendigo frames 000 and 005 | Extend the claw to its farthest reach; whip the head beneath the high shoulder; stretch the neck; split eye focus; add short dark-crimson strands between teeth and scatter frost shards. |
| 007 | Wendigo frames 000 and 006 | Snap the jaw partly closed off-center; cross tooth lines; curl tongue aside; hook every extended finger inward; kink the neck lower and scatter cheek/fingertip ice. |
| 008 | Wendigo frames 000 and 007 | Reach the maximum corkscrewed apex: towering/collapsed shoulders, S-neck, largest eye asymmetry, fully unequal gape, nearest claw, cracked ice plates, and strongest crimson frozen accents. |
| 009 | Wendigo frames 000 and 008 | Recoil diagonally; retract elbow while fingers remain hooked; shudder jaw partly closed; swap shoulder motion; shed temple, jaw, collar, and claw ice; track the withdrawing hand. |
| 010 | Wendigo frames 000 and 009 | Whip the head past center; form a pronounced S-neck; roll one eye up and lock the other forward; lash tongue sideways; swap shoulder heights and pull claw to chest. |
| 011 | Wendigo frames 000 and 010 | Clamp the jaw into a crooked tooth-bearing spasm; expand the throat in an unnatural swallow; compress the claw against chest; collapse one shoulder and exhale from one mouth corner. |
| 012 | Wendigo frames 000 and 011 | Collapse the current high shoulder and raise the opposite; fold backward; hang head low; crawl fingers across sternum; redirect breath downward and open new chest fissures. |
| 013 | Wendigo frames 000 and 012 | Draw unequal jaw hinges nearer without becoming human; retract tongue; curl the claw to chest; shorten but retain kinked neck; begin frost sealing and move toward starting shoulder imbalance. |
| 014 | Wendigo frames 000 and 013 | Fold into a tense crooked re-crouch; restore high/low shoulders; keep the neck extended; hover and uncurl claw; split eye focus; thin breath and shift loose ice plates. |
| 015 | Wendigo frame 000 only | Full fresh redraw within nearly matching start geometry; raise one upper finger, turn the smaller eye aside, open jaw fractionally, add a new chin wisp, and redraw all textures so last-to-first motion is smooth but hash-distinct. |

## Rejected loop-return attempt

The first generated frame 015 referenced frames 000 and 014. It remained valid source art but returned too loosely to the starting silhouette. It was rejected and not retained. A new full imagegen render referenced frame 000 directly and reduced the last-to-first processed mean absolute difference from 20.50 to 7.93 while remaining independently generated and hash-distinct.

## Accepted output policy

Only the sixteen files in `source_frames/` are accepted source frames. Discarded variants and Codex default generated-image copies are not final project assets.
