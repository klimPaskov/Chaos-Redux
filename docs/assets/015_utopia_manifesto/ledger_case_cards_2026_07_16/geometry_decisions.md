# Geometry decisions

The runtime ratio is `3.125:1` (`300x96`). Ratios below are measured after
external-matte removal. Every accepted card uses a centred cover crop followed
by one uniform resize; no axis is stretched independently.

| State stem | Post-matte size | Ratio | Delta from target | Geometry crop box | Result | Decision |
|---|---:|---:|---:|---|---:|---|
| `no_target` | 2188x718 | 3.047354 | -2.485% | 0,9,2188,709 | 2188x700 | Small vertical cover crop; shield and complete frame retained. |
| `target_eligible` | 2172x718 | 3.025070 | -3.198% | 0,11,2172,706 | 2172x695 | Small vertical cover crop; compass, dossier, and frame retained. |
| `target_selected` | 2172x724 | 3.000000 | -4.000% | 0,14,2172,709 | 2172x695 | Fresh wide replacement; small crop retains round compass, seal, dossier, and border. |
| `offer_pending` | 1935x641 | 3.018721 | -3.401% | 0,11,1935,630 | 1935x619 | White external matte removed, then small crop retains packet, tubes, sandglass, and frame. |
| `counteroffer` | 2172x720 | 3.016667 | -3.467% | 0,12,2172,707 | 2172x695 | Small crop retains both dockets, round seals, hinge, ribbons, and split frame. |
| `refusal` | 2172x718 | 3.025070 | -3.198% | 0,11,2172,706 | 2172x695 | Small crop retains crossed latch, cracked seal, and interrupted border. |
| `ultimatum_available` | 2172x724 | 3.000000 | -4.000% | 0,14,2172,709 | 2172x695 | Fresh wide replacement; small crop retains packet, full hourglass, gavel, and alert frame. |
| `expired` | 2172x724 | 3.000000 | -4.000% | 0,14,2172,709 | 2172x695 | Small crop retains curled dossier, stopped glass, cold seal, and frame. |
| `stewardship_active` | 2172x720 | 3.016667 | -3.467% | 0,12,2172,707 | 2172x695 | Small crop retains keys, ledger, round seal, leaves, and green frame. |
| `associate_established` | 2172x718 | 3.025070 | -3.198% | 0,11,2172,706 | 2172x695 | Small crop retains linked round seals, institutions, ribbon, gear, and frame. |

The full-size, post-matte, processed-native, DDS-decoded, and 2x-nearest
contact reviews confirm that circles remain round and the right-side emblems
are not squashed. The maximum accepted source-ratio difference is 4.0%.

