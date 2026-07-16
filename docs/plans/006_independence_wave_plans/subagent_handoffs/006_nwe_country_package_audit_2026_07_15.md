# Event 006 Northern and Western Europe country-package audit

> **Portrait-specific supersession (2026-07-16):** Portrait and art-acceptance
> conclusions in this audit are superseded by the male-HOI4 package manifest
> and final independent audit. Unrelated gameplay, route, balance, flag, and
> admission findings remain bounded historical evidence.

> Parent resolution: the route-matrix finding was remediated in
> `006_nwe_route_matrix_remediation_2026_07_15.md`. A later independent audit
> certified only `IW-009` Bavaria, and the parent applied its exact runtime and
> SCN-008 attestation branches. `IW-001`, `IW-002`, `IW-008`, and all other
> unaudited package IDs remain closed pending their formable dependencies and
> independent certifications. The body below remains the original audit
> snapshot and evidence record.

Date: 2026-07-15

Auditor: `event6_nwe_country_package_audit`

Scope: `IW-001` Scotland (`SCO`), `IW-002` Wales (`WLS`), `IW-008` Rhineland (`RHI`), and `IW-009` Bavaria (`BAY`).

Mode: read-only gameplay audit. This handoff is the only file changed by the auditor.

## Executive verdict

None of the four packages may receive static content attestation in the current tree.

The package-owned gameplay, AI, localisation, tag reuse, base-country flags, leader portraits, advisor dossiers, dispatch adapters, and cleanup/repeat guards are substantially present. Release readiness is nevertheless blocked by two critical gates and one major accepted-design mismatch:

1. `FORM-01`, `FORM-02`, and `FORM-04` are profile-only and have no operational identity, flag, territory, or integration implementation.
2. `has_independence_wave_runtime_package_content_attestation_for_execution_id` is `always = no`, so automatic and scenario preflight reject all four packages.
3. The RHI and BAY setup proofs publish routes outside the accepted package matrix.

Finding count:

- Critical: 2
- Major: 1
- Minor: 1

This is not an Event 006 completion claim.

## Package verdicts

| Package | Runtime adapter | Package-owned surface | Direct formable dependency | Current static attestation | Verdict |
| --- | --- | --- | --- | --- | --- |
| `IW-001 SCO` | present | otherwise audit-ready | `FORM-01` and player-selectable `FORM-02` | absent | **blocked** |
| `IW-002 WLS` | present | otherwise audit-ready | `FORM-01` | absent | **blocked** |
| `IW-008 RHI` | present | route matrix is not accepted | `FORM-04` | absent | **blocked** |
| `IW-009 BAY` | present | route matrix is not accepted | none in the accepted registry; South German restoration is an ambition | absent | **blocked** |

The missing `FORM-01/02/04` implementations block SCO, WLS, and RHI directly and block release-readiness reconciliation for this audited tranche. They must not be represented by a fallback tag, borrowed flag, or no-op adapter. BAY must not be assigned an invented formable dependency merely to match the current coarse gate.

## Critical findings

### C-01 — FORM-01, FORM-02, and FORM-04 are not operational

The accepted family registry binds:

- `FORM-01`: Celtic Cooperation State;
- `FORM-02`: North Atlantic Compact;
- `FORM-04`: Rhine Federation.

The shared formable architecture handoff explicitly reports `0/48` operational families. The runtime proof at `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:243` requires a family-bound readiness variable and all six of these flags:

- `independence_wave_formable_territory_adapter_ready`;
- `independence_wave_formable_x_tag_reserved`;
- `independence_wave_formable_flag_package_ready`;
- `independence_wave_formable_identity_adapter_ready`;
- `independence_wave_formable_integration_adapter_ready`;
- `independence_wave_formable_member_policy_audited`.

There is no setter for any of those flags under `common/` or `events/`. The generic dispatcher at `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:1071` also expects exact family effects that do not exist:

