"""Run Event 042's parsed entry and recovery effects under narrow stubs.

This is an actual-source interpreter for the entry and recovery state machines.
It models persistent country flags, helper temp lifetimes, queueing country
events, lost-state eligibility, manual reroutes, and modifier/accident receipts.
Manifest construction and physical stockpile operations are narrow stubs. It
does not emulate HOI4, combat, or effects outside the command set below.
"""

from copy import deepcopy
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
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
            operator = tokens[cursor]
            cursor += 1
            value = tokens[cursor]
            cursor += 1
            if operator in ('<', '>'):
                result.append((key, (operator, value)))
                continue
            if value == '{':
                value = block()
                if cursor >= len(tokens) or tokens[cursor] != '}':
                    raise ValueError('Unclosed source block')
                cursor += 1
            result.append((key, value))
        return result

    result = block()
    if cursor != len(tokens):
        raise ValueError('Unexpected trailing source tokens')
    return result


def get(nodes, key):
    return next(value for name, value in nodes if name == key)


def entries(nodes, key):
    return [value for name, value in nodes if name == key]


def descendants(nodes):
    for name, body in nodes:
        yield name, body
        if isinstance(body, list):
            yield from descendants(body)


def event_map(source):
    return {get(body, 'id'): body for name, body in source if name == 'country_event'}


EVENTS = event_map(parse((ROOT / 'events/042_equipment_from_heavens.txt').read_text(encoding='utf-8-sig')))
EFFECTS = {name: body for name, body in parse((ROOT / 'common/scripted_effects/042_equipment_from_heavens_effects.txt').read_text(encoding='utf-8-sig')) if isinstance(body, list)}
TRIGGERS = {name: body for name, body in parse((ROOT / 'common/scripted_triggers/042_equipment_from_heavens_triggers.txt').read_text(encoding='utf-8-sig')) if isinstance(body, list)}


