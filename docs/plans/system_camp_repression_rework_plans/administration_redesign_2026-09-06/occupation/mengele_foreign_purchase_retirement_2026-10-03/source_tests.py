"""Run owned production completions and compatibility helpers with native PP mock.
This is source-contract evidence, not HOI4 execution or native cooldown proof.
"""
from pathlib import Path
from copy import deepcopy
import hashlib
import difflib
import json
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(HERE.parents[1]))
from foundation_source_tests import parse, get, prime_existing_custody
from major_countries_source_tests import CountryRuntime

IDS = ('import_subjects_from_japanese_china', 'import_subjects_from_india', 'import_subjects_from_africa')
HELPERS = ('germany_mengele_import_subjects_from_from_state_accepted', 'germany_mengele_import_subjects_from_from_state')


def block_bytes(data, identifier):
    """Extract one known definition without parsing unrelated package meta text."""
    match = re.search(rb'(?m)^\t?' + identifier.encode() + rb' = \{', data)
    assert match, identifier
    start = match.start()
    # These owned blocks contain no brace-bearing quoted text.
    depth = 0
    for index in range(data.index(b'{', start), len(data)):
        depth += (data[index:index+1] == b'{') - (data[index:index+1] == b'}')
        if depth == 0:
            return start, index + 1, data[start:index+1]
    raise AssertionError('Unclosed owned block ' + identifier)


def read_owned(path, identifiers):
    data = (ROOT / path).read_bytes()
    return data, {name: parse(block_bytes(data, name)[2].decode('utf-8-sig'))[0][2] for name in identifiers}


def mask_owned(data, identifiers):
    for start, end, _ in sorted((block_bytes(data, name) for name in identifiers), reverse=True):
        data = data[:start] + b'OWNED_BLOCK' + data[end:]
    return data


def runtime_fixture(programme='active', target='live'):
    runtime = CountryRuntime()
    country = runtime.country('GER')
    country['flags'].update({'camp_admin_initialized', 'genocide_decisions_visible',
                             'germany_mengele_program_authorized' if programme == 'active' else 'germany_mengele_program_restricted'})
    country.update(hidden_atrocity_score=9, genocide_tribunal_severity=8, mengele_permission_level=2,
                   mengele_autonomy=4, camp_admin_institution_progress=3, camp_admin_research_awards_this_year=1)
    if target != 'missing':
        runtime.country('JAP')
        site = runtime.state('88', 'GER', population=100, buildings=2)
        site.update(owner='POL', controller='GER')
        prime_existing_custody(runtime, '88', 10)
        # Historical source evidence must survive retirement, and a clean
        # target must gain no imported-state or atrocity-source marker.
        if target == 'historical':
            site['flags'].update({'germany_mengele_subjects_imported_from_state',
                                  'genocide_foreign_experimentation_source', 'genocide_atrocity_site_known_to_regime'})
        if target == 'ambiguous':
            site['flags'].add('camp_origin_ambiguous')
    for category, _, body in parse((ROOT / 'common/script_constants/germany_mengele_constants.txt').read_text(encoding='utf-8-sig')):
        for key, _, value in body:
            if key != 'schema' and not isinstance(value, list):
                runtime.constants[f'{category}.{key}'] = float(value)
    return runtime


