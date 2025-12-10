#!/usr/bin/env python3
"""
Generate complete planting grid based on space calculations and companion rules.
"""

import csv

# Grid dimensions
ROWS = 30
COLS = 100

# Initialize empty grid
grid = [['' for _ in range(COLS)] for _ in range(ROWS)]

# Plant placements based on space_calculations.md
# Format: (row_start, col_start, row_end, col_end, plant_num, plant_name)

placements = [
    # ROW 1-2: Trees (North edge) - Fruit trees
    (0, 0, 0, 3, '69', 'Apple'),  # 4x4 = 16 m²
    (0, 5, 0, 8, '69', 'Apple'),
    (0, 10, 0, 13, '69', 'Apple'),
    (0, 20, 0, 23, '70', 'Pear'),  # 4x4 = 16 m²
    (0, 25, 0, 28, '70', 'Pear'),
    (1, 0, 1, 3, '71', 'Plum'),  # 4x4 = 12 m²
    (1, 5, 1, 8, '71', 'Plum'),
    (1, 20, 1, 23, '72', 'Cherry'),  # 4x4 = 12 m²
    (1, 25, 1, 28, '72', 'Cherry'),
    (0, 35, 0, 38, '73', 'Apricot'),  # 4x4 = 12 m²
    (0, 45, 0, 48, '74', 'Quince'),  # 4x4 = 12 m²
    
    # ROW 2-3: Nut trees (larger spacing)
    (2, 0, 3, 4, '84', 'Walnut'),  # 5x5 = 25 m²
    (2, 6, 3, 10, '84', 'Walnut'),
    (2, 12, 3, 16, '84', 'Walnut'),
    (2, 18, 3, 22, '84', 'Walnut'),
    (2, 24, 3, 28, '84', 'Walnut'),
    (4, 0, 5, 2, '85', 'Hazelnut'),  # 3x3 = 9 m²
    (4, 4, 5, 6, '85', 'Hazelnut'),
    (4, 8, 5, 10, '85', 'Hazelnut'),
    (4, 12, 5, 14, '85', 'Hazelnut'),
    (6, 0, 7, 3, '86', 'Almond'),  # 4x4 = 16 m²
    (6, 5, 7, 8, '86', 'Almond'),
    (6, 10, 7, 13, '86', 'Almond'),
    (8, 0, 9, 4, '87', 'Chestnut'),  # 5x5 = 25 m²
    (8, 6, 9, 10, '87', 'Chestnut'),
    
    # ROW 10-12: Support trees
    (10, 0, 11, 3, '88', 'Black Locust'),  # 4x4 = 16 m²
    (10, 5, 11, 8, '88', 'Black Locust'),
    (10, 10, 11, 13, '88', 'Black Locust'),
    (10, 15, 11, 18, '88', 'Black Locust'),
    (10, 20, 11, 23, '88', 'Black Locust'),
    (12, 0, 13, 3, '89', 'Elder'),  # 4x4 = 12 m²
    (12, 5, 13, 8, '89', 'Elder'),
    
    # ROW 14-16: Shrubs (Berry)
    (14, 0, 14, 0, '75', 'Raspberry'),  # 0.5 m² each, 20 canes
    (14, 2, 14, 2, '75', 'Raspberry'),
    (14, 4, 14, 4, '75', 'Raspberry'),
    (14, 6, 14, 6, '75', 'Raspberry'),
    (14, 8, 14, 8, '75', 'Raspberry'),
    (14, 10, 14, 10, '75', 'Raspberry'),
    (14, 12, 14, 12, '75', 'Raspberry'),
    (14, 14, 14, 14, '75', 'Raspberry'),
    (14, 16, 14, 16, '75', 'Raspberry'),
    (14, 18, 14, 18, '75', 'Raspberry'),
    (15, 0, 15, 0, '75', 'Raspberry'),
    (15, 2, 15, 2, '75', 'Raspberry'),
    (15, 4, 15, 4, '75', 'Raspberry'),
    (15, 6, 15, 6, '75', 'Raspberry'),
    (15, 8, 15, 8, '75', 'Raspberry'),
    (15, 10, 15, 10, '75', 'Raspberry'),
    (15, 12, 15, 12, '75', 'Raspberry'),
    (15, 14, 15, 14, '75', 'Raspberry'),
    (15, 16, 15, 16, '75', 'Raspberry'),
    (15, 18, 15, 18, '75', 'Raspberry'),
    
    (14, 25, 15, 26, '76', 'Blackberry'),  # 1 m² each, 10 canes
    (14, 28, 15, 29, '76', 'Blackberry'),
    (14, 31, 15, 32, '76', 'Blackberry'),
    (14, 34, 15, 35, '76', 'Blackberry'),
    (14, 37, 15, 38, '76', 'Blackberry'),
    (16, 25, 17, 26, '76', 'Blackberry'),
    (16, 28, 17, 29, '76', 'Blackberry'),
    (16, 31, 17, 32, '76', 'Blackberry'),
    (16, 34, 17, 35, '76', 'Blackberry'),
    (16, 37, 17, 38, '76', 'Blackberry'),
    
    (14, 45, 15, 46, '77', 'Red Currant'),  # 2 m² each, 5 bushes
    (14, 48, 15, 49, '77', 'Red Currant'),
    (14, 51, 15, 52, '77', 'Red Currant'),
    (14, 54, 15, 55, '77', 'Red Currant'),
    (14, 57, 15, 58, '77', 'Red Currant'),
    
    (16, 45, 17, 46, '78', 'Black Currant'),  # 2 m² each, 5 bushes
    (16, 48, 17, 49, '78', 'Black Currant'),
    (16, 51, 17, 52, '78', 'Black Currant'),
    (16, 54, 17, 55, '78', 'Black Currant'),
    (16, 57, 17, 58, '78', 'Black Currant'),
    
    (18, 45, 19, 46, '79', 'Gooseberry'),  # 2 m² each, 5 bushes
    (18, 48, 19, 49, '79', 'Gooseberry'),
    (18, 51, 19, 52, '79', 'Gooseberry'),
    (18, 54, 19, 55, '79', 'Gooseberry'),
    (18, 57, 19, 58, '79', 'Gooseberry'),
    
    (18, 0, 19, 1, '80', 'Elderberry'),  # 4 m² each, 3 bushes
    (18, 3, 19, 4, '80', 'Elderberry'),
    (18, 6, 19, 7, '80', 'Elderberry'),
    
    (20, 0, 21, 1, '81', 'Sea Buckthorn'),  # 4 m² each, 3 bushes
    (20, 3, 21, 4, '81', 'Sea Buckthorn'),
    (20, 6, 21, 7, '81', 'Sea Buckthorn'),
    
    (20, 45, 21, 46, '82', 'Jostaberry'),  # 2 m² each, 3 bushes
    (20, 48, 21, 49, '82', 'Jostaberry'),
    (20, 51, 21, 52, '82', 'Jostaberry'),
    
    (22, 45, 23, 46, '83', 'Aronia'),  # 2 m² each, 3 bushes
    (22, 48, 23, 49, '83', 'Aronia'),
    (22, 51, 23, 52, '83', 'Aronia'),
    
    # ROW 18-20: Support shrubs
    (18, 25, 19, 26, '90', 'Siberian Pea Shrub'),  # 2 m² each, 5 bushes
    (18, 28, 19, 29, '90', 'Siberian Pea Shrub'),
    (18, 31, 19, 32, '90', 'Siberian Pea Shrub'),
    (18, 34, 19, 35, '90', 'Siberian Pea Shrub'),
    (18, 37, 19, 38, '90', 'Siberian Pea Shrub'),
    
    (20, 25, 21, 26, '91', 'Goumi'),  # 2 m² each, 3 bushes
    (20, 28, 21, 29, '91', 'Goumi'),
    (20, 31, 21, 32, '91', 'Goumi'),
    
    (22, 25, 23, 26, '92', 'Autumn Olive'),  # 2 m² each, 3 bushes
    (22, 28, 23, 29, '92', 'Autumn Olive'),
    (22, 31, 23, 32, '92', 'Autumn Olive'),
    
    (22, 0, 23, 1, '93', 'Serviceberry'),  # 2 m² each, 2 bushes
    (22, 3, 23, 4, '93', 'Serviceberry'),
    
    # ROW 24-29: Annual beds (central area)
    # Start with large crops that need space
    
    # Potatoes (8) - 20 m² = 20 cells
    (24, 0, 24, 19, '8', 'Potato'),
    
    # Wheat (29) - 4 m² = 4 cells
    (24, 25, 24, 28, '29', 'Wheat'),
    
    # Oats (30) - 3 m² = 3 cells
    (24, 30, 24, 32, '30', 'Oats'),
    
    # Barley (31) - 3 m² = 3 cells
    (24, 35, 24, 37, '31', 'Barley'),
    
    # Tomatoes (1) with Basil (18) - 8 m² tomatoes + 2 m² basil = 10 cells
    (25, 0, 25, 7, '1', 'Tomato'),
    (25, 1, 25, 1, '18', 'Basil'),  # Interplanted
    (25, 3, 25, 3, '18', 'Basil'),
    (25, 5, 25, 5, '18', 'Basil'),
    (25, 7, 25, 7, '18', 'Basil'),
    
    # Carrots (6) with Onions (7) - 4 m² carrots + 9 m² onions = 13 cells
    (25, 10, 25, 13, '6', 'Carrot'),
    (25, 11, 25, 11, '7', 'Onion'),  # Interplanted
    (25, 13, 25, 13, '7', 'Onion'),
    (25, 15, 25, 23, '7', 'Onion'),  # More onions
    
    # Beans (3) - 2 m² = 2 cells (but need more for yield, use 4)
    (26, 0, 26, 3, '3', 'Bean'),
    
    # Peas (4) - 2 m² = 2 cells
    (26, 5, 26, 6, '4', 'Pea'),
    
    # Cabbage (5) - 4 m² = 4 cells
    (26, 10, 26, 13, '5', 'Cabbage'),
    
    # Broccoli (44) - 5 m² = 5 cells
    (26, 15, 26, 19, '44', 'Broccoli'),
    
    # Lettuce (12) - 6 m² = 6 cells
    (26, 25, 26, 30, '12', 'Lettuce'),
    
    # Spinach (14) - 5 m² = 5 cells
    (26, 35, 26, 39, '14', 'Spinach'),
    
    # Beets (16) - 3 m² = 3 cells
    (27, 0, 27, 2, '16', 'Beet'),
    
    # Turnips (38) - 3 m² = 3 cells
    (27, 5, 27, 7, '38', 'Turnip'),
    
    # Radish (13) - 2 m² = 2 cells
    (27, 10, 27, 11, '13', 'Radish'),
    
    # Peppers (2) - 5 m² = 5 cells
    (27, 15, 27, 19, '2', 'Pepper'),
    
    # Squash summer (10) - 5 m² = 5 cells
    (27, 25, 27, 29, '10', 'Squash'),
    
    # Squash winter (10) - 10 m² = 10 cells
    (27, 35, 27, 44, '10', 'Squash'),
    
    # Cucumbers (11) - 5 m² = 5 cells
    (28, 0, 28, 4, '11', 'Cucumber'),
    
    # Corn (9) - needs space, use 10 m² = 10 cells
    (28, 10, 28, 19, '9', 'Corn'),
    
    # Garlic (17) - 3 m² = 3 cells
    (28, 25, 28, 27, '17', 'Garlic'),
    
    # Leeks (40) - 2 m² = 2 cells
    (28, 30, 28, 31, '40', 'Leek'),
    
    # Kale (15) - 3 m² = 3 cells
    (29, 0, 29, 2, '15', 'Kale'),
    
    # Chard (41) - 2 m² = 2 cells
    (29, 5, 29, 6, '41', 'Chard'),
    
    # Arugula (42) - 2 m² = 2 cells
    (29, 10, 29, 11, '42', 'Arugula'),
    
    # Mizuna (43) - 2 m² = 2 cells
    (29, 15, 29, 16, '43', 'Mizuna'),
    
    # Legumes - spread out
    (24, 40, 24, 41, '21', 'Lentil'),  # 2 m²
    (24, 45, 24, 46, '22', 'Chickpea'),  # 2 m²
    (24, 50, 24, 51, '23', 'Fava Bean'),  # 2 m²
    (24, 55, 24, 56, '24', 'Black Bean'),  # 2 m²
    (24, 60, 24, 61, '25', 'Kidney Bean'),  # 2 m²
    (24, 65, 24, 65, '26', 'Navy Bean'),  # 1 m²
    (24, 70, 24, 70, '27', 'Lima Bean'),  # 1 m²
    (24, 75, 24, 76, '28', 'Soybean'),  # 2 m²
    
    # More grains
    (25, 40, 25, 42, '32', 'Quinoa'),  # 1 m²
    (25, 45, 25, 45, '33', 'Amaranth'),  # 1 m²
    (25, 50, 25, 52, '34', 'Buckwheat'),  # 3 m²
    (25, 55, 25, 56, '35', 'Millet'),  # 2 m²
    (25, 60, 25, 62, '36', 'Rye'),  # 3 m²
    
    # Sweet Potato (37) - 6 m² = 6 cells
    (26, 40, 26, 45, '37', 'Sweet Potato'),
    
    # Perennial vegetables
    (23, 60, 23, 84, '50', 'Asparagus'),  # 25 m² = 25 cells (50 crowns)
    (23, 85, 23, 94, '51', 'Rhubarb'),  # 10 m² = 10 cells (10 crowns)
    (23, 95, 23, 99, '52', 'Artichoke'),  # 10 m² = 10 cells (10 plants)
    
    # Herbs - borders and interplanted
    (24, 80, 24, 81, '58', 'Oregano'),  # 1 m²
    (24, 85, 24, 85, '59', 'Thyme'),  # 1 m²
    (24, 90, 24, 91, '60', 'Rosemary'),  # 2 m²
    (24, 95, 24, 95, '61', 'Sage'),  # 1 m²
    (25, 80, 25, 81, '62', 'Mint'),  # 2 m²
    (25, 85, 25, 86, '63', 'Parsley'),  # 2 m²
    (25, 90, 25, 90, '64', 'Dill'),  # 1 m²
    (25, 95, 25, 95, '65', 'Coriander'),  # 1 m²
    
    # Pest deterrents - borders
    (23, 0, 23, 2, '19', 'Marigold'),  # 3 m²
    (23, 10, 23, 14, '20', 'Nasturtium'),  # 5 m²
    (23, 20, 23, 21, '101', 'Tansy'),  # 2 m²
    
    # Nitrogen fixers - interplanted
    (24, 20, 24, 24, '94', 'White Clover'),  # 5 m²
    (25, 30, 25, 34, '95', 'Red Clover'),  # 5 m²
]

def place_plant(row_start, col_start, row_end, col_end, plant_num):
    """Place a plant in the grid."""
    for row in range(row_start, min(row_end + 1, ROWS)):
        for col in range(col_start, min(col_end + 1, COLS)):
            if grid[row][col] == '':
                grid[row][col] = plant_num

# Apply all placements
for placement in placements:
    place_plant(*placement[:5])

# Write to CSV
with open('complete_planting_grid.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # Header
    header = ['Row'] + [str(i+1) for i in range(COLS)]
    writer.writerow(header)
    # Data rows
    for i, row in enumerate(grid):
        writer.writerow([str(i+1)] + row)

print(f"Complete planting grid generated: complete_planting_grid.csv")
print(f"Grid size: {ROWS} rows × {COLS} columns = {ROWS * COLS} cells")

