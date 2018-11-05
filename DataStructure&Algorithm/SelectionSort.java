
import java.util.Arrays;

public class SelectionSort {

	public static void main(String[] args) {
		int[] lst = {4, 9, 7, 1, 3, 6, 5};
		for(int i = 0; i < lst.length; i++) {
			for(int j = i + 1; j < lst.length; j++) {
				if(lst[i] > lst[j]) {
					int tmp = lst[i];
					lst[i] = lst[j];
					lst[j] = tmp;
				}
			}
		}
		System.out.println(Arrays.toString(lst));
		
	}

}
