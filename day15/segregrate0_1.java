public class segregrate0_1 {
    public static void main(String[] args) {
        int[] arr = { 1,0,1,1,1,1,1};
        int count0 = 0 ,count1 = 0;
        segregrate(arr , count0 , count1);
        for(int ele : arr ){
            System.out.print(ele + " ");
        }
    }
    public static void segregrate(int[] arr , int count0 , int count1){
        for (int i =0 ; i < arr.length ; i++){
            if (arr[i] == 0 ){
                count0 +=1;
           }
        }
        
        for( int j = 0 ; j < count0;j++){
            arr[j] = 0;
        }
        for(int j = count0 ; j < arr.length ; j++){
            arr[j] = 1;
        }
        
    }
}
