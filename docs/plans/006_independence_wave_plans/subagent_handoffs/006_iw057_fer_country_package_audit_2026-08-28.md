# IW-057 Far Eastern Republic country-package audit

Date: 2026-08-28

Owner: bounded Chaos Redux country-package audit

Event/package: Event 006 Independence Wave, IW-057 Far Eastern Republic (FER)

Disposition: **HOLD / PACKAGE-LOCAL / FAIL-CLOSED**.

No gameplay or central-dispatch source patch was justified by this audit. The package has a substantial local source surface, but the parent-owned identity, roster, flag, typed-probability, runtime-map, and central-admission receipts are not complete. FER was not promoted to central attestation, preflight, setup/final-validation/cleanup dispatch, startup recruitment, or deterministic Join.

## Authority and review basis

The Event 006 source-of-truth map remains the authority in `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`. Its current boundary is 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows; IW-057 FER is explicitly package-local or research-only and absent from central attestation and deterministic Join.

The design rows are `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:58`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:58`, and `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:35`. They define registered-tag reuse, automatic eligibility only when not living, ordered anchors `408|409`, reservation group `RG-408-409`, a compact Far Eastern corridor, and a sourced real male or authentic institutional identity requirement.

The package design is documented in `docs/events/006_independence_wave/far_eastern_republic_package.md:1-11`. It correctly states that FER uses ordered anchors 408/409, has no Event 006 character, portrait, flag, cosmetic tag, vanilla-history override, capital transfer, central dispatcher, attestation, normal preflight, SCN-008 preflight, or Join path.

Before source review I read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-focus-trees/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, and `.agents/skills/chaos-redux-comfyui/SKILL.md`. I also consulted the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, country creation, characters, focuses, technology, states, and map behavior, together with the corresponding vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

## Country-package coverage checklist

| Surface | Status | Evidence and disposition |
| --- | --- | --- |
| Tag and country identity | **Blocked** | Vanilla registers `FER = "countries/Fareastern Republic.txt"` in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:224`. The mod's Event 006 country-tag file does not add FER; the package deliberately reuses the vanilla carrier behind parent-owned rights flags. |
| Country/history shell | **Conditional, not admitted** | Vanilla FER history uses capital 563/Chita, three research slots, and vanilla starting research in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/FER - Far Eastern Republic.txt:1-3`. No Event 006 FER country or history override exists in the mod, which is correct while the package remains fail-closed. |
| Ordered map anchors | **Source-present, runtime-unproven** | `RG-408-409` reserves 408 Vladivostok or 409 Khabarovsk as one ordered compact anchor. Package triggers require ownership/control and a capital anchor in 408 or 409; dormant vanilla state 563 is explicitly excluded from Event 006 runtime allocation. |
| Former-host and collision safety | **Source-present, not admitted** | The package captures a former-host target, requires a living host to be at war or absent, preserves a protected host state, and rejects Soviet Collapse origin/flags. No central preflight receipt exists for FER. |
| Politics and parties | **Package-local source present** | Four route installers and four route party-name sets exist in the local effects file. They remain gated by package setup, identity rights, roster, and central admission. |
| Leader, roster, and advisors | **Blocked** | `independence_wave_fer_checkpoint_institutional_roster` only records parent-provided identity and command-roster flags; it does not create a character. No Event 006 FER leader, advisor, high-command, commander, or institutional roster consumer is accepted. |
| Portrait | **Blocked / research-only** | The same-day portrait gate keeps Pyotr Mikhailovich Nikiforov and Alexander Mikhailovich Krasnoshchyokov as research candidates only. No Event 006 character, portrait GFX, runtime DDS, or installed portrait path exists. The people-free 1923 passport is institutional evidence only. See `subagent_handoffs/006_iw057_fer_portrait_gate_2026-08-28.md`. |
| Flag and cosmetic identity | **Blocked** | No approved Event 006 FER neutral/runtime flag, cosmetic tag, or asset receipt exists. Event 005 FEV art and `GFX_portrait_FER_far_eastern_republic_council` are separate and are not valid substitutes. |
| Focus tree | **Shared source present** | FER has five callbacks in the shared `independence_wave_focus_tree`; no bespoke FER tree is authorized or required by the package. MCP inspection resolved 184 focuses and 195 connectors with no Event 006 blocking diagnostic. |
| Decisions and mission | **Package-local source present** | One activation-only 420-day founding mission and ten serialized projects are present with costs, effects, tooltips, and anchor-loss cancellation guards. Their runtime availability remains gated. |
| Ideas and lifecycle | **Package-local source present** | Seven FER ideas have icons/modifiers and are allowed only after `independence_wave_iw_057_identity_rights_cleared`. Setup, failure, compact, route, and cleanup effects are present. |
| Assets and icon wiring | **Partial** | Shared Event 006 focus/decision/idea icon references and FER localisation exist, but no FER Event 006 flag, portrait, character GFX, or runtime DDS/manifest exists. |
| Forces and setup | **Package-local source present, runtime-unproven** | FER uses mapped `regular_defectors` force profile `p57`, five reinforcement paths, and inherited navy/air gates. No live release/setup receipt is claimed. |
| Technology | **No package-specific surface claimed** | FER inherits vanilla history research; no Event 006 technology tree is authored. The installed package exposes no Technology Tree Viewer, so technology acceptance remains unresolved. Current tech inspect/render are partial helper projections and are not a source-accurate acceptance receipt. |
| Industry, supply, and production | **Source inheritance only** | The package does not invent a country history, factories, stockpile, railway, port, supply, or production fallback. Vanilla states 408/409 provide the inspected map/building context; live setup and supply behavior remain unproven. |
| AI and weighted logic | **Blocked / partial evidence** | Four FER strategy blocks and eleven mission/project `ai_will_do` candidates are authored, but the mandatory `chaosx_ai_probability_auditor` route is unavailable in this session. No balance, dominance, starvation, or live timing claim is made. |
| Localisation | **Source coverage present** | `localisation/english/006_independence_wave_far_eastern_l_english.yml:1-87` covers country/party names, category, mission/projects, ideas, focus callbacks, cost tooltips, blocked costs, and effects. The current Event 006 localisation audit records the FER administration-standard tooltip and blocked-cost coverage. |
| Central admission | **Intentionally absent** | FER is absent from central adapter/content-attestation/preflight lists, central setup/final-validation/cleanup dispatch, startup character recruitment, and deterministic Join. This absence is the required fail-closed state. |

## File-surface checklist and findings

| File | Identifiers or span | Finding |
| --- | --- | --- |
| `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt:11-252` | `is_independence_wave_far_eastern_package`, `is_independence_wave_fer_project_ready`, `has_independence_wave_fer_capital_anchor`, `is_independence_wave_exact_package_iw_057_runtime_ready`, `can_initialize_independence_wave_iw_057_package`, `has_independence_wave_fer_command_roster`, `is_independence_wave_exact_package_iw_057_tag_available` | Exact `original_tag = FER`, `iw_057`, Event 006 origin, current force generation, ordered 408/409 anchor, capital anchor, former-host, project, route, ledger, setup, roster, and cleanup gates are source-wired. The tag-availability proof deliberately does not use dormant 563. |
| `common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt:1-497` | `independence_wave_setup_iw_057_fer`, `independence_wave_fer_checkpoint_institutional_roster`, `independence_wave_dispatch_fer_package_setup`, `independence_wave_dispatch_fer_package_final_validation`, `independence_wave_dispatch_fer_package_cleanup` | Package-local setup, four government routes, focus hooks, compact ledgers, force/AI setup, validation, and cleanup exist. The roster checkpoint only consumes parent-owned receipts and never invents a leader or portrait. |
| `common/decisions/006_independence_wave_far_eastern_decisions.txt:15-603` | `independence_wave_fer_railway_compact_category`, `independence_wave_fer_hold_railway_council`, ten `independence_wave_fer_*` projects | One founding mission is activation-only (`available = { always = no }`); ten projects are serialized, costed, and cancellation-safe. All ten project cancellation triggers include `NOT = { has_independence_wave_fer_anchor_owned = yes }` after the 2026-08-25 lifecycle hardening. |
| `common/ideas/006_independence_wave_ideas_registry.txt:1221-1298` | Seven `fer_*` ideas | Ideas have modifiers/icons and are gated by FER identity-rights clearance. |
| `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:589-657` | `independence_wave_fer_railway_port_survival`, `independence_wave_fer_host_restraint`, `independence_wave_fer_settled_compact`, `independence_wave_fer_coastal_emergency_guard` | Source has four AI profiles and centralized constants. The settled-compact and coastal-emergency enable blocks omit the setup/current-generation guards used by the other profiles; this is a weighted surface risk, not a patched defect, because the required baseline/compare route is unavailable. |
| `common/scripted_effects/006_independence_wave_effects.txt:3613-3718` | `independence_wave_dispatch_package_setup`, `independence_wave_dispatch_package_final_validation`, `independence_wave_dispatch_package_cleanup` | Central dispatch calls no FER adapter. No central wiring was added because identity, roster, flag, typed-probability, and runtime receipts are incomplete. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:11-~590` | runtime adapter, content attestation, normal preflight, scenario preflight | The central OR-lists contain no `iw_057`; this is required fail-closed behavior. |
| `common/scripted_effects/006_independence_wave_join_effects.txt:270` | deterministic Join candidate chain | Candidate chain ends at admitted packages and contains no `iw_057`. |
| `history/general/006_independence_wave_character_recruitment_registry.txt` | startup roster registry | FER has no startup recruitment record while its identity/roster receipt is open. |
| `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1158-1235` and `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:477-490` | `independence_wave_load_package_iw_057`, `can_plan_independence_wave_package_iw_057` | Planner metadata and reservation availability are source-present, but planning eligibility is not central execution admission. |
| `common/national_focus/006_independence_wave_focus.txt:37-38,128,181,215,1447,1718` | `independence_wave_focus_tree`, five FER callback branches | Shared tree assignment/callbacks are present and remain conditional on package runtime gates. |
| `events/006_independence_wave.txt:5,12` | `add_namespace = chaosx.nr6`, `chaosx.nr6.1` | Event root and dispatch event are source-present. FER has no event-specific root or central admission branch. |

