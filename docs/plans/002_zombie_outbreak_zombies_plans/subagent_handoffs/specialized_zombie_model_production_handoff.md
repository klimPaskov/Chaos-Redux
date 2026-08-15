# Specialized zombie model production handoff

Status: `blocked_before_paid_generation`.

The active working set contains the seven requested non-armored specialized zombie packages: infected, rabid, parasitic, mutant, undead, necrotic, and demonic. The base `zombies` package and all armored variants remain outside this handoff. The separately staged Wendigo reference is retained outside the active objective because its quadruped route is not enabled.

Each package has an event-scoped job root under `docs/assets/002_zombie_outbreak/models_3d/<unit>/`, exactly one hashed `refs/original/meshy_input.png`, an `input_manifest.json`, a portrait-fidelity brief, a `job.yaml`, and a manifest. Vanilla calibration meshes are copied read-only under each `refs/vanilla/` folder.

The current provider gate is recorded in `docs/assets/002_zombie_outbreak/models_3d/provider_credit_gate.json`. Meshy 6 generation, rigging, four skeletal actions per unit, material processing, PDX export, reimport proof, sourced unit audio, bespoke counters, and runtime wiring have not started because the seven-package tranche requires 329 credits before recovery and the latest balance is 144, leaving a 185-credit shortfall.

The parent owns the eventual `.gfx`, `.asset`, `common/units`, sound definitions, counter GFX, gameplay wiring, and live in-game validation. No runtime file points to any incomplete job root.

When the credit gate clears, spawn one `chaosx_3d_model_pipeline` worker per disjoint job root with `fork_context=false`, pass the exact job brief and dependency lock, keep Meshy 6 as the provider model, require the four named actions and custom-unit sound/counter receipts, and stop for parent review before runtime promotion. Failure-driven paid recovery requires a separate user-approved credit decision; planned initial generation and required animation spend does not.

## Audit outcome

No Meshy task, balance call, remesh, retexture, rig, conversion, animation, download, or other provider operation was made during this audit. No Blender model mutation, export, reimport, runtime synchronization, audio sourcing, counter production, fallback, or runtime wiring was performed.

| Package | Approval state | Actual provider image evidence | Profile and deterministic route | Exact blockers |
| --- | --- | --- | --- | --- |
| `infected_zombies` | User-accepted | One `meshy_input.png`; `1085x1450`; SHA-256 `9FF840F0984761BB81A896E656400FAE4AAA4BF35C2F5A14CB0DEA0FFD503AD4`; manifest SHA-256 `9C837D38723236FDDBE73A929DD4AE6E6C7A95124D0838362240491D86F4E2FD` | `humanoid_infected` maps to locked `humanoid_unit`; discoverable | Full-tranche credit shortfall; sound/counter intake and extra-recovery limits missing |
| `rabid_zombies` | Needs explicit user visual approval | One `meshy_input.png`; `992x1586`; SHA-256 `EBAF7F16F153C822892C04F39CD9B824885278E47123AF5CA0070B4AF204EFC2`; manifest SHA-256 `92E276334F2727B60DFC33DD4F130E781FF91670A34937C4830081CC899D0453` | `humanoid_rabid` maps to locked `humanoid_unit`; discoverable after approval | Visual approval; full-tranche credit shortfall; sound/counter intake and extra-recovery limits missing |
| `parasitic_zombies` | Canonical revision 4 needs approval; revisions 5, 6, 7, and 8 are staged candidates | Canonical `meshy_input.png`; `1024x1536`; SHA-256 `E9A60A459A96FB37B4ABB93EBB0BAF88DEB13A60ADB46E31784534285312658B`; candidate revision 5 SHA-256 `C0337E128B0115D90265FECFC07F93DB6B3BADE50BF60A4EEE32D4C1EA966038`; candidate revision 6 SHA-256 `86555A8CC91C24B7AF324EEF9D4F3C245558BFAFE7DC873DB0981B6DB1444CFE`; candidate revision 7 SHA-256 `B971618E71BEBED146582307A85F935397E503C8B62764ADE90FCA3BBAF76F88`; candidate revision 8 SHA-256 `70E47C655B3F920C2FC9FA6069B26BF1D33F11038F85402A5ED91DE1338E1186`; manifest SHA-256 `EFE290DE72EC6136B898474D5D5FBBC1BE33289BB5563E1C95CFC824BDB9747D` | `humanoid_parasitic` maps to locked `humanoid_unit`; discoverable after approval | Candidate/canonical visual approval; full-tranche credit shortfall; sound/counter intake and extra-recovery limits missing |
| `mutant_zombies` | Needs explicit user visual approval | One `meshy_input.png`; `1089x1444`; SHA-256 `48802BDA28BBF33A6FF7C8FAF63BA362CCD6229424FC77A6E7B1932495F57649`; manifest SHA-256 `5D6893AC731103B5DC90D68FCBD4C37D86CD66C08E75B6EE068F5FCB13C30914` | `humanoid_mutant` maps to locked `humanoid_unit`; humanoid rig remains deformation-gated | Visual approval; full-tranche credit shortfall; sound/counter intake and extra-recovery limits missing |
| `undead_zombies` | Needs explicit user visual approval | One `meshy_input.png`; `1065x1477`; SHA-256 `E61777858E3931412416465437523D4FE1B7BB8E6A3ED6504E3E0A5478577F8C`; manifest SHA-256 `27B4848940AFAAD67B27B45602B30BE8F1711BE9BF04BA0A4AE80862A9A2435B` | `humanoid_undead` maps to locked `humanoid_unit`; discoverable after approval | Visual approval; full-tranche credit shortfall; sound/counter intake and extra-recovery limits missing |
| `necrotic_zombies` | Needs explicit user visual approval | One `meshy_input.png`; `1080x1456`; SHA-256 `62685EAE4EC035181C9449754CF99FBA66ECB0C213354AC8B43D07288B487DFF`; manifest SHA-256 `366FBBA3F95E397903E5BE4D7394F7F5C415F0A439B640EB09927A6725757CD6` | `humanoid_necrotic` maps to locked `humanoid_unit`; discoverable after approval | Visual approval; full-tranche credit shortfall; sound/counter intake and extra-recovery limits missing |
| `demonic_zombies` | Needs explicit user visual approval | One `meshy_input.png`; `1122x1402`; SHA-256 `3899AD441676879A58002E15A99156F5B83CE348B48263CC33179A00EAB7EAA2`; manifest SHA-256 `06FAA247956B3AB54C5D7F8A5DB58388AEA07BA41A0097F0DCC818F8709FACD3` | `nonhumanoid_winged_biped` with `winged_biped`; custom Blender creature rig, never Meshy humanoid rig | Visual approval; full-tranche credit shortfall; required post-generation root/wing/digitigrade contact checks; sound/counter intake and extra-recovery limits missing |
| `wendigo_zombies` | Outside active seven-unit objective | One `meshy_input.png`; `1122x1402`; SHA-256 `5ECDB83B74264F0D33EFDB8C30085B31A8CF3B44C7730B588BB2B7AAEC136B60`; manifest match | Retained as a separate reference; excluded by `load_pilot_configs()` until an enabled quadruped rig/action route exists | Quadruped route and deformation crosswalk are not part of this handoff |

