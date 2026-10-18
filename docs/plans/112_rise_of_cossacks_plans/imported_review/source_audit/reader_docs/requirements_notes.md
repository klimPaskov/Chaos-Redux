# Documentation curator source reading notes

## Scope and evidence status

This is a source reading handoff for planning, not a specification or implementation audit.
Only assigned source files are being read before the team gate passes.
The parent owns external research and final design after that gate.
No source, gameplay, catalog, spreadsheet, asset, or external-service changes are authorized here.
All notes in this directory are intermediate working evidence.

## Prerequisite requirements

The source protocol requires every supplied file and each distinct nested archive variant to be read fully before substantive planning.
Truncated output does not count and must be replayed.
Exact byte equality, established by SHA-256 verification across supplied paths, supports reading one representative for a group.
The initial combined prerequisite response was truncated and is not used for coverage.
Every prerequisite was subsequently replayed completely through bounded character chunks.

Current AGENTS.md requires offline Paradox wiki sections and installed vanilla documentation for later implementation.
Installed documentation is the more authoritative technical reference, but both sources remain required.
The Paradox wiki must not be accessed on the web.
Read-only MCP reference routes must be discovered and their live schemas verified before use.
Source paths, line spans, revisions, unresolved commands, omitted content, route availability and health remain explicit evidence.
Scope-specific MCP inspect, render and compare evidence remains necessary for later implementation and is not implied by tool exposure.
The user performs live-game validation and agents do not launch the game.
The ChatGPT source protocol explicitly permits future MCP and project-role usage maps when those capabilities are absent.

No source-only review may be called engine validation.
Current user decisions outrank older design and classification.
Accepted design needs explicit acceptance evidence and is separate from current implementation, proposals and dated handoffs.
Plan dispositions are unresolved, accepted and queued with evidence and reason, implemented with evidence and validation limits, promoted into an accepted spec with evidence and destination, rejected with reason, superseded by a named replacement, or blocked by an exact limitation.
Source specs belong under docs/specs/<event_id>_<slug>_specs/ and working plans and handoffs under docs/plans/<event_id>_<slug>_plans/.
Markdown prose keeps each sentence on a physical line.

The curator may reconcile only documentation within the parent scope.
It may not create new gameplay design from scratch, change source implementation, assets, localisation or spreadsheets, or claim gameplay completion.
The parent reviews all handoffs and owns final integration and completion claims.
Project role prompts are self-contained and have no inherited context in runtimes supporting that mechanism.
The canonical Codex argument is fork_turns="none".

The shared event log, event-details window, settings, super-events and shared registries remain parent-owned.
The event UI worker is only for a dedicated window expressly owned by the named event and introduced by accepted design.
AI and probability changes require a named-scenario baseline audit, owner-applied patch, immutable source snapshots and mandatory probability_compare through the read-only probability auditor.
Exact baseline source bytes and scenario identities matter.

All portraits route to the portrait creator.
Grounded identities use attributed source material, durable portrait source storage and a wired source placeholder.
The user alone supplies grounded HOI4-style finals through their own RunPod work.
Fictional or impossible portraits use native ImageGen under the portrait worker.
Counter and icon art has its own original-art and exact-consumer reference requirements.
Native alpha is required by default for transparent consumer families.
All flags need ImageGen source evidence, with sourced exact geometry for historical designs.

The event catalog XLSX is the sole editable catalog authority.
CSV files are export-only, regenerated with python .tools/export_event_catalog_csv.py after a successful workbook update.
Spreadsheet work is deferred until implementation facts exist and mirrors in-game text.

## External references identified so far

- docs/runtimes.md for runtime mappings and tool configuration.
- Relevant offline paradox_wiki files for effects, triggers, scopes, modifiers, data structures, decisions, events, ideas, AI, on-actions, localisation and any used GUI, focus, country, technology or unit surfaces.
- Installed HOI4 documentation for corresponding syntax and semantics.
- common/scripted_effects/chaosx_dynamic_effects.txt and its Markdown documentation before planning new reusable helpers.
- docs/testing/chaosx_test_country.md when new land units, equipment, projects, facilities, doctrines or general systems require idempotent CXT setup registration.
- docs/spreadsheets/README.md before later catalog edits.
- Named current event source files, runtime consumers, asset definitions and exact installed vanilla precedents after the source gate.

