# Event 006 Statehood Ledger semantic matrix static receipt

Date: 2026-08-02.

This receipt records a source-level semantic matrix for the Statehood Ledger without launching Hearts of Iron IV, rendering a live save, or claiming player-owned GUI validation.

## Command and sources

The deterministic audit is `.tools/audit_event6_gui_matrix.py` and runs from the mod root with `python -B .tools/audit_event6_gui_matrix.py`.

The audit reads `common/scripted_effects/006_independence_wave_effects.txt`, `common/scripted_guis/006_independence_wave_scripted_gui.txt`, `interface/006_independence_wave.gui`, and `interface/006_independence_wave.gfx`.

## Static matrix

| Scenario family | Source contract checked | Result |
| --- | --- | --- |
| Tabs | Government, recognition, security, League, and ambitions each set their own flag and clear the other four; the default government panel is visible when no tab is selected | PASS |
| Recognition | Unrecognized, Observed, De Facto, Treaty-backed, and Internationally Entrenched map to five ordered semantic frames from the shared recognition bands | PASS |
| Dependency | Calm, patron warning, and severe instability map to the three dependency frames | PASS |
| League | Rest is the default; regional conferences and congress preparation use drafting; charter vote uses vote; consultative, formal, durable, crisis, reformed, and rival-league phases use activated; failed and dissolved phases never inherit activated | PASS |
| Formable | Hidden, discovered, eligible after initial integration, and committed transaction map to four semantic frames | PASS |
| Animation toggle | Four static consumers and four animated siblings are mutually selected by the animation flag; each state remains bound to the same semantic frame variable | PASS |
| Refresh | The refresh click calls the shared country-state refresh, which recomputes values, lifecycles, achievements, and all four frame variables | PASS |
| Cleanup | Generation reset clears the five tab flags, four frame variables, and animation flag | PASS |

## Receipt output

The audit reports five mutually exclusive tab contracts, five recognition frames, three dependency frames, four League frames, four formable frames, four static/animated sibling pairs, and complete generation cleanup.

The source contract is static evidence only; GUI rendering, save/load persistence, animation playback, and player-owned observation remain outside this receipt.

No second Statehood Ledger, advisor icon, or additional animation family is introduced.
