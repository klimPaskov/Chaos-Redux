"""Event 026 sale prices for the camp source suites.

The camp decisions, window rows, payments and refunds read
`global.black_friday_price_<category>_<key>`. This helper builds those globals
the way the production table does: it parses the Camps registrations (and the
genocide crisis prices that camp payments read) of
`black_friday_price_table_refresh_entries` and runs the production
`black_friday_price_table_quote` body through the foundation interpreter at the
requested payment ratio (basis points of `black_friday_event.ratio_basis`). A
suite that reads a price the table does not register gets a KeyError, so a
typo in a decision or effect cannot silently read zero.

`install` also serves the ratio the table holds, loads the production camp
sale helpers (the trigger-side quote mirror, the stock checks, the stock marks
and the order credit), runs hidden_effect, custom_trigger_tooltip and
hidden_trigger bodies in place, and replaces the Event 026 achievement credit
with a counter (`camp_test_black_friday_credits`) that also records the last
credited family and whether it counted a non-political payment.

Source-contract evidence only; no HOI4 engine runs.
"""
from pathlib import Path
import re

from foundation_source_tests import Runtime, parse

ROOT = Path(__file__).resolve().parents[4]
PRICE_TABLE = 'common/scripted_effects/026_black_friday_price_table_effects.txt'
BLACK_FRIDAY_CONSTANTS = 'common/script_constants/026_black_friday_constants.txt'
CAMP_CONSTANTS = 'common/script_constants/camp_repression_rework_constants.txt'
GENOCIDE_CONSTANTS = 'common/script_constants/genocide_crisis_constants.txt'
OCCUPATION_CONSTANTS = 'common/script_constants/camp_administration_occupation_constants.txt'
UNIVERSAL_COST_CONSTANTS = 'common/script_constants/chaosx_universal_cost_constants.txt'
SITE_COST_TRIGGERS = 'common/scripted_triggers/camp_repression_site_cost_triggers.txt'
REWORK_EFFECTS = 'common/scripted_effects/camp_repression_rework_effects.txt'
RATIO_BASIS = 10000
# Ordinary price, the Event 026 baseline sale, and the evolved sale.
SALE_RATIOS = (10000, 5000, 2500)
PRICE_GROUPS = ('camp_rework_cost.', 'camp_rework_equipment_cost.', 'genocide_decision_cost.', 'camp_occ_partner_response.')
CREDIT_COUNTER = 'camp_test_black_friday_credits'
TABLE_RATIO = 'global.black_friday_price_table_ratio'
SALE_HELPER_EFFECTS = ('camp_rework_mark_sale_stock_equipment', 'camp_rework_credit_sale_order')


def _constants(path, categories):
    values = {}
    for category, _, block in parse((ROOT / path).read_text(encoding='utf-8-sig')):
        if category not in categories or not isinstance(block, list):
            continue
        for key, _, value in block:
            if key != 'schema' and not isinstance(value, list):
                try:
                    values[f'{category}.{key}'] = float(value)
                except ValueError:
                    pass
    return values


def _production_effects():
    return {key: value for key, _, value in parse((ROOT / PRICE_TABLE).read_text(encoding='utf-8-sig'))
            if not key.startswith('@')}


def camp_registrations():
    """Ordered (ordinary constant, global name, quantum constant) for camp and genocide entries."""
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
                pending = amount if amount.startswith('constant:') and amount[9:].startswith(PRICE_GROUPS) else None
        elif key == 'set_variable' and isinstance(value, list) and pending is not None:
            name, _, amount = value[0]
            if amount == 'black_friday_price_payable':
                registrations.append((pending, name, quantum))
                pending = None
    return registrations


def price_constants():
    constants = _constants(BLACK_FRIDAY_CONSTANTS, {'black_friday_event'})
    constants.update(_constants(CAMP_CONSTANTS, {'camp_rework_cost', 'camp_rework_equipment_cost',
                                                 'camp_rework_mission_equipment_reserve'}))
    constants.update(_constants(GENOCIDE_CONSTANTS, {'genocide_decision_cost'}))
    constants.update(_constants(OCCUPATION_CONSTANTS, {'camp_occ_partner_response'}))
    constants.update(_constants(UNIVERSAL_COST_CONSTANTS, {'universal_cost_family', 'universal_cost_framework',
                                                           'universal_cost_fixed_point_quantum'}))
    return constants


