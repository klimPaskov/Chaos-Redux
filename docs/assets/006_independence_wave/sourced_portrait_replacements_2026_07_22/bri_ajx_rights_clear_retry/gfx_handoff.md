# Event 006 BRI/AJX portrait source retry — GFX handoff

Date: 2026-07-22  
Scope: source provenance and proposed sprite names only. No `.gfx` file was edited.

The parent agent owns final role approval, native portrait processing, independent
visual review, DDS conversion, and runtime wiring. Do not copy a sprite entry for
a role whose source status is `needs_review` or `blocked`.

## Proposed sprite table

| Proposed sprite name | Intended target `.gfx` | Deferred DDS path | Candidate/source status | Handoff action |
|---|---|---|---|---|
| `GFX_portrait_BRI_independence_wave_civic_commission` | `interface/_leader_portraits.gfx` (or the parent package's dedicated leader GFX file) | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds` | Blocked; Marcel Cachin is `rejected_current_role_mismatch` for the oligarchic traditional/patron token | Do not wire Cachin here. Retain him only as a possible separately implemented labor-route identity; source a real Breton regionalist for this sprite. |
| `GFX_portrait_BRI_independence_wave_coastal_commandant` | `interface/_leader_portraits.gfx` (or dedicated package file) | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds` | Henri-Léon Devin `source_ready` | Process as a full `156×210` portrait; his École navale command at Brest supplies the 1936 Joint Coastal Command fit. Do not depict or describe him as maritime prefect before September 1936. |
| `GFX_portrait_AJX_saar_municipal_neutral_commission` | `interface/_leader_portraits.gfx` (or dedicated package file) | `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` | Johannes Hoffmann — `needs_review_rights` | Do not process until independent US redistribution evidence is recorded. |
| `GFX_portrait_AJX_saar_industrial_security_command` | `interface/_leader_portraits.gfx` (or dedicated package file) | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_command.dds` | `blocked` | No fallback portrait; source a new rights-clear, role-valid candidate in a later retry. |

## Source path for the one current-role ready candidate

`source_masters/BRI/BRI_leon_henri_devin_brest_prefet_1930.jpg`

The source is a 6318×8587 Gallica IIIF original from Agence Rol (1930),
SHA-256 `ab7d69e6f485be51bfc02823bf94187a9239b54f56525ff97223c9e7b2f7e4c0`.
Its face, cap, and upper uniform are clear and crop-capable. The manifest
contains the source URLs, public-domain basis, role evidence, and ownership-scan
result. Marcel Cachin's source remains retained only for a possible future
labor-route identity and is not ready for the current civic token.

## Runtime snippet policy

No ready-to-copy sprite snippet is supplied because this retry deliberately stops
before PNG/DDS generation and parent-owned `.gfx` edits. Once the parent has an
approved native portrait DDS, the usual sprite declaration should be copied from
the existing Chaos Redux leader-portrait pattern with the exact proposed name
and deferred path above; do not point a live entry at a source JPEG or at a
review-gated candidate.

## Explicit non-wiring evidence

- `BRI_jean_marie_abrial_gallica_rol_brest_1929_original.jpg` and its
  size-negotiated derivative are retained only to document a clean source that
  collides with vanilla's active FRA Abrial identity.
- `BRI_raoul_castex_brest_prefet_1935.jpg` is a rights-clear role lead but a
  bust/sculpture photograph, not a period headshot, and is rejected for this
  portrait brief.
- No AJX commander DDS or source master is present; the role remains blocked.
