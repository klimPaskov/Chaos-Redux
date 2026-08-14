# IW-153 POK compatibility audit (2026-08-12)

> Historical audit snapshot. The current dormant compatibility boundary and current-source preservation evidence are recorded in `006_iw153_pok_compatibility_adapter_2026_08_14.md`; the older 31/28/162/39 arithmetic and manifest-failure wording below remain dated traceability only.

## Disposition

IW-153 Dayak Federation remains unbound and fail-closed. No gameplay, central adapter, content-attestation, Join, flag, portrait, or localisation source was changed by this audit.

The accepted representation is a specific-community variant that reuses vanilla `POK` only after a named Dayak polity or river-region federation is selected. The broad “Dayak federation” label is not permission to invent a pan-Dayak leader, flag, capital, or automatic release.

## Vanilla preservation contract

Vanilla registers `POK` as `countries/Pontianak.txt` in `common/country_tags/00_countries.txt`. Its history file is `history/countries/POK - Pontianak.txt`, with capital state 334 (Kalimantan Barat), two research slots, the vanilla starting technology block, and `recruit_character = INS_syarif_muhammad_alkadrie`.

Vanilla state files assign `POK` cores in state 334 (`history/states/334-Kalimantan Barat.txt`) and state 1022 (`history/states/1022 - Interior Borneo.txt`). Those cores and the installed country history must remain authoritative when the Event 006 compatibility context is absent.

Vanilla Indonesia records `POK` in the `INS_releasables` array in `history/countries/INS - Indonesia.txt`. The vanilla `common/scripted_effects/INS_scripted_effects.txt` defines `indonesia_transfer_POK`: when `POK` exists, it changes `INS_syarif_muhammad_alkadrie` nationality to `INS`, removes the despotism country-leader role while retaining the advisor transfer target, and stores the global character target; when `POK` does not exist, it finds the character on another country and performs the same nationality/target transfer.

The compatibility adapter must therefore preserve all four surfaces together: Pontianak history, the vanilla character and role transfer, the POK cores, and `INS_releasables` membership. A tag-only `original_tag = POK` check is insufficient.

## Current Chaos Redux source evidence

`common/script_constants/006_independence_wave_package_constants.txt` defines package id `iw_153`, and the registry constants include `POK` among registered carriers. However, the Region 13 package loader has no `independence_wave_load_package_iw_153` block, no anchor/host event-target transaction for IW-153, and no current package-specific setup/final-validation/cleanup adapter.

The central dispatcher and content-attestation lists do not include IW-153. This is correct for the current `specific_community_variant_only` and unbound disposition; adding a dormant helper alone would not make the package playable and would risk presenting broad Dayak content before the accepted identity decision.

The existing `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt` only proves generic registered-tag membership. It does not prove POK history, cores, releasable membership, or the `indonesia_transfer_POK` behavior. No existing Event 006 file references `indonesia_transfer_POK` or provides a POK-specific preservation receipt.

## Safe next implementation boundary

Before any POK runtime adapter is written, the project needs an accepted named polity or river-region scope, exact current-map anchor and host-remnant contract, a sourced leader/institution and flag decision, and a route entry that can invoke the compatibility helper without changing ordinary Pontianak or Indonesian behavior.

The eventual adapter should be origin-gated and non-selectable until that contract exists. Its setup proof should verify `original_tag = POK`, the exact Event 006 package id, state 334 anchor ownership/control, the vanilla character and cores, and the releasable context; its cleanup proof should clear only Event 006 flags/ideas/variables and leave vanilla POK history, cores, character transfer, and INS release behavior untouched.

## Validation and blockers

The required offline wiki and vanilla scripted-effects/history references were consulted. Current HOI4 MCP map, event, focus, and probability calls are blocked before source inspection by `ARTIFACT_MANIFEST_INVALID` for workspace `mod_chaos_redux_ea3b2d67c2c0`; no engine receipt is claimed.

The static allocator/scenario audits remain the current source checks, with the whole-event authority at 31 content-attested packages, 28 compatible reservation groups, 162 unattested selectable rows, and 39 adapters. IW-153 remains outside those admitted lists.

No fallback tag, generic leader, synthetic historical flag, or broad automatic package was introduced.
