# Produce the Event 077 visual assets

Read all presentation and relevant gameplay parts in `docs/specs/077_parliament_of_fear_specs/`, especially Parts 2, 6, 7, 9, 10, and 12. Read the complete event-assets, frame-animation, scripted-GUI, portrait/ComfyUI, and relevant country-flag skills. Follow `supporting_material/077_asset_manifest.csv` and its notes.

The manifest has 48 production records covering ten report compositions, two news compositions, four action icons, three idea icons, chamber state and overlay art, warning animation and static state, the severe-outcome super-event image, eight achievement triplets, and conditional real-portrait and successor-flag roles. Conditional roles are not a request to invent people or countries.

Inspect existing assets and build native-family contact sheets before generation. Keep report 210x176, news 397x153, decision 32x32, idea 64x64, achievement 64x64, and super-event 457x328 families separate. Use the actual relevant leader or adviser portrait family. News receives a separate monochrome composition, not a stretched report image.

Create an approved in-game chamber reference before producing its exact native parts. Measure the host category and record every element's bounds, font, state, hitbox, clipping and scrolling behavior. GUI dimensions marked REFERENCE_GATED in the manifest are unresolved until that work is complete. Do not guess them from a browser screenshot.

The visual state model separates support base, occupancy state, and accusation overlay. A loyal accused seat must communicate both facts. Vacancy has a distinct empty shape. Protection, suspension, cleared evidence, selection, and hover remain readable without depending solely on color. Do not bake values, labels, country names, or case text into background art.

The warning sequence needs actual authored frames, a documented sheet layout, and an equivalent static fallback. It is brief and tied to an actual state change. A brightness pulse over a still picture is not the required frame-animation output. Provide native frame contact sheets and a review preview in addition to runtime assets.

Reports use fictional neutral institutional scenes unless a grounded country-specific source is necessary and verified. Avoid modern items, inaccurate national insignia, invented readable documents, and misleading depictions of actual historical arrests. Serious purge imagery should communicate absence and disruption without celebratory or sensational treatment.

Reuse existing real portraits first. New portraits require a named actual figure, verified relevant role, and source likeness. Never generate a face and present it as an unidentified historical minister. Abstract groups use institutional symbols. Leader and adviser consumers receive separate appropriate preparation.

Each achievement has one original native icon and the dedicated pipeline's grey and exact not-eligible variants. Use flat `gfx/achievements/<achievement_id>.dds`, `<achievement_id>_grey.dds`, and `<achievement_id>_not_eligible.dds` paths. Inspect the actual processor and overlay templates before conversion. Do not make three independent generated images.

A successor flag is conditional on a verified actual outcome identity. Reuse existing valid flags before adding new ones. Any new flag needs source-grounded geometry and all native size variants. Do not invent an ideology flag simply to fill a folder.

Read the actual report processor, dedicated achievement processor, and approved DDS converter implementation. Complete alpha, full-canvas, native dimension, decode, and source-to-output comparison checks. Verify every final runtime consumer and remove documentation-folder references from runtime files.

Return final assets, source records, approved reference map, family contact sheets, animation evidence, decode evidence, and an updated manifest with actual filenames and consumers. Record production blockers explicitly. Do not substitute placeholder drawings, missing images, or unverified portraits and call the asset family complete.
