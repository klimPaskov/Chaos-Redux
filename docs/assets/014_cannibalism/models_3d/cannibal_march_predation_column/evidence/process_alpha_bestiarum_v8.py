"""Create and lightly decontaminate alpha for the approved Bestiarum v8 reference."""

from __future__ import annotations

import io
import sys

import cv2
import numpy as np
from PIL import Image
from rembg import new_session, remove
from scipy import ndimage


def main() -> int:
	if len(sys.argv) != 3:
		raise SystemExit("usage: process_alpha_bestiarum_v8.py INPUT OUTPUT")

	source = Image.open(sys.argv[1]).convert("RGB")
	cutout_bytes = remove(
		_image_bytes(source),
		session=new_session("u2net"),
		post_process_mask=True,
	)
	image = np.array(Image.open(io.BytesIO(cutout_bytes)).convert("RGBA"))
	rgb = image[:, :, :3]
	alpha = image[:, :, 3]
	kernel = np.ones((3, 3), dtype=np.uint8)

	# Replace neutral checker contamination only at the cutout boundary. The
	# subject's interior ash-white paint and ivory bone must remain untouched.
	channel_spread = rgb.max(axis=2) - rgb.min(axis=2)
	neutral_light = (rgb.min(axis=2) > 205) & (channel_spread < 16)
	near_transparency = cv2.dilate((alpha == 0).astype(np.uint8), kernel, iterations=2) > 0
	fringe = (alpha > 0) & near_transparency & neutral_light
	good = (alpha > 0) & ~neutral_light
	_, nearest = ndimage.distance_transform_edt(~good, return_indices=True)
	rgb[fringe] = rgb[nearest[0][fringe], nearest[1][fringe]]

	# Reintroduce a narrow antialiased edge from the clean binary mask. Newly
	# visible edge pixels inherit the nearest subject colour, never checker RGB.
	core = alpha > 0
	soft_alpha = cv2.GaussianBlur(alpha, (0, 0), 0.55)
	soft_alpha[soft_alpha < 8] = 0
	soft_alpha[soft_alpha > 247] = 255
	new_edge = (soft_alpha > 0) & ~core
	_, nearest_core = ndimage.distance_transform_edt(~core, return_indices=True)
	rgb[new_edge] = rgb[nearest_core[0][new_edge], nearest_core[1][new_edge]]
	alpha = soft_alpha

	image[:, :, 3] = alpha
	Image.fromarray(image, mode="RGBA").save(sys.argv[2])
	return 0


def _image_bytes(image: Image.Image) -> bytes:
	buffer = io.BytesIO()
	image.save(buffer, format="PNG")
	return buffer.getvalue()


if __name__ == "__main__":
	raise SystemExit(main())
