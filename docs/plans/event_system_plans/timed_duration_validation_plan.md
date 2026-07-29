# Timed duration syntax validation plan

Date: 2026-07-29

Status: deferred validation and migration plan. No duration expression is changed by this document.

## Why this plan exists

The Events 001-020 cleanup found many timed `days =` fields that receive script constants, normal or temporary variables, explicit `var:` tokens, file-scoped `@` values, or literals. Repository guidance and historical audits do not give one consistent rule for every timed effect: `AGENTS.md` prefers a variable bridge when a script constant is rejected, the events skill treats timed flags as sensitive and prefers a mirrored file-scoped value, and current vanilla precedents include supported variable forms.

A blanket conversion would duplicate tuning, change expiry behavior, or replace working syntax without parser evidence. The existing expressions therefore remain in place until each field family has a documented syntax contract.

## Scope

The first inventory covers Events 001-020 and shared event-system callers. Event 021 and later standalone implementations remain out of scope except when they provide a shared helper, registry, or vanilla-compatible precedent used by Events 001-020.

Prioritize:

1. timed `set_country_flag` and `set_global_flag` blocks that gate super-event visibility, terminal routes, cleanup, cooldowns, or achievement evidence;
2. mission and decision re-enable durations;
3. delayed event and hidden cleanup callbacks;
4. timed ideas and modifiers;
5. low-impact presentation or recency flags.

## Phase 1: exact inventory

Record every non-literal `days =` expression with its file, owning helper, effect type, token form, tuning source, cleanup consumer, and gameplay consequence if the duration fails to parse.

Classify each expression as:

- direct `constant:category.key`;
- unscoped normal or temporary variable;
- explicit `var:name`;
- file-scoped `@NAME`;
- literal;
- meta-effect injection;
- another documented form.

Do not count the same helper more than once merely because it has several callers.

## Phase 2: evidence matrix

For each effect family, compare:

- the current official vanilla effect and script-concept documentation;
- at least one current vanilla use of the same effect field and token form;
- the offline wiki syntax;
- the relevant repository skill and `AGENTS.md` rule;
- any existing Chaos Redux audit that records a parser failure or verified correction.

Evidence for one field does not automatically authorize changing a different field. A supported delayed-event duration does not prove a timed-flag duration, and a country flag does not prove a global flag.

## Phase 3: guidance reconciliation

Before gameplay migration, reconcile the events skill and repository guidance into one field-specific table:

- use a shared script constant directly when the field accepts it;
- use a normal or temporary variable bridge only where the field accepts variables;
- use an explicit `var:` form where the field documents or demonstrates that syntax;
- use a file-scoped `@` value only where a dynamic form is not supported, with one documented authoritative tuning owner and an explicit mirror rule;
- use a meta effect only when text injection is supported and materially safer than a duplicated literal.

Do not introduce silent hardcoded replacements.

## Phase 4: bounded migrations

Migrate one effect family or event-owned subsystem at a time. Each tranche must update its tuning documentation, preserve the exact duration, preserve cleanup and cancellation behavior, and include a focused source-to-consumer check.

Start with Event 020 terminal and super-event visibility flags, then the other Events 011-020 terminal and cooldown gates, then Event 006 package flags. Do not combine unrelated events in one migration commit.

## Acceptance gates

A tranche is accepted only when:

- every changed duration has one authoritative tuning source;
- the selected syntax is supported by official documentation or a matching current vanilla precedent;
- every producer and cleanup consumer remains connected;
- the duration value is unchanged unless a separate balance decision authorizes a change;
- no new whole-world daily, weekly, or monthly loop replaces timed expiry;
- localisation and documentation still describe the actual duration;
- no Event 021 or later standalone implementation is changed incidentally.

If evidence remains contradictory, retain the current code and document the unresolved field rather than substituting a fallback.

## Current disposition

No duration migration is authorized by this plan. The cleanup retains the existing expressions because their parser validity is field-specific and cannot be inferred safely from token shape alone.
