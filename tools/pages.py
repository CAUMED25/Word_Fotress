# 안내 페이지 생성기: python3 tools/pages.py  → public/*.html
# 머리글/바닥글을 한 곳에서 관리하려고 만든 스크립트입니다.
import os, html
ROOT = os.path.join(os.path.dirname(__file__), "..", "public")
SITE = "https://wordsfortress.com"
EMAIL = "a01076527276@gmail.com"
NAV = [("guide.html","게임 방법"),("books.html","단어장"),("study-tips.html","공부법"),("about.html","소개")]

def page(fn, title, desc, body, extra_head="", extra_js=""):
    nav = "".join(f'<a href="/{h}"{" class=\"on\"" if h==fn else ""}>{t}</a>' for h,t in NAV)
    doc = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | 단어 요새</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}/{fn}">
<meta property="og:title" content="{html.escape(title)} | 단어 요새">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0b0c22">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23141238'/%3E%3Cpath d='M32 6l12 14-12 38-12-38z' fill='%2359d4ff'/%3E%3Cpath d='M32 6l12 14H20z' fill='%23e8fbff'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/ads.js" defer></script>
{extra_head}
</head>
<body>
<header class="site"><div class="wrap"><a class="brand" href="/">단어 요새</a><nav class="main">{nav}<a class="play" href="/">게임하기</a></nav></div></header>
<main><div class="wrap">
{body}
<div class="ad-slot" data-slot="content"></div>
</div></main>
<footer class="site"><div class="wrap"><nav><a href="/about.html">소개</a><a href="/privacy.html">개인정보처리방침</a><a href="/terms.html">이용약관</a><a href="/contact.html">문의</a></nav><span class="copy">© 2026 단어 요새 · wordsfortress.com</span></div></footer>
{extra_js}
</body>
</html>
'''
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write(doc)

# ---------------- 소개 ----------------
page("about.html", "소개", "단어 요새는 뜻을 보고 영단어를 타이핑해 몬스터를 막는 무료 영단어 학습 게임입니다. 만든 이유와 특징을 소개합니다.", f'''
<div class="hero"><div class="kicker">ABOUT</div><h1>단어 요새를 소개합니다</h1>
<p>뜻을 보고 영단어를 직접 타이핑해 몬스터를 막는, 무료 영단어 학습 게임입니다.</p></div>

<h2>왜 만들었나요</h2>
<p>단어장을 눈으로 훑어보면 아는 것 같은데, 막상 시험에서 뜻을 보고 영어 철자를 떠올리려면 잘 나오지 않는 경우가 많습니다. 보는 것과 꺼내 쓰는 것은 서로 다른 일이기 때문입니다. 단어 요새는 바로 그 "꺼내 쓰는" 연습을 게임으로 만든 것입니다.</p>
<p>화면에는 한국어 뜻만 적힌 몬스터가 나타나고, 플레이어는 그 뜻에 해당하는 영단어를 철자까지 정확하게 입력해야 합니다. 몬스터가 요새에 닿기 전에 떠올려야 하므로 자연스럽게 빠른 회상 연습이 되고, 키보드로 직접 치기 때문에 철자도 함께 익히게 됩니다.</p>

<h2>무엇이 다른가요</h2>
<ul>
<li><strong>내 단어장으로 플레이</strong> — 시험 범위, 교재 단원, 전공 용어 등 원하는 단어를 직접 넣어 게임을 만들 수 있습니다. 엑셀에서 두 열을 복사해 붙여 넣어도 됩니다.</li>
<li><strong>단어장 공유</strong> — 만든 단어장을 공개하면 다른 사람이 이름이나 번호(예: No.1001)로 검색해 같은 단어장으로 플레이할 수 있습니다. 공개 단어장은 <a href="/books.html">단어장 둘러보기</a>에서 로그인 없이 미리 볼 수 있습니다.</li>
<li><strong>단어장별 명예의 전당</strong> — 같은 단어장을 쓴 사람끼리 점수를 겨룹니다. 스터디 모임에서 공통 단어장을 정해 두고 순위를 비교하기 좋습니다.</li>
<li><strong>놓친 단어 복습</strong> — 게임이 끝나면 요새에 닿은(=떠올리지 못한) 단어가 정리되어 나오고, 다음 판에는 그 단어가 더 자주 등장합니다.</li>
<li><strong>10단계 스테이지</strong> — 점수가 오를수록 몬스터가 빨라지고 많아집니다. 처음에는 여유 있게, 익숙해질수록 빠르게 떠올리도록 난이도가 올라갑니다.</li>
</ul>

<h2>누구를 위한 게임인가요</h2>
<p>수능·내신·토익처럼 영단어를 대량으로 외워야 하는 학생, 의학·간호·공학 등 전공 영어 용어를 익혀야 하는 대학생, 아이와 함께 쉬운 단어로 타자와 영어를 같이 연습하고 싶은 가족 모두에게 맞도록 만들었습니다. 회원가입 절차 없이 닉네임과 비밀번호만 정하면 바로 시작할 수 있습니다.</p>

