"""Execute the bounded Event 35 center-project contract from production source.

This is a source-limited executor for the named Event 35 effect and trigger
closure. It does not emulate engine callbacks, saves, AI selection, or live
timed-flag expiry. Native primitives update fixture state and record calls.
Unknown script commands fail loudly.
"""
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import operator
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
EFFECT_FILES = (
    r"common\scripted_effects\035_great_depression_effects.txt",
    r"common\scripted_effects\035_great_depression_decision_effects.txt",
    r"common\scripted_effects\035_great_depression_region_effects.txt",
    r"common\scripted_effects\035_great_depression_inherited_liability_effects.txt",
)
TRIGGER_FILES = (
    r"common\scripted_triggers\035_great_depression_triggers.txt",
    r"common\scripted_triggers\035_great_depression_decision_triggers.txt",
    r"common\scripted_triggers\035_great_depression_decision_surface_triggers.txt",
)
CONSTANTS_FILE = r"common\script_constants\035_great_depression_constants.txt"
REGION_CONSTANTS_FILE = r"common\script_constants\035_great_depression_region_constants.txt"
TOKEN = re.compile(r'"(?:[^"\\]|\\.)*"|[{}=<>]|[^\s{}=<>]+')
HEADER = re.compile(r"(?m)^([A-Za-z_][A-Za-z0-9_]*)[ \t]*=[ \t]*\{")
NUMBER = re.compile(r"^-?\d+(?:\.\d+)?$")


class SourceContractError(AssertionError):
    pass


@dataclass(frozen=True)
class Token:
    text: str
    line: int
    offset: int


@dataclass(frozen=True)
class Node:
    key: str
    op: str
    value: object
    line: int


@dataclass(frozen=True)
class Definition:
    name: str
    path: Path
    line: int
    body: list


def uncomment(source):
    return re.sub(r"(?m)#[^\n]*", lambda m: " " * len(m.group(0)), source)


def lex(source):
    result = []
    line = 1
    offset = 0
    for match in TOKEN.finditer(source):
        line += source.count("\n", offset, match.start())
        result.append(Token(match.group(0), line, match.start()))
        offset = match.end()
    return result


def parse_nodes(tokens, cursor, definition):
    result = []
    while cursor < len(tokens) and tokens[cursor].text != "}":
        key = tokens[cursor]
        if cursor + 2 >= len(tokens):
            raise SourceContractError(f"{definition}: incomplete assignment at line {key.line}")
        op = tokens[cursor + 1]
        raw = tokens[cursor + 2]
        if op.text not in ("=", "<", ">"):
            raise SourceContractError(
                f"{definition}: unsupported operator {op.text!r} at line {op.line}"
            )
        cursor += 3
        if raw.text == "{":
            value, cursor = parse_nodes(tokens, cursor, definition)
            if cursor >= len(tokens) or tokens[cursor].text != "}":
                raise SourceContractError(f"{definition}: unclosed block opened at line {raw.line}")
            cursor += 1
        else:
            value = raw.text
        result.append(Node(key.text, op.text, value, key.line))
    return result, cursor


def read_definitions(relative_path):
    path = ROOT / relative_path
    raw = path.read_text(encoding="utf-8-sig")
    source = uncomment(raw)
    tokens = lex(source)
    depth = 0
    for token in tokens:
        if token.text == "{":
            depth += 1
        elif token.text == "}":
            depth -= 1
            if depth < 0:
                raise SourceContractError(f"{path}: unmatched closing brace at line {token.line}")
    if depth:
        raise SourceContractError(f"{path}: {depth} unclosed source block(s)")

    token_at = {token.offset: index for index, token in enumerate(tokens)}
    definitions = {}
    for match in HEADER.finditer(source):
        name = match.group(1)
        opening = token_at.get(match.end() - 1)
        if opening is None or tokens[opening].text != "{":
            raise SourceContractError(f"{path}: could not locate block for {name}")
        body, cursor = parse_nodes(tokens, opening + 1, f"{path.name}:{name}")
        if cursor >= len(tokens) or tokens[cursor].text != "}":
            raise SourceContractError(f"{path}: unclosed helper {name} at line {tokens[opening].line}")
        if name in definitions:
            previous = definitions[name]
            raise SourceContractError(
                f"duplicate definition {name}: {previous.path} and {path}:{tokens[opening].line}"
            )
        definitions[name] = Definition(name, path, tokens[opening].line, body)
    return definitions


def first(nodes, key, default=None):
    return next((node.value for node in nodes if node.key == key), default)


@dataclass
class Scope:
    kind: str
    id: object
    values: dict = field(default_factory=dict)
    arrays: dict = field(default_factory=dict)
    flags: set = field(default_factory=set)
    resources: dict = field(default_factory=dict)
    modifiers: set = field(default_factory=set)
    ideas: set = field(default_factory=set)
    exists: bool = True
    owner: object = None
    controller: object = None
    population_k: float = 0
    buildings: dict = field(default_factory=dict)
    normal_civilian_systems: bool = True
    ai: bool = False


