# Event 012 Gods grading arithmetic and source audit

Date: 2026-10-04.
Disposition: **blocked for helper publication; partial implementation, with accepted design retained**.
This is a bounded read-only audit of the grading tranche, not an Event 012 completion claim.
The only file written is this report.
No gameplay edit, Git operation, HOI4 launch, balance target, or design expansion was performed.

Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

## Scope, acceptance, and source identity

The accepted design is `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_full_grading_rewards_design_2026-10-03.md`, lines 4–7, 226–343.
Its recorded parent acceptance adopts unique contracts, actual contribution receipts, twelve deterministic conduct/doctrine factors, and frozen material entitlements.
The present assignment independently authorizes the corrected quantity-normalization order and single contract-enum owner.
The design remains **accepted and queued** for combined integration; this audit does not promote it to fully implemented or audit spec promotion.
The full-spec final-evaluation section, lines 1083–1165, was also read as background.

The following labels bind every line citation below to the inspected bytes.

| Label | File | SHA-256 |
| --- | --- | --- |
| E | `common\scripted_effects\012_africa_gods_grading_effects.txt` | `a8a6d34a9c95590ecbdfa09f3b0b428c4c9eef1e162a3ec93079da56fff0d3a8` |
| T | `common\scripted_triggers\012_africa_gods_grading_triggers.txt` | `8e1f3ccc7faf9bc01a7198814b148a2fac6b4f3ae3e96dc32cf032647fca64f6` |
| C | `common\script_constants\012_africa_gods_grading_constants.txt` | `a6a4f98fa7fd60c9e83a55cf62d8b3519554ce89e22ec3f048bf910766cd9365` |
| A | `common\scripted_effects\012_africa_gods_grading_effects.md` | `eb2ac605272674164ea90faa69dc8c4fb6d66b8dd11d6c0d553d6eb4c16d8e82` |
| H | `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_grading_helpers_2026-10-03.md` | `0fc027b2b33f6ac02ce3fd08dd8da550e81919756c72998e10cddf092fa14e8e` |
| D | `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_full_grading_rewards_design_2026-10-03.md` | `4bbbdefec2c092a110010bfca19965b353d75924eca138d57b5b618b896ac060` |

Dependency reads were limited to required values and owner boundaries.
The existing Gods constants hash is `b3473262a3c9bfce17218773ffea5a1bc5063336bea9b82da7b9a2511bed21f4`.
The contract-constants hash is `23e6dba1a4a20dcd10a6612888d74a8280b23ba3120c3f2008c8c1ec6836880f`.
The full-spec hash is `2ccb9fbdedb7f7715187397b6bdc31610dc0fdd7cf4e2b1388f16d7490066798`.
AGENTS.md hash is `38e479cb75828ba888860be8bc3739f9286c0d925cc7d8de5ecd3b8dadec46cf`.

Parent core wiring, quantity-receipt producers, reconciliation/conduct observation, recovery integration, native payouts, decisions, localisation, catalog alignment, and final integration remain unfinished outside this audit's ownership.
Their absence is not misreported as a missing grading-worker implementation.

## Completion status by surface

| Surface | Status | Evidence and limit |
| --- | --- | --- |
| Four grading constant groups and closure ownership | Finished within source scope | C:6–73 contains exactly four schema-first groups. The single closure group is in contract constants:2–10, with `war_breach = 5`; the inspected contract callers use that key. |
| First-genuine ledger initializer | Finished helper contract; caller integration unverified | E:5–112 consumes caller temp authorization, rejects an existing issued field including zero, and preserves existing ledger on re-entry. It must precede contract initialization. |
| Ten-kind quantity normalizer | Finished for accepted denominators/bound | E:128–150 uses the corrected exact scale, caps before the quantity multiply, and preserves one man. This is not a guarantee for arbitrary utility parameters. |
| Actual quantity snapshots and subset validation | Finished source structure; producers unverified | T:12–161 requires all forty nonnegative quantity fields and all thirty subset-to-total inequalities. E:189–228 copies exact suffixes; all forty normalizer input/denominator pairings were checked. |
| Freeze accounting and derived inputs | Blocked | F1 applies to every otherwise authorized freeze; F3 leaves count arithmetic without a range proof. E:152–546. |
| Four-standing/doctrine/recovery predicates | Finished source rule mapping; integrated evidence partial | T:188–327 matches the accepted matrix. Isolated predicate scenarios pass; a successful complete native-safe freeze is not established. |
| Settlement entitlements | Blocked | F2 exceeds native range before caps or zero multipliers; F4 loses accepted formula precision. E:548–612. |
| Replay and one-use guards | Finished source guard structure; combined transaction unverified | E:178–179 via T, E:538–545, and E:554–555 preserve existing snapshots/entitlements. Parent cleanup, obligation receipts, and delivery remain outside scope. |
| Helper API and worker validation handoff | Partial/stale | F5 identifies obsolete arithmetic/owner descriptions and a historical five-decimal, range-unbounded fixture claim. |
| MCP lifecycle/comparison evidence | Blocked/partial | Focused inspect/render defer helpers; artifact reads fail provenance; baseline comparison is unavailable. Exact results below. |
| Assets, GUI, animations, portraits, 3D, super-events | No new surface in this tranche | D:452–458 and A:163–167 reuse existing presentation. No new asset or event-UI-worker handoff is required here. |
| Weighted AI/probability | No in-scope surface | Deterministic grading/reward multipliers are not selection weights. Existing decision AI remains parent-owned. |

## Arithmetic standard and validation limits

The audit uses the parent-required signed three-decimal representation: integer milli-units from -2,147,483,648 through 2,147,483,647, representing -2,147,483.648 through 2,147,483.647.
Every native stored arithmetic result must fit this range.
Intermediate overflow is a defect even when a later division, zero multiplier, or final ceiling would produce a small value.

The read-only ephemeral source checks parsed the actual helper files through H's published AST interpreter, with each stored result additionally truncated toward zero to 0.001 and range-checked.
Caller-owned temporary outputs and conservative helper-frame cleanup were retained.
The parent's history and standing-enum validators remained explicit external fixture boundaries.
No test files were written.

Range violations stop the audit model.
This does **not** assert that HOI4 throws an exception or establishes its exact wrapping/saturation outcome.
Manual source arithmetic independently establishes the out-of-range intermediates.
Precision findings use the required three-decimal truncation model.
Installed documentation confirms fixed-point arithmetic and the variable operators, but does not specify all native rounding details.
The offline wiki's five-decimal/large-whole-number claim conflicts with the supplied native contract and is not used to certify range safety.