- `independence_wave_formable_identity_adapter_1`;
- `independence_wave_formable_integration_adapter_1`;
- `independence_wave_formable_identity_adapter_2`;
- `independence_wave_formable_integration_adapter_2`;
- `independence_wave_formable_identity_adapter_4`;
- `independence_wave_formable_integration_adapter_4`.

No X-ending identity is reserved for these three families, and no complete formable flag package exists. The installed SCO/WLS/RHI/BAY vanilla flags are base-country assets; they do not satisfy a new formable identity's root/medium/small flag requirement.

Exact repair required before attestation:

1. Select and collision-audit the final X-ending identity for each family. No identifier should be invented by this audit.
2. Implement exact territory and capital policy, exclusions, member consent, living-member settlement, and bounded integration-state registration.
3. Produce every required identity/ideology flag variant in all three HOI4 sizes and wire the chosen identity without reusing a base-country or another formable's flag.
4. Implement the six exact identity/integration adapter effects above.
5. Bind `independence_wave_formable_readiness_family` to the loaded family and set the six readiness flags only after their corresponding evidence is complete.
6. Have the identity and integration adapters publish `independence_wave_formable_identity_committed` and `independence_wave_formable_integration_committed` only after their atomic work succeeds.
7. Audit rollback, member-origin cleanup, identity ownership, formable flags, and repeated formation attempts before enabling the package gate.

Until those steps are complete, keeping the formable transaction fail-closed is correct.

### C-02 — 0/4 audited packages have static content attestation

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10` recognizes exact runtime adapter IDs for all four packages. However:

- `has_independence_wave_runtime_package_content_attestation_for_execution_id` is `always = no` at lines 25-27;
- `is_independence_wave_runtime_package_preflight_ready` requires that attestation at lines 32-35;
- `is_independence_wave_scenario_package_preflight_ready` is also `always = no` at lines 67-71.

Consequently, automatic release and SCN-008 scenario release both reject SCO, WLS, RHI, and BAY before setup. The allocator audit passing its 149-publisher, 126 automatic/high-chaos, 138 scenario-ranked, and 3/4/5/7/10 count proofs does not override this package content gate.

Exact repair required:

- keep the global fail-closed behavior while C-01 and M-01 remain unresolved;
- after each package's dependencies and audit are complete, replace the blanket `always = no` with exact package-ID branches;
- require the immutable ID/tag proof already present and do not use dormant-history readiness flags;
- add matching exact scenario preflight coverage only after the same content proof is valid;
- attest packages independently rather than making one package silently inherit another package's readiness.

BAY has no accepted `FORM-01/02/04` family. Its attestation must remain absent now because its route matrix is not accepted, but it should not be forced to wait on an invented formable once M-01 is repaired.

## Major finding

### M-01 — RHI and BAY over-publish government routes

The accepted candidate registry and the reviewed NWE implementation map agree on these route sets:

- RHI: constitutional, popular/labor, emergency military, and patron client; no traditional and no radical sovereignty.
- BAY: constitutional, popular/labor, traditional/restoration, and emergency military; no patron client and no radical sovereignty.

The implementation map records those exact values at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_package_implementation_map.md:332`, `:360`, and in the matrix at `:493-501`.

Current RHI setup additionally enables radical sovereignty:

- setup call: `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:615`;
- prepared proof requires it: `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt:201`;
- player route: `independence_wave_rhi_proclaim_sovereign_corridor` at `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt:209`;
- installer: `independence_wave_install_rhi_sovereignty_government` at `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:496`;
- AI includes the sovereignty government at `common/ai_strategy/006_independence_wave_rhineland_bavaria.txt:54`.

Current BAY setup additionally enables patron client and radical sovereignty:

- setup calls: `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:667-668`;
- prepared proof requires them: `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt:265-266`;
- player routes: `independence_wave_bay_accept_patron_estates_mandate` at decision line 480 and `independence_wave_bay_proclaim_sovereign_directorate` at line 495;
- installers: `independence_wave_install_bay_patron_government` at effect line 565 and `independence_wave_install_bay_sovereignty_government` at line 578;
- AI includes those government flags at `common/ai_strategy/006_independence_wave_rhineland_bavaria.txt:101` and `:121`.

