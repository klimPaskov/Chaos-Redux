# Event 006 BRI/AJX rights-clear portrait source retry handoff

Date: 2026-07-22  
Producer: `/root/event6_bri_ajx_source_retry`  
Scope: sourced real-person research only; no gameplay, localisation, `.gfx`,
portrait processing, PNG, or DDS edits.

## Package and manifest

- Source package: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/`
- Manifest: [manifest.md](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/manifest.md)
- GFX handoff: [gfx_handoff.md](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/gfx_handoff.md)
- Hash ledger: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/source_hashes.sha256`
- Search/ownership notes: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/search_notes/ownership_and_candidate_log.md`

## Result by requested role

| Role | Result | Candidate and evidence |
|---|---|---|
| BRI civic commission | `rejected_current_role_mismatch`; `source_ready_labor_identity_only` | Marcel Cachin has an excellent Agence Meurisse/Gallica 1918 source, was born in Paimpol, was alive in 1936, and has no active owner. However, the existing civic-delegate token becomes the oligarchic traditional or patron-route leader; Cachin's socialist/communist career is not plausible for that office. He may be used only if a separate labor-route character slot is deliberately implemented. |
| BRI coastal commandant | `source_ready` | Henri-Léon Devin has a clean Gallica/Agence Rol 1930 headshot and rights basis. He commanded the École navale at Brest from September 1930, which is valid for the accepted Joint Coastal Command role on 1936-01-01; the later maritime-prefect appointment is not required by that role. Raoul Castex's bust is unnecessary, and Abrial/Huntziger remain rejected active vanilla identities. |
| AJX/Saar municipal neutral commission | `needs_review_rights` (exact role blocked pending evidence) | Johannes Hoffmann, Saar-Nostalgie/Brazilian Immigration Agency photo, 1941, 306×408, SHA-256 `9f9032681cd7cb2f087d2b89cd7932c8702e1fe872e33533cd754d19819416cf`; clear face and Saar civic identity, but family-estate source and URAA/US status are unresolved. |
| AJX/Saar industrial-security command | `blocked` | Anton Dunckern, Willy Schmelcher, Theodor Berkelmann, and Kurt Daluege were screened; each fails rights, role, or both. No generic/generated fallback is allowed. |

## Ownership findings

Vanilla active character/portrait ownership was confirmed for Abrial and
Huntziger, so neither may be repurposed for BRI. No active character/portrait
owner was found for Cachin, Devin, or Hoffmann; the only Castex hit was a
historical naval-unit comment, not a portrait owner.

## Parent actions

1. Do not wire Marcel Cachin to the existing civic-commission sprite. Retain his
   source and visual treatment only as a labor-route candidate. Research a real
   male Breton regionalist/traditional civic figure for the current token;
   Régis de l'Estourbeillon is a strong lead subject to source and ownership
   review. Event 006 does not use advisor/dossier portrait assets.
2. Treat Devin as the source-ready Joint Coastal Command identity. His command
   of the École navale at Brest from 1930 supplies the required start-date naval
   and regional fit; do not relabel him as maritime prefect before September
   1936 and do not substitute Castex's bust.
3. Obtain independent US redistribution evidence for Hoffmann before processing;
   otherwise keep the AJX civic role blocked.
4. Keep the AJX commander blocked until a role-valid, rights-defensible period
   portrait is found. Do not wire source JPEGs, rejected Abrial derivatives, or
   any generated face.

## Residual risks and simplifications

- BRI coastal command has a source-ready master, but the current BRI
  traditional/patron civic slot remains source-blocked after Cachin's role
  mismatch. AJX civic is rights-review-gated, and AJX command remains blocked.
- No processed PNG, DDS, contact sheet, or `.gfx` edit is included by design;
  the parent portrait pipeline owns those steps.
- The retained Castex bust and Abrial originals/derivative are rejection
  evidence only and must not be treated as approved portrait inputs.
