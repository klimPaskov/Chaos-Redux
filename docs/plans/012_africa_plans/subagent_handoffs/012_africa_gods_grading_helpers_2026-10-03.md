# Event 012 Gods grading helpers implementation handoff

Assignment date: 2026-10-03; continued through the 2026-10-04 environment date.
Current disposition (2026-10-04): bounded source arithmetic repair implemented for F1-F5; independent parent re-review and combined integration/publication remain pending.
The former duplicate closure category and normalizer order were already reconciled by the parent; they are not current publication blockers.
Current proof and hashes are in [grading arithmetic repair](012_africa_gods_grading_arithmetic_repair_2026-10-04.md).
The original seventeen five-decimal/range-unbounded results and worker hashes below are historical provenance only.
Acceptance basis: the user's explicit full Gods implementation/no-simplification assignment and accepted recommended design in `012_africa_gods_full_grading_rewards_design_2026-10-03.md`.
The accepted design read for this continuation has SHA-256 `4bbbdefec2c092a110010bfca19965b353d75924eca138d57b5b618b896ac060`.
The assigned grading files were absent at inspection; no interrupted-worker grading content was discarded.
No Git staging/commit or HOI4 launch was performed.
The original worker wrote the five assigned files.
The arithmetic repair updates those same five and adds only its explicitly authorized companion handoff.

## Files and identifiers

- `common/script_constants/012_africa_gods_grading_constants.txt`: current schema-first integer categories `gods_of_africa_grading`, `gods_of_africa_contribution_units`, `gods_of_africa_reward_units`; fixed-point `gods_of_africa_reward_scale`.
- `common/scripted_effects/012_africa_gods_grading_effects.txt`: seven COUNTRY effects (including added `gods_of_africa_required_fulfilled_count` and `gods_of_africa_floor_scaled_entitlement`) `gods_of_africa_initialize_grading_ledger`, `gods_of_africa_normalize_paid_quantity_milli`, `gods_of_africa_floor_temporary_value`, `gods_of_africa_freeze_final_grade_inputs`, `gods_of_africa_calculate_settlement_entitlement`.
- `common/scripted_effects/012_africa_gods_grading_effects.md`: full API, actual fields, defaults, temporary output lifetime, constants, lifecycle, migration, cleanup, and parent call sites.
- `common/scripted_triggers/012_africa_gods_grading_triggers.txt`: fourteen `gods_of_africa_full_grade_*` checks covering history/ledger/freeze/inputs, prior hostility, Enemy/Favored/Respected/Distrusted, two recovery gates, exceptional support, Favored doctrine, and Respected adverse limits.
- This handoff: source references, validation results, exact gaps, and reproducible source fixtures.

Historical worker source SHA-256 (superseded for current arithmetic evidence):

| File | SHA-256 |
| --- | --- |
| Grading effects | `b9ce2b3e21b97c6cfd67e33879a779a956bc70c068103987c9a9cc6b4bbb9eee` |
| Grading triggers | `8e1f3ccc7faf9bc01a7198814b148a2fac6b4f3ae3e96dc32cf032647fca64f6` |
| Grading constants | `7ce3170ba58466b60206c87c583baa0734e6f1fd95de0ef92441cd311035f817` |

Before this tranche, the assigned full-grading helpers did not exist.
The existing classifier used coarse action counts and standing reward owners used fixed quantities/PP branches.
This tranche supplies the accepted actual-history calculation without editing those parent owners.
Native payments, conduct observations, unique contract closures, endpoint calls, diplomacy, source binding, owed/delivery accounting, UI/localisation, recovery integration, docs/spec/catalog alignment, and final review remain parent-owned.

## Immediate parent integration API

All calls use `= yes` in participant COUNTRY scope.
Set unscoped caller temp `gods_of_africa_grading_first_genuine_history = 1`, then call `gods_of_africa_initialize_grading_ledger = yes` only in the first-genuine-history branch.
The helper consumes that authorization.
Never call it as a coarse-history backfill or migration, including a retained history count of zero.
An initialized ledger or existing issued field is preserved on re-entry.

