# 005 Soviet Collapse localisation style cleanup handoff

Scope: `localisation/english/005_soviet_collapse_l_english.yml` only. The pass preserves every localisation key, dynamic token, format code, route meaning, and scripted-localisation contract.

## Changed files and keys

- `localisation/english/005_soviet_collapse_l_english.yml` received 296 changed values.
- Early event prose was rewritten at `chaosx.nr5.2.d`, `chaosx.nr5.3.d`, `chaosx.nr5.5.d`, `chaosx.nr5.7.d`, `chaosx.nr5.8.d`, `chaosx.nr5.9.d`, `chaosx.nr5.10.d`, `chaosx.nr5.13.d`, `chaosx.nr5.14.d`, `chaosx.nr5.16.d`, `chaosx.nr5.20.d`, `chaosx.nr5.23.d`, `chaosx.nr5.24.d`, `chaosx.nr5.31.d`, `chaosx.nr5.34.d`, `chaosx.nr5.37.d`, `chaosx.nr5.40.d`, `chaosx.nr5.41.d`, `chaosx.nr5.42.d`, `chaosx.nr5.44.d`, `chaosx.nr5.45.d`, `chaosx.nr5.51.d`, `chaosx.nr5.71.d`, `chaosx.nr5.77.d`, `chaosx.nr5.91.d`, `chaosx.nr5.98.d`, `chaosx.nr5.99.d`, and `chaosx.nr5.134.d`.
- Super-event copy was rewritten at `chaosx_super_event.15.d`, `chaosx_super_event.16.d`, and `chaosx_super_event.18.d`.
- Decision, focus, and mission requirement text had list punctuation changed to readable comma or sentence structures while retaining all costs, gates, variables, and icons.
- The live release ledger text at `soviet_collapse_review_republic_release_risk_desc` now starts with `The release ledger shows` instead of an instruction to use the ledger.
- Dynamic reward families were made route-specific for Ukraine, Belarus, Kazakhstan, generic breakaways, Baltic routes, Caucasus routes, Central Asian routes, and Moldova across political, army, industry, expansion, foreign, League, and opening keys.
- The repeated custom-splinter route descriptions now identify their local institutions for FTH, AOX, AEX, UDC, SDZ, and TNC at the mobilization, civilian-rule, extreme-gate, claim-consolidation, enemy-front, propaganda, extreme-route, foreign, settlement, hidden-doctrine, legitimacy, stores, economy, internal-faction, and late-program keys.
- Custom event reports at `chaosx.nr5_custom.1.d`, `.2.d`, `.3.d`, `.4.d`, `.5.d`, `.13.d`, and `.18.d` now state each authority's institutions and actors directly instead of asking whether it is a government, mutiny, or emergency committee.

## Before and after examples

- `chaosx.nr5.2.d` changed `The first declarations are not only speeches. They come with soldiers...` to `The first declarations arrive with soldiers...`.
- `chaosx.nr5.24.d` changed a semicolon-heavy list into direct sentences about committees, the Supreme Soviet, and recruiters.
- `ukr_soviet_collapse_focus_black_banner_dynamic_reward_tt` changed a generic route-template description into `Strengthens the Black Banner route through Ukrainian institutions, recognition, resilience, and rural enforcement capacity.`
- `FTH_propaganda_desc` changed the shared `Broadcasts and manifestos speak to the former Union` template into a black-banner and village-manifesto description tied to the Free Territory.
- `soviet_collapse_review_republic_release_risk_desc` still exposes every live forecast value and lock status, but its opening now describes the ledger state directly.

## Audit results

Missing player-facing keys: none found in 455 direct title, description, option, tooltip, category, name, and text references extracted from the Soviet Collapse event and decision sources.

Scripted-localisation targets: all 164 `localization_key` targets in `common/scripted_localisation/005_soviet_collapse_scripted_localisation.txt` resolve to keys in the 005 English file.

Scripted-localisation display references: the five dynamic names used by the 005 file are `GetSovietCollapseFirstMonthReleaseLockStatus`, `GetSovietCollapseProgressiveReleaseCooldownStatus`, `GetSovietCollapseReleaseRollGateStatus`, `GetSovietCollapseSelectedSponsorInfluenceColored`, and `GetSovietCollapseStrongCenterReleaseLockStatus`; all resolve across `common/scripted_localisation/`.

Duplicate keys: zero case-sensitive duplicate keys were found among 10,343 parsed keys.

