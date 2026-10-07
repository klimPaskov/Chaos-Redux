"""Event 088 design model. This is NOT HOI4 code or evidence of game support.

The caller supplies already-verified owner and region sets as an oracle.
This module does not discover maps, call native effects, observe sweeping,
model combat, or promise engine atomicity. Failure injection deliberately
keeps partial writes and blocks a blind retry.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

Pair = tuple[str, int]


class UnsupportedConfiguration(ValueError):
    """The model rejects a configuration before any mine write."""


class IncompleteApplication(RuntimeError):
    """The model retains partial effects and requires an explicit repair."""


@dataclass
class World:
    eligible_owners: set[str]
    valid_regions: set[int]
    fields: dict[Pair, int] = field(default_factory=dict)
    caps: dict[Pair, int] = field(default_factory=dict)
    default_cap: int = 1000
    status: str = 'unfired'
    chaos: int = 0
    history_entries: int = 0
    pair_calls: list[Pair] = field(default_factory=list)
    changed_pairs: set[Pair] = field(default_factory=set)


@dataclass(frozen=True)
class Receipt:
    committed: bool
    new_calls: int
    changed_fields: int
    chaos_delta: int
    note: str


def fire(
    world: World,
    owners: Iterable[str] | None = None,
    regions: Iterable[int] | None = None,
    *,
    coverage_verified: bool = True,
    fail_after: int | None = None,
) -> Receipt:
    """Apply the once-only additive design to a supplied abstract world.

    `fail_after` injects a failure after that many individual field writes.
    It exists only to test partial-state handling. No repair is simulated.
    """
    if world.status in {'committed', 'legacy-consumed'}:
        return Receipt(False, 0, 0, 0, 'already consumed')
    if world.status != 'unfired':
        raise IncompleteApplication(f'Blind reentry prohibited: {world.status}')
    if not coverage_verified:
        raise UnsupportedConfiguration('Effective map coverage is unverified')
    c = set(world.eligible_owners if owners is None else owners)
    r = set(world.valid_regions if regions is None else regions)
    if c != world.eligible_owners or r != world.valid_regions:
        raise UnsupportedConfiguration('Coverage differs from the verified oracle')
    if not c or not r:
        raise UnsupportedConfiguration('Empty owner or region set')
    if any(not isinstance(owner, str) or not owner for owner in c):
        raise UnsupportedConfiguration('Owner identities must be nonempty strings')
    if any(type(region) is not int for region in r):
        raise UnsupportedConfiguration('Region identities must be integers')
    if fail_after is not None and (type(fail_after) is not int or fail_after < 0):
        raise ValueError('fail_after must be a nonnegative integer or None')

    # Validate every pair before writes. These capabilities are supplied to
    # the model, not claimed to exist as in-game observation interfaces.
    planned: list[tuple[Pair, int, int]] = []
    for owner in sorted(c):
        for region in sorted(r):
            pair = (owner, region)
            before = world.fields.get(pair, 0)
            cap = world.caps.get(pair, world.default_cap)
            if type(cap) is not int or cap <= 0:
                raise UnsupportedConfiguration(f'Invalid cap for {pair}')
            if type(before) is not int or before < 0:
                raise UnsupportedConfiguration(f'Invalid count for {pair}')
            if before > cap:
                raise UnsupportedConfiguration(f'Over-cap preservation unproved: {pair}')
            planned.append((pair, before, min(cap, before + 1000)))

    world.status = 'applying'
    calls = 0
    changed = 0
    for pair, before, after in planned:
        if fail_after is not None and calls == fail_after:
            world.status = 'incomplete'
            raise IncompleteApplication(f'Injected failure after {calls} writes')
        world.fields[pair] = after
        world.pair_calls.append(pair)
        calls += 1
        if after > before:
            changed += 1
            world.changed_pairs.add(pair)
    world.status = 'committed'
    world.history_entries += 1
    delta = 20 if changed else 0
    world.chaos += delta
    return Receipt(True, calls, changed, delta, 'complete design-model pass')


def remove_for_test(world: World, pair: Pair, amount: int) -> None:
    """Abstract reduction for retry tests, NOT a simulation of native sweeping."""
    if type(amount) is not int or amount < 0:
        raise ValueError('amount must be a nonnegative integer')
    world.fields[pair] = max(0, world.fields.get(pair, 0) - amount)
