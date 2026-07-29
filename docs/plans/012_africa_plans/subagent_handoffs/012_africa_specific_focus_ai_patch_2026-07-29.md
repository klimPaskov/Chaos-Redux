# Event 12 specific host focus AI patch handoff

## Scope

This patch adds 22 bounded AI strategy plans for the full Event 12 host playbooks in matrix rows 43 through 64.
The plans only edit `common/ai_strategy_plans/012_africa_focus_plans.txt`.
The existing national focus tree, focus `ai_will_do` blocks, route plans, country tags, and gameplay effects are unchanged.

Each plan requires `is_ai = yes`, `africa_is_current_host = yes`, `africa_focus_has_continental_tree = yes`, and the exact `africa_host_playbook` script constant.
The abort block repeats the host, tree, and exact constant checks so a transferred or invalid host cannot keep a stale specific plan.
The 22 constants are mutually exclusive because the host playbook classifier stores one accepted playbook value.

## Matrix-to-plan mapping

| Matrix ID | Matrix profile | Exact host constant | AI plan | Regional overlay | Distinct focus emphasis |
| ---: | --- | --- | --- | --- | --- |
| 43 | `host_ethiopia_specific` | `africa_host_playbook.ethiopia` | `africa_host_ethiopia_focus_plan` | Nile and Horn | Survival, officer reform, Red Sea corridor, food and military support, Crown or command route preference |
| 44 | `host_egypt_specific` | `africa_host_playbook.egypt` | `africa_host_egypt_focus_plan` | Nile and Horn | Sovereignty, canal defence, Nile access, logistics, Republican or Crown route preference |
| 45 | `host_sudan_specific` | `africa_host_playbook.sudan` | `africa_host_sudan_focus_plan` | Nile and Horn | Congress, transport, pastoral settlement, river access, Federal or Confederation route preference |
| 46 | `host_morocco_specific` | `africa_host_playbook.morocco` | `africa_host_morocco_focus_plan` | Maghreb and Sahara | Zone reunification, Rif and Atlantic access, desert council, Crown route preference |
| 47 | `host_algeria_specific` | `africa_host_playbook.algeria` | `africa_host_algeria_focus_plan` | Maghreb and Sahara | Citizenship, land, nationalist coalition, urban and Sahara governance, Republican route preference |
| 48 | `host_tunisia_specific` | `africa_host_playbook.tunisia` | `africa_host_tunisia_focus_plan` | Maghreb and Sahara | Coalition institutions, port defence, rural reform, Maghreb congress, Republican route preference |
| 49 | `host_libya_specific` | `africa_host_playbook.libya` | `africa_host_libya_focus_plan` | Maghreb and Sahara | Regional compact, resistance integration, desert logistics, consent restoration, command or Confederation route preference |
| 50 | `host_liberia_specific` | `africa_host_playbook.liberia` | `africa_host_liberia_focus_plan` | West Atlantic | Concession audit, citizenship and labour, port roads, resource contracts, Republican or Confederation route preference |
| 51 | `host_nigeria_specific` | `africa_host_playbook.nigeria` | `africa_host_nigeria_focus_plan` | West Atlantic | Federal bargain, regional representation, rail and river integration, revenue sharing, Federal route preference |
| 52 | `host_gold_coast_specific` | `africa_host_playbook.gold_coast` | `africa_host_gold_coast_focus_plan` | West Atlantic | Producer settlement, mining revenue, port and inland balance, resource contracts, Federal or People's Union route preference |
| 53 | `host_senegal_fwa_specific` | `africa_host_playbook.senegal_fwa` | `africa_host_senegal_fwa_focus_plan` | West Atlantic | Federal reconstitution, citizenship, rail corridors, Sahel congress, Federal route preference |
| 54 | `host_sierra_leone_specific` | `africa_host_playbook.sierra_leone` | `africa_host_sierra_leone_focus_plan` | West Atlantic | Colony and protectorate settlement, mining and labour, port defence, diaspora support, Republican route preference |
| 55 | `host_belgian_congo_specific` | `africa_host_playbook.belgian_congo` | `africa_host_belgian_congo_focus_plan` | Congo Basin | Administrative transfer, river and rail spine, mining settlement, resource sovereignty, Federal or People's Union route preference |
| 56 | `host_angola_specific` | `africa_host_playbook.angola` | `africa_host_angola_focus_plan` | Congo Basin | Labour abolition, concession review, port and rail integration, regional representation, Federal or People's Union route preference |
| 57 | `host_french_equatorial_africa_specific` | `africa_host_playbook.french_equatorial_africa` | `africa_host_french_equatorial_africa_focus_plan` | Congo Basin | Federal reconstitution, concession review, interior transport, Chad and Cameroon links, Federal route preference |
| 58 | `host_kenya_specific` | `africa_host_playbook.kenya` | `africa_host_kenya_focus_plan` | Swahili and Indian Ocean | Land commission, railway authority, pastoral access, territorial defence, Federal or Republican route preference |
| 59 | `host_uganda_specific` | `africa_host_playbook.uganda` | `africa_host_uganda_focus_plan` | Great Lakes | Federal settlement, cotton revenue, lake transport, kingdom and civic representation, Federal or Crown route preference |
| 60 | `host_tanganyika_specific` | `africa_host_playbook.tanganyika` | `africa_host_tanganyika_focus_plan` | Swahili and Indian Ocean | Mandate transition, labour, railway, Zanzibar association, Federal route preference |
| 61 | `host_somali_specific` | `africa_host_playbook.somali_territories` | `africa_host_somali_specific_focus_plan` | Nile and Horn | Territorial congress, pastoral mobility, port customs, water and voluntary association, Confederation or command route preference |
| 62 | `host_madagascar_specific` | `africa_host_playbook.madagascar` | `africa_host_madagascar_focus_plan` | Madagascar and Islands | Island congress, land and labour, roads and ports, diaspora support, Confederation route preference |
| 63 | `host_south_africa_specific` | `africa_host_playbook.south_africa` | `africa_host_south_africa_focus_plan` | Southern Africa | Civil-war coalition, representation, land and labour, rail and mine recovery, military route preference |
| 64 | `host_southern_rhodesia_specific` | `africa_host_playbook.southern_rhodesia` | `africa_host_southern_rhodesia_focus_plan` | Southern Africa | Land settlement, constitutional conflict, mining and rail, balanced forces, Federal or Confederation route preference |

