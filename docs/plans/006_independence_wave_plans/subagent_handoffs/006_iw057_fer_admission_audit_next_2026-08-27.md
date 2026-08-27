# IW-057 Far Eastern Republic admission audit — 2026-08-27

## Disposition

IW-057 Far Eastern Republic (FER, package `iw_057`, ordered anchors 408 Vladivostok and 409 Khabarovsk, reservation group `RG-408-409`) remains package-local and fail-closed.

No gameplay or central-admission source defect was found that is both directly proven and safe to patch in this bounded audit.

The current Event 006 boundary is unchanged at 32 content-attested selectable packages, 40 runtime adapters, 29 compatible reservation groups, and 161 unattested selectable rows out of 193 non-overlay rows.

## Authority and scope

This audit follows `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`, `docs/specs/006_independence_wave_specs/quality/package_manifest.md`, and the IW-057 research and hardening handoffs in this directory.

The required offline Paradox wiki pages, vanilla documentation, and relevant vanilla FER history, character, flag, and portrait references were read before source review.

The audit used the `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-comfyui` guidance. No portrait or flag fallback was created, and no RunPod operation was performed.

## Admission gate matrix

| Gate | Current status | Evidence and blocker |
| --- | --- | --- |
| Identity and tag | Blocked | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` defines IW-057 as FER, but `common/country_tags/chaosx_countries.txt` only registers the separate Event 005 FEV package. The package trigger is source-wired, while the identity-rights receipt and central tag/admission path are absent. |
| Territory and ordered anchor | Source-ready but runtime-unproven | Package source uses the ordered 408/409 contract and requires ownership/control plus a capital anchor. State 563 is dormant vanilla FER history only and is deliberately excluded from the Event 006 pre-release identity gate. Current map MCP inspection/render was blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED`. |
| Host survival and collision | Source guards present; admission blocked | Package triggers preserve a living former-host/remnant test and reject Soviet Collapse origins, but no central adapter, attestation, normal preflight, SCN-008 preflight, or deterministic Join row exists for IW-057. No current live transaction receipt proves collision safety. |
| Roster and leadership | Blocked | No Event 006 FER character or institutional roster is accepted. `FER_independence_wave_pyotr_nikiforov`, if selected, remains a research/source-placeholder proposal only; the roster and identity receipts are not set. |
| Portrait | Blocked | No FER Event 006 portrait-specific character/GFX/runtime DDS package exists. The research handoff names Pyotr M. Nikiforov as a rights-pending source-placeholder candidate. Event 005 FEV council art is not a valid FER substitute. |
| Flag and cosmetic identity | Blocked | No approved FER Event 006 neutral/runtime flag, cosmetic tag, or source receipt exists. The proposed `FER_INDEPENDENCE_WAVE_PROVISIONALX` must not be created before parent rights and identity acceptance. Vanilla ideology flags do not provide the missing Event 006 neutral identity receipt. |
| Politics and parties | Package-local source present; admission blocked | Four route installers, party names, ledgers, lifecycle ideas, and guarded setup/cleanup are present in the FER package. They remain gated by the unresolved identity and package-admission receipts. |
| Focus | Shared source present; MCP global pass | `independence_wave_focus_tree` has the FER helper callbacks and the current focus inspect/render resolved 184 focuses and 195 connectors with no Event 006 blocking diagnostic. The only reported warning is an unrelated vanilla continuous-focus localisation reference. |
| Decisions and ideas | Package-local source present; runtime admission blocked | One 420-day founding mission, ten serialized projects, seven FER ideas, cancellation guards, and cleanup are present. No central dispatcher or runtime admission row exposes them. |
| Forces and setup | Package-local source present; runtime-unproven | `regular_defectors`, p57, five reinforcement paths, and navy/air inheritance gates are source-wired. No live release/setup receipt exists, and the central dispatcher does not call FER setup/final-validation/cleanup. |
| Technology | No package-specific surface claimed; tooling unresolved | FER inherits vanilla history research and has no Event 006 technology tree. The installed package exposes no Technology Tree Viewer; current tech inspect/render also hit `ARTIFACT_MANIFEST_INTEGRITY_FAILED`. |
| AI and probability | Source present; not admissible | Four package AI strategy blocks exist, but `independence_wave_fer_settled_compact` lacks setup/current-generation guards. The weighted patch cannot be safely made without the mandatory baseline and same-scenario compare. Current typed mission evaluation is partial with empty fixtures and 155 unresolved rows. |
| Localisation and shared icons | Source coverage present | FER package localisation, shared Event 006 focus icons, and idea/decision icon references are present. This does not replace the missing flag, portrait, roster, or central admission receipts. |
| Central admission | Blocked | FER is absent from the central package adapter, content attestation, setup/final-validation/cleanup dispatch, normal preflight, SCN-008 preflight, startup registry, and deterministic Join. This absence is intentional fail-closed behavior under the current authority. |

