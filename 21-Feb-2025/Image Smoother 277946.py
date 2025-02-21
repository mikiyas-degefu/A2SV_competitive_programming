# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        result = []
        for i in range(len(img)):
            updated_arr = []
            for j in range(len(img[0])):
                counter = 0
                sum_ = 0 
                if j-1 >= 0:
                    sum_+= img[i][j-1]
                    counter+=1
                
                if j+1 < len(img[i]):
                    sum_+= img[i][j+1]
                    counter+=1
                
                if i-1 >= 0:
                    sum_+= img[i-1][j]
                    counter+=1
                
                if i+1 < len(img):
                    sum_+= img[i+1][j]
                    counter+=1

                if j-1 >= 0 and i-1 >= 0:
                    sum_+= img[i-1][j-1]
                    counter+=1

                if i-1 >= 0 and j+1 < len(img[i]):
                    sum_+= img[i-1][j+1]
                    counter+=1

                if i+1 < len(img) and j-1 >= 0:
                    sum_+= img[i+1][j-1]
                    counter+=1

                if i+1 < len(img) and j+1 < len(img[i]):
                    sum_+= img[i+1][j+1]
                    counter+=1
                counter+=1
                sum_+=img[i][j]
                updated_arr.append(sum_ // counter)

            result.append(updated_arr)
        
        return result


        