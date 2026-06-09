# Event006 Source Of Truth Map

Date: 2026-06-08
Scope: Event006 Independence Wave documentation, specs, plans, handoffs, and docs asset manifests.

This map tells the next parent agent which Event006 documents to trust first. It is documentation-only and does not claim Event006 completion.

## Current Non-Negotiable Corrections

| Subject | Current rule |
| --- | --- |
| Country direction | The active base wave should not hardcode releasable tags. It uses the generic possible-country pool first. Niche generic, custom, and chaos-only countries can be added later through a separate explicit pool when their cores, flags, localisation, and playability package are intentionally wired. |
| Shared tree | Countries released by Event006 use `independence_wave_liberation_provisional_tree`. The shared tree must stay generic for Independence Wave releases; package identity belongs in decisions, missions, ideas, route state, event details, and localisation unless a later request explicitly promotes a bespoke tree. |
| African story mechanics | Current African custom releases keep the shared tree but have distinct story decisions, spirits, claim routes, and leader hooks. `ASN` uses the Asante Stool Court, `KBN` uses the Kanem-Bornu Caravan Court, `DFR` uses the Acacia Frontier Pact, and `ZUL` uses the Lion Crown plus the Gorilla Chair strange-story path. |
| Custom flags | `ASN`, `KBN`, `DFR`, `ZUL`, `PLM`, `AYM`, and `MAP` use imagegen-regenerated unique flags documented in `docs/assets/006_independence_wave/flags/manifest.md`. |
| Candidate pool | The active release pass uses one generic `every_possible_country` scan. Any inactive possible country can enter the base pool. The later host-safety resolver decides whether it actually has a valid host-owned, controlled, non-protected core state that can be released without erasing the host. Custom and chaos-only countries should be added later through a separate explicit pool instead of hardcoding every releasable tag into the base pass. |
| Actor rule | The base Independence Wave has no responsible country actor. The event recipient, manual trigger country, and first host that lost land must not be written as the event-history actor or release-scale evolution actor. |
| KUB and ALT | Kuban (`KUB`) and Altai (`ALT`) package-expansion framing is superseded. Do not expand them, add KUB/ALT assets, or treat their old package handoffs as current source-of-truth scope unless the user explicitly reopens them. They are vanilla releasable tags and may enter the ordinary Independence Wave candidate pool when they pass the same inactive possible-country and host-safety checks as other vanilla candidates. They must not receive package-specific Event006 overlays unless explicitly reopened. |
| Event005 separation | Event006 is independent from Event005 Soviet Collapse. Shared tags may overlap, but focus loading, decisions, AI, event logs, achievements, and package logic must follow release origin. |
| Release timing | Event006 waves release valid countries immediately after hidden resolver checks. Dossiers, boards, decisions, GUI, recognition, patronage, and border work are aftermath systems, not pre-release waiting rooms. |
| Host survival | Event006 must never erase the host. Every wave must preserve at least one host-owned state, preferably the capital when valid. |
| Evolutions | Evolution logs are a few real release-scale tier milestones. Baseline/calm waves are not normal evolution entries. Current milestone names are Dossier Surge, Rising Chaos Release Pattern, Chaos Tier Release Pattern, Great Partition Week, and Open Season. Great Partition Week displays at Chaos Tier, while Open Season is the World Collapse-stage entry displayed at Totalen Chaos. Individual releases, package route steps, formations, and ordinary progression should not spam evolution rows. |
| Completion status | Current wrap-up target is technical playability and honest documentation alignment. Event006 is not fully complete. |

## Highest Authority

| Source | Use for | Notes |
| --- | --- | --- |
| `AGENTS.md` | Repository rules, no-fallback policy, required HOI4 references, validation and completion standards. | Always applies. |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | Documentation-curator boundaries, handoff requirements, plan/spec folder rules. | Documentation curator may patch docs only. |
| `.agents/skills/chaos-redux-events/SKILL.md` | Event contract, evolution rules, event-log/detail expectations, spreadsheet/documentation alignment. | Use for Event006 docs even when gameplay is out of scope. |
| `docs/plans/006_independence_wave_plans/source_of_truth_map.md` | Current routing map, dispositions, contradictions, and active docs status. | This file. |

