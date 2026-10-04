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
OCCUPATION_CONSTANTS = (ROOT / 'common/script_constants/camp_administration_occupation_constants.txt').read_text()
VANILLA = Path('C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV')

def value(source, key):
    return D(re.search(r'\b' + key + r'\s*=\s*([0-9.]+)', source)[1])

def people(k):
    return int(k * 1000)

def rounded(k):
    return (k * 1000).to_integral_value(rounding=ROUND_FLOOR) / 1000

def vanilla_european_origin_inventory():
    """Read the installed starting owner and province continents used by the seed effect."""
    province_continent = {}
    for line in (VANILLA / 'map/definition.csv').read_text(encoding='utf-8-sig').splitlines():
        fields = line.split(';')
        if len(fields) >= 8 and fields[0].isdigit() and fields[7].isdigit():
            province_continent[int(fields[0])] = int(fields[7])
    inventory = {}
    mixed = []
    for path in (VANILLA / 'history/states').glob('*.txt'):
        source = path.read_text(encoding='utf-8-sig', errors='ignore')
        identity = re.search(r'\bid\s*=\s*(\d+)', source)
        owner = re.search(r'\bowner\s*=\s*([A-Z]{3})\b', source)
        population = re.search(r'\bmanpower\s*=\s*(\d+)', source)
        province_block = re.search(r'\bprovinces\s*=\s*\{([^{}]*)\}', source)
        if not all((identity, owner, population, province_block)):
            continue
        provinces = [int(token) for token in re.findall(r'\d+', province_block[1])]
        continents = {province_continent.get(province) for province in provinces}
        if continents == {1}:
            inventory.setdefault(owner[1].lower(), []).append((int(identity[1]), int(population[1])))
        elif 1 in continents:
            mixed.append(int(identity[1]))
    for rows in inventory.values():
        rows.sort()
    return inventory, sorted(mixed)


def staged_direct_control_rows(selected):
    """Model only the declared full-month GER-controller windows and one campaign cause."""
    inventory, _ = vanilla_european_origin_inventory()
    selected_ids = [state_id for _, state_id, _, _ in selected]
    assert len(selected_ids) == len(set(selected_ids))
    rows = []
    for origin, state_id, start, end in selected:
        states = dict(inventory[origin])
        assert state_id in states
        origin_population = sum(states.values())
        state_population = states[state_id]
        allocated_people = int(D(state_population) * constant(origin) * 1000 / D(origin_population))
        cohort = Cohort(D(state_population) / 1000, D(allocated_people) / 1000)
        for year in range(start[0], end[0] + 1):
            for month in range(1, 13):
                if start <= (year, month) <= end:
                    cohort.pulse(year * 12 + month, constant('german_campaign_monthly_fraction'))
        cohort.close()
        after_control = cohort.dead
        cohort.pulse(1946 * 12 + 1, constant('german_campaign_monthly_fraction'))
        assert cohort.dead == after_control
        assert cohort.conserved()
        assert cohort.projection == cohort.dead
        assert cohort.receipts == (end[0] - start[0]) * 12 + end[1] - start[1] + 1
        rows.append({
            'origin': origin.upper(),
            'state_id': state_id,
            'initial_state_population_people': state_population,
            'apportioned_source_people': allocated_people,
            'assumed_direct_control_first_month': f'{start[0]}-{start[1]:02}',
            'assumed_direct_control_last_month': f'{end[0]}-{end[1]:02}',
            'campaign_violence_people': people(cohort.dead),
            'survivors_at_control_end_people': people(cohort.released),
            'accepted_campaign_receipts': cohort.receipts,
            'custody_or_arrival_violence_people': 0,
            'unattributed_outside_losses_people': people(cohort.removed),
        })
    return rows


NINE_STAGED_CONTROL_WINDOWS = [
    ('pol', 87, (1941, 7), (1944, 12)),
    ('pol', 88, (1941, 7), (1944, 12)),
    ('hol', 7, (1941, 7), (1945, 4)),
    ('bel', 6, (1941, 7), (1944, 8)),
    ('fra', 16, (1941, 7), (1944, 7)),
    ('sov', 206, (1941, 7), (1944, 5)),
    ('lit', 11, (1941, 7), (1944, 6)),
    ('lat', 808, (1941, 7), (1944, 9)),
    ('gre', 731, (1941, 7), (1944, 9)),
]