All full-freeze fixtures with ordinary small counts encounter F1.
Standing/recovery checks therefore use explicitly declared valid frozen inputs as an isolated boundary.
Those checks cannot establish end-to-end freeze, entitlement, receipt, or native delivery completion.

## Findings and required owner corrections

### F1 — Blocking: emergency PP arithmetic still creates 8,000,000 intermediates

E:468–476 prepares `gods_of_africa_grade_work_emergency_pp_cap` as 16000 × 500, then divides by 1000.
The multiplication stores **8,000,000**, above 2,147,483.647.
It executes even when `gods_of_africa_grade_emergency_paid_pp = 0`.
Source cases with PP 0, 500, and 8000 all stop at that exact field in the bounded audit model.

A second unsafe step remains at E:473.
Even if the cap were safely computed as 8000 PP, the current multiply-before-divide conversion can store 8000 × 1000 = **8,000,000** before dividing by 500.
Bounding final emergency credit to 16000 does not protect either intermediate.

Owner action: compute the exact PP-to-milli scale first, 1000 / 500 = 2, obtain the PP cap as 16000 / 2 = 8000, and scale the bounded paid PP once.
Recheck PP 0, 0.001, 500, 8000, and the highest representable positive ledger value.
The required 500 PP → 1000 emergency milli and zero material/voluntary/campaign credit must remain unchanged.

### F2 — Blocking: equipment/fuel entitlement arithmetic overflows before division and caps

E:597–600 starts from contribution **milli-packages**, multiplies by 1000 equipment/package, then by B, and only then divides by 1000.
At C = 16, the first stored result is **16,000,000**.
The mathematical maximum of the following multiply is **60,000,000** for reciprocal Favored B = 3.75.
The accepted raw equipment formula itself is at most **60,000**, then capped to 50000.

E:604–607 has the same unnecessary scale for fuel.
Its first mathematical intermediate is **8,000,000**, followed by at most **30,000,000**, although raw fuel is at most **30,000**, then capped to 25000.
The strict source model stops at the earlier equipment violation, so the fuel defect is separately established from its source order.

The issue occurs well below the contribution ceiling.
`contribution_milli = 2148` already makes the equipment first multiply 2,148,000.
The accepted consistent donor C = 10 would first store 10,000,000 before reaching its intended 32500/16250 entitlement.
Respected and even zero-multiplier Distrusted/Enemy with substantial past material also execute the unsafe first multiply before B takes effect.

E:557–558 creates both durable entitlement fields at zero before calculation.
Their existence then prevents replay recalculation under E:554–555.
This makes trustworthy arithmetic and publication of the completed pair necessary before relying on one-use guards.

Owner action: cancel the equal milli/package and equipment/package factors algebraically while retaining fractional milli contribution.
With a correctly represented B, equipment can use `C_milli × B` and fuel `C_milli × B × 0.5`, with maxima 60000/30000 before ceilings.
Do not first quantize C to whole or three-decimal packages and lose small contributions.
Recheck all four standings, zero M, the accepted donor examples, floors, and ceilings after the precision correction in F4.

### F3 — Range-proof gap: contract sums and percent comparisons accept inputs that overflow

T:14–51 checks presence and nonnegativity, but establishes no upper bound for counters used by E:155–162 or E:299–308.

A consistent valid count record with issued = fulfilled = full_original = 21475, retired = failed = refused = war closures = 0 passes the endpoint accounting equations.
E:300 then stores `gods_of_africa_grade_fulfilled_percent_numerator = 21475 × 100 = 2,147,500`, outside native range.
No caller maximum was proved in this bounded assignment.

For integer counters the largest safe multiplicands are:

| Product | Last safe count | First unsafe count |
| --- | ---: | ---: |
| 100 × F | 21474 | 21475 |
| 80 × N | 26843 | 26844 |
| 90 × N | 23860 | 23861 |
| 50 × N | 42949 | 42950 |

Malformed but individually representable nonnegative inputs also overflow before they can be rejected.
For example, fulfilled = 1,100,000 and failed = 1,100,000 store terminal sum 2,200,000 at E:158 before the invariant comparison.
Full_original = honored_substitute = 1,100,000 similarly overflow `gods_of_africa_grade_work_paid_closures` at E:162.

Issued-minus-retired itself is safe for representable nonnegative inputs, since its difference remains within the signed range.
The unchecked additions and percent products are the gaps.

Owner action: protect validation sums before addition and provide an exact range-safe ratio implementation or a proved owner-side admissible-count bound.
Preserve the uncapped historical ledger, the exact 80/90/50 percent boundaries, and unresolved disposition for inconsistent evidence.
A gameplay cap or approximate ratio is not accepted by this audit.

### F4 — Precision defect: the early Respected multiplier truncates the accepted reward formula

E:559–561 stores S at three decimals; E:590–592 separately stores `0.75 × S`.
Even integer Strength produces nonrepresentable four-decimal products at odd values.

For Strength 1, S = 0.010.
The exact B is 0.2575, but the three-decimal source sequence stores 0.007, then B = 0.257.
For an isolated valid Respected reward input M = 2, V = L = 0, the current source stays within range and returns **514 equipment / 257 fuel**.
The accepted formula gives floor(2000 × 0.2575) = **515 equipment**, with the same 257 fuel.

At Strength 33 and the same contribution, source returns **994/497** versus accepted **995/497**.
Strength 80 is the control: source and design both give **1700/850**.
At C = 16 the multiplier error alone would cost 8 equipment at odd integer Strength, but current C = 16 execution is already blocked by F2.

Fractional Strength can additionally lose precision during the early /100 at E:561.
No integer-only Strength guarantee or permission for this economic rounding simplification was supplied.

Owner action: carry a scaled or rearranged reward numerator with enough precision through the calculation and apply the intended integer floor at the end.
Recheck odd and fractional Strength, sub-package contributions, reciprocal multipliers, and floor boundaries.
The small difference is still a deviation from the accepted exact formula.

### F5 — Documentation and validation claims need reconciliation

A:132 still says the grading constants file owns `gods_of_africa_contract_close`; current C:4 delegates it to contract constants.
A:138 explicitly describes multiplying paid quantity twice before division, although current E:141–148 first computes a scale and then multiplies the capped quantity once.
Following the obsolete description would reproduce the parent's corrected overflow.

H:4 and H:183–185 still describe the duplicate category as the current publication blocker, while H:419–425 correctly records its removal and `war_breach` alignment.
H:13 also retains the obsolete category inventory.
Those historical statements need a clear current disposition.

