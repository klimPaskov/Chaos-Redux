# IW-058 ASY country package closure audit v80

Audit date: 2026-08-01.

Scope: bounded closure audit for the Assyria carrier `ASY` and Event 006 package `iw_058`, including the current gameplay package, vanilla carrier history, state 676 anchor, host and force contracts, FORM-18 adapters, focus and decision surfaces, AI strategy, identity and party surfaces, and the portrait source packages under `docs/assets/006_independence_wave/asy_roster_clearance_v37_2026_07_29/` and `docs/assets/006_independence_wave/asy_portrait_replacements_v41_2026_07_29/`.

## Decision

IW-058 remains **BLOCKED / FAIL-CLOSED** for runtime admission.

The gameplay package is structurally present, but the three grounded route consumers do not have a single current, independently reconciled sourced-male promotion record with matching runtime evidence.

The central runtime content-attestation trigger must continue to omit `iw_058`; adding it would bypass unresolved portrait and identity gates.

No gameplay, `.gfx`, portrait DDS, country-tag, or central attestation file was changed in this audit.

## Country package coverage checklist

| Surface | Result | Evidence and identifiers |
| --- | --- | --- |
| Carrier and origin | PASS structurally | Vanilla `ASY` remains the carrier in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:338`. `is_independence_wave_iw058_country` requires `original_tag = ASY`, Event 006 independence-wave origin, `independence_wave_package_id = iw_058`, `independence_wave_package_iw058_assyria`, and rejects Soviet-collapse origins in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:45-56`. |
| Capital and state anchor | PASS structurally | `can_initialize_independence_wave_iw058_package` requires the setup anchor target and capital state `676`; `independence_wave_iw058_anchor_secured` requires state `676` owned and controlled by ASY in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:911-974`. |
| Reservation and map binding | PASS | `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv` binds IW-058 to reservation group `RG-NORTHERN-MESOPOTAMIA` and state `676`; `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` records `IW-058`, `ASY`, `676`, `Mosul`, and `RG-NORTHERN-MESOPOTAMIA`. IW-060 uses the separate state `421` slot in the same broad region, so no local anchor collision was found. |
| Former-host contract | PASS structurally | `can_initialize_independence_wave_iw058_package` requires `independence_wave_setup_former_host` to exist and not equal ASY; `has_independence_wave_iw058_former_host` persists and validates the host target in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:165-177` and `956-975`. |
| Setup and force receipts | PASS structurally | `independence_wave_setup_iw058_assyria` loads the IW-058 force mapping, applies the dynamic starting force, defines the Assyrian Levies Detachment template, records force receipts, applies cosmetics and institutional/political surfaces, assigns the full focus framework, and registers the Mesopotamian Federation profile in `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1370-1474`. |
| Final gameplay validation | PASS structurally | `independence_wave_validate_iw058_package` checks setup, force receipts, cosmetic/institutional/political surfaces, full focus framework, route and host contracts, formable registration, signature module registration, state 676 anchor, route mutex, and bounded IW-058 values in `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1513-1547`. This validator does not replace the separate visual content-attestation gate. |
| Cleanup | PASS structurally | `independence_wave_cleanup_iw058_assyria` removes all IW-058 decisions, closes FORM-18 ledgers, releases the force package, clears generation-scoped division provenance and event targets, removes ideas and IW-058 leader roles, drops cosmetics, clears route/setup/formable flags and variables, and returns to the generic focus tree in `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1830-2149`. |
| Runtime admission | BLOCKED by design | `has_independence_wave_runtime_package_adapter_for_execution_id` includes `iw_058` at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-35`, but `has_independence_wave_runtime_package_content_attestation_for_execution_id` lists only the independently admitted package IDs and omits `iw_058` at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:72-89`. The preflight requires both adapter and content attestation at lines 94-100. |

## File surface checklist

