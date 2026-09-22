# File ownership and implementation order

## Event-owned files

Paths below are proposed destinations. Inspect the current repository before adding or renaming a file. Retain compatible existing Event 79 filenames when they are already consumed.

| Owner | Proposed file or family | Responsibility |
| --- | --- | --- |
| Parent system implementer | `events/079_the_master.txt` | Root, internal lifecycle, reports, immediate takeover dispatch |
| Parent system implementer | `common/scripted_effects/079_the_master_effects.txt` | Race registry, payments, score changes, commitment, cleanup |
| Parent system implementer | `common/scripted_triggers/079_the_master_triggers.txt` | Target, sponsor, action, and takeover validity |
| Parent system implementer | `common/script_constants/079_the_master_constants.txt` | Thresholds, durations, anchors, enum IDs, caps |
| Parent system implementer | `common/on_actions/079_the_master_on_actions.txt` | Narrow lifecycle callbacks and CXT registration |
| Parent system implementer | `common/decisions/079_the_master_decisions.txt` | Paid actions and finite aftermath work |
| Parent system implementer | Existing Event 79 category definition or event-owned category file | Category visibility and context |
| Parent system implementer with AI audit | `common/mtth/079_the_master_mtth.txt` | Verified willingness providers and evolution timing |
| Parent system implementer | `common/ideas/079_the_master_ideas.txt` and verified dynamic-modifier file | Consolidated status and industrial reservations |
| Event UI worker | `common/scripted_guis/079_the_master_scripted_gui.txt` | Selected-view logic, live fields, tooltips, native actions |
| Event UI worker | `interface/079_the_master.gui` | Event-owned category board and expanded panel |
| Parent integration owner | `interface/079_the_master.gfx` | Registration of delivered event-owned assets |
| Parent writing owner | `localisation/english/079_the_master_l_english.yml` | Final writing under the direction-only specification |
| Art workers | Event-owned `gfx/` subfolders and documented achievement exceptions | Source and final art plus processing receipts |

The architecture reviewer and decision auditor do not both edit the same effect file in parallel. The parent merges their findings. Shared files remain single-owner.

## Shared edits owned by the parent

The event selector, repeat logic, settings, evolution log, Event Details, cluster arrays, shared achievement registry, CXT registry consumption, and catalog workbook must not be assigned to a child GUI or art worker. Each shared edit needs a before/after review to avoid removing unrelated registrations.

The spreadsheet worker is the sole workbook writer during its tranche. It regenerates exports after the workbook is saved. Other workers can propose row changes in Markdown but cannot edit CSV snapshots directly.

## Delivery sequence

### Tranche A: prove the central result

Complete the unread engine references and close G01 through G06, including the subject-hierarchy conflict. Build a tiny targeted runtime fixture that creates a real puppet without waiting for a popup. Do not begin a large polished interface around an unproven core result.

### Tranche B: race and payment core

Implement generation-safe race records, registration, seed snapshots, positive-action history, immediate threshold handling, and once-only payment receipts. Prove save/load and two simultaneous races before adding all action variants. Complete equipment and investment adapter gates.

### Tranche C: complete baseline

Implement all five positive families and counter-propaganda, baseline target reactions, refunds, inactivity, AI, political compatibility, saturation, and actual building/equipment delivery. Test a poor minor, a rich major, and an ideological outsider with the same rules.

### Tranche D: evolutions

Implement active maturation and evolved openings, stronger action variants, institution operations, Great Game capacity, blocking coalitions, and cross-race action capacity. Preserve old action receipts during stage upgrades.

### Tranche E: interface, art, and writing

Review the HOI4-style interface reference, implement the native board, generate and process the required art, and write final localization. Use real data snapshots for render tests. Check long names, insufficient resources, partial refunds, and empty-rival states.

### Tranche F: integration and review

Integrate event selection, cluster severity, logs, settings, achievements, CXT, and catalog changes. Run the independent near-completion improvement planner, merge accepted design changes into the main specs, and perform source, GUI, AI, multiplayer, and runtime completion audits.

### Tranche G: release decision

Re-run affected tests after fixes. Confirm all critical gates and list any accepted noncritical limitations. Keep the catalog To Be Reworked until the user authorizes a status change after the relevant completion evidence exists.

## Migration from the legacy implementation

Do not reuse `global.minor_to_attract` as the new race identity. The existing `attraction_points` and historical score arrays need a versioned migration disposition. For an old save with an active legacy race, the safe default is an explicit administrative closure with preservation of already delivered assets and removal of legacy-only pending actions.

Do not retroactively invent new receipts for unrecorded legacy spending. Do not remove pre-existing guarantees just because the old system created some guarantees without ownership records. An exact safe migration needs a separate inspected save fixture. Until then, recommend new-save testing and identify old-save migration as unsupported rather than claiming it works.
