import java.util.*;
import java.io.PrintStream;

public class SparseMatrix {

    HashMap<String, Integer> MyMap = new HashMap<String, Integer>();

    public SparseMatrix(){}

    // create an empty square matrix of given size
    public static void createEmptyMatrix(int size){
        //int MyMatrix[][] = new int[size][size];
    }

    // put A[i][j] = 1
    public void set(int i, int j, int value){
       MyMap.put(currentKey(i,j),value);
    }

    // return value at A[i][j]
    public int get(int i, int j){
       if (MyMap.containsKey(currentKey(i,j))){
           return MyMap.get(currentKey(i,j));
       }else{
           return 0;
       }
    }
    public String currentKey(int i, int j){       //Make a unique key by joining 'i' and 'j'
        return Integer.toString(i)+ "|" +Integer.toString(j);
    }
}