def run_cases():
    decision_path = 'common/decisions/germany_mengele_decisions.txt'
    effect_path = 'common/scripted_effects/germany_mengele_effects.txt'
    decisions_bytes, decisions = read_owned(decision_path, IDS)
    effects_bytes, helpers = read_owned(effect_path, HELPERS)
    for current, before_name, identifiers in ((decisions_bytes, 'before_germany_mengele_decisions.txt', IDS),
                                             (effects_bytes, 'shared_current_outside_baseline_germany_mengele_effects.txt', HELPERS)):
        assert mask_owned(current, identifiers) == mask_owned((HERE / before_name).read_bytes(), identifiers)
    old_outside = mask_owned((HERE / 'before_germany_mengele_effects.txt').read_bytes(), HELPERS).decode('utf-8-sig').splitlines()
    new_outside = mask_owned(effects_bytes, HELPERS).decode('utf-8-sig').splitlines()
    shared_outputs = ('mengele_clone_deployment_command_power_spend', 'black_friday_owner_transaction_id',
                      'universal_cost_quote_final_cost', 'universal_cost_quote_valid', 'universal_cost_quote_affordable',
                      'universal_cost_payment_result', 'universal_cost_record_transaction_result',
                      'universal_cost_settle_transaction_result')
    reviewed_achievement_inputs = (
        'set_temp_variable = { universal_cost_transaction_achievement_family_id = constant:universal_cost_family.command_power }',
        'set_temp_variable = { universal_cost_transaction_achievement_primary_component_id = constant:black_friday_event.owner_component_command_power }',
        'set_temp_variable = { universal_cost_transaction_achievement_cost_basis = constant:universal_cost_achievement_basis.primary_component }',
        'set_temp_variable = { universal_cost_transaction_achievement_primary_member = constant:universal_cost_framework.one }',
    )
    # Parent reviewed these four exact existing-owner inputs in this one
    # transaction-recording context. Do not admit arbitrary achievement vars.
    achievement_block = '\n'.join('\t\t\t\t' + line for line in reviewed_achievement_inputs)
    assert effects_bytes.decode('utf-8-sig').replace('\r\n', '\n').count(
        '\t\t\t\tset_temp_variable = { universal_cost_record_transaction_result = constant:universal_cost_framework.result_no_op }\n'
        + achievement_block + '\n\t\t\t\tuniversal_cost_record_transaction = yes') == 1
    # The wait for the AI baseline overlapped another owner's cost-helper
    # work. Check the actual original freeze, allowing only its reviewed
    # output initialization insertions outside our helper ownership.
    for tag, a, b, c, d in difflib.SequenceMatcher(None, old_outside, new_outside, autojunk=False).get_opcodes():
        if tag != 'equal':
            assert tag == 'insert', ('Unreviewed shared edit', tag, old_outside[a:b], new_outside[c:d])
            for line in new_outside[c:d]:
                assert (line.strip() == '# Existing-owner caller output storage.' or
                        line.strip() in reviewed_achievement_inputs or
                        any(line.strip().startswith('set_temp_variable = { ' + name + ' = ') for name in shared_outputs)), line
    results = [{'case': 'owned_boundaries_and_reviewed_concurrent_output_insertions', 'passed': True}]
    for identifier in IDS:
        decision = decisions[identifier]
        before = parse(block_bytes((HERE / 'before_germany_mengele_decisions.txt').read_bytes(), identifier)[2].decode('utf-8-sig'))[0][2]
        assert get(decision, 'cost') == get(before, 'cost')
        assert get(decision, 'days_re_enable') == get(before, 'days_re_enable')
        assert get(decision, 'ai_will_do') == get(before, 'ai_will_do')
        completion = get(decision, 'complete_effect')
        assert completion == [('add_political_power', '=', get(decision, 'cost'))]
        for programme in ('active', 'restricted'):
            for target in ('live', 'historical', 'missing', 'ambiguous'):
                runtime = runtime_fixture(programme, target)
                # The production initialized-administration gate is what
                # retires these rows. Programme and target primitives are
                # supplied below only to stress stale callback inertness.
                runtime.triggers['germany_mengele_program_active'] = [('always', '=', 'yes' if programme == 'active' else 'no')]
                runtime.triggers['germany_mengele_restricted_program_active'] = [('always', '=', 'yes' if programme == 'restricted' else 'no')]
                for gate in ('visible', 'target_root_trigger'):
                    cutover = next(entry for entry in get(decision, gate) if entry == ('NOT', '=', [('has_country_flag', '=', 'camp_admin_initialized')]))
                    assert not runtime.cond([cutover], 'GER')
                assert not runtime.cond(get(get(decision, 'available'), 'hidden_trigger'), 'GER')
                for gate in ('visible', 'target_root_trigger'):
                    assert not runtime.cond(get(decision, gate), 'GER')
                cost = runtime.val(get(decision, 'cost'), 'GER')
                before_scopes = deepcopy(runtime.scopes)
                for _ in range(2):
                    # Native cost is the only payment for these IDs. Every
                    # stale paid invocation is charged before its completion.
                    runtime.scopes['GER']['political_power'] -= cost
                    runtime.execute(completion, 'GER')
                    assert runtime.scopes == before_scopes
                assert runtime.debits == 0 and runtime.logged == 0 and not runtime.awards
                assert 'last_country_event' not in runtime.temp
                results.append({'case': f'{identifier}_{programme}_{target}_paid_replay',
                                'refund_pp': cost, 'net_pp_change': 0, 'physical_debits': 0,
                                'report_events': 0, 'native_cooldown': 'not modeled'})
    for helper in HELPERS:
        for target in ('live', 'historical', 'missing', 'ambiguous'):
            runtime = runtime_fixture(target=target)
            runtime.effects.update(helpers)
            before_scopes = deepcopy(runtime.scopes)
            for _ in range(2):
                runtime.temp['germany_mengele_foreign_subjects_autonomy'] = 999
                runtime.run(helper, 'GER')
                assert runtime.temp['germany_mengele_foreign_subjects_autonomy'] == 0
                assert runtime.scopes == before_scopes
            assert runtime.debits == 0 and runtime.logged == 0 and not runtime.awards
            assert 'last_country_event' not in runtime.temp
            results.append({'case': f'{helper}_{target}_direct_replay', 'persistent_changes': 0})
    return {'status': 'passed', 'source_scenarios': results,
            'source_hashes': {decision_path: hashlib.sha256(decisions_bytes).hexdigest(),
                              effect_path: hashlib.sha256(effects_bytes).hexdigest()},
            'limits': ['Native charge is explicitly mocked before each paid completion.',
                       'No native cooldown cancellation or engine execution is proved.',
                       'Uncharged direct execution of a native refund body is outside this paid-completion contract.']}


if __name__ == '__main__':
    result = run_cases()
    (HERE / 'source_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'scenarios': len(result['source_scenarios'])}))