## Coverage detail

See coverage_ledger.json for completed source hashes and character ranges.

## Role definition requirements and version differences

All twenty assigned old and current TOML variants have been read completely.
The old comfyui source has also been read completely.
Its source-placeholder mode preserves the attributed identity, crop and deterministic 156x210 resize and does not require an HOI4 repaint.
An optional styled final begins only after an explicit user request and is supplied by the user.
Never operate, configure, queue or monitor RunPod.
Do not mark replacement_pending unless a styled-final request is outstanding.
Current general prose still calls the grounded source placeholder pending until a user-supplied styled replacement, so separate source-placeholder delivery status from any optional replacement request.

The current curator and skill-maintainer model strings move from gpt-5.6-sol to gpt-6.1-sol.
Text research, audio research, sourced visual art, generated art, portrait, spreadsheet and icon roles move from gpt-5.6-luna to gpt-6-luna.
Those runtime settings do not imply that an already running agent changes model.
The curator body is unchanged between variants apart from the model metadata.

The source and generated art roles replace assets/vanilla_reference with assets/gfx_references as the canonical reference root.
Reference copies are review evidence, not runtime art.
The parent must give exact asset identity and source classifications, target sizes, paths, sprite names and handoff paths.
Grounded documentary imagery requires period fit and defensible provenance, with no invented licensing or substitute identity.
Generated scenes maintain period clothing, vehicles, architecture and technology.
Councils and collective institutions use people-free institutional compositions and institutional names.
Generated art and source researchers do not own character portraits or gameplay and GFX wiring.

The text researcher considers multiple real main quotes and cultural remark candidates, verifies exact wording and attribution with primary sources, records sources, dates, confidence and rights, and provides a complete selection plus backups tied to the specific super-event role.
It never fabricates a quote or presents a paraphrase as a direct quotation.
Modern copyrighted excerpts stay short.
The audio researcher separately checks composition and recording rights, preserves the downloaded source, prepares a real game-ready WAV, documents conversions and attribution, and cannot call default or placeholder audio complete.
Usual super-event track length is one to three minutes unless the brief justifies otherwise.
Both research roles have narrow research context and do not own wiring.
Those narrow context rules are implementation routing rules and do not waive the initial all-source reading gate.

The current portrait role replaces the comfyui skill read with event-assets plus references/portrait-production.md.
It adds assets/visual_components/portrait_backdrops as reference-only material that can inform composition after exact vanilla portrait reference inspection.
That family never provides an identity source or a replacement portrait.
Portrait worker ownership includes source research, durable docs/assets/portraits/<event_id>_<slug>/ provenance, fictional ImageGen output, PNG and DDS production, portrait-specific GFX and existing portrait references, manifests and handoffs.
It cannot change character identities, traits or other gameplay.

The current spreadsheet role explicitly names chaos-redux-xlsx and adds docs/spreadsheets/README.md for schema, status, Legend and export rules.
All mirror fields use exact in-game localisation wording, while summary fields may summarize.
Missing, stale, contradictory or unimplemented text is blocked or needs_user_review rather than guessed.
No spreadsheet action is authorized in this planning task.

The current icon role uses gfx_references and adds visual_components/CATALOG.md and matching sheets where useful.
Focus pieces and backgrounds guide original ImageGen composition.
Only entries explicitly cataloged background_template for idea, national-spirit or decision-category use may be composited beneath an original subject when the exact consumer fits.
Keep component source layer, original ImageGen layer and final output distinct, with catalog entry and role in the manifest.
Achievement art uses one original transparent subject at 64x64 and exact immutable completed, grey and overlay template inputs.
Grey is deterministically derived from the subject and the not-eligible layer adds the unchanged red-cross overlay at exact alignment.
Use process_achievement_icons.py on all three sources, retain exact source and output evidence and put final DDS files directly under gfx/achievements using the registered achievement ID.
Custom counters require exact installed-vanilla definition, DDS, frame order, canvas, alpha, consumers and sampled green palette before original production.
Uninspected references, arbitrary green and copied or renamed vanilla counters fail acceptance.

## 3D role requirements pending full owner-skill verification