H:91 and H:298 model five-decimal truncation without native range checking.
H's seventeen passing cases are historical source-model evidence, not native arithmetic proof for the current bytes.
H:427–431 correctly asks for this independent review, but the lead completion language and API range claims have not yet incorporated F1–F4.

Owner action: synchronize the API's actual operation order, category ownership, admissible utility-input limits, and current validation disposition after correcting arithmetic.
Keep the historical worker hashes and result provenance, while linking the current bounded audit and later re-review.

## Complete arithmetic inventory

| Source operation family | Stored intermediate bound or issue |
| --- | --- |
| E:5–112 initialization and authorization consumption | Zero/one assignments; no arithmetic amplification. Existing-issued guard protects re-entry. |
| E:114–126 round-and-correct floor | Within intended entitlement domain 0–50000, nearest rounding can produce at most 50000; subtract-one correction implements floor. Arbitrary near-native-limit utility inputs are not certified. |
| E:141–148 normalization scale and cap | 1000 × 1000 = 1,000,000; exact accepted scales and caps below. Output ≤16000. |
| E:155–156 eligible count | Difference of representable nonnegative counts is safe; negative N rejected. |
| E:157–162 terminal/fulfilled-kind sums | F3: sums computed before consistency/range rejection. |
| E:169–298 snapshots, array lengths, conduct flags | Copies/count reads without multiplicative amplification; receipt truth, array uniqueness, and observation freshness remain parent-owned. |
| E:299–308 percent cross-products | F3: no counter range proof. |
| E:309–310 derived bound | 16 × 1000 = 16000, safe and exact. |
| E:313–467, 478–529 four ten-kind accumulators | Each normalized term ≤16000; accumulator ≤16000 after each clamp; pre-clamp addition ≤32000. |
| E:468–476 emergency PP | F1: 16000 × 500 and capped 8000 × 1000 both reach 8,000,000. Intended final term ≤16000 and post-addition ≤32000. |
| E:530–532 exceptional sum | Three bounded aggregates sum to at most 48000, safe. |
| E:559–561 Strength | Clamp 0–100, divide to 0–1; range safe, fractional precision limit in F4. |
| E:562–571 contribution premiums/cap | Each premium ≤8000; contribution before clamp ≤32000; 16 × 1000 cap = 16000. Accepted quantity quanta keep the half-premiums representable. |
| E:572–595 B and ceilings | B ≤3.75 Favored, ≤1 Respected, zero otherwise; coefficients and ceilings fit range, but F4 affects exactness. |
| E:597–608 payout arithmetic | F2: 16m/60m equipment and 8m/30m fuel mathematical intermediates before cancellation. |
| E:602–610 floor/output copies | Final intended ceilings fit range; prior arithmetic defects prevent certification. |

The accepted normalizer's divisions are exact at three decimals for every kind:

| Kind | Denominator | Scale = 1,000,000 / denominator | Cap in thousands = 16000 / scale |
| --- | ---: | ---: | ---: |
| Infantry | 1000 | 1000 | 16 |
| Support | 500 | 2000 | 8 |
| Trucks | 100 | 10000 | 1.6 |
| Artillery | 50 | 20000 | 0.8 |
| Armor | 25 | 40000 | 0.4 |
| Aircraft | 50 | 20000 | 0.8 |
| Fuel | 1000 | 1000 | 16 |
| Convoys | 20 | 50000 | 0.32 |
| Trains | 20 | 50000 | 0.32 |
| Manpower | 10000 | 100 | 160 |

One man is 0.001k × 100 = **0.100 milli-package**, exactly representable.
A denominator-sized actual payment gives 1000 milli for every kind.
The highest native-representable positive quantity saturates to 16000 for every kind.
The uncapped actual snapshot remains a separate retained quantity.
Saturation preserves the accepted 1/2-package standing thresholds and the 16-package reward ceiling.

## Standing, ledger, and manual source cases

The twelve-factor mapping is present in T:188–327 and E's frozen inputs.
Wrath is strictly below 40 for Favored, strictly below 70 for Respected, and strictly above 80 as one Enemy cause.
Current war, owned/controlled host cores, actual unresolved treaty/major offense, opt-out, live defiance, or three applicable refusals have Enemy priority.

| Doctrine | Favored F / ratio / current and longest streak | Additional positive gate | Respected adverse ceilings |
| --- | --- | --- | --- |
| Reciprocal | 2 / 80% / 2 | V≥1, E≥1, L≥1, verified return, or F≥4 | Failures and refusals each <2 |
| Exaction | 4 / 90% / 4 | V+E+L≥2 or F≥6 | Each <2 |
| Ambiguity | 3 / 80% / 3 | V+E+L≥1 or F≥5 | Each <3 |
| Unchosen | 3 / 80% / 3 | Same Favored gate as ambiguity | Each <2 |

All Favored paths additionally require M≥2, zero applicable failures, and no Enemy cause.
Respected additionally requires the positive 50%-with-F≥1 contract path or exceptional aid/verified return.
Prior defiance, war, occupation, or treaty breach requires actual accepted reconciliation and post-acceptance recovery: two fulfillments/current streak two for Respected; four/current streak four plus zero post failures/refusals for Favored.
Lifetime ratio/history remain retained; accepted reconciliation changes the applicable adverse record, not the lifetime denominator.
The recovery producer is not independently validated here.

