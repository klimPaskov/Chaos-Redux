# WP2 audio needs: cues that still require a new recording or a recovered archive

Status after the WP2 cannibal batch (`.tools/3d_pipeline/audio/cannibal_batch.py`, spec and report under `docs/plans/unit_fix_2026-10/wp2_evidence/audio/`): 71 derived cues were installed from licensed recordings already archived in the repository; no Internet download was performed in this session. The items below are the only cues that could not be served from in-repo recordings under the shared mastering gates.

## 1. Second weapon-impact takes for the five spear or polearm units (recording needed)

Units: cannibal_scavenger_warband, cannibal_feast_guard, cannibal_feast_cohort, cannibal_island_reavers, cannibal_bone_guard.
The only in-repo spear-contact recordings (Still North Media, CC0, `docs/assets/012_africa/models_3d/riverborn/audio/finalize_20260912/extracted/Spear Spear *.wav`) are sharp clicks with a 23 to 29 dB crest factor; after peak normalization their RMS sits 6 to 10 dB under the shared one-shot band (-18 dBFS +/- 4), so `master.py` refuses them (`shot_rms_minus18_plusminus4`). The siege_eaters haft-on-haft hit 0 passed and is installed as `cannibal_siege_eaters_weapon_impact_02.wav`.
Need: one CC0 / CC BY recorded blunt spear or polearm body impact per unit (0.25 to 0.5 s, with a short thud tail so the RMS lands near -18 dBFS), for example a Freesound or OpenGameArt wooden-shaft body hit. Until then each impact soundeffect keeps its single rubberduck take.

## 2. HaelDB `Male Grunt/Yelling Sounds` original pack (archive recovery needed)

The CC0 pack behind every selection and idle vocal is no longer archived in the repository (`provenance_review.json` records `archival_gap` for all 14 derived files, and the `originals_selected/` folders of the three WP2 jobs are gone). WP2 re-trimmed the existing runtime derivatives to their voiced parts, which keeps them licensed but prevents choosing fresh distinct takes. Need: re-download https://opengameart.org/sites/default/files/yelling%20sounds.zip (CC0 option on https://opengameart.org/content/male-gruntyelling-sounds) into a job evidence root so each unit can receive a unique selection and idle take and the country voices can drop the four takes they currently share with unit selection cues (`cannibal_voice_06..09.wav` reuse the feast_guard, island_reavers, siege_eaters and march selection recordings; declared family pool).

## 3. stilgar `Male pain grunts` (no longer needed)

The seven death cues now use distinct takes from thebardofblasphemy's CC0 `Grunts of male death and pain` (archived at `docs/assets/039_murder_mystery/audio/source/death_pain_grunts.wav`) plus a second Exewin CC0 take each, so the clipped stilgar excerpts and the missing stilgar archive are retired rather than needed.

## 4. Not a recording need: gate note

The plan asked for footsteps at about -18 dB peak and swishes at -4 / -6 dBFS; the shared section 3.5 gate that every installed WAV must pass enforces -6 dBFS for steps and -3 dBFS for one-shots, so the files are mastered to the gate and the relative level is left to the soundeffect `volume` values (0.68 movement, 0.86 attack) already in `014_cannibalism_units_sound.asset`.