Before the census, the host owns normal `gods_of_africa_settlement_final_strength` and `gods_of_africa_settlement_final_doctrine`.
Before participant freeze, neutral-close and clear any ordinary demand, then refresh conduct.
The freeze requires both ordinary `gods_of_africa_contract_ledger_open` and `gods_of_africa_demand_active` clear.
The actual unresolved major-offense input is `gods_of_africa_unresolved_major_offense`; actual treaty breach uses `gods_of_africa_unresolved_treaty_break`.
Accepted reconciliation is proven by `gods_of_africa_reconciliation_count > 0`.
No generic offender flag invents an agreement breach.

Call `gods_of_africa_freeze_final_grade_inputs = yes`, then require `gods_of_africa_full_grade_inputs_are_valid = yes`.
Success flag is `gods_of_africa_grade_inputs_frozen`; failure flag is `gods_of_africa_grading_unresolved`.
Invariant failure or missing ledger creates no outcome and no entitlement.
The parent must guard its old fallback branch as well as its better-standing branches.

Bind the parent's final aliases to `gods_of_africa_full_grade_enemy_is_valid` (4), `gods_of_africa_full_grade_favored_is_valid` (1), `gods_of_africa_full_grade_respected_is_valid` (2), and `gods_of_africa_full_grade_distrusted_is_valid` (3).
Set the actual existing `gods_of_africa_final_settlement` enum, then call `gods_of_africa_calculate_settlement_entitlement = yes` before the parent initializes its immutable obligation.
It calculates when either entitlement field is absent, completes both in temporary storage, then writes only `gods_of_africa_reward_equipment_entitlement` and `gods_of_africa_reward_fuel_entitlement`, and preserves them on replay.
It writes no source, owed, granted, complete-delivery, or outcome receipt and applies no native grant.

All forty normal actual quantity fields keep their exact `paid_<kind>_k`, `voluntary_paid_<kind>_k`, `emergency_paid_<kind>_k`, `campaign_paid_<kind>_k` names.
The nineteen actual count/cache/PP fields and forty quantity fields are copied to `gods_of_africa_grade_<same_suffix>`.
Frozen booleans use `gods_of_africa_grade_prior_defiance/prior_war/prior_occupation/prior_treaty_break/current_war/unresolved_treaty_break/unresolved_major_offense/permanent_opt_out/defiant/reconciliation_accepted/no_contract_history`.
Other normal snapshots are documented exhaustively in the matching API Markdown.
Existing capability/identity snapshot names remain `gods_of_africa_settlement_strength/doctrine/generation/origin_host_id/history_generation`.
Do not overwrite them with live host values after freeze.
Parent cleanup must retain actual and frozen history, entitlements, prior conduct, and unique state arrays.

Utility callers must preinitialize `gods_of_africa_normalize_output_milli = 0` or `gods_of_africa_floor_output = 0` before calling and consuming the relevant helper.
Normalization inputs are caller temps `gods_of_africa_normalize_paid_k`, `gods_of_africa_normalize_denominator`, `gods_of_africa_normalize_bound_milli`.
Floor input is caller temp `gods_of_africa_floor_input`.
All nested utility call sites in the grading source already own their outputs.

## Constants, event targets, cleanup, and migration

The accepted ten normalization denominators and grading/reward anchors are central in the assigned constants file.
The sole closure enum is in `012_africa_gods_contract_constants.txt`, with `war_breach = 5`.
The extra integer `gods_of_africa_grading.ratio_percent_scale = 100` keeps compliance comparison independent from the reward Strength divisor.
The accepted close key is `war_breach = 5`.
Shared tribute/protection/emergency payment prices are unchanged.
No AI score, MTTH, random pool, strategy factor, or probability-bearing modifier was added or changed.
Reward coefficients are deterministic economic multipliers, not probability weights.

