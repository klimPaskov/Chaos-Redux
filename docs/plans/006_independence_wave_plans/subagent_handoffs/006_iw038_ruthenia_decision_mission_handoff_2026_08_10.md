# IW-038 Ruthenia decision and mission handoff

## Scope and ownership

This handoff covers the bounded Ruthenia decision surface for Event 006 IW-038. The owned gameplay files are `common/decisions/categories/006_independence_wave_ruthenia_categories.txt` and `common/decisions/006_independence_wave_ruthenia_decisions.txt`. No country-core, focus, localisation, AI strategy, icon, or GUI source was changed by this subagent.

The design follows the accepted KOS/MNT Event 006 decision precedent: one activation-backed founding mission, ordinary paid timed projects represented by `days_remove`, material costs paid when the project begins, and completion through `remove_effect`. Project cancellation invokes a bounded failure helper. The founding mission alone has an explicit `timeout_effect`.

## Changed identifiers

The category is `independence_wave_rut_mountain_compact_category` with `GFX_decision_independence_wave_integration_missions`.

The founding mission is `independence_wave_rut_hold_mountain_compact_together`.

The ten paid projects are:

- `independence_wave_rut_secure_mountain_depots`
- `independence_wave_rut_integrate_border_guards`
- `independence_wave_rut_register_community_compacts`
- `independence_wave_rut_settle_former_host_ledgers`
- `independence_wave_rut_ratify_constitutional_autonomy`
- `independence_wave_rut_adopt_agrarian_compact`
- `independence_wave_rut_convene_socialist_councils`
- `independence_wave_rut_establish_mountain_emergency_command`
- `independence_wave_rut_codify_durable_sovereignty`
- `independence_wave_rut_open_carpathian_network_corridor`

## Category lifecycle

The category is visible only while `is_independence_wave_rut_package = yes`. The package trigger also requires the Event 006 active-country identity and IW-038 package id. Paid projects additionally require `is_independence_wave_rut_project_ready = yes`, which requires the completed IW-038 setup flag and excludes the failed founding crisis.

The founding mission activates only after `independence_wave_iw_038_setup_complete`, remains hidden from manual firing with `available = { always = no }`, and times out using `constant:independence_wave_ruthenia_duration.founding_crisis` (600 days in the current constants file). It resolves successfully only when both Ruthenia ledgers are stable, a route government is installed, state 73 is owned and controlled, and the capital remains controlled. Loss of the package or capital invokes failure cleanup. Timeout marks `independence_wave_rut_compact_crisis_failed` and calls `independence_wave_rut_apply_project_failure`.

## Mission and project quality matrix

All entries are RUT-owned, appear under the mountain-compact category, and are anchored to the state-73 capital in Eastern Europe / Carpathian region `REG-04`. Every paid project requires active package readiness, capital control, no other active RUT project, and its custom material gate. Every paid project now also cancels when the founding crisis has failed (positive `has_country_flag` guard), closing the race where a project could complete after the founding mission timed out.

