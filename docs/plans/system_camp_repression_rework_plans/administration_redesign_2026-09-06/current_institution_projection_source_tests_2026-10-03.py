"""Institution display fixtures using the existing parsed production runtime.
Engine primitives are mocked by foundation_source_tests; no HOI4 or pixel proof.
"""
import copy
import hashlib
import json
import re
from pathlib import Path
import foundation_source_tests as foundation

HERE = Path(__file__).resolve().parent
ROOT = foundation.ROOT

def runtime():
    r = foundation.Runtime()
    r.triggers.update({k: v for k, _, v in foundation.parse((ROOT / 'common/scripted_triggers/camp_administration_country_triggers.txt').read_text(encoding='utf-8-sig'))})
    for name in ('camp_administration_country_constants.txt', 'camp_administration_civil_constants.txt'):
        for category, _, body in foundation.parse((ROOT / 'common/script_constants' / name).read_text(encoding='utf-8-sig')):
            for key, _, value in body:
                if key != 'schema' and not isinstance(value, list):
                    r.constants[category + '.' + key] = float(value)
    return r

CASES = [
    ('civil claims', 'USA', {'camp_admin_civil_claims_active'}, {'camp_admin_civil_claims_progress': 3}, .5, 6),
    ('civil review', 'ENG', {'camp_admin_civil_review_active'}, {'camp_admin_civil_review_progress': 1}, 1 / 3, 3),
    ('major archives', 'GER', {'camp_admin_country_archive_work_active'}, {'camp_admin_country_archive_progress': 3}, .5, 6),
    ('major oversight', 'JAP', {'camp_admin_country_oversight_active'}, {'camp_admin_country_review_progress': 4}, 4 / 6, 6),
    ('active major program', 'SOV', {'camp_admin_institution_slot_active'}, {'camp_admin_country_program': 7, 'camp_admin_institution_progress': 3, 'camp_admin_institution_target': 6}, .5, 6),
    ('saved suspended program', 'SOV', {'camp_admin_country_institution_paused'}, {'camp_admin_country_program': 7, 'camp_admin_institution_progress': 2, 'camp_admin_institution_target': 6}, 2 / 6, 6),
    ('zero target', 'GER', {'camp_admin_institution_slot_active'}, {'camp_admin_country_program': 1, 'camp_admin_institution_progress': 2, 'camp_admin_institution_target': 0}, 0, 0),
    ('inactive without paid work', 'GER', set(), {'camp_admin_country_program': 1, 'camp_admin_institution_progress': 0, 'camp_admin_institution_target': 6}, 0, 0),
    ('suspended without paid work', 'GER', {'camp_admin_country_institution_paused'}, {'camp_admin_country_program': 1, 'camp_admin_institution_progress': 0, 'camp_admin_institution_target': 6}, 0, 0),
    ('upper clamp', 'GER', {'camp_admin_country_archive_work_active'}, {'camp_admin_country_archive_progress': 9}, 1, 6),
    ('lower clamp', 'JAP', {'camp_admin_country_oversight_active'}, {'camp_admin_country_review_progress': -2}, 0, 6),
]

def select_text(path, getter, r, scope):
    definitions = foundation.parse((ROOT / path).read_text(encoding='utf-8-sig'))
    body = next(body for key, _, body in definitions if key == 'defined_text' and foundation.get(body, 'name') == getter)
    for key, _, branch in body:
        if key == 'text' and r.cond(foundation.get(branch, 'trigger', []), scope):
            return foundation.get(branch, 'localization_key')
    raise AssertionError(getter)

