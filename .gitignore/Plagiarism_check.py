from math import *

def processing1(f1, f2):
    l1 = f1.readlines()
    l2 = f2.readlines()
    temp_sentence_1=[l1[0]]
    temp_sentence_2=[l2[0]]
    for t_l1 in range(1,len(l1)):
        temp_sentence_1[0] += l1[t_l1]
        lowered_sen_1=processing2(temp_sentence_1[0].lower())# 대문자와 소문자가 다르게 인식되는 것을 방지하기 위해 소문자화
    for t_l2 in range(1,len(l2)):
        temp_sentence_2[0] += l2[t_l2]
        lowered_sen_2 = processing2(temp_sentence_2[0].lower())

    sentence1 = lowered_sen_1.split(' ')
    sentence2 = lowered_sen_2.split(' ')

    test_list = list(set(sentence1).union(set(sentence2)))

    result = Cosine_Similarity(sentence1, sentence2, test_list)

    return result

#############################################################

def processing2(str1): # 단어들 만을 비교하기 위해서 글자들 외에 특수문자 제거
    symbol = '''.,~!@#$%^&*()_+{}|[]"'/?<>;:'''
    for k in range(len(symbol)):
        n1 = str1.count(symbol[k])
        str1 = str1.replace(symbol[k], '', n1)
    n2 = str1.count('\n')
    str1 = str1.replace('\n', ' ', n2)
    return str1

#############################################################

def Cosine_Similarity(sen1,sen2,t_list):
    vector_1 = []
    vector_2 = []
    numerator = 0
    denominator_1 = 0
    denominator_2 = 0

    for v1 in range(len(t_list)): # 문서 1의 벡터
        n1 = sen1.count(t_list[v1])
        vector_1.append(n1)
    for v2 in range(len(t_list)): # 문서 2의 벡터
        n2 = sen2.count(t_list[v2])
        vector_2.append(n2)

    for v_n in range(0,len(t_list)):
        numerator += vector_1[v_n]*vector_2[v_n]

    for v_d1 in range(0,len(t_list)):
        denominator_1 += vector_1[v_d1]**2
    result_1 = sqrt(denominator_1)

    for v_d2 in range(0,len(t_list)):
        denominator_2 += vector_2[v_d2]**2
    result_2 = sqrt(denominator_2)

    C_similarity = numerator/(result_1*result_2)

    percentage = C_similarity * 100

    return percentage



#############################################################

n = int(input('입력을 원하는 문서의 개수를 5개 이하로 입력해 주세요 : '))

if n > 5: # 5개 보다 더 큰 숫자를 입력했을 때를 위한 코드
    while n <= 5:
        n = int(input('입력을 원하는 문서의 개수를 5개 이하로 입력해 주세요 : '))
else:
    pass

file_list = [] # n번 인덱스의 파일 : 실제로 n+1번 파일

for _ in range(n): # 문서 0~4 경로 및 이름 저장
    file_name = input('입력을 원하는 문서의 경로를 포함하여 정확하게 작성해주세요. ex) c:\\\\Python\\\\example.txt >>> ')
    file_list.append(file_name)

all_percentage = []
for i in range(0,n-1): # 모든 문서 한번씩 매치 하면서 비교 후 리스트에 잠시 저장
    for j in range(i+1, n):
        temp = []
        temp.append(i)
        temp.append(j)
        file_1 = open(file_list[i], 'r')
        file_2 = open(file_list[j], 'r')
        temp.append(processing1(file_1,file_2))
        all_percentage.append(temp)

nc2 = int((n*(n-1))/2) # 매치되어 처리된 파일쌍들의 개수

max_index=0
for fin_n in range(nc2): #
    if all_percentage[max_index][2] < all_percentage[fin_n][2]: #
        max_index = fin_n
    else:
        pass

print('*'*100)
print('입력한 파일 순서')
for nbr in range(n):
    print('%d : %s\n'%(nbr+1, file_list[nbr]))
print('%d 번째로 입력한 문서와 %d 번째로 입력한 문서와의 유사도가 가장 높습니다'%(all_percentage[max_index][0]+1,all_percentage[max_index][1]+1))
similarity=round(all_percentage[max_index][2],2)
print('유사도 : %0.1f %%'%(similarity))