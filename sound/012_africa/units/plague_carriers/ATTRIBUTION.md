# Plague Carriers sound attribution

Every installed file is an edited arrangement of recordings that were already archived in this repository with a recorded licence (cut, fade, pitch-shift, EQ, level, layering, mono, 44.1 kHz, PCM16 conversion). No tone, noise bed, synthesized, generated or newly recorded audio is present. No recording was downloaded for this rework.
Licence statements are inherited from the archived source records; derivative licensing was not independently reassessed. CC BY 4.0 material needs the credit line given in the table; CC0 and public-domain items are credited voluntarily.

## Source recordings

| Key | Recording | Creator | Licence | URL | Archived original (repo-relative) | Source SHA-256 | Note |
|---|---|---|---|---|---|---|---|
| plague_death_pre | Installed plague death derivative (inherited from Cough 1 / Air duster, package-level record) | ezwa and stephan (PDSounds) | Public domain dedication (package record; per-file mapping not proven) | https://commons.wikimedia.org/wiki/File:Cough_1.ogg | `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/src/installed_preimage/plague_carriers/chaosx_plague_carriers_death.wav` | `0ff9c42a208e9cd4f536e935c2d9b4268fe6d2811f22bd85bd76388b85df65f4` | originals absent; installed derivative is the archived input |
| plague_idle_pre | Installed plague idle derivative (inherited from Cough 1 / Air duster, package-level record) | ezwa and stephan (PDSounds) | Public domain dedication (package record; per-file mapping not proven) | https://commons.wikimedia.org/wiki/File:Cough_1.ogg | `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/src/installed_preimage/plague_carriers/chaosx_plague_carriers_idle.wav` | `2da96b2e1e550ba11f68a48f3b81277ce99c03201092de513bcbf85773cf6a76` | originals absent; installed derivative is the archived input |

## Installed files (11 Oct 2026 rework)

| Runtime file | Soundeffect | Role | Composition from the recordings above | Composite SHA-256 | Before SHA-256 | Installed SHA-256 | Length s | Peak dBFS | RMS dBFS | LUFS | TP dBTP | Loudest 5 ms window s | Head trimmed by master s | Designed contact in file s |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `chaosx_plague_carriers_idle.wav` | chaosx_plague_carriers_idle_sfx | shot | plague_idle_pre 0.410-0.770 s, placed at 0.000 s | `0896211cb52e211244cc15fb0040e4c3d6e828ad5b56ebb4befaa715b7e1fcae` | `new file` | `6b0ee2fb8ef22ccdbe917337ae53615b44899e477f2232f45fe673e01e35cdbc` | 0.36 | -3.0 | -21.03 | -70.0 | -3.0 | 0.06 | 0.0 | - |
| `chaosx_plague_carriers_idle_02.wav` | chaosx_plague_carriers_idle_sfx | shot | plague_idle_pre 0.410-0.770 s, placed at 0.000 s, pitch -2 st (rubberband) | `da98508567e5d93564fc1b55f806206412138dda535309d915c42db95873ff57` | `new file` | `be0dda5531ca893098c6a702a38fcf6bd4fe5409685db4c485d1f649cb691986` | 0.36 | -3.0 | -21.71 | -70.0 | -2.9 | 0.07 | 0.0 | - |
| `chaosx_plague_carriers_idle_03.wav` | chaosx_plague_carriers_idle_sfx | shot | plague_idle_pre 0.410-0.770 s, placed at 0.000 s, pitch +2 st (rubberband) | `354bf69284204dd351d8bb041b93de160a3cc75352f9f2fb8148e6ac811d950d` | `new file` | `c79f36f344247ee6b15c44eb4f4f6af45d74f327a84e2cc260484beeae84a7ab` | 0.36 | -3.0 | -21.65 | -70.0 | -2.9 | 0.055 | 0.0 | - |
| `chaosx_plague_carriers_death.wav` | chaosx_plague_carriers_death_sfx | shot | plague_death_pre 0.000-1.120 s, placed at 0.000 s | `e446c439826ec9096fa7450acc135d48af802b4b75be30a5b97ca11aaec2a544` | `new file` | `281733bcc6ed29f07c9e5a4b3ca41c14fa71f40d4c56be43982dd769fe0956cc` | 1.12 | -3.0 | -21.32 | -21.3 | -2.9 | 0.025 | 0.0 | - |
| `chaosx_plague_carriers_death_02.wav` | chaosx_plague_carriers_death_sfx | shot | plague_death_pre 0.000-1.120 s, placed at 0.000 s, pitch -2 st (rubberband) | `77145948b0a34cb0fb994010fc6617104d2256f0616b6e0d2d2ae644349594a4` | `new file` | `03dd401df3820f610ef5a7a507311f6b93d944240d5bb4f1eb8c5da300addacb` | 1.12 | -3.0 | -21.29 | -21.2 | -2.9 | 0.025 | 0.0 | - |
| `chaosx_plague_carriers_death_03.wav` | chaosx_plague_carriers_death_sfx | shot | plague_death_pre 0.000-1.120 s, placed at 0.000 s, pitch +1.5 st (rubberband) | `e0db4133ab3a35d8576d1e51e389d712980f5cdb857e3e49927bc6efaff7c4b7` | `new file` | `14795a95e164e012aae64cd52e4e149462a2aea9e3cfa2f5e95b978afb5584a2` | 1.12 | -3.0 | -21.56 | -21.2 | -3.0 | 0.02 | 0.0 | - |