def labels():
    strings = {}
    for path in (ROOT / 'localisation/english').glob('camp_administration*_l_english.yml'):
        for line in path.read_text(encoding='utf-8-sig').splitlines():
            match = re.match(r'^([^:]+): "(.*)"$', line)
            if match:
                strings[match[1]] = match[2]
    font = Path('C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/fonts/hoi_18mbs.fnt')
    advances = {}
    pairs = {}
    for line in font.read_text(encoding='utf-8-sig').splitlines():
        fields = dict(re.findall(r'(\w+)=(-?\d+)', line))
        if line.startswith('char '):
            advances[int(fields['id'])] = int(fields['xadvance'])
        elif line.startswith('kerning '):
            pairs[int(fields['first']), int(fields['second'])] = int(fields['amount'])
    keys = ['camp_admin_civil_status_claims', 'camp_admin_civil_status_review', 'camp_admin_civil_status_claims_complete', 'camp_admin_civil_status_conversion', 'camp_admin_civil_status_funded', 'camp_admin_civil_status_authorized', 'camp_admin_civil_status_inactive']
    out = []
    for key in keys:
        text = strings[key]
        width = sum(advances[ord(c)] for c in text) + sum(pairs.get((ord(a), ord(b)), 0) for a, b in zip(text, text[1:]))
        assert width <= 388, (key, width)
        out.append({'key': key, 'text': text, 'fontAdvanceWidth': width, 'sourceTextBoxWidth': 388})
    return {'note': 'Installed BMFont advances with kerning, not a production image or complete rendered glyph bounds.', 'font': str(font), 'fontSha256': hashlib.sha256(font.read_bytes()).hexdigest(), 'labels': out}

def run_cases():
    out = []
    for name, tag, flags, values, expected, target in CASES:
        r = runtime()
        c = r.country(tag)
        r.state(88, tag, population=100)
        c['flags'].update(flags)
        c.update(values)
        c.update(camp_admin_gui_institution_progress=99, camp_admin_gui_institution_target=99)
        before = copy.deepcopy(r.scopes)
        temporary_before = copy.deepcopy(r.temp)
        r.run('camp_admin_project_institution_progress', tag)
        assert abs(c['camp_admin_gui_institution_progress'] - expected) < .00001, name
        assert c['camp_admin_gui_institution_target'] == target, name
        after = copy.deepcopy(r.scopes)
        for view in (before, after):
            view[tag].pop('camp_admin_gui_institution_progress', None)
            view[tag].pop('camp_admin_gui_institution_target', None)
        assert before == after, (name, 'non-display scope mutation')
        assert temporary_before == r.temp and r.debits == 0 and r.logged == 0, name
        progress_key = select_text('common/scripted_localisation/camp_administration_ui_localisation.txt', 'GetCampAdminInstitutionProgress', r, tag)
        assert progress_key == ('camp_admin_institution_progress_value' if target > 0 else 'camp_admin_blank'), name
        out.append({'fixture': name, 'fraction': c['camp_admin_gui_institution_progress'], 'target': target, 'progressKey': progress_key, 'onlyDisplayVariablesChanged': True})
    return out

def status_cases():
    cases = [
        ('claims over review', {'camp_admin_civil_claims_active', 'camp_admin_civil_review_active'}, 'camp_admin_civil_status_claims'),
        ('review over funded policy', {'camp_admin_civil_review_active', 'camp_admin_civil_policy_funded'}, 'camp_admin_civil_status_review'),
        ('settled claims', {'camp_admin_civil_claims_complete'}, 'camp_admin_civil_status_claims_complete'),
        ('conversion', {'camp_admin_reforming'}, 'camp_admin_civil_status_conversion'),
        ('funded policy', {'camp_admin_civil_policy_funded', 'camp_admin_civil_policy_authorized'}, 'camp_admin_civil_status_funded'),
        ('authorized policy', {'camp_admin_civil_policy_authorized'}, 'camp_admin_civil_status_authorized'),
        ('inactive', set(), 'camp_admin_civil_status_inactive'),
    ]
    out = []
    for name, flags, expected in cases:
        r = runtime()
        c = r.country('USA')
        c['flags'].update(flags)
        before = copy.deepcopy(r.scopes)
        key = select_text('common/scripted_localisation/camp_administration_country_localisation.txt', 'GetCampAdminCivilInstitutionStatus', r, 'USA')
        assert key == expected and before == r.scopes, name
        out.append({'fixture': name, 'selectedKey': key, 'noScopeMutation': True})
    return out

