import java.util.Arrays;

public class BubbleSort {

	public static void main(String[] args) {
		int[] lst = {4, 9, 7, 1, 3, 6, 5};
		
		for(int i = 0; i < lst.length-1; i++) {
			for(int j = 0; j < (lst.length - i); j++) {
				// (j+1 < lst.length) to handle out of range
				if((j+1 < lst.length) && lst[j] > lst[j+1]) {
					int tmp = lst[j];
					lst[j] = lst[j+1];
					lst[j+1] = tmp;
				}
			}
		}
		
		System.out.println(Arrays.toString(lst));
	}

}