<h2>운영 정보</h2>
<table>
<tr><th style="width:130px">서비스 이름</th><td>단어 요새 (Word Fortress)</td></tr>
<tr><th>주소</th><td><a href="/">{SITE}</a></td></tr>
<tr><th>이용 요금</th><td>무료</td></tr>
<tr><th>문의</th><td><a href="mailto:{EMAIL}">{EMAIL}</a> (<a href="/contact.html">문의 안내</a>)</td></tr>
</table>
<p class="muted small">개인정보를 어떻게 다루는지는 <a href="/privacy.html">개인정보처리방침</a>에서 확인할 수 있습니다.</p>
<p style="margin-top:24px"><a class="btn" href="/">지금 플레이하기</a> &nbsp; <a class="btn ghost" href="/guide.html">게임 방법 보기</a></p>
''')

# ---------------- 게임 방법 ----------------
stages = [(1,0,"숲의 가장자리","슬라임만 등장, 느린 속도"),(2,400,"안개 낀 들판","창을 든 임프 등장"),(3,1000,"박쥐 동굴 입구","하늘을 나는 박쥐 등장"),
 (4,1900,"유령의 언덕","반투명 유령 등장"),(5,3100,"골렘의 길목","보스 골렘 출현(3번 맞혀야 쓰러짐)"),(6,4700,"붉은 달","동시에 나오는 몬스터 증가"),
 (7,6700,"폭풍 전야","속도 증가"),(8,9200,"어둠의 행군","보스 골렘 출현(4번)"),(9,12300,"마지막 방벽","더 빠르고 많아짐"),(10,16000,"최후의 결전","보스 골렘 출현(5번), 최고 난이도")]
st_rows = "".join(f"<tr><td>STAGE {n}</td><td>{need:,}점</td><td>{nm}</td><td>{f}</td></tr>" for n,need,nm,f in stages)
page("guide.html", "게임 방법", "단어 요새 게임 방법 안내: 시작하는 법, 조작, 몬스터 종류, 점수 계산, 1~10 스테이지, 명예의 전당, 단어장 만드는 형식까지 정리했습니다.", f'''
<div class="hero"><div class="kicker">HOW TO PLAY</div><h1>게임 방법</h1>
<p>뜻이 적힌 몬스터가 요새로 다가옵니다. 그 뜻에 맞는 영단어를 입력하고 Enter를 누르면 수정탑이 번개를 쏴 몬스터를 물리칩니다.</p></div>
<div class="box toc"><strong>목차</strong> · <a href="#start">시작하기</a> · <a href="#control">조작</a> · <a href="#monsters">몬스터</a> · <a href="#score">점수</a> · <a href="#stage">스테이지</a> · <a href="#hof">명예의 전당</a> · <a href="#book">단어장 만들기</a> · <a href="#faq">자주 묻는 질문</a></div>

<h2 id="start">1. 시작하기</h2>
<ol>
<li><strong>입장</strong> — 첫 화면에서 닉네임(12자 이내)과 비밀번호(2자 이상)를 입력합니다. 처음 쓰는 닉네임이면 그 비밀번호로 바로 등록되고, 다음부터는 같은 비밀번호로 들어오면 됩니다.</li>
<li><strong>단어장 고르기</strong> — 개인 화면에서 ‘단어장 고르기’를 눌러 기본 단어장이나 다른 사람이 공개한 단어장을 고릅니다. 카드를 누르면 단어 목록을 먼저 미리 볼 수 있습니다.</li>
<li><strong>시작</strong> — ‘요새 방어 시작’을 누르면 STAGE 1부터 게임이 시작됩니다.</li>
</ol>

<h2 id="control">2. 조작</h2>
<table>
<tr><th style="width:140px">키</th><th>동작</th></tr>
<tr><td><kbd>영단어</kbd> + <kbd>Enter</kbd></td><td>입력한 단어와 뜻이 맞는 몬스터 중 요새에 가장 가까운 몬스터를 공격합니다.</td></tr>
<tr><td><kbd>Esc</kbd></td><td>일시정지 / 다시 시작</td></tr>
<tr><td><kbd>한/영</kbd></td><td>한글 입력 상태로 치면 입력창 위에 경고가 뜹니다. 한/영 키로 영문으로 바꿔 주세요.</td></tr>
</table>
<p>대소문자는 구분하지 않습니다. 틀린 단어를 입력하면 콤보가 끊기지만 다른 불이익은 없습니다.</p>

