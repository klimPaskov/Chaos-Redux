# shared_chaosx_ideas GFX fix report

Disposition: parent approved all 11 candidate assets after native-size and 4x review; all 11 DDS files were promoted with current-file hash guards.

Source plan: `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` lines 1228-1240.
Raw issue source: `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_issues.json` rows 695-701.
The group has seven plan rows: four severity 2 and three severity 3.
The mass-panic finding expands from the named `good_3` row to all five `good_1..3` and `bad_1..2` state icons.
The complete machine manifest and strict validation reports are under `docs/assets/gfx_fix_2026-10/shared_chaosx_ideas/`.

## Finding dispositions

- Severity 2, `GFX_idea_antarctica`: the registered texture was missing; a new Antarctic saucer and ice-shelf icon now occupies the exact registered path, although no current idea block consumes it.
- Severity 2, `GFX_idea_never_ending_hunger`: the opaque near-black skull matte is replaced by a clean native-alpha painted skull.
- Severity 2, `GFX_idea_mass_panic_good_3`: all five variants now use painted muted olive or brick chevrons rather than neon overlays.
- Severity 2, `GFX_idea_chemical_air_deep_strike_spirit`: the 45x45 officer spirit now depicts a period bomber over a chemical cloud; the first generated source with U.S. wing roundels was rejected and retained, and the selected v2 edit removes those unrequested insignia.
- Severity 3, `GFX_idea_chemical_operations_academy_spirit`: the 45x45 officer spirit now uses a brighter open manual and mask.
- Severity 3, `GFX_idea_jews_massacre`: the cell-door alias is replaced by a sober candle-and-cracked-star memorial icon at a new unique texture path.
- Severity 3, `GFX_idea_country_without_breath`: the full-canvas ink blot is replaced by a readable gas mask and contained smoke.

## Asset provenance and runtime results

Every selected source used built-in ImageGen with genuine transparency requested in its initial generation call.
Each full prompt is preserved at the listed path, and source, processed and final DDS hashes are recorded in the table and manifest.

