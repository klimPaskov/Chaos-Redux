#!/usr/bin/env node

// Generates the runtime GUI, GFX, scripted-GUI, scripted-localisation, and
// English localisation surfaces from reviewed exact-geometry manifests.
// The generated files are committed; this script keeps future map rebuilds
// reproducible and fails closed when a selected category lacks a manifest.

import fs from "node:fs";
import path from "node:path";

const workspace = process.cwd();
const manifestRoot = path.join(workspace, "docs", "formables", "state_puzzles");

const normalise = (value) => value.replace(/[^A-Za-z0-9_]/g, "_").toLowerCase();
const SCRIPT_IDENTIFIER_RE = /^[A-Za-z_][A-Za-z0-9_]*$/;
const pascal = (value) => normalise(value).split("_").filter(Boolean).map((part) => part[0].toUpperCase() + part.slice(1)).join("");
const slash = (value) => value.replaceAll("\\", "/");
const quote = (value) => `"${value}"`;

function normalisedId(value, field) {
	if (typeof value !== "string" || !value.trim()) throw new Error(`${field} must be a non-empty string`);
	const token = normalise(value).replace(/^_+|_+$/g, "");
	if (!/[a-z0-9]/.test(token)) throw new Error(`${field} normalises to an empty runtime identifier: ${value}`);
	return token;
}

function scriptIdentifier(value, field) {
	if (typeof value !== "string" || !SCRIPT_IDENTIFIER_RE.test(value)) {
		throw new Error(`${field} must match [A-Za-z_][A-Za-z0-9_]*: ${value}`);
	}
	return value;
}

function runtimePath(value, field) {
	if (typeof value !== "string" || !value.trim()) throw new Error(`${field} must be a non-empty relative path`);
	const normalisedPath = slash(value);
	if (path.isAbsolute(value) || /^[A-Za-z]:[\\/]/.test(value) || normalisedPath.split("/").includes("..")) {
		throw new Error(`${field} must remain inside the mod workspace: ${value}`);
	}
	const absolute = path.resolve(workspace, normalisedPath);
	const workspacePrefix = workspace.endsWith(path.sep) ? workspace : `${workspace}${path.sep}`;
	if (absolute !== workspace && !absolute.startsWith(workspacePrefix)) {
		throw new Error(`${field} escapes the mod workspace: ${value}`);
	}
	return absolute;
}

function normaliseManifest(manifest, manifestPath) {
	if (manifest.schema === "chaos-redux-formable-state-puzzle/v1") {
		return {
			...manifest,
			decision_category: manifest.decision_category || manifest.category_id,
			__path: manifestPath,
			__sourceSchema: manifest.schema,
		};
	}

	const canvas = manifest.projection?.canvas;
	if (
		manifest.status !== "complete"
		|| !manifest.category_id
		|| !manifest.formable_id
		|| !Array.isArray(canvas)
		|| !Array.isArray(manifest.state_groups)
		|| !Array.isArray(manifest.assets)
	) {
		throw new Error(`${manifestPath}: unsupported legacy manifest shape`);
	}

	const requiredStateIds = [];
	for (const group of manifest.state_groups) {
		for (const stateId of group.state_ids ?? []) {
			if (!requiredStateIds.includes(stateId)) requiredStateIds.push(stateId);
		}
	}

	const states = requiredStateIds.map((stateId) => {
		const unresolved = manifest.assets.find((asset) => asset.state_id === stateId && asset.variant === "unresolved");
		const qualifying = manifest.assets.find((asset) => asset.state_id === stateId && asset.variant === "qualifying");
		if (!unresolved || !qualifying || !Array.isArray(unresolved.bbox)) {
			throw new Error(`${manifestPath}: state ${stateId} lacks a complete unresolved/qualifying asset pair`);
		}
		return {
			state_id: stateId,
			canvas_position: unresolved.bbox.slice(0, 2),
			sprite_names: {
				unresolved: unresolved.sprite_name,
				qualifying: qualifying.sprite_name,
			},
			runtime_dds: {
				unresolved: unresolved.dds,
				qualifying: qualifying.dds,
			},
		};
	});

	return {
		...manifest,
		schema: "chaos-redux-formable-state-puzzle/v1",
		decision_category: manifest.category_id,
		projection: { ...manifest.projection, canvas },
		state_policy: { required_state_ids: requiredStateIds },
		states,
		__path: manifestPath,
		__sourceSchema: "reviewed-legacy-assets/v1",
	};
}

