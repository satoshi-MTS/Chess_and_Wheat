fig, ax = plt.subplots()
ax.set_xlabel("column")
ax.set_ylabel("row")
ax.set_title("heatmap of chess board")
ax.invert_yaxis()
plt.pcolor(chess_board_wheal(8, 8))
plt.show()