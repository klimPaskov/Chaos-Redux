# Dynamic Severity-Aware Cluster Localisation Audit

## Scope

Audited the final cluster constants, member data arrays, settings selectors, Event Log selectors, and English GUI localisation for the Dynamic Severity-Aware Cluster Overhaul.

The owned runtime localisation surface was limited to `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`, and `localisation/english/chaosx_gui_l_english.yml`.

No gameplay source was edited.

## Files changed

- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/plans/event_cluster_system_plans/subagent_handoffs/localisation_audit.md`

`common/scripted_localisation/chaosx_scripted_localisation_settings.txt` was audited and needed no additional patch from this pass.

## Changed keys and selectors

- Added the `GetEventsLogClusterMemberChance` history branch for automatic, non-trigger optional members.
- Added `chaosx.events_log.cluster.member.chance.history_roll` so automatic history rows show the snapshotted final participation chance and the actual member roll together.
- Updated `chaosx.events_log.window.clusters.empty` to describe a filtered empty result accurately.
- Updated `chaosx.events_log.window.cluster_details.description.peace`.
- Updated `chaosx.events_log.window.cluster_details.description.natural_disasters`.
- Updated `chaosx.events_log.window.cluster_details.description.formables`.
- Updated `chaosx.events_log.window.cluster_details.description.economy_positive`.
- Updated `chaosx.events_log.window.cluster_details.description.diseases`.
- Updated `chaosx.events_log.window.cluster_details.trigger.tt`.
- Updated all six `chaosx.events_log.cluster.na_reason.*` keys to use the visible term `Activation` instead of `Roll`.
- Retained the accepted visible label `By Roll` while preserving its internal key and weighted activation metric.
- Updated `chaosx.trigger_events.cluster_trigger.tt`.

## Coverage findings

### Missing keys

No missing localisation keys were found in the audited cluster selector ranges.

All eight cluster IDs resolve in Event Log and Settings selectors, including `diseases`.

### Duplicate keys

No duplicate keys were found in `chaosx_gui_l_english.yml`.

No duplicate `defined_text` names were found in either audited scripted-localisation file.

### Scripted localisation issues

The automatic history fallback in `GetEventsLogClusterMemberChance` previously displayed only `global.events_log_cluster_detail_member_final_chance_entries`.

The new history branch also displays `global.events_log_cluster_detail_member_roll_entries` and applies only when the selected row belongs to automatic history, is optional, and is not the trigger row.

The earlier N/A, Manual, and Guaranteed branches remain authoritative, so those special states are unchanged.

No other broken scripted-localisation reference was found in the audited cluster ranges.

### Dynamic text opportunities

The preserved history roll array was the only missing material dynamic value found in scope, and it is now displayed.

The existing selectors already resolve Trigger, Required, and Optional roles, all four severities, all six effective Chaos tiers, every member status including `skipped_runtime`, and the canonical disabled, already-fired, and zero-weight reasons.

### Cross-surface consistency

Event Log, Settings, and Help consistently describe severity-aware activation, eligible-member scaling, fatigue, prior optional turnout, guaranteed required participation, and optional participation rolls.

The displayed term `Activation` now matches the cluster list, detail panel, Settings panel, and blocked-reason tooltips, while the accepted sort-mode label remains `By Roll`.

`GetEventsLogDetailClusterLine` resolves a single-row event to the percentage activation label and duplicate logical rows with a severity range to `Varies by row`.

The catalogue and history branches retain separate activation displays, and manual history retains the `Manual` label.

### File encoding

All three audited source files decode as strict UTF-8.

`localisation/english/chaosx_gui_l_english.yml` retains its UTF-8 BOM.

The two `common/scripted_localisation/*.txt` files remain ordinary UTF-8 script files without a BOM, which is consistent with their source type.

### Prose quality

- Vagueness: `abnormal moving paths` was replaced with the concrete description of disasters moving along abnormal paths.
- Bloat: the Formables description no longer repeats cluster type, unlock tier, role, severity, and member event type already visible in the panel.
- Obvious explanation: the Positive Economy and Peace descriptions no longer explain their visible member metadata.
- Repetition: `Roll` terminology was removed from player-facing activation controls and blocked explanations.
- Overcomplication: the Peace, Natural Disasters, Formables, Positive Economy, and Diseases descriptions were shortened while preserving their established gameplay premise.
- Style repair: manual-trigger tooltips now distinguish the cluster's bypassed gates from the event-system fireability checks that still apply to members.

### Sourced quotations

No sourced or attributed quotation appears on the audited cluster surfaces.

No quotation was changed.

## Behavior before and after

Before this patch, an automatic optional-member history row showed `Final chance: 45%` even though the snapshot also preserved its actual roll.

After this patch, the same row shows `Final chance: 45%  Roll: 63`.

Guaranteed trigger and required rows still show `100% / Guaranteed`, manually fired rows still show `Manual`, and unavailable rows still show `N/A`.

Before this patch, player-facing cluster controls mixed the terms `Activation` and `Roll` for the same top-level probability.

After this patch, the player-facing term is consistently `Activation`, while `Roll` remains only where an actual recorded random result is displayed.

## Validation

Targeted constant-to-selector coverage found zero missing cluster names, roles, severities, statuses, canonical reasons, or sort modes.

Repository-wide English localisation lookup found zero missing keys referenced by the audited cluster selector ranges.

The audited English file contains zero duplicate keys, and both scripted-localisation files contain zero duplicate `defined_text` names.

Strict UTF-8 decoding succeeded for all three audited files, and the English YML BOM remains present.

## Skipped meaningful validation and blocker

The required production GUI inspection and render could not run.

Both `hoi4.gui_inspect` and `hoi4.gui_render` returned `ARTIFACT_MANIFEST_INTEGRITY_FAILED` for workspace `mod_chaos_redux_ea3b2d67c2c0`, with the blocker message `Artifact provenance manifest does not match its immutable address`.

No GUI artifact URI was produced, so clipping, wrapping, alignment, and the new history value cannot be accepted through the mandatory one-to-one production render in this pass.

Source inspection confirms the member text remains inside the existing three-line localisation structure, but source review is not equivalent to the blocked production render.

## Remaining issues and parent follow-up

The parent must rerun `hoi4.gui_inspect` and `hoi4.gui_render` for `events_log_cluster_details_window` after the MCP artifact-manifest issue is repaired, covering automatic optional history, Manual, Guaranteed, N/A, `skipped_runtime`, long text, and 1920x1080 plus 1366x768 layouts.

No unresolved wording decision or missing gameplay mechanic was found in this bounded audit.

No new design plan was required.

No commit was created because the shared worktree contains extensive concurrent changes owned by other agents.
