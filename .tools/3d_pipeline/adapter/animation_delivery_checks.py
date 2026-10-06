"""Read-only .anim delivery gates and lossless quaternion sign cleanup.

The inspection path consumes the decoded XML-like tree returned by the locked
io_pdx_mesh parser. The F-curve helper changes only signs of existing
quaternion keys and their Bézier handles; it never creates or removes keys.
"""
from __future__ import annotations

import ast
import math
from collections import defaultdict


PDX_TO_BLENDER_AXES = {"x": "x", "y": "z", "z": "y"}
PDX_HORIZONTAL_AXES = ("x", "z")
PDX_VERTICAL_AXIS = "y"
PDX_FORWARD_AXIS = "-z"


def _as_sequence(value, label):
    if isinstance(value, (list, tuple)):
        return list(value)
    if isinstance(value, str):
        try:
            decoded = ast.literal_eval(value)
        except (ValueError, SyntaxError) as exc:
            raise ValueError(f"{label} is not a decoded PDX array.") from exc
        if isinstance(decoded, (list, tuple)):
            return list(decoded)
        if isinstance(decoded, (int, float)) and not isinstance(decoded, bool):
            return [decoded]
    raise ValueError(f"{label} is not a decoded PDX array.")


def _number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label} must contain finite numeric values.")
    return float(value)


def _vector(value, size, label):
    row = _as_sequence(value, label)
    if len(row) != size:
        raise ValueError(f"{label} must contain exactly {size} values.")
    return tuple(_number(item, label) for item in row)


def _scalar(value, label):
    row = _as_sequence(value, label)
    if len(row) != 1:
        raise ValueError(f"{label} must contain one value.")
    return _number(row[0], label)


def _unit_quaternion(value, label):
    q = _vector(value, 4, label)
    length = math.sqrt(sum(item * item for item in q))
    if length <= 1e-12:
        raise ValueError(f"{label} is a zero quaternion.")
    return tuple(item / length for item in q), abs(length - 1.0) > 1e-5


def _quaternion_angle_degrees(left, right):
    q1, _ = _unit_quaternion(left, "left quaternion")
    q2, _ = _unit_quaternion(right, "right quaternion")
    dot = min(1.0, max(-1.0, abs(sum(a * b for a, b in zip(q1, q2)))))
    return math.degrees(2.0 * math.acos(dot))


def _distance(left, right):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def _child(node, tag):
    found = [child for child in node if child.tag == tag]
    if len(found) != 1:
        raise ValueError(f"Decoded animation requires one {tag!r} block.")
    return found[0]


def _channel_names(value, bone_name):
    if isinstance(value, str):
        raw = value
        try:
            decoded = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            decoded = None
        if isinstance(decoded, (list, tuple)) and len(decoded) == 1 and isinstance(decoded[0], str):
            raw = decoded[0]
    else:
        entries = _as_sequence(value, f"{bone_name}.sa")
        if len(entries) != 1 or not isinstance(entries[0], str):
            raise ValueError(f"{bone_name}.sa must identify one transform-channel string.")
        raw = entries[0]
    if any(channel not in "tqs" for channel in raw) or len(set(raw)) != len(raw):
        raise ValueError(f"{bone_name}.sa contains unknown or duplicate transform channels.")
    return frozenset(raw)