The current 3D TOML is materially different from the old one.
Old body text names GPT-6-astra for Blender work and fixes a Blender version, while its own metadata names gpt-5.6-sol.
Current body text uses runtime agent configuration and dependency-lock versions and names gpt-6-luna in metadata.
Current adapter work uses separate factory-startup Blender workers for processing and export.
Current live Blender Lab authoring is permitted for actual component, rig, weight and keyframe work where the adapter lacks operations.
The old body had restricted Blender Lab to a development profile and required the adapter for every Blender operation.

Both versions demand a nonblank Meshy environment key before provider discovery, balance checks or calls, with no key needed for existing Blender-only repair.
They require verified dependency locks, actual exposed schemas, exact Meshy 7 identifier, immediate downloads and checksums, protected provider sources, named vanilla scales, export and reimport evidence and explicit blocked states for unavailable capabilities.
The current version limits geometry recovery to paid_generation_attempts_per_pilot and retry_paid_calls recorded in the lock and job.
The older role permitted automatic geometry retry and recovery while balance and provider capabilities allowed.
Repeated paid rigging or action attempts are not the ordinary fallback in either route.
One provider rig attempt per eligible model and one provider attempt per required action precede actual Blender repair or authoring for failed or unsupported stages.
The latest detailed body expands provider eligibility from standard humanoids to clear bipedal anatomy, which need not be human.

All equipped bodies in current detailed rules must be generated item-free with empty neutral hands.
Each held firearm, melee weapon, tool, shield, staff, banner, instrument or carried object gets a separate Meshy geometry task from exactly one item-only image.
The body skeleton, skinning and provider actions come from receipt-verified Meshy results for eligible bodies.
Blender assembles and adapts the whole body and item before final action review.
Parenting an item after reviewing empty-handed actions fails acceptance.
This supersedes the old firearm-only instruction to bypass provider rigging and author firearm unit rigs and animation directly in Blender.

The current TOML description still repeats the older firearm-direct-to-Blender route while the detailed equipped-item rules require Meshy rigging and provider actions.
This is an actual internal conflict to flag and resolve against the full current 3D owner skill.
Current general subagent routing also describes automatic authorized recovery while the detailed current role supplies explicit locked attempt allowances.
Do not flatten that distinction or propagate unlimited credit retries into the planning handoff.

Every model source is selected modern designed artwork with verified terms, then native ImageGen creates an original model-ready refinement that preserves selected identity traits.
Archival, museum, historical, ethnographic, reenactment and documentary imagery is rejected as model input under this source rule.
Source-free generation is a separately approved fallback after documented source-search failure.
Explicit NoAI or no-derivative restrictions are rejected.
Exactly one approved final image reaches each provider task and evidence boards never become provider inputs.

Model runtime ownership stays with the parent.
The 3D worker produces models, materials, rigs, actions, source and QA evidence, sourced-audio packages and bespoke-counter handoffs, but it does not edit entity, GFX or sound-definition runtime wiring.
Every semantic action needs real articulated motion, contact and deformation evidence.
Static poses, whole-rig transforms and relabeling one action as another are forbidden substitutes.
Skeleton changes invalidate downstream action and export approvals.
Custom-unit sounds must be legally sourced recordings, with no generated, synthesized, recorded-by-agent, placeholder or unlicensed final audio.
Mechanical edits preserve original files, provenance and hashes.
Required sounds map to exact animation frames or phases.
Counters require the exact vanilla family and sampled green palette as above.

## Additional required external references

- .agents/skills/chaos-redux-event-assets/references/portrait-production.md for the current portrait workflow.
- .agents/skills/chaos-redux-event-assets/assets/gfx_references and the exact matching family and contact sheets.
- .agents/skills/chaos-redux-event-assets/assets/visual_components/CATALOG.md and permitted family materials when relevant.
- The achievement template images and process_achievement_icons.py when producing achievement states.
- .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py for ordinary PNG to DDS conversion.
- .tools/3d_pipeline/config/dependencies.lock.json, meshy_tool_schema.lock.json and blender_hoi4_adapter.json for any later model job.
- Exact installed-vanilla meshes, entities, materials, action sources, subuniticons.gfx and counter DDS files for calibrated model and counter production.

## Completed asset-skill requirements

