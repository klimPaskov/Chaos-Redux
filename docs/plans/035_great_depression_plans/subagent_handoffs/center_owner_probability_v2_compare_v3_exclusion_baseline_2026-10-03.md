# Event 35 v2 weighted-change comparison and v3 permission baseline

Status: source-level fixture arithmetic and permission-gate audit complete. MCP analyzer evidence remains unavailable in the child context; no numeric analyzer result or normalized probability is claimed. No gameplay source was edited.

## Frozen inputs and source identities

The immutable before-source remains `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\035_great_depression_effects_before.txt`, SHA-256 `02B6C5708BE053957CADB2C60AC476927929B17DE1FB5BA90958A8281FF61106`. The v1 fixture remains unchanged at SHA-256 `5539B8D4DCB64DB32D9EC3252953D5B684E4A517C45A9F3643A20B4D65256E1D`.

The v2 fixture used for the owner-reference and first-valid-candidate comparison is `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\scenarios_v2.json`, SHA-256 `F348094B23CD57F16C067DB32C5C7F4BD2E6CE780145E3C6B4808346743C63C3`. Its seven IDs and bytes are unchanged.

The complete v3 fixture is `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\scenarios_v3.json`, SHA-256 `2C92489F1C2764C729096B2FF88505A3E8F653D204E6F92F76B1627B4134BF66`. It preserves all seven v2 IDs and adds the four requested permission cases. The file already existed in the shared tree; I reviewed it and removed the inherited-seed marker from the live-forbidden and frozen-forbidden candidate cases because the Event 34 companion would not pass those candidates as `industrial_boom_inherited_region`. The v3 file is fixture-only domain data, not a claimed MCP scenario schema.

The current constants file `common\script_constants\035_great_depression_constants.txt` is SHA-256 `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7`; all score weights and penalties are unchanged. The live effects source was SHA-256 `6549B92D2BDB30CC5060F9CE33B45E8A967ED88E1C730DE0180DF9ED8751159F` at the targeted read. Shared-file hashes are point-in-time identities; findings below are limited to the named source blocks.

## v2 comparison: owner scope and first-valid acceptance

The after-source uses `is_owned_by = PREV.PREV` inside `any_neighbor_state` at line 1344. Its initial selector acceptance condition first checks `great_depression_center_candidate_saved = 0` at line 1688, then retains the score-greater-than and equal-score/smaller-state-ID conditions at lines 1689–1693. The industry, infrastructure, population, capital, and adjacency coefficients remain `4`, `2`, `1`, `-16`, and `-10`; the invalid-score sentinel remains `-1`, and the state-ID sentinel remains `100000`.

The table is explicit source arithmetic from the complete v2 fixture and unchanged constants. It is not MCP output.

| Scenario ID | Immutable before-source scores and selection | Current after-source scores and selection | Source-level change |
|---|---|---|---|
| `CTR35-ROOT-ACTOR` | 1: 520; 2: 525; selects 2 | 1: 520; 2: 525; selects 2 | No score or winner change. |
| `CTR35-ROOT-DIFFERENT` | 1: 530; 2: 525; selects 1 | 1: 520; 2: 525; selects 2 | The actor-owned center now applies the existing -10 adjacency term; winner changes 1 → 2. |
| `CTR35-FOREIGN-ROOT-NEIGHBOR` | 1: 520; 2: 525; selects 2 | 1: 530; 2: 525; selects 1 | The foreign ENG center no longer applies that term; winner changes 2 → 1. |
| `CTR35-NO-CENTER-NEIGHBOR` | 1: 530; 2: 525; selects 1 | 1: 530; 2: 525; selects 1 | No score or winner change. |
| `CTR35-CAPITAL` | 1: 514; 2: 525; selects 2 | 1: 504; 2: 525; selects 2 | Capital penalty remains -16; the corrected actor-owned adjacency test adds -10. |
| `CTR35-TINY-CAPITAL` | 1: -7; no candidate saved | 1: -7; selects 1 | No score delta; first-valid acceptance now saves the sole valid candidate. |
| `CTR35-NEGATIVE-TIE` | 1: -1; 2: 6; selects 2 | 1: -1; 2: 6; selects 2 | No raw-score or final-winner change; the first candidate is accepted before state 2 supersedes it. |

The v2 pool has no equal-score candidate pair. `CTR35-NEGATIVE-TIE` tests equality with the initial sentinel, not a tie between candidates. The lower-ID tie-break remains in source, but this fixture does not demonstrate an equal-score candidate-to-candidate tie. These deterministic rankings are not willingness scores, timing distributions, or normalized probabilities.

