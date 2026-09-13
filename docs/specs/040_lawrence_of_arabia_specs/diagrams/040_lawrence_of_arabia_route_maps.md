# Event 40 Route Maps

## Baseline campaign flow

```mermaid
flowchart TD
    A[Britain verifies Lawrence and valid regional access] --> B[Select one valid Arabian target]
    B --> C[Recall and arrival]
    C --> D[Terms of access]
    D --> E[Network contest]
    E --> F{Decisive settlement available}
    F -->|High Influence| G[Client, protectorate, or British-backed government]
    F -->|Controlled middle band| H[Independent ally or sovereign armed partner]
    F -->|Low Influence and evidence| I[Expulsion, arrest, or dismantlement]
    F -->|Hidden trust and British overreach| J[Lawrence defects to an independent Arab project]
    F -->|No decisive result| K[Restricted mission or unresolved balance]
    G --> L[Record settlement and regional node]
    H --> L
    I --> L
    J --> L
    K --> L
    L --> M{Campaign can continue}
    M -->|Yes| N[Dynamic regional delay]
    N --> B
    M -->|No| O[Regional campaign closes and cleanup runs]
```

## Influence response map

```mermaid
flowchart LR
    A[Broken Access 0 to 19] --> B[Restricted Mission 20 to 39]
    B --> C[Contested Network 40 to 59]
    C --> D[Embedded Mission 60 to 79]
    D --> E[Ascendant Network 80 to 94]
    E --> F[Dominant Influence 95 to 100]

    B -. target controls terms .-> A
    C -. audit, custody, sponsor balance .-> B
    D -. exposure, route control, officer reform .-> C
    E -. arrest risk, public proof, British failure .-> D
    F -. exceptional counter-operation .-> E

    A -. British route and funding .-> B
    B -. officer and political access .-> C
    C -. successful aid and missions .-> D
    D -. regional nodes and government weakness .-> E
    E -. coup coalition or settlement pressure .-> F
```

## Evolution entry paths

```mermaid
flowchart TD
    A[Event 40 has not fired] --> B{Current Chaos and enabled evolution}
    B -->|Baseline only| C[Ordinary first intervention]
    B -->|Evolution I| D[First target begins with an established contact and cell footprint]
    B -->|Evolution II| E[Existing British relationships are assessed as regional nodes]
    B -->|Evolution III| F[Unification is declared as a long-term objective]

    G[Event 40 is already active] --> H{Evolution becomes available through pacing}
    H -->|Evolution I| I[Current network gains smuggling, sabotage, officer, and revolt capacity]
    H -->|Evolution II| J[Settled clients and allies become a regional system]
    H -->|Evolution III| K[Congress and federation routes open from current settlements]
```

## Evolution I incident ladder

```mermaid
flowchart TD
    A[Contact network] --> B[Arms, route, officer, local-leader, or political cell]
    B --> C{Target detects the cell}
    C -->|Early detection| D[Turn contact, seize cache, rotate officers, or expose funding]
    C -->|Partial detection| E[Mission contest and mixed result]
    C -->|No detection| F[Sabotage, defection, mutiny, or local revolt]
    F --> G{Government rupture proven}
    G -->|No| H[Severe incident and renewed contest]
    G -->|Yes| I[Coup, government replacement, or viable civil war]
    D --> J[Cell strength reduced]
    E --> J
    H --> J
    I --> K[New government and settlement identity]
```

## Evolution II system map

```mermaid
flowchart TD
    A[Britain] --> B[Arabian Liaison Conference]
    A --> C[Arms Standardization Office]
    A --> D[Regional Intelligence Office]
    A --> E[Desert Air Route]
    A --> F[Oil and Transport Agreements]
    A --> G[Joint Defense Charter]

    H[Clients and allies] --> B
    H --> C
    H --> D
    H --> E
    H --> F
    H --> G

    I[Active target] --> J{Response}
    J -->|Join| H
    J -->|Bargain| K[Independent ally or autonomy settlement]
    J -->|Refuse| L[Counter-bloc or resistance]
    J -->|Exploit rivalry| M[Favor and autonomy contest]
```

