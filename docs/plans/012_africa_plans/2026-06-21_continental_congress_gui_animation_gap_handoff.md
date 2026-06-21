# Event 012 Africa Continental Congress GUI/Animation Gap Handoff

Date: 2026-06-21

Scope: documentation-only reconciliation for the Continental Congress scripted GUI and animated asset status.

This handoff does not claim live render proof, Event 012 completion, or prompt-equivalent asset completion. It records the current evidence and queues the missing prompt-named GUI/static/animated asset families.

## Source-of-Truth Map

| Surface | Current source |
| --- | --- |
| Accepted asset prompt requirements | `docs/specs/012_africa_specs/prompts/012_africa_asset_prompt.md` |
| Current live asset ledger | `docs/assets/012_africa/implementation_asset_manifest.md` |
| Current Event 012 source-of-truth ledger | `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md` |
| Foundation addendum disposition | `docs/plans/012_africa_plans/2026-06-20_foundation_addendum_disposition.md` |
| Static GUI/animation wiring audit | `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_gui_animation_static_wiring_audit_handoff.md` |
| Older completion-audit evidence for named animation gap | `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_012_africa_completion_audit_handoff.md` |

## Current Evidence

The current wired Continental Congress visual strip is useful and live-wired. It includes:

- `GFX_africa_authority_atlas_seal_loop`, 4 frames, with `GFX_africa_authority_atlas_seal_static`.
- `GFX_africa_charter_league_banner_pulse`, 4 frames, with `GFX_africa_charter_league_banner_static`.
- `GFX_africa_bestiary_warning_loop`, 4 frames, with `GFX_africa_bestiary_warning_static`.

Read-only evidence checked:

- `interface/012_africa.gfx` registers exactly those three `frameAnimatedSpriteType` sprites in the Event 012 animated strip.
- `interface/012_africa_scripted_gui.gui` places exactly those three animated overlay sprites, with matching static fallbacks, in the Continental Congress panel.
- `docs/assets/012_africa/implementation_asset_manifest.md` lists the same three wired frame sheets and the same static fallbacks.
- `2026-06-20_012_africa_gui_animation_static_wiring_audit_handoff.md` verifies static wiring, sprite registration, final DDS dimensions, and visibility hooks, while explicitly saying it does not replace live in-game render proof.

## Status Conclusion

The current visual strip is accepted only as a partial, useful wired presentation layer. It is not accepted as the full `012_africa_asset_prompt.md` scripted-GUI/animation package unless a later file proves the prompt-named families were implemented, wired, manifest-documented, and live-render-validated.

The current wired strip is also not a substitute for live render/readability proof. Static wiring proof means the controls, sprites, DDS files, and visibility hooks line up; it does not prove in-game z-order, animation playback, hover readability, or readability across route states.

## Queued Missing Prompt-Named GUI Families

The asset prompt still queues the following Continental Congress UI families unless later evidence proves them present:

| Prompt family | Required disposition |
| --- | --- |
| Background panel | Queue final static DDS/source package, sprite registration, GUI placement, manifest row, and live screenshot proof. |
| Header plate | Queue final static DDS/source package, sprite registration, GUI placement, manifest row, and live screenshot proof. |
| Meter frames and fills | Queue Legitimacy, Authority, Cohesion, Momentum, Regional Trust, Colonial Alarm, Paper-Core Burden, and Covenant Pressure meter frame/fill families with GUI state proof. |
| Regional authority cards | Queue neutral, protected, integrating, rebellious, and integrated card states with GUI placement and live state proof. |
| Selected target frame | Queue selected region/member/dossier target frame or documented accepted equivalent with live state proof. |
| Cohesion/rebellion warning border | Queue static fallback plus prompt-named animation package below. |
| Charter seal states | Queue locked, available, active, and formed states unless mapped by explicit evidence to current sprites. |
| Green Covenant seal states | Queue hidden, revealed, active, and critical states unless mapped by explicit evidence to current sprites. |
| Formable progress emblem | Queue incomplete, ready, and formed states unless mapped by explicit evidence to current sprites. |
| Static fallbacks | Queue static fallback DDS and manifest row for every animated prompt element. |

## Queued Missing Prompt-Named Animated Packages

| Prompt animation | Prompt expectation | Current evidence | Disposition |
| --- | --- | --- | --- |
| `africa_charter_seal_animated` | 64x64 or current GUI size, 8-12 real frames, slow glow/float, static fallback `GFX_africa_charter_seal` | No matching sprite name found in current checked docs/GFX. Current Charter strip is `GFX_africa_charter_league_banner_pulse`, 4 frames, banner-shaped. | Queued. Do not mark complete from the current banner pulse alone. |
| `africa_cohesion_warning_border_animated` | Target GUI card size, 6-10 real frames, warning pulse, static fallback | No matching sprite name found in current checked docs/GFX. Current warning strip is `GFX_africa_bestiary_warning_loop`, 4 frames, 96x96 seal/icon. | Queued. Do not mark complete from the Bestiary warning icon alone. |
| `africa_green_covenant_seal_animated` | 64x64 or UI size, 10-16 real frames, storm/river/tree glow, static fallback | No matching sprite name found in current checked docs/GFX. Current strip has no prompt-named Green Covenant seal animation. | Queued. |
| `africa_formable_ready_emblem_animated` | Target UI emblem size, 8-12 real frames, availability glow, static fallback | No matching sprite name found in current checked docs/GFX. Current strip has no prompt-named formable-ready emblem animation. | Queued. |

For each queued animation, acceptance requires source frames, processed frames, sheet PNG, sheet DDS, static fallback DDS, preview GIF for review only, contact sheet, manifest entry, `.gfx` handoff, final sprite registration, GUI placement or explicit non-GUI use path, and live render/playback evidence.

