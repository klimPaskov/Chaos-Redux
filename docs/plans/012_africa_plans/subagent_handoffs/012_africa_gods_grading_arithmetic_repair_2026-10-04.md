# Event 012 bounded grading arithmetic repair

Date: 2026-10-04.
Disposition: **implemented bounded source repair; independent parent arithmetic re-review and combined publication pending**.
Acceptance basis: the explicit bounded F1-F5 repair assignment, preserving the accepted matrix/formulas in `012_africa_gods_full_grading_rewards_design_2026-10-03.md` (SHA-256 `4bbbdefec2c092a110010bfca19965b353d75924eca138d57b5b618b896ac060`).
Audit input is `012_africa_gods_grading_audit_2026-10-04.md`, findings F1-F5; that read-only report is preserved.
Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
No inherited context, Git operation, game launch, AI/decision/world source edit, parent recovery/core/contribution edit, or external tool modification was performed.
Only the five assigned files and this explicitly permitted companion handoff were written.
Other agents' shared-tree work was preserved; MCP graph revisions may include their concurrent changes and are not a repository-wide freeze.

## Files changed and exact source identities

| Owned file | Before SHA-256 | Current SHA-256 |
| --- | --- | --- |
| `common/scripted_effects/012_africa_gods_grading_effects.txt` | `a8a6d34a9c95590ecbdfa09f3b0b428c4c9eef1e162a3ec93079da56fff0d3a8` | `22daba90392a7df952c00fdf23816d2fc779e6d51b7762494b3409fb407f99f0` |
| `common/scripted_triggers/012_africa_gods_grading_triggers.txt` | `8e1f3ccc7faf9bc01a7198814b148a2fac6b4f3ae3e96dc32cf032647fca64f6` | `c4623d33abe32544d41f253d973e6de9d682cf64e05ca29c0a6cb56061364f77` |
| `common/script_constants/012_africa_gods_grading_constants.txt` | `a6a4f98fa7fd60c9e83a55cf62d8b3519554ce89e22ec3f048bf910766cd9365` | `eabc3b784fae4a857c08791e35dd6d80875657f9c100376840bb95d46eb84533` |
| `common/scripted_effects/012_africa_gods_grading_effects.md` | `eb2ac605272674164ea90faa69dc8c4fb6d66b8dd11d6c0d553d6eb4c16d8e82` | `87693ec601cf052b73a16eb95c21914b27b43fd743cf429ee3c36bad063260bd` |
| `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_grading_helpers_2026-10-03.md` | `0fc027b2b33f6ac02ce3fd08dd8da550e81919756c72998e10cddf092fa14e8e` | `d81b23caf4e7c65073fd49debdee1064d1d34d6f589af04a35e0b26607adc364` |

This new handoff records its own executable fixture text as evidence; its final hash is returned separately, since embedding a self-hash changes that hash.
The source hashes above bind the arithmetic case results, not a native engine run.

## Completed F1-F5 repairs and API changes

All seven effect helpers remain boolean `= yes` calls in participant COUNTRY scope, with no `$...$` parameters.
Existing outer initialization/freeze/entitlement helper names and parent entry points are unchanged.
The fourteen standing/history triggers retain the accepted Enemy/Favored/Respected/Distrusted matrix, doctrine bands, Wrath boundaries, unique-receipt/streak requirements, recovery barriers, and enum values.

| Surface/helper | Exact inputs | Outputs, side effects and call sites |
| --- | --- | --- |
| `gods_of_africa_full_grade_ledger_is_present` | Complete actual ledger; eighteen integral actual count/cache fields; fractional actual PP remains allowed. | Copies each count to scratch `gods_of_africa_grade_count_integral_work`, applies modulo one, and requires remainder zero. Called by freeze authorization; no numeric eligibility cap or normal historical write. |
| `gods_of_africa_freeze_final_grade_inputs` | Existing proven host/history and complete authorized ledger. | F3 computes N = issued - retired and successively subtracts fulfilled, failed, refused and war closures only with residual headroom. Any failure skips later subtractions and leaves unresolved/unfrozen. F - full_original must equal honored_substitute after proving nonnegative subtraction. New scratch fields are `gods_of_africa_grade_work_residual` and `gods_of_africa_grade_work_consistent`; existing `grade_work_paid_closures` is now a residual, not a sum. Source and frozen history stay uncapped. |
| New `gods_of_africa_required_fulfilled_count` | Caller-owned unscoped temps `gods_of_africa_ratio_eligible` (integer 0-2147483) and `gods_of_africa_ratio_percent` (80, 90, 50), with `gods_of_africa_ratio_required_output` preinitialized. These are required inputs, not a generic invalid-input recovery API. | Output `ceil(percent*N/100)` via N = 100q+r. Private scratch `gods_of_africa_ratio_quotient`, `ratio_remainder`, `ratio_tail`, and caller-local floor input/output. Four freeze call sites publish the exact requirements. |
| Emergency PP conversion inside freeze | Frozen actual paid PP 0-2147483.647. | F1 first computes `gods_of_africa_grade_work_emergency_pp_scale = 1000/500 = 2`, cap = 16000/2 = 8000, bounds a temporary copy of PP, then multiplies once. Only E increases; M/V/L remain unaffected, actual PP snapshot unchanged. |
| New `gods_of_africa_floor_scaled_entitlement` | Caller-owned unscoped `gods_of_africa_entitlement_contribution_milli`, `entitlement_coefficient`, `entitlement_denominator`; preinitialized `gods_of_africa_scaled_entitlement_output`. Domain is C_milli 0-16000 and the rational coefficient/D table below. | F2/F4 returns exact integer `floor(C_milli*coefficient/D)` using base-100 splitting. No cap or durable write. Two direct call sites inside entitlement, for equipment D and fuel 2D. Local scratch fields: `gods_of_africa_entitlement_quotient`, `entitlement_remainder`, `entitlement_tail`, `entitlement_denominator_a`, `entitlement_numerator_a`, `entitlement_remainder_a`, `entitlement_numerator_b`, and floor input/output. |
| `gods_of_africa_calculate_settlement_entitlement` | Unchanged valid frozen grade and existing four-standing enum, now requiring an incomplete entitlement pair rather than both fields absent. | Raw clamped frozen Strength is retained; no early S or B. Computes equipment/fuel in `gods_of_africa_entitlement_equipment_completed` and `entitlement_fuel_completed`, applies integer standing ceilings, then publishes only the completed pair to existing `gods_of_africa_reward_{equipment,fuel}_entitlement`. Both-present replay is immutable; a one-field partial pair is repairable. No source/obligation/outcome/delivery flags changed or native grants. |

