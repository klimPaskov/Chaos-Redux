# Super-event research prompt for Event 028: Asteroid Incoming

Use `chaos-redux-super-events`, `chaos-redux-event-assets`, the Event 028 specification pack, and the project web-research rules. Spawn the text and audio research workers with `fork_context=false` when the project subagent route is available. Do not edit event, localisation, GFX, GUI, sound-definition, or spreadsheet files during the research pass.

## Super-event role

The package marks the first global reveal after the main asteroid impact transaction has completed. The main target state is already destroyed, neighboring countries have suffered damage, fragments may have struck elsewhere, and atmospheric dust is beginning. The super-event identifies the locked target country and broad region dynamically.

The miss outcome uses global news and does not use this super-event package.

## Text research

Return several sourced candidates and one recommendation for each surface.

### Title direction

Find a short, specific title direction tied to impact, falling stone, the target region, or the loss of the sky. Avoid generic apocalypse titles. The final title must work with dynamic target context and should not name a fixed country.

### Description direction

Write a concise final description only after research. It should identify the main target and region, state that surrounding territory has been damaged, mention worldwide fragments when active, and note developing atmospheric effects. It should not list exact raw percentages or every country.

### Button remark

Research five or more brief reaction candidates. Suitable directions include scientific understatement, a period phrase about falling stars, a short cultural allusion, or grim administrative acceptance. Mass civilian death rules out cheap comedy.

For each candidate record exact wording, source work, creator, year when known, source link, quotation status, copyright risk, and why it fits. Keep modern copyrighted fragments very short.

### Main quote

Research at least eight verified candidates from historical speeches, public-domain literature, scripture, philosophy, scientific writing, mythology, or other traceable sources. Themes can include falling bodies, human attempts to control nature, consequences, dust, pride, chance, or irreversible action.

Do not invent or misattribute a quote. Prefer a primary source. Record exact wording, author or speaker, source work, date, source link, public-domain or rights status, attribution confidence, and fit. Recommend one short quote that fits the UI.

## Image alignment

Review the generated-image brief for `super_event_028_asteroid_impact`. Confirm that the selected title, description, remark, and quote describe the same moment as a distant period documentary view of the main impact. Flag any mismatch before wiring.

The image itself belongs to the generated event-art worker.

## Audio research

Research at least five legitimate musical candidates and recommend one.

The track should:

- Fit a scientific disaster and global impact
- Use solemn orchestral, choral, period, liturgical, or restrained modern-classical character where rights allow
- Be a real musical recording
- Be suitable for a final in-game cut of about one to two minutes
- Be unique to Event 028 unless the user explicitly approves reuse

Reject unclear licensing, commercial recordings without permission, trailer libraries without clear terms, YouTube-only provenance, drones, test tones, noise beds, explosion sounds, oscillator layers, and placeholder cues.

For every candidate record:

- Title
- Composer or creator
- Performer or recording source
- Source page and direct download source when distinct
- Composition rights
- Recording rights
- License and usage terms
- Attribution requirement
- Original duration
- Proposed edit and final duration
- Fit and pacing notes
- Suitability status

For the selected cue, preserve the original download, create the game-ready WAV, record transformations and checksums, and return the proposed final path under `sound/028_asteroid_incoming/`.

## Handoff

Write or update `docs/super_events/028_asteroid_incoming_super_event_research.md` with all candidates, the selected quote, selected remark, selected track, source and rights evidence, image direction, uncertainties, and implementation identifiers proposed by the parent.

Return blocked status when no defensible quote, remark, image alignment, or licensed musical recording can be completed. Do not substitute default audio or invented text.
