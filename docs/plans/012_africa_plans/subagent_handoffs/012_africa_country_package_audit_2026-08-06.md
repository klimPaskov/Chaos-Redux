# Event 012 Africa country-package audit — 2026-08-06

Status: read-only country-package audit. No gameplay, map, asset, localisation, or AI files were changed by this audit. The only changed file is this handoff.

## Scope and source of truth

This audit covers the sixteen priority-member packages in `docs/specs/012_africa_specs/specs/012_africa_spec_part_9_priority_member_country_packages.md` and the Tier A package requirements in `docs/specs/012_africa_specs/specs/012_africa_spec_part_4_country_packages_formables.md`. The source-of-truth implementation is the current repository state; older 2026-08-01 and 2026-08-03 handoffs are treated as historical evidence where they disagree with current files.

Required offline Paradox wiki pages and the relevant vanilla documentation were consulted for country, state, focus, event, decision, idea, AI, technology, map, and character syntax. Vanilla state and country history files were used to confirm the existing carrier tags and core-state precedents.

## Coverage checklist

| Surface | Result | Evidence and caveat |
|---|---|---|
| New country tags | Pass | No Event 012 country-tag file exists. Event 006 owns the seven niche tags (`DOX`, `DSX`, `DUX`, `DYX`, `DZX`, `EMX`, `EQX`); the other nine packages use existing vanilla carriers. The country-tag audit reports 136 protected Event 006/Soviet tags, zero external definition collisions, and zero external identity-surface collisions. |
| Carrier mapping | Pass with dormant rows | All sixteen origin predicates and direct-carrier predicates exist. `DYX`, `DZX`, and `EMX` are intentionally disabled until a unique current state is installed. |
| Host preservation | Pass in current source | `africa_priority_member_focus_surface_is_protected` and the priority loader preserve an existing Event 006/Soviet tree and set the overlay-skip flag. This supersedes the stale 2026-08-03 handoff wording that claimed unconditional direct loading. |
| Registration/promotion | Present, runtime-gated | `africa_priority_member_can_register_package` requires the active event, completed host commit, promotion approval, a valid origin, supported carrier identity, a viable compact base, and no stale active package. `africa_priority_member_can_be_promoted` requires the confidence criteria and minimum support threshold. The dormant map rows cannot pass the viable-state gate. |
| Package mechanics | 16/16 | Each package has a distinct mechanic flag and package-specific scripted-effect branch. |
| Force payloads | 16/16 | Each package has a force payload, a named guard template, a primary guard, and a reserve path through the shared elephant unit bridge. |
| League roles and refusal | 16/16 | Each package has a distinct preferred clause, League decision path, refusal/counterproposal handling, overlap settlement, and post-settlement action. |
| Leaders, parties, and localisation | 16/16 structural coverage | Sixteen character IDs, male metadata, stable portrait sprite keys, three party-name variants per package, sovereign descriptions, and lifecycle idea strings are present. Provenance/actor eligibility remains open for source-locked portraits. |
| Focus surface | Present, intentionally shared | The shared eight-focus package-aware overlay is loaded only on safe surfaces; the current tree is MCP-clean. It has no branch nodes, so package depth is delivered through effects, decisions, and localisation rather than sixteen separate trees. |
| Decisions and ideas | 16/16 package branches | Shared registration/politics/League/overlap/departure decisions plus sixteen mechanic, force, and post-settlement decisions are present. Each package has distinct lifecycle ideas and icons. |
| Flags and visual assets | Structural pass | Niche carriers have existing flag assets; vanilla carriers use vanilla flags. All Event 012 priority focus/idea/decision/report texture paths resolve in the registered GFX. |
| South Africa Allied branch | Pass in source | The SAF Allied route snapshots the pre-war host, starts a deterministic civil war, tracks interveners, resolves the continental or loyalist victory, and uses peace/settlement callbacks without forced annexation. |
| Dormant fictional identities | Pass | `012_africa_fictional_characters.txt` contains six dormant male characters and no country tags, party assignment, leader registration, or package-carrier linkage. |

## Sixteen-package carrier matrix

The table records the current carrier, map readiness, distinct mechanic, force profile, and League identity. “No unique current state” is intentional ledger state, not an unreviewed tag collision.