<h2 id="monsters">3. 몬스터</h2>
<table>
<tr><th>몬스터</th><th>특징</th><th>요새 피해</th></tr>
<tr><td>슬라임</td><td>통통 튀며 천천히 다가옵니다. STAGE 1부터 등장.</td><td>8</td></tr>
<tr><td>임프</td><td>창을 들고 조금 더 빠르게 걸어옵니다. STAGE 2부터.</td><td>10</td></tr>
<tr><td>박쥐</td><td>하늘을 날아 가장 빠르게 다가옵니다. STAGE 3부터.</td><td>7</td></tr>
<tr><td>유령</td><td>흐릿해졌다 선명해졌다 합니다. STAGE 4부터.</td><td>9</td></tr>
<tr><td>보스 골렘</td><td>여러 번 맞혀야 쓰러지며, 맞을 때마다 새로운 뜻으로 바뀝니다. 쓰러뜨리면 요새 체력 +25.</td><td>30</td></tr>
<tr><td>★ 황금 몬스터</td><td>뜻 앞에 ★이 붙어 있습니다. 처치하면 점수 2배와 함께 치유(체력 +20), 빙결(4초 정지), 번개 폭풍(화면의 몬스터 일소) 중 하나가 발동합니다.</td><td>종류별</td></tr>
</table>
<p>요새 체력은 100이며, 0이 되면 게임이 끝납니다. 스테이지가 오를수록 몬스터 피해도 조금씩 커집니다.</p>

<h2 id="score">4. 점수</h2>
<p>몬스터를 처치하면 <strong>단어 길이</strong>에 비례한 기본 점수를 얻고, 여기에 다음 배율이 곱해집니다.</p>
<ul>
<li><strong>스테이지 배율</strong> — 스테이지가 하나 오를 때마다 15%씩 늘어납니다.</li>
<li><strong>콤보 배율</strong> — 연속으로 5번 맞힐 때마다 ×0.5씩, 최대 ×4까지 올라갑니다. 틀리거나 몬스터를 놓치면 초기화됩니다.</li>
<li><strong>아슬아슬 보너스</strong> — 요새 바로 앞까지 온 몬스터를 처치하면 ×1.5.</li>
<li><strong>보스·황금 몬스터</strong> — 각각 ×2.</li>
</ul>

<h2 id="stage">5. 스테이지</h2>
<p>점수가 아래 기준에 닿으면 자동으로 다음 스테이지로 올라갑니다. 게임 오버 후 새 판은 다시 STAGE 1부터 시작합니다.</p>
<table class="stage-t"><tr><th>스테이지</th><th>필요 점수</th><th>이름</th><th>특징</th></tr>{st_rows}</table>

<h2 id="hof">6. 명예의 전당</h2>
<p>명예의 전당은 <strong>단어장마다 따로</strong> 운영됩니다. 같은 단어장으로 플레이한 사람끼리 최고 점수를 비교하며, 한 사람당 최고 기록 하나만 남습니다. 게임이 끝나면 점수가 자동으로 기록되고, 개인 최고 기록을 넘으면 ‘NEW RECORD’가 표시됩니다.</p>

<h2 id="book">7. 단어장 만들기</h2>
<p>개인 화면의 ‘+ 새로 만들기’에서 단어장 이름과 단어 목록을 입력합니다. 한 줄에 한 쌍씩, 영단어와 뜻 사이를 아래 중 하나로 구분하면 됩니다.</p>
<div class="box"><code>abandon - 버리다<br>accurate, 정확한<br>achieve:성취하다<br>adapt[Tab]적응하다</code></div>
<ul>
<li>저장하면 <strong>No.1001</strong>처럼 일련번호가 붙습니다. 친구에게 번호만 알려 주면 바로 같은 단어장을 찾을 수 있습니다.</li>
<li><strong>공개</strong>로 저장하면 다른 사람이 검색해서 플레이할 수 있고, <strong>비공개</strong>면 나만 볼 수 있습니다.</li>
<li>다른 사람의 단어장은 고칠 수 없지만, ‘복사해서 내 것으로’를 누르면 내 단어장으로 가져와 수정할 수 있습니다.</li>
<li>단어는 최소 3쌍이 필요하며, 너무 많으면 한 판에 같은 단어를 다시 만나기 어렵습니다. 20~60개 정도가 반복 학습에 알맞습니다.</li>
</ul>

<h2 id="faq">8. 자주 묻는 질문</h2>
<h3>같은 뜻을 가진 단어가 여러 개면 어떻게 되나요?</h3>
<p>단어장 안에서 뜻이 똑같이 적힌 단어라면 그중 어느 것을 입력해도 정답으로 인정됩니다.</p>
<h3>비밀번호를 잊어버렸어요.</h3>
<p>비밀번호는 암호화되어 저장되기 때문에 운영자도 알 수 없습니다. <a href="/contact.html">문의</a>로 닉네임을 알려 주시면 계정 정리를 도와드립니다.</p>
<h3>모바일에서도 되나요?</h3>
<p>화면 키보드로도 플레이할 수 있지만, 빠르게 입력해야 하는 게임이라 PC 키보드 환경을 권장합니다.</p>
<p style="margin-top:24px"><a class="btn" href="/">게임 시작하기</a></p>
''')

# ---------------- 공부법 ----------------
page("study-tips.html", "영단어, 보는 것보다 꺼내 쓰는 연습이 중요한 이유", "영단어를 오래 기억하는 공부법: 인출 연습, 간격 반복, 직접 쓰며 철자 익히기, 틀린 단어 집중 복습, 좋은 단어장 만드는 요령과 하루 루틴 예시.", '''
<div class="hero"><div class="kicker">STUDY TIPS</div><h1>영단어, 보는 것보다<br>꺼내 쓰는 연습이 중요한 이유</h1>
<p>단어장을 여러 번 훑었는데도 시험장에서 단어가 떠오르지 않았다면, 공부 시간보다 공부 방식을 바꿔 볼 때입니다.</p></div>

