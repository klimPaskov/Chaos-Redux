# Event001 Existing Asset Provenance and Suitability Audit

Audit date: 2026-10-05.

Disposition: the current runtime pictures are present and registered, but the sourced-asset package is incomplete and several images do not show the subjects specified in the event overview. Exact duplicate hashes are explainable as reuse of five installed vanilla pictures; duplicates alone do not prove a defect or approved design. Keep every unapproved image assignment `needs_user_review` until the parent records acceptance or routes an approved source replacement.

This was a read-only audit. I changed no runtime asset, GFX, event, portrait, source archive, or gameplay file. I wrote only this handoff.

## Scope and evidence

I inspected `events/001_communism_spread.txt`, `interface/001_communism_spread.gfx`, `interface/chaosx_characters.gfx`, `interface/chaosx_pictures.gfx`, `common/scripted_effects/001_communism_spread_effects.txt`, `docs/events/001_communism_spread/overview.md`, the 17 DDS files in `gfx/event_pictures/001_communism_spread/`, and `gfx/leaders/001_communism_spread/portrait_communist_rebels.dds`.

The Event001 report sprites are declared in `interface/001_communism_spread.gfx:93-157`; the portrait sprite is declared in `interface/chaosx_characters.gfx:151-152`. A targeted search of `interface/*.gfx` found no `GFX_report_event_communist_*` declarations in `interface/chaosx_pictures.gfx`.

The event source maps report sprites to event ids in `events/001_communism_spread.txt`; the design descriptions are in `docs/events/001_communism_spread/overview.md:223-240`. That overview calls the current DDS files placeholders and asks for unique pictures. This wording records a plan, not approval of the current pictures or a source-rights determination.

I read the canonical reference library rules and provenance entries in `.agents/skills/chaos-redux-event-assets/assets/gfx_references/README.md`, `REFERENCE_MANIFEST.md`, and the report rows in `CATALOG.md:354-359`, and visually inspected `event_art/report/contact_sheet.png`. The canonical contact sheet contains five review references; none is pixel-identical to the current Event001 pictures. The contact sheet is a review aid, not runtime art.

I also rendered in-memory comparison sheets from the five exact vanilla DDS matches and six exact vanilla strike/factory candidates for visual inspection. They were not saved because this audit owns only the handoff file. The user-provided captures `evt001_pop00.png`, `evt001_pop01.png`, and `evt001_pop03.png` were inspected as current-use evidence.

`hoi4.reference_context`, `hoi4.reference_search`, and `hoi4.reference_read` were not exposed in the connected tool list. This was a read-only visual provenance audit with no engine-facing edit, so no engine rule was inferred from missing MCP routes and no unrelated wiki sections were loaded.

## Report-picture inventory and provenance

