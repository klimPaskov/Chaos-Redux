# Event 006 formable state-puzzle category attachment audit

## Result

All seventeen current Event 006 formable decision categories attach `independence_wave_formable_state_puzzle_scripted_gui`. The grouped runtime contains fourteen family overlays. The shared formation decision and AI commit gate require `has_independence_wave_selected_formable_state_puzzle_territory`, and the separate FORM-05 proclamation gate requires its own state-puzzle territory helper.

## Category crosswalk

| Category | Source | Family surface |
| --- | --- | --- |
| `independence_wave_formables_category` | `common/decisions/categories/006_independence_wave_categories.txt` | Discovery and selected-family route |
| `independence_wave_formable_transaction_category` | `common/decisions/categories/006_independence_wave_formable_registry_categories.txt` | Shared preparation and commit transaction |
| `independence_wave_form0124_membership_category` | `common/decisions/categories/006_independence_wave_form01_02_04_categories.txt` | Pending FORM-01, FORM-02, FORM-04, FORM-08, and FORM-09 invitations |
| `independence_wave_form01_congress_category` | same | FORM-01 |
| `independence_wave_form02_union_category` | same | FORM-02 |
| `independence_wave_form04_league_category` | same | FORM-04 |
| `independence_wave_form03_low_countries_category` | `common/decisions/categories/006_independence_wave_form03_categories.txt` | FORM-03 |
| `independence_wave_form05_charter_category` | `common/decisions/categories/006_independence_wave_form05_categories.txt` | FORM-05 |
| `independence_wave_form08_danube_category` | `common/decisions/categories/006_independence_wave_form08_categories.txt` | FORM-08 |
| `independence_wave_form09_balkan_category` | `common/decisions/categories/006_independence_wave_form09_categories.txt` | FORM-09 |
| `independence_wave_iw043_middle_volga_congress_category` | `common/decisions/categories/006_independence_wave_iw043_iw058_categories.txt` | FORM-12 and FORM-13 |
| `independence_wave_iw058_council_of_communities_category` | same | FORM-18 |
| `independence_wave_form16_integration_category` | `common/decisions/categories/006_independence_wave_transcaucasus_categories.txt` | FORM-16 |
| `independence_wave_form39_invitation_category` | `common/decisions/categories/006_independence_wave_form39_categories.txt` | FORM-39 invitation |
| `independence_wave_form39_federal_compact_category` | same | FORM-39 formation and progression |
| `independence_wave_form48_invitation_category` | `common/decisions/categories/006_independence_wave_form48_categories.txt` | FORM-48 invitation |
| `independence_wave_form48_federal_compact_category` | same | FORM-48 formation and progression |

## Gameplay alignment

`common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt` contains the finite family and state helpers. `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt` dispatches the selected family to the same territory helper before the shared formation transaction can pass. `common/scripted_triggers/006_independence_wave_form05_triggers.txt` applies the same rule to the dedicated island-league proclamation. This makes the GUI summary, player availability, and AI availability share one territory contract.

FORM-01 and FORM-02 include both Scottish compact states 121 and 133. FORM-03 admits state 6 only through a frozen `BEL_flanders` founding consent and never transfers Belgian territory. FORM-12 and FORM-13 require the state 249 carrier plus three consenting external member anchors. FORM-18 requires the state 676 carrier plus both consenting external member anchors. FORM-08 stays fail-closed at two of three until a researched third Danubian member is approved.

## Evidence

The compiler produced fourteen manifests and 100 readable DDS pieces. Source inspection found exactly seventeen attachments. The current grouped GUI inspection is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ef2673ff8f17120d4af57ee1ea186242cab51bbd0de180293f6dee95f5ba358/466d18177cb6f43241458de2d3e61a09c36b90b67dbddf56274eade7e6cc18a1/gui-inspect.fc2200e9c790f7c3.json`. The current 1920x1080 and 1366x768 render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5cf4a0e6908e754ba9e1bae29b05ae013092399118afcfe42cedf62d2833fe9/bad290e958062d59c6887532469bc60e48c725f8a9ce6ea2fd8f95c81eb43eb5/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The generic MCP scenario activates mutually exclusive overlays together and therefore reports aggregate overlap diagnostics. Source activation gives pending invitations precedence and otherwise selects one family. A dedicated Event UI worker is not used because this is a shared formable registry window, which the repository routing rules explicitly exclude from event-owned GUI workers.