No event target, world observer, clock, new UI, asset, CXT content, or broad mechanic was created.
The existing host target is used at validation/freeze only; frozen classifier/entitlement reads do not follow later host-pointer changes.
Regular report targets and durable reward source binding remain parent-owned.
Only new ledger arrays/flags are initialized under genuine-history authorization.
There is no destructive cleanup of retained history.
The parent migrates its existing call sites in the sequence: first-history initialization, unique closure/actual receipts, host capability freeze, participant conduct refresh/freeze, guarded four-way classification, entitlement calculation, source obligation, native delivery, ordinary cleanup.

## Historical original-source validation (not current arithmetic certification)

An ephemeral read-only Python fixture runner parsed the actual three engine-facing files.
It executed their effect/trigger ASTs and constants with explicit COUNTRY and host fixture scopes, NOR semantics for NOT, scoped normal state, unscoped temp state, and conservative helper-frame cleanup.
Temporary scalars first created in a helper disappear on return; caller-preinitialized outputs retain modifications.
Historical arithmetic truncation was modeled at five decimal places from the offline data-structures reference, and round-to-nearest was corrected by the actual floor helper.
Unknown commands fail the runner instead of being treated as successful.
The original worker snapshot passed all seventeen named case families after separating percentage scale from the reward Strength divisor.

The parent's existing retained-history trigger and four-enum validator are explicit fixture boundaries.
The inherited-generation cases model that documented parent contract; they do not independently execute or validate the parent implementation.
No native stock, payment, source receipts, event execution, core observation, UI, or live game behavior was tested.

| Case | Meaningful expected result exercised |
| --- | --- |
| `G12_normalization_ten_kinds_and_one_man` | One denominator-sized payment for each of ten kinds gives 1000 milli; one man (0.001k) gives exactly 0.1 milli and remains 0.001k in the uncapped snapshot. |
| `G12_zero_history` | N=0 gives no-contract-history, Distrusted, 0/0 entitlement, and no perfect ratio. |
| `G12_consistent_donor` | Reciprocal, F=N=6, streak 6, M=8/V=2/L=2, Strength 80: Favored, C=10, B=3.25, 32500 infantry/16250 fuel. |
| `G12_reciprocal_ratio_streak_wrath_boundaries` | 4/5 ratio, streak 2, Wrath 39.999 qualifies; 3/4 ratio, streak 1, or Wrath 40 blocks Favored. |
| `G12_exaction_ratio_and_exceptional_boundaries` | 9/10 with streak 4 qualifies; 8/9 fails; four fulfilled plus V+E=2 qualifies, V+E=1.999 does not. |
| `G12_ambiguity_standing_boundaries` | Ambiguity Favored gate uses streak 3; two failures at 50% can be Respected, three cannot. |
| `G12_no_chosen_doctrine_boundaries` | Doctrine zero shares ambiguity's Favored gate; two failures still block Respected under the default ceiling. |
| `G12_unresolved_terminal_invariant` | Issued 3 with two terminal fulfillments leaves unresolved/unfrozen; no standing, outcome, or entitlement is fabricated. |
| `G12_invalid_ledger_counts_and_subsets` | Invalid retirements, inconsistent original/substitute tally, negative count, or voluntary quantity exceeding total prevents freeze. |
| `G12_identity_inheritance_and_closed_contract` | One exact inherited generation is accepted under the parent fixture; wrong owner/origin, older generation, open tuple, or demand-active blocks freeze. |
| `G12_repaired_prior_hostility_recovery` | Each of prior defiance/war/occupation/treaty break remains Distrusted without acceptance; accepted recovery with 1/2/4 post-fulfillments yields Distrusted/Respected/Favored when all other gates hold. Lifetime ratio remains lifetime; a post-acceptance refusal blocks Favored. |
| `G12_enemy_priority_and_strict_wrath` | Actual outstanding treaty/major offense, opt-out, defiance, current war, controlled/owned core, Wrath 80.001, or three applicable refusals is Enemy with 0/0 entitlement. Wrath 80 alone is not Enemy. |
| `G12_emergency_pp_and_no_fabricated_material` | 500 emergency PP is 1000 emergency milli with zero material; emergency-only Respected gets 0/0. Arbitrarily large coarse aid/compliance/history counts add no contract or material credit. |
| `G12_weak_host_capability` | Consistent donor at Strength 20 receives 17500/8750 frozen entitlement. Actual funding and proportional delivery remain parent cases. |
| `G12_strong_low_contribution_and_integer_floor` | Reciprocal F=2, M=3/V=1, Strength 100 yields 13125/6562; 6562.5 is floored. One combined material package/one fulfillment cannot satisfy Favored streak. |
| `G12_entitlement_ceilings_and_actual_uncapped_snapshot` | High Favored caps at 50000/25000; default Respected M=3/Strength 80 gives 2550/1275; huge actual material remains uncapped in history while normalized bound and Respected 10000/5000 ceilings hold. |
| `G12_reentry_replay_temp_lifetimes_and_missing_inputs` | Re-entry preserves actual quantities; frozen inputs and entitlements resist replay/live-input changes; nested outputs survive only when preinitialized; missing authorization or ledger cannot initialize/grade. |