<h2>1. ‘알아보는 것’과 ‘떠올리는 것’은 다르다</h2>
<p>단어장에서 <em>abandon — 버리다</em>를 보면 “아, 이거 알지” 하고 넘어가게 됩니다. 그런데 이것은 눈앞에 답이 있을 때 그것을 <strong>알아보는</strong> 능력입니다. 실제 시험이나 영작에서 필요한 것은 “버리다가 영어로 뭐였지?” 하고 머릿속에서 <strong>스스로 꺼내는</strong> 능력이고, 두 가지는 생각보다 차이가 큽니다.</p>
<p>그래서 단어를 오래 기억하려면 정답을 보기 전에 먼저 떠올려 보는 과정, 흔히 <strong>인출 연습</strong>이라고 부르는 과정을 공부 안에 넣어야 합니다. 뜻을 가리고 단어를 말해 보거나, 빈칸을 채우거나, 플래시카드를 넘기기 전에 답을 먼저 말하는 것이 모두 인출 연습입니다. 떠올리려고 애쓰는 순간이 조금 힘들게 느껴지는데, 바로 그 노력이 기억을 단단하게 만드는 부분입니다.</p>

<h2>2. 한 번에 몰아서 보다 나눠서 여러 번</h2>
<p>하루에 같은 단어 100개를 세 시간 동안 보는 것보다, 같은 시간을 사흘에 나눠 한 시간씩 보는 편이 오래 남습니다. 시간 간격을 두고 다시 만나면 약간 잊힌 상태에서 다시 떠올리게 되고, 그때 기억이 다시 강화되기 때문입니다. 이것을 <strong>간격 반복</strong>이라고 합니다.</p>
<p>실천하는 방법은 간단합니다. 오늘 외운 단어를 내일 한 번, 사흘 뒤 한 번, 일주일 뒤 한 번 다시 확인하는 식으로 간격을 점점 늘려 가면 됩니다. 매번 처음부터 다 외우려 하지 말고, “아직 기억나는지 확인한다”는 가벼운 마음으로 짧게 반복하는 것이 핵심입니다.</p>

<h2>3. 손으로 직접 쓰면 철자가 남는다</h2>
<p>눈으로만 본 단어는 뜻은 기억나도 철자가 헷갈리기 쉽습니다. <em>accommodate</em>에 c와 m이 몇 개였는지, <em>necessary</em>의 s가 어디서 겹치는지 같은 것들입니다. 단어를 직접 쓰거나 타이핑하면 글자 하나하나를 순서대로 만들어 내야 하므로 철자가 훨씬 정확하게 남습니다.</p>
<p>단어 요새가 객관식 선택이 아니라 <strong>직접 타이핑</strong> 방식인 것도 이 때문입니다. 한 글자라도 틀리면 몬스터가 쓰러지지 않으니, 철자를 대충 기억하던 단어가 금방 드러납니다.</p>

<h2>4. 틀린 단어에 시간을 더 쓴다</h2>
<p>이미 잘 아는 단어를 반복하면 기분은 좋지만 실력은 거의 늘지 않습니다. 공부 시간의 대부분은 <strong>헷갈리거나 틀린 단어</strong>에 써야 합니다. 시험을 본 뒤 오답 노트를 만들듯, 단어 공부도 매번 틀린 단어를 따로 모아 다음 복습의 출발점으로 삼으면 효율이 크게 오릅니다.</p>
<p>단어 요새에서는 게임이 끝날 때 요새까지 다가온, 즉 시간 안에 떠올리지 못한 단어가 ‘놓친 단어 복습’으로 정리됩니다. 그리고 다음 판에서는 그 단어들이 더 자주 등장합니다. 놓친 단어 목록을 한 번 소리 내어 읽고 바로 다음 판을 시작하는 것만으로도 자연스러운 오답 복습이 됩니다.</p>

