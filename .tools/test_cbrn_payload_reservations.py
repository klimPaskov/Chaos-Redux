"""Bounded actual-source chemical receipt regressions, not HOI4 engine proof.

Run: python -B .tools/test_cbrn_payload_reservations.py
Only native stock observations/mutations and world predicates use scenario data.
Authorization, dispatch to stock primitives, measurement, receipt transitions,
and accounting execute the parsed production bodies. Unknown commands fail.
Conservative helper/meta frames discard newly created temps and temp arrays.
Normal variables and arrays belong to typed scopes, independent of those frames.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from hashlib import sha256
from pathlib import Path
import operator
import re
import unittest


ROOT_DIR = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r'#[^\n]*|"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>#"]+')
D = Decimal
ZERO = D(0)
MODELS = tuple(f"{kind}_chemical_air_payload_lot_1" for kind in
               ("choking", "blister", "nerve", "incapacitating"))
AGENTS = {
    "chlorine": ("choking", "chlorine_gas", None),
    "phosgene": ("choking", "phosgene", None),
    "mustard": ("blister", "mustard_gas", None),
    "lewisite": ("blister", "lewisite", None),
    "tabun": ("nerve", "tabun", None),
    "sarin": ("nerve", "sarin", "sp_cw_sarin_program"),
    "soman": ("nerve", "soman", "sp_cw_soman_program"),
    "malodor": ("incapacitating", None, "sp_cw_malodor_bomb_program"),
    "behavioral": ("incapacitating", None, "sp_cw_aphrodisiac_bomb_program"),
}
EFFECT_FILES = (
    "cbrn_payload_reservation_effects.txt", "cbrn_payload_reservation_native_effects.txt",
    "cbrn_state_escrow_native_effects.txt", "cbrn_payload_effects.txt",
    "cbrn_chemical_raid_effects.txt", "cbrn_exposure_effects.txt",
    "condemnation_response_effects.txt",
    "032_missiles_payload_receipt_effects.txt",
    "032_missiles_operations_effects.txt",
)
# Read the owning consumption boundary only, without importing the unmodeled
# commit/resolution/consequence closure into this bounded source fixture.
SELECTED_EFFECTS = {"032_missiles_operations_effects.txt":
                    ("missiles_consume_chemical_payload", "missiles_consume_special_payload")}
TRIGGER_FILES = ("cbrn_payload_reservation_triggers.txt", "cbrn_payload_triggers.txt",
                 "cbrn_triggers.txt", "cbrn_diplomacy_triggers.txt", "cbrn_designer_triggers.txt",
                 "condemnation_sanctions_triggers.txt", "032_missiles_payload_receipt_triggers.txt",
                 "032_missiles_operations_triggers.txt", "032_missiles_triggers.txt",
                 "032_missiles_preparation_cost_triggers.txt")
CONSTANT_FILES = ("cbrn_payload_reservation_constants.txt", "cbrn_system_constants.txt",
                  "cbrn_chemical_delivery_constants.txt", "cbrn_action_record_constants.txt",
                  "cbrn_diplomacy_constants.txt", "condemnation_sanctions_constants.txt",
                  "032_missiles_constants.txt", "biological_lifecycle_constants.txt")


@dataclass(frozen=True)
class Node:
    key: str
    op: str | None
    value: str | list
    line: int


def parse(text):
    """Keep operators, repeated keys, order, and source lines intact."""
    tokens = [(m.group(), text.count("\n", 0, m.start()) + 1)
              for m in TOKEN.finditer(text) if not m.group().startswith("#")]
    cursor = 0

    def block(nested=False):
        nonlocal cursor
        result = []
        while cursor < len(tokens):
            key, line = tokens[cursor]
            cursor += 1
            if key == "}":
                if not nested:
                    raise ValueError(f"Unexpected closing brace at line {line}")
                return result
            if key == "{":
                result.append(Node("", None, block(True), line))
                continue
            if key in ("{", "=", "<", ">"):
                raise ValueError(f"Unexpected {key} at line {line}")
            if cursor == len(tokens) or tokens[cursor][0] not in ("=", "<", ">"):
                result.append(Node(key, None, "", line))
                continue
            op = tokens[cursor][0]
            cursor += 1
            if cursor == len(tokens):
                raise ValueError(f"Missing value at line {line}")
            val = tokens[cursor][0]
            cursor += 1
            if val == "{":
                val = block(True)
            elif val in ("}", "=", "<", ">"):
                raise ValueError(f"Unexpected value {val} at line {line}")
            result.append(Node(key, op, val, line))
        if nested:
            raise ValueError("Unclosed source block")
        return result

    return block()


def item(nodes, key, default=None):
    return next((n.value for n in nodes if n.key == key), default)


class Source:
    def __init__(self):
        self.effects, self.triggers, self.constants = {}, {}, {}
        self.hashes = {}
        for folder, names, destination in (
            ("scripted_effects", EFFECT_FILES, self.effects),
            ("scripted_triggers", TRIGGER_FILES, self.triggers),
            ("script_constants", CONSTANT_FILES, None),
        ):
            for name in names:
                path = ROOT_DIR / "common" / folder / name
                raw = path.read_bytes()
                self.hashes[str(path.relative_to(ROOT_DIR))] = sha256(raw).hexdigest()
                try:
                    source_text = raw.decode("utf-8-sig")
                    if folder == "scripted_effects" and name in SELECTED_EFFECTS:
                        nodes = []
                        headers = list(re.finditer(r"(?m)^([a-z_0-9]+)\s*=\s*\{", source_text))
                        for index, header in enumerate(headers):
                            if header.group(1) not in SELECTED_EFFECTS[name]:
                                continue
                            end = headers[index + 1].start() if index + 1 < len(headers) else len(source_text)
                            prefix_lines = source_text.count("\n", 0, header.start())
                            nodes.extend(parse("\n" * prefix_lines + source_text[header.start():end]))
                        if {n.key for n in nodes} != set(SELECTED_EFFECTS[name]):
                            raise ValueError("Missing owning consumption helper")
                    else:
                        nodes = parse(source_text)
                except ValueError as exc:
                    raise ValueError(f"{path}: {exc}") from exc
                local = {n.key: n.value for n in nodes if n.key.startswith("@")}
                for n in nodes:
                    if n.key.startswith("@"):
                        continue
                    if destination is None:
                        def constants(prefix, children):
                            for child in children:
                                if child.key == "schema":
                                    continue
                                key = f"{prefix}.{child.key}"
                                if isinstance(child.value, list):
                                    constants(key, child.value)
                                else:
                                    self.constants[key] = D(child.value)
                        constants(n.key, n.value)
                    else:
                        if n.key in destination:
                            raise ValueError(f"Duplicate helper {n.key}")
                        destination[n.key] = (n.value, local, str(path.relative_to(ROOT_DIR)), n.line)

    def constant(self, name):
        return self.constants[name]


@dataclass(eq=False)
class Scope:
    name: str
    identity: int
    kind: str = "country"
    variables: dict = field(default_factory=dict)
    arrays: dict = field(default_factory=dict)
    flags: set = field(default_factory=set)
    techs: set = field(default_factory=set)
    projects: set = field(default_factory=set)
    wars: set = field(default_factory=set)
    stocks: dict = field(default_factory=dict)
    controller: Scope | None = None
    exists: bool = True
    impassable: bool = False
    organizations: list = field(default_factory=list)
    timed_flags: dict = field(default_factory=dict)


@dataclass
class Frame:
    scalars: dict = field(default_factory=dict)
    arrays: dict = field(default_factory=dict)


@dataclass
class Outcome:
    """Explicit native leaf injection, independent of receipt success status."""
    fraction: Decimal = D(1)
    before: Decimal | None = None
    after: Decimal | None = None
    actual_model: str | None = None
    reads: int = 0


class Machine:
    def __init__(self, source, actor, root=None, temp_has_variable=True):
        self.source = source
        self.current = actor
        self.root = actor if root is None else root
        self.stack = []
        self.frames = [Frame()]
        self.targets = {}
        self.global_flags = set()
        self.locals = [{}]
        self.calls = Counter()
        self.trace = []
        self.nativecalls = []
        self.outcomes = {"debit": deque(), "credit": deque()}
        self.measurement = None
        self.after_call = {}  # Scenario transitions after real helper/frame return.
        self.temp_has_variable = temp_has_variable

    def temp_owner(self, name, arrays=False):
        for frame in reversed(self.frames):
            values = frame.arrays if arrays else frame.scalars
            if name in values:
                return values
        return None

    def temp(self, name, value):
        owner = self.temp_owner(name)
        (self.frames[-1].scalars if owner is None else owner)[name] = value

    def targeted(self, name):
        if "@var:" in name:
            prefix, selector = name.split("@var:", 1)
            v = self.value(selector)
            if not isinstance(v, Decimal) or v != v.to_integral_value():
                raise AssertionError(f"Unmodeled noninteger targeted key {name}: {v!r}")
            return prefix + str(int(v))
        return name

    def scope(self, token):
        if token == "ROOT":
            return self.root
        if token == "THIS":
            return self.current
        if token == "PREV":
            if not self.stack:
                raise AssertionError("PREV without a scope caller")
            return self.stack[-1]
        if token == "CONTROLLER":
            if self.current.kind != "state":
                raise AssertionError("CONTROLLER outside STATE")
            return self.current.controller
        if token.startswith("event_target:"):
            return self.targets.get(token[13:])
        if token.startswith("var:"):
            v = self.value(token[4:])
            return v if isinstance(v, Scope) else None
        raise AssertionError(f"Unmodeled scope {token}")

    def value(self, token):
        if not isinstance(token, str):
            return token
        token = token.strip('"')
        if token.startswith("constant:"):
            return self.source.constant(token[9:])
        if token.startswith("token:"):
            return token[6:]
        if token.startswith("@"):
            return self.value(self.locals[-1][token])
        if token.startswith("num_equipment@"):
            model = token[14:]
            if self.measurement is not None:
                outcome = self.measurement
                observation = outcome.before if outcome.reads == 0 else outcome.after
                outcome.reads += 1
                if observation is not None:
                    return D(observation)
            return self.current.stocks.get(model, ZERO)
        if token.startswith("event_target:") and "." not in token:
            return self.scope(token)
        if token.startswith(("ROOT.", "PREV.", "THIS.", "event_target:")) and "." in token:
            scope_token, key = token.split(".", 1)
            target = self.scope(scope_token)
            if target is None:
                return ZERO
            key = self.targeted(key)
            return D(target.identity) if key == "id" else target.variables.get(key, ZERO)
        try:
            return D(token)
        except InvalidOperation:
            pass
        if "." in token or token.startswith("var:"):
            raise AssertionError(f"Unmodeled scoped value/getter {token}")
        token = self.targeted(token)
        if token == "id":
            return D(self.current.identity)
        owner = self.temp_owner(token)
        return owner[token] if owner is not None else self.current.variables.get(token, ZERO)

    def has_variable(self, token):
        key = self.targeted(token)
        # Chosen model: native has_variable sees live unscoped temps too.
        # Normal-only counterexample is exercised and reported separately.
        return (self.temp_has_variable and self.temp_owner(key) is not None) or key in self.current.variables

    def enter(self, target, body, trigger=False):
        if target is None:
            if trigger:
                return False
            raise AssertionError("Effect enters missing/non-scope pointer")
        old = self.current
        self.stack.append(old)
        self.current = target
        try:
            return self.condition(body) if trigger else self.execute(body)
        finally:
            self.current = old
            self.stack.pop()

    def call(self, name, trigger=False):
        definitions = self.source.triggers if trigger else self.source.effects
        if name not in definitions:
            raise AssertionError(f"Unmodeled {'trigger' if trigger else 'effect'} helper {name}")
        body, local, path, line = definitions[name]
        self.calls[name] += 1
        self.frames.append(Frame())
        self.locals.append(local)
        self.trace.append(f"{path}:{line} {name} [{self.current.name}]")
        previous_measurement = self.measurement
        if name in ("cbrn_state_escrow_measure_model_debit", "cbrn_state_escrow_measure_model_credit"):
            kind = "debit" if name.endswith("debit") else "credit"
            self.measurement = self.outcomes[kind].popleft() if self.outcomes[kind] else Outcome()
        try:
            result = self.condition(body) if trigger else self.execute(body)
        except (AssertionError, KeyError, TypeError) as exc:
            raise AssertionError(f"{exc}\n  at {self.trace[-1]}") from None
        finally:
            self.measurement = previous_measurement
            self.trace.pop()
            self.locals.pop()
            self.frames.pop()
        hook = self.after_call.get(name)
        if hook is not None:
            hook(self)
        return result

    def compare(self, body):
        var = item(body, "var")
        if var is not None:
            left, right, op = self.value(var), self.value(item(body, "value")), item(body, "compare", "equals")
        else:
            if len(body) != 1:
                raise AssertionError("Unmodeled shorthand variable comparison")
            n = body[0]
            left, right, op = self.value(n.key), self.value(n.value), n.op
        comparisons = {"=": operator.eq, "<": operator.lt, ">": operator.gt,
                       "equals": operator.eq, "not_equals": operator.ne,
                       "greater_than": operator.gt, "less_than": operator.lt,
                       "greater_than_or_equals": operator.ge, "less_than_or_equals": operator.le}
        return comparisons[op](left, right)

    def condition(self, nodes, mode="AND"):
        # Lazy evaluation avoids traversing unreachable branches outside this surface.
        values = (self.predicate(n) for n in nodes)
        if mode == "OR":
            return any(values)
        if mode == "NOT":
            return not any(values)  # Clausewitz NOT siblings have NOR semantics.
        return all(values)

    def predicate(self, n):
        k, v = n.key, n.value
        if k in ("AND", "OR", "NOT", "hidden_trigger"):
            return self.condition(v, "AND" if k == "hidden_trigger" else k)
        if k == "check_variable":
            return self.compare(v)
        if k == "has_variable":
            return self.has_variable(v)
        if k == "has_event_target":
            return v in self.targets
        if k == "has_country_flag":
            return v in self.current.flags
        if k == "has_global_flag":
            return v in self.global_flags
        if k == "has_state_flag":
            if self.current.kind != "state":
                raise AssertionError("STATE flag predicate outside STATE")
            return v in self.current.flags
        if k == "scope_exists":
            # This checks the fixture's typed object, never pointer arithmetic or
            # ownership. Production object-specific guards still execute.
            return isinstance(self.current, Scope) == (v == "yes")
        if k == "has_war":
            return bool(self.current.wars) == (v == "yes")
        if k in ("exists", "impassable"):
            if k == "exists" and self.current.kind != "country":
                raise AssertionError("COUNTRY existence predicate used on STATE")
            return getattr(self.current, k) == (v == "yes")
        if k == "tag":
            return self.current is self.scope(v)
        if k == "is_controlled_by":
            return self.current.controller is self.scope(v)
        if k == "has_war_with":
            return self.scope(v) in self.current.wars
        if k == "has_tech":
            return v in self.current.techs
        if k == "num_of_nukes":
            if self.current.kind != "country":
                raise AssertionError("COUNTRY nuclear inventory predicate outside COUNTRY")
            # Explicit native inventory fact, not a payment acknowledgement.
            comparisons = {"=": operator.eq, "<": operator.lt, ">": operator.gt}
            return comparisons[n.op](self.current.variables.get('num_of_nukes', ZERO), self.value(v))
        if k == "has_equipment":
            if len(v) != 1:
                self.unmodeled(n)
            entry = v[0]
            archetypes = {f"{kind}_chemical_air_payload": f"{kind}_chemical_air_payload_lot_1"
                          for kind in ("choking", "blister", "nerve", "incapacitating")}
            archetypes["chemical_artillery_ammunition"] = "chemical_shell_lot_1"
            if entry.key in archetypes:
                model = archetypes[entry.key]
            elif entry.key.startswith("chemical_") and entry.key.endswith("_payload_cylinder_1"):
                model = entry.key
            else:
                self.unmodeled(n)
            comparisons = {"=": operator.eq, "<": operator.lt, ">": operator.gt}
            return comparisons[entry.op](self.current.stocks.get(model, ZERO), self.value(entry.value))
        if k == "is_special_project_completed":
            return v.removeprefix("sp:") in self.current.projects
        if k == "any_military_industrial_organization":
            # Execute the real designer predicate with explicit empty-country
            # MIO inventory. Nonempty trait/organization analysis is unsupported.
            if self.current.organizations:
                raise AssertionError("Unmodeled nonempty military-industrial-organization inventory")
            return False
        if k in self.source.triggers:
            result = self.call(k, True)
            return result if v == "yes" else not result if v == "no" else self.unmodeled(n)
        if k.startswith(("var:", "event_target:")) or k in ("ROOT", "PREV", "THIS", "CONTROLLER"):
            return self.enter(self.scope(k), v, True)
        if k == "set_temp_variable":
            self.execute([n])
            return True
        if k == "meta_trigger":
            return self.meta(v, True)
        return self.unmodeled(n)

    def unmodeled(self, n):
        raise AssertionError(f"Unmodeled command {n.key} at source line {n.line}")

    def meta(self, nodes, trigger=False):
        replacements = {}
        for n in nodes:
            if n.key in ("text", "debug"):
                continue
            raw = n.value.strip('"')
            match = re.fullmatch(r'\[\?(.+?)(?:\.GetTokenKey|\|\.0)\]', raw)
            if not match:
                raise AssertionError(f"Unmodeled meta replacement {n.key}={raw}")
            val = self.value(match[1])
            replacements[f"[{n.key}]"] = str(int(val)) if isinstance(val, Decimal) else val

        def replace(raw):
            if isinstance(raw, list):
                return [Node(replace(n.key), n.op, replace(n.value), n.line) for n in raw]
            for key, value in replacements.items():
                raw = raw.replace(key, value)
            return raw

        self.frames.append(Frame())
        try:
            body = replace(item(nodes, "text"))
            return self.condition(body) if trigger else self.execute(body)
        finally:
            self.frames.pop()

    def execute(self, nodes):
        taken = None
        for n in nodes:
            k, v = n.key, n.value
            if k in ("if", "else_if", "else"):
                if k == "if":
                    taken = False
                elif taken is None:
                    raise AssertionError("Orphan else branch")
                if not taken and (k == "else" or self.condition(item(v, "limit", []))):
                    taken = True
                    self.execute([child for child in v if child.key != "limit"])
                continue
            taken = None
            if k in ("set_variable", "set_temp_variable", "add_to_variable", "add_to_temp_variable",
                     "subtract_from_variable", "subtract_from_temp_variable", "multiply_variable",
                     "multiply_temp_variable", "modulo_temp_variable", "clamp_temp_variable"):
                key = item(v, "var", v[0].key)
                key = self.targeted(key)
                value_token = item(v, "value", v[0].value)
                old = self.value(key) if "temp_variable" in k else self.current.variables.get(key, ZERO)
                if k == "clamp_temp_variable":
                    result = min(max(old, self.value(item(v, "min"))), self.value(item(v, "max")))
                else:
                    value = self.value(value_token)
                    if k.startswith("set_"):
                        result = value
                    elif k.startswith("add_"):
                        result = old + value
                    elif k.startswith("subtract_"):
                        result = old - value
                    elif k.startswith("multiply_"):
                        result = old * value
                    else:
                        result = old % value
                if "temp_variable" in k:
                    self.temp(key, result)
                else:
                    self.current.variables[key] = result
            elif k == "clear_variable":
                self.current.variables.pop(self.targeted(v), None)
            elif k == "round_temp_variable":
                self.temp(v, self.value(v).quantize(D(1), rounding=ROUND_HALF_UP))
            elif k in ("set_country_flag", "clr_country_flag"):
                if self.current.kind != "country":
                    self.unmodeled(n)
                if isinstance(v, list):
                    if k != "set_country_flag" or {child.key for child in v} != {"flag", "days"}:
                        self.unmodeled(n)
                    flag, duration = item(v, "flag"), item(v, "days")
                    self.current.timed_flags[flag] = self.value(duration.removeprefix("var:"))
                    v = flag
                if k.startswith("set"):
                    self.current.flags.add(v)
                else:
                    self.current.flags.discard(v)
            elif k == "save_event_target_as":
                self.targets[v] = self.current
            elif k in ("clear_array", "add_to_array", "remove_from_array", "clear_temp_array", "add_to_temp_array"):
                temporary = "temp_array" in k
                key = v if isinstance(v, str) else item(v, "array")
                key = self.targeted(key)
                owner = self.temp_owner(key, True) if temporary else self.current.arrays
                if owner is None:
                    owner = self.frames[-1].arrays
                if k.startswith("clear"):
                    owner[key] = []
                elif k.startswith("add"):
                    owner.setdefault(key, []).append(self.value(item(v, "value")))
                else:
                    val = self.value(item(v, "value"))
                    owner[key] = [x for x in owner.get(key, []) if x != val]
            elif k == "meta_effect":
                self.meta(v)
            elif k == "for_each_loop":
                key = self.targeted(item(v, "array"))
                owner = self.temp_owner(key, True)
                rows = (self.current.arrays if owner is None else owner).get(key, [])
                if len(rows) > 1000:
                    raise AssertionError("Unmodeled for_each_loop tail beyond 1,000 rows")
                # These selector loops freeze their working handle set explicitly.
                # Mutation of the iterated array itself is outside this model.
                frozen = list(rows)
                value_key, index_key = item(v, "value", "v"), item(v, "index", "i")
                break_key = item(v, "break", "break")
                # Preserve caller storage. Resetting here would mask production
                # collectors that inherit default break=1 or stale private breaks.
                body = [child for child in v if child.key not in ("array", "value", "index", "break")]
                for index, value in enumerate(frozen):
                    self.temp(value_key, value)
                    self.temp(index_key, D(index))
                    self.execute(body)
                    if list(rows) != frozen:
                        raise AssertionError("Unmodeled mutation of iterated array")
                    if self.value(break_key) != ZERO:
                        break
            elif k == "add_equipment_to_stockpile":
                if any(child.key not in ("type", "amount") for child in v):
                    raise AssertionError("Unmodeled native stock argument (producer/variant/etc.)")
                model, amount = item(v, "type"), self.value(item(v, "amount"))
                profile_wastage = any(" cbrn_remove_air_profile_wastage_internal [" in entry
                                      for entry in self.trace)
                # Quarantined-owner tests execute the full destruction helper
                # with explicitly empty free stock. Its zero-amount native calls
                # are retained as calls, never silently omitted or paid twice.
                sanctions_zero = amount == ZERO and any(" condemnation_destroy_chemical_stockpiles [" in entry
                                                         for entry in self.trace)
                if self.measurement is None and not profile_wastage and not sanctions_zero:
                    raise AssertionError("Native stock mutation outside measured primitive")
                outcome = self.measurement if self.measurement is not None else Outcome()
                actual_model = outcome.actual_model or model
                delta = amount * D(outcome.fraction)
                if delta != ZERO or actual_model in self.current.stocks:
                    self.current.stocks[actual_model] = self.current.stocks.get(actual_model, ZERO) + delta
                self.nativecalls.append((self.current.name, model, amount, actual_model, delta))
            elif k in self.source.effects:
                if v != "yes":
                    self.unmodeled(n)
                self.call(k)
            elif k.startswith(("var:", "event_target:")) or k in ("ROOT", "PREV", "THIS", "CONTROLLER"):
                self.enter(self.scope(k), v)
            else:
                self.unmodeled(n)


SOURCE = None
COVERAGE = Counter()


class ChemicalReceipts(unittest.TestCase):
    def test_selected_payload_affordability_rejects_wrong_or_missing_real_stock(self):
        predicate = 'missiles_selected_payload_can_be_reserved'
        for agent in AGENTS:
            for balance in (D(239), D(240)):
                with self.subTest(payload='chemical', agent=agent, balance=balance):
                    self.setUp()
                    self.configure(agent)
                    self.actor.variables['missiles_selected_payload'] = self.c('missiles_payload.chemical')
                    self.actor.variables['missiles_selected_chemical_agent'] = self.c(f'cbrn_agent.{agent}')
                    self.actor.stocks[self.model] = balance
                    before = self.snapshot_scope(self.actor)
                    self.assertEqual(self.m.call(predicate, trigger=True), balance >= self.cost)
                    self.assertEqual(self.snapshot_scope(self.actor), before)
                    self.assertEqual(self.m.nativecalls, [])
                    if balance == self.cost:
                        self.reserve()
                        self.actor.stocks[self.model] = balance
                        self.assertFalse(self.m.call(predicate, trigger=True), 'held consumer cannot open another preparation')
                    COVERAGE.update(self.m.calls)
        for agent in ('anthrax', 'plague', 'tularemia', 'smallpox'):
            with self.subTest(payload='biological', agent=agent):
                self.setUp()
                self.actor.variables['missiles_selected_payload'] = self.c('missiles_payload.biological')
                self.actor.variables['missiles_selected_biological_agent'] = self.c(f'bio_lifecycle_agent.{agent}')
                self.actor.techs.add(f'{agent}_bomb_delivery_systems')
                self.assertFalse(self.m.call(predicate, trigger=True))
                self.actor.stocks[f'{agent}_bomb_1'] = self.c('missiles_resolution.biological_payload_units')
                self.assertTrue(self.m.call(predicate, trigger=True))
                self.actor.techs.discard(f'{agent}_bomb_delivery_systems')
                self.assertFalse(self.m.call(predicate, trigger=True))
                self.assertEqual(self.m.nativecalls, [])
                COVERAGE.update(self.m.calls)
        for payload in ('nuclear', 'thermonuclear'):
            with self.subTest(payload=payload):
                self.setUp()
                self.actor.variables['missiles_selected_payload'] = self.c(f'missiles_payload.{payload}')
                self.actor.techs.update({'atomic_research', 'nukes', 'thermonuclear_bombs'})
                self.actor.variables['num_of_nukes'] = ZERO
                self.assertFalse(self.m.call(predicate, trigger=True))
                self.actor.variables['num_of_nukes'] = self.c('missiles_resolution.nuclear_payload_units')
                self.assertTrue(self.m.call(predicate, trigger=True))
                self.actor.techs.discard('nukes')
                self.assertFalse(self.m.call(predicate, trigger=True))
                self.assertEqual(self.m.nativecalls, [])
                COVERAGE.update(self.m.calls)

    def test_read_only_preparation_quote_uses_exact_shared_agent_and_stock(self):
        for agent in AGENTS:
            for balance in (D(239), D(240), D(241)):
                with self.subTest(agent=agent, balance=balance):
                    self.setUp()
                    self.configure(agent)
                    self.actor.stocks[self.model] = balance
                    self.m.temp('cbrn_action_agent', self.c(f'cbrn_agent.{agent}'))
                    before = self.snapshot_scope(self.actor)
                    self.assertEqual(self.m.call('cbrn_air_payload_can_fund_strategic_action', trigger=True), balance >= self.cost)
                    self.assertEqual(self.snapshot_scope(self.actor), before)
                    self.assertEqual(self.m.nativecalls, [])
                    self.actor.variables['cbrn_air_payload_agent'] = ZERO
                    self.assertFalse(self.m.call('cbrn_air_payload_can_fund_strategic_action', trigger=True))
                    COVERAGE.update(self.m.calls)

    def test_read_only_consumer_quote_blocks_held_but_not_copied_foreign_slot(self):
        self.m.temp('cbrn_payload_lookup_consumer', self.c('cbrn_payload_receipt_consumer.missiles'))
        predicate = 'cbrn_payload_consumer_has_no_open_receipt'
        self.assertTrue(self.m.call(predicate, trigger=True))
        self.reserve()
        self.assertFalse(self.m.call(predicate, trigger=True))
        self.actor.variables['cbrn_payload_ledger_owner_id'] = D(self.foreign.identity)
        before = self.snapshot_scope(self.actor)
        self.assertTrue(self.m.call(predicate, trigger=True))
        self.assertEqual(self.snapshot_scope(self.actor), before)

    def setUp(self):
        self.s = SOURCE
        self.actor = Scope("actor", 11)
        self.enemy = Scope("enemy", 22)
        self.foreign = Scope("foreign", 33)
        self.site = Scope("site", 101, "state", controller=self.actor)
        self.target = Scope("target", 202, "state", controller=self.enemy)
        self.actor.wars.add(self.enemy)
        self.enemy.wars.add(self.actor)
        self.m = Machine(self.s, self.actor)
        self.configure()

    def tearDown(self):
        COVERAGE.update(self.m.calls)

    def c(self, name):
        return self.s.constant(name)

    def configure(self, agent="chlorine", route="strategic_chemical_raid", who=None):
        who = who or self.actor
        kind, tech, project = AGENTS[agent]
        who.techs = {"chemical_air_interdiction"}
        who.projects = set()
        if tech:
            who.techs.add(tech)
        if project:
            who.projects.add(project)
        who.variables.update({"cbrn_air_payload_agent": self.c(f"cbrn_agent.{agent}"),
                              "cbrn_use_policy": self.c("cbrn_use_policy.unrestricted_authorization"),
                              "cbrn_payload_request_consumer": self.c("cbrn_payload_receipt_consumer.missiles"),
                              "cbrn_payload_request_nonce": D(1),
                              "cbrn_payload_request_site": self.site,
                              "cbrn_payload_request_target": self.target,
                              "cbrn_payload_request_agent": self.c(f"cbrn_agent.{agent}"),
                              "cbrn_payload_request_route": self.c(f"cbrn_delivery_route.{route}"),
                              "cbrn_payload_custody_proof": self.c("cbrn_proof.supplied"),
                              "cbrn_payload_recovery_proof": self.c("cbrn_proof.supplied")})
        model = f"{kind}_chemical_air_payload_lot_1"
        cost = self.c(f"cbrn_payload_route_cost.{route}")
        who.stocks = {name: ZERO for name in MODELS}
        who.stocks[model] = cost
        self.model, self.cost = model, cost

    def call(self, name, who=None, root=None):
        self.m.current = who or self.actor
        self.m.root = root or self.m.current
        self.m.call(name)

    def reserve(self):
        self.call("cbrn_reserve_action_payload")
        self.assert_result("accepted")
        handle = self.actor.variables["cbrn_payload_handle"]
        self.actor.variables["cbrn_payload_request_handle"] = handle
        return int(handle)

    def row(self, key, handle=1, who=None):
        return (who or self.actor).variables.get(f"cbrn_payload_receipt_{key}_{handle}", ZERO)

    def assert_result(self, result, who=None):
        self.assertEqual((who or self.actor).variables["cbrn_payload_result"],
                         self.c(f"cbrn_payload_receipt_result.{result}"))

    def assert_totals(self, held, captured=0, bound=0, quarantined=0, who=None):
        v = (who or self.actor).variables
        self.assertEqual(tuple(v[f"cbrn_payload_{k}"] for k in
                               ("held_total", "captured_total", "profile_bound_count", "quarantined_count")),
                         tuple(map(D, (held, captured, bound, quarantined))))

    def snapshot_scope(self, who):
        return (dict(who.variables), {key: list(values) for key, values in who.arrays.items()},
                set(who.flags), set(who.techs), set(who.projects), dict(who.stocks), dict(who.timed_flags))

    def prepare_other_actor_hold(self, agent="chlorine"):
        self.configure(agent, who=self.enemy)
        other_site = Scope("other_actor_site", 707, "state", controller=self.enemy)
        self.enemy.variables["cbrn_payload_request_site"] = other_site
        self.enemy.variables["cbrn_payload_request_target"] = self.site
        self.call("cbrn_reserve_action_payload", self.enemy)
        self.assert_result("accepted", self.enemy)
        self.assert_totals(self.cost, bound=1, who=self.enemy)
        return self.snapshot_scope(self.enemy)

    def prepare_event32_receipt(self, agent="chlorine"):
        """Scope fixture for the public receipt adapter, not full launch orchestration."""
        self.configure(agent)
        for key in ("cbrn_payload_custody_proof", "cbrn_payload_recovery_proof",
                    "cbrn_payload_transfer_proof", "cbrn_payload_loss_proof"):
            self.actor.variables.pop(key, None)
        self.actor.variables.update({
            "missiles_active_operation_id": D(42),
            "missiles_operation_launch_site": self.site,
            "missiles_operation_launch_site_id": D(self.site.identity),
            "missiles_operation_target_state": self.target,
            "missiles_operation_target_state_id": D(self.target.identity),
            "missiles_operation_payload": self.c("missiles_payload.chemical"),
            "missiles_operation_state": self.c("missiles_operation_state.resources_reserved"),
            "missiles_operation_type": self.c("missiles_operation.precision"),
            "missiles_selected_chemical_agent": self.c(f"cbrn_agent.{agent}"),
            "missiles_special_payload_policy": self.c("missiles_special_payload_policy.unrestricted_war"),
            "missiles_operation_payload_reservation_result": self.c("missiles_result.rejected"),
        })
        self.actor.flags.update({"missiles_operation_active", "missiles_special_payload_selected",
                                 "missiles_evolution_special_warheads", "missiles_chemical_integration_operational"})
        self.site.flags.update({"missiles_site_active", "missiles_site_special_payload_custody",
                                "missiles_site_custody_chemical"})
        self.site.variables["missiles_site_capacity"] = self.c("missiles_site_capacity.initial")
        self.site.variables["missiles_site_operation_id"] = D(42)
        self.call("missiles_reserve_chemical_payload_receipt")
        self.assertEqual(self.actor.variables["missiles_operation_payload_reservation_result"], self.c("missiles_result.accepted"))
        self.assertIn("missiles_operation_chemical_receipt_active", self.actor.flags)
        self.assertEqual(self.actor.variables["missiles_operation_chemical_receipt"], 1)
        self.assertEqual(self.actor.variables["missiles_operation_chemical_agent"], self.c(f"cbrn_agent.{agent}"))
        self.assertEqual(self.row("nonce"), 42)
        self.assertEqual(self.row("site_id"), self.site.identity)
        self.assertEqual(self.row("target_id"), self.target.identity)
        self.assertEqual(self.row("model"), self.model)
        self.assertEqual(self.row("held"), 240)
        self.assertEqual(self.actor.stocks[self.model], 0)
        self.assertEqual(self.m.nativecalls, [("actor", self.model, -D(240), self.model, -D(240))])

    def test_event32_public_receipt_adapter_prepare_commit_consume_no_second_debit(self):
        for agent in ("chlorine", "mustard", "tabun", "malodor"):
            with self.subTest(agent=agent):
                self.setUp()
                self.prepare_event32_receipt(agent)
                # A mutable UI selector cannot relabel the frozen chemical order.
                self.actor.variables["missiles_selected_chemical_agent"] = self.c("cbrn_agent.phosgene")
                self.call("missiles_check_chemical_receipt_for_commit")
                self.assertEqual(self.actor.variables["missiles_chemical_stock_result"], self.c("missiles_result.accepted"))
                self.assertEqual(len(self.m.nativecalls), 1)
                self.call("missiles_consume_chemical_payload_receipt")
                self.assertEqual(self.actor.variables["missiles_operation_payload_consumed"], 240)
                self.assertIn("missiles_operation_payload_debit_verified", self.actor.flags)
                self.assertNotIn("missiles_operation_chemical_receipt_active", self.actor.flags)
                self.assertEqual(self.actor.variables["missiles_operation_chemical_agent"], self.c(f"cbrn_agent.{agent}"))
                self.assertEqual(self.row("consumed"), 240)
                self.assertEqual(self.row("held"), 0)
                self.assertEqual(len(self.m.nativecalls), 1)
                self.call("missiles_consume_chemical_payload_receipt")
                self.assertEqual(self.actor.variables["missiles_operation_payload_consumed"], 0)
                self.assertNotIn("missiles_operation_payload_debit_verified", self.actor.flags)
                self.call("missiles_release_chemical_payload_receipt")
                self.assertEqual(len(self.m.nativecalls), 1)
                self.assertEqual(self.actor.stocks[self.model], 0)
                COVERAGE.update(self.m.calls)

    def test_event32_caller_rejects_current_eligibility_changes(self):
        for reason in ("technology", "profile", "policy", "source", "missile_custody", "evolution_toggle", "nonce", "target_id"):
            with self.subTest(reason=reason):
                self.setUp()
                self.prepare_event32_receipt()
                if reason == "technology":
                    self.actor.techs.clear()
                elif reason == "profile":
                    self.actor.variables["cbrn_air_payload_agent"] = self.c("cbrn_agent.phosgene")
                elif reason == "policy":
                    self.actor.variables["cbrn_use_policy"] = ZERO
                elif reason == "source":
                    self.site.controller = self.foreign
                elif reason == "missile_custody":
                    self.site.flags.discard("missiles_site_custody_chemical")
                elif reason == "evolution_toggle":
                    self.m.global_flags.add("events_log_disabled_evolution_32_32_3")
                elif reason == "nonce":
                    self.actor.variables["missiles_active_operation_id"] = D(999)
                else:
                    self.actor.variables["missiles_operation_target_state_id"] = D(999)
                self.call("missiles_check_chemical_receipt_for_commit")
                self.assertEqual(self.actor.variables["missiles_chemical_stock_result"], self.c("missiles_result.rejected"))
                self.call("missiles_consume_chemical_payload_receipt")
                self.assertEqual(self.actor.variables["missiles_operation_payload_consumed"], 0)
                self.assertNotIn("missiles_operation_payload_debit_verified", self.actor.flags)
                self.assertEqual(self.row("held"), 240)
                self.assertEqual(len(self.m.nativecalls), 1)
                COVERAGE.update(self.m.calls)

    def test_event32_actual_release_twice_voluntary_and_foreign_root_loss_variants(self):
        for disposition in ("voluntary", "other_participant", "primary_capture", "primary_destroy"):
            with self.subTest(disposition=disposition):
                self.setUp()
                self.prepare_event32_receipt()
                root = self.actor if disposition == "voluntary" else self.foreign
                if disposition != "voluntary":
                    self.actor.flags.add("missiles_site_settlement_in_progress")
                    self.actor.variables["missiles_payload_custody_action"] = self.c(
                        "cbrn_payload_site_action.destroy" if disposition == "primary_destroy" else "cbrn_payload_site_action.capture")
                    if disposition == "other_participant":
                        lost = Scope("lost_other_participant", 808, "state", controller=self.foreign)
                    else:
                        lost = self.site
                        self.site.controller = self.foreign
                        self.site.flags.add("missiles_site_captured" if disposition == "primary_capture" else "missiles_site_scuttled")
                    self.m.targets["missiles_lost_allocation_site"] = lost
                self.call("missiles_release_chemical_payload_receipt", root=root)
                self.assertNotIn("missiles_operation_chemical_receipt_active", self.actor.flags)
                self.assertNotIn("missiles_operation_chemical_receipt", self.actor.variables)
                self.assertEqual(self.row("held"), 0)
                if disposition in ("voluntary", "other_participant"):
                    self.assertEqual(self.row("returned"), 240)
                    self.assertEqual(self.actor.stocks[self.model], 240)
                    self.assertEqual(self.m.nativecalls[-1], ("actor", self.model, D(240), self.model, D(240)))
                    self.assertEqual(len(self.m.nativecalls), 2)
                    self.assertEqual(self.foreign.stocks, {})
                elif disposition == "primary_capture":
                    self.assertEqual(self.row("transferred"), 240)
                    self.assertEqual(self.row("held", who=self.foreign), 240)
                    self.assertEqual(self.row("agent", who=self.foreign), self.c("cbrn_agent.chlorine"))
                    self.assertEqual(self.row("model", who=self.foreign), self.model)
                    self.assertEqual(self.foreign.stocks, {})
                    self.assertEqual(self.actor.stocks[self.model], 0)
                    self.assertEqual(len(self.m.nativecalls), 1)
                else:
                    self.assertEqual(self.row("destroyed"), 240)
                    self.assertEqual(self.foreign.variables, {})
                    self.assertEqual(self.actor.stocks[self.model], 0)
                    self.assertEqual(len(self.m.nativecalls), 1)
                snapshot = (self.snapshot_scope(self.actor), self.snapshot_scope(self.foreign), list(self.m.nativecalls))
                self.call("missiles_release_chemical_payload_receipt", root=root)
                self.assertEqual((self.snapshot_scope(self.actor), self.snapshot_scope(self.foreign), self.m.nativecalls), snapshot)
                COVERAGE.update(self.m.calls)

    def test_event32_fractional_disposal_rejects_commit_and_cleanup_returns_only_sixty(self):
        self.prepare_event32_receipt()
        self.m.temp("cbrn_payload_disposal_fraction", self.c("condemnation_cost.chemical_stockpile_fraction"))
        self.call("cbrn_dispose_reserved_payload_fraction")
        self.assertEqual(self.row("destroyed"), 180)
        self.call("missiles_check_chemical_receipt_for_commit")
        self.assertEqual(self.actor.variables["missiles_chemical_stock_result"], self.c("missiles_result.rejected"))
        self.call("missiles_consume_chemical_payload_receipt")
        self.assertEqual(self.actor.variables["missiles_operation_payload_consumed"], 0)
        self.assertNotIn("missiles_operation_payload_debit_verified", self.actor.flags)
        self.assertEqual(len(self.m.nativecalls), 1)
        self.call("missiles_release_chemical_payload_receipt", root=self.foreign)
        self.assertEqual(self.row("returned"), 60)
        self.assertEqual(self.actor.stocks[self.model], 60)
        self.assertEqual(self.row("destroyed"), 180)
        self.assertEqual(len(self.m.nativecalls), 2)
        self.assertEqual(self.m.nativecalls[-1], ("actor", self.model, D(60), self.model, D(60)))
        self.call("missiles_release_chemical_payload_receipt", root=self.foreign)
        self.assertEqual(len(self.m.nativecalls), 2)

    def test_event32_adapter_leaves_stock_mapping_in_cbrn(self):
        def walk(nodes):
            for node in nodes:
                yield node
                if isinstance(node.value, list):
                    yield from walk(node.value)

        for name, (body, _, path, _) in self.s.effects.items():
            if not path.endswith("032_missiles_payload_receipt_effects.txt"):
                continue
            with self.subTest(helper=name):
                for node in walk(body):
                    self.assertNotIn(node.key, ("add_equipment_to_stockpile", "cbrn_payload_measure_model_debit",
                                               "cbrn_payload_measure_model_credit", "cbrn_payload_resolve_air_model"))
                    if isinstance(node.value, str):
                        self.assertFalse(node.value.startswith("num_equipment@"))
                        self.assertNotIn(node.value.removeprefix("token:"), MODELS)
        # This source-boundary check supplements the actual caller paths above.

    def test_event32_owning_special_payload_consumer_rejects_duplicate_release(self):
        self.prepare_event32_receipt()
        self.call("missiles_consume_special_payload")
        self.assertEqual(self.actor.variables["missiles_operation_payload_consumed"], 240)
        self.assertIn("missiles_operation_payload_debit_verified", self.actor.flags)
        self.assertNotIn("missiles_operation_chemical_receipt_active", self.actor.flags)
        self.assertEqual(self.row("consumed"), 240)
        self.assertEqual(len(self.m.nativecalls), 1)
        self.call("missiles_consume_special_payload")
        self.assertEqual(self.actor.variables["missiles_operation_payload_consumed"], 0)
        self.assertNotIn("missiles_operation_payload_debit_verified", self.actor.flags)
        self.assertEqual(self.row("consumed"), 240)
        self.call("missiles_release_chemical_payload_receipt")
        self.call("missiles_release_chemical_payload_receipt")
        self.assertEqual(self.row("returned"), 0)
        self.assertEqual(self.actor.stocks[self.model], 0)
        self.assertEqual(len(self.m.nativecalls), 1)
        self.assertEqual(self.m.calls["missiles_consume_chemical_payload"], 2)

    def test_fractional_disposal_invalidates_preparation_and_returns_only_remainder(self):
        for agent in ("chlorine", "mustard", "tabun", "malodor"):
            with self.subTest(agent=agent):
                self.setUp()
                self.configure(agent)
                self.reserve()
                other_before = self.prepare_other_actor_hold(agent)
                self.assertEqual(self.cost, 240)
                self.m.temp("cbrn_payload_disposal_fraction", self.c("condemnation_cost.chemical_stockpile_fraction"))
                self.assertEqual(self.m.value("cbrn_payload_disposal_fraction"), D("0.75"))
                for key in ("break", "cbrn_payload_disposal_collect_break", "cbrn_payload_disposal_apply_break"):
                    self.m.temp(key, D(1))
                native_before = list(self.m.nativecalls)
                self.call("cbrn_dispose_reserved_payload_fraction", root=self.foreign)
                self.assert_result("accepted")
                self.assertEqual(self.actor.variables["cbrn_payload_result_amount"], 180)
                self.assertEqual(self.row("destroyed"), 180)
                self.assertEqual(self.row("held"), 60)
                self.assertEqual(self.row("reserved"), 240)
                self.assertEqual(self.row("phase"), self.c("cbrn_payload_receipt_phase.recovery_pending"))
                self.assert_totals(60, bound=1)
                self.assertEqual(self.m.nativecalls, native_before)
                self.assertEqual(self.m.value("cbrn_payload_disposal_fraction"), D("0.75"))
                self.assertEqual(self.m.value("break"), 1)
                self.assertIsNone(self.m.temp_owner("cbrn_payload_disposal_handles", True))
                self.assertEqual(self.snapshot_scope(self.enemy), other_before)
                self.m.current = self.actor
                self.assertTrue(self.m.call("condemnation_has_chemical_stockpile", True))
                for _ in range(2):
                    self.call("cbrn_payload_refresh_reservation_counts")
                    self.assert_totals(60, bound=1)
                    self.assertEqual(self.row("destroyed"), 180)
                self.call("cbrn_validate_payload_reservation")
                self.assertEqual(self.actor.variables["cbrn_payload_validation_result"],
                                 self.c("cbrn_payload_receipt_result.rejected"))
                self.call("cbrn_consume_payload_reservation")
                self.assert_result("rejected")
                self.call("cbrn_reserve_action_payload")
                self.assert_result("rejected")
                self.assertEqual(self.m.nativecalls, native_before)
                self.assertEqual(self.actor.stocks[self.model], 0)
                self.call("cbrn_return_payload_reservation")
                self.assert_result("accepted")
                self.assertEqual(self.actor.variables["cbrn_payload_result_amount"], 60)
                self.assertEqual(self.actor.stocks[self.model], 60)
                self.assertEqual(self.row("returned"), 60)
                self.assertEqual(self.row("destroyed"), 180)
                self.assertEqual(self.row("returned") + self.row("destroyed"), self.row("reserved"))
                self.assertEqual(self.m.nativecalls[len(native_before):], [("actor", self.model, D(60), self.model, D(60))])
                self.call("cbrn_return_payload_reservation")
                self.assert_result("already_settled")
                self.call("cbrn_dispose_reserved_payload_fraction")
                self.assert_result("accepted")
                self.assertEqual(self.actor.variables["cbrn_payload_result_amount"], 0)
                self.assertEqual(self.actor.stocks[self.model], 60)
                self.assert_totals(0)
                self.assertEqual(self.snapshot_scope(self.enemy), other_before)
                COVERAGE.update(self.m.calls)

    def test_fractional_disposal_of_sealed_capture_preserves_origin_and_only_integrates_remainder(self):
        for agent, (_, tech, project) in ((name, AGENTS[name]) for name in ("chlorine", "mustard", "tabun", "malodor")):
            with self.subTest(agent=agent):
                self.setUp()
                self.capture(agent)
                origin_before = self.snapshot_scope(self.actor)
                self.m.temp("cbrn_payload_disposal_fraction", self.c("condemnation_cost.chemical_stockpile_fraction"))
                native_before = list(self.m.nativecalls)
                self.call("cbrn_dispose_reserved_payload_fraction", self.foreign, self.actor)
                self.assert_result("accepted", self.foreign)
                self.assertEqual(self.foreign.variables["cbrn_payload_result_amount"], 180)
                self.assertEqual(self.row("phase", who=self.foreign), self.c("cbrn_payload_receipt_phase.captured"))
                self.assertEqual(self.row("held", who=self.foreign), 60)
                self.assertEqual(self.row("destroyed", who=self.foreign), 180)
                self.assertEqual(self.row("agent", who=self.foreign), self.c(f"cbrn_agent.{agent}"))
                self.assertEqual(self.row("received", who=self.foreign), 240)
                self.assertEqual(self.foreign.stocks, {})
                self.assertEqual(self.m.nativecalls, native_before)
                for _ in range(2):
                    self.call("cbrn_payload_refresh_reservation_counts", self.foreign)
                    self.assert_totals(60, captured=60, who=self.foreign)
                self.assertEqual(self.snapshot_scope(self.actor), origin_before)
                self.call("cbrn_integrate_captured_payload_reservation", self.foreign)
                self.assert_result("rejected", self.foreign)
                self.foreign.techs = {"chemical_air_interdiction"} | ({tech} if tech else set())
                self.foreign.projects = {project} if project else set()
                self.foreign.variables["cbrn_air_payload_agent"] = self.c(f"cbrn_agent.{agent}")
                self.call("cbrn_integrate_captured_payload_reservation", self.foreign)
                self.assert_result("accepted", self.foreign)
                self.assertEqual(self.foreign.stocks[self.model], 60)
                self.assertEqual(self.row("returned", who=self.foreign), 60)
                self.assertEqual(self.row("destroyed", who=self.foreign), 180)
                self.assertEqual(self.m.nativecalls[len(native_before):], [("foreign", self.model, D(60), self.model, D(60))])
                self.assert_totals(0, who=self.foreign)
                self.assertEqual(self.snapshot_scope(self.actor), origin_before)
                COVERAGE.update(self.m.calls)

    def test_quarantined_disposal_blocks_owner_rewards_and_keeps_presence(self):
        for captured in (False, True):
            with self.subTest(captured=captured):
                self.setUp()
                if captured:
                    self.capture()
                    holder = self.foreign
                    holder.variables["cbrn_payload_receipt_phase_1"] = self.c("cbrn_payload_receipt_phase.captured_quarantined")
                    self.call("cbrn_payload_refresh_reservation_counts", holder)
                    expected_held = D(240)
                    origin_before = self.snapshot_scope(self.actor)
                else:
                    self.m.outcomes["debit"].append(Outcome(after=D(-1)))
                    self.call("cbrn_reserve_action_payload")
                    self.assert_result("quarantined")
                    holder = self.actor
                    expected_held = ZERO
                    origin_before = self.snapshot_scope(self.foreign)
                holder.variables["condemnation_decay_credit"] = D(7)
                holder.variables["condemnation_compliance_state"] = D(999)
                self.m.current = holder
                self.assertTrue(self.m.call("condemnation_has_chemical_stockpile", True))
                receipt_before = {key: value for key, value in holder.variables.items()
                                  if key.startswith("cbrn_payload_receipt_")}
                self.m.temp("cbrn_payload_disposal_fraction", self.c("condemnation_cost.chemical_stockpile_fraction"))
                self.call("cbrn_dispose_reserved_payload_fraction", holder)
                self.assert_result("quarantined", holder)
                self.assertEqual(holder.variables["cbrn_payload_result_amount"], 0)
                native_before = len(self.m.nativecalls)
                self.call("condemnation_destroy_chemical_stockpiles", holder)
                self.assert_result("quarantined", holder)
                self.assertEqual(holder.variables["cbrn_payload_result_amount"], 0)
                self.assertEqual(holder.variables["condemnation_decay_credit"], 7)
                self.assertEqual(holder.variables["condemnation_compliance_state"], 999)
                for flag in ("condemnation_stockpiles_destroyed", "condemnation_chemical_stockpiles_destroyed",
                             "condemnation_chemical_stockpile_restriction"):
                    self.assertNotIn(flag, holder.flags)
                    self.assertNotIn(flag, holder.timed_flags)
                self.assertEqual(self.m.calls["condemnation_apply_response_duration"], 0)
                self.assertEqual(self.m.calls["cbrn_achievement_record_stockpile_destruction"], 0)
                calls = self.m.nativecalls[native_before:]
                self.assertTrue(calls)  # Owner really executed its free-stock path.
                self.assertTrue(all(call[0] == holder.name and call[2] == ZERO and call[4] == ZERO for call in calls))
                for _ in range(2):
                    self.call("cbrn_payload_refresh_reservation_counts", holder)
                    self.assert_totals(expected_held, captured=expected_held if captured else 0,
                                       bound=0 if captured else 1, quarantined=1, who=holder)
                self.assertEqual({key: holder.variables[key] for key in receipt_before}, receipt_before)
                self.assertEqual(self.row("destroyed", who=holder), 0)
                self.assertEqual(self.snapshot_scope(self.actor if captured else self.foreign), origin_before)
                self.m.current = holder
                self.assertTrue(self.m.call("condemnation_has_chemical_stockpile", True))
                COVERAGE.update(self.m.calls)

    def test_all_agents_reserve_duplicate_consume_once(self):
        for agent in AGENTS:
            with self.subTest(agent=agent):
                self.setUp()
                self.configure(agent)
                handle = self.reserve()
                self.assertEqual(self.row("agent", handle), self.c(f"cbrn_agent.{agent}"))
                self.assertEqual(self.row("model", handle), self.model)
                self.assertEqual(self.actor.stocks[self.model], 0)
                self.assert_totals(self.cost, bound=1)
                self.call("cbrn_reserve_action_payload")
                self.assert_result("accepted")
                self.assertEqual(self.actor.variables["cbrn_payload_handle"], handle)
                self.assertEqual(len(self.m.nativecalls), 1)
                self.call("cbrn_consume_payload_reservation")
                self.assert_result("accepted")
                self.assertEqual(self.row("consumed"), self.cost)
                self.assertEqual(self.actor.variables["cbrn_payload_consumed_agent"], self.c(f"cbrn_agent.{agent}"))
                self.assertEqual(self.actor.variables["cbrn_payload_consumed_model"], self.model)
                self.assertEqual(self.actor.variables["cbrn_payload_consumed_class"],
                                 self.c(f"cbrn_agent_class.{AGENTS[agent][0]}"))
                self.assert_totals(0)
                self.assertNotIn("cbrn_payload_receipt_site_1", self.actor.variables)
                self.call("cbrn_consume_payload_reservation")
                self.assert_result("rejected")
                self.assertEqual(self.actor.variables["cbrn_payload_result_amount"], 0)
                self.call("cbrn_return_payload_reservation")
                self.assert_result("already_settled")
                self.call("cbrn_reserve_action_payload")
                self.assert_result("rejected")
                self.assertEqual(len(self.m.nativecalls), 1)
                COVERAGE.update(self.m.calls)

    def test_all_agents_return_twice(self):
        for agent in AGENTS:
            with self.subTest(agent=agent):
                self.setUp()
                self.configure(agent)
                self.reserve()
                self.call("cbrn_return_payload_reservation")
                self.assert_result("accepted")
                self.assertEqual(self.row("returned"), self.cost)
                self.assertEqual(self.actor.stocks[self.model], self.cost)
                self.call("cbrn_return_payload_reservation")
                self.assert_result("already_settled")
                self.assertEqual(len(self.m.nativecalls), 2)
                self.assert_totals(0)
                COVERAGE.update(self.m.calls)

    def test_partial_debit_and_partial_credit_all_models(self):
        for agent in ("chlorine", "mustard", "tabun", "malodor"):
            with self.subTest(agent=agent):
                self.setUp()
                self.configure(agent)
                self.m.outcomes["debit"].append(Outcome(fraction=D("0.5")))
                self.call("cbrn_reserve_action_payload")
                self.assert_result("partial")
                self.actor.variables["cbrn_payload_request_handle"] = D(1)
                self.assertEqual(self.row("held"), self.cost / 2)
                self.assertEqual(self.row("reserved"), self.cost / 2)
                self.assert_totals(self.cost / 2, bound=1)
                self.call("cbrn_reserve_action_payload")
                self.assert_result("rejected")
                self.call("cbrn_consume_payload_reservation")
                self.assert_result("rejected")
                self.assertEqual(len(self.m.nativecalls), 1)
                self.m.outcomes["credit"].append(Outcome(fraction=D("0.5")))
                self.call("cbrn_return_payload_reservation")
                self.assert_result("partial")
                self.assertEqual(self.row("held"), self.cost / 4)
                self.assertEqual(self.row("returned"), self.cost / 4)
                self.assert_totals(self.cost / 4, bound=1)
                self.call("cbrn_return_payload_reservation")
                self.assert_result("accepted")
                self.assertEqual(self.row("returned"), self.cost / 2)
                self.assertEqual(self.actor.stocks[self.model], self.cost)
                self.assert_totals(0)
                COVERAGE.update(self.m.calls)

    def test_invalid_measurement_quarantine(self):
        for kind in ("debit", "credit"):
            for outcome in (Outcome(after=D(-1)), Outcome(after=D(1000)),
                            Outcome(actual_model=MODELS[1], after=D(-1))):
                with self.subTest(kind=kind, outcome=outcome):
                    self.setUp()
                    if kind == "credit":
                        self.reserve()
                    self.m.outcomes[kind].append(outcome)
                    self.call("cbrn_reserve_action_payload" if kind == "debit" else "cbrn_return_payload_reservation")
                    self.assert_result("quarantined")
                    self.actor.variables["cbrn_payload_request_handle"] = D(1)
                    self.assertEqual(self.row("native_after"), outcome.after)
                    self.assertEqual(self.row("phase"), self.c("cbrn_payload_receipt_phase.quarantined"))
                    self.assert_totals(0 if kind == "debit" else self.cost, bound=1, quarantined=1)
                    before = len(self.m.nativecalls)
                    self.call("cbrn_return_payload_reservation")
                    self.call("cbrn_consume_payload_reservation")
                    self.call("cbrn_discard_payload_reservation")
                    self.assertEqual(len(self.m.nativecalls), before)
                    COVERAGE.update(self.m.calls)

    def test_wrong_model_payment_cannot_be_full_hold(self):
        self.m.outcomes["debit"].append(Outcome(actual_model=MODELS[1]))
        self.call("cbrn_reserve_action_payload")
        self.assert_result("partial")
        self.assertEqual(self.row("held"), 0)
        self.assertEqual(self.actor.stocks[self.model], self.cost)
        self.assertEqual(self.m.nativecalls[0][3], MODELS[1])
        self.setUp()
        self.reserve()
        self.m.outcomes["credit"].append(Outcome(actual_model=MODELS[1]))
        self.call("cbrn_return_payload_reservation")
        self.assert_result("partial")
        self.assertEqual(self.row("held"), self.cost)
        self.assertEqual(self.row("returned"), 0)
        self.assertEqual(self.actor.stocks[self.model], 0)
        self.assertEqual(self.m.nativecalls[-1][3], MODELS[1])

    def test_binding_rejections(self):
        changes = {"nonce": D(2), "consumer": D(999), "handle": D(999),
                   "agent": self.c("cbrn_agent.phosgene"),
                   "route": self.c("cbrn_delivery_route.chemical_air_raid"),
                   "site": Scope("other_site", 303, "state", controller=self.actor),
                   "target": Scope("other_target", 404, "state", controller=self.enemy)}
        for key, value in changes.items():
            with self.subTest(key=key):
                self.setUp()
                self.reserve()
                self.actor.variables[f"cbrn_payload_request_{key}"] = value
                self.call("cbrn_consume_payload_reservation")
                self.assert_result("rejected")
                self.assertEqual(self.row("held"), self.cost)
                self.assertEqual(len(self.m.nativecalls), 1)
                COVERAGE.update(self.m.calls)
        self.setUp()
        self.reserve()
        self.foreign.variables.update(self.actor.variables)
        self.call("cbrn_consume_payload_reservation", self.foreign)
        self.assert_result("rejected", self.foreign)
        self.assertEqual(self.row("held"), self.cost)
        self.assertEqual(len(self.m.nativecalls), 1)

    def test_real_authorization_rejections(self):
        for reason in ("tech", "air_tech", "profile", "profile_busy", "policy", "war", "target",
                       "custody", "source", "foreign_root", "stock", "agent", "route", "nonce"):
            with self.subTest(reason=reason):
                self.setUp()
                if reason == "tech":
                    self.actor.techs.discard("chlorine_gas")
                elif reason == "air_tech":
                    self.actor.techs.discard("chemical_air_interdiction")
                elif reason == "profile":
                    self.actor.variables["cbrn_air_payload_agent"] = self.c("cbrn_agent.phosgene")
                elif reason == "profile_busy":
                    self.actor.flags.add("cbrn_air_profile_change_in_progress")
                elif reason == "policy":
                    self.actor.variables["cbrn_use_policy"] = ZERO
                elif reason == "war":
                    self.enemy.wars.clear()
                elif reason == "target":
                    self.target.impassable = True
                elif reason == "custody":
                    self.actor.variables["cbrn_payload_custody_proof"] = ZERO
                elif reason == "source":
                    self.site.controller = self.enemy
                elif reason == "stock":
                    self.actor.stocks[self.model] = self.cost - 1
                elif reason in ("agent", "route", "nonce"):
                    self.actor.variables[f"cbrn_payload_request_{reason}"] = ZERO
                self.call("cbrn_reserve_action_payload", root=self.foreign if reason == "foreign_root" else None)
                self.assert_result("rejected")
                self.assertEqual(len(self.m.nativecalls), 0)
                self.assertNotIn("cbrn_payload_receipt_holder_id_1", self.actor.variables)
                COVERAGE.update(self.m.calls)

    def test_current_authorization_required_after_reserve(self):
        for reason in ("tech", "profile", "policy", "source", "model", "quantity"):
            with self.subTest(reason=reason):
                self.setUp()
                self.reserve()
                if reason == "tech":
                    self.actor.techs.clear()
                elif reason == "profile":
                    self.actor.variables["cbrn_air_payload_agent"] = self.c("cbrn_agent.phosgene")
                elif reason == "policy":
                    self.actor.variables["cbrn_use_policy"] = ZERO
                elif reason == "source":
                    self.site.controller = self.foreign
                elif reason == "model":
                    self.actor.variables["cbrn_payload_receipt_model_1"] = MODELS[1]
                else:
                    self.actor.variables["cbrn_payload_receipt_held_1"] -= 1
                self.call("cbrn_consume_payload_reservation")
                self.assert_result("rejected")
                self.assertEqual(len(self.m.nativecalls), 1)
                COVERAGE.update(self.m.calls)

    def test_validator_result_cannot_reuse_fresh_consumption_proof(self):
        self.reserve()
        self.call("cbrn_validate_payload_reservation")
        self.assertEqual(self.actor.variables["cbrn_payload_validation_result"],
                         self.c("cbrn_payload_receipt_result.accepted"))
        self.assert_result("accepted")  # Prior reserve result, not fresh consumption.
        self.assertEqual(self.row("consumed"), 0)
        self.actor.variables["cbrn_payload_request_nonce"] = D(999)
        self.call("cbrn_consume_payload_reservation")
        self.assert_result("rejected")
        self.assertEqual(self.actor.variables["cbrn_payload_result_amount"], 0)
        self.assertEqual(self.actor.variables["cbrn_payload_consumed_agent"], self.c("cbrn_agent.none"))
        self.assertEqual(self.row("held"), self.cost)
        self.assertEqual(len(self.m.nativecalls), 1)

    def test_closed_transition_after_actual_validator_returns(self):
        for phase in ("consumed", "returned", "destroyed", "transferred"):
            with self.subTest(phase=phase):
                self.setUp()
                self.reserve()
                injected = []

                def close_after_validation(machine):
                    self.assertEqual(self.actor.variables["cbrn_payload_validation_result"],
                                     self.c("cbrn_payload_receipt_result.accepted"))
                    # Explicit external transition between validation and mutation.
                    # This is a scenario input, not a mocked validator success.
                    machine.execute(parse(
                        f"set_variable = {{ cbrn_payload_receipt_held_1 = 0 }} "
                        f"set_variable = {{ cbrn_payload_receipt_phase_1 = constant:cbrn_payload_receipt_phase.{phase} }} "
                        f"set_variable = {{ cbrn_payload_receipt_{phase}_1 = {self.cost} }}"))
                    machine.call("cbrn_payload_retire_receipt")
                    injected.append(True)

                self.m.after_call["cbrn_validate_payload_reservation"] = close_after_validation
                self.call("cbrn_consume_payload_reservation")
                self.assertEqual(injected, [True])
                self.assert_result("rejected")
                self.assertEqual(self.actor.variables["cbrn_payload_result_amount"], 0)
                self.assertEqual(self.actor.variables["cbrn_payload_consumed_agent"], self.c("cbrn_agent.none"))
                self.assertEqual(self.row("phase"), self.c(f"cbrn_payload_receipt_phase.{phase}"))
                self.assertEqual(self.row(phase), self.cost)
                if phase != "consumed":
                    self.assertEqual(self.row("consumed"), 0)
                self.assertEqual(self.row("held"), 0)
                self.assertEqual(len(self.m.nativecalls), 1)
                self.assertEqual(self.actor.stocks[self.model], 0)
                self.assert_totals(0)
                COVERAGE.update(self.m.calls)

    def test_changed_binding_after_actual_validator_returns(self):
        for field in ("nonce", "agent", "target_id", "site_id", "holder_id", "quantity", "source_controller"):
            with self.subTest(field=field):
                self.setUp()
                self.reserve()
                injected = []

                def change_after_validation(machine):
                    self.assertEqual(self.actor.variables["cbrn_payload_validation_result"],
                                     self.c("cbrn_payload_receipt_result.accepted"))
                    if field == "source_controller":
                        self.site.controller = self.foreign
                    else:
                        key = "held" if field == "quantity" else field
                        self.actor.variables[f"cbrn_payload_receipt_{key}_1"] = D(999)
                    injected.append(True)

                self.m.after_call["cbrn_validate_payload_reservation"] = change_after_validation
                self.call("cbrn_consume_payload_reservation")
                self.assertEqual(injected, [True])
                self.assert_result("rejected")
                self.assertEqual(self.actor.variables["cbrn_payload_result_amount"], 0)
                self.assertEqual(self.row("consumed"), 0)
                self.assertEqual(self.row("held"), D(999) if field == "quantity" else self.cost)
                self.assertEqual(self.row("phase"), self.c("cbrn_payload_receipt_phase.held"))
                self.assertEqual(len(self.m.nativecalls), 1)
                COVERAGE.update(self.m.calls)

    def test_has_variable_temporary_presence_assumption_and_counterexample(self):
        self.m.temp("temporary_only", D(1))
        self.assertTrue(self.m.has_variable("temporary_only"))
        self.assertNotIn("temporary_only", self.actor.variables)
        self.m.temp_has_variable = False
        self.assertFalse(self.m.has_variable("temporary_only"))
        self.call("cbrn_reserve_action_payload")
        # Native docs only say 'exists in a scope'. A normal-only reading rejects
        # the shared target-supplied temporary before authorization reaches stock.
        self.assert_result("rejected")
        self.assertGreater(self.m.calls["cbrn_action_target_state_is_valid"], 0)
        self.m.temp("cbrn_action_payload_required", self.cost)
        self.assertFalse(self.m.call("cbrn_action_payload_stock_is_sufficient", True))
        self.assertEqual(self.m.nativecalls, [])

    def test_foreign_root_refund_ignores_lost_launch_eligibility(self):
        self.reserve()
        self.actor.techs.clear()
        self.actor.projects.clear()
        self.actor.variables["cbrn_use_policy"] = ZERO
        self.enemy.wars.clear()
        self.call("cbrn_return_payload_reservation", root=self.foreign)
        self.assert_result("accepted")
        self.assertEqual(self.m.nativecalls[-1][0], "actor")
        self.assertEqual(self.foreign.stocks, {})
        self.assertEqual(self.actor.stocks[self.model], self.cost)

    def capture(self, agent="chlorine"):
        self.configure(agent)
        self.reserve()
        self.site.controller = self.foreign
        self.actor.variables.update({"cbrn_payload_request_recipient": self.foreign,
                                     "cbrn_payload_transfer_proof": self.c("cbrn_proof.supplied")})
        self.call("cbrn_transfer_payload_reservation", root=self.foreign)
        self.assert_result("accepted")
        self.assertEqual(self.row("transferred"), self.cost)
        self.assertEqual(self.row("held"), 0)
        self.assertEqual(self.row("origin_id", who=self.foreign), self.actor.identity)
        self.assertEqual(self.row("agent", who=self.foreign), self.c(f"cbrn_agent.{agent}"))
        self.assertEqual(self.row("model", who=self.foreign), self.model)
        self.assertEqual(self.row("received", who=self.foreign), self.cost)
        self.assertEqual(self.foreign.techs, set())
        self.assertEqual(self.foreign.stocks, {})
        self.assert_totals(0)
        self.assert_totals(self.cost, captured=self.cost, who=self.foreign)
        self.foreign.variables.update({"cbrn_payload_request_handle": D(1),
                                       "cbrn_payload_request_consumer": self.c("cbrn_payload_receipt_consumer.missiles"),
                                       "cbrn_payload_request_nonce": D(1),
                                       "cbrn_payload_recovery_proof": self.c("cbrn_proof.supplied")})

    def test_capture_sealed_duplicate_and_integration(self):
        for agent, (_, tech, project) in AGENTS.items():
            with self.subTest(agent=agent):
                self.setUp()
                self.capture(agent)
                self.call("cbrn_transfer_payload_reservation", root=self.foreign)
                self.assertEqual(len(self.m.nativecalls), 1)
                self.assertEqual(self.foreign.variables["cbrn_payload_receipt_sequence"], 1)
                self.call("cbrn_return_payload_reservation", self.foreign)
                self.assert_result("quarantined", self.foreign)
                self.call("cbrn_integrate_captured_payload_reservation", self.foreign)
                self.assert_result("rejected", self.foreign)
                self.assertEqual(len(self.m.nativecalls), 1)
                self.foreign.techs = {"chemical_air_interdiction"} | ({tech} if tech else set())
                self.foreign.projects = {project} if project else set()
                other_agent = "chlorine" if agent != "chlorine" else "phosgene"
                self.foreign.variables["cbrn_air_payload_agent"] = self.c(f"cbrn_agent.{other_agent}")
                self.call("cbrn_integrate_captured_payload_reservation", self.foreign)
                self.assert_result("rejected", self.foreign)
                self.foreign.variables["cbrn_air_payload_agent"] = self.c(f"cbrn_agent.{agent}")
                self.call("cbrn_integrate_captured_payload_reservation", self.foreign)
                self.assert_result("accepted", self.foreign)
                self.assertEqual(self.foreign.stocks[self.model], self.cost)
                self.assertEqual(self.row("returned", who=self.foreign), self.cost)
                self.assert_totals(0, who=self.foreign)
                self.call("cbrn_integrate_captured_payload_reservation", self.foreign)
                self.assert_result("rejected", self.foreign)
                self.assertEqual(len(self.m.nativecalls), 2)
                COVERAGE.update(self.m.calls)

    def test_project_unlock_alternatives_are_actual_trigger_paths(self):
        for agent in ("sarin", "soman", "malodor", "behavioral"):
            with self.subTest(agent=agent):
                self.setUp()
                self.configure(agent)
                _, tech, project = AGENTS[agent]
                if tech:
                    self.actor.techs.discard(tech)
                self.reserve()  # Project alone, including Sarin and Soman alternatives.
                self.actor.projects.discard(project)
                self.call("cbrn_consume_payload_reservation")
                self.assert_result("rejected")
                self.assertEqual(self.row("held"), self.cost)
                self.assertEqual(len(self.m.nativecalls), 1)
                COVERAGE.update(self.m.calls)

    def test_capture_partial_integration_binds_only_remaining_quantity(self):
        self.capture()
        self.foreign.techs = {"chlorine_gas", "chemical_air_interdiction"}
        self.foreign.variables["cbrn_air_payload_agent"] = self.c("cbrn_agent.chlorine")
        self.m.outcomes["credit"].append(Outcome(fraction=D("0.5")))
        self.call("cbrn_integrate_captured_payload_reservation", self.foreign)
        self.assert_result("partial", self.foreign)
        self.assert_totals(self.cost / 2, bound=1, who=self.foreign)
        self.assertEqual(self.row("returned", who=self.foreign), self.cost / 2)
        self.call("cbrn_integrate_captured_payload_reservation", self.foreign)
        self.assert_result("rejected", self.foreign)
        self.foreign.variables["cbrn_air_payload_agent"] = self.c("cbrn_agent.phosgene")
        self.call("cbrn_return_payload_reservation", self.foreign)
        self.assert_result("rejected", self.foreign)
        self.assertEqual(len(self.m.nativecalls), 2)
        self.foreign.variables["cbrn_air_payload_agent"] = self.c("cbrn_agent.chlorine")
        self.call("cbrn_return_payload_reservation", self.foreign)
        self.assert_result("accepted", self.foreign)
        self.assertEqual(self.foreign.stocks[self.model], self.cost)
        self.assert_totals(0, who=self.foreign)

    def test_settlement_requires_exact_identity_and_physical_proof(self):
        for helper in ("cbrn_return_payload_reservation", "cbrn_discard_payload_reservation",
                       "cbrn_transfer_payload_reservation"):
            for reason in ("nonce", "consumer", "holder", "proof"):
                with self.subTest(helper=helper, reason=reason):
                    self.setUp()
                    self.reserve()
                    self.actor.variables["cbrn_payload_request_recipient"] = self.foreign
                    self.actor.variables["cbrn_payload_transfer_proof"] = self.c("cbrn_proof.supplied")
                    self.actor.variables["cbrn_payload_loss_proof"] = self.c("cbrn_proof.supplied")
                    if helper.endswith("transfer_payload_reservation"):
                        self.site.controller = self.foreign
                    if reason in ("nonce", "consumer"):
                        self.actor.variables[f"cbrn_payload_request_{reason}"] = D(999)
                    elif reason == "holder":
                        self.actor.variables["cbrn_payload_receipt_holder_id_1"] = D(999)
                    else:
                        proof = "recovery" if "return" in helper else "loss" if "discard" in helper else "transfer"
                        self.actor.variables[f"cbrn_payload_{proof}_proof"] = ZERO
                    self.call(helper, root=self.foreign)
                    self.assert_result("rejected")
                    self.assertEqual(self.row("held"), self.cost)
                    self.assertEqual(len(self.m.nativecalls), 1)
                    self.assertEqual(self.foreign.stocks, {})
                    COVERAGE.update(self.m.calls)

    def test_refund_cannot_follow_captured_source_or_changed_profile(self):
        for reason in ("source", "site_id", "profile", "removed_actor"):
            with self.subTest(reason=reason):
                self.setUp()
                self.reserve()
                if reason == "source":
                    self.site.controller = self.foreign
                elif reason == "site_id":
                    self.actor.variables["cbrn_payload_receipt_site_id_1"] = D(999)
                elif reason == "profile":
                    self.actor.variables["cbrn_air_payload_agent"] = self.c("cbrn_agent.phosgene")
                else:
                    self.actor.exists = False
                self.call("cbrn_return_payload_reservation", root=self.foreign)
                self.assert_result("rejected")
                self.assertEqual(self.row("held"), self.cost)
                self.assertEqual(len(self.m.nativecalls), 1)
                self.assert_totals(self.cost, bound=1)
                COVERAGE.update(self.m.calls)

    def test_native_zero_negative_and_invalid_observations_all_models(self):
        for model in MODELS:
            for kind in ("debit", "credit"):
                for stock, request, outcome, observed, valid, count in (
                    (D(0), D(0), Outcome(), D(0), D(1), 0),
                    (D(0), D(10), Outcome(), D(0 if kind == "debit" else 10), D(1), 0 if kind == "debit" else 1),
                    (D(20), D(-1), Outcome(), D(0), D(0), 0),
                    (D(-1), D(10), Outcome(), D(0), D(0), 0),
                    (D(20), D(10), Outcome(fraction=D(0)), D(0), D(1), 1),
                    (D(20), D(10), Outcome(after=D(40)), D(-20 if kind == "debit" else 20), D(0), 1),
                    (D(20), D(10), Outcome(after=D(0)), D(20 if kind == "debit" else -20), D(0), 1),
                    (D(20), D(10), Outcome(after=D(-1)), D(21 if kind == "debit" else -21), D(0), 1),
                ):
                    with self.subTest(model=model, kind=kind, stock=stock, request=request, after=outcome.after):
                        self.setUp()
                        self.actor.stocks[model] = stock
                        self.m.temp("cbrn_payload_native_model", model)
                        self.m.temp("cbrn_payload_native_requested", request)
                        for key in ("before", "after", "observed", "valid"):
                            self.m.temp(f"cbrn_payload_native_{key}", ZERO)
                        self.m.outcomes[kind].append(outcome)
                        self.call(f"cbrn_payload_measure_model_{kind}")
                        self.assertEqual(self.m.value("cbrn_payload_native_observed"), observed)
                        self.assertEqual(self.m.value("cbrn_payload_native_valid"), valid)
                        self.assertEqual(self.m.value("cbrn_payload_native_requested"), request)
                        self.assertEqual(len(self.m.nativecalls), count)
                        COVERAGE.update(self.m.calls)
        for model in ("unsupported_payload_model", ZERO):
            self.setUp()
            self.m.temp("cbrn_payload_native_model", model)
            self.m.temp("cbrn_payload_native_requested", D(10))
            self.m.temp("cbrn_payload_native_valid", D(999))
            self.m.temp("cbrn_payload_native_observed", D(999))
            self.call("cbrn_payload_measure_model_debit")
            self.assertEqual(self.m.value("cbrn_payload_native_valid"), 0)
            self.assertEqual(self.m.value("cbrn_payload_native_observed"), 0)
            self.assertEqual(self.m.nativecalls, [])

    def test_incremental_selected_receipt_counters(self):
        self.capture()
        for nonce in (2, 3):
            self.actor.stocks[self.model] = self.cost
            self.site.controller = self.actor
            self.actor.variables["cbrn_payload_request_nonce"] = D(nonce)
            handle = self.reserve()
            self.actor.variables["cbrn_payload_request_handle"] = D(handle)
            self.site.controller = self.foreign
            self.call("cbrn_transfer_payload_reservation", root=self.foreign)
            self.assert_result("accepted")
        self.assert_totals(self.cost * 3, captured=self.cost * 3, who=self.foreign)
        # An unselected long registry suffix must not enter or alter this delta.
        self.foreign.arrays["cbrn_payload_open_receipts"].extend(map(D, range(100, 1205)))
        self.foreign.variables["cbrn_payload_handle"] = D(2)
        for _ in range(2):
            self.call("cbrn_payload_refresh_reservation_counts", self.foreign)
            self.assert_totals(self.cost * 3, captured=self.cost * 3, who=self.foreign)
        self.foreign.variables["cbrn_payload_request_handle"] = D(2)
        self.foreign.variables["cbrn_payload_request_nonce"] = D(2)
        self.foreign.variables["cbrn_payload_loss_proof"] = self.c("cbrn_proof.supplied")
        self.call("cbrn_discard_payload_reservation", self.foreign)
        self.assert_result("accepted", self.foreign)
        self.assert_totals(self.cost * 2, captured=self.cost * 2, who=self.foreign)
        self.assertEqual(self.row("held", 1, self.foreign), self.cost)
        self.assertEqual(self.row("held", 3, self.foreign), self.cost)

    def test_copied_foreign_ledger_initialization(self):
        self.reserve()
        self.foreign.variables.update(self.actor.variables)
        self.foreign.arrays.update({key: list(values) for key, values in self.actor.arrays.items()})
        self.call("cbrn_payload_initialize_reservations", self.foreign)
        self.assertEqual(self.foreign.variables["cbrn_payload_ledger_owner_id"], self.foreign.identity)
        self.assertEqual(self.foreign.variables["cbrn_payload_receipt_sequence"], 0)
        self.assertEqual(self.foreign.arrays["cbrn_payload_open_receipts"], [])
        self.assertNotIn("cbrn_payload_consumer_handle_32", self.foreign.variables)
        self.assertNotIn("cbrn_payload_consumer_last_nonce_32", self.foreign.variables)
        self.assert_totals(0, who=self.foreign)
        self.assert_totals(self.cost, bound=1)
        self.call("cbrn_return_payload_reservation", self.foreign)
        self.assert_result("rejected", self.foreign)
        self.assertEqual(len(self.m.nativecalls), 1)

    def test_exact_site_selector_uses_real_settlement_helpers(self):
        for action in ("recover", "hold", "destroy", "capture", "integrate"):
            with self.subTest(action=action):
                self.setUp()
                if action == "integrate":
                    self.capture()
                    holder = self.foreign
                    holder.techs = {"chlorine_gas", "chemical_air_interdiction"}
                    holder.variables["cbrn_air_payload_agent"] = self.c("cbrn_agent.chlorine")
                else:
                    self.reserve()
                    holder = self.actor
                holder.variables["cbrn_payload_request_site"] = self.site
                holder.variables["cbrn_payload_site_action"] = self.c(f"cbrn_payload_site_action.{action}")
                if action == "capture":
                    self.site.controller = self.foreign
                    holder.variables["cbrn_payload_request_recipient"] = self.foreign
                # A distinct source receipt is not selected, even with matching
                # owner and an active registry row. No source constructor mocks.
                other_site = Scope("other_site", 999, "state", controller=holder)
                for key in tuple(holder.variables):
                    if key.startswith("cbrn_payload_receipt_") and key.endswith("_1"):
                        holder.variables[key[:-1] + "99"] = holder.variables[key]
                holder.variables["cbrn_payload_receipt_site_id_99"] = D(other_site.identity)
                holder.variables["cbrn_payload_receipt_site_99"] = other_site
                holder.variables["cbrn_payload_receipt_counted_phase_99"] = ZERO
                holder.variables["cbrn_payload_receipt_counted_quantity_99"] = ZERO
                holder.arrays["cbrn_payload_open_receipts"].append(D(99))
                holder.variables["cbrn_payload_handle"] = D(99)
                self.call("cbrn_payload_refresh_reservation_counts", holder)
                self.call("cbrn_settle_site_payload_reservations", holder, self.foreign)
                expected_result = "partial" if action == "hold" else "accepted"
                self.assertEqual(holder.variables["cbrn_payload_site_result"], self.c(f"cbrn_payload_receipt_result.{expected_result}"))
                self.assertEqual(holder.variables["cbrn_payload_site_settled_amount"], 0 if action == "hold" else self.cost)
                self.assertEqual(self.row("held", 99, holder), self.cost)
                self.assertIn(D(99), holder.arrays["cbrn_payload_open_receipts"])
                self.assertIsNone(self.m.temp_owner("cbrn_payload_site_handles", True))
                expected_calls = 2 if action in ("recover", "integrate") else 1
                self.assertEqual(len(self.m.nativecalls), expected_calls)
                if action == "hold":
                    self.assertEqual(self.row("phase"), self.c("cbrn_payload_receipt_phase.recovery_pending"))
                    self.assert_totals(self.cost * 2, bound=2, who=holder)
                elif action == "integrate":
                    self.assert_totals(self.cost, captured=self.cost, who=holder)
                else:
                    self.assert_totals(self.cost, bound=1, who=holder)
                if action == "capture":
                    self.assertEqual(self.foreign.stocks, {})
                    self.assertEqual(self.foreign.techs, set())
                COVERAGE.update(self.m.calls)

    def test_site_selector_ignores_inherited_default_and_private_breaks(self):
        for action in ("destroy", "integrate"):
            with self.subTest(action=action):
                self.setUp()
                self.capture()
                other_site = Scope("unrelated_site", 909, "state", controller=self.actor)
                for nonce, site in ((2, other_site), (3, self.site)):
                    site.controller = self.actor
                    self.actor.stocks[self.model] = self.cost
                    self.actor.variables["cbrn_payload_request_site"] = site
                    self.actor.variables["cbrn_payload_request_nonce"] = D(nonce)
                    self.reserve()
                    site.controller = self.foreign
                    self.call("cbrn_transfer_payload_reservation", root=self.foreign)
                    self.assert_result("accepted")
                self.assertEqual(self.foreign.arrays["cbrn_payload_open_receipts"], [D(1), D(2), D(3)])
                self.assert_totals(self.cost * 3, captured=self.cost * 3, who=self.foreign)
                unrelated = {key: value for key, value in self.foreign.variables.items()
                             if key.startswith("cbrn_payload_receipt_") and key.endswith("_2")}
                self.foreign.variables["cbrn_payload_request_site"] = self.site
                self.foreign.variables["cbrn_payload_site_action"] = self.c(f"cbrn_payload_site_action.{action}")
                if action == "integrate":
                    self.foreign.techs = {"chlorine_gas", "chemical_air_interdiction"}
                    self.foreign.variables["cbrn_air_payload_agent"] = self.c("cbrn_agent.chlorine")
                for key in ("break", "cbrn_payload_site_collect_break", "cbrn_payload_site_settle_break"):
                    self.m.temp(key, D(1))
                self.call("cbrn_settle_site_payload_reservations", self.foreign)
                self.assertEqual(self.m.value("break"), 1)
                self.assertEqual(self.m.value("cbrn_payload_site_collect_break"), 0)
                self.assertEqual(self.m.value("cbrn_payload_site_settle_break"), 0)
                self.assertEqual(self.foreign.variables["cbrn_payload_site_result"],
                                 self.c("cbrn_payload_receipt_result.accepted"))
                self.assertEqual(self.foreign.variables["cbrn_payload_site_settled_amount"], self.cost * 2)
                self.assertEqual(self.foreign.arrays["cbrn_payload_open_receipts"], [D(2)])
                for handle in (1, 3):
                    self.assertEqual(self.row("held", handle, self.foreign), 0)
                    column = "destroyed" if action == "destroy" else "returned"
                    self.assertEqual(self.row(column, handle, self.foreign), self.cost)
                self.assertEqual({key: self.foreign.variables[key] for key in unrelated}, unrelated)
                self.assert_totals(self.cost, captured=self.cost, who=self.foreign)
                self.assertEqual(len(self.m.nativecalls), 3 if action == "destroy" else 5)
                self.assertEqual(self.foreign.stocks.get(self.model, ZERO),
                                 0 if action == "destroy" else self.cost * 2)
                COVERAGE.update(self.m.calls)

    def test_loop_model_preserves_inherited_break_counterexample(self):
        self.m.frames[0].arrays["probe_values"] = [D(1), D(2)]
        self.m.temp("break", D(1))
        self.m.temp("iterations", ZERO)
        self.m.execute(parse("for_each_loop = { array = probe_values add_to_temp_variable = { iterations = 1 } }"))
        # Chosen bounded loop model checks break after the body. Native timing
        # is unobserved, but an inherited nonzero break must never be cleared.
        self.assertEqual(self.m.value("iterations"), 1)
        self.assertEqual(self.m.value("break"), 1)

    def test_capture_rejects_stored_pointer_different_from_frozen_state(self):
        for handle in (1, 2):
            with self.subTest(handle=handle):
                self.setUp()
                self.reserve()
                if handle == 2:
                    self.call("cbrn_return_payload_reservation")
                    self.actor.variables["cbrn_payload_request_nonce"] = D(2)
                    self.assertEqual(self.reserve(), 2)
                wrong_site = Scope("wrong_stored_state", 909, "state", controller=self.foreign)
                self.actor.variables[f"cbrn_payload_receipt_site_{handle}"] = wrong_site
                self.actor.variables["cbrn_payload_request_recipient"] = self.foreign
                self.actor.variables["cbrn_payload_transfer_proof"] = self.c("cbrn_proof.supplied")
                before_calls = list(self.m.nativecalls)
                before_held = self.row("held", handle)
                self.call("cbrn_transfer_payload_reservation", root=self.foreign)
                self.assert_result("rejected")
                self.assertEqual(self.row("held", handle), before_held)
                self.assertEqual(self.row("site_id", handle), self.site.identity)
                self.assertEqual(self.row("phase", handle), self.c("cbrn_payload_receipt_phase.held"))
                self.assertEqual(self.row("transferred", handle), 0)
                self.assertEqual(self.actor.variables["cbrn_payload_transferred_handle"], 0)
                self.assertEqual(self.foreign.variables, {})
                self.assertEqual(self.foreign.arrays, {})
                self.assertEqual(self.foreign.stocks, {})
                self.assertEqual(self.m.nativecalls, before_calls)
                self.assert_totals(self.cost, bound=1)
                COVERAGE.update(self.m.calls)

    def test_air_profile_guard_blocks_open_and_allows_closed_receipt(self):
        self.reserve()
        old_agent = self.actor.variables["cbrn_air_payload_agent"]
        self.actor.techs.add("phosgene")
        self.m.temp("cbrn_requested_payload_agent", self.c("cbrn_agent.phosgene"))
        self.m.temp("cbrn_payload_profile_change_accepted", ZERO)
        self.call("cbrn_change_air_payload_profile")
        self.assertEqual(self.m.value("cbrn_payload_profile_change_accepted"), 0)
        self.assertEqual(self.actor.variables["cbrn_air_payload_agent"], old_agent)
        self.assertEqual(self.row("agent"), old_agent)
        self.assertEqual(self.row("held"), self.cost)
        self.assertNotIn("cbrn_air_profile_change_in_progress", self.actor.flags)
        self.assertEqual(len(self.m.nativecalls), 1)
        self.call("cbrn_return_payload_reservation")
        self.assert_result("accepted")
        self.assert_totals(0)
        self.call("cbrn_change_air_payload_profile")
        self.assertEqual(self.m.value("cbrn_payload_profile_change_accepted"), self.c("cbrn_proof.supplied"))
        self.assertEqual(self.actor.variables["cbrn_air_payload_agent"], self.c("cbrn_agent.phosgene"))
        self.assertEqual(self.row("agent"), old_agent)
        self.assertEqual(self.row("returned"), self.cost)
        self.assertIn("cbrn_air_profile_change_in_progress", self.actor.flags)
        self.assertEqual(self.actor.timed_flags["cbrn_air_profile_change_in_progress"],
                         self.c("cbrn_payload_profile_timing.air_change_days"))
        loss = (self.cost * (D(1) - self.c("cbrn_payload_conversion.air_profile_switch_recovery"))).quantize(
            D(1), rounding=ROUND_HALF_UP)
        self.assertEqual(self.actor.stocks[self.model], self.cost - loss)
        self.assertEqual(len(self.m.nativecalls), 3)
        self.assertEqual(self.m.nativecalls[-1], ("actor", self.model, -loss, self.model, -loss))

    def test_legacy_air_default_setter_respects_open_receipt_guard(self):
        self.reserve()
        self.actor.variables["cbrn_air_payload_agent"] = self.c("cbrn_agent.none")
        self.actor.variables["cbrn_shell_filling_agent"] = self.c("cbrn_agent.phosgene")
        self.call("cbrn_migrate_legacy_payload_stockpiles")
        self.assertEqual(self.actor.variables["cbrn_air_payload_agent"], self.c("cbrn_agent.none"))
        self.assertEqual(self.row("agent"), self.c("cbrn_agent.chlorine"))
        self.assertEqual(self.row("held"), self.cost)
        self.assertEqual(len(self.m.nativecalls), 1)
        self.actor.variables["cbrn_payload_loss_proof"] = self.c("cbrn_proof.supplied")
        self.call("cbrn_discard_payload_reservation")
        self.assert_result("accepted")
        self.actor.flags.discard("cbrn_legacy_payload_stockpiles_migrated")
        self.call("cbrn_migrate_legacy_payload_stockpiles")
        self.assertEqual(self.actor.variables["cbrn_air_payload_agent"], self.c("cbrn_agent.phosgene"))
        self.assertEqual(self.row("agent"), self.c("cbrn_agent.chlorine"))
        self.assertEqual(self.row("destroyed"), self.cost)
        self.assertEqual(len(self.m.nativecalls), 1)

    def test_closed_stale_and_recovery_receipts(self):
        self.reserve()
        self.actor.variables["cbrn_payload_recovery_proof"] = ZERO
        self.call("cbrn_return_payload_reservation")
        self.assert_result("rejected")
        self.assertEqual(self.row("phase"), self.c("cbrn_payload_receipt_phase.recovery_pending"))
        self.assert_totals(self.cost, bound=1)
        self.actor.variables["cbrn_payload_recovery_proof"] = self.c("cbrn_proof.supplied")
        self.call("cbrn_return_payload_reservation")
        self.actor.variables["cbrn_payload_request_nonce"] = D(2)
        self.reserve()
        self.assertEqual(self.actor.variables["cbrn_payload_request_handle"], 2)
        self.actor.variables["cbrn_payload_request_handle"] = D(1)
        self.call("cbrn_return_payload_reservation")
        self.assert_result("rejected")
        self.assertEqual(self.row("held", 2), self.cost)
        self.assert_totals(self.cost, bound=1)
        self.actor.variables["cbrn_payload_request_nonce"] = D(1)
        self.call("cbrn_return_payload_reservation")
        self.assert_result("already_settled")
        self.assertEqual(self.actor.variables["cbrn_payload_consumer_handle_32"], 2)
        self.assertEqual(self.row("held", 2), self.cost)
        self.actor.variables["cbrn_payload_request_nonce"] = D(2)
        self.actor.variables["cbrn_payload_request_handle"] = D(2)
        self.actor.variables["cbrn_payload_loss_proof"] = self.c("cbrn_proof.supplied")
        self.call("cbrn_discard_payload_reservation")
        self.assert_result("accepted")
        self.call("cbrn_discard_payload_reservation")
        self.assert_result("already_settled")
        self.assertEqual(self.row("destroyed", 2), self.cost)
        self.assert_totals(0)

    def test_primitives_all_models_and_conservative_output_frames(self):
        for model in MODELS:
            for kind in ("debit", "credit"):
                with self.subTest(model=model, kind=kind):
                    self.setUp()
                    self.actor.stocks[model] = D(20)
                    self.m.temp("cbrn_payload_native_model", model)
                    self.m.temp("cbrn_payload_native_requested", D(30))
                    for key in ("before", "after", "observed", "valid"):
                        self.m.temp(f"cbrn_payload_native_{key}", ZERO)
                    self.call(f"cbrn_payload_measure_model_{kind}")
                    expected = D(20 if kind == "debit" else 30)
                    self.assertEqual(self.m.value("cbrn_payload_native_observed"), expected)
                    self.assertEqual(self.m.value("cbrn_payload_native_valid"), 1)
                    self.assertEqual(self.m.value("cbrn_payload_native_requested"), 30)
                    self.assertIsNone(self.m.temp_owner("cbrn_mask_native_observed"))
                    self.assertEqual(len(self.m.nativecalls), 1)
                    self.assertEqual(self.m.nativecalls[0][1], model)
                    self.assertEqual(self.m.nativecalls[0][2], -D(20) if kind == "debit" else D(30))
                    COVERAGE.update(self.m.calls)
        self.setUp()
        self.m.temp("cbrn_payload_native_model", self.model)
        self.m.temp("cbrn_payload_native_requested", D(5))
        self.call("cbrn_payload_measure_model_debit")
        self.assertIsNone(self.m.temp_owner("cbrn_payload_native_observed"))
        self.assertEqual(len(self.m.nativecalls), 1)

    def test_resolver_all_agents_routes_and_mismatched_class(self):
        for agent, (kind, _, _) in AGENTS.items():
            for route in ("chemical_air_raid", "strategic_chemical_raid"):
                with self.subTest(agent=agent, route=route):
                    self.m.temp("cbrn_action_agent", self.c(f"cbrn_agent.{agent}"))
                    self.m.temp("cbrn_action_delivery_route", self.c(f"cbrn_delivery_route.{route}"))
                    self.m.temp("cbrn_action_agent_class", D(999))
                    self.m.temp("cbrn_payload_native_model", ZERO)
                    self.m.temp("cbrn_payload_native_model_matched", ZERO)
                    self.call("cbrn_payload_resolve_air_model")
                    self.assertEqual(self.m.value("cbrn_payload_native_model"), f"{kind}_chemical_air_payload_lot_1")
                    self.assertEqual(self.m.value("cbrn_action_agent_class"), self.c(f"cbrn_agent_class.{kind}"))
                    self.assertEqual(self.m.value("cbrn_payload_native_model_matched"), 1)
        for agent, route in ((ZERO, self.c("cbrn_delivery_route.strategic_chemical_raid")),
                             (self.c("cbrn_agent.chlorine"), ZERO)):
            self.m.temp("cbrn_action_agent", agent)
            self.m.temp("cbrn_action_delivery_route", route)
            self.call("cbrn_payload_resolve_air_model")
            self.assertEqual(self.m.value("cbrn_payload_native_model_matched"), 0)
            self.assertEqual(self.m.value("cbrn_payload_native_model"), 0)

    def test_interpreter_operators_scopes_frames_and_fail_loudly(self):
        self.assertEqual([n.op for n in parse("x > 1 x < 3 x = 2")], [">", "<", "="])
        self.actor.variables["same"] = D(5)
        self.foreign.variables["same"] = D(9)
        self.m.temp("same", D(7))
        self.m.targets["foreign"] = self.foreign
        self.m.execute(parse("event_target:foreign = { set_variable = { result = ROOT.same } set_temp_variable = { same = 8 } }"))
        self.assertEqual(self.foreign.variables["result"], 5)
        self.assertEqual(self.m.value("same"), 8)
        self.assertEqual(self.actor.variables["same"], 5)
        self.m.execute(parse("add_to_variable = { same = 1 }"))
        self.assertEqual(self.actor.variables["same"], 6)
        self.assertEqual(self.m.value("same"), 8)
        self.assertTrue(self.m.condition(parse("check_variable = { same > 7 }")))
        self.assertFalse(self.m.condition(parse("check_variable = { same < 7 }")))
        self.m.execute(parse("clear_temp_array = kept"))
        helper = "fixture_frame_probe"
        self.s.effects[helper] = (parse("set_temp_variable = { transient = 1 } add_to_temp_array = { array = kept value = 2 } clear_temp_array = transient_array meta_effect = { text = { set_temp_variable = { same = 10 } set_temp_variable = { meta_only = 1 } } }"), {}, "test-only-frame-probe", 1)
        try:
            self.m.call(helper)
        finally:
            del self.s.effects[helper]
        self.assertEqual(self.m.value("same"), 10)
        self.assertEqual(self.m.frames[0].arrays["kept"], [D(2)])
        self.assertIsNone(self.m.temp_owner("transient"))
        self.assertIsNone(self.m.temp_owner("meta_only"))
        self.assertIsNone(self.m.temp_owner("transient_array", True))
        with self.assertRaisesRegex(AssertionError, "Unmodeled command"):
            self.m.execute(parse("unexpected_gameplay_effect = yes"))


if __name__ == "__main__":
    SOURCE = Source()  # Fresh production bytes on every invocation, no fixtures masking draft changes.
    print("Production source SHA-256 (source evidence only):", flush=True)
    for path, digest in SOURCE.hashes.items():
        print(f"  {path} {digest}", flush=True)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ChemicalReceipts)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    executed = [name for name in COVERAGE if name in SOURCE.effects or name in SOURCE.triggers]
    print(f"Executed {len(executed)} production helper definitions across explicit scenarios.")
    print("Executed helper families: " + ", ".join(
        f"{label}={sum(name.startswith(prefix) for name in executed)}"
        for label, prefix in (("CBRN", "cbrn_"), ("Event32", "missiles_"), ("Sanctions", "condemnation_"))))
    changed = [path for path, digest in SOURCE.hashes.items()
               if sha256((ROOT_DIR / path).read_bytes()).hexdigest() != digest]
    if changed:
        print(f"SOURCE CHANGED DURING RUN: {changed}. Rerun against fresh bytes.")
    print("Native/world leaves are injected. Engine stock, variants, callback custody and runtime lifetime remain unproven.")
    raise SystemExit(0 if result.wasSuccessful() and not changed else 1)