## Map and state setup

Vanilla source review confirms state 408 (`408-Vladivostok.txt`) and state 409 (`409-Khabarovsk.txt`) contain FER cores and their expected port/industry/air/infrastructure context. Vanilla state 563 (`563-TS 5.txt`) is the FER history capital/Chita carrier and is retained only as a dormant comparison/history reference; it is not an Event 006 release anchor.

The read-only `hoi4_map_inspect` call selected states 408, 409, and 563 and produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40d9163253b18d77883e71b226fe01d89f633eca94a90d34e365ecb030139821/fb01af88b6ead6a6fc5310b01cf020c9b362d07288260f321455cda54cc7e4a0/map-inspect.83e908658b9f56ae.json`. State/region membership and network/adjacency checks passed, but the global inspect reported 2,654 locator/position diagnostics, including unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` rows in the mod map. This is not FER-specific proof and prevents a clean global map acceptance claim.

The owner-layer `hoi4_map_render` passed and produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0610a166e8e08877d5a2fc27cddb5656b9ad93125156adfcd25b08ff7eef74c/1ea202874f52d0d4ae06e33ffee878eb968ed6b3efd88bfae20355fc3ca23776/map-owner.png`. No `hoi4.map_rewrite` was called, so map dry-run/review/apply/post-validation and rollback/recovery evidence are not applicable to this audit.

## Politics, leadership, portraits, flags, advisors, and parties

The local effects file defines constitutional, railway-charter, coastal-council, and coastal-emergency route installers and party names in `common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt:166-265`. These are source-local and guarded; they do not establish an accepted identity.

The current portrait gate `subagent_handoffs/006_iw057_fer_portrait_gate_2026-08-28.md` remains **BLOCKED / HOLD / FAIL-CLOSED / RESEARCH-ONLY**. Nikiforov is a research-attribution candidate with unresolved restored-1936 semantics and rights acceptance; Krasnoshchyokov has an unresolved role/date reconciliation and rights hold; the 1923 passport is people-free institutional evidence. The source masters are LFS pointers without local objects, and no 156x210 output, DDS, character definition, portrait GFX, or runtime path is installed.

The existing Event 005 asset `gfx/leaders/005_soviet_collapse/FER_leader.dds` and sprite `GFX_portrait_FER_far_eastern_republic_council` in `interface/005_soviet_collapse.gfx` belong to FEV/Soviet Collapse and are not reused. No opposite-gender portrait/name pairing exists because no Event 006 FER character or portrait consumer was added.

## Focus, decisions, ideas, and assets

The shared focus tree source has five FER callback branches for railway council, railway ports, coastal guards, former-host ledgers, and Pacific corridor work. `hoi4_focus_inspect` returned 184 focuses, 195 connectors, zero crossings/intersections/long connectors, and zero blocking diagnostics; its only warning was an unrelated vanilla `continuous_restrict_freedom_desc` localisation reference. The useful inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6baa41eaae01106c29bb85cca6eac60e7ae788dfc05f3fb8722978c4a094db78/c04588114ccbd2c4e076ae02b0f790c8ce548031c3dc8f500077dc9bb61bd81d/focus-inspect.82e9c552e92dc491.json`; the rendered tree is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a5463d0623b340dee9f4d756857dab2af290ef55dabb710a4c51dfe7d4bd766/6240509fe22958a9dd54bd7d6da42b1a9eb08358aecb64b14b643595a93c8a9f/independence_wave_focus_tree.focus.html`.

The source has one 420-day founding mission and ten projects with distinct costs/effects, project serialization, route gates, former-host ledgers, and anchor-loss cancellation. Seven ideas are identity-rights gated and have icon/modifier definitions. No FER-specific event GUI is introduced; the package consumes the shared Event 006 surfaces, so no package-owned GUI inspect/render claim is made.

The narrow `hoi4_event_inspect` trace for `chaosx.nr6.1` and matching overview render returned partial workspace results with zero blocking diagnostics. Useful artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7c460ce5fec474d50d3643e2da1b082ae57a8e85017bf21984759db460b403a/0c303ac2fb512a6c4f55b65fdee143a89722ae99c05dfc4db24c6f349c150a97/event-trace-c2878e0a5f2b.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b561e82c6c36715e392163479f72232717d493791c50fda29471ffb6ab3c3173/3228d9a00d5c81c8b7e1e4c5420bc86ffbcbd79b3e43ab14b8b9a7049e3070e7/event-overview-c2878e0a5f2b-manifest.json`. The event route is partial because the large workspace helper projection was deferred and the narrow source inventory resolved unexpectedly against vanilla event files; source review remains authoritative.

