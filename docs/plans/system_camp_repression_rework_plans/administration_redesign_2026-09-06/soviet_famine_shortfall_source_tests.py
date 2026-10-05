"""Exercise production famine options and relief dispatch with mocked native primitives.

Equipment, political-power ordering and mission activation are explicit mocks.
This suite establishes source behavior, not observed Clausewitz execution.
"""
from pathlib import Path
import json
from foundation_source_tests import Runtime, parse, get
import black_friday_sale_prices as sale

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
SALE_RATIO = sale.RATIO_BASIS


class FamineRuntime(Runtime):
    def __init__(self):
        super().__init__()
        for file in ('camp_repression_major_country_effects', 'camp_repression_action_dispatcher_effects', 'camp_repression_rework_effects'):
            self.effects.update({k: v for k, _, v in parse((ROOT / f'common/scripted_effects/{file}.txt').read_text(encoding='utf-8-sig')) if not k.startswith('@')})
        self.triggers.update({k: v for k, _, v in parse((ROOT / 'common/scripted_triggers/camp_repression_rework_triggers.txt').read_text(encoding='utf-8-sig'))})
        for category, _, body in parse((ROOT / 'common/script_constants/camp_repression_rework_constants.txt').read_text(encoding='utf-8-sig')):
            if isinstance(body, list):
                for key, _, value in body:
                    if key != 'schema' and not isinstance(value, list):
                        try:
                            self.constants[f'{category}.{key}'] = float(value)
                        except ValueError:
                            pass
        for helper in ('camp_rework_soviet_initialize_country_values', 'camp_rework_soviet_refresh_famine_states', 'camp_rework_recalculate_country_values', 'camp_rework_rebuild_display_values'):
            self.effects[helper] = []  # Other projections have separate suites.
        self.effects['camp_rework_show_soviet_famine_super_event'] = [('add_to_variable', '=', [('super_event_calls', '=', '1')])]
        self.timed_flag_writes = []
        self.equipment_debits = []
        self.activations = []
        self.c = self.country('SOV')
        self.c.update(original_tag='SOV', famine_pressure=85, grain_extraction_burden=60, forced_labor_quota=60, camp_administrator_corruption=20, camp_policy_evidence=10, state_population_k=1000)
        # One sale-aware stock cost: the decision, the event options and the shortfall all read the Event 026 price.
        sale.install(self, SALE_RATIO)
        self.quote = {kind: sale.stock(self, key) for kind, key in [('motorized_equipment_1', 'motorized_equipment'), ('train_equipment_1', 'trains'), ('support_equipment_1', 'support_equipment')]}
        self.c['equipment'] = self.quote.copy()
        source = parse((ROOT / 'events/soviet_gulag.txt').read_text(encoding='utf-8-sig'))
        self.events = {get(body, 'id'): body for key, _, body in source if key == 'country_event'}
        decisions = parse((ROOT / 'common/decisions/camp_repression_major_country_decisions.txt').read_text(encoding='utf-8-sig'))
        self.decision = next(body for _, _, category in decisions if isinstance(category, list) for key, _, body in category if key == 'sov_emergency_famine_relief')
        assert get(self.decision, 'cost') == 'global.black_friday_price_camp_rework_cost_labor_project_pp'
        self.price = sale.price(self, 'labor_project_pp')

    def cond(self, body, scope, previous=None):
        for key, operator, value in body:
            if key in ('AND', 'OR', 'NOT'):
                values = [self.cond([item], scope, previous) for item in value]
                accepted = all(values) if key == 'AND' else any(values) if key == 'OR' else not any(values)
                if not accepted:
                    return False
            elif key == 'has_active_mission':
                if value not in self.scopes[scope].get('missions', set()):
                    return False
            elif key == 'hidden_trigger':
                if not self.cond(value, scope, previous):
                    return False
            elif not super().cond([(key, operator, value)], scope, previous):
                return False
        return True

    def val(self, value, scope, previous=None):
        if isinstance(value, str) and value.startswith('var:'):
            return super().val(value[4:], scope, previous)
        return super().val(value, scope, previous)

    def execute(self, body, scope, previous=None):
        for i, (key, operator, value) in enumerate(body):
            if key == 'hidden_effect':
                super().execute(body[:i], scope, previous)
                self.execute(value, scope, previous)
                self.execute(body[i + 1:], scope, previous)
                return
            if key in ('add_equipment_to_stockpile', 'activate_mission') or (key == 'set_country_flag' and isinstance(value, list)):
                super().execute(body[:i], scope, previous)
                if key == 'add_equipment_to_stockpile':
                    kind = get(value, 'type')
                    amount = self.val(get(value, 'amount'), scope, previous)
                    self.scopes[scope]['equipment'][kind] += amount
                    self.equipment_debits.append((kind, amount))
                elif key == 'activate_mission':
                    self.scopes[scope].setdefault('missions', set()).add(value)
                    self.activations.append(value)
                else:
                    flag = get(value, 'flag')
                    duration = self.val(get(value, 'days'), scope, previous)
                    self.scopes[scope]['flags'].add(flag)
                    self.scopes[scope].setdefault('flag_durations', {})[flag] = duration
                    self.timed_flag_writes.append((flag, duration))
                self.execute(body[i + 1:], scope, previous)
                return
        super().execute(body, scope, previous)

    def options(self, event):
        return [body for key, _, body in self.events[event] if key == 'option' and self.cond(get(body, 'trigger', []), 'SOV')]

    def choose(self, event, name):
        option = next(body for key, _, body in self.events[event] if key == 'option' and get(body, 'name') == name)
        self.execute([item for item in option if item[0] not in ('name', 'trigger', 'ai_chance')], 'SOV')

    def paid_decision(self):
        self.c['political_power'] -= self.val(get(self.decision, 'cost'), 'SOV')
        self.execute(get(self.decision, 'complete_effect'), 'SOV')


