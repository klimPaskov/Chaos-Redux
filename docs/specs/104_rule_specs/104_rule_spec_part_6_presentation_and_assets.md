# Event 104 Rule: presentation and assets

## Presentation purpose

Rule must be understood quickly as a real change to the campaign's current rules.
The main report names what changed and gives enough practical meaning for the player to reassess their next action.
The ordinary diplomacy and campaign interfaces provide the detailed consequences where the player uses them.
The existing event history preserves the sequence of changes.

All player-facing text in this package is direction only.
The existing user-provided event and evolution names identify the design.
New working labels are not final localisation.
Do not copy a planning paragraph into an event description or tooltip as finished text.

## Report contract

The main report is the existing native country-event report presentation with one acknowledgement.
The gameplay change is committed before it opens.
The acknowledgement has no gameplay effect.
Its tooltip can explain the committed consequences but cannot promise an option the player has not actually received.

| Element | Required writing direction |
| --- | --- |
| Title | Identify Rule or the applicable scale of this occurrence plainly. Avoid implying a responsible state or negotiator. |
| Description | Briefly establish that the campaign's operating rules changed, then identify the actual committed transitions. |
| Rule row | Display the actual localised native rule name, old option, and new option. Use a clear directional separator appropriate to the existing UI. |
| Consequence | Explain the changed class of action or behaviour in concrete terms, including the affected country for a country-specific AI rule. |
| Acknowledgement | Convey recognition and continued play. Do not imply consent, a veto, or a second application. |
| Effect tooltip | Describe the verified result, persistence, and any important existing-object limitation for the selected transition. |
| Partial success | State the actual number of rules changed. Explain only a player-relevant omission, without exposing internal debugging text. |
| Unavailable manual request | Explain that no compatible meaningful rule change was available, through the shared failure receipt. Do not present a normal successful Rule report. |

The report must support one through eight committed transitions.
Long localised rule and option names must be tested at the shared report's supported resolutions and UI scales.
The complete list can use the normal description and existing tooltip space, but no committed row may disappear through clipping.
If the existing consumer cannot display the required information accurately, presentation remains an implementation blocker until an appropriate shared-surface solution is reviewed.
Do not introduce a permanent Rule window to avoid the constraint.

## History and Event Details

One successful Rule occurrence creates one ordinary event-history entry with an immutable result payload.
Its detailed content can list multiple transitions.
The history must distinguish fresh changes from revisions and preserve their actual dates and sequence.
It does not need to treat each changed rule as another randomly fired event.

The global event uses no invented actor.
For a country-specific rule, the affected country is named as a subject where useful.
The executor's flag must not imply that it caused the world's rules to change.
Country loss or a later tag presentation change cannot erase the earlier rule identity or destination meaning.

Event Details gives the premise and persistence of Rule.
It should explain that later firings can build an unusual rule set and that evolutions change how many rules can change and whether earlier rules can return to the pool.
It is not a duplicate of the full coding contract or a long list of every possible native option.
Unavailable implementation state displays the shared N/A treatment, not a misleading ordinary zero weight.

## Evolution presentation

Each evolution has a preview in Event Details and a dated history entry only when it actually activates.
The preview describes its own capability, including the independent toggle semantics from Part 3.
The activation notice makes clear that the event's capabilities changed.
It must not claim that a native rule changed at that moment unless a separate verified Rule occurrence also did so.

The same stage identity, title direction, threshold, and capability must agree across global history, selected-event history, and Event Details.
Preview rows do not use fake dates or fabricated history sequence numbers.
Disabled stages are not silently marked recorded.

## Voice and information hierarchy

Use direct, concrete prose with a restrained period tone.
The event is strange because its rules change, and that fact does not need a second supernatural explanation or an invented official conspiracy.
Avoid generic declarations about a world transformed forever, theatrical denial, bureaucratic filler, and terminology taken from the implementation process.

Lead with the actual result.
Keep the rule name and destination easy to locate.
Explain persistence once and describe a special limitation only when it affects a player's meaningful decision.
Do not reveal hidden achievement conditions in the occurrence report.
Do not call a blocked attempt a partial success unless at least one native transition really committed.

Use integer formatting for counts.
Use the native option's localised name rather than exposing its internal enum token.
If a localisation key is missing, the candidate cannot be considered presentation-complete.
Do not ship a raw key as an acceptable Rule label.

## Asset set

The submitted presentation design needs one report illustration and three achievement subject designs.
The achievement state derivatives bring the runtime total to ten DDS textures.
No generated assets are delivered by this planning task.
The separate asset prompt describes the production and validation work.

