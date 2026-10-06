# Delivery preparation icon source record

## Initial built-in ImageGen prompt

Use case: stylized-concept.
Asset type: Hearts of Iron IV decision icon, intended for a transparent 33x32 canvas.
Primary request: Paint a single WWII Soviet twin-engine propeller medium bomber carrying one clearly visible bomb beneath the fuselage. Use a compact three-quarter front view from slightly above: the rounded bomber nose points toward the viewer at lower centre, the tail recedes toward the upper centre, and both broad wings project outward and backward with two distinct engine nacelles. Make the aircraft read as a bomber rather than a fighter.
Style/medium: detailed but bold hand-painted strategy-game icon, charcoal and dark steel aircraft with aged bronze edge highlights, restrained Soviet red star insignia, warm highlights that match a bronze Soviet military icon set. Keep propellers stopped and sharply defined, with no motion blur.
Composition/framing: deliberately near-square silhouette, occupying about 85% of both the 33x32 canvas width and height. Foreshorten the aircraft body so it is compact, while keeping both wings, tail, propellers and full bomb visibly separate and inside a narrow transparent margin. Prioritize a clear small-size outline and broad painted shapes over tiny panel detail.
Background: genuine transparent alpha requested for the initial output; aircraft and bomb only, with a tight natural cutout edge.
Avoid: long horizontal side profile, tiny distant plane, fighter aircraft, single-engine aircraft, extra planes or bombs, detached ordnance, modern jet, missile, people, terrain, sky, clouds, smoke, unreadable text, numbers, watermark, badge, medal, border, square tile, opaque backdrop, fake checkerboard, chroma key, matte, halo, cropped wingtip, cropped tail, cropped bomb.

## Background-only edit prompt

Use case: background-extraction.
Input image: Image 1 is the accepted compact three-quarter Soviet bomber artwork and is the edit target.
Primary request: Change only the checkerboard outside the aircraft-and-bomb silhouette to genuine transparent alpha. Preserve the current bomber exactly: compact nose-forward three-quarter view from above, broad wings, two propeller engines, Soviet red markings, one complete bomb below the fuselage, dark steel and warm bronze palette, lighting, crop and proportions.
Keep all aircraft, propeller, tail and bomb edges intact. Do not repaint, redraw, sharpen, blur, recolour, resize, move or add anything. Remove only the checkerboard beyond the complete silhouette and preserve its natural antialiased painted edge without grey or white matte spill.
Output a PNG with genuinely transparent unused canvas. Do not leave or replace the checkerboard with any other backdrop.

## Generation trace

Built-in `image_gen.imagegen` generated the initial source at `C:/Users/klimp/.codex/generated_images/01a10fb8-9773-7252-b990-c8265513a127/exec-b6296310-2168-4f1e-84b1-78c7796451b0.png`. The initial output was opaque with a checkerboard; the untouched copy is `source_png/imagegen_initial/sov_nuclear_decision_delivery_preparation_initial.png`.

Built-in `image_gen.imagegen` then performed the background-only edit using that generated file as its sole edit target and `transparent_background=true`. The selected source is `source_png/transparent_edit/sov_nuclear_decision_delivery_preparation_background_edit.png`; its untouched generated output path was `C:/Users/klimp/.codex/generated_images/01a10fb8-9773-7252-b990-c8265513a127/exec-67cb3687-8477-4fc0-b61d-2d9a8d06dcb5.png`.