| Surface | File or path | State |
| --- | --- | --- |
| Country carrier | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt` and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/ASY - Assyria.txt` | Vanilla carrier intentionally reused; no mod-side history replacement was required by the current package design. |
| State anchor | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/676-Mosul.txt` | Baseline owner/controller is IRQ, cores include IRQ/KUR/ASY, capital is state 676, and the package requires an explicit transfer/ownership contract before setup completion. |
| Package triggers | `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt` | ASY identity, route mutex, former-host, anchor, setup, force, values, and FORM-18 contracts present. |
| Package effects | `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt` | Setup, final validation, leader/party/idea surfaces, force receipts, and cleanup present. |
| Characters and traits | `common/characters/006_independence_wave_iw043_iw058_characters.txt` and `common/country_leader/006_independence_wave_iw043_iw058_traits.txt` | Four IW-058 character consumers and their route traits present. |
| Ideas | `common/ideas/006_independence_wave_iw043_iw058_ideas.txt` | Opening and route-lifecycle ideas present, including `independence_wave_iw058_provisional_council_idea`, `independence_wave_iw058_exposed_mosul_corridor_idea`, and `independence_wave_iw058_fragile_diaspora_links_idea`. |
| Decisions and missions | `common/decisions/categories/006_independence_wave_iw043_iw058_categories.txt` and `common/decisions/006_independence_wave_iw043_iw058_decisions.txt` | `independence_wave_iw058_council_of_communities_category` and its opening, guarantee, crisis, host, FORM-18, and sovereign-autonomy actions are present. |
| Focus tree | `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` and `common/national_focus/006_independence_wave_focus.txt` | Twenty-five ASY shared focuses and the package focus-loading surface are present. |
| AI | `common/ai_strategy/006_independence_wave_iw043_iw058_ai_strategy.txt` | Nine ASY-specific strategy lanes are present and gated by exact ASY setup/route/crisis state. |
| Formable identity | `common/countries/006_independence_wave_formable_cosmetics.txt` | ASY route cosmetics and `MESOPOTAMIAN_FEDERATIONX` are defined. |
| Dispatch registry | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` and `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` | Adapter is registered; content attestation remains intentionally closed. |
| Portrait sprites | `interface/006_independence_wave_iw043_iw058_portraits.gfx` and `gfx/leaders/006_independence_wave/` | Eight package large-portrait sprite names are registered and all referenced DDS files exist. No small/advisor sprites are defined by design. |
| Localisation | `localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml`, `..._focus_l_english.yml`, `..._decisions_l_english.yml`, `..._categories_l_english.yml`, and `..._events_l_english.yml` | Country, party, character, idea, focus, decision, category, event, tooltip, and cosmetic keys are present per the prior focus/localisation audits. |

## Politics, leaders, portraits, flags, advisors, and parties

The four country consumers are `ASY_independence_wave_provisional_national_council`, `ASY_independence_wave_concordat_council`, `ASY_independence_wave_civic_national_assembly`, and `ASY_independence_wave_levies_guardianship` in `common/characters/006_independence_wave_iw043_iw058_characters.txt:51-89`.

All four character records set `gender = male` and only define `civilian.large` sprites.

The opening consumer displays the existing project-owned `ASY_gallo_shabo` identity; reusing Gallo as the separate Civic National Assembly consumer would be exact same-project identity reuse and requires an explicit parent role decision.

The concordat, civic, and levies records use institutional character names, which is compatible with the council/assembly/guardianship institutional-body naming rule, but their grounded route portraits still require the independent sourced-male evidence below.

No female leader metadata, opposite-gender pool, small portrait, advisor portrait, or advisor icon was introduced.

Party names are set by the IW-058 political-surface effect and localized in `localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml`; the route party IDs include `ASY_independence_wave_concordat_council_party`, `ASY_independence_wave_civic_national_assembly_party`, `ASY_independence_wave_levies_guardianship_party`, and the provisional/traditional/popular/security party variants.

The ASY route cosmetics `ASY_independence_wave_national_councilX`, `ASY_independence_wave_church_compactX`, `ASY_independence_wave_civic_federationX`, `ASY_independence_wave_security_guardianshipX`, and `MESOPOTAMIAN_FEDERATIONX` are present and collision-free in the local country-tag audit.

### Grounded route portrait gate