<h2>5. 좋은 단어장 만드는 요령</h2>
<ul>
<li><strong>한 번에 20~60개</strong> — 너무 많으면 같은 단어를 다시 만나기까지 오래 걸려 반복 효과가 떨어집니다. 범위가 크면 단원이나 날짜별로 나눠 여러 단어장을 만드세요.</li>
<li><strong>뜻은 짧고 분명하게</strong> — “~을 포기하다, 버리다, 유기하다”처럼 길게 적기보다 가장 중요한 뜻 하나나 둘만 적는 편이 떠올리기 연습에 좋습니다.</li>
<li><strong>헷갈리는 단어는 함께</strong> — <em>adapt / adopt</em>, <em>affect / effect</em>처럼 비슷한 단어를 같은 단어장에 넣어 두면 차이를 확실히 구분하게 됩니다.</li>
<li><strong>뜻이 같은 단어는 똑같이 적기</strong> — 단어 요새에서는 뜻이 똑같이 적힌 단어끼리는 어느 것을 입력해도 정답으로 인정됩니다. 동의어를 함께 익히고 싶을 때 활용하세요.</li>
<li><strong>전공 용어도 좋다</strong> — 해부학, 병리학, 법률, 경제 용어처럼 영어 원어를 그대로 알아야 하는 분야라면 수업 자료의 용어를 그대로 옮겨 단어장으로 만들어 보세요.</li>
</ul>

<h2>6. 하루 20분 루틴 예시</h2>
<table>
<tr><th style="width:110px">시간</th><th>할 일</th></tr>
<tr><td>0~5분</td><td>어제 놓친 단어 목록을 소리 내어 한 번 읽기</td></tr>
<tr><td>5~15분</td><td>오늘 범위 단어장으로 게임 2~3판. 판이 끝날 때마다 놓친 단어 확인</td></tr>
<tr><td>15~20분</td><td>사흘 전·일주일 전 단어장으로 한 판씩 (간격 반복)</td></tr>
</table>
<p>매일 길게 하기보다 <strong>짧게, 자주, 떠올리면서</strong> 하는 것이 오래 가는 방법입니다. 스터디 친구들과 같은 단어장을 정해 명예의 전당 순위를 겨루면 꾸준히 이어 가는 데에도 도움이 됩니다.</p>

<div class="box tip"><strong>정리</strong><br>① 보기 전에 먼저 떠올린다 ② 간격을 두고 여러 번 만난다 ③ 직접 쳐서 철자까지 익힌다 ④ 틀린 단어에 시간을 쓴다 — 이 네 가지만 지켜도 같은 시간으로 훨씬 많은 단어를 오래 기억할 수 있습니다.</div>
<p style="margin-top:24px"><a class="btn" href="/">단어 요새로 연습하기</a> &nbsp; <a class="btn ghost" href="/books.html">공개 단어장 둘러보기</a></p>
''')

# ---------------- 공개 단어장 목록 ----------------
page("books.html", "공개 단어장", "단어 요새에 공개된 영단어 단어장 목록입니다. 이름이나 번호로 검색하고, 단어 목록을 미리 본 뒤 바로 플레이할 수 있습니다.", '''
<div class="hero"><div class="kicker">WORDBOOKS</div><h1>공개 단어장</h1>
<p>다른 사람들이 공개한 단어장입니다. 카드를 누르면 단어 목록과 명예의 전당을 볼 수 있고, 마음에 들면 바로 플레이할 수 있습니다.</p></div>
<input class="search" id="q" placeholder="단어장 이름, 만든 사람, 번호(예: 1001, #1001)로 검색">
<p class="muted small" id="info" style="margin-top:10px">불러오는 중…</p>
<div class="grid" id="list"></div>
<div class="box small muted">나만의 단어장을 만들려면 <a href="/">게임</a>에 입장한 뒤 개인 화면의 ‘+ 새로 만들기’를 누르세요. 공개로 저장하면 이 목록에 나타납니다.</div>
''', extra_js='''<script>
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
let t=null;
async function load(){
  const q=document.getElementById("q").value.trim();
  try{
    const r=await fetch("/api/books"+(q?"?q="+encodeURIComponent(q):""),{cache:"no-store"});const j=await r.json();
    const b=j.books||[];
    document.getElementById("info").textContent=b.length?`단어장 ${b.length}개`:"검색 결과가 없어요.";
    document.getElementById("list").innerHTML=b.map(x=>`<a class="card" href="/book.html?id=${encodeURIComponent(x.id)}"><span class="bdg">No.${x.no}</span>${x.builtin?'<span class="bdg g">기본 제공</span>':""}<h4>${esc(x.title)}</h4><p>${esc(x.desc||"")}</p><div class="meta">${esc(x.owner)} · ${x.count}단어 · ${x.plays||0}판</div></a>`).join("");
  }catch(e){document.getElementById("info").textContent="단어장 목록을 불러오지 못했어요. 잠시 후 다시 시도해 주세요."}
}
document.getElementById("q").addEventListener("input",()=>{clearTimeout(t);t=setTimeout(load,250)});
load();
</script>''')

# ---------------- 단어장 상세 ----------------
page("book.html", "단어장 보기", "단어 요새 공개 단어장의 단어 목록과 명예의 전당을 확인하고 바로 플레이할 수 있습니다.", '''
<div class="hero"><div class="kicker" id="kick">WORDBOOK</div><h1 id="ttl">단어장 불러오는 중…</h1><p id="desc"></p>
<p class="small muted" id="meta"></p>
<p id="acts" style="display:none;margin-top:14px"><a class="btn" id="play" href="/">이 단어장으로 플레이</a> &nbsp; <a class="btn ghost" href="/books.html">다른 단어장 보기</a></p></div>
<div id="err" class="box" style="display:none"></div>
<div id="content" style="display:none">
<h2>단어 목록</h2>
<input class="search" id="q" placeholder="단어 또는 뜻으로 찾기">
<table><thead><tr><th style="width:56px">#</th><th>영단어</th><th>뜻</th></tr></thead><tbody id="words"></tbody></table>
<h2>명예의 전당</h2>
<table><thead><tr><th style="width:56px">순위</th><th>닉네임</th><th>점수</th><th>스테이지</th></tr></thead><tbody id="hof"></tbody></table>
</div>
''', extra_js='''<script>
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const id=new URLSearchParams(location.search).get("id")||"";
let B=null;
function words(){const q=document.getElementById("q").value.trim().toLowerCase();
  document.getElementById("words").innerHTML=B.pairs.map((p,i)=>[i+1,p]).filter(([,p])=>!q||p.w.toLowerCase().includes(q)||p.m.toLowerCase().includes(q)).map(([i,p])=>`<tr><td class="muted">${i}</td><td><strong>${esc(p.w)}</strong></td><td>${esc(p.m)}</td></tr>`).join("")||'<tr><td colspan="3" class="muted">찾는 단어가 없어요</td></tr>'}
