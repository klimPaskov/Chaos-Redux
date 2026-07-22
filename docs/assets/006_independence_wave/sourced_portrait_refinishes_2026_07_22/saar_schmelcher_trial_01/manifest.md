# IW-010 Saar Willy Schmelcher portrait trial 01

Date: 2026-07-22

Status: `rejected_independent_visual_audit`; no DDS or runtime overwrite is
authorized by this package. The source and trial remain provenance evidence
only.

This package applies the built-in ImageGen identity-preserving edit workflow to
an unchanged, sourced 1938 portrait of the real male Willy Schmelcher. Saar is a
grounded polity, so ImageGen supplies only the HOI4 painted finish; it does not
authorize a fictional or substitute identity.

## Source and role

- Intended package/role: IW-010 AJX Saar industrial-security commander.
- Stable runtime character token: `AJX_karl_becker`; if this portrait passes,
  its player-facing name and biography must identify Willy Schmelcher while the
  stable script token may remain unchanged.
- Stable sprite: `GFX_portrait_AJX_karl_becker`.
- Authoritative existing texture path:
  `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds`.
- Subject: Willy Schmelcher (1894-1974), Polizeipraesident in Saarbruecken from
  1935, providing an exact period and regional security-role fit.
- Source authority: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wallonia_saar_retry_01/manifest.md`.
- Unchanged local source:
  `source_masters/AJX_willy_schmelcher_commander_1938.jpg`; JPEG, `539x703`,
  SHA-256 `a843a31c949b1128d857365f2e27c53e4897d7d2c62d6e2fd3b600c6823d2ad7`.
- Rights basis: the source ledger records the 1938 Reichstag publication,
  Commons public-domain metadata, and its `PD-Germany-§134` basis. The
  politically charged historical role must remain factual and unglamorized.

## Edit and processing evidence

- The first edit attempted to retain the source uniform neutrally and was
  rejected by the built-in image service before an output was produced. No
  artifact from that attempt exists.
- The accepted processing attempt changes only the charged uniform into a
  plain, historically plausible 1930s dark civilian administrative suit. This
  is a disclosed moderation-driven clothing adjustment, not a claim that the
  source depicts Schmelcher in that suit.
- Prompt: `prompts/AJX_willy_schmelcher_identity_preserve_trial_01.txt`.
- Identity/edit target: the unchanged Schmelcher source above.
- Style-only reference:
  `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/contact_sheet.png`;
  no face, ethnicity, identity, or clothing transfer was authorized.
- Raw ImageGen master:
  `raw_masters/AJX_willy_schmelcher_hoi4_trial_01.png`; `1081x1455` RGB,
  SHA-256 `46bdcf6db2521ec019d31460a8b71833a41f92259515df462ba4b2a74081d70d`.
- Processed native review PNG:
  `processed_png/AJX_saar_industrial_security_commissioner.png`; `156x210`
  opaque RGBA, SHA-256
  `23e5b6317eba3602d907a6bd0a01a574c730f0a4c481e2b58e0fd21176666f7b`.
- Exact processing: crop `(0, 0, 1080, 1454)` from the raw master, leaving one
  unused pixel at the right and bottom, then Lanczos resize to `156x210` and
  conversion to opaque RGBA. No post-generation face edit or filter was used.
- Comparison sheet:
  `contact_sheets/source_result_style_comparison.png`; SHA-256
  `0899be676a31d8e22c3fc6afb28e184fbde6463389a6384e5b2805574e4e6c3e`.

## Independent audit disposition

The independent review in
`docs/plans/006_independence_wave_plans/subagent_handoffs/006_saar_schmelcher_trial01_visual_audit_2026-07-22.md`
rejected this trial. Direct comparison found identity drift in the brows, eyes
and gaze, nose tip, moustache, jaw, and apparent age. Replacing the sourced
uniform with a civilian suit was also not accepted as source-preserving role
evidence. The processed PNG is therefore fail-closed provenance only: do not
convert it to DDS, overwrite the runtime texture, rename the runtime character,
or change the sprite. A later attempt requires another attributed photograph
or a source-preserving treatment that passes a fresh independent review.

No advisor, dossier, `_small`, female, flag, focus, decision, or gameplay asset
is created here.