| Package | Carrier | Current state evidence | Distinct mechanic | Force profile | League clause |
|---|---|---|---|---|---|
| Asante | `DOX` | 274; Event 006 niche shell, ready in high-chaos ledger | Stool-council legitimacy | Royal guard | Stool council and autonomy |
| Oyo | `DSX` | 558; Event 006 niche shell, ready in high-chaos ledger | Corridor-city compact | Mobile guard | Corridor and city compact |
| Sokoto | `SOK` | 902 current split; existing vanilla carrier | Emirate jurisdiction/reform | Mobile guard | Emirate jurisdiction and reform |
| Kanem-Bornu | `DUX` | 901 rebound state; Event 006 niche shell, ready in high-chaos ledger | Lake/caravan covenant | Mobile guard | Lake and caravan covenant |
| Manden | `MLI` | 556, 782, 898, 899; existing vanilla carrier | Assembly legitimacy | Mobile guard | Assembly and corridor guarantee |
| Kongo | `COG` | 295, 538, 718, 768, 769 confirmed by MCP; 888–890 confirmed in vanilla state files | Cross-border consent | River guard | Cultural citizenship separate from territory |
| Buganda | `UGA` | 548; existing vanilla carrier | Kingdom federal balance | Royal guard | Kingdom federal balance |
| Aksum | `TIG` | 842; existing vanilla carrier | Heritage consent | Highland guard | Heritage without annexation |
| Harar | `HAR` | 835; existing vanilla carrier | Corridor guarantees | Mobile guard | Corridor non-monopoly |
| Kilwa | `EMX` | No unique current state; intentionally dormant Event 006 shell | Common customs | Coastal guard | Distributed customs and patrols |
| Nubia | `SUD` | 549, 551, 883–887 confirmed by MCP; additional SUD cores in vanilla history | River rights | Mobile guard | Dual river recognition |
| Luba | `DYX` | No unique current state; intentionally dormant Event 006 shell | Mining revenue/local consent | River guard | Mining revenue and local consent |
| Lunda | `DZX` | No unique current state; intentionally dormant Event 006 shell | Cross-border access | Mobile guard | Cross-border access and citizenship |
| Great Zimbabwe | `ZIM` | 545; existing vanilla carrier | Restoration mandate | Highland guard | Bounded restoration mandate |
| Merina | `MAD` | 543, 706, 708; existing vanilla carrier | Asymmetric island federalism | Coastal guard | Asymmetric island federalism |
| Zulu | `EQX` | 719; Event 006 niche shell, ready in current-map ledger | Crown/land/labour balance | Mobile guard | Crown, land, and labour balance |

## File-surface checklist

| Surface | Files and identifiers reviewed | Finding |
|---|---|---|
| Tag registration and carrier identity | `common/country_tags/006_independence_wave_countries.txt`; `common/countries/006_independence_wave_{DOX,DSX,DUX,DYX,DZX,EMX,EQX}.txt`; `common/countries/012_africa_cosmetic.txt`; `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` | Existing niche shells and vanilla carriers are consistently mapped. `012_africa_cosmetic.txt` contains host/cosmetic identities only; it does not redeclare the sixteen priority members. |
| Origin and registration triggers | `common/scripted_triggers/012_africa_priority_member_triggers.txt` | Sixteen origin predicates, direct niche/vanilla carrier gates, promotion confidence gate, viable compact-base gate, and terminal cleanup guards are present. |
| Focus loading | `common/scripted_effects/012_africa_priority_member_effects.txt`; `common/national_focus/012_africa_priority_member_focus.txt`; focus IDs `africa_priority_define_compact_country` through `africa_priority_write_post_settlement_programme` | Current source preserves protected Event 006/Soviet trees and loads the shared tree only on safe surfaces. |
| Events | `events/012_africa_priority_member_events.txt`; hidden recruitment `africa_priority_member.1240`; visible events `.1200`, `.1210`, `.1220`, `.1230` | Each visible event contains sixteen package trigger references. Narrow MCP lint of `africa_priority_member.1200` returned no blocking diagnostics; global helper projection remained deferred. |
| Characters and party wiring | `common/characters/012_africa_priority_member_characters.txt`; `common/scripted_effects/012_africa_priority_member_character_effects.txt`; `localisation/english/012_africa_priority_member_characters_l_english.yml` | Sixteen character IDs, three political outcomes, male metadata, party keys, sovereign descriptions, and prior-leader preservation are wired. No package-specific advisor/high-command entries were found. |
| Portrait runtime | `interface/012_africa_priority_member_characters.gfx`; `gfx/leaders/012_africa/priority_members`; `docs/assets/portraits/012_africa/source_locked_runtime_mapping.md` | All sixteen runtime keys point to 156x210 `_source_locked.dds` files. Unreferenced base Aksum, Merina, and Nubia files are 210x156 and should not be silently promoted or deleted. |
| Lifecycle ideas | `common/ideas/012_africa_priority_member_ideas.txt` | Sixteen distinct starting/mature pairs and three shared settlement ideas; clear-before-phase-change effect is present. |
| Decisions/missions | `common/decisions/012_africa_priority_member_decisions.txt` | Shared lifecycle decisions plus sixteen mechanic, force, and post-settlement decision branches; withdrawal mission and recall paths exist. |
| Forces and technology | `common/scripted_effects/012_africa_priority_member_force_effects.txt`; `common/scripted_effects/012_africa_elephant_effects.txt`; `common/technologies/012_africa_elephant_technologies.txt` | Idempotent guard/reserve generation and package-specific reinforcement are present. The elephant technology is a hidden direct-grant bridge, not a research-tree node. |
| Icons and GFX | `interface/012_africa_priority_member_assets.gfx`; `gfx/interface/goals/012_africa/priority_members`; `gfx/interface/ideas/012_africa/priority_members`; `gfx/interface/decisions/012_africa/priority_members`; `gfx/event_pictures/012_africa/priority_members` | Eight focus, thirty-five idea, fifty-six decision, and four event-report assets are registered; texture path scan found no missing referenced files. |
| RSA Allied lifecycle | `common/scripted_triggers/012_africa_rsa_triggers.txt`; `common/scripted_effects/012_africa_rsa_effects.txt`; `events/012_african_union.txt`; `common/on_actions/012_africa_rsa_on_actions.txt` | Allied eligibility requires SAF/original SAF plus explicit ENG faction evidence. Civil-war, intervening-war, victory, peace, cleanup, and event-log paths are present. |

