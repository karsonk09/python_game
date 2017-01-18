import arcade

arcade.open_window("My Drawing", 600, 600)

# Night Sky
arcade.set_background_color((58, 56, 59))

arcade.start_render()

# Grass
arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.color.DARK_GREEN)

# Moon
arcade.draw_circle_filled(525, 525, 50, arcade.color.GHOST_WHITE)

# Cloud
arcade.draw_circle_filled(425, 500, 45, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(380, 525, 56, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(335, 515, 50, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(290, 515, 30, arcade.color.LIGHT_GRAY)

# Stars
arcade.draw_circle_filled(20, 575, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(67, 575, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(300, 575, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(425, 575, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(500, 575, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(38, 532, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(100, 530, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(75, 470, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(10, 470, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(45, 500, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(75, 470, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(120, 450, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(110, 480, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(150, 490, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(155, 510, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(165, 500, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(225, 490, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(210, 520, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(175, 537, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(145, 550, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(200, 555, 2, arcade.color.YELLOW)
arcade.draw_circle_filled(250, 550, 2, arcade.color.YELLOW)


# Fence number 2
arcade.draw_line(0, 250, 600, 250, arcade.color.BLACK, 1)
arcade.draw_line(15, 200, 15, 250, arcade.color.BLACK, 1)
arcade.draw_line(30, 200, 30, 250, arcade.color.BLACK, 1)
arcade.draw_line(45, 200, 45, 250, arcade.color.BLACK, 1)
arcade.draw_line(60, 200, 60, 250, arcade.color.BLACK, 1)
arcade.draw_line(75, 200, 75, 250, arcade.color.BLACK, 1)
arcade.draw_line(90, 200, 90, 250, arcade.color.BLACK, 1)
arcade.draw_line(105, 200, 105, 250, arcade.color.BLACK, 1)
arcade.draw_line(120, 200, 120, 250, arcade.color.BLACK, 1)
arcade.draw_line(135, 200, 135, 250, arcade.color.BLACK, 1)
arcade.draw_line(150, 200, 150, 250, arcade.color.BLACK, 1)
arcade.draw_line(165, 200, 165, 250, arcade.color.BLACK, 1)
arcade.draw_line(180, 200, 180, 250, arcade.color.BLACK, 1)
arcade.draw_line(195, 200, 195, 250, arcade.color.BLACK, 1)
arcade.draw_line(210, 200, 210, 250, arcade.color.BLACK, 1)
arcade.draw_line(225, 200, 225, 250, arcade.color.BLACK, 1)
arcade.draw_line(240, 200, 240, 250, arcade.color.BLACK, 1)
arcade.draw_line(255, 200, 255, 250, arcade.color.BLACK, 1)
arcade.draw_line(270, 200, 270, 250, arcade.color.BLACK, 1)
arcade.draw_line(285, 200, 285, 250, arcade.color.BLACK, 1)
arcade.draw_line(300, 200, 300, 250, arcade.color.BLACK, 1)
arcade.draw_line(315, 200, 315, 250, arcade.color.BLACK, 1)
arcade.draw_line(330, 200, 330, 250, arcade.color.BLACK, 1)
arcade.draw_line(345, 200, 345, 250, arcade.color.BLACK, 1)
arcade.draw_line(360, 200, 360, 250, arcade.color.BLACK, 1)
arcade.draw_line(375, 200, 375, 250, arcade.color.BLACK, 1)
arcade.draw_line(390, 200, 390, 250, arcade.color.BLACK, 1)
arcade.draw_line(405, 200, 405, 250, arcade.color.BLACK, 1)
arcade.draw_line(420, 200, 420, 250, arcade.color.BLACK, 1)
arcade.draw_line(435, 200, 435, 250, arcade.color.BLACK, 1)
arcade.draw_line(450, 200, 450, 250, arcade.color.BLACK, 1)
arcade.draw_line(465, 200, 465, 250, arcade.color.BLACK, 1)
arcade.draw_line(480, 200, 480, 250, arcade.color.BLACK, 1)
arcade.draw_line(495, 200, 495, 250, arcade.color.BLACK, 1)
arcade.draw_line(510, 200, 510, 250, arcade.color.BLACK, 1)
arcade.draw_line(525, 200, 525, 250, arcade.color.BLACK, 1)
arcade.draw_line(540, 200, 540, 250, arcade.color.BLACK, 1)
arcade.draw_line(555, 200, 555, 250, arcade.color.BLACK, 1)
arcade.draw_line(570, 200, 570, 250, arcade.color.BLACK, 1)
arcade.draw_line(585, 200, 585, 250, arcade.color.BLACK, 1)
arcade.draw_line(600, 200, 600, 250, arcade.color.BLACK, 1)

# Graves

arcade.draw_rectangle_filled(75, 75, 50, 65, arcade.color.GRAY)
arcade.draw_arc_filled(75, 100, 25, 20, arcade.color.GRAY, 0, 180)
arcade.draw_text("R.I.P.", 53, 90, arcade.color.BLACK, 17)

arcade.draw_rectangle_filled(125, 125, 50, 65, arcade.color.GRAY)
arcade.draw_arc_filled(125, 150, 25, 20, arcade.color.GRAY, 0, 180)
arcade.draw_text("R.I.P.", 103, 140, arcade.color.BLACK, 17)

# These graves need changed coordinates
arcade.draw_rectangle_filled(200, 100, 50, 65, arcade.color.GRAY)
arcade.draw_arc_filled(200, 125, 25, 20, arcade.color.GRAY, 0, 180)
arcade.draw_text("R.I.P.", 178, 115, arcade.color.BLACK, 17)

arcade.draw_rectangle_filled(250, 175, 50, 65, arcade.color.GRAY)
arcade.draw_arc_filled(250, 200, 25, 20, arcade.color.GRAY, 0, 180)
arcade.draw_text("R.I.P.", 228, 190, arcade.color.BLACK, 17)

arcade.draw_rectangle_filled(425, 75, 50, 65, arcade.color.GRAY)
arcade.draw_arc_filled(425, 100, 25, 20, arcade.color.GRAY, 0, 180)
arcade.draw_text("R.I.P.", 403, 90, arcade.color.BLACK, 17)

arcade.draw_rectangle_filled(400, 150, 50, 65, arcade.color.GRAY)
arcade.draw_arc_filled(400, 175, 25, 20, arcade.color.GRAY, 0, 180)
arcade.draw_text("R.I.P.", 378, 165, arcade.color.BLACK, 17)

arcade.draw_rectangle_filled(500, 175, 50, 65, arcade.color.GRAY)
arcade.draw_arc_filled(500, 200, 25, 20, arcade.color.GRAY, 0, 180)
arcade.draw_text("R.I.P.", 478, 185, arcade.color.BLACK, 17)

arcade.draw_rectangle_filled(535, 75, 50, 65, arcade.color.GRAY)
arcade.draw_arc_filled(535, 100, 25, 20, arcade.color.GRAY, 0, 180)
arcade.draw_text("R.I.P.", 513, 90, arcade.color.BLACK, 17)

arcade.draw_rectangle_filled(50, 195, 50, 65, arcade.color.GRAY)
arcade.draw_arc_filled(50, 220, 25, 20, arcade.color.GRAY, 0, 180)
arcade.draw_text("R.I.P.", 28, 210, arcade.color.BLACK, 17)

# Fence number 1
arcade.draw_line(0, 100, 225, 100, arcade.color.BLACK, border_width=1)
arcade.draw_line(375, 100, 600, 100, arcade.color.BLACK, border_width=1)
arcade.draw_line(20, 0, 20, 100, arcade.color.BLACK, 1)
arcade.draw_line(40, 0, 40, 100, arcade.color.BLACK, 1)
arcade.draw_line(60, 0, 60, 100, arcade.color.BLACK, 1)
arcade.draw_line(80, 0, 80, 100, arcade.color.BLACK, 1)
arcade.draw_line(100, 0, 100, 100, arcade.color.BLACK, 1)
arcade.draw_line(120, 0, 120, 100, arcade.color.BLACK, 1)
arcade.draw_line(140, 0, 140, 100, arcade.color.BLACK, 1)
arcade.draw_line(160, 0, 160, 100, arcade.color.BLACK, 1)
arcade.draw_line(180, 0, 180, 100, arcade.color.BLACK, 1)
arcade.draw_line(200, 0, 200, 100, arcade.color.BLACK, 1)
arcade.draw_line(225, 0, 225, 100, arcade.color.BLACK, 1)
arcade.draw_line(375, 0, 375, 100, arcade.color.BLACK, 1)
arcade.draw_line(400, 0, 400, 100, arcade.color.BLACK, 1)
arcade.draw_line(420, 0, 420, 100, arcade.color.BLACK, 1)
arcade.draw_line(440, 0, 440, 100, arcade.color.BLACK, 1)
arcade.draw_line(460, 0, 460, 100, arcade.color.BLACK, 1)
arcade.draw_line(480, 0, 480, 100, arcade.color.BLACK, 1)
arcade.draw_line(500, 0, 500, 100, arcade.color.BLACK, 1)
arcade.draw_line(520, 0, 520, 100, arcade.color.BLACK, 1)
arcade.draw_line(540, 0, 540, 100, arcade.color.BLACK, 1)
arcade.draw_line(560, 0, 560, 100, arcade.color.BLACK, 1)
arcade.draw_line(580, 0, 580, 100, arcade.color.BLACK, 1)
arcade.draw_line(226, 110, 374, 110, arcade.color.BLACK, 1)
arcade.draw_line(230, 130, 369, 130, arcade.color.BLACK, 1)
arcade.draw_text("CEMETARY", 230, 110, arcade.color.BLACK, 19, font_name="Gungsuh")
arcade.draw_arc_outline(300, 100, 75, 75, arcade.color.BLACK, 0, 180)

arcade.finish_render()

arcade.run()