def decode_animation_tree(tree):
    """Decode PDX ``info`` and flattened ``samples`` channels without mutation."""
    if getattr(tree, "tag", None) != "File":
        raise ValueError("Animation delivery requires an io_pdx_mesh File tree.")
    info, samples = _child(tree, "info"), _child(tree, "samples")
    fps = _scalar(info.get("fps"), "info.fps")
    frame_count_float = _scalar(info.get("sa"), "info.sa")
    joint_count_float = _scalar(info.get("j"), "info.j")
    if fps <= 0 or not frame_count_float.is_integer() or not joint_count_float.is_integer():
        raise ValueError("Animation FPS, frame count, and joint count must be positive whole values.")
    frame_count, joint_count = int(frame_count_float), int(joint_count_float)
    if frame_count < 2 or joint_count < 1 or len(info) != joint_count:
        raise ValueError("Animation info frame or joint counts do not match the decoded tree.")

    bones = []
    for child in info:
        name = str(child.tag)
        channels = _channel_names(child.get("sa"), name)
        initial_t = _vector(child.get("t"), 3, f"{name}.t")
        initial_q, nonunit = _unit_quaternion(child.get("q"), f"{name}.q")
        initial_s = _as_sequence(child.get("s"), f"{name}.s")
        if len(initial_s) not in (1, 3):
            raise ValueError(f"{name}.s must contain one or three scale values.")
        initial_s = tuple(_number(value, f"{name}.s") for value in initial_s)
        bones.append({"name": name, "channels": channels, "initial_t": initial_t, "initial_q": initial_q,
                      "initial_s": initial_s, "initial_q_nonunit": nonunit})

    scale_lengths = {len(bone["initial_s"]) for bone in bones}
    if len(scale_lengths) != 1:
        raise ValueError("Decoded animation uses mixed scale-vector lengths unsupported by io_pdx_mesh.")
    sample_values = {}
    for channel, width in (("t", 3), ("q", 4), ("s", next(iter(scale_lengths)))):
        count = frame_count * sum(width if channel in bone["channels"] else 0 for bone in bones)
        raw = samples.get(channel)
        values = [] if raw is None else [_number(value, f"samples.{channel}") for value in _as_sequence(raw, f"samples.{channel}")]
        if len(values) != count:
            raise ValueError(f"samples.{channel} has {len(values)} values; decoded info requires {count}.")
        sample_values[channel] = values

    offsets = {channel: 0 for channel in "tqs"}
    widths = {"t": 3, "q": 4, "s": next(iter(scale_lengths))}
    frames = []
    nonunit_sample_count = 0
    for _frame_index in range(frame_count):
        frame = {}
        for bone in bones:
            pose = {"t": bone["initial_t"], "q": bone["initial_q"], "s": bone["initial_s"]}
            for channel in "tqs":
                if channel not in bone["channels"]:
                    continue
                width = widths[channel]
                start = offsets[channel]
                values = sample_values[channel][start:start + width]
                offsets[channel] += width
                if channel == "q":
                    pose[channel], nonunit = _unit_quaternion(values, f"samples.q.{bone['name']}")
                    nonunit_sample_count += int(nonunit)
                else:
                    pose[channel] = tuple(values)
            frame[bone["name"]] = pose
        frames.append(frame)

    if any(offsets[channel] != len(sample_values[channel]) for channel in "tqs"):
        raise ValueError("Flattened animation sample channels did not decode to their declared frame count.")
    return {"fps": fps, "frame_count": frame_count, "joint_count": joint_count, "bones": bones,
            "frames": frames, "nonunit_initial_quaternions": sum(int(b["initial_q_nonunit"]) for b in bones),
            "nonunit_sample_quaternions": nonunit_sample_count}


def _validate_windows(strike_windows, frame_start, frame_end):
    windows = []
    for row in strike_windows:
        if isinstance(row, dict):
            start, end = row.get("start_frame"), row.get("end_frame")
        else:
            try:
                start, end = row
            except (TypeError, ValueError) as exc:
                raise ValueError("Strike windows must be [start_frame, end_frame] pairs.") from exc
        if type(start) is not int or type(end) is not int or start > end or start < frame_start or end > frame_end:
            raise ValueError("Strike windows must be bounded whole frames inside the action range.")
        windows.append((start, end))
    return tuple(windows)


def _inside_window(frame, windows):
    return any(start <= frame <= end for start, end in windows)


def _local_peak_indices(values):
    if len(values) < 2:
        return set()
    peaks = set()
    for index, value in enumerate(values):
        if value <= 0:
            continue
        left = values[index - 1] if index else -math.inf
        right = values[index + 1] if index + 1 < len(values) else -math.inf
        if value >= left and value >= right and (value > left or value > right):
            peaks.add(index)
    return peaks


def decode_skeleton_hierarchy(tree):
    """Read one consistent PDX ``skeleton`` hierarchy from a decoded mesh tree."""
    if getattr(tree, "tag", None) == "skeleton":
        skeleton_nodes = [tree]
    else:
        skeleton_nodes = [node for node in tree.iter() if node.tag == "skeleton"]
    if not skeleton_nodes:
        raise ValueError("Matching PDX mesh tree has no decoded skeleton hierarchy.")
    signatures, decoded_rows = [], []
    for skeleton in skeleton_nodes:
        rows = []
        for bone in skeleton:
            index = int(_scalar(bone.get("ix"), f"skeleton.{bone.tag}.ix"))
            parent_raw = bone.get("pa")
            parent = None if parent_raw is None else int(_scalar(parent_raw, f"skeleton.{bone.tag}.pa"))
            transform = _vector(bone.get("tx"), 12, f"skeleton.{bone.tag}.tx")
            rows.append({"name": str(bone.tag), "index": index, "parent_index": parent, "tx": transform})
        rows.sort(key=lambda row: row["index"])
        if not rows or len({row["index"] for row in rows}) != len(rows) or len({row["name"] for row in rows}) != len(rows):
            raise ValueError("PDX skeleton indices and names must be nonempty and unique.")
        index_set = {row["index"] for row in rows}
        if any(row["parent_index"] is not None and row["parent_index"] not in index_set for row in rows):
            raise ValueError("PDX skeleton parent index is missing from its hierarchy.")
        roots = [row for row in rows if row["parent_index"] is None]
        if len(roots) != 1:
            raise ValueError("PDX skeleton must have exactly one parentless root for FK measurement.")
        by_index = {row["index"]: row for row in rows}
        pending, ordered = set(index_set), []
        while pending:
            ready = sorted(index for index in pending if by_index[index]["parent_index"] is None or by_index[index]["parent_index"] not in pending)
            if not ready:
                raise ValueError("PDX skeleton parent links contain a cycle.")
            ordered.extend(by_index[index] for index in ready)
            pending.difference_update(ready)
        signature = tuple((row["name"], row["index"], row["parent_index"], row["tx"]) for row in ordered)
        signatures.append(signature)
        decoded_rows.append(ordered)
    if any(signature != signatures[0] for signature in signatures[1:]):
        raise ValueError("Matching PDX mesh streams contain different skeleton hierarchies.")
    return {"bones": decoded_rows[0], "root_bone": next(row["name"] for row in decoded_rows[0] if row["parent_index"] is None),
            "skeleton_stream_count": len(skeleton_nodes), "tx_policy": "validated as decoded inverse-rest transforms but not used to invent animated poses"}


