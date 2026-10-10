"""Production-source checks for the extended partner route (Slovakia, Croatia, Bulgaria, Vichy).

Every order window is measured in days since Germany's campaign opened (the country flag
camp_occ_campaign_opened). The harness opens it on CAMPAIGN_OPENED and derives each window
from camp_occ_partner_table, so no calendar date gates the route.

Uses the existing occupation harness. Scope, eligibility, registration, exact
transfer, answer and closure logic come from production definitions; mocked
engine primitives do not establish HOI4 runtime behavior.
"""
from pathlib import Path
import datetime
import json
import sys
import copy

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from foundation_source_tests import get, parse
from partner_deportation_source_tests import ResponseRuntime, event, choose
from partner_deportation_source_tests import ROOT, EVENTS, DECISIONS, allocations, HUN_STATES
from partner_deportation_source_tests import transform as partner_transform


# Harness timeline only: the day Germany's campaign opens. The windows below follow from it.
CAMPAIGN_OPENED = datetime.date(1941, 6, 22)


def _table():
    source = ROOT / "common/script_constants/camp_occ_partner_constants.txt"
    values = {}
    for category, _, body in parse(source.read_text(encoding="utf-8-sig")):
        if category == "camp_occ_partner_table":
            values = {key: float(value) for key, _, value in body if key != "schema" and not isinstance(value, list)}
    return values


TABLE = _table()


def day(count):
    """The date on which Germany's campaign is `count` days old."""
    return CAMPAIGN_OPENED + datetime.timedelta(days=int(count))


def window(prefix):
    """First date the order stands and first date it no longer stands (days > start, not days > end)."""
    return day(TABLE[prefix + "_start_days"] + 1), day(TABLE[prefix + "_end_days"] + 1)


PARTNERS = {
    "SLO": (70, "SLO") + window("slo"),
    "CRO": (109, "CRO") + window("cro"),
    "BUL": (106, "BUL") + window("bul"),
    "VIC": (21, "FRA") + window("vic"),
    "FRA": (22, "FRA") + window("vic"),
}
SLO_ORDER_DAY = PARTNERS["SLO"][2] + datetime.timedelta(days=7)
CRO_FIRST_WAVE_END = day(TABLE["cro_first_end_days"] + 1)
CRO_SECOND_WAVE_START = day(TABLE["cro_second_start_days"] + 1)


