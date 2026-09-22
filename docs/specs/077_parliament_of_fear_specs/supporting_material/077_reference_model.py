"""Pure planning invariants. This module does not execute or validate HOI4."""
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Iterable


def apportion(weights: Iterable[int]) -> list[int]:
    """Allocate exactly 100 influence seats with stable largest remainders."""
    values = list(weights)
    if not values or any(type(x) is not int or x < 0 for x in values):
        raise ValueError("Provide a nonempty list of nonnegative integer weights")
    if sum(values) == 0:
        values = [1] * len(values)
    total = sum(values)
    exact = [Fraction(100 * x, total) for x in values]
    seats = [x.numerator // x.denominator for x in exact]
    priority = sorted(range(len(values)), key=lambda i: (-(exact[i] - seats[i]), i))
    for i in priority[:100 - sum(seats)]:
        seats[i] += 1
    assert sum(seats) == 100
    return seats


@dataclass
class Seat:
    filled: bool = True
    suspended: bool = False
    support: str = "uncertain"
    evidence: str = "none"

    def counts(self) -> bool:
        return self.filled and not self.suspended

    def supports(self) -> bool:
        return self.counts() and self.support in {"loyal", "dependable"}


@dataclass(frozen=True)
class CaseIdentity:
    case_id: str
    original_truth: str
    source_id: str


@dataclass
class Crisis:
    instance: int
    seats: list[Seat]
    paranoia: int = 25
    active: bool = True
    prepared_plot: bool = False
    essential_case: bool = False
    purge_pending: bool = False
    safe_days: int = 0
    release_count: int = 0
    political_power: int = 100
    commits: set[str] = field(default_factory=set)
    cases: dict[str, CaseIdentity] = field(default_factory=dict)
    findings: dict[str, str] = field(default_factory=dict)
    persistent_history: dict[str, object] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if len(self.seats) != 100 or not 0 <= self.paranoia <= 100:
            raise ValueError("A crisis needs exactly 100 seats and Paranoia from 0 to 100")

    @property
    def support(self) -> int:
        return sum(s.supports() for s in self.seats)

    @property
    def filled(self) -> int:
        return sum(s.counts() for s in self.seats)

    def has_majority(self) -> bool:
        return self.support >= 51

    def purge(self, indices: Iterable[int]) -> None:
        indexes = list(indices)
        if any(type(i) is not int or i < 0 or i >= 100 for i in indexes):
            raise ValueError("Invalid influence seat index")
        for i in set(indexes):
            self.seats[i].filled = False
            self.seats[i].suspended = False

    def accuse(self, index: int) -> None:
        self.seats[index].evidence = "accused"

    def appoint(self, index: int, support: str) -> None:
        if support not in {"loyal", "dependable", "uncertain", "opposed"}:
            raise ValueError("Unknown support state")
        if self.seats[index].filled:
            raise ValueError("Appointment cannot displace an occupied seat")
        self.seats[index] = Seat(support=support)

    def callback_valid(self, instance: int) -> bool:
        return self.active and self.instance == instance

    def debit_once(self, action_id: str, cost: int) -> bool:
        if type(cost) is not int or cost < 0:
            raise ValueError("Invalid cost")
        if action_id in self.commits or self.political_power < cost:
            return False
        self.political_power -= cost
        self.commits.add(action_id)
        return True

    def safe_today(self) -> bool:
        return (self.active and self.paranoia <= 20 and self.support >= 55
                and self.filled >= 80 and not self.prepared_plot
                and not self.essential_case and not self.purge_pending)

    def advance_day(self) -> bool:
        self.safe_days = self.safe_days + 1 if self.safe_today() else 0
        if self.safe_days >= 21:
            self.close()
            return True
        return False

    def close(self) -> None:
        if self.active:
            self.active = False
            self.release_count += 1
            self.persistent_history["closed_instance"] = self.instance


@dataclass
class ChaosLedger:
    added: int = 0
    reversed: int = 0
    transactions: set[str] = field(default_factory=set)
    reversals: set[str] = field(default_factory=set)

    def add(self, transaction: str, amount: int) -> int:
        if type(amount) is not int or amount < 0:
            raise ValueError("Expected a nonnegative contribution")
        if transaction in self.transactions:
            return 0
        self.transactions.add(transaction)
        self.added += amount
        return amount

    def reverse(self, milestone: str, amount: int) -> int:
        if type(amount) is not int or amount < 0:
            raise ValueError("Expected a nonnegative reversal request")
        if milestone in self.reversals:
            return 0
        actual = min(amount, self.added - self.reversed)
        self.reversals.add(milestone)
        self.reversed += actual
        return actual
