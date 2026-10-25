"""Bounded actual-source Event 032 clocks, not native MTTH/whole logger proof.

Run: python -B .tools/tests/test_event32_native_evolution.py
Reuse the operator-preserving CBRN parser and conservative helper/meta frames.
World facts and native country_event enqueueing are explicit leaves. The shared
record_events_log_evolution_entry call is a declared boundary: capture its input
only, never invent its success or execute its history/UI closure. Event .8
dispatch is captured, not country adoption execution. Authorization, pressure
arithmetic, shared chemical affordability, clocks, record acknowledgement and
date conversion execute production bodies. Unknown commands fail closed.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import operator
import unittest

from test_cbrn_payload_reservations import (
    D, ZERO, Node, Frame, Scope, Source, Machine, parse, item,
)

ROOT_DIR = Path(__file__).resolve().parents[2]
# Evaluation order differs from catalog order.
TRACKS = (
    ('rogue_launch_commands', 'rogue_commands', 'rogue', 4, 201, 120),
    ('unreliable_guidance', 'unreliable_guidance', 'guidance', 2, 202, 105),
    ('saturation', 'saturation', 'saturation', 1, 203, 90),
    ('special_warheads', 'special_warheads', 'special', 3, 204, 120),
    ('automatic_retaliation', 'automatic_retaliation', 'retaliation', 5, 205, 150),
)


def walk(nodes):
    for n in nodes:
        yield n
        if isinstance(n.value, list):
            yield from walk(n.value)


class EvolutionSource(Source):
    def __init__(self):
        super().__init__()  # Real shared CBRN predicates and owning receipts.
        self.mtth, self.events, self.event_locals = {}, {}, {}
        for path, dest, selected in (
            ('common/scripted_effects/032_missiles_operations_effects.txt', self.effects, None),
            ('common/scripted_effects/032_missiles_effects.txt', self.effects, None),
            ('common/scripted_effects/032_missiles_evolution_effects.txt', self.effects, None),
            ('common/scripted_effects/032_missiles_achievement_effects.txt', self.effects,
             {'chaosx_032_achievement_initialize_country'}),
            ('common/scripted_effects/chaosx_dynamic_effects.txt', self.effects,
             {'chaosx_convert_days_to_date_offset', 'chaosx_convert_date_offset_to_days'}),
            ('common/scripted_triggers/032_missiles_evolution_triggers.txt', self.triggers, None),
            ('common/scripted_triggers/chaosx_settings_triggers.txt', self.triggers,
             {'is_current_evolution_enabled', 'has_disabled_current_evolution',
              'has_reached_current_evolution_tier'}),
            ('common/mtth/032_missiles_evolution_mtth.txt', self.mtth, None),
        ):
            self.load(path, dest, selected)
        for path in ('common/script_constants/chaos_meter_constants.txt',
                     'common/script_constants/chaosx_date_units_constants.txt'):
            nodes = self.read(path)
            def flatten(prefix, children):
                for n in children:
                    if n.key == 'schema':
                        continue
                    if isinstance(n.value, list):
                        flatten(f'{prefix}.{n.key}', n.value)
                    else:
                        self.constants[f'{prefix}.{n.key}'] = D(n.value)
            for n in nodes:
                flatten(n.key, n.value)
        for path in ('events/032_missile_crisis.txt', 'events/032_missiles_evolution_events.txt'):
            nodes = self.read(path)
            local = {n.key: n.value for n in nodes if n.key.startswith('@')}
            for n in nodes:
                if n.key == 'country_event':
                    event_id = item(n.value, 'id')
                    if event_id in self.events:
                        raise AssertionError(f'Duplicate event {event_id}')
                    self.events[event_id] = n.value
                    self.event_locals[event_id] = local
        hooks = self.read('common/on_actions/032_missiles_on_actions.txt')
        state_control = item(item(hooks, 'on_actions'), 'on_state_control_changed')
        # Execute only the actual notification if/limit/body. The separate
        # preceding capture handler is outside this predicate regression.
        notifications = [n for n in item(state_control, 'effect') if n.key == 'if'
                         and any(c.key == 'missiles_notify_evolution_change' for c in n.value)]
        if len(notifications) != 1:
            raise AssertionError('Expected one state-control notification block')
        self.state_control_notification = notifications[0]

    def read(self, path):
        raw = (ROOT_DIR / path).read_bytes()
        self.hashes[path] = sha256(raw).hexdigest()
        return parse(raw.decode('utf-8-sig'))

    def load(self, path, destination, selected=None):
        nodes = self.read(path)
        local = {n.key: n.value for n in nodes if n.key.startswith('@')}
        for n in nodes:
            if isinstance(n.value, list) and (selected is None or n.key in selected):
                destination[n.key] = (n.value, local, path, n.line)


class EvolutionMachine(Machine):
    def __init__(self, source, actor):
        super().__init__(source, actor)
        self.world = Scope('global', -1, 'global')
        self.flag_values = {}
        self.deliveries, self.log_inputs = [], []

    def scope(self, token):
        if token in ('FROM', 'FROM.FROM'):
            target = getattr(self, 'callback_former' if token == 'FROM' else 'callback_state', None)
            if not isinstance(target, Scope):
                raise AssertionError(f'Missing explicit native callback scope {token}')
            return target
        return super().scope(token)

    def storage(self, token):
        if token.startswith('global.'):
            return self.world, token[7:]
        return self.current, self.targeted(token)

    def value(self, token):
        if isinstance(token, str) and token.startswith('global.'):
            return self.world.variables.get(token[7:], ZERO)
        if isinstance(token, str) and token.startswith('mtth:'):
            return self.mtth_value(token[5:])
        if token in ('THIS', 'ROOT', 'PREV'):
            return self.scope(token)
        return super().value(token)

    def has_variable(self, token):
        if token.startswith('global.'):
            return token[7:] in self.world.variables
        return super().has_variable(token)

    def rows(self, token):
        if token.startswith('global.'):
            return self.world.arrays.get(token[7:], [])
        owner = self.temp_owner(token, True)
        return (self.current.arrays if owner is None else owner).get(token, [])

    def predicate(self, n):
        k, v = n.key, n.value
        if k in ('FROM', 'FROM.FROM'):
            return self.enter(self.scope(k), v, True)
        if k == 'num_of_controlled_states':
            if self.current.kind != 'country' or not hasattr(self.current, 'native_controlled_states'):
                raise AssertionError('Missing native COUNTRY controlled-state count')
            return {'<': operator.lt, '>': operator.gt, '=': operator.eq}[n.op](
                self.current.native_controlled_states, self.value(v))
        if k == 'has_global_flag' and isinstance(v, list):
            flag = item(v, 'flag')
            return flag in self.global_flags and (item(v, 'value') is None or
                self.flag_values.get(flag, ZERO) == self.value(item(v, 'value')))
        if k in ('any_owned_state', 'any_controlled_state', 'any_of_scopes'):
            rows = self.rows(item(v, 'array')) if k == 'any_of_scopes' else getattr(self.current, k[4:], [])
            body = [c for c in v if c.key != 'array']
            return any(self.enter(s, body, True) for s in list(rows))
        if k in ('has_wargoal_against', 'is_justifying_wargoal_against', 'is_in_faction_with'):
            field = {'has_wargoal_against': 'wargoals', 'is_justifying_wargoal_against': 'justifications',
                     'is_in_faction_with': 'allies'}[k]
            return self.scope(v) in getattr(self.current, field, set())
        if k == 'is_subject_of':
            return getattr(self.current, 'overlord', None) is self.scope(v)
        if k == 'has_civil_war':
            return getattr(self.current, 'civil_war', False) == (v == 'yes')
        if k == 'has_stability':
            return {'<': operator.lt, '>': operator.gt, '=': operator.eq}[n.op](
                getattr(self.current, 'stability', D(1)), self.value(v))
        return super().predicate(n)

    def meta(self, nodes, trigger=False):
        # Shared Event Log toggle constructor uses |0, equivalent here to |.0.
        nodes = [Node(n.key, n.op, n.value.replace('|0]', '|.0]')
                      if isinstance(n.value, str) else n.value, n.line) for n in nodes]
        return super().meta(nodes, trigger)

    def call(self, name, trigger=False):
        if name == 'record_events_log_evolution_entry' and not trigger:
            self.calls[name] += 1
            self.log_inputs.append(tuple(self.value(f'events_log_evolution_{key}')
                                         for key in ('event_id', 'type', 'stage', 'tier', 'has_actor')))
            return None  # No synthetic success output or native logger claim.
        return super().call(name, trigger)

    def mtth_value(self, name):
        body = self.source.mtth[name][0]
        result = self.value(item(body, 'base'))
        for n in body:
            if n.key == 'modifier' and self.condition([c for c in n.value if c.key not in ('factor', 'add')]):
                result *= self.value(item(n.value, 'factor', '1'))
                result += self.value(item(n.value, 'add', '0'))
        return result

    def execute(self, nodes):
        # Keep base interpreter branch order, scope stack and conservative frames.
        taken = None
        for n in nodes:
            k, v = n.key, n.value
            if k in ('if', 'else_if', 'else'):
                if k == 'if':
                    taken = False
                elif taken is None:
                    raise AssertionError('Orphan else')
                if not taken and (k == 'else' or self.condition(item(v, 'limit', []))):
                    taken = True
                    self.execute([c for c in v if c.key != 'limit'])
                continue
            taken = None
            if k in ('set_global_flag', 'clr_global_flag'):
                if not isinstance(v, str):
                    self.unmodeled(n)
                (self.global_flags.add if k.startswith('set') else self.global_flags.discard)(v)
            elif k in ('set_variable', 'add_to_variable', 'subtract_from_variable', 'multiply_variable',
                       'divide_variable', 'divide_temp_variable', 'clamp_temp_variable', 'clear_variable'):
                if k == 'clear_variable':
                    target, key = self.storage(v)
                    target.variables.pop(key, None)
                    continue
                key = item(v, 'var', v[0].key)
                target, stored = self.storage(key)
                temporary = 'temp_variable' in k
                old = self.value(key) if temporary else target.variables.get(stored, ZERO)
                if k == 'clamp_temp_variable':
                    result = old
                    for bound, function in (('min', max), ('max', min)):
                        if item(v, bound) is not None:
                            result = function(result, self.value(item(v, bound)))
                else:
                    val = self.value(item(v, 'value', v[0].value))
                    if k.startswith('set'):
                        result = val
                    elif k.startswith('add'):
                        result = old + val
                    elif k.startswith('subtract'):
                        result = old - val
                    elif k.startswith('multiply'):
                        result = old * val
                    else:
                        if k == 'divide_variable' and item(v, 'if_zero') is not None:
                            raise AssertionError('Unsupported regular divide_variable if_zero')
                        if k == 'divide_variable' and val == ZERO:
                            raise AssertionError('Regular division reached an unguarded zero denominator')
                        result = old / val if val != ZERO else self.value(item(v, 'if_zero', '0'))
                if temporary:
                    self.temp(key, result)
                else:
                    target.variables[stored] = result
            elif k == 'for_each_scope_loop':
                rows = list(self.rows(item(v, 'array')))
                body = [c for c in v if c.key not in ('array', 'break', 'tooltip')]
                for scope in rows:
                    self.enter(scope, body)
                    if self.value(item(v, 'break', 'break')) != ZERO:
                        break  # No fixture reset that could hide inherited breaks.
            elif k == 'country_event':
                allowed = {'id', 'days', 'hours'}
                if {c.key for c in v} - allowed or self.current.kind != 'country':
                    self.unmodeled(n)
                days = self.value(item(v, 'days', '0')) + self.value(item(v, 'hours', '0')) / D(24)
                self.deliveries.append((self.current, item(v, 'id'), days, self.value('global.date')))
            elif k == 'record_events_log_evolution_entry':
                if v != 'yes':
                    self.unmodeled(n)
                self.call(k)
            else:
                super().execute([n])

    def deliver(self, event_id, actor=None):
        """Execute actual immediate body in a fresh recipient-rooted context."""
        self.current = self.root = actor or self.current
        self.frames = [Frame()]
        self.locals.append(self.source.event_locals[event_id])
        try:
            self.execute(item(self.source.events[event_id], 'immediate'))
        finally:
            self.locals.pop()


SOURCE = None


def source():
    global SOURCE
    if SOURCE is None:
        SOURCE = EvolutionSource()
    return SOURCE


class NativeEvolutionTests(unittest.TestCase):
    def setUp(self):
        self.s = source()
        self.a, self.b, self.c = [Scope(name, i) for name, i in (('A', 11), ('B', 22), ('C', 33))]
        self.m = EvolutionMachine(self.s, self.a)
        self.m.world.variables.update(date=D(10), chaos_meter_value=D(950))
        self.m.world.arrays['missiles_program_registry'] = [self.a, self.b]
        self.m.global_flags.update({'missiles_program_ever_initialized', 'missiles_evolution_observing'})
        for country in (self.a, self.b, self.c):
            country.flags.add('missiles_program_initialized')
            country.variables.update(missiles_program_stage=self.s.constant('missiles_stage.advanced'),
                missiles_operational_reserve=D(100), missiles_launch_readiness=D(40),
                missiles_command_control=D(90), missiles_total_site_capacity=D(200))
            site = Scope(f'{country.name}_site', country.identity + 100, 'state', controller=country)
            site.flags.update({'missiles_site_active', 'missiles_site_hardened'})
            country.owned_state = country.controlled_state = [site]
            country.arrays['missiles_launch_site_states'] = [site]
        self.a.wars.add(self.b)
        self.b.wars.add(self.a)
        self.a.flags.add('missiles_code_compromise_active')
        self.a.techs.update({'atomic_research', 'nukes'})
        self.a.variables['num_of_nukes'] = D(1)
        self.m.temp('break', D(1))

    def offset(self, days):
        return D(days) * self.s.constant('chaosx_date_units.hours_per_day') / self.s.constant('chaosx_date_units.hours_per_date_unit')

    def g(self, key):
        return self.m.world.variables[key]

    def pulse(self, ordinary=False):
        if ordinary:
            self.m.global_flags.add('missiles_evolution_first_pulse_done')
        self.m.call('missiles_evaluate_evolution_unlocks')

    def select(self, track):
        self.m.temp('missiles_evolution_selection', self.s.constant(f'missiles_evolution.{track[1]}'))

    def test_durable_counts_private_breaks_and_repeat_observation(self):
        self.c.variables['missiles_program_stage'] = self.s.constant('missiles_stage.complete')
        self.b.variables['missiles_operational_reserve'] = ZERO
        self.m.world.arrays['missiles_program_registry'].append(self.c)
        for name in ('missiles_pressure_program_loop_break', 'missiles_pressure_pair_outer_break',
                     'missiles_pressure_pair_inner_break'):
            self.m.temp(name, D(1))
        for generation in (1, 2):
            self.m.call('missiles_measure_evolution_pressure')
            for key, expected in (('programs', 3), ('operational', 3), ('mature', 1),
                                  ('responders', 2), ('war', 2), ('hostile_pairs', 1), ('reserve', 200)):
                self.assertEqual(self.g(f'missiles_pressure_{key}'), D(expected), key)
            self.assertEqual(self.g('missiles_pressure_observation_generation'), D(generation))
            self.assertIsNone(self.m.temp_owner('missiles_pressure_operational_pool', True))
            self.assertIn('missiles_pressure_observation_ready', self.m.global_flags)
        self.assertEqual(self.m.value('break'), D(1))

    def test_empty_registry_observation_cannot_arm_or_choose_host(self):
        self.m.world.arrays['missiles_program_registry'] = []
        self.pulse(ordinary=True)
        self.assertEqual(self.g('missiles_pressure_programs'), ZERO)
        self.assertEqual(self.g('missiles_pressure_operational'), ZERO)
        self.assertEqual(self.g('missiles_pressure_responders'), ZERO)
        self.assertEqual(self.g('missiles_pressure_operational_share'), ZERO)
        self.assertEqual(self.g('missiles_pressure_unmaintained_share'), ZERO)
        divisions = [n for n in walk(self.s.effects['missiles_measure_evolution_pressure'][0])
                     if n.key == 'divide_variable']
        self.assertEqual(len(divisions), 2)
        self.assertTrue(all(item(n.value, 'if_zero') is None for n in divisions))
        self.assertNotIn('missiles_evolution_host_id', self.m.world.variables)
        self.assertEqual(self.m.deliveries, [])
        self.assertFalse(any(f.endswith(('_native_pending', '_short_pending')) for f in self.m.global_flags))

    def test_hostile_pairs_are_unordered_and_response_capability_is_separate(self):
        for responders, opponents, expected in ((2, 1, 1), (1, 2, 2)):
            with self.subTest(responders=responders, opponents=opponents):
                self.setUp()
                self.b.variables['missiles_operational_reserve'] = D(100 if responders == 2 else 0)
                if opponents == 2:
                    self.m.world.arrays['missiles_program_registry'].append(self.c)
                    self.c.variables['missiles_operational_reserve'] = ZERO
                    self.a.wars.add(self.c)
                    self.c.wars.add(self.a)
                self.m.call('missiles_measure_evolution_pressure')
                self.assertEqual(self.g('missiles_pressure_hostile_pairs'), D(expected))
                self.assertEqual(self.g('missiles_pressure_responders'), D(responders))
        # Detailed spec permits one neutral responder beside a hostile OP pair.
        self.setUp()
        self.m.world.arrays['missiles_program_registry'].append(self.c)
        self.a.variables['missiles_operational_reserve'] = ZERO
        self.b.variables['missiles_operational_reserve'] = ZERO
        self.m.call('missiles_measure_evolution_pressure')
        self.assertEqual(self.g('missiles_pressure_responders'), D(1))
        self.assertEqual(self.g('missiles_pressure_hostile_pairs'), D(1))
        self.assertTrue(self.m.call('missiles_evolution_automatic_retaliation_is_eligible', True))

    def test_pair_hostility_direction_and_peacetime_ties(self):
        for signal in ('war', 'wargoals', 'justifications'):
            for reverse in (False, True):
                for tie in ('none', 'ally', 'subject_a', 'subject_b'):
                    with self.subTest(signal=signal, reverse=reverse, tie=tie):
                        self.setUp()
                        self.a.wars.clear()
                        self.b.wars.clear()
                        sender, target = (self.b, self.a) if reverse else (self.a, self.b)
                        if signal == 'war':
                            sender.wars.add(target)
                            target.wars.add(sender)  # Native war is symmetric.
                        else:
                            setattr(sender, signal, {target})
                        if tie == 'ally':
                            self.a.allies, self.b.allies = {self.b}, {self.a}
                        elif tie == 'subject_a':
                            self.a.overlord = self.b
                        elif tie == 'subject_b':
                            self.b.overlord = self.a
                        self.m.call('missiles_measure_evolution_pressure')
                        self.assertEqual(self.g('missiles_pressure_hostile_pairs'), D(signal == 'war' or tie == 'none'))
        self.setUp()
        self.a.wars.clear()
        self.b.wars.clear()
        self.m.call('missiles_measure_evolution_pressure')
        self.assertEqual(self.g('missiles_pressure_hostile_pairs'), ZERO)

    def test_actual_shared_chemical_affordability_not_profile_token(self):
        self.a.techs = {'chemical_air_interdiction', 'chlorine_gas'}
        self.a.variables['cbrn_air_payload_agent'] = self.s.constant('cbrn_agent.chlorine')
        cost = self.s.constant('cbrn_payload_route_cost.strategic_chemical_raid')
        for balance in (ZERO, cost - 1, cost, cost + 1):
            with self.subTest(stock=balance):
                self.a.stocks['choking_chemical_air_payload_lot_1'] = balance
                self.m.call('missiles_measure_evolution_pressure')
                self.assertEqual(self.g('missiles_pressure_payload_owners'), D(balance >= cost))
                self.assertEqual(self.a.stocks['choking_chemical_air_payload_lot_1'], balance)
        self.assertGreater(self.m.calls['cbrn_air_payload_can_fund_strategic_action'], 0)
        self.assertGreater(self.m.calls['cbrn_action_payload_stock_is_sufficient'], 0)

    def test_stage_and_surviving_site_requirements_are_actual_predicates(self):
        self.a.variables['missiles_program_stage'] = self.s.constant('missiles_stage.experimental')
        self.b.variables['missiles_program_stage'] = self.s.constant('missiles_stage.complete')
        self.m.call('missiles_measure_evolution_pressure')
        self.assertEqual(self.g('missiles_pressure_operational'), D(1))
        self.assertEqual(self.g('missiles_pressure_mature'), D(1))
        self.assertEqual(self.g('missiles_pressure_responders'), D(1))
        self.b.controlled_state[0].flags.add('missiles_site_damaged_beyond_use')
        self.m.call('missiles_measure_evolution_pressure')
        self.assertEqual(self.g('missiles_pressure_programs'), D(2))
        self.assertEqual(self.g('missiles_pressure_operational'), ZERO)
        self.assertEqual(self.g('missiles_pressure_mature'), D(1))
        self.assertEqual(self.g('missiles_pressure_responders'), ZERO)
        self.assertEqual(self.g('missiles_pressure_operational_share'), ZERO)
        self.assertEqual(self.g('missiles_pressure_unmaintained_share'), ZERO)

    def test_first_fire_dates_and_earliest_job_coalescing(self):
        self.pulse()
        for i, track in enumerate(TRACKS):
            key = f'missiles_evolution_{track[0]}'
            self.assertEqual(self.g(f'{key}_due_date'), D(10) + self.offset(21 + 14 * i))
            self.assertIn(f'{key}_short_pending', self.m.global_flags)
            self.assertNotIn(f'{key}_native_pending', self.m.global_flags)
            self.assertFalse(self.m.condition(item(self.s.events[f'chaosx.nr32.{track[4]}'], 'trigger')))
        jobs = [x for x in self.m.deliveries if x[1] == 'chaosx.nr32.190']
        self.assertEqual([x[2] for x in jobs], [D(21)])
        self.m.deliver('chaosx.nr32.190')  # Early/manual callback retains work.
        self.assertEqual(self.m.log_inputs, [])
        self.assertIn('missiles_evolution_short_job_queued', self.m.global_flags)
        for days, new_count in ((40, 1), (21, 1), (7, 2), (9, 2)):
            self.m.temp('missiles_evolution_job_days', D(days))
            self.m.call('missiles_queue_evolution_job')
            self.assertEqual(sum(x[1] == 'chaosx.nr32.190' for x in self.m.deliveries), new_count)
        self.assertEqual(self.g('missiles_evolution_short_job_due_date'), D(10) + self.offset(7))

    def test_unchanged_numeric_stamp_refresh_schedules_nothing(self):
        self.pulse(ordinary=True)  # Production normalization creates the stamp.
        self.m.global_flags.discard('missiles_evolution_observing')
        self.assertIn('missiles_evolution_numbers_known', self.a.flags)
        stamp = {k: v for k, v in self.a.variables.items() if k.startswith('missiles_evolution_noted_')}
        self.assertEqual(len(stamp), 8)
        notifications = self.m.calls['missiles_notify_evolution_change']
        generation = self.g('missiles_pressure_observation_generation')
        for _ in range(3):
            self.m.call('missiles_notify_program_numbers_changed')
        self.assertEqual(self.m.calls['missiles_notify_evolution_change'], notifications)
        self.assertEqual(self.m.deliveries, [])
        self.assertEqual(self.g('missiles_pressure_observation_generation'), generation)
        self.assertEqual({k: v for k, v in self.a.variables.items()
                          if k.startswith('missiles_evolution_noted_')}, stamp)

    def test_material_number_change_queues_exactly_one_observation(self):
        for field in ('program_stage', 'operational_reserve', 'launch_readiness', 'command_control',
                      'active_site_count', 'total_site_capacity', 'launch_site_count', 'active_site_region_count'):
            with self.subTest(field=field):
                self.setUp()
                self.pulse(ordinary=True)
                self.m.global_flags.discard('missiles_evolution_observing')
                generation = self.g('missiles_pressure_observation_generation')
                key = f'missiles_{field}'
                self.a.variables[key] = self.a.variables.get(key, ZERO) + D(1)
                self.m.call('missiles_notify_program_numbers_changed')
                self.m.call('missiles_notify_program_numbers_changed')
                self.assertEqual(self.a.variables[f'missiles_evolution_noted_{field}'], self.a.variables[key])
                self.assertEqual([x[1] for x in self.m.deliveries], ['chaosx.nr32.192'])
                self.assertEqual(self.g('missiles_pressure_observation_generation'), generation)
                self.m.deliver('chaosx.nr32.192', self.a)
                self.assertEqual(self.g('missiles_pressure_observation_generation'), generation + D(1))
                self.assertNotIn('missiles_evolution_observation_queued', self.m.global_flags)
                self.assertEqual([x[1] for x in self.m.deliveries], ['chaosx.nr32.192'])
                self.assertEqual(self.m.log_inputs, [])

    def test_chaos_threshold_edges_queue_one_pulse_and_same_band_none(self):
        self.assertEqual(self.s.constant('missiles_evolution_pressure.minimum_chaos_retaliation'), D(900))
        for before, after, expected in ((899, 900, 1), (899, 898, 0), (900, 899, 1)):
            with self.subTest(before=before, after=after):
                self.setUp()
                self.m.world.variables['chaos_meter_value'] = D(before)
                self.pulse(ordinary=True)
                # Seed the persistent band through its real helper while the
                # enclosing observation suppresses notification recursion.
                self.m.call('missiles_note_chaos_threshold_change')
                band = self.g('missiles_evolution_observed_chaos_band')
                generation = self.g('missiles_pressure_observation_generation')
                notifications = self.m.calls['missiles_notify_evolution_change']
                self.m.global_flags.discard('missiles_evolution_observing')
                self.m.world.variables['chaos_meter_value'] = D(after)
                self.m.call('missiles_note_chaos_threshold_change')
                self.m.call('missiles_note_chaos_threshold_change')
                self.assertEqual(self.m.calls['missiles_notify_evolution_change'], notifications + expected)
                self.assertEqual(len(self.m.deliveries), expected)
                self.assertTrue(all(x[1] == 'chaosx.nr32.192' for x in self.m.deliveries))
                self.assertEqual(self.g('missiles_evolution_observed_chaos_band'),
                                 band + D((after > before) - (after < before)) if expected else band)
                self.assertEqual(self.g('missiles_pressure_observation_generation'), generation)
                if expected:
                    self.m.deliver('chaosx.nr32.192', self.a)
                    self.assertEqual(self.g('missiles_pressure_observation_generation'), generation + D(1))
                    self.assertNotIn('missiles_evolution_observation_queued', self.m.global_flags)
                    self.assertEqual(len(self.m.deliveries), 1)
                    self.assertEqual('missiles_evolution_automatic_retaliation_native_pending'
                                     in self.m.global_flags, after >= 900)
                self.assertEqual(self.m.log_inputs, [])
    def test_native_mode_has_no_short_dates_and_repairs_malformed_at_pulse(self):
        self.pulse(ordinary=True)
        for track in TRACKS:
            key = f'missiles_evolution_{track[0]}'
            self.assertIn(f'{key}_native_pending', self.m.global_flags)
            self.assertNotIn(f'{key}_short_pending', self.m.global_flags)
            self.assertNotIn(f'{key}_due_date', self.m.world.variables)
            self.assertTrue(self.m.condition(item(self.s.events[f'chaosx.nr32.{track[4]}'], 'trigger')))
            self.m.global_flags.add(f'{key}_short_pending')
            self.m.world.variables[f'{key}_due_date'] = D(1)
        self.assertEqual(self.m.deliveries, [])
        self.m.deliver('chaosx.nr32.201')
        self.assertEqual(self.m.log_inputs, [])  # Malformed modes cannot commit.
        self.pulse()
        for track in TRACKS:
            self.select(track)
            self.assertTrue(self.m.call('missiles_selected_evolution_has_native_clock', True))
        self.assertEqual(self.m.log_inputs, [])

    def test_malformed_modes_repair_only_on_authorized_observation(self):
        track = TRACKS[0]
        key = f'missiles_evolution_{track[0]}'
        for pending, native, short, dated in ((1, 0, 0, 0), (1, 1, 0, 1),
                                               (1, 0, 1, 0), (1, 1, 1, 1),
                                               (0, 1, 0, 0)):
            with self.subTest(mode=(pending, native, short, dated)):
                self.setUp()
                self.pulse(ordinary=True)
                for suffix, enabled in (('pending', pending), ('native_pending', native), ('short_pending', short)):
                    flag = f'{key}_{suffix}'
                    (self.m.global_flags.add if enabled else self.m.global_flags.discard)(flag)
                if dated:
                    self.m.world.variables[f'{key}_due_date'] = D(1)
                self.select(track)
                self.assertFalse(self.m.call('missiles_selected_evolution_pending_is_well_formed', True))
                self.assertFalse(self.m.condition(item(self.s.events['chaosx.nr32.201'], 'trigger')))
                self.m.deliver('chaosx.nr32.201')
                self.assertEqual(self.m.log_inputs, [])
                self.pulse()
                self.select(track)
                self.assertTrue(self.m.call('missiles_selected_evolution_has_native_clock', True))
                self.assertEqual(self.m.log_inputs, [])

    def test_duplicate_native_callbacks_and_fresh_record_acknowledgement(self):
        self.pulse(ordinary=True)
        self.m.deliver('chaosx.nr32.201')
        self.assertEqual([row[:3] for row in self.m.log_inputs], [(D(32), D(32), D(4))])
        self.assertEqual(self.m.log_inputs[0][-1], ZERO)
        self.assertEqual(sum(x[1] == 'chaosx.nr32.8' for x in self.m.deliveries), 2)
        self.m.deliver('chaosx.nr32.201')
        self.assertEqual(len(self.m.log_inputs), 1)
        self.m.temp('missiles_evolution_commits', ZERO)
        self.m.temp('missiles_evolution_logged_stage', D(99))
        self.select(TRACKS[0])
        self.m.call('missiles_commit_evolution_track')
        self.assertEqual(self.m.value('missiles_evolution_commits'), ZERO)
        self.assertEqual(self.m.value('missiles_evolution_logged_stage'), ZERO)
        self.assertEqual(len(self.m.log_inputs), 1)

    def test_duplicate_recorder_between_gate_and_commit_has_no_fresh_ack(self):
        self.pulse(ordinary=True)
        self.select(TRACKS[0])
        self.m.temp('missiles_evolution_commits', ZERO)
        self.m.temp('missiles_evolution_logged_stage', D(99))
        # Explicit scenario transition after the real shared gate returns.
        # No predicate, recorder, arithmetic or acknowledgement is stubbed.
        self.m.after_call['is_current_evolution_enabled'] = lambda m: m.global_flags.add(
            'missiles_evolution_rogue_launch_commands_unlocked')
        self.m.call('missiles_commit_evolution_track')
        self.assertEqual(self.m.value('missiles_evolution_logged_stage'), ZERO)
        self.assertEqual(self.m.value('missiles_evolution_commits'), ZERO)
        self.assertEqual(self.m.log_inputs, [])
        self.assertEqual(self.m.deliveries, [])

    def test_caller_owned_outputs_survive_but_helper_created_outputs_expire(self):
        self.pulse(ordinary=True)
        self.select(TRACKS[0])
        self.m.temp('missiles_evolution_commits', ZERO)
        self.m.temp('missiles_evolution_adoption_loop_break', D(1))
        self.m.call('missiles_commit_evolution_track')
        self.assertEqual(self.m.value('missiles_evolution_commits'), D(1))
        # Shared inputs were owned by commit, stayed live through nested recorder,
        # then expired. The boundary captured actual live values above.
        for key in ('missiles_evolution_logged_stage', 'events_log_evolution_stage',
                    'events_log_evolution_tier', 'missiles_evolution_log_stage_input'):
            self.assertIsNone(self.m.temp_owner(key), key)
        self.assertEqual(self.m.log_inputs[0][:3], (D(32), D(32), D(4)))
        self.assertIsNone(self.m.temp_owner('chaosx_date_offset'))
        self.assertEqual(sum(x[1] == 'chaosx.nr32.8' for x in self.m.deliveries), 2)

    def test_short_mode_disabled_and_terminal_callbacks_never_record(self):
        for terminal in (False, True):
            with self.subTest(terminal=terminal):
                self.setUp()
                self.pulse()
                self.m.world.variables['date'] += self.offset(100)
                if terminal:
                    self.m.global_flags.add('world_end')
                else:
                    for track in TRACKS:
                        self.m.global_flags.add(f'events_log_disabled_evolution_32_32_{track[3]}')
                self.m.deliver('chaosx.nr32.190')
                self.assertEqual(self.m.log_inputs, [])
                self.assertNotIn('missiles_evolution_short_job_queued', self.m.global_flags)
                self.assertFalse(any(f.endswith(('_native_pending', '_short_pending')) for f in self.m.global_flags))

    def test_disabled_recorded_and_terminal_refuse_and_cancel(self):
        for reason in ('disabled', 'recorded', 'world_end'):
            for track in TRACKS:
                with self.subTest(reason=reason, track=track[0]):
                    self.setUp()
                    self.pulse(ordinary=True)
                    flag = (f'events_log_disabled_evolution_32_32_{track[3]}' if reason == 'disabled'
                            else f'missiles_evolution_{track[0]}_unlocked' if reason == 'recorded' else 'world_end')
                    self.m.global_flags.add(flag)
                    self.assertFalse(self.m.condition(item(self.s.events[f'chaosx.nr32.{track[4]}'], 'trigger')))
                    self.m.deliver(f'chaosx.nr32.{track[4]}')
                    self.pulse()
                    self.assertEqual(self.m.log_inputs, [])
                    self.assertNotIn(f'missiles_evolution_{track[0]}_pending', self.m.global_flags)
                    if reason == 'world_end':
                        self.assertFalse(any(f.endswith(('_native_pending', '_short_pending')) for f in self.m.global_flags))

    def test_overdue_short_callbacks_stagger_by_seven_days(self):
        self.pulse()
        self.m.world.variables['date'] = D(10) + self.offset(100)
        dates = []
        for track in TRACKS:
            before = len(self.m.log_inputs)
            self.m.deliver('chaosx.nr32.190')
            self.assertEqual(len(self.m.log_inputs), before + 1)
            self.assertEqual(self.m.log_inputs[-1][2], D(track[3]))
            dates.append(self.g('date'))
            self.m.deliver('chaosx.nr32.190')
            self.assertEqual(len(self.m.log_inputs), before + 1)
            if track != TRACKS[-1]:
                self.assertEqual(self.g('missiles_evolution_short_job_due_date'), dates[-1] + self.offset(7))
                self.m.world.variables['date'] += self.offset(7)
        self.assertEqual([b - a for a, b in zip(dates, dates[1:])], [self.offset(7)] * 4)
        self.assertNotIn('missiles_evolution_short_job_queued', self.m.global_flags)

    def test_host_change_and_zero_host_preserve_finite_track_receipts(self):
        self.pulse()
        original_due = self.g('missiles_evolution_rogue_launch_commands_due_date')
        self.a.exists = False
        self.m.temp('missiles_evolution_host_break', D(1))
        self.m.call('missiles_requeue_pending_evolution_jobs')
        self.assertIs(self.g('missiles_evolution_host'), self.b)
        self.assertEqual(self.g('missiles_evolution_short_job_host_id'), D(self.b.identity))
        self.m.world.variables['date'] = original_due
        self.m.deliver('chaosx.nr32.190', self.a)
        self.assertEqual(self.m.log_inputs, [])
        self.assertIn('missiles_evolution_short_job_queued', self.m.global_flags)
        self.b.exists = False
        self.m.call('missiles_select_evolution_host')
        self.assertNotIn('missiles_evolution_host', self.m.world.variables)
        self.assertNotIn('missiles_evolution_short_job_queued', self.m.global_flags)
        self.assertEqual(self.g('missiles_evolution_rogue_launch_commands_due_date'), original_due)
        self.b.exists = True
        self.m.call('missiles_requeue_pending_evolution_jobs')
        self.assertIs(self.g('missiles_evolution_host'), self.b)

    def test_notification_coalescing_has_no_self_successor(self):
        self.m.global_flags.discard('missiles_evolution_observing')
        for _ in range(3):
            self.m.call('missiles_notify_evolution_change')
        observations = lambda: [x for x in self.m.deliveries if x[1] == 'chaosx.nr32.192']
        self.assertEqual(len(observations()), 1)
        self.a.exists = False
        self.m.call('missiles_notify_evolution_change')
        self.assertEqual(len(observations()), 2)
        self.m.deliver('chaosx.nr32.192', self.a)
        self.assertIn('missiles_evolution_observation_queued', self.m.global_flags)
        self.m.deliver('chaosx.nr32.192', self.b)
        self.assertNotIn('missiles_evolution_observation_queued', self.m.global_flags)
        self.assertEqual(len(observations()), 2)
        generation = self.g('missiles_pressure_observation_generation')
        self.m.deliver('chaosx.nr32.192', self.b)
        self.assertEqual(self.g('missiles_pressure_observation_generation'), generation)

    def test_native_host_migration_rejects_obsolete_and_zero_host(self):
        self.pulse(ordinary=True)
        self.a.exists = False
        self.m.call('missiles_select_evolution_host')
        self.assertIs(self.g('missiles_evolution_host'), self.b)
        self.m.deliver('chaosx.nr32.202', self.a)
        self.assertEqual(self.m.log_inputs, [])
        self.b.exists = False
        self.m.call('missiles_select_evolution_host')
        self.assertNotIn('missiles_evolution_host_id', self.m.world.variables)
        self.m.deliver('chaosx.nr32.202', self.b)
        self.assertEqual(self.m.log_inputs, [])
        self.b.exists = True
        self.m.call('missiles_select_evolution_host')
        # Selecting another host invalidates the stored observation. An exact
        # allowed pulse must publish fresh counts before native delivery.
        self.assertNotIn('missiles_pressure_observation_ready', self.m.global_flags)
        self.m.deliver('chaosx.nr32.202', self.b)
        self.assertEqual(self.m.log_inputs, [])
        self.pulse()
        self.m.deliver('chaosx.nr32.202', self.b)
        self.assertEqual([row[2] for row in self.m.log_inputs], [D(2)])

    def test_state_control_notification_predicate_filters_stable_frontlines(self):
        # Inject post-change native counts and documented ROOT/FROM/FROM.FROM.
        # There is no engine callback execution or timing/order simulation.
        scenarios = (
            ('non_site_2_to_3', 3, 4, False, True, True, False),
            ('new_controller_two_boundary', 2, 4, False, True, True, False),
            ('old_controller_one_boundary', 3, 1, False, True, True, False),
            ('first_land_gain', 1, 4, False, True, True, True),
            ('last_land_loss', 3, 0, False, True, True, True),
            ('registered_site_new_programme', 3, 4, True, True, False, True),
            ('registered_site_former_programme', 3, 4, True, False, True, True),
            ('registered_site_no_programme', 3, 4, True, False, False, False),
            ('non_site_first_last_no_programme', 1, 0, False, False, False, False),
        )
        for label, new_count, old_count, registered, new_programme, old_programme, expected in scenarios:
            with self.subTest(scenario=label):
                self.setUp()
                self.m.global_flags.discard('missiles_evolution_observing')
                for country, count, participant in ((self.a, new_count, new_programme),
                                                     (self.b, old_count, old_programme)):
                    country.native_controlled_states = D(count)
                    # Keep the land-existence predicates consistent with the
                    # count facts if the real notification selects a host.
                    country.controlled_state = [Scope(f'{country.name}_land_{i}',
                        country.identity * 100 + i, 'state', controller=country) for i in range(count)]
                    if not participant:
                        country.flags.discard('missiles_program_initialized')
                changed = Scope('changed_state', 999, 'state', controller=self.a)
                if registered:
                    changed.flags.add('missiles_site_active')
                    changed.variables['missiles_site_capacity'] = D(10)
                self.m.callback_former, self.m.callback_state = self.b, changed
                block = self.s.state_control_notification
                self.assertEqual(self.m.condition(item(block.value, 'limit')), expected)
                self.m.execute([block])
                self.assertEqual(self.m.calls['missiles_notify_evolution_change'], int(expected))
                self.assertEqual([x[1] for x in self.m.deliveries], ['chaosx.nr32.192'] if expected else [])
                self.assertEqual(self.m.calls['missiles_measure_evolution_pressure'], 0)
                self.assertEqual(self.m.calls['missiles_handle_site_control_changed'], 0)
                self.assertEqual(self.m.log_inputs, [])

    def test_notification_handoff_reconciles_existing_short_dates_on_replacement(self):
        # B retains eligibility for the earliest Rogue row after A disappears.
        self.b.flags.add('missiles_code_compromise_active')
        self.pulse()
        key = 'missiles_evolution_rogue_launch_commands_due_date'
        due = self.g(key)
        self.assertEqual(due, D(10) + self.offset(21))
        self.assertEqual(self.g('missiles_evolution_short_job_host_id'), D(self.a.identity))
        # Explicit removed-world facts. Execute the real notification and
        # receiver handoff, not the chemical/site/operation removal closure.
        self.a.exists = False
        self.a.flags.add('missiles_program_cleanup_complete')
        self.m.world.arrays['missiles_program_registry'] = [self.b]
        self.m.global_flags.discard('missiles_evolution_observing')
        self.m.call('missiles_notify_evolution_change')
        self.assertIs(self.g('missiles_evolution_host'), self.b)
        self.assertEqual(self.g('missiles_evolution_short_job_host_id'), D(self.a.identity))
        self.assertEqual([x[0] for x in self.m.deliveries if x[1] == 'chaosx.nr32.192'], [self.b])
        self.m.deliver('chaosx.nr32.192', self.b)
        replacement_jobs = lambda: [x for x in self.m.deliveries
                                    if x[0] is self.b and x[1] == 'chaosx.nr32.190']
        self.assertEqual(len(replacement_jobs()), 1)
        self.assertEqual(replacement_jobs()[0][2], D(21))
        self.assertEqual(self.g(key), due)
        self.assertEqual(self.g('missiles_evolution_short_job_due_date'), due)
        self.assertEqual(self.g('missiles_evolution_short_job_host_id'), D(self.b.identity))
        # A duplicate notification burst and repeated allowed pulse must not
        # create another delivery for the same surviving finite receipt.
        self.m.call('missiles_notify_evolution_change')
        self.m.call('missiles_notify_evolution_change')
        self.m.deliver('chaosx.nr32.192', self.b)
        self.pulse()
        self.assertEqual(len(replacement_jobs()), 1)
        self.assertEqual(self.g(key), due)
        self.assertEqual(self.m.log_inputs, [])
        self.m.world.variables['date'] = due
        self.m.deliver('chaosx.nr32.190', self.a)
        self.assertEqual(self.m.log_inputs, [])
        self.assertEqual(self.g('missiles_evolution_short_job_host_id'), D(self.b.identity))
        self.assertEqual(self.g('missiles_evolution_short_job_due_date'), due)
        self.m.deliver('chaosx.nr32.190', self.b)
        self.assertEqual([row[:3] for row in self.m.log_inputs], [(D(32), D(32), D(4))])
        self.assertEqual(self.g('missiles_evolution_rogue_launch_commands_unlock_date'), due)
        self.assertNotIn(key, self.m.world.variables)
        self.m.deliver('chaosx.nr32.190', self.b)
        self.assertEqual(len(self.m.log_inputs), 1)

    def test_requeue_ignores_native_stale_dates_and_mixed_mode_rows(self):
        self.pulse()
        earliest = self.g('missiles_evolution_unreliable_guidance_due_date')
        self.a.exists = False
        # Both bad rows precede the earliest valid short date. Requeue must
        # filter them directly, before any observation can repair their mode.
        for track, mixed, days in ((TRACKS[0], False, 1), (TRACKS[3], True, 2)):
            key = f'missiles_evolution_{track[0]}'
            self.m.global_flags.add(f'{key}_native_pending')
            if not mixed:
                self.m.global_flags.discard(f'{key}_short_pending')
            self.m.world.variables[f'{key}_due_date'] = D(10) + self.offset(days)
        self.m.call('missiles_requeue_pending_evolution_jobs')
        jobs = [x for x in self.m.deliveries if x[0] is self.b and x[1] == 'chaosx.nr32.190']
        self.assertEqual(len(jobs), 1)
        self.assertEqual(jobs[0][2], D(35))
        self.assertEqual(self.g('missiles_evolution_short_job_due_date'), earliest)
        self.assertEqual(self.g('missiles_evolution_short_job_host_id'), D(self.b.identity))
        # This helper did not manufacture repair or consume either stale row.
        self.assertEqual(self.g('missiles_evolution_rogue_launch_commands_due_date'), D(10) + self.offset(1))
        self.assertEqual(self.g('missiles_evolution_special_warheads_due_date'), D(10) + self.offset(2))
        self.assertEqual(self.m.log_inputs, [])

    def test_native_trigger_closure_never_scans_registry_or_schedules(self):
        forbidden = {'any_country', 'every_country', 'random_country', 'for_each_loop',
                     'for_each_scope_loop', 'any_of_scopes', 'country_event', 'set_temp_variable_to_random'}
        def inspect(nodes, visited):
            for n in walk(nodes):
                self.assertNotIn(n.key, forbidden)
                if n.key in self.s.triggers and n.key not in visited:
                    visited.add(n.key)
                    inspect(self.s.triggers[n.key][0], visited)
        for track in TRACKS:
            event = self.s.events[f'chaosx.nr32.{track[4]}']
            self.assertEqual(item(event, 'is_triggered_only'), 'no')
            inspect(item(event, 'trigger'), set())
            mtth = item(event, 'mean_time_to_happen')
            # A native base above one day avoids the automatic-event diagnostic;
            # an always-on reciprocal factor keeps the effective unit at exactly
            # one day, so the global variable alone sets the median duration.
            local = self.s.event_locals[f'chaosx.nr32.{track[4]}']
            self.assertEqual(item(mtth, 'days'), '@missiles_mtth_unit_days')
            base = D(local['@missiles_mtth_unit_days'])
            self.assertGreater(base, D(1))
            modifiers = [n.value for n in mtth if n.key == 'modifier']
            self.assertEqual(len(modifiers), 2)
            self.assertEqual(item(modifiers[0], 'factor'), '@missiles_mtth_unit_reciprocal')
            self.assertEqual(item(modifiers[0], 'always'), 'yes')
            self.assertEqual(base * D(local['@missiles_mtth_unit_reciprocal']), D(1))
            self.assertEqual(item(modifiers[1], 'factor'), f'global.missiles_evolution_{track[2]}_mtth_days')
            self.assertEqual([n.key for n in modifiers[1]], ['factor'])
        for helper in ('missiles_run_evolution_watch', 'missiles_queue_evolution_watch'):
            self.assertFalse(any(n.key == 'country_event' for n in walk(self.s.effects[helper][0])))
        self.pulse(ordinary=True)
        for track in TRACKS:
            self.m.deliver(f'chaosx.nr32.{track[4]}')
        self.assertTrue(all(x[1] == 'chaosx.nr32.8' for x in self.m.deliveries))

    def test_actual_mtth_base_few_pressure_and_final_tier_factors(self):
        # M only, no cumulative curve, event tick cadence or random simulation.
        scenarios = (
            ('rogue', 120,
             {'vulnerable': 1}, {'vulnerable': 4}),
            ('guidance', 105,
             {'operational': 1, 'war': 0}, {'operational': 2, 'war': 2}),
            ('saturation', 90,
             {'operational': 1, 'war': 0}, {'operational': 2, 'war': 4}),
            ('special', 120,
             {'payload_owners': 1}, {'payload_owners': 2}),
            ('retaliation', 150,
             {'responders': 1, 'hostile_pairs': 0}, {'responders': 2, 'hostile_pairs': 2}),
        )
        for name, base, few, high in scenarios:
            entry = f'missiles_{name}_evolution_mtth'
            self.assertEqual(self.m.value(item(self.s.mtth[entry][0], 'base')), D(base))
            for settings, factor, final in ((few, D('1.5'), False), (high, D('.5'), False),
                                            (high, D('.4'), True)):
                with self.subTest(track=name, settings=settings, final=final):
                    self.m.world.variables.update({f'missiles_pressure_{k}': D(v) for k, v in settings.items()})
                    self.m.global_flags.discard('chaos_tier')
                    if final:
                        self.m.global_flags.add('chaos_tier')
                        self.m.flag_values['chaos_tier'] = self.s.constant('chaos_meter_tier_id.tier_final')
                    self.assertEqual(self.m.mtth_value(entry), D(base) * factor)
                    self.m.call('missiles_update_evolution_mtth_values')
                    self.assertEqual(self.g(f'missiles_evolution_{name}_mtth_days'), D(base) * factor)


if __name__ == '__main__':
    unittest.main()
