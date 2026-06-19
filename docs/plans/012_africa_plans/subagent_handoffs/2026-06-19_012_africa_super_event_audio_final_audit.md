# Event 012 Africa Super-Event Audio Final Audit

Date: `2026-06-19`

Scope: final audit of Event 012 Africa super-event audio/source/license/wiring status after the parent confirmed slots/audio ids `68-80` were already wired.

## Files reviewed

- `docs/specs/012_africa_specs/prompts/012_africa_super_event_prompt.md`
- `docs/assets/012_africa/super_events/audio/manifest.md`
- `docs/super_events/012_africa_super_event_research.md`
- `music/chaosx_super_event_music.asset`
- `music/chaosx_super_event_music.txt`
- `sound/chaosx_sound.asset`
- `music/chaosx_music_track_list.html`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- on-disk `music/super_event_africa_*.ogg`
- on-disk `sound/chaosx_super_event_africa_*.wav`
- on-disk `docs/assets/012_africa/super_events/audio/final/*.ogg`

## Source and license verification

Primary source verification was done against Wikimedia Commons file pages for the selected packaged tracks.

- Verified U.S. federal-government or equivalent public-domain status for:
  - `South African national anthem.oga` via U.S. Navy Band Commons source.
  - `Holst-_mars.ogg` via U.S. Air Force Band Commons source.
  - `Holst_First_Suite_March.ogg` via U.S. Marine Band Commons source.
  - `Sousa's "The Thunderer" - United States Marine Band (2017).ogg` via Commons composition/performance public-domain tags.
  - `Intermezzo from Goyescas - U.S. Marine Band.ogg` via Commons composition/performance public-domain tags.
  - `Charles Gounod - U.S. Marine Band - Grand March from La reine de Saba.ogg` via Commons federal-work and public-domain composition tags.
  - `Siegfrieds_funeral_march_and_finale.ogg` via Commons U.S. Marine Band federal-work tag.
- Verified CC0 Commons status for:
  - `Beethoven_EgmontOvertureOp.84_LudwigVanBeethoven-EgmontOvertureOp.84.ogg`
  - `Funeral_March_Chopin_Op_72_2.ogg`
- Verified clean public-domain or self-dedicated Commons status for later-variant tracks:
  - `Judith Bokor plays Valse triste by Sibelius.flac` via 1925 publication plus public-domain tags on Commons.
  - `Veni.sancte.spiritus.ogg` via uploader public-domain dedication on Commons.
  - `PhiladelphiaSymphonyOrchestra-DanseMacabre.ogg` via pre-1926 U.S. public-domain sound-recording basis on Commons.
  - `Dies.irae.ogg` via uploader public-domain dedication on Commons.

## Wiring audit result

- `music/chaosx_super_event_music.asset` contains live music definitions for ids `68-80`.
- `music/chaosx_super_event_music.txt` contains station rows for the Event 012 tracks.
- `sound/chaosx_sound.asset` contains soundeffect blocks for ids `68-80`.
- `music/chaosx_music_track_list.html` contains Africa rows for ids `68-80`, including the root-terminal row noting `80` as audio id with visible slot `72`.
- `docs/events/012_africa_foundation.md` and `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md` agree that the World Root terminal branch is an intentional hybrid: shared visible slot `72`, dedicated audio id `80`.
- On-disk files exist for all `13` live Africa music `.ogg` files and all `13` wrapper `.wav` files.

## Validation

- Confirmed durations for live `music/super_event_africa_*.ogg` files:
  - `112s` old seats
  - `116s` RSA peace
  - `118s` scramble / counterfeit crowns / dynamic union / forest parliament / root and fang
  - `120s` unification / world is one / continent sponsor / world root / archive world / world root terminal
- Confirmed `12` visible roles plus root-terminal audio id `80`.
- Confirmed all live Africa rows are present in the HTML track list.
- Compared archived final `.ogg` files in `docs/assets/.../final/` against live `music/` copies by SHA-256.

## Remaining blocker

One blocker remains.

- `africa_continent_sponsor` has a documentation/file-integrity mismatch.
- The archived final file is `docs/assets/012_africa/super_events/audio/final/super_event_africa_continent_sponsor.ogg`.
- The live file is `music/super_event_africa_continent_sponsor.ogg`.
- Their SHA-256 values do not match.
  - archived final: `c1b7ee2991b4ad4fbd89a1d546d0cd7c63d99ec1bbcdd6b375aac9d6347b81b4`
  - live music: `e93a668de3da9672e1df852118daa24254188627f79ca51f24611a22374e1aef`
- Both files have the same size and duration, and their decoded PCM hashes match, which strongly suggests container-level drift rather than a different audible track.
- The manifest previously listed a third stale hash (`77ee7af6039b942348e0c2d92a9ffa68c90cd0e2351d222660f8b4e48c63fcfe`), so the sponsor role was not fully self-consistent across docs and files.

## Non-blockers confirmed resolved

- Root-terminal audio id `80` is resolved, not a blocker.
- No missing Africa row remains in `music/chaosx_music_track_list.html`.
- No missing sound-definition block remains for ids `68-80`.
- No source-license blocker remains for the selected packaged tracks reviewed above.

## Docs changed by this audit

- `docs/assets/012_africa/super_events/audio/manifest.md`
- `docs/super_events/012_africa_super_event_research.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-19_012_africa_super_event_audio_final_audit.md`

## Parent action

- Reconcile `music/super_event_africa_continent_sponsor.ogg` against the archived final sponsor export, or explicitly document why the live copy intentionally differs.
- Until that is done, treat the Event 012 Africa super-event audio package as almost complete but not fully closed.