Every installed file above is pcm_s16le, 44.1 kHz, mono, produced by `.tools/3d_pipeline/audio/master.py batch` (30 Hz high-pass, 8 ms fade-in, 50 ms fade-out, role peak/RMS/loudness gates, source clipping gate, lead silence at most 20 ms). Mastering evidence per file: `docs/assets/012_africa/models_3d/_wp1_audio_rework_20261011/reports/plague_carriers_all_report.json` and `cuts/*.recipe.json` (ignored working area).

## BLOCKED cues (missing recording)

- `bray` at frame 12: needs a CC0/CC BY donkey bray recording, 0.4-1 s, 2-3 takes (Freesound or Wikimedia Commons); no donkey vocal is archived, so no bray was installed and no soundeffect was created.
- `idle`/`death` donkey vocal: the installed takes are tail-trimmed and pitch-varied (-2/0/+2 and -2/0/+1.5 semitones) versions of the existing cough-derived derivatives; a donkey-appropriate idle and death vocal remains missing.

## Files not changed in this rework

- `chaosx_plague_carriers_select.wav`, `_deploy`, `_impact`, `_release_containment`: unchanged inherited derivatives (Cough 1 and Air duster public domain, Metal Clanging Noises CC BY-SA 4.0 for the impact).
- `chaosx_plague_carriers_move.wav`, `_02`, `_03`, `_04`: installed earlier by the parent from the archived horse-hoof recordings; source chain in `docs/plans/unit_fix_2026-10/wp1_sound_attribution.md`.

## Earlier notice (still applies to the unchanged files named above)


The impact candidate derives from Camshaft64, Metal Clanging Noises, https://commons.wikimedia.org/wiki/File:Metal_Clanging_Noises.ogg , licensed CC BY-SA4.0, https://creativecommons.org/licenses/by-sa/4.0/ .
The inherited derivative was trimmed, faded and normalized as documented in the historical audio manifest.
The current modification is only float32-to-signed16 PCM conversion at unity gain with no dithering or filtering.
Retain attribution, this change notice and the CC BY-SA4.0 terms with the impact derivative.
Cough1 by ezwa/PDSounds and Air duster by stephan/PDSounds are public-domain recordings according to the preserved source-page evidence.
Their pages are https://commons.wikimedia.org/wiki/File:Cough_1.ogg and https://commons.wikimedia.org/wiki/File:Air_duster.ogg .
The named originalOGGfiles are absent; this package preserves and converts the existing sourced derivatives.

These synchronized siblings additionally apply the exact source-interval trims and5ms entry/40ms exit fades in copy_manifest.json; the impact derivative remains CC BY-SA4.0.
