# Event 016 Directorate UI image-generation record

All source masters in this package were generated with the built-in `image_gen` skill on 2026-07-24, then cropped or composited into the exact contract sizes. The shared direction was a 1930s–40s scientific Directorate dossier: blue-black enamel, oxidized brass, paper-blue instrumentation, engraved laboratory geometry, low-contrast drafting grids, transparent outer edges where required, and no generated words, numerals, flags, signatures, labels, watermarks, modern electronics, or logos.

## Source masters

- `directorate_background_master.png` (`exec-06bed6a0-97ac-466a-9968-457c93d581d6.png`): wide empty Directorate dossier panel, dark blue-black enamel and brass corners, central drafting seal, instrument bulbs and riveted trim, text-safe center.
- `profile_frame_master.png` (`exec-fddc7d30-c3d3-4481-8557-53e4694f3349.png`): tall ornate brass-and-teal scientific profile frame with a dark transparent aperture and no portrait or lettering.
- `meter_master.png` (`exec-a1d08fc4-69fe-46c9-a2d8-4565607b0fbc.png`): horizontal brass/teal/amber laboratory meter with empty central fill channel, engraved ends, and transparent outer edge.
- `status_badge_master.png` (`exec-2b7e3d69-6f07-4747-a2ff-67ca58871115.png`): compact horizontal Directorate status instrument with circular warning lamps, brass end caps, teal inset channel, and no text.
- `project_card_master.png` (`exec-2767030c-18fa-44c1-9e7e-25b9d0ad0a19.png`): tall scientific apparatus project dossier card, central glass vessel, pressure gauge, hand-drawn drafting sheet, brass frame.
- `facility_card_master.png` (`exec-d963b209-5c95-45ff-934d-be3e531f1ce1.png`): fortified Directorate facility dossier card, blast door, vertical lamps, rivets, dark industrial lab geometry, no labels.
- `contact_card_master.png` (`exec-379e72be-8bde-4f2e-92f0-4e4645c96ca3.png`): foreign-contact dossier card with sealed envelope, flask, radio coil, brass and teal frame, no flags or writing.
- `sovereignty_card_master.png` (`exec-194760d1-f95a-4643-b9e0-f21a2b705466.png`): sovereignty dossier card with crossed charter scrolls, keyhole seal, brass hinges, blue-black paper field, no writing.
- `singularity_master.png` (`exec-663a9f54-c840-49f6-8ab1-49e8e4f67a6a.png`): square containment indicator with black-star core, teal arcs, brass ring, amber and red containment lamps.
- `button_master.png` (`exec-68094ac0-cc3c-4f82-b5b3-39bc8d7cd80e.png`): compact brass compass/star control emblem on transparent dark field, suitable for four state-material variants.
- `decision_category_master.png` (`exec-8ffedcc7-139f-43bf-b25c-67a405f12cda.png`): small circular brass and teal scientific Directorate seal on a transparent dark field.

## Animation storyboards

- `control_warning_storyboard.png` (`exec-bff982c2-d9a0-4cc6-a50d-26f6b4d34308.png`): 4x2 storyboard of eight materially distinct warning-seal states, moving from dim brass/teal to red containment peak and back. Tiles are preserved as individual source frames under `source_frames/control_warning/`.
- `active_project_marker_storyboard.png` (`exec-d0fc840c-a31e-48a6-bbe1-17c37116a96b.png`): 4x2 storyboard of eight distinct project-apparatus states with expanding teal ring, lamp changes, and instrument glints. Tiles are preserved under `source_frames/active_project_marker/`.
- `singularity_armed_storyboard.png` (`exec-19bb6f32-c06c-4913-a732-864b7c1d4e0f.png`): 5x2 storyboard of ten distinct singularity containment states, from dark core through amber ignition and teal/red arc peak back to a dim core. Tiles are preserved under `source_frames/singularity_armed/`.

The storyboard crops are real generated source frames, not a still image moved, scaled, blurred, recoloured, rotated, or overlaid to imply motion. Static fallback PNGs are retained beside each animated sheet.

## Derived controls

The five four-frame button sheets reuse the generated button emblem as a base and apply semantic material changes for normal, hover, pressed, and disabled states. Their individual source variants are retained in `source_masters/` and the packed sheets are under `sheets/`.
