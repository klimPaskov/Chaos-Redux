# Parliament of Fear
## Part 10. Visual assets and the severe-outcome super-event

### Art direction

The visual language centers on political institutions and the records they produce: chamber seating, council tables, marked files, hearings, office doors, appointment papers, and absent officials. It uses the game's period-appropriate painted and photographic asset families. Generic generated scenes must not accidentally claim to document a named historical purge or a real person's arrest.

Political identities come from the actual country. Generic art avoids national insignia that would make it inaccurate for most targets. Country-specific variants require verified references and a clear consumer. The base set should work across governments without an unnecessary separate painting for every tag.

### Report and news families

Country reports use the native 210 by 176 canvas. News images use a separate 397 by 153 monochrome composition. A report image must not be stretched into a news image. Similar subjects can share a researched or generated source, but each family receives a separate crop and composition suitable for its consumer.

| Asset role | Composition direction | Primary consumers |
|---|---|---|
| Opening chamber | An occupied chamber or council room with a small documentary disturbance | Opening and early political reports |
| Inquiry | Files and a formal investigative setting, with visible but unreadable records | Standard inquiry and preliminary review |
| Protection | A protected officeholder or institutional position implied through a guarded hearing or retained place | Provisional guarantee and contested protection |
| Removal | An empty place, withdrawn appointment, or sealed office | Targeted removal and vacancy consequences |
| Appointments | Administrative selection and a partly restored council | Appointment queue and chamber restoration |
| Contradictory evidence | Two incompatible documentary records with a plausible provenance problem | Forgery and rival-inquiry cases |
| Military inquiry | Period staff work or a command setting under investigation | Evolution I military cases and Generalissimo connection |
| Institutional disruption | A disrupted administrative or specialist workplace | Research, industry, intelligence, or civil-service impairment |
| Prepared conspiracy | A restrained depiction of secret coordination, without declaring guilt for a real person | Organization and prepared-plot reports |
| Recovery | A functioning but visibly changed institution | Stable settlement and post-purge recovery |
| Political crisis news | A public institutional exterior or neutral press scene | Major public deadlock or internationally relevant crisis |
| Purge aftermath news | A markedly depleted institution, without spectacle or invented victim photography | Material Great Purge news |

No report image includes baked player-facing text. Documents may carry non-readable period marks, but a generated quote or name must not be treated as evidence.

### Interface asset family

The chamber needs native seat silhouettes, empty and suspended states, evidence overlays, selected and hover states, protection markers, and a restrained warning animation. The interface frame and background must match the approved in-game reference composition.

Seat state art is separated into a support base, occupancy state, and evidence overlay. This allows the GUI to display an accused supporter correctly. A single combined texture per imagined political combination would make the state system harder to maintain and would risk missing combinations.

The precise seat-cell dimensions and panel canvas are established from the native reference and host category. They are deliberately not guessed from a web screenshot. The asset manifest marks these dimensions as reference-gated until the layout is measured.

### Icons

The four action families each receive a dedicated decision icon at the native decision family size. Secondary modes can reuse the parent icon with native selection text where appropriate. Distinct case indicators must remain legible at their actual display size.

The three consolidated national-spirit surfaces receive separate idea-family icons. Their appearance distinguishes administrative pressure, institutional damage, and settlement aftermath. A small government symbol or institutional motif is preferable to a crowded collage of faces and documents.

Achievement icons use 64 by 64 native art. Each has a single readable subject and a specific mechanical meaning. The normal, grey, and not-eligible variants are derived through the existing achievement pipeline. They are not three independently generated pictures.

### Portraits

Existing valid character portraits are reused. A new portrait is produced only when a real identified figure is required and no suitable existing asset is available. The person, historical role, and reference likeness must be sourced before production.

Leader and adviser portraits use their separate native families, including 156 by 210 leader portraits and 65 by 67 adviser portraits where appropriate to the actual consumer. A portrait cannot be stretched between those roles without a proper family-specific preparation.

Abstract seats use institutional symbols. The package does not request fictional faces presented as historical ministers or scientists. A disappeared character's portrait can be marked unavailable by the GUI, but the underlying art is not replaced with an invented corpse or unrelated person.

### Warning animation

The required animation is a short documentary accusation or removal warning, with authored changes across real frames. It must have a legible static terminal state. The approved sequence should be restrained enough to remain useful during several concurrent country crises.

The manifest records frame count, native frame canvas, sheet arrangement, playback behavior, static fallback, and actual GUI consumer after the reference map is approved. Review includes a native-size frame contact sheet and a preview animation. The preview format is not the runtime deliverable.

### Severe-outcome super-event

A super-event is reserved for a Great Purge that has become a substantial campaign event. Eligibility requires a major or player-controlled affected country, actual multi-group removals, and material impairment extending beyond one isolated office. The first minimum is a committed Great Purge wave with serious lasting consequences. A later wave can satisfy the broader threshold if the first did not.

The threshold should consider the actual breadth of affected institutions and political influence, not a mandatory count of historical deaths. A representative design anchor is at least 20 influence seats removed or made nonfunctional during the purge, plus two materially impaired institutions. A smaller country does not produce a super-event merely because one important character was dismissed.

The event plays once per crisis instance through the shared super-event system. It follows the established audio, observer, queue, and settings behavior. A delayed display checks that the referenced country and aftermath still make sense. It does not replay because a user changes observer country or reloads the save.

### Super-event text and image direction

The viewpoint is a public historical-style account of an administration consuming its own institutions. It identifies the affected country, the governing institution, the breadth of the purge, and what remains uncertain. It does not claim a particular real-world atrocity has happened in a different country.

The 457 by 328 image emphasizes an emptied or disrupted seat of authority and the administrative record of removal. A grounded country-specific setting can be used when sourced. A neutral institution is appropriate for dynamic targets. The composition must remain readable under the native overlay.

No final title, quotation, button, cultural remark, or musical choice is supplied here. The text and audio research roles must verify any quotation's wording, speaker, date, context, and suitability. A quotation that is only popularly attributed is not accepted. A source found after a decision has been made does not justify a fabricated earlier attribution.

### Audio direction and rights

The audio should support institutional dread and political consequence without celebratory treatment of persecution. It needs a verified recording, a clear excerpt, and separate rights checks for the composition and recording. The intended excerpt normally falls within the shared 60 to 120 second range, with exact timing determined by the selected source.

The research must confirm that the music is not already assigned to another Chaos Redux super-event. A low-quality placeholder, an invented track title, or a few warning tones do not satisfy the asset requirement. The production handoff remains blocked until the final audio and text sources have been checked.

### Asset acceptance

Every asset has an actual consumer, correct native family, source or generation record, final filename, and review evidence. Opaque reports fill the native canvas. Icons preserve the required transparency. Runtime files do not point into documentation folders.

DDS files must be decoded and checked after conversion. Achievement variants follow their dedicated processor and exact overlay templates. The full manifest and the asset prompt define the production handoff. This planning package contains briefs and requirements, not finished raster art or audio.