(async()=>{
  try{
    const r=await fetch("/api/book",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({id})});const j=await r.json();
    if(!r.ok||!j.book)throw new Error(j.error||"단어장을 찾을 수 없어요.");
    B=j.book;document.title=B.title+" | 단어 요새";
    document.getElementById("kick").textContent="WORDBOOK · No."+B.no;
    document.getElementById("ttl").textContent=B.title;
    document.getElementById("desc").textContent=B.desc||"";
    document.getElementById("meta").textContent=`만든 사람 ${B.owner} · ${B.pairs.length}단어 · ${B.plays||0}판 플레이`;
    document.getElementById("play").href="/?book="+encodeURIComponent(B.id);
    document.getElementById("acts").style.display="";document.getElementById("content").style.display="";
    words();document.getElementById("q").addEventListener("input",words);
    const h=await (await fetch("/api/hof?book="+encodeURIComponent(B.id),{cache:"no-store"})).json();
    const rows=(h.rows||[]).slice(0,20);
    document.getElementById("hof").innerHTML=rows.length?rows.map((x,i)=>`<tr><td>${i+1}</td><td>${esc(x.name)}</td><td><strong>${Number(x.score).toLocaleString()}</strong></td><td>STAGE ${esc(x.stage||1)}</td></tr>`).join(""):'<tr><td colspan="4" class="muted">아직 기록이 없어요. 첫 기록의 주인공이 되어 보세요!</td></tr>';
  }catch(e){document.getElementById("ttl").textContent="단어장을 찾을 수 없어요";const el=document.getElementById("err");el.style.display="";el.innerHTML=esc(e.message)+' <a href="/books.html">공개 단어장 목록으로</a>'}
})();
</script>''')

# ---------------- 개인정보처리방침 ----------------
page("privacy.html", "개인정보처리방침", "단어 요새가 수집하는 정보, 이용 목적, 보관 기간, 쿠키와 광고, 이용자 권리에 대한 안내입니다.", f'''
<div class="hero"><div class="kicker">PRIVACY</div><h1>개인정보처리방침</h1>
<p>단어 요새(이하 ‘서비스’)는 이용자의 개인정보를 소중히 여기며, 필요한 최소한의 정보만 다룹니다.</p>
<p class="small muted">시행일: 2026년 10월 30일</p></div>

<h2>1. 수집하는 정보</h2>
<table>
<tr><th style="width:170px">항목</th><th>내용</th></tr>
<tr><td>닉네임</td><td>입장 시 이용자가 정한 이름 (명예의 전당과 단어장 작성자로 공개됨)</td></tr>
<tr><td>비밀번호</td><td>입장 시 이용자가 정한 비밀번호. 원문은 저장하지 않으며, 되돌릴 수 없는 방식(암호화 해시)으로 바꾼 값만 저장합니다.</td></tr>
<tr><td>단어장</td><td>이용자가 만든 단어장의 이름, 설명, 단어 목록, 공개 여부</td></tr>
<tr><td>게임 기록</td><td>단어장별 점수, 도달 스테이지, 콤보, 정확도, 분당 타수, 플레이 시각</td></tr>
<tr><td>자동 생성 정보</td><td>서비스 이용 과정에서 브라우저 종류, 접속 시각, IP 주소 등 접속 기록이 호스팅 서버에 자동으로 남을 수 있습니다.</td></tr>
</table>
<p>서비스는 이름, 전화번호, 이메일 주소 등 실명 확인 정보를 수집하지 않습니다. 닉네임과 단어장에 실명이나 연락처 같은 개인정보를 적지 않도록 주의해 주세요.</p>

