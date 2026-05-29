# Event 005 Decision, Release, and Focus Reward Fix

## Scope

This pass tightens the Soviet collapse decision economy, makes early republic releases more assertive at low threat, opens foreign intervention visibility for eligible major patrons earlier, and gives League-aligned focus rewards a concrete unit-deployment surface.

## Gameplay Changes

- Soviet collapse fuel costs are higher across Soviet, breakaway, Ukrainian, Moldovan, Kazakh, Central Asian, regional League, foreign patron, and Moscow reintegration decisions.
- The first wave of republic releases now includes an extra republic by default, and low-threat follow-on release checks begin sooner with stronger release weighting.
- Progressive republic releases are evaluated from the existing Soviet monthly crisis heartbeat. A first-year backlog pass keeps releases moving even under low threat, with staged release floors by the third, sixth, and tenth crisis month so the constituent republics are not left waiting indefinitely.
- Foreign patron categories are visible to eligible major and regional patrons once the crisis exists, while individual target decisions still use route, acceptance, and cost checks.
- Soviet emergency mobilization is a one-time war emergency order. It is hidden until the Union Unmade super-event has fired, is available only while the Soviet Union is in an active breakaway war, does not lock on its stability/war-support/command-power cost, grants a large reserve equipment package, and deploys emergency rifle and motorized units at the capital.
- League preparation focuses unlock two repeatable deployment decisions:
  - `soviet_collapse_deploy_league_rifle_cadres`
  - `soviet_collapse_deploy_league_motor_columns`
- Republic focus rewards hide consolidated idea maintenance behind `hidden_effect`, so focus tooltips show the meaningful reward instead of the internal remove/add idea refresh.
- Focus-tree layout cleanup removed detected duplicate focus coordinates and midpoint collisions where mutually-exclusive links placed their marker over an unrelated focus. The Ukraine tree also gets a second entry into statehood through the telegraph/grain branch instead of forcing the whole political route through the military line.

## Icons

No new sprites are required. The new League deployment decisions reuse existing regional decision icons:

- `GFX_decision_soviet_collapse_regional_goal_defense`
- `GFX_decision_soviet_collapse_regional_coordinate`

## Validation

- `git diff --check` passed for all touched Event 005 files.
- Touched Clausewitz script files have balanced braces.
- No unsupported `<=` or `>=` operators were introduced.
- Touched localisation files retain UTF-8 BOM.
- The focus layout audit reports zero duplicate coordinates and zero mutually-exclusive midpoint collisions across `common/national_focus/005_soviet_collapse*.txt`.
