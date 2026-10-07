# Main Chaos Warfare emblem

Acceptance basis: the user explicitly requests the original main Chaos Warfare icon restored on October 7, 2026.
The main emblem is an exception to the broader native black/orange doctrine artwork direction; track icons and reward strips retain their accepted current art.
The active sprite remains GFX_doctrine_chaos_warfare_medium in interface/cbrn_doctrine.gfx, consumed by chaos_warfare and its existing texticon references.
The runtime texture at gfx/interface/doctrines/icons/doctrine_chaos_warfare.dds uses the exact historical bytes from Git parent 4efc01fc87f1137e98c864f928dd5603e6b7d2f1, SHA-256 af90fd785c56719867f84ddb7f011bd05811f1c0e2a8fddaabc43aa0dd7908ad.
Disposition: implemented and parent-reviewed restoration; decoded pixels, dimensions, alpha and historical mip levels match the selected source.
The [restoration handoff](../../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-07_restore_main_doctrine_emblem.md) records the source/history and before/after evidence.
No gameplay, public label, category, reward, cost, sprite identity or catalog field changes.
