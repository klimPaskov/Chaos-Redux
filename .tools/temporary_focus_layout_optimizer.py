#!/usr/bin/env python3
"""Emit an apply_patch payload for dependency-layered HOI4 focus-tree coordinates.

This is a temporary Event 005 repair helper. It never writes source files.
"""

from __future__ import annotations

import argparse
import math
import random
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import networkx as nx
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


@dataclass
class Focus:
	id: str
	x: int
	y: int
	parents: list[str]
	start: int
	buffer: list[str]
	id_offset: int
	coordinate_end_offset: int


def parse_tree(path: Path, tree_id: str) -> dict[str, Focus]:
	lines = path.read_text(encoding="utf-8-sig").splitlines()
	id_line = next(
		i
		for i, line in enumerate(lines)
		if re.match(r"^\s*id\s*=\s*" + re.escape(tree_id) + r"\s*$", line)
	)
	start = max(i for i in range(id_line + 1) if re.match(r"^focus_tree\s*=\s*\{", lines[i]))
	end = next(
		(i for i in range(id_line + 1, len(lines)) if re.match(r"^focus_tree\s*=\s*\{", lines[i])),
		len(lines),
	)
	nodes: dict[str, Focus] = {}
	i = start
	while i < end:
		if not re.match(r"^\s*focus\s*=\s*\{", lines[i]):
			i += 1
			continue
		block_start = i
		depth = 0
		buffer: list[str] = []
		while i < end:
			line = lines[i]
			buffer.append(line)
			depth += line.count("{") - line.count("}")
			i += 1
			if depth == 0:
				break
		raw = "\n".join(buffer)
		focus_id = re.search(r"^\s*id\s*=\s*(\S+)", raw, re.M).group(1)
		x = int(re.search(r"\bx\s*=\s*(-?\d+)", raw).group(1))
		y = int(re.search(r"\by\s*=\s*(-?\d+)", raw).group(1))
		parents: list[str] = []
		for match in re.finditer(r"^\s*prerequisite\s*=\s*\{([^}]*)\}", raw, re.M):
			parents.extend(re.findall(r"focus\s*=\s*(\S+)", match.group(1)))
		id_offset = next(j for j, line in enumerate(buffer) if re.match(r"^\s*id\s*=", line))
		x_offset = next(j for j, line in enumerate(buffer) if re.search(r"\bx\s*=\s*-?\d+", line))
		y_offset = next(j for j, line in enumerate(buffer) if re.search(r"\by\s*=\s*-?\d+", line))
		nodes[focus_id] = Focus(
			id=focus_id,
			x=x,
			y=y,
			parents=parents,
			start=block_start,
			buffer=buffer,
			id_offset=id_offset,
			coordinate_end_offset=max(x_offset, y_offset),
		)
	return nodes


def dependency_depths(nodes: dict[str, Focus]) -> dict[str, int]:
	depths: dict[str, int] = {}
	visiting: set[str] = set()

	def visit(focus_id: str) -> int:
		if focus_id in depths:
			return depths[focus_id]
		if focus_id in visiting:
			raise ValueError(f"Prerequisite cycle at {focus_id}")
		visiting.add(focus_id)
		parent_depths = [visit(parent) for parent in nodes[focus_id].parents if parent in nodes]
		depth = (max(parent_depths) + 1) if parent_depths else 0
		visiting.remove(focus_id)
		depths[focus_id] = depth
		return depth

	for focus_id in nodes:
		visit(focus_id)
	return depths


def proper_cross(a, b, c, d) -> bool:
	def orient(p, q, r):
		return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
	o1, o2, o3, o4 = orient(a, b, c), orient(a, b, d), orient(c, d, a), orient(c, d, b)
	return ((o1 > 0 > o2) or (o2 > 0 > o1)) and ((o3 > 0 > o4) or (o4 > 0 > o3))


