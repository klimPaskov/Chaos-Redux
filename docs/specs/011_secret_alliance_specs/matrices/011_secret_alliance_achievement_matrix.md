# Event 011 Secret Alliance Achievement Matrix

| Working key | Visibility | Difficulty | Core conditions | Disqualifiers | Tracking notes |
| --- | --- | --- | --- | --- | --- |
| `secret_alliance_empty_chair` | visible | hard | expose and dissolve before any target-member war | target starts war first, formal pact war starts | track peaceful exposure and member exits |
| `secret_alliance_all_names` | hidden | hard | confirm every live member before public reveal | self-reveal or war reveal before all confirmed | snapshot member count and confirmed count |
| `secret_alliance_three_knocks` | visible | hard | neutralize all three founders within time window | founder annexed by unrelated country before handled | mark founder handled by expose, exit, or defeat |
| `secret_alliance_lone_target` | hidden | very hard | as minor target, win war against pact with five members and major patron | target joins a large faction after reveal if isolation is required | store target size at event start |
| `secret_alliance_counter_protocol` | visible | hard | strike first at Evolution III with high readiness and win quickly | low counter-readiness or tiny pact | track declaration source and war duration |
| `secret_alliance_wrong_room` | hidden | medium hard | false leak causes expulsion, then target wins without declaring first | repeated false leak failure | track successful false leak and war initiator |
| `secret_alliance_no_patrons` | visible | hard | prevent all major patron joins and defeat or dissolve pact | any major patron joins | track patron_joined flag |
| `secret_alliance_paid_in_promises` | hidden | hard | expose conflicting promises and force two members out | no conflicting promises generated | track conflicting promise pair and exits |
