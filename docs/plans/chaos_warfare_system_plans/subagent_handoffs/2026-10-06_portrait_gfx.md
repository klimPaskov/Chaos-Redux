# CBRN historical advisor portrait framing repair

Disposition: implemented for the six assigned CBRN historical advisor cards and approved by the parent on 2026-10-06 after review of the final DDS-derived sheets and overlay-edge audit. This is a portrait-only tranche and does not close the wider CBRN-11 requirement.

## Scope and accepted source

The parent task accepts the six `cbrn_historical_advisors` rows in the GFX repair owner table. The user confirmed on 2026-09-25 that the existing in-mod CBRN portraits are approved and recovery of their missing historical source archives is not a completion blocker; the disposition is recorded in [the portrait provenance audit](2026-09-25_cbrn_scientist_portrait_provenance_audit.md) and the CBRN-11 ledger entry. That approval supports deterministic framing, exposure, and edge corrections to these existing portraits while preserving identity and style.

Each small advisor card was recomposed from its existing approved `156x210` master in `gfx/leaders/scientists/portrait_<ID>.dds`. Five cards use a uniform 85% cover scale and upper-left placement. Kitano uses the same master with gamma `0.80` after the existing sepia blend and an upper-left placement at 85% cover scale; the 4x review confirms his face clears the note and both eyes remain readable. No new identity, sourced portrait, ImageGen art, placeholder, or RunPod output was used. No source-mode gate was changed, and no new provenance or rights claim is made for the existing master bytes.

| Person | Runtime path | Sprite and character consumer | Scale and local opening offset | Additional correction |
|---|---|---|---|---|
| `POL_franciszek_witaszek` | `gfx/interface/advisors/cbrn/POL_franciszek_witaszek.dds` | `GFX_idea_POL_franciszek_witaszek`; `civilian.small` | 85%; `(-5,-3)` | None |
| `SOV_grigory_mairanovsky` | `gfx/interface/advisors/cbrn/SOV_grigory_mairanovsky.dds` | `GFX_idea_SOV_grigory_mairanovsky`; `civilian.small` | 85%; `(-4,-4)` | None |
| `SOV_ivan_mikhailovich_velikanov` | `gfx/interface/advisors/cbrn/SOV_ivan_mikhailovich_velikanov.dds` | `GFX_idea_SOV_ivan_mikhailovich_velikanov`; `army.small` | 85%; `(-5,-3)` | None |
| `SOV_nikolay_zelinsky` | `gfx/interface/advisors/cbrn/SOV_nikolay_zelinsky.dds` | `GFX_idea_SOV_nikolay_zelinsky`; `civilian.small` | 85%; `(-6,-3)` | None |
| `GER_gerhard_schrader` | `gfx/interface/advisors/cbrn/GER_gerhard_schrader.dds` | `GFX_idea_GER_gerhard_schrader`; `army.small` | 85%; `(-5,-3)` | None |
| `JAP_masaji_kitano` | `gfx/interface/advisors/cbrn/JAP_masaji_kitano.dds` | `GFX_idea_JAP_masaji_kitano`; `civilian.small` | 85%; `(-7,-3)` | Gamma `0.80` after sepia `0.18` |

The complete per-person source, processed PNG, runtime DDS, dimensions, transforms, alpha coverage, and pixel-equality records are in the [portrait manifest](../../../assets/portraits/cbrn_historical_advisors/2026-10-06_reframing/manifest.md) and its per-person JSON files. All six runtime DDS files and processed PNGs are `65x67` RGBA; decoding each DDS reproduces its PNG pixels exactly. Before-state runtime hashes are preserved in `evidence/2026-10-06_cbrn_historical_advisors/before_runtime_hashes.json`.

