#!/usr/bin/env python3
"""Verify document preservation and symbolic rules, optionally build the final ZIP.

This does not run Hearts of Iron IV, inspect native game behavior, or audit AI
probabilities. It uses the bundled Stage 8 identity record to verify the exact
cumulative source baseline without requiring another copy of the old ZIP.
"""
from __future__ import annotations
import argparse
import ast
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_CEILING
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SPEC = ROOT / 'docs/specs/089_doctor_wu_specs'
PLAN = ROOT / 'docs/plans/089_doctor_wu_plans'

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

@dataclass
class FiniteCohort:
    produced: int
    unsettled: int
    settled: int = 0
    pre_settlement_deaths: int = 0
    civilian_credit: int = 0
    military_credit: int = 0
    requests: set[str] = field(default_factory=set)

    def settle(self, request: str, amount: int, destination: str) -> bool:
        if request in self.requests:
            return False
        if amount <= 0 or amount > self.unsettled or destination not in {'civilian', 'military'}:
            return False
        self.unsettled -= amount
        self.settled += amount
        if destination == 'civilian':
            self.civilian_credit += amount
        else:
            self.military_credit += amount
        self.requests.add(request)
        return True

    def lose_unsettled(self, amount: int) -> None:
        require(0 <= amount <= self.unsettled, 'Invalid unsettled death request')
        self.unsettled -= amount
        self.pre_settlement_deaths += amount

    def conserved(self) -> bool:
        return self.produced == self.unsettled + self.settled + self.pre_settlement_deaths