## Current Source Docs

| Source | Current use | Caveat |
| --- | --- | --- |
| `docs/events/006_independence_wave.md` | Compact current event overview, runtime behavior summary, event-log/evolution policy, Event005 separation, asset needs, and incomplete/future-work list. | Summary only. Do not treat as a full completion report. |
| `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md` | Main source design for identity, instant release, host survival, candidate ladder, evolution scale, decisions, AI, achievements, and final closure standard. | Some candidate examples remain aspirational; use current correction above before implementing packages. |
| `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md` | Package ladder, ordinary/generic release policy, current niche lane, blocked/queued packages, implemented package notes. | KUB/ALT rows are historical candidate notes only. |
| `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md` | Shared Liberation Provisional Tree architecture and package-overlay rules. | Current niche generic releases should share the tree, not receive bespoke overlays. |
| `docs/specs/006_independence_wave_specs/006_independence_wave_decisions_ai.md` | Decision category and AI design rules. | Read through the current instant-release and Event005-separation corrections. |
| `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md` | Asset workflow and sprite-name expectations. | Current report/news asset blocker is closed; future route-specific visuals are optional polish unless reopened. |
| `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md` | Super-event candidates, text/image/audio needs, and escalation role. | Only trust candidates whose gameplay unlock conditions are implemented or explicitly queued. |
| `docs/specs/006_independence_wave_specs/006_independence_wave_achievements_prompt.md` | Achievement design and icon prompt alignment. | Final achievement/catalog parity still needs audit after implementation stabilizes. |
| `docs/specs/006_independence_wave_specs/006_independence_wave_catalog_update.md` | Catalog/spreadsheet wording target. | Workbook edits are outside documentation-curator scope and may lag implementation facts. |
| `docs/specs/006_independence_wave_specs/006_independence_wave_research_notes.md` | Background candidate research. | Research notes do not override the current package lane or no-fallback rule. |
| `docs/specs/006_independence_wave_specs/006_independence_wave_goal_prompt.txt` and prompt files | Original task prompts and production briefs. | Historical inputs, not current completion proof. |

## Current Working Plans

| Source | Current disposition |
| --- | --- |
| `006_independence_wave_instant_release_correction_handoff.md` | Current rule: releases are immediate, dossiers are aftermath. |
| `006_independence_wave_event005_separation_handoff.md` | Current rule: Event006 origin gates must block Event005 mechanics. |
| `006_independence_wave_foundation_tranche_handoff.md` | Historical foundation evidence. Its per-release evolution wording is superseded by release-scale tier milestones. |
| `006_independence_wave_improvement_addendum_post_focus_formation_tranche.md` | Closed as a broad implementation plan. Implemented parts are preserved; remaining work is queued. Do not spawn another broad improvement-loop planner until queued work is handled or narrowed. |
| `006_independence_wave_improvement_loop_gate.md` | Still useful as a gate against shallow repeated expansion. |
| `006_independence_wave_subagent_deployment_plan.md` | Historical/current routing aid for subagent use. Source specs and this map have higher priority for current Event006 scope. |

## Recent Handoffs To Trust For Current State

