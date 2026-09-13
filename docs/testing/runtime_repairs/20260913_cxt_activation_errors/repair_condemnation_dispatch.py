"""Preserve condemnation ledgers while deferring dormant CXT world consumers."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent
names = ('common/scripted_effects/condemnation_sanctions_effects.txt', 'common/scripted_effects/chaosx_test_country_effects.txt', 'docs/testing/chaosx_test_country.md', 'docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md')
hashes = {}
for name in names:
    raw = (ROOT / name).read_bytes()
    dest = QA / 'baseline' / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    assert not dest.exists()
    dest.write_bytes(raw)
    hashes[name] = hashlib.sha256(raw).hexdigest()
(QA / 'condemnation_before_hashes.json').write_bytes((json.dumps(hashes, indent=2) + '\n').encode('utf-8'))

name = names[0]
raw = (ROOT / name).read_bytes()
text = raw.decode('utf-8-sig').replace('\r\n', '\n')
for helper, flag in (('condemnation_recalculate_participants', 'condemnation_participant_refresh_pending'), ('condemnation_start_targeted_pulse', 'condemnation_targeted_pulse_pending')):
    signature = helper + ' = {'
    assert text.count(signature) == 1
    wrapper = f'''# Country scope. Preserve the requested refresh until dormant CXT has a capital.
{helper} = {{
	if = {{
		limit = {{ tag = CXT NOT = {{ any_owned_state = {{ is_capital = yes }} }} }}
		set_country_flag = {flag}
	}}
	else = {{ {helper}_apply = yes }}
}}

{helper}_apply = {{'''
    text = text.replace(signature, wrapper, 1)
flush = '''# Country scope. Inputs: queued refresh flags; no refresh is discarded.
# CXT setup and its registered-content bus call this after capital activation.
condemnation_flush_deferred_refresh = {
	if = {
		limit = { any_owned_state = { is_capital = yes } }
		if = {
			limit = { has_country_flag = condemnation_participant_refresh_pending }
			clr_country_flag = condemnation_participant_refresh_pending
			condemnation_recalculate_participants = yes
		}
		if = {
			limit = { has_country_flag = condemnation_targeted_pulse_pending }
			clr_country_flag = condemnation_targeted_pulse_pending
			condemnation_start_targeted_pulse = yes
		}
	}
}

'''
text = text.replace('condemnation_start_targeted_pulse = {', flush + 'condemnation_start_targeted_pulse = {', 1)
encoded = text.encode('utf-8')
if raw.startswith(b'\xef\xbb\xbf'):
    encoded = b'\xef\xbb\xbf' + encoded
if b'\r\n' in raw:
    encoded = encoded.replace(b'\n', b'\r\n')
(ROOT / name).write_bytes(encoded)

name = names[1]
raw = (ROOT / name).read_bytes()
text = raw.decode('utf-8-sig').replace('\r\n', '\n')
for helper in ('chaosx_test_country_initial_setup', 'chaosx_test_country_sync_registered_content'):
    signature = helper + ' = {\n'
    assert text.count(signature) == 1
    text = text.replace(signature, signature + '\tcondemnation_flush_deferred_refresh = yes\n', 1)
encoded = text.encode('utf-8')
if raw.startswith(b'\xef\xbb\xbf'):
    encoded = b'\xef\xbb\xbf' + encoded
if b'\r\n' in raw:
    encoded = encoded.replace(b'\n', b'\r\n')
(ROOT / name).write_bytes(encoded)
print('Dormant CXT participant and pulse requests preserved for valid-capital activation.')