| ID | Duration | Requirement and route/host/network gate | Completion | Cancellation / duplicate risk |
| --- | --- | --- | --- | --- |
| `secure_mountain_depots` | `decision_duration.short` (75 days) | RUT administration-light cost; capital controlled; depot flag absent | Pays administration-light cost at start, calls the provisional-assembly focus helper and depot tooltip | Package/capital/crisis-loss cancellation calls failure; completion flag is `independence_wave_rut_depots_secured`; focus helper is expected to be idempotent |
| `integrate_border_guards` | `decision_duration.standard` (120 days) | Shared security-standard infantry/support/manpower/army-XP gate; capital controlled | Calls border-guards focus helper and guard tooltip after timer | Package/capital/crisis-loss cancellation calls failure; `independence_wave_rut_guards_integrated` suppresses repeats |
| `register_community_compacts` | `decision_duration.standard` (120 days) | RUT administration-standard cost and civilian-factory burden; capital controlled | Calls mountain-community guarantee helper and community tooltip | Package/capital/crisis-loss cancellation calls failure; `independence_wave_rut_communities_guaranteed` suppresses repeats |
| `settle_former_host_ledgers` | `decision_duration.long` (180 days) | Shared diplomatic-standard command/convoy/train gate; living former host at peace, or depot-secured local fallback when former host is dead/at war | Calls former-host focus helper and host-ledger tooltip | Package/capital/crisis-loss, host disappearance, or host war cancels. Local fallback now also requires `independence_wave_rut_depots_secured`, preventing a host-loss path from bypassing the depot gate; otherwise failure helper runs. `independence_wave_rut_host_ledgers_settled` suppresses repeats |
| `ratify_constitutional_autonomy` | `decision_duration.short` (75 days) | Generic constitutional route available; no RUT route government; RUT administration-light cost | Installs `independence_wave_install_rut_constitutional_government`, then applies administrative progress | Route/package/capital/crisis loss cancels through failure helper; shared route trigger plus `independence_wave_rut_constitutional_government` makes the route installer idempotent |
| `adopt_agrarian_compact` | `decision_duration.long` (180 days) | Generic traditional route available; no route government; shared diplomatic-standard cost | Installs `independence_wave_install_rut_agrarian_government`, then applies diplomatic progress | Route/package/capital/crisis loss cancels through failure helper; `independence_wave_rut_agrarian_government` is the route lock |
| `convene_socialist_councils` | `decision_duration.short` (75 days) | Generic popular-council route available; no route government; RUT administration-light cost | Installs `independence_wave_install_rut_socialist_government`, then applies administrative progress | Route/package/capital/crisis loss cancels through failure helper; `independence_wave_rut_socialist_government` is the route lock |
| `establish_mountain_emergency_command` | `decision_duration.standard` (120 days) | Generic emergency-military route available; no route government; shared security-major material gate | Installs `independence_wave_install_rut_emergency_government`, then applies security progress | Route/package/capital/crisis loss cancels through failure helper; urgent AI doubles during war; `independence_wave_rut_emergency_government` is the route lock |
| `codify_durable_sovereignty` | `decision_duration.strategic` (300 days) | Stable compact, founding settlement complete, a RUT route government, capital control, and RUT strategic cost | Sets `independence_wave_rut_durable_sovereignty` and applies the major settlement helper | Package/route/stability/capital/crisis loss calls failure. It is intentionally retryable after a failed timed attempt; the completion flag is the idempotent duplicate guard |
| `open_carpathian_network_corridor` | `decision_duration.long` (180 days) | Stable compact, `independence_wave_network_member`, `independence_wave_league_route_available`, capital control, shared diplomatic-standard cost | Calls the Carpathian focus helper and network reward helper | Package/network/league/stability/capital/crisis loss calls failure; `independence_wave_rut_carpathian_corridor_open` suppresses repeats |

## Costs and requirement clarity

Ruthenia administration-light, administration-standard, and strategic custom triggers are country-core-owned and use the centralized `independence_wave_ruthenia_cost.civilian_factory_floor` plus shared Event 006 command-power/manpower/stability/war-support values. Security-standard and security-major use shared infantry-equipment, support-equipment, manpower, and army-XP gates. Diplomatic-standard uses shared command-power plus convoy-or-train gates. The paid decisions expose the same custom-cost triggers and custom-cost text keys that gate selection, so the UI cannot present an affordable action that fails its material check.

No political-power store, passive checklist, free unit grant, advisor icon, or bespoke GUI is used. Civilian factory burden is a file-scoped parser-safe value of one for administration and strategic projects, matching the RUT constants intent.

## AI validity and route locks

Decision and mission scores use centralized `constant:independence_wave_decision_ai` values: urgent for the founding crisis and emergency command, high for depots/guards/communities/constitutional/socialist/sovereignty, standard for host settlement/agrarian/network. Guard integration and emergency command receive a double modifier during war; host settlement receives a double modifier when no severe host threat exists. Route decisions require the generic shared route triggers and no existing RUT government. The route-government trigger in the current core source agrees with the four installed RUT flags: constitutional, agrarian, socialist, and emergency.

The required read-only MCP probability source inspection was run against the current decision file. `decision_ai_will_do` discovered no ordinary decision candidates and correctly suggested the mission adapter because every RUT surface is a mission-style block (`days_remove` or `days_mission_timeout`). `mission_ai_will_do` then discovered all 11 mission candidates (founding mission plus ten projects), 15 required inputs, zero unresolved parser inputs, and an intentionally incomplete runtime pool. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/431013578e784c2dd98965fa4f448355aa8598ed2fb279bdf629bf4359955972/0a5dd58825697323eb8381cfc05fc32cb5ae0d9e623c413f458e4f6aaeb6364e/probability-inspect-1abc644d8975.json`.

The RUT AI-strategy source was separately inspected with `ai_strategy_factor`; the installed adapter returned `PROBABILITY_SOURCE_DISCOVERED` with the exact blocker `no_weighted_surfaces` and zero candidates because the source contains strategy declarations rather than a recognized weighted-factor surface. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82a04a99920221935925ce723ad58229e6df53ea54135af2f2287dd13968f97c/5954a14f9f4de2eeaa1beb2eca71637cfc6885975f622fb7f69755661c68f2b5/probability-inspect-9a8e1fd82c85.json`.

No normalized runtime probabilities or live AI behavior are claimed. The delegated `chaosx_ai_probability_auditor` remains responsible for named empty/unprepared, ready-peace, ready-war, host-threat, stable-route, and network-ready scenarios plus any compare/sweep evidence.

## Localisation and tooltip gaps

Localisation was intentionally not edited in this scope. The parent localisation package must provide the category key/description, all 11 names and descriptions, three RUT cost text keys (`independence_wave_rut_cost_administration_light`, `independence_wave_rut_cost_administration_standard`, `independence_wave_rut_cost_strategic`), and the founding/project effect tooltips referenced in the source (`independence_wave_rut_project_failure_effect_tt`, depot, guards, communities, host-ledger, host-loss, constitutional, agrarian, socialist, emergency, sovereignty, and network tooltip keys). Tooltip prose should describe current civic, security, route, host, and network outcomes rather than implementation history.

## Cleanup and exploit-risk notes

The active-project trigger in `common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt` enumerates exactly the ten paid IDs. All paid projects block while any listed project is active. The founding-crisis-failed cancellation guard was added to all ten paid projects so a founding timeout cannot leave a project running into a success callback. The host-loss fallback requires depot completion, preventing free settlement when the prerequisite infrastructure was never secured. Completion relies on country-core idempotent helpers and completion flags; parent review must verify those helpers also clear active flags and stale decision state in failure cleanup.

The project timer semantics intentionally follow KOS/MNT: timer expiry executes `remove_effect` as completion, while `cancel_trigger`/`cancel_effect` is the failed path. If the plan is later interpreted as requiring a distinct timeout-failure branch for each paid project, that is a broader decision-system redesign and is not silently substituted here. Durable sovereignty is timed and retryable after cancellation; its completion flag prevents successful duplicate execution.

There is no decision-owned scripted GUI. The category uses the ordinary HOI4 decision shell, so the mandatory `hoi4.gui_inspect`/`hoi4.gui_render` route is not applicable and no `hoi4.gui_rewrite` was used. Existing category icon precedent is reused.

## Validation and remaining blockers

Targeted checks completed: decision and category braces are balanced; the decision file has no unsupported `<=` or `>=` operators; all 11 decision blocks and 11 cancellation blocks are present; all ten paid cancellation blocks contain the positive founding-crisis-failed guard; the active-project trigger contains all ten exact IDs; `git diff --check` is clean for the two owned source files. Offline wiki pages, vanilla decision documentation and AFG mission precedent, and sibling KOS/MNT sources were consulted before editing.

No Hearts of Iron IV process was launched. Live save/runtime, country-core helper execution, and localisation rendering remain parent-owned. At handoff drafting time, the RUT trigger file is present and agrees with all decision references; the country-core scripted-effect file and its idempotent helper bodies are still expected from the parallel core worker and must be checked before IW-038 attestation.

No simplification was made to the requested ten-project surface. The only deliberate bounded choice is the accepted ordinary `days_remove` timer convention for paid projects and the absence of a bespoke GUI/localisation edit, both required by scope and sibling precedent.
