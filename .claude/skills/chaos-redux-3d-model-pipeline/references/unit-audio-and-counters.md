# Custom-unit audio and counter delivery

Read both sections for every custom-unit model package. They define the required sourced audio and bespoke counter handoffs; the parent retains final runtime wiring.

## Custom unit-counter companion

Every new custom unit or subunit must ship with bespoke counter art for every counter surface it uses. At minimum, a land subunit that emits the standard tokens needs its own large `unit_<subunit_id>_icon` counter strip and small `onmap_unit_<subunit_id>_icon` map counter. Air and naval units need the corresponding domain-specific map counters and inverted or state variants when the verified consumer exposes them. Derive the actual required tokens from the installed unit and `interface/subuniticons.gfx`. Do not infer them only from this example.

This skill owns the custom-unit counter requirement and routes actual 2D counter production to `chaos-redux-event-assets` and `chaosx_icon_artist`. The shared `chaos-redux-event-assets` [2D icon and counter generation contract](../../chaos-redux-event-assets/references/icon-and-ui-families.md#2d-icon-and-counter-generation-contract) owns image-generation source evidence (Claude Code: the gptimage MCP generate_image tool with reference_images, one image per call, each reference's role stated in the prompt, alpha verified on the saved PNG; Codex: native ImageGen), alpha processing, native-canvas QA, contact sheets, DDS round-trip validation, and parent-review states. Do not make the 3D worker draw, trace, reconstruct, resize, recolor, or otherwise author 2D icons itself.

Before counter design, inspect the closest matching installed-vanilla definition and DDS. Record source paths, native canvas, per-frame dimensions, `noOfFrames`, frame order, alpha/background behavior, border treatment, visual scale, silhouette, exact green hues and value range, shading, contrast, and owning consumer. Also inspect the matching skill-local reference and contact sheet: `units/land/counters_large/`, `units/land/map_counters/`, `units/air/map_counters/`, or `units/naval/map_counters/`. If the installed definition, DDS, and matching reference family cannot be inspected, mark counter production `blocked`. Never guess the canvas, frames, sprite contract, or style.

Route the counter brief to `chaosx_icon_artist` through `chaos-redux-event-assets` and require that worker to return the shared contract's original source PNG, saved prompt, processed alpha PNG, final DDS, native-size contact sheet, decoded round-trip evidence, manifest entry, and `gfx_handoff.md`. Preserve the sampled vanilla green palette and selected, inverted, or frame-state behavior rather than using arbitrary green. The parent owns `.gfx`, texticons, subunit definitions, localisation, and runtime wiring. A missing bespoke counter is `needs_user_review` or `blocked`. Do not use a copied vanilla counter, renamed counter, generic placeholder, or other fallback for runtime promotion or completion.

Require the counter artist's final review evidence to use matte composites decoded from the final DDS at actual consumer size, compared beside the inspected installed-vanilla family for palette, silhouette, contrast, alpha edges, and frame states. Source PNG previews alone do not pass this gate. Require counter palette arithmetic, including color differences and squared distances, to use float or int32, never int16; clamp and cast only at output to prevent overflow.

The 3D worker must keep the counter source, processed evidence, and runtime copy distinct, report the selected source, and never silently synchronize an older candidate back into the runtime surface. Until the parent visually reviews the counter contact sheet, the handoff remains `needs_user_review` or `blocked`, and the worker must not claim in-game completion.

## Custom unit sound-design companion

Every new custom unit package must define a coherent custom sound identity. Do not leave a distinctive unit silent or attach an unrelated default sound family. A vanilla sound family may be reused only when the accepted design says it genuinely matches the unit.

Selection audio is mandatory for every custom unit package. Provide at least one sourced selection one-shot, a stable runtime identifier, and an exact consumer/binding plan. Do not treat idle entry, entity creation, or another animation-state event as unit selection.

Inspect the exact vanilla consumer before planning the package because land units, creatures, vehicles, aircraft, and ships do not necessarily expose the same sound roles. Include these roles:

- selection, plus order acknowledgements or unit voice when the consumer exposes them
- idle, ambient, engine, rotor, mechanical, or creature loops
- movement
- weapon attack, plus weapon discharge only for a unit declared to fire in combat
- impact, hit, or contact
- special actions
- death, destruction, shutdown, or disappearance

The installed HOI4 infantry voice path uses the hardcoded templates `TAG_infantry_idle`, `TAG_infantry_move_out`, `TAG_infantry_neutral_combat`, `TAG_infantry_positive_combat`, and `TAG_infantry_retreat`. Installed `vo.asset` files realize them as entries such as `GER_infantry_idle` and `SOV_infantry_idle`. Recheck these templates and their installed vanilla definitions for every job.

For a custom infantry family owned by a dedicated country or original tag, define the exact `<TAG>_infantry_idle` selection soundeffect in the vanilla `Voices` category. Verify the actual tag or `original_tag` used by every intended country, including dynamic countries and cosmetic-tag transitions. This is country/original-tag routing, not subunit or sprite routing: enumerate every infantry division under that tag as a consumer. If custom and ordinary infantry coexist under the same tag and require distinct selection voices, mark per-subunit selection `blocked`. Do not replace another unit family's voice. A new soundeffect name without the exact engine-consumed identifier is not a binding by itself.

Use the repository web-search workflow to locate candidate files on the Internet, inspect the source page and direct download terms, and save only approved candidates under the deterministic job evidence root. Prefer public-domain, Creative Commons, official archive, institutional, user-authorized, or otherwise clearly licensed sources. Reject unclear provenance, unclear recording rights, unclear modification rights, vague royalty-free claims, and sources that do not permit the intended mod use.

Download and preserve the original source file under the deterministic job evidence root. Record the source page URL, direct download URL when distinct, title, creator or performer, license, usage terms, download date, original format and duration. Keep the source file immutable and link every derived file back to it.

Mechanical transformations such as trimming, fading, silence removal, normalization, channel conversion, resampling, and codec conversion are permitted only when the source license allows them. Keep the original source, transformation recipe, and final format in the evidence package. These operations must never become a way to create audio from scratch.

Probe every runtime WAV against the actual installed consumer precedent before the parent wires it. For a `Voices` category soundeffect, including `<TAG>_infantry_idle`, the default delivery contract is signed 16-bit PCM (`pcm_s16le`), 44.1 kHz, mono, matching the installed vanilla and approved custom voice precedents. A float WAV such as `pcm_f32le` must not be called runtime-compatible. Use the shared `.tools/3d_pipeline/audio/master.py` (`--help` for `inspect`, `audit-tree`, and `batch`) for supported shot, step, and loop mastering from an explicit attributable source allowlist; preserve the original source. The script stages PCM16, 44.1 kHz mono derivatives, removes DC/subsonic bias, trims leading silence, adds short fades, and measures role-specific levels and clipping. Its current targets are shot peak -3 dBFS, step peak -6 dBFS, and loop -20 LUFS with true peak at most -1 dBTP. Do not relabel an unsupported voice or selection role merely to fit those presets; record its required consumer contract separately. Do not mark the handoff complete until every installed WAV has an `ffprobe` receipt for codec, sample rate, channels, and bit depth.

Bind each audio derivative to the exact source and derived paths and SHA-256 values, the cited attribution row, creator/license/source URLs, transformation recipe, before/after measurements, and exact unit/soundeffect consumer. A cited row or successful mastering receipt does not independently establish derivative licensing or playback quality. The shared script cannot synthesize audio, authorize a missing source, or install runtime files; keep long-form and super-event audio audit-only in this unit-mastering route.

The sound handoff must define:

- the unit or subunit id and runtime consumer
- the chosen vanilla sound and voice precedents
- the mandatory selection source, soundeffect identifier, exact engine consumer, binding scope, resolved country or original tag, and every infantry consumer under that identity
- proposed sound, soundeffect, wrapper, and file identifiers
- one-shot or loop behavior
- the animation action and exact frame or phase that each sound should follow
- source mode, provenance, licence status, and forbidden substitutions
- expected final file format and runtime path based on verified local precedent
- any volume, range, variation, or randomization behavior supported by that precedent
- the Internet source URL, attribution, license, original file path, derived file path for every sourced audio candidate
- the parent-owned files that must be wired and the validation still required

Custom vocal units should have voice direction that matches their culture, language, body, and role. Nonhuman or impossible units should use purpose-built, sourced vocalizations or mechanical sounds rather than ordinary soldier acknowledgements. Do not manufacture final audio from test tones, primitive oscillators, placeholder beeps, or unrelated stock effects.

The model worker does not claim the sound package complete merely because synchronization points and identifiers are documented. It must provide sourced audio candidates and licensing evidence or mark the role blocked. Selection acceptance requires evidence from the actual selection consumer and cannot be inferred from idle or another entity state. Sound definitions and entity or unit wiring remain parent-owned unless the task explicitly grants that production scope. The user performs in-game playback validation, and the parent reviews that evidence.
