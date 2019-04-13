// Selection Sort
// In-place algorithm
// O(n^2) time complexity - quadratic
// Doesn't require as much swapping as bubble sort
// Unstable algorithm

public class SelectionSort_3 {
  public static void main(String[] args) {
    int[] arr = {20, 35, -15, 7, 55, 1, -22};
    for (int j = arr.length - 1; j > 0; --j) {
      int index = 0;
      for (int i = 0; i <= j; ++i) {
        if (arr[i] > arr[index]) {
          index = i;
        }
      }
      int tmp = arr[index];
      arr[index] = arr[j];
      arr[j] = tmp;
    }
    for (int i = 0; i < arr.length; ++i) {
      System.out.println(arr[i]);
    }
  }
}
