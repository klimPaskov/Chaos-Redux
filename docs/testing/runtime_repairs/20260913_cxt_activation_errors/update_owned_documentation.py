"""Apply exact owned documentation edits while preserving existing file bytes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
QA = Path(__file__).resolve().parent

def replace_once(name, old, new):
    path = ROOT / name
    raw = path.read_bytes()
    ending = b'\r\n' if b'\r\n' in raw else b'\n'
    old_raw = old.encode('utf-8').replace(b'\n', ending)
    new_raw = new.encode('utf-8').replace(b'\n', ending)
    assert raw.count(old_raw) == 1, name
    path.write_bytes(raw.replace(old_raw, new_raw, 1))

replace_once('docs/testing/chaosx_test_country.md',
    'The technology helper enumerates `global.technology` and passes its database objects to native `var:` technology fields with `popup = no`.\nThe supplied error report leaves one rejected object unidentified; temporary `CXT_TECH_DIAGNOSTIC` output records the database count, index, numeric value, and token text so that failure can be traced without using token text as executable technology script.',
    'The technology helper captures `global.technology^num`, reads every zero-based index below that count explicitly, and passes each database object to native `var:` technology fields with `popup = no`.\nAn empty database produces no technology reads, and the numeric loop has its own initialized break variable.\nTemporary `CXT_TECH_DIAGNOSTIC` output records the count, index, numeric value, and token text; the supplied error report does not include those values, so runtime error elimination remains unverified.')
replace_once('docs/testing/chaosx_test_country.md',
    'Core and registered project grants are idempotent and use `chaosx_test_country_silent_unlocks` to suppress completion reports while retaining their gameplay outputs.',
    "Core and registered project grants are idempotent and use `chaosx_test_country_silent_unlocks` to suppress completion reports while retaining their gameplay outputs.\nProject condemnation gains remain in CXT's country record during dormant history setup; participant calculations and pulse scheduling wait until it has an owned capital.\nInitialization and the existing registered-content bus flush the queued requests after activation, so scoring has valid capital and initialized-country scopes without repeating project completion.")
replace_once('docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md',
    '## Data model\n',
    '''## Data model

### Dormant test-country activation

Dormant CXT history unlocks retain their condemnation source records, totals, tiers, and project outputs.
`condemnation_recalculate_participants` and `condemnation_start_targeted_pulse` queue their requests through `condemnation_participant_refresh_pending` and `condemnation_targeted_pulse_pending` while CXT has no owned capital.
Their `_apply` helpers retain the ordinary participant calculations, AI strategy values, native embargo ownership, and pulse timing.
`condemnation_flush_deferred_refresh` runs through CXT initialization and its registered-content bus after capital activation, clears each queued flag before dispatch, and leaves it queued while no capital exists.
Ordinary countries continue through the same immediate helpers.
''')

name = '.agents/skills/chaos-redux-events/SKILL.md'
baseline = QA / 'baseline' / name
baseline.parent.mkdir(parents=True, exist_ok=True)
assert not baseline.exists()
baseline.write_bytes((ROOT / name).read_bytes())
replace_once(name, '### 7. Duration fields and constants\n',
    '''History grants can run before the recipient has a capital or other countries are initialized.
Keep their local grants and records, but queue capital-dependent scoring and diplomatic refreshes until country activation rather than dropping gameplay outputs.
Guard capital entry with an owned-state capital check; entering `capital_scope` to test whether it exists can itself raise an invalid-target error.

### 7. Duration fields and constants
''')
print('Updated indexed-grant, deferred-refresh, and reusable history guidance.')
