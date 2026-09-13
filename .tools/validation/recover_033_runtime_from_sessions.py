"""Locate complete Event 033 runtime snapshots in Codex session transcripts.

This recovery helper reads completed command stdout records, extracts only text
between the Event 033 runtime sentinels, and reports candidate hashes. It never
overwrites the gameplay source; ``--extract`` writes the selected candidate to
an explicit recovery path for separate validation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path


START = "# CHAOS REDUX - EVENT 033 ACID RAIN RUNTIME"
END = "# END_EVENT033_HOST_RUNTIME"


@dataclass(frozen=True)
class Candidate:
    session: Path
    ordinal: int
    timestamp: str
    text: str

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.text.encode("utf-8")).hexdigest()


def extract_candidate(stdout: str) -> str | None:
    if START not in stdout or END not in stdout:
        return None
    start = stdout.index(START)
    end = stdout.index(END, start) + len(END)
    if stdout[end : end + 2] == "\r\n":
        end += 2
    elif stdout[end : end + 1] == "\n":
        end += 1
    return stdout[start:end]


def scan_session(path: Path) -> list[Candidate]:
    candidates: list[Candidate] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if START not in line or END not in line:
                continue
            record = json.loads(line)
            item = record.get("payload", {}).get("item", {})
            stdout = item.get("stdout", "")
            text = extract_candidate(stdout)
            if text is None:
                continue
            candidates.append(
                Candidate(
                    session=path,
                    ordinal=int(record.get("ordinal", -1)),
                    timestamp=str(record.get("timestamp", "")),
                    text=text,
                )
            )
    return candidates


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sessions", type=Path, nargs="+")
    parser.add_argument("--extract", type=Path)
    parser.add_argument("--sha256", help="Select an exact candidate hash before extraction.")
    args = parser.parse_args()

    candidates = [candidate for session in args.sessions for candidate in scan_session(session)]
    candidates.sort(key=lambda candidate: (candidate.timestamp, candidate.ordinal))
    for index, candidate in enumerate(candidates, start=1):
        print(
            json.dumps(
                {
                    "index": index,
                    "session": str(candidate.session),
                    "ordinal": candidate.ordinal,
                    "timestamp": candidate.timestamp,
                    "sha256": candidate.sha256,
                    "bytes": len(candidate.text.encode("utf-8")),
                    "lines": len(candidate.text.splitlines()),
                },
                sort_keys=True,
            )
        )

    if args.extract:
        selected = [candidate for candidate in candidates if not args.sha256 or candidate.sha256 == args.sha256]
        if not selected:
            raise SystemExit("no matching complete runtime candidate")
        candidate = selected[-1]
        args.extract.parent.mkdir(parents=True, exist_ok=True)
        args.extract.write_bytes(candidate.text.encode("utf-8"))
        print(f"extracted {candidate.sha256} to {args.extract}")


if __name__ == "__main__":
    main()
