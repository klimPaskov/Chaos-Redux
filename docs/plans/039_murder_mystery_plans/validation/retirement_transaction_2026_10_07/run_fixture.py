"""Event039 retirement and row consumption: bounded actual-source execution.

Run from mod root: python -B docs/plans/039_murder_mystery_plans/validation/retirement_transaction_2026_10_07/run_fixture.py
No source writes, engine launches, or general-purpose HOI4 execution API.
"""
import copy
from decimal import Decimal
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
P = "murder_mystery_"
RETIRE = P + "retire_selected_leader"
MARK = P + "mark_selected_target_removed"
CAPTURE = P + "capture_current_ruling_character"
FIELDS = ("id", "disposition", "role", "owner", "subject", "protection", "used", "generation")
SOURCE_FILES = [
    "common/scripted_effects/039_murder_mystery_character_effects.txt",
    "common/scripted_effects/039_murder_mystery_runtime_effects.txt",
    "common/scripted_triggers/039_murder_mystery_character_triggers.txt",
    "common/scripted_triggers/039_murder_mystery_runtime_triggers.txt",
    "common/script_constants/039_murder_mystery_constants.txt",
    "common/scripted_effects/039_murder_mystery_integration_effects.txt",  # hashed caller boundary, not executed
    ".tools/3d_pipeline/runtime/clausewitz.py",
]
EFFECTS = {RETIRE, MARK, CAPTURE, P + "prepare_safe_target_action",
           P + "validate_selected_target", P + "approve_selected_target_owner"}
TRIGGERS = {P + x for x in (
    "selected_target_is_registered", "selected_target_allows_named_action",
    "selected_target_allows_generic_office", "target_registry_is_aligned",
    "selected_character_is_recruited", "runtime_is_active", "runtime_is_initialized")}


class Unsupported(RuntimeError):
    pass


class Sources:
    def __init__(self):
        # Read exact current bytes once, hash the same bytes parsed, then verify
        # them again after all cases. Concurrent changes invalidate this run.
        self.bytes = {p: (REPO / p).read_bytes() for p in SOURCE_FILES}
        self.hashes = {p: hashlib.sha256(b).hexdigest() for p, b in self.bytes.items()}
        spec = importlib.util.spec_from_file_location("retirement_clausewitz", REPO / SOURCE_FILES[-1])
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        self.parse = module.parse
        self.defs, self.locations, self.constants = {}, {}, {}
        for path, raw in self.bytes.items():
            if path.endswith(".py"):
                continue
            tree = self.parse(raw.decode("utf-8-sig"))
            for n in tree.children():
                if "script_constants" in path:
                    for c in n.children():
                        if not isinstance(c.value, list):
                            value = Decimal(c.value)
                            self.constants[n.key + "." + c.key] = int(value) if value == value.to_integral_value() else value
                elif n.key in EFFECTS | TRIGGERS:
                    if n.key in self.defs:
                        raise Unsupported("Duplicate helper " + n.key)
                    self.defs[n.key] = n
                    self.locations[n.key] = {"path": path, "line": n.line}
        missing = (EFFECTS | TRIGGERS) - self.defs.keys()
        if missing:
            raise Unsupported("Missing actual helper bodies: " + repr(missing))
        for name in EFFECTS | TRIGGERS:
            self.validate(self.defs[name].children(), name in TRIGGERS)

    def validate(self, nodes, trigger=False):
        """Validate the whole selected AST, including branches not executed."""
        for n in nodes:
            k, v = n.key, n.value
            if not k:
                raise Unsupported(f"Anonymous/operator token at line {n.line}: {v}")
            if k in EFFECTS | TRIGGERS:
                if v != "yes" or (trigger and k in EFFECTS):
                    raise Unsupported("Unsupported helper call " + k)
            elif k in {"if", "else_if", "else", "while_loop_effect", "every_character"} and not trigger:
                for c in n.children():
                    if c.key == "limit":
                        self.validate(c.children(), True)
                    else:
                        self.validate([c], False)
            elif k in {"AND", "OR", "NOT", "any_character", "hidden_trigger"} and trigger:
                self.validate(n.children(), True)
            elif k in {"ROOT", "PREV", "THIS"} or k.startswith(("event_target:", "var:")):
                self.validate(n.children(), trigger)
            elif k == "check_variable" and trigger:
                if {c.key for c in n.children()} != {"var", "value", "compare"}:
                    raise Unsupported("Only explicit check_variable supported")
                if n.scalar("compare") not in {"equals", "less_than", "greater_than", "less_than_or_equals", "greater_than_or_equals"}:
                    raise Unsupported("Unsupported comparison")
            elif k in {"set_variable", "set_temp_variable", "add_to_temp_variable"} and not trigger:
                if len(n.children()) != 1 or isinstance(n.children()[0].value, list):
                    raise Unsupported("Only one scalar variable assignment supported")
            elif trigger and k in {"has_variable", "has_country_flag", "has_global_flag", "has_character_flag", "has_event_target", "is_character", "tag", "exists", "has_trait", "is_country_leader"}:
                if isinstance(v, list):
                    raise Unsupported("Unsupported predicate arguments " + k)
            elif not trigger and k in {"clr_country_flag", "set_country_flag", "clr_global_flag", "set_global_flag", "clear_variable", "save_event_target_as", "save_global_event_target_as", "clear_global_event_target", "add_country_leader_trait", "remove_country_leader_trait", "retire"}:
                if isinstance(v, list):
                    raise Unsupported("Unsupported effect arguments " + k)
                if k == "retire" and v != "yes":
                    raise Unsupported("Unsupported retirement argument")
            else:
                raise Unsupported(f"Unsupported {'trigger' if trigger else 'effect'} {k} at line {n.line}")

    def stable(self):
        return all((REPO / p).read_bytes() == b for p, b in self.bytes.items())