| Case family and concrete fields | Source result / limit |
| --- | --- |
| Ten denominators, ordinary package, one man, maximum native quantity | All standalone normalizer source cases match the exact table and 0.100 one-man result. E:128–150; C:30–45. |
| All 30 voluntary/emergency/campaign subsets above corresponding total | Each is rejected by T:132–161; overlapping subsets are independently bounded, not required to be disjoint. |
| Forty snapshot suffixes and forty quantity-kind normalization pairs | Every total/voluntary/emergency/campaign kind uses its actual same-kind field and denominator. E:189–228, 314–528. |
| N=issued−retired=terminal sum; F=original+substitute | Exact equations at E:155–167. Inconsistent records are unresolved when validation arithmetic is representable; oversized invalid sums are F3. |
| Zero N and no positive evidence | Isolated frozen predicate gives Distrusted; no positive ratio gate. E:285–289; T:247,259,274,315. |
| Zero N with E=1, M=V=L=0 | Isolated predicate can give Respected through aid; standalone entitlement gives 0/0 for zero material. Full PP-based freeze remains F1-blocked. |
| Reciprocal 4/5 versus 3/4 | Favored versus Respected with otherwise valid M/streaks. T:242–253. |
| Exaction 9/10 versus 8/9; exceptional 2 versus 1.999 at F=4 | Favored versus Respected in each threshold pair. T:254–265. |
| Ambiguity and unchosen F=3 with exceptional 1 versus 0.999 | Favored versus Respected; current/longest streak three required. T:266–280. |
| Two failures, F=2/N=4 | Ambiguity Respected; unchosen Distrusted. T:292–320. |
| Reciprocal F=2 with V=1, E=1, L=1, or one return separately | Each positive alternative qualifies when M=2 and both streaks satisfy two. Current or longest streak one blocks Favored. |
| Each of four prior-hostility flags | Without acceptance Distrusted; accepted post-fulfillment/streak 1/2/4 gives Distrusted/Respected/Favored when other gates hold. T:188–229. |
| Accepted recovery with one new post failure or refusal | Favored blocked; otherwise eligible Respected retained. T:215–218, 292–320. |
| Each current Enemy flag/core cache, and Wrath 40/70/80/80.001 | Current causes give Enemy. Wrath boundaries give Respected/Distrusted/Distrusted/Enemy for the declared otherwise-valid fixture. |
| PP 0/500/8000 full-freeze attempts | All encounter the 8,000,000 cap intermediate; intended 500 PP→E=1 is not an end-to-end passing case. |
| C=16, all four standing enum values | Isolated entitlement source encounters 16,000,000 before B/caps; no capped native-safe payout is established. |
| Respected M=2, Strength 1/33/80 | Source 514/257, 994/497, 1700/850; accepted 515/257, 995/497, 1700/850. |
| Floor 6562.499/6562.500/6562.999, 50000, 0.001 | Standalone floor helper returns 6562/6562/6562, 50000, 0. Conservative caller-preinitialized output survives return. |
| Existing issued field zero and re-entry | Initializer does not reset retained quantity, even when initialized flag is absent. E:11–12. |
| Already frozen inputs or either existing entitlement field | Source replay does not change the snapshot or existing entitlement and does not fabricate the missing second field. E:538–545, 554–555. |
| Coarse action/history, promises, host gifts, PP/material distinction | Grading reads actual quantity fields, not coarse aid/compliance/history rows. Producer qualification and actual paid receipts remain outside scope. |

No PP/native equipment/fuel grant exists in the grading entitlement helper.
Its persistent writes are the two entitlement variables.
It does not create source, owed, delivered, outcome, diplomacy, or reward-granted receipts.
This limited ownership is correct, but it cannot validate the unfinished parent transaction.

## Read-only references and MCP evidence

Working connected reference/source routes: `hoi4.reference_context`, `reference_search`, `reference_read`, and `source_lookup`.
The source-lookup schema supports line bounds and revisions, but exposes no `view/keyPath` interface in this session.
No unsupported structure paging was attempted.

| Read reference | Exact span / revision |
| --- | --- |
| Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | Math Expressions 184–215 read through MCP; fixed-point arithmetic, not a precision/range specification. Revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`. |
| Installed `common\script_constants\documentation.md` under that root | 1–34 through MCP: schema first, int/fixed_point, supported access. Revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`. |
| Installed `documentation\effects_documentation.md` | 3587–3594 divide, 5012–5018 multiply, 6476–6485 round, all through MCP. Revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`. Round documentation gives no tie rule; the tested round-then-correct floor is robust to ordinary nearest tie choices in its intended domain. |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | Variables 425–434 through MCP. Revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`. Its five-decimal/large-range assertion conflicts with this assignment's native contract. |
| Vanilla `common\scripted_effects\zz_debug_effects.txt`, `d_add_fake_armies` | Source lookup 72–86 shows temporary multiply/round/clamp structure; no gameplay copied. Index revision `a516eeb4e2f730fe2bdf9f642d0cdb46b7b4ad731a432b9199b1e8957c88858b`. |
| Current `gods_of_africa_normalize_paid_quantity_milli` | Source lookup E:128–150, one definition, not overridden/shadowed, same index revision `a516eeb4e2f730fe2bdf9f642d0cdb46b7b4ad731a432b9199b1e8957c88858b`. |

The event reference-context bundle returned omitted Triggers, Scopes, On actions, and Localisation headings.
It is not claimed as complete detailed coverage.
Only the arithmetic/constants sections needed for this read-only grading assignment were read through targeted routes.
There was no online Paradox wiki access.

The parent supplied `.603` lint/render as partial, helpers deferred, artifact provenance unavailable, and comparison pending.
No new broad/helper lifecycle graph was requested to repeat that work.
The required read-only event routes were exercised on the existing settlement report `chaosx.nr12.608`, depth 1, one selected node, no helper expansion; trace used maxEdges 1.
The initial depth-zero requests were rejected by live validation and corrected to the minimum depth one.

Inspect returned `EVENT_INSPECTED_PARTIAL`; render returned `EVENT_RENDERED_PARTIAL`.
Both use focused revision `6b9a6428e7573efc5012d443d97c822ff503dfc95bfa7688d849b8093c88c733`, graph hash `953f84b7e8b2fb596118e7f28ad466f155a09346e53965d72ebc77f93411ad36`, and zero helper projections.
The results explicitly defer whole-workspace helper projections/lifecycle passes.
Inline source inventory was truncated to 64 of 388 paths.
Global indexed diagnostic counts are not grading-specific findings.

Returned artifacts:

- Trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/410c539fc92454de6125859ceb8853150542a16751f80d9a2dcf4d072786d35b/84525b794b314b8bc1986739485b62b0116e6ed662cac76f07c06876200343b4/event-trace-6b9a6428e757.json`.
- Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9670e2134ca77d7b9a86c55c6f42cccecbcc5283267eccb31047bdb466d138b/3c076470d36996960d8d0fc78997fe210e48c0ec9f329827557a2429adb9ff4b/event-options-6b9a6428e757-manifest.json`.
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73a0a79b7a1ce9dc29496357b8e70b81b001f60880018cf544e8bf4a769b1f13/dc4740129831a7bee09f6a5b2a994a289f3ca03d82b968de22c6cd6ab0707a78/event-options-6b9a6428e757.png`.

Bounded reads of the trace (offset 0, length 2048) and render manifest (offset 0, length 4096) both failed with **MCP -32603: Artifact provenance manifest is unavailable**.
The artifact links/hashes are retained as returned identities; artifact contents and image acceptance are not claimed.

Compare requested the worker's retained baseline revision `828ca59a9a1fa1a44d0bf5a12bce75e5cb65e717d2d055388d5ac1994d71fe92` with the same one-node report selection and rendering disabled.
It returned **EVENT_REVISION_NOT_CACHED: Requested event graph revision is not cached or retained as a graph artifact**.
No before/after comparison exists from this audit.

`hoi4.script_validate` is not exposed.
No connected health/version or native-task negotiation was verified, so the exposed helper_expansion enum was not used.
These exact limitations prevent helper lifecycle/engine evidence claims; manual/source checks do not replace them.
No probability route is required for this deterministic tranche; affected decision AI still requires the parent's separate `chaosx_ai_probability_auditor` pass when integration reaches that surface.

## Simplifications, omissions, and next actions

No audit-side gameplay simplification, fallback, new weight, asset, or mechanic was introduced.
The source's F4 early rounding is an unapproved arithmetic approximation, not an accepted design change.
No mapped doctrine gate or quantity kind was found missing in the bounded helper source.
Missing parent implementation and integrated evidence remain explicitly outside the worker's completed surface.

The parent should correct F1 and F2 before publishing or integrating the helpers, address F3's validation/ratio range proof and F4's precision loss, then reconcile F5.
Request a bounded re-review against the corrected file hashes.
Rerun the zero/500/8000 PP cases, one-man case, exact denominator table, counter boundaries, odd/fractional Strength, all four standing outcomes, accepted donor/ceiling examples, and replay protections.
Record successful complete freeze-to-entitlement cases separately from isolated predicates.

Parent integration must preserve the initializer order, genuine-history authorization, actual receipt/conduct producers, neutral terminal accounting, frozen host capability, immutable source/owed records, and native donor-backed delivery.
Those owners require their own audits and meaningful scenario evidence after implementation.
The accepted plan remains queued until those owners and mandatory evidence are resolved; no global goal completion is claimed.

Skills applied: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, and `chaos-redux-event-planning`, with relevant bounded sections read.
No skill was created or changed.
Asset, GUI, 3D, and live-playtest skills were not applicable to the owned grading files.

---

## Independent F1–F5 re-review — 2026-10-04

Current disposition: **bounded source arithmetic ready for qualified helper publication; native/full-feature completion remains unproved**.
The original audit and its F1–F5 findings above are retained as the historical pre-repair snapshot.
This append is the current disposition for the repaired bytes below.
Only this audit report was modified by the re-review.
No gameplay, API, handoff, Git, AI hook, native payout, or game-launch action was performed.

### Important qualification of the original arithmetic language

The three-decimal / 2,147,483.647 representation is a **conservative source-audit contract only**.
It is not an independently established ordinary-variable or getter storage limit.
References in the original audit to “native overflow” must therefore be read as violations of that supplied model, not proof of the engine's actual width, precision, overflow behavior, or exception behavior.
The historical arithmetic concerns remain legitimate reasons to construct a safer algorithm.

Installed `documentation\script_concept_documentation.md:184–215` confirms fixed-point math but does not specify a complete ordinary-variable representation.
Its revision is `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:425–434`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, describes five decimals and a wider whole-number range.
Neither modifier-specific three-decimal guidance nor deprecated plain-manpower getter behavior proves the representation of every normal variable.
This native-documentation gap remains explicit.

### Current source identities

All new citations use these current labels rather than the earlier E/T/C/A hashes.

| Label | File | SHA-256 |
| --- | --- | --- |
| E2 | `common\scripted_effects\012_africa_gods_grading_effects.txt` | `22daba90392a7df952c00fdf23816d2fc779e6d51b7762494b3409fb407f99f0` |
| T2 | `common\scripted_triggers\012_africa_gods_grading_triggers.txt` | `c4623d33abe32544d41f253d973e6de9d682cf64e05ca29c0a6cb56061364f77` |
| C2 | `common\script_constants\012_africa_gods_grading_constants.txt` | `eabc3b784fae4a857c08791e35dd6d80875657f9c100376840bb95d46eb84533` |
| A2 | `common\scripted_effects\012_africa_gods_grading_effects.md` | `87693ec601cf052b73a16eb95c21914b27b43fd743cf429ee3c36bad063260bd` |
| R2 | `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_grading_arithmetic_repair_2026-10-04.md` | `4542e125552a0416bc72f626d7e52f7521523444388098766c9c84d4300c4ff1` |
| H2 | `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_grading_helpers_2026-10-03.md` | `d81b23caf4e7c65073fd49debdee1064d1d34d6f589af04a35e0b26607adc364` |

The accepted-design and AGENTS.md hashes still match the original audit.
The pre-append audit hash was `a983860ff0cebcb070bf7cca69b6574644047a2e08ae6ced14c239a3cf6c7d6c`.
R2's claimed 216543 additional passing cases were read as worker evidence; this re-review does not adopt that number as its own validation.

### F1–F5 disposition

| Finding | Current result | Evidence / remaining qualification |
| --- | --- | --- |
| F1 emergency PP | Resolved within the audit domain | E2:568–578 computes scale 2, cap 8000, then multiplies bounded PP once. Independent complete-freeze cases pass for 0, 0.001, 500, 8000, and 2147483.647. Actual PP remains unchanged; M/V/L and zero-material reward remain zero. |
| F2 entitlement overflow/publication | Resolved within the audit domain | E2:177–208 uses base-100 splitting; E2:698–708 completes both temporary components before publishing. No 16m/60m/8m/30m cross-product remains. Either one-field partial pair repairs correctly; a both-present pair is immutable. |
| F3 sums and ratio arithmetic | Resolved within the declared count domain; broader acceptance remains qualified | E2:213–264 checks residual headroom before subtraction. E2:152–175 computes exact required F without a large percent product. T2:12–139 also imposes the count-validation domain discussed in R1 below. |
| F4 reward precision | Resolved under tested positive truncation models | Raw Strength rational coefficients in E2:660–694 preserve the accepted formula. Integer/fractional Strength, sub-package values, and floor-boundary neighborhoods agree with an independent exact-rational oracle at three and five decimals. Engine semantics remain unverified. |
| F5 stale ownership/order/provenance | Original stale descriptions resolved; count-domain wording still needs qualification | A2:144–160 matches current ownership and normalizer/PP order; A2:173–209 documents rational arithmetic and the model gap. H2:4–7 and 91–102 clearly distinguish current repair from historical fixtures. A2:79 and R2:186 must not be read as proof that no gameplay eligibility restriction exists. |

No additional arithmetic mismatch was found in the supported domain.
The seven effects include directly consumed `gods_of_africa_required_fulfilled_count` and `gods_of_africa_floor_scaled_entitlement`.
The fourteen standing/history triggers and four schema-first grading groups remain present.
No asset, GUI, portrait, animation, 3D, super-event, or weighted AI surface was added by these helpers.

### R1 — Remaining qualification: the assumed maximum is also a real grading eligibility gate

C2:8–9 defines `maximum_integral_count = 2147483`.
For each of eighteen count/cache fields, T2:12–139 copies the original to scratch, clamps scratch to that maximum, rounds scratch, and requires equality with the untouched original.
Thus this is both an integer-integrity check **and an upper eligibility bound**.
It does not clamp or reset the historical normal field.

Independent alternative-wide five-decimal source case:
issued = fulfilled = full_original = current/longest streak = **2147484**, with an otherwise consistent ledger and positive cooperation.
The validation scratch becomes 2147483, equality fails, freeze remains unresolved, no standing is selected, and the original 2147484 values remain intact.
This alternative model demonstrates source behavior if wider values are representable; it does not establish actual engine support for those values.

The gate is acceptable as a disclosed fail-closed restriction of this bounded audit contract.
It cannot yet be certified as merely rejecting unrepresentable native data, because the engine's actual limit was not proved.
In a wider engine it would exclude otherwise integral, consistent history from final grading.
Therefore “not a history cap” is accurate only in the sense of **no historical-field mutation**.
It is not equivalent to “no gameplay restriction.”

Qualified source-helper publication may retain this documented domain.
Full native/no-simplification acceptance needs authoritative representation evidence, a proved reachable-count bound, or an explicit accepted design disposition for the restriction.
No such broader acceptance is inferred here.
The parent should describe the upper eligibility bound plainly in the API/current handoff rather than relying on categorical “no gameplay cap” language.

### Independent arithmetic proof and intermediate inventory

**Contract accounting.**
For nonnegative validated integral fields, N = issued − retired stays inside the conservative signed magnitude range.
Each terminal subtraction requires residual ≥ that terminal count; failure prevents all later subtractions.
Success requires final residual zero.
The fulfilled-kind equation is checked by F − full_original = honored_substitute after proving F ≥ full_original.
Neither malformed 1100000 + 1100000 sum is formed.
The historical counters are retained unchanged.

**Exact ratios.**
For integral N, write N = 100q + r, with 0≤r≤99.
Then `ceil(pN/100) = pq + ceil(pr/100)`.
This is exactly equivalent to 100F≥pN for integral F.
At N=2147483, q=21474 and r=83.
The required counts are 1717987 at 80%, 1932735 at 90%, and 1073742 at 50%.
T2:338,350,365,407 all compare F with the correct new required-count fields.
Zero N retains its separate state and positive-denominator gates.

**Accepted reward equivalence.**
For raw clamped Strength s and contribution milli c:

| Standing | Exact equipment expression | Fuel |
| --- | --- | --- |
| Favored, nonreciprocal | floor(c × (50+s) / 50) | Double the denominator |
| Favored, reciprocal | floor(c × 5(50+s) / 200) | Double the denominator |
| Respected | floor(c × (100+3s) / 400) | Double the denominator |
| Distrusted / Enemy | 0 | 0 |

These equal the accepted 1000CB and 500CB expressions before standing ceilings.
There is no stored early S or rounded B.

**Base-100 floor.**
Let c=100q+r, a=D/100, u=q×coefficient, f=floor(u/a), and v=u−fa.
Then `floor(c×coefficient/D) = f + floor((100v+r×coefficient)/D)`.
q is integral, so u, fa, and 100v are exactly representable on both tested decimal grids.
Only r×coefficient can lose sub-grid precision.
Since the other summand and each integer-floor threshold kD are on the same grid, downward truncation cannot move the numerator across a threshold.
At exact equality the product is itself grid-representable.
Positive quotient truncation also preserves its integer floor.
This proves equivalence for the declared positive truncation semantics; it is not proof of unobserved engine rounding rules.

| Intermediate family | Bound / result within the conservative contract |
| --- | --- |
| Actual/count scratch and snapshot copies | Retain their supported input magnitudes; model maximum actual value tested 2147483.647. |
| Count-validation rounding | Scratch is clamped to integral 2147483 before rounding; near-max fractions reject without rounding above that model bound. |
| Residual accounting | Differences stay in range; guarded terminal residuals stay nonnegative. |
| Ratio quotient, reconstructed 100q, pq, tail pr | q≤21474; 100q≤2147400; pq≤1932660; pr≤8910. |
| Final required fulfilled count | ≤1932735. |
| Quantity normalizer | Scale-construction intermediate 1000000; converted term≤16000; pre-clamp aggregate addition≤32000. |
| Emergency PP | Scale 2; cap 8000; converted term≤16000; material-plus-PP emergency pre-clamp≤32000. |
| Exceptional sum / contribution premiums | Exceptional sum≤48000; each half-premium≤8000; contribution pre-clamp≤32000 and final c≤16000. |
| Raw Strength / rational coefficient / D/100 | s∈[0,100]; coefficient≤750; D/100∈{0.5,1,2,4,8}. |
| Reward q and u | q≤160; u≤120000; the initial numerator-b copy also reaches 120000 before residual subtraction. |
| Reward residual/tail after subtraction | v<a≤8; 100v<800; r×coefficient<75000; completed tail numerator<75800. |
| Uncapped reward / published standing ceilings | ≤60000 equipment / 30000 fuel; Favored 50000/25000, Respected 10000/5000, others zero. |

The numerator-b bound below 75800 applies **after** residual/tail construction.
Its earlier source copy of u can be 120000; that remains safe.
This distinction is included so the inventory covers every stored intermediate rather than only final expressions.

### Independently executed source cases

A separately authored ephemeral evaluator parsed the current Clausewitz files and executed assignments, trigger-side scratch operations, conditionals, and helper calls.
It used exact rational arithmetic for calculations, applied truncation and magnitude checks at every stored result, and discarded helper-created temporary outputs unless their caller owned storage.
Parent history eligibility and final-standing enum validation remained explicit external fixture boundaries.
No fixture or tool script was written to disk.

The seventeen original named families were re-executed with this evaluator and passed.
Additional independently selected cases comprised **3076 checks at three decimals and 4342 at five decimals**, for **7418**.
These include whole freeze/classification/entitlement paths and separately identified arithmetic utility boundaries.
They do not duplicate or claim the worker's 216543-case total.
The five-decimal pass uses an alternative precision model while retaining the conservative magnitude budget; the one wider-range case is isolated to R1.

| Same-case family | Current concrete result |
| --- | --- |
| PP 0 / 0.001 / 500 / 8000 / 2147483.647 | E milli 0 / 0.002 / 1000 / 16000 / 16000; actual PP retained; no material or PP-based physical entitlement. |
| F=N=21475 | Complete freeze succeeds in the model; required F 17180 / 19328 / 10738 for 80/90/50; historical F remains 21475. |
| F=N=1000000 / 2000000 / 2147483 | Exact ratio fields and complete reward calculation; no historical counter cap/reset. Maximum-domain 90% requirement is 1932735. |
| Threshold F−1 / F / F+1 | Old cross-product boundaries and million-scale N agree exactly with integral ceil comparisons. |
| Two 1100000 terminal counts or original/substitute counts; retired>issued | Unresolved before unsafe arithmetic; actual fields retained. |
| All eighteen count/cache fields at 0.001, 1.999, 2147483.647 | 108 malformed-field checks across the two models reject without changing historical inputs. |
| All thirty subset>total cases | Rejected; total/voluntary/emergency/campaign kinds remain correctly paired. |
| Forty material snapshots plus raw emergency PP | All **41** same-suffix pairs verified; all forty normalizer input/denominator pairs verified. All 41 maximum-domain actual values remain uncapped in snapshots. |
| One man | 0.001k gives 0.100 milli; no early whole-package rounding. |
| N=0, no conduct/material | Distrusted and 0/0; no perfect ratio. N=0 with genuine positive aid can still take the accepted exceptional Respected path. |
| Respected M=2, Strength 1 / 33 / 80 | 515/257, 995/497, 1700/850, matching the accepted formula. |
| Respected M=2, Strength 0.001 / 33.333 / 99.999 | 500/250, 999/499, 1999/999; full freeze-to-entitlement paths agree with exact-rational floors. |
| Fine five-decimal Strength | Includes 0.00001, 0.99999, 33.33333, 99.99999, with fine-grid floor neighborhoods and whole-path oracle comparisons. |
| Integer-floor boundaries | Tested grid values immediately around exact rational thresholds, before source quantization, for all nonzero coefficient families and equipment/fuel denominators. No floor mismatch found. |
| Accepted donor/weak/low-contribution/high Favored anchors | 32500/16250, 17500/8750, 13125/6562, 50000/25000 retained. |
| Respected raw 13125/6562 | Arithmetic utility retains these raw values; accepted Respected ceilings correctly produce 10000/5000. |
| High material, Distrusted or Enemy | 0/0 through the complete path without the old large cross-product. |
| One existing entitlement field, either side | A nonzero partial field is recomputed to the completed 32500/16250 pair; both-present replay remains immutable after Strength changes. |
| Frozen inputs, re-entry, existing issued field zero | No existing historical reset; source freeze/entitlement replay protections remain intact. |
| Four doctrines, twelve factors, hostility/recovery | Original matrix, strict Wrath boundaries, lifetime ratios, accepted-reconciliation barriers, post-counter/streak requirements, and PP/material exclusions pass the re-executed original families. |

### MCP, documentation, assets, and remaining ownership

A current narrow `hoi4.source_lookup` found the new scaled-entitlement helper as one non-overridden/non-shadowed definition.
Index revision: `669a9ad00120f961896461aba9dcc8fff61f7ed2611a7d0578a3718284e7089d`.
The returned excerpt covered E2:177–198 with a line/column continuation; the complete E2:177–208 body was independently read from source.
The installed fixed-point section was read again through `hoi4.reference_read`.
These working read-only routes establish source access, not native arithmetic execution.

The existing original/repair `.603/.608` focused event evidence is retained.
No duplicate event graph was requested for this same-chain source re-review.
R2:169–181 records the repair's `.608` inspect/render revisions, deferred helper/lifecycle coverage, provenance-read failure, and comparison failure.
The exact outstanding MCP gaps remain:

- `-32603: Artifact provenance manifest is unavailable`.
- `EVENT_REVISION_NOT_CACHED: Requested event graph revision is not cached or retained as a graph artifact`.
- `hoi4.script_validate` unavailable in the exposed catalog.
- Unverified connected health/version and client native-task negotiation; no helper-expansion/native-task proof.

The new source checks do not clear those gaps.
No new presentation asset or event-owned GUI is introduced.
The deterministic coefficients remain outside AI/probability auditing; future parent decision AI hooks retain their separate probability-auditor requirement.

A2 and H2 now correctly document category ownership, safe normalization order, utility call sites, partial-pair repair, and historical-versus-current evidence.
The count-domain wording qualification in R1 remains necessary.
No new broad design gap or event expansion is recommended.

### Current handoff to the parent

**Ready:** the bounded helper arithmetic, integer-floor equivalence, supported-domain source cases, unchanged accepted standing matrix, actual-field mapping, and one-use/partial-pair behavior.
**Partial/qualified:** F3's broader native-domain acceptance and F5's categorical “not a gameplay cap” wording.
**Blocked/unproved:** actual ordinary-variable representation and native rounding behavior, MCP helper/lifecycle/comparison evidence, and all unfinished parent receipt/core/recovery/native-delivery integration.

Publish these helpers only with the supported-domain and R1 qualifications carried forward.
Do not mark the full native goal or accepted event plan complete from this re-review.
Parent integration remains separately queued under the recorded accepted design.
The parent should reconcile R1's API wording and obtain the missing native/domain disposition while completing its own owners and validation.

Skills applied remain `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, and `chaos-redux-event-planning`.
No skill was changed.

