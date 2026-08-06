# Event 006 IW-029 Bosnia country-package audit — 2026-08-06 re-audit

## Verdict

IW-029 (Bosnia, carrier `BOS`) is conditionally wired and content-complete at source level after the parent moved BOS character attachment into the synchronous `chaosx.nr6.350` roster event. This audit made no gameplay edits. The only file changed by this subagent is this handoff, which replaces the stale pre-adapter audit.

Admission remains **HOLD / fail-closed** for one exact package evidence reason: the required MCP `ai_strategy_factor` route returns `PROBABILITY_SURFACE_EMPTY` for the Bosnia AI strategy file. The fixed package contract now explicitly requires the former host to remain `YUG` in all three runtime/setup proofs. This is an evidence blocker, not a claim that the package source is absent. The shared focus, event, map, and Technology Tree Viewer limitations listed later are non-BOS evidence boundaries, not additional IW-029 package blockers.

The earlier handoff statements that no BOS adapter, package files, portrait, or central attestation existed are superseded by this re-audit.

## Scope and references

The audited package surfaces are `common/scripted_triggers/006_independence_wave_bosnia_package_triggers.txt`, `common/scripted_effects/006_independence_wave_bosnia_package_effects.txt`, `common/decisions/006_independence_wave_bosnia_decisions.txt`, `common/ideas/006_independence_wave_bosnia_ideas.txt`, `common/script_constants/006_independence_wave_bosnia_constants.txt`, `common/characters/006_independence_wave_bosnia_characters.txt`, `common/ai_strategy/006_independence_wave_bosnia.txt`, `localisation/english/006_independence_wave_bosnia_l_english.yml`, `interface/006_independence_wave_iw029_bosnia_portraits.gfx`, the Event 006 roster event in `events/006_independence_wave.txt`, and the central package dispatch and region-03 binding files.

The exact localization path is `localisation/english/006_independence_wave_bosnia_l_english.yml`; the similarly named `006_independence_wave_iw029_bosnia_l_english.yml` path is not present.

Required offline Paradox wiki pages, relevant character, country, state, focus, decision, event, map, portrait, interface, and AI pages, and the corresponding vanilla documentation files were read before this audit. Vanilla Bosnia and state history were used as the country and map precedent.

## Country-package coverage checklist

