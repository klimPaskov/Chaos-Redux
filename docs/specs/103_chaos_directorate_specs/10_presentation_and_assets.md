# 10. Presentation and asset direction

Every label except the three user-supplied names is a design working label. Final public writing follows the research and consumer review described here.

## Cohesive fictional identity

### Identity premise

The Directorate is an invented military institution that has acquired the world's accumulated means of destruction. Its visual identity should convey organized appropriation, unrelenting industrial scale, and a disturbing common command over visibly incompatible forces.

Use a single institutional emblem built around a heavy, irregular industrial seal with layered engraved plates and an empty central aperture. The design should have enough authored heraldic detail to remain distinctive at normal flag size while preserving a strong outer silhouette at small size. This is a direction for original art. It is not an instruction to manufacture the final emblem from local circles, rectangles, or a traced existing symbol.

The preferred palette is charcoal, aged ivory, restrained oxidized brass, and a small dark-red accent. Palette choices remain subordinate to the inspected HOI4 surface family. The emblem may recur as a motif, but each focus, spirit, decision, and achievement icon receives its own source art and consumer-specific composition. Do not repaint the entire inherited arsenal into this palette. Existing unit counters retain their verified owner art and native green conventions.

The public identity has no test-state jokes, console terminology, debug labels, carrier acronym, implementation history, or implication that the country has just been assembled by a developer. The visible country should appear operational at the instant the committed arrival is announced.

### Institutional authority portrait

Use one fictional institutional authority with an institutional name. The portrait is a people-free composition at full country-leader dimensions. It may show the Directorate emblem in a strongly lit command alcove with a silent speaking grille and a folded service banner. It must read as the country's governing authority rather than as a map, a generic office photograph, or a substitute individual face.

`chaosx_portrait_creator` owns this asset even though no person appears. The source classification is fictional institutional high-chaos identity. Do not invent a historical official, attach a real person's name, imply archival provenance, add an anonymous human council without an accepted group brief, or create a personal name pool. Part 06 also specifies no new advisor roster or bespoke individual commanders.

The authority remains static. Animation is not required to make it a major identity asset. A later accepted animation must be an explicit presentation requirement with real source frames, a static fallback, a verified portrait or overlay consumer, and a stated purpose.

### Visible mixed arsenal

The distinctive military presentation comes primarily from the units, equipment, models, counters, and operations that the Directorate actually fields. Preserve the inherited visual differences between those families. Mixed formations in native army, equipment, battle, production, and intelligence views should make the breadth apparent without creating another currency or an encyclopedic dashboard.

Arrival and terminal artwork may feature a few readable conventional, organic, and mechanical silhouettes selected from the verified installed arsenal. This is scene composition, not a curated gameplay roster. Later art briefs must identify their actual source families so an image does not advertise a nonexistent unit. New registry entries inherit their own established art through the owner package. Their absence from a static news composition does not remove their gameplay access.

Narrative messages may refer to an actually deployed or observed capability when its identity is known. They must not claim that an unlocked technology has already been produced, that a project has succeeded merely because it is available, or that an unobserved enemy formation has been precisely identified.

## Required asset-surface matrix

All paths below are proposed path families. Implementation must bind final basenames and sprites after checking current identifiers. No placeholder token is a reserved runtime ID. The canonical current reference root is `.claude/skills/chaos-redux-event-assets/assets/gfx_references/`. Every stated default still requires the exact active consumer check before production.