## Starting military, technology, industry, supply, and production

The package maps `regular_defectors` to force profile `p57` and uses the shared force setup/inheritance gates. It does not create a new FER OOB, equipment archetype, factory baseline, port, railway, supply hub, technology tree, or production fallback. Vanilla FER history remains the carrier reference and is not asserted as an Event 006 runtime release setup.

The read-only technology scan returned `TECH_INSPECTED_PARTIAL` with 672 technologies, 18 folders, 457 edges, 850 unlocks, 19,805 references, 1,189 issues, and four unresolved items; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e859e6de044d269bcdf7ea157e6d362615ce650bb24295046dd4e94acf039a7/2d8092f70ee7f93242e4321b7769d2105bcdc8f85632adf3a8eefc555b8b9/technology-scan-f5c719257c7d.json`. The corresponding technology render was also partial and not source-accurate. The installed package exposes no Technology Tree Viewer, so the required technology viewer acceptance remains unresolved.

## AI and playability

The four FER strategy profiles and constants are source-present. `independence_wave_fer_settled_compact` and `independence_wave_fer_coastal_emergency_guard` omit setup/current-generation guards, which is a known weighted-surface risk. I did not patch those blocks because the required `chaosx_ai_probability_auditor` custom route is not callable in this session and no owner-applied baseline/typed same-scenario comparison exists.

The mission probability source inspection used the exact eleven FER IDs from `common/decisions/006_independence_wave_far_eastern_decisions.txt`, returned `PROBABILITY_SOURCE_INSPECTED`, source hash `e7735d0cc36c3a10d032980b0db89f9f557e22f8575a8b4aa8b363c7a1ad390d`, 11 candidates, zero available candidates, and `poolComplete=false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67fa77fafcf7cb25dc6e8bc80eafd809443067aa3f87cd53d75459b9cfc2c4ce/400626f389be754179bbce46bd34a1ab8a8bb4917d397c411d6577bc2709af9b/probability-inspect-e7735d0cc36c.json`.

Evaluation over the named empty fixture set `IW057_FER_EMPTY_TYPED_BASELINE_2026_08_28` returned `PROBABILITY_ANALYZED_PARTIAL`, 132 candidate/scenario rows, 156 unresolved items, and 11 diagnostics; all eleven candidates were `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` under `{}` fixtures. This is instrumentation evidence only, not a live-campaign availability or balance result. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/929a6dc046e1abebf1312b56a9f8f1a761f6f49fc992ed61eb1fe1a81627fc38/e4982b8181159fa80d114590a36b4100fc0a9390ab2b9512d63d6f70ded72ca1/probability-4e7ce03561c4c8e1977991d3.json`.