| Surface | Evidence | Result |
|---|---|---|
| Tag and country identity | Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:189` maps `BOS` to `countries/Bosnia.txt`; the package deliberately reuses the vanilla carrier. | PASS |
| Package registry and central admission | `iw_029` is present in the region-03 loader/reservation, central setup/final-validation/cleanup dispatch, runtime adapter, content attestation, exact `BOS` preflight, and scenario preflight. | PASS |
| Candidate anchor | `common/scripted_triggers/006_independence_wave_bosnia_package_triggers.txt:15-23` requires exact BOS, capital/state 104, and an available non-BOS owner; region-03 uses reservation group `rg_104`. | PASS |
| State and map binding | Vanilla states 104 and 804 are YUG-owned with BOS cores; state 104 is Sarajevo and the package capital anchor. Current map MCP inspected both states and region 3. | PASS for current map; no write performed |
| Former-host relationship | Setup/runtime triggers require a living `YUG` former host with `liberation_release_protected_state` owned by the released country. | PASS after parent added the explicit fixed-host assertion to all three proofs |
| Character and commander | `BOS_independence_wave_drina_council` has male metadata, two large portrait consumers, five country-leader ideologies, and a corps-commander role. | PASS |
| Character attachment | `events/006_independence_wave.txt:219-233` idempotently recruits BOS from `chaosx.nr6.350` and sets the BOS checkpoint only after `has_independence_wave_bos_command_roster`. The BOS scripted setup effect no longer calls `recruit_character`. | PASS after parent correction |
| Portrait and source state | The sourced male Mehmed Spaho source-placeholder handoff, runtime DDS, and portrait-specific GFX sprite are present and wired. | PASS as `source_placeholder`; not a styled final |
| Flags | Vanilla BOS flag families remain the carrier flags; no unsupported route-specific flag art is claimed. | PASS for reuse |
| Parties and politics | Setup initializes democratic, communist, neutrality, and fascist party names and route effects set five route ideologies and popularity profiles. | PASS |
| Ideas and lifecycle | Two lifecycle ideas plus five mutually exclusive route ideas are defined, localized, added, refreshed, and removed by the package effects. | PASS |
| Decisions and mission | One 420-day founding mission and eleven paid projects are defined in the BOS category with availability, cancellation, timeout, cost, AI, and localized tooltip surfaces. | PASS |
| Focus contract | Setup selects the additive shared overlay when the installed carrier exposes `austro_hungarian_releasable_focus`, otherwise the full Event 006 framework, and registers all five government routes, four host routes, power struggle, ambition, signature, league, and formable surfaces. The overlay calls all five BOS focus hooks. | PASS at package source level; shared-tree MCP has unrelated diagnostics |
| Formable and network contract | Setup selects the Danubian Confederation family and registers the league/network route. | PASS |
| Force package | Setup loads p29 `mountain_frontier`, military tradition 66, and exactly five documented reinforcement pathways before applying the dynamic starting force. | PASS at source level; live force receipt not run |
| Technology, industry, supply | Vanilla BOS has three research slots and Yugoslav-clone starting technology; dynamic force setup supplies package opening forces and stockpiles. States 104/804 have current vanilla infrastructure and supply data. | PASS for intended shared contract; no Technology Tree Viewer is installed |
| AI | Four route-aware BOS AI strategy blocks are present with centralized priorities and host restraint. | HOLD for quantitative evidence because the required probability adapter is empty |
| Cleanup | BOS cleanup removes its mission, decisions, ideas, variables, and flags; shared reset clears force, focus, host, network, and generation state. | PASS at source level |
| Localization and assets | All package decision, idea, character, party, and tooltip keys resolve in the actual BOM-encoded localization file; the portrait GFX texture exists. | PASS |

## File-surface checklist

The package-specific gameplay files are present at the paths listed below.

- `common/scripted_triggers/006_independence_wave_bosnia_package_triggers.txt` defines package identity, exact candidate/runtime/setup gates, roster, ledgers, active projects, live league phase, and complete setup proof.
- `common/scripted_effects/006_independence_wave_bosnia_package_effects.txt` defines setup, politics, route effects, focus signatures, lifecycle, decisions, dynamic-force calls, final validation, and cleanup.
- `common/decisions/006_independence_wave_bosnia_decisions.txt` defines `independence_wave_bos_drina_council_category`, the founding mission, and eleven BOS projects.
- `common/ideas/006_independence_wave_bosnia_ideas.txt` defines `bos_divided_drina_authority`, `bos_drina_compact`, and five route ideas.
- `common/script_constants/006_independence_wave_bosnia_constants.txt` centralizes politics, ledger thresholds, mission duration, and AI tuning.
- `common/characters/006_independence_wave_bosnia_characters.txt` defines `BOS_independence_wave_drina_council`.
- `common/ai_strategy/006_independence_wave_bosnia.txt` defines the Sarajevo survival, host restraint, settled Drina, and emergency command strategy blocks.
- `localisation/english/006_independence_wave_bosnia_l_english.yml` contains the package-facing names, descriptions, route strings, character strings, and tooltips.
- `interface/006_independence_wave_iw029_bosnia_portraits.gfx` registers `GFX_portrait_BOS_independence_wave_mehmed_spaho`.
- `events/006_independence_wave.txt:184-236` owns the synchronous roster checkpoint event used by BOS and other fixed-tag Event 006 packages.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` dispatches BOS setup, final validation, and cleanup.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` admits `iw_029` in runtime, content-attestation, exact-origin, and scenario preflight surfaces.
- `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt` and `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt` bind BOS to state 104, optional state 804, YUG host data, and `rg_104`.

## Detailed findings

### Map, state, and host setup

Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/104-Bosnia.txt:16-36` has YUG ownership, Sarajevo victory points, infrastructure 3, two civilian factories, an air base, BOS/YUG cores, and local supplies 7.

Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/804-Herzegovina.txt:15-31` has YUG ownership, a victory point, infrastructure 2, BOS/YUG/HRZ cores, and no local supplies.

The region-03 package loader saves BOS as the candidate country and state 104 as the anchor with its owner as the primary host, while reservation includes optional state 804. The current installed-map package-binding documents also record `104=YUG|804=YUG`.

The fixed binding is now explicit and fail-closed. `is_independence_wave_exact_package_iw_029_runtime_ready`, `can_initialize_independence_wave_iw_029_package`, and `has_prepared_independence_wave_iw_029_package_setup` each require the former-host target to be `tag = YUG`, not ROOT, living, and still owning the protected state. This preserves the installed `104=YUG|804=YUG` binding rather than accepting an arbitrary protected host.

Current map MCP evidence is authoritative for the installed map but not a substitute for the missing fail-closed trigger. `hoi4.map_inspect` inspected states 104 and 804 and region 3 at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a1f85c08fc487192e39673c54c476cfbe09659e3d19bb8575470884b3309591/355a9e9025b7dc5151950f33c72a42a77ab2a5fffc38c534e2ce097c287143d9/map-inspect.181a16b4b11bb771.json`.

