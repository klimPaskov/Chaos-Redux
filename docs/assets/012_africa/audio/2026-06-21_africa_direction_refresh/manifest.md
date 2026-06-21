# Event 012 Africa Audio Direction Refresh Manifest

Date: `2026-06-21`

Scope: replacement-candidate audio package for Event `012` Africa super-event slots `68-80` after the existing Europe-heavy anthem/classical direction was rejected.

Package root: `docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/`

This package does not edit live `music/`, `sound/`, localisation, or scripted wiring. It delivers replacement `.ogg` finals, preserved source files, license notes, and parent wiring guidance only.

## Validation

- Final format target: `44.1 kHz` stereo `.ogg`
- Validation command:

```bash
for f in docs/assets/012_africa/audio/2026-06-21_africa_direction_refresh/final/*.ogg; do
	ffprobe -v error -show_entries format=duration:stream=sample_rate,channels -of default=nk=1:nw=1 "$f"
done
```

- Result: all final files are `44100 Hz`, `2` channels, and render to the expected slot-length range.

## Source inventory

All accepted source files are preserved under `source/`.

- `kagoma_drummer.ogv`
  - Source page: `https://commons.wikimedia.org/wiki/File:Kagoma_Drummer.ogv`
  - Recording/source: village drummer in Kagoma, Kaduna State, Nigeria
  - Author: Meredithdevoe
  - License: `CC BY-SA 4.0`
  - License confidence: high
  - Source SHA-256: `0f93000eb8c34ba85a220dc581b547e45392f153e34f62f68d200550b7e19278`

- `Rush%20Peace%20dance%20concert%201%20libtheora.ogv`
  - Source page: `https://commons.wikimedia.org/wiki/File:Rush_Peace_dance_concert_1_libtheora.ogv`
  - Recording/source: Ghana peace-dance competition performance
  - Author: Myraclera
  - License: `CC BY-SA 4.0`
  - License confidence: high
  - Source SHA-256: `92c64f02692e3ccb23f6b48fc3969c9b97f5a10a97fde2470f9807d20bd9efa1`

- `Rush%20Peace%20dance%20concert%202%20libtheora.ogv`
  - Source page: `https://commons.wikimedia.org/wiki/File:Rush_Peace_dance_concert_2_libtheora.ogv`
  - Recording/source: Ghana peace-dance competition performance
  - Author: Myraclera
  - License: `CC BY-SA 4.0`
  - License confidence: high
  - Source SHA-256: `bc8899658245694d00c586aecea4eb336121c6a552e7873f312972b71978ec5b`

- `Ghana%20Dancers%20Group.ogv`
  - Source page: `https://commons.wikimedia.org/wiki/File:Ghana_Dancers_Group.ogv`
  - Recording/source: Ghana dancers group battle dance
  - Author: Celestinesucess
  - License: `CC BY-SA 4.0`
  - License confidence: high
  - Source SHA-256: `3efcaa1344ec6ae10fc487fda83b0dfc46d3705c649aeb3576f6fcd6918ff1ef`

- `Bawa%20Dance%20libtheora.ogv`
  - Source page: `https://commons.wikimedia.org/wiki/File:Bawa_Dance_libtheora.ogv`
  - Recording/source: Bawa dance, Northern/Upper Ghana
  - Author: Myraclera
  - License: `CC BY-SA 4.0`
  - License confidence: high
  - Source SHA-256: `92170d4488621e4a2be6793fdd92233ee4fcebc2870b7201967632e1a81012dc`

- `Mapoch.-%20Playing%20music%20in%20Ndebele%20Village.ogv`
  - Source page: `https://commons.wikimedia.org/wiki/File:Mapoch.-_Playing_music_in_Ndebele_Village.ogv`
  - Recording/source: Ndebele village performance, South Africa
  - Author: Pierre Andre Leclercq
  - License: `CC BY-SA 4.0`
  - License confidence: high
  - Source SHA-256: `dab6d081c6ab661d84511509974f0637aeb19faeae7aaf8915ba226318f6589c`

- `Southern%20Ndebele%20music%20video%20.ogv`
  - Source page: `https://commons.wikimedia.org/wiki/File:Southern_Ndebele_music_video_.ogv`
  - Recording/source: Southern Ndebele musicians in Botshabelo, South Africa
  - Author: Pierre Andre Leclercq
  - License: `CC BY-SA 4.0`
  - License confidence: high
  - Source SHA-256: `8815fe93dee5715f81ca837c302a252b4a502c00fb310030cdfa545865dfa618`

- `Traditional%20Adowa%20dance%20form%20and%20music%20performance.ogv`
  - Source page: `https://commons.wikimedia.org/wiki/File:Traditional_Adowa_dance_form_and_music_performance.ogv`
  - Recording/source: Adowa dance/music performance, Ghana
  - Author/source note: Commons page records a Flickr-reviewed import
  - License: `CC BY-SA 2.0 Generic`
  - License confidence: high
  - Source SHA-256: `d20924080fedaf53ad68a2c888ffcd95b3c9a9e9d91b87f7c24733a00745d68b`

