# Event 006 Documentation Curator Handoff: Broad Cleanup

Role: `chaosx_documentation_curator`
Date: 2026-06-05
Scope: broad documentation-only cleanup for Event 006 Independence Wave.

No subagents were spawned from this curator pass. No gameplay, localisation, scripted localisation, GUI/GFX, assets, spreadsheets, events, focuses, decisions, ideas, history, scripted effects, scripted triggers, or on_actions were edited.

## Files Changed

- `docs/plans/006_independence_wave_plans/source_of_truth_map.md`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_event006_completion_audit_continuation_readonly.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_141433_event006_next_missing_package_audit.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_163000_documentation_curator_broad_cleanup.md`

## Current Docs Source Of Truth

Primary routing map:

- `docs/plans/006_independence_wave_plans/source_of_truth_map.md`

Current source documents to trust first:

- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_decisions_ai.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_achievements_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_catalog_update.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_research_notes.md`

Current practical status:

- Event006 is an instant-release wave with aftermath dossiers and boards.
- Event006 is independent from Event005 Soviet Collapse; origin decides mechanics.
- Hosts must never be erased.
- Current new-country direction is niche generic releases, especially Africa/South America/etc.
- `ASN`, `KBN`, `PLM`, and `AYM` are current generic niche examples with unique flags and shared `independence_wave_liberation_provisional_tree` access.
- KUB/ALT package-expansion framing is superseded.
- Evolution logs are release-scale tier milestones only: Gathering Storm, Rising Cascade, Old Names Return, and Impossible Statehood. Calm/baseline waves should not normally create evolution rows.
- Current wrap-up status is technical playability and documentation alignment, not full Event006 completion.

## Superseded Docs And Claims

- `2026_06_04_145232_parent_event006_kuban_package_handoff.md`: historical only. Do not use as current KUB package scope.
- `2026_06_04_151704_parent_event006_altai_package_handoff.md`: historical only. Do not use as current ALT package scope.
- `2026_06_05_142822_parent_event006_catalog_125_focus_alignment.md`: partially superseded where it treated KUB/ALT as current package/focus summaries.
- `2026_06_04_event006_completion_audit_continuation_readonly.md`: now annotated as historical where it lists KUB/ALT route evidence.
- `2026_06_04_141433_event006_next_missing_package_audit.md`: now annotated as historical where it researches KUB/ALT candidates.
- Older per-release or per-package evolution-log wording: superseded by release-scale tier milestones.
- Older report/news missing-GFX blocker: superseded; current docs say report/news GFX and DDS references resolve.
- Older broad completion/audit claims: historical evidence only and must be re-read through the June 5 correction.

## Queued Or Blocked Items

- Mapuche remains blocked until a real tag and accepted state package exist.
- Idel-Ural remains blocked until a real accepted carrier exists; do not substitute Altai.
- PRA remains queued until Event005 railway baggage is separated.
- Additional package overlays, portraits, seals, route art, animations, final spreadsheet/catalog parity, and final completion audits remain future work.
- Unused KUB/ALT gameplay or localisation remnants may still exist for parser stability; removing them is a future gameplay task, not documentation-curator scope.

## Unresolved Docs Contradictions

- Source specs intentionally keep large candidate matrices. The source map now clarifies that these are design pools, not requirements for playable wrap-up.
- Historical handoffs preserve old implementation facts even when current direction changed. They are not rewritten wholesale; they are annotated or classified through the source map.
- Asset manifests can be complete while Event006 remains incomplete. The map now separates asset-manifest status from event completion.
- Workbook/catalog claims may lag implementation facts because spreadsheet editing was explicitly out of scope.

## Validation Commands

Ran or prepared these documentation checks:

```text
rg --files docs | rg '006|independence|Independence|event_006|Event_006'
```

```text
rg -n "Kuban|KUB|Altai|ALT" docs/specs/006_independence_wave_specs docs/plans/006_independence_wave_plans docs/events/006_independence_wave.md docs/assets/006_independence_wave -g '*.md' -g '*.txt'
```

```text
rg -n "Event 006|006_independence_wave|Independence Wave" docs -g '*.md' -g '*.txt' | cut -d: -f1 | sort -u
```

```text
git diff --check -- docs/plans/006_independence_wave_plans/source_of_truth_map.md docs/events/006_independence_wave.md docs/specs/006_independence_wave_specs/006_independence_wave_spec.md docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_event006_completion_audit_continuation_readonly.md docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_141433_event006_next_missing_package_audit.md docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_163000_documentation_curator_broad_cleanup.md
```

## Remaining Docs Risks

- There are many old Event006 handoffs. The source map classifies them, but not every historical handoff was individually rewritten.
- Some Event006 references in general system docs, super-event audio docs, and achievement docs are valid current references but were not exhaustively rewritten because no contradiction was found in the sampled sections.
- The repo worktree contains extensive unrelated and pre-existing gameplay, localisation, asset, spreadsheet, and Event005 changes. This curator pass did not inspect or alter them beyond documentation searches.
- A future final audit should re-check docs, event details, localisation wording, catalog/spreadsheet rows, and implementation facts together before any Event006 completion claim.

## References Consulted

- Offline Paradox wiki snapshot: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`.
- Repo skills: `chaos-redux-subagents`, `chaos-redux-events`.
