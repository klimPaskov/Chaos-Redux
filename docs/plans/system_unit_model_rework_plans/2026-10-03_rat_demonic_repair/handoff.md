# Rat and demonic zombie model repair (2026-10-03)

Disposition: `implemented`, awaiting the orchestrator's in-game review. A follow-up round on the same day (coordinator items 1-4: demonic leap, demonic death landing, rat glossiness, rat mouth) is folded into the sections below and marked "follow-up".
Acceptance basis: the user rejected both models after watching live footage (rat: static raised-claw pose, rigid rod tail; demonic: near-white body, wings smearing into translucent streaks) and the orchestrator delegated the repair with the files and behaviour listed in its brief.
Nothing was committed and Hearts of Iron IV was not launched.

## Route, tools, and credits

- Route: Blender-only repair of existing non-firearm models (no new body, no provider rig or animation call). Both models already used their one Meshy rig and their one Meshy animation per role, so every replacement motion is authored in Blender, as the 3D pipeline skill requires after a provider action fails review.
- Meshy credits spent: 0. `credit_ledger.json` is unchanged (no paid call was made; `MESHY_API_KEY` was present but not needed).
- Verified stack (`evidence/verify_environment_report.json`, no findings): Blender 5.2.2 LTS (build d13f752e3b9c) at the locked path, `chaosx_blender_hoi4` adapter 1.10.51 with the locked operation list and source hashes, io_pdx_mesh 0.91.0 (archive A683DF08…, py313 compat archive 508643…, the three patched files at their locked hashes), Blender Lab MCP 1.0.3 at commit 2cea8d56 with add-on 1.0.3 on 127.0.0.1:9877 exposing `execute_blender_code`.
- Live Lab session: started hidden on port 9877 at 09:58 and used for inspection, rig tests, pose tests, and weight edits until the host stopped it at its two-hour background limit. Long authoring and bake passes ran as headless workers of the same locked Blender build (`review_cli.py blender --script …`), which the rebuild workflow prescribes for long scripts; every export, partition, and reimport went through the locked adapter.
- Authoring scripts, configs, and every authored key table are kept with each job (`blender/working/r2/{cfg,tools}`); the tables are also copied to `evidence/authored/` because `docs/assets/` is git-ignored.

## 1. Event 020 rat (`black_plague_rat_entity`)

### Root causes (triage of the shipped bytes, `evidence/triage_before/`)

1. No tail or jaw bones. The 24-bone Meshy humanoid rig has nothing behind the pelvis, so the 5-unit tail was weighted wholly to `Hips` and moved as one rigid rod. Measured from the shipped `.anim` bytes: the tail tip moved 0.001–0.012 units relative to the pelvis in every action (`evidence/rat_review/rat_motion_metrics.txt`).
2. Wrong-character actions. All eight shipped actions were human weapon presets on an empty-handed rat: idle "Combat Stance" (the raised-claw boxer pose seen in game, peak body motion 0.13 units over 40 frames), attack "Thrust Slash", defend "Two Handed Parry", training "Weapon Combo". Attack chains to idle, so in combat the brute spent most of its time in the raised-claw stance.
3. Facing. The shipped actions turned the body 90° from the vanilla infantry facing (`triage_before/sheet_rat.png`: the "front" camera sees the rat in profile; vanilla `GER_infantry_idle_rifle.anim` frame 1 faces −Y). The new actions keep the vanilla −Y facing, matching the zombie units.

### Rig and weights

