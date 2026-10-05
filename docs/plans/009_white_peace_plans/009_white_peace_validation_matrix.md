# Event 009 White Peace Validation Matrix

This matrix records current source behavior and exact verification limits. It is not a substitute for a live game result or the required HOI4 MCP artifacts.

## Availability and Safety

| Scenario | Expected source behavior | Current evidence and limitation |
| --- | --- | --- |
| No active war | Event 009 has no live weight. A forced root or Settings entry stores `no_active_war` and sends one plain rejection report to the human requester. | `calculate_white_peace_dynamic_cap` maps the condition to `white_peace_skip_reason.no_active_war`; `.6` formats the reason. The shared Settings precheck calls `white_peace_report_failed_manual_request` only after setting dispatch disallowed. |
| Only an otherwise safe major war before Stage II | The event remains unavailable with `major_locked`; no peace is imposed, and the human requester receives `.6`. | The fresh USA test had Italy-Ethiopia as its only war and returned reason `3`, `major_locked`. Direct root entry uses `dispatch_white_peace_unavailable_report`; the Settings precheck uses its guarded 009 callback. |
| One isolated safe minor war | Base branch settles that war immediately before the report. Each human-controlled participant gets the same country report once; an AI-only pair gets one global news event. | Candidate gating requires both selected countries to have no active enemy besides each other. Source code and asset paths are present; MCP event execution and a fresh White Peace screenshot are unavailable. |
| A country has another active enemy besides the selected partner | The candidate is rejected at every stage, even if the other war is separate and otherwise safe. | `can_white_peace_conflict_be_isolated` checks each country's enemy scope against the proposed pair. This conservative rule bounds the effect to a two-country war. |
| A safe major pair after the major stage opens | The major branch can settle one isolated war. | Stage II eligibility requires the matching evolution/tier gate and existing war-pressure threshold. Global stage flags cannot override a disabled current evolution. Numeric route evidence is blocked. |
| Protected, special, nonhuman, civil-war, subject, faction, near-capitulation, unsafe-capital, or recent-settlement actor | The affected pair is vetoed. | `can_country_be_white_peace_target` and `can_pair_receive_white_peace` own the checks. This is source evidence only. |

## Branches, Evolution Settings, and Memory

| Scenario | Expected source behavior | Current evidence and limitation |
| --- | --- | --- |
| All three evolutions disabled | Base isolated minor settlement remains available, while multi, major, and broad branches have zero weight. | `set_white_peace_evolution_gates` sets event ID, type, stage, and tier before `is_current_evolution_enabled`. Existing war-pressure thresholds remain required. MCP setting scenarios are blocked. |
| Stage I multi disabled | No multi-minor branch operates at any later stage. | Stage I, II, and III multi weights use the matching Stage I enable gate. |
| Stage II major disabled | No major branch operates, even if an old global stage flag is present. | Major weights and `can_country_be_white_peace_major_target` use the current Stage II enable flag. |
| Stage III broad disabled | No broad branch operates. | The Stage III broad weight is zero unless the matching enable/tier gate passes. |
| Several separate safe minor wars | Stage I or III may settle multiple separate isolated wars within its existing cap. | Recent-country memory can reduce the actual count. Notification routing uses actual successful counts; `.5` is only used for a successful broad branch with at least three settlements. |
| A third country shares a war | No country pair from that war is selected. | The accepted one-on-one boundary deliberately removes the prior one-overcrowded-war route because third-party safety cannot be established. |
| Participant capitulates, is annexed, or becomes a subject during the No Winner watch | That participant's watch clears permanently, so later liberation cannot restore eligibility. | Event-driven callbacks in `common/on_actions/009_white_peace_on_actions.txt` clear the watch. No daily or weekly world iteration was added. |
| A country is considered again at the day-180 boundary | It remains blocked until after the delayed No Winner check. | Country memory lasts 181 days, the check runs at 180 days, and the watch lasts 181 days. The one-day margin was accepted to avoid re-arming before the prior check. |

## Outcome, Reports, News, and Achievements

