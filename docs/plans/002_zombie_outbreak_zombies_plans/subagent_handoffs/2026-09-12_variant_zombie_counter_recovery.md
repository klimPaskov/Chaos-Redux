# Variant zombie counter recovery handoff

Disposition: `implemented` for bounded artifact production and `needs_user_review` for parent visual acceptance.

This handoff covers only the four requested bespoke counter packages: `parasitic_zombies`, `mutant_zombies`, `necrotic_zombies`, and `demonic_zombies`.

The owned files are each exact `docs/assets/002_zombie_outbreak/models_3d/<unit>/counters/` folder and this handoff file.

No runtime GFX or DDS file, model file, gameplay file, localisation file, sound file, dependency lock, or parent package manifest was edited.

## Reference gate

The installed vanilla definition was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx` before production.

The exact installed references were read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds` and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`.

The canonical contact sheets were inspected before the individual reference PNGs at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/contact_sheet.png` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/contact_sheet.png`.

The canonical individual review PNGs were `.../units/land/counters_large/unit_infantry_icon.png` and `.../units/land/map_counters/onmap_infantry.png` under that same canonical reference root.

The large reference is a 152x42 RGBA two-frame strip with 76x42 frames, and the small reference is a 60x12 RGBA two-frame strip with 30x12 frames.

Frame order follows the installed consumer: frame 0 is the normal state and frame 1 is the pale sparse schematic state.

The installed normal large palette contains the required exact `#496a49` RGB anchor, and the corrected palette mapper selects from that native palette without arbitrary color injection.

All produced visible RGB values are sampled from the corresponding installed reference frame palette; no arbitrary green, renamed vanilla art, copied existing counter, or resized unrelated icon was used.

## Production method

All sixteen selected source frames were generated with native ImageGen calls requesting genuine transparency in the initial call, a single centered subject, and no frame, text, terrain, checkerboard, or opaque background.

The unmodified native outputs are retained as `source/imagegen_large_frame0.png`, `source/imagegen_large_frame1.png`, `source/imagegen_small_frame0.png`, and `source/imagegen_small_frame1.png` in every unit package.

Exact native ImageGen origin paths are recorded in each package's `source/native_imagegen_origins.md`, and source-copy hashes are recorded in both that origin record and `validation.json`.

The existing model visibility references supplied anatomy guidance only and were never used as runtime source pixels.

Parasitic art uses the measured neutral front reference and preserves the bulbous one-sided parasitic shoulder/head growth, dominant claw, and hanging tendrils.

Mutant art uses the recovered neutral front reference and preserves the heavy asymmetric body, long oversized arms, and dragging hands.

Necrotic art uses the recovered neutral front reference and preserves the thin decayed humanoid, narrow shoulders, sagging torso, and bone-like gaps.

Demonic art uses both resume neutral front and neutral right references and preserves the bat wings, hooked claws, angular horns, digitigrade legs, and clawed feet.

Several native sources contained low-alpha halo values, so the verified Pillow 11.1.0 fallback cleared only source alpha values 1..31 before premultiplied resize; untouched sources remain preserved and RGB was never used as a chroma key.

The corrected mapper uses float luminance arithmetic and the full sampled value distribution; `validation.json` records exact `#496a49` presence when the source luminance naturally selects that native palette entry.

