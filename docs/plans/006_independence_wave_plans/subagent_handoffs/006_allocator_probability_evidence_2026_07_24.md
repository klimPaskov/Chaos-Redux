# Event 006 allocator probability evidence

Evidence date: 2026-07-24.

## Scope

This is a read-only probability check of the automatic allocator's outer `random_list` at `common/scripted_effects/006_independence_wave_package_allocator_effects.txt:57`.

It supplements, and does not replace, the exact count, capacity, host-survival, Event 005 collision, frozen-plan, and SCN-008 checks in `.tools/audit_event6_allocator.py`.

## Adapter inspection

The HOI4 probability inspector resolved one complete proportional-categorical pool with 14 region entries.

Every entry weight is the corresponding dynamic `independence_wave_region_XX_total_weight` variable.

The inspection found 14 candidates, 14 declared inputs, zero unresolved expressions, and no unsupported constructs.

The inspected source SHA-256 is `BC6F7FF8598DF33B610442E6ADA24C28D7D82167FE135474DEB18094B3B6CF83`.

The authoritative inspection artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4289f4f87922745387ef8ffbf8929a7a98512261b35d0f45338ec2afa3054ee7/8e16514160d70c6a99ed9332886f56ce8765839cd3d8a9e9a41835940214b84d/probability-inspect-bc6f7ff8598d.json`

## Uniform-pool normalization control

A control scenario assigned weight `1` to all 14 regions.

The evaluator completed with 14 candidates, zero unresolved inputs, zero diagnostics, and a complete normalized pool.

The authoritative analysis artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da93f8dcb04ec5f95d1ccdf540cce542b2ea5a441cbb2b0278aa6295771eff39/5f2e8f231e80361c3969615069e51e7c80f8cfb9af0a4a31cf36a00fee24b2ca/probability-ae48a47051233bd48a2a9850.json`

## Canonical eight-package first-draw scenarios

The canonical content-attestation set is IW-001, IW-004, IW-007, IW-008, IW-009, IW-017, IW-019, and IW-184.

The declared first-draw scenarios assume:

- every otherwise relevant live tag, anchor, host, and reservation proof passes;
- no sponsorship bonus;
- no prior-wave penalty;
- every region and host is novel at the first draw;
- registered carriers receive the centralized registered-tag bonus;
- unregistered X-tag carriers do not receive that bonus.

These are bounded first-draw probability scenarios, not claims about later draws after novelty and prior-wave memory are recomputed.

| Chaos band | Exact target | Eligible attested package weights by region | Outer-region probability |
| --- | ---: | --- | --- |
| Calm | 3 | Region 01 Northern/Western Europe `525`; Region 02 Mediterranean/Iberia `175` | Region 01 `75%`; Region 02 `25%` |
| Gathering | 4 | Region 01 `700`; Region 02 `325`; Region 14 Americas/Caribbean `150` | Region 01 `59.574%`; Region 02 `27.660%`; Region 14 `12.766%` |
| Rising | 5 | Region 01 `850`; Region 02 `325`; Region 14 `150` | Region 01 `64.151%`; Region 02 `24.528%`; Region 14 `11.321%` |
| Totalen | 7 | Region 01 `850`; Region 02 `325`; Region 14 `150` | Region 01 `64.151%`; Region 02 `24.528%`; Region 14 `11.321%` |
| World Collapse | 10 | Region 01 `850`; Region 02 `325`; Region 14 `150` | Region 01 `64.151%`; Region 02 `24.528%`; Region 14 `11.321%` |

World Collapse does not add a country-count candidate.

None of the eight attested packages has the Totalen-only earliest-band rarity multiplier, so the outer first-draw weights remain equal to the Totalen case.

World Collapse strength, instability, rarity, and ambition are handled by their separate centralized package and execution factors.

The five-scenario evaluator completed with zero unresolved inputs.

The authoritative analysis artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b14fdd29fbb20375da268089db7cb24668c51a1f4669665c94bd4fc287bc019/604da423a015e514fd04e0eb59e6cf361a7421815bb03bba7d92f1d6f3df7ccb/probability-ffc053bd331fd0a83cce1415.json`

## Diagnostic interpretation

The evaluator reports zero-weight region entries as `PROBABILITY_STARVED_OUTCOME` because the outer `random_list` has no separate entry-level trigger.

That is expected in this design.

The inner package preparation effects set unavailable or empty regions to weight zero before the outer draw, and Clausewitz proportional selection cannot select a zero-weight entry.

The warnings therefore document the intended fail-closed region state rather than a hidden eligible outcome.

No unresolved dynamic input or negative weight was present in the declared scenarios.

## Count and scenario boundary

`.tools/audit_event6_allocator.py` independently passes:

- the exact automatic target ladder `3 / 4 / 5 / 7 / 10`;
- World Collapse fixed at ten;
- all four SCN-008 intensity mappings;
- all six SCN-008 type mappings;
- all-anchor before optional-territory reservation;
- Event 005 anchors before Event 006 anchors in joint firing;
- lock before synchronized execution.

The probability adapter evaluates weighted choice, not frozen-plan capacity.

The eight-package attestation set can conditionally satisfy targets 3, 4, 5, and 7.

Both ten-country bands remain fail-closed until at least two more independently complete packages are admitted.

## Simplifications and blockers

No fallback or gameplay simplification was introduced.

The five scenarios are declared first-draw calculations and do not substitute for live later-draw, ordinary-wave, joint-cluster, rollback, or SCN-008 execution evidence.
