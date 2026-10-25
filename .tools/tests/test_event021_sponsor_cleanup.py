"""Execute the production sponsor-clear helpers against bounded country fixtures.

Native scopes, flags and variables are modeled. This does not execute HOI4,
simulate timed expiry or certify war/annexation engine behavior.
"""
from pathlib import Path
import unittest
from decimal import Decimal

from test_event021_evolution_log import parse

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'common/scripted_effects/021_random_civil_war_effects.txt'
PREFIX = 'random_civil_war_sponsor_'


class Country:
    def __init__(self, tag):
        self.tag = tag
        self.flags = set()
        self.variables = {}


class ReceiptRuntime:
    def __init__(self):
        source = dict(parse(SOURCE.read_text(encoding='utf-8-sig')))
        self.helpers = {name: source[name] for name in (
            'event021_clear_sponsor_commitment_receipt',
            'event021_clear_received_sponsor_commitment_receipt')}
        self.targets = {}
        self.calls = 0

    def matches(self, country, body):
        for key, value in body:
            if key == 'has_country_flag':
                matched = value in country.flags
            elif key == 'has_variable':
                matched = value in country.variables
            elif key == 'exists':
                matched = value == 'yes'
            elif key == 'tag':
                matched = country is self.targets[value.removeprefix('event_target:')]
            elif key.startswith('var:'):
                target = country.variables.get(key[4:])
                matched = target is not None and self.matches(target, value)
            else:
                raise AssertionError('Unhandled production trigger: ' + key)
            if not matched:
                return False
        return True

    def run(self, country, helper):
        self.calls += 1
        if self.calls > 20:
            raise AssertionError('Cleanup entered a reciprocal cycle')
        self.execute(country, self.helpers[helper])

    def execute(self, country, body):
        for key, value in body:
            if key == 'if':
                limit = next(data for name, data in value if name == 'limit')
                if self.matches(country, limit):
                    self.execute(country, [(name, data) for name, data in value if name != 'limit'])
            elif key == 'save_event_target_as':
                self.targets[value] = country
            elif key == 'clear_variable':
                country.variables.pop(value, None)
            elif key == 'clr_country_flag':
                country.flags.discard(value)
            elif key.startswith('var:'):
                target = country.variables.get(key[4:])
                if target is not None:
                    self.execute(target, value)
            elif key.startswith('event_target:'):
                self.execute(self.targets[key[13:]], value)
            elif key in self.helpers and value == 'yes':
                self.run(country, key)
            else:
                raise AssertionError('Unhandled production effect: ' + key)


def commitment(sponsor, recipient):
    sponsor.flags.add(PREFIX + 'commitment_active')
    sponsor.variables[PREFIX + 'recipient_scope'] = recipient
    sponsor.variables[PREFIX + 'recipient_id'] = recipient.tag
    recipient.flags.add(PREFIX + 'commitment_received')
    recipient.variables[PREFIX + 'scope'] = sponsor
    recipient.variables[PREFIX + 'id'] = sponsor.tag


class SponsorCleanupTests(unittest.TestCase):
    def setUp(self):
        self.runtime = ReceiptRuntime()
        self.sponsor = Country('ENG')
        self.recipient = Country('FRA')
        commitment(self.sponsor, self.recipient)

    def assert_closed(self):
        self.assertNotIn(PREFIX + 'commitment_active', self.sponsor.flags)
        self.assertNotIn(PREFIX + 'recipient_scope', self.sponsor.variables)
        self.assertNotIn(PREFIX + 'commitment_received', self.recipient.flags)
        self.assertNotIn(PREFIX + 'scope', self.recipient.variables)

    def test_sponsor_closes_both_ends(self):
        self.runtime.run(self.sponsor, 'event021_clear_sponsor_commitment_receipt')
        self.assert_closed()

    def test_recipient_releases_its_exact_sponsor_and_repeat_is_safe(self):
        self.runtime.run(self.recipient, 'event021_clear_sponsor_commitment_receipt')
        self.assert_closed()
        self.runtime.run(self.recipient, 'event021_clear_sponsor_commitment_receipt')
        self.assert_closed()

    def test_uninvolved_neighbor_does_not_cancel_source_aid(self):
        neighbor = Country('BEL')
        neighbor.variables['random_civil_war_exposure_source_country_scope'] = self.recipient
        self.runtime.run(neighbor, 'event021_clear_sponsor_commitment_receipt')
        self.assertIn(PREFIX + 'commitment_active', self.sponsor.flags)
        self.assertIs(self.recipient.variables[PREFIX + 'scope'], self.sponsor)

    def test_reciprocal_pair_cannot_recurse_forever(self):
        commitment(self.recipient, self.sponsor)
        self.runtime.run(self.sponsor, 'event021_clear_sponsor_commitment_receipt')
        self.assert_closed()
        self.assertLess(self.runtime.calls, 10)

    def test_stale_recipient_cannot_clear_a_different_current_commitment(self):
        other = Country('GER')
        commitment(self.sponsor, other)
        self.runtime.run(self.recipient, 'event021_clear_sponsor_commitment_receipt')
        self.assertIs(self.sponsor.variables[PREFIX + 'recipient_scope'], other)
        self.assertIn(PREFIX + 'commitment_active', self.sponsor.flags)
        self.assertIs(other.variables[PREFIX + 'scope'], self.sponsor)