function readManifests() {
	if (!fs.existsSync(manifestRoot)) {
		throw new Error(`Manifest root is missing: ${manifestRoot}`);
	}

	const manifests = [];
	for (const entry of fs.readdirSync(manifestRoot, { withFileTypes: true })) {
		if (!entry.isDirectory()) continue;
		const manifestPath = path.join(manifestRoot, entry.name, "manifest.json");
		if (!fs.existsSync(manifestPath)) continue;
		const rawManifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
		if (!rawManifest || typeof rawManifest !== "object" || Array.isArray(rawManifest)) {
			throw new Error(`${manifestPath}: manifest root must be an object`);
		}
		if (rawManifest.status && rawManifest.status !== "complete") continue;
		const manifest = normaliseManifest(rawManifest, manifestPath);
		manifests.push(manifest);
	}
	if (!manifests.length) {
		throw new Error(`No complete manifests found below ${manifestRoot}`);
	}
	const seenCategories = new Map();
	const seenFormables = new Map();
	for (const manifest of manifests) {
		const categoryKey = normalisedId(manifest.decision_category, `${manifest.__path}: decision_category`);
		const formableKey = normalisedId(manifest.formable_id, `${manifest.__path}: formable_id`);
		if (seenCategories.has(categoryKey)) throw new Error(`Duplicate normalized decision category manifest: ${manifest.decision_category} conflicts with ${seenCategories.get(categoryKey)}`);
		if (seenFormables.has(formableKey)) throw new Error(`Duplicate normalized formable manifest: ${manifest.formable_id} conflicts with ${seenFormables.get(formableKey)}`);
		seenCategories.set(categoryKey, manifest.decision_category);
		seenFormables.set(formableKey, manifest.formable_id);
	}

	return manifests.sort((left, right) => left.decision_category.localeCompare(right.decision_category));
}

