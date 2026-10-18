"""Source-backed entry and notification regressions; no HOI4 execution.

The model executes the production gates and notification helpers.
Native ownership, disease visibility, human-host eligibility, event delivery,
and the existence of a suitable origin are explicit fixture boundaries.
It does not model spread, mortality, initialization, or event-target lifetime.
"""
from dataclasses import dataclass, field
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


def parse(text):
    tokens = re.findall(r'#[^\n]*|"[^"\n]*"|[{}=]|[^\s{}=]+', text)
    tokens = [t for t in tokens if not t.startswith('#')]
    index = 0

    def block():
        nonlocal index
        result = []
        while index < len(tokens) and tokens[index] != '}':
            key = tokens[index]
            index += 1
            if index == len(tokens) or tokens[index] != '=':
                result.append((key, None))
                continue
            index += 1
            value = tokens[index]
            index += 1
            if value == '{':
                value = block()
                assert tokens[index] == '}'
                index += 1
            result.append((key, value))
        return result

    return block()


def load(folder, name):
    return dict(parse((ROOT / 'common' / folder / name).read_text(encoding='utf-8-sig')))


TRIGGERS = load('scripted_triggers', '020_black_plague_triggers.txt')
EFFECTS = load('scripted_effects', '020_black_plague_effects.txt')
CONSTANTS = load('script_constants', '020_black_plague_constants.txt')


@dataclass
class Country:
    human: bool = True
    ai: bool = False
    flags: set = field(default_factory=set)
    values: dict = field(default_factory=dict)


@dataclass
class State:
    id: int
    owner: Country
    controller: Country
    neighbours: list = field(default_factory=list)
    public: bool = True
    established: bool = True


class Model:
    def __init__(self, flags=(), active=0, origin=True):
        self.flags = set(flags)
        self.active = active
        self.origin = origin
        self.events = []
        self.globals = {}
        self.global_consumers = []

    def value(self, token):
        if token.startswith('constant:'):
            group, key = token[9:].split('.')
            return float(dict(CONSTANTS[group])[key])
        if token == 'global.black_plague_active_states^num':
            return self.active
        if token.startswith('global.'):
            return self.globals.get(token, 0)
        raise AssertionError(token)

    def matches(self, nodes, scope=None):
        def match(key, data):
            if key == 'OR':
                return any(match(k, v) for k, v in data)
            if key in ('AND', 'hidden_trigger'):
                # hidden_trigger only hides its tooltip; it is evaluated like AND.
                return self.matches(data, scope)
            if key == 'NOT':
                return not any(match(k, v) for k, v in data)
            if key == 'has_global_flag':
                return data in self.flags
            if key == 'has_country_flag':
                return data in scope.flags
            if key == 'has_variable':
                return data in self.globals if data.startswith('global.') else data in scope.values
            if key == 'is_ai':
                return scope.ai == (data == 'yes')
            if key == 'black_plague_has_valid_origin':
                return self.origin
            if key == 'black_plague_country_is_human_host':
                return scope.human
            if key == 'black_plague_state_is_publicly_visible':
                return scope.public
            if key == 'black_plague_state_is_established':
                return scope.established
            if key == 'check_variable':
                if dict(data).get('compare') == 'greater_than':
                    return self.value(dict(data)['var']) > self.value(dict(data)['value'])
                left, compare, right = [k for k, _ in data]
                assert compare == '>'
                return self.value(left) > self.value(right)
            if key in TRIGGERS:
                return self.matches(TRIGGERS[key], scope)
            raise AssertionError((key, data))
        return all(match(k, v) for k, v in nodes)

    def execute(self, nodes, scope, prev=None):
        for key, data in nodes:
            if key == 'if':
                if self.matches(dict(data)['limit'], scope):
                    self.execute([(k, v) for k, v in data if k != 'limit'], scope, prev)
            elif key in ('OWNER', 'CONTROLLER'):
                self.execute(data, getattr(scope, key.lower()), scope)
            elif key == 'every_neighbor_state':
                for neighbour in scope.neighbours:
                    self.execute(data, neighbour, scope)
            elif key == 'set_country_flag':
                scope.flags.add(data)
            elif key == 'set_variable':
                name, value = data[0]
                if name.startswith('global.'):
                    self.globals[name] = self.value(value)
                else:
                    assert value == 'PREV' and isinstance(prev, State)
                    scope.values[name] = prev.id
            elif key == 'country_event':
                self.events.append((scope, dict(data)['id']))
            elif key in ('black_plague_emit_death_threshold_report', 'black_plague_emit_eradication_report',
                         'black_plague_evolution_runtime_pulse', 'black_plague_rat_run_runtime_pulse',
                         'black_plague_achievement_process_runtime_pulse', 'black_plague_refresh_air_cleanliness_source',
                         'black_plague_scenario_refresh_shared_threat'):
                # Global progression consumers are outside this orchestration model.
                assert isinstance(scope, Country)
                self.global_consumers.append(key)
            elif key in EFFECTS:
                self.execute(EFFECTS[key], scope, prev)
            else:
                raise AssertionError((key, data))