New durable private fields are exactly `gods_of_africa_grade_ratio_reciprocal_required_fulfilled`, `gods_of_africa_grade_ratio_exaction_required_fulfilled`, `gods_of_africa_grade_ratio_ambiguity_required_fulfilled`, and `gods_of_africa_grade_ratio_respected_required_fulfilled`.
These replace the old `gods_of_africa_grade_fulfilled_percent_numerator` and four `grade_ratio_*_denominator` products.
Actual F is the already existing `gods_of_africa_grade_demands_fulfilled`.
The three Favored doctrine comparisons in `gods_of_africa_full_grade_favored_doctrine_is_valid` and the Respected ratio comparison in `gods_of_africa_full_grade_respected_is_valid` were all changed consistently.
Repository consumer search found no other engine-facing consumers of those private old fields.
No parent call-site signature changes are required; utilities must retain caller-preinitialized unscoped output storage when called independently.

## Constants, ownership, migration and cleanup

The grading constants file still owns exactly four schema-first categories: `gods_of_africa_grading`, `gods_of_africa_contribution_units`, `gods_of_africa_reward_units`, `gods_of_africa_reward_scale`.
`gods_of_africa_contract_close` belongs only to the untouched contract constants owner, whose actual `war_breach = 5` was read.
No duplicate closure category or changed price exists in this repair.
The parent's precomputed normalizer scale/order correction is retained; its accepted domain is the ten denominators and bound 16000, not arbitrary positive utility inputs.
The API and original handoff were updated for this ownership, arithmetic order, incomplete-pair contract, utility domains, and current evidence status.
The original seventeen five-decimal/range-unbounded fixture results and historical worker hashes are explicitly historical, not current certification.

Current integer validation uses modulo one; the earlier `maximum_integral_count` key was removed by the parent correction below.
New fixed-point reward keys: `arithmetic_split_base = 100`, `favored_coefficient_base = 50`, `favored_denominator = 50`, `reciprocal_coefficient_multiplier = 5`, `reciprocal_denominator = 200`, `respected_coefficient_base = 100`, `respected_coefficient_strength_multiplier = 3`, `respected_denominator = 400`, `fuel_denominator_multiplier = 2`.
The rational table is authoritative for entitlement arithmetic; retained descriptive S/B anchors were not removed or used for early-rounded calculation.
Future tuning must preserve the table's algebraic equivalence to the accepted formula rather than independently changing descriptive anchors.

| Reward standing/doctrine | Raw-Strength coefficient | Equipment D | Fuel D |
| --- | --- | ---: | ---: |
| Favored, nonreciprocal/default | 50 + Strength | 50 | 100 |
| Favored, reciprocal | (50 + Strength)*5 | 200 | 400 |
| Respected | 100 + 3*Strength | 400 | 800 |
| Distrusted/Enemy | 0 | 50 | 100 |

Migration is local: freeze publishes four required-count fields, its predicate consumers read them, and entitlement uses the two utility calls.
Historical ledger totals, frozen host/source identity, parent recovery, receipts, conduct flags, first-history authorization, and main publication remain their existing owners.
No new event target, normal-history cleanup, periodic hook, central router, wrapper skill, localisation, GUI, map, focus, or AI surface was introduced.
Scratch variables are temporary; actual/frozen ledgers and completed entitlements are retained through parent cleanup.
No helper was added without direct call sites or documentation.

## Conservative range and exact-floor proof

The required source model represents values on a 0.001 grid, with maximum positive 2147483.647 and minimum -2147483.648.
Installed primary documentation describes fixed-point arithmetic and variable operators but does not fully establish actual engine width/precision.
The offline Data structures five-decimal/wider-range statement is not treated as primary engine proof.
Neither these cases nor the following proof is native engine verification.
This is a CONSERVATIVE AUDIT CONTRACT, not an observed general-variable storage limit or observed native overflow.
Modifier-specific three-decimal guidance does not decisively override the offline Variables paragraph; actual ordinary-variable width and precision remain a documentation gap.
Deprecated plain manpower getter limits near 2.1 million are a separate field-getter issue and are not evidence for general variable storage width.

N is a difference of representable nonnegative integral receipts, so it fits signed storage before negative-N rejection.
Residual subtraction never proceeds below zero; inconsistent sums such as two 1100000 terminal counts or two 1100000 original/substitute counts are rejected without adding them.
Count validation clamps only scratch to the largest representable integer before rounding, so malformed native-max fractional counts cannot round above the assumed range.
For exact ratios, q = floor(N/100) is at most 21474, r = N - 100q is at most 99, q*90 at most 1932660, r*90 at most 8910, and the final 90% required F at most 1932735.
80/50 percent are smaller; zero N retains its explicit no-contract-history flag and never creates a positive-denominator grade.

Normalizer maximum scale intermediate remains 1000000, converted terms at most 16000, each pre-clamp accumulation at most 32000, and exceptional sum at most 48000.
PP uses scale 2 and a cap 8000, with output at most 16000, including PP zero.
Material native-thousands values on the 0.001 grid normalize at integer scales of at least 100, yielding multiples of 0.1 milli.
V/L half-premiums therefore remain exact multiples of 0.05, and C_milli = min(16000, M_milli + 0.5V_milli + 0.5L_milli) has no premature package rounding.
Raw frozen Strength on the 0.001 grid yields exact coefficients at most 750.

For each component, C_milli = 100q+r, q = floor(C_milli/100), denomA = D/100, numeratorA = q*coefficient, floorA = floor(numeratorA/denomA), remainderA = numeratorA - floorA*denomA, numeratorB = 100*remainderA + r*coefficient, and result = floorA + floor(numeratorB/D).
This algebra is exactly floor(C_milli*coefficient/D), before applying the accepted standing ceiling.
q is integral and at most 160; numeratorA is exact on the grid and at most 120000; floorA at most 60000; floorA*denomA no larger than numeratorA.
denomA is exactly 0.5/1/2/4/8, remainderA below denomA, its scaled term below 800, r*coefficient below 75000, and numeratorB below 75800.
The total uncapped entitlement maxima are 60000 equipment and 30000 fuel, both in range.

The only potentially non-grid product is the positive r*coefficient; its downward truncation is smaller than 0.001.
The other numeratorB summand is exactly on the 0.001 grid, and every integer-floor threshold is an integer multiple of D.
At an exact threshold, the product's fractional part must be representable because the threshold and other summand are representable.
Above a threshold, truncation onto the same grid cannot take the sum below that threshold.
Thus product truncation preserves the integer floor, and truncating the subsequent positive quotient to 0.001 preserves it too.
No residual precision gap remains under these stated input quanta and truncation semantics; other engine rounding semantics remain unverified.

