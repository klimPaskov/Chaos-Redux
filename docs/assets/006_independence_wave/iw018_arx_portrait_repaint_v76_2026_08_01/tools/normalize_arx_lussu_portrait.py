"""Reproduce the IW-018 Emilio Lussu 156x210 portrait candidate.

The source-locked ImageGen repaint is cropped only to remove lower torso
content and then scaled with ffmpeg's Lanczos filter. No face, emblem, frame,
or advisor overlay is drawn by this processor.
"""

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "repaints_raw/ARX_emilio_lussu_hoi4_repaint_v1.png"
OUTPUT = ROOT / "repaints_processed/portrait_ARX_independence_wave_emilio_lussu_156x210_candidate.png"
FILTER = "crop=1054:1418:0:0,scale=156:210:flags=lanczos,format=rgba"


def main() -> None:
	OUTPUT.parent.mkdir(parents=True, exist_ok=True)
	command = [
		"ffmpeg",
		"-hide_banner",
		"-loglevel",
		"error",
		"-y",
		"-i",
		str(SOURCE),
		"-vf",
		FILTER,
		"-frames:v",
		"1",
		str(OUTPUT),
	]
	subprocess.run(command, check=True)
	print(OUTPUT)


if __name__ == "__main__":
	main()