def sale_prices(ratio_bp):
    """Map every registered camp and genocide global to its production quote at ratio_bp."""
    runtime = Runtime()
    runtime.constants.update(price_constants())
    runtime.effects['black_friday_price_table_quote'] = _production_effects()['black_friday_price_table_quote']
    runtime.scopes['TABLE'] = {'id': 'TABLE', 'flags': set(), 'arrays': {}, 'mods': set()}
    prices = {}
    for ordinary, name, quantum in camp_registrations():
        runtime.temp.clear()
        runtime.temp['black_friday_price_ratio'] = ratio_bp
        runtime.temp['black_friday_price_quantum'] = runtime.val(quantum, 'TABLE') if quantum else 0
        runtime.temp['black_friday_price_ordinary'] = runtime.val(ordinary, 'TABLE')
        runtime.run('black_friday_price_table_quote', 'TABLE')
        assert name not in prices, ('Price registered twice', name)
        prices[name] = runtime.temp['black_friday_price_payable']
    return prices


def production_quote(ordinary, ratio_bp, quantum=0):
    """The production table quote for one amount, for comparing the trigger mirror."""
    runtime = Runtime()
    runtime.constants.update(price_constants())
    runtime.effects['black_friday_price_table_quote'] = _production_effects()['black_friday_price_table_quote']
    runtime.scopes['TABLE'] = {'id': 'TABLE', 'flags': set(), 'arrays': {}, 'mods': set()}
    runtime.temp.update(black_friday_price_ratio=ratio_bp, black_friday_price_quantum=quantum,
                        black_friday_price_ordinary=ordinary)
    runtime.run('black_friday_price_table_quote', 'TABLE')
    return runtime.temp['black_friday_price_payable']


def _rewrite(block, ratio_installed):
    """Engine primitives: tooltip wrappers are AND blocks; the table ratio global exists once built."""
    out = []
    for key, op, value in block:
        if key in ('custom_trigger_tooltip', 'hidden_trigger') and isinstance(value, list):
            out.append(('AND', '=', _rewrite([item for item in value if item[0] != 'tooltip'], ratio_installed)))
        elif key == 'has_variable' and value == TABLE_RATIO:
            out.append(('always', '=', 'yes' if ratio_installed else 'no'))
        elif isinstance(value, list):
            out.append((key, op, _rewrite(value, ratio_installed)))
        else:
            out.append((key, op, value))
    return out


def install(runtime, ratio_bp=RATIO_BASIS, table_built=True):
    """Serve sale prices to an interpreter instance, load the camp sale helpers and count credits."""
    prices = sale_prices(ratio_bp)
    if table_built:
        prices[TABLE_RATIO] = ratio_bp
    runtime.black_friday_prices = prices
    runtime.black_friday_ratio = ratio_bp
    for key, value in price_constants().items():
        runtime.constants.setdefault(key, value)
    runtime.triggers.setdefault('always', [])
    for name, _, body in parse((ROOT / SITE_COST_TRIGGERS).read_text(encoding='utf-8-sig')):
        if name == 'camp_rework_sale_quote' or name.startswith(('camp_rework_can_pay_', 'camp_rework_can_start_')):
            runtime.triggers[name] = body
    rework = {name: body for name, _, body in parse((ROOT / REWORK_EFFECTS).read_text(encoding='utf-8-sig'))
              if not name.startswith('@')}
    for name in SALE_HELPER_EFFECTS:
        runtime.effects[name] = rework[name]
    runtime.effects['black_friday_price_table_quote'] = _production_effects()['black_friday_price_table_quote']
    base_value = runtime.val

    def sale_value(value, scope, previous=None):
        if isinstance(value, str) and value.startswith('global.black_friday_price_'):
            return prices[value]
        return base_value(value, scope, previous)

    runtime.val = sale_value
    base_condition = runtime.cond
    cache = {}

    def condition(block, scope, previous=None):
        entry = cache.get(id(block))
        if entry is None or entry[0] is not block:
            entry = cache[id(block)] = (block, _rewrite(block, table_built))
        return base_condition(entry[1], scope, previous)

    runtime.cond = condition
    base_execute = runtime.execute

    def execute(block, scope, previous=None):
        # Engine primitive: hidden_effect runs its body in the current scope.
        flattened = [('if', '=', [('limit', '=', [])] + value) if key == 'hidden_effect' and isinstance(value, list)
                     else (key, op, value) for key, op, value in block]
        return base_execute(flattened, scope, previous)

    runtime.execute = execute
    runtime.effects['black_friday_credit_political_power_purchase'] = [
        ('set_temp_variable', '=', [('black_friday_purchase_family_id', '=', 'constant:universal_cost_family.political_power')]),
        ('set_temp_variable', '=', [('black_friday_purchase_non_political', '=', '0')]),
        ('black_friday_credit_sale_purchase', '=', 'yes')]
    runtime.effects['black_friday_credit_sale_purchase'] = [
        ('add_to_temp_variable', '=', [(CREDIT_COUNTER, '=', '1')]),
        ('set_temp_variable', '=', [('camp_test_black_friday_last_family', '=', 'black_friday_purchase_family_id')]),
        ('set_temp_variable', '=', [('camp_test_black_friday_last_non_political', '=', 'black_friday_purchase_non_political')])]
    return prices


