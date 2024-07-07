//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int t = Integer.parseInt(in.readLine().trim());
        while (t-- > 0) {
            String line = in.readLine();
            String[] tokens = line.split(" ");

            // Create an ArrayList to store the integers
            ArrayList<Integer> array = new ArrayList<>();

            // Parse the tokens into integers and add to the array
            for (String token : tokens) {
                array.add(Integer.parseInt(token));
            }

            int[] arr = new int[array.size()];
            int idx = 0;
            for (int i : array) arr[idx++] = i;

            int key = Integer.parseInt(in.readLine().trim());

            out.println(new Solution().search(arr, key));
        }
        out.close();
    }
}
// } Driver Code Ends


// User function Template for Java

 class Solution {
    int search(int[] arr, int key) {
        // Complete this function
        int n = arr.length;
        int pivot = findPivot(arr, 0, n - 1);
        
        // If pivot is -1, then array is not rotated at all
        if (pivot == -1) {
            return binarySearch(arr, 0, n - 1, key);
        }
        
        // If we found a pivot, decide which subarray to search
        if (arr[pivot] == key) {
            return pivot;
        }
        if (arr[0] <= key) {
            return binarySearch(arr, 0, pivot - 1, key);
        }
        return binarySearch(arr, pivot + 1, n - 1, key);
    }
    
    // Function to find the pivot in rotated sorted array
    private int findPivot(int[] arr, int low, int high) {
        if (high < low) {
            return -1;
        }
        if (high == low) {
            return low;
        }
        
        int mid = low + (high - low) / 2;
        
        if (mid < high && arr[mid] > arr[mid + 1]) {
            return mid;
        }
        if (mid > low && arr[mid] < arr[mid - 1]) {
            return mid - 1;
        }
        if (arr[low] >= arr[mid]) {
            return findPivot(arr, low, mid - 1);
        }
        return findPivot(arr, mid + 1, high);
    }
    
    // Standard binary search function
    private int binarySearch(int[] arr, int low, int high, int key) {
        if (high < low) {
            return -1;
        }
        
        int mid = low + (high - low) / 2;
        
        if (key == arr[mid]) {
            return mid;
        }
        if (key > arr[mid]) {
            return binarySearch(arr, mid + 1, high, key);
        }
        return binarySearch(arr, low, mid - 1, key);
    }
}