## File surface checklist

| Surface | Current files and identifiers | Finding |
| --- | --- | --- |
| Candidate and binding | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`; `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` | IW-057/FER resolves to ordered alternatives `408|409`, names Vladivostok/Khabarovsk, and uses `RG-408-409`; it is not a cumulative anchor set. |
| Package triggers | `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt:11-252` | Identity, origin, anchor, host, project readiness, roster, force, route, prepared setup, complete setup, and cleanup guards exist. `is_independence_wave_exact_package_iw_057_tag_available` uses 408/409 and does not use dormant state 563. |
| Package effects | `common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt:1-497` | Politics, route effects, ideas, focus callbacks, force/AI setup, local roster checkpoint, validation, and cleanup are package-local. The roster checkpoint only records already-cleared parent receipts and does not create a leader. |
| Decisions | `common/decisions/006_independence_wave_far_eastern_decisions.txt` | `independence_wave_fer_hold_railway_council` plus the ten FER project decisions are present. All ten project cancellation triggers now include `NOT = { has_independence_wave_fer_anchor_owned = yes }`, confirming the 2026-08-25 ordered-anchor hardening. |
| Ideas and constants | `common/ideas/006_independence_wave_ideas_registry.txt`; `common/script_constants/006_independence_wave_constants_registry.txt` | Seven FER ideas and pressure, duration, cost, politics, force, and tradition constants are present. Existing modifier and duration values were not changed because that would be a balance change without typed comparison evidence. |
| AI | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:589-657` | Survival, host-restraint, settled-compact, and coastal-emergency profiles are source-wired. The settled-compact enable block lacks setup/current-generation guards and is a known weighted surface, not a safe local patch under the unavailable auditor/compare route. |
| Shared focus | `common/national_focus/006_independence_wave_focus.txt` | FER-specific callbacks are present in the shared tree; no bespoke FER tree is authorized by the current scope. |
| Region loader | `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt`; `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt` | Region planning can reserve/load FER package-local data, but planning availability is not central execution admission. |
| Localisation | `localisation/english/006_independence_wave_far_eastern_l_english.yml` | Package category, founding mission, projects, ideas, parties, tooltips, and effect text are present. No new visible identity key was added in this audit. |
| Registry and central dispatch | `history/general/006_independence_wave_character_recruitment_registry.txt`; `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`; `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`; `common/scripted_effects/006_independence_wave_join_effects.txt` | FER is intentionally absent from startup recruitment, adapter/attestation, dispatch, preflight, and Join. No central row was added. |
| Assets and character wiring | `gfx/flags/`, `common/characters/`, `interface/`, Event 005 FEV files | No approved FER Event 006 runtime flag, cosmetic tag, character, portrait GFX, portrait DDS, or manifest exists. Event 005 FEV assets remain separate and were not reused. |

## Map, state, host, and collision findings

The binding contract is two independent alternatives: 408/Vladivostok or 409/Khabarovsk, with the candidate retaining at least one 1936 state in either alternative and the former host retaining its protected remnant first.

`is_independence_wave_fer_project_ready`, `is_independence_wave_fer_runtime_ready`, `is_independence_wave_fer_setup_ready`, and all ten project cancellation blocks now require the ordered anchor ownership/control predicate. This supersedes the older pre-2026-08-25 note that lacked anchor-loss cancellation.

The vanilla FER country history uses capital 563/Chita, but 563 is a dormant comparison/history reference and is not an Event 006 runtime anchor. The current package source correctly keeps the release contract on 408/409.

