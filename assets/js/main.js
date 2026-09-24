(function () {
  "use strict";

  var cfg = window.CD_CONFIG || {};
  var GA_ID = cfg.ga4Id || "";

  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  function track(name, params) {
    params = params || {};
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(Object.assign({ event: name }, params));
    if (typeof window.gtag === "function") {
      window.gtag("event", name, params);
    }
  }

  function loadGA4() {
    if (!GA_ID || document.getElementById("cd-ga4")) return;
    var s = document.createElement("script");
    s.async = true;
    s.id = "cd-ga4";
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA_ID);
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", GA_ID, { anonymize_ip: true });
  }

  ready(function () {
    loadGA4();

    var toggle = document.querySelector(".menu-toggle");
    var links = document.querySelector(".nav-links");
    if (toggle && links) {
      toggle.addEventListener("click", function () {
        var open = links.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
      links.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", function () {
          links.classList.remove("open");
          toggle.setAttribute("aria-expanded", "false");
        });
      });
    }

    document.querySelectorAll("[data-track]").forEach(function (el) {
      el.addEventListener("click", function () {
        track(el.getAttribute("data-track"), {
          location: el.getAttribute("data-track-location") || "site"
        });
      });
    });

    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!reduce && "IntersectionObserver" in window) {
      document.documentElement.classList.add("motion");
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
      document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
    }

    var filterBar = document.querySelector("[data-kc-filters]");
    if (filterBar) {
      filterBar.addEventListener("click", function (e) {
        var btn = e.target.closest("[data-filter]");
        if (!btn) return;
        var cat = btn.getAttribute("data-filter");
        filterBar.querySelectorAll("[data-filter]").forEach(function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        document.querySelectorAll("[data-cat]").forEach(function (el) {
          el.hidden = cat !== "all" && el.getAttribute("data-cat") !== cat;
        });
      });
    }

    var params = new URLSearchParams(window.location.search);
    if (params.get("intent") === "demo") {
      document.querySelectorAll("form[data-enquiry]").forEach(function (form) {
        form.setAttribute("data-enquiry", "demo_request");
        var subject = form.querySelector('input[name="_subject"]');
        var type = form.querySelector('input[name="form_type"]');
        if (subject) subject.value = "Consultation request | Cyber Developers";
        if (type) type.value = "consultation_request";
        var headingBtn = form.querySelector('button[type="submit"]');
        if (headingBtn) headingBtn.textContent = "Request a Consultation";
      });
    }

    document.querySelectorAll("form[data-enquiry]").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        var error = form.querySelector(".form-error");
        var hp = form.querySelector('input[name="website"]');
        if (hp && hp.value) {
          e.preventDefault();
          return;
        }

        var name = (form.querySelector('[name="name"]') || {}).value || "";
        var email = (form.querySelector('[name="email"]') || {}).value || "";
        var desc = (form.querySelector('[name="project_description"], [name="message"]') || {}).value || "";
        if (name.trim().length < 2 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || desc.trim().length < 10) {
          e.preventDefault();
          if (error) {
            error.textContent = "Please add your name, a valid email address, and a short project description.";
            error.classList.add("show");
          }
          return;
        }

        var key = "cd-form-ts";
        var last = Number(sessionStorage.getItem(key) || 0);
        if (Date.now() - last < 20000) {
          e.preventDefault();
          if (error) {
            error.textContent = "Please wait a moment before sending another enquiry.";
            error.classList.add("show");
          }
          return;
        }
        sessionStorage.setItem(key, String(Date.now()));

        var kind = form.getAttribute("data-enquiry") || "project_enquiry";
        track(kind, { form_id: form.getAttribute("id") || "enquiry" });
        if (kind === "demo_request") track("demo_requested");
        if (kind === "consultation_request") track("consultation_requested");
        track("project_enquiry_submitted");
      });
    });
  });
})();
