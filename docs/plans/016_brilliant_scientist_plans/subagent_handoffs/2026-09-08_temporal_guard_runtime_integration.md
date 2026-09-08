# Temporal Guard mesh and animation integration

Status: implemented for the requested skeletal repair and sourced action-audio integration; auditory acceptance and historical provenance remain unresolved.
Acceptance basis: the user authorized repair of existing faulty unit rigs/actions in Blender, and the parent reviewed the three final role sheets and accepted the repaired surface and articulated collapse, impact and settling phases.

The runtime consumer `temporal_guard_entity` clones `chaosx_temporal_guard_entity` for the existing `sprite = temporal_guard` sub-unit.
The calibrated entity scale is 0.8, applied once.
The mesh contains 29,966 triangles and the original 24-bone exported rest skeleton, with two `char1.002` streams at indices 0 and 1.
Both streams use the same verified diffuse, packed normal and gloss/specular maps through `PdxMeshAdvanced`.

All ten roles have actual-byte Blender reimport evidence: idle, move, attack, defend, entrain, death, temporal_anchor, synchronization, support_attack and retreat.
The nine living actions loop; death is non-looping with no successor state.
The selected ten animation binaries are unchanged from the accepted action candidates.
The repaired editable checkpoint preserves all ten roles with measured grounding-basis equivalence; native key identity is not claimed.

Runtime definitions are `gfx/entities/temporal_guard.gfx`, `gfx/entities/temporal_guard.asset`, and `gfx/models/units/temporal_guard/animation_temporal_guard.asset`.
Source evidence is under `docs/assets/chaos_redux_3d_model_pilots/models_3d/temporal_guard/evidence/20260906_repair/`: `final_repair_manifest.json`, `action_crosswalk_final.json`, `rest_bind_export_equality.json`, `editable_action_replay_equivalence.json` and `runtime_copy_manifest.json`.
The parent independently compared all 14 source/runtime payload hashes and reviewed `final_role_review_1.png`, `final_role_review_2.png` and `final_role_review_3.png`.
The worker recorded 150 previews across five sampled frames and three views per role; this is sampled export/reimport evidence, not continuous game playback.

## Payload verification

| Runtime file | Bytes | SHA-256 |
| --- | ---: | --- |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard.mesh` | 7554535 | `BF13AA313FDB3D7869665810ACDFE64A77C555EEFC802D947FF332986BB39848` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_diff.dds` | 4194432 | `82071750202D2435542841E8354313DDB4B46BFD4B23CEBA0308CE4DE6DB4044` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_normal.dds` | 4194432 | `77A342BF40D9C65A36F74829EFA94A174C634AD5341C72E16A85CF0360EB805A` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_spec.dds` | 4194432 | `A482D6BACACE80C23EA97E36849B2F79118EC59D5A2501F4057905835F1B64AE` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_idle.anim` | 76627 | `C2BE045CF4079A647E012EFF8145B07CFE69CF3018E9F616FC898E90EF603563` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_move.anim` | 26707 | `E3839142F49EA48A5182DB4145CAF04A462EAFEE9ABB8F39B42FF53DE947DAE4` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_attack.anim` | 48211 | `F22DF39A34FADEF4ECA718102E966EA7AC704E3B3D89244D715D619CE406B3DF` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_defend.anim` | 66643 | `F468CB8B13041D18FC8D894557F82E70E3E31B79E0D15B2C53EBABC582655128` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_entrain.anim` | 32851 | `E130DDEF7FD1650C6D62E44F496F44CAF89784BF3575AA402306AD55AD6D7FEE` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_death.anim` | 42835 | `409714D9C162A0A2C072781327BBA73869021BC5CAA115A732EBFDCFE4494133` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_temporal_anchor.anim` | 52051 | `CF35348B9AE481D606240EFCA2722ACBB5CDACB4F5A858FBACAC4A37F28A715A` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_synchronization.anim` | 82003 | `1DE85573412CE3A4A121AC6D4B6A5178EC308B3B37FD1FF1F4047E61B331624B` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_support_attack.anim` | 25035 | `4733FB4DAE6C335AE9063BDC81EB9D891C62A688D975C8FB45A664D0690528A4` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_retreat.anim` | 38781 | `8D62D4BD2D8C9DE3C8AF50F58348166D77643B6D713661FDF5DADAD4668BD017` |

## Simplifications, omissions, and blockers

No unapproved simplification was used for the mesh/action repair.
The localized surface repair and equivalent editable grounding representation were accepted after preservation and visual review.
Historical source-art authorization/refinement receipts and complete remesh/credit lineage remain unresolved.
Nine source-derived PCM16 cues are installed through sound/temporal_guard.asset and sound/chaosx/temporal_guard/; the rejected square-wave candidate is not selected.
The physical clock recording and accepted same-boots movement/retreat reuse have documented source hashes, attribution, measured onsets and ten entity event times.
The idle clock is a bounded four-second sample per idle cycle, with loop=no; other cues are short action accents.
Selection, acknowledgement and received-hit sounds are registered without inventing unsupported consumers.
Auditory suitability remains unverified; timing, format, licensing and share-alike notices have mechanical/source evidence.
Per-subunit selection/acknowledgement consumers remain unsupported in mixed-tag armies.
The existing bespoke counters remain installed and unchanged.
No provider calls or credits were consumed by this repair tranche.