Exact subset premium and PP exclusions are tested by executing actual normalization and entitlement source.
The utility source handles missing input with zero output.
The historical replay test modeled that changing live paid quantity, Wrath, or host frozen capability after participant freeze cannot rewrite entitlement.
No simplification of the assigned grading design was used.

## Read references and revisions

Repo skills used: `.agents/skills/chaos-redux-events/SKILL.md` and `.agents/skills/chaos-redux-subagents/SKILL.md`; no skill was created or changed.
Read `AGENTS.md`, the full assigned design, current settlement/core/lifecycle/constants owners, and relevant existing dynamic-effect documentation/source before designing utilities.
The generic dynamic-effect owner has inline population floor correction at lines 674–681, but no standalone matching floor helper; the assigned utility extracts this bounded pattern locally without modifying that shared file.

Installed root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Offline root: this workspace's `paradox_wiki`.
Only offline Paradox references were used.

| Path relative to reference root | Read spans and rule | Source revision |
| --- | --- | --- |
| Installed `documentation\script_concept_documentation.md` | 216–222, explicit scoped-variable `constant:` access and supported-field limit; live reference read. | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md` | 1–34, schema must be first; int versus fixed_point; live reference read. | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Installed `documentation\effects_documentation.md` | 2681–2694 clamp_temp_variable; 2713–2722 clear_array; 6476–6485 round_temp_variable, live reference reads; 3587–3599 division, 5012–5043 multiplication, 7820–7840 assignment, 6496–6511 target definitions read locally. | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\triggers_documentation.md` | 2110–2153 variable comparisons; 5006–5058 has_variable/has_war_with, locally read. | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Offline `Data structures - Hearts of Iron 4 Wiki.md` | 425–434 variable precision, live read; 435–480 temp lifetime/unscoped versus scoped normal values; 1069–1123 arrays; 303–327 regular-target lifetime; 102–126 boolean country flags, local reads. | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `Triggers - Hearts of Iron 4 Wiki.md` | 329–373 flow control, NOT is NOR; local read. | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Offline `Effects - Hearts of Iron 4 Wiki.md` | 4683–4714 scripted effects and plain `= yes` invocation; local read. | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `Scopes - Hearts of Iron 4 Wiki.md` | 52–76 effect/trigger scope domains and examples; 90–139 effect limits and scope behavior; local read. | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Installed `common\scripted_effects\zz_debug_effects.txt` | 42–98 `d_add_fake_armies`, underlying read; live `source_lookup` 72–83 explicitly shows caller temp, multiply, round, clamp. Only that arithmetic structure is a precedent; its debug gameplay is not copied. | Lookup index `c73b36ff412e1c4ef463c8b1e3b0500f73bc9618a0862f861ee953e36dd318dc`; file SHA `a047040b0fe3b4672d5c2a46abe4771e23b5ca3a621b1c4060291f9ecfb82bef` |

