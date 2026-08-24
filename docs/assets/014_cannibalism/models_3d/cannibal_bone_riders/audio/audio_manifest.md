# Bone Riders sourced audio manifest

Status: partial. Five licensed source recordings and five 44.1 kHz game-ready candidates exist; the required stone-impact role remains blocked because the bounded search did not identify a semantically defensible licensed recording.

| Role | Source | Creator | Terms | Original SHA-256 | Derived SHA-256 |
|---|---|---|---|---|---|
| selection / idle horse | [Wiehern.ogg](https://commons.wikimedia.org/wiki/File:Wiehern.ogg) | Hü | Public domain dedication | `EC30F1A269D0FADBDDF1C8E170200AC7BE8A493967518A7984D147120A620226` | `52736FE0F5FA830C9089564F325FED9E75D0078115D331F275FF4827697D37A6` |
| hoof movement | [WWS Clatter of Horseshoes on the Pavement](https://commons.wikimedia.org/wiki/File:WWS_Clatterofhorseshoesonthepavement.ogg) | Monika Widzicka / Work With Sounds | CC BY 4.0; attribution and change notice required | `5C0E7B589F2C3CDCF4613702C628501DDFB4A4A31A8582A79CC7EB92D64EEB85` | `DF8B3676564FE1175443F79B951E597A6FB6D5F69620AB7A953F0A9863B8CAC3` |
| sling release | [Whip-sound.ogg](https://commons.wikimedia.org/wiki/File:Whip-sound.ogg) | Mike Koenig | CC BY 3.0; attribution and change notice required | `2D2DF16B3EC41B9B73E023A0DEA67A44916B676779983F583E0BC1E704CBBFBA` | `1C68F1164960CBF0D28673C3BA584366F3729E1E4C49C6B2D393D4099A66C3DC` |
| training / rider acknowledgement | [Human whistling.ogg](https://commons.wikimedia.org/wiki/File:Human_whistling.ogg) | TwoWings | Public domain dedication | `49D16E64A667FD7B87B70BD21183C98C7A747F6F4F1933D8DF3EBC61445E1647` | `8E2E41C2A6F05FAB876FEE1C6EA2CA7F928AEE179221AEC60DE6AB204A1995AB` |
| rider death | [Wilhelm Scream.ogg](https://commons.wikimedia.org/wiki/File:Wilhelm_Scream.ogg) | Sheb Wooley recording, Commons CC0 edition | CC0 1.0 | `360097C9715F55ABCC26AB73F12F69B730C660FBF019FC63CAA685BFA9B6585B` | `E8DD92650CDF99386AD59EAEEA0067F05B6CF88A9BB7FEF538CC583C705BE54E` |

All sources were retrieved on 2026-08-24 from the named Commons description page and its original-file link. Originals are immutable under `audio/sources/original/`. The only transformation was FFmpeg decode/channel conversion/resampling to PCM S16LE, 44100 Hz, mono under `audio/derived/`; `ffprobe` confirms those exact properties for all five WAV files.

Proposed identifiers are `cannibal_bone_riders_select`, `cannibal_bone_riders_move`, `cannibal_bone_riders_idle`, `cannibal_bone_riders_sling_release`, `cannibal_bone_riders_training`, and `cannibal_bone_riders_death`. Synchronization remains blocked with the absent skeletal actions. The sling release belongs at the attack discharge frame, hoof movement follows move/retreat hoof-contact phases, training whistle belongs at the rider cue, and death belongs at initial rider impact/collapse. No sound definitions were wired.
