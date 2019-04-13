
// Time complexity and memory complexity
// Main concern is Time complexity(how many steps we take?), because memory is cheap these days
// O of n~, O to the n~ (Order below, best->worst)
// O(1) Constant time
// O(logn) Logarithmic - log to the base2 (log2n)
// O(n) linear time complexity e.g. 2n+2, 2's are constant, n is the element
// O(nlogn) n log-star n
// O(n^2) Quadratic

// Array - Fixed size, contiguous memory
// When you know the index, O(1)
// When you don't know index, retrieving data, the worst case is the size of the array O(n)
// Add an element to a full array O(n) -> need to create new array and copy them all first
// Add an element to the end of an array O(1)
// Insert or update an element at a specific index O(1)
// Delete an element by setting it to null O(1)
// Delete an element by shifting elements O(n)
public class Array_1 {
  public static void main(String[] args) {
    int[] intArr = new int[7];
    intArr[0] = 10;
    intArr[1] = 20;
    intArr[2] = -18;
    intArr[3] = 39;
    intArr[4] = 23;
    intArr[5] = 11;

    for(int i = 0; i < intArr.length; ++i) {
      System.out.println(intArr[i]);
    }
  }
}