def _quat_multiply(left, right):
    x1, y1, z1, w1 = left
    x2, y2, z2, w2 = right
    result = (w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
              w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
              w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
              w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2)
    return _unit_quaternion(result, "composed world quaternion")[0]


def _rotate_vector(vector, quaternion):
    x, y, z, w = quaternion
    vx, vy, vz = vector
    dot_uv = x * vx + y * vy + z * vz
    dot_uu = x * x + y * y + z * z
    cross = (y * vz - z * vy, z * vx - x * vz, x * vy - y * vx)
    return tuple(2.0 * dot_uv * axis + (w * w - dot_uu) * value + 2.0 * w * cross[index]
                 for index, (axis, value) in enumerate(zip((x, y, z), (vx, vy, vz))))


def _scale3(values):
    if len(values) == 1:
        return (values[0], values[0], values[0])
    return tuple(values)


def _world_motion_report(decoded, skeleton_tree, frame_start, fps, strike_windows,
                         angular_limit, translation_limit, entity_scale):
    if skeleton_tree is None:
        return {"status": "unmeasured", "reason": "matching decoded PDX mesh skeleton was not supplied",
                "world_motion_peak_table": [], "violations": [], "measurement_space": "unresolved"}
    try:
        hierarchy = decode_skeleton_hierarchy(skeleton_tree)
    except ValueError as exc:
        return {"status": "unmeasured", "reason": str(exc), "world_motion_peak_table": [],
                "violations": [], "measurement_space": "unresolved"}
    animation_names = {bone["name"] for bone in decoded["bones"]}
    skeleton_names = {bone["name"] for bone in hierarchy["bones"]}
    if animation_names != skeleton_names:
        return {"status": "unmeasured", "reason": "animation and matching mesh skeleton bone-name sets differ",
                "animation_only_bones": sorted(animation_names - skeleton_names),
                "skeleton_only_bones": sorted(skeleton_names - animation_names),
                "world_motion_peak_table": [], "violations": [], "measurement_space": "unresolved"}

    scale_factor = 1.0 if entity_scale is None else _number(entity_scale, "entity_scale")
    if scale_factor <= 0:
        raise ValueError("entity_scale must be positive when supplied.")
    skeleton_by_index = {bone["index"]: bone for bone in hierarchy["bones"]}
    world_frames = []
    for local_frame in decoded["frames"]:
        world_frame = {}
        for bone in hierarchy["bones"]:
            local = local_frame[bone["name"]]
            local_translation = local["t"]
            local_rotation = local["q"]
            local_scale = _scale3(local["s"])
            if bone["parent_index"] is None:
                world_translation = tuple(value * scale_factor for value in local_translation)
                world_rotation = local_rotation
                world_scale = local_scale
            else:
                parent = skeleton_by_index[bone["parent_index"]]
                parent_world = world_frame[parent["name"]]
                scaled_local = tuple(parent_world["scale"][axis] * local_translation[axis] for axis in range(3))
                rotated = _rotate_vector(scaled_local, parent_world["rotation"])
                world_translation = tuple(parent_world["translation"][axis] + rotated[axis] * scale_factor for axis in range(3))
                world_rotation = _quat_multiply(parent_world["rotation"], local_rotation)
                world_scale = tuple(parent_world["scale"][axis] * local_scale[axis] for axis in range(3))
            world_frame[bone["name"]] = {"translation": world_translation, "rotation": world_rotation, "scale": world_scale}
        world_frames.append(world_frame)

    transitions_by_bone = defaultdict(list)
    violations = []
    for bone in hierarchy["bones"]:
        name = bone["name"]
        for index in range(len(world_frames) - 1):
            left, right = world_frames[index][name], world_frames[index + 1][name]
            frame = frame_start + index + 1
            angle = _quaternion_angle_degrees(left["rotation"], right["rotation"])
            step = _distance(left["translation"], right["translation"])
            row = {"frame": frame, "bone": name, "angular_deg": angle,
                   "translation_step": step, "time_seconds": (frame - frame_start) / fps}
            transitions_by_bone[name].append(row)
            if not _inside_window(frame, strike_windows):
                if angle > angular_limit:
                    violations.append({**row, "kind": "world_joint_rotation_exceeds_limit", "limit": angular_limit})
                if step > translation_limit:
                    violations.append({**row, "kind": "world_joint_translation_exceeds_limit", "limit": translation_limit})

    peak_table = []
    for name, rows in transitions_by_bone.items():
        angles = [row["angular_deg"] for row in rows]
        steps = [row["translation_step"] for row in rows]
        angular_peaks, translation_peaks = _local_peak_indices(angles), _local_peak_indices(steps)
        for index in sorted(angular_peaks | translation_peaks):
            row = dict(rows[index])
            row["peak_dimensions"] = (["angular"] if index in angular_peaks else []) + (["translation"] if index in translation_peaks else [])
            peak_table.append(row)
    peak_table.sort(key=lambda row: (row["frame"], row["bone"]))
    return {"status": "blocked" if violations else "pass", "skeleton_root_bone": hierarchy["root_bone"],
            "skeleton_stream_count": hierarchy["skeleton_stream_count"], "bone_count": len(hierarchy["bones"]),
            "measurement_space": "PDX Y-up local TRS composed through decoded mesh parent indices",
            "entity_scale_applied_for_measurement": entity_scale,
            "joint_speed_limit_units_per_frame_exclusive": translation_limit,
            "angular_limit_degrees_exclusive": angular_limit, "violations": violations,
            "world_motion_peak_table": peak_table,
            "joint_head_position_basis": "animated per-bone .anim local t/q/s samples and the matching .mesh skeleton pa/ix hierarchy; validated inverse-rest tx is not used to invent pose transforms"}


