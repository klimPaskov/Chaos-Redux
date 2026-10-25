"""Bounded actual-source Event032 site payments and lifecycle regressions.

Run: python -B .tools/tests/test_event32_site_work_transactions.py
Production quote, universal native cost dispatch, measurements, date conversion,
receipt, site eligibility/scorer/region probe, recovery and decision/mission bodies execute in conservative
helper frames. Unknown commands fail. Only native wallet/world facts, native
mutation, scheduling/presentation primitives and survey registration are leaves.
State buildings, cores, category, neighbours and native strategic-region
membership are explicit world fixtures, never replacement scorer/helper bodies.
Registration records its exact input without claiming downstream construction.
This is not native engine stock, mission ordering, supply or AI-order proof.
"""
from __future__ import annotations

from collections import defaultdict, deque
from copy import copy
from decimal import ROUND_DOWN
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import operator
import unittest
from functools import lru_cache

from test_cbrn_payload_reservations import D, ZERO, Frame, Scope, Node, item, parse
from test_event32_native_evolution import EvolutionSource, EvolutionMachine, walk

ROOT_DIR = Path(__file__).resolve().parents[2]
SURVEY = 'missiles_launch_state_survey_mission'
RECOVERY = 'missiles_site_recovery_mission'
SURVEY_PARTS = ('manpower', 'support', 'fuel')
WALLET_PARTS = ('manpower', 'support_equipment', 'fuel')
SURVEY_QUOTE = (D(300), D(40), D(250))
RECOVERY_QUOTE = (D(1200), D(140), D(15))


class SiteSource(EvolutionSource):
    def __init__(self):
        super().__init__()
        for path, destination in (
            ('common/scripted_effects/032_missiles_survey_effects.txt', self.effects),
            ('common/scripted_effects/032_missiles_recovery_effects.txt', self.effects),
            ('common/scripted_effects/032_missiles_payload_receipt_effects.txt', self.effects),
            ('common/scripted_effects/032_missiles_achievement_effects.txt', self.effects),
            ('common/scripted_effects/chaosx_universal_cost_effects.txt', self.effects),
            ('common/scripted_triggers/032_missiles_survey_triggers.txt', self.triggers),
            ('common/scripted_triggers/032_missiles_recovery_triggers.txt', self.triggers),
            ('common/scripted_triggers/032_missiles_achievement_triggers.txt', self.triggers),
            ('common/scripted_triggers/chaosx_universal_cost_triggers.txt', self.triggers),
        ):
            self.load(path, destination)
        for path in (
            'common/script_constants/032_missiles_survey_constants.txt',
            'common/script_constants/032_missiles_recovery_constants.txt',
            'common/script_constants/chaosx_universal_cost_constants.txt',
        ):
            def flatten(prefix, nodes):
                for n in nodes:
                    if n.key == 'schema':
                        continue
                    key = f'{prefix}.{n.key}'
                    if isinstance(n.value, list):
                        flatten(key, n.value)
                    else:
                        self.constants[key] = D(n.value)
            for n in self.read(path):
                flatten(n.key, n.value)
        self.decisions, self.missions = {}, {}
        for path, destination in (
            ('common/decisions/032_missiles_decisions.txt', self.decisions),
            ('common/decisions/032_missiles_missions.txt', self.missions),
        ):
            nodes = self.read(path)
            locals_ = {n.key: n.value for n in nodes if n.key.startswith('@')}
            for category in nodes:
                if isinstance(category.value, list):
                    for n in category.value:
                        destination[n.key] = (n.value, locals_, path, n.line)