def arrival_sensitivity(source_people, resident_places, monthly_throughput, arrival_fraction, support=1, deaths_enabled=True, control=True, months=2):
    """Independent arithmetic envelope for exact living waves and measured destination losses."""
    living = source_people
    custody = moved = dead = batches = 0
    if not control:
        return {'moved': 0, 'arrival_dead': 0, 'custody': 0, 'living_source': living, 'batches': 0}
    max_batches = int(value((ROOT / 'common/script_constants/camp_administration_occupation_constants.txt').read_text().split('camp_occ_arrival = {', 1)[1], 'max_batches_per_month'))
    for _ in range(months):
        throughput_left = int(D(monthly_throughput) * D(support))
        for _ in range(max_batches):
            request = min(living, resident_places - custody, throughput_left)
            if request <= 0:
                break
            living -= request
            moved += request
            custody += request
            throughput_left -= request
            actual = int(D(request) * D(arrival_fraction)) if deaths_enabled else 0
            custody -= actual
            dead += actual
            batches += 1
    assert source_people == living + custody + dead
    return {'moved': moved, 'arrival_dead': dead, 'custody': custody, 'living_source': living, 'batches': batches}

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
    def test_all_seeded_european_origins_have_state_identity(self):
        constants = OCCUPATION_CONSTANTS.split('camp_occ_origin_k = {', 1)[1].split('\n}', 1)[0]
        origins = {tag: D(amount) for tag, amount in re.findall(r'(?m)^\s*([a-z]{3})\s*=\s*([0-9.]+)\s*$', constants)}
        self.assertEqual(len(origins), 21)
        inventory, mixed = vanilla_european_origin_inventory()
        rows = {}
        for tag, ceiling_k in origins.items():
            states = inventory.get(tag, [])
            self.assertTrue(states, f'No installed European starting states for {tag}')
            total_population = sum(population for _, population in states)
            self.assertGreater(total_population, 0)
            rows[tag] = {
                'starting_owner': tag.upper(),
                'seed_ceiling_people': int(ceiling_k * 1000),
                'initial_european_population': total_population,
                'initial_european_state_ids': [state_id for state_id, _ in states],
                'german_occupation_admission': 'excluded_home_origin' if tag == 'ger' else 'requires_current_GER_control_radical_authority_and_headroom',
                'controller_by_month': 'not established by initial-owner files',
            }
        self.assertIn(87, rows['pol']['initial_european_state_ids'])
        self.assertIn(88, rows['pol']['initial_european_state_ids'])
        self.assertEqual(rows['ger']['german_occupation_admission'], 'excluded_home_origin')
        RESULT['all_seeded_origin_initial_european_inventory'] = {
            'rows': rows,
            'cross_continent_state_ids_requiring_map_review': mixed,
            'total_seed_ceiling_people': sum(row['seed_ceiling_people'] for row in rows.values()),
            'limit': 'Installed vanilla starting ownership and province-continent inventory; no 1939-1945 controller path or population receipt',
        }

    def test_dated_lodz_to_krakow_cause_and_capacity_envelope(self):
        # Explicit GER control of states 87/88 from July 1941, one supported
        # killing-center level with no prior custody, and no outside loss.
        # This is a source-linked control sensitivity, not a reconstructed transport.
        vanilla_states = Path('C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states')
        owned_pol = {}
        for path in vanilla_states.glob('*.txt'):
            source = path.read_text(encoding='utf-8-sig', errors='ignore')
            owner = re.search(r'\bowner\s*=\s*([A-Z]{3})\b', source)
            state_id = re.search(r'\bid\s*=\s*(\d+)', source)
            population = re.search(r'\bmanpower\s*=\s*(\d+)', source)
            if owner and owner[1] == 'POL' and state_id and population:
                owned_pol[int(state_id[1])] = int(population[1])
        self.assertIn(87, owned_pol)
        state_88_source = next(v for p in vanilla_states.glob('88-*.txt') for v in [p.read_text(encoding='utf-8-sig', errors='ignore')])
        destination_population = int(re.search(r'\bmanpower\s*=\s*(\d+)', state_88_source)[1])
        source_population = owned_pol[87]
        initial_physical = source_population + destination_population
        origin_ceiling_people = int(constant('pol') * 1000)
        initial_exposure = int(D(origin_ceiling_people) * D(source_population) / D(sum(owned_pol.values())))
        living = initial_exposure
        campaign_deaths = transferred = arrival_deaths = custody_deaths = killing_deaths = 0
        site_capacity = int(value(FOUNDATION, 'capacity_per_building_k') * 1000)
        campaign_fraction = constant('german_campaign_monthly_fraction')
        dated_share = constant('lodz_auschwitz_living_share')
        arrival_fraction = value((ROOT / 'common/script_constants/camp_administration_occupation_constants.txt').read_text().split('camp_occ_arrival = {', 1)[1], 'violence_request_fraction')
        throughput = int(value((ROOT / 'common/script_constants/camp_administration_occupation_constants.txt').read_text().split('camp_occ_arrival = {', 1)[1], 'throughput_per_supported_level_k') * 1000)
        max_batches = int(value((ROOT / 'common/script_constants/camp_administration_occupation_constants.txt').read_text().split('camp_occ_arrival = {', 1)[1], 'max_batches_per_month'))
        custody_rate = value(FOUNDATION, 'custody_monthly_rate')
        killing_rate = value(FOUNDATION, 'violence_monthly_rate')
        destination_custody = 0
        pending = None
        batch_count = 0
        august_source = None
        dated_months = []
        for year in range(1941, 1945):
            for month in range(1, 13):
                if (year, month) < (1941, 7) or (year, month) > (1944, 9):
                    continue
                # The integration recipient runs funded foundation site mortality
                # before occupation transfers in each month.
                if (year, month) == (1944, 9):
                    custody_deaths = int(D(destination_custody) * custody_rate)
                    destination_custody -= custody_deaths
                    killing_deaths = int(D(destination_custody) * killing_rate)
                    destination_custody -= killing_deaths
                    destination_population -= custody_deaths + killing_deaths
                if (year, month) in ((1944, 8), (1944, 9)):
                    prior_moved = transferred
                    prior_arrival = arrival_deaths
                    if pending is None:
                        august_source = living
                        pending = int(D(living) * dated_share)
                    monthly_throughput = throughput
                    for _ in range(max_batches):
                        request = min(pending, monthly_throughput, site_capacity - destination_custody, living)
                        if request <= 0:
                            break
                        living -= request
                        pending -= request
                        monthly_throughput -= request
                        transferred += request
                        source_population -= request
                        destination_population += request
                        destination_custody += request
                        # A death is recorded only after the exact living movement binds its destination row.
                        actual_arrival = min(int(D(request) * arrival_fraction), destination_custody)
                        destination_custody -= actual_arrival
                        destination_population -= actual_arrival
                        arrival_deaths += actual_arrival
                        batch_count += 1
                loss = int(D(living) * campaign_fraction)
                living -= loss
                source_population -= loss
                campaign_deaths += loss
                if (year, month) in ((1944, 8), (1944, 9)):
                    dated_months.append({'month': f'{year}-{month:02}', 'living_transfer_people': transferred - prior_moved,
                                         'arrival_violence_people': arrival_deaths - prior_arrival,
                                         'source_campaign_violence_people': loss})
        self.assertGreater(transferred, 0)
        self.assertLessEqual(transferred, throughput * 2)
        self.assertLessEqual(batch_count, max_batches * 2)
        self.assertEqual(initial_exposure, living + campaign_deaths + arrival_deaths + destination_custody + custody_deaths + killing_deaths)
        self.assertEqual(initial_physical, source_population + destination_population + campaign_deaths + arrival_deaths + custody_deaths + killing_deaths)
        RESULT['lodz_1941_07_to_1944_09_control_sensitivity'] = {
            'assumed_control': 'GER controls states 87 and 88 from July 1941 through September 1944',
            'assumed_site': 'one supported killing-center level in state 88; zero prior custody; no outside losses',
            'source_initial_people': initial_exposure,
            'source_campaign_violence_people': campaign_deaths,
            'living_transfer_people': transferred,
            'destination_arrival_violence_people': arrival_deaths,
            'destination_custody_cause_people': custody_deaths,
            'destination_killing_cause_people': killing_deaths,
            'source_survivors_people': living,
            'destination_transfer_survivors_people': destination_custody,
            'source_transport_reference_people': 67000,
            'transport_gap_people': 67000 - transferred,
            'arrival_reference_people': 44000,
            'arrival_gap_people': 44000 - arrival_deaths,
            'transfer_batches': batch_count,
            'unmoved_pending_people': pending,
            'dated_months': dated_months,
        }
        isolated = {
            f'{fraction:.2f}': arrival_sensitivity(august_source, site_capacity, throughput, fraction)
            for fraction in (D('0.55'), D('0.65'), D('0.75'))
        }
        self.assertLess(isolated['0.55']['arrival_dead'], isolated['0.65']['arrival_dead'])
        self.assertLess(isolated['0.65']['arrival_dead'], isolated['0.75']['arrival_dead'])
        suspended = arrival_sensitivity(august_source, site_capacity, throughput, arrival_fraction, support=0)
        disabled = arrival_sensitivity(august_source, site_capacity, throughput, arrival_fraction, deaths_enabled=False)
        absent_control = arrival_sensitivity(august_source, site_capacity, throughput, arrival_fraction, control=False)
        self.assertEqual((suspended['moved'], absent_control['moved']), (0, 0))
        self.assertEqual(disabled['moved'], disabled['custody'])
        self.assertEqual(disabled['arrival_dead'], 0)
        self.assertLessEqual(disabled['moved'], site_capacity)
        RESULT['lodz_isolated_arrival_sensitivity'] = {
            'august_living_source_people': august_source,
            'fractions': isolated,
            'unsupported': suspended,
            'deaths_disabled': disabled,
            'no_control': absent_control,
            'limit': 'Isolated arithmetic bounds with no campaign attrition or ordinary monthly custody loss; not engine execution',
        }

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

    def test_staged_direct_control_state_sensitivity(self):
        # These nine state windows are deliberately narrower than the historical
        # country occupations. They stage direct GER control at the monthly tick,
        # which is not established by installed starting-owner files or a save.
        selected = NINE_STAGED_CONTROL_WINDOWS
        rows = staged_direct_control_rows(selected)
        self.assertEqual(len(rows), 9)
        self.assertLess(sum(row['apportioned_source_people'] for row in rows), 8539960)
        self.assertEqual(sum(row['apportioned_source_people'] for row in rows),
                         sum(row['campaign_violence_people'] + row['survivors_at_control_end_people'] for row in rows))
        RESULT['staged_nine_state_direct_control_sensitivity'] = {
            'scenario_kind': 'historically dated partial-state direct-control sensitivity, not game-controller evidence',
            'rows': rows,
            'total_apportioned_source_people': sum(row['apportioned_source_people'] for row in rows),
            'total_campaign_violence_people': sum(row['campaign_violence_people'] for row in rows),
            'total_survivors_at_control_end_people': sum(row['survivors_at_control_end_people'] for row in rows),
            'total_accepted_campaign_receipts': sum(row['accepted_campaign_receipts'] for row in rows),
            'historical_reconstruction': False,
            'engine_controller_or_population_receipt': False,
        }

    def test_four_additional_staged_direct_control_states(self):
        # Bounded protectorate and military-control probes. Direct HOI4
        # controllers, outside losses and destination deaths remain unknown.
        selected = [
            ('nor', 110, (1941, 7), (1945, 4)),
            ('cze', 9, (1941, 7), (1945, 4)),
            ('cze', 75, (1941, 7), (1945, 4)),
            ('yug', 108, (1941, 7), (1944, 8)),
        ]
        rows = staged_direct_control_rows(selected)
        self.assertEqual(len(rows), 4)
        self.assertEqual(sum(row['accepted_campaign_receipts'] for row in rows), 176)
        self.assertEqual(sum(row['apportioned_source_people'] for row in rows),
                         sum(row['campaign_violence_people'] + row['survivors_at_control_end_people'] for row in rows))
        self.assertTrue(all(row['custody_or_arrival_violence_people'] == 0 and row['unattributed_outside_losses_people'] == 0 for row in rows))
        RESULT['staged_four_additional_state_direct_control_sensitivity'] = {
            'scenario_kind': 'historically bounded supplementary direct-control sensitivity, not game-controller evidence',
            'rows': rows,
            'total_apportioned_source_people': sum(row['apportioned_source_people'] for row in rows),
            'total_campaign_violence_people': sum(row['campaign_violence_people'] for row in rows),
            'total_survivors_at_control_end_people': sum(row['survivors_at_control_end_people'] for row in rows),
            'total_accepted_campaign_receipts': sum(row['accepted_campaign_receipts'] for row in rows),
            'historical_reconstruction': False,
            'engine_controller_or_population_receipt': False,
        }
        earlier = staged_direct_control_rows(NINE_STAGED_CONTROL_WINDOWS)
        self.assertFalse({row['state_id'] for row in earlier} & {row['state_id'] for row in rows})
        combined = earlier + rows
        self.assertEqual(sum(row['apportioned_source_people'] for row in combined),
                         sum(row['campaign_violence_people'] + row['survivors_at_control_end_people'] for row in combined))
        RESULT['staged_thirteen_state_disjoint_source_subtotal'] = {
            'scenario_kind': 'disjoint staged state subtotal for occupation cause only; excludes the rejected Denmark control',
            'state_ids': [row['state_id'] for row in combined],
            'total_apportioned_source_people': sum(row['apportioned_source_people'] for row in combined),
            'total_campaign_violence_people': sum(row['campaign_violence_people'] for row in combined),
            'total_survivors_at_control_end_people': sum(row['survivors_at_control_end_people'] for row in combined),
            'total_accepted_campaign_receipts': sum(row['accepted_campaign_receipts'] for row in combined),
            'historical_reconstruction': False,
            'engine_controller_or_population_receipt': False,
        }

    def test_denmark_no_rescue_counterfactual_is_not_historical_acceptance(self):
        # The generic GER campaign would start in 1941 and has no 1943 rescue
        # movement; use these direct-control rows only to expose that defect.
        selected = [
            ('den', 37, (1941, 7), (1945, 4)),
            ('den', 99, (1941, 7), (1945, 4)),
        ]
        rows = staged_direct_control_rows(selected)
        self.assertEqual(len(rows), 2)
        self.assertEqual(sum(row['accepted_campaign_receipts'] for row in rows), 92)
        self.assertEqual(sum(row['apportioned_source_people'] for row in rows),
                         sum(row['campaign_violence_people'] + row['survivors_at_control_end_people'] for row in rows))
        RESULT['rejected_denmark_no_rescue_counterfactual'] = {
            'scenario_kind': 'negative control: generic direct-GER campaign without Denmark rescue or policy exception',
            'rows': rows,
            'total_apportioned_source_people': sum(row['apportioned_source_people'] for row in rows),
            'total_campaign_violence_people': sum(row['campaign_violence_people'] for row in rows),
            'total_survivors_at_control_end_people': sum(row['survivors_at_control_end_people'] for row in rows),
            'total_accepted_campaign_receipts': sum(row['accepted_campaign_receipts'] for row in rows),
            'historical_reconstruction': False,
            'accepted_historical_sensitivity': False,
            'engine_controller_or_population_receipt': False,
        }

    def test_all_foreign_origins_counterfactual_upper_envelope(self):
        # Deliberately impossible as a historical controller series: every
        # non-German seeded origin is treated as fully GER controlled for all
        # months after the campaign opens, with no outside or custody debit.
        constants = OCCUPATION_CONSTANTS.split('camp_occ_origin_k = {', 1)[1].split('\n}', 1)[0]
        origins = {tag: D(amount) for tag, amount in re.findall(r'(?m)^\s*([a-z]{3})\s*=\s*([0-9.]+)\s*$', constants)}
        rows = {}
        for tag, amount_k in origins.items():
            if tag == 'ger':
                continue
            cohort = Cohort(amount_k + 1, amount_k)
            for year in range(1941, 1946):
                for month in range(1, 13):
                    if (1941, 7) <= (year, month) <= (1945, 4):
                        cohort.pulse(year * 12 + month, constant('german_campaign_monthly_fraction'))
            cohort.close()
            self.assertTrue(cohort.conserved())
            rows[tag] = {'source_people': people(cohort.initial), 'campaign_people': people(cohort.dead),
                         'survivors_people': people(cohort.released)}
        self.assertEqual(len(rows), 20)
        self.assertEqual(sum(row['source_people'] for row in rows.values()), 8539960)
        RESULT['all_foreign_origins_counterfactual_full_control'] = {
            'assumption': 'GER controls every seeded foreign European origin from 1941-07 through 1945-04, including countries it never occupied; no outside deaths, custody, or movement',
            'rows': rows,
            'total_source_people': sum(row['source_people'] for row in rows.values()),
            'total_campaign_people': sum(row['campaign_people'] for row in rows.values()),
            'historical_reconstruction': False,
        }

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

    def test_five_installed_direct_japan_control_states(self):
        # Installed state histories establish direct JAP control from 1938-10-25.
        # The later endpoint is a bounded continuity assumption, not a province-level
        # archival controller series or a Pingfang institutional-death estimate.
        selected = {
            608: '608-Beijing.txt',
            1035: '1035 - Nanjing.txt',
            597: '597-shandong.txt',
            598: '598-Jiansu.txt',
            743: '743-Qingdao.txt',
        }
        rows = []
        for state_id, filename in selected.items():
            source = (VANILLA / 'history/states' / filename).read_text(encoding='utf-8-sig', errors='ignore')
            self.assertEqual(int(re.search(r'\bid\s*=\s*(\d+)', source)[1]), state_id)
            self.assertEqual(re.search(r'\bowner\s*=\s*([A-Z]{3})', source)[1], 'CHI')
            self.assertRegex(source, r'1938\.10\.25\s*=\s*\{[^{}]*\bcontroller\s*=\s*JAP\b')
            population = int(re.search(r'\bmanpower\s*=\s*(\d+)', source)[1])
            cohort = Cohort(D(population) / 1000,
                            D(population) * constant('japan_exposure_share') / 1000,
                            owner='JAP')
            for year in range(1938, 1946):
                for month in range(1, 13):
                    if (1938, 11) <= (year, month) <= (1945, 7):
                        cohort.pulse(year * 12 + month,
                                     constant('japan_campaign_monthly_fraction'), actor='JAP')
            cohort.close()
            before_postwindow = cohort.dead
            cohort.pulse(1945 * 12 + 8, constant('japan_campaign_monthly_fraction'), actor='JAP')
            self.assertEqual(cohort.dead, before_postwindow)
            self.assertTrue(cohort.conserved())
            self.assertEqual(cohort.dead, cohort.projection)
            self.assertEqual(cohort.receipts, 81)
            self.assertEqual(people(cohort.initial), people(cohort.dead) + people(cohort.released))
            rows.append({
                'state_id': state_id,
                'initial_vanilla_population_people': population,
                'registered_exposure_people': people(cohort.initial),
                'sourced_first_full_month': '1938-11',
                'assumed_last_full_month': '1945-07',
                'occupation_violence_people': people(cohort.dead),
                'survivors_at_control_end_people': people(cohort.released),
                'accepted_source_model_receipts': cohort.receipts,
                'custody_or_labor_people': 0,
                'pingfang_institutional_people': 0,
                'outbreak_people': 0,
            })
        self.assertNotIn(328, selected)  # Kirin/Pingfang is MAN subject territory.
        self.assertEqual(sum(row['accepted_source_model_receipts'] for row in rows), 405)
        self.assertEqual(sum(row['registered_exposure_people'] for row in rows),
                         sum(row['occupation_violence_people'] + row['survivors_at_control_end_people'] for row in rows))
        RESULT['japan_five_installed_direct_control_state_sensitivity'] = {
            'scenario_kind': 'installed 1938-10-25 direct-JAP state-history start with bounded control-continuity assumption through 1945-07',
            'rows': rows,
            'total_initial_vanilla_population_people': sum(row['initial_vanilla_population_people'] for row in rows),
            'total_registered_exposure_people': sum(row['registered_exposure_people'] for row in rows),
            'total_occupation_violence_people': sum(row['occupation_violence_people'] for row in rows),
            'total_survivors_at_control_end_people': sum(row['survivors_at_control_end_people'] for row in rows),
            'total_accepted_source_model_receipts': sum(row['accepted_source_model_receipts'] for row in rows),
            'pingfang_state_328_included': False,
            'historical_reconstruction': False,
            'accepted_historical_sensitivity': False,
            'engine_controller_or_population_receipt': False,
        }

RESULT = {'historical_total_acceptance_complete':False,'evidence':'source-linked arithmetic bounds; no engine receipt, combined transfer/control matrix or historical casualty reconstruction'}
if __name__ == '__main__':
    outcome = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(HistoricalEnvelopes))
    RESULT.update(tests=outcome.testsRun, failures=len(outcome.failures), errors=len(outcome.errors))
    Path(__file__).with_name('historical_envelope_results.json').write_text(json.dumps(RESULT,indent=2)+'\n')
    raise SystemExit(not outcome.wasSuccessful())