## MCP artifacts and unsupported evidence

Live exposure was verified for `hoi4.reference_context/search/read`, `hoi4.source_lookup`, and `hoi4.event_inspect/render/compare`, then those routes were called.
Live reference/source calls established functioning service responses for workspace `mod_chaos_redux_ea3b2d67c2c0`.
The initial event context bundle reported omitted On actions and Localisation sources; no such source edit is in this assignment, and the bundle is not claimed as a full detailed reference read.
The detailed arithmetic sections were targeted separately.
The live source lookup schema offers line bounds but no `view/keyPath`; no unsupported structure paging was used.

`hoi4.event_inspect`, selector `{ kind: event, eventId: chaosx.nr12.608 }`, depth 1/nodes 4/edges 6/no helpers returned `EVENT_INSPECTED_PARTIAL`.
Revision: `828ca59a9a1fa1a44d0bf5a12bce75e5cb65e717d2d055388d5ac1994d71fe92`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2fd6618ecd24529d169219464846ab95c3bf13cae76304f0014c6a08914805c/5ba166ea59b278a6c8e3ace25a6f2f3614e9cfd13678938646859ac4c40782bf/event-trace-828ca59a9a1f.json`.
The focused route reported zero helper projections and deferred lifecycle passes, so this is direct event-source evidence only.

`hoi4.event_render` options for the same event/depth 1/nodes 2/no helpers returned `EVENT_RENDERED_PARTIAL` at the same revision.
Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/820544b9d34f493a354fd6d8a19507fb7d117f075c0e6c42b68d79fc7928a149/743aa3f4112cb112567b5a97a53108d1a93794177800274b09769c881f93c2d0/event-options-828ca59a9a1f-manifest.json`.
PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4eb3a154be6714cb16ecf1005d5529b98ee13e5f12c3a703fe3f25e667572fc7/ea275dd241a43e3749071715eee78b950dfe0bab8548838fe50713bb6afa002c/event-options-828ca59a9a1f.png`.
No visual acceptance is claimed from that artifact; this assignment changes no event presentation.

`hoi4.event_compare` requested the retained pre-edit revision with the same event selection and bounded limits; it returned `EVENT_REVISION_NOT_CACHED`: “Requested event graph revision is not cached or retained as a graph artifact.”
No before/after comparison was established.
A trace/render artifact was not falsely substituted for a graph-bearing cache.
The parent needs an integrated revision-backed comparison after its call sites are installed.
No timeout result was observed; no broad retry or server change was made.
Two initial selector-shape validation errors were corrected narrowly to the confirmed discriminator/eventId form before the successful inspection.

`hoi4.script_validate` is not exposed in the connected tools, so installed-documentation scope validation through that route is blocked.
The connected health/version route and client task negotiation were not verified; helper_expansion, jobs, cancellation, and native tasks were not used.
The seventeen fixtures are actual-source arithmetic/logic evidence only and do not replace missing MCP helper lifecycle or native/runtime validation.
No probability pass applies to these deterministic helpers.
The parent owns any affected decision AI availability/score audit through its separate probability auditor.

## Simplifications, omissions, and blockers

No assigned design factor, quantity kind, doctrine gate, recovery barrier, reward formula, or grading snapshot was simplified or omitted.
No fallback was introduced.
The helper tranche is reusable and documented, but Event 012 is not declared complete.

**Historical integration collision, resolved by parent:** the original worker duplicated `gods_of_africa_contract_close`.
Current grading constants do not declare it.
The sole contract-constants owner and its callers use `war_breach = 5`; no parent owner was edited by this arithmetic repair.

Parent-required work: actual native payment/receipt and conduct owners, unique contract closures including neutral retirement, initialized first-history call, guarded final classifier aliases, authoritative host capability snapshots, source-funded obligations/delivery/recovery, UI/category/localisation bindings, final documentation/catalog alignment, combined source/MCP reviews, and publication.
Required checks skipped here: parent call-site execution, native inventory deltas, closure-owner scenarios, conduct observation/core scenarios, integrated lifecycle comparison, and rendered UI acceptance, because those sources are not owned by this assignment.
Full native/runtime acceptance is unsupported by this worker and remains parent/user-owned under repository policy.

## Historical original-source fixture runner

Run this code from the mod root through Python stdin.
It writes no files.
Its external-parent fixture boundary and conservative temp-frame model are explicit in the code.
This original runner is retained as historical provenance; it does not model conservative native-range storage or the current trigger-side integer checks.
Use the companion arithmetic-repair runner for current source checks; it reruns these seventeen families under three-decimal bounded storage and adds the required stress cases.

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
            elif k=='round_temp_variable':self.temps[v]=self.val(v).quantize(D(1),rounding=ROUND_HALF_UP)
            elif k in ['clamp_temp_variable','clamp_variable']:
                d={a:c for a,o,c in v};store=self.temps if 'temp' in k else self.vars
                value=self.val(d['var']);value=max(value,self.val(d['min'])) if 'min' in d else value;value=min(value,self.val(d['max'])) if 'max' in d else value
                store[d['var']]=value
            elif k in ['set_variable','set_temp_variable','multiply_variable','multiply_temp_variable','add_to_variable','add_to_temp_variable','subtract_from_temp_variable','divide_temp_variable']:
                store=self.temps if 'temp' in k else self.vars
                for a,o,c in v:
                    q=self.val(c);old=self.val(a)
                    val=q if k.startswith('set_') else old*q if k.startswith('multiply_') else old+q if k.startswith('add_') else old-q if k.startswith('subtract_') else old/q
                    store[a]=val.quantize(D('.00001'),rounding=ROUND_DOWN)
            else:raise AssertionError(('unknown effect',k))
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
print(json.dumps({'casesPassed':passed,'caseCount':len(passed),'effects':len(E),'triggers':len(T),'scope':'actual helper source; parent external identity trigger fixture boundary; no native or runtime claims','sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in ['common/scripted_effects/012_africa_gods_grading_effects.txt','common/scripted_triggers/012_africa_gods_grading_triggers.txt','common/script_constants/012_africa_gods_grading_constants.txt']}},indent=2))
```