class SiteMachine(EvolutionMachine):
    """Typed native leaves plus the existing ordered source VM.

    Wallet outcomes specify a fraction of the requested mutation, never helper
    success. Getter queues separately model unavailable or inconsistent reads.
    Native credit captures both paid flags before mutation to prove retirement.
    Optional five-decimal truncation follows the offline variable representation
    as a sensitivity model, not a claimed measured engine implementation.
    """
    def __init__(self, source, actor, state, root=None, truncate=False):
        super().__init__(source, actor)
        self.root = actor if root is None else root
        self.callback_former = state  # Explicit native state-targeted FROM.
        self.world.variables['date'] = D(1000)
        self.wallet_outcomes = defaultdict(deque)
        self.getter_outcomes = defaultdict(deque)
        self.registrations, self.presentation, self.mission_requests = [], [], []
        # Applied dynamic modifiers as (scope identity, modifier) pairs, so
        # guarded removals read the same state that add/remove maintain.
        self.dynamic_modifiers = set()
        self.garrison_reads = []
        self.scored_states, self.score_outputs, self.payment_pools = [], [], []
        self.native_regions = {}
        self.truncate = truncate

    def scope(self, token):
        return super().scope(token.upper() if token in ('controller', 'owner') else token)

    def storage(self, token):
        if token.startswith(('ROOT.', 'PREV.', 'THIS.', 'event_target:')):
            owner, key = token.split('.', 1)
            return self.scope(owner), self.targeted(key)
        return super().storage(token)

    def temp(self, name, value):
        if self.truncate and isinstance(value, D):
            value = value.quantize(D('.00001'), rounding=ROUND_DOWN)
        super().temp(name, value)

    def value(self, token):
        if token == 'infrastructure_level':
            if self.current.kind != 'state':
                raise AssertionError('Native infrastructure getter outside STATE')
            return self.current.infrastructure
        if token == 'FROM':
            return self.scope(token)
        if token == 'FROM.id':
            return D(self.scope('FROM').identity)
        if isinstance(token, str) and token.startswith('var:'):
            return self.value(token[4:])
        if token in ('manpower_k', 'fuel_k') or (isinstance(token, str) and token.startswith('num_equipment@')):
            if self.current.kind != 'country':
                raise AssertionError('Native country wallet getter outside COUNTRY')
            queue = self.getter_outcomes[(self.current.name, token)]
            if queue:
                return queue.popleft()
            key = {'manpower_k': 'manpower', 'fuel_k': 'fuel'}.get(token)
            if key is not None:
                return self.current.stocks[key] / D(1000)
            return self.current.stocks.get(token[14:], ZERO)
        if isinstance(token, str) and token.endswith('^num'):
            return D(len(self.array(token[:-4])))
        return super().value(token)

    def array(self, token):
        if token.startswith(('ROOT.', 'PREV.', 'THIS.', 'event_target:')):
            owner, key = token.split('.', 1)
            return self.scope(owner).arrays.get(key, [])
        return super().rows(token)

    def rows(self, token):
        return self.array(token)

    def predicate(self, n):
        k, v = n.key, n.value
        if k in ('subtract_from_temp_variable', 'add_to_temp_variable'):
            # Installed trigger docs 713-736 and 7624-7641 support these.
            # Reuse the actual arithmetic execution, preserving frame lifetime.
            self.execute([n])
            return True
        if k == 'custom_trigger_tooltip':
            return self.condition([c for c in v if c.key != 'tooltip'])
        if k == 'always':
            return v == 'yes'
        if k == 'is_ai':
            return self.current.is_ai == (v == 'yes')
        if k == 'has_active_mission':
            return v in self.current.missions
        if k == 'is_owned_by':
            return self.current.owner is self.scope(v)
        if k == 'is_owned_and_controlled_by':
            return self.current.owner is self.scope(v) and self.current.controller is self.scope(v)
        if k == 'is_core_of':
            return self.scope(v) in self.current.cores
        if k == 'is_island_state':
            return self.current.is_island == (v == 'yes')
        if k == 'has_state_category':
            return self.current.category == v
        if k == 'any_neighbor_state':
            return any(self.enter(s, v, True) for s in self.current.neighbors)
        if k == 'any_state_in':
            # Installed triggers 1693-1714. Region IDs come from the supplied
            # native map fixture. Production meta expansion and membership
            # filters still execute, including PREV/ROOT scope transitions.
            if not isinstance(v, list) or item(v, 'strategic_region') is None:
                self.unmodeled(n)
            region = item(v, 'strategic_region')
            if not region.isdigit():
                raise AssertionError('Region selector must be emitted as a static native ID')
            body = [c for c in v if c.key != 'strategic_region']
            return any(self.enter(s, body, True) for s in self.native_regions.get(int(region), []))
        if k in ('rocket_site', 'supply_node', 'anti_air_building', 'radar_station',
                 'rail_way', 'arms_factory', 'industrial_complex', 'dockyard',
                 'resistance', 'resistance_target'):
            if self.current.kind != 'state':
                raise AssertionError('Native state value outside STATE')
            return {'<': operator.lt, '>': operator.gt, '=': operator.eq}[n.op](
                self.current.native_values[k], self.value(v))
        if k == 'is_in_array':
            return self.value(item(v, 'value')) in self.array(item(v, 'array'))
        if k in ('has_manpower', 'has_fuel', 'command_power'):
            key = {'has_manpower': 'manpower', 'has_fuel': 'fuel', 'command_power': 'command_power'}[k]
            return {'<': operator.lt, '>': operator.gt, '=': operator.eq}[n.op](
                self.current.stocks[key], self.value(v))
        if k == 'has_equipment':
            if len(v) != 1 or v[0].key not in ('support_equipment', 'infantry_equipment'):
                return super().predicate(n)
            entry = v[0]
            return {'<': operator.lt, '>': operator.gt, '=': operator.eq}[entry.op](
                self.current.stocks[entry.key], self.value(entry.value))
        if k == 'divisions_in_state':
            if self.current.kind != 'country' or {c.key for c in v} != {'state', 'size'}:
                self.unmodeled(n)
            state = self.value(item(v, 'state'))
            if not isinstance(state, Scope) or state.kind != 'state':
                raise AssertionError('Garrison requires a typed exact STATE pointer')
            size = next(c for c in v if c.key == 'size')
            if size.value.startswith(('constant:', 'var:')):
                raise AssertionError('Garrison static count was not emitted by production meta trigger')
            count = state.divisions.get(self.current, 0)
            self.garrison_reads.append((self.current, state, count, size.op, D(size.value)))
            return {'>': operator.gt, '<': operator.lt}[size.op](D(count), D(size.value))
        if k == 'infrastructure':
            return {'<': operator.lt, '>': operator.gt, '=': operator.eq}[n.op](
                self.current.infrastructure, self.value(v))
        if k == 'is_capital':
            return self.current.is_capital == (v == 'yes')
        if k == 'has_dynamic_modifier':
            if not isinstance(v, list) or {c.key for c in v} != {'modifier'}:
                self.unmodeled(n)
            return (self.current.identity, item(v, 'modifier')) in self.dynamic_modifiers
        return super().predicate(n)

    def call(self, name, trigger=False):
        if name == 'missiles_register_site' and not trigger:
            if self.current.kind != 'state':
                raise AssertionError('Survey registration consumer outside STATE')
            # Boundary captures input only. It neither invents an active site nor
            # simulates construction, registry insertion or registration success.
            self.calls[name] += 1
            self.registrations.append((self.current, self.root,
                self.root.variables.get('missiles_survey_payment_id'),
                'missiles_survey_payment_active' in self.root.flags,
                'missiles_survey_fully_paid' in self.root.flags))
            return None
        if name == 'missiles_score_site_candidate' and not trigger:
            # Trace the real helper, verify caller-owned output lifetime rather
            # than permitting its newly created local temporary to escape.
            if self.temp_owner('missiles_candidate_score') is None:
                raise AssertionError('Scorer output was not initialized by its caller')
            state = self.current
            self.scored_states.append(state)
            result = super().call(name, trigger)
            self.score_outputs.append((state, self.value('missiles_candidate_score')))
            return result
        return super().call(name, trigger)

    def mutate_wallet(self, key, delta):
        if self.current.kind != 'country':
            raise AssertionError('Wallet mutation outside COUNTRY')
        kind = 'debit' if delta < 0 else 'credit'
        if kind == 'debit' and 'missiles_survey_payment_active' in self.current.flags:
            self.payment_pools.append((list(self.current.arrays['missiles_survey_candidate_states']),
                list(self.current.arrays['missiles_survey_candidate_scores']),
                self.current.variables['missiles_survey_candidate_state'],
                self.current.variables['missiles_survey_candidate_generation'],
                self.current.variables['missiles_survey_payment_id']))
        queue = self.wallet_outcomes[(self.current.name, key, kind)]
        fraction = queue.popleft() if queue else D(1)
        before = self.current.stocks[key]
        actual = delta * fraction
        after = before + actual
        if after < 0:
            raise AssertionError('Injected native mutation overdraws wallet')
        self.nativecalls.append((self.current, key, delta, after - before,
            'missiles_survey_payment_active' in self.current.flags,
            'missiles_survey_fully_paid' in self.current.flags))
        self.current.stocks[key] = after

    def execute(self, nodes):
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
            if k == 'hidden_effect':
                self.execute(v)
            elif k == 'custom_effect_tooltip':
                self.presentation.append((self.current, k, v))
            elif k in ('add_manpower', 'add_fuel', 'add_command_power'):
                self.mutate_wallet({'add_manpower': 'manpower', 'add_fuel': 'fuel',
                                    'add_command_power': 'command_power'}[k], self.value(v))
            elif k == 'add_equipment_to_stockpile':
                if {c.key for c in v} != {'type', 'amount'} or item(v, 'type') not in ('support_equipment', 'infantry_equipment'):
                    self.unmodeled(n)
                self.mutate_wallet(item(v, 'type'), self.value(item(v, 'amount')))
            elif k == 'activate_mission':
                # Captured request plus declared native active flag, no autonomous
                # ticking, available/cancel evaluation or callback order invented.
                self.mission_requests.append((self.current, v))
                self.current.missions.add(v)
            elif k == 'remove_mission':
                # Installed effect docs: removal runs no completion/timeout.
                self.mission_requests.append((self.current, k, v))
                self.current.missions.discard(v)
            elif k in ('set_state_flag', 'clr_state_flag'):
                if self.current.kind != 'state' or not isinstance(v, str):
                    self.unmodeled(n)
                (self.current.flags.add if k == 'set_state_flag' else self.current.flags.discard)(v)
            elif k in ('add_dynamic_modifier', 'remove_dynamic_modifier'):
                if not isinstance(v, list) or item(v, 'modifier') is None:
                    self.unmodeled(n)
                entry = (self.current.identity, item(v, 'modifier'))
                if k == 'add_dynamic_modifier':
                    self.dynamic_modifiers.add(entry)
                else:
                    self.dynamic_modifiers.discard(entry)
                self.presentation.append((self.current, k, v))
            elif k in ('add_ideas', 'remove_ideas'):
                self.presentation.append((self.current, k, v))
            elif k in ('every_owned_state', 'every_controlled_state'):
                if self.current.kind != 'country':
                    raise AssertionError('Native owned/control iterator outside COUNTRY')
                for s in list(getattr(self.current, k[6:])):
                    if self.enter(s, item(v, 'limit', []), True):
                        self.enter(s, [c for c in v if c.key != 'limit'])
            elif k == 'controller':
                self.enter(self.scope(k), v)
            elif k in ('clear_array', 'add_to_array', 'remove_from_array'):
                token = v if isinstance(v, str) else item(v, 'array')
                owner, key = self.storage(token)
                if k == 'clear_array':
                    owner.arrays[key] = []
                elif k == 'add_to_array':
                    owner.arrays.setdefault(key, []).append(self.value(item(v, 'value')))
                else:
                    val = self.value(item(v, 'value'))
                    owner.arrays[key] = [s for s in owner.arrays.get(key, []) if s != val]
            elif k == 'for_loop_effect':
                # Installed effects 4312-4330. Only the region probe's supported
                # ascending inclusive form is implemented. Unlike foreach,
                # this numeric iterator has the documented 1,000 bound.
                if item(v, 'compare') != 'less_than_or_equals' or item(v, 'add', '1') != '1':
                    self.unmodeled(n)
                start, end = self.value(item(v, 'start')), self.value(item(v, 'end'))
                if start != start.to_integral_value() or end != end.to_integral_value():
                    self.unmodeled(n)
                body = [c for c in v if c.key not in ('start', 'end', 'compare', 'add', 'value', 'break')]
                for index in range(int(start), min(int(end) + 1, int(start) + 1000)):
                    self.temp(item(v, 'value', 'v'), D(index))
                    self.execute(body)
                    if self.value(item(v, 'break', 'break')) != ZERO:
                        break
            else:
                super().execute([n])

    def surface(self, definition, field, trigger=False):
        body, locals_, path, line = definition
        self.locals.append(locals_)
        self.frames.append(Frame())
        self.trace.append(f'{path}:{line} {field}')
        try:
            nodes = item(body, field)
            if nodes is None:
                raise AssertionError(f'Missing {field}')
            return self.condition(nodes) if trigger else self.execute(nodes)
        finally:
            self.trace.pop()
            self.frames.pop()
            self.locals.pop()

    def advance(self, days):
        # Scenario time, distinct from execution of production date helpers.
        units = self.source.constant('chaosx_date_units.hours_per_day') / self.source.constant('chaosx_date_units.hours_per_date_unit')
        self.world.variables['date'] = D(1000) + D(days) * units