Both complete asset-skill variants have now been semantically read.
The old variant has 109688 decoded characters and the current variant has 117311.
The full normalized source diff was also inspected after the full reads, solely to check the version-difference handoff.

### Authorization and source classification

Start from accepted asset requirement rows, not from whatever gameplay objects or files happen to exist.
Do not infer an advisor card, small portrait, extra route emblem, animation or custom asset family from a character, trait, idea or consumer slot.
The formable asset checklist lists possible identity coverage, but the accepted requirement inventory determines which rows are authorized.
Every row needs a requirement ID, purpose, source package, runtime registration, live consumer, state binding and current audit record.
Extra files and sprite totals do not satisfy missing rows.

Grounded source-only identities include real, partly real, restored, separatist, regional, indigenous, dynastic and otherwise plausibly historical polities, communities and institutions.
Such identities need attributed real people or authentic institutional sources.
Invented people are limited to truly fictional high-chaos identities or impossible entities.
This makes the source-mode classification important for the later Cossack package, but no candidate roster is selected in this source reading phase.
Before reusing a real-person token, check variants, transliterations, titles and name order in vanilla and project character, history, portrait, interface and localisation roots.
A live roster cannot duplicate a person.
Any transfer must invalidate original ownership before target ownership and prevent simultaneous ownership.

Portrait source packages keep unchanged original bytes, exact lossless crop, deterministic 156x210 candidate, crop and equality JSON, and co-located provenance text together under the stable runtime basename.
Independent identity, framing and provenance review precedes wiring.
The producer cannot self-approve a portrait or an advisor card.
Source-placeholder delivery does not equal a styled-final portrait.
The state replacement_pending is reserved for an explicitly requested styled final that remains outstanding.
The user alone supplies the grounded styled final and no agent operates RunPod.

### Consumer sizes and production boundaries

The skill defaults are report 210x176, news 397x153, full leader/commander/operative portrait 156x210, super-event 457x328, idea 64x64, focus 94x86, decision 32x32 and achievement 64x64.
Flags use 82x52, 41x26 and 10x7.
Advisor and high-command cards are independent 65x67 art and never plain 50x67 crops of full portraits.
The exact active consumer overrides a generic default.
Record canvas and frame semantics from the actual definition for every other family.
Technology aliases and equipment aliases can share misleading suffixes, so inspect actual consumers before changing dimensions.

Report images are documentary photographs processed into a deterministic tilted 210x176 RGBA card with monochrome sepia, transparent corner space and a soft shadow.
Generate or source the photo first and apply card treatment locally with process_report_event_image.py.
News is 397x153 monochrome documentary material.
Super-event art is a real scene, archival image, painted scene or generated documentary scene at 457x328, never a title card or primitive symbolic diagram unless explicitly requested.
Period sources and fictional documentary output fit 1936 to 1945 unless an explicit accepted exception changes the date boundary.

Flags always begin with ImageGen output even when historical, after exact sourced geometry and heraldry are established.
Flat geometry, symbol count, orientation, colors and details must match historical evidence where attested.
Do not replace an existing country base flag during an ideology-only pass.
Route changes use explicit cosmetic or route flags.
Ideology variants are independent designs, not palette swaps.
The full source and all three size exports must retain identity and have vanilla-compatible TGA orientation.

Focus, idea, decision, officer corps, mission, achievement, technology, agency, trait, raid, MIO, faction, building and other icon surfaces are separate types.
Each gets separate source art, brief, reference, canvas, naming, manifest and output.
A coordinated family may share visual vocabulary but may not satisfy one type by resizing another.
Native transparent canvas is the default for alpha-backed families.
Background removal is a documented repair route after native-alpha failure, not a normal generation stage.
Review real zero-alpha padding, intact edges, matte, halos, fringe, holes and native-size readability.
Boundary contact at a very low alpha threshold alone does not prove clipping, while real clipped painting must be repaired by editing the source.

Achievement art uses exact immutable template hashes and one generated subject whose deterministic grey and not-eligible states stay aligned.
The processor verifies each full triplet and exact composition rather than generating three different subjects.
Final achievement IDs, registry, localisation, sprites and root-level DDS filenames must agree.
Generic conversion does not replace process_achievement_icons.py.

