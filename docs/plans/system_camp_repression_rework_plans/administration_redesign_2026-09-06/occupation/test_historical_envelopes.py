"""Dated source-coefficient envelopes, not historical reconstruction or engine execution."""
from decimal import Decimal as D, ROUND_FLOOR
from pathlib import Path
import json
import re
import unittest
from test_occupation_accounting import Cohort, constant, ROOT

COUNTRY = (ROOT / 'common/script_constants/camp_administration_country_constants.txt').read_text()
FOUNDATION = (ROOT / 'common/script_constants/camp_administration_constants.txt').read_text()
CENSUS = (ROOT / 'common/scripted_effects/camp_administration_country_census_effects.txt').read_text()

def value(source, key):
    return D(re.search(r'\b' + key + r'\s*=\s*([0-9.]+)', source)[1])

def people(k):
    return int(k * 1000)

def rounded(k):
    return (k * 1000).to_integral_value(rounding=ROUND_FLOOR) / 1000

def stock(year, month):
    key = 'ger_early_k'
    if (year, month) >= (1939, 9): key = 'ger_prewar_k'
    if (year, month) >= (1942, 9): key = 'ger_1942_k'
    if (year, month) >= (1943, 9): key = 'ger_1943_k'
    if (year, month) >= (1945, 1): key = 'ger_1945_k'
    return value(COUNTRY, key)

def custody_path(capacity, support, lifetime=True):
    live = admitted = custody_dead = labor_dead = D(0)
    history = []
    for year in range(1936, 1946):
        for month in range(1, 13):
            if (year, month) > (1945, 4): break
            bound = stock(year, month)
            remaining = max(D(0), (value(COUNTRY, 'ger_registered_lifetime_k') if lifetime else bound)-admitted)
            requested = max(D(0), bound-(live if lifetime else admitted))
            intake = min(requested, remaining, max(D(0), D(capacity)-live))
            admitted += intake
            live += intake
            assert live <= bound and live <= capacity
            custody = rounded(live * value(FOUNDATION, 'custody_monthly_rate') * (1+(1-D(support))*value(FOUNDATION, 'shortage_mortality_factor')))
            live -= custody
            # Labor-role, industry-priority maximum allocation, no killing-site or institution term.
            labor = rounded(live * value(FOUNDATION, 'workforce_share') * D(support) * value(FOUNDATION, 'labor_monthly_rate'))
            live -= labor
            custody_dead += custody
            labor_dead += labor
            history.append({'month': f'{year}-{month:02}', 'admitted_people': people(admitted), 'live_people': people(live)})
    assert admitted == live + custody_dead + labor_dead
    return {'admitted_people': people(admitted), 'released_survivors_people': people(live), 'custody_cause_people': people(custody_dead), 'labor_cause_people': people(labor_dead), 'history': history}

