# Event 012 Africa Root-Terminal Audio Resolution Handoff

Date: `2026-06-18`

Scope: resolved the outstanding audio blocker for `africa_world_is_one_root_variant_terminal` without editing gameplay, localisation, event, GUI, scripted localisation, sound definition, or music definition files.

## Files changed

- `docs/assets/012_africa/super_events/audio/source/siegfrieds_funeral_march_and_finale_us_marine_band.ogg`
- `docs/assets/012_africa/super_events/audio/final/super_event_africa_world_is_one_root_terminal.ogg`
- `docs/assets/012_africa/super_events/audio/manifest.md`
- `docs/super_events/012_africa_super_event_research.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_audio_root_terminal_resolution_handoff.md`

## Final recommendation

- Treat `africa_world_is_one_root_variant_terminal` as a distinct terminal-grade audio role.
- Do not reuse `super_event_africa_world_is_one.ogg`.
- Recommended later sound id: `super_event_africa_world_is_one_root_terminal`

Reason:

- Event 012 already separates base terminal, archive terminal, world-root escalation, and root-and-fang escalation in presentation language.
- The selected Wagner cue is legally cleaner than the earlier medium-confidence fallback pool and is materially different from both the base Chopin terminal and archive `Dies irae`.
- This keeps the root-terminal branch from sounding like a silent variant of an already-packaged ending.

## Selected package

- Role: `africa_world_is_one_root_variant_terminal`
- Final file: `docs/assets/012_africa/super_events/audio/final/super_event_africa_world_is_one_root_terminal.ogg`
- Source file: `docs/assets/012_africa/super_events/audio/source/siegfrieds_funeral_march_and_finale_us_marine_band.ogg`
- Title: `Siegfried's Funeral March and Finale`
- Composer: Richard Wagner
- Performer / recording source: United States Marine Band
- Source URL: `https://commons.wikimedia.org/wiki/File:Siegfrieds_funeral_march_and_finale.ogg`
- License: public domain composition and U.S. federal government public domain performance/recording on Commons
- License confidence: high
- Source duration: `629.603265s`
- Final duration: `120.000000s`
- Source SHA-256: `68124de4da401be0e07b2e2d637347e1a981b5cafa6ead74b5cd43f6becc6e41`
- Final SHA-256: `5f130776eb076abd275687cb104951874ef45c734553f14a6845d791e304bc31`

## Editing notes

- Kept the original Commons download intact.
- Exported the strongest terminal stretch from `240s` to `360s`.
- Applied a `4s` fade-out.
- Preserved stereo and `44.1 kHz` output.

Conversion command:

```bash
ffmpeg -y -ss 240 -t 120 -i docs/assets/012_africa/super_events/audio/source/siegfrieds_funeral_march_and_finale_us_marine_band.ogg -af "asetpts=N/SR/TB,afade=t=out:st=116:d=4" -ar 44100 -ac 2 -c:a libvorbis -q:a 5 docs/assets/012_africa/super_events/audio/final/super_event_africa_world_is_one_root_terminal.ogg
```

## Validation

- `ffprobe`: `44100 Hz`, `2` channels, `120.000000s`
- `volumedetect`: mean volume `-18.3 dB`, max volume `-0.2 dB`

## Remaining blockers

- None on licensing, sourcing, or conversion.
- Parent still needs to decide whether to wire this new id as a new terminal role or explicitly override that decision and document reuse instead. This pass recommends the new distinct cue.