## Evolution III formation map

```mermaid
flowchart TD
    A[Enough durable governments and routes] --> B[Call an Arab congress or British federal conference]
    B --> C[Select a legitimate core government]
    C --> D[Negotiate representation, defense, revenue, and foreign policy]
    D --> E{Ratification pattern}
    E -->|British dominance| F[British Arabia]
    E -->|Sovereign charter| G[Independent Arab Federation]
    E -->|Rare personal authority| H[Lawrence's Kingdom]
    E -->|Insufficient agreement| I[League, partial settlement, or failed congress]
    F --> J[Validated federation transaction]
    G --> J
    H --> J
    J --> K[Federal Authority replaces Lawrence's Influence]
```

## Lawrence character state map

```mermaid
stateDiagram-v2
    [*] --> Concealed
    Concealed --> BritishLiaison: first intervention
    BritishLiaison --> FieldAdviser: military appointment
    BritishLiaison --> PoliticalAdviser: negotiated access
    BritishLiaison --> Detained: target arrests mission
    BritishLiaison --> Expelled: target removes mission
    BritishLiaison --> Defected: hidden independent route succeeds
    BritishLiaison --> Wounded: incident or failed operation
    BritishLiaison --> Dead: lethal outcome
    Detained --> BritishLiaison: rescue or release
    Detained --> Defected: host wins personal allegiance
    Detained --> Dead: failed rescue or execution
    Expelled --> BritishLiaison: Britain assigns later mission
    Wounded --> BritishLiaison: recovery
    Defected --> FederationArchitect: Evolution III congress
    FederationArchitect --> FederationLeader: rare Lawrence's Kingdom formation
    FederationArchitect --> Retired: constitution excludes personal rule
    FederationLeader --> Dead: mortality
    BritishLiaison --> Retired: Britain ends campaign
    Dead --> [*]
```

## Federation focus architecture

```text
                         PROVISIONAL FEDERATION
                                  |
                 FOUNDING CHARTER AND TEMPORARY CAPITAL
                                  |
        +-------------------------+-------------------------+
        |                         |                         |
POLITICAL SETTLEMENT       FEDERAL STRUCTURE        COMMAND INTEGRATION
        |                         |                         |
+-------+-------+          +------+-------+          +------+-------+
|       |       |          |              |          |              |
British Sovereign Lawrence Central State Charter     General Staff  Member Council
Compact Congress Personal  Method        Method      Method         Method
        |       Settlement        |              |          |              |
        +-----------+-------------+--------------+----------+--------------+
                    |
       ECONOMY, OIL, RAIL, PORTS, AIR ROUTES, SUPPLY
                    |
         DIPLOMACY, RECOGNITION, AND ACCESSION
                    |
          REGIONAL SETTLEMENT AND LATE ORDER
```

## Outcome and cleanup matrix

| Outcome | Lawrence status | British regional reach | Target category | Later role |
| --- | --- | --- | --- | --- |
| British client | British liaison or regional adviser | increases | closes | regional node |
| Independent ally | British liaison with limits | moderate increase | closes | treaty partner |
| Sovereign armed partner | British liaison with narrow access | small increase | closes | possible congress member |
| Restricted mission | may remain or return | little change | closes | neutral memory |
| Expulsion | expelled | decreases | closes after cleanup | target preparedness |
| Arrest | detained | uncertain | captivity actions replace ordinary actions | exchange, rescue, trial, or defection |
| Dismantled network | expelled or returned | strong decrease | closes after mission | counter-bloc support |
| Defection | independent adviser | decreases sharply | independent actions replace British actions | federation architect |
| Federation formation | architect, adviser, leader, retired, or dead | converted into outcome-specific relation | Lawrence's Influence closes | Federal Authority begins |
