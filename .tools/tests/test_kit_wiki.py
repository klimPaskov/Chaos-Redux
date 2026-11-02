"""Regression tests for `.tools/sync/kit_wiki.py`, the check that keeps `hoi4_wiki/` equal to a kit commit.

Every test builds a small repository in a temporary folder, so nothing tracked is written. The last class
checks the real repository. Run from the mod root: `python -B .tools/tests/test_kit_wiki.py`.
"""

import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS / "sync"))

import kit_wiki

PAGE = "# Effect\n\nWiki text.\n"
IMAGE = b"\x89PNG\r\n\x1a\nbinary\r\n"
ENVIRONMENT = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@example.test",
	GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@example.test")


def write(path, data):
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_bytes(data.encode("utf-8") if isinstance(data, str) else data)


def git(repository, *command):
	return subprocess.run(["git", "-C", str(repository), *command], check=True, capture_output=True, text=True, env=ENVIRONMENT).stdout


class KitWikiCase(unittest.TestCase):
	def setUp(self):
		self.temporary = tempfile.TemporaryDirectory()
		self.addCleanup(self.temporary.cleanup)
		self.root = Path(self.temporary.name) / "mod"
		self.kit = Path(self.temporary.name) / "kit"
		write(self.kit / "hoi4_wiki/effect.md", PAGE)
		write(self.kit / "hoi4_wiki/media/effect_img1.png", IMAGE)
		write(self.kit / "hoi4_wiki/LICENSE.txt", "CC BY-SA 3.0\n")
		write(self.kit / "README.md", "Not part of the snapshot.\n")
		git(self.kit, "init", "-q")
		git(self.kit, "add", "-A")
		git(self.kit, "-c", "commit.gpgsign=false", "commit", "-q", "-m", "kit")

	def run_tool(self, *arguments):
		output = io.StringIO()
		with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
			status = kit_wiki.main(["--root", str(self.root), *arguments])
		return status, output.getvalue()

	def refresh(self, revision="HEAD"):
		return self.run_tool("--refresh", "--kit", str(self.kit), "--commit", revision)


class Refresh(KitWikiCase):
	def test_refresh_copies_the_commit_and_the_check_then_passes(self):
		# The working tree changes after the commit, and the snapshot must still come from the commit.
		write(self.kit / "hoi4_wiki/effect.md", "uncommitted\n")
		self.assertEqual(self.refresh()[0], 0)
		self.assertEqual((self.root / "hoi4_wiki/effect.md").read_text(encoding="utf-8"), PAGE)
		self.assertEqual((self.root / "hoi4_wiki/media/effect_img1.png").read_bytes(), IMAGE)
		self.assertFalse((self.root / "README.md").exists())
		manifest = json.loads((self.root / kit_wiki.MANIFEST).read_text(encoding="utf-8"))
		self.assertEqual(manifest["kit_commit"], git(self.kit, "rev-parse", "HEAD").strip())
		self.assertEqual(sorted(manifest["files"]), ["hoi4_wiki/LICENSE.txt", "hoi4_wiki/effect.md", "hoi4_wiki/media/effect_img1.png"])
		self.assertEqual(self.run_tool(), (0, "Wiki snapshot matches the kit: 3 files.\n"))

	def test_a_newer_kit_commit_replaces_the_snapshot_and_removes_dropped_pages(self):
		self.refresh()
		write(self.kit / "hoi4_wiki/trigger.md", "# Trigger\n")
		git(self.kit, "rm", "-q", "hoi4_wiki/effect.md")
		git(self.kit, "add", "-A")
		git(self.kit, "-c", "commit.gpgsign=false", "commit", "-q", "-m", "newer")
		self.assertEqual(self.refresh()[0], 0)
		self.assertFalse((self.root / "hoi4_wiki/effect.md").exists())
		self.assertEqual(self.run_tool()[0], 0)

	def test_a_kit_without_a_wiki_cannot_run_and_writes_nothing(self):
		git(self.kit, "rm", "-q", "-r", "hoi4_wiki")
		git(self.kit, "-c", "commit.gpgsign=false", "commit", "-q", "-m", "no wiki")
		status, output = self.refresh()
		self.assertEqual(status, 2)
		self.assertIn("no hoi4_wiki/", output)
		self.assertFalse((self.root / kit_wiki.MANIFEST).exists())


class Drift(KitWikiCase):
	def setUp(self):
		super().setUp()
		self.refresh()

	def test_hand_edit_is_drift(self):
		write(self.root / "hoi4_wiki/effect.md", PAGE + "Local note.\n")
		status, output = self.run_tool("--check")
		self.assertEqual(status, 1)
		self.assertIn("DRIFT hoi4_wiki/effect.md: differs from the kit snapshot", output)

	def test_extra_and_missing_files_are_drift(self):
		write(self.root / "hoi4_wiki/local_page.md", "# Local\n")
		(self.root / "hoi4_wiki/LICENSE.txt").unlink()
		status, output = self.run_tool()
		self.assertEqual(status, 1)
		self.assertIn("DRIFT hoi4_wiki/local_page.md: not in the kit snapshot", output)
		self.assertIn("DRIFT hoi4_wiki/LICENSE.txt: missing", output)

	def test_crlf_checkout_is_not_drift(self):
		write(self.root / "hoi4_wiki/effect.md", PAGE.replace("\n", "\r\n"))
		self.assertEqual(self.run_tool()[0], 0)

	def test_missing_manifest_cannot_run(self):
		(self.root / kit_wiki.MANIFEST).unlink()
		self.assertEqual(self.run_tool()[0], 2)


class RepositoryState(unittest.TestCase):
	def test_wiki_snapshot_matches_the_pinned_kit_commit(self):
		output = io.StringIO()
		with contextlib.redirect_stdout(output):
			status = kit_wiki.main([])
		self.assertEqual(status, 0, output.getvalue())


if __name__ == "__main__":
	unittest.main()
