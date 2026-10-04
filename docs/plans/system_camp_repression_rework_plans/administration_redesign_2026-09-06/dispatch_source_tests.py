"""Check the bounded camp timer wiring and model its calendar-month guard.

This is source and deterministic calendar evidence, not Clausewitz execution.
Run from the mod root with python <this file>.
"""
from datetime import date, timedelta
from pathlib import Path
import json

from foundation_source_tests import get, parse


ROOT = Path(__file__).resolve().parents[4]


def contains(block, key, value):
    return any((name == key and item == value) or
               (isinstance(item, list) and contains(item, key, value))
               for name, _, item in block)


def source_contract():
    effects = parse((ROOT / 'common/scripted_effects/camp_repression_rework_effects.txt').read_text(encoding='utf-8-sig'))
    events = parse((ROOT / 'events/camp_administration_country_events.txt').read_text(encoding='utf-8-sig'))
    constants = parse((ROOT / 'common/script_constants/camp_administration_dispatch_constants.txt').read_text(encoding='utf-8-sig'))
    integration = parse((ROOT / 'common/scripted_effects/camp_administration_integration_effects.txt').read_text(encoding='utf-8-sig'))
    triggers = parse((ROOT / 'common/scripted_triggers/camp_repression_rework_triggers.txt').read_text(encoding='utf-8-sig'))
    initializer = get(effects, 'camp_rework_initialize_eligible_country_variables')
    register = get(effects, 'camp_rework_register_country_for_monthly_pulse')
    ensure_timer = get(effects, 'camp_rework_ensure_country_timer')
    schedule = get(effects, 'camp_rework_schedule_country_timer')
    close_country = get(integration, 'camp_admin_integration_close_country')
    integration_triggers = parse((ROOT / 'common/scripted_triggers/camp_administration_integration_triggers.txt').read_text(encoding='utf-8-sig'))
    timer_due = get(integration_triggers, 'camp_admin_dispatch_timer_is_due')
    cleanup = get(effects, 'camp_rework_clean_inactive_countries')
    registry_work = get(triggers, 'camp_rework_country_has_registry_work')
    event = next(value for key, _, value in events if key == 'country_event' and get(value, 'id') == 'camp_administration_country.2')
    period = int(get(get(constants, 'camp_admin_dispatch'), 'period_days'))
    tolerance = int(get(get(constants, 'camp_admin_dispatch'), 'due_tolerance_days'))
    assert 0 < period < 29 and 0 < tolerance < period
    assert get(event, 'hidden') == 'yes' and get(event, 'is_triggered_only') == 'yes'
    assert contains(initializer, 'camp_rework_ensure_country_timer', 'yes')
    assert contains(register, 'camp_rework_ensure_country_timer', 'yes')
    assert contains(ensure_timer, 'set_country_flag', 'camp_admin_dispatch_timer_active')
    assert contains(ensure_timer, 'camp_rework_schedule_country_timer', 'yes')
    assert contains(schedule, 'id', 'camp_administration_country.2')
    assert contains(schedule, 'days', 'constant:camp_admin_dispatch.period_days')
    assert contains(schedule, 'chaosx_convert_days_to_date_offset', 'yes')
    assert contains(schedule, 'subtract_from_temp_variable', [('chaosx_date_days', '=', 'constant:camp_admin_dispatch.due_tolerance_days')])
    assert contains(schedule, 'set_variable', [('camp_admin_dispatch_timer_earliest', '=', 'global.date')])
    # Annexation and special-country exclusion share this terminal cleanup.
    assert contains(close_country, 'clr_country_flag', 'camp_admin_dispatch_timer_active')
    assert contains(close_country, 'clear_variable', 'camp_admin_dispatch_timer_earliest')
    assert contains(timer_due, 'has_variable', 'camp_admin_dispatch_timer_earliest')
    assert contains(get(effects, 'camp_rework_on_country_annexed'), 'camp_admin_integration_close_country', 'yes')
    assert contains(get(effects, 'camp_rework_exclude_special_country'), 'camp_admin_integration_close_country', 'yes')
    assert contains(cleanup, 'camp_rework_country_has_registry_work', 'yes')
    for gate in ('has_active_camp_network', 'has_visible_camp_reform_work',
                 'camp_rework_country_has_focus_hook_watch', 'camp_admin_integration_has_continuing_work'):
        assert contains(registry_work, gate, 'yes')
    assert contains(registry_work, 'has_country_flag', 'camp_repression_ledger_open')
    assert contains(event, 'camp_rework_country_is_eligible', 'yes')
    assert contains(event, 'array', 'global.camp_repression_active_countries')
    assert contains(event, 'camp_admin_integration_monthly_country_recipient', 'yes')
    assert contains(event, 'camp_rework_country_has_registry_work', 'yes')
    assert contains(event, 'remove_from_array', [('array', '=', 'global.camp_repression_active_countries'), ('value', '=', 'THIS')])
    assert contains(event, 'camp_rework_exclude_special_country', 'yes')
    assert contains(event, 'clr_country_flag', 'camp_admin_dispatch_timer_active')
    assert contains(event, 'camp_rework_schedule_country_timer', 'yes')
    assert contains(event, 'camp_admin_dispatch_timer_is_due', 'yes')
    recipient = get(integration, 'camp_admin_integration_monthly_country_recipient')
    assert contains(recipient, 'camp_admin_integration_month', 'camp_admin_month_key')
    assert contains(recipient, 'camp_admin_monthly_country', 'yes')
    return period, tolerance


