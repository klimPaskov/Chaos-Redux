# Event 015 Advisor Portrait ImageGen Evidence

This package contains sixteen fictional Event 015 advisor portrait reframings; the parent accepted all sixteen candidates on 2026-10-06 and they are installed at their existing runtime paths.

The new masters were created with the built-in native image_gen.imagegen tool, then copied from its generated-image output folder into imagegen_master_candidates/; the source crop for each was the preserved 65×67 runtime decode in source_png/.

The earlier full-resolution July masters cited by the historical 015 handoffs are absent from this workspace, so these candidates are fresh ImageGen edits guided by the low-resolution existing cards and are not claimed to reproduce the missing accepted masters.

The prior test master imagegen_master_png/advisor_utopia_manifesto_interpreter.png remains unchanged and unselected because its hairstyle drifted.

The minister_portrait_background.png asset below was used only as a frame-shape and transparent-corner reference; no pixels from the reference shelf were shipped or composited into runtime assets.

## Initial Full-Resolution Portrait Prompt

The following prompt template was used for the first unframed enlargement pass; {id}, {display_name}, and {source_png} were substituted for each row in the output table.

Use case: stylized-concept

Asset type: full-resolution source master for the existing fictional HOI4 advisor portrait “utopia_manifesto_{id}”, to be mechanically prepared as a native 65x67 portrait icon.

Input image: Image 1, {source_png} — the exact fictional subject reference. Transfer only this same person’s facial proportions, facial features, gender presentation, skin tone, apparent age, expression, gaze, hairstyle and hairline, head angle, and clothing shape/color. Ignore the existing paper card, outer frame, and all pseudo-writing.

Primary request: faithfully enlarge this same person into a clear, plain head-and-shoulders painted portrait for the existing {display_name} advisor. Change only composition: remove the dossier card and note, and make the person’s face larger so it is immediately recognizable at 65x67. Preserve the face, hair, age, expression, pose, and clothing from Image 1; do not beautify, symmetrize, or invent another person.

Scene/backdrop: simple muted softly painted neutral background, close to the subdued tones of Image 1.

Style/medium: restrained hand-painted HOI4 portrait art, subtle visible brush texture, muted period-appropriate palette consistent with Image 1.

Composition/framing: one person only, centered frontal or three-quarter head-and-shoulders portrait; face fills most of the portrait canvas and remains readable at 65x67; shoulders visible near the bottom.

Lighting/mood: soft painted portrait lighting consistent with Image 1.

Constraints: keep the exact fictional subject appearance and clothing; change only the crop/scale and remove the old card and note.

Avoid: text, handwriting, paper note, surrounding UI/card frame, borders, badges, insignia, extra people, changed hairstyle, changed face, changed gender presentation, changed clothing, new accessories, logos, watermarks.

The initial pass was retained as intermediate_unframed_png/ evidence and was not installed.

## Framed Candidate Edit Prompt

Except where noted below, the following prompt was used to add the plain frame and native transparency to each portrait’s own unframed candidate.

Use case: stylized-concept

Asset type: focused edit of a fictional HOI4 advisor portrait master for the existing 65x67 card.

Input images:

- Image 1, docs/assets/gfx_fix_portraits_2026-10/source_png/advisor_utopia_manifesto_{id}.png — exact fictional identity anchor. Preserve the same face, facial proportions, gender presentation, skin tone, apparent age, expression, gaze, hairstyle/hairline, head angle, and clothing. Ignore the old card and paper note.
- Image 2, {unframed_candidate_path} — edit target for this same fictional person. Keep this exact generated person’s face, hair, clothing, pose, and painted portrait interior.
- Image 3, .agents/skills/chaos-redux-event-assets/assets/visual_components/portrait_backdrops/minister_portrait_background.png — reference for compact dark bevelled advisor-card framing and transparent outside corners only. Do not copy its background pixels or any person; it is a style/geometry reference only.

Primary request: make a faithful framed version of Image 2 for the existing {display_name} advisor. Preserve this exact person’s face, hair, age, expression, pose, and clothing. Add a narrow, irregular charcoal/bronze painted frame around the outside edge, matching the compact vanilla advisor-card footprint. Make the portrait large inside the opening so the face reads clearly at 65x67. This is a frame/alpha edit only.

Style/medium: retain Image 2’s muted hand-painted HOI4 style, light texture, and quiet neutral backdrop; the frame is dark charcoal with subtle bronze bevel highlights.

Composition/framing: one centered head-and-shoulders portrait in a compact almost-square card; frame around the outer edge only, no insert or corner plate. Face fills the opening; shoulders are visible at the bottom.