class World:
    def __init__(self, src, caller="caller"):
        self.src, self.caller, self.root = src, caller, "root"
        self.vars = {x: {} for x in ("caller", "owner", "root", "other_owner", "victim", "successor", "other_victim", "other_successor")}
        self.flags = {x: set() for x in self.vars}
        self.countries = {"caller", "owner", "root", "other_owner"}
        self.rosters = {"caller": [], "root": [], "owner": ["victim", "successor"], "other_owner": ["other_victim", "other_successor"]}
        self.rulers = {"owner": "successor", "other_owner": "other_successor"}
        self.traits = {x: set() for x in self.vars if x not in self.countries}
        self.global_flags = {P + "runtime_initialized", P + "runtime_active"}
        self.global_vars, self.temps, self.local_targets, self.global_targets = {}, {}, {}, {}
        self.trace, self.temp_cleanup, self.steps, self.calls = [], [], 0, {}
        self.injected_row = None
        self.hooks, self.fail_native = {}, False
        for field, values in zip(FIELDS, ([390003, 391001], [1, 1], [1, 1], ["owner", "other_owner"], ["victim", "other_victim"], [1, 0], [0, 0], [17, 23])):
            self.global_vars[P + "target_" + field + "_entries"] = values
        self.vars[caller].update({P + "selected_target_id": 390003, P + "selected_target_expected_generation": 17})
        self.flags[caller].add(P + "target_owner_callback_passed")
        self.flags["owner"].update({P + "capture_successor_verified", P + "first_knife_registered"})
        self.flags["victim"].add(P + "first_knife_character")
        self.global_targets[P + "assassin_state"] = "owner"

    def value(self, token, scope):
        if token.startswith("constant:"):
            return self.src.constants[token[9:]]
        if token.startswith("event_target:"):
            return self.target(token[13:])
        if token in {"ROOT", "THIS"}:
            return self.root if token == "ROOT" else scope
        try:
            return int(token)
        except ValueError:
            pass
        if "^" in token:
            base, index = token.split("^", 1)
            arr = self.value(base, scope)
            if not isinstance(arr, list):
                raise Unsupported("Not an array " + base)
            return len(arr) if index == "num" else arr[self.value(index, scope)]
        if token.startswith("global."):
            return self.global_vars.get(token[7:], 0)
        if "." in token:
            prefix, field = token.split(".", 1)
            if prefix == "ROOT":
                return self.vars[self.root].get(field, 0)
            if prefix in self.vars:
                return self.vars[prefix].get(field, 0)
            raise Unsupported("Unsupported scoped value " + token)
        return self.temps[token] if token in self.temps else self.vars[scope].get(token, 0)

    def target(self, name):
        return self.local_targets.get(name, self.global_targets.get(name))

    def scoped(self, key, scope, prev):
        if key == "ROOT":
            return self.root
        if key == "PREV":
            return prev
        if key == "THIS":
            return scope
        if key.startswith("event_target:"):
            return self.target(key[13:])
        if key.startswith("var:"):
            return self.value(key[4:], scope)
        raise Unsupported("Unknown scope " + key)

    def write(self, key, value, scope, temp=False):
        if temp:
            self.temps[key] = value
        elif "^" in key:
            base, idx = key.split("^", 1)
            self.value(base, scope)[self.value(idx, scope)] = value
        elif key.startswith("global."):
            self.global_vars[key[7:]] = value
        elif "." in key:
            prefix, field = key.split(".", 1)
            owner = self.root if prefix == "ROOT" else prefix
            if owner not in self.vars:
                raise Unsupported("Unsupported variable destination " + key)
            self.vars[owner][field] = value
        else:
            self.vars[scope][key] = value

    def invoke(self, name, scope, prev=None):
        prior = set(self.temps)
        self.calls[name] = self.calls.get(name, 0) + 1
        if name in EFFECTS:
            self.trace.append({"helper": name, "scope": scope, "ROOT": self.root, "PREV": prev})
        self.hook("before:" + name, scope)
        try:
            if name in TRIGGERS:
                return self.test(self.src.defs[name].children(), scope, prev)
            self.execute(self.src.defs[name].children(), scope, prev)
            self.hook("after:" + name, scope)
        finally:
            created = set(self.temps) - prior
            if created or name in EFFECTS:
                self.temp_cleanup.append({"helper": name, "discarded": sorted(created)})
            for key in created:
                del self.temps[key]

    def hook(self, key, scope):
        callback = self.hooks.pop(key, None)
        if callback:
            callback(self, scope)

    def test(self, nodes, scope, prev=None):
        # No short-circuit assumption is needed by these side-effect-free
        # predicates. Evaluate all children so unsupported paths cannot vanish.
        results = [self.predicate(n, scope, prev) for n in nodes]
        return all(results)

    def predicate(self, n, scope, prev):
        k, v = n.key, n.value
        if k in TRIGGERS:
            return self.invoke(k, scope, prev)
        if k in {"AND", "hidden_trigger"}:
            return self.test(n.children(), scope, prev)
        if k in {"OR", "NOT"}:
            items = [self.predicate(c, scope, prev) for c in n.children()]
            return any(items) if k == "OR" else not any(items)
        if k == "check_variable":
            a, b = self.value(n.scalar("var"), scope), self.value(n.scalar("value"), scope)
            return {"equals": lambda: a == b, "less_than": lambda: a < b,
                    "greater_than": lambda: a > b, "less_than_or_equals": lambda: a <= b,
                    "greater_than_or_equals": lambda: a >= b}[n.scalar("compare")]()
        if k == "has_variable":
            return v in self.temps or (v[7:] in self.global_vars if v.startswith("global.") else v in self.vars[scope])
        if k in {"has_country_flag", "has_character_flag"}:
            return v in self.flags[scope]
        if k == "has_global_flag":
            return v in self.global_flags
        if k == "has_event_target":
            return self.target(v) is not None
        if k in {"tag", "is_character"}:
            self.require(scope, "country" if k == "tag" else "character")
            return scope == self.value(v, scope)
        if k == "exists":
            self.require(scope, "country")
            return scope in self.rosters
        if k == "is_country_leader":
            self.require(scope, "character")
            # Native country-leader role is broader than current ruler. The
            # anchor, applied only to ruler, disambiguates in actual capture.
            return any(scope in r for r in self.rosters.values())
        if k == "has_trait":
            self.require(scope, "character")
            return v in self.traits[scope]
        if k == "any_character":
            self.require(scope, "country")
            return any(self.test(n.children(), c, scope) for c in list(self.rosters[scope]))
        dest = self.scoped(k, scope, prev)
        return False if dest is None else self.test(n.children(), dest, scope)

    def require(self, scope, kind):
        if scope not in self.vars or ((scope in self.countries) != (kind == "country")):
            raise Unsupported(f"{kind} operation in {scope}")

    def execute(self, nodes, scope, prev=None):
        branch = None
        for n in nodes:
            self.steps += 1
            if self.steps > 20000:
                raise Unsupported("Fixture instruction budget exhausted")
            k, v = n.key, n.value
            if k in {"if", "else_if", "else"}:
                if k == "if":
                    branch = False
                elif branch is None:
                    raise Unsupported("Orphan else branch")
                take = not branch and (k == "else" or self.test(n.children("limit")[0].children(), scope, prev))
                if take:
                    self.execute([c for c in n.children() if c.key != "limit"], scope, prev)
                    branch = True
                continue
            branch = None
            if k in EFFECTS:
                self.invoke(k, scope, prev)
            elif k == "while_loop_effect":
                count = 0
                while self.test(n.children("limit")[0].children(), scope, prev):
                    count += 1
                    if count > 1000:
                        raise Unsupported("Native loop budget exceeded")
                    self.execute([c for c in n.children() if c.key != "limit"], scope, prev)
            elif k in {"set_variable", "set_temp_variable", "add_to_temp_variable"}:
                c = n.children()[0]
                val = self.value(c.value, scope)
                if k == "add_to_temp_variable":
                    val += self.value(c.key, scope)
                self.write(c.key, val, scope, k != "set_variable")
            elif k == "clear_variable":
                self.vars[scope].pop(v, None)
            elif k in {"set_country_flag", "clr_country_flag"}:
                self.require(scope, "country")
                (self.flags[scope].add if k.startswith("set") else self.flags[scope].discard)(v)
            elif k in {"set_global_flag", "clr_global_flag"}:
                (self.global_flags.add if k.startswith("set") else self.global_flags.discard)(v)
            elif k in {"save_event_target_as", "save_global_event_target_as"}:
                (self.local_targets if k == "save_event_target_as" else self.global_targets)[v] = scope
            elif k == "clear_global_event_target":
                self.global_targets.pop(v, None)
            elif k in {"add_country_leader_trait", "remove_country_leader_trait"}:
                self.require(scope, "country")
                ruler = self.rulers.get(scope)
                if ruler is not None:
                    (self.traits[ruler].add if k.startswith("add") else self.traits[ruler].discard)(v)
                self.hook("native:" + k, scope)
            elif k == "every_character":
                self.require(scope, "country")
                for char in list(self.rosters[scope]):
                    if self.test(n.children("limit")[0].children(), char, scope):
                        self.execute([c for c in n.children() if c.key != "limit"], char, scope)
            elif k == "retire":
                self.require(scope, "character")
                self.trace.append({"native": "retire", "character": scope, "ROOT": self.root})
                if not self.fail_native:
                    for roster in self.rosters.values():
                        if scope in roster:
                            roster.remove(scope)
                self.hook("native:retire", scope)
            else:
                dest = self.scoped(k, scope, prev)
                if dest is None:
                    raise Unsupported("Unresolved effect scope " + k)
                self.execute(n.children(), dest, scope)

    def row(self, index=0):
        return {f: self.global_vars[P + "target_" + f + "_entries"][index] for f in FIELDS}

    def setrow(self, field, value, index=0):
        self.global_vars[P + "target_" + field + "_entries"][index] = value

    def retire(self):
        self.invoke(RETIRE, self.caller)

    def clean(self):
        leaked = {scope: sorted(k for k in values if k.startswith(P + "removal_"))
                  for scope, values in self.vars.items()}
        assert not any(leaked.values()), f"private saved fields leaked: {leaked}"
        assert P + "named_removal_active" not in self.global_flags, "global recursion guard leaked"
        assert not self.temps, f"helper-local temps leaked: {self.temps}"
        assert all(P + "ruling_selection_authorized" not in f for f in self.flags.values()), "ruler authorization leaked"
        assert all(not t for t in self.traits.values()), "native ruler anchor leaked"


