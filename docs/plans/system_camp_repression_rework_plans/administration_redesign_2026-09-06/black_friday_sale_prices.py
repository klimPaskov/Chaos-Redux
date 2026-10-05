"""Event 026 sale prices for the camp source suites.

The camp decisions, window rows and refunds read
`global.black_friday_price_camp_rework_cost_<key>`. This helper builds those
globals the way the production table does: it parses the Camps group of
`black_friday_price_table_refresh_entries` and runs the production
`black_friday_price_table_quote` body through the foundation interpreter at
the requested payment ratio (basis points of `black_friday_event.ratio_basis`).
A suite reads a price that the table does not register as a KeyError, so a
typo in a decision or effect cannot silently read zero.

The Political Power credit is an Event 026 effect; suites count its calls
through `camp_test_black_friday_pp_credits` instead of executing the
achievement framework.

Source-contract evidence only; no HOI4 engine runs.
"""
from pathlib import Path
import re

from foundation_source_tests import Runtime, parse

ROOT = Path(__file__).resolve().parents[4]
PRICE_TABLE = 'common/scripted_effects/026_black_friday_price_table_effects.txt'
BLACK_FRIDAY_CONSTANTS = 'common/script_constants/026_black_friday_constants.txt'
CAMP_CONSTANTS = 'common/script_constants/camp_repression_rework_constants.txt'
RATIO_BASIS = 10000
# Ordinary price, the Event 026 baseline sale, and the evolved sale.
SALE_RATIOS = (10000, 5000, 2500)
CAMP_GROUPS = ('camp_rework_cost.', 'camp_rework_equipment_cost.')
CREDIT_COUNTER = 'camp_test_black_friday_pp_credits'


def _constants(path, categories):
    values = {}
    for category, _, block in parse((ROOT / path).read_text(encoding='utf-8-sig')):
        if category not in categories or not isinstance(block, list):
            continue
        for key, _, value in block:
            if key != 'schema' and not isinstance(value, list):
                values[f'{category}.{key}'] = float(value)
    return values


def _production_effects():
    return {key: value for key, _, value in parse((ROOT / PRICE_TABLE).read_text(encoding='utf-8-sig'))
            if not key.startswith('@')}


def camp_registrations():
    """Ordered (ordinary constant, global name, quantum constant) for camp entries."""
    entries = _production_effects()['black_friday_price_table_refresh_entries']
    registrations = []
    quantum = None
    pending = None
    for key, _, value in entries:
        if key == 'set_temp_variable' and isinstance(value, list):
            name, _, amount = value[0]
            if name == 'black_friday_price_quantum':
                quantum = None if amount == 'constant:black_friday_event.zero' else amount
            elif name == 'black_friday_price_ordinary':
                pending = amount if amount.startswith('constant:') and amount[9:].startswith(CAMP_GROUPS) else None
        elif key == 'set_variable' and isinstance(value, list) and pending is not None:
            name, _, amount = value[0]
            if amount == 'black_friday_price_payable':
                registrations.append((pending, name, quantum))
                pending = None
    return registrations


def sale_prices(ratio_bp):
    """Map every registered camp global to its production quote at ratio_bp."""
    runtime = Runtime()
    runtime.constants.update(_constants(BLACK_FRIDAY_CONSTANTS, {'black_friday_event'}))
    runtime.constants.update(_constants(CAMP_CONSTANTS, {'camp_rework_cost', 'camp_rework_equipment_cost'}))
    runtime.effects['black_friday_price_table_quote'] = _production_effects()['black_friday_price_table_quote']
    runtime.scopes['TABLE'] = {'id': 'TABLE', 'flags': set(), 'arrays': {}, 'mods': set()}
    prices = {}
    for ordinary, name, quantum in camp_registrations():
        runtime.temp.clear()
        runtime.temp['black_friday_price_ratio'] = ratio_bp
        runtime.temp['black_friday_price_quantum'] = runtime.val(quantum, 'TABLE') if quantum else 0
        runtime.temp['black_friday_price_ordinary'] = runtime.val(ordinary, 'TABLE')
        runtime.run('black_friday_price_table_quote', 'TABLE')
        assert name not in prices, ('Camp price registered twice', name)
        prices[name] = runtime.temp['black_friday_price_payable']
    return prices


