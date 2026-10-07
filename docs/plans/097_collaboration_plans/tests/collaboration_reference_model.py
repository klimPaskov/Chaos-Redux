"""Pure design reference model for Event 097. This is NOT HOI4 code.

The model assumes a normalized native scale of 0..100 and receives P/T, legal
territory, and other native facts as inputs. Passing tests proves only that this
Python implementation of selected design rules has the asserted arithmetic.
It does not verify engine commands, callbacks, native caps, DLC support, identity
persistence, government creation, observer completeness, or multiplayer behavior.

Run with Python 3.10+ using only the standard library:
    python collaboration_reference_model.py --output model_results.json
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass, field
from decimal import Decimal
import io
import itertools
import json
import math
from pathlib import Path
import random
import unittest

CAP = 100.0

def percentage(value: float) -> float:
    if not math.isfinite(value) or not 0 <= value <= CAP:
        raise ValueError('Expected a finite normalized percentage in [0, 100].')
    return float(value)

def normal_grant(active: set[str]) -> int:
    if not active <= {'I','II','III','IV'}:
        raise ValueError('Unknown evolution.')
    return 25 if active & {'II','IV'} else 20 if 'I' in active else 10

@dataclass
class World:
    collaboration: dict[tuple[str,str],float] = field(default_factory=dict)
    delivered: set[str] = field(default_factory=set)

    def fire(self, firing: str, countries: list[str], grant: float) -> dict:
        if not firing:
            raise ValueError('A genuine firing identity is required.')
        if grant < 0 or not math.isfinite(grant):
            raise ValueError('Grant must be nonnegative and finite.')
        if firing in self.delivered:
            return {'pairs':0,'gain':0.0,'crossed_targets':0,'chaos':0,'replay':True}
        roster = tuple(dict.fromkeys(countries))
        if any(not c for c in roster):
            raise ValueError('Countries need explicit identities.')
        before = {(a,b):percentage(self.collaboration.get((a,b),0.0))
                  for a in roster for b in roster if a != b}
        crossed = set()
        gain = 0.0
        for (a,b), old in before.items():
            new = min(CAP, old + grant)
            self.collaboration[a,b] = new
            gain += new-old
            if old < 50 <= new:
                crossed.add(b)
        self.delivered.add(firing)
        chaos = 0 if gain == 0 else 5 + (5 if 2*len(crossed) >= len(roster) else 0)
        return {'pairs':len(before),'gain':gain,'crossed_targets':len(crossed),
                'chaos':chaos,'replay':False}

@dataclass
class Administration:
    offered: dict[tuple[str,str,str],float] = field(default_factory=dict)

    def apply(self, identity: tuple[str,str,str], collaboration: float,
              compliance: float, eligible: bool = True) -> tuple[float,float]:
        c, current = percentage(collaboration), percentage(compliance)
        if not eligible or c < 50:
            return current,0.0
        floor = min(80.0,c+20.0)
        previous = self.offered.get(identity)
        if previous is None:
            after = max(current,floor)
        elif floor > previous:
            after = max(current,min(floor,current+floor-previous))
        else:
            after = current
        self.offered[identity] = max(floor,previous or 0.0)
        return after,after-current

@dataclass
class Stages:
    first_day: int | None = None
    final_resolved: bool = False

    def evaluate(self, *, day: int, progress: float, threshold: float,
                 collaboration: float, war: bool = True, foothold: bool = True,
                 capitulated: bool = False, enabled: bool = True,
                 exists: bool = True) -> tuple[float,int | None]:
        c=percentage(collaboration)
        if not (0 <= progress <= 1) or not math.isfinite(progress):
            raise ValueError('Progress must be finite and in [0,1].')
        valid = (enabled and exists and war and foothold and not capitulated
                 and c >= 50 and progress >= .25 and threshold > 0
                 and math.isfinite(threshold) and progress < threshold)
        if not valid:
            return c,None
        # Decimal cross-products preserve exact design boundaries such as 0.60/0.80.
        # The real game must use its verified native numeric precision.
        p100=Decimal(str(progress))*100
        t=Decimal(str(threshold))
        if self.first_day is None and p100 >= t*75:
            self.first_day=day
            return min(CAP,c+10),1
        if (self.first_day is not None and not self.final_resolved
            and day >= self.first_day+5 and p100 >= t*90):
            self.final_resolved=True
            return min(CAP,c+15),2
        return c,None

@dataclass
class Readiness:
    used: set[tuple[str,str]] = field(default_factory=set)

    def offer(self, pair: tuple[str,str], *, pre_defeat_c: float | None,
              current_c: float, q: float, states: dict[str,float],
              eligible_states: set[str], valid_defeat: bool,
              native_supported: bool = True) -> dict[str,float]:
        q=percentage(q)
        c=percentage(pre_defeat_c if pre_defeat_c is not None else current_c)
        out={s:percentage(v) for s,v in states.items()}
        if (not valid_defeat or not native_supported or c < 60 or pair in self.used
            or not eligible_states or not eligible_states <= states.keys()):
            return out
        self.used.add(pair)
        for s in eligible_states:
            out[s]=max(out[s],q)
        return out

def government_preference(*, shortage:bool=False, broad:bool=False,
                          treaty:bool=False, essential:bool=False,
                          unsafe:bool=False, legal:bool=True) -> tuple[int,str]:
    score=50+25*shortage+20*broad+20*treaty-30*essential-25*unsafe
    return score,('ineligible' if not legal else 'install' if score>=60 else 'retain')

@dataclass
class CohortTimer:
    cohort: tuple[str,...] | None=None
    start: int | None=None

    def observe(self, day:int, cohort:tuple[str,...], all_valid:bool,
                required_days:int=180) -> bool:
        if not all_valid:
            self.cohort=None
            self.start=None
            return False
        if self.cohort != cohort or self.start is None:
            self.cohort=cohort
            self.start=day
        return day-self.start >= required_days

class ReferenceTests(unittest.TestCase):
    def test_01_three_countries_six_directed_pairs(self):
        w=World();r=w.fire('f1',['A','B','C'],10)
        self.assertEqual(r['pairs'],6)
        self.assertEqual(r['gain'],60)
        self.assertTrue(all(a!=b for a,b in w.collaboration))
    def test_02_asymmetry_is_preserved(self):
        w=World({('A','B'):45,('B','A'):10});w.fire('f1',['A','B'],10)
        self.assertEqual((w.collaboration['A','B'],w.collaboration['B','A']),(55,20))
    def test_03_cap_and_actual_gain(self):
        w=World({('A','B'):95,('B','A'):100});r=w.fire('f1',['A','B'],10)
        self.assertEqual(r['gain'],5)
        self.assertEqual(w.collaboration['A','B'],100)
    def test_04_replay_is_not_a_repeat(self):
        w=World();w.fire('f1',['A','B'],10);r=w.fire('f1',['A','B'],10)
        self.assertEqual(r['gain'],0);self.assertEqual(r['chaos'],0)
        w.fire('f2',['A','B'],10);self.assertEqual(w.collaboration['A','B'],20)
    def test_05_new_country_gets_no_history(self):
        w=World();w.fire('1',['A','B'],10);w.fire('2',['A','B'],10)
        w.fire('3',['A','B','C'],10)
        self.assertEqual(w.collaboration['A','B'],30)
        self.assertEqual(w.collaboration['A','C'],10)
    def test_06_native_operation_between_firings(self):
        w=World();w.fire('1',['A','B'],10);w.collaboration['A','B']+=30
        w.fire('2',['A','B'],10);self.assertEqual(w.collaboration['A','B'],50)
    def test_07_saturated_world_is_zero_impact(self):
        w=World({('A','B'):100,('B','A'):100});r=w.fire('1',['A','B'],25)
        self.assertEqual((r['gain'],r['chaos']),(0,0))
    def test_08_distinct_targets_not_pairs(self):
        w=World({('A','C'):45,('B','C'):45,('D','C'):45})
        r=w.fire('1',['A','B','C','D'],10)
        self.assertEqual((r['crossed_targets'],r['chaos']),(1,5))
    def test_09_half_world_breadth_increment(self):
        w=World({('A','C'):45,('B','D'):45});r=w.fire('1',['A','B','C','D'],10)
        self.assertEqual((r['crossed_targets'],r['chaos']),(2,10))
    def test_10_duplicate_roster_does_not_multiply(self):
        w=World();self.assertEqual(w.fire('1',['A','A','B'],10)['pairs'],2)
    def test_11_all_toggle_combinations(self):
        self.assertEqual(normal_grant(set()),10)
        self.assertEqual(normal_grant({'I'}),20)
        self.assertEqual(normal_grant({'III'}),10)
        self.assertEqual(normal_grant({'II'}),25)
        self.assertEqual(normal_grant({'IV'}),25)
        self.assertEqual(normal_grant({'I','II','III','IV'}),25)
        for bits in itertools.product([False,True],repeat=4):
            active={stage for stage,on in zip(('I','II','III','IV'),bits) if on}
            expected=25 if active & {'II','IV'} else 20 if 'I' in active else 10
            self.assertEqual(normal_grant(active),expected)
    def test_12_randomized_monotonic_clamp(self):
        rng=random.Random(97)
        for _ in range(500):
            a,b=rng.uniform(0,100),rng.uniform(0,100);g=rng.choice([10,20,25])
            w=World({('A','B'):a,('B','A'):b});w.fire('1',['A','B'],g)
            self.assertAlmostEqual(w.collaboration['A','B'],min(100,a+g))
            self.assertGreaterEqual(w.collaboration['B','A'],b)
    def test_13_administration_threshold(self):
        a=Administration();key=('A','B','S')
        self.assertEqual(a.apply(key,45,20),(20,0))
        self.assertNotIn(key,a.offered)
        self.assertEqual(a.apply(key,50,20),(70,50))
    def test_14_early_offer_cap(self):
        a=Administration();self.assertEqual(a.apply(('A','B','S'),100,20),(80,60))
    def test_15_higher_compliance_preserved_and_spent(self):
        a=Administration();k=('A','B','S');self.assertEqual(a.apply(k,50,95),(95,0))
        self.assertEqual(a.apply(k,50,20),(20,0))
    def test_16_recapture_does_not_restore(self):
        a=Administration();k=('A','B','S');a.apply(k,50,20)
        self.assertEqual(a.apply(k,50,25),(25,0))
    def test_17_only_incremental_offer_paid(self):
        a=Administration();k=('A','B','S');a.apply(k,50,20)
        self.assertEqual(a.apply(k,60,25),(35,10))
    def test_18_native_lowering_does_not_clear_history(self):
        a=Administration();k=('A','B','S');a.apply(k,60,20)
        a.apply(k,20,10);self.assertEqual(a.apply(k,60,10),(10,0))
    def test_19_peaceful_transfer_is_not_eligible(self):
        a=Administration();k=('A','B','S');self.assertEqual(a.apply(k,80,20,False),(20,0))
        self.assertNotIn(k,a.offered)
    def test_20_rival_native_network_is_separate(self):
        a=Administration();a.apply(('A','B','S'),60,20)
        self.assertEqual(a.apply(('C','B','S'),50,10),(70,60))
    def test_21_proximity_boundary(self):
        s=Stages();self.assertEqual(s.evaluate(day=0,progress=.59,threshold=.8,collaboration=60),(60,None))
        self.assertEqual(s.evaluate(day=0,progress=.60,threshold=.8,collaboration=60),(70,1))
    def test_22_five_day_separation(self):
        s=Stages();s.evaluate(day=0,progress=.75,threshold=.8,collaboration=60)
        self.assertEqual(s.evaluate(day=0,progress=.75,threshold=.8,collaboration=70),(70,None))
        self.assertEqual(s.evaluate(day=4,progress=.75,threshold=.8,collaboration=70),(70,None))
        self.assertEqual(s.evaluate(day=5,progress=.75,threshold=.8,collaboration=70),(85,2))
    def test_23_recovery_stops_pending_award(self):
        s=Stages();s.evaluate(day=0,progress=.65,threshold=.8,collaboration=60)
        self.assertEqual(s.evaluate(day=5,progress=.3,threshold=.8,collaboration=70),(70,None))
        self.assertFalse(s.final_resolved)
    def test_24_later_decline_can_use_unspent_stage(self):
        s=Stages();s.evaluate(day=0,progress=.65,threshold=.8,collaboration=60)
        s.evaluate(day=5,progress=.3,threshold=.8,collaboration=70)
        self.assertEqual(s.evaluate(day=20,progress=.75,threshold=.8,collaboration=70),(85,2))
    def test_25_absolute_progress_floor(self):
        s=Stages();self.assertEqual(s.evaluate(day=0,progress=.2,threshold=.22,collaboration=80),(80,None))
    def test_26_live_guards(self):
        for args in [dict(war=False),dict(foothold=False),dict(enabled=False),dict(exists=False),dict(capitulated=True)]:
            with self.subTest(args=args):
                s=Stages();self.assertEqual(s.evaluate(day=0,progress=.65,threshold=.8,collaboration=60,**args),(60,None))
    def test_27_invalid_threshold_and_already_defeated(self):
        for p,t in [(0.5,0),(0.9,.8),(.8,.8)]:
            with self.subTest(p=p,t=t):
                self.assertEqual(Stages().evaluate(day=0,progress=p,threshold=t,collaboration=60),(60,None))
    def test_28_spent_stages_do_not_replenish(self):
        s=Stages();s.evaluate(day=0,progress=.75,threshold=.8,collaboration=60)
        s.evaluate(day=5,progress=.75,threshold=.8,collaboration=70)
        self.assertEqual(s.evaluate(day=365,progress=.75,threshold=.8,collaboration=60),(60,None))
    def test_29_capped_stage_has_no_overflow(self):
        s=Stages();self.assertEqual(s.evaluate(day=0,progress=.75,threshold=.8,collaboration=100),(100,1))
        self.assertEqual(s.evaluate(day=5,progress=.75,threshold=.8,collaboration=100),(100,2))
    def test_30_saved_stage_reconstruction(self):
        s=Stages();s.evaluate(day=10,progress=.75,threshold=.8,collaboration=60)
        restored=Stages(**json.loads(json.dumps(s.__dict__)))
        self.assertEqual(restored.evaluate(day=15,progress=.75,threshold=.8,collaboration=70),(85,2))
    def test_31_pre_defeat_network_not_post_conversion_zero(self):
        r=Readiness();out=r.offer(('A','B'),pre_defeat_c=60,current_c=0,q=80,
              states={'S':20},eligible_states={'S'},valid_defeat=True)
        self.assertEqual(out,{'S':80})
    def test_32_foreign_state_not_touched(self):
        r=Readiness();out=r.offer(('A','B'),pre_defeat_c=60,current_c=0,q=80,
              states={'S':20,'foreign':10},eligible_states={'S'},valid_defeat=True)
        self.assertEqual(out,{'S':80,'foreign':10})
    def test_33_government_offer_once(self):
        r=Readiness();kwargs=dict(pre_defeat_c=60,current_c=0,q=80,states={'S':20},eligible_states={'S'},valid_defeat=True)
        r.offer(('A','B'),**kwargs);self.assertEqual(r.offer(('A','B'),**kwargs),{'S':20})
    def test_34_native_requirement_is_an_input(self):
        r=Readiness();out=r.offer(('A','B'),pre_defeat_c=60,current_c=0,q=85,
              states={'S':90,'T':20},eligible_states={'S','T'},valid_defeat=True)
        self.assertEqual(out,{'S':90,'T':85})
    def test_35_unsupported_native_route_stays_blocked(self):
        r=Readiness();out=r.offer(('A','B'),pre_defeat_c=60,current_c=0,q=80,
              states={'S':20},eligible_states={'S'},valid_defeat=True,native_supported=False)
        self.assertEqual(out,{'S':20});self.assertFalse(r.used)
    def test_36_ai_policy_examples(self):
        self.assertEqual(government_preference(),(50,'retain'))
        self.assertEqual(government_preference(shortage=True),(75,'install'))
        self.assertEqual(government_preference(broad=True),(70,'install'))
        self.assertEqual(government_preference(shortage=True,essential=True),(45,'retain'))
        self.assertEqual(government_preference(treaty=True),(70,'install'))
        self.assertEqual(government_preference(treaty=True,unsafe=True),(45,'retain'))
    def test_37_ai_legality_overrides_score(self):
        self.assertEqual(government_preference(shortage=True,treaty=True,legal=False)[1],'ineligible')
    def test_38_fixed_cohort_interval(self):
        t=CohortTimer();c=('1','2','3','4','5')
        self.assertFalse(t.observe(0,c,True));self.assertFalse(t.observe(179,c,True))
        self.assertTrue(t.observe(180,c,True))
    def test_39_broken_condition_resets(self):
        t=CohortTimer();c=('1','2','3','4','5');t.observe(0,c,True)
        t.observe(100,c,False);t.observe(110,c,True)
        self.assertFalse(t.observe(180,c,True));self.assertTrue(t.observe(290,c,True))
    def test_40_cohort_substitution_restarts(self):
        t=CohortTimer();t.observe(0,('1','2','3','4','5'),True)
        self.assertFalse(t.observe(180,('1','2','3','4','6'),True))
    def test_41_input_guards(self):
        for bad in [-1,101,float('nan')]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):percentage(bad)
    def test_42_country_order_does_not_change_normal_matrix(self):
        start={('A','B'):45,('B','C'):95,('C','A'):50}
        a,b=World(dict(start)),World(dict(start))
        ra=a.fire('1',['A','B','C'],20);rb=b.fire('1',['C','A','B'],20)
        self.assertEqual(a.collaboration,b.collaboration);self.assertEqual(ra,rb)

    def test_43_exact_final_proximity_boundary(self):
        s=Stages();s.evaluate(day=0,progress=.6,threshold=.8,collaboration=60)
        self.assertEqual(s.evaluate(day=5,progress=.72,threshold=.8,collaboration=70),(85,2))
    def test_44_immediately_below_both_boundaries(self):
        s=Stages()
        self.assertEqual(s.evaluate(day=0,progress=.599999,threshold=.8,collaboration=60),(60,None))
        s.evaluate(day=0,progress=.6,threshold=.8,collaboration=60)
        self.assertEqual(s.evaluate(day=5,progress=.719999,threshold=.8,collaboration=70),(70,None))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('model_results.json'))
    args=parser.parse_args()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(ReferenceTests)
    ids=[test.id() for test in suite]
    stream=io.StringIO()
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    report={'scope':'Selected design arithmetic only, not HOI4 implementation',
            'native_cap_assumption':'Normalized 0..100, not installed-engine verification',
            'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
            'successful':result.wasSuccessful(),'randomized_cases_in_test_12':500,
            'native_engine_validation':False,'independent_subagent_review':False,
            'test_ids':ids,'output':stream.getvalue()}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(stream.getvalue())
    raise SystemExit(0 if result.wasSuccessful() else 1)