def _root_report(decoded, root_bone, role, root_policy, frame_start, drift_ceiling, entity_scale):
    names = [bone["name"] for bone in decoded["bones"]]
    resolved_bone = root_bone if root_bone is not None else (names[0] if names else None)
    resolution = "explicit_input" if root_bone is not None else "first_serialized_info_bone"
    if resolved_bone not in names:
        return {"status": "unmeasured", "reason": "explicit_root_bone_not_in_animation", "root_bone": root_bone,
                "pdx_to_blender_axis_mapping": PDX_TO_BLENDER_AXES}
    # io_pdx_mesh serializes the rig hierarchy from its root bone downward.
    # An explicit parent value takes precedence; a missing value remains visible as inferred evidence.
    poses = [frame[resolved_bone]["t"] for frame in decoded["frames"]]
    origin = poses[0]
    scale = 1.0 if entity_scale is None else _number(entity_scale, "entity_scale")
    if scale <= 0:
        raise ValueError("entity_scale must be positive when supplied.")
    horizontal_offsets = [(pos[0] - origin[0], pos[2] - origin[2]) for pos in poses]
    max_planar = max(math.hypot(x, z) for x, z in horizontal_offsets) * scale
    x_range = (max(pos[0] for pos in poses) - min(pos[0] for pos in poses)) * scale
    z_range = (max(pos[2] for pos in poses) - min(pos[2] for pos in poses)) * scale
    y_range = (max(pos[1] for pos in poses) - min(pos[1] for pos in poses)) * scale
    forward_max = max(abs(pos[2] - origin[2]) for pos in poses) * scale
    death_role = role.casefold() in {"death", "destruction"}
    if death_role:
        measured = forward_max
        limit = drift_ceiling
        rule = "absolute PDX -Z forward travel from first sample"
    elif root_policy == "in_place_xy_preserve_z":
        measured = max_planar
        limit = drift_ceiling
        rule = "PDX X/Z planar travel from first sample; PDX Y is vertical and preserved"
    else:
        measured, limit, rule = max_planar, None, "root-motion policy declared outside this gate"
    if limit is None or measured is None:
        status = "unmeasured"
    else:
        status = "pass" if measured <= limit else "blocked"
    if root_bone is None and status == "pass":
        status = "needs_review"
    return {"status": status, "root_bone": resolved_bone, "root_resolution": resolution,
            "root_resolution_note": "PDX info order follows the locked io_pdx_mesh root-first skeleton hierarchy; verify against the owning mesh skeleton when the source was not produced by that exporter.",
            "root_policy": root_policy, "policy_rule": rule, "drift_ceiling_units": limit,
            "measurement_units": "runtime_units" if entity_scale is not None else "pdx_model_units",
            "entity_scale_applied_for_measurement": entity_scale,
            "max_planar_xz_from_first": max_planar, "x_range": x_range, "z_range": z_range,
            "vertical_y_range_preserved": y_range, "death_forward_abs_z_from_first": forward_max,
            "pdx_to_blender_axis_mapping": PDX_TO_BLENDER_AXES,
            "pdx_horizontal_axes": list(PDX_HORIZONTAL_AXES), "pdx_vertical_axis": PDX_VERTICAL_AXIS,
            "pdx_forward_axis": PDX_FORWARD_AXIS, "frame_start": frame_start}


