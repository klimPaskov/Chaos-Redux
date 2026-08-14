# IW-047 Mari El localisation implementation and audit handoff

Date: 2026-08-14

## Disposition

The package-local MEL English localisation is complete for the current canonical decisions, category, ideas, party names, cosmetic identities, effect tooltips, and focus-helper consumers. No missing scoped visible key or exact duplicate key remains.

MEL remains unadmitted. This localisation tranche does not change central attestation, normal or scenario preflight, deterministic Join, gameplay logic, AI, assets, or the event catalog workbook.

## Changed files

- `localisation/english/006_independence_wave_mari_l_english.yml` was created with UTF-8 BOM.
- `docs/events/006_independence_wave/mari_el_package.md` was reconciled with the landed package effects, current focus consumers, localisation coverage, and asset blockers.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw047_mari_localisation_2026_08_14.md` records this implementation and audit.

## Changed keys

### Party names

- `MEL_independence_wave_constitutional_party` and `_long`
- `MEL_independence_wave_socialist_party` and `_long`
- `MEL_independence_wave_forest_land_party` and `_long`
- `MEL_independence_wave_emergency_party` and `_long`

### Cosmetic identities

Complete 15-key name, definite-name, and adjective matrices were added for each live cosmetic tag:

- `MEL_INDEPENDENCE_WAVE_CIVICX`
- `MEL_INDEPENDENCE_WAVE_FORESTX`
- `MEL_INDEPENDENCE_WAVE_SOCIALISTX`
- `MEL_INDEPENDENCE_WAVE_EMERGENCYX`

Each matrix covers the base tag plus democratic, communism, neutrality, and fascism variants. The four tags are current `set_cosmetic_tag` consumers in `common/scripted_effects/006_independence_wave_mari_package_effects.txt`.

### Ideas

Name and `_desc` keys were added for `mel_fragmented_forest_mandate`, `mel_mari_forest_compact`, `mel_forest_congress_charter`, `mel_woodland_councils`, `mel_mari_community_register`, `mel_forest_land_compact`, and `mel_forest_emergency_command`.

### Category, mission, and decisions

- `independence_wave_mari_forest_compact_category` and `_desc`
- `independence_wave_mel_hold_forest_congress` and `_desc`
- `independence_wave_mel_secure_forest_depots` and `_desc`
- `independence_wave_mel_integrate_woodland_guards` and `_desc`
- `independence_wave_mel_register_mari_communities` and `_desc`
- `independence_wave_mel_settle_former_host_ledgers` and `_desc`
- `independence_wave_mel_ratify_constitutional_autonomy` and `_desc`
- `independence_wave_mel_adopt_forest_land_compact` and `_desc`
- `independence_wave_mel_convene_woodland_councils` and `_desc`
- `independence_wave_mel_establish_forest_emergency_command` and `_desc`
- `independence_wave_mel_codify_durable_sovereignty` and `_desc`
- `independence_wave_mel_open_volga_finnic_corridor` and `_desc`

### Effect tooltips

- `independence_wave_mel_depots_effect_tt`
- `independence_wave_mel_guards_effect_tt`
- `independence_wave_mel_communities_effect_tt`
- `independence_wave_mel_host_ledgers_effect_tt`
- `independence_wave_mel_host_loss_effect_tt`
- `independence_wave_mel_constitutional_route_effect_tt`
- `independence_wave_mel_forest_land_route_effect_tt`
- `independence_wave_mel_woodland_route_effect_tt`
- `independence_wave_mel_forest_emergency_route_effect_tt`
- `independence_wave_mel_sovereignty_effect_tt`
- `independence_wave_mel_network_effect_tt`
- `independence_wave_mel_project_failure_effect_tt`

### Helper-facing keys

- `independence_wave_mel_focus_convene_forest_congress`
- `independence_wave_mel_focus_secure_forest_depots`
- `independence_wave_mel_focus_secure_mari_communities`
- `independence_wave_mel_focus_register_mari_communities`
- `independence_wave_mel_focus_integrate_woodland_guards`
- `independence_wave_mel_focus_settle_former_host_ledgers`
- `independence_wave_mel_focus_open_volga_finnic_corridor`

No obsolete decision alias or agrarian cosmetic alias was added. A concurrent source canonicalization changed the traditional cosmetic consumer to `MEL_INDEPENDENCE_WAVE_FORESTX` and its party consumer to `MEL_independence_wave_forest_land_party`. The localisation was aligned to those exact current IDs before handoff.

## Dynamic localisation added

The category dynamically displays Congress Cohesion, Forest Readiness, their maximum, and the stability threshold. The founding mission displays its tuned duration and stability threshold. Package effect tooltips display the exact package-specific ledger gains or loss magnitudes through `independence_wave_mari_pressure` constants.

Shared country, bilateral, network, and league changes remain described by their player-facing ledger names because those shared effects contain several values and no package-specific display helper exists. No hidden variable name or tuning history appears in the text.

## Display before and after

Before this tranche, every MEL package category, mission, project, idea, party override, and effect tooltip lacked package English localisation and could display raw keys. The four route cosmetic tags also lacked their complete ideology matrices.

After this tranche, the current package has concise English names and descriptions, the founding requirements identify Yoshkar-Ola rather than state 833, the two compact ledgers are visible with dynamic thresholds, exact package ledger changes are shown in tooltips, and all four cosmetic identities resolve across every ideology suffix.

## Prose before-and-after summary

### Vagueness

Package ledger changes use exact dynamic values rather than `improves` or `improves sharply`. Requirements name Yoshkar-Ola and the two visible ledgers.

### Bloat

Decision descriptions lead with the concrete action and omit implementation, tuning, and admission history. Route descriptions state who receives authority and what institutions they control.

### Obvious explanation

Descriptions do not repeat button titles. Each adds a concrete institution, requirement, or material purpose.

### Repetition

No stale project aliases were copied from earlier packages. Helper-facing keys are limited to current MEL effect and focus consumers.

### Overcomplication

Raw database identifiers, internal trigger names, and long mechanical inventories are absent from player-facing prose. Former-host text describes the claims being settled in ordinary language.

### Style-rule repair

The file contains no sentence semicolons, em dashes, staccato chains, dialectical hedging, staged contrast formulas, working labels, implementation history, or sourced quotations.

## Required audit lists

- Missing keys: none in the scoped category, mission, canonical decisions, ideas, parties, effects, cosmetics, or focus-helper consumers.
- Exact duplicate keys: none among 126 MEL keys and none found elsewhere under `localisation/english`.
- Scripted-localisation issues: none. The file uses supported direct variable and constant substitutions.
- Dynamic opportunities: package values are dynamic. A future shared scripted-localisation helper could expose exact shared Legitimacy, Recognition, State Capacity, Security, Instability, host, network, and league deltas, but this is not required for current key coverage.
- Cross-surface mismatch: no current decision, idea, party, cosmetic, or focus-helper key mismatch. The historical anchor 256 versus implemented 833 contradiction remains a package admission issue, not a localisation mismatch.
- Encoding concerns: none. The file is strict UTF-8 with BOM.
- Sourced quotations: none inspected or changed.

## Focus MCP evidence

The current shared focus tree contains guarded MEL calls for the Forest Congress, Mari communities, woodland guards, former-host settlement, and Volga-Finnic corridor helpers.

- Inspect revision: `653a3a130d61c0732e89233cc5b3964d7b1fce657e032eaadb754538565d05bb`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1620929ffe9f2fb6f3c7f86f0ef7db2f61e580c7d832c20b02f4120e10ef0f59/6b07099d4bb2dd44f996c0bfebb904c2e996af7e8b7b2519c709e5314e68665a/focus-inspect.653a3a130d61c073.json`.
- Result: 184 focuses, 184 resolved titles, 196 connectors, unchanged layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`.
- Limitation: validation remains false because of 14 shared or installed focus diagnostics outside MEL localisation.

The installed MCP exposes no decision-category inspector or renderer. Decision text wrapping, category overflow, and cost-row layout therefore remain unresolved rather than inferred from source review.

## Asset caveats

The neutral 1936 flag remains unattested, but the four package-defined alternate-history route ladders are now produced and documented under `docs/assets/006_independence_wave/iw047_mari_flags_2026_08_14/`. The route tags are `MEL_INDEPENDENCE_WAVE_CIVICX`, `MEL_INDEPENDENCE_WAVE_FORESTX`, `MEL_INDEPENDENCE_WAVE_SOCIALISTX`, and `MEL_INDEPENDENCE_WAVE_EMERGENCYX`; the asset handoff records 12/12 TGA and 12/12 DDS evidence. No central admission or Join change follows from this asset tranche.

The portrait remains blocked. Vanilla `MEL_zinovy_zhadinov` has no reliable attributed identity record or rights-clear source image. Czeslaw Iosifovich Wróblewski is a different 1936 officeholder, while Zinovy Yakovlevich Zhadnov enters the Mari office after the 1936 start. No substitute portrait or identity was invented.

## Meaningful validation

- Parsed all 126 localisation keys and found no duplicates.
- Cross-referenced every decision `name`, `desc`, and MEL `custom_effect_tooltip` reference against the new file with no missing key.
- Verified all seven idea name/description pairs and all eight party-name consumers.
- Verified each of the four live cosmetic tags has a complete 15-key matrix.
- Verified the file's strict UTF-8 decoding and BOM from raw bytes.
- Verified the current five MEL shared-focus call sites and ran the mandatory focus inspection.

## Skipped validation

- Decision/category rendering and overflow inspection were unavailable in the installed MCP.
- No live HOI4 validation was performed. Runtime consumer validation belongs to the user and parent boundary.
- No workbook check or update was performed because the task explicitly excluded central workbook work.

## Unresolved decisions and blockers

- Parent must reconcile research anchor 256 with implemented and vanilla-history state 833 before admission.
- The parent-corrected IW-047 allocator now matches the `river_or_corridor`/`river_jungle` package contract; older generic archetype wording is historical and superseded. The research anchor 256 versus implemented state 833 remains an admission blocker.
- Route flag production is complete for generated alternate-history identities; neutral-flag attestation and package admission remain blocked.
- Leader identity and portrait rights remain blocked.
- Central attestation, normal and scenario preflight, deterministic Join, and final package admission remain parent-owned and unchanged.

No simplification or fallback was used. Nothing was staged or committed.