def run_cases():
    results = []
    r = FamineRuntime()
    r.paid_decision()
    assert r.c['equipment'] == {kind: 0 for kind in r.quote}
    assert len(r.equipment_debits) == 3 and len(r.activations) == 1
    assert r.c['political_power'] == 100 - r.price and sale.credits(r) == 1
    assert r.timed_flag_writes == [('camp_gui_country_action_2_cooldown', r.constants['camp_rework_timing.standard_action_days'])]
    assert r.c['grain_extraction_burden'] < 60 and r.c['state_population_k'] == 1000 and r.logged == 0
    results.append('Exact stock: one quote, one mission, one PP debit and success cooldown')

    for kind in r.quote:
        short = FamineRuntime()
        short.c['equipment'][kind] -= 1
        before = short.c['equipment'].copy()
        assert not short.cond(get(short.decision, 'custom_cost_trigger'), 'SOV')
        assert not short.cond(get(short.decision, 'available'), 'SOV')
        for event, name in [('soviet_gulag.1', 'soviet_gulag.1.c'), ('soviet_gulag.2', 'soviet_gulag.2.shortfall')]:
            assert name in [get(option, 'name') for option in short.options(event)]
        short.paid_decision()  # Mock a click accepted before the stock changed.
        assert short.c['political_power'] == 100 and short.c['equipment'] == before and sale.credits(short) == 0
        assert not short.timed_flag_writes and not short.activations
        assert short.c['grain_extraction_burden'] == 60 and short.c['famine_pressure'] == 85
        results.append(f'One-unit-short {kind}: selectable shortfall, stale paid refund, no success')

    for event, funded, shortage in [('soviet_gulag.1', 'soviet_gulag.1.a', 'soviet_gulag.1.c'), ('soviet_gulag.2', 'soviet_gulag.2.a', 'soviet_gulag.2.shortfall')]:
        r = FamineRuntime()
        assert [get(option, 'name') for option in r.options(event)] == [funded]
        r.choose(event, funded)
        assert r.c['political_power'] == 100 and len(r.equipment_debits) == 3 and len(r.activations) == 1
        assert r.c['equipment'] == {kind: 0 for kind in r.quote} and sale.credits(r) == 1 and sale.last_family(r) == sale.family(r, 'equipment')
        results.append(f'{event}: funded option without site, no additional PP charge, sale-priced stock and one equipment purchase')
        r = FamineRuntime()
        r.c['equipment'] = {kind: 0 for kind in r.quote}
        assert [get(option, 'name') for option in r.options(event)] == [shortage]
        r.choose(event, shortage)
        assert r.c['famine_pressure'] > 85 and r.c['camp_administrator_corruption'] > 20
        assert not r.equipment_debits and not r.activations and r.c['political_power'] == 100
        assert r.c['state_population_k'] == 1000 and r.logged == 0
        if event == 'soviet_gulag.1':
            assert r.c['camp_policy_evidence'] == 10
        else:
            assert r.c['camp_policy_evidence'] > 10 and 'sov_famine_crisis_active' in r.c['flags']
        results.append(f'{event}: empty stock and invalid site still have one response, distinct penalty')
        r = FamineRuntime()
        r.c['equipment']['motorized_equipment_1'] -= 1
        r.choose(event, funded)  # Option was displayed while the quote was payable.
        assert not r.equipment_debits and not r.activations and r.c['famine_pressure'] > 85
        results.append(f'{event}: funded option stale at selection takes unfinanced consequence')
        r = FamineRuntime()
        r.c['equipment'] = {kind: 0 for kind in r.quote}
        r.c['flags'].add('sov_famine_relief_active')
        r.c['missions'] = {'sov_emergency_famine_relief_mission'}
        assert [get(option, 'name') for option in r.options(event)] == [event + '.relief_underway']
        r.choose(event, shortage)
        assert r.c['famine_pressure'] == 85 and r.c['camp_administrator_corruption'] == 20 and r.c['camp_policy_evidence'] == 10
        assert 'sov_famine_relief_active' in r.c['flags'] and r.c['missions'] == {'sov_emergency_famine_relief_mission'}
        assert not r.equipment_debits and not r.activations
        results.append(f'{event}: ongoing funded relief survives a late shortfall response without duplicate penalties')
        r = FamineRuntime()
        r.c['famine_pressure'] = 0
        r.c['equipment'] = {kind: 0 for kind in r.quote}
        r.execute(get(r.events[event], 'immediate', []), 'SOV')
        assert [get(option, 'name') for option in r.options(event)] == [event + '.famine_eased']
        r.choose(event, event + '.famine_eased')
        assert r.c.get('super_event_calls', 0) == 0 and 'sov_famine_crisis_active' not in r.c['flags']
        assert r.c['famine_pressure'] == 0 and r.c['equipment'] == {kind: 0 for kind in r.quote}
        assert not r.equipment_debits and not r.activations
        results.append(f'{event}: resolved famine has one acknowledgement and no false crisis presentation or payment')

    r = FamineRuntime()
    r.c['equipment'] = {kind: amount * 3 for kind, amount in r.quote.items()}
    r.paid_decision()
    paid = r.c['equipment'].copy()
    r.paid_decision()
    assert r.c['equipment'] == paid and len(r.activations) == 1 and r.c['political_power'] == 100 - r.price
    assert sale.credits(r) == 1  # The refunded duplicate earns no second sale credit.
    assert r.timed_flag_writes == [('camp_gui_country_action_2_cooldown', r.constants['camp_rework_timing.standard_action_days'])]
    results.append('Concurrent duplicate order: refund and no second material payment or mission')

    r = FamineRuntime()
    r.c['famine_pressure'] = 0
    r.paid_decision()
    assert not r.equipment_debits and not r.activations and r.c['political_power'] == 100 and sale.credits(r) == 0
    results.append('Resolved famine rejects stale native order without relief or cooldown')
    r = FamineRuntime()
    r.c['original_tag'] = 'GER'
    r.run('camp_rework_soviet_emergency_famine_relief', 'SOV')
    assert not r.equipment_debits and not r.activations
    results.append('Invalid original authority cannot execute the funded Soviet helper')
    return results


if __name__ == '__main__':
    cases = []
    for ratio in sale.SALE_RATIOS:
        SALE_RATIO = ratio
        cases += [f'payment ratio {ratio}: {case}' for case in run_cases()]
    (HERE / 'soviet_famine_shortfall_source_results.json').write_text(json.dumps({'scope': 'Production-source interpretation with mocked native receipts', 'cases': cases, 'count': len(cases)}, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'passed': len(cases), 'cases': cases}, indent=2))
