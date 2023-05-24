
document.addEventListener("DOMContentLoaded", () => {
	class TabController {
	 constructor(tabId) {
		let tab = document.querySelector(tabId),
		 tabs = tab.querySelectorAll("li a[class^='nav-link']"),
		 tabPanes = tab.querySelectorAll("div.tab-pane"),
     links = tab.querySelectorAll("a[class^='edit_property_button']"),
     btnId = 0,
		 currentTab = 0;

		// we'll need 4 different functions to do this
		showTab(currentTab);
    setButtonHandlers();

		function showTab(n) {
		 hideAllTabsAndTabPanes(n);

		 tabs[n].classList.add("active");
		 tabs[n].classList.add("show");
		 tabPanes[n].classList.add("active");
		 tabPanes[n].classList.add("show");

     currentTab = n;
		}

		function hideAllTabsAndTabPanes(n) {
		 for (let i = 0; i < tabs.length; i++) {
      tabs[i].classList.remove("active");
      tabs[i].classList.remove("show");
      tabPanes[i].classList.remove("active");
      tabPanes[i].classList.remove("show");
		 }
		}
    function setButtonHandlers() {
      for (let i = 0; i < links.length; i++) {
        links[i].addEventListener('click', (e) => {
          e.preventDefault();
        }); 
      }
    }

	 }
	}
	let TC = new TabController("#dash-tab");
 });

