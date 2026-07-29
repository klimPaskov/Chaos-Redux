# Event 016 Idea and National-Spirit Icon Prompt Record

Source mode for every icon: official built-in `$imagegen` generate mode, followed by the installed `remove_chroma_key.py` helper with `--auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill` and a deterministic Pillow RGBA resize to 64x64.

The generation brief for every icon required a compact HOI4 idea or national-spirit composition, one centered subject, dark charcoal outline, subtle subject-only drop shadow, aged WW2-era industrial materials, strong contrast at 64x64, no readable text, no letters or numbers, no protected medical emblems, no modern UI, no watermark, no checkerboard, no white halo, no square frame, and a perfectly flat `#00ff00` chroma-key background that is not used in the subject.

The canonical visual reference inspected before generation was `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas/contact_sheet.png`, with the matching idea rows in `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`. The references informed spirit-icon scale, aged texture, outline, silhouette, and transparent-canvas expectations only.

## Per-icon prompts

### `idea_brilliant_scientist_kruger_appointment`

Generate a gloved scientist hand presenting a precise brass laboratory key before a shadowed civic seal. Use a cautious opportunity mood with brass gold, iron grey, muted crimson, and ivory glove. Keep the key, hand, and seal as one centered vertical emblem.

### `idea_brilliant_scientist_kruger_method`

Generate a precision brass compass and calipers embracing a sealed amber specimen vial, with concentric measuring rings and a dark lens suggesting repeatable method. Use exacting, obsessive cool steel shadows and amber highlights.

### `idea_brilliant_scientist_national_scientific_dependence`

Generate a small state laboratory apparatus chained to a larger brass institutional hand and gear, with a glowing central flask and a smaller dependent gear. Use an uneasy, constrained institutional mood and a single amber dependency glow.

### `idea_brilliant_scientist_public_scientific_renaissance`

Generate a luminous brass laboratory tree sprouting from a glass vessel, with copper-tubing roots, muted laurel leaves, and a rising lens-sun disk. Use a hopeful but disciplined sunrise mood without books, crowds, lettering, or signs.

### `idea_brilliant_scientist_controlled_secret_compact`

Generate two gloved hands sealing a black leather laboratory dossier with a heavy brass clasp and a hidden stoppered vial. Use low warm security light, deep maroon shadows, and a discreet controlled-pact mood.

### `idea_brilliant_scientist_unrestricted_laboratory_state`

Generate a heavy laboratory door thrown open around a bright glass retort and contained curling vapor. Use stark furnace amber spilling into deep blue-black to communicate an unchecked facility without words or signage.

### `idea_brilliant_scientist_scientific_vacuum`

Generate an empty glass bell jar with a deep matte-black hollow, two dormant brass instruments, and one cold spark. Use cold blue edge light swallowed by the void to communicate stalled research and absence.

### `idea_brilliant_scientist_improvised_laboratory_state`

Generate a patched-together brass-and-tin apparatus assembled from salvaged coils, clamp, bottle, and field tools on a rough base. Use warm practical sparks and aged wood, copper, glass, and iron for resourcefulness under pressure.

### `idea_brilliant_scientist_inherited_project_portfolio`

Generate a heavy leather portfolio with a brass clasp carrying a tiny lens, coil, vial, and gear as inherited project relics. Use warm rim light and a clear burden-of-legacy silhouette.

### `idea_brilliant_scientist_fragmented_command`

Generate a cracked brass command baton with three disconnected bakelite radio nodes and snapped cables. Use cold steel highlights and muted red fracture points to show authority split into pieces.

### `idea_brilliant_scientist_experimental_supply_chain`

Generate three rugged cargo crates, copper tubing, and a glowing test flask linked as one fragile logistics emblem. Use practical amber glow and cold steel shadows, with no route arrows or maps.

### `idea_brilliant_scientist_scientific_exodus`

Generate a rugged leather case carrying a glowing laboratory flask through a broken arched doorway, with a small trailing instrument shadow and no face or text. Use melancholy urgency as warm glow recedes into cold dusk.

### `idea_brilliant_scientist_world_threat_project_state`

Generate a dark steel globe-like sphere inside a brass containment ring, wrapped by three red-hot experimental tendrils and a small warning spark. Use severe crimson glow through near-black metal to communicate global project danger without maps or flags.

## Provenance and processing

The original generated PNG for each icon is retained under `source_png/` and the processed alpha PNG under `processed_png/`. The final runtime DDS was produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` as one-level uncompressed BGRA 32-bit output. Each DDS was decoded through Pillow into `dds_decoded_png/`, and `validation.tsv` confirms that every decoded pixel buffer equals its processed PNG pixel buffer.
