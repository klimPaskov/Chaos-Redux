from pathlib import Path
import re
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06'))
from foundation_source_tests import parse, get
ROOT = Path(__file__).resolve().parents[4]
EFFECTS = ROOT / 'common/scripted_effects/camp_administration_civil_effects.txt'
ACHIEVEMENTS = ROOT / 'common/achievements/chaos_redux_achievements.txt'
LOCALISATION = ROOT / 'localisation/english/chaosx_achievements_l_english.yml'
CLAIMS = ROOT / 'common/scripted_effects/camp_administration_civil_effects.txt'

def block(path, key):
    return next(value for name, _, value in parse(path.read_text(encoding='utf-8-sig')) if name == key)

def constant(name):
    top = parse((ROOT / 'common/script_constants/camp_administration_civil_constants.txt').read_text(encoding='utf-8-sig'))
    group = get(top, 'camp_admin_civil')
    return float(get(group, name))

def matches(items, country, flags, variables, war):
    for key, op, value in items:
        if key in ('AND','OR','NOT'):
            results = [matches(value, country, flags, variables, war)] if key == 'NOT' else [matches([child], country, flags, variables, war) for child in value]
            if key == 'NOT' and results[0]: return False
            if key == 'AND' and not all(results): return False
            if key == 'OR' and not any(results): return False
        elif key == 'original_tag':
            if country != value: return False
        elif key == 'tag':
            if country != value: return False
        elif key == 'has_war':
            if war != (value == 'yes'): return False
        elif key == 'camp_administration_civil_review_ready':
            if variables.get('review_ready', True) != (value == 'yes'): return False
        elif key == 'check_variable':
            var = get(value, 'var')
            if var is None:
                var, compare, rhs_key = value[0]
            else:
                compare, rhs_key = get(value, 'compare', 'equals'), get(value, 'value')
            lhs = variables.get(var, 0)
            rhs = constant(rhs_key.split('.',1)[1]) if rhs_key.startswith('constant:') else float(rhs_key)
            ok = lhs >= rhs if compare in ('greater_than_or_equals','>') else lhs == rhs
            if not ok: return False
        else:
            raise AssertionError(f'Unhandled review trigger in source suite: {key}')
    return True

def execute(items, country, flags, variables, war):
    i = 0
    while i < len(items):
        key, op, value = items[i]
        if key == 'if':
            chain = [(key, value)]; i += 1
            while i < len(items) and items[i][0] in ('else_if','else'):
                chain.append((items[i][0], items[i][2])); i += 1
            for branch, body in chain:
                limit = get(body, 'limit', []) if branch != 'else' else []
                if branch == 'else' or matches(limit, country, flags, variables, war):
                    execute([node for node in body if node[0] != 'limit'], country, flags, variables, war)
                    break
            continue
        if key == 'set_country_flag': flags.add(value)
        elif key == 'clr_country_flag': flags.discard(value)
        elif key in ('set_variable','add_to_variable','subtract_from_variable','clamp_variable','add_autonomy_ratio'): pass
        else: raise AssertionError(f'Unhandled review effect in source suite: {key}')
        i += 1

def run_finish(country, war=True, progress=None, ready=True):
    effect = block(EFFECTS, 'camp_administration_civil_finish_review')
    outer = effect[0][2]
    review_months = constant('review_months')
    flags = {'camp_admin_civil_review_active','camp_admin_institution_slot_active'}
    variables = {'camp_admin_civil_review_progress': review_months if progress is None else progress, 'review_ready': ready}
    if matches(get(outer, 'limit'), country, flags, variables, war):
        execute([node for node in outer if node[0] != 'limit'], country, flags, variables, war)
    return flags

def test_country_settlements():
    assert 'camp_rework_uk_raj_review_complete' in run_finish('ENG')
    usa_war = run_finish('USA', war=True)
    assert 'camp_rework_usa_court_review_complete' in usa_war
    assert 'camp_rework_achievement_usa_redress_before_victory' in usa_war
    usa_peace = run_finish('USA', war=False)
    assert 'camp_rework_usa_court_review_complete' in usa_peace
    assert 'camp_rework_achievement_usa_redress_before_victory' not in usa_peace
    italy = run_finish('ITA')
    assert {'camp_admin_civil_review_complete','camp_rework_italy_desert_camps_closed'} <= italy
    assert not run_finish('USA', progress=constant('review_months') - 1).__contains__('camp_admin_civil_review_complete')
    assert not run_finish('USA', ready=False).__contains__('camp_admin_civil_review_complete')

def test_achievement_68_and_claims_open():
    block68 = block(ACHIEVEMENTS, '000_chaos_redux_68_roads_without_camps')
    text = str(block68)
    assert 'camp_admin_civil_review_complete' in text and 'camp_rework_italy_desert_camps_closed' in text
    assert 'camp_rework_achievement_italy_conventional_infrastructure_complete' not in text
    assert 'camp_rework_achievement_italy_conventional_garrison_used' not in text
    assert 'is_core_of' in text and 'infrastructure' in text and 'divisions_in_state' in text
    source = CLAIMS.read_text(encoding='utf-8-sig')
    assert 'camp_administration_civil_usa_claims_open = yes' in source
    assert not re.search(r'\bdate\s*[<>]', source)
    assert 'camp_rework_achievement_usa_redress_before_victory' in source
    assert 'has_war = yes' in source[source.index('camp_rework_achievement_usa_redress_before_victory')-80:source.index('camp_rework_achievement_usa_redress_before_victory')]
    loc = LOCALISATION.read_text(encoding='utf-8-sig')
    assert 'while the war is still being fought, then settle the property claims.' in loc
    assert 'retain a developed Libyan state with an Italian division stationed there.' in loc

if __name__ == '__main__':
    test_country_settlements()
    test_achievement_68_and_claims_open()
    print('PASS: ENG, USA wartime, USA peacetime, ITA review completion; progress/readiness gates; 68 retained-state checks; claims open once relocation authority ends and the war is over.')
