# Event 006 dense localisation clarity handoff

Date: 2026-08-27

## Scope and changed files

- `localisation/english/006_independence_wave_western_l_english.yml`
- `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026-08-27_event006_dense_localisation_clarity.md`

Only `independence_wave_ice_north_atlantic_category_desc` and `independence_wave_afx_codify_basin_government_tt` changed in localisation. Existing unrelated worktree edits, including the Wallonia and Frisia technology-bonus localisation, were preserved.

## Exact key changes

### `independence_wave_ice_north_atlantic_category_desc`

Before:

```text
Reykjavík's emergency government must keep the harbour working, settle with the former host, and decide how far it will bind itself to the wider network.\n\nPort Authority: §Y[?independence_wave_ice_port_authority|0]§!   Civic Cohesion: §Y[?independence_wave_ice_civic_cohesion|0]§!   Coastwatch Readiness: §Y[?independence_wave_ice_coastwatch_readiness|0]§!   Shipping Security: §Y[?independence_wave_ice_shipping_security|0]§!   Compact Support: §Y[?independence_wave_ice_compact_support|0]§!\n\nFormer Host Claims: §R[?independence_wave_host_claim_intensity|0]§!   Hostility: §R[?independence_wave_hostility|0]§!   Obligations: §Y[?independence_wave_host_obligations|0]§!   Property Dispute: §R[?independence_wave_property_dispute|0]§!   Population Dispute: §R[?independence_wave_population_dispute|0]§!   Border Settlement: §G[?independence_wave_border_settlement_progress|0]§!   Host Pressure: §R[?independence_wave_host_domestic_pressure|0]§!   Reconquest Fear: §R[?independence_wave_reconquest_fear|0]§!\n\nNetwork Standing: §Y[?independence_wave_network_standing|0]§!   League Cohesion: §Y[?global.independence_wave_league_cohesion|0]§!   Common Cause: §Y[?global.independence_wave_league_common_cause|0]§!   Patron Capture: §R[?global.independence_wave_league_patron_capture|0]§!   Shared Reserve: §Y[?global.independence_wave_league_shared_reserve|0]§!   Member Confidence: §Y[?global.independence_wave_league_member_confidence|0]§!
```

After:

```text
Reykjavík's emergency government must keep the harbour working, settle with the former host, and decide how closely it will bind itself to the wider network.\n\n§YIsland Government§!\nPort Authority: §Y[?independence_wave_ice_port_authority|0]§!   Civic Cohesion: §Y[?independence_wave_ice_civic_cohesion|0]§!\nCoastwatch Readiness: §Y[?independence_wave_ice_coastwatch_readiness|0]§!   Shipping Security: §Y[?independence_wave_ice_shipping_security|0]§!\nCompact Support: §Y[?independence_wave_ice_compact_support|0]§!\n\n§YFormer Host Settlement§!\nFormer Host Claims: §R[?independence_wave_host_claim_intensity|0]§!   Hostility: §R[?independence_wave_hostility|0]§!\nObligations: §Y[?independence_wave_host_obligations|0]§!   Property Dispute: §R[?independence_wave_property_dispute|0]§!\nPopulation Dispute: §R[?independence_wave_population_dispute|0]§!   Border Settlement: §G[?independence_wave_border_settlement_progress|0]§!\nHost Pressure: §R[?independence_wave_host_domestic_pressure|0]§!   Reconquest Fear: §R[?independence_wave_reconquest_fear|0]§!\n\n§YLeague Network§!\nNetwork Standing: §Y[?independence_wave_network_standing|0]§!   League Cohesion: §Y[?global.independence_wave_league_cohesion|0]§!\nCommon Cause: §Y[?global.independence_wave_league_common_cause|0]§!   Patron Capture: §R[?global.independence_wave_league_patron_capture|0]§!\nShared Reserve: §Y[?global.independence_wave_league_shared_reserve|0]§!   Member Confidence: §Y[?global.independence_wave_league_member_confidence|0]§!
```

### `independence_wave_afx_codify_basin_government_tt`

Before:

```text
The selected government receives a route-specific settlement. Constitutional government gains 10 Industrial Continuity and loses 5 percent War Support. Popular Council government gains 15 Industrial Continuity and loses 5 percent War Support. Emergency Military government gains 20 Industrial Continuity and loses 5 percent Stability. Patron-Client government gains 15 Industrial Continuity and loses 5 percent Stability. Constitutional and Popular Council settlements raise Legitimacy and Security by 5, Capacity by 10, and lower Instability by 5. The Emergency Military settlement raises Legitimacy and Capacity by 5, Security by 10, and lowers Instability by 5. The Patron-Client settlement raises Legitimacy and Capacity by 5, Recognition by 10, and lowers Instability by 5.
```

After:

