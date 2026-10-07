"""Parent-authored symbolic design fixtures for Doctor Wu Part 7.

This is NOT Clausewitz code, an engine emulator, a biological simulation,
or evidence that the proposed shared interfaces are implemented.
Run with Python 3.10+ to reproduce the arithmetic and conservation examples.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
import json
import math


@dataclass
class CohortModel:
    """Individual IDs make the proposed first-settlement invariant explicit."""
    people: dict[int, str] = field(default_factory=dict)
    orders: set[str] = field(default_factory=set)
    receipts: set[str] = field(default_factory=set)
    stock: dict[str, float] = field(default_factory=dict)
    first_settled: set[int] = field(default_factory=set)
    before_settlement_dead: set[int] = field(default_factory=set)
    later_dead: set[int] = field(default_factory=set)
    appointments: set[int] = field(default_factory=set)
    transfers: dict[str, tuple[str, tuple[int, ...], str]] = field(default_factory=dict)

    def birth(self, order: str, count: int, location: str = 'nursery') -> int:
        if count < 0:
            raise ValueError('The actual living count cannot be negative.')
        if order in self.orders:
            return 0
        self.orders.add(order)
        start = len(self.people)
        self.people.update({start+i: location for i in range(count)})
        self.stock[location] = self.stock.get(location, 0)+count
        return count

    def at(self, location: str) -> list[int]:
        return [p for p,s in self.people.items() if s == location and p not in self.first_settled and p not in self.before_settlement_dead]

    def settle(self, receipt: str, count: int, destination: str, location: str = 'nursery') -> tuple[int, ...]:
        if destination not in {'civilian', 'military_pool', 'formation'}:
            raise ValueError('The fixture has only three first-settlement destinations.')
        if count < 0:
            raise ValueError('A settlement request cannot be negative.')
        if receipt in self.receipts:
            return ()
        allowed = min(count, len(self.at(location)), max(0, math.floor(self.stock.get(location,0))))
        ids = tuple(self.at(location)[:allowed])
        self.receipts.add(receipt)
        self.stock[location] = self.stock.get(location,0)-allowed
        for p in ids:
            self.first_settled.add(p)
            self.people[p] = destination
        return ids

    def appoint(self, person: int) -> bool:
        if person not in self.first_settled or self.people[person] != 'civilian' or person in self.later_dead:
            return False
        old = len(self.appointments)
        self.appointments.add(person)
        return len(self.appointments) != old

    def death_before(self, count: int, location: str = 'nursery') -> int:
        ids = self.at(location)[:count]
        self.before_settlement_dead.update(ids)
        for p in ids:
            self.people[p] = 'dead_before_settlement'
        self.stock[location] = self.stock.get(location,0)-len(ids)
        return len(ids)

    def death_after(self, person: int) -> bool:
        if person not in self.first_settled or person in self.later_dead:
            return False
        self.later_dead.add(person)
        return True

    def depart(self, receipt: str, count: int, origin: str = 'nursery') -> tuple[int, ...]:
        if receipt in self.transfers:
            return ()
        ids = tuple(self.at(origin)[:count])
        self.stock[origin] -= len(ids)
        transit = 'transit:'+receipt
        self.stock[transit] = len(ids)
        for p in ids:
            self.people[p] = transit
        self.transfers[receipt] = (origin, ids, 'pending')
        return ids

    def finish_transfer(self, receipt: str, destination: str | None) -> int:
        origin,ids,status = self.transfers[receipt]
        if status != 'pending':
            return 0
        target = origin if destination is None else destination
        for p in ids:
            self.people[p] = target
        self.stock['transit:'+receipt] = 0
        self.stock[target] = self.stock.get(target,0)+len(ids)
        self.transfers[receipt] = (origin,ids,'returned' if destination is None else 'delivered')
        return len(ids)

    def invariant(self) -> bool:
        unsettled = set(self.people)-self.first_settled-self.before_settlement_dead
        return (len(self.people) == len(unsettled)+len(self.first_settled)+len(self.before_settlement_dead)
                and not self.first_settled.intersection(self.before_settlement_dead)
                and self.later_dead.issubset(self.first_settled))


def run() -> dict:
    results=[]
    def check(name: str, condition: bool, meaning: str) -> None:
        if not condition:
            raise AssertionError(name)
        results.append({'fixture':name,'result':'pass','meaning':meaning})

    c=CohortModel()
    check('F01 actual birth',c.birth('paid_order',1000)==1000 and c.invariant(),'One fictional living milestone creates 1,000 new IDs.')
    check('F02 repeated birth callback',c.birth('paid_order',1000)==0 and len(c.people)==1000,'Repeated order completion creates no new people.')
    mp=c.settle('military',600,'military_pool')
    civ=c.settle('civilian',250,'civilian')
    check('F03 split first settlement',len(mp)==600 and len(civ)==250 and len(c.at('nursery'))==150,'The example has 850 historical first settlements and 150 remaining.')
    check('F04 repeat first settlement',c.settle('military',600,'military_pool')==(),'A repeated receipt does not settle more people.')
    check('F05 specialist overlay',all(c.appoint(p) for p in civ[:5]) and len(c.people)==1000,'Five appointments overlay already counted civilian people.')
    check('F06 repeated appointment',not c.appoint(civ[0]),'The same named appointment does not repeat.')
    check('F07 unissued appointment rejected',not c.appoint(c.at('nursery')[0]),'An unissued candidate is not counted as a qualified civilian-role carrier.')
    check('F08 military appointment is not new civilian credit',not c.appoint(mp[0]),'Ordinary manpower settlement is not a second civilian admission.')
    check('F09 actual pre-settlement death',c.death_before(10)==10 and c.invariant(),'1,000 = 140 unsettled + 850 first-settled + 10 deaths before settlement.')
    check('F10 later military death',c.death_after(mp[0]) and c.invariant() and len(c.first_settled)==850,'Later death does not reopen the historical entitlement.')
    check('F11 repeated later death',not c.death_after(mp[0]),'A repeated report does not count the same later death twice in this fixture.')
    check('F12 no over-redemption',len(c.settle('remaining',1000,'civilian'))==140 and c.invariant(),'Only the remaining 140 people can settle.')
    check('F13 exhausted cohort',not c.settle('extra',1,'military_pool'),'An exhausted cohort cannot award another person.')

    t=CohortModel()
    t.birth('transfer_order',1000)
    check('F14 exact departure',len(t.depart('transfer_200',200))==200 and len(t.at('nursery'))==800 and t.invariant(),'Only 200 people enter transit.')
    check('F15 repeated departure',not t.depart('transfer_200',200),'A second callback cannot remove a second group.')
    check('F16 exact receipt',t.finish_transfer('transfer_200','recipient')==200 and len(t.at('recipient'))==200,'The recipient receives 200, not the original 1,000-person order.')
    check('F17 delivered group cannot be refunded',t.finish_transfer('transfer_200',None)==0 and len(t.at('nursery'))==800,'Return and delivery cannot both settle the same transfer.')
    check('F18 recipient first settlement',len(t.settle('recipient_issue',200,'civilian','recipient'))==200 and t.invariant(),'Transfer preserves, then consumes, the original remaining entitlement.')
    t.depart('return_50',50)
    check('F19 failed delivery with actual return',t.finish_transfer('return_50',None)==50 and len(t.at('nursery'))==800,'This fixture explicitly assumes the people genuinely returned.')
    check('F20 returned group cannot later arrive',t.finish_transfer('return_50','recipient')==0,'A late arrival callback cannot duplicate a returned group.')

    s=CohortModel()
    s.birth('small',10)
    s.stock['nursery']=2.9
    check('F21 fractional stock',len(s.settle('partial',10,'military_pool'))==2,'Physical entitlement is floored, never rounded up.')
    check('F22 missing stock is not death',len(s.before_settlement_dead)==0 and s.invariant(),'An aggregate stock discrepancy records no invented death.')
    s.stock['nursery']=100
    check('F23 unexplained surplus',len(s.settle('surplus',100,'civilian'))==8,'Provenance limits extra stock to eight actually remaining people.')

    check('F24 normal four-cell order',(4*250,4*150,4*1000,4*10)==(1000,600,4000,40),'Normal proposal costs and count agree with the Part 7 table.')
    check('F25 normal ten-cell order',(10*250,10*150,10*1000,10*10)==(2500,1500,10000,100),'The larger order scales real factory cells and materials.')
    check('F26 personal one-person order',(100+10,1000+100,10+5)==(110,1100,15),'One-person direct costs match the proposed formula.')
    check('F27 personal five-person order',(100+5*10,1000+5*100,10+5*5)==(150,1500,35),'Five-person direct costs match the proposed formula.')
    check('F28 accelerated four-cell order',(4*250,4*250,4*2000,4*20)==(1000,1000,8000,80),'Acceleration changes the schedule and costs, not cohort capacity.')
    check('F29 normal military timetable',180+90+90+120==480,'Living milestone, maturation, orientation, and training are separate proposed periods.')
    check('F30 accelerated military timetable',150+60+90+120==420,'Acceleration saves 60 days without shortening orientation or training.')
    check('F31 continuity qualification',60+45+75==180,'Three qualification assignments fill the proposed 180-day period.')
    check('F32 ordinary formation',(5*1000,5*90,5*5*3)==(5000,450,75),'Five battalions require 5,000 people, 450 rifles, and 75 lots for three service intervals.')
    check('F33 enhanced formation',(5*1000,5*90,5*5,5*15)==(5000,450,25,75),'The enhanced profile matches Part 6 inputs without adding the ordinary care bill.')
    check('F34 current legacy reference',100*10==1000,'A legacy stock of 100 at the inspected rate produces 1,000 weekly manpower, separate from finite settlement.')
    check('F35 animation sheet',(10*156,210,Fraction(10,5))==(1560,210,2),'Ten proposed frames at five fps occupy 1,560 by 210 pixels and last two seconds.')

    rate=1/(1-Fraction(20,100))
    work=Fraction(200)
    check('F36 projected specialist time',work/rate==160,'A 20 percent shorter duration is a 1.25 working rate, not completed work at appointment.')
    remaining=work-50*rate
    check('F37 loss preserves only earned work',remaining==Fraction(275,2),'Fifty days of service complete 62.5 work units, leaving 137.5.')
    check('F38 reassignment does not compound',remaining/rate==110 and rate==Fraction(5,4),'Reassignment keeps the same strongest rate, with no second discount.')

    profiles={
        'replication research':['lane','civilian_factory','support_equipment','political_power_or_army_experience'],
        'normal or accelerated production':['civilian_factory','support_equipment','fuel','clinical_material'],
        'specialist apprenticeship':['candidate','civilian_factory','clinical_material','political_power_or_service_experience'],
        'service training':['trainees','training_rifles','clinical_material','army_experience'],
        'ordinary commissioning':['people','rifles','clinical_material','command_power'],
        'enhanced commissioning':['people','rifles','preparation_packs','military_care_packs'],
        'ordinary recall':['people_or_formation','civilian_factory','clinical_material'],
        'military recall':['people_or_formation','civilian_factory','clinical_material','command_power'],
        'archive update':['lane','civilian_factory','support_equipment','political_power'],
        'continuity qualification':['candidate','civilian_factory','clinical_material','political_power'],
        'remedial assignment':['candidate','civilian_factory','clinical_material'],
        'secondary continuity placement':['qualified_copy','civilian_factory','support_equipment','political_power']}
    check('F39 four-cost action budget',all(len(set(v))<=4 for v in profiles.values()),'These declared profiles fit the design ceiling. No native cost consumer was executed.')
    return {'stage':'DW-089-S3','kind':'parent-authored symbolic design and arithmetic fixtures','engine_validation':False,'independent_audit':False,'count':len(results),'results':results,'cost_profiles':profiles,'limits':['The model does not execute game files or native effects.','No population side effect, stock transfer, character role, formation operation, payment callback, or save format is validated.','The receipt and person-ID operations describe intended design semantics only.','Numeric profiles remain proposals.']}


if __name__ == '__main__':
    target=Path(__file__).with_name('2026-09-25_stage_3_design_fixture_results.json')
    report=run()
    target.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(f"{report['count']} symbolic design and arithmetic fixtures passed. No engine validation performed.")