| Consumer | Intended identity and package evidence | Current closure status |
| --- | --- | --- |
| `ASY_independence_wave_provisional_national_council` / `GFX_portrait_ASY_independence_wave_provisional_national_council` | Existing sourced Gallo Shabo treatment is documented in `docs/assets/006_independence_wave/sourced_portrait_treatments_2026_07_22/` and the current character record names `ASY_gallo_shabo`. | Existing opening identity is accepted as a current project-owned asset. It is not an automatic replacement for the Civic National Assembly role. |
| `ASY_independence_wave_concordat_council` / `GFX_portrait_ASY_independence_wave_concordat_council` | Ignatius Afram I Barsoum source and repaint are in `docs/assets/006_independence_wave/asy_roster_clearance_v37_2026_07_29/`; v41 records authoritative Commons API and PD-Syria rights evidence. v38 previously failed its rights/jurisdiction gate, and no fresh v80 visual/package attestation reconciles that change. The v37/v41 handoff claims runtime DDS SHA-256 `86616a420cf00473d5422c140337b600b9542cfcf4456d34d959de41cd05b48f`, while the checked-in DDS is `8CFD82ACEE444E9C026FAB0688DF7C5C797D8D4E237F3CAF72F7575EBD77C085`; the hash mismatch is unresolved. | BLOCKED pending a current independent source/rights/visual/runtime reconciliation and parent-owned DDS promotion evidence. |
| `ASY_independence_wave_civic_national_assembly` / `GFX_portrait_ASY_independence_wave_civic_national_assembly` | Rev. Joel E. Werda/Warda source in v37 is only 283x378 and the source tranche did not establish his later-life or 1936 office status. The v38 visual audit failed identity-detail and historical-role gates. The candidate PNG is not present under the documented `processed_png/` path and no runtime DDS promotion is authorized. | BLOCKED pending a detailed solo source or an explicitly approved same-project identity with a distinct civic-national role. Gallo Shabo reuse remains a parent decision, not a silent fallback. |
| `ASY_independence_wave_levies_guardianship` / `GFX_portrait_ASY_independence_wave_levies_guardianship` | Malik Ismail II of Upper Tyari has the strongest direct Levies/security relevance and a sourced candidate under `repaints_processed/`, but the exact IW-058 date versus his 1936 death and active officeholder status remain unresolved. Agha Petros is wrong-era and Kaiserreich-owned, Malik Khoshaba is Kaiserreich-owned as `ASY_khoshaba_yosip`, and Shamoun Hanne Haydo remains rights-blocked in v41. | BLOCKED pending the exact event-date/active-role ruling or a new cleared identity. |

The current DDS inventory is `portrait_ASY_independence_wave_provisional_national_council.dds` SHA-256 `129FC2C576C57871EBABA5E715AF35B4A1D50A4D655CD93E0EEB1E9E79CC1F43`, `portrait_ASY_independence_wave_concordat_council.dds` SHA-256 `8CFD82ACEE444E9C026FAB0688DF7C5C797D8D4E237F3CAF72F7575EBD77C085`, `portrait_ASY_independence_wave_civic_national_assembly.dds` SHA-256 `ED1F449FD16A21B84E5015983A9C6A84F47291D9B4F097067F79B8D6211F3D9E`, and `portrait_ASY_independence_wave_levies_guardianship.dds` SHA-256 `1A8AE9C6327D2C2BEA323D867D9775CA669BD7BEE8E348ABA14429B8E782142A`.

The v41 Barsoum references use a nonexistent `asy_roster_clearance_v37_2026_07_29/processed_png/` directory; the actual candidate directory is `repaints_processed/`. This stale historical path and the Barsoum runtime hash mismatch are recorded here rather than silently rewriting archived asset manifests.

## Focus, decision, idea, and asset issues