- Working blend from the shipped `.mesh` through io_pdx_mesh (`r2/ck/00_import.blend`).
- Tail: a 10-bone chain `Tail_1…Tail_10` under `Hips`, joints placed on a measured centreline traced through tail cross-sections (root under the belt at (0.12, 0.40, 4.20), down behind the left calf to the tip beside the left foot), 1,583 vertices heat-weighted through a welded duplicate with overlapping capped cylinders (a first pass with a global feather produced sawtooth spikes and was rejected, `ev/test_sheet.png`); the root seam blend toward `Hips` was authored explicitly (140 tail and 72 neighbouring vertices). Pose test: `evidence/rat_review/tail_jaw_pose_test.png`.
- Jaw: `Jaw_1` under `Head`, hinge (0, −0.62, 6.62) to chin (0, −1.18, 6.55), 675 under-snout vertices (upper incisors excluded) with a 0.10 feather. It moves the underside of the snout and the beard; bites read mainly through the head snap.
- Mouth split (follow-up item 4): not done. Close-ups (`evidence/rat_review/rat_mouth_closeups.png`) and a midline profile of the snout show there is no modelled lower jaw, lip line, or mouth crease: the snout's underside runs straight into a ruff of fur cards, and the hanging incisors sit on the midline where a lip cut would have to pass. Splitting there would open a slot into the closed head shell, which the engine renders see-through (back faces are culled), and would cut through the fur cards. A visible mouth would need new geometry (a lower jaw, lips, and a dark mouth interior with its own texture area), which is a modelling addition rather than a split; it is recorded here as a possible later task.
- Thigh and shin bones were given their real segment tails (heads unchanged) so leg IK could be used as an animator control; rest equivalence 5 mm.
- Every vertex weighted, at most four influences, normalised. Skeleton: 35 bones (was 24).
- Welding: the PDX import split the shared vertices; they were re-welded to the shipped 14,997 (zero weight mismatches) and smooth shading restored so the custom normals share vertices again (44,195 export vertices, matching the shipped mesh's 44,233).

### Actions (all authored, 30 fps, keys in `evidence/authored/rat_actions_authored.py`)

Foot and tail-tip targets with IK were animator controls only; every authored control key and FK key was baked to plain per-frame FK keys and the controls were removed. Every animated bone is keyed at every key frame.

| Role | Frames | Content |
|---|---|---|
| idle | 1–91 loop | hunched breathing with heaving chest and shoulders, two sniffing bursts with jaw twitches, slow look left and right (±26°), claw flexing, weight shift, tail sweeping side to side |
| move | 1–31 loop | hunched loping walk in place: heel strike, mid-stance, toe-off, high swing; pelvis bob and yaw, counter-twisting chest, arms swinging opposite the legs, tail streaming behind and swinging |
| retreat | 1–25 loop | lower, faster scurry glancing back over the left shoulder, forearms drawn to the chest, shorter steps, tail dragging low |
| attack | 1–61 | right claw raised high and out (10–16), lunge on a forward step raking down and across (20), head thrust and bite (jaw open 25, shut 28), left backhand (34), step back to the stance |
| support_attack | 1–67 | deep crouch with both claws raised and a screech (12), spring onto the toes (20), two-claw slam (26), bite at the ground (30–33), rear up roaring with arms spread and tail lashing (40) |
| defend | 1–49 | forearms crossed before the face (8), hiss between the arms (15), flinch (21), quick left swat (28), guard (34), ease back |
| training | 1–73 loop | bent low raking the ground twice with each claw, straightening to sniff |
| death | 1–76 | struck and squealing with arms flung out (5), staggers back (12), knees buckle (20), drops to its knees (30), topples forward onto its left side (34–40), lands, settles; tail twitches twice and goes limp |

Measured on the reimported runtime bytes (`rat_motion_metrics.txt`): tail tip range relative to the pelvis 0.70–2.57 units in every action (was ≤ 0.012); idle peak body motion 0.355 units (was 0.128). Clay review sheets: `evidence/rat_review/rat_clay_review_r3.png`; per-action before/after from the actual runtime files: `evidence/rat_before_after/<role>.png`.

### Specular (follow-up item 3)

- Root cause: the shipped `black_plague_rat_spec.dds` stored the provider roughness directly in alpha (correlation +0.9999 with `roughness.png`, mean 149/255), so the shader treated the rough fur as glossy and its Fresnel cubemap term put a blue-white sheen on the black coat.
- Rebuilt from the immutable Meshy remesh download (`evidence/authored/rat_specular.py`, manifest `rat_specular_manifest.json`): R 0, G 32 (unchanged profile level; vanilla mean 31.5), B metallic, A = (255 − roughness) × 0.40. Alpha is now inverted correctly (correlation −0.9998) and sits in the vanilla infantry range: mean 42.3, p5/p95 34/78 (vanilla `GER_infantry_alt_0_specular.dds` mean 44, p95 76).
- The diffuse and normal maps are untouched. Both `meshsettings` blocks in the `.gfx` already name the same `black_plague_rat_spec.dds`, so both streams use the new map.
- Lit PDX-decoded before/after: `evidence/rat_review/rat_gloss_before_after.png` (the sheen on the shoulders and head is gone; the coat reads matte brown-black).

### Ground contact, export, reimport

- Every role grounded per frame (root keyed so the lowest vertex sits 4 mm up). The death and the jump frames of support_attack lose a few centimetres of air as a result.
- Exported through the adapter as two streams of node `char1.002` (20,000 + 9,999 triangles): the shipped single stream carried 89,997 triangle indices, above the adapter's enforced 65,535-index budget, so the locked skeletal partition was used.
- All eight `.anim` files reimported through `reimport_export` with the mesh; contact 4.0–4.07 mm at every sampled frame (`rat_ground_unit_shared/export/r2_v4/export_report.json`, proofs `blender/checkpoints/reimport_r2_v4_<role>.blend`). The installed folder was triaged again from the runtime bytes: 35 bones, 30 fps, all eight actions (`evidence/triage_after_rat/`).

### Runtime files changed

| File | Change | SHA-256 |
|---|---|---|
| `gfx/models/units/020_black_plague_rat/black_plague_rat.mesh` | tail and jaw rig, 2 streams | C8FE70D1D10164D39AC87B4D82F5AB245AC349B17521811A477D0C171B2AA5EC |
| `…/black_plague_rat_idle.anim` | new | 20C2460391B599354FEC26AFAD57C88E2AF9573150A350E817E5FBDCC176E629 |
| `…/black_plague_rat_move.anim` | new | 89930D2DCBD27942D395889B31AED84048BC301FCE1CF38A3A125262AEC9F626 |
| `…/black_plague_rat_retreat.anim` | new | 0DB243B8001FFC72B60B63B2BDD10F6342C7941BA4B628AC06FFF4A2FFF9B174 |
| `…/black_plague_rat_attack.anim` | new | F922A413D129C3CBE7B25A133A675D6C40E7A0A11FAF9003BDF715D5232469E9 |
| `…/black_plague_rat_support_attack.anim` | new | 68849E0EF1D4C3A6173F5BCEE623983512E6E117C4960B0C58D2B98655F8366C |
| `…/black_plague_rat_defend.anim` | new | C82059B4FD7F0CCE44B20DEBCF5911A98052C223E47A54F6F541C5A0CC6B20D9 |
| `…/black_plague_rat_training.anim` | new | 0E62ACA0A5FC6C5C5134F05155308FE25715C43604B5D09EDC43DBD0AE074BA6 |
| `…/black_plague_rat_death.anim` | new | 32F2441A6F6AF376879719E89B6460BBF7D46A02F85C5F0E4666B33F7082CF94 |
| `…/black_plague_rat_spec.dds` | gloss inverted and calibrated (follow-up) | E639B565F17B735F64F2BF5E8205CC5EB4C3E978642DAEE4671834C03918F3B6 |
| `gfx/entities/020_black_plague_rat.gfx` | second `meshsettings` block for `char1.002` index 1 (same three DDS maps); header comment states 2 streams | — |
| `gfx/entities/020_black_plague_rat.asset` | event times only, moved to the new phases (below) | — |

The diffuse and normal maps, the animation `.asset`, entity name, mesh name, state names, sound events, and entity scale 1.35 are unchanged. The previous runtime files (including the old specular map) are archived at `rat_ground_unit_shared/evidence/runtime_snapshot_2026_10_03_before/`.

The `.gfx` stream block is a wiring change outside the brief's "event times only" note; it was required because the exported mesh now has two streams and stream 1 would otherwise render without its material. Please review it.

Event times (s = (frame − 1) / 30): attack snarl 0.30 (wind-up, 10), rake impact 0.63 (20), bite 0.87 (jaw snaps shut 27–28); defend hiss 0.47 (15), impact 0.67 (flinch, 21); support_attack screech 0.37 (12), slam impact 0.83 (26), bite 1.07 (33); death squeal 0.13 (5), impact 1.30 (body down, 40); training impact 0.50 (first rake, 16). Idle, move, and retreat events are unchanged.

## 2. Demonic zombies (`chaosx_demonic_zombies_entity`)

### Root causes

1. Diffuse grade and palette. The shipped diffuse came from the shared humanoid-profile grade (gamma 0.72), which lifted an already pale Meshy atlas to mottled light grey (covered-texel mean 119/109/114, body 126/117/121). The Meshy texture had also lost the reference's dark wing membranes (wings mean 106/96/101 against the reference's ~60/48/49).
2. Glossiness. Specular alpha (glossiness) averaged 124/255 (p95 148), against 44 for vanilla `GER_infantry_alt_0_specular.dds`. In `PixelPdxMeshStandard` (PDX_IMPROVED_BLINN_PHONG), glossiness drives `FresnelGlossy`, which mixes the sky cubemap in at grazing angles up to the glossiness value, so the thin limbs and edge-on membranes washed toward white.
3. Wing streaks. The previous wing selection was made by position, so 39 arm-skin vertices on the back of the upper arms carried 100 % wing weight, and the membrane's lower inner edge was fused by mesh edges to the upper arms and hips. Every arm swing stretched those edges into long flat strips: measured on the shipped actions, seam edges grew by up to 0.84 units in idle, 1.67 in move, and 3.8 in attack, with 125–380 edges stretched over 0.25 units on every sampled frame. Each wing was also one long two-bone chain, so the whole membrane swung as a rigid plate.