def _foot_contact_report(measurements, frame_count, fps, frame_start, looped, humanoid_move):
    if measurements is None:
        return {"status": "unmeasured", "reason": "no measured Blender world-foot coordinates supplied",
                "plant_counts": None, "plants": [], "suggested_event_times_seconds": [], "uncertainty_flagged": True}
    required = {"feet", "ground_plane", "contact_tolerance", "stationary_tolerance", "measurement_uncertainty", "min_contact_frames"}
    if set(measurements) != required:
        return {"status": "unmeasured", "reason": "foot measurements lack required ground or uncertainty metadata",
                "plant_counts": None, "plants": [], "suggested_event_times_seconds": [], "uncertainty_flagged": True}
    feet = measurements["feet"]
    if set(feet) != {"left", "right"}:
        raise ValueError("Foot evidence must identify exactly left and right feet.")
    plane = measurements["ground_plane"]
    normal = _vector(plane.get("normal"), 3, "ground_plane.normal")
    norm = math.sqrt(sum(v * v for v in normal))
    if norm <= 1e-12:
        raise ValueError("Ground-plane normal cannot be zero.")
    normal = tuple(v / norm for v in normal)
    offset = _number(plane.get("offset"), "ground_plane.offset")
    contact_tolerance = _number(measurements["contact_tolerance"], "contact_tolerance")
    stationary_tolerance = _number(measurements["stationary_tolerance"], "stationary_tolerance")
    uncertainty = _number(measurements["measurement_uncertainty"], "measurement_uncertainty")
    min_frames = measurements["min_contact_frames"]
    if min(contact_tolerance, stationary_tolerance, uncertainty) < 0 or type(min_frames) is not int or min_frames < 1:
        raise ValueError("Foot thresholds must be nonnegative and min_contact_frames must be positive.")

    plants = []
    uncertain_any = False
    counts = {}
    for side, row in feet.items():
        positions = row.get("world_positions")
        if not isinstance(positions, (list, tuple)) or len(positions) != frame_count:
            raise ValueError(f"{side} foot needs one measured world position per decoded animation sample.")
        points = [_vector(point, 3, f"{side}.world_positions") for point in positions]
        distances = [sum(n * p for n, p in zip(normal, point)) - offset for point in points]
        tangent_steps, step_errors = [], []
        for index in range(frame_count):
            neighbor = index + 1 if index + 1 < frame_count else (0 if looped else index - 1)
            if neighbor < 0 or neighbor == index:
                tangent_steps.append(0.0)
                step_errors.append(2.0 * uncertainty)
                continue
            delta = tuple(points[neighbor][axis] - points[index][axis] for axis in range(3))
            vertical = sum(delta[axis] * normal[axis] for axis in range(3))
            tangent = tuple(delta[axis] - vertical * normal[axis] for axis in range(3))
            tangent_steps.append(math.sqrt(sum(value * value for value in tangent)))
            step_errors.append(2.0 * uncertainty)
        certain_contact = [abs(d) + uncertainty <= contact_tolerance for d in distances]
        possible_contact = [max(0.0, abs(d) - uncertainty) <= contact_tolerance for d in distances]
        certain_stationary = [step + error <= stationary_tolerance for step, error in zip(tangent_steps, step_errors)]
        possible_stationary = [max(0.0, step - error) <= stationary_tolerance for step, error in zip(tangent_steps, step_errors)]
        certain = [a and b for a, b in zip(certain_contact, certain_stationary)]
        possible = [a and b for a, b in zip(possible_contact, possible_stationary)]

        def runs(mask):
            indices = [i for i, value in enumerate(mask) if value]
            groups = []
            for index in indices:
                if not groups or index > groups[-1][-1] + 1:
                    groups.append([index])
                else:
                    groups[-1].append(index)
            if looped and len(groups) > 1 and groups[0][0] == 0 and groups[-1][-1] == frame_count - 1:
                groups = [groups[-1] + groups[0]] + groups[1:-1]
            return [group for group in groups if len(group) >= min_frames]

        certain_runs, possible_runs = runs(certain), runs(possible)
        side_plants = []
        for group in possible_runs:
            group_certain = next((candidate for candidate in certain_runs if set(candidate) & set(group)), None)
            index = min(group) if min(group) < frame_count else 0
            item = {"foot": side, "bone": row.get("bone"), "frame": frame_start + index,
                    "time_seconds": index / fps, "contact_frames": [frame_start + i for i in group],
                    "confidence": "measured_certain" if group_certain else "uncertain_within_measurement_error",
                    "signed_ground_distance_units": distances[index], "tangent_step_units_per_frame": tangent_steps[index],
                    "measurement_uncertainty_units": uncertainty}
            side_plants.append(item)
        plants.extend(side_plants)
        counts[side] = {"certain": len(certain_runs), "possible": len(possible_runs),
                        "uncertain": len(possible_runs) - len(certain_runs)}
        uncertain_any = uncertain_any or counts[side]["uncertain"] > 0

    duration = frame_count / fps
    if humanoid_move:
        duration_ok = 1.0 <= duration <= 1.5
        counts_ok = all(counts[side]["certain"] == 1 and counts[side]["possible"] == 1 for side in ("left", "right"))
        status = "pass" if duration_ok and counts_ok and not uncertain_any else "blocked" if not duration_ok or any(counts[s]["certain"] != 1 or counts[s]["possible"] != 1 for s in ("left", "right")) else "needs_review"
    else:
        status = "needs_review" if uncertain_any else "measured"
        duration_ok = None
    return {"status": status, "source": "measured_blender_world_foot_coordinates",
            "ground_plane": {"normal": list(normal), "offset": offset},
            "thresholds": {"contact_tolerance_units": contact_tolerance, "stationary_tolerance_units_per_frame": stationary_tolerance,
                           "measurement_uncertainty_units": uncertainty, "min_contact_frames": min_frames},
            "frame_count": frame_count, "fps": fps, "cycle_duration_seconds": duration,
            "humanoid_move_duration_in_1_to_1_5_seconds": duration_ok, "plant_counts": counts,
            "plants": plants, "suggested_event_times_seconds": sorted(item["time_seconds"] for item in plants),
            "uncertainty_flagged": uncertain_any}