def point_segment_distance(point, start, end) -> float:
	dx, dy = end[0] - start[0], end[1] - start[1]
	if dx == 0 and dy == 0:
		return math.dist(point, start)
	t = ((point[0] - start[0]) * dx + (point[1] - start[1]) * dy) / (dx * dx + dy * dy)
	if t <= 0 or t >= 1:
		return 999.0
	projection = (start[0] + t * dx, start[1] + t * dy)
	return math.dist(point, projection)


def layout_score(nodes, depths, coords):
	edges = [(parent, child) for child, focus in nodes.items() for parent in focus.parents if parent in nodes]
	crossings = 0
	for index, (a, b) in enumerate(edges):
		for c, d in edges[index + 1 :]:
			if len({a, b, c, d}) < 4:
				continue
			if proper_cross((coords[a], depths[a]), (coords[b], depths[b]), (coords[c], depths[c]), (coords[d], depths[d])):
				crossings += 1
	node_hits = 0
	for parent, child in edges:
		start, end = (coords[parent], depths[parent]), (coords[child], depths[child])
		for other in nodes:
			if other == parent or other == child:
				continue
			if point_segment_distance((coords[other], depths[other]), start, end) < 0.45:
				node_hits += 1
	long_connectors = 0
	total_span = 0
	for parent, child in edges:
		horizontal = abs(coords[parent] - coords[child])
		vertical = depths[child] - depths[parent]
		total_span += horizontal + vertical
		if horizontal > 8 or vertical > 4 or horizontal + vertical > 10:
			long_connectors += 1
	children = defaultdict(list)
	indegree = defaultdict(int)
	for parent, child in edges:
		children[parent].append(child)
		indegree[child] += 1
	detours = 0
	for parent, child in edges:
		if len(children[parent]) == 1 and indegree[child] == 1 and (coords[parent] != coords[child] or depths[child] != depths[parent] + 1):
			detours += 1
	return (
		crossings * 1_000_000
		+ node_hits * 200_000
		+ long_connectors * 20_000
		+ detours * 400
		+ total_span,
		(crossings, node_hits, long_connectors, detours, total_span),
	)


def ordered_layers(nodes, depths):
	graph = nx.Graph()
	graph.add_nodes_from(nodes)
	for child, focus in nodes.items():
		for parent in focus.parents:
			if parent in nodes:
				graph.add_edge(parent, child)
	parents = {node: [parent for parent in nodes[node].parents if parent in nodes] for node in nodes}
	children = defaultdict(list)
	for child, focus_parents in parents.items():
		for parent in focus_parents:
			children[parent].append(child)
	for parent in children:
		children[parent].sort(key=lambda child: (nodes[child].x, child))
	layers = defaultdict(list)
	if all(len(focus_parents) <= 1 for focus_parents in parents.values()):
		roots = sorted((node for node in nodes if not parents[node]), key=lambda node: (nodes[node].x, node))
		preorder: list[str] = []

		def walk(node):
			preorder.append(node)
			for child in children[node]:
				walk(child)

		for root in roots:
			walk(root)
		preorder_index = {node: index for index, node in enumerate(preorder)}
		for node in nodes:
			layers[depths[node]].append(node)
		for layer in layers:
			layers[layer].sort(key=lambda node: preorder_index[node])
		return layers
	if nx.check_planarity(graph)[0]:
		planar_position = nx.planar_layout(graph)
		for node in nodes:
			layers[depths[node]].append(node)
		for layer in layers:
			layers[layer].sort(key=lambda node: (float(planar_position[node][0]), nodes[node].x, node))
	else:
		for node in nodes:
			layers[depths[node]].append(node)
		for layer in layers:
			layers[layer].sort(key=lambda node: (nodes[node].x, node))
	return layers


def coordinates_for_layers(layers, offsets=None):
	coords = {}
	for layer, ordered in layers.items():
		offset = 0 if offsets is None else offsets.get(layer, 0)
		for rank, node in enumerate(ordered):
			coords[node] = 2 * rank - (len(ordered) - 1) + offset
	return coords