The normal map was correct: the RRxG packing (x in G, y in A, B = 0 so no emissive) matches the shader's `UnpackRRxGNormal` and the io_pdx decode, and the provider normal is OpenGL-style. It is rebuilt only to mirror vanilla exactly (R = G, as in `GER_infantry_alt_0_normal.dds`).

### Textures (`evidence/authored/demonic_textures.py`, manifest `textures_manifest.json`)

Rebuilt from the immutable Meshy PBR download every run, never from the old runtime maps:
- Ambient occlusion (Cycles, 0.6-unit distance) and region masks (wing / head / hands-feet weights) baked from the rest mesh onto its own UV atlas (`evidence/demonic_textures/ao_regions_preview.png`).
- Diffuse: per-region colour targets from the approved reference `refs/original/meshy_input.png` (skin 113/98/101, set about 8 % darker to offset brighter in-game mesh lighting; head 116/99/103 with stronger detail so the sockets, teeth, and grin read; wings 60/48/49), provider detail kept around each target, cloth keeps its provider colour, AO multiplied (35 % floor), light unsharp mask. Covered-texel mean is now 73/63/65, body 86/75/78 (vanilla infantry 76/66/58 to 96/78/67), wings 52/42/43.
- Specular: R 0, G strength by region (skin 34, head 40, wing 46, claws 70, cloth 14; mean 45), B metallic, A = (255 − roughness) × 0.40, so the inversion is kept (correlation with roughness −0.998) and glossiness lands in the vanilla range (mean 49, p95 59).
- Normal: R = G = tangent x, B = 0, A = tangent y, resampled channel by channel.
- 1024² uncompressed BGRA DDS through the event-asset converter, the format of the other unit models.
- Lit PDX-decoded before/after (`evidence/demonic_textures/tex_before_after.png`, per action `evidence/demonic_before_after/<role>_lit.png`) shows the darker mauve body, readable face and ribs, and dark membranes at reduced (map-distance) size.