class ExtendedRuntime(ResponseRuntime):
    def __init__(self):
        super().__init__()
        source = ROOT / "common/scripted_effects/camp_occ_partner_effects.txt"
        self.effects.update({k: v for k, _, v in parse(source.read_text(encoding="utf-8-sig"))})
        source = ROOT / "common/scripted_triggers/camp_occ_partner_triggers.txt"
        self.triggers.update({k: partner_transform(v) for k, _, v in parse(source.read_text(encoding="utf-8-sig"))})
        source = ROOT / "common/script_constants/camp_occ_partner_constants.txt"
        for category, _, body in parse(source.read_text(encoding="utf-8-sig")):
            for key, _, value in body:
                if key != "schema" and not isinstance(value, list):
                    self.constants[f"{category}.{key}"] = float(value)
        self.triggers = {name: partner_transform(body) for name, body in self.triggers.items()}

    def target(self, x, scope, previous):
        if x == "CONTROLLER" and (scope not in self.scopes or "controller" not in self.scopes[scope]):
            raise AssertionError(f"CONTROLLER evaluated outside a state scope: {scope!r}, previous={previous!r}, block={getattr(self, '_debug_block', None)!r}")
        return super().target(x, scope, previous)

    def execute(self, block, scope, prev=None):
        pending = []
        for key, op, value in block:
            if key in ("add_to_array", "remove_from_array"):
                if pending:
                    super().execute(pending, scope, prev)
                    pending = []
                array = get(value, "array")
                item = self.val(get(value, "value"), scope, prev)
                values = self.scopes[scope]["arrays"].setdefault(array, [])
                if key == "add_to_array":
                    values.append(item)
                elif item in values:
                    values.remove(item)
            elif key in ("all_of", "any_of"):
                if pending:
                    super().execute(pending, scope, prev)
                    pending = []
                array = get(value, "array")
                items = list(self.scopes[scope]["arrays"].get(array, []))
                body = [entry for entry in value if entry[0] not in ("array", "value", "index")]
                matched = []
                for index, item in enumerate(items):
                    self.temp[get(value, "index", "i")] = index
                    self.temp[get(value, "value", "v")] = item
                    limit = get(value, "limit", [])
                    if limit and not self.cond(limit, scope, prev):
                        continue
                    matched.append(item)
                    self.execute([entry for entry in body if entry[0] != "limit"], scope, prev)
                    if key == "any_of":
                        break
            elif key in self.triggers and value == "yes":
                if pending:
                    super().execute(pending, scope, prev)
                    pending = []
                self.cond(self.triggers[key], scope, prev)
            else:
                pending.append((key, op, value))
        if pending:
            try:
                super().execute(pending, scope, prev)
            except NotImplementedError as error:
                raise AssertionError(f"unsupported scripted primitive {error} from block: {pending!r}") from error

    def cond(self, block, scope, previous=None):
        self._debug_block = block
        # The source trigger deliberately uses a quote trigger with ordered
        # if/else_if temp assignments. Model that native trigger-side effect
        # sequence before evaluating its remaining guards.
        def run_chains(entries):
            out = []
            index = 0
            while index < len(entries):
                key, op, value = entries[index]
                if key in ("if", "else_if", "else"):
                    chain = []
                    while index < len(entries) and entries[index][0] in ("if", "else_if", "else"):
                        chain.append(entries[index])
                        index += 1
                    for branch, _, body in chain:
                        limit = get(body, "limit", [])
                        allowed = branch == "else" or self.cond(limit, scope, previous)
                        if allowed:
                            self.execute([item for item in body if item[0] != "limit"], scope, previous)
                            break
                    continue
                if key in ("set_temp_variable", "add_to_temp_variable", "subtract_from_temp_variable",
                           "multiply_temp_variable", "divide_temp_variable", "clamp_temp_variable",
                           "round_temp_variable"):
                    self.execute([(key, op, value)], scope, previous)
                    index += 1
                    continue
                if key in self.triggers and value in ("yes", "no"):
                    result = self.cond(self.triggers[key], scope, previous) == (value == "yes")
                    marker = f"__extended_trigger_result_{len(self.temp)}_{index}"
                    self.temp[marker] = int(result)
                    out.append(("check_variable", "=", [("var", "=", marker), ("value", "=", "1")]))
                    index += 1
                    continue
                if key == "has_cosmetic_tag":
                    out.append(("has_country_flag", op, str(value)))
                    index += 1
                    continue
                if isinstance(value, list) and key in ("AND", "OR", "NOT"):
                    value = run_chains(value)
                out.append((key, op, value))
                index += 1
            return out

        def expand_meta(value):
            text = get(value, "text", [])
            params = {key: raw for key, _, raw in value if key != "text"}
            rendered = {}
            for key, raw in params.items():
                token = raw
                if isinstance(token, str) and token.startswith("[?"):
                    token = token[2:token.index("|")]
                    rendered[key] = str(int(self.val(token, scope, previous)))
                elif isinstance(token, str) and token.startswith("[?constant:"):
                    token = token[11:token.index("|")]
                    rendered[key] = str(int(self.val("constant:" + token, scope, previous)))
                else:
                    rendered[key] = str(token).strip('"')

            def replace(entries):
                result = []
                for key, op, child in entries:
                    if isinstance(child, list):
                        child = replace(child)
                    elif isinstance(child, str):
                        for name, value in rendered.items():
                            child = child.replace(f"[{name}]", value)
                    result.append((key, op, child))
                return result
            return replace(text)

        def visit(entries):
            out = []
            for key, op, value in entries:
                if key == "meta_trigger":
                    out.extend(visit(expand_meta(value)))
                elif isinstance(value, list):
                    out.append((key, op, visit(value)))
                else:
                    out.append((key, op, value))
            return out
        return super().cond(visit(run_chains(block)), scope, previous)