The matrix uses the profile key `host_somali_specific`, while the accepted script constant is `africa_host_playbook.somali_territories`.
The plan keeps the accepted constant and records the profile-key alias in the source comment.

## Behaviour before and after

Before this patch, the file had constitutional route, support, and formation plans but no host-playbook-specific focus factor layer.
After this patch, one host-specific plan composes with the existing regional overlay and constitutional route plans for the current host.
Opening priorities and the four full signature focuses are weighted for every host.
The matching six-focus regional overlay, support lanes, and all six grounded route openers receive host-specific multipliers.
Existing focus-local `ai_will_do` logic remains live and continues to gate feasibility, proof state, crisis urgency, and route validity.

## Validation

The static validation read the matrix, the focus tree, and the edited AI plan file.
It found 22 plan blocks for 22 expected full-host rows.
It found all 22 expected `africa_host_playbook` constants exactly once with no extra constants.
It found no invalid focus references against `common/national_focus/012_africa_continental_focus_tree.txt`.
It found no duplicate focus entries inside a plan.
It found 22 distinct complete focus-factor vectors and 22 distinct focus-ID sets.
Each plan contains 30 factors, except Sierra Leone with 31 because its colony and protectorate profile adds a local-consent support anchor, and South Africa with 31 because its matrix priorities include a postwar constitutional review support lane.
The vector categories cover opening, full-host signature, regional overlay, support, and constitutional route choices for every profile.

No MCP focus render or live game simulation was run because this patch changes only AI strategy plans and does not alter focus-tree structure or layout.
A live campaign audit should still sample the 22 host constants with peace, invasion, transfer, and `world_end` states before release.

## Simplifications and remaining risks

No matrix host row was omitted, merged, or replaced with a fallback.
The plan layer translates the matrix focus priorities into existing focus IDs and leaves decision, diplomacy, military, and high-chaos action behavior to the already-scoped Event 12 profile controller.
The main remaining risk is balance interaction between these multiplicative plan factors and live `ai_will_do` modifiers during simultaneous proof or crisis gates.
