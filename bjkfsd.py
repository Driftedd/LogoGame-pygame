pygame.Rect(1500,100,60,60)
leaderboard_button=pygame.draw.rect(screen,(245, 237, 169), pygame.Rect(1500, 30, 52, 52),  2, 3)
screen.blit(leaderboard_icon, (1502,32))
pygame.draw.rect(screen,colour1,textbox_usuario,0)
pygame.draw.rect(screen,colour2,textbox_password,0)
if event.type == pygame.MOUSEBUTTONDOWN:
    if leaderboard_button.collidepoint(event.pos) and gaming == False:
        USER = "Leaderboard"