`docs/events/006_independence_wave/northern_western_europe_packages.md` currently repeats the implemented extra routes rather than the accepted matrix, so it is not authority to preserve them.

Exact repair required:

1. Either amend the accepted candidate registry and reviewed implementation matrix with explicit user approval, or remove the unaccepted routes.
2. Under the current accepted design, RHI's radical availability must be withheld and its prepared proof must require the flag to be absent.
3. Under the current accepted design, BAY's patron and radical availability must be withheld and its prepared proof must require both flags to be absent.
4. Remove or make unreachable the associated route decisions, installers, route ideas, AI branches, localisation, cleanup entries, and documentation as one coherent change. Do not leave dead visible content or stale proof clauses.
5. Reaudit the remaining high-chaos actions separately. A bounded high-chaos action is not automatically authority for an unaccepted permanent government route.

This mismatch blocks RHI and BAY static attestation even if the global dispatcher gate is opened.

## Minor finding

### m-01 — the package-gate comment incorrectly implies BAY has a FORM-01/02/04 dependency

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:21-24` says the four audited packages require `FORM-01`, `FORM-02`, or `FORM-04`. BAY setup explicitly clears selected/registered formable family state at `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:677-679`, and the accepted implementation map defines a South German/restoration ambition rather than a shared formable.

The gate is safely closed, so this is not a runtime escape. Correct the comment and make eventual attestation per-package. Do not assign BAY to `FORM-04` or create a South German formable without an accepted spec amendment.

## Coverage evidence

### Gameplay and focus coverage

| Package | Decision/mission blocks | Origin-gated focus additions | Package ideas | Generated institutional characters | Conditional historical character | Advisors | AI strategy plans |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SCO | 11 | 5 | 6 | 2 | 0 | 3 | 7 |
| WLS | 9 | 5 | 6 | 2 | 0 | 3 | 7 |
| RHI | 15, including 1 mission | 0 | 7 | 2 | Matthes | 3 | 6 |
| BAY | 18, including 1 mission | 0 | 8 | 2 | Rupprecht | 3 | 7 |
| **Total** | **53** | **10** | **27** | **8** | **2** | **12** | **27** |

RHI and BAY intentionally use the dedicated full Event 006 focus framework plus package-specific decisions, ideas, AI, characters, ambitions, and lifecycle mechanics. Setup calls `independence_wave_assign_focus_framework` and the prepared proofs require `independence_wave_full_focus_framework`. This is not a fall-through to vanilla `generic_focus`. The accepted implementation map authorizes `full` assignment for both tags. Adding origin-gated RHI/BAY focus branches would be a depth improvement, not a substitute for fixing C-01, C-02, or M-01.

All 53 package decision/mission blocks have `ai_will_do`. The 43 timed decisions and both missions have cancellation or timeout handling; the remaining eight are one-shot/instant choices. Active-project triggers and cleanup cover the package operations.

### Characters, portraits, advisors, and GFX

Installed DDS coverage:

- 10 large leader/council/historical portraits at `156x210`;
- 4 separate commander thumbnails at `50x67`;
- 12 distinct advisor dossier cards at exactly `65x67`;
- all 26 are legacy, uncompressed, one-level 32-bit BGRA DDS with the standard masks;
- 26 relevant sprite registrations resolve to existing textures; no duplicate sprite name was found.

Manual contact-sheet review found the eight generated institutional leaders/commanders, Matthes, and Rupprecht consistent with restrained HOI4 painted portrait treatment. The advisor review sheets show twelve separate institutional dossier compositions rather than resized leader portraits or repeated art.

The authoritative production evidence is under:

- `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/` for the later user-directed HOI4 portrait pass;
- `docs/assets/006_independence_wave/nwe_advisor_dossiers_2026_07_15/` for advisor dossier cards.

Static advisors are recruited only by hidden, triggered event `chaosx.nr6.10` at `events/006_independence_wave.txt:55`. Each of the 12 calls is guarded by `NOT = { has_character = ... }`. All four setup effects fire that event without a delay and then require the exact three-advisor roster before publishing setup success. The offline Event Modding reference states that a no-delay `country_event` effect fires instantly, and the official effects documentation lists hours/days/months as optional waits. This satisfies the event-only static-character recruitment rule and is repeat-safe.

### Base-country flags and tag identity

- `SCO`, `WLS`, `RHI`, and `BAY` are registered vanilla tags at `common/country_tags/00_countries.txt` in the installed game.
- Chaos Redux does not redefine those tags.
- The installed collision audit parsed 7,981 vanilla/external tag definitions, found all 91 accepted reused tags, and found zero reserved custom-tag collisions.
- Each audited tag has four ideology flags in each of root, medium, and small directories: 12 files per tag, 48/48 present.
- The accepted asset-source handoff explicitly permits installed flag reuse. It preserves the WLS 1959-layout caveat, the RHI separatist distinction, BAY republican/royal distinctions, and a Scottish royal banner as route-owned rather than neutral fallback art.

These 48 base-country files do not satisfy the missing `FORM-01/02/04` identity flag packages.

### Localisation

The three exact package/advisor localisation files are UTF-8 with BOM:

- NWE advisors: 48 keys;
- RHI/BAY package: 156 keys;
- SCO/WLS package: 143 keys.

The reference-to-localisation audit found:

- 0 missing among 213 decision/category/focus/tooltip/party/generated-character keys;
- 0 missing among 54 package-idea name/description keys;
- 0 missing among the 48 advisor name/description and trait name/description keys;
- no duplicate NWE package keys across English localisation.

The RHI/BAY package document and localisation must be reconciled if M-01 is fixed; presently they faithfully describe the unaccepted implemented routes.

### AI, cleanup, and repeat safety

- 27 origin-locked AI strategy plans use exact `original_tag`, package/setup activation, and `abort_when_not_enabled = yes`.
- Generated institutional characters are guarded by `NOT = { has_character = ... }`.
- Setup reuses exact package IDs, original tags, anchors, force mappings, and lifecycle proofs.
- Package-prefix flags set during gameplay all have cleanup coverage: SCO 19/19, WLS 17/17, RHI 22/22, BAY 24/24. Cleanup also clears additional inherited/shared route markers, which accounts for the larger clear lists.
- All 53 package decisions/missions are removed or invalidated by package cleanup.
- RHI's Event 006 setup closes the vanilla German reunification decision and cleanup restores it.
- BAY makes the South German ambition versus German reunification choice explicit; cleanup restores the vanilla decision only when the package path had closed it.
- Package setup contains no daily, weekly, monthly, or all-country iteration.

No cleanup or repeat-safety blocker was found in the audited package-owned surface.

## Required release order

1. Reconcile M-01 against the accepted route matrix.
2. Implement and asset-audit `FORM-01`, `FORM-02`, and `FORM-04` with exact X identities, three-size flag families, territory/member policy, and the numeric identity/integration adapters.
3. Reaudit the three formable transactions, including failure rollback and living-member outcomes.
4. Reaudit each package independently, including BAY without an invented formable dependency.
5. Replace the blanket runtime and scenario content gates with exact, independently justified package-ID attestations.

## Audit limitations

The requested `hoi4.event_*`/`hoi4.focus_*` MCP tool family was not exposed in this session, so no MCP render or compare result is claimed. The audit used direct Chaos Redux source, the required offline wiki snapshot, official installed-game documentation, installed vanilla precedents, manifests, contact sheets, and read-only structural checks.

No live-game result is claimed. This report answers only whether the current files may be statically attested.

## Simplifications, omissions, and blockers

The audit introduced no gameplay simplification, fallback, placeholder, or omitted package surface. It did not edit gameplay. The blockers are C-01, C-02, and M-01 above. Overall Event 006 completion is not claimed.

Skills used: `chaos-redux-events`, `chaos-redux-event-assets`, `hoi4-focus-trees`, `hoi4-decisions-missions`, and `chaos-redux-subagents`.
