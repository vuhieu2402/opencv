import cv2
import pygame

def count_bottle_caps(frame) :
    #chuyen hinh anh sang mau HSV
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #tao gioi han mau sac
    lower_color = (0,0,0)
    upper_color = (180,255,50)
    
    #tao mat na de loc mau sac trong pham vi gioi han
    mask = cv2.inRange(hsv_img,lower_color, upper_color)
    
    #tim doi tuong co trong khung hinh
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,  contours , -1 , (0,255,0), 1, cv2.LINE_AA)
    
    #dem so luong nap chai
    count = len(contours)
    
    return count

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ game
window_width = 800
window_height = 600

# Tạo cửa sổ game
window = pygame.display.set_mode((window_width, window_height))

# Nút 'Start'
start_button = pygame.Rect(150, 500, 100, 50)
start_button_color = (0, 255, 0)

# Nút 'Stop'
stop_button = pygame.Rect(550, 500, 100, 50)
stop_button_color = (255, 0, 0)

# Biến kiểm tra trạng thái của chương trình
running = False

# Phần chương trình xử lý
def program_loop():
    cam = cv2.VideoCapture(0)

    while running:
        ret , frame = cam.read()

        count = count_bottle_caps(frame)

        cv2.putText(frame,f"Bottle Caps: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Hiển thị khung hình
        cv2.imshow("Bottle Cap Counter", frame)

        # Thoát khỏi vòng lặp nếu nhấn phím 'q' hoặc nút 'Stop'
        if cv2.waitKey(1) & 0xFF == ord('q') or not running:
            break

    cam.release()
    cv2.destroyAllWindows()

# Vòng lặp chính của game
running_game = True
while running_game:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra xem chuột được nhấn vào nút nào
            if event.button == 1:  # Chuột trái
                if start_button.collidepoint(event.pos):
                    running = True
                    program_loop()

                elif stop_button.collidepoint(event.pos):
                    running = False

    # Vẽ background
    window.fill((255, 255, 255))

    # Vẽ nút 'Start'
    pygame.draw.rect(window, start_button_color, start_button)
    pygame.draw.rect(window, (0, 0, 0), start_button, 2)
    font = pygame.font.Font(None, 30)
    text = font.render("Start", True, (0, 0, 0))
    text_rect = text.get_rect(center=start_button.center)
    window.blit(text, text_rect)

    # Vẽ nút 'Stop'
    pygame.draw.rect(window, stop_button_color, stop_button)
    pygame.draw.rect(window, (0, 0, 0), stop_button, 2)
    font = pygame.font.Font(None, 30)
    text = font.render("Stop", True, (0, 0, 0))
    text_rect = text.get_rect(center=stop_button.center)
    window.blit(text, text_rect)

    # Cập nhật giao diện game
    pygame.display.update()

# Kết thúc chương trình Pygame
pygame.quit()
