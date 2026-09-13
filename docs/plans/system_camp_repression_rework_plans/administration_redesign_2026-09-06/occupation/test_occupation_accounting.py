"""Source-linked accounting model; not a Clausewitz interpreter or runtime proof."""
from pathlib import Path
from decimal import Decimal as D, ROUND_FLOOR
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[5]
CONSTANTS = (ROOT / 'common/script_constants/camp_administration_occupation_constants.txt').read_text()
EFFECTS = (ROOT / 'common/scripted_effects/camp_administration_occupation_effects.txt').read_text()
TRIGGERS = (ROOT / 'common/scripted_triggers/camp_administration_occupation_triggers.txt').read_text()

def constant(name):
    return D(re.search(r'\b' + name + r'\s*=\s*([0-9.]+)', CONSTANTS)[1])

class Cohort:
    def __init__(self, population, requested, custody=0, owner='GER'):
        self.pop, self.custody = D(population), D(custody)
        self.remaining = min(D(requested), max(D(0), self.pop-self.custody-constant('minimum_population_k')))
        self.initial = self.remaining
        self.owner = owner
        self.observed = self.pop
        self.state_ledger = self.observed_ledger = D(0)
        self.dead = self.removed = self.released = D(0)
        self.projection = D(0)
        self.month = None
        self.closed = False
        self.receipts = 0

    def reconcile(self):
        headroom = max(D(0), self.pop-self.custody-constant('minimum_population_k'))
        unknown = min(self.remaining, max(D(0), self.observed-self.pop, self.state_ledger-self.observed_ledger, self.remaining-headroom))
        self.remaining -= unknown
        self.removed += unknown
        self.observed = self.pop
        self.observed_ledger = self.state_ledger

    def pulse(self, month, rate, actor=None, active=True, overlap=False, engine_fraction=D(1)):
        if month == self.month:
            return
        self.month = month
        self.reconcile()
        if self.closed or not active or actor not in (None, self.owner):
            self.close()
            return
        request = min(self.remaining * D(rate), self.remaining, constant('maximum_receipt_k'))
        request = (request*1000).to_integral_value(rounding=ROUND_FLOOR)/1000
        actual = min(request, max(D(0), self.pop-self.custody-constant('minimum_population_k'))) * engine_fraction
        self.pop -= actual
        measured = self.observed-self.pop
        self.observed = self.pop
        self.remaining -= measured
        self.dead += measured
        self.projection += measured
        self.state_ledger += measured
        self.observed_ledger = self.state_ledger
        self.receipts += int(measured > 0)

    def close(self):
        if not self.closed:
            self.reconcile()
            self.released += self.remaining
            self.remaining = D(0)
            self.closed = True

    def conserved(self):
        return self.initial == self.remaining+self.dead+self.removed+self.released

