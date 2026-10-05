# Event 009: Text, Log, Cluster, and Result Delivery

Disposition: implemented for accepted settlement and delivery rules, with MCP validation unresolved and catalog-workbook alignment accepted and queued. Parent G3 wording corrections are already applied to the current shared localisation.
Acceptance basis is the parent's 2026-10-05 task and [accepted decisions](../../../plans/009_white_peace_plans/agent_decisions_2026-10-05.md), including user G6 for isolated wars and G7 for invalid-entry feedback. The parent accepted G2 per-human aggregate reports and G3 plain cause-first prose on 2026-10-06.
This replaces the legacy popup-ID draft and does not certify gameplay completion.

## Settlement and delivery

Hidden `chaosx.nr9.1` prepares a safe candidate and applies settlement immediately.
Acknowledgment options do not execute peace or select another branch.
Stages I and III settle multiple separate isolated wars within branch caps, and a third war participant or another active enemy disqualifies a candidate at every stage.
One successful chain produces one aggregate country report to every human-controlled participant in the settled wars, or one global news event if every settled participant is AI. The pending-report queue is cleared at entry and after delivery, so each affected human sees one result per chain.
The single-war displayed countries are preserved as `white_peace_report_primary` and `white_peace_report_partner`.

| Actual result | Human-participant report | AI-only observer news |
| --- | --- | --- |
| One minor war | `chaosx.nr9.2` | `chaosx.nr9.7` |
| Multiple minor wars without the broad-result condition | `chaosx.nr9.3` | `chaosx.nr9.8` |
| One major-branch war | `chaosx.nr9.4` | `chaosx.nr9.9` |
| Broad branch settles at least three separate minor wars | `chaosx.nr9.5` | `chaosx.nr9.10` |

A selected multi or broad branch that only settles one war uses the single-war result, and a broad branch that only settles two uses the multi-war result.
Forced invalid human entry uses `chaosx.nr9.6`, whose plain description states a rejection reason and confirms that no peace was imposed.
Reasons cover no active war, no safe pair, locked major stage, protected conflicts, and recent settlement memory.
Source evidence is `events/009_white_peace.txt` and `prepare_white_peace_runtime_context`, `apply_white_peace_current_context`, `dispatch_white_peace_unavailable_report`, and `fire_white_peace_report_event` in `common/scripted_effects/009_white_peace_effects.txt`.

## Localisation key authority

Current report and news wording is owned by `localisation/english/009_white_peace_l_english.yml`.
Reports `.2` through `.6` use their own `.t`, `.d`, `.a`, and `.tt` keys, and news `.7` through `.10` uses `.t`, `.d`, and `.a`.
`chaosx.nr9.1.t` names the hidden dispatcher, which has no visible description or acknowledgment contract.
Event-name lookup uses `chaosx.event_name.9` in the shared event-log selectors.
Use `[white_peace_report_primary.GetName]` and `[white_peace_report_partner.GetName]` for preserved report targets.
Parchment descriptions and invalid-entry reasons use plain names and values.

The former titles `A Note Without Demands`, `Tables in Several Rooms`, `A Major Power Steps Back`, and `The Armistice Circular` were prose proposals.
Their base `.1`, multi `.2`, major `.3`, and broad `.4` draft mapping is superseded by the map above.
The suggested `chaosx_event_name_9` and `chaosx_event_debug_name_9` keys and `[?white_peace_primary.GetName]` draft syntax are superseded by the current namespace and target syntax.

## Details, evolution, history, and cluster

Event Details and catalog detail fields describe the armistice premise without listing hidden branches or predicting later mechanical outcomes.
This is parent-accepted prose direction in the 2026-10-05 decisions, and final shared-localisation reconciliation remains parent-owned.
Evolution titles remain `Repeated Minor Settlements`, `Major-Country Settlement`, and `Broad Diplomatic Settlement`.
The parent explicitly accepted actual branch gating by current evolution settings in its 2026-10-05 follow-up task.
`set_white_peace_evolution_gates` sets caller-local event id and type, then stage and tier for each `is_current_evolution_enabled` check.
Its computed flags are `white_peace_multi_branch_enabled`, `white_peace_major_branch_enabled`, and `white_peace_broad_branch_enabled`.
A disabled Stage I blocks multi-settlement branches at all later stages, a disabled Stage II blocks major eligibility and branch weight, and a disabled Stage III blocks the broad branch.
Stage progression and existing war-pressure gates still apply, and old global unlock history cannot bypass a disabled current setting.
Disabling all three evolutions retains eligible base isolated minor peace.
Evolution history and preview rows do not independently authorize a gameplay branch.
Evolution descriptions must distinguish several separate isolated wars from a multi-party war and must not describe a larger safe segment of one overcrowded conflict.
Cluster ID `4` is `Peace`, with Event ID `9` as a low-severity repeatable member.
Availability requires an eligible isolated candidate, and compact reasons explain unavailable wars without exposing raw trigger identifiers.
History uses Event ID `9` and a primary actor through the existing shared mapping.
The curator did not review or edit shared GUI layouts, registries, history effects, or localisation selectors.

## Achievements and image references

The accepted Circular criterion is a broad branch settling three distinct isolated minor wars.
The five-pair alternative is rejected because each eligible pair is already a separate war under the isolated boundary.
No Winner keeps the continuous 180-day condition for both countries, and shared achievement prose follow-up belongs to the parent.
Reports use `GFX_report_event_009_white_peace`, and news uses `GFX_news_event_009_white_peace`, both registered in `interface/009_white_peace_event_images.gfx`.
The news runtime texture is opaque monochrome `397x153` `gfx/event_pictures/009_white_peace/news_event_009_white_peace.dds`.
Production and DDS round-trip evidence is in [white_peace_news_art_handoff.md](../../../plans/009_white_peace_plans/subagent_handoffs/white_peace_news_art_handoff.md) and the active `docs/assets/009_white_peace/` workspace.
The news handoff's pending-wiring statement predates the parent's integration evidence, and that new handoff is outside this curator's edit scope.

## Catalog and validation limits

The older workbook handoff is historical evidence and does not establish current alignment.
Workbook reconciliation is accepted and queued in [catalog_changes_pending.md](../../../plans/009_white_peace_plans/catalog_changes_pending.md).
Its worker must mirror final in-game text in the authoritative XLSX and run the catalog exporter after saving.
No workbook or CSV was read or edited in this reconciliation.
Source confirms the ID map, immediate settlement, result-count selection, and image consumption, while MCP inspection, rendering, and comparison remain unresolved or blocked as recorded by the parent and curator handoff.
Source review does not replace MCP evidence, parent integration review, or live-game observations.