| Source | Trust for | Notes |
| --- | --- | --- |
| `subagent_handoffs/2026_06_05_parent_event006_playable_wrapup_handoff.md` | Historical technical playability wrap-up: full candidate pool scan, release-scale evolution entries, no Calm World evolution entry, targeted tooltip tranche, no final completion claim. Superseded on final count by the five-stage Dossier Surge to Open Season ladder. | Parent handoff; docs-only curator did not verify runtime in game. |
| `subagent_handoffs/2026_06_05_parent_event006_audit_followup_runtime_cleanup.md` | Follow-up after the 17:00 completion audit: removed stale KUB/ALT AI/idea surfaces, changed release truce duration to a parser-safer file constant, and preserved generic release expansion/army support. | Runtime cleanup evidence; spreadsheet parity still remains separate. |
| `subagent_handoffs/2026_06_05_parent_event006_event005_origin_separation_audit.md` | Parent audit of Event005-side origin separation after the 17:00 completion audit. | Found guarded setup/focus-loader helpers and high-chaos spawn triggers requiring target tags not to exist, so no extra patch was made. |
| `subagent_handoffs/2026_06_05_161512_parent_event006_playable_wrapup_urgent_fixes.md` | Historical urgent KUB/ALT candidate exclusion, Event005 setup guard for Event006-origin countries, and four-entry evolution log validation. | KUB/ALT candidate exclusion is superseded; use the current non-negotiable corrections above. |
| `subagent_handoffs/2026_06_05_153901_parent_event006_candidate_pool_resolver_fix.md` | Historical candidate-pool resolver fix after no-release manual firing risk. | Superseded where it describes hardcoded package seed calls in the active base pass. |
| `subagent_handoffs/2026_06_05_152724_parent_event006_kub_alt_and_log_mapping_fix.md` | Gameplay-side KUB/ALT cutback and evolution log mapping cleanup. | Notes that unused KUB/ALT helpers remain for parser stability. |
| `subagent_handoffs/2026_06_05_145208_parent_event006_custom_generic_release_tranche.md` | Historical `ASN`, `KBN`, `PLM`, `AYM` generic niche release lane. | Superseded for active release-pool behavior. Reintroduce through a separate custom pool later if desired. |
| `subagent_handoffs/2026_06_05_144741_event006_niche_country_flag_asset_handoff.md` | Historical niche-country flag asset package for `ASN`, `KBN`, `PLM`, and `AYM`. | Asset evidence only; not proof that these tags are in the active base pool. |
| `subagent_handoffs/2026_06_05_175813_event006_mapuche_flag_asset_handoff.md` | Historical MAP flag asset package. | Asset evidence only; MAP needs a separate custom pool before it can enter the active release pass. |
| `subagent_handoffs/2026_06_05_parent_event006_peripheral_host_release_gate.md` | Peripheral host pressure gate and release eligibility context. | Useful for origin and host-survival docs. |
| `subagent_handoffs/2026_06_05_155247_decision_tooltip_cleanup.md` | Targeted decision tooltip cleanup. | KUB/ALT tooltip wrappers were applied only because old blocks existed; no scope expansion. |
| `subagent_handoffs/2026_06_05_160045_documentation_curator_wrapup_cleanup.md` | Prior docs cleanup for playable wrap-up, report/news blocker correction, and evolution tier wording. | Superseded as latest curator handoff by the broad cleanup handoff created with this map, but still valid for scoped notes. |
| `subagent_handoffs/2026_06_05_152010_documentation_curator_kub_alt_correction.md` | Narrow KUB/ALT documentation correction and validation. | Superseded as latest curator handoff by the broad cleanup handoff, but still valid for its scoped correction. |

## Asset Manifest Disposition

| Source | Current use |
| --- | --- |
| `docs/assets/006_independence_wave/flags/manifest.md` | Historical manifest for the generic niche flag lane: `ASN`, `KBN`, `PLM`, `AYM`. |
| `docs/assets/006_independence_wave/flags/mapuche/manifest.md` | Historical manifest for custom MAP Mapuche Land Congress flag assets. |
| `docs/assets/006_independence_wave/report_event_images/manifest.md` and `news_event_images/manifest.md` | Current report/news image manifest set. The old missing-GFX blocker is closed; future variants are optional polish. |
| `docs/assets/006_independence_wave/focus_icons/manifest.md`, `decision_icons/manifest.md`, `decision_category_icons/manifest.md`, `idea_icons/manifest.md`, `achievement_icons/manifest.md` | Current reusable Event006 visual families and achievement icon packages. |
| `docs/assets/006_independence_wave/super_events/*/manifest.md` | Current or historical super-event asset packages by super-event. Trust only alongside implemented unlocks in the event doc and recent handoffs. |
| `docs/assets/006_independence_wave/flags/darfur/manifest.md` and `flags/zulu/manifest.md` | Specific DFR/ZUL flag manifests. They are package/tag asset records, not general package-completion proof. |

