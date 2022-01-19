
'''
sentence를 ' '(띄어쓰기) 단위로 나누어 sentence_list를 만들고
sentence_list를 reverse()를 이용하여 뒤집는다.
뒤집은 sentence_list를 join()로 각 요소들을 ' '(띄어쓰기) 단위로 문자열을 만들어 반환한다.
'''

sentence = "way a is there will a is there Where"

def reverse_sentence(sentence):
    reversed_sentence_list = sentence.split(' ')
    reversed_sentence_list.reverse()
    return ' '.join(reversed_sentence_list)

print(reverse_sentence(sentence))