The repository converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` produced the evidence DDS files, and every decoded DDS round-trip is pixel-equal to its processed PNG sheet.

## Runtime identifiers and parent boundary

Each package records the exact large token `GFX_unit_<unit>_icon_medium`, small token `GFX_unit_<unit>_icon_medium_white`, large destination `gfx/interface/counters/divisions_large/unit_<unit>_icon.dds`, small destination `gfx/interface/counters/divisions_small/onmap_unit_<unit>_icon.dds`, owning definition `interface/chaosx_subuniticons.gfx`, unit consumer `common/units/zombies.txt`, and sprite consumer `chaosx_<unit>`.

The existing runtime destinations were preserved for parent review and are not claimed as updated.

All eight current runtime DDS files exist at 152x42 or 60x12 but have different SHA256 bytes from the new evidence DDS files, so the current runtime/evidence discrepancy is intentional and recorded below.

`armored_necrotic_zombies` and `armored_demonic_zombies` resolve shared sprites in `common/units/zombies.txt` but armored counters are outside this bounded task.

## Artifact inventory and hashes

The following hashes are SHA256 of the exact files in the workspace at handoff time.

| Unit | Role | Workspace path | SHA256 |
| --- | --- | --- | --- |
| parasitic_zombies | source large frame 0 | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/source/imagegen_large_frame0.png` | `377475e911a970c36fd8b1d8eaa9c53767dfb3b9f8804b2eeabe5e46dab1c8c8` |
| parasitic_zombies | source large frame 1 | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/source/imagegen_large_frame1.png` | `3a5a013d3c8311c81b230b13d752f2d46d2a0ef678579f5ac7f79b51e1bbd19f` |
| parasitic_zombies | source small frame 0 | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/source/imagegen_small_frame0.png` | `580eb17694fa1353f2bcaed1907605f4337e2725ae8df5e568c7b1c86a389c50` |
| parasitic_zombies | source small frame 1 | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/source/imagegen_small_frame1.png` | `04105b8094ebfa6a03df632f73ad9e9ceb8a15fbcda9f2b3eb6d17dbd23e78ed` |
| parasitic_zombies | processed large sheet | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/processed/large_unit_parasitic_zombies_icon.png` | `b72f4f3a49454a35e8cad72f84444fbc7bf2c5d29017585cb151282b6dd304e4` |
| parasitic_zombies | processed small sheet | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/processed/small_onmap_unit_parasitic_zombies_icon.png` | `0be2d8eba25fa6050933587588ceea82fe6c076d973a8d7a8baf16a50f2791a6` |
| parasitic_zombies | evidence large DDS | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/large/unit_parasitic_zombies_icon.dds` | `c5f830fd94f874e31343071e3d3b905f06939e0e2fdd86664fe4a5829c52f07c` |
| parasitic_zombies | evidence small DDS | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/small/onmap_unit_parasitic_zombies_icon.dds` | `89d233328a5b83292b29be513b2524825f83d0548c571e6eb26b908ba7978937` |
| parasitic_zombies | large decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/decoded/large_parasitic_zombies_icon_roundtrip.png` | `b72f4f3a49454a35e8cad72f84444fbc7bf2c5d29017585cb151282b6dd304e4` |
| parasitic_zombies | small decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/parasitic_zombies/counters/decoded/small_parasitic_zombies_icon_roundtrip.png` | `0be2d8eba25fa6050933587588ceea82fe6c076d973a8d7a8baf16a50f2791a6` |
| mutant_zombies | source large frame 0 | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/source/imagegen_large_frame0.png` | `9bcd174ae7b1fb11062381ba5e2454273fe1840e72494d89951a59cd9be0ce61` |
| mutant_zombies | source large frame 1 | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/source/imagegen_large_frame1.png` | `7acb8755544f6f7d402c0ddfc3199ccd8f5590baf3514e206b29aa3a72b2ef72` |
| mutant_zombies | source small frame 0 | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/source/imagegen_small_frame0.png` | `1d9bb9cd998002ddb94ba8276b08d1e8aaa96919d00e92e084d60eb047f83171` |
| mutant_zombies | source small frame 1 | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/source/imagegen_small_frame1.png` | `6c1e861ddbb2fb1b42d7f810fc9bf8ff8bf60fd9548f10a3a3a468973576d7d8` |
| mutant_zombies | processed large sheet | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/processed/large_unit_mutant_zombies_icon.png` | `8a9569526fc18f4c3933a2c131a15010e8e0ffb06bd81040a1d9ec59517e93c4` |
| mutant_zombies | processed small sheet | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/processed/small_onmap_unit_mutant_zombies_icon.png` | `336d9bf6f2ceb58327c2cc9acdfc4fb474d933da90540324c260c143396c28e4` |
| mutant_zombies | evidence large DDS | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/large/unit_mutant_zombies_icon.dds` | `556371d5321dd354b2d66edbe3e58ee92cbde85539cb0ff30975e1b40b9b464b` |
| mutant_zombies | evidence small DDS | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/small/onmap_unit_mutant_zombies_icon.dds` | `b1fbb0a53d544c99b1eeb7700499cd614068a99dff4224f17b8e1e1b992c54de` |
| mutant_zombies | large decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/decoded/large_mutant_zombies_icon_roundtrip.png` | `8a9569526fc18f4c3933a2c131a15010e8e0ffb06bd81040a1d9ec59517e93c4` |
| mutant_zombies | small decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/mutant_zombies/counters/decoded/small_mutant_zombies_icon_roundtrip.png` | `336d9bf6f2ceb58327c2cc9acdfc4fb474d933da90540324c260c143396c28e4` |
| necrotic_zombies | source large frame 0 | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/source/imagegen_large_frame0.png` | `3b7ae85867576d9f0c8e85eaddd44bbb3cf8c102ea48b9095024892cbe6a91bc` |
| necrotic_zombies | source large frame 1 | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/source/imagegen_large_frame1.png` | `35c1c269f6821cbf549b113f802f2ba81130d6638f1d4db8e04e57b9c69a9696` |
| necrotic_zombies | source small frame 0 | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/source/imagegen_small_frame0.png` | `19a64ca276ee74ccce5a33addb480382f3f590ebf45a219a012fa960546f48d8` |
| necrotic_zombies | source small frame 1 | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/source/imagegen_small_frame1.png` | `cca9651a9b14b3cca0c52ef6718e4bd4df8b5414c499d3845b15fbc899eb6c98` |
| necrotic_zombies | processed large sheet | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/processed/large_unit_necrotic_zombies_icon.png` | `2a62c7495a7339ff146b2a3a653e8898671c7ddcf33c1e711cb2144da7081c21` |
| necrotic_zombies | processed small sheet | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/processed/small_onmap_unit_necrotic_zombies_icon.png` | `9f9a53295f608aea9a447648ade7b8801d7d7f4d3ae887d7661e0e99abd3db18` |
| necrotic_zombies | evidence large DDS | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/large/unit_necrotic_zombies_icon.dds` | `3e8a06e6eb8355e6e2732afa5670730f936cffd79465201b86a6a5bef5077756` |
| necrotic_zombies | evidence small DDS | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/small/onmap_unit_necrotic_zombies_icon.dds` | `da3f0313b5be2dd44230e30df294908c3704832fcc71d0b4bea5debb6e315ca5` |
| necrotic_zombies | large decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/decoded/large_necrotic_zombies_icon_roundtrip.png` | `2a62c7495a7339ff146b2a3a653e8898671c7ddcf33c1e711cb2144da7081c21` |
| necrotic_zombies | small decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/necrotic_zombies/counters/decoded/small_necrotic_zombies_icon_roundtrip.png` | `9f9a53295f608aea9a447648ade7b8801d7d7f4d3ae887d7661e0e99abd3db18` |
| demonic_zombies | source large frame 0 | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/source/imagegen_large_frame0.png` | `39c67e646fe227621bc74d22d1f783e4b91a4c0a2bf40472079872f21c6ad340` |
| demonic_zombies | source large frame 1 | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/source/imagegen_large_frame1.png` | `257656174e9d3c8631f2f3f7ee7986e51ae46a7c4b664fb19b74861ce70ef63d` |
| demonic_zombies | source small frame 0 | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/source/imagegen_small_frame0.png` | `0b50374231850c3a7ba8f0d9ee83f1b97526c9f57d08758d59c4b14b7a8749fc` |
| demonic_zombies | source small frame 1 | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/source/imagegen_small_frame1.png` | `83a481225167adf4f7ad015cd3f9a94f7abf602453df3f47651a947180547adb` |
| demonic_zombies | processed large sheet | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/processed/large_unit_demonic_zombies_icon.png` | `06618f6fb5bb94bc54211abcf7a5e29d24b96fb4d332097247c0f2381348fa19` |
| demonic_zombies | processed small sheet | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/processed/small_onmap_unit_demonic_zombies_icon.png` | `49e8eba21e4682a3be3f7f6423eaf5c65c6c9dfa2bcba2c2acb585475c9d135a` |
| demonic_zombies | evidence large DDS | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/large/unit_demonic_zombies_icon.dds` | `fcccd9a15b7ef4286c0aae3b0cd1a90aba1d543c4060e0147bf34575937dda08` |
| demonic_zombies | evidence small DDS | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/small/onmap_unit_demonic_zombies_icon.dds` | `b853bb6056240cfa453e74db41174e42008a24dfd89bc19bef02f0cc367cf1bf` |
| demonic_zombies | large decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/decoded/large_demonic_zombies_icon_roundtrip.png` | `06618f6fb5bb94bc54211abcf7a5e29d24b96fb4d332097247c0f2381348fa19` |
| demonic_zombies | small decoded round-trip | `docs/assets/002_zombie_outbreak/models_3d/demonic_zombies/counters/decoded/small_demonic_zombies_icon_roundtrip.png` | `49e8eba21e4682a3be3f7f6423eaf5c65c6c9dfa2bcba2c2acb585475c9d135a` |