The selected state/region geometry, membership, networks, adjacencies, supply nodes, and railways were valid. Global map validation is false because unrelated `map/buildings.txt` records contain 1,323 `MAP_BUILDING_POSITION_INVALID` and 1,331 `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics; no Bosnia-specific geometry error was reported.

The deterministic state render passed at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b11da464a58a00f392d20160c03b0af4a5e89f3dc88629a12e57291b26e12dba/c29a962b4fbcd0ad05c6046e2c407cdb3cd1fa8add2345add4eea7047f4b69f9/map-state.png`.

No `hoi4.map_rewrite` was run because this audit had no approved map mutation.

### Politics, leaders, portraits, flags, and parties

The parent correction now attaches `BOS_independence_wave_drina_council` from the hidden country event only when the active BOS package lacks the character. The following checkpoint requires the character to exist and be a corps commander, so the dynamic force and setup proof cannot silently pass a missing roster.

The character is explicitly male and uses the male localized identity “Mehmed Spaho” for all five country-leader ideologies and the corps-commander role. The portrait pairing therefore satisfies the gender and source requirements. The council name is an institutional role key while the localized identity is a sourced real male, not an opposite-gender or generic pool pairing.

The portrait worker handoff is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw029_bosnia_portrait_source_placeholder_2026_08_06.md`. It records the Wikimedia Commons source, exact crop, processed 156x210 candidate, DDS checksum, source-placeholder state, and the runtime sprite path. The runtime texture is `gfx/leaders/006_independence_wave/portrait_BOS_independence_wave_mehmed_spaho.dds`.

No advisor, dossier, commander-small, or alternate portrait asset is defined. This is an explicit bounded asset surface, not an unreported missing consumer.

Setup starts democratic with elections disabled during the provisional authority, sets all four party names, and assigns popularity profiles that sum to 100 for the initial state and each of the constitutional, workers, traditional, emergency, and patron routes. Route effects promote the same male character under conservatism, marxism, centrism, despotism, or liberalism as appropriate and replace the route idea atomically.

Vanilla BOS flag families remain the carrier flags. No unsupported generated route flag is claimed.

### Focus, decisions, ideas, and assets

The package setup effect registers the shared `independence_wave_focus_tree` dynamically: it selects `independence_wave_focus_assignment.additive_overlay` when the installed BOS carrier exposes `austro_hungarian_releasable_focus`, preserving the meaningful vanilla tree, and selects `independence_wave_focus_assignment.full_framework` otherwise. Both branches register all five government routes, all four host routes, the municipal-commission-versus-industrial-security power struggle, ambition family, signature module, league route, and Danubian Confederation formable family. The shared overlay completion rewards now call the five `independence_wave_bos_focus_*` hooks for BOS.

The national focus MCP inspection resolved 184 focus nodes and 193 connectors. Its only blocking diagnostics are 14 missing generic/continuous vanilla focus sprites outside the BOS adapter, with five layout warnings; no BOS-specific node, icon, or assignment diagnostic was reported. Evidence is at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/918a982825834dff2be33825a8dab8aa4adf75b3ac038322e3de5e84ebaccb1f/fdde78743cc460de47946a863aedd1e44175cb281bbb139677996fb379298dcb/focus-inspect.5d8e1a3b15608287.json`.