## Unresolved Plan and Handoff Disposition Table

| File | Disposition |
| --- | --- |
| `docs/specs/012_africa_specs/prompts/012_africa_asset_prompt.md` | Current accepted asset requirement source. Leave unchanged. |
| `docs/assets/012_africa/implementation_asset_manifest.md` | Current live asset manifest. Patched to distinguish the useful three-sprite visual strip from the missing prompt-named package. |
| `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md` | Current status ledger. Patched to point to this handoff and state that prompt-equivalent GUI/animation remains queued. |
| `docs/plans/012_africa_plans/2026-06-20_foundation_addendum_disposition.md` | Patched so the GUI/animation row no longer reads as a mere undecided equivalence question; the missing prompt-named families are queued unless explicitly accepted later with evidence. |
| `2026-06-20_012_africa_gui_animation_static_wiring_audit_handoff.md` | Leave unchanged. It is valid static wiring evidence for the current strip, not prompt-equivalent completion. |
| `2026-06-16_012_africa_completion_audit_handoff.md` | Leave unchanged. Its named-animation gap remains useful evidence, though many unrelated findings are stale after later tranches. |
| `2026-06-18_012_africa_gui_selected_target_cards_parent_handoff.md` | Leave unchanged. It improves selected-target readability but explicitly does not implement full scrollable region/member/dossier card lists or live screenshot validation. |

## Contradiction List

| Files | Evidence | Resolution |
| --- | --- | --- |
| `012_africa_asset_prompt.md` vs `implementation_asset_manifest.md` | The prompt requires background/header/meters/regional cards/warning border/seal states/formable emblem plus four named animations with 6-16-ish frame expectations. The manifest lists three wired 4-frame strip animations with different names and roles. | Resolved in docs by treating the current strip as partial and queuing the prompt-named families. |
| `CURRENT_SOURCE_OF_TRUTH.md` vs prompt status | The source-of-truth says the remaining UI blocker is live render/animation proof, which could be read as saying the prompt-named package itself is otherwise complete. | Resolved in docs by adding an explicit prompt-equivalence gap statement and pointer to this handoff. |
| `foundation_addendum_disposition.md` recommendation vs parent-observed evidence | The ledger asked the parent to decide whether the current fixed panel is accepted as equivalent. The checked files do not prove prompt-equivalent GUI/static/animated coverage. | Resolved in docs by defaulting to queued follow-up unless a later parent decision and evidence accepts a narrower equivalent. |

## Duplicate or Superseded Document List

- No files were deleted or archived.
- Older handoffs that say the current visual strip narrows the GUI/animation gap remain useful, but they are superseded by this handoff for prompt-equivalence status.
- The static wiring audit remains current for its narrow scope and is not superseded.

## Stale Prompt or Stale Instruction List

- Any instruction or handoff that treats the current Charter/Authority/Bestiary visual strip as closing the full asset prompt is stale unless it names the four prompt animations and provides implementation, manifest, and live render evidence.
- Any instruction that reduces the remaining GUI/animation blocker to live render proof only is incomplete; live proof is still required, but prompt-named GUI/static/animated asset families also remain queued.
- The asset prompt itself is not stale for this surface. It remains the accepted requirement source until the parent explicitly revises it.

## Acceptance Evidence Needed To Close

To close this gap later, the parent needs one of two evidence paths:

1. Full prompt implementation evidence: prompt-named static and animated families exist, are registered, are placed or otherwise used by the Continental Congress UI, have manifest rows, and have live render/playback proof.
2. Explicit parent-approved equivalence decision: a later documentation file states which current or replacement sprites intentionally satisfy each prompt family, why the narrower design is accepted, which prompt items are rejected or out of scope, and what live proof validates the accepted design.

Neither path exists in the checked files.

## Patch Handoff

Files changed by this documentation reconciliation:

- `docs/plans/012_africa_plans/2026-06-21_continental_congress_gui_animation_gap_handoff.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/assets/012_africa/implementation_asset_manifest.md`
- `docs/plans/012_africa_plans/2026-06-20_foundation_addendum_disposition.md`

Disposition changes:

- Promoted: none.
- Implemented: none.
- Queued: prompt-named Continental Congress GUI/static/animated asset families listed above.
- Rejected: none.
- Superseded: broad readings of the current three-sprite strip as prompt-equivalent completion.
- Left unchanged: asset prompt requirements, static wiring audit, older completion-audit evidence.

Validation checks run:

- `rg` for the four prompt animation names across `docs/specs/012_africa_specs`, `docs/plans/012_africa_plans`, `docs/assets/012_africa`, `interface/012_africa.gfx`, and `interface/012_africa_scripted_gui.gui`.
- `rg` for current strip sprite names and `frameAnimatedSpriteType`.
- Targeted reads of the asset prompt, implementation manifest, source-of-truth ledger, foundation disposition ledger, GUI static wiring audit, completion audit, selected-target-card handoff, and relevant `.gfx`/`.gui` lines.

Skipped validation:

- No gameplay, localisation, GFX, GUI, spreadsheet, or asset binary files were edited.
- No live HOI4 render proof was run or claimed; this pass only reconciles documentation.

Remaining risks:

- A later unsearched file outside the checked Event 012 docs/GFX/GUI surfaces could claim a parent-approved equivalence decision. No such decision was found in the targeted checks.
- The current three-sprite strip may remain valuable and should not be removed by this documentation status alone.
- Future implementation should avoid renaming already wired sprites unless the new prompt-named package is deliberately wired and documented.