Background and alpha: preserve Image 2’s painted background inside the frame; render unused outer corners genuinely transparent with no checkerboard, matte, or halo.

Constraints: exact identity and clothing from Images 1 and 2; add only the plain frame and genuine transparent exterior.

Avoid: paper, notes, lettering, handwriting, text, badges, insignia, symbols, extra people, changed face, changed hair, changed gender presentation, changed clothing, new accessories, logos, watermark.

Native transparency was requested for all sixteen framed outputs and the processed 65×67 PNGs have zero alpha at all four canvas corners.

## Per-Asset Output Lineage

| Advisor | Identity input | First unframed output | Final framed output |
| --- | --- | --- | --- |
| Advocate of Limits | source_png/advisor_utopia_manifesto_advocate_of_limits.png | exec-14f5ba3d-20dd-4350-9e2b-93874601d7ca.png | exec-3e63cd84-1a8c-4cf6-9031-9bcf5cf654c6.png |
| Chief Surveyor | source_png/advisor_utopia_manifesto_chief_surveyor.png | exec-5be9f3e3-e1c8-47c0-9541-3c64d9602408.png | exec-3e0b8af1-72ae-4523-9c10-05b5e31134f8.png |
| Civic Engineer | source_png/advisor_utopia_manifesto_civic_engineer.png | exec-841929d7-0fa9-4d27-81f1-a204c775788b.png | exec-2cd02712-f972-4cb6-a0fd-a53b142b51b1.png |
| Constitutional Jurist | source_png/advisor_utopia_manifesto_constitutional_jurist.png | exec-51336b01-1fea-431e-a724-af49dc1300ca.png | exec-9648bb31-b0a3-4058-831b-2b22d79bdf98.png |
| Contract Broker | source_png/advisor_utopia_manifesto_contract_broker.png | exec-60456dcd-ab30-49b2-a822-bf1849ee91e3.png | exec-a61d48cd-486d-4e7d-9b83-f73862967abb.png |
| Council Organizer | source_png/advisor_utopia_manifesto_council_organizer.png | exec-b5346abf-c065-475a-a7f5-dd0bfdaae408.png | exec-cad8b023-ded5-4a18-9635-83ef3267ef80.png |
| General Provisioner | source_png/advisor_utopia_manifesto_general_provisioner.png | exec-ee45a6a4-c9b6-4e65-b142-bcc8fd54ec9c.png | exec-2ee2e41e-d6d5-4f5f-83bc-b50d3f68944a.png |
| Public Interpreter | source_png/advisor_utopia_manifesto_interpreter.png | exec-5423ba85-cabb-4856-b1e2-20c263366306.png | exec-ab179da2-5016-4280-9f5b-23a8863e5c53.png |
| Keeper of Stores | source_png/advisor_utopia_manifesto_keeper_of_stores.png | exec-4d1352e1-1852-4e35-b521-abe3fa4ff433.png | exec-8095429a-a3eb-4214-8afe-78465a48d5ec.png |
| League Envoy | source_png/advisor_utopia_manifesto_league_envoy.png | exec-1b405d19-7b34-48ae-bc1a-8d042585c644.png | exec-f9216f81-4724-41f9-9b6a-385884cfb609.png |
| Public Auditor | source_png/advisor_utopia_manifesto_public_auditor.png | exec-6dfe418d-0dd9-4ea7-adb6-23a50dd29899.png | exec-da7ecf4a-1a36-4776-9162-9f57befe5ec6.png |
| Secretary of Callings | source_png/advisor_utopia_manifesto_secretary_of_callings.png | exec-4127075b-0e4f-46b2-906c-bfcc166154a6.png | exec-239f435a-93a7-4e81-b599-f89627d28763.png |
| Social Workshop Planner | source_png/advisor_utopia_manifesto_social_workshop_planner.png | exec-899792eb-fb4b-4bd2-a87b-9782f195a2d6.png | exec-74f38bca-542d-414a-9976-345368f50b18.png |
| Standards Engineer | source_png/advisor_utopia_manifesto_standards_engineer.png | exec-7fbb5bcd-0d08-4980-b727-0d3d2c960c23.png | exec-925f9f0b-38c2-4c23-b7eb-5e9c9b31fcf6.png |
| Steward of Service | source_png/advisor_utopia_manifesto_steward_of_service.png | exec-1f2e7b4f-7833-41d4-9f10-fe3c3b4adbcc.png | exec-cf0bb560-fc2f-4821-9f51-28ec804adceb.png |
| Surveyor of Shores | source_png/advisor_utopia_manifesto_surveyor_of_shores.png | exec-a0f9c551-2507-40cf-9ce7-ddb5e5eb9ea8.png | exec-1ef48d55-f305-44c6-9ce7-ddb5e5eb9ea8.png |