The seven active inputs are single clean full-body images rather than turnarounds, collages, or multi-view boards. The separate Wendigo input follows the same one-image rule. Each was visually compared with its named portrait, and the fidelity notes are recorded in the package manifests. Visual comparison is evidence only and does not promote the six pending active candidates to user-approved state.

## Credits and provider lineage

The verified balance is `144` credits against the indivisible `329`-credit seven-package baseline, leaving a `185`-credit shortfall. The baseline estimate is `47` credits per package: image-to-3D `30`, rig `5`, and four planned animations `12`; remesh and recovery are excluded.

Estimated credits for this audit: `0`. Consumed credits for this audit: `0`. Provider task IDs, response IDs, downloads, and provider artifact checksums: none.

## Dependency-lock and route-schema evidence

- `MESHY_API_KEY` was present and nonblank before repository intake; the secret was not printed or archived.
- Official Meshy route: `@meshy-ai/meshy-mcp-server` `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, wrapper `.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd`, schema revision `live-declaration-2026-08-05`, and exposed model selection includes `meshy-6`.
- Verified Meshy tools are `meshy_check_balance` (free), `meshy_image_to_3d` (paid; exactly one of `file_path`, `image_url`, or `input_task_id`), `meshy_get_task_status` (free; requires `task_id`), `meshy_download_model` (free; requires `task_id`), `meshy_remesh` (paid; exclusive `input_task_id` or `model_url`), `meshy_rig` (paid; exclusive `input_task_id` or `model_url`), `meshy_convert` (paid; requires `target_formats` and one model input), and `meshy_animate` (paid; requires `rig_task_id` and `action_id`). No general geometry prompt is exposed by the locked image-to-3D schema.
- Blender is `5.1.2`, build hash `ec6e62d40fa9`, Windows release build dated `2026-05-19`.
- Blender Lab MCP is tag `v1.0.0`, server `1.28.1`, git commit and observed vendor head `03004fd0216bfe5e0a3d9ac9b47d5efadc3d78c4`, with add-on manifest version `1.0.0`.
- The required `127.0.0.1:9876` bridge was initially absent, so the lock-selected Blender executable was started hidden in background mode with the required `blender_mcp` command; the follow-up socket probe passed.
- The repository adapter is `chaosx_blender_hoi4` `1.3.0`. Its callable declarations cover bounded health, candidate preparation, inspection, texture processing, export, animation import/retime/authoring, winged-biped creature segmentation/rig/action, legacy creature calibration, grounding/root correction, sanitation, reimport, and checkpoint operations. No unrestricted Blender Python or shell route was used.
- `io_pdx_mesh` is release `0.91`, installed manifest version `0.91.0`; archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2` matches the lock.
- Observed lock checksums after the route/tool update: `dependencies.lock.json` `D1B4D5BC48B77B099208A235BDFE37E446AD861E730A2E73111E673EB0374197`; `meshy_tool_schema.lock.json` `3BA8321E82BC32B78D00781C85BCE1A3DDFA566A63ECC133AB302752CD085189`; `blender_hoi4_adapter.json` `079E8183BBFABD65FA746FD3358A070DDDBCC24069352DABEDE88E2A5FC397B3`.