def inspect_animation_delivery(tree, *, skeleton_tree=None, action_name="", role="", looped=None, frame_start=1,
                               root_bone=None, root_policy="in_place_xy_preserve_z", strike_windows=(),
                               foot_world_measurements=None, entity_scale=None, root_drift_ceiling=0.2,
                               humanoid=None):
    """Measure an actual decoded ``.anim`` tree and return delivery evidence.

    PDX animation samples use the locked exporter order ``t,q,s`` and xyzw
    quaternions. Root checks follow PDX Y-up coordinates, so Blender's
    ``in_place_xy_preserve_z`` policy maps to PDX horizontal X/Z with vertical Y.
    Foot contact is omitted as unmeasured unless measured world positions and
    their ground/uncertainty metadata are supplied by Blender inspection.
    """
    decoded = decode_animation_tree(tree)
    if looped is not None and type(looped) is not bool:
        raise ValueError("looped must be a boolean when supplied.")
    if humanoid is not None and type(humanoid) is not bool:
        raise ValueError("humanoid must be a boolean when supplied.")
    if type(frame_start) is not int or frame_start < 0:
        raise ValueError("frame_start must be a nonnegative whole frame.")
    if not isinstance(action_name, str) or not isinstance(role, str):
        raise ValueError("action_name and role must be strings.")
    root_drift_ceiling = _number(root_drift_ceiling, "root_drift_ceiling")
    if root_drift_ceiling < 0:
        raise ValueError("root_drift_ceiling must be nonnegative.")
    frame_end = frame_start + decoded["frame_count"] - 1
    windows = _validate_windows(strike_windows, frame_start, frame_end)
    role_key = role.casefold()
    angular_limit = 15.0 if role_key in {"idle", "move"} else 30.0

    transitions = []
    q_sign_discontinuities = []
    loop_seams = []
    raw_q_samples_by_bone = _raw_quaternion_samples_by_bone(tree, decoded)
    for bone in decoded["bones"]:
        name = bone["name"]
        poses = [frame[name] for frame in decoded["frames"]]
        raw_samples = raw_q_samples_by_bone.get(name, [])
        angular, translation = [], []
        for index in range(decoded["frame_count"] - 1):
            angle = _quaternion_angle_degrees(poses[index]["q"], poses[index + 1]["q"])
            step = _distance(poses[index]["t"], poses[index + 1]["t"])
            angular.append(angle)
            translation.append(step)
            frame = frame_start + index + 1
            transitions.append({"frame": frame, "bone": name, "angular_deg": angle,
                                "translation_step": step, "time_seconds": (frame - frame_start) / decoded["fps"]})
            if raw_samples:
                dot = sum(a * b for a, b in zip(raw_samples[index], raw_samples[index + 1]))
                if dot < 0:
                    q_sign_discontinuities.append({"frame": frame, "bone": name, "raw_dot": dot})
        if raw_samples:
            initial_q = bone["initial_q"]
            if sum(a * b for a, b in zip(initial_q, raw_samples[0])) < 0:
                q_sign_discontinuities.append({"frame": frame_start, "bone": name, "raw_dot": sum(a * b for a, b in zip(initial_q, raw_samples[0])), "seam": "initial_to_first_sample"})
        seam_angle = _quaternion_angle_degrees(poses[-1]["q"], poses[0]["q"])
        seam_position = _distance(poses[-1]["t"], poses[0]["t"])
        loop_seams.append({"bone": name, "angular_gap_deg": seam_angle, "translation_gap_units": seam_position})

    local_rotation_violations = []
    local_translation_exceedances = []
    for row in transitions:
        if not _inside_window(row["frame"], windows):
            if row["angular_deg"] > angular_limit:
                local_rotation_violations.append({**row, "kind": "local_joint_rotation_exceeds_limit", "limit": angular_limit})
            if row["translation_step"] > 0.25:
                local_translation_exceedances.append({**row, "kind": "local_channel_translation_exceeds_world_speed_limit", "limit": 0.25})

    peak_table = []
    by_bone = defaultdict(list)
    for row in transitions:
        by_bone[row["bone"]].append(row)
    for bone_name, rows in by_bone.items():
        angles = [row["angular_deg"] for row in rows]
        steps = [row["translation_step"] for row in rows]
        peaks = _local_peak_indices(angles) | _local_peak_indices(steps)
        for index in sorted(peaks):
            row = dict(rows[index])
            dimensions = []
            if index in _local_peak_indices(angles):
                dimensions.append("angular")
            if index in _local_peak_indices(steps):
                dimensions.append("translation")
            row["peak_dimensions"] = dimensions
            peak_table.append(row)
    peak_table.sort(key=lambda row: (row["frame"], row["bone"]))

    seam_failures = [row for row in loop_seams if row["angular_gap_deg"] >= 3.0 or row["translation_gap_units"] >= 0.05]
    loop_report = {"status": "not_applicable", "angular_ceiling_deg_exclusive": 3.0,
                   "translation_ceiling_units_exclusive": 0.05, "per_bone": loop_seams,
                   "worst_angular_gap_deg": max((row["angular_gap_deg"] for row in loop_seams), default=0.0),
                   "worst_translation_gap_units": max((row["translation_gap_units"] for row in loop_seams), default=0.0)}
    if looped is True:
        loop_report["status"] = "blocked" if seam_failures else "pass"
        loop_report["failures"] = seam_failures
    elif looped is None:
        loop_report["status"] = "needs_review"
        loop_report["reason"] = "loop or state-chaining behavior was not declared"

    if skeleton_tree is None and any(node.tag == "skeleton" for node in tree.iter()):
        skeleton_tree = tree
    world_motion = _world_motion_report(decoded, skeleton_tree, frame_start, decoded["fps"], windows,
                                        angular_limit, 0.25, entity_scale)
    world_violations = world_motion.get("violations", [])
    violations = local_rotation_violations + world_violations
    root_report = _root_report(decoded, root_bone, role, root_policy, frame_start, root_drift_ceiling, entity_scale)
    humanoid_move = humanoid and role_key == "move"
    foot_report = _foot_contact_report(foot_world_measurements, decoded["frame_count"], decoded["fps"], frame_start, looped is True, humanoid_move)
    q_status = "blocked" if q_sign_discontinuities else "pass"
    threshold_status = "blocked" if violations else "needs_review" if world_motion["status"] != "pass" else "pass"
    statuses = [q_status, threshold_status]
    if looped is not False:
        statuses.append(loop_report["status"])
    statuses.append(root_report["status"])
    statuses.append(world_motion["status"])
    if humanoid_move:
        statuses.append(foot_report["status"])
    if humanoid is None or not role.strip():
        statuses.append("needs_review")
    status = "blocked" if "blocked" in statuses else "needs_review" if "needs_review" in statuses or "unmeasured" in statuses else "pass"
    return {"status": status, "action_name": action_name, "semantic_role": role, "fps": decoded["fps"],
            "frame_start": frame_start, "frame_end": frame_end, "frame_count": decoded["frame_count"],
            "sampled_span_seconds": (decoded["frame_count"] - 1) / decoded["fps"],
            "cycle_duration_seconds": decoded["frame_count"] / decoded["fps"], "looped": looped,
            "profile_evidence": "humanoid" if humanoid is True else "nonhumanoid" if humanoid is False else "unresolved",
            "joint_count": decoded["joint_count"], "bone_names": [bone["name"] for bone in decoded["bones"]],
            "quaternion_order": "xyzw", "quaternion_sign_continuity": {"status": q_status,
                "negative_dot_count": len(q_sign_discontinuities), "discontinuities": q_sign_discontinuities,
                "operation_policy": "q/-q sign only; rotation is equivalent; no key/bone/weight synthesis"},
            "single_frame_limits": {"angular_degrees_exclusive": angular_limit, "world_translation_units_per_frame_exclusive": 0.25,
                                    "explicit_strike_windows": [list(row) for row in windows], "status": threshold_status,
                                    "violations": violations,
                                    "local_channel_translation_exceedances_review_only": local_translation_exceedances,
                                    "world_motion_status": world_motion["status"]},
            "loop_seam": loop_report, "root_motion": root_report, "world_motion": world_motion,
            "foot_contacts": foot_report,
            "motion_peak_table": peak_table, "motion_peak_time_policy": "local maxima of decoded per-bone local q/t sample deltas; times are seconds from frame_start; suggestions require semantic/contact review",
            "measurement_scope": "decoded per-bone local channels; world-space foot contacts require supplied Blender measurements",
            "nonunit_quaternions": {"initial": decoded["nonunit_initial_quaternions"], "samples": decoded["nonunit_sample_quaternions"]}}


