# CYSE-130
Text-based game
World of the Forgotten

Team Members 

Harsimar Kaur,
Hajra Amin,
Rashed Alkhaaldi,
Fey Zurita-Sejas,
Abby Agyemang.

Project Overview 

World of the Forgotten is a text-based interactive story game where players explore a mysterious world, make decisions, collect items, and experience multiple endings based on their choices. 

How to Run the Game 

1. Install Python 3 
2. Download or clone the repository 
3. Run the program using: python main.py 

Core Features 

- Three branching story paths 
- Multiple endings 
- Inventory system 
- Health tracking 
- Save and load system 
- Tamper detection using SHA-256 hashing 
- Audit logging system 

Story Paths 

1. First Life – A surreal garden journey where players gather items and try to escape. 
2. Deja Vu – A looping world where memory helps navigate puzzles. 
3. Reincarnation / Revenge – A darker path involving past memories and moral choices. 

Endings 

1. Freedom Ending – Player escapes successfully. 
2. Acceptance Ending – Player remains trapped. 
3. Aware Loop / Partial Freedom – Player gains awareness or partial escape. 

Locations / Events 

1. The Garden 
2. Tea Party 
3. Mirror Garden / Hall 
4. Gatekeeper Room 
5. Throne Room / Clock Tower 

NPCs 

1. Host – Appears in Tea Party/End; guides the story. 
2. Gatekeeper – Blocks path; gives riddle challenge. 
3. Smiling Girl – Gives bandages in meadow. 
4. Cheshire Cat – Can help or harm player. 
5. Forgotten Ones – Represent past memories; affect choices. 

Inventory Items 

1. Cracked Watch – Allows retry of challenge. 
2. Tea Vial – Skips riddle challenge. 
3. Glass Shard – Increases item count but drains health. 
4. Shiny Key – Earned from riddle. 
5. Bandages – Restore health. 

Challenges 

1. Gatekeeper Riddle – Solve correctly to proceed; failure may trap player. 
2. Memory Chamber – Answer based on earlier choice; wrong answer leads to failure ending. 

Cyber Pack Features 

Audit logging records actions into a file. SHA-256 hashing ensures the save file is not altered. Tamper detection prevents loading modified files. The save/load system securely stores player progress. 
