# Event 010 — Death State Effects Matrix

| State condition | Owner/controller | Population | Buildings/resources | Movement/supply | Attrition/withering | Visual | Cleanup |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal candidate island | Existing owner | Normal | Normal | Normal | None | Normal | Candidate only. |
| Origin consumed | Death owns/controls | Set to zero; add to Death consumed population; record civilian deaths if enabled. | Delete factories/dockyards/strategic buildings; disable resources. | Severe supply and movement penalty. | Death wasteland hazard active if invaded. | Hidden dark/fog state if possible; no public reveal. | Mark `death_origin_state`, `death_consumed_state`, core for Death. |
| Hidden island spread consumed | Death owns/controls | Zero and counted. | Delete/disable. | Severe. | Active if invaded. | Hidden dark/fog. | Schedule delayed report. |
| Mainland reveal consumed | Death owns/controls | Zero and counted; if pre-pop >100k, reveal fires. | Delete/disable. | Severe. | Active. | Public dark/fog. | Set reveal, world threat, neighbor war checks. |
| Neighbor wither target | Existing owner/controller until completed | Normal until consumed. | Normal until consumed. | May receive fear/supply disruption. | Wither progress rises only if no non-Death divisions present. | Warning/shroud marker after reveal. | Clear if defended, quarantined, or Death defeated. |
| Withered consumed state | Death owns/controls | Zero and counted. | Delete/disable. | Severe. | Active. | Public dark/fog. | Remove wither target flags; add core. |
| Recaptured wasteland | Non-Death controller/owner or occupied by enemy | Remains zero. | Remains deleted/disabled. | Lingering severe or moderate penalty; outpost can reduce. | Lingering hazard; less than active Death state. | Dead-zone visual remains. | Opens survey/outpost missions. |
| Purified outpost | Non-Death controller/owner | Still zero. | Limited strategic repair only; no population restoration. | Improved enough for limited supply/movement. | No active wither unless Death returns. | Muted wasteland/outpost visual. | Can be reconsumed if Death returns. |
| World-end foothold | Death owns/controls | Zero and counted immediately. | Delete/disable. | Extreme. | Strong active wither and ghost spawn. | Strong dark storm/fog. | Counts as terminal Death foothold. |

## Design notes

- Population restoration is not part of this event. Consumed population is literally deleted.
- Recapture is meaningful because it defeats Death and opens safe corridors, not because it restores the old state.
- If the engine cannot remove a building or resource directly, the implementation must neutralize it with a state modifier or equivalent scripted representation and document the limitation.
- Every state path must call the shared consumption effect when Death consumes it.