class Event35Runtime:
    """Only the source commands reached by the center-project call paths run."""

    EXTERNAL_FIXTURES = {"great_depression_submit_humanitarian_center_pressure"}
    NATIVE_PRIMITIVES = {
        "add_building_construction", "remove_building", "add_dynamic_modifier",
        "remove_dynamic_modifier", "add_ideas", "remove_ideas", "country_event",
        "news_event", "add_equipment_to_stockpile", "add_political_power",
        "add_manpower", "add_fuel", "add_stability", "add_war_support",
    }

    def __init__(self):
        self.effect_defs = {}
        self.trigger_defs = {}
        for path in EFFECT_FILES:
            self.effect_defs.update(read_definitions(path))
        for path in TRIGGER_FILES:
            self.trigger_defs.update(read_definitions(path))
        self.constants = self._read_constants()
        self.file_constants = {}
        for path in EFFECT_FILES:
            raw = uncomment((ROOT / path).read_text(encoding="utf-8-sig"))
            self.file_constants.update({
                name: float(value) for name, value in re.findall(
                    r"(?m)^@([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(-?\d+(?:\.\d+)?)\s*$", raw
                )
            })
        self.globals = {"num_days": 300}
        self.global_arrays = {}
        self.global_flags = set()
        self.targets = {}
        self.scope_stack = []
        self.root = None
        self.temp_frames = [{}]
        self.call_stack = []
        self.timed_flags = {}
        self.timed_flag_writes = []
        self.resource_writes = []
        self.native_calls = []
        self.external_calls = []
        self.events = []

    def _read_constants(self):
        result = {}
        for constant_file in (CONSTANTS_FILE, REGION_CONSTANTS_FILE):
            for group, definition in read_definitions(constant_file).items():
                for node in definition.body:
                    if isinstance(node.value, str) and NUMBER.fullmatch(node.value):
                        result[f"constant:{group}.{node.key}"] = float(node.value)
        return result

    @property
    def current(self):
        if not self.scope_stack:
            raise SourceContractError("no current scope")
        return self.scope_stack[-1]

    def _scope_for_prefix(self, prefix):
        if prefix == "ROOT":
            return self.root
        if prefix == "THIS":
            return self.current
        if prefix == "PREV":
            if len(self.scope_stack) < 2:
                raise SourceContractError("PREV read without a caller scope")
            return self.scope_stack[-2]
        raise SourceContractError(f"unsupported scope prefix {prefix}")

    @staticmethod
    def _same(left, right):
        if isinstance(left, Scope) or isinstance(right, Scope):
            return isinstance(left, Scope) and isinstance(right, Scope) and left.kind == right.kind and left.id == right.id
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return float(left) == float(right)
        return left == right

    def _array_value(self, container, path):
        base, _, index = path.partition("^")
        values = container.arrays.get(base, [])
        if index == "num":
            return len(values)
        if index:
            index = int(self._value(index))
            return values[index] if 0 <= index < len(values) else 0
        return values

    def _path_container(self, path):
        if path.startswith("global."):
            return None, path[7:], True
        for prefix in ("ROOT.", "PREV.", "THIS."):
            if path.startswith(prefix):
                return self._scope_for_prefix(prefix[:-1]), path[len(prefix):], False
        return self.current, path, False

    def _array_values(self, path):
        if not isinstance(path, str):
            raise SourceContractError(f"array selector must remain a source path, got {type(path).__name__}")
        container, rest, global_scope = self._path_container(path)
        arrays = self.global_arrays if global_scope else container.arrays
        return arrays.get(rest, [])

    def _path_exists(self, path):
        if path.startswith("constant:"):
            return path in self.constants
        if path.startswith("global."):
            rest = path[7:]
            if "^" in rest:
                base, _, index = rest.partition("^")
                return index == "num" and base in self.global_arrays or index.isdigit() and int(index) < len(self.global_arrays.get(base, []))
            return rest in self.globals
        if path.startswith("@"):
            return path[1:] in self.file_constants
        container, rest, global_scope = self._path_container(path)
        if "^" in rest:
            base, _, index = rest.partition("^")
            arrays = self.global_arrays if global_scope else container.arrays
            return index == "num" and base in arrays or index.isdigit() and int(index) < len(arrays.get(base, []))
        return rest in container.values

    def _value(self, token):
        if isinstance(token, Scope) or isinstance(token, (float, int, bool)):
            return token
        if not isinstance(token, str):
            return token
        if len(token) >= 2 and token[0] == token[-1] == '"':
            return token[1:-1].replace(r'\"', '"')
        if token == "ROOT":
            return self.root
        if token == "THIS":
            return self.current
        if token == "PREV":
            return self._scope_for_prefix("PREV")
        if token.startswith("event_target:"):
            name, _, member = token.split(":", 1)[1].partition(".")
            if name not in self.targets:
                raise SourceContractError(f"unresolved event target {name}")
            target = self.targets[name]
            return target.values.get(member, 0) if member else target
        if token.startswith("constant:"):
            if token not in self.constants:
                raise SourceContractError(f"unresolved script constant {token}")
            return self.constants[token]
        if token.startswith("@"):
            if token[1:] not in self.file_constants:
                raise SourceContractError(f"unresolved file constant {token}")
            return self.file_constants[token[1:]]
        if token.startswith("var:"):
            return self._value(token[4:])
        if token == "THIS.id":
            return self.current.id
        if token == "ROOT.id":
            return self.root.id
        if token == "PREV.id":
            return self._scope_for_prefix("PREV").id
        if token.startswith("global.") or token.startswith(("ROOT.", "PREV.", "THIS.")) or "^" in token:
            container, rest, global_scope = self._path_container(token)
            if "^" in rest:
                return self._array_value(container if not global_scope else None, rest)
            if global_scope:
                return self.globals.get(rest, 0)
            return container.values.get(rest, 0)
        if token in ("yes", "no"):
            return token == "yes"
        if NUMBER.fullmatch(token):
            value = float(token)
            return int(value) if value.is_integer() else value
        for frame in reversed(self.temp_frames):
            if token in frame:
                return frame[token]
        if token in self.current.values:
            return self.current.values[token]
        if token in self.current.arrays:
            return self.current.arrays[token]
        return token

    def _write_path(self, path, value, clear=False):
        container, rest, global_scope = self._path_container(path)
        values = self.globals if global_scope else container.values
        arrays = self.global_arrays if global_scope else container.arrays
        if "^" in rest:
            base, _, raw_index = rest.partition("^")
            index = int(self._value(raw_index))
            row = arrays.setdefault(base, [])
            while len(row) <= index:
                row.append(0)
            if clear:
                row[index] = 0
            else:
                row[index] = value
        elif clear:
            values.pop(rest, None)
        else:
            values[rest] = value

    def _variable(self, token):
        if token.startswith("constant:"):
            return self._value(token)
        if token.startswith("global.") or token.startswith(("ROOT.", "PREV.", "THIS.")) or "^" in token:
            return self._value(token)
        for frame in reversed(self.temp_frames):
            if token in frame:
                return frame[token]
        return self.current.values.get(token, 0)

    def _set_temp(self, name, value):
        for frame in reversed(self.temp_frames[:-1]):
            if name in frame:
                frame[name] = value
                return
        self.temp_frames[-1][name] = value

    def _numeric_builtin(self, key, scope):
        if key == "state_population_k" and scope.kind == "state":
            return scope.population_k
        if key in ("industrial_complex", "arms_factory", "dockyard") and scope.kind == "state":
            return scope.buildings.get(key, 0)
        if key == "num_of_civilian_factories_available_for_projects" and scope.kind == "country":
            return scope.resources.get("civilian_factories_available", 0)
        if key == "has_political_power" and scope.kind == "country":
            return scope.resources.get("political_power", 0)
        if key == "has_manpower" and scope.kind == "country":
            return scope.resources.get("manpower", 0)
        if key == "has_fuel" and scope.kind == "country":
            return scope.resources.get("fuel", 0)
        if key == "has_stability" and scope.kind == "country":
            return scope.resources.get("stability", 0)
        if key == "has_war_support" and scope.kind == "country":
            return scope.resources.get("war_support", 0)
        if key in scope.resources:
            return scope.resources[key]
        raise SourceContractError(f"unsupported numeric trigger {key} in {scope.kind} scope")

    def _compare(self, left, op, right):
        operations = {"=": operator.eq, "<": operator.lt, ">": operator.gt}
        if op not in operations:
            raise SourceContractError(f"unsupported comparison operator {op}")
        return operations[op](left, right)

    def test_trigger(self, name, scope, root=None):
        previous_root = self.root
        previous_stack = self.scope_stack
        self.root = root if root is not None else (scope if scope.kind == "country" else scope.owner)
        self.scope_stack = [scope]
        try:
            return self._run_trigger(name, scope)
        finally:
            self.scope_stack = previous_stack
            self.root = previous_root

    def _run_trigger(self, name, scope):
        if name not in self.trigger_defs:
            raise SourceContractError(f"unsupported scripted trigger {name}; ancestry={self.call_stack}")
        definition = self.trigger_defs[name]
        self.call_stack.append(f"{definition.path.name}:{name}:{definition.line}")
        try:
            return self._conditions(definition.body, scope)
        except SourceContractError as exc:
            raise SourceContractError(f"{exc}; ancestry={' -> '.join(self.call_stack)}") from exc
        finally:
            self.call_stack.pop()

    def _conditions(self, nodes, scope):
        return all(self._condition(node, scope) for node in nodes)

    def _condition(self, node, scope):
        key, op, value = node.key, node.op, node.value
        if op != "=":
            if key in ("has_equipment", "has_fuel", "has_manpower", "has_political_power", "has_stability", "has_war_support") or key == "num_of_civilian_factories_available_for_projects":
                return self._compare(self._numeric_builtin(key, scope), op, self._value(value))
            return self._compare(self._numeric_builtin(key, scope), op, self._value(value))
        if key == "NOT":
            # Native NOT is NOR: any true child makes the block false.
            return not any(self._condition(child, scope) for child in value)
        if key == "OR":
            return any(self._conditions([child], scope) for child in value)
        if key == "AND":
            return self._conditions(value, scope)
        if key in ("hidden_trigger", "custom_trigger_tooltip"):
            predicate = first(value, "trigger", None)
            if predicate is None:
                predicate = [child for child in value if child.key != "tooltip"]
            return self._conditions(predicate, scope)
        if key == "check_variable":
            if len(value) == 1 and value[0].op in ("<", ">"):
                clause = value[0]
                return self._compare(self._variable(clause.key), clause.op, self._value(clause.value))
            args = {item.key: item.value for item in value}
            compares = {
                "equals": operator.eq, "less_than": operator.lt, "greater_than": operator.gt,
                "less_than_or_equals": operator.le, "greater_than_or_equals": operator.ge,
            }
            compare = self._value(args["compare"])
            if compare not in compares:
                raise SourceContractError(f"unsupported check_variable compare={compare}")
            return compares[compare](self._variable(args["var"]), self._value(args["value"]))
        if key == "has_variable":
            return self._path_exists(value)
        if key == "has_state_flag":
            if scope.kind != "state":
                raise SourceContractError(f"has_state_flag in {scope.kind} scope")
            return value in scope.flags
        if key == "has_country_flag":
            if scope.kind != "country":
                raise SourceContractError(f"has_country_flag in {scope.kind} scope")
            return value in scope.flags
        if key == "has_global_flag":
            return value in self.global_flags
        if key == "has_idea":
            return scope.kind == "country" and value in scope.ideas
        if key == "exists":
            if scope.kind != "country":
                raise SourceContractError(f"country-only exists trigger in {scope.kind} scope at line {node.line}")
            return scope.exists == (value == "yes")
        if key in ("ROOT", "PREV", "THIS") or key.startswith("event_target:") or key.startswith("var:"):
            target = self._value(key)
            if not isinstance(target, Scope):
                raise SourceContractError(f"scope selector {key} did not resolve to an object")
            self.scope_stack.append(target)
            try:
                return self._conditions(value, target)
            finally:
                self.scope_stack.pop()
        if key == "is_owned_by":
            return scope.kind == "state" and self._same(scope.owner, self._value(value))
        if key == "is_controlled_by":
            return scope.kind == "state" and self._same(scope.controller, self._value(value))
        if key == "state":
            return scope.kind == "state" and self._same(scope, self._value(value))
        if key == "is_in_array":
            args = {item.key: item.value for item in value}
            array = self._array_values(args["array"])
            item = self._value(args["value"])
            return any(self._same(candidate, item) for candidate in array)
        if key == "has_equipment":
            return self._conditions(value, scope)
        if key == "uses_normal_civilian_systems":
            return scope.kind == "country" and scope.normal_civilian_systems == (value == "yes")
        if key in ("is_special_chaos_country", "is_actual_nonhuman_country"):
            return scope.values.get(key, False) == (value == "yes")
        if key == "is_ai":
            return scope.kind == "country" and scope.ai == (value == "yes")
        if key == "has_active_mission":
            return value in scope.values.get("active_missions", set())
        if key in self.trigger_defs and value == "yes":
            return self._run_trigger(key, scope)
        if key in ("has_fuel", "has_manpower", "has_political_power", "has_stability", "has_war_support", "state_population_k", "industrial_complex", "arms_factory", "dockyard", "num_of_civilian_factories_available_for_projects"):
            return self._compare(self._numeric_builtin(key, scope), "=", self._value(value))
        if key == "owner_exists":
            return scope.kind == "state" and scope.owner is not None and scope.owner.exists == (value == "yes")
        raise SourceContractError(f"unsupported trigger command {key} at line {node.line}")

    def run_effect(self, name, scope, root=None):
        previous_root = self.root
        previous_stack = self.scope_stack
        self.root = root if root is not None else (scope if scope.kind == "country" else scope.owner)
        self.scope_stack = [scope]
        try:
            self._call_effect(name, scope)
        finally:
            self.scope_stack = previous_stack
            self.root = previous_root

    def _call_effect(self, name, scope):
        if name not in self.effect_defs:
            if name in self.EXTERNAL_FIXTURES:
                self.external_calls.append((name, scope.id, self.root.id if self.root else None))
                return
            raise SourceContractError(f"unsupported scripted effect {name}; ancestry={' -> '.join(self.call_stack)}")
        definition = self.effect_defs[name]
        self.call_stack.append(f"{definition.path.name}:{name}:{definition.line}")
        self.temp_frames.append({})
        try:
            self._effects(definition.body, scope)
        except SourceContractError as exc:
            raise SourceContractError(f"{exc}; ancestry={' -> '.join(self.call_stack)}") from exc
        finally:
            self.temp_frames.pop()
            self.call_stack.pop()

    def _effects(self, nodes, scope):
        branch_taken = False
        previous_was_branch = False
        for node in nodes:
            key, value = node.key, node.value
            if key in ("if", "else_if", "else"):
                if key == "if":
                    branch_taken = False
                limit = first(value, "limit", [])
                matched = (key == "if" or not branch_taken) and self._conditions(limit, scope)
                if matched:
                    self._effects([child for child in value if child.key != "limit"], scope)
                    branch_taken = True
                previous_was_branch = True
                continue
            if previous_was_branch:
                branch_taken = False
                previous_was_branch = False
            if key in ("ROOT", "PREV", "THIS") or key.startswith("event_target:") or key.startswith("var:"):
                target = self._value(key)
                if not isinstance(target, Scope):
                    raise SourceContractError(f"scope selector {key} did not resolve to an object")
                self.scope_stack.append(target)
                try:
                    self._effects(value, target)
                finally:
                    self.scope_stack.pop()
            elif key == "set_variable":
                name, rhs = value[0].key, value[0].value
                self._write_path(name, self._value(rhs))
            elif key in ("add_to_variable", "subtract_from_variable", "multiply_variable"):
                name, rhs = value[0].key, self._value(value[0].value)
                current = self._variable(name)
                if key == "add_to_variable": result = current + rhs
                elif key == "subtract_from_variable": result = current - rhs
                else: result = current * rhs
                self._write_path(name, result)
            elif key == "clear_variable":
                self._write_path(value, 0, clear=True)
            elif key == "set_temp_variable":
                self._set_temp(value[0].key, self._value(value[0].value))
            elif key in ("add_to_temp_variable", "subtract_from_temp_variable", "multiply_temp_variable"):
                name, rhs = value[0].key, self._value(value[0].value)
                current = self._variable(name)
                result = current + rhs if key == "add_to_temp_variable" else current - rhs if key == "subtract_from_temp_variable" else current * rhs
                self._set_temp(name, result)
            elif key == "clear_temp_variable":
                for frame in reversed(self.temp_frames):
                    if value in frame:
                        del frame[value]
                        break
            elif key in ("round_variable", "round_temp_variable"):
                current = self._variable(value)
                rounded = int(Decimal(str(current)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
                if key == "round_variable":
                    self._write_path(value, rounded)
                else:
                    self._set_temp(value, rounded)
            elif key == "set_state_flag":
                self._require_scope(scope, "state", key, node.line)
                scope.flags.add(value)
            elif key == "clr_state_flag":
                self._require_scope(scope, "state", key, node.line)
                scope.flags.discard(value)
            elif key in ("set_country_flag", "clr_country_flag"):
                if isinstance(value, list):
                    args = {child.key: child.value for child in value}
                    flag = self._value(args["flag"])
                    duration = self._value(args["days"]) if "days" in args else None
                else:
                    flag, duration = value, None
                self._require_scope(scope, "country", key, node.line)
                if key == "set_country_flag":
                    scope.flags.add(flag)
                    if duration is not None:
                        self.timed_flags[(scope.id, flag)] = self.globals["num_days"] + duration
                        self.timed_flag_writes.append((scope.id, flag, duration))
                else:
                    scope.flags.discard(flag)
                    self.timed_flags.pop((scope.id, flag), None)
            elif key in ("set_global_flag", "clr_global_flag"):
                (self.global_flags.add if key == "set_global_flag" else self.global_flags.discard)(value)
            elif key == "clear_variable":
                self._write_path(value, 0, clear=True)
            elif key == "clear_array":
                container, rest, global_scope = self._path_container(value)
                arrays = self.global_arrays if global_scope else container.arrays
                arrays[rest] = []
            elif key == "add_to_array":
                args = {child.key: child.value for child in value}
                array_name = args["array"]
                item = self._value(args["value"])
                container, rest, global_scope = self._path_container(array_name)
                arrays = self.global_arrays if global_scope else container.arrays
                arrays.setdefault(rest, []).append(item)
            elif key == "remove_from_array":
                args = {child.key: child.value for child in value}
                array_name = args["array"]
                index = int(self._value(args["index"]))
                container, rest, global_scope = self._path_container(array_name)
                arrays = self.global_arrays if global_scope else container.arrays
                if 0 <= index < len(arrays.get(rest, [])):
                    arrays[rest].pop(index)
            elif key == "save_event_target_as":
                self.targets[value] = scope
            elif key in ("clear_event_target", "clear_global_event_target"):
                self.targets.pop(value, None)
            elif key == "for_loop_effect":
                args = {child.key: child.value for child in value if child.key in ("start", "end", "value")}
                start, end, var = int(self._value(args["start"])), int(self._value(args["end"])), args["value"]
                body = [child for child in value if child.key not in ("start", "end", "value")]
                for index in range(start, end):
                    self._set_temp(var, index)
                    self._effects(body, scope)
            elif key == "hidden_effect":
                # Tooltip suppression only; the effects still run.
                self._effects(value, scope)
            elif key == "custom_effect_tooltip":
                pass
            elif key == "for_each_scope_loop":
                array_name = first(value, "array")
                container, rest, global_scope = self._path_container(array_name)
                arrays = self.global_arrays if global_scope else container.arrays
                body = [child for child in value if child.key not in ("array", "break", "tooltip")]
                for target in list(arrays.get(rest, [])):
                    self.scope_stack.append(target)
                    try:
                        self._effects(body, target)
                    finally:
                        self.scope_stack.pop()
            elif key in self.NATIVE_PRIMITIVES:
                self._native_effect(key, value, scope, node.line)
            elif key in self.effect_defs or key in self.EXTERNAL_FIXTURES:
                self._call_effect(key, scope)
            else:
                raise SourceContractError(f"unsupported effect command {key} at line {node.line}")

    @staticmethod
    def _require_scope(scope, kind, command, line):
        if scope.kind != kind:
            raise SourceContractError(f"{command} requires {kind} scope, got {scope.kind} at line {line}")

    def _native_effect(self, key, value, scope, line):
        self.native_calls.append((key, scope.id))
        if key in ("add_political_power", "add_manpower", "add_fuel", "add_stability", "add_war_support"):
            self._require_scope(scope, "country", key, line)
            resource = {
                "add_political_power": "political_power", "add_manpower": "manpower",
                "add_fuel": "fuel", "add_stability": "stability", "add_war_support": "war_support",
            }[key]
            amount = self._value(value)
            scope.resources[resource] = scope.resources.get(resource, 0) + amount
            self.resource_writes.append((scope.id, resource, amount))
        elif key == "add_equipment_to_stockpile":
            self._require_scope(scope, "country", key, line)
            args = {child.key: child.value for child in value}
            resource = self._value(args["type"])
            amount = self._value(args["amount"])
            scope.resources[resource] = scope.resources.get(resource, 0) + amount
            self.resource_writes.append((scope.id, resource, amount))
        elif key in ("add_dynamic_modifier", "remove_dynamic_modifier"):
            args = {child.key: child.value for child in value}
            modifier = self._value(args["modifier"])
            (scope.modifiers.add if key == "add_dynamic_modifier" else scope.modifiers.discard)(modifier)
        elif key in ("add_ideas", "remove_ideas"):
            (scope.ideas.add if key == "add_ideas" else scope.ideas.discard)(self._value(value))
        elif key == "country_event":
            args = {child.key: child.value for child in value}
            self.events.append((scope.id, self._value(args["id"]), self._value(args.get("days", "0"))))
        elif key == "news_event":
            args = {child.key: child.value for child in value}
            self.events.append((scope.id, self._value(args["id"]), 0))
        elif key == "add_building_construction":
            self._require_scope(scope, "state", key, line)
            args = {child.key: child.value for child in value}
            self.native_calls.append((key, scope.id, self._value(args.get("type")), self._value(args.get("level"))))
        elif key == "remove_building":
            self._require_scope(scope, "state", key, line)
            args = {child.key: child.value for child in value}
            building = self._value(args["type"])
            amount = self._value(args["level"])
            scope.buildings[building] = max(0, scope.buildings.get(building, 0) - amount)

    def advance(self, days):
        self.globals["num_days"] += days
        expired = [key for key, expiry in self.timed_flags.items() if expiry <= self.globals["num_days"]]
        for scope_id, flag in expired:
            for scope in self._all_scopes:
                if scope.id == scope_id:
                    scope.flags.discard(flag)
            del self.timed_flags[(scope_id, flag)]

    @property
    def _all_scopes(self):
        seen = {}
        for definition in self.effect_defs.values():
            del definition
        return list(_SCOPE_REGISTRY.values())


_SCOPE_REGISTRY = {}


def country(identifier):
    scope = Scope("country", identifier)
    _SCOPE_REGISTRY[("country", identifier)] = scope
    return scope


def state(identifier, owner, controller=None):
    scope = Scope("state", identifier, owner=owner, controller=controller or owner)
    _SCOPE_REGISTRY[("state", identifier)] = scope
    return scope


def registered_case(stage="shuttered", episode=35):
    _SCOPE_REGISTRY.clear()
    owner = country("AAA")
    owner.flags.add("great_depression_active")
    owner.values.update({
        "great_depression_active_episode_id": episode,
        "great_depression_depression_severity": 45,
        "great_depression_episode_peak_severity": 55,
        "great_depression_evolution_floor": 0,
        "great_depression_phase": 1,
        "great_depression_doctrine": 1,
        "great_depression_center_count": 1,
        "great_depression_active_start_date": 100,
    })
    owner.resources.update({
        "political_power": 500, "manpower": 500000, "fuel": 5000,
        "train_equipment": 500, "convoy_1": 500, "support_equipment": 500,
        "civilian_factories_available": 20, "stability": 0.7, "war_support": 0.6,
    })
    site = state(121, owner)
    site.population_k = 8000
    site.buildings.update({"industrial_complex": 3, "arms_factory": 1, "dockyard": 0})
    site.flags.update({"great_depression_center", f"great_depression_center_{stage}"})
    site.values.update({
        "great_depression_center_episode_id": episode,
        "great_depression_center_registry_index": 0,
        "great_depression_center_stage": 2,
    })
    owner.arrays.update({
        "great_depression_center_state_ids": [site],
        "great_depression_center_stage_entries": [2],
        "great_depression_center_project_entries": [0],
        "great_depression_center_loss_receipt_entries": [0],
        "great_depression_center_factory_baseline_civilian_entries": [3],
        "great_depression_center_factory_baseline_military_entries": [1],
        "great_depression_center_project_stage_entries": [0],
        "great_depression_center_project_start_day_entries": [0],
        "great_depression_center_project_stage_day_entries": [0],
        "great_depression_center_project_due_day_entries": [0],
        "great_depression_center_project_pause_day_entries": [0],
        "great_depression_center_owner_country_entries": [owner],
        "great_depression_center_event35_civilian_loss_entries": [0],
        "great_depression_center_event35_military_loss_entries": [0],
    })
    owner.values["great_depression_selected_center_state"] = site
    owner.flags.add("great_depression_center_selected")
    runtime = Event35Runtime()
    return runtime, owner, site


def append_existing_center_row(owner, site, stage, project=0):
    """Seed an already-registered row with all parallel registry columns."""
    row = {
        "great_depression_center_state_ids": site,
        "great_depression_center_stage_entries": stage,
        "great_depression_center_project_entries": project,
        "great_depression_center_loss_receipt_entries": 0,
        "great_depression_center_factory_baseline_civilian_entries": site.buildings.get("industrial_complex", 0),
        "great_depression_center_factory_baseline_military_entries": site.buildings.get("arms_factory", 0),
        "great_depression_center_project_stage_entries": 0,
        "great_depression_center_project_start_day_entries": 0,
        "great_depression_center_project_stage_day_entries": 0,
        "great_depression_center_project_due_day_entries": 0,
        "great_depression_center_project_pause_day_entries": 0,
        "great_depression_center_owner_country_entries": owner,
        "great_depression_center_event35_civilian_loss_entries": 0,
        "great_depression_center_event35_military_loss_entries": 0,
    }
    index = len(owner.arrays["great_depression_center_state_ids"])
    for name, value in row.items():
        owner.arrays[name].append(value)
    owner.values["great_depression_center_count"] = index + 1
    site.values["great_depression_center_registry_index"] = index


def register_inherited_state(runtime, owner, site, episode, failed_authorization=0):
    """Apply inheritance to an already validated existing center row.

    This does not claim coverage of validation, preflight, commit, or the
    public inherited-region registration contract.
    """
    owner.values.update({
        "great_depression_region_resolved_state": site,
        "great_depression_region_existing_center": 0,
        "great_depression_region_resolved_stage": runtime.constants["constant:great_depression_center_stage.shuttered"],
        "great_depression_region_call_episode_id": episode,
        "great_depression_region_call_event34_episode_id": 7,
        "great_depression_region_call_state_id": site.id,
        "great_depression_region_call_role": 0,
        "great_depression_region_call_project_profile": 0,
        "great_depression_region_call_project_stage": 0,
        "great_depression_region_call_protection": 0,
        "great_depression_region_call_fragility": 0,
        "great_depression_region_call_control": 0,
        "great_depression_region_call_damage": 0,
        "great_depression_region_call_receipt_id": 1,
        "great_depression_region_call_collapse_receipt_id": 1,
        "great_depression_region_call_legacy_receipt_id": 0,
        "great_depression_region_call_corridor_receipt_id": 0,
        "great_depression_region_call_exhaustion": 0,
    })
    site.values["great_depression_center_project_failed_authorization_id"] = failed_authorization
    if failed_authorization:
        site.values["great_depression_center_project_authorization_id"] = failed_authorization
        site.flags.add("great_depression_center_project_failed_receipt")
    runtime.targets["great_depression_inherited_region_state"] = site
    runtime.run_effect("great_depression_apply_inherited_center_state", owner, root=owner)


def pay_action(runtime, owner, site, action, target_trigger, cost_trigger):
    if not runtime.test_trigger(target_trigger, site, root=owner):
        return False
    if not runtime.test_trigger(cost_trigger, owner, root=owner):
        return False
    runtime.run_effect(action, site, root=owner)
    return True


class CenterProjectSourceTests(unittest.TestCase):
    def test_native_not_is_nor(self):
        runtime, owner, _ = registered_case()
        predicate = Node("NOT", "=", [
            Node("has_country_flag", "=", "fixture_not_first", 0),
            Node("has_country_flag", "=", "fixture_not_second", 0),
        ], 0)
        for first_flag, second_flag in ((False, False), (True, False), (False, True), (True, True)):
            with self.subTest(first=first_flag, second=second_flag):
                for flag, present in (("fixture_not_first", first_flag), ("fixture_not_second", second_flag)):
                    (owner.flags.add if present else owner.flags.discard)(flag)
                self.assertEqual(runtime._condition(predicate, owner), not (first_flag or second_flag))

    def prepared(self, stage="shuttered", episode=35):
        runtime, owner, site = registered_case(stage, episode)
        runtime.run_effect("great_depression_refresh_costs", owner, root=owner)
        return runtime, owner, site

    def complete_by_processing(self, runtime, owner, site):
        total = runtime.constants["constant:great_depression_event.center_project_total_days"]
        runtime.advance(int(total))
        runtime.run_effect("great_depression_process_center_project", site, root=owner)

    def assert_project_ledger_matches(self, owner, site):
        index = site.values["great_depression_center_registry_index"]
        for array_name, state_name in (
            ("great_depression_center_project_entries", "great_depression_center_project_type"),
            ("great_depression_center_project_stage_entries", "great_depression_center_project_stage"),
            ("great_depression_center_project_start_day_entries", "great_depression_center_project_start_day"),
            ("great_depression_center_project_stage_day_entries", "great_depression_center_project_stage_day"),
            ("great_depression_center_project_due_day_entries", "great_depression_center_project_due_day"),
            ("great_depression_center_project_pause_day_entries", "great_depression_center_project_pause_day"),
        ):
            self.assertEqual(owner.arrays[array_name][index], site.values[state_name], array_name)

    def test_completed_reopening_then_public_works_then_lasting_capacity(self):
        runtime, owner, site = self.prepared("shuttered")
        resource_writes_before = len(runtime.resource_writes)
        cooldown_writes_before = len(runtime.timed_flag_writes)
        self.assertTrue(pay_action(runtime, owner, site, "great_depression_reopen_selected_center",
                                   "great_depression_center_reopen_target_is_valid", "great_depression_can_pay_center_reopen"))
        quote = {
            "manpower": -owner.values["great_depression_cost_manpower"],
            "fuel": -owner.values["great_depression_cost_fuel"],
            "train_equipment": -owner.values["great_depression_cost_trains"],
        }
        actual_writes = runtime.resource_writes[resource_writes_before:]
        self.assertEqual(len(actual_writes), 3)
        self.assertEqual({resource: amount for _, resource, amount in actual_writes}, quote)
        self.assertEqual(
            runtime.timed_flag_writes[cooldown_writes_before:],
            [(owner.id, "great_depression_action_lock", 7)],
        )
        self.assertEqual(owner.values["great_depression_committed_civilian"], owner.values["great_depression_cost_civilian"])
        self.assertEqual(owner.values["great_depression_severity_trend"], runtime.constants["constant:great_depression_action.center_reopen_relief"])
        self.assertNotIn("great_depression_action_delta", runtime.temp_frames[0])
        self.assert_project_ledger_matches(owner, site)
        self.assertEqual(site.values["great_depression_center_project_type"], runtime.constants["constant:great_depression_center_project.reopened_capacity"])
        self.assertTrue(owner.flags.__contains__("great_depression_action_lock"))
        self.assertEqual(runtime.timed_flag_writes[-1][1:], ("great_depression_action_lock", 7))
        self.complete_by_processing(runtime, owner, site)
        self.assert_project_ledger_matches(owner, site)
        first_authorization = site.values["great_depression_center_project_authorization_id"]
        self.assertIn("great_depression_center_project_completed_receipt", site.flags)
        self.assertEqual(site.values["great_depression_center_project_completed_authorization_id"], first_authorization)
        self.assertEqual(site.values["great_depression_center_episode_id"], owner.values["great_depression_active_episode_id"])
        self.assertEqual(owner.values["great_depression_centers_reopened_count"], 1)

        runtime.advance(8)
        self.assertTrue(pay_action(runtime, owner, site, "great_depression_launch_regional_works_program",
                                   "great_depression_center_public_works_target_is_valid", "great_depression_can_pay_public_works"))
        resource_writes_after_works = len(runtime.resource_writes)
        cooldown_writes_after_works = len(runtime.timed_flag_writes)
        runtime.run_effect("great_depression_launch_regional_works_program", site, root=owner)
        self.assertEqual(len(runtime.resource_writes), resource_writes_after_works)
        self.assertEqual(len(runtime.timed_flag_writes), cooldown_writes_after_works)
        self.assert_project_ledger_matches(owner, site)
        self.assertGreater(site.values["great_depression_center_project_authorization_id"], first_authorization)
        self.complete_by_processing(runtime, owner, site)
        self.assert_project_ledger_matches(owner, site)
        self.assertIn("great_depression_center_public_works_completed_receipt", site.flags)
        self.assertEqual(site.values["great_depression_center_episode_id"], owner.values["great_depression_active_episode_id"])

        runtime.advance(8)
        self.assertTrue(pay_action(runtime, owner, site, "great_depression_convert_works_into_lasting_capacity",
                                   "great_depression_center_lasting_capacity_target_is_valid", "great_depression_can_pay_public_works"))
        self.complete_by_processing(runtime, owner, site)
        self.assert_project_ledger_matches(owner, site)
        self.assertIn("great_depression_center_lasting_capacity_completed_receipt", site.flags)
        self.assertIn("great_depression_center_lasting_capacity", site.flags)
        self.assertEqual(owner.values["great_depression_lasting_capacity_count"], 1)
        self.assertEqual(site.values["great_depression_center_episode_id"], owner.values["great_depression_active_episode_id"])
        runtime.run_effect("great_depression_clear_center_treatment_flags", site, root=owner)
        self.assertNotIn("great_depression_center_lasting_capacity", site.flags)
        self.assertIn("great_depression_center_lasting_capacity_completed_receipt", site.flags)
        self.assertTrue(runtime.test_trigger("great_depression_center_lasting_capacity_target_is_valid", site, root=owner) is False)

    def test_inherited_failed_receipt_can_reclose_then_accept_paid_reopening(self):
        runtime, owner, site = self.prepared("distressed", episode=41)
        register_inherited_state(runtime, owner, site, 41, failed_authorization=9)
        self.assertEqual(site.values["great_depression_center_episode_id"], 41)
        self.assertIn("great_depression_inherited_center", site.flags)
        self.assertIn("great_depression_center_shuttered", site.flags)
        self.assertIn("great_depression_center_project_failed_receipt", site.flags)
        self.assertTrue(pay_action(runtime, owner, site, "great_depression_reopen_selected_center",
                                   "great_depression_center_reopen_target_is_valid", "great_depression_can_pay_center_reopen"))
        self.assertNotIn("great_depression_center_project_failed_receipt", site.flags)
        self.assertEqual(site.values["great_depression_center_project_failed_authorization_id"], 9)
        self.assertEqual(site.values["great_depression_center_project_authorization_id"], 10)
        self.assertEqual(site.values["great_depression_center_project_episode_id"], 41)
        self.assertTrue(any(op[1] == "train_equipment" and op[2] < 0 for op in runtime.resource_writes))

    def test_active_project_blocks_target_and_paid_action(self):
        runtime, owner, site = self.prepared("shuttered")
        site.flags.update({"great_depression_center_project_authorized"})
        owner.flags.add("great_depression_center_project_active")
        site.values.update({
            "great_depression_center_project_authorization_id": 2,
            "great_depression_center_project_episode_id": owner.values["great_depression_active_episode_id"],
            "great_depression_center_project_type": runtime.constants["constant:great_depression_center_project.reopened_capacity"],
        })
        before = dict(owner.resources)
        before_resource_writes = len(runtime.resource_writes)
        before_cooldown_writes = len(runtime.timed_flag_writes)
        self.assertFalse(runtime.test_trigger("great_depression_center_reopen_target_is_valid", site, root=owner))
        runtime.run_effect("great_depression_reopen_selected_center", site, root=owner)
        self.assertEqual(owner.resources, before)
        self.assertEqual(len(runtime.resource_writes), before_resource_writes)
        self.assertEqual(len(runtime.timed_flag_writes), before_cooldown_writes)
        self.assertFalse(owner.flags.__contains__("great_depression_action_lock"))

    def test_old_or_foreign_episode_is_rejected_before_payment(self):
        runtime, owner, site = self.prepared("shuttered", episode=52)
        site.values["great_depression_center_episode_id"] = 51
        self.assertFalse(runtime.test_trigger("great_depression_center_reopen_target_is_valid", site, root=owner))
        before = dict(owner.resources)
        before_writes = len(runtime.resource_writes)
        before_cooldowns = len(runtime.timed_flag_writes)
        runtime.run_effect("great_depression_reopen_selected_center", site, root=owner)
        self.assertEqual(owner.resources, before)
        self.assertEqual(len(runtime.resource_writes), before_writes)
        self.assertEqual(len(runtime.timed_flag_writes), before_cooldowns)

        foreign = country("BBB")
        foreign.values.update(owner.values)
        foreign.flags.add("great_depression_active")
        foreign.arrays["great_depression_center_state_ids"] = [site]
        site.owner = foreign
        site.controller = foreign
        site.values["great_depression_center_episode_id"] = owner.values["great_depression_active_episode_id"]
        self.assertFalse(runtime.test_trigger("great_depression_center_reopen_target_is_valid", site, root=owner))

    def test_duplicate_completion_does_not_repeat_reward(self):
        runtime, owner, site = self.prepared("shuttered")
        self.assertTrue(pay_action(runtime, owner, site, "great_depression_reopen_selected_center",
                                   "great_depression_center_reopen_target_is_valid", "great_depression_can_pay_center_reopen"))
        self.complete_by_processing(runtime, owner, site)
        snapshot = (owner.values.get("great_depression_centers_reopened_count", 0),
                    owner.values.get("great_depression_lasting_capacity_count", 0),
                    set(site.flags), dict(site.values))
        runtime.run_effect("great_depression_complete_center_project", site, root=owner)
        self.assertEqual(snapshot[0], owner.values.get("great_depression_centers_reopened_count", 0))
        self.assertEqual(snapshot[1], owner.values.get("great_depression_lasting_capacity_count", 0))
        self.assertEqual(snapshot[2], site.flags)
        self.assertEqual(snapshot[3], site.values)

    def test_protection_branch_closes_only_after_total_work(self):
        runtime, owner, site = self.prepared("distressed")
        owner.values["great_depression_pending_center_project"] = runtime.constants["constant:great_depression_center_project.protection"]
        runtime.run_effect("great_depression_authorize_center_project", site, root=owner)
        self.assertIn("great_depression_center_project_authorized", site.flags)
        runtime.advance(int(runtime.constants["constant:great_depression_event.center_project_total_days"]) - 1)
        runtime.run_effect("great_depression_process_center_project", site, root=owner)
        self.assertNotIn("great_depression_center_project_completed_receipt", site.flags)
        runtime.advance(1)
        runtime.run_effect("great_depression_process_center_project", site, root=owner)
        self.assertIn("great_depression_center_project_completed_receipt", site.flags)
        self.assertIn("great_depression_center_protected", site.flags)
        self.assertNotIn("great_depression_center_project_authorized", site.flags)
        self.assert_project_ledger_matches(owner, site)

    def test_failure_retry_preserves_historical_completion_receipt(self):
        runtime, owner, site = self.prepared("shuttered")
        self.assertTrue(pay_action(runtime, owner, site, "great_depression_reopen_selected_center",
                                   "great_depression_center_reopen_target_is_valid", "great_depression_can_pay_center_reopen"))
        self.complete_by_processing(runtime, owner, site)
        completed_id = site.values["great_depression_center_project_completed_authorization_id"]
        runtime.advance(8)
        self.assertTrue(pay_action(runtime, owner, site, "great_depression_launch_regional_works_program",
                                   "great_depression_center_public_works_target_is_valid", "great_depression_can_pay_public_works"))
        runtime.run_effect("great_depression_fail_center_project", site, root=owner)
        self.assertIn("great_depression_center_project_completed_receipt", site.flags)
        self.assertEqual(site.values["great_depression_center_project_completed_authorization_id"], completed_id)
        failed_id = site.values["great_depression_center_project_failed_authorization_id"]
        runtime.advance(8)
        self.assertTrue(pay_action(runtime, owner, site, "great_depression_convert_works_into_lasting_capacity",
                                   "great_depression_center_lasting_capacity_target_is_valid", "great_depression_can_pay_public_works"))
        self.assertEqual(site.values["great_depression_center_project_failed_authorization_id"], failed_id)
        self.assertGreater(site.values["great_depression_center_project_authorization_id"], failed_id)
        self.assertEqual(site.values["great_depression_center_project_completed_authorization_id"], completed_id)

    def test_transfer_retains_receipts_and_adopts_new_episode_identity(self):
        runtime, owner, site = self.prepared("reopened", episode=61)
        site.flags.update({"great_depression_center_project_completed_receipt", "great_depression_center_lasting_capacity_completed_receipt"})
        site.values.update({
            "great_depression_center_project_authorization_id": 4,
            "great_depression_center_project_completed_authorization_id": 4,
            "great_depression_center_project_failed_authorization_id": 3,
            "great_depression_center_project_episode_id": 61,
        })
        successor = country("BBB")
        successor.flags.add("great_depression_active")
        successor.values.update({
            "great_depression_active_episode_id": 72,
            "great_depression_depression_severity": 35,
            "great_depression_evolution_floor": 0,
            "great_depression_center_count": 0,
        })
        successor.arrays.update({name: [] for name in owner.arrays})
        site.owner = successor
        site.controller = successor
        runtime.run_effect("great_depression_reconcile_center_transfer", site, root=owner)
        self.assertIn("great_depression_center_transfer_receipt", site.flags)
        self.assertEqual(site.values["great_depression_center_transfer_episode_id"], 61)
        self.assertEqual(site.values["great_depression_center_project_completed_authorization_id"], 4)
        self.assertTrue(runtime.external_calls)
        runtime.run_effect("great_depression_select_center", site, root=successor)
        self.assertIn(site, successor.arrays["great_depression_center_state_ids"])
        self.assertEqual(site.values["great_depression_center_episode_id"], 72)
        self.assertEqual(site.values["great_depression_center_project_episode_id"], 61)
        self.assertEqual(site.values["great_depression_center_project_authorization_id"], 4)
        self.assertEqual(site.values["great_depression_center_project_completed_authorization_id"], 4)
        self.assertEqual(site.values["great_depression_center_project_failed_authorization_id"], 3)

    def test_pending_transfer_adoption_replay_second_transfer_and_lost_interval(self):
        runtime, owner, site = self.prepared("reopened", episode=61)
        site.flags.add("great_depression_center_project_active_work")
        owner.flags.add("great_depression_center_project_active")
        site.values.update({
            "great_depression_center_project_authorization_id": 5,
            "great_depression_center_project_completed_authorization_id": 4,
            "great_depression_center_project_failed_authorization_id": 3,
            "great_depression_center_project_episode_id": 61,
            "great_depression_center_project_type": runtime.constants["constant:great_depression_center_project.public_works"],
            "great_depression_center_project_stage": runtime.constants["constant:great_depression_center_project_stage.active_work"],
            "great_depression_center_project_start_day": 280,
            "great_depression_center_project_stage_day": 300,
            "great_depression_center_project_due_day": 380,
            "great_depression_center_project_pause_day": 0,
            "great_depression_center_project_pause_days": 0,
            "great_depression_center_project_work_days": 12,
            "great_depression_center_project_last_process_day": 300,
        })
        successor = country("BBB")
        successor.flags.add("great_depression_active")
        successor.values.update({
            "great_depression_active_episode_id": 72,
            "great_depression_depression_severity": 35,
            "great_depression_evolution_floor": 0,
            "great_depression_center_count": 0,
        })
        successor.arrays.update({name: [] for name in owner.arrays})
        site.owner = successor
        site.controller = successor

        runtime.run_effect("great_depression_reconcile_center_transfer", site, root=owner)
        self.assertEqual(site.values["great_depression_center_project_pause_day"], 300)
        self.assertIn("great_depression_center_project_paused", site.flags)
        self.assertNotIn("great_depression_center_project_active", owner.flags)
        self.assertEqual(site.values["great_depression_center_project_work_days"], 12)
        runtime.advance(20)
        runtime.run_effect("great_depression_select_center", site, root=successor)
        self.assertEqual(site.values["great_depression_center_episode_id"], 72)
        self.assertEqual(site.values["great_depression_center_project_episode_id"], 72)
        self.assertEqual(site.values["great_depression_center_project_authorization_id"], 5)
        self.assertEqual(site.values["great_depression_center_project_completed_authorization_id"], 4)
        self.assertEqual(site.values["great_depression_center_project_failed_authorization_id"], 3)
        self.assertIn("great_depression_center_project_active", successor.flags)

        row_count = len(successor.arrays["great_depression_center_state_ids"])
        center_count = successor.values["great_depression_center_count"]
        registry_index = site.values["great_depression_center_registry_index"]
        runtime.run_effect("great_depression_select_center", site, root=successor)
        self.assertEqual(len(successor.arrays["great_depression_center_state_ids"]), row_count)
        self.assertEqual(successor.values["great_depression_center_count"], center_count)
        self.assertEqual(site.values["great_depression_center_registry_index"], registry_index)

        runtime.run_effect("great_depression_process_center_project", site, root=successor)
        self.assertEqual(site.values["great_depression_center_project_work_days"], 12)
        self.assertEqual(site.values["great_depression_center_project_due_day"], 400)

        # A different lost center has no project of its own and cannot release this slot.
        other = state(122, successor)
        other.population_k = 7000
        other.buildings["industrial_complex"] = 2
        other.flags.add("great_depression_center")
        other.values.update({
            "great_depression_center_episode_id": 72,
        })
        append_existing_center_row(successor, other, 2)
        third = country("CCC")
        other.owner = third
        other.controller = third
        runtime.run_effect("great_depression_reconcile_center_transfer", other, root=successor)
        self.assertIn("great_depression_center_project_active", successor.flags)

        # The historical transfer receipt remains, while the closed contract permits a second transfer.
        site.owner = third
        site.controller = third
        transfer_count = successor.values["great_depression_center_transfer_count"]
        runtime.run_effect("great_depression_reconcile_center_transfer", site, root=successor)
        self.assertIn("great_depression_center_transfer_contract_open", site.flags)
        self.assertEqual(site.values["great_depression_center_transfer_episode_id"], 72)
        self.assertEqual(successor.values["great_depression_center_transfer_count"], transfer_count + 1)
        runtime.run_effect("great_depression_reconcile_center_transfer", site, root=successor)
        self.assertEqual(successor.values["great_depression_center_transfer_count"], transfer_count + 1)

    def test_terminal_cleanup_only_clears_matching_episode(self):
        runtime, owner, first = self.prepared("reopened", episode=84)
        second = state(122, owner)
        second.values["great_depression_center_episode_id"] = 85
        second.flags.update({"great_depression_center", "great_depression_center_reopened", "great_depression_center_lasting_capacity_completed_receipt"})
        append_existing_center_row(owner, second, 2)
        first.flags.update({"great_depression_center_project_completed_receipt", "great_depression_center_lasting_capacity_completed_receipt"})
        first.values.update({
            "great_depression_center_project_authorization_id": 9,
            "great_depression_center_project_completed_authorization_id": 8,
            "great_depression_center_project_failed_authorization_id": 7,
            "great_depression_center_project_episode_id": 84,
            "great_depression_center_project_type": 4,
            "great_depression_center_project_work_days": 22,
        })
        first.flags.add("great_depression_center_reconstruction_building_receipt")
        runtime.run_effect("great_depression_clear_center_resolution_receipts", owner, root=owner)
        self.assertNotIn("great_depression_center", first.flags)
        self.assertNotIn("great_depression_center_lasting_capacity_completed_receipt", first.flags)
        self.assertNotIn("great_depression_center_episode_id", first.values)
        self.assertNotIn("great_depression_center_project_episode_id", first.values)
        self.assertNotIn("great_depression_center_project_type", first.values)
        self.assertNotIn("great_depression_center_project_work_days", first.values)
        self.assertEqual(first.values["great_depression_center_project_authorization_id"], 9)
        self.assertEqual(first.values["great_depression_center_project_completed_authorization_id"], 8)
        self.assertEqual(first.values["great_depression_center_project_failed_authorization_id"], 7)
        self.assertNotIn("great_depression_center_reconstruction_building_receipt", first.flags)
        self.assertIn("great_depression_center", second.flags)
        self.assertIn("great_depression_center_lasting_capacity_completed_receipt", second.flags)
        self.assertEqual(second.values["great_depression_center_episode_id"], 85)


class DoctrineProjectProducerTests(unittest.TestCase):
    """Producers for finance_restoration, transport_integration and
    international_reconstruction, and the Strategic Industry closers."""

    prepared = CenterProjectSourceTests.prepared
    complete_by_processing = CenterProjectSourceTests.complete_by_processing

    def project(self, runtime, name):
        return runtime.constants["constant:great_depression_center_project." + name]

    def test_finance_restoration_needs_audit_then_reopens_restructured(self):
        runtime, owner, site = self.prepared("shuttered")
        owner.values["great_depression_doctrine"] = 3
        self.assertFalse(runtime.test_trigger("great_depression_can_start_finance_restoration", site, root=owner))
        owner.flags.add("great_depression_bank_audit_complete")
        self.assertTrue(pay_action(runtime, owner, site, "great_depression_restore_local_credit_and_trade_connection",
                                   "great_depression_can_start_finance_restoration", "great_depression_can_pay_finance_trade"))
        self.assertEqual(site.values["great_depression_center_project_type"], self.project(runtime, "finance_restoration"))
        self.assertNotIn("great_depression_pending_center_project", owner.values)
        self.complete_by_processing(runtime, owner, site)
        self.assertIn("great_depression_center_finance_restored", site.flags)
        self.assertIn("great_depression_center_restructured", site.flags)

    def test_freight_success_starts_transport_then_credits_once(self):
        runtime, owner, site = self.prepared("idled")
        runtime.run_effect("great_depression_apply_freight_to_selected_center", owner, root=owner)
        self.assertEqual(site.values["great_depression_center_project_type"], self.project(runtime, "transport_integration"))
        self.assertNotIn("great_depression_paid_center_project", owner.values)
        self.assertNotIn("great_depression_pending_center_project", owner.values)
        runtime.advance(5)
        runtime.run_effect("great_depression_process_center_project", site, root=owner)
        before = site.values["great_depression_center_project_work_days"]
        runtime.run_effect("great_depression_apply_freight_to_selected_center", owner, root=owner)
        credit = runtime.constants["constant:great_depression_center_project_credit.freight_days"]
        self.assertEqual(site.values["great_depression_center_project_work_days"], before + credit)
        runtime.run_effect("great_depression_apply_freight_to_selected_center", owner, root=owner)
        self.assertEqual(site.values["great_depression_center_project_work_days"], before + credit)
        self.complete_by_processing(runtime, owner, site)
        self.assertIn("great_depression_center_reopened", site.flags)
        self.assertNotIn("great_depression_center_restructured", site.flags)

    def test_coordinated_reconstruction_starts_project_only_when_slot_is_open(self):
        runtime, owner, site = self.prepared("shuttered")
        owner.flags.add("great_depression_center_project_active")
        runtime.run_effect("great_depression_start_international_reconstruction_project", owner, root=owner)
        self.assertNotIn("great_depression_center_project_type", site.values)
        self.assertNotIn("great_depression_pending_center_project", owner.values)
        owner.flags.discard("great_depression_center_project_active")
        runtime.run_effect("great_depression_start_international_reconstruction_project", owner, root=owner)
        self.assertEqual(site.values["great_depression_center_project_type"], self.project(runtime, "international_reconstruction"))
        self.complete_by_processing(runtime, owner, site)
        self.assertIn("great_depression_center_public_works", site.flags)

    def test_strategic_closers_satisfy_relapse_measure_and_exclude_each_other(self):
        for closer, flag in (("great_depression_end_rescue_dependence", "great_depression_rescue_dependence_ended"),
                             ("great_depression_retain_bounded_arsenal_institution", "great_depression_arsenal_institution_retained")):
            with self.subTest(closer=closer):
                runtime, owner, site = self.prepared("reopened")
                owner.values["great_depression_doctrine"] = 2
                owner.flags.add("great_depression_strategic_network_designated")
                site.flags.add("great_depression_center_strategic")
                self.assertTrue(runtime.test_trigger("great_depression_should_show_strategic_rescue_closer", owner, root=owner))
                self.assertFalse(runtime.test_trigger("great_depression_strategic_closer_phase_is_open", owner, root=owner))
                owner.values["great_depression_phase"] = runtime.constants["constant:great_depression_phase.stabilization"]
                self.assertTrue(runtime.test_trigger("great_depression_strategic_closer_phase_is_open", owner, root=owner))
                runtime.run_effect(closer, owner, root=owner)
                self.assertIn(flag, owner.flags)
                self.assertFalse(runtime.test_trigger("great_depression_should_show_strategic_rescue_closer", owner, root=owner))
                self.assertEqual(flag == "great_depression_arsenal_institution_retained",
                                 "great_depression_essential_orders_guaranteed" in owner.flags)


if __name__ == "__main__":
    unittest.main(verbosity=2)