class OutbreakTests(unittest.TestCase):
    def test_initialized_empty_runtime_can_start(self):
        model = Model(flags=['black_plague_system_started', 'black_plague_system_active'])
        self.assertTrue(model.matches(TRIGGERS['black_plague_automatic_event_is_available']))

    def test_existing_outbreak_and_terminal_states_block(self):
        for flags, active in [(['black_plague_natural_outbreak_started'], 0),
                              (['black_plague_state_was_established'], 0),
                              ([], 1), (['world_end'], 0),
                              (['black_plague_terminal_takeover_complete'], 0)]:
            with self.subTest(flags=flags, active=active):
                self.assertFalse(Model(flags, active).matches(TRIGGERS['black_plague_automatic_event_is_available']))

    def test_no_origin_still_blocks(self):
        self.assertFalse(Model(origin=False).matches(TRIGGERS['black_plague_automatic_event_is_available']))

    def test_notifications_aggregate_and_freeze_places(self):
        domestic, nearby = Country(), Country()
        border = State(2, nearby, nearby)
        origin = State(1, domestic, domestic, [border, border])
        model = Model()
        model.execute(EFFECTS['black_plague_notify_exposed_players'], origin)
        later_border = State(4, nearby, nearby)
        later_case = State(3, domestic, domestic, [later_border])
        model.execute(EFFECTS['black_plague_notify_exposed_players'], later_case)
        self.assertEqual([event for _, event in model.events], ['chaosx.nr20.16', 'chaosx.nr20.15'])
        self.assertEqual(domestic.values['black_plague_domestic_notice_state'], 1)
        self.assertEqual(nearby.values['black_plague_nearby_notice_state'], 2)

    def test_domestic_notice_suppresses_nearby_duplicate(self):
        country = Country(flags={'black_plague_domestic_notice_received'})
        neighbour = State(2, country, country)
        origin = State(1, Country(ai=True), Country(ai=True), [neighbour])
        model = Model()
        model.execute(EFFECTS['black_plague_notify_exposed_players'], origin)
        self.assertEqual(model.events, [])

    def test_hidden_cases_and_scenario_bootstrap_do_not_notify(self):
        country = Country()
        for public, flags in [(False, []), (True, ['black_plague_triggerable_scenario_bootstrap'])]:
            model = Model(flags=flags)
            model.execute(EFFECTS['black_plague_notify_exposed_players'], State(1, country, country, public=public))
            self.assertEqual(model.events, [])

    def test_country_aftermath_consumes_each_sequence_once(self):
        model = Model(flags={'black_plague_system_active'})
        model.globals['global.black_plague_pulse_sequence'] = 1
        for _ in range(2):
            model.execute(EFFECTS['black_plague_process_global_country_pulse'], Country())
        self.assertEqual(len(model.global_consumers), 7)
        model.globals['global.black_plague_pulse_sequence'] = 2
        model.execute(EFFECTS['black_plague_process_global_country_pulse'], Country())
        self.assertEqual(len(model.global_consumers), 14)
        model.flags.add('black_plague_pulses_suppressed')
        model.globals['global.black_plague_pulse_sequence'] = 3
        model.execute(EFFECTS['black_plague_process_global_country_pulse'], Country())
        self.assertEqual(len(model.global_consumers), 14)

    def test_aftermath_receiver_declares_country_root(self):
        events = parse((ROOT / 'events/020_black_death.txt').read_text(encoding='utf-8-sig'))
        receiver = [(kind, dict(data)) for kind, data in events if isinstance(data, list)
                    and dict(data).get('id') == 'chaosx.nr20.906']
        self.assertEqual([kind for kind, _ in receiver], ['country_event'])
        immediate = dict(receiver[0][1]['immediate'])['hidden_effect']
        self.assertIn(('black_plague_process_global_country_pulse', 'yes'), immediate)


if __name__ == '__main__':
    unittest.main()