- `Traditional%20Sounds%20-%20Igbo%20Language%20-%20Nsukka%20-%20Enugu%20State%20-%20Nigeria.ogg`
  - Source page: `https://commons.wikimedia.org/wiki/File:Traditional_Sounds_-_Igbo_Language_-_Nsukka_-_Enugu_State_-_Nigeria.ogg`
  - Recording/source: Igbo traditional sounds, Nsukka, Enugu State, Nigeria
  - Author: Arch-Angel Raphael the Artist
  - License: `CC BY-SA 4.0`
  - License confidence: high
  - Source SHA-256: `0cb66082f030f0d213739bf5ba38407f211444809f461b364d2b094dd07bb455`

- `Live%20Band%20at%20a%20Traditional%20Marriage%20-%20Igbo%20Tribe%20-%20Imo%20State%20-%20Nigeria.ogg`
  - Source page: `https://commons.wikimedia.org/wiki/File:Live_Band_at_a_Traditional_Marriage_-_Igbo_Tribe_-_Imo_State_-_Nigeria.ogg`
  - Recording/source: live band at an Igbo traditional marriage, Imo State, Nigeria
  - Author: Arch-Angel Raphael the Artist
  - License: `CC BY-SA 4.0`
  - License confidence: high
  - Source SHA-256: `575bf9503b2d90a9ea26f3d0ca303b8619d61e02de7cab4f7d7a535004ddc53b`

## Final slot package

### Slot `68` / `super_event_africa_unification`

- Final path: `final/super_event_africa_unification.ogg`
- Final SHA-256: `1d348c562facc87cddbddb0859676cbfb957d369ab00dc0142419bc9331861e2`
- Duration: `120.000000s`
- Source: `Rush%20Peace%20dance%20concert%201%20libtheora.ogv`
- Edit: excerpt starting `46s`, trimmed to `120s`, `3s` fade-out, loudness normalized
- Why it fits: large communal dance/percussion energy reads as a continental proclamation better than a brass hymn or European march

### Slot `69` / `super_event_africa_scramble`

- Final path: `final/super_event_africa_scramble.ogg`
- Final SHA-256: `4e8ecb12d5633c34aa075bbad3efb5a7e69ccd689e77abc4e6737c8e78ffca35`
- Duration: `118.000000s`
- Source: `kagoma_drummer.ogv`
- Edit: main performance body trimmed to `118s`, `3s` fade-out, normalized
- Why it fits: raw solo drumming keeps the cue tense and immediate without drifting back into European war-music shorthand

### Slot `70` / `super_event_africa_old_seats`

- Final path: `final/super_event_africa_old_seats.ogg`
- Final SHA-256: `a2b5c81dae94e0b8bd3b1da2aa87bbade59238cd878c055068e66bdaacbe88fd`
- Duration: `112.000000s`
- Source: `Traditional%20Sounds%20-%20Igbo%20Language%20-%20Nsukka%20-%20Enugu%20State%20-%20Nigeria.ogg`
- Edit: looped once to cover length, trimmed from `0.25s` to `112.25s`, `3s` fade-out, normalized
- Why it fits: more archival and processional than celebratory, which suits the old-seats registry/record tone

### Slot `71` / `super_event_africa_counterfeit_crowns`

- Final path: `final/super_event_africa_counterfeit_crowns.ogg`
- Final SHA-256: `83be15668ef20dce4875660ff728590509dbd1856fdaefd0f9efb98c3e88b4c2`
- Duration: `118.000000s`
- Source: `Rush%20Peace%20dance%20concert%202%20libtheora.ogv`
- Edit: excerpt starting `4s`, trimmed to `118s`, `3s` fade-out, normalized
- Why it fits: public-performance force and rhythmic pressure sell exposure and legitimacy crisis better than stately coronation music

### Slot `72` / `super_event_africa_world_is_one`

- Final path: `final/super_event_africa_world_is_one.ogg`
- Final SHA-256: `6729b44e767ef67dc0676acf64e90fd2d2933db03d77ef7d033b0e4af124d053`
- Duration: `120.000000s`
- Source: `Ghana%20Dancers%20Group.ogv`
- Edit: first `111s` slowed with `atempo=0.92`, low-pass filtered, trimmed to `120s`, `4s` fade-out, normalized
- Why it fits: this is the strongest terminal cue in the package without importing outside classical material; the slowing/filtering keeps it ominous rather than festive

### Slot `73` / `super_event_africa_continent_sponsor`

- Final path: `final/super_event_africa_continent_sponsor.ogg`
- Final SHA-256: `61305b0068e366f033e7d9c3c062c82f897bbe2bd878c0e74fc8a3686cc626b4`
- Duration: `120.000000s`
- Source: `Bawa%20Dance%20libtheora.ogv`
- Edit: looped once to fill runtime, trimmed to `120s`, `3s` fade-out, normalized
- Why it fits: a steady Ghanaian dance pulse suggests exported movement, organization, and momentum without sounding like a colonial brass parade

### Slot `74` / `super_event_africa_rsa_allies_peace`

