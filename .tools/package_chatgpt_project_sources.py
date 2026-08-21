#!/usr/bin/env python3
"""Build the flat Chaos Redux source bundle used for ChatGPT projects."""

from __future__ import annotations

import argparse
import filecmp
import os
import shutil
import sys
import tempfile
import uuid
import zipfile
from pathlib import Path


PACKAGE_NAME = "chaos-redux-chatgpt-project-sources"

STATIC_FILES = {
	"AGENTS.md": Path("AGENTS.md"),
	"CHAOS_REDUX_MECHANICS.md": Path("CHAOS_REDUX_MECHANICS.md"),
	"README.md": Path("README.md"),
	"chaos_redux_clusters_catalog.csv": Path("docs/spreadsheets/chaos_redux_clusters_catalog.csv"),
	"chaos_redux_events_catalog.csv": Path("docs/spreadsheets/chaos_redux_events_catalog.csv"),
	"chaos_redux_scenarios_catalog.csv": Path("docs/spreadsheets/chaos_redux_scenarios_catalog.csv"),
	"chaosx_dynamic_effects.md": Path("common/scripted_effects/chaosx_dynamic_effects.md"),
	"chaosx_dynamic_triggers.md": Path("common/scripted_triggers/chaosx_dynamic_triggers.md"),
	"config.toml": Path(".codex/config.toml"),
}


def repository_root() -> Path:
	return Path(__file__).resolve().parent.parent


def default_output() -> Path:
	return Path.home() / "Downloads" / PACKAGE_NAME


def collect_sources(root: Path) -> dict[str, Path]:
	"""Return destination names mapped to their authoritative source files."""
	files = {name: root / relative for name, relative in STATIC_FILES.items()}

	skills_dir = root / ".agents" / "skills"
	for skill_dir in sorted(skills_dir.glob("chaos-redux-*")):
		source = skill_dir / "SKILL.md"
		if source.is_file():
			files[f"{skill_dir.name}.md"] = source

	missing = [str(source) for source in files.values() if not source.is_file()]
	if missing:
		raise FileNotFoundError("Required package sources are missing:\n  " + "\n  ".join(missing))

	return dict(sorted(files.items()))


def collect_subagents(root: Path) -> list[Path]:
	sources = sorted((root / ".codex" / "agents").glob("*.toml"))
	if not sources:
		raise FileNotFoundError("No Codex subagent TOML files were found in .codex/agents")
	return sources


def write_subagents_archive(destination: Path, sources: list[Path]) -> None:
	with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
		for source in sources:
			archive.write(source, arcname=source.name)

	with zipfile.ZipFile(destination, "r") as archive:
		expected_names = [source.name for source in sources]
		if archive.namelist() != expected_names:
			raise OSError("Subagent archive entry verification failed")
		for source in sources:
			if archive.read(source.name) != source.read_bytes():
				raise OSError(f"Subagent archive content verification failed: {source}")


def validate_output(output: Path, root: Path, expected_names: set[str]) -> None:
	resolved = output.resolve()
	resolved_root = root.resolve()
	protected = {Path.home().resolve(), resolved_root, resolved_root.parent, Path(resolved.anchor)}
	if resolved in protected:
		raise ValueError(f"Refusing to replace protected directory: {resolved}")
	if resolved_root in resolved.parents:
		raise ValueError(f"The package output must be outside the repository: {resolved}")
	if output.exists() and not output.is_dir():
		raise ValueError(f"Output path exists and is not a directory: {output}")
	if output.is_symlink():
		raise ValueError(f"Refusing to replace a symbolic link: {output}")
	if output.exists() and resolved != default_output().resolve():
		children = list(output.iterdir())
		if any(child.is_dir() for child in children):
			raise ValueError(f"Custom output directory contains subdirectories: {output}")
		unknown = sorted(child.name for child in children if child.name not in expected_names)
		if unknown:
			raise ValueError(
				"Custom output directory contains files not managed by this packager:\n  "
				+ "\n  ".join(unknown)
			)


def install_staging_directory(staging: Path, output: Path) -> None:
	"""Replace output only after every source has been copied successfully."""
	backup: Path | None = None
	try:
		if output.exists():
			backup = output.with_name(f".{output.name}.backup-{uuid.uuid4().hex}")
			output.rename(backup)
		staging.rename(output)
	except Exception:
		if backup is not None and backup.exists() and not output.exists():
			backup.rename(output)
		raise
	else:
		if backup is not None:
			shutil.rmtree(backup)


def build_package(output: Path, root: Path, *, make_zip: bool, dry_run: bool) -> tuple[int, int]:
	files = collect_sources(root)
	subagents = collect_subagents(root)
	source_count = len(files) + len(subagents)
	bundle_file_count = len(files) + 1
	total_bytes = sum(source.stat().st_size for source in [*files.values(), *subagents])

	if dry_run:
		print(
			f"Would package {source_count} source files ({total_bytes:,} bytes) "
			f"as {bundle_file_count} bundle files into:"
		)
		print(f"  {output}")
		for destination, source in files.items():
			print(f"  {destination} <- {source.relative_to(root)}")
		print(f"  subagents.zip <- {len(subagents)} files from .codex/agents")
		return source_count, total_bytes

	validate_output(output, root, {*files, "subagents.zip"})
	output.parent.mkdir(parents=True, exist_ok=True)
	staging = Path(tempfile.mkdtemp(prefix=f".{output.name}.staging-", dir=output.parent))

	try:
		for destination, source in files.items():
			copied = staging / destination
			shutil.copy2(source, copied)
			if not filecmp.cmp(source, copied, shallow=False):
				raise OSError(f"Copied file verification failed: {source}")
		write_subagents_archive(staging / "subagents.zip", subagents)
		install_staging_directory(staging, output)
	except Exception:
		if staging.exists():
			shutil.rmtree(staging)
		raise

	if make_zip:
		archive = Path(shutil.make_archive(str(output), "zip", output.parent, output.name))
		print(f"ZIP archive: {archive}")

	print(
		f"Packaged {source_count} source files ({total_bytes:,} bytes) "
		f"as {bundle_file_count} bundle files into:"
	)
	print(f"  {output}")
	return source_count, total_bytes


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Build the flat Chaos Redux source bundle for a ChatGPT project."
	)
	parser.add_argument(
		"--output",
		type=Path,
		default=default_output(),
		help=f"destination directory (default: {default_output()})",
	)
	parser.add_argument("--zip", action="store_true", help="also create a ZIP archive beside the folder")
	parser.add_argument("--dry-run", action="store_true", help="list package contents without writing files")
	parser.add_argument("--open", action="store_true", dest="open_output", help="open the package folder when done")
	parser.add_argument("--pause", action="store_true", help=argparse.SUPPRESS)
	return parser.parse_args()


def main() -> int:
	args = parse_args()
	try:
		output = args.output.expanduser().resolve()
		build_package(output, repository_root(), make_zip=args.zip, dry_run=args.dry_run)
		if args.open_output and not args.dry_run:
			if sys.platform == "win32":
				os.startfile(output)
			else:
				print(f"Open the package folder: {output}")
	except Exception as error:
		print(f"Packaging failed: {error}", file=sys.stderr)
		return 1
	finally:
		if args.pause:
			try:
				input("\nPress Enter to close...")
			except EOFError:
				pass
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
