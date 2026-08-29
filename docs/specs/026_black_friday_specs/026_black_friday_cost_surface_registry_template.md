# Event 26 cost surface registry template

This ledger must be copied into the implementation plan or system documentation and completed against the exact implementation commit.

## Registry metadata

| Field | Value |
| --- | --- |
| Repository commit | To be recorded |
| Supported game version | To be recorded |
| Installed DLC set used for discovery | To be recorded |
| Audit date | To be recorded |
| Primary auditor | To be recorded |
| Completion auditor | To be recorded |

## Coverage rows

| Surface ID | Logical transaction ID | Cost component ID | Logical action | Owner file | Engine or mod system | DLC gate | Payer scope | Cost family | Primary achievement family | Resource type | Ordinary cost source | Affordability source | Payment effect | Display source | Refund policy | AI consumer | Rounding quantum | Strategy A to D | Baseline test | Evolution I test | Save and reload test | Status | Evidence or blocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Example only | Remove before completion |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Required status values

Use one of these exact dispositions:

- `covered_native`
- `covered_scripted`
- `covered_static_variants`
- `engine_inaccessible`
- `not_a_purchase_cost`
- `blocked_pending_evidence`

`blocked_pending_evidence` cannot remain in a completion claim.

## Strategy D evidence form

| Field | Required entry |
| --- | --- |
| Surface and exact cost field |  |
| Current displayed-cost source |  |
| Current payment source |  |
| Native modifier routes checked |  |
| Database conditional routes checked |  |
| Scripted effect or trigger routes checked |  |
| GUI adapter routes checked |  |
| Offline documentation checked |  |
| Vanilla precedents checked |  |
| Exact reason the real cost cannot change |  |
| Reason a replacement action would be inaccurate |  |
| Player-facing compatibility effect |  |
| Completion-report reference |  |

## Family summary

| Cost family | Discovered surfaces | Native | Scripted | Static variants | Engine inaccessible | Not a purchase | Blocked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Political power |  |  |  |  |  |  |  |
| Laws |  |  |  |  |  |  |  |
| Personnel |  |  |  |  |  |  |  |
| Command power |  |  |  |  |  |  |  |
| Army experience |  |  |  |  |  |  |  |
| Navy experience |  |  |  |  |  |  |  |
| Air experience |  |  |  |  |  |  |  |
| Equipment |  |  |  |  |  |  |  |
| Convoys and trains |  |  |  |  |  |  |  |
| Fuel |  |  |  |  |  |  |  |
| Manpower |  |  |  |  |  |  |  |
| Stability and war support |  |  |  |  |  |  |  |
| Factory and dockyard commitments |  |  |  |  |  |  |  |
| Intelligence |  |  |  |  |  |  |  |
| Organizations and market |  |  |  |  |  |  |  |
| Special projects |  |  |  |  |  |  |  |
| Custom currencies |  |  |  |  |  |  |  |
| Other discovered families |  |  |  |  |  |  |  |

## Sign-off questions

1. Does every discovered voluntary payment have one row?
2. Do displayed and paid values share one source or one verified static variant?
3. Does every positive cost retain one quantum?
4. Does each refundable action return the paid amount?
5. Does each static logical action expose one variant to the player and AI?
6. Does every multi-resource action have one row per cost component and one primary achievement family?
7. Does source expiry remove only its own modifier?
8. Does every changed AI weight have a probability comparison?
9. Does every engine-inaccessible row have exact evidence?
10. Were the registry and tests updated after the final code change?
11. Did the completion auditor find any unregistered cost surface?