def country(r, tag, original_tag=None, faction=True, subject=False, vichy=False):
    r.scopes[tag] = {
        "id": tag, "exists": True, "original_tag": original_tag or tag,
        "flags": {"test_faction_GER"} if faction else set(), "arrays": {}, "mods": set(),
        "government": "fascism", "wars": set(), "has_war": False,
    }
    if subject:
        r.scopes[tag]["overlord"] = "GER"
    if vichy and tag == "FRA":
        r.scopes[tag]["cosmetic_tag"] = "FRA_VICHY"
        r.scopes[tag]["flags"].add("FRA_VICHY")


def setup_partner(tag, state_id=None, destination_controller="GEN", answer=True, faction=True):
    r = ExtendedRuntime()
    r.date = datetime.date(1942, 1, 1)
    ger = r.country("GER")
    ger["flags"].add("origin_test_campaign_eligible")
    ger["flags"].add("camp_occ_campaign_opened")
    ger.setdefault("flag_dates", {})["camp_occ_campaign_opened"] = CAMPAIGN_OPENED
    r.run("camp_occ_initialize_country", "GER")
    r.scopes["HUN"] = {"id": "HUN", "exists": True, "flags": set(), "arrays": {}, "mods": set(),
                       "government": "fascism", "wars": set(), "has_war": False}
    r.global_flags.add("test_exists_HUN")
    for origin_state, (population, allocated) in allocations().items():
        r.scopes[origin_state] = {
            "id": origin_state, "state": origin_state,
            "flags": {"camp_occ_origin_assigned", "test_continent_europe"},
            "arrays": {}, "mods": set(), "owner": "HUN", "controller": "HUN", "cores": {"HUN"},
            "state_population_k": population / 1000, "chaos_state_civilian_deaths_total": 0,
            "camp_occ_origin_country": "HUN", "camp_occ_origin_ceiling_k": allocated / 1000,
            "camp_occ_origin_observed_population_k": population / 1000,
            "camp_occ_origin_observed_state_deaths": 0,
        }
    country(r, "GEN", subject=True)
    for other in ("SLO", "CRO", "BUL", "VIC", "FRA"):
        country(r, other, original_tag="FRA" if other == "VIC" else other,
                vichy=(other == "FRA"), faction=(faction if other == tag else True))
    if destination_controller == "SOV":
        country(r, "SOV")
    state_id = state_id or HUN_STATES[0]
    if state_id not in r.scopes:
        source = copy.deepcopy(r.scopes[HUN_STATES[0]])
        source.update(id=state_id, state=state_id)
        r.scopes[state_id] = source
    controller = "FRA" if tag == "VIC" else tag
    core = "FRA" if tag == "VIC" else tag
    state = r.scopes[state_id]
    state["owner"] = controller
    state["controller"] = controller
    state["cores"] = {core}
    state["flags"].discard("camp_occ_registered")
    state["flags"].discard("camp_occ_partner_host")
    state["flags"].discard("camp_occ_closed")
    r.scopes[controller]["capital"] = state_id
    if state_id == 107:
        state["cores"] = {"BUL"}
    r.scopes[92] = {
        "id": 92, "state": 92, "flags": {"camp_origin_observation_initialized", "test_continent_europe"},
        "arrays": {}, "mods": set(), "owner": "GEN", "controller": destination_controller,
        "cores": set(), "state_population_k": 300.0, "chaos_state_civilian_deaths_total": 0,
        "camp_origin_observed_population_k": 300.0, "camp_origin_observed_state_deaths_people": 0,
    }
    r.global_flags.add("test_exists_GEN")
    r.date = PARTNERS[tag][2]
    if answer:
        r.scopes[controller]["flags"].add("camp_occ_extended_order_answered")
    return r, controller, state_id


def run_month(r, date):
    r.date = date
    r.run("camp_occ_monthly_country", "GER")


def run_partner(r, tag, date):
    r.date = date
    r.temp["camp_occ_extended_authority"] = "GER"
    r.temp["camp_occ_extended_destination"] = 92
    r.run("camp_occ_extended_partner_process", tag)