@lru_cache(maxsize=1)
def source_template():
    # Parse this process's actual source once. Node definitions are immutable;
    # each scenario receives its own tuning dictionary and all world objects.
    return SiteSource()


def setup(ai=False, rogue=False, root_foreign=False, truncate=False):
    source = copy(source_template())
    source.constants = source.constants.copy()
    actor, foreign = Scope('owner', 11), Scope('foreign', 22)
    site, other = Scope('site', 101, 'state'), Scope('other', 102, 'state')
    for country in (actor, foreign):
        country.stocks.update(manpower=D(10000), support_equipment=D(500), fuel=D(5000),
                              infantry_equipment=D(1000), command_power=D(100))
        country.is_ai = ai
        country.missions = set()
        country.owned_state = [site, other] if country is actor else []
        country.controlled_state = list(country.owned_state)
        country.native_controlled_states = len(country.controlled_state)
    for s in (site, other):
        native_state(s, actor)
        s.divisions = {actor: 2 if rogue else 0, foreign: 20}
        s.variables['missiles_site_strategic_region'] = D(7)
    actor.flags.update({'missiles_program_initialized', 'missiles_command_control_secure',
                        'missiles_program_phase_rogue' if rogue else 'missiles_program_phase_establishment'})
    actor.variables.update(missiles_program_stage=D(1), missiles_operational_reserve=ZERO,
                           missiles_launch_readiness=D(60), missiles_command_control=D(60),
                           missiles_reserved_reserve=ZERO)
    actor.arrays['missiles_launch_site_states'] = [site] if rogue else []
    if rogue:
        actor.flags.update({'missiles_rogue_command_active', 'missiles_rogue_active_counted', 'missiles_incident_active'})
        actor.variables.update(missiles_rogue_site_state=site, missiles_rogue_site_id=D(site.identity),
            missiles_rogue_context_id=D(71), missiles_active_incident_id=D(71),
            missiles_current_incident_type=source.constant('missiles_incident_type.rogue_preparation'))
        site.flags.add('missiles_site_rogue')
        site.variables.update(missiles_site_capacity=D(10), missiles_site_damage=ZERO,
                              missiles_site_hardening=D(10), missiles_site_security=D(10))
    machine = SiteMachine(source, actor, site, foreign if root_foreign else actor, truncate)
    machine.world.variables['missiles_rogue_active_incidents'] = D(1 if rogue else 0)
    return machine, actor, site, foreign, other


