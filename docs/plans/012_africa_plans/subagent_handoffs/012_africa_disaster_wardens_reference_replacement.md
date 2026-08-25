# Event 012 Africa disaster wardens reference-replacement handoff

Status: `parent_approved_exact_hash_geometry_passed_rig_recovery_blocked`.

## Outcome

The active single Meshy reference is parent-approved, fully colored, non-anime, period-compatible, and depicts a disaster warden whose complete rifle is held in a genuine combat-ready firing relationship.

- Active input: `docs/assets/012_africa/models_3d/disaster_wardens/refs/original/meshy_input.png`.
- SHA-256: `B5C29A3DB993E5C88E980B0C12F79E4EE60E8958D907AA5DBAB0EEFBA70BA146`.
- Dimensions/mode: 1422x1106 RGBA.
- Alpha: extrema 0..255; 1,174,618 transparent pixels; 398,114 opaque pixels; zero semitransparent pixels; all corners transparent.
- Approval: parent visual review passed color, period compatibility, non-anime style, full-body silhouette, trigger hand, support hand, stock-to-shoulder contact, complete barrel/muzzle/bayonet, base removal, and dark/light/green-checker alpha review on 2026-08-25. Any byte change requires renewed approval.

## Follow-on provider disposition — 2026-08-25

One bounded Meshy 7 generation followed approval, using the exact active hash, and produced accepted 25,000-triangle geometry under task `01a038b8-9bc6-758a-9981-2a5c7dd65ac8` for 30 credits.

The downloaded GLB SHA-256 is `1B73A95B382F8B9F780778BCA9FE4528976DC37FDCDFABBC2C3CC7F0BE525945` and the downloaded FBX SHA-256 is `652D99A6220907295F86ED1657ECAE906103EA0C95E76FE4281184A18FC59A38`; the firearm gate passed.

No further generation spend followed that bounded attempt. The first rig request is recorded in the redo handoff as task `01a038be-66f7-79aa-bd55-f9bd97eadc60`, terminal `FAILED` at 90% with `unexpected_error`, no download, and final `consumed_credits=0` after the transient 5-credit estimate/lock was refunded. One and only one failure-driven retry, task `01a038d2-b191-7f51-baa0-dd00a1d41daf`, also reached terminal `FAILED` at 90% with `unexpected_error`, no download, and `consumed_credits=0` after refund; the current observed balance is 13. No custom animation or local rig/action fallback was attempted.

All remaining rig, action, export, reimport, runtime, and in-game work remains blocked in `012_africa_disaster_wardens_meshy7_redo.md`; old-reference provider artifacts remain rejected and quarantined.

## Selected Internet artwork and terms

- Title: `B004 - British Infantry In Gasmasks`.
- Selected subject: exact top-right firing rifleman.
- Creator/manufacturer: Great War Miniatures.
- Publisher/retailer: North Star Military Figures Ltd.
- Product page: https://www.northstarfigures.com/prod.php?prod=562
- Official image: https://www.northstarfigures.com/product-images/562/lg/1.webp
- Terms: https://www.northstarfigures.com/terms-conditions.php
- Source fingerprint: 700x433 WebP, SHA-256 `DEE868C2BAB3FA086AA6F70492D9B0A5578C99BEA5DA47ECD6215212CCF26600`.
- Decision: `reference_only_user_authorized`. No explicit NoAI or no-derivatives restriction was found; no general archival/reuse license was stated. Standalone downloaded source bytes were deleted after fingerprinting and review. The labeled comparison excerpt is non-shipping evidence and must not enter runtime.

## Old-lineage rejection disposition

The old input SHA-256 `B73E80781FEC249AA7C96C95CC06BDBB499A3F6E1FD7EE5A601B27A75606AE80` is rejected and superseded because its grounded/abnormally held rifle cannot support normal combat. Exact bytes and its prior input manifest are preserved at `provider/rejected/superseded_reference_b73e8078/`.

All completed Meshy 7 attempts derived from that input are rejected and superseded, with immutable evidence retained: `01a033db-bbd0-74b5-b7f3-f2aec86cb89c`, `01a03402-77f9-7d7f-938e-cf6fae54148d`, `01a0340f-4af0-78be-a3f5-60157d98df46`, `01a03419-e76f-7cd3-996d-d0d3ec181b5f`, and `01a03429-ae8c-7253-b32c-65eb6d80b05f`. Historical spend remains 150 credits. The recovery 6 transport failure created no task and incurred no charge.

## Evidence

- Source search and rejections: `refs/source/source_replacement_search_2026-08-25.md`.
- Machine-readable provenance: `refs/source/replacement_provenance_2026-08-25.json`.
- Prompt record: `refs/briefs/meshy_input_replacement_prompts_2026-08-25.md`.
- Processing/alpha QA: `validation/evidence/reference_replacement_processing_2026-08-25.md`.
- Source-to-cleanup/dark-light-checker comparison: `validation/evidence/reference_replacement_comparison_2026-08-25.png`, SHA-256 `BECAED65B48A53B2128F420A2A674929A916F177E280674698E590C76DDC101D`.
- Active input manifest: `refs/original/input_manifest.json`.
- Updated package state: `job.yaml`, `manifest.md`, and `history.jsonl`.

## Required parent work

1. Treat the exact active input hash as parent-approved and immutable.
2. Do not begin another generation or recovery spend without a new bounded parent decision; the one approved generation and one permitted rig retry are already recorded above.
3. Continue to treat all old-reference provider artifacts as rejected and never promote them.

No runtime, gameplay, GFX, entity, sound-definition, localisation, spreadsheet, Blender, adapter, or runtime wiring file was modified in this reference-replacement handoff; the later Meshy generation and failed/refunded rig request are evidence-only and remain parent-owned for any future promotion.