| Row | Required surface and coverage | Native delivery or exact sizing rule | Reference family | Ownership and boundary |
| --- | --- | --- | --- | --- |
| P01 | Directorate country flag identity, no-suffix base and all four ideology lookup variants | Normal 82x52, medium 41x26, small 10x7 TGA, 15 files for one active identity token | `flags/normal/`, `flags/medium/`, `flags/small/`, combined flag contact sheet | Generated flat master through the asset route. Parent owns cosmetic or country binding. All five lookup names intentionally use the same institutional design because there are no ideology routes. Record that deliberate sharing. |
| P02 | Institutional country authority portrait | One 156x210 PNG and final DDS, opaque consumer background | `portraits/leaders/`, then reference-only portrait backdrops if useful | `chaosx_portrait_creator`, including portrait-specific GFX and existing portrait reference wiring. No small portrait or individual identity is inferred. |
| P03 | Focus icons across eight accepted path families | One independent source and final nominal 94x86 DDS per visible focus node, with actual canvas verified | `icons/national_focus/`, optional reference-only focus pieces and backgrounds | `chaosx_icon_artist`. The implementation owner expands this into one requirement row per actual node. Eight path families are not eight interchangeable finished icons. |
| P04 | Three institution spirit slots | Three independent 64x64 base icon designs, plus a separate accepted phase design only when the visible identity changes | `icons/ideas/`, cataloged national-spirit background templates where suitable | `chaosx_icon_artist`. Slots are command institution, war economy institution, and absorption institution. Replacing a stage never creates a fourth simultaneous tree-owned spirit. |
| P05 | Directorate native decision category icon | Nominal 32x32, exact category consumer governs | `icons/decision_categories/` | `chaosx_icon_artist`. Keep distinct from the flag, spirit icon, and focus art. |
| P06 | Resistance native decision category icon | Nominal 32x32, exact category consumer governs | `icons/decision_categories/` | `chaosx_icon_artist`. Its motif should imply organized local resistance without inventing a universal anti-Directorate faction. |
| P07 | Directorate action icons | Independent 32x32 semantic designs for front logistics, campaign concentration, production priority, reconstruction, overseas staging, special-operation coordination, terminal redeployment, and final sweep | `icons/decisions/` and `icons/missions/` for actual timed missions | Eight working action families. Repeated targets may share the same action-family icon intentionally. The final decision map determines any extra semantically distinct row. |
| P08 | Resistance action icons | Independent 32x32 semantic designs for defence objectives, industrial evacuation, local asset denial, reconnaissance, counterattack, aid convoys, and capability-specific protection | `icons/decisions/` and `icons/missions/` for actual timed missions | Seven working action families. Protection variants may use an existing verified owner icon when the exact same operation is exposed. No resized focus substitutes. |
| P09 | Existing owner-operated capabilities and arsenal surfaces | Reuse each owner's actual canvas, frames, names, alpha and consumer | Exact technology, project, equipment, unit, raid, operation, or facility family | Owner packages supply valid references. A missing alias or consumer is a required integration gap, not permission to use a generic Directorate placeholder. |
| P10 | Arrival news photograph | One 397x153 black-and-white final DDS | `event_art/news/` | `chaosx_generated_event_art`. Show abrupt organized armed occupation with recognizable mixed forces and the new flag. No super-event treatment at arrival. |
| P11 | Confirmed Directorate defeat news photograph | One 397x153 black-and-white final DDS | `event_art/news/` | `chaosx_generated_event_art`. Show the broken military institution and the cost of survival. One scene may support phase-aware pre-terminal and post-terminal descriptions if the final review confirms both uses. |
| P12 | Chaos Always Wins terminal scene | One 457x328 final DDS, actual super-event consumer background | `event_art/super_event/` | `chaosx_generated_event_art`. Single terminal scene contract below. No title card, symbolic chart, or flattened interface. |
| P13 | Eight achievement subjects and state triplets | Eight original 64x64 subjects, each with completed, grey and not-eligible runtime DDS states, 24 final DDS files | `icons/achievements/` and immutable `template/` inputs | `chaosx_icon_artist`. Use the exact achievement processor and root-only runtime placement. The icon concept belongs to its achievement rather than to an existing focus. |
| P14 | Compact objective display and exact-state navigation | Reuse verified native text, country-flag, state-target and map-navigation consumers. No invented universal texture size | Exact active decision-category and native state-navigation references | Parent and `chaosx_event_ui_worker` own the source and context checks. A new painted background, meter frame, category picture, tab set, or decorative control is not required. |
| P15 | One terminal musical cue for Chaos Always Wins | Final 60 to 120 second WAV matching the verified super-event sound consumer, with unique audio registration | Named existing audio catalog, exact sound helper and source licensing record | `chaosx_super_event_audio_researcher` researches and delivers the final file. Parent accepts, places, registers and wires it. No recording is selected here. |

The focus path art directions correspond to command establishment, war economy, absorption and reconstruction, combined arsenal coordination, continental campaign, logistics and ocean reach, victory adaptation, and global conquest. Use scene-specific subjects such as command equipment, worked industrial machinery, repaired infrastructure, incompatible military components under a common standard, difficult terrain, functional transport, captured materiel, and sustained expeditionary reach. These are prompt directions, not final focus titles or new gameplay effects.

P01 requires review of every active country and cosmetic identity lookup so no missing suffix falls back to dormant carrier art. Preserve the dormant carrier's unrelated use outside the active event. One master may produce all three flag sizes and the deliberately identical ideology lookup variants. Each visually distinct future route flag would require its own generated design. Check the TGA origin against installed vanilla rather than fixing an inverted flag through GUI workarounds.

