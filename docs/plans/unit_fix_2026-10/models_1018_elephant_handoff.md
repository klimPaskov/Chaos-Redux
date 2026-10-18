# Elephant model repair handoff

Status: implementation in progress; the missing-model defect is not yet repaired in runtime bytes.
Authorization: the user's `models_1018_elephant` brief dated 18 October 2026 requests a complete custom elephant replacement and explicitly prohibits commits.

## Root cause and scope

`common/units/012_africa_elephant_forces.txt` binds `chaosx_elephant` to `sprite = elephantry`.
The installed `common/units/cavalry.txt:158–179` defines that inactive subunit, but the installed entity definitions provide no `elephantry_entity`.
The `elephantry_idle` and `elephantry_move` entries in `gfx/entities/infantry.gfx:107–108,142–143` are infantry-mesh animation registrations, not an elephant entity or elephant geometry.
The user observed the engine's missing-model cube.

The required replacement is an African elephant with tusks, trunk, tail, reinforced woven-wood howdah/harness and one period rider.
The body, howdah/harness, and rider require separate source-informed Meshy 7 geometry tasks, followed by dedicated live Blender quadruped authoring and eight distinct actions.
The intended runtime path is `gfx/models/units/012_africa_elephant/`, with `chaosx_elephant_entity` consuming `chaosx_elephant_mesh` and the subunit selecting `sprite = chaosx_elephant`.
No runtime candidate or unit binding has been installed by this relaunch yet.

## Work and evidence

The 3D specialist owns source preparation, provider tasks, live Blender work on port 9886, material processing, export/reimport, counter evidence, action-phase markers, and the package `runtime/handoff.md`.
The parent owns audio recovery/preparation, final runtime copies, entity/material/action/sound registrations, the unit sprite change, documentation, and review.
The approved source SHA-256 is `78A04549F24C4C1E5E510BEEAD8932D89F402CC8E0B64A17DCCD7E8CBF9AA702`.
Earlier stopped-attempt files under `.tmp/models_1018/elephant/` and the job's `evidence/models_1018/` are unreviewed historical evidence until independently checked.

Current documentation has been corrected to distinguish the missing vanilla entity from the authorized custom production requirement.
The current Event 012 elephant doc, Gods visual boundary, elephant visual disposition, and test-country visual note point here for acceptance status.
Historical handoffs remain unchanged.