def optimize_layout(nodes, depths):
	layers = ordered_layers(nodes, depths)
	parent_map = {node: [parent for parent in nodes[node].parents if parent in nodes] for node in nodes}
	child_map = defaultdict(list)
	for child, parents in parent_map.items():
		for parent in parents:
			child_map[parent].append(child)
	if all(len(parents) <= 1 for parents in parent_map.values()):
		base = coordinates_for_layers(layers)
		ordered_depths = sorted(layers)
		offset_range = range(-20, 21)
		dp = {0: (0, None)}
		choices = {}
		for depth in ordered_depths[1:]:
			new_dp = {}
			for child_offset in offset_range:
				best = None
				for parent_offset, (prior_cost, _) in dp.items():
					cost = prior_cost + abs(child_offset - parent_offset)
					for child in layers[depth]:
						parents = parent_map[child]
						if not parents:
							continue
						parent = parents[0]
						span = abs((base[child] + child_offset) - (base[parent] + parent_offset))
						cost += max(0, span - 8) * 100_000 + span
						if len(child_map[parent]) == 1 and span:
							cost += 400
					candidate = (cost, parent_offset)
					if best is None or candidate < best:
						best = candidate
				new_dp[child_offset] = best
			choices[depth] = {offset: previous for offset, (_, previous) in new_dp.items()}
			dp = new_dp
		last_offset = min(dp, key=lambda offset: dp[offset][0])
		offsets = {ordered_depths[-1]: last_offset}
		for index in range(len(ordered_depths) - 1, 0, -1):
			depth = ordered_depths[index]
			last_offset = choices[depth][last_offset]
			offsets[ordered_depths[index - 1]] = last_offset
		coords = coordinates_for_layers(layers, offsets)
		return coords, layout_score(nodes, depths, coords)[1]
	for _ in range(16):
		positions = {node: index for layer in layers.values() for index, node in enumerate(layer)}
		for layer in sorted(layers):
			if layer == 0:
				continue
			layers[layer].sort(key=lambda node: ((sum(positions[p] for p in parent_map[node]) / len(parent_map[node])) if parent_map[node] else positions[node], positions[node]))
		positions = {node: index for layer in layers.values() for index, node in enumerate(layer)}
		for layer in sorted(layers, reverse=True):
			layers[layer].sort(key=lambda node: ((sum(positions[c] for c in child_map[node]) / len(child_map[node])) if child_map[node] else positions[node], positions[node]))
	offsets = {layer: 0 for layer in layers}
	coords = coordinates_for_layers(layers, offsets)
	best_score, best_details = layout_score(nodes, depths, coords)
	rng = random.Random(5005 + len(nodes))
	for iteration in range(800):
		movable_layers = [layer for layer, ordered in layers.items() if len(ordered) > 1]
		layer = rng.choice(movable_layers)
		ordered = layers[layer]
		left = rng.randrange(len(ordered) - 1)
		ordered[left], ordered[left + 1] = ordered[left + 1], ordered[left]
		candidate = coordinates_for_layers(layers, offsets)
		candidate_score, candidate_details = layout_score(nodes, depths, candidate)
		if candidate_score <= best_score:
			coords, best_score, best_details = candidate, candidate_score, candidate_details
		else:
			ordered[left], ordered[left + 1] = ordered[left + 1], ordered[left]
		if iteration % 100 == 99:
			for target_layer in sorted(layers):
				current_offset = offsets[target_layer]
				choice = (best_score, current_offset, best_details, coords)
				for offset in range(current_offset - 4, current_offset + 5):
					offsets[target_layer] = offset
					candidate = coordinates_for_layers(layers, offsets)
					candidate_score, candidate_details = layout_score(nodes, depths, candidate)
					if candidate_score < choice[0]:
						choice = (candidate_score, offset, candidate_details, candidate)
				offsets[target_layer] = choice[1]
				best_score, best_details, coords = choice[0], choice[2], choice[3]
	return coords, best_details