## Meaningful current-source validation

The self-contained runner below parses and executes the actual current grading effects, triggers and constants.
Every stored assignment, arithmetic result, round result and clamp result is truncated toward zero to 0.001 and range-checked.
Temporary outputs obey conservative helper lifetime: only caller-preinitialized storage survives a scripted-effect return.
Trigger-side temporary count validation is executed, not stubbed.
Unknown commands fail; parent retained-history proof and four-enum validation remain explicit external fixture boundaries.
No parent/native receipt, stock, conduct observer, source transfer, or integrated lifecycle claim is inferred from the fixtures.

All original 17 case families passed under this stricter model, and all **216543 additional current-source cases** passed.
Largest stored magnitude including retained native-max actual inputs was **2147483.647**.

| Current case family | Checks | Meaningful result |
| --- | ---: | --- |
| B01 | 5 | PP 0, 0.001, 500, 8000, native maximum; E credit is 0, 0.002, 1000, 16000, 16000; M/V/L and material entitlements remain zero. |
| B02 | 5 | Whole freeze/entitlement with F=N 0, 21474, 21475, 2000000 and 2147483; no capped historical counts or overflowing ratios. |
| B03 | 1 | All forty material quantities and PP at native maximum plus largest integral contract count; actual snapshots retained, normalized aggregates bounded, Favored entitlement 50000/25000. |
| B04 | 3 | Two 1100000 terminal counts, two 1100000 original/substitute counts, and retired greater than issued reject unresolved before unsafe arithmetic. |
| B05 | 54 | Each of eighteen count/cache inputs at 0.001, 1.999 and native maximum rejects fractional malformed receipts while retaining original actual values. |
| B06 | 3 | Missing issued, material or emergency PP field remains unresolved; no fabricated entitlement pair. |
| B07 | 51 | Exact 80/90/50 required-F utility at seventeen N values, including 21474/21475, each old product boundary, 2000000 and 2147483. |
| B08 | 99 | Whole freeze at required F and one below, with all four stored thresholds equivalent to exact 100F >= percent*N oracle. |
| B09 | 315 | Whole freeze -> classification -> entitlement across all standing contexts, seven material/half-subset quantities, and Strength 0, 1, 33, 0.001, 0.999, 33.333, 99.999, 80, 100; exact rational floor oracle. Some tiny Favored contexts correctly classify lower because M < 2. |
| B10 | 2 | Respected M=2 at Strength 1/33 yields 515/257 and 995/497, correcting the audit's premature-B defect. |
| B11 | 1 | Respected raw C_milli=13125/Strength100 produces 13125/6562 before accepted standing ceilings; durable result 10000/5000. This preserves the requested raw anchor without changing the accepted Respected ceiling. |
| B12 | 2 | Distrusted/Enemy with large material still receive zero without overflowing intermediate multiplication. |
| B13 | 2 | Either partially present entitlement field at zero is repaired to the complete 32500/16250 pair; both-present replay preserves the pair despite later Strength change. |
| B14 | 216000 | Actual source utility sweep of every 0.05-milli remainder in 0-99.95, q=1 and q=159, all three nonzero coefficients, both component denominators and nine listed Strength values; no exact-rational integer-floor mismatch. |

The original bounded re-execution also retains accepted reciprocal donor 32500/16250, reciprocal low-contribution 13125/6562, weak-host 17500/8750, high Favored 50000/25000, Respected 2550/1275, zero M, four doctrines, Wrath boundaries, source-only identity/recovery fixtures and one-use replay.
B14 isolates the arithmetic helper for exhaustive tail coverage; B01-B13 and the seventeen families provide the whole-freeze path where stated.
This division is explicit, not a claim that a utility sweep alone validates production receipt owners.

## References and mandatory MCP evidence limits

Skills read/applied: `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`.
No skills were created or changed.
Read AGENTS.md, full assigned accepted plan, audit F1-F5, all five grading owners, the contract enum owner, and pertinent existing `chaosx_dynamic_effects.txt`/Markdown sections before patching.
Existing shared population floor correction was read as an arithmetic pattern; the shared owner was not changed.

Successful live `hoi4.reference_context(surface=event, limit=12)` reported no omitted/missing required sources, followed by targeted `reference_search` and `reference_read` calls.
The context index itself is not claimed as detailed source coverage.

| Citation | Read span / rule | Revision |
| --- | --- | --- |
| Installed `documentation\effects_documentation.md` | Live 3587-3594 division and 6476-6485 rounding; direct 5012-5043 multiplication. | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\triggers_documentation.md` | Live 2110-2135 explicit variable comparison semantics. | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation\script_concept_documentation.md` | Live 184-215 fixed-point math and 216-222 supported scoped-variable constants. No complete width/precision contract. | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md` | Live 1-34 mandatory first-entry schema and int/fixed_point. | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Offline `Data structures - Hearts of Iron 4 Wiki.md` | Live 435-443 temporary lifetime/unscoped storage; direct 425-434 conflicting width/precision statement and 555-582 operator conventions. | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `Effects - Hearts of Iron 4 Wiki.md` | Direct 4683-4714 plain scripted effect `= yes` invocation. | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `Triggers - Hearts of Iron 4 Wiki.md` | Direct 329-373 AND, OR, NOT/NOR and control semantics. | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Offline `Scopes - Hearts of Iron 4 Wiki.md` | Direct 52-76 country scope domains. | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Installed `common\scripted_effects\zz_debug_effects.txt` | `d_add_fake_armies`, live 42-86 and direct 42-98, including temp multiply/round/clamp at 72-83; arithmetic-only precedent, no debug gameplay copied. | Lookup revision `ae19cd1aefa3f04847edcf5f1a094311fe87c08542c15f5e5c353106e95b924b` |

Connected reference/source tools are exposed and returned live successful results for workspace `mod_chaos_redux_ea3b2d67c2c0`.
Source lookup schema lacks `view`/`keyPath`; no unsupported route was assumed.
`hoi4.script_validate` is absent from the connected tool catalog, so installed-documentation scope validation through that route is unavailable.
Server health/version/client task negotiation were not independently verified; no helper-expansion, job, native-task or rewrite route was used.

Before patch: `hoi4.event_inspect`, `{kind:event,eventId:chaosx.nr12.608}`, depth1/nodes4/edges8/no helpers, returned `EVENT_INSPECTED_PARTIAL`, revision `d0087fea8accc02308dd34698d35ccfa59abc878e1f3543a1d6d6157785a4482`.
Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf9c8b39b3d84ec40a672131448ca6417eccaeca93f0e63bdea64c0a37459890/edac542e261b447a05da398e58ad37466d39947defd0f30901fe3c85357a0f00/event-trace-d0087fea8acc.json`.
Two initial selector-shape validation errors were corrected to the actual discriminator/eventId contract before successful inspection.