## Superseded Current-State Claims

| Source or claim | Current resolution |
| --- | --- |
| `subagent_handoffs/2026_06_04_145232_parent_event006_kuban_package_handoff.md` | Superseded historical tranche. Do not use as current package scope. |
| `subagent_handoffs/2026_06_04_151704_parent_event006_altai_package_handoff.md` | Superseded historical tranche. Do not use as current package scope. |
| `subagent_handoffs/2026_06_05_142822_parent_event006_catalog_125_focus_alignment.md` | Partially superseded where it treats Kuban or Altai as current package/focus summaries. |
| Older wording that every release, package step, or formation should write an evolution row | Superseded. Evolution logs are release-scale tier milestones only. |
| Older report/news asset missing-GFX blocker | Superseded. Current report/news GFX and DDS references resolve according to the wrap-up docs. |
| Older completion-audit claims before the June 5 correction | Historical evidence only. Re-read through current KUB/ALT, generic niche, instant-release, host-survival, and evolution-tier rules. |

## Queued Or Blocked Work

| Item | Status |
| --- | --- |
| Custom and chaos country pool | Deferred. Add niche generic, custom, and chaos-only countries through a separate explicit pool later; do not hardcode every releasable into the base possible-country scan. |
| Idel-Ural | Blocked until a real accepted carrier exists. Do not substitute Altai. |
| PRA railway package | Queued until Event005 railway baggage is separated. Do not borrow Event005 focus, decision, helper, asset, or origin state. |
| KUB/ALT cleanup | Active package-specific gameplay/localisation/script remnants are removed. Historical handoffs and superseded docs remain preserved as records only. KUB/ALT may still appear as ordinary vanilla releases if the resolver finds valid core territory and a safe host. |
| Additional package overlays | Future polish only unless explicitly requested. Needs verified tags, state groups, leaders/councils, AI, localisation, assets, validation, and no fallback. |
| Package-specific portraits, seals, route art, animations | Future asset work. Animated work needs real frames, manifests, static fallback, and GFX/GUI handoff. |
| Spreadsheet/catalog parity | Current workbook text was aligned for the 50-focus tree, KUB/ALT correction, and reduced-core recovery on 2026-06-05. Future catalog parity still needs review after any new packages, achievements, recovery systems, or event-detail wording changes. |
| Final completion audit | Still required before any completion claim. Current docs make playable wrap-up explicit without claiming full completion. |

## Known Contradictions To Preserve Or Resolve

| Subject | Current resolution |
| --- | --- |
| Source specs list many candidate identities, including historical packages | Treat broad matrices as design pools. They do not require all packages for playable wrap-up. |
| Historical KUB/ALT handoffs list completed gameplay changes | They are preserved as historical records but superseded as current scope. |
| Event006 can share tags with Event005 | Tag overlap is allowed. Origin decides mechanics. |
| Calm World can fire Event006 | Baseline/calm waves can release countries, but they should not normally create evolution rows. |
| Asset manifests can be complete while Event006 is incomplete | Asset completion does not equal gameplay, localisation, spreadsheet, or final event completion. |

## Out Of Scope For Documentation Curator

- gameplay script files
- localisation or scripted localisation files
- GUI/GFX files
- binary assets, image assets, audio, or spreadsheets
- events, focuses, decisions, ideas, history, country files, scripted effects, scripted triggers, or on_actions
- commits in the current dirty worktree

## Latest Curator Handoff

The latest broad documentation cleanup handoff is:

`docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_163000_documentation_curator_broad_cleanup.md`