class EntryModel:
    """Execute actual entry/preparation effects with validity and stockpile stubs."""

    def __init__(self, countries):
        self.countries = {tag: {'flags': set(), 'vars': {}, 'valid': valid}
                          for tag, valid in countries.items()}
        self.current = next(iter(self.countries))
        self.temp = {}
        self.temp_arrays = {}
        self.targets = {}
        self.global_vars = {}
        self.queue = []
        self.visible = []
        self.unavailable = 0
        self.grants = 0
        self.manifest_manual = {}

    def number(self, token):
        if token is None:
            return 0
        if token.isdigit():
            return int(token)
        if token == 'yes':
            return True
        if token == 'no':
            return False
        if token.startswith('constant:') or token == 'global.date':
            return 0
        if '^' in token:
            key, index = token.rsplit('^', 1)
            if index == 'num':
                return len(self.temp_arrays.get(key, []))
            return self.temp_arrays.get(key, [])[int(self.number(index))]
        if token.startswith('global.'):
            return self.global_vars.get(token[7:], 0)
        return self.temp.get(token, self.countries[self.current]['vars'].get(token, 0))

    def set_value(self, key, token, temporary=False):
        value = self.number(token)
        if key.startswith('global.'):
            self.global_vars[key[7:]] = value
            return
        if '^' in key:
            name, index = key.rsplit('^', 1)
            array = self.temp_arrays.setdefault(name, [])
            index = int(index)
            while len(array) <= index:
                array.append(None)
            array[index] = value
        elif temporary:
            self.temp[key] = value
        else:
            self.countries[self.current]['vars'][key] = value

    def condition(self, nodes):
        result = True
        for name, body in nodes:
            if not result:
                break
            if name == 'NOT':
                result = not self.condition(body)
            elif name == 'OR':
                result = any(self.condition([entry]) for entry in body)
            elif name == 'AND':
                result = all(self.condition([entry]) for entry in body)
            elif name == 'has_country_flag':
                result = body in self.countries[self.current]['flags']
            elif name == 'has_event_target':
                result = body in self.targets
            elif name == 'has_variable':
                result = (body[7:] in self.global_vars if body.startswith('global.')
                          else body in self.countries[self.current]['vars'])
            elif name == 'is_ai':
                result = body == 'yes' and False or body == 'no'
            elif name == 'check_variable':
                fields = dict(body)
                if 'var' in fields:
                    left, right = self.number(fields['var']), self.number(fields['value'])
                    op = fields['compare']
                elif body and isinstance(body[0][1], tuple):
                    left, (op, right_token) = self.number(body[0][0]), body[0][1]
                    right = self.number(right_token)
                else:
                    left, right, op = self.number(body[0][0]), self.number(body[0][1]), '='
                result = {'<': left < right, '>': left > right, '=': left == right,
                          'greater_than_or_equals': left >= right,
                          'less_than_or_equals': left <= right}.get(op, False)
            elif name == 'equipment_from_heavens_country_is_valid_recipient':
                country = self.countries[self.current]
                result = country['valid'] and 'efh_chain_active' not in country['flags']
            elif name == 'equipment_from_heavens_has_any_valid_recipient':
                result = any(c['valid'] and 'efh_chain_active' not in c['flags'] for c in self.countries.values())
            elif name in ('equipment_from_heavens_stage_i_active', 'equipment_from_heavens_stage_ii_active',
                          'equipment_from_heavens_stage_iii_active', 'is_current_evolution_enabled'):
                result = False
            else:
                raise AssertionError(f'Unsupported entry condition: {name}')
        return result

    def call(self, name):
        before = set(self.temp)
        self.execute(EFFECTS[name])
        for key in set(self.temp) - before:
            del self.temp[key]

    def execute(self, nodes):
        chain_taken = None
        for name, body in nodes:
            if name == 'if':
                passed = self.condition(get(body, 'limit'))
                chain_taken = passed
                if passed:
                    self.execute([(k, v) for k, v in body if k != 'limit'])
            elif name == 'else_if':
                passed = False if chain_taken else self.condition(get(body, 'limit'))
                chain_taken = bool(chain_taken or passed)
                if passed:
                    self.execute([(k, v) for k, v in body if k != 'limit'])
            elif name == 'else':
                if chain_taken is False:
                    self.execute(body)
                chain_taken = None
            elif name == 'set_country_flag':
                self.countries[self.current]['flags'].add(body)
            elif name == 'clr_country_flag':
                self.countries[self.current]['flags'].discard(body)
            elif name == 'set_variable' or name == 'set_temp_variable':
                self.set_value(body[0][0], body[0][1], name == 'set_temp_variable')
            elif name == 'add_to_variable' or name == 'add_to_temp_variable':
                key, token = body[0]
                target = self.temp if name == 'add_to_temp_variable' else self.countries[self.current]['vars']
                if key.startswith('global.'):
                    self.global_vars[key[7:]] = self.number(key) + self.number(token)
                else:
                    target[key] = self.number(key) + self.number(token)
            elif name == 'clear_variable':
                self.countries[self.current]['vars'].pop(body, None)
            elif name == 'clear_array':
                self.countries[self.current]['vars'][body] = []
            elif name == 'clear_temp_array':
                self.temp_arrays[body] = []
            elif name == 'add_to_temp_array':
                array, value = body[0]
                self.temp_arrays.setdefault(array, []).append(self.current if value == 'THIS' else self.number(value))
            elif name == 'every_country':
                old = self.current
                for tag, country in self.countries.items():
                    self.current = tag
                    if self.condition(get(body, 'limit')):
                        self.execute([(k, v) for k, v in body if k != 'limit'])
                self.current = old
            elif name == 'random_scope_in_array':
                fields = dict(body)
                candidates = self.temp_arrays.get(fields['array'], [])
                if candidates:
                    old = self.current
                    self.current = candidates[0]
                    self.execute([(k, v) for k, v in body if k not in ('array',)])
                    self.current = old
            elif name == 'save_event_target_as':
                self.targets[body] = self.current
            elif name == 'event_target:efh_prefire_recipient':
                old = self.current
                self.current = self.targets.get('efh_prefire_recipient', old)
                if self.current != old:
                    self.execute(body)
                self.current = old
            elif name == 'equipment_from_heavens_enter_delivery':
                self.call(name)
            elif name == 'equipment_from_heavens_prepare_random_event_fire':
                self.call(name)
            elif name == 'equipment_from_heavens_open_delivery':
                self.call_open_delivery()
            elif name == 'equipment_from_heavens_resolve_active_stage':
                self.call(name)
            elif name == 'equipment_from_heavens_grant_manifest':
                self.grants += 1
                self.manifest_manual[self.current] = 'efh_manifest_manual' in self.countries[self.current]['flags']
            elif name == 'country_event':
                event_id = dict(body)['id']
                if event_id == 'chaosx.nr42.1':
                    self.queue.append((event_id, self.current))
                elif event_id == 'chaosx.nr42.2':
                    self.visible.append(event_id)
                elif event_id == 'chaosx.nr42.18':
                    self.unavailable += 1
            elif name in EFFECTS:
                # Gameplay constructors and unrelated package hooks are
                # intentionally stubbed. The entry, prepare, open, stage, and
                # grant transaction calls above execute or record actual source.
                continue
            elif name.startswith('equipment_from_heavens_'):
                # Effects in the achievement and special files are outside
                # this bounded entry proof. They do not alter manual flags or
                # issue the conventional grant transaction.
                continue
            elif name in ('has_country_flag', 'NOT', 'OR', 'AND'):
                continue
            else:
                raise AssertionError(f'Unsupported entry effect command: {name} = {body}')

    def fire_root(self, tag):
        self.current = tag
        self.execute(get(EVENTS['chaosx.nr42.1'], 'immediate'))
        steps = 0
        while self.queue:
            if steps > 4:
                raise AssertionError('Entry reroute did not settle')
            steps += 1
            event_id, tag = self.queue.pop(0)
            self.current = tag
            self.execute(get(EVENTS[event_id], 'immediate'))
        return self

    def call_open_delivery(self):
        """Execute the source-owned provenance transfer, stub the grant body."""
        body = EFFECTS['equipment_from_heavens_open_delivery']
        stop = next(i for i, (name, _) in enumerate(body)
                    if name == 'set_temp_variable' and dict(body[i][1]).get('efh_active_stage') == '0')
        before = set(self.temp)
        self.execute(body[:stop])
        for key in set(self.temp) - before:
            del self.temp[key]
        # One invocation of the source open helper reaches one manifest grant
        # call. The manifest builder and physical stockpile rows are stubs.
        self.grants += sum(name == 'equipment_from_heavens_grant_manifest'
                           for name, _ in descendants(body))
        self.manifest_manual[self.current] = 'efh_manifest_manual' in self.countries[self.current]['flags']


