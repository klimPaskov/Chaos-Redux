# Crisis Board State Flow

```mermaid
flowchart TD
    A[Clear] -->|exposure exceeds protection| B[Threatened]
    B -->|exposure decays| A
    B -->|infection establishes| C[Incubating]
    C -->|early suppression| D[Contained]
    C -->|public recognition| E[Infected]
    E -->|load and mortality rise| F[Severe Crisis]
    E -->|effective quarantine and treatment| D
    F -->|administration fails| G[Collapsed]
    F -->|major suppression| D
    G -->|human control restored| F
    G -->|Evolution III basin emergence| H[Rat Controlled]
    H -->|human liberation| F
    D -->|sustained low load| I[Recovery]
    D -->|fresh exposure or rushed reopening| E
    I -->|cleanup complete| J[Cured and Monitored]
    I -->|relapse| E
    J -->|monitoring period complete| A
    J -->|major new exposure| C
```

## Provenance overlay

Natural, accidental, weaponized, relapse, and rat-occupation provenance sit above this state flow. They change condemnation, starting load, attribution, or rat behavior without creating duplicate disease instances.