No dedicated faction emblem is required because this design does not create a new faction. No new custom unit family, counter family, model, commander portrait, advisor card, report-image series, or animation quota follows from universal arsenal access. Those become requirements only through an explicit accepted gap or added surface.

### Production and row-level acceptance

For every actual asset row, later production must retain the exact request, source mode, reference paths, immutable source art, processed PNG, selected candidate identity, native-size review, final delivered bytes, proposed runtime registration, live consumer, visibility state, and parent verdict. Exact runtime row coverage is separate from file and alias counts.

Final 2D DDS files follow the current strict one-level BGRA contract. Flags use the exact TGA lookup layout. Achievements use the supplied immutable backgrounds and overlay, the single original subject and deterministic state derivation, and the dedicated achievement triplet processor. All 24 achievement DDS files belong directly under `gfx/achievements/` using the final registered achievement IDs. The general planning source's looser wording about later achievement variants does not weaken the current asset skill's complete triplet requirement.

Event-scoped art belongs under the accepted engine-facing category and `103_chaos_directorate/`, except engine-required flag and achievement roots. Runtime files never reference `docs/assets/`. Active production evidence remains in the temporary event workspace until review and integration are complete, then durable provenance and crosswalk facts are promoted before cleanup. The separate durable portrait archive is protected by its own source contract.

## Compact objective display and native actions

### Exactly two public measures

The Directorate-specific interface may expose at most these two measurements:

1. Live controlled origin-continent states relative to the exact required state set.
2. Current operational capacity relative to the Part 03 planned force requirement.

A phase heading, current target, action cost, mission due date, native war status, or settings explanation is not a new currency. Do not add harvested population points, stolen technology points, a conquest budget, a boss level, an arsenal completion meter, another threat score, or a visible probability countdown. Shared Chaos and World Threat remain on their existing shared surfaces.

Use the same compact display contract in the Directorate context and the resistance or observer context. The origin-state set comes from the same canonical geometry definition as the terminal predicate. Disconnected islands remain part of that set. Current control is recomputed from live eligible states, so losing a state immediately removes it from completion. Historical continental success must never replace the live display.

The Directorate player may see the exact operational-capacity ratio if ordinary supported player control is verified. Other countries must receive only the precision their verified intelligence context permits. If the native context does not authorize an exact enemy ratio, omit that number and give a qualitative observed condition or the applicable native intelligence result. The limiting component named in the tooltip and its supply node appear only to a country holding a live Reconnaissance receipt from Part 07. Do not fill the field with a made-up estimate or build an intelligence meter. The implementation must demonstrate which source provides every displayed observation.

### Native decision presentation

Keep ordinary scoped decision categories and a small set of currently relevant actions. The category description supplies the compact objective and the next useful instruction. Native decision rows supply costs, availability, targets, time limits, and visible results. Earlier phase actions disappear or are replaced when terminal redeployment and final sweep become relevant.

Exact-state navigation is justified because a single offshore state can prevent first-continent completion. The preferred solution is the existing native state-target list and map focus behavior, with clear remaining-state names and a distinction between current control and historical control. Reuse the same state set in the display, native targets, and terminal check.

If verified native consumers cannot identify all outstanding states clearly, the parent may implement one compact read-only exact-state view within this same objective surface. It must be shared by context, use exact installed state geometry and one projection, and provide native labels and map navigation. It must not become a new multi-tab window or a second objective dashboard. No category picture accompanies such an interactive extension. The baseline plan does not require a painted map or image-generated borders.

The objective does not become a new global conquest percentage after terminal activation. The origin-continent ratio remains truthful, operational capacity keeps its established definition, and native fronts, wars and current targets communicate worldwide expansion. The terminal history remains visible as a phase fact even if live origin control later falls.

### Context and accessibility checks

Required future comparisons include a dormant event, committed automatic arrival, low-Chaos manual arrival, a bordering defender, an outside observer, an explicitly enrolled boss player, the last disconnected origin state, complete geography with a blocked terminal gate, actual terminal activation, origin-state recapture after terminal, boss destruction, and save/load recovery.

Inspect at supported UI scales including 1080p. No clipped dynamic country or state names, raw localisation keys, debug text, duplicate active/completed messages, misleading empty rows, or wrong-country objective state may pass. Light-parchment description text stays plain. Native costs and actionable tooltips retain their consumer-supported formatting. Continent status needs a textual or shape distinction as well as colour.

