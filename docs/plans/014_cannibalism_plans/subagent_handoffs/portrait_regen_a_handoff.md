# Portrait Regeneration A Handoff

## Completed scope

- Regenerated all 28 Event 014 CBA-CBD regional/default warlord portraits as separate fictional image-generation sources.
- Installed all 28 at their exact existing 156x210 live DDS paths.
- Rejected and replaced nine close-shave/buzz-cut/stubble sources after an enlarged scalp audit; the final source set is 28/28 smooth bald.
- Made `leader_CBA_warlord_south_america` the required regional skull-lick portrait with unambiguous tongue-to-skull contact.
- Regenerated ordinary revealed Hannibal as a stronger static identity master with cloudy misaligned eye, damaged ear, scar web, irregular teeth, feral grin, and map-and-shelf command studio.
- Built 12 real image-model edit frames from that selected master, including approach, first contact, deliberate lick, retraction, and loop return.
- Assembled the 1872x210 horizontal sheet and 2-second/6-fps review GIF.
- Replaced only `leader_CBL_hannibal_static.dds` and `leader_CBL_hannibal_sheet.dds`; the separate `hannibal.dds` was preserved.

## Files and evidence

- Warlord package: `docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/`.
- Hannibal package: `docs/assets/014_cannibalism/leader_portraits_refresh/hannibal/`.
- Warlord contact sheet: `cba_cbd/contact_sheets/cba_cbd_warlords_contact_sheet.png`.
- Enlarged scalp audit: `cba_cbd/contact_sheets/cba_cbd_baldness_audit_contact_sheet.png`.
- Explicit 28/28 audit checklist: `cba_cbd/baldness_audit.md`.
- Hannibal processed contact sheet: `hannibal/previews/leader_CBL_hannibal_processed_contact_sheet.png`.
- Hannibal GIF: `hannibal/previews/leader_CBL_hannibal_preview.gif`.
- Detailed dimensions, header checks, visual review, and protected-file hash: `hannibal/validation.md`.
- Exact existing sprite bindings: `cba_cbd/gfx_handoff.md` and `hannibal/gfx_handoff.md`.

## Generation accounting

- 60 built-in image-generation invocations in total.
- 41 selected source deliverables: 28 warlords, one Hannibal static, and 12 Hannibal frames.
- Fourteen additional successful review outputs retained: nine rejected visible-hair warlords, four rejected over-composed first-pass bald replacements, and one rejected composed Hannibal static.
- Five failed/non-persisted attempts: an initial four-invocation warlord batch that yielded no persisted package outputs after moderation rejection, plus one rejected first attempt for Hannibal frame `005`.

## Validation result

- All 28 warlord sources and all 12 Hannibal frame sources are hash-unique.
- Enlarged source-crop review confirms all 28 approved warlords are smooth bald with no visible scalp hair or close-shave cues.
- All final portraits are 156x210; the animation sheet is 1872x210 and its slices exactly match the 12 processed frames.
- All 30 installed DDS files have valid uncompressed 32-bit BGRA headers, masks, dimensions, and exact byte lengths.
- All 30 DDS pixel payloads match their packaged PNG masters byte for byte after RGBA-to-BGRA channel ordering.
- Visual review found no prison/cell/confinement imagery anywhere in the package.
- Existing `interface/014_cannibalism.gfx` wiring already matches the outputs and was not edited.
- `hannibal.dds` hash is unchanged.

## Simplifications, omissions, and blockers

None. No placeholder, fallback, transform-only animation, gameplay/localisation/GFX/spreadsheet/spec/flag edit, or unrelated texture edit was used. No Git commit was created; the parent agent retains final diff review and commit ownership.

## Skills used

- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `imagegen`