### Wings

- Each wing chain rebuilt (`evidence/authored/21_wing_rig.json`): `WingX_Arm` kept, and the single 4.7-unit `WingX_Finger` replaced by four finger struts measured from the modelled struts (A outer, 3 segments; B, C, D inner, 2 segments each), 10 bones per wing. The 6,494 left and 6,676 right membrane vertices were heat-weighted jointly to their chain through a welded duplicate, and the root was feathered only into back skin (spine, shoulders, neck), never into arms, hands, or legs. Skeleton: 44 bones (was 28).
- Membrane detached from arms and hips (`tools/wing_detach.py`): faces assigned to wing or body by wing weight; 113 junction vertices shared with arm or hip faces were ripped (wing faces get one coincident duplicate weighted like the membrane, the original keeps body weights; 67 such originals and 39 swept-in arm-skin vertices were given their arm/hip neighbour's weights; 4 orphan vertices joined the wing). Positions, UVs, custom normals, and faces are unchanged (30,931 triangles, 37,321 vertices).
- Wing keys authored for all eight actions on the provider body phases (`evidence/authored/demonic_wing_keys.py`): breathing and a stretch in idle; half-open cloak pulsing on the foot plants in move; a forward cloak with flutter in retreat; a forward shield on the dodges in defend; wide flares on each claw slash in attack; full spread in the leap, a forward mantle over the pinned prey, and a high flare for the scream in support_attack; flares on the stomps in training; flung open in death, folded forward and up while the torso lands, then lowered onto the floor beside the body (see the death landing section).
- Body motion of every action is the existing receipt-verified provider motion; only the wing curves were replaced (16 per action), quaternion sign continuity was normalised, and every role was re-grounded. In the follow-up the root height was re-authored inside the one spring of attack and support_attack (see the leap section).

Membrane integrity in world units, every 3rd frame of every action (`demonic_zombies/blender/working/r2/ev/stretch_world*.txt`):

| Role | Seam growth max, before → after | Seam edges stretched > 0.25, before → after |
|---|---|---|
| idle | 0.84 → 0.25 | 125 → 1 |
| move | 1.67 → 0.22 | 184 → 0 |
| retreat | 1.63 → 0.21 | 233 → 0 |
| defend | 2.67 → 0.36 | 284 → 2 |
| attack | 3.80 → 0.50 | 373 → 6 |
| support_attack | 3.24 → 0.55 | 381 → 8 |
| training | 2.79 → 0.34 | 284 → 4 |
| death | 3.45 → 0.46 | 361 → 7 |

The remaining seam edges are at the back root (shoulders and the wing arm), where the membrane is meant to stay attached.

### Leap (follow-up item 1)

- Root cause: the provider attack and support_attack motions float at an arbitrary height (feet 0.9–2.2 units up in most frames), so the pipeline grounds every frame to its lowest vertex. That also pinned the feet to the floor through the spring, so the leap read as standing up and the body was pulled down by up to 1.6 units.
- Fix (`tools/leap.py`, keys in `cfg/22i_leap_authored_keys.json`): only inside the leap window, the root height is re-authored as a straight path between the grounded takeoff and landing heights plus authored lift keys (Bezier, auto-clamped). Outside the window and for every other bone nothing changes. Any frame that would still dip below the 4 mm clearance is raised to it (only the first two takeoff frames of attack, by 0.14 and 0.09 units, while the feet are still planted).
  - attack: takeoff on the planted feet at 30, airborne 33–45 (lift keys 0 / 0.6 / 1.1 / 1.3 apex at 39 / 0.9 / 0.35 / 0), feet up to 1.72 units off the floor, landing on the feet at 46.
  - support_attack: takeoff at 27, airborne 29–47 (lift keys 0 / 0.75 / 1.3 / 1.5 apex at 38 / 1.15 / 0.55 / 0), feet up to 2.44 units off the floor, landing on both claws at 48 for the pin.
- Wing check against the corrected body: with the body raised, no wing vertex reaches the floor in either leap (attack: lowest wing point 0.10–0.48 units up over takeoff frames 30–32 and 0.67–4.5 in flight; support_attack: 2.8 units or more throughout), so the wing keys are unchanged for these two actions.
- Evidence: `evidence/demonic_before_after/attack_leap_landing_lit.png` and `support_attack_leap_landing_lit.png` (shipped / round 1 / round 2 on one fixed camera with the floor line), `leap_round1_vs_round2_closeup.png`, per-frame heights in `demonic_zombies/blender/working/r2/ev/22k_leap.txt`.

### Death landing (follow-up item 2)

- Root cause: the inner struts (C and D) hung down past the hips; as the body fell backward they swung under it and touched the floor 0.4–0.8 units before the torso (frames 36–46), so grounding propped the body on its wings.
- Fix: new authored wing shapes chosen by measured searches (`fall_search3/4.json`, `settle_search.json`, `settle_search2.json`): FALL (wing arms tilted toward the body's front and swept forward, inner struts folded up) at 36–46, SETTLE (struts open, wings held 0.2–0.4 up) at 52, LIE (wings sink onto the floor beside the body) at 58–68.
- Measured landing order (lowest torso / wing point above the floor, `ev/death_contact_after.txt`): 30–38 torso 0.004 / wings 0.27–1.9 (the body lands first); 40–48 torso within 0.03–0.08 of the floor while the wing root on the shoulder blade touches (that membrane root lies on the back, so it meets the floor together with the back); 50–56 torso 0.004 / wings 0.21–0.40 (still settling); 60–68 wings down, torso 0.01–0.07. Before: torso 0.43–0.77 above the floor at 36–46.
- Evidence: `evidence/demonic_before_after/death_leap_landing_lit.png`.

### Export and reimport

- Final package (after the follow-up): partitioned to the same four `char1.001` streams the `.gfx` registers (8,000 / 8,000 / 8,000 / 6,931 triangles), exported, and every `.anim` reimported with the mesh (`demonic_zombies/export/r2_v2/export_report.json`, proofs `blender/checkpoints/reimport_r2_v2_<role>.blend`): ground contact 3.9–4.0 mm at every sampled frame, except the sampled airborne frames of the two leaps (attack up to 0.034, support_attack 1.60 units above the floor), which is the leap itself. The mesh differs from the first-round export only by float noise in the tangents (at most 1.8e-7). Triage of the installed files: attack lowest point up to 1.47 units and support_attack up to 2.45 units above the floor at the sampled frames (`triage_after_demonic_report.json`). Frame ranges, the 30 fps rate, and the body phases the entity events follow are unchanged, so no event time moved (the death body-fall sound at 1.37 s still falls inside the back's landing, frames 40-46). The `.asset` comment "the body and splayed wings reach the ground near frame 42" is now slightly loose: the wings settle at 58; I left the comment alone because only event times were in scope. The installed folder was triaged again from the runtime bytes (`evidence/triage_after_demonic_sheet.png`, `triage_after_demonic_report.json`); per-action before/after: `evidence/demonic_before_after/<role>.png`.

### Runtime files changed

| File | SHA-256 |
|---|---|
| `gfx/models/units/chaosx_demonic_zombies/chaosx_demonic_zombies.mesh` | 776595014BD9960A69BACD9D32B1DD8DBE914B3AE019A903C9E919B82026F47D |
| `…_idle.anim` | 11B38D6095F83E94F9F21BCD7229CF9CA386736A3FC5446A77C2EBE06A61A08A |
| `…_move.anim` | 94B3E562094FF378F56EE59152F0B13228889C90CC32285C7C6FDED2C071CCD5 |
| `…_retreat.anim` | A71A1BAFA4EC1FF44D1779040A15D82938660FC476630672052AE2B162D55522 |
| `…_defend.anim` | 58C7A240A4388E09C77E2AD4DB702D7A2554EC22DB7B6666C73A5965674C20EF |
| `…_attack.anim` | 822F8EDCF8271ED6D6B6246406FABFE19A518D90A6EBCC6CD3000BB6602E3476 |
| `…_support_attack.anim` | 784EA9141A9B5D9ACE7A19FB641E65AEFD0F44FFD70B5F8EBAABCB9F6B9AFB62 |
| `…_training.anim` | 4FC49A75F11DB2B787C8AB1F68822A8A7AF55EA65CA43B4F38E37DC03F1DF2C6 |
| `…_death.anim` | 76C7652A60EFCEA8EE4A9790523C1273CE5FB35B3DCC37C4DFC29070457976DA |
| `…_diffuse.dds` | A75020829AA3988C681C22610F734D7454F1CA3BBB5F6AA05DAF576EC928460C |
| `…_specular.dds` | 0B8B893FD2AF916D6D4C9C1BF074E00FA951EE2DB1F63AE19DDAABFE38A087DA |
| `…_normal.dds` | D970353E55253E6F26184EBF78826AF9088DC3AF3BB956F558E3C242DFB28C66 |

`gfx/entities/chaosx_demonic_zombies.gfx` and `.asset` are unchanged. The previous runtime files are archived at `demonic_zombies/evidence/runtime_snapshot_2026_10_03_before/`.

## Remaining risks and limits

- In-game look is unverified; the lit previews approximate the PDX shader in EEVEE and cannot show HOI4's exact light, fog, or map tint. If the body still reads too pale at map distance, the next step is the skin target in `demonic_textures.py` (one constant), rebuilt from the provider base.
- Demonic death: resolved in the follow-up; the remaining contact detail is the wing root on the shoulder blade meeting the floor together with the back (torso within 0.03–0.08 units at frames 40–48).
- Demonic leaps: resolved in the follow-up for the one spring in each attack. Other frames of these actions stay per-frame grounded, so the provider's other airborne moments (none read as leaps in the side sequences) remain on the ground.
- Demonic membrane edges still stretch while fanned (up to 0.9 units in flares) because the modelled membrane is pleated at rest; no tearing or seam streaks were measured.
- The demonic arm chain keeps the provider's elbow placed about 0.9 units behind the arm geometry; it was not reported and was left alone.
- Rat: no visible mouth opening (see the jaw note: the model has no lower jaw or lip line to split); the bite reads through the head snap. The rat's glossiness was fixed in the follow-up.
- Rat walk and scurry are keyframed cycles, not motion capture; stride and bob were tuned from side renders.
- Counters and sounds were not changed; no new sound files were added.

## Evidence index (this folder)

- `evidence/rat_frames.png`, `demon_frames.png`, `demon_tex.png`: the orchestrator's in-game evidence.
- `evidence/triage_before/`: triage sheets and report of both shipped models.
- `evidence/triage_after_rat/`, `evidence/triage_after_demonic_*`: triage of the installed runtime bytes.
- `evidence/rat_before_after/`, `evidence/demonic_before_after/`: per-action before/after sheets (triage renders of shipped versus installed bytes; `_lit` sheets are PDX-decoded EEVEE renders).
- `evidence/rat_review/`: clay review, tail/jaw pose test, motion metrics.
- `evidence/demonic_textures/`: texture before/after and baked maps preview.
- `evidence/authored/`: every authored key table (including `22i_leap_authored_keys.json`), rig config, texture script (`demonic_textures.py`, `rat_specular.py`), and texture manifest.
- `evidence/demonic_before_after/*_leap_landing_lit.png`, `leap_round1_vs_round2_closeup.png`: follow-up leap and death evidence.
- `evidence/rat_review/rat_gloss_before_after.png`, `rat_mouth_closeups.png`: follow-up rat evidence.
- `evidence/verify_environment_report.json`: dependency verification.
- Per-frame triage renders: `rat_ground_unit_shared/evidence/repair_2026_10_03_triage_frames/` (git-ignored workspace).
