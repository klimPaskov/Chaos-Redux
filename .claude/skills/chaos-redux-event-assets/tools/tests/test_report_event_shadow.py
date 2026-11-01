"""Golden tests for the report-event card and shadow against vanilla's report-card alpha masks.

Run from the repository root:
    python -B -m unittest discover -s .claude/skills/chaos-redux-event-assets/tools/tests -v
(pytest collects these tests too). The golden tests read the installed game at test time and skip when it is absent;
no vanilla pixels are stored in the repository.

Vanilla paints every 210x176 report card into one of four fixed alpha masks (measured on 1.19: 230, 180, 117 and 5 of
532 files). The card is about 192x154 at about 4.2 degrees counter-clockwise with a tight near-black shadow on all four
sides. The processed card's alpha channel is compared with those masks.
"""

from __future__ import annotations

import collections
import hashlib
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
from PIL import Image

TOOLS = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[5]
MAIN_RMSE_LIMIT = 12.0
MAIN_TEMPLATES = 2  # the two most common masks (230 and 180 files) must meet the limit; the rarer two are printed
EDGE_ALPHA_LIMIT = 40
SIZE = (210, 176)
_TEMPLATE_CACHE: Dict[str, List[Tuple[int, np.ndarray]]] = {}


def load_processor() -> Any:
    spec = importlib.util.spec_from_file_location("process_report_event_image", TOOLS / "process_report_event_image.py")
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def find_game_dir() -> Optional[Path]:
    sys.path.insert(0, str(REPO_ROOT / ".tools"))
    try:
        from lib.game import game_dir  # type: ignore

        folder = Path(game_dir())
    except Exception:
        return None
    finally:
        sys.path.pop(0)
    return folder if (folder / "gfx" / "event_pictures").is_dir() else None


def vanilla_templates(game: Path) -> List[Tuple[int, np.ndarray]]:
    """Return (file count, alpha) for the four most common distinct 210x176 report-card alpha masks."""
    key_name = str(game)
    if key_name in _TEMPLATE_CACHE:
        return _TEMPLATE_CACHE[key_name]
    files: Dict[str, List[Path]] = collections.defaultdict(list)
    alphas: Dict[str, np.ndarray] = {}
    for path in sorted((game / "gfx" / "event_pictures").glob("report_event*.dds")):
        try:
            with Image.open(path) as image:
                alpha = np.asarray(image.convert("RGBA"))[..., 3]
        except Exception:
            continue  # a few vanilla files use a DX10 format Pillow cannot decode
        if alpha.shape != (SIZE[1], SIZE[0]):
            continue
        key = hashlib.sha1(alpha.tobytes()).hexdigest()
        files[key].append(path)
        alphas.setdefault(key, alpha.astype(float))
    top = sorted(files, key=lambda key: -len(files[key]))[:4]
    _TEMPLATE_CACHE[key_name] = [(len(files[key]), alphas[key]) for key in top]
    return _TEMPLATE_CACHE[key_name]


def synthetic_photo(path: Path) -> Path:
    rng = np.random.default_rng(7)
    y, x = np.mgrid[0:300, 0:400]
    pixels = np.stack([x * 255 / 400, y * 255 / 300, (x + y) * 255 / 700], -1) + rng.normal(0, 12, (300, 400, 3))
    Image.fromarray(np.clip(pixels, 0, 255).astype("uint8")).save(path)
    return path


def rmse(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(((a - b) ** 2).mean()))