The current `hoi4.map_inspect` and `hoi4.map_render` requests for states 408, 409, and 563 returned the exact blocker `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with the message “Artifact provenance manifest does not match its immutable address.” No map artifact, map write, allocation change, post-validation, or rollback evidence exists from this audit.

## Politics, roster, leader, portrait, flag, advisor, and party findings

FER has source-local baseline politics, four route government installers, four party-name sets, seven lifecycle ideas, and guarded restoration logic. These are not central admission evidence while the identity receipt is absent.

The proposed `FER_independence_wave_pyotr_nikiforov` character, `GFX_portrait_FER_independence_wave_pyotr_nikiforov` sprite, and `portrait_FER_independence_wave_pyotr_nikiforov` runtime basename remain design/research identifiers only. No character or portrait file was created.

The flag-source handoff records historical candidates H0/H1 and institutional/alternate-history options, but none is approved for runtime. No `FER_INDEPENDENCE_WAVE_PROVISIONALX` cosmetic tag or runtime flag was created.

No Event 006 FER advisor, high-command, commander, or institutional portrait package is authorized or present. No opposite-gender portrait/name issue was introduced because no FER portrait/leader consumer was added.

## Focus, decisions, ideas, and asset findings

The current shared focus MCP inspect returned `FOCUS_INSPECTED` and the render returned `FOCUS_RENDERED`; both resolved the shared Event 006 tree with no selected Event 006 blocker. Useful artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb255e65e6922a662a4117cfdc0e1151a033bb5a87b6e36b523d7555324a3dc0/a96838d016ce3d609f9859316171f8c101c8d35db4b1b7e69961eaa455e78ed8/focus-inspect.9887d2c9efb1cba6.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1387f679ebb46e99df9e4385f2d934232a98fdff7c3d1ee0a817d3b318cc0f0c/debf63a2f83054eab954bb7bed96e962c52d9881fd7180e2d053cef47dea706b/independence_wave_focus_tree.focus.html`.

The FER decision category, founding mission, ten projects, project serialization, cost/effect tooltips, and cancellation cleanup are source-present. The current mission probability source contains the exact eleven FER candidates and all are unavailable under the tool's empty campaign fixture, so no gameplay availability claim is made.

No new focus, decision, idea, flag, portrait, or other asset was produced. Existing shared icon references were not treated as evidence for the missing identity assets.

## Starting military, technology, industry, supply, and production findings

The package uses the source-mapped `regular_defectors` force profile at p57 with five reinforcement paths and inherited navy/air gates. It does not invent a separate FER army, equipment stockpile, technology tree, factory baseline, railway, port, supply network, or production fallback.

Vanilla FER history provides the dormant FEV-era country history at capital 563 with three research slots and starting tech/doctrines, but no Event 006 FER history or country shell is installed in the mod. The package does not claim that dormant history as an admitted runtime setup.

The current Technology MCP inspect/render requests both returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with the same immutable-address provenance message. The installed package has no Technology Tree Viewer, so no technology acceptance claim is made.

## AI, probability, and playability findings

The source AI profiles are `independence_wave_fer_railway_port_survival`, `independence_wave_fer_host_restraint`, `independence_wave_fer_settled_compact`, and `independence_wave_fer_coastal_emergency_guard`. The settled-compact profile is enabled by identity/package/compact state but does not also require package setup and current force generation; correcting that weighted surface requires the mandatory baseline and same-scenario probability comparison and was not safe while the required auditor route was unavailable.

