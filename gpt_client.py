
from openai import OpenAI
import base64
import traceback


def ask_gpt(text,image_path=None,api_key=None):
    if not api_key:
        return"API 키가 없습니다"
    client = OpenAI(api_key=api_key)
    #서버와 연결하는 객체
    print("GPT 요청 준비중...")
    if image_path:
        with open(image_path,"rb") as f:
            image_read=f.read()
            incode=base64.b64encode(image_read)
            incode_str=incode.decode("utf-8")
            data_url="data:image/png;base64,"+ incode_str
            input_data = [
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": text},
                        {"type": "input_image", "image_url": data_url},
                    ],
                }
            ]
            print("이미지 인코딩 완료")
    else:
        input_data = text
        print("텍스트 입력으로 데이터 설정 완료.")
    try:
        print("AI 요청 시작")
        response= client.responses.create(
        model="gpt-4.1-mini",
        input=input_data
        ) 
        print("AI 응답 수신 완료")
        #ai의 모델과 질문을 답변 받음
        result = response.output_text
        print("응답 텍스트 추출 완료",result)
        if not result:
            return "응답 텍스트가 비어있습니다ㅠㅠ"
        #결과값을 텍스트로 추출
        return result

    except Exception as e:
        print("에러 타입:", type(e))
        print("에러 상세:", repr(e))
        traceback.print_exc()
        print("AI에서 오류가 발생했습니다 이유:", e)
        return "GPT 응답 실패"