function validateManifest(manifest) {
	if (manifest.schema !== "chaos-redux-formable-state-puzzle/v1") {
		throw new Error(`${manifest.__path}: unsupported schema ${manifest.schema}`);
	}
	normalisedId(manifest.formable_id, `${manifest.__path}: formable_id`);
	normalisedId(manifest.decision_category, `${manifest.__path}: decision_category`);
	if (!Array.isArray(manifest.states) || !manifest.states.length) {
		throw new Error(`${manifest.__path}: missing formable_id, decision_category, or states`);
	}
	if (manifest.territory_helper !== undefined && manifest.territory_helper !== null) {
		scriptIdentifier(manifest.territory_helper, `${manifest.__path}: territory_helper`);
	}
	if (
		!Array.isArray(manifest.projection?.canvas)
		|| manifest.projection.canvas.length !== 2
		|| !Number.isInteger(manifest.projection.canvas[0])
		|| !Number.isInteger(manifest.projection.canvas[1])
		|| manifest.projection.canvas[0] <= 0
		|| manifest.projection.canvas[1] <= 0
	) {
		throw new Error(`${manifest.__path}: runtime projection canvas must contain two positive integers`);
	}
	if (!Array.isArray(manifest.state_policy?.required_state_ids)) {
		throw new Error(`${manifest.__path}: state_policy.required_state_ids is missing`);
	}

	const ids = new Set();
	for (const state of manifest.states) {
		if (!state || typeof state !== "object" || !Number.isInteger(state.state_id) || state.state_id < 1) {
			throw new Error(`${manifest.__path}: state entries require positive integer state_id`);
		}
		if (ids.has(state.state_id)) throw new Error(`${manifest.__path}: duplicate state ${state.state_id}`);
		ids.add(state.state_id);
		if ("required" in state && typeof state.required !== "boolean") throw new Error(`${manifest.__path}: state ${state.state_id} required must be boolean`);
		if (state.required === false && !state.visibility_helper) throw new Error(`${manifest.__path}: optional state ${state.state_id} requires visibility_helper`);
		for (const field of ["qualification_helper", "visibility_helper"]) {
			if (field in state && state[field] !== null && state[field] !== undefined) scriptIdentifier(state[field], `${manifest.__path}: state ${state.state_id}.${field}`);
		}
		if (!Array.isArray(state.canvas_position) || state.canvas_position.length !== 2) {
			throw new Error(`${manifest.__path}: state ${state.state_id} lacks canvas_position`);
		}
		if (!state.canvas_position.every((value) => Number.isInteger(value))) {
			throw new Error(`${manifest.__path}: state ${state.state_id} canvas_position must contain integers`);
		}
		for (const variant of ["unresolved", "qualifying"]) {
			const runtimeDds = state.runtime_dds?.[variant];
			const sprite = state.sprite_names?.[variant];
			if (!runtimeDds || !sprite) throw new Error(`${manifest.__path}: state ${state.state_id} lacks ${variant} runtime data`);
			const absoluteDds = runtimePath(runtimeDds, `${manifest.__path}: state ${state.state_id}.${variant} runtime_dds`);
			if (!fs.existsSync(absoluteDds)) {
				throw new Error(`${manifest.__path}: runtime DDS is missing: ${runtimeDds}`);
			}
		}
	}
	const requiredStateIds = manifest.state_policy.required_state_ids;
	if (new Set(requiredStateIds).size !== requiredStateIds.length || requiredStateIds.some((stateId) => !Number.isInteger(stateId) || stateId < 1)) {
		throw new Error(`${manifest.__path}: required_state_ids must be unique positive integers`);
	}
	for (const requiredStateId of manifest.state_policy.required_state_ids) {
		if (!ids.has(requiredStateId)) throw new Error(`${manifest.__path}: required state ${requiredStateId} is not present in states`);
	}
}

function formableNames(manifest) {
	const formableKey = normalise(manifest.formable_id);
	const categoryKey = normalise(manifest.decision_category).replace(/_category$/, "");
	const scriptedGui = categoryKey.endsWith("_state")
		? `${categoryKey}_puzzle_scripted_gui`
		: `${categoryKey}_state_puzzle_scripted_gui`;
	return {
		formableKey,
		categoryKey,
		pascalKey: pascal(manifest.formable_id),
		window: `chaosx_formable_state_puzzle_${formableKey}_window`,
		scriptedGui,
		helperBase: `chaosx_formable_${formableKey}`,
		summaryKey: `chaosx_formable_state_puzzle_${formableKey}_summary`,
	};
}

function stateNames(manifest, state) {
	const form = formableNames(manifest);
	const stateId = state.state_id;
	return {
		element: `${form.formableKey}_state_${stateId}_piece`,
		hoverKey: `chaosx_formable_state_puzzle_${form.formableKey}_state_${stateId}_tt`,
		spriteFunction: `GetChaosxFormable${form.pascalKey}State${stateId}Sprite`,
		qualificationFunction: `GetChaosxFormable${form.pascalKey}State${stateId}Qualification`,
		wrapper: state.qualification_helper || `${form.helperBase}_state_${stateId}_qualifies`,
		visibilityHelper: state.visibility_helper || null,
	};
}

