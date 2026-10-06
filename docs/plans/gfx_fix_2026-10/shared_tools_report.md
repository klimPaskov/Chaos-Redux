# Shared GFX tooling

Implemented `.tools/gfx/gfx.py`, its README, dependency list and focused regression tests for the October GFX repair task.
The commands provide batch alpha erosion/interior-colour bleeding, per-frame subject-alpha inspection, slot/margin inspection, reference-based unit-counter inspection, guarded BGRA DDS writing and narrowed registry contact sheets.
The tool never installs runtime art implicitly and refuses input/report collisions and competing non-force output writers.

The parent accepted the requested slot sizes and 1 px erosion from the user's task and the repair plan's cross-cutting rules.
Decision icons use the task's 34x34 target; category icons use 52x40 with a 3 px margin.
Focus and decision margin defaults use the plan's 2–4 px range; those values remain explicit profile defaults with consumer-specific overrides.
No event design, gameplay, weights, localisation, GUI layout or catalog wording changed in this tooling tranche.

The independent Luna audit is recorded in `tools_audit.md`.
All 20 focused regression tests passed, including exact installed-vanilla counter self-comparisons, frame-local edge processing, canonical DDS header/pixel checks, mixed-frame batch lists, report/input collisions, a competing output creator and exact spill-mask selection.
The counter CLI defaults to two frames and exposes both frame diagnostics without an extra argument.
Its field-density/footprint/aspect checks reject white-and-black speckle noise without treating it as a NATO box, and stock small-counter margins pass without inventing a border gap.
The audit found and prompted fixes for report-path overwrites and concurrent output overwrites before the tools were committed.
Parent contact-sheet review prompted a further safeguard that restricts opaque chroma recolouring to the original boundary band, preserving vivid green paint inside the subject.
Explicit, reviewed coordinate masks remain available for confirmed internal key blobs; the mask never changes alpha and is protected from report overwrites.

The literal alpha check remains mean below 200 over nonzero-alpha subject pixels.
Actual installed-vanilla infantry counter silhouettes average 162.254 and 164.212 because of antialiasing.
The counter-convention check therefore compares opacity and colour spread to its supplied exact vanilla reference; the independent literal alpha check still reports those values for owner review.
White/black pixel structure and palette checks are triage, and native-size visual review remains necessary to establish a readable, correct NATO glyph.

`reference_evidence.json` retains the successfully read MCP source paths, exact line spans and source revisions for offline graphical sprite definitions, unit icon frame conventions and installed scripted-GUI documentation.
The exact canonical DDS recipe was read from `.agents/skills/chaos-redux-event-assets/SKILL.md` lines 820–841 and its `tools/convert_to_dds.py` writer lines 238–269.
A narrow `hoi4.source_lookup` request for `GFX_unit_infantry_icon_medium` (`kind = sprite`, references disabled, at most 3 definitions / 25 lines) remained pending for several minutes and was stopped; source conclusions use the directly inspected installed vanilla registry and DDS files rather than claiming that pending request succeeded.
The required reference routes were present and worked after initial discovery; there is no persistent reference-route absence.

Skills used: `chaos-redux-event-assets`, `chaos-redux-subagents` and `chaos-redux-shared-git-commit`.
No skill was created or changed; the reusable tool workflow is documented in `.tools/gfx/README.md` under the existing asset skill's mechanical-processor DDS exception.

No tool functionality was simplified or omitted.
The explicitly documented visual limitations of the counter heuristics are not completion proof for artwork.
Runtime repair selection and remaining source-art defects are recorded separately in the group reports.
