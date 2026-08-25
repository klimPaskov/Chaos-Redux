# IW-013 NAV José Antonio Aguirre source-placeholder archive re-audit — 2026-08-25

## Scope

This handoff covers only the grounded portrait evidence for the existing `NAV_independence_wave_jose_antonio_aguirre` army corps-commander consumer and leaves gameplay, central admission, character definitions, GFX wiring, and unrelated packages untouched.

The source-placeholder state is preserved, and this handoff does not claim final HOI4-style portrait completion because no user-supplied styled final was supplied for this task.

## Changed and created files

The durable source package follows the flat archive contract: the original master and exact source crop remain directly in `docs/assets/portraits/006_independence_wave/` under their dated `iw013_nav_jose_antonio_aguirre_source_placeholder_2026_08_13__...` names, while processed evidence is in the single `docs/assets/portraits/006_independence_wave/processed/` child.

The processed child retains only the non-156x210 review artifact `portrait_NAV_jose_antonio_aguirre_source_placeholder_native_4x_roundtrip.png`. The 156x210 PNG and evidence DDS are not retained in the archive. The temporary evidence-only HTML, JSON, review, and manifest files were removed from the asset tree during parent reconciliation; their source URLs, hashes, crop coordinates, rights status, and role evidence remain recorded here and in the current gap re-audit.

The `docs/assets/` tree is ignored by the repository policy, so these files exist as durable workspace evidence but may require the parent to force-add them if the package is to be committed.

The source-placeholder crop metadata was corrected to point at the co-located immutable master and to record the updated provenance-contract hash.

## Internet source and role evidence

Source page: https://commons.wikimedia.org/wiki/File:Jose_Antonio_Agirre,_Aberri_Eguna_1933.jpg.

Direct media: https://upload.wikimedia.org/wikipedia/commons/2/2c/Jose_Antonio_Agirre%2C_Aberri_Eguna_1933.jpg.

The source is attributed to Pascual Marín, Marín Collection / GureGipuzkoa, GureGipuzkoa photo 1112433, Aberri Eguna in Donostia-San Sebastián, 1933.

The Commons page was rechecked at 2026-08-25T13:17:28Z with HTTP 200 and archived locally at revision 858701972.

Role source: https://en.wikipedia.org/wiki/Jos%C3%A9_Antonio_Aguirre_(politician), archived locally at revision 1365420480.

The role source records Aguirre as the first Basque Lehendakari or president and records his defense responsibility during the Spanish Civil War, with the first Basque Government beginning on 1936-10-07.

The live game consumer is `NAV_independence_wave_jose_antonio_aguirre`, an existing `corps_commander` using `army.large` through `GFX_portrait_NAV_jose_antonio_aguirre`; commander-family vanilla references were used for framing review.

The ownership search covered `Aguirre`, `Agirre`, `José Antonio`, `Jose Antonio`, and `Lecube` across `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, `localisation/`, and installed vanilla character/portrait definitions; only the existing NAV consumer matched, so no alternate owner was duplicated or transferred.

## Rights status

The Commons description, categories, and JSON-LD identify CC BY-SA 3.0, while the current page also exposes a generic `rel=license` link to CC BY-SA 4.0.

Rights status is `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW`; no public-domain claim is made, and the package retains attribution, source URL, change notice, and ShareAlike requirements.

The 3.0 versus 4.0 metadata discrepancy remains an explicit blocker to unconditional rights acceptance.

## Asset evidence

The immutable master is 669x1024 RGB with SHA-256 `1d34f7b23459f750dcbfcb8e300dc3d41f7087c4b24caf544d6ab2f8671e6bc9`.

The exact source crop uses `[268, 235, 500, 510]`, is 232x275 RGB, and has SHA-256 `960948067a1478798f82da673099fff1d34bf9ca23b29bfa7fc8490ebf80f366`.

The deterministic processed PNG is 156x210 RGB with file SHA-256 `55ff6c989e4b93a4811c379192d1854b2f44222e5eb59d38671d6a6d8df4e496` and decoded RGBA SHA-256 `a46c355acd11daa0fb736a8ec6bf39e771c899aa90f9e1ac0cd8d62f937852a5`.

The evidence-only DDS produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` is 156x210 uncompressed BGRA, 131168 bytes, SHA-256 `8f38eefc44b92fbd2f55ca9bc1752fc4569050a4b8d1721ccb2bb587bc35ef73`, and decodes to RGBA SHA-256 `a46c355acd11daa0fb736a8ec6bf39e771c899aa90f9e1ac0cd8d62f937852a5`.

The retained native and 4x nearest-neighbour round-trip review is `docs/assets/portraits/006_independence_wave/processed/portrait_NAV_jose_antonio_aguirre_source_placeholder_native_4x_roundtrip.png`, SHA-256 `983daba9003cf894751658ee9dd0c33c7461fbb0af90ee9964319091445d73987`; the processed PNG and decoded candidate DDS remain aligned without visible geometry drift.

The current runtime DDS at `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds` was not changed and remains 131168 bytes with SHA-256 `19bed96acca3728eaf7cb79f861b097f1e12c3af4fabab8962af843f6e16ac7c` and decoded RGBA SHA-256 `83f74be0afbaa042596284920324f3cb301328a4649dc214193155dc309f90b5`.

The current runtime decoded pixels do not match the source-placeholder candidate, and the file appears to be a separate colored or styled candidate; this task does not authorize replacing it or treating it as an approved final.

## Review result and replacement state

Identity verdict: `PASS`; the source is the grounded José Antonio Aguirre and no alternate identity was introduced.

Framing verdict: `PASS`; the exact source crop and 156x210 commander canvas were reviewed against the installed commander reference family.

Provenance verdict: `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW`; the rights-version discrepancy and independent reviewer identity remain unresolved.

`portrait_state` remains `source_placeholder`, `styled_final` is `not_requested`, and `replacement_pending` remains `false`.

Existing stable runtime path and sprite wiring were preserved, and no GFX or character files were edited.

## Skipped checks and blockers

RunPod, ImageGen, and any final-style generation were skipped because the subject is grounded and no user-supplied styled final was supplied.

Gameplay, central admission, character setup, GFX wiring, live-game validation, and unrelated package review were skipped as out of scope.

The parent must record an independent reviewer and resolve the Commons license-version discrepancy before treating the evidence as unconditionally accepted.

The parent must separately decide whether the current runtime DDS is retained, replaced by an explicitly supplied final, or replaced by the archived source-placeholder candidate; no such replacement was performed here.