| Person | Source master SHA-256 | Processed PNG SHA-256 | Runtime DDS SHA-256 |
|---|---|---|---|
| `POL_franciszek_witaszek` | `720bc822c3c8ae285573a0267fbcf2aea1b2a19ba5b698635fc9baa7a48a6670` | `7979504a829065a309fb8bbd2825ee7e0ee5858bd3ed76e16444d2bcbbf075ba` | `318d4552dceaec75104e24be01143a3e2501d449dcd5ecf13bd21324c4f3a6e3` |
| `SOV_grigory_mairanovsky` | `4204f5d12f1abe804eec65ec97aa593850e7ead78cde1f9603643b6b5631c6bc` | `32e6f1705e7613de91b9052a3f77cf62cd921d449ff03b60a3122536686070f5` | `f9b126b34733c2a707d65004d2e987abe05f5f585a89855edd8438966aa9f0d9` |
| `SOV_ivan_mikhailovich_velikanov` | `ca1c9c9dcf62ec22967269bf5fffe79a24dab0327aca44ff85d98a47da13677c` | `6c7be3e15f1241e8ef5c4b62bbf6d00e8807db912d13f8f03c1b4f983fdfa2d4` | `b0dbf0476a25421a7b6aff93bace0e4d17c52c5733f2706cdfac24da8ac478f6` |
| `SOV_nikolay_zelinsky` | `953b502bdc71ad4887963b69e82adb00f1d67d0bb77c0ff5424efe181ab5e597` | `9a4c0796569ca5152893abf3fd62866c1f0b5f49a0b0e9d023944ddd207c6437` | `3abf2fa4d3a69d52d5d87ee32b2cfb266c13b181228e0eaf654b053c62a7c9d8` |
| `GER_gerhard_schrader` | `078b0b105b82129750e386eccdf30bf072a9f47525f29124463ee5cf140411d1` | `2831bed2e80ac60dda5590ed285b4bd36b94871a9a5dc51961cb3c73d09caa89` | `c88806d729076914ad4d4f54ecc0f718335a06cdd7ef932affdcc9453e0d1f29` |
| `JAP_masaji_kitano` | `6a23c16ec9afee8a3e307172a996fe75e055bec58230c9f9711d7f4166aa0812` | `2c1b9dc5273a15a902f3d5eea875c80e476fb62b6e8dfdcd6eb3b2304c85b6d1` | `1fdbce57b6a085c21c293e1d391d8008fe9d8acc50189d5ab6b89bee91ae0273` |

## Frame and visual review

The canonical advisor template `advisor_template.png` is the exact unchanged final top layer. The six existing `.gfx` entries and character `small` portrait references retain their IDs and paths. The final DDS sheet and 8x template comparison showed the paper and frame remain inset and intact. The overlay audit records zero missing paper pixels, zero opaque-template pixel mismatches, and zero transparent output over a nontransparent template pixel; the paper bounds remain `[30,27,56,57]`, leaving nine pixels at the right edge of the 65px canvas.

The installed vanilla references `idea_generic_political_advisor_europe_1.dds` through `_6.dds` under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/ideas/` were inspected at `65x67` before inspecting the backdrop reference family. The native and nearest-neighbour 4x before/after contact sheets are in [the review evidence folder](evidence/2026-10-06_cbrn_historical_advisors/); it also contains one 4x placement study per person, the decoded final runtime sheet, the source-master sheet, the overlay comparison, the before hashes, and the overlay audit. The parent reviewed these images and approved all six cards on 2026-10-06.

## Changed files

- Six existing runtime DDS files under `gfx/interface/advisors/cbrn/`, named in the table above.
- Six processed `65x67` PNGs, six per-person metadata JSON records, one package summary, and the manifest under `docs/assets/portraits/cbrn_historical_advisors/2026-10-06_reframing/`.
- The accepted visual scope paragraph in `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md`.
- The CBRN-11 portrait status note in `docs/plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md`.
- The before/after sheets and review metadata under `docs/plans/chaos_warfare_system_plans/subagent_handoffs/evidence/2026-10-06_cbrn_historical_advisors/`.

The portrait package under `docs/assets/` is local working data and is intentionally ignored by the repository rule at `.gitignore:80`; its approval basis, transform details, hashes, and review evidence are summarized here and in the CBRN ledger.

No `.gfx`, character, gameplay, trait, event, focus, decision, localization, or UI wiring changed because the existing sprite IDs, texture paths, and character references already pointed to the six runtime files.

## Skipped checks and remaining limits

No Internet source archive was restored and no external licensing claim was added, per the user's 2026-09-25 waiver for already-installed portraits. The original source and provider/job lineage remain unavailable. No RunPod or game session was opened; live Hearts of Iron IV appearance validation remains user-owned. The parent review passed the file-level visual correction and overlay integrity; it does not claim broader CBRN completion.

Replacement state: none pending for these six framing corrections. No source placeholder is installed, and no user-supplied new styled portrait is required for this bounded reuse of the existing approved masters.

Selected final before/after, decoded runtime, source-master, placement and overlay proof stays in the plans evidence folder.
Superseded preview/candidate variations are retained as working studies under `docs/assets/portraits/cbrn_historical_advisors/2026-10-06_reframing/studies/`, without publishing every trial as final evidence.