| Sprite | Canvas | Source PNG and SHA-256 | Processed PNG and SHA-256 | Full prompt | Promoted runtime DDS and SHA-256 | State |
|---|---:|---|---|---|---|---|
| `GFX_idea_antarctica` | 64x64 | `source_pngs/idea_antarctica.png` (`dfbc56e940c0924ea967ec3fce54f898f0804356135b7f2533126cb3a86b3df0`) | `processed_pngs/idea_antarctica.png` (`a0b2224fe0e0e3661710ee08e502b8cfe04584d83a3b2bcbee47fb8e6fbb93bb`) | `prompts/idea_antarctica.md` | `gfx/interface/ideas/025_antarctic_ufo_race/idea_antarctica.dds` (`19b502f990ea815bab2c42c9c2ac7f2a2eb9ef174373dc87c7a5c285ee42c828`) | promoted_registered_but_unconsumed |
| `GFX_idea_never_ending_hunger` | 64x64 | `source_pngs/idea_never_ending_hunger.png` (`ffe5b845761e3e9c8903d0e9db5ff7e4dfbe11eec827b873f258b685baab1d61`) | `processed_pngs/idea_never_ending_hunger.png` (`a66901925fc18a604c6080f69309e3e8ddb8f2a60c8ac1500c6f02a848220798`) | `prompts/idea_never_ending_hunger.md` | `gfx/interface/ideas/002_zombie_outbreak/idea_never_ending_hunger.dds` (`11fb5b86685453fb21352c8ba7a8b95d9d67b99eb9d7d549b3aa1dba89402f19`) | parent_approved_and_promoted |
| `GFX_idea_mass_panic_good_1` | 64x64 | `source_pngs/idea_mass_panic_good_1.png` (`ae0454b3b4f247defb5a69497cc98e0d0f65b7a226b1702c68b9283790157892`) | `processed_pngs/idea_mass_panic_good_1.png` (`50f7274ba8fcf041fea0506e51f2ebca66ac5944d538cacdafbc65fa5e2d7cc1`) | `prompts/idea_mass_panic_good_1.md` | `gfx/interface/ideas/049_mass_panic/idea_mass_panic_good_1.dds` (`fc20f7403d9bf3f22eba5c1e6574941bc0f1eee7796d84f0f2d4aebcc88b4ad5`) | parent_approved_and_promoted |
| `GFX_idea_mass_panic_good_2` | 64x64 | `source_pngs/idea_mass_panic_good_2.png` (`d95915e69f7a269314f438819dfba9a6d68bdbf4eef0cc45f8b8adc5516e3a70`) | `processed_pngs/idea_mass_panic_good_2.png` (`8b5e238ba6aa037c0416fa748fcdeafe4d7b6515c113957e610d470941e94cd2`) | `prompts/idea_mass_panic_good_2.md` | `gfx/interface/ideas/049_mass_panic/idea_mass_panic_good_2.dds` (`a895f058e3e51c5414525239bff4b3f35ef011d77440db97aad7c4ce1eb83354`) | parent_approved_and_promoted |
| `GFX_idea_mass_panic_good_3` | 64x64 | `source_pngs/idea_mass_panic_good_3.png` (`23e205cb7323e42b6935c0a4209982b25b1435da576e01d17ff3a8b8fb59299e`) | `processed_pngs/idea_mass_panic_good_3.png` (`7398906af2a27d80221238019b13b6370c7ddea13d43618254a2161b9a992e16`) | `prompts/idea_mass_panic_good_3.md` | `gfx/interface/ideas/049_mass_panic/idea_mass_panic_good_3.dds` (`88497b6904ce5b3aca51f05a7362b78239256d2a9de827e652ee9f3129a34a0e`) | parent_approved_and_promoted |
| `GFX_idea_mass_panic_bad_1` | 64x64 | `source_pngs/idea_mass_panic_bad_1.png` (`97e8e812b3b3b2c3597fcba3b4ef9ab66b873544265f471423d811814ae7a8b9`) | `processed_pngs/idea_mass_panic_bad_1.png` (`31a1669b6510d9cd72b676bd53308cb95099a6f82930b240341c26a30cb7d7bb`) | `prompts/idea_mass_panic_bad_1.md` | `gfx/interface/ideas/049_mass_panic/idea_mass_panic_bad_1.dds` (`a29d177e6768223e5ebd0a3b51fa772fc117a9d161899c74b4d4fd9dc09cb96e`) | parent_approved_and_promoted |
| `GFX_idea_mass_panic_bad_2` | 64x64 | `source_pngs/idea_mass_panic_bad_2.png` (`95624c9ac93a0fb883dc4e817a5be5cb5e47777d703b3781b631349be6a9c821`) | `processed_pngs/idea_mass_panic_bad_2.png` (`15abdbe3816601b644c98ff3795c45beb68749e123bae2cac2fb49d972c1bb63`) | `prompts/idea_mass_panic_bad_2.md` | `gfx/interface/ideas/049_mass_panic/idea_mass_panic_bad_2.dds` (`c9572fbd106965a12aafbf4b7c8463abd379058331c0553ac809b5c50635dcec`) | parent_approved_and_promoted |
| `GFX_idea_chemical_air_deep_strike_spirit` | 45x45 | `source_pngs/idea_chemical_air_deep_strike_spirit_v2.png` (`5797ff6a615a02668d6d17584194fd2d99b57bc955ba7fefee4f435270880032`) | `processed_pngs/spirit_idea_chemical_air_deep_strike_spirit.png` (`ab216867ed0a0dd15284a556eb880738923b92fed421760c5a367d3bc4ae6b26`) | `prompts/idea_chemical_air_deep_strike_spirit_v2.md` | `gfx/interface/officer_corp/spirits/spirit_idea_chemical_air_deep_strike_spirit.dds` (`23342b159132d814192b52bab388723a020bd1cddf30428ea408a77297442c91`) | parent_approved_and_promoted |
| `GFX_idea_chemical_operations_academy_spirit` | 45x45 | `source_pngs/idea_chemical_operations_academy_spirit.png` (`9b3d5aed627e92136a1246cbb71667bfa41f62a85e80ca5e835452ae0eca1343`) | `processed_pngs/spirit_idea_chemical_operations_academy_spirit.png` (`22e63b3c8e991e5011e22f2976c024b5190611a20e59f6a0b98474b47da612c2`) | `prompts/idea_chemical_operations_academy_spirit.md` | `gfx/interface/officer_corp/spirits/spirit_idea_chemical_operations_academy_spirit.dds` (`dba166788806a4d22376b7266ce698b240808ffbed455d3e2e3bd54a9c15a548`) | parent_approved_and_promoted |
| `GFX_idea_jews_massacre` | 64x64 | `source_pngs/idea_jews_massacre.png` (`ec285c08f5b9b957d066497e8ff666d8cae9a9107bbf65eb49c5b31a25ba39b8`) | `processed_pngs/idea_jews_massacre.png` (`5992351de4bfb625d1f984fe2fca92766d999fbec7402241f3be23f9a467b9c5`) | `prompts/idea_jews_massacre.md` | `gfx/interface/ideas/022_jews_massacre/idea_jews_massacre.dds` (`fe40a85a35f58212969f3ecde2ccbbac5721e2d50cdd97cf710d7da4fca3913e`) | parent_approved_promoted_and_gfx_wired |
| `GFX_idea_country_without_breath` | 64x64 | `source_pngs/idea_country_without_breath.png` (`abba30de41af99c7ec3f5d29d9331d1997f0f1a2581e0a4b1d3f30f8a8206d14`) | `processed_pngs/idea_country_without_breath.png` (`d038ea9d0a3992d310f559966d0b863e4df3e2c1ee00e48f49e5f2fe3a20971a`) | `prompts/idea_country_without_breath.md` | `gfx/interface/ideas/010_death/idea_country_without_breath.dds` (`69ce0385765850b20a3750045447d545163aebd7ed97013567141c3d97d69691`) | parent_approved_and_promoted |

