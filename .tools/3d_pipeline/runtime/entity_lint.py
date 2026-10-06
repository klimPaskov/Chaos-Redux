"""Lint unit particle density, sound lifetime, and installed action timing.

No source or runtime asset is edited. Motion peaks are synchronization proxies;
only explicit hash-bound contact markers establish authored contact evidence.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import subprocess
import wave

from clausewitz import walk
from inventory import REPO, VANILLA, definitions, effective_entity, index_assets, resolve, snapshot
from pdx_reader import read, sha256


def number(value, default=None):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def duration(path):
    try:
        with wave.open(str(path), 'rb') as audio:
            return audio.getnframes() / audio.getframerate()
    except (wave.Error, EOFError):
        output = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                 '-of', 'json', str(path)], capture_output=True, text=True, check=True)
        return float(json.loads(output.stdout)['format']['duration'])


def particle_index():
    types, systems = {}, {}
    for root in (VANILLA, REPO):
        for folder, suffixes in [(root / 'gfx/entities', {'.gfx'}),
                                 (root / 'gfx/particles', {'.asset', '.gfx'})]:
            for source in definitions(folder, suffixes):
                if 'tree' not in source:
                    continue
                for node in walk(source['tree']):
                    if node.key in {'particleType', 'pdxparticle', 'particle'} and node.scalar('name'):
                        row = {'path': source['path'], 'node': node}
                        (systems if node.key == 'particle' else types)[node.scalar('name')] = row
    result = {}
    for name, definition in types.items():
        file_value = definition['node'].scalar('file')
        target = resolve(file_value, definition['path']) if file_value else None
        type_value = definition['node'].scalar('type')
        candidates = [s for key, s in systems.items() if
                      (target and s['path'].resolve() == target) or key == type_value]
        if not target and candidates:
            target = candidates[0]['path']
        lives, spans, rates = [], [], []
        for source in candidates:
            for system in source['node'].children('subsystem'):
                for key, bucket in [('life', lives), ('duration', spans), ('emission', rates)]:
                    rows = system.children(key)
                    if rows:
                        node = rows[0]
                        vals = [number(n.value) for n in node.children()] if isinstance(node.value, list) else [number(node.value)]
                        bucket.extend(v for v in vals if v is not None)
        result[name] = {'file': str(target) if target else file_value,
                        'sha256': sha256(target) if target else None,
                        'max_particle_life_s': max(lives) if lives else None,
                        'max_emitter_duration_s': max(spans) if spans else None,
                        'max_emission_per_s': max(rates) if rates else None}
    return result


def lint_state(state, *, entity_name, path, cycle, cue_samples, effects, particles,
               motion=None, contact_markers=None, animation_sha=None):
    findings = []
    name = state.scalar('name')
    speed = number(state.scalar('animation_speed', '1'), 1)
    if speed <= 0:
        findings.append({'rule': 'invalid_animation_speed'})
    cycle = cycle / speed if cycle and speed > 0 else cycle
    repeating = state.scalar('looping') == 'yes' or state.scalar('next_state') == name
    events = []
    by_node = defaultdict(list)
    for node in state.children('event'):
        event = {'time': number(node.scalar('time', '0'), 0), 'line': node.line,
                 'locator': node.scalar('node', '<entity>'), 'particle': node.scalar('particle'),
                 'keep_particle': node.scalar('keep_particle') == 'yes',
                 'trigger_once': node.scalar('trigger_once') == 'yes',
                 'soundeffect': next((n.value for n in walk(node) if n.key == 'soundeffect'), None)}
        events.append(event)
        if cycle and (event['time'] < 0 or event['time'] >= cycle):
            findings.append({'rule': 'event_outside_action', **event, 'cycle_s': cycle})
        if event['particle']:
            particle = particles.get(event['particle'])
            if particle is None:
                findings.append({'rule': 'particle_definition_unresolved', **event})
            else:
                event['particle_definition'] = particle
                by_node[event['locator']].append(event)
                if event['keep_particle'] and any(v in event['particle'].lower() for v in ('muzzle', 'flash', 'casing', 'blood')):
                    findings.append({'rule': 'keep_particle_on_impulse_emitter', **event})
        cue = event['soundeffect']
        if cue:
            effect = effects.get(cue)
            if not effect:
                findings.append({'rule': 'soundeffect_unresolved', **event})
                continue
            loop = effect['node'].scalar('loop', 'no') == 'yes'
            durations = cue_samples.get(cue, [])
            longest = max(durations) if durations else None
            if repeating and event['trigger_once'] and not loop:
                findings.append({'rule': 'one_shot_then_silent_repeating_state', **event})
            if cycle and longest and longest > cycle:
                if not (loop and event['trigger_once'] and number(effect['node'].scalar('max_audible')) == 1):
                    findings.append({'rule': 'sample_longer_than_cycle_without_single_loop', **event,
                                     'sample_s': longest, 'cycle_s': cycle})
            if loop and repeating and not event['trigger_once']:
                findings.append({'rule': 'loop_restarted_each_cycle', **event})
    for locator, rows in by_node.items():
        rows.sort(key=lambda r: r['time'])
        pairs = list(zip(rows, rows[1:]))
        if repeating and cycle and len(rows) > 1:
            pairs.append((rows[-1], {**rows[0], 'time': rows[0]['time'] + cycle}))
        for left, right in pairs:
            life = left['particle_definition']['max_particle_life_s']
            if life and right['time'] - left['time'] < life:
                findings.append({'rule': 'particle_overlap_on_locator', 'locator': locator,
                                 'first_line': left['line'], 'second_line': right['line'],
                                 'spacing_s': right['time'] - left['time'], 'particle_life_s': life})
    reports = [e for e in events if e['soundeffect'] and any(s in e['soundeffect'].lower() for s in ('shot', 'fire', 'mg_attack', 'rifle_attack', 'burst'))]
    for report in reports:
        nearby = [e for e in events if abs(e['time'] - report['time']) <= .15 and e['particle']]
        flashes = [e for e in nearby if any(s in e['particle'].lower() for s in ('muzzle', 'flash'))]
        if len(flashes) != 1:
            findings.append({'rule': 'one_flash_per_report', 'line': report['line'], 'count': len(flashes)})
    for cue in {e['soundeffect'] for e in events if e['soundeffect']}:
        rows = sorted(e['time'] for e in events if e['soundeffect'] == cue)
        longest = max(cue_samples.get(cue, []), default=0)
        gaps = [b - a for a, b in zip(rows, rows[1:])]
        if cycle and repeating and rows and not all(e['trigger_once'] for e in events if e['soundeffect'] == cue):
            gaps.append(cycle + rows[0] - rows[-1])
        if gaps and longest > min(gaps):
            findings.append({'rule': 'sound_samples_overlap', 'soundeffect': cue,
                             'sample_s': longest, 'smallest_gap_s': min(gaps)})
    contacts = contact_markers or []
    for event in events:
        cue = event['soundeffect'] or ''
        if name not in {'attack', 'support_attack', 'defend', 'training', 'death'} or not any(s in cue.lower() for s in ('impact', 'attack', 'shot', 'release', 'strike', 'burst', 'spray')):
            continue
        exact = [m for m in contacts if m.get('animation_sha256') == animation_sha and
                 m.get('event_line') == event['line'] and m.get('entity') == entity_name]
        if exact:
            delta = min(abs(event['time'] - m['time_s'] / speed) for m in exact)
            if delta > .15:
                findings.append({'rule': 'authored_contact_timing_offset', 'line': event['line'], 'offset_s': delta})
        else:
            # Measured peaks are useful leads, but a snap is not a weapon strike.
            rows = (motion or {}).get('world_motion', {}).get('world_motion_peak_table', []) or (motion or {}).get('motion_peak_table', [])
            relevant = [m for m in rows if any(part in m.get('bone', '').lower() for part in ('hand', 'arm', 'weapon', 'jaw', 'claw'))]
            if relevant:
                angular_max = max(m.get('angular_deg', 0) for m in relevant)
                speed_max = max(m.get('translation_step', 0) for m in relevant)
                relevant = [m for m in relevant if m.get('angular_deg', 0) >= .8 * angular_max or m.get('translation_step', 0) >= .8 * speed_max]
            delta = min((abs(event['time'] - m['time_seconds'] / speed) for m in relevant), default=None)
            if delta is not None and delta > .15:
                findings.append({'rule': 'measured_contact_peak_offset', 'line': event['line'], 'offset_s': delta,
                                 'basis': 'strongest measured joint-motion peaks; semantic contact remains subject to review'})
            findings.append({'rule': 'contact_evidence_required', 'line': event['line'],
                             'nearest_motion_peak_offset_s': delta, 'within_0_15s': delta <= .15 if delta is not None else None,
                             'animation_sha256': animation_sha})
    return {'entity': entity_name, 'state': name, 'path': path, 'line': state.line,
            'animation': state.scalar('animation'), 'cycle_s': cycle, 'repeating': repeating,
            'events': events, 'findings': findings}


def audit(inventory, motion_reports=None, contacts=None):
    meshes, animations, entities, sounds, effects, errors = index_assets()
    particles = particle_index()
    cue_samples, report_rows = {}, []
    for model in inventory['models']:
        for cue in model['sound_cues']:
            if cue['name'] in cue_samples:
                continue
            cue_samples[cue['name']] = [duration(Path(s['file']['path']) if Path(s['file']['path']).is_absolute() else REPO / s['file']['path'])
                                         for s in cue['samples'] if s['file']]
        for entity in model['entities']:
            node = effective_entity(entity['name'], entities)
            armed = any(child.key == 'particle' and any(token in str(child.value).lower() for token in ('muzzle', 'laser', 'spray')) for child in walk(node))
            for state in node.children('state'):
                action = model['actions'].get(state.scalar('animation'), {})
                item = action.get('file')
                cycle, motion = None, None
                if item:
                    tree, _ = read(resolve(item['path']))
                    info = tree.find('info')
                    cycle = info.get('sa')[0] / info.get('fps')[0]
                    motion = (motion_reports or {}).get(item['sha256'])
                state_report = lint_state(state, entity_name=entity['name'], path=entity['path'],
                                               cycle=cycle, cue_samples=cue_samples, effects=effects,
                                               particles=particles, motion=motion, contact_markers=contacts,
                                               animation_sha=item['sha256'] if item else None)
                if armed and state.scalar('name') in {'attack', 'defend', 'support_attack'}:
                    if not any(event['particle'] for event in state_report['events']) or not any(event['soundeffect'] for event in state_report['events']):
                        state_report['findings'].append({'rule': 'weapon_state_missing_particle_or_sound',
                                                        'basis': 'same entity has firing particles; owner must declare any non-firing state exception'})
                report_rows.append(state_report)
    counts = defaultdict(int)
    for row in report_rows:
        for finding in row['findings']:
            counts[finding['rule']] += 1
    return {'schema': 1, 'coverage': {'states': len(report_rows), 'particles': len(particles),
                                     'source_parse_errors': errors}, 'rules': dict(counts), 'states': report_rows,
            'limitation': 'Motion peaks are measured proxies. Hash-bound authored contact markers are required for a timing pass.'}


if __name__ == '__main__':
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--inventory', type=Path)
    cli.add_argument('--motion', type=Path)
    cli.add_argument('--contacts', type=Path)
    cli.add_argument('--output', type=Path, required=True)
    args = cli.parse_args()
    data = json.loads(args.inventory.read_text()) if args.inventory else snapshot()
    motions = json.loads(args.motion.read_text()) if args.motion else None
    contacts = json.loads(args.contacts.read_text()) if args.contacts else None
    result = audit(data, motions, contacts)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'coverage': result['coverage'], 'rules': result['rules'], 'output': str(args.output)}))
