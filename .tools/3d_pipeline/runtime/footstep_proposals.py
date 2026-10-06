"""Emit exact event snippets only from measured, certain sole plants.

Proposals carry the exact installed action SHA and never edit entity assets or
generate skeletal keys. An unmeasured stride cannot produce an event proposal.
"""
import argparse
import json
import re
from pathlib import Path


def proposals(report, cue, speed=1):
    if not re.fullmatch(r'[A-Za-z0-9_]+', cue):
        raise ValueError('Footstep proposal needs an exact soundeffect identifier')
    contact = report.get('foot_contacts', {})
    if contact.get('status') != 'pass' or speed <= 0:
        raise ValueError('Footstep placement needs a passing measured sole-contact stride and positive animation_speed.')
    plants = contact.get('plants', [])
    if any(plant['confidence'] != 'measured_certain' for plant in plants):
        raise ValueError('Uncertain plants cannot author runtime event times')
    return [{'foot': plant['foot'], 'frame': plant['frame'], 'time': plant['time_seconds'] / speed,
             'event': 'event = { time = %.4f sound = { soundeffect = "%s" } }' % (plant['time_seconds'] / speed, cue)}
            for plant in plants]


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--report', type=Path, required=True)
    cli.add_argument('--cue', required=True)
    cli.add_argument('--animation-speed', type=float, default=1)
    cli.add_argument('--output', type=Path, required=True)
    args = cli.parse_args()
    document = json.loads(args.report.read_text(encoding='utf-8-sig'))
    report = document.get('delivery', document)
    output = {'animation_sha256': document.get('animation_sha256') or document.get('file', {}).get('sha256'),
              'events': proposals(report, args.cue, args.animation_speed),
              'scope': 'reviewed entity-event proposals from measured existing authored action; no skeleton/key generation'}
    args.output.write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