| Scenario | Expected source behavior | Current evidence and limitation |
| --- | --- | --- |
| Two human participants in one selected war | Each participant receives exactly one acknowledgement for the same result variant after the war ends. | The pair application marks both human endpoints in the transient report queue. The source-model dispatch cases verify one event to each. No live multiplayer session was run. |
| Human participants in several wars settled by one chain | Each affected human receives exactly one aggregate report, including participants from later settlements in the chain. No player receives more than one result popup. | The per-country pending flag is set on both endpoints for every applied pair, then one bounded report loop sends the aggregate result and clears the queue. The [bounded source model](source_models/009_white_peace_helper_output_lifetimes.py) covers four human countries across two settled pairs. |
| Mixed human and AI participants | Human belligerents receive reports; AI belligerents receive none; no observer news event is sent. | The invocation flag selects human-report routing, while the per-country queue excludes AI countries. This is source-model evidence only. |
| AI-only successful single or multi-war chain | One observer news event is sent after settlement, with no country report. It is declared `major = yes` so it broadcasts beyond the firing country. | `.7` through `.10` provide branch-appropriate results and use the `397x153` GFX sprite. The source model confirms one news dispatch for an AI-only entry. No live observer screenshot was supplied. |
| Major branch falls back to a minor pair | The result uses the single-minor report/news route and does not claim major involvement. | `global.white_peace_last_major_involved` from the applied pair determines major-result routing. |
| Aggregate multi or broad branch settles fewer wars than its cap | The notification reflects the actual outcome. | The report helper reads `global.white_peace_last_settled_pair_count`; the broad result requires at least three separate wars. |
| Invalid direct root entry | `.6` shows the captured plain skip reason and confirms no peace was imposed. | `dispatch_white_peace_unavailable_report` snapshots the reason onto the root country. |
| Valid Settings precheck followed by `.1` | `.1` applies the same selected primary, partner, and branch that the precheck passed, then reports that outcome. The selected primary remains the event-log actor. | `.1` reuses ready context with both targets present. `apply_white_peace_pair` still revalidates its proposed partner immediately before `white_peace`. Source review confirms one weighted selection per valid entry; no MCP or live source-identity scenario is available. |
| Prepared pair fails transaction-time revalidation | No war is settled, no success history is written, and the entry reports `no_safe_pair`. | `apply_white_peace_pair` guards `white_peace` with `can_pair_receive_white_peace`. No MCP or live race scenario is available. |
| Invalid Settings force request | The requester receives `.6` instead of generic no-target feedback, with no event-dispatch success record. | The shared precheck calls the 009 helper after `event_single_fire_allowed = 0`. The helper sets the existing failure receipt before `.6`; generic no-target feedback is therefore suppressed. This is source evidence only. |
| No Winner achievement | Both countries must remain alive, independent, and uncapitulated for 180 days. | `.20` checks the explicitly carried partner target; event-driven status changes clear watch flags. MCP and live save proof are unavailable. |
| The Circular achievement | One broad settlement must end at least three separate isolated minor wars. | The owned effect and constants use only `broad_conflicts_required = 3`; the parent-updated description and tooltip now state this requirement. |

## Assets and Visual Review

The accepted requirement-to-runtime audit is recorded in [009_asset_coverage_crosswalk.md](009_asset_coverage_crosswalk.md).

| Surface | Evidence | Limitation |
| --- | --- | --- |
| Report popup | Existing DDS decodes at `210x176`, and the native-size preview shows a restrained period table scene. | Its original source, prompt, and durable provenance manifest are missing from the current package. |
| AI observer news | `news_event_009_white_peace.dds` decodes at `397x153`; the image is opaque monochrome, and DDS pixels match the processed PNG. The sprite is registered in `interface/009_white_peace_event_images.gfx`. | No live news-window screenshot is available. |
| Achievement icons | Five completed, grey, and not-eligible textures decode at `64x64`, are wired, and have visually distinct runtime states. | Source art, prompt lineage, and a durable requirement-to-runtime manifest are missing from the current package. |
| GUI and popup screenshots | The supplied `evt009_sheet.jpg` shows unrelated USA/Japan reports and Rhineland/Aussa news. | No supplied image shows Event 009, so popup/news layout remains unverified. |

## Weight and Validation Status

The baseline probability agent attempted `hoi4.probability_inspect`, evaluation, sweep, and same-scenario comparison with the saved five-scenario set. Each required analysis route timed out after 600 seconds and returned no artifact, candidate ranking, scenario hash, or numeric delta. Its handoff is the evidence for this blocker.

The baseline source copies are under `docs/plans/009_white_peace_plans/evidence_2026_10_05/baseline/`. The named scenarios are under `docs/plans/009_white_peace_plans/subagent_handoffs/white_peace_probability_scenarios_2026-10-05.json`. The direct source audit identified two unresolved balance risks: the minimum valid cap may flatten stage/repeatable reductions at low values, and ordinary ineligible wars can still add active-war pressure when at least one safe pair exists.

The reference context/search routes returned partial citations, while the required context/read/inspect/render routes either timed out or reported unavailable. The completion auditor's bounded `hoi4.event_inspect` and one `hoi4.event_render` reachability request each timed out after 600 seconds without artifacts or revisions. `hoi4.event_compare` was not run because there is no validated baseline graph or confirmed before/after binding. The probability auditor's inspect, evaluate, sweep, and compare requests also timed out after 600 seconds without analysis artifacts. The event-completion and probability handoffs record their exact errors and saved scenarios. No successful event graph, render, comparison, or probability artifact was produced. No game session was launched for this audit.
