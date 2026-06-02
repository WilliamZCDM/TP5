"""
William Zheng
Tp5 dessiner avec arcade
407
"""
import arcade

WINDOW_WIDTH = 680
WINDOW_HEIGHT = 952
WINDOW_TITLE = "Pokemon Card Charizard"


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.CORAL

        self.charizard_sprite = arcade.Sprite("charizard.png")
        self.charizard_sprite.position = (340, 670)

        self.charmeleon_sprite = arcade.Sprite("charmeleon.png")
        self.charmeleon_sprite.position = (95, 830)

        self.sprites_list = arcade.SpriteList()
        self.sprites_list.append(self.charizard_sprite)
        self.sprites_list.append(self.charmeleon_sprite)


    def border(self):
        arcade.draw_line(0, 0, 0, 952, arcade.color.GOLD, line_width=60)
        arcade.draw_line(0, 0, 680, 0, arcade.color.GOLD, line_width=90)
        arcade.draw_line(680, 0, 680, 952, arcade.color.GOLD, line_width=60)
        arcade.draw_line(0, 952, 680, 952, arcade.color.GOLD, line_width=90)
        arcade.draw_line(120, 870, 565, 870, arcade.color.GOLD, line_width=1)
        arcade.draw_line(100, 520, 580, 520, arcade.color.GOLDENROD, line_width=7)
        arcade.draw_line(100, 516, 100, 820, arcade.color.GOLDENROD, line_width=7)
        arcade.draw_line(580, 516, 580, 820, arcade.color.GOLDENROD, line_width=7)
        arcade.draw_line(96, 820, 583, 820, arcade.color.GOLDENROD, line_width=7)
        rec = arcade.XYWH(95, 830, 70, 60)
        arcade.draw_rect_filled(rec, arcade.color.GOLDENROD, 90)
        re = arcade.XYWH(95, 830, 70, 60)
        arcade.draw_rect_filled(re, arcade.color.GOLDENROD, 60)
        w = arcade.XYWH(95, 830, 70, 60)
        arcade.draw_rect_filled(w, arcade.color.GOLDENROD, 30)
        r = arcade.XYWH(95, 830, 60, 50)
        arcade.draw_rect_filled(r, arcade.color.ASH_GREY)
        rect = arcade.XYWH(340, 500, 430, 20)
        arcade.draw_rect_filled(rect, arcade.color.GOLDENROD)
        bottom_rectangle = arcade.XYWH(340, 93, 490, 40)
        arcade.draw_rect_outline(bottom_rectangle, arcade.color.GOLDENROD, 3)


    def attack(self):
        arcade.draw_line(70,260, 610, 260, arcade.color.BLACK, line_width=3)
        arcade.draw_line(70, 180, 610, 180, arcade.color.BLACK, line_width=3)
        arcade.draw_text("FIRE SPIN", 150, 220, arcade.color.BLACK, 20, bold=True)
        arcade.draw_text("1", 520, 205, arcade.color.BLACK, 35, bold=True)
        arcade.draw_text("Discard 2 energy attached", 262, 223, arcade.color.BLACK, 14)
        arcade.draw_text("to Charizard in order to use this attack.", 150, 200, arcade.color.BLACK, 14)
        arcade.draw_text("weakness", 97, 163, arcade.color.BLACK,13, bold=True)
        arcade.draw_text("resistance", 300, 163, arcade.color.BLACK, 13, bold=True)
        arcade.draw_text("retreat cost", 510, 163, arcade.color.BLACK, 13, bold=True)


    def cicle_ellipse(self):
        arcade.draw_circle_filled(90, 201, 15, arcade.color.RED)
        arcade.draw_circle_filled(90, 235, 15, arcade.color.RED)
        arcade.draw_circle_filled(124, 201, 15, arcade.color.RED)
        arcade.draw_circle_filled(124, 235, 15, arcade.color.RED)
        arcade.draw_circle_filled(565, 843, 20, arcade.color.RED)
        arcade.draw_circle_filled(128, 143, 15, arcade.color.BLUE)
        arcade.draw_circle_filled(91, 492, 13, arcade.color.BLACK)
        arcade.draw_circle_filled(335, 143, 15, arcade.color.DARK_RED)
        arcade.draw_circle_filled(519, 143, 14, arcade.color.WHITE)
        arcade.draw_circle_filled(551, 143, 14, arcade.color.WHITE)
        arcade.draw_circle_filled(584, 143, 14, arcade.color.WHITE)
        arcade.draw_circle_outline(170, 55, 7, arcade.color.BLACK)
        arcade.draw_circle_outline(480, 55, 7, arcade.color.BLACK)
        arcade.draw_ellipse_outline(579, 221, 23, 33, arcade.color.BLACK, 5)
        arcade.draw_ellipse_outline(554, 221, 23, 33, arcade.color.BLACK, 5)
        points =  [(200, 200), (130, 700), (400, 900)]
        arcade.draw_polygon_filled(points, arcade.color.BALL_BLUE)


    def text(self):
        arcade.draw_text("Charizard", 140, 822, arcade.color.BLACK, 38, bold=True)
        arcade.draw_text("120 HP", 405, 822, arcade.color.RED, 35, bold=True)
        arcade.draw_text("Evolves from Charmeleon", 130, 870, arcade.color.BLACK, 10, bold=True)
        arcade.draw_text("Put  Charizard  on  stage  1  card", 370, 870, arcade.color.BLACK, 14)
        arcade.draw_text("STAGE 2", 65, 860, arcade.color.BLACK, 14, bold=True)
        arcade.draw_text("Flame Pokémon. Length:5' 7'', Weight: 200 lbs.", 172, 495, arcade.color.BLACK, 14, italic=True)
        arcade.draw_text("E D I T I O N", 74, 506, arcade.color.BLACK, 6)
        arcade.draw_text("-30", 355, 136, arcade.color.BLACK, 12, bold=True)
        arcade.draw_text("Spits  fire  that  is  hot  enough  to  melt  boulders. Known  to", 120, 93, arcade.color.BLACK, bold=True)
        arcade.draw_text("unintentionally  cause  forest  fires.  LV.76   #6", 120, 77, arcade.color.BLACK, bold=True)
        arcade.draw_text("Illus. Mitsuhiro Arita", 36, 50, arcade.color.BLACK, 10, bold=True)
        arcade.draw_text("C", 167, 50, arcade.color.BLACK, 9)
        arcade.draw_text("C", 477, 50, arcade.color.BLACK, 9)
        arcade.draw_text("1995 , 96, 98, 99,   Nintendo,   Creatures,   GAMEFREAK", 178, 50, arcade.color.BLACK, 9)
        arcade.draw_text("1999 Wizards.        4/102 ⭐", 490, 50, arcade.color.BLACK, 9)
        arcade.draw_text("Pokémon  Power: Energy Burn", 125, 456, arcade.color.BLUEBERRY, 20, bold=True)
        arcade.draw_text("As often as you", 453, 458, arcade.color.BLACK)
        arcade.draw_text("like  during  your  turn   ( before your attack )    ,   you   may   turn", 125, 425, arcade.color.BLACK)
        arcade.draw_text("all   Energy   attached  to   Charizard  into", 125, 385, arcade.color.BLACK)
        arcade.draw_text("Energy    for    the", 425, 385, arcade.color.BLACK)
        arcade.draw_text("rest   of   the   turn .   This   power   can ' t   be   used   if  Charizard", 125, 345, arcade.color.BLACK)
        arcade.draw_text("is   Asleep,   Confused   , or  Paralyzed", 125, 300, arcade.color.BLACK)


    def emoji(self):
        arcade.draw_text("🔥", 82, 196, arcade.color.BLACK)
        arcade.draw_text("🔥", 82, 230, arcade.color.BLACK)
        arcade.draw_text("🔥", 116, 196, arcade.color.BLACK)
        arcade.draw_text("🔥", 116, 230, arcade.color.BLACK)
        arcade.draw_text("🔥", 556, 836, arcade.color.BLACK, 15)
        arcade.draw_line(87, 495, 92, 497, arcade.color.CORAL, 3)
        arcade.draw_line(91, 497, 92, 487, arcade.color.CORAL, 3)
        arcade.draw_line(87, 487, 95, 487, arcade.color.CORAL, 3)
        arcade.draw_point(335, 143, arcade.color.BLACK, 14)
        arcade.draw_triangle_filled(511, 137, 528, 137, 519, 153, arcade.color.BLACK)
        arcade.draw_triangle_filled(543, 137, 560, 137, 551, 153, arcade.color.BLACK)
        arcade.draw_triangle_filled(575, 137, 592, 137, 583, 153, arcade.color.BLACK)
        arcade.draw_text("🔥", 400, 385, arcade.color.RED)
        arcade.draw_arc_filled(127, 154, 30, 35, arcade.color.BLACK, 250, 285)


    def on_draw(self):

        self.clear()
        self.border()
        self.text()
        self.attack()
        self.cicle_ellipse()
        self.emoji()


        self.sprites_list.draw()


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