def align_linear_columns(nodes, depths):
	"""Keep every mechanically linear chain vertical while preserving layer order."""
	parents = {node: [parent for parent in focus.parents if parent in nodes] for node, focus in nodes.items()}
	children = defaultdict(list)
	for child, focus_parents in parents.items():
		for parent in focus_parents:
			children[parent].append(child)
	group_parent = {node: node for node in nodes}

	def find(node):
		while group_parent[node] != node:
			group_parent[node] = group_parent[group_parent[node]]
			node = group_parent[node]
		return node

	def union(left, right):
		left_root, right_root = find(left), find(right)
		if left_root != right_root:
			group_parent[right_root] = left_root

	for parent, focus_children in children.items():
		if len(focus_children) != 1:
			continue
		child = focus_children[0]
		if len(parents[child]) == 1 and depths[child] == depths[parent] + 1:
			union(parent, child)
	groups = {node: find(node) for node in nodes}
	constraints = nx.DiGraph()
	constraints.add_nodes_from(set(groups.values()))
	layers = defaultdict(list)
	for node, depth in depths.items():
		layers[depth].append(node)
	for ordered in layers.values():
		ordered.sort(key=lambda node: (nodes[node].x, node))
		for left, right in zip(ordered, ordered[1:]):
			left_group, right_group = groups[left], groups[right]
			if left_group != right_group:
				constraints.add_edge(left_group, right_group)
	if not nx.is_directed_acyclic_graph(constraints):
		raise ValueError("Linear-column constraints conflict with the current planar layer order")
	columns = {group: 0 for group in constraints}
	for group in nx.topological_sort(constraints):
		for successor in constraints.successors(group):
			columns[successor] = max(columns[successor], columns[group] + 2)
	coords = {node: columns[groups[node]] for node in nodes}
	center = round((min(coords.values()) + max(coords.values())) / 2)
	coords = {node: x - center for node, x in coords.items()}
	return coords, layout_score(nodes, depths, coords)[1]


def optimize_linear_columns(nodes, depths, maximum_span=8):
	"""MILP layout: vertical linear chains, stable layer order, bounded connectors."""
	parents = {node: [parent for parent in focus.parents if parent in nodes] for node, focus in nodes.items()}
	children = defaultdict(list)
	for child, focus_parents in parents.items():
		for parent in focus_parents:
			children[parent].append(child)
	group_parent = {node: node for node in nodes}

	def find(node):
		while group_parent[node] != node:
			group_parent[node] = group_parent[group_parent[node]]
			node = group_parent[node]
		return node

	def union(left, right):
		left_root, right_root = find(left), find(right)
		if left_root != right_root:
			group_parent[right_root] = left_root

	for parent, focus_children in children.items():
		if len(focus_children) == 1:
			child = focus_children[0]
			if len(parents[child]) == 1 and depths[child] == depths[parent] + 1:
				union(parent, child)
	groups_by_node = {node: find(node) for node in nodes}
	groups = sorted(set(groups_by_node.values()))
	group_index = {group: index for index, group in enumerate(groups)}
	edges = [(parent, child) for child, focus in nodes.items() for parent in focus.parents if parent in nodes]
	variable_count = len(groups) + len(edges)
	objective = np.zeros(variable_count)
	objective[len(groups):] = 1.0
	lower = np.full(variable_count, -200.0)
	upper = np.full(variable_count, 200.0)
	lower[len(groups):] = 0.0
	upper[len(groups):] = float(maximum_span)
	root = min(nodes, key=lambda node: (depths[node], nodes[node].x, node))
	root_index = group_index[groups_by_node[root]]
	lower[root_index] = upper[root_index] = 0.0
	rows = []
	row_lower = []
	row_upper = []
	layers = defaultdict(list)
	for node, depth in depths.items():
		layers[depth].append(node)
	for ordered in layers.values():
		ordered.sort(key=lambda node: (nodes[node].x, node))
		for left, right in zip(ordered, ordered[1:]):
			row = np.zeros(variable_count)
			row[group_index[groups_by_node[right]]] = 1
			row[group_index[groups_by_node[left]]] = -1
			rows.append(row)
			row_lower.append(2.0)
			row_upper.append(np.inf)
	for edge_index, (parent, child) in enumerate(edges):
		parent_index = group_index[groups_by_node[parent]]
		child_index = group_index[groups_by_node[child]]
		span_index = len(groups) + edge_index
		for parent_sign in (-1, 1):
			row = np.zeros(variable_count)
			row[parent_index] = parent_sign
			row[child_index] = -parent_sign
			row[span_index] = 1
			rows.append(row)
			row_lower.append(0.0)
			row_upper.append(np.inf)
	result = milp(
		c=objective,
		integrality=np.ones(variable_count),
		bounds=Bounds(lower, upper),
		constraints=LinearConstraint(np.vstack(rows), np.array(row_lower), np.array(row_upper)),
		options={"time_limit": 30},
	)
	if not result.success:
		raise ValueError(f"MILP layout failed: {result.message}")
	coords = {node: int(round(result.x[group_index[groups_by_node[node]]])) for node in nodes}
	return coords, layout_score(nodes, depths, coords)[1]