After patch: `hoi4.event_render`, same event/options/depth1/nodes2/no helpers, returned `EVENT_RENDERED_PARTIAL`, revision `d397c49bcd704632e8edc807c7fbaf2d801de75dd4f095a9ee52deac8d3673e5`.
Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d8357917e7ca7c459d401dae73b4a85896f160f9ef163fac4868abd6863935da/aa71a7310836d4b421f335567d2a14361b2cd8f4329c3f5652adb39d93c1170b/event-options-d397c49bcd70-manifest.json`.
PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/439a8ceae4c68367dc0f6c5f2e20745059d41ed67bbdc080fe00a554c0b2b666/7e391a2ed3781de604042941f17e1778e83a8480561bbeb04fd4479b90fbc4a8/event-options-d397c49bcd70.png`.
Focused routes defer helper projections and lifecycle passes; they provide direct event source evidence only, not proof of grading arithmetic, visual acceptance or integrated consumer coverage.
A bounded 3000-byte manifest read failed `-32603: Artifact provenance manifest is unavailable`; visual/artifact-detail inspection remains unresolved.

`hoi4.event_compare` using those before/after revision objects and the same event selector returned `EVENT_REVISION_NOT_CACHED`: "Requested event graph revision is not cached or retained as a graph artifact."
No successful before/after event lifecycle comparison exists for this patch.
Do not substitute the source-model arithmetic tests for that blocked engine-evidence route.
No probability pass was run because this repair contains only deterministic arithmetic and no weighted/AI selection surface; parent decision AI work remains separately owned.

## Simplifications, omissions, blockers and parent follow-up

No accepted matrix, formula, actual-history input kind, ratio boundary, premium, ceiling or assigned repair was simplified; no gameplay historical cap, approximate ratio, early-rounded multiplier, PP substitute or fallback was introduced.
All requested source repairs and matching helper documentation are complete inside this ownership.
Combined Gods completion/publication is not claimed.

Required independent parent re-review through the same arithmetic auditor remains pending, using the current exact source hashes and bounded named cases above.
Parent recovery/core/contribution, actual receipt producers, source-funded delivery, immutable obligation/source flags and main integration were deliberately left untouched under the explicit ownership boundary.
Any external consumer changes or producer-side representability checks belong to that parent; this helper cannot recover information already overflowed by a producer and does not cap history to hide it.
Physical source/receiver deltas, integrated cleanup/closure/conduct/recovery, and native engine execution were not checked because they are outside this task's owned source and HOI4 launch was forbidden.
Native engine width/precision/rounding and the unavailable MCP comparison/artifact/scope-validation evidence remain uncertain as stated, rather than being reported as engine-verified.
No Git commit was made because the specific task forbids Git.

## Reproducible conservative current-source cases

Run this fenced code through Python stdin from the mod root.
It writes no files.
It models required three-decimal truncation and bounded storage, not observed native engine behavior.
The original seventeen families below are re-executed under that bounded model; the older handoff retains their original five-decimal provenance separately.