The ASY focus route is present in `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` with the following concrete IDs: `independence_wave_iw058_assemble_provisional_national_council`, `independence_wave_iw058_hold_mosul_council_quarter`, `independence_wave_iw058_seat_church_civic_and_village_delegates`, `independence_wave_iw058_secure_nineveh_approaches`, `independence_wave_iw058_open_diaspora_liaison_bureau`, `independence_wave_iw058_write_four_community_guarantees`, `independence_wave_iw058_settle_church_and_civil_jurisdiction`, `independence_wave_iw058_discipline_the_levies_board`, `independence_wave_iw058_request_external_guarantees`, `independence_wave_iw058_entrench_mosul_recognition`, `independence_wave_iw058_convene_concordat_council`, `independence_wave_iw058_charter_church_civic_compact`, `independence_wave_iw058_link_synods_villages_and_diaspora`, `independence_wave_iw058_ratify_concordat_state`, `independence_wave_iw058_convene_civic_national_assembly`, `independence_wave_iw058_charter_municipal_and_community_chambers`, `independence_wave_iw058_bind_diaspora_experts_to_public_service`, `independence_wave_iw058_ratify_civic_national_state`, `independence_wave_iw058_authorize_levies_guardianship`, `independence_wave_iw058_restore_civilian_command`, `independence_wave_iw058_fortify_mountain_river_corridor`, `independence_wave_iw058_negotiate_former_host_settlement`, `independence_wave_iw058_offer_mesopotamian_autonomy_charter`, `independence_wave_iw058_convene_mesopotamian_federal_congress`, and `independence_wave_iw058_ratify_mesopotamian_settlement`.

The church and civic branch mutexes are explicit in the focus file, and the route trigger `has_valid_independence_wave_iw058_route_mutex` rejects simultaneous church and civic route flags.

The decision category `independence_wave_iw058_council_of_communities_category` covers the opening anchor, council seats, four community guarantees, church/civil competence, diaspora experts, levies discipline, Nineveh patrol, corridor fortification, external guarantees, former-host security settlement, reclamation crisis, FORM-18 federal congress, member charters, defence/revenue, sovereign autonomy, and guarantee reopening actions in `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`.

The prior package focus/localisation audit found all package-local title, description, icon, decision, mission, and tooltip keys present; the remaining shared focus geometry diagnostics are outside this ASY closure scope.

The asset package has no advisor icons and no small portrait consumers. This is a deliberate surface restriction, not a missing advisor fallback.

## Starting military, technology, industry, supply, and production

The vanilla ASY carrier history at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/ASY - Assyria.txt:1-21` starts at capital state 676 with infantry weapons, mountaineers, trucks, artillery, fuel silos, optional camelry, and vanilla characters `ASY_shimun_eshai` and `ASY_benjamin_arsanis`.

The package does not rewrite the vanilla carrier history; its starting force is supplied by the dynamic Event 006 allocator and verified by IW-058 force receipts and current-generation formation checks.

State 676 at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/676-Mosul.txt` has the vanilla IRQ owner/controller baseline, ASY core, manpower, oil, infrastructure, and victory points; the package's setup and final contracts require state 676 to be owned and controlled by ASY before the relevant actions.

No new naval, air, port, railway, resource, supply, or production override was introduced by this audit.

The installed package exposes no Technology Tree Viewer, so technology-tree placement, unlock, and prerequisite rendering remain an unresolved tooling limitation; vanilla carrier technology syntax was read directly from the installed history file and the required offline documentation.

## AI and playability

The ASY AI file contains `independence_wave_iw058_foundation`, `independence_wave_iw058_reserve_recovery`, `independence_wave_iw058_tracked_crisis`, `independence_wave_iw058_church_compact_route`, `independence_wave_iw058_civic_assembly_route`, `independence_wave_iw058_guardianship_route`, `independence_wave_iw058_civilian_normalization`, `independence_wave_iw058_federal_settlement`, and `independence_wave_iw058_sovereign_autonomy` in `common/ai_strategy/006_independence_wave_iw043_iw058_ai_strategy.txt:114-254`.

Each strategy is gated by `original_tag = ASY`, exact IW-058 country/setup state, route or crisis flags, and reserve checks where applicable.

No whole-world on-action or AI scan was introduced, and no live HOI4 session was launched.

Because runtime content attestation remains closed, live route survivability and AI execution are not claimable as complete even though the static strategy contracts are present.

## FORM-18 and terminal settlement

`is_independence_wave_iw058_form18_carrier` requires exact ASY/IW-058 setup, the Mesopotamian autonomy route, no Levies guardianship route, the Mesopotamian Federation family, and a loaded formable profile at `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:446-454`.

`has_independence_wave_form18_local_settlement_contract` requires the capstone, all four community guarantees, church/civil competence, autonomy jurisdiction, council seats, diaspora liaison, anchor defense, corridor fortification, former-host security settlement, civilian-law Levies recognition, bounded values, and state 676 ownership/control at lines 1179-1199.