<h2>2. 이용 목적</h2>
<ul>
<li>닉네임 확인(로그인)과 다른 사람의 닉네임 도용 방지</li>
<li>단어장 저장·공유와 단어장별 명예의 전당 운영</li>
<li>서비스 오류 확인, 부정 이용 방지, 서비스 개선</li>
<li>광고 게재 (아래 4항 참고)</li>
</ul>

<h2>3. 보관 기간과 파기</h2>
<p>수집한 정보는 서비스를 운영하는 동안 보관하며, 이용자가 삭제를 요청하면 지체 없이 파기합니다. 단어장은 이용자가 직접 삭제할 수 있고, 닉네임과 게임 기록 삭제는 <a href="/contact.html">문의</a>로 요청할 수 있습니다. 서비스를 종료하는 경우 보관 중인 정보를 모두 파기합니다.</p>

<h2>4. 쿠키와 광고</h2>
<p>서비스는 운영비 마련을 위해 Google AdSense 등 제3자 광고 서비스를 이용할 수 있습니다.</p>
<ul>
<li>Google을 포함한 제3자 광고 사업자는 <strong>쿠키</strong>를 사용하여 이용자가 이 사이트나 다른 웹사이트를 방문한 기록을 바탕으로 광고를 게재할 수 있습니다.</li>
<li>Google은 광고 쿠키를 사용하여 이용자의 이 사이트 및 다른 사이트 방문 기록을 바탕으로 이용자와 관련성 높은 광고를 보여줄 수 있습니다.</li>
<li>이용자는 <a href="https://adssettings.google.com" rel="noopener" target="_blank">Google 광고 설정</a>에서 맞춤 광고를 끌 수 있으며, <a href="https://www.aboutads.info/choices" rel="noopener" target="_blank">www.aboutads.info</a>에서 제3자 사업자의 맞춤 광고용 쿠키 사용을 거부할 수 있습니다.</li>
<li>Google이 정보를 사용하는 방식은 <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">Google 파트너 사이트 정보 사용 방식</a>에서 확인할 수 있습니다.</li>
<li>대부분의 브라우저는 설정에서 쿠키 저장을 거부하거나 삭제할 수 있습니다. 쿠키를 거부해도 게임은 이용할 수 있으나, 일부 광고가 맞춤형으로 표시되지 않을 수 있습니다.</li>
</ul>

<h2>5. 브라우저 저장소 사용</h2>
<p>서비스는 편의를 위해 이용자의 브라우저 저장소(localStorage, sessionStorage)에 마지막으로 쓴 닉네임, 고른 단어장, 소리 설정을 저장합니다. 로그인 상태를 유지하기 위한 정보는 브라우저 탭을 닫으면 지워지는 sessionStorage에만 보관합니다. 서버에 연결할 수 없을 때에는 단어장과 기록이 이 기기의 브라우저 저장소에만 저장됩니다. 이 정보는 브라우저 설정에서 사이트 데이터를 삭제하면 지울 수 있습니다.</p>

<h2>6. 처리 위탁과 제3자 제공</h2>
<p>서비스는 수집한 정보를 제3자에게 판매하거나 제공하지 않습니다. 다만 서비스 운영을 위해 아래 업체의 인프라를 이용합니다.</p>
<table>
<tr><th style="width:170px">업체</th><th>위탁 업무</th></tr>
<tr><td>Netlify, Inc.</td><td>웹사이트 호스팅, 데이터(닉네임, 암호화된 비밀번호, 단어장, 게임 기록) 저장</td></tr>
<tr><td>Cloudflare, Inc.</td><td>도메인 이름 관리(DNS)</td></tr>
<tr><td>Google LLC</td><td>광고 게재(AdSense) 및 글꼴 제공(Google Fonts)</td></tr>
</table>
<p>위 업체의 서버는 해외에 있을 수 있습니다.</p>

<h2>7. 아동의 개인정보</h2>
<p>서비스는 실명이나 연락처를 수집하지 않으며, 만 14세 미만 아동의 개인정보를 의도적으로 수집하지 않습니다. 만 14세 미만 이용자는 보호자와 함께 이용해 주세요.</p>

<h2>8. 이용자의 권리</h2>
<p>이용자는 언제든지 자신의 정보에 대한 열람, 정정, 삭제를 요청할 수 있습니다. 요청은 아래 연락처로 닉네임과 함께 보내 주시면 확인 후 처리합니다.</p>

<h2>9. 문의처</h2>
<p>개인정보 관련 문의: <a href="mailto:{EMAIL}">{EMAIL}</a></p>

