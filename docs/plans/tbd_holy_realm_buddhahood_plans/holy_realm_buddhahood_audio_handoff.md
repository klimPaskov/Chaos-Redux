# Holy Realm Buddhahood Audio Handoff

## Recommended package

- `The Awakened One`: [holy_realm_awakened_one_candidate.ogg](/home/klim/projects/chaos_redux/docs/assets/003_holy_realm_buddhahood/audio_research/processed/holy_realm_awakened_one_candidate.ogg)
  Source: Hariharan, `Buddham Saranam Gacchami - Male Voice, with Female Chorus`
  License: CC0 1.0
  Suggested id: `holy_realm_awakened_one_music`

- `Powers of the Awakened`: [holy_realm_powers_of_the_awakened_candidate.ogg](/home/klim/projects/chaos_redux/docs/assets/003_holy_realm_buddhahood/audio_research/processed/holy_realm_powers_of_the_awakened_candidate.ogg)
  Source: `Bhikkhu Pāṭimokkha Pali`
  License: CC BY 3.0
  Suggested id: `holy_realm_powers_of_the_awakened_music`

- `The Final Silence` non-terminal: [holy_realm_final_silence_nonterminal_candidate.ogg](/home/klim/projects/chaos_redux/docs/assets/003_holy_realm_buddhahood/audio_research/processed/holy_realm_final_silence_nonterminal_candidate.ogg)
  Source: `Bore Xinjing (Heart Sutra) ... layperson 2`
  License: CC0 1.0
  Suggested id: `holy_realm_final_silence_nonterminal_music`

- `The Final Silence` terminal: [holy_realm_final_silence_terminal_candidate.ogg](/home/klim/projects/chaos_redux/docs/assets/003_holy_realm_buddhahood/audio_research/processed/holy_realm_final_silence_terminal_candidate.ogg)
  Source: `Shikanotoone new`
  License status: Commons public-domain / PDM presentation
  Suggested id: `holy_realm_final_silence_terminal_music`

## Source files

- [buddham_saranam_gacchami_male_voice_female_chorus.oga](/home/klim/projects/chaos_redux/docs/assets/003_holy_realm_buddhahood/audio_research/source/buddham_saranam_gacchami_male_voice_female_chorus.oga)
- [bhikkhu_patimokkha_pali.ogg](/home/klim/projects/chaos_redux/docs/assets/003_holy_realm_buddhahood/audio_research/source/bhikkhu_patimokkha_pali.ogg)
- [heart_sutra_mandarin_layperson_2.ogg](/home/klim/projects/chaos_redux/docs/assets/003_holy_realm_buddhahood/audio_research/source/heart_sutra_mandarin_layperson_2.ogg)
- [shika_no_tone_shikanotoone_new.ogg](/home/klim/projects/chaos_redux/docs/assets/003_holy_realm_buddhahood/audio_research/source/shika_no_tone_shikanotoone_new.ogg)

## Required attribution

- `Powers of the Awakened` must keep attribution because the selected recording is CC BY 3.0.
- The two CC0 selections do not require attribution, but courtesy credit is still recommended in audio docs.
- The terminal `Shika no Tōne` variant should be treated as a medium-confidence public-domain candidate. Keep the detailed rights note from the research file when wiring it.

## Wiring status

- `The Awakened One` is wired to existing slot 7 via `music/super_event_buddha_mandate.ogg` and `sound/chaosx_super_event_buddha_mandate.wav`.
- `Powers of the Awakened` is wired to new slot 61 via `music/super_event_powers_of_the_awakened.ogg` and `sound/chaosx_super_event_powers_of_the_awakened.wav`.
- Non-terminal `The Final Silence` is wired to slot 8 via `music/super_event_final_silence.ogg` and `sound/chaosx_super_event_final_silence.wav`.
- Terminal `The Final Silence` is wired to slot 9 via `music/super_event_final_silence_thermonuclear.ogg` and `sound/chaosx_super_event_final_silence_thermonuclear.wav`.
- `gfx/super_events/super_event_powers_of_the_awakened.dds` now uses bespoke generated monochrome battlefield art. Source, prompt, processed PNG, and image manifest are under `docs/assets/003_holy_realm_buddhahood/super_event_images/`.

## Main risk

- If the project wants only explicit modern license grants with no public-domain-chain ambiguity, keep the non-terminal `Final Silence` chant and replace only the terminal `Shika no Tōne` candidate.
