public class rotate_array {
        public static void main(String[] args) {
            int[] arr = {1,2,3,4,5,6,7,8,9,10};
            int d = 3;
            int n = arr.length ;
            rotate(arr , d , n);
            for(int j = 0 ; j < n ; j++){
                System.out.print(arr[j] + " ");
            }
            }
        
        static void rotate(int[] arr , int d, int n ){
            reverse(arr ,0 , d);
            reverse(arr ,d ,n );
            reverse(arr , 0 , n-d);
         
        
            
        
           
       }
        static void reverse(int[] arr ,int d ,  int n){
            for( int i = 0 ; i <= n/2 ;i++){
                int temp = arr[i];
                arr[i] = arr[n - 1 - i] ;
                arr[n - 1 - i] = temp ;
                
                
            }
        }




}
