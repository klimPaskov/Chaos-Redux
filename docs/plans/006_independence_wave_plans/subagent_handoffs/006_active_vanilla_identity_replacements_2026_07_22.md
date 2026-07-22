# Event 006 active vanilla identity replacements

Date: `2026-07-22`

Status: `gameplay_localisation_replacement_complete_portrait_runtime_deferred`

## Scope

This patch replaces the three grounded Event 006 identities that were rejected
because the same people are active vanilla characters. Stable Event 006
character tokens and all existing portrait sprite and DDS paths remain intact.
The package setup remains guarded and fail-closed. No readiness attestation,
asset, GFX, DDS filename, advisor content, unrelated character, or historical
research handoff was changed.

The source-ready primaries are retained in the parent-provided package:
`docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/`.

## Changed files and identifiers

- `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml`
  - `RHI_independence_wave_provisional_directorate`: `Konrad Adenauer` ->
    `Karl Jarres`.
  - Added `RHI_independence_wave_provisional_directorate_desc` with Jarres's
    Rhenish municipal and Weimar constitutional context.
  - `BAY_independence_wave_mountain_commandant`: `Franz Ritter von Epp` ->
    `Eugen Ritter von Schobert`.
  - Replaced the stale `BAY_independence_wave_mountain_commandant_desc` with
    Schobert's documented Würzburg, Royal Bavarian Army, and pre-crisis
    infantry-command context.
- `localisation/english/006_independence_wave_scotland_wales_l_english.yml`
  - `SCO_independence_wave_territorial_commandant`: `Edmund Ironside` ->
    `Victor Morven Fortune`.
  - Added `SCO_independence_wave_territorial_commandant_desc` with Fortune's
    Scottish-born Black Watch and 52nd (Lowland) Division command context at
    the scenario start.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_active_vanilla_identity_replacements_2026_07_22.md`
  - This handoff.

## Stable gameplay consumers and before/after behavior

The generated character definitions remain in their existing setup effects:

- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`
  - `independence_wave_prepare_rhi_roster_and_portrait` retains
    `RHI_independence_wave_provisional_directorate` and
    `GFX_portrait_RHI_independence_wave_provisional_directorate`.
  - `independence_wave_prepare_bay_roster_and_portrait` retains
    `BAY_independence_wave_mountain_commandant` and
    `GFX_portrait_BAY_independence_wave_mountain_commandant`.
- `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt`
  - `independence_wave_prepare_sco_institutional_roster` retains
    `SCO_independence_wave_territorial_commandant` and
    `GFX_portrait_SCO_independence_wave_territorial_commandant`.

The exact create/recruit and portrait call sites remain stable at
`generate_character` token/name pairs RHI 232-233, BAY 306-307, and SCO
231-232, followed by the existing `set_portraits` hooks RHI 244, BAY 323-325,
and SCO 248-250. Promotion consumers also remain stable for the existing route
contracts (`promote_character` RHI 425/451/469/497, BAY 557, and SCO 427).

Each setup path still creates the character only under its existing
`NOT = { has_character = ... }` guard, assigns the existing male country-leader
and/or corps-commander roles, and then applies the same stable portrait sprite.
There are no Event 006 history `recruit_character` calls for these generated
tokens. `generate_character` remains the create-and-recruit call at the exact
setup sites, and its package initialization remains gated by the existing
`can_initialize_independence_wave_iw_001/iw_008/iw_009_package` checks. No trait
was added or removed because the source package supports the identity and role,
but does not establish a distinct Event 006 trait requirement.

Before the patch, the three stable tokens displayed the active vanilla names
Konrad Adenauer, Franz Ritter von Epp, and Edmund Ironside. After the patch,
the same tokens display Karl Jarres, Eugen Ritter von Schobert, and Victor
Morven Fortune, with grounded descriptions where the package needs biography.
Portrait processing and independent visual admission remain deferred, so the
package does not claim runtime portrait readiness.

## Source and ownership evidence

The selected replacement primaries and unchanged source hashes are recorded in
the parent package manifest and source hash list:

- Karl Jarres: `source_masters/RHI/RHI_karl_jarres_bundesarchiv_1925.jpg`,
  SHA-256 `72c952b0f1a1e3c08a16b20c123466b4bfc737d7c03ae63594cf7e6332c2c8d6`.
- Eugen Ritter von Schobert: `source_masters/BAY/BAY_eugen_von_schobert_nac_1940.jpg`,
  SHA-256 `0512bb979b5bac234eac4c0c61f397664ba97e64cf1626ec95aa05d6d99e7f83`.
- Victor Morven Fortune: `source_masters/SCO/SCO_victor_fortune_iwm_1940_portrait.jpg`,
  SHA-256 `830f175712988c825a604e48464584dc0b71cd61b51ab423e2badc0c1a46d049`.

The bounded ownership scan covered installed vanilla and current Chaos Redux
`common/characters`, `history/countries`, `common/country_leader`, `interface`,
`gfx/leaders`, and `localisation/english` roots. Exact, token, and common name
variants for all three replacement identities returned no hits. The former
identities remain documented as rejected active vanilla ownership findings in
the existing parent-owned Event 006 audits and are intentionally not reused.

## Validation

- Confirmed the three replacement identities have no active vanilla or current
  Chaos Redux roster/name/portrait ownership hits using exact and variant scans
  across the roots above.
- Confirmed the old names have no remaining references in Event 006 gameplay or
  Event 006 English localisation files. Historical docs and parent handoffs were
  intentionally excluded from this stale-runtime-reference check.
- Confirmed all three stable Event 006 character tokens, setup function names,
  `generate_character` guards, and `GFX_portrait_*` sprite names remain present
  and unchanged in the setup files.
- Confirmed both edited localisation files retain UTF-8 BOM encoding.

Meaningful validation skipped: no game launch or portrait rendering was run.
The replacement source package contains unchanged source masters only, with no
processed PNG/DDS output, and the parent owns the later visual/rights review and
runtime admission. No readiness attestation was changed.

## Residual risks and parent follow-up

- The stable portrait sprite/DDS paths still point at the existing Event 006
  portrait consumers. They must be independently processed and approved from
  the selected source masters before runtime admission. The low-resolution
  Fortune primary and Schobert's infantry-versus-mountain role caveat remain
  documented in the source manifest.
- Event 006 remains fail-closed until the parent completes portrait processing,
  visual/rights approval, and the post-replacement country-package and
  ownership audit. This patch does not alter readiness flags or make the
  packages selectable by itself.
- Alternate Jarres/Schobert/Fortune source masters in the package remain
  deferred and must not be substituted without the documented review decision.

No fallback, generated portrait, generic replacement, advisor content, GFX
change, or unrelated character change was made.
