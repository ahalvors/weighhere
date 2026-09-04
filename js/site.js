(function () {
  var btn = document.querySelector(".menu-toggle");
  var nav = document.querySelector("nav.site-nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  var filterBar = document.querySelector("[data-filters]");
  if (filterBar) {
    filterBar.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-filter]");
      if (!b) return;
      var key = b.getAttribute("data-filter");
      filterBar.querySelectorAll("button").forEach(function (x) {
        x.setAttribute("aria-pressed", x === b ? "true" : "false");
      });
      document.querySelectorAll("[data-rig]").forEach(function (card) {
        var rigs = (card.getAttribute("data-rig") || "").split(/\s+/);
        var show = key === "all" || rigs.indexOf(key) !== -1;
        card.classList.toggle("hidden", !show);
      });
      document.querySelectorAll("[data-filter-section]").forEach(function (sec) {
        var visible = sec.querySelectorAll("[data-rig]:not(.hidden)").length;
        sec.hidden = visible === 0;
      });
    });
  }

  var mapEl = document.getElementById("map");
  if (mapEl && window.L && window.WEIGHHERE_POINTS) {
    var pts = window.WEIGHHERE_POINTS.filter(function (p) {
      return typeof p.lat === "number" && typeof p.lng === "number";
    });
    if (!pts.length) return;
    var map = L.map(mapEl, { scrollWheelZoom: false });
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "&copy; OpenStreetMap",
      maxZoom: 18
    }).addTo(map);
    var colors = {
      dedicated_public: "#0d3b2a",
      cat: "#c4a035",
      truck_stop: "#1546a0",
      landfill: "#6b4708",
      quarry: "#6b4708",
      industrial: "#555",
      recycling: "#555",
      mill: "#6b4708",
      enforcement: "#8e1515"
    };
    var group = [];
    pts.forEach(function (p) {
      var c = colors[p.type] || "#111";
      var m = L.circleMarker([p.lat, p.lng], {
        radius: p.type === "enforcement" ? 8 : 6,
        color: "#111",
        weight: 1,
        fillColor: c,
        fillOpacity: 0.9
      }).addTo(map);
      m.bindPopup("<strong>" + p.name + "</strong><br>" + (p.city || "") +
        (p.type === "enforcement" ? "<br>Do not go here for a ticket." : ""));
      group.push(m);
    });
    var g = L.featureGroup(group);
    map.fitBounds(g.getBounds().pad(0.18));
  }
})();
