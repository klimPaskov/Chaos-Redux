"""Command-line front end for hash-bound 3D model texture batches."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

PIPELINE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PIPELINE_ROOT.parents[1]
if str(PIPELINE_ROOT) not in sys.path:
    sys.path.insert(0, str(PIPELINE_ROOT))

from textures.delivery import (
    TextureDeliveryError,
    convert_batch,
    install_batch,
    prepare_batch,
    resolve_uv_mask,
)


def _emit(value) -> None:
    print(json.dumps(value, indent=2, sort_keys=True, default=str))


def _path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (REPO_ROOT / path)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Plan, encode, validate, and compare-and-swap install HOI4 model texture batches."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="Hash inputs and create a dry-run CAS manifest.")
    prepare.add_argument("--root", default=str(REPO_ROOT), help="Repository root.")
    prepare.add_argument("--request", required=True, help="Repository-relative request JSON.")
    prepare.add_argument("--staging-root", required=True, help="Separate repository-relative staging directory.")
    prepare.add_argument("--manifest", required=True, help="New repository-relative CAS manifest path.")

    convert = subparsers.add_parser("convert", help="Native BC1/BC3 stage conversion; dry-run unless --execute.")
    convert.add_argument("--root", default=str(REPO_ROOT), help="Repository root.")
    convert.add_argument("--manifest", required=True, help="Prepared CAS manifest.")
    convert.add_argument("--execute", action="store_true", help="Write only to the manifest's staging root.")

    install = subparsers.add_parser("install", help="CAS install; dry-run unless --execute.")
    install.add_argument("--root", default=str(REPO_ROOT), help="Repository root.")
    install.add_argument("--manifest", required=True, help="Staged CAS manifest.")
    install.add_argument("--execute", action="store_true", help="Apply staged DDS files after CAS checks.")

    mask = subparsers.add_parser("resolve-mask", help="Verify one entry in the runtime UV-mask manifest.")
    mask.add_argument("--root", default=str(REPO_ROOT), help="Repository root.")
    mask.add_argument("--manifest", required=True, help="Runtime UV-mask manifest JSON.")
    mask.add_argument("--pdxmesh", required=True, help="Exact PDX mesh identifier.")
    mask.add_argument("--texture", required=True, help="Exact texture slot filename.")
    mask.add_argument("--mesh-sha256")
    mask.add_argument("--registration-sha256")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        root = _path(args.root).resolve(strict=True)
        if args.command == "prepare":
            result = prepare_batch(root, _path(args.request), _path(args.staging_root), _path(args.manifest))
        elif args.command == "convert":
            result = convert_batch(root, _path(args.manifest), execute=args.execute)
        elif args.command == "install":
            result = install_batch(root, _path(args.manifest), execute=args.execute)
        else:
            result = resolve_uv_mask(
                root,
                _path(args.manifest),
                args.pdxmesh,
                args.texture,
                expected_mesh_sha256=args.mesh_sha256,
                expected_registration_sha256=args.registration_sha256,
            )
    except (TextureDeliveryError, OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    _emit(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