| Asset ID | Consumer | Final dimensions | Proposed sprite or basename | Runtime path |
| --- | --- | --- | --- | --- |
| ART104-01 | Native occurrence report | 210 × 176 | `GFX_report_event_104_rule` | `gfx/event_pictures/104_rule/104_rule_report.dds` |
| ART104-02 | A01 completed achievement | 64 × 64 | `chaosx_rule_adaptation` | `gfx/achievements/chaosx_rule_adaptation.dds` |
| ART104-03 | A01 grey state | 64 × 64 | `chaosx_rule_adaptation_grey` | `gfx/achievements/chaosx_rule_adaptation_grey.dds` |
| ART104-04 | A01 not-eligible state | 64 × 64 | `chaosx_rule_adaptation_not_eligible` | `gfx/achievements/chaosx_rule_adaptation_not_eligible.dds` |
| ART104-05 | A02 completed achievement | 64 × 64 | `chaosx_rule_coalition` | `gfx/achievements/chaosx_rule_coalition.dds` |
| ART104-06 | A02 grey state | 64 × 64 | `chaosx_rule_coalition_grey` | `gfx/achievements/chaosx_rule_coalition_grey.dds` |
| ART104-07 | A02 not-eligible state | 64 × 64 | `chaosx_rule_coalition_not_eligible` | `gfx/achievements/chaosx_rule_coalition_not_eligible.dds` |
| ART104-08 | A03 completed achievement | 64 × 64 | `chaosx_rule_cascade_victory` | `gfx/achievements/chaosx_rule_cascade_victory.dds` |
| ART104-09 | A03 grey state | 64 × 64 | `chaosx_rule_cascade_victory_grey` | `gfx/achievements/chaosx_rule_cascade_victory_grey.dds` |
| ART104-10 | A03 not-eligible state | 64 × 64 | `chaosx_rule_cascade_victory_not_eligible` | `gfx/achievements/chaosx_rule_cascade_victory_not_eligible.dds` |

The sprite and basenames are proposed new identifiers.
Check current consumers and collisions before final wiring.
The parent owns runtime `.gfx` registration and achievement binding.
Asset workers own their requested source imagery, processing, and evidence within their bounded handoff.

## Report illustration direction

Use a fictional documentary photograph of a late-1930s international road checkpoint where an ordinary convoy is being redirected under a newly changed access arrangement.
Place a period barrier and a border guard in the foreground, with a small line of period civilian and diplomatic vehicles beyond.
The action should be readable at report size and should suggest that ordinary movement now follows a different instruction.
Keep the scene calm enough for the low-Chaos baseline and broad enough to serve later multi-rule firings.

The image should look like a plausible period photograph, with coherent material detail, restrained contrast, and a clear central action.
It must not depict modern uniforms, vehicles, cameras, road markings, traffic signs, or office equipment.
Avoid readable signs, generated writing, exaggerated gestures, fantasy portals, floating symbols, game interfaces, a map full of arrows, and a generic crowded war room.

Generate or source the full photographic scene first.
Do not ask the image model to paint the final report card, border, transparency shape, labels, or folded-paper frame.
The current event-assets report processor creates the final 210 by 176 sepia documentary-card treatment and transparent edges.
Use the current owner workflow and reference family rather than inventing a report frame or assuming an additional template file exists.

## Achievement art direction

The three subjects must remain distinguishable at 64 by 64 pixels.
A01 uses a redirected field compass and a small metal star.
A02 uses five linked metal fittings with a repaired joint.
A03 uses a battered book clasp, shifted tabs, and a small campaign laurel.
Use one clear central silhouette per icon and a consistent period material treatment.

Generate each original achievement subject through native ImageGen with real transparent unused canvas in the initial request.
Preserve alpha through edits, processing, template composition, resizing, and DDS conversion.
Background removal is a documented fallback after failed native alpha or for an inherited opaque source under the current event-assets skill.
Preserve the exact achievement frame and overlays from the reference assets.
Produce grey and not-eligible states through the prescribed deterministic treatment.
Do not independently regenerate the three states and introduce inconsistent silhouettes, framing, or damage.

## Reference and evidence contract

Use the current owning event-assets skill and its canonical reference root:

`.agents/skills/chaos-redux-event-assets/assets/gfx_references`

Inspect the report family under `event_art/report` and the achievement family under `icons/achievements` before production.
Record the exact reference files actually used.
The planning task read the asset instructions but did not inspect those image files or claim visual matching.
The production handoff must retain source provenance, actual tool route, accepted candidate lineage, processing steps, PNG previews, final DDS paths, and the final consumer mapping.

For an AI-created source, record the actual exposed generation tool and reported model information.
Do not claim a named backend if the available route does not expose or confirm it.
For a sourced historical image, record its source URL and rights evidence.
The fictional checkpoint direction does not require representing a real photographed event.

## Visual acceptance

Compare the report preview against the canonical report references at the actual final size.
Check the image's central action, sepia treatment, card shape, alpha edges, and absence of generated writing.
Inspect each achievement completed and derivative state at 64 by 64 pixels and in the actual achievement UI.
Decode the final DDS files back into a viewable image and verify that conversion did not damage colour, alpha, dimensions, or template alignment.

Render the main report with one short transition and with eight long transitions.
Render the shared history detail for the same immutable receipts and each evolution preview and recorded entry.
Check the standard supported resolution and a constrained supported resolution, including the UI scale that produces the worst wrapping.
Tool rendering and engine observation must be reported separately.
A successful render call without inspection is not visual acceptance.

## Catalog wording

The final catalog's short description and Details must match their designated in-game text exactly where the workbook contract requires mirrored fields.
The parent finalises localisation first.
The spreadsheet worker then updates the authoritative XLSX and regenerates all CSV exports.
The worker does not invent gameplay readiness or paraphrase approved in-game wording to fit the sheet.
Catalog conflicts involving older IDs and Randomizations membership remain explicit until the actual workbook and current registration are reconciled.
