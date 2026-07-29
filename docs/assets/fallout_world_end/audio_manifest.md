# Fallout World End Audio Manifest

## Selected source

- Track: `Eyes In The Void`
- Composer and recording owner: Scott Buckley
- Official source page: `https://www.scottbuckley.com.au/library/eyes-in-the-void/`
- Official source file: `https://www.scottbuckley.com.au/library/wp-content/uploads/2025/06/EyesInTheVoid.mp3`
- Release date: 12 June 2025
- License: Creative Commons Attribution 4.0 International
- Creator terms: `https://www.scottbuckley.com.au/library/using-this-music/`
- Source file: `docs/assets/fallout_world_end/source_audio/eyes_in_the_void_scott_buckley.mp3`
- Source SHA-256: `285E9AEA3E24698FDA179EBA56D2F6C7D6ECD92F0DDC78932633E0641F769335`

The official source page, creator usage terms, and CC BY 4.0 legal code are preserved under `docs/assets/fallout_world_end/source_audio/evidence/`.

## Required attribution

`'Eyes In The Void' by Scott Buckley - released under CC-BY 4.0. www.scottbuckley.com.au`

Change notice:

`Edited by Chaos Redux: excerpted from 02:22.370 to 04:22.370, faded, attenuated, and converted to 44.1 kHz WAV.`

## Processing record

- Selected range: `02:22.370` through `04:22.370`
- Output duration: exactly 120 seconds
- Fade in: 0.75 seconds
- Fade out: final 1.5 seconds
- Master attenuation: 12 dB
- Filter chain: `atrim=start=142.370:end=262.370,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.75,afade=t=out:st=118.5:d=1.5,volume=-12dB`
- Sound output: `sound/fallout_world_end/fallout_world_end_blackout.wav`
- Sound format: PCM16 WAV, 44.1 kHz, stereo
- Sound SHA-256: `7C6901A5B93C876030FBED7D176A3CB84EBD42A6DC15E568537F91BA3D8AAA39`

## Wiring

- Sound asset file: `sound/fallout_world_end_sound.asset`
- Sound wrappers: `fallout_world_end_blackout_sound_0_5` through `fallout_world_end_blackout_sound_3_0`
- Playback owner: `fallout_play_blackout_audio`

The playback route reads the existing player preference for super-event volume, but it does not use the ordinary super-event visibility flag, audio identifier, sprite, file, or path.

## License constraints

Attribution and the change notice must remain in the distributed project. The track is synchronized to the Fallout blackout presentation. Do not distribute the source or edited cue as a standalone audio product, upload it to music streaming services, or submit it to an audio fingerprinting service.
