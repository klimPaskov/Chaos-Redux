# GFX and GUI handoff

The stable GFX and GUI registrations were already present when this package
was finished. This asset task did not edit `.gfx`, `.gui`, scripted GUI, or
gameplay files. Read-only validation confirms the following contract.

| State | Sprite | Runtime texture |
|---|---|---|
| No target selected | `GFX_utopia_ledger_case_no_target` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_case_no_target.dds` |
| Target eligible | `GFX_utopia_ledger_case_target_eligible` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_case_target_eligible.dds` |
| Target selected | `GFX_utopia_ledger_case_target_selected` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_case_target_selected.dds` |
| Offer pending | `GFX_utopia_ledger_case_offer_pending` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_case_offer_pending.dds` |
| Counteroffer | `GFX_utopia_ledger_case_counteroffer` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_case_counteroffer.dds` |
| Refusal | `GFX_utopia_ledger_case_refusal` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_case_refusal.dds` |
| Ultimatum available | `GFX_utopia_ledger_case_ultimatum_available` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_case_ultimatum_available.dds` |
| Case expired | `GFX_utopia_ledger_case_expired` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_case_expired.dds` |
| Stewardship active | `GFX_utopia_ledger_case_stewardship_active` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_case_stewardship_active.dds` |
| Associate established | `GFX_utopia_ledger_case_associate_established` | `gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_case_associate_established.dds` |

## Placement

- GFX registration: `interface/015_utopia_manifesto.gfx`.
- GUI layout: `interface/015_utopia_manifesto_ledger.gui`.
- Parent container: `utopia_ledger_ground_panel`.
- Each card position: `x = 8`, `y = 4`.
- Native texture size: `300x96`.
- Each icon remains `alwaystransparent = yes` so it does not consume input.
- The live text box remains separate from the art. The accepted cards keep the
  left and centre dark and quiet for that overlay.

## Existing live-state priority

The scripted GUI evaluates the specialised states before idle states:

1. stewardship active;
2. refusal;
3. counteroffer;
4. ultimatum available;
5. offer pending;
6. target selected;
7. target eligible;
8. associate established;
9. case expired;
10. no target selected.

This file is an asset handoff only; state logic remains owned by the gameplay
and scripted-GUI implementation.

