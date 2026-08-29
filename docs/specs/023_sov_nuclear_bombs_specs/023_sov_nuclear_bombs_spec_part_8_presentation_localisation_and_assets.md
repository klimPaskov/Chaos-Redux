# Event 023 specification, Part 8: Presentation, localisation, and assets

## Presentation goal

Event 23 needs strong identity and clear control without a full custom mechanic window.

The primary surface is one ordinary decision category with:

- One static decision-category picture.
- One category icon.
- A concise dynamic header.
- Phased decisions and missions.
- Target selection through the standard selected-target pattern.
- Report and news events for important changes.
- One nonterminal super-event for the first multi-major exchange.

The presentation should make the arsenal feel secret, heavy, guarded, and difficult to command. It should not resemble a shop, a debug panel, or a modern launch simulator.

## Visible information budget

The category should show four pieces of information at most:

1. Operational Soviet bombs.
2. Arsenal Readiness.
3. Command Integrity.
4. Current posture and public knowledge as one compact status line.

Detailed component values remain in tooltips.

The player should be able to answer:

- How many usable bombs remain.
- Whether the arsenal can be delivered.
- Whether the command chain can authorize and account for use.
- Whether the arsenal is hidden, demonstrated, coercive, retaliatory, unrestrained, broken, or under moratorium.

Do not show exposure, credibility, reactor entitlement, storage risk, foreign evidence, and exchange stage as separate permanent numbers. Use short status labels, mission text, and contextual tooltips.

## Decision category phases

### Hidden project phase

Visible emphasis:

- Arsenal count.
- Readiness and Integrity.
- Custody doctrine.
- Storage, production, delivery preparation, and testing.

Targeting is absent except for a valid wartime emergency.

### Demonstrated deterrent phase

Visible emphasis:

- Public knowledge.
- Test aftermath.
- Foreign reactions.
- Deterrence and wartime warnings.

### Coercive doctrine phase

Visible emphasis:

- Selected target.
- Active demand.
- Credibility status.
- Response deadline.
- Preparation and settlement actions.

### Exchange phase

Visible emphasis:

- Active opposing nuclear actor.
- Confirmed strikes or launch warning.
- Retaliation deadline.
- Hotline, stand-down, limited response, and authorization.

### Collapse custody phase

This is a filtered overlay state within the same event-owned category or a closely linked event-owned category if current decision constraints require separation.

Visible emphasis:

- Selected disputed site or breakaway.
- Accounted devices.
- Custody state.
- Recovery, negotiation, disablement, and settlement actions.

The ordinary category should hide actions unrelated to the current crisis.

## Decision-category picture

Working asset name: `sov_nuclear_command_category_picture`.

Source mode: generated period-authentic documentary scene.

Visual direction:

- A guarded Soviet nuclear assembly or storage interior.
- 1930s to 1940s industrial construction, uniforms, instruments, cables, cranes, and heavy steel.
- Scientists and military officers working around a weapon or sealed casing.
- The weapon should be present as a controlled industrial object, not a glowing science-fiction device.
- Strong depth and one clear central subject.
- Muted monochrome or restrained period color consistent with the current decision-category picture family.
- Enough open value contrast to remain readable behind normal category text and UI.

Avoid:

- Maps as the main subject.
- Painted buttons, meters, labels, numbers, or interface controls.
- Readable generated text.
- Modern computers, screens, weapons, protective equipment, or architecture.
- Mushroom clouds as the default category image.
- A heroic propaganda pose.
- Gore or visible victims.

The final runtime canvas must be derived from the active category picture sprite and GUI consumer. The skill reference family uses 114 by 101 examples, but that size is not assumed as the runtime requirement.

## Core icon families

Every icon family requires separate source art, processing, and DDS output for its own UI role.

### Decision category icon

Working sprite direction: a Soviet atomic device under a guarded star or sealed command emblem.

- Strong silhouette.
- Readable at category-button size.
- No text.
- Transparent or framed according to the verified category icon precedent.

### Primary national spirit icon family

The primary spirit can use a coordinated progression family.

Required working states:

- Secret Soviet Arsenal.
- Demonstrated Arsenal.
- Coercive Arsenal.
- Retaliatory Command.
- Unrestrained Release.
- Broken Chain.
- Atomic Moratorium.

The implementation can reduce this to fewer distinct runtime icons only if the accepted asset review proves that stage variation remains clear through localisation and the reuse is deliberate. A resized decision icon cannot satisfy the spirit family.

Visual motifs can progress through:

- Sealed casing and closed command chain.
- Test flash reflected on instruments.
- Targeting compass or command line.
- Dispersed command and retaliatory signal.
- Open release mechanism and fractured horizon.
- Broken seals, separated keys, or an empty cradle.
- Locked device under inspection or dismantlement tools.

### Decision icons

