# Live re-authoring plans: the first five trailer units

Disposition: `unresolved`. These are working plans for live authoring under decisions 3D-3 and 3D-5, written before any authoring. They record what each action must show, its key poses and its prop controls, so authoring can start at once. They are not accepted design; the independent review of the authored result decides acceptance.

Sources read for these plans (2026-11-06): the repaired units in `C:\Users\klimp\Documents\Projects\cr-3d-wt\.tmp\unit_repair\<unit>\files\` (repair status `done` in the shared `cr-3d-units.md`), the installed `autonomous_robot` (its repair is not done yet), the audit reviewers' findings (`cr-3d-audit-findings/audit_group3.md`, `audit_group7.md`, `audit_group8.md` in the shared notes folder), each unit's `animation_*.asset`, its localisation, a read-only bone, weight and clip inventory, and rest renders from front, side and the HOI4 camera.

## Rules for every unit

- **Session.** Work in the `blender_lab` session on the hidden Blender on port 9877. Import the repaired `.mesh` through `io_pdx_mesh`, save a working `.blend` per unit under the job root, and name actions `<mesh stem>_<role>`.
- **Live keys only.** Set each key pose by hand, a few bones at a time. After each pose, render the front view and the HOI4 camera and look at them before the next change. Do not copy a pose from another unit or another role. Closing a loop by setting the first pose again on the last frame of the same action is fine.
- **Roles.** Author every role the unit's `.asset` plays, not only the six of the brief, because every wired clip shows in game. Keep the current frame counts unless a note says otherwise, so the existing `.asset` timing still fits.
- **In place.** Every role keeps the root in place. The engine moves the unit; only the pelvis bobs and sways.
- **Ground.** The planted foot sits on z = 0 at every contact key. In death, the lying body rests on the ground: nothing sinks in and nothing floats.
- **Reading at map zoom.** Each role must read from the HOI4 camera at counter size. Exaggerate the silhouette: wide stance for defend, body lean for move and retreat, a clear extension for attack.
- **Role distinctions** (the audit's most common finding):
  - idle: calm and nearly still, with breathing and a small weight shift; not a combat crouch.
  - move: a forward march loop with alternating legs, opposite arm swing and a forward lean.
  - attack: the unit's own way of fighting, with a clear wind-up, strike or fire, and recovery.
  - defend: a braced, low, wide stance, weapon or limbs covering, absorbing hits.
  - support_attack: covering fire or a secondary action, held back and visibly different from attack.
  - retreat: withdrawing; the body faces forward because the engine turns the unit, but the head looks back over the shoulder, the posture is hunched and the cadence is faster and more ragged than move.
  - training: drill at rest, slower and more formal than attack.
  - death: a one-shot hit reaction, then a fall to the ground with no frame jumps, and the final pose held.
- **Before review.** Export, reimport, run `check_unit_files.py` and `review_unit.py`, and give the sheets to a fresh reviewer.
- **Weights.** Weight defects found while posing go back to the repair session, which owns scripted weight correction, unless they belong to a new bone authored here.

## 1. portal_raider (Portal Raider)

- **Body.** Gas-masked infantryman in a long coat with a large tank backpack, carrying a minigun. Height 7.35. Rig of 46 bones: `root`, `pelvis`, `spine`, `chest`, `neck`, `head`, `pack`, both arms with clavicles and two-joint fingers (index, middle, ring, little, thumb), legs to `toe`, a `weapon` bone under `hand.R` (2,251 gun vertices) and `muzzle` under `weapon`. One locator, `portal_raider_muzzle_locator`, sits on `weapon`.
- **Roles wired.** idle 73, move 33, attack 49, defend 57, support_attack 61, retreat 41, guard 97, portal_arrival 61, wounded 49, death 91 frames.
- **Why it fails now.**
  - Every clip turns `weapon` by about 90°, so the gun floats beside the hip and neither hand grips it.
  - Eight of the ten clips share one near-static pose.
  - Death jumps from a stagger to lying on the ground.
  - Specks show through the shroud slots. That is geometry, so it goes to the repair session.
- **Prop control.**
  - Keep `weapon` under `hand.R`, which holds the rear grip.
  - Re-key `weapon` so the gun lies level at the hip, the barrel forward and the feed toward the pack.
  - Key `hand.L` on the front carry handle or top grip at every key pose, and check left-palm contact in a close-up render.
  - Close the fingers around the grips with the finger bones.
  - Don't bake a constraint: if an IK helper guides the left hand, key the visual pose only at the chosen key frames, then remove the helper.
- **Roles.**
  - **idle.** Hip carry, gun angled down 15°, weight on one leg, slow breathing in the chest, the mask turning slightly.
  - **move.** Heavy walk under the load: short stride, forward lean, the pack bobbing on `pack` a frame behind the pelvis. The gun stays level, so both hands don't swing.
  - **attack.** Brace and fire: a wide stance with the front knee bent, the gun level at the hip and pointed forward. Recoil shakes the shoulders and `weapon` at the clip's fire rhythm. The muzzle locator stays on the barrel axis.
  - **defend.** Crouched behind the gun on one knee, barrel up 10°, head low, the pack covering the back.
  - **support_attack.** Suppressing sweep: fire while turning the upper body across about 40°, feet planted.
  - **guard.** Sentry: upright, gun across the body pointing down-left, head scanning slowly. Clearly not idle: the stance is squarer and the gun is carried port arms.
  - **portal_arrival.** Stumble out of a portal: crouched landing, a hand down for balance, then rising into the hip carry.
  - **wounded.** Limp: drags one leg, hunched over the gun, one hand briefly pressed to the side.
  - **retreat.** Backing walk: the gun pointed back over the shoulder line, head turned back, hurried short steps.
  - **death.** Hit in the chest: rocks back, the knees buckle, the body falls sideways on the pack. The gun drops out of the left hand and rests on the ground under the right hand, not through the body. The fall lasts about 20 frames with no jump, then the pose holds.

## 2. autonomous_robot (Autonomous Robot)

Its repair is not done yet. Plan only; author after its row in `cr-3d-units.md` says `done`.

- **Body.** A heavy bipedal machine with a large torso and pack and forearm-mounted guns with ammunition feeds. Height 7.35. Rig of 22 bones: `Root`, `Pelvis`, `Torso`, `Neck`, `Head`, `Pack`, both arms from `UpperArm` to `Hand`, `Gun_L` and `Gun_R` under the forearms, and legs from `Thigh` to `Toe`. Separate meshes: `RB_Gun_L`, `RB_Gun_R`, `RB_MountFeed_L`, `RB_MountFeed_R`. Locators `robot_muzzle_l` and `robot_muzzle_r` sit on the guns.
- **Roles wired.** idle 97, move 49, attack 97, defend 97, support_attack 121, retreat 49, training 121, death 97 frames.
- **Why it fails now.**
  - Every clip is mirrored left and right with identical angles, and idle is nearly rest.
  - Death crumples the torso into the legs, and the armour plates stand out like fins. The plate weights go to the repair session.
  - The feet slide in move.
- **Prop control.** The guns are already rigid on `Gun_L` and `Gun_R`. Aim them by posing the forearms and give each gun a small recoil on its own bone. Check that `RB_MountFeed` follows the arm without stretching; if it stretches, report it as a weight defect.
- **Roles.**
  - **idle.** Powered stance: knees slightly bent, a slow servo settle in the torso and head, one arm lowering a few degrees. Asymmetric, never mirrored.
  - **move.** Heavy mechanical stomp. A full stride: heel strike, the weight shifting over the planted foot, the torso dipping on each step. The arms swing very little and the guns point forward-down.
  - **attack.** Both guns raised to the front at chest height, firing alternately: the left gun recoils, then the right. The torso absorbs each recoil and the knees are braced.
  - **defend.** Hunkered: knees deep, the torso low, the forearms crossed in front of the head as armour, guns outward.
  - **support_attack.** One arm firing a long burst while the other stays lowered. The torso turns into the shot, and it's different from attack's alternating fire.
  - **training.** Calibration: raise one arm, sweep it, lower it, then the other, with the head tracking each sweep. Slow and precise.
  - **retreat.** Backing away: short heavy steps, the torso turned back over one shoulder, one gun covering the rear.
  - **death.** Systems failing: one knee locks, the torso sags, the robot drops to its knees and topples forward onto its guns, with no star-shaped limbs. The plates stay on the limbs. It lies flat on the ground; the root's 0.235 height drop must end with the body resting on the ground.

## 3. xenobiological_assault_organism

- **Body.** A gaunt insectoid biped with four arms: a lower pair with hands and an upper pair with large claws. Antennae, digitigrade legs, spines on the back. Height 8.09.
- **Rig.** Meshy humanoid (24 bones) plus `UpperArmL_1..3` and `UpperArmR_1..3` from `Spine` for the claw arms.
- **Weight gaps (for the repair session).** `RightForeArm` and `RightHand` own no vertices, so the lower right forearm can't bend; this is the "flat box" arm in the audit. `neck` and `Spine` own none either. Ask the repair session to correct these weights before any authoring.
- **Roles wired.** idle 192, move 35, attack 120, defend 39, support_attack 120, retreat 39, training 176, death 76 frames.
- **Why it fails now.** Restless idle, a shuffling move, claws through the head, a crouch that drops the head into the ground, a flailing death, and retreat equal to move.
- **Props.** None. The claws are limbs on the `UpperArm*_3` bones.
- **Roles.**
  - **idle.** A predator at rest: hunched, the claw arms folded high like a mantis, the lower hands loose. Slow breathing, the antennae and head twitching. No raised waving arm.
  - **move.** A digitigrade stalk: long strides lifting the hocks high, the body level and leaning forward. The claws stay folded and bob slightly, the lower arms swing in opposition, and the head stays level.
  - **attack.** Mantis strike: draw both claw arms back, then whip them forward and down, the lower hands grabbing low. Recoil, then strike again. The claws stay in front of the head and never pass through it.
  - **defend.** Threat posture: rear up, claws spread wide and high, the lower arms covering the abdomen, a wide low stance.
  - **support_attack.** Pinning: the lower hands push forward as if holding prey, and one claw jabs repeatedly. The body stays upright; it doesn't collapse.
  - **training.** Practice strikes into the air, slower, with the head cocking between strikes.
  - **retreat.** A skittering retreat: low and fast, the body turned back, the claws raised toward the rear, the legs on a faster cadence than move.
  - **death.** Hit, then a spasm in the claws. The legs fold at the hocks and it collapses on its side, the claws curling in. The claw tips rest on the ground and don't pierce it.

## 4. temporal_guard (Temporal Continuity Guard)

- **Body.** An armoured guard with a full helmet and a glowing chest emitter, unarmed. Height 7.35. Plain Meshy humanoid rig of 24 bones, with no finger bones.
- **Roles wired.** idle 57, move 81, attack 120, defend 105, support_attack 120, retreat 53, training 121, death 281 frames.
- **Why it fails now.** Fin hands, an over-long arm in attack, the arms crossing through the helmet, a hopping-dance move, a raised knee in idle, a glow shell standing off the body, and a 281-frame death with a leg in the air.
- **Weights and geometry (for the repair session).** The fin hands come from the hand weights. The glow shell is a separate layer at the chest.
- **Props.** None. Its fighting style is a design question for the coordinator: an unarmed line guard reads oddly at map zoom. Until that is answered, the plan uses close combat with a chest-emitter pulse.
- **Roles.**
  - **idle.** At attention: feet at shoulder width, hands at the sides, chest breathing, the head turning slowly. Both feet flat.
  - **move.** A disciplined march: even stride, a measured arm swing, upright torso.
  - **attack.** Close-quarters strike: step in, a right palm or fist strike at head height, then the left, then recover to a guarded stance. The arms keep rest length and never cross the helmet.
  - **defend.** Guard stance: a forward-and-back stance, forearms raised in front of the face, absorbing two hits with a recoil of the torso.
  - **support_attack.** Field projection: plant the feet and hold both palms forward at chest height while the chest emitter faces the target, with a slow push and a hold. The arms stay forward, not raised in an X.
  - **training.** Kata: a slow sequence of block, strike and step, then return.
  - **retreat.** Disciplined withdrawal: backward-facing steps with the head turned back and one forearm raised as cover. Different from move in cadence and posture.
  - **death.** Hit in the chest: the emitter flickers (no effect here), the body staggers back, the knees buckle and it falls onto its back with the legs flat. Shorten to about 90 frames. The `.asset` timing stays, because the clip ends on a held pose.

## 5. paleogenetic_creature (Paleogenetic Shock Pack)

- **Body.** A gaunt humanoid predator with long hair, a swollen fleshy hump over the right shoulder, tentacles from the back and shoulders, a ragged skirt and bare feet. Height 8.09.
- **Rig.** Meshy humanoid (24 bones) plus four tentacle chains from `Spine`: `TentFrontL_1..4`, `TentOuterL_1..4`, `TentFrontR_1..4` and `TentOuterR_1..4`.
- **Rig fit (needs a decision before authoring).**
  - The rest render shows six tentacles and two arms, but the rig has four tentacle chains.
  - The weights are lopsided: `LeftArm` 2,333 against `RightArm` 884 dominant vertices, and `RightShoulder` 2,734. That suggests tentacles and the hump ride on the arm and shoulder bones.
  - This is the audit's "tentacles stretch to twice their length and pass through the torso".
  - **Fix (live, under 3D-3 and 3D-5):** count the tentacles from close-up renders and give each its own four-bone chain from the shoulder or back root, with no bone on the arm. Paint its weights live, then move the hump onto `Spine` or a `Hump` bone.
  - New weights for new bones are live authoring, not a scripted correction.
  - Separately, ask the repair session whether the skirt can get a few skirt bones, or failing that get weights blended over the thighs and hips, so it stops tearing into shards in death.
- **Roles wired.** idle 146, move 87, attack 120, defend 50, support_attack 120, retreat 82, training 216, death 69 frames.
- **Props.** None.
- **Roles.**
  - **idle.** Hunched predator: the head low, the tentacles hanging and curling slowly with offset timing, one hand twitching. Calm, with no fanning.
  - **move.** A loping, lurching walk: a long stride, the body pitched forward, the hump swaying a frame behind. The tentacles trail behind the body with a lag down each chain, never in front of the torso.
  - **attack.** Lunge and lash: a crouched step forward, the arms grabbing. Then the tentacles lash forward in sequence, outer pair first and front pair second, stretched along their chains, not scaled. Recover.
  - **defend.** Coiled threat: crouched, the tentacles raised and spread around the body like a fence, the arms in front. A wide low stance, no thrashing.
  - **support_attack.** Grapple: the tentacles reach forward low and pull back as if dragging prey, the arms braced.
  - **training.** Handler drill: a slow stalk forward, a stop, a sniff with the head up, the tentacles probing ahead.
  - **retreat.** A cringing backward lope: the head turned back, the tentacles pulled in over the back, a faster ragged gait.
  - **death.** Shot, then a recoil. The tentacles spasm outward, then go limp. It falls sideways onto the hump and arm and comes to rest on the ground, with the tentacles draped flat around it. No hovering.

## Order once the session starts

1. portal_raider (repair done, rig fits; prop re-seat plus ten roles).
2. temporal_guard (repair done, plain humanoid; hands and the glow shell go to repair first).
3. xenobiological_assault_organism (after the right-forearm weight fix).
4. paleogenetic_creature (after the tentacle-chain decision).
5. autonomous_robot (after its repair pass).

Open questions for the coordinator: the temporal guard's weapon or fighting style, and approval of new tentacle chains and live weights on the paleogenetic creature.
