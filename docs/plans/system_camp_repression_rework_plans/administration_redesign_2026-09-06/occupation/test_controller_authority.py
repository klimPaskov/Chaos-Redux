from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[5]
TRIGGERS = (ROOT / "common/scripted_triggers/camp_administration_occupation_triggers.txt").read_text(encoding="utf-8-sig")
SITE_TRIGGERS = (ROOT / "common/scripted_triggers/camp_administration_triggers.txt").read_text(encoding="utf-8-sig")
COUNTRY_TRIGGERS = (ROOT / "common/scripted_triggers/camp_administration_country_triggers.txt").read_text(encoding="utf-8-sig")
EFFECTS = (ROOT / "common/scripted_effects/camp_administration_occupation_effects.txt").read_text(encoding="utf-8-sig")


def block(source, key):
    start = source.index(key + " = {")
    opening = source.index("{", start)
    depth = 0
    for index in range(opening, len(source)):
        if source[index] == "{":
            depth += 1
        elif source[index] == "}":
            depth -= 1
            if depth == 0:
                return source[start:index + 1]
    raise AssertionError(f"Unclosed block: {key}")


def german_authority(controller, original_tag=None, special=False, cosmetic_tag=None):
    if original_tag == "GER":
        return True
    excluded = {"HUN", "ROM", "BUL", "SLO", "CRO", "VIC", "ITA", "FIN"}
    german_subject_controllers = {"GEN", "RKO", "RKU", "RKN", "RKB", "RKG", "RKM", "RKK", "RKT", "RKH", "POL", "NOR", "HOL", "GRE"}
    is_subject = controller == "GER_subject" or controller in german_subject_controllers
    return original_tag not in excluded and cosmetic_tag != "FRA_VICHY" and not special and is_subject


def japanese_authority(controller, china_region, core=None):
    if not china_region or core in {"MAN", "MEN"}:
        return False
    return controller in {"JAP", "JAP_subject", "RNG", "MAN", "MEN"}


