# The Orchard Flowers Once

The Orchard Flowers Once is a recovery-era Fallout chain for a rural state whose first flowering arrives after the soot retreat. It is separate from Seed Vault Custody, which decides who owns stored seed, and The Bad Batch, which tests a questionable cultivar. This chain asks what the first living harvest means to a community that has not trusted open ground for years.

## Runtime identity

| Surface | Contract |
| --- | --- |
| Candidate | 408 |
| Transaction | 710032 |
| Route | 7132 |
| Event ids | `chaosx.fallout.408` through `.414` |
| Target | Lowest valid native owned state with a produced Air Winter recovery snapshot |
| Opening | Human choice or hidden AI choice |
| Branches | Harvest early, preserve seed, open a public festival, scientist control |
| Result delay | 42 days |
| Callback | First harvest review after 210 days |
| Event Log history | 9137 with fifteen outcome payloads |
| Asset | `GFX_report_event_fallout_orchard_flowers` |

## Eligibility and deterministic selection

The state must be controlled by the owner, have a current Fallout identity and resource row, retain population, and carry a produced Air Winter snapshot. Adaptation must be at least 38, exposure must remain below 72, reclamation must remain below 88, and the state must remain in a rural, pastoral, or town category. The state must also carry at least one point of the produced food reserve. The country selector requires current Food, Medicine, Cohesion, and the recovery campaign window from day 1200 through day 3200.

The candidate producer scans owned states in native id order and records only the lowest eligible state. It stores the food reserve as mechanic pressure, so a missing or stale snapshot cannot turn an unrelated state into a generic orchard target.

## Choices and delayed outcomes

Harvest early exchanges Food and Medicine for immediate food and a smaller seed memory. Preserve seed protects the next planting window at the cost of a slower current recovery. Open a public festival turns the first bloom into a shared local memory and risks crowd damage. Scientist control trades current food for adaptation evidence and a documented cultivar. Each branch freezes Food, Medicine, Cohesion, Recognition, Adaptation, Reclamation, and seed memory before reserving its delayed transaction. Result bands are deterministic and use distinct thresholds for each branch.

Success and partial results change the nine-resource survival ledger, Cohesion, Stability, War Support, state Reclamation, Adaptation, Exposure, and Supply Access. Failure damages one repairable building family, spends the state reserve, and records a Deaths-system loss. Every branch writes an explicit state memory and a timed state modifier. The callback changes the same ledgers and records whether the first harvest became durable, uneven, or lost.

## AI and cleanup

The hidden AI route prefers an early harvest when Food is strong, preserves seed when Adaptation is high, opens the festival when Cohesion is high, and uses science control when Medicine is the limiting resource. It uses the same delayed receipt, branch effects, Deaths path, Event Log payloads, callback, and cleanup as human play. Cleanup releases the callback and result tickets by exact token, clears the state registry, and leaves the durable orchard memory ledgers in place.

The candidate remains dormant until the Fallout scheduler activation gates, host authority, save-recovery, multiplayer input blocking, and runtime Event Log delivery are reviewed. This chain does not count toward the 660-block release floor while those gates remain closed.

## Asset wiring

The generated source and processed PNG live under `docs/assets/air_cleanliness_fallout/fallout_orchard_flowers/`. The final DDS lives at `gfx/event_pictures/fallout/report_event_fallout_orchard_flowers.dds`. The sprite is registered in `interface/fallout_consolidated.gfx`, and events 408, 410, and 412 use the dedicated sprite. No Zombie Apocalypse asset, path, audio, or sprite is reused.