Case-fold collision list: `ilx_observatory_guard`, `ILX_observatory_guard`, `ilx_observatory_guard_desc`, `ILX_observatory_guard_desc`, `ilx_starfall_mandate`, `ILX_starfall_mandate`, `ilx_starfall_mandate_desc`, `ILX_starfall_mandate_desc`, `icd_citizens_after_death`, `ICD_citizens_after_death`, `icd_citizens_after_death_desc`, `ICD_citizens_after_death_desc`, `ikx_reliquary_guard`, `IKX_reliquary_guard`, `ikx_reliquary_guard_desc`, `IKX_reliquary_guard_desc`, `nrf_northern_revenant_fleet`, `NRF_northern_revenant_fleet`, `nrf_northern_revenant_fleet_desc`, `NRF_northern_revenant_fleet_desc`, `nrf_icebound_marine_guard`, `NRF_icebound_marine_guard`, `nrf_icebound_marine_guard_desc`, `NRF_icebound_marine_guard_desc`, `nrf_fleet_that_does_not_dock`, `NRF_fleet_that_does_not_dock`, `nrf_fleet_that_does_not_dock_desc`, and `NRF_fleet_that_does_not_dock_desc`. These are intentional-looking idea or focus case variants, but they remain a parser-level collision risk and were not renamed inside a prose-only pass.

Forbidden-style scan: no em dash, semicolon, `not only`, `not just`, `not ... but`, or `Some ... . Others ...` pattern remains in the 005 localisation values outside the immutable sourced Mackinder quotation.

Sourced-quotation audit: no `.q` key appears in the final diff. `chaosx_super_event.19.q` matches the original Mackinder quotation exactly, including its semicolon and attribution. The other eight super-event `.q` keys are also unchanged. The changed super-event descriptions contain narrator wording and attributed actors, not sourced quotations, so no quotation punctuation or wording was altered.

Dynamic text opportunities: the 118 identical `Partial success` mission tooltips are a deliberate shared mechanical status and should stay shared unless the mission system gains per-objective dynamic text. The eight repeated League gate tooltips and eight repeated high-threat or high-chaos gate tooltips are also shared mechanical requirements. Future work could inject the route name into those gates, but that would be a gameplay-facing dynamic localisation change rather than a safe copyedit.

Cross-surface mismatch notes: the event, decision, focus, and mission text retains its original namespaces and keys. The 005 scripted-localisation file and direct event or decision references have complete key coverage. Shared custom-splinter focus titles remain shared mechanic labels, while their descriptions now carry route-specific institutions. The event catalog workbook was not edited because this pass changes general player-facing copy and does not change event detail, evolution detail, or cluster meaning.

## File encoding concerns

The touched file retains its UTF-8 BOM bytes `239,187,191`. Git reports its normal LF-to-CRLF conversion warning for the working copy, but no BOM loss or accidental encoding change was detected.

## Recommended fixes

- Ask the owner of the related idea and focus packages to decide whether the 14 case-fold collisions should be merged or renamed in a dedicated key migration.
- Consider a future dynamic route-name pass for the shared League and threat gate tooltips if the gameplay owner wants each route to expose its actor explicitly.
- Keep the shared 118 partial-success strings as a standard mechanical status unless the event system adds objective-specific values.

## Unresolved wording decisions

Many remaining `rather than` and `instead of` phrases describe concrete legal, military, or diplomatic alternatives such as a republic versus a mutiny or local control versus patron control. They were reviewed and retained where they state the actual choice instead of staging an unofficial-versus-official contrast.

The cost tooltip at `soviet_collapse_reclaim_cost_tooltip` keeps its direct action wording because it exposes live resource tokens and the stability floor. No gameplay meaning, route gate, cost, or dynamic token was changed.

No fallback text, placeholder text, route lore, or mechanic was added.

## Validation

- Parsed 10,343 localisation keys and found zero case-sensitive duplicates.
- Compared all 164 scripted-localisation targets against the 005 English file and found no missing target.
- Compared direct event and decision localisation slots against the full English localisation set and found no missing key.
- Compared token signatures for all 296 changed keys and found no loss or addition of `\\n`, `£`, `§`, or bracketed dynamic tokens.
- Confirmed the BOM and ran the style-pattern scan after the final patch.
- No game launch was performed because live consumer validation belongs to the parent and user.

Plan handoff path: `docs/plans/player_facing_text_style_cleanup/subagent_handoffs/loc_005_soviet_collapse_localisation_style_cleanup_handoff_2026-08-02.md`.