```text
The selected government receives one settlement:\n§YConstitutional Government§!: §G+10 Industrial Continuity§!, §R-5% War Support§!, §G+5 Legitimacy§!, §G+5 Security§!, §G+10 Capacity§!, and §G-5 Instability§!.\n§YPopular Council Government§!: §G+15 Industrial Continuity§!, §R-5% War Support§!, §G+5 Legitimacy§!, §G+5 Security§!, §G+10 Capacity§!, and §G-5 Instability§!.\n§YEmergency Military Government§!: §G+20 Industrial Continuity§!, §R-5% Stability§!, §G+5 Legitimacy§!, §G+10 Security§!, §G+5 Capacity§!, and §G-5 Instability§!.\n§YPatron-Client Government§!: §G+15 Industrial Continuity§!, §R-5% Stability§!, §G+5 Legitimacy§!, §G+5 Capacity§!, §G+10 Recognition§!, and §G-5 Instability§!.
```

## Preservation and display behavior

The Iceland category description still exposes all 19 original dynamic values with the same variable names, scopes, integer formatters, labels, and value colors. No dynamic localisation was added or removed. The values are grouped under Island Government, Former Host Settlement, and League Network headings, with two related values per line where possible.

The Basin Government tooltip still discloses every route-specific effect. Constitutional Government retains +10 Industrial Continuity, -5% War Support, +5 Legitimacy, +5 Security, +10 Capacity, and -5 Instability. Popular Council Government retains +15 Industrial Continuity and the same remaining effects as the constitutional settlement. Emergency Military Government retains +20 Industrial Continuity, -5% Stability, +5 Legitimacy, +10 Security, +5 Capacity, and -5 Instability. Patron-Client Government retains +15 Industrial Continuity, -5% Stability, +5 Legitimacy, +5 Capacity, +10 Recognition, and -5 Instability.

Before, both strings required the player to extract related facts from long, uninterrupted prose or telemetry runs. After, explicit headings and route lines make the same values and consequences scannable without changing gameplay meaning, keys, costs, scopes, or tokens.

## Prose-quality repairs

- Vagueness: `route-specific settlement` was replaced by a direct statement that the selected government receives one of the listed settlements.
- Bloat: repeated settlement-summary sentences were consolidated into one complete route line per government.
- Obvious explanation: no title or button action is restated beyond the necessary explanation that the selected government determines the settlement.
- Repetition: shared consequence prose is no longer repeated after the four route openings.
- Overcomplication: the Iceland ledger is divided into three concrete subjects, and each government route keeps all of its consequences together.
- Style-rule repair: the revised text contains no em dashes, semicolons, staged contrast formula, staccato dramatic prose, implementation history, or hidden-mechanic explanation.

## Audit results

- Missing keys: none in the two-key scope.
- Duplicate keys: none in the two-key scope.
- Scripted localisation issues: none found. Every Iceland variable token remains unchanged.
- Dynamic text opportunities: none added. The Iceland surface already uses live scoped variables, while the Basin Government settlement values are static effect disclosures.
- Cross-surface mismatches: none introduced or identified within the bounded two-key review.
- File encoding concerns: none found. Both localisation files retained UTF-8 BOM.
- Sourced quotations: neither inspected string contains a sourced or attributed quotation.

## Meaningful validation

- Compared the pre-change and post-change Iceland token sets and confirmed that all 19 dynamic variable tokens, including `global` scopes and `|0` formatters, are identical.
- Checked the Basin Government rewrite route by route against the original effect disclosure and confirmed that all 24 stated gains or losses retain the same affected value and magnitude.
- Confirmed each changed key occurs once in its owning localisation file and both files still decode as UTF-8 with BOM.

## Skipped validation and MCP blocker

No in-engine visual overflow result is available. The mandatory read-only `hoi4.event_inspect` trace was called for `chaosx.nr6.1` with the corrected event selector, but the server returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with workspace `mod_chaos_redux_ea3b2d67c2c0` and no artifacts. The installed MCP package exposes event-chain and dedicated scripted-GUI rendering, but no ordinary decision-category or decision-tooltip localisation renderer that can display these two strings in their actual vanilla consumer. Source review and token preservation checks are not treated as equivalent visual evidence. Parent review should retain overflow as unresolved until the MCP artifact manifest is repaired and an ordinary decision-surface renderer is available.

## Remaining decisions and follow-up

No wording decision remains within the assigned scope. The parent should review the exact diff and retain the MCP visual overflow limitation in the Event 006 completion evidence. No plan addendum was required because the change exposes no missing mechanic or design-depth gap.

## Simplifications, omissions, and blockers

No mechanics, values, routes, costs, tokens, or effect disclosures were simplified or omitted. Visual overflow verification remains blocked as documented above.
