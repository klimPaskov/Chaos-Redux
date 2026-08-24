"""Extract the baked neutral checker field without erasing pale character materials."""

from __future__ import annotations

import sys

import cv2
import numpy as np
from PIL import Image
from scipy import ndimage


def main() -> int:
	if len(sys.argv) != 3:
		raise SystemExit("usage: process_checker_alpha_chiveli_v9.py INPUT OUTPUT")

	image = np.array(Image.open(sys.argv[1]).convert("RGBA"))
	rgb = image[:, :, :3]
	spread = rgb.max(axis=2).astype(np.int16) - rgb.min(axis=2).astype(np.int16)
	minimum = rgb.min(axis=2)
	light_neutral = (minimum >= 228) & (spread <= 15)
	strong_subject = (spread >= 22) | (minimum <= 205)

	# Seed GrabCut with the light-neutral checker as probable background and the
	# character's chromatic/dark pixels as definite foreground. This lets pale
	# belly highlights follow adjacent skin instead of being keyed away, while
	# enclosed checker gaps around the bow and limbs remain background.
	mask = np.full(light_neutral.shape, cv2.GC_PR_FGD, dtype=np.uint8)
	mask[light_neutral] = cv2.GC_PR_BGD
	mask[strong_subject] = cv2.GC_FGD
	mask[:8, :] = cv2.GC_BGD
	mask[-8:, :] = cv2.GC_BGD
	mask[:, :8] = cv2.GC_BGD
	mask[:, -8:] = cv2.GC_BGD
	background_model = np.zeros((1, 65), np.float64)
	foreground_model = np.zeros((1, 65), np.float64)
	cv2.grabCut(rgb, mask, None, background_model, foreground_model, 6, cv2.GC_INIT_WITH_MASK)
	core = (mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD)
	# The painted abdominal highlight is intentionally almost neutral white. Its
	# bounded torso silhouette is unambiguous in the source render, so retain the
	# original RGB inside that closed anatomical region rather than allowing the
	# checker classifier to punch through it.
	torso = np.array([[802, 300], [875, 300], [880, 405], [795, 405]], dtype=np.int32)
	cv2.fillPoly(core, [torso], True)

	# A narrow soft edge keeps the bowstring and hair tips while avoiding a hard
	# cutout. Newly visible fringe pixels inherit nearest subject RGB so no baked
	# checker colour remains in partially transparent pixels.
	alpha = cv2.GaussianBlur((core.astype(np.uint8) * 255), (0, 0), 0.55)
	alpha[alpha < 8] = 0
	alpha[alpha > 247] = 255
	new_edge = (alpha > 0) & ~core
	_, nearest_core = ndimage.distance_transform_edt(~core, return_indices=True)
	rgb[new_edge] = rgb[nearest_core[0][new_edge], nearest_core[1][new_edge]]

	image[:, :, :3] = rgb
	image[:, :, 3] = alpha
	Image.fromarray(image, mode="RGBA").save(sys.argv[2])
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