Each package also contains `manifest.md`, `prompts/generation_prompts.md`, `source/native_imagegen_origins.md`, `candidate_lineage.json`, `validation.json`, `previews/contact_sheet.png`, `previews/alpha_contrast_review.png`, and `sha256sums_artifacts.txt`.

## Existing runtime discrepancy

These are the current preserved runtime hashes, compared with the newly produced evidence hashes above.

| Unit | Runtime path | Current runtime SHA256 | Evidence SHA256 | Match |
| --- | --- | --- | --- | --- |
| parasitic_zombies | `gfx/interface/counters/divisions_large/unit_parasitic_zombies_icon.dds` | `d41ebb36df5d11c43a853646e111a2f38215c9845695e9b5b65c5a78738e35a1` | `c5f830fd94f874e31343071e3d3b905f06939e0e2fdd86664fe4a5829c52f07c` | no |
| parasitic_zombies | `gfx/interface/counters/divisions_small/onmap_unit_parasitic_zombies_icon.dds` | `ee0973f34cedca5593f4bfd4d84efecfab80731ef7c0e6e470c55effce79abe9` | `89d233328a5b83292b29be513b2524825f83d0548c571e6eb26b908ba7978937` | no |
| mutant_zombies | `gfx/interface/counters/divisions_large/unit_mutant_zombies_icon.dds` | `41a03a4fcff3fe7409dbb68e5dde7a56747f06ce1c39152792abdb56569a597a` | `556371d5321dd354b2d66edbe3e58ee92cbde85539cb0ff30975e1b40b9b464b` | no |
| mutant_zombies | `gfx/interface/counters/divisions_small/onmap_unit_mutant_zombies_icon.dds` | `4f3f3d2080a6a66390eae72004645494c17bb142bf67a04ca7e4c2af7271b08a` | `b1fbb0a53d544c99b1eeb7700499cd614068a99dff4224f17b8e1e1b992c54de` | no |
| necrotic_zombies | `gfx/interface/counters/divisions_large/unit_necrotic_zombies_icon.dds` | `f6497cb84905cc10a70c82590d8e952e5a1b2e4d07f5c6805ef35ffc07843b01` | `3e8a06e6eb8355e6e2732afa5670730f936cffd79465201b86a6a5bef5077756` | no |
| necrotic_zombies | `gfx/interface/counters/divisions_small/onmap_unit_necrotic_zombies_icon.dds` | `48a931b536feac9c315ace0c9b057268bf65cb81648de3e176cf7a21341262a3` | `da3f0313b5be2dd44230e30df294908c3704832fcc71d0b4bea5debb6e315ca5` | no |
| demonic_zombies | `gfx/interface/counters/divisions_large/unit_demonic_zombies_icon.dds` | `dd657c7eba183cffc7346896b95378ffb965397dd033c57646ccb0fc75274e9f` | `fcccd9a15b7ef4286c0aae3b0cd1a90aba1d543c4060e0147bf34575937dda08` | no |
| demonic_zombies | `gfx/interface/counters/divisions_small/onmap_unit_demonic_zombies_icon.dds` | `a6f63d46e73ba827cb378b98391ebac7c7042f5af23ceab80ec5b4aeeebfa92e` | `b853bb6056240cfa453e74db41174e42008a24dfd89bc19bef02f0cc367cf1bf` | no |

## Review evidence and limits

The four `previews/contact_sheet.png` files show native-size sheets enlarged for review beside decoded DDS round-trips, and the `previews/alpha_contrast_review.png` files show dark/light backing checks.

The four `previews/rejected_palette_overflow_*` sets retain the earlier processor outputs as rejected comparison evidence after an int16 reference-luminance overflow was found and corrected.

The `validation.json` files confirm exact dimensions, two-frame order, sampled palette-subset checks, source alpha evidence, corrected value distribution, DDS header structure, and pixel-equal DDS decoding.

The packages are ready for parent visual review and promotion review; no in-game acceptance claim is made.

The only deliberate simplification is that native ImageGen source detail is reduced to the exact vanilla counter footprints and sampled palettes required by the consumer; the source PNGs and processing evidence remain available for review.