def quote_boundary_cases():
    parsed = foundation.parse((ROOT / 'common/scripted_localisation/camp_administration_country_localisation.txt').read_text(encoding='utf-8-sig'))
    getter = next(body for key, _, body in parsed if key == 'defined_text' and foundation.get(body, 'name') == 'GetCampAdminCountryAction1BlockedReason')
    checks = {foundation.get(body, 'localization_key'): foundation.get(body, 'trigger', []) for key, _, body in getter if key == 'text'}
    out = []
    for name, pp, support, expected in [('exact quote', 5, 12, (False, False)), ('PP short by one fixed-point unit', 4.999, 12, (True, False)), ('support short by one fixed-point unit', 5, 11.999, (False, True)), ('above both quotes', 5.001, 12.001, (False, False))]:
        r = runtime()
        c = r.country('GER', support=support)
        c['political_power'] = pp
        c['camp_admin_budget'] = r.constants['camp_admin_budget.development']
        before = copy.deepcopy(r.scopes)
        actual = tuple(r.cond(checks[key], 'GER') for key in ('camp_admin_country_action_1_blocked_pp', 'camp_admin_country_action_1_blocked_support'))
        assert actual == expected and before == r.scopes, name
        assert r.cond(r.triggers['camp_admin_country_can_commit'], 'GER') == (not any(expected)), name
        out.append({'fixture': name, 'PPBlocked': actual[0], 'supportBlocked': actual[1], 'matchesAuthorizationPredicate': True, 'noScopeMutation': True})
    return out

def place_cases():
    cases = [
        ('active program', {'camp_admin_institution_slot_active'}, 7, 88, False, 'camp_admin_institution_active_place'),
        ('halted saved program', {'camp_admin_country_institution_paused'}, 7, 88, False, 'camp_admin_institution_active_place'),
        ('captured saved program', {'camp_admin_country_institution_paused'}, 7, 88, True, 'camp_admin_institution_active_place'),
        ('zero saved state', {'camp_admin_institution_slot_active'}, 7, 0, False, 'camp_admin_blank'),
        ('missing saved state', {'camp_admin_institution_slot_active'}, 7, None, False, 'camp_admin_blank'),
        ('national archives', {'camp_admin_country_archive_work_active', 'camp_admin_institution_slot_active'}, 0, None, False, 'camp_admin_blank'),
        ('national oversight', {'camp_admin_country_oversight_active', 'camp_admin_institution_slot_active'}, 0, None, False, 'camp_admin_blank'),
        ('civil review', {'camp_admin_civil_review_active', 'camp_admin_institution_slot_active'}, 0, None, False, 'camp_admin_blank'),
        ('no program with stale site', set(), 0, 88, False, 'camp_admin_blank'),
    ]
    out = []
    for name, flags, program, state_id, captured, expected in cases:
        r = runtime()
        c = r.country('SOV')
        r.country('POL')
        state = r.state(88, 'SOV', population=100)
        if captured:
            state['controller'] = 'POL'
            state['owner'] = 'POL'
        c['flags'].update(flags)
        c['camp_admin_country_program'] = program
        c.pop('camp_admin_institution_state_id', None)
        if state_id is not None:
            c['camp_admin_institution_state_id'] = state_id
        before = copy.deepcopy(r.scopes)
        actual = select_text('common/scripted_localisation/camp_administration_country_localisation.txt', 'GetCampAdminInstitutionPlace', r, 'SOV')
        assert actual == expected and before == r.scopes, name
        assert r.debits == 0 and r.logged == 0, name
        out.append({'fixture': name, 'selectedKey': actual, 'savedStateId': state_id, 'captured': captured, 'noScopeMutation': True})
    return out

if __name__ == '__main__':
    result = {'scope': 'Parsed production effect using existing foundation runtime and real constants/triggers, mocked engine primitives. No pixel or engine proof.', 'fixtures': run_cases(), 'statusFixtures': status_cases(), 'quoteBoundaryFixtures': quote_boundary_cases(), 'placeFixtures': place_cases(), 'fontMetrics': labels()}
    paths = ['common/scripted_effects/camp_administration_ui_effects.txt', 'common/scripted_localisation/camp_administration_ui_localisation.txt', 'common/scripted_localisation/camp_administration_country_localisation.txt', 'localisation/english/camp_administration_ui_l_english.yml', 'localisation/english/camp_administration_country_l_english.yml', 'common/scripted_triggers/camp_administration_country_triggers.txt']
    result['sourceHashes'] = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths}
    (HERE / 'current_institution_projection_source_results_2026-10-03.json').write_bytes(json.dumps(result, indent=2).encode('utf-8'))
    print(json.dumps(result, indent=2))