Large land-unit counters use two adjacent 76x42 frames in one 152x42 strip.
The left is the muted vanilla-green normal counter and the right is a separate sparse pale schematic glyph, not a white repaint.
Division-template emblems separately use 76x42 and 30x12.
These dimensions remain subject to exact consumer inspection and are separate from map counters or equipment illustrations.
Every used custom-unit counter surface needs original art and sampled exact vanilla colors.

### Presentation hierarchy and geographic accuracy

An ordinary decision category may use a small category icon and a static picture, or a justified animated picture, only while it has normal decisions, descriptions and at most basic formatted value tables.
Complex meters, extra custom controls, rich panels or other animation make the category picture ineligible.
Do not combine a territorial category picture with an interactive state-puzzle GUI for the same presentation surface.
Native controls, labels, states and click regions must remain separate from decorative image layers.
A flattened screenshot or fake control baked into a background cannot be called a functional UI.

Formable territorial pieces come from exact installed state and province geometry under one projection, scale, origin, border and edge treatment.
The manifest identifies the state ID, name, alternate group, counting rule, source geometry, bounds, anchor and sprite.
Use grey unmet and green qualifying states with an additional non-color distinction and reliable hover regions.
Never invent borders with ImageGen, trace screenshots by hand, replace geometry with tiles or use a modern political map as a substitute.
Choose separate sprites, atlas frames, sheets or masks only after confirming the GUI can address each state independently.

### Evidence, conversion and handoff

Before production assign stable runtime basenames and sprite paths and retain exact ImageGen request arguments.
Each candidate records parent, input roles, exact delta, invariants, native source hash, dimensions, alpha evidence, full-resolution and native-size review, final selection and source-to-consumer mapping.
Review against actual source and saved request before promotion.
Do not reconstruct an unavailable historical prompt as though it were the actual request.
Preserve pre-edit runtime textures, registry text and baseline sheets with hashes during replacement work.
Contact sheets never overwrite baseline evidence or count as runtime assets.
All changed frames in a strip need separate native-size review.

For ordinary 2D assets use only .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py.
The old .tools/convert_to_dds.py path is obsolete.
Require the documented one-level BGRA header and byte length and retain decoded round-trip visual evidence for small icons and counters.
Current text explicitly exempts 3D materials from the 2D recipe and sends them to the owner 3D skill's BC1/BC3 full-mip workflow.
Model-byte decode and reimport evidence alone does not establish rendered material, deformation, playback or live-game acceptance.

Event assets use <category>/<event_id>_<slug>/ with no redundant project namespace layer.
Flags retain tag naming and engine flag folders.
Achievement DDS triplets stay directly under gfx/achievements/.
Super-event audio uses sound/<event_id>_<slug>/ and source audio remains in evidence storage during work.
The parent owns general GFX, GUI, gameplay and sound wiring, while portrait-specific GFX is the documented narrow exception.
Asset workspace cleanup is deferred until all accepted rows are wired, reviewed and durably documented.
Blocked or active work retains evidence.
Completed work has no runtime path into docs/assets and deletes the temporary event workspace after promotion of provenance and handoff facts.
The separate durable portrait archive is never part of that deletion.

## Asset version differences verified after complete reads

- Current references move from assets/vanilla_reference to assets/gfx_references.
- The old assets/leader_portraits compatibility shelf is replaced by the direct canonical leaders shelf and gfx_references/REFERENCE_MANIFEST.md.
- UI reference families move from generic interface subfolders to scripted_guis, including explicit Chaos Redux settings, event log and chaos-meter provenance.
- The current skill adds the owned references/portrait-production.md workflow and removes the old comfyui routing dependency.
- Current text adds visual_components catalogs, exact permitted background-template roles and separate source layers.
- Current text adds exact subtype palette review and actual-consumer checks before changing shared texture dimensions.
- Current alpha validation distinguishes low-alpha residue from genuinely clipped subject parts.
- The current advisor workflow resolves old conflicting wording about a missing shared processor by explicitly using create_advisor_icon.py for the canonical template surface.
- Current 3D handoff text replaces direct firearm Blender rigging with Meshy body rig/actions and separate item geometry tasks plus live Blender assembly review.
- Current text separates compressed full-mip model materials from ordinary uncompressed 2D DDS and names the shared model audio mastering path.
- Current lineage records retain exact request arguments, source hashes and per-subject source-to-layer or frame-to-consumer mappings.
- Current replacement review preserves baseline textures, registries and contact sheets, checks every changed frame and distinguishes DDS decoder limitations from missing assets.
- Current coverage distinguishes logical slots, aliases, consumed paths, file hashes, decoded-pixel hashes, provenance and accepted-final coverage.
- Remaining asset differences are wording, punctuation or formatting and do not alter the core route.

