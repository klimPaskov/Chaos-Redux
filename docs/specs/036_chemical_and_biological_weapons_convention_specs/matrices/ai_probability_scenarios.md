# AI probability scenarios

| Scenario | Inputs that must be declared | Surface | Expected result | Evidence class |
| --- | --- | --- | --- | --- |
| `E36_P01` Aggressive capable major | War, chemical tech, biological tech, delivery, high industry, low sanction aversion | Opening posture | Full Ratification ranks first | Exact score and normalized option share |
| `E36_P02` Peaceful restraint state | Peace, no CBRN tech, low threat, high sanction aversion | Opening posture | Reservation or Rejection above Full | Exact score and normalized option share |
| `E36_P03` Threatened minor | External threat, low industry, no payload, protection need | Opening posture | Reservation above Full and Covert | Exact score and normalized option share |
| `E36_P04` Chemical specialist | Chemical tech, no bio route, high outbreak fear | Opening posture | Chemical Accession ranks first | Exact score and normalized option share |
| `E36_P05` Secret-capable opponent | Strong intelligence, research capacity, public restraint, high secrecy tolerance | Opening posture | Covert route viable but not dominant without all factors | Sensitivity sweep |
| `E36_P06` Losing nuclear major | Evolution II, major war, nuclear payload, valid strategic target, worsening war score | Nuclear use | Use willingness rises above peace case | Score comparison with hard validity proof |
| `E36_P07` Retaliation victim | Reservation, valid hostile chemical record, payload and target | Chemical use | Retaliatory use becomes viable | Exact comparison |
| `E36_P08` Reservation aggressor | Reservation, no hostile record, otherwise valid payload | Chemical use | Offensive option weight is zero | Hard-gate proof |
| `E36_P09` Industrial project leader | Surplus civilian factories, research capacity, active project, low current share | Contributions | Industrial and research actions rank above no action | Exact score ordering |
| `E36_P10` Resource-poor minor | Small industry, low equipment reserve, valid facility, active project | Contributions | Facility or research action above equipment contribution | Exact score ordering |
| `E36_P11` Close treaty opposition | Opposition Leader, contested support, sufficient political resources | Conference influence | Organize Opposition ranks first | Exact score ordering |
| `E36_P12` Three project candidates | Three complete unique eligible provider IDs | Project selection | Each candidate receives one-third probability | Exact normalized pool |
| `E36_P13` Duplicate registration | Three unique providers and one duplicate row | Project selection | Deduplication leaves one-third per unique ID | Inspect and evaluate |
| `E36_P14` Normal availability callback | Active selected project, source unlock transaction | Project lifecycle | Cancellation is certain and completion impossible | Deterministic path proof |
| `E36_P15` Thermonuclear use | Evolution III, full member, thermonuclear payload | Use and Condemnation | No routine-use bonus and source multiplier `1.00` | Compare to non-member baseline |
| `E36_P16` Biological blowback | Evolution III, permissive policy, high friendly spread risk | Biological use | AI rejects use despite permissive policy | Sensitivity sweep |
| `E36_P17` Impossible treaty quorum | Too few eligible members and missing capability anchor | Treaty response | Sponsorship and ratification resolution cannot claim adoption | Hard-gate proof |
| `E36_P18` Planned withdrawal | Active project, AI intends withdrawal before completion | Contribution | Contribution weight falls to zero or near zero according to hard route | Exact score proof |

## Probability comparison contract

For every source patch, compare the same named scenario before and after.

The report must include:

- analyzed file and identifier
- scenario inputs
- complete option or candidate pool
- missing external factors
- raw scores
- normalized shares when valid
- hard invalidity gates
- expected ordering
- actual ordering
- revision or comparison ID
- unresolved uncertainty

Do not claim an exact normalized probability when the option pool is incomplete.
