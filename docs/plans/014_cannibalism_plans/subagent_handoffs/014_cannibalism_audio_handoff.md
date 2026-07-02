# Event 014 Cannibalism Audio Handoff

Scope completed:

- researched and verified four super-event audio candidates
- preserved legitimate source downloads
- converted four game-ready `.ogg` candidates at `44100 Hz`
- documented source, license, durations, edit notes, and recommended use

Scope not touched:

- no sound definition edits
- no event wiring
- no localisation edits

## Recommended package

1. Cannibal islands reveal
- Use: `music/super_events/014_cannibalism/014_cannibalism_islands_reveal_purcell.ogg`
- Suggested audio id: `chaosx_se_014_cannibalism_islands_reveal_audio`
- Rights note: `CC BY-SA 3.0`; attribution and edited-derivative notice required

2. Hannibal network reveal
- Use: `music/super_events/014_cannibalism/014_cannibalism_hannibal_network_handel.ogg`
- Suggested audio id: `chaosx_se_014_cannibalism_hannibal_network_audio`
- Rights note: public domain
- Wiring note: keep blocked until Hannibal content exists

3. World-end terminal route
- Use: `music/super_events/014_cannibalism/014_cannibalism_world_end_dies_irae.ogg`
- Suggested audio id: `chaosx_se_014_cannibalism_world_end_audio`
- Rights note: public domain

4. Defeat aftermath
- Use: `music/super_events/014_cannibalism/014_cannibalism_defeat_aftermath_in_memoriam.ogg`
- Suggested audio id: `chaosx_se_014_cannibalism_defeat_aftermath_audio`
- Rights note: public domain

## Validation

Verified with `ffprobe`:

- `014_cannibalism_islands_reveal_purcell.ogg`: Vorbis, stereo, `44100 Hz`, `127` seconds
- `014_cannibalism_hannibal_network_handel.ogg`: Vorbis, stereo, `44100 Hz`, `142` seconds
- `014_cannibalism_world_end_dies_irae.ogg`: Vorbis, stereo, `44100 Hz`, `118` seconds
- `014_cannibalism_defeat_aftermath_in_memoriam.ogg`: Vorbis, stereo, `44100 Hz`, `136` seconds

## Practical notes for the parent agent

- The `In Memoriam` Commons `.oga` source carries an attached picture stream. I preserved it, but the clean final render was made from the linked `mp3` source variant from the same Commons entry.
- The islands cue is the only non-public-domain selection. If you want a strictly PD package, switch that slot to the documented Chopin backup before wiring.
- Full research details, backups, attribution text, and source URLs are in `docs/super_events/014_cannibalism_super_event_research.md`.
