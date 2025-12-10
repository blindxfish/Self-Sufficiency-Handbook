#!/usr/bin/env python3
"""
Generate COMPLETE planting grid using ALL space efficiently.
Includes succession planting and all missing plants.
"""

import csv

ROWS = 30
COLS = 100
grid = [['' for _ in range(COLS)] for _ in range(ROWS)]

def place_plant(row_start, col_start, row_end, col_end, plant_num):
    """Place a plant in the grid, only if cell is empty."""
    for row in range(row_start, min(row_end + 1, ROWS)):
        for col in range(col_start, min(col_end + 1, COLS)):
            if grid[row][col] == '':
                grid[row][col] = plant_num

def place_single(row, col, plant_num):
    """Place a single plant in one cell."""
    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == '':
        grid[row][col] = plant_num

# ===== TREES (Rows 1-13, North edge) =====
# Fruit trees
place_plant(0, 0, 3, 3, '69')  # Apple 1 (16 m²)
place_plant(0, 5, 3, 8, '69')  # Apple 2
place_plant(0, 10, 3, 13, '69')  # Apple 3
place_plant(0, 20, 3, 23, '70')  # Pear 1 (16 m²)
place_plant(0, 25, 3, 28, '70')  # Pear 2
place_plant(0, 35, 3, 38, '71')  # Plum 1 (12 m²)
place_plant(0, 40, 3, 43, '71')  # Plum 2
place_plant(0, 50, 3, 53, '72')  # Cherry 1 (12 m²)
place_plant(0, 55, 3, 58, '72')  # Cherry 2
place_plant(0, 65, 3, 68, '73')  # Apricot (12 m²)
place_plant(0, 75, 3, 78, '74')  # Quince (12 m²)

# Nut trees (larger spacing)
place_plant(4, 0, 8, 4, '84')  # Walnut 1 (25 m²)
place_plant(4, 6, 8, 10, '84')  # Walnut 2
place_plant(4, 12, 8, 16, '84')  # Walnut 3
place_plant(4, 18, 8, 22, '84')  # Walnut 4
place_plant(4, 24, 8, 28, '84')  # Walnut 5
place_plant(4, 30, 7, 32, '85')  # Hazelnut 1 (9 m²)
place_plant(4, 34, 7, 36, '85')  # Hazelnut 2
place_plant(4, 38, 7, 40, '85')  # Hazelnut 3
place_plant(4, 42, 7, 44, '85')  # Hazelnut 4
place_plant(8, 30, 11, 33, '86')  # Almond 1 (16 m²)
place_plant(8, 35, 11, 38, '86')  # Almond 2
place_plant(8, 40, 11, 43, '86')  # Almond 3
place_plant(8, 50, 12, 54, '87')  # Chestnut 1 (25 m²)
place_plant(8, 56, 12, 60, '87')  # Chestnut 2

# Support trees
place_plant(9, 0, 12, 3, '88')  # Black Locust 1 (16 m²)
place_plant(9, 5, 12, 8, '88')  # Black Locust 2
place_plant(9, 10, 12, 13, '88')  # Black Locust 3
place_plant(9, 15, 12, 18, '88')  # Black Locust 4
place_plant(9, 20, 12, 23, '88')  # Black Locust 5
place_plant(9, 65, 12, 68, '89')  # Elder 1 (12 m²)
place_plant(9, 70, 12, 73, '89')  # Elder 2

