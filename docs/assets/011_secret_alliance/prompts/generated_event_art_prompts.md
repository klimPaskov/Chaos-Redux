# Event 011 Secret Alliance generated raster prompts

## Shared generation contract

- Workflow: built-in `$imagegen` (`image_gen`), one generation per distinct asset.
- Taxonomy: `historical-scene`.
- Intended use: fictional, procedural alternate-history event art for Hearts of Iron IV.
- Period: 1936-1945 photographic technology, clothing, vehicles, architecture, props, lighting, and press composition.
- Identity rule: no real leader likenesses, no fixed national flags, no legible insignia, and no real extremist symbols.
- Output rule: source scene only. The report-card tilt, sepia treatment, news monochrome treatment, exact crop, and DDS conversion are deterministic local processing steps.
- Common exclusions: no readable text, letters, numbers, captions, watermarks, logos, modern streets, modern tactical clothing, modern safety gear, modern weapons, modern surveillance devices, neon cyber imagery, UI overlays, fake paper damage, title cards, diagrammatic arrows, map-only compositions, or cinematic colour grading.

## `report_event_first_pattern`

```text
Use case: historical-scene
Asset type: HOI4 report-event source photograph, later cropped into a 210x176 sepia documentary card
Primary request: a fictional 1938 railway dispatch office where two civilian railway clerks and one plain-clothes investigator compare several physically damaged dispatch envelopes and duplicated route slips after noticing the same interference pattern
Scene/backdrop: cramped period railway office, timber desks, pigeonholes, wall clock, telegraph equipment and rain-streaked windows; papers contain no readable writing
Subject: the people and their tangible evidence are central; one clerk holds two matching torn route slips while the investigator studies damaged seals
Style/medium: authentic 1936-1945 black-and-white press photograph, candid documentary realism, period lens softness and restrained film grain
Composition/framing: landscape medium-wide view, human figures and evidence large and readable, no map as the main subject, crop-safe center
Lighting/mood: overcast window light and practical desk lamp, quiet realization and unease
Constraints: fictional anonymous people only; period-correct clothing and equipment; no readable text, flags, insignia, logos, watermark or modern objects
Avoid: conspiracy board, red string, cinematic spy thriller lighting, posed handshake, empty still life
```

## `report_event_missing_courier`

```text
Use case: historical-scene
Asset type: HOI4 report-event source photograph, later cropped into a 210x176 sepia documentary card
Primary request: a fictional 1939 rural border-road search after a courier vanishes, showing an abandoned period bicycle beside a shallow ditch, an open leather satchel, and a restrained search party of border guards and a civilian constable
Scene/backdrop: muddy rural road near a simple border barrier and wooded hills, telegraph poles and morning mist
Subject: open satchel and abandoned bicycle in the foreground, three searchers examining tracks and the roadside; no body and no graphic violence
Style/medium: authentic 1936-1945 black-and-white field-documentary photograph, natural imperfections, period press realism
Composition/framing: landscape medium-wide view, strong central triangle between bicycle, satchel and searchers, crop-safe center
Lighting/mood: cold dawn light, uncertainty and methodical investigation
Constraints: fictional anonymous people only; period bicycle, uniforms, boots and road furniture; no readable signs, flags, insignia, text, logos, watermark or modern objects
Avoid: corpse-centered sensationalism, car crash, modern police tape, cinematic action pose
```

## `report_event_machine_sabotage`

```text
Use case: historical-scene
Asset type: HOI4 report-event source photograph, later cropped into a 210x176 sepia documentary card
Primary request: fictional wartime factory engineers inspecting deliberately damaged machine tools, with one opened lathe housing, snapped drive components and matching tool marks being compared under a work lamp
Scene/backdrop: busy 1940 industrial machine shop with belt-driven equipment, riveted steel, oil-stained floor and workers kept in the background
Subject: two engineers and one factory foreman closely examining the damaged mechanism and a removed metal part; the physical sabotage evidence is unmistakable
Style/medium: authentic 1936-1945 black-and-white industrial press photograph, documentary realism, period lens and film response
Composition/framing: landscape close documentary view, people and damaged machinery fill the frame, crop-safe center
Lighting/mood: hard practical workshop light, controlled alarm, no spectacle
Constraints: fictional anonymous people only; period coveralls and tools; no modern safety equipment, screens, plastics, readable labels, flags, insignia, text, logos or watermark
Avoid: explosion, fireball, futuristic machinery, generic assembly line panorama
```

## `report_event_safehouse_raid`

```text
Use case: historical-scene
Asset type: HOI4 report-event source photograph, later cropped into a 210x176 sepia documentary card
Primary request: fictional 1941 police and intelligence officers entering a sparse rented safehouse room and discovering a compact valve radio, travel cases and an opened concealed compartment behind loose wall panelling
Scene/backdrop: modest interwar apartment room with iron bed, plain table, blackout curtains, worn plaster and period luggage
Subject: three officers in period coats actively searching; one opens the wall compartment while another examines the valve radio; no suspect is shown
Style/medium: authentic 1936-1945 black-and-white crime and intelligence press photograph, natural documentary realism
Composition/framing: landscape interior, doorway perspective with strong depth, room evidence and people readable, crop-safe center
Lighting/mood: harsh ceiling bulb and window spill, tense but procedural
Constraints: fictional anonymous people only; no readable papers, modern electronics, tactical gear, flags, insignia, text, logos or watermark
Avoid: gunfight, noir glamour portrait, conspiracy board, piles of dossiers as the sole subject
```

## `report_event_border_survey`

