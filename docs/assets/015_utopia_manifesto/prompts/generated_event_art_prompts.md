# Event 015 Utopian Manifesto generated event art prompts

Tool: official `image_gen`

Source mode summary: generated period-documentary scenes were appropriate because Event 015 needs fictional and alternate-history report, news, super-event, and ledger-panel art rather than archival photos of one real historical incident.

## Report event image prompt

- `report_event_utopia_manifesto_found`: 1936-1945 period documentary-style political photograph, reformers, one local soldier, teachers, and townspeople gathered around a large old manuscript in a storehouse reading room, manuscript central, island sketch and storehouse shelves secondary, intimate and slightly severe mood, no readable text, no modern objects, no fantasy glow.

## News event image prompt

- `news_event_utopia_boundary_crisis`: 1936-1945 black-and-white period press photograph, tense frontier inspection around newly placed boundary markers, inspectors and civic wardens examining posts while uneasy locals and one neighboring officer observe, wide newspaper-banner composition, no readable text, no modern props, no battle smoke.

## Super-event image prompts

- `super_event_utopia_new_utopia`: 1936-1945 period-authentic proclamation scene in a harbor civic square, commonwealth celebration with workers, teachers, dock laborers, and household council delegates gathered around a raised platform, common stores and banners visible but unreadable, strong central composition, no modern objects.
- `super_event_utopia_marked_bounds`: 1936-1945 period-authentic frontier survey scene, boundary surveyors, guarded settlers, magistrates, and uneasy neighbors among newly placed posts and a temporary survey camp, manuscript doctrine turning into territorial pressure, bleak disciplined mood, no readable text, no modern props.

## Scripted GUI panel prompt

- `utopia_ledger_background_panel`: thematic Utopian Ledger desk-and-wall tableau with an open civic ledger, wax seals, survey compass, simple island seal, storehouse inventory tokens, folded banners, and a period harbor map in the background, no readable text, center kept quieter for UI overlays, subdued institutional mood.

## Local processing notes

- Report image was processed with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` for the local report-card treatment.
- News image was cover-cropped to `397x153`, converted to black and white, and normalized to stronger press-photo contrast.
- Super-event images were cover-cropped to `457x328`, normalized to high-contrast monochrome, and exported as DDS through the repo helper.
- GUI background art was cover-cropped to `700x500`.
- `utopia_ledger_header_plate` and `utopia_ledger_warning_panel` were derived from the same generated ledger tableau source to keep the GUI pack visually consistent.
- The repo DDS helper `.tools/convert_to_dds.py` required a local header-pack fix from `"<4sIIIIIII11I"+"IIIII"+"IIIII"+"IIIII"` to `"<4s31I"` before standard DDS export succeeded in this workspace.