def _raw_quaternion_samples_by_bone(tree, decoded):
    """Return raw xyzw samples by bone in one pass through the flattened q array."""
    info, samples = _child(tree, "info"), _child(tree, "samples")
    q_bones = [bone for bone in info if "q" in _channel_names(bone.get("sa"), str(bone.tag))]
    if not q_bones:
        return {}
    values = [_number(value, "samples.q") for value in _as_sequence(samples.get("q"), "samples.q")]
    stride = len(q_bones) * 4
    result = {str(bone.tag): [] for bone in q_bones}
    for frame in range(decoded["frame_count"]):
        for index, bone in enumerate(q_bones):
            start = frame * stride + index * 4
            result[str(bone.tag)].append(tuple(values[start:start + 4]))
    return result


def _curve_xy(point):
    return (_number(point.co[0], "quaternion key frame"), _number(point.co[1], "quaternion key value"))


def _set_curve_y(coordinate, value):
    try:
        coordinate.y = value
    except AttributeError:
        coordinate[1] = value


def _negate_point_y(point):
    for attribute in ("co", "handle_left", "handle_right"):
        coordinate = getattr(point, attribute, None)
        if coordinate is None:
            raise ValueError(f"Quaternion curve point is missing {attribute} data.")
        value = _number(coordinate[1], f"quaternion {attribute}")
        _set_curve_y(coordinate, -value)


