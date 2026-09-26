# IW-040/KUB Ivanis grounded portrait handoff

Date: 2026-09-26.

Owner: `chaosx_portrait_creator`.

Disposition: `blocked` at source-rights gate; no portrait asset or runtime wiring was produced.

## Accepted scope

The accepted amendment in [Part 5](../../../specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md) authorizes research and preparation of an exact-identity `source_placeholder` for the existing grounded character `KUB_ivanis_vasily_nikolaevich`. It supersedes the 2026-09-19 gap handoff only for this source-placeholder research/production authorization. It does not authorize an alternate leader, generated real-person likeness, unsupported source, or agent-run RunPod final.

## Research result

The [source research record](../../../assets/portraits/006_independence_wave/portrait_KUB_ivanis_vasily_nikolaevich_source_research_blocked_2026-09-26.md) documents the exact subject, installed vanilla consumers, canonical leader references, source candidates, attribution, dimensions, hashes, source-level visual review, rights claims, and blockers.

The one-person Commons portrait is identified by the Internet Encyclopedia of Ukraine but its Commons record says both `Date=unknown` and `PD-Ukraine` on the basis of pre-1952 publication; no archive, photographer, publication record, or permission substantiates that claim. The contemporary 1920 Commons group photo explicitly identifies Ivanis as the sixth seated person but lists an unknown photographer, a LiveJournal root as source, and an unsubstantiated `PD-old` claim. A separate 1942 group photo carries CC BY-SA 4.0 but does not identify Ivanis at person level. No source passed both identity and rights checks.

## Files changed

- `docs/assets/portraits/006_independence_wave/portrait_KUB_ivanis_vasily_nikolaevich_source_research_blocked_2026-09-26.md` — source and rights research record; no source binary was archived because rights are unresolved.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw040_kuban_ivanis_portrait_source_placeholder_2026-09-26.md` — this handoff.

## Production and wiring state

- Classification remains `grounded_source_only`; requested source mode is `source_placeholder`; package portrait disposition is `blocked`.
- No original source, source crop, crop JSON, processed 156x210 PNG, provenance contract, DDS, or portrait asset manifest was created.
- `interface/006_independence_wave_portraits_registry.gfx` was not changed and has no `GFX_portrait_KUB_ivanis_vasily_nikolaevich_independence_wave` entry. The target DDS path `gfx/leaders/006_independence_wave/portrait_KUB_ivanis_vasily_nikolaevich_independence_wave.dds` is absent.
- No character, setup, cleanup, event, focus, decision, localisation, or country file was changed. Existing ordinary KUB uses keep their vanilla portrait token; the parent-owned Event 006 conditional setup/cleanup wiring remains absent pending a cleared source asset.
- No ImageGen was used because the subject is real. RunPod was never opened, operated, configured, queued, or monitored.
- Replacement state is `blocked`, not `replacement_pending`; the placeholder was not installed and the user has not supplied a styled final.

## Review and validation

The installed `common/characters/KUB.txt` and No Step Back `.gfx` declarations were rechecked. The large vanilla portrait sprite points to an absent DDS in the installed game tree; the small idea sprite resolves to an existing 65x67 RGBA DDS with SHA-256 `c215128b588ffff5b03fc1885e0619dcc66cac31798b6cc3b514f48f31a26e93`. The canonical leader contact sheet and a native 156x210 vanilla leader reference were inspected. The small vanilla Ivanis DDS was decoded and visually inspected at native size.

Project collision searches found no matching subject token in `common/characters/`, `history/countries/`, `interface/`, `gfx/`, or `localisation/`, no custom sprite collision, and no target DDS. Existing shared-registry content was left untouched.

The three web candidates were inspected at their available source dimensions. The direct one-person portrait is a recognizable, well-framed photograph; the 1920 group source identifies Ivanis by seat number but a temporary crop contained neighboring figures and did not pass framing review; the 1942 licensed group does not let the subject be assigned unambiguously. These were source-level reviews only, not approved portrait candidates.

The portrait source crop extractor and `convert_to_dds.py` were not run because no source passed the rights gate. Crop JSON/equality evidence, processed-PNG native-size review, DDS round-trip, portrait GFX validation, independent crop review, engine rendering, and user live-game validation were consequently skipped. No code tests were run. The `web.run` search endpoint did not return within repeated attempts; direct Commons API/file records, Brave Search result pages, the Encyclopedia of Ukraine, and the RIA 1914 profile were consulted instead.

## Required follow-up

Production can resume when an exact-person image has an explicit reuse license/permission or a primary archive/catalog record identifies the photographer or collection and supports the applicable public-domain term. If the 1942 CC BY-SA 4.0 group photograph is proposed, a reliable person-level caption or record must identify Ivanis and locate him in that image. Until then, keep the package portrait blocked and do not add the sprite or runtime DDS.

No commit was made because the accepted portrait package remains blocked by missing source-rights evidence.

## Independent current-state recheck

The portrait subagent re-fetched the standalone Commons original and confirmed its 343x458 dimensions, 38,551-byte size, and SHA-256 `ACC3E81BA099FA0C96A69A9896D3139CAC2F0E7F3A8A9B21DE62663061DC1B23`; its identity is corroborated by the Ukrainian biography's use of the exact file, but its unknown date and unsupported `PD-Ukraine` publication condition still fail the rights gate. The Encyclopedia of Ukraine pages identify Ivanis but state that the Canadian Institute of Ukrainian Studies reserves all rights.

The direct 1920 group original was re-fetched at 1022x794, 280,948 bytes, SHA-256 `5BE0C69AD374D6CBC0F9E4A45BAC14022C23FB0BCF63C4612BBF054DD9E81B6F`; the Commons record still has an unknown photographer, a LiveJournal root as source, and no substantiated reuse basis. The installed character/GFX ownership scan and the 65x67 RGBA small-portrait decode were repeated, and the canonical leader contact sheet, one native 156x210 reference, and the small Ivanis card were visually inspected. This adds no source clearance and changes no production state: no original was archived, no crop/PNG/DDS or `.gfx` entry was created, and the package remains blocked pending an exact-person licensed source or primary archival rights evidence.

## Additional archive/catalog checks

At the user's request, I checked the direct Internet Encyclopedia of Ukraine portrait page; it identifies Ivanys but supplies no image-level license, photographer, archive, or date, and its footer says all rights are reserved by the Internet Encyclopedia of Ukraine. The Commons record for the 1942 Senate group explicitly lists CC BY-SA 4.0, but its caption names only the group and its Commons subject category does not identify Ivanys within the photograph.

The exact queries and outcomes are recorded in the linked source research file. They include Commons category `Vasyl Ivanys`, Openverse `Vasyl Ivanys`, Internet Archive `title:(Ivanis) OR creator:(Ivanis)`, the Ukrainian and English book-title/author queries for S. Narizhnyi, Open Library `Naryzhny Ukrainian emigration 1942`, Google Books `"Українська еміграція" Наріжний`, and Library of Congress Books `Naryzhny Ukrainian emigration 1942`. The archive and Open Library searches found no matching book record, Google Books returned HTTP 429, and the Library of Congress endpoint returned a Cloudflare challenge; none supplied the missing source identification or rights evidence.

The source gate therefore remains blocked. No image, crop, placeholder, DDS, or portrait sprite was added, and no source bytes were copied into the repository.
