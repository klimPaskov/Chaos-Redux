// Shared Clausewitz source helpers for the maintained Event 012 and Event 033 JS tests.
// The functions are copied unchanged from the Event 033 caller-repair test of 3 October 2026
// (docs/plans/033_acid_rain_plans/validation/caller_repairs_source_tests_2026_10_03.js), which
// stays in its plan folder as a historical record. Requiring this module reads two script-constant
// files from the mod root (the current working directory) and writes nothing.
const fs = require('fs');
const crypto = require('crypto');
const assert = require('assert/strict');
const hash = value => crypto.createHash('sha256').update(value).digest('hex');

function parse(text) {
	const tokens = text.replace(/#[^\r\n]*/g, '').match(/"(?:\\.|[^"\\])*"|[{}=<>]|[^\s{}=<>]+/g) || [];
	let i = 0;
	function body(nested = false) {
		const nodes = [];
		while (i < tokens.length && tokens[i] !== '}') {
			const key = tokens[i++];
			if (key === '{') {
				nodes.push({ key: '__anonymous', op: '=', value: body(true) });
				continue;
			}
			if (!['=', '<', '>'].includes(tokens[i])) {
				nodes.push({ key: '__atom', op: '=', value: key });
				continue;
			}
			const op = tokens[i++];
			let value = tokens[i++];
			if (value === '{') value = body(true);
			nodes.push({ key, op, value });
		}
		if (nested) assert.equal(tokens[i++], '}');
		return nodes;
	}
	return body();
}

function namedBlock(text, name) {
	const found = new RegExp('^' + name + '\\s*=\\s*\\{', 'm').exec(text);
	assert.ok(found, 'missing named block ' + name);
	let depth = 0, quoted = false, comment = false;
	for (let i = found.index + found[0].indexOf('{'); i < text.length; i++) {
		const c = text[i];
		if (c === '\n') comment = false;
		if (comment) continue;
		if (!quoted && c === '#') { comment = true; continue; }
		if (c === '"' && text[i - 1] !== '\\') { quoted = !quoted; continue; }
		if (quoted) continue;
		if (c === '{') depth++;
		if (c === '}' && --depth === 0) return text.slice(found.index, i + 1);
	}
	throw Error('unclosed block ' + name);
}

const constants = new Map();
for (const filename of ['chaos_meter_constants.txt', 'humanitarian_runtime_constants.txt']) {
	for (const category of parse(fs.readFileSync('common/script_constants/' + filename, 'utf8'))) {
		if (!Array.isArray(category.value)) continue;
		for (const entry of category.value) {
			if (!Array.isArray(entry.value) && Number.isFinite(Number(entry.value)))
				constants.set('constant:' + category.key + '.' + entry.key, Number(entry.value));
		}
	}
}

function assignment(node) {
	assert.ok(Array.isArray(node.value));
	const explicit = node.value.find(n => n.key === 'var');
	return explicit ? [explicit.value, node.value.find(n => n.key === 'value').value]
		: [node.value[0].key, node.value[0].value];
}

module.exports = { parse, namedBlock, assignment, constants, hash };
