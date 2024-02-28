# 자동화 작성 예시

안녕하세요, QA Engineer 백찬입니다.
pytest 로 실행하면 자동화 실행 코드를 볼 수 있습니다.
2023년 11월 17일(금) 기준으로 작성이 되었으며, 이후에 사이트가 변경되었거나, 유효하지 않은 정보가 입력될 시 오류가 발생될 수 있습니다. 이 때는 pytest 결과를 통해서 오류 내용을 볼 수 있습니다.

이동 경로

1. 자동화 작성 예시 사이트
2. GNB 에서 Work 진입
3. 제공 서비스 중에 하나 새창 링크 바로가기 클릭
4. 무료체험 신청 버튼 클릭
5. 내용 입력
6. 전부 내용이 입력된 상태에서 신청 취소

자동화 테스트 실행 방법

> pytest ./tests/test_filltheform.py

[재현 동영상](https://drive.google.com/file/d/1sqMW5cNcVwAdFaretSawo3_bVINUV2d5/view?usp=sharing)을 클릭하시면 실행된 예시를 보실 수 있습니다.
