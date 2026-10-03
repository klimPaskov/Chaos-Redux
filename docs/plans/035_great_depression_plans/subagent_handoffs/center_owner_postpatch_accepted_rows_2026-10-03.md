# Event 35 post-patch source comparison and accepted rows

Status: source-only post-patch comparison complete. The required native probability compare remains unresolved because no analyzer result has returned; accepted rows below are deterministic source eligibility, not native probabilities.

## MCP status

The parent first called `mcp__hoi4_agent_tools__hoi4_probability_inspect` on the immutable before-source with workspace `mod_chaos_redux_ea3b2d67c2c0`; it timed out after 600 seconds with `isError: true`, text `tool call error ... timed out awaiting tools/call after 600s`, and no artifact. The identifier-specific retry used the same source path plus `source.identifier = "great_depression_score_center_candidate"` and the same workspace; it also completed with `isError: true`, exact text `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: timed out awaiting tools/call after 600s`, and no artifact. Cell 90 is now terminal; cell 87 had already completed and closed. No handles remain running, and I did not duplicate either call. These parent domain-call timeouts are distinct from the child's earlier inspect-unavailable-to-model result and its two approximately 120-second resource-template startup handshakes. Mandatory inspect and adapter discovery never returned, so no native `probability_compare` can be made or safely constructed from the unknown v3 scenario schema. No analyzer comparison ID, scenario hash, source revision, artifact, or render exists.

## Source and fixture identities

The immutable before-source is `docs\plans\035_great_depression_plans\audit_inputs\center_owner_2026_10_03\035_great_depression_effects_before.txt`, SHA-256 `02B6C5708BE053957CADB2C60AC476927929B17DE1FB5BA90958A8281FF61106`. The current constants remain SHA-256 `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7`.

V2 remains `scenarios_v2.json`, SHA-256 `F348094B23CD57F16C067DB32C5C7F4BD2E6CE780145E3C6B4808346743C63C3`. V3 remains `scenarios_v3.json`, SHA-256 `2C92489F1C2764C729096B2FF88505A3E8F653D204E6F92F76B1627B4134BF66`; all 11 scenario IDs and bytes are unchanged in this turn.

## Current permission helper and owned call sites

The after-source helper is `great_depression_new_center_state_is_permitted` in `common\scripted_triggers\035_great_depression_triggers.txt`, lines 57–73. It rejects any live `great_depression_center`, rejects the live `industrial_boom_region_conversion_forbidden` flag, and rejects the exact candidate state whose ID equals `industrial_boom_snapshot_region_state_id` when the receiving country has the Event 34 caller type and frozen conversion-forbidden flag. The final check is exact state-ID equality; it does not exclude arbitrary mentioned IDs.

The helper is called before the core-pool preflight candidate gates, inherited-region seed at effects lines 1563–1570, availability count at lines 1631–1644, and scored candidate pass at lines 1671–1683. `great_depression_has_viable_center_pool` applies the helper at trigger lines 41–55. `great_depression_start_or_deepen` rejects a new inactive country when that pool is empty at effects line 3500, before `great_depression_initialize_new_crisis` begins state setup. Active deepening does not call the new-center selector; it runs the inherited-region preflight/commit path. The region companion retains its explicit same-episode merge condition at `common\scripted_effects\035_great_depression_region_effects.txt` lines 746–749, so existing active centers remain mergeable.

The v3 frozen case maps to the helper's Event 34 caller branch through the actual source contract: `industrial_boom_prepare_collapse_request` sets `great_depression_call_caller_type = industrial_boom_collapse` at `common\scripted_effects\034_industrial_boom_collapse_handoff_effects.txt:51`; v3 declares the exact snapshot/call/recipient state ID as 1 and the frozen/call-forbidden flags as true. The live state flag is false. No extra fixture schema key was invented to make the caller type fit.

## Accepted source rows for the unchanged v3 fixture

`acceptedSourceRows` means the state IDs that pass the new permission helper and the fixture's complete legacy owner/controller/core/passability/population/industry/registry gates. It does not mean a selected winner, a score, or a probability. V2 and v3 scores remain deterministic maximum-score comparisons with the existing ID tie-break.