class RecoveryModel:
    """Conservative scripted-effect temp lifetime plus saved country state."""

    def __init__(self, count, themes=None, valid_states=None, saved_states=None):
        self.flags = {'efh_chain_active'}
        self.vars = {
            'efh_report_next_index': 0,
            'efh_report_theme_entries': list(themes or ['ordinary'] * count),
            'efh_report_day_entries': list(range(1, count + 1)),
            'efh_report_state_entries': list(saved_states or ['A'] * count),
            'efh_recovery_sites_cleared': 0,
        }
        self.valid_states = list(valid_states if valid_states is not None else ['A'])
        self.temp = {}
        self.queue = []
        self.presented = ['chaosx.nr42.2']
        self.modifier_visits = []
        self.accident_losses = []
        self.stockpile = {'fixture_equipment': 37}
        self.event_target_state = None
        self.active_state = None

    def call(self, name):
        before = set(self.temp)
        self.execute(EFFECTS[name])
        # Temporary values born in the helper frame disappear. Only caller
        # initialized storage and its modifications survive the return.
        for key in set(self.temp) - before:
            del self.temp[key]

    def number(self, token):
        if token is None:
            raise AssertionError('Expected a value')
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            return int(token)
        if token.endswith('^num'):
            return len(self.resolve(token[:-4]))
        return self.resolve(token)

    def resolve(self, token):
        if token.startswith('var:'):
            token = token[4:]
        if '^' in token:
            key, index = token.rsplit('^', 1)
            if index == 'num':
                return len(self.vars.get(key, []))
            return self.vars[key][int(self.number(index))]
        if token in self.temp:
            return self.temp[token]
        if token in self.vars:
            return self.vars[token]
        if token in ('yes', 'no'):
            return token == 'yes'
        return token

    def set_value(self, key, value, temporary=False):
        store = self.temp if temporary else self.vars
        if '^' in key:
            name, index = key.rsplit('^', 1)
            index = int(index)
            arr = self.vars.setdefault(name, [])
            while len(arr) <= index:
                arr.append(None)
            arr[index] = self.number(value)
        else:
            store[key] = self.number(value)

    def condition(self, nodes):
        result = True
        for name, body in nodes:
            if not result:
                break
            if name == 'NOT':
                result = result and not self.condition(body)
            elif name == 'OR':
                result = result and any(self.condition([entry]) for entry in body)
            elif name == 'AND':
                result = result and all(self.condition([entry]) for entry in body)
            elif name == 'has_country_flag':
                result = result and body in self.flags
            elif name == 'has_variable':
                result = result and body in self.vars
            elif name == 'is_owned_and_controlled_by':
                result = result and self.active_state in self.valid_states
            elif name == 'equipment_from_heavens_state_is_valid_landing':
                result = result and self.active_state in self.valid_states
            elif name == 'any_owned_state':
                result = result and bool(self.valid_states)
            elif name == 'check_variable':
                fields = dict(body)
                if 'var' in fields:
                    left = self.number(fields['var'])
                    right = self.number(fields['value'])
                    operator = fields['compare']
                elif body and isinstance(body[0][1], tuple):
                    left = self.number(body[0][0])
                    operator, right_token = body[0][1]
                    right = self.number(right_token)
                else:
                    left = self.number(body[0][0])
                    operator = '='
                    right = self.number(body[0][1])
                if operator == '<':
                    ok = left < right
                elif operator == '>':
                    ok = left > right
                elif operator == '=':
                    ok = left == right
                elif operator == 'greater_than_or_equals':
                    ok = left >= right
                elif operator == 'less_than_or_equals':
                    ok = left <= right
                else:
                    raise AssertionError(f'Unknown variable comparison: {operator}')
                result = result and ok
            else:
                raise AssertionError(f'Unsupported condition in recovery model: {name}')
        return result

    def execute(self, nodes, state=None):
        chain_taken = None
        for name, body in nodes:
            if name == 'if':
                passed = self.condition(get(body, 'limit'))
                chain_taken = passed
                if passed:
                    self.execute([(key, value) for key, value in body if key != 'limit'], state)
            elif name == 'else_if':
                passed = False if chain_taken else self.condition(get(body, 'limit'))
                chain_taken = chain_taken or passed
                if passed:
                    self.execute([(key, value) for key, value in body if key != 'limit'], state)
            elif name == 'else':
                if chain_taken is False:
                    self.execute(body, state)
                chain_taken = None
            elif name == 'set_country_flag':
                self.flags.add(body)
            elif name == 'clr_country_flag':
                self.flags.discard(body)
            elif name == 'set_variable':
                key, token = body[0]
                self.set_value(key, token)
            elif name == 'set_temp_variable':
                key, token = body[0]
                self.set_value(key, token, temporary=True)
            elif name == 'add_to_variable':
                key, token = body[0]
                left, right = self.number(key), self.number(token)
                if not isinstance(left, int) or not isinstance(right, int):
                    raise AssertionError(f'Non-numeric persistent increment {key}={left!r} by {token}={right!r}')
                self.vars[key] = left + right
            elif name == 'add_to_temp_variable':
                key, token = body[0]
                self.temp[key] = self.number(key) + self.number(token)
            elif name == 'subtract_from_temp_variable':
                key, token = body[0]
                self.temp[key] = self.number(key) - self.number(token)
            elif name == 'clamp_temp_variable':
                fields = dict(body)
                key = fields['var']
                value = self.number(key)
                if 'min' in fields:
                    value = max(value, self.number(fields['min']))
                if 'max' in fields:
                    value = min(value, self.number(fields['max']))
                self.temp[key] = value
            elif name == 'clear_variable':
                self.vars.pop(body, None)
            elif name == 'clear_array':
                self.vars[body] = []
            elif name == 'country_event':
                fields = dict(body)
                delay = self.number(fields['days']) if 'days' in fields else 0
                self.queue.append((fields['id'], delay))
                if delay == 0 and fields['id'] in ('chaosx.nr42.13', 'chaosx.nr42.16', 'chaosx.nr42.17'):
                    self.presented.append(fields['id'])
            elif name == 'equipment_from_heavens_apply_landing_zone':
                self.modifier_visits.append(state or self.event_target_state)
            elif name == 'equipment_from_heavens_apply_recovery_accident':
                self.accident_losses.append(self.vars.get('efh_report_current_state', state))
            elif name == 'equipment_from_heavens_start_recovery':
                self.call(name)
            elif name == 'equipment_from_heavens_dispatch_next_report':
                self.call(name)
            elif name == 'equipment_from_heavens_fire_visible_report':
                self.call(name)
            elif name == 'equipment_from_heavens_close_chain_if_done':
                self.call(name)
            elif name == 'equipment_from_heavens_cleanup_chain':
                self.call(name)
            elif name == 'equipment_from_heavens_clear_popup_lines':
                for key in list(self.vars):
                    if key.startswith('efh_line_') or key.startswith('efh_special_line_'):
                        del self.vars[key]
            elif name == 'random_owned_state':
                found = next((candidate for candidate in self.valid_states), None)
                if found is not None:
                    self.event_target_state = found
                    previous = self.active_state
                    self.active_state = found
                    self.execute([(key, value) for key, value in body if key != 'limit'], found)
                    self.active_state = previous
            elif name == 'var:efh_report_current_state':
                candidate = self.vars.get('efh_report_current_state')
                if candidate in self.valid_states:
                    self.event_target_state = candidate
                    previous = self.active_state
                    self.active_state = candidate
                    self.execute(body, candidate)
                    self.active_state = previous
            elif name == 'event_target:efh_report_state':
                if self.event_target_state in self.valid_states:
                    self.execute(body, self.event_target_state)
            elif name == 'save_event_target_as':
                if body == 'efh_report_state':
                    self.event_target_state = state
            elif name == 'is_owned_and_controlled_by' or name == 'equipment_from_heavens_state_is_valid_landing':
                # These are evaluated in state limits above; state validity is
                # represented by membership in valid_states.
                continue
            elif name == 'is_owned_and_controlled_by':
                if self.active_state not in self.valid_states:
                    return False
            elif name in ('hidden_effect',):
                self.execute(body, state)
            elif name in ('damage_building', 'add_equipment_to_stockpile'):
                raise AssertionError(f'Unexpected physical grant in recovery flow: {name}')
            elif name in ('equipment_from_heavens_show_report_tooltip', 'custom_effect_tooltip', 'ai_chance', 'name'):
                continue
            elif name in ('title', 'desc', 'picture', 'is_triggered_only', 'hidden', 'trigger', 'option', 'id', 'immediate'):
                continue
            elif name is None:
                continue
            else:
                raise AssertionError(f'Unsupported recovery command: {name} = {body}')

    def run_hidden_report_event(self):
        event = EVENTS['chaosx.nr42.9']
        self.execute(get(event, 'immediate'))

    def run_one_dispatch(self):
        self.run_hidden_report_event()

    def drain_dispatches(self, duplicate_first=False):
        delay = 0
        if duplicate_first:
            self.queue.append(('chaosx.nr42.9', delay))
        turns = 0
        while any(event_id == 'chaosx.nr42.9' for event_id, _ in self.queue):
            if turns > 30:
                raise AssertionError('Recovery dispatch failed to make bounded progress')
            turns += 1
            event_i = next((i for i, (event_id, _) in enumerate(self.queue)
                            if event_id == 'chaosx.nr42.9'), None)
            if event_i is None:
                raise AssertionError('Recovery source failed to queue the next dispatcher')
            self.queue.pop(event_i)
            self.run_one_dispatch()
        return turns

    def click_summary(self, event_id=None):
        final = event_id or self.presented[-1]
        option = get(EVENTS[final], 'option')
        hidden = get(option, 'hidden_effect')
        self.execute(hidden)


