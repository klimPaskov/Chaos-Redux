# Event 006 generic focus-tree audit v98

Date: 2026-08-02

Scope: the single `independence_wave_focus_tree`, its assignment and final-validation contract, the FSM package correction, route coverage, rewards, AI, prerequisites, mutual exclusions, icons, and localisation. Bespoke country trees and live or in-game testing are outside this audit by the accepted user decision.

## Verdict

The generic-tree contract is a static PASS. Event 006 has one shared tree, and every admitted full-framework package uses that tree. IW-012 ICE is the sole reviewed additive carrier and preserves its meaningful `iceland_tree`; the common package finalizer fails closed when neither the full-tree nor reviewed-carrier contract is proven.

Vanilla FSM exposes only the non-meaningful `generic_focus` tree. Its dormant IW-179 package therefore uses `independence_wave_focus_assignment.full_framework`, and its preparation trigger requires `independence_wave_full_focus_framework`, `independence_wave_focus_tree`, and the full-framework assignment value. No meaningful existing tree is overwritten.

## Static coverage

- 207 focus blocks in the inspected Event 006 focus file: 184 regular and 23 shared; no duplicate IDs.
- Every inspected block has an AI weight and completion reward.
- Focus names, descriptions, and the 207 custom tooltips resolve through localisation.
- 52 unique icon IDs resolve with shine variants.
- 108 mutual-exclusion edges resolve to valid targets; the six one-sided AJX exclusions are intentional government-route blockers.
- Prerequisite targets and OR/AND semantics are valid.
- Survival/state construction, government, economy, military/security, diplomacy/host, regional expansion, Network/League, formable/high-chaos, and gated package modules are all present and connected to the shared effects and ledgers.

## Evidence boundary and risks

`hoi4.focus_inspect` and `hoi4.focus_render` remain unavailable beyond the tool's `SCAN_BYTE_LIMIT`, so connector geometry and visual overlap are not claimed as runtime-verified. One hundred fourteen focuses use base-only AI weighting; route gates remain present, but a future AI-depth pass could add dedicated strategy modifiers. No gameplay fallback, bespoke tree, new lane, or asset family was introduced.

The allocator, protected-tag scan, and brace/static checks were rerun after the FSM correction. The whole-event v98 completion audit remains **PARTIAL / HOLD** for package capacity/admission, scenario acceptance evidence, formables, assets, GUI/achievement evidence, catalog status, and super-event `6001`; those blockers are not caused by the generic-tree contract.