class ReportShadowTests(unittest.TestCase):
    processor: Any
    folder: tempfile.TemporaryDirectory
    photo: Path
    game: Optional[Path]

    @classmethod
    def setUpClass(cls) -> None:
        cls.processor = load_processor()
        cls.folder = tempfile.TemporaryDirectory()
        cls.photo = synthetic_photo(Path(cls.folder.name) / "photo.png")
        cls.game = find_game_dir()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.folder.cleanup()

    def process(self, name: str, **overrides: Any) -> np.ndarray:
        """Process the synthetic photo with the CLI defaults (plus overrides); return the RGBA array."""
        output = Path(self.folder.name) / name
        args = self.processor.build_parser().parse_args([str(self.photo), str(output)])
        values: Dict[str, Any] = dict(
            canvas_size=args.canvas_size, card_size=args.card_size, border=args.border, angle=args.angle,
            shadow_offset=tuple(args.shadow_offset), shadow_blur=args.shadow_blur, shadow_opacity=args.shadow_opacity,
            grain=args.grain, paper_grain=args.paper_grain, seed=args.seed,
            rotate_supersample=args.rotate_supersample, edge_soften=args.edge_soften,
        )
        values.update(overrides)
        self.processor.process_report_event_image(input_path=self.photo, output_path=output, **values)
        with Image.open(output) as image:
            return np.asarray(image.convert("RGBA"))

    def templates(self) -> List[Tuple[int, np.ndarray]]:
        if self.game is None:
            self.skipTest("Hearts of Iron IV is not installed here (set HOI4_GAME_DIR); the vanilla golden test needs it")
        found = vanilla_templates(self.game)
        if len(found) < MAIN_TEMPLATES:
            self.skipTest(f"only {len(found)} distinct vanilla report alpha masks found in {self.game}")
        return found

    def test_alpha_matches_vanilla_masks(self) -> None:
        alpha = self.process("golden.png")[..., 3].astype(float)
        scores = [(count, rmse(alpha, template)) for count, template in self.templates()]
        print("alpha RMSE per vanilla mask (files, rmse):", [(n, round(s, 2)) for n, s in scores])
        for count, score in scores[:MAIN_TEMPLATES]:
            self.assertLessEqual(score, MAIN_RMSE_LIMIT, f"alpha RMSE {score:.2f} vs the {count}-file vanilla mask")

    def test_old_defaults_would_fail_the_golden_comparison(self) -> None:
        old = self.process(
            "old.png", card_size=(192, 153), angle=4.0, shadow_offset=(4, 5), shadow_blur=4.5, shadow_opacity=0.50,
        )[..., 3].astype(float)
        _, main = self.templates()[0]
        self.assertGreater(rmse(old, main), MAIN_RMSE_LIMIT)

    def test_no_hard_edge_at_canvas_right_and_bottom(self) -> None:
        alpha = self.process("edge.png")[..., 3]
        self.assertLessEqual(int(alpha[:, -1].max()), EDGE_ALPHA_LIMIT)
        self.assertLessEqual(int(alpha[-1, :].max()), EDGE_ALPHA_LIMIT)

    def test_shadow_is_visible_on_all_four_sides(self) -> None:
        alpha = self.process("sides.png")[..., 3].astype(float)
        ys, xs = np.where(alpha >= 250)
        top, bottom, left, right = ys.min(), ys.max(), xs.min(), xs.max()
        # The strongest alpha in the three pixel rows or columns just outside the card's opaque extent. A shadow on
        # that side lifts it well above zero (vanilla measures 100 to 230 right next to the card).
        sides = {
            "top": alpha[max(top - 3, 0):top, :],
            "bottom": alpha[bottom + 1:bottom + 4, :],
            "left": alpha[:, max(left - 3, 0):left],
            "right": alpha[:, right + 1:right + 4],
        }
        for name, strip in sides.items():
            self.assertGreaterEqual(float(strip.max()), 40.0, f"no shadow outside the {name} side of the card")

    def test_output_is_deterministic(self) -> None:
        first = self.process("a.png")
        second = self.process("b.png")
        self.assertEqual(hashlib.sha256(first.tobytes()).hexdigest(), hashlib.sha256(second.tobytes()).hexdigest())

    def test_shadow_is_not_clipped_at_the_card_layer_bounds(self) -> None:
        # The old recipe blurred a layer the size of the rotated card, so the halo stopped at its bounding box.
        card = Image.new("RGBA", (40, 30), (255, 255, 255, 255))
        canvas = Image.new("RGBA", (80, 70), (0, 0, 0, 0))
        self.processor.apply_shadow(canvas, card, (20, 20), (0, 0), 2.3, 0.93)
        alpha = np.asarray(canvas)[..., 3]
        self.assertGreater(int(alpha[19, 40]), 0)  # one row above the card's top edge
        self.assertGreater(int(alpha[40, 19]), 0)  # one column left of the card

    def test_recorded_recipe_version_is_current(self) -> None:
        self.assertGreaterEqual(self.processor.RECIPE_VERSION, 2)


if __name__ == "__main__":
    unittest.main()
