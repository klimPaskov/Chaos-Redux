# IW-002 Wales Lewis Pugh Evans ownership scan

This scan covers the identity, stable token, portrait sprite, and Event 6 roster ownership gates before a future portrait replacement.

## Search terms

The exact and variant identity terms checked were `Lewis Pugh Evans`, `Lewis Evans`, `Pugh Evans`, `Lewis_Pugh_Evans`, `Lewis-Pugh-Evans`, `lewis_pugh_evans`, `WLS_lewis_pugh_evans`, `Thomas Wynford Rees`, `Wynford Rees`, and `T W Rees`.

The stable consumer terms checked were `WLS_independence_wave_mountain_commandant`, `GFX_portrait_WLS_independence_wave_mountain_commandant`, and `portrait_WLS_independence_wave_mountain_commandant`.

## Roots and results

| Root | Result | Disposition |
| --- | --- | --- |
| Current Chaos Redux `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, `localisation/` | No Lewis Pugh Evans identity owner, portrait file, or recruitment consumer. The stable WLS token and sprite consumer exist as the expected generated-character target. | No origin owner; retain the stable target token and do not create a duplicate identity key. |
| Installed vanilla `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, `localisation/` | No Lewis Pugh Evans identity, character, portrait, `.gfx` consumer, or localisation owner. | No vanilla transfer conflict. Edmund Ironside and other vanilla-owned commanders were not used. |
| Approved reference mod `1521695605` | No Evans identity or asset owner. The scan did find `RAJ_thomas_wynford_rees` and its portrait consumers; Rees was rejected and no reference-mod art was copied. | Disclosure only; the rejected Rees identity remains owned by the reference mod and is not reused. |
| Approved reference mods `2265420196` and `1458561226` | No Lewis Pugh Evans identity, portrait, recruitment, `.gfx` consumer, or localisation owner. | No reference-mod conflict; no art or source copied. |
| Event 6 specs and plans for IW-002/WLS | No named Evans or Rees entry in the WLS roster. The roster only requires a sourced real male leader and allows an institutional command if sourcing fails. | Evans fills the sourced commander slot without changing the spec or roster files. |

No same-person owner is active in Chaos Redux or vanilla, and the selected identity is not imported from an approved reference mod.

This source-only package does not edit any character, history, portrait, interface, localisation, or gameplay file.
