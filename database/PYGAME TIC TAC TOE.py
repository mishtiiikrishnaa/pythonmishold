import pygame
import mysql.connector
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQ_SIZE = WIDTH // BOARD_COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)
BG_COLOR = (176, 224, 230)

# MySQL Connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="meghnanair"
)
cursor = db_connection.cursor()

# Create database and table
def create_database_and_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS games ("
                   "id INT AUTO_INCREMENT PRIMARY KEY,"
                   "player1 VARCHAR(50) NOT NULL,"
                   "player2 VARCHAR(50) NOT NULL,"
                   "winner VARCHAR(50),"
                   "game_data TEXT,"
                   "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
                   ")")

# Function to draw the board
def draw_board():
    screen.fill(BG_COLOR)
    # Draw grid lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQ_SIZE), (WIDTH, i * SQ_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQ_SIZE, 0), (i * SQ_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw the X or O
def draw_marker(row, col, marker):
    centerX = col * SQ_SIZE + SQ_SIZE // 2
    centerY = row * SQ_SIZE + SQ_SIZE // 2

    if marker == 'X':
        pygame.draw.line(screen, BLACK, (centerX - SQ_SIZE // 4, centerY - SQ_SIZE // 4),
                         (centerX + SQ_SIZE // 4, centerY + SQ_SIZE // 4), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (centerX + SQ_SIZE // 4, centerY - SQ_SIZE // 4),
                         (centerX - SQ_SIZE // 4, centerY + SQ_SIZE // 4), LINE_WIDTH)
    elif marker == 'O':
        pygame.draw.circle(screen, BLACK, (centerX, centerY), SQ_SIZE // 4, LINE_WIDTH)

# Function to check for a winner
def check_winner(board, marker):
    # Check rows
    for row in board:
        if all(cell == marker for cell in row):
            return True

    # Check columns
    for col in range(BOARD_COLS):
        if all(board[row][col] == marker for row in range(BOARD_ROWS)):
            return True

    # Check diagonals
    if all(board[i][i] == marker for i in range(BOARD_ROWS)):
        return True
    if all(board[i][BOARD_COLS - 1 - i] == marker for i in range(BOARD_ROWS)):
        return True

    return False

# Function to save game data to MySQL
def save_game(player1, player2, winner, game_data):
    query = "INSERT INTO games (player1, player2, winner, game_data) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (player1, player2, winner, game_data))
    db_connection.commit()

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Game variables
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player_turn = 'X'
game_over = False

# Create database and table
create_database_and_table()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQ_SIZE
            clicked_col = mouseX // SQ_SIZE

            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = player_turn
                draw_marker(clicked_row, clicked_col, player_turn)

                if check_winner(board, player_turn):
                    game_over = True
                    winner = player_turn
                    save_game('Player 1', 'Player 2', winner, str(board))
                    print(f"Player {player_turn} wins!")

                player_turn = 'O' if player_turn == 'X' else 'X'

    draw_board()
    pygame.display.flip()

pygame.quit()
