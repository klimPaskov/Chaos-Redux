# Event 006 achievement localisation registry merge

Date: 2026-08-25

## Scope

The standalone Event 006 achievement localisation file was merged into the shared Event 006 localisation registry. This is a source-layout reduction only; achievement identifiers, wording, and achievement wiring are unchanged.

## Changed files

- `localisation/english/006_independence_wave_l_english.yml`
  - appended the 49 achievement localisation keys from the former registry under an explicit source marker
  - retained the existing UTF-8 BOM and the single `l_english:` root
- `localisation/english/006_independence_wave_achievements_l_english.yml`
  - removed after its complete key/value set was copied into the shared registry

## Evidence

- The former file contained one `l_english:` root and 49 achievement keys. The receiver contains those same 49 achievement keys exactly once.
- No achievement key already existed in the receiver; the merge therefore does not replace or shadow any existing localisation.
- The receiver retains the UTF-8 BOM (`EF BB BF`).
- The source tree decreases by 106 bytes after removing the duplicate root/file overhead. The receiver remains a single parser file for the shared Event 006 namespace.
- The achievement on-action file remains separate because its callback keys are engine-owned and are not part of this localisation merge.

## Validation

Run the targeted localisation crosswalk from the mod root:

```text
python -B .tools/audit_event6_allocator.py
python -B .tools/audit_event6_country_api.py
python -B .tools/audit_event6_flags.py --strict
```

The merge does not widen package admission, alter event reachability, change achievement triggers, or claim live game execution.
