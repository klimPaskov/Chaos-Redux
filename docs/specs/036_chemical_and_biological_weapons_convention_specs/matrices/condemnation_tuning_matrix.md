# Condemnation tuning matrix

## Ordinary source multipliers

| Stage | Full chemical | Full biological | Full nuclear | Full repeat | Chemical-only chemical | Chemical-only nuclear | Reservation chemical retaliation | Reservation biological retaliation | Reservation nuclear retaliation |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Baseline | `0.55` | `0.75` | `0.90` | `0.75` | `0.60` | `0.95` | `0.70` | `0.85` | `0.95` |
| Evolution I | `0.35` | `0.60` | `0.82` | `0.60` | `0.40` | `0.90` | `0.50` | `0.70` | `0.90` |
| Evolution II | `0.18` | `0.40` | `0.65` | `0.40` | `0.22` | `0.75` | `0.30` | `0.50` | `0.78` |
| Evolution III | `0.08` | `0.22` | `0.50` | `0.25` | `0.12` | `0.60` | `0.18` | `0.35` | `0.65` |

Public Rejection and covert Public Rejection use `1.00` for every source.

Chemical Accession uses `1.00` for biological sources.

Reservation values require a valid retaliation receipt.

## Severity floors

| Source condition | Floor |
| --- | ---: |
| Ordinary chemical military use | Table value |
| Chemical extreme civilian destruction | `0.50` |
| Ordinary controlled biological use | `0.20` |
| Catastrophic biological outbreak | `0.70` |
| Nuclear military or industrial target | `0.50` |
| Nuclear populated capital or dense civilian target | `0.80` |
| Thermonuclear use | `1.00` |
| Doomsday effect | `1.00` |
| Atrocity | `1.00` |
| Cover-up | `1.00` |

## Opening source reductions

| Posture | Chemical reduction | Biological reduction | Nuclear reduction | Eligible repeat reduction |
| --- | ---: | ---: | ---: | ---: |
| Full Ratification | `35%` | `25%` | `10%` | `20%` |
| Chemical Accession Only | `30%` | `0%` | `5%` | `15%` for chemical-derived repeat sources |
| Retaliation Reservation | `15%` | `10%` | `5%` | `10%` |
| Public Rejection | `0%` | `0%` | `0%` | `0%` |
| Covert Public Rejection | `0%` | `0%` | `0%` | `0%` |

## Required impact sweeps

| Sweep ID | Variable range | Required observation |
| --- | --- | --- |
| `E36_C01` | Base chemical source from low to extreme | Ordinary member use falls as intended while extreme civilian floor dominates |
| `E36_C02` | Base biological source and outbreak severity | Catastrophic outbreak never falls below `0.70` |
| `E36_C03` | Nuclear target type | Military target can reach `0.50`, populated capital stays at or above `0.80` |
| `E36_C04` | Thermonuclear source | Multiplier remains `1.00` at every evolution |
| `E36_C05` | Atrocity and cover-up mix | Event 036 changes neither component |
| `E36_C06` | Repeat-use count | Repeat component weakens without double-reducing base family source |
| `E36_C07` | Reservation retaliation proof | Valid retaliation uses table, offensive use returns to normal treatment |
| `E36_C08` | Opening condemnation composition | Only eligible public source buckets are reduced once |
| `E36_C09` | Hidden evidence | No opening or treaty operation reveals or reduces hidden evidence |
| `E36_C10` | Posture change after action | Historical action keeps its original treaty snapshot and final source value |
