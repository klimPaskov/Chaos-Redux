# ImageGen Prompt Ledger

## Shared generation record

- Tool: official built-in `$imagegen` / `image_gen` tool mode
- Intent: generate, not edit
- Source mode: fictional symbolic raster art
- Source canvas: `1254x1254` RGB PNG
- Transparency method: flat `#00ff00` chroma-key source followed by the
  installed `remove_chroma_key.py` helper; no CLI fallback was used
- Shared constraints: no text, letters, numbers, biohazard symbol, procedure,
  instructions, gore, skull, watermark, UI, border, checkerboard, or cast
  shadow; no real-world source material
- Review style reference: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions/`

The first explicit-action prompt set was rejected by the ImageGen safety
filter. The final prompts below are normalized ledger records preserving the
accepted generation intent and constraints; they were narrowed to
non-instructional fictional game symbolism and generated successfully.

## Anthrax source

- Output: `source/decision_bio_sabotage_anthrax_imagegen.png`
- Prompt:

  > Use case: stylized-concept. Asset type: fictional HOI4-style 32x32
  > decision icon, transparent icon source. Create an original compact
  > symbolic icon for a fictional wartime food-supply crisis associated with
  > anthrax. Show a single centered burlap grain sack, a short wheat sheaf, a
  > sealed dark glass sample vial resting against the sack, and a few heavy
  > charcoal spore-like flecks suspended above the grain. This is a static,
  > non-instructional game symbol of a compromised supply chain, not a
  > tutorial or real-world procedure. Use a perfectly flat solid #00ff00
  > chroma-key background for later removal; no environment. Use a painted WW2
  > grand-strategy game icon style with gritty aged canvas texture, restrained
  > painterly detail, crisp dark outline, high readability at 32x32, centered
  > large shapes and generous padding. Use warm umber and ochre highlights
  > against charcoal brown, with wheat gold, burlap tan, dark anthracite, and
  > muted rust. No text, letters, numbers, biohazard symbol, laboratory
  > procedure, instructions, people, gore, skull, watermark, UI, border,
  > checkerboard, or cast shadow. Keep the #00ff00 background perfectly
  > uniform. Avoid photorealism, vector-only flat shapes, poster layout,
  > labels, logos, battlefield scenes, and explosions.

## Plague source

- Output: `source/decision_bio_sabotage_plague_imagegen.png`
- Prompt:

  > Use case: stylized-concept. Asset type: fictional HOI4-style 32x32
  > decision icon, transparent icon source. Create an original compact
  > symbolic icon for a fictional wartime water-supply crisis associated with
  > plague. Show a single centered dark rat silhouette creeping across a
  > cracked iron water pipe above a small metal canteen; one dark droplet hangs
  > from the pipe, and a subtle clustered swelling on the rat's neck
  > distinguishes the disease identity. This is a static, non-instructional
  > game symbol of a compromised water chain, not a tutorial or real-world
  > procedure. Use a perfectly flat solid #00ff00 chroma-key background for
  > later removal; no environment. Use a painted WW2 grand-strategy game icon
  > style with gritty aged canvas texture, restrained painterly detail, crisp
  > dark outline, high readability at 32x32, centered triangular silhouette,
  > large readable forms, and generous padding. Use cold blue-grey highlights
  > with muted olive and brown, iron blue-grey, dark brown-black rat, muted
  > brass canteen, and a tiny dull green-grey accent. No text, letters,
  > numbers, biohazard symbol, laboratory procedure, instructions, people,
  > gore, skull, watermark, UI, border, checkerboard, or cast shadow. Keep the
  > #00ff00 background perfectly uniform. Avoid photorealism, vector-only flat
  > shapes, poster layout, labels, logos, battlefield scenes, and explosions.

## Tularemia source

- Output: `source/decision_bio_sabotage_tularemia_imagegen.png`
- Prompt:

  > Use case: stylized-concept. Asset type: fictional HOI4-style 32x32
  > decision icon, transparent icon source. Create an original compact
  > symbolic icon for a fictional wartime medical-supply crisis associated
  > with tularemia. Show a single centered open canvas medical crate beside a
  > folded bandage roll and a sealed old ampoule; a small unmistakable rabbit
  > silhouette and a tiny tick-like mark appear as subtle pathogen cues
  > integrated into the still life. This is a static, non-instructional game
  > symbol of a compromised medical chain, not a tutorial or real-world
  > procedure. Use a perfectly flat solid #00ff00 chroma-key background for
  > later removal; no environment. Use a painted WW2 grand-strategy game icon
  > style with gritty aged canvas texture, restrained painterly detail, crisp
  > dark outline, high readability at 32x32, centered crate and bandage,
  > large readable forms, and generous padding. Use muted clinic ivory and
  > olive against deep charcoal, canvas khaki, aged ivory bandage, dark
  > charcoal, muted olive, and a small rust-red accent. No text, letters,
  > numbers, biohazard symbol, laboratory procedure, instructions, people,
  > gore, skull, watermark, UI, border, checkerboard, or cast shadow. Keep the
  > #00ff00 background perfectly uniform. Avoid photorealism, vector-only flat
  > shapes, poster layout, labels, logos, battlefield scenes, and explosions.

## Smallpox source

- Output: `source/decision_bio_sabotage_smallpox_imagegen.png`
- Prompt:

  > Use case: stylized-concept. Asset type: fictional HOI4-style 32x32
  > decision icon, transparent icon source. Create an original compact
  > symbolic icon for a fictional wartime medical-chain crisis associated with
  > smallpox. Show a single centered medical shipment crate with folded
  > dressings and a small cracked vaccine vial; the dressing and crate carry a
  > clearly readable cluster of dark red-brown pockmarks, making the disease
  > identity distinct without any symbols or lettering. This is a static,
  > non-instructional game symbol of a compromised medical chain, not a
  > tutorial or real-world procedure. Use a perfectly flat solid #00ff00
  > chroma-key background for later removal; no environment. Use a painted WW2
  > grand-strategy game icon style with gritty aged canvas texture, restrained
  > painterly detail, crisp dark outline, high readability at 32x32, centered
  > crate and dressing, large readable forms, and generous padding. Use pale
  > medical cloth against deep blue-charcoal and muted red-brown, cold ivory,
  > faded blue-grey, dark charcoal, and muted rust-red pockmarks. No text,
  > letters, numbers, biohazard symbol, laboratory procedure, instructions,
  > people, gore, skull, watermark, UI, border, checkerboard, or cast shadow.
  > Keep the #00ff00 background perfectly uniform. Avoid photorealism,
  > vector-only flat shapes, poster layout, labels, logos, battlefield scenes,
  > and explosions.

## Local processing record

- Chroma-key command: `python C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py --input <source> --out <intermediate> --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill`
- Composition: visible alpha bbox plus a small proportional margin; fit within
  30 pixels on the long axis; center on a transparent 32×32 RGBA canvas;
  Lanczos downsample; save as processed PNG.
- DDS command: `python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <processed> --output <final> --width 32 --height 32`
