import chat
import face_expression

# chat_bot 테스트
#input_text = input('표정분석 결과를 입력 해주세요 :')
for i in range(6):
    tmp = face_expression.face_dict[f'{i}']
    #print(tmp)
    print('Q :'+ tmp)
    print('A : '+ chat.chat_ai(tmp))