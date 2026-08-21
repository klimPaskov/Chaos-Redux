#!/usr/bin/env python3
"""Estimate Meshy API credits for a planned Chaos Redux 3D job.

This is a planning utility. The live Meshy pricing page and task response are
always authoritative. Snapshot date: 2026-07-22.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from typing import Final

SNAPSHOT_DATE: Final[str] = "2026-07-22"

MODEL_COSTS: Final[dict[str, tuple[int, int]]] = {
    "smart_topology": (5, 15),
    "other": (5, 15),
    "meshy7": (20, 30),
    "lowpoly_t1": (20, 30),
}

OPERATION_COSTS: Final[dict[str, int]] = {
    "remesh": 5,
    "retexture": 10,
    "convert": 1,
    "resize": 1,
    "rig": 5,
    "animation": 3,
}


@dataclass(frozen=True)
class Estimate:
    snapshot_date: str
    model: str
    textured: bool
    generation_attempts: int
    generation_cost: int
    remesh_count: int
    retexture_count: int
    convert_count: int
    resize_count: int
    rig_count: int
    animation_count: int
    uv_unwrap_count: int
    uv_unwrap_unit_cost: int | None
    uv_unwrap_cost: int
    subtotal: int
    retry_reserve: int
    total_with_reserve: int
    warning: str


def non_negative_int(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("value must be zero or greater")
    return parsed


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("value must be one or greater")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", choices=sorted(MODEL_COSTS), default="smart_topology")
    parser.add_argument("--textured", action="store_true")
    parser.add_argument("--generation-attempts", type=positive_int, default=1)
    parser.add_argument("--remesh", type=non_negative_int, default=0, dest="remesh_count")
    parser.add_argument("--retexture", type=non_negative_int, default=0, dest="retexture_count")
    parser.add_argument("--convert", type=non_negative_int, default=0, dest="convert_count")
    parser.add_argument("--resize", type=non_negative_int, default=0, dest="resize_count")
    parser.add_argument("--rig", action="store_true")
    parser.add_argument("--rig-count", type=non_negative_int, default=None)
    parser.add_argument("--animations", type=non_negative_int, default=0, dest="animation_count")
    parser.add_argument("--uv-unwrap", type=non_negative_int, default=0, dest="uv_unwrap_count")
    parser.add_argument(
        "--uv-unwrap-unit-cost",
        type=non_negative_int,
        default=None,
        help=(
            "Explicit live per-call UV unwrap cost. The reviewed pricing table did not "
            "publish a UV unwrap row, so this is required when --uv-unwrap is nonzero."
        ),
    )
    parser.add_argument(
        "--retry-reserve-percent",
        type=non_negative_int,
        default=0,
        help="Add a planning reserve as a percentage of the subtotal.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of a text summary.")
    return parser


def calculate(args: argparse.Namespace, parser: argparse.ArgumentParser) -> Estimate:
    if args.uv_unwrap_count > 0 and args.uv_unwrap_unit_cost is None:
        parser.error(
            "--uv-unwrap-unit-cost is required when --uv-unwrap is nonzero. "
            "Read the live pricing or consumed_credits instead of assuming a cost."
        )

    no_texture, with_texture = MODEL_COSTS[args.model]
    generation_unit = with_texture if args.textured else no_texture
    generation_cost = generation_unit * args.generation_attempts
    rig_count = args.rig_count if args.rig_count is not None else int(args.rig)
    uv_unwrap_cost = args.uv_unwrap_count * (args.uv_unwrap_unit_cost or 0)

    subtotal = (
        generation_cost
        + args.remesh_count * OPERATION_COSTS["remesh"]
        + args.retexture_count * OPERATION_COSTS["retexture"]
        + args.convert_count * OPERATION_COSTS["convert"]
        + args.resize_count * OPERATION_COSTS["resize"]
        + rig_count * OPERATION_COSTS["rig"]
        + args.animation_count * OPERATION_COSTS["animation"]
        + uv_unwrap_cost
    )
    retry_reserve = (subtotal * args.retry_reserve_percent + 99) // 100

    return Estimate(
        snapshot_date=SNAPSHOT_DATE,
        model=args.model,
        textured=args.textured,
        generation_attempts=args.generation_attempts,
        generation_cost=generation_cost,
        remesh_count=args.remesh_count,
        retexture_count=args.retexture_count,
        convert_count=args.convert_count,
        resize_count=args.resize_count,
        rig_count=rig_count,
        animation_count=args.animation_count,
        uv_unwrap_count=args.uv_unwrap_count,
        uv_unwrap_unit_cost=args.uv_unwrap_unit_cost,
        uv_unwrap_cost=uv_unwrap_cost,
        subtotal=subtotal,
        retry_reserve=retry_reserve,
        total_with_reserve=subtotal + retry_reserve,
        warning=(
            "Planning estimate only. Recheck live Meshy API pricing and record actual "
            "consumed_credits. UV unwrap is not estimated without an explicit live unit cost."
        ),
    )


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    estimate = calculate(args, parser)

    if args.json:
        print(json.dumps(asdict(estimate), indent=2))
        return 0

    print(f"Meshy API credit estimate, pricing snapshot {estimate.snapshot_date}")
    print(f"Generation: {estimate.generation_cost} credits")
    print(f"Remesh: {estimate.remesh_count * OPERATION_COSTS['remesh']} credits")
    print(f"Retexture: {estimate.retexture_count * OPERATION_COSTS['retexture']} credits")
    print(f"Convert: {estimate.convert_count * OPERATION_COSTS['convert']} credits")
    print(f"Resize: {estimate.resize_count * OPERATION_COSTS['resize']} credits")
    print(f"Rig: {estimate.rig_count * OPERATION_COSTS['rig']} credits")
    print(f"Animations: {estimate.animation_count * OPERATION_COSTS['animation']} credits")
    print(f"UV unwrap: {estimate.uv_unwrap_cost} credits")
    print(f"Subtotal: {estimate.subtotal} credits")
    print(f"Retry reserve: {estimate.retry_reserve} credits")
    print(f"Total with reserve: {estimate.total_with_reserve} credits")
    print(estimate.warning)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
