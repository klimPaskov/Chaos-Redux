# Asset manifest and candidate lineage

Read this reference when creating or updating an event asset workspace manifest, and whenever generated candidates are produced, edited, reviewed, or selected. The main skill keeps contact sheets, the requirement-to-runtime coverage audit, and completion rules.

## Evidence and completion

### Manifest requirements

Every active event asset workspace must include a markdown manifest.

Recommended path while work is active:

```text
docs/assets/<event_id>_<event_slug>/manifest.md
```

The manifest must list every asset. Before deleting the temporary workspace, copy any durable provenance, licensing, attribution, coverage, review, and exception facts needed by the event documentation or audit handoff into a permanent documentation surface.

Each asset entry must identify:

- Asset name/type, event id/slug, intended in-game use, exact target size, related focus/idea/event/decision/UI/super-event id, and localisation key where relevant.
- Source mode (image generation, portrait-production output, internet source, or user-provided source); generated prompt and rationale, or source link, available author/archive/collection, date/range, license/public-domain status, era fit, and uncertainty.
- Background mode (`native_transparent`, `consumer_opaque`, or `fallback_removed`), with the fallback reason, verified edit/tool and settings where applicable.
- Source and processed PNG paths, final DDS path, sprite name, owning `.gfx`, notes, and status.
- Generated candidate lineage and review evidence under [Candidate lineage and review](#candidate-lineage-and-review), including input roles, exact edit deltas, immutable source/intermediate paths, verdicts, and explicit final selection.
- For animation: frame count/timing, loop, anchor, static fallback, sheet or frame-sequence paths, and each frame's source mode and source note.
- For real-person portraits: durable source path/attribution, exact crop evidence, source-placeholder wiring when selected, provider-backed styled final only when explicitly requested and available, role references, review evidence, and exact runtime DDS basename/path. Record the independent reviewer's identity/date, proof they are not the producer, separate likeness/style/framing/provenance verdicts, and gate state.
- For portrait ownership: search terms, roots/files/ids checked, matched owner/consumer or explicit no-match evidence, disposition, and guarded transfer/availability contract where applicable.
- Selected portrait mode/state: `source_placeholder` (accepted unchanged source/crop runtime, explicitly pending HOI4-style replacement), `replacement_pending` (only while an explicit styled-final request remains outstanding), `styled_final` (validated provider-backed output), `not_needed`, or `blocked`.

Use `not_needed`, `planned`, `sourced`, `generated`, `processed`, `converted`, `handed_off`, `wired`, `complete`, `needs_user_review`, or `blocked` as asset statuses.

#### Candidate lineage and review

Before each image-generation call or edit, save the exact request arguments in a repo-contained prompt record: `prompt` (including the transparency request), `transparent_background` where the tool exposes it, `out`, `quality`, and `size` where the tool exposes them, and supplied reference paths or recent-image count, with the actual referenced images identified and retained.

While the asset workspace is active, keep the original generated source and every accepted intermediate immutable at distinct versioned paths. Keep source outputs separate from processed previews and runtime files. In the active manifest or linked prompt record, record for each generated candidate:

- candidate id, parent candidate id or new-generation reason, and input paths with their declared roles
- linked exact saved request, focused edit delta, invariants, and background mode
- tool-reported output path, retained workspace path, source SHA-256, decoded dimensions, and alpha evidence
- source-resolution and final-native-size review results, accepted/rejected status, and remaining defects
- explicit final-selected candidate id, processed PNG path, final runtime path after conversion, and each subject's source-to-layer/frame-to-consumer mapping

Before runtime promotion, review every newly generated or edited subject against its actual source and saved request; a correct-looking preview does not establish image-generation lineage.
Deterministic template/frame geometry and processing remain allowed under the applicable family contract, but cannot replace generated subject art.
If an exact historical request is unavailable, mark it unavailable and preserve known source paths/hashes rather than reconstructing it; fresh generation or editing must remain within existing authorization and portrait/source-mode, provider, and fallback boundaries.

Do not silently overwrite a prior accepted candidate or synchronize an older candidate into runtime. Before normal temporary-workspace cleanup, promote the lineage, prompts, final selection, and review facts into permanent documentation under the existing cleanup contract. Retain active image files until the required package review is complete; this rule does not create a second permanent asset archive.
