/* 단어 요새 — 광고 설정
 * Google AdSense 승인 전에는 아무것도 하지 않습니다 (광고 자리도 보이지 않음).
 * 승인 후: client에 게시자 ID(ca-pub-로 시작), slots에 광고 단위 ID를 넣으면 광고가 켜집니다.
 * 같은 때에 public/ads.txt 파일도 만들어야 합니다 (README 참고).
 */
window.WF_ADS = {
  client: "ca-pub-6022643424246082",
  slots: {
    content: "",         // 안내 페이지 본문 아래
    lobby: "",           // 게임 개인 화면
    over: ""             // 게임 오버 화면
  }
};
(function () {
  var cfg = window.WF_ADS;
  if (!cfg.client) return;
  var s = document.createElement("script");
  s.async = true;
  s.crossOrigin = "anonymous";
  s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + encodeURIComponent(cfg.client);
  document.head.appendChild(s);
  cfg.fill = function (root) {
    (root || document).querySelectorAll(".ad-slot[data-slot]").forEach(function (el) {
      var id = cfg.slots[el.dataset.slot];
      if (!id || el.dataset.filled) return;
      el.dataset.filled = "1";
      el.innerHTML = '<ins class="adsbygoogle" style="display:block" data-ad-client="' + cfg.client + '" data-ad-slot="' + id + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { cfg.fill(); });
  else cfg.fill();
})();
