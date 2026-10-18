"""Actual-source graphics receipt checks, not native rendering or save proof.

Native graphical creation/destruction are declared opaque primitives, not
simulated engine outcomes. Temporary helper frames are conservatively discarded.
"""
import re
import subprocess
from pathlib import Path

from validate_028_availability import parse_source

ROOT = Path(__file__).resolve().parents[2]
BASELINE_COMMIT = "e9cd71fcddfc10310ed2112eef00610ed205e357"
PRESENTATION = ROOT / "common/scripted_effects/028_asteroid_incoming_map_visual_effects.txt"
DEFS = parse_source(PRESENTATION)
CONSTANTS = parse_source(ROOT / "common/script_constants/028_asteroid_incoming_constants.txt")
CONSTANTS.update(parse_source(ROOT / "common/script_constants/028_asteroid_incoming_visual_constants.txt"))


def terms(rows):
    return {key: value for key, _, value in rows}


class TextSource:
    def __init__(self, text):
        self.text = text

    def read_text(self, encoding):
        return self.text


anchor_text = (ROOT / "common/scripted_effects/fallout_consolidated_effects.txt").read_text(encoding="utf-8-sig")
start = re.search(r"(?m)^air_winter_visual_seed_anchor_provinces\s*=\s*\{", anchor_text)
assert start
depth = 1
for end in range(start.end(), len(anchor_text)):
    depth += (anchor_text[end] == "{") - (anchor_text[end] == "}")
    if depth == 0:
        break
else:
    raise AssertionError("Unclosed anchor definition")
anchors = parse_source(TextSource(anchor_text[start.start():end + 1]))["air_winter_visual_seed_anchor_provinces"]
ANCHOR_IDS = {int(key): int(rows[0][2][0][2]) for key, _, rows in anchors}


class Model:
    def __init__(self, impact=True, anchor=True):
        self.global_flags = {"asteroid_incoming_impact_recorded"} if impact else set()
        self.global_values = {"global.num_days": 100, "global.asteroid_incoming_transaction_id": 9}
        self.states = {}
        self.arrays = {}
        self.temp = {}
        self.created = []
        self.destroyed = []
        self.anchor = anchor

    def state(self, sid, main=True, applied=True):
        flags = {"asteroid_incoming_main_crater" if main else "asteroid_incoming_fragment_site"}
        if applied:
            flags.add("asteroid_incoming_state_transaction_applied")
        self.states[sid] = {"flags": flags, "values": {}}
        return sid

    def value(self, token, sid):
        if token == "THIS":
            return sid
        if token == "THIS.id":
            raise AssertionError("Typed scope reference must not be modeled as a numeric state ID")
        if token.startswith("constant:"):
            category, key = token[9:].split(".")
            return float(terms(CONSTANTS[category])[key])
        if token.startswith("global."):
            return self.global_values.get(token, 0)
        if token in self.temp:
            return self.temp[token]
        try:
            return float(token)
        except ValueError:
            assert sid is not None, (token, sid)
            return self.states[sid]["values"].get(token, 0)

    def trigger_node(self, key, op, val, sid):
        if key == "AND":
            return self.trigger(val, sid)
        if key == "OR":
            return any(self.trigger_node(*row, sid) for row in val)
        if key == "NOT":
            return not any(self.trigger_node(*row, sid) for row in val)
        if key == "has_global_flag":
            return val in self.global_flags
        if key == "has_state_flag":
            return val in self.states[sid]["flags"]
        if key == "has_variable":
            return val in self.states[sid]["values"]
        if key == "check_variable":
            fields = terms(val)
            left, right = self.value(fields["var"], sid), self.value(fields["value"], sid)
            return {"equals": left == right, "greater_than_or_equals": left >= right}[fields["compare"]]
        if key == "is_in_array":
            fields = terms(val)
            return self.value(fields["value"], sid) in self.arrays.get(fields["array"], [])
        if key == "any_of_scopes":
            fields = terms(val)
            body = [row for row in val if row[0] != "array"]
            return any(self.trigger(body, member) for member in self.arrays.get(fields["array"], []))
        raise AssertionError(("unmodelled trigger", key, op, val))

    def trigger(self, rows, sid):
        return all(self.trigger_node(*row, sid) for row in rows)

    def call(self, name, sid=None):
        existing = set(self.temp)
        self.execute(DEFS[name], sid)
        self.temp = {key: value for key, value in self.temp.items() if key in existing}

    def execute(self, rows, sid):
        branch = None
        for key, _, val in rows:
            if key == "if":
                branch = self.trigger(terms(val)["limit"], sid)
                if branch:
                    self.execute([row for row in val if row[0] != "limit"], sid)
            elif key == "else":
                assert branch is not None
                if not branch:
                    self.execute(val, sid)
                branch = None
            elif key in DEFS:
                self.call(key, sid)
            elif key == "air_winter_visual_seed_anchor_provinces":
                if self.anchor:
                    for state_id, member in self.states.items():
                        member["values"]["air_winter_visual_anchor_province"] = ANCHOR_IDS[state_id]
            elif key == "set_temp_variable":
                name, _, value = val[0]
                self.temp[name] = self.value(value, sid)
            elif key in ("set_variable", "add_to_variable"):
                name, _, value = val[0]
                storage = self.global_values if name.startswith("global.") else self.states[sid]["values"]
                storage[name] = self.value(value, sid) + (storage.get(name, 0) if key == "add_to_variable" else 0)
            elif key == "clear_variable":
                self.states[sid]["values"].pop(val, None)
            elif key in ("set_state_flag", "clr_state_flag", "set_global_flag", "clr_global_flag"):
                flags = self.global_flags if "global" in key else self.states[sid]["flags"]
                flags.add(val) if key.startswith("set_") else flags.discard(val)
            elif key == "add_to_array":
                fields = terms(val)
                self.arrays.setdefault(fields["array"], []).append(self.value(fields["value"], sid))
            elif key == "clear_array":
                self.arrays[val] = []
            elif key == "for_each_scope_loop":
                fields = terms(val)
                for member in list(self.arrays.get(fields["array"], [])):
                    self.execute([row for row in val if row[0] != "array"], member)
            elif key == "meta_effect":
                fields = terms(val)
                replacements = {}
                for name, expression in fields.items():
                    if name != "text":
                        match = re.fullmatch(r'"\[\?([^|]+)\|\.0\]"', expression)
                        assert match, expression
                        replacements[name] = str(int(self.value(match[1], sid)))

                def expand(value):
                    if isinstance(value, list):
                        return [(name, op, expand(item)) for name, op, item in value]
                    for name, replacement in replacements.items():
                        value = value.replace("[" + name + "]", replacement)
                    return value

                self.execute(expand(fields["text"]), sid)
            elif key == "create_entity":
                fields = terms(val)
                self.created.append((sid, fields["entity"], int(fields["province"]), int(fields["id"])))
            elif key == "destroy_entity":
                self.destroyed.append(int(val))
            else:
                raise AssertionError(("unmodelled effect", key, val))


