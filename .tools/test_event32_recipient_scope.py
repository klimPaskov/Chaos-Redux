"""Offline ROOT-boundary regression for Event 032 country transactions.

Models documented scope iteration, immediate country-event delivery, and the
positive reserve-package arithmetic. It does not establish runtime tie behavior.
It is source-path evidence, not a game simulation or probability evaluator.
Pass --baseline to prove the preserved pre-repair source violates the invariant.
"""

from pathlib import Path
import argparse
import re
import unittest
from decimal import Decimal, ROUND_HALF_UP


ROOT_DIR = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>]+')


def parse(text):
    tokens = [m.group() for m in TOKEN.finditer(text) if not m.group().startswith('#')]
    cursor = 0

    def block():
        nonlocal cursor
        result = []
        while cursor < len(tokens) and tokens[cursor] != '}':
            key = tokens[cursor]
            cursor += 1
            if cursor >= len(tokens) or tokens[cursor] not in ('=', '<', '>'):
                result.append((key, None))
                continue
            cursor += 1
            value = tokens[cursor]
            cursor += 1
            if value == '{':
                value = block()
                if cursor >= len(tokens) or tokens[cursor] != '}':
                    raise ValueError('Unclosed source block')
                cursor += 1
            result.append((key, value))
        return result

    return block()


def value(nodes, name):
    return next(v for k, v in nodes if k == name)


def descendants(nodes):
    for name, body in nodes:
        yield name, body
        if isinstance(body, list):
            yield from descendants(body)


def load_sources(baseline):
    if baseline:
        folder = ROOT_DIR / 'docs/plans/032_missiles_plans/baselines/2026-10-03_recipient_root'
        paths = [folder / name for name in (
            '032_missile_crisis.txt', '032_missiles_effects.txt',
            '032_missiles_scenario_effects.txt', '032_missiles_scenario_triggers.txt')]
    else:
        paths = [ROOT_DIR / name for name in (
            'events/032_missile_crisis.txt',
            'common/scripted_effects/032_missiles_effects.txt',
            'common/scripted_effects/032_missiles_scenario_effects.txt',
            'common/scripted_triggers/032_missiles_scenario_triggers.txt')]
    return [parse(p.read_text(encoding='utf-8-sig')) for p in paths]


parser = argparse.ArgumentParser()
parser.add_argument('--baseline', action='store_true')
parser.add_argument('--reserve-baseline', action='store_true')
args, unittest_args = parser.parse_known_args()
EVENTS, CORE, SCENARIO, TRIGGERS = load_sources(args.baseline)
if args.reserve_baseline:
    reserve_source = ROOT_DIR / 'docs/plans/032_missiles_plans/baselines/2026-10-03_reserve_integer/032_missiles_effects.txt'
    CORE = parse(reserve_source.read_text(encoding='utf-8-sig'))
RECEIVERS = {value(body, 'id'): body for kind, body in EVENTS if kind == 'country_event'}
CONSTANTS = dict(parse((ROOT_DIR / 'common/script_constants/032_missiles_constants.txt').read_text(encoding='utf-8-sig')))


def reserve_package(factories, states, mature=False, war=False, saturation=False, saturation_disabled=False):
    """Evaluate only the source package arithmetic, not game stockpile effects."""
    variables = {'num_of_factories': Decimal(factories), 'num_of_controlled_states': Decimal(states)}
    flags = {'missiles_program_mature': mature, 'missiles_evolution_saturation_arsenals': saturation}

    def number(token):
        if token.startswith('constant:'):
            group, key = token[9:].split('.', 1)
            return Decimal(value(CONSTANTS[group], key))
        return variables[token] if token in variables else Decimal(token)

    def execute(nodes):
        taken = False
        for name, body in nodes:
            if name == 'if':
                condition = dict(value(body, 'limit'))
                taken = flags.get(condition.get('has_country_flag'), False) or ('has_war' in condition and war)
                if 'missiles_saturation_active' in condition:
                    taken = saturation and not saturation_disabled
                if taken:
                    execute([(key, val) for key, val in body if key != 'limit'])
            elif name == 'else':
                if not taken:
                    execute(body)
            elif name == 'round_temp_variable':
                variables[body] = variables[body].quantize(Decimal(1), rounding=ROUND_HALF_UP)
            elif name == 'set_temp_variable':
                key, token = body[0]
                variables[key] = number(token)
            elif name in ('add_to_temp_variable', 'multiply_temp_variable', 'divide_temp_variable', 'clamp_temp_variable'):
                fields = dict(body)
                key = fields.get('var', body[0][0])
                if name == 'add_to_temp_variable':
                    variables[key] += number(fields[key])
                elif name == 'multiply_temp_variable':
                    variables[key] *= number(fields['value'])
                elif name == 'divide_temp_variable':
                    variables[key] /= number(fields['value'])
                else:
                    variables[key] = min(number(fields['max']), max(number(fields['min']), variables[key]))
            else:
                raise AssertionError(f'Package arithmetic requires explicit support for {name}')

    execute(value(CORE, 'missiles_calculate_reserve_package'))
    return variables['missiles_package_base']


def country_root_at_call(nodes, current, root, sought):
    """Follow source calls through the immediate receiver until setup begins."""
    for name, body in nodes:
        if name == sought:
            return root
        if name == 'country_event':
            receiver = RECEIVERS[value(body, 'id')]
            if any(k in ('days', 'hours', 'months') for k, _ in body):
                raise AssertionError('Recipient transaction was delayed')
            found = country_root_at_call(value(receiver, 'immediate'), current, current, sought)
        elif name == 'missiles_process_frozen_recipient':
            found = country_root_at_call(value(CORE, name), current, root, sought)
        elif isinstance(body, list) and name != 'limit':
            found = country_root_at_call(body, current, root, sought)
        else:
            found = None
        if found is not None:
            return found
    return None