function generateGfx(manifests) {
	const lines = [
		"# ============================================================================",
		"# CHAOS REDUX - FORMABLE STATE-PUZZLE SPRITES",
		"# Generated from reviewed exact-geometry manifests; do not hand-edit entries.",
		"# ============================================================================",
		"",
		"spriteTypes = {",
	];
	for (const manifest of manifests) {
		lines.push(`\t# ${manifest.decision_category}`);
		for (const state of manifest.states) {
			for (const variant of ["unresolved", "qualifying"]) {
				lines.push("\tspriteType = {");
				lines.push(`\t\tname = ${quote(`GFX_${state.sprite_names[variant]}`)}`);
				lines.push(`\t\ttexturefile = ${quote(slash(state.runtime_dds[variant]))}`);
				lines.push("\t}");
			}
		}
	}
	lines.push("}", "");
	return lines.join("\n");
}

function generateGui(manifests) {
	const lines = [
		"# ============================================================================",
		"# CHAOS REDUX - FORMABLE STATE-PUZZLE WINDOWS",
		"# Generated from reviewed exact-geometry manifests; icons are informational.",
		"# ============================================================================",
		"",
		"guiTypes = {",
	];
	for (const manifest of manifests) {
		const form = formableNames(manifest);
		lines.push("\tcontainerWindowType = {");
		lines.push(`\t\tname = ${quote(form.window)}`);
		lines.push("\t\tposition = { x = 0 y = 0 }");
		lines.push(`\t\tsize = { width = 100% height = ${manifest.projection.canvas[1] + 26} }`);
		lines.push("\t\tclipping = yes");
		lines.push("");
		lines.push("\t\tinstantTextBoxType = {");
		lines.push(`\t\t\tname = ${quote(`${form.formableKey}_summary`)}`);
		lines.push("\t\t\tposition = { x = 0 y = 0 }");
		lines.push("\t\t\tfont = \"hoi_18mbs\"");
		lines.push(`\t\t\ttext = ${quote(form.summaryKey)}`);
		lines.push("\t\t\tformat = center");
		lines.push("\t\t\tmaxHeight = 22");
		lines.push(`\t\t\tmaxWidth = ${manifest.projection.canvas[0]}`);
		lines.push("\t\t}");
		lines.push("");
		lines.push("\t\tcontainerWindowType = {");
		lines.push(`\t\t\tname = ${quote(`${form.formableKey}_map`)}`);
		lines.push("\t\t\tposition = { x = 0 y = 24 }");
		lines.push(`\t\t\tsize = { width = ${manifest.projection.canvas[0]} height = ${manifest.projection.canvas[1]} }`);
		lines.push("\t\t\tclipping = yes");
		for (const state of manifest.states) {
			const names = stateNames(manifest, state);
			lines.push("");
			lines.push("\t\t\ticonType = {");
			lines.push(`\t\t\t\tname = ${quote(names.element)}`);
			lines.push(`\t\t\t\tposition = { x = ${state.canvas_position[0]} y = ${state.canvas_position[1]} }`);
			lines.push(`\t\t\t\tspriteType = ${quote(`GFX_${state.sprite_names.unresolved}`)}`);
			lines.push(`\t\t\t\tpdx_tooltip_delayed = ${quote(names.hoverKey)}`);
			lines.push("\t\t\t}");
		}
		lines.push("\t\t}");
		lines.push("\t}");
		lines.push("");
	}
	lines.push("}", "");
	return lines.join("\n");
}

