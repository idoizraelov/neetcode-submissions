class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, left_half, right_half, start):
            i = start
            j = k = 0
            
            while j < len(left_half) and k < len(right_half):
                if left_half[j] <= right_half[k]:
                    arr[i] = left_half[j]
                    j += 1
                else:
                    arr[i] = right_half[k]
                    k += 1
                i += 1
            
            while j < len(left_half):
                arr[i] = left_half[j]
                j += 1
                i += 1
                
            while k < len(right_half):
                arr[i] = right_half[k]
                k += 1
                i += 1


                    
        def mergeSort(arr,left,right):
            if left==right:
                return arr
            mid=(left+right)//2
            mergeSort(arr,left,mid)
            mergeSort(arr,mid+1,right)
            merge(arr,arr[left:mid+1],arr[mid+1:right+1],left)
            return arr
        
        return mergeSort(nums,0,len(nums)-1)

                    