def optimize_minimum_detours(nodes, depths, maximum_span=8, layers_override=None):
	"""Minimize unavoidable linear detours while keeping every connector short."""
	ordered_nodes = list(nodes)
	node_index = {node: index for index, node in enumerate(ordered_nodes)}
	edges = [(parent, child) for child, focus in nodes.items() for parent in focus.parents if parent in nodes]
	parents = defaultdict(list)
	children = defaultdict(list)
	for parent, child in edges:
		parents[child].append(parent)
		children[parent].append(child)
	linear_edges = [(parent, child) for parent, child in edges if len(children[parent]) == 1 and len(parents[child]) == 1 and depths[child] == depths[parent] + 1]
	span_start = len(ordered_nodes)
	detour_start = span_start + len(edges)
	variable_count = detour_start + len(linear_edges)
	objective = np.zeros(variable_count)
	objective[span_start:detour_start] = 1.0
	objective[detour_start:] = 10_000.0
	lower = np.full(variable_count, -200.0)
	upper = np.full(variable_count, 200.0)
	lower[span_start:detour_start] = 0.0
	upper[span_start:detour_start] = float(maximum_span)
	lower[detour_start:] = 0.0
	upper[detour_start:] = 1.0
	root = min(nodes, key=lambda node: (depths[node], nodes[node].x, node))
	lower[node_index[root]] = upper[node_index[root]] = 0.0
	rows = []
	row_lower = []
	row_upper = []
	if layers_override is None:
		layers = defaultdict(list)
		for node, depth in depths.items():
			layers[depth].append(node)
		for ordered in layers.values():
			ordered.sort(key=lambda node: (nodes[node].x, node))
	else:
		layers = {depth: list(ordered) for depth, ordered in layers_override.items()}
	for ordered in layers.values():
		for left, right in zip(ordered, ordered[1:]):
			row = np.zeros(variable_count)
			row[node_index[right]] = 1
			row[node_index[left]] = -1
			rows.append(row)
			row_lower.append(2.0)
			row_upper.append(np.inf)
	for edge_index, (parent, child) in enumerate(edges):
		span_index = span_start + edge_index
		for parent_sign in (-1, 1):
			row = np.zeros(variable_count)
			row[node_index[parent]] = parent_sign
			row[node_index[child]] = -parent_sign
			row[span_index] = 1
			rows.append(row)
			row_lower.append(0.0)
			row_upper.append(np.inf)
	for detour_index, (parent, child) in enumerate(linear_edges):
		binary_index = detour_start + detour_index
		for parent_sign in (-1, 1):
			row = np.zeros(variable_count)
			row[node_index[parent]] = parent_sign
			row[node_index[child]] = -parent_sign
			row[binary_index] = 200.0
			rows.append(row)
			row_lower.append(0.0)
			row_upper.append(np.inf)
	result = milp(
		c=objective,
		integrality=np.ones(variable_count),
		bounds=Bounds(lower, upper),
		constraints=LinearConstraint(np.vstack(rows), np.array(row_lower), np.array(row_upper)),
		options={"time_limit": 30},
	)
	if not result.success:
		raise ValueError(f"Minimum-detour MILP failed: {result.message}")
	coords = {node: int(round(result.x[node_index[node]])) for node in nodes}
	return coords, layout_score(nodes, depths, coords)[1]


