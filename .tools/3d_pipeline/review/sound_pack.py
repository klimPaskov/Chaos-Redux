"""Build a unit sound package from licensed source recordings.

Every source clip is converted mechanically (mono 44.1 kHz PCM16, lead-in trimmed from 5 ms
before the -40 dB onset to 20 ms after the -50 dB tail, 5 ms / 30 ms fades, peak-normalised to
-3 dBFS). Nothing is mixed, pitched, stretched, or synthesised. The tool writes the runtime WAVs,
a sound .asset with one `sound` per file and one `soundeffect` per effect (random variation among
its files), the `Effects` category registration, and a receipts JSON with source and output hashes.

Spec (JSON):
{
  "asset": "sound/chaosx_zombie_variant_sounds.asset",          # mod-relative output
  "wav_dir": "sound/002_zombie_outbreak/zombies/variants",       # mod-relative output folder
  "wav_prefix": "002_zombie_outbreak/zombies/variants",          # path as seen from sound/
  "receipts": "docs/.../variant_sound_receipts.json",
  "header": "Chaos Redux zombie variant voices.",
  "sources": {"artisticdude": {"dir": "docs/.../original_wavs", "licence": "CC0", "title": "...", "url": "..."}},
  "effects": {
    "chaosx_demonic_zombie_attack": {"source": "artisticdude", "files": ["zombie-14.wav"], "volume": 0.55,
                                      "falloff": "falloff_100", "max_audible": 5, "pitch": 0.08}
  }
}
Usage: python .tools/3d_pipeline/review/sound_pack.py <spec.json>
"""
import hashlib
import json
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np

MOD = Path(__file__).resolve().parents[3]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()


def process(src, dst):
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "m.wav"
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(src), "-ac", "1", "-ar", "44100", "-c:a", "pcm_s16le", str(tmp)], check=True)
        with wave.open(str(tmp)) as w:
            x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(float) / 32768
        pk = float(np.abs(x).max())
        if pk <= 0:
            raise ValueError(f"silent source {src}")
        on = int(np.argmax(np.abs(x) > pk * 10 ** (-40 / 20)))
        start = max(0, on - int(0.005 * 44100))
        tail = int(np.where(np.abs(x) > pk * 10 ** (-50 / 20))[0][-1])
        end = min(len(x), tail + int(0.02 * 44100))
        dur = (end - start) / 44100
        gain = -3 - 20 * np.log10(pk)
        af = (f"atrim=start_sample={start}:end_sample={end},asetpts=N/SR/TB,afade=t=in:d=0.005,"
              f"afade=t=out:st={max(0.0, dur - 0.03):.4f}:d=0.03,volume={gain:.3f}dB")
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(tmp), "-af", af, "-ac", "1", "-ar", "44100",
                        "-c:a", "pcm_s16le", "-map_metadata", "-1", str(dst)], check=True)
    return {"trim_s": [round(start / 44100, 4), round(end / 44100, 4)], "gain_db": round(float(gain), 2), "duration_s": round(dur, 3)}


def main():
    spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    wav_dir = MOD / spec["wav_dir"]
    wav_dir.mkdir(parents=True, exist_ok=True)
    sounds, effects, receipts = [], [], {"sources": spec["sources"], "files": []}
    done = {}
    for eff, cfg in spec["effects"].items():
        src_cfg = spec["sources"][cfg["source"]]
        names = []
        for f in cfg["files"]:
            key = (cfg["source"], f)
            if key not in done:
                out_name = f"{cfg['source']}_{Path(f).stem}.wav".replace("-", "_")
                src = MOD / src_cfg["dir"] / f
                info = process(src, wav_dir / out_name)
                sname = f"{Path(spec['asset']).stem}_{Path(out_name).stem}"
                sounds.append(f'sound = {{ name = "{sname}" file = "{spec["wav_prefix"]}/{out_name}" always_load = no }}')
                receipts["files"].append({"source": str(Path(src_cfg["dir"]) / f).replace("\\", "/"), "source_sha256": digest(src),
                                          "runtime": f"{spec['wav_dir']}/{out_name}", "runtime_sha256": digest(wav_dir / out_name), **info})
                done[key] = sname
            names.append(done[key])
        members = " ".join(f'sound = "{n}"' for n in names)
        pitch = cfg.get("pitch", 0.08)
        effects.append(f'soundeffect = {{ name = "{eff}" falloff = "{cfg.get("falloff", "falloff_100")}" sounds = {{ {members} }} '
                       f'volume = {cfg.get("volume", 0.55)} max_audible = {cfg.get("max_audible", 5)} max_audible_behaviour = fail '
                       f'playbackrate_random_offset = {{ -{pitch} {pitch} }} prevent_random_repetition = yes is3d = yes loop = no }}')
    lines = [f"# {spec['header']}", f"# Sources, licences, and processing receipts: {spec['receipts']}.", "",
             "category = {", '\tname = "Effects"', "\tsoundeffects = {"]
    lines += [f"\t\t{e}" for e in spec["effects"]] + ["\t}", "}", ""] + sounds + [""] + effects + [""]
    with open(MOD / spec["asset"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines))
    (MOD / spec["receipts"]).write_text(json.dumps(receipts, indent=1), encoding="utf-8")
    print("wrote", spec["asset"], len(sounds), "sounds", len(effects), "effects")


if __name__ == "__main__":
    main()