## v3 exclusion baseline on the immutable before-source

In `great_depression_register_initial_centers`, the inherited-region seed checks only event-target presence, owner, controller, core, and passability at immutable before-source lines 1561–1567. It then inserts that state into the actor registry and sets its center flag at lines 1583–1608. The availability pass at lines 1628–1644 and the score-candidate pass at lines 1667–1683 likewise lack checks for the live conversion-forbidden flag and an already center-flagged state outside the current actor array. The scorer only checks whether neighboring states are centers; it does not validate the candidate's own state permission.

The companion contract is narrower and explicit. In `common\scripted_effects\034_industrial_boom_collapse_handoff_effects.txt`, the frozen snapshot stores the exact source state and its ID at lines 211–213, snapshots the live conversion-forbidden flag at line 276, and copies the snapshot state ID and frozen flag into the region-call context at lines 296–300. The inherited state event target is supplied separately at lines 311–313. The handoff filter rejects live and frozen forbidden states and permits a center flag only when its episode ID matches the receiving actor's active episode at lines 317–330.

`common\scripted_effects\035_great_depression_region_effects.txt` rechecks the live forbidden flag, the frozen call flag, and the same-episode center exception at lines 735–749, then checks current center-array membership at line 753. Its SHA-256 at review was `2A58A6A5D94B4DB1E4D4E506CC4E8EFAEA78D14BD67560161408276A04760FA3`; the Event 34 handoff file's SHA-256 was `AA8DC3A071992AB0285AADB3DA796781641451B00C3784EAB5F828EE82F7C5C5`.

The v3 fixture's new candidate pools use the same state score inputs, so state 1 scores 530 and state 2 scores 525 when neither receives an adjacency term. Under the before-source main selection path, `CTR35-FORBIDDEN-PRIMARY+validother` and `CTR35-ALL-RESERVED-OR-FORBIDDEN` can select forbidden state 1; `CTR35-RESERVED-OTHER-EPISODE+validother` can select state 1 even though its center episode is 34 while the receiving actor is in episode 35. `CTR35-FROZEN-FORBIDDEN-CLEARED-LIVE` declares snapshot state ID 1, region-call state ID 1, recipient source state ID 1, frozen/call-forbidden true, and live state-forbidden false. The before-source generic candidate gates ignore that frozen recipient proof and can select state 1 over valid state 2.

The frozen-forbidden v3 case is a generic candidate-pool case, not an inherited seed. The Event 34 companion does not pass a frozen-forbidden state as `industrial_boom_inherited_region`; v3 therefore does not assert that the companion-prohibited target reaches the seed path. The main seed block still lacks its own permission guard as source fact, but the known companion gate prevents that specific Event 34 route from supplying a forbidden seed under these declared facts.

The permission contract for the owner patch is to apply the same test before seeding, availability counting, and score selection: reject a live conversion-forbidden state; reject a frozen conversion proof only when the call-forbidden flag is true and the recipient source state ID exactly matches the Event 34 snapshot state ID; reject a live center already claimed by another episode, while allowing only an explicit inherited seed from the same receiving episode; and honor current actor registry membership. The new viable-center-pool gate should reject an empty permitted pool before map-state mutation. Do not exclude any other state merely because a source ID was mentioned in a frozen receipt.

This is bounded source inference over the immutable before-source and the declared v3 inputs. The v3 JSON parsed with all 11 expected IDs and the required state, flag, episode, registry, and adjacency fields. Candidate-pool completeness is explicit for the fixture; outer caller reachability and live game behavior remain unobserved.

Where the center episode metadata is unknown or inapplicable, v3 keeps the optional value at -1; that sentinel is not treated as a reason to exclude the state.

## MCP boundary and handoff

The child probability-route gap remains as previously recorded: the before-source inspect call returned `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`, resource-template discovery timed out twice during startup, and refreshed `ALL_TOOLS` had no probability routes. I did not retry the route, per the instruction not to block this source handoff on another long timeout. No v2 or v3 fixture was translated into a live `scenarioSet`, and no analyzer compare/evaluate/sweep artifact, comparison ID, scenario hash, or render exists.

For future parent-side work, compare before and after with the identical v2 fixture for the owner/first-valid changes and the identical v3 fixture for the state-permission patch, using only the live MCP schema to translate each fixture. Keep the current arithmetic and source findings separate from analyzer evidence. V2 and v1 fixtures, the immutable before-source, and earlier handoffs remain preserved. This report is the only new file written by this auditor; no gameplay source was edited, staged, or committed.