```text
Use case: historical-scene
Asset type: HOI4 report-event source photograph, later cropped into a 210x176 sepia documentary card
Primary request: fictional civilian-looking surveyors measuring a strategic stone bridge and mountain pass while two concealed border guards observe them from a wooded ridge
Scene/backdrop: 1930s rural mountain crossing, old stone bridge, narrow road, survey tripod, measuring rod and distant customs hut
Subject: survey team near the bridge is central, with the watchers visibly framed by branches in the near foreground; the scene suggests military preparation without open combat
Style/medium: authentic 1936-1945 black-and-white reconnaissance photograph, restrained documentary realism and period optics
Composition/framing: landscape telephoto-like observation view, layered foreground watchers and midground surveyors, crop-safe center
Lighting/mood: thin afternoon cloud, watchful suspicion
Constraints: fictional anonymous people only; period clothing, optical survey gear and bridge; no modern road markings, vehicles, optics, readable signs, flags, insignia, text, logos or watermark
Avoid: tactical map overlay, crosshairs, sniper view, overt battle, generic landscape without people
```

## `report_event_political_attack`

```text
Use case: historical-scene
Asset type: HOI4 report-event source photograph, later cropped into a 210x176 sepia documentary card
Primary request: restrained fictional aftermath of a 1942 attempted political killing on government steps, with a damaged official staff car, shattered side window, guards establishing a perimeter and civilians being moved away
Scene/backdrop: severe interwar government building entrance, broad stone steps, period official automobile and scattered personal effects
Subject: security officers around the damaged vehicle and steps; no identifiable politician, no corpse, no graphic injury and no active shooter
Style/medium: authentic 1936-1945 black-and-white breaking-news photograph, sober documentary realism, period lens softness
Composition/framing: landscape medium-wide press view, damaged vehicle and guarded steps form one clear central event, crop-safe center
Lighting/mood: flat winter daylight, grave and controlled
Constraints: fictional anonymous people only; period car, coats and security equipment; no readable license plates, banners, flags, insignia, text, logos, watermark or modern objects
Avoid: sensational blood, explosion, heroic action pose, riot spectacle, modern motorcade
```

## `report_event_turned_channel`

```text
Use case: historical-scene
Asset type: HOI4 report-event source photograph, later cropped into a 210x176 sepia documentary card
Primary request: a tense fictional 1943 night meeting where a nervous civilian envoy quietly passes a sealed travel case to two intelligence handlers in period dress inside a dim railway waiting room
Scene/backdrop: nearly empty provincial station waiting room, wooden benches, frosted window, small stove, wall clock and luggage trolley; no readable timetable
Subject: three anonymous people in a close triangular arrangement, faces partly obscured naturally by hats, profile and shadow, not blurred; the controlled handover is central
Style/medium: authentic 1936-1945 black-and-white covert documentary photograph, candid realism, period film grain and lens softness
Composition/framing: landscape medium shot, hands and travel case readable, crop-safe center
Lighting/mood: one practical lamp and weak platform light, uneasy cooperation and secrecy
Constraints: fictional anonymous people only; period civilian coats, hats and luggage; no guns displayed, readable text, flags, insignia, logos, watermark or modern objects
Avoid: generic handshake, glamorous noir poster, artificial face blur, spy gadgets, interrogation room
```

## `news_event_public_coalition`

```text
Use case: historical-scene
Asset type: HOI4 public news-event source photograph, later cropped to 397x153 and processed as high-contrast black-and-white period press art
Primary request: a fictional 1941 public coalition announcement showing several visibly different civilian delegations standing shoulder to shoulder beneath one simple unlettered geometric emblem while uniformed military staff assemble behind them
Scene/backdrop: formal civic hall entrance with stone columns and a broad press platform, no national flags or readable signage
Subject: six to eight delegates with varied period civilian dress and generic uniforms, unified but visibly from different governments; shared public commitment is unmistakable
Style/medium: authentic 1936-1945 panoramic black-and-white wire-service photograph, sober press realism, period lens and film response
Composition/framing: very wide landscape group composition, delegates occupy the center band with complete heads and shoulders, important faces and emblem kept away from extreme edges for a 397x153 crop
Lighting/mood: bright press flash and overcast daylight, formal resolve rather than celebration
Constraints: fictional anonymous people only; no real leader likenesses, fixed country flags, extremist symbols, readable insignia, text, letters, numbers, logos, watermark or modern objects
Avoid: handshake close-up, cheering stadium, title card, map backdrop, modern summit photograph
```

## `super_event_public_reveal`

```text
Use case: historical-scene
Asset type: HOI4 reveal super-event source photograph, later cropped to 457x328 and reviewed inside the repository super-event mask
Primary request: a fictional alternate-history 1942 documentary scene in a dark formal hall where several civilian delegations and military representatives converge around one long table to sign and publicly commit to a common anti-target coalition
Scene/backdrop: severe interwar council hall, tall windows, dark timber and stone, overhead practical lamps, press observers at the rear; one broken wax seal and folded unlabelled target map are small secondary props on the table
Subject: the human coalition is central: multiple distinct delegations lean or stand toward the same commitment, with a senior anonymous chair at the center but no single real-person likeness
Style/medium: authentic 1936-1945 black-and-white documentary press photograph with dramatic but plausible period lighting, rich tonal range and restrained film grain
Composition/framing: 4:3 landscape, strong central convergence, readable faces and uniforms at 457x328, clear depth, important subjects inside the central and right-center safe area
Lighting/mood: low formal chamber light with a controlled pool of illumination on the gathered people, public resolve after long concealment
Constraints: fictional anonymous people only; no real leader likenesses, no fixed national flags, readable insignia, extremist symbols, readable text, letters, numbers, UI, logos, watermark or modern objects
Avoid: anonymous globe, pile of dossiers, map with arrows, generic handshake, title card, abstract diagram, empty conference room, modern summit photography
```
