# Event 011 Secret Alliance generated event art prompts

Source mode: generated non-icon art through built-in `image_gen`

## Event images

- `report_event_secret_alliance_meeting`
  - 1936-1945 period documentary diplomatic photograph of a secret founding meeting for a covert anti-target alliance, shadowed interwar government chamber, three delegations in period civilian and military dress, faces partly obscured, sealed pouch near doorway, black-and-white wartime press realism, no readable text, no real leaders, no modern props.
- `report_event_secret_alliance_courier`
  - 1936-1945 period documentary photograph of a covert courier intercepted at a border rail checkpoint, small border station platform and customs office, period security officials opening a leather diplomatic pouch, loose papers unreadable, black-and-white press realism, no real leaders, no modern vehicles.
- `report_event_secret_alliance_sabotage`
  - 1936-1945 period documentary photograph of sabotage aftermath inside a rail-linked factory, damaged machine hall, broken windows and twisted piping, period workers, engineers, and soldiers inspecting wrecked machinery, black-and-white press realism, no graphic violence, no modern machinery.
- `news_event_secret_alliance_reveal`
  - 1936-1945 period press photograph of the public reveal of a clandestine anti-target alliance, broad government forecourt and stone steps, generic delegations shoulder to shoulder, faces partly shadowed or turned, blurred strategic wall chart behind them, wide newspaper banner composition, black-and-white press realism, no readable text, no readable flags, no real leaders.
- `super_event_secret_alliance_reveal`
  - 1936-1945 period documentary-style super-event image of a secret alliance becoming a public bloc, vast shadowed diplomatic hall with gallery balconies, colossal blurred map wall, central raised dais with several generic delegations beneath a looming circular emblem, strong central composition, monochrome radio-era press realism, no readable text, no real leaders.

## Dossier Board UI art

- `secret_alliance_board_bg`
  - Large fictional investigation-board background, aged corkboard and map-table hybrid viewed straight on, dark walnut frame edges, pinned map fragments, empty photo corners, wax marks, string anchor pins, paper clips, functional UI art rather than exact layout, no readable text.
- `secret_alliance_member_unknown`
  - Single dossier card for an unidentified pact member, aged investigation card on dark backing, central silhouette bust, wax seal fragments and quiet dossier ornament, no readable text, no real person likeness.
- `secret_alliance_member_known`
  - Single dossier card for an exposed pact member, aged investigation card on dark backing, central monochrome portrait of a fictional period diplomat or officer, stronger confirmation styling than the unknown card, no readable text, no real person likeness.
- `secret_alliance_pact_emblem`
  - Fictional diplomatic compact emblem, dark plaque or medallion surface, closed ring made from three wax seals surrounding an empty central marker with fine compass geometry, muted brass and oxblood wax, no letters.
- `secret_alliance_evidence_meter`
  - Functional horizontal investigation meter panel with parchment inset and brass trim, subtle index ticks, document tabs, magnifier and file motifs, no numbers or letters.
- `secret_alliance_pressure_meter`
  - Functional horizontal pressure meter panel with warning styling, subtle index ticks, thread path motifs, seal fragments, and diplomatic warning cues, no numbers or letters.
- `secret_alliance_preparedness_meter`
  - Functional horizontal preparedness meter panel with organized military-planning styling, subtle index ticks, reserve-plan motifs, shielded file tabs, no numbers or letters.

## Animation source

- `secret_alliance_thread_glow`
  - Single generated `4x2` source sheet containing eight distinct loop frames for a dossier-board red-thread glow, same straight-on board in every panel, only the thread-network light state changes from faint to strong and back down, no panel labels, no readable text, no camera drift.

## Processing notes

- Report images were processed with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` for the final `210x176` house report-card treatment.
- News image was cropped to `397x153` and processed into black-and-white press treatment.
- Super-event image was cropped to `457x328` and kept in monochrome high-contrast treatment for the shared super-event frame.
- Meter fill variants are mechanical UI state variants at `25`, `50`, `75`, and `100` percent. They reuse the approved meter base art so the board can show live evidence, pressure, and preparedness bands.