class RecoverySourceTests(unittest.TestCase):
    def test_entry_preserves_provenance_through_prepared_and_direct_reroutes(self):
        cases = (
            ('prepared automatic valid', {'A': True}, 'A', True, False, False),
            ('prepared forced valid', {'A': True}, 'A', True, True, True),
            ('prepared automatic rejected', {'A': False, 'B': True}, 'A', True, False, False),
            ('prepared forced rejected', {'A': False, 'B': True}, 'A', True, True, True),
            ('direct unprepared valid', {'A': True}, 'A', False, False, True),
            ('direct unprepared reroute', {'A': False, 'B': True}, 'A', False, False, True),
        )
        for label, pools, original, prepared, forced, expected_manual in cases:
            with self.subTest(label=label):
                model = EntryModel(pools)
                flags = model.countries[original]['flags']
                if prepared:
                    flags.add('efh_prefire_pending')
                    if forced:
                        flags.add('efh_pending_manual')
                model.fire_root(original)
                self.assertEqual(model.grants, 1)
                recipient = original if pools[original] else 'B'
                self.assertEqual(model.manifest_manual.get(recipient), expected_manual)
                self.assertIn('efh_chain_active', model.countries[recipient]['flags'])
                self.assertNotIn('efh_prefire_pending', model.countries[recipient]['flags'])
                self.assertNotIn('efh_pending_manual', model.countries[recipient]['flags'])
                if recipient != original:
                    self.assertNotIn('efh_prefire_pending', flags)
                    self.assertNotIn('efh_pending_manual', flags)
                self.assertEqual(model.visible, ['chaosx.nr42.2'])
                self.assertEqual(model.unavailable, 0)

    def test_direct_empty_pool_clears_markers_and_never_grants(self):
        model = EntryModel({'A': False})
        model.countries['A']['flags'].update({'efh_prefire_pending', 'efh_pending_manual'})
        model.fire_root('A')
        self.assertEqual(model.grants, 0)
        self.assertEqual(model.unavailable, 1)
        self.assertNotIn('efh_prefire_pending', model.countries['A']['flags'])
        self.assertNotIn('efh_pending_manual', model.countries['A']['flags'])
        self.assertEqual(model.visible, [])

    def test_stale_prefire_target_does_not_set_readiness_for_an_empty_pool(self):
        model = EntryModel({'A': False})
        model.current = 'A'
        model.targets['efh_prefire_recipient'] = 'A'
        model.temp['efh_prefire_ready'] = 0
        model.call('equipment_from_heavens_prepare_random_event_fire')
        self.assertEqual(model.temp['efh_prefire_ready'], 0)
        self.assertEqual(model.targets['efh_prefire_recipient'], 'A')
        self.assertEqual(model.grants, 0)

    def test_count_three_through_seven_has_one_summary_and_exact_visits(self):
        for count in range(3, 8):
            for accident in (False, True):
                with self.subTest(count=count, accident=accident):
                    themes = ['ordinary'] * count
                    if accident:
                        themes[count // 2] = 'constant:equipment_from_heavens_report_theme.recovery_accident'
                    model = RecoveryModel(count, themes=themes)
                    model.call('equipment_from_heavens_start_recovery')
                    before = deepcopy(model.stockpile)
                    # Snapshot the persistent schedule exactly as a save/load
                    # would. Arrays, index, accident state, and flags survive.
                    restored = deepcopy(model)
                    restored.drain_dispatches()
                    self.assertEqual(restored.stockpile, before)
                    self.assertEqual(len(restored.modifier_visits), count)
                    self.assertEqual(len(restored.presented), 2)
                    expected = 'chaosx.nr42.16' if accident else 'chaosx.nr42.13'
                    self.assertEqual(restored.presented[-1], expected)
                    restored.click_summary(expected)
                    self.assertNotIn('efh_chain_active', restored.flags)
                    self.assertEqual(restored.vars['efh_report_theme_entries'], [])

    def test_recovery_start_is_idempotent(self):
        model = RecoveryModel(3)
        model.call('equipment_from_heavens_start_recovery')
        queue = list(model.queue)
        model.call('equipment_from_heavens_start_recovery')
        self.assertEqual(model.queue, queue)
        self.assertEqual(sum(event == 'chaosx.nr42.9' for event, _ in model.queue), 1)

    def test_lost_states_fall_back_and_no_valid_state_skips_physical_effects(self):
        lost = RecoveryModel(3, saved_states=['LOST', 'LOST', 'LOST'], valid_states=['SAFE'])
        lost.call('equipment_from_heavens_start_recovery')
        lost.drain_dispatches()
        self.assertEqual(lost.modifier_visits, ['SAFE'] * 3)
        self.assertEqual(lost.presented, ['chaosx.nr42.2', 'chaosx.nr42.13'])
        self.assertEqual(lost.vars['efh_recovery_sites_cleared'], 3)

        none = RecoveryModel(3, saved_states=['LOST'] * 3, valid_states=[])
        none.call('equipment_from_heavens_start_recovery')
        none.drain_dispatches()
        self.assertEqual(none.modifier_visits, [])
        self.assertEqual(none.presented, ['chaosx.nr42.2', 'chaosx.nr42.17'])

    def test_losing_all_landing_grounds_mid_chain_halts_without_false_summary(self):
        model = RecoveryModel(3, valid_states=['SAFE'])
        model.call('equipment_from_heavens_start_recovery')
        first = next(i for i, (event_id, _) in enumerate(model.queue) if event_id == 'chaosx.nr42.9')
        model.queue.pop(first)
        model.run_one_dispatch()
        model.valid_states.clear()
        model.drain_dispatches()
        self.assertEqual(model.vars['efh_recovery_sites_cleared'], 1)
        self.assertEqual(len(model.modifier_visits), 1)
        self.assertEqual(model.presented, ['chaosx.nr42.2', 'chaosx.nr42.17'])

    def test_hazard_is_aggregated_to_accident_summary(self):
        themes = ['ordinary', 'constant:equipment_from_heavens_report_theme.recovery_accident', 'ordinary']
        model = RecoveryModel(3, themes=themes)
        model.call('equipment_from_heavens_start_recovery')
        model.drain_dispatches()
        self.assertIn('efh_recovery_accident', model.flags)
        self.assertEqual(model.presented, ['chaosx.nr42.2', 'chaosx.nr42.16'])
        self.assertEqual(len(model.accident_losses), 1)

    def test_duplicate_dispatch_after_close_is_inert(self):
        model = RecoveryModel(3)
        model.call('equipment_from_heavens_start_recovery')
        model.drain_dispatches()
        model.click_summary()
        before = (list(model.presented), list(model.modifier_visits), deepcopy(model.stockpile))
        model.run_one_dispatch()
        self.assertEqual((model.presented, model.modifier_visits, model.stockpile), before)

    def test_duplicate_pulse_preserves_indexed_visits_and_single_final_event(self):
        model = RecoveryModel(4)
        model.call('equipment_from_heavens_start_recovery')
        model.drain_dispatches(duplicate_first=True)
        self.assertEqual(model.vars['efh_report_next_index'], 4)
        self.assertEqual(len(model.modifier_visits), 4)
        self.assertEqual(len(model.presented), 2)
        self.assertEqual(model.stockpile['fixture_equipment'], 37)

    def test_source_has_one_delivery_grant_call_and_recovery_never_grants(self):
        entry = EFFECTS['equipment_from_heavens_enter_delivery']
        self.assertEqual([body for name, body in descendants(entry)
                          if name == 'equipment_from_heavens_open_delivery'], ['yes'])
        opening = EFFECTS['equipment_from_heavens_open_delivery']
        self.assertEqual(entries(opening, 'equipment_from_heavens_grant_manifest'), ['yes'])
        # The bounded interpreter rejects stockpile effects while dispatching,
        # and every count test above traverses the actual parsed recovery source.

    def test_family_profile_outputs_are_initialized_at_each_call(self):
        callers = (
            ('equipment_from_heavens_build_manifest', 'equipment_from_heavens_load_family_profile'),
            ('equipment_from_heavens_compute_family_entry', 'equipment_from_heavens_load_family_profile'),
            ('equipment_from_heavens_reroll_failed_row', 'equipment_from_heavens_load_family_profile'),
        )
        profile_outputs = ('efh_profile_min_stage', 'efh_profile_max_tier', 'efh_profile_group',
                           'efh_profile_qclass', 'efh_profile_designer', 'efh_profile_mismatch')
        for owner, helper in callers:
            body = EFFECTS[owner]
            found = 0

            def visit(nodes):
                nonlocal found
                initialized = set()
                for name, value in nodes:
                    if name == 'set_temp_variable' and isinstance(value, list):
                        initialized.update(dict(value).keys())
                    if name == helper:
                        found += 1
                        self.assertEqual(value, 'yes')
                        outputs = (('efh_entry_tier', 'efh_entry_amount') if helper == 'equipment_from_heavens_compute_family_entry'
                                   else profile_outputs)
                        for output in outputs:
                            self.assertIn(output, initialized,
                                          f'{owner} lacks caller storage for {output}')
                    if isinstance(value, list):
                        visit(value)

            visit(body)
            self.assertGreater(found, 0, f'{owner} has no {helper} call')


if __name__ == '__main__':
    unittest.main()