At minimum, separate icons are needed for these decision families:

- Arsenal accounting.
- Storage hardening.
- Reactor construction.
- Device assembly.
- Delivery crew preparation.
- Command exercise.
- Safety and authentication.
- Test-site survey.
- Concealed test.
- Public test.
- Counterintelligence response.
- Select target.
- Private signal.
- Public ultimatum.
- Wartime demonstration.
- Strike preparation.
- Final authorization.
- Hold or abort.
- Hotline and stand-down.
- Dismantlement or moratorium.
- Depot recall.
- Rail security.
- Joint custody.
- Recovery raid.
- Device disablement.

Several closely related decisions may share one icon when they occupy the same action family and remain visually clear. Unrelated decisions should not reuse a generic nuclear symbol.

### Mission icons

Mission art should distinguish:

- Test preparation.
- Target response deadline.
- Strike preparation.
- Retaliation window.
- Rail corridor security.
- Breakaway operationalization.
- Joint-custody transfer.
- Dismantlement inspection.

Mission icons should be authored as mission assets, not resized decision icons.

## Event and news art

### Opening event picture

Working direction:

- A closed Soviet laboratory or industrial chamber after successful assembly.
- Scientists, guards, and officials understand what has been completed.
- The weapon remains partly obscured.
- The image should support secrecy and physical scale.

Source mode: generated period-authentic documentary scene.

### Test report picture

Working direction:

- Instruments, protective observation, a distant flash, or a remote test tower.
- Show the test as an observed technical event.
- Avoid using a generic modern stock mushroom cloud.

Source mode: generated, unless a suitable period archival image is deliberately chosen and licensed.

### Accident report picture

Working direction:

- Damaged rail equipment, an evacuated compound, protective crews, or a sealed industrial accident site.
- No gore.
- The source image should communicate contamination and command failure.

Source mode: generated period documentary scene.

### Public-test news picture

Working direction:

- A clear distant Soviet test cloud or flash with period observers, aircraft, or press imagery.
- The composition should read at news-event size.

Source mode: generated or sourced archival material after rights and era review.

### Nuclear ultimatum news picture

Working direction:

- Civil-defense movement, embassy departure, guarded Soviet bombers, or a target capital preparing for a threat.
- The image should show consequences of the demand, not a map arrow.

Source mode: generated period documentary scene.

### First Soviet combat-use news picture

Working direction:

- A distant detonation and the immediate human or military environment.
- No celebratory framing.
- Avoid explicit bodies.
- The image should communicate blast scale and irreversible damage.

Source mode: generated period documentary scene.

### Breakaway custody news picture

Working direction:

- Local troops and technicians controlling a guarded depot or rail convoy.
- The device is physically present but the scene does not imply operational launch control.

Source mode: generated alternate-history documentary scene.

## Super-event image

Working asset direction: the first confirmed nuclear exchange among major powers.

The image should show several elements of an exchange without becoming a collage:

- A major city or military horizon under a nuclear flash.
- Communications and warning infrastructure failing or crowded in the foreground.
- Aircraft, searchlights, radio operators, or evacuation movement that place the event in the 1936 to 1945 visual world.
- One dominant composition and period documentary realism.

Avoid:

- Modern intercontinental missiles unless the campaign route and separate missile event justify them.
- Satellite views.
- Modern command screens.
- Readable generated text.
- Abstract diagrams.
- A clean title card.
- Reuse of the Fallout terminal image.

Source mode: generated high-chaos period documentary art.

## Super-event audio and text boundary

The super-event requires:

- A unique slot verified against the current registry.
- A unique licensed or public-domain musical track.
- A verified real quote.
- A researched short cultural remark or a plain severe reaction.
- Settings-aware playback.
- A final WAV under the event-scoped sound folder.
- Full source and license documentation.

The planning package defines direction only. It does not select final wording, quote, remark, or audio.

The audio should be a structured musical recording, likely severe orchestral, choral, liturgical, or period modernist music. Pure drones, generated sound, alarms, test tones, and sound-effect beds are forbidden.

## Achievement art

Every achievement requires a complete state triplet:

- Eligible or unlocked art.
- Grey state.
- Not-eligible state.

Working achievement IDs and visual directions appear in Part 10.

Achievement art should use the exact achievement canvas and overlay precedent. The not-eligible overlay is a workflow input, not a substitute for the base art.

## Assets explicitly absent

Event 23 does not require:

- Character portraits.
- Advisor portraits.
- New leaders.
- New flags.
- New country tags.
- Faction emblems.
- Custom unit counters.
- Equipment art.
- Custom 3D models.
- Skeletal animations.
- Frame-sheet UI animation.
- A focus-tree icon family.
- A full scripted-GUI panel.

These families should not be created during implementation unless a later accepted design explicitly adds a consumer.

## Source-mode rules