The terminal opening gate rejects both modes, both receipts/completions, active formable identity/integration, and prior settlement completion at lines 1201-1222.

The federation and sovereign-autonomy finalization gates reject the opposite mode and receipt/completion state at lines 1224-1249.

No cross-mode terminal settlement defect was found; the FORM-18 route remains unreachable through normal runtime until content attestation is admitted.

## Validation performed

- `python -B .tools/audit_hoi4_country_tags.py --workshop-root C:\__chaosx_no_workshop__ --local-mod-root C:\__chaosx_no_local_mods__` completed with `collisions=0`, `custom_cosmetic_collisions=0`, `identity_matches=50`, and `safe_x_tags=452`. The explicit empty roots kept this run bounded to the repository and vanilla reference rather than scanning the full workshop collection.
- `python -B .tools/audit_event6_allocator.py` completed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 14 attested packages, and 13 compatible reservation groups.
- PowerShell static reference check confirmed all eight `GFX_portrait_*` texture paths in `interface/006_independence_wave_iw043_iw058_portraits.gfx` resolve to existing DDS files.
- PowerShell static character check confirmed all four ASY IW-058 character consumers are male and only use `civilian.large` portrait slots.
- PowerShell source/runtime hash check recorded the four current DDS hashes above and exposed the Barsoum v37/v41 claimed hash mismatch.
- The required offline Paradox wiki pages and installed vanilla documentation for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, events, decisions, ideas, AI, country creation, focuses, characters, portraits, states, and maps were read before this audit.

## Skipped meaningful validation

- No Hearts of Iron IV process was launched, as required by the repository instructions; live consumer and save validation remain parent/user-owned.
- No Technology Tree Viewer render was possible because the installed MCP package exposes no Technology Tree Viewer.
- No new map rewrite or live map mutation was attempted; the existing state-anchor and reservation evidence was sufficient for this bounded country audit.
- No portrait DDS promotion or visual pipeline re-audit was attempted because the current Barsoum runtime hash contradicts the v37/v41 handoff and Werda/Malik remain blocked by independent gates.

## Changed files and behavior

Only this handoff file was added: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw058_asy_package_closure_audit_v80_2026_08_01.md`.

No tags, states, leaders, parties, focus IDs, decision IDs, localisation keys, formable IDs, gameplay effects, dispatch gates, `.gfx` definitions, or DDS files were changed.

Before and after behavior is therefore unchanged: IW-058 retains its structural setup/cleanup and FORM-18 contracts but cannot pass central runtime preflight because its content-attestation entry is absent.

## Remaining blockers and next actions

1. Reconcile Ignatius Afram I Barsoum's v38 rights failure versus v41 rights resolution, obtain a current independent visual/package audit, and reconcile or replace the checked-in `portrait_ASY_independence_wave_concordat_council.dds` with parent-owned hash evidence.
2. Resolve Rev. Joel E. Werda's low-resolution identity/detail and 1936 life/office gate, or obtain a distinct rights-clear civic-national male source; do not silently assign the existing Gallo Shabo consumer.
3. Resolve Malik Ismail II's exact IW-058 event date and active officeholder interpretation, or obtain a new rights-clear post-1936-relevant Levies/security male source; do not use Agha Petros, Malik Khoshaba, or Haydo as unreviewed fallbacks.
4. Correct or supersede the stale v41 `processed_png/` Barsoum path in a future asset-doc pass without rewriting historical provenance, then record the final candidate-to-DDS hash chain.
5. Only after all three route consumers have current independent passes and the full post-wire ASY package audit is complete should the parent consider adding `constant:independence_wave_package_id.iw_058` to `has_independence_wave_runtime_package_content_attestation_for_execution_id`.

## Simplifications, omissions, and blockers

No fallback portrait, generic/generated replacement, opposite-gender pairing, advisor surrogate, tag remap, map mutation, or central admission bypass was introduced.

The package is incomplete for runtime release solely because the grounded portrait and content-attestation gates remain unresolved; static country, map, focus, decision, force, AI, formable, and cleanup surfaces are present but do not substitute for that gate.

Parent review and commit are required.
