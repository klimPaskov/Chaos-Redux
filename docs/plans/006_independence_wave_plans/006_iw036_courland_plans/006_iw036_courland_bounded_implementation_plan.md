# IW-036 Courland bounded implementation plan

Status: queued; this plan is not an admission or an implementation approval.

The package remains dormant until every gate below is complete and reviewed by the parent owner.

## Gate 1: freeze the map and tag contract

Reconfirm `BJX`, state 190 Kurzeme, its six installed provinces, and `RG-BALTIC-LIVONIA` against the current map revision immediately before source edits. Preserve Latvia's capital state 808 and at least one additional 1936 remnant, and add an explicit Event-005 footprint/conflict check before any owner transfer. Do not reserve state 195 Leningrad or the route-only Vidzeme/Tartu pair for the automatic package.

Re-run the full installed tag collision audit with Random Events excluded by the repository audit policy. Keep the existing BJX shell and history file as the only dormant identity source.

## Gate 2: resolve Courland identity and assets

Select the exact institutional baseline from the research resolution: a provisional assembly, cabinet, municipal council, or congress joined to period regional institutions, schools, labor, veterans, and administrative bodies. Decide whether the duchy/royal restoration is a later route rather than an automatic baseline.

Route all real-person or institutional portrait work to `chaosx_portrait_creator`. Use sourced male officeholders or authentic archival institutional material; never substitute a generated personal portrait for a grounded subject. If a one-person leader is approved, use a regional male name pool and male leader metadata only.

Resolve flag and symbol ownership, date, function, route, and license. The existing BJX TGA ladder cannot be treated as provenance-cleared until the symbol dossier passes. A generated civic flag is permissible only when explicitly labelled as alternate-history synthesis and after the asset blocker is closed.

Add package-specific English localisation for route names, party names, leader/institution names, ideas, decisions, tooltips, and dynamic host/territory text in UTF-8 with BOM.

## Gate 3: implement the country package lifecycle

Add a dedicated IW-036 setup effect, active/final validation trigger, and generation-safe cleanup effect in Event 006 package files. The setup must transfer only the approved compact state, set capital and politics, register the chosen institutional roster, attach ideas, set route and host ledgers, assign the shared focus framework, and publish package/network receipts.

Keep the host settlement explicit. Every route must either preserve Latvia, negotiate a protected remnant, or fail closed before the anchor is transferred. Cleanup must clear BJX flags, ideas, decisions, route variables, temporary characters, cosmetic state, and event targets without touching vanilla Latvian history.

## Gate 4: map the researched force and playability

Map the research row's `coastal_maritime` profile and military identity 49 to coastal guards and territorial infantry. Implement a defensible starting template, equipment and manpower budget, port/supply/rail assumptions, production lines, reinforcement paths, and no-inheritance guards for unsupported host navy or air assets.

Add a narrow AI strategy file for survival, host restraint, port and supply defence, and staged Baltic ambition. Route all AI weights and any package/random scores through `chaosx_ai_probability_auditor` using named scenarios and the same before/after scenario set; do not publish numeric balance claims from source-only inspection.

## Gate 5: connect shared focus, decisions, and formable routes

Use the shared `independence_wave_focus_tree` through an explicit BJX package assignment. Publish only the government routes supported by the research row: constitutional, traditional duchy, military, and patron-client, plus any approved popular-council or host-settlement hooks. Add BJX-specific focus hooks only where a decision or event consumer exists.

Add a Courland decision category and paid projects that build administration, coastal defence, port logistics, rights/autonomy, host settlement, recognition, and Baltic network capacity. Every decision must have visibility, affordability, trigger tooltips, AI values, one-project locking, cancellation/failure consequences, and cleanup.

Extend the Baltic Federation formable registry only through an explicit family adapter: founding carrier, territory/state-puzzle ownership, identity compatibility, flag package, member policy, readiness attestation, commit proof, route cosmetics, and generation-safe cleanup. State 190 alone is never a free formable claim. Keep Livonia's existing route-only semantics separate from BJX's automatic compact.

## Gate 6: admission and evidence

After implementation, add IW-036 only to the central adapter, content-attestation, normal preflight, and scenario preflight lists once the package audit is complete. Update the package source-of-truth map, resume packet, asset manifest, event documentation, and any event-catalog row owned by the parent.

Run task-specific static audits for tag/identity surfaces, package APIs, localisation/asset coverage, host remnant and map binding, and formable state-puzzle alignment. Use mandatory `hoi4.map_inspect` and map render for state 190 and all transfer/network provinces, `hoi4.focus_inspect` and focus render for the shared tree and BJX hooks, narrow `hoi4.event_inspect` and event render for the release/setup/cleanup chain, and `chaosx_ai_probability_auditor` plus `hoi4.probability_compare` for every weighted surface.

The installed package has no Technology Tree Viewer. If no custom technology is added, record the limitation and inherit vanilla BJX technology only after package setup is proven; if custom technology is proposed, stop and request a separate technology audit route.

## Explicit non-goals

Do not overwrite vanilla Latvian or state history, add a second independent country tree, grant `independence_wave_package_content_ready` as a shortcut, promote the existing BJX flag ladder without provenance, invent a named leader, seize protected state 195, or claim Baltic federation formation from state 190 alone.