Use the scripted GUI skill's inspect and render checks where available. If rendering is unavailable, review the same layout, states, resolutions and click regions from source and record the visual limitation. That limitation does not authorize a smaller interface.

## Public writing and observer-message direction

Write observed consequences directly. Use active soldiers, civilians, occupied industry, transport, unfamiliar formations, and changing control. Avoid administrative paperwork as the emotional center, vague ominous announcements, official-denial contrast formulas, staged diplomatic introductions, or prose explaining that this is a fallback algorithm.

Event Details and catalog-facing detail text describe the situation and premise. They do not list modifiers or mechanical rewards. Actions and tooltips accurately describe their visible costs, targets, and consequences. They do not advertise achievement routes. All final wording is deferred to implementation.

| Situation | Audience and surface | Information direction | Delivery rule |
| --- | --- | --- | --- |
| Automatic grace or increasing pool weight | Existing shared Chaos surfaces only | No new countdown, weight disclosure, Directorate preview, or early ending spoiler | No Event 103 public delivery before a committed arrival |
| Successful arrival | One global news event and the event log, plus normal local war notifications | The country's public name, actual seized state, immediate organized occupation, and visible armed force. Former controller and neighbors receive the consequences of wars that already exist | Deliver only after setup commits. Provisional setup and rollback remain silent |
| First local war or newly acquired border | Affected country through native war and relevant decision surfaces | Actual front, threatened population or infrastructure, and current available responses | Do not repeat a global popup for every new border |
| New observed special capability | Countries with valid observation and the relevant native intelligence or operation result | What was actually deployed or suffered, with uncertainty where identification is incomplete | One receipt-bound result. Availability, registration, and failed operations do not produce success prose |
| Continental resistance becomes extremely narrow | Exposed countries and the event log | Remaining defended territory and practical current routes for defence, evacuation, or counterattack | At most one episode milestone notice from the accepted control measure. Recapture oscillation does not replay it |
| All origin states currently controlled but terminal gates are unsatisfied | Current objective and event log | Geographic control is complete. No statement that a world-end has begun | No terminal sound, super-event, or irreversible text until the terminal commit |
| Chaos Always Wins commits | Every eligible human audience through the established super-event system | A continent has been consumed and the Directorate is now carrying its accumulated strength into worldwide war. Remaining countries still physically exist and can fight | One terminal super-event and one durable event-log entry, with settings-aware sound |
| Directorate destroyed before its ending | Global defeat news and event log | The military institution has been broken at great cost. Existing Chaos remains a separate world condition | Requires confirmed destruction and zero controlled territory. Capitulation alone produces no defeat claim |
| Directorate destroyed after Chaos Always Wins | The same defeat-news surface with phase-aware text and event log | The military force was defeated after the terminal order began. Do not claim that history or the global ending flag was undone | One destruction receipt. Preserve the terminal history |
| Actual world conquest | Native outcome or victory surface and event log | No independent sovereign remains outside Directorate control under the Part 09 completion predicate | No second super-event and no premature declaration based only on wars or capitulations |

The first-continent objective must be understandable once the military campaign is public. Its future hidden presentation and achievement routes should not be narrated in ordinary event prose. The implementation's visible action requirements remain accurate even when flavour withholds future spectacle.

## Single terminal super-event

### Role and trigger boundary

The only Event 103 super-event is **Chaos Always Wins**. Arrival uses news because the country is an immediate military crisis with an uncertain eventual outcome. Reserving the larger presentation for successful continental consumption makes that later threshold distinct.

The trigger is the committed terminal transaction in Part 09: live complete origin-continent control, strictly above 1000 Chaos, this branch enabled, global world ends enabled, and no prior world-end. The manual scenario bypasses none of these gates. Presentation consumes the successful terminal receipt and never creates the ending by itself.

The implementation owner handles slot and audio-ID reservation, visibility, `.t`, `.d`, `.a`, `.q`, all scripted-localisation getters including `GetSuperEventImage`, final image GFX, sound definitions, settings-volume wrappers, the playback helper, event log, and permanent documentation. All identifiers remain unreserved in this specification.

### Image direction

Compose a period-documentary scene of the Directorate's mixed army moving through an occupied continental port toward a wider campaign. A readable institutional flag and disciplined mass movement establish a single owner. Conventional transport and visibly different verified mod formations establish the accumulated arsenal. Captured industrial capacity and working embarkation infrastructure communicate that the conquest has supplied the next offensive.

