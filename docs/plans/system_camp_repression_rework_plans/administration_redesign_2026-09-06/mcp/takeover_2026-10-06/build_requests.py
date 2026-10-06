import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ctx = json.loads((HERE / 'event_reference_context.json').read_text())['structuredContent']['data']['sections']
requests = []
for i, (section, start, count) in enumerate(((ctx[0], 6404, 20), (ctx[1], 2320, 39), (ctx[5], 425, 24), (ctx[4], 40, 70))):
    requests.append({'name': 'hoi4.reference_read', 'arguments': {'workspaceId': 'camp_origin_architecture_oct3', 'id': section['id'], 'revision': section['revision'], 'startLine': start, 'maxLines': count}, 'output': str(HERE / ('reference_read_%s.json' % i))})
requests.extend([
    {'name': 'hoi4.source_lookup', 'arguments': {'workspaceId': 'camp_origin_architecture_oct3', 'symbol': 'GER_generalgouvernement', 'includeReferences': False, 'maxLines': 50}, 'output': str(HERE / 'vanilla_gen_source.json')},
    {'name': 'hoi4.event_inspect', 'arguments': {'workspaceId': 'camp_origin_architecture_oct3', 'mode': 'lint', 'selector': {'kind': 'event', 'eventId': 'camp_occ_partner.3'}, 'maxNodes': 10, 'maxDepth': 2, 'maxEdges': 15}, 'output': str(HERE / 'partner_event_lint.json')},
    {'name': 'hoi4.event_render', 'arguments': {'workspaceId': 'camp_origin_architecture_oct3', 'view': 'options', 'selector': {'kind': 'event', 'eventId': 'camp_occ_partner.3'}, 'maxNodes': 10, 'maxDepth': 2}, 'output': str(HERE / 'partner_event_render.json')},
    {'name': 'hoi4.script_validate', 'arguments': {'workspaceId': 'camp_origin_architecture_oct3', 'scope': 'country', 'kind': 'trigger', 'source': 'set_temp_variable = { camp_occ_order_sy = 1942 } meta_trigger = { text = { NOT = { date < "[SY].3.25" } date < "1942.10.21" } SY = "[?camp_occ_order_sy|.0]" }', 'limit': 12}, 'output': str(HERE / 'window_validation.json')},
])
(HERE / 'requests_source.json').write_text(json.dumps(requests, indent=2))

import subprocess
graph = json.loads((HERE / 'event-options-05d44b40df4d.json').read_text())
comparison = {'name': 'hoi4.event_compare', 'arguments': {
    'workspaceId': 'camp_origin_architecture_oct3',
    'before': {'revision': graph['graphRevision']},
    'selector': {'kind': 'namespace', 'namespace': 'camp_occ_partner'},
    'proposedSources': [{'relativePath': 'events/camp_occ_partner_events.txt', 'source': subprocess.check_output(['git', 'show', 'HEAD:events/camp_occ_partner_events.txt']).decode()}],
    'render': False, 'maxChainNodes': 15, 'refresh': False,
}, 'output': str(HERE / 'event_compare_inverse_to_head.json')}
(HERE / 'requests_compare.json').write_text(json.dumps([comparison], indent=2))

fixture = json.loads((HERE.parent / 'current_render_2026-10-04/records_ger_1945_05_01_full.json').read_text())
fixture['id'] = 'takeover_records_after'
fixture['lists']['camp_admin_history_list'][0]['GetCampAdminHistoryKind'] = 'Deportation trains halted'
fixture['lists']['camp_admin_history_list'][0]['GetCampAdminHistoryPlace'] = 'Bratislava'
fixture.pop('resolution', None)
fixture.pop('uiScale', None)
after = [{'name': 'hoi4.gui_inspect', 'arguments': {'workspaceId': 'camp_origin_architecture_oct3', 'windowName': 'repression_ledger_window', 'scenario': fixture}, 'output': str(HERE / 'records_after_inspect.json')},
         {'name': 'hoi4.gui_render', 'arguments': {'workspaceId': 'camp_origin_architecture_oct3', 'windowName': 'repression_ledger_window', 'scenario': fixture, 'resolutions': [{'width': 1280, 'height': 720, 'uiScale': 1}, {'width': 1920, 'height': 1080, 'uiScale': 1}, {'width': 1920, 'height': 1080, 'uiScale': 1.25}]}, 'output': str(HERE / 'records_after_render.json')}]
(HERE / 'requests_after.json').write_text(json.dumps(after, indent=2))
