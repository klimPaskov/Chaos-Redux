"""Reuse identical accepted facility scenarios to check this syntax repair."""
from pathlib import Path
import copy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
previous = ROOT / 'docs/testing/runtime_repairs/20260913_cxt_history_followup/facility_probability_corrected'
pool = json.loads((previous / 'manifest_after.json').read_text(encoding='utf-8-sig'))
out = QA / 'facility_probability'
out.mkdir(exist_ok=True)
for phase in ('before', 'after'):
    manifest = copy.deepcopy(pool)
    manifest['id'] = f'cxt_facility_parameter_syntax_repair_{phase}_20260913'
    manifest['description'] = ('Uniform owned campus selection under unchanged intended predicates. '
        'The baseline source contained unsupported placeholders; this declared model is not a claim '
        'that the baseline loaded in HOI4. Native construction legality is explicit scenario input. '
        'Foreign candidate search and engine execution are outside this adapter.')
    (out / f'manifest_{phase}.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
(out / 'scenarios.json').write_bytes((previous / 'scenarios.json').read_bytes())
sources = {}
for name in ('common/scripted_effects/chaosx_test_country_effects.txt', 'common/scripted_triggers/chaosx_test_country_triggers.txt'):
    sources[name] = {phase: hashlib.sha256((QA / 'baseline' / name if phase == 'before' else ROOT / name).read_bytes()).hexdigest() for phase in ('before', 'after')}
(out / 'source_provenance.json').write_text(json.dumps(sources, indent=2) + '\n', encoding='utf-8')
print('Identical candidate semantics and scenario inputs prepared.')