---

## Narrow R1 modulo correction re-review — 2026-10-04

Current disposition: **R1 upper-eligibility restriction resolved in source**.
The count-cap qualification from the preceding re-review is removed for the current patch.
Bounded source-helper readiness remains established; engine width/precision, native execution, MCP lifecycle/comparison evidence, and parent integration remain unproved.
This is not acceptance of the rejected eligibility-cap fallback.
The earlier audits remain intact as historical snapshots.
Only this audit report was written during this re-review.

### Current identities and bounded change

| File | SHA-256 |
| --- | --- |
| `common\scripted_triggers\012_africa_gods_grading_triggers.txt` | `4f378fb730da12f5a8f0b70bbe8b7096f496ec2fab29c8bdc183ffe9e2846464` |
| `common\script_constants\012_africa_gods_grading_constants.txt` | `4938c7e7b8682d36084dd72af38a6e02b060abcea2792c88fa0f4b8a71526a15` |
| `common\scripted_effects\012_africa_gods_grading_effects.txt` | `22daba90392a7df952c00fdf23816d2fc779e6d51b7762494b3409fb407f99f0` |
| `common\scripted_effects\012_africa_gods_grading_effects.md` | `92ff2bb3fa4260bf10379f778c90d34033f118c3d35f65c6abd96bbe9f834e01` |
| `docs\plans\012_africa_plans\subagent_handoffs\012_africa_gods_grading_arithmetic_repair_2026-10-04.md` | `aadcce17002ec130a73da48046e4fed7387d0bd81a76144f91a570d4f1a1dc76` |

