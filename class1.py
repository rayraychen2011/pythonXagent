######################匯入模組######################
import pygame
import sys

######################初始化######################
pygame.init()  # 啟動Pygame
clock = pygame.time.Clock()  # 建立時鐘物件 (可控制遊戲迴圈速率)
width = 640  # 設定視窗寬度
height = 320  # 設定視窗高度

######################建立視窗及物件######################
screen = pygame.display.set_mode((width, height))  # 設定視窗大小
pygame.display.set_caption("My Game")  # 設定視窗標題
#######################建立畫布######################
bg = pygame.Surface((width, height))  # 建立一個畫布
bg_color = (31, 255, 235)
bg.fill(bg_color)  # 將畫布填滿顏色
#####################繪製圖形######################
# 以下範例示範如何使用 Pygame 的繪圖函式在 `bg` Surface 上畫基本幾何圖形。
# 常見函式與參數簡述：
# - pygame.draw.rect(surface, color, rect, width=0)
#   rect 為 (x, y, w, h)，width=0 表示填滿，>0 表示描邊線寬。
# - pygame.draw.circle(surface, color, center, radius, width=0)
#   center 為 (x, y)，width 同上。
# - pygame.draw.ellipse(surface, color, rect, width=0)
#   在指定 rect 內繪製橢圓。
# - pygame.draw.polygon(surface, color, pointlist, width=0)
#   pointlist 為多邊形頂點清單。
# - pygame.draw.line(surface, color, start_pos, end_pos, width=1)
# - pygame.draw.aaline(surface, color, start_pos, end_pos)
# - pygame.draw.arc(surface, color, rect, start_angle, stop_angle, width=1)
#   角度以弧度表示；此範例使用近似值 3.14 以避免引入 math 模組。
#
# 顏色以 RGB 三元組表示；所有圖形都直接畫在 `bg` 畫布上，最後由主迴圈貼到視窗。

# 紅色填滿矩形（左上） - rect=(x, y, w, h)
pygame.draw.rect(bg, (255, 0, 0), (20, 20, 120, 80))
# 黑色矩形描邊（左上偏右） - width=4 表示描邊
pygame.draw.rect(bg, (0, 0, 0), (160, 20, 120, 80), 4)

# 藍色填滿圓（左中） - center, radius
pygame.draw.circle(bg, (0, 0, 255), (90, 160), 40)
# 白色圓形描邊（中左） - width=5 為描邊粗細
pygame.draw.circle(bg, (255, 255, 255), (250, 160), 40, 5)

# 橙色橢圓（右上） - 橢圓放在 rect 內填滿
pygame.draw.ellipse(bg, (255, 165, 0), (320, 20, 200, 100))
# 綠色橢圓描邊（右中） - width=4
pygame.draw.ellipse(bg, (0, 128, 0), (320, 140, 200, 80), 4)

# 紫色三角形（左下） - polygon 頂點順序 (x, y)
pygame.draw.polygon(bg, (128, 0, 128), [(50, 240), (20, 300), (100, 300)])
# 金色五邊形（中下） - 五個頂點
pygame.draw.polygon(
    bg, (255, 215, 0), [(150, 240), (130, 300), (170, 320), (210, 300), (190, 260)]
)

# 黑色直線（中右） - width=3
pygame.draw.line(bg, (0, 0, 0), (260, 240), (380, 320), 3)
# 抗鋸齒線段（中右偏下） - aaline 提供平滑線條
pygame.draw.aaline(bg, (0, 0, 0), (260, 320), (380, 240))

# 半圓弧（右下） - arc 在 rect 內繪製弧線，使用 0 到 ~3.14 的弧度
pygame.draw.arc(bg, (0, 0, 0), (420, 220, 150, 80), 0, 3.14, 3)

# 模擬半透明矩形：此處用較淡的顏色填滿，若要真正半透明可使用 convert_alpha() 的 Surface
pygame.draw.rect(bg, (200, 200, 255), (440, 40, 140, 60), 0)


######################循環偵測######################
while True:
    clock.tick(60)  # 設定遊戲迴圈速率為每秒60次(FPS=60)
    for event in pygame.event.get():  # 偵測所有事件
        if event.type == pygame.QUIT:  # 如果點擊視窗的X按鈕
            pygame.quit()  # 關閉Pygame
            sys.exit()  # 結束程式

        # 偵測滑鼠有無按下
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 滑鼠左鍵
                print("左鍵按下")
            if event.button == 2:  # 滑鼠中鍵
                print("中鍵按下")
            if event.button == 3:  # 滑鼠右鍵
                print("右鍵按下")

    # 讀取滑鼠座標
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(f"滑鼠座標：({mouse_x}, {mouse_y})")

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
    elif mouse_buttons[2]:
        color = bg_color
        if last_pos is None:
            pygame.draw.circle(bg, color, (mouse_x, mouse_y), brush_radius)
        else:
            pygame.draw.line(bg, color, last_pos, (mouse_x, mouse_y), brush_radius * 2)
        last_pos = (mouse_x, mouse_y)
    else:
        last_pos = None

    screen.blit(bg, (0, 0))  # 將畫布貼到視窗左上角
    pygame.display.update()  # 更新視窗內容