def native_state(state, actor, infrastructure=5):
    """Explicit native facts, independently supplied from production scores."""
    state.owner = state.controller = actor
    state.infrastructure, state.is_capital = D(infrastructure), False
    state.cores, state.neighbors, state.is_island = {actor}, [], False
    state.category = 'rural'
    state.native_values = dict.fromkeys(('rocket_site', 'supply_node', 'anti_air_building',
        'radar_station', 'rail_way', 'arms_factory', 'industrial_complex', 'dockyard',
        'resistance', 'resistance_target'), ZERO)
    # Most scenarios supply the durable region cache. The explicit region-probe
    # scenario removes it and supplies native_regions, exercising the real probe.
    state.variables['missiles_site_strategic_region'] = D(7)
    return state


def wallet(actor, parts=WALLET_PARTS):
    return tuple(actor.stocks[k] for k in parts)


def snapshot(actor):
    # Preserve pointer identity when comparing rejected transactions.
    return (dict(actor.variables), set(actor.flags),
            {k: list(v) for k, v in actor.arrays.items()}, dict(actor.stocks), set(actor.missions))


class SurveyTransactions(unittest.TestCase):
    def start(self, m):
        m.call('missiles_begin_survey')

    def test_quote_component_available_and_native_cost_gates_below_exact_above(self):
        for ai in (False, True):
            for index, (resource, quote) in enumerate(zip(WALLET_PARTS, SURVEY_QUOTE)):
                for offset in (-1, 0, 1):
                    with self.subTest(ai=ai, resource=resource, offset=offset):
                        m, a, _, _, _ = setup(ai=ai)
                        a.stocks[resource] = quote + offset
                        before = snapshot(a)
                        decision = m.source.decisions['missiles_survey_launch_state']
                        self.assertEqual(m.call(f'missiles_survey_{SURVEY_PARTS[index]}_is_affordable', True), offset >= 0)
                        self.assertTrue(m.surface(decision, 'available', True))
                        self.assertEqual(m.surface(decision, 'custom_cost_trigger', True), offset >= 0)
                        self.assertEqual(snapshot(a), before)
                        self.assertGreater(m.calls['universal_cost_component_is_affordable'], 0)

    def test_actual_decision_starts_once_and_freezes_quote_due_and_paid_receipt(self):
        m, a, s, _, _ = setup()
        for k, v in zip(WALLET_PARTS, SURVEY_QUOTE):
            a.stocks[k] = v
        decision = m.source.decisions['missiles_survey_launch_state']
        m.surface(decision, 'complete_effect')
        self.assertEqual(wallet(a), (ZERO, ZERO, ZERO))
        self.assertEqual([c[2] for c in m.nativecalls], [-v for v in SURVEY_QUOTE])
        self.assertEqual(a.variables['missiles_survey_start_result'], D(1))
        self.assertIs(a.variables['missiles_survey_site_state'], s)
        self.assertEqual(a.variables['missiles_survey_payment_actor_id'], D(a.identity))
        self.assertEqual(a.variables['missiles_survey_payment_site_id'], D(s.identity))
        self.assertEqual(a.variables['missiles_survey_payment_id'], a.variables['missiles_survey_generation'])
        self.assertEqual(a.variables['missiles_survey_paid_duration_days'], D(60))
        date_units = D(60) * m.source.constant('chaosx_date_units.hours_per_day') / m.source.constant('chaosx_date_units.hours_per_date_unit')
        self.assertEqual(a.variables['missiles_survey_due_date'] - a.variables['missiles_survey_started_date'], date_units)
        self.assertTrue(m.call('missiles_survey_project_is_funded', True))
        self.assertEqual(m.mission_requests, [(a, SURVEY)])
        receipt = tuple(a.variables[f'missiles_survey_{k}'] for k in ('payment_id', 'generation', 'started_date', 'due_date'))
        self.start(m)
        self.assertEqual(len(m.nativecalls), 3)
        self.assertEqual(tuple(a.variables[f'missiles_survey_{k}'] for k in ('payment_id', 'generation', 'started_date', 'due_date')), receipt)
        self.assertEqual(m.calls['universal_cost_pay_component'], 3)

    def test_rejected_start_has_no_payment_receipt_mission_or_site_mutation(self):
        for reason in ('poor', 'foreign', 'registered', 'impassable', 'wasteland',
                       'cleanup', 'active', 'stale_active', 'native_active', 'split'):
            with self.subTest(reason=reason):
                m, a, s, foreign, other = setup()
                if reason == 'poor': a.stocks['fuel'] = D(249)
                if reason == 'foreign':
                    for state in (s, other): state.owner = foreign
                if reason == 'registered': a.arrays['missiles_launch_site_states'] = [s, other]
                if reason == 'impassable':
                    for state in (s, other): state.impassable = True
                if reason == 'wasteland':
                    for state in (s, other): state.category = 'wasteland'
                if reason == 'cleanup': a.flags.add('missiles_program_cleanup_complete')
                if reason == 'split': a.flags.add('missiles_civil_war_split_transaction_active')
                if reason in ('active', 'stale_active'):
                    a.flags.add('missiles_survey_payment_active')
                    a.variables['missiles_survey_payment_id'] = D(5)
                if reason == 'native_active': a.missions.add(SURVEY)
                before = snapshot(a)
                self.start(m)
                expected_vars = dict(before[0], missiles_survey_start_result=ZERO,
                    missiles_survey_quote_manpower=D(300), missiles_survey_quote_support=D(40), missiles_survey_quote_fuel=D(250))
                expected_arrays = before[2]
                # An all-impassable country has no controlled land, so the owner gate rejects before any pool is frozen.
                if reason in ('foreign', 'registered', 'wasteland'):
                    expected_arrays = dict(expected_arrays, missiles_survey_candidate_states=[], missiles_survey_candidate_scores=[])
                self.assertEqual(snapshot(a), (expected_vars, before[1], expected_arrays, *before[3:]))
                self.assertEqual(m.nativecalls, [])
                self.assertEqual(m.mission_requests, [])
                self.assertEqual(m.registrations, [])

    def test_refund_elapsed_days_ceil_and_integer_floor_without_repricing(self):
        for days in ('0', '30', '60', '90', '0.5', '30.5', '59.5'):
            with self.subTest(days=days):
                m, a, _, _, _ = setup()
                before = wallet(a)
                self.start(m)
                m.source.constants.update({'missiles_survey_payment.manpower': D(999),
                    'missiles_survey_payment.support_equipment': D(99),
                    'missiles_survey_payment.fuel': D(9999),
                    'missiles_evolution_timing.survey_mission_days': D(10)})
                m.call('missiles_refresh_survey_quote')
                m.advance(days)
                m.call('missiles_cancel_site_survey')
                elapsed = min(60, (Fraction(days).__ceil__()))
                expected = tuple(D((int(q) * (60 - elapsed)) // 60) for q in SURVEY_QUOTE)
                self.assertEqual(tuple(a.variables[f'missiles_survey_last_refund_{p}'] for p in SURVEY_PARTS), expected)
                self.assertEqual(wallet(a), tuple(b - q + r for b, q, r in zip(before, SURVEY_QUOTE, expected)))
                self.assertNotIn('missiles_survey_payment_active', a.flags)
                self.assertNotIn('missiles_survey_fully_paid', a.flags)
                self.assertFalse(any(c[4] or c[5] for c in m.nativecalls if c[2] > 0))
                paid_wallet = wallet(a)
                for callback in ('missiles_cancel_site_survey', 'missiles_complete_survey', 'missiles_refund_cancelled_survey'):
                    m.call(callback)
                self.assertEqual(wallet(a), paid_wallet)
                self.assertEqual(m.registrations, [])

    def test_invalid_receipt_is_retained_and_cannot_mint_refunds_or_succeed(self):
        cases = {'zero_id': ('missiles_survey_payment_id', ZERO),
                 'negative_id': ('missiles_survey_payment_id', D(-1)),
                 'actor': ('missiles_survey_payment_actor_id', D(22)),
                 'generation': ('missiles_survey_generation', D(99)),
                 'pool_generation': ('missiles_survey_candidate_generation', D(99)),
                 'missing_pool_generation': ('missiles_survey_candidate_generation', None),
                 'frozen_winner_id': ('missiles_survey_candidate_state_id', D(999)),
                 'site_id': ('missiles_survey_payment_site_id', D(999)),
                 'zero_duration': ('missiles_survey_paid_duration_days', ZERO),
                 'missing_actual': ('missiles_survey_paid_support', None),
                 'inflated_actual': ('missiles_survey_paid_support', D(41)),
                 'missing_quote': ('missiles_survey_quoted_support', None),
                 'negative_actual': ('missiles_survey_paid_fuel', D(-1)),
                 'missing_start': ('missiles_survey_started_date', None)}
        for name, (field, val) in cases.items():
            with self.subTest(case=name):
                m, a, s, _, _ = setup()
                self.start(m)
                if val is None: a.variables.pop(field)
                else: a.variables[field] = val
                hold = (a.variables.get('missiles_survey_payment_id'), a.variables.get('missiles_survey_paid_manpower'))
                before = wallet(a)
                m.advance(60)
                m.call('missiles_complete_survey')
                m.call('missiles_cancel_site_survey')
                self.assertEqual(wallet(a), before)
                self.assertIn('missiles_survey_payment_active', a.flags)
                self.assertIs(a.variables['missiles_survey_site_state'], s)
                self.assertEqual((a.variables.get('missiles_survey_payment_id'), a.variables.get('missiles_survey_paid_manpower')), hold)
                self.assertEqual(m.registrations, [])
                self.assertEqual(len(m.nativecalls), 3)

    def test_unfunded_receipt_cannot_satisfy_actual_mission_goal(self):
        for field in ('missiles_survey_fully_paid', 'missiles_survey_paid_support', 'missiles_survey_quoted_fuel'):
            with self.subTest(field=field):
                m, a, _, _, _ = setup()
                self.start(m)
                if field.endswith('fully_paid'): a.flags.remove(field)
                elif field.endswith('paid_support'): a.variables[field] = ZERO
                else: a.variables[field] += 1
                m.advance(60)
                self.assertFalse(m.surface(m.source.missions[SURVEY], 'available', True))
                m.call('missiles_complete_survey')
                self.assertEqual(m.registrations, [])

    def test_fresh_success_calls_exact_registration_once_and_has_zero_refund(self):
        m, a, s, _, _ = setup()
        self.start(m)
        before = wallet(a)
        m.advance(59)
        m.call('missiles_complete_survey')
        self.assertEqual(m.registrations, [])
        m.advance(60)
        self.assertTrue(m.surface(m.source.missions[SURVEY], 'available', True))
        m.surface(m.source.missions[SURVEY], 'complete_effect')
        self.assertEqual(m.registrations, [(s, a, D(1), True, True)])
        self.assertEqual(wallet(a), before)
        self.assertEqual(tuple(a.variables[f'missiles_survey_last_refund_{p}'] for p in SURVEY_PARTS), (ZERO,) * 3)
        self.assertIn('missiles_survey_complete', a.flags)
        self.assertNotIn('missiles_survey_payment_active', a.flags)
        self.assertNotIn('missiles_survey_in_progress', a.flags)
        for field in ('complete_effect', 'cancel_effect', 'timeout_effect'):
            m.surface(m.source.missions[SURVEY], field)
        self.assertEqual(len(m.registrations), 1)
        self.assertEqual(wallet(a), before)

    def test_depleted_wallet_foreign_root_and_removed_country_refund_ownership(self):
        m, a, _, foreign, _ = setup()
        self.start(m)
        for part in WALLET_PARTS: a.stocks[part] = ZERO
        m.root = foreign
        foreign_before = wallet(foreign)
        m.advance(30)
        m.call('missiles_cancel_site_survey')
        self.assertEqual(wallet(a), (D(150), D(20), D(125)))
        self.assertEqual(wallet(foreign), foreign_before)
        self.assertTrue(all(c[0] is a for c in m.nativecalls))
        m, a, _, foreign, _ = setup()
        self.start(m)
        a.exists = False
        m.root = foreign
        before = wallet(a), wallet(foreign)
        m.advance(30)
        m.call('missiles_cancel_site_survey')
        self.assertEqual((wallet(a), wallet(foreign)), before)
        self.assertIn('missiles_survey_refund_pending', a.flags)
        self.assertEqual(tuple(a.variables[f'missiles_survey_refund_{p}_pending'] for p in SURVEY_PARTS), (D(150), D(20), D(125)))

    def test_partial_native_debit_rolls_back_only_observed_payment(self):
        for resource in WALLET_PARTS:
            for fraction in (ZERO, D('.5')):
                with self.subTest(resource=resource, fraction=fraction):
                    m, a, _, _, _ = setup()
                    before = wallet(a)
                    m.wallet_outcomes[(a.name, resource, 'debit')].append(fraction)
                    self.start(m)
                    self.assertEqual(wallet(a), before)
                    self.assertNotIn('missiles_survey_in_progress', a.flags)
                    self.assertNotIn('missiles_survey_fully_paid', a.flags)
                    self.assertNotIn('missiles_survey_payment_active', a.flags)
                    self.assertEqual(a.variables['missiles_survey_start_result'], ZERO)
                    self.assertEqual(m.mission_requests, [])
                    self.assertEqual(m.registrations, [])
                    paid = {p: a.variables[f'missiles_survey_paid_{p}'] for p in SURVEY_PARTS}
                    for part, native in zip(SURVEY_PARTS, WALLET_PARTS):
                        actual_debit = -sum(c[3] for c in m.nativecalls if c[1] == native and c[2] < 0)
                        self.assertEqual(paid[part], actual_debit)
                        self.assertEqual(a.variables[f'missiles_survey_last_refund_{part}'], actual_debit)

    def test_capacity_limited_credit_remains_pending_and_retries_once(self):
        m, a, _, _, _ = setup()
        before = wallet(a)
        self.start(m)
        m.advance(30)
        m.wallet_outcomes[(a.name, 'fuel', 'credit')].append(D('.2'))
        m.call('missiles_cancel_site_survey')
        self.assertEqual(wallet(a), (before[0] - D(150), before[1] - D(20), before[2] - D(225)))
        self.assertEqual(a.variables['missiles_survey_last_refund_fuel'], D(25))
        self.assertEqual(a.variables['missiles_survey_refund_fuel_pending'], D(100))
        self.assertIn('missiles_survey_refund_pending', a.flags)
        self.assertFalse(m.call('missiles_survey_owner_is_ready', True))
        m.call('missiles_settle_pending_survey_refund')
        self.assertEqual(a.variables['missiles_survey_last_refund_fuel'], D(125))
        self.assertEqual(a.variables['missiles_survey_refund_fuel_pending'], ZERO)
        self.assertNotIn('missiles_survey_refund_pending', a.flags)
        settled = wallet(a)
        m.call('missiles_settle_pending_survey_refund')
        m.call('missiles_cancel_site_survey')
        self.assertEqual(wallet(a), settled)

    def test_inconsistent_native_observations_quarantine_without_repeat_credit(self):
        m, a, _, _, _ = setup()
        self.start(m)
        m.advance(30)
        m.getter_outcomes[(a.name, 'fuel_k')].extend((D('4.75'), D('4.95')))
        m.call('missiles_cancel_site_survey')
        self.assertIn('missiles_survey_native_accounting_quarantined', a.flags)
        self.assertIn('missiles_survey_refund_pending', a.flags)
        self.assertEqual(a.variables['missiles_survey_refund_fuel_pending'], D(125))
        before, calls = wallet(a), len(m.nativecalls)
        m.call('missiles_settle_pending_survey_refund')
        self.assertEqual(wallet(a), before)
        self.assertEqual(len(m.nativecalls), calls)
        self.assertFalse(m.call('missiles_survey_owner_is_ready', True))

    def test_malformed_pending_return_retains_balance_without_fresh_credit(self):
        for reason in ('missing_paid', 'missing_balance', 'wrong_payer', 'wrong_receipt', 'inflated', 'already_returned'):
            with self.subTest(reason=reason):
                m, a, _, _, _ = setup()
                self.start(m)
                m.advance(30)
                m.wallet_outcomes[(a.name, 'fuel', 'credit')].append(ZERO)
                m.call('missiles_cancel_site_survey')
                if reason == 'missing_paid': a.variables.pop('missiles_survey_paid_fuel')
                if reason == 'missing_balance': a.variables.pop('missiles_survey_refund_fuel_pending')
                if reason == 'wrong_payer': a.variables['missiles_survey_refund_actor_id'] = D(22)
                if reason == 'wrong_receipt': a.variables['missiles_survey_last_settlement_id'] += 1
                if reason == 'inflated': a.variables['missiles_survey_refund_fuel_pending'] = D(251)
                if reason == 'already_returned': a.variables['missiles_survey_last_refund_fuel'] = D(251)
                before, calls = snapshot(a), len(m.nativecalls)
                m.call('missiles_settle_pending_survey_refund')
                self.assertEqual(snapshot(a), before)
                self.assertEqual(len(m.nativecalls), calls)
                self.assertIn('missiles_survey_refund_pending', a.flags)

    def test_unavailable_before_read_prevents_mutation_and_quarantine_stops_same_pass(self):
        m, a, _, _, _ = setup()
        before = wallet(a)
        m.getter_outcomes[(a.name, 'manpower_k')].append(D(-1))
        self.start(m)
        self.assertEqual(wallet(a), before)

        self.assertEqual(m.nativecalls, [])
        self.assertIn('missiles_survey_native_accounting_quarantined', a.flags)
        self.assertEqual(a.variables['missiles_survey_anomaly_before'], D(-1000))
        self.assertEqual(a.variables['missiles_survey_anomaly_requested'], D(300))
        m, a, _, _, _ = setup()
        self.start(m)
        m.advance(30)
        before, calls = wallet(a), len(m.nativecalls)
        m.getter_outcomes[(a.name, 'manpower_k')].append(D(-1))
        m.call('missiles_cancel_site_survey')
        self.assertEqual(wallet(a), before)
        self.assertEqual(len(m.nativecalls), calls)
        self.assertEqual(tuple(a.variables[f'missiles_survey_refund_{p}_pending'] for p in SURVEY_PARTS),
                         (D(150), D(20), D(125)))
        saved = {k: v for k, v in a.variables.items() if k.startswith('missiles_survey_anomaly_')}
        m.call('missiles_settle_pending_survey_refund')
        self.assertEqual({k: v for k, v in a.variables.items() if k.startswith('missiles_survey_anomaly_')}, saved)
        self.assertEqual(wallet(a), before)


    def test_zero_return_does_not_query_native_stock_or_quarantine_success(self):
        m, a, _, _, _ = setup()
        self.start(m)
        for token in ('manpower_k', 'fuel_k', 'num_equipment@support_equipment'):
            m.getter_outcomes[(a.name, token)].append(D(-1))
        m.advance(60)
        before, calls = wallet(a), len(m.nativecalls)
        m.call('missiles_complete_survey')
        self.assertEqual(wallet(a), before)
        self.assertEqual(len(m.nativecalls), calls)
        self.assertNotIn('missiles_survey_native_accounting_quarantined', a.flags)
        self.assertNotIn('missiles_survey_refund_pending', a.flags)
        self.assertIn('missiles_survey_complete', a.flags)
        for token in ('manpower_k', 'fuel_k', 'num_equipment@support_equipment'):
            self.assertEqual(list(m.getter_outcomes[(a.name, token)]), [D(-1)])


class RecoveryTransactions(unittest.TestCase):
    def test_human_ai_share_entry_and_goal_garrison_without_foreign_units(self):
        for ai in (False, True):
            for troops in (0, 1, 2):
                with self.subTest(ai=ai, own_divisions=troops):
                    m, a, s, foreign, _ = setup(ai=ai, rogue=True)
                    s.divisions = {a: troops, foreign: 20}
                    decision = m.source.decisions['missiles_send_loyal_forces']
                    before = wallet(a, ('manpower', 'infantry_equipment', 'command_power'))
                    self.assertEqual(m.surface(decision, 'available', True), troops >= 2)
                    m.surface(decision, 'complete_effect')
                    if troops < 2:
                        self.assertEqual(wallet(a, ('manpower', 'infantry_equipment', 'command_power')), before)
                        self.assertNotIn('missiles_site_recovery_active', a.flags)
                        self.assertEqual(m.mission_requests, [])
                        continue
                    self.assertEqual(wallet(a, ('manpower', 'infantry_equipment', 'command_power')),
                                     tuple(v-q for v, q in zip(before, RECOVERY_QUOTE)))
                    self.assertEqual(m.mission_requests, [(a, RECOVERY)])
                    m.advance(14)
                    self.assertTrue(m.surface(m.source.missions[RECOVERY], 'available', True))
                    s.divisions[a] = 1
                    self.assertFalse(m.surface(m.source.missions[RECOVERY], 'available', True))
                    m.call('missiles_complete_site_recovery')
                    self.assertNotIn('missiles_site_recovery_complete', a.flags)
                    self.assertIn('missiles_rogue_command_active', a.flags)

    def test_exact_quote_is_payable_and_duplicate_start_does_not_debit(self):
        for resource, quote in zip(('manpower', 'infantry_equipment', 'command_power'), RECOVERY_QUOTE):
            for delta in (-1, 0, 1):
                with self.subTest(resource=resource, delta=delta):
                    m, a, _, _, _ = setup(rogue=True)
                    a.stocks[resource] = quote + delta
                    decision = m.source.decisions['missiles_send_loyal_forces']
                    self.assertEqual(m.surface(decision, 'available', True), delta >= 0)
                    self.assertEqual(m.surface(decision, 'custom_cost_trigger', True), delta >= 0)
                    before = wallet(a, ('manpower', 'infantry_equipment', 'command_power'))
                    m.surface(decision, 'complete_effect')
                    if delta < 0:
                        self.assertEqual(wallet(a, ('manpower', 'infantry_equipment', 'command_power')), before)
                        continue
                    paid = wallet(a, ('manpower', 'infantry_equipment', 'command_power'))
                    m.call('missiles_begin_site_recovery')
                    self.assertEqual(wallet(a, ('manpower', 'infantry_equipment', 'command_power')), paid)
                    self.assertEqual(len(m.nativecalls), 3)

    def test_invalid_early_or_stale_recovery_never_rewards_or_closes_crisis(self):
        for reason in ('early', 'lost', 'scuttled', 'context', 'site', 'actor', 'no_crisis'):
            with self.subTest(reason=reason):
                m, a, s, foreign, other = setup(rogue=True)
                m.call('missiles_begin_site_recovery')
                m.advance(13 if reason == 'early' else 14)
                if reason == 'lost': s.controller = foreign
                if reason == 'scuttled': s.flags.add('missiles_site_scuttled')
                if reason == 'context': a.variables['missiles_rogue_context_id'] += 1
                if reason == 'site': a.variables['missiles_recovery_site_state'] = other
                if reason == 'actor': a.variables['missiles_site_recovery_actor_id'] = D(foreign.identity)
                if reason == 'no_crisis': a.flags.discard('missiles_rogue_command_active')
                before = a.variables['missiles_command_control']
                calls = m.calls['missiles_close_rogue_incident']
                m.call('missiles_complete_site_recovery')
                self.assertEqual(a.variables['missiles_command_control'], before)
                self.assertNotIn('missiles_site_recovery_complete', a.flags)
                self.assertEqual(m.calls['missiles_close_rogue_incident'], calls)

    def test_success_recovers_exact_site_closes_once_and_clears_receipt(self):
        m, a, s, _, _ = setup(rogue=True)
        m.call('missiles_begin_site_recovery')
        m.advance(14)
        before = a.variables['missiles_command_control']
        m.surface(m.source.missions[RECOVERY], 'complete_effect')
        self.assertEqual(a.variables['missiles_command_control'],
                         before + m.source.constant('missiles_program_value.command_loyal_force_gain'))
        self.assertIn('missiles_site_recovery_complete', a.flags)
        self.assertNotIn('missiles_site_recovery_active', a.flags)
        self.assertNotIn('missiles_rogue_command_active', a.flags)
        self.assertNotIn('missiles_rogue_context_id', a.variables)
        self.assertNotIn(RECOVERY, a.missions)
        self.assertNotIn('missiles_site_rogue', s.flags)
        self.assertEqual(m.world.variables['missiles_rogue_active_incidents'], ZERO)
        for key in ('actor_id', 'context_id', 'site_id'):
            self.assertNotIn(f'missiles_site_recovery_{key}', a.variables)
        recovered = snapshot(a)
        m.call('missiles_complete_site_recovery')
        self.assertEqual(snapshot(a), recovered)
        self.assertEqual(m.calls['missiles_close_rogue_incident'], 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
