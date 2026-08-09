#!/usr/bin/env node

// Generates the runtime GUI, GFX, scripted-GUI, scripted-localisation, and
// English localisation surfaces from reviewed exact-geometry manifests.
// The generated files are committed; this script keeps future map rebuilds
// reproducible and fails closed when a selected category lacks a manifest.

import fs from "node:fs";
import path from "node:path";

const workspace = process.cwd();
const manifestRoot = path.join(workspace, "docs", "formables", "state_puzzles");

const selectedCategories = new Set([
	"form_scandinavia_category",
	"form_north_sea_category",
	"form_baltic_sea_empire_category",
	"form_gran_colombia_category",
	"form_commonwealth_category",
	"form_united_netherlands_category",
	"form_baltic_federation_category",
	"form_mutapa_category",
	"form_rattanakosin_kingdom_category",
	"form_turkestan_category",
	"form_mountainous_republic_category",
	"form_idel_ural_category",
	"greater_italy_category",
	"form_sweden_hungary_category",
	"latin_africa_category",
	"neo_assyrian_empire_category",
	"neo_mesopotamia_category",
	"maghreb_formable_category",
	"greater_mongolia_category",
	"greater_hui_state_category",
	"GOE_form_hindustan_category",
]);

const normalise = (value) => value.replace(/[^A-Za-z0-9_]/g, "_").toLowerCase();
const pascal = (value) => normalise(value).split("_").filter(Boolean).map((part) => part[0].toUpperCase() + part.slice(1)).join("");
const slash = (value) => value.replaceAll("\\", "/");
const quote = (value) => `"${value}"`;

function normaliseManifest(manifest, manifestPath) {
	if (manifest.schema === "chaos-redux-formable-state-puzzle/v1") {
		return { ...manifest, __path: manifestPath, __sourceSchema: manifest.schema };
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
		const manifest = normaliseManifest(JSON.parse(fs.readFileSync(manifestPath, "utf8")), manifestPath);
		if (selectedCategories.has(manifest.decision_category)) manifests.push(manifest);
	}

	const seenCategories = new Set(manifests.map((manifest) => manifest.decision_category));
	const missing = [...selectedCategories].filter((category) => !seenCategories.has(category));
	if (missing.length) {
		throw new Error(`Selected categories are missing reviewed manifests: ${missing.join(", ")}`);
	}

	if (manifests.length !== selectedCategories.size) {
		throw new Error(`Expected ${selectedCategories.size} selected manifests, found ${manifests.length}`);
	}

	return manifests.sort((left, right) => left.decision_category.localeCompare(right.decision_category));
}

function validateManifest(manifest) {
	if (manifest.schema !== "chaos-redux-formable-state-puzzle/v1") {
		throw new Error(`${manifest.__path}: unsupported schema ${manifest.schema}`);
	}
	if (!manifest.formable_id || !manifest.decision_category || !Array.isArray(manifest.states)) {
		throw new Error(`${manifest.__path}: missing formable_id, decision_category, or states`);
	}
	if (manifest.projection?.canvas?.[0] !== 440 || manifest.projection?.canvas?.[1] !== 180) {
		throw new Error(`${manifest.__path}: runtime projection must be 440x180`);
	}
	if (manifest.states.length !== manifest.state_policy?.required_state_ids?.length) {
		throw new Error(`${manifest.__path}: states and required_state_ids differ`);
	}

	const ids = new Set();
	for (const state of manifest.states) {
		if (ids.has(state.state_id)) throw new Error(`${manifest.__path}: duplicate state ${state.state_id}`);
		ids.add(state.state_id);
		if (!Array.isArray(state.canvas_position) || state.canvas_position.length !== 2) {
			throw new Error(`${manifest.__path}: state ${state.state_id} lacks canvas_position`);
		}
		for (const variant of ["unresolved", "qualifying"]) {
			const runtimePath = state.runtime_dds?.[variant];
			const sprite = state.sprite_names?.[variant];
			if (!runtimePath || !sprite) throw new Error(`${manifest.__path}: state ${state.state_id} lacks ${variant} runtime data`);
			if (!fs.existsSync(path.join(workspace, runtimePath))) {
				throw new Error(`${manifest.__path}: runtime DDS is missing: ${runtimePath}`);
			}
		}
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
		wrapper: `${form.helperBase}_state_${stateId}_qualifies`,
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
		lines.push("\t\tsize = { width = 100% height = 206 }");
		lines.push("\t\tclipping = yes");
		lines.push("");
		lines.push("\t\tinstantTextBoxType = {");
		lines.push(`\t\t\tname = ${quote(`${form.formableKey}_summary`)}`);
		lines.push("\t\t\tposition = { x = 0 y = 0 }");
		lines.push("\t\t\tfont = \"hoi_18mbs\"");
		lines.push(`\t\t\ttext = ${quote(form.summaryKey)}`);
		lines.push("\t\t\tformat = center");
		lines.push("\t\t\tmaxHeight = 22");
		lines.push("\t\t\tmaxWidth = 440");
		lines.push("\t\t}");
		lines.push("");
		lines.push("\t\tcontainerWindowType = {");
		lines.push(`\t\t\tname = ${quote(`${form.formableKey}_map`)}`);
		lines.push("\t\t\tposition = { x = 0 y = 24 }");
		lines.push("\t\t\tsize = { width = 440 height = 180 }");
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
		for (const state of manifest.states) {
			const names = stateNames(manifest, state);
			lines.push(`\t\t\t${names.element} = {`);
			lines.push(`\t\t\t\timage = ${quote(`[${names.spriteFunction}]`)}`);
			lines.push("\t\t\t}");
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
		for (let count = manifest.states.length; count > 0; count--) {
			lines.push("\ttext = {");
			lines.push("\t\ttrigger = {");
			lines.push("\t\t\tcount_triggers = {");
			lines.push(`\t\t\t\tamount > ${count - 1}`);
			for (const countedState of manifest.states) {
				lines.push(`\t\t\t\t${stateNames(manifest, countedState).wrapper} = yes`);
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
		lines.push("defined_text = {");
		lines.push(`\tname = GetChaosxFormable${form.pascalKey}SummaryStatus`);
		lines.push("\ttext = {");
		lines.push(`\t\ttrigger = { ${form.helperBase}_territory_qualifies = yes }`);
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
