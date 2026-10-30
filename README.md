# 단어 요새 (Word Fortress)

뜻을 보고 영단어를 타이핑해 몬스터를 막는 학습 게임입니다.

## 기능
- 로그인(닉네임+비밀번호, 첫 입장 시 자동 등록) → 개인 화면 → 단어장 선택 → 게임
- 단어장: 이름 지정, 일련번호(No.1001부터) 자동 부여, 공개/비공개 선택
- 공개 단어장은 이름·번호(예: 1001, #1001)로 검색, 미리보기 후 플레이, 복사해서 내 것으로 만들기
- 다른 사람이 만든 단어장은 수정·삭제 불가 (서버에서 차단)
- STAGE 1~10: 점수에 따라 자동 진급, 게임 오버 후 새 판은 STAGE 1부터
- 명예의 전당: 단어장별로 따로 집계

## 구조
- `public/index.html` — 게임 전체 (한 파일)
- `netlify/functions/api.mjs` — API (`/api/*`), Netlify Blobs 저장
- `netlify/functions/lib/core.mjs` — 서버 핵심 로직 (index.html 안에도 같은 코드가 들어 있어 서버가 없을 때 이 기기 저장 모드로 동작)
- `netlify/functions/lib/builtins.mjs` — 기본 제공 단어장

## 배포
GitHub에 push하면 Netlify가 자동으로 배포합니다.

## 주의
- 점수는 브라우저에서 계산해 보내므로 작정하고 조작하면 막기 어렵습니다.
- core.mjs를 고치면 public/index.html 안의 같은 코드도 함께 고쳐야 합니다.