Generated non-icon art belongs to `chaosx_generated_event_art`.

Generated icons and achievement art belong to `chaosx_icon_artist`.

A real historical image, if selected for a report, news, or super-event asset, belongs to `chaosx_asset_source_researcher` and requires source, rights, era, and crop evidence.

No portrait worker is needed because the event creates no portrait consumer.

## Runtime placement direction

Final event-owned assets should use an event-scoped folder such as:

- `gfx/event_pictures/023_sov_nuclear_bombs/`
- `gfx/interface/ideas/023_sov_nuclear_bombs/`
- `gfx/interface/decisions/023_sov_nuclear_bombs/`
- `gfx/super_events/023_sov_nuclear_bombs/`
- `sound/023_sov_nuclear_bombs/`

Achievement DDS files remain in the root achievement folder and use the full achievement IDs.

Exact sprite names and paths must be locked before generation so the asset workers do not need to rename completed files.

## Localisation surfaces

Implementation needs finished player-facing text for:

- Opening event.
- Custody doctrine options.
- Doctrine reform report.
- Readiness and Integrity labels and tooltips.
- Posture states.
- National spirit forms.
- Decision category title and description.
- Every decision and mission.
- Test outcomes and incidents.
- Public-test news.
- Foreign reaction reports.
- Target demands and response events.
- Strike authorization and abort reports.
- First Soviet combat-use news.
- Evolution reports and Event Details previews.
- Soviet Collapse custody events.
- Exchange crisis reports.
- Super-event title, description, quote, and button.
- Achievements and tooltips.
- Event log and debug name mappings.
- Catalog-facing event and evolution details.

## Writing direction by surface

### Opening event

Viewpoint: Soviet political and scientific leadership receiving proof that the first arsenal is complete.

Visible information:

- The devices exist.
- The stockpile is large.
- Storage, command, and delivery are unresolved.
- The world does not yet know.

Uncertain information:

- Whether every device is reliable.
- Whether secrecy will hold.
- Whether the state can control the arsenal during crisis.

Tone: controlled, secretive, technical, and politically severe.

Avoid: triumphant slogans, generic claims of world domination, and explanations of hidden mechanics.

### Custody options

Each option should sound like the institution speaking.

- Party custody uses political control and suspicion.
- Military custody uses readiness, hierarchy, and field authority.
- Scientific veto uses certification, procedure, and fear of unsafe orders.
- Dispersed commands use survival, redundancy, and emergency delegation.

The final option text should state the visible tradeoff through tone and tooltip, without listing future secret incidents.

### Test reports

Focus on instruments, isolation, technical evidence, workers, guards, and local consequences. Public tests should show foreign observation and strategic reaction.

### Threats and responses

State the demand, deadline, target, and visible consequence. Target responses should reflect government type, military situation, and foreign backing.

Avoid vague surrender language when the demand is limited.

### Nuclear use

Use direct, serious wording. Describe the affected place, blast, disrupted command, evacuation, and response. Do not write celebratory or ironic civilian-death text.

### Soviet Collapse

Distinguish physical custody, technical access, command, and delivery. Use concrete depots, trains, officers, technicians, and settlements.

### Exchange

Show shortening decision time, failed communications, retaliatory preparation, evacuations, and confirmed detonations. Do not label every report as an omen or warning.

### Achievements

Achievement names can use restrained wordplay, historical allusion, or bitter irony. Descriptions must explain visible goals without exposing internal variable names.

## Dynamic localisation

Dynamic text should include:

- Current actor and selected target names.
- Selected state or named region.
- Bomb count.
- Readiness and Integrity values with bands.
- Current posture.
- Public knowledge state.
- Active demand and deadline.
- Current custody state and accounted devices.
- Retaliation or stand-down status.

Important values should use consistent labels, icons, and colors across decisions, spirits, reports, and tooltips. Color cannot be the only distinction.

## Accessibility and layout

- No critical information should exist only in image color.
- Readiness and Integrity need distinct icons and text labels.
- Locked actions need a concise blocked reason.
- Tooltips should normally stay within two to four short lines per value or control.
- Decision costs are icon-first and use no more than four spendable cost entries.
- Long state lists should use named regions or selected-state text.
- The category picture must not interfere with text readability.
- Decorative art must not block clicks.

## Asset review and completion

Asset production is complete only when:

- Source art exists.
- Processed PNG previews exist.
- Final DDS files exist in runtime folders.
- Sprite handoff notes identify every consumer.
- Generated source and prompts are preserved during active work.
- Contact sheets show final-size readability and transparency.
- The parent wires every non-portrait sprite.
- The super-event track is licensed, converted, registered, and documented.
- Achievement triplets are complete.
- No required asset remains a placeholder.
- The temporary event asset workspace is reconciled and removed only after durable evidence is promoted and runtime references are verified.
