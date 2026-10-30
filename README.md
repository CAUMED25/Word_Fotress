# 단어 요새 (Word Fortress)

뜻을 보고 영단어를 타이핑해 몬스터를 막는 학습 게임입니다.

## 구조
- `public/index.html` — 게임 전체 (한 파일)
- `netlify/functions/hof.mjs` — 명예의 전당 API (`/api/hof`), Netlify Blobs에 저장
- `netlify.toml`, `package.json` — Netlify 설정

## 배포 (GitHub 연동, 추천)
1. 이 폴더를 GitHub 저장소로 올립니다.
2. Netlify → Add new site → Import an existing project → 저장소 선택.
3. 설정은 netlify.toml이 알아서 잡습니다. Deploy 누르면 끝.

## 배포 (CLI)
```
npm install
npx netlify-cli login
npx netlify-cli deploy --prod
```

## 주의
- Netlify Drop(폴더 끌어다 놓기)은 서버 함수를 올리지 못합니다. 그렇게 올리면 게임은 되지만 명예의 전당이 "이 기기 기록"으로만 동작합니다.
- 점수는 브라우저에서 계산해 보내므로, 마음먹고 조작하면 막기 어렵습니다. 친구끼리 쓰는 용도로 생각해 주세요.
- 순위 초기화: Netlify 대시보드 → Blobs → `hall-of-fame` 스토어에서 `board` 항목을 지우면 됩니다.