function generateScriptedGui(manifests) {
	const lines = [
		"# ============================================================================",
		"# CHAOS REDUX - FORMABLE STATE-PUZZLE SCRIPTED GUI",
		"# Presentation reads live shared helpers; AI continues through decisions.",
		"# ============================================================================",
		"",
		"scripted_gui = {",
	];
	for (const manifest of manifests) {
		const form = formableNames(manifest);
		lines.push(`\t${form.scriptedGui} = {`);
		lines.push("\t\tcontext_type = decision_category");
		lines.push(`\t\twindow_name = ${quote(form.window)}`);
		lines.push("\t\tvisible = { is_ai = no }");
		lines.push("\t\tproperties = {");
		const hasVisibilityHooks = manifest.states.some((state) => state.visibility_helper);
		for (const state of manifest.states) {
			const names = stateNames(manifest, state);
			lines.push(`\t\t\t${names.element} = {`);
			lines.push(`\t\t\t\timage = ${quote(`[${names.spriteFunction}]`)}`);
			lines.push("\t\t\t}");
			if (hasVisibilityHooks) {
				lines.push(`\t\t\t${names.element}_visible = {`);
				if (state.required || !names.visibilityHelper) {
					lines.push("\t\t\t\talways = yes");
				} else {
					lines.push(`\t\t\t\t${names.visibilityHelper} = yes`);
				}
				lines.push("\t\t\t}");
			}
		}
		lines.push("\t\t}");
		lines.push("\t\tai_enabled = { always = no }");
		lines.push("\t}");
		lines.push("");
	}
	lines.push("}", "");
	return lines.join("\n");
}