The focus render completed with shared-tree diagnostics at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d0a9699de3bed2979acd7edfaec33d0329bb3b929bf39b4713db192ea82735c/be7435c0da6502ec73db5a4367d8e25516b0097d5e4eb7e15b41b5079227cb61/independence_wave_focus_tree.focus.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99315e3b89510ee95475cdcaa004b6120834db4ffe96f9ca9e101b1bae25ff3e/22f99073165243293e92eb2743e8d2eca07279603d622def8fbc4c88fa352239/independence_wave_focus_tree.focus.svg`.

The BOS decision category contains the 420-day `independence_wave_bos_hold_drina_council_together` mission plus eleven projects covering administration, security, host settlement, five government routes, sovereignty, and the Danube network. All decision names, descriptions, custom-cost text, effect tooltips, and cancellation/failure strings resolve in the package localization.

The two lifecycle ideas are refreshed from civic and mountain-defence ledgers at the 60-point stability threshold. Five route ideas are removed and replaced by route effects, and cleanup removes every package decision, mission, idea, route flag, ledger variable, and BOS lifecycle flag.

### Starting military, technology, industry, supply, and production

Vanilla Bosnia supplies three research slots and the Yugoslav-clone support, engineer, mountaineer, infantry, truck, train, and DLC-gated tank/ship/air technology baseline. The package does not replace vanilla history or add a copied OOB.

The package loads `independence_wave_package_id.iw_029`, `independence_wave_force_profile.mountain_frontier`, `independence_wave_force_package_military_tradition.p29` (66), and five pathways: integrate militias, secure depots, convert defecting host units, recruit terrain units, and create a professional officer corps. It then calls the shared dynamic starting-force allocator, which owns the researched template, opening divisions, stockpiles, and inherited technology/slots.

The complete setup trigger requires the roster checkpoint, loaded p29 mapping, current-generation force receipt, applied force flag, exact five-pathway mask, no unsupported inheritance paths, and one of the two lifecycle ideas. The source chain is therefore fail-closed when the roster or allocator receipt is absent.

No package-specific production-line override, navy, air wing, or direct unit-history file is claimed. The vanilla starting history and shared allocator are the intended surfaces.

The installed package exposes no Technology Tree Viewer. Technology-tree engine inspection is therefore an unresolved limitation, not a pass claim.

### AI and playability

`common/ai_strategy/006_independence_wave_bosnia.txt` defines four route-aware strategies: Sarajevo survival, host restraint, settled Drina, and emergency command. Their enables require BOS package/setup flags and the relevant lifecycle or route state, and their priorities are centralized in `006_independence_wave_bosnia_constants.txt` with file-local mirrors where the AI fields require them.

The mandatory probability pass was attempted against `{ "path": "common/ai_strategy/006_independence_wave_bosnia.txt" }` with adapter `ai_strategy_factor`. The installed MCP returned `PROBABILITY_SURFACE_EMPTY` with blocker `No weighted blocks matched this request`, no artifacts, and no scenario ranking. Do not claim quantitative AI survival, strategy-factor balance, or allocator probability evidence until the adapter can discover this source or a supported source adapter is supplied.

The package is playable by source contract only after the host assertion and probability evidence blockers are resolved. Live game launch, save/load, and player-owned in-game validation were not performed.

### Event and checkpoint evidence

The current `chaosx.nr6.350` event owns the idempotent MAC/BOS runtime attachment and post-attachment checkpoints. The focused Event Chain Viewer lint inspection of `chaosx.nr6.350` returned no blocking diagnostics at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56d43f8e2179998c77f2ff0c19c887f7cc3585ecfa5e616709a2a2eb8a13a0d0/85c169c6631d3c2ca61d78d1eb408f56fee19de0b3c2edebc27cd0c5ec3f5594/event-lint-be8a459e7129.json`.

The current root Event 006 lint inspection also returned no blocking diagnostics at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ced480db025918ed14d60fd9b42e0835b96c2f0eafe37c26ef5c29acfe9d446/1d24b95e46b2c79505c430a5f9f4aa960dde313a3e2f2f1c55fd889f20d4b9d2/event-lint-be8a459e7129.json`.

The event render is partial because the large workspace defers helper/lifecycle projections, not because the BOS checkpoint has a reported blocking diagnostic. Current root render evidence is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94fc1f3ca4e352d19dc559ea2c326211272021fe93bb167ebed303145895f6c8/0890e1434733c19891ba55e67603847b644d5bc331e623c205cd07c187c2dcd3/event-overview-be8a459e7129.json`.

## Parent correction re-audit

The parent moved `recruit_character = BOS_independence_wave_drina_council` from the BOS scripted setup effect into `events/006_independence_wave.txt:223-226`, matching the repository rule that scripted effects do not own dynamic character recruitment. The event now checks the roster at `:230-233` and only publishes `independence_wave_bos_roster_checkpoint` after the character has the required corps-commander role.