# ===== SHRUBS (Rows 14-23) =====
# Berry shrubs
for i in range(20):  # Raspberry canes (0.5 m² each = 10 m² total)
    row = 14 + (i % 2)
    col = (i // 2) * 2
    place_single(row, col, '75')

for i in range(10):  # Blackberry canes (1 m² each = 10 m² total)
    row = 16 + (i % 2)
    col = 25 + (i // 2) * 3
    place_plant(row, col, row+1, col+1, '76')

for i in range(5):  # Red Currant (2 m² each = 10 m²)
    row = 18
    col = 45 + i * 3
    place_plant(row, col, row+1, col+1, '77')

for i in range(5):  # Black Currant (2 m² each = 10 m²)
    row = 20
    col = 45 + i * 3
    place_plant(row, col, row+1, col+1, '78')

for i in range(5):  # Gooseberry (2 m² each = 10 m²)
    row = 18
    col = 60 + i * 3
    place_plant(row, col, row+1, col+1, '79')

for i in range(3):  # Elderberry (4 m² each = 12 m²)
    row = 20
    col = 0 + i * 4
    place_plant(row, col, row+1, col+1, '80')

for i in range(3):  # Sea Buckthorn (4 m² each = 12 m²)
    row = 22
    col = 0 + i * 4
    place_plant(row, col, row+1, col+1, '81')

for i in range(3):  # Jostaberry (2 m² each = 6 m²)
    row = 20
    col = 15 + i * 3
    place_plant(row, col, row+1, col+1, '82')

for i in range(3):  # Aronia (2 m² each = 6 m²)
    row = 22
    col = 15 + i * 3
    place_plant(row, col, row+1, col+1, '83')

# Support shrubs
for i in range(5):  # Siberian Pea Shrub (2 m² each = 10 m²)
    row = 18
    col = 30 + i * 3
    place_plant(row, col, row+1, col+1, '90')

for i in range(3):  # Goumi (2 m² each = 6 m²)
    row = 20
    col = 45 + i * 3
    place_plant(row, col, row+1, col+1, '91')

for i in range(3):  # Autumn Olive (2 m² each = 6 m²)
    row = 22
    col = 30 + i * 3
    place_plant(row, col, row+1, col+1, '92')

for i in range(2):  # Serviceberry (2 m² each = 4 m²)
    row = 22
    col = 45 + i * 3
    place_plant(row, col, row+1, col+1, '93')

# ===== PERENNIAL VEGETABLES (Row 23) =====
place_plant(23, 60, 23, 84, '50')  # Asparagus (25 m²)
place_plant(23, 85, 23, 94, '51')  # Rhubarb (10 m²)
place_plant(23, 95, 23, 99, '52')  # Artichoke (10 m²)

# ===== ANNUAL BEDS (Rows 24-30) =====
# Large calorie crops first
place_plant(24, 0, 24, 19, '8')  # Potatoes (20 m²)
place_plant(24, 20, 24, 23, '29')  # Wheat (4 m²)
place_plant(24, 24, 24, 26, '30')  # Oats (3 m²)
place_plant(24, 27, 24, 29, '31')  # Barley (3 m²)
place_plant(24, 30, 24, 30, '32')  # Quinoa (1 m²)
place_plant(24, 31, 24, 31, '33')  # Amaranth (1 m²)
place_plant(24, 32, 24, 34, '34')  # Buckwheat (3 m²)
place_plant(24, 35, 24, 36, '35')  # Millet (2 m²)
place_plant(24, 37, 24, 39, '36')  # Rye (3 m²)

# Legumes (protein sources) - 18 m² total
place_plant(24, 40, 24, 41, '21')  # Lentil (2 m²)
place_plant(24, 42, 24, 43, '22')  # Chickpea (2 m²)
place_plant(24, 44, 24, 45, '3')  # Bean (2 m²)
place_plant(24, 46, 24, 47, '23')  # Fava Bean (2 m²)
place_plant(24, 48, 24, 49, '4')  # Pea (2 m²)
place_plant(24, 50, 24, 51, '24')  # Black Bean (2 m²)
place_plant(24, 52, 24, 53, '25')  # Kidney Bean (2 m²)
place_plant(24, 54, 24, 54, '26')  # Navy Bean (1 m²)
place_plant(24, 55, 24, 55, '27')  # Lima Bean (1 m²)
place_plant(24, 56, 24, 57, '28')  # Soybean (2 m²)

# Fat sources
place_plant(24, 60, 24, 61, '47')  # Sunflower (2 m²)
place_plant(24, 62, 24, 62, '48')  # Flax (1 m²)
place_plant(24, 63, 24, 63, '49')  # Hemp (1 m²)

# Vegetables with companions
place_plant(25, 0, 25, 7, '1')  # Tomatoes (8 m²)
place_single(25, 1, '18')  # Basil interplanted
place_single(25, 3, '18')
place_single(25, 5, '18')
place_single(25, 7, '18')

place_plant(25, 10, 25, 13, '6')  # Carrots (4 m²)
place_plant(25, 14, 25, 22, '7')  # Onions (9 m²) - companion to carrots

place_plant(25, 25, 25, 29, '2')  # Peppers (5 m²)
place_plant(25, 30, 25, 35, '5')  # Cabbage (4 m²)
place_plant(25, 36, 25, 40, '44')  # Broccoli (5 m²)
place_plant(25, 41, 25, 44, '45')  # Cauliflower (4 m²)
place_plant(25, 45, 25, 47, '46')  # Brussels Sprouts (3 m²)

place_plant(25, 50, 25, 55, '12')  # Lettuce (6 m²)
place_plant(25, 56, 25, 60, '14')  # Spinach (5 m²)
place_plant(25, 61, 25, 62, '15')  # Kale (3 m²)
place_plant(25, 63, 25, 64, '41')  # Chard (2 m²)
place_plant(25, 65, 25, 66, '42')  # Arugula (2 m²)
place_plant(25, 67, 25, 68, '43')  # Mizuna (2 m²)

place_plant(25, 70, 25, 72, '16')  # Beets (3 m²)
place_plant(25, 73, 25, 75, '38')  # Turnips (3 m²)
place_plant(25, 76, 25, 77, '13')  # Radish (2 m²)
place_plant(25, 78, 25, 80, '39')  # Parsnip (3 m²)

place_plant(25, 85, 25, 87, '17')  # Garlic (3 m²)
place_plant(25, 88, 25, 89, '40')  # Leeks (2 m²)

# More vegetables
place_plant(26, 0, 26, 3, '3')  # Beans (4 m² - more for yield)
place_plant(26, 5, 26, 6, '4')  # Peas (2 m²)
place_plant(26, 10, 26, 19, '9')  # Corn (10 m²)
place_plant(26, 20, 26, 24, '10')  # Squash summer (5 m²)
place_plant(26, 25, 26, 34, '10')  # Squash winter (10 m²)
place_plant(26, 35, 26, 39, '11')  # Cucumbers (5 m²)
place_plant(26, 40, 26, 45, '37')  # Sweet Potato (6 m²)

# Succession planting areas (spring → fall)
# Peas then Lettuce
place_plant(26, 50, 26, 51, '4;12')  # Pea → Lettuce
place_plant(26, 52, 26, 53, '4;12')
place_plant(26, 54, 26, 55, '4;12')
place_plant(26, 56, 26, 57, '4;12')

# Lentil then Wheat
place_plant(26, 60, 26, 61, '21;29')  # Lentil → Wheat
place_plant(26, 62, 26, 63, '21;29')

# Radish then Spinach
place_plant(26, 70, 26, 71, '13;14')  # Radish → Spinach
place_plant(26, 72, 26, 73, '13;14')

# More succession
place_plant(27, 0, 27, 1, '13;12')  # Radish → Lettuce
place_plant(27, 2, 27, 3, '13;12')
place_plant(27, 5, 27, 6, '4;14')  # Pea → Spinach
place_plant(27, 7, 27, 8, '4;14')

# Fill remaining space with more vegetables
place_plant(27, 10, 27, 19, '1')  # More Tomatoes (10 m²)
place_plant(27, 20, 27, 24, '2')  # More Peppers (5 m²)
place_plant(27, 25, 27, 29, '6')  # More Carrots (5 m²)
place_plant(27, 30, 27, 34, '7')  # More Onions (5 m²)
place_plant(27, 35, 27, 39, '12')  # More Lettuce (5 m²)
place_plant(27, 40, 27, 44, '14')  # More Spinach (5 m²)
place_plant(27, 45, 27, 49, '16')  # More Beets (5 m²)
place_plant(27, 50, 27, 54, '5')  # More Cabbage (5 m²)
place_plant(27, 55, 27, 59, '44')  # More Broccoli (5 m²)
place_plant(27, 60, 27, 64, '45')  # More Cauliflower (5 m²)
place_plant(27, 65, 27, 69, '46')  # More Brussels Sprouts (5 m²)
place_plant(27, 70, 27, 74, '15')  # More Kale (5 m²)
place_plant(27, 75, 27, 79, '41')  # More Chard (5 m²)
place_plant(27, 80, 27, 84, '42')  # More Arugula (5 m²)
place_plant(27, 85, 27, 89, '43')  # More Mizuna (5 m²)
place_plant(27, 90, 27, 94, '38')  # More Turnips (5 m²)
place_plant(27, 95, 27, 99, '39')  # More Parsnip (5 m²)

# Row 28 - More crops
place_plant(28, 0, 28, 9, '8')  # More Potatoes (10 m²)
place_plant(28, 10, 28, 19, '29')  # More Wheat (10 m²)
place_plant(28, 20, 28, 29, '30')  # More Oats (10 m²)
place_plant(28, 30, 28, 39, '31')  # More Barley (10 m²)
place_plant(28, 40, 28, 49, '3')  # More Beans (10 m²)
place_plant(28, 50, 28, 59, '4')  # More Peas (10 m²)
place_plant(28, 60, 28, 69, '21')  # More Lentils (10 m²)
place_plant(28, 70, 28, 79, '22')  # More Chickpeas (10 m²)
place_plant(28, 80, 28, 89, '23')  # More Fava Beans (10 m²)
place_plant(28, 90, 28, 99, '24')  # More Black Beans (10 m²)

# Row 29 - More crops
place_plant(29, 0, 29, 9, '25')  # More Kidney Beans (10 m²)
place_plant(29, 10, 29, 19, '28')  # More Soybeans (10 m²)
place_plant(29, 20, 29, 29, '9')  # More Corn (10 m²)
place_plant(29, 30, 29, 39, '10')  # More Squash (10 m²)
place_plant(29, 40, 29, 49, '11')  # More Cucumbers (10 m²)
place_plant(29, 50, 29, 59, '37')  # More Sweet Potatoes (10 m²)
place_plant(29, 60, 29, 69, '47')  # More Sunflowers (10 m²)
place_plant(29, 70, 29, 79, '48')  # More Flax (10 m²)
place_plant(29, 80, 29, 89, '49')  # More Hemp (10 m²)
place_plant(29, 90, 29, 99, '8')  # More Potatoes (10 m²)

# ===== HERBS (borders and interplanted) =====
place_plant(23, 0, 23, 1, '58')  # Oregano (1 m²)
place_plant(23, 2, 23, 2, '59')  # Thyme (1 m²)
place_plant(23, 3, 23, 4, '60')  # Rosemary (2 m²)
place_plant(23, 5, 23, 5, '61')  # Sage (1 m²)
place_plant(23, 6, 23, 7, '62')  # Mint (2 m²)
place_plant(23, 8, 23, 9, '63')  # Parsley (2 m²)
place_plant(23, 10, 23, 10, '64')  # Dill (1 m²)
place_plant(23, 11, 23, 11, '65')  # Coriander (1 m²)
place_plant(23, 12, 23, 12, '66')  # Fennel (1 m²)
place_plant(23, 13, 23, 13, '67')  # Marjoram (1 m²)
place_plant(23, 14, 23, 14, '68')  # Tarragon (1 m²)

# ===== PEST DETERRENTS (borders) =====
place_plant(23, 15, 23, 17, '19')  # Marigold (3 m²)
place_plant(23, 18, 23, 22, '20')  # Nasturtium (5 m²)
place_plant(23, 23, 23, 24, '101')  # Tansy (2 m²)

# ===== NITROGEN FIXERS (interplanted) =====
place_plant(24, 20, 24, 24, '94')  # White Clover (5 m²)
place_plant(25, 30, 25, 34, '95')  # Red Clover (5 m²)
place_plant(26, 60, 26, 67, '96')  # Vetch (8 m²)
place_plant(27, 0, 27, 2, '97')  # Alfalfa (3 m²)
place_plant(28, 0, 28, 7, '98')  # Lupine (8 m²)
place_plant(29, 0, 29, 1, '99')  # Field Pea (2 m²)
place_plant(29, 2, 29, 2, '100')  # Fenugreek (2 m²)

# ===== LIVING MULCHES =====
place_plant(23, 25, 23, 27, '102')  # Comfrey (3 m²)
place_plant(23, 28, 23, 29, '103')  # Yarrow (2 m²)
place_plant(23, 30, 23, 31, '104')  # Chamomile (2 m²)

# ===== FILL REMAINING SPACE WITH ADDITIONAL CROPS =====
# Add more of everything to meet yield requirements and use space efficiently

# More grains in empty spaces
place_plant(26, 70, 26, 79, '29')  # More Wheat (10 m²)
place_plant(26, 80, 26, 89, '30')  # More Oats (10 m²)
place_plant(26, 90, 26, 99, '31')  # More Barley (10 m²)

# More legumes
place_plant(27, 0, 27, 9, '21')  # More Lentils (10 m²) - overwrite some succession
place_plant(27, 10, 27, 19, '22')  # More Chickpeas (10 m²)
place_plant(27, 20, 27, 29, '23')  # More Fava Beans (10 m²)
place_plant(27, 30, 27, 39, '24')  # More Black Beans (10 m²)
place_plant(27, 40, 27, 49, '25')  # More Kidney Beans (10 m²)
place_plant(27, 50, 27, 59, '26')  # More Navy Beans (10 m²)
place_plant(27, 60, 27, 69, '27')  # More Lima Beans (10 m²)
place_plant(27, 70, 27, 79, '28')  # More Soybeans (10 m²)

# Fill ALL remaining empty spaces systematically
# Check each cell and fill if empty

def fill_empty_spaces():
    """Fill remaining empty cells with appropriate crops."""
    # Priority: grains, legumes, vegetables that can be succession planted
    
    # Fill empty cells in rows 24-30 with additional crops
    for row in range(24, ROWS):
        for col in range(COLS):
            if grid[row][col] == '':
                # Use succession planting to maximize space
                # Pattern: early crop;late crop
                if row == 24 and col >= 60:
                    # Row 24: grains and legumes
                    if col < 70:
                        grid[row][col] = '29'  # Wheat
                    elif col < 80:
                        grid[row][col] = '30'  # Oats
                    elif col < 90:
                        grid[row][col] = '31'  # Barley
                    else:
                        grid[row][col] = '36'  # Rye
                elif row == 25 and col >= 70:
                    # Row 25: more vegetables
                    if col < 80:
                        grid[row][col] = '16'  # Beets
                    elif col < 90:
                        grid[row][col] = '38'  # Turnips
                    else:
                        grid[row][col] = '13'  # Radish
                elif row == 26 and col >= 70:
                    # Row 26: succession plantings
                    if col < 80:
                        grid[row][col] = '4;12'  # Pea;Lettuce
                    elif col < 90:
                        grid[row][col] = '21;29'  # Lentil;Wheat
                    else:
                        grid[row][col] = '13;14'  # Radish;Spinach
                elif row == 27 and col >= 80:
                    # Row 27: more vegetables
                    if col < 90:
                        grid[row][col] = '38'  # Turnips
                    else:
                        grid[row][col] = '39'  # Parsnip
                elif row == 28 and col >= 80:
                    # Row 28: more legumes
                    if col < 90:
                        grid[row][col] = '23'  # Fava Bean
                    else:
                        grid[row][col] = '24'  # Black Bean
                elif row == 29 and col >= 90:
                    # Row 29: more crops
                    grid[row][col] = '8'  # Potatoes
                elif row == 29:  # Fill entire row 29
                    if col < 10:
                        grid[row][col] = '25'  # Kidney Beans
                    elif col < 20:
                        grid[row][col] = '28'  # Soybeans
                    elif col < 30:
                        grid[row][col] = '9'  # Corn
                    elif col < 40:
                        grid[row][col] = '10'  # Squash
                    elif col < 50:
                        grid[row][col] = '11'  # Cucumbers
                    elif col < 60:
                        grid[row][col] = '37'  # Sweet Potatoes
                    elif col < 70:
                        grid[row][col] = '47'  # Sunflowers
                    elif col < 80:
                        grid[row][col] = '48'  # Flax
                    elif col < 90:
                        grid[row][col] = '49'  # Hemp
                    else:
                        grid[row][col] = '8'  # Potatoes

fill_empty_spaces()

# ===== PERENNIAL VEGETABLES (additional) =====
place_plant(22, 60, 22, 61, '53')  # Sorrel (2 m²)
place_plant(22, 62, 22, 63, '54')  # Lovage (2 m²)
place_plant(22, 64, 22, 64, '55')  # Chives (1 m²)
place_plant(22, 65, 22, 66, '56')  # Walking Onion (2 m²)
place_plant(22, 67, 22, 68, '57')  # Sea Kale (2 m²)

# Write to CSV
with open('complete_planting_grid.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['Row'] + [str(i+1) for i in range(COLS)]
    writer.writerow(header)
    for i, row in enumerate(grid):
        writer.writerow([str(i+1)] + row)

# Count used cells
used = sum(1 for row in grid for cell in row if cell != '')
total = ROWS * COLS
print(f"Complete planting grid generated: complete_planting_grid.csv")
print(f"Grid size: {ROWS} rows × {COLS} columns = {total} cells (3000 m²)")
print(f"Used cells: {used} ({used/total*100:.1f}%)")
print(f"Empty cells: {total - used} ({(total-used)/total*100:.1f}%)")

