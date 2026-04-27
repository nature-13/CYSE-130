# CYSE-130
Text-based game
The Garden Between Lives - Graphic Version

GAME DESCRIPTION:
This is a story-based interactive adventure game built using Python and the tkinter library.
The game places the player inside a surreal, dream-like world where they explore different paths,
make choices, collect items, and unlock multiple endings.

The main idea of the game is reincarnation and memory. The player starts in a mysterious garden
and slowly realizes they have lived this moment before. Based on their decisions, they either stay
trapped in a loop, partially escape, or completely break free.

FEATURES IMPLEMENTED:
- Graphical User Interface (GUI) using tkinter (no terminal input required)
- Button-based choices instead of typing input
- Multiple story paths (3 main paths)
- Inventory system with items and memory fragments
- Player animation using Canvas (moving + idle animation)
- Scene rendering using shapes (rectangles, ovals, lines, arcs)
- Dynamic story progression based on decisions
- Multiple endings (Loop, Partial Freedom, Aware Loop, Dark Ruler, True Ending, Corruption)
- Unit testing using unittest module

PROGRAMMING CONCEPTS USED:
- Classes and Object-Oriented Programming (GardenGame class)
- Functions (modular structure like show_scene, add_item, maze, etc.)
- Conditionals (if/else statements for choices and endings)
- Lists (inventory system)
- Loops (button creation and animation updates)
- Event-driven programming (button clicks trigger functions)
- tkinter Canvas drawing (graphics)
- Animation using after() loop
- Math module (sin function for smooth animation movement)

IMPORTANT FUNCTIONS IN THE CODE:
- build_ui(): Creates the game window layout
- show_scene(): Updates text, graphics, and choices
- set_scene_art(): Draws each location visually
- draw_player(): Creates animated character
- animate_player(): Runs continuous animation loop
- move_player_to(): Handles movement of the character
- add_item(): Adds items to inventory
- add_memory_fragment(): Tracks memory progression
- show_inventory(): Displays current items

HOW THE GAME WORKS:
1. Player clicks "Start Game"
2. Game shows story + choices as buttons
3. Player clicks options to progress
4. Game updates scenes, inventory, and story
5. Ending is reached based on decisions

TESTING:
The game includes unit tests to verify logic like:
- Inventory system
- Memory fragment counting
- Ending conditions
- Player movement calculations

How to run tests:
python garden_between_lives_game.py --test

How to run game:
python garden_between_lives_game.py

If tkinter is missing, install Python with Tk support from python.org.
"""