<h2>10. 방침 변경</h2>
<p>이 방침이 바뀌는 경우 시행 7일 전부터 이 페이지를 통해 알립니다.</p>
''')

# ---------------- 이용약관 ----------------
page("terms.html", "이용약관", "단어 요새 서비스 이용약관입니다.", f'''
<div class="hero"><div class="kicker">TERMS</div><h1>이용약관</h1><p class="small muted">시행일: 2026년 10월 30일</p></div>
<h2>제1조 (목적)</h2>
<p>이 약관은 단어 요새(이하 ‘서비스’)를 이용하는 데 필요한 조건과 절차, 이용자와 운영자의 권리·의무를 정합니다.</p>
<h2>제2조 (서비스 내용)</h2>
<p>서비스는 영단어 학습 게임, 단어장 작성·공유, 단어장별 명예의 전당을 무료로 제공합니다. 운영자는 서비스 개선을 위해 내용을 바꾸거나, 부득이한 경우 서비스를 중단할 수 있습니다.</p>
<h2>제3조 (계정)</h2>
<ul>
<li>이용자는 닉네임과 비밀번호를 정해 입장합니다. 비밀번호 관리 책임은 이용자에게 있으며, 다른 서비스에서 쓰는 비밀번호를 사용하지 않기를 권장합니다.</li>
<li>다른 사람을 사칭하거나 욕설·혐오 표현이 담긴 닉네임은 예고 없이 삭제될 수 있습니다.</li>
</ul>
<h2>제4조 (단어장과 게시물)</h2>
<ul>
<li>이용자가 만든 단어장의 권리와 책임은 작성자에게 있습니다.</li>
<li>공개로 저장한 단어장은 다른 이용자가 검색·열람·플레이하고, ‘복사해서 내 것으로’ 기능으로 복사해 쓸 수 있습니다. 이를 원하지 않으면 비공개로 저장해 주세요.</li>
<li>타인의 저작권을 침해하는 내용(교재·출판물 전체를 그대로 옮긴 경우 등), 개인정보, 불법·음란·혐오 내용을 담은 단어장은 운영자가 삭제할 수 있습니다.</li>
</ul>
<h2>제5조 (금지 행위)</h2>
<ul>
<li>프로그램 조작, 자동 입력 도구 사용, 서버 요청 변조 등으로 점수를 부정하게 기록하는 행위</li>
<li>서비스 운영을 방해하거나 서버에 과도한 부하를 주는 행위</li>
<li>광고를 부정하게 클릭하거나 다른 사람에게 클릭을 유도하는 행위</li>
</ul>
<p>위 행위가 확인되면 기록 삭제나 이용 제한 조치를 할 수 있습니다.</p>
<h2>제6조 (책임의 한계)</h2>
<p>서비스는 무료로 제공되며, 운영자는 서비스 이용으로 생긴 학습 결과나 데이터 손실에 대해 고의 또는 중대한 과실이 없는 한 책임지지 않습니다. 공개 단어장의 내용(뜻의 정확성 등)은 작성자가 책임집니다.</p>
<h2>제7조 (문의)</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
''')

# ---------------- 문의 ----------------
page("contact.html", "문의", "단어 요새 운영자에게 문의하는 방법입니다. 오류 신고, 계정·기록 삭제 요청, 단어장 신고, 제안을 이메일로 받습니다.", f'''
<div class="hero"><div class="kicker">CONTACT</div><h1>문의</h1>
<p>오류 신고, 계정·기록 삭제 요청, 부적절한 단어장 신고, 새 기능 제안 모두 환영합니다.</p></div>
<div class="box gold" style="font-size:18px">이메일: <a href="mailto:{EMAIL}"><strong>{EMAIL}</strong></a></div>
<h2>문의할 때 함께 알려 주세요</h2>
<table>
<tr><th style="width:170px">문의 종류</th><th>함께 보내 주시면 좋은 내용</th></tr>
<tr><td>오류 신고</td><td>사용한 기기와 브라우저(예: Windows / Chrome), 오류가 난 화면 캡처, 어떤 순서로 하다가 생겼는지</td></tr>
<tr><td>계정·기록 삭제</td><td>닉네임, 삭제를 원하는 범위(전체 / 특정 단어장 기록)</td></tr>
<tr><td>비밀번호 분실</td><td>닉네임, 그 닉네임으로 만든 단어장 번호(있다면)</td></tr>
<tr><td>단어장 신고</td><td>단어장 번호(예: No.1001)와 신고 사유</td></tr>
<tr><td>제안</td><td>원하는 기능이나 바뀌었으면 하는 점</td></tr>
</table>
<p class="muted">보통 3일 안에 답장드립니다. 개인정보 처리에 관한 내용은 <a href="/privacy.html">개인정보처리방침</a>을 참고해 주세요.</p>
''')

# ---------------- sitemap / robots ----------------
urls = ["", "guide.html", "books.html", "study-tips.html", "about.html", "contact.html", "privacy.html", "terms.html"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>2026-10-30</lastmod></url>\n" for u in urls) + "</urlset>\n"
open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /api/\n\nSitemap: {SITE}/sitemap.xml\n")
print("ok")
