# Chemical and biological technology folder repair (10 Oct 2026)

Disposition: implemented. Scope: the chemical warfare and biowarfare research folders, their cards, their art, and their localisation.

## Before

The two folders used `format = "UP"` gridboxes with `slotsize = { width = 90 height = 50 }`, all seven chemical branches sharing one origin at x = 110, y = 160.

- Connector lines broke. The engine draws a path from `techtree_line_item` with 36-pixel segments built for a 70-pixel slot, so a 90-pixel column left a gap in every horizontal link and a 50-pixel row left the vertical links short.
- Branch labels sat in a 98-pixel gutter that ended at x = 106, four pixels before the first 72-pixel card, and the 1918 and 1936 columns were one slot apart, so the first cards crowded the labels.
- Rows did not match their labels. Nerve agents were at row 2 and blister agents at row 4, while the mustard to lewisite link ran across the row the nerve label named.
- Card art was inconsistent. The three Livens projector cards used the 94x45 equipment painting inside a 72-pixel card, and the seven agent cards all reused one green cylinder painting with a different coloured band.
- Six project technologies (four bomb delivery systems, sarin, soman) had `allow = { always = no }` and no folder entry, so the biological folder showed eight cards in a 1300x800 area and the chemical nerve row ended after tabun.

## After

- Both folders use the vanilla grid: `format = "LEFT"`, `slotsize = { width = 70 height = 70 }`, one gridbox per branch. Branch gridboxes start at x = 170, the first row at y = 190, and each later row 100 pixels lower. Year columns are two slots (140 pixels) apart, which is what the connector segments are drawn for.
- Chemical rows are choking, blister, nerve, projectors, protection, detection, decontamination; columns are 1918, 1936, 1937, 1939, 1940, 1941, 1942. Biological rows are munitions, containment, surveillance, medical; columns are 1936, 1938, 1940, 1941.
- Branch labels are right-aligned in the 170-pixel gutter and end ten pixels before the first card. Year headers sit ten pixels left of their own column at y = 50, as in the vanilla infantry folder.
- Every card chain is drawn by `path`. Tabun now paths to sarin and sarin to soman, so the nerve line is continuous instead of relying on invisible dependencies.
- The six project technologies are visible locked cards with `allow = { ROOT = { is_special_project_completed = sp:<project> } }`, `is_special_project_tech = yes` and zero research weight, following the vanilla `jet_fighter1` pattern. This also puts the already registered special-project card backgrounds to use.
- All card art is 64x64. New paintings replace the shared cylinder for chlorine, phosgene, mustard, lewisite, tabun, sarin and soman, and the three Livens cards get their own 64x64 art while the 94x45 paintings stay with the Livens equipment sprites.
- Content fillers are sized to the content: 1140x920 chemical, 960x715 biological.

## Geometry evidence

`hoi4.tech_render` `view = folder`, source-accurate, after the change:

- chemical_warfare_folder: 21 cards, columns at x = 167, 307, 447, 587, 727, 867, 1007 and rows at y = 315, 415, 515, 615, 715, 815, 915 in renderer coordinates (the renderer offsets the folder origin). Card boxes are 72x72, so every gap is 68 pixels horizontally and 28 vertically. Pairwise overlap count: zero. No unresolved icon sprite.
- biowarfare_folder: 12 cards, columns at x = 167, 307, 447, 587, rows at y = 315, 415, 515, 615. Pairwise overlap count: zero. No unresolved icon sprite.

`hoi4.gui_render` for `chemical_warfare_folder` at 1920x1080 and 2560x1440, UI scale 1: the rebuilt chrome draws with no missing reference of its own. Its overlap findings are the folder's own full-size filler container against each label, which is the vanilla nesting pattern, and the one blocking reference is the vanilla `GFX_prod_progress_bar3` progress bar that the index does not resolve; both are unchanged by this work.

## Not verified

The GUI renderer does not draw native technology cards, tooltips or scrolling, so in-game scroll reach, card tooltips, the locked-card tooltip text for the project technologies, and final DDS appearance are left to live play.

## Second pass, same day: card size and link length

The first pass kept `force_use_small_tech_layout = yes` on every CBRN technology, so all 33 cards drew in the 72-pixel doctrine box with no name, and the two-slot column pitch produced links of up to nine slots.

- Every technology placed in either folder lost `force_use_small_tech_layout`. The engine now applies the vanilla rule: a technology that unlocks equipment draws the full-size named card, everything else draws the small box. Chemical: 20 full-size cards and Dimercaprol small. Biological: the four bomb cards full-size, the eight service technologies small.
- The column pitch went from two slots (140 pixels) to three (210 pixels), which is the room the 183-pixel card needs; vanilla never places two full-size cards closer. The grid origin moved from x = 170 to x = 220 so the gutter labels stay clear of the card's left edge at x = 164, and the row pitch went from 100 to 110 pixels so the 84-pixel cards keep a gap.
- The 1937 column was removed. Lewisite and tabun are 1936 research and Rapid Decontamination Plants is 1941 research, so every branch advances one column per step and the longest link in either folder is two columns (420 pixels), the same as the longest vanilla support-folder link. Before this, Improved Service Masks to Advanced Protective Clothing and the matching projector link spanned 630 pixels.
- Fillers resized to 1450x980 (chemical) and 1040x715 (biological).

Render evidence after the second pass, from `hoi4.tech_render view = folder`: chemical columns at renderer x = 217, 427, 637, 847, 1057, 1267 and rows at y = 315, 425, 535, 645, 755, 865, 975; biological columns at 217, 427, 637, 847 and rows at 315, 425, 535, 645. Card boxes are 183x84 (full-size) and 72x72 (small), pairwise overlap count zero in both folders, no unresolved icon sprite, and the per-row maximum column gap is 420 pixels. `hoi4.gui_render` at 1920x1080 and 2560x1440 shows the six year headers and seven branch labels inside the window with no clipping.

## Current correction: preserved artwork and card name binding (11 Oct 2026)

This correction supersedes the earlier art-redesign claims above: this repair preserves the original artwork, including the existing 64x64 gas-agent card art. The Livens projector equipment and technology sprite mappings in `interface/chaosx_equipment.gfx` point to the original `livens_projector.dds`, `livens_projector_improved.dds` and `livens_projector_advanced.dds` files. Geometry remains at 70x70 slots, regular-card size 183x84, offsets x=-56/y=-7, origin x=220, 210-pixel column pitch and 110-pixel row pitch.

Both custom full-size templates now name the `instantTextBoxType` child `Name`, matching the vanilla case-sensitive binding (`interface/countrytechtreeview.gui`, vanilla line 4251). The prior lowercase `name` could prevent title text from binding. Parent live-game verification is pending; inspector and renderer geometry evidence do not verify native card drawing, title display, tooltips or scrolling.