class OccupationAccountingTests(unittest.TestCase):
    def test_actual_receipt_not_request(self):
        c = Cohort(1000, 500)
        c.pulse(1, D('.1'), engine_fraction=D('.8'))
        self.assertEqual(c.dead, 40)
        self.assertEqual(c.projection, 40)
        self.assertEqual(c.pop, 960)
        self.assertTrue(c.conserved())

    def test_floor_and_custody(self):
        c = Cohort(100, 200, custody=99)
        c.pulse(1, 100)
        self.assertEqual(c.pop, D('99.001'))
        self.assertEqual(c.dead, D('.999'))
        self.assertTrue(c.conserved())

    def test_outside_loss_not_authority_deaths(self):
        c = Cohort(1000, 500)
        c.pop -= 100
        c.pulse(1, 0)
        self.assertEqual(c.removed, 100)
        self.assertEqual(c.dead, 0)
        self.assertEqual(c.projection, 0)
        self.assertTrue(c.conserved())

    def test_capture_and_annexation_keep_owner(self):
        c = Cohort(1000, 500)
        c.pulse(1, D('.1'))
        c.pulse(2, D('.1'), actor='USA')
        self.assertEqual(c.owner, 'GER')
        self.assertEqual(c.dead, 50)
        self.assertEqual(c.released, 450)
        self.assertTrue(c.conserved())

    def test_double_month_and_release_no_resurrection(self):
        c = Cohort(1000, 500)
        c.pulse(1, D('.1'))
        c.pulse(1, D('.1'))
        self.assertEqual(c.receipts, 1)
        c.close()
        saved_population = c.pop
        c.pulse(2, D('.1'))
        self.assertEqual(c.pop, saved_population)
        self.assertTrue(c.conserved())

    def test_shared_occupation_and_campaign_have_distinct_receipts(self):
        c = Cohort(1000, 500)
        c.pop -= 30
        c.state_ledger += 30
        c.pulse(1, D('.1'), overlap=True)
        self.assertEqual(c.dead, 47)
        self.assertEqual(c.removed, 30)
        self.assertEqual(c.pop, 923)
        self.assertEqual(c.state_ledger, 77)
        self.assertEqual(c.projection, 47)
        self.assertTrue(c.conserved())
        self.assertNotIn('has_resistance = yes', TRIGGERS)

    def test_growth_does_not_hide_recorded_external_deaths(self):
        c = Cohort(1000, 500)
        c.pop += 10  # Thirty recorded deaths and forty arrivals/growth.
        c.state_ledger += 30
        c.pulse(1, D('.1'))
        self.assertEqual(c.removed, 30)
        self.assertEqual(c.dead, 47)
        self.assertEqual(c.pop, 963)
        self.assertTrue(c.conserved())

    def test_interleaved_core_custody_own_receipts_and_capture(self):
        c = Cohort(1000, 500, custody=100)
        c.pop -= 35
        c.custody -= 5
        c.state_ledger += 35  # Thirty core deaths, five custody receipts.
        c.pulse(1, D('.1'))
        self.assertEqual(c.dead, D('46.5'))
        c.pop -= 20
        c.state_ledger += 20
        c.pulse(1, D('.1'))  # Duplicate month must not repeat the physical debit.
        self.assertEqual(c.receipts, 1)
        c.pulse(2, D('.1'))
        self.assertEqual(c.removed, 55)
        self.assertEqual(c.dead, D('86.35'))
        c.pulse(3, D('.1'), actor='USA')
        self.assertEqual(c.owner, 'GER')
        self.assertEqual(c.dead, c.projection)
        self.assertEqual(c.pop, D('858.65'))
        self.assertTrue(c.conserved())

    def test_current_custody_shortfall_retires_exposure_without_debit(self):
        c = Cohort(1000, 500)
        c.custody = D(900)
        c.reconcile()
        self.assertEqual(c.remaining, D('99.999'))
        self.assertEqual(c.pop, 1000)
        self.assertEqual(c.dead, 0)
        self.assertTrue(c.conserved())

    def test_partial_territory_does_not_reallocate_origin(self):
        ceiling = constant('pol')
        populations = [D(10000), D(20000), D(10000)]
        shares = [ceiling*p/sum(populations) for p in populations]
        self.assertEqual(sum(shares), ceiling)
        self.assertEqual(shares[0], 750)
        self.assertLess(shares[0], ceiling)

    def test_chronology_is_source_gated(self):
        self.assertIn('date > 1937.7.6', TRIGGERS)
        self.assertIn('date > 1941.6.21', TRIGGERS)
        self.assertIn('camp_admin_mandate = 3', TRIGGERS)
        self.assertIn('camp_admin_country_regime_valid = yes', TRIGGERS)

    def test_million_scale_is_finite_not_quota(self):
        cohorts = [Cohort(10000, 9000, owner='JAP') for _ in range(10)]
        for month in range(96):
            for c in cohorts:
                c.pulse(month, constant('japan_campaign_monthly_fraction'))
        losses = sum(c.dead for c in cohorts)
        self.assertGreater(losses, 1000)
        self.assertLess(losses, 90000)
        self.assertTrue(all(c.conserved() for c in cohorts))
        RESULT['illustrative_china_100m_96_months_increment_people'] = round(float(losses*1000))

    def test_source_coverage_cannot_be_called_six_million_calibrated(self):
        entries = re.search(r'camp_occ_origin_k\s*=\s*\{(.*)\}', CONSTANTS, re.S)[1]
        ceilings = sum(D(n) for n in re.findall(r'^\s*[a-z]{3}\s*=\s*([0-9.]+)', entries, re.M))
        survivors = ceilings*(1-constant('german_campaign_monthly_fraction'))**48
        RESULT['documented_country_ceilings_people'] = int(ceilings*1000)
        RESULT['all_covered_origins_48_month_unblocked_increment_people'] = round(float((ceilings-survivors)*1000))
        RESULT['historical_six_million_calibration_complete'] = False
        self.assertLess(ceilings, 9500)
        self.assertGreater(ceilings-survivors, 1000)
        self.assertLess(ceilings-survivors, ceilings)
        # Full control without core overlap is a capacity bound, not a historical occupation path.
        self.assertLess((ceilings-survivors)/2, 6000)

    def test_documented_late_hungarian_control_and_divergent_paths(self):
        # USHMM: German occupation in March 1944. Original 1933 border ceiling, not 1944 Hungary.
        def path(share=D(1), early_reform=False):
            c = None
            for year in range(1936, 1950):
                for month in range(1, 13):
                    stamp = year*12+month
                    active = 1944*12+3 <= stamp <= 1945*12+4
                    if early_reform and stamp >= 1945*12+1:
                        active = False
                    if c is None and active:
                        c = Cohort(10000, constant('hun')*share)
                    if c is not None:
                        c.pulse(stamp, constant('german_campaign_monthly_fraction'), active=active)
            return c
        full, partial, reform = path(), path(D('.25')), path(early_reform=True)
        self.assertGreater(full.dead, reform.dead)
        self.assertLess(partial.dead, full.dead/D(3))
        self.assertTrue(all(c.closed and c.conserved() for c in (full, partial, reform)))
        RESULT['hungary_original_border_timeline_capacity_people'] = {
            'march_1944_to_april_1945': int(full.dead*1000),
            'quarter_control_same_fixed_origin': int(partial.dead*1000),
            'reform_january_1945': int(reform.dead*1000),
        }

    def test_china_full_period_with_interleaved_external_losses(self):
        # Museum-supported July 1937-August 1945 war envelope; population shares are sensitivities.
        def path(population_k, end=(1945, 8), external_people=1000):
            rows = [Cohort(D(population_k)/10, D(population_k)*constant('japan_exposure_share')/10, owner='JAP') for _ in range(10)]
            external_total = D(0)
            for year in range(1936, 1950):
                for month in range(1, 13):
                    stamp = (year, month)
                    if stamp < (1937, 7):
                        continue
                    for c in rows:
                        active = stamp <= end
                        if active:
                            external_k = D(external_people)/1000
                            c.pop -= external_k
                            c.state_ledger += external_k
                            external_total += external_k
                        c.pulse(year*12+month, constant('japan_campaign_monthly_fraction'), active=active)
            return rows, external_total
        full, outside = path(100000)
        partial, _ = path(50000)
        peace, _ = path(100000, end=(1940, 12))
        own = sum(c.dead for c in full)
        self.assertGreater(own, 1000)
        self.assertEqual(sum(c.projection for c in full), own)
        self.assertEqual(sum(c.removed for c in full), outside)
        self.assertLess(sum(c.dead for c in partial), own)
        self.assertLess(sum(c.dead for c in peace), own)
        self.assertTrue(all(c.conserved() and c.closed for c in full+partial+peace))
        RESULT['china_1937_07_1945_08_stress_scenario_people'] = {
            'campaign_attributed': int(own*1000),
            'outside_cause_unattributed_to_campaign': int(outside*1000),
            'combined_distinct_physical_losses': int((own+outside)*1000),
            'half_territory_campaign_attributed': int(sum(c.dead for c in partial)*1000),
            'peace_end_1940_campaign_attributed': int(sum(c.dead for c in peace)*1000),
            'historically_sourced_monthly_cause_split': False,
        }

    def test_single_debit_and_non_debit_projection_source(self):
        self.assertEqual(EFFECTS.count('apply_exact_state_civilian_population_loss = yes'), 1)
        self.assertEqual(EFFECTS.count('chaos_meter_register_deaths = yes'), 1)
        self.assertIn('state_civilian_population_loss_log_deaths = 0', EFFECTS)
        self.assertIn('chaos_deaths_apply_state_pop = 0', EFFECTS)
        self.assertNotIn('every_state =', EFFECTS)
        self.assertNotIn('every_country =', EFFECTS)

RESULT = {'evidence_kind': 'source-linked arithmetic model, not engine execution'}
if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(OccupationAccountingTests)
    outcome = unittest.TextTestRunner(verbosity=2).run(suite)
    RESULT.update(tests=outcome.testsRun, failures=len(outcome.failures), errors=len(outcome.errors))
    Path(__file__).with_name('accounting_results.json').write_text(json.dumps(RESULT, indent=2)+'\n')
    raise SystemExit(not outcome.wasSuccessful())
