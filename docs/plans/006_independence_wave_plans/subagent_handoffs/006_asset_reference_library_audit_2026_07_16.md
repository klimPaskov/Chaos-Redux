# Asset Reference Library Audit Handoff

Date: 2026-07-16
Owner: `/root/asset_reference_audit`
Scope: reusable `chaos-redux-event-assets` skill, its visual-reference library, and the reusable advisor-card processor
Gameplay scope: none; no Event 006 script, localisation, runtime asset, spreadsheet, or presentation file was edited

## Outcome

The reusable asset-reference library is organized under
`.agents/skills/chaos-redux-event-assets/assets/`, with the canonical examples
under `assets/vanilla_reference/`. It contains 283 cataloged reference PNGs in
37 semantic families, 37 local contact sheets, and one separately documented
achievement workflow overlay that is intentionally excluded from the reference
count and contact sheet.

The reusable advisor-card package is self-contained. Its active manifest pins
both approved ImageGen frame/paper source-overlay pairs and the exact six
skill-local advisor references. The processor does not need an Event 006 or
Event 015 package, a user-specific ImageGen store, or an external working copy.

The final advisor processor state is version 4.3. Two clean invocations passed
the complete six-reference gate and produced byte-identical PNGs. A 65x67 DDS
conversion decoded pixel-for-pixel identically to the approved PNG candidate.

## Required references consulted

- Offline wiki core pages: Data structures, Triggers, Effects, Modifiers,
  Localisation, Scopes, On actions, Event modding, Decision modding, Idea
  modding, and AI modding.
- Offline wiki system pages relevant to this audit: Interface modding, Scripted
  GUI modding, Country creation, National focus, and Equipment.
- Vanilla documentation and precedents: character, decision, equipment,
  equipment-group, special-project, and focus-inlay documentation, plus every
  vanilla source/owning-definition path recorded in the generated catalog.

## Files and surfaces changed

### Reference library