Keep the foreground legible at 457x328. Use a few distinct silhouettes and a coherent perspective rather than a crowded catalogue of every unit. Preserve 1936 to 1945 documentary visual language around any explicitly intended unusual mod technology. Do not introduce modern electronics or futuristic staging merely to make the image more spectacular. Do not show a map already painted as total world conquest, fabricated legible placards, titles, a boardroom, a still-life emblem, or a UI composition.

The image is generated fictional scene art with retained source and prompt lineage. It is not presented as a historical photograph or as a screenshot of a built model. The source families shown must be checked against actual installed visual assets before the final art brief is accepted.

### Text research direction

The title is fixed by the user. Description direction is finality about the failed containment of a continent, followed by the visible continuation of war. It should not state that every remaining country has surrendered or that a later military defeat is mechanically impossible.

The main quote research should compare short primary-source passages on the failure of containment, instruments turning on their makers, systems of domination, or the endurance of destructive order. Prefer sources with traceable editions and rights. Reject quotations that merely announce inevitable literal extinction, because the game continues and the Directorate can still be destroyed.

The acknowledgement direction is a brief cold, grim, or bitter reaction to this exact moment. A researched allusion is acceptable only when its wording, context, and rights are verified. No proposed final quote, acknowledgement, lyric fragment, music title, or fabricated attribution appears in this specification.

Future `chaosx_super_event_text_researcher` output must compare several main-quote and acknowledgement candidates, identify exact primary sources, verify wording and attribution, record translation or edition where relevant, assess fit and quotation limits, and recommend a complete pair with backups. The parent chooses and writes the final localisation. A missing quote remains research pending and cannot be replaced by invented historic-sounding text.

### Audio research direction

Seek one intentional musical recording with heavy ordered momentum and a strong sense of expansion. Low orchestral weight, restrained brass, a measured march structure, or a musically coherent choral passage may fit. The cue should develop over its duration rather than become a one-shot effect, drone, noise bed, or synthesized pulse.

First inspect the named existing audio catalog and provenance to establish uniqueness and whether an unused approved recording fits. Reuse of a track already assigned to another super-event requires explicit approval for that exact reuse. Otherwise research official archives, publishers, performers, or other primary licensing sources. Composition and recording rights must be checked separately under the source contract.

Target 60 to 120 seconds for the final cue. The current super-event skill requires a documented exception outside its preferred range and a final file no longer than two minutes without explicit longer-track approval. The current audio TOML's looser usual one-to-three-minute preference does not override that more specific final-delivery rule.

`chaosx_super_event_audio_researcher` must deliver the actual final game-ready WAV, the immutable downloaded source, title and creator metadata, performer or recording source, primary source and rights URLs, license and attribution record, original and final durations, conversion recipe, hashes, audition notes, and a wiring handoff. The parent accepts and places the WAV and adds a unique base sound, required volume wrappers, a unique audio ID, `global.current_super_event_audio_id`, and `play_current_super_event_sound = yes` under the verified existing contract.

Update `music/chaosx_music_track_list.html` and permanent super-event research documentation with the real source identity and exact super-event use. No final cue is selected here. Lack of usable researched music is an implementation blocker, not permission for test tones, a generic default, unsupported reuse, or false provenance.

## Conditional 3D and audio integration gaps

Universal use of existing content does not authorize a new Directorate unit family or a broad model remake. Audit and reuse the current actual family consumers first. A missing model, material, counter, or firing-state sound is a specific owner integration gap. The implementation owner must decide the required bounded repair without treating it as completed by this plan.

If a new or rebuilt model is genuinely required later, follow the [3D pipeline skill](../../../.claude/skills/chaos-redux-3d-model-pipeline/SKILL.md) through its specialist owner, which defines the body-rig, action, texture, counter and audio requirements. The later job must inspect the current owner rules, recorded attempt lineage and exact consumer before production.

Selection audio needs special care for a country that mixes many families. The supplied 3D source states that infantry selection voices route through country or original-tag identifiers such as the country infantry idle consumer, not through each subunit sprite. Existing entity-state effects may still reach their properly bound family consumers, but those are not proof of selection playback.

The design intent is one coherent Directorate country-level selection voice treatment if a matching verified consumer and legally sourced recording can be supplied, while preserving family-specific movement, weapon, impact and other verified entity effects. Do not promise a separate zombie, machine, clone, and conventional-infantry selection voice within the same tag unless a real engine route is proven. Do not replace another country's voice or impersonate an original package host to obtain its sound. A missing acceptable country-level selection source or binding remains an audio gap, not a reason to synthesize a voice or relabel idle entry as selection.

No voice file, recording, quote, model, counter, or other runtime asset has been produced in this specification.