def normalize_quaternion_curve_signs(fcurves):
    """Negate equivalent q keys/handles to enforce per-bone sign continuity.

    The entire input is validated before any point is changed. Every animated
    quaternion path must have channels 0..3 with identical, unique key times.
    """
    groups = defaultdict(dict)
    for curve in fcurves:
        path = getattr(curve, "data_path", "")
        if not isinstance(path, str) or not path.endswith(".rotation_quaternion"):
            continue
        index = getattr(curve, "array_index", None)
        if type(index) is not int or index not in range(4):
            raise ValueError("Quaternion F-curves must use component indices 0 through 3.")
        if index in groups[path]:
            raise ValueError(f"Duplicate quaternion F-curve component for {path!r}.")
        groups[path][index] = curve

    prepared = []
    for path, channels in sorted(groups.items()):
        if set(channels) != {0, 1, 2, 3}:
            raise ValueError(f"Quaternion F-curve group {path!r} must contain all four components.")
        points_by_channel = {index: list(channels[index].keyframe_points) for index in range(4)}
        times_by_channel = []
        for index in range(4):
            points = points_by_channel[index]
            coordinates = [_curve_xy(point) for point in points]
            times = [row[0] for row in coordinates]
            if len(times) != len(set(times)):
                raise ValueError(f"Quaternion F-curve group {path!r} has duplicate key times.")
            order = sorted(range(len(times)), key=times.__getitem__)
            points_by_channel[index] = [points[position] for position in order]
            times_by_channel.append(tuple(times[position] for position in order))
        if any(times != times_by_channel[0] for times in times_by_channel[1:]):
            raise ValueError(f"Quaternion F-curve group {path!r} does not have exactly aligned component key times.")
        for position, frame in enumerate(times_by_channel[0]):
            q = tuple(_curve_xy(points_by_channel[index][position])[1] for index in range(4))
            _unit_quaternion(q, f"{path} key at frame {frame}")
        for index in range(4):
            for point in points_by_channel[index]:
                _curve_xy(point)
                for attribute in ("handle_left", "handle_right"):
                    coord = getattr(point, attribute, None)
                    if coord is None or not math.isfinite(float(coord[0])) or not math.isfinite(float(coord[1])):
                        raise ValueError(f"Quaternion F-curve group {path!r} has malformed Bezier handles.")
        prepared.append((path, points_by_channel, times_by_channel[0]))

    reports = []
    for path, points_by_channel, times in prepared:
        flips = []
        previous = None
        for position, frame in enumerate(times):
            q = tuple(_curve_xy(points_by_channel[index][position])[1] for index in range(4))
            normalized, _ = _unit_quaternion(q, f"{path} key at frame {frame}")
            if previous is not None and sum(a * b for a, b in zip(previous, normalized)) < 0:
                for index in range(4):
                    _negate_point_y(points_by_channel[index][position])
                normalized = tuple(-value for value in normalized)
                flips.append(frame)
            previous = normalized
        reports.append({"data_path": path, "key_count": len(times), "sign_flipped_key_times": flips,
                        "keys_added": 0, "keys_removed": 0, "bones_or_weights_changed": False,
                        "operation": "negate all four existing quaternion component values and both handle values; x/time data retained"})
    return {"status": "pass", "curve_groups": reports,
            "sign_flipped_key_count": sum(len(row["sign_flipped_key_times"]) for row in reports),
            "keys_added": 0, "keys_removed": 0}