The original tool outputs in that table are archived in this folder as imagegen_master_candidates/ and intermediate_unframed_png/; the rows identify their original generated-image filenames.

## Focused Identity Corrections

The Constitutional Jurist first unframed candidate added round glasses that were not clear in the preserved crop, so a targeted edit removed the eyewear before the framed master was generated.

The Steward of Service first unframed candidate changed the source’s older fair-skinned male presentation, receding hairline, glasses, and green sweater, so a targeted edit restored those source-visible properties before framing.

The identity-correction prompt outputs are recorded under intermediate_identity_corrections/ and their hashes are in the v1 and v2 candidate manifests.

## Review State

The v1 sheets parent_review_native_old_new.png and parent_review_4x_old_new.png preserve the first review set; the v2 sheets parent_review_native_old_new_v2.png and parent_review_4x_old_new_v2.png include the parent-requested Interpreter and Contract Broker corrections.

The parent reviewed the v2 native and 4x sheets and accepted the framing, painted style, note removal, and all sixteen portraits.

All sixteen portraits were accepted by the parent after individual likeness review; Chief Surveyor eyewear remains indeterminate in the low-resolution source and no uncertain eyewear trait was invented. The source eye-detail preview is preserved at docs/assets/gfx_fix_portraits_2026-10/evidence/source_details/chief_surveyor_eyes_nearest_20x.png.

## Asset-Specific Initial Prompt Overrides

Every generated-image filename in this file is relative to C:/Users/klimp/.codex/generated_images/01a10fb9-55b1-7621-8530-1694ae0c2f34/.

The Public Interpreter first enlargement used this more specific prompt, with the original 65×67 source PNG as the only reference image:

Use case: stylized-concept
Asset type: full-resolution source master for the existing fictional Hearts of Iron IV advisor portrait “utopia_manifesto_interpreter”; this will be reduced to a native 65x67 portrait icon.
Input image: Image 1, docs/assets/gfx_fix_portraits_2026-10/source_png/advisor_utopia_manifesto_interpreter.png — exact fictional identity and appearance reference. Transfer only the same woman’s face, facial proportions, skin tone, age, expression, gaze, dark hair style/length, and brown jacket with light blouse. Ignore the frame, paper card, and all pseudo-writing.
Primary request: faithfully enlarge the same woman into a clear head-and-shoulders painted portrait. Change only the composition by removing the dossier card and note, then framing her face larger so it remains immediately recognizable at 65x67. Preserve her hairstyle exactly: dark, short-to-medium hair close around the head, with the same part and silhouette as Image 1. Preserve the same apparent age, face shape, eyes, nose, mouth, expression, skin tone, and clothing colors. Do not beautify, symmetrize, or invent a different person.
Scene/backdrop: simple softly painted muted warm-grey and olive background, understated and close in tone to Image 1.
Style/medium: restrained hand-painted HOI4 portrait art, period-appropriate muted palette, visible but subtle brush texture; preserve the treatment already present in Image 1.
Composition/framing: one person only, centered frontal/three-quarter head and shoulders, head and shoulders filling almost the whole square canvas, face large and readable; show a small amount of shoulders at the bottom.
Lighting/mood: soft even studio light consistent with Image 1.
Constraints: keep the exact fictional subject appearance, gender presentation, hairstyle, facial geometry, expression, head angle, and clothing. No framing card, no border, no note, no paper, no props, no badges or insignia.
Avoid: text, handwriting, symbols, extra people, different hairstyle, different face, changed gender, changed clothing, new accessories, logos, watermarks.

The Advocate of Limits first enlargement used the same structure but specified the visible source traits as a woman with a dark bob hairstyle, light blouse, and dark jacket.

## Public Interpreter Framed Candidate Prompt

The Public Interpreter framed output used the preserved source card, the unframed candidate, and the backdrop reference with the following prompt:

