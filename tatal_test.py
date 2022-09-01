import chat
import face_expression

# chat_bot 테스트
#input_text = input('표정분석 결과를 입력 해주세요 :')
for i in range(6):
    file = open('result.txt', 'a')
    tmp = face_expression.face_dict[f'{i}']
    tmp_answer = chat.chat_ai(tmp)
    file.write(tmp_answer+'\n')

    print('Q :'+ tmp)
    print('A : '+ tmp_answer)
file.close()