- Final path: `final/super_event_africa_rsa_allies_peace.ogg`
- Final SHA-256: `a2ecd765a41090875013f4be772e5d9e45405a87eb106db65d039fc34608a640`
- Duration: `116.000000s`
- Source: `Mapoch.-%20Playing%20music%20in%20Ndebele%20Village.ogv`
- Edit: looped village-performance segment to `116s`, `3s` fade-out, normalized
- Why it fits: reflective communal music is more credible for an exhausted settlement aftermath than triumphal military scoring

### Slot `75` / `super_event_africa_dynamic_cross_continent_union`

- Final path: `final/super_event_africa_dynamic_cross_continent_union.ogg`
- Final SHA-256: `363d5871d5ff5250da9307757f57c1d666c936fe02f6e89462d349a80ffe9cb2`
- Duration: `118.000000s`
- Source: `Rush%20Peace%20dance%20concert%201%20libtheora.ogv`
- Edit: second distinct excerpt starting `246s`, trimmed to `118s`, `3s` fade-out, normalized
- Why it fits: the long Ghana source had enough internal movement to support a separate union-scale cue without sounding identical to slot `68`

### Slot `76` / `super_event_africa_forest_parliament`

- Final path: `final/super_event_africa_forest_parliament.ogg`
- Final SHA-256: `f9f18e5370908a2d7aa1a812953d2ad4a6a1b0c43efa30a299f1b6ad0229723d`
- Duration: `118.000000s`
- Source: `Southern%20Ndebele%20music%20video%20.ogv`
- Edit: looped to `118s`, `3s` fade-out, normalized
- Why it fits: group-vocal/percussive texture reads as a living collective assembly rather than a human-only state anthem

### Slot `77` / `super_event_africa_world_root`

- Final path: `final/super_event_africa_world_root.ogg`
- Final SHA-256: `c1c310d8b6023048bf24ff58468db00826041d20e1520bb1c666088a9f6ec883`
- Duration: `120.000000s`
- Source: `Traditional%20Adowa%20dance%20form%20and%20music%20performance.ogv`
- Edit: looped repeatedly to `120s`, `3s` fade-out, normalized
- Why it fits: the repeating Adowa pulse gives the root-path a ritual/public-force character rather than a fantasy drone

### Slot `78` / `super_event_africa_root_and_fang`

- Final path: `final/super_event_africa_root_and_fang.ogg`
- Final SHA-256: `4b3a8d532a7271e81fe57e368345401629cbfb183eedb566b71510c173b02d3d`
- Duration: `117.800000s`
- Source: `Live%20Band%20at%20a%20Traditional%20Marriage%20-%20Igbo%20Tribe%20-%20Imo%20State%20-%20Nigeria.ogg`
- Edit: looped repeatedly to the maximum clean render length, `3s` fade-out, normalized
- Why it fits: the clipped, sharp live-band pulse lands as the most aggressive short-loop option in the downloaded set
- Note: final render settles at `117.8s`; technically fine, but slightly under the nominal `118s` target

### Slot `79` / `super_event_africa_archive_world`

- Final path: `final/super_event_africa_archive_world.ogg`
- Final SHA-256: `37e919dedb1b32b81c36302537ad0984891b541acc77bb04efd3ecb03974cae0`
- Duration: `120.000000s`
- Source: `Rush%20Peace%20dance%20concert%201%20libtheora.ogv`
- Edit: third distinct excerpt starting `398s`, low-pass filtered, trimmed to `120s`, `3s` fade-out, normalized
- Why it fits: this excerpt keeps institutional scale but sounds more distant and archival than the unification/union cuts

### Slot `80` / `super_event_africa_world_is_one_root_terminal`

- Final path: `final/super_event_africa_world_is_one_root_terminal.ogg`
- Final SHA-256: `712944fabb019157d63ba90d38f85f3d975b8932d48e8b8dd74233bdbd7fc6f1`
- Duration: `120.000000s`
- Source: `Traditional%20Sounds%20-%20Igbo%20Language%20-%20Nsukka%20-%20Enugu%20State%20-%20Nigeria.ogg`
- Edit: alternate later-section cut from `18s` to `138s`, low-pass filtered, `4s` fade-out, normalized
- Why it fits: this stays recognizably rooted in the same archival/traditional sound family as slot `70` while turning colder and more terminal

## Attempted but blocked archival additions

- `chirillo_gallica.bin`
  - Intended use: darker archival terminal/aftermath support
  - Source target: Commons page for the 1931 lamentation recording and its Gallica origin
  - Outcome: Wikimedia file-download requests were rate-limited (`HTTP 429`), and the direct Gallica media endpoint returned HTML rather than a decodable audio object in this pass
  - Blocker status: real blocker, documented for parent follow-up

## Package assessment

- This package successfully replaces the rejected Europe-heavy direction with African-source percussion/vocal/live-performance material.
- The main compromise is source reuse:
  - `Rush Peace dance concert 1` is used for slots `68`, `75`, and `79` via different excerpts and filtering.
  - `Traditional Sounds - Igbo...` is used for slots `70` and `80`.
- That reuse is intentional and documented, not hidden.