def expect(condition, message):
    if not condition:
        raise AssertionError(message)


def rejected(w, before, retires=0):
    expect(w.row() == before, f"rejected operation changed row: {before} -> {w.row()}")
    expect("victim" in w.rosters["owner"], "rejected operation retired victim")
    expect(P + "named_removal_committed" not in w.flags[w.caller], "rejected operation committed")
    expect(P + "named_removal_failed" in w.flags[w.caller], "missing failure receipt")
    expect(P + "target_consumption_committed" not in w.flags[w.caller], "rejected or rolled-back operation retained a consumption receipt")
    expect(sum(t.get("native") == "retire" for t in w.trace) == retires, "unexpected native retirement count")
    expect(P + "named_removal_target_id" not in w.vars[w.caller], "rejection retained success identity")
    w.clean()


def successful(w):
    expect("victim" not in w.rosters["owner"] and "successor" in w.rosters["owner"], "wrong recruited roster after retirement")
    expect(w.row()["used"] == 1 and w.row()["disposition"] == 7 and w.row()["protection"] == 3, "row not consumed")
    expect(P + "named_removal_committed" in w.flags[w.caller], "missing commit receipt")
    expect(P + "target_consumption_committed" in w.flags[w.caller], "successful removal lacks an actual consumption receipt")
    expect(P + "named_removal_failed" not in w.flags[w.caller], "success retains failure flag")
    expect(w.vars[w.caller].get(P + "named_removal_target_id") == 390003, "outcome used overwritten public target ID")
    expect(w.vars[w.caller].get(P + "named_removal_generation") == 17, "outcome used overwritten public generation")
    expect(w.row(1)["used"] == 0 and "other_victim" in w.rosters["other_owner"], "unrelated row/roster changed")
    expect(not w.vars["root"] and not w.flags["root"], "transaction wrote to unrelated ROOT")
    expect(sum(t.get("native") == "retire" for t in w.trace) == 1, "native operation did not execute exactly once")
    w.clean()


