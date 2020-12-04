import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Day3 {

    public static int count_trees(char[][] tree_matrix, int step_right, int step_down) {

        int tree_count = 0;
        char jump_val = '-';
        int new_row_idx = 0;
        int new_col_idx = 0;
        int rows = 323;
        int clmns = 31;

        boolean end = false;
        while(!end) {

            new_row_idx += step_down;
            new_col_idx = (new_col_idx + step_right) % clmns;

            if(new_row_idx >= rows){
                end = true;
                break;
            }

            if(new_col_idx >= clmns || new_col_idx < 0){
                System.out.println("what why");
            }

            jump_val = tree_matrix[new_row_idx][new_col_idx];
            
            if(jump_val == '#') {
                tree_count++;
            }
        }

        System.out.println("\nNumber of trees on the path: " + tree_count);
        return tree_count;

    }

    public static void main(String[] args) {

        File file = new File("input0.txt");

        Scanner scanner;
        int rows = 323;
        int clmns = 31;
        char[][] tree_matrix = new char[rows][clmns];

        try {
            scanner = new Scanner(file);

            for (int i = 0; i < rows; i++) {
                tree_matrix[i] = scanner.nextLine().toCharArray();
            }

            System.out.println(Arrays.deepToString(tree_matrix));

            scanner.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (NoSuchElementException n) {
            n.printStackTrace();
        }

        long a = count_trees(tree_matrix, 3, 1);
        long b = count_trees(tree_matrix, 1, 1);
        long c = count_trees(tree_matrix, 5, 1);
        long d = count_trees(tree_matrix, 7, 1);
        long e = count_trees(tree_matrix, 1, 2);

        System.out.println(a*b*c*d*e);
    }
}