The AI-strategy adapter returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces` and zero candidates, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7221bd9a3e7de9a72cb6a24d8d337301be1212203e9af29df4e5469b68cc500/24b551124c2b26919ea99059529ab89338d7ea64f88a21c2abb7dd5715e951a2/probability-inspect-c9a81863c89a.json`. This adapter limitation is not proof that the authored strategy blocks are safe or balanced.

The mandatory custom worker `chaosx_ai_probability_auditor` was not available in the callable tool inventory. A true owner-applied before/after probability compare, typed scenario sweep, and strategy-factor review therefore remain blocked.

## Validation performed

The following focused static validators passed against the current shared source:

- `python -B .tools/audit_event6_country_api.py`: broad 242 tags, 191 resolved carriers, 34 Soviet, 45 Africa, missing 0, duplicates 0, IW-031 crosswalk pass.
- `python -B .tools/audit_event6_allocator.py`: publishers 149, automatic/high-chaos 126, SCN-008 ranked 138, runtime adapters 40, attested 32, compatible groups 29, adapter-only fail-closed rows 8, reservation ladder and anchor-order checks passed.
- `python -B .tools/audit_event6_flags.py`: 102 registered Event 006 tags and 102 complete flag families.
- `python -B .tools/audit_event6_scenario_matrix.py`: all 32 SCN-008 cells and eight edge cases passed.
- `python -B .tools/audit_event6_gui_matrix.py`: Statehood Ledger semantic source matrix passed for its five tabs; no FER-specific GUI admission was inferred.