Use case: stylized-concept
Asset type: edit of an existing fictional HOI4 advisor portrait master for a 65x67 card.
Input images:
- Image 1, docs/assets/gfx_fix_portraits_2026-10/source_png/advisor_utopia_manifesto_interpreter.png — the exact fictional person identity anchor; transfer her actual face, hairline, short-to-medium dark hairstyle, skin tone, age, expression, eye direction, head angle, and brown jacket/light blouse. Ignore the existing frame and paper note.
- Image 2, C:/Users/klimp/.codex/generated_images/01a10fb9-55b1-7621-8530-1694ae0c2f34/exec-5423ba85-cabb-4856-b1e2-20c263366306.png — edit target for this same fictional person; retain its painted face, hair, clothing, pose, and backdrop as closely as possible.
- Image 3, .agents/skills/chaos-redux-event-assets/assets/visual_components/portrait_backdrops/minister_portrait_background.png — composition/frame-shape reference only. Transfer only a simple dark painted beveled portrait-card edge and its transparent outer corners. Do not copy any person or treat this image as portrait art.
Primary request: preserve the Image 2 portrait of the same person and add a plain narrow dark painted frame around the portrait opening, inspired by Image 3. Make the portrait feel like an HOI4 advisor card, with the head large in the visible opening. Keep the current face and all subject details fixed; this is only a frame and alpha treatment edit.
Style/medium: retain Image 2’s restrained hand-painted HOI4 art and muted warm grey/olive palette; dark charcoal/bronze irregular bevel around the portrait edge only.
Composition/framing: one large head-and-shoulders portrait, centered; portrait fills nearly the full inner opening, with a small shoulder area at the bottom. Frame hugs the image edge like a compact 65x67 advisor card.
Background and alpha: preserve Image 2’s painted background inside the frame and make the unused outer corners genuinely transparent. Do not fill transparent corners with a checkerboard or matte.
Constraints: keep the exact face, gender presentation, hairstyle, clothing, pose, age, and expression from Image 2, guided by Image 1. Add only the simple edge frame and transparent corners.
Avoid: any paper note or card insert, all handwriting or text, badges, symbols, extra people, changed face, changed hair, changed clothing, beautification, extra accessories, logos, watermark.

## Constitutional Jurist Identity Correction

The first unframed Constitutional Jurist candidate introduced round glasses that were not clear in the source crop, so this focused edit removed only the eyewear before framing:

Use case: identity-preserve
Asset type: targeted edit of the full-resolution fictional advisor portrait “utopia_manifesto_constitutional_jurist”.
Input images:
- Image 1, docs/assets/gfx_fix_portraits_2026-10/source_png/advisor_utopia_manifesto_constitutional_jurist.png — exact fictional identity anchor.
- Image 2, C:/Users/klimp/.codex/generated_images/01a10fb9-55b1-7621-8530-1694ae0c2f34/exec-51336b01-1fea-431e-a724-af49dc1300ca.png — edit target; preserve its current painted face, hair, clothing, pose, backdrop, and lighting.
Primary request: remove only the round eyeglasses currently added in Image 2, since they are not supported by Image 1. Leave the eyes naturally unobstructed and paint the underlying eye/brow area consistently with the existing portrait.
Constraints: preserve exactly the same face, eyes, nose, cheeks, mouth, skin tone, hairstyle, age, expression, head angle, clothing, shoulders, muted background, composition, and painterly style; alter only the eyeglasses and the small area they cover.
Avoid: adding glasses or eyewear, changing any facial features, hair, expression, gender presentation, outfit, background, frame, text, symbols, logos, watermark.

The final Constitutional Jurist frame edit used the framed candidate template with “eyewear” added to the avoid list.

## Steward of Service Identity Correction

The first unframed Steward of Service candidate changed the source’s older fair-skinned male presentation, receding hairline, glasses, and green sweater, so this focused identity correction used the original source as authoritative:

Use case: identity-preserve
Asset type: focused identity correction for the full-resolution fictional HOI4 advisor portrait “utopia_manifesto_steward_of_service”.
Input images:
- Image 1, docs/assets/gfx_fix_portraits_2026-10/source_png/advisor_utopia_manifesto_steward_of_service.png — authoritative identity source. This subject is a fair-skinned older man with a receding hairline and short light-brown/greying hair at the sides, dark eyeglasses, and a dark olive-green sweater. Preserve the face shape, apparent age, gender presentation, glasses, hairline, and clothing visible here.
- Image 2, C:/Users/klimp/.codex/generated_images/01a10fb9-55b1-7621-8530-1694ae0c2f34/exec-1f2e7b4f-7833-41d4-9f10-fe3c3b4adbcc.png — painterly style, composition, shoulder framing, and background reference only. Do not retain its mismatched East Asian face or hairstyle.
Primary request: correct the subject in Image 2 to depict the same older fair-skinned man from Image 1. Keep a frontal head-and-shoulders portrait in the same subdued hand-painted HOI4 style and quiet neutral background, with the dark green sweater from Image 1. Use a plausible enlarged rendering of the actual source identity rather than a new person.
Constraints: preserve the older male identity, pale skin tone, receding hairline, visible eyeglasses, and green sweater; do not beautify or change ethnicity. Keep the existing full-square unframed composition and portrait scale.
Avoid: young face, East Asian face, different age, different gender, no glasses, full dark hair, suit and tie, paper note, frame, text, logos, watermark.

