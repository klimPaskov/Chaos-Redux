# Event 006 shared focus layout closeout

Date: 2026-07-25

Scope: `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`.

## Outcome

The restored baseline was inspected and rendered again. The gameplay source remains untouched. A prior coordinated `+1` x/y reflow candidate was rejected: it increased the validator result to 19 blocking diagnostics, 64 connector crossings, 26 node intersections, and 27 long connectors. The candidate was fully reverted before this closeout; no source coordinate, prerequisite, mutual exclusion, reward, AI block, icon reference, or localisation key from that candidate remains.

Current baseline evidence is stable:

| Metric | Baseline |
|---|---:|
| Regular focuses | 176 |
| Connectors | 214 |
| Connector crossings | 49 |
| Node intersections | 18 |
| Long connectors | 26 |
| Bounds | `x=1..97`, `y=0..19` |
| Layout hash | `3e5996acbdbed97ab085d52cd058861f2fbd21acc896f859268b204a9c81a5a2` |
| Inspector validation | Failed: 14 blocking focus diagnostics |

The layout hash above is the source-derived hash returned by the current inspector. The exact source and MCP revision are recorded below.

## Files and source integrity

| Surface | Result |
|---|---|
| `common/national_focus/006_independence_wave_focus.txt` | Unchanged; worktree blob `92e86959022df8a2d0f50f2cbde8950cc3c76ac6` equals `HEAD:common/national_focus/006_independence_wave_focus.txt`. |
| Gameplay/AI/reward surfaces | No file was edited by this audit; no focus id, prerequisite, mutual exclusion, completion reward, `ai_will_do`, icon, or localisation key changed. |
| New file | This handoff only. Existing untracked handoffs in the same directory were not touched. |
| Focus tree | `independence_wave_focus_tree`; source `common/national_focus/006_independence_wave_focus.txt`. |

## MCP evidence

Inspector artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7bd5f349df84104fecd819209aa5cb0ca699f678106803a4bfb51d96036533fa/45aa318285576901021e0307d9c0eac6cda1043434b109ff0d6c541656d075f6/focus-inspect.450b181d807e8a96.json`

Inspector revision: `450b181d807e8a96e8702a9fa0cf775b244d44239e80cf90314da43c6adaa075`.

Render artifacts (national mode, `horizontalSpacing=96`, `verticalSpacing=130`, `padding=48`, `reviewScale=1`; output `9456x2642`):

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1b11861a97cf950c6fbbc83f65959b445626eff71b589c0ab04c84f52f2282d5/d3152e1159e5da492b36879b68b6d72ac5d9ccc5b3ea8f533cfe6f433b6833e0/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ac59a6968946dc8bc50040e5d8c1ed1b4a4d6eaf3e03a1b6423900a1631fd8f/bfde03418ec2156decfbdb5ff223b8591e7990b500b0d399c30ec308871f47ff/independence_wave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/240e6f7e5c777c81dc2092da0b14716b8f91b527e20531daf98375256d1f11c2/ebc86449c0230f9e48d58ae7a251d17304fd6325fb94c068a4b184a67f0b6798/independence_wave_focus_tree.focus.json`
- Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b66834bb2de543afaee08bad9cf110c48cb9447d9cf7ee57f2f0d169879d41e/c1c4cefc1bb8cb24fb878fe43a472334b29564bb821fa08356e7b279f6d4f91f/independence_wave_focus_tree.focus.source-map.json`
- Layout plan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84f0996962af15cda701b880b63c84c58f9e58bdd5531731a4e3215f4e94927d/3b37cc15540e14ccab76cbe6154343009bcc6eb17170c1146ed986b0d3f4ce34/independence_wave_focus_tree.focus.plan.json`

## Route coverage

