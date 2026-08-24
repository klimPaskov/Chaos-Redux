# Source-to-refinement comparison

- Source: `refs/source/recovery_v7/candidates/conan_fashion_contest_painted_archer.png`, SHA-256 `8AEB254BA8D7BF61F35439D037E84EC4FB205610C10FE458ABADE9D7E76BAED6`.
- Refinement: `refs/original/meshy_input.png`, SHA-256 `3A0F19C7329FD433C538F6D1BCE3A97C5CDE72EBEF52B3D5270AA151E41C740A`.
- Visual comparison: `refs/derived/source_to_refinement_comparison_v8.png`, SHA-256 `B5343605993175091236EDCA8C4BF76FBB07C0720FA72F60D2D5333CC658BCF3`.
- Preserved: face and body identity, crouched pose, gaze, braided hair, facial and body paint, physique, bow, bowstring, arrow, quiver and arrow bundle, bracers, necklaces, lower clothing, palette, and overall silhouette.
- Approved additions: one small sheathed bone close weapon and restrained bone or tooth trophies.
- Approved moderation-only change: minimal distressed leather or hide chest wrap; it is not armor and does not modernize the design.
- Source limitation: the archived landscape image clips the lower legs at the bottom edge. The refinement completes the boots while preserving the visible stance; this completion is explicitly disclosed rather than treated as source-visible geometry.
- Removed: sky, trees, terrain, cast shadow, and the extra lower-left figure.
- Alpha route: both native ImageGen attempts returned baked checkerboard RGB. Installed `rembg 2.0.61` post-processed masking supplied the fallback alpha; the retained boundary-only processor removed or decontaminated neutral-white fringe without editing interior subject pixels.
- Cultural review: no new sacred motif, living-community marker, ethnographic element, modern equipment, knight armor, or cultural label was added.
- Approval status: `needs_parent_visual_approval_before_meshy`.
