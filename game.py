'''cyse 130'''
import tkinter as tk
from tkinter import messagebox
import unittest
import math


class GardenGame:
    def __init__(self, root):
        self.root = root
        self.root.title("The Garden Between Lives")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        self.inventory = []
        self.memory_fragments = 0
        self.darkness = 0
        self.aware = False
        self.current_location = "The Garden"
        self.player_parts = []
        self.player_x = 410
        self.player_y = 175
        self.target_x = 410
        self.walking = False
        self.animation_tick = 0
        self.idle_job = None

        self.bg_color = "#132018"
        self.text_color = "#f2ead3"
        self.button_color = "#314d35"
        self.button_text = "#ffffff"

        self.build_ui()
        self.main_menu()
        self.animate_player()

    def build_ui(self):
        self.root.configure(bg=self.bg_color)

        self.title_label = tk.Label(
            self.root,
            text="The Garden Between Lives",
            font=("Georgia", 28, "bold"),
            bg=self.bg_color,
            fg="#d8c27a"
        )
        self.title_label.pack(pady=20)

        self.canvas = tk.Canvas(
            self.root,
            width=820,
            height=230,
            bg="#1d2d22",
            highlightthickness=3,
            highlightbackground="#8a7f4f"
        )
        self.canvas.pack(pady=10)

        self.story_label = tk.Label(
            self.root,
            text="",
            font=("Georgia", 16),
            wraplength=780,
            justify="center",
            bg=self.bg_color,
            fg=self.text_color
        )
        self.story_label.pack(pady=15)

        self.button_frame = tk.Frame(self.root, bg=self.bg_color)
        self.button_frame.pack(pady=10)

        self.status_label = tk.Label(
            self.root,
            text="Inventory: Empty",
            font=("Arial", 12),
            bg=self.bg_color,
            fg="#c9d6bd"
        )
        self.status_label.pack(pady=10)

    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def set_scene_art(self, scene):
        self.canvas.delete("all")
        self.player_parts = []

        if scene == "garden":
            self.canvas.configure(bg="#1b3b2a")
            self.canvas.create_oval(80, 160, 150, 220, fill="#5e9f55", outline="")
            self.canvas.create_oval(690, 160, 760, 220, fill="#5e9f55", outline="")
            self.canvas.create_rectangle(370, 80, 450, 230, fill="#5d3a1a", outline="")
            self.canvas.create_oval(310, 20, 510, 130, fill="#2f7d46", outline="")
            self.canvas.create_text(410, 35, text="The sky swirls like paint", fill="#f2ead3", font=("Georgia", 16, "italic"))
            self.canvas.create_line(250, 230, 410, 120, fill="#d8c27a", width=3)
            self.canvas.create_line(570, 230, 410, 120, fill="#d8c27a", width=3)

        elif scene == "tea":
            self.canvas.configure(bg="#35272d")
            self.canvas.create_rectangle(90, 120, 730, 175, fill="#6b3f2a", outline="#d8c27a", width=2)
            for x in range(140, 710, 90):
                self.canvas.create_oval(x, 105, x + 45, 130, fill="#f2ead3", outline="#d8c27a")
            self.canvas.create_text(410, 60, text="The Host smiles too widely", fill="#f2ead3", font=("Georgia", 18, "italic"))
            self.canvas.create_oval(385, 75, 435, 125, fill="#f0d5b5", outline="")
            self.canvas.create_arc(392, 88, 428, 118, start=200, extent=140, style="arc", outline="#000", width=2)

        elif scene == "gate":
            self.canvas.configure(bg="#19202b")
            self.canvas.create_rectangle(330, 35, 490, 230, fill="#2d2d2d", outline="#d8c27a", width=3)
            self.canvas.create_line(410, 35, 410, 230, fill="#d8c27a", width=2)
            self.canvas.create_text(410, 110, text="?", fill="#d8c27a", font=("Georgia", 50, "bold"))
            self.canvas.create_text(410, 20, text="The Gatekeeper blocks your path", fill="#f2ead3", font=("Georgia", 16))

        elif scene == "mirror":
            self.canvas.configure(bg="#1c2635")
            for x in [160, 330, 500]:
                self.canvas.create_rectangle(x, 40, x + 120, 220, fill="#b8c7d9", outline="#d8c27a", width=3)
                self.canvas.create_text(x + 60, 130, text="you?", fill="#314d35", font=("Georgia", 18, "italic"))
            self.canvas.create_text(410, 20, text="One reflection does not follow", fill="#f2ead3", font=("Georgia", 16))

        elif scene == "maze":
            self.canvas.configure(bg="#12331f")
            for x in range(80, 760, 120):
                self.canvas.create_rectangle(x, 40, x + 60, 230, fill="#254d2e", outline="")
            self.canvas.create_line(60, 210, 760, 60, fill="#d8c27a", width=4)
            self.canvas.create_text(410, 25, text="The path repeats", fill="#f2ead3", font=("Georgia", 16))

        elif scene == "clock":
            self.canvas.configure(bg="#17151f")
            self.canvas.create_oval(310, 30, 510, 230, fill="#e0d3a4", outline="#d8c27a", width=5)
            self.canvas.create_line(410, 130, 410, 70, fill="#000", width=5)
            self.canvas.create_line(410, 130, 465, 130, fill="#000", width=5)
            self.canvas.create_text(410, 20, text="The clock ticks backward", fill="#f2ead3", font=("Georgia", 16))

        elif scene == "throne":
            self.canvas.configure(bg="#241827")
            self.canvas.create_rectangle(340, 90, 480, 230, fill="#5b1c1c", outline="#d8c27a", width=3)
            self.canvas.create_polygon(340, 90, 410, 30, 480, 90, fill="#7d2424", outline="#d8c27a")
            self.canvas.create_text(410, 55, text="The throne waits", fill="#f2ead3", font=("Georgia", 18, "italic"))

        elif scene == "ending":
            self.canvas.configure(bg="#0e0e12")
            self.canvas.create_text(410, 115, text="The cycle changes...", fill="#d8c27a", font=("Georgia", 28, "bold"))

        self.draw_player()

    def draw_player(self):
        """Draws a simple 2D animated player character."""
        for part in self.player_parts:
            self.canvas.delete(part)
        self.player_parts = []

        bob = math.sin(self.animation_tick / 6) * 3
        leg_swing = math.sin(self.animation_tick / 4) * 8 if self.walking else math.sin(self.animation_tick / 10) * 2
        arm_swing = -leg_swing

        x = self.player_x
        y = self.player_y + bob

        shadow = self.canvas.create_oval(x - 23, y + 43, x + 23, y + 52, fill="#000000", outline="", stipple="gray50")
        body = self.canvas.create_rectangle(x - 12, y - 5, x + 12, y + 30, fill="#263b73", outline="#f2ead3", width=2)
        head = self.canvas.create_oval(x - 14, y - 35, x + 14, y - 7, fill="#d6a77a", outline="#f2ead3", width=2)
        hair = self.canvas.create_arc(x - 15, y - 36, x + 15, y - 10, start=0, extent=180, fill="#2a1b11", outline="#2a1b11")

        left_arm = self.canvas.create_line(x - 12, y + 2, x - 24, y + 20 + arm_swing, fill="#d6a77a", width=5)
        right_arm = self.canvas.create_line(x + 12, y + 2, x + 24, y + 20 - arm_swing, fill="#d6a77a", width=5)
        left_leg = self.canvas.create_line(x - 7, y + 30, x - 15, y + 48 + leg_swing, fill="#1a1a1a", width=6)
        right_leg = self.canvas.create_line(x + 7, y + 30, x + 15, y + 48 - leg_swing, fill="#1a1a1a", width=6)

        eye1 = self.canvas.create_oval(x - 6, y - 24, x - 3, y - 21, fill="#000", outline="")
        eye2 = self.canvas.create_oval(x + 4, y - 24, x + 7, y - 21, fill="#000", outline="")

        self.player_parts = [shadow, left_arm, right_arm, left_leg, right_leg, body, head, hair, eye1, eye2]

    def animate_player(self):
        """Keeps the character moving with idle/walking animation."""
        self.animation_tick += 1

        if self.walking:
            if abs(self.player_x - self.target_x) > 4:
                direction = 1 if self.target_x > self.player_x else -1
                self.player_x += direction * 4
            else:
                self.player_x = self.target_x
                self.walking = False

        self.draw_player()
        self.idle_job = self.root.after(45, self.animate_player)

    def move_player_to(self, x):
        """Moves the player smoothly to a new x position."""
        self.target_x = x
        self.walking = True

    def update_status(self):
        if not self.inventory:
            text = "Inventory: Empty"
        else:
            items = []
            for item in self.inventory:
                if item == "Memory Fragment":
                    items.append(f"Memory Fragment ({self.memory_fragments}/5)")
                else:
                    items.append(item)
            text = "Inventory: " + ", ".join(items)
        self.status_label.config(text=text)

    def show_scene(self, art, story, choices):
        old_x = self.player_x
        self.set_scene_art(art)
        if art == "garden":
            self.player_x = 160
            self.target_x = 410
        elif art == "tea":
            self.player_x = 110
            self.target_x = 360
        elif art == "gate":
            self.player_x = 140
            self.target_x = 300
        elif art == "mirror":
            self.player_x = 120
            self.target_x = 300
        elif art == "maze":
            self.player_x = 80
            self.target_x = 500
        elif art == "clock":
            self.player_x = 170
            self.target_x = 370
        elif art == "throne":
            self.player_x = 150
            self.target_x = 360
        elif art == "ending":
            self.player_x = 410
            self.target_x = 410
        self.walking = old_x != self.target_x
        self.draw_player()
        self.story_label.config(text=story)
        self.clear_buttons()
        self.update_status()

        for label, command in choices:
            btn = tk.Button(
                self.button_frame,
                text=label,
                command=command,
                font=("Arial", 13, "bold"),
                width=28,
                bg=self.button_color,
                fg=self.button_text,
                activebackground="#4e7351",
                activeforeground="#ffffff"
            )
            btn.pack(pady=5)

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
        self.update_status()
        messagebox.showinfo("Item Added", f"{item} added to inventory.")

    def add_memory_fragment(self):
        self.memory_fragments += 1
        if "Memory Fragment" not in self.inventory:
            self.inventory.append("Memory Fragment")
        self.aware = True
        self.update_status()
        messagebox.showinfo("Memory Added", f"Memory Fragment added. ({self.memory_fragments}/5)")

    def show_inventory(self):
        if not self.inventory:
            messagebox.showinfo("Inventory", "Your inventory is empty.")
            return

        lines = []
        for item in self.inventory:
            if item == "Memory Fragment":
                lines.append(f"Memory Fragment ({self.memory_fragments}/5)")
            else:
                lines.append(item)
        messagebox.showinfo("Inventory", "\n".join(lines))

    def main_menu(self):
        self.show_scene(
            "garden",
            "THE GARDEN BETWEEN LIVES\n\nA surreal story about memory, reincarnation, and choice.",
            [
                ("Start Game", self.start_scene),
                ("How to Play", self.how_to_play),
                ("Quit", self.root.destroy),
            ],
        )

    def how_to_play(self):
        self.show_scene(
            "garden",
            "HOW TO PLAY\n\nClick buttons to choose your actions.\nCheck your inventory when needed.\nYour choices affect the ending.",
            [
                ("Back to Main Menu", self.main_menu),
            ],
        )

    def reset_game(self):
        self.inventory = []
        self.memory_fragments = 0
        self.darkness = 0
        self.aware = False
        self.current_location = "The Garden"
        self.update_status()

    def start_scene(self):
        self.reset_game()
        self.show_scene(
            "garden",
            "You wake on cold grass.\nThe sky above you swirls like paint.\n\nA voice echoes:\n\"You're late again.\"\n\nThree paths stretch before you.",
            [
                ("Follow the white figure", self.path_one_tea_party),
                ("Walk into the forest alone", self.path_two_mirror_hall),
                ("Follow the whispering voice", self.path_three_hidden_tunnel),
                ("Check Inventory", self.show_inventory),
            ],
        )

    # PATH 1
    def path_one_tea_party(self):
        self.show_scene(
            "tea",
            "A long table stretches endlessly.\nA figure known as The Host smiles.\n\n\"You made it. You always do.\"\n\nThe Host lifts a cup.\n\"Will you drink?\"",
            [
                ("Drink the tea", self.drink_tea),
                ("Refuse", self.refuse_tea),
                ("Check Inventory", self.show_inventory),
            ],
        )

    def drink_tea(self):
        self.add_item("Tea Vial")
        self.show_scene(
            "tea",
            "The world bends slightly.\nSomething feels... off.\n\nThe Host smiles like this already happened.",
            [
                ("Continue to the Gatekeeper", self.gatekeeper),
                ("Check Inventory", self.show_inventory),
            ],
        )

    def refuse_tea(self):
        self.show_scene(
            "tea",
            "The Host's smile fades.\n\n\"How disappointing.\"\n\n[The Host will remember this]",
            [
                ("Continue to the Gatekeeper", self.gatekeeper),
                ("Check Inventory", self.show_inventory),
            ],
        )

    def gatekeeper(self):
        choices = [("Solve riddle", self.riddle_scene)]
        if "Tea Vial" in self.inventory:
            choices.append(("Use Tea Vial", self.use_tea_at_gate))
        choices.append(("Check Inventory", self.show_inventory))

        self.show_scene(
            "gate",
            "A tall figure blocks your path.\n\n\"Answer correctly... or remain.\"",
            choices,
        )

    def riddle_scene(self):
        self.show_scene(
            "gate",
            "Riddle:\n\nI disappear when named.\nWhat am I?",
            [
                ("Silence", self.correct_riddle),
                ("A shadow", self.wrong_riddle),
                ("A dream", self.wrong_riddle),
            ],
        )

    def correct_riddle(self):
        self.show_scene(
            "gate",
            "The Gatekeeper steps aside.\n\n\"Correct. For now.\"",
            [
                ("Go to the glowing door", self.loop_ending_choice),
            ],
        )

    def wrong_riddle(self):
        self.darkness += 1
        self.show_scene(
            "gate",
            "The Gatekeeper stares through you.\n\n\"Wrong. But the garden is merciful today.\"",
            [
                ("Go to the glowing door", self.loop_ending_choice),
            ],
        )

    def use_tea_at_gate(self):
        self.darkness += 1
        self.show_scene(
            "gate",
            "You pour the tea onto the roots beneath the gate.\nThe gate opens, but something feels wrong.\n\n[Something has changed]",
            [
                ("Go to the glowing door", self.loop_ending_choice),
            ],
        )

    def loop_ending_choice(self):
        self.show_scene(
            "garden",
            "You reach a glowing door.\nThe Host appears beside it.\n\nDo you trust them?",
            [
                ("Trust the Host", self.loop_ending),
                ("Distrust the Host", self.loop_ending),
            ],
        )

    def loop_ending(self):
        self.show_ending(
            "ENDING A: LOOP ENDING",
            "You step through the door.\nLight blinds you.\n\n...\n\nYou wake on cold grass.\n\n\"You're late again.\"",
        )

    # PATH 2
    def path_two_mirror_hall(self):
        self.show_scene(
            "mirror",
            "You enter a hall of mirrors.\nOne reflection does not follow you.\n\n\"You chose differently last time.\"",
            [
                ("Touch the mirror", self.touch_mirror),
                ("Ignore it", self.ignore_mirror),
                ("Check Inventory", self.show_inventory),
            ],
        )

    def touch_mirror(self):
        self.add_memory_fragment()
        self.show_scene(
            "mirror",
            "A memory flashes through your mind.\nYou remember cold grass, the voice, and the feeling that this has happened before.",
            [
                ("Enter the Maze", self.maze),
            ],
        )

    def ignore_mirror(self):
        self.show_scene(
            "mirror",
            "You walk away, but your reflection stays behind.\nIt looks disappointed.",
            [
                ("Enter the Maze", self.maze),
            ],
        )

    def maze(self):
        choices = [("Follow instinct", self.maze_instinct)]
        if self.memory_fragments > 0:
            choices.append(("Use memory", self.maze_memory))
        choices.append(("Check Inventory", self.show_inventory))

        self.show_scene(
            "maze",
            "The paths repeat.\nThe same tree appears again and again.\nYou feel stuck.",
            choices,
        )

    def maze_instinct(self):
        self.darkness += 1
        self.show_scene(
            "maze",
            "You follow your instinct.\nYou loop for what feels like hours before finally escaping.",
            [
                ("Go to the Clock Tower", self.clock_tower),
            ],
        )

    def maze_memory(self):
        self.add_item("Key of Roots")
        self.show_scene(
            "maze",
            "You remember the false path and turn away from it.\nThe maze opens for you.",
            [
                ("Go to the Clock Tower", self.clock_tower),
            ],
        )

    def clock_tower(self):
        self.show_scene(
            "clock",
            "A massive clock ticks loudly above you.\nThe hands move backward, then forward, then stop.",
            [
                ("Reset the clock", self.partial_freedom_ending),
                ("Break the clock", self.aware_loop_ending),
                ("Check Inventory", self.show_inventory),
            ],
        )

    def partial_freedom_ending(self):
        self.show_ending(
            "ENDING B: PARTIAL FREEDOM",
            "Time resets.\nThe world shifts.\nYou fall into darkness...\n\nYou are not fully free, but something has changed.",
        )

    def aware_loop_ending(self):
        self.show_ending(
            "ENDING C: AWARE LOOP",
            "The clock shatters.\nYou remain—\n\nbut now you remember everything.",
        )

    # PATH 3
    def path_three_hidden_tunnel(self):
        self.aware = True
        self.add_memory_fragment()
        self.add_memory_fragment()
        self.inventory.append("Broken Pocket Watch")
        self.inventory.append("Mask Fragment")
        self.update_status()

        self.show_scene(
            "maze",
            "You already know this place.\nYou remember everything.\n\n[Broken Pocket Watch Added]\n[Mask Fragment Added]",
            [
                ("Face the NPCs", self.npc_confrontations),
                ("Check Inventory", self.show_inventory),
            ],
        )

    def npc_confrontations(self):
        self.show_scene(
            "mirror",
            "You face those who wronged you.\nThe White Messenger, The Host, and the Mirror Twin stand before you.",
            [
                ("Forgive them", self.forgive_npcs),
                ("Take revenge", self.revenge_npcs),
            ],
        )

    def forgive_npcs(self):
        self.darkness -= 1
        self.show_scene(
            "mirror",
            "Their faces soften.\nThe garden becomes quiet.\n\n[Something has changed]",
            [
                ("Enter the Throne Room", self.throne_room),
            ],
        )

    def revenge_npcs(self):
        self.darkness += 2
        self.show_scene(
            "mirror",
            "The sky darkens.\nThe flowers close like fists.\n\n[The world becomes darker]",
            [
                ("Enter the Throne Room", self.throne_room),
            ],
        )

    def throne_room(self):
        self.show_scene(
            "throne",
            "The Host sits calmly on a silver throne.\n\n\"So... you remember.\"\n\nThis is your final choice.",
            [
                ("Destroy the system", self.destroy_system),
                ("Take control", self.dark_ruler_ending),
                ("Let go", self.true_ending),
                ("Check Inventory", self.show_inventory),
            ],
        )

    def destroy_system(self):
        if self.darkness >= 2:
            self.corruption_ending()
        else:
            self.true_ending()

    def dark_ruler_ending(self):
        self.show_ending(
            "ENDING D: DARK RULER",
            "You take the throne.\nThe garden bows.\n\n\"They're late again.\"",
        )

    def true_ending(self):
        self.show_ending(
            "ENDING E: TRUE ENDING",
            "The world collapses.\nThe garden, the mirrors, the clock, and the throne all fade.\n\nYou wake up.\nFor the first time—it's real.",
        )

    def corruption_ending(self):
        self.show_ending(
            "ENDING F: CORRUPTION",
            "You destroy everything.\nFor one second, you feel free.\n\nThen something worse replaces it.",
        )

    def show_ending(self, title, text):
        self.show_scene(
            "ending",
            f"{title}\n\n{text}",
            [
                ("Play Again", self.start_scene),
                ("Main Menu", self.main_menu),
                ("Quit", self.root.destroy),
            ],
        )


class TestGameLogic(unittest.TestCase):
    def test_inventory_adds_item_once(self):
        inventory = []
        item = "Tea Vial"
        if item not in inventory:
            inventory.append(item)
        if item not in inventory:
            inventory.append(item)
        self.assertEqual(inventory.count(item), 1)

    def test_memory_fragment_count(self):
        memory_fragments = 0
        memory_fragments += 1
        memory_fragments += 1
        self.assertEqual(memory_fragments, 2)

    def test_corruption_logic(self):
        darkness = 2
        ending = "Corruption" if darkness >= 2 else "True Ending"
        self.assertEqual(ending, "Corruption")

    def test_true_ending_logic(self):
        darkness = -1
        ending = "Corruption" if darkness >= 2 else "True Ending"
        self.assertEqual(ending, "True Ending")

    def test_player_movement_target(self):
        player_x = 100
        target_x = 140
        direction = 1 if target_x > player_x else -1
        player_x += direction * 4
        self.assertEqual(player_x, 104)


def run_game():
    root = tk.Tk()
    GardenGame(root)
    root.mainloop()


if __name__ == "__main__":
    import sys

    if "--test" in sys.argv:
        unittest.main(argv=[sys.argv[0]])
    else:
        run_game()

"some one add our names to the ending ""