## Complete frame-animation requirements and differences

Both complete frame-animation variants have been read, with 28266 old and 29504 current decoded characters.
Their normalized full diff was also inspected after full reading.
The current substantive addition is the 16384-pixel ceiling for either texture side and a synchronized vertical-strip route for sheets that cannot fit without unacceptable reduction.
Strip width must divide the frame width and strip width times frame count must fit the ceiling.
Each strip sprite shares frame count, FPS, looping, play_on_show and pause_on_loop, with contiguous GUI placement and correctly interpreted center origins.
Do not silently downgrade requested motion when applying the size limit.

Every meaningful visual state must have an actual generated, sourced, user-provided or approved authored frame.
Transforming one still with position, scale, rotation, filters, opacity, glow or scripted particles is not final animation.
A GIF is review-only and never a runtime asset.
Generate an accepted seed and frame plan first, then use accepted seed or neighboring accepted frames with explicit motion deltas and unchanged subject, palette, camera, canvas and anchor.
Sunburst is the stated preference where selection exists, but the actual tool path must be reported honestly when the active ImageGen schema exposes no model selector.
No unreported backend model, resolution or quality selector may be claimed.
Native alpha is requested for each alpha-backed frame and preserved through every mechanical step.
Real-person animation must not imply invented footage, speech or new real-world behavior.
Permitted sourced stills and symbolic overlays stay clearly within game-art scope.

The brief specifies use, size, frame count, sheet dimensions, timing, looping, play_on_show, anchor, source mode per frame, background, static and animated sprite names, runtime paths, target files and inspected precedent.
The frame plan has a motion state and exact visible change for each frame and a clean loop transition.
Choose adequate real frames for intended smoothness.
A low frame count needs a size, performance or deliberately stepped-motion justification rather than convenience.
Mechanical scripts may align, crop, normalize, pad, assemble, preview and convert existing frames only.

The usual runtime package is a one-row sheet, no gaps or labels, source and processed PNG frames, sheet PNG and DDS, static fallback PNG and DDS, preview GIF, contact sheet, manifest and GFX handoff.
The sheet width is frame width times noOfFrames and the height is the frame height.
Do not append an extra first frame to the runtime sheet unless its frame count and loop semantics deliberately include it.
The sprite generally uses frameAnimatedSpriteType, but the exact target surface still requires offline wiki and installed-vanilla or established project precedent inspection.
No generic example snippet proves engine support for a portrait, focus or decision consumer.

Leader overlays use separate transparent scripted GUI containers rather than silently replacing portrait art.
Inspect countrypoliticsview.gui or countrydiplomacyview.gui, record exact element and ancestor offsets, and use the correct player, selected-country or diplomacy-target context.
Decorative layers are click-through with alwaystransparent.
Gate both the GUI and icon by the same actor-scoped trigger.
Fix incorrect actor visibility through scope, not coordinate changes.
Independent loaded parents are safer than guessed nested instance names.
Record parent, context, trigger, position, scale, offset calculation, static fallback and source definition.

Missing real frames, source or runtime precedents, failed alpha, identity drift, conversion failure, mismatched sheet size or unresolved prompt names remain exact blockers.
Do not replace an accepted animated row with a static image or a mockup.

## Final source-reading status

All 25 hashes in the revised curator assignment are fully read.
The protocol, current AGENTS.md and current subagent routing skill are also fully read.
The old event-planning skill and both super-event skills transferred unread to the parent.
Both full 3D skills transferred to the scripted-system architect, with the current skill's first 48000 characters read here and the rest assigned there.
This report does not claim those transferred full files were completed by this agent.
The parent owns the global gate and must combine every agent's complete coverage before substantive work.
No external research, requested specification drafting, gameplay editing, asset production, provider work, workbook edit, CSV edit or engine verification occurred here.
