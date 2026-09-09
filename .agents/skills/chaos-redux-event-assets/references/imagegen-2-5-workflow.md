# ChatGPT Images 2.5 asset workflow

Read this reference for generated Chaos Redux raster assets and edits permitted by the owning asset skill.
It supplements the official `$imagegen` skill with project evidence and consumer requirements.

## Execution boundary

Use built-in `image_gen` by default for ChatGPT Images 2.5 generation and editing in Codex.
OpenAI documents improved reference fidelity, focused editing, multi-turn consistency, complex composition, transparency, and latency in [Introducing ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/) (September 8, 2026).
These improvements support incremental correction; they do not prove that a candidate satisfies the brief.

The built-in tool currently exposes no model, quality, size, or destination-path selector.
Describe composition, intended consumer dimensions, detail, and background treatment in the prompt, inspect the returned dimensions, and process the selected output to the exact runtime canvas afterward.
Do not present API model choices such as `gpt-image-2.5-flare` or `gpt-image-2.5-sunburst` as built-in controls or claim a backend variant that the tool did not report.
If the user explicitly requests CLI/API execution, follow the installed official `$imagegen` skill and verify its supported model/parameter contract; do not duplicate its runner or silently switch execution paths.

## Brief and reference roles

State the intended asset and consumer, subject, composition, style, and constraints before generation.
Label each supplied image by index and filename, with its role and the properties that may transfer:

| Role | Allowed transfer | Properties to exclude unless explicitly required |
| --- | --- | --- |
| Edit target | Current accepted image and the named edit region/property | Unrequested changes elsewhere |
| Identity or subject anchor | Authorized fictional subject, object, motif, or other permitted subject properties | A reference person's face, unsupported insignia, extra subjects |
| Style or reference-family anchor | Palette, shading, texture, visual density, edge treatment | Exact artwork, subject identity, frame, text, canvas from another UI surface |
| Geometry or composition anchor | Intended arrangement, silhouette proportions, camera, reserved space | Sketch marks, labels, incidental props, invented map geometry |
| Insert or compositing input | Explicitly named object or layer with its intended placement | Its backdrop, unrelated content, unintended text |

Inspect local edit targets with `view_image` before editing and attach inputs using the actual built-in schema.
When all targets have local paths, use `referenced_image_paths`; otherwise use the smallest `num_last_images_to_include` covering the required recent images, and never supply both.
Do not rely on an unseen path, ambiguous “previous image,” or filenames alone to convey visual references.

Subject anchoring never changes the portrait source-mode gate.
Grounded people and institutions remain sourced under `chaos-redux-comfyui`; improved likeness is not permission to repaint or synthesize them with ImageGen.
Historical design sources and exact map geometry retain their existing verification rules.

## Focused iteration

When a candidate is close, edit that candidate to correct the specific defect before choosing a fresh composition.
Use one coherent change per iteration, then inspect it before proceeding.
Use the prior accepted output as the next edit target; if a revision drifts, return to the last accepted candidate and record that branch instead of building on the rejected result.
A substantially wrong composition or an explicitly requested alternative can justify a new generation; record the reason and retain accepted candidates.
The shared prompting approach follows [OpenAI's image prompting guidance](https://developers.openai.com/api/docs/guides/image-prompting).

Restate the invariants in every edit: subject identity where authorized, pose/composition, palette/style, consumer canvas and intended footprint, reserved space, and alpha/background mode.
For alpha-backed assets explicitly request preservation of real transparent unused canvas after every edit.
For opaque scene art preserve the required painted background instead.
State “no added text, symbols, subjects, borders, or UI controls” where applicable; list any deliberately authorized exception precisely.
Keep functional UI labels and controls native even when the generated composition follows a complex layout.

For a coordinated asset family, an accepted candidate can serve as a style anchor when it improves consistency.
Transfer only the stated palette, materials, texture, or motif vocabulary, and retain the exact consumer family's reference as the authority.
Generate every distinct icon or UI surface separately with its own brief, source, canvas, silhouette, and manifest row.
A style anchor does not permit cross-type resizing, tracing, recolouring, or lightly editing one focus icon into a decision icon.
Preserve deterministic supplied-template composition and state derivation where the owner skill requires them, including achievement triplets.

## Candidate lineage and review

While the asset workspace is active, keep the original generated source and every accepted intermediate immutable at distinct versioned paths.
Keep source outputs separate from processed previews and runtime files.
In the active manifest or linked prompt record, record for each generated candidate:

- candidate id, parent candidate id or new-generation reason, and input paths/hashes with their declared roles
- exact submitted prompt, focused edit delta, invariants, and background mode
- tool-reported output path, retained workspace path, SHA-256, decoded dimensions, and alpha evidence
- source-resolution and final-native-size review results, accepted/rejected status, and remaining defects
- explicit final-selected candidate id, processed PNG path/hash, and final runtime path/hash after conversion

Do not silently overwrite a prior accepted candidate or synchronize an older candidate into runtime.
Before normal temporary-workspace cleanup, promote the lineage, prompts, hashes, final selection, and review facts into permanent documentation under the existing cleanup contract.
Retain active image files until the required package review is complete; this rule does not create a second permanent asset archive.

Inspect every iteration at full source resolution and the final HOI4 native size before accepting it.
Check subject and reference fidelity, silhouette, footprint, clipping, unintended additions, and small-size readability; reject fine detail that becomes noise after downsampling.
Decode alpha rather than trusting a checkerboard preview: verify transparent unused pixels, intact intended opaque interior, edge continuity, and no matte, halo, colour fringe, or unintended holes.
Compare each edit with its accepted parent and original anchor so accumulated drift is visible.
Keep the existing contact-sheet, DDS round-trip, frame continuity, independent portrait review, and parent promotion requirements from the owner skills.