The mission probability inspect used source `common/decisions/006_independence_wave_far_eastern_decisions.txt`, source hash `2131b4382b1d51515aa7327252949d86541c353d8f6e634217dc65f7ef849709`, and the eleven exact FER candidates. It returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, 11 candidates, 0 available candidates, 17 required inputs, and 0 unresolved source rows. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d321d23b0be4ed3664d8ecb5f27676147143d809f51f30c19e9935aa13d2ee9a/d7fbaa12e2079b1ea3d8cb2e8efb85d8d7cb05862c1f4ccbdc647007cdeee80f/probability-inspect-2131b4382b1d.json`.

The candidate IDs were `independence_wave_fer_hold_railway_council`, `independence_wave_fer_secure_railway_ports`, `independence_wave_fer_integrate_coastal_guards`, `independence_wave_fer_register_fer_communities`, `independence_wave_fer_settle_former_host_ledgers`, `independence_wave_fer_ratify_constitutional_autonomy`, `independence_wave_fer_adopt_railway_charter_compact`, `independence_wave_fer_convene_coastal_councils`, `independence_wave_fer_establish_coastal_emergency_command`, `independence_wave_fer_codify_durable_sovereignty`, and `independence_wave_fer_open_pacific_corridor`.

The named scenario set remains `IW057_FER_EMPTY_TYPED_BASELINE_2026_08_15` with scenario hash `2c89ce66f56c07b9eff850e73dfa77bb48ade645331729407c489850b53e1c58`. Evaluation across the 12 named scenarios with the empty `{}` fixture returned `PROBABILITY_ANALYZED_PARTIAL`, 132 candidate/scenario rows, 155 unresolved rows, and `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for all candidates under that empty fixture. This is an instrumentation result, not a valid campaign balance result. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65e02ef25160a3bc77041ce600dc4f4a2496ac35810a374a6eb16a83c03ccbfe/f6974ec49ce7ba2654e942e0c3ebe9146dab91bd3c3e3c7462e72dbbe74e281e/probability-205e61d7bbf6ad32f211468d.json`.

AI-strategy probability discovery returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`; this adapter response does not prove the static strategy blocks are safe or quantitatively balanced. The required `chaosx_ai_probability_auditor` is absent from the callable tool inventory, so no worker-mediated baseline/compare sign-off exists.

## Event and focus MCP evidence

The narrow Event 006 root inspection for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with status OK and zero selected blocking diagnostics. The read-only event render returned `EVENT_RENDERED_PARTIAL` with zero selected blocking diagnostics. Useful artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9bf23d701573bac86f105977a459bb0705579027f4f876cbbfdd53f7589f88d5/0dc5d2a6fcb677c1ff97bc296a234eab8f6305e2bdea00a4492d4da41e539f7c/event-scan-f4498b37c697.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f9a8382c23a63b7443f80df272cb5d3956526b47f2b7a481e7edd10f9575d03b/b0df8a36f5aa42042a74a9ee9c3c94a55f2c557b7a826143a93f74cf880ef1a0/event-overview-f4498b37c697-manifest.json`.

The focus inspect/render receipts are usable for shared-tree structure, but they do not establish FER admission, roster, asset, or live country behavior.

## Successor selection

No non-admitted successor currently meets the requested complete-evidence standard.

IW-045 Bashkiria (BSK) is the next package with a current source-backed promotion receipt, but it is already in the 32-package admitted set and therefore is not a next candidate for admission.

IW-048 Udmurtia and IW-050 Komi remain package-local and fail-closed with unresolved identity/portrait or source gates, central adapter/attestation/preflight/Join coverage, and typed probability/runtime evidence. IW-055 remains research-only/fail-closed, and the adapter-only IDs remain explicitly fail-closed in the current manifest.

The authoritative queue therefore continues IW-057 FER and IW-055 rather than promoting a partially evidenced successor. No central boundary was widened.

## Validation, changes, and remaining gates

Only this read-only audit handoff was written: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw057_fer_admission_audit_next_2026-08-27.md`.

No gameplay, map, central dispatch, tag, character, portrait, flag, localisation, AI, probability, spreadsheet, or registry file was changed.

Meaningful task-specific validation consists of the current Event and shared-focus MCP receipts, the package source gate review, the ordered-anchor hardening review, and the mission probability inspect/evaluate receipts listed above.

Skipped or blocked validation includes the custom country-package auditor, the custom probability auditor, live save/load and transaction validation, Technology Tree Viewer inspection, map post-validation, probability compare/sweep with typed fixtures, and live AI balance evaluation. The exact map/technology MCP blocker was `ARTIFACT_MANIFEST_INTEGRITY_FAILED`; the custom worker routes were absent from the installed callable tool inventory.

Remaining gates are parent-owned identity and rights clearance, an accepted FER roster/institution and portrait package, an approved neutral/runtime flag and cosmetic identity, central adapter/attestation/preflight/Join/dispatch wiring, live ordered-anchor and host-remnant receipts, complete typed probability scenarios and auditor compare, and final runtime validation.

No simplification or unapproved fallback was used. FER remains fail-closed, and no source patch is recommended from this audit.
