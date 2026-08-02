# Event 012 RSA prefire permission-guard repair

Date: 2026-08-02.

Status: Implemented source repair; live-save acceptance remains open.

## Scope

The Event 012 fire-once dispatcher accepted both the generic African host route and the validated South African Allied-rupture route when selecting and dispatching a frozen prefire host.

An intervening permission guard still rejected every selected host that did not satisfy `africa_is_eligible_host`, which requires `generic_focus` and therefore excluded original SAF even though the RSA route intentionally preserves its meaningful South African focus tree.

## Change

`common/scripted_effects/chaosx_settings_effects.txt` now validates the frozen `africa_prefire_host` with `africa_can_initialize_selected_host`.

That existing centralized trigger admits exactly the generic host predicate or `africa_rsa_shared_entry_is_eligible`, so the repair does not weaken generic host rules or add a tag, fallback branch, or alternate country identity.

## Expected behavior

- An eligible generic host remains permitted through the existing generic predicate.
- Original SAF can pass the shared prefire permission guard when its frozen contact roster and Allied/RSA gate are valid.
- SAF remains rejected when its post-freeze exile-patron requirement or any other RSA opening condition fails.
- The canonical `chaosx.nr12.1` entry remains the only caller of the public RSA civil-war start effect.

## Validation boundary

Static source inspection confirmed the selector, permission guard, dispatcher, centralized initializer trigger, and RSA gate now use the same admitted route set.

The bounded `hoi4_event_inspect` lint for `chaosx.nr12.1` returned status `ok` with no blocking diagnostics, while its workspace-wide helper analysis remained deferred by the adapter.

No Hearts of Iron IV executable or live save was launched, so civil-war, patron-selection, and no-patron runtime outcomes remain open acceptance work.

No models, new country tags, dormant Event 006 carriers, external continent packages, pathogen gates, or achievement proxies were changed.
