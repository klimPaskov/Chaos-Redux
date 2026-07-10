# Repression Ledger UI GFX Handoff

The main implementation has registered all UI sprites in `interface/camp_repression_rework.gfx` and consumes them from `interface/camp_repression_ledger.gui` plus the repression decision category.

| Family | Live path pattern | Consumer |
| --- | --- | --- |
| Category/open icons | `gfx/interface/camp_repression/GFX_decision_*_repression_ledger.dds` | Decision category and open/close decisions |
| Window/panels | `gfx/interface/camp_repression/GFX_repression_ledger_{window_bg,summary_strip,card_bg,country_card_bg}.dds` | Main window and five tabs |
| Buttons | `gfx/interface/camp_repression/GFX_repression_ledger_{tab_button,action_button}.dds` | Three-frame `buttonType` sprites |
| Compact marks | `gfx/interface/camp_repression/GFX_repression_ledger_{tab_*,population_pressure,labor_output,evidence_risk,reform_pressure,guard_burden,rail_burden}.dds` | Tabs and value-card icon family |
| Static state layers | `gfx/interface/camp_repression/GFX_repression_ledger_{warning_frame_static,evidence_seal_static,reform_seal_static,selected_state_frame_static,critical_frame_static}.dds` | Pool warning, discovery, reform, selected state, and critical state |

No animation `.gfx` entry is required. The accepted static fallback IDs are the runtime sprites.