There are 17 runtime DDS paths and 17 corresponding Event001 sprite aliases. The paths reduce to five unique whole-file SHA-256 hashes and five unique decoded RGBA pixel hashes. Each runtime whole-file hash exactly matches one installed vanilla file in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/event_pictures/`, scanned across 882 DDS files. The installed vanilla files are the immediate byte-identical sources; this does not establish their original photographer, date, archive, public-domain status, or redistribution license.

All current images have transparent corners and alpha extrema 0-255. Fifteen are 210x176; the two generic-rally DDS files are 209x176. The asset skill describes 210x176 as the standard processed report-card canvas. The parent clarified on 2026-10-05 that these generic-rally files' 209x176 dimensions are a valid vanilla-family native-size override, not a defect per se; do not resample them solely to force 210 pixels.

| Runtime DDS aliases and event consumers | Exact vanilla source and dimensions | Runtime SHA-256 | Decoded RGBA pixel SHA-256 | Visual fit against the overview |
| --- | --- | --- | --- | --- |
| `communist_insurgency_start` (`chaosx.nr1.1`), `communist_state_control` (`.4`), `communist_world_revolution_whispers` (`.13`), `communist_world_revolution_foreshadowing` (`.16`, `.30`, `.31`, `.32`) | `gfx/event_pictures/report_event_stalin_propaganda.dds`, 210x176 | `50d1cecabd1a1fb435d90e8f8b5f47f008af553e8ec2b625e758d4af9858d0b0` | `9398af6190807194babf957c781b5c8357617c5a5459f416dd218870efcfc864` | The poster is a clear thematic fit for the initial insurgency and local communist control; the supplied `pop00` and `pop01` captures show those uses. It does not depict the overview's clandestine cells, couriers, or cross-border map for the later whisper and foreshadowing events, so those aliases remain needs-review. |
| `communist_control_escalates` (`.5`), `communist_dark_worker_rituals` (`.12`), `communist_emergency_intervention` (`.3`), `communist_intervention_backfire` (`.7`), `communist_surprise_revolt` (`.14`, `.18`, `.19`), `communist_unstable_activity` (`.11`), `communist_uprising` (`.10`), `communist_war_warning` (`.8`), `communist_worker_ritual` (`.15`, `.27`, `.28`, `.29`) | `gfx/event_pictures/report_event_worker_protests.dds`, 210x176 | `b89f281b33f667167e41569d94b358beff8a36a69cb054605a0b4af0fa45bcb1` | `152902aa75465557dab34127ee74ce60c37407cddbd8bb6e9f59dad8db70ed17` | The visible worker crowd and signs can support organizing, strikes, or an intervention backfire. It does not show police or loyal troops (`.3`), an armed uprising or militia mobilization (`.10`, `.8`), a hidden cell/cache (`.11`), or a factory ritual (`.12`, `.15`, `.27-.29`); those are specific subject mismatches. Escalation and surprise revolt also lack the described barricades, control, or sudden armed action. |
| `communist_intervention_success` (`.6`), `communist_emergency_success` (`.9`) | `gfx/event_pictures/report_event_generic_rally.dds`, 209x176 | `65a65ef3d86658a4c9d0aeaded8a935dc08ee50d4a7a8217dc1fd8ad13e5b80a` | `34f62942b34de8ba5ae5599d4393ffef3927874ab108ae49c2dc5962d32fa1cd` | The crowd rally does not show seized weapons, arrests, restored loyal authority, or loyal troops holding a cleared site. Both aliases remain needs-review for scene fit. The parent accepts this vanilla-native 209x176 size as a family override. |
| `communist_industry_sabotage` (`.2`, `.34`) | `gfx/event_pictures/report_event_FIN_helsinki_bombed.dds`, 210x176 | `2ba641a4e47267f273c9d2929ce5e1f264898119505c6200da6589afd55f5e7e` | `380986e6ffe827dfc88b55a60212902f6159202c441d49510f290655e9d9d8f9` | The image shows a bomb-damaged Helsinki street, not factory machinery, a rail depot, or workers disrupting production. The supplied `pop03` capture shows it under the coordinated strike-wave event; consistent with the parent's stated atmospheric reading, the ruined street is visually legible there, but the source image contains no strike action and its named historical context remains a provenance/context issue. For `.2` industry sabotage, it is a direct mismatch to the overview's requested subject. |
| `communist_insurgency_defeated` (`.17`) | `gfx/event_pictures/report_event_generic_parliament.dds`, 210x176 | `3463efe78172032a555cfa534eca2f40f95beae4c46c13bad7c066017b49f233` | `6860e8b24db4facd7001c17025c4e076a9325a3206d3113b3ab552e16d781914` | The assembly at a political hall does not show a cleared committee, removed banner, insurgent defeat, or restored office. It is an unclear substitute and needs review. |

The report aliases above are not separate scenes merely because they have separate filenames. The nine worker-protest files, four poster files, two rally files, and other single aliases have byte-identical installed vanilla sources as listed. Reusing a source can be legitimate when the accepted design calls for it, but the current overview still says the existing files are placeholders and specifies more distinct scenes; no accepted amendment authorizing these substitutions was in the inspected scope. The parent is considering documenting the current five-image reuse as intentional and retiring that stale placeholder wording instead of creating 17 new images; record that as the accepted reuse contract if chosen.

## Strike and industrial-protest replacement candidate

The strongest exact vanilla report-picture candidate for the strike and production-disruption slot is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/event_pictures/report_event_generic_strike.dds`, 210x176, whole-file SHA-256 `526aa7ad0da0a94fb6eb7b33ccdfe7e185aaf88e8f41c844a5941194c8f54191`, and decoded RGBA pixel SHA-256 `223dc225064e4f97e7f7c9e82eb79f1faaeb96ef20b05efd45f85f1ddea271cc`.

Visual comparison shows workers assembled indoors with a speaker in an industrial/workplace setting. It reads as an actual strike meeting and avoids the air-raid damage shown by `report_event_FIN_helsinki_bombed.dds`; it is the best match I found for both `chaosx.nr1.2` and the coordinated strike wave at `chaosx.nr1.34`.

Other exact vanilla candidates inspected were `report_event_worker_protests.dds` (street crowd with protest signs), `report_event_gathering_protest.dds` (generic mass protest), and `report_event_generic_factory.dds` (workers and machinery, without a stoppage). The generic-strike image is the clearest fit for coordinated labor action. All three alternatives are also available under the installed vanilla `gfx/event_pictures/` directory, but the generic-factory candidate is 209x176 and the gathering-protest scene is less specifically about workers.

If the parent accepts this replacement, one bounded copy from the exact vanilla source path to the existing runtime slot `gfx/event_pictures/001_communism_spread/communist_industry_sabotage.dds` serves both event consumers without changing their sprite names or paths. The source date, photographer, archive, and redistribution license remain unknown, and this audit did not make that runtime copy.

## Visual review of supplied runtime captures