def test_all():
    cases = []
    # Table-driven window boundaries through the production quote and window triggers.
    prefix_of = {"SLO": "slo", "CRO": "cro", "BUL": "bul", "VIC": "vic", "FRA": "vic"}
    for tag, (_, _, start, end) in PARTNERS.items():
        r, partner, state_id = setup_partner(tag, answer=False)
        quote = r.triggers["camp_occ_extended_partner_quote"]
        assert r.cond(quote, partner)
        assert r.temp["camp_occ_order_share"] > 0
        for date, expected in ((start - datetime.timedelta(days=1), False), (start, True),
                               (end - datetime.timedelta(days=1), True), (end, False)):
            r.date = date
            assert r.cond(r.triggers["camp_occ_extended_partner_window"], partner) is expected, (tag, date)
        cases.append(f"{tag} window opens the day after campaign day {int(TABLE[prefix_of[tag] + '_start_days'])} and closes after day {int(TABLE[prefix_of[tag] + '_end_days'])}, enforced by the production partner-window trigger")

    # Bulgarian home/core territory is never a foreign handover source.
    r, partner, _ = setup_partner("BUL", state_id=107, answer=False)
    r.date = PARTNERS["BUL"][2]
    assert not r.cond(r.triggers["camp_occ_extended_partner_candidate"], 107, partner)
    for state_id in (106, 184, 731, 803):
        r, partner, _ = setup_partner("BUL", state_id=state_id, answer=False)
        r.date = PARTNERS["BUL"][2]
        assert r.cond(r.triggers["camp_occ_extended_partner_candidate"], state_id, partner), state_id
    german_731, bul, _ = setup_partner("BUL", state_id=731, answer=False)
    german_731.scopes[731]["controller"] = "GER"
    german_731.date = PARTNERS["BUL"][2]
    assert not german_731.cond(german_731.triggers["camp_occ_extended_partner_candidate"], 731, bul)
    cases.append("BUL-held states 106, 184, 731 and 803 qualify; 731 under German control and Bulgarian home state 107 do not")

    # CRO's inter-wave gap preserves the enrolled remainder, with no movement, death or repeated order report.
    r, partner, source = setup_partner("CRO", answer=False)
    run_partner(r, partner, PARTNERS["CRO"][2])
    assert r.events == [(partner, "camp_occ_partner.3")]
    choose(r, partner, "camp_occ_partner.3", "camp_occ_partner.3.a")
    run_partner(r, partner, CRO_FIRST_WAVE_END)
    source_row = r.scopes["GER"]["arrays"]["camp_occ_row_hosts"].index(source)
    moved_after_first = r.scopes["GER"]["arrays"]["camp_occ_row_moved_out_k"][source_row]
    assert moved_after_first > 0
    assert "camp_occ_extended_first_wave_done" in r.scopes[source]["flags"]
    registered_total = r.scopes["GER"]["arrays"]["camp_occ_row_amounts_k"][source_row] + moved_after_first
    first_share = r.constants["camp_occ_partner_table.cro_first_wave_share"]
    assert 0 < moved_after_first <= registered_total * first_share + 1e-9
    assert r.scopes["GER"]["arrays"]["camp_occ_row_amounts_k"][source_row] > 0
    death_count = r.logged
    run_partner(r, partner, CRO_FIRST_WAVE_END + datetime.timedelta(days=19))
    run_partner(r, partner, CRO_SECOND_WAVE_START - datetime.timedelta(days=1))
    assert r.scopes["GER"]["arrays"]["camp_occ_row_moved_out_k"][source_row] == moved_after_first
    assert r.logged == death_count
    assert r.events == [(partner, "camp_occ_partner.3")]
    run_partner(r, partner, CRO_SECOND_WAVE_START)
    moved_after_second = r.scopes["GER"]["arrays"]["camp_occ_row_moved_out_k"][source_row]
    assert 0 <= registered_total - moved_after_second < r.constants["camp_occ_value.minimum_population_k"]
    assert 0 <= r.scopes["GER"]["arrays"]["camp_occ_row_amounts_k"][source_row] < r.constants["camp_occ_value.minimum_population_k"]
    second_deaths = r.logged - death_count
    assert second_deaths > 0
    after_may = (r.debits, r.credits, r.logged, moved_after_second)
    run_partner(r, partner, CRO_SECOND_WAVE_START + datetime.timedelta(days=14))
    assert (r.debits, r.credits, r.logged, r.scopes["GER"]["arrays"]["camp_occ_row_moved_out_k"][source_row]) == after_may
    cases.append("Croatia transfers only the first-wave share once, holds the living remainder through the gap, transfers that remainder when the second wave opens, and never repeats the demand")

    # Every recipient waits for an answer before the first valid wave; the
    # answer dispatches the current month, including the March-only Bulgarian window.
    r, partner, source = setup_partner("SLO", answer=False)
    run_partner(r, partner, SLO_ORDER_DAY)
    assert r.events == [(partner, "camp_occ_partner.3")]
    assert "camp_occ_extended_order_notified" in r.scopes[partner]["flags"]
    assert "camp_occ_registered" in r.scopes[source]["flags"]
    assert r.debits == r.credits == r.logged == 0
    choose(r, partner, "camp_occ_partner.3", "camp_occ_partner.3.a")
    assert r.debits > 0 and r.credits > 0 and len(r.events) == 1
    before = (r.debits, r.credits, r.logged)
    r.run("camp_occ_try_extended_partner_orders", "GER")
    assert (r.debits, r.credits, r.logged) == before
    cases.append("first source registration sends one demand and no transport; the answer dispatches the current transport once, and a same-month retry is idempotent")

    bul, _, bul_source = setup_partner("BUL", state_id=106, answer=False)
    run_partner(bul, "BUL", PARTNERS["BUL"][2])
    assert bul.events == [("BUL", "camp_occ_partner.3")] and bul.debits == 0
    choose(bul, "BUL", "camp_occ_partner.3", "camp_occ_partner.3.a")
    assert bul.debits > 0 and bul.credits > 0
    cases.append("the Bulgarian order, the shortest window, dispatches on the partner's same-month answer instead of losing its sole month")

    delayed, delayed_partner, delayed_source = setup_partner("SLO", answer=False)
    run_partner(delayed, delayed_partner, SLO_ORDER_DAY)
    choose(delayed, delayed_partner, "camp_occ_partner.3", "camp_occ_partner.3.b")
    delayed_index = delayed.scopes["GER"]["arrays"]["camp_occ_row_hosts"].index(delayed_source)
    delayed_moved = delayed.scopes["GER"]["arrays"]["camp_occ_row_moved_out_k"][delayed_index] * 1000
    assert 0 < delayed_moved <= delayed.constants["camp_occ_partner_table.wave_people"] * delayed.constants["camp_occ_partner_table.delay_share"] + 1
    assert "camp_occ_extended_transports_delayed" in delayed.scopes[delayed_partner]["flags"]
    cases.append("a delayed answer halves the monthly capacity and source offer, and the first live monthly debit respects the reduced ceiling")

    for partner_tag, (state_id, _, start, _) in PARTNERS.items():
        if partner_tag == "BUL":
            state_id = 106
        compliant, compliant_country, compliant_state = setup_partner(partner_tag, state_id=state_id, answer=False)
        run_partner(compliant, compliant_country, start)
        choose(compliant, compliant_country, "camp_occ_partner.3", "camp_occ_partner.3.a")
        normal_rows = compliant.scopes["GER"]["arrays"]
        normal_index = normal_rows["camp_occ_row_hosts"].index(compliant_state)
        normal_moved = normal_rows["camp_occ_row_moved_out_k"][normal_index] * 1000

        delayed_case, delayed_country, delayed_state = setup_partner(partner_tag, state_id=state_id, answer=False)
        run_partner(delayed_case, delayed_country, start)
        choose(delayed_case, delayed_country, "camp_occ_partner.3", "camp_occ_partner.3.b")
        delayed_rows = delayed_case.scopes["GER"]["arrays"]
        delayed_index = delayed_rows["camp_occ_row_hosts"].index(delayed_state)
        delayed_moved = delayed_rows["camp_occ_row_moved_out_k"][delayed_index] * 1000
        assert 0 < delayed_moved < normal_moved, (partner_tag, normal_moved, delayed_moved)
        assert delayed_moved <= normal_moved * delayed_case.constants["camp_occ_partner_table.delay_share"] + 1
        assert normal_rows["camp_occ_row_deaths_k"][normal_index] == 0
        assert delayed_rows["camp_occ_row_deaths_k"][delayed_index] == 0
        cases.append(f"{partner_tag} delayed answer moves a smaller living origin amount than compliance and records no source death")

    vichy, vichy_country, _ = setup_partner("VIC", answer=False)
    run_partner(vichy, vichy_country, PARTNERS["VIC"][2] - datetime.timedelta(days=10))
    assert not vichy.events and not vichy.scopes[vichy_country]["arrays"].get("camp_occ_states")
    run_partner(vichy, vichy_country, PARTNERS["VIC"][2] + datetime.timedelta(days=21))
    assert vichy.events == [(vichy_country, "camp_occ_partner.3")] and vichy.debits == 0
    cases.append("the Vichy order does not register on a monthly pulse before its window opens; it reports at the first pulse inside the window")

    import black_friday_sale_prices as sale
    partner_decision = get(get(DECISIONS, "political_actions"), "camp_occ_partner_halt_transports")
    for ratio in (10000, 5000, 2500):
        r, partner, _ = setup_partner("SLO", answer=False)
        run_partner(r, partner, SLO_ORDER_DAY)
        sale.install(r, ratio)
        price = r.val(get(partner_decision, "cost"), partner)
        assert price == sale.production_quote(r.constants["camp_occ_partner_response.halt_pp"], ratio)
        assert r.cond(get(partner_decision, "visible"), partner) and r.cond(get(partner_decision, "available"), partner)
        r.scopes[partner]["political_power"] = 100 - price
        r.execute(get(partner_decision, "complete_effect"), partner)
        assert "camp_occ_extended_transports_halted" in r.scopes[partner]["flags"]
        assert sale.credits(r) == 1 and r.scopes[partner]["political_power"] == 100 - price
        assert r.events.count(("GER", "camp_occ_partner.4")) == 1
    cases.append("the paid partner halt charges and credits exactly once at full price and the 50%/25% sale quotes")

    stale, stale_partner, _ = setup_partner("SLO", answer=False)
    run_partner(stale, stale_partner, SLO_ORDER_DAY)
    sale.install(stale, 2500)
    stale_price = stale.val(get(partner_decision, "cost"), stale_partner)
    assert stale.cond(get(partner_decision, "available"), stale_partner)
    stale.scopes[stale_partner]["political_power"] = 100 - stale_price
    stale.date = PARTNERS["SLO"][3]
    stale.execute(get(partner_decision, "complete_effect"), stale_partner)
    assert stale.scopes[stale_partner]["political_power"] == 100
    assert not stale.cond(get(partner_decision, "visible"), stale_partner)
    assert sale.credits(stale) == 0 and "camp_occ_extended_transports_halted" not in stale.scopes[stale_partner]["flags"]
    cases.append("a stale post-window completion after the 25% sale quote refunds its exact charge and grants no purchase credit")

    subject, subject_partner, _ = setup_partner("SLO", answer=False)
    subject.scopes[subject_partner]["overlord"] = "GER"
    run_partner(subject, subject_partner, SLO_ORDER_DAY)
    choose(subject, subject_partner, "camp_occ_partner.3", "camp_occ_partner.3.c")
    assert subject.autonomy == [(subject_partner, "@CAMP_OCC_PARTNER_HALT_AUTONOMY", "camp_occ_partner_halt_autonomy")]
    cases.append("a German subject that halts also pays the documented autonomy penalty")

    refused, refused_partner, refused_source = setup_partner("SLO", answer=False, faction=False)
    run_partner(refused, refused_partner, SLO_ORDER_DAY)
    assert not refused.events and "camp_occ_registered" not in refused.scopes[refused_source]["flags"]
    assert refused.debits == refused.credits == refused.logged == 0
    refused_special, special_partner, special_source = setup_partner("SLO", answer=False)
    refused_special.scopes[special_partner]["special_chaos"] = True
    run_partner(refused_special, special_partner, SLO_ORDER_DAY)
    assert not refused_special.events and "camp_occ_registered" not in refused_special.scopes[special_source]["flags"]
    assert refused_special.debits == refused_special.credits == refused_special.logged == 0
    cases.append("a partner outside Germany's faction and a special Chaos country are both refused without registration or population change")

    # State 92 as a German puppet accepts an exact receipt; loss belongs to the newly appended arrival row.
    r, partner, source = setup_partner("SLO", destination_controller="GEN", answer=True)
    run_partner(r, partner, SLO_ORDER_DAY)
    assert r.debits == 2 and r.credits == 1
    rows = r.scopes["GER"]["arrays"]
    source_row = rows["camp_occ_row_hosts"].index(source)
    assert rows["camp_occ_row_moved_out_k"][source_row] > 0
    imported = [i for i, origin in enumerate(rows["camp_occ_row_origins"]) if origin == source and rows["camp_occ_row_hosts"][i] == 92]
    assert len(imported) == 1
    arrival = imported[0]
    assert rows["camp_occ_row_deaths_k"][arrival] > 0
    assert abs(rows["camp_occ_row_amounts_k"][arrival] + rows["camp_occ_row_deaths_k"][arrival] - rows["camp_occ_row_moved_in_k"][arrival]) < 1e-9
    deaths = rows["camp_occ_row_deaths_k"][arrival]
    debits, credits, logged = r.debits, r.credits, r.logged
    r.run("camp_occ_try_extended_partner_orders", "GER")
    assert (r.debits, r.credits, r.logged) == (debits, credits, logged)
    assert rows["camp_occ_row_deaths_k"][arrival] == deaths
    cases.append("state 92 under GEN receives one measured transfer and one bound arrival-loss row; replay cannot repeat either")

    # Destination capture or an invalid host rejects the route before source debit.
    r, _, source = setup_partner("SLO", destination_controller="SOV", answer=True)
    r.scopes["SOV"] = {"id": "SOV", "exists": True, "original_tag": "SOV", "flags": set(), "arrays": {}, "mods": set()}
    run_partner(r, "SLO", SLO_ORDER_DAY)
    assert r.debits == r.credits == r.logged == 0
    assert not r.scopes[source].get("camp_occ_registered", False)
    cases.append("state 92 captured by the Soviet Union rejects registration and transfer without a physical debit")

    # Halt closes the order permanently; no re-report or later movement.
    r, partner, source = setup_partner("SLO", answer=False)
    run_partner(r, partner, SLO_ORDER_DAY)
    choose(r, partner, "camp_occ_partner.3", "camp_occ_partner.3.c")
    assert r.events.count(("GER", "camp_occ_partner.4")) == 1
    before = r.scopes[source]["state_population_k"]
    run_month(r, SLO_ORDER_DAY + datetime.timedelta(days=30))
    source_rows = [i for i, host in enumerate(r.scopes["GER"]["arrays"]["camp_occ_row_hosts"]) if host == source]
    assert source_rows
    assert all(r.scopes["GER"]["arrays"]["camp_occ_row_statuses"][i] == r.constants["camp_occ_row_status.released"]
               and r.scopes["GER"]["arrays"]["camp_occ_row_amounts_k"][i] == 0
               and r.scopes["GER"]["arrays"]["camp_occ_row_deaths_k"][i] == 0 for i in source_rows)
    released = sum(r.scopes["GER"]["arrays"]["camp_occ_row_released_k"][i] for i in source_rows)
    assert released > 0 and r.scopes[source]["state_population_k"] == before
    run_partner(r, partner, SLO_ORDER_DAY + datetime.timedelta(days=44))
    assert r.events.count((partner, "camp_occ_partner.3")) == 1
    assert r.scopes[source]["state_population_k"] == before
    cases.append("a halt is single-use, sends one German notification, and the next close releases the unpaid remainder in place with no death, movement or repeat report")

    return cases


if __name__ == "__main__":
    cases = test_all()
    payload = {"status": "passed", "count": len(cases), "cases": cases,
               "limits": "Production parsed logic with existing harness primitives; country scopes, geography and engine transactions are fixtures/mocks. No HOI4 execution."}
    (HERE / "extended_partner_source_results.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