## Vanilla reference and copy provenance

The installed reference is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh` with `gfx/entities/units_infantry.asset#infantry_rifle_entity`, source-height record `7.351824797689915`, entity scale `0.8`, forward `-Y`, and up `+Z`. The inspected entity confirms `scale = 0.8` and the expected idle, move, attack/defend/support, retreat, death, and training state family.

The installed mesh SHA-256 is `F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA`. Every package-local `refs/vanilla/western_european_infantry.mesh` is `201966` bytes and has that exact hash.

The humanoid packages retain source height separately from effective runtime height. Demonic and Wendigo use infantry only as a comparison baseline; neither may inherit a humanoid scale by assumption.

## Missing custom-unit intake

The shared plan provides selection, idle, movement, attack, and death roles, and it identifies country/original-tag infantry selection as the selection-consumer class. The jobs still lack selected exact vanilla sound/voice precedents, per-role source and licensing requirements, exact resolved country/original-tag consumers, and action frame/phase synchronization points. No audio was downloaded or authored.

The shared plan provides the large `unit_<unit>_icon` and on-map `onmap_unit_<unit>_icon` token pattern and planned DDS folders. The jobs still lack the exact inspected installed-vanilla `interface/subuniticons.gfx` entries and DDS paths, verified frame/state sizes, sampled green palette, matching skill-local reference-family paths, and an icon-artist handoff path. No counter was produced, reused, renamed, or substituted.

Package-specific extra-recovery credit and paid-attempt limits are absent. Failure-driven recovery remains unavailable until those limits are explicitly supplied and, after a failure or rejection, separately approved.

## Files changed

- `docs/assets/002_zombie_outbreak/models_3d/infected_zombies/manifest.md`
- `docs/assets/002_zombie_outbreak/models_3d/rabid_zombies/manifest.md`
- `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/manifest.md`
- `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/manifest.md`
- `docs/assets/002_zombie_outbreak/models_3d/undead_zombies/manifest.md`
- `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/manifest.md`
- `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/manifest.md`
- `docs/assets/002_zombie_outbreak/models_3d/wendigo_zombies/manifest.md`
- `docs/plans/002_zombie_outbreak_zombies_plans/subagent_handoffs/specialized_zombie_model_production_handoff.md`

Audit artifact SHA-256 values after the latest write: infected manifest `7B80875055C27B581B437AB5659738A02C34D211F1E1C0B1258AE8F814C6CB80`; rabid `072DE147794860F9567A844E370F66A366E67B3DBE58199135D43D738D444554`; parasitic `DE9E16FAC24B04717E8521BA27CCE4584C9197AA6B2F975EEA89C00ED01A8BF4`; mutant `3E17C34D35892635A16B914CBC086C1DFB498BE318B0C44477EB368065F5FAD6`; undead `7EF2E0B5B850265307140800FEAE1B8267FB30C6F101DA1224860EB295C71027`; necrotic `0B545A28779CB37894F3415EB650F477A5B74F9B71F40D81293DE923CBF40582`; demonic `3FFD2CAA3FE3B7D974024B09B8B841E64B8DDCC291572AED3DB073415D387AD2`; Wendigo `6FD270757B98A364CEE7245AEF6474EF47C2C85368C4C6BB8DA3F9981793CD6F`.

## Validation and remaining parent work

Meaningful validation performed: image count, decoded dimensions, and SHA-256 against every active `input_manifest.json`; visual comparison of the seven active candidates and the separate Wendigo reference with their named portraits; package-local vanilla mesh hash comparison with the installed source; lock versions/checksums, actual Meshy and adapter declarations, Blender build, Blender Lab git head, `io_pdx_mesh` archive/manifest, adapter job overrides, specialized-runner routing, and bridge reachability.

Meaningful validation skipped: provider generation/status/download and credit reconciliation, geometry/material/rig/weight/action/export/reimport QA, source-to-runtime synchronization, Internet audio licensing/download checks, counter consumer/palette/DDS checks, and live HOI4 validation. These require the blocked tranche, missing intake, future artifacts, or parent-owned runtime wiring.

The enabled nonhumanoid route received an isolated Blender validation after the adapter fix: the custom winged-biped rig reported `pass`, and authored `idle`, `move`, `attack`, and `death` actions all reported `pass` with minimum ground contact at or above `-0.01m`. The grounding correction is now an absolute armature-object translation measured from the uncorrected pose per frame; it is fail-closed in the creature continuation before export.

Before paid work, the parent must obtain explicit visual approval for rabid, parasitic revision 8, mutant, undead, necrotic, and demonic; provide a verified balance covering the complete seven-unit plan; and supply sound/counter intake and extra-recovery limits. Future custom workers must use `fork_context=false` and complete per-job prompts.

No simplification or fallback was used. The package set remains incomplete and blocked; only the parent may perform runtime wiring, live-consumer validation, and the overall completion claim.
