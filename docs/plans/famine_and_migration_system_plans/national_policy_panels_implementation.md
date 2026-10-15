# National policy panels implementation record

Status: the accepted implementation and source/visual review are complete. All seven maintained source-contract suites also pass from the isolated commit candidate, excluding unrelated working-tree changes. No live-game run is claimed.

The current presentation and automatic-update contract follow the shared Camps/Migration/Famine refinement below.
Earlier GUI v4 and manual-refresh previews remain historical baseline evidence.

Acceptance basis: the user explicitly instructed “PLEASE IMPLEMENT THIS PLAN” on 2026-10-15. The accepted scope is recorded in [Part 9](../../specs/famine_and_migration_system_specs/national_policy_panels_part9.md). The [country matrix](../../specs/famine_and_migration_system_specs/national_policy_country_matrix.md) supplies the exact 1936/1939 tag inventory and profile evidence.

## Source-of-truth map

| Surface | Authority | Current evidence |
| --- | --- | --- |
| Accepted policy/panel design | Part 9 in the source spec package | User acceptance is explicit and dated 2026-10-15. The Part 9 list records all accepted choices and preserves famine/migration ownership. |
| Famine and migration core mechanics | [famine_system.md](../../systems/famine_system.md) and [migration_system.md](../../systems/migration_system.md) | Existing mechanics remain independent; their status and balance evidence continue to use the 2026-10-10 improvement record. |
| Native law IDs, costs, publication, starting profiles, lifecycle, retaliation | [National policies](../../systems/national_policies.md), `common/ideas/national_policy_laws.txt`, `common/scripted_effects/national_policy_effects.txt`, and `common/scripted_effects/national_policy_warfare_effects.txt` | Laws are the authority; callbacks publish derived values and family-specific permission. Source/model handoffs do not prove engine timing. |
| Bookmark country matrix | [national_policy_country_matrix.md](../../specs/famine_and_migration_system_specs/national_policy_country_matrix.md) | 91-tag union across 1936 and 1939; its source parser and profile table are preserved. The country worker records 90 and 85 owners per bookmark and tags all specific profile bases. |
| Famine and migration panels | `common/scripted_guis/{famine,migration}_management_scripted_gui.txt`, `interface/{famine,migration}_management.gui`, and `.tmp/national_policy_panels/gui/` evidence | Parent accepted native PNG review of seven state scenarios per window at source revisions `9d3dcd0fc700c8fab6187950a4cba32e4a4255a3201a84e3e4b40501bf0f01c1` (famine) and `7003daf0fdd6d97edd5490741845d0a2e973f09c32a14a03bb0500bc08a40b91` (migration). See the visual evidence table below; declared fixture values are not campaign proof. |
| Costs and action wrappers | `common/scripted_effects/national_policy_cost_effects.md`, each mechanic's GUI/action helpers, and current worker handoffs in `.tmp/national_policy_panels/` | Native law UI owns law PP spending. Existing operational owners retain action costs and receipts; the panel does not initialize mechanic gameplay. |
| CXT package | [CXT testing contract](../../testing/chaosx_test_country.md#national-policy-laws), `national_policy_cxt_extension` carrier and `national_policy_cxt_extension_apply` helper | Registration is separate from player-triggered package application; the daily CXT fallback does not grant laws. |
| Chaos Warfare doctrine | [Chaos Warfare doctrine](../../systems/cbrn_warfare/chaos_warfare_doctrine.md#use-policy) | Doctrine adoption does not set policy. An active doctrine state supplies the accepted live 25% discount on the three warfare laws; the former separate policy-purchase decisions are removed. |
| Asset provenance | Durable crosswalk below; detailed source package at [ignored local icon archive](../../../.tmp/national_policy_panels/asset_archive/icons/manifest.md) | Five generated 60×68 law-family DDS assets and the native category strip are source-hash mapped below. Reused report scenes and the native eleven-frame progress meter are identified separately. The generated reference board is not a runtime asset. |

## Plan and handoff dispositions

| Work item | Disposition | Basis and evidence | Remaining limit |
| --- | --- | --- | --- |
| Accepted policy and panel design | Accepted; implementation and source/visual review complete | Explicit user decision above; captured in Part 9 and reflected in the reviewed source surfaces. | The isolated candidate passed all seven maintained source-contract suites. |
| Native five-slot law package | Implemented within assigned scope | `.tmp/national_policy_panels/laws_handoff.md` records 19 native law options, five slots in two categories, costs, profiles, publishers, lifecycle and CXT registration. The corrected maintained `.tools/test_national_policy_laws.py` source suite covers all 19 options, 132 transitions, 18 profiles, Holy Realm/Event 003 requests and 21 request pairs. | Native callbacks and law replacement order remain source-modeled, not engine-observed. |
| CBRN permission and retaliation | Implemented within assigned scope | `.tmp/national_policy_panels/warfare_handoff.md` records exact-offender, cross-family C/B/N evidence, 365-day receipts, nuclear `None`, the retained action taxonomy and ten passing source-contract tests. | Script validation returned partial coverage (`valid=null`); no engine behavior is claimed. |
| Native policy costs and discount | Implemented within assigned scope | `.tmp/national_policy_panels/costs_handoff.md` records native PP ownership, three mutually exclusive cost variants, live doctrine discount and the corrected final run: 160 lifecycle cases, 19 paid law-option changes and five free-change rejection cases passed without macro substitution. The current `.tools/test_humanitarian_cost_display.py` result passes all four test groups against the current source hashes in `.tmp/national_policy_panels/cost_display_test_results.json`. | Native localization execution, cost rounding, affordability display and actual PP debit remain engine behavior. |
| Country start profiles and lifecycle | Implemented/audited within assigned scope | `.tmp/national_policy_panels/country_handoff.md` plus the 91-tag matrix document the exact profiles, MAN/MEN defaults, release reset, civil-war retention, bounded startup and CXT path. | The auditor's earlier Holy Realm adapter finding was addressed in subsequent source and permission review; `.tmp/national_policy_panels/probability_handoff.md` records 21 modeled valid pairs and atomic rejection. Runtime callback execution is unresolved. |
| Operational panel/action integration | Implemented in source and visually reviewed | `.tmp/national_policy_panels/actions_handoff.md` records 10 famine and 17 migration operations, unchanged AI missions/weights, 19 passing production-source action tests, all 11 existing famine regressions passing, and all 71 production callbacks retaining baseline equivalence. `common/script_enums.txt` contains one `script_enum_humanitarian_action_part` with 32 tokenizable members: two families, 27 operation suffixes, and three retired private receipt-compatibility IDs. The separate numeric script-constant groups carry the 10 and 17 operation IDs plus zero markers. The maintained panel test passes 10 contract groups, including quiet open/refresh/close, sparse state selection, due progress and 1,201-row collection. | Native clicks, automatic tooltip evaluation and live campaign action state remain unobserved. |
| Localisation | Implemented within assigned scope | `.tmp/national_policy_panels/localisation_handoff.md` and `localisation_check.json` record the scoped key audit with no duplicate keys, missing GUI/law keys, unknown getters or missing substitutions, and 27 action-tooltip overrides retaining native requirement tokens. | Native automatic tooltip text remains unobserved; parent reviewed the rendered hover and label layouts using the declared scenarios. |
| CXT package registration | Implemented in source/docs | The package carrier and setup effect are named above; source uses the existing CXT registration token extension. | No new grant or initialization hook is claimed from a registration fallback. |
| Icon production and wiring | Accepted and integrated in parent scope | The five generated family icons and native strip are crosswalked below; existing GFX references resolve to their DDS paths. Parent accepted the five family icons and reviewed the two added native-strip family frames. | The reference board is excluded from runtime use. |
| Event catalog | No update required | The panels and law system create no player-visible random event, event-log entry or catalog content. | Hidden bridge plumbing is not a catalog event. |
| Skill updates | Implemented by owning skill workers | The user-authorized native ImageGen cache flexibility is recorded in canonical `chaos-redux-event-assets`; this run also linked `chaos-redux-decisions-missions` and `chaos-redux-ideas-modifiers` to the existing helper contracts. Supporting event, scripted-GUI, and subagent references were read without claiming ownership of other sessions' changes. | These three canonical skill changes are included in isolated commit verification. |

No plan or handoff is promoted into the source spec based on file location or old status. Part 9 is the accepted design record because of the explicit user instruction; worker handoffs remain implementation evidence.

## Documentation changes in this consolidation

- Added [National policies](../../systems/national_policies.md) as the current system overview and authority map.
- Added accepted [Part 9](../../specs/famine_and_migration_system_specs/national_policy_panels_part9.md) and linked it from the specs README without altering the original famine/migration parts.
- Added short cross-links in both system docs, the Chaos Warfare doctrine policy section, and the CXT registration contract.
- Reconciled famine/migration player-surface descriptions to quiet-accessible panels with crisis-specific operational gates; listed the ten famine and seventeen migration actions and removed the three former pure migration policy purchases from the action description.
- Replaced the doctrine's obsolete three-policy/5-Command-Power table and stale AI/icon references with the five native law groups, their current base costs, the live discount and the exact-state cleanup decision that remains active.
- Preserved the existing country matrix and asset manifest as owned source records.
- Added the parent-accepted GUI v4 review, current source revisions, test dispositions and durable art/runtime crosswalk below before cleanup of the task asset workspace.
- Captured pre-edit copies of the six modified pre-existing docs in `.tmp/national_policy_panels/baseline_docs/` for the parent-directed source snapshot. No images or PNGs were copied into the repository by this report.

## Contradictions and superseded material

The specs README previously named the 2026-10-10 improvement plan as the single current plan/status record for both mechanics. That remains correct for famine and migration core status, but it omitted the later accepted national-policy integration. The README distinguishes this completed panel implementation report and accepted Part 9 without superseding or rewriting famine/migration design.

The doctrine document previously described three five-Command-Power policy purchase commands and their AI/icon consumers. Current source removes those purchases and makes native laws authoritative; the doctrine documentation now maps all five law groups, their 100/150 Political Power base costs and the live 25% warfare discount. Its retained exact-state cleanup command is the remaining active decision in that file. The famine/migration category-gating description is superseded by quiet-accessible management panels; crisis and local state facts gate actions, not entry to the panels.

Older source parts' crisis eligibility and native AI mission descriptions remain in force. The accepted panel-first operational surface does not remove AI missions. No event-catalog spreadsheet update is warranted because no visible event was added.

## GUI visual acceptance and verification limits

The parent accepted the actual native PNG review for GUI v4. Each panel has seven state scenarios: group 1 hover, group 2 with every action locked and grey labels, group 3 with long labels, 1366-wide layout, 1920 at 1.25 scale, a full seven-row scrolled list, and the empty-state prompt. The reviewed source revisions are `9d3dcd0fc700c8fab6187950a4cba32e4a4255a3201a84e3e4b40501bf0f01c1` for famine and `7003daf0fdd6d97edd5490741845d0a2e973f09c32a14a03bb0500bc08a40b91` for migration. The v3 calm/active overview states and 1.25-scale views remain accepted and unchanged. The entry render review also covers both category openers and the native politics view with two law-family rows.

The v4 review fixed the scrollbar hitbox, long-name fit, partially visible bottom rows, disabled-label appearance, and empty-state guidance. The render manifest records seven scenarios per window and zero missing assets, but also carries `unresolved = 15` and `unsupported = 1` representation items for each system; its generic state gallery is missing and it flags hidden zero-sized clipping regions. These MCP/representation flags prevent a universal validation-pass claim. The visual review covers the requested rendered states, not every engine state or native interaction.

The render fixtures supply explicit display values, selected states and action enablement to exercise layout. They are not campaign-derived gameplay proof. Native button clicks, automatic tooltip text, native law-price rounding and affordability remain unobserved. The implementation, source/visual review and isolated-candidate verification are complete. No live game was run or claimed.

## Durable asset and runtime crosswalk

The five generated law-family icons were accepted by the parent on 2026-10-15. Each uses native ImageGen with transparent background, a single canonical vanilla idea icon as a style-only reference, and a copied source PNG whose hash matches the reported user-authorized native cache output. The source hashes below identify those generated PNGs; runtime hashes identify the final 60×68 DDS files. Processed PNG and decoded DDS comparisons were pixel-identical, with real alpha and safe canvas margins.

| Family | Source PNG | Runtime sprite and slot alias | Runtime DDS | Source PNG SHA-256 | Runtime DDS SHA-256 |
| --- | --- | --- | --- | --- |
| Reception | `.tmp/national_policy_panels/asset_archive/icons/source_png/source_reception_v001.png` | `GFX_idea_national_policy_reception` / `GFX_idea_slot_refugee_reception` | `gfx/interface/ideas/national_policies/idea_national_policy_reception.dds` | `0f84b14971fdb6571babe0bff9e34d70b893c3a805859e32a4fbfb7c6db3c358` | `0d00cfbcbfc08c76037f97518d1c63a2291340091bdd2760f3a6f0f42e449104` |
| Departure | `.tmp/national_policy_panels/asset_archive/icons/source_png/source_departure_v001.png` | `GFX_idea_national_policy_departure` / `GFX_idea_slot_civilian_departure` | `gfx/interface/ideas/national_policies/idea_national_policy_departure.dds` | `aa7443087d8c8b9e7ca8a291a0c0300c3ae17b73963fcec150d941a89dfe23c9` | `f1884108fa86a21dc5128a86eecfbb7ec9c34f00fe0c8128f6af68c30b6b7be0` |
| Chemical | `.tmp/national_policy_panels/asset_archive/icons/source_png/source_chemical_v001.png` | `GFX_idea_national_policy_chemical` / `GFX_idea_slot_chemical_use_policy` | `gfx/interface/ideas/national_policies/idea_national_policy_chemical.dds` | `6763c7f14f5405e4071f06e6b7b6e4e16f3ff28cb88a092aa48d0add241685b7` | `04751a321a4912c4e7ff2a47df88eb23bbfdda68bfd59955d28ae2aa394803e4` |
| Biological | `.tmp/national_policy_panels/asset_archive/icons/source_png/source_biological_v001.png` | `GFX_idea_national_policy_biological` / `GFX_idea_slot_biological_use_policy` | `gfx/interface/ideas/national_policies/idea_national_policy_biological.dds` | `c7ce6d661fa81b42f8e5a95c01805a9435a66db522bf796e9ce7e8bcb05ed340` | `1543b16b48f4d1bdcc384d2986f0e8aed59efe4c71e33af038587a42d1f04874` |
| Nuclear | `.tmp/national_policy_panels/asset_archive/icons/source_png/source_nuclear_v001.png` | `GFX_idea_national_policy_nuclear` / `GFX_idea_slot_nuclear_use_policy` | `gfx/interface/ideas/national_policies/idea_national_policy_nuclear.dds` | `8e441da4512fcbb3d82d5d441a506203e143e5a6714ed2924d8584da57332bdc` | `dee5843c0e8786989c265882ac92cc3fd97d1bde6ac5051c2a633aa3c8a76b80` |

The politics category strip is a sixth, native-assembled runtime asset: source `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/idea_categories.dds`, SHA-256 `889c019e75389e8fe4cd4e1206055b5e80b20cd70988932c83a2365cd24113a5`; runtime `gfx/interface/ideas/national_policies/national_policy_idea_categories.dds`, SHA-256 `9a5d0aff530bdf4197a9a13179c1a2c0f409028e580c25c0dfa40eef7bd2680d`. The 384×33 strip preserves the pixel content of original frames 1–6 and adds reception and nuclear family frames 7–8. `GFX_national_policy_idea_categories` registers the eight-frame output.

The panels reuse three famine report scenes (`GFX_report_event_famine_generic`, `GFX_report_event_famine_island_blockade`, and `GFX_report_event_famine_relief_arrival`) and four migration report scenes (`GFX_report_event_migration_wartime_evacuation`, `GFX_report_event_migration_closed_border`, `GFX_report_event_migration_nuclear_evacuation`, and `GFX_report_event_migration_return`). Both active-work meters reuse the native `GFX_camp_admin_meter`; no progress-meter artwork was generated. The generated reference board is a planning/review artifact and has no runtime consumer.

After acceptance and promotion of the durable crosswalk, the temporary `docs/assets/national_policy_panels/` workspace was retired. Its unchanged sources, prompts, manifests and previews remain in the ignored local archive `.tmp/national_policy_panels/asset_archive/`; that archive is review history, not a runtime or Git dependency. Runtime consumers resolve only installed/native assets or final `gfx/` files.

## Simplifications and omissions

No accepted mechanics, operation routes, country profiles, law choices, actions, AI missions, assets, or panel states were simplified or omitted. The 27 human operational actions remain connected to their production owners; three private tokenizable receipt-compatibility IDs remain in the shared 32-member enum and do not restore policy-purchase decisions. Source fixtures and declared GUI values are reported within their limits above, without being presented as engine or campaign observations.

The task-owned path inventory is `.tmp/national_policy_panels/owned_paths.json` (132 paths, including `common/script_enums.txt`); it is an ignored commit-scoping receipt, not a runtime dependency. Read-only reference material is excluded from that ownership list.

## Skill updates

Three canonical domain skills were updated in this workstream: `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-ideas-modifiers`. The event-assets change records the user-authorized flexibility for native ImageGen cache storage and requires source-hash lineage. The ideas/modifiers and decisions/missions skills link to the existing helper argument and temporary-output contracts. This task read the existing event, scripted-GUI and subagent reference material without claiming ownership of other sessions' changes. No new skill was created.

## Resumption

Resume from this report and the current source in place. Keep the accepted Part 9, country matrix, visual dispositions, and durable asset crosswalk. Implementation, source/visual review and isolated-candidate verification are complete. Do not recreate specs, rerun completed audits without changed inputs, or turn representation flags into universal pass claims.

## Isolated commit verification

The reviewed candidate was exported into an ignored task directory and tested independently of unrelated working-tree modifications. All seven maintained suites passed: national law publication/lifecycle, policy pricing and sale composition, warfare permissions/retaliation, panel presentation, the 19 action-contract cases, the 11 existing famine regressions, and transport-cost display context. The candidate receipt is `.tmp/national_policy_panels/candidate_test_results.json`. Final documentation-only reconciliation does not change those tested runtime sources.

## Presentation refinement: 15 October 2026

Acceptance basis: after viewing the previews, the user described the UI and text as debug-like and requested more color.
The parent accepted two generated composition references within that authorization, preserving all functional controls during native mapping.
The windows are titled **Civilian Displacement** and **Famine Relief**.
Muted teal and amber identify headers and selections; smooth olive panels, gold headings, larger summary values, existing decision icons and dark disabled buttons provide hierarchy.
Red, amber, green and gray status cues retain explicit words, so color is not the sole indicator.
Short descriptions replace terms such as unassessed, recorded need and native mission requirements.
Mission-placement instructions were removed from the main canvas; native missions and their category entry points are unchanged.

Changed sources: `interface/{migration,famine}_management.gui`, new `interface/humanitarian_panels.gfx`, `localisation/english/humanitarian_panels_l_english.yml`, `humanitarian_panel_values_l_english.yml`, the two DDS files below, this report and Part 9.
The text review found the undefined `migration_cost_evacuate_administration` alias and linked it to the identical civilian-evacuation quote: five trains plus standard transport under existing route and affordability rules.
No payment, law, AI, simulation, permission, receipt, mission or timing code was changed.

### Asset crosswalk

| Consumer | Runtime DDS and sprite | Generated source SHA-256 | Runtime SHA-256 |
| --- | --- | --- | --- |
| Migration header, selected tabs/row, opener and response navigation | `gfx/interface/humanitarian_panels/migration_accent_tile.dds`; `GFX_migration_panel_accent` | `5d786321fcf64e71525e85da7ed307fd8840191ad39bf0b625ad4b88328a9bfb` | `35f0898d36857bb8eecdf709ca19524cab6e0ef57d09660db9894317a7a94190` |
| Famine header, selected tabs/row, opener and response navigation | `gfx/interface/humanitarian_panels/famine_accent_tile.dds`; `GFX_famine_panel_accent` | `75e0ecd175c56e02d28579882ed536b0ab0fc6b84276dd7a3d7f92466e98df8d` | `b25d960a835d3a45dd2ae4616fd04ea95de651179ff661c4dd0e5c54ab295cff` |

Both original native-ImageGen skins are 96×96 one-frame BGRA DDS with eight-pixel corner slices and transparent outer corners, registered in `interface/humanitarian_panels.gfx`.
The producer preserved original sources, cleaned negligible-alpha exterior noise in processed copies, resized with premultiplied alpha and documented the interior palette adjustment.
Native-size review and exact decoded-DDS pixel comparison passed; the parent accepted both in rendered windows.
Shared textures and sprite definitions are preserved.
Existing category, decision, report and law-family art remains in use; composite references have no runtime consumers.
Both famine tabs, Update reports and Show on map remain native despite their omission from a reference, and the selected-view highlight follows the actual view.
Sources, requests, manifests and reference images are retained in ignored `.tmp/national_policy_panels/polish/asset_archive/` after retirement of the temporary `docs/assets/humanitarian_panel_polish/` workspace.

### Review evidence and limits

Nine declared scenarios per window cover active states, active overview, quiet overview, disabled actions, long names, 1366×768, 1920×1080 at 1.25 scale, scrolled lists and empty states.
Intermediate renders exposed a repeating panel texture and a displaced famine context-tab highlight; the affected surfaces were corrected and rendered again.
The final famine alignment review uses revision `d04b7604f6fa8f3f4266c7b941abcb20631b29b637df48eef48dcb6665dd1009` at both 1366×768 and 1.25 scale.
Migration's accepted state/active-overview matrix is `7465b7408751baae68fbe71c7f311aac9476afbdf8c3d31537711c9493657bba`; its quiet-copy follow-up is `ecba45b16e961164c6cc219cf3bc0275604f0eb86f5f66d156b9bf04ac4634bb`.
Famine's overview matrix is `9ac273ee61890099f0da0aad19c50932c2ab4d0e51b6fff4bc2c9794c4f73db4`; its state repair matrix is `e33f47b91e6372aba5572c59db43b2c4cbc18ddaf38818f20e4a46dc8dbaad02`, followed by the exact alignment correction above.
The final empty-state wording was reviewed separately at migration revision `5fcb01bd32f9fae5a760c7a8c9d3e57250e58768540509a6c9a60580370201e5` and famine revision `980aa972782d188c5e3a096bb87dab95d3239648aaeaa4c9a6920f891f29955d`; it reports the quiet state without asking the player to select an absent row.
Artifacts, verified matrix hashes, native PNGs and fixtures are in `.tmp/national_policy_panels/polish/preview_manifest.json` and the adjacent files.
These are explicit layout fixtures, including control and long-text stress cases, not campaign observations.
Cost examples resolve production aliases for an assumed affordable mainland route without discounts; the former generic preview prices were discarded.

The localisation specialist reviewed the two English files and their dynamic substitutions.
An additional decision-audit task remained uninitialized and was stopped; the parent performed its bounded checklist rather than claiming a specialist result.
Parent review verified the same 43 migration and 31 famine button definitions, original operation/state-row hitboxes and tooltip targets, aligned click-through highlights, byte-identical scripted-GUI bindings and recursive resolution of all 25 cost strings.
The maintained panel suite passed ten contract groups, the action suite passed nineteen cases, and the cost-display suite passed four cases.
Evidence is recorded in `final_source_review.json`, `localisation_handoff.md` and the existing test receipts under `.tmp/national_policy_panels/`.
Unresolved engine-state representation and hidden-element warnings remain renderer limitations; native clicks and in-game behavior are not claimed as observed.
No controls, mechanics, assets or requested presentation states were omitted, and no functional simplifications were made.

Reference basis: installed `common/scripted_guis/_documentation.md` lines 50–114, revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`; offline Interface modding lines 196–226, revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`; Data structures localisation lines 488–517, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`; and installed `interface/core.gfx` native tile, header and font definitions.
Skills used: scripted GUI, event assets and UI-family references, subagents, player-facing event text guidance through the localisation worker, and shared Git commit isolation.
No skill changes were required for this refinement.

## Shared Camps styling and automatic updates: 15 October 2026

Acceptance basis: the user required Camps to match the other management windows and explicitly rejected Update reports buttons in favor of automatic dynamic UI.
Both manual report buttons, their localisation and click bindings, the humanitarian dirty gates and their obsolete producer counters are removed.
Native visibility, affordability, enabled states and dynamic text reevaluate at the GUI tick.
Copied totals, lists, selected-state details and progress frames update through existing owner publications and a single country-owned observer every elapsed game hour while at least one eligible human panel is open.
The observer is presentation-only, enrolls no crisis and adds no recurring world scan.
Ordinary close/reopen shares the pending delivery; closed or ineligible panels do not rebuild, and the chain retires when no eligible window remains open.
Annexation, terminal Camp exclusion and release initialization clear old UI reservations; an earliest-hour guard rejects stale deliveries after a fresh reservation, including either ordering of old and fresh events at the same due hour.
The existing Camp dispatch lifecycle supplied this recovery precedent.

The authoritative helper contract is [national_policy_panel_effects.md](../../../common/scripted_effects/national_policy_panel_effects.md).
Implementation includes the matching effects/triggers, hidden `national_policy_panel.1` event, humanitarian openers, the actual Camp opener, six actor-rooted action receiver tails, the existing state-control and annex callbacks, country initialization/release boundaries and terminal Camp cleanup.
Camp cached projections also isolate their loop-break temporaries and initialize caller-owned quote outputs.
No action cost, population accounting, mission, political law choice, AI weight, monthly Camp process or famine assessment rule was changed.
Underlying reports remain as current as the subsystem that publishes them; while paused, direct getters and synchronous owner publications update, while an arbitrary external edit without a publication callback waits for a game-hour boundary or opening to rebuild copied projections.
No live engine timing or event delivery was observed.

Camps keeps Administration, Locations and Records in its existing 900×540 footprint, using the same native charcoal frame, olive panels, brass selections, gold headings and distinct enabled/locked buttons as the humanitarian family.
The existing Camp icons, menus, command IDs, tooltips and outcome records remain intact.
The history viewport shows five complete rows with scrolling instead of a clipped sixth row, and the selected state title accommodates long names.
`GFX_humanitarian_panel_brass` in `interface/humanitarian_panels.gfx` aliases the existing `gfx/interface/humanitarian_panels/famine_accent_tile.dds` (SHA-256 `b25d960a835d3a45dd2ae4616fd04ea95de651179ff661c4dd0e5c54ab295cff`); there is no additional runtime texture or repointed shared sprite.
The parent accepted the Camp composition reference (SHA-256 `cd558927df0b93bbecaf7ba0d940e8ca1af7737853ee41dd4dddfE0116bff9c4`, generated source `027c82f19480302b85c0fa2342a9d4ee5015318edc6d8156b3e67d8ed9c77b09`) within the user's requested visual direction.
That reference is not runtime art; its source, prompt-capture limitations and native mapping are archived in `.tmp/national_policy_panels/consistency/reference_archive/` after retiring `docs/assets/camp_panel_consistency/`.

The parent reviewed eleven Camp scenarios covering all three views, shortages, disabled actions, a role picker, the longest mandate, long state names and incomplete-record status, empty locations, scrolled history, 1366×768 and 1920×1080 at 1.25 scale.
Final Camp matrix revision: `5ece616502dbeaba188bec763d55b57236145ed18dc3ef381a485cef6fe2c1f4`.
The two button-free humanitarian overview previews use revisions `7e4101051f7848ee16ff890eababdd5acd171bbfc01f7001363c1404ebf3a154` and `1af1bec0d5c3656d0f0089b9e90b4e3d0d6f2140c167da40f1e2ab6ad84ba025`.
Fixtures, authoritative artifacts, PNG hashes and native-size reviews are under `.tmp/national_policy_panels/consistency/`; values and enabled states are explicit layout assumptions, not campaign observations.
MCP script/event checks remain partial, and GUI rendering retains unresolved game-state/representation findings; no universal tool pass is claimed.

The scripted-system worker and independent decision auditor passed twelve focused observer/lifecycle tests and all eleven national-policy groups.
The ten existing panel groups and nineteen action-contract cases also passed after the update seam was introduced.
The localisation specialist reviewed 65 Camp UI keys, preserving dynamic tokens, costs and action meanings; the parent reviewed the final text in native previews.
Exact file inventories, reference citations and test receipts are in `live_updates_handoff.md`, `live_audit_handoff.md`, `camp_localisation_handoff.md` and `skill_handoff.md` in the same ignored task directory.
The canonical scripted-GUI skill now requires automatic management-panel updates, complete cache invalidation and lifecycle review; only that owned addition is included, preserving unrelated skill edits.
Skills used: scripted GUI, event assets, decisions/missions, scripted-system/subagent routing, localisation prose guidance, skill maintenance and shared Git commit isolation.
No requested functionality or controls were simplified or omitted; the manual controls were removed by explicit user direction.
The final isolated candidate also passed all five selected suites: observer lifecycle, national policies, humanitarian panel projection, shared GUI actions and cost display.
The exact tested tree and logs are recorded in `.tmp/national_policy_panels/consistency/candidate_tests.json`; subsequent reconciliation changes documentation only.

The commit uses a separate Git index. Pre-existing Event 034 receipt work remains in the working tree at its relocated operation-body position, with its unrelated tuning change; unrelated Kruger, migration cleanup, Event 037 and CXT documentation hunks remain outside this commit. The converted decision file retains the necessary removal of an invalid root-level constant assignment; its canonical value already exists in the committed constants.