def cases(src):
    def success(w):
        w.retire()
        successful(w)
    yield "different_caller_owner_ROOT_success", World(src), success
    yield "owner_caller_different_ROOT_success", World(src, "owner"), success

    def twice(w):
        w.retire()
        successful(w)
        before, roster = w.row(), copy.deepcopy(w.rosters)
        w.retire()
        expect(w.row() == before and w.rosters == roster, "second call changed consumption or roster")
        expect(P + "named_removal_committed" not in w.flags[w.caller], "second call retained successful receipt")
        expect(sum(t.get("native") == "retire" for t in w.trace) == 1, "second call retired again")
        w.clean()
    yield "second_call_rejected", World(src), twice

    for name, field, value in (
        ("stale_expected_generation", None, 16),
        ("protected_target", "protection", 2),
        ("temporarily_protected_target", "disposition", 4),
        ("permanently_protected_target", "disposition", 5),
        ("owner_managed_target", "disposition", 6),
        ("disposed_target", "disposition", 7),
        ("used_target", "used", 1),
    ):
        w = World(src)
        if field:
            w.setrow(field, value)
        else:
            w.vars[w.caller][P + "selected_target_expected_generation"] = value
        def reject(w):
            before = w.row()
            w.retire()
            rejected(w, before)
        yield name, w, reject

    for name, ruler in (("unresolved_successor", None), ("successor_is_victim", "victim")):
        w = World(src)
        w.rulers["owner"] = ruler
        yield name, w, reject

    def failed(w):
        before, roster = w.row(), copy.deepcopy(w.rosters)
        registry = copy.deepcopy(w.global_vars)
        w.fail_native = True
        w.retire()
        rejected(w, before, 1)
        expect(w.rosters == roster, "failed native retirement changed roster")
        expect(w.global_vars == registry, "failed native retirement did not restore the exact entire registry")
        expect(P + "selected_target_retired" not in w.flags[w.caller], "rollback retained consumption flag")
    yield "failed_native_restores_exact_row", World(src), failed

    # Hook after actual capture but before revalidation checks frozen inputs.
    for field, value in (("generation", 18), ("owner", "other_owner"), ("subject", "other_victim"), ("role", 2), ("disposition", 6), ("protection", 2)):
        w = World(src)
        w.hooks["after:" + CAPTURE] = lambda w, scope, f=field, v=value: w.setrow(f, v)
        def stale_before_revalidation(w):
            w.retire()
            expect("victim" in w.rosters["owner"], "stale frozen selection retired victim")
            expect(P + "named_removal_committed" not in w.flags[w.caller], "stale frozen selection committed")
            expect(not any(t.get("native") == "retire" for t in w.trace), "stale frozen selection reached native retirement")
            expect(w.row()["used"] == 0, "stale frozen selection consumed row")
            w.clean()
        yield "stale_before_revalidation_" + field, w, stale_before_revalidation

    # R039-RET-01: revalidation may publish the row's already-retired state.
    # That cached status must not authorize native work or rollback a row
    # consumed by another operation during ruling-character resolution.
    for tombstone in (False, True):
        for native_noop in (False, True):
            w = World(src)
            w.fail_native = native_noop
            def concurrent_consumption(w, scope, tombstone=tombstone):
                w.setrow("used", src.constants[P + "value.one"])
                if tombstone:
                    w.setrow("disposition", src.constants[P + "target_disposition.already_removed"])
                    w.setrow("protection", src.constants[P + "target_protection.hardened"])
                w.injected_row = w.row()
                w.injected_registry = copy.deepcopy(w.global_vars)
                # Also exercise freshness when a previous consumption receipt
                # is inherited by the current synchronous effect chain.
                w.flags[w.caller].add(P + "target_consumption_committed")
            w.hooks["native:remove_country_leader_trait"] = concurrent_consumption
            def already_consumed(w):
                rosters = copy.deepcopy(w.rosters)
                w.retire()
                expect(w.calls.get(MARK, 0) == 0, "already-consumed row reached mark helper")
                expect(w.global_vars == w.injected_registry,
                       f"another operation's consumption was rolled back: {w.injected_row} -> {w.row()}")
                expect(w.rosters == rosters, "already-consumed row permitted native roster removal")
                expect(not any(t.get("native") == "retire" for t in w.trace), "cached retired status permitted native retirement")
                expect(P + "selected_target_retired" in w.flags[w.caller], "scenario did not reproduce revalidation's cached retired status")
                expect(P + "target_consumption_committed" not in w.flags[w.caller], "stale consumption receipt survived the attempted transaction")
                expect(P + "named_removal_committed" not in w.flags[w.caller], "already-consumed row committed named removal")
                expect(P + "named_removal_failed" in w.flags[w.caller], "already-consumed row omitted failure receipt")
                expect(P + "named_removal_target_id" not in w.vars[w.caller]
                       and P + "named_removal_generation" not in w.vars[w.caller], "rejection published named-removal identity")
                w.clean()
            mode = "full_tombstone" if tombstone else "used_only"
            native = "native_noop" if native_noop else "native_removal"
            yield "R039-RET-01_" + mode + "_" + native + "_rejected", w, already_consumed

    # Between final validation and mark execution, leave public selection stale.
    # This intentionally tests the consume API's own exact-row checks.
    for field, value in (("generation", 18), ("owner", "other_owner"), ("subject", "other_victim"), ("role", 2), ("disposition", 6), ("protection", 2), ("used", 1)):
        w = World(src)
        def mutation(w, scope, f=field, v=value):
            w.setrow(f, v)
            w.injected_row = w.row()
        w.hooks["before:" + MARK] = mutation
        def stale_before_consumption(w):
            w.retire()
            expect("victim" in w.rosters["owner"], "stale registry at consumption retired victim")
            expect(P + "named_removal_committed" not in w.flags[w.caller], "stale registry at consumption committed")
            expect(not any(t.get("native") == "retire" for t in w.trace), "stale registry reached native retirement")
            expect(w.row() == w.injected_row, "consume API modified a stale row")
            w.clean()
        yield "stale_before_consumption_" + field, w, stale_before_consumption

    w = World(src)
    def duplicate_id(w, scope):
        selected_id = w.vars[w.caller][P + "selected_target_id"]
        second_before = w.row(1)
        w.setrow("id", selected_id, 1)
        expect(w.row(1) == dict(second_before, id=selected_id), "duplicate injection changed another payload field")
        expect(w.row()["generation"] != w.row(1)["generation"]
               and w.row()["owner"] != w.row(1)["owner"], "duplicate rows must retain distinct generation and owner")
        w.injected_registry = copy.deepcopy(w.global_vars)
    w.hooks["before:" + MARK] = duplicate_id
    def ambiguous_id(w):
        rosters = copy.deepcopy(w.rosters)
        w.retire()
        expect(w.calls.get(MARK, 0) == 1, "duplicate-ID case did not exercise actual consume API")
        expect(w.global_vars == w.injected_registry, "ambiguous ID consumed or changed a registry row")
        expect(w.row()["used"] == 0 and w.row(1)["used"] == 0, "ambiguous ID consumed a row")
        expect(w.rosters == rosters and not any(t.get("native") == "retire" for t in w.trace), "ambiguous ID reached native retirement")
        expect(P + "target_consumption_committed" not in w.flags[w.caller], "ambiguous ID published consumption receipt")
        expect(P + "selected_target_retired" not in w.flags[w.caller], "ambiguous ID published cached retired status")
        expect(P + "named_removal_committed" not in w.flags[w.caller]
               and P + "named_removal_failed" in w.flags[w.caller], "ambiguous ID published wrong outcome receipt")
        expect(P + "named_removal_target_id" not in w.vars[w.caller]
               and P + "named_removal_generation" not in w.vars[w.caller], "ambiguous ID published named-removal identity")
        w.clean()
    yield "duplicate_ID_before_MARK_rejected_without_mutation", w, ambiguous_id

    def overwrite(w, scope):
        for field, value in w.row(1).items():
            if field not in {"owner", "subject"}:
                w.vars[w.caller][P + "selected_target_" + field] = value
        w.vars[w.caller][P + "selected_target_expected_generation"] = 23
        w.global_targets[P + "selected_target_owner"] = "other_owner"
        w.global_targets[P + "selected_target_character"] = "other_victim"
    w = World(src)
    w.hooks["native:retire"] = overwrite
    yield "native_callback_overwrites_public_selection", w, success
    w = World(src)
    w.hooks["native:remove_country_leader_trait"] = overwrite
    yield "ruler_callback_overwrites_public_selection", w, success

    def recurse(w, scope):
        private_before = {k: v for k, v in w.vars[w.caller].items() if k.startswith(P + "removal_")}
        marks = w.calls.get(MARK, 0)
        w.invoke(RETIRE, w.caller)
        expect(w.calls.get(MARK, 0) == marks, "recursive entry reached consumption")
        expect(P + "named_removal_active" in w.global_flags, "recursive rejection released outer guard")
        private_after = {k: v for k, v in w.vars[w.caller].items() if k.startswith(P + "removal_")}
        expect(private_before == private_after, "recursive rejection destroyed outer private frame")
    for boundary in ("after:" + CAPTURE, "native:retire"):
        w = World(src)
        w.hooks[boundary] = recurse
        yield "recursive_entry_guard_" + boundary.split(":", 1)[0], w, success

    def caller_owned(w):
        w.temps[P + "target_registry_index"] = 83
        w.temps[P + "target_registry_match"] = 0
        w.retire()
        expect(w.temps[P + "target_registry_match"] == 1, "caller-owned temp output lost after nested calls")
        expect(set(w.temps) == {P + "target_registry_index", P + "target_registry_match"}, "unowned temp survived helper return")
        w.temps.clear()  # caller ends its own effect lifetime
        successful(w)
    yield "caller_owned_temp_storage_survives", World(src), caller_owned

    # Generic casualties consume an owner-country sentinel, not a character.
    # Execute actual validation and approval before the same consume API used
    # by named retirement. Do not seed its success flag or a character alias.
    for disposition in ("generic_office_only", "owner_managed"):
        for mismatch in (False, True):
            w = World(src, "owner")
            target_id = src.constants[P + "value.dynamic_target_base_id"] + 2
            w.setrow("id", target_id)
            w.vars[w.caller][P + "selected_target_id"] = target_id
            w.setrow("disposition", src.constants[P + "target_disposition." + disposition])
            w.setrow("role", src.constants[P + "target_role.cabinet"])
            w.setrow("subject", "owner")

            def generic(w, mismatch=mismatch):
                rosters = copy.deepcopy(w.rosters)
                w.invoke(P + "prepare_safe_target_action", w.caller)
                expect(w.invoke(P + "selected_target_allows_generic_office", w.caller), "generic caller did not validate")
                expect(not w.invoke(P + "selected_target_allows_named_action", w.caller), "generic row became eligible for named retirement")
                expect(w.target(P + "selected_target_character") is None, "generic row selected a character")
                if mismatch:
                    w.setrow("subject", "other_owner")
                    w.injected_row = w.row()
                    w.flags[w.caller].add(P + "target_consumption_committed")
                expected_registry = copy.deepcopy(w.global_vars)
                if not mismatch:
                    for field, key in (("disposition", "target_disposition.already_removed"),
                                       ("protection", "target_protection.hardened"), ("used", "value.one")):
                        expected_registry[P + "target_" + field + "_entries"][0] = src.constants[P + key]
                w.invoke(MARK, w.caller)
                expect(w.global_vars == expected_registry, "generic consumption changed the wrong fields or failed sentinel matching")
                expect((P + "selected_target_retired" in w.flags[w.caller]) == (not mismatch), "generic consumption receipt disagrees with sentinel match")
                expect((P + "target_consumption_committed" in w.flags[w.caller]) == (not mismatch), "generic fresh receipt disagrees with actual consumption")
                expect(w.rosters == rosters, "generic consumption changed a recruited roster")
                expect(not any(t.get("native") == "retire" for t in w.trace), "generic consumption reached native retirement")
                expect(w.calls.get(RETIRE, 0) == 0 and w.calls.get(CAPTURE, 0) == 0, "generic consumption entered named retirement or ruler resolution")
                expect(P + "named_removal_committed" not in w.flags[w.caller], "generic consumption published a named-removal receipt")
                expect(w.target(P + "selected_target_character") is None, "generic consumption created a character selection")
                w.clean()
            yield disposition + "_sentinel_" + ("mismatch_rejected" if mismatch else "success"), w, generic

    # Fixture self-checks ensure fail-closed AST dispatch is real, even in an
    # unreachable branch. They mutate only an in-memory parsed copy.
    def unsupported(w):
        bad = w.src.parse("if = { limit = { has_global_flag = impossible } unsupported_native = yes }")
        try:
            w.src.validate(bad.children())
        except Unsupported:
            return
        raise AssertionError("unsupported unreachable statement was ignored")
    yield "fixture_rejects_unsupported_unreachable_statement", World(src), unsupported