Independent read-only audit by pilot_integration_audit passed: 14 payload pairs, ten role chains, both material streams, sprite alias, single scale application and terminal death all matched the evidence with zero mismatches.


## Sourced audio payloads

Source recipes, licensing and ten onset-adjusted event times are in docs/assets/chaos_redux_3d_model_pilots/models_3d/temporal_guard/audio/final/20260908/audio_manifest.json.

| Runtime file | Seconds | SHA-256 |
| --- | ---: | --- |
| `sound/chaosx/temporal_guard/chaosx_temporal_guard_selection.wav` | 0.510000 | `F8604DC3D0B56BE1DB723FC4C5148A663DF2CA5A7666CB19F9469E8AEFEB0612` |
| `sound/chaosx/temporal_guard/chaosx_temporal_guard_acknowledgement.wav` | 0.510000 | `1EBFD7112D2BD1F481D0783B1940C16A93333208B9EA99330D52F5CB9AB9E825` |
| `sound/chaosx/temporal_guard/chaosx_temporal_guard_idle_clock.wav` | 4.000000 | `1F3556E8EC22205E0FCAF75E2261DCBACDAB2DA685A19608C29C158D28C4E30C` |
| `sound/chaosx/temporal_guard/chaosx_temporal_guard_footstep_a.wav` | 0.279002 | `C5449DA0DA2F2C7BEA6586EE28ED260A0DD243E6608E679B0B261C765961C67B` |
| `sound/chaosx/temporal_guard/chaosx_temporal_guard_footstep_b.wav` | 0.290998 | `04442F0E9F6FE3E5B7BA937B2E3913FC000F928700ECB4C111BDF7B2FD562086` |
| `sound/chaosx/temporal_guard/chaosx_temporal_guard_attack_contact.wav` | 0.430000 | `64BDD3434ABFD872FC2DE77CFE93F5D56E62F785437D076A81230B6E6059B79E` |
| `sound/chaosx/temporal_guard/chaosx_temporal_guard_impact.wav` | 0.761701 | `CC75ECAF27B1BD0CEA0635FB105A193B1772236952A41483E4978947304753B6` |
| `sound/chaosx/temporal_guard/chaosx_temporal_guard_temporal_special.wav` | 0.650000 | `2AEAA8A8AE4CD10123D4C2DA64BE2038610EF8A89CEF0B9CAE6B002E14736354` |
| `sound/chaosx/temporal_guard/chaosx_temporal_guard_death.wav` | 0.700000 | `D95600E6A2674E065856A282DD021BCE076E339F12182F05C477F4A67AE5C547` |

## Independent audio integration audit

The independent read-only audio audit passed all nine source-to-runtime WAV pairs by SHA-256 and byte count.
Every selected file is mono 44.1 kHz signed PCM16, and the manifest records zero clipped samples for all nine cues.
All five deduplicated original-source hashes also match the preserved originals: physical clock, boots, metal clanging, metal drop, and physical electrical buzzing.

`sound/temporal_guard.asset` defines nine sample ids and nine non-looping soundeffects under the Effects category, with one selected sample per effect.
The installed `ATTRIBUTION.md` covers the public-domain clock and electrical recordings, the CC BY-SA 4.0 boot and metal-clanging adaptations, and the CC BY-SA 3.0 metal-drop adaptation, including source pages and direct ShareAlike license links.
No auditory suitability review is claimed; the verification is limited to hashes, formats, waveform receipts, attribution coverage, and source/action timing.

All ten runtime event rows match `audio_manifest.json` exactly.
Their target frames fall within the corresponding unchanged 24 FPS actions in `evidence/20260906_repair/action_crosswalk_final.json`, and each target contact time follows `(target_frame - 1) / 24` before the manifest's measured-onset compensation.
The verified rows are idle frame 1 at 0.000000; move frames 1 and 16 at 0.000000 and 0.617018; retreat frames 1 and 25 at 0.000000 and 0.992018; attack frame 30 at 1.206338; support_attack frame 26 at 1.038673; temporal_anchor frame 44 at 1.788673; synchronization frame 52 at 2.122007; and death frame 36 at 1.456338.

The current diff of `gfx/entities/temporal_guard.asset` adds only these ten event rows.
It does not change any state name, animation role, looping policy, transition, blend time, speed, scale, entity alias, or stance mapping.
Selection and acknowledgement are registered for possible future isolated consumers but remain unbound, and the registered impact effect remains unused because no verified received-hit callback exists.
No selection, acknowledgement, received-hit, defend, or entrain consumer was invented during integration.

The audio manifest's source-only readiness label is preserved as worker handoff history; current source/runtime hashes and entity definitions establish that parent integration has since occurred.
Live-game and listening validation remain outside this audit, and the broader package limitations recorded above remain open.