- `.tools/extract_hoi4_asset_references.py`
  - owns the allowlisted extraction and exact decoded-pixel validation;
  - emits the semantic tree, catalog, and one contact sheet per type;
  - places all normal flags under `flags/normal/`;
  - labels the flag sheet with `normal/`, `medium/`, and `small/` relative paths
    so same-basename flag ladder entries are unambiguous.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`
  - canonical semantic reference tree;
  - regenerated local contact sheets;
  - regenerated `CATALOG.md` with source type, exact source path, canvas, owning
    definition when available, and local review sheet;
  - updated `README.md` with the one-library and workflow-overlay rules.
- `.agents/skills/chaos-redux-event-assets/assets/README.md`
  - documents the canonical tree, identity-preserving portrait rules, flat flag
    rules, advisor separation, unit surfaces, and retained workflow inputs.

### Advisor package and tools

- `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`
  - validates provenance schema 4 and rejects event- or machine-specific
    dependencies;
  - pins and verifies the exact six canonical advisor reference names and
    SHA-256 hashes;
  - rejects a substituted event-specific reference directory;
  - requires the active manifest and both retained source-overlay pairs;
  - retains hard face, paper, frame, palette, alpha, silhouette, Jaccard, and
    row/column occupancy gates;
  - emits deterministic seed, render configuration, provenance, composition,
    and validation metadata.
- `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/advisor_dossier_overlay_manifest.json`
  - active schema-4 reusable manifest with two approved processing records and
    six canonical style-reference hashes.
- `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/v3/advisor_dossier_overlay_manifest.json`
  - retained full iteration/provenance manifest made portable by removing
    Event 015 package-copy fields, user-store roots, and absolute tool paths;
  - retains generated sources, prompts, alpha derivatives, and superseded
    iterations rather than deleting source evidence.
- `.agents/skills/chaos-redux-event-assets/tools/README.md`
  - documents the self-contained advisor invocation, pixel-equal DDS proof, and
    correct skill-local report-event processor path.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
  - makes the semantic reference tree authoritative;
  - keeps real-person sourcing, explicit head-and-shoulders crops, and
    identity-preserving HOI4 finishing mandatory;
  - keeps fictional portrait masters ImageGen-authored;
  - makes advisor/high-command icons independent 65x67 dossier compositions,
    never resized 156x210 portraits;
  - requires historical flag research followed by an ImageGen-created flat,
    orthographic flag reconstruction, never illustrative flag art;
  - removes reusable guidance that depended on an event package;
  - fixes report-event processor examples to the actual skill-local tool.

The DDS converter and report-event processor were preserved and functionally
probed; neither tool was deleted.

## Exact reference coverage

| Semantic family | References |
|---|---:|
| `portraits/leaders` | 8 |
| `portraits/commanders` | 5 |
| `portraits/operatives` | 5 |
| `portraits/advisors` | 9 |
| `flags` (normal, medium, small) | 21 |
| `event_art/report` | 5 |
| `event_art/news` | 5 |
| `event_art/super_event` | 5 |
| `icons/national_focus` | 16 |
| `icons/ideas` | 15 |
| `icons/decisions` | 15 |
| `icons/decision_categories` | 15 |
| `icons/missions` | 5 |
| `icons/achievements` | 18 |
| `icons/technologies` | 15 |
| `icons/special_projects` | 8 |
| `icons/balance_of_power` | 12 |
| `icons/officer_corps_spirits` | 5 |
| `icons/intelligence_agency` | 5 |
| `icons/intelligence_operations` | 5 |
| `icons/commander_traits` | 5 |
| `icons/medals` | 5 |
| `icons/military_raids` | 5 |
| `icons/state_modifiers` | 5 |
| `icons/military_industrial_organizations` | 5 |
| `icons/factions` | 5 |
| `icons/buildings` | 5 |
| `icons/modifiers` | 5 |
| `units/equipment/technology_art` | 5 |
| `units/land/counters_large` | 6 |
| `units/land/map_counters` | 5 |
| `units/land/division_template_emblems` | 5 |
| `units/air/map_counters` | 5 |
| `units/naval/map_counters` | 5 |
| `units/models_3d/land_materials` | 5 |
| `units/models_3d/air_materials` | 5 |
| `units/models_3d/naval_materials` | 5 |
| **Total** | **283** |

`assets/vanilla_reference/icons/achievements/overlay.png` is the retained
64x64 not-eligible compositing input. It is deliberately not counted as a
reference and is not placed on the achievement contact sheet.

## Duplicate and source-preservation audit

The migration has 99 tracked legacy PNG deletions.

- 90 have decoded-pixel-identical copies in the canonical semantic tree.
- 7 were obsolete broad contact sheets replaced by 37 per-type sheets:
  `event_art.png`, `icons.png`, `icons_extended.png`,
  `portraits_and_flags.png`, `units.png`, `units_expanded.png`, and
  `focus_reference_contact.png`.
- 2 were replaced by exact current-source extractions rather than retaining a
  degraded review copy:
  - old `the_revolution_triumphant.png` had slight RGB drift from the current
    authoritative vanilla source;
  - old `focus_GER_strengthen_the_waffen_ss.png` was an 86x85 crop, while the
    current vanilla source canvas is 100x88.

Four stale untracked files directly under `vanilla_reference/flags/` were
removed only after byte-for-byte comparison with their new `flags/normal/`
copies: `afg_second_empire_neutrality.png`, `anu_fascism.png`,
`arg_gen_nazism_party.png`, and `arm_uk.png`.

All advisor generated masters, prompt records, approved overlays, superseded
iterations, and v2/v3 provenance were retained. No source or distinct
iteration was deleted merely because it was not active.

## Final advisor calibration

The file changed concurrently during the audit. A transient version 4.3 state
set paper geometry to 25x30 at `(29,26)`, angle `-4.25`, and alpha thresholds
`128/200`; that state failed its own hard geometry gate with area 694 and a
measured top-edge angle of 8.785299 degrees. It was not accepted.
That external overwrite also marked the owned processor read-only; the
read-only attribute was cleared before the parent-authorized final patch.

The final version 4.3 state keeps the later grading additions while using the
geometry and opacity calibration that passes the complete gate:

| Setting | Final value |
|---|---|
| processor / advisor render / render schema | `4.3` / `4.3` / `v4.3` |
| frame size / position / angle | `40x58` / `(1,1)` / `5.0` |
| paper size / position / angle | `26x30` / `(30,25)` / `-3.0` |
| paper color / brightness | `0.85` / `1.15` |
| paper contrast / sharpness | `1.06` / `1.35` |
| paper RGB channel scale | `(0.886, 0.820, 0.839)` |
| paper outer/inner source-alpha thresholds | `32` / `36` |
| paper outer/inner/opaque mapped alpha | `224` / `250` / `255` |

Final processor SHA-256:
`c300a0acc6ca91beb98d5ae62fcb6c98ad61c39bb7c271491c761295ca11b411`.
Final render-configuration SHA-256:
`4d1b48b4c8e3535cff3f0bbe98fa91237282104dbe764a64940ecd61f52df6d1`.

## Meaningful validation evidence

### Library and skill

- `python -B .tools/extract_hoi4_asset_references.py --check`:
  `validated 283 references across 37 per-type contact sheets`.
- All 283 managed reference paths exist and match their declared source pixels;
  all 37 contact-sheet paths exist.
- Official skill validation:
  `Skill is valid!`.
- Both advisor manifests parse as schema 4. Their declared local paths exist;
  no manifest value contains an absolute user path, generated-image store
  dependency, `event_package_copy`, or Event 006/Event 015 package path.
- Project-root `assets/`, `assets/leader_portraits/`, and
  `assets/advisor_icons/` do not exist; no textual references to the two stale
  portrait paths remain.
- The full flag contact sheet now distinguishes all three ladder sizes in its
  labels. Portrait, advisor, focus, idea, decision, flag, unit, report, news,
  and super-event sheets were visually inspected.

### Advisor processor

The practical self-test used the canonical 156x210 Thorvald Stauning leader
reference as a real-person portrait master, an explicit full source crop,
explicit face bounds, the active manifest, both retained v3 sources, and both
retained v3 overlays. This validates the processor without adding runtime art.

- Two clean runs produced byte-identical PNG files:
  `07115e5abca8d065344f9670613f38538bcee3c40b3e03812dc17296e135c463`.
- The metadata pinned all six canonical advisor references.
- Candidate paper geometry:
  - bbox `[30,25,58,57]`;
  - area `721`;
  - center `[43.110957,41.080444]`;
  - measured top-edge angle `5.098153` degrees.
- Candidate paper palette:
  - mean luminance `206.37331`;
  - mean saturation `0.227646`;
  - mean RGB `[221.970874,205.380028,171.610264]`.
- Candidate paper opacity:
  - minimum/maximum alpha `250/255`;
  - mean alpha `254.715673`;
  - fully opaque ratio `0.943135`.
- Final alpha envelope:
  - bbox `[2,1,63,65]`;
  - centroid `[29.857007,33.651871]`;
  - minimum all-reference Jaccard `0.926852`;
  - row occupancy MAE `0.026598`;
  - column occupancy MAE `0.044432`.
- The review sheet was inspected at native and enlarged size; the portrait,
  dark irregular frame, pale dossier paper, scale, and transparent corners read
  consistently with the six-reference family.
- DDS export is `65x67`, begins with `DDS `, contains one uncompressed BGRA
  surface, and decodes pixel-for-pixel identically to the PNG. The shared
  decoded RGBA SHA-256 is
  `e44962ea97e3a13833eecfe734fff04425886aa8cae69a1c1f719b40d22fe9eb`.

The metadata status remains `candidate_requires_visual_approval` by design;
the self-test is evidence that the reusable processor works, not a request to
ship the Stauning test card as a runtime asset.

## Simplifications, omissions, and blockers

No simplifications or fallbacks were used. No requested reference family,
processor dependency, manifest check, or preservation check was omitted.

There are no blocking defects in this scope. Super-event references include
explicitly labeled Chaos Redux review copies because vanilla has no equivalent
super-event asset surface; their provenance is not presented as vanilla.

## Skills used

- `chaos-redux-event-assets`
- official `skill-creator`
- `chaos-redux-subagents`

No files were staged or committed by this subagent.
