# Repowiki page-worker brief

This is the shared brief for every worker that refreshes or creates pages under `.qoder/repowiki/`.
Read `.qoder/repowiki/AUTHORING.md` first; it is the format contract and this file is the process contract.

## Why this work exists

The wiki was generated against a repository revision that is roughly 1,100 commits behind the working tree.
Cited files have been moved, archived, renamed or rewritten, so anchors point at the wrong lines and whole sections describe systems that have since changed.
A page is only finished when its claims match the files that exist now and every anchor points at lines that prove the claim.

## Workflow per page

1. Read the current page in full and list the claims it makes.
2. Open every file in its `<cite>` block and every file it cites.
3. Resolve citations that no longer exist:

   ```text
   python -B .tools/repowiki/verify_repowiki_refs.py --page "<page path fragment>" --verbose
   ```

   For a missing target, find the current location with `git log --diff-filter=D --name-only -- <path>` or `git log --follow --name-status -- <path>`.
   `.tools/README.md` records which tools moved into `.tools/archive/`, and `docs/README.md` records how the `docs/` tree is organised.
   When a source was genuinely deleted with no replacement, remove the citation and rewrite or drop the claim that depended on it.

4. Re-derive every anchor by reading the target file and locating the lines that support the claim.
   Prefer a narrow anchor (`#L412-L438`) over a whole-file anchor, and never keep an anchor you have not looked at.
5. Update the prose where the system changed. Keep the skeleton from `AUTHORING.md`, keep existing headings and the table of contents in sync, and keep mermaid diagrams accurate — fix node and label names that no longer exist.
6. Re-run the verifier for your pages until it reports zero broken targets and zero stale anchors.

## Hard rules

- Never invent a file, identifier, effect, trigger, localisation key, sprite name, or numeric value.
- Never describe wiki generation, drift, staleness, or repair work in page prose; write as if the system has always existed.
- Keep each sentence on one physical line; break lines only between sentences.
- Do not place code blocks inside table cells.
- Preserve the page's existing `<cite>` list ordering style and the bare-filename link labels.
- Only edit the pages assigned to you. Do not touch other pages, the metadata JSON, or `knowledge/` modules.
- Prefer primary sources: the script that implements a behaviour, its constants file, and the `.gfx`/`.gui`/localisation file that consumes it.
- When a claim needs engine semantics, the authoritative references are `paradox_wiki/` and the vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.

## Reference material

| Need | Location |
| --- | --- |
| Format contract | `.qoder/repowiki/AUTHORING.md` |
| Tooling and verification | `.tools/repowiki/README.md` |
| Repository rules | `AGENTS.md` |
| Tool inventory and retention rules | `.tools/README.md` |
| Documentation map | `docs/README.md` |
| Runtime layouts | `docs/runtimes.md`, `.codex/README.md` |
| Offline engine reference | `paradox_wiki/` |
| Vanilla documentation | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` |

## Documentation relocation map

The wiki was generated before the documentation tree was reorganised, so several cited paths no longer exist.
These are the moves that matter most when repairing citations:

| Dead path | Current path |
| --- | --- |
| `docs/biological_warfare/*` | `docs/systems/cbrn_warfare/biological_warfare/*` |
| `docs/chemical_warfare/*` | `docs/systems/cbrn_warfare/chemical_warfare/*` |
| `docs/systems/condemnation_sanctions.md` | `docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md` |
| `docs/systems/air_contamination_mechanic.md` | `docs/systems/cbrn_warfare/biological_warfare/biological_air_cleanliness.md` |
| `docs/systems/events_log_window.md` | `docs/systems/` was reorganised; search `docs/` for the current owner before citing |
| `.tools/build_formable_state_registry.py` | `.tools/archive/build_formable_state_registry.py`, retired and not a supported command |
| `.tools/build_formable_state_puzzle_consumer.py` | `.tools/archive/build_formable_state_puzzle_consumer.py`, retired |
| `.tools/generate_formable_state_geometry_registry.py` | `.tools/archive/generate_formable_state_geometry_registry.py`, retired |
| `.tools/generate_chaosx_building_positions.py` | `.tools/archive/generate_chaosx_building_positions.py`, retired |
| `.tools/audit_chaosx_country_tags.py` and `.tools/audit_hoi4_country_tags.py` | `.tools/archive/`, retired |
| `docs/specs/chaos_redux_3d_model_workflow_planning_package/*` | that package was reorganised; list the folder before citing |
| `docs/testing/live_qa/<dated run>/*` | dated evidence is not stable to cite; cite the durable test-country contract instead |
| `common/script_effects/` | no such folder exists; the effects live in `common/scripted_effects/` |
| `common/ai_strategy/006_independence_wave_generic.txt` | Event 006 AI strategy was renamed or consolidated; search `common/ai_strategy/` |
| `agents/skills/...` | the skills root is `.agents/skills/` |
| `docs/systems/triggerable_scenarios.md` | scenario documentation is event-owned now: `docs/events/<event_id>_<event_slug>/systems/triggerable_scenario.md` |
| `docs/systems/chaosx_event_logging_controls.md`, `docs/systems/events_log_window.md`, `docs/systems/settings_miscellaneous_menu.md` | those shared-system notes are gone; cite the scripted effects and GUI sources instead |

When a source was genuinely deleted with no replacement, remove the citation and rewrite or drop the claim that depended on it.
Never keep a citation to a retired tool as if it were a current command.
`docs/systems/` now holds only the cross-event system notes; per-event system documentation lives under `docs/events/<event_id>_<event_slug>/systems/`.

## Anchor rules that the verifier enforces

- Derive line counts with Python, never with PowerShell `Measure-Object -Line`. That cmdlet undercounts a file whose last line has no trailing newline, and the verifier uses `readlines()`, so a PowerShell-derived count produces an anchor that over-claims by exactly one line.
- Never put a line anchor on a binary asset. A `.dds`, `.mesh`, `.png`, `.tga`, `.wav`, or `.ogg` has no meaningful line range, so cite it by path alone.
- A `#L1-N` anchor is legitimate only when the target really has `N` lines. The verifier reports an anchor whose end sits within ten lines of the real end as loose, because that shape means the anchor came from an earlier revision of the file.
- A citation to a zero-length file proves nothing. The verifier reports those separately.
- Prefer a narrow anchor that contains the evidence over a whole-file span. Whole-file anchors on long files hide which lines actually support the claim.

## Binary asset locations

Asset folder membership changes between revisions, so verify before citing:

- PDX material naming is `<name>_diffuse.dds`, `<name>_normal.dds`, `<name>_specular.dds` alongside `<name>.mesh`. `gfx/models/buildings/` is a current example.
- A generic `Image_0.dds` / `Image_1.dds` / `Image_2.dds` material trio is a pre-consolidation convention and no longer describes the shipped layout. Check `gfx/models/<family>/` for what the family actually contains before describing its materials.

## Report format

Report back with:

- the pages you changed, as repository-relative paths
- for each page, the citations you repaired and where the target moved to
- the claims you had to rewrite because the system changed
- any citation you removed because its source no longer exists
- the verifier output for your pages
- anything you could not verify, stated explicitly as unverified
