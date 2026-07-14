# Event 015 final icon and frame generation prompts

All generated icon sources use the built-in image generation tool. Icon atlases are source artwork only; cells are cropped, keyed to real alpha, fitted to the target canvas, and converted to DDS mechanically. No focus icon is reused as a decision or idea icon.

## Decision and category atlas

- Source mode: built-in image generation
- Layout: exactly 5 columns by 6 rows, row-major, 30 isolated icons
- Background: perfectly flat solid `#ff00ff` chroma key
- Style: compact HOI4 decision art, bronze/wood/ink civic palette, simple silhouette, black outline, restrained shadow, no text, no wreath frame, no square backdrop
- Row-major subjects:
  1. garden district plan and civic plots
  2. fortified island and harbor
  3. marked survey stake and outlined district
  4. stewardship key and open charter
  5. shield over a public storehouse
  6. gavel and corrected charter
  7. five linked household rings forming one seal
  8. open ledger and ink stamp
  9. grain barrel and winter reserve mark
  10. crossed trade tools and instruction book
  11. boundary map and registry quill
  12. survey tripod and plot map
  13. civic rowhouses and foundation shovel
  14. island silhouette and construction plan
  15. lighthouse and common dock
  16. inland rail terminal and grain crates
  17. scales, an empty bowl, and a petition
  18. coin purse and land deed
  19. key and lease scroll
  20. two hands over one civic building
  21. sealed ultimatum with sword and clock
  22. emergency relief crate with grain and medicine
  23. bridge joining linked household blocks
  24. engineer gear and diplomatic satchel
  25. joined grain sheaves and compact clasp
  26. lantern and civic watch shield
  27. crossed wrench and pick over a bridge
  28. auxiliary helmet and signed contract
  29. repaired constitutional parchment and gavel
  30. radiant civic proclamation seal and open charter

## Idea atlas

- Source mode: built-in image generation
- Layout: exactly 5 columns by 2 rows, row-major, 10 isolated icons
- Background: perfectly flat solid `#ff00ff` chroma key
- Style: compact HOI4 national-spirit art for 64x64 use, aged civic manuscript palette, strong silhouette, black outline, restrained shadow, no focus wreath, no text
- Row-major subjects:
  1. unmeasured country: blank map, broken ruler, uncertain compass
  2. inherited order: old estate deed, locked key, inherited burden
  3. charter of households: linked house seals around one charter
  4. common table: communal round table with bread and tools
  5. perfect measure: ornate scales, calipers, and civic grid
  6. closed island: sealed fortified island behind a chain
  7. practical commonwealth: open book, civic lamp, and working hands
  8. garden district network: linked garden towns and rail lines
  9. auxiliary dependency: foreign helmet and coin bound by a chain
  10. stewardship burden: heavy charter, key ring, and balancing weight

## Achievement atlas

- Source mode: built-in image generation
- Layout: exactly 4 columns by 4 rows, row-major; first 14 cells contain completed achievement art and the final two cells remain empty
- Background: opaque charcoal square in every used cell
- Style: HOI4 achievement medallion, sculpted bronze and muted gold, circular relief, laurel or civic border, high contrast at 64x64, no text or numerals
- Row-major subjects:
  1. homeland island encircled by protective houses
  2. peaceful hand balancing bread against an empty crown
  3. six useful tools radiating from a central handshake
  4. provision table with two complete harvest rings and an hourglass
  5. five linked small islands with household lights
  6. landlocked fortress-town encircled by rail
  7. gold coins transformed into public grain and bread
  8. open satirical book, half-mask, and civic lamp
  9. raised household ballots surrounding a charter
  10. pristine scales over a measured district grid
  11. sealed island ring with a fortified gate
  12. home-guard shield turning away a foreign gauntlet
  13. intact overflowing public storehouse after a storm
  14. broken chain surrounding linked households

## Animation source storyboards

Every storyboard is explicitly generated as an animation source sheet, not a review contact sheet. Each panel is saved as a separate source frame before processing. Camera, silhouette, scale, palette, and center anchor remain fixed.

### Need warning

- Layout: 4 columns by 2 rows; 8 states from `frame_plan.md`
- Background: flat `#00ff00`
- Subject: one empty brass civic measure with a tightening cord and a real painted crack progression
- Style: small HOI4 warning sprite, red wax and amber light, no text

### Reserve fill

- Layout: 4 columns by 2 rows; 8 states from `frame_plan.md`
- Background: flat `#00ff00`
- Subject: one horizontal brass-and-wood public reserve gauge whose bins visibly gain and lose sacks, crates, and grain
- Style: elongated HOI4 ledger meter, no text, fixed framing

### Formation-ready seal

- Layout: 5 columns by 2 rows; 10 states from `frame_plan.md`
- Background: flat `#00ff00`
- Subject: one bronze civic seal with five linked household emblems and a central charter
- Style: restrained HOI4 formation-ready loop, painted light passing through real relief states, no text