checks = []
for main in (True, False):
    entry = "asteroid_incoming_emit_main_visual" if main else "asteroid_incoming_emit_fragment_visual"
    for impact, applied, anchor in ((True, True, True), (False, True, True),
                                   (True, False, True), (True, True, False)):
        model = Model(impact, anchor)
        sid = model.state(64, main, applied)
        model.call(entry, sid)
        expected = impact and applied and anchor
        assert len(model.created) == int(expected)
        assert ("asteroid_incoming_visual_emitted" in model.states[sid]["flags"]) == expected
        assert model.temp == {}, "Helper-local temporaries leaked"
        if expected:
            assert model.created[0][3] == 15000 + ANCHOR_IDS[sid]
            model.call(entry, sid)
            assert len(model.created) == 1, "Duplicate emission"
        checks.append((main, impact, applied, anchor))

model = Model()
for sid in range(1, 8):
    model.state(sid, main=sid == 1)
for sid in range(1, 8):
    model.call("asteroid_incoming_emit_main_visual" if sid == 1 else "asteroid_incoming_emit_fragment_visual", sid)
assert len(model.created) == 7
assert len({row[3] for row in model.created}) == 7, "Distinct real anchors shared a visual ID"
for day, expected in ((129, 0), (130, 7), (160, 7)):
    model.global_values["global.num_days"] = day
    model.call("asteroid_incoming_cleanup_expired_visuals")
    assert len(model.destroyed) == expected
assert len(set(model.destroyed)) == 7
assert model.arrays["global.asteroid_incoming_visual_sites"] == []
assert "asteroid_incoming_visual_cleanup_active" not in model.global_flags
for state in model.states.values():
    assert "asteroid_incoming_visual_emitted" in state["flags"]
    assert "asteroid_incoming_visual_cleanup_pending" not in state["flags"]
    assert "asteroid_incoming_visual_entity_id" not in state["values"]
    assert "asteroid_incoming_visual_cleanup_day" not in state["values"]
model.call("asteroid_incoming_emit_main_visual", 1)
assert len(model.created) == 7, "Cleanup reopened a delivered visual"

empty = Model(impact=False)
empty.call("asteroid_incoming_cleanup_expired_visuals")
assert not empty.created and not empty.destroyed and not empty.arrays

# Graphics-only orchestration has no ledger/damage calls, including its one
# borrowed helper. Map-anchor seeding consists exclusively of coordinate writes.
for _, _, rows in anchors:
    assert rows[0][0] == "set_variable" and len(rows) == 1
    assert rows[0][2][0][0] == "air_winter_visual_anchor_province"
runtime = ROOT / "common/scripted_effects/028_asteroid_incoming_runtime_effects.txt"
assert "launch_nuke" not in runtime.read_text(encoding="utf-8-sig")
assert "asteroid_incoming_visual_strike_state" not in runtime.read_text(encoding="utf-8-sig")
old = subprocess.check_output(["git", "show", BASELINE_COMMIT + ":" + str(runtime.relative_to(ROOT)).replace("\\", "/")], cwd=ROOT).decode("utf-8-sig")
before, after = parse_source(TextSource(old)), parse_source(runtime)
changed = {key for key in before.keys() | after.keys() if before.get(key) != after.get(key)}
assert changed == {"asteroid_incoming_mark_visual_strike_state", "asteroid_incoming_play_fragment_visual",
                   "asteroid_incoming_apply_state_profile", "asteroid_incoming_update_achievements",
                   # bc12ee47e4 guards the national dust-protection removal with
                   # has_dynamic_modifier; no gameplay change.
                   "asteroid_incoming_refresh_national_dust_protection"}, changed
news_path = "common/scripted_effects/028_asteroid_incoming_presentation_effects.txt"
news_before = subprocess.check_output(["git", "show", BASELINE_COMMIT + ":" + news_path], cwd=ROOT).decode("utf-8-sig")
assert parse_source(TextSource(news_before)) == parse_source(ROOT / news_path), "Existing news-delivery module changed"
print(f"{len(checks)} emission/receipt cases, seven-site retirement boundaries, duplicate/empty-host cases passed.")
print(f"Borrowed anchor helper has {len(anchors)} coordinate-only rows. Native rendering, handle persistence and engine side effects remain UNVERIFIED.")