The required read-only focus, event, map, technology, and probability MCP routes were attempted. Focus and map render evidence is usable for their bounded structural views; event and technology calls are partial workspace projections; map inspection has global locator diagnostics; probability calls are empty-fixture/partial evidence. No HOI4 process was launched, and no live or save-load behavior is claimed.

## Changed files

Only this handoff was added by this audit:

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw057_fer_country_package_audit_2026-08-28.md`

No FER gameplay, central dispatch, character, portrait, flag, cosmetic tag, history, localisation, event, focus, decision, idea, AI, map, or technology file was changed. Existing concurrent edits elsewhere in the shared worktree were not reverted or overwritten.

## Remaining gates and blockers

FER may not be promoted until the parent/designated owners provide all of the following:

1. An accepted restored/revival or institution-backed 1936 identity interpretation and consistent role/date statement.
2. Independent rights acceptance and hydrated source bytes for the selected human candidate, or an explicitly accepted people-free institutional consumer.
3. A parent-owned Event 006 roster/character or institution receipt with correct portrait framing, gender metadata, and no opposite-gender name/portrait pairing.
4. An approved FER runtime flag/cosmetic identity and asset manifest, without reusing Event 005 FEV art or an unapproved fallback.
5. Current-map 408/409 rebinding and runtime ordered-anchor, former-host, protected-state, and collision receipts.
6. A mandatory typed probability audit through `chaosx_ai_probability_auditor`, including baseline and same-scenario compare before any AI-weight patch or admission claim.
7. Parent-reviewed central adapter, attestation, normal/SCN-008 preflight, setup/final-validation/cleanup dispatch, startup roster, and deterministic Join wiring only after the preceding receipts are complete.
8. Final runtime and save-load validation by the parent/user; this subagent did not and must not launch HOI4.

The installed Technology Tree Viewer limitation and global map locator diagnostics remain unresolved. No map write occurred, so no map rollback/recovery evidence exists or is required. No simplification, invented identity, unapproved fallback, or central-boundary widening was used.
