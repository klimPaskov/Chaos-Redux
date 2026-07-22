# Event 006 WLS / AFX rights-clear portrait retry handoff

Date: `2026-07-22`

Status: `blocked_no_source_ready_candidate`

## Scope and result

This retry was limited to the parent-requested grounded male commander roles:

| Package / role | Best research lead | Disposition | Blocking gate |
|---|---|---|---|
| `IW-002 WLS` Welsh territorial / mountain commander | Gervase Thorpe (GOC 53rd (Welsh) Infantry Division, June 1935-June 1939) | `blocked` | No defensible period redistribution source; only Generals.dk and rights-ambiguous family/Wikipedia leads. Geoffrey Raikes and Wilfrith Green also lacked an accepted source; Cubitt was NPG/role-date unsuitable. |
| `IW-006 AFX` Belgian reserve / military commander | Victor van Strydonck de Burkel (Flemish/Antwerp-born Belgian cavalry general) | `blocked` | The IWM/Commons source is otherwise period-capable and marked public domain, but vanilla actively owns Victor as `BEL_victor_van_strydonck_de_burkel`. Raoul Van Overstraeten is likewise active vanilla-owned; Jules Pire, de Nève de Roden, Michem, Six, and Dossin had rights/source/timing failures. |

No accepted source-ready candidate exists for either slot. No generated face,
generic substitute, fallback, PNG, DDS, `.gfx`, gameplay, or localisation edit
was made. The runtime portraits remain withdrawn pending a new source that
clears every gate.

## Source package

The complete bounded manifest, rejection ledger, ownership evidence, search log,
and deferred processing state are in
[`wls_afx_rights_clear_retry/manifest.md`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wls_afx_rights_clear_retry/manifest.md).

The only retained binary is an unchanged, rejected audit bitstream:

- `source_masters/AFX/AFX_victor_van_strydonck_iwm_1943.jpg`
- 904 x 1300 RGB JPEG; 123,082 bytes
- SHA-256: `244df6dd6ef2d3e72e699c9a1c27282a04e708d6d72a0d274300b174774268ef`
- [Commons file record](https://commons.wikimedia.org/wiki/File:United_Nations_Day_Parade,_London,_14_June_1943_TR1113.jpg)
- [IWM object TR 1113](https://www.iwm.org.uk/collections/item/object/205188666)

The source ledger is [`source_hashes.sha256`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wls_afx_rights_clear_retry/source_hashes.sha256), and the explicit no-wire state is [`gfx_handoff.md`](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wls_afx_rights_clear_retry/gfx_handoff.md).

## Ownership checks

The narrow scan covered only the relevant current-project and installed-vanilla
roots (`common/characters`, `history/countries`, `gfx/leaders`, `interface`,
and `localisation`) and exact/variant name and stem tokens.

- Current Chaos Redux: no hits for Victor van Strydonck, Raoul Van Overstraeten,
  Gervase Thorpe, or Geoffrey Raikes.
- Installed vanilla: Victor is actively defined at
  `common/characters/BEL.txt:595` and recruited in
  `history/countries/BEL - Belgium.txt:327` and `:370`; Van Overstraeten is
  actively defined at `common/characters/BEL.txt:398` and recruited at
  `history/countries/BEL - Belgium.txt:325` and `:368`.

The vanilla ownership gate is dispositive even where Victor's Commons/IWM
source has a plausible public-domain basis. Do not duplicate or override the
vanilla identity.

## Parent follow-up

1. Keep both Event 006 runtime commander portraits blocked; do not wire the
   retained Victor source.
2. If another source search is authorized, require a one-person image with a
   defensible rights chain, alive and role-valid on 1936-01-01, and no active
   vanilla/current-project identity collision before processing.
3. Process only a future accepted source through the approved leader-portrait
   pipeline and obtain separate visual/rights review before creating DDS.

## Files changed by this handoff

- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wls_afx_rights_clear_retry/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wls_afx_rights_clear_retry/source_hashes.sha256`
- `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wls_afx_rights_clear_retry/gfx_handoff.md`
- unchanged rejected source master under that package's `source_masters/`
- this dated handoff file

No existing gameplay, localisation, interface, GFX, specs, or skill files were
changed.

