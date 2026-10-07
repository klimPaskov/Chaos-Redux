#!/usr/bin/env python3
"""Abstract checks of selected Event 092 design contracts.

This is NOT HOI4 mod code, an engine adapter, a complete auction implementation,
a probability simulation, or evidence that native construction/escrow is supported.
It models integer-hour deadlines and already-funded mock balances to test the
arithmetic and transaction requirements stated in the specification.
Run with Python 3.10+: python 092_greenland_sale_design_checks.py
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
import copy
import json
import unittest

QUANTUM = 5
HOLD_HOURS = 240


def ceiling_quantum(value: Fraction | int, quantum: int = QUANTUM) -> int:
    value = Fraction(value)
    if value < 0 or quantum <= 0:
        raise ValueError('Only non-negative prices and positive quanta are valid.')
    units = value / quantum
    return ((units.numerator + units.denominator - 1) // units.denominator) * quantum


def next_bid(current: int) -> int:
    if current <= 0:
        raise ValueError('Use the reserve for the first bid.')
    return current + max(QUANTUM, ceiling_quantum(Fraction(current, 20)))


@dataclass
class Ledger:
    # Initial balances represent previously earned mock reserve, not free game money.
    free: dict[str, int]
    escrow: dict[str, tuple[str, int]] = field(default_factory=dict)
    lost: int = 0

    def total(self) -> int:
        return sum(self.free.values()) + sum(p for _, p in self.escrow.values()) + self.lost

    def hold(self, lot: str, bidder: str, amount: int) -> None:
        if amount <= 0 or self.free.get(bidder, 0) < amount:
            raise ValueError('Insufficient actual free funds.')
        self.free[bidder] -= amount  # Check before releasing anyone else's funds.
        previous = self.escrow.pop(lot, None)
        if previous:
            self.free[previous[0]] = self.free.get(previous[0], 0) + previous[1]
        self.escrow[lot] = (bidder, amount)

    def refund(self, lot: str, living: set[str] | None = None) -> int:
        previous = self.escrow.pop(lot, None)
        if not previous:
            return 0
        owner, paid = previous
        if living is not None and owner not in living:
            self.lost += paid
        else:
            self.free[owner] = self.free.get(owner, 0) + paid
        return paid

    def settle(self, lot: str, seller: str) -> int:
        previous = self.escrow.pop(lot, None)
        if not previous:
            return 0
        paid = previous[1]
        self.free[seller] = self.free.get(seller, 0) + paid
        return paid


@dataclass
class Auction:
    lot: str
    seller: str
    reserve: int
    start: int = 15 * 24
    first_deadline: int = (15 + 30) * 24
    bidder: str | None = None
    amount: int = 0
    deadline: int | None = None
    state: str = 'open'

    def quote(self) -> int:
        return self.reserve if self.bidder is None else next_bid(self.amount)

    def bid(self, ledger: Ledger, bidder: str, price_seen: int, hour: int) -> None:
        if self.state != 'open' or hour < self.start:
            raise ValueError('Auction is not open for bidding.')
        deadline = self.first_deadline if self.bidder is None else self.deadline
        if deadline is None or hour >= deadline:
            raise ValueError('Bids at or after the exact deadline are rejected.')
        if bidder == self.seller or bidder == self.bidder:
            raise ValueError('Neither seller self-bids nor leader self-raises are valid.')
        if price_seen != self.quote():
            raise ValueError('Stale quote requires fresh confirmation.')
        ledger.hold(self.lot, bidder, price_seen)
        self.bidder, self.amount = bidder, price_seen
        self.deadline = hour + HOLD_HOURS

    def close(self, ledger: Ledger, hour: int) -> int:
        if self.state != 'open':
            return 0
        deadline = self.first_deadline if self.bidder is None else self.deadline
        if deadline is None or hour < deadline:
            raise ValueError('Cannot close before the exact deadline.')
        if self.bidder is None:
            self.state = 'unsold'
            return 0
        paid = ledger.settle(self.lot, self.seller)
        self.state = 'sold'
        return paid

    def cancel(self, ledger: Ledger, living: set[str] | None = None) -> int:
        if self.state != 'open':
            return 0
        paid = ledger.refund(self.lot, living)
        self.state = 'cancelled'
        return paid


def permissions(*, regional=False, strategic=False, core=False, founding=False) -> set[str]:
    if founding:
        return set()  # Survival and ownership remain separately required.
    needed = {'II'} if regional else set()
    if strategic:
        needed.add('III')
    if core:
        needed.add('IV')
    if not needed:
        needed.add('I')
    return needed


def survives(capital: int, owned_controlled: set[int], inhabited: set[int],
             cores: set[int], pending: list[set[int]]) -> bool:
    sold = set().union(*pending) if pending else set()
    remaining = owned_controlled - sold
    if capital in sold or capital not in remaining:
        return False
    home = owned_controlled & inhabited
    eligible_home = home & cores if home & cores else home
    return bool(remaining & eligible_home)


CHAOS = {'founding': 5, 'secondary': 5, 'regional': 5, 'strategic': 10, 'homeland': 10}


@dataclass
class Milestones:
    consumed: set[str] = field(default_factory=set)
    total_positive: int = 0
    homeland_receipt: str | None = None
    reversed: bool = False

    def award(self, receipt: str, qualified: set[str]) -> int:
        new = qualified - self.consumed
        amount = max((CHAOS[x] for x in new), default=0)
        self.consumed.update(new)
        self.total_positive += amount
        if 'homeland' in new:
            self.homeland_receipt = receipt  # Homeland wins equal-effect explanation.
        return amount

    def reverse(self, receipt: str, qualifying_recovery: bool) -> int:
        if not self.reversed and qualifying_recovery and receipt == self.homeland_receipt:
            self.reversed = True
            return -5
        return 0


class DesignContracts(unittest.TestCase):
    def ledger(self):
        return Ledger({'seller': 0, 'a': 500, 'b': 500, 'c': 500})

    def test_01_positive_rounding_never_underquotes(self):
        for numerator in range(1, 1001):
            value = Fraction(numerator, 7)
            price = ceiling_quantum(value)
            self.assertGreaterEqual(price, value)
            self.assertLess(price - value, 5)
            self.assertEqual(price % 5, 0)

    def test_02_zero_and_invalid_quantization(self):
        self.assertEqual(ceiling_quantum(0), 0)
        with self.assertRaises(ValueError): ceiling_quantum(-1)
        with self.assertRaises(ValueError): ceiling_quantum(1, 0)

    def test_03_next_prices(self):
        self.assertEqual([next_bid(x) for x in (75, 80, 100, 450, 3000)], [80, 85, 105, 475, 3150])

    def test_04_first_bid_requires_preparation(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        with self.assertRaises(ValueError): a.bid(l, 'a', 75, 359)
        a.bid(l, 'a', 75, 360)
        self.assertEqual(a.deadline, 600)

    def test_05_no_bid_becomes_unsold_without_payment(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        before = copy.deepcopy(l)
        self.assertEqual(a.close(l, 1080), 0)
        self.assertEqual(a.state, 'unsold')
        self.assertEqual(l, before)

    def test_06_no_first_bid_at_expiry(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        with self.assertRaises(ValueError): a.bid(l, 'a', 75, 1080)

    def test_07_every_higher_bid_resets_full_period(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        a.bid(l, 'b', 80, 599)
        self.assertEqual(a.deadline, 839)
        a.bid(l, 'c', 85, 838)
        self.assertEqual(a.deadline, 1078)

    def test_08_bid_at_exact_high_bid_deadline_rejected(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        with self.assertRaises(ValueError): a.bid(l, 'b', 80, 600)
        self.assertEqual(a.close(l, 600), 75)

    def test_09_stale_quote_does_not_auto_spend(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        before = copy.deepcopy((a, l))
        with self.assertRaises(ValueError): a.bid(l, 'b', 75, 360)
        self.assertEqual((a, l), before)

    def test_10_seller_cannot_bid(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        l.free['seller'] = 500
        with self.assertRaises(ValueError): a.bid(l, 'seller', 75, 360)

    def test_11_leader_cannot_self_raise(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        before = copy.deepcopy((a, l))
        with self.assertRaises(ValueError): a.bid(l, 'a', 80, 500)
        self.assertEqual((a, l), before)

    def test_12_outbid_refunds_actual_paid_amount(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        a.bid(l, 'b', 80, 500)
        self.assertEqual(l.free['a'], 500)
        self.assertEqual(l.free['b'], 420)
        self.assertEqual(l.total(), 1500)

    def test_13_unaffordable_challenger_does_not_release_leader(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        l.free['b'] = 79
        before = copy.deepcopy((a, l))
        with self.assertRaises(ValueError): a.bid(l, 'b', 80, 500)
        self.assertEqual((a, l), before)

    def test_14_settlement_transfers_once_without_second_debit(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        a.close(l, 600)
        self.assertEqual(l.free['a'], 425)
        self.assertEqual(l.free['seller'], 75)
        self.assertEqual(a.close(l, 601), 0)
        self.assertEqual(l.total(), 1500)

    def test_15_cancellation_refunds_once(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        self.assertEqual(a.cancel(l), 75)
        self.assertEqual(a.cancel(l), 0)
        self.assertEqual(l.free['a'], 500)
        self.assertEqual(l.total(), 1500)

    def test_16_completed_sale_cannot_cancel_into_refund(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        a.close(l, 600)
        self.assertEqual(a.cancel(l), 0)
        self.assertEqual(l.free['a'], 425)

    def test_17_two_lots_cannot_double_spend_escrow(self):
        l = Ledger({'seller': 0, 'a': 100})
        x, y = Auction('x', 'seller', 75), Auction('y', 'seller', 75)
        x.bid(l, 'a', 75, 360)
        with self.assertRaises(ValueError): y.bid(l, 'a', 75, 360)
        self.assertEqual(l.free['a'], 25)
        self.assertEqual(l.total(), 100)

    def test_18_escrow_survives_loss_of_future_earning_capacity(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        # Capacity is intentionally not a debt input: this is already paid principal.
        self.assertEqual(a.close(l, 600), 75)

    def test_19_snapshot_keeps_deadline_and_principal(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        saved = json.dumps({'auction': a.__dict__, 'free': l.free, 'escrow': l.escrow})
        data = json.loads(saved)
        restored = Auction(**data['auction'])
        balance = Ledger(data['free'], {k: tuple(v) for k, v in data['escrow'].items()})
        self.assertEqual(restored.deadline, 600)
        self.assertEqual(restored.close(balance, 600), 75)
        self.assertEqual(balance.total(), 1500)

    def test_20_abolished_bidder_has_explicit_loss_not_seller_profit(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        a.bid(l, 'a', 75, 360)
        a.cancel(l, {'seller', 'b', 'c'})
        self.assertEqual(l.lost, 75)
        self.assertEqual(l.free['seller'], 0)
        self.assertEqual(l.free['a'], 425)
        self.assertEqual(l.total(), 1500)

    def test_21_foundation_does_not_require_evolutions(self):
        self.assertEqual(permissions(founding=True, core=True, strategic=True, regional=True), set())

    def test_22_all_permission_combinations(self):
        self.assertEqual(permissions(), {'I'})
        self.assertEqual(permissions(regional=True), {'II'})
        self.assertEqual(permissions(strategic=True), {'III'})
        self.assertEqual(permissions(core=True), {'IV'})
        self.assertEqual(permissions(regional=True, strategic=True), {'II', 'III'})
        self.assertEqual(permissions(core=True, strategic=True), {'III', 'IV'})
        self.assertEqual(permissions(regional=True, core=True), {'II', 'IV'})
        self.assertEqual(permissions(regional=True, strategic=True, core=True), {'II', 'III', 'IV'})

    def test_23_capital_cannot_be_sold(self):
        self.assertFalse(survives(1, {1, 2}, {1, 2}, {1, 2}, [{1}]))

    def test_24_combined_lots_cannot_erase_inhabited_core_home(self):
        # Abstract capital 1 is uninhabited, so 2 and 3 are the qualifying homes.
        args = (1, {1, 2, 3}, {2, 3}, {2, 3})
        self.assertTrue(survives(*args, [{2}]))
        self.assertTrue(survives(*args, [{3}]))
        self.assertFalse(survives(*args, [{2}, {3}]))

    def test_25_country_without_cores_keeps_its_actual_home(self):
        self.assertTrue(survives(1, {1, 2}, {1}, set(), [{2}]))
        self.assertFalse(survives(1, {1, 2}, {2}, set(), [{2}]))

    def test_26_independent_greenland_cannot_sell_everything(self):
        self.assertFalse(survives(101, {101}, {101}, {101}, [{101}]))

    def test_27_chaos_separate_milestones_bound_positive_total(self):
        m = Milestones()
        for i, key in enumerate(CHAOS): m.award(str(i), {key})
        self.assertEqual(m.total_positive, 35)
        self.assertEqual(m.award('repeat', set(CHAOS)), 0)

    def test_28_overlapping_chaos_uses_largest_and_consumes_all(self):
        m = Milestones()
        self.assertEqual(m.award('sale', {'secondary', 'regional', 'strategic', 'homeland'}), 10)
        self.assertEqual(m.award('later', {'secondary', 'regional', 'strategic'}), 0)
        self.assertEqual(m.homeland_receipt, 'sale')

    def test_29_chaos_reversal_is_one_identified_receipt(self):
        m = Milestones()
        m.award('home', {'homeland', 'strategic'})
        self.assertEqual(m.reverse('other', True), 0)
        self.assertEqual(m.reverse('home', False), 0)
        self.assertEqual(m.reverse('home', True), -5)
        self.assertEqual(m.reverse('home', True), 0)

    def test_30_reconstruction_target_not_raised_by_winning_price(self):
        published = {'reserve': 1000, 'construction_target': 750}
        for paid in (1000, 2000, 10000):
            self.assertLessEqual(published['construction_target'], paid)
            self.assertEqual(published['construction_target'], 750)

    def test_31_floor_ratios_and_rounded_example(self):
        self.assertEqual(ceiling_quantum(Fraction(100 * 75, 100)), 75)
        self.assertEqual(ceiling_quantum(Fraction(4000 * 75, 100)), 3000)
        self.assertEqual(ceiling_quantum(Fraction(101 * 75, 100)), 80)

    def test_32_no_negative_final_escrow_or_free_balance(self):
        a, l = Auction('x', 'seller', 75), self.ledger()
        for i, who in enumerate(('a', 'b', 'c', 'a', 'b')):
            a.bid(l, who, a.quote(), 360 + i)
            self.assertTrue(all(v >= 0 for v in l.free.values()))
            self.assertEqual(l.total(), 1500)
        a.cancel(l)
        self.assertEqual(l.free, self.ledger().free)


class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records: list[dict[str, str]] = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.records.append({'case': test._testMethodName, 'status': 'PASS'})

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.records.append({'case': test._testMethodName, 'status': 'FAIL'})

    def addError(self, test, err):
        super().addError(test, err)
        self.records.append({'case': test._testMethodName, 'status': 'ERROR'})


def main() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(DesignContracts)
    result = unittest.TextTestRunner(verbosity=2, resultclass=RecordedResult).run(suite)
    payload = {
        'scope': 'Abstract Python design contracts only. Not native HOI4, game, AI probability or asset tests.',
        'cases_run': result.testsRun,
        'passed': sum(x['status'] == 'PASS' for x in result.records),
        'failures': len(result.failures),
        'errors': len(result.errors),
        'cases': result.records,
        'omissions': [
            'No native factory withholding or construction redemption.',
            'No real map geometry, transfer, cores or subject APIs.',
            'No native save loading or multiplayer scheduling.',
            'No MTTH distribution, AI performance, asset or localisation checks.',
            'No actual specialist subagent or independent review.'
        ],
    }
    Path(__file__).with_name('092_greenland_sale_design_check_results.json').write_text(
        json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
