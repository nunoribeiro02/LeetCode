import java.util.*;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Initialize set/ All filled cells satisfy the ruless for rows, columns, and sub-boxes
        Map<Integer, Set<Character>> rowMap = new HashMap<>();
        Map<Integer, Set<Character>> colMap = new HashMap<>();
        Map<Integer, Set<Character>> boxMap = new HashMap<>();

        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                char cell = board[row][col];
                if (cell == '.'){
                    continue;
                }

                // Check row
                if (!rowMap.containsKey(row)) {
                    rowMap.put(row, new HashSet<>());
                }
                if (!rowMap.get(row).add(cell)) {
                    return false;
                }

                // Check column
                if (!colMap.containsKey(col)) {
                    colMap.put(col, new HashSet<>());
                }
                if (!colMap.get(col).add(cell)) {
                    return false;
                }

                // Check sub-box
                int boxIndex = (row / 3) * 3 + col / 3;
                if (!boxMap.containsKey(boxIndex)) {
                    boxMap.put(boxIndex, new HashSet<>());
                }
                if (!boxMap.get(boxIndex).add(cell)) {
                    return false;
                }
            }
        }

        return true;
    }
}