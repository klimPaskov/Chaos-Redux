# Assassin forces unit models (2026-09-28)

Disposition: `implemented` — all five Event 039 land units have their own map models, actions, locators, effects, and vanilla-sourced sounds; in-game validation belongs to the user.
Acceptance basis: the user approved the unit-model rework on 2026-09-27, asked for every remaining model to be finished, and Part 9 and the 3D prompt of the Event 039 spec define one humanoid family with texture variants, a distinct Silent Guard, and a period armoured car.

## Runtime

| Sub-unit | Entity | Mesh and textures | Notes |
| --- | --- | --- | --- |
| `assassin_cadre` | `assassin_cadre_entity` | `gfx/models/units/039_assassin_cadre/` | Masked beret operative, folding-stock SMG, satchel, radio pack |
| `shadow_company` | `shadow_company_entity` (clone) | Cadre mesh, `chaosx_shadow_company_diffuse.dds` | Night-dyed slate-blue cloth |
| `master_assassin` | `master_assassin_entity` (clone) | Cadre mesh, `chaosx_master_assassin_diffuse.dds` | Oxblood cloth |
| `silent_guard` | `silent_guard_entity` | `gfx/models/units/039_silent_guard/` | Trench coat, bowl helmet, same SMG |
| `mechanized_assassin` | `mechanized_assassin_entity` | `gfx/models/units/039_mechanized_assassin/` | Dark gunmetal four-wheeled armoured car with a machine-gun turret |

Registration files are `gfx/entities/chaosx_assassin_cadre.{gfx,asset}`, `chaosx_assassin_cadre_variants.gfx`, `chaosx_silent_guard.{gfx,asset}`, and `chaosx_mechanized_assassin.{gfx,asset}`.
The existing counters in `interface/039_murder_mystery_counters.gfx` are unchanged.

## Route

- Bodies and the SMG are separate Meshy 7 generations; the humanoids were rigged and animated through the provider (six presets and two text-to-motion firing roles each), ingested, and grounded.
- The SMG was fitted with `lab_items` (pistol grip in the fist, `side_to: Z`, offset `[0, 0.05, -0.022]`) and joined into one atlas material.
  The provider firing roles held the weapon raised 45–55° or across the body, so the `aim_items` pass re-keyed the right hand toward a level, forward muzzle (Cadre turns 2–55°, Silent Guard 1–50°, clamped at 50°).
- The `muzzle` locator sits at the SMG muzzle on `RightHand`, oriented like the vanilla rifle muzzle (weapon forward on local −Y, up on +Z).
- Shots are timed only on frames where the measured muzzle axis is level and forward: three-round bursts with the vanilla `mg_muzzle_particle`, `mg_muzzle_flash`, and one `infantry_mg_attack` sound per burst; movement uses `infantry_move_animation`.
- Shadow Company and Master Assassin atlases come from `texture_variant.py` with the specs under `docs/assets/039_murder_mystery/models_3d/assassin_cadre/blender/working/v1/variants/`, which dye only low-saturation cloth and keep skin and the weapon cell.
- The armoured car was imported from its GLB, fitted to the vanilla armoured car's length (6.8 units, entity scale 0.6), and rigged in `lab_limbs` with a chassis, a forward turret bone, and four wheel bones weighted rigidly inside measured wheel cylinders.
  Its eight actions are authored: wheel `spin` keys for move and retreat, turret traverse with recoil for attack, support attack, and defend, turret exercise for training, and a nose drop for death.
  Its `barrel`, `left_tracks`, and `right_tracks` locators match the vanilla `US_mechanized_01.mesh` placement and world-identity orientation, and its entity mirrors `USA_mechanized_entity` (barrel particle, track dust, `mechanized_units_mg_fire`, `motorized_unit_move_animation`).

## Evidence

- Export reports with per-role reimport ground contact: `assassin_cadre/export/v3`, `silent_guard/export/v2`, `mechanized_assassin/export/v3` under `docs/assets/039_murder_mystery/models_3d/`.
- Item and aim reviews: `.../assassin_cadre/blender/working/v1/review/items_aim2/`, `.../silent_guard/blender/working/v1/review/items_aim/`; variant renders: `.../assassin_cadre/blender/working/v1/variants/model_compare.png`.
- Every role reimports at 4 mm contact except the Cadre death, where the SMG under the fallen hand rests 0.10 unit below the ground.

## Remaining limits

- The Silent Guard's aim correction is clamped at 50°, so parts of its defend and support attack still point the weapon high or low; bursts fire only on the level frames.
- The armoured car's idle engine shake is removed by grounding (the wheels ride on the chassis bone); idle carries the turret scan only.
- The car's tyre rims show slight triangle stretching where the fused provider mesh joins the wheel cylinders; it is not visible at map scale in the review renders.
- No dedicated unit sounds were sourced: new downloads need the user's permission, so all five units use vanilla infantry and armoured-car sounds.
- The four provider generations in this batch were submitted together; the credit ledger records them as one batch because the provider list does not name the job each belongs to.
