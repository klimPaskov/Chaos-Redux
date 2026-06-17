# Event 012 Africa Audio Research Handoff

Date: `2026-06-16`
Scope: bounded super-event audio research only

Current status note: this research-only handoff was superseded by the later audio packaging handoffs and manifest. It is retained for source-discovery provenance; use `docs/assets/012_africa/super_events/audio/manifest.md` for current packaged-file status.

## Files changed

- `docs/super_events/012_africa_super_event_research.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_audio_research_handoff.md`

## Work completed

- Researched clearly licensed or public-domain audio candidates for the required Event 012 Africa super-event role set.
- Verified source provenance from primary file pages, mainly Wikimedia Commons.
- Checked existing documented Chaos Redux super-event audio notes to avoid obvious reuse of already documented final tracks.
- Documented per-role:
  - source URL
  - creator / performer
  - license / provenance
  - duration
  - trim / transformation note
  - placeholder sound id
  - proposed final path
  - legal / technical usability status

## Important non-actions

- No gameplay, localisation, interface, focus, decision, event, or shared scripted-localisation files were edited.
- No `sound.asset` or `music.asset` wiring was added.
- No audio files were downloaded, trimmed, or exported in this pass.

## Main findings

- Cleanest high-confidence picks:
  - `South African national anthem.oga` for unification
  - `Holst- mars.ogg` for scramble reaction
  - `Beethoven_EgmontOvertureOp.84...ogg` for continent-sponsor or counterfeit-crowns pressure
  - `Holst First Suite March.ogg` for old-seats reveal
- Usable but lower-confidence / follow-up-needed picks:
  - `JOHN MICHEL CELLO-BEETHOVEN SYMPHONY 7 Allegretto.ogg` because the rights are VRT-confirmed rather than a simple public-domain tag
  - `PMLP02751-S002-07-Mozart Requiem Mass.ogg` because the performer is not surfaced clearly on the summary block
  - `Allegri - Miserere Mei, Deus - Ensamble Escénico Vocal (audio).ogg` because the rights chain runs through a YouTube Creative Commons declaration
  - `Veni.creator.spiritus.ogg` because it is only `30` seconds and would need looping or doubling

## Remaining blockers

1. No final `.ogg` candidates exist on disk yet; packaging remains undone.
2. Archive / bestiary roles still need a uniqueness pass if multiple of them survive to implementation.
3. Technical validation still needs real downloads and `44.1 kHz` export checks.

## Suggested next step

Pick the subset of Event 012 super-events that will definitely be implemented first, then run a second pass to:

- download the selected sources;
- preserve originals under `docs/assets/012_africa/super_events/audio/source/`;
- export final `44.1 kHz` `.ogg` files under `docs/assets/012_africa/super_events/audio/final/`;
- write a small manifest with hashes, durations, and exact conversion commands.
