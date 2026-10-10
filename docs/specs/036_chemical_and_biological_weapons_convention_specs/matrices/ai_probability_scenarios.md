# AI probability scenarios

AI rules are owned by [10](../10_ai_behavior_and_probability_contract.md).
Each scenario declares its inputs, the complete option pool, and any external factor the analysis cannot see.
Run them through `chaosx_ai_probability_auditor` before and after every weighted change, as `CLAUDE.md` describes.

| Scenario | Inputs | Surface | Expected result | Evidence |
| --- | --- | --- | --- | --- |
| `E36_P01` Aggressive capable major | War, chemical and biological technology, delivery, high industry | Opening response | Full Ratification first | Normalized option shares |
| `E36_P02` Peaceful restrained democracy | Peace, no CBRN technology, low threat | Opening response | Reservation or Rejection above Full Ratification | Normalized option shares |
| `E36_P03` Threatened minor | External threat, low industry, no payload | Opening response | Reservation above Full Ratification and the covert response | Normalized option shares |
| `E36_P04` Chemical specialist | Chemical technology, no biological route, outbreak fear | Opening response | Chemical Accession first | Normalized option shares |
| `E36_P05` Secret-capable opponent | Research capacity, non-democratic, public restraint | Opening response | Covert response viable but not dominant | Sweep of research capacity |
| `E36_P06` Condemned country | Formal Censure from earlier chemical use | Opening response | Full or Chemical Accession weight rises with the bucket size | Sweep of chemical bucket |
| `E36_P07` Reservation victim | Retaliation Authority against the attacker, payload, target | Chemical use | Retaliation viable | Score comparison |
| `E36_P08` Reservation aggressor | No Retaliation Authority, otherwise valid | Chemical use and policy choice | Zero for first use and for broader policies | Hard-gate proof |
| `E36_P09` Losing nuclear major | Nuclear Accord, major war, valid military target | Nuclear use | Higher than without the Accord, still zero without payload | Score comparison and hard gate |
| `E36_P10` Thermonuclear | Arsenal ratifier with a thermonuclear payload | Use | No Event 036 factor | Comparison with a non-member |
| `E36_P11` Biological blowback | Arsenal ratifier, high friendly spread risk | Biological use | Rejected despite the permissive treaty | Sweep of spread risk |
| `E36_P12` Close first-use vote | Opposition Leader, count one short of quorum | Conference actions | Organize Opposition first | Score ordering |
| `E36_P13` Industrial project leader | Surplus factories, low share | Contributions | Industrial and research above none | Score ordering |
| `E36_P14` Resource-poor minor | Low equipment reserve, facility state | Contributions | Facility or research above equipment | Score ordering |
| `E36_P15` Planned withdrawal | Active Withdrawal Notice | Contributions | Zero | Hard-gate proof |
| `E36_P16` Agenda pool after a member attack | Several eligible families | Agenda selection | Protection and Assistance Compact weighted highest | Normalized pool |
| `E36_P17` Three providers | Three unique eligible ids | Project selection | One third each | Exact pool |
| `E36_P18` Duplicate registration | Three ids plus one duplicate | Project selection | One third each | Exact pool |
| `E36_P19` Normal availability | Selected provider's proof turns true | Lifecycle | Cancellation certain, completion impossible | Path proof |

Never claim an exact probability from an incomplete option pool, and keep scores separate from probabilities.