class RecipientRootRegression(unittest.TestCase):
    def check_loop(self, definitions, entry, array, helper):
        loops = [body for name, body in descendants(value(definitions, entry))
                 if name == 'for_each_scope_loop' and value(body, 'array') == array]
        self.assertEqual(len(loops), 1)
        # A major, subject, and one-state minor must each own their mutations,
        # even though a different country initiated the global transaction.
        for recipient in ('GER', 'CAN', 'LUX'):
            with self.subTest(recipient=recipient):
                resolved = country_root_at_call(loops[0], recipient, 'ENG', helper)
                self.assertEqual(resolved, recipient)

    def test_global_firing_recipient_root(self):
        self.check_loop(CORE, 'missiles_global_firing_transaction',
                        'global.missiles_frozen_recipients', 'missiles_initialize_or_advance_program')

    def test_scenario_package_recipient_root(self):
        self.check_loop(SCENARIO, 'missiles_scenario_launch_unregistered',
                        'global.missiles_scenario_selected_recipients', 'missiles_scenario_apply_country_package')

    def test_preflight_uses_recipient_country(self):
        state_gate = value(value(TRIGGERS, 'missiles_scenario_country_has_site_plan'), 'any_owned_state')
        fields = dict(state_gate)
        self.assertEqual(fields.get('is_controlled_by'), 'PREV')
        self.assertEqual(fields.get('missiles_state_has_valid_site_geography'), 'yes')

    def test_receiver_delivery_is_hidden_and_unpaced(self):
        for event_id in ('chaosx.nr32.5', 'chaosx.nr32.6'):
            self.assertTrue(event_id in RECEIVERS, f'Missing receiver {event_id}')
            receiver = RECEIVERS[event_id]
            self.assertEqual(value(receiver, 'hidden'), 'yes')
            self.assertEqual(value(receiver, 'is_triggered_only'), 'yes')
            keys = {name for name, _ in descendants(receiver)}
            self.assertFalse(keys & {'record_events_log_history_entry', 'handle_fired_event', 'news_event'})

    def test_event_option_weights_unchanged(self):
        # The only accepted later change is the AI guard on the special-payload
        # selection options (chaosx.nr32.31), which rejects a special warhead
        # whose standing policy would refuse every ordinary preparation.
        policy_guard = ('modifier', [('factor', 'constant:missiles_ai_factor.reject'),
                                     ('NOT', [('missiles_special_payload_policy_permits_ordinary_use', 'yes')])])
        before_events = load_sources(True)[0]
        before = [(name, body) for name, body in descendants(before_events) if name == 'ai_chance']
        after = [(name, [entry for entry in body if entry != policy_guard])
                 for name, body in descendants(EVENTS) if name == 'ai_chance']
        self.assertEqual(after, before)

    def test_event16_host_receipt_is_not_consumed_by_first_nonhost(self):
        setup = value(CORE, 'missiles_initialize_or_advance_program')
        calls = [name for name, _ in descendants(setup)]
        self.assertIn('brilliant_scientist_record_missile_crisis', calls)
        gates = [body for name, body in descendants(setup) if name == 'has_global_flag']
        self.assertNotIn('missiles_event16_bridge_fired', gates)

    def test_registration_capacity_reads_state_value(self):
        registration = value(CORE, 'missiles_register_site')
        sums = [body for name, body in descendants(registration)
                if name == 'add_to_variable' and 'missiles_total_site_capacity' in dict(body)]
        self.assertEqual(len(sums), 1)
        self.assertEqual(value(sums[0], 'missiles_total_site_capacity'), 'PREV.missiles_site_capacity')

    def test_first_package_advances_existing_research(self):
        ordinary_setup = value(value(CORE, 'missiles_initialize_or_advance_program'), 'else')
        first_package = value(ordinary_setup, 'if')
        self.assertEqual(dict(first_package).get('missiles_apply_next_technology_step'), 'yes')

    def test_exhausted_technology_line_is_valid(self):
        step = value(CORE, 'missiles_apply_next_technology_step')
        completed = [body for name, body in step if name in ('if', 'else_if')
                     and isinstance(body, list)
                     and any(name == 'value' and token == 'constant:missiles_stage.complete'
                             for name, token in descendants(value(body, 'limit')))]
        self.assertEqual(len(completed), 1)
        keys = [name for name, _ in descendants(completed[0])]
        self.assertNotIn('set_technology', keys)
        self.assertEqual(value(completed[0], 'set_country_flag'), 'missiles_supported_line_complete')

    def test_technology_grants_use_country_report(self):
        grants = [body for name, body in descendants(value(CORE, 'missiles_apply_next_technology_step'))
                  if name == 'set_technology']
        self.assertTrue(grants)
        self.assertTrue(all(dict(grant).get('popup') == 'no' for grant in grants))

    def test_reserve_package_creates_whole_missiles(self):
        for factories in (0, 5, 17, 63, 64):
            for states in (1, 7, 40, 50):
                for mature, war, saturation in ((False, False, False), (True, True, False), (True, True, True)):
                    with self.subTest(factories=factories, states=states, mature=mature, war=war, saturation=saturation):
                        package = reserve_package(factories, states, mature, war, saturation)
                        self.assertGreaterEqual(package, 0)
                        self.assertEqual(package, package.to_integral_value())


if __name__ == '__main__':
    unittest.main(argv=[__file__, *unittest_args])