class ControllerAuthorityTests(unittest.TestCase):
    def test_custody_import_into_gen_held_auschwitz_preserves_ger(self):
        from origin_observer_owner_integration_source_tests import routed_fixture, transfer
        runtime, germany, source, destination = routed_fixture()
        runtime.scopes['GEN'] = {'id': 'GEN', 'exists': True, 'original_tag': 'GEN',
                                 'overlord': 'GER', 'flags': set(), 'arrays': {}, 'mods': set()}
        destination['controller'] = 'GEN'
        before_source = source['state_population_k']
        before_destination = destination['state_population_k']
        self.assertEqual(transfer(runtime), runtime.constants['camp_occ_value.transfer_valid'])
        self.assertAlmostEqual(before_source - source['state_population_k'],
                               destination['state_population_k'] - before_destination)
        self.assertEqual(destination['camp_admin_responsible_country'], 'GER')
        self.assertTrue(all(authority == 'GER' for authority in destination['arrays']['camp_admin_row_authorities']))

    def test_control_is_tracked_before_campaign_and_registers_on_later_pulse(self):
        from danish_rescue_source_tests import world
        import datetime
        runtime = world(sweden='absent')
        germany = runtime.scopes['GER']
        germany['arrays']['camp_occ_eligible_states'] = []
        germany['flags'].discard('origin_test_campaign_eligible')
        runtime.run('camp_occ_track_controlled_state', 37)
        self.assertIn(37, germany['arrays']['camp_occ_eligible_states'])
        self.assertNotIn('camp_occ_registered', runtime.scopes[37]['flags'])
        germany['flags'].add('origin_test_campaign_eligible')
        runtime.date = datetime.date(1944, 8, 1)
        runtime.run('camp_occ_monthly_country', 'GER')
        self.assertIn('camp_occ_registered', runtime.scopes[37]['flags'])
        self.assertEqual(runtime.scopes[37]['camp_occ_responsible_country'], 'GER')

    def test_german_subject_list_and_exclusions(self):
        trigger = block(TRIGGERS, "camp_occ_country_counts_as_german_authority")
        self.assertIn("original_tag = GER", trigger)
        self.assertIn("is_subject_of = GER", trigger)
        self.assertIn("is_special_chaos_country = yes", trigger)
        for tag in ("HUN", "ROM", "BUL", "SLO", "CRO", "VIC", "ITA", "FIN"):
            self.assertIn(f"original_tag = {tag}", trigger)
        self.assertIn("has_cosmetic_tag = FRA_VICHY", trigger)
        self.assertTrue(german_authority("GEN", "GEN"))
        self.assertTrue(german_authority("RKO", "RKO"))
        self.assertTrue(german_authority("POL", "POL"))
        self.assertFalse(german_authority("HUN", "HUN"))
        self.assertFalse(german_authority("SLO", "SLO"))
        self.assertFalse(german_authority("GEN", "XYZ", special=True))
        self.assertFalse(german_authority("GEN", "XYZ", cosmetic_tag="FRA_VICHY"))
        self.assertTrue(german_authority("GER_subject", "FRA"))
        self.assertFalse(german_authority("GER_subject", "VIC"))

    def test_german_authority_consumers_keep_responsibility_with_ger(self):
        current = block(TRIGGERS, "camp_occ_state_has_current_authority")
        self.assertIn("camp_occ_state_has_german_authority = yes", current)
        registration = block(EFFECTS, "camp_occ_register_cohort")
        self.assertIn("camp_occ_state_has_german_authority = yes", registration)
        self.assertIn("set_variable = { camp_occ_responsible_country = camp_occ_source_authority }", registration)
        try_register = block(EFFECTS, "camp_occ_try_register_current_state")
        self.assertIn("set_temp_variable = { camp_occ_source_authority = GER }", try_register)
        track = block(EFFECTS, "camp_occ_track_controlled_state")
        self.assertIn("GER = {", track)
        self.assertIn("camp_occ_eligible_states", track)
        self.assertIn("camp_occ_state_has_german_authority = yes", block(SITE_TRIGGERS, "camp_admin_site_authority_is_valid"))
        self.assertIn("camp_occ_state_has_german_authority = yes", block(COUNTRY_TRIGGERS, "camp_admin_ger_krakow_setup_context"))
        self.assertIn("camp_occ_state_has_german_authority = yes", block(COUNTRY_TRIGGERS, "camp_admin_country_mengele_historical_gate"))
        legacy = (ROOT / 'common/scripted_triggers/germany_mengele_triggers.txt').read_text(encoding='utf-8-sig')
        self.assertIn('camp_occ_state_has_german_authority = yes', block(legacy, 'germany_controls_auschwitz_area'))
        self.assertIn("camp_occ_state_has_german_authority = yes", block(TRIGGERS, "camp_occ_killing_destination_active"))

    def test_registered_row_stays_open_after_handover_to_german_administration(self):
        monthly = block(EFFECTS, "camp_occ_monthly_country")
        self.assertIn("NOT = { camp_occ_state_has_current_authority = yes }", monthly)
        self.assertIn("camp_occ_close_state = yes", monthly)
        self.assertIn("camp_occ_state_has_german_authority = yes", block(TRIGGERS, "camp_occ_state_has_current_authority"))
        self.assertTrue(german_authority("GEN", "GEN"))
        self.assertTrue(german_authority("RKO", "RKO"))

    def test_exact_transfer_and_lodz_gates_accept_german_administration(self):
        destination_gate = block(TRIGGERS, "camp_occ_state_accepts_transfer_authority")
        self.assertIn("camp_occ_state_has_german_authority = yes", destination_gate)
        transfer = block(EFFECTS, "camp_occ_transfer_survivors_exact")
        self.assertIn("camp_occ_state_accepts_transfer_authority = yes", transfer)
        lodz = block(EFFECTS, "camp_occ_try_lodz_auschwitz_transfer")
        self.assertIn("camp_occ_state_has_current_authority = yes", lodz)
        self.assertNotIn("is_controlled_by = PREV", lodz)

    def test_japanese_clients_register_china_but_not_man_or_men_cores(self):
        geography = block(TRIGGERS, "camp_occ_state_is_china_region")
        self.assertIn("NOT = { OR = { is_core_of = MAN is_core_of = MEN } }", geography)
        japan = block(TRIGGERS, "camp_occ_state_has_japanese_client_authority")
        self.assertIn("is_subject_of = JAP", japan)
        self.assertIn("camp_occ_state_is_china_region = yes", block(TRIGGERS, "camp_occ_state_has_current_authority"))
        try_register = block(EFFECTS, "camp_occ_try_register_current_state")
        self.assertIn("set_temp_variable = { camp_occ_source_authority = JAP }", try_register)
        self.assertIn("JAP = {", block(EFFECTS, "camp_occ_track_controlled_state"))
        self.assertTrue(japanese_authority("RNG", True, "CHI"))  # State 613 pattern.
        self.assertTrue(japanese_authority("MAN", True, "CHI"))  # Captured state outside MAN's core.
        self.assertFalse(japanese_authority("MAN", True, "MAN"))
        self.assertFalse(japanese_authority("MEN", True, "MEN"))
        self.assertFalse(japanese_authority("third_country_subject", True, "CHI"))
        pingfang = block(COUNTRY_TRIGGERS, "camp_admin_country_census_jap_pingfang_host")
        self.assertIn("state = 328", pingfang)
        self.assertNotIn("camp_occ_state_has_japanese_client_authority", pingfang)


if __name__ == "__main__":
    unittest.main(verbosity=2)