def install(runtime, ratio_bp=RATIO_BASIS):
    """Serve camp sale prices to an interpreter instance and count PP credits."""
    prices = sale_prices(ratio_bp)
    runtime.black_friday_prices = prices
    runtime.black_friday_ratio = ratio_bp
    base_value = runtime.val

    def sale_value(value, scope, previous=None):
        if isinstance(value, str) and value.startswith('global.black_friday_price_'):
            return prices[value]
        return base_value(value, scope, previous)

    runtime.val = sale_value
    base_execute = runtime.execute

    def execute(block, scope, previous=None):
        # Engine primitive: hidden_effect runs its body in the current scope.
        flattened = [('if', '=', [('limit', '=', [])] + value) if key == 'hidden_effect' and isinstance(value, list)
                     else (key, op, value) for key, op, value in block]
        return base_execute(flattened, scope, previous)

    runtime.execute = execute
    runtime.effects['black_friday_credit_political_power_purchase'] = [
        ('add_to_temp_variable', '=', [(CREDIT_COUNTER, '=', '1')])]
    return prices


def credits(runtime):
    return runtime.temp.get(CREDIT_COUNTER, 0)


def price(runtime, key):
    return runtime.black_friday_prices['global.black_friday_price_camp_rework_cost_' + key]


def decision_cost_globals(text):
    """Every native cost global a decision file reads."""
    return re.findall(r'(?m)^\t\tcost = (global\.black_friday_price_[a-z0-9_]+)\s*$', text)


CAMP_DECISION_FILES = (
    'common/decisions/camp_repression_major_country_decisions.txt',
    'common/decisions/camp_repression_colonial_country_decisions.txt',
    'common/decisions/camp_repression_generic_decisions.txt',
    'common/decisions/camp_administration_country_decisions.txt',
    'common/decisions/camp_administration_civil_decisions.txt',
)
# Decisions whose payload credits the purchase only when the order is kept.
CREDIT_IN_EFFECT = {
    'ita_raise_colonial_security_battalions': (
        'common/scripted_effects/camp_repression_colonial_country_effects.txt',
        'camp_rework_italy_raise_security_battalions'),
}


def _count(block, key):
    total = 0
    for name, _, value in block:
        if name == key:
            total += 1
        if isinstance(value, list):
            total += _count(value, key)
    return total


def check_native_costs():
    """Every positive native camp cost reads a registered sale price and credits once."""
    prices = sale_prices(RATIO_BASIS)
    paid = []
    for path in CAMP_DECISION_FILES:
        source = (ROOT / path).read_text(encoding='utf-8-sig')
        assert 'cost = constant:camp_rework_cost.' not in source, path
        for _, _, category in parse(source):
            if not isinstance(category, list):
                continue
            for name, _, body in category:
                if not isinstance(body, list):
                    continue
                cost = next((value for key, _, value in body if key == 'cost'), None)
                if cost is None or cost == '0':
                    continue
                assert cost in prices, (name, cost)
                completion = next(value for key, _, value in body if key == 'complete_effect')
                credits_here = _count(completion, 'black_friday_credit_political_power_purchase')
                if name in CREDIT_IN_EFFECT:
                    effect_path, effect = CREDIT_IN_EFFECT[name]
                    effects = dict((key, value) for key, _, value in parse((ROOT / effect_path).read_text(encoding='utf-8-sig')))
                    assert credits_here == 0 and _count(effects[effect], 'black_friday_credit_political_power_purchase') == 1, name
                else:
                    assert credits_here == 1, (name, credits_here)
                paid.append(name)
    return paid