The effects file is byte-identical to the preceding reviewed repair.
The new trigger validator, lines 12–123, keeps each field's existence and nonnegative checks.
All eighteen integer checks now copy the actual field to `gods_of_africa_grade_count_integral_work`, apply `modulo_temp_variable` with divisor `constant:gods_of_africa_value.one`, then require scratch zero.
There is no clamp or round in that validator, and no `maximum_integral_count` key in current grading constants.
The validator writes temporary scratch only.
It does not alter historical normal fields or invent receipt counts.

### Documented modulo route and evaluator semantics

Live `hoi4.reference_search` and `hoi4.reference_read` independently confirmed and read:

| Installed reference | Read span | Revision |
| --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 6442–6454, `modulo_temp_variable`, any scope, explicit `var`/`value` form and temporary-variable mutation | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation\effects_documentation.md` | 4986–4998, matching effect form | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |

Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:555–572` also describes temporary variable operators as valid triggers and modulo as a division remainder.
Its revision remains `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.

The independent AST evaluator was extended with this documented `var`/`value` modulo operation.
It models modulo as the parent's confirmed neutral-true trigger side effect; the subsequent explicit zero comparison supplies the integer predicate.
The installed excerpts independently establish the trigger route, mutation, and argument shape; no live game execution or observed return-value test is claimed.
No synthetic LoopScope, gameplay loop, or scope-changing operation was introduced.
No modulo syntax, argument, or source-flow blocker was found.

For a present nonnegative value x, x modulo 1 is its fractional remainder.
The remainder lies in [0,1) and is zero exactly for an integral x under the tested fixed-point models.
The operation does not round x upward or compare it with an assumed numeric maximum.
Copying a representable input to scratch does not enlarge it; the remainder is smaller than one.
Negative inputs are rejected by the retained nonnegative guard before their modulo result could qualify.

### Independent same-case results

The evaluator executed **180 integer-validator checks**: ten value/model combinations on every one of the eighteen count/cache fields.
Parent history eligibility and final-standing enum validation remain explicit fixture boundaries, as in the preceding review.
Each check verified both the boolean result and unchanged actual normal fields.
The wider-range cases are explicitly alternative models, not statements about native engine width.

| Input / model | All eighteen integer checks | Actual history |
| --- | --- | --- |
| 0, conservative three-decimal model | Accept | Unchanged |
| 0.001 | Reject, remainder 0.001 | Unchanged |
| 1.999 | Reject, remainder 0.999 | Unchanged |
| -1 and -0.001 | Reject through nonnegative guard | Unchanged |
| 2147483.647, three/five-decimal models | Reject, remainder 0.647 | Unchanged |
| 2147483.00001, five-decimal model | Reject, remainder 0.00001 | Unchanged |
| 2147484, alternative wider five-decimal model | Accept, remainder zero | Unchanged |
| 5000000, alternative wider five-decimal model | Accept, remainder zero | Unchanged |

Complete freeze/classification/entitlement source cases also passed:

| F=N | Model | Required F at 80% / 90% / 50% | Result with the declared compliant donor inputs |
| --- | --- | --- | --- |
| 21475 | Conservative | 17180 / 19328 / 10738 | Favored; 50000 equipment / 25000 fuel |
| 1000000 | Conservative | 800000 / 900000 / 500000 | Same |
| 2000000 | Conservative | 1600000 / 1800000 / 1000000 | Same |
| 2147483 | Conservative | 1717987 / 1932735 / 1073742 | Same |
| 2147484 | Alternative wider five-decimal | 1717988 / 1932736 / 1073742 | Same; formerly excluded R1 case now succeeds |
| 5000000 | Alternative wider five-decimal | 4000000 / 4500000 / 2500000 | Same; no replacement upper gate |

Those donor fixtures use the same positive material and sustained cooperation as the preceding bounded tests.
Every actual historical field was retained.
The unchanged ratio decomposition produced exact `ceil(pN/100)` requirements.
Larger results were evaluated against the declared alternative representation budget, not silently accepted by an unbounded-float model.

Additional complete-path checks confirmed:

- Fractional issued values 0.001, 1.999, and 2147483.647, and negative issued -1, remain unresolved without an outcome or entitlement.
- Every one of the eighteen missing count/cache fields remains missing and prevents freeze; no history is backfilled.
- Zero history remains Distrusted with 0/0 entitlement and the separate no-contract-history flag.
- The malformed 1100000+1100000 terminal and original/substitute records are rejected through the unchanged guarded residual arithmetic.
- All seventeen original named case families pass again with the independent modulo-aware evaluator, including doctrine/recovery, reward precision, actual quantities, and replay cases.

The prior 7418 additional arithmetic cases were not rerun for this narrow validator-only patch.
Their effects source hash is unchanged.
The new same-case checks and seventeen-family rerun establish the relevant regression coverage; they do not claim native execution.

### Documentation disposition and remaining limits

The API's parent correction at lines 234–241 and repair handoff's parent correction at lines 899–906 explicitly supersede the old scratch-maximum description.
The earlier numeric-domain proof and worker fixture claims remain historical evidence for the previous trigger hash.
The embedded worker evaluator predates modulo support; it is not adopted as current-patch execution evidence.
This independent evaluator includes modulo and supplies the current results above.

**Removed:** the source-imposed 2147483 upper eligibility bound and its near-maximum rounding step.
**Retained:** field presence, nonnegative/integral receipt validation, uncapped historical fields, exact ratios, guarded residual accounting, accepted standing matrix, and immutable completed entitlement behavior.
**Still unproved:** actual ordinary-variable width/precision and native runtime behavior, unavailable MCP artifact/comparison/scope-validation evidence, and unfinished parent receipt/core/recovery/native delivery integration.

No new full event graph was requested.
The existing partial/deferred helper evidence, provenance-unavailable errors, revision-not-cached comparison, and absent `hoi4.script_validate` route remain as previously recorded.
There is no new AI/probability, asset, or GUI surface.

The parent does not need to accept an eligibility-cap fallback for this current validator.
The R1 source restriction and associated wording qualification are resolved by its removal and the explicit superseding notes.
Source-helper readiness remains separate from native validation and the queued parent integration.
No global goal completion or publication action is claimed.
