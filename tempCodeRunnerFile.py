 # 畫筆與橡皮擦功能
    # - 左鍵按住：畫筆 (黑色圓圈)
    # - 右鍵按住：橡皮擦 (用背景色畫圓)
    # 為了讓筆畫更連續，會記錄上一個位置並用寬線連接
    brush_radius = 8
    brush_color = (0, 0, 0)
    # 使用全域變數 last_pos 存放上一個座標，若不存在則建立
    try:
        last_pos
    except NameError:
        last_pos = None

    mouse_buttons = pygame.mouse.get_pressed()
    # 優先處理左鍵 (畫筆)，再處理右鍵 (橡皮擦)
    if mouse_buttons[0]:
        color = brush_color
        if last_pos is None:
            pygame.draw.circle(bg, color, (mouse_x, mouse_y), brush_radius)
        else:
            pygame.draw.line(bg, color, last_pos, (mouse_x, mouse_y), brush_radius * 2)
        last_pos = (mouse_x, mouse_y)