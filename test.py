def index():
    list_items = ""
    category_list = list(sudoku.keys())
    for category in category_list:
        list_items += f"<li>{category}</li>"
        html = f"<ul>{list_items}</ul>"
    return list_items
sudoku = {"sudoku_spelen":"Hier ga je sudoku spelen",
          "sudoku_oplossen":"Hier ga je sudoku laten oplossen"}
print(index())