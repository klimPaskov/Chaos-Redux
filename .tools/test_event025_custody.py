"""Execute the six-slot alien custody helpers, not a HOI4 engine emulator.

Scope switches, meta substitution and bounded loops are evaluated from source.
Scheduling, UI, diplomacy effects and external rewards are outside this test.
"""
from pathlib import Path
import re
import unittest

from test_event025_final_recovery import Country, Runtime, block

ROOT = Path(__file__).resolve().parents[1]
LEDGER = (ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt").read_text(encoding="utf-8-sig")
TRIGGERS = (ROOT / "common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt").read_text(encoding="utf-8-sig")
PREFIX = "chaosx_alien_recovery_"


class CustodyRuntime(Runtime):
    def __init__(self, countries):
        super().__init__(countries)
        self.global_values = {}
        self.global_flags = set()
        self.temporary = {}
        self.targets = {}
        self.effects = {name: block(name, re.sub(r"#[^\n]*", "", LEDGER))
                        for name in re.findall(r"^(chaosx_alien_recovery_\w+)\s*=\s*\{", LEDGER, re.M)}
        self.triggers = {name: block(name, re.sub(r"#[^\n]*", "", TRIGGERS))
                         for name in re.findall(r"^(chaosx_alien_recovery_\w+)\s*=\s*\{", TRIGGERS, re.M)}
        self.prev = None
        self.root = None
        self.wars = set()

    def scoped(self, country, actor, operation, nodes):
        old = self.prev
        self.prev = actor
        try:
            return operation(nodes, country)
        finally:
            self.prev = old

    def scope(self, token, actor):
        if token == "THIS":
            return actor
        if token == "PREV":
            return self.prev
        if token == "ROOT":
            return self.root
        return self.targets.get(token.removeprefix("event_target:"))

    def value(self, token, actor):
        if token in ("THIS", "PREV", "ROOT") or token.startswith("event_target:"):
            country = self.scope(token, actor)
            return country.id if country else 0
        for namespace in ("THIS", "PREV", "ROOT"):
            if token.startswith(namespace + "."):
                country = self.scope(namespace, actor)
                return country.values.get(token.split(".", 1)[1], 0) if country else 0
        return super().value(token, actor)

    def flag(self, token, actor):
        return re.sub(r"@(PREV|ROOT|THIS)", lambda m: str(self.scope(m[1], actor).id), token)

    def expand(self, data, actor):
        args = dict(data)
        replacements = {}
        for key, value in data:
            if key == "text":
                continue
            match = re.fullmatch(r'"\[\?([\w.]+)\|\.0\]"', value)
            if not match:
                raise AssertionError(f"Unsupported meta argument: {value}")
            replacements[key] = str(int(self.value(match[1], actor)))

        def substitute(value):
            if isinstance(value, list):
                return [(substitute(k), substitute(v)) for k, v in value]
            for key, replacement in replacements.items():
                value = value.replace("[" + key + "]", replacement)
            return value
        return substitute(args["text"])

    def condition(self, nodes, actor):
        for key, data in nodes:
            if key == "NOT":
                result = not self.condition(data, actor)
            elif key == "OR":
                result = any(self.condition([item], actor) for item in data)
            elif key == "AND":
                result = self.condition(data, actor)
            elif key in self.triggers:
                result = self.condition(self.triggers[key], actor) == (data == "yes")
            elif key.startswith("event_target:"):
                target = self.scope(key, actor)
                result = bool(target and self.scoped(target, actor, self.condition, data))
            elif key == "meta_trigger":
                result = self.condition(self.expand(data, actor), actor)
            elif key == "tag":
                result = actor == self.scope(data, actor)
            elif key == "has_war_with":
                target = self.scope(data, actor)
                result = frozenset((actor.id, target.id)) in self.wars
            elif key == "has_variable":
                result = data in actor.values or data in self.temporary
            elif key == "has_country_flag":
                result = self.flag(data, actor) in actor.flags
            else:
                result = super().condition([(key, data)], actor)
            if not result:
                return False
        return True

    def run(self, name, actor):
        self.root = actor
        self.execute(self.effects[name], actor)

    def execute(self, nodes, actor):
        branch_taken = False
        for key, data in nodes:
            if key in ("if", "else_if", "else"):
                if key == "if":
                    branch_taken = False
                limit = next((v for k, v in data if k == "limit"), [])
                if (key == "if" or not branch_taken) and self.condition(limit, actor):
                    self.execute([(k, v) for k, v in data if k != "limit"], actor)
                    branch_taken = True
            elif key in self.effects:
                self.execute(self.effects[key], actor)
            elif key.startswith("event_target:"):
                target = self.scope(key, actor)
                if target:
                    self.scoped(target, actor, self.execute, data)
            elif key == "meta_effect":
                self.execute(self.expand(data, actor), actor)
            elif key == "for_loop_effect":
                args = dict(data)
                self.temporary[args["value"]] = self.value(args["start"], actor)
                body = [(k, v) for k, v in data if k not in ("start", "end", "compare", "value")]
                self.assert_bounded_loop(args, actor, body)
            elif key in ("save_event_target_as", "save_global_event_target_as"):
                self.targets[data] = actor
            elif key == "clear_global_event_target":
                self.targets.pop(data, None)
            elif key in ("set_country_flag", "clr_country_flag", "set_global_flag", "clr_global_flag"):
                target = self.global_flags if "global" in key else actor.flags
                name = self.flag(data, actor)
                (target.add if key.startswith("set_") else target.discard)(name)
            elif key in ("set_variable", "set_temp_variable", "add_to_variable", "add_to_temp_variable", "subtract_from_variable"):
                name, value = data[0]
                target = self.temporary if "temp" in key else actor.values
                if name.startswith("global."):
                    target, name = self.global_values, name[7:]
                amount = self.value(value, actor)
                if key == "subtract_from_variable":
                    target[name] = target.get(name, 0) - amount
                else:
                    target[name] = amount + (target.get(name, 0) if key.startswith("add_") else 0)
            elif key == "clear_variable":
                actor.values.pop(data, None)
            elif key == "clear_array":
                self.global_values[data.removeprefix("global.")] = []
            elif key == "add_to_array":
                args = dict(data)
                value = self.scope(args["value"], actor) if args["value"].startswith("event_target:") else self.value(args["value"], actor)
                self.global_values.setdefault(args["array"].removeprefix("global."), []).append(value)
            else:
                raise AssertionError(f"Unchecked custody effect: {key}")

    def assert_bounded_loop(self, args, actor, body):
        if args["compare"] != "less_than_or_equals":
            raise AssertionError("Unhandled loop comparison")
        steps = 0
        while self.temporary[args["value"]] <= self.value(args["end"], actor):
            self.execute(body, actor)
            self.temporary[args["value"]] += 1
            steps += 1
            if steps > 6:
                raise AssertionError("Custody exceeded the six-slot budget")


class CustodyTests(unittest.TestCase):
    def setUp(self):
        self.sender, self.recipient, self.other = (Country(n, flags=set()) for n in (1, 2, 3))
        self.runtime = CustodyRuntime([self.sender, self.recipient, self.other])
        self.runtime.targets[PREFIX + "event025_owner"] = self.sender
        self.runtime.global_flags.add(PREFIX + "event025_claimed")
        self.sender.flags.update((PREFIX + "event025_recorded", "learned_technology"))
        self.sender.values[PREFIX + "event025_result"] = 2
        self.runtime.run(PREFIX + "ledger_initialize_core_custody", self.sender)

    def acquire(self, country, slot, role=None):
        self.runtime.temporary.update({PREFIX + "fragment_id": slot, PREFIX + "fragment_role": slot if role is None else role})
        self.runtime.run(PREFIX + "ledger_assign_fragment", country)

    def consent(self, recipient=None):
        recipient = recipient or self.recipient
        self.runtime.targets[PREFIX + "custody_recipient"] = recipient
        self.sender.values[PREFIX + "custody_recipient_id"] = recipient.id
        recipient.flags.add(PREFIX + "custody_consent_1")

    def count(self, country):
        return country.values.get("chaosx_nr25_fragment_count", 0)

    def test_acquisition_is_exclusive_and_duplicate_safe(self):
        for slot in range(1, 7):
            self.acquire(self.sender, slot)
            self.acquire(self.sender, slot)
            self.assertEqual(self.runtime.temporary[PREFIX + "fragment_assigned"], 0)
            self.acquire(self.other, slot)
            self.assertIs(self.runtime.targets[PREFIX + f"fragment_owner_{slot}"], self.sender)
        self.assertEqual(self.count(self.sender), 6)
        self.assertEqual(self.count(self.other), 0)

    def test_transfer_preserves_recipient_fragments_roles_and_history(self):
        for slot in (1, 3, 5):
            self.acquire(self.sender, slot)
        self.acquire(self.recipient, 2)
        self.consent()
        self.runtime.run(PREFIX + "ledger_transfer_physical_custody", self.sender)
        self.assertEqual(self.runtime.temporary[PREFIX + "fragments_moved"], 3)
        self.assertEqual((self.count(self.sender), self.count(self.recipient)), (0, 4))
        self.assertIs(self.runtime.targets[PREFIX + "core_custodian"], self.recipient)
        self.assertIs(self.runtime.targets[PREFIX + "event025_owner"], self.sender)
        self.assertIn("learned_technology", self.sender.flags)
        self.assertEqual(self.sender.values[PREFIX + "event025_result"], 2)
        self.assertNotIn(PREFIX + "custody_consent_1", self.recipient.flags)
        self.assertEqual(self.runtime.global_values["chaosx_nr25_fragment_status"], [1, 2, 3, 0, 5, 0])

    def test_invalid_transfer_is_no_mutation_and_clears_selection(self):
        for reason in ("no_consent", "wrong_consent", "wrong_id", "subject", "capitulated", "annexed", "war", "self", "bad_role"):
            with self.subTest(reason=reason):
                self.setUp()
                self.acquire(self.sender, 1)
                self.consent(self.sender if reason == "self" else None)
                if reason == "no_consent": self.recipient.flags.clear()
                if reason == "wrong_consent": self.recipient.flags = {PREFIX + "custody_consent_3"}
                if reason == "wrong_id": self.sender.values[PREFIX + "custody_recipient_id"] = 3
                if reason == "subject": self.recipient.subject = True
                if reason == "capitulated": self.recipient.capitulated = True
                if reason == "annexed": self.recipient.exists = False
                if reason == "war": self.runtime.wars.add(frozenset((1, 2)))
                if reason == "bad_role": self.runtime.global_values[PREFIX + "fragment_1_role"] = 9
                self.runtime.run(PREFIX + "ledger_transfer_physical_custody", self.sender)
                self.assertEqual(self.runtime.temporary[PREFIX + "custody_applied"], 0)
                self.assertIs(self.runtime.targets[PREFIX + "core_custodian"], self.sender)
                self.assertIs(self.runtime.targets[PREFIX + "fragment_owner_1"], self.sender)
                self.assertNotIn(PREFIX + "custody_recipient_id", self.sender.values)

    def test_repeated_transfer_has_no_receipt(self):
        self.consent()
        self.runtime.run(PREFIX + "ledger_transfer_physical_custody", self.sender)
        self.consent()
        self.runtime.run(PREFIX + "ledger_transfer_physical_custody", self.sender)
        self.assertEqual(self.runtime.temporary[PREFIX + "custody_applied"], 0)

    def test_destruction_retires_only_owned_material_permanently(self):
        for slot in (1, 3, 6): self.acquire(self.sender, slot)
        self.acquire(self.other, 2)
        self.runtime.run(PREFIX + "ledger_destroy_physical_custody", self.sender)
        self.assertEqual(self.runtime.temporary[PREFIX + "fragments_moved"], 3)
        self.assertEqual(self.count(self.sender), 0)
        self.assertEqual(self.count(self.other), 1)
        self.assertIn(PREFIX + "core_destroyed", self.runtime.global_flags)
        self.assertIs(self.runtime.targets[PREFIX + "event025_owner"], self.sender)
        self.assertIn("learned_technology", self.sender.flags)
        self.runtime.run(PREFIX + "ledger_initialize_core_custody", self.sender)
        self.assertNotIn(PREFIX + "core_custodian", self.runtime.targets)
        for slot in (1, 3, 6):
            self.acquire(self.other, slot)
            self.assertEqual(self.runtime.temporary[PREFIX + "fragment_assigned"], 0)
        self.runtime.run(PREFIX + "ledger_destroy_physical_custody", self.sender)
        self.assertEqual(self.runtime.temporary[PREFIX + "custody_applied"], 0)

    def test_invalid_owner_cleanup_retains_reward_and_aligned_projection(self):
        self.acquire(self.sender, 1)
        self.acquire(self.other, 2)
        self.sender.exists = False
        self.runtime.run(PREFIX + "ledger_cleanup_invalid_targets", self.other)
        self.assertNotIn(PREFIX + "core_custodian", self.runtime.targets)
        self.assertIn(PREFIX + "core_abandoned", self.runtime.global_flags)
        self.assertIs(self.runtime.targets[PREFIX + "event025_owner"], self.sender)
        self.assertIn(PREFIX + "event025_claimed", self.runtime.global_flags)
        self.assertEqual(self.count(self.sender), 0)
        self.assertEqual(self.runtime.global_values["chaosx_nr25_fragment_status"], [0, 2, 0, 0, 0, 0])
        self.acquire(self.recipient, 1)
        self.assertEqual(self.count(self.recipient), 1)

    def test_invalid_fragment_inputs_cannot_allocate(self):
        for slot, role in ((0, 1), (7, 1), (1.5, 1), (1, 0), (1, 7), (1, 2.5)):
            with self.subTest(slot=slot, role=role):
                self.acquire(self.sender, slot, role)
                self.assertEqual(self.runtime.temporary[PREFIX + "fragment_assigned"], 0)

    def test_acquisition_callers_do_not_double_count(self):
        source = (ROOT / "common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt").read_text(encoding="utf-8-sig")
        self.assertNotRegex(source, r"add_to_variable\s*=\s*\{\s*chaosx_nr25_fragment_count\s*=")


if __name__ == "__main__":
    unittest.main()