def annexation_scenario(period, tolerance, start, annexed, released, end):
    """Model the timer flag, the stored earliest date and stale events.

    The pending event from before annexation is kept and still delivered (the
    worst case), so the guard rather than engine cleanup must stop it.
    """
    pending = [start + timedelta(days=period)]
    flag, earliest = True, start + timedelta(days=period - tolerance)
    last_month, paid, stale_stops = None, [], 0
    day = start
    while day <= end:
        exists = not (annexed <= day < released)
        if day == annexed:
            flag, earliest = False, None          # camp_admin_integration_close_country
        if day == released:
            flag = True                           # registration: camp_rework_ensure_country_timer
            earliest = day + timedelta(days=period - tolerance)
            pending.append(day + timedelta(days=period))
        for due in [d for d in pending if d == day]:
            pending.remove(due)
            if not exists:
                continue
            if flag and earliest is not None and day < earliest:
                stale_stops += 1                  # stale chain stops, current chain untouched
                continue
            if flag:
                key = (day.year, day.month)
                if key != last_month:
                    last_month = key
                    paid.append(key)
                earliest = day + timedelta(days=period - tolerance)
                pending.append(day + timedelta(days=period))
            else:
                earliest = None
        assert len(pending) <= 2
        day += timedelta(days=1)
    assert len(paid) == len(set(paid))
    return {'paid_months': len(paid), 'stale_events_stopped': stale_stops, 'outstanding_timers': len(pending)}


def calendar_scenario(start, end, period, global_dispatch, stop=None, responsibility_end=None):
    """Model the recipient's persisted month key under both dispatch paths."""
    next_timer = start + timedelta(days=period)
    last_month = None
    paid_months = []
    timer_events = 0
    timer_active = True
    day = start
    while day <= end:
        registered = stop is None or day < stop
        if registered and global_dispatch and day.day == 1:
            key = (day.year, day.month)
            if key != last_month:
                last_month = key
                paid_months.append(key)
        if timer_active and day == next_timer:
            timer_events += 1
            if not registered:
                timer_active = False
            else:
                key = (day.year, day.month)
                if key != last_month:
                    last_month = key
                    paid_months.append(key)
                if responsibility_end is not None and day >= responsibility_end:
                    timer_active = False
                else:
                    next_timer = day + timedelta(days=period)
        day += timedelta(days=1)
    assert len(paid_months) == len(set(paid_months))
    return {'paid_months': len(paid_months), 'timer_events': timer_events}


def main():
    period, tolerance = source_contract()
    cases = {
        'disabled_1938_full_year': calendar_scenario(date(1938, 1, 1), date(1938, 12, 31), period, False),
        'enabled_1938_full_year': calendar_scenario(date(1938, 1, 1), date(1938, 12, 31), period, True),
        'disabled_1940_leap_year': calendar_scenario(date(1940, 1, 1), date(1940, 12, 31), period, False),
        'enabled_1940_leap_year': calendar_scenario(date(1940, 1, 1), date(1940, 12, 31), period, True),
        'disabled_after_exclusion': calendar_scenario(date(1938, 1, 1), date(1938, 12, 31), period, False, date(1938, 7, 10)),
        'disabled_after_ordinary_inactivity': calendar_scenario(date(1938, 1, 1), date(1938, 12, 31), period, False,
                                                               responsibility_end=date(1938, 7, 10)),
    }
    assert all(cases[name]['paid_months'] == 12 for name in cases if 'full_year' in name or 'leap_year' in name)
    assert cases['disabled_after_exclusion']['paid_months'] == 6
    assert cases['disabled_after_exclusion']['timer_events'] == 7
    assert cases['disabled_after_ordinary_inactivity'] == {'paid_months': 7, 'timer_events': 7}
    # Annexed with a timer pending, then re-released before it would fire.
    early = annexation_scenario(period, tolerance, date(1938, 1, 1), date(1938, 3, 5), date(1938, 3, 12), date(1938, 12, 31))
    assert early['stale_events_stopped'] == 1 and early['outstanding_timers'] == 1
    cases['annexed_then_released_before_stale_event'] = early
    # Re-released after the stale event would have fired.
    late = annexation_scenario(period, tolerance, date(1938, 1, 1), date(1938, 3, 5), date(1938, 6, 1), date(1938, 12, 31))
    assert late['stale_events_stopped'] == 0 and late['outstanding_timers'] == 1
    cases['annexed_then_released_after_stale_event'] = late
    print(json.dumps({'status': 'passed', 'period_days': period, 'scenarios': cases,
                      'limit': 'Calendar model and parsed source only; no engine event-scheduling proof.'}, indent=2))


if __name__ == '__main__':
    main()
