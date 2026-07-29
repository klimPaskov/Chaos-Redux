# Mengele super-event prompt

Use this for the super-event research and wiring pass after the coding agent verifies the live super-event slots.

## Required reading

- `chaos-redux-super-events`.
- `chaos-redux-event-assets` for image handoff.
- `specs/mengele_super_event_acceptance_criteria.md`.
- The verified super-event localisation, GFX, audio, event, and docs files in the repository.

## Super-events to verify

1. Angel Directorate reveal. Current source names `GFX_super_event_angel_directorate`, slot and audio ID `12`, `sound/003_holy_realm/super_event_12_angel_directorate.wav`, and `chaosx_super_event_angel_directorate_track`.
2. Angelic World Order, if the final clone-network world-end branch is live.
3. Aryan Supremacy title variant, if the Aryan branch is live.

## Text research

Spawn `chaosx_super_event_text_researcher` with `fork_context=false` for final quote and button research. The prompt must include the exact super-event role, the verified slot, the final trigger, and the sensitivity rules.

Requirements:

- Use real traceable quotes only.
- Prefer public-domain, historical, philosophical, political, legal, religious, or literary sources for the main quote.
- Do not invent quotes.
- Avoid quote-site material without verification.
- Keep modern copyrighted references out of the main quote.
- Button text can use a short cultural or historical allusion only after source checks.
- No gore, mockery of victims, heroic perpetrator framing, or joke reward framing.

## Audio research

Spawn `chaosx_super_event_audio_researcher` with `fork_context=false` if the existing track is missing, undocumented, poorly licensed, wrong format, reused without approval, or mismatched.

Requirements:

- Preserve source audio.
- Document title, creator, performer or recording source, URL, license, duration, usage terms, conversion notes, and uncertainty.
- Convert final WAV to 44.1 kHz.
- Verify sound and sound definitions.
- Update audio docs and track list as required by repo convention.

## Image work

Use `chaosx_asset_source_researcher` for archival or documentary source imagery. Use `chaosx_generated_event_art` only for symbolic or fictional presentation that does not claim to show actual victims, experiments, or real person likenesses.

The current source says the Angel Directorate image is registered but contains default super-event art. Replace it or document repo evidence that it was already replaced.

## Wiring checks

The final event effect must set visibility and audio id, use settings-aware playback, avoid duplicates, update docs, and align spreadsheet-facing wording after localisation is final.
