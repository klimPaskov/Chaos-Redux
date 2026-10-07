# Acceptance matrix

All **54 scenarios below are NOT RUN against HOI4**. They are implementation acceptance requirements. The separate Python model test result is not a pass for any engine row. JSON provides the same cases with an explicit per-row engine status.

A passing row needs the supported game build, actual source revision, exact setup, evidence source, observed outcome and reviewer disposition. A plausible script snippet or a list of expected outcomes is not a result.

| ID | Area and scenario | Setup | Required result | Required evidence |
| --- | --- | --- | --- | --- |
| T01 | Coverage: Empty ordinary map | Several eligible countries and every valid sea, all fields empty | Every pair reaches the verified ordinary cap with one 1,000 addition | Native field inventory before/after and full map coverage receipt |
| T02 | Coverage: Existing partial fields | Mix 0, 250, 995 and 1,000 for multiple owners | Additive results preserve all existing ownership and respect the native cap | Per-owner/per-region before/after inventory |
| T03 | Coverage: Raised cap | Cap 2,000 and existing amount 250 | Result is 1,250, not 2,000 and not 1,000 | Installed define and actual effect result |
| T04 | Coverage: Lower cap | Cap 750 with existing 250 | Result respects 750 and does not change the define | Installed define and actual effect result |
| T05 | Coverage: Over-cap existing data | A native field already exceeds current cap | No reduction. Unsupported additive behavior rejects before any writes | Preflight and exceptional-state proof |
| T06 | Coverage: Two enemies same sea | Opposing owners share a region | Both independent fields remain present after their additions | Owner-resolved state and hostile view |
| T07 | Coverage: Many owners same sea | Several enemies plus friendly and neutral owners | All eligible ownership is present, with native combat aggregation rather than assumed linear scaling | Multi-owner state and actual combat/tooltip behavior |
| T08 | Map: Sparse and unusual IDs | Valid regions use sparse IDs and zero where supported | Every valid ID is included once, with no arbitrary ceiling or zero exclusion | Effective map inventory and application coverage |
| T09 | Map: Added ocean region | Compatible map adds a valid remote region | New region receives every eligible contribution | Map provenance and native field inspection |
| T10 | Map: Overridden classification | Map changes a region from land to naval or naval to land | Effective classification wins and invalid land receives no call | Resolved overlay data and call inventory |
| T11 | Map: Enclosed accessible sea | Valid sea behind a restricted approach | Region covered without opening access or moving fleets | Region field state and unchanged access |
| T12 | Map: Unsupported lake or land | Non-naval lake or land-only strategic region | No native mine call to an invalid target | Validity predicate and exclusion proof |
| T13 | Map: Load-order change | Provider registry was built for different active overrides | Stale coverage rejects before consumption rather than skipping regions | Configuration fingerprint failure receipt |
| T14 | Map: Incomplete registry | Known active sea omitted from registry | Normal dispatch remains ineligible and no partial success is logged | Prefire and history/field comparison |
| T15 | Owners: Landlocked country | Compare legally supported and invalid mine ownership cases | Native legality determines inclusion without reducing region set | Owner eligibility evidence and complete region set |
| T16 | Owners: No ships or mine technology | Existing country lacks ordinary minelaying tools | No exclusion unless native effect legality actually requires it | Current effect/trigger documentation and result |
| T17 | Owners: Subjects and minor AI | Subject, small AI and human share legal capability | Same placement eligibility and amount | Owner-resolved before/after data |
| T18 | Owners: Dynamic current country | Existing dynamic tag absent from initial historical map | Included under the same native legality rule | Current tag identity and contribution receipt |
| T19 | Owners: Exile or capitulation | Compare valid and invalid ownership states | Verified native rule applied consistently | Engine behavior and eligibility explanation |
| T20 | Owners: No eligible recipients | Valid seas but C is empty | No successful incident, Chaos or mine writes | Dispatch/history/state comparison |
| T21 | Owners: No valid naval regions | Map has no valid seas | No successful incident and no invalid calls | Map and dispatch evidence |
| T22 | Lifecycle: Acknowledgment order | Human leaves report open while other viewers acknowledge | Placement completed independently and is never repeated | Event ordering and field comparison |
| T23 | Lifecycle: Duplicate direct call | Reenter after complete firing under a raised cap | No extra 1,000, history entry, Chaos or timer outcome | Before/after and state-flow evidence |
| T24 | Lifecycle: Duplicate after clearance | Clear a hostile field, then call event again | Cleared field remains cleared | Native clearance result and duplicate-call comparison |
| T25 | Lifecycle: Shared timer cluster | Cluster fires with multiple valid members | One logical timer/weight outcome, Event 088 applied once | Complete picker/cluster state trace |
| T26 | Lifecycle: Independent timers | Another country later reaches Event 088 eligibility | Global consumed state prevents another pass without resetting all recipient timers | Multi-country timer and fired-state trace |
| T27 | Lifecycle: Later cluster firing | Repeatable Sudden Abundance selected after 088 consumption | Other valid members remain eligible and 088 stays consumed | Aligned member arrays and actual pool evidence |
| T28 | Lifecycle: Save/load and reentry | Load committed state and later invoke another caller | No deposition or duplicate historical award | Native save-state and caller trace |
| T29 | Lifecycle: Legacy fired save | Old single-region version already consumed Event 088 | No automatic global refill and no invented achievement provenance | Migration and original field comparison |
| T30 | Lifecycle: Late-created owner | New legal country appears after commit | No automatic mine grant | Creation hook audit and field comparison |
| T31 | Lifecycle: Partial execution failure | Inject or reproduce failure after some pair writes | No destructive rollback, no success claim, no blind retry | Exact partial state and progress evidence |
| T32 | Lifecycle: Peace and decay | Change war status and advance under native rules | Native removal/decay is not compensated by event refill | Controlled native lifecycle comparison |
| T33 | Lifecycle: Annexation and civil war | Ownership changes after original firing | Native ownership behavior preserved without invented redistribution | Owner lifecycle and field inspection |
| T34 | Performance: Large supported configuration | Many current countries and large modded sea set | Complete synchronous coverage without omitted pairs or delayed-world advantage | Pair count, engine limits and measured execution evidence |
| T35 | Chaos: Material pass | At least one native field actually increases | Exactly +20 proposed manifestation Chaos once | Native increase proof and shared meter trace |
| T36 | Chaos: All fields already full | Complete pass produces zero increase | Consumes once with zero Chaos and honest historical result | Before/after full inventory and meter trace |
| T37 | Chaos: Subsequent sinking or war | Native loss or new war after commit | No additional Event 088 award duplicating shared systems | Chaos source ownership and trace |
| T38 | Clearance: Single owner swept | Another hostile field remains | Route not reported as fully clear for that country | Country-relative hostility and field view |
| T39 | Clearance: All relevant hostile fields swept | Qualifying native clearing under stable hostility | Operational route stays reopened against Event 088 with no refill | Mission outcome and native field history |
| T40 | Achievement: Five real clearances | Five distinct regions, two qualifying owners each, positive player removal | First achievement unlocks once with full evidence | Native attribution and framework unlock receipt |
| T41 | Achievement: Same region repeated | Repeated clear/re-lay loop in one region | Counts as one distinct region | Progress identity history |
| T42 | Achievement: Passive reduction | Mines disappear from decay, peace or owner removal | No clearance achievement progress | Causal negative test |
| T43 | Achievement: Allied-only sweeping | Player present but allies remove all mines | No player clearance credit | Removal attribution negative test |
| T44 | Achievement: Qualifying offensive | Three cleared regions, actual player landing through one, target defeat with retained beachhead | Offensive achievement unlocks once | Native operation route/attacker/target and defeat evidence |
| T45 | Achievement: Coastal land conquest | Player takes coast through land attack or peace transfer | No landing credit | Operation attribution negative test |
| T46 | Achievement: Prior landing or unrelated annexation | Landing predates clearance or target removed by other event | No offensive unlock | Ordered provenance and defeat-source evidence |
| T47 | Achievement: Test or legacy provenance | Debug placement or legacy one-region incident | No new global achievement provenance | Framework eligibility and event identity proof |
| T48 | Text: Observer country | Ineligible mine owner sees report | No claim of personal mines, fleet loss or immunity | Reviewed actual localisation and rendering |
| T49 | Text: Historical versus live detail | Months pass and fields are swept | Detail snapshot does not masquerade as current mine count | Native state and rendered shared detail |
| T50 | Assets: Report consumer | Final 210 by 176 processed report DDS | Readable mine, period fit, correct alpha and active sprite | Decoded DDS/native-size contact sheet and parent review |
| T51 | Assets: Achievement triplets | Two final 64 by 64 three-state sets | Correct same-subject completed, grey and unchanged-overlay variants | Template inspection, decoded six DDS files and registry linkage |
| T52 | Catalog: Workbook/export alignment | Current XLSX differs from old CSV and connected cluster doc | Only authorized 088 changes plus verified runtime mirror, unrelated entries preserved | Workbook diff, export diff and source text crosswalk |
| T53 | Audit: Probability and completion | Inspect full active picker/cluster pool and all changed files | Actual classified probability evidence and independent completion findings | Real tool and custom-agent receipts |
| T54 | Audit: Near-completion improvement pass | All implemented and planned surfaces compared | Actual custom planner disposition, no forced extra subsystems | Real planner output and parent disposition |

## Weighted-logic audit scenarios

Use the actual `hoi4.probability_inspect` route before choosing the full pool. Inspect Event 088 before and after consumption, Sudden Abundance with 088 eligible and consumed, event disabled, cluster disabled, unsupported map, zero legal recipients, shared mode and independent mode. Check required/optional role separately from Medium severity. Include all competitors and the real pool cadence for normalized or sequence claims.

There is no region lottery or response-choice lottery in the new design. A deterministic acknowledgment does not eliminate the need to audit the enclosing picker. Do not present a raw weight as a probability, assume the member chance is 100 percent, or claim a completed probability pass from this prose matrix.

## Evidence boundary

The parent coding agent owns the actual source and available automated checks. No automatic game launch or desktop playtest is authorized by this plan. Unperformed live validation stays explicit and is not disguised as a user instruction to perform routine testing.
