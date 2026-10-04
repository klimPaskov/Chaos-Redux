"""Source-contract tests for the Event 032 incident aftermath decisions.

Deny responsibility, accelerated recovery, emergency recalibration, and debris
investigation must use their existing effects and cost keys, respect their
incident gates and once-per-incident rules, and keep the incident phase within
six visible actions. This is source evidence, not an engine simulation.
"""
from pathlib import Path
import unittest
from test_event32_recipient_scope import parse, value, descendants

ROOT = Path(__file__).resolve().parents[1]


def source(path):
    return dict(parse((ROOT / path).read_text(encoding='utf-8-sig')))


EFFECTS = source('common/scripted_effects/032_missiles_operations_effects.txt')
TRIGGERS = source('common/scripted_triggers/032_missiles_operations_triggers.txt')
DECISIONS = dict(source('common/decisions/032_missiles_decisions.txt')['missiles_program_management_category'])
AFTERMATH = {
    'missiles_deny_incident_responsibility': ('missiles_cost_deny_responsibility', 'missiles_incident_can_be_denied'),
    'missiles_accelerate_incident_recovery': ('missiles_cost_accelerate_recovery', 'missiles_incident_active'),
    'missiles_emergency_guidance_recalibration': ('missiles_cost_emergency_recalibration', 'missiles_incident_is_own_guidance_failure'),
    'missiles_investigate_debris': ('missiles_cost_investigate_debris', 'missiles_incident_debris_is_reachable'),
}


def nodes(body):
    return list(descendants(body))


class IncidentAftermath(unittest.TestCase):
    def test_decisions_use_existing_effects_costs_and_gates(self):
        for name, (cost, gate) in AFTERMATH.items():
            decision = dict(DECISIONS[name])
            with self.subTest(decision=name):
                self.assertEqual(decision['custom_cost_text'], cost)
                self.assertIn((name, 'yes'), nodes(decision['complete_effect']))
                self.assertIn(('has_country_flag', 'missiles_program_phase_incident'), decision['visible'])
                self.assertIn((gate, 'yes'), nodes(decision['visible']))
                self.assertIn('days_re_enable', decision)
                self.assertIn('ai_will_do', decision)
                self.assertTrue(decision['icon'].startswith('GFX_decision_032_missiles_'))

    def test_denial_needs_an_own_unconfirmed_neutral_accident(self):
        deny = nodes(TRIGGERS['missiles_incident_can_be_denied'])
        self.assertIn(('missiles_neutral_incident_active', 'yes'), deny)
        self.assertIn(('check_variable', [('var', 'missiles_last_incident_actor_id'), ('value', 'ROOT.id'), ('compare', 'equals')]), deny)
        self.assertIn(('NOT', [('check_variable', [('var', 'missiles_last_incident_attribution'), ('value', 'constant:missiles_attribution.confirmed'), ('compare', 'equals')])]), deny)
        decision = dict(DECISIONS['missiles_deny_incident_responsibility'])
        self.assertEqual(decision['ai_hint_pp_cost'], '@m32_pp_low')

    def test_recalibration_and_debris_need_an_own_guidance_failure(self):
        failure = nodes(TRIGGERS['missiles_incident_is_own_guidance_failure'])
        types = {dict(v)['value'] for k, v in failure if k == 'check_variable' and dict(v)['var'] == 'missiles_current_incident_type'}
        self.assertEqual(types, {f'constant:missiles_incident_type.{t}' for t in ('guidance_failure', 'neutral_accident', 'self_strike')})
        self.assertIn(('missiles_incident_is_own_guidance_failure', 'yes'), TRIGGERS['missiles_incident_debris_is_reachable'])
        recalibration = nodes(EFFECTS['missiles_emergency_guidance_recalibration'])
        self.assertTrue(any(k == 'subtract_from_variable' and 'missiles_launch_readiness' in dict(v) for k, v in recalibration))

    def test_once_per_incident_flags_reset_with_the_incident(self):
        for effect in ('missiles_close_current_incident', 'missiles_record_operation_incident'):
            body = nodes(EFFECTS[effect])
            for flag in ('missiles_incident_recovery_accelerated', 'missiles_debris_investigated'):
                self.assertIn(('clr_country_flag', flag), body, (effect, flag))
            self.assertNotIn(('clr_country_flag', 'missiles_guidance_recalibrated_next_launch'), body)
        self.assertIn(('clr_country_flag', 'missiles_guidance_recalibrated_next_launch'), nodes(EFFECTS['missiles_commit_operation']))

    def test_incident_phase_stays_within_six_actions(self):
        shown = []
        for name, body in DECISIONS.items():
            visible = list(dict(body).get('visible', []))
            if ('has_country_flag', 'missiles_program_phase_incident') not in nodes(visible):
                continue
            if ('NOT', [('missiles_incident_is_own_guidance_failure', 'yes')]) in visible:
                continue
            if ('NOT', [('has_country_flag', 'missiles_captured_site_unresolved')]) not in visible and ('has_country_flag', 'missiles_captured_site_unresolved') in visible:
                continue
            shown.append(name)
        self.assertEqual(set(shown), {
            'missiles_inspect_incident', 'missiles_compensate_neutral_victim', 'missiles_deny_incident_responsibility',
            'missiles_accelerate_incident_recovery', 'missiles_emergency_guidance_recalibration', 'missiles_investigate_debris',
        })
        self.assertLessEqual(len(shown), 6)


if __name__ == '__main__':
    unittest.main()