def search_minimum_detours(nodes, depths):
	layers = defaultdict(list)
	for node, depth in depths.items():
		layers[depth].append(node)
	for ordered in layers.values():
		ordered.sort(key=lambda node: (nodes[node].x, node))
	best_coords, best_details = optimize_minimum_detours(nodes, depths, layers_override=layers)
	for _ in range(8):
		parents = defaultdict(list)
		children = defaultdict(list)
		for child, focus in nodes.items():
			for parent in focus.parents:
				if parent in nodes:
					parents[child].append(parent)
					children[parent].append(child)
		problem_nodes = set()
		for parent, focus_children in children.items():
			if len(focus_children) != 1:
				continue
			child = focus_children[0]
			if len(parents[child]) == 1 and best_coords[parent] != best_coords[child]:
				problem_nodes.update((parent, child))
		choice = None
		for node in problem_nodes:
			depth = depths[node]
			original = layers[depth]
			old_index = original.index(node)
			for new_index in range(len(original)):
				if new_index == old_index:
					continue
				candidate_layers = {layer: list(ordered) for layer, ordered in layers.items()}
				ordered = candidate_layers[depth]
				ordered.pop(old_index)
				ordered.insert(new_index, node)
				rank_coords = {item: 2 * index for layer in candidate_layers.values() for index, item in enumerate(layer)}
				if layout_score(nodes, depths, rank_coords)[1][0] != 0:
					continue
				try:
					candidate_coords, candidate_details = optimize_minimum_detours(nodes, depths, layers_override=candidate_layers)
				except ValueError:
					continue
				candidate_key = (candidate_details[3], candidate_details[4])
				best_key = (best_details[3], best_details[4])
				if candidate_key < best_key and (choice is None or candidate_key < choice[0]):
					choice = (candidate_key, candidate_layers, candidate_coords, candidate_details)
		if choice is None:
			break
		_, layers, best_coords, best_details = choice
	return best_coords, best_details


def fast_crossing_count(nodes, depths, coords):
	edges = [(parent, child) for child, focus in nodes.items() for parent in focus.parents if parent in nodes]
	crossings = 0
	for index, (left_parent, left_child) in enumerate(edges):
		left_start = (coords[left_parent], depths[left_parent])
		left_end = (coords[left_child], depths[left_child])
		for right_parent, right_child in edges[index + 1:]:
			if len({left_parent, left_child, right_parent, right_child}) < 4:
				continue
			if proper_cross(left_start, left_end, (coords[right_parent], depths[right_parent]), (coords[right_child], depths[right_child])):
				crossings += 1
	return crossings


