(function () {
  // Only run over http(s) at the site root — skip when opened as a local file.
  if (window.location.protocol === "file:") return;
  var SKIP_KEY = "umco_region_choice";
  var manualSwitch = sessionStorage.getItem(SKIP_KEY);
  sessionStorage.removeItem(SKIP_KEY);
  var isUS = window.location.pathname.indexOf("/us/") === 0 || window.location.pathname === "/us";

  function otherPath() {
    var path = window.location.pathname;
    if (isUS) {
      return path.replace(/^\/us(\/|$)/, "/");
    }
    return "/us" + path;
  }

  function attachToggleLinks() {
    document.querySelectorAll(".region-toggle-link").forEach(function (link) {
      link.addEventListener("click", function () {
        sessionStorage.setItem(SKIP_KEY, isUS ? "PK" : "US");
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", attachToggleLinks);
  } else {
    attachToggleLinks();
  }

  if (manualSwitch) return;

  fetch("https://ipwho.is/")
    .then(function (res) { return res.json(); })
    .then(function (data) {
      if (!data || !data.country_code) return;
      // Pakistan gets the PK version; every other country defaults to the US version.
      var wantsUS = data.country_code !== "PK";
      if (wantsUS !== isUS) {
        window.location.replace(otherPath());
      }
    })
    .catch(function () {});
})();
