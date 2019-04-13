// In-place algorithm (no need another array)
// O(n^2) time complexity - Quadratic (2 loops)
// Algorithm degrades quickly
// Unstable sort: Flip the relative order of the duplicated values
// Stable sort: Preserve the relative order of the duplicated values (Preferred)
// When the values are numbers, probably doesn't matter
// But if the values are objects, then that is another problem
public class BubbleSort_2 {
  public static void main(String[] args) {
    int[] arr = {20, 35, -15, 7, 55, 1, -22};
    for (int k = arr.length - 1; k > 0; --k) {
      for (int i = 0; i < k; ++i) {
        if (arr[i] > arr[i+1]) {
          int tmp = arr[i];
          arr[i] = arr[i+1];
          arr[i+1] = tmp;
        }
      }
    }
    for (int i = 0; i < arr.length; i++)
      System.out.println(arr[i]);
  }
}
