# Temporal Guard mesh and animation integration

Status: implemented for the requested skeletal repair; whole-package audio and historical provenance remain incomplete.
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
Audio integration is incomplete: the primitive square-wave selection/ambient candidate is unsuitable, and distinct retreat audio or sourced-footstep reuse requires role review.
Sourced cue timing, attribution/share-alike and the available selection/acknowledgement consumer must be reviewed before any corresponding audio completion claim.
The existing bespoke counters remain installed and unchanged.
No provider calls or credits were consumed by this repair tranche.

Independent read-only audit by pilot_integration_audit passed: 14 payload pairs, ten role chains, both material streams, sprite alias, single scale application and terminal death all matched the evidence with zero mismatches.