The BOS setup effect at `common/scripted_effects/006_independence_wave_bosnia_package_effects.txt:331-384` now calls `chaosx.nr6.350`, initializes politics and ledgers, sets the generic focus contract, registers routes and formable family, loads the p29 force mapping, applies the dynamic starting force, enables the AI profile, and publishes package setup only when `has_prepared_independence_wave_iw_029_package_setup` is true.

The current source audit confirms that `recruit_character` is absent from the BOS scripted effect and present only in the event checkpoint contract. This removes the earlier gameplay blocker.

The parent focus-preservation correction also removes the earlier false full-framework claim. `can_attach_independence_wave_additive_focus_carrier` now admits BOS when `austro_hungarian_releasable_focus` is present; the BOS setup effect selects the additive assignment in that case and the complete-setup proof accepts either the additive or full assignment. The latest focus MCP inspection resolved 184 nodes and 193 connectors after this change, with no new BOS-specific diagnostic. This correction preserves the documented vanilla carrier tree while still delivering the shared Event 006 overlay and its five BOS hook calls.

## Cleanup and lifecycle

`independence_wave_cleanup_iw_029_bosnia` removes the BOS mission and eleven decisions, all package ideas, the two ledger variables, the roster/setup/lifecycle/AI flags, and every BOS route/project flag. The shared `independence_wave_reset_current_generation` and `independence_wave_end_active_origin` paths also clear generation variables, force mapping, focus runtime, host/network arrays, league membership, former-host ledgers, and origin ideas before provenance is reset.

No stale package-specific cleanup omission was found after accounting for the shared reset contract.

## Validation performed

- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` passed with 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions.
- All audited BOS package scripts and the touched Event 006 event file were brace-balanced by a read-only structural check.
- The actual BOS localization file begins with UTF-8 BOM `EF BB BF`, and all package decision, idea, character, party, and tooltip keys resolved in the package localization scan.
- The BOS portrait DDS has valid `DDS ` magic and 156x210 dimensions, and the exact sprite texture path exists.
- The current map MCP inspected states 104/804 and region 3 and rendered the state-layer evidence; unrelated global map diagnostics are recorded above.
- The current focus MCP inspected and rendered `independence_wave_focus_tree`; 14 generic missing-icon diagnostics and five layout warnings are recorded as shared-tree issues.
- The current Event Chain Viewer inspected and rendered both `chaosx.nr6.350` and root `chaosx.nr6.1`; both returned no blocking diagnostics but partial workspace analysis.
- The mandatory AI probability MCP route was attempted and is explicitly unresolved with `PROBABILITY_SURFACE_EMPTY`.
- No map write, gameplay runtime launch, save/load, or live AI simulation was performed.

## Changed files and handoff

This subagent changed only `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw029_bosnia_country_package_audit_2026_08_06.md` by replacing the stale audit. No gameplay, map, localization, portrait, focus, decision, event, character, or AI source file was edited by this subagent.

The parent’s re-audit correction changed the BOS roster ownership in `events/006_independence_wave.txt` and removed the recruit call from `common/scripted_effects/006_independence_wave_bosnia_package_effects.txt`; those gameplay edits are parent-owned and are described here for evidence only.

## Simplifications, omissions, and blockers

- **Only remaining IW-029 package evidence blocker:** the installed MCP `ai_strategy_factor` probability adapter cannot discover the BOS strategy file and returned `PROBABILITY_SURFACE_EMPTY`; no quantitative AI claim is made.
- Shared focus MCP validation remains false because of 14 unrelated generic/continuous focus icon references and five layout warnings; no BOS-specific focus diagnostic was found.
- Event MCP validation is partial because workspace-wide helper/lifecycle projections are deferred; no blocking diagnostic was returned for the inspected roots.
- Global map validation remains false because of unrelated `map/buildings.txt` position and floating-harbor diagnostics; no Bosnia-specific map error was reported.
- The installed package has no Technology Tree Viewer, so technology-tree engine evidence is unavailable.
- The portrait is intentionally a grounded source placeholder rather than a styled HOI4 final; its provenance, wiring, and placeholder state are documented and no fallback is claimed.

No other simplification, fallback, identity invention, unsupported gender pairing, missing package localization, or gameplay edit was made by this subagent.