```python

from pathlib import Path

from decimal import Decimal as D, ROUND_DOWN, ROUND_HALF_UP

import re, hashlib, json

P='gods_of_africa_'; G=P+'grade_'

def parse(path):

    tokens=re.findall(r'[{}=<>]|[^\s{}=<>]+',re.sub(r'#.*','',Path(path).read_text(encoding='utf-8-sig')))

    it=iter(tokens); tok=next(it,None)

    def block(nested=False):

        nonlocal tok

        out=[]

        while tok is not None and tok!='}':

            k=tok; op=next(it); tok=next(it)

            if tok=='{':

                tok=next(it,None); v=block(True)

            else: v=tok; tok=next(it,None)

            out.append((k,op,v))

        if nested:

            assert tok=='}'; tok=next(it,None)

        return out

    return block()

E=dict((k,v) for k,op,v in parse('common/scripted_effects/012_africa_gods_grading_effects.txt'))

T=dict((k,v) for k,op,v in parse('common/scripted_triggers/012_africa_gods_grading_triggers.txt'))

C={}

for f in ['common/script_constants/012_africa_gods_constants.txt','common/script_constants/012_africa_gods_grading_constants.txt']:

    for group,_,body in parse(f):

        assert body[0][0]=='schema'

        for k,_,v in body[1:]:

            if not isinstance(v,list): C['constant:'+group+'.'+k]=D(v)

kind={k:D(v) for k,v in [(k,v) for group,_,b in parse('common/script_constants/012_africa_gods_grading_constants.txt') if group==P+'contribution_units' for k,_,v in b if not isinstance(v,list)] if k in ['infantry','support','trucks','artillery','armor','aircraft','fuel','convoys','trains','manpower']}

class Engine:

    def __init__(self,doctrine=1,strength=80):

        self.vars={P+'history_owner_id':D(1),P+'history_origin_host_id':D(10),P+'participant_generation':D(7),P+'wrath':D(8)}

        self.host={'africa_origin_host_id':D(10),'africa_host_generation':D(7),P+'settlement_final_strength':D(str(strength)),P+'settlement_final_doctrine':D(doctrine)}

        self.flags=set(); self.hflags={P+'final_settlement_committed'};self.temps={};self.arrays={};self.war=False;self.exists=True;self.hostexists=True

        self.temps[P+'grading_first_genuine_history']=D(1)

        self.call(P+'initialize_grading_ledger')

        self.flags.add(P+'history_initialized')

    def val(self,k,scope='country'):

        if k in C:return C[k]

        try:return D(k)

        except:pass

        if k=='THIS.id':return D(1 if scope=='country' else 10)

        if k.startswith('event_target:africa_host.'):return self.host.get(k.split('.',1)[1],D(0))

        if k.endswith('^num'):return D(len(self.arrays.get(k[:-4],[])))

        return self.temps.get(k,(self.vars if scope=='country' else self.host).get(k,D(0)))

    def cmp(self,l,op,r):

        return {'=':l==r,'>':l>r,'<':l<r,'equals':l==r,'not_equals':l!=r,'greater_than':l>r,'less_than':l<r,'greater_than_or_equals':l>=r,'less_than_or_equals':l<=r}[op]

    def cond(self,b,s='country'):

        def item(k,op,v):

            if k=='AND':return self.cond(v,s)

            if k=='OR':return any(item(*x) for x in v)

            if k=='NOT':return not any(item(*x) for x in v)

            if k=='exists':return (self.exists if s=='country' else self.hostexists)==(v=='yes')

            if k=='has_country_flag':return v in (self.flags if s=='country' else self.hflags)

            if k=='has_variable':return v in self.temps or v in (self.vars if s=='country' else self.host)

            if k=='has_war_with':return self.war

            if k=='event_target:africa_host':return self.cond(v,'host')

            if k=='check_variable':

                if len(v)==1:

                    a,o,c=v[0];return self.cmp(self.val(a,s),o,self.val(c,s))

                d={a:c for a,o,c in v};return self.cmp(self.val(d['var'],s),d.get('compare','equals'),self.val(d['value'],s))

            if k==P+'participant_has_settlement_history':

                # External parent's settlement trigger is an explicit fixture boundary.

                gen=self.vars[P+'participant_generation'];origin=self.vars[P+'history_origin_host_id']

                return self.exists and self.hostexists and P+'history_initialized' in self.flags and origin==self.host['africa_origin_host_id'] and (gen==self.host['africa_host_generation'] or (gen==self.host.get(P+'inherited_history_generation') and origin==self.host.get(P+'inherited_history_origin_host_id')))

            if k==P+'final_settlement_value_is_valid':return self.vars.get(P+'final_settlement') in [D(1),D(2),D(3),D(4)]

            if k in ['set_temp_variable','clamp_temp_variable','round_temp_variable']:

                self.run([(k,op,v)]);return True

            if k in T:return self.cond(T[k],s)==(v=='yes')

            raise AssertionError(('unknown trigger',k))

        return all(item(*x) for x in b)

    def call(self,k):

        prior=set(self.temps);self.run(E[k])

        # Conservative helper frame lifetime: retain only preexisting temp storage.

        self.temps={n:v for n,v in self.temps.items() if n in prior}

    def run(self,b):

        last=False

        for k,op,v in b:

            if k in ['if','else_if']:

                d=[x for x in v if x[0]!='limit'];limit=next(x[2] for x in v if x[0]=='limit')

                allowed=(k=='if' or not last) and self.cond(limit)

                if allowed:self.run(d)

                last=(last or allowed) if k=='else_if' else allowed

            elif k=='else':

                if not last:self.run(v)

                last=True

            elif k in E:self.call(k)

            elif k=='set_country_flag':self.flags.add(v)

            elif k=='clr_country_flag':self.flags.discard(v)

            elif k=='clear_array':self.arrays[v]=[]

            elif k=='round_temp_variable':self.put(self.temps,v,self.val(v).quantize(D(1),rounding=ROUND_HALF_UP))

            elif k in ['clamp_temp_variable','clamp_variable']:

                d={a:c for a,o,c in v};store=self.temps if 'temp' in k else self.vars

                value=self.val(d['var']);value=max(value,self.val(d['min'])) if 'min' in d else value;value=min(value,self.val(d['max'])) if 'max' in d else value

                self.put(store,d['var'],value)

            elif k in ['set_variable','set_temp_variable','multiply_variable','multiply_temp_variable','add_to_variable','add_to_temp_variable','subtract_from_temp_variable','divide_temp_variable']:

                store=self.temps if 'temp' in k else self.vars

                for a,o,c in v:

                    q=self.val(c);old=self.val(a)

                    val=q if k.startswith('set_') else old*q if k.startswith('multiply_') else old+q if k.startswith('add_') else old-q if k.startswith('subtract_') else old/q

                    self.put(store,a,val)

            else:raise AssertionError(('unknown effect',k))

    def put(self,store,a,val):

        val=val.quantize(D('.001'),rounding=ROUND_DOWN)

        assert D('-2147483.648') <= val <= D('2147483.647'), ('range',a,val)

        self.max_stored=max(getattr(self,'max_stored',D(0)),abs(val))

        store[a]=val

    def set(self,**kv):

        for k,v in kv.items():self.vars[P+k]=D(str(v))

        return self

    def flag(self,*f):self.flags.update(P+x for x in f);return self

    def contracts(self,F,N=None,failed=0,refused=0,war=0,streak=None):

        N=F+failed+refused+war if N is None else N

        self.set(demands_issued=N,demands_fulfilled=F,demands_full_original=F,demands_failed=failed,demands_refused=refused,demands_broken_by_war=war,compliance_streak=F if streak is None else streak,longest_compliance_streak=F if streak is None else streak)

        return self

    def amounts(self,M=0,V=0,L=0,E=0):

        return self.set(paid_infantry_k=M,voluntary_paid_infantry_k=V,campaign_paid_infantry_k=L,emergency_paid_infantry_k=E)

    def freeze(self):self.call(P+'freeze_final_grade_inputs');return self

    def standing(self):

        hits=[(n,num) for n,num in [('enemy',4),('favored',1),('respected',2),('distrusted',3)] if self.cond(T[P+'full_grade_'+n+'_is_valid'])]

        assert len(hits)<=1,hits

        return hits[0][1] if hits else None

    def entitlement(self):

        standing=self.standing()

        if standing is not None:self.vars[P+'final_settlement']=D(standing)

        self.call(P+'calculate_settlement_entitlement')

        return tuple(self.vars.get(P+'reward_'+x+'_entitlement') for x in ['equipment','fuel'])

passed=[]

def record(n):passed.append(n)

# 1: all denominators and tiny payment preserve arithmetic.

for k,den in kind.items():

    x=Engine();x.temps.update({P+'normalize_paid_k':den/D(1000),P+'normalize_denominator':den,P+'normalize_bound_milli':D(16000),P+'normalize_output_milli':D(0)})

    x.call(P+'normalize_paid_quantity_milli');assert x.temps[P+'normalize_output_milli']==1000,(k,x.temps)

x.temps[P+'normalize_paid_k']=D('.001');x.temps[P+'normalize_denominator']=D(10000);x.call(P+'normalize_paid_quantity_milli');assert x.temps[P+'normalize_output_milli']==D('.1')

x=Engine().set(paid_manpower_k='.001').freeze();assert x.vars[G+'paid_manpower_k']==D('.001') and x.vars[G+'material_milli']==D('.1')

record('G12_normalization_ten_kinds_and_one_man')

# 2

x=Engine().freeze();assert x.standing()==3 and P+'grade_no_contract_history' in x.flags and x.entitlement()==(0,0)

record('G12_zero_history')

# 3

x=Engine().contracts(6).amounts(8,2,2).freeze();assert x.standing()==1 and x.entitlement()==(32500,16250)

record('G12_consistent_donor')

# 4 reciprocal 80%, wrath boundary, current/longest streak.

x=Engine().contracts(4,refused=1,streak=2).amounts(2).set(wrath='39.999').freeze();assert x.standing()==1

x=Engine().contracts(3,refused=1,streak=2).amounts(2,V=1).freeze();assert x.standing()==2

x=Engine().contracts(4,refused=1,streak=1).amounts(2).freeze();assert x.standing()==2

x=Engine().contracts(4,streak=2).amounts(2).set(wrath=40).freeze();assert x.standing()==2

record('G12_reciprocal_ratio_streak_wrath_boundaries')

# 5 exaction 90%, fulfillment, streak, exceptional boundary.

x=Engine(2).contracts(9,refused=1,streak=4).amounts(2).freeze();assert x.standing()==1

x=Engine(2).contracts(8,refused=1,streak=4).amounts(2).freeze();assert x.standing()==2

x=Engine(2).contracts(4,streak=4).amounts(2,V=1,E=1).freeze();assert x.standing()==1

x=Engine(2).contracts(4,streak=4).amounts(2,V=1,E='.999').freeze();assert x.standing()==2

record('G12_exaction_ratio_and_exceptional_boundaries')

# 6 ambiguity tolerates two failures, no chosen doctrine does not.

x=Engine(3).contracts(4,refused=1,streak=3).amounts(2,V=1).freeze();assert x.standing()==1

x=Engine(3).contracts(2,failed=2,streak=2).amounts(2).freeze();assert x.standing()==2

x=Engine(3).contracts(2,failed=3,streak=2).amounts(2).freeze();assert x.standing()==3

record('G12_ambiguity_standing_boundaries')

# 7 doctrine zero favored gate, default adverse bound.

x=Engine(0).contracts(4,refused=1,streak=3).amounts(2,V=1).freeze();assert x.standing()==1

x=Engine(0).contracts(2,failed=2,streak=2).amounts(2).freeze();assert x.standing()==3

record('G12_no_chosen_doctrine_boundaries')

# 8 invariant failure

x=Engine().contracts(2,N=3).freeze();assert x.standing() is None and P+'grading_unresolved' in x.flags and P+'grade_inputs_frozen' not in x.flags and x.entitlement()==(None,None) and P+'final_outcome_committed' not in x.flags

record('G12_unresolved_terminal_invariant')

# 9 inconsistent receipt type and quantity subset.

for kv in [dict(demands_retired=1),dict(demands_full_original=1),dict(demands_failed=-1),dict(voluntary_paid_infantry_k=3)]:

    x=Engine().contracts(2).amounts(2).set(**kv).freeze();assert x.standing() is None

record('G12_invalid_ledger_counts_and_subsets')

# 10 exact owner/origin and one inherited generation plus open demand rejection.

x=Engine().contracts(2).amounts(2,V=1).set(participant_generation=6)

x.host.update({P+'inherited_history_generation':D(6),P+'inherited_history_origin_host_id':D(10)})

x.freeze();assert x.standing()==1

for kv in [dict(history_owner_id=2),dict(history_origin_host_id=20),dict(participant_generation=5)]:

    x=Engine().set(**kv).freeze();assert x.standing() is None

for flag in ['contract_ledger_open','demand_active']:

    x=Engine().flag(flag).freeze();assert x.standing() is None

record('G12_identity_inheritance_and_closed_contract')

# 11 prior hostility: no pardon => Distrusted; accepted => 2 respected/4 favored, new adverse conduct matters.

for prior in ['prior_war','prior_occupation','prior_treaty_break','prior_defiance']:

    x=Engine().contracts(6).amounts(8,V=2).flag(prior).freeze();assert x.standing()==3

    for f,want in [(1,3),(2,2),(4,1)]:

        x=Engine().contracts(6,streak=f).amounts(8,V=2).flag(prior).set(reconciliation_count=1,post_reconciliation_fulfilled=f).freeze();assert x.standing()==want,(prior,f,x.standing())

x=Engine().contracts(6,refused=3,streak=4).amounts(8,V=2).flag('prior_defiance').set(reconciliation_count=1,post_reconciliation_fulfilled=4).freeze();assert x.standing()==2 # lifetime ratio is 6/9, not repaired by pardon.

x=Engine().contracts(9,refused=3,streak=4).amounts(8,V=2).flag('prior_defiance').set(reconciliation_count=1,post_reconciliation_fulfilled=4,post_reconciliation_refusals=1).freeze();assert x.standing()==2

record('G12_repaired_prior_hostility_recovery')

# 12 each current Enemy cause and >80 strict boundary.

for cause in ['unresolved_treaty_break','unresolved_major_offense','permanent_opt_out','defiant']:

    x=Engine().contracts(6).amounts(8,V=2).flag(cause).freeze();assert x.standing()==4 and x.entitlement()==(0,0)

for kv in [dict(observed_host_core_count=1),dict(owned_host_core_count=1),dict(wrath='80.001')]:

    x=Engine().set(**kv).freeze();assert x.standing()==4

x=Engine();x.war=True;x.freeze();assert x.standing()==4

x=Engine().set(wrath=80).freeze();assert x.standing()==3

x=Engine().contracts(0,refused=3).freeze();assert x.standing()==4

record('G12_enemy_priority_and_strict_wrath')

# 13 PP only emergency credit, no material from gifts/procedural history.

x=Engine(0,100).set(emergency_paid_pp=500).freeze();assert x.vars[G+'emergency_milli']==1000 and x.vars[G+'material_milli']==0 and x.standing()==2 and x.entitlement()==(0,0)

x=Engine().set(history_count=1000,aid_count=1000,compliance_count=1000).freeze();assert x.standing()==3 and x.entitlement()==(0,0)

record('G12_emergency_pp_and_no_fabricated_material')

# 14 weak host

x=Engine(1,20).contracts(6).amounts(8,2,2).freeze();assert x.entitlement()==(17500,8750)

record('G12_weak_host_capability')

# 15 strong low, floor 6562.5 => 6562, partial one fulfilled does not qualify favored.

x=Engine(1,100).contracts(2).amounts(3,1).freeze();assert x.standing()==1 and x.entitlement()==(13125,6562)

x=Engine().contracts(1).amounts(1).freeze();assert x.standing()==2 and x.entitlement()==(850,425)

record('G12_strong_low_contribution_and_integer_floor')

# 16 ceilings, bounds and default material-only respected.

x=Engine(1,100).contracts(6).amounts(12,2,4).freeze();assert x.entitlement()==(50000,25000)

x=Engine(0,80).contracts(3,failed=1,streak=3).amounts(3).set(wrath=45).freeze();assert x.entitlement()==(2550,1275)

x=Engine(0,100).contracts(3,failed=1,streak=3).amounts(1000000).set(wrath=45).freeze();assert x.vars[G+'paid_infantry_k']==1000000 and x.vars[G+'material_milli']==16000 and x.entitlement()==(10000,5000)

record('G12_entitlement_ceilings_and_actual_uncapped_snapshot')

# 17 replay and conservative outputs/defaults.

x=Engine().contracts(6).amounts(8,2,2);old=x.vars[P+'paid_infantry_k'];x.temps[P+'grading_first_genuine_history']=D(1);x.call(P+'initialize_grading_ledger');assert x.vars[P+'paid_infantry_k']==old

x.freeze();a=x.entitlement();frozen=dict(x.vars);x.set(paid_infantry_k=100,wrath=95);x.host[P+'settlement_final_strength']=D(1);x.call(P+'freeze_final_grade_inputs');x.call(P+'calculate_settlement_entitlement');assert x.entitlement()==a and x.vars[G+'paid_infantry_k']==8

y=Engine();y.temps[P+'floor_input']=D('6562.5');y.call(P+'floor_temporary_value');assert P+'floor_output' not in y.temps

y.temps[P+'floor_output']=D(0);y.call(P+'floor_temporary_value');assert y.temps[P+'floor_output']==6562

y=Engine();y.temps={};y.call(P+'normalize_paid_quantity_milli');assert y.temps=={}

y=Engine();y.flags.discard(P+'grading_ledger_initialized');y.freeze();assert y.standing() is None

y=Engine();y.vars.pop(P+'demands_issued');y.flags.discard(P+'grading_ledger_initialized');y.temps={};y.call(P+'initialize_grading_ledger');assert P+'grading_ledger_initialized' not in y.flags

record('G12_reentry_replay_temp_lifetimes_and_missing_inputs')

assert len(passed)==17



from fractions import Fraction as Q

from math import ceil,floor

native_max=D('2147483.647')

case_counts={}

checks=0

max_stored=D(0)

def note(family,x=None):

    global checks,max_stored

    checks+=1;case_counts[family]=case_counts.get(family,0)+1

    if x is not None:max_stored=max(max_stored,x.max_stored)

def unresolved(x):

    x.freeze();assert x.standing() is None and P+'grading_unresolved' in x.flags

    assert P+'grade_inputs_frozen' not in x.flags and x.entitlement()==(None,None)

# F1: source freeze, actual paid PP preserved, no PP to material or entitlement.

for pp in [D(0),D('.001'),D(500),D(8000),native_max]:

    x=Engine(0,100).set(emergency_paid_pp=pp).freeze()

    assert x.vars[G+'emergency_paid_pp']==pp

    assert x.vars[G+'emergency_milli']==min(D(16000),pp*2)

    assert all(x.vars[G+n+'_milli']==0 for n in ['material','voluntary','campaign'])

    assert x.entitlement()==(0,0)

    note('B01_emergency_PP_0_tiny_500_8000_nativeMax',x)

# F3: maximal integral receipt, maximum native actual quantity, malformed sums.

for n in [0,21474,21475,2000000,2147483]:

    x=Engine(1,100).contracts(n).amounts(12,2,4).freeze()

    assert x.vars[G+'demands_fulfilled']==n and x.vars[G+'eligible_demands']==n

    x.entitlement();note('B02_full_freeze_integral_count_range',x)

x=Engine(1,100).contracts(2147483)

for k in kind:

    for stem in ['paid_','voluntary_paid_','emergency_paid_','campaign_paid_']:

        x.set(**{stem+k+'_k':native_max})

x.set(emergency_paid_pp=native_max).freeze()

assert x.entitlement()==(50000,25000)

for k in kind:assert x.vars[G+'paid_'+k+'_k']==native_max

assert all(x.vars[G+n+'_milli']==16000 for n in ['material','voluntary','campaign','emergency'])

note('B03_nativeMax_all_40_quantities_and_PP',x)

for kv in [dict(demands_issued=2000000,demands_fulfilled=1100000,demands_full_original=1100000,demands_failed=1100000),dict(demands_issued=2000000,demands_fulfilled=2000000,demands_full_original=1100000,demands_honored_substitute=1100000),dict(demands_issued=1,demands_retired=2147483)]:

    x=Engine().set(**kv);unresolved(x);note('B04_malformed_sums_and_negative_N',x)

counts=re.findall(r'has_variable = (gods_of_africa_\w+)\n',Path('common/scripted_triggers/012_africa_gods_grading_triggers.txt').read_text()[Path('common/scripted_triggers/012_africa_gods_grading_triggers.txt').read_text().index(P+'full_grade_ledger_is_present'):Path('common/scripted_triggers/012_africa_gods_grading_triggers.txt').read_text().index('has_variable = '+P+'emergency_paid_pp')])

assert len(counts)==18

for field in counts:

    for malformed in [D('.001'),D('1.999'),native_max]:

        x=Engine();x.vars[field]=malformed;unresolved(x)

        assert x.vars[field]==malformed

        note('B05_all_18_fractional_receipts_rejected',x)

for field in ['demands_issued','paid_infantry_k','emergency_paid_pp']:

    x=Engine();x.vars.pop(P+field);unresolved(x);note('B06_missing_ledger_field',x)

# F3: exact ceil threshold, full freeze at and one below threshold.

ns=[0,1,99,100,101,21474,21475,26843,26844,23860,23861,42949,42950,1000000,1999999,2000000,2147483]

for n in ns:

    for percent in [80,90,50]:

        required=(n*percent+99)//100

        x=Engine();x.temps.update({P+'ratio_eligible':D(n),P+'ratio_percent':D(percent),P+'ratio_required_output':D(0)})

        x.call(P+'required_fulfilled_count');assert x.temps[P+'ratio_required_output']==required

        note('B07_exact_ratio_utility',x)

        for f in sorted(set([max(0,required-1),required])):

            x=Engine().contracts(f,N=n,failed=n-f).freeze()

            for d,p in [('reciprocal',80),('exaction',90),('ambiguity',80),('respected',50)]:

                req=x.vars[G+'ratio_'+d+'_required_fulfilled']

                assert req==(n*p+99)//100

                assert (x.vars[G+'demands_fulfilled']>=req)==(100*f>=p*n)

            x.entitlement();note('B08_full_freeze_ratio_boundary',x)

# Whole freeze through final payout for quanta and odd/fractional Strength.

strengths=[D(0),D(1),D(33),D('.001'),D('.999'),D('33.333'),D('99.999'),D(80),D(100)]

for strength in strengths:

    for mode in ['favored_other','favored_reciprocal','respected','distrusted','enemy']:

        doctrine=1 if mode=='favored_reciprocal' else 0

        for amount in ['.001','.01','.999','1.001','20','199.999','1599.999']:

            x=Engine(doctrine,strength).set(paid_manpower_k=amount,voluntary_paid_manpower_k=amount,campaign_paid_manpower_k=amount)

            if mode.startswith('favored'):x.contracts(6)

            elif mode=='respected':x.contracts(1).set(wrath=45)

            elif mode=='distrusted':x.flag('prior_defiance')

            else:x.flag('permanent_opt_out')

            x.freeze();actual_standing=x.standing();result=x.entitlement()

            cm=Q(x.vars[G+'material_milli'])+Q(x.vars[G+'voluntary_milli'])/2+Q(x.vars[G+'campaign_milli'])/2

            cm=min(Q(16000),cm);st=Q(strength)

            coeff,den=((50+st)*5,200) if actual_standing==1 and doctrine==1 else ((50+st),50) if actual_standing==1 else (100+3*st,400) if actual_standing==2 else (Q(0),50)

            eqcap,fcap=(50000,25000) if actual_standing==1 else (10000,5000) if actual_standing==2 else (0,0)

            expected=(min(eqcap,floor(cm*coeff/den)),min(fcap,floor(cm*coeff/(2*den))))

            assert result==expected,(mode,strength,amount,cm,result,expected)

            note('B09_whole_freeze_fractional_strength_subpackages_all_standings',x)

# Named exact reward anchors and the audit's premature B defect cases.

for strength,want in [(1,(515,257)),(33,(995,497))]:

    x=Engine(0,strength).contracts(2).amounts(2).set(wrath=45).freeze();assert x.standing()==2 and x.entitlement()==want

    note('B10_respected_odd_strength_correction',x)

x=Engine(0,100).contracts(2).amounts('13.125').set(wrath=45).freeze()

assert x.standing()==2 and x.entitlement()==(10000,5000)

# Respected raw calculation 13125/6562 precedes its required 10000/5000 ceiling.

x.temps.update({P+'entitlement_contribution_milli':D(13125),P+'entitlement_coefficient':D(400),P+'entitlement_denominator':D(400),P+'scaled_entitlement_output':D(0)})

x.call(P+'floor_scaled_entitlement');assert x.temps[P+'scaled_entitlement_output']==13125

x.temps[P+'entitlement_denominator']=D(800);x.call(P+'floor_scaled_entitlement');assert x.temps[P+'scaled_entitlement_output']==6562

note('B11_respected_raw_13125_6562_then_standing_ceiling',x)

for standing in [3,4]:

    x=Engine(1,100).amounts(1600,1600,1600).flag('prior_defiance' if standing==3 else 'permanent_opt_out').freeze()

    assert x.standing()==standing and x.entitlement()==(0,0)

    note('B12_Distrusted_Enemy_high_material_zero',x)

# Existing pair immutable; one partially present field can be recomputed without zero lock.

for component in ['equipment','fuel']:

    x=Engine().contracts(6).amounts(8,2,2).freeze()

    x.vars[P+'reward_'+component+'_entitlement']=D(0)

    assert x.entitlement()==(32500,16250)

    x.vars[P+'settlement_strength']=D(1)

    assert x.entitlement()==(32500,16250)

    note('B13_partial_pair_repair_and_completed_pair_replay',x)

# Actual source helper sweep: every accepted 0.05-milli remainder, three coefficients,

# odd/fractional Strength, q=1 and q=159. Both eq and fuel denominators.

for strength in strengths:

    for mode in ['favored_other','favored_reciprocal','respected']:

        st=Q(strength)

        coeff,den=((50+st)*5,200) if mode=='favored_reciprocal' else (50+st,50) if mode=='favored_other' else (100+3*st,400)

        x=Engine()

        x.temps.update({P+'entitlement_coefficient':D(coeff.numerator)/D(coeff.denominator),P+'scaled_entitlement_output':D(0)})

        for q in [1,159]:

            for i in range(2000):

                cm=Q(q*100)+Q(i,20)

                x.temps[P+'entitlement_contribution_milli']=D(cm.numerator)/D(cm.denominator)

                for divisor in [den,2*den]:

                    x.temps[P+'entitlement_denominator']=D(divisor)

                    x.call(P+'floor_scaled_entitlement')

                    assert x.temps[P+'scaled_entitlement_output']==floor(cm*coeff/divisor),(strength,mode,cm,divisor,x.temps)

                    note('B14_all_005_milli_remainders_source_floor',x)

print(json.dumps({'originalCaseFamiliesPassed':passed,'boundedCaseFamilies':case_counts,'boundedCases':checks,'maximumStoredMagnitudeIncludingInputs':str(max_stored),'effects':len(E),'triggers':len(T),'scope':'actual grading source AST; every stored arithmetic result truncated to 0.001 and range checked; external parent identity/standing enum explicit fixtures; no native engine claim','sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in ['common/scripted_effects/012_africa_gods_grading_effects.txt','common/scripted_triggers/012_africa_gods_grading_triggers.txt','common/script_constants/012_africa_gods_grading_constants.txt']}},indent=2))



```


## Parent correction of count eligibility

The independent review identified the scratch maximum as an actual grading eligibility restriction, not merely an unchanged historical field.
The parent removes `maximum_integral_count` and replaces all eighteen clamp/round integer checks with remainder modulo one on caller-owned scratch, requiring remainder zero.
The installed trigger documentation explicitly supports `modulo_temp_variable` at `documentation/triggers_documentation.md:6442?6454`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`; the effect counterpart is `effects_documentation.md:4986?4998`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
This validates integral receipt counters without imposing an assumed numeric maximum or rounding a near-maximum field upward.
Actual history remains untouched, and the residual accounting and exact ratio decomposition remain unchanged.
The earlier bounded maximum description records the pre-correction source; independent same-case review is required for this replacement.