function generateScriptedLocalisation(manifests) {
	const lines = [
		"# ============================================================================",
		"# CHAOS REDUX - FORMABLE STATE-PUZZLE SCRIPTED LOCALISATION",
		"# Supplies live sprite, owner, controller, control, core, and summary state.",
		"# ============================================================================",
		"",
	];
	const uniqueStates = new Set();

	for (const manifest of manifests) {
		const form = formableNames(manifest);
		for (const state of manifest.states) {
			uniqueStates.add(state.state_id);
			const names = stateNames(manifest, state);
			lines.push("defined_text = {");
			lines.push(`\tname = ${names.spriteFunction}`);
			lines.push("\ttext = {");
			lines.push(`\t\ttrigger = { ${names.wrapper} = yes }`);
			lines.push(`\t\tlocalization_key = ${quote(`GFX_${state.sprite_names.qualifying}`)}`);
			lines.push("\t}");
			lines.push("\ttext = {");
			lines.push("\t\ttrigger = { always = yes }");
			lines.push(`\t\tlocalization_key = ${quote(`GFX_${state.sprite_names.unresolved}`)}`);
			lines.push("\t}");
			lines.push("}", "");
			lines.push("defined_text = {");
			lines.push(`\tname = ${names.qualificationFunction}`);
			lines.push("\ttext = {");
			lines.push(`\t\ttrigger = { ${names.wrapper} = yes }`);
			lines.push("\t\tlocalization_key = chaosx_formable_state_puzzle_status_qualifying");
			lines.push("\t}");
			lines.push("\ttext = {");
			lines.push("\t\ttrigger = { always = yes }");
			lines.push("\t\tlocalization_key = chaosx_formable_state_puzzle_status_unresolved");
			lines.push("\t}");
			lines.push("}", "");
		}
		lines.push("defined_text = {");
		lines.push(`\tname = GetChaosxFormable${form.pascalKey}QualifyingCount`);
		const optionalVisibleStates = manifest.states.filter((state) => !state.required && state.visibility_helper);
		for (let count = manifest.states.length; count > 0; count--) {
			lines.push("\ttext = {");
			lines.push("\t\ttrigger = {");
			lines.push("\t\t\tcount_triggers = {");
			lines.push(`\t\t\t\tamount > ${count - 1}`);
			for (const countedState of manifest.states) {
				const countedNames = stateNames(manifest, countedState);
				if (!countedState.required && countedNames.visibilityHelper) {
					lines.push(`\t\t\t\tAND = { ${countedNames.visibilityHelper} = yes ${countedNames.wrapper} = yes }`);
				} else {
					lines.push(`\t\t\t\t${countedNames.wrapper} = yes`);
				}
			}
			lines.push("\t\t\t}");
			lines.push("\t\t}");
			lines.push(`\t\tlocalization_key = chaosx_formable_state_puzzle_count_${count}`);
			lines.push("\t}");
		}
		lines.push("\ttext = {");
		lines.push("\t\ttrigger = { always = yes }");
		lines.push("\t\tlocalization_key = chaosx_formable_state_puzzle_count_0");
		lines.push("\t}");
		lines.push("}", "");
		if (optionalVisibleStates.length) {
			lines.push("defined_text = {");
			lines.push(`\tname = GetChaosxFormable${form.pascalKey}RelevantCount`);
			for (let count = optionalVisibleStates.length + manifest.states.filter((state) => state.required).length; count > 0; count--) {
				lines.push("\ttext = {");
				lines.push("\t\ttrigger = {");
				lines.push("\t\t\tcount_triggers = {");
				lines.push(`\t\t\t\tamount > ${count - 1}`);
				for (const countedState of manifest.states) {
					const countedNames = stateNames(manifest, countedState);
					if (!countedState.required && countedNames.visibilityHelper) {
						lines.push(`\t\t\t\t${countedNames.visibilityHelper} = yes`);
					} else {
						lines.push("\t\t\t\talways = yes");
					}
				}
				lines.push("\t\t\t}");
				lines.push("\t\t}");
				lines.push(`\t\tlocalization_key = chaosx_formable_state_puzzle_count_${count}`);
				lines.push("\t}");
			}
			lines.push("\ttext = {");
			lines.push("\t\ttrigger = { always = yes }");
			lines.push("\t\tlocalization_key = chaosx_formable_state_puzzle_count_0");
			lines.push("\t}");
			lines.push("}", "");
		}
		lines.push("defined_text = {");
		lines.push(`\tname = GetChaosxFormable${form.pascalKey}SummaryStatus`);
		lines.push("\ttext = {");
		lines.push(`\t\ttrigger = { ${manifest.territory_helper || `${form.helperBase}_territory_qualifies`} = yes }`);
		lines.push("\t\tlocalization_key = chaosx_formable_state_puzzle_summary_ready");
		lines.push("\t}");
		lines.push("\ttext = {");
		lines.push("\t\ttrigger = { always = yes }");
		lines.push("\t\tlocalization_key = chaosx_formable_state_puzzle_summary_incomplete");
		lines.push("\t}");
		lines.push("}", "");
	}

	for (const stateId of [...uniqueStates].sort((left, right) => left - right)) {
		for (const [suffix, scope, presentKey, absentKey] of [
			["Owner", "owner", `chaosx_formable_state_puzzle_state_${stateId}_owner`, "chaosx_formable_state_puzzle_no_owner"],
			["Controller", "controller", `chaosx_formable_state_puzzle_state_${stateId}_controller`, "chaosx_formable_state_puzzle_no_controller"],
		]) {
			lines.push("defined_text = {");
			lines.push(`\tname = GetChaosxFormableState${stateId}${suffix}`);
			lines.push("\ttext = {");
			lines.push(`\t\ttrigger = { ${stateId} = { ${scope} = { exists = yes } } }`);
			lines.push(`\t\tlocalization_key = ${presentKey}`);
			lines.push("\t}");
			lines.push("\ttext = {");
			lines.push("\t\ttrigger = { always = yes }");
			lines.push(`\t\tlocalization_key = ${absentKey}`);
			lines.push("\t}");
			lines.push("}", "");
		}
		lines.push("defined_text = {");
		lines.push(`\tname = GetChaosxFormableState${stateId}CoreStatus`);
		lines.push("\ttext = {");
		lines.push(`\t\ttrigger = { ${stateId} = { is_core_of = ROOT } }`);
		lines.push("\t\tlocalization_key = chaosx_formable_state_puzzle_core_yes");
		lines.push("\t}");
		lines.push("\ttext = {");
		lines.push("\t\ttrigger = { always = yes }");
		lines.push("\t\tlocalization_key = chaosx_formable_state_puzzle_core_no");
		lines.push("\t}");
		lines.push("}", "");
	}

	return lines.join("\n");
}