## Parent ownership reconciliation

The parent removes the duplicate `gods_of_africa_contract_close` declaration from the grading constants file and retains one definition in `012_africa_gods_contract_constants.txt`.
The unique contract owner and its callers use `.war_breach = 5` consistently.
The original worker checksum above records its handoff snapshot; the current parent-reviewed source has this bounded integration correction.
The grading initializer must run before the contract initializer in the first-genuine-history branch because its no-backfill guard rejects an already present `gods_of_africa_demands_issued` field.
No initializer runs on retained history.

The parent review also replaces the normalizer's large raw-unit intermediates with a precomputed exact scale for the accepted denominators.
The original manpower path reached 160,000,000 before division, beyond the conservative audit range, despite the worker's unbounded arithmetic model passing.
The installed math-expression documentation confirms fixed-point arithmetic but does not establish every ordinary variable/getter's exact width or precision; the offline Variables paragraph reports a wider five-decimal representation.
The conservative three-decimal/range model is source-review evidence, not observed native overflow behavior.
The current source computes `scale = 1000 * 1000 / denominator`, clamps the quantity to `bound_milli / scale`, and multiplies once.
The largest scale intermediate is 1,000,000, normalization output remains at most 16,000, and one manpower (`0.001k`) still yields `0.1` milli-package.
That parent correction was retained by the F1?F5 arithmetic repair.
The current companion runner enforces three-decimal bounded storage; its cases remain source-model evidence, and independent parent re-review is still required.
The original source fixture pass alone did not cover arithmetic overflow.