The native and 4x before/after sheets are `docs/assets/gfx_fix_2026-10/shared_chaosx_ideas/evidence/ideas_before_after_native.png` and `docs/assets/gfx_fix_2026-10/shared_chaosx_ideas/evidence/ideas_before_after_4x.png`.
The final contact sheets are `docs/assets/gfx_fix_2026-10/shared_chaosx_ideas/evidence/ideas_after_native_contact_sheet.png` and `docs/assets/gfx_fix_2026-10/shared_chaosx_ideas/evidence/ideas_after_4x_contact_sheet.png`.
The selected air-spirit v2 alpha edit preserves the original plane composition while removing wing roundels.
The initial roundel-bearing air-spirit source and prompt remain in the workspace and manifest as rejected v1 evidence.
The processed air-spirit alpha mean is 168.005 after resizing to 45x45; the parent approved it after native and 4x review.

## Reference evidence

The canonical idea and officer-spirit contact sheets were inspected before individual references.
All canonical references are under the approved skill-local `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/` root; hashes are in the manifest.
Installed vanilla definition anchors include `interface/ideas.gfx` `GFX_idea_generic_oppression` and `GFX_idea_generic_purge`, plus `interface/officer_corp_spirits.gfx` `GFX_idea_academy_scholarships_spirit` and `GFX_idea_air_power_projection_spirit`.
The exact vanilla source DDS paths and hashes are in the manifest.
The skill-local component catalog and national-spirit-background contact sheet were checked; the optional circle background was not layered because the inspected idea family uses standalone transparent painted objects and these subjects already fill their canvases.

## Parent wiring and remaining live checks

- `GFX_idea_jews_massacre` is now wired in `interface/chaosx_ideas.gfx:4` to `gfx/interface/ideas/022_jews_massacre/idea_jews_massacre.dds`; the old shared camp-administration texture remains unchanged.
- `GFX_idea_antarctica` already names `gfx/interface/ideas/025_antarctic_ufo_race/idea_antarctica.dds`; the promoted file fills that missing path.
- All other sprite names and current texture paths remain unchanged.
- `GFX_idea_country_without_breath` remains 64x64 for its dynamic modifier consumers; no separate 65x67 idea-picture consumer was found.
- The parent/user live check is to inspect national-spirit icons, the five mass-panic states, both officer-corps spirits and the relevant state-modifier lists at native size.

No GFX, GUI, gameplay, localization or cost files were edited by this worker.

