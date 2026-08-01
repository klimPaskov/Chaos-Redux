"""Reproduce the IW-018 ARX source-locked 156x210 portrait candidates.

Each crop removes only excess lower torso or side background before the
repository's standard ffmpeg Lanczos resize. The processor never draws a
face, insignia, frame, advisor overlay, or other subject.
"""

from pathlib import Path
import argparse
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PORTRAITS = {
	"emilio_lussu": ("ARX_emilio_lussu_hoi4_repaint_v1.png", "portrait_ARX_independence_wave_emilio_lussu_156x210_candidate.png", "crop=1054:1418:0:0"),
	"luigi_mella_santelia": ("ARX_luigi_mella_santelia_hoi4_repaint_v1.png", "portrait_ARX_luigi_mella_santelia_156x210_candidate.png", "crop=1047:1409:34:0"),
	"vittorio_verne": ("ARX_vittorio_verne_hoi4_repaint_v1.png", "portrait_ARX_vittorio_verne_156x210_candidate.png", "crop=1081:1455:0:0"),
	"gioacchino_solinas": ("ARX_gioacchino_solinas_hoi4_repaint_v1.png", "portrait_ARX_gioacchino_solinas_156x210_candidate.png", "crop=1084:1451:0:0"),
}


def export(name: str) -> None:
	source_name, output_name, crop = PORTRAITS[name]
	source = ROOT / "repaints_raw" / source_name
	output = ROOT / "repaints_processed" / output_name
	output.parent.mkdir(parents=True, exist_ok=True)
	command = [
		"ffmpeg",
		"-hide_banner",
		"-loglevel",
		"error",
		"-y",
		"-i",
		str(source),
		"-vf",
		f"{crop},scale=156:210:flags=lanczos,format=rgba",
		"-frames:v",
		"1",
		str(output),
	]
	subprocess.run(command, check=True)
	print(output)


def main() -> None:
	parser = argparse.ArgumentParser()
	parser.add_argument("--portrait", choices=["all", *PORTRAITS], default="all")
	args = parser.parse_args()
	for name in PORTRAITS if args.portrait == "all" else [args.portrait]:
		export(name)


if __name__ == "__main__":
	main()
