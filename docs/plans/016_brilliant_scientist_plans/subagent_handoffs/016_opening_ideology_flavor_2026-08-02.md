# Event 016 opening ideology-flavour handoff

Date: 2026-08-02

## Scope

This bounded content tranche adds governing-ideology presentation to the existing opening and one-time referral reports. It does not add a new event, option, reward, meter, receipt, evolution, project stage, asset, unit, model, or country route.

## Runtime changes

- `GetBrilliantScientistIdeologyClause` in `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt` selects democratic, communist, fascist, non-aligned, or safe default wording from the current country scope.
- The base and evolved `chaosx.nr16.2` and `chaosx.nr16.3` descriptions now append that clause after their existing host-archetype or evolution prose. Archetype selection still has priority because it remains the event description trigger; ideology is an additional sentence rather than a competing fire path.
- The clause is descriptive only. Public and secret appointment effects, AI weights, referral guards, fixed Kruger identity, and host transfer logic are unchanged.

## Localisation

The five new keys are in `localisation/english/016_brilliant_scientist_l_english.yml`:

- `brilliant_scientist_ideology_clause_democratic`
- `brilliant_scientist_ideology_clause_communist`
- `brilliant_scientist_ideology_clause_fascist`
- `brilliant_scientist_ideology_clause_neutral`
- `brilliant_scientist_ideology_clause_default`

The file remains UTF-8 with BOM. No new sprite or GFX key is needed.

## Validation and boundary

- The scripted-localisation file has balanced braces and no unsupported comparison operators.
- The opening event file remains balanced and unchanged by this tranche.
- All eighteen opening and referral description consumers reference the helper, and all five helper keys are present.
- No Hearts of Iron IV session was launched; live opening and referral display remains user-owned.
- Broader country-specific chains, quantitative balance evidence, live consumer validation, and the seven deferred Event 016 3D packages remain outside this tranche.