The final Steward of Service frame edit used the framed candidate template with explicit preservation of the older fair-skinned man, receding hair, glasses, green sweater, and avoidance of altered identity or ethnicity.

## Parent-Requested v2 Identity Rechecks

The parent’s 2026-10-06 v1-sheet review accepted the painted style, frame family, and removal of all note writing, and requested a pulled-back-hair/warmer-complexion correction for the Public Interpreter and a rounder/warmer face correction for the Contract Broker.

The Public Interpreter source close-up showed dark hair pulled back smoothly from the forehead and temples and a medium warm-brown complexion, so this focused edit was applied to its unframed candidate before a new framed master was generated:

Use case: identity-preserve
Asset type: focused hair and complexion correction for the full-resolution fictional HOI4 advisor portrait “utopia_manifesto_interpreter”.
Input images:
- Image 1, docs/assets/gfx_fix_portraits_2026-10/source_png/advisor_utopia_manifesto_interpreter.png — authoritative identity and hair reference. Preserve the same woman’s face, facial proportions, medium warm-brown skin tone, age, eyes, nose, mouth, expression, and dark brown jacket with off-white blouse.
- Image 2, C:/Users/klimp/.codex/generated_images/01a10fb9-55b1-7621-8530-1694ae0c2f34/exec-5423ba85-cabb-4856-b1e2-20c263366306.png — edit target for this same person. Preserve the current head-and-shoulders composition, face geometry, expression, jacket, blouse, painted background, lighting, and painterly treatment.
Primary request: change only her hairstyle to match Image 1: dark hair drawn smoothly back from the forehead and temples, close to the head with no loose waves around her cheeks, not a bob, not shoulder-length curls. Keep her complexion at the medium warm-brown tone visible in Image 1.
Constraints: same person, same facial shape, asymmetry, age, gaze, pose, clothing, and painted background; alter only the hair silhouette/finish and complexion where the current candidate is lighter than Image 1.
Avoid: loose curls, waves, bob haircut, bangs, changed face, changed ethnicity, pale complexion, beautification, new accessories, frame, paper, text, logos, watermark.

Its v2 framed edit used the same source and the corrected unframed output as the edit target, with the minister_portrait_background.png reference for frame geometry only and transparency requested.

The Contract Broker source close-up showed a softer rounder face and warmer medium complexion than its first unframed candidate, so this focused edit was applied before generating a new framed master:

Use case: identity-preserve
Asset type: focused facial-identity correction for the full-resolution fictional HOI4 advisor portrait “utopia_manifesto_contract_broker”.
Input images:
- Image 1, docs/assets/gfx_fix_portraits_2026-10/source_png/advisor_utopia_manifesto_contract_broker.png — authoritative identity anchor. Preserve the same woman’s soft rounded cheek and jaw shape, medium warm complexion, apparent age, dark eyes, expression, and dark hair drawn close and back from the face.
- Image 2, C:/Users/klimp/.codex/generated_images/01a10fb9-55b1-7621-8530-1694ae0c2f34/exec-60456dcd-ab30-49b2-a822-bf1849ee91e3.png — edit target for this same woman. Keep its painterly HOI4 style, head-and-shoulders pose, brown jacket, dark blouse, neutral backdrop, lighting, and overall composition.
Primary request: correct the face to match the softer, rounder, warmer source appearance in Image 1. The current face is too pale and angular. Restore fuller cheeks and a rounder jaw, retain the medium warm skin tone, and keep the dark hair pulled back from the face.
Constraints: preserve this same fictional woman, her face, expression, hairline, age, clothing, head angle, and pose from Image 1; alter only facial fullness and complexion where Image 2 drifted.
Avoid: pale complexion, narrow angular face, pointed chin, younger appearance, loose shoulder-length curls, changed identity, changed gender, new accessories, frame, paper, text, logo, watermark.

Its v2 framed edit used the corrected unframed candidate as the edit target, the original source as the identity anchor, and minister_portrait_background.png for frame geometry only with real transparency requested.

The v2 generated outputs are C:/Users/klimp/.codex/generated_images/01a10fb9-55b1-7621-8530-1694ae0c2f34/exec-95cf4ad5-6758-40fb-aa43-d65b0a30ad87.png for Public Interpreter and exec-ae3b7e62-1647-4d06-b0eb-a7c9eb0ed601.png for Contract Broker.