def search_crossing_order(nodes, depths):
	base_layers = ordered_layers(nodes, depths)
	parent_map = {node: [parent for parent in nodes[node].parents if parent in nodes] for node in nodes}
	child_map = defaultdict(list)
	for child, parents in parent_map.items():
		for parent in parents:
			child_map[parent].append(child)
	best_layers = {layer: list(ordered) for layer, ordered in base_layers.items()}
	best_coords = coordinates_for_layers(best_layers)
	best_crossings = fast_crossing_count(nodes, depths, best_coords)
	rng = random.Random(5005 + len(nodes))
	for restart in range(6):
		layers = {layer: list(ordered) for layer, ordered in base_layers.items()}
		if restart:
			for ordered in layers.values():
				for _ in range(max(1, len(ordered) // 3)):
					left = rng.randrange(len(ordered))
					right = rng.randrange(len(ordered))
					ordered[left], ordered[right] = ordered[right], ordered[left]
		for _ in range(24):
			positions = {node: index for ordered in layers.values() for index, node in enumerate(ordered)}
			for layer in sorted(layers):
				layers[layer].sort(key=lambda node: ((sum(positions[parent] for parent in parent_map[node]) / len(parent_map[node])) if parent_map[node] else positions[node], positions[node]))
			positions = {node: index for ordered in layers.values() for index, node in enumerate(ordered)}
			for layer in sorted(layers, reverse=True):
				layers[layer].sort(key=lambda node: ((sum(positions[child] for child in child_map[node]) / len(child_map[node])) if child_map[node] else positions[node], positions[node]))
		coords = coordinates_for_layers(layers)
		current_crossings = fast_crossing_count(nodes, depths, coords)
		for _ in range(500):
			movable = [layer for layer, ordered in layers.items() if len(ordered) > 1]
			layer = rng.choice(movable)
			ordered = layers[layer]
			old_index = rng.randrange(len(ordered))
			new_index = rng.randrange(len(ordered))
			if new_index == old_index:
				continue
			node = ordered.pop(old_index)
			ordered.insert(new_index, node)
			candidate_coords = coordinates_for_layers(layers)
			candidate_crossings = fast_crossing_count(nodes, depths, candidate_coords)
			if candidate_crossings <= current_crossings:
				coords, current_crossings = candidate_coords, candidate_crossings
			else:
				ordered.pop(new_index)
				ordered.insert(old_index, node)
			if current_crossings == 0:
				break
		if current_crossings < best_crossings:
			best_crossings = current_crossings
			best_layers = {layer: list(ordered) for layer, ordered in layers.items()}
		if best_crossings == 0:
			break
	try:
		return optimize_minimum_detours(nodes, depths, layers_override=best_layers)
	except ValueError:
		coords = coordinates_for_layers(best_layers)
		return coords, layout_score(nodes, depths, coords)[1]


def emit_patch(path, nodes, depths, coords):
	abs_path = str(path.resolve()).replace("\\", "/")
	patch = ["*** Begin Patch", f"*** Update File: {abs_path}"]
	changed = 0
	for focus in sorted(nodes.values(), key=lambda item: item.start):
		new_x, new_y = coords[focus.id], depths[focus.id]
		if new_x == focus.x and new_y == focus.y:
			continue
		changed += 1
		snippet = focus.buffer[focus.id_offset : focus.coordinate_end_offset + 1]
		for old_line in snippet:
			new_line = re.sub(r"\bx\s*=\s*-?\d+", f"x = {new_x}", old_line, count=1)
			new_line = re.sub(r"\by\s*=\s*-?\d+", f"y = {new_y}", new_line, count=1)
			if new_line == old_line:
				patch.append(" " + old_line)
			else:
				patch.extend(["-" + old_line, "+" + new_line])
		patch.append("@@")
	if not changed:
		raise SystemExit("No coordinate changes generated")
	patch.pop()
	patch.append("*** End Patch")
	print("\n".join(patch))


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("path", type=Path)
	parser.add_argument("tree_id")
	parser.add_argument("--report", action="store_true")
	parser.add_argument("--align-linear", action="store_true")
	parser.add_argument("--align-linear-milp", action="store_true")
	parser.add_argument("--minimum-detours", action="store_true")
	parser.add_argument("--search-minimum-detours", action="store_true")
	parser.add_argument("--crossing-search", action="store_true")
	args = parser.parse_args()
	nodes = parse_tree(args.path, args.tree_id)
	depths = dependency_depths(nodes)
	if args.crossing_search:
		coords, details = search_crossing_order(nodes, depths)
	elif args.search_minimum_detours:
		coords, details = search_minimum_detours(nodes, depths)
	elif args.minimum_detours:
		coords, details = optimize_minimum_detours(nodes, depths)
	elif args.align_linear_milp:
		coords, details = optimize_linear_columns(nodes, depths)
	elif args.align_linear:
		coords, details = align_linear_columns(nodes, depths)
	else:
		coords, details = optimize_layout(nodes, depths)
	if args.report:
		print({"tree": args.tree_id, "focuses": len(nodes), "predicted": details})
		return
	emit_patch(args.path, nodes, depths, coords)


if __name__ == "__main__":
	main()