class HistoricalEnvelopes(unittest.TestCase):
    def test_host_addition_cannot_expand_national_stock(self):
        live = [D(350),D(350),D(0)]
        bound = D(700)
        remaining = max(D(0),bound-sum(live))
        for index, amount in enumerate(live):
            accepted = min(max(D(0),bound/len(live)-amount),remaining)
            live[index] += accepted
            remaining -= accepted
        self.assertEqual(sum(live),bound)
        self.assertIn('max = camp_admin_census_stock_remaining_k',CENSUS)

    def test_dated_nonoverlapping_origins(self):
        rows = {}
        # Whole-origin optimistic bounds, NOT exact control shares or modeled transfers.
        for origin, start, end in [('pol',(1941,7),(1945,4)), ('hol',(1941,7),(1945,4)), ('hun',(1944,3),(1945,4))]:
            c = Cohort(constant(origin)+1, constant(origin))
            for year in range(start[0], end[0]+1):
                for month in range(1,13):
                    if start <= (year,month) <= end:
                        c.pulse(year*12+month, constant('german_campaign_monthly_fraction'))
            c.close()
            self.assertTrue(c.conserved())
            rows[origin] = {'start':start,'end':end,'source_people':people(c.initial),'campaign_people':people(c.dead),'survivors_people':people(c.released)}
        RESULT['dated_origin_upper_envelopes'] = rows
        self.assertLess(rows['pol']['campaign_people'], 2770000)
        self.assertLess(rows['hun']['campaign_people'], 297621)

    def test_stock_lifetime_and_capacity(self):
        self.assertEqual([stock(*stamp) for stamp in [(1936,1),(1939,9),(1942,9),(1943,9),(1945,1)]], list(map(D,[4,21,110,224,700])))
        results = {}
        for capacity in [25,100,700]:
            for support in ['0','1']:
                label = f'capacity_{capacity}k_support_{support}'
                result = custody_path(D(capacity), support)
                old = custody_path(D(capacity), support, lifetime=False)
                self.assertLessEqual(result['admitted_people'], people(value(COUNTRY,'ger_registered_lifetime_k')))
                self.assertGreaterEqual(result['admitted_people'], old['admitted_people'])
                result.pop('history')
                result['previous_cumulative_stock_ceiling_admitted_people'] = old['admitted_people']
                results[label] = result
        RESULT['german_registered_custody_1936_01_to_1945_04'] = results

    def test_release_and_death_cannot_reset_lifetime(self):
        lifetime = value(COUNTRY,'ger_registered_lifetime_k')
        cumulative = D(0)
        for cycle in range(100):
            intake = min(D(700), max(D(0),lifetime-cumulative))
            cumulative += intake
            # Full death or release empties custody, never lifetime receipts.
        self.assertEqual(cumulative,lifetime)
        self.assertIn('camp_admin_census_national_remaining_k = camp_admin_census_lifetime_k', CENSUS)
        self.assertIn('camp_admin_admission_requested_k = camp_admin_detainees_k', CENSUS)
        self.assertIn('subtract_from_temp_variable = { camp_admin_admission_source_k = camp_occ_remaining_k }',CENSUS)

    def test_china_archival_snapshot_only_and_combined_sensitivity(self):
        # FRUS 17 Aug 1945 forwards Chu Teh's 160m occupied-area CLAIM, not a verified census.
        # One month is defensible as a dated snapshot test; 38 months is explicitly counterfactual persistence.
        results = {}
        for share in ['0.25','0.5','1']:
            for months in [1,38]:
                population = D(160000)*D(share)
                custody = value(COUNTRY,'jap_industrial_project_initial_k')
                self.assertLessEqual(custody,2*value(FOUNDATION,'capacity_per_building_k'))
                c = Cohort(population,population*constant('japan_exposure_share'),custody=custody,owner='JAP')
                custody_deaths = labor_deaths = D(0)
                for m in range(months):
                    d = rounded(c.custody*value(FOUNDATION,'custody_monthly_rate'))
                    c.custody -= d
                    labor = rounded(c.custody*value(FOUNDATION,'workforce_share')*value(FOUNDATION,'labor_monthly_rate'))
                    c.custody -= labor
                    c.pop -= d+labor
                    c.state_ledger += d+labor
                    custody_deaths += d
                    labor_deaths += labor
                    c.pulse(m,constant('japan_campaign_monthly_fraction'))
                c.close()
                self.assertEqual(population-c.pop,c.dead+custody_deaths+labor_deaths)
                self.assertTrue(c.conserved())
                results[f'direct_share_{share}_months_{months}'] = {'campaign_people':people(c.dead),'custody_people':people(custody_deaths),'labor_people':people(labor_deaths),'combined_people':people(population-c.pop),'institutional_people':0,'exposure_retired_people':people(c.removed)}
        RESULT['china_snapshot_and_explicit_persistence_sensitivities'] = results

RESULT = {'historical_total_acceptance_complete':False,'evidence':'source-linked arithmetic bounds; no engine, transfer, control-map or historical casualty reconstruction'}
if __name__ == '__main__':
    outcome = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(HistoricalEnvelopes))
    RESULT.update(tests=outcome.testsRun, failures=len(outcome.failures), errors=len(outcome.errors))
    Path(__file__).with_name('historical_envelope_results.json').write_text(json.dumps(RESULT,indent=2)+'\n')
    raise SystemExit(not outcome.wasSuccessful())