function generateLocalisation(manifests) {
	const lines = [
		"l_english:",
		"chaosx_formable_state_puzzle_status_qualifying: \"§GQualifying§!\"",
		"chaosx_formable_state_puzzle_status_unresolved: \"§YUnresolved§!\"",
		"chaosx_formable_state_puzzle_core_yes: \"§GYes§!\"",
		"chaosx_formable_state_puzzle_core_no: \"§YNo§!\"",
		"chaosx_formable_state_puzzle_no_owner: \"No owner\"",
		"chaosx_formable_state_puzzle_no_controller: \"No controller\"",
		"chaosx_formable_state_puzzle_summary_ready: \"§GFormation ready§!\"",
		"chaosx_formable_state_puzzle_summary_incomplete: \"§YRequirements incomplete§!\"",
	];
	const maximumCount = Math.max(...manifests.map((manifest) => manifest.states.length));
	for (let count = 0; count <= maximumCount; count++) {
		lines.push(`chaosx_formable_state_puzzle_count_${count}: \"${count}\"`);
	}
	const uniqueStates = new Set();
	for (const manifest of manifests) {
		const form = formableNames(manifest);
		lines.push(`${form.summaryKey}: \"Qualifying states: §Y[GetChaosxFormable${form.pascalKey}QualifyingCount] / ${manifest.states.length}§! — [GetChaosxFormable${form.pascalKey}SummaryStatus]\"`);
		for (const state of manifest.states) {
			uniqueStates.add(state.state_id);
			const names = stateNames(manifest, state);
			lines.push(`${names.hoverKey}: \"§Y[${state.state_id}.GetName]§!\\nOwner: [GetChaosxFormableState${state.state_id}Owner]\\nController: [GetChaosxFormableState${state.state_id}Controller]\\nRequired control: [${names.qualificationFunction}]\\nOur core: [GetChaosxFormableState${state.state_id}CoreStatus]\"`);
		}
	}
	for (const stateId of [...uniqueStates].sort((left, right) => left - right)) {
		lines.push(`chaosx_formable_state_puzzle_state_${stateId}_owner: \"[${stateId}.owner.GetNameWithFlag]\"`);
		lines.push(`chaosx_formable_state_puzzle_state_${stateId}_controller: \"[${stateId}.controller.GetNameWithFlag]\"`);
	}
	for (const manifest of manifests) {
		if (!manifest.states.some((state) => !state.required && state.visibility_helper)) continue;
		const form = formableNames(manifest);
		const index = lines.findIndex((line) => line.startsWith(`${form.summaryKey}:`));
		if (index >= 0) lines[index] = lines[index].replace(` / ${manifest.states.length}`, ` / [GetChaosxFormable${form.pascalKey}RelevantCount]`);
	}
	lines.push("");
	return `\uFEFF${lines.join("\n")}`;
}

function write(relativePath, source) {
	const absolutePath = path.join(workspace, relativePath);
	fs.mkdirSync(path.dirname(absolutePath), { recursive: true });
	fs.writeFileSync(absolutePath, source, "utf8");
}

const manifests = readManifests();
for (const manifest of manifests) validateManifest(manifest);

write("interface/chaosx_formable_state_puzzles.gfx", generateGfx(manifests));
for (const manifest of manifests) {
	write(`interface/chaosx_formable_state_puzzle_${formableNames(manifest).formableKey}.gui`, generateGui([manifest]));
}
write("common/scripted_guis/chaosx_formable_state_puzzles.txt", generateScriptedGui(manifests));
write("common/scripted_localisation/chaosx_formable_state_puzzles.txt", generateScriptedLocalisation(manifests));
write("localisation/english/chaosx_formable_state_puzzles_l_english.yml", generateLocalisation(manifests));

const stateEntries = manifests.reduce((count, manifest) => count + manifest.states.length, 0);
process.stdout.write(`Generated ${manifests.length} formable state puzzles with ${stateEntries} state-piece entries.\n`);