def main():
    src = Sources()
    results = []
    for name, world, run in cases(src):
        try:
            run(world)
            status, error = "pass", None
        except Exception as exc:
            status, error = "fail", f"{type(exc).__name__}: {exc}"
        result = {"case": name, "status": status, "error": error, "row": world.row(),
                  "registry_rows": [world.row(i) for i in range(len(world.global_vars[P + "target_id_entries"]))],
                  "injected_row": world.injected_row,
                  "selected_target_retired": P + "selected_target_retired" in world.flags[world.caller],
                  "target_consumption_committed": P + "target_consumption_committed" in world.flags[world.caller],
                  "caller_receipts": {k: v for k, v in world.vars[world.caller].items() if "named_removal" in k},
                  "rosters": world.rosters, "trace": world.trace,
                  "helper_call_counts": world.calls,
                  "temp_cleanup": world.temp_cleanup}
        results.append(result)
        print(f"{status.upper()} {name}" + (f": {error}" if error else ""), flush=True)
    stable = src.stable()
    report = {"evidence_type": "bounded actual-source mock execution, not engine evidence",
              "source_hashes": src.hashes, "helper_locations": src.locations,
              "stable_source_bytes_through_run": stable, "cases": results,
              "passed": sum(r["status"] == "pass" for r in results),
              "failed": sum(r["status"] == "fail" for r in results)}
    # Only generated validation evidence is written, below the authorized root.
    (HERE / "results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("passed", "failed", "stable_source_bytes_through_run", "source_hashes")}, indent=2))
    return 1 if report["failed"] or not stable else 0


if __name__ == "__main__":
    sys.exit(main())