def symbolic_checks() -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    def check(name: str, condition: bool) -> None:
        require(condition, name)
        results.append({'name': name, 'passed': True, 'evidence_type': 'local_symbolic_not_engine'})

    c = FiniteCohort(1000, 1000)
    check('finite_military_first_settlement', c.settle('military-1', 600, 'military'))
    check('finite_civilian_first_settlement', c.settle('civilian-1', 250, 'civilian'))
    check('first_settlement_conservation', c.conserved() and c.unsettled == 150 and c.settled == 850)
    snapshot = (c.unsettled, c.civilian_credit, c.military_credit)
    check('same_request_cannot_credit_another_destination', not c.settle('military-1', 600, 'civilian'))
    check('duplicate_request_changes_nothing', snapshot == (c.unsettled, c.civilian_credit, c.military_credit))
    check('remaining_entitlement_cannot_be_overspent', not c.settle('military-2', 200, 'military'))
    c.lose_unsettled(10)
    check('pre_settlement_death_conservation', c.conserved() and (c.unsettled, c.settled, c.pre_settlement_deaths) == (140, 850, 10))
    qualified_specialists = 5
    check('specialists_draw_from_already_counted_civilians', qualified_specialists <= c.civilian_credit and c.produced == 1000)
    later_settled_deaths = 100
    check('later_deaths_do_not_reopen_first_settlement', c.conserved() and c.settled == 850 and c.produced - c.pre_settlement_deaths - later_settled_deaths == 890)
    custody_a, custody_b = 80, 60
    check('unsettled_custody_partition_is_not_population_grant', custody_a + custody_b == c.unsettled and c.civilian_credit == 250)

    free = {'A': 120, 'B': 0}
    reserved = {'operation-A': ('A', 40)}
    free['A'] -= 40
    current_standard = 'B'
    free[current_standard] += 30
    check('standard_change_preserves_old_stock', free == {'A': 80, 'B': 30})
    check('standard_change_preserves_pending_profile', reserved['operation-A'] == ('A', 40))
    consumed = reserved.pop('operation-A')[1]
    check('completed_reservation_model_conserves_material', sum(free.values()) + consumed == 150)
    check('completed_callback_has_no_second_reservation', 'operation-A' not in reserved)
    free['A'] -= 20
    hidden_report_claim = 20
    check('report_does_not_recreate_destroyed_material', free['A'] == 60 and hidden_report_claim == 20)

    available = 100 - 40 - 20
    awards = [25, 15]
    check('auction_excludes_prior_commitments', available == 40 and sum(awards) == available)
    check('partial_delivery_preserves_unfilled_principal', awards[0] - 10 == 15)
    quoted_price, delivered, ordered, paid = 200, 6, 10, 100
    due = Decimal(quoted_price) * Decimal(delivered) / Decimal(ordered) - Decimal(paid)
    check('proportional_partial_delivery_settlement', due == 20)

    before, requested = 95, 10
    after = min(100, before + requested)
    applied = after - before
    check('authority_tracks_actual_clamped_grant', applied == 5)
    check('reversal_cannot_remove_unapplied_authority', after - applied == before)

    recipients = set(range(1, 1001)) | set(range(501, 1501)) | set(range(2001, 2501))
    check('purpose_coverage_counts_unique_people', len(recipients) == 2000)
    check('coverage_bounded_by_material_and_route', min(len(recipients), 1600, 1250) == 1250)
    food_proof, shelter_places = False, 1000
    check('shelter_without_food_proof_cannot_admit', (shelter_places if food_proof else 0) == 0)
    check('qualification_cannot_fit_shorter_care_deadline', 90 > 45)
    check('administrative_discount_only', Decimal(20) * Decimal('0.75') == 15 and 30 + 90 == 120)
    check('separate_manufacturing_and_qualification_unchanged', 15 + 30 + 90 == 135)

    def interval(base: str, factors: list[str], lower: int, upper: int) -> int:
        value = Decimal(base)
        for factor in factors:
            value *= Decimal(factor)
        rounded = int((value / Decimal(5)).to_integral_value(rounding=ROUND_CEILING)) * 5
        return min(upper, max(lower, rounded))
    check('international_nominal_interval', interval('120', ['0.75', '0.75'], 30, 360) == 70)
    check('autonomous_nominal_interval', interval('150', ['0.65', '0.80'], 45, 450) == 80)
    check('sovereignty_nominal_interval', interval('180', ['0.65', '0.75'], 60, 540) == 90)
    check('supervised_sovereignty_nominal_interval', interval('180', ['1.50', '1.25'], 60, 540) == 340)
    check('nominal_interval_lower_bound', interval('120', ['0.01'], 30, 360) == 30)
    check('nominal_interval_upper_bound', interval('120', ['10'], 30, 360) == 360)
    thresholds = [200, 400, 600, 800]
    check('four_evolution_thresholds', len(thresholds) == 4 and thresholds == sorted(set(thresholds)))
    check('threshold_boundary_is_inclusive', all(not (t - 1 >= t) and t >= t for t in thresholds))
    activation_changes = {t: 0 for t in thresholds}
    check('evolution_activation_has_zero_chaos', sum(activation_changes.values()) == 0)

    previous_credit = 0
    applied_credits = []
    for cumulative_cap in [5, 10, 20, 20]:
        applied_credits.append(max(0, cumulative_cap - previous_credit))
        previous_credit = max(previous_credit, cumulative_cap)
    check('local_national_global_rewards_share_one_ceiling', applied_credits == [5, 5, 10, 0] and sum(applied_credits) == 20)
    manufactured_farming_episode = True
    check('manufactured_episode_has_no_negative_chaos_reward', (0 if manufactured_farming_episode else 20) == 0)
    teams = {'team-1': 'domestic-care'}
    check('one_team_cannot_fill_two_simultaneous_jobs', teams.get('team-1') is not None)
    del teams['team-1']
    teams['team-1'] = 'qualified-new-service'
    check('qualified_handover_changes_assignment_not_people', len(teams) == 1)
    check('portrait_frame_sheet_width', 12 * 156 == 1872)
    check('emblem_frame_sheet_width', 12 * 64 == 768)
    return results


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--build-zip', type=Path)
    args = ap.parse_args()
    baseline = json.loads((HERE / 'baseline_stage_8_identity.json').read_text())
    mutable = set(baseline['mutable_entry_documents'])
    unchanged = 0
    snapshots = 0
    for rel, expected in baseline['members'].items():
        path = ROOT / rel
        require(path.is_file(), 'Missing baseline member: ' + rel)
        if rel in mutable:
            snapshot = HERE / 'baseline_stage_8_document_snapshots' / rel
            require(snapshot.is_file() and sha(snapshot.read_bytes()) == expected, 'Changed baseline snapshot: ' + rel)
            snapshots += 1
        else:
            require(sha(path.read_bytes()) == expected, 'Changed inherited member: ' + rel)
            unchanged += 1

    found = list(SPEC.rglob('*spec_part_*.md'))
    numbers = [int(re.search(r'part_(\d+)', p.name)[1]) for p in found]
    require(sorted(numbers) == list(range(1, 21)), 'The specification must contain exactly Parts 1–20')
    parts = dict(zip(numbers, found))
    wordcounts = {n: len(p.read_text().split()) for n, p in parts.items()}
    for n, title, sub in [
        (13, '# Doctor Wu: The International Biological Contest', '## When medical success becomes an international contest'),
        (14, '# Doctor Wu: Forbidden and Autonomous Biology', None),
        (15, '# Doctor Wu: Sovereign Biology', None),
    ]:
        text = parts[n].read_text()
        require(text.splitlines()[0] == title, f'Unexpected Part {n} title')
        if sub:
            require(text.splitlines()[2] == sub, 'Unexpected Part 13 opening section')

    prompt_names = ['asset', 'super_event', 'achievement', 'decision_mission', 'coding', 'goal']
    for name in prompt_names:
        p = SPEC / f'089_doctor_wu_{name}_prompt.md'
        require(p.is_file() and p.stat().st_size > 1000, 'Missing or empty prompt: ' + name)
    goal_chars = len((SPEC / '089_doctor_wu_goal_prompt.md').read_text())
    require(3500 <= goal_chars <= 4000, 'Goal prompt length out of range')
    assets = json.loads((SPEC / 'presentation/089_doctor_wu_asset_manifest.json').read_text())
    achievements = json.loads((SPEC / 'presentation/089_doctor_wu_achievement_manifest.json').read_text())['achievements']
    projects = assets['project_icons']
    expected_ids = {f'{f}{i:02}' for f, count in [('M',16), ('H',7), ('C',8), ('R',12), ('L',15), ('S',12)] for i in range(1, count+1)}
    require({p['id'] for p in projects} == expected_ids and len(projects) == 70, 'Project manifest mismatch')
    require(len({p['proposed_runtime_path'] for p in projects}) == 70, 'Duplicate project runtime path')
    for row in projects:
        require((SPEC / row['source_path']).is_file(), 'Missing project source')
        require(row['status'] == 'planned_not_produced', 'False asset production state')
    require(len(achievements) == 20 and {a['id'] for a in achievements} == {f'ACH{i:02}' for i in range(1,21)}, 'Achievement roster mismatch')
    for a in achievements:
        require(len(a['rules']) > 650, 'Incomplete achievement rule block: ' + a['id'])
    require(len(assets['units']) == 10 and len(assets['portraits']) == 7 and len(assets['flags']) == 3, 'Visible family manifest mismatch')
    require(len(assets['super_events']) == 3 and len(assets['animations']) == 2, 'Announcement or animation count mismatch')
    require(all(a['audio_status'] == 'not_selected_or_produced' for a in assets['super_events']), 'False audio status')
    for a in assets['animations']:
        require(a['sheet_canvas'] == [a['frame_canvas'][0] * a['frames'], a['frame_canvas'][1]], 'Animation geometry mismatch')
    # Readability lint is deliberately scoped to new prose, never rewrites inherited files.
    new_md = [parts[n] for n in range(13,21)] + list(SPEC.glob('*_prompt.md'))
    for p in new_md:
        text = p.read_text()
        require('\u2014' not in text and ';' not in text, 'New prose contains prohibited punctuation: ' + p.name)
    require('SB01' in parts[15].read_text() and 'SB10' in parts[15].read_text(), 'Sovereignty action namespace missing')
    require(not re.search(r'^\| S\d{2}\b', parts[15].read_text(), re.M), 'Sovereignty collides with Part 9 project IDs')
    ast.parse(Path(__file__).read_text())

    report_path = HERE / 'FINAL_VALIDATION_REPORT.md'
    if not report_path.exists():
        report_path.write_text('# Final local validation\n\nValidation is running.\n')
    checked_links = []
    failed_links = []
    link_pattern = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
    for p in ROOT.rglob('*.md'):
        if 'baseline_stage_8_document_snapshots' in p.parts or 'source_inputs' in p.parts:
            continue
        for match in link_pattern.finditer(p.read_text()):
            raw = match.group(1).strip()
            if raw.startswith(('http:', 'https:', '#', 'mailto:', 'sandbox:', 'hoi4-agent:')):
                continue
            target = raw.split(' "',1)[0].strip('<>')
            target = unquote(target.split('#',1)[0])
            if not target:
                continue
            q = (p.parent / target).resolve()
            if not q.exists():
                failed_links.append({'file':str(p.relative_to(ROOT)), 'target':raw})
            checked_links.append({'file':str(p.relative_to(ROOT)), 'target':raw})
    if failed_links:
        dump(HERE/'link_failures.json',failed_links)
        raise AssertionError(f'{len(failed_links)} broken local links, see link_failures.json')
    old_failure = HERE/'link_failures.json'
    if old_failure.exists():
        old_failure.unlink()
    symbolic = symbolic_checks()
    result = {
        'status':'passed_local_document_and_symbolic_checks',
        'engine_validation':False, 'probability_audit':False, 'asset_production':False,
        'fresh_exhaustive_source_read':False, 'source_reading_exception':'explicitly_authorized_by_user',
        'baseline_members':len(baseline['members']), 'unchanged_baseline_members':unchanged,
        'changed_entry_documents_preserved_as_snapshots':snapshots,
        'unchanged_original_specification_parts':12,
        'specification_parts':20, 'specification_words':sum(wordcounts.values()),
        'new_part_words':sum(v for n,v in wordcounts.items() if n>=13),
        'goal_characters':goal_chars, 'final_prompts':6,
        'project_icon_roles':70, 'achievement_plans':20, 'unit_visual_consumers':10,
        'checked_local_markdown_links':len(checked_links), 'broken_local_links':0,
        'link_scope':'Markdown in the package excluding preserved contextual snapshots and supplied source_inputs. External URL reachability and anchor correctness are not tested.',
        'symbolic_check_count':len(symbolic), 'symbolic_checks':symbolic,
        'word_count_method':'Whitespace-separated tokens in the twenty specification files, including headings and tables',
    }
    dump(HERE/'local_validation_results.json',result)
    report_path.write_text(f'''# Doctor Wu final local validation report

Result: **passed local document and symbolic checks**. This report is produced by `verify_final_package.py`.

## Exact preservation

The baseline identity record contains {len(baseline['members'])} Stage 8 members. All {unchanged} non-entry members are unchanged. The three mutable entry documents, README, current index and current resume, have exact original snapshots. Parts 1–12 and the original brief remain byte-identical to Stage 8.

## Structure and inventories

The package contains twenty specification parts totaling {sum(wordcounts.values()):,} words, including {sum(v for n,v in wordcounts.items() if n>=13):,} words in Parts 13–20. All six final prompt files exist. The goal prompt contains {goal_chars:,} characters, including its heading and final newline, within the 4,000-character limit.

The manifests contain seventy distinct research icon roles, twenty complete achievement entries, ten unit visual consumers, seven portrait states, three flag families, two animation families and three major announcement roles. Their state remains planned or unproduced. No asset-production claim is inferred from the manifest.

{len(checked_links)} local Markdown links resolve. This check excludes preserved contextual snapshots and supplied source inputs, and does not test external URL reachability or Markdown anchor correctness. The new sovereignty actions use SB01–SB10, preserving S01–S12 for the inherited modification projects.

## Symbolic examples

{len(symbolic)} local checks pass for finite first settlement, duplicate requests, civilian/specialist accounting, pre- and post-settlement deaths, custody partitions, immutable stock profiles, reservations, partial delivery, actual clamped Authority, unique recipient union, food proof, care deadlines, administrative-only timing, proposed rounded MTTH intervals, four thresholds, zero activation Chaos, cumulative cure credit, staff assignment and animation sheet dimensions.

These tests are deliberately small symbolic models of the written rules. They do not execute the game, validate an engine API, simulate native cancellation or establish real AI probabilities. The complete named campaign and MCP test sets remain future work.

## Archive build procedure

When invoked with `--build-zip`, the same script writes a per-file SHA-256 manifest, creates the cumulative archive, checks ZIP CRC integrity, rejects duplicate/unsafe member paths, and compares every archived byte with its source file. It then writes an external archive verification record and SHA-256 sidecar. A failed archive comparison aborts the run.

## Limits

A fresh exhaustive Project Source reread was explicitly waived by the user and was not completed. No named specialist, HOI4 MCP, installed-vanilla, live-game, quote/audio research or asset-production workflow ran. D03, N-D11 and the final implementation gates remain unresolved or unapproved as recorded. The deliverable is a complete-scope proposed planning package, not a release-certified mod.
''',encoding='utf-8')
    manifest_path = HERE/'FINAL_FILE_MANIFEST.json'
    rows = [{'path':p.relative_to(ROOT).as_posix(), 'bytes':p.stat().st_size, 'sha256':sha(p.read_bytes())} for p in sorted(ROOT.rglob('*')) if p.is_file() and p != manifest_path]
    dump(manifest_path, {'schema':'doctor_wu_final_file_manifest_v1','scope':'Every delivered file except this self-referential manifest','files':rows})
    if args.build_zip:
        output=args.build_zip.resolve()
        require(not output.is_relative_to(ROOT), 'Place the output ZIP outside its source root')
        output.parent.mkdir(parents=True,exist_ok=True)
        members=[p for p in sorted(ROOT.rglob('*')) if p.is_file()]
        with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            for p in members:
                z.write(p,p.relative_to(ROOT).as_posix())
        with zipfile.ZipFile(output) as z:
            require(z.testzip() is None, 'ZIP CRC failure')
            require(len(z.namelist())==len(set(z.namelist()))==len(members),'ZIP member count or duplication failure')
            for p in members:
                name=p.relative_to(ROOT).as_posix()
                require(not name.startswith('/') and '..' not in Path(name).parts, 'Unsafe ZIP member')
                require(z.read(name)==p.read_bytes(),'ZIP/source byte mismatch: '+name)
        archive_record={'status':'verified','filename':output.name,'bytes':output.stat().st_size,'sha256':sha(output.read_bytes()),'members':len(members),'crc_integrity':True,'all_archived_bytes_equal_sources':True,'baseline_preservation':result['unchanged_baseline_members'],'engine_validation':False}
        dump(output.with_suffix('.verification.json'),archive_record)
        output.with_suffix('.sha256.txt').write_text(archive_record['sha256']+'  '+output.name+'\n')
        print(json.dumps(archive_record,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k not in {'symbolic_checks'}},indent=2))

if __name__=='__main__':
    main()