def credits(runtime):
    return runtime.temp.get(CREDIT_COUNTER, 0)


def last_family(runtime):
    return runtime.temp.get('camp_test_black_friday_last_family', 0)


def family(runtime, name):
    return runtime.constants['universal_cost_family.' + name]


def price(runtime, key, category='camp_rework_cost'):
    return runtime.black_friday_prices[f'global.black_friday_price_{category}_{key}']


def stock(runtime, key):
    return price(runtime, key, 'camp_rework_equipment_cost')


def decision_cost_globals(text):
    """Every native cost global a decision file reads."""
    return re.findall(r'(?m)^\t\tcost = (global\.black_friday_price_[a-z0-9_]+)\s*$', text)


CAMP_DECISION_FILES = (
    'common/decisions/camp_repression_major_country_decisions.txt',
    'common/decisions/camp_repression_colonial_country_decisions.txt',
    'common/decisions/camp_repression_generic_decisions.txt',
    'common/decisions/camp_administration_country_decisions.txt',
    'common/decisions/camp_administration_civil_decisions.txt',
    'common/decisions/camp_occ_partner_decisions.txt',
)
# Decisions whose payload credits the purchase only when the order is kept.
CREDIT_IN_EFFECT = {
    'ita_raise_colonial_security_battalions': (
        'common/scripted_effects/camp_repression_colonial_country_effects.txt',
        'camp_rework_italy_raise_security_battalions'),
}
ORDER_CREDIT = 'camp_rework_credit_sale_order'
STOCK_COMPARISON = re.compile(
    r'(has_manpower|command_power|has_fuel|has_equipment = \{ [a-z_0-9]+) [<>] '
    r'constant:camp_rework_(?:cost\.[a-z_]+_(?:manpower|command|fuel)|equipment_cost\.(?:infantry_equipment|support_equipment|motorized_equipment|trains|convoys))\b')


def _count(block, key):
    total = 0
    for name, _, value in block:
        if name == key:
            total += 1
        if isinstance(value, list):
            total += _count(value, key)
    return total


def check_native_costs():
    """Every positive native camp cost reads a registered sale price and the order credits once."""
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
                credits_here = _count(completion, ORDER_CREDIT) + _count(completion, 'black_friday_credit_political_power_purchase')
                if name in CREDIT_IN_EFFECT:
                    effect_path, effect = CREDIT_IN_EFFECT[name]
                    effects = dict((key, value) for key, _, value in parse((ROOT / effect_path).read_text(encoding='utf-8-sig')))
                    assert credits_here == 0 and _count(effects[effect], ORDER_CREDIT) == 1, name
                else:
                    assert credits_here == 1, (name, credits_here)
                paid.append(name)
    return paid


def check_stock_prices():
    """No camp purchase check compares stock with an ordinary price; AI capacity heuristics may."""
    allowed = {'common/scripted_effects/camp_repression_rework_effects.txt': {'camp_rework_apply_ai_cap'}}
    files = list(CAMP_DECISION_FILES) + [
        'common/decisions/genocide_crisis_decisions.txt',
        'common/scripted_effects/camp_repression_rework_effects.txt',
        'common/scripted_effects/camp_repression_colonial_country_effects.txt',
        'common/scripted_effects/camp_repression_major_country_effects.txt',
        'common/scripted_triggers/camp_repression_rework_triggers.txt',
        'common/scripted_triggers/camp_administration_occupation_triggers.txt',
        'common/scripted_localisation/camp_repression_ui_scripted_localisation.txt',
        'common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt',
        'common/scripted_localisation/camp_administration_country_localisation.txt',
    ]
    offenders = []
    for path in files:
        text = (ROOT / path).read_text(encoding='utf-8-sig')
        current = None
        for line in text.splitlines():
            head = re.match(r'^([A-Za-z0-9_]+) = \{', line)
            if head:
                current = head.group(1)
            if STOCK_COMPARISON.search(line.split('#', 1)[0]) and current not in allowed.get(path, set()):
                offenders.append((path, line.strip()))
    assert not offenders, offenders
    return len(files)