Integration baselines and source citations, including SHA-256 revisions, are retained at `.tmp/models_1018/elephant/integration/preflight.json`.
The connected tool inventory does not expose `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, or `hoi4.source_lookup`; direct local references were used.
Relevant offline sections read: `Unit modding - Hearts of Iron 4 Wiki.md:132–171` and `Entity modding - Hearts of Iron 4 Wiki.md:25–183`.
No detailed entity/animation/material schema chapter was found in installed documentation markdown; installed cavalry entities and the Event 012 forest-giant and gorilla registrations provide the concrete precedents.
`pipeline_report.md` and `wp1_africa_report.md` cover the existing model cohort and seven Africa strange forces; they do not establish elephant model acceptance.

## Reference, scale, and counter review

Parent review accepted the recovered item-free elephant and howdah derivatives after inspecting the approved original, each full-size candidate, and `evidence/models_1018/production/prepared_mattes.png`.
Saturated RGB in fully transparent pixels did not appear on the light/dark matte composites.
The separately generated full-body empty-handed rider preserves the ochre headwrap, brick-red tunic, leather/textile construction and period identity.
The source rider's short curved wooden goad is accepted as a separately generated controlled item for the support-attack performance.

Fresh Blender measurements reported visible western infantry height 7.3518247977 source units, or 5.8814598382 at entity scale 0.8.
The horse measures 6.59552288 × 20.33619547 × 15.64604477 source units, or 4.28708987 × 13.21852705 × 10.16992910 at scale 0.65.
The accepted target is elephant body height 15.6460447654 source units at entity scale 0.8, giving 12.5168358123 runtime units, approximately 2.12818 infantry heights.
The assembled height ceiling is 22.05 source units, with footprint at most 8.25 × 22 source units; runtime limits are 17.64 high and 6.6 × 17.6 footprint.
These are calibrated production targets, not measurements of an accepted final elephant.
Only uniform fitting is authorized, followed by actual-byte map-camera review.

The parent decoded both existing elephant counters beside installed vanilla infantry references and reviewed both frames at native and enlarged sizes in `evidence/models_1018/counter_parent_review.png`.
The large 152×42 strip retains its bespoke green elephant/howdah silhouette and alpha; the small 60×12 strip retains the grayscale map silhouette and alpha.
The final DDS hashes match the historical records exactly: large `5D455DC3268BE89451D967E187FD5AAA8D6966C9A82FF8AE933208DF2201A21E`, small `6E2AC8B322F4FE1D6D126E1B02727BE721B83FD4EEC5788D6B9D0AB083188BDD`.
The `GFX_unit_chaosx_elephant_icon_medium` and `_medium_white` aliases at `interface/chaosx_subuniticons.gfx:195–199` already point to those textures.
Reuse is accepted under the user's explicit instruction; no counter pixels or registry entries were changed.
The historical missing source-art/prompt lineage is not reconstructed by this byte and visual check.

## Pending delivery

Provider task IDs and consumed credits, final changed-file hashes, audio source/licence rows, exact rendered action paths, and `evidence/final_reimported_actions.png` must be recorded after production.
No render, animation, material, sound synchronization, or in-game validation is claimed by this interim handoff.
No simplified model or aliased action is accepted.

## Audio sources and staged candidates

The historical audio-original directory was absent at relaunch.
All three recordings were recovered from their Commons original-file URLs on 18 October 2026 and exactly match the historical SHA-256 values.
Their source pages were checked for creator and licence.

| Recording | Author | Licence | Original SHA-256 |
| --- | --- | --- | --- |
| [Dull Thud](https://commons.wikimedia.org/wiki/File:Dull_thud.ogg) | gregoryweir | Public domain | `5B91906D41BD57F1F6551E446D30FBFF06EC59A39D22725140293EF4AEC6CDB3` |
| [Elephant voice - trumpeting](https://commons.wikimedia.org/wiki/File:Elephant_voice_-_trumpeting.ogg) | தகவலுழவன் | CC0 1.0 | `E5F3120E5EACA87CC080BBF57BD185C96D52FD0F63CC1DFE33228C8BFA29F3BC` |
| [Squeaky door](https://commons.wikimedia.org/wiki/File:Squeaky_door.ogg) | leonmire | Public domain | `B60B97C3F73C9754FC36B58CEA4862D50FF800F12632C9B55BC6F8132E93D9C5` |

Original files remain under the job's `evidence/audio/original/`.
Mechanical trim/fade/normalization through `sound_pack.py` produced an initial rejected stage with substantial inherited DC offset.
The selected staged revision was regenerated from the immutable originals with a 30 Hz second-order high-pass before trimming, fading and normalization, under `evidence/audio/repair_2026_10_18_v2/`.
`receipt.json` records original, intermediary, staged, and runtime-preimage identities, exact processing, attribution, and ffprobe results.
`sample_review.json` records zero clipped samples and absolute DC below 0.000028 for every staged cue; `move_inspection.json` passes the shared step checks.
These are staged audio checks, not playback or animation-synchronization acceptance.

| Existing soundeffect identifier | Staged duration | Staged SHA-256 |
| --- | --- | --- |
| `chaosx_elephant_move_contact` | 0.369320 s | `43D52977BB54A9FEB871E13766FF3CF081721C1A0A7C9E2096EAD9DF35AFD2BD` |
| `chaosx_elephant_impact_contact` | 0.369320 s | `0100B084C1392E30EB49461D543E2EF660431E542FA83F2E09F32B07F927D3A3` |
| `chaosx_elephant_idle_call` | 0.715261 s | `839AE59BE7F39D5098649D8F333872063DF9D4ACF370C496AC558AB573F268B4` |
| `chaosx_elephant_attack_call` | 1.301995 s | `49EF9406056629FDD8F0859D0AAD383AF6E949D70E872FAFD93E686BE7542CEB` |
| `chaosx_elephant_death_call` | 1.301995 s | `49EF9406056629FDD8F0859D0AAD383AF6E949D70E872FAFD93E686BE7542CEB` |
| `chaosx_elephant_supply_load_creak` | 2.323197 s | `D53A95B4B41CEDBE6866F6016932A3607CA3E3D7F3FE0BE515EC64C15CD6A2ED` |

Movement and impact deliberately share the thud source at different levels.
Idle, attack and death derive from one trumpet recording; attack and death currently share the same staged bytes and are not claimed as distinct recorded takes.
The source recording was historically identified as an Asian elephant and is retained under the user's explicit recovered-audio instruction.
Per-subunit selection audio remains unverified: the installed country/original-tag voice routing cannot distinguish this elephant from ordinary infantry under the same country.
Entity idle playback is not selection, and country voice definitions have not been changed.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-units-divisions`, and `chaos-redux-subagents`.
