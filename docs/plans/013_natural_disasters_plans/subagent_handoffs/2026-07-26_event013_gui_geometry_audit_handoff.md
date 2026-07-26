# Event 013 direct GUI geometry audit handoff

Date: 2026-07-26
Mode: bounded direct-interface audit and source patch
Scope: `natural_disaster_abnormal_path_window` only

## Finding and correction

The prior targeted HOI4 MCP layout artifact `natural_disaster_abnormal_path_window-layout.json` reported 17 intersecting clickable-region pairs at the supported review resolutions. The intersections came from legacy clickbox sizes that no longer matched the declared scaled sprites after the direct Event 013 window was expanded with the family header and eight-item legend.

The source correction is in `interface/013_natural_disasters.gui`.

- Sequence navigation now uses 86x28 hitboxes at x=810 and x=910.
- Each of the five family cards now uses a 232x102 hitbox, matching the 0.83-scaled card frame and leaving a two-pixel vertical gap between cards.
- Previous, locate, and next path controls now use 80x28 hitboxes with five-pixel horizontal gaps.
- The six milestone controls remain 48x48 and no longer intersect the reduced family-card rectangles.

An independent bounded source-coordinate parser enumerated 25 button regions and found zero pairwise overlaps after the correction. The parser check is a source-level geometry proof; it does not replace an engine render.

## MCP status

A fresh `hoi4.gui_inspect`/`hoi4.gui_render` pass completed at 1280x720, 1920x1080, and 2560x1440/1.25 across twelve states at source revision `2452b17255026c63b7d59f61594eec80bbea9fc3fcc8374acc3e06c2e890063`. The offline renderer reports four card-3/milestone intersections only because it multiplies source offsets by each control's `scale`; the offline wiki contract and vanilla `airselectionview.gui` precedent define scale as button-size scaling with unscaled screen positions. The independent raw-source parser reports zero overlaps, and the fresh direct scene reports no element-level long-text overflow or clipping; close-button shader and DDS decoding warnings are renderer limitations. The live engine scenario matrix remains separately queued, and no GUI or gameplay fallback was introduced.

## Boundary confirmation

This audit did not modify `interface/chaosx_super_events.gui`, `common/scripted_guis/chaosx_scripted_gui_super_events.txt`, `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, or the shared super-event localisation. The Event 013-owned delta for those shared/general surfaces remains byte-identical to the pre-Event 013 baseline; unrelated Brilliant Scientist/Rat King working-tree edits in two shared scripted files were preserved and are outside this audit.

## Validation and remaining risk

The direct source graph still resolves the Event 013 family header, state-driven marker cards, animation/static pairs, footer controls, and legend assets without GIF gameplay references. The remaining validation risk is the offline renderer's documented scale-offset false positive and the user-owned live HOI4 matrix; the current source patch is not described as an unconditional engine proof.