| Scenario ID | acceptedSourceRows | Source interpretation |
|---|---|---|
| `CTR35-ROOT-ACTOR` | `[1, 2]` | Both candidate states are unflagged and otherwise eligible. |
| `CTR35-ROOT-DIFFERENT` | `[1, 2]` | The center flag is on neighbor state 3, not either candidate. |
| `CTR35-FOREIGN-ROOT-NEIGHBOR` | `[1, 2]` | The foreign flagged neighbor is not a candidate. |
| `CTR35-NO-CENTER-NEIGHBOR` | `[1, 2]` | Both candidates are unflagged and eligible. |
| `CTR35-CAPITAL` | `[1, 2]` | Capital affects score, not permission. |
| `CTR35-TINY-CAPITAL` | `[1]` | The candidate remains permitted despite its -7 score; first-valid selection accepts it. |
| `CTR35-NEGATIVE-TIE` | `[1, 2]` | The sentinel tie does not change permission; state 2 still outranks state 1. |
| `CTR35-FORBIDDEN-PRIMARY+validother` | `[2]` | State 1 has the live conversion-forbidden flag. |
| `CTR35-RESERVED-OTHER-EPISODE+validother` | `[2]` | State 1 is flagged as a center for episode 34 while the receiver is in episode 35. |
| `CTR35-ALL-RESERVED-OR-FORBIDDEN` | `[]` | State 1 is live-forbidden and state 2 is already center-flagged; the core-pool preflight rejects before new-center mutation. |
| `CTR35-FROZEN-FORBIDDEN-CLEARED-LIVE` | `[2]` | State 1's live flag is false, but its exact Event 34 snapshot/recipient ID is 1 and frozen/call-forbidden proof is true. |

For v2, the source arithmetic from the immutable before-source to the current after-source remains: `CTR35-ROOT-DIFFERENT` changes state 1 from 530 to 520 and winner 1 to 2; `CTR35-FOREIGN-ROOT-NEIGHBOR` changes state 1 from 520 to 530 and winner 2 to 1; `CTR35-CAPITAL` changes state 1 from 514 to 504 with winner 2 unchanged; `CTR35-TINY-CAPITAL` stays -7 but changes from no saved candidate to state 1; the other three winners remain 2, 1, and 2 respectively for ROOT-ACTOR, NO-CENTER-NEIGHBOR, and NEGATIVE-TIE. These are fixture arithmetic, not analyzer results.

## Bounded current-scope block hashes

These SHA-256 values hash each named block's UTF-8 text after LF-normalizing its line breaks. They identify the reviewed scope blocks without treating concurrent whole-file changes as certainty.

| Source block | Current lines | CurrentScopeBlockSHA-256 |
|---|---:|---|
| `great_depression_new_center_state_is_permitted` in `035_great_depression_triggers.txt` | 60–73 | `9E5350F103FBC7AEBCCAA97326DED50CF87982BC8DD5E0A1337485D37E19DF86` |
| `great_depression_has_viable_center_pool` in `035_great_depression_triggers.txt` | 41–55 | `BC7F393F1AB99BC6C2D776554188226FBAC9E0415CBF647A2CECDE840171DBD9` |
| `great_depression_score_center_candidate` in current effects | 1322–1350 | `054A3126ABBA51D18568E68B50A1AF162F2DD18EE1BC9FBBBB1F9D535DC9B90B` |
| `great_depression_register_initial_centers` in current effects | 1525–1748 | `990BCBD77A5D4F5DF4EE580BDBE55282F2FE7269B9EF020BEC773B5B50745332` |
| `great_depression_start_or_deepen` in current effects | 3482–3616 | `1F02CF47E53583EF549ADC12815DFFCB8BE2A61819F5160CCA1FCB743872199F` |
| `great_depression_preflight_inherited_region` in region effects | 947–960 | `4CC11B8F77B77BEFB28A5DD1D023B6086444B6731CD49D68B7712797704BEC96` |

The corresponding immutable before-source block hashes are `F0101A4F550E91227F76D1E21DEB06394EF629FFA46472DB0FBA402DCA02F416` for `great_depression_score_center_candidate`, `24348A883941E2F4DCDA0964216EBE7D02DB42AE95FE75D77F4730A88F4B5849` for `great_depression_register_initial_centers`, and `7BD7F450734340FF0BB5469C00168893D5A6B0BFA83751B4722E5FF00EA18E3B` for `great_depression_start_or_deepen`. The permission helper did not exist in the immutable effects snapshot and has no before block or before call sites.

## Analyzer boundary and handoff

The mandatory post-patch `hoi4.probability_compare` has not completed. The parent inspect timed out, and the parent-owned narrower inspect retry is still running on cell 90. I did not call or duplicate that route. No numeric analyzer score, normalized probability, comparison ID, scenario hash, or rendered artifact is available. The 11 `acceptedSourceRows` are source permission results only.

Use the same v2 bytes for the owner/first-valid source comparison and the same v3 bytes for the permission-patch before/after compare, translating only through the live MCP schema when the parent retry returns. V1, v2, v3, and the immutable before-source remain byte-preserved. No gameplay source or fixture was edited in this turn, and nothing was staged or committed.