## MCP evidence and limitations

The mandatory read-only MCP routes were used for the country-linked focus, event, map, and technology surfaces.

* Focus inspect of `common/national_focus/012_africa_priority_member_focus.txt` returned `FOCUS_INSPECTED` at revision `9f1b670d365569e5`. The priority tree has eight focuses, zero branches, resolved localisation for all eight nodes, clean bounds, zero crossing/overlap/long-connector diagnostics, and layout hash `045689563a44e3b12d452e03ce01f575d98b0ea3ac5b0d571c4b709d1a47c4c8`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b4a7d7988d202f4586b81f9c7583118980c80bd815a2fea79f01d202facccdf/56b961fd1c9cbf983fa689dbe5c34157958ffc637ff65bc90006f652ef01fed8/focus-inspect.9f1b670d365569e5.json`.
* Focus render returned `FOCUS_RENDERED`; the useful artifacts are `africa_priority_member_focus_tree.focus.html` (SHA `66ada9871bf54db42500c8cf562c119abf14b6fba9fb0e3952423099433c4c70`), `.focus.svg` (SHA `64ff52a12478e69cad0499d65a5470c2bc87e68bee5df574218e0b4356cafda6`), and `.focus.json` (SHA `6053a253582469c2380168292113bb8d286eb4272a9449d7dbf3c28ee024d751`).
* Map inspect of the twenty-eight explicit package dependency state IDs returned `MAP_INSPECTED` at revision `02d1d4f1800e7bfd`. Queried state IDs and definitions resolved, and state/region membership, networks, adjacencies, supply, and railways passed. Global map validation is false because the workspace still reports 2,657 `MAP_PORT_ADJACENT_SEA_INVALID` and 1,324 `MAP_BUILDING_POSITION_INVALID` diagnostics for unrelated floating positions/buildings; these were not attributed to the package states. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1b1e4ab06f75cb879619c05c879615b69b79e8afab7d0ca106a757b7bf479ac/949991491507869664991973d4c5018c8b032fa1eeef8dfee5ad7bd40b59be2e/map-inspect.02d1d4f1800e7bfd.json`.
* Event scan of `events/012_africa_priority_member_events.txt` returned `EVENT_INSPECTED_PARTIAL` at revision `e95cc5f8ce60d44bb8a4775ab5277cf015ee24921d1bb876e9e2dbbdcb02b551`; the narrow `africa_priority_member.1200` lint also had no blocking diagnostics. The partial/global status reflects deferred helper projections, not a package event blocker. Scan artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6404443b7cb5c8cb9dc939d0bcdccbfcffa5f92e7dc30e70a9551ab5d84df6af/33c8c85a10bf1b51426661183c785825b236113aa5af7f3a975c7ac2931916f0/event-scan-e95cc5f8ce60.json`; narrow lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39ee9e7b45ad319f38575205bbbbda32034dae07345ecbef706a6a6b0a18eb29/709fbd9674ac9c3836ba48f55e0e9507489423cc9676b022e8d6f6a0bdf057e9/event-lint-e95cc5f8ce60.json`.
* Technology inspect of `chaosx_africa_elephant_warfare_tech` returned `TECH_INSPECTED_PARTIAL` at revision `9139884746eb8fcfdc7bc836c072adb8a06517d54539c7f4a292609e6a57b233`, with no technology-specific blocker. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d59c033dc6ebadcf0ef78478f9516fafb9b4dca8d5c67dcc53c3d72e214953a8/b74090db6dee6882e63d82d0b7391769509467ecc8aabcf5752a61e64ef5f377/technology-scan-9139884746eb.json`. The installed package exposes no Technology Tree Viewer, so no tree-viewer evidence can be supplied; this remains an unresolved tooling limitation.
* The focus, event, map, and technology MCP workspace-level validation flags remain false/partial where the diagnostics are global or helper projections are deferred. Source review and the package-scoped findings above should not be represented as a clean whole-workspace validation.

## Politics, leaders, portraits, flags, advisors, and parties

The political package has three explicit settlement outcomes per sovereign role: council/civic, producer, and democratic/liberal. Party names and long names are supplied for all sixteen packages (forty-eight short and forty-eight long keys), and the character effect preserves the prior host leader while installing one package sovereign after settlement.

There is no opposite-gender portrait/name pairing: all sixteen runtime characters are explicitly male and use male name metadata. However, portrait acceptance is not closed. The `_source_locked` DDS files are runtime source placeholders, and the runtime approval trigger admits all sixteen packages independently of source, rights, and actor review. Aksum/Ezana, Nubia/Taharqa, and Merina/Radama II are ancient or date-misaligned actors for a 1936-style runtime, while several source maps/artifacts are not human likenesses. The portrait worker or parent must decide whether those identities remain accepted, receive a sourced replacement, or stay explicitly placeholder. This is a provenance/actor-eligibility blocker, not a path or gender metadata defect.

No package-specific advisors or high-command entries were found in the character or decision surfaces. The current specification concentrates the package identity in the sovereign, council/party outcomes, lifecycle ideas, decisions, and force payloads, so this is an acceptance gap to review rather than a safe narrow patch.

Niche tags have their existing Event 006 flag assets; the nine vanilla carriers use vanilla flags. No Event 012 cosmetic tag or missing registered flag was found.

## Focus, decisions, ideas, and assets

The shared focus overlay is deliberately package-aware rather than sixteen copied trees. Its eight focuses are mechanically distinct through sixteen package branches in scripted effects, decisions, ideas, force payloads, and dynamic localisation. This keeps the host's protected focus tree intact, but the zero-branch layout is a design risk if acceptance requires a bespoke route layout for every sovereign.

The current loader behavior is authoritative: a protected Event 006/Soviet surface receives `africa_priority_member_focus_tree_overlay_skipped = yes` and keeps its creating tree; a safe direct/generic surface loads `africa_priority_member_focus_tree`. The 2026-08-03 direct-load handoff is stale and should not be used to infer runtime behavior.

All package-specific idea, focus, decision, and report-picture texture paths referenced by `interface/012_africa_priority_member_assets.gfx` resolve. No new package-specific advisor icon family is required by the current implementation.

## Starting military, technology, industry, supply, and production

The package does not rewrite every host's start-of-game order of battle. When a package is active, `initialize_starting_force` is idempotent, requires an owned and controlled African state, and avoids duplicate divisions; guard and reserve payloads then reinforce from local support. Five force profiles cover all sixteen packages and use the shared elephant entity/equipment bridge.

The only package technology is `chaosx_africa_elephant_warfare_tech`, a hidden `allow = { always = no }` bridge granted directly by `africa_elephant_unlock_warfare`; it grants the custom equipment and battalion and has zero AI research weight. There is no package-specific research tree or production-line bootstrap. Economic payloads add the package's distinct capital/project infrastructure, dockyard, industrial, transport, or arms-factory effect as applicable. State ownership, capital, control, port, supply, and railway viability are guarded by the compact-base trigger rather than by a new map rewrite.

## AI and playability

The shared focus tree has package-group AI modifiers, and all package-specific decisions have AI weights sourced from the Event 012 constants. The existing `common/ai_strategy/006_independence_wave_iw093_iw098_ai_strategy.txt` only covers Event 006 DOX/SOK production/route pressure. No Event 012-specific production or strategic-plan file covering all sixteen packages was found. This is a playability and balance gap for the parent AI/probability audit; no probability-bearing patch was made here and no duplicate probability agent was spawned.

The three dormant carriers (`DYX`, `DZX`, `EMX`) cannot currently be promoted because their ledger rows have no unique current state. The other carriers have either current vanilla states or the existing Event 006 niche state bindings listed above. The compact-base trigger rejects capitulated, uncontrolled, non-African, or stale-host situations, which protects against invalid starting setup but may reject edge-case restoration scenarios that need explicit parent design.

## South Africa Allied civil-war and settlement review

The Allied route in `events/012_african_union.txt` dispatches only when the current and original tag are `SAF`, no civil war is already active, host gates are valid, and England faction evidence is present. `africa_rsa_start_allied_civil_war` snapshots capital, faction leader, autonomy, popularity, enemies, patrons, and ratios, then starts a deterministic civil war across the declared South African state filter. The Allied Union government receives its cosmetic identity while host flags and prior faction context are preserved or explicitly cleared.

`common/on_actions/012_africa_rsa_on_actions.txt` records intervention relations and invokes victory preparation/resolution on civil-war end. The continental and loyalist paths white-peace/truce intervention wars, restore the original capital, clear the civil-war flag, set settlement state, and clean global targets. Settlement events `.1204`, `.1205`, `.1206`, and `.1208` handle Cape Convention, loyalist suppression, exile, and no-patron outcomes without forced annexation. This satisfies the requested SAF Allies civil-war/peace-settlement dependency at source level.

## Missing, stale, or unresolved surfaces

1. Portrait source/rights/actor review remains open for the source-locked runtime set, especially ancient/date-misaligned names and artifact/map placeholders. The runtime approval trigger currently does not encode that review.
2. No package-specific advisor/high-command roster exists; parent should confirm whether the sovereign/council design intentionally replaces those roles.
3. No Event 012 strategic AI plan covers all sixteen packages; focus/decision AI is present, but production and diplomacy behavior needs the separate probability/AI audit.
4. `DYX`, `DZX`, and `EMX` remain dormant with no unique current state by design. They are not runtime-ready restoration packages until an approved map binding exists.
5. The shared focus has zero branch nodes. Package-specific scripted effects and decisions provide differentiation, but a requirement for visible bespoke branches would need a design handoff, not a narrow patch.
6. MCP whole-workspace validation is affected by unrelated port/building position diagnostics, and event/technology inspections remain partial because helper projections are deferred. These are evidence limitations, not package-local failures.
7. The installed toolset has no Technology Tree Viewer, so the required viewer comparison cannot be performed.

## Changed files and validation

Changed files: `docs/plans/012_africa_plans/subagent_handoffs/012_africa_country_package_audit_2026-08-06.md` only. No tags, states, leaders, parties, focus IDs, localisation keys, formables, map data, AI weights, or runtime assets were patched.

Meaningful checks completed:

* `.tools/audit_chaosx_country_tags.py` reported zero external country-definition or identity-surface collisions.
* Source scans verified sixteen package origin predicates, sixteen mechanic branches, sixteen force branches, sixteen League clause/refusal/post-settlement paths, sixteen character IDs, and the absence of package-linked dormant fictional tags.
* MCP focus inspect/render, event inspect/lint, map inspect, and technology inspect were run as documented above.
* Vanilla state-history scans confirmed the existing `SOK`, `MLI`, `COG`, `UGA`, `TIG`, `HAR`, `SUD`, `ZIM`, and `MAD` carrier precedents.
* GFX texture-path scan found no missing referenced Event 012 priority assets; runtime portrait DDS dimensions were checked for all sixteen `_source_locked` files.

Skipped checks: no live Hearts of Iron IV launch or save-game validation was performed, because live consumer testing belongs to the parent/user. No `hoi4.map_rewrite`, `hoi4.focus_rewrite`, or gameplay patch was appropriate for the read-only audit.

## Parent review actions

Please treat this handoff as an actionable audit, not a full Event 012 completion claim. The parent should reconcile the stale direct-focus handoff, route the portrait source/rights/actor decisions to `chaosx_portrait_creator`, obtain the separate probability/AI comparison for all weighted surfaces, and decide whether the advisor gap and zero-branch shared focus are accepted design choices. Any request to activate `DYX`, `DZX`, or `EMX` needs an approved current-map binding and a separate map review before implementation.