`evt001_pop00.png` shows `chaosx.nr1.1` with the Stalin-propaganda poster, which reads as a communist organizing poster. `evt001_pop01.png` shows `chaosx.nr1.4` with the same poster, which is consistent with the described spread of local communist influence. These two uses have direct screenshot evidence of a coherent visual match.

`evt001_pop03.png` shows `chaosx.nr1.34` with the Helsinki-bombing rubble image. It is usable as an atmospheric urban-damage image in that capture, as the parent prompt states, but it does not depict a workers' strike. The original source context should be kept distinct from any interpretation of the screenshot.

The captures cover three events only. They do not establish visual acceptance of the other aliases, establish asset source rights, or replace source and processed previews.

## Asset package and licensing gaps

The expected event workspace `docs/assets/001_communism_spread/` is absent. No retained source PNGs, processed report PNGs, event asset manifest, or per-asset provenance handoff were found at that path. The existing runtime DDS files can be traced to installed vanilla DDS files by hash, but the immediate copy is not a documentary source archive.

The canonical report catalog identifies its five reference examples as Vanilla HOI4 and names their vanilla paths, but those five files are not pixel matches for the Event001 runtime images, and the catalog does not supply the runtime images' original photo authors, capture dates, archives, or rights. I found no evidence supporting public-domain or Creative Commons claims for the five exact vanilla matches; license status must remain unknown.

Do not mark the current pictures `complete` from hash matches alone. For each alias still intended for runtime, the parent should record an explicit visual acceptance or route clear scene mismatches to `chaosx_asset_source_researcher` for archival source and license research. Any generated replacement must be separately authorized and handled as fictional/documentary scene art; this audit produced no art. The parent has accepted the generic-rally 209x176 vanilla-native size as a family override, while its scene mismatch remains open.

## Portrait handoff

The runtime portrait is `gfx/leaders/001_communism_spread/portrait_communist_rebels.dds`, 156x210, 131,188 bytes, SHA-256 `7e6a0404c9b329b9a3ec4a345132cfad49ee13facc3fb7591e81e3946e6c4efcc`. Its sprite is `GFX_portrait_communist_rebels`. Two consumers in `common/scripted_effects/001_communism_spread_effects.txt:2363-2366` and `:2453-2456` name the leaders `Revolutionary Committee` and `Local Revolutionary Committee`; neither consumer names a historical individual.

A bounded raw-file hash comparison against all 1,129 installed vanilla `gfx/leaders/**/*.dds` files found no exact vanilla hash match. The expected durable source package `docs/assets/portraits/001_communism_spread/` is absent, and a targeted filename search under `docs/assets/portraits/` found no `communist_rebels`, `communist`, or `001_communism_spread` source file. The parent clarifies that the subjects are a fictional, globally generated collective named `Revolutionary Committee` and `Local Revolutionary Committee`, not historical individuals. I did not research identity, visually inspect or alter the portrait, or infer the current image's source mode. Route its production and provenance gate to `chaosx_portrait_creator`; current source documentation remains `needs_user_review`, not `complete`.

## Audit snapshot hashes

The following hashes identify the inspected project inputs at audit time.

- `events/001_communism_spread.txt`: `18d346747f3fd5ef5a46196656180b569e14708d793f2ab38c89219bcba4a27d`.
- `interface/001_communism_spread.gfx`: `be59637a511fe8611d184238f67ec3f8d8a9c223e061065756adeadc43f8b3fb`.
- `interface/chaosx_pictures.gfx`: `1c4d4a11711e98e959e47dc471c601a48d8c2659ac2df2fa3e796dcf8a172ff0`.
- `interface/chaosx_characters.gfx`: `b4f9b8c8115f41bb92e7fd82f6c4f029b88814037ec5f11c443412a3c4010576`.
- `interface/chaosx_pictures.gfx`: `1c4d4a11711e98e959e47dc471c601a48d8c2659ac2df2fa3e796dcf8a172ff0`.
- `common/scripted_effects/001_communism_spread_effects.txt`: `a8408e327196c027d89890fd86205bffc65afb572dfcda6770600158d3e6d8f4`.
- `docs/events/001_communism_spread/overview.md`: `6cf23e04de17d07619e5f668ee054a90170a708d098fb8626fea15fcecbd903a`.
- `evt001_pop00.png`: `2b44ca99ee84cae8f2745c482b79be9401f192feb2493d7ee69a1c060602b40f`.
- `evt001_pop01.png`: `76e4d36976812823b274d5c7a04d44019da27cd56baadf8b3b0dd8d837dc6605`.
- `evt001_pop03.png`: `c42c8b1ef2e487f64e417a056c5ca59c35716349f8e31d97415fb96736189503`.

Unresolved items: source author/archive/date/license and source-image archives for all five vanilla-derived groups; parent acceptance or replacement for mismatched report aliases; whether to copy the exact vanilla generic-strike DDS into the current industry-sabotage slot; and portrait image/source-mode provenance review by the portrait owner.
