# Normalized Levels Coding Question
import re
class Solution(object):
    def normalizeLevels(self, level):
        """
        input: levels(str)
        return: normalized levels(str)
        """
        N_set,N_element=self.countSetAndElement(level)
        #print(N_set,N_element)
        string=self.constructNormalizedLevel(level, N_set, N_element)
        return string

    def countSetAndElement(self,level):
        """
        input: levels(str)
        return: two integers
        """
        split1=level.replace("\n"," ")
        #print(split1)
        i=split1.count(" ")
        j=split1.count(",")
        if i>j:
         set=int(i-j-1)
        else:
          set=i-1
        element=int(j/set+1)
        return set,element

    def constructNormalizedLevel(self,level, N_set,N_element):
        """
        input: levels(str), number of sets and elements in each set
        return: Normalized Level(str)
        """
        str1=level.replace("\n"," ")
        #print(str1)
        str2=str1.replace(","," ").replace("  "," ").strip()
        splitList=str2.split(" ")
        print(splitList)
        string = ""
        for set in range(0,N_set):
            lst = list()
            for element in range(set*N_element,set*N_element+N_element):
                lst.append(int(splitList[element]))
            newlst=sorted(lst)
            numberMax=newlst[-1]
            #print(lst)
            #print(numberMax)
            for i in range(N_element):
                number=round(lst[i] * 100 / numberMax)
                if i < N_element-1:
                  string = string + str(number) + ","
                else:
                  string = string + str(number) + "\n"

        return string

ans=Solution()

level0="""
28,54,812,438
12,35,78,26
18,2,212,5
"""
case0=ans.normalizeLevels(level0)
case0_real="""3,7,100,54
15,45,100,33
8,1,100,2
"""

level1="""
28,54,812,438 12,35,78,26 18,2,212,5
"""
case1=ans.normalizeLevels(level1)
case1_real="""3,7,100,54
15,45,100,33
8,1,100,2
"""


level2="""
127, 174, 17, 115, 56, 42, 234 214, 26, 129, 122, 145, 230, 90
232, 234, 38, 248, 142, 125, 19 18, 133, 97, 166, 114, 165, 153
99, 101, 247, 34, 36, 229, 143 203, 193, 199, 196, 72, 1, 95 162,
195, 88, 55, 218, 145, 36 157, 114, 86, 29, 102, 92, 127 63, 68,
113, 248, 30, 103, 100
"""
case2=ans.normalizeLevels(level2)
case2_real="""54,74,7,49,24,18,100
93,11,56,53,63,100,39
94,94,15,100,57,50,8
11,80,58,100,69,99,92
40,41,100,14,15,93,58
100,95,98,97,35,0,47
74,89,40,25,100,67,17
100,73,55,18,65,59,81
25,27,46,100,12,42,40
"""


level3="""
456, 20, 316, 646, 598, 433, 209, 517, 580, 718, 345, 619, 743,
421, 612, 174, 269, 774, 643, 505, 595 662, 343, 651, 395, 4, 54,
459, 37, 244, 687, 9, 372, 364, 761, 786, 515, 561, 121, 148,
253, 523 36, 339, 643, 47, 779, 792, 584, 42, 459, 455, 753, 529,
27, 388, 64, 796, 100, 195, 372, 67, 694 238, 479, 145, 490, 674,
642, 472, 307, 557, 652, 609, 393, 606, 225, 1, 657, 268, 466,
695, 473, 351 589, 152, 80, 405, 409, 334, 781, 145, 362, 226,
310, 538, 454, 459, 419, 688, 489, 83, 318, 361, 155 146, 419,
737, 700, 452, 544, 553, 710, 335, 605, 530, 518, 473, 107, 188,
534, 374, 612, 183, 610, 333 9, 515, 118, 500, 480, 749, 241,
179, 771, 525, 60, 368, 442, 325, 776, 798, 509, 154, 482, 709,
423 656, 406, 70, 216, 669, 622, 402, 693, 614, 424, 784, 632,
278, 498, 517, 324, 239, 581, 491, 288, 106 226, 672, 196, 381,
509, 94, 566, 99, 488, 303, 532, 411, 519, 584, 234, 290, 319,
28, 710, 500, 795 315, 281, 37, 344, 765, 236, 313, 607, 175,
204, 400, 595, 42, 29, 123, 764, 445, 171, 639, 775, 193 275,
306, 672, 370, 150, 502, 314, 539, 695, 353, 28, 557, 770, 738,
125, 579, 737, 663, 526, 26, 525
"""
case3=ans.normalizeLevels(level3)
case3_real="""59,3,41,83,77,56,27,67,75,93,45,80,96,54,79,22,35,100,83,65,77
84,44,83,50,1,7,58,5,31,87,1,47,46,97,100,66,71,15,19,32,67
5,43,81,6,98,99,73,5,58,57,95,66,3,49,8,100,13,24,47,8,87
34,69,21,71,97,92,68,44,80,94,88,57,87,32,0,95,39,67,100,68,51
75,19,10,52,52,43,100,19,46,29,40,69,58,59,54,88,63,11,41,46,20
20,57,100,95,61,74,75,96,45,82,72,70,64,15,26,72,51,83,25,83,45
1,65,15,63,60,94,30,22,97,66,8,46,55,41,97,100,64,19,60,89,53
84,52,9,28,85,79,51,88,78,54,100,81,35,64,66,41,30,74,63,37,14
28,85,25,48,64,12,71,12,61,38,67,52,65,73,29,36,40,4,89,63,100
41,36,5,44,99,30,40,78,23,26,52,77,5,4,16,99,57,22,82,100,25
36,40,87,48,19,65,41,70,90,46,4,72,100,96,16,75,96,86,68,3,68
"""


print(case0,case0==case0_real)
print(case1,case1==case1_real)
print(case2,case2==case2_real)
print(case3,case3==case3_real)