| Required route | Source anchors | Status |
|---|---|---|
| Survival and state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement` (approximately lines 62-216) | Present |
| Government and internal power | Constitutional, popular-council, traditional, emergency-command, patron/client, radical-sovereignty, and AJX settlement blocks (approximately lines 817-1212) | Present; route locks preserved |
| Economy, infrastructure, and administration | `independence_wave_inventory_the_state` line 100; `independence_wave_establish_emergency_revenue` line 281; `independence_wave_secure_food_and_fuel` line 300; `independence_wave_build_regional_transport_authority` line 320 | Present; geometry only remains noisy |
| Army, security, and military identity | `independence_wave_integrate_militia_commands` line 401 through `independence_wave_preserve_independent_command` line 653; convergence at `independence_wave_found_professional_defense_institution` line 502 | Present; convergence is the main layout hotspot |
| Diplomacy, recognition, and patrons | Foreign-office, guarantor, recognition, and treaty blocks (approximately lines 670-812) | Present |
| Former-host policy, borders, and expansion | `independence_wave_define_former_host_policy` line 1274 through the former-host/regional expansion block | Present |
| Network, league, formables, and high-chaos sovereignty | `independence_wave_recognize_fellow_new_states` line 1529 and later league/formable/high-chaos blocks | Present |
| Shared regional overlays | Existing IW043, IW058, IW093, IW098, and regional package blocks | Present; no overlay was removed or disconnected |

## Blocking layout diagnostics

The 14 blocking diagnostics are all connector crossings. One physical crossing emits both `FOCUS_AVOIDABLE_CONNECTOR_CROSSING` and `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`; the other 13 are unsatisfied crossings whose endpoints are fixed or relative.

| Crossing group | Focus identifiers and source lines | Count |
|---|---|---:|
| Founding/economy | `bind_the_first_oath` line 119 -> `integrate_provinces_and_councils` line 177 crosses `inventory_the_state` line 100 -> `establish_emergency_revenue` line 281 | 2 diagnostics |
| Founding root into regional/economy/officer lanes | `complete_founding_settlement` line 197 -> `ajx_appoint_neutral_commission_focus` line 1214 crosses each of: `secure_food_and_fuel` line 300 -> `build_regional_transport_authority` line 320; `secure_food_and_fuel` -> `define_former_host_policy` line 1274; `secure_food_and_fuel` -> `recognize_fellow_new_states` line 1529; `secure_national_depots` line 421 -> `recall_and_vet_officers` line 442; `secure_national_depots` -> `define_former_host_policy`; `secure_national_depots` -> `recognize_fellow_new_states` | 6 diagnostics |
| Professional-defense convergence | `adopt_military_archetype_program` line 483 -> `adopt_border_defense` line 611 crosses `confirm_civilian_control` line 527 -> `found_professional_defense_institution` line 502 and `grant_military_autonomy` line 541 -> the same convergence; `adopt_military_archetype_program` -> `adopt_reclamation_doctrine` line 625 crosses both `confirm_civilian_control` and `grant_military_autonomy`; `adopt_military_archetype_program` -> `preserve_independent_command` line 653 crosses `build_professional_core` line 569 -> the convergence; `adopt_military_archetype_program` -> `standardize_with_league` line 639 crosses `confirm_civilian_control` -> the convergence | 6 diagnostics |

Nonblocking geometry warnings remain on these source-linked paths:

- Long connectors: `complete_founding_settlement` line 197 -> `map_internal_power_centers` line 221 (17 columns); `inventory_the_state` line 100 -> `establish_emergency_revenue` line 281 (12 columns); `bind_the_first_oath` line 119 -> `integrate_militia_commands` line 401 (14 columns).
- Through-node intersections: `complete_founding_settlement` line 197 -> `survey_regional_ambition` line 1456 passes through `activate_package_economic_program` line 358 and `adopt_military_archetype_program` line 483.

## Missing or simplified content

None found within this bounded layout audit. No route, focus reward, decision/mission hook, idea, advisor, leader, flag, claim, core, war goal, event, or formable unlock was removed, added as a substitute, or simplified. A broader route redesign remains out of scope.

## Icon coverage

| Surface | Result |
|---|---|
| Regular focuses | All 176 focus nodes retained icon assignments; no missing-icon diagnostic was emitted by inspect or render. |
| Shared/regional overlays | Existing icon ids and `.gfx` registrations were not changed. |
| Continuous palette | Existing 14 continuous focuses were not changed; no asset issue was emitted. |

## Localisation and reward mismatch list

No mismatch found. Inspector resolved 176 focus titles, and neither inspect nor render emitted a missing-localisation or reward-text diagnostic. Existing descriptions, custom reward tooltips, and completion effects remain paired with their original focus ids.

## AI behavior gaps

No bounded-scope AI gap found. Existing `available` and `ai_will_do` blocks remain unchanged, including route-aware weights where present. No AI tuning was attempted because the only safe scope was coordinate/layout evidence.

## High-priority fixes

1. Re-pack the founding fan-out, economy/officer lanes, and regional roots as coupled clusters before attempting another rewrite; isolated endpoint moves were already shown to worsen aggregate geometry.
2. Reflow the professional-defense cohort together: `confirm_civilian_control`, `grant_military_autonomy`, `build_professional_core`, `adopt_border_defense`, `adopt_reclamation_doctrine`, `standardize_with_league`, `preserve_independent_command`, and `found_professional_defense_institution`.
3. Only after crossings are solved, shorten the three long connectors and clear the two through-node paths. Do not alter prerequisites or hidden availability merely to suppress lines.
4. If a fully planar tree is required, authorize a broader layout plan/rewrite with coupled-cluster review; the rejected +1-x/+1-y candidate shows that a global nudge is not safe.

## Remaining route risks and validation limits

The gameplay graph and route coverage are intact, but fixed/relative endpoint geometry still produces 14 blocking crossings plus five nonblocking warning paths. Moving one root can shift errors into regional overlays and formable lanes. No game runtime or save validation was run because no gameplay source changed. The next layout pass must rerun both `hoi4.focus_inspect` and `hoi4.focus_render` after every coupled-cluster candidate.
