# Event 006 Frisia portrait-refinish handoff

Date: 2026-07-22  
Owner: generated-event-art asset subagent  
Scope: source-preserving portrait treatment only; the parent retains runtime
ownership and final acceptance.

## Delivered files

Package root:
`docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/frisia/`

- `source_masters/AGX_douwe_kalma.jpg` — unchanged source master, 545x667 RGB,
  SHA-256 `d8ce5c3cfe7d3b29bb9422139b21e83504f71dfd64a8fc0a821ef7d9b6501d9f`.
- `imagegen_masters/leader_AGX_douwe_kalma_imagegen_master.png` — raw
  ImageGen identity-preserving edit, 1081x1455 RGB, SHA-256
  `05ca0a2794fac5819f0c2c143b3e9f833d8139a218128d5552c10f0c6c14f5aa`.
- `processed_png/leader_AGX_douwe_kalma_156x210.png` — native 156x210 opaque
  RGB PNG, SHA-256
  `628157f9ec2dd956186a321d0260628f126637494ebc3246e8749f12544e9c89`.
- `source_masters/AGX_pieter_reenalda.jpg` — unchanged source master, 1243x1787
  grayscale, SHA-256 `2830fdc7d56040c2a3fa6a6f686bfd73126612786cc6eba80d428863190c488f`.
- `imagegen_masters/commander_AGX_pieter_reenalda_imagegen_master.png` — raw
  ImageGen identity-preserving edit, 1080x1456 RGB, SHA-256
  `ea0209e84fecb5702df53dbf82da70d1cb587fb2c218006216c8260c765cef7a`.
- `processed_png/commander_AGX_pieter_reenalda_156x210.png` — native 156x210
  opaque RGB PNG, SHA-256
  `d38acb3fe1432b378bbebe5d88ba3b55d2100397d6bb19ffd7716e67434fea05d5`.
- `prompts/leader_AGX_douwe_kalma_imagegen.txt` and
  `prompts/commander_AGX_pieter_reenalda_imagegen.txt` — exact prompts used.
- `review/contact_sheet.png` — source/raw/native comparison sheet for review only.
- `manifest.md` — source mode, role facts, paths, dimensions, hashes, crop method,
  identity verdicts, and explicit no-DDS boundary.

## Proposed runtime mapping (parent-owned)

| Identity | Native PNG handoff | Proposed existing runtime consumer | Proposed sprite/name note |
|---|---|---|---|
| Douwe Kalma | `processed_png/leader_AGX_douwe_kalma_156x210.png` | `portrait_AGX_friesland_coastal_council.dds` | Preserve the parent-provided leader token/name; no `_small` or advisor surface. |
| Pieter Reenalda | `processed_png/commander_AGX_pieter_reenalda_156x210.png` | `portrait_AGX_friesland_coastal_commander.dds` | Preserve the parent-provided commander token/name; full 156x210 texture only. |

## Acceptance and blockers

Both outputs are `needs_user_review` with provisional visual passes. The contact
sheet shows unchanged source → ImageGen master → 156x210 output. The same face,
age, expression, hair, and source-supported clothing/uniform are retained on visual
inspection; no invented people or prohibited props are present. Because ImageGen
touched real identities, parent human review is required before runtime acceptance.

No DDS conversion, `.gfx`, gameplay, localisation, character, advisor/dossier,
flag, or spreadsheet work was performed by this handoff. If either reviewer finds
identity drift, reject that portrait and do not substitute a generated or generic
person; return to the unchanged source master for a new bounded edit or mark it
blocked.
