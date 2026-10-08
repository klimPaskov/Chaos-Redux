"""Build the pure Event016 state/province geometry query from a verified MCP catalog.

The input contains all state memberships, not supply-node or ownership eligibility.
Run --extract with an artifact and its returned digest, then --write or --check.
"""
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'docs/testing/event016_transit_catalog_20261008/state_membership.json'
OUTPUTS = {
    'constants': ROOT / 'common/script_constants/016_transit_catalog_constants.txt',
    'public': ROOT / 'common/scripted_triggers/016_transit_state_province_catalog_triggers.txt',
    'data': ROOT / 'common/scripted_triggers/016_transit_state_province_catalog_data.txt',
}


def extract(path, expected_sha):
    raw = Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected_sha, 'MCP artifact bytes changed'
    artifact = json.loads(raw)
    checks = {x['id']: x['passed'] for x in artifact['validation']['checks']}
    for key in ['map-files-and-definitions', 'map-bitmap-geometry', 'map-state-region-membership', 'map-networks-adjacencies']:
        assert checks.get(key), 'Required map-source check failed: ' + key
    states = []
    for s in sorted(artifact['catalog']['states'], key=lambda x: x['id']):
        states.append({'id': s['id'], 'provinceIds': sorted(s['provinceIds']),
                       'sourcePath': s['sourcePath'], 'sourceLine': s['sourceLine'],
                       'sourceSha256': artifact['sourceHashes'][s['sourcePath']]})
    data = {'schemaVersion': 1, 'revision': artifact['revision'], 'artifactSha256': expected_sha,
            'states': states, 'mapCheckResults': checks,
            'overallValidationPassed': artifact['validation']['passed']}
    validate(data)
    INPUT.parent.mkdir(parents=True, exist_ok=True)
    if INPUT.exists():
        assert json.loads(INPUT.read_text(encoding='utf-8')) == data, 'Preserved catalog differs; review a new revision explicitly'
    else:
        INPUT.write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')


def validate(data):
    assert data['schemaVersion'] == 1
    states = data['states']
    ids = [s['id'] for s in states]
    assert all(type(x) is int for x in ids), 'State IDs must be integers, not booleans/fractions'
    assert ids and ids == sorted(set(ids)) and min(ids) > 0
    provinces = []
    for s in states:
        p = s['provinceIds']
        assert all(type(x) is int for x in p), 'Province IDs must be integers, not booleans/fractions'
        assert p and p == sorted(set(p)) and min(p) > 0
        assert s['sourcePath'] and len(s['sourceSha256']) == 64
        provinces.extend(p)
    assert len(provinces) == len(set(provinces)), 'Duplicate state/province membership'


def render(data):
    states = data['states']
    first, last = states[0]['id'], states[-1]['id']
    constants = ('# Event016 source-geometry bounds; generated from the retained MCP membership input.\n'
                 '# These are map IDs and query metadata, not balance tuning or live eligibility.\n'
                 'transit_catalog = {\n\tschema = { any_key = yes data = int }\n'
                 f'\tzero = 0\n\tone = 1\n\tstate_id_min = {first}\n\tstate_id_max = {last}\n}}\n')
    blocks = []

    def branch(rows):
        name = f"brilliant_scientist_transit_catalog_{rows[0]['id']}_{rows[-1]['id']}"
        if len(rows) == 1:
            row = rows[0]
            lines = [f'{name} = {{', '\tif = {',
                     f"\t\tlimit = {{ check_variable = {{ var = transit_catalog_state_id value = {row['id']} compare = equals }} }}"]
            lines += [f'\t\tadd_to_temp_array = {{ array = transit_state_province_ids value = {p} }}' for p in row['provinceIds']]
            lines += ['\t\tset_temp_variable = { transit_catalog_loaded = constant:transit_catalog.one }', '\t}', '\talways = yes', '}']
        else:
            mid = len(rows) // 2
            left, right = branch(rows[:mid]), branch(rows[mid:])
            lines = [f'{name} = {{', '\tif = {',
                     f"\t\tlimit = {{ check_variable = {{ transit_catalog_state_id < {rows[mid]['id']} }} }}",
                     f'\t\t{left} = yes', '\t}', '\telse = {', f'\t\t{right} = yes', '\t}', '\talways = yes', '}']
        blocks.append('\n'.join(lines))
        return name

    top = branch(states)
    data_source = ('# Event016 exact state/province geometry data. Generated; regenerate rather than editing IDs.\n'
                   f"# MCP revision {data['revision']}; retained source input {INPUT.relative_to(ROOT).as_posix()}.\n"
                   '# Pure STATE-trigger leaves append only temporary data; no live supply or ownership fact is stored.\n\n'
                   + '\n\n'.join(blocks) + '\n')
    public = ('# Event016 lazy state/province membership query, STATE scope.\n'
              '# Caller initializes all consumed temporary outputs before this pure query.\n'
              '# Numeric GetID is distinct from the opaque state id variable.\n'
              '# Unknown IDs leave an empty array and loaded=zero; no dynamically pasted helper name.\n'
              '# See 016_transit_state_province_catalog_triggers.md.\n\n'
              'brilliant_scientist_transit_load_state_province_catalog = {\n'
              '\tclear_temp_array = transit_state_province_ids\n'
              '\tset_temp_variable = { transit_catalog_state_id = constant:transit_catalog.zero }\n'
              '\tset_temp_variable = { transit_catalog_loaded = constant:transit_catalog.zero }\n'
              '\tmeta_trigger = {\n\t\ttext = {\n'
              '\t\t\tset_temp_variable = { transit_catalog_state_id = [STATE_ID] }\n'
              '\t\t\talways = yes\n\t\t}\n\t\tSTATE_ID = "[This.GetID]"\n\t}\n'
              '\tif = {\n\t\tlimit = {\n'
              '\t\t\tcheck_variable = { var = transit_catalog_state_id value = constant:transit_catalog.state_id_min compare = greater_than_or_equals }\n'
              '\t\t\tcheck_variable = { var = transit_catalog_state_id value = constant:transit_catalog.state_id_max compare = less_than_or_equals }\n'
              f'\t\t}}\n\t\t{top} = yes\n\t}}\n\talways = yes\n}}\n')
    return {'constants': constants, 'public': public, 'data': data_source}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--extract')
    p.add_argument('--sha256')
    p.add_argument('--write', action='store_true')
    p.add_argument('--check', action='store_true')
    args = p.parse_args()
    if args.extract:
        assert args.sha256, 'Use the returned MCP artifact digest'
        extract(args.extract, args.sha256)
    data = json.loads(INPUT.read_text(encoding='utf-8'))
    validate(data)
    result = render(data)
    if args.write:
        for key, text in result.items():
            OUTPUTS[key].write_bytes(text.encode('utf-8'))
    if args.check:
        for key, text in result.items():
            assert OUTPUTS[key].read_bytes() == text.encode('utf-8'), 'Generated source differs: ' + key
    print(json.dumps({'states': len(data['states']), 'memberships': sum(len(s['provinceIds']) for s in data['states']),
                      'outputHashes': {k: hashlib.sha256(v.encode('utf-8')).hexdigest() for k, v in result.items()}}))


if __name__ == '__main__':
    main()