class NewsRuntime(ReceiptRuntime):
    def __init__(self):
        super().__init__()
        source = dict(parse((ROOT / 'common/scripted_effects/021_random_civil_war_regional_response_effects.txt').read_text(encoding='utf-8-sig')))
        self.helpers['event021_emit_multifront_news_once'] = source['event021_emit_multifront_news_once']
        self.constants = dict(parse((ROOT / 'common/script_constants/021_random_civil_war_constants.txt').read_text(encoding='utf-8-sig')))
        self.arrays = {}
        self.news = []

    def value(self, country, token):
        if token.startswith('constant:'):
            category, name = token[9:].split('.', 1)
            return Decimal(dict(self.constants[category])[name])
        try:
            return Decimal(token)
        except Exception:
            return Decimal(country.variables.get(token, 0))

    def matches(self, country, body):
        for key, value in body:
            if key == 'NOT':
                matched = not self.matches(country, value)
            elif key == 'is_in_array':
                fields = dict(value)
                matched = self.value(country, fields['value']) in self.arrays.get(fields['array'], [])
            elif key == 'check_variable':
                fields = dict(value)
                left = self.value(country, fields['var'])
                right = self.value(country, fields['value'])
                if fields['compare'] == 'greater_than':
                    matched = left > right
                elif fields['compare'] == 'equals':
                    matched = left == right
                else:
                    raise AssertionError(fields['compare'])
            else:
                matched = super().matches(country, [(key, value)])
            if not matched:
                return False
        return True

    def execute(self, country, body):
        for key, value in body:
            if key == 'set_country_flag':
                country.flags.add(value)
            elif key == 'add_to_array':
                fields = dict(value)
                self.arrays.setdefault(fields['array'], []).append(self.value(country, fields['value']))
            elif key == 'news_event':
                self.news.append(dict(value)['id'])
            else:
                super().execute(country, [(key, value)])


class NewsBudgetTests(unittest.TestCase):
    def test_same_crisis_and_successor_emit_only_one_news(self):
        runtime = NewsRuntime()
        host = Country('GER')
        successor = Country('D01')
        for country in (host, successor):
            country.variables['random_civil_war_crisis_id'] = 21
        runtime.run(host, 'event021_emit_multifront_news_once')
        runtime.run(host, 'event021_emit_multifront_news_once')
        runtime.run(successor, 'event021_emit_multifront_news_once')
        self.assertEqual(runtime.news, ['chaosx.news.211'])

    def test_scenario_identity_suppresses_news_after_successor_role_change(self):
        runtime = NewsRuntime()
        successor = Country('D01')
        successor.variables['random_civil_war_crisis_id'] = 22
        successor.variables['random_civil_war_origin_kind'] = int(runtime.value(successor, 'constant:random_civil_war_origin.event006'))
        runtime.arrays['global.random_civil_war_scenario_crisis_ids'] = [Decimal(22)]
        runtime.run(successor, 'event021_emit_multifront_news_once')
        self.assertEqual(runtime.news, [])

    def test_different_regular_crises_each_emit_once(self):
        runtime = NewsRuntime()
        for identity in (21, 22):
            host = Country('GER')
            host.variables['random_civil_war_crisis_id'] = identity
            runtime.run(host, 'event021_emit_multifront_news_once')
        self.assertEqual(runtime.news, ['chaosx.news.211', 'chaosx.news.211'])


if __name__ == '__main__':
    unittest.main()
