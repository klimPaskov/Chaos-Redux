# Event 045 claim registry design map

| Registry layer | Purpose | Public effect |
| --- | --- | --- |
| Geographic state group | Exact current map states and adjacency | names the claim and settlement area |
| Interested actor family | identifies valid claimant and successor families | controls who may register an interest |
| Baseline dispute flag | makes the group eligible for opening or immediate adjacent claims | enables early objectives |
| Evolution I flag | marks broader historical ambitions | enables wider claims after Evolution I |
| Conflict set | records overlapping claimants | affects camps and Evolution III |
| Settlement modes | transfer, corridor, access, demilitarization, subject, unresolved memory | bounds postwar results |
| External owner link | points to another event that already owns the claim | prevents duplicate grants and rewards |

## Implementation map rule

The state groups must be built from installed map data and inspected with the HOI4 map tools. Working historical names in the spec are not state IDs. Every claim helper, tooltip, decision, settlement check, and AI target must use the same maintained state-group definition.
