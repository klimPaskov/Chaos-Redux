"""Remove the residual neutral-white checker fringe from the v8 reference cutout."""

from __future__ import annotations

import sys

import cv2
import numpy as np
from PIL import Image
from scipy import ndimage


def main() -> int:
	if len(sys.argv) != 3:
		raise SystemExit("usage: process_checker_alpha_v8.py INPUT OUTPUT")

	image = np.array(Image.open(sys.argv[1]).convert("RGBA"))
	rgb = image[:, :, :3]
	alpha = image[:, :, 3]
	kernel = np.ones((3, 3), dtype=np.uint8)

	# Drop one outer layer of essentially white checker pixels.
	for _ in range(1):
		transparent_neighbor = cv2.dilate((alpha == 0).astype(np.uint8), kernel) > 0
		channel_spread = rgb.max(axis=2) - rgb.min(axis=2)
		neutral_white = (rgb.min(axis=2) > 250) & (channel_spread < 8)
		remove = (alpha > 0) & transparent_neighbor & neutral_white
		alpha[remove] = 0

	# Decontaminate the remaining neutral-white boundary without shrinking thin
	# bow, string, hair, quiver, or boot silhouettes. Each fringe pixel receives
	# the colour of its nearest opaque, non-white interior pixel.
	channel_spread = rgb.max(axis=2) - rgb.min(axis=2)
	neutral_white = (rgb.min(axis=2) > 220) & (channel_spread < 15)
	near_transparency = cv2.dilate((alpha == 0).astype(np.uint8), kernel, iterations=3) > 0
	fringe = (alpha > 0) & near_transparency & neutral_white
	good = (alpha > 0) & ~neutral_white
	_, nearest = ndimage.distance_transform_edt(~good, return_indices=True)
	rgb[fringe] = rgb[nearest[0][fringe], nearest[1][fringe]]

	image[:, :, 3] = alpha
	Image.fromarray(image, mode="RGBA").save(sys.argv[